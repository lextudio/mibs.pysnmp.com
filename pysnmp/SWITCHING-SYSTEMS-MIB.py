# SNMP MIB module (SWITCHING-SYSTEMS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SWITCHING-SYSTEMS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:59:22 2024
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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class SwSysStorageType(Integer32):
    """Custom type SwSysStorageType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )





class SwSysAddressType(Integer32):
    """Custom type SwSysAddressType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )





class SwSysResourceType(Integer32):
    """Custom type SwSysResourceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )





class SwSysResourceBitMask(OctetString):
    """Custom type SwSysResourceBitMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )





class IpxNetworkNumber(OctetString):
    """Custom type IpxNetworkNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )





class ATNetworkNumber(OctetString):
    """Custom type ATNetworkNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )





class ATName(OctetString):
    """Custom type ATName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )





class DdpNodeAddress(OctetString):
    """Custom type DdpNodeAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )





class MacAddress(OctetString):
    """Custom type MacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Synernetics_ObjectIdentity = ObjectIdentity
synernetics = _Synernetics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114)
)
_SwitchingSystems_ObjectIdentity = ObjectIdentity
switchingSystems = _SwitchingSystems_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1)
)
_CorebuilderProductsI_ObjectIdentity = ObjectIdentity
corebuilderProductsI = _CorebuilderProductsI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 3)
)
_SwitchingSystemsMib_ObjectIdentity = ObjectIdentity
switchingSystemsMib = _SwitchingSystemsMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 4)
)
_SwSysSystem_ObjectIdentity = ObjectIdentity
swSysSystem = _SwSysSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 1)
)
_SwSysSystemId_Type = Integer32
_SwSysSystemId_Object = MibScalar
swSysSystemId = _SwSysSystemId_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 1, 1),
    _SwSysSystemId_Type()
)
swSysSystemId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysSystemId.setStatus("mandatory")


class _SwSysSystemType_Type(Integer32):
    """Custom type swSysSystemType based on Integer32"""
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
        *(("coreBuilder3500", 4),
          ("coreBuilder9400", 5),
          ("lanplex2000", 3),
          ("lanplex6000", 2),
          ("other", 1),
          ("superStack3900", 6),
          ("superStack9300", 7))
    )


_SwSysSystemType_Type.__name__ = "Integer32"
_SwSysSystemType_Object = MibScalar
swSysSystemType = _SwSysSystemType_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 1, 2),
    _SwSysSystemType_Type()
)
swSysSystemType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysSystemType.setStatus("mandatory")


class _SwSysSystemName_Type(DisplayString):
    """Custom type swSysSystemName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_SwSysSystemName_Type.__name__ = "DisplayString"
_SwSysSystemName_Object = MibScalar
swSysSystemName = _SwSysSystemName_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 1, 3),
    _SwSysSystemName_Type()
)
swSysSystemName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSysSystemName.setStatus("mandatory")


class _SwSysSystemManufacturer_Type(DisplayString):
    """Custom type swSysSystemManufacturer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_SwSysSystemManufacturer_Type.__name__ = "DisplayString"
_SwSysSystemManufacturer_Object = MibScalar
swSysSystemManufacturer = _SwSysSystemManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 1, 4),
    _SwSysSystemManufacturer_Type()
)
swSysSystemManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysSystemManufacturer.setStatus("mandatory")


class _SwSysSystemHardwareRevision_Type(OctetString):
    """Custom type swSysSystemHardwareRevision based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_SwSysSystemHardwareRevision_Type.__name__ = "OctetString"
_SwSysSystemHardwareRevision_Object = MibScalar
swSysSystemHardwareRevision = _SwSysSystemHardwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 1, 5),
    _SwSysSystemHardwareRevision_Type()
)
swSysSystemHardwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysSystemHardwareRevision.setStatus("mandatory")
_SwSysSystemMemorySize_Type = Integer32
_SwSysSystemMemorySize_Object = MibScalar
swSysSystemMemorySize = _SwSysSystemMemorySize_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 1, 6),
    _SwSysSystemMemorySize_Type()
)
swSysSystemMemorySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysSystemMemorySize.setStatus("mandatory")
_SwSysSystemFlashMemorySize_Type = Integer32
_SwSysSystemFlashMemorySize_Object = MibScalar
swSysSystemFlashMemorySize = _SwSysSystemFlashMemorySize_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 1, 7),
    _SwSysSystemFlashMemorySize_Type()
)
swSysSystemFlashMemorySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysSystemFlashMemorySize.setStatus("mandatory")
_SwSysSystemNvMemorySize_Type = Integer32
_SwSysSystemNvMemorySize_Object = MibScalar
swSysSystemNvMemorySize = _SwSysSystemNvMemorySize_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 1, 8),
    _SwSysSystemNvMemorySize_Type()
)
swSysSystemNvMemorySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysSystemNvMemorySize.setStatus("mandatory")


class _SwSysSystemSoftwareRevision_Type(OctetString):
    """Custom type swSysSystemSoftwareRevision based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_SwSysSystemSoftwareRevision_Type.__name__ = "OctetString"
_SwSysSystemSoftwareRevision_Object = MibScalar
swSysSystemSoftwareRevision = _SwSysSystemSoftwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 1, 9),
    _SwSysSystemSoftwareRevision_Type()
)
swSysSystemSoftwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysSystemSoftwareRevision.setStatus("mandatory")


class _SwSysSystemBuildTime_Type(DisplayString):
    """Custom type swSysSystemBuildTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_SwSysSystemBuildTime_Type.__name__ = "DisplayString"
_SwSysSystemBuildTime_Object = MibScalar
swSysSystemBuildTime = _SwSysSystemBuildTime_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 1, 10),
    _SwSysSystemBuildTime_Type()
)
swSysSystemBuildTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysSystemBuildTime.setStatus("mandatory")
_SwSysSystemSnmpRevision_Type = Integer32
_SwSysSystemSnmpRevision_Object = MibScalar
swSysSystemSnmpRevision = _SwSysSystemSnmpRevision_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 1, 11),
    _SwSysSystemSnmpRevision_Type()
)
swSysSystemSnmpRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysSystemSnmpRevision.setStatus("mandatory")


class _SwSysSystemRequestedSnmpMode_Type(Integer32):
    """Custom type swSysSystemRequestedSnmpMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("multiAgentMode", 2),
          ("singleAgentMode", 1))
    )


_SwSysSystemRequestedSnmpMode_Type.__name__ = "Integer32"
_SwSysSystemRequestedSnmpMode_Object = MibScalar
swSysSystemRequestedSnmpMode = _SwSysSystemRequestedSnmpMode_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 1, 12),
    _SwSysSystemRequestedSnmpMode_Type()
)
swSysSystemRequestedSnmpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSysSystemRequestedSnmpMode.setStatus("mandatory")


class _SwSysSystemCurrentSnmpMode_Type(Integer32):
    """Custom type swSysSystemCurrentSnmpMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("multiAgentMode", 2),
          ("singleAgentMode", 1))
    )


_SwSysSystemCurrentSnmpMode_Type.__name__ = "Integer32"
_SwSysSystemCurrentSnmpMode_Object = MibScalar
swSysSystemCurrentSnmpMode = _SwSysSystemCurrentSnmpMode_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 1, 13),
    _SwSysSystemCurrentSnmpMode_Type()
)
swSysSystemCurrentSnmpMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysSystemCurrentSnmpMode.setStatus("mandatory")


class _SwSysSystemAction_Type(Integer32):
    """Custom type swSysSystemAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("nvReset", 3),
          ("other", 1),
          ("reset", 2))
    )


_SwSysSystemAction_Type.__name__ = "Integer32"
_SwSysSystemAction_Object = MibScalar
swSysSystemAction = _SwSysSystemAction_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 1, 14),
    _SwSysSystemAction_Type()
)
swSysSystemAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSysSystemAction.setStatus("mandatory")


class _SwSysSystemOvertemperature_Type(Integer32):
    """Custom type swSysSystemOvertemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("notSupported", 3),
          ("true", 1))
    )


_SwSysSystemOvertemperature_Type.__name__ = "Integer32"
_SwSysSystemOvertemperature_Object = MibScalar
swSysSystemOvertemperature = _SwSysSystemOvertemperature_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 1, 15),
    _SwSysSystemOvertemperature_Type()
)
swSysSystemOvertemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysSystemOvertemperature.setStatus("mandatory")


class _SwSysSystemFanFailure_Type(Integer32):
    """Custom type swSysSystemFanFailure based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("notSupported", 3),
          ("true", 1))
    )


_SwSysSystemFanFailure_Type.__name__ = "Integer32"
_SwSysSystemFanFailure_Object = MibScalar
swSysSystemFanFailure = _SwSysSystemFanFailure_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 1, 16),
    _SwSysSystemFanFailure_Type()
)
swSysSystemFanFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysSystemFanFailure.setStatus("mandatory")
_SwSysSystemProtocolMask_Type = Integer32
_SwSysSystemProtocolMask_Object = MibScalar
swSysSystemProtocolMask = _SwSysSystemProtocolMask_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 1, 17),
    _SwSysSystemProtocolMask_Type()
)
swSysSystemProtocolMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysSystemProtocolMask.setStatus("mandatory")


class _SwSysSystemConsoleAccess_Type(Integer32):
    """Custom type swSysSystemConsoleAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SwSysSystemConsoleAccess_Type.__name__ = "Integer32"
_SwSysSystemConsoleAccess_Object = MibScalar
swSysSystemConsoleAccess = _SwSysSystemConsoleAccess_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 1, 18),
    _SwSysSystemConsoleAccess_Type()
)
swSysSystemConsoleAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSysSystemConsoleAccess.setStatus("mandatory")


class _SwSysSystemConsoleReadPwd_Type(DisplayString):
    """Custom type swSysSystemConsoleReadPwd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_SwSysSystemConsoleReadPwd_Type.__name__ = "DisplayString"
_SwSysSystemConsoleReadPwd_Object = MibScalar
swSysSystemConsoleReadPwd = _SwSysSystemConsoleReadPwd_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 1, 19),
    _SwSysSystemConsoleReadPwd_Type()
)
swSysSystemConsoleReadPwd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSysSystemConsoleReadPwd.setStatus("mandatory")


class _SwSysSystemConsoleWritePwd_Type(DisplayString):
    """Custom type swSysSystemConsoleWritePwd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_SwSysSystemConsoleWritePwd_Type.__name__ = "DisplayString"
_SwSysSystemConsoleWritePwd_Object = MibScalar
swSysSystemConsoleWritePwd = _SwSysSystemConsoleWritePwd_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 1, 20),
    _SwSysSystemConsoleWritePwd_Type()
)
swSysSystemConsoleWritePwd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSysSystemConsoleWritePwd.setStatus("mandatory")


class _SwSysSystemConsoleAdminPwd_Type(DisplayString):
    """Custom type swSysSystemConsoleAdminPwd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_SwSysSystemConsoleAdminPwd_Type.__name__ = "DisplayString"
_SwSysSystemConsoleAdminPwd_Object = MibScalar
swSysSystemConsoleAdminPwd = _SwSysSystemConsoleAdminPwd_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 1, 21),
    _SwSysSystemConsoleAdminPwd_Type()
)
swSysSystemConsoleAdminPwd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSysSystemConsoleAdminPwd.setStatus("mandatory")
_SwSysSystemDateTime_Type = DisplayString
_SwSysSystemDateTime_Object = MibScalar
swSysSystemDateTime = _SwSysSystemDateTime_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 1, 22),
    _SwSysSystemDateTime_Type()
)
swSysSystemDateTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSysSystemDateTime.setStatus("mandatory")


class _SwSysSystemDSTime_Type(Integer32):
    """Custom type swSysSystemDSTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-120, 120),
    )


_SwSysSystemDSTime_Type.__name__ = "Integer32"
_SwSysSystemDSTime_Object = MibScalar
swSysSystemDSTime = _SwSysSystemDSTime_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 1, 23),
    _SwSysSystemDSTime_Type()
)
swSysSystemDSTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSysSystemDSTime.setStatus("mandatory")


class _SwSysSystemTimeZone_Type(Integer32):
    """Custom type swSysSystemTimeZone based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-720, 720),
    )


_SwSysSystemTimeZone_Type.__name__ = "Integer32"
_SwSysSystemTimeZone_Object = MibScalar
swSysSystemTimeZone = _SwSysSystemTimeZone_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 1, 24),
    _SwSysSystemTimeZone_Type()
)
swSysSystemTimeZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSysSystemTimeZone.setStatus("mandatory")


class _SwSysSystemCurrentFddiStationMode_Type(Integer32):
    """Custom type swSysSystemCurrentFddiStationMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("multiStationMode", 2),
          ("singleStationMode", 1))
    )


_SwSysSystemCurrentFddiStationMode_Type.__name__ = "Integer32"
_SwSysSystemCurrentFddiStationMode_Object = MibScalar
swSysSystemCurrentFddiStationMode = _SwSysSystemCurrentFddiStationMode_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 1, 25),
    _SwSysSystemCurrentFddiStationMode_Type()
)
swSysSystemCurrentFddiStationMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysSystemCurrentFddiStationMode.setStatus("mandatory")


class _SwSysSystemRequestedFddiStationMode_Type(Integer32):
    """Custom type swSysSystemRequestedFddiStationMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("multiStationMode", 2),
          ("singleStationMode", 1))
    )


_SwSysSystemRequestedFddiStationMode_Type.__name__ = "Integer32"
_SwSysSystemRequestedFddiStationMode_Object = MibScalar
swSysSystemRequestedFddiStationMode = _SwSysSystemRequestedFddiStationMode_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 1, 26),
    _SwSysSystemRequestedFddiStationMode_Type()
)
swSysSystemRequestedFddiStationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSysSystemRequestedFddiStationMode.setStatus("mandatory")
_SwSysSystemLog_ObjectIdentity = ObjectIdentity
swSysSystemLog = _SwSysSystemLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 1, 27)
)
_SwSysSystemLogEntryCurrentCount_Type = Integer32
_SwSysSystemLogEntryCurrentCount_Object = MibScalar
swSysSystemLogEntryCurrentCount = _SwSysSystemLogEntryCurrentCount_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 1, 27, 1),
    _SwSysSystemLogEntryCurrentCount_Type()
)
swSysSystemLogEntryCurrentCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysSystemLogEntryCurrentCount.setStatus("mandatory")
_SwSysSystemLogMaxSize_Type = Integer32
_SwSysSystemLogMaxSize_Object = MibScalar
swSysSystemLogMaxSize = _SwSysSystemLogMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 1, 27, 2),
    _SwSysSystemLogMaxSize_Type()
)
swSysSystemLogMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysSystemLogMaxSize.setStatus("mandatory")


class _SwSysSystemLogSeverityThreshold_Type(Integer32):
    """Custom type swSysSystemLogSeverityThreshold based on Integer32"""
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
        *(("error", 3),
          ("fatal", 4),
          ("informational", 1),
          ("warning", 2))
    )


_SwSysSystemLogSeverityThreshold_Type.__name__ = "Integer32"
_SwSysSystemLogSeverityThreshold_Object = MibScalar
swSysSystemLogSeverityThreshold = _SwSysSystemLogSeverityThreshold_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 1, 27, 3),
    _SwSysSystemLogSeverityThreshold_Type()
)
swSysSystemLogSeverityThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSysSystemLogSeverityThreshold.setStatus("mandatory")
_SwSysSystemLogTable_Object = MibTable
swSysSystemLogTable = _SwSysSystemLogTable_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 1, 27, 4)
)
if mibBuilder.loadTexts:
    swSysSystemLogTable.setStatus("mandatory")
_SwSysSystemLogEntry_Object = MibTableRow
swSysSystemLogEntry = _SwSysSystemLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 1, 27, 4, 1)
)
swSysSystemLogEntry.setIndexNames(
    (0, "SWITCHING-SYSTEMS-MIB", "swSysSystemLogIndex"),
)
if mibBuilder.loadTexts:
    swSysSystemLogEntry.setStatus("mandatory")
_SwSysSystemLogIndex_Type = Integer32
_SwSysSystemLogIndex_Object = MibTableColumn
swSysSystemLogIndex = _SwSysSystemLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 1, 27, 4, 1, 1),
    _SwSysSystemLogIndex_Type()
)
swSysSystemLogIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysSystemLogIndex.setStatus("mandatory")


class _SwSysSystemLogSeverityLevel_Type(Integer32):
    """Custom type swSysSystemLogSeverityLevel based on Integer32"""
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
        *(("error", 3),
          ("fatal", 4),
          ("information", 1),
          ("warning", 2))
    )


_SwSysSystemLogSeverityLevel_Type.__name__ = "Integer32"
_SwSysSystemLogSeverityLevel_Object = MibTableColumn
swSysSystemLogSeverityLevel = _SwSysSystemLogSeverityLevel_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 1, 27, 4, 1, 2),
    _SwSysSystemLogSeverityLevel_Type()
)
swSysSystemLogSeverityLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysSystemLogSeverityLevel.setStatus("mandatory")
_SwSysSystemLogDateTime_Type = DisplayString
_SwSysSystemLogDateTime_Object = MibTableColumn
swSysSystemLogDateTime = _SwSysSystemLogDateTime_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 1, 27, 4, 1, 3),
    _SwSysSystemLogDateTime_Type()
)
swSysSystemLogDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysSystemLogDateTime.setStatus("mandatory")


class _SwSysSystemLogFacility_Type(Integer32):
    """Custom type swSysSystemLogFacility based on Integer32"""
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
        *(("assertion", 3),
          ("efsm", 10),
          ("esm", 8),
          ("exception", 1),
          ("fcmlmm", 5),
          ("fsm", 11),
          ("hsi", 12),
          ("lmmboard", 7),
          ("lmmfddi", 6),
          ("operatingSystem", 2),
          ("spanningTree", 4),
          ("trsm", 9))
    )


_SwSysSystemLogFacility_Type.__name__ = "Integer32"
_SwSysSystemLogFacility_Object = MibTableColumn
swSysSystemLogFacility = _SwSysSystemLogFacility_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 1, 27, 4, 1, 4),
    _SwSysSystemLogFacility_Type()
)
swSysSystemLogFacility.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysSystemLogFacility.setStatus("mandatory")
_SwSysSystemLogMessage_Type = DisplayString
_SwSysSystemLogMessage_Object = MibTableColumn
swSysSystemLogMessage = _SwSysSystemLogMessage_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 1, 27, 4, 1, 5),
    _SwSysSystemLogMessage_Type()
)
swSysSystemLogMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysSystemLogMessage.setStatus("mandatory")
_SwSysSystemBaseMACAddress_Type = MacAddress
_SwSysSystemBaseMACAddress_Object = MibScalar
swSysSystemBaseMACAddress = _SwSysSystemBaseMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 1, 28),
    _SwSysSystemBaseMACAddress_Type()
)
swSysSystemBaseMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysSystemBaseMACAddress.setStatus("mandatory")
_SwSysSystemMACAddressCount_Type = Integer32
_SwSysSystemMACAddressCount_Object = MibScalar
swSysSystemMACAddressCount = _SwSysSystemMACAddressCount_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 1, 29),
    _SwSysSystemMACAddressCount_Type()
)
swSysSystemMACAddressCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysSystemMACAddressCount.setStatus("mandatory")


class _SwSysSystemChassisSerialNumber_Type(DisplayString):
    """Custom type swSysSystemChassisSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )


_SwSysSystemChassisSerialNumber_Type.__name__ = "DisplayString"
_SwSysSystemChassisSerialNumber_Object = MibScalar
swSysSystemChassisSerialNumber = _SwSysSystemChassisSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 1, 30),
    _SwSysSystemChassisSerialNumber_Type()
)
swSysSystemChassisSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysSystemChassisSerialNumber.setStatus("mandatory")
_SwSysSystemFPMemorySize_Type = Integer32
_SwSysSystemFPMemorySize_Object = MibScalar
swSysSystemFPMemorySize = _SwSysSystemFPMemorySize_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 1, 31),
    _SwSysSystemFPMemorySize_Type()
)
swSysSystemFPMemorySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysSystemFPMemorySize.setStatus("mandatory")
_SwSysSystemBufferSize_Type = Integer32
_SwSysSystemBufferSize_Object = MibScalar
swSysSystemBufferSize = _SwSysSystemBufferSize_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 1, 32),
    _SwSysSystemBufferSize_Type()
)
swSysSystemBufferSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysSystemBufferSize.setStatus("mandatory")
_SwSysSlot_ObjectIdentity = ObjectIdentity
swSysSlot = _SwSysSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 2)
)
_SwSysSlotCount_Type = Integer32
_SwSysSlotCount_Object = MibScalar
swSysSlotCount = _SwSysSlotCount_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 2, 1),
    _SwSysSlotCount_Type()
)
swSysSlotCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysSlotCount.setStatus("mandatory")
_SwSysSlotTable_Object = MibTable
swSysSlotTable = _SwSysSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 2, 2)
)
if mibBuilder.loadTexts:
    swSysSlotTable.setStatus("mandatory")
_SwSysSlotEntry_Object = MibTableRow
swSysSlotEntry = _SwSysSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 2, 2, 1)
)
swSysSlotEntry.setIndexNames(
    (0, "SWITCHING-SYSTEMS-MIB", "swSysSlotIndex"),
)
if mibBuilder.loadTexts:
    swSysSlotEntry.setStatus("mandatory")
_SwSysSlotIndex_Type = Integer32
_SwSysSlotIndex_Object = MibTableColumn
swSysSlotIndex = _SwSysSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 2, 2, 1, 1),
    _SwSysSlotIndex_Type()
)
swSysSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysSlotIndex.setStatus("mandatory")


class _SwSysSlotBoardType_Type(Integer32):
    """Custom type swSysSlotBoardType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14)
        )
    )
    namedValues = NamedValues(
        *(("efsmBoard", 10),
          ("emptyLocation", 2),
          ("esmBoard", 7),
          ("fcmBoard", 8),
          ("fesmBoard", 14),
          ("fsmBoard", 13),
          ("lmmBoard", 9),
          ("other", 1),
          ("tmmBoard", 12),
          ("trsmBoard", 11))
    )


_SwSysSlotBoardType_Type.__name__ = "Integer32"
_SwSysSlotBoardType_Object = MibTableColumn
swSysSlotBoardType = _SwSysSlotBoardType_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 2, 2, 1, 2),
    _SwSysSlotBoardType_Type()
)
swSysSlotBoardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysSlotBoardType.setStatus("mandatory")


class _SwSysSlotBoardRevision_Type(OctetString):
    """Custom type swSysSlotBoardRevision based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1),
    )


_SwSysSlotBoardRevision_Type.__name__ = "OctetString"
_SwSysSlotBoardRevision_Object = MibTableColumn
swSysSlotBoardRevision = _SwSysSlotBoardRevision_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 2, 2, 1, 3),
    _SwSysSlotBoardRevision_Type()
)
swSysSlotBoardRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysSlotBoardRevision.setStatus("mandatory")


class _SwSysSlotBoardStatus_Type(Integer32):
    """Custom type swSysSlotBoardStatus based on Integer32"""
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
        *(("notPresent", 1),
          ("offline", 3),
          ("online", 4),
          ("testing", 2))
    )


_SwSysSlotBoardStatus_Type.__name__ = "Integer32"
_SwSysSlotBoardStatus_Object = MibTableColumn
swSysSlotBoardStatus = _SwSysSlotBoardStatus_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 2, 2, 1, 4),
    _SwSysSlotBoardStatus_Type()
)
swSysSlotBoardStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysSlotBoardStatus.setStatus("mandatory")


class _SwSysSlotBoardName_Type(DisplayString):
    """Custom type swSysSlotBoardName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SwSysSlotBoardName_Type.__name__ = "DisplayString"
_SwSysSlotBoardName_Object = MibTableColumn
swSysSlotBoardName = _SwSysSlotBoardName_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 2, 2, 1, 5),
    _SwSysSlotBoardName_Type()
)
swSysSlotBoardName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysSlotBoardName.setStatus("mandatory")


class _SwSysSlotBoardNameAbbrev_Type(DisplayString):
    """Custom type swSysSlotBoardNameAbbrev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_SwSysSlotBoardNameAbbrev_Type.__name__ = "DisplayString"
_SwSysSlotBoardNameAbbrev_Object = MibTableColumn
swSysSlotBoardNameAbbrev = _SwSysSlotBoardNameAbbrev_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 2, 2, 1, 6),
    _SwSysSlotBoardNameAbbrev_Type()
)
swSysSlotBoardNameAbbrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysSlotBoardNameAbbrev.setStatus("mandatory")
_SwSysSlotEthernetPortCount_Type = Integer32
_SwSysSlotEthernetPortCount_Object = MibTableColumn
swSysSlotEthernetPortCount = _SwSysSlotEthernetPortCount_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 2, 2, 1, 7),
    _SwSysSlotEthernetPortCount_Type()
)
swSysSlotEthernetPortCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysSlotEthernetPortCount.setStatus("mandatory")
_SwSysSlotFddiMacCount_Type = Integer32
_SwSysSlotFddiMacCount_Object = MibTableColumn
swSysSlotFddiMacCount = _SwSysSlotFddiMacCount_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 2, 2, 1, 8),
    _SwSysSlotFddiMacCount_Type()
)
swSysSlotFddiMacCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysSlotFddiMacCount.setStatus("mandatory")
_SwSysSlotFddiPortCount_Type = Integer32
_SwSysSlotFddiPortCount_Object = MibTableColumn
swSysSlotFddiPortCount = _SwSysSlotFddiPortCount_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 2, 2, 1, 9),
    _SwSysSlotFddiPortCount_Type()
)
swSysSlotFddiPortCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysSlotFddiPortCount.setStatus("mandatory")


class _SwSysSlotOvertemperature_Type(Integer32):
    """Custom type swSysSlotOvertemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("notSupported", 3),
          ("true", 1))
    )


_SwSysSlotOvertemperature_Type.__name__ = "Integer32"
_SwSysSlotOvertemperature_Object = MibTableColumn
swSysSlotOvertemperature = _SwSysSlotOvertemperature_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 2, 2, 1, 10),
    _SwSysSlotOvertemperature_Type()
)
swSysSlotOvertemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysSlotOvertemperature.setStatus("mandatory")
_SwSysSlotTokenRingPortCount_Type = Integer32
_SwSysSlotTokenRingPortCount_Object = MibTableColumn
swSysSlotTokenRingPortCount = _SwSysSlotTokenRingPortCount_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 2, 2, 1, 11),
    _SwSysSlotTokenRingPortCount_Type()
)
swSysSlotTokenRingPortCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysSlotTokenRingPortCount.setStatus("mandatory")


class _SwSysSlotBoardRevStr_Type(DisplayString):
    """Custom type swSysSlotBoardRevStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_SwSysSlotBoardRevStr_Type.__name__ = "DisplayString"
_SwSysSlotBoardRevStr_Object = MibTableColumn
swSysSlotBoardRevStr = _SwSysSlotBoardRevStr_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 2, 2, 1, 12),
    _SwSysSlotBoardRevStr_Type()
)
swSysSlotBoardRevStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysSlotBoardRevStr.setStatus("mandatory")


class _SwSysSlotConverterBad_Type(Integer32):
    """Custom type swSysSlotConverterBad based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("notSupported", 3),
          ("true", 1))
    )


_SwSysSlotConverterBad_Type.__name__ = "Integer32"
_SwSysSlotConverterBad_Object = MibTableColumn
swSysSlotConverterBad = _SwSysSlotConverterBad_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 2, 2, 1, 13),
    _SwSysSlotConverterBad_Type()
)
swSysSlotConverterBad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysSlotConverterBad.setStatus("mandatory")
_SwSysControlPanel_ObjectIdentity = ObjectIdentity
swSysControlPanel = _SwSysControlPanel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 3)
)


class _SwSysControlPanelHardwareRevision_Type(OctetString):
    """Custom type swSysControlPanelHardwareRevision based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_SwSysControlPanelHardwareRevision_Type.__name__ = "OctetString"
_SwSysControlPanelHardwareRevision_Object = MibScalar
swSysControlPanelHardwareRevision = _SwSysControlPanelHardwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 3, 1),
    _SwSysControlPanelHardwareRevision_Type()
)
swSysControlPanelHardwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysControlPanelHardwareRevision.setStatus("mandatory")


class _SwSysControlPanelSoftwareRevision_Type(OctetString):
    """Custom type swSysControlPanelSoftwareRevision based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_SwSysControlPanelSoftwareRevision_Type.__name__ = "OctetString"
_SwSysControlPanelSoftwareRevision_Object = MibScalar
swSysControlPanelSoftwareRevision = _SwSysControlPanelSoftwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 3, 2),
    _SwSysControlPanelSoftwareRevision_Type()
)
swSysControlPanelSoftwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysControlPanelSoftwareRevision.setStatus("mandatory")
_SwSysControlPanelLines_Type = Integer32
_SwSysControlPanelLines_Object = MibScalar
swSysControlPanelLines = _SwSysControlPanelLines_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 3, 3),
    _SwSysControlPanelLines_Type()
)
swSysControlPanelLines.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysControlPanelLines.setStatus("mandatory")
_SwSysControlPanelColumns_Type = Integer32
_SwSysControlPanelColumns_Object = MibScalar
swSysControlPanelColumns = _SwSysControlPanelColumns_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 3, 4),
    _SwSysControlPanelColumns_Type()
)
swSysControlPanelColumns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysControlPanelColumns.setStatus("mandatory")


class _SwSysControlPanelText_Type(OctetString):
    """Custom type swSysControlPanelText based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_SwSysControlPanelText_Type.__name__ = "OctetString"
_SwSysControlPanelText_Object = MibScalar
swSysControlPanelText = _SwSysControlPanelText_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 3, 5),
    _SwSysControlPanelText_Type()
)
swSysControlPanelText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysControlPanelText.setStatus("mandatory")


class _SwSysControlPanelAccess_Type(Integer32):
    """Custom type swSysControlPanelAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SwSysControlPanelAccess_Type.__name__ = "Integer32"
_SwSysControlPanelAccess_Object = MibScalar
swSysControlPanelAccess = _SwSysControlPanelAccess_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 3, 6),
    _SwSysControlPanelAccess_Type()
)
swSysControlPanelAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSysControlPanelAccess.setStatus("mandatory")
_SwSysPowerSupply_ObjectIdentity = ObjectIdentity
swSysPowerSupply = _SwSysPowerSupply_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 4)
)
_SwSysPowerSupplyCount_Type = Integer32
_SwSysPowerSupplyCount_Object = MibScalar
swSysPowerSupplyCount = _SwSysPowerSupplyCount_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 4, 1),
    _SwSysPowerSupplyCount_Type()
)
swSysPowerSupplyCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysPowerSupplyCount.setStatus("mandatory")
_SwSysPowerSupplyStatusTable_Object = MibTable
swSysPowerSupplyStatusTable = _SwSysPowerSupplyStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 4, 2)
)
if mibBuilder.loadTexts:
    swSysPowerSupplyStatusTable.setStatus("mandatory")
_SwSysPowerSupplyStatusEntry_Object = MibTableRow
swSysPowerSupplyStatusEntry = _SwSysPowerSupplyStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 4, 2, 1)
)
swSysPowerSupplyStatusEntry.setIndexNames(
    (0, "SWITCHING-SYSTEMS-MIB", "swSysPowerSupplyStatusIndex"),
)
if mibBuilder.loadTexts:
    swSysPowerSupplyStatusEntry.setStatus("mandatory")
_SwSysPowerSupplyStatusIndex_Type = Integer32
_SwSysPowerSupplyStatusIndex_Object = MibTableColumn
swSysPowerSupplyStatusIndex = _SwSysPowerSupplyStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 4, 2, 1, 1),
    _SwSysPowerSupplyStatusIndex_Type()
)
swSysPowerSupplyStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysPowerSupplyStatusIndex.setStatus("mandatory")
_SwSysPowerSupplyStatus_Type = Integer32
_SwSysPowerSupplyStatus_Object = MibTableColumn
swSysPowerSupplyStatus = _SwSysPowerSupplyStatus_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 4, 2, 1, 2),
    _SwSysPowerSupplyStatus_Type()
)
swSysPowerSupplyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysPowerSupplyStatus.setStatus("mandatory")
_SwSysPowerSupplyStatusSupported_Type = Integer32
_SwSysPowerSupplyStatusSupported_Object = MibTableColumn
swSysPowerSupplyStatusSupported = _SwSysPowerSupplyStatusSupported_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 4, 2, 1, 3),
    _SwSysPowerSupplyStatusSupported_Type()
)
swSysPowerSupplyStatusSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysPowerSupplyStatusSupported.setStatus("mandatory")
_SwSysSnmp_ObjectIdentity = ObjectIdentity
swSysSnmp = _SwSysSnmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 5)
)
_SwSysSnmpAgentId_Type = Integer32
_SwSysSnmpAgentId_Object = MibScalar
swSysSnmpAgentId = _SwSysSnmpAgentId_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 5, 1),
    _SwSysSnmpAgentId_Type()
)
swSysSnmpAgentId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysSnmpAgentId.setStatus("mandatory")


class _SwSysSnmpInternalAgentTrapMask_Type(OctetString):
    """Custom type swSysSnmpInternalAgentTrapMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_SwSysSnmpInternalAgentTrapMask_Type.__name__ = "OctetString"
_SwSysSnmpInternalAgentTrapMask_Object = MibScalar
swSysSnmpInternalAgentTrapMask = _SwSysSnmpInternalAgentTrapMask_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 5, 2),
    _SwSysSnmpInternalAgentTrapMask_Type()
)
swSysSnmpInternalAgentTrapMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSysSnmpInternalAgentTrapMask.setStatus("mandatory")
_SwSysSnmpInternalAgentTrapDestinationMask_Type = Integer32
_SwSysSnmpInternalAgentTrapDestinationMask_Object = MibScalar
swSysSnmpInternalAgentTrapDestinationMask = _SwSysSnmpInternalAgentTrapDestinationMask_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 5, 3),
    _SwSysSnmpInternalAgentTrapDestinationMask_Type()
)
swSysSnmpInternalAgentTrapDestinationMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSysSnmpInternalAgentTrapDestinationMask.setStatus("mandatory")


class _SwSysSnmpProxyInternalRequests_Type(Integer32):
    """Custom type swSysSnmpProxyInternalRequests based on Integer32"""
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


_SwSysSnmpProxyInternalRequests_Type.__name__ = "Integer32"
_SwSysSnmpProxyInternalRequests_Object = MibScalar
swSysSnmpProxyInternalRequests = _SwSysSnmpProxyInternalRequests_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 5, 4),
    _SwSysSnmpProxyInternalRequests_Type()
)
swSysSnmpProxyInternalRequests.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSysSnmpProxyInternalRequests.setStatus("deprecated")


class _SwSysSnmpInternalProxyRequestMaxAge_Type(Integer32):
    """Custom type swSysSnmpInternalProxyRequestMaxAge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SwSysSnmpInternalProxyRequestMaxAge_Type.__name__ = "Integer32"
_SwSysSnmpInternalProxyRequestMaxAge_Object = MibScalar
swSysSnmpInternalProxyRequestMaxAge = _SwSysSnmpInternalProxyRequestMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 5, 5),
    _SwSysSnmpInternalProxyRequestMaxAge_Type()
)
swSysSnmpInternalProxyRequestMaxAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSysSnmpInternalProxyRequestMaxAge.setStatus("mandatory")


class _SwSysSnmpProxyInternalTraps_Type(Integer32):
    """Custom type swSysSnmpProxyInternalTraps based on Integer32"""
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


_SwSysSnmpProxyInternalTraps_Type.__name__ = "Integer32"
_SwSysSnmpProxyInternalTraps_Object = MibScalar
swSysSnmpProxyInternalTraps = _SwSysSnmpProxyInternalTraps_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 5, 6),
    _SwSysSnmpProxyInternalTraps_Type()
)
swSysSnmpProxyInternalTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSysSnmpProxyInternalTraps.setStatus("deprecated")
_SwSysSnmpInternalProxyTable_Object = MibTable
swSysSnmpInternalProxyTable = _SwSysSnmpInternalProxyTable_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 5, 7)
)
if mibBuilder.loadTexts:
    swSysSnmpInternalProxyTable.setStatus("mandatory")
_SwSysSnmpInternalProxyEntry_Object = MibTableRow
swSysSnmpInternalProxyEntry = _SwSysSnmpInternalProxyEntry_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 5, 7, 1)
)
swSysSnmpInternalProxyEntry.setIndexNames(
    (0, "SWITCHING-SYSTEMS-MIB", "swSysSnmpInternalProxyAgentId"),
    (0, "SWITCHING-SYSTEMS-MIB", "swSysSnmpInternalProxyAccessClass"),
)
if mibBuilder.loadTexts:
    swSysSnmpInternalProxyEntry.setStatus("mandatory")
_SwSysSnmpInternalProxyAgentId_Type = Integer32
_SwSysSnmpInternalProxyAgentId_Object = MibTableColumn
swSysSnmpInternalProxyAgentId = _SwSysSnmpInternalProxyAgentId_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 5, 7, 1, 1),
    _SwSysSnmpInternalProxyAgentId_Type()
)
swSysSnmpInternalProxyAgentId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysSnmpInternalProxyAgentId.setStatus("mandatory")


class _SwSysSnmpInternalProxyAccessClass_Type(Integer32):
    """Custom type swSysSnmpInternalProxyAccessClass based on Integer32"""
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


_SwSysSnmpInternalProxyAccessClass_Type.__name__ = "Integer32"
_SwSysSnmpInternalProxyAccessClass_Object = MibTableColumn
swSysSnmpInternalProxyAccessClass = _SwSysSnmpInternalProxyAccessClass_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 5, 7, 1, 2),
    _SwSysSnmpInternalProxyAccessClass_Type()
)
swSysSnmpInternalProxyAccessClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysSnmpInternalProxyAccessClass.setStatus("mandatory")
_SwSysSnmpInternalProxyCommunity_Type = OctetString
_SwSysSnmpInternalProxyCommunity_Object = MibTableColumn
swSysSnmpInternalProxyCommunity = _SwSysSnmpInternalProxyCommunity_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 5, 7, 1, 3),
    _SwSysSnmpInternalProxyCommunity_Type()
)
swSysSnmpInternalProxyCommunity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysSnmpInternalProxyCommunity.setStatus("mandatory")
_SwSysAgent_ObjectIdentity = ObjectIdentity
swSysAgent = _SwSysAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 6)
)


class _SwSysAgentRequestMaxAge_Type(Integer32):
    """Custom type swSysAgentRequestMaxAge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SwSysAgentRequestMaxAge_Type.__name__ = "Integer32"
_SwSysAgentRequestMaxAge_Object = MibScalar
swSysAgentRequestMaxAge = _SwSysAgentRequestMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 6, 1),
    _SwSysAgentRequestMaxAge_Type()
)
swSysAgentRequestMaxAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSysAgentRequestMaxAge.setStatus("mandatory")


class _SwSysAgentProxyRemoteSmtRequests_Type(Integer32):
    """Custom type swSysAgentProxyRemoteSmtRequests based on Integer32"""
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


_SwSysAgentProxyRemoteSmtRequests_Type.__name__ = "Integer32"
_SwSysAgentProxyRemoteSmtRequests_Object = MibScalar
swSysAgentProxyRemoteSmtRequests = _SwSysAgentProxyRemoteSmtRequests_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 6, 2),
    _SwSysAgentProxyRemoteSmtRequests_Type()
)
swSysAgentProxyRemoteSmtRequests.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSysAgentProxyRemoteSmtRequests.setStatus("deprecated")


class _SwSysAgentRemoteSmtProxyRequestMaxAge_Type(Integer32):
    """Custom type swSysAgentRemoteSmtProxyRequestMaxAge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SwSysAgentRemoteSmtProxyRequestMaxAge_Type.__name__ = "Integer32"
_SwSysAgentRemoteSmtProxyRequestMaxAge_Object = MibScalar
swSysAgentRemoteSmtProxyRequestMaxAge = _SwSysAgentRemoteSmtProxyRequestMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 6, 3),
    _SwSysAgentRemoteSmtProxyRequestMaxAge_Type()
)
swSysAgentRemoteSmtProxyRequestMaxAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSysAgentRemoteSmtProxyRequestMaxAge.setStatus("mandatory")


class _SwSysAgentProxyRemoteSmtEvents_Type(Integer32):
    """Custom type swSysAgentProxyRemoteSmtEvents based on Integer32"""
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


_SwSysAgentProxyRemoteSmtEvents_Type.__name__ = "Integer32"
_SwSysAgentProxyRemoteSmtEvents_Object = MibScalar
swSysAgentProxyRemoteSmtEvents = _SwSysAgentProxyRemoteSmtEvents_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 6, 4),
    _SwSysAgentProxyRemoteSmtEvents_Type()
)
swSysAgentProxyRemoteSmtEvents.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSysAgentProxyRemoteSmtEvents.setStatus("mandatory")
_SwSysAgentTrapDescriptionTable_Object = MibTable
swSysAgentTrapDescriptionTable = _SwSysAgentTrapDescriptionTable_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 6, 5)
)
if mibBuilder.loadTexts:
    swSysAgentTrapDescriptionTable.setStatus("mandatory")
_SwSysAgentTrapDescriptionTableEntry_Object = MibTableRow
swSysAgentTrapDescriptionTableEntry = _SwSysAgentTrapDescriptionTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 6, 5, 1)
)
swSysAgentTrapDescriptionTableEntry.setIndexNames(
    (0, "SWITCHING-SYSTEMS-MIB", "swSysAgentTrapDescriptionIndex"),
)
if mibBuilder.loadTexts:
    swSysAgentTrapDescriptionTableEntry.setStatus("mandatory")
_SwSysAgentTrapDescriptionIndex_Type = Integer32
_SwSysAgentTrapDescriptionIndex_Object = MibTableColumn
swSysAgentTrapDescriptionIndex = _SwSysAgentTrapDescriptionIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 6, 5, 1, 1),
    _SwSysAgentTrapDescriptionIndex_Type()
)
swSysAgentTrapDescriptionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysAgentTrapDescriptionIndex.setStatus("mandatory")
_SwSysAgentTrapEnterprise_Type = ObjectIdentifier
_SwSysAgentTrapEnterprise_Object = MibTableColumn
swSysAgentTrapEnterprise = _SwSysAgentTrapEnterprise_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 6, 5, 1, 2),
    _SwSysAgentTrapEnterprise_Type()
)
swSysAgentTrapEnterprise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysAgentTrapEnterprise.setStatus("mandatory")
_SwSysAgentTrapNumber_Type = Integer32
_SwSysAgentTrapNumber_Object = MibTableColumn
swSysAgentTrapNumber = _SwSysAgentTrapNumber_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 6, 5, 1, 3),
    _SwSysAgentTrapNumber_Type()
)
swSysAgentTrapNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysAgentTrapNumber.setStatus("mandatory")
_SwSysAgentTrapDestinationTable_Object = MibTable
swSysAgentTrapDestinationTable = _SwSysAgentTrapDestinationTable_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 6, 6)
)
if mibBuilder.loadTexts:
    swSysAgentTrapDestinationTable.setStatus("mandatory")
_SwSysAgentTrapDestinationTableEntry_Object = MibTableRow
swSysAgentTrapDestinationTableEntry = _SwSysAgentTrapDestinationTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 6, 6, 1)
)
swSysAgentTrapDestinationTableEntry.setIndexNames(
    (0, "SWITCHING-SYSTEMS-MIB", "swSysAgentTrapDestinationAddressType"),
    (0, "SWITCHING-SYSTEMS-MIB", "swSysAgentTrapDestinationAddress"),
)
if mibBuilder.loadTexts:
    swSysAgentTrapDestinationTableEntry.setStatus("mandatory")


class _SwSysAgentTrapDestinationAddressType_Type(Integer32):
    """Custom type swSysAgentTrapDestinationAddressType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("ip", 1)
    )


_SwSysAgentTrapDestinationAddressType_Type.__name__ = "Integer32"
_SwSysAgentTrapDestinationAddressType_Object = MibTableColumn
swSysAgentTrapDestinationAddressType = _SwSysAgentTrapDestinationAddressType_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 6, 6, 1, 1),
    _SwSysAgentTrapDestinationAddressType_Type()
)
swSysAgentTrapDestinationAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysAgentTrapDestinationAddressType.setStatus("mandatory")
_SwSysAgentTrapDestinationAddress_Type = OctetString
_SwSysAgentTrapDestinationAddress_Object = MibTableColumn
swSysAgentTrapDestinationAddress = _SwSysAgentTrapDestinationAddress_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 6, 6, 1, 2),
    _SwSysAgentTrapDestinationAddress_Type()
)
swSysAgentTrapDestinationAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysAgentTrapDestinationAddress.setStatus("mandatory")


class _SwSysAgentTrapDestinationTrapMask_Type(OctetString):
    """Custom type swSysAgentTrapDestinationTrapMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_SwSysAgentTrapDestinationTrapMask_Type.__name__ = "OctetString"
_SwSysAgentTrapDestinationTrapMask_Object = MibTableColumn
swSysAgentTrapDestinationTrapMask = _SwSysAgentTrapDestinationTrapMask_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 6, 6, 1, 3),
    _SwSysAgentTrapDestinationTrapMask_Type()
)
swSysAgentTrapDestinationTrapMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSysAgentTrapDestinationTrapMask.setStatus("mandatory")


class _SwSysAgentTrapDestinationEntryStatus_Type(Integer32):
    """Custom type swSysAgentTrapDestinationEntryStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_SwSysAgentTrapDestinationEntryStatus_Type.__name__ = "Integer32"
_SwSysAgentTrapDestinationEntryStatus_Object = MibTableColumn
swSysAgentTrapDestinationEntryStatus = _SwSysAgentTrapDestinationEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 6, 6, 1, 4),
    _SwSysAgentTrapDestinationEntryStatus_Type()
)
swSysAgentTrapDestinationEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSysAgentTrapDestinationEntryStatus.setStatus("mandatory")


class _SwSysAgentReadCommunity_Type(DisplayString):
    """Custom type swSysAgentReadCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_SwSysAgentReadCommunity_Type.__name__ = "DisplayString"
_SwSysAgentReadCommunity_Object = MibScalar
swSysAgentReadCommunity = _SwSysAgentReadCommunity_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 6, 7),
    _SwSysAgentReadCommunity_Type()
)
swSysAgentReadCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSysAgentReadCommunity.setStatus("mandatory")


class _SwSysAgentReadWriteCommunity_Type(DisplayString):
    """Custom type swSysAgentReadWriteCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_SwSysAgentReadWriteCommunity_Type.__name__ = "DisplayString"
_SwSysAgentReadWriteCommunity_Object = MibScalar
swSysAgentReadWriteCommunity = _SwSysAgentReadWriteCommunity_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 6, 8),
    _SwSysAgentReadWriteCommunity_Type()
)
swSysAgentReadWriteCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSysAgentReadWriteCommunity.setStatus("mandatory")
_SwSysInterface_ObjectIdentity = ObjectIdentity
swSysInterface = _SwSysInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 7)
)
_SwSysInterfaceLocationTable_Object = MibTable
swSysInterfaceLocationTable = _SwSysInterfaceLocationTable_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 7, 1)
)
if mibBuilder.loadTexts:
    swSysInterfaceLocationTable.setStatus("mandatory")
_SwSysInterfaceLocationEntry_Object = MibTableRow
swSysInterfaceLocationEntry = _SwSysInterfaceLocationEntry_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 7, 1, 1)
)
swSysInterfaceLocationEntry.setIndexNames(
    (0, "SWITCHING-SYSTEMS-MIB", "swSysInterfaceLocationIfIndex"),
)
if mibBuilder.loadTexts:
    swSysInterfaceLocationEntry.setStatus("mandatory")
_SwSysInterfaceLocationIfIndex_Type = Integer32
_SwSysInterfaceLocationIfIndex_Object = MibTableColumn
swSysInterfaceLocationIfIndex = _SwSysInterfaceLocationIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 7, 1, 1, 1),
    _SwSysInterfaceLocationIfIndex_Type()
)
swSysInterfaceLocationIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysInterfaceLocationIfIndex.setStatus("mandatory")


class _SwSysInterfaceLocationInterfaceType_Type(Integer32):
    """Custom type swSysInterfaceLocationInterfaceType based on Integer32"""
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
        *(("atmPort", 5),
          ("ethernetPort", 2),
          ("fddiMac", 3),
          ("other", 1),
          ("tokenringPort", 4))
    )


_SwSysInterfaceLocationInterfaceType_Type.__name__ = "Integer32"
_SwSysInterfaceLocationInterfaceType_Object = MibTableColumn
swSysInterfaceLocationInterfaceType = _SwSysInterfaceLocationInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 7, 1, 1, 2),
    _SwSysInterfaceLocationInterfaceType_Type()
)
swSysInterfaceLocationInterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysInterfaceLocationInterfaceType.setStatus("mandatory")


class _SwSysInterfaceLocationType_Type(Integer32):
    """Custom type swSysInterfaceLocationType based on Integer32"""
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
        *(("chassis", 3),
          ("modularCard", 4),
          ("modularSlot", 2),
          ("other", 1))
    )


_SwSysInterfaceLocationType_Type.__name__ = "Integer32"
_SwSysInterfaceLocationType_Object = MibTableColumn
swSysInterfaceLocationType = _SwSysInterfaceLocationType_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 7, 1, 1, 3),
    _SwSysInterfaceLocationType_Type()
)
swSysInterfaceLocationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysInterfaceLocationType.setStatus("mandatory")
_SwSysInterfaceLocationTypeIndex_Type = Integer32
_SwSysInterfaceLocationTypeIndex_Object = MibTableColumn
swSysInterfaceLocationTypeIndex = _SwSysInterfaceLocationTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 7, 1, 1, 4),
    _SwSysInterfaceLocationTypeIndex_Type()
)
swSysInterfaceLocationTypeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysInterfaceLocationTypeIndex.setStatus("mandatory")
_SwSysInterfaceLocationLocalIndex_Type = Integer32
_SwSysInterfaceLocationLocalIndex_Object = MibTableColumn
swSysInterfaceLocationLocalIndex = _SwSysInterfaceLocationLocalIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 7, 1, 1, 5),
    _SwSysInterfaceLocationLocalIndex_Type()
)
swSysInterfaceLocationLocalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysInterfaceLocationLocalIndex.setStatus("mandatory")
_SwSysInterfaceLocationSystemModuleIndex_Type = Integer32
_SwSysInterfaceLocationSystemModuleIndex_Object = MibTableColumn
swSysInterfaceLocationSystemModuleIndex = _SwSysInterfaceLocationSystemModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 7, 1, 1, 6),
    _SwSysInterfaceLocationSystemModuleIndex_Type()
)
swSysInterfaceLocationSystemModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysInterfaceLocationSystemModuleIndex.setStatus("mandatory")
_SwSysEthernetPort_ObjectIdentity = ObjectIdentity
swSysEthernetPort = _SwSysEthernetPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 8)
)
_SwSysEthernetPortCount_Type = Integer32
_SwSysEthernetPortCount_Object = MibScalar
swSysEthernetPortCount = _SwSysEthernetPortCount_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 8, 1),
    _SwSysEthernetPortCount_Type()
)
swSysEthernetPortCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysEthernetPortCount.setStatus("mandatory")
_SwSysEthernetPortTable_Object = MibTable
swSysEthernetPortTable = _SwSysEthernetPortTable_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 8, 2)
)
if mibBuilder.loadTexts:
    swSysEthernetPortTable.setStatus("mandatory")
_SwSysEthernetPortEntry_Object = MibTableRow
swSysEthernetPortEntry = _SwSysEthernetPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 8, 2, 1)
)
swSysEthernetPortEntry.setIndexNames(
    (0, "SWITCHING-SYSTEMS-MIB", "swSysEthernetPortIndex"),
)
if mibBuilder.loadTexts:
    swSysEthernetPortEntry.setStatus("mandatory")
_SwSysEthernetPortIndex_Type = Integer32
_SwSysEthernetPortIndex_Object = MibTableColumn
swSysEthernetPortIndex = _SwSysEthernetPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 8, 2, 1, 1),
    _SwSysEthernetPortIndex_Type()
)
swSysEthernetPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysEthernetPortIndex.setStatus("mandatory")
_SwSysEthernetPortIfIndex_Type = Integer32
_SwSysEthernetPortIfIndex_Object = MibTableColumn
swSysEthernetPortIfIndex = _SwSysEthernetPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 8, 2, 1, 2),
    _SwSysEthernetPortIfIndex_Type()
)
swSysEthernetPortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysEthernetPortIfIndex.setStatus("mandatory")


class _SwSysEthernetPortLabel_Type(DisplayString):
    """Custom type swSysEthernetPortLabel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_SwSysEthernetPortLabel_Type.__name__ = "DisplayString"
_SwSysEthernetPortLabel_Object = MibTableColumn
swSysEthernetPortLabel = _SwSysEthernetPortLabel_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 8, 2, 1, 3),
    _SwSysEthernetPortLabel_Type()
)
swSysEthernetPortLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSysEthernetPortLabel.setStatus("mandatory")


class _SwSysEthernetPortLinkStatus_Type(Integer32):
    """Custom type swSysEthernetPortLinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inActive", 2))
    )


_SwSysEthernetPortLinkStatus_Type.__name__ = "Integer32"
_SwSysEthernetPortLinkStatus_Object = MibTableColumn
swSysEthernetPortLinkStatus = _SwSysEthernetPortLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 8, 2, 1, 4),
    _SwSysEthernetPortLinkStatus_Type()
)
swSysEthernetPortLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysEthernetPortLinkStatus.setStatus("mandatory")


class _SwSysEthernetPortType_Type(Integer32):
    """Custom type swSysEthernetPortType based on Integer32"""
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
              17,
              18,
              19,
              20,
              21,
              22,
              23)
        )
    )
    namedValues = NamedValues(
        *(("aui", 4),
          ("bnc10Base2", 5),
          ("db91000BaseCx", 16),
          ("gbic1000BaseCxDb9", 18),
          ("gbic1000BaseCxHssdc", 19),
          ("gbic1000BaseLx", 21),
          ("gbic1000BaseLx10Km", 20),
          ("gbic1000BaseSx", 22),
          ("gbicNotPresent", 17),
          ("hssdc1000BaseCx", 15),
          ("other", 6),
          ("rj2110BaseT", 1),
          ("rj451000BaseT", 23),
          ("rj45100BaseT", 7),
          ("rj4510BaseT", 2),
          ("sc1000BaseLx10km", 13),
          ("sc1000BaseLxMm", 11),
          ("sc1000BaseLxSm", 10),
          ("sc1000BaseLxSmMm", 12),
          ("sc1000BaseSx", 14),
          ("sc100BaseFx", 8),
          ("st10BaseFL", 3),
          ("untermBnc10Base2", 9))
    )


_SwSysEthernetPortType_Type.__name__ = "Integer32"
_SwSysEthernetPortType_Object = MibTableColumn
swSysEthernetPortType = _SwSysEthernetPortType_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 8, 2, 1, 5),
    _SwSysEthernetPortType_Type()
)
swSysEthernetPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysEthernetPortType.setStatus("mandatory")
_SwSysEthernetPortRateTable_Object = MibTable
swSysEthernetPortRateTable = _SwSysEthernetPortRateTable_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 8, 3)
)
if mibBuilder.loadTexts:
    swSysEthernetPortRateTable.setStatus("mandatory")
_SwSysEthernetPortRateEntry_Object = MibTableRow
swSysEthernetPortRateEntry = _SwSysEthernetPortRateEntry_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 8, 3, 1)
)
swSysEthernetPortRateEntry.setIndexNames(
    (0, "SWITCHING-SYSTEMS-MIB", "swSysEthernetPortRateIndex"),
)
if mibBuilder.loadTexts:
    swSysEthernetPortRateEntry.setStatus("mandatory")
_SwSysEthernetPortRateIndex_Type = Integer32
_SwSysEthernetPortRateIndex_Object = MibTableColumn
swSysEthernetPortRateIndex = _SwSysEthernetPortRateIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 8, 3, 1, 1),
    _SwSysEthernetPortRateIndex_Type()
)
swSysEthernetPortRateIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysEthernetPortRateIndex.setStatus("mandatory")
_SwSysEthernetPortRateByteReceiveRate_Type = Integer32
_SwSysEthernetPortRateByteReceiveRate_Object = MibTableColumn
swSysEthernetPortRateByteReceiveRate = _SwSysEthernetPortRateByteReceiveRate_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 8, 3, 1, 2),
    _SwSysEthernetPortRateByteReceiveRate_Type()
)
swSysEthernetPortRateByteReceiveRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysEthernetPortRateByteReceiveRate.setStatus("mandatory")
_SwSysEthernetPortRatePeakByteReceiveRate_Type = Integer32
_SwSysEthernetPortRatePeakByteReceiveRate_Object = MibTableColumn
swSysEthernetPortRatePeakByteReceiveRate = _SwSysEthernetPortRatePeakByteReceiveRate_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 8, 3, 1, 3),
    _SwSysEthernetPortRatePeakByteReceiveRate_Type()
)
swSysEthernetPortRatePeakByteReceiveRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysEthernetPortRatePeakByteReceiveRate.setStatus("mandatory")
_SwSysEthernetPortRateFrameReceiveRate_Type = Integer32
_SwSysEthernetPortRateFrameReceiveRate_Object = MibTableColumn
swSysEthernetPortRateFrameReceiveRate = _SwSysEthernetPortRateFrameReceiveRate_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 8, 3, 1, 4),
    _SwSysEthernetPortRateFrameReceiveRate_Type()
)
swSysEthernetPortRateFrameReceiveRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysEthernetPortRateFrameReceiveRate.setStatus("mandatory")
_SwSysEthernetPortRatePeakFrameReceiveRate_Type = Integer32
_SwSysEthernetPortRatePeakFrameReceiveRate_Object = MibTableColumn
swSysEthernetPortRatePeakFrameReceiveRate = _SwSysEthernetPortRatePeakFrameReceiveRate_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 8, 3, 1, 5),
    _SwSysEthernetPortRatePeakFrameReceiveRate_Type()
)
swSysEthernetPortRatePeakFrameReceiveRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysEthernetPortRatePeakFrameReceiveRate.setStatus("mandatory")
_SwSysEthernetPortRateByteTransmitRate_Type = Integer32
_SwSysEthernetPortRateByteTransmitRate_Object = MibTableColumn
swSysEthernetPortRateByteTransmitRate = _SwSysEthernetPortRateByteTransmitRate_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 8, 3, 1, 6),
    _SwSysEthernetPortRateByteTransmitRate_Type()
)
swSysEthernetPortRateByteTransmitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysEthernetPortRateByteTransmitRate.setStatus("mandatory")
_SwSysEthernetPortRatePeakByteTransmitRate_Type = Integer32
_SwSysEthernetPortRatePeakByteTransmitRate_Object = MibTableColumn
swSysEthernetPortRatePeakByteTransmitRate = _SwSysEthernetPortRatePeakByteTransmitRate_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 8, 3, 1, 7),
    _SwSysEthernetPortRatePeakByteTransmitRate_Type()
)
swSysEthernetPortRatePeakByteTransmitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysEthernetPortRatePeakByteTransmitRate.setStatus("mandatory")
_SwSysEthernetPortRateFrameTransmitRate_Type = Integer32
_SwSysEthernetPortRateFrameTransmitRate_Object = MibTableColumn
swSysEthernetPortRateFrameTransmitRate = _SwSysEthernetPortRateFrameTransmitRate_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 8, 3, 1, 8),
    _SwSysEthernetPortRateFrameTransmitRate_Type()
)
swSysEthernetPortRateFrameTransmitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysEthernetPortRateFrameTransmitRate.setStatus("mandatory")
_SwSysEthernetPortRatePeakFrameTransmitRate_Type = Integer32
_SwSysEthernetPortRatePeakFrameTransmitRate_Object = MibTableColumn
swSysEthernetPortRatePeakFrameTransmitRate = _SwSysEthernetPortRatePeakFrameTransmitRate_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 8, 3, 1, 9),
    _SwSysEthernetPortRatePeakFrameTransmitRate_Type()
)
swSysEthernetPortRatePeakFrameTransmitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysEthernetPortRatePeakFrameTransmitRate.setStatus("mandatory")
_SwSysSmt_ObjectIdentity = ObjectIdentity
swSysSmt = _SwSysSmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 9)
)
_SwSysSmtCount_Type = Integer32
_SwSysSmtCount_Object = MibScalar
swSysSmtCount = _SwSysSmtCount_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 9, 1),
    _SwSysSmtCount_Type()
)
swSysSmtCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysSmtCount.setStatus("mandatory")
_SwSysSmtFddiMacBeaconTable_Object = MibTable
swSysSmtFddiMacBeaconTable = _SwSysSmtFddiMacBeaconTable_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 9, 4)
)
if mibBuilder.loadTexts:
    swSysSmtFddiMacBeaconTable.setStatus("mandatory")
_SwSysSmtFddiMacBeaconEntry_Object = MibTableRow
swSysSmtFddiMacBeaconEntry = _SwSysSmtFddiMacBeaconEntry_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 9, 4, 1)
)
swSysSmtFddiMacBeaconEntry.setIndexNames(
    (0, "SWITCHING-SYSTEMS-MIB", "swSysSmtFddiMacBeaconSmtIndex"),
    (0, "SWITCHING-SYSTEMS-MIB", "swSysSmtFddiMacBeaconIndex"),
)
if mibBuilder.loadTexts:
    swSysSmtFddiMacBeaconEntry.setStatus("mandatory")
_SwSysSmtFddiMacBeaconSmtIndex_Type = Integer32
_SwSysSmtFddiMacBeaconSmtIndex_Object = MibTableColumn
swSysSmtFddiMacBeaconSmtIndex = _SwSysSmtFddiMacBeaconSmtIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 9, 4, 1, 1),
    _SwSysSmtFddiMacBeaconSmtIndex_Type()
)
swSysSmtFddiMacBeaconSmtIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysSmtFddiMacBeaconSmtIndex.setStatus("mandatory")
_SwSysSmtFddiMacBeaconIndex_Type = Integer32
_SwSysSmtFddiMacBeaconIndex_Object = MibTableColumn
swSysSmtFddiMacBeaconIndex = _SwSysSmtFddiMacBeaconIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 9, 4, 1, 2),
    _SwSysSmtFddiMacBeaconIndex_Type()
)
swSysSmtFddiMacBeaconIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysSmtFddiMacBeaconIndex.setStatus("mandatory")


class _SwSysSmtFddiMacBeaconHistory_Type(OctetString):
    """Custom type swSysSmtFddiMacBeaconHistory based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_SwSysSmtFddiMacBeaconHistory_Type.__name__ = "OctetString"
_SwSysSmtFddiMacBeaconHistory_Object = MibTableColumn
swSysSmtFddiMacBeaconHistory = _SwSysSmtFddiMacBeaconHistory_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 9, 4, 1, 3),
    _SwSysSmtFddiMacBeaconHistory_Type()
)
swSysSmtFddiMacBeaconHistory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysSmtFddiMacBeaconHistory.setStatus("mandatory")
_SwSysSmtFddiMacRateTable_Object = MibTable
swSysSmtFddiMacRateTable = _SwSysSmtFddiMacRateTable_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 9, 5)
)
if mibBuilder.loadTexts:
    swSysSmtFddiMacRateTable.setStatus("mandatory")
_SwSysSmtFddiMacRateEntry_Object = MibTableRow
swSysSmtFddiMacRateEntry = _SwSysSmtFddiMacRateEntry_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 9, 5, 1)
)
swSysSmtFddiMacRateEntry.setIndexNames(
    (0, "SWITCHING-SYSTEMS-MIB", "swSysSmtFddiMacRateSmtIndex"),
    (0, "SWITCHING-SYSTEMS-MIB", "swSysSmtFddiMacRateIndex"),
)
if mibBuilder.loadTexts:
    swSysSmtFddiMacRateEntry.setStatus("mandatory")
_SwSysSmtFddiMacRateSmtIndex_Type = Integer32
_SwSysSmtFddiMacRateSmtIndex_Object = MibTableColumn
swSysSmtFddiMacRateSmtIndex = _SwSysSmtFddiMacRateSmtIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 9, 5, 1, 1),
    _SwSysSmtFddiMacRateSmtIndex_Type()
)
swSysSmtFddiMacRateSmtIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysSmtFddiMacRateSmtIndex.setStatus("mandatory")
_SwSysSmtFddiMacRateIndex_Type = Integer32
_SwSysSmtFddiMacRateIndex_Object = MibTableColumn
swSysSmtFddiMacRateIndex = _SwSysSmtFddiMacRateIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 9, 5, 1, 2),
    _SwSysSmtFddiMacRateIndex_Type()
)
swSysSmtFddiMacRateIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysSmtFddiMacRateIndex.setStatus("mandatory")
_SwSysSmtFddiMacRateByteReceiveRate_Type = Integer32
_SwSysSmtFddiMacRateByteReceiveRate_Object = MibTableColumn
swSysSmtFddiMacRateByteReceiveRate = _SwSysSmtFddiMacRateByteReceiveRate_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 9, 5, 1, 3),
    _SwSysSmtFddiMacRateByteReceiveRate_Type()
)
swSysSmtFddiMacRateByteReceiveRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysSmtFddiMacRateByteReceiveRate.setStatus("mandatory")
_SwSysSmtFddiMacRatePeakByteReceiveRate_Type = Integer32
_SwSysSmtFddiMacRatePeakByteReceiveRate_Object = MibTableColumn
swSysSmtFddiMacRatePeakByteReceiveRate = _SwSysSmtFddiMacRatePeakByteReceiveRate_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 9, 5, 1, 4),
    _SwSysSmtFddiMacRatePeakByteReceiveRate_Type()
)
swSysSmtFddiMacRatePeakByteReceiveRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysSmtFddiMacRatePeakByteReceiveRate.setStatus("mandatory")
_SwSysSmtFddiMacRateFrameReceiveRate_Type = Integer32
_SwSysSmtFddiMacRateFrameReceiveRate_Object = MibTableColumn
swSysSmtFddiMacRateFrameReceiveRate = _SwSysSmtFddiMacRateFrameReceiveRate_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 9, 5, 1, 5),
    _SwSysSmtFddiMacRateFrameReceiveRate_Type()
)
swSysSmtFddiMacRateFrameReceiveRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysSmtFddiMacRateFrameReceiveRate.setStatus("mandatory")
_SwSysSmtFddiMacRatePeakFrameReceiveRate_Type = Integer32
_SwSysSmtFddiMacRatePeakFrameReceiveRate_Object = MibTableColumn
swSysSmtFddiMacRatePeakFrameReceiveRate = _SwSysSmtFddiMacRatePeakFrameReceiveRate_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 9, 5, 1, 6),
    _SwSysSmtFddiMacRatePeakFrameReceiveRate_Type()
)
swSysSmtFddiMacRatePeakFrameReceiveRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysSmtFddiMacRatePeakFrameReceiveRate.setStatus("mandatory")
_SwSysSmtFddiMacRateByteTransmitRate_Type = Integer32
_SwSysSmtFddiMacRateByteTransmitRate_Object = MibTableColumn
swSysSmtFddiMacRateByteTransmitRate = _SwSysSmtFddiMacRateByteTransmitRate_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 9, 5, 1, 7),
    _SwSysSmtFddiMacRateByteTransmitRate_Type()
)
swSysSmtFddiMacRateByteTransmitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysSmtFddiMacRateByteTransmitRate.setStatus("mandatory")
_SwSysSmtFddiMacRatePeakByteTransmitRate_Type = Integer32
_SwSysSmtFddiMacRatePeakByteTransmitRate_Object = MibTableColumn
swSysSmtFddiMacRatePeakByteTransmitRate = _SwSysSmtFddiMacRatePeakByteTransmitRate_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 9, 5, 1, 8),
    _SwSysSmtFddiMacRatePeakByteTransmitRate_Type()
)
swSysSmtFddiMacRatePeakByteTransmitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysSmtFddiMacRatePeakByteTransmitRate.setStatus("mandatory")
_SwSysSmtFddiMacRateFrameTransmitRate_Type = Integer32
_SwSysSmtFddiMacRateFrameTransmitRate_Object = MibTableColumn
swSysSmtFddiMacRateFrameTransmitRate = _SwSysSmtFddiMacRateFrameTransmitRate_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 9, 5, 1, 9),
    _SwSysSmtFddiMacRateFrameTransmitRate_Type()
)
swSysSmtFddiMacRateFrameTransmitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysSmtFddiMacRateFrameTransmitRate.setStatus("mandatory")
_SwSysSmtFddiMacRatePeakFrameTransmitRate_Type = Integer32
_SwSysSmtFddiMacRatePeakFrameTransmitRate_Object = MibTableColumn
swSysSmtFddiMacRatePeakFrameTransmitRate = _SwSysSmtFddiMacRatePeakFrameTransmitRate_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 9, 5, 1, 10),
    _SwSysSmtFddiMacRatePeakFrameTransmitRate_Type()
)
swSysSmtFddiMacRatePeakFrameTransmitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysSmtFddiMacRatePeakFrameTransmitRate.setStatus("mandatory")
_SwSysSmtFddiPortTable_Object = MibTable
swSysSmtFddiPortTable = _SwSysSmtFddiPortTable_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 9, 6)
)
if mibBuilder.loadTexts:
    swSysSmtFddiPortTable.setStatus("mandatory")
_SwSysSmtFddiPortEntry_Object = MibTableRow
swSysSmtFddiPortEntry = _SwSysSmtFddiPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 9, 6, 1)
)
swSysSmtFddiPortEntry.setIndexNames(
    (0, "SWITCHING-SYSTEMS-MIB", "swSysSmtFddiPortSmtIndex"),
    (0, "SWITCHING-SYSTEMS-MIB", "swSysSmtFddiPortIndex"),
)
if mibBuilder.loadTexts:
    swSysSmtFddiPortEntry.setStatus("mandatory")
_SwSysSmtFddiPortSmtIndex_Type = Integer32
_SwSysSmtFddiPortSmtIndex_Object = MibTableColumn
swSysSmtFddiPortSmtIndex = _SwSysSmtFddiPortSmtIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 9, 6, 1, 1),
    _SwSysSmtFddiPortSmtIndex_Type()
)
swSysSmtFddiPortSmtIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysSmtFddiPortSmtIndex.setStatus("mandatory")
_SwSysSmtFddiPortIndex_Type = Integer32
_SwSysSmtFddiPortIndex_Object = MibTableColumn
swSysSmtFddiPortIndex = _SwSysSmtFddiPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 9, 6, 1, 2),
    _SwSysSmtFddiPortIndex_Type()
)
swSysSmtFddiPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysSmtFddiPortIndex.setStatus("mandatory")


class _SwSysSmtFddiPortLocationType_Type(Integer32):
    """Custom type swSysSmtFddiPortLocationType based on Integer32"""
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
        *(("chassis", 3),
          ("modularCard", 4),
          ("modularSlot", 2),
          ("other", 1))
    )


_SwSysSmtFddiPortLocationType_Type.__name__ = "Integer32"
_SwSysSmtFddiPortLocationType_Object = MibTableColumn
swSysSmtFddiPortLocationType = _SwSysSmtFddiPortLocationType_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 9, 6, 1, 3),
    _SwSysSmtFddiPortLocationType_Type()
)
swSysSmtFddiPortLocationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysSmtFddiPortLocationType.setStatus("mandatory")
_SwSysSmtFddiPortLocationTypeIndex_Type = Integer32
_SwSysSmtFddiPortLocationTypeIndex_Object = MibTableColumn
swSysSmtFddiPortLocationTypeIndex = _SwSysSmtFddiPortLocationTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 9, 6, 1, 4),
    _SwSysSmtFddiPortLocationTypeIndex_Type()
)
swSysSmtFddiPortLocationTypeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysSmtFddiPortLocationTypeIndex.setStatus("mandatory")
_SwSysSmtFddiPortLocationLocalIndex_Type = Integer32
_SwSysSmtFddiPortLocationLocalIndex_Object = MibTableColumn
swSysSmtFddiPortLocationLocalIndex = _SwSysSmtFddiPortLocationLocalIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 9, 6, 1, 5),
    _SwSysSmtFddiPortLocationLocalIndex_Type()
)
swSysSmtFddiPortLocationLocalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysSmtFddiPortLocationLocalIndex.setStatus("mandatory")


class _SwSysSmtFddiPortLabel_Type(DisplayString):
    """Custom type swSysSmtFddiPortLabel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_SwSysSmtFddiPortLabel_Type.__name__ = "DisplayString"
_SwSysSmtFddiPortLabel_Object = MibTableColumn
swSysSmtFddiPortLabel = _SwSysSmtFddiPortLabel_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 9, 6, 1, 6),
    _SwSysSmtFddiPortLabel_Type()
)
swSysSmtFddiPortLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSysSmtFddiPortLabel.setStatus("mandatory")
_SwSysSmtFddiMacLocationTable_Object = MibTable
swSysSmtFddiMacLocationTable = _SwSysSmtFddiMacLocationTable_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 9, 7)
)
if mibBuilder.loadTexts:
    swSysSmtFddiMacLocationTable.setStatus("mandatory")
_SwSysSmtFddiMacLocationEntry_Object = MibTableRow
swSysSmtFddiMacLocationEntry = _SwSysSmtFddiMacLocationEntry_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 9, 7, 1)
)
swSysSmtFddiMacLocationEntry.setIndexNames(
    (0, "SWITCHING-SYSTEMS-MIB", "swSysSmtFddiMacLocationSmtIndex"),
    (0, "SWITCHING-SYSTEMS-MIB", "swSysSmtFddiMacLocationIndex"),
)
if mibBuilder.loadTexts:
    swSysSmtFddiMacLocationEntry.setStatus("mandatory")
_SwSysSmtFddiMacLocationSmtIndex_Type = Integer32
_SwSysSmtFddiMacLocationSmtIndex_Object = MibTableColumn
swSysSmtFddiMacLocationSmtIndex = _SwSysSmtFddiMacLocationSmtIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 9, 7, 1, 1),
    _SwSysSmtFddiMacLocationSmtIndex_Type()
)
swSysSmtFddiMacLocationSmtIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysSmtFddiMacLocationSmtIndex.setStatus("mandatory")
_SwSysSmtFddiMacLocationIndex_Type = Integer32
_SwSysSmtFddiMacLocationIndex_Object = MibTableColumn
swSysSmtFddiMacLocationIndex = _SwSysSmtFddiMacLocationIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 9, 7, 1, 2),
    _SwSysSmtFddiMacLocationIndex_Type()
)
swSysSmtFddiMacLocationIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysSmtFddiMacLocationIndex.setStatus("mandatory")


class _SwSysSmtFddiMacCurrentLocation_Type(Integer32):
    """Custom type swSysSmtFddiMacCurrentLocation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("externalFddiPort", 2),
          ("internalBackplane", 1))
    )


_SwSysSmtFddiMacCurrentLocation_Type.__name__ = "Integer32"
_SwSysSmtFddiMacCurrentLocation_Object = MibTableColumn
swSysSmtFddiMacCurrentLocation = _SwSysSmtFddiMacCurrentLocation_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 9, 7, 1, 3),
    _SwSysSmtFddiMacCurrentLocation_Type()
)
swSysSmtFddiMacCurrentLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysSmtFddiMacCurrentLocation.setStatus("mandatory")


class _SwSysSmtFddiMacRequestedLocation_Type(Integer32):
    """Custom type swSysSmtFddiMacRequestedLocation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("externalFddiPort", 2),
          ("internalBackplane", 1))
    )


_SwSysSmtFddiMacRequestedLocation_Type.__name__ = "Integer32"
_SwSysSmtFddiMacRequestedLocation_Object = MibTableColumn
swSysSmtFddiMacRequestedLocation = _SwSysSmtFddiMacRequestedLocation_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 9, 7, 1, 4),
    _SwSysSmtFddiMacRequestedLocation_Type()
)
swSysSmtFddiMacRequestedLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSysSmtFddiMacRequestedLocation.setStatus("mandatory")


class _SwSysSmtFddiMacAvailableLocation_Type(Integer32):
    """Custom type swSysSmtFddiMacAvailableLocation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("externalFddiPort", 2),
          ("internalBackplane", 1),
          ("internalOrExternal", 3))
    )


_SwSysSmtFddiMacAvailableLocation_Type.__name__ = "Integer32"
_SwSysSmtFddiMacAvailableLocation_Object = MibTableColumn
swSysSmtFddiMacAvailableLocation = _SwSysSmtFddiMacAvailableLocation_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 9, 7, 1, 5),
    _SwSysSmtFddiMacAvailableLocation_Type()
)
swSysSmtFddiMacAvailableLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysSmtFddiMacAvailableLocation.setStatus("mandatory")
_SwSysSmtFddiMacStationTable_Object = MibTable
swSysSmtFddiMacStationTable = _SwSysSmtFddiMacStationTable_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 9, 8)
)
if mibBuilder.loadTexts:
    swSysSmtFddiMacStationTable.setStatus("mandatory")
_SwSysSmtFddiMacStationEntry_Object = MibTableRow
swSysSmtFddiMacStationEntry = _SwSysSmtFddiMacStationEntry_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 9, 8, 1)
)
swSysSmtFddiMacStationEntry.setIndexNames(
    (0, "SWITCHING-SYSTEMS-MIB", "swSysSmtFddiMacStationSmtIndex"),
    (0, "SWITCHING-SYSTEMS-MIB", "swSysSmtFddiMacStationIndex"),
)
if mibBuilder.loadTexts:
    swSysSmtFddiMacStationEntry.setStatus("mandatory")
_SwSysSmtFddiMacStationSmtIndex_Type = Integer32
_SwSysSmtFddiMacStationSmtIndex_Object = MibTableColumn
swSysSmtFddiMacStationSmtIndex = _SwSysSmtFddiMacStationSmtIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 9, 8, 1, 1),
    _SwSysSmtFddiMacStationSmtIndex_Type()
)
swSysSmtFddiMacStationSmtIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysSmtFddiMacStationSmtIndex.setStatus("mandatory")
_SwSysSmtFddiMacStationIndex_Type = Integer32
_SwSysSmtFddiMacStationIndex_Object = MibTableColumn
swSysSmtFddiMacStationIndex = _SwSysSmtFddiMacStationIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 9, 8, 1, 2),
    _SwSysSmtFddiMacStationIndex_Type()
)
swSysSmtFddiMacStationIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysSmtFddiMacStationIndex.setStatus("mandatory")
_SwSysSmtFddiMacCurrentStation_Type = Integer32
_SwSysSmtFddiMacCurrentStation_Object = MibTableColumn
swSysSmtFddiMacCurrentStation = _SwSysSmtFddiMacCurrentStation_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 9, 8, 1, 3),
    _SwSysSmtFddiMacCurrentStation_Type()
)
swSysSmtFddiMacCurrentStation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysSmtFddiMacCurrentStation.setStatus("mandatory")
_SwSysSmtFddiMacRequestedStation_Type = Integer32
_SwSysSmtFddiMacRequestedStation_Object = MibTableColumn
swSysSmtFddiMacRequestedStation = _SwSysSmtFddiMacRequestedStation_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 9, 8, 1, 4),
    _SwSysSmtFddiMacRequestedStation_Type()
)
swSysSmtFddiMacRequestedStation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSysSmtFddiMacRequestedStation.setStatus("mandatory")
_SwSysSmtFddiMacAvailableStations_Type = Integer32
_SwSysSmtFddiMacAvailableStations_Object = MibTableColumn
swSysSmtFddiMacAvailableStations = _SwSysSmtFddiMacAvailableStations_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 9, 8, 1, 5),
    _SwSysSmtFddiMacAvailableStations_Type()
)
swSysSmtFddiMacAvailableStations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysSmtFddiMacAvailableStations.setStatus("mandatory")
_SwSysSmtFddiPortStationTable_Object = MibTable
swSysSmtFddiPortStationTable = _SwSysSmtFddiPortStationTable_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 9, 9)
)
if mibBuilder.loadTexts:
    swSysSmtFddiPortStationTable.setStatus("mandatory")
_SwSysSmtFddiPortStationEntry_Object = MibTableRow
swSysSmtFddiPortStationEntry = _SwSysSmtFddiPortStationEntry_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 9, 9, 1)
)
swSysSmtFddiPortStationEntry.setIndexNames(
    (0, "SWITCHING-SYSTEMS-MIB", "swSysSmtFddiPortStationSmtIndex"),
    (0, "SWITCHING-SYSTEMS-MIB", "swSysSmtFddiPortStationIndex"),
)
if mibBuilder.loadTexts:
    swSysSmtFddiPortStationEntry.setStatus("mandatory")
_SwSysSmtFddiPortStationSmtIndex_Type = Integer32
_SwSysSmtFddiPortStationSmtIndex_Object = MibTableColumn
swSysSmtFddiPortStationSmtIndex = _SwSysSmtFddiPortStationSmtIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 9, 9, 1, 1),
    _SwSysSmtFddiPortStationSmtIndex_Type()
)
swSysSmtFddiPortStationSmtIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysSmtFddiPortStationSmtIndex.setStatus("mandatory")
_SwSysSmtFddiPortStationIndex_Type = Integer32
_SwSysSmtFddiPortStationIndex_Object = MibTableColumn
swSysSmtFddiPortStationIndex = _SwSysSmtFddiPortStationIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 9, 9, 1, 2),
    _SwSysSmtFddiPortStationIndex_Type()
)
swSysSmtFddiPortStationIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysSmtFddiPortStationIndex.setStatus("mandatory")
_SwSysSmtFddiPortCurrentStation_Type = Integer32
_SwSysSmtFddiPortCurrentStation_Object = MibTableColumn
swSysSmtFddiPortCurrentStation = _SwSysSmtFddiPortCurrentStation_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 9, 9, 1, 3),
    _SwSysSmtFddiPortCurrentStation_Type()
)
swSysSmtFddiPortCurrentStation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysSmtFddiPortCurrentStation.setStatus("mandatory")
_SwSysSmtFddiPortRequestedStation_Type = Integer32
_SwSysSmtFddiPortRequestedStation_Object = MibTableColumn
swSysSmtFddiPortRequestedStation = _SwSysSmtFddiPortRequestedStation_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 9, 9, 1, 4),
    _SwSysSmtFddiPortRequestedStation_Type()
)
swSysSmtFddiPortRequestedStation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSysSmtFddiPortRequestedStation.setStatus("mandatory")
_SwSysSmtFddiPortAvailableStations_Type = Integer32
_SwSysSmtFddiPortAvailableStations_Object = MibTableColumn
swSysSmtFddiPortAvailableStations = _SwSysSmtFddiPortAvailableStations_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 9, 9, 1, 5),
    _SwSysSmtFddiPortAvailableStations_Type()
)
swSysSmtFddiPortAvailableStations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysSmtFddiPortAvailableStations.setStatus("mandatory")
_SwSysBridge_ObjectIdentity = ObjectIdentity
swSysBridge = _SwSysBridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 10)
)
_SwSysBridgeCount_Type = Integer32
_SwSysBridgeCount_Object = MibScalar
swSysBridgeCount = _SwSysBridgeCount_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 10, 1),
    _SwSysBridgeCount_Type()
)
swSysBridgeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysBridgeCount.setStatus("mandatory")
_SwSysBridgeTable_Object = MibTable
swSysBridgeTable = _SwSysBridgeTable_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 10, 2)
)
if mibBuilder.loadTexts:
    swSysBridgeTable.setStatus("mandatory")
_SwSysBridgeEntry_Object = MibTableRow
swSysBridgeEntry = _SwSysBridgeEntry_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 10, 2, 1)
)
swSysBridgeEntry.setIndexNames(
    (0, "SWITCHING-SYSTEMS-MIB", "swSysBridgeIndex"),
)
if mibBuilder.loadTexts:
    swSysBridgeEntry.setStatus("mandatory")
_SwSysBridgeIndex_Type = Integer32
_SwSysBridgeIndex_Object = MibTableColumn
swSysBridgeIndex = _SwSysBridgeIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 10, 2, 1, 1),
    _SwSysBridgeIndex_Type()
)
swSysBridgeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysBridgeIndex.setStatus("mandatory")
_SwSysBridgePortCount_Type = Integer32
_SwSysBridgePortCount_Object = MibTableColumn
swSysBridgePortCount = _SwSysBridgePortCount_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 10, 2, 1, 2),
    _SwSysBridgePortCount_Type()
)
swSysBridgePortCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysBridgePortCount.setStatus("mandatory")
_SwSysBridgeAddressTableSize_Type = Integer32
_SwSysBridgeAddressTableSize_Object = MibTableColumn
swSysBridgeAddressTableSize = _SwSysBridgeAddressTableSize_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 10, 2, 1, 3),
    _SwSysBridgeAddressTableSize_Type()
)
swSysBridgeAddressTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysBridgeAddressTableSize.setStatus("mandatory")
_SwSysBridgeAddressTableCount_Type = Integer32
_SwSysBridgeAddressTableCount_Object = MibTableColumn
swSysBridgeAddressTableCount = _SwSysBridgeAddressTableCount_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 10, 2, 1, 4),
    _SwSysBridgeAddressTableCount_Type()
)
swSysBridgeAddressTableCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysBridgeAddressTableCount.setStatus("mandatory")
_SwSysBridgeAddressTablePeakCount_Type = Integer32
_SwSysBridgeAddressTablePeakCount_Object = MibTableColumn
swSysBridgeAddressTablePeakCount = _SwSysBridgeAddressTablePeakCount_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 10, 2, 1, 5),
    _SwSysBridgeAddressTablePeakCount_Type()
)
swSysBridgeAddressTablePeakCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysBridgeAddressTablePeakCount.setStatus("mandatory")
_SwSysBridgeAddressThreshold_Type = Integer32
_SwSysBridgeAddressThreshold_Object = MibTableColumn
swSysBridgeAddressThreshold = _SwSysBridgeAddressThreshold_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 10, 2, 1, 6),
    _SwSysBridgeAddressThreshold_Type()
)
swSysBridgeAddressThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSysBridgeAddressThreshold.setStatus("mandatory")


class _SwSysBridgeMode_Type(Integer32):
    """Custom type swSysBridgeMode based on Integer32"""
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
        *(("expressMode", 1),
          ("ibmSRBridgeMode", 6),
          ("ieee8021dBridgeMode", 2),
          ("ieee8021dSRBridgeMode", 5),
          ("ieee8021dSRTBridgeMode", 4),
          ("notSupported", 3),
          ("srExpressBridgeMode", 8),
          ("srtBBridgeMode", 7))
    )


_SwSysBridgeMode_Type.__name__ = "Integer32"
_SwSysBridgeMode_Object = MibTableColumn
swSysBridgeMode = _SwSysBridgeMode_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 10, 2, 1, 7),
    _SwSysBridgeMode_Type()
)
swSysBridgeMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSysBridgeMode.setStatus("mandatory")
_SwSysBridgeBackbonePort_Type = Integer32
_SwSysBridgeBackbonePort_Object = MibTableColumn
swSysBridgeBackbonePort = _SwSysBridgeBackbonePort_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 10, 2, 1, 8),
    _SwSysBridgeBackbonePort_Type()
)
swSysBridgeBackbonePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSysBridgeBackbonePort.setStatus("mandatory")


class _SwSysBridgeIpFragmentationEnabled_Type(Integer32):
    """Custom type swSysBridgeIpFragmentationEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("notSupported", 3),
          ("true", 1))
    )


_SwSysBridgeIpFragmentationEnabled_Type.__name__ = "Integer32"
_SwSysBridgeIpFragmentationEnabled_Object = MibTableColumn
swSysBridgeIpFragmentationEnabled = _SwSysBridgeIpFragmentationEnabled_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 10, 2, 1, 9),
    _SwSysBridgeIpFragmentationEnabled_Type()
)
swSysBridgeIpFragmentationEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSysBridgeIpFragmentationEnabled.setStatus("mandatory")


class _SwSysBridgeTrFddiTranslationMode_Type(Integer32):
    """Custom type swSysBridgeTrFddiTranslationMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("backbone", 2),
          ("native", 1))
    )


_SwSysBridgeTrFddiTranslationMode_Type.__name__ = "Integer32"
_SwSysBridgeTrFddiTranslationMode_Object = MibTableColumn
swSysBridgeTrFddiTranslationMode = _SwSysBridgeTrFddiTranslationMode_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 10, 2, 1, 10),
    _SwSysBridgeTrFddiTranslationMode_Type()
)
swSysBridgeTrFddiTranslationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSysBridgeTrFddiTranslationMode.setStatus("mandatory")


class _SwSysBridgeSTPGroupAddress_Type(OctetString):
    """Custom type swSysBridgeSTPGroupAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_SwSysBridgeSTPGroupAddress_Type.__name__ = "OctetString"
_SwSysBridgeSTPGroupAddress_Object = MibTableColumn
swSysBridgeSTPGroupAddress = _SwSysBridgeSTPGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 10, 2, 1, 11),
    _SwSysBridgeSTPGroupAddress_Type()
)
swSysBridgeSTPGroupAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSysBridgeSTPGroupAddress.setStatus("mandatory")


class _SwSysBridgeSTPEnable_Type(Integer32):
    """Custom type swSysBridgeSTPEnable based on Integer32"""
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


_SwSysBridgeSTPEnable_Type.__name__ = "Integer32"
_SwSysBridgeSTPEnable_Object = MibTableColumn
swSysBridgeSTPEnable = _SwSysBridgeSTPEnable_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 10, 2, 1, 12),
    _SwSysBridgeSTPEnable_Type()
)
swSysBridgeSTPEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSysBridgeSTPEnable.setStatus("mandatory")


class _SwSysBridgeIpxSnapTranslationEnable_Type(Integer32):
    """Custom type swSysBridgeIpxSnapTranslationEnable based on Integer32"""
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


_SwSysBridgeIpxSnapTranslationEnable_Type.__name__ = "Integer32"
_SwSysBridgeIpxSnapTranslationEnable_Object = MibTableColumn
swSysBridgeIpxSnapTranslationEnable = _SwSysBridgeIpxSnapTranslationEnable_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 10, 2, 1, 13),
    _SwSysBridgeIpxSnapTranslationEnable_Type()
)
swSysBridgeIpxSnapTranslationEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSysBridgeIpxSnapTranslationEnable.setStatus("mandatory")


class _SwSysBridgeLowLatencyEnable_Type(Integer32):
    """Custom type swSysBridgeLowLatencyEnable based on Integer32"""
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


_SwSysBridgeLowLatencyEnable_Type.__name__ = "Integer32"
_SwSysBridgeLowLatencyEnable_Object = MibTableColumn
swSysBridgeLowLatencyEnable = _SwSysBridgeLowLatencyEnable_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 10, 2, 1, 14),
    _SwSysBridgeLowLatencyEnable_Type()
)
swSysBridgeLowLatencyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSysBridgeLowLatencyEnable.setStatus("mandatory")


class _SwSysBridgeVlanMode_Type(Integer32):
    """Custom type swSysBridgeVlanMode based on Integer32"""
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
        *(("closed", 2),
          ("mixed", 3),
          ("notSupported", 4),
          ("open", 1))
    )


_SwSysBridgeVlanMode_Type.__name__ = "Integer32"
_SwSysBridgeVlanMode_Object = MibTableColumn
swSysBridgeVlanMode = _SwSysBridgeVlanMode_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 10, 2, 1, 15),
    _SwSysBridgeVlanMode_Type()
)
swSysBridgeVlanMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSysBridgeVlanMode.setStatus("mandatory")
_SwSysBridgePortTable_Object = MibTable
swSysBridgePortTable = _SwSysBridgePortTable_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 10, 3)
)
if mibBuilder.loadTexts:
    swSysBridgePortTable.setStatus("mandatory")
_SwSysBridgePortEntry_Object = MibTableRow
swSysBridgePortEntry = _SwSysBridgePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 10, 3, 1)
)
swSysBridgePortEntry.setIndexNames(
    (0, "SWITCHING-SYSTEMS-MIB", "swSysBridgePortBridgeIndex"),
    (0, "SWITCHING-SYSTEMS-MIB", "swSysBridgePortIndex"),
)
if mibBuilder.loadTexts:
    swSysBridgePortEntry.setStatus("mandatory")
_SwSysBridgePortBridgeIndex_Type = Integer32
_SwSysBridgePortBridgeIndex_Object = MibTableColumn
swSysBridgePortBridgeIndex = _SwSysBridgePortBridgeIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 10, 3, 1, 1),
    _SwSysBridgePortBridgeIndex_Type()
)
swSysBridgePortBridgeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysBridgePortBridgeIndex.setStatus("mandatory")
_SwSysBridgePortIndex_Type = Integer32
_SwSysBridgePortIndex_Object = MibTableColumn
swSysBridgePortIndex = _SwSysBridgePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 10, 3, 1, 2),
    _SwSysBridgePortIndex_Type()
)
swSysBridgePortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysBridgePortIndex.setStatus("mandatory")
_SwSysBridgePortIfIndex_Type = Integer32
_SwSysBridgePortIfIndex_Object = MibTableColumn
swSysBridgePortIfIndex = _SwSysBridgePortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 10, 3, 1, 3),
    _SwSysBridgePortIfIndex_Type()
)
swSysBridgePortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysBridgePortIfIndex.setStatus("mandatory")


class _SwSysBridgePortReceiveMulticastLimit_Type(Integer32):
    """Custom type swSysBridgePortReceiveMulticastLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwSysBridgePortReceiveMulticastLimit_Type.__name__ = "Integer32"
_SwSysBridgePortReceiveMulticastLimit_Object = MibTableColumn
swSysBridgePortReceiveMulticastLimit = _SwSysBridgePortReceiveMulticastLimit_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 10, 3, 1, 4),
    _SwSysBridgePortReceiveMulticastLimit_Type()
)
swSysBridgePortReceiveMulticastLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSysBridgePortReceiveMulticastLimit.setStatus("mandatory")


class _SwSysBridgePortAddressAction_Type(Integer32):
    """Custom type swSysBridgePortAddressAction based on Integer32"""
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
        *(("flushAddress", 3),
          ("flushDynamicAddress", 4),
          ("freezeAddress", 2),
          ("other", 1))
    )


_SwSysBridgePortAddressAction_Type.__name__ = "Integer32"
_SwSysBridgePortAddressAction_Object = MibTableColumn
swSysBridgePortAddressAction = _SwSysBridgePortAddressAction_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 10, 3, 1, 5),
    _SwSysBridgePortAddressAction_Type()
)
swSysBridgePortAddressAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSysBridgePortAddressAction.setStatus("mandatory")
_SwSysBridgePortSpanningTreeFrameReceivedCounts_Type = Counter32
_SwSysBridgePortSpanningTreeFrameReceivedCounts_Object = MibTableColumn
swSysBridgePortSpanningTreeFrameReceivedCounts = _SwSysBridgePortSpanningTreeFrameReceivedCounts_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 10, 3, 1, 6),
    _SwSysBridgePortSpanningTreeFrameReceivedCounts_Type()
)
swSysBridgePortSpanningTreeFrameReceivedCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysBridgePortSpanningTreeFrameReceivedCounts.setStatus("mandatory")
_SwSysBridgePortReceiveBlockedDiscards_Type = Counter32
_SwSysBridgePortReceiveBlockedDiscards_Object = MibTableColumn
swSysBridgePortReceiveBlockedDiscards = _SwSysBridgePortReceiveBlockedDiscards_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 10, 3, 1, 7),
    _SwSysBridgePortReceiveBlockedDiscards_Type()
)
swSysBridgePortReceiveBlockedDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysBridgePortReceiveBlockedDiscards.setStatus("mandatory")
_SwSysBridgePortReceiveMulticastLimitExceededs_Type = Counter32
_SwSysBridgePortReceiveMulticastLimitExceededs_Object = MibTableColumn
swSysBridgePortReceiveMulticastLimitExceededs = _SwSysBridgePortReceiveMulticastLimitExceededs_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 10, 3, 1, 8),
    _SwSysBridgePortReceiveMulticastLimitExceededs_Type()
)
swSysBridgePortReceiveMulticastLimitExceededs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysBridgePortReceiveMulticastLimitExceededs.setStatus("mandatory")
_SwSysBridgePortReceiveMulticastLimitExceededDiscards_Type = Counter32
_SwSysBridgePortReceiveMulticastLimitExceededDiscards_Object = MibTableColumn
swSysBridgePortReceiveMulticastLimitExceededDiscards = _SwSysBridgePortReceiveMulticastLimitExceededDiscards_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 10, 3, 1, 9),
    _SwSysBridgePortReceiveMulticastLimitExceededDiscards_Type()
)
swSysBridgePortReceiveMulticastLimitExceededDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysBridgePortReceiveMulticastLimitExceededDiscards.setStatus("mandatory")
_SwSysBridgePortReceiveSecurityDiscards_Type = Counter32
_SwSysBridgePortReceiveSecurityDiscards_Object = MibTableColumn
swSysBridgePortReceiveSecurityDiscards = _SwSysBridgePortReceiveSecurityDiscards_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 10, 3, 1, 10),
    _SwSysBridgePortReceiveSecurityDiscards_Type()
)
swSysBridgePortReceiveSecurityDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysBridgePortReceiveSecurityDiscards.setStatus("mandatory")
_SwSysBridgePortReceiveUnknownDiscards_Type = Counter32
_SwSysBridgePortReceiveUnknownDiscards_Object = MibTableColumn
swSysBridgePortReceiveUnknownDiscards = _SwSysBridgePortReceiveUnknownDiscards_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 10, 3, 1, 11),
    _SwSysBridgePortReceiveUnknownDiscards_Type()
)
swSysBridgePortReceiveUnknownDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysBridgePortReceiveUnknownDiscards.setStatus("mandatory")
_SwSysBridgePortReceiveOtherDiscards_Type = Counter32
_SwSysBridgePortReceiveOtherDiscards_Object = MibTableColumn
swSysBridgePortReceiveOtherDiscards = _SwSysBridgePortReceiveOtherDiscards_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 10, 3, 1, 12),
    _SwSysBridgePortReceiveOtherDiscards_Type()
)
swSysBridgePortReceiveOtherDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysBridgePortReceiveOtherDiscards.setStatus("mandatory")
_SwSysBridgePortReceiveErrorDiscards_Type = Counter32
_SwSysBridgePortReceiveErrorDiscards_Object = MibTableColumn
swSysBridgePortReceiveErrorDiscards = _SwSysBridgePortReceiveErrorDiscards_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 10, 3, 1, 13),
    _SwSysBridgePortReceiveErrorDiscards_Type()
)
swSysBridgePortReceiveErrorDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysBridgePortReceiveErrorDiscards.setStatus("mandatory")
_SwSysBridgePortSameSegmentDiscards_Type = Counter32
_SwSysBridgePortSameSegmentDiscards_Object = MibTableColumn
swSysBridgePortSameSegmentDiscards = _SwSysBridgePortSameSegmentDiscards_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 10, 3, 1, 14),
    _SwSysBridgePortSameSegmentDiscards_Type()
)
swSysBridgePortSameSegmentDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysBridgePortSameSegmentDiscards.setStatus("mandatory")
_SwSysBridgePortTransmitBlockedDiscards_Type = Counter32
_SwSysBridgePortTransmitBlockedDiscards_Object = MibTableColumn
swSysBridgePortTransmitBlockedDiscards = _SwSysBridgePortTransmitBlockedDiscards_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 10, 3, 1, 15),
    _SwSysBridgePortTransmitBlockedDiscards_Type()
)
swSysBridgePortTransmitBlockedDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysBridgePortTransmitBlockedDiscards.setStatus("mandatory")
_SwSysBridgePortReceiveAllPathFilteredFrames_Type = Counter32
_SwSysBridgePortReceiveAllPathFilteredFrames_Object = MibTableColumn
swSysBridgePortReceiveAllPathFilteredFrames = _SwSysBridgePortReceiveAllPathFilteredFrames_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 10, 3, 1, 16),
    _SwSysBridgePortReceiveAllPathFilteredFrames_Type()
)
swSysBridgePortReceiveAllPathFilteredFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysBridgePortReceiveAllPathFilteredFrames.setStatus("mandatory")
_SwSysBridgePortReceiveMulticastPathFilteredFrames_Type = Counter32
_SwSysBridgePortReceiveMulticastPathFilteredFrames_Object = MibTableColumn
swSysBridgePortReceiveMulticastPathFilteredFrames = _SwSysBridgePortReceiveMulticastPathFilteredFrames_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 10, 3, 1, 17),
    _SwSysBridgePortReceiveMulticastPathFilteredFrames_Type()
)
swSysBridgePortReceiveMulticastPathFilteredFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysBridgePortReceiveMulticastPathFilteredFrames.setStatus("mandatory")
_SwSysBridgePortTransmitAllPathFilteredFrames_Type = Counter32
_SwSysBridgePortTransmitAllPathFilteredFrames_Object = MibTableColumn
swSysBridgePortTransmitAllPathFilteredFrames = _SwSysBridgePortTransmitAllPathFilteredFrames_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 10, 3, 1, 18),
    _SwSysBridgePortTransmitAllPathFilteredFrames_Type()
)
swSysBridgePortTransmitAllPathFilteredFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysBridgePortTransmitAllPathFilteredFrames.setStatus("mandatory")
_SwSysBridgePortTransmitMulticastPathFilteredFrames_Type = Counter32
_SwSysBridgePortTransmitMulticastPathFilteredFrames_Object = MibTableColumn
swSysBridgePortTransmitMulticastPathFilteredFrames = _SwSysBridgePortTransmitMulticastPathFilteredFrames_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 10, 3, 1, 19),
    _SwSysBridgePortTransmitMulticastPathFilteredFrames_Type()
)
swSysBridgePortTransmitMulticastPathFilteredFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysBridgePortTransmitMulticastPathFilteredFrames.setStatus("mandatory")
_SwSysBridgePortForwardedUnicastFrames_Type = Counter32
_SwSysBridgePortForwardedUnicastFrames_Object = MibTableColumn
swSysBridgePortForwardedUnicastFrames = _SwSysBridgePortForwardedUnicastFrames_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 10, 3, 1, 20),
    _SwSysBridgePortForwardedUnicastFrames_Type()
)
swSysBridgePortForwardedUnicastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysBridgePortForwardedUnicastFrames.setStatus("mandatory")
_SwSysBridgePortForwardedUnicastOctets_Type = Counter32
_SwSysBridgePortForwardedUnicastOctets_Object = MibTableColumn
swSysBridgePortForwardedUnicastOctets = _SwSysBridgePortForwardedUnicastOctets_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 10, 3, 1, 21),
    _SwSysBridgePortForwardedUnicastOctets_Type()
)
swSysBridgePortForwardedUnicastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysBridgePortForwardedUnicastOctets.setStatus("mandatory")
_SwSysBridgePortForwardedMulticastFrames_Type = Counter32
_SwSysBridgePortForwardedMulticastFrames_Object = MibTableColumn
swSysBridgePortForwardedMulticastFrames = _SwSysBridgePortForwardedMulticastFrames_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 10, 3, 1, 22),
    _SwSysBridgePortForwardedMulticastFrames_Type()
)
swSysBridgePortForwardedMulticastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysBridgePortForwardedMulticastFrames.setStatus("mandatory")
_SwSysBridgePortForwardedMulticastOctets_Type = Counter32
_SwSysBridgePortForwardedMulticastOctets_Object = MibTableColumn
swSysBridgePortForwardedMulticastOctets = _SwSysBridgePortForwardedMulticastOctets_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 10, 3, 1, 23),
    _SwSysBridgePortForwardedMulticastOctets_Type()
)
swSysBridgePortForwardedMulticastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysBridgePortForwardedMulticastOctets.setStatus("mandatory")
_SwSysBridgePortFloodedUnicastFrames_Type = Counter32
_SwSysBridgePortFloodedUnicastFrames_Object = MibTableColumn
swSysBridgePortFloodedUnicastFrames = _SwSysBridgePortFloodedUnicastFrames_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 10, 3, 1, 24),
    _SwSysBridgePortFloodedUnicastFrames_Type()
)
swSysBridgePortFloodedUnicastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysBridgePortFloodedUnicastFrames.setStatus("mandatory")
_SwSysBridgePortFloodedUnicastOctets_Type = Counter32
_SwSysBridgePortFloodedUnicastOctets_Object = MibTableColumn
swSysBridgePortFloodedUnicastOctets = _SwSysBridgePortFloodedUnicastOctets_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 10, 3, 1, 25),
    _SwSysBridgePortFloodedUnicastOctets_Type()
)
swSysBridgePortFloodedUnicastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysBridgePortFloodedUnicastOctets.setStatus("mandatory")


class _SwSysBridgePortStpMode_Type(Integer32):
    """Custom type swSysBridgePortStpMode based on Integer32"""
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
          ("remove", 3))
    )


_SwSysBridgePortStpMode_Type.__name__ = "Integer32"
_SwSysBridgePortStpMode_Object = MibTableColumn
swSysBridgePortStpMode = _SwSysBridgePortStpMode_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 10, 3, 1, 26),
    _SwSysBridgePortStpMode_Type()
)
swSysBridgePortStpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSysBridgePortStpMode.setStatus("mandatory")


class _SwSysBridgePortReceiveMulticastLimitFrameType_Type(Integer32):
    """Custom type swSysBridgePortReceiveMulticastLimitFrameType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("broadcastAndMulticast", 1),
          ("broadcastOnly", 2))
    )


_SwSysBridgePortReceiveMulticastLimitFrameType_Type.__name__ = "Integer32"
_SwSysBridgePortReceiveMulticastLimitFrameType_Object = MibTableColumn
swSysBridgePortReceiveMulticastLimitFrameType = _SwSysBridgePortReceiveMulticastLimitFrameType_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 10, 3, 1, 27),
    _SwSysBridgePortReceiveMulticastLimitFrameType_Type()
)
swSysBridgePortReceiveMulticastLimitFrameType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSysBridgePortReceiveMulticastLimitFrameType.setStatus("mandatory")
_SwSysBridgePortAddressTable_Object = MibTable
swSysBridgePortAddressTable = _SwSysBridgePortAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 10, 5)
)
if mibBuilder.loadTexts:
    swSysBridgePortAddressTable.setStatus("mandatory")
_SwSysBridgePortAddressEntry_Object = MibTableRow
swSysBridgePortAddressEntry = _SwSysBridgePortAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 10, 5, 1)
)
swSysBridgePortAddressEntry.setIndexNames(
    (0, "SWITCHING-SYSTEMS-MIB", "swSysBridgePortAddressBridgeIndex"),
    (0, "SWITCHING-SYSTEMS-MIB", "swSysBridgePortAddressPortIndex"),
    (0, "SWITCHING-SYSTEMS-MIB", "swSysBridgePortAddressIndex"),
)
if mibBuilder.loadTexts:
    swSysBridgePortAddressEntry.setStatus("mandatory")
_SwSysBridgePortAddressBridgeIndex_Type = Integer32
_SwSysBridgePortAddressBridgeIndex_Object = MibTableColumn
swSysBridgePortAddressBridgeIndex = _SwSysBridgePortAddressBridgeIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 10, 5, 1, 1),
    _SwSysBridgePortAddressBridgeIndex_Type()
)
swSysBridgePortAddressBridgeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysBridgePortAddressBridgeIndex.setStatus("mandatory")
_SwSysBridgePortAddressPortIndex_Type = Integer32
_SwSysBridgePortAddressPortIndex_Object = MibTableColumn
swSysBridgePortAddressPortIndex = _SwSysBridgePortAddressPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 10, 5, 1, 2),
    _SwSysBridgePortAddressPortIndex_Type()
)
swSysBridgePortAddressPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysBridgePortAddressPortIndex.setStatus("mandatory")
_SwSysBridgePortAddressIndex_Type = Integer32
_SwSysBridgePortAddressIndex_Object = MibTableColumn
swSysBridgePortAddressIndex = _SwSysBridgePortAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 10, 5, 1, 3),
    _SwSysBridgePortAddressIndex_Type()
)
swSysBridgePortAddressIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysBridgePortAddressIndex.setStatus("mandatory")


class _SwSysBridgePortAddressRemoteAddress_Type(OctetString):
    """Custom type swSysBridgePortAddressRemoteAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_SwSysBridgePortAddressRemoteAddress_Type.__name__ = "OctetString"
_SwSysBridgePortAddressRemoteAddress_Object = MibTableColumn
swSysBridgePortAddressRemoteAddress = _SwSysBridgePortAddressRemoteAddress_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 10, 5, 1, 4),
    _SwSysBridgePortAddressRemoteAddress_Type()
)
swSysBridgePortAddressRemoteAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSysBridgePortAddressRemoteAddress.setStatus("mandatory")


class _SwSysBridgePortAddressType_Type(Integer32):
    """Custom type swSysBridgePortAddressType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_SwSysBridgePortAddressType_Type.__name__ = "Integer32"
_SwSysBridgePortAddressType_Object = MibTableColumn
swSysBridgePortAddressType = _SwSysBridgePortAddressType_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 10, 5, 1, 5),
    _SwSysBridgePortAddressType_Type()
)
swSysBridgePortAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSysBridgePortAddressType.setStatus("mandatory")


class _SwSysBridgePortAddressIsStatic_Type(Integer32):
    """Custom type swSysBridgePortAddressIsStatic based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("isDynamic", 2),
          ("isStatic", 1))
    )


_SwSysBridgePortAddressIsStatic_Type.__name__ = "Integer32"
_SwSysBridgePortAddressIsStatic_Object = MibTableColumn
swSysBridgePortAddressIsStatic = _SwSysBridgePortAddressIsStatic_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 10, 5, 1, 6),
    _SwSysBridgePortAddressIsStatic_Type()
)
swSysBridgePortAddressIsStatic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSysBridgePortAddressIsStatic.setStatus("mandatory")
_SwSysBridgePortAddressStaticPort_Type = Integer32
_SwSysBridgePortAddressStaticPort_Object = MibTableColumn
swSysBridgePortAddressStaticPort = _SwSysBridgePortAddressStaticPort_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 10, 5, 1, 7),
    _SwSysBridgePortAddressStaticPort_Type()
)
swSysBridgePortAddressStaticPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysBridgePortAddressStaticPort.setStatus("mandatory")
_SwSysBridgePortAddressAge_Type = Integer32
_SwSysBridgePortAddressAge_Object = MibTableColumn
swSysBridgePortAddressAge = _SwSysBridgePortAddressAge_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 10, 5, 1, 8),
    _SwSysBridgePortAddressAge_Type()
)
swSysBridgePortAddressAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysBridgePortAddressAge.setStatus("mandatory")


class _SwSysBridgeStpGroupAddress_Type(OctetString):
    """Custom type swSysBridgeStpGroupAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_SwSysBridgeStpGroupAddress_Type.__name__ = "OctetString"
_SwSysBridgeStpGroupAddress_Object = MibScalar
swSysBridgeStpGroupAddress = _SwSysBridgeStpGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 10, 6),
    _SwSysBridgeStpGroupAddress_Type()
)
swSysBridgeStpGroupAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSysBridgeStpGroupAddress.setStatus("obsolete")


class _SwSysBridgeStpEnable_Type(Integer32):
    """Custom type swSysBridgeStpEnable based on Integer32"""
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


_SwSysBridgeStpEnable_Type.__name__ = "Integer32"
_SwSysBridgeStpEnable_Object = MibScalar
swSysBridgeStpEnable = _SwSysBridgeStpEnable_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 10, 7),
    _SwSysBridgeStpEnable_Type()
)
swSysBridgeStpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSysBridgeStpEnable.setStatus("obsolete")
_SwSysIpRouter_ObjectIdentity = ObjectIdentity
swSysIpRouter = _SwSysIpRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 11)
)
_SwSysNetworkMonitor_ObjectIdentity = ObjectIdentity
swSysNetworkMonitor = _SwSysNetworkMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 12)
)
_SwSysNetworkAnalyzerTable_Object = MibTable
swSysNetworkAnalyzerTable = _SwSysNetworkAnalyzerTable_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 12, 1)
)
if mibBuilder.loadTexts:
    swSysNetworkAnalyzerTable.setStatus("mandatory")
_SwSysNetworkAnalyzerTableEntry_Object = MibTableRow
swSysNetworkAnalyzerTableEntry = _SwSysNetworkAnalyzerTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 12, 1, 1)
)
swSysNetworkAnalyzerTableEntry.setIndexNames(
    (0, "SWITCHING-SYSTEMS-MIB", "swSysNetworkAnalyzerBridgeIndex"),
    (0, "SWITCHING-SYSTEMS-MIB", "swSysNetworkAnalyzerBridgePortIndex"),
)
if mibBuilder.loadTexts:
    swSysNetworkAnalyzerTableEntry.setStatus("mandatory")
_SwSysNetworkAnalyzerBridgeIndex_Type = Integer32
_SwSysNetworkAnalyzerBridgeIndex_Object = MibTableColumn
swSysNetworkAnalyzerBridgeIndex = _SwSysNetworkAnalyzerBridgeIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 12, 1, 1, 1),
    _SwSysNetworkAnalyzerBridgeIndex_Type()
)
swSysNetworkAnalyzerBridgeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysNetworkAnalyzerBridgeIndex.setStatus("mandatory")
_SwSysNetworkAnalyzerBridgePortIndex_Type = Integer32
_SwSysNetworkAnalyzerBridgePortIndex_Object = MibTableColumn
swSysNetworkAnalyzerBridgePortIndex = _SwSysNetworkAnalyzerBridgePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 12, 1, 1, 2),
    _SwSysNetworkAnalyzerBridgePortIndex_Type()
)
swSysNetworkAnalyzerBridgePortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysNetworkAnalyzerBridgePortIndex.setStatus("mandatory")


class _SwSysNetworkAnalyzerPhysicalAddress_Type(OctetString):
    """Custom type swSysNetworkAnalyzerPhysicalAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_SwSysNetworkAnalyzerPhysicalAddress_Type.__name__ = "OctetString"
_SwSysNetworkAnalyzerPhysicalAddress_Object = MibTableColumn
swSysNetworkAnalyzerPhysicalAddress = _SwSysNetworkAnalyzerPhysicalAddress_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 12, 1, 1, 3),
    _SwSysNetworkAnalyzerPhysicalAddress_Type()
)
swSysNetworkAnalyzerPhysicalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysNetworkAnalyzerPhysicalAddress.setStatus("mandatory")


class _SwSysNetworkAnalyzerStatus_Type(Integer32):
    """Custom type swSysNetworkAnalyzerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_SwSysNetworkAnalyzerStatus_Type.__name__ = "Integer32"
_SwSysNetworkAnalyzerStatus_Object = MibTableColumn
swSysNetworkAnalyzerStatus = _SwSysNetworkAnalyzerStatus_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 12, 1, 1, 4),
    _SwSysNetworkAnalyzerStatus_Type()
)
swSysNetworkAnalyzerStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSysNetworkAnalyzerStatus.setStatus("mandatory")
_SwSysNetworkPortMonitorTable_Object = MibTable
swSysNetworkPortMonitorTable = _SwSysNetworkPortMonitorTable_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 12, 2)
)
if mibBuilder.loadTexts:
    swSysNetworkPortMonitorTable.setStatus("mandatory")
_SwSysNetworkPortMonitorTableEntry_Object = MibTableRow
swSysNetworkPortMonitorTableEntry = _SwSysNetworkPortMonitorTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 12, 2, 1)
)
swSysNetworkPortMonitorTableEntry.setIndexNames(
    (0, "SWITCHING-SYSTEMS-MIB", "swSysNetworkPortMonitorBridgeIndex"),
    (0, "SWITCHING-SYSTEMS-MIB", "swSysNetworkPortMonitorBridgePortIndex"),
)
if mibBuilder.loadTexts:
    swSysNetworkPortMonitorTableEntry.setStatus("mandatory")
_SwSysNetworkPortMonitorBridgeIndex_Type = Integer32
_SwSysNetworkPortMonitorBridgeIndex_Object = MibTableColumn
swSysNetworkPortMonitorBridgeIndex = _SwSysNetworkPortMonitorBridgeIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 12, 2, 1, 1),
    _SwSysNetworkPortMonitorBridgeIndex_Type()
)
swSysNetworkPortMonitorBridgeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysNetworkPortMonitorBridgeIndex.setStatus("mandatory")
_SwSysNetworkPortMonitorBridgePortIndex_Type = Integer32
_SwSysNetworkPortMonitorBridgePortIndex_Object = MibTableColumn
swSysNetworkPortMonitorBridgePortIndex = _SwSysNetworkPortMonitorBridgePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 12, 2, 1, 2),
    _SwSysNetworkPortMonitorBridgePortIndex_Type()
)
swSysNetworkPortMonitorBridgePortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysNetworkPortMonitorBridgePortIndex.setStatus("mandatory")


class _SwSysNetworkPortMonitorAnalyzerAddress_Type(OctetString):
    """Custom type swSysNetworkPortMonitorAnalyzerAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_SwSysNetworkPortMonitorAnalyzerAddress_Type.__name__ = "OctetString"
_SwSysNetworkPortMonitorAnalyzerAddress_Object = MibTableColumn
swSysNetworkPortMonitorAnalyzerAddress = _SwSysNetworkPortMonitorAnalyzerAddress_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 12, 2, 1, 3),
    _SwSysNetworkPortMonitorAnalyzerAddress_Type()
)
swSysNetworkPortMonitorAnalyzerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSysNetworkPortMonitorAnalyzerAddress.setStatus("mandatory")


class _SwSysNetworkPortMonitorStatus_Type(Integer32):
    """Custom type swSysNetworkPortMonitorStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_SwSysNetworkPortMonitorStatus_Type.__name__ = "Integer32"
_SwSysNetworkPortMonitorStatus_Object = MibTableColumn
swSysNetworkPortMonitorStatus = _SwSysNetworkPortMonitorStatus_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 12, 2, 1, 4),
    _SwSysNetworkPortMonitorStatus_Type()
)
swSysNetworkPortMonitorStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSysNetworkPortMonitorStatus.setStatus("mandatory")
_SwSysTokenRingPort_ObjectIdentity = ObjectIdentity
swSysTokenRingPort = _SwSysTokenRingPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 13)
)
_SwSysTokenRingPortCount_Type = Integer32
_SwSysTokenRingPortCount_Object = MibScalar
swSysTokenRingPortCount = _SwSysTokenRingPortCount_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 13, 1),
    _SwSysTokenRingPortCount_Type()
)
swSysTokenRingPortCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysTokenRingPortCount.setStatus("mandatory")
_SwSysTokenRingPortTable_Object = MibTable
swSysTokenRingPortTable = _SwSysTokenRingPortTable_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 13, 2)
)
if mibBuilder.loadTexts:
    swSysTokenRingPortTable.setStatus("mandatory")
_SwSysTokenRingPortEntry_Object = MibTableRow
swSysTokenRingPortEntry = _SwSysTokenRingPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 13, 2, 1)
)
swSysTokenRingPortEntry.setIndexNames(
    (0, "SWITCHING-SYSTEMS-MIB", "swSysTokenRingPortIndex"),
)
if mibBuilder.loadTexts:
    swSysTokenRingPortEntry.setStatus("mandatory")
_SwSysTokenRingPortIndex_Type = Integer32
_SwSysTokenRingPortIndex_Object = MibTableColumn
swSysTokenRingPortIndex = _SwSysTokenRingPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 13, 2, 1, 1),
    _SwSysTokenRingPortIndex_Type()
)
swSysTokenRingPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysTokenRingPortIndex.setStatus("mandatory")
_SwSysTokenRingPortIfIndex_Type = Integer32
_SwSysTokenRingPortIfIndex_Object = MibTableColumn
swSysTokenRingPortIfIndex = _SwSysTokenRingPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 13, 2, 1, 2),
    _SwSysTokenRingPortIfIndex_Type()
)
swSysTokenRingPortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysTokenRingPortIfIndex.setStatus("mandatory")


class _SwSysTokenRingPortLabel_Type(DisplayString):
    """Custom type swSysTokenRingPortLabel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_SwSysTokenRingPortLabel_Type.__name__ = "DisplayString"
_SwSysTokenRingPortLabel_Object = MibTableColumn
swSysTokenRingPortLabel = _SwSysTokenRingPortLabel_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 13, 2, 1, 3),
    _SwSysTokenRingPortLabel_Type()
)
swSysTokenRingPortLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSysTokenRingPortLabel.setStatus("mandatory")


class _SwSysTokenRingPortInsertStatus_Type(Integer32):
    """Custom type swSysTokenRingPortInsertStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deinserted", 2),
          ("inserted", 1))
    )


_SwSysTokenRingPortInsertStatus_Type.__name__ = "Integer32"
_SwSysTokenRingPortInsertStatus_Object = MibTableColumn
swSysTokenRingPortInsertStatus = _SwSysTokenRingPortInsertStatus_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 13, 2, 1, 4),
    _SwSysTokenRingPortInsertStatus_Type()
)
swSysTokenRingPortInsertStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysTokenRingPortInsertStatus.setStatus("mandatory")


class _SwSysTokenRingPortType_Type(Integer32):
    """Custom type swSysTokenRingPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 2),
          ("rj45", 1))
    )


_SwSysTokenRingPortType_Type.__name__ = "Integer32"
_SwSysTokenRingPortType_Object = MibTableColumn
swSysTokenRingPortType = _SwSysTokenRingPortType_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 13, 2, 1, 5),
    _SwSysTokenRingPortType_Type()
)
swSysTokenRingPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysTokenRingPortType.setStatus("mandatory")


class _SwSysTokenRingPortMode_Type(Integer32):
    """Custom type swSysTokenRingPortMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lobe", 2),
          ("station", 1))
    )


_SwSysTokenRingPortMode_Type.__name__ = "Integer32"
_SwSysTokenRingPortMode_Object = MibTableColumn
swSysTokenRingPortMode = _SwSysTokenRingPortMode_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 13, 2, 1, 6),
    _SwSysTokenRingPortMode_Type()
)
swSysTokenRingPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSysTokenRingPortMode.setStatus("mandatory")


class _SwSysTokenRingPortSpeed_Type(Integer32):
    """Custom type swSysTokenRingPortSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fourMegabit", 1),
          ("sixteenMegabit", 2),
          ("sixteenMegabitETR", 3))
    )


_SwSysTokenRingPortSpeed_Type.__name__ = "Integer32"
_SwSysTokenRingPortSpeed_Object = MibTableColumn
swSysTokenRingPortSpeed = _SwSysTokenRingPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 13, 2, 1, 7),
    _SwSysTokenRingPortSpeed_Type()
)
swSysTokenRingPortSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSysTokenRingPortSpeed.setStatus("mandatory")
_SwSysTokenRingPortLineErrors_Type = Counter32
_SwSysTokenRingPortLineErrors_Object = MibTableColumn
swSysTokenRingPortLineErrors = _SwSysTokenRingPortLineErrors_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 13, 2, 1, 8),
    _SwSysTokenRingPortLineErrors_Type()
)
swSysTokenRingPortLineErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysTokenRingPortLineErrors.setStatus("mandatory")
_SwSysTokenRingPortBurstErrors_Type = Counter32
_SwSysTokenRingPortBurstErrors_Object = MibTableColumn
swSysTokenRingPortBurstErrors = _SwSysTokenRingPortBurstErrors_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 13, 2, 1, 9),
    _SwSysTokenRingPortBurstErrors_Type()
)
swSysTokenRingPortBurstErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysTokenRingPortBurstErrors.setStatus("mandatory")
_SwSysTokenRingPortACErrors_Type = Counter32
_SwSysTokenRingPortACErrors_Object = MibTableColumn
swSysTokenRingPortACErrors = _SwSysTokenRingPortACErrors_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 13, 2, 1, 10),
    _SwSysTokenRingPortACErrors_Type()
)
swSysTokenRingPortACErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysTokenRingPortACErrors.setStatus("mandatory")
_SwSysTokenRingPortAbortTransErrors_Type = Counter32
_SwSysTokenRingPortAbortTransErrors_Object = MibTableColumn
swSysTokenRingPortAbortTransErrors = _SwSysTokenRingPortAbortTransErrors_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 13, 2, 1, 11),
    _SwSysTokenRingPortAbortTransErrors_Type()
)
swSysTokenRingPortAbortTransErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysTokenRingPortAbortTransErrors.setStatus("mandatory")
_SwSysTokenRingPortInternalErrors_Type = Counter32
_SwSysTokenRingPortInternalErrors_Object = MibTableColumn
swSysTokenRingPortInternalErrors = _SwSysTokenRingPortInternalErrors_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 13, 2, 1, 12),
    _SwSysTokenRingPortInternalErrors_Type()
)
swSysTokenRingPortInternalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysTokenRingPortInternalErrors.setStatus("mandatory")
_SwSysTokenRingPortLostFrameErrors_Type = Counter32
_SwSysTokenRingPortLostFrameErrors_Object = MibTableColumn
swSysTokenRingPortLostFrameErrors = _SwSysTokenRingPortLostFrameErrors_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 13, 2, 1, 13),
    _SwSysTokenRingPortLostFrameErrors_Type()
)
swSysTokenRingPortLostFrameErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysTokenRingPortLostFrameErrors.setStatus("mandatory")
_SwSysTokenRingPortReceiveCongestionErrors_Type = Counter32
_SwSysTokenRingPortReceiveCongestionErrors_Object = MibTableColumn
swSysTokenRingPortReceiveCongestionErrors = _SwSysTokenRingPortReceiveCongestionErrors_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 13, 2, 1, 14),
    _SwSysTokenRingPortReceiveCongestionErrors_Type()
)
swSysTokenRingPortReceiveCongestionErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysTokenRingPortReceiveCongestionErrors.setStatus("mandatory")
_SwSysTokenRingPortFrameCopiedErrors_Type = Counter32
_SwSysTokenRingPortFrameCopiedErrors_Object = MibTableColumn
swSysTokenRingPortFrameCopiedErrors = _SwSysTokenRingPortFrameCopiedErrors_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 13, 2, 1, 15),
    _SwSysTokenRingPortFrameCopiedErrors_Type()
)
swSysTokenRingPortFrameCopiedErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysTokenRingPortFrameCopiedErrors.setStatus("mandatory")
_SwSysTokenRingPortTokenErrors_Type = Counter32
_SwSysTokenRingPortTokenErrors_Object = MibTableColumn
swSysTokenRingPortTokenErrors = _SwSysTokenRingPortTokenErrors_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 13, 2, 1, 16),
    _SwSysTokenRingPortTokenErrors_Type()
)
swSysTokenRingPortTokenErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysTokenRingPortTokenErrors.setStatus("mandatory")
_SwSysTokenRingPortSoftErrors_Type = Counter32
_SwSysTokenRingPortSoftErrors_Object = MibTableColumn
swSysTokenRingPortSoftErrors = _SwSysTokenRingPortSoftErrors_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 13, 2, 1, 17),
    _SwSysTokenRingPortSoftErrors_Type()
)
swSysTokenRingPortSoftErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysTokenRingPortSoftErrors.setStatus("mandatory")
_SwSysTokenRingPortHardErrors_Type = Counter32
_SwSysTokenRingPortHardErrors_Object = MibTableColumn
swSysTokenRingPortHardErrors = _SwSysTokenRingPortHardErrors_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 13, 2, 1, 18),
    _SwSysTokenRingPortHardErrors_Type()
)
swSysTokenRingPortHardErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysTokenRingPortHardErrors.setStatus("mandatory")
_SwSysTokenRingPortTransmitBeacons_Type = Counter32
_SwSysTokenRingPortTransmitBeacons_Object = MibTableColumn
swSysTokenRingPortTransmitBeacons = _SwSysTokenRingPortTransmitBeacons_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 13, 2, 1, 19),
    _SwSysTokenRingPortTransmitBeacons_Type()
)
swSysTokenRingPortTransmitBeacons.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysTokenRingPortTransmitBeacons.setStatus("mandatory")
_SwSysTokenRingPortLobeWires_Type = Counter32
_SwSysTokenRingPortLobeWires_Object = MibTableColumn
swSysTokenRingPortLobeWires = _SwSysTokenRingPortLobeWires_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 13, 2, 1, 20),
    _SwSysTokenRingPortLobeWires_Type()
)
swSysTokenRingPortLobeWires.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysTokenRingPortLobeWires.setStatus("mandatory")
_SwSysTokenRingPortRemoves_Type = Counter32
_SwSysTokenRingPortRemoves_Object = MibTableColumn
swSysTokenRingPortRemoves = _SwSysTokenRingPortRemoves_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 13, 2, 1, 21),
    _SwSysTokenRingPortRemoves_Type()
)
swSysTokenRingPortRemoves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysTokenRingPortRemoves.setStatus("mandatory")
_SwSysTokenRingPortSingles_Type = Counter32
_SwSysTokenRingPortSingles_Object = MibTableColumn
swSysTokenRingPortSingles = _SwSysTokenRingPortSingles_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 13, 2, 1, 22),
    _SwSysTokenRingPortSingles_Type()
)
swSysTokenRingPortSingles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysTokenRingPortSingles.setStatus("mandatory")
_SwSysTokenRingPortFreqErrors_Type = Counter32
_SwSysTokenRingPortFreqErrors_Object = MibTableColumn
swSysTokenRingPortFreqErrors = _SwSysTokenRingPortFreqErrors_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 13, 2, 1, 23),
    _SwSysTokenRingPortFreqErrors_Type()
)
swSysTokenRingPortFreqErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysTokenRingPortFreqErrors.setStatus("optional")
_SwSysTokenRingPortRingStatus_Type = Integer32
_SwSysTokenRingPortRingStatus_Object = MibTableColumn
swSysTokenRingPortRingStatus = _SwSysTokenRingPortRingStatus_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 13, 2, 1, 24),
    _SwSysTokenRingPortRingStatus_Type()
)
swSysTokenRingPortRingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysTokenRingPortRingStatus.setStatus("mandatory")
_SwSysFtGroup_ObjectIdentity = ObjectIdentity
swSysFtGroup = _SwSysFtGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 14)
)
_SwSysFtTable_Object = MibTable
swSysFtTable = _SwSysFtTable_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 14, 1)
)
if mibBuilder.loadTexts:
    swSysFtTable.setStatus("mandatory")
_SwSysFtTableEntry_Object = MibTableRow
swSysFtTableEntry = _SwSysFtTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 14, 1, 1)
)
swSysFtTableEntry.setIndexNames(
    (0, "SWITCHING-SYSTEMS-MIB", "swSysFtIndex"),
)
if mibBuilder.loadTexts:
    swSysFtTableEntry.setStatus("mandatory")


class _SwSysFtIndex_Type(Integer32):
    """Custom type swSysFtIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SwSysFtIndex_Type.__name__ = "Integer32"
_SwSysFtIndex_Object = MibTableColumn
swSysFtIndex = _SwSysFtIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 14, 1, 1, 1),
    _SwSysFtIndex_Type()
)
swSysFtIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysFtIndex.setStatus("mandatory")


class _SwSysFtDirection_Type(Integer32):
    """Custom type swSysFtDirection based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("localToRemote", 1),
          ("remoteToLocal", 2))
    )


_SwSysFtDirection_Type.__name__ = "Integer32"
_SwSysFtDirection_Object = MibTableColumn
swSysFtDirection = _SwSysFtDirection_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 14, 1, 1, 2),
    _SwSysFtDirection_Type()
)
swSysFtDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSysFtDirection.setStatus("mandatory")


class _SwSysFtLocalStorageType_Type(SwSysStorageType):
    """Custom type swSysFtLocalStorageType based on SwSysStorageType"""
    defaultValue = 3


_SwSysFtLocalStorageType_Object = MibTableColumn
swSysFtLocalStorageType = _SwSysFtLocalStorageType_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 14, 1, 1, 3),
    _SwSysFtLocalStorageType_Type()
)
swSysFtLocalStorageType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSysFtLocalStorageType.setStatus("mandatory")


class _SwSysFtLocalResourceType_Type(SwSysResourceType):
    """Custom type swSysFtLocalResourceType based on SwSysResourceType"""
    defaultValue = 2


_SwSysFtLocalResourceType_Object = MibTableColumn
swSysFtLocalResourceType = _SwSysFtLocalResourceType_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 14, 1, 1, 4),
    _SwSysFtLocalResourceType_Type()
)
swSysFtLocalResourceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSysFtLocalResourceType.setStatus("mandatory")


class _SwSysFtLocalResourceMask_Type(SwSysResourceBitMask):
    """Custom type swSysFtLocalResourceMask based on SwSysResourceBitMask"""
    defaultHexValue = "80"


_SwSysFtLocalResourceMask_Object = MibTableColumn
swSysFtLocalResourceMask = _SwSysFtLocalResourceMask_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 14, 1, 1, 5),
    _SwSysFtLocalResourceMask_Type()
)
swSysFtLocalResourceMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSysFtLocalResourceMask.setStatus("mandatory")


class _SwSysFtLocalResourceAttribute_Type(ObjectIdentifier):
    """Custom type swSysFtLocalResourceAttribute based on ObjectIdentifier"""
    defaultValue = (1, 3, 6, 1, 4, 1, 114, 1, 4, 14, 2, 1, 1)


_SwSysFtLocalResourceAttribute_Object = MibTableColumn
swSysFtLocalResourceAttribute = _SwSysFtLocalResourceAttribute_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 14, 1, 1, 6),
    _SwSysFtLocalResourceAttribute_Type()
)
swSysFtLocalResourceAttribute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSysFtLocalResourceAttribute.setStatus("mandatory")


class _SwSysFtRemoteAddressType_Type(SwSysAddressType):
    """Custom type swSysFtRemoteAddressType based on SwSysAddressType"""
    defaultValue = 2


_SwSysFtRemoteAddressType_Object = MibTableColumn
swSysFtRemoteAddressType = _SwSysFtRemoteAddressType_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 14, 1, 1, 7),
    _SwSysFtRemoteAddressType_Type()
)
swSysFtRemoteAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSysFtRemoteAddressType.setStatus("mandatory")


class _SwSysFtRemoteAddress_Type(OctetString):
    """Custom type swSysFtRemoteAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SwSysFtRemoteAddress_Type.__name__ = "OctetString"
_SwSysFtRemoteAddress_Object = MibTableColumn
swSysFtRemoteAddress = _SwSysFtRemoteAddress_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 14, 1, 1, 8),
    _SwSysFtRemoteAddress_Type()
)
swSysFtRemoteAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSysFtRemoteAddress.setStatus("mandatory")


class _SwSysFtRemoteFileName_Type(DisplayString):
    """Custom type swSysFtRemoteFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_SwSysFtRemoteFileName_Type.__name__ = "DisplayString"
_SwSysFtRemoteFileName_Object = MibTableColumn
swSysFtRemoteFileName = _SwSysFtRemoteFileName_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 14, 1, 1, 9),
    _SwSysFtRemoteFileName_Type()
)
swSysFtRemoteFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSysFtRemoteFileName.setStatus("mandatory")


class _SwSysFtRemoteUserName_Type(DisplayString):
    """Custom type swSysFtRemoteUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_SwSysFtRemoteUserName_Type.__name__ = "DisplayString"
_SwSysFtRemoteUserName_Object = MibTableColumn
swSysFtRemoteUserName = _SwSysFtRemoteUserName_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 14, 1, 1, 10),
    _SwSysFtRemoteUserName_Type()
)
swSysFtRemoteUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSysFtRemoteUserName.setStatus("mandatory")


class _SwSysFtRemoteUserPassword_Type(OctetString):
    """Custom type swSysFtRemoteUserPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_SwSysFtRemoteUserPassword_Type.__name__ = "OctetString"
_SwSysFtRemoteUserPassword_Object = MibTableColumn
swSysFtRemoteUserPassword = _SwSysFtRemoteUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 14, 1, 1, 11),
    _SwSysFtRemoteUserPassword_Type()
)
swSysFtRemoteUserPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSysFtRemoteUserPassword.setStatus("mandatory")


class _SwSysFtForceTransfer_Type(Integer32):
    """Custom type swSysFtForceTransfer based on Integer32"""
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


_SwSysFtForceTransfer_Type.__name__ = "Integer32"
_SwSysFtForceTransfer_Object = MibTableColumn
swSysFtForceTransfer = _SwSysFtForceTransfer_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 14, 1, 1, 12),
    _SwSysFtForceTransfer_Type()
)
swSysFtForceTransfer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSysFtForceTransfer.setStatus("mandatory")
_SwSysFtBytesTransferred_Type = Counter32
_SwSysFtBytesTransferred_Object = MibTableColumn
swSysFtBytesTransferred = _SwSysFtBytesTransferred_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 14, 1, 1, 13),
    _SwSysFtBytesTransferred_Type()
)
swSysFtBytesTransferred.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysFtBytesTransferred.setStatus("mandatory")


class _SwSysFtStatus_Type(Integer32):
    """Custom type swSysFtStatus based on Integer32"""
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
        *(("statusError", 10),
          ("statusFileIncompatible", 9),
          ("statusFileNotFound", 7),
          ("statusFileTooBig", 8),
          ("statusInProgress", 2),
          ("statusLocalInvalid", 3),
          ("statusRemoteInvalid", 4),
          ("statusRemoteUnreachable", 5),
          ("statusSuccessfulCompletion", 1),
          ("statusUserAuthFailed", 6))
    )


_SwSysFtStatus_Type.__name__ = "Integer32"
_SwSysFtStatus_Object = MibTableColumn
swSysFtStatus = _SwSysFtStatus_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 14, 1, 1, 14),
    _SwSysFtStatus_Type()
)
swSysFtStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysFtStatus.setStatus("mandatory")
_SwSysFtDetailedStatus_Type = ObjectIdentifier
_SwSysFtDetailedStatus_Object = MibTableColumn
swSysFtDetailedStatus = _SwSysFtDetailedStatus_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 14, 1, 1, 15),
    _SwSysFtDetailedStatus_Type()
)
swSysFtDetailedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysFtDetailedStatus.setStatus("mandatory")
_SwSysFtDetailedStatusString_Type = DisplayString
_SwSysFtDetailedStatusString_Object = MibTableColumn
swSysFtDetailedStatusString = _SwSysFtDetailedStatusString_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 14, 1, 1, 16),
    _SwSysFtDetailedStatusString_Type()
)
swSysFtDetailedStatusString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysFtDetailedStatusString.setStatus("mandatory")


class _SwSysFtOwnerString_Type(DisplayString):
    """Custom type swSysFtOwnerString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_SwSysFtOwnerString_Type.__name__ = "DisplayString"
_SwSysFtOwnerString_Object = MibTableColumn
swSysFtOwnerString = _SwSysFtOwnerString_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 14, 1, 1, 17),
    _SwSysFtOwnerString_Type()
)
swSysFtOwnerString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSysFtOwnerString.setStatus("mandatory")
_SwSysFtRowStatus_Type = RowStatus
_SwSysFtRowStatus_Object = MibTableColumn
swSysFtRowStatus = _SwSysFtRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 14, 1, 1, 18),
    _SwSysFtRowStatus_Type()
)
swSysFtRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSysFtRowStatus.setStatus("mandatory")
_SwSysFtResourceAttributes_ObjectIdentity = ObjectIdentity
swSysFtResourceAttributes = _SwSysFtResourceAttributes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 14, 2)
)
_SwSysFtSystemAttributes_ObjectIdentity = ObjectIdentity
swSysFtSystemAttributes = _SwSysFtSystemAttributes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 14, 2, 1)
)
_SwSysFtSystemOperationalCode_ObjectIdentity = ObjectIdentity
swSysFtSystemOperationalCode = _SwSysFtSystemOperationalCode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 14, 2, 1, 1)
)
_SwSysFtSystemConfiguration_ObjectIdentity = ObjectIdentity
swSysFtSystemConfiguration = _SwSysFtSystemConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 14, 2, 1, 2)
)
_SwSysFtSystemBridgeFilterCode_ObjectIdentity = ObjectIdentity
swSysFtSystemBridgeFilterCode = _SwSysFtSystemBridgeFilterCode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 14, 2, 1, 3)
)
_SwSysFtDetailedResourceStatus_ObjectIdentity = ObjectIdentity
swSysFtDetailedResourceStatus = _SwSysFtDetailedResourceStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 14, 3)
)
_SwSysFtSystemDetailedStatus_ObjectIdentity = ObjectIdentity
swSysFtSystemDetailedStatus = _SwSysFtSystemDetailedStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 14, 3, 1)
)
_SwSysFtSysStatusNotApplicable_ObjectIdentity = ObjectIdentity
swSysFtSysStatusNotApplicable = _SwSysFtSysStatusNotApplicable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 14, 3, 1, 1)
)
_SwSysFtSysStatusNoImageLabel_ObjectIdentity = ObjectIdentity
swSysFtSysStatusNoImageLabel = _SwSysFtSysStatusNoImageLabel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 14, 3, 1, 2)
)
_SwSysFtSysStatusConfigIdMismatch_ObjectIdentity = ObjectIdentity
swSysFtSysStatusConfigIdMismatch = _SwSysFtSysStatusConfigIdMismatch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 14, 3, 1, 3)
)
_SwSysFtSysStatusChecksumError_ObjectIdentity = ObjectIdentity
swSysFtSysStatusChecksumError = _SwSysFtSysStatusChecksumError_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 14, 3, 1, 4)
)
_SwSysFtSysStatusNvRamError_ObjectIdentity = ObjectIdentity
swSysFtSysStatusNvRamError = _SwSysFtSysStatusNvRamError_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 14, 3, 1, 5)
)
_SwSysFtSysStatusFlashError_ObjectIdentity = ObjectIdentity
swSysFtSysStatusFlashError = _SwSysFtSysStatusFlashError_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 14, 3, 1, 6)
)
_SwSysFtSysStatusNoRoom_ObjectIdentity = ObjectIdentity
swSysFtSysStatusNoRoom = _SwSysFtSysStatusNoRoom_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 14, 3, 1, 7)
)
_SwSysFtSysBridgeFilterNotApplicable_ObjectIdentity = ObjectIdentity
swSysFtSysBridgeFilterNotApplicable = _SwSysFtSysBridgeFilterNotApplicable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 14, 3, 1, 8)
)
_SwSysFtSysBridgeFilterSyntaxError_ObjectIdentity = ObjectIdentity
swSysFtSysBridgeFilterSyntaxError = _SwSysFtSysBridgeFilterSyntaxError_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 14, 3, 1, 9)
)
_SwSysFtSysBridgeFilterdownloadError_ObjectIdentity = ObjectIdentity
swSysFtSysBridgeFilterdownloadError = _SwSysFtSysBridgeFilterdownloadError_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 14, 3, 1, 10)
)
_SwSysFtSysBridgeFilterNoRoom_ObjectIdentity = ObjectIdentity
swSysFtSysBridgeFilterNoRoom = _SwSysFtSysBridgeFilterNoRoom_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 14, 3, 1, 11)
)
_SwSysIpGroup_ObjectIdentity = ObjectIdentity
swSysIpGroup = _SwSysIpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 15)
)
_SwSysIpBaseGroup_ObjectIdentity = ObjectIdentity
swSysIpBaseGroup = _SwSysIpBaseGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 15, 1)
)
_SwSysIpInterfaceGroup_ObjectIdentity = ObjectIdentity
swSysIpInterfaceGroup = _SwSysIpInterfaceGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 15, 2)
)
_SwSysIpInterfaceCount_Type = Integer32
_SwSysIpInterfaceCount_Object = MibScalar
swSysIpInterfaceCount = _SwSysIpInterfaceCount_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 15, 2, 1),
    _SwSysIpInterfaceCount_Type()
)
swSysIpInterfaceCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysIpInterfaceCount.setStatus("mandatory")
_SwSysIpInterfaceTable_Object = MibTable
swSysIpInterfaceTable = _SwSysIpInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 15, 2, 2)
)
if mibBuilder.loadTexts:
    swSysIpInterfaceTable.setStatus("mandatory")
_SwSysIpInterfaceEntry_Object = MibTableRow
swSysIpInterfaceEntry = _SwSysIpInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 15, 2, 2, 1)
)
swSysIpInterfaceEntry.setIndexNames(
    (0, "SWITCHING-SYSTEMS-MIB", "swSysIpInterfaceIpStackIndex"),
    (0, "SWITCHING-SYSTEMS-MIB", "swSysIpInterfaceAddr"),
    (0, "SWITCHING-SYSTEMS-MIB", "swSysIpInterfaceNetMask"),
)
if mibBuilder.loadTexts:
    swSysIpInterfaceEntry.setStatus("mandatory")
_SwSysIpInterfaceIpStackIndex_Type = Integer32
_SwSysIpInterfaceIpStackIndex_Object = MibTableColumn
swSysIpInterfaceIpStackIndex = _SwSysIpInterfaceIpStackIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 15, 2, 2, 1, 1),
    _SwSysIpInterfaceIpStackIndex_Type()
)
swSysIpInterfaceIpStackIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysIpInterfaceIpStackIndex.setStatus("mandatory")
_SwSysIpInterfaceAddr_Type = IpAddress
_SwSysIpInterfaceAddr_Object = MibTableColumn
swSysIpInterfaceAddr = _SwSysIpInterfaceAddr_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 15, 2, 2, 1, 2),
    _SwSysIpInterfaceAddr_Type()
)
swSysIpInterfaceAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysIpInterfaceAddr.setStatus("mandatory")
_SwSysIpInterfaceNetMask_Type = IpAddress
_SwSysIpInterfaceNetMask_Object = MibTableColumn
swSysIpInterfaceNetMask = _SwSysIpInterfaceNetMask_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 15, 2, 2, 1, 3),
    _SwSysIpInterfaceNetMask_Type()
)
swSysIpInterfaceNetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysIpInterfaceNetMask.setStatus("mandatory")
_SwSysIpInterfaceIndex_Type = Integer32
_SwSysIpInterfaceIndex_Object = MibTableColumn
swSysIpInterfaceIndex = _SwSysIpInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 15, 2, 2, 1, 4),
    _SwSysIpInterfaceIndex_Type()
)
swSysIpInterfaceIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSysIpInterfaceIndex.setStatus("mandatory")


class _SwSysIpInterfaceBcastAddr_Type(Integer32):
    """Custom type swSysIpInterfaceBcastAddr based on Integer32"""
    defaultValue = 1


_SwSysIpInterfaceBcastAddr_Object = MibTableColumn
swSysIpInterfaceBcastAddr = _SwSysIpInterfaceBcastAddr_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 15, 2, 2, 1, 5),
    _SwSysIpInterfaceBcastAddr_Type()
)
swSysIpInterfaceBcastAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSysIpInterfaceBcastAddr.setStatus("mandatory")


class _SwSysIpInterfaceCost_Type(Integer32):
    """Custom type swSysIpInterfaceCost based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_SwSysIpInterfaceCost_Type.__name__ = "Integer32"
_SwSysIpInterfaceCost_Object = MibTableColumn
swSysIpInterfaceCost = _SwSysIpInterfaceCost_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 15, 2, 2, 1, 6),
    _SwSysIpInterfaceCost_Type()
)
swSysIpInterfaceCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSysIpInterfaceCost.setStatus("mandatory")
_SwSysIpInterfaceStatus_Type = RowStatus
_SwSysIpInterfaceStatus_Object = MibTableColumn
swSysIpInterfaceStatus = _SwSysIpInterfaceStatus_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 15, 2, 2, 1, 7),
    _SwSysIpInterfaceStatus_Type()
)
swSysIpInterfaceStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSysIpInterfaceStatus.setStatus("mandatory")
_SwSysIpxGroup_ObjectIdentity = ObjectIdentity
swSysIpxGroup = _SwSysIpxGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 16)
)
_SwSysIpxBaseGroup_ObjectIdentity = ObjectIdentity
swSysIpxBaseGroup = _SwSysIpxBaseGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 16, 1)
)
_SwSysIpxInterfaceGroup_ObjectIdentity = ObjectIdentity
swSysIpxInterfaceGroup = _SwSysIpxInterfaceGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 16, 2)
)
_SwSysIpxInterfaceCount_Type = Integer32
_SwSysIpxInterfaceCount_Object = MibScalar
swSysIpxInterfaceCount = _SwSysIpxInterfaceCount_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 16, 2, 1),
    _SwSysIpxInterfaceCount_Type()
)
swSysIpxInterfaceCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysIpxInterfaceCount.setStatus("mandatory")
_SwSysIpxInterfaceTable_Object = MibTable
swSysIpxInterfaceTable = _SwSysIpxInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 16, 2, 2)
)
if mibBuilder.loadTexts:
    swSysIpxInterfaceTable.setStatus("mandatory")
_SwSysIpxInterfaceEntry_Object = MibTableRow
swSysIpxInterfaceEntry = _SwSysIpxInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 16, 2, 2, 1)
)
swSysIpxInterfaceEntry.setIndexNames(
    (0, "SWITCHING-SYSTEMS-MIB", "swSysIpxInterfaceIpxStackIndex"),
    (0, "SWITCHING-SYSTEMS-MIB", "swSysIpxInterfaceNetNumber"),
)
if mibBuilder.loadTexts:
    swSysIpxInterfaceEntry.setStatus("mandatory")
_SwSysIpxInterfaceIpxStackIndex_Type = Integer32
_SwSysIpxInterfaceIpxStackIndex_Object = MibTableColumn
swSysIpxInterfaceIpxStackIndex = _SwSysIpxInterfaceIpxStackIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 16, 2, 2, 1, 1),
    _SwSysIpxInterfaceIpxStackIndex_Type()
)
swSysIpxInterfaceIpxStackIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysIpxInterfaceIpxStackIndex.setStatus("mandatory")
_SwSysIpxInterfaceNetNumber_Type = IpxNetworkNumber
_SwSysIpxInterfaceNetNumber_Object = MibTableColumn
swSysIpxInterfaceNetNumber = _SwSysIpxInterfaceNetNumber_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 16, 2, 2, 1, 2),
    _SwSysIpxInterfaceNetNumber_Type()
)
swSysIpxInterfaceNetNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysIpxInterfaceNetNumber.setStatus("mandatory")
_SwSysIpxInterfaceIfIndex_Type = Integer32
_SwSysIpxInterfaceIfIndex_Object = MibTableColumn
swSysIpxInterfaceIfIndex = _SwSysIpxInterfaceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 16, 2, 2, 1, 3),
    _SwSysIpxInterfaceIfIndex_Type()
)
swSysIpxInterfaceIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSysIpxInterfaceIfIndex.setStatus("mandatory")


class _SwSysIpxInterfaceCost_Type(Integer32):
    """Custom type swSysIpxInterfaceCost based on Integer32"""
    defaultValue = 1


_SwSysIpxInterfaceCost_Object = MibTableColumn
swSysIpxInterfaceCost = _SwSysIpxInterfaceCost_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 16, 2, 2, 1, 4),
    _SwSysIpxInterfaceCost_Type()
)
swSysIpxInterfaceCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSysIpxInterfaceCost.setStatus("mandatory")


class _SwSysIpxInterfaceFrameType_Type(Integer32):
    """Custom type swSysIpxInterfaceFrameType based on Integer32"""
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
        *(("frame-802-2", 2),
          ("frame-802-3-Raw", 3),
          ("frame-SNAP", 4),
          ("frame-ethernetII", 1))
    )


_SwSysIpxInterfaceFrameType_Type.__name__ = "Integer32"
_SwSysIpxInterfaceFrameType_Object = MibTableColumn
swSysIpxInterfaceFrameType = _SwSysIpxInterfaceFrameType_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 16, 2, 2, 1, 5),
    _SwSysIpxInterfaceFrameType_Type()
)
swSysIpxInterfaceFrameType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSysIpxInterfaceFrameType.setStatus("mandatory")
_SwSysIpxInterfaceStatus_Type = RowStatus
_SwSysIpxInterfaceStatus_Object = MibTableColumn
swSysIpxInterfaceStatus = _SwSysIpxInterfaceStatus_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 16, 2, 2, 1, 6),
    _SwSysIpxInterfaceStatus_Type()
)
swSysIpxInterfaceStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSysIpxInterfaceStatus.setStatus("mandatory")
_SwSysAppleTalkGroup_ObjectIdentity = ObjectIdentity
swSysAppleTalkGroup = _SwSysAppleTalkGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 17)
)
_SwSysAppleTalkBaseGroup_ObjectIdentity = ObjectIdentity
swSysAppleTalkBaseGroup = _SwSysAppleTalkBaseGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 17, 1)
)
_SwSysAppleTalkInterfaceGroup_ObjectIdentity = ObjectIdentity
swSysAppleTalkInterfaceGroup = _SwSysAppleTalkInterfaceGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 17, 2)
)
_SwSysAtInterfaceCount_Type = Integer32
_SwSysAtInterfaceCount_Object = MibScalar
swSysAtInterfaceCount = _SwSysAtInterfaceCount_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 17, 2, 1),
    _SwSysAtInterfaceCount_Type()
)
swSysAtInterfaceCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysAtInterfaceCount.setStatus("mandatory")
_SwSysAtInterfaceTable_Object = MibTable
swSysAtInterfaceTable = _SwSysAtInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 17, 2, 2)
)
if mibBuilder.loadTexts:
    swSysAtInterfaceTable.setStatus("mandatory")
_SwSysAtInterfaceEntry_Object = MibTableRow
swSysAtInterfaceEntry = _SwSysAtInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 17, 2, 2, 1)
)
swSysAtInterfaceEntry.setIndexNames(
    (0, "SWITCHING-SYSTEMS-MIB", "swSysAtInterfaceAtStackIndex"),
    (0, "SWITCHING-SYSTEMS-MIB", "swSysAtInterfaceIfIndex"),
)
if mibBuilder.loadTexts:
    swSysAtInterfaceEntry.setStatus("mandatory")
_SwSysAtInterfaceAtStackIndex_Type = Integer32
_SwSysAtInterfaceAtStackIndex_Object = MibTableColumn
swSysAtInterfaceAtStackIndex = _SwSysAtInterfaceAtStackIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 17, 2, 2, 1, 1),
    _SwSysAtInterfaceAtStackIndex_Type()
)
swSysAtInterfaceAtStackIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSysAtInterfaceAtStackIndex.setStatus("mandatory")
_SwSysAtInterfaceNetAddress_Type = DdpNodeAddress
_SwSysAtInterfaceNetAddress_Object = MibTableColumn
swSysAtInterfaceNetAddress = _SwSysAtInterfaceNetAddress_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 17, 2, 2, 1, 2),
    _SwSysAtInterfaceNetAddress_Type()
)
swSysAtInterfaceNetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysAtInterfaceNetAddress.setStatus("mandatory")


class _SwSysAtInterfaceType_Type(Integer32):
    """Custom type swSysAtInterfaceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nonseedInterface", 2),
          ("seedInterface", 1))
    )


_SwSysAtInterfaceType_Type.__name__ = "Integer32"
_SwSysAtInterfaceType_Object = MibTableColumn
swSysAtInterfaceType = _SwSysAtInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 17, 2, 2, 1, 3),
    _SwSysAtInterfaceType_Type()
)
swSysAtInterfaceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSysAtInterfaceType.setStatus("mandatory")
_SwSysAtInterfaceNetStart_Type = ATNetworkNumber
_SwSysAtInterfaceNetStart_Object = MibTableColumn
swSysAtInterfaceNetStart = _SwSysAtInterfaceNetStart_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 17, 2, 2, 1, 4),
    _SwSysAtInterfaceNetStart_Type()
)
swSysAtInterfaceNetStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSysAtInterfaceNetStart.setStatus("mandatory")
_SwSysAtInterfaceNetEnd_Type = ATNetworkNumber
_SwSysAtInterfaceNetEnd_Object = MibTableColumn
swSysAtInterfaceNetEnd = _SwSysAtInterfaceNetEnd_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 17, 2, 2, 1, 5),
    _SwSysAtInterfaceNetEnd_Type()
)
swSysAtInterfaceNetEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSysAtInterfaceNetEnd.setStatus("mandatory")
_SwSysAtInterfaceZoneDefault_Type = ATName
_SwSysAtInterfaceZoneDefault_Object = MibTableColumn
swSysAtInterfaceZoneDefault = _SwSysAtInterfaceZoneDefault_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 17, 2, 2, 1, 6),
    _SwSysAtInterfaceZoneDefault_Type()
)
swSysAtInterfaceZoneDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSysAtInterfaceZoneDefault.setStatus("mandatory")
_SwSysAtInterfaceZone1_Type = ATName
_SwSysAtInterfaceZone1_Object = MibTableColumn
swSysAtInterfaceZone1 = _SwSysAtInterfaceZone1_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 17, 2, 2, 1, 7),
    _SwSysAtInterfaceZone1_Type()
)
swSysAtInterfaceZone1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSysAtInterfaceZone1.setStatus("mandatory")
_SwSysAtInterfaceZone2_Type = ATName
_SwSysAtInterfaceZone2_Object = MibTableColumn
swSysAtInterfaceZone2 = _SwSysAtInterfaceZone2_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 17, 2, 2, 1, 8),
    _SwSysAtInterfaceZone2_Type()
)
swSysAtInterfaceZone2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSysAtInterfaceZone2.setStatus("mandatory")
_SwSysAtInterfaceZone3_Type = ATName
_SwSysAtInterfaceZone3_Object = MibTableColumn
swSysAtInterfaceZone3 = _SwSysAtInterfaceZone3_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 17, 2, 2, 1, 9),
    _SwSysAtInterfaceZone3_Type()
)
swSysAtInterfaceZone3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSysAtInterfaceZone3.setStatus("mandatory")
_SwSysAtInterfaceZone4_Type = ATName
_SwSysAtInterfaceZone4_Object = MibTableColumn
swSysAtInterfaceZone4 = _SwSysAtInterfaceZone4_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 17, 2, 2, 1, 10),
    _SwSysAtInterfaceZone4_Type()
)
swSysAtInterfaceZone4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSysAtInterfaceZone4.setStatus("mandatory")
_SwSysAtInterfaceZone5_Type = ATName
_SwSysAtInterfaceZone5_Object = MibTableColumn
swSysAtInterfaceZone5 = _SwSysAtInterfaceZone5_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 17, 2, 2, 1, 11),
    _SwSysAtInterfaceZone5_Type()
)
swSysAtInterfaceZone5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSysAtInterfaceZone5.setStatus("mandatory")
_SwSysAtInterfaceZone6_Type = ATName
_SwSysAtInterfaceZone6_Object = MibTableColumn
swSysAtInterfaceZone6 = _SwSysAtInterfaceZone6_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 17, 2, 2, 1, 12),
    _SwSysAtInterfaceZone6_Type()
)
swSysAtInterfaceZone6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSysAtInterfaceZone6.setStatus("mandatory")
_SwSysAtInterfaceZone7_Type = ATName
_SwSysAtInterfaceZone7_Object = MibTableColumn
swSysAtInterfaceZone7 = _SwSysAtInterfaceZone7_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 17, 2, 2, 1, 13),
    _SwSysAtInterfaceZone7_Type()
)
swSysAtInterfaceZone7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSysAtInterfaceZone7.setStatus("mandatory")
_SwSysAtInterfaceZone8_Type = ATName
_SwSysAtInterfaceZone8_Object = MibTableColumn
swSysAtInterfaceZone8 = _SwSysAtInterfaceZone8_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 17, 2, 2, 1, 14),
    _SwSysAtInterfaceZone8_Type()
)
swSysAtInterfaceZone8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSysAtInterfaceZone8.setStatus("mandatory")
_SwSysAtInterfaceZone9_Type = ATName
_SwSysAtInterfaceZone9_Object = MibTableColumn
swSysAtInterfaceZone9 = _SwSysAtInterfaceZone9_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 17, 2, 2, 1, 15),
    _SwSysAtInterfaceZone9_Type()
)
swSysAtInterfaceZone9.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSysAtInterfaceZone9.setStatus("mandatory")
_SwSysAtInterfaceZone10_Type = ATName
_SwSysAtInterfaceZone10_Object = MibTableColumn
swSysAtInterfaceZone10 = _SwSysAtInterfaceZone10_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 17, 2, 2, 1, 16),
    _SwSysAtInterfaceZone10_Type()
)
swSysAtInterfaceZone10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSysAtInterfaceZone10.setStatus("mandatory")
_SwSysAtInterfaceZone11_Type = ATName
_SwSysAtInterfaceZone11_Object = MibTableColumn
swSysAtInterfaceZone11 = _SwSysAtInterfaceZone11_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 17, 2, 2, 1, 17),
    _SwSysAtInterfaceZone11_Type()
)
swSysAtInterfaceZone11.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSysAtInterfaceZone11.setStatus("mandatory")
_SwSysAtInterfaceZone12_Type = ATName
_SwSysAtInterfaceZone12_Object = MibTableColumn
swSysAtInterfaceZone12 = _SwSysAtInterfaceZone12_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 17, 2, 2, 1, 18),
    _SwSysAtInterfaceZone12_Type()
)
swSysAtInterfaceZone12.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSysAtInterfaceZone12.setStatus("mandatory")
_SwSysAtInterfaceZone13_Type = ATName
_SwSysAtInterfaceZone13_Object = MibTableColumn
swSysAtInterfaceZone13 = _SwSysAtInterfaceZone13_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 17, 2, 2, 1, 19),
    _SwSysAtInterfaceZone13_Type()
)
swSysAtInterfaceZone13.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSysAtInterfaceZone13.setStatus("mandatory")
_SwSysAtInterfaceZone14_Type = ATName
_SwSysAtInterfaceZone14_Object = MibTableColumn
swSysAtInterfaceZone14 = _SwSysAtInterfaceZone14_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 17, 2, 2, 1, 20),
    _SwSysAtInterfaceZone14_Type()
)
swSysAtInterfaceZone14.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSysAtInterfaceZone14.setStatus("mandatory")
_SwSysAtInterfaceZone15_Type = ATName
_SwSysAtInterfaceZone15_Object = MibTableColumn
swSysAtInterfaceZone15 = _SwSysAtInterfaceZone15_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 17, 2, 2, 1, 21),
    _SwSysAtInterfaceZone15_Type()
)
swSysAtInterfaceZone15.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSysAtInterfaceZone15.setStatus("mandatory")
_SwSysAtInterfaceIfIndex_Type = Integer32
_SwSysAtInterfaceIfIndex_Object = MibTableColumn
swSysAtInterfaceIfIndex = _SwSysAtInterfaceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 17, 2, 2, 1, 22),
    _SwSysAtInterfaceIfIndex_Type()
)
swSysAtInterfaceIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSysAtInterfaceIfIndex.setStatus("mandatory")


class _SwSysAtInterfaceState_Type(Integer32):
    """Custom type swSysAtInterfaceState based on Integer32"""
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
        *(("discover", 7),
          ("down", 5),
          ("enabled", 9),
          ("failed", 4),
          ("initialize", 2),
          ("terminate", 3),
          ("unused", 1),
          ("validate", 6),
          ("waiting", 8))
    )


_SwSysAtInterfaceState_Type.__name__ = "Integer32"
_SwSysAtInterfaceState_Object = MibTableColumn
swSysAtInterfaceState = _SwSysAtInterfaceState_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 17, 2, 2, 1, 23),
    _SwSysAtInterfaceState_Type()
)
swSysAtInterfaceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysAtInterfaceState.setStatus("mandatory")
_SwSysAtInterfaceStatus_Type = RowStatus
_SwSysAtInterfaceStatus_Object = MibTableColumn
swSysAtInterfaceStatus = _SwSysAtInterfaceStatus_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 17, 2, 2, 1, 24),
    _SwSysAtInterfaceStatus_Type()
)
swSysAtInterfaceStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSysAtInterfaceStatus.setStatus("mandatory")
_SwSysModuleCardGroup_ObjectIdentity = ObjectIdentity
swSysModuleCardGroup = _SwSysModuleCardGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 18)
)
_SwSysModuleCardCount_Type = Integer32
_SwSysModuleCardCount_Object = MibScalar
swSysModuleCardCount = _SwSysModuleCardCount_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 18, 1),
    _SwSysModuleCardCount_Type()
)
swSysModuleCardCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysModuleCardCount.setStatus("mandatory")
_SwSysModuleCardInfoTable_Object = MibTable
swSysModuleCardInfoTable = _SwSysModuleCardInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 18, 2)
)
if mibBuilder.loadTexts:
    swSysModuleCardInfoTable.setStatus("mandatory")
_SwSysModuleCardInfoEntry_Object = MibTableRow
swSysModuleCardInfoEntry = _SwSysModuleCardInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 18, 2, 1)
)
swSysModuleCardInfoEntry.setIndexNames(
    (0, "SWITCHING-SYSTEMS-MIB", "swSysModuleCardInfoIndex"),
)
if mibBuilder.loadTexts:
    swSysModuleCardInfoEntry.setStatus("mandatory")
_SwSysModuleCardInfoIndex_Type = Integer32
_SwSysModuleCardInfoIndex_Object = MibTableColumn
swSysModuleCardInfoIndex = _SwSysModuleCardInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 18, 2, 1, 1),
    _SwSysModuleCardInfoIndex_Type()
)
swSysModuleCardInfoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysModuleCardInfoIndex.setStatus("mandatory")


class _SwSysModuleCardInfoFamily_Type(Integer32):
    """Custom type swSysModuleCardInfoFamily based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("coreBuilder3500", 1),
          ("superStack7000", 2),
          ("superStack9000", 3))
    )


_SwSysModuleCardInfoFamily_Type.__name__ = "Integer32"
_SwSysModuleCardInfoFamily_Object = MibTableColumn
swSysModuleCardInfoFamily = _SwSysModuleCardInfoFamily_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 18, 2, 1, 2),
    _SwSysModuleCardInfoFamily_Type()
)
swSysModuleCardInfoFamily.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysModuleCardInfoFamily.setStatus("mandatory")


class _SwSysModuleCardInfoGenericType_Type(Integer32):
    """Custom type swSysModuleCardInfoGenericType based on Integer32"""
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
        *(("atmAdaptor", 6),
          ("backplaneOrMotherboard", 1),
          ("enet10MbAnd100MbAdaptor", 3),
          ("enet1GbAdaptor", 4),
          ("fddiAdaptor", 5),
          ("processorBoard", 2))
    )


_SwSysModuleCardInfoGenericType_Type.__name__ = "Integer32"
_SwSysModuleCardInfoGenericType_Object = MibTableColumn
swSysModuleCardInfoGenericType = _SwSysModuleCardInfoGenericType_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 18, 2, 1, 3),
    _SwSysModuleCardInfoGenericType_Type()
)
swSysModuleCardInfoGenericType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysModuleCardInfoGenericType.setStatus("mandatory")


class _SwSysModuleCardInfoSpecificType_Type(Integer32):
    """Custom type swSysModuleCardInfoSpecificType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              161,
              162,
              163,
              164,
              177,
              178,
              179,
              180,
              225,
              226,
              227,
              228,
              229,
              241,
              242,
              243,
              244)
        )
    )
    namedValues = NamedValues(
        *(("atmSonetOC12Copper", 164),
          ("atmSonetOC12Fiber", 162),
          ("atmSonetOC3Copper", 163),
          ("atmSonetOC3Fiber", 161),
          ("enet100Mb100BaseFx", 227),
          ("enet100Mb100BaseT2", 226),
          ("enet100Mb100BaseT4", 228),
          ("enet100Mb100BaseTx", 225),
          ("enet100Mb100BaseTxSTP", 229),
          ("enet1Gb1000BaseTx", 180),
          ("enet1Gb1300nMFiber", 178),
          ("enet1Gb850nMMultimodeFiber", 177),
          ("enet1GbCoax", 179),
          ("fddiCopperSTP", 244),
          ("fddiCopperUTP", 243),
          ("fddiMultimodeSC", 241),
          ("fddiSingleModeSC", 242),
          ("notApplicable", 1))
    )


_SwSysModuleCardInfoSpecificType_Type.__name__ = "Integer32"
_SwSysModuleCardInfoSpecificType_Object = MibTableColumn
swSysModuleCardInfoSpecificType = _SwSysModuleCardInfoSpecificType_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 18, 2, 1, 4),
    _SwSysModuleCardInfoSpecificType_Type()
)
swSysModuleCardInfoSpecificType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysModuleCardInfoSpecificType.setStatus("mandatory")
_SwSysModuleCardInfoPartNumber_Type = DisplayString
_SwSysModuleCardInfoPartNumber_Object = MibTableColumn
swSysModuleCardInfoPartNumber = _SwSysModuleCardInfoPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 18, 2, 1, 5),
    _SwSysModuleCardInfoPartNumber_Type()
)
swSysModuleCardInfoPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysModuleCardInfoPartNumber.setStatus("mandatory")
_SwSysModuleCardInfoManufacturingDate_Type = DisplayString
_SwSysModuleCardInfoManufacturingDate_Object = MibTableColumn
swSysModuleCardInfoManufacturingDate = _SwSysModuleCardInfoManufacturingDate_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 18, 2, 1, 6),
    _SwSysModuleCardInfoManufacturingDate_Type()
)
swSysModuleCardInfoManufacturingDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysModuleCardInfoManufacturingDate.setStatus("mandatory")


class _SwSysModuleCardInfoModuleSerialNumber_Type(DisplayString):
    """Custom type swSysModuleCardInfoModuleSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )


_SwSysModuleCardInfoModuleSerialNumber_Type.__name__ = "DisplayString"
_SwSysModuleCardInfoModuleSerialNumber_Object = MibTableColumn
swSysModuleCardInfoModuleSerialNumber = _SwSysModuleCardInfoModuleSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 18, 2, 1, 7),
    _SwSysModuleCardInfoModuleSerialNumber_Type()
)
swSysModuleCardInfoModuleSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysModuleCardInfoModuleSerialNumber.setStatus("mandatory")


class _SwSysModuleCardInfoTLASerialNumber_Type(DisplayString):
    """Custom type swSysModuleCardInfoTLASerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )


_SwSysModuleCardInfoTLASerialNumber_Type.__name__ = "DisplayString"
_SwSysModuleCardInfoTLASerialNumber_Object = MibTableColumn
swSysModuleCardInfoTLASerialNumber = _SwSysModuleCardInfoTLASerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 18, 2, 1, 8),
    _SwSysModuleCardInfoTLASerialNumber_Type()
)
swSysModuleCardInfoTLASerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysModuleCardInfoTLASerialNumber.setStatus("mandatory")


class _SwSysModuleCardInfo3CNumber_Type(DisplayString):
    """Custom type swSysModuleCardInfo3CNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )


_SwSysModuleCardInfo3CNumber_Type.__name__ = "DisplayString"
_SwSysModuleCardInfo3CNumber_Object = MibTableColumn
swSysModuleCardInfo3CNumber = _SwSysModuleCardInfo3CNumber_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 18, 2, 1, 9),
    _SwSysModuleCardInfo3CNumber_Type()
)
swSysModuleCardInfo3CNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysModuleCardInfo3CNumber.setStatus("mandatory")
_SwSysModuleCardInfoICTTestStatus_Type = Integer32
_SwSysModuleCardInfoICTTestStatus_Object = MibTableColumn
swSysModuleCardInfoICTTestStatus = _SwSysModuleCardInfoICTTestStatus_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 18, 2, 1, 10),
    _SwSysModuleCardInfoICTTestStatus_Type()
)
swSysModuleCardInfoICTTestStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysModuleCardInfoICTTestStatus.setStatus("mandatory")
_SwSysModuleCardInfoICTTestRevision_Type = DisplayString
_SwSysModuleCardInfoICTTestRevision_Object = MibTableColumn
swSysModuleCardInfoICTTestRevision = _SwSysModuleCardInfoICTTestRevision_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 18, 2, 1, 11),
    _SwSysModuleCardInfoICTTestRevision_Type()
)
swSysModuleCardInfoICTTestRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysModuleCardInfoICTTestRevision.setStatus("mandatory")
_SwSysModuleCardInfoSystemTestStatus_Type = Integer32
_SwSysModuleCardInfoSystemTestStatus_Object = MibTableColumn
swSysModuleCardInfoSystemTestStatus = _SwSysModuleCardInfoSystemTestStatus_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 18, 2, 1, 12),
    _SwSysModuleCardInfoSystemTestStatus_Type()
)
swSysModuleCardInfoSystemTestStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysModuleCardInfoSystemTestStatus.setStatus("mandatory")
_SwSysModuleCardInfoFunctionalTestStatus_Type = Integer32
_SwSysModuleCardInfoFunctionalTestStatus_Object = MibTableColumn
swSysModuleCardInfoFunctionalTestStatus = _SwSysModuleCardInfoFunctionalTestStatus_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 18, 2, 1, 13),
    _SwSysModuleCardInfoFunctionalTestStatus_Type()
)
swSysModuleCardInfoFunctionalTestStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysModuleCardInfoFunctionalTestStatus.setStatus("mandatory")
_SwSysModuleCardInfoFunctionalTestRevision_Type = DisplayString
_SwSysModuleCardInfoFunctionalTestRevision_Object = MibTableColumn
swSysModuleCardInfoFunctionalTestRevision = _SwSysModuleCardInfoFunctionalTestRevision_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 18, 2, 1, 14),
    _SwSysModuleCardInfoFunctionalTestRevision_Type()
)
swSysModuleCardInfoFunctionalTestRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysModuleCardInfoFunctionalTestRevision.setStatus("mandatory")
_SwSysModuleCardInfoBoardRevision_Type = DisplayString
_SwSysModuleCardInfoBoardRevision_Object = MibTableColumn
swSysModuleCardInfoBoardRevision = _SwSysModuleCardInfoBoardRevision_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 18, 2, 1, 15),
    _SwSysModuleCardInfoBoardRevision_Type()
)
swSysModuleCardInfoBoardRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysModuleCardInfoBoardRevision.setStatus("mandatory")
_SwSysModuleCardInfoRuntimeHours_Type = Integer32
_SwSysModuleCardInfoRuntimeHours_Object = MibTableColumn
swSysModuleCardInfoRuntimeHours = _SwSysModuleCardInfoRuntimeHours_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 18, 2, 1, 16),
    _SwSysModuleCardInfoRuntimeHours_Type()
)
swSysModuleCardInfoRuntimeHours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysModuleCardInfoRuntimeHours.setStatus("mandatory")
_SwSysDiagnosticsGroup_ObjectIdentity = ObjectIdentity
swSysDiagnosticsGroup = _SwSysDiagnosticsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 19)
)
_SwSysDiagnosticsInfoTable_Object = MibTable
swSysDiagnosticsInfoTable = _SwSysDiagnosticsInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 19, 1)
)
if mibBuilder.loadTexts:
    swSysDiagnosticsInfoTable.setStatus("mandatory")
_SwSysDiagnosticsInfoEntry_Object = MibTableRow
swSysDiagnosticsInfoEntry = _SwSysDiagnosticsInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 19, 1, 1)
)
swSysDiagnosticsInfoEntry.setIndexNames(
    (0, "SWITCHING-SYSTEMS-MIB", "swSysDiagnosticsInfoIndex"),
)
if mibBuilder.loadTexts:
    swSysDiagnosticsInfoEntry.setStatus("mandatory")
_SwSysDiagnosticsInfoIndex_Type = Integer32
_SwSysDiagnosticsInfoIndex_Object = MibTableColumn
swSysDiagnosticsInfoIndex = _SwSysDiagnosticsInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 19, 1, 1, 1),
    _SwSysDiagnosticsInfoIndex_Type()
)
swSysDiagnosticsInfoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysDiagnosticsInfoIndex.setStatus("mandatory")
_SwSysDiagnosticsInfoPOVDiagnosticsRevision_Type = DisplayString
_SwSysDiagnosticsInfoPOVDiagnosticsRevision_Object = MibTableColumn
swSysDiagnosticsInfoPOVDiagnosticsRevision = _SwSysDiagnosticsInfoPOVDiagnosticsRevision_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 19, 1, 1, 2),
    _SwSysDiagnosticsInfoPOVDiagnosticsRevision_Type()
)
swSysDiagnosticsInfoPOVDiagnosticsRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysDiagnosticsInfoPOVDiagnosticsRevision.setStatus("mandatory")
_SwSysDiagnosticsInfoExtendedDiagnosticsRevision_Type = DisplayString
_SwSysDiagnosticsInfoExtendedDiagnosticsRevision_Object = MibTableColumn
swSysDiagnosticsInfoExtendedDiagnosticsRevision = _SwSysDiagnosticsInfoExtendedDiagnosticsRevision_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 19, 1, 1, 3),
    _SwSysDiagnosticsInfoExtendedDiagnosticsRevision_Type()
)
swSysDiagnosticsInfoExtendedDiagnosticsRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysDiagnosticsInfoExtendedDiagnosticsRevision.setStatus("mandatory")
_SwSysDiagnosticsInfoDiagnosticFailureCode_Type = DisplayString
_SwSysDiagnosticsInfoDiagnosticFailureCode_Object = MibTableColumn
swSysDiagnosticsInfoDiagnosticFailureCode = _SwSysDiagnosticsInfoDiagnosticFailureCode_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 19, 1, 1, 4),
    _SwSysDiagnosticsInfoDiagnosticFailureCode_Type()
)
swSysDiagnosticsInfoDiagnosticFailureCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysDiagnosticsInfoDiagnosticFailureCode.setStatus("mandatory")
_SwSysDiagnosticsInfoDiagnosticFailureDateTime_Type = DisplayString
_SwSysDiagnosticsInfoDiagnosticFailureDateTime_Object = MibTableColumn
swSysDiagnosticsInfoDiagnosticFailureDateTime = _SwSysDiagnosticsInfoDiagnosticFailureDateTime_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 19, 1, 1, 5),
    _SwSysDiagnosticsInfoDiagnosticFailureDateTime_Type()
)
swSysDiagnosticsInfoDiagnosticFailureDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysDiagnosticsInfoDiagnosticFailureDateTime.setStatus("mandatory")
_SwSysDiagnosticsInfoDiagnosticFailureSlotNumber_Type = Integer32
_SwSysDiagnosticsInfoDiagnosticFailureSlotNumber_Object = MibTableColumn
swSysDiagnosticsInfoDiagnosticFailureSlotNumber = _SwSysDiagnosticsInfoDiagnosticFailureSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 19, 1, 1, 6),
    _SwSysDiagnosticsInfoDiagnosticFailureSlotNumber_Type()
)
swSysDiagnosticsInfoDiagnosticFailureSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysDiagnosticsInfoDiagnosticFailureSlotNumber.setStatus("mandatory")
_SwSysDiagnosticsInfoDiagnosticFailureCounter_Type = Integer32
_SwSysDiagnosticsInfoDiagnosticFailureCounter_Object = MibTableColumn
swSysDiagnosticsInfoDiagnosticFailureCounter = _SwSysDiagnosticsInfoDiagnosticFailureCounter_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 19, 1, 1, 7),
    _SwSysDiagnosticsInfoDiagnosticFailureCounter_Type()
)
swSysDiagnosticsInfoDiagnosticFailureCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysDiagnosticsInfoDiagnosticFailureCounter.setStatus("mandatory")
_SwSysDiagnosticsInfoDiagnosticFieldDOACounter_Type = Integer32
_SwSysDiagnosticsInfoDiagnosticFieldDOACounter_Object = MibTableColumn
swSysDiagnosticsInfoDiagnosticFieldDOACounter = _SwSysDiagnosticsInfoDiagnosticFieldDOACounter_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 19, 1, 1, 8),
    _SwSysDiagnosticsInfoDiagnosticFieldDOACounter_Type()
)
swSysDiagnosticsInfoDiagnosticFieldDOACounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysDiagnosticsInfoDiagnosticFieldDOACounter.setStatus("mandatory")
_CorebuilderSystemsMib_ObjectIdentity = ObjectIdentity
corebuilderSystemsMib = _CorebuilderSystemsMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 5)
)
_SuperstackSystemsMib_ObjectIdentity = ObjectIdentity
superstackSystemsMib = _SuperstackSystemsMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 6)
)
_SwitchingSystemsFddiMib_ObjectIdentity = ObjectIdentity
switchingSystemsFddiMib = _SwitchingSystemsFddiMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 10)
)
_SwitchingSystemsProducts_ObjectIdentity = ObjectIdentity
switchingSystemsProducts = _SwitchingSystemsProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 2)
)
_CorebuilderProductsII_ObjectIdentity = ObjectIdentity
corebuilderProductsII = _CorebuilderProductsII_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 2, 1)
)
_SuperstackProducts_ObjectIdentity = ObjectIdentity
superstackProducts = _SuperstackProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 2, 2)
)

# Managed Objects groups


# Notification objects

swSysSystemOverTemperatureEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 0, 1)
)
swSysSystemOverTemperatureEvent.setObjects(
    ("SWITCHING-SYSTEMS-MIB", "swSysSystemOvertemperature")
)
if mibBuilder.loadTexts:
    swSysSystemOverTemperatureEvent.setStatus(
        ""
    )

swSysPowerSupplyFailureEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 0, 2)
)
swSysPowerSupplyFailureEvent.setObjects(
      *(("SWITCHING-SYSTEMS-MIB", "swSysPowerSupplyStatusIndex"),
        ("SWITCHING-SYSTEMS-MIB", "swSysPowerSupplyStatus"),
        ("SWITCHING-SYSTEMS-MIB", "swSysPowerSupplyStatusSupported"))
)
if mibBuilder.loadTexts:
    swSysPowerSupplyFailureEvent.setStatus(
        ""
    )

swSysChassisSlotOverTemperatureEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 0, 3)
)
swSysChassisSlotOverTemperatureEvent.setObjects(
      *(("SWITCHING-SYSTEMS-MIB", "swSysSlotIndex"),
        ("SWITCHING-SYSTEMS-MIB", "swSysSlotBoardType"),
        ("SWITCHING-SYSTEMS-MIB", "swSysSlotBoardRevision"),
        ("SWITCHING-SYSTEMS-MIB", "swSysSlotBoardStatus"),
        ("SWITCHING-SYSTEMS-MIB", "swSysSlotOvertemperature"),
        ("SWITCHING-SYSTEMS-MIB", "swSysSlotConverterBad"))
)
if mibBuilder.loadTexts:
    swSysChassisSlotOverTemperatureEvent.setStatus(
        ""
    )

swSysChassisSlotInsertEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 0, 4)
)
swSysChassisSlotInsertEvent.setObjects(
      *(("SWITCHING-SYSTEMS-MIB", "swSysSlotIndex"),
        ("SWITCHING-SYSTEMS-MIB", "swSysSlotBoardType"),
        ("SWITCHING-SYSTEMS-MIB", "swSysSlotBoardRevision"))
)
if mibBuilder.loadTexts:
    swSysChassisSlotInsertEvent.setStatus(
        ""
    )

swSysChassisSlotExtractEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 0, 5)
)
swSysChassisSlotExtractEvent.setObjects(
    ("SWITCHING-SYSTEMS-MIB", "swSysSlotIndex")
)
if mibBuilder.loadTexts:
    swSysChassisSlotExtractEvent.setStatus(
        ""
    )

swSysBridgeAddressThresholdEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 0, 6)
)
swSysBridgeAddressThresholdEvent.setObjects(
    ("SWITCHING-SYSTEMS-MIB", "swSysBridgeIndex")
)
if mibBuilder.loadTexts:
    swSysBridgeAddressThresholdEvent.setStatus(
        ""
    )

swSysSystemFanFailureEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 0, 7)
)
swSysSystemFanFailureEvent.setObjects(
    ("SWITCHING-SYSTEMS-MIB", "swSysSystemFanFailure")
)
if mibBuilder.loadTexts:
    swSysSystemFanFailureEvent.setStatus(
        ""
    )

swModuleCardSysOverTemperatureEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 0, 8)
)
swModuleCardSysOverTemperatureEvent.setObjects(
      *(("SWITCHING-SYSTEMS-MIB", "swSysModuleCardInfoIndex"),
        ("SWITCHING-SYSTEMS-MIB", "swSysModuleCardInfoFamily"),
        ("SWITCHING-SYSTEMS-MIB", "swSysModuleCardInfoGenericType"))
)
if mibBuilder.loadTexts:
    swModuleCardSysOverTemperatureEvent.setStatus(
        ""
    )

swModuleCardInsertEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 0, 9)
)
swModuleCardInsertEvent.setObjects(
      *(("SWITCHING-SYSTEMS-MIB", "swSysModuleCardInfoIndex"),
        ("SWITCHING-SYSTEMS-MIB", "swSysModuleCardInfoFamily"),
        ("SWITCHING-SYSTEMS-MIB", "swSysModuleCardInfoGenericType"),
        ("SWITCHING-SYSTEMS-MIB", "swSysModuleCardInfoSpecificType"))
)
if mibBuilder.loadTexts:
    swModuleCardInsertEvent.setStatus(
        ""
    )

swModuleCardExtractEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 0, 10)
)
swModuleCardExtractEvent.setObjects(
    ("SWITCHING-SYSTEMS-MIB", "swSysModuleCardInfoIndex")
)
if mibBuilder.loadTexts:
    swModuleCardExtractEvent.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SWITCHING-SYSTEMS-MIB",
    **{"SwSysStorageType": SwSysStorageType,
       "SwSysAddressType": SwSysAddressType,
       "SwSysResourceType": SwSysResourceType,
       "SwSysResourceBitMask": SwSysResourceBitMask,
       "IpxNetworkNumber": IpxNetworkNumber,
       "ATNetworkNumber": ATNetworkNumber,
       "ATName": ATName,
       "DdpNodeAddress": DdpNodeAddress,
       "MacAddress": MacAddress,
       "synernetics": synernetics,
       "switchingSystems": switchingSystems,
       "corebuilderProductsI": corebuilderProductsI,
       "switchingSystemsMib": switchingSystemsMib,
       "swSysSystemOverTemperatureEvent": swSysSystemOverTemperatureEvent,
       "swSysPowerSupplyFailureEvent": swSysPowerSupplyFailureEvent,
       "swSysChassisSlotOverTemperatureEvent": swSysChassisSlotOverTemperatureEvent,
       "swSysChassisSlotInsertEvent": swSysChassisSlotInsertEvent,
       "swSysChassisSlotExtractEvent": swSysChassisSlotExtractEvent,
       "swSysBridgeAddressThresholdEvent": swSysBridgeAddressThresholdEvent,
       "swSysSystemFanFailureEvent": swSysSystemFanFailureEvent,
       "swModuleCardSysOverTemperatureEvent": swModuleCardSysOverTemperatureEvent,
       "swModuleCardInsertEvent": swModuleCardInsertEvent,
       "swModuleCardExtractEvent": swModuleCardExtractEvent,
       "swSysSystem": swSysSystem,
       "swSysSystemId": swSysSystemId,
       "swSysSystemType": swSysSystemType,
       "swSysSystemName": swSysSystemName,
       "swSysSystemManufacturer": swSysSystemManufacturer,
       "swSysSystemHardwareRevision": swSysSystemHardwareRevision,
       "swSysSystemMemorySize": swSysSystemMemorySize,
       "swSysSystemFlashMemorySize": swSysSystemFlashMemorySize,
       "swSysSystemNvMemorySize": swSysSystemNvMemorySize,
       "swSysSystemSoftwareRevision": swSysSystemSoftwareRevision,
       "swSysSystemBuildTime": swSysSystemBuildTime,
       "swSysSystemSnmpRevision": swSysSystemSnmpRevision,
       "swSysSystemRequestedSnmpMode": swSysSystemRequestedSnmpMode,
       "swSysSystemCurrentSnmpMode": swSysSystemCurrentSnmpMode,
       "swSysSystemAction": swSysSystemAction,
       "swSysSystemOvertemperature": swSysSystemOvertemperature,
       "swSysSystemFanFailure": swSysSystemFanFailure,
       "swSysSystemProtocolMask": swSysSystemProtocolMask,
       "swSysSystemConsoleAccess": swSysSystemConsoleAccess,
       "swSysSystemConsoleReadPwd": swSysSystemConsoleReadPwd,
       "swSysSystemConsoleWritePwd": swSysSystemConsoleWritePwd,
       "swSysSystemConsoleAdminPwd": swSysSystemConsoleAdminPwd,
       "swSysSystemDateTime": swSysSystemDateTime,
       "swSysSystemDSTime": swSysSystemDSTime,
       "swSysSystemTimeZone": swSysSystemTimeZone,
       "swSysSystemCurrentFddiStationMode": swSysSystemCurrentFddiStationMode,
       "swSysSystemRequestedFddiStationMode": swSysSystemRequestedFddiStationMode,
       "swSysSystemLog": swSysSystemLog,
       "swSysSystemLogEntryCurrentCount": swSysSystemLogEntryCurrentCount,
       "swSysSystemLogMaxSize": swSysSystemLogMaxSize,
       "swSysSystemLogSeverityThreshold": swSysSystemLogSeverityThreshold,
       "swSysSystemLogTable": swSysSystemLogTable,
       "swSysSystemLogEntry": swSysSystemLogEntry,
       "swSysSystemLogIndex": swSysSystemLogIndex,
       "swSysSystemLogSeverityLevel": swSysSystemLogSeverityLevel,
       "swSysSystemLogDateTime": swSysSystemLogDateTime,
       "swSysSystemLogFacility": swSysSystemLogFacility,
       "swSysSystemLogMessage": swSysSystemLogMessage,
       "swSysSystemBaseMACAddress": swSysSystemBaseMACAddress,
       "swSysSystemMACAddressCount": swSysSystemMACAddressCount,
       "swSysSystemChassisSerialNumber": swSysSystemChassisSerialNumber,
       "swSysSystemFPMemorySize": swSysSystemFPMemorySize,
       "swSysSystemBufferSize": swSysSystemBufferSize,
       "swSysSlot": swSysSlot,
       "swSysSlotCount": swSysSlotCount,
       "swSysSlotTable": swSysSlotTable,
       "swSysSlotEntry": swSysSlotEntry,
       "swSysSlotIndex": swSysSlotIndex,
       "swSysSlotBoardType": swSysSlotBoardType,
       "swSysSlotBoardRevision": swSysSlotBoardRevision,
       "swSysSlotBoardStatus": swSysSlotBoardStatus,
       "swSysSlotBoardName": swSysSlotBoardName,
       "swSysSlotBoardNameAbbrev": swSysSlotBoardNameAbbrev,
       "swSysSlotEthernetPortCount": swSysSlotEthernetPortCount,
       "swSysSlotFddiMacCount": swSysSlotFddiMacCount,
       "swSysSlotFddiPortCount": swSysSlotFddiPortCount,
       "swSysSlotOvertemperature": swSysSlotOvertemperature,
       "swSysSlotTokenRingPortCount": swSysSlotTokenRingPortCount,
       "swSysSlotBoardRevStr": swSysSlotBoardRevStr,
       "swSysSlotConverterBad": swSysSlotConverterBad,
       "swSysControlPanel": swSysControlPanel,
       "swSysControlPanelHardwareRevision": swSysControlPanelHardwareRevision,
       "swSysControlPanelSoftwareRevision": swSysControlPanelSoftwareRevision,
       "swSysControlPanelLines": swSysControlPanelLines,
       "swSysControlPanelColumns": swSysControlPanelColumns,
       "swSysControlPanelText": swSysControlPanelText,
       "swSysControlPanelAccess": swSysControlPanelAccess,
       "swSysPowerSupply": swSysPowerSupply,
       "swSysPowerSupplyCount": swSysPowerSupplyCount,
       "swSysPowerSupplyStatusTable": swSysPowerSupplyStatusTable,
       "swSysPowerSupplyStatusEntry": swSysPowerSupplyStatusEntry,
       "swSysPowerSupplyStatusIndex": swSysPowerSupplyStatusIndex,
       "swSysPowerSupplyStatus": swSysPowerSupplyStatus,
       "swSysPowerSupplyStatusSupported": swSysPowerSupplyStatusSupported,
       "swSysSnmp": swSysSnmp,
       "swSysSnmpAgentId": swSysSnmpAgentId,
       "swSysSnmpInternalAgentTrapMask": swSysSnmpInternalAgentTrapMask,
       "swSysSnmpInternalAgentTrapDestinationMask": swSysSnmpInternalAgentTrapDestinationMask,
       "swSysSnmpProxyInternalRequests": swSysSnmpProxyInternalRequests,
       "swSysSnmpInternalProxyRequestMaxAge": swSysSnmpInternalProxyRequestMaxAge,
       "swSysSnmpProxyInternalTraps": swSysSnmpProxyInternalTraps,
       "swSysSnmpInternalProxyTable": swSysSnmpInternalProxyTable,
       "swSysSnmpInternalProxyEntry": swSysSnmpInternalProxyEntry,
       "swSysSnmpInternalProxyAgentId": swSysSnmpInternalProxyAgentId,
       "swSysSnmpInternalProxyAccessClass": swSysSnmpInternalProxyAccessClass,
       "swSysSnmpInternalProxyCommunity": swSysSnmpInternalProxyCommunity,
       "swSysAgent": swSysAgent,
       "swSysAgentRequestMaxAge": swSysAgentRequestMaxAge,
       "swSysAgentProxyRemoteSmtRequests": swSysAgentProxyRemoteSmtRequests,
       "swSysAgentRemoteSmtProxyRequestMaxAge": swSysAgentRemoteSmtProxyRequestMaxAge,
       "swSysAgentProxyRemoteSmtEvents": swSysAgentProxyRemoteSmtEvents,
       "swSysAgentTrapDescriptionTable": swSysAgentTrapDescriptionTable,
       "swSysAgentTrapDescriptionTableEntry": swSysAgentTrapDescriptionTableEntry,
       "swSysAgentTrapDescriptionIndex": swSysAgentTrapDescriptionIndex,
       "swSysAgentTrapEnterprise": swSysAgentTrapEnterprise,
       "swSysAgentTrapNumber": swSysAgentTrapNumber,
       "swSysAgentTrapDestinationTable": swSysAgentTrapDestinationTable,
       "swSysAgentTrapDestinationTableEntry": swSysAgentTrapDestinationTableEntry,
       "swSysAgentTrapDestinationAddressType": swSysAgentTrapDestinationAddressType,
       "swSysAgentTrapDestinationAddress": swSysAgentTrapDestinationAddress,
       "swSysAgentTrapDestinationTrapMask": swSysAgentTrapDestinationTrapMask,
       "swSysAgentTrapDestinationEntryStatus": swSysAgentTrapDestinationEntryStatus,
       "swSysAgentReadCommunity": swSysAgentReadCommunity,
       "swSysAgentReadWriteCommunity": swSysAgentReadWriteCommunity,
       "swSysInterface": swSysInterface,
       "swSysInterfaceLocationTable": swSysInterfaceLocationTable,
       "swSysInterfaceLocationEntry": swSysInterfaceLocationEntry,
       "swSysInterfaceLocationIfIndex": swSysInterfaceLocationIfIndex,
       "swSysInterfaceLocationInterfaceType": swSysInterfaceLocationInterfaceType,
       "swSysInterfaceLocationType": swSysInterfaceLocationType,
       "swSysInterfaceLocationTypeIndex": swSysInterfaceLocationTypeIndex,
       "swSysInterfaceLocationLocalIndex": swSysInterfaceLocationLocalIndex,
       "swSysInterfaceLocationSystemModuleIndex": swSysInterfaceLocationSystemModuleIndex,
       "swSysEthernetPort": swSysEthernetPort,
       "swSysEthernetPortCount": swSysEthernetPortCount,
       "swSysEthernetPortTable": swSysEthernetPortTable,
       "swSysEthernetPortEntry": swSysEthernetPortEntry,
       "swSysEthernetPortIndex": swSysEthernetPortIndex,
       "swSysEthernetPortIfIndex": swSysEthernetPortIfIndex,
       "swSysEthernetPortLabel": swSysEthernetPortLabel,
       "swSysEthernetPortLinkStatus": swSysEthernetPortLinkStatus,
       "swSysEthernetPortType": swSysEthernetPortType,
       "swSysEthernetPortRateTable": swSysEthernetPortRateTable,
       "swSysEthernetPortRateEntry": swSysEthernetPortRateEntry,
       "swSysEthernetPortRateIndex": swSysEthernetPortRateIndex,
       "swSysEthernetPortRateByteReceiveRate": swSysEthernetPortRateByteReceiveRate,
       "swSysEthernetPortRatePeakByteReceiveRate": swSysEthernetPortRatePeakByteReceiveRate,
       "swSysEthernetPortRateFrameReceiveRate": swSysEthernetPortRateFrameReceiveRate,
       "swSysEthernetPortRatePeakFrameReceiveRate": swSysEthernetPortRatePeakFrameReceiveRate,
       "swSysEthernetPortRateByteTransmitRate": swSysEthernetPortRateByteTransmitRate,
       "swSysEthernetPortRatePeakByteTransmitRate": swSysEthernetPortRatePeakByteTransmitRate,
       "swSysEthernetPortRateFrameTransmitRate": swSysEthernetPortRateFrameTransmitRate,
       "swSysEthernetPortRatePeakFrameTransmitRate": swSysEthernetPortRatePeakFrameTransmitRate,
       "swSysSmt": swSysSmt,
       "swSysSmtCount": swSysSmtCount,
       "swSysSmtFddiMacBeaconTable": swSysSmtFddiMacBeaconTable,
       "swSysSmtFddiMacBeaconEntry": swSysSmtFddiMacBeaconEntry,
       "swSysSmtFddiMacBeaconSmtIndex": swSysSmtFddiMacBeaconSmtIndex,
       "swSysSmtFddiMacBeaconIndex": swSysSmtFddiMacBeaconIndex,
       "swSysSmtFddiMacBeaconHistory": swSysSmtFddiMacBeaconHistory,
       "swSysSmtFddiMacRateTable": swSysSmtFddiMacRateTable,
       "swSysSmtFddiMacRateEntry": swSysSmtFddiMacRateEntry,
       "swSysSmtFddiMacRateSmtIndex": swSysSmtFddiMacRateSmtIndex,
       "swSysSmtFddiMacRateIndex": swSysSmtFddiMacRateIndex,
       "swSysSmtFddiMacRateByteReceiveRate": swSysSmtFddiMacRateByteReceiveRate,
       "swSysSmtFddiMacRatePeakByteReceiveRate": swSysSmtFddiMacRatePeakByteReceiveRate,
       "swSysSmtFddiMacRateFrameReceiveRate": swSysSmtFddiMacRateFrameReceiveRate,
       "swSysSmtFddiMacRatePeakFrameReceiveRate": swSysSmtFddiMacRatePeakFrameReceiveRate,
       "swSysSmtFddiMacRateByteTransmitRate": swSysSmtFddiMacRateByteTransmitRate,
       "swSysSmtFddiMacRatePeakByteTransmitRate": swSysSmtFddiMacRatePeakByteTransmitRate,
       "swSysSmtFddiMacRateFrameTransmitRate": swSysSmtFddiMacRateFrameTransmitRate,
       "swSysSmtFddiMacRatePeakFrameTransmitRate": swSysSmtFddiMacRatePeakFrameTransmitRate,
       "swSysSmtFddiPortTable": swSysSmtFddiPortTable,
       "swSysSmtFddiPortEntry": swSysSmtFddiPortEntry,
       "swSysSmtFddiPortSmtIndex": swSysSmtFddiPortSmtIndex,
       "swSysSmtFddiPortIndex": swSysSmtFddiPortIndex,
       "swSysSmtFddiPortLocationType": swSysSmtFddiPortLocationType,
       "swSysSmtFddiPortLocationTypeIndex": swSysSmtFddiPortLocationTypeIndex,
       "swSysSmtFddiPortLocationLocalIndex": swSysSmtFddiPortLocationLocalIndex,
       "swSysSmtFddiPortLabel": swSysSmtFddiPortLabel,
       "swSysSmtFddiMacLocationTable": swSysSmtFddiMacLocationTable,
       "swSysSmtFddiMacLocationEntry": swSysSmtFddiMacLocationEntry,
       "swSysSmtFddiMacLocationSmtIndex": swSysSmtFddiMacLocationSmtIndex,
       "swSysSmtFddiMacLocationIndex": swSysSmtFddiMacLocationIndex,
       "swSysSmtFddiMacCurrentLocation": swSysSmtFddiMacCurrentLocation,
       "swSysSmtFddiMacRequestedLocation": swSysSmtFddiMacRequestedLocation,
       "swSysSmtFddiMacAvailableLocation": swSysSmtFddiMacAvailableLocation,
       "swSysSmtFddiMacStationTable": swSysSmtFddiMacStationTable,
       "swSysSmtFddiMacStationEntry": swSysSmtFddiMacStationEntry,
       "swSysSmtFddiMacStationSmtIndex": swSysSmtFddiMacStationSmtIndex,
       "swSysSmtFddiMacStationIndex": swSysSmtFddiMacStationIndex,
       "swSysSmtFddiMacCurrentStation": swSysSmtFddiMacCurrentStation,
       "swSysSmtFddiMacRequestedStation": swSysSmtFddiMacRequestedStation,
       "swSysSmtFddiMacAvailableStations": swSysSmtFddiMacAvailableStations,
       "swSysSmtFddiPortStationTable": swSysSmtFddiPortStationTable,
       "swSysSmtFddiPortStationEntry": swSysSmtFddiPortStationEntry,
       "swSysSmtFddiPortStationSmtIndex": swSysSmtFddiPortStationSmtIndex,
       "swSysSmtFddiPortStationIndex": swSysSmtFddiPortStationIndex,
       "swSysSmtFddiPortCurrentStation": swSysSmtFddiPortCurrentStation,
       "swSysSmtFddiPortRequestedStation": swSysSmtFddiPortRequestedStation,
       "swSysSmtFddiPortAvailableStations": swSysSmtFddiPortAvailableStations,
       "swSysBridge": swSysBridge,
       "swSysBridgeCount": swSysBridgeCount,
       "swSysBridgeTable": swSysBridgeTable,
       "swSysBridgeEntry": swSysBridgeEntry,
       "swSysBridgeIndex": swSysBridgeIndex,
       "swSysBridgePortCount": swSysBridgePortCount,
       "swSysBridgeAddressTableSize": swSysBridgeAddressTableSize,
       "swSysBridgeAddressTableCount": swSysBridgeAddressTableCount,
       "swSysBridgeAddressTablePeakCount": swSysBridgeAddressTablePeakCount,
       "swSysBridgeAddressThreshold": swSysBridgeAddressThreshold,
       "swSysBridgeMode": swSysBridgeMode,
       "swSysBridgeBackbonePort": swSysBridgeBackbonePort,
       "swSysBridgeIpFragmentationEnabled": swSysBridgeIpFragmentationEnabled,
       "swSysBridgeTrFddiTranslationMode": swSysBridgeTrFddiTranslationMode,
       "swSysBridgeSTPGroupAddress": swSysBridgeSTPGroupAddress,
       "swSysBridgeSTPEnable": swSysBridgeSTPEnable,
       "swSysBridgeIpxSnapTranslationEnable": swSysBridgeIpxSnapTranslationEnable,
       "swSysBridgeLowLatencyEnable": swSysBridgeLowLatencyEnable,
       "swSysBridgeVlanMode": swSysBridgeVlanMode,
       "swSysBridgePortTable": swSysBridgePortTable,
       "swSysBridgePortEntry": swSysBridgePortEntry,
       "swSysBridgePortBridgeIndex": swSysBridgePortBridgeIndex,
       "swSysBridgePortIndex": swSysBridgePortIndex,
       "swSysBridgePortIfIndex": swSysBridgePortIfIndex,
       "swSysBridgePortReceiveMulticastLimit": swSysBridgePortReceiveMulticastLimit,
       "swSysBridgePortAddressAction": swSysBridgePortAddressAction,
       "swSysBridgePortSpanningTreeFrameReceivedCounts": swSysBridgePortSpanningTreeFrameReceivedCounts,
       "swSysBridgePortReceiveBlockedDiscards": swSysBridgePortReceiveBlockedDiscards,
       "swSysBridgePortReceiveMulticastLimitExceededs": swSysBridgePortReceiveMulticastLimitExceededs,
       "swSysBridgePortReceiveMulticastLimitExceededDiscards": swSysBridgePortReceiveMulticastLimitExceededDiscards,
       "swSysBridgePortReceiveSecurityDiscards": swSysBridgePortReceiveSecurityDiscards,
       "swSysBridgePortReceiveUnknownDiscards": swSysBridgePortReceiveUnknownDiscards,
       "swSysBridgePortReceiveOtherDiscards": swSysBridgePortReceiveOtherDiscards,
       "swSysBridgePortReceiveErrorDiscards": swSysBridgePortReceiveErrorDiscards,
       "swSysBridgePortSameSegmentDiscards": swSysBridgePortSameSegmentDiscards,
       "swSysBridgePortTransmitBlockedDiscards": swSysBridgePortTransmitBlockedDiscards,
       "swSysBridgePortReceiveAllPathFilteredFrames": swSysBridgePortReceiveAllPathFilteredFrames,
       "swSysBridgePortReceiveMulticastPathFilteredFrames": swSysBridgePortReceiveMulticastPathFilteredFrames,
       "swSysBridgePortTransmitAllPathFilteredFrames": swSysBridgePortTransmitAllPathFilteredFrames,
       "swSysBridgePortTransmitMulticastPathFilteredFrames": swSysBridgePortTransmitMulticastPathFilteredFrames,
       "swSysBridgePortForwardedUnicastFrames": swSysBridgePortForwardedUnicastFrames,
       "swSysBridgePortForwardedUnicastOctets": swSysBridgePortForwardedUnicastOctets,
       "swSysBridgePortForwardedMulticastFrames": swSysBridgePortForwardedMulticastFrames,
       "swSysBridgePortForwardedMulticastOctets": swSysBridgePortForwardedMulticastOctets,
       "swSysBridgePortFloodedUnicastFrames": swSysBridgePortFloodedUnicastFrames,
       "swSysBridgePortFloodedUnicastOctets": swSysBridgePortFloodedUnicastOctets,
       "swSysBridgePortStpMode": swSysBridgePortStpMode,
       "swSysBridgePortReceiveMulticastLimitFrameType": swSysBridgePortReceiveMulticastLimitFrameType,
       "swSysBridgePortAddressTable": swSysBridgePortAddressTable,
       "swSysBridgePortAddressEntry": swSysBridgePortAddressEntry,
       "swSysBridgePortAddressBridgeIndex": swSysBridgePortAddressBridgeIndex,
       "swSysBridgePortAddressPortIndex": swSysBridgePortAddressPortIndex,
       "swSysBridgePortAddressIndex": swSysBridgePortAddressIndex,
       "swSysBridgePortAddressRemoteAddress": swSysBridgePortAddressRemoteAddress,
       "swSysBridgePortAddressType": swSysBridgePortAddressType,
       "swSysBridgePortAddressIsStatic": swSysBridgePortAddressIsStatic,
       "swSysBridgePortAddressStaticPort": swSysBridgePortAddressStaticPort,
       "swSysBridgePortAddressAge": swSysBridgePortAddressAge,
       "swSysBridgeStpGroupAddress": swSysBridgeStpGroupAddress,
       "swSysBridgeStpEnable": swSysBridgeStpEnable,
       "swSysIpRouter": swSysIpRouter,
       "swSysNetworkMonitor": swSysNetworkMonitor,
       "swSysNetworkAnalyzerTable": swSysNetworkAnalyzerTable,
       "swSysNetworkAnalyzerTableEntry": swSysNetworkAnalyzerTableEntry,
       "swSysNetworkAnalyzerBridgeIndex": swSysNetworkAnalyzerBridgeIndex,
       "swSysNetworkAnalyzerBridgePortIndex": swSysNetworkAnalyzerBridgePortIndex,
       "swSysNetworkAnalyzerPhysicalAddress": swSysNetworkAnalyzerPhysicalAddress,
       "swSysNetworkAnalyzerStatus": swSysNetworkAnalyzerStatus,
       "swSysNetworkPortMonitorTable": swSysNetworkPortMonitorTable,
       "swSysNetworkPortMonitorTableEntry": swSysNetworkPortMonitorTableEntry,
       "swSysNetworkPortMonitorBridgeIndex": swSysNetworkPortMonitorBridgeIndex,
       "swSysNetworkPortMonitorBridgePortIndex": swSysNetworkPortMonitorBridgePortIndex,
       "swSysNetworkPortMonitorAnalyzerAddress": swSysNetworkPortMonitorAnalyzerAddress,
       "swSysNetworkPortMonitorStatus": swSysNetworkPortMonitorStatus,
       "swSysTokenRingPort": swSysTokenRingPort,
       "swSysTokenRingPortCount": swSysTokenRingPortCount,
       "swSysTokenRingPortTable": swSysTokenRingPortTable,
       "swSysTokenRingPortEntry": swSysTokenRingPortEntry,
       "swSysTokenRingPortIndex": swSysTokenRingPortIndex,
       "swSysTokenRingPortIfIndex": swSysTokenRingPortIfIndex,
       "swSysTokenRingPortLabel": swSysTokenRingPortLabel,
       "swSysTokenRingPortInsertStatus": swSysTokenRingPortInsertStatus,
       "swSysTokenRingPortType": swSysTokenRingPortType,
       "swSysTokenRingPortMode": swSysTokenRingPortMode,
       "swSysTokenRingPortSpeed": swSysTokenRingPortSpeed,
       "swSysTokenRingPortLineErrors": swSysTokenRingPortLineErrors,
       "swSysTokenRingPortBurstErrors": swSysTokenRingPortBurstErrors,
       "swSysTokenRingPortACErrors": swSysTokenRingPortACErrors,
       "swSysTokenRingPortAbortTransErrors": swSysTokenRingPortAbortTransErrors,
       "swSysTokenRingPortInternalErrors": swSysTokenRingPortInternalErrors,
       "swSysTokenRingPortLostFrameErrors": swSysTokenRingPortLostFrameErrors,
       "swSysTokenRingPortReceiveCongestionErrors": swSysTokenRingPortReceiveCongestionErrors,
       "swSysTokenRingPortFrameCopiedErrors": swSysTokenRingPortFrameCopiedErrors,
       "swSysTokenRingPortTokenErrors": swSysTokenRingPortTokenErrors,
       "swSysTokenRingPortSoftErrors": swSysTokenRingPortSoftErrors,
       "swSysTokenRingPortHardErrors": swSysTokenRingPortHardErrors,
       "swSysTokenRingPortTransmitBeacons": swSysTokenRingPortTransmitBeacons,
       "swSysTokenRingPortLobeWires": swSysTokenRingPortLobeWires,
       "swSysTokenRingPortRemoves": swSysTokenRingPortRemoves,
       "swSysTokenRingPortSingles": swSysTokenRingPortSingles,
       "swSysTokenRingPortFreqErrors": swSysTokenRingPortFreqErrors,
       "swSysTokenRingPortRingStatus": swSysTokenRingPortRingStatus,
       "swSysFtGroup": swSysFtGroup,
       "swSysFtTable": swSysFtTable,
       "swSysFtTableEntry": swSysFtTableEntry,
       "swSysFtIndex": swSysFtIndex,
       "swSysFtDirection": swSysFtDirection,
       "swSysFtLocalStorageType": swSysFtLocalStorageType,
       "swSysFtLocalResourceType": swSysFtLocalResourceType,
       "swSysFtLocalResourceMask": swSysFtLocalResourceMask,
       "swSysFtLocalResourceAttribute": swSysFtLocalResourceAttribute,
       "swSysFtRemoteAddressType": swSysFtRemoteAddressType,
       "swSysFtRemoteAddress": swSysFtRemoteAddress,
       "swSysFtRemoteFileName": swSysFtRemoteFileName,
       "swSysFtRemoteUserName": swSysFtRemoteUserName,
       "swSysFtRemoteUserPassword": swSysFtRemoteUserPassword,
       "swSysFtForceTransfer": swSysFtForceTransfer,
       "swSysFtBytesTransferred": swSysFtBytesTransferred,
       "swSysFtStatus": swSysFtStatus,
       "swSysFtDetailedStatus": swSysFtDetailedStatus,
       "swSysFtDetailedStatusString": swSysFtDetailedStatusString,
       "swSysFtOwnerString": swSysFtOwnerString,
       "swSysFtRowStatus": swSysFtRowStatus,
       "swSysFtResourceAttributes": swSysFtResourceAttributes,
       "swSysFtSystemAttributes": swSysFtSystemAttributes,
       "swSysFtSystemOperationalCode": swSysFtSystemOperationalCode,
       "swSysFtSystemConfiguration": swSysFtSystemConfiguration,
       "swSysFtSystemBridgeFilterCode": swSysFtSystemBridgeFilterCode,
       "swSysFtDetailedResourceStatus": swSysFtDetailedResourceStatus,
       "swSysFtSystemDetailedStatus": swSysFtSystemDetailedStatus,
       "swSysFtSysStatusNotApplicable": swSysFtSysStatusNotApplicable,
       "swSysFtSysStatusNoImageLabel": swSysFtSysStatusNoImageLabel,
       "swSysFtSysStatusConfigIdMismatch": swSysFtSysStatusConfigIdMismatch,
       "swSysFtSysStatusChecksumError": swSysFtSysStatusChecksumError,
       "swSysFtSysStatusNvRamError": swSysFtSysStatusNvRamError,
       "swSysFtSysStatusFlashError": swSysFtSysStatusFlashError,
       "swSysFtSysStatusNoRoom": swSysFtSysStatusNoRoom,
       "swSysFtSysBridgeFilterNotApplicable": swSysFtSysBridgeFilterNotApplicable,
       "swSysFtSysBridgeFilterSyntaxError": swSysFtSysBridgeFilterSyntaxError,
       "swSysFtSysBridgeFilterdownloadError": swSysFtSysBridgeFilterdownloadError,
       "swSysFtSysBridgeFilterNoRoom": swSysFtSysBridgeFilterNoRoom,
       "swSysIpGroup": swSysIpGroup,
       "swSysIpBaseGroup": swSysIpBaseGroup,
       "swSysIpInterfaceGroup": swSysIpInterfaceGroup,
       "swSysIpInterfaceCount": swSysIpInterfaceCount,
       "swSysIpInterfaceTable": swSysIpInterfaceTable,
       "swSysIpInterfaceEntry": swSysIpInterfaceEntry,
       "swSysIpInterfaceIpStackIndex": swSysIpInterfaceIpStackIndex,
       "swSysIpInterfaceAddr": swSysIpInterfaceAddr,
       "swSysIpInterfaceNetMask": swSysIpInterfaceNetMask,
       "swSysIpInterfaceIndex": swSysIpInterfaceIndex,
       "swSysIpInterfaceBcastAddr": swSysIpInterfaceBcastAddr,
       "swSysIpInterfaceCost": swSysIpInterfaceCost,
       "swSysIpInterfaceStatus": swSysIpInterfaceStatus,
       "swSysIpxGroup": swSysIpxGroup,
       "swSysIpxBaseGroup": swSysIpxBaseGroup,
       "swSysIpxInterfaceGroup": swSysIpxInterfaceGroup,
       "swSysIpxInterfaceCount": swSysIpxInterfaceCount,
       "swSysIpxInterfaceTable": swSysIpxInterfaceTable,
       "swSysIpxInterfaceEntry": swSysIpxInterfaceEntry,
       "swSysIpxInterfaceIpxStackIndex": swSysIpxInterfaceIpxStackIndex,
       "swSysIpxInterfaceNetNumber": swSysIpxInterfaceNetNumber,
       "swSysIpxInterfaceIfIndex": swSysIpxInterfaceIfIndex,
       "swSysIpxInterfaceCost": swSysIpxInterfaceCost,
       "swSysIpxInterfaceFrameType": swSysIpxInterfaceFrameType,
       "swSysIpxInterfaceStatus": swSysIpxInterfaceStatus,
       "swSysAppleTalkGroup": swSysAppleTalkGroup,
       "swSysAppleTalkBaseGroup": swSysAppleTalkBaseGroup,
       "swSysAppleTalkInterfaceGroup": swSysAppleTalkInterfaceGroup,
       "swSysAtInterfaceCount": swSysAtInterfaceCount,
       "swSysAtInterfaceTable": swSysAtInterfaceTable,
       "swSysAtInterfaceEntry": swSysAtInterfaceEntry,
       "swSysAtInterfaceAtStackIndex": swSysAtInterfaceAtStackIndex,
       "swSysAtInterfaceNetAddress": swSysAtInterfaceNetAddress,
       "swSysAtInterfaceType": swSysAtInterfaceType,
       "swSysAtInterfaceNetStart": swSysAtInterfaceNetStart,
       "swSysAtInterfaceNetEnd": swSysAtInterfaceNetEnd,
       "swSysAtInterfaceZoneDefault": swSysAtInterfaceZoneDefault,
       "swSysAtInterfaceZone1": swSysAtInterfaceZone1,
       "swSysAtInterfaceZone2": swSysAtInterfaceZone2,
       "swSysAtInterfaceZone3": swSysAtInterfaceZone3,
       "swSysAtInterfaceZone4": swSysAtInterfaceZone4,
       "swSysAtInterfaceZone5": swSysAtInterfaceZone5,
       "swSysAtInterfaceZone6": swSysAtInterfaceZone6,
       "swSysAtInterfaceZone7": swSysAtInterfaceZone7,
       "swSysAtInterfaceZone8": swSysAtInterfaceZone8,
       "swSysAtInterfaceZone9": swSysAtInterfaceZone9,
       "swSysAtInterfaceZone10": swSysAtInterfaceZone10,
       "swSysAtInterfaceZone11": swSysAtInterfaceZone11,
       "swSysAtInterfaceZone12": swSysAtInterfaceZone12,
       "swSysAtInterfaceZone13": swSysAtInterfaceZone13,
       "swSysAtInterfaceZone14": swSysAtInterfaceZone14,
       "swSysAtInterfaceZone15": swSysAtInterfaceZone15,
       "swSysAtInterfaceIfIndex": swSysAtInterfaceIfIndex,
       "swSysAtInterfaceState": swSysAtInterfaceState,
       "swSysAtInterfaceStatus": swSysAtInterfaceStatus,
       "swSysModuleCardGroup": swSysModuleCardGroup,
       "swSysModuleCardCount": swSysModuleCardCount,
       "swSysModuleCardInfoTable": swSysModuleCardInfoTable,
       "swSysModuleCardInfoEntry": swSysModuleCardInfoEntry,
       "swSysModuleCardInfoIndex": swSysModuleCardInfoIndex,
       "swSysModuleCardInfoFamily": swSysModuleCardInfoFamily,
       "swSysModuleCardInfoGenericType": swSysModuleCardInfoGenericType,
       "swSysModuleCardInfoSpecificType": swSysModuleCardInfoSpecificType,
       "swSysModuleCardInfoPartNumber": swSysModuleCardInfoPartNumber,
       "swSysModuleCardInfoManufacturingDate": swSysModuleCardInfoManufacturingDate,
       "swSysModuleCardInfoModuleSerialNumber": swSysModuleCardInfoModuleSerialNumber,
       "swSysModuleCardInfoTLASerialNumber": swSysModuleCardInfoTLASerialNumber,
       "swSysModuleCardInfo3CNumber": swSysModuleCardInfo3CNumber,
       "swSysModuleCardInfoICTTestStatus": swSysModuleCardInfoICTTestStatus,
       "swSysModuleCardInfoICTTestRevision": swSysModuleCardInfoICTTestRevision,
       "swSysModuleCardInfoSystemTestStatus": swSysModuleCardInfoSystemTestStatus,
       "swSysModuleCardInfoFunctionalTestStatus": swSysModuleCardInfoFunctionalTestStatus,
       "swSysModuleCardInfoFunctionalTestRevision": swSysModuleCardInfoFunctionalTestRevision,
       "swSysModuleCardInfoBoardRevision": swSysModuleCardInfoBoardRevision,
       "swSysModuleCardInfoRuntimeHours": swSysModuleCardInfoRuntimeHours,
       "swSysDiagnosticsGroup": swSysDiagnosticsGroup,
       "swSysDiagnosticsInfoTable": swSysDiagnosticsInfoTable,
       "swSysDiagnosticsInfoEntry": swSysDiagnosticsInfoEntry,
       "swSysDiagnosticsInfoIndex": swSysDiagnosticsInfoIndex,
       "swSysDiagnosticsInfoPOVDiagnosticsRevision": swSysDiagnosticsInfoPOVDiagnosticsRevision,
       "swSysDiagnosticsInfoExtendedDiagnosticsRevision": swSysDiagnosticsInfoExtendedDiagnosticsRevision,
       "swSysDiagnosticsInfoDiagnosticFailureCode": swSysDiagnosticsInfoDiagnosticFailureCode,
       "swSysDiagnosticsInfoDiagnosticFailureDateTime": swSysDiagnosticsInfoDiagnosticFailureDateTime,
       "swSysDiagnosticsInfoDiagnosticFailureSlotNumber": swSysDiagnosticsInfoDiagnosticFailureSlotNumber,
       "swSysDiagnosticsInfoDiagnosticFailureCounter": swSysDiagnosticsInfoDiagnosticFailureCounter,
       "swSysDiagnosticsInfoDiagnosticFieldDOACounter": swSysDiagnosticsInfoDiagnosticFieldDOACounter,
       "corebuilderSystemsMib": corebuilderSystemsMib,
       "superstackSystemsMib": superstackSystemsMib,
       "switchingSystemsFddiMib": switchingSystemsFddiMib,
       "switchingSystemsProducts": switchingSystemsProducts,
       "corebuilderProductsII": corebuilderProductsII,
       "superstackProducts": superstackProducts}
)
