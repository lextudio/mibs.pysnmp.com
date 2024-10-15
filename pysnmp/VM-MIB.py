# SNMP MIB module (VM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/VM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:12:47 2024
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

_Dell_ObjectIdentity = ObjectIdentity
dell = _Dell_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674)
)
_Server_ObjectIdentity = ObjectIdentity
server = _Server_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10890)
)
_Drac2_ObjectIdentity = ObjectIdentity
drac2 = _Drac2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5)
)
_Identification_ObjectIdentity = ObjectIdentity
identification = _Identification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 1)
)


class _IdManufacturer_Type(DisplayString):
    """Custom type idManufacturer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_IdManufacturer_Type.__name__ = "DisplayString"
_IdManufacturer_Object = MibScalar
idManufacturer = _IdManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 1, 1),
    _IdManufacturer_Type()
)
idManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    idManufacturer.setStatus("mandatory")


class _IdProduct_Type(DisplayString):
    """Custom type idProduct based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_IdProduct_Type.__name__ = "DisplayString"
_IdProduct_Object = MibScalar
idProduct = _IdProduct_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 1, 2),
    _IdProduct_Type()
)
idProduct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    idProduct.setStatus("mandatory")


class _IdAgentRevMajor_Type(Integer32):
    """Custom type idAgentRevMajor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_IdAgentRevMajor_Type.__name__ = "Integer32"
_IdAgentRevMajor_Object = MibScalar
idAgentRevMajor = _IdAgentRevMajor_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 1, 3),
    _IdAgentRevMajor_Type()
)
idAgentRevMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    idAgentRevMajor.setStatus("mandatory")


class _IdAgentRevMinor_Type(Integer32):
    """Custom type idAgentRevMinor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_IdAgentRevMinor_Type.__name__ = "Integer32"
_IdAgentRevMinor_Object = MibScalar
idAgentRevMinor = _IdAgentRevMinor_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 1, 4),
    _IdAgentRevMinor_Type()
)
idAgentRevMinor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    idAgentRevMinor.setStatus("mandatory")


class _IdMibRevMajor_Type(Integer32):
    """Custom type idMibRevMajor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_IdMibRevMajor_Type.__name__ = "Integer32"
_IdMibRevMajor_Object = MibScalar
idMibRevMajor = _IdMibRevMajor_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 1, 5),
    _IdMibRevMajor_Type()
)
idMibRevMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    idMibRevMajor.setStatus("mandatory")


class _IdMibRevMinor_Type(Integer32):
    """Custom type idMibRevMinor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_IdMibRevMinor_Type.__name__ = "Integer32"
_IdMibRevMinor_Object = MibScalar
idMibRevMinor = _IdMibRevMinor_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 1, 6),
    _IdMibRevMinor_Type()
)
idMibRevMinor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    idMibRevMinor.setStatus("mandatory")
_Module_ObjectIdentity = ObjectIdentity
module = _Module_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 2)
)
_ModNumber_Type = Gauge32
_ModNumber_Object = MibScalar
modNumber = _ModNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 2, 1),
    _ModNumber_Type()
)
modNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modNumber.setStatus("mandatory")
_ModTable_Object = MibTable
modTable = _ModTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 2, 2)
)
if mibBuilder.loadTexts:
    modTable.setStatus("mandatory")
_ModEntry_Object = MibTableRow
modEntry = _ModEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 2, 2, 1)
)
modEntry.setIndexNames(
    (0, "VM-MIB", "modIndex"),
)
if mibBuilder.loadTexts:
    modEntry.setStatus("mandatory")
_ModIndex_Type = Integer32
_ModIndex_Object = MibTableColumn
modIndex = _ModIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 2, 2, 1, 1),
    _ModIndex_Type()
)
modIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modIndex.setStatus("mandatory")
_ModFwRevMajor_Type = Integer32
_ModFwRevMajor_Object = MibTableColumn
modFwRevMajor = _ModFwRevMajor_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 2, 2, 1, 2),
    _ModFwRevMajor_Type()
)
modFwRevMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modFwRevMajor.setStatus("mandatory")
_ModFwRevMinor_Type = Integer32
_ModFwRevMinor_Object = MibTableColumn
modFwRevMinor = _ModFwRevMinor_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 2, 2, 1, 3),
    _ModFwRevMinor_Type()
)
modFwRevMinor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modFwRevMinor.setStatus("mandatory")


class _ModType_Type(Integer32):
    """Custom type modType based on Integer32"""
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
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("cdrom", 7),
          ("chassis", 4),
          ("dell-remote-assistant-card-v2-0", 1),
          ("diskDrive", 6),
          ("motherboard", 2),
          ("powerSupply", 5),
          ("processor", 3),
          ("tapeDrive", 8),
          ("unknown", 0))
    )


_ModType_Type.__name__ = "Integer32"
_ModType_Object = MibTableColumn
modType = _ModType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 2, 2, 1, 4),
    _ModType_Type()
)
modType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modType.setStatus("mandatory")


class _ModFwRelDate_Type(DisplayString):
    """Custom type modFwRelDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_ModFwRelDate_Type.__name__ = "DisplayString"
_ModFwRelDate_Object = MibTableColumn
modFwRelDate = _ModFwRelDate_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 2, 2, 1, 5),
    _ModFwRelDate_Type()
)
modFwRelDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modFwRelDate.setStatus("mandatory")


class _ModPciBridge_Type(DisplayString):
    """Custom type modPciBridge based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_ModPciBridge_Type.__name__ = "DisplayString"
_ModPciBridge_Object = MibTableColumn
modPciBridge = _ModPciBridge_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 2, 2, 1, 6),
    _ModPciBridge_Type()
)
modPciBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modPciBridge.setStatus("mandatory")


class _ModNetworkCtrl_Type(DisplayString):
    """Custom type modNetworkCtrl based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_ModNetworkCtrl_Type.__name__ = "DisplayString"
_ModNetworkCtrl_Object = MibTableColumn
modNetworkCtrl = _ModNetworkCtrl_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 2, 2, 1, 7),
    _ModNetworkCtrl_Type()
)
modNetworkCtrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modNetworkCtrl.setStatus("mandatory")


class _ModPcmciaHost_Type(DisplayString):
    """Custom type modPcmciaHost based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_ModPcmciaHost_Type.__name__ = "DisplayString"
_ModPcmciaHost_Object = MibTableColumn
modPcmciaHost = _ModPcmciaHost_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 2, 2, 1, 8),
    _ModPcmciaHost_Type()
)
modPcmciaHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modPcmciaHost.setStatus("mandatory")


class _ModPcCardMfgr_Type(DisplayString):
    """Custom type modPcCardMfgr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_ModPcCardMfgr_Type.__name__ = "DisplayString"
_ModPcCardMfgr_Object = MibTableColumn
modPcCardMfgr = _ModPcCardMfgr_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 2, 2, 1, 9),
    _ModPcCardMfgr_Type()
)
modPcCardMfgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modPcCardMfgr.setStatus("mandatory")


class _ModPcCardName_Type(DisplayString):
    """Custom type modPcCardName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_ModPcCardName_Type.__name__ = "DisplayString"
_ModPcCardName_Object = MibTableColumn
modPcCardName = _ModPcCardName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 2, 2, 1, 10),
    _ModPcCardName_Type()
)
modPcCardName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modPcCardName.setStatus("mandatory")


class _ModBattery_Type(DisplayString):
    """Custom type modBattery based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ModBattery_Type.__name__ = "DisplayString"
_ModBattery_Object = MibTableColumn
modBattery = _ModBattery_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 2, 2, 1, 11),
    _ModBattery_Type()
)
modBattery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modBattery.setStatus("mandatory")
_ModVoltCount_Type = Integer32
_ModVoltCount_Object = MibTableColumn
modVoltCount = _ModVoltCount_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 2, 2, 1, 12),
    _ModVoltCount_Type()
)
modVoltCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modVoltCount.setStatus("mandatory")
_ModTempCount_Type = Integer32
_ModTempCount_Object = MibTableColumn
modTempCount = _ModTempCount_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 2, 2, 1, 13),
    _ModTempCount_Type()
)
modTempCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modTempCount.setStatus("mandatory")
_ModFanCount_Type = Integer32
_ModFanCount_Object = MibTableColumn
modFanCount = _ModFanCount_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 2, 2, 1, 14),
    _ModFanCount_Type()
)
modFanCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modFanCount.setStatus("mandatory")
_ModSwitchCount_Type = Integer32
_ModSwitchCount_Object = MibTableColumn
modSwitchCount = _ModSwitchCount_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 2, 2, 1, 15),
    _ModSwitchCount_Type()
)
modSwitchCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modSwitchCount.setStatus("mandatory")
_ModFaultCount_Type = Integer32
_ModFaultCount_Object = MibTableColumn
modFaultCount = _ModFaultCount_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 2, 2, 1, 16),
    _ModFaultCount_Type()
)
modFaultCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modFaultCount.setStatus("mandatory")
_ModUpTime_Type = TimeTicks
_ModUpTime_Object = MibTableColumn
modUpTime = _ModUpTime_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 2, 2, 1, 17),
    _ModUpTime_Type()
)
modUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modUpTime.setStatus("mandatory")
_ModStartDelay_Type = Integer32
_ModStartDelay_Object = MibTableColumn
modStartDelay = _ModStartDelay_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 2, 2, 1, 18),
    _ModStartDelay_Type()
)
modStartDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modStartDelay.setStatus("mandatory")
_ModRecoveryTimeout_Type = Integer32
_ModRecoveryTimeout_Object = MibTableColumn
modRecoveryTimeout = _ModRecoveryTimeout_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 2, 2, 1, 19),
    _ModRecoveryTimeout_Type()
)
modRecoveryTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modRecoveryTimeout.setStatus("mandatory")


class _ModAutoRecoveryEnable_Type(Integer32):
    """Custom type modAutoRecoveryEnable based on Integer32"""
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


_ModAutoRecoveryEnable_Type.__name__ = "Integer32"
_ModAutoRecoveryEnable_Object = MibTableColumn
modAutoRecoveryEnable = _ModAutoRecoveryEnable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 2, 2, 1, 20),
    _ModAutoRecoveryEnable_Type()
)
modAutoRecoveryEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modAutoRecoveryEnable.setStatus("mandatory")


class _ModHeartBeatEnable_Type(Integer32):
    """Custom type modHeartBeatEnable based on Integer32"""
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


_ModHeartBeatEnable_Type.__name__ = "Integer32"
_ModHeartBeatEnable_Object = MibScalar
modHeartBeatEnable = _ModHeartBeatEnable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 2, 2, 1, 21),
    _ModHeartBeatEnable_Type()
)
modHeartBeatEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modHeartBeatEnable.setStatus("mandatory")


class _ModAccessControl_Type(DisplayString):
    """Custom type modAccessControl based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ModAccessControl_Type.__name__ = "DisplayString"
_ModAccessControl_Object = MibTableColumn
modAccessControl = _ModAccessControl_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 2, 2, 1, 22),
    _ModAccessControl_Type()
)
modAccessControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modAccessControl.setStatus("mandatory")


class _ModEthernetAddress_Type(DisplayString):
    """Custom type modEthernetAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_ModEthernetAddress_Type.__name__ = "DisplayString"
_ModEthernetAddress_Object = MibTableColumn
modEthernetAddress = _ModEthernetAddress_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 2, 2, 1, 23),
    _ModEthernetAddress_Type()
)
modEthernetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modEthernetAddress.setStatus("mandatory")
_ConfigAdmin_ObjectIdentity = ObjectIdentity
configAdmin = _ConfigAdmin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 3)
)
_CfgAdminNumber_Type = Gauge32
_CfgAdminNumber_Object = MibScalar
cfgAdminNumber = _CfgAdminNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 3, 1),
    _CfgAdminNumber_Type()
)
cfgAdminNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgAdminNumber.setStatus("mandatory")
_CfgAdminTable_Object = MibTable
cfgAdminTable = _CfgAdminTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 3, 2)
)
if mibBuilder.loadTexts:
    cfgAdminTable.setStatus("mandatory")
_CfgAdminEntry_Object = MibTableRow
cfgAdminEntry = _CfgAdminEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 3, 2, 1)
)
cfgAdminEntry.setIndexNames(
    (0, "VM-MIB", "cfgAdminModIndex"),
    (0, "VM-MIB", "cfgAdminIndex"),
)
if mibBuilder.loadTexts:
    cfgAdminEntry.setStatus("mandatory")
_CfgAdminModIndex_Type = Integer32
_CfgAdminModIndex_Object = MibTableColumn
cfgAdminModIndex = _CfgAdminModIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 3, 2, 1, 1),
    _CfgAdminModIndex_Type()
)
cfgAdminModIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgAdminModIndex.setStatus("mandatory")
_CfgAdminIndex_Type = Integer32
_CfgAdminIndex_Object = MibTableColumn
cfgAdminIndex = _CfgAdminIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 3, 2, 1, 2),
    _CfgAdminIndex_Type()
)
cfgAdminIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgAdminIndex.setStatus("mandatory")


class _CfgAdminAlias_Type(DisplayString):
    """Custom type cfgAdminAlias based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_CfgAdminAlias_Type.__name__ = "DisplayString"
_CfgAdminAlias_Object = MibTableColumn
cfgAdminAlias = _CfgAdminAlias_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 3, 2, 1, 3),
    _CfgAdminAlias_Type()
)
cfgAdminAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgAdminAlias.setStatus("mandatory")


class _CfgAdminPassword_Type(DisplayString):
    """Custom type cfgAdminPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_CfgAdminPassword_Type.__name__ = "DisplayString"
_CfgAdminPassword_Object = MibTableColumn
cfgAdminPassword = _CfgAdminPassword_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 3, 2, 1, 4),
    _CfgAdminPassword_Type()
)
cfgAdminPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgAdminPassword.setStatus("mandatory")


class _CfgAdminSessionCallback_Type(DisplayString):
    """Custom type cfgAdminSessionCallback based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_CfgAdminSessionCallback_Type.__name__ = "DisplayString"
_CfgAdminSessionCallback_Object = MibTableColumn
cfgAdminSessionCallback = _CfgAdminSessionCallback_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 3, 2, 1, 5),
    _CfgAdminSessionCallback_Type()
)
cfgAdminSessionCallback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgAdminSessionCallback.setStatus("mandatory")


class _CfgAdminPagerNumber_Type(DisplayString):
    """Custom type cfgAdminPagerNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_CfgAdminPagerNumber_Type.__name__ = "DisplayString"
_CfgAdminPagerNumber_Object = MibTableColumn
cfgAdminPagerNumber = _CfgAdminPagerNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 3, 2, 1, 6),
    _CfgAdminPagerNumber_Type()
)
cfgAdminPagerNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgAdminPagerNumber.setStatus("mandatory")


class _CfgAdminPagerSubscriber_Type(DisplayString):
    """Custom type cfgAdminPagerSubscriber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_CfgAdminPagerSubscriber_Type.__name__ = "DisplayString"
_CfgAdminPagerSubscriber_Object = MibTableColumn
cfgAdminPagerSubscriber = _CfgAdminPagerSubscriber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 3, 2, 1, 7),
    _CfgAdminPagerSubscriber_Type()
)
cfgAdminPagerSubscriber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgAdminPagerSubscriber.setStatus("mandatory")


class _CfgAdminPagerType_Type(Integer32):
    """Custom type cfgAdminPagerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alphanumeric", 2),
          ("none", 0),
          ("numeric", 1))
    )


_CfgAdminPagerType_Type.__name__ = "Integer32"
_CfgAdminPagerType_Object = MibTableColumn
cfgAdminPagerType = _CfgAdminPagerType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 3, 2, 1, 8),
    _CfgAdminPagerType_Type()
)
cfgAdminPagerType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgAdminPagerType.setStatus("mandatory")
_CfgAdminPagerMask_Type = Integer32
_CfgAdminPagerMask_Object = MibTableColumn
cfgAdminPagerMask = _CfgAdminPagerMask_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 3, 2, 1, 9),
    _CfgAdminPagerMask_Type()
)
cfgAdminPagerMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgAdminPagerMask.setStatus("mandatory")


class _CfgAdminCustomPagerCode_Type(DisplayString):
    """Custom type cfgAdminCustomPagerCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_CfgAdminCustomPagerCode_Type.__name__ = "DisplayString"
_CfgAdminCustomPagerCode_Object = MibTableColumn
cfgAdminCustomPagerCode = _CfgAdminCustomPagerCode_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 3, 2, 1, 10),
    _CfgAdminCustomPagerCode_Type()
)
cfgAdminCustomPagerCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgAdminCustomPagerCode.setStatus("mandatory")
_CfgAdminTestPager_Type = Integer32
_CfgAdminTestPager_Object = MibTableColumn
cfgAdminTestPager = _CfgAdminTestPager_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 3, 2, 1, 11),
    _CfgAdminTestPager_Type()
)
cfgAdminTestPager.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgAdminTestPager.setStatus("mandatory")
_ConfigAlert_ObjectIdentity = ObjectIdentity
configAlert = _ConfigAlert_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 4)
)
_CfgAlertNumber_Type = Gauge32
_CfgAlertNumber_Object = MibScalar
cfgAlertNumber = _CfgAlertNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 4, 1),
    _CfgAlertNumber_Type()
)
cfgAlertNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgAlertNumber.setStatus("mandatory")
_CfgAlertTable_Object = MibTable
cfgAlertTable = _CfgAlertTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 4, 2)
)
if mibBuilder.loadTexts:
    cfgAlertTable.setStatus("mandatory")
_CfgAlertEntry_Object = MibTableRow
cfgAlertEntry = _CfgAlertEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 4, 2, 1)
)
cfgAlertEntry.setIndexNames(
    (0, "VM-MIB", "cfgAlertModIndex"),
    (0, "VM-MIB", "cfgAlertIndex"),
)
if mibBuilder.loadTexts:
    cfgAlertEntry.setStatus("mandatory")
_CfgAlertModIndex_Type = Integer32
_CfgAlertModIndex_Object = MibTableColumn
cfgAlertModIndex = _CfgAlertModIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 4, 2, 1, 1),
    _CfgAlertModIndex_Type()
)
cfgAlertModIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgAlertModIndex.setStatus("mandatory")
_CfgAlertIndex_Type = Integer32
_CfgAlertIndex_Object = MibTableColumn
cfgAlertIndex = _CfgAlertIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 4, 2, 1, 2),
    _CfgAlertIndex_Type()
)
cfgAlertIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgAlertIndex.setStatus("mandatory")


class _CfgAlertTrapSendIPAddress_Type(DisplayString):
    """Custom type cfgAlertTrapSendIPAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CfgAlertTrapSendIPAddress_Type.__name__ = "DisplayString"
_CfgAlertTrapSendIPAddress_Object = MibTableColumn
cfgAlertTrapSendIPAddress = _CfgAlertTrapSendIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 4, 2, 1, 3),
    _CfgAlertTrapSendIPAddress_Type()
)
cfgAlertTrapSendIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgAlertTrapSendIPAddress.setStatus("mandatory")


class _CfgAlertTrapSendCommunity_Type(DisplayString):
    """Custom type cfgAlertTrapSendCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_CfgAlertTrapSendCommunity_Type.__name__ = "DisplayString"
_CfgAlertTrapSendCommunity_Object = MibTableColumn
cfgAlertTrapSendCommunity = _CfgAlertTrapSendCommunity_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 4, 2, 1, 4),
    _CfgAlertTrapSendCommunity_Type()
)
cfgAlertTrapSendCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgAlertTrapSendCommunity.setStatus("mandatory")


class _CfgAlertTrapCallBackNumber_Type(DisplayString):
    """Custom type cfgAlertTrapCallBackNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_CfgAlertTrapCallBackNumber_Type.__name__ = "DisplayString"
_CfgAlertTrapCallBackNumber_Object = MibScalar
cfgAlertTrapCallBackNumber = _CfgAlertTrapCallBackNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 4, 2, 1, 5),
    _CfgAlertTrapCallBackNumber_Type()
)
cfgAlertTrapCallBackNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgAlertTrapCallBackNumber.setStatus("mandatory")
_ConfigNetwork_ObjectIdentity = ObjectIdentity
configNetwork = _ConfigNetwork_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 5)
)
_CfgNetNumber_Type = Gauge32
_CfgNetNumber_Object = MibScalar
cfgNetNumber = _CfgNetNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 5, 1),
    _CfgNetNumber_Type()
)
cfgNetNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgNetNumber.setStatus("mandatory")
_CfgNetTable_Object = MibTable
cfgNetTable = _CfgNetTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 5, 2)
)
if mibBuilder.loadTexts:
    cfgNetTable.setStatus("mandatory")
_CfgNetEntry_Object = MibTableRow
cfgNetEntry = _CfgNetEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 5, 2, 1)
)
cfgNetEntry.setIndexNames(
    (0, "VM-MIB", "cfgNetModIndex"),
    (0, "VM-MIB", "cfgNetIndex"),
)
if mibBuilder.loadTexts:
    cfgNetEntry.setStatus("mandatory")
_CfgNetModIndex_Type = Integer32
_CfgNetModIndex_Object = MibTableColumn
cfgNetModIndex = _CfgNetModIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 5, 2, 1, 1),
    _CfgNetModIndex_Type()
)
cfgNetModIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgNetModIndex.setStatus("mandatory")
_CfgNetIndex_Type = Integer32
_CfgNetIndex_Object = MibTableColumn
cfgNetIndex = _CfgNetIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 5, 2, 1, 2),
    _CfgNetIndex_Type()
)
cfgNetIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgNetIndex.setStatus("mandatory")


class _CfgNetIPAddress_Type(DisplayString):
    """Custom type cfgNetIPAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CfgNetIPAddress_Type.__name__ = "DisplayString"
_CfgNetIPAddress_Object = MibTableColumn
cfgNetIPAddress = _CfgNetIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 5, 2, 1, 3),
    _CfgNetIPAddress_Type()
)
cfgNetIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgNetIPAddress.setStatus("mandatory")


class _CfgNetSubnetMask_Type(DisplayString):
    """Custom type cfgNetSubnetMask based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CfgNetSubnetMask_Type.__name__ = "DisplayString"
_CfgNetSubnetMask_Object = MibTableColumn
cfgNetSubnetMask = _CfgNetSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 5, 2, 1, 4),
    _CfgNetSubnetMask_Type()
)
cfgNetSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgNetSubnetMask.setStatus("mandatory")


class _CfgNetGateway_Type(DisplayString):
    """Custom type cfgNetGateway based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CfgNetGateway_Type.__name__ = "DisplayString"
_CfgNetGateway_Object = MibTableColumn
cfgNetGateway = _CfgNetGateway_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 5, 2, 1, 5),
    _CfgNetGateway_Type()
)
cfgNetGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgNetGateway.setStatus("mandatory")
_ConfigModem_ObjectIdentity = ObjectIdentity
configModem = _ConfigModem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 6)
)
_CfgModemNumber_Type = Gauge32
_CfgModemNumber_Object = MibScalar
cfgModemNumber = _CfgModemNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 6, 1),
    _CfgModemNumber_Type()
)
cfgModemNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgModemNumber.setStatus("mandatory")
_CfgModemTable_Object = MibTable
cfgModemTable = _CfgModemTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 6, 2)
)
if mibBuilder.loadTexts:
    cfgModemTable.setStatus("mandatory")
_CfgModemEntry_Object = MibTableRow
cfgModemEntry = _CfgModemEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 6, 2, 1)
)
cfgModemEntry.setIndexNames(
    (0, "VM-MIB", "cfgModemModIndex"),
    (0, "VM-MIB", "cfgModemIndex"),
)
if mibBuilder.loadTexts:
    cfgModemEntry.setStatus("mandatory")
_CfgModemModIndex_Type = Integer32
_CfgModemModIndex_Object = MibTableColumn
cfgModemModIndex = _CfgModemModIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 6, 2, 1, 1),
    _CfgModemModIndex_Type()
)
cfgModemModIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgModemModIndex.setStatus("mandatory")
_CfgModemIndex_Type = Integer32
_CfgModemIndex_Object = MibTableColumn
cfgModemIndex = _CfgModemIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 6, 2, 1, 2),
    _CfgModemIndex_Type()
)
cfgModemIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgModemIndex.setStatus("mandatory")
_CfgModemBaudRate_Type = Integer32
_CfgModemBaudRate_Object = MibTableColumn
cfgModemBaudRate = _CfgModemBaudRate_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 6, 2, 1, 3),
    _CfgModemBaudRate_Type()
)
cfgModemBaudRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgModemBaudRate.setStatus("mandatory")
_CfgModemDialMode_Type = Integer32
_CfgModemDialMode_Object = MibTableColumn
cfgModemDialMode = _CfgModemDialMode_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 6, 2, 1, 4),
    _CfgModemDialMode_Type()
)
cfgModemDialMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgModemDialMode.setStatus("mandatory")


class _CfgModemExtraInitString_Type(DisplayString):
    """Custom type cfgModemExtraInitString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 79),
    )


_CfgModemExtraInitString_Type.__name__ = "DisplayString"
_CfgModemExtraInitString_Object = MibTableColumn
cfgModemExtraInitString = _CfgModemExtraInitString_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 6, 2, 1, 5),
    _CfgModemExtraInitString_Type()
)
cfgModemExtraInitString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgModemExtraInitString.setStatus("mandatory")
_CfgModemPwrOnDelay_Type = Integer32
_CfgModemPwrOnDelay_Object = MibTableColumn
cfgModemPwrOnDelay = _CfgModemPwrOnDelay_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 6, 2, 1, 6),
    _CfgModemPwrOnDelay_Type()
)
cfgModemPwrOnDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgModemPwrOnDelay.setStatus("mandatory")
_CfgModemSignalDelay_Type = Integer32
_CfgModemSignalDelay_Object = MibTableColumn
cfgModemSignalDelay = _CfgModemSignalDelay_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 6, 2, 1, 7),
    _CfgModemSignalDelay_Type()
)
cfgModemSignalDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgModemSignalDelay.setStatus("mandatory")
_CfgModemRingDelay_Type = Integer32
_CfgModemRingDelay_Object = MibTableColumn
cfgModemRingDelay = _CfgModemRingDelay_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 6, 2, 1, 8),
    _CfgModemRingDelay_Type()
)
cfgModemRingDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgModemRingDelay.setStatus("mandatory")
_CfgModemCDDelay_Type = Integer32
_CfgModemCDDelay_Object = MibTableColumn
cfgModemCDDelay = _CfgModemCDDelay_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 6, 2, 1, 9),
    _CfgModemCDDelay_Type()
)
cfgModemCDDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgModemCDDelay.setStatus("mandatory")
_CfgModemResponseDelay_Type = Integer32
_CfgModemResponseDelay_Object = MibTableColumn
cfgModemResponseDelay = _CfgModemResponseDelay_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 6, 2, 1, 10),
    _CfgModemResponseDelay_Type()
)
cfgModemResponseDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgModemResponseDelay.setStatus("mandatory")
_CfgModemHangUpDelay_Type = Integer32
_CfgModemHangUpDelay_Object = MibTableColumn
cfgModemHangUpDelay = _CfgModemHangUpDelay_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 6, 2, 1, 11),
    _CfgModemHangUpDelay_Type()
)
cfgModemHangUpDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgModemHangUpDelay.setStatus("mandatory")
_CfgModemConnectTimeout_Type = Integer32
_CfgModemConnectTimeout_Object = MibTableColumn
cfgModemConnectTimeout = _CfgModemConnectTimeout_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 6, 2, 1, 12),
    _CfgModemConnectTimeout_Type()
)
cfgModemConnectTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgModemConnectTimeout.setStatus("mandatory")
_CfgModemDetectTimeout_Type = Integer32
_CfgModemDetectTimeout_Object = MibTableColumn
cfgModemDetectTimeout = _CfgModemDetectTimeout_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 6, 2, 1, 13),
    _CfgModemDetectTimeout_Type()
)
cfgModemDetectTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgModemDetectTimeout.setStatus("mandatory")
_Control_ObjectIdentity = ObjectIdentity
control = _Control_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 7)
)
_CtlNumber_Type = Gauge32
_CtlNumber_Object = MibScalar
ctlNumber = _CtlNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 7, 1),
    _CtlNumber_Type()
)
ctlNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlNumber.setStatus("mandatory")
_CtlTable_Object = MibTable
ctlTable = _CtlTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 7, 2)
)
if mibBuilder.loadTexts:
    ctlTable.setStatus("mandatory")
_CtlEntry_Object = MibTableRow
ctlEntry = _CtlEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 7, 2, 1)
)
ctlEntry.setIndexNames(
    (0, "VM-MIB", "ctlModIndex"),
    (0, "VM-MIB", "ctlIndex"),
)
if mibBuilder.loadTexts:
    ctlEntry.setStatus("mandatory")
_CtlModIndex_Type = Integer32
_CtlModIndex_Object = MibTableColumn
ctlModIndex = _CtlModIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 7, 2, 1, 1),
    _CtlModIndex_Type()
)
ctlModIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlModIndex.setStatus("mandatory")
_CtlIndex_Type = Integer32
_CtlIndex_Object = MibTableColumn
ctlIndex = _CtlIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 7, 2, 1, 2),
    _CtlIndex_Type()
)
ctlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlIndex.setStatus("mandatory")
_CtlSystemReset_Type = Integer32
_CtlSystemReset_Object = MibTableColumn
ctlSystemReset = _CtlSystemReset_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 7, 2, 1, 3),
    _CtlSystemReset_Type()
)
ctlSystemReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlSystemReset.setStatus("current")
_CtlSystemShutdown_Type = Integer32
_CtlSystemShutdown_Object = MibTableColumn
ctlSystemShutdown = _CtlSystemShutdown_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 7, 2, 1, 4),
    _CtlSystemShutdown_Type()
)
ctlSystemShutdown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlSystemShutdown.setStatus("current")
_CtlSystemPwrCycle_Type = Integer32
_CtlSystemPwrCycle_Object = MibTableColumn
ctlSystemPwrCycle = _CtlSystemPwrCycle_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 7, 2, 1, 5),
    _CtlSystemPwrCycle_Type()
)
ctlSystemPwrCycle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlSystemPwrCycle.setStatus("current")
_CtlCardShutdown_Type = Integer32
_CtlCardShutdown_Object = MibTableColumn
ctlCardShutdown = _CtlCardShutdown_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 7, 2, 1, 6),
    _CtlCardShutdown_Type()
)
ctlCardShutdown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlCardShutdown.setStatus("current")
_CtlCardSoftReset_Type = Integer32
_CtlCardSoftReset_Object = MibTableColumn
ctlCardSoftReset = _CtlCardSoftReset_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 7, 2, 1, 7),
    _CtlCardSoftReset_Type()
)
ctlCardSoftReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlCardSoftReset.setStatus("current")
_CtlCardHardReset_Type = Integer32
_CtlCardHardReset_Object = MibTableColumn
ctlCardHardReset = _CtlCardHardReset_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 7, 2, 1, 8),
    _CtlCardHardReset_Type()
)
ctlCardHardReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlCardHardReset.setStatus("current")
_CtlCardFlushGPNV_Type = Integer32
_CtlCardFlushGPNV_Object = MibScalar
ctlCardFlushGPNV = _CtlCardFlushGPNV_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 7, 2, 1, 9),
    _CtlCardFlushGPNV_Type()
)
ctlCardFlushGPNV.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlCardFlushGPNV.setStatus("current")
_Voltage_ObjectIdentity = ObjectIdentity
voltage = _Voltage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 20)
)
_VoltNumber_Type = Gauge32
_VoltNumber_Object = MibScalar
voltNumber = _VoltNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 20, 1),
    _VoltNumber_Type()
)
voltNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltNumber.setStatus("mandatory")
_VoltTable_Object = MibTable
voltTable = _VoltTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 20, 2)
)
if mibBuilder.loadTexts:
    voltTable.setStatus("mandatory")
_VoltEntry_Object = MibTableRow
voltEntry = _VoltEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 20, 2, 1)
)
voltEntry.setIndexNames(
    (0, "VM-MIB", "voltModIndex"),
    (0, "VM-MIB", "voltIndex"),
)
if mibBuilder.loadTexts:
    voltEntry.setStatus("mandatory")
_VoltModIndex_Type = Integer32
_VoltModIndex_Object = MibTableColumn
voltModIndex = _VoltModIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 20, 2, 1, 1),
    _VoltModIndex_Type()
)
voltModIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltModIndex.setStatus("mandatory")
_VoltIndex_Type = Integer32
_VoltIndex_Object = MibTableColumn
voltIndex = _VoltIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 20, 2, 1, 2),
    _VoltIndex_Type()
)
voltIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltIndex.setStatus("mandatory")


class _VoltType_Type(Integer32):
    """Custom type voltType based on Integer32"""
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
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("minus12", 6),
          ("minus15", 8),
          ("minus5", 4),
          ("pciVolt", 1),
          ("plus12", 5),
          ("plus15", 7),
          ("plus3", 2),
          ("plus5", 3),
          ("wallAdapter", 0))
    )


_VoltType_Type.__name__ = "Integer32"
_VoltType_Object = MibTableColumn
voltType = _VoltType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 20, 2, 1, 3),
    _VoltType_Type()
)
voltType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltType.setStatus("mandatory")


class _VoltDescr_Type(DisplayString):
    """Custom type voltDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_VoltDescr_Type.__name__ = "DisplayString"
_VoltDescr_Object = MibTableColumn
voltDescr = _VoltDescr_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 20, 2, 1, 4),
    _VoltDescr_Type()
)
voltDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltDescr.setStatus("mandatory")


class _VoltReading_Type(DisplayString):
    """Custom type voltReading based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_VoltReading_Type.__name__ = "DisplayString"
_VoltReading_Object = MibTableColumn
voltReading = _VoltReading_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 20, 2, 1, 5),
    _VoltReading_Type()
)
voltReading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltReading.setStatus("mandatory")
if mibBuilder.loadTexts:
    voltReading.setUnits("Volts")


class _VoltLimitLowCritical_Type(DisplayString):
    """Custom type voltLimitLowCritical based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_VoltLimitLowCritical_Type.__name__ = "DisplayString"
_VoltLimitLowCritical_Object = MibTableColumn
voltLimitLowCritical = _VoltLimitLowCritical_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 20, 2, 1, 6),
    _VoltLimitLowCritical_Type()
)
voltLimitLowCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voltLimitLowCritical.setStatus("mandatory")
if mibBuilder.loadTexts:
    voltLimitLowCritical.setUnits("Volts")


class _VoltLimitHighCritical_Type(DisplayString):
    """Custom type voltLimitHighCritical based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_VoltLimitHighCritical_Type.__name__ = "DisplayString"
_VoltLimitHighCritical_Object = MibTableColumn
voltLimitHighCritical = _VoltLimitHighCritical_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 20, 2, 1, 7),
    _VoltLimitHighCritical_Type()
)
voltLimitHighCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voltLimitHighCritical.setStatus("mandatory")
if mibBuilder.loadTexts:
    voltLimitHighCritical.setUnits("Volts")


class _VoltLimitLowWarning_Type(DisplayString):
    """Custom type voltLimitLowWarning based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_VoltLimitLowWarning_Type.__name__ = "DisplayString"
_VoltLimitLowWarning_Object = MibTableColumn
voltLimitLowWarning = _VoltLimitLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 20, 2, 1, 8),
    _VoltLimitLowWarning_Type()
)
voltLimitLowWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voltLimitLowWarning.setStatus("mandatory")
if mibBuilder.loadTexts:
    voltLimitLowWarning.setUnits("Volts")


class _VoltLimitHighWarning_Type(DisplayString):
    """Custom type voltLimitHighWarning based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_VoltLimitHighWarning_Type.__name__ = "DisplayString"
_VoltLimitHighWarning_Object = MibTableColumn
voltLimitHighWarning = _VoltLimitHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 20, 2, 1, 9),
    _VoltLimitHighWarning_Type()
)
voltLimitHighWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voltLimitHighWarning.setStatus("mandatory")
if mibBuilder.loadTexts:
    voltLimitHighWarning.setUnits("Volts")


class _VoltItemStatus_Type(Integer32):
    """Custom type voltItemStatus based on Integer32"""
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
        *(("critical", 5),
          ("non-recoverable", 6),
          ("ok", 3),
          ("other", 1),
          ("undetermined", 0),
          ("unknown", 2),
          ("warning", 4))
    )


_VoltItemStatus_Type.__name__ = "Integer32"
_VoltItemStatus_Object = MibTableColumn
voltItemStatus = _VoltItemStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 20, 2, 1, 10),
    _VoltItemStatus_Type()
)
voltItemStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltItemStatus.setStatus("mandatory")
_VoltLastAlarm_Type = TimeTicks
_VoltLastAlarm_Object = MibTableColumn
voltLastAlarm = _VoltLastAlarm_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 20, 2, 1, 11),
    _VoltLastAlarm_Type()
)
voltLastAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltLastAlarm.setStatus("mandatory")
_VoltTrapSystem_Type = OctetString
_VoltTrapSystem_Object = MibTableColumn
voltTrapSystem = _VoltTrapSystem_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 20, 2, 1, 12),
    _VoltTrapSystem_Type()
)
voltTrapSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltTrapSystem.setStatus("mandatory")
_VoltTrapGroup_Type = OctetString
_VoltTrapGroup_Object = MibTableColumn
voltTrapGroup = _VoltTrapGroup_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 20, 2, 1, 13),
    _VoltTrapGroup_Type()
)
voltTrapGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltTrapGroup.setStatus("mandatory")
_VoltTrapMessage_Type = OctetString
_VoltTrapMessage_Object = MibTableColumn
voltTrapMessage = _VoltTrapMessage_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 20, 2, 1, 14),
    _VoltTrapMessage_Type()
)
voltTrapMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltTrapMessage.setStatus("mandatory")
_Temperature_ObjectIdentity = ObjectIdentity
temperature = _Temperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 21)
)
_TempNumber_Type = Gauge32
_TempNumber_Object = MibScalar
tempNumber = _TempNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 21, 1),
    _TempNumber_Type()
)
tempNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempNumber.setStatus("mandatory")
_TempTable_Object = MibTable
tempTable = _TempTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 21, 2)
)
if mibBuilder.loadTexts:
    tempTable.setStatus("mandatory")
_TempEntry_Object = MibTableRow
tempEntry = _TempEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 21, 2, 1)
)
tempEntry.setIndexNames(
    (0, "VM-MIB", "tempModIndex"),
    (0, "VM-MIB", "tempIndex"),
)
if mibBuilder.loadTexts:
    tempEntry.setStatus("mandatory")
_TempModIndex_Type = Integer32
_TempModIndex_Object = MibTableColumn
tempModIndex = _TempModIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 21, 2, 1, 1),
    _TempModIndex_Type()
)
tempModIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempModIndex.setStatus("mandatory")
_TempIndex_Type = Integer32
_TempIndex_Object = MibTableColumn
tempIndex = _TempIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 21, 2, 1, 2),
    _TempIndex_Type()
)
tempIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempIndex.setStatus("mandatory")


class _TempType_Type(Integer32):
    """Custom type tempType based on Integer32"""
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
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("ambient", 0),
          ("zone1", 1),
          ("zone2", 2),
          ("zone3", 3),
          ("zone4", 4),
          ("zone5", 5),
          ("zone6", 6),
          ("zone7", 7),
          ("zone8", 8))
    )


_TempType_Type.__name__ = "Integer32"
_TempType_Object = MibTableColumn
tempType = _TempType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 21, 2, 1, 3),
    _TempType_Type()
)
tempType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempType.setStatus("mandatory")


class _TempDescr_Type(DisplayString):
    """Custom type tempDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_TempDescr_Type.__name__ = "DisplayString"
_TempDescr_Object = MibTableColumn
tempDescr = _TempDescr_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 21, 2, 1, 4),
    _TempDescr_Type()
)
tempDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempDescr.setStatus("mandatory")


class _TempReading_Type(DisplayString):
    """Custom type tempReading based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_TempReading_Type.__name__ = "DisplayString"
_TempReading_Object = MibTableColumn
tempReading = _TempReading_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 21, 2, 1, 5),
    _TempReading_Type()
)
tempReading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempReading.setStatus("mandatory")
if mibBuilder.loadTexts:
    tempReading.setUnits("Degrees Celcius")


class _TempLowCritical_Type(DisplayString):
    """Custom type tempLowCritical based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_TempLowCritical_Type.__name__ = "DisplayString"
_TempLowCritical_Object = MibTableColumn
tempLowCritical = _TempLowCritical_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 21, 2, 1, 6),
    _TempLowCritical_Type()
)
tempLowCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tempLowCritical.setStatus("mandatory")
if mibBuilder.loadTexts:
    tempLowCritical.setUnits("Degrees Celcius")


class _TempHighCritical_Type(DisplayString):
    """Custom type tempHighCritical based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_TempHighCritical_Type.__name__ = "DisplayString"
_TempHighCritical_Object = MibTableColumn
tempHighCritical = _TempHighCritical_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 21, 2, 1, 7),
    _TempHighCritical_Type()
)
tempHighCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tempHighCritical.setStatus("mandatory")
if mibBuilder.loadTexts:
    tempHighCritical.setUnits("Degrees Celcius")


class _TempLowWarning_Type(DisplayString):
    """Custom type tempLowWarning based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_TempLowWarning_Type.__name__ = "DisplayString"
_TempLowWarning_Object = MibTableColumn
tempLowWarning = _TempLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 21, 2, 1, 8),
    _TempLowWarning_Type()
)
tempLowWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tempLowWarning.setStatus("mandatory")
if mibBuilder.loadTexts:
    tempLowWarning.setUnits("Degrees Celcius")


class _TempHighWarning_Type(DisplayString):
    """Custom type tempHighWarning based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_TempHighWarning_Type.__name__ = "DisplayString"
_TempHighWarning_Object = MibTableColumn
tempHighWarning = _TempHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 21, 2, 1, 9),
    _TempHighWarning_Type()
)
tempHighWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tempHighWarning.setStatus("mandatory")
if mibBuilder.loadTexts:
    tempHighWarning.setUnits("Degrees Celcius")


class _TempItemStatus_Type(Integer32):
    """Custom type tempItemStatus based on Integer32"""
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
        *(("critical", 5),
          ("non-recoverable", 6),
          ("ok", 3),
          ("other", 1),
          ("undetermined", 0),
          ("unknown", 2),
          ("warning", 4))
    )


_TempItemStatus_Type.__name__ = "Integer32"
_TempItemStatus_Object = MibTableColumn
tempItemStatus = _TempItemStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 21, 2, 1, 10),
    _TempItemStatus_Type()
)
tempItemStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempItemStatus.setStatus("mandatory")
_TempLastAlarm_Type = TimeTicks
_TempLastAlarm_Object = MibTableColumn
tempLastAlarm = _TempLastAlarm_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 21, 2, 1, 11),
    _TempLastAlarm_Type()
)
tempLastAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempLastAlarm.setStatus("mandatory")
_TempTrapSystem_Type = OctetString
_TempTrapSystem_Object = MibTableColumn
tempTrapSystem = _TempTrapSystem_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 21, 2, 1, 12),
    _TempTrapSystem_Type()
)
tempTrapSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempTrapSystem.setStatus("mandatory")
_TempTrapGroup_Type = OctetString
_TempTrapGroup_Object = MibTableColumn
tempTrapGroup = _TempTrapGroup_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 21, 2, 1, 13),
    _TempTrapGroup_Type()
)
tempTrapGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempTrapGroup.setStatus("mandatory")
_TempTrapMessage_Type = OctetString
_TempTrapMessage_Object = MibTableColumn
tempTrapMessage = _TempTrapMessage_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 21, 2, 1, 14),
    _TempTrapMessage_Type()
)
tempTrapMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempTrapMessage.setStatus("mandatory")
_Battery_ObjectIdentity = ObjectIdentity
battery = _Battery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 25)
)
_BatteryNumber_Type = Gauge32
_BatteryNumber_Object = MibScalar
batteryNumber = _BatteryNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 25, 1),
    _BatteryNumber_Type()
)
batteryNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryNumber.setStatus("mandatory")
_BatteryTable_Object = MibTable
batteryTable = _BatteryTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 25, 2)
)
if mibBuilder.loadTexts:
    batteryTable.setStatus("mandatory")
_BatteryEntry_Object = MibTableRow
batteryEntry = _BatteryEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 25, 2, 1)
)
batteryEntry.setIndexNames(
    (0, "VM-MIB", "batteryModIndex"),
    (0, "VM-MIB", "batteryIndex"),
)
if mibBuilder.loadTexts:
    batteryEntry.setStatus("mandatory")
_BatteryModIndex_Type = Integer32
_BatteryModIndex_Object = MibTableColumn
batteryModIndex = _BatteryModIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 25, 2, 1, 1),
    _BatteryModIndex_Type()
)
batteryModIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryModIndex.setStatus("mandatory")
_BatteryIndex_Type = Integer32
_BatteryIndex_Object = MibTableColumn
batteryIndex = _BatteryIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 25, 2, 1, 2),
    _BatteryIndex_Type()
)
batteryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryIndex.setStatus("mandatory")


class _BatteryType_Type(Integer32):
    """Custom type batteryType based on Integer32"""
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
        *(("lithiumION", 2),
          ("metalHydride", 4),
          ("nickelCadmium", 3),
          ("standardDryCell", 1),
          ("unknown", 0))
    )


_BatteryType_Type.__name__ = "Integer32"
_BatteryType_Object = MibTableColumn
batteryType = _BatteryType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 25, 2, 1, 3),
    _BatteryType_Type()
)
batteryType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryType.setStatus("mandatory")


class _BatteryDescr_Type(DisplayString):
    """Custom type batteryDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_BatteryDescr_Type.__name__ = "DisplayString"
_BatteryDescr_Object = MibTableColumn
batteryDescr = _BatteryDescr_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 25, 2, 1, 4),
    _BatteryDescr_Type()
)
batteryDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryDescr.setStatus("mandatory")


class _BatteryChargeStatus_Type(Integer32):
    """Custom type batteryChargeStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fastCharging", 1),
          ("notCharging", 0),
          ("trickleCharging", 2))
    )


_BatteryChargeStatus_Type.__name__ = "Integer32"
_BatteryChargeStatus_Object = MibScalar
batteryChargeStatus = _BatteryChargeStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 25, 2, 1, 5),
    _BatteryChargeStatus_Type()
)
batteryChargeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryChargeStatus.setStatus("mandatory")
_BatteryFastChargeCount_Type = Integer32
_BatteryFastChargeCount_Object = MibScalar
batteryFastChargeCount = _BatteryFastChargeCount_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 25, 2, 1, 6),
    _BatteryFastChargeCount_Type()
)
batteryFastChargeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryFastChargeCount.setStatus("mandatory")


class _BatteryChargePercent_Type(Integer32):
    """Custom type batteryChargePercent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_BatteryChargePercent_Type.__name__ = "Integer32"
_BatteryChargePercent_Object = MibTableColumn
batteryChargePercent = _BatteryChargePercent_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 25, 2, 1, 7),
    _BatteryChargePercent_Type()
)
batteryChargePercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryChargePercent.setStatus("mandatory")


class _BatteryStatus_Type(Integer32):
    """Custom type batteryStatus based on Integer32"""
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
        *(("critical", 5),
          ("non-recoverable", 6),
          ("ok", 3),
          ("other", 1),
          ("undetermined", 0),
          ("unknown", 2),
          ("warning", 4))
    )


_BatteryStatus_Type.__name__ = "Integer32"
_BatteryStatus_Object = MibTableColumn
batteryStatus = _BatteryStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 25, 2, 1, 8),
    _BatteryStatus_Type()
)
batteryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryStatus.setStatus("mandatory")
_BatteryLastAlarm_Type = TimeTicks
_BatteryLastAlarm_Object = MibTableColumn
batteryLastAlarm = _BatteryLastAlarm_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 25, 2, 1, 9),
    _BatteryLastAlarm_Type()
)
batteryLastAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryLastAlarm.setStatus("mandatory")
_BatteryTrapSystem_Type = OctetString
_BatteryTrapSystem_Object = MibTableColumn
batteryTrapSystem = _BatteryTrapSystem_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 25, 2, 1, 10),
    _BatteryTrapSystem_Type()
)
batteryTrapSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryTrapSystem.setStatus("mandatory")
_BatteryTrapGroup_Type = OctetString
_BatteryTrapGroup_Object = MibTableColumn
batteryTrapGroup = _BatteryTrapGroup_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 25, 2, 1, 11),
    _BatteryTrapGroup_Type()
)
batteryTrapGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryTrapGroup.setStatus("mandatory")
_BatteryTrapMessage_Type = OctetString
_BatteryTrapMessage_Object = MibTableColumn
batteryTrapMessage = _BatteryTrapMessage_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 25, 2, 1, 12),
    _BatteryTrapMessage_Type()
)
batteryTrapMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryTrapMessage.setStatus("mandatory")
_HealthStatus_ObjectIdentity = ObjectIdentity
healthStatus = _HealthStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 26)
)
_HealthStatusNumber_Type = Gauge32
_HealthStatusNumber_Object = MibScalar
healthStatusNumber = _HealthStatusNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 26, 1),
    _HealthStatusNumber_Type()
)
healthStatusNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthStatusNumber.setStatus("mandatory")
_HealthTable_Object = MibTable
healthTable = _HealthTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 26, 2)
)
if mibBuilder.loadTexts:
    healthTable.setStatus("mandatory")
_HealthEntry_Object = MibTableRow
healthEntry = _HealthEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 26, 2, 1)
)
healthEntry.setIndexNames(
    (0, "VM-MIB", "healthModIndex"),
    (0, "VM-MIB", "healthIndex"),
)
if mibBuilder.loadTexts:
    healthEntry.setStatus("mandatory")
_HealthModIndex_Type = Integer32
_HealthModIndex_Object = MibTableColumn
healthModIndex = _HealthModIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 26, 2, 1, 1),
    _HealthModIndex_Type()
)
healthModIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthModIndex.setStatus("mandatory")
_HealthIndex_Type = Integer32
_HealthIndex_Object = MibTableColumn
healthIndex = _HealthIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 26, 2, 1, 2),
    _HealthIndex_Type()
)
healthIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthIndex.setStatus("mandatory")


class _HealthType_Type(Integer32):
    """Custom type healthType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("overallCard", 1),
          ("overallIPMI", 3),
          ("overallSystem", 2),
          ("unknown", 0))
    )


_HealthType_Type.__name__ = "Integer32"
_HealthType_Object = MibTableColumn
healthType = _HealthType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 26, 2, 1, 3),
    _HealthType_Type()
)
healthType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthType.setStatus("mandatory")


class _OverallHealthStatus_Type(Integer32):
    """Custom type overallHealthStatus based on Integer32"""
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
        *(("critical", 5),
          ("non-recoverable", 6),
          ("ok", 3),
          ("other", 1),
          ("undetermined", 0),
          ("unknown", 2),
          ("warning", 4))
    )


_OverallHealthStatus_Type.__name__ = "Integer32"
_OverallHealthStatus_Object = MibTableColumn
overallHealthStatus = _OverallHealthStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 26, 2, 1, 4),
    _OverallHealthStatus_Type()
)
overallHealthStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    overallHealthStatus.setStatus("mandatory")


class _OverallVoltageStatus_Type(Integer32):
    """Custom type overallVoltageStatus based on Integer32"""
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
        *(("critical", 5),
          ("non-recoverable", 6),
          ("ok", 3),
          ("other", 1),
          ("undetermined", 0),
          ("unknown", 2),
          ("warning", 4))
    )


_OverallVoltageStatus_Type.__name__ = "Integer32"
_OverallVoltageStatus_Object = MibTableColumn
overallVoltageStatus = _OverallVoltageStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 26, 2, 1, 5),
    _OverallVoltageStatus_Type()
)
overallVoltageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    overallVoltageStatus.setStatus("mandatory")


class _OverallTemperatureStatus_Type(Integer32):
    """Custom type overallTemperatureStatus based on Integer32"""
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
        *(("critical", 5),
          ("non-recoverable", 6),
          ("ok", 3),
          ("other", 1),
          ("undetermined", 0),
          ("unknown", 2),
          ("warning", 4))
    )


_OverallTemperatureStatus_Type.__name__ = "Integer32"
_OverallTemperatureStatus_Object = MibTableColumn
overallTemperatureStatus = _OverallTemperatureStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 26, 2, 1, 6),
    _OverallTemperatureStatus_Type()
)
overallTemperatureStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    overallTemperatureStatus.setStatus("mandatory")


class _OverallBatteryStatus_Type(Integer32):
    """Custom type overallBatteryStatus based on Integer32"""
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
        *(("critical", 5),
          ("non-recoverable", 6),
          ("ok", 3),
          ("other", 1),
          ("undetermined", 0),
          ("unknown", 2),
          ("warning", 4))
    )


_OverallBatteryStatus_Type.__name__ = "Integer32"
_OverallBatteryStatus_Object = MibTableColumn
overallBatteryStatus = _OverallBatteryStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 26, 2, 1, 7),
    _OverallBatteryStatus_Type()
)
overallBatteryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    overallBatteryStatus.setStatus("mandatory")
_Traps_ObjectIdentity = ObjectIdentity
traps = _Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 100)
)

# Managed Objects groups


# Notification objects

trapVoltageGood = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 0, 4)
)
trapVoltageGood.setObjects(
      *(("VM-MIB", "voltTrapSystem"),
        ("VM-MIB", "voltTrapGroup"),
        ("VM-MIB", "voltTrapMessage"),
        ("VM-MIB", "voltItemStatus"),
        ("VM-MIB", "voltReading"))
)
if mibBuilder.loadTexts:
    trapVoltageGood.setStatus(
        ""
    )

trapVoltageWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 0, 5)
)
trapVoltageWarning.setObjects(
      *(("VM-MIB", "voltTrapSystem"),
        ("VM-MIB", "voltTrapGroup"),
        ("VM-MIB", "voltTrapMessage"),
        ("VM-MIB", "voltItemStatus"),
        ("VM-MIB", "voltReading"))
)
if mibBuilder.loadTexts:
    trapVoltageWarning.setStatus(
        ""
    )

trapVoltageCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 0, 6)
)
trapVoltageCritical.setObjects(
      *(("VM-MIB", "voltTrapSystem"),
        ("VM-MIB", "voltTrapGroup"),
        ("VM-MIB", "voltTrapMessage"),
        ("VM-MIB", "voltItemStatus"),
        ("VM-MIB", "voltReading"))
)
if mibBuilder.loadTexts:
    trapVoltageCritical.setStatus(
        ""
    )

trapTemperatureGood = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 0, 7)
)
trapTemperatureGood.setObjects(
      *(("VM-MIB", "tempTrapSystem"),
        ("VM-MIB", "tempTrapGroup"),
        ("VM-MIB", "tempTrapMessage"),
        ("VM-MIB", "tempItemStatus"),
        ("VM-MIB", "tempReading"))
)
if mibBuilder.loadTexts:
    trapTemperatureGood.setStatus(
        ""
    )

trapTemperatureWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 0, 8)
)
trapTemperatureWarning.setObjects(
      *(("VM-MIB", "tempTrapSystem"),
        ("VM-MIB", "tempTrapGroup"),
        ("VM-MIB", "tempTrapMessage"),
        ("VM-MIB", "tempItemStatus"),
        ("VM-MIB", "tempReading"))
)
if mibBuilder.loadTexts:
    trapTemperatureWarning.setStatus(
        ""
    )

trapTemperatureCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 0, 9)
)
trapTemperatureCritical.setObjects(
      *(("VM-MIB", "tempTrapSystem"),
        ("VM-MIB", "tempTrapGroup"),
        ("VM-MIB", "tempTrapMessage"),
        ("VM-MIB", "tempItemStatus"),
        ("VM-MIB", "tempReading"))
)
if mibBuilder.loadTexts:
    trapTemperatureCritical.setStatus(
        ""
    )

trapBatteryGood = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 0, 10)
)
trapBatteryGood.setObjects(
      *(("VM-MIB", "batteryTrapSystem"),
        ("VM-MIB", "batteryTrapGroup"),
        ("VM-MIB", "batteryTrapMessage"),
        ("VM-MIB", "batteryStatus"),
        ("VM-MIB", "batteryChargePercent"))
)
if mibBuilder.loadTexts:
    trapBatteryGood.setStatus(
        ""
    )

trapBatteryLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10890, 5, 0, 11)
)
trapBatteryLow.setObjects(
      *(("VM-MIB", "batteryTrapSystem"),
        ("VM-MIB", "batteryTrapGroup"),
        ("VM-MIB", "batteryTrapMessage"),
        ("VM-MIB", "batteryStatus"),
        ("VM-MIB", "batteryChargePercent"))
)
if mibBuilder.loadTexts:
    trapBatteryLow.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VM-MIB",
    **{"dell": dell,
       "server": server,
       "drac2": drac2,
       "trapVoltageGood": trapVoltageGood,
       "trapVoltageWarning": trapVoltageWarning,
       "trapVoltageCritical": trapVoltageCritical,
       "trapTemperatureGood": trapTemperatureGood,
       "trapTemperatureWarning": trapTemperatureWarning,
       "trapTemperatureCritical": trapTemperatureCritical,
       "trapBatteryGood": trapBatteryGood,
       "trapBatteryLow": trapBatteryLow,
       "identification": identification,
       "idManufacturer": idManufacturer,
       "idProduct": idProduct,
       "idAgentRevMajor": idAgentRevMajor,
       "idAgentRevMinor": idAgentRevMinor,
       "idMibRevMajor": idMibRevMajor,
       "idMibRevMinor": idMibRevMinor,
       "module": module,
       "modNumber": modNumber,
       "modTable": modTable,
       "modEntry": modEntry,
       "modIndex": modIndex,
       "modFwRevMajor": modFwRevMajor,
       "modFwRevMinor": modFwRevMinor,
       "modType": modType,
       "modFwRelDate": modFwRelDate,
       "modPciBridge": modPciBridge,
       "modNetworkCtrl": modNetworkCtrl,
       "modPcmciaHost": modPcmciaHost,
       "modPcCardMfgr": modPcCardMfgr,
       "modPcCardName": modPcCardName,
       "modBattery": modBattery,
       "modVoltCount": modVoltCount,
       "modTempCount": modTempCount,
       "modFanCount": modFanCount,
       "modSwitchCount": modSwitchCount,
       "modFaultCount": modFaultCount,
       "modUpTime": modUpTime,
       "modStartDelay": modStartDelay,
       "modRecoveryTimeout": modRecoveryTimeout,
       "modAutoRecoveryEnable": modAutoRecoveryEnable,
       "modHeartBeatEnable": modHeartBeatEnable,
       "modAccessControl": modAccessControl,
       "modEthernetAddress": modEthernetAddress,
       "configAdmin": configAdmin,
       "cfgAdminNumber": cfgAdminNumber,
       "cfgAdminTable": cfgAdminTable,
       "cfgAdminEntry": cfgAdminEntry,
       "cfgAdminModIndex": cfgAdminModIndex,
       "cfgAdminIndex": cfgAdminIndex,
       "cfgAdminAlias": cfgAdminAlias,
       "cfgAdminPassword": cfgAdminPassword,
       "cfgAdminSessionCallback": cfgAdminSessionCallback,
       "cfgAdminPagerNumber": cfgAdminPagerNumber,
       "cfgAdminPagerSubscriber": cfgAdminPagerSubscriber,
       "cfgAdminPagerType": cfgAdminPagerType,
       "cfgAdminPagerMask": cfgAdminPagerMask,
       "cfgAdminCustomPagerCode": cfgAdminCustomPagerCode,
       "cfgAdminTestPager": cfgAdminTestPager,
       "configAlert": configAlert,
       "cfgAlertNumber": cfgAlertNumber,
       "cfgAlertTable": cfgAlertTable,
       "cfgAlertEntry": cfgAlertEntry,
       "cfgAlertModIndex": cfgAlertModIndex,
       "cfgAlertIndex": cfgAlertIndex,
       "cfgAlertTrapSendIPAddress": cfgAlertTrapSendIPAddress,
       "cfgAlertTrapSendCommunity": cfgAlertTrapSendCommunity,
       "cfgAlertTrapCallBackNumber": cfgAlertTrapCallBackNumber,
       "configNetwork": configNetwork,
       "cfgNetNumber": cfgNetNumber,
       "cfgNetTable": cfgNetTable,
       "cfgNetEntry": cfgNetEntry,
       "cfgNetModIndex": cfgNetModIndex,
       "cfgNetIndex": cfgNetIndex,
       "cfgNetIPAddress": cfgNetIPAddress,
       "cfgNetSubnetMask": cfgNetSubnetMask,
       "cfgNetGateway": cfgNetGateway,
       "configModem": configModem,
       "cfgModemNumber": cfgModemNumber,
       "cfgModemTable": cfgModemTable,
       "cfgModemEntry": cfgModemEntry,
       "cfgModemModIndex": cfgModemModIndex,
       "cfgModemIndex": cfgModemIndex,
       "cfgModemBaudRate": cfgModemBaudRate,
       "cfgModemDialMode": cfgModemDialMode,
       "cfgModemExtraInitString": cfgModemExtraInitString,
       "cfgModemPwrOnDelay": cfgModemPwrOnDelay,
       "cfgModemSignalDelay": cfgModemSignalDelay,
       "cfgModemRingDelay": cfgModemRingDelay,
       "cfgModemCDDelay": cfgModemCDDelay,
       "cfgModemResponseDelay": cfgModemResponseDelay,
       "cfgModemHangUpDelay": cfgModemHangUpDelay,
       "cfgModemConnectTimeout": cfgModemConnectTimeout,
       "cfgModemDetectTimeout": cfgModemDetectTimeout,
       "control": control,
       "ctlNumber": ctlNumber,
       "ctlTable": ctlTable,
       "ctlEntry": ctlEntry,
       "ctlModIndex": ctlModIndex,
       "ctlIndex": ctlIndex,
       "ctlSystemReset": ctlSystemReset,
       "ctlSystemShutdown": ctlSystemShutdown,
       "ctlSystemPwrCycle": ctlSystemPwrCycle,
       "ctlCardShutdown": ctlCardShutdown,
       "ctlCardSoftReset": ctlCardSoftReset,
       "ctlCardHardReset": ctlCardHardReset,
       "ctlCardFlushGPNV": ctlCardFlushGPNV,
       "voltage": voltage,
       "voltNumber": voltNumber,
       "voltTable": voltTable,
       "voltEntry": voltEntry,
       "voltModIndex": voltModIndex,
       "voltIndex": voltIndex,
       "voltType": voltType,
       "voltDescr": voltDescr,
       "voltReading": voltReading,
       "voltLimitLowCritical": voltLimitLowCritical,
       "voltLimitHighCritical": voltLimitHighCritical,
       "voltLimitLowWarning": voltLimitLowWarning,
       "voltLimitHighWarning": voltLimitHighWarning,
       "voltItemStatus": voltItemStatus,
       "voltLastAlarm": voltLastAlarm,
       "voltTrapSystem": voltTrapSystem,
       "voltTrapGroup": voltTrapGroup,
       "voltTrapMessage": voltTrapMessage,
       "temperature": temperature,
       "tempNumber": tempNumber,
       "tempTable": tempTable,
       "tempEntry": tempEntry,
       "tempModIndex": tempModIndex,
       "tempIndex": tempIndex,
       "tempType": tempType,
       "tempDescr": tempDescr,
       "tempReading": tempReading,
       "tempLowCritical": tempLowCritical,
       "tempHighCritical": tempHighCritical,
       "tempLowWarning": tempLowWarning,
       "tempHighWarning": tempHighWarning,
       "tempItemStatus": tempItemStatus,
       "tempLastAlarm": tempLastAlarm,
       "tempTrapSystem": tempTrapSystem,
       "tempTrapGroup": tempTrapGroup,
       "tempTrapMessage": tempTrapMessage,
       "battery": battery,
       "batteryNumber": batteryNumber,
       "batteryTable": batteryTable,
       "batteryEntry": batteryEntry,
       "batteryModIndex": batteryModIndex,
       "batteryIndex": batteryIndex,
       "batteryType": batteryType,
       "batteryDescr": batteryDescr,
       "batteryChargeStatus": batteryChargeStatus,
       "batteryFastChargeCount": batteryFastChargeCount,
       "batteryChargePercent": batteryChargePercent,
       "batteryStatus": batteryStatus,
       "batteryLastAlarm": batteryLastAlarm,
       "batteryTrapSystem": batteryTrapSystem,
       "batteryTrapGroup": batteryTrapGroup,
       "batteryTrapMessage": batteryTrapMessage,
       "healthStatus": healthStatus,
       "healthStatusNumber": healthStatusNumber,
       "healthTable": healthTable,
       "healthEntry": healthEntry,
       "healthModIndex": healthModIndex,
       "healthIndex": healthIndex,
       "healthType": healthType,
       "overallHealthStatus": overallHealthStatus,
       "overallVoltageStatus": overallVoltageStatus,
       "overallTemperatureStatus": overallTemperatureStatus,
       "overallBatteryStatus": overallBatteryStatus,
       "traps": traps}
)
