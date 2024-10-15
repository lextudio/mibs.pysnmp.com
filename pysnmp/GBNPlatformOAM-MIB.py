# SNMP MIB module (GBNPlatformOAM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/GBNPlatformOAM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:47:53 2024
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

(gbnPlatform,) = mibBuilder.importSymbols(
    "GREENTECH-MASTER-MIB",
    "gbnPlatform")

(PortList,
 dot1qStaticMulticastEntry) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList",
    "dot1qStaticMulticastEntry")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

gbnPlatformOAM = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1)
)
gbnPlatformOAM.setRevisions(
        ("1900-11-02 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class VctRunResultTxRxPairNoType(Integer32, TextualConvention):
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
        *(("rxpair1", 1),
          ("rxpair2", 3),
          ("txpair1", 0),
          ("txpair2", 2))
    )



class VctRunResultStatusType(Integer32, TextualConvention):
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
        *(("impedance_mismatch", 3),
          ("normal", 0),
          ("open", 2),
          ("short", 1))
    )



# MIB Managed Objects in the order of their OIDs

_GbnPlatformOAMSysIf_ObjectIdentity = ObjectIdentity
gbnPlatformOAMSysIf = _GbnPlatformOAMSysIf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 1)
)
_SysIfMACAddr_Type = MacAddress
_SysIfMACAddr_Object = MibScalar
sysIfMACAddr = _SysIfMACAddr_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 1, 1),
    _SysIfMACAddr_Type()
)
sysIfMACAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysIfMACAddr.setStatus("current")
_SysIfIpAddress_Type = IpAddress
_SysIfIpAddress_Object = MibScalar
sysIfIpAddress = _SysIfIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 1, 2),
    _SysIfIpAddress_Type()
)
sysIfIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysIfIpAddress.setStatus("current")
_SysIfIPGateAddress_Type = IpAddress
_SysIfIPGateAddress_Object = MibScalar
sysIfIPGateAddress = _SysIfIPGateAddress_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 1, 3),
    _SysIfIPGateAddress_Type()
)
sysIfIPGateAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysIfIPGateAddress.setStatus("current")
_SysIfIPNetMask_Type = IpAddress
_SysIfIPNetMask_Object = MibScalar
sysIfIPNetMask = _SysIfIPNetMask_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 1, 4),
    _SysIfIPNetMask_Type()
)
sysIfIPNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysIfIPNetMask.setStatus("current")


class _SysIfIPStatus_Type(Integer32):
    """Custom type sysIfIPStatus based on Integer32"""
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
        *(("apply", 4),
          ("modified", 2),
          ("notModified", 1),
          ("restore", 3))
    )


_SysIfIPStatus_Type.__name__ = "Integer32"
_SysIfIPStatus_Object = MibScalar
sysIfIPStatus = _SysIfIPStatus_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 1, 5),
    _SysIfIPStatus_Type()
)
sysIfIPStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysIfIPStatus.setStatus("current")


class _SysIfBOOTPOnOff_Type(Integer32):
    """Custom type sysIfBOOTPOnOff based on Integer32"""
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


_SysIfBOOTPOnOff_Type.__name__ = "Integer32"
_SysIfBOOTPOnOff_Object = MibScalar
sysIfBOOTPOnOff = _SysIfBOOTPOnOff_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 1, 7),
    _SysIfBOOTPOnOff_Type()
)
sysIfBOOTPOnOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysIfBOOTPOnOff.setStatus("current")


class _SysIfDHCPOnOff_Type(Integer32):
    """Custom type sysIfDHCPOnOff based on Integer32"""
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


_SysIfDHCPOnOff_Type.__name__ = "Integer32"
_SysIfDHCPOnOff_Object = MibScalar
sysIfDHCPOnOff = _SysIfDHCPOnOff_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 1, 8),
    _SysIfDHCPOnOff_Type()
)
sysIfDHCPOnOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysIfDHCPOnOff.setStatus("current")
_SysIfManageVLANTbale_Object = MibTable
sysIfManageVLANTbale = _SysIfManageVLANTbale_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 1, 9)
)
if mibBuilder.loadTexts:
    sysIfManageVLANTbale.setStatus("mandatory")
_SysIfManageVLANEntry_Object = MibTableRow
sysIfManageVLANEntry = _SysIfManageVLANEntry_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 1, 9, 1)
)
sysIfManageVLANEntry.setIndexNames(
    (0, "GBNPlatformOAM-MIB", "sysIfManageVLANVid"),
)
if mibBuilder.loadTexts:
    sysIfManageVLANEntry.setStatus("mandatory")
_SysIfManageVLANVid_Type = Integer32
_SysIfManageVLANVid_Object = MibTableColumn
sysIfManageVLANVid = _SysIfManageVLANVid_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 1, 9, 1, 1),
    _SysIfManageVLANVid_Type()
)
sysIfManageVLANVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysIfManageVLANVid.setStatus("current")
_SysIfManageVLANRowStatus_Type = RowStatus
_SysIfManageVLANRowStatus_Object = MibTableColumn
sysIfManageVLANRowStatus = _SysIfManageVLANRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 1, 9, 1, 2),
    _SysIfManageVLANRowStatus_Type()
)
sysIfManageVLANRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysIfManageVLANRowStatus.setStatus("current")
_GbnPlatformOAMSystem_ObjectIdentity = ObjectIdentity
gbnPlatformOAMSystem = _GbnPlatformOAMSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 2)
)


class _SoftwarePlate_Type(DisplayString):
    """Custom type softwarePlate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_SoftwarePlate_Type.__name__ = "DisplayString"
_SoftwarePlate_Object = MibScalar
softwarePlate = _SoftwarePlate_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 2, 1),
    _SoftwarePlate_Type()
)
softwarePlate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softwarePlate.setStatus("current")


class _SoftwareVersion_Type(DisplayString):
    """Custom type softwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_SoftwareVersion_Type.__name__ = "DisplayString"
_SoftwareVersion_Object = MibScalar
softwareVersion = _SoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 2, 2),
    _SoftwareVersion_Type()
)
softwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softwareVersion.setStatus("current")


class _SoftwareCompiledTimeE_Type(DisplayString):
    """Custom type softwareCompiledTimeE based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_SoftwareCompiledTimeE_Type.__name__ = "DisplayString"
_SoftwareCompiledTimeE_Object = MibScalar
softwareCompiledTimeE = _SoftwareCompiledTimeE_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 2, 3),
    _SoftwareCompiledTimeE_Type()
)
softwareCompiledTimeE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softwareCompiledTimeE.setStatus("current")


class _SoftwareCompiledTimeC_Type(DisplayString):
    """Custom type softwareCompiledTimeC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_SoftwareCompiledTimeC_Type.__name__ = "DisplayString"
_SoftwareCompiledTimeC_Object = MibScalar
softwareCompiledTimeC = _SoftwareCompiledTimeC_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 2, 4),
    _SoftwareCompiledTimeC_Type()
)
softwareCompiledTimeC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softwareCompiledTimeC.setStatus("current")


class _CpuDescription_Type(DisplayString):
    """Custom type cpuDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_CpuDescription_Type.__name__ = "DisplayString"
_CpuDescription_Object = MibScalar
cpuDescription = _CpuDescription_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 2, 5),
    _CpuDescription_Type()
)
cpuDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuDescription.setStatus("current")


class _SdramDescription_Type(DisplayString):
    """Custom type sdramDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_SdramDescription_Type.__name__ = "DisplayString"
_SdramDescription_Object = MibScalar
sdramDescription = _SdramDescription_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 2, 6),
    _SdramDescription_Type()
)
sdramDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdramDescription.setStatus("current")


class _FlashDescription_Type(DisplayString):
    """Custom type flashDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_FlashDescription_Type.__name__ = "DisplayString"
_FlashDescription_Object = MibScalar
flashDescription = _FlashDescription_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 2, 7),
    _FlashDescription_Type()
)
flashDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flashDescription.setStatus("current")


class _HardwareVersion_Type(DisplayString):
    """Custom type hardwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_HardwareVersion_Type.__name__ = "DisplayString"
_HardwareVersion_Object = MibScalar
hardwareVersion = _HardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 2, 8),
    _HardwareVersion_Type()
)
hardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hardwareVersion.setStatus("current")


class _BootromVersion_Type(DisplayString):
    """Custom type bootromVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_BootromVersion_Type.__name__ = "DisplayString"
_BootromVersion_Object = MibScalar
bootromVersion = _BootromVersion_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 2, 9),
    _BootromVersion_Type()
)
bootromVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bootromVersion.setStatus("current")


class _HostName_Type(DisplayString):
    """Custom type hostName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HostName_Type.__name__ = "DisplayString"
_HostName_Object = MibScalar
hostName = _HostName_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 2, 10),
    _HostName_Type()
)
hostName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hostName.setStatus("current")


class _CpuIdle_Type(Integer32):
    """Custom type cpuIdle based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CpuIdle_Type.__name__ = "Integer32"
_CpuIdle_Object = MibScalar
cpuIdle = _CpuIdle_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 2, 11),
    _CpuIdle_Type()
)
cpuIdle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuIdle.setStatus("current")
_MemorySize_Type = Integer32
_MemorySize_Object = MibScalar
memorySize = _MemorySize_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 2, 12),
    _MemorySize_Type()
)
memorySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memorySize.setStatus("current")
_MemoryIdle_Type = Integer32
_MemoryIdle_Object = MibScalar
memoryIdle = _MemoryIdle_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 2, 13),
    _MemoryIdle_Type()
)
memoryIdle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryIdle.setStatus("current")
_SystemClock_ObjectIdentity = ObjectIdentity
systemClock = _SystemClock_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 2, 14)
)
_ClockTime_Type = Unsigned32
_ClockTime_Object = MibScalar
clockTime = _ClockTime_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 2, 14, 1),
    _ClockTime_Type()
)
clockTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clockTime.setStatus("current")


class _TimeZoneName_Type(DisplayString):
    """Custom type timeZoneName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_TimeZoneName_Type.__name__ = "DisplayString"
_TimeZoneName_Object = MibScalar
timeZoneName = _TimeZoneName_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 2, 14, 2),
    _TimeZoneName_Type()
)
timeZoneName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeZoneName.setStatus("current")


class _TimeZoneOffset_Type(Integer32):
    """Custom type timeZoneOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86399),
    )


_TimeZoneOffset_Type.__name__ = "Integer32"
_TimeZoneOffset_Object = MibScalar
timeZoneOffset = _TimeZoneOffset_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 2, 14, 3),
    _TimeZoneOffset_Type()
)
timeZoneOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeZoneOffset.setStatus("current")
_OffsetNegFlag_Type = TruthValue
_OffsetNegFlag_Object = MibScalar
offsetNegFlag = _OffsetNegFlag_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 2, 14, 4),
    _OffsetNegFlag_Type()
)
offsetNegFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    offsetNegFlag.setStatus("current")


class _ProductName_Type(DisplayString):
    """Custom type productName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_ProductName_Type.__name__ = "DisplayString"
_ProductName_Object = MibScalar
productName = _ProductName_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 2, 15),
    _ProductName_Type()
)
productName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    productName.setStatus("current")


class _SystemReset_Type(Integer32):
    """Custom type systemReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noop", 1),
          ("reset", 2),
          ("resetToDefaults", 3))
    )


_SystemReset_Type.__name__ = "Integer32"
_SystemReset_Object = MibScalar
systemReset = _SystemReset_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 2, 16),
    _SystemReset_Type()
)
systemReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemReset.setStatus("current")


class _WriteConfig_Type(Integer32):
    """Custom type writeConfig based on Integer32"""
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
        *(("noop", 1),
          ("save", 2),
          ("saveFailed", 4),
          ("saveInProgress", 3))
    )


_WriteConfig_Type.__name__ = "Integer32"
_WriteConfig_Object = MibScalar
writeConfig = _WriteConfig_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 2, 17),
    _WriteConfig_Type()
)
writeConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    writeConfig.setStatus("current")
_SaveNMInterfaceConfig_ObjectIdentity = ObjectIdentity
saveNMInterfaceConfig = _SaveNMInterfaceConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 2, 18)
)


class _NmInterfaceId_Type(Integer32):
    """Custom type nmInterfaceId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_NmInterfaceId_Type.__name__ = "Integer32"
_NmInterfaceId_Object = MibScalar
nmInterfaceId = _NmInterfaceId_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 2, 18, 1),
    _NmInterfaceId_Type()
)
nmInterfaceId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmInterfaceId.setStatus("current")
_NmInterfaceIpAddress_Type = IpAddress
_NmInterfaceIpAddress_Object = MibScalar
nmInterfaceIpAddress = _NmInterfaceIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 2, 18, 2),
    _NmInterfaceIpAddress_Type()
)
nmInterfaceIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmInterfaceIpAddress.setStatus("current")
_NmInterfaceNetMask_Type = IpAddress
_NmInterfaceNetMask_Object = MibScalar
nmInterfaceNetMask = _NmInterfaceNetMask_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 2, 18, 3),
    _NmInterfaceNetMask_Type()
)
nmInterfaceNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmInterfaceNetMask.setStatus("current")
_NmInterfaceGateAddress_Type = IpAddress
_NmInterfaceGateAddress_Object = MibScalar
nmInterfaceGateAddress = _NmInterfaceGateAddress_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 2, 18, 4),
    _NmInterfaceGateAddress_Type()
)
nmInterfaceGateAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmInterfaceGateAddress.setStatus("current")


class _WriteNMInterfaceConifig_Type(Integer32):
    """Custom type writeNMInterfaceConifig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("saveNmconfig", 1)
    )


_WriteNMInterfaceConifig_Type.__name__ = "Integer32"
_WriteNMInterfaceConifig_Object = MibScalar
writeNMInterfaceConifig = _WriteNMInterfaceConifig_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 2, 18, 5),
    _WriteNMInterfaceConifig_Type()
)
writeNMInterfaceConifig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    writeNMInterfaceConifig.setStatus("current")


class _WriteNMInterfaceConifigStatus_Type(Integer32):
    """Custom type writeNMInterfaceConifigStatus based on Integer32"""
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
        *(("differentSubnet", 6),
          ("invalidIpOrMask", 11),
          ("noGatewayParameter", 10),
          ("noInterface", 4),
          ("noInterfaceParameter", 7),
          ("noIpAddress", 5),
          ("noIpAddressParameter", 8),
          ("noMaskParameter", 9),
          ("saveFailed", 3),
          ("saveInProgress", 2),
          ("saveSuccess", 1))
    )


_WriteNMInterfaceConifigStatus_Type.__name__ = "Integer32"
_WriteNMInterfaceConifigStatus_Object = MibScalar
writeNMInterfaceConifigStatus = _WriteNMInterfaceConifigStatus_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 2, 18, 6),
    _WriteNMInterfaceConifigStatus_Type()
)
writeNMInterfaceConifigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    writeNMInterfaceConifigStatus.setStatus("current")


class _ProdSerialNo_Type(DisplayString):
    """Custom type prodSerialNo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_ProdSerialNo_Type.__name__ = "DisplayString"
_ProdSerialNo_Object = MibScalar
prodSerialNo = _ProdSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 2, 19),
    _ProdSerialNo_Type()
)
prodSerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prodSerialNo.setStatus("current")
_CpuBusyStatus_Type = TruthValue
_CpuBusyStatus_Object = MibScalar
cpuBusyStatus = _CpuBusyStatus_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 2, 20),
    _CpuBusyStatus_Type()
)
cpuBusyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuBusyStatus.setStatus("current")


class _CpuBusyAlarmEnable_Type(TruthValue):
    """Custom type cpuBusyAlarmEnable based on TruthValue"""
    defaultValue = 1

    subtypeSpec = TruthValue.subtypeSpec
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


_CpuBusyAlarmEnable_Type.__name__ = "TruthValue"
_CpuBusyAlarmEnable_Object = MibScalar
cpuBusyAlarmEnable = _CpuBusyAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 2, 21),
    _CpuBusyAlarmEnable_Type()
)
cpuBusyAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpuBusyAlarmEnable.setStatus("current")


class _CpuBusyThreshold_Type(Integer32):
    """Custom type cpuBusyThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CpuBusyThreshold_Type.__name__ = "Integer32"
_CpuBusyThreshold_Object = MibScalar
cpuBusyThreshold = _CpuBusyThreshold_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 2, 22),
    _CpuBusyThreshold_Type()
)
cpuBusyThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpuBusyThreshold.setStatus("current")
_CpuUnbusyThreshold_Type = Integer32
_CpuUnbusyThreshold_Object = MibScalar
cpuUnbusyThreshold = _CpuUnbusyThreshold_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 2, 23),
    _CpuUnbusyThreshold_Type()
)
cpuUnbusyThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpuUnbusyThreshold.setStatus("current")
_CpuStatusTrap_ObjectIdentity = ObjectIdentity
cpuStatusTrap = _CpuStatusTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 2, 24)
)
_GbnPlatformOAMIpAccessControl_ObjectIdentity = ObjectIdentity
gbnPlatformOAMIpAccessControl = _GbnPlatformOAMIpAccessControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 3)
)
_IpAccessControlTable_Object = MibTable
ipAccessControlTable = _IpAccessControlTable_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    ipAccessControlTable.setStatus("current")
_IpAccessControlEntry_Object = MibTableRow
ipAccessControlEntry = _IpAccessControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 3, 1, 1)
)
ipAccessControlEntry.setIndexNames(
    (0, "GBNPlatformOAM-MIB", "controlIpAddress"),
    (0, "GBNPlatformOAM-MIB", "controlIpMask"),
    (0, "GBNPlatformOAM-MIB", "controlTeminal"),
)
if mibBuilder.loadTexts:
    ipAccessControlEntry.setStatus("current")
_ControlIpAddress_Type = IpAddress
_ControlIpAddress_Object = MibTableColumn
controlIpAddress = _ControlIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 3, 1, 1, 1),
    _ControlIpAddress_Type()
)
controlIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlIpAddress.setStatus("current")
_ControlIpMask_Type = IpAddress
_ControlIpMask_Object = MibTableColumn
controlIpMask = _ControlIpMask_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 3, 1, 1, 2),
    _ControlIpMask_Type()
)
controlIpMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlIpMask.setStatus("current")


class _ControlTeminal_Type(Integer32):
    """Custom type controlTeminal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("snmp", 1),
          ("telnet", 3),
          ("web", 2))
    )


_ControlTeminal_Type.__name__ = "Integer32"
_ControlTeminal_Object = MibTableColumn
controlTeminal = _ControlTeminal_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 3, 1, 1, 3),
    _ControlTeminal_Type()
)
controlTeminal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlTeminal.setStatus("current")


class _ControlStatus_Type(Integer32):
    """Custom type controlStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("destroy", 2))
    )


_ControlStatus_Type.__name__ = "Integer32"
_ControlStatus_Object = MibTableColumn
controlStatus = _ControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 3, 1, 1, 4),
    _ControlStatus_Type()
)
controlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    controlStatus.setStatus("current")
_GbnPlatformOAMWatchDog_ObjectIdentity = ObjectIdentity
gbnPlatformOAMWatchDog = _GbnPlatformOAMWatchDog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 4)
)


class _SoftDogProxy_Type(Integer32):
    """Custom type softDogProxy based on Integer32"""
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


_SoftDogProxy_Type.__name__ = "Integer32"
_SoftDogProxy_Object = MibScalar
softDogProxy = _SoftDogProxy_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 4, 1),
    _SoftDogProxy_Type()
)
softDogProxy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    softDogProxy.setStatus("current")
_GbnPlatformOAMMuser_ObjectIdentity = ObjectIdentity
gbnPlatformOAMMuser = _GbnPlatformOAMMuser_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 5)
)
_MusrTable_Object = MibTable
musrTable = _MusrTable_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 5, 1)
)
if mibBuilder.loadTexts:
    musrTable.setStatus("current")
_MusrEntry_Object = MibTableRow
musrEntry = _MusrEntry_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 5, 1, 1)
)
musrEntry.setIndexNames(
    (0, "GBNPlatformOAM-MIB", "musrIndex"),
)
if mibBuilder.loadTexts:
    musrEntry.setStatus("current")


class _MusrIndex_Type(Integer32):
    """Custom type musrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_MusrIndex_Type.__name__ = "Integer32"
_MusrIndex_Object = MibTableColumn
musrIndex = _MusrIndex_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 5, 1, 1, 1),
    _MusrIndex_Type()
)
musrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    musrIndex.setStatus("current")


class _MusrName_Type(DisplayString):
    """Custom type musrName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_MusrName_Type.__name__ = "DisplayString"
_MusrName_Object = MibTableColumn
musrName = _MusrName_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 5, 1, 1, 2),
    _MusrName_Type()
)
musrName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    musrName.setStatus("current")


class _MusrPassword_Type(DisplayString):
    """Custom type musrPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_MusrPassword_Type.__name__ = "DisplayString"
_MusrPassword_Object = MibTableColumn
musrPassword = _MusrPassword_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 5, 1, 1, 3),
    _MusrPassword_Type()
)
musrPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    musrPassword.setStatus("current")


class _MusrType_Type(Integer32):
    """Custom type musrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normalUser", 0),
          ("superUser", 1))
    )


_MusrType_Type.__name__ = "Integer32"
_MusrType_Object = MibTableColumn
musrType = _MusrType_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 5, 1, 1, 4),
    _MusrType_Type()
)
musrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    musrType.setStatus("current")


class _MusrRowStatus_Type(Integer32):
    """Custom type musrRowStatus based on Integer32"""
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


_MusrRowStatus_Type.__name__ = "Integer32"
_MusrRowStatus_Object = MibTableColumn
musrRowStatus = _MusrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 5, 1, 1, 5),
    _MusrRowStatus_Type()
)
musrRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    musrRowStatus.setStatus("current")


class _ManageUserAuthenType_Type(Integer32):
    """Custom type manageUserAuthenType based on Integer32"""
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
        *(("locacl", 1),
          ("radius", 2),
          ("radiusFailLocal", 3),
          ("tacacsplus", 4),
          ("tacacsplusFailLocal", 5))
    )


_ManageUserAuthenType_Type.__name__ = "Integer32"
_ManageUserAuthenType_Object = MibScalar
manageUserAuthenType = _ManageUserAuthenType_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 5, 2),
    _ManageUserAuthenType_Type()
)
manageUserAuthenType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    manageUserAuthenType.setStatus("current")


class _ManageUserAuthenRadiusName_Type(DisplayString):
    """Custom type manageUserAuthenRadiusName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ManageUserAuthenRadiusName_Type.__name__ = "DisplayString"
_ManageUserAuthenRadiusName_Object = MibScalar
manageUserAuthenRadiusName = _ManageUserAuthenRadiusName_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 5, 3),
    _ManageUserAuthenRadiusName_Type()
)
manageUserAuthenRadiusName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    manageUserAuthenRadiusName.setStatus("current")


class _ManageUserAuthChallegeType_Type(Integer32):
    """Custom type manageUserAuthChallegeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("chap", 1),
          ("pap", 2))
    )


_ManageUserAuthChallegeType_Type.__name__ = "Integer32"
_ManageUserAuthChallegeType_Object = MibScalar
manageUserAuthChallegeType = _ManageUserAuthChallegeType_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 5, 4),
    _ManageUserAuthChallegeType_Type()
)
manageUserAuthChallegeType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    manageUserAuthChallegeType.setStatus("current")
_ManageUserTacacsAuthor_Type = TruthValue
_ManageUserTacacsAuthor_Object = MibScalar
manageUserTacacsAuthor = _ManageUserTacacsAuthor_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 5, 5),
    _ManageUserTacacsAuthor_Type()
)
manageUserTacacsAuthor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    manageUserTacacsAuthor.setStatus("current")
_ManageUserTacacsAccount_Type = TruthValue
_ManageUserTacacsAccount_Object = MibScalar
manageUserTacacsAccount = _ManageUserTacacsAccount_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 5, 6),
    _ManageUserTacacsAccount_Type()
)
manageUserTacacsAccount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    manageUserTacacsAccount.setStatus("current")
_GbnPlatformOAMUpDownLoad_ObjectIdentity = ObjectIdentity
gbnPlatformOAMUpDownLoad = _GbnPlatformOAMUpDownLoad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 6)
)
_LoadTftpAddress_Type = IpAddress
_LoadTftpAddress_Object = MibScalar
loadTftpAddress = _LoadTftpAddress_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 6, 1),
    _LoadTftpAddress_Type()
)
loadTftpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadTftpAddress.setStatus("current")


class _LoadTftpFileName_Type(DisplayString):
    """Custom type loadTftpFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_LoadTftpFileName_Type.__name__ = "DisplayString"
_LoadTftpFileName_Object = MibScalar
loadTftpFileName = _LoadTftpFileName_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 6, 2),
    _LoadTftpFileName_Type()
)
loadTftpFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadTftpFileName.setStatus("current")


class _LoadType_Type(Integer32):
    """Custom type loadType based on Integer32"""
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
        *(("alarm", 5),
          ("application", 1),
          ("bootCode", 4),
          ("configuration", 3),
          ("normalBootRom", 2),
          ("syslog", 6),
          ("wholeBootRom", 7))
    )


_LoadType_Type.__name__ = "Integer32"
_LoadType_Object = MibScalar
loadType = _LoadType_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 6, 3),
    _LoadType_Type()
)
loadType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadType.setStatus("current")


class _LoadExecute_Type(Integer32):
    """Custom type loadExecute based on Integer32"""
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
        *(("downloadFtp", 4),
          ("downloadTftp", 2),
          ("downloadXmodem", 6),
          ("noop", 1),
          ("uploadFtp", 5),
          ("uploadTftp", 3))
    )


_LoadExecute_Type.__name__ = "Integer32"
_LoadExecute_Object = MibScalar
loadExecute = _LoadExecute_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 6, 4),
    _LoadExecute_Type()
)
loadExecute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadExecute.setStatus("current")


class _LoadExecuteStatus_Type(Integer32):
    """Custom type loadExecuteStatus based on Integer32"""
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
              16)
        )
    )
    namedValues = NamedValues(
        *(("errorConnectionFtp", 9),
          ("errorConnectionTftp", 4),
          ("errorConnectionXmodem", 14),
          ("errorFaultFtp", 11),
          ("errorFaultTftp", 6),
          ("errorFaultXmodem", 16),
          ("errorFilenameFtp", 10),
          ("errorFilenameTftp", 5),
          ("errorFilenameXmodem", 15),
          ("inProgressFtp", 7),
          ("inProgressTftp", 2),
          ("inProgressXmodem", 12),
          ("notStarted", 1),
          ("successFtp", 8),
          ("successTftp", 3),
          ("successXmodem", 13))
    )


_LoadExecuteStatus_Type.__name__ = "Integer32"
_LoadExecuteStatus_Object = MibScalar
loadExecuteStatus = _LoadExecuteStatus_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 6, 5),
    _LoadExecuteStatus_Type()
)
loadExecuteStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loadExecuteStatus.setStatus("current")
_LoadFtpAddress_Type = IpAddress
_LoadFtpAddress_Object = MibScalar
loadFtpAddress = _LoadFtpAddress_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 6, 6),
    _LoadFtpAddress_Type()
)
loadFtpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadFtpAddress.setStatus("current")


class _LoadFtpFileName_Type(DisplayString):
    """Custom type loadFtpFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_LoadFtpFileName_Type.__name__ = "DisplayString"
_LoadFtpFileName_Object = MibScalar
loadFtpFileName = _LoadFtpFileName_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 6, 7),
    _LoadFtpFileName_Type()
)
loadFtpFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadFtpFileName.setStatus("current")


class _LoadFtpUserName_Type(DisplayString):
    """Custom type loadFtpUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_LoadFtpUserName_Type.__name__ = "DisplayString"
_LoadFtpUserName_Object = MibScalar
loadFtpUserName = _LoadFtpUserName_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 6, 8),
    _LoadFtpUserName_Type()
)
loadFtpUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadFtpUserName.setStatus("current")


class _LoadFtpUserPassword_Type(DisplayString):
    """Custom type loadFtpUserPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_LoadFtpUserPassword_Type.__name__ = "DisplayString"
_LoadFtpUserPassword_Object = MibScalar
loadFtpUserPassword = _LoadFtpUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 6, 9),
    _LoadFtpUserPassword_Type()
)
loadFtpUserPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadFtpUserPassword.setStatus("current")
_GbnPlatformOAMSnmp_ObjectIdentity = ObjectIdentity
gbnPlatformOAMSnmp = _GbnPlatformOAMSnmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 7)
)
_SnmpCommunityToViewTable_Object = MibTable
snmpCommunityToViewTable = _SnmpCommunityToViewTable_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 7, 1)
)
if mibBuilder.loadTexts:
    snmpCommunityToViewTable.setStatus("current")
_SnmpCommunityToViewEntry_Object = MibTableRow
snmpCommunityToViewEntry = _SnmpCommunityToViewEntry_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 7, 1, 1)
)
snmpCommunityToViewEntry.setIndexNames(
    (0, "GBNPlatformOAM-MIB", "snmpComm2ViewIndex"),
)
if mibBuilder.loadTexts:
    snmpCommunityToViewEntry.setStatus("current")


class _SnmpComm2ViewIndex_Type(Integer32):
    """Custom type snmpComm2ViewIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_SnmpComm2ViewIndex_Type.__name__ = "Integer32"
_SnmpComm2ViewIndex_Object = MibTableColumn
snmpComm2ViewIndex = _SnmpComm2ViewIndex_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 7, 1, 1, 1),
    _SnmpComm2ViewIndex_Type()
)
snmpComm2ViewIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    snmpComm2ViewIndex.setStatus("current")


class _SnmpComm2ViewCommName_Type(DisplayString):
    """Custom type snmpComm2ViewCommName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_SnmpComm2ViewCommName_Type.__name__ = "DisplayString"
_SnmpComm2ViewCommName_Object = MibTableColumn
snmpComm2ViewCommName = _SnmpComm2ViewCommName_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 7, 1, 1, 2),
    _SnmpComm2ViewCommName_Type()
)
snmpComm2ViewCommName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpComm2ViewCommName.setStatus("current")


class _SnmpComm2ViewViewName_Type(SnmpAdminString):
    """Custom type snmpComm2ViewViewName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SnmpComm2ViewViewName_Type.__name__ = "SnmpAdminString"
_SnmpComm2ViewViewName_Object = MibTableColumn
snmpComm2ViewViewName = _SnmpComm2ViewViewName_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 7, 1, 1, 3),
    _SnmpComm2ViewViewName_Type()
)
snmpComm2ViewViewName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpComm2ViewViewName.setStatus("current")


class _SnmpComm2ViewPermission_Type(Integer32):
    """Custom type snmpComm2ViewPermission based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("readOnly", 1),
          ("readWrite", 2))
    )


_SnmpComm2ViewPermission_Type.__name__ = "Integer32"
_SnmpComm2ViewPermission_Object = MibTableColumn
snmpComm2ViewPermission = _SnmpComm2ViewPermission_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 7, 1, 1, 4),
    _SnmpComm2ViewPermission_Type()
)
snmpComm2ViewPermission.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpComm2ViewPermission.setStatus("current")
_SnmpComm2ViewRowStatus_Type = RowStatus
_SnmpComm2ViewRowStatus_Object = MibTableColumn
snmpComm2ViewRowStatus = _SnmpComm2ViewRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 7, 1, 1, 5),
    _SnmpComm2ViewRowStatus_Type()
)
snmpComm2ViewRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpComm2ViewRowStatus.setStatus("current")
_SnmpNotifyTypeTable_Object = MibTable
snmpNotifyTypeTable = _SnmpNotifyTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 7, 2)
)
if mibBuilder.loadTexts:
    snmpNotifyTypeTable.setStatus("current")
_SnmpNotifyTypeEntry_Object = MibTableRow
snmpNotifyTypeEntry = _SnmpNotifyTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 7, 2, 1)
)
snmpNotifyTypeEntry.setIndexNames(
    (0, "GBNPlatformOAM-MIB", "snmpPrivateNotifyType"),
)
if mibBuilder.loadTexts:
    snmpNotifyTypeEntry.setStatus("current")


class _SnmpPrivateNotifyType_Type(DisplayString):
    """Custom type snmpPrivateNotifyType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SnmpPrivateNotifyType_Type.__name__ = "DisplayString"
_SnmpPrivateNotifyType_Object = MibTableColumn
snmpPrivateNotifyType = _SnmpPrivateNotifyType_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 7, 2, 1, 1),
    _SnmpPrivateNotifyType_Type()
)
snmpPrivateNotifyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpPrivateNotifyType.setStatus("current")


class _SnmpNotifyTypeStatus_Type(Integer32):
    """Custom type snmpNotifyTypeStatus based on Integer32"""
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


_SnmpNotifyTypeStatus_Type.__name__ = "Integer32"
_SnmpNotifyTypeStatus_Object = MibTableColumn
snmpNotifyTypeStatus = _SnmpNotifyTypeStatus_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 7, 2, 1, 2),
    _SnmpNotifyTypeStatus_Type()
)
snmpNotifyTypeStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpNotifyTypeStatus.setStatus("current")
_GbnPlatformOAMSnmpNotifyType_ObjectIdentity = ObjectIdentity
gbnPlatformOAMSnmpNotifyType = _GbnPlatformOAMSnmpNotifyType_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 7, 3)
)


class _SnmpTrapSource_Type(Integer32):
    """Custom type snmpTrapSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_SnmpTrapSource_Type.__name__ = "Integer32"
_SnmpTrapSource_Object = MibScalar
snmpTrapSource = _SnmpTrapSource_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 7, 4),
    _SnmpTrapSource_Type()
)
snmpTrapSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapSource.setStatus("current")
_SnmpRemoteEngineTable_Object = MibTable
snmpRemoteEngineTable = _SnmpRemoteEngineTable_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 7, 5)
)
if mibBuilder.loadTexts:
    snmpRemoteEngineTable.setStatus("current")
_SnmpRemoteEngineEntry_Object = MibTableRow
snmpRemoteEngineEntry = _SnmpRemoteEngineEntry_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 7, 5, 1)
)
snmpRemoteEngineEntry.setIndexNames(
    (0, "GBNPlatformOAM-MIB", "snmpRemoteEngineID"),
)
if mibBuilder.loadTexts:
    snmpRemoteEngineEntry.setStatus("current")
_SnmpRemoteEngineID_Type = DisplayString
_SnmpRemoteEngineID_Object = MibTableColumn
snmpRemoteEngineID = _SnmpRemoteEngineID_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 7, 5, 1, 1),
    _SnmpRemoteEngineID_Type()
)
snmpRemoteEngineID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    snmpRemoteEngineID.setStatus("current")


class _SnmpRemoteHostTAddr_Type(OctetString):
    """Custom type snmpRemoteHostTAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_SnmpRemoteHostTAddr_Type.__name__ = "OctetString"
_SnmpRemoteHostTAddr_Object = MibTableColumn
snmpRemoteHostTAddr = _SnmpRemoteHostTAddr_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 7, 5, 1, 2),
    _SnmpRemoteHostTAddr_Type()
)
snmpRemoteHostTAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpRemoteHostTAddr.setStatus("current")


class _SnmpDeleteRemoteEngineTableRow_Type(Integer32):
    """Custom type snmpDeleteRemoteEngineTableRow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("deleteRow", 1)
    )


_SnmpDeleteRemoteEngineTableRow_Type.__name__ = "Integer32"
_SnmpDeleteRemoteEngineTableRow_Object = MibTableColumn
snmpDeleteRemoteEngineTableRow = _SnmpDeleteRemoteEngineTableRow_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 7, 5, 1, 3),
    _SnmpDeleteRemoteEngineTableRow_Type()
)
snmpDeleteRemoteEngineTableRow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpDeleteRemoteEngineTableRow.setStatus("current")


class _SnmpTrapSourceType_Type(Integer32):
    """Custom type snmpTrapSourceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_SnmpTrapSourceType_Type.__name__ = "Integer32"
_SnmpTrapSourceType_Object = MibScalar
snmpTrapSourceType = _SnmpTrapSourceType_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 7, 6),
    _SnmpTrapSourceType_Type()
)
snmpTrapSourceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapSourceType.setStatus("current")
_GbnPlatformOAMSntpClient_ObjectIdentity = ObjectIdentity
gbnPlatformOAMSntpClient = _GbnPlatformOAMSntpClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 8)
)
_GbnPlatformOAMSyslog_ObjectIdentity = ObjectIdentity
gbnPlatformOAMSyslog = _GbnPlatformOAMSyslog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 9)
)
_GbnPlatformOAMPortCar_ObjectIdentity = ObjectIdentity
gbnPlatformOAMPortCar = _GbnPlatformOAMPortCar_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 10)
)
_PortCarTable_Object = MibTable
portCarTable = _PortCarTable_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 10, 1)
)
if mibBuilder.loadTexts:
    portCarTable.setStatus("current")
_PortCarEntry_Object = MibTableRow
portCarEntry = _PortCarEntry_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 10, 1, 1)
)
portCarEntry.setIndexNames(
    (0, "GBNPlatformOAM-MIB", "portCarPort"),
)
if mibBuilder.loadTexts:
    portCarEntry.setStatus("current")
_PortCarPort_Type = Integer32
_PortCarPort_Object = MibTableColumn
portCarPort = _PortCarPort_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 10, 1, 1, 1),
    _PortCarPort_Type()
)
portCarPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    portCarPort.setStatus("current")
_PortCarEnable_Type = TruthValue
_PortCarEnable_Object = MibTableColumn
portCarEnable = _PortCarEnable_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 10, 1, 1, 2),
    _PortCarEnable_Type()
)
portCarEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portCarEnable.setStatus("current")


class _PortDiscardBpdu_Type(Integer32):
    """Custom type portDiscardBpdu based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_PortDiscardBpdu_Type.__name__ = "Integer32"
_PortDiscardBpdu_Object = MibTableColumn
portDiscardBpdu = _PortDiscardBpdu_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 10, 1, 1, 3),
    _PortDiscardBpdu_Type()
)
portDiscardBpdu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portDiscardBpdu.setStatus("current")
_PortCarRateBpdu_Type = Integer32
_PortCarRateBpdu_Object = MibTableColumn
portCarRateBpdu = _PortCarRateBpdu_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 10, 1, 1, 4),
    _PortCarRateBpdu_Type()
)
portCarRateBpdu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portCarRateBpdu.setStatus("current")
_PortCarGlobalEnable_Type = TruthValue
_PortCarGlobalEnable_Object = MibScalar
portCarGlobalEnable = _PortCarGlobalEnable_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 10, 2),
    _PortCarGlobalEnable_Type()
)
portCarGlobalEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portCarGlobalEnable.setStatus("current")
_PortCarOpenTime_Type = Integer32
_PortCarOpenTime_Object = MibScalar
portCarOpenTime = _PortCarOpenTime_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 10, 3),
    _PortCarOpenTime_Type()
)
portCarOpenTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portCarOpenTime.setStatus("current")


class _DiscardBpdu_Type(Integer32):
    """Custom type discardBpdu based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_DiscardBpdu_Type.__name__ = "Integer32"
_DiscardBpdu_Object = MibScalar
discardBpdu = _DiscardBpdu_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 10, 4),
    _DiscardBpdu_Type()
)
discardBpdu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    discardBpdu.setStatus("current")
_PortCarRate_Type = Integer32
_PortCarRate_Object = MibScalar
portCarRate = _PortCarRate_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 10, 5),
    _PortCarRate_Type()
)
portCarRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portCarRate.setStatus("current")
_GbnPlatformOAMSsh_ObjectIdentity = ObjectIdentity
gbnPlatformOAMSsh = _GbnPlatformOAMSsh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 11)
)
_GbnPlatformOAMMailalarm_ObjectIdentity = ObjectIdentity
gbnPlatformOAMMailalarm = _GbnPlatformOAMMailalarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 12)
)
_GbnPlatformOAMVctRun_ObjectIdentity = ObjectIdentity
gbnPlatformOAMVctRun = _GbnPlatformOAMVctRun_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 13)
)
_VctRunTable_Object = MibTable
vctRunTable = _VctRunTable_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 13, 1)
)
if mibBuilder.loadTexts:
    vctRunTable.setStatus("current")
_VctRunEntry_Object = MibTableRow
vctRunEntry = _VctRunEntry_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 13, 1, 1)
)
vctRunEntry.setIndexNames(
    (0, "GBNPlatformOAM-MIB", "vctRunPort"),
)
if mibBuilder.loadTexts:
    vctRunEntry.setStatus("current")


class _VctRunPort_Type(Integer32):
    """Custom type vctRunPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_VctRunPort_Type.__name__ = "Integer32"
_VctRunPort_Object = MibTableColumn
vctRunPort = _VctRunPort_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 13, 1, 1, 1),
    _VctRunPort_Type()
)
vctRunPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vctRunPort.setStatus("current")
_VctRunEnable_Type = TruthValue
_VctRunEnable_Object = MibTableColumn
vctRunEnable = _VctRunEnable_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 13, 1, 1, 2),
    _VctRunEnable_Type()
)
vctRunEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vctRunEnable.setStatus("current")
_VctAutoRunEnable_Type = TruthValue
_VctAutoRunEnable_Object = MibTableColumn
vctAutoRunEnable = _VctAutoRunEnable_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 13, 1, 1, 3),
    _VctAutoRunEnable_Type()
)
vctAutoRunEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vctAutoRunEnable.setStatus("current")
_VctAutoRunGlobalEnable_Type = TruthValue
_VctAutoRunGlobalEnable_Object = MibScalar
vctAutoRunGlobalEnable = _VctAutoRunGlobalEnable_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 13, 2),
    _VctAutoRunGlobalEnable_Type()
)
vctAutoRunGlobalEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vctAutoRunGlobalEnable.setStatus("current")
_GbnPlatformOAMVctRunResult_ObjectIdentity = ObjectIdentity
gbnPlatformOAMVctRunResult = _GbnPlatformOAMVctRunResult_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 14)
)
_VctRunResultTable_Object = MibTable
vctRunResultTable = _VctRunResultTable_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 14, 1)
)
if mibBuilder.loadTexts:
    vctRunResultTable.setStatus("current")
_VctRunResultEntry_Object = MibTableRow
vctRunResultEntry = _VctRunResultEntry_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 14, 1, 1)
)
vctRunResultEntry.setIndexNames(
    (0, "GBNPlatformOAM-MIB", "vctRunResultPort"),
    (0, "GBNPlatformOAM-MIB", "vctRunResultTxRxPairNo"),
)
if mibBuilder.loadTexts:
    vctRunResultEntry.setStatus("current")


class _VctRunResultPort_Type(Integer32):
    """Custom type vctRunResultPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_VctRunResultPort_Type.__name__ = "Integer32"
_VctRunResultPort_Object = MibTableColumn
vctRunResultPort = _VctRunResultPort_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 14, 1, 1, 1),
    _VctRunResultPort_Type()
)
vctRunResultPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vctRunResultPort.setStatus("current")
_VctRunResultTxRxPairNo_Type = VctRunResultTxRxPairNoType
_VctRunResultTxRxPairNo_Object = MibTableColumn
vctRunResultTxRxPairNo = _VctRunResultTxRxPairNo_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 14, 1, 1, 2),
    _VctRunResultTxRxPairNo_Type()
)
vctRunResultTxRxPairNo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vctRunResultTxRxPairNo.setStatus("current")
_VctRunResultStatus_Type = VctRunResultStatusType
_VctRunResultStatus_Object = MibTableColumn
vctRunResultStatus = _VctRunResultStatus_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 14, 1, 1, 3),
    _VctRunResultStatus_Type()
)
vctRunResultStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vctRunResultStatus.setStatus("current")
_VctRunResultErrorLocation_Type = Integer32
_VctRunResultErrorLocation_Object = MibTableColumn
vctRunResultErrorLocation = _VctRunResultErrorLocation_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 14, 1, 1, 4),
    _VctRunResultErrorLocation_Type()
)
vctRunResultErrorLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vctRunResultErrorLocation.setStatus("current")

# Managed Objects groups


# Notification objects

cpuBusyTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 2, 24, 1)
)
if mibBuilder.loadTexts:
    cpuBusyTrap.setStatus(
        "current"
    )

cpuUnbusyTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 2, 24, 2)
)
if mibBuilder.loadTexts:
    cpuUnbusyTrap.setStatus(
        "current"
    )

snmpNotifyTypeSaveConfiguration = NotificationType(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 7, 3, 1)
)
if mibBuilder.loadTexts:
    snmpNotifyTypeSaveConfiguration.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "GBNPlatformOAM-MIB",
    **{"VctRunResultTxRxPairNoType": VctRunResultTxRxPairNoType,
       "VctRunResultStatusType": VctRunResultStatusType,
       "gbnPlatformOAM": gbnPlatformOAM,
       "gbnPlatformOAMSysIf": gbnPlatformOAMSysIf,
       "sysIfMACAddr": sysIfMACAddr,
       "sysIfIpAddress": sysIfIpAddress,
       "sysIfIPGateAddress": sysIfIPGateAddress,
       "sysIfIPNetMask": sysIfIPNetMask,
       "sysIfIPStatus": sysIfIPStatus,
       "sysIfBOOTPOnOff": sysIfBOOTPOnOff,
       "sysIfDHCPOnOff": sysIfDHCPOnOff,
       "sysIfManageVLANTbale": sysIfManageVLANTbale,
       "sysIfManageVLANEntry": sysIfManageVLANEntry,
       "sysIfManageVLANVid": sysIfManageVLANVid,
       "sysIfManageVLANRowStatus": sysIfManageVLANRowStatus,
       "gbnPlatformOAMSystem": gbnPlatformOAMSystem,
       "softwarePlate": softwarePlate,
       "softwareVersion": softwareVersion,
       "softwareCompiledTimeE": softwareCompiledTimeE,
       "softwareCompiledTimeC": softwareCompiledTimeC,
       "cpuDescription": cpuDescription,
       "sdramDescription": sdramDescription,
       "flashDescription": flashDescription,
       "hardwareVersion": hardwareVersion,
       "bootromVersion": bootromVersion,
       "hostName": hostName,
       "cpuIdle": cpuIdle,
       "memorySize": memorySize,
       "memoryIdle": memoryIdle,
       "systemClock": systemClock,
       "clockTime": clockTime,
       "timeZoneName": timeZoneName,
       "timeZoneOffset": timeZoneOffset,
       "offsetNegFlag": offsetNegFlag,
       "productName": productName,
       "systemReset": systemReset,
       "writeConfig": writeConfig,
       "saveNMInterfaceConfig": saveNMInterfaceConfig,
       "nmInterfaceId": nmInterfaceId,
       "nmInterfaceIpAddress": nmInterfaceIpAddress,
       "nmInterfaceNetMask": nmInterfaceNetMask,
       "nmInterfaceGateAddress": nmInterfaceGateAddress,
       "writeNMInterfaceConifig": writeNMInterfaceConifig,
       "writeNMInterfaceConifigStatus": writeNMInterfaceConifigStatus,
       "prodSerialNo": prodSerialNo,
       "cpuBusyStatus": cpuBusyStatus,
       "cpuBusyAlarmEnable": cpuBusyAlarmEnable,
       "cpuBusyThreshold": cpuBusyThreshold,
       "cpuUnbusyThreshold": cpuUnbusyThreshold,
       "cpuStatusTrap": cpuStatusTrap,
       "cpuBusyTrap": cpuBusyTrap,
       "cpuUnbusyTrap": cpuUnbusyTrap,
       "gbnPlatformOAMIpAccessControl": gbnPlatformOAMIpAccessControl,
       "ipAccessControlTable": ipAccessControlTable,
       "ipAccessControlEntry": ipAccessControlEntry,
       "controlIpAddress": controlIpAddress,
       "controlIpMask": controlIpMask,
       "controlTeminal": controlTeminal,
       "controlStatus": controlStatus,
       "gbnPlatformOAMWatchDog": gbnPlatformOAMWatchDog,
       "softDogProxy": softDogProxy,
       "gbnPlatformOAMMuser": gbnPlatformOAMMuser,
       "musrTable": musrTable,
       "musrEntry": musrEntry,
       "musrIndex": musrIndex,
       "musrName": musrName,
       "musrPassword": musrPassword,
       "musrType": musrType,
       "musrRowStatus": musrRowStatus,
       "manageUserAuthenType": manageUserAuthenType,
       "manageUserAuthenRadiusName": manageUserAuthenRadiusName,
       "manageUserAuthChallegeType": manageUserAuthChallegeType,
       "manageUserTacacsAuthor": manageUserTacacsAuthor,
       "manageUserTacacsAccount": manageUserTacacsAccount,
       "gbnPlatformOAMUpDownLoad": gbnPlatformOAMUpDownLoad,
       "loadTftpAddress": loadTftpAddress,
       "loadTftpFileName": loadTftpFileName,
       "loadType": loadType,
       "loadExecute": loadExecute,
       "loadExecuteStatus": loadExecuteStatus,
       "loadFtpAddress": loadFtpAddress,
       "loadFtpFileName": loadFtpFileName,
       "loadFtpUserName": loadFtpUserName,
       "loadFtpUserPassword": loadFtpUserPassword,
       "gbnPlatformOAMSnmp": gbnPlatformOAMSnmp,
       "snmpCommunityToViewTable": snmpCommunityToViewTable,
       "snmpCommunityToViewEntry": snmpCommunityToViewEntry,
       "snmpComm2ViewIndex": snmpComm2ViewIndex,
       "snmpComm2ViewCommName": snmpComm2ViewCommName,
       "snmpComm2ViewViewName": snmpComm2ViewViewName,
       "snmpComm2ViewPermission": snmpComm2ViewPermission,
       "snmpComm2ViewRowStatus": snmpComm2ViewRowStatus,
       "snmpNotifyTypeTable": snmpNotifyTypeTable,
       "snmpNotifyTypeEntry": snmpNotifyTypeEntry,
       "snmpPrivateNotifyType": snmpPrivateNotifyType,
       "snmpNotifyTypeStatus": snmpNotifyTypeStatus,
       "gbnPlatformOAMSnmpNotifyType": gbnPlatformOAMSnmpNotifyType,
       "snmpNotifyTypeSaveConfiguration": snmpNotifyTypeSaveConfiguration,
       "snmpTrapSource": snmpTrapSource,
       "snmpRemoteEngineTable": snmpRemoteEngineTable,
       "snmpRemoteEngineEntry": snmpRemoteEngineEntry,
       "snmpRemoteEngineID": snmpRemoteEngineID,
       "snmpRemoteHostTAddr": snmpRemoteHostTAddr,
       "snmpDeleteRemoteEngineTableRow": snmpDeleteRemoteEngineTableRow,
       "snmpTrapSourceType": snmpTrapSourceType,
       "gbnPlatformOAMSntpClient": gbnPlatformOAMSntpClient,
       "gbnPlatformOAMSyslog": gbnPlatformOAMSyslog,
       "gbnPlatformOAMPortCar": gbnPlatformOAMPortCar,
       "portCarTable": portCarTable,
       "portCarEntry": portCarEntry,
       "portCarPort": portCarPort,
       "portCarEnable": portCarEnable,
       "portDiscardBpdu": portDiscardBpdu,
       "portCarRateBpdu": portCarRateBpdu,
       "portCarGlobalEnable": portCarGlobalEnable,
       "portCarOpenTime": portCarOpenTime,
       "discardBpdu": discardBpdu,
       "portCarRate": portCarRate,
       "gbnPlatformOAMSsh": gbnPlatformOAMSsh,
       "gbnPlatformOAMMailalarm": gbnPlatformOAMMailalarm,
       "gbnPlatformOAMVctRun": gbnPlatformOAMVctRun,
       "vctRunTable": vctRunTable,
       "vctRunEntry": vctRunEntry,
       "vctRunPort": vctRunPort,
       "vctRunEnable": vctRunEnable,
       "vctAutoRunEnable": vctAutoRunEnable,
       "vctAutoRunGlobalEnable": vctAutoRunGlobalEnable,
       "gbnPlatformOAMVctRunResult": gbnPlatformOAMVctRunResult,
       "vctRunResultTable": vctRunResultTable,
       "vctRunResultEntry": vctRunResultEntry,
       "vctRunResultPort": vctRunResultPort,
       "vctRunResultTxRxPairNo": vctRunResultTxRxPairNo,
       "vctRunResultStatus": vctRunResultStatus,
       "vctRunResultErrorLocation": vctRunResultErrorLocation}
)
