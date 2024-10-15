# SNMP MIB module (DES-1210-28ME_B2) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DES-1210-28ME_B2
# Produced by pysmi-1.5.4 at Mon Oct 14 21:24:23 2024
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
_Dlink_DES1210SeriesProd_ObjectIdentity = ObjectIdentity
dlink_DES1210SeriesProd = _Dlink_DES1210SeriesProd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 75)
)
_Des_1210_28ME_ObjectIdentity = ObjectIdentity
des_1210_28ME = _Des_1210_28ME_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15)
)
_Des_1210_28ME_B2_ObjectIdentity = ObjectIdentity
des_1210_28ME_B2 = _Des_1210_28ME_B2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2)
)
_CompanySystem_ObjectIdentity = ObjectIdentity
companySystem = _CompanySystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 1)
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 1, 8),
    _SysSafeGuardEnable_Type()
)
sysSafeGuardEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSafeGuardEnable.setStatus("current")


class _SysRestart_Type(TruthValue):
    """Custom type sysRestart based on TruthValue"""


_SysRestart_Object = MibScalar
sysRestart = _SysRestart_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 1, 9),
    _SysRestart_Type()
)
sysRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysRestart.setStatus("current")


class _SysSave_Type(TruthValue):
    """Custom type sysSave based on TruthValue"""


_SysSave_Object = MibScalar
sysSave = _SysSave_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 1, 10),
    _SysSave_Type()
)
sysSave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSave.setStatus("current")
_SysPortCtrlTable_Object = MibTable
sysPortCtrlTable = _SysPortCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 1, 13)
)
if mibBuilder.loadTexts:
    sysPortCtrlTable.setStatus("current")
_SysPortCtrlEntry_Object = MibTableRow
sysPortCtrlEntry = _SysPortCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 1, 13, 1)
)
sysPortCtrlEntry.setIndexNames(
    (0, "DES-1210-28ME_B2", "sysPortCtrlIndex"),
    (0, "DES-1210-28ME_B2", "sysPortCtrlMediumType"),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 1, 13, 1, 1),
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
              101,
              102)
        )
    )
    namedValues = NamedValues(
        *(("copper", 100),
          ("fiber100M", 102),
          ("fiber1G", 101))
    )


_SysPortCtrlMediumType_Type.__name__ = "Integer32"
_SysPortCtrlMediumType_Object = MibTableColumn
sysPortCtrlMediumType = _SysPortCtrlMediumType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 1, 13, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 1, 13, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 1, 13, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 1, 13, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 1, 13, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 1, 13, 1, 7),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 1, 13, 1, 8),
    _SysPortCtrlType_Type()
)
sysPortCtrlType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysPortCtrlType.setStatus("current")
_SysPortDescriptionTable_Object = MibTable
sysPortDescriptionTable = _SysPortDescriptionTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 1, 14)
)
if mibBuilder.loadTexts:
    sysPortDescriptionTable.setStatus("current")
_SysPortDescriptionEntry_Object = MibTableRow
sysPortDescriptionEntry = _SysPortDescriptionEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 1, 14, 1)
)
sysPortDescriptionEntry.setIndexNames(
    (0, "DES-1210-28ME_B2", "sysPortDescIndex"),
    (0, "DES-1210-28ME_B2", "sysPortDescMediumType"),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 1, 14, 1, 1),
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
              101,
              102)
        )
    )
    namedValues = NamedValues(
        *(("copper", 100),
          ("fiber100M", 102),
          ("fiber1G", 101))
    )


_SysPortDescMediumType_Type.__name__ = "Integer32"
_SysPortDescMediumType_Object = MibTableColumn
sysPortDescMediumType = _SysPortDescMediumType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 1, 14, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 1, 14, 1, 3),
    _SysPortDescString_Type()
)
sysPortDescString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysPortDescString.setStatus("current")
_SysPortErrTable_Object = MibTable
sysPortErrTable = _SysPortErrTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 1, 15)
)
if mibBuilder.loadTexts:
    sysPortErrTable.setStatus("current")
_SysPortErrEntry_Object = MibTableRow
sysPortErrEntry = _SysPortErrEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 1, 15, 1)
)
sysPortErrEntry.setIndexNames(
    (0, "DES-1210-28ME_B2", "sysPortErrPortIndex"),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 1, 15, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 1, 15, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 1, 15, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 1, 15, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 1, 16),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 1, 17),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 1, 18),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 1, 19),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 1, 20),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 1, 23),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 1, 24),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 1, 25),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 1, 26),
    _FloodfdbOnOff_Type()
)
floodfdbOnOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    floodfdbOnOff.setStatus("current")
_CompanyIpifGroup_ObjectIdentity = ObjectIdentity
companyIpifGroup = _CompanyIpifGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 2)
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 2, 1),
    _SysIpAddrCfgMode_Type()
)
sysIpAddrCfgMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysIpAddrCfgMode.setStatus("current")
_SysIpAddr_Type = IpAddress
_SysIpAddr_Object = MibScalar
sysIpAddr = _SysIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 2, 2),
    _SysIpAddr_Type()
)
sysIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysIpAddr.setStatus("current")
_SysIpSubnetMask_Type = IpAddress
_SysIpSubnetMask_Object = MibScalar
sysIpSubnetMask = _SysIpSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 2, 3),
    _SysIpSubnetMask_Type()
)
sysIpSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysIpSubnetMask.setStatus("current")
_SysGateway_Type = IpAddress
_SysGateway_Object = MibScalar
sysGateway = _SysGateway_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 2, 4),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 2, 5),
    _DhcpOption12Status_Type()
)
dhcpOption12Status.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpOption12Status.setStatus("current")
_DhcpOption12HostName_Type = OctetString
_DhcpOption12HostName_Object = MibScalar
dhcpOption12HostName = _DhcpOption12HostName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 2, 6),
    _DhcpOption12HostName_Type()
)
dhcpOption12HostName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpOption12HostName.setStatus("current")
_CompanyTftpGroup_ObjectIdentity = ObjectIdentity
companyTftpGroup = _CompanyTftpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 3)
)
_TftpFwServerIpAddress_Type = IpAddress
_TftpFwServerIpAddress_Object = MibScalar
tftpFwServerIpAddress = _TftpFwServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 3, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 3, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 3, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 3, 4),
    _TftpFwTftpOperationStatus_Type()
)
tftpFwTftpOperationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tftpFwTftpOperationStatus.setStatus("current")
_TftpCfgServerIpAddress_Type = IpAddress
_TftpCfgServerIpAddress_Object = MibScalar
tftpCfgServerIpAddress = _TftpCfgServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 3, 5),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 3, 6),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 3, 7),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 3, 8),
    _TftpConfigTftpOperationStatus_Type()
)
tftpConfigTftpOperationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tftpConfigTftpOperationStatus.setStatus("current")
_CompanyMiscGroup_ObjectIdentity = ObjectIdentity
companyMiscGroup = _CompanyMiscGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 4)
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 4, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 4, 3),
    _MiscStatisticsReset_Type()
)
miscStatisticsReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    miscStatisticsReset.setStatus("current")
_CompanySNMPV3_ObjectIdentity = ObjectIdentity
companySNMPV3 = _CompanySNMPV3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 5)
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 5, 1),
    _SnmpGlobalState_Type()
)
snmpGlobalState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpGlobalState.setStatus("current")
_SnmpV3User_ObjectIdentity = ObjectIdentity
snmpV3User = _SnmpV3User_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 5, 2)
)
_SnmpV3UserTable_Object = MibTable
snmpV3UserTable = _SnmpV3UserTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 5, 2, 1)
)
if mibBuilder.loadTexts:
    snmpV3UserTable.setStatus("current")
_SnmpV3UserEntry_Object = MibTableRow
snmpV3UserEntry = _SnmpV3UserEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 5, 2, 1, 1)
)
snmpV3UserEntry.setIndexNames(
    (0, "DES-1210-28ME_B2", "snmpV3UserName"),
    (0, "DES-1210-28ME_B2", "snmpV3UserVersion"),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 5, 2, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 5, 2, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 5, 2, 1, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 5, 2, 1, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 5, 2, 1, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 5, 2, 1, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 5, 2, 1, 1, 7),
    _SnmpV3UserPrivProtocolPassword_Type()
)
snmpV3UserPrivProtocolPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpV3UserPrivProtocolPassword.setStatus("current")
_SnmpV3UserStatus_Type = RowStatus
_SnmpV3UserStatus_Object = MibTableColumn
snmpV3UserStatus = _SnmpV3UserStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 5, 2, 1, 1, 8),
    _SnmpV3UserStatus_Type()
)
snmpV3UserStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpV3UserStatus.setStatus("current")
_SnmpV3Group_ObjectIdentity = ObjectIdentity
snmpV3Group = _SnmpV3Group_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 5, 3)
)
_SnmpV3GroupTable_Object = MibTable
snmpV3GroupTable = _SnmpV3GroupTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 5, 3, 1)
)
if mibBuilder.loadTexts:
    snmpV3GroupTable.setStatus("current")
_SnmpV3GroupEntry_Object = MibTableRow
snmpV3GroupEntry = _SnmpV3GroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 5, 3, 1, 1)
)
snmpV3GroupEntry.setIndexNames(
    (0, "DES-1210-28ME_B2", "snmpV3GroupName"),
    (0, "DES-1210-28ME_B2", "snmpV3GroupSecurityModel"),
    (0, "DES-1210-28ME_B2", "snmpV3GroupSecurityLevel"),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 5, 3, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 5, 3, 1, 1, 2),
    _SnmpV3GroupSecurityModel_Type()
)
snmpV3GroupSecurityModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpV3GroupSecurityModel.setStatus("current")
_SnmpV3GroupSecurityLevel_Type = SnmpSecurityLevel
_SnmpV3GroupSecurityLevel_Object = MibTableColumn
snmpV3GroupSecurityLevel = _SnmpV3GroupSecurityLevel_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 5, 3, 1, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 5, 3, 1, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 5, 3, 1, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 5, 3, 1, 1, 6),
    _SnmpV3GroupNotifyViewName_Type()
)
snmpV3GroupNotifyViewName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpV3GroupNotifyViewName.setStatus("current")
_SnmpV3GroupStatus_Type = RowStatus
_SnmpV3GroupStatus_Object = MibTableColumn
snmpV3GroupStatus = _SnmpV3GroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 5, 3, 1, 1, 7),
    _SnmpV3GroupStatus_Type()
)
snmpV3GroupStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpV3GroupStatus.setStatus("current")
_SnmpV3ViewTree_ObjectIdentity = ObjectIdentity
snmpV3ViewTree = _SnmpV3ViewTree_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 5, 4)
)
_SnmpV3ViewTreeTable_Object = MibTable
snmpV3ViewTreeTable = _SnmpV3ViewTreeTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 5, 4, 1)
)
if mibBuilder.loadTexts:
    snmpV3ViewTreeTable.setStatus("current")
_SnmpV3ViewTreeEntry_Object = MibTableRow
snmpV3ViewTreeEntry = _SnmpV3ViewTreeEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 5, 4, 1, 1)
)
snmpV3ViewTreeEntry.setIndexNames(
    (0, "DES-1210-28ME_B2", "snmpV3viewTreeName"),
    (0, "DES-1210-28ME_B2", "snmpV3viewTreeSubtree"),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 5, 4, 1, 1, 1),
    _SnmpV3viewTreeName_Type()
)
snmpV3viewTreeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpV3viewTreeName.setStatus("current")
_SnmpV3viewTreeSubtree_Type = ObjectIdentifier
_SnmpV3viewTreeSubtree_Object = MibTableColumn
snmpV3viewTreeSubtree = _SnmpV3viewTreeSubtree_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 5, 4, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 5, 4, 1, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 5, 4, 1, 1, 4),
    _SnmpV3viewTreeType_Type()
)
snmpV3viewTreeType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpV3viewTreeType.setStatus("current")
_SnmpV3viewTreeStatus_Type = RowStatus
_SnmpV3viewTreeStatus_Object = MibTableColumn
snmpV3viewTreeStatus = _SnmpV3viewTreeStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 5, 4, 1, 1, 5),
    _SnmpV3viewTreeStatus_Type()
)
snmpV3viewTreeStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpV3viewTreeStatus.setStatus("current")
_SnmpV3Community_ObjectIdentity = ObjectIdentity
snmpV3Community = _SnmpV3Community_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 5, 5)
)
_SnmpV3CommunityTable_Object = MibTable
snmpV3CommunityTable = _SnmpV3CommunityTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 5, 5, 1)
)
if mibBuilder.loadTexts:
    snmpV3CommunityTable.setStatus("current")
_SnmpV3CommunityEntry_Object = MibTableRow
snmpV3CommunityEntry = _SnmpV3CommunityEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 5, 5, 1, 1)
)
snmpV3CommunityEntry.setIndexNames(
    (0, "DES-1210-28ME_B2", "snmpV3CommunityName"),
)
if mibBuilder.loadTexts:
    snmpV3CommunityEntry.setStatus("current")
_SnmpV3CommunityName_Type = OctetString
_SnmpV3CommunityName_Object = MibTableColumn
snmpV3CommunityName = _SnmpV3CommunityName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 5, 5, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 5, 5, 1, 1, 2),
    _SnmpV3CommunityPolicy_Type()
)
snmpV3CommunityPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpV3CommunityPolicy.setStatus("current")
_SnmpV3CommunityStatus_Type = RowStatus
_SnmpV3CommunityStatus_Object = MibTableColumn
snmpV3CommunityStatus = _SnmpV3CommunityStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 5, 5, 1, 1, 3),
    _SnmpV3CommunityStatus_Type()
)
snmpV3CommunityStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpV3CommunityStatus.setStatus("current")
_SnmpV3Host_ObjectIdentity = ObjectIdentity
snmpV3Host = _SnmpV3Host_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 5, 6)
)
_SnmpV3HostTable_Object = MibTable
snmpV3HostTable = _SnmpV3HostTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 5, 6, 1)
)
if mibBuilder.loadTexts:
    snmpV3HostTable.setStatus("current")
_SnmpV3HostEntry_Object = MibTableRow
snmpV3HostEntry = _SnmpV3HostEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 5, 6, 1, 1)
)
snmpV3HostEntry.setIndexNames(
    (0, "DES-1210-28ME_B2", "snmpV3HostAddress"),
)
if mibBuilder.loadTexts:
    snmpV3HostEntry.setStatus("current")
_SnmpV3HostAddress_Type = IpAddress
_SnmpV3HostAddress_Object = MibTableColumn
snmpV3HostAddress = _SnmpV3HostAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 5, 6, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 5, 6, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 5, 6, 1, 1, 3),
    _SnmpV3HostVersion_Type()
)
snmpV3HostVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpV3HostVersion.setStatus("current")
_SnmpV3HostStatus_Type = RowStatus
_SnmpV3HostStatus_Object = MibTableColumn
snmpV3HostStatus = _SnmpV3HostStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 5, 6, 1, 1, 4),
    _SnmpV3HostStatus_Type()
)
snmpV3HostStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpV3HostStatus.setStatus("current")
_SnmpV3EngineID_Type = SnmpEngineID
_SnmpV3EngineID_Object = MibScalar
snmpV3EngineID = _SnmpV3EngineID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 5, 7),
    _SnmpV3EngineID_Type()
)
snmpV3EngineID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpV3EngineID.setStatus("current")
_SnmpV3Trap_ObjectIdentity = ObjectIdentity
snmpV3Trap = _SnmpV3Trap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 5, 8)
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 5, 8, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 5, 8, 2),
    _SnmpV3TrapBootup_Type()
)
snmpV3TrapBootup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpV3TrapBootup.setStatus("current")


class _SnmpV3TrapFiberLinkUpDown_Type(Integer32):
    """Custom type snmpV3TrapFiberLinkUpDown based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SnmpV3TrapFiberLinkUpDown_Type.__name__ = "Integer32"
_SnmpV3TrapFiberLinkUpDown_Object = MibScalar
snmpV3TrapFiberLinkUpDown = _SnmpV3TrapFiberLinkUpDown_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 5, 8, 3),
    _SnmpV3TrapFiberLinkUpDown_Type()
)
snmpV3TrapFiberLinkUpDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpV3TrapFiberLinkUpDown.setStatus("current")


class _SnmpV3TrapCopperLinkUpDown_Type(Integer32):
    """Custom type snmpV3TrapCopperLinkUpDown based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SnmpV3TrapCopperLinkUpDown_Type.__name__ = "Integer32"
_SnmpV3TrapCopperLinkUpDown_Object = MibScalar
snmpV3TrapCopperLinkUpDown = _SnmpV3TrapCopperLinkUpDown_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 5, 8, 4),
    _SnmpV3TrapCopperLinkUpDown_Type()
)
snmpV3TrapCopperLinkUpDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpV3TrapCopperLinkUpDown.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 5, 8, 5),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 5, 8, 6),
    _SnmpV3TrapFirmUpgrade_Type()
)
snmpV3TrapFirmUpgrade.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpV3TrapFirmUpgrade.setStatus("current")


class _SnmpV3TrapBPDUAttack_Type(Integer32):
    """Custom type snmpV3TrapBPDUAttack based on Integer32"""
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
        *(("attackCleared", 3),
          ("attackDetected", 2),
          ("both", 4),
          ("none", 1))
    )


_SnmpV3TrapBPDUAttack_Type.__name__ = "Integer32"
_SnmpV3TrapBPDUAttack_Object = MibScalar
snmpV3TrapBPDUAttack = _SnmpV3TrapBPDUAttack_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 5, 8, 11),
    _SnmpV3TrapBPDUAttack_Type()
)
snmpV3TrapBPDUAttack.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpV3TrapBPDUAttack.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 5, 8, 12),
    _SnmpV3TrapPortSecurity_Type()
)
snmpV3TrapPortSecurity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpV3TrapPortSecurity.setStatus("current")


class _SnmpV3TrapIMPBViolation_Type(Integer32):
    """Custom type snmpV3TrapIMPBViolation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SnmpV3TrapIMPBViolation_Type.__name__ = "Integer32"
_SnmpV3TrapIMPBViolation_Object = MibScalar
snmpV3TrapIMPBViolation = _SnmpV3TrapIMPBViolation_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 5, 8, 13),
    _SnmpV3TrapIMPBViolation_Type()
)
snmpV3TrapIMPBViolation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpV3TrapIMPBViolation.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 5, 8, 14),
    _SnmpV3TrapLBD_Type()
)
snmpV3TrapLBD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpV3TrapLBD.setStatus("current")


class _SnmpV3TrapDHCPServerScreening_Type(Integer32):
    """Custom type snmpV3TrapDHCPServerScreening based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SnmpV3TrapDHCPServerScreening_Type.__name__ = "Integer32"
_SnmpV3TrapDHCPServerScreening_Object = MibScalar
snmpV3TrapDHCPServerScreening = _SnmpV3TrapDHCPServerScreening_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 5, 8, 15),
    _SnmpV3TrapDHCPServerScreening_Type()
)
snmpV3TrapDHCPServerScreening.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpV3TrapDHCPServerScreening.setStatus("current")


class _SnmpV3TrapDuplicateIPDetected_Type(Integer32):
    """Custom type snmpV3TrapDuplicateIPDetected based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SnmpV3TrapDuplicateIPDetected_Type.__name__ = "Integer32"
_SnmpV3TrapDuplicateIPDetected_Object = MibScalar
snmpV3TrapDuplicateIPDetected = _SnmpV3TrapDuplicateIPDetected_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 5, 8, 16),
    _SnmpV3TrapDuplicateIPDetected_Type()
)
snmpV3TrapDuplicateIPDetected.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpV3TrapDuplicateIPDetected.setStatus("current")
_CompanySTP_ObjectIdentity = ObjectIdentity
companySTP = _CompanySTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 6)
)
_StpBridgeGlobal_ObjectIdentity = ObjectIdentity
stpBridgeGlobal = _StpBridgeGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 6, 1)
)


class _StpModuleStatus_Type(Integer32):
    """Custom type stpModuleStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_StpModuleStatus_Type.__name__ = "Integer32"
_StpModuleStatus_Object = MibScalar
stpModuleStatus = _StpModuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 6, 1, 1),
    _StpModuleStatus_Type()
)
stpModuleStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpModuleStatus.setStatus("current")


class _StpProtocolVersion_Type(Integer32):
    """Custom type stpProtocolVersion based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mstp", 3),
          ("rstp", 2),
          ("stp", 0))
    )


_StpProtocolVersion_Type.__name__ = "Integer32"
_StpProtocolVersion_Object = MibScalar
stpProtocolVersion = _StpProtocolVersion_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 6, 1, 2),
    _StpProtocolVersion_Type()
)
stpProtocolVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpProtocolVersion.setStatus("current")


class _StpBridgePriority_Type(Integer32):
    """Custom type stpBridgePriority based on Integer32"""
    defaultValue = 32768

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 61440),
    )


_StpBridgePriority_Type.__name__ = "Integer32"
_StpBridgePriority_Object = MibScalar
stpBridgePriority = _StpBridgePriority_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 6, 1, 3),
    _StpBridgePriority_Type()
)
stpBridgePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpBridgePriority.setStatus("current")


class _StpTxHoldCount_Type(Integer32):
    """Custom type stpTxHoldCount based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_StpTxHoldCount_Type.__name__ = "Integer32"
_StpTxHoldCount_Object = MibScalar
stpTxHoldCount = _StpTxHoldCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 6, 1, 4),
    _StpTxHoldCount_Type()
)
stpTxHoldCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpTxHoldCount.setStatus("current")


class _StpBridgeMaxAge_Type(Timeout):
    """Custom type stpBridgeMaxAge based on Timeout"""
    defaultValue = 2000

    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(600, 4000),
    )


_StpBridgeMaxAge_Type.__name__ = "Timeout"
_StpBridgeMaxAge_Object = MibScalar
stpBridgeMaxAge = _StpBridgeMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 6, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 6, 1, 6),
    _StpBridgeHelloTime_Type()
)
stpBridgeHelloTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpBridgeHelloTime.setStatus("current")


class _StpBridgeForwardDelay_Type(Timeout):
    """Custom type stpBridgeForwardDelay based on Timeout"""
    defaultValue = 1500

    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(400, 3000),
    )


_StpBridgeForwardDelay_Type.__name__ = "Timeout"
_StpBridgeForwardDelay_Object = MibScalar
stpBridgeForwardDelay = _StpBridgeForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 6, 1, 7),
    _StpBridgeForwardDelay_Type()
)
stpBridgeForwardDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpBridgeForwardDelay.setStatus("current")


class _StpFowardBPDU_Type(Integer32):
    """Custom type stpFowardBPDU based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_StpFowardBPDU_Type.__name__ = "Integer32"
_StpFowardBPDU_Object = MibScalar
stpFowardBPDU = _StpFowardBPDU_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 6, 1, 8),
    _StpFowardBPDU_Type()
)
stpFowardBPDU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpFowardBPDU.setStatus("current")
_StpRootBridge_Type = BridgeId
_StpRootBridge_Object = MibScalar
stpRootBridge = _StpRootBridge_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 6, 1, 9),
    _StpRootBridge_Type()
)
stpRootBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpRootBridge.setStatus("current")
_StpRootCost_Type = Integer32
_StpRootCost_Object = MibScalar
stpRootCost = _StpRootCost_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 6, 1, 10),
    _StpRootCost_Type()
)
stpRootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpRootCost.setStatus("current")
_StpMaxAge_Type = Timeout
_StpMaxAge_Object = MibScalar
stpMaxAge = _StpMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 6, 1, 11),
    _StpMaxAge_Type()
)
stpMaxAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpMaxAge.setStatus("current")
_StpForwardDelay_Type = Timeout
_StpForwardDelay_Object = MibScalar
stpForwardDelay = _StpForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 6, 1, 12),
    _StpForwardDelay_Type()
)
stpForwardDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpForwardDelay.setStatus("current")
_StpRootPort_Type = Integer32
_StpRootPort_Object = MibScalar
stpRootPort = _StpRootPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 6, 1, 13),
    _StpRootPort_Type()
)
stpRootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpRootPort.setStatus("current")
_StpPortTable_Object = MibTable
stpPortTable = _StpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 6, 2)
)
if mibBuilder.loadTexts:
    stpPortTable.setStatus("current")
_StpPortEntry_Object = MibTableRow
stpPortEntry = _StpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 6, 2, 1)
)
stpPortEntry.setIndexNames(
    (0, "DES-1210-28ME_B2", "stpPort"),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 6, 2, 1, 1),
    _StpPort_Type()
)
stpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpPort.setStatus("current")


class _StpPortStatus_Type(Integer32):
    """Custom type stpPortStatus based on Integer32"""
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


_StpPortStatus_Type.__name__ = "Integer32"
_StpPortStatus_Object = MibTableColumn
stpPortStatus = _StpPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 6, 2, 1, 2),
    _StpPortStatus_Type()
)
stpPortStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpPortStatus.setStatus("current")


class _StpPortPriority_Type(Integer32):
    """Custom type stpPortPriority based on Integer32"""
    defaultValue = 128

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_StpPortPriority_Type.__name__ = "Integer32"
_StpPortPriority_Object = MibTableColumn
stpPortPriority = _StpPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 6, 2, 1, 3),
    _StpPortPriority_Type()
)
stpPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpPortPriority.setStatus("current")


class _StpAdminPortPathCost_Type(Integer32):
    """Custom type stpAdminPortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_StpAdminPortPathCost_Type.__name__ = "Integer32"
_StpAdminPortPathCost_Object = MibTableColumn
stpAdminPortPathCost = _StpAdminPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 6, 2, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 6, 2, 1, 5),
    _StpPortPathCost_Type()
)
stpPortPathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpPortPathCost.setStatus("current")
_StpPortProtocolMigration_Type = TruthValue
_StpPortProtocolMigration_Object = MibTableColumn
stpPortProtocolMigration = _StpPortProtocolMigration_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 6, 2, 1, 6),
    _StpPortProtocolMigration_Type()
)
stpPortProtocolMigration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpPortProtocolMigration.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 6, 2, 1, 7),
    _StpPortEdge_Type()
)
stpPortEdge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpPortEdge.setStatus("current")


class _StpPortAdminP2P_Type(Integer32):
    """Custom type stpPortAdminP2P based on Integer32"""
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


_StpPortAdminP2P_Type.__name__ = "Integer32"
_StpPortAdminP2P_Object = MibTableColumn
stpPortAdminP2P = _StpPortAdminP2P_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 6, 2, 1, 8),
    _StpPortAdminP2P_Type()
)
stpPortAdminP2P.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpPortAdminP2P.setStatus("current")
_StpPortRestrictedRole_Type = TruthValue
_StpPortRestrictedRole_Object = MibTableColumn
stpPortRestrictedRole = _StpPortRestrictedRole_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 6, 2, 1, 9),
    _StpPortRestrictedRole_Type()
)
stpPortRestrictedRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpPortRestrictedRole.setStatus("current")
_StpPortRestrictedTCN_Type = TruthValue
_StpPortRestrictedTCN_Object = MibTableColumn
stpPortRestrictedTCN = _StpPortRestrictedTCN_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 6, 2, 1, 10),
    _StpPortRestrictedTCN_Type()
)
stpPortRestrictedTCN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpPortRestrictedTCN.setStatus("current")


class _StpPortHelloTime_Type(Timeout):
    """Custom type stpPortHelloTime based on Timeout"""
    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000),
    )


_StpPortHelloTime_Type.__name__ = "Timeout"
_StpPortHelloTime_Object = MibTableColumn
stpPortHelloTime = _StpPortHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 6, 2, 1, 11),
    _StpPortHelloTime_Type()
)
stpPortHelloTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpPortHelloTime.setStatus("current")


class _StpPortState_Type(Integer32):
    """Custom type stpPortState based on Integer32"""
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
        *(("disabled", 1),
          ("discarding", 2),
          ("forwarding", 5),
          ("learning", 4))
    )


_StpPortState_Type.__name__ = "Integer32"
_StpPortState_Object = MibTableColumn
stpPortState = _StpPortState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 6, 2, 1, 12),
    _StpPortState_Type()
)
stpPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpPortState.setStatus("current")


class _StpPortFowardBPDU_Type(Integer32):
    """Custom type stpPortFowardBPDU based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_StpPortFowardBPDU_Type.__name__ = "Integer32"
_StpPortFowardBPDU_Object = MibTableColumn
stpPortFowardBPDU = _StpPortFowardBPDU_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 6, 2, 1, 13),
    _StpPortFowardBPDU_Type()
)
stpPortFowardBPDU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpPortFowardBPDU.setStatus("current")
_MstConfigurationIdentification_ObjectIdentity = ObjectIdentity
mstConfigurationIdentification = _MstConfigurationIdentification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 6, 3)
)


class _MstiConfigurationName_Type(OctetString):
    """Custom type mstiConfigurationName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MstiConfigurationName_Type.__name__ = "OctetString"
_MstiConfigurationName_Object = MibScalar
mstiConfigurationName = _MstiConfigurationName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 6, 3, 1),
    _MstiConfigurationName_Type()
)
mstiConfigurationName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mstiConfigurationName.setStatus("current")


class _MstiRevisionLevel_Type(Integer32):
    """Custom type mstiRevisionLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MstiRevisionLevel_Type.__name__ = "Integer32"
_MstiRevisionLevel_Object = MibScalar
mstiRevisionLevel = _MstiRevisionLevel_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 6, 3, 2),
    _MstiRevisionLevel_Type()
)
mstiRevisionLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mstiRevisionLevel.setStatus("current")


class _MstCistVlanMapped_Type(OctetString):
    """Custom type mstCistVlanMapped based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_MstCistVlanMapped_Type.__name__ = "OctetString"
_MstCistVlanMapped_Object = MibScalar
mstCistVlanMapped = _MstCistVlanMapped_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 6, 3, 3),
    _MstCistVlanMapped_Type()
)
mstCistVlanMapped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstCistVlanMapped.setStatus("current")


class _MstCistVlanMapped2k_Type(OctetString):
    """Custom type mstCistVlanMapped2k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_MstCistVlanMapped2k_Type.__name__ = "OctetString"
_MstCistVlanMapped2k_Object = MibScalar
mstCistVlanMapped2k = _MstCistVlanMapped2k_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 6, 3, 4),
    _MstCistVlanMapped2k_Type()
)
mstCistVlanMapped2k.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstCistVlanMapped2k.setStatus("current")


class _MstCistVlanMapped3k_Type(OctetString):
    """Custom type mstCistVlanMapped3k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_MstCistVlanMapped3k_Type.__name__ = "OctetString"
_MstCistVlanMapped3k_Object = MibScalar
mstCistVlanMapped3k = _MstCistVlanMapped3k_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 6, 3, 5),
    _MstCistVlanMapped3k_Type()
)
mstCistVlanMapped3k.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstCistVlanMapped3k.setStatus("current")


class _MstCistVlanMapped4k_Type(OctetString):
    """Custom type mstCistVlanMapped4k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_MstCistVlanMapped4k_Type.__name__ = "OctetString"
_MstCistVlanMapped4k_Object = MibScalar
mstCistVlanMapped4k = _MstCistVlanMapped4k_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 6, 3, 6),
    _MstCistVlanMapped4k_Type()
)
mstCistVlanMapped4k.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstCistVlanMapped4k.setStatus("current")
_MstVlanMstiMappingTable_Object = MibTable
mstVlanMstiMappingTable = _MstVlanMstiMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 6, 3, 7)
)
if mibBuilder.loadTexts:
    mstVlanMstiMappingTable.setStatus("current")
_MstVlanMstiMappingEntry_Object = MibTableRow
mstVlanMstiMappingEntry = _MstVlanMstiMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 6, 3, 7, 1)
)
mstVlanMstiMappingEntry.setIndexNames(
    (0, "DES-1210-28ME_B2", "mstInstanceIndex"),
)
if mibBuilder.loadTexts:
    mstVlanMstiMappingEntry.setStatus("current")


class _MstInstanceIndex_Type(Integer32):
    """Custom type mstInstanceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_MstInstanceIndex_Type.__name__ = "Integer32"
_MstInstanceIndex_Object = MibTableColumn
mstInstanceIndex = _MstInstanceIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 6, 3, 7, 1, 1),
    _MstInstanceIndex_Type()
)
mstInstanceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstInstanceIndex.setStatus("current")


class _MstSetVlanList_Type(OctetString):
    """Custom type mstSetVlanList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_MstSetVlanList_Type.__name__ = "OctetString"
_MstSetVlanList_Object = MibTableColumn
mstSetVlanList = _MstSetVlanList_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 6, 3, 7, 1, 2),
    _MstSetVlanList_Type()
)
mstSetVlanList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mstSetVlanList.setStatus("current")


class _MstResetVlanList_Type(OctetString):
    """Custom type mstResetVlanList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_MstResetVlanList_Type.__name__ = "OctetString"
_MstResetVlanList_Object = MibTableColumn
mstResetVlanList = _MstResetVlanList_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 6, 3, 7, 1, 3),
    _MstResetVlanList_Type()
)
mstResetVlanList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mstResetVlanList.setStatus("current")


class _MstInstanceVlanMapped_Type(OctetString):
    """Custom type mstInstanceVlanMapped based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_MstInstanceVlanMapped_Type.__name__ = "OctetString"
_MstInstanceVlanMapped_Object = MibTableColumn
mstInstanceVlanMapped = _MstInstanceVlanMapped_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 6, 3, 7, 1, 4),
    _MstInstanceVlanMapped_Type()
)
mstInstanceVlanMapped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstInstanceVlanMapped.setStatus("current")


class _MstInstanceVlanMapped2k_Type(OctetString):
    """Custom type mstInstanceVlanMapped2k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_MstInstanceVlanMapped2k_Type.__name__ = "OctetString"
_MstInstanceVlanMapped2k_Object = MibTableColumn
mstInstanceVlanMapped2k = _MstInstanceVlanMapped2k_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 6, 3, 7, 1, 5),
    _MstInstanceVlanMapped2k_Type()
)
mstInstanceVlanMapped2k.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstInstanceVlanMapped2k.setStatus("current")


class _MstInstanceVlanMapped3k_Type(OctetString):
    """Custom type mstInstanceVlanMapped3k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_MstInstanceVlanMapped3k_Type.__name__ = "OctetString"
_MstInstanceVlanMapped3k_Object = MibTableColumn
mstInstanceVlanMapped3k = _MstInstanceVlanMapped3k_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 6, 3, 7, 1, 6),
    _MstInstanceVlanMapped3k_Type()
)
mstInstanceVlanMapped3k.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstInstanceVlanMapped3k.setStatus("current")


class _MstInstanceVlanMapped4k_Type(OctetString):
    """Custom type mstInstanceVlanMapped4k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_MstInstanceVlanMapped4k_Type.__name__ = "OctetString"
_MstInstanceVlanMapped4k_Object = MibTableColumn
mstInstanceVlanMapped4k = _MstInstanceVlanMapped4k_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 6, 3, 7, 1, 7),
    _MstInstanceVlanMapped4k_Type()
)
mstInstanceVlanMapped4k.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstInstanceVlanMapped4k.setStatus("current")
_StpInstance_ObjectIdentity = ObjectIdentity
stpInstance = _StpInstance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 6, 4)
)


class _MstCistBridgePriority_Type(Integer32):
    """Custom type mstCistBridgePriority based on Integer32"""
    defaultValue = 32768

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 61440),
    )


_MstCistBridgePriority_Type.__name__ = "Integer32"
_MstCistBridgePriority_Object = MibScalar
mstCistBridgePriority = _MstCistBridgePriority_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 6, 4, 1),
    _MstCistBridgePriority_Type()
)
mstCistBridgePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mstCistBridgePriority.setStatus("current")


class _MstCistStatus_Type(Integer32):
    """Custom type mstCistStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_MstCistStatus_Type.__name__ = "Integer32"
_MstCistStatus_Object = MibScalar
mstCistStatus = _MstCistStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 6, 4, 2),
    _MstCistStatus_Type()
)
mstCistStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstCistStatus.setStatus("current")
_MstMstiBridgeTable_Object = MibTable
mstMstiBridgeTable = _MstMstiBridgeTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 6, 4, 3)
)
if mibBuilder.loadTexts:
    mstMstiBridgeTable.setStatus("current")
_MstMstiBridgeEntry_Object = MibTableRow
mstMstiBridgeEntry = _MstMstiBridgeEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 6, 4, 3, 1)
)
mstMstiBridgeEntry.setIndexNames(
    (0, "DES-1210-28ME_B2", "mstMstiInstanceIndex"),
)
if mibBuilder.loadTexts:
    mstMstiBridgeEntry.setStatus("current")


class _MstMstiInstanceIndex_Type(Integer32):
    """Custom type mstMstiInstanceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_MstMstiInstanceIndex_Type.__name__ = "Integer32"
_MstMstiInstanceIndex_Object = MibTableColumn
mstMstiInstanceIndex = _MstMstiInstanceIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 6, 4, 3, 1, 1),
    _MstMstiInstanceIndex_Type()
)
mstMstiInstanceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstMstiInstanceIndex.setStatus("current")


class _MstMstiBridgePriority_Type(Integer32):
    """Custom type mstMstiBridgePriority based on Integer32"""
    defaultValue = 32768

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 61440),
    )


_MstMstiBridgePriority_Type.__name__ = "Integer32"
_MstMstiBridgePriority_Object = MibTableColumn
mstMstiBridgePriority = _MstMstiBridgePriority_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 6, 4, 3, 1, 2),
    _MstMstiBridgePriority_Type()
)
mstMstiBridgePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mstMstiBridgePriority.setStatus("current")


class _MstMstiStatus_Type(Integer32):
    """Custom type mstMstiStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_MstMstiStatus_Type.__name__ = "Integer32"
_MstMstiStatus_Object = MibTableColumn
mstMstiStatus = _MstMstiStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 6, 4, 3, 1, 3),
    _MstMstiStatus_Type()
)
mstMstiStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstMstiStatus.setStatus("current")
_StpInstancePortTable_ObjectIdentity = ObjectIdentity
stpInstancePortTable = _StpInstancePortTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 6, 5)
)
_MstCistPortTable_Object = MibTable
mstCistPortTable = _MstCistPortTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 6, 5, 1)
)
if mibBuilder.loadTexts:
    mstCistPortTable.setStatus("current")
_MstCistPortEntry_Object = MibTableRow
mstCistPortEntry = _MstCistPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 6, 5, 1, 1)
)
mstCistPortEntry.setIndexNames(
    (0, "DES-1210-28ME_B2", "mstCistPort"),
)
if mibBuilder.loadTexts:
    mstCistPortEntry.setStatus("current")


class _MstCistPort_Type(Integer32):
    """Custom type mstCistPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MstCistPort_Type.__name__ = "Integer32"
_MstCistPort_Object = MibTableColumn
mstCistPort = _MstCistPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 6, 5, 1, 1, 1),
    _MstCistPort_Type()
)
mstCistPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mstCistPort.setStatus("current")
_MstCistPortDesignatedBridge_Type = BridgeId
_MstCistPortDesignatedBridge_Object = MibTableColumn
mstCistPortDesignatedBridge = _MstCistPortDesignatedBridge_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 6, 5, 1, 1, 2),
    _MstCistPortDesignatedBridge_Type()
)
mstCistPortDesignatedBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstCistPortDesignatedBridge.setStatus("current")


class _MstCistPortAdminPathCost_Type(Integer32):
    """Custom type mstCistPortAdminPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_MstCistPortAdminPathCost_Type.__name__ = "Integer32"
_MstCistPortAdminPathCost_Object = MibTableColumn
mstCistPortAdminPathCost = _MstCistPortAdminPathCost_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 6, 5, 1, 1, 3),
    _MstCistPortAdminPathCost_Type()
)
mstCistPortAdminPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mstCistPortAdminPathCost.setStatus("current")


class _MstCistPortPathCost_Type(Integer32):
    """Custom type mstCistPortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200000000),
    )


_MstCistPortPathCost_Type.__name__ = "Integer32"
_MstCistPortPathCost_Object = MibTableColumn
mstCistPortPathCost = _MstCistPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 6, 5, 1, 1, 4),
    _MstCistPortPathCost_Type()
)
mstCistPortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mstCistPortPathCost.setStatus("current")


class _MstCistPortPriority_Type(Integer32):
    """Custom type mstCistPortPriority based on Integer32"""
    defaultValue = 128

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_MstCistPortPriority_Type.__name__ = "Integer32"
_MstCistPortPriority_Object = MibTableColumn
mstCistPortPriority = _MstCistPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 6, 5, 1, 1, 5),
    _MstCistPortPriority_Type()
)
mstCistPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mstCistPortPriority.setStatus("current")


class _MstCistForcePortState_Type(Integer32):
    """Custom type mstCistForcePortState based on Integer32"""
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


_MstCistForcePortState_Type.__name__ = "Integer32"
_MstCistForcePortState_Object = MibTableColumn
mstCistForcePortState = _MstCistForcePortState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 6, 5, 1, 1, 6),
    _MstCistForcePortState_Type()
)
mstCistForcePortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstCistForcePortState.setStatus("current")


class _MstCistCurrentPortRole_Type(Integer32):
    """Custom type mstCistCurrentPortRole based on Integer32"""
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
        *(("alternate", 1),
          ("backup", 2),
          ("designated", 4),
          ("disabled", 0),
          ("master", 5),
          ("root", 3))
    )


_MstCistCurrentPortRole_Type.__name__ = "Integer32"
_MstCistCurrentPortRole_Object = MibTableColumn
mstCistCurrentPortRole = _MstCistCurrentPortRole_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 6, 5, 1, 1, 7),
    _MstCistCurrentPortRole_Type()
)
mstCistCurrentPortRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstCistCurrentPortRole.setStatus("current")
_MstMstiPortTable_Object = MibTable
mstMstiPortTable = _MstMstiPortTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 6, 5, 2)
)
if mibBuilder.loadTexts:
    mstMstiPortTable.setStatus("current")
_MstMstiPortEntry_Object = MibTableRow
mstMstiPortEntry = _MstMstiPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 6, 5, 2, 1)
)
mstMstiPortEntry.setIndexNames(
    (0, "DES-1210-28ME_B2", "mstMstiPort"),
    (0, "DES-1210-28ME_B2", "mstInstanceIndex"),
)
if mibBuilder.loadTexts:
    mstMstiPortEntry.setStatus("current")


class _MstMstiPort_Type(Integer32):
    """Custom type mstMstiPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MstMstiPort_Type.__name__ = "Integer32"
_MstMstiPort_Object = MibTableColumn
mstMstiPort = _MstMstiPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 6, 5, 2, 1, 1),
    _MstMstiPort_Type()
)
mstMstiPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mstMstiPort.setStatus("current")
_MstMstiPortDesignatedBridge_Type = BridgeId
_MstMstiPortDesignatedBridge_Object = MibTableColumn
mstMstiPortDesignatedBridge = _MstMstiPortDesignatedBridge_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 6, 5, 2, 1, 2),
    _MstMstiPortDesignatedBridge_Type()
)
mstMstiPortDesignatedBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstMstiPortDesignatedBridge.setStatus("current")


class _MstMstiPortAdminPathCost_Type(Integer32):
    """Custom type mstMstiPortAdminPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_MstMstiPortAdminPathCost_Type.__name__ = "Integer32"
_MstMstiPortAdminPathCost_Object = MibTableColumn
mstMstiPortAdminPathCost = _MstMstiPortAdminPathCost_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 6, 5, 2, 1, 3),
    _MstMstiPortAdminPathCost_Type()
)
mstMstiPortAdminPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mstMstiPortAdminPathCost.setStatus("current")


class _MstMstiPortPathCost_Type(Integer32):
    """Custom type mstMstiPortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200000000),
    )


_MstMstiPortPathCost_Type.__name__ = "Integer32"
_MstMstiPortPathCost_Object = MibTableColumn
mstMstiPortPathCost = _MstMstiPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 6, 5, 2, 1, 4),
    _MstMstiPortPathCost_Type()
)
mstMstiPortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mstMstiPortPathCost.setStatus("current")


class _MstMstiPortPriority_Type(Integer32):
    """Custom type mstMstiPortPriority based on Integer32"""
    defaultValue = 128

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_MstMstiPortPriority_Type.__name__ = "Integer32"
_MstMstiPortPriority_Object = MibTableColumn
mstMstiPortPriority = _MstMstiPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 6, 5, 2, 1, 5),
    _MstMstiPortPriority_Type()
)
mstMstiPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mstMstiPortPriority.setStatus("current")


class _MstMstiForcePortState_Type(Integer32):
    """Custom type mstMstiForcePortState based on Integer32"""
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


_MstMstiForcePortState_Type.__name__ = "Integer32"
_MstMstiForcePortState_Object = MibTableColumn
mstMstiForcePortState = _MstMstiForcePortState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 6, 5, 2, 1, 6),
    _MstMstiForcePortState_Type()
)
mstMstiForcePortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstMstiForcePortState.setStatus("current")


class _MstMstiCurrentPortRole_Type(Integer32):
    """Custom type mstMstiCurrentPortRole based on Integer32"""
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
        *(("alternate", 1),
          ("backup", 2),
          ("designated", 4),
          ("disabled", 0),
          ("master", 5),
          ("root", 3))
    )


_MstMstiCurrentPortRole_Type.__name__ = "Integer32"
_MstMstiCurrentPortRole_Object = MibTableColumn
mstMstiCurrentPortRole = _MstMstiCurrentPortRole_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 6, 5, 2, 1, 7),
    _MstMstiCurrentPortRole_Type()
)
mstMstiCurrentPortRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstMstiCurrentPortRole.setStatus("current")
_CompanyDot1qVlanGroup_ObjectIdentity = ObjectIdentity
companyDot1qVlanGroup = _CompanyDot1qVlanGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 7)
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 7, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 7, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 7, 5),
    _Dot1qVlanAsyOnOff_Type()
)
dot1qVlanAsyOnOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1qVlanAsyOnOff.setStatus("current")
_Dot1qVlanTable_Object = MibTable
dot1qVlanTable = _Dot1qVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 7, 6)
)
if mibBuilder.loadTexts:
    dot1qVlanTable.setStatus("current")
_Dot1qVlanEntry_Object = MibTableRow
dot1qVlanEntry = _Dot1qVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 7, 6, 1)
)
dot1qVlanEntry.setIndexNames(
    (0, "DES-1210-28ME_B2", "dot1qVlanName"),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 7, 6, 1, 1),
    _Dot1qVlanName_Type()
)
dot1qVlanName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1qVlanName.setStatus("current")
_Dot1qVlanEgressPorts_Type = PortList
_Dot1qVlanEgressPorts_Object = MibTableColumn
dot1qVlanEgressPorts = _Dot1qVlanEgressPorts_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 7, 6, 1, 2),
    _Dot1qVlanEgressPorts_Type()
)
dot1qVlanEgressPorts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1qVlanEgressPorts.setStatus("current")
_Dot1qVlanForbiddenPorts_Type = PortList
_Dot1qVlanForbiddenPorts_Object = MibTableColumn
dot1qVlanForbiddenPorts = _Dot1qVlanForbiddenPorts_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 7, 6, 1, 3),
    _Dot1qVlanForbiddenPorts_Type()
)
dot1qVlanForbiddenPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1qVlanForbiddenPorts.setStatus("current")
_Dot1qVlanUntaggedPorts_Type = PortList
_Dot1qVlanUntaggedPorts_Object = MibTableColumn
dot1qVlanUntaggedPorts = _Dot1qVlanUntaggedPorts_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 7, 6, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 7, 6, 1, 5),
    _Dot1qVlanAdvertisementStatus_Type()
)
dot1qVlanAdvertisementStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1qVlanAdvertisementStatus.setStatus("current")
_Dot1qVlanRowStatus_Type = RowStatus
_Dot1qVlanRowStatus_Object = MibTableColumn
dot1qVlanRowStatus = _Dot1qVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 7, 6, 1, 6),
    _Dot1qVlanRowStatus_Type()
)
dot1qVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1qVlanRowStatus.setStatus("current")
_CompanyLA_ObjectIdentity = ObjectIdentity
companyLA = _CompanyLA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 8)
)
_LaSystem_ObjectIdentity = ObjectIdentity
laSystem = _LaSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 8, 1)
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 8, 1, 2),
    _LaStatus_Type()
)
laStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    laStatus.setStatus("current")
_LaPortChannelTable_Object = MibTable
laPortChannelTable = _LaPortChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 8, 1, 3)
)
if mibBuilder.loadTexts:
    laPortChannelTable.setStatus("current")
_LaPortChannelEntry_Object = MibTableRow
laPortChannelEntry = _LaPortChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 8, 1, 3, 1)
)
laPortChannelEntry.setIndexNames(
    (0, "DES-1210-28ME_B2", "laPortChannelIfIndex"),
)
if mibBuilder.loadTexts:
    laPortChannelEntry.setStatus("current")
_LaPortChannelIfIndex_Type = InterfaceIndex
_LaPortChannelIfIndex_Object = MibTableColumn
laPortChannelIfIndex = _LaPortChannelIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 8, 1, 3, 1, 1),
    _LaPortChannelIfIndex_Type()
)
laPortChannelIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    laPortChannelIfIndex.setStatus("current")
_LaPortChannelMemberList_Type = PortList
_LaPortChannelMemberList_Object = MibTableColumn
laPortChannelMemberList = _LaPortChannelMemberList_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 8, 1, 3, 1, 2),
    _LaPortChannelMemberList_Type()
)
laPortChannelMemberList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    laPortChannelMemberList.setStatus("current")
_LaPortChannelMode_Type = PortLaMode
_LaPortChannelMode_Object = MibTableColumn
laPortChannelMode = _LaPortChannelMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 8, 1, 3, 1, 3),
    _LaPortChannelMode_Type()
)
laPortChannelMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    laPortChannelMode.setStatus("current")
_LaPortChannelMasterPort_Type = InterfaceIndex
_LaPortChannelMasterPort_Object = MibTableColumn
laPortChannelMasterPort = _LaPortChannelMasterPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 8, 1, 3, 1, 4),
    _LaPortChannelMasterPort_Type()
)
laPortChannelMasterPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    laPortChannelMasterPort.setStatus("current")


class _LaAlgorithm_Type(Integer32):
    """Custom type laAlgorithm based on Integer32"""
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
        *(("destIP", 5),
          ("destMAC", 2),
          ("sourceAndDestIP", 6),
          ("sourceAndDestMAC", 3),
          ("sourceIP", 4),
          ("sourceMAC", 1))
    )


_LaAlgorithm_Type.__name__ = "Integer32"
_LaAlgorithm_Object = MibScalar
laAlgorithm = _LaAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 8, 1, 4),
    _LaAlgorithm_Type()
)
laAlgorithm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    laAlgorithm.setStatus("current")
_LaPortControl_ObjectIdentity = ObjectIdentity
laPortControl = _LaPortControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 8, 2)
)
_LaPortControlTable_Object = MibTable
laPortControlTable = _LaPortControlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 8, 2, 1)
)
if mibBuilder.loadTexts:
    laPortControlTable.setStatus("current")
_LaPortControlEntry_Object = MibTableRow
laPortControlEntry = _LaPortControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 8, 2, 1, 1)
)
laPortControlEntry.setIndexNames(
    (0, "DES-1210-28ME_B2", "laPortControlIndex"),
)
if mibBuilder.loadTexts:
    laPortControlEntry.setStatus("current")
_LaPortControlIndex_Type = InterfaceIndex
_LaPortControlIndex_Object = MibTableColumn
laPortControlIndex = _LaPortControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 8, 2, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 8, 2, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 8, 2, 1, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 8, 2, 1, 1, 4),
    _LaPortActorTimeout_Type()
)
laPortActorTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    laPortActorTimeout.setStatus("current")
_CompanyStaticMAC_ObjectIdentity = ObjectIdentity
companyStaticMAC = _CompanyStaticMAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 9)
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 9, 1),
    _StaticDisableAutoLearn_Type()
)
staticDisableAutoLearn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticDisableAutoLearn.setStatus("current")
_StaticAutoLearningList_Type = PortList
_StaticAutoLearningList_Object = MibScalar
staticAutoLearningList = _StaticAutoLearningList_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 9, 2),
    _StaticAutoLearningList_Type()
)
staticAutoLearningList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticAutoLearningList.setStatus("current")
_StaticTable_Object = MibTable
staticTable = _StaticTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 9, 3)
)
if mibBuilder.loadTexts:
    staticTable.setStatus("current")
_StaticEntry_Object = MibTableRow
staticEntry = _StaticEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 9, 3, 1)
)
staticEntry.setIndexNames(
    (0, "DES-1210-28ME_B2", "staticVlanID"),
    (0, "DES-1210-28ME_B2", "staticMac"),
    (0, "DES-1210-28ME_B2", "staticPort"),
)
if mibBuilder.loadTexts:
    staticEntry.setStatus("current")
_StaticVlanID_Type = Integer32
_StaticVlanID_Object = MibTableColumn
staticVlanID = _StaticVlanID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 9, 3, 1, 1),
    _StaticVlanID_Type()
)
staticVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staticVlanID.setStatus("current")
_StaticMac_Type = MacAddress
_StaticMac_Object = MibTableColumn
staticMac = _StaticMac_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 9, 3, 1, 2),
    _StaticMac_Type()
)
staticMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staticMac.setStatus("current")
_StaticPort_Type = Integer32
_StaticPort_Object = MibTableColumn
staticPort = _StaticPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 9, 3, 1, 3),
    _StaticPort_Type()
)
staticPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staticPort.setStatus("current")
_StaticStatus_Type = RowStatus
_StaticStatus_Object = MibTableColumn
staticStatus = _StaticStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 9, 3, 1, 4),
    _StaticStatus_Type()
)
staticStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticStatus.setStatus("current")
_CompanyIgsGroup_ObjectIdentity = ObjectIdentity
companyIgsGroup = _CompanyIgsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 10)
)
_IgsSystem_ObjectIdentity = ObjectIdentity
igsSystem = _IgsSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 10, 1)
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 10, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 10, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 10, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 10, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 10, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 10, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 10, 1, 7),
    _IgsQueryMaxResponseTime_Type()
)
igsQueryMaxResponseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igsQueryMaxResponseTime.setStatus("current")


class _IgsDataDrivenLearningMaxLearnedEntryVlaue_Type(Integer32):
    """Custom type igsDataDrivenLearningMaxLearnedEntryVlaue based on Integer32"""
    defaultValue = 64

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_IgsDataDrivenLearningMaxLearnedEntryVlaue_Type.__name__ = "Integer32"
_IgsDataDrivenLearningMaxLearnedEntryVlaue_Object = MibScalar
igsDataDrivenLearningMaxLearnedEntryVlaue = _IgsDataDrivenLearningMaxLearnedEntryVlaue_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 10, 1, 8),
    _IgsDataDrivenLearningMaxLearnedEntryVlaue_Type()
)
igsDataDrivenLearningMaxLearnedEntryVlaue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igsDataDrivenLearningMaxLearnedEntryVlaue.setStatus("current")
_IgsVlan_ObjectIdentity = ObjectIdentity
igsVlan = _IgsVlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 10, 3)
)
_IgsVlanRouterTable_Object = MibTable
igsVlanRouterTable = _IgsVlanRouterTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 10, 3, 3)
)
if mibBuilder.loadTexts:
    igsVlanRouterTable.setStatus("current")
_IgsVlanRouterEntry_Object = MibTableRow
igsVlanRouterEntry = _IgsVlanRouterEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 10, 3, 3, 1)
)
igsVlanRouterEntry.setIndexNames(
    (0, "DES-1210-28ME_B2", "igsVlanRouterVlanId"),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 10, 3, 3, 1, 1),
    _IgsVlanRouterVlanId_Type()
)
igsVlanRouterVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igsVlanRouterVlanId.setStatus("current")
_IgsVlanRouterPortList_Type = PortList
_IgsVlanRouterPortList_Object = MibTableColumn
igsVlanRouterPortList = _IgsVlanRouterPortList_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 10, 3, 3, 1, 2),
    _IgsVlanRouterPortList_Type()
)
igsVlanRouterPortList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igsVlanRouterPortList.setStatus("current")
_IgsVlanFilterTable_Object = MibTable
igsVlanFilterTable = _IgsVlanFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 10, 3, 4)
)
if mibBuilder.loadTexts:
    igsVlanFilterTable.setStatus("current")
_IgsVlanFilterEntry_Object = MibTableRow
igsVlanFilterEntry = _IgsVlanFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 10, 3, 4, 1)
)
igsVlanFilterEntry.setIndexNames(
    (0, "DES-1210-28ME_B2", "igsVlanFilterVlanId"),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 10, 3, 4, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 10, 3, 4, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 10, 3, 4, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 10, 3, 4, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 10, 3, 4, 1, 5),
    _IgsVlanQueryInterval_Type()
)
igsVlanQueryInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igsVlanQueryInterval.setStatus("current")
_IgsVlanRtrPortList_Type = PortList
_IgsVlanRtrPortList_Object = MibTableColumn
igsVlanRtrPortList = _IgsVlanRtrPortList_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 10, 3, 4, 1, 6),
    _IgsVlanRtrPortList_Type()
)
igsVlanRtrPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igsVlanRtrPortList.setStatus("current")
_IgsVlanFbdRtrPortList_Type = PortList
_IgsVlanFbdRtrPortList_Object = MibTableColumn
igsVlanFbdRtrPortList = _IgsVlanFbdRtrPortList_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 10, 3, 4, 1, 7),
    _IgsVlanFbdRtrPortList_Type()
)
igsVlanFbdRtrPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igsVlanFbdRtrPortList.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 10, 3, 4, 1, 8),
    _IgsVlanFastLeave_Type()
)
igsVlanFastLeave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igsVlanFastLeave.setStatus("current")


class _IgsVlanDataDrivenLearningStatus_Type(Integer32):
    """Custom type igsVlanDataDrivenLearningStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_IgsVlanDataDrivenLearningStatus_Type.__name__ = "Integer32"
_IgsVlanDataDrivenLearningStatus_Object = MibTableColumn
igsVlanDataDrivenLearningStatus = _IgsVlanDataDrivenLearningStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 10, 3, 4, 1, 9),
    _IgsVlanDataDrivenLearningStatus_Type()
)
igsVlanDataDrivenLearningStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igsVlanDataDrivenLearningStatus.setStatus("current")
_IgsVlanMulticastGroupTable_Object = MibTable
igsVlanMulticastGroupTable = _IgsVlanMulticastGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 10, 3, 5)
)
if mibBuilder.loadTexts:
    igsVlanMulticastGroupTable.setStatus("current")
_IgsVlanMulticastGroupEntry_Object = MibTableRow
igsVlanMulticastGroupEntry = _IgsVlanMulticastGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 10, 3, 5, 1)
)
igsVlanMulticastGroupEntry.setIndexNames(
    (0, "DES-1210-28ME_B2", "igsVlanMulticastGroupVlanId"),
    (0, "DES-1210-28ME_B2", "igsVlanMulticastGroupIpAddress"),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 10, 3, 5, 1, 1),
    _IgsVlanMulticastGroupVlanId_Type()
)
igsVlanMulticastGroupVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igsVlanMulticastGroupVlanId.setStatus("current")
_IgsVlanMulticastGroupIpAddress_Type = InetAddress
_IgsVlanMulticastGroupIpAddress_Object = MibTableColumn
igsVlanMulticastGroupIpAddress = _IgsVlanMulticastGroupIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 10, 3, 5, 1, 2),
    _IgsVlanMulticastGroupIpAddress_Type()
)
igsVlanMulticastGroupIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igsVlanMulticastGroupIpAddress.setStatus("current")
_IgsVlanMulticastGroupMacAddress_Type = MacAddress
_IgsVlanMulticastGroupMacAddress_Object = MibTableColumn
igsVlanMulticastGroupMacAddress = _IgsVlanMulticastGroupMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 10, 3, 5, 1, 3),
    _IgsVlanMulticastGroupMacAddress_Type()
)
igsVlanMulticastGroupMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igsVlanMulticastGroupMacAddress.setStatus("current")
_IgsVlanMulticastGroupPortList_Type = PortList
_IgsVlanMulticastGroupPortList_Object = MibTableColumn
igsVlanMulticastGroupPortList = _IgsVlanMulticastGroupPortList_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 10, 3, 5, 1, 4),
    _IgsVlanMulticastGroupPortList_Type()
)
igsVlanMulticastGroupPortList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igsVlanMulticastGroupPortList.setStatus("current")
_IgsAccessAuth_ObjectIdentity = ObjectIdentity
igsAccessAuth = _IgsAccessAuth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 10, 5)
)
_IgsAccessAuthTable_Object = MibTable
igsAccessAuthTable = _IgsAccessAuthTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 10, 5, 1)
)
if mibBuilder.loadTexts:
    igsAccessAuthTable.setStatus("current")
_IgsAccessAuthEntry_Object = MibTableRow
igsAccessAuthEntry = _IgsAccessAuthEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 10, 5, 1, 1)
)
igsAccessAuthEntry.setIndexNames(
    (0, "DES-1210-28ME_B2", "igsAccessAuthPortIndex"),
)
if mibBuilder.loadTexts:
    igsAccessAuthEntry.setStatus("current")
_IgsAccessAuthPortIndex_Type = Integer32
_IgsAccessAuthPortIndex_Object = MibTableColumn
igsAccessAuthPortIndex = _IgsAccessAuthPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 10, 5, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 10, 5, 1, 1, 2),
    _IgsAccessAuthState_Type()
)
igsAccessAuthState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igsAccessAuthState.setStatus("current")
_IgsHost_ObjectIdentity = ObjectIdentity
igsHost = _IgsHost_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 10, 6)
)
_IgsHostTable_Object = MibTable
igsHostTable = _IgsHostTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 10, 6, 1)
)
if mibBuilder.loadTexts:
    igsHostTable.setStatus("current")
_IgsHostEntry_Object = MibTableRow
igsHostEntry = _IgsHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 10, 6, 1, 1)
)
igsHostEntry.setIndexNames(
    (0, "DES-1210-28ME_B2", "igsHostTableVLANID"),
    (0, "DES-1210-28ME_B2", "igsHostTableGroupAddress"),
    (0, "DES-1210-28ME_B2", "igsHostTablePort"),
    (0, "DES-1210-28ME_B2", "igsHostTableHostIPAddress"),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 10, 6, 1, 1, 1),
    _IgsHostTableVLANID_Type()
)
igsHostTableVLANID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igsHostTableVLANID.setStatus("current")
_IgsHostTableGroupAddress_Type = InetAddress
_IgsHostTableGroupAddress_Object = MibTableColumn
igsHostTableGroupAddress = _IgsHostTableGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 10, 6, 1, 1, 2),
    _IgsHostTableGroupAddress_Type()
)
igsHostTableGroupAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igsHostTableGroupAddress.setStatus("current")


class _IgsHostTablePort_Type(Integer32):
    """Custom type igsHostTablePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 28),
    )


_IgsHostTablePort_Type.__name__ = "Integer32"
_IgsHostTablePort_Object = MibTableColumn
igsHostTablePort = _IgsHostTablePort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 10, 6, 1, 1, 3),
    _IgsHostTablePort_Type()
)
igsHostTablePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igsHostTablePort.setStatus("current")
_IgsHostTableHostIPAddress_Type = InetAddress
_IgsHostTableHostIPAddress_Object = MibTableColumn
igsHostTableHostIPAddress = _IgsHostTableHostIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 10, 6, 1, 1, 4),
    _IgsHostTableHostIPAddress_Type()
)
igsHostTableHostIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igsHostTableHostIPAddress.setStatus("current")
_CompanyGVRPGroup_ObjectIdentity = ObjectIdentity
companyGVRPGroup = _CompanyGVRPGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 11)
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 11, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 11, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 11, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 11, 4),
    _GvrpSettingsLeaveAllTime_Type()
)
gvrpSettingsLeaveAllTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gvrpSettingsLeaveAllTime.setStatus("current")
_GvrpSettingsTable_Object = MibTable
gvrpSettingsTable = _GvrpSettingsTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 11, 5)
)
if mibBuilder.loadTexts:
    gvrpSettingsTable.setStatus("current")
_GvrpSettingsEntry_Object = MibTableRow
gvrpSettingsEntry = _GvrpSettingsEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 11, 5, 1)
)
gvrpSettingsEntry.setIndexNames(
    (0, "DES-1210-28ME_B2", "gvrpSettingsPortControlIndex"),
)
if mibBuilder.loadTexts:
    gvrpSettingsEntry.setStatus("current")
_GvrpSettingsPortControlIndex_Type = InterfaceIndex
_GvrpSettingsPortControlIndex_Object = MibTableColumn
gvrpSettingsPortControlIndex = _GvrpSettingsPortControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 11, 5, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 11, 5, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 11, 5, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 11, 5, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 11, 5, 1, 5),
    _GvrpSettingsAcceptableFrameType_Type()
)
gvrpSettingsAcceptableFrameType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gvrpSettingsAcceptableFrameType.setStatus("current")
_CompanyQoSGroup_ObjectIdentity = ObjectIdentity
companyQoSGroup = _CompanyQoSGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 12)
)


class _CosScheduleMechanism_Type(Integer32):
    """Custom type cosScheduleMechanism based on Integer32"""
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


_CosScheduleMechanism_Type.__name__ = "Integer32"
_CosScheduleMechanism_Object = MibScalar
cosScheduleMechanism = _CosScheduleMechanism_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 12, 1),
    _CosScheduleMechanism_Type()
)
cosScheduleMechanism.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cosScheduleMechanism.setStatus("current")
_CosOutputSchedule_ObjectIdentity = ObjectIdentity
cosOutputSchedule = _CosOutputSchedule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 12, 2)
)
_CosClassTable_Object = MibTable
cosClassTable = _CosClassTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 12, 2, 1)
)
if mibBuilder.loadTexts:
    cosClassTable.setStatus("current")
_CosClassEntry_Object = MibTableRow
cosClassEntry = _CosClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 12, 2, 1, 1)
)
cosClassEntry.setIndexNames(
    (0, "DES-1210-28ME_B2", "cosClassIndex"),
)
if mibBuilder.loadTexts:
    cosClassEntry.setStatus("current")


class _CosClassIndex_Type(Integer32):
    """Custom type cosClassIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_CosClassIndex_Type.__name__ = "Integer32"
_CosClassIndex_Object = MibTableColumn
cosClassIndex = _CosClassIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 12, 2, 1, 1, 1),
    _CosClassIndex_Type()
)
cosClassIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cosClassIndex.setStatus("current")


class _CosWeight_Type(Integer32):
    """Custom type cosWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 55),
    )


_CosWeight_Type.__name__ = "Integer32"
_CosWeight_Object = MibTableColumn
cosWeight = _CosWeight_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 12, 2, 1, 1, 2),
    _CosWeight_Type()
)
cosWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cosWeight.setStatus("current")
_QosDefaultUserPri_ObjectIdentity = ObjectIdentity
qosDefaultUserPri = _QosDefaultUserPri_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 12, 4)
)
_QosDefaultUserPriTable_Object = MibTable
qosDefaultUserPriTable = _QosDefaultUserPriTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 12, 4, 1)
)
if mibBuilder.loadTexts:
    qosDefaultUserPriTable.setStatus("current")
_QosDefaultUserPriEntry_Object = MibTableRow
qosDefaultUserPriEntry = _QosDefaultUserPriEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 12, 4, 1, 1)
)
qosDefaultUserPriEntry.setIndexNames(
    (0, "DES-1210-28ME_B2", "qosDefaultUserPriPortIndex"),
)
if mibBuilder.loadTexts:
    qosDefaultUserPriEntry.setStatus("current")
_QosDefaultUserPriPortIndex_Type = Integer32
_QosDefaultUserPriPortIndex_Object = MibTableColumn
qosDefaultUserPriPortIndex = _QosDefaultUserPriPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 12, 4, 1, 1, 1),
    _QosDefaultUserPriPortIndex_Type()
)
qosDefaultUserPriPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosDefaultUserPriPortIndex.setStatus("current")


class _QosDefaultPriority_Type(Integer32):
    """Custom type qosDefaultPriority based on Integer32"""
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
        *(("priority0", 0),
          ("priority1", 1),
          ("priority2", 2),
          ("priority3", 3),
          ("priority4", 4),
          ("priority5", 5),
          ("priority6", 6),
          ("priority7", 7))
    )


_QosDefaultPriority_Type.__name__ = "Integer32"
_QosDefaultPriority_Object = MibTableColumn
qosDefaultPriority = _QosDefaultPriority_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 12, 4, 1, 1, 2),
    _QosDefaultPriority_Type()
)
qosDefaultPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosDefaultPriority.setStatus("current")


class _QosEffectiveDefaultPriority_Type(Integer32):
    """Custom type qosEffectiveDefaultPriority based on Integer32"""
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
        *(("priority0", 0),
          ("priority1", 1),
          ("priority2", 2),
          ("priority3", 3),
          ("priority4", 4),
          ("priority5", 5),
          ("priority6", 6),
          ("priority7", 7))
    )


_QosEffectiveDefaultPriority_Type.__name__ = "Integer32"
_QosEffectiveDefaultPriority_Object = MibTableColumn
qosEffectiveDefaultPriority = _QosEffectiveDefaultPriority_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 12, 4, 1, 1, 3),
    _QosEffectiveDefaultPriority_Type()
)
qosEffectiveDefaultPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosEffectiveDefaultPriority.setStatus("current")
_QosUserPriority_ObjectIdentity = ObjectIdentity
qosUserPriority = _QosUserPriority_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 12, 5)
)
_QosUserPriorityTable_Object = MibTable
qosUserPriorityTable = _QosUserPriorityTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 12, 5, 1)
)
if mibBuilder.loadTexts:
    qosUserPriorityTable.setStatus("current")
_QosUserPriEntry_Object = MibTableRow
qosUserPriEntry = _QosUserPriEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 12, 5, 1, 1)
)
qosUserPriEntry.setIndexNames(
    (0, "DES-1210-28ME_B2", "qosUserPriIndex"),
)
if mibBuilder.loadTexts:
    qosUserPriEntry.setStatus("current")


class _QosUserPriIndex_Type(Integer32):
    """Custom type qosUserPriIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_QosUserPriIndex_Type.__name__ = "Integer32"
_QosUserPriIndex_Object = MibTableColumn
qosUserPriIndex = _QosUserPriIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 12, 5, 1, 1, 1),
    _QosUserPriIndex_Type()
)
qosUserPriIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosUserPriIndex.setStatus("current")


class _QosUserPriClass_Type(Integer32):
    """Custom type qosUserPriClass based on Integer32"""
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


_QosUserPriClass_Type.__name__ = "Integer32"
_QosUserPriClass_Object = MibTableColumn
qosUserPriClass = _QosUserPriClass_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 12, 5, 1, 1, 2),
    _QosUserPriClass_Type()
)
qosUserPriClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosUserPriClass.setStatus("current")
_QosDiffServTOS_ObjectIdentity = ObjectIdentity
qosDiffServTOS = _QosDiffServTOS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 12, 6)
)


class _QosDSCPTOSMode_Type(Integer32):
    """Custom type qosDSCPTOSMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dscp", 2),
          ("tos", 1))
    )


_QosDSCPTOSMode_Type.__name__ = "Integer32"
_QosDSCPTOSMode_Object = MibScalar
qosDSCPTOSMode = _QosDSCPTOSMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 12, 6, 1),
    _QosDSCPTOSMode_Type()
)
qosDSCPTOSMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosDSCPTOSMode.setStatus("current")
_QosDiffServTypeGroup_ObjectIdentity = ObjectIdentity
qosDiffServTypeGroup = _QosDiffServTypeGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 12, 6, 2)
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 12, 6, 2, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 12, 6, 2, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 12, 6, 2, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 12, 6, 2, 4),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 12, 6, 2, 5),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 12, 6, 2, 6),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 12, 6, 2, 7),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 12, 6, 2, 8),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 12, 6, 2, 9),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 12, 6, 2, 10),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 12, 6, 2, 11),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 12, 6, 2, 12),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 12, 6, 2, 13),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 12, 6, 2, 14),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 12, 6, 2, 15),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 12, 6, 2, 16),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 12, 6, 2, 17),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 12, 6, 2, 18),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 12, 6, 2, 19),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 12, 6, 2, 20),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 12, 6, 2, 21),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 12, 6, 2, 22),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 12, 6, 2, 23),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 12, 6, 2, 24),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 12, 6, 2, 25),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 12, 6, 2, 26),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 12, 6, 2, 27),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 12, 6, 2, 28),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 12, 6, 2, 29),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 12, 6, 2, 30),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 12, 6, 2, 31),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 12, 6, 2, 32),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 12, 6, 2, 33),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 12, 6, 2, 34),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 12, 6, 2, 35),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 12, 6, 2, 36),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 12, 6, 2, 37),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 12, 6, 2, 38),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 12, 6, 2, 39),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 12, 6, 2, 40),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 12, 6, 2, 41),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 12, 6, 2, 42),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 12, 6, 2, 43),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 12, 6, 2, 44),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 12, 6, 2, 45),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 12, 6, 2, 46),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 12, 6, 2, 47),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 12, 6, 2, 48),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 12, 6, 2, 49),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 12, 6, 2, 50),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 12, 6, 2, 51),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 12, 6, 2, 52),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 12, 6, 2, 53),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 12, 6, 2, 54),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 12, 6, 2, 55),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 12, 6, 2, 56),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 12, 6, 2, 57),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 12, 6, 2, 58),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 12, 6, 2, 59),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 12, 6, 2, 60),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 12, 6, 2, 61),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 12, 6, 2, 62),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 12, 6, 2, 63),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 12, 6, 2, 64),
    _QosDiffServType63_Type()
)
qosDiffServType63.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosDiffServType63.setStatus("current")
_QosTOSGroup_ObjectIdentity = ObjectIdentity
qosTOSGroup = _QosTOSGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 12, 6, 3)
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 12, 6, 3, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 12, 6, 3, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 12, 6, 3, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 12, 6, 3, 4),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 12, 6, 3, 5),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 12, 6, 3, 6),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 12, 6, 3, 7),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 12, 6, 3, 8),
    _QosTOSType07_Type()
)
qosTOSType07.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosTOSType07.setStatus("current")
_QosPriSettings_ObjectIdentity = ObjectIdentity
qosPriSettings = _QosPriSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 12, 7)
)
_QosPriSettingsTable_Object = MibTable
qosPriSettingsTable = _QosPriSettingsTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 12, 7, 1)
)
if mibBuilder.loadTexts:
    qosPriSettingsTable.setStatus("current")
_QosPriSettingsEntry_Object = MibTableRow
qosPriSettingsEntry = _QosPriSettingsEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 12, 7, 1, 1)
)
qosPriSettingsEntry.setIndexNames(
    (0, "DES-1210-28ME_B2", "qosPriSetPortIndex"),
)
if mibBuilder.loadTexts:
    qosPriSettingsEntry.setStatus("current")
_QosPriSetPortIndex_Type = Integer32
_QosPriSetPortIndex_Object = MibTableColumn
qosPriSetPortIndex = _QosPriSetPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 12, 7, 1, 1, 1),
    _QosPriSetPortIndex_Type()
)
qosPriSetPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosPriSetPortIndex.setStatus("current")


class _QosPriSetPortType_Type(Integer32):
    """Custom type qosPriSetPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("dscp-tos", 4),
          ("ieee8021P", 2),
          ("ieee8021P_dscp-tos", 6),
          ("none", 0))
    )


_QosPriSetPortType_Type.__name__ = "Integer32"
_QosPriSetPortType_Object = MibTableColumn
qosPriSetPortType = _QosPriSetPortType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 12, 7, 1, 1, 2),
    _QosPriSetPortType_Type()
)
qosPriSetPortType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosPriSetPortType.setStatus("current")
_QosAclPrioritySettings_ObjectIdentity = ObjectIdentity
qosAclPrioritySettings = _QosAclPrioritySettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 12, 8)
)
_AclQosTable_Object = MibTable
aclQosTable = _AclQosTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 12, 8, 1)
)
if mibBuilder.loadTexts:
    aclQosTable.setStatus("current")
_AclQosEntry_Object = MibTableRow
aclQosEntry = _AclQosEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 12, 8, 1, 1)
)
aclQosEntry.setIndexNames(
    (0, "DES-1210-28ME_B2", "aclQosIndex"),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 12, 8, 1, 1, 1),
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
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("ip", 1),
          ("mac", 0),
          ("protocol", 5),
          ("tcp", 2),
          ("udp", 3),
          ("vlanid", 4))
    )


_AclQosType_Type.__name__ = "Integer32"
_AclQosType_Object = MibTableColumn
aclQosType = _AclQosType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 12, 8, 1, 1, 2),
    _AclQosType_Type()
)
aclQosType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclQosType.setStatus("current")
_AclQosMACAddr_Type = MacAddress
_AclQosMACAddr_Object = MibTableColumn
aclQosMACAddr = _AclQosMACAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 12, 8, 1, 1, 3),
    _AclQosMACAddr_Type()
)
aclQosMACAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclQosMACAddr.setStatus("current")
_AclQosIPAddr_Type = IpAddress
_AclQosIPAddr_Object = MibTableColumn
aclQosIPAddr = _AclQosIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 12, 8, 1, 1, 4),
    _AclQosIPAddr_Type()
)
aclQosIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclQosIPAddr.setStatus("current")


class _AclQosTCPUDPPort_Type(Integer32):
    """Custom type aclQosTCPUDPPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AclQosTCPUDPPort_Type.__name__ = "Integer32"
_AclQosTCPUDPPort_Object = MibTableColumn
aclQosTCPUDPPort = _AclQosTCPUDPPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 12, 8, 1, 1, 5),
    _AclQosTCPUDPPort_Type()
)
aclQosTCPUDPPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclQosTCPUDPPort.setStatus("current")


class _AclQosVlanID_Type(Integer32):
    """Custom type aclQosVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_AclQosVlanID_Type.__name__ = "Integer32"
_AclQosVlanID_Object = MibTableColumn
aclQosVlanID = _AclQosVlanID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 12, 8, 1, 1, 6),
    _AclQosVlanID_Type()
)
aclQosVlanID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclQosVlanID.setStatus("current")


class _AclQosProtocol_Type(Integer32):
    """Custom type aclQosProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AclQosProtocol_Type.__name__ = "Integer32"
_AclQosProtocol_Object = MibTableColumn
aclQosProtocol = _AclQosProtocol_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 12, 8, 1, 1, 7),
    _AclQosProtocol_Type()
)
aclQosProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclQosProtocol.setStatus("current")


class _AclQosAssignClass_Type(Integer32):
    """Custom type aclQosAssignClass based on Integer32"""
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
        *(("class0", 0),
          ("class1", 1),
          ("class2", 2),
          ("class3", 3))
    )


_AclQosAssignClass_Type.__name__ = "Integer32"
_AclQosAssignClass_Object = MibTableColumn
aclQosAssignClass = _AclQosAssignClass_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 12, 8, 1, 1, 8),
    _AclQosAssignClass_Type()
)
aclQosAssignClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclQosAssignClass.setStatus("current")
_AclQosStatus_Type = RowStatus
_AclQosStatus_Object = MibTableColumn
aclQosStatus = _AclQosStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 12, 8, 1, 1, 9),
    _AclQosStatus_Type()
)
aclQosStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclQosStatus.setStatus("current")
_CompanyTrafficMgmt_ObjectIdentity = ObjectIdentity
companyTrafficMgmt = _CompanyTrafficMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 13)
)
_BandwidthCtrlSettings_ObjectIdentity = ObjectIdentity
bandwidthCtrlSettings = _BandwidthCtrlSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 13, 1)
)
_BandwidthCtrlTable_Object = MibTable
bandwidthCtrlTable = _BandwidthCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 13, 1, 2)
)
if mibBuilder.loadTexts:
    bandwidthCtrlTable.setStatus("current")
_BandwidthCtrlEntry_Object = MibTableRow
bandwidthCtrlEntry = _BandwidthCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 13, 1, 2, 1)
)
bandwidthCtrlEntry.setIndexNames(
    (0, "DES-1210-28ME_B2", "bandwidthCtrlIndex"),
)
if mibBuilder.loadTexts:
    bandwidthCtrlEntry.setStatus("current")
_BandwidthCtrlIndex_Type = Integer32
_BandwidthCtrlIndex_Object = MibTableColumn
bandwidthCtrlIndex = _BandwidthCtrlIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 13, 1, 2, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 13, 1, 2, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 13, 1, 2, 1, 3),
    _BandwidthCtrlRxThreshold_Type()
)
bandwidthCtrlRxThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bandwidthCtrlRxThreshold.setStatus("current")
_TrafficCtrlSettings_ObjectIdentity = ObjectIdentity
trafficCtrlSettings = _TrafficCtrlSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 13, 4)
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 13, 4, 1),
    _TrafficCtrlTrap_Type()
)
trafficCtrlTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trafficCtrlTrap.setStatus("current")
_TrafficCtrlTable_Object = MibTable
trafficCtrlTable = _TrafficCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 13, 4, 2)
)
if mibBuilder.loadTexts:
    trafficCtrlTable.setStatus("current")
_TrafficCtrlEntry_Object = MibTableRow
trafficCtrlEntry = _TrafficCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 13, 4, 2, 1)
)
trafficCtrlEntry.setIndexNames(
    (0, "DES-1210-28ME_B2", "trafficCtrlIndex"),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 13, 4, 2, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 13, 4, 2, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 13, 4, 2, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 13, 4, 2, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 13, 4, 2, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 13, 4, 2, 1, 6),
    _TrafficCtrlTimeInterval_Type()
)
trafficCtrlTimeInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trafficCtrlTimeInterval.setStatus("current")
_CompanySecurity_ObjectIdentity = ObjectIdentity
companySecurity = _CompanySecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 14)
)
_SecurityTrustedHost_ObjectIdentity = ObjectIdentity
securityTrustedHost = _SecurityTrustedHost_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 14, 1)
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 14, 1, 1),
    _TrustedHostStatus_Type()
)
trustedHostStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trustedHostStatus.setStatus("current")
_TrustedHostTable_Object = MibTable
trustedHostTable = _TrustedHostTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 14, 1, 2)
)
if mibBuilder.loadTexts:
    trustedHostTable.setStatus("current")
_TrustedHostEntry_Object = MibTableRow
trustedHostEntry = _TrustedHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 14, 1, 2, 1)
)
trustedHostEntry.setIndexNames(
    (0, "DES-1210-28ME_B2", "trustedHostIpAddr"),
    (0, "DES-1210-28ME_B2", "trustedHostIpMask"),
)
if mibBuilder.loadTexts:
    trustedHostEntry.setStatus("current")
_TrustedHostIpAddr_Type = IpAddress
_TrustedHostIpAddr_Object = MibTableColumn
trustedHostIpAddr = _TrustedHostIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 14, 1, 2, 1, 1),
    _TrustedHostIpAddr_Type()
)
trustedHostIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trustedHostIpAddr.setStatus("current")
_TrustedHostIpMask_Type = IpAddress
_TrustedHostIpMask_Object = MibTableColumn
trustedHostIpMask = _TrustedHostIpMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 14, 1, 2, 1, 2),
    _TrustedHostIpMask_Type()
)
trustedHostIpMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trustedHostIpMask.setStatus("current")
_TrustedHostRowStatus_Type = RowStatus
_TrustedHostRowStatus_Object = MibTableColumn
trustedHostRowStatus = _TrustedHostRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 14, 1, 2, 1, 3),
    _TrustedHostRowStatus_Type()
)
trustedHostRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    trustedHostRowStatus.setStatus("current")
_SecurityPortSecurity_ObjectIdentity = ObjectIdentity
securityPortSecurity = _SecurityPortSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 14, 2)
)
_PortSecTable_Object = MibTable
portSecTable = _PortSecTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 14, 2, 1)
)
if mibBuilder.loadTexts:
    portSecTable.setStatus("current")
_PortSecEntry_Object = MibTableRow
portSecEntry = _PortSecEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 14, 2, 1, 1)
)
portSecEntry.setIndexNames(
    (0, "DES-1210-28ME_B2", "portSecIndex"),
)
if mibBuilder.loadTexts:
    portSecEntry.setStatus("current")
_PortSecIndex_Type = Integer32
_PortSecIndex_Object = MibTableColumn
portSecIndex = _PortSecIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 14, 2, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 14, 2, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 14, 2, 1, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 14, 2, 1, 1, 4),
    _PortSecLockAddrMode_Type()
)
portSecLockAddrMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portSecLockAddrMode.setStatus("current")
_PortSecFDBPermanentTable_Object = MibTable
portSecFDBPermanentTable = _PortSecFDBPermanentTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 14, 2, 2)
)
if mibBuilder.loadTexts:
    portSecFDBPermanentTable.setStatus("current")
_PortSecFDBPermanentEntry_Object = MibTableRow
portSecFDBPermanentEntry = _PortSecFDBPermanentEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 14, 2, 2, 1)
)
portSecFDBPermanentEntry.setIndexNames(
    (0, "DES-1210-28ME_B2", "portSecFDBPermPort"),
    (0, "DES-1210-28ME_B2", "portSecFDBPermIndex"),
)
if mibBuilder.loadTexts:
    portSecFDBPermanentEntry.setStatus("current")
_PortSecFDBPermIndex_Type = Integer32
_PortSecFDBPermIndex_Object = MibTableColumn
portSecFDBPermIndex = _PortSecFDBPermIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 14, 2, 2, 1, 1),
    _PortSecFDBPermIndex_Type()
)
portSecFDBPermIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portSecFDBPermIndex.setStatus("current")
_PortSecFDBPermVlanID_Type = Integer32
_PortSecFDBPermVlanID_Object = MibTableColumn
portSecFDBPermVlanID = _PortSecFDBPermVlanID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 14, 2, 2, 1, 2),
    _PortSecFDBPermVlanID_Type()
)
portSecFDBPermVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portSecFDBPermVlanID.setStatus("current")
_PortSecFDBPermMac_Type = MacAddress
_PortSecFDBPermMac_Object = MibTableColumn
portSecFDBPermMac = _PortSecFDBPermMac_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 14, 2, 2, 1, 3),
    _PortSecFDBPermMac_Type()
)
portSecFDBPermMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portSecFDBPermMac.setStatus("current")
_PortSecFDBPermPort_Type = Integer32
_PortSecFDBPermPort_Object = MibTableColumn
portSecFDBPermPort = _PortSecFDBPermPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 14, 2, 2, 1, 4),
    _PortSecFDBPermPort_Type()
)
portSecFDBPermPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portSecFDBPermPort.setStatus("current")
_SecurityARPSpoofPrevent_ObjectIdentity = ObjectIdentity
securityARPSpoofPrevent = _SecurityARPSpoofPrevent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 14, 3)
)
_ARPSpoofPreventTable_Object = MibTable
aRPSpoofPreventTable = _ARPSpoofPreventTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 14, 3, 1)
)
if mibBuilder.loadTexts:
    aRPSpoofPreventTable.setStatus("current")
_ARPSpoofPreventEntry_Object = MibTableRow
aRPSpoofPreventEntry = _ARPSpoofPreventEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 14, 3, 1, 1)
)
aRPSpoofPreventEntry.setIndexNames(
    (0, "DES-1210-28ME_B2", "aRPSpoofPreventIpAddr"),
)
if mibBuilder.loadTexts:
    aRPSpoofPreventEntry.setStatus("current")
_ARPSpoofPreventIpAddr_Type = IpAddress
_ARPSpoofPreventIpAddr_Object = MibTableColumn
aRPSpoofPreventIpAddr = _ARPSpoofPreventIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 14, 3, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 14, 3, 1, 1, 2),
    _ARPSpoofPreventMacAddress_Type()
)
aRPSpoofPreventMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aRPSpoofPreventMacAddress.setStatus("current")
_ARPSpoofPreventPortList_Type = PortList
_ARPSpoofPreventPortList_Object = MibTableColumn
aRPSpoofPreventPortList = _ARPSpoofPreventPortList_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 14, 3, 1, 1, 3),
    _ARPSpoofPreventPortList_Type()
)
aRPSpoofPreventPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aRPSpoofPreventPortList.setStatus("current")
_ARPSpoofPreventRowStatus_Type = RowStatus
_ARPSpoofPreventRowStatus_Object = MibTableColumn
aRPSpoofPreventRowStatus = _ARPSpoofPreventRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 14, 3, 1, 1, 4),
    _ARPSpoofPreventRowStatus_Type()
)
aRPSpoofPreventRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aRPSpoofPreventRowStatus.setStatus("current")
_SecuritySSL_ObjectIdentity = ObjectIdentity
securitySSL = _SecuritySSL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 14, 5)
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 14, 5, 1),
    _SslSecurityHttpStatus_Type()
)
sslSecurityHttpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sslSecurityHttpStatus.setStatus("current")
_SslCiphers_ObjectIdentity = ObjectIdentity
sslCiphers = _SslCiphers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 14, 5, 2)
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 14, 5, 2, 1),
    _SslCipherSuiteList_Type()
)
sslCipherSuiteList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sslCipherSuiteList.setStatus("current")
_SecurityDhcpServerScreen_ObjectIdentity = ObjectIdentity
securityDhcpServerScreen = _SecurityDhcpServerScreen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 14, 7)
)
_DhcpServerScreenEnablePortlist_Type = PortList
_DhcpServerScreenEnablePortlist_Object = MibScalar
dhcpServerScreenEnablePortlist = _DhcpServerScreenEnablePortlist_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 14, 7, 1),
    _DhcpServerScreenEnablePortlist_Type()
)
dhcpServerScreenEnablePortlist.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpServerScreenEnablePortlist.setStatus("current")
_FilterDHCPServerTable_Object = MibTable
filterDHCPServerTable = _FilterDHCPServerTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 14, 7, 2)
)
if mibBuilder.loadTexts:
    filterDHCPServerTable.setStatus("current")
_FilterDHCPServerEntry_Object = MibTableRow
filterDHCPServerEntry = _FilterDHCPServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 14, 7, 2, 1)
)
filterDHCPServerEntry.setIndexNames(
    (0, "DES-1210-28ME_B2", "filterDHCPServerIpAddr"),
    (0, "DES-1210-28ME_B2", "filterDHCPServerClientMacAddr"),
)
if mibBuilder.loadTexts:
    filterDHCPServerEntry.setStatus("current")
_FilterDHCPServerIpAddr_Type = IpAddress
_FilterDHCPServerIpAddr_Object = MibTableColumn
filterDHCPServerIpAddr = _FilterDHCPServerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 14, 7, 2, 1, 1),
    _FilterDHCPServerIpAddr_Type()
)
filterDHCPServerIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    filterDHCPServerIpAddr.setStatus("current")


class _FilterDHCPServerClientMacAddr_Type(MacAddress):
    """Custom type filterDHCPServerClientMacAddr based on MacAddress"""
    defaultHexValue = "000102030405"


_FilterDHCPServerClientMacAddr_Object = MibTableColumn
filterDHCPServerClientMacAddr = _FilterDHCPServerClientMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 14, 7, 2, 1, 2),
    _FilterDHCPServerClientMacAddr_Type()
)
filterDHCPServerClientMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    filterDHCPServerClientMacAddr.setStatus("current")
_FilterDHCPServerPortList_Type = PortList
_FilterDHCPServerPortList_Object = MibTableColumn
filterDHCPServerPortList = _FilterDHCPServerPortList_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 14, 7, 2, 1, 3),
    _FilterDHCPServerPortList_Type()
)
filterDHCPServerPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterDHCPServerPortList.setStatus("current")
_FilterDHCPServerRowStatus_Type = RowStatus
_FilterDHCPServerRowStatus_Object = MibTableColumn
filterDHCPServerRowStatus = _FilterDHCPServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 14, 7, 2, 1, 4),
    _FilterDHCPServerRowStatus_Type()
)
filterDHCPServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    filterDHCPServerRowStatus.setStatus("current")
_SecuritySSH_ObjectIdentity = ObjectIdentity
securitySSH = _SecuritySSH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 14, 8)
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 14, 8, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 14, 8, 2),
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
              10,
              30,
              60)
        )
    )
    namedValues = NamedValues(
        *(("never", 0),
          ("sixty-min", 60),
          ("ten-min", 10),
          ("thirty-min", 30))
    )


_SshSessionKeyRekeying_Type.__name__ = "Integer32"
_SshSessionKeyRekeying_Object = MibScalar
sshSessionKeyRekeying = _SshSessionKeyRekeying_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 14, 8, 3),
    _SshSessionKeyRekeying_Type()
)
sshSessionKeyRekeying.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sshSessionKeyRekeying.setStatus("current")


class _SshMaxSession_Type(Integer32):
    """Custom type sshMaxSession based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_SshMaxSession_Type.__name__ = "Integer32"
_SshMaxSession_Object = MibScalar
sshMaxSession = _SshMaxSession_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 14, 8, 4),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 14, 8, 5),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 14, 8, 6),
    _SshAuthenMethodPassWordAdmin_Type()
)
sshAuthenMethodPassWordAdmin.setMaxAccess("read-write")
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 14, 8, 7),
    _SshAuthenMethodPubKeyAdmin_Type()
)
sshAuthenMethodPubKeyAdmin.setMaxAccess("read-write")
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 14, 8, 8),
    _SshAuthenMethodHostKeyAdmin_Type()
)
sshAuthenMethodHostKeyAdmin.setMaxAccess("read-write")
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 14, 8, 9),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 14, 8, 10),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 14, 8, 11),
    _SshPublKeyRSAAdmin_Type()
)
sshPublKeyRSAAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sshPublKeyRSAAdmin.setStatus("current")
_SshUserInfoTable_Object = MibTable
sshUserInfoTable = _SshUserInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 14, 8, 12)
)
if mibBuilder.loadTexts:
    sshUserInfoTable.setStatus("current")
_SshUserInfoEntry_Object = MibTableRow
sshUserInfoEntry = _SshUserInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 14, 8, 12, 1)
)
sshUserInfoEntry.setIndexNames(
    (0, "DES-1210-28ME_B2", "sshUserInfoID"),
)
if mibBuilder.loadTexts:
    sshUserInfoEntry.setStatus("current")


class _SshUserInfoID_Type(Integer32):
    """Custom type sshUserInfoID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_SshUserInfoID_Type.__name__ = "Integer32"
_SshUserInfoID_Object = MibTableColumn
sshUserInfoID = _SshUserInfoID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 14, 8, 12, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 14, 8, 12, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 14, 8, 12, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 14, 8, 12, 1, 4),
    _SshUserInfoHostName_Type()
)
sshUserInfoHostName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sshUserInfoHostName.setStatus("current")
_SshUserInfoHostIp_Type = IpAddress
_SshUserInfoHostIp_Object = MibTableColumn
sshUserInfoHostIp = _SshUserInfoHostIp_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 14, 8, 12, 1, 5),
    _SshUserInfoHostIp_Type()
)
sshUserInfoHostIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sshUserInfoHostIp.setStatus("current")
_SecurityTrafficSeg_ObjectIdentity = ObjectIdentity
securityTrafficSeg = _SecurityTrafficSeg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 14, 9)
)
_TrafficSegTable_Object = MibTable
trafficSegTable = _TrafficSegTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 14, 9, 1)
)
if mibBuilder.loadTexts:
    trafficSegTable.setStatus("current")
_TrafficSegEntry_Object = MibTableRow
trafficSegEntry = _TrafficSegEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 14, 9, 1, 1)
)
trafficSegEntry.setIndexNames(
    (0, "DES-1210-28ME_B2", "trafficSegIfIndex"),
)
if mibBuilder.loadTexts:
    trafficSegEntry.setStatus("current")
_TrafficSegIfIndex_Type = InterfaceIndex
_TrafficSegIfIndex_Object = MibTableColumn
trafficSegIfIndex = _TrafficSegIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 14, 9, 1, 1, 1),
    _TrafficSegIfIndex_Type()
)
trafficSegIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trafficSegIfIndex.setStatus("current")
_TrafficSegMemberList_Type = PortList
_TrafficSegMemberList_Object = MibTableColumn
trafficSegMemberList = _TrafficSegMemberList_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 14, 9, 1, 1, 2),
    _TrafficSegMemberList_Type()
)
trafficSegMemberList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trafficSegMemberList.setStatus("current")
_SecurityIpMacPortBinding_ObjectIdentity = ObjectIdentity
securityIpMacPortBinding = _SecurityIpMacPortBinding_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 14, 10)
)
_ImpbSettingTable_Object = MibTable
impbSettingTable = _ImpbSettingTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 14, 10, 1)
)
if mibBuilder.loadTexts:
    impbSettingTable.setStatus("current")
_ImpbSettingEntry_Object = MibTableRow
impbSettingEntry = _ImpbSettingEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 14, 10, 1, 1)
)
impbSettingEntry.setIndexNames(
    (0, "DES-1210-28ME_B2", "impbPortIndex"),
)
if mibBuilder.loadTexts:
    impbSettingEntry.setStatus("current")
_ImpbPortIndex_Type = Integer32
_ImpbPortIndex_Object = MibTableColumn
impbPortIndex = _ImpbPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 14, 10, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 14, 10, 1, 1, 2),
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
        *(("disabled", 1),
          ("enabled", 0))
    )


_ImpbInsIpPacPortState_Type.__name__ = "Integer32"
_ImpbInsIpPacPortState_Object = MibTableColumn
impbInsIpPacPortState = _ImpbInsIpPacPortState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 14, 10, 1, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 14, 10, 1, 1, 4),
    _ImpbDHCPPortState_Type()
)
impbDHCPPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    impbDHCPPortState.setStatus("current")
_ImpbSmartTable_Object = MibTable
impbSmartTable = _ImpbSmartTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 14, 10, 2)
)
if mibBuilder.loadTexts:
    impbSmartTable.setStatus("current")
_ImpbSmartEntry_Object = MibTableRow
impbSmartEntry = _ImpbSmartEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 14, 10, 2, 1)
)
impbSmartEntry.setIndexNames(
    (0, "DES-1210-28ME_B2", "impbSmartMacAddress"),
    (0, "DES-1210-28ME_B2", "impbSmartPort"),
    (0, "DES-1210-28ME_B2", "impbSmartIpAddress"),
)
if mibBuilder.loadTexts:
    impbSmartEntry.setStatus("current")
_ImpbSmartMacAddress_Type = MacAddress
_ImpbSmartMacAddress_Object = MibTableColumn
impbSmartMacAddress = _ImpbSmartMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 14, 10, 2, 1, 1),
    _ImpbSmartMacAddress_Type()
)
impbSmartMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    impbSmartMacAddress.setStatus("current")
_ImpbSmartPort_Type = Integer32
_ImpbSmartPort_Object = MibTableColumn
impbSmartPort = _ImpbSmartPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 14, 10, 2, 1, 2),
    _ImpbSmartPort_Type()
)
impbSmartPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    impbSmartPort.setStatus("current")
_ImpbSmartIpAddress_Type = IpAddress
_ImpbSmartIpAddress_Object = MibTableColumn
impbSmartIpAddress = _ImpbSmartIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 14, 10, 2, 1, 3),
    _ImpbSmartIpAddress_Type()
)
impbSmartIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    impbSmartIpAddress.setStatus("current")
_ImpbSmartVlanId_Type = Integer32
_ImpbSmartVlanId_Object = MibTableColumn
impbSmartVlanId = _ImpbSmartVlanId_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 14, 10, 2, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 14, 10, 2, 1, 5),
    _ImpbSmartBinding_Type()
)
impbSmartBinding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    impbSmartBinding.setStatus("current")
_ImpbWhiteListTable_Object = MibTable
impbWhiteListTable = _ImpbWhiteListTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 14, 10, 3)
)
if mibBuilder.loadTexts:
    impbWhiteListTable.setStatus("current")
_ImpbWhiteListEntry_Object = MibTableRow
impbWhiteListEntry = _ImpbWhiteListEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 14, 10, 3, 1)
)
impbWhiteListEntry.setIndexNames(
    (0, "DES-1210-28ME_B2", "impbWhiteListIpAddress"),
    (0, "DES-1210-28ME_B2", "impbWhiteListMacAddress"),
)
if mibBuilder.loadTexts:
    impbWhiteListEntry.setStatus("current")
_ImpbWhiteListIpAddress_Type = IpAddress
_ImpbWhiteListIpAddress_Object = MibTableColumn
impbWhiteListIpAddress = _ImpbWhiteListIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 14, 10, 3, 1, 1),
    _ImpbWhiteListIpAddress_Type()
)
impbWhiteListIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    impbWhiteListIpAddress.setStatus("current")
_ImpbWhiteListMacAddress_Type = MacAddress
_ImpbWhiteListMacAddress_Object = MibTableColumn
impbWhiteListMacAddress = _ImpbWhiteListMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 14, 10, 3, 1, 2),
    _ImpbWhiteListMacAddress_Type()
)
impbWhiteListMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    impbWhiteListMacAddress.setStatus("current")
_ImpbWhiteListPort_Type = Integer32
_ImpbWhiteListPort_Object = MibTableColumn
impbWhiteListPort = _ImpbWhiteListPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 14, 10, 3, 1, 3),
    _ImpbWhiteListPort_Type()
)
impbWhiteListPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    impbWhiteListPort.setStatus("current")
_ImpbWhiteListRowStatus_Type = RowStatus
_ImpbWhiteListRowStatus_Object = MibTableColumn
impbWhiteListRowStatus = _ImpbWhiteListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 14, 10, 3, 1, 4),
    _ImpbWhiteListRowStatus_Type()
)
impbWhiteListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    impbWhiteListRowStatus.setStatus("current")
_ImpbBlackListTable_Object = MibTable
impbBlackListTable = _ImpbBlackListTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 14, 10, 4)
)
if mibBuilder.loadTexts:
    impbBlackListTable.setStatus("current")
_ImpbBlackListEntry_Object = MibTableRow
impbBlackListEntry = _ImpbBlackListEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 14, 10, 4, 1)
)
impbBlackListEntry.setIndexNames(
    (0, "DES-1210-28ME_B2", "impbBlackListMacAddress"),
    (0, "DES-1210-28ME_B2", "impbBlackListVlanId"),
    (0, "DES-1210-28ME_B2", "impbBlackListPort"),
)
if mibBuilder.loadTexts:
    impbBlackListEntry.setStatus("current")
_ImpbBlackListMacAddress_Type = MacAddress
_ImpbBlackListMacAddress_Object = MibTableColumn
impbBlackListMacAddress = _ImpbBlackListMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 14, 10, 4, 1, 1),
    _ImpbBlackListMacAddress_Type()
)
impbBlackListMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    impbBlackListMacAddress.setStatus("current")
_ImpbBlackListVlanId_Type = Integer32
_ImpbBlackListVlanId_Object = MibTableColumn
impbBlackListVlanId = _ImpbBlackListVlanId_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 14, 10, 4, 1, 2),
    _ImpbBlackListVlanId_Type()
)
impbBlackListVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    impbBlackListVlanId.setStatus("current")
_ImpbBlackListPort_Type = Integer32
_ImpbBlackListPort_Object = MibTableColumn
impbBlackListPort = _ImpbBlackListPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 14, 10, 4, 1, 3),
    _ImpbBlackListPort_Type()
)
impbBlackListPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    impbBlackListPort.setStatus("current")
_ImpbBlackListIpAddress_Type = IpAddress
_ImpbBlackListIpAddress_Object = MibTableColumn
impbBlackListIpAddress = _ImpbBlackListIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 14, 10, 4, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 14, 10, 4, 1, 5),
    _ImpbBlackListStatus_Type()
)
impbBlackListStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    impbBlackListStatus.setStatus("current")
_ImpbAutoScanIpAddressFrom_Type = IpAddress
_ImpbAutoScanIpAddressFrom_Object = MibScalar
impbAutoScanIpAddressFrom = _ImpbAutoScanIpAddressFrom_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 14, 10, 5),
    _ImpbAutoScanIpAddressFrom_Type()
)
impbAutoScanIpAddressFrom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    impbAutoScanIpAddressFrom.setStatus("current")
_ImpbAutoScanIpAddressTo_Type = IpAddress
_ImpbAutoScanIpAddressTo_Object = MibScalar
impbAutoScanIpAddressTo = _ImpbAutoScanIpAddressTo_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 14, 10, 6),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 14, 10, 7),
    _ImpbAutoScanStatus_Type()
)
impbAutoScanStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    impbAutoScanStatus.setStatus("current")
_SecurityAAC_ObjectIdentity = ObjectIdentity
securityAAC = _SecurityAAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 14, 11)
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 14, 11, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 14, 11, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 14, 11, 3),
    _AacAuthParamAttempt_Type()
)
aacAuthParamAttempt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aacAuthParamAttempt.setStatus("current")
_AacAPAuthMethodGroup_ObjectIdentity = ObjectIdentity
aacAPAuthMethodGroup = _AacAPAuthMethodGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 14, 11, 4)
)
_AacAPLoginMethod_ObjectIdentity = ObjectIdentity
aacAPLoginMethod = _AacAPLoginMethod_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 14, 11, 4, 1)
)


class _AacAPConsoleLoginMethod_Type(Integer32):
    """Custom type aacAPConsoleLoginMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_AacAPConsoleLoginMethod_Type.__name__ = "Integer32"
_AacAPConsoleLoginMethod_Object = MibScalar
aacAPConsoleLoginMethod = _AacAPConsoleLoginMethod_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 14, 11, 4, 1, 1),
    _AacAPConsoleLoginMethod_Type()
)
aacAPConsoleLoginMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aacAPConsoleLoginMethod.setStatus("current")


class _AacAPTelnetLoginMethod_Type(Integer32):
    """Custom type aacAPTelnetLoginMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_AacAPTelnetLoginMethod_Type.__name__ = "Integer32"
_AacAPTelnetLoginMethod_Object = MibScalar
aacAPTelnetLoginMethod = _AacAPTelnetLoginMethod_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 14, 11, 4, 1, 2),
    _AacAPTelnetLoginMethod_Type()
)
aacAPTelnetLoginMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aacAPTelnetLoginMethod.setStatus("current")


class _AacAPSSHLoginMethod_Type(Integer32):
    """Custom type aacAPSSHLoginMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_AacAPSSHLoginMethod_Type.__name__ = "Integer32"
_AacAPSSHLoginMethod_Object = MibScalar
aacAPSSHLoginMethod = _AacAPSSHLoginMethod_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 14, 11, 4, 1, 3),
    _AacAPSSHLoginMethod_Type()
)
aacAPSSHLoginMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aacAPSSHLoginMethod.setStatus("current")


class _AacAPHttpLoginMethod_Type(Integer32):
    """Custom type aacAPHttpLoginMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_AacAPHttpLoginMethod_Type.__name__ = "Integer32"
_AacAPHttpLoginMethod_Object = MibScalar
aacAPHttpLoginMethod = _AacAPHttpLoginMethod_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 14, 11, 4, 1, 4),
    _AacAPHttpLoginMethod_Type()
)
aacAPHttpLoginMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aacAPHttpLoginMethod.setStatus("current")
_AacAPEnableMethod_ObjectIdentity = ObjectIdentity
aacAPEnableMethod = _AacAPEnableMethod_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 14, 11, 4, 2)
)


class _AacAPConsoleEnableMethod_Type(Integer32):
    """Custom type aacAPConsoleEnableMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_AacAPConsoleEnableMethod_Type.__name__ = "Integer32"
_AacAPConsoleEnableMethod_Object = MibScalar
aacAPConsoleEnableMethod = _AacAPConsoleEnableMethod_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 14, 11, 4, 2, 1),
    _AacAPConsoleEnableMethod_Type()
)
aacAPConsoleEnableMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aacAPConsoleEnableMethod.setStatus("current")


class _AacAPTelnetEnableMethod_Type(Integer32):
    """Custom type aacAPTelnetEnableMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_AacAPTelnetEnableMethod_Type.__name__ = "Integer32"
_AacAPTelnetEnableMethod_Object = MibScalar
aacAPTelnetEnableMethod = _AacAPTelnetEnableMethod_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 14, 11, 4, 2, 2),
    _AacAPTelnetEnableMethod_Type()
)
aacAPTelnetEnableMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aacAPTelnetEnableMethod.setStatus("current")


class _AacAPSSHEnableMethod_Type(Integer32):
    """Custom type aacAPSSHEnableMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_AacAPSSHEnableMethod_Type.__name__ = "Integer32"
_AacAPSSHEnableMethod_Object = MibScalar
aacAPSSHEnableMethod = _AacAPSSHEnableMethod_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 14, 11, 4, 2, 3),
    _AacAPSSHEnableMethod_Type()
)
aacAPSSHEnableMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aacAPSSHEnableMethod.setStatus("current")


class _AacAPHttpEnableMethod_Type(Integer32):
    """Custom type aacAPHttpEnableMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_AacAPHttpEnableMethod_Type.__name__ = "Integer32"
_AacAPHttpEnableMethod_Object = MibScalar
aacAPHttpEnableMethod = _AacAPHttpEnableMethod_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 14, 11, 4, 2, 4),
    _AacAPHttpEnableMethod_Type()
)
aacAPHttpEnableMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aacAPHttpEnableMethod.setStatus("current")
_AacServerGroupTable_Object = MibTable
aacServerGroupTable = _AacServerGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 14, 11, 5)
)
if mibBuilder.loadTexts:
    aacServerGroupTable.setStatus("current")
_AacServerGroupEntry_Object = MibTableRow
aacServerGroupEntry = _AacServerGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 14, 11, 5, 1)
)
aacServerGroupEntry.setIndexNames(
    (0, "DES-1210-28ME_B2", "aacServerGroupIndex"),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 14, 11, 5, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 14, 11, 5, 1, 2),
    _AacServerGroupName_Type()
)
aacServerGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aacServerGroupName.setStatus("current")


class _AacServersInGroup_Type(Bits):
    """Custom type aacServersInGroup based on Bits"""
    namedValues = NamedValues(
        *(("id_1", 0),
          ("id_10", 9),
          ("id_11", 10),
          ("id_12", 11),
          ("id_13", 12),
          ("id_14", 13),
          ("id_15", 14),
          ("id_16", 15),
          ("id_2", 1),
          ("id_3", 2),
          ("id_4", 3),
          ("id_5", 4),
          ("id_6", 5),
          ("id_7", 6),
          ("id_8", 7),
          ("id_9", 8))
    )

_AacServersInGroup_Type.__name__ = "Bits"
_AacServersInGroup_Object = MibTableColumn
aacServersInGroup = _AacServersInGroup_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 14, 11, 5, 1, 3),
    _AacServersInGroup_Type()
)
aacServersInGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aacServersInGroup.setStatus("current")
_AacServerGroupRowStatus_Type = RowStatus
_AacServerGroupRowStatus_Object = MibTableColumn
aacServerGroupRowStatus = _AacServerGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 14, 11, 5, 1, 4),
    _AacServerGroupRowStatus_Type()
)
aacServerGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aacServerGroupRowStatus.setStatus("current")
_AacServerInfoTable_Object = MibTable
aacServerInfoTable = _AacServerInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 14, 11, 6)
)
if mibBuilder.loadTexts:
    aacServerInfoTable.setStatus("current")
_AacServerInfoEntry_Object = MibTableRow
aacServerInfoEntry = _AacServerInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 14, 11, 6, 1)
)
aacServerInfoEntry.setIndexNames(
    (0, "DES-1210-28ME_B2", "aacServerIndex"),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 14, 11, 6, 1, 1),
    _AacServerIndex_Type()
)
aacServerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aacServerIndex.setStatus("current")
_AacServerIPAddr_Type = IpAddress
_AacServerIPAddr_Object = MibTableColumn
aacServerIPAddr = _AacServerIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 14, 11, 6, 1, 2),
    _AacServerIPAddr_Type()
)
aacServerIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aacServerIPAddr.setStatus("current")


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
          ("tacacs-plus", 1))
    )


_AacServerAuthProtocol_Type.__name__ = "Integer32"
_AacServerAuthProtocol_Object = MibTableColumn
aacServerAuthProtocol = _AacServerAuthProtocol_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 14, 11, 6, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 14, 11, 6, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 14, 11, 6, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 14, 11, 6, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 14, 11, 6, 1, 7),
    _AacServerRetryCount_Type()
)
aacServerRetryCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aacServerRetryCount.setStatus("current")
_AacServerRowStatus_Type = RowStatus
_AacServerRowStatus_Object = MibTableColumn
aacServerRowStatus = _AacServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 14, 11, 6, 1, 8),
    _AacServerRowStatus_Type()
)
aacServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aacServerRowStatus.setStatus("current")
_AacLoginMethodListTable_Object = MibTable
aacLoginMethodListTable = _AacLoginMethodListTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 14, 11, 7)
)
if mibBuilder.loadTexts:
    aacLoginMethodListTable.setStatus("current")
_AacLoginMethodListEntry_Object = MibTableRow
aacLoginMethodListEntry = _AacLoginMethodListEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 14, 11, 7, 1)
)
aacLoginMethodListEntry.setIndexNames(
    (0, "DES-1210-28ME_B2", "aacLoginMethodListIndex"),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 14, 11, 7, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 14, 11, 7, 1, 2),
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
          ("tacacs-plus", 1))
    )


_AacLoginMethod1_Type.__name__ = "Integer32"
_AacLoginMethod1_Object = MibTableColumn
aacLoginMethod1 = _AacLoginMethod1_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 14, 11, 7, 1, 3),
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
          ("tacacs-plus", 1))
    )


_AacLoginMethod2_Type.__name__ = "Integer32"
_AacLoginMethod2_Object = MibTableColumn
aacLoginMethod2 = _AacLoginMethod2_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 14, 11, 7, 1, 4),
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
          ("tacacs-plus", 1))
    )


_AacLoginMethod3_Type.__name__ = "Integer32"
_AacLoginMethod3_Object = MibTableColumn
aacLoginMethod3 = _AacLoginMethod3_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 14, 11, 7, 1, 5),
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
          ("tacacs-plus", 1))
    )


_AacLoginMethod4_Type.__name__ = "Integer32"
_AacLoginMethod4_Object = MibTableColumn
aacLoginMethod4 = _AacLoginMethod4_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 14, 11, 7, 1, 6),
    _AacLoginMethod4_Type()
)
aacLoginMethod4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aacLoginMethod4.setStatus("current")
_AacLoginMethodListRowStatus_Type = RowStatus
_AacLoginMethodListRowStatus_Object = MibTableColumn
aacLoginMethodListRowStatus = _AacLoginMethodListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 14, 11, 7, 1, 7),
    _AacLoginMethodListRowStatus_Type()
)
aacLoginMethodListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aacLoginMethodListRowStatus.setStatus("current")
_AacEnableMethodListTable_Object = MibTable
aacEnableMethodListTable = _AacEnableMethodListTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 14, 11, 8)
)
if mibBuilder.loadTexts:
    aacEnableMethodListTable.setStatus("current")
_AacEnableMethodListEntry_Object = MibTableRow
aacEnableMethodListEntry = _AacEnableMethodListEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 14, 11, 8, 1)
)
aacEnableMethodListEntry.setIndexNames(
    (0, "DES-1210-28ME_B2", "aacEnableMethodListIndex"),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 14, 11, 8, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 14, 11, 8, 1, 2),
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
          ("tacacs-plus", 1))
    )


_AacEnableMethod1_Type.__name__ = "Integer32"
_AacEnableMethod1_Object = MibTableColumn
aacEnableMethod1 = _AacEnableMethod1_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 14, 11, 8, 1, 3),
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
          ("tacacs-plus", 1))
    )


_AacEnableMethod2_Type.__name__ = "Integer32"
_AacEnableMethod2_Object = MibTableColumn
aacEnableMethod2 = _AacEnableMethod2_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 14, 11, 8, 1, 4),
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
          ("tacacs-plus", 1))
    )


_AacEnableMethod3_Type.__name__ = "Integer32"
_AacEnableMethod3_Object = MibTableColumn
aacEnableMethod3 = _AacEnableMethod3_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 14, 11, 8, 1, 5),
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
          ("tacacs-plus", 1))
    )


_AacEnableMethod4_Type.__name__ = "Integer32"
_AacEnableMethod4_Object = MibTableColumn
aacEnableMethod4 = _AacEnableMethod4_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 14, 11, 8, 1, 6),
    _AacEnableMethod4_Type()
)
aacEnableMethod4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aacEnableMethod4.setStatus("current")
_AacEnableMethodListRowStatus_Type = RowStatus
_AacEnableMethodListRowStatus_Object = MibTableColumn
aacEnableMethodListRowStatus = _AacEnableMethodListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 14, 11, 8, 1, 7),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 14, 11, 9),
    _AacLocalEnablePassword_Type()
)
aacLocalEnablePassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aacLocalEnablePassword.setStatus("current")
_CompanyACLGroup_ObjectIdentity = ObjectIdentity
companyACLGroup = _CompanyACLGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 15)
)
_AclProfile_ObjectIdentity = ObjectIdentity
aclProfile = _AclProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 15, 1)
)
_AclProfileTable_Object = MibTable
aclProfileTable = _AclProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 15, 1, 1)
)
if mibBuilder.loadTexts:
    aclProfileTable.setStatus("current")
_AclProfileEntry_Object = MibTableRow
aclProfileEntry = _AclProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 15, 1, 1, 1)
)
aclProfileEntry.setIndexNames(
    (0, "DES-1210-28ME_B2", "aclProfileNo"),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 15, 1, 1, 1, 1),
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
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("aclQos", 8),
          ("arpSP_deny", 5),
          ("arpSP_permit", 4),
          ("impb", 3),
          ("l2", 1),
          ("l3", 2),
          ("userDefined", 9))
    )


_AclProfileType_Type.__name__ = "Integer32"
_AclProfileType_Object = MibTableColumn
aclProfileType = _AclProfileType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 15, 1, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 15, 1, 1, 1, 3),
    _AclProfileRuleCount_Type()
)
aclProfileRuleCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclProfileRuleCount.setStatus("current")
_AclProfileMask_Type = OctetString
_AclProfileMask_Object = MibTableColumn
aclProfileMask = _AclProfileMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 15, 1, 1, 1, 4),
    _AclProfileMask_Type()
)
aclProfileMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclProfileMask.setStatus("current")
_AclProfileDstMacAddrMask_Type = MacAddress
_AclProfileDstMacAddrMask_Object = MibTableColumn
aclProfileDstMacAddrMask = _AclProfileDstMacAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 15, 1, 1, 1, 5),
    _AclProfileDstMacAddrMask_Type()
)
aclProfileDstMacAddrMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclProfileDstMacAddrMask.setStatus("current")
_AclProfileSrcMacAddrMask_Type = MacAddress
_AclProfileSrcMacAddrMask_Object = MibTableColumn
aclProfileSrcMacAddrMask = _AclProfileSrcMacAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 15, 1, 1, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 15, 1, 1, 1, 7),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 15, 1, 1, 1, 8),
    _AclProfileIPProtocolMask_Type()
)
aclProfileIPProtocolMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclProfileIPProtocolMask.setStatus("current")


class _AclProfileDstIpAddrMask_Type(IpAddress):
    """Custom type aclProfileDstIpAddrMask based on IpAddress"""
    defaultHexValue = "FFFFFFFF"


_AclProfileDstIpAddrMask_Object = MibTableColumn
aclProfileDstIpAddrMask = _AclProfileDstIpAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 15, 1, 1, 1, 9),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 15, 1, 1, 1, 10),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 15, 1, 1, 1, 11),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 15, 1, 1, 1, 12),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 15, 1, 1, 1, 13),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 15, 1, 1, 1, 14),
    _AclProfileArpSenderIpAddrMask_Type()
)
aclProfileArpSenderIpAddrMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclProfileArpSenderIpAddrMask.setStatus("current")
_AclProfileUdfOffsetMap_Type = OctetString
_AclProfileUdfOffsetMap_Object = MibTableColumn
aclProfileUdfOffsetMap = _AclProfileUdfOffsetMap_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 15, 1, 1, 1, 15),
    _AclProfileUdfOffsetMap_Type()
)
aclProfileUdfOffsetMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclProfileUdfOffsetMap.setStatus("current")


class _AclUdfOffsetBase1_Type(Integer32):
    """Custom type aclUdfOffsetBase1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("l2", 0),
          ("l3", 2),
          ("l4", 3))
    )


_AclUdfOffsetBase1_Type.__name__ = "Integer32"
_AclUdfOffsetBase1_Object = MibTableColumn
aclUdfOffsetBase1 = _AclUdfOffsetBase1_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 15, 1, 1, 1, 16),
    _AclUdfOffsetBase1_Type()
)
aclUdfOffsetBase1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclUdfOffsetBase1.setStatus("current")


class _AclUdfOffsetByte1_Type(Integer32):
    """Custom type aclUdfOffsetByte1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_AclUdfOffsetByte1_Type.__name__ = "Integer32"
_AclUdfOffsetByte1_Object = MibTableColumn
aclUdfOffsetByte1 = _AclUdfOffsetByte1_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 15, 1, 1, 1, 17),
    _AclUdfOffsetByte1_Type()
)
aclUdfOffsetByte1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclUdfOffsetByte1.setStatus("current")


class _AclUdfOffsetMask1_Type(OctetString):
    """Custom type aclUdfOffsetMask1 based on OctetString"""
    defaultHexValue = "FFFFFFFF"


_AclUdfOffsetMask1_Object = MibTableColumn
aclUdfOffsetMask1 = _AclUdfOffsetMask1_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 15, 1, 1, 1, 18),
    _AclUdfOffsetMask1_Type()
)
aclUdfOffsetMask1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclUdfOffsetMask1.setStatus("current")


class _AclUdfOffsetBase2_Type(Integer32):
    """Custom type aclUdfOffsetBase2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("l2", 0),
          ("l3", 2),
          ("l4", 3))
    )


_AclUdfOffsetBase2_Type.__name__ = "Integer32"
_AclUdfOffsetBase2_Object = MibTableColumn
aclUdfOffsetBase2 = _AclUdfOffsetBase2_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 15, 1, 1, 1, 19),
    _AclUdfOffsetBase2_Type()
)
aclUdfOffsetBase2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclUdfOffsetBase2.setStatus("current")


class _AclUdfOffsetByte2_Type(Integer32):
    """Custom type aclUdfOffsetByte2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_AclUdfOffsetByte2_Type.__name__ = "Integer32"
_AclUdfOffsetByte2_Object = MibTableColumn
aclUdfOffsetByte2 = _AclUdfOffsetByte2_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 15, 1, 1, 1, 20),
    _AclUdfOffsetByte2_Type()
)
aclUdfOffsetByte2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclUdfOffsetByte2.setStatus("current")


class _AclUdfOffsetMask2_Type(OctetString):
    """Custom type aclUdfOffsetMask2 based on OctetString"""
    defaultHexValue = "FFFFFFFF"


_AclUdfOffsetMask2_Object = MibTableColumn
aclUdfOffsetMask2 = _AclUdfOffsetMask2_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 15, 1, 1, 1, 21),
    _AclUdfOffsetMask2_Type()
)
aclUdfOffsetMask2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclUdfOffsetMask2.setStatus("current")


class _AclUdfOffsetBase3_Type(Integer32):
    """Custom type aclUdfOffsetBase3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("l2", 0),
          ("l3", 2),
          ("l4", 3))
    )


_AclUdfOffsetBase3_Type.__name__ = "Integer32"
_AclUdfOffsetBase3_Object = MibTableColumn
aclUdfOffsetBase3 = _AclUdfOffsetBase3_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 15, 1, 1, 1, 22),
    _AclUdfOffsetBase3_Type()
)
aclUdfOffsetBase3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclUdfOffsetBase3.setStatus("current")


class _AclUdfOffsetByte3_Type(Integer32):
    """Custom type aclUdfOffsetByte3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_AclUdfOffsetByte3_Type.__name__ = "Integer32"
_AclUdfOffsetByte3_Object = MibTableColumn
aclUdfOffsetByte3 = _AclUdfOffsetByte3_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 15, 1, 1, 1, 23),
    _AclUdfOffsetByte3_Type()
)
aclUdfOffsetByte3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclUdfOffsetByte3.setStatus("current")


class _AclUdfOffsetMask3_Type(OctetString):
    """Custom type aclUdfOffsetMask3 based on OctetString"""
    defaultHexValue = "FFFFFFFF"


_AclUdfOffsetMask3_Object = MibTableColumn
aclUdfOffsetMask3 = _AclUdfOffsetMask3_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 15, 1, 1, 1, 24),
    _AclUdfOffsetMask3_Type()
)
aclUdfOffsetMask3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclUdfOffsetMask3.setStatus("current")


class _AclUdfOffsetBase4_Type(Integer32):
    """Custom type aclUdfOffsetBase4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("l2", 0),
          ("l3", 2),
          ("l4", 3))
    )


_AclUdfOffsetBase4_Type.__name__ = "Integer32"
_AclUdfOffsetBase4_Object = MibTableColumn
aclUdfOffsetBase4 = _AclUdfOffsetBase4_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 15, 1, 1, 1, 25),
    _AclUdfOffsetBase4_Type()
)
aclUdfOffsetBase4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclUdfOffsetBase4.setStatus("current")


class _AclUdfOffsetByte4_Type(Integer32):
    """Custom type aclUdfOffsetByte4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_AclUdfOffsetByte4_Type.__name__ = "Integer32"
_AclUdfOffsetByte4_Object = MibTableColumn
aclUdfOffsetByte4 = _AclUdfOffsetByte4_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 15, 1, 1, 1, 26),
    _AclUdfOffsetByte4_Type()
)
aclUdfOffsetByte4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclUdfOffsetByte4.setStatus("current")


class _AclUdfOffsetMask4_Type(OctetString):
    """Custom type aclUdfOffsetMask4 based on OctetString"""
    defaultHexValue = "FFFFFFFF"


_AclUdfOffsetMask4_Object = MibTableColumn
aclUdfOffsetMask4 = _AclUdfOffsetMask4_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 15, 1, 1, 1, 27),
    _AclUdfOffsetMask4_Type()
)
aclUdfOffsetMask4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclUdfOffsetMask4.setStatus("current")
_AclProfileStatus_Type = RowStatus
_AclProfileStatus_Object = MibTableColumn
aclProfileStatus = _AclProfileStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 15, 1, 1, 1, 28),
    _AclProfileStatus_Type()
)
aclProfileStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclProfileStatus.setStatus("current")
_AclL2Rule_ObjectIdentity = ObjectIdentity
aclL2Rule = _AclL2Rule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 15, 2)
)
_AclL2RuleTable_Object = MibTable
aclL2RuleTable = _AclL2RuleTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 15, 2, 1)
)
if mibBuilder.loadTexts:
    aclL2RuleTable.setStatus("current")
_AclL2RuleEntry_Object = MibTableRow
aclL2RuleEntry = _AclL2RuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 15, 2, 1, 1)
)
aclL2RuleEntry.setIndexNames(
    (0, "DES-1210-28ME_B2", "aclL2ProfileID"),
    (0, "DES-1210-28ME_B2", "aclL2AccessID"),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 15, 2, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 15, 2, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 15, 2, 1, 1, 3),
    _AclL2RuleEtherType_Type()
)
aclL2RuleEtherType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL2RuleEtherType.setStatus("current")
_AclL2RuleDstMacAddr_Type = MacAddress
_AclL2RuleDstMacAddr_Object = MibTableColumn
aclL2RuleDstMacAddr = _AclL2RuleDstMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 15, 2, 1, 1, 4),
    _AclL2RuleDstMacAddr_Type()
)
aclL2RuleDstMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL2RuleDstMacAddr.setStatus("current")
_AclL2RuleSrcMacAddr_Type = MacAddress
_AclL2RuleSrcMacAddr_Object = MibTableColumn
aclL2RuleSrcMacAddr = _AclL2RuleSrcMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 15, 2, 1, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 15, 2, 1, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 15, 2, 1, 1, 7),
    _AclL2Rule1pPriority_Type()
)
aclL2Rule1pPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL2Rule1pPriority.setStatus("current")
_AclL2RuleDstMacAddrMask_Type = MacAddress
_AclL2RuleDstMacAddrMask_Object = MibTableColumn
aclL2RuleDstMacAddrMask = _AclL2RuleDstMacAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 15, 2, 1, 1, 8),
    _AclL2RuleDstMacAddrMask_Type()
)
aclL2RuleDstMacAddrMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclL2RuleDstMacAddrMask.setStatus("current")
_AclL2RuleSrcMacAddrMask_Type = MacAddress
_AclL2RuleSrcMacAddrMask_Object = MibTableColumn
aclL2RuleSrcMacAddrMask = _AclL2RuleSrcMacAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 15, 2, 1, 1, 9),
    _AclL2RuleSrcMacAddrMask_Type()
)
aclL2RuleSrcMacAddrMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclL2RuleSrcMacAddrMask.setStatus("current")
_AclL2RuleInPortList_Type = PortList
_AclL2RuleInPortList_Object = MibTableColumn
aclL2RuleInPortList = _AclL2RuleInPortList_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 15, 2, 1, 1, 10),
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
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("drop", 2),
          ("mirror", 3),
          ("rateLimit", 4),
          ("replace1P", 6),
          ("replaceDSCP", 5))
    )


_AclL2RuleAction_Type.__name__ = "Integer32"
_AclL2RuleAction_Object = MibTableColumn
aclL2RuleAction = _AclL2RuleAction_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 15, 2, 1, 1, 11),
    _AclL2RuleAction_Type()
)
aclL2RuleAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL2RuleAction.setStatus("current")
_AclL2RuleRateLimit_Type = Unsigned32
_AclL2RuleRateLimit_Object = MibTableColumn
aclL2RuleRateLimit = _AclL2RuleRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 15, 2, 1, 1, 12),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 15, 2, 1, 1, 13),
    _AclL2RuleReplaceDSCP_Type()
)
aclL2RuleReplaceDSCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL2RuleReplaceDSCP.setStatus("current")


class _AclL2RuleReplace1P_Type(Integer32):
    """Custom type aclL2RuleReplace1P based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 7),
    )


_AclL2RuleReplace1P_Type.__name__ = "Integer32"
_AclL2RuleReplace1P_Object = MibTableColumn
aclL2RuleReplace1P = _AclL2RuleReplace1P_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 15, 2, 1, 1, 14),
    _AclL2RuleReplace1P_Type()
)
aclL2RuleReplace1P.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL2RuleReplace1P.setStatus("current")
_AclL2RuleStatus_Type = RowStatus
_AclL2RuleStatus_Object = MibTableColumn
aclL2RuleStatus = _AclL2RuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 15, 2, 1, 1, 15),
    _AclL2RuleStatus_Type()
)
aclL2RuleStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclL2RuleStatus.setStatus("current")
_AclL3Rule_ObjectIdentity = ObjectIdentity
aclL3Rule = _AclL3Rule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 15, 3)
)
_AclL3RuleTable_Object = MibTable
aclL3RuleTable = _AclL3RuleTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 15, 3, 1)
)
if mibBuilder.loadTexts:
    aclL3RuleTable.setStatus("current")
_AclL3RuleEntry_Object = MibTableRow
aclL3RuleEntry = _AclL3RuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 15, 3, 1, 1)
)
aclL3RuleEntry.setIndexNames(
    (0, "DES-1210-28ME_B2", "aclL3RuleProfileNo"),
    (0, "DES-1210-28ME_B2", "aclL3RuleAccessID"),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 15, 3, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 15, 3, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 15, 3, 1, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 15, 3, 1, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 15, 3, 1, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 15, 3, 1, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 15, 3, 1, 1, 7),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 15, 3, 1, 1, 8),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 15, 3, 1, 1, 9),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 15, 3, 1, 1, 10),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 15, 3, 1, 1, 11),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 15, 3, 1, 1, 12),
    _AclL3RuleTcpUdpSrcPort_Type()
)
aclL3RuleTcpUdpSrcPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3RuleTcpUdpSrcPort.setStatus("current")
_AclL3RuleTcpUdpDstPortMask_Type = OctetString
_AclL3RuleTcpUdpDstPortMask_Object = MibTableColumn
aclL3RuleTcpUdpDstPortMask = _AclL3RuleTcpUdpDstPortMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 15, 3, 1, 1, 13),
    _AclL3RuleTcpUdpDstPortMask_Type()
)
aclL3RuleTcpUdpDstPortMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclL3RuleTcpUdpDstPortMask.setStatus("current")
_AclL3RuleTcpUdpSrcPortMask_Type = OctetString
_AclL3RuleTcpUdpSrcPortMask_Object = MibTableColumn
aclL3RuleTcpUdpSrcPortMask = _AclL3RuleTcpUdpSrcPortMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 15, 3, 1, 1, 14),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 15, 3, 1, 1, 15),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 15, 3, 1, 1, 16),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 15, 3, 1, 1, 17),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 15, 3, 1, 1, 18),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 15, 3, 1, 1, 19),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 15, 3, 1, 1, 20),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 15, 3, 1, 1, 21),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 15, 3, 1, 1, 22),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 15, 3, 1, 1, 23),
    _AclL3RuleIgmpType_Type()
)
aclL3RuleIgmpType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3RuleIgmpType.setStatus("current")
_AclL3RulePortList_Type = PortList
_AclL3RulePortList_Object = MibTableColumn
aclL3RulePortList = _AclL3RulePortList_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 15, 3, 1, 1, 24),
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
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("drop", 2),
          ("mirror", 3),
          ("rateLimit", 4),
          ("replace1P", 6),
          ("replaceDSCP", 5))
    )


_AclL3RuleAction_Type.__name__ = "Integer32"
_AclL3RuleAction_Object = MibTableColumn
aclL3RuleAction = _AclL3RuleAction_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 15, 3, 1, 1, 25),
    _AclL3RuleAction_Type()
)
aclL3RuleAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3RuleAction.setStatus("current")
_AclL3RuleRateLimit_Type = Unsigned32
_AclL3RuleRateLimit_Object = MibTableColumn
aclL3RuleRateLimit = _AclL3RuleRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 15, 3, 1, 1, 26),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 15, 3, 1, 1, 27),
    _AclL3RuleReplaceDSCP_Type()
)
aclL3RuleReplaceDSCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3RuleReplaceDSCP.setStatus("current")


class _AclL3RuleReplace1P_Type(Integer32):
    """Custom type aclL3RuleReplace1P based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 7),
    )


_AclL3RuleReplace1P_Type.__name__ = "Integer32"
_AclL3RuleReplace1P_Object = MibTableColumn
aclL3RuleReplace1P = _AclL3RuleReplace1P_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 15, 3, 1, 1, 28),
    _AclL3RuleReplace1P_Type()
)
aclL3RuleReplace1P.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3RuleReplace1P.setStatus("current")
_AclL3RuleStatus_Type = RowStatus
_AclL3RuleStatus_Object = MibTableColumn
aclL3RuleStatus = _AclL3RuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 15, 3, 1, 1, 29),
    _AclL3RuleStatus_Type()
)
aclL3RuleStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclL3RuleStatus.setStatus("current")
_AclPacketRule_ObjectIdentity = ObjectIdentity
aclPacketRule = _AclPacketRule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 15, 4)
)
_AclPacketRuleTable_Object = MibTable
aclPacketRuleTable = _AclPacketRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 15, 4, 1)
)
if mibBuilder.loadTexts:
    aclPacketRuleTable.setStatus("current")
_AclPacketRuleEntry_Object = MibTableRow
aclPacketRuleEntry = _AclPacketRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 15, 4, 1, 1)
)
aclPacketRuleEntry.setIndexNames(
    (0, "DES-1210-28ME_B2", "aclPacketProfileID"),
    (0, "DES-1210-28ME_B2", "aclPacketAccessID"),
)
if mibBuilder.loadTexts:
    aclPacketRuleEntry.setStatus("current")


class _AclPacketAccessID_Type(Integer32):
    """Custom type aclPacketAccessID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AclPacketAccessID_Type.__name__ = "Integer32"
_AclPacketAccessID_Object = MibTableColumn
aclPacketAccessID = _AclPacketAccessID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 15, 4, 1, 1, 1),
    _AclPacketAccessID_Type()
)
aclPacketAccessID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclPacketAccessID.setStatus("current")


class _AclPacketProfileID_Type(Integer32):
    """Custom type aclPacketProfileID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_AclPacketProfileID_Type.__name__ = "Integer32"
_AclPacketProfileID_Object = MibTableColumn
aclPacketProfileID = _AclPacketProfileID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 15, 4, 1, 1, 2),
    _AclPacketProfileID_Type()
)
aclPacketProfileID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclPacketProfileID.setStatus("current")
_AclPacketRuleOffsetValue1_Type = OctetString
_AclPacketRuleOffsetValue1_Object = MibTableColumn
aclPacketRuleOffsetValue1 = _AclPacketRuleOffsetValue1_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 15, 4, 1, 1, 3),
    _AclPacketRuleOffsetValue1_Type()
)
aclPacketRuleOffsetValue1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclPacketRuleOffsetValue1.setStatus("current")
_AclPacketRuleOffsetValue2_Type = OctetString
_AclPacketRuleOffsetValue2_Object = MibTableColumn
aclPacketRuleOffsetValue2 = _AclPacketRuleOffsetValue2_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 15, 4, 1, 1, 4),
    _AclPacketRuleOffsetValue2_Type()
)
aclPacketRuleOffsetValue2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclPacketRuleOffsetValue2.setStatus("current")
_AclPacketRuleOffsetValue3_Type = OctetString
_AclPacketRuleOffsetValue3_Object = MibTableColumn
aclPacketRuleOffsetValue3 = _AclPacketRuleOffsetValue3_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 15, 4, 1, 1, 5),
    _AclPacketRuleOffsetValue3_Type()
)
aclPacketRuleOffsetValue3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclPacketRuleOffsetValue3.setStatus("current")
_AclPacketRuleOffsetValue4_Type = OctetString
_AclPacketRuleOffsetValue4_Object = MibTableColumn
aclPacketRuleOffsetValue4 = _AclPacketRuleOffsetValue4_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 15, 4, 1, 1, 6),
    _AclPacketRuleOffsetValue4_Type()
)
aclPacketRuleOffsetValue4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclPacketRuleOffsetValue4.setStatus("current")
_AclPacketRuleInPortList_Type = PortList
_AclPacketRuleInPortList_Object = MibTableColumn
aclPacketRuleInPortList = _AclPacketRuleInPortList_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 15, 4, 1, 1, 7),
    _AclPacketRuleInPortList_Type()
)
aclPacketRuleInPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclPacketRuleInPortList.setStatus("current")


class _AclPacketRuleAction_Type(Integer32):
    """Custom type aclPacketRuleAction based on Integer32"""
    defaultValue = 1

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
        *(("allow", 1),
          ("drop", 2),
          ("mirror", 3),
          ("rateLimit", 4),
          ("replace1P", 6),
          ("replaceDSCP", 5))
    )


_AclPacketRuleAction_Type.__name__ = "Integer32"
_AclPacketRuleAction_Object = MibTableColumn
aclPacketRuleAction = _AclPacketRuleAction_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 15, 4, 1, 1, 8),
    _AclPacketRuleAction_Type()
)
aclPacketRuleAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclPacketRuleAction.setStatus("current")
_AclPacketRuleRateLimit_Type = Unsigned32
_AclPacketRuleRateLimit_Object = MibTableColumn
aclPacketRuleRateLimit = _AclPacketRuleRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 15, 4, 1, 1, 9),
    _AclPacketRuleRateLimit_Type()
)
aclPacketRuleRateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclPacketRuleRateLimit.setStatus("current")


class _AclPacketRuleReplaceDSCP_Type(Integer32):
    """Custom type aclPacketRuleReplaceDSCP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 63),
    )


_AclPacketRuleReplaceDSCP_Type.__name__ = "Integer32"
_AclPacketRuleReplaceDSCP_Object = MibTableColumn
aclPacketRuleReplaceDSCP = _AclPacketRuleReplaceDSCP_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 15, 4, 1, 1, 10),
    _AclPacketRuleReplaceDSCP_Type()
)
aclPacketRuleReplaceDSCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclPacketRuleReplaceDSCP.setStatus("current")


class _AclPacketRuleReplace1P_Type(Integer32):
    """Custom type aclPacketRuleReplace1P based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 7),
    )


_AclPacketRuleReplace1P_Type.__name__ = "Integer32"
_AclPacketRuleReplace1P_Object = MibTableColumn
aclPacketRuleReplace1P = _AclPacketRuleReplace1P_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 15, 4, 1, 1, 11),
    _AclPacketRuleReplace1P_Type()
)
aclPacketRuleReplace1P.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclPacketRuleReplace1P.setStatus("current")
_AclPacketRuleStatus_Type = RowStatus
_AclPacketRuleStatus_Object = MibTableColumn
aclPacketRuleStatus = _AclPacketRuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 15, 4, 1, 1, 12),
    _AclPacketRuleStatus_Type()
)
aclPacketRuleStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclPacketRuleStatus.setStatus("current")
_CompanySyslog_ObjectIdentity = ObjectIdentity
companySyslog = _CompanySyslog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 16)
)
_SyslogSettingGroup_ObjectIdentity = ObjectIdentity
syslogSettingGroup = _SyslogSettingGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 16, 1)
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 16, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 16, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 16, 1, 3),
    _SyslogSaveMinutes_Type()
)
syslogSaveMinutes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogSaveMinutes.setStatus("current")
_SyslogServerGroup_ObjectIdentity = ObjectIdentity
syslogServerGroup = _SyslogServerGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 16, 2)
)
_SyslogServTable_Object = MibTable
syslogServTable = _SyslogServTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 16, 2, 1)
)
if mibBuilder.loadTexts:
    syslogServTable.setStatus("current")
_SyslogServEntry_Object = MibTableRow
syslogServEntry = _SyslogServEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 16, 2, 1, 1)
)
syslogServEntry.setIndexNames(
    (0, "DES-1210-28ME_B2", "syslogServIndex"),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 16, 2, 1, 1, 1),
    _SyslogServIndex_Type()
)
syslogServIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syslogServIndex.setStatus("current")
_SyslogServAddr_Type = IpAddress
_SyslogServAddr_Object = MibTableColumn
syslogServAddr = _SyslogServAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 16, 2, 1, 1, 2),
    _SyslogServAddr_Type()
)
syslogServAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogServAddr.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 16, 2, 1, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 16, 2, 1, 1, 4),
    _SyslogServFacility_Type()
)
syslogServFacility.setMaxAccess("read-write")
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 16, 2, 1, 1, 5),
    _SyslogServUDPport_Type()
)
syslogServUDPport.setMaxAccess("read-write")
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 16, 2, 1, 1, 6),
    _SyslogServSrvStatus_Type()
)
syslogServSrvStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogServSrvStatus.setStatus("current")
_SyslogServSrvRowStatus_Type = RowStatus
_SyslogServSrvRowStatus_Object = MibTableColumn
syslogServSrvRowStatus = _SyslogServSrvRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 16, 2, 1, 1, 7),
    _SyslogServSrvRowStatus_Type()
)
syslogServSrvRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogServSrvRowStatus.setStatus("current")
_CompanyLBD_ObjectIdentity = ObjectIdentity
companyLBD = _CompanyLBD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 17)
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 17, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 17, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 17, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 17, 4),
    _SysLBDRecoverTime_Type()
)
sysLBDRecoverTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLBDRecoverTime.setStatus("current")
_SysLBDCtrlTable_Object = MibTable
sysLBDCtrlTable = _SysLBDCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 17, 5)
)
if mibBuilder.loadTexts:
    sysLBDCtrlTable.setStatus("current")
_SysLBDCtrlEntry_Object = MibTableRow
sysLBDCtrlEntry = _SysLBDCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 17, 5, 1)
)
sysLBDCtrlEntry.setIndexNames(
    (0, "DES-1210-28ME_B2", "sysLBDCtrlIndex"),
)
if mibBuilder.loadTexts:
    sysLBDCtrlEntry.setStatus("current")
_SysLBDCtrlIndex_Type = Integer32
_SysLBDCtrlIndex_Object = MibTableColumn
sysLBDCtrlIndex = _SysLBDCtrlIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 17, 5, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 17, 5, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 17, 5, 1, 3),
    _SysLBDPortLoopStatus_Type()
)
sysLBDPortLoopStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysLBDPortLoopStatus.setStatus("current")
_SysLBDVlanLoopTable_Object = MibTable
sysLBDVlanLoopTable = _SysLBDVlanLoopTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 17, 6)
)
if mibBuilder.loadTexts:
    sysLBDVlanLoopTable.setStatus("current")
_SysLBDVlanLoopEntry_Object = MibTableRow
sysLBDVlanLoopEntry = _SysLBDVlanLoopEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 17, 6, 1)
)
sysLBDVlanLoopEntry.setIndexNames(
    (0, "DES-1210-28ME_B2", "sysLBDVlanLoopIndex"),
)
if mibBuilder.loadTexts:
    sysLBDVlanLoopEntry.setStatus("current")
_SysLBDVlanLoopIndex_Type = Integer32
_SysLBDVlanLoopIndex_Object = MibTableColumn
sysLBDVlanLoopIndex = _SysLBDVlanLoopIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 17, 6, 1, 1),
    _SysLBDVlanLoopIndex_Type()
)
sysLBDVlanLoopIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysLBDVlanLoopIndex.setStatus("current")
_SysLBDVlanLoopPorts_Type = PortList
_SysLBDVlanLoopPorts_Object = MibTableColumn
sysLBDVlanLoopPorts = _SysLBDVlanLoopPorts_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 17, 6, 1, 2),
    _SysLBDVlanLoopPorts_Type()
)
sysLBDVlanLoopPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysLBDVlanLoopPorts.setStatus("current")
_CompanyMirror_ObjectIdentity = ObjectIdentity
companyMirror = _CompanyMirror_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 18)
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 18, 1),
    _SysMirrorStatus_Type()
)
sysMirrorStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysMirrorStatus.setStatus("current")
_SysMirrorTargetPort_Type = Integer32
_SysMirrorTargetPort_Object = MibScalar
sysMirrorTargetPort = _SysMirrorTargetPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 18, 2),
    _SysMirrorTargetPort_Type()
)
sysMirrorTargetPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysMirrorTargetPort.setStatus("current")
_SysMirrorCtrlIngressMirroring_Type = PortList
_SysMirrorCtrlIngressMirroring_Object = MibScalar
sysMirrorCtrlIngressMirroring = _SysMirrorCtrlIngressMirroring_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 18, 3),
    _SysMirrorCtrlIngressMirroring_Type()
)
sysMirrorCtrlIngressMirroring.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysMirrorCtrlIngressMirroring.setStatus("current")
_SysMirrorCtrlEgressMirroring_Type = PortList
_SysMirrorCtrlEgressMirroring_Object = MibScalar
sysMirrorCtrlEgressMirroring = _SysMirrorCtrlEgressMirroring_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 18, 4),
    _SysMirrorCtrlEgressMirroring_Type()
)
sysMirrorCtrlEgressMirroring.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysMirrorCtrlEgressMirroring.setStatus("current")
_CompanyStaticMcast_ObjectIdentity = ObjectIdentity
companyStaticMcast = _CompanyStaticMcast_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 19)
)
_StaticMcastTable_Object = MibTable
staticMcastTable = _StaticMcastTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 19, 1)
)
if mibBuilder.loadTexts:
    staticMcastTable.setStatus("current")
_StaticMcastEntry_Object = MibTableRow
staticMcastEntry = _StaticMcastEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 19, 1, 1)
)
staticMcastEntry.setIndexNames(
    (0, "DES-1210-28ME_B2", "staticMcastVlanID"),
    (0, "DES-1210-28ME_B2", "staticMcastMac"),
    (0, "DES-1210-28ME_B2", "staticMcastEgressPorts"),
)
if mibBuilder.loadTexts:
    staticMcastEntry.setStatus("current")
_StaticMcastVlanID_Type = Integer32
_StaticMcastVlanID_Object = MibTableColumn
staticMcastVlanID = _StaticMcastVlanID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 19, 1, 1, 1),
    _StaticMcastVlanID_Type()
)
staticMcastVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staticMcastVlanID.setStatus("current")
_StaticMcastMac_Type = MacAddress
_StaticMcastMac_Object = MibTableColumn
staticMcastMac = _StaticMcastMac_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 19, 1, 1, 2),
    _StaticMcastMac_Type()
)
staticMcastMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staticMcastMac.setStatus("current")
_StaticMcastEgressPorts_Type = PortList
_StaticMcastEgressPorts_Object = MibTableColumn
staticMcastEgressPorts = _StaticMcastEgressPorts_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 19, 1, 1, 3),
    _StaticMcastEgressPorts_Type()
)
staticMcastEgressPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staticMcastEgressPorts.setStatus("current")
_StaticMcastStatus_Type = RowStatus
_StaticMcastStatus_Object = MibTableColumn
staticMcastStatus = _StaticMcastStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 19, 1, 1, 4),
    _StaticMcastStatus_Type()
)
staticMcastStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticMcastStatus.setStatus("current")
_CompanySNTPSetting_ObjectIdentity = ObjectIdentity
companySNTPSetting = _CompanySNTPSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 20)
)
_SysSNTPTimeSeconds_Type = Integer32
_SysSNTPTimeSeconds_Object = MibScalar
sysSNTPTimeSeconds = _SysSNTPTimeSeconds_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 20, 1),
    _SysSNTPTimeSeconds_Type()
)
sysSNTPTimeSeconds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSNTPTimeSeconds.setStatus("current")
_SysSNTPFirstServer_Type = IpAddress
_SysSNTPFirstServer_Object = MibScalar
sysSNTPFirstServer = _SysSNTPFirstServer_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 20, 2),
    _SysSNTPFirstServer_Type()
)
sysSNTPFirstServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSNTPFirstServer.setStatus("current")
_SysSNTPSecondServer_Type = IpAddress
_SysSNTPSecondServer_Object = MibScalar
sysSNTPSecondServer = _SysSNTPSecondServer_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 20, 3),
    _SysSNTPSecondServer_Type()
)
sysSNTPSecondServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSNTPSecondServer.setStatus("current")
_SysSNTPPollInterval_Type = Integer32
_SysSNTPPollInterval_Object = MibScalar
sysSNTPPollInterval = _SysSNTPPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 20, 4),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 20, 5),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 20, 6),
    _SysSNTPDSTOffset_Type()
)
sysSNTPDSTOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSNTPDSTOffset.setStatus("current")
_SysSNTPGMTMinutes_Type = Integer32
_SysSNTPGMTMinutes_Object = MibScalar
sysSNTPGMTMinutes = _SysSNTPGMTMinutes_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 20, 7),
    _SysSNTPGMTMinutes_Type()
)
sysSNTPGMTMinutes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSNTPGMTMinutes.setStatus("current")
_SysSNTPDSTStartMon_Type = Integer32
_SysSNTPDSTStartMon_Object = MibScalar
sysSNTPDSTStartMon = _SysSNTPDSTStartMon_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 20, 8),
    _SysSNTPDSTStartMon_Type()
)
sysSNTPDSTStartMon.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSNTPDSTStartMon.setStatus("current")
_SysSNTPDSTStartDay_Type = Integer32
_SysSNTPDSTStartDay_Object = MibScalar
sysSNTPDSTStartDay = _SysSNTPDSTStartDay_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 20, 9),
    _SysSNTPDSTStartDay_Type()
)
sysSNTPDSTStartDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSNTPDSTStartDay.setStatus("current")
_SysSNTPDSTStartHour_Type = Integer32
_SysSNTPDSTStartHour_Object = MibScalar
sysSNTPDSTStartHour = _SysSNTPDSTStartHour_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 20, 10),
    _SysSNTPDSTStartHour_Type()
)
sysSNTPDSTStartHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSNTPDSTStartHour.setStatus("current")
_SysSNTPDSTStartMin_Type = Integer32
_SysSNTPDSTStartMin_Object = MibScalar
sysSNTPDSTStartMin = _SysSNTPDSTStartMin_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 20, 11),
    _SysSNTPDSTStartMin_Type()
)
sysSNTPDSTStartMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSNTPDSTStartMin.setStatus("current")
_SysSNTPDSTEndMon_Type = Integer32
_SysSNTPDSTEndMon_Object = MibScalar
sysSNTPDSTEndMon = _SysSNTPDSTEndMon_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 20, 12),
    _SysSNTPDSTEndMon_Type()
)
sysSNTPDSTEndMon.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSNTPDSTEndMon.setStatus("current")
_SysSNTPDSTEndDay_Type = Integer32
_SysSNTPDSTEndDay_Object = MibScalar
sysSNTPDSTEndDay = _SysSNTPDSTEndDay_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 20, 13),
    _SysSNTPDSTEndDay_Type()
)
sysSNTPDSTEndDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSNTPDSTEndDay.setStatus("current")
_SysSNTPDSTEndHour_Type = Integer32
_SysSNTPDSTEndHour_Object = MibScalar
sysSNTPDSTEndHour = _SysSNTPDSTEndHour_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 20, 14),
    _SysSNTPDSTEndHour_Type()
)
sysSNTPDSTEndHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSNTPDSTEndHour.setStatus("current")
_SysSNTPDSTEndMin_Type = Integer32
_SysSNTPDSTEndMin_Object = MibScalar
sysSNTPDSTEndMin = _SysSNTPDSTEndMin_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 20, 15),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 20, 16),
    _SysSNTPDSTState_Type()
)
sysSNTPDSTState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSNTPDSTState.setStatus("current")
_CompanyRMON_ObjectIdentity = ObjectIdentity
companyRMON = _CompanyRMON_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 22)
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 22, 1),
    _RmonGlobalState_Type()
)
rmonGlobalState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmonGlobalState.setStatus("current")
_RmonStatistics_ObjectIdentity = ObjectIdentity
rmonStatistics = _RmonStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 22, 2)
)
_RmonStatsTable_Object = MibTable
rmonStatsTable = _RmonStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 22, 2, 1)
)
if mibBuilder.loadTexts:
    rmonStatsTable.setStatus("current")
_RmonStatsEntry_Object = MibTableRow
rmonStatsEntry = _RmonStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 22, 2, 1, 1)
)
rmonStatsEntry.setIndexNames(
    (0, "DES-1210-28ME_B2", "rmonStatsIndex"),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 22, 2, 1, 1, 1),
    _RmonStatsIndex_Type()
)
rmonStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonStatsIndex.setStatus("current")
_RmonStatsDataSource_Type = ObjectIdentifier
_RmonStatsDataSource_Object = MibTableColumn
rmonStatsDataSource = _RmonStatsDataSource_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 22, 2, 1, 1, 2),
    _RmonStatsDataSource_Type()
)
rmonStatsDataSource.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rmonStatsDataSource.setStatus("current")
_RmonStatsOwner_Type = OwnerString
_RmonStatsOwner_Object = MibTableColumn
rmonStatsOwner = _RmonStatsOwner_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 22, 2, 1, 1, 3),
    _RmonStatsOwner_Type()
)
rmonStatsOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rmonStatsOwner.setStatus("current")
_RmonStatsStatus_Type = RmonStatus
_RmonStatsStatus_Object = MibTableColumn
rmonStatsStatus = _RmonStatsStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 22, 2, 1, 1, 4),
    _RmonStatsStatus_Type()
)
rmonStatsStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rmonStatsStatus.setStatus("current")
_RmonHistory_ObjectIdentity = ObjectIdentity
rmonHistory = _RmonHistory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 22, 3)
)
_RmonHistoryTable_Object = MibTable
rmonHistoryTable = _RmonHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 22, 3, 1)
)
if mibBuilder.loadTexts:
    rmonHistoryTable.setStatus("current")
_RmonHistoryEntry_Object = MibTableRow
rmonHistoryEntry = _RmonHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 22, 3, 1, 1)
)
rmonHistoryEntry.setIndexNames(
    (0, "DES-1210-28ME_B2", "rmonHistoryIndex"),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 22, 3, 1, 1, 1),
    _RmonHistoryIndex_Type()
)
rmonHistoryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonHistoryIndex.setStatus("current")
_RmonHistoryDataSource_Type = ObjectIdentifier
_RmonHistoryDataSource_Object = MibTableColumn
rmonHistoryDataSource = _RmonHistoryDataSource_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 22, 3, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 22, 3, 1, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 22, 3, 1, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 22, 3, 1, 1, 5),
    _RmonHistoryOwner_Type()
)
rmonHistoryOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rmonHistoryOwner.setStatus("current")
_RmonHistoryStatus_Type = RmonStatus
_RmonHistoryStatus_Object = MibTableColumn
rmonHistoryStatus = _RmonHistoryStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 22, 3, 1, 1, 6),
    _RmonHistoryStatus_Type()
)
rmonHistoryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rmonHistoryStatus.setStatus("current")
_RmonAlarm_ObjectIdentity = ObjectIdentity
rmonAlarm = _RmonAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 22, 4)
)
_RmonAlarmTable_Object = MibTable
rmonAlarmTable = _RmonAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 22, 4, 1)
)
if mibBuilder.loadTexts:
    rmonAlarmTable.setStatus("current")
_RmonAlarmEntry_Object = MibTableRow
rmonAlarmEntry = _RmonAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 22, 4, 1, 1)
)
rmonAlarmEntry.setIndexNames(
    (0, "DES-1210-28ME_B2", "rmonAlarmIndex"),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 22, 4, 1, 1, 1),
    _RmonAlarmIndex_Type()
)
rmonAlarmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonAlarmIndex.setStatus("current")
_RmonAlarmInterval_Type = Integer32
_RmonAlarmInterval_Object = MibTableColumn
rmonAlarmInterval = _RmonAlarmInterval_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 22, 4, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 22, 4, 1, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 22, 4, 1, 1, 4),
    _RmonAlarmSampleType_Type()
)
rmonAlarmSampleType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rmonAlarmSampleType.setStatus("current")
_RmonAlarmRisingThreshold_Type = Integer32
_RmonAlarmRisingThreshold_Object = MibTableColumn
rmonAlarmRisingThreshold = _RmonAlarmRisingThreshold_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 22, 4, 1, 1, 5),
    _RmonAlarmRisingThreshold_Type()
)
rmonAlarmRisingThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rmonAlarmRisingThreshold.setStatus("current")
_RmonAlarmFallingThreshold_Type = Integer32
_RmonAlarmFallingThreshold_Object = MibTableColumn
rmonAlarmFallingThreshold = _RmonAlarmFallingThreshold_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 22, 4, 1, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 22, 4, 1, 1, 7),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 22, 4, 1, 1, 8),
    _RmonAlarmFallingEventIndex_Type()
)
rmonAlarmFallingEventIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rmonAlarmFallingEventIndex.setStatus("current")
_RmonAlarmOwner_Type = OwnerString
_RmonAlarmOwner_Object = MibTableColumn
rmonAlarmOwner = _RmonAlarmOwner_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 22, 4, 1, 1, 9),
    _RmonAlarmOwner_Type()
)
rmonAlarmOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rmonAlarmOwner.setStatus("current")
_RmonAlarmStatus_Type = RmonStatus
_RmonAlarmStatus_Object = MibTableColumn
rmonAlarmStatus = _RmonAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 22, 4, 1, 1, 10),
    _RmonAlarmStatus_Type()
)
rmonAlarmStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rmonAlarmStatus.setStatus("current")
_RmonEvent_ObjectIdentity = ObjectIdentity
rmonEvent = _RmonEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 22, 5)
)
_RmonEventTable_Object = MibTable
rmonEventTable = _RmonEventTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 22, 5, 1)
)
if mibBuilder.loadTexts:
    rmonEventTable.setStatus("current")
_RmonEventEntry_Object = MibTableRow
rmonEventEntry = _RmonEventEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 22, 5, 1, 1)
)
rmonEventEntry.setIndexNames(
    (0, "DES-1210-28ME_B2", "rmonEventIndex"),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 22, 5, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 22, 5, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 22, 5, 1, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 22, 5, 1, 1, 4),
    _RmonEventCommunity_Type()
)
rmonEventCommunity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rmonEventCommunity.setStatus("current")
_RmonEventOwner_Type = OwnerString
_RmonEventOwner_Object = MibTableColumn
rmonEventOwner = _RmonEventOwner_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 22, 5, 1, 1, 5),
    _RmonEventOwner_Type()
)
rmonEventOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rmonEventOwner.setStatus("current")
_RmonEventStatus_Type = RmonStatus
_RmonEventStatus_Object = MibTableColumn
rmonEventStatus = _RmonEventStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 22, 5, 1, 1, 6),
    _RmonEventStatus_Type()
)
rmonEventStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rmonEventStatus.setStatus("current")
_CompanyAuthGroup_ObjectIdentity = ObjectIdentity
companyAuthGroup = _CompanyAuthGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 23)
)
_SwAuthenCtrl_ObjectIdentity = ObjectIdentity
swAuthenCtrl = _SwAuthenCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 23, 1)
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 23, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 23, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 23, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 23, 1, 4),
    _SwAuthCtrlPktFwdMode_Type()
)
swAuthCtrlPktFwdMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swAuthCtrlPktFwdMode.setStatus("current")
_SwAuthPortAccessCtrl_ObjectIdentity = ObjectIdentity
swAuthPortAccessCtrl = _SwAuthPortAccessCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 23, 2)
)
_SwAuthPortAccessControlTable_Object = MibTable
swAuthPortAccessControlTable = _SwAuthPortAccessControlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 23, 2, 1)
)
if mibBuilder.loadTexts:
    swAuthPortAccessControlTable.setStatus("current")
_SwAuthPortAccessControlEntry_Object = MibTableRow
swAuthPortAccessControlEntry = _SwAuthPortAccessControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 23, 2, 1, 1)
)
swAuthPortAccessControlEntry.setIndexNames(
    (0, "DES-1210-28ME_B2", "swAuthAuthConfigPortNumber"),
)
if mibBuilder.loadTexts:
    swAuthPortAccessControlEntry.setStatus("current")
_SwAuthAuthConfigPortNumber_Type = Integer32
_SwAuthAuthConfigPortNumber_Object = MibTableColumn
swAuthAuthConfigPortNumber = _SwAuthAuthConfigPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 23, 2, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 23, 2, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 23, 2, 1, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 23, 2, 1, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 23, 2, 1, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 23, 2, 1, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 23, 2, 1, 1, 7),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 23, 2, 1, 1, 8),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 23, 2, 1, 1, 9),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 23, 2, 1, 1, 10),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 23, 2, 1, 1, 11),
    _SwAuthAuthDirection_Type()
)
swAuthAuthDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swAuthAuthDirection.setStatus("current")
_SwAuthUser_ObjectIdentity = ObjectIdentity
swAuthUser = _SwAuthUser_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 23, 3)
)
_SwAuthUserTable_Object = MibTable
swAuthUserTable = _SwAuthUserTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 23, 3, 1)
)
if mibBuilder.loadTexts:
    swAuthUserTable.setStatus("current")
_SwAuthUserEntry_Object = MibTableRow
swAuthUserEntry = _SwAuthUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 23, 3, 1, 1)
)
swAuthUserEntry.setIndexNames(
    (0, "DES-1210-28ME_B2", "swAuthUserName"),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 23, 3, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 23, 3, 1, 1, 2),
    _SwAuthUserPassword_Type()
)
swAuthUserPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swAuthUserPassword.setStatus("current")
_SwAuthUserStatus_Type = RowStatus
_SwAuthUserStatus_Object = MibTableColumn
swAuthUserStatus = _SwAuthUserStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 23, 3, 1, 1, 3),
    _SwAuthUserStatus_Type()
)
swAuthUserStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swAuthUserStatus.setStatus("current")
_SwAuthRadiusServer_ObjectIdentity = ObjectIdentity
swAuthRadiusServer = _SwAuthRadiusServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 23, 4)
)
_SwAuthRadiusServerTable_Object = MibTable
swAuthRadiusServerTable = _SwAuthRadiusServerTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 23, 4, 1)
)
if mibBuilder.loadTexts:
    swAuthRadiusServerTable.setStatus("current")
_SwAuthRadiusServerEntry_Object = MibTableRow
swAuthRadiusServerEntry = _SwAuthRadiusServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 23, 4, 1, 1)
)
swAuthRadiusServerEntry.setIndexNames(
    (0, "DES-1210-28ME_B2", "swAuthRadiusServerIndex"),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 23, 4, 1, 1, 1),
    _SwAuthRadiusServerIndex_Type()
)
swAuthRadiusServerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAuthRadiusServerIndex.setStatus("current")
_SwAuthRadiusServerAddress_Type = IpAddress
_SwAuthRadiusServerAddress_Object = MibTableColumn
swAuthRadiusServerAddress = _SwAuthRadiusServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 23, 4, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 23, 4, 1, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 23, 4, 1, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 23, 4, 1, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 23, 4, 1, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 23, 4, 1, 1, 7),
    _SwAuthRadiusServerKey_Type()
)
swAuthRadiusServerKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swAuthRadiusServerKey.setStatus("current")
_SwAuthRadiusServerStatus_Type = RowStatus
_SwAuthRadiusServerStatus_Object = MibTableColumn
swAuthRadiusServerStatus = _SwAuthRadiusServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 23, 4, 1, 1, 8),
    _SwAuthRadiusServerStatus_Type()
)
swAuthRadiusServerStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swAuthRadiusServerStatus.setStatus("current")
_CompanyGuestVlan_ObjectIdentity = ObjectIdentity
companyGuestVlan = _CompanyGuestVlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 24)
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 24, 1),
    _GuestVlanName_Type()
)
guestVlanName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    guestVlanName.setStatus("current")
_GuestVlanPort_Type = PortList
_GuestVlanPort_Object = MibScalar
guestVlanPort = _GuestVlanPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 24, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 24, 3),
    _GuestVlanDelState_Type()
)
guestVlanDelState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    guestVlanDelState.setStatus("current")
_CompanyMacNotify_ObjectIdentity = ObjectIdentity
companyMacNotify = _CompanyMacNotify_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 25)
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 25, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 25, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 25, 3),
    _MacNotifyHistorySize_Type()
)
macNotifyHistorySize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    macNotifyHistorySize.setStatus("current")
_MacNotifyCtrlTable_Object = MibTable
macNotifyCtrlTable = _MacNotifyCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 25, 4)
)
if mibBuilder.loadTexts:
    macNotifyCtrlTable.setStatus("current")
_MacNotifyCtrlEntry_Object = MibTableRow
macNotifyCtrlEntry = _MacNotifyCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 25, 4, 1)
)
macNotifyCtrlEntry.setIndexNames(
    (0, "DES-1210-28ME_B2", "macNotifyCtrlIndex"),
)
if mibBuilder.loadTexts:
    macNotifyCtrlEntry.setStatus("current")
_MacNotifyCtrlIndex_Type = Integer32
_MacNotifyCtrlIndex_Object = MibTableColumn
macNotifyCtrlIndex = _MacNotifyCtrlIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 25, 4, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 25, 4, 1, 2),
    _MacNotifyPortStatus_Type()
)
macNotifyPortStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    macNotifyPortStatus.setStatus("current")
_CompanyISMVLAN_ObjectIdentity = ObjectIdentity
companyISMVLAN = _CompanyISMVLAN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 27)
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 27, 1),
    _IgmpMulticastVlanStatus_Type()
)
igmpMulticastVlanStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpMulticastVlanStatus.setStatus("current")
_IgmpMulticastVlanTable_Object = MibTable
igmpMulticastVlanTable = _IgmpMulticastVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 27, 2)
)
if mibBuilder.loadTexts:
    igmpMulticastVlanTable.setStatus("current")
_IgmpMulticastVlanEntry_Object = MibTableRow
igmpMulticastVlanEntry = _IgmpMulticastVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 27, 2, 1)
)
igmpMulticastVlanEntry.setIndexNames(
    (0, "DES-1210-28ME_B2", "igmpMulticastVlanid"),
)
if mibBuilder.loadTexts:
    igmpMulticastVlanEntry.setStatus("current")


class _IgmpMulticastVlanid_Type(Integer32):
    """Custom type igmpMulticastVlanid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 4094),
    )


_IgmpMulticastVlanid_Type.__name__ = "Integer32"
_IgmpMulticastVlanid_Object = MibTableColumn
igmpMulticastVlanid = _IgmpMulticastVlanid_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 27, 2, 1, 1),
    _IgmpMulticastVlanid_Type()
)
igmpMulticastVlanid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpMulticastVlanid.setStatus("current")


class _IgmpMulticastVlanName_Type(DisplayString):
    """Custom type igmpMulticastVlanName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_IgmpMulticastVlanName_Type.__name__ = "DisplayString"
_IgmpMulticastVlanName_Object = MibTableColumn
igmpMulticastVlanName = _IgmpMulticastVlanName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 27, 2, 1, 2),
    _IgmpMulticastVlanName_Type()
)
igmpMulticastVlanName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    igmpMulticastVlanName.setStatus("current")
_IgmpMulticastVlanSourcePort_Type = PortList
_IgmpMulticastVlanSourcePort_Object = MibTableColumn
igmpMulticastVlanSourcePort = _IgmpMulticastVlanSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 27, 2, 1, 3),
    _IgmpMulticastVlanSourcePort_Type()
)
igmpMulticastVlanSourcePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpMulticastVlanSourcePort.setStatus("current")
_IgmpMulticastVlanMemberPort_Type = PortList
_IgmpMulticastVlanMemberPort_Object = MibTableColumn
igmpMulticastVlanMemberPort = _IgmpMulticastVlanMemberPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 27, 2, 1, 4),
    _IgmpMulticastVlanMemberPort_Type()
)
igmpMulticastVlanMemberPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpMulticastVlanMemberPort.setStatus("current")
_IgmpMulticastVlanTagMemberPort_Type = PortList
_IgmpMulticastVlanTagMemberPort_Object = MibTableColumn
igmpMulticastVlanTagMemberPort = _IgmpMulticastVlanTagMemberPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 27, 2, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 27, 2, 1, 6),
    _IgmpMulticastVlanState_Type()
)
igmpMulticastVlanState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpMulticastVlanState.setStatus("current")
_IgmpMulticastVlanReplaceSourceIp_Type = IpAddress
_IgmpMulticastVlanReplaceSourceIp_Object = MibTableColumn
igmpMulticastVlanReplaceSourceIp = _IgmpMulticastVlanReplaceSourceIp_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 27, 2, 1, 7),
    _IgmpMulticastVlanReplaceSourceIp_Type()
)
igmpMulticastVlanReplaceSourceIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpMulticastVlanReplaceSourceIp.setStatus("current")
_IgmpMulticastVlanRowStatus_Type = RowStatus
_IgmpMulticastVlanRowStatus_Object = MibTableColumn
igmpMulticastVlanRowStatus = _IgmpMulticastVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 27, 2, 1, 8),
    _IgmpMulticastVlanRowStatus_Type()
)
igmpMulticastVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    igmpMulticastVlanRowStatus.setStatus("current")
_IgmpMulticastVlanGroupTable_Object = MibTable
igmpMulticastVlanGroupTable = _IgmpMulticastVlanGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 27, 3)
)
if mibBuilder.loadTexts:
    igmpMulticastVlanGroupTable.setStatus("current")
_IgmpMulticastVlanGroupEntry_Object = MibTableRow
igmpMulticastVlanGroupEntry = _IgmpMulticastVlanGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 27, 3, 1)
)
igmpMulticastVlanGroupEntry.setIndexNames(
    (0, "DES-1210-28ME_B2", "igmpMulticastVlanGroupVid"),
    (0, "DES-1210-28ME_B2", "igmpMulticastVlanGroupFromIp"),
    (0, "DES-1210-28ME_B2", "igmpMulticastVlanGroupToIp"),
)
if mibBuilder.loadTexts:
    igmpMulticastVlanGroupEntry.setStatus("current")


class _IgmpMulticastVlanGroupVid_Type(Integer32):
    """Custom type igmpMulticastVlanGroupVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_IgmpMulticastVlanGroupVid_Type.__name__ = "Integer32"
_IgmpMulticastVlanGroupVid_Object = MibTableColumn
igmpMulticastVlanGroupVid = _IgmpMulticastVlanGroupVid_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 27, 3, 1, 1),
    _IgmpMulticastVlanGroupVid_Type()
)
igmpMulticastVlanGroupVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpMulticastVlanGroupVid.setStatus("current")
_IgmpMulticastVlanGroupFromIp_Type = IpAddress
_IgmpMulticastVlanGroupFromIp_Object = MibTableColumn
igmpMulticastVlanGroupFromIp = _IgmpMulticastVlanGroupFromIp_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 27, 3, 1, 2),
    _IgmpMulticastVlanGroupFromIp_Type()
)
igmpMulticastVlanGroupFromIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpMulticastVlanGroupFromIp.setStatus("current")
_IgmpMulticastVlanGroupToIp_Type = IpAddress
_IgmpMulticastVlanGroupToIp_Object = MibTableColumn
igmpMulticastVlanGroupToIp = _IgmpMulticastVlanGroupToIp_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 27, 3, 1, 3),
    _IgmpMulticastVlanGroupToIp_Type()
)
igmpMulticastVlanGroupToIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpMulticastVlanGroupToIp.setStatus("current")
_IgmpMulticastVlanGroupStatus_Type = RowStatus
_IgmpMulticastVlanGroupStatus_Object = MibTableColumn
igmpMulticastVlanGroupStatus = _IgmpMulticastVlanGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 27, 3, 1, 4),
    _IgmpMulticastVlanGroupStatus_Type()
)
igmpMulticastVlanGroupStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    igmpMulticastVlanGroupStatus.setStatus("current")
_CompanyDHCPRelay_ObjectIdentity = ObjectIdentity
companyDHCPRelay = _CompanyDHCPRelay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 28)
)
_DhcpBOOTPRelayControl_ObjectIdentity = ObjectIdentity
dhcpBOOTPRelayControl = _DhcpBOOTPRelayControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 28, 1)
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 28, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 28, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 28, 1, 3),
    _DhcpBOOTPRelayTimeThreshold_Type()
)
dhcpBOOTPRelayTimeThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpBOOTPRelayTimeThreshold.setStatus("current")
_DhcpBOOTPRelayManagement_ObjectIdentity = ObjectIdentity
dhcpBOOTPRelayManagement = _DhcpBOOTPRelayManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 28, 2)
)
_DhcpBOOTPRelayInterfaceSettingsTable_Object = MibTable
dhcpBOOTPRelayInterfaceSettingsTable = _DhcpBOOTPRelayInterfaceSettingsTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 28, 2, 1)
)
if mibBuilder.loadTexts:
    dhcpBOOTPRelayInterfaceSettingsTable.setStatus("current")
_DhcpBOOTPRelayInterfaceSettingsEntry_Object = MibTableRow
dhcpBOOTPRelayInterfaceSettingsEntry = _DhcpBOOTPRelayInterfaceSettingsEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 28, 2, 1, 1)
)
dhcpBOOTPRelayInterfaceSettingsEntry.setIndexNames(
    (0, "DES-1210-28ME_B2", "dhcpBOOTPRelayInterface"),
    (0, "DES-1210-28ME_B2", "dhcpBOOTPRelayServerIP"),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 28, 2, 1, 1, 1),
    _DhcpBOOTPRelayInterface_Type()
)
dhcpBOOTPRelayInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpBOOTPRelayInterface.setStatus("current")
_DhcpBOOTPRelayServerIP_Type = IpAddress
_DhcpBOOTPRelayServerIP_Object = MibTableColumn
dhcpBOOTPRelayServerIP = _DhcpBOOTPRelayServerIP_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 28, 2, 1, 1, 2),
    _DhcpBOOTPRelayServerIP_Type()
)
dhcpBOOTPRelayServerIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpBOOTPRelayServerIP.setStatus("current")
_DhcpBOOTPRelayInterfaceSettingsRowStatus_Type = RowStatus
_DhcpBOOTPRelayInterfaceSettingsRowStatus_Object = MibTableColumn
dhcpBOOTPRelayInterfaceSettingsRowStatus = _DhcpBOOTPRelayInterfaceSettingsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 28, 2, 1, 1, 3),
    _DhcpBOOTPRelayInterfaceSettingsRowStatus_Type()
)
dhcpBOOTPRelayInterfaceSettingsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpBOOTPRelayInterfaceSettingsRowStatus.setStatus("current")
_DhcpBOOTPRelayManagementOption82_ObjectIdentity = ObjectIdentity
dhcpBOOTPRelayManagementOption82 = _DhcpBOOTPRelayManagementOption82_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 28, 2, 2)
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 28, 2, 2, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 28, 2, 2, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 28, 2, 2, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 28, 2, 2, 4),
    _DhcpBOOTPRelayOption82RemoteIDType_Type()
)
dhcpBOOTPRelayOption82RemoteIDType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpBOOTPRelayOption82RemoteIDType.setStatus("current")
_DhcpBOOTPRelayOption82RemoteID_Type = DisplayString
_DhcpBOOTPRelayOption82RemoteID_Object = MibScalar
dhcpBOOTPRelayOption82RemoteID = _DhcpBOOTPRelayOption82RemoteID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 28, 2, 2, 5),
    _DhcpBOOTPRelayOption82RemoteID_Type()
)
dhcpBOOTPRelayOption82RemoteID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpBOOTPRelayOption82RemoteID.setStatus("current")
_CompanyDHCPLocalRelay_ObjectIdentity = ObjectIdentity
companyDHCPLocalRelay = _CompanyDHCPLocalRelay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 29)
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 29, 1),
    _DhcpLocalRelayGlobalState_Type()
)
dhcpLocalRelayGlobalState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpLocalRelayGlobalState.setStatus("current")
_DhcpLocalRelayTable_Object = MibTable
dhcpLocalRelayTable = _DhcpLocalRelayTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 29, 2)
)
if mibBuilder.loadTexts:
    dhcpLocalRelayTable.setStatus("current")
_DhcpLocalRelayTableEntry_Object = MibTableRow
dhcpLocalRelayTableEntry = _DhcpLocalRelayTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 29, 2, 1)
)
dhcpLocalRelayTableEntry.setIndexNames(
    (0, "DES-1210-28ME_B2", "dhcpLocalRelaySettingsVLANID"),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 29, 2, 1, 1),
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
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3))
    )


_DhcpLocalRelaySettingsState_Type.__name__ = "Integer32"
_DhcpLocalRelaySettingsState_Object = MibTableColumn
dhcpLocalRelaySettingsState = _DhcpLocalRelaySettingsState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 29, 2, 1, 2),
    _DhcpLocalRelaySettingsState_Type()
)
dhcpLocalRelaySettingsState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpLocalRelaySettingsState.setStatus("current")
_CompanyTrapSetting_ObjectIdentity = ObjectIdentity
companyTrapSetting = _CompanyTrapSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 30)
)
_SysTrapIP_Type = IpAddress
_SysTrapIP_Object = MibScalar
sysTrapIP = _SysTrapIP_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 30, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 30, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 30, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 30, 4),
    _SysTrapTwistedPortEvent_Type()
)
sysTrapTwistedPortEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysTrapTwistedPortEvent.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 30, 5),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 30, 6),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 30, 10),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 30, 13),
    _SysTrapPortSecurity_Type()
)
sysTrapPortSecurity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysTrapPortSecurity.setStatus("current")


class _SysTrapIMPBViolation_Type(Integer32):
    """Custom type sysTrapIMPBViolation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SysTrapIMPBViolation_Type.__name__ = "Integer32"
_SysTrapIMPBViolation_Object = MibScalar
sysTrapIMPBViolation = _SysTrapIMPBViolation_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 30, 14),
    _SysTrapIMPBViolation_Type()
)
sysTrapIMPBViolation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysTrapIMPBViolation.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 30, 15),
    _SysTrapLBD_Type()
)
sysTrapLBD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysTrapLBD.setStatus("current")


class _SysTrapDHCPServerScreening_Type(Integer32):
    """Custom type sysTrapDHCPServerScreening based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SysTrapDHCPServerScreening_Type.__name__ = "Integer32"
_SysTrapDHCPServerScreening_Object = MibScalar
sysTrapDHCPServerScreening = _SysTrapDHCPServerScreening_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 30, 16),
    _SysTrapDHCPServerScreening_Type()
)
sysTrapDHCPServerScreening.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysTrapDHCPServerScreening.setStatus("current")


class _SysTrapDuplicateIPDetected_Type(Integer32):
    """Custom type sysTrapDuplicateIPDetected based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SysTrapDuplicateIPDetected_Type.__name__ = "Integer32"
_SysTrapDuplicateIPDetected_Object = MibScalar
sysTrapDuplicateIPDetected = _SysTrapDuplicateIPDetected_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 30, 17),
    _SysTrapDuplicateIPDetected_Type()
)
sysTrapDuplicateIPDetected.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysTrapDuplicateIPDetected.setStatus("current")
_CompanyLLDPSetting_ObjectIdentity = ObjectIdentity
companyLLDPSetting = _CompanyLLDPSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 32)
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 32, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 32, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 32, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 32, 4),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 32, 5),
    _DlinklldpTxDelay_Type()
)
dlinklldpTxDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlinklldpTxDelay.setStatus("current")
_DlinklldpConfigManAddrPortsTxEnable_Type = PortList
_DlinklldpConfigManAddrPortsTxEnable_Object = MibScalar
dlinklldpConfigManAddrPortsTxEnable = _DlinklldpConfigManAddrPortsTxEnable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 32, 6),
    _DlinklldpConfigManAddrPortsTxEnable_Type()
)
dlinklldpConfigManAddrPortsTxEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlinklldpConfigManAddrPortsTxEnable.setStatus("current")
_LldpPortConfigTable_Object = MibTable
lldpPortConfigTable = _LldpPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 32, 11)
)
if mibBuilder.loadTexts:
    lldpPortConfigTable.setStatus("current")
_LldpPortConfigEntry_Object = MibTableRow
lldpPortConfigEntry = _LldpPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 32, 11, 1)
)
lldpPortConfigEntry.setIndexNames(
    (0, "DES-1210-28ME_B2", "lldpPortConfigPortNum"),
)
if mibBuilder.loadTexts:
    lldpPortConfigEntry.setStatus("current")
_LldpPortConfigPortNum_Type = LldpPortNumber
_LldpPortConfigPortNum_Object = MibTableColumn
lldpPortConfigPortNum = _LldpPortConfigPortNum_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 32, 11, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 32, 11, 1, 2),
    _LldpPortConfigAdminStatus_Type()
)
lldpPortConfigAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpPortConfigAdminStatus.setStatus("current")


class _LldpPortConfigNotificationEnable_Type(TruthValue):
    """Custom type lldpPortConfigNotificationEnable based on TruthValue"""


_LldpPortConfigNotificationEnable_Object = MibTableColumn
lldpPortConfigNotificationEnable = _LldpPortConfigNotificationEnable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 32, 11, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 32, 11, 1, 4),
    _LldpPortConfigTLVsTxEnable_Type()
)
lldpPortConfigTLVsTxEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpPortConfigTLVsTxEnable.setStatus("current")
_LldpXdot3Objects_ObjectIdentity = ObjectIdentity
lldpXdot3Objects = _LldpXdot3Objects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 32, 12)
)
_LldpXdot3Config_ObjectIdentity = ObjectIdentity
lldpXdot3Config = _LldpXdot3Config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 32, 12, 1)
)
_LldpXdot3PortConfigTable_Object = MibTable
lldpXdot3PortConfigTable = _LldpXdot3PortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 32, 12, 1, 1)
)
if mibBuilder.loadTexts:
    lldpXdot3PortConfigTable.setStatus("current")
_LldpXdot3PortConfigEntry_Object = MibTableRow
lldpXdot3PortConfigEntry = _LldpXdot3PortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 32, 12, 1, 1, 1)
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 32, 12, 1, 1, 1, 1),
    _LldpXdot3PortConfigTLVsTxEnable_Type()
)
lldpXdot3PortConfigTLVsTxEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpXdot3PortConfigTLVsTxEnable.setStatus("current")
_LldpXdot3LocalData_ObjectIdentity = ObjectIdentity
lldpXdot3LocalData = _LldpXdot3LocalData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 32, 12, 2)
)
_LldpXdot3LocPortTable_Object = MibTable
lldpXdot3LocPortTable = _LldpXdot3LocPortTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 32, 12, 2, 1)
)
if mibBuilder.loadTexts:
    lldpXdot3LocPortTable.setStatus("current")
_LldpXdot3LocPortEntry_Object = MibTableRow
lldpXdot3LocPortEntry = _LldpXdot3LocPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 32, 12, 2, 1, 1)
)
lldpXdot3LocPortEntry.setIndexNames(
    (0, "DES-1210-28ME_B2", "lldpXdot3LocPortAutoNegSupported"),
)
if mibBuilder.loadTexts:
    lldpXdot3LocPortEntry.setStatus("current")
_LldpXdot3LocPortAutoNegSupported_Type = TruthValue
_LldpXdot3LocPortAutoNegSupported_Object = MibTableColumn
lldpXdot3LocPortAutoNegSupported = _LldpXdot3LocPortAutoNegSupported_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 32, 12, 2, 1, 1, 1),
    _LldpXdot3LocPortAutoNegSupported_Type()
)
lldpXdot3LocPortAutoNegSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot3LocPortAutoNegSupported.setStatus("current")
_LldpXdot3LocPortAutoNegEnabled_Type = TruthValue
_LldpXdot3LocPortAutoNegEnabled_Object = MibTableColumn
lldpXdot3LocPortAutoNegEnabled = _LldpXdot3LocPortAutoNegEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 32, 12, 2, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 32, 12, 2, 1, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 32, 12, 2, 1, 1, 4),
    _LldpXdot3LocPortOperMauType_Type()
)
lldpXdot3LocPortOperMauType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot3LocPortOperMauType.setStatus("current")
_LldpXdot3LocPowerTable_Object = MibTable
lldpXdot3LocPowerTable = _LldpXdot3LocPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 32, 12, 2, 2)
)
if mibBuilder.loadTexts:
    lldpXdot3LocPowerTable.setStatus("current")
_LldpXdot3LocPowerEntry_Object = MibTableRow
lldpXdot3LocPowerEntry = _LldpXdot3LocPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 32, 12, 2, 2, 1)
)
lldpXdot3LocPowerEntry.setIndexNames(
    (0, "DES-1210-28ME_B2", "lldpXdot3LocPowerPortClass"),
)
if mibBuilder.loadTexts:
    lldpXdot3LocPowerEntry.setStatus("current")
_LldpXdot3LocPowerPortClass_Type = LldpPowerPortClass
_LldpXdot3LocPowerPortClass_Object = MibTableColumn
lldpXdot3LocPowerPortClass = _LldpXdot3LocPowerPortClass_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 32, 12, 2, 2, 1, 1),
    _LldpXdot3LocPowerPortClass_Type()
)
lldpXdot3LocPowerPortClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot3LocPowerPortClass.setStatus("current")
_LldpXdot3LocPowerMDISupported_Type = TruthValue
_LldpXdot3LocPowerMDISupported_Object = MibTableColumn
lldpXdot3LocPowerMDISupported = _LldpXdot3LocPowerMDISupported_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 32, 12, 2, 2, 1, 2),
    _LldpXdot3LocPowerMDISupported_Type()
)
lldpXdot3LocPowerMDISupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot3LocPowerMDISupported.setStatus("current")
_LldpXdot3LocPowerMDIEnabled_Type = TruthValue
_LldpXdot3LocPowerMDIEnabled_Object = MibTableColumn
lldpXdot3LocPowerMDIEnabled = _LldpXdot3LocPowerMDIEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 32, 12, 2, 2, 1, 3),
    _LldpXdot3LocPowerMDIEnabled_Type()
)
lldpXdot3LocPowerMDIEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot3LocPowerMDIEnabled.setStatus("current")
_LldpXdot3LocPowerPairControlable_Type = TruthValue
_LldpXdot3LocPowerPairControlable_Object = MibTableColumn
lldpXdot3LocPowerPairControlable = _LldpXdot3LocPowerPairControlable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 32, 12, 2, 2, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 32, 12, 2, 2, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 32, 12, 2, 2, 1, 6),
    _LldpXdot3LocPowerClass_Type()
)
lldpXdot3LocPowerClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot3LocPowerClass.setStatus("current")
_LldpXdot3LocLinkAggTable_Object = MibTable
lldpXdot3LocLinkAggTable = _LldpXdot3LocLinkAggTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 32, 12, 2, 3)
)
if mibBuilder.loadTexts:
    lldpXdot3LocLinkAggTable.setStatus("current")
_LldpXdot3LocLinkAggEntry_Object = MibTableRow
lldpXdot3LocLinkAggEntry = _LldpXdot3LocLinkAggEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 32, 12, 2, 3, 1)
)
lldpXdot3LocLinkAggEntry.setIndexNames(
    (0, "DES-1210-28ME_B2", "lldpXdot3LocLinkAggStatus"),
)
if mibBuilder.loadTexts:
    lldpXdot3LocLinkAggEntry.setStatus("current")
_LldpXdot3LocLinkAggStatus_Type = LldpLinkAggStatusMap
_LldpXdot3LocLinkAggStatus_Object = MibTableColumn
lldpXdot3LocLinkAggStatus = _LldpXdot3LocLinkAggStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 32, 12, 2, 3, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 32, 12, 2, 3, 1, 2),
    _LldpXdot3LocLinkAggPortId_Type()
)
lldpXdot3LocLinkAggPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot3LocLinkAggPortId.setStatus("current")
_LldpXdot3LocMaxFrameSizeTable_Object = MibTable
lldpXdot3LocMaxFrameSizeTable = _LldpXdot3LocMaxFrameSizeTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 32, 12, 2, 4)
)
if mibBuilder.loadTexts:
    lldpXdot3LocMaxFrameSizeTable.setStatus("current")
_LldpXdot3LocMaxFrameSizeEntry_Object = MibTableRow
lldpXdot3LocMaxFrameSizeEntry = _LldpXdot3LocMaxFrameSizeEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 32, 12, 2, 4, 1)
)
lldpXdot3LocMaxFrameSizeEntry.setIndexNames(
    (0, "DES-1210-28ME_B2", "lldpXdot3LocMaxFrameSize"),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 32, 12, 2, 4, 1, 1),
    _LldpXdot3LocMaxFrameSize_Type()
)
lldpXdot3LocMaxFrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot3LocMaxFrameSize.setStatus("current")
_LldpXdot3RemoteData_ObjectIdentity = ObjectIdentity
lldpXdot3RemoteData = _LldpXdot3RemoteData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 32, 12, 3)
)
_LldpXdot3RemPortTable_Object = MibTable
lldpXdot3RemPortTable = _LldpXdot3RemPortTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 32, 12, 3, 1)
)
if mibBuilder.loadTexts:
    lldpXdot3RemPortTable.setStatus("current")
_LldpXdot3RemPortEntry_Object = MibTableRow
lldpXdot3RemPortEntry = _LldpXdot3RemPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 32, 12, 3, 1, 1)
)
lldpXdot3RemPortEntry.setIndexNames(
    (0, "DES-1210-28ME_B2", "lldpXdot3RemPortAutoNegSupported"),
)
if mibBuilder.loadTexts:
    lldpXdot3RemPortEntry.setStatus("current")
_LldpXdot3RemPortAutoNegSupported_Type = TruthValue
_LldpXdot3RemPortAutoNegSupported_Object = MibTableColumn
lldpXdot3RemPortAutoNegSupported = _LldpXdot3RemPortAutoNegSupported_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 32, 12, 3, 1, 1, 1),
    _LldpXdot3RemPortAutoNegSupported_Type()
)
lldpXdot3RemPortAutoNegSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot3RemPortAutoNegSupported.setStatus("current")
_LldpXdot3RemPortAutoNegEnabled_Type = TruthValue
_LldpXdot3RemPortAutoNegEnabled_Object = MibTableColumn
lldpXdot3RemPortAutoNegEnabled = _LldpXdot3RemPortAutoNegEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 32, 12, 3, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 32, 12, 3, 1, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 32, 12, 3, 1, 1, 4),
    _LldpXdot3RemPortOperMauType_Type()
)
lldpXdot3RemPortOperMauType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot3RemPortOperMauType.setStatus("current")
_LldpXdot3RemPowerTable_Object = MibTable
lldpXdot3RemPowerTable = _LldpXdot3RemPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 32, 12, 3, 2)
)
if mibBuilder.loadTexts:
    lldpXdot3RemPowerTable.setStatus("current")
_LldpXdot3RemPowerEntry_Object = MibTableRow
lldpXdot3RemPowerEntry = _LldpXdot3RemPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 32, 12, 3, 2, 1)
)
lldpXdot3RemPowerEntry.setIndexNames(
    (0, "DES-1210-28ME_B2", "lldpXdot3RemPowerPortClass"),
)
if mibBuilder.loadTexts:
    lldpXdot3RemPowerEntry.setStatus("current")
_LldpXdot3RemPowerPortClass_Type = LldpPowerPortClass
_LldpXdot3RemPowerPortClass_Object = MibTableColumn
lldpXdot3RemPowerPortClass = _LldpXdot3RemPowerPortClass_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 32, 12, 3, 2, 1, 1),
    _LldpXdot3RemPowerPortClass_Type()
)
lldpXdot3RemPowerPortClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot3RemPowerPortClass.setStatus("current")
_LldpXdot3RemPowerMDISupported_Type = TruthValue
_LldpXdot3RemPowerMDISupported_Object = MibTableColumn
lldpXdot3RemPowerMDISupported = _LldpXdot3RemPowerMDISupported_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 32, 12, 3, 2, 1, 2),
    _LldpXdot3RemPowerMDISupported_Type()
)
lldpXdot3RemPowerMDISupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot3RemPowerMDISupported.setStatus("current")
_LldpXdot3RemPowerMDIEnabled_Type = TruthValue
_LldpXdot3RemPowerMDIEnabled_Object = MibTableColumn
lldpXdot3RemPowerMDIEnabled = _LldpXdot3RemPowerMDIEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 32, 12, 3, 2, 1, 3),
    _LldpXdot3RemPowerMDIEnabled_Type()
)
lldpXdot3RemPowerMDIEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot3RemPowerMDIEnabled.setStatus("current")
_LldpXdot3RemPowerPairControlable_Type = TruthValue
_LldpXdot3RemPowerPairControlable_Object = MibTableColumn
lldpXdot3RemPowerPairControlable = _LldpXdot3RemPowerPairControlable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 32, 12, 3, 2, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 32, 12, 3, 2, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 32, 12, 3, 2, 1, 6),
    _LldpXdot3RemPowerClass_Type()
)
lldpXdot3RemPowerClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot3RemPowerClass.setStatus("current")
_LldpXdot3RemLinkAggTable_Object = MibTable
lldpXdot3RemLinkAggTable = _LldpXdot3RemLinkAggTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 32, 12, 3, 3)
)
if mibBuilder.loadTexts:
    lldpXdot3RemLinkAggTable.setStatus("current")
_LldpXdot3RemLinkAggEntry_Object = MibTableRow
lldpXdot3RemLinkAggEntry = _LldpXdot3RemLinkAggEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 32, 12, 3, 3, 1)
)
lldpXdot3RemLinkAggEntry.setIndexNames(
    (0, "DES-1210-28ME_B2", "lldpXdot3RemLinkAggStatus"),
)
if mibBuilder.loadTexts:
    lldpXdot3RemLinkAggEntry.setStatus("current")
_LldpXdot3RemLinkAggStatus_Type = LldpLinkAggStatusMap
_LldpXdot3RemLinkAggStatus_Object = MibTableColumn
lldpXdot3RemLinkAggStatus = _LldpXdot3RemLinkAggStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 32, 12, 3, 3, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 32, 12, 3, 3, 1, 2),
    _LldpXdot3RemLinkAggPortId_Type()
)
lldpXdot3RemLinkAggPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot3RemLinkAggPortId.setStatus("current")
_LldpXdot3RemMaxFrameSizeTable_Object = MibTable
lldpXdot3RemMaxFrameSizeTable = _LldpXdot3RemMaxFrameSizeTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 32, 12, 3, 4)
)
if mibBuilder.loadTexts:
    lldpXdot3RemMaxFrameSizeTable.setStatus("current")
_LldpXdot3RemMaxFrameSizeEntry_Object = MibTableRow
lldpXdot3RemMaxFrameSizeEntry = _LldpXdot3RemMaxFrameSizeEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 32, 12, 3, 4, 1)
)
lldpXdot3RemMaxFrameSizeEntry.setIndexNames(
    (0, "DES-1210-28ME_B2", "lldpXdot3RemMaxFrameSize"),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 32, 12, 3, 4, 1, 1),
    _LldpXdot3RemMaxFrameSize_Type()
)
lldpXdot3RemMaxFrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot3RemMaxFrameSize.setStatus("current")
_LldpXdot1Objects_ObjectIdentity = ObjectIdentity
lldpXdot1Objects = _LldpXdot1Objects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 32, 13)
)
_LldpXdot1Config_ObjectIdentity = ObjectIdentity
lldpXdot1Config = _LldpXdot1Config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 32, 13, 1)
)
_LldpXdot1ConfigPortVlanTable_Object = MibTable
lldpXdot1ConfigPortVlanTable = _LldpXdot1ConfigPortVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 32, 13, 1, 1)
)
if mibBuilder.loadTexts:
    lldpXdot1ConfigPortVlanTable.setStatus("current")
_LldpXdot1ConfigPortVlanEntry_Object = MibTableRow
lldpXdot1ConfigPortVlanEntry = _LldpXdot1ConfigPortVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 32, 13, 1, 1, 1)
)
if mibBuilder.loadTexts:
    lldpXdot1ConfigPortVlanEntry.setStatus("current")


class _LldpXdot1ConfigPortVlanTxEnable_Type(TruthValue):
    """Custom type lldpXdot1ConfigPortVlanTxEnable based on TruthValue"""


_LldpXdot1ConfigPortVlanTxEnable_Object = MibTableColumn
lldpXdot1ConfigPortVlanTxEnable = _LldpXdot1ConfigPortVlanTxEnable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 32, 13, 1, 1, 1, 1),
    _LldpXdot1ConfigPortVlanTxEnable_Type()
)
lldpXdot1ConfigPortVlanTxEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpXdot1ConfigPortVlanTxEnable.setStatus("current")
_LldpXdot1ConfigVlanNameTable_Object = MibTable
lldpXdot1ConfigVlanNameTable = _LldpXdot1ConfigVlanNameTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 32, 13, 1, 2)
)
if mibBuilder.loadTexts:
    lldpXdot1ConfigVlanNameTable.setStatus("current")
_LldpXdot1ConfigVlanNameEntry_Object = MibTableRow
lldpXdot1ConfigVlanNameEntry = _LldpXdot1ConfigVlanNameEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 32, 13, 1, 2, 1)
)
if mibBuilder.loadTexts:
    lldpXdot1ConfigVlanNameEntry.setStatus("current")


class _LldpXdot1ConfigVlanNameTxEnable_Type(TruthValue):
    """Custom type lldpXdot1ConfigVlanNameTxEnable based on TruthValue"""


_LldpXdot1ConfigVlanNameTxEnable_Object = MibTableColumn
lldpXdot1ConfigVlanNameTxEnable = _LldpXdot1ConfigVlanNameTxEnable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 32, 13, 1, 2, 1, 1),
    _LldpXdot1ConfigVlanNameTxEnable_Type()
)
lldpXdot1ConfigVlanNameTxEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpXdot1ConfigVlanNameTxEnable.setStatus("current")
_LldpXdot1ConfigProtoVlanTable_Object = MibTable
lldpXdot1ConfigProtoVlanTable = _LldpXdot1ConfigProtoVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 32, 13, 1, 3)
)
if mibBuilder.loadTexts:
    lldpXdot1ConfigProtoVlanTable.setStatus("current")
_LldpXdot1ConfigProtoVlanEntry_Object = MibTableRow
lldpXdot1ConfigProtoVlanEntry = _LldpXdot1ConfigProtoVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 32, 13, 1, 3, 1)
)
if mibBuilder.loadTexts:
    lldpXdot1ConfigProtoVlanEntry.setStatus("current")


class _LldpXdot1ConfigProtoVlanTxEnable_Type(TruthValue):
    """Custom type lldpXdot1ConfigProtoVlanTxEnable based on TruthValue"""


_LldpXdot1ConfigProtoVlanTxEnable_Object = MibTableColumn
lldpXdot1ConfigProtoVlanTxEnable = _LldpXdot1ConfigProtoVlanTxEnable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 32, 13, 1, 3, 1, 1),
    _LldpXdot1ConfigProtoVlanTxEnable_Type()
)
lldpXdot1ConfigProtoVlanTxEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpXdot1ConfigProtoVlanTxEnable.setStatus("current")
_LldpXdot1ConfigProtocolTable_Object = MibTable
lldpXdot1ConfigProtocolTable = _LldpXdot1ConfigProtocolTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 32, 13, 1, 4)
)
if mibBuilder.loadTexts:
    lldpXdot1ConfigProtocolTable.setStatus("current")
_LldpXdot1ConfigProtocolEntry_Object = MibTableRow
lldpXdot1ConfigProtocolEntry = _LldpXdot1ConfigProtocolEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 32, 13, 1, 4, 1)
)
if mibBuilder.loadTexts:
    lldpXdot1ConfigProtocolEntry.setStatus("current")


class _LldpXdot1ConfigProtocolTxEnable_Type(TruthValue):
    """Custom type lldpXdot1ConfigProtocolTxEnable based on TruthValue"""


_LldpXdot1ConfigProtocolTxEnable_Object = MibTableColumn
lldpXdot1ConfigProtocolTxEnable = _LldpXdot1ConfigProtocolTxEnable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 32, 13, 1, 4, 1, 1),
    _LldpXdot1ConfigProtocolTxEnable_Type()
)
lldpXdot1ConfigProtocolTxEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpXdot1ConfigProtocolTxEnable.setStatus("current")
_LldpXdot1LocalData_ObjectIdentity = ObjectIdentity
lldpXdot1LocalData = _LldpXdot1LocalData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 32, 13, 2)
)
_LldpXdot1LocTable_Object = MibTable
lldpXdot1LocTable = _LldpXdot1LocTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 32, 13, 2, 1)
)
if mibBuilder.loadTexts:
    lldpXdot1LocTable.setStatus("current")
_LldpXdot1LocEntry_Object = MibTableRow
lldpXdot1LocEntry = _LldpXdot1LocEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 32, 13, 2, 1, 1)
)
lldpXdot1LocEntry.setIndexNames(
    (0, "DES-1210-28ME_B2", "lldpXdot1LocPortVlanId"),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 32, 13, 2, 1, 1, 1),
    _LldpXdot1LocPortVlanId_Type()
)
lldpXdot1LocPortVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1LocPortVlanId.setStatus("current")
_LldpXdot1LocProtoVlanTable_Object = MibTable
lldpXdot1LocProtoVlanTable = _LldpXdot1LocProtoVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 32, 13, 2, 2)
)
if mibBuilder.loadTexts:
    lldpXdot1LocProtoVlanTable.setStatus("current")
_LldpXdot1LocProtoVlanEntry_Object = MibTableRow
lldpXdot1LocProtoVlanEntry = _LldpXdot1LocProtoVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 32, 13, 2, 2, 1)
)
lldpXdot1LocProtoVlanEntry.setIndexNames(
    (0, "DES-1210-28ME_B2", "lldpXdot1LocProtoVlanId"),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 32, 13, 2, 2, 1, 1),
    _LldpXdot1LocProtoVlanId_Type()
)
lldpXdot1LocProtoVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lldpXdot1LocProtoVlanId.setStatus("current")
_LldpXdot1LocProtoVlanSupported_Type = TruthValue
_LldpXdot1LocProtoVlanSupported_Object = MibTableColumn
lldpXdot1LocProtoVlanSupported = _LldpXdot1LocProtoVlanSupported_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 32, 13, 2, 2, 1, 2),
    _LldpXdot1LocProtoVlanSupported_Type()
)
lldpXdot1LocProtoVlanSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1LocProtoVlanSupported.setStatus("current")
_LldpXdot1LocProtoVlanEnabled_Type = TruthValue
_LldpXdot1LocProtoVlanEnabled_Object = MibTableColumn
lldpXdot1LocProtoVlanEnabled = _LldpXdot1LocProtoVlanEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 32, 13, 2, 2, 1, 3),
    _LldpXdot1LocProtoVlanEnabled_Type()
)
lldpXdot1LocProtoVlanEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1LocProtoVlanEnabled.setStatus("current")
_LldpXdot1LocVlanNameTable_Object = MibTable
lldpXdot1LocVlanNameTable = _LldpXdot1LocVlanNameTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 32, 13, 2, 3)
)
if mibBuilder.loadTexts:
    lldpXdot1LocVlanNameTable.setStatus("current")
_LldpXdot1LocVlanNameEntry_Object = MibTableRow
lldpXdot1LocVlanNameEntry = _LldpXdot1LocVlanNameEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 32, 13, 2, 3, 1)
)
lldpXdot1LocVlanNameEntry.setIndexNames(
    (0, "DES-1210-28ME_B2", "lldpXdot1LocVlanId"),
)
if mibBuilder.loadTexts:
    lldpXdot1LocVlanNameEntry.setStatus("current")
_LldpXdot1LocVlanId_Type = VlanId
_LldpXdot1LocVlanId_Object = MibTableColumn
lldpXdot1LocVlanId = _LldpXdot1LocVlanId_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 32, 13, 2, 3, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 32, 13, 2, 3, 1, 2),
    _LldpXdot1LocVlanName_Type()
)
lldpXdot1LocVlanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1LocVlanName.setStatus("current")
_LldpXdot1LocProtocolTable_Object = MibTable
lldpXdot1LocProtocolTable = _LldpXdot1LocProtocolTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 32, 13, 2, 4)
)
if mibBuilder.loadTexts:
    lldpXdot1LocProtocolTable.setStatus("current")
_LldpXdot1LocProtocolEntry_Object = MibTableRow
lldpXdot1LocProtocolEntry = _LldpXdot1LocProtocolEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 32, 13, 2, 4, 1)
)
lldpXdot1LocProtocolEntry.setIndexNames(
    (0, "DES-1210-28ME_B2", "lldpXdot1LocProtocolIndex"),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 32, 13, 2, 4, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 32, 13, 2, 4, 1, 2),
    _LldpXdot1LocProtocolId_Type()
)
lldpXdot1LocProtocolId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1LocProtocolId.setStatus("current")
_LldpXdot1RemoteData_ObjectIdentity = ObjectIdentity
lldpXdot1RemoteData = _LldpXdot1RemoteData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 32, 13, 3)
)
_LldpXdot1RemTable_Object = MibTable
lldpXdot1RemTable = _LldpXdot1RemTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 32, 13, 3, 1)
)
if mibBuilder.loadTexts:
    lldpXdot1RemTable.setStatus("current")
_LldpXdot1RemEntry_Object = MibTableRow
lldpXdot1RemEntry = _LldpXdot1RemEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 32, 13, 3, 1, 1)
)
lldpXdot1RemEntry.setIndexNames(
    (0, "DES-1210-28ME_B2", "lldpXdot1RemPortVlanId"),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 32, 13, 3, 1, 1, 1),
    _LldpXdot1RemPortVlanId_Type()
)
lldpXdot1RemPortVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1RemPortVlanId.setStatus("current")
_LldpXdot1RemProtoVlanTable_Object = MibTable
lldpXdot1RemProtoVlanTable = _LldpXdot1RemProtoVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 32, 13, 3, 2)
)
if mibBuilder.loadTexts:
    lldpXdot1RemProtoVlanTable.setStatus("current")
_LldpXdot1RemProtoVlanEntry_Object = MibTableRow
lldpXdot1RemProtoVlanEntry = _LldpXdot1RemProtoVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 32, 13, 3, 2, 1)
)
lldpXdot1RemProtoVlanEntry.setIndexNames(
    (0, "DES-1210-28ME_B2", "lldpXdot1RemProtoVlanId"),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 32, 13, 3, 2, 1, 1),
    _LldpXdot1RemProtoVlanId_Type()
)
lldpXdot1RemProtoVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lldpXdot1RemProtoVlanId.setStatus("current")
_LldpXdot1RemProtoVlanSupported_Type = TruthValue
_LldpXdot1RemProtoVlanSupported_Object = MibTableColumn
lldpXdot1RemProtoVlanSupported = _LldpXdot1RemProtoVlanSupported_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 32, 13, 3, 2, 1, 2),
    _LldpXdot1RemProtoVlanSupported_Type()
)
lldpXdot1RemProtoVlanSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1RemProtoVlanSupported.setStatus("current")
_LldpXdot1RemProtoVlanEnabled_Type = TruthValue
_LldpXdot1RemProtoVlanEnabled_Object = MibTableColumn
lldpXdot1RemProtoVlanEnabled = _LldpXdot1RemProtoVlanEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 32, 13, 3, 2, 1, 3),
    _LldpXdot1RemProtoVlanEnabled_Type()
)
lldpXdot1RemProtoVlanEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1RemProtoVlanEnabled.setStatus("current")
_LldpXdot1RemVlanNameTable_Object = MibTable
lldpXdot1RemVlanNameTable = _LldpXdot1RemVlanNameTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 32, 13, 3, 3)
)
if mibBuilder.loadTexts:
    lldpXdot1RemVlanNameTable.setStatus("current")
_LldpXdot1RemVlanNameEntry_Object = MibTableRow
lldpXdot1RemVlanNameEntry = _LldpXdot1RemVlanNameEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 32, 13, 3, 3, 1)
)
lldpXdot1RemVlanNameEntry.setIndexNames(
    (0, "DES-1210-28ME_B2", "lldpXdot1RemVlanId"),
)
if mibBuilder.loadTexts:
    lldpXdot1RemVlanNameEntry.setStatus("current")
_LldpXdot1RemVlanId_Type = VlanId
_LldpXdot1RemVlanId_Object = MibTableColumn
lldpXdot1RemVlanId = _LldpXdot1RemVlanId_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 32, 13, 3, 3, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 32, 13, 3, 3, 1, 2),
    _LldpXdot1RemVlanName_Type()
)
lldpXdot1RemVlanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1RemVlanName.setStatus("current")
_LldpXdot1RemProtocolTable_Object = MibTable
lldpXdot1RemProtocolTable = _LldpXdot1RemProtocolTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 32, 13, 3, 4)
)
if mibBuilder.loadTexts:
    lldpXdot1RemProtocolTable.setStatus("current")
_LldpXdot1RemProtocolEntry_Object = MibTableRow
lldpXdot1RemProtocolEntry = _LldpXdot1RemProtocolEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 32, 13, 3, 4, 1)
)
lldpXdot1RemProtocolEntry.setIndexNames(
    (0, "DES-1210-28ME_B2", "lldpXdot1RemProtocolIndex"),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 32, 13, 3, 4, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 32, 13, 3, 4, 1, 2),
    _LldpXdot1RemProtocolId_Type()
)
lldpXdot1RemProtocolId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1RemProtocolId.setStatus("current")
_CompanyCPUInterfaceFilterGroup_ObjectIdentity = ObjectIdentity
companyCPUInterfaceFilterGroup = _CompanyCPUInterfaceFilterGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 33)
)
_CpuFilterProfile_ObjectIdentity = ObjectIdentity
cpuFilterProfile = _CpuFilterProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 33, 1)
)
_CpuFilterProfileTable_Object = MibTable
cpuFilterProfileTable = _CpuFilterProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 33, 1, 1)
)
if mibBuilder.loadTexts:
    cpuFilterProfileTable.setStatus("current")
_CpuFilterProfileEntry_Object = MibTableRow
cpuFilterProfileEntry = _CpuFilterProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 33, 1, 1, 1)
)
cpuFilterProfileEntry.setIndexNames(
    (0, "DES-1210-28ME_B2", "cpuFilterProfileNo"),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 33, 1, 1, 1, 1),
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
              2)
        )
    )
    namedValues = NamedValues(
        *(("l2", 1),
          ("l3", 2))
    )


_CpuFilterProfileType_Type.__name__ = "Integer32"
_CpuFilterProfileType_Object = MibTableColumn
cpuFilterProfileType = _CpuFilterProfileType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 33, 1, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 33, 1, 1, 1, 3),
    _CpuFilterProfileRuleCount_Type()
)
cpuFilterProfileRuleCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuFilterProfileRuleCount.setStatus("current")
_CpuFilterProfileMask_Type = OctetString
_CpuFilterProfileMask_Object = MibTableColumn
cpuFilterProfileMask = _CpuFilterProfileMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 33, 1, 1, 1, 4),
    _CpuFilterProfileMask_Type()
)
cpuFilterProfileMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpuFilterProfileMask.setStatus("current")
_CpuFilterProfileDstMacAddrMask_Type = MacAddress
_CpuFilterProfileDstMacAddrMask_Object = MibTableColumn
cpuFilterProfileDstMacAddrMask = _CpuFilterProfileDstMacAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 33, 1, 1, 1, 5),
    _CpuFilterProfileDstMacAddrMask_Type()
)
cpuFilterProfileDstMacAddrMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpuFilterProfileDstMacAddrMask.setStatus("current")
_CpuFilterProfileSrcMacAddrMask_Type = MacAddress
_CpuFilterProfileSrcMacAddrMask_Object = MibTableColumn
cpuFilterProfileSrcMacAddrMask = _CpuFilterProfileSrcMacAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 33, 1, 1, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 33, 1, 1, 1, 7),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 33, 1, 1, 1, 8),
    _CpuFilterProfileIPProtocolMask_Type()
)
cpuFilterProfileIPProtocolMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpuFilterProfileIPProtocolMask.setStatus("current")


class _CpuFilterProfileDstIpAddrMask_Type(IpAddress):
    """Custom type cpuFilterProfileDstIpAddrMask based on IpAddress"""
    defaultHexValue = "FFFFFFFF"


_CpuFilterProfileDstIpAddrMask_Object = MibTableColumn
cpuFilterProfileDstIpAddrMask = _CpuFilterProfileDstIpAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 33, 1, 1, 1, 9),
    _CpuFilterProfileDstIpAddrMask_Type()
)
cpuFilterProfileDstIpAddrMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpuFilterProfileDstIpAddrMask.setStatus("current")


class _CpuFilterProfileSrcIpAddrMask_Type(IpAddress):
    """Custom type cpuFilterProfileSrcIpAddrMask based on IpAddress"""
    defaultHexValue = "FFFFFFFF"


_CpuFilterProfileSrcIpAddrMask_Object = MibTableColumn
cpuFilterProfileSrcIpAddrMask = _CpuFilterProfileSrcIpAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 33, 1, 1, 1, 10),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 33, 1, 1, 1, 11),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 33, 1, 1, 1, 12),
    _CpuFilterProfileSrcPortMask_Type()
)
cpuFilterProfileSrcPortMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpuFilterProfileSrcPortMask.setStatus("current")
_CpuFilterProfileStatus_Type = RowStatus
_CpuFilterProfileStatus_Object = MibTableColumn
cpuFilterProfileStatus = _CpuFilterProfileStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 33, 1, 1, 1, 15),
    _CpuFilterProfileStatus_Type()
)
cpuFilterProfileStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpuFilterProfileStatus.setStatus("current")
_CpuFilterL2Rule_ObjectIdentity = ObjectIdentity
cpuFilterL2Rule = _CpuFilterL2Rule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 33, 2)
)
_CpuFilterL2RuleTable_Object = MibTable
cpuFilterL2RuleTable = _CpuFilterL2RuleTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 33, 2, 1)
)
if mibBuilder.loadTexts:
    cpuFilterL2RuleTable.setStatus("current")
_CpuFilterL2RuleEntry_Object = MibTableRow
cpuFilterL2RuleEntry = _CpuFilterL2RuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 33, 2, 1, 1)
)
cpuFilterL2RuleEntry.setIndexNames(
    (0, "DES-1210-28ME_B2", "cpuFilterL2ProfileID"),
    (0, "DES-1210-28ME_B2", "cpuFilterL2AccessID"),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 33, 2, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 33, 2, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 33, 2, 1, 1, 3),
    _CpuFilterL2RuleEtherType_Type()
)
cpuFilterL2RuleEtherType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpuFilterL2RuleEtherType.setStatus("current")
_CpuFilterL2RuleDstMacAddr_Type = MacAddress
_CpuFilterL2RuleDstMacAddr_Object = MibTableColumn
cpuFilterL2RuleDstMacAddr = _CpuFilterL2RuleDstMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 33, 2, 1, 1, 4),
    _CpuFilterL2RuleDstMacAddr_Type()
)
cpuFilterL2RuleDstMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpuFilterL2RuleDstMacAddr.setStatus("current")
_CpuFilterL2RuleSrcMacAddr_Type = MacAddress
_CpuFilterL2RuleSrcMacAddr_Object = MibTableColumn
cpuFilterL2RuleSrcMacAddr = _CpuFilterL2RuleSrcMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 33, 2, 1, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 33, 2, 1, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 33, 2, 1, 1, 7),
    _CpuFilterL2Rule1pPriority_Type()
)
cpuFilterL2Rule1pPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpuFilterL2Rule1pPriority.setStatus("current")
_CpuFilterL2RuleDstMacAddrMask_Type = MacAddress
_CpuFilterL2RuleDstMacAddrMask_Object = MibTableColumn
cpuFilterL2RuleDstMacAddrMask = _CpuFilterL2RuleDstMacAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 33, 2, 1, 1, 8),
    _CpuFilterL2RuleDstMacAddrMask_Type()
)
cpuFilterL2RuleDstMacAddrMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuFilterL2RuleDstMacAddrMask.setStatus("current")
_CpuFilterL2RuleSrcMacAddrMask_Type = MacAddress
_CpuFilterL2RuleSrcMacAddrMask_Object = MibTableColumn
cpuFilterL2RuleSrcMacAddrMask = _CpuFilterL2RuleSrcMacAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 33, 2, 1, 1, 9),
    _CpuFilterL2RuleSrcMacAddrMask_Type()
)
cpuFilterL2RuleSrcMacAddrMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuFilterL2RuleSrcMacAddrMask.setStatus("current")
_CpuFilterL2RuleInPortList_Type = PortList
_CpuFilterL2RuleInPortList_Object = MibTableColumn
cpuFilterL2RuleInPortList = _CpuFilterL2RuleInPortList_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 33, 2, 1, 1, 10),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 33, 2, 1, 1, 11),
    _CpuFilterL2RuleAction_Type()
)
cpuFilterL2RuleAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpuFilterL2RuleAction.setStatus("current")
_CpuFilterL2RuleStatus_Type = RowStatus
_CpuFilterL2RuleStatus_Object = MibTableColumn
cpuFilterL2RuleStatus = _CpuFilterL2RuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 33, 2, 1, 1, 14),
    _CpuFilterL2RuleStatus_Type()
)
cpuFilterL2RuleStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpuFilterL2RuleStatus.setStatus("current")
_CpuFilterL3Rule_ObjectIdentity = ObjectIdentity
cpuFilterL3Rule = _CpuFilterL3Rule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 33, 3)
)
_CpuFilterL3RuleTable_Object = MibTable
cpuFilterL3RuleTable = _CpuFilterL3RuleTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 33, 3, 1)
)
if mibBuilder.loadTexts:
    cpuFilterL3RuleTable.setStatus("current")
_CpuFilterL3RuleEntry_Object = MibTableRow
cpuFilterL3RuleEntry = _CpuFilterL3RuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 33, 3, 1, 1)
)
cpuFilterL3RuleEntry.setIndexNames(
    (0, "DES-1210-28ME_B2", "cpuFilterL3RuleProfileNo"),
    (0, "DES-1210-28ME_B2", "cpuFilterL3RuleAccessID"),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 33, 3, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 33, 3, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 33, 3, 1, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 33, 3, 1, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 33, 3, 1, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 33, 3, 1, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 33, 3, 1, 1, 7),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 33, 3, 1, 1, 8),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 33, 3, 1, 1, 9),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 33, 3, 1, 1, 10),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 33, 3, 1, 1, 11),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 33, 3, 1, 1, 12),
    _CpuFilterL3RuleTcpUdpSrcPort_Type()
)
cpuFilterL3RuleTcpUdpSrcPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpuFilterL3RuleTcpUdpSrcPort.setStatus("current")
_CpuFilterL3RuleTcpUdpDstPortMask_Type = OctetString
_CpuFilterL3RuleTcpUdpDstPortMask_Object = MibTableColumn
cpuFilterL3RuleTcpUdpDstPortMask = _CpuFilterL3RuleTcpUdpDstPortMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 33, 3, 1, 1, 13),
    _CpuFilterL3RuleTcpUdpDstPortMask_Type()
)
cpuFilterL3RuleTcpUdpDstPortMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuFilterL3RuleTcpUdpDstPortMask.setStatus("current")
_CpuFilterL3RuleTcpUdpSrcPortMask_Type = OctetString
_CpuFilterL3RuleTcpUdpSrcPortMask_Object = MibTableColumn
cpuFilterL3RuleTcpUdpSrcPortMask = _CpuFilterL3RuleTcpUdpSrcPortMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 33, 3, 1, 1, 14),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 33, 3, 1, 1, 15),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 33, 3, 1, 1, 16),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 33, 3, 1, 1, 17),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 33, 3, 1, 1, 18),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 33, 3, 1, 1, 19),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 33, 3, 1, 1, 20),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 33, 3, 1, 1, 21),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 33, 3, 1, 1, 22),
    _CpuFilterL3RuleIgmpType_Type()
)
cpuFilterL3RuleIgmpType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpuFilterL3RuleIgmpType.setStatus("current")
_CpuFilterL3RulePortList_Type = PortList
_CpuFilterL3RulePortList_Object = MibTableColumn
cpuFilterL3RulePortList = _CpuFilterL3RulePortList_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 33, 3, 1, 1, 23),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 33, 3, 1, 1, 24),
    _CpuFilterL3RuleAction_Type()
)
cpuFilterL3RuleAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpuFilterL3RuleAction.setStatus("current")
_CpuFilterL3RuleStatus_Type = RowStatus
_CpuFilterL3RuleStatus_Object = MibTableColumn
cpuFilterL3RuleStatus = _CpuFilterL3RuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 33, 3, 1, 1, 27),
    _CpuFilterL3RuleStatus_Type()
)
cpuFilterL3RuleStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpuFilterL3RuleStatus.setStatus("current")
_CompanyCableDiagnostic_ObjectIdentity = ObjectIdentity
companyCableDiagnostic = _CompanyCableDiagnostic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 35)
)


class _CableDiagTriggerIndex_Type(Integer32):
    """Custom type cableDiagTriggerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 28),
    )


_CableDiagTriggerIndex_Type.__name__ = "Integer32"
_CableDiagTriggerIndex_Object = MibScalar
cableDiagTriggerIndex = _CableDiagTriggerIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 35, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 35, 2),
    _CableDiagPair1TestResult_Type()
)
cableDiagPair1TestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cableDiagPair1TestResult.setStatus("current")
_CableDiagPair1FaultDistance_Type = Integer32
_CableDiagPair1FaultDistance_Object = MibScalar
cableDiagPair1FaultDistance = _CableDiagPair1FaultDistance_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 35, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 35, 4),
    _CableDiagPair2TestResult_Type()
)
cableDiagPair2TestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cableDiagPair2TestResult.setStatus("current")
_CableDiagPair2FaultDistance_Type = Integer32
_CableDiagPair2FaultDistance_Object = MibScalar
cableDiagPair2FaultDistance = _CableDiagPair2FaultDistance_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 35, 5),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 35, 6),
    _CableDiagPair3TestResult_Type()
)
cableDiagPair3TestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cableDiagPair3TestResult.setStatus("current")
_CableDiagPair3FaultDistance_Type = Integer32
_CableDiagPair3FaultDistance_Object = MibScalar
cableDiagPair3FaultDistance = _CableDiagPair3FaultDistance_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 35, 7),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 35, 8),
    _CableDiagPair4TestResult_Type()
)
cableDiagPair4TestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cableDiagPair4TestResult.setStatus("current")
_CableDiagPair4FaultDistance_Type = Integer32
_CableDiagPair4FaultDistance_Object = MibScalar
cableDiagPair4FaultDistance = _CableDiagPair4FaultDistance_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 35, 9),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 35, 10),
    _CableDiagLengthinRange_Type()
)
cableDiagLengthinRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cableDiagLengthinRange.setStatus("current")
_CompanyVLANTrunk_ObjectIdentity = ObjectIdentity
companyVLANTrunk = _CompanyVLANTrunk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 36)
)
_VlanTrunkSystem_ObjectIdentity = ObjectIdentity
vlanTrunkSystem = _VlanTrunkSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 36, 1)
)


class _VlanTrunkGlobalStatus_Type(Integer32):
    """Custom type vlanTrunkGlobalStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_VlanTrunkGlobalStatus_Type.__name__ = "Integer32"
_VlanTrunkGlobalStatus_Object = MibScalar
vlanTrunkGlobalStatus = _VlanTrunkGlobalStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 36, 1, 1),
    _VlanTrunkGlobalStatus_Type()
)
vlanTrunkGlobalStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanTrunkGlobalStatus.setStatus("current")
_VlanTrunkTable_Object = MibTable
vlanTrunkTable = _VlanTrunkTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 36, 1, 2)
)
if mibBuilder.loadTexts:
    vlanTrunkTable.setStatus("current")
_VlanTrunkEntry_Object = MibTableRow
vlanTrunkEntry = _VlanTrunkEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 36, 1, 2, 1)
)
vlanTrunkEntry.setIndexNames(
    (0, "DES-1210-28ME_B2", "vlanTrunkIfIndex"),
)
if mibBuilder.loadTexts:
    vlanTrunkEntry.setStatus("current")
_VlanTrunkIfIndex_Type = InterfaceIndex
_VlanTrunkIfIndex_Object = MibTableColumn
vlanTrunkIfIndex = _VlanTrunkIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 36, 1, 2, 1, 1),
    _VlanTrunkIfIndex_Type()
)
vlanTrunkIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanTrunkIfIndex.setStatus("current")


class _VlanTrunkState_Type(Integer32):
    """Custom type vlanTrunkState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_VlanTrunkState_Type.__name__ = "Integer32"
_VlanTrunkState_Object = MibTableColumn
vlanTrunkState = _VlanTrunkState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 36, 1, 2, 1, 2),
    _VlanTrunkState_Type()
)
vlanTrunkState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanTrunkState.setStatus("current")
_CompanyQinQ_ObjectIdentity = ObjectIdentity
companyQinQ = _CompanyQinQ_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 37)
)
_QinqSystem_ObjectIdentity = ObjectIdentity
qinqSystem = _QinqSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 37, 1)
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 37, 1, 1),
    _QinqGlobalStatus_Type()
)
qinqGlobalStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qinqGlobalStatus.setStatus("current")
_QinqTable_Object = MibTable
qinqTable = _QinqTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 37, 1, 2)
)
if mibBuilder.loadTexts:
    qinqTable.setStatus("current")
_QinqEntry_Object = MibTableRow
qinqEntry = _QinqEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 37, 1, 2, 1)
)
qinqEntry.setIndexNames(
    (0, "DES-1210-28ME_B2", "qinqIfIndex"),
)
if mibBuilder.loadTexts:
    qinqEntry.setStatus("current")
_QinqIfIndex_Type = InterfaceIndex
_QinqIfIndex_Object = MibTableColumn
qinqIfIndex = _QinqIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 37, 1, 2, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 37, 1, 2, 1, 2),
    _QinqRoleState_Type()
)
qinqRoleState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qinqRoleState.setStatus("current")
_QinqOuterTPID_Type = Unsigned32
_QinqOuterTPID_Object = MibTableColumn
qinqOuterTPID = _QinqOuterTPID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 37, 1, 2, 1, 3),
    _QinqOuterTPID_Type()
)
qinqOuterTPID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qinqOuterTPID.setStatus("current")


class _QinqTrustCVIDState_Type(Integer32):
    """Custom type qinqTrustCVIDState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_QinqTrustCVIDState_Type.__name__ = "Integer32"
_QinqTrustCVIDState_Object = MibTableColumn
qinqTrustCVIDState = _QinqTrustCVIDState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 37, 1, 2, 1, 4),
    _QinqTrustCVIDState_Type()
)
qinqTrustCVIDState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qinqTrustCVIDState.setStatus("current")


class _QinqVLANTranslationState_Type(Integer32):
    """Custom type qinqVLANTranslationState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_QinqVLANTranslationState_Type.__name__ = "Integer32"
_QinqVLANTranslationState_Object = MibTableColumn
qinqVLANTranslationState = _QinqVLANTranslationState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 37, 1, 2, 1, 5),
    _QinqVLANTranslationState_Type()
)
qinqVLANTranslationState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qinqVLANTranslationState.setStatus("current")
_QinqVLANTranslation_ObjectIdentity = ObjectIdentity
qinqVLANTranslation = _QinqVLANTranslation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 37, 2)
)
_QinqVlanTranslationCVIDTable_Object = MibTable
qinqVlanTranslationCVIDTable = _QinqVlanTranslationCVIDTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 37, 2, 1)
)
if mibBuilder.loadTexts:
    qinqVlanTranslationCVIDTable.setStatus("current")
_QinqVlanTranslationCVIDEntry_Object = MibTableRow
qinqVlanTranslationCVIDEntry = _QinqVlanTranslationCVIDEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 37, 2, 1, 1)
)
qinqVlanTranslationCVIDEntry.setIndexNames(
    (0, "DES-1210-28ME_B2", "qinqVlanTranslationCVID"),
)
if mibBuilder.loadTexts:
    qinqVlanTranslationCVIDEntry.setStatus("current")
_QinqVlanTranslationCVID_Type = Unsigned32
_QinqVlanTranslationCVID_Object = MibTableColumn
qinqVlanTranslationCVID = _QinqVlanTranslationCVID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 37, 2, 1, 1, 1),
    _QinqVlanTranslationCVID_Type()
)
qinqVlanTranslationCVID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qinqVlanTranslationCVID.setStatus("current")
_QinqVlanTranslationSVID_Type = Unsigned32
_QinqVlanTranslationSVID_Object = MibTableColumn
qinqVlanTranslationSVID = _QinqVlanTranslationSVID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 37, 2, 1, 1, 2),
    _QinqVlanTranslationSVID_Type()
)
qinqVlanTranslationSVID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qinqVlanTranslationSVID.setStatus("current")


class _QinqVlanTranslationSVIDOperation_Type(Integer32):
    """Custom type qinqVlanTranslationSVIDOperation based on Integer32"""
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


_QinqVlanTranslationSVIDOperation_Type.__name__ = "Integer32"
_QinqVlanTranslationSVIDOperation_Object = MibTableColumn
qinqVlanTranslationSVIDOperation = _QinqVlanTranslationSVIDOperation_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 37, 2, 1, 1, 3),
    _QinqVlanTranslationSVIDOperation_Type()
)
qinqVlanTranslationSVIDOperation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qinqVlanTranslationSVIDOperation.setStatus("current")
_QinqVlanTranslationCVIDRowStatus_Type = RowStatus
_QinqVlanTranslationCVIDRowStatus_Object = MibTableColumn
qinqVlanTranslationCVIDRowStatus = _QinqVlanTranslationCVIDRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 37, 2, 1, 1, 4),
    _QinqVlanTranslationCVIDRowStatus_Type()
)
qinqVlanTranslationCVIDRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qinqVlanTranslationCVIDRowStatus.setStatus("current")
_CompanySMTP_ObjectIdentity = ObjectIdentity
companySMTP = _CompanySMTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 40)
)


class _SmtpState_Type(Integer32):
    """Custom type smtpState based on Integer32"""
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


_SmtpState_Type.__name__ = "Integer32"
_SmtpState_Object = MibScalar
smtpState = _SmtpState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 40, 1),
    _SmtpState_Type()
)
smtpState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smtpState.setStatus("current")
_SmtpServerAddr_Type = IpAddress
_SmtpServerAddr_Object = MibScalar
smtpServerAddr = _SmtpServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 40, 2),
    _SmtpServerAddr_Type()
)
smtpServerAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smtpServerAddr.setStatus("current")
_SmtpServerPort_Type = Integer32
_SmtpServerPort_Object = MibScalar
smtpServerPort = _SmtpServerPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 40, 3),
    _SmtpServerPort_Type()
)
smtpServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smtpServerPort.setStatus("current")
_SmtpSelfMailAddr_Type = OctetString
_SmtpSelfMailAddr_Object = MibScalar
smtpSelfMailAddr = _SmtpSelfMailAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 40, 4),
    _SmtpSelfMailAddr_Type()
)
smtpSelfMailAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smtpSelfMailAddr.setStatus("current")
_SmtpRecvMailAddrTable_Object = MibTable
smtpRecvMailAddrTable = _SmtpRecvMailAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 40, 5)
)
if mibBuilder.loadTexts:
    smtpRecvMailAddrTable.setStatus("current")
_SmtpRecvMailAddrEntry_Object = MibTableRow
smtpRecvMailAddrEntry = _SmtpRecvMailAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 40, 5, 1)
)
smtpRecvMailAddrEntry.setIndexNames(
    (0, "DES-1210-28ME_B2", "smtpRecvMailAddrIndex"),
)
if mibBuilder.loadTexts:
    smtpRecvMailAddrEntry.setStatus("current")
_SmtpRecvMailAddrIndex_Type = Integer32
_SmtpRecvMailAddrIndex_Object = MibTableColumn
smtpRecvMailAddrIndex = _SmtpRecvMailAddrIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 40, 5, 1, 1),
    _SmtpRecvMailAddrIndex_Type()
)
smtpRecvMailAddrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smtpRecvMailAddrIndex.setStatus("current")
_SmtpRecvMailAddr_Type = OctetString
_SmtpRecvMailAddr_Object = MibTableColumn
smtpRecvMailAddr = _SmtpRecvMailAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 40, 5, 1, 2),
    _SmtpRecvMailAddr_Type()
)
smtpRecvMailAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smtpRecvMailAddr.setStatus("current")
_SmtpRecvMailAddrStatus_Type = RowStatus
_SmtpRecvMailAddrStatus_Object = MibTableColumn
smtpRecvMailAddrStatus = _SmtpRecvMailAddrStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 40, 5, 1, 3),
    _SmtpRecvMailAddrStatus_Type()
)
smtpRecvMailAddrStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smtpRecvMailAddrStatus.setStatus("current")
_CompanyLimitIp_ObjectIdentity = ObjectIdentity
companyLimitIp = _CompanyLimitIp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 45)
)
_LimitIpMulticastProfileTable_Object = MibTable
limitIpMulticastProfileTable = _LimitIpMulticastProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 45, 1)
)
if mibBuilder.loadTexts:
    limitIpMulticastProfileTable.setStatus("current")
_LimitIpMulticastProfileEntry_Object = MibTableRow
limitIpMulticastProfileEntry = _LimitIpMulticastProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 45, 1, 1)
)
limitIpMulticastProfileEntry.setIndexNames(
    (0, "DES-1210-28ME_B2", "limitIpMulticastProfileID"),
)
if mibBuilder.loadTexts:
    limitIpMulticastProfileEntry.setStatus("current")
_LimitIpMulticastProfileID_Type = Integer32
_LimitIpMulticastProfileID_Object = MibTableColumn
limitIpMulticastProfileID = _LimitIpMulticastProfileID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 45, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 45, 1, 1, 2),
    _LimitIpMulticastProfileName_Type()
)
limitIpMulticastProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    limitIpMulticastProfileName.setStatus("current")
_LimitIpMulticastProfileStatus_Type = RowStatus
_LimitIpMulticastProfileStatus_Object = MibTableColumn
limitIpMulticastProfileStatus = _LimitIpMulticastProfileStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 45, 1, 1, 3),
    _LimitIpMulticastProfileStatus_Type()
)
limitIpMulticastProfileStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    limitIpMulticastProfileStatus.setStatus("current")
_LimitIpMulticastEntryTable_Object = MibTable
limitIpMulticastEntryTable = _LimitIpMulticastEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 45, 2)
)
if mibBuilder.loadTexts:
    limitIpMulticastEntryTable.setStatus("current")
_LimitIpMulticastEntry_Object = MibTableRow
limitIpMulticastEntry = _LimitIpMulticastEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 45, 2, 1)
)
limitIpMulticastEntry.setIndexNames(
    (0, "DES-1210-28ME_B2", "limitIpMulticastEntryProfileID"),
    (0, "DES-1210-28ME_B2", "limitIpMulticaststartIpAddr"),
    (0, "DES-1210-28ME_B2", "limitIpMulticastendIpAddr"),
)
if mibBuilder.loadTexts:
    limitIpMulticastEntry.setStatus("current")
_LimitIpMulticastEntryProfileID_Type = Integer32
_LimitIpMulticastEntryProfileID_Object = MibTableColumn
limitIpMulticastEntryProfileID = _LimitIpMulticastEntryProfileID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 45, 2, 1, 1),
    _LimitIpMulticastEntryProfileID_Type()
)
limitIpMulticastEntryProfileID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    limitIpMulticastEntryProfileID.setStatus("current")
_LimitIpMulticaststartIpAddr_Type = IpAddress
_LimitIpMulticaststartIpAddr_Object = MibTableColumn
limitIpMulticaststartIpAddr = _LimitIpMulticaststartIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 45, 2, 1, 2),
    _LimitIpMulticaststartIpAddr_Type()
)
limitIpMulticaststartIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    limitIpMulticaststartIpAddr.setStatus("current")
_LimitIpMulticastendIpAddr_Type = IpAddress
_LimitIpMulticastendIpAddr_Object = MibTableColumn
limitIpMulticastendIpAddr = _LimitIpMulticastendIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 45, 2, 1, 3),
    _LimitIpMulticastendIpAddr_Type()
)
limitIpMulticastendIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    limitIpMulticastendIpAddr.setStatus("current")
_LimitIpMulticastStatus_Type = RowStatus
_LimitIpMulticastStatus_Object = MibTableColumn
limitIpMulticastStatus = _LimitIpMulticastStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 45, 2, 1, 4),
    _LimitIpMulticastStatus_Type()
)
limitIpMulticastStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    limitIpMulticastStatus.setStatus("current")
_LimitIpMulticastPortTable_Object = MibTable
limitIpMulticastPortTable = _LimitIpMulticastPortTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 45, 3)
)
if mibBuilder.loadTexts:
    limitIpMulticastPortTable.setStatus("current")
_LimitIpMulticastPortEntry_Object = MibTableRow
limitIpMulticastPortEntry = _LimitIpMulticastPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 45, 3, 1)
)
limitIpMulticastPortEntry.setIndexNames(
    (0, "DES-1210-28ME_B2", "limitIpMulticastPortID"),
)
if mibBuilder.loadTexts:
    limitIpMulticastPortEntry.setStatus("current")
_LimitIpMulticastPortID_Type = Integer32
_LimitIpMulticastPortID_Object = MibTableColumn
limitIpMulticastPortID = _LimitIpMulticastPortID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 45, 3, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 45, 3, 1, 2),
    _LimitIpMulticastPortState_Type()
)
limitIpMulticastPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    limitIpMulticastPortState.setStatus("current")
_LimitIpMulticastPortProfileID_Type = PortList
_LimitIpMulticastPortProfileID_Object = MibTableColumn
limitIpMulticastPortProfileID = _LimitIpMulticastPortProfileID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 45, 3, 1, 3),
    _LimitIpMulticastPortProfileID_Type()
)
limitIpMulticastPortProfileID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    limitIpMulticastPortProfileID.setStatus("current")


class _LimitIpMulticastPortMaxGrp_Type(Integer32):
    """Custom type limitIpMulticastPortMaxGrp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_LimitIpMulticastPortMaxGrp_Type.__name__ = "Integer32"
_LimitIpMulticastPortMaxGrp_Object = MibTableColumn
limitIpMulticastPortMaxGrp = _LimitIpMulticastPortMaxGrp_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 45, 3, 1, 4),
    _LimitIpMulticastPortMaxGrp_Type()
)
limitIpMulticastPortMaxGrp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    limitIpMulticastPortMaxGrp.setStatus("current")
_CompanyGratuitousARP_ObjectIdentity = ObjectIdentity
companyGratuitousARP = _CompanyGratuitousARP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 48)
)
_SysGratuitousARPGlobalSettings_ObjectIdentity = ObjectIdentity
sysGratuitousARPGlobalSettings = _SysGratuitousARPGlobalSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 48, 1)
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 48, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 48, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 48, 1, 3),
    _SysGratuitousARPLearning_Type()
)
sysGratuitousARPLearning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysGratuitousARPLearning.setStatus("current")
_SysGratuitousARPSettings_ObjectIdentity = ObjectIdentity
sysGratuitousARPSettings = _SysGratuitousARPSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 48, 2)
)
_SysGratuitousARPTable_Object = MibTable
sysGratuitousARPTable = _SysGratuitousARPTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 48, 2, 1)
)
if mibBuilder.loadTexts:
    sysGratuitousARPTable.setStatus("current")
_SysGratuitousARPEntry_Object = MibTableRow
sysGratuitousARPEntry = _SysGratuitousARPEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 48, 2, 1, 1)
)
sysGratuitousARPEntry.setIndexNames(
    (0, "DES-1210-28ME_B2", "sysGratuitousARPIFName"),
)
if mibBuilder.loadTexts:
    sysGratuitousARPEntry.setStatus("current")
_SysGratuitousARPIFName_Type = OctetString
_SysGratuitousARPIFName_Object = MibTableColumn
sysGratuitousARPIFName = _SysGratuitousARPIFName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 48, 2, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 48, 2, 1, 1, 2),
    _SysGratuitousARPInterval_Type()
)
sysGratuitousARPInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysGratuitousARPInterval.setStatus("current")
_CompanyMulticastFilter_ObjectIdentity = ObjectIdentity
companyMulticastFilter = _CompanyMulticastFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 49)
)
_McastFilterPortTable_Object = MibTable
mcastFilterPortTable = _McastFilterPortTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 49, 1)
)
if mibBuilder.loadTexts:
    mcastFilterPortTable.setStatus("current")
_McastFilterPortEntry_Object = MibTableRow
mcastFilterPortEntry = _McastFilterPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 49, 1, 1)
)
mcastFilterPortEntry.setIndexNames(
    (0, "DES-1210-28ME_B2", "mcastFilterPortIndex"),
)
if mibBuilder.loadTexts:
    mcastFilterPortEntry.setStatus("current")
_McastFilterPortIndex_Type = Integer32
_McastFilterPortIndex_Object = MibTableColumn
mcastFilterPortIndex = _McastFilterPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 49, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 49, 1, 1, 2),
    _McastFilterPortType_Type()
)
mcastFilterPortType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcastFilterPortType.setStatus("current")
_CompanyBPDUAttack_ObjectIdentity = ObjectIdentity
companyBPDUAttack = _CompanyBPDUAttack_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 77)
)


class _SysBPDUAttackStateEnable_Type(Integer32):
    """Custom type sysBPDUAttackStateEnable based on Integer32"""
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


_SysBPDUAttackStateEnable_Type.__name__ = "Integer32"
_SysBPDUAttackStateEnable_Object = MibScalar
sysBPDUAttackStateEnable = _SysBPDUAttackStateEnable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 77, 1),
    _SysBPDUAttackStateEnable_Type()
)
sysBPDUAttackStateEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysBPDUAttackStateEnable.setStatus("current")


class _SysBPDUAttackRecoverTime_Type(Integer32):
    """Custom type sysBPDUAttackRecoverTime based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(60, 1000000),
    )


_SysBPDUAttackRecoverTime_Type.__name__ = "Integer32"
_SysBPDUAttackRecoverTime_Object = MibScalar
sysBPDUAttackRecoverTime = _SysBPDUAttackRecoverTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 77, 2),
    _SysBPDUAttackRecoverTime_Type()
)
sysBPDUAttackRecoverTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysBPDUAttackRecoverTime.setStatus("current")
_SysBPDUAttackCtrlTable_Object = MibTable
sysBPDUAttackCtrlTable = _SysBPDUAttackCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 77, 3)
)
if mibBuilder.loadTexts:
    sysBPDUAttackCtrlTable.setStatus("current")
_SysBPDUAttackCtrlEntry_Object = MibTableRow
sysBPDUAttackCtrlEntry = _SysBPDUAttackCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 77, 3, 1)
)
sysBPDUAttackCtrlEntry.setIndexNames(
    (0, "DES-1210-28ME_B2", "sysBPDUAttackCtrlIndex"),
)
if mibBuilder.loadTexts:
    sysBPDUAttackCtrlEntry.setStatus("current")
_SysBPDUAttackCtrlIndex_Type = Integer32
_SysBPDUAttackCtrlIndex_Object = MibTableColumn
sysBPDUAttackCtrlIndex = _SysBPDUAttackCtrlIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 77, 3, 1, 1),
    _SysBPDUAttackCtrlIndex_Type()
)
sysBPDUAttackCtrlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysBPDUAttackCtrlIndex.setStatus("current")


class _SysBPDUAttackPortState_Type(Integer32):
    """Custom type sysBPDUAttackPortState based on Integer32"""
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


_SysBPDUAttackPortState_Type.__name__ = "Integer32"
_SysBPDUAttackPortState_Object = MibTableColumn
sysBPDUAttackPortState = _SysBPDUAttackPortState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 77, 3, 1, 2),
    _SysBPDUAttackPortState_Type()
)
sysBPDUAttackPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysBPDUAttackPortState.setStatus("current")


class _SysBPDUAttackPortMode_Type(Integer32):
    """Custom type sysBPDUAttackPortMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("block", 2),
          ("drop", 1),
          ("shutdown", 3))
    )


_SysBPDUAttackPortMode_Type.__name__ = "Integer32"
_SysBPDUAttackPortMode_Object = MibTableColumn
sysBPDUAttackPortMode = _SysBPDUAttackPortMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 77, 3, 1, 3),
    _SysBPDUAttackPortMode_Type()
)
sysBPDUAttackPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysBPDUAttackPortMode.setStatus("current")


class _SysBPDUAttackPortStatus_Type(Integer32):
    """Custom type sysBPDUAttackPortStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("underAttack", 2))
    )


_SysBPDUAttackPortStatus_Type.__name__ = "Integer32"
_SysBPDUAttackPortStatus_Object = MibTableColumn
sysBPDUAttackPortStatus = _SysBPDUAttackPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 77, 3, 1, 4),
    _SysBPDUAttackPortStatus_Type()
)
sysBPDUAttackPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysBPDUAttackPortStatus.setStatus("current")


class _SysBPDUAttackLog_Type(Integer32):
    """Custom type sysBPDUAttackLog based on Integer32"""
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
        *(("attackCleared", 3),
          ("attackDetected", 2),
          ("both", 4),
          ("none", 1))
    )


_SysBPDUAttackLog_Type.__name__ = "Integer32"
_SysBPDUAttackLog_Object = MibScalar
sysBPDUAttackLog = _SysBPDUAttackLog_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 77, 4),
    _SysBPDUAttackLog_Type()
)
sysBPDUAttackLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysBPDUAttackLog.setStatus("current")
_CompanyDoSCtrl_ObjectIdentity = ObjectIdentity
companyDoSCtrl = _CompanyDoSCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 99)
)


class _DoSTrapLog_Type(Integer32):
    """Custom type doSTrapLog based on Integer32"""
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
          ("other", 3))
    )


_DoSTrapLog_Type.__name__ = "Integer32"
_DoSTrapLog_Object = MibScalar
doSTrapLog = _DoSTrapLog_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 99, 1),
    _DoSTrapLog_Type()
)
doSTrapLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    doSTrapLog.setStatus("current")


class _DoSClearCounters_Type(Integer32):
    """Custom type doSClearCounters based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("all", 8),
          ("blat-attack", 2),
          ("land-attack", 1),
          ("other", 9),
          ("smurf-attack", 3),
          ("tcp-null-scan", 4),
          ("tcp-syn-srcport-less-1024", 7),
          ("tcp-synfin", 6),
          ("tcp-xmascan", 5))
    )


_DoSClearCounters_Type.__name__ = "Integer32"
_DoSClearCounters_Object = MibScalar
doSClearCounters = _DoSClearCounters_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 99, 2),
    _DoSClearCounters_Type()
)
doSClearCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    doSClearCounters.setStatus("current")
_DoSCtrlTable_Object = MibTable
doSCtrlTable = _DoSCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 99, 3)
)
if mibBuilder.loadTexts:
    doSCtrlTable.setStatus("current")
_DoSCtrlEntry_Object = MibTableRow
doSCtrlEntry = _DoSCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 99, 3, 1)
)
doSCtrlEntry.setIndexNames(
    (0, "DES-1210-28ME_B2", "doSCtrlType"),
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
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("blat-attack", 2),
          ("land-attack", 1),
          ("smurf-attack", 3),
          ("tcp-null-scan", 4),
          ("tcp-syn-srcport-less-1024", 7),
          ("tcp-synfin", 6),
          ("tcp-xmascan", 5))
    )


_DoSCtrlType_Type.__name__ = "Integer32"
_DoSCtrlType_Object = MibTableColumn
doSCtrlType = _DoSCtrlType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 99, 3, 1, 1),
    _DoSCtrlType_Type()
)
doSCtrlType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    doSCtrlType.setStatus("current")


class _DoSCtrlState_Type(Integer32):
    """Custom type doSCtrlState based on Integer32"""
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


_DoSCtrlState_Type.__name__ = "Integer32"
_DoSCtrlState_Object = MibTableColumn
doSCtrlState = _DoSCtrlState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 99, 3, 1, 2),
    _DoSCtrlState_Type()
)
doSCtrlState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    doSCtrlState.setStatus("current")


class _DoSCtrlActionType_Type(Integer32):
    """Custom type doSCtrlActionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("drop", 1),
          ("mirror", 2))
    )


_DoSCtrlActionType_Type.__name__ = "Integer32"
_DoSCtrlActionType_Object = MibTableColumn
doSCtrlActionType = _DoSCtrlActionType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 99, 3, 1, 3),
    _DoSCtrlActionType_Type()
)
doSCtrlActionType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    doSCtrlActionType.setStatus("current")


class _DoSCtrlMirrorPort_Type(Integer32):
    """Custom type doSCtrlMirrorPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DoSCtrlMirrorPort_Type.__name__ = "Integer32"
_DoSCtrlMirrorPort_Object = MibTableColumn
doSCtrlMirrorPort = _DoSCtrlMirrorPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 99, 3, 1, 4),
    _DoSCtrlMirrorPort_Type()
)
doSCtrlMirrorPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    doSCtrlMirrorPort.setStatus("current")


class _DoSCtrlMirrorPriority_Type(Integer32):
    """Custom type doSCtrlMirrorPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_DoSCtrlMirrorPriority_Type.__name__ = "Integer32"
_DoSCtrlMirrorPriority_Object = MibTableColumn
doSCtrlMirrorPriority = _DoSCtrlMirrorPriority_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 99, 3, 1, 5),
    _DoSCtrlMirrorPriority_Type()
)
doSCtrlMirrorPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    doSCtrlMirrorPriority.setStatus("current")


class _DoSCtrlMirrorRxRate_Type(Integer32):
    """Custom type doSCtrlMirrorRxRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024000),
    )


_DoSCtrlMirrorRxRate_Type.__name__ = "Integer32"
_DoSCtrlMirrorRxRate_Object = MibTableColumn
doSCtrlMirrorRxRate = _DoSCtrlMirrorRxRate_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 99, 3, 1, 6),
    _DoSCtrlMirrorRxRate_Type()
)
doSCtrlMirrorRxRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    doSCtrlMirrorRxRate.setStatus("current")
_DoSCtrlFrameCount_Type = Integer32
_DoSCtrlFrameCount_Object = MibTableColumn
doSCtrlFrameCount = _DoSCtrlFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 99, 3, 1, 7),
    _DoSCtrlFrameCount_Type()
)
doSCtrlFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    doSCtrlFrameCount.setStatus("current")
_DoSNotify_ObjectIdentity = ObjectIdentity
doSNotify = _DoSNotify_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 99, 4)
)
_DoSNotifyPrefix_ObjectIdentity = ObjectIdentity
doSNotifyPrefix = _DoSNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 99, 4, 0)
)
_DoSNotifyVarBindings_ObjectIdentity = ObjectIdentity
doSNotifyVarBindings = _DoSNotifyVarBindings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 99, 4, 1)
)
_DoSNotifyVarIpAddr_Type = IpAddress
_DoSNotifyVarIpAddr_Object = MibScalar
doSNotifyVarIpAddr = _DoSNotifyVarIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 99, 4, 1, 1),
    _DoSNotifyVarIpAddr_Type()
)
doSNotifyVarIpAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    doSNotifyVarIpAddr.setStatus("current")
_DoSNotifyVarPortNumber_Type = DisplayString
_DoSNotifyVarPortNumber_Object = MibScalar
doSNotifyVarPortNumber = _DoSNotifyVarPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 99, 4, 1, 2),
    _DoSNotifyVarPortNumber_Type()
)
doSNotifyVarPortNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    doSNotifyVarPortNumber.setStatus("current")
lldpPortConfigEntry.registerAugmentions(
    ("DES-1210-28ME_B2",
     "lldpXdot3PortConfigEntry")
)
lldpXdot3PortConfigEntry.setIndexNames(*lldpPortConfigEntry.getIndexNames())
lldpPortConfigEntry.registerAugmentions(
    ("DES-1210-28ME_B2",
     "lldpXdot1ConfigPortVlanEntry")
)
lldpXdot1ConfigPortVlanEntry.setIndexNames(*lldpPortConfigEntry.getIndexNames())
lldpXdot1LocVlanNameEntry.registerAugmentions(
    ("DES-1210-28ME_B2",
     "lldpXdot1ConfigVlanNameEntry")
)
lldpXdot1ConfigVlanNameEntry.setIndexNames(*lldpXdot1LocVlanNameEntry.getIndexNames())
lldpXdot1LocProtoVlanEntry.registerAugmentions(
    ("DES-1210-28ME_B2",
     "lldpXdot1ConfigProtoVlanEntry")
)
lldpXdot1ConfigProtoVlanEntry.setIndexNames(*lldpXdot1LocProtoVlanEntry.getIndexNames())
lldpXdot1LocProtocolEntry.registerAugmentions(
    ("DES-1210-28ME_B2",
     "lldpXdot1ConfigProtocolEntry")
)
lldpXdot1ConfigProtocolEntry.setIndexNames(*lldpXdot1LocProtocolEntry.getIndexNames())

# Managed Objects groups


# Notification objects

doSAttackDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 10, 75, 15, 2, 99, 4, 0, 1)
)
doSAttackDetected.setObjects(
      *(("DES-1210-28ME_B2", "doSCtrlType"),
        ("DES-1210-28ME_B2", "doSNotifyVarIpAddr"),
        ("DES-1210-28ME_B2", "doSNotifyVarPortNumber"))
)
if mibBuilder.loadTexts:
    doSAttackDetected.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DES-1210-28ME_B2",
    **{"VlanIndex": VlanIndex,
       "PortList": PortList,
       "BridgeId": BridgeId,
       "Timeout": Timeout,
       "LldpManAddress": LldpManAddress,
       "OwnerString": OwnerString,
       "RmonStatus": RmonStatus,
       "PortLaMode": PortLaMode,
       "LacpKey": LacpKey,
       "LldpPortNumber": LldpPortNumber,
       "LldpPowerPortClass": LldpPowerPortClass,
       "LldpLinkAggStatusMap": LldpLinkAggStatusMap,
       "d-link": d_link,
       "dlink-products": dlink_products,
       "dlink-DES1210SeriesProd": dlink_DES1210SeriesProd,
       "des-1210-28ME": des_1210_28ME,
       "des-1210-28ME-B2": des_1210_28ME_B2,
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
       "companyIpifGroup": companyIpifGroup,
       "sysIpAddrCfgMode": sysIpAddrCfgMode,
       "sysIpAddr": sysIpAddr,
       "sysIpSubnetMask": sysIpSubnetMask,
       "sysGateway": sysGateway,
       "dhcpOption12Status": dhcpOption12Status,
       "dhcpOption12HostName": dhcpOption12HostName,
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
       "snmpV3TrapFiberLinkUpDown": snmpV3TrapFiberLinkUpDown,
       "snmpV3TrapCopperLinkUpDown": snmpV3TrapCopperLinkUpDown,
       "snmpV3TrapRSTPStateChange": snmpV3TrapRSTPStateChange,
       "snmpV3TrapFirmUpgrade": snmpV3TrapFirmUpgrade,
       "snmpV3TrapBPDUAttack": snmpV3TrapBPDUAttack,
       "snmpV3TrapPortSecurity": snmpV3TrapPortSecurity,
       "snmpV3TrapIMPBViolation": snmpV3TrapIMPBViolation,
       "snmpV3TrapLBD": snmpV3TrapLBD,
       "snmpV3TrapDHCPServerScreening": snmpV3TrapDHCPServerScreening,
       "snmpV3TrapDuplicateIPDetected": snmpV3TrapDuplicateIPDetected,
       "companySTP": companySTP,
       "stpBridgeGlobal": stpBridgeGlobal,
       "stpModuleStatus": stpModuleStatus,
       "stpProtocolVersion": stpProtocolVersion,
       "stpBridgePriority": stpBridgePriority,
       "stpTxHoldCount": stpTxHoldCount,
       "stpBridgeMaxAge": stpBridgeMaxAge,
       "stpBridgeHelloTime": stpBridgeHelloTime,
       "stpBridgeForwardDelay": stpBridgeForwardDelay,
       "stpFowardBPDU": stpFowardBPDU,
       "stpRootBridge": stpRootBridge,
       "stpRootCost": stpRootCost,
       "stpMaxAge": stpMaxAge,
       "stpForwardDelay": stpForwardDelay,
       "stpRootPort": stpRootPort,
       "stpPortTable": stpPortTable,
       "stpPortEntry": stpPortEntry,
       "stpPort": stpPort,
       "stpPortStatus": stpPortStatus,
       "stpPortPriority": stpPortPriority,
       "stpAdminPortPathCost": stpAdminPortPathCost,
       "stpPortPathCost": stpPortPathCost,
       "stpPortProtocolMigration": stpPortProtocolMigration,
       "stpPortEdge": stpPortEdge,
       "stpPortAdminP2P": stpPortAdminP2P,
       "stpPortRestrictedRole": stpPortRestrictedRole,
       "stpPortRestrictedTCN": stpPortRestrictedTCN,
       "stpPortHelloTime": stpPortHelloTime,
       "stpPortState": stpPortState,
       "stpPortFowardBPDU": stpPortFowardBPDU,
       "mstConfigurationIdentification": mstConfigurationIdentification,
       "mstiConfigurationName": mstiConfigurationName,
       "mstiRevisionLevel": mstiRevisionLevel,
       "mstCistVlanMapped": mstCistVlanMapped,
       "mstCistVlanMapped2k": mstCistVlanMapped2k,
       "mstCistVlanMapped3k": mstCistVlanMapped3k,
       "mstCistVlanMapped4k": mstCistVlanMapped4k,
       "mstVlanMstiMappingTable": mstVlanMstiMappingTable,
       "mstVlanMstiMappingEntry": mstVlanMstiMappingEntry,
       "mstInstanceIndex": mstInstanceIndex,
       "mstSetVlanList": mstSetVlanList,
       "mstResetVlanList": mstResetVlanList,
       "mstInstanceVlanMapped": mstInstanceVlanMapped,
       "mstInstanceVlanMapped2k": mstInstanceVlanMapped2k,
       "mstInstanceVlanMapped3k": mstInstanceVlanMapped3k,
       "mstInstanceVlanMapped4k": mstInstanceVlanMapped4k,
       "stpInstance": stpInstance,
       "mstCistBridgePriority": mstCistBridgePriority,
       "mstCistStatus": mstCistStatus,
       "mstMstiBridgeTable": mstMstiBridgeTable,
       "mstMstiBridgeEntry": mstMstiBridgeEntry,
       "mstMstiInstanceIndex": mstMstiInstanceIndex,
       "mstMstiBridgePriority": mstMstiBridgePriority,
       "mstMstiStatus": mstMstiStatus,
       "stpInstancePortTable": stpInstancePortTable,
       "mstCistPortTable": mstCistPortTable,
       "mstCistPortEntry": mstCistPortEntry,
       "mstCistPort": mstCistPort,
       "mstCistPortDesignatedBridge": mstCistPortDesignatedBridge,
       "mstCistPortAdminPathCost": mstCistPortAdminPathCost,
       "mstCistPortPathCost": mstCistPortPathCost,
       "mstCistPortPriority": mstCistPortPriority,
       "mstCistForcePortState": mstCistForcePortState,
       "mstCistCurrentPortRole": mstCistCurrentPortRole,
       "mstMstiPortTable": mstMstiPortTable,
       "mstMstiPortEntry": mstMstiPortEntry,
       "mstMstiPort": mstMstiPort,
       "mstMstiPortDesignatedBridge": mstMstiPortDesignatedBridge,
       "mstMstiPortAdminPathCost": mstMstiPortAdminPathCost,
       "mstMstiPortPathCost": mstMstiPortPathCost,
       "mstMstiPortPriority": mstMstiPortPriority,
       "mstMstiForcePortState": mstMstiForcePortState,
       "mstMstiCurrentPortRole": mstMstiCurrentPortRole,
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
       "dot1qVlanAdvertisementStatus": dot1qVlanAdvertisementStatus,
       "dot1qVlanRowStatus": dot1qVlanRowStatus,
       "companyLA": companyLA,
       "laSystem": laSystem,
       "laStatus": laStatus,
       "laPortChannelTable": laPortChannelTable,
       "laPortChannelEntry": laPortChannelEntry,
       "laPortChannelIfIndex": laPortChannelIfIndex,
       "laPortChannelMemberList": laPortChannelMemberList,
       "laPortChannelMode": laPortChannelMode,
       "laPortChannelMasterPort": laPortChannelMasterPort,
       "laAlgorithm": laAlgorithm,
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
       "igsDataDrivenLearningMaxLearnedEntryVlaue": igsDataDrivenLearningMaxLearnedEntryVlaue,
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
       "igsVlanFbdRtrPortList": igsVlanFbdRtrPortList,
       "igsVlanFastLeave": igsVlanFastLeave,
       "igsVlanDataDrivenLearningStatus": igsVlanDataDrivenLearningStatus,
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
       "companyQoSGroup": companyQoSGroup,
       "cosScheduleMechanism": cosScheduleMechanism,
       "cosOutputSchedule": cosOutputSchedule,
       "cosClassTable": cosClassTable,
       "cosClassEntry": cosClassEntry,
       "cosClassIndex": cosClassIndex,
       "cosWeight": cosWeight,
       "qosDefaultUserPri": qosDefaultUserPri,
       "qosDefaultUserPriTable": qosDefaultUserPriTable,
       "qosDefaultUserPriEntry": qosDefaultUserPriEntry,
       "qosDefaultUserPriPortIndex": qosDefaultUserPriPortIndex,
       "qosDefaultPriority": qosDefaultPriority,
       "qosEffectiveDefaultPriority": qosEffectiveDefaultPriority,
       "qosUserPriority": qosUserPriority,
       "qosUserPriorityTable": qosUserPriorityTable,
       "qosUserPriEntry": qosUserPriEntry,
       "qosUserPriIndex": qosUserPriIndex,
       "qosUserPriClass": qosUserPriClass,
       "qosDiffServTOS": qosDiffServTOS,
       "qosDSCPTOSMode": qosDSCPTOSMode,
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
       "qosTOSGroup": qosTOSGroup,
       "qosTOSType00": qosTOSType00,
       "qosTOSType01": qosTOSType01,
       "qosTOSType02": qosTOSType02,
       "qosTOSType03": qosTOSType03,
       "qosTOSType04": qosTOSType04,
       "qosTOSType05": qosTOSType05,
       "qosTOSType06": qosTOSType06,
       "qosTOSType07": qosTOSType07,
       "qosPriSettings": qosPriSettings,
       "qosPriSettingsTable": qosPriSettingsTable,
       "qosPriSettingsEntry": qosPriSettingsEntry,
       "qosPriSetPortIndex": qosPriSetPortIndex,
       "qosPriSetPortType": qosPriSetPortType,
       "qosAclPrioritySettings": qosAclPrioritySettings,
       "aclQosTable": aclQosTable,
       "aclQosEntry": aclQosEntry,
       "aclQosIndex": aclQosIndex,
       "aclQosType": aclQosType,
       "aclQosMACAddr": aclQosMACAddr,
       "aclQosIPAddr": aclQosIPAddr,
       "aclQosTCPUDPPort": aclQosTCPUDPPort,
       "aclQosVlanID": aclQosVlanID,
       "aclQosProtocol": aclQosProtocol,
       "aclQosAssignClass": aclQosAssignClass,
       "aclQosStatus": aclQosStatus,
       "companyTrafficMgmt": companyTrafficMgmt,
       "bandwidthCtrlSettings": bandwidthCtrlSettings,
       "bandwidthCtrlTable": bandwidthCtrlTable,
       "bandwidthCtrlEntry": bandwidthCtrlEntry,
       "bandwidthCtrlIndex": bandwidthCtrlIndex,
       "bandwidthCtrlTxThreshold": bandwidthCtrlTxThreshold,
       "bandwidthCtrlRxThreshold": bandwidthCtrlRxThreshold,
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
       "portSecLockAddrMode": portSecLockAddrMode,
       "portSecFDBPermanentTable": portSecFDBPermanentTable,
       "portSecFDBPermanentEntry": portSecFDBPermanentEntry,
       "portSecFDBPermIndex": portSecFDBPermIndex,
       "portSecFDBPermVlanID": portSecFDBPermVlanID,
       "portSecFDBPermMac": portSecFDBPermMac,
       "portSecFDBPermPort": portSecFDBPermPort,
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
       "filterDHCPServerTable": filterDHCPServerTable,
       "filterDHCPServerEntry": filterDHCPServerEntry,
       "filterDHCPServerIpAddr": filterDHCPServerIpAddr,
       "filterDHCPServerClientMacAddr": filterDHCPServerClientMacAddr,
       "filterDHCPServerPortList": filterDHCPServerPortList,
       "filterDHCPServerRowStatus": filterDHCPServerRowStatus,
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
       "securityTrafficSeg": securityTrafficSeg,
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
       "securityAAC": securityAAC,
       "aacAuthenAdminState": aacAuthenAdminState,
       "aacAuthParamResponseTimeout": aacAuthParamResponseTimeout,
       "aacAuthParamAttempt": aacAuthParamAttempt,
       "aacAPAuthMethodGroup": aacAPAuthMethodGroup,
       "aacAPLoginMethod": aacAPLoginMethod,
       "aacAPConsoleLoginMethod": aacAPConsoleLoginMethod,
       "aacAPTelnetLoginMethod": aacAPTelnetLoginMethod,
       "aacAPSSHLoginMethod": aacAPSSHLoginMethod,
       "aacAPHttpLoginMethod": aacAPHttpLoginMethod,
       "aacAPEnableMethod": aacAPEnableMethod,
       "aacAPConsoleEnableMethod": aacAPConsoleEnableMethod,
       "aacAPTelnetEnableMethod": aacAPTelnetEnableMethod,
       "aacAPSSHEnableMethod": aacAPSSHEnableMethod,
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
       "aacServerIPAddr": aacServerIPAddr,
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
       "aclProfileDstIpAddrMask": aclProfileDstIpAddrMask,
       "aclProfileSrcIpAddrMask": aclProfileSrcIpAddrMask,
       "aclProfileDstPortMask": aclProfileDstPortMask,
       "aclProfileSrcPortMask": aclProfileSrcPortMask,
       "aclProfileArpSenderMacAddrMask": aclProfileArpSenderMacAddrMask,
       "aclProfileArpSenderIpAddrMask": aclProfileArpSenderIpAddrMask,
       "aclProfileUdfOffsetMap": aclProfileUdfOffsetMap,
       "aclUdfOffsetBase1": aclUdfOffsetBase1,
       "aclUdfOffsetByte1": aclUdfOffsetByte1,
       "aclUdfOffsetMask1": aclUdfOffsetMask1,
       "aclUdfOffsetBase2": aclUdfOffsetBase2,
       "aclUdfOffsetByte2": aclUdfOffsetByte2,
       "aclUdfOffsetMask2": aclUdfOffsetMask2,
       "aclUdfOffsetBase3": aclUdfOffsetBase3,
       "aclUdfOffsetByte3": aclUdfOffsetByte3,
       "aclUdfOffsetMask3": aclUdfOffsetMask3,
       "aclUdfOffsetBase4": aclUdfOffsetBase4,
       "aclUdfOffsetByte4": aclUdfOffsetByte4,
       "aclUdfOffsetMask4": aclUdfOffsetMask4,
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
       "aclL2RuleReplace1P": aclL2RuleReplace1P,
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
       "aclL3RuleReplace1P": aclL3RuleReplace1P,
       "aclL3RuleStatus": aclL3RuleStatus,
       "aclPacketRule": aclPacketRule,
       "aclPacketRuleTable": aclPacketRuleTable,
       "aclPacketRuleEntry": aclPacketRuleEntry,
       "aclPacketAccessID": aclPacketAccessID,
       "aclPacketProfileID": aclPacketProfileID,
       "aclPacketRuleOffsetValue1": aclPacketRuleOffsetValue1,
       "aclPacketRuleOffsetValue2": aclPacketRuleOffsetValue2,
       "aclPacketRuleOffsetValue3": aclPacketRuleOffsetValue3,
       "aclPacketRuleOffsetValue4": aclPacketRuleOffsetValue4,
       "aclPacketRuleInPortList": aclPacketRuleInPortList,
       "aclPacketRuleAction": aclPacketRuleAction,
       "aclPacketRuleRateLimit": aclPacketRuleRateLimit,
       "aclPacketRuleReplaceDSCP": aclPacketRuleReplaceDSCP,
       "aclPacketRuleReplace1P": aclPacketRuleReplace1P,
       "aclPacketRuleStatus": aclPacketRuleStatus,
       "companySyslog": companySyslog,
       "syslogSettingGroup": syslogSettingGroup,
       "syslogEnable": syslogEnable,
       "syslogSaveMode": syslogSaveMode,
       "syslogSaveMinutes": syslogSaveMinutes,
       "syslogServerGroup": syslogServerGroup,
       "syslogServTable": syslogServTable,
       "syslogServEntry": syslogServEntry,
       "syslogServIndex": syslogServIndex,
       "syslogServAddr": syslogServAddr,
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
       "staticMcastStatus": staticMcastStatus,
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
       "swAuthRadiusServerAddress": swAuthRadiusServerAddress,
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
       "companyISMVLAN": companyISMVLAN,
       "igmpMulticastVlanStatus": igmpMulticastVlanStatus,
       "igmpMulticastVlanTable": igmpMulticastVlanTable,
       "igmpMulticastVlanEntry": igmpMulticastVlanEntry,
       "igmpMulticastVlanid": igmpMulticastVlanid,
       "igmpMulticastVlanName": igmpMulticastVlanName,
       "igmpMulticastVlanSourcePort": igmpMulticastVlanSourcePort,
       "igmpMulticastVlanMemberPort": igmpMulticastVlanMemberPort,
       "igmpMulticastVlanTagMemberPort": igmpMulticastVlanTagMemberPort,
       "igmpMulticastVlanState": igmpMulticastVlanState,
       "igmpMulticastVlanReplaceSourceIp": igmpMulticastVlanReplaceSourceIp,
       "igmpMulticastVlanRowStatus": igmpMulticastVlanRowStatus,
       "igmpMulticastVlanGroupTable": igmpMulticastVlanGroupTable,
       "igmpMulticastVlanGroupEntry": igmpMulticastVlanGroupEntry,
       "igmpMulticastVlanGroupVid": igmpMulticastVlanGroupVid,
       "igmpMulticastVlanGroupFromIp": igmpMulticastVlanGroupFromIp,
       "igmpMulticastVlanGroupToIp": igmpMulticastVlanGroupToIp,
       "igmpMulticastVlanGroupStatus": igmpMulticastVlanGroupStatus,
       "companyDHCPRelay": companyDHCPRelay,
       "dhcpBOOTPRelayControl": dhcpBOOTPRelayControl,
       "dhcpBOOTPRelayState": dhcpBOOTPRelayState,
       "dhcpBOOTPRelayHopCount": dhcpBOOTPRelayHopCount,
       "dhcpBOOTPRelayTimeThreshold": dhcpBOOTPRelayTimeThreshold,
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
       "companyTrapSetting": companyTrapSetting,
       "sysTrapIP": sysTrapIP,
       "sysTrapSystemEvent": sysTrapSystemEvent,
       "sysTrapFiberPortEvent": sysTrapFiberPortEvent,
       "sysTrapTwistedPortEvent": sysTrapTwistedPortEvent,
       "sysTrapStateChangeEvent": sysTrapStateChangeEvent,
       "sysTrapFirmUpgradeEvent": sysTrapFirmUpgradeEvent,
       "sysTrapStatus": sysTrapStatus,
       "sysTrapPortSecurity": sysTrapPortSecurity,
       "sysTrapIMPBViolation": sysTrapIMPBViolation,
       "sysTrapLBD": sysTrapLBD,
       "sysTrapDHCPServerScreening": sysTrapDHCPServerScreening,
       "sysTrapDuplicateIPDetected": sysTrapDuplicateIPDetected,
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
       "cpuFilterProfileDstIpAddrMask": cpuFilterProfileDstIpAddrMask,
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
       "companyVLANTrunk": companyVLANTrunk,
       "vlanTrunkSystem": vlanTrunkSystem,
       "vlanTrunkGlobalStatus": vlanTrunkGlobalStatus,
       "vlanTrunkTable": vlanTrunkTable,
       "vlanTrunkEntry": vlanTrunkEntry,
       "vlanTrunkIfIndex": vlanTrunkIfIndex,
       "vlanTrunkState": vlanTrunkState,
       "companyQinQ": companyQinQ,
       "qinqSystem": qinqSystem,
       "qinqGlobalStatus": qinqGlobalStatus,
       "qinqTable": qinqTable,
       "qinqEntry": qinqEntry,
       "qinqIfIndex": qinqIfIndex,
       "qinqRoleState": qinqRoleState,
       "qinqOuterTPID": qinqOuterTPID,
       "qinqTrustCVIDState": qinqTrustCVIDState,
       "qinqVLANTranslationState": qinqVLANTranslationState,
       "qinqVLANTranslation": qinqVLANTranslation,
       "qinqVlanTranslationCVIDTable": qinqVlanTranslationCVIDTable,
       "qinqVlanTranslationCVIDEntry": qinqVlanTranslationCVIDEntry,
       "qinqVlanTranslationCVID": qinqVlanTranslationCVID,
       "qinqVlanTranslationSVID": qinqVlanTranslationSVID,
       "qinqVlanTranslationSVIDOperation": qinqVlanTranslationSVIDOperation,
       "qinqVlanTranslationCVIDRowStatus": qinqVlanTranslationCVIDRowStatus,
       "companySMTP": companySMTP,
       "smtpState": smtpState,
       "smtpServerAddr": smtpServerAddr,
       "smtpServerPort": smtpServerPort,
       "smtpSelfMailAddr": smtpSelfMailAddr,
       "smtpRecvMailAddrTable": smtpRecvMailAddrTable,
       "smtpRecvMailAddrEntry": smtpRecvMailAddrEntry,
       "smtpRecvMailAddrIndex": smtpRecvMailAddrIndex,
       "smtpRecvMailAddr": smtpRecvMailAddr,
       "smtpRecvMailAddrStatus": smtpRecvMailAddrStatus,
       "companyLimitIp": companyLimitIp,
       "limitIpMulticastProfileTable": limitIpMulticastProfileTable,
       "limitIpMulticastProfileEntry": limitIpMulticastProfileEntry,
       "limitIpMulticastProfileID": limitIpMulticastProfileID,
       "limitIpMulticastProfileName": limitIpMulticastProfileName,
       "limitIpMulticastProfileStatus": limitIpMulticastProfileStatus,
       "limitIpMulticastEntryTable": limitIpMulticastEntryTable,
       "limitIpMulticastEntry": limitIpMulticastEntry,
       "limitIpMulticastEntryProfileID": limitIpMulticastEntryProfileID,
       "limitIpMulticaststartIpAddr": limitIpMulticaststartIpAddr,
       "limitIpMulticastendIpAddr": limitIpMulticastendIpAddr,
       "limitIpMulticastStatus": limitIpMulticastStatus,
       "limitIpMulticastPortTable": limitIpMulticastPortTable,
       "limitIpMulticastPortEntry": limitIpMulticastPortEntry,
       "limitIpMulticastPortID": limitIpMulticastPortID,
       "limitIpMulticastPortState": limitIpMulticastPortState,
       "limitIpMulticastPortProfileID": limitIpMulticastPortProfileID,
       "limitIpMulticastPortMaxGrp": limitIpMulticastPortMaxGrp,
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
       "companyMulticastFilter": companyMulticastFilter,
       "mcastFilterPortTable": mcastFilterPortTable,
       "mcastFilterPortEntry": mcastFilterPortEntry,
       "mcastFilterPortIndex": mcastFilterPortIndex,
       "mcastFilterPortType": mcastFilterPortType,
       "companyBPDUAttack": companyBPDUAttack,
       "sysBPDUAttackStateEnable": sysBPDUAttackStateEnable,
       "sysBPDUAttackRecoverTime": sysBPDUAttackRecoverTime,
       "sysBPDUAttackCtrlTable": sysBPDUAttackCtrlTable,
       "sysBPDUAttackCtrlEntry": sysBPDUAttackCtrlEntry,
       "sysBPDUAttackCtrlIndex": sysBPDUAttackCtrlIndex,
       "sysBPDUAttackPortState": sysBPDUAttackPortState,
       "sysBPDUAttackPortMode": sysBPDUAttackPortMode,
       "sysBPDUAttackPortStatus": sysBPDUAttackPortStatus,
       "sysBPDUAttackLog": sysBPDUAttackLog,
       "companyDoSCtrl": companyDoSCtrl,
       "doSTrapLog": doSTrapLog,
       "doSClearCounters": doSClearCounters,
       "doSCtrlTable": doSCtrlTable,
       "doSCtrlEntry": doSCtrlEntry,
       "doSCtrlType": doSCtrlType,
       "doSCtrlState": doSCtrlState,
       "doSCtrlActionType": doSCtrlActionType,
       "doSCtrlMirrorPort": doSCtrlMirrorPort,
       "doSCtrlMirrorPriority": doSCtrlMirrorPriority,
       "doSCtrlMirrorRxRate": doSCtrlMirrorRxRate,
       "doSCtrlFrameCount": doSCtrlFrameCount,
       "doSNotify": doSNotify,
       "doSNotifyPrefix": doSNotifyPrefix,
       "doSAttackDetected": doSAttackDetected,
       "doSNotifyVarBindings": doSNotifyVarBindings,
       "doSNotifyVarIpAddr": doSNotifyVarIpAddr,
       "doSNotifyVarPortNumber": doSNotifyVarPortNumber}
)
