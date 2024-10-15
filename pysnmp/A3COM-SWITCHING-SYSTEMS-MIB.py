# SNMP MIB module (A3COM-SWITCHING-SYSTEMS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/A3COM-SWITCHING-SYSTEMS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:29:50 2024
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



class RowStatus(Integer32):
    """Custom type RowStatus based on Integer32"""
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
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )





class A3ComSysStorageType(Integer32):
    """Custom type A3ComSysStorageType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )





class A3ComSysAddressType(Integer32):
    """Custom type A3ComSysAddressType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )





class A3ComSysResourceType(Integer32):
    """Custom type A3ComSysResourceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )





class A3ComSysResourceBitMask(OctetString):
    """Custom type A3ComSysResourceBitMask based on OctetString"""
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

_A3Com_ObjectIdentity = ObjectIdentity
a3Com = _A3Com_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43)
)
_SwitchingSystems_mib_ObjectIdentity = ObjectIdentity
switchingSystems_mib = _SwitchingSystems_mib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 29)
)
_SwitchingSystemsMibGroups_ObjectIdentity = ObjectIdentity
switchingSystemsMibGroups = _SwitchingSystemsMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 29, 4)
)
_A3ComSysSystem_ObjectIdentity = ObjectIdentity
a3ComSysSystem = _A3ComSysSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 1)
)
_A3ComSysSystemId_Type = Integer32
_A3ComSysSystemId_Object = MibScalar
a3ComSysSystemId = _A3ComSysSystemId_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 1, 1),
    _A3ComSysSystemId_Type()
)
a3ComSysSystemId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysSystemId.setStatus("mandatory")


class _A3ComSysSystemType_Type(Integer32):
    """Custom type a3ComSysSystemType based on Integer32"""
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


_A3ComSysSystemType_Type.__name__ = "Integer32"
_A3ComSysSystemType_Object = MibScalar
a3ComSysSystemType = _A3ComSysSystemType_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 1, 2),
    _A3ComSysSystemType_Type()
)
a3ComSysSystemType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysSystemType.setStatus("mandatory")


class _A3ComSysSystemName_Type(DisplayString):
    """Custom type a3ComSysSystemName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_A3ComSysSystemName_Type.__name__ = "DisplayString"
_A3ComSysSystemName_Object = MibScalar
a3ComSysSystemName = _A3ComSysSystemName_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 1, 3),
    _A3ComSysSystemName_Type()
)
a3ComSysSystemName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComSysSystemName.setStatus("mandatory")


class _A3ComSysSystemManufacturer_Type(DisplayString):
    """Custom type a3ComSysSystemManufacturer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_A3ComSysSystemManufacturer_Type.__name__ = "DisplayString"
_A3ComSysSystemManufacturer_Object = MibScalar
a3ComSysSystemManufacturer = _A3ComSysSystemManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 1, 4),
    _A3ComSysSystemManufacturer_Type()
)
a3ComSysSystemManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysSystemManufacturer.setStatus("mandatory")


class _A3ComSysSystemHardwareRevision_Type(OctetString):
    """Custom type a3ComSysSystemHardwareRevision based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_A3ComSysSystemHardwareRevision_Type.__name__ = "OctetString"
_A3ComSysSystemHardwareRevision_Object = MibScalar
a3ComSysSystemHardwareRevision = _A3ComSysSystemHardwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 1, 5),
    _A3ComSysSystemHardwareRevision_Type()
)
a3ComSysSystemHardwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysSystemHardwareRevision.setStatus("mandatory")
_A3ComSysSystemMemorySize_Type = Integer32
_A3ComSysSystemMemorySize_Object = MibScalar
a3ComSysSystemMemorySize = _A3ComSysSystemMemorySize_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 1, 6),
    _A3ComSysSystemMemorySize_Type()
)
a3ComSysSystemMemorySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysSystemMemorySize.setStatus("mandatory")
_A3ComSysSystemFlashMemorySize_Type = Integer32
_A3ComSysSystemFlashMemorySize_Object = MibScalar
a3ComSysSystemFlashMemorySize = _A3ComSysSystemFlashMemorySize_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 1, 7),
    _A3ComSysSystemFlashMemorySize_Type()
)
a3ComSysSystemFlashMemorySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysSystemFlashMemorySize.setStatus("mandatory")
_A3ComSysSystemNvMemorySize_Type = Integer32
_A3ComSysSystemNvMemorySize_Object = MibScalar
a3ComSysSystemNvMemorySize = _A3ComSysSystemNvMemorySize_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 1, 8),
    _A3ComSysSystemNvMemorySize_Type()
)
a3ComSysSystemNvMemorySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysSystemNvMemorySize.setStatus("mandatory")


class _A3ComSysSystemSoftwareRevision_Type(OctetString):
    """Custom type a3ComSysSystemSoftwareRevision based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_A3ComSysSystemSoftwareRevision_Type.__name__ = "OctetString"
_A3ComSysSystemSoftwareRevision_Object = MibScalar
a3ComSysSystemSoftwareRevision = _A3ComSysSystemSoftwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 1, 9),
    _A3ComSysSystemSoftwareRevision_Type()
)
a3ComSysSystemSoftwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysSystemSoftwareRevision.setStatus("mandatory")


class _A3ComSysSystemBuildTime_Type(DisplayString):
    """Custom type a3ComSysSystemBuildTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_A3ComSysSystemBuildTime_Type.__name__ = "DisplayString"
_A3ComSysSystemBuildTime_Object = MibScalar
a3ComSysSystemBuildTime = _A3ComSysSystemBuildTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 1, 10),
    _A3ComSysSystemBuildTime_Type()
)
a3ComSysSystemBuildTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysSystemBuildTime.setStatus("mandatory")
_A3ComSysSystemSnmpRevision_Type = Integer32
_A3ComSysSystemSnmpRevision_Object = MibScalar
a3ComSysSystemSnmpRevision = _A3ComSysSystemSnmpRevision_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 1, 11),
    _A3ComSysSystemSnmpRevision_Type()
)
a3ComSysSystemSnmpRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysSystemSnmpRevision.setStatus("mandatory")


class _A3ComSysSystemRequestedSnmpMode_Type(Integer32):
    """Custom type a3ComSysSystemRequestedSnmpMode based on Integer32"""
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


_A3ComSysSystemRequestedSnmpMode_Type.__name__ = "Integer32"
_A3ComSysSystemRequestedSnmpMode_Object = MibScalar
a3ComSysSystemRequestedSnmpMode = _A3ComSysSystemRequestedSnmpMode_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 1, 12),
    _A3ComSysSystemRequestedSnmpMode_Type()
)
a3ComSysSystemRequestedSnmpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComSysSystemRequestedSnmpMode.setStatus("mandatory")


class _A3ComSysSystemCurrentSnmpMode_Type(Integer32):
    """Custom type a3ComSysSystemCurrentSnmpMode based on Integer32"""
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


_A3ComSysSystemCurrentSnmpMode_Type.__name__ = "Integer32"
_A3ComSysSystemCurrentSnmpMode_Object = MibScalar
a3ComSysSystemCurrentSnmpMode = _A3ComSysSystemCurrentSnmpMode_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 1, 13),
    _A3ComSysSystemCurrentSnmpMode_Type()
)
a3ComSysSystemCurrentSnmpMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysSystemCurrentSnmpMode.setStatus("mandatory")


class _A3ComSysSystemAction_Type(Integer32):
    """Custom type a3ComSysSystemAction based on Integer32"""
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


_A3ComSysSystemAction_Type.__name__ = "Integer32"
_A3ComSysSystemAction_Object = MibScalar
a3ComSysSystemAction = _A3ComSysSystemAction_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 1, 14),
    _A3ComSysSystemAction_Type()
)
a3ComSysSystemAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComSysSystemAction.setStatus("mandatory")


class _A3ComSysSystemOvertemperature_Type(Integer32):
    """Custom type a3ComSysSystemOvertemperature based on Integer32"""
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


_A3ComSysSystemOvertemperature_Type.__name__ = "Integer32"
_A3ComSysSystemOvertemperature_Object = MibScalar
a3ComSysSystemOvertemperature = _A3ComSysSystemOvertemperature_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 1, 15),
    _A3ComSysSystemOvertemperature_Type()
)
a3ComSysSystemOvertemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysSystemOvertemperature.setStatus("mandatory")


class _A3ComSysSystemFanFailure_Type(Integer32):
    """Custom type a3ComSysSystemFanFailure based on Integer32"""
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


_A3ComSysSystemFanFailure_Type.__name__ = "Integer32"
_A3ComSysSystemFanFailure_Object = MibScalar
a3ComSysSystemFanFailure = _A3ComSysSystemFanFailure_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 1, 16),
    _A3ComSysSystemFanFailure_Type()
)
a3ComSysSystemFanFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysSystemFanFailure.setStatus("mandatory")
_A3ComSysSystemProtocolMask_Type = Integer32
_A3ComSysSystemProtocolMask_Object = MibScalar
a3ComSysSystemProtocolMask = _A3ComSysSystemProtocolMask_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 1, 17),
    _A3ComSysSystemProtocolMask_Type()
)
a3ComSysSystemProtocolMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysSystemProtocolMask.setStatus("mandatory")


class _A3ComSysSystemConsoleAccess_Type(Integer32):
    """Custom type a3ComSysSystemConsoleAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_A3ComSysSystemConsoleAccess_Type.__name__ = "Integer32"
_A3ComSysSystemConsoleAccess_Object = MibScalar
a3ComSysSystemConsoleAccess = _A3ComSysSystemConsoleAccess_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 1, 18),
    _A3ComSysSystemConsoleAccess_Type()
)
a3ComSysSystemConsoleAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComSysSystemConsoleAccess.setStatus("mandatory")


class _A3ComSysSystemConsoleReadPwd_Type(DisplayString):
    """Custom type a3ComSysSystemConsoleReadPwd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_A3ComSysSystemConsoleReadPwd_Type.__name__ = "DisplayString"
_A3ComSysSystemConsoleReadPwd_Object = MibScalar
a3ComSysSystemConsoleReadPwd = _A3ComSysSystemConsoleReadPwd_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 1, 19),
    _A3ComSysSystemConsoleReadPwd_Type()
)
a3ComSysSystemConsoleReadPwd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComSysSystemConsoleReadPwd.setStatus("mandatory")


class _A3ComSysSystemConsoleWritePwd_Type(DisplayString):
    """Custom type a3ComSysSystemConsoleWritePwd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_A3ComSysSystemConsoleWritePwd_Type.__name__ = "DisplayString"
_A3ComSysSystemConsoleWritePwd_Object = MibScalar
a3ComSysSystemConsoleWritePwd = _A3ComSysSystemConsoleWritePwd_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 1, 20),
    _A3ComSysSystemConsoleWritePwd_Type()
)
a3ComSysSystemConsoleWritePwd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComSysSystemConsoleWritePwd.setStatus("mandatory")


class _A3ComSysSystemConsoleAdminPwd_Type(DisplayString):
    """Custom type a3ComSysSystemConsoleAdminPwd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_A3ComSysSystemConsoleAdminPwd_Type.__name__ = "DisplayString"
_A3ComSysSystemConsoleAdminPwd_Object = MibScalar
a3ComSysSystemConsoleAdminPwd = _A3ComSysSystemConsoleAdminPwd_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 1, 21),
    _A3ComSysSystemConsoleAdminPwd_Type()
)
a3ComSysSystemConsoleAdminPwd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComSysSystemConsoleAdminPwd.setStatus("mandatory")
_A3ComSysSystemDateTime_Type = DisplayString
_A3ComSysSystemDateTime_Object = MibScalar
a3ComSysSystemDateTime = _A3ComSysSystemDateTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 1, 22),
    _A3ComSysSystemDateTime_Type()
)
a3ComSysSystemDateTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComSysSystemDateTime.setStatus("mandatory")


class _A3ComSysSystemDSTime_Type(Integer32):
    """Custom type a3ComSysSystemDSTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-120, 120),
    )


_A3ComSysSystemDSTime_Type.__name__ = "Integer32"
_A3ComSysSystemDSTime_Object = MibScalar
a3ComSysSystemDSTime = _A3ComSysSystemDSTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 1, 23),
    _A3ComSysSystemDSTime_Type()
)
a3ComSysSystemDSTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComSysSystemDSTime.setStatus("mandatory")


class _A3ComSysSystemTimeZone_Type(Integer32):
    """Custom type a3ComSysSystemTimeZone based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-720, 720),
    )


_A3ComSysSystemTimeZone_Type.__name__ = "Integer32"
_A3ComSysSystemTimeZone_Object = MibScalar
a3ComSysSystemTimeZone = _A3ComSysSystemTimeZone_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 1, 24),
    _A3ComSysSystemTimeZone_Type()
)
a3ComSysSystemTimeZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComSysSystemTimeZone.setStatus("mandatory")


class _A3ComSysSystemCurrentFddiStationMode_Type(Integer32):
    """Custom type a3ComSysSystemCurrentFddiStationMode based on Integer32"""
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


_A3ComSysSystemCurrentFddiStationMode_Type.__name__ = "Integer32"
_A3ComSysSystemCurrentFddiStationMode_Object = MibScalar
a3ComSysSystemCurrentFddiStationMode = _A3ComSysSystemCurrentFddiStationMode_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 1, 25),
    _A3ComSysSystemCurrentFddiStationMode_Type()
)
a3ComSysSystemCurrentFddiStationMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysSystemCurrentFddiStationMode.setStatus("mandatory")


class _A3ComSysSystemRequestedFddiStationMode_Type(Integer32):
    """Custom type a3ComSysSystemRequestedFddiStationMode based on Integer32"""
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


_A3ComSysSystemRequestedFddiStationMode_Type.__name__ = "Integer32"
_A3ComSysSystemRequestedFddiStationMode_Object = MibScalar
a3ComSysSystemRequestedFddiStationMode = _A3ComSysSystemRequestedFddiStationMode_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 1, 26),
    _A3ComSysSystemRequestedFddiStationMode_Type()
)
a3ComSysSystemRequestedFddiStationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComSysSystemRequestedFddiStationMode.setStatus("mandatory")
_A3ComSysSystemLog_ObjectIdentity = ObjectIdentity
a3ComSysSystemLog = _A3ComSysSystemLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 1, 27)
)
_A3ComSysSystemLogEntryCurrentCount_Type = Integer32
_A3ComSysSystemLogEntryCurrentCount_Object = MibScalar
a3ComSysSystemLogEntryCurrentCount = _A3ComSysSystemLogEntryCurrentCount_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 1, 27, 1),
    _A3ComSysSystemLogEntryCurrentCount_Type()
)
a3ComSysSystemLogEntryCurrentCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysSystemLogEntryCurrentCount.setStatus("mandatory")
_A3ComSysSystemLogMaxSize_Type = Integer32
_A3ComSysSystemLogMaxSize_Object = MibScalar
a3ComSysSystemLogMaxSize = _A3ComSysSystemLogMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 1, 27, 2),
    _A3ComSysSystemLogMaxSize_Type()
)
a3ComSysSystemLogMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysSystemLogMaxSize.setStatus("mandatory")


class _A3ComSysSystemLogSeverityThreshold_Type(Integer32):
    """Custom type a3ComSysSystemLogSeverityThreshold based on Integer32"""
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


_A3ComSysSystemLogSeverityThreshold_Type.__name__ = "Integer32"
_A3ComSysSystemLogSeverityThreshold_Object = MibScalar
a3ComSysSystemLogSeverityThreshold = _A3ComSysSystemLogSeverityThreshold_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 1, 27, 3),
    _A3ComSysSystemLogSeverityThreshold_Type()
)
a3ComSysSystemLogSeverityThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComSysSystemLogSeverityThreshold.setStatus("mandatory")
_A3ComSysSystemLogTable_Object = MibTable
a3ComSysSystemLogTable = _A3ComSysSystemLogTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 1, 27, 4)
)
if mibBuilder.loadTexts:
    a3ComSysSystemLogTable.setStatus("mandatory")
_A3ComSysSystemLogEntry_Object = MibTableRow
a3ComSysSystemLogEntry = _A3ComSysSystemLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 1, 27, 4, 1)
)
a3ComSysSystemLogEntry.setIndexNames(
    (0, "A3COM-SWITCHING-SYSTEMS-MIB", "a3ComSysSystemLogIndex"),
)
if mibBuilder.loadTexts:
    a3ComSysSystemLogEntry.setStatus("mandatory")
_A3ComSysSystemLogIndex_Type = Integer32
_A3ComSysSystemLogIndex_Object = MibTableColumn
a3ComSysSystemLogIndex = _A3ComSysSystemLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 1, 27, 4, 1, 1),
    _A3ComSysSystemLogIndex_Type()
)
a3ComSysSystemLogIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysSystemLogIndex.setStatus("mandatory")


class _A3ComSysSystemLogSeverityLevel_Type(Integer32):
    """Custom type a3ComSysSystemLogSeverityLevel based on Integer32"""
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


_A3ComSysSystemLogSeverityLevel_Type.__name__ = "Integer32"
_A3ComSysSystemLogSeverityLevel_Object = MibTableColumn
a3ComSysSystemLogSeverityLevel = _A3ComSysSystemLogSeverityLevel_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 1, 27, 4, 1, 2),
    _A3ComSysSystemLogSeverityLevel_Type()
)
a3ComSysSystemLogSeverityLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysSystemLogSeverityLevel.setStatus("mandatory")
_A3ComSysSystemLogDateTime_Type = DisplayString
_A3ComSysSystemLogDateTime_Object = MibTableColumn
a3ComSysSystemLogDateTime = _A3ComSysSystemLogDateTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 1, 27, 4, 1, 3),
    _A3ComSysSystemLogDateTime_Type()
)
a3ComSysSystemLogDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysSystemLogDateTime.setStatus("mandatory")


class _A3ComSysSystemLogFacility_Type(Integer32):
    """Custom type a3ComSysSystemLogFacility based on Integer32"""
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


_A3ComSysSystemLogFacility_Type.__name__ = "Integer32"
_A3ComSysSystemLogFacility_Object = MibTableColumn
a3ComSysSystemLogFacility = _A3ComSysSystemLogFacility_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 1, 27, 4, 1, 4),
    _A3ComSysSystemLogFacility_Type()
)
a3ComSysSystemLogFacility.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysSystemLogFacility.setStatus("mandatory")
_A3ComSysSystemLogMessage_Type = DisplayString
_A3ComSysSystemLogMessage_Object = MibTableColumn
a3ComSysSystemLogMessage = _A3ComSysSystemLogMessage_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 1, 27, 4, 1, 5),
    _A3ComSysSystemLogMessage_Type()
)
a3ComSysSystemLogMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysSystemLogMessage.setStatus("mandatory")
_A3ComSysSystemBaseMACAddress_Type = MacAddress
_A3ComSysSystemBaseMACAddress_Object = MibScalar
a3ComSysSystemBaseMACAddress = _A3ComSysSystemBaseMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 1, 28),
    _A3ComSysSystemBaseMACAddress_Type()
)
a3ComSysSystemBaseMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysSystemBaseMACAddress.setStatus("mandatory")
_A3ComSysSystemMACAddressCount_Type = Integer32
_A3ComSysSystemMACAddressCount_Object = MibScalar
a3ComSysSystemMACAddressCount = _A3ComSysSystemMACAddressCount_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 1, 29),
    _A3ComSysSystemMACAddressCount_Type()
)
a3ComSysSystemMACAddressCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysSystemMACAddressCount.setStatus("mandatory")


class _A3ComSysSystemChassisSerialNumber_Type(DisplayString):
    """Custom type a3ComSysSystemChassisSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )


_A3ComSysSystemChassisSerialNumber_Type.__name__ = "DisplayString"
_A3ComSysSystemChassisSerialNumber_Object = MibScalar
a3ComSysSystemChassisSerialNumber = _A3ComSysSystemChassisSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 1, 30),
    _A3ComSysSystemChassisSerialNumber_Type()
)
a3ComSysSystemChassisSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysSystemChassisSerialNumber.setStatus("mandatory")
_A3ComSysSystemFPMemorySize_Type = Integer32
_A3ComSysSystemFPMemorySize_Object = MibScalar
a3ComSysSystemFPMemorySize = _A3ComSysSystemFPMemorySize_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 1, 31),
    _A3ComSysSystemFPMemorySize_Type()
)
a3ComSysSystemFPMemorySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysSystemFPMemorySize.setStatus("mandatory")
_A3ComSysSystemBufferSize_Type = Integer32
_A3ComSysSystemBufferSize_Object = MibScalar
a3ComSysSystemBufferSize = _A3ComSysSystemBufferSize_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 1, 32),
    _A3ComSysSystemBufferSize_Type()
)
a3ComSysSystemBufferSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysSystemBufferSize.setStatus("mandatory")
_A3ComSysSlot_ObjectIdentity = ObjectIdentity
a3ComSysSlot = _A3ComSysSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 2)
)
_A3ComSysSlotCount_Type = Integer32
_A3ComSysSlotCount_Object = MibScalar
a3ComSysSlotCount = _A3ComSysSlotCount_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 2, 1),
    _A3ComSysSlotCount_Type()
)
a3ComSysSlotCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysSlotCount.setStatus("mandatory")
_A3ComSysSlotTable_Object = MibTable
a3ComSysSlotTable = _A3ComSysSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 2, 2)
)
if mibBuilder.loadTexts:
    a3ComSysSlotTable.setStatus("mandatory")
_A3ComSysSlotEntry_Object = MibTableRow
a3ComSysSlotEntry = _A3ComSysSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 2, 2, 1)
)
a3ComSysSlotEntry.setIndexNames(
    (0, "A3COM-SWITCHING-SYSTEMS-MIB", "a3ComSysSlotIndex"),
)
if mibBuilder.loadTexts:
    a3ComSysSlotEntry.setStatus("mandatory")
_A3ComSysSlotIndex_Type = Integer32
_A3ComSysSlotIndex_Object = MibTableColumn
a3ComSysSlotIndex = _A3ComSysSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 2, 2, 1, 1),
    _A3ComSysSlotIndex_Type()
)
a3ComSysSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysSlotIndex.setStatus("mandatory")


class _A3ComSysSlotBoardType_Type(Integer32):
    """Custom type a3ComSysSlotBoardType based on Integer32"""
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


_A3ComSysSlotBoardType_Type.__name__ = "Integer32"
_A3ComSysSlotBoardType_Object = MibTableColumn
a3ComSysSlotBoardType = _A3ComSysSlotBoardType_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 2, 2, 1, 2),
    _A3ComSysSlotBoardType_Type()
)
a3ComSysSlotBoardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysSlotBoardType.setStatus("mandatory")


class _A3ComSysSlotBoardRevision_Type(OctetString):
    """Custom type a3ComSysSlotBoardRevision based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1),
    )


_A3ComSysSlotBoardRevision_Type.__name__ = "OctetString"
_A3ComSysSlotBoardRevision_Object = MibTableColumn
a3ComSysSlotBoardRevision = _A3ComSysSlotBoardRevision_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 2, 2, 1, 3),
    _A3ComSysSlotBoardRevision_Type()
)
a3ComSysSlotBoardRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysSlotBoardRevision.setStatus("mandatory")


class _A3ComSysSlotBoardStatus_Type(Integer32):
    """Custom type a3ComSysSlotBoardStatus based on Integer32"""
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


_A3ComSysSlotBoardStatus_Type.__name__ = "Integer32"
_A3ComSysSlotBoardStatus_Object = MibTableColumn
a3ComSysSlotBoardStatus = _A3ComSysSlotBoardStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 2, 2, 1, 4),
    _A3ComSysSlotBoardStatus_Type()
)
a3ComSysSlotBoardStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysSlotBoardStatus.setStatus("mandatory")


class _A3ComSysSlotBoardName_Type(DisplayString):
    """Custom type a3ComSysSlotBoardName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_A3ComSysSlotBoardName_Type.__name__ = "DisplayString"
_A3ComSysSlotBoardName_Object = MibTableColumn
a3ComSysSlotBoardName = _A3ComSysSlotBoardName_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 2, 2, 1, 5),
    _A3ComSysSlotBoardName_Type()
)
a3ComSysSlotBoardName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysSlotBoardName.setStatus("mandatory")


class _A3ComSysSlotBoardNameAbbrev_Type(DisplayString):
    """Custom type a3ComSysSlotBoardNameAbbrev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_A3ComSysSlotBoardNameAbbrev_Type.__name__ = "DisplayString"
_A3ComSysSlotBoardNameAbbrev_Object = MibTableColumn
a3ComSysSlotBoardNameAbbrev = _A3ComSysSlotBoardNameAbbrev_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 2, 2, 1, 6),
    _A3ComSysSlotBoardNameAbbrev_Type()
)
a3ComSysSlotBoardNameAbbrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysSlotBoardNameAbbrev.setStatus("mandatory")
_A3ComSysSlotEthernetPortCount_Type = Integer32
_A3ComSysSlotEthernetPortCount_Object = MibTableColumn
a3ComSysSlotEthernetPortCount = _A3ComSysSlotEthernetPortCount_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 2, 2, 1, 7),
    _A3ComSysSlotEthernetPortCount_Type()
)
a3ComSysSlotEthernetPortCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysSlotEthernetPortCount.setStatus("mandatory")
_A3ComSysSlotFddiMacCount_Type = Integer32
_A3ComSysSlotFddiMacCount_Object = MibTableColumn
a3ComSysSlotFddiMacCount = _A3ComSysSlotFddiMacCount_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 2, 2, 1, 8),
    _A3ComSysSlotFddiMacCount_Type()
)
a3ComSysSlotFddiMacCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysSlotFddiMacCount.setStatus("mandatory")
_A3ComSysSlotFddiPortCount_Type = Integer32
_A3ComSysSlotFddiPortCount_Object = MibTableColumn
a3ComSysSlotFddiPortCount = _A3ComSysSlotFddiPortCount_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 2, 2, 1, 9),
    _A3ComSysSlotFddiPortCount_Type()
)
a3ComSysSlotFddiPortCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysSlotFddiPortCount.setStatus("mandatory")


class _A3ComSysSlotOvertemperature_Type(Integer32):
    """Custom type a3ComSysSlotOvertemperature based on Integer32"""
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


_A3ComSysSlotOvertemperature_Type.__name__ = "Integer32"
_A3ComSysSlotOvertemperature_Object = MibTableColumn
a3ComSysSlotOvertemperature = _A3ComSysSlotOvertemperature_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 2, 2, 1, 10),
    _A3ComSysSlotOvertemperature_Type()
)
a3ComSysSlotOvertemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysSlotOvertemperature.setStatus("mandatory")
_A3ComSysSlotTokenRingPortCount_Type = Integer32
_A3ComSysSlotTokenRingPortCount_Object = MibTableColumn
a3ComSysSlotTokenRingPortCount = _A3ComSysSlotTokenRingPortCount_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 2, 2, 1, 11),
    _A3ComSysSlotTokenRingPortCount_Type()
)
a3ComSysSlotTokenRingPortCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysSlotTokenRingPortCount.setStatus("mandatory")


class _A3ComSysSlotBoardRevStr_Type(DisplayString):
    """Custom type a3ComSysSlotBoardRevStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_A3ComSysSlotBoardRevStr_Type.__name__ = "DisplayString"
_A3ComSysSlotBoardRevStr_Object = MibTableColumn
a3ComSysSlotBoardRevStr = _A3ComSysSlotBoardRevStr_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 2, 2, 1, 12),
    _A3ComSysSlotBoardRevStr_Type()
)
a3ComSysSlotBoardRevStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysSlotBoardRevStr.setStatus("mandatory")


class _A3ComSysSlotConverterBad_Type(Integer32):
    """Custom type a3ComSysSlotConverterBad based on Integer32"""
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


_A3ComSysSlotConverterBad_Type.__name__ = "Integer32"
_A3ComSysSlotConverterBad_Object = MibTableColumn
a3ComSysSlotConverterBad = _A3ComSysSlotConverterBad_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 2, 2, 1, 13),
    _A3ComSysSlotConverterBad_Type()
)
a3ComSysSlotConverterBad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysSlotConverterBad.setStatus("mandatory")
_A3ComSysControlPanel_ObjectIdentity = ObjectIdentity
a3ComSysControlPanel = _A3ComSysControlPanel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 3)
)


class _A3ComSysControlPanelHardwareRevision_Type(OctetString):
    """Custom type a3ComSysControlPanelHardwareRevision based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_A3ComSysControlPanelHardwareRevision_Type.__name__ = "OctetString"
_A3ComSysControlPanelHardwareRevision_Object = MibScalar
a3ComSysControlPanelHardwareRevision = _A3ComSysControlPanelHardwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 3, 1),
    _A3ComSysControlPanelHardwareRevision_Type()
)
a3ComSysControlPanelHardwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysControlPanelHardwareRevision.setStatus("mandatory")


class _A3ComSysControlPanelSoftwareRevision_Type(OctetString):
    """Custom type a3ComSysControlPanelSoftwareRevision based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_A3ComSysControlPanelSoftwareRevision_Type.__name__ = "OctetString"
_A3ComSysControlPanelSoftwareRevision_Object = MibScalar
a3ComSysControlPanelSoftwareRevision = _A3ComSysControlPanelSoftwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 3, 2),
    _A3ComSysControlPanelSoftwareRevision_Type()
)
a3ComSysControlPanelSoftwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysControlPanelSoftwareRevision.setStatus("mandatory")
_A3ComSysControlPanelLines_Type = Integer32
_A3ComSysControlPanelLines_Object = MibScalar
a3ComSysControlPanelLines = _A3ComSysControlPanelLines_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 3, 3),
    _A3ComSysControlPanelLines_Type()
)
a3ComSysControlPanelLines.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysControlPanelLines.setStatus("mandatory")
_A3ComSysControlPanelColumns_Type = Integer32
_A3ComSysControlPanelColumns_Object = MibScalar
a3ComSysControlPanelColumns = _A3ComSysControlPanelColumns_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 3, 4),
    _A3ComSysControlPanelColumns_Type()
)
a3ComSysControlPanelColumns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysControlPanelColumns.setStatus("mandatory")


class _A3ComSysControlPanelText_Type(OctetString):
    """Custom type a3ComSysControlPanelText based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_A3ComSysControlPanelText_Type.__name__ = "OctetString"
_A3ComSysControlPanelText_Object = MibScalar
a3ComSysControlPanelText = _A3ComSysControlPanelText_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 3, 5),
    _A3ComSysControlPanelText_Type()
)
a3ComSysControlPanelText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysControlPanelText.setStatus("mandatory")


class _A3ComSysControlPanelAccess_Type(Integer32):
    """Custom type a3ComSysControlPanelAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_A3ComSysControlPanelAccess_Type.__name__ = "Integer32"
_A3ComSysControlPanelAccess_Object = MibScalar
a3ComSysControlPanelAccess = _A3ComSysControlPanelAccess_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 3, 6),
    _A3ComSysControlPanelAccess_Type()
)
a3ComSysControlPanelAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComSysControlPanelAccess.setStatus("mandatory")
_A3ComSysPowerSupply_ObjectIdentity = ObjectIdentity
a3ComSysPowerSupply = _A3ComSysPowerSupply_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 4)
)
_A3ComSysPowerSupplyCount_Type = Integer32
_A3ComSysPowerSupplyCount_Object = MibScalar
a3ComSysPowerSupplyCount = _A3ComSysPowerSupplyCount_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 4, 1),
    _A3ComSysPowerSupplyCount_Type()
)
a3ComSysPowerSupplyCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysPowerSupplyCount.setStatus("mandatory")
_A3ComSysPowerSupplyStatusTable_Object = MibTable
a3ComSysPowerSupplyStatusTable = _A3ComSysPowerSupplyStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 4, 2)
)
if mibBuilder.loadTexts:
    a3ComSysPowerSupplyStatusTable.setStatus("mandatory")
_A3ComSysPowerSupplyStatusEntry_Object = MibTableRow
a3ComSysPowerSupplyStatusEntry = _A3ComSysPowerSupplyStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 4, 2, 1)
)
a3ComSysPowerSupplyStatusEntry.setIndexNames(
    (0, "A3COM-SWITCHING-SYSTEMS-MIB", "a3ComSysPowerSupplyStatusIndex"),
)
if mibBuilder.loadTexts:
    a3ComSysPowerSupplyStatusEntry.setStatus("mandatory")
_A3ComSysPowerSupplyStatusIndex_Type = Integer32
_A3ComSysPowerSupplyStatusIndex_Object = MibTableColumn
a3ComSysPowerSupplyStatusIndex = _A3ComSysPowerSupplyStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 4, 2, 1, 1),
    _A3ComSysPowerSupplyStatusIndex_Type()
)
a3ComSysPowerSupplyStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysPowerSupplyStatusIndex.setStatus("mandatory")
_A3ComSysPowerSupplyStatus_Type = Integer32
_A3ComSysPowerSupplyStatus_Object = MibTableColumn
a3ComSysPowerSupplyStatus = _A3ComSysPowerSupplyStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 4, 2, 1, 2),
    _A3ComSysPowerSupplyStatus_Type()
)
a3ComSysPowerSupplyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysPowerSupplyStatus.setStatus("mandatory")
_A3ComSysPowerSupplyStatusSupported_Type = Integer32
_A3ComSysPowerSupplyStatusSupported_Object = MibTableColumn
a3ComSysPowerSupplyStatusSupported = _A3ComSysPowerSupplyStatusSupported_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 4, 2, 1, 3),
    _A3ComSysPowerSupplyStatusSupported_Type()
)
a3ComSysPowerSupplyStatusSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysPowerSupplyStatusSupported.setStatus("mandatory")
_A3ComSysSnmp_ObjectIdentity = ObjectIdentity
a3ComSysSnmp = _A3ComSysSnmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 5)
)
_A3ComSysSnmpAgentId_Type = Integer32
_A3ComSysSnmpAgentId_Object = MibScalar
a3ComSysSnmpAgentId = _A3ComSysSnmpAgentId_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 5, 1),
    _A3ComSysSnmpAgentId_Type()
)
a3ComSysSnmpAgentId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysSnmpAgentId.setStatus("mandatory")


class _A3ComSysSnmpInternalAgentTrapMask_Type(OctetString):
    """Custom type a3ComSysSnmpInternalAgentTrapMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_A3ComSysSnmpInternalAgentTrapMask_Type.__name__ = "OctetString"
_A3ComSysSnmpInternalAgentTrapMask_Object = MibScalar
a3ComSysSnmpInternalAgentTrapMask = _A3ComSysSnmpInternalAgentTrapMask_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 5, 2),
    _A3ComSysSnmpInternalAgentTrapMask_Type()
)
a3ComSysSnmpInternalAgentTrapMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComSysSnmpInternalAgentTrapMask.setStatus("mandatory")
_A3ComSysSnmpInternalAgentTrapDestinationMask_Type = Integer32
_A3ComSysSnmpInternalAgentTrapDestinationMask_Object = MibScalar
a3ComSysSnmpInternalAgentTrapDestinationMask = _A3ComSysSnmpInternalAgentTrapDestinationMask_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 5, 3),
    _A3ComSysSnmpInternalAgentTrapDestinationMask_Type()
)
a3ComSysSnmpInternalAgentTrapDestinationMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComSysSnmpInternalAgentTrapDestinationMask.setStatus("mandatory")


class _A3ComSysSnmpProxyInternalRequests_Type(Integer32):
    """Custom type a3ComSysSnmpProxyInternalRequests based on Integer32"""
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


_A3ComSysSnmpProxyInternalRequests_Type.__name__ = "Integer32"
_A3ComSysSnmpProxyInternalRequests_Object = MibScalar
a3ComSysSnmpProxyInternalRequests = _A3ComSysSnmpProxyInternalRequests_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 5, 4),
    _A3ComSysSnmpProxyInternalRequests_Type()
)
a3ComSysSnmpProxyInternalRequests.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComSysSnmpProxyInternalRequests.setStatus("deprecated")


class _A3ComSysSnmpInternalProxyRequestMaxAge_Type(Integer32):
    """Custom type a3ComSysSnmpInternalProxyRequestMaxAge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_A3ComSysSnmpInternalProxyRequestMaxAge_Type.__name__ = "Integer32"
_A3ComSysSnmpInternalProxyRequestMaxAge_Object = MibScalar
a3ComSysSnmpInternalProxyRequestMaxAge = _A3ComSysSnmpInternalProxyRequestMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 5, 5),
    _A3ComSysSnmpInternalProxyRequestMaxAge_Type()
)
a3ComSysSnmpInternalProxyRequestMaxAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComSysSnmpInternalProxyRequestMaxAge.setStatus("mandatory")


class _A3ComSysSnmpProxyInternalTraps_Type(Integer32):
    """Custom type a3ComSysSnmpProxyInternalTraps based on Integer32"""
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


_A3ComSysSnmpProxyInternalTraps_Type.__name__ = "Integer32"
_A3ComSysSnmpProxyInternalTraps_Object = MibScalar
a3ComSysSnmpProxyInternalTraps = _A3ComSysSnmpProxyInternalTraps_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 5, 6),
    _A3ComSysSnmpProxyInternalTraps_Type()
)
a3ComSysSnmpProxyInternalTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComSysSnmpProxyInternalTraps.setStatus("deprecated")
_A3ComSysSnmpInternalProxyTable_Object = MibTable
a3ComSysSnmpInternalProxyTable = _A3ComSysSnmpInternalProxyTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 5, 7)
)
if mibBuilder.loadTexts:
    a3ComSysSnmpInternalProxyTable.setStatus("mandatory")
_A3ComSysSnmpInternalProxyEntry_Object = MibTableRow
a3ComSysSnmpInternalProxyEntry = _A3ComSysSnmpInternalProxyEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 5, 7, 1)
)
a3ComSysSnmpInternalProxyEntry.setIndexNames(
    (0, "A3COM-SWITCHING-SYSTEMS-MIB", "a3ComSysSnmpInternalProxyAgentId"),
    (0, "A3COM-SWITCHING-SYSTEMS-MIB", "a3ComSysSnmpInternalProxyAccessClass"),
)
if mibBuilder.loadTexts:
    a3ComSysSnmpInternalProxyEntry.setStatus("mandatory")
_A3ComSysSnmpInternalProxyAgentId_Type = Integer32
_A3ComSysSnmpInternalProxyAgentId_Object = MibTableColumn
a3ComSysSnmpInternalProxyAgentId = _A3ComSysSnmpInternalProxyAgentId_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 5, 7, 1, 1),
    _A3ComSysSnmpInternalProxyAgentId_Type()
)
a3ComSysSnmpInternalProxyAgentId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysSnmpInternalProxyAgentId.setStatus("mandatory")


class _A3ComSysSnmpInternalProxyAccessClass_Type(Integer32):
    """Custom type a3ComSysSnmpInternalProxyAccessClass based on Integer32"""
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


_A3ComSysSnmpInternalProxyAccessClass_Type.__name__ = "Integer32"
_A3ComSysSnmpInternalProxyAccessClass_Object = MibTableColumn
a3ComSysSnmpInternalProxyAccessClass = _A3ComSysSnmpInternalProxyAccessClass_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 5, 7, 1, 2),
    _A3ComSysSnmpInternalProxyAccessClass_Type()
)
a3ComSysSnmpInternalProxyAccessClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysSnmpInternalProxyAccessClass.setStatus("mandatory")
_A3ComSysSnmpInternalProxyCommunity_Type = OctetString
_A3ComSysSnmpInternalProxyCommunity_Object = MibTableColumn
a3ComSysSnmpInternalProxyCommunity = _A3ComSysSnmpInternalProxyCommunity_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 5, 7, 1, 3),
    _A3ComSysSnmpInternalProxyCommunity_Type()
)
a3ComSysSnmpInternalProxyCommunity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysSnmpInternalProxyCommunity.setStatus("mandatory")
_A3ComSysAgent_ObjectIdentity = ObjectIdentity
a3ComSysAgent = _A3ComSysAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 6)
)


class _A3ComSysAgentRequestMaxAge_Type(Integer32):
    """Custom type a3ComSysAgentRequestMaxAge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_A3ComSysAgentRequestMaxAge_Type.__name__ = "Integer32"
_A3ComSysAgentRequestMaxAge_Object = MibScalar
a3ComSysAgentRequestMaxAge = _A3ComSysAgentRequestMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 6, 1),
    _A3ComSysAgentRequestMaxAge_Type()
)
a3ComSysAgentRequestMaxAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComSysAgentRequestMaxAge.setStatus("mandatory")


class _A3ComSysAgentProxyRemoteSmtRequests_Type(Integer32):
    """Custom type a3ComSysAgentProxyRemoteSmtRequests based on Integer32"""
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


_A3ComSysAgentProxyRemoteSmtRequests_Type.__name__ = "Integer32"
_A3ComSysAgentProxyRemoteSmtRequests_Object = MibScalar
a3ComSysAgentProxyRemoteSmtRequests = _A3ComSysAgentProxyRemoteSmtRequests_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 6, 2),
    _A3ComSysAgentProxyRemoteSmtRequests_Type()
)
a3ComSysAgentProxyRemoteSmtRequests.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComSysAgentProxyRemoteSmtRequests.setStatus("deprecated")


class _A3ComSysAgentRemoteSmtProxyRequestMaxAge_Type(Integer32):
    """Custom type a3ComSysAgentRemoteSmtProxyRequestMaxAge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_A3ComSysAgentRemoteSmtProxyRequestMaxAge_Type.__name__ = "Integer32"
_A3ComSysAgentRemoteSmtProxyRequestMaxAge_Object = MibScalar
a3ComSysAgentRemoteSmtProxyRequestMaxAge = _A3ComSysAgentRemoteSmtProxyRequestMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 6, 3),
    _A3ComSysAgentRemoteSmtProxyRequestMaxAge_Type()
)
a3ComSysAgentRemoteSmtProxyRequestMaxAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComSysAgentRemoteSmtProxyRequestMaxAge.setStatus("mandatory")


class _A3ComSysAgentProxyRemoteSmtEvents_Type(Integer32):
    """Custom type a3ComSysAgentProxyRemoteSmtEvents based on Integer32"""
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


_A3ComSysAgentProxyRemoteSmtEvents_Type.__name__ = "Integer32"
_A3ComSysAgentProxyRemoteSmtEvents_Object = MibScalar
a3ComSysAgentProxyRemoteSmtEvents = _A3ComSysAgentProxyRemoteSmtEvents_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 6, 4),
    _A3ComSysAgentProxyRemoteSmtEvents_Type()
)
a3ComSysAgentProxyRemoteSmtEvents.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComSysAgentProxyRemoteSmtEvents.setStatus("mandatory")
_A3ComSysAgentTrapDescriptionTable_Object = MibTable
a3ComSysAgentTrapDescriptionTable = _A3ComSysAgentTrapDescriptionTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 6, 5)
)
if mibBuilder.loadTexts:
    a3ComSysAgentTrapDescriptionTable.setStatus("mandatory")
_A3ComSysAgentTrapDescriptionTableEntry_Object = MibTableRow
a3ComSysAgentTrapDescriptionTableEntry = _A3ComSysAgentTrapDescriptionTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 6, 5, 1)
)
a3ComSysAgentTrapDescriptionTableEntry.setIndexNames(
    (0, "A3COM-SWITCHING-SYSTEMS-MIB", "a3ComSysAgentTrapDescriptionIndex"),
)
if mibBuilder.loadTexts:
    a3ComSysAgentTrapDescriptionTableEntry.setStatus("mandatory")
_A3ComSysAgentTrapDescriptionIndex_Type = Integer32
_A3ComSysAgentTrapDescriptionIndex_Object = MibTableColumn
a3ComSysAgentTrapDescriptionIndex = _A3ComSysAgentTrapDescriptionIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 6, 5, 1, 1),
    _A3ComSysAgentTrapDescriptionIndex_Type()
)
a3ComSysAgentTrapDescriptionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysAgentTrapDescriptionIndex.setStatus("mandatory")
_A3ComSysAgentTrapEnterprise_Type = ObjectIdentifier
_A3ComSysAgentTrapEnterprise_Object = MibTableColumn
a3ComSysAgentTrapEnterprise = _A3ComSysAgentTrapEnterprise_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 6, 5, 1, 2),
    _A3ComSysAgentTrapEnterprise_Type()
)
a3ComSysAgentTrapEnterprise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysAgentTrapEnterprise.setStatus("mandatory")
_A3ComSysAgentTrapNumber_Type = Integer32
_A3ComSysAgentTrapNumber_Object = MibTableColumn
a3ComSysAgentTrapNumber = _A3ComSysAgentTrapNumber_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 6, 5, 1, 3),
    _A3ComSysAgentTrapNumber_Type()
)
a3ComSysAgentTrapNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysAgentTrapNumber.setStatus("mandatory")
_A3ComSysAgentTrapDestinationTable_Object = MibTable
a3ComSysAgentTrapDestinationTable = _A3ComSysAgentTrapDestinationTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 6, 6)
)
if mibBuilder.loadTexts:
    a3ComSysAgentTrapDestinationTable.setStatus("mandatory")
_A3ComSysAgentTrapDestinationTableEntry_Object = MibTableRow
a3ComSysAgentTrapDestinationTableEntry = _A3ComSysAgentTrapDestinationTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 6, 6, 1)
)
a3ComSysAgentTrapDestinationTableEntry.setIndexNames(
    (0, "A3COM-SWITCHING-SYSTEMS-MIB", "a3ComSysAgentTrapDestinationAddressType"),
    (0, "A3COM-SWITCHING-SYSTEMS-MIB", "a3ComSysAgentTrapDestinationAddress"),
)
if mibBuilder.loadTexts:
    a3ComSysAgentTrapDestinationTableEntry.setStatus("mandatory")


class _A3ComSysAgentTrapDestinationAddressType_Type(Integer32):
    """Custom type a3ComSysAgentTrapDestinationAddressType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("ip", 1)
    )


_A3ComSysAgentTrapDestinationAddressType_Type.__name__ = "Integer32"
_A3ComSysAgentTrapDestinationAddressType_Object = MibTableColumn
a3ComSysAgentTrapDestinationAddressType = _A3ComSysAgentTrapDestinationAddressType_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 6, 6, 1, 1),
    _A3ComSysAgentTrapDestinationAddressType_Type()
)
a3ComSysAgentTrapDestinationAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysAgentTrapDestinationAddressType.setStatus("mandatory")
_A3ComSysAgentTrapDestinationAddress_Type = OctetString
_A3ComSysAgentTrapDestinationAddress_Object = MibTableColumn
a3ComSysAgentTrapDestinationAddress = _A3ComSysAgentTrapDestinationAddress_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 6, 6, 1, 2),
    _A3ComSysAgentTrapDestinationAddress_Type()
)
a3ComSysAgentTrapDestinationAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysAgentTrapDestinationAddress.setStatus("mandatory")


class _A3ComSysAgentTrapDestinationTrapMask_Type(OctetString):
    """Custom type a3ComSysAgentTrapDestinationTrapMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_A3ComSysAgentTrapDestinationTrapMask_Type.__name__ = "OctetString"
_A3ComSysAgentTrapDestinationTrapMask_Object = MibTableColumn
a3ComSysAgentTrapDestinationTrapMask = _A3ComSysAgentTrapDestinationTrapMask_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 6, 6, 1, 3),
    _A3ComSysAgentTrapDestinationTrapMask_Type()
)
a3ComSysAgentTrapDestinationTrapMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComSysAgentTrapDestinationTrapMask.setStatus("mandatory")


class _A3ComSysAgentTrapDestinationEntryStatus_Type(Integer32):
    """Custom type a3ComSysAgentTrapDestinationEntryStatus based on Integer32"""
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


_A3ComSysAgentTrapDestinationEntryStatus_Type.__name__ = "Integer32"
_A3ComSysAgentTrapDestinationEntryStatus_Object = MibTableColumn
a3ComSysAgentTrapDestinationEntryStatus = _A3ComSysAgentTrapDestinationEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 6, 6, 1, 4),
    _A3ComSysAgentTrapDestinationEntryStatus_Type()
)
a3ComSysAgentTrapDestinationEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComSysAgentTrapDestinationEntryStatus.setStatus("mandatory")


class _A3ComSysAgentReadCommunity_Type(DisplayString):
    """Custom type a3ComSysAgentReadCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_A3ComSysAgentReadCommunity_Type.__name__ = "DisplayString"
_A3ComSysAgentReadCommunity_Object = MibScalar
a3ComSysAgentReadCommunity = _A3ComSysAgentReadCommunity_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 6, 7),
    _A3ComSysAgentReadCommunity_Type()
)
a3ComSysAgentReadCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComSysAgentReadCommunity.setStatus("mandatory")


class _A3ComSysAgentReadWriteCommunity_Type(DisplayString):
    """Custom type a3ComSysAgentReadWriteCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_A3ComSysAgentReadWriteCommunity_Type.__name__ = "DisplayString"
_A3ComSysAgentReadWriteCommunity_Object = MibScalar
a3ComSysAgentReadWriteCommunity = _A3ComSysAgentReadWriteCommunity_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 6, 8),
    _A3ComSysAgentReadWriteCommunity_Type()
)
a3ComSysAgentReadWriteCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComSysAgentReadWriteCommunity.setStatus("mandatory")
_A3ComSysInterface_ObjectIdentity = ObjectIdentity
a3ComSysInterface = _A3ComSysInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 7)
)
_A3ComSysInterfaceLocationTable_Object = MibTable
a3ComSysInterfaceLocationTable = _A3ComSysInterfaceLocationTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 7, 1)
)
if mibBuilder.loadTexts:
    a3ComSysInterfaceLocationTable.setStatus("mandatory")
_A3ComSysInterfaceLocationEntry_Object = MibTableRow
a3ComSysInterfaceLocationEntry = _A3ComSysInterfaceLocationEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 7, 1, 1)
)
a3ComSysInterfaceLocationEntry.setIndexNames(
    (0, "A3COM-SWITCHING-SYSTEMS-MIB", "a3ComSysInterfaceLocationIfIndex"),
)
if mibBuilder.loadTexts:
    a3ComSysInterfaceLocationEntry.setStatus("mandatory")
_A3ComSysInterfaceLocationIfIndex_Type = Integer32
_A3ComSysInterfaceLocationIfIndex_Object = MibTableColumn
a3ComSysInterfaceLocationIfIndex = _A3ComSysInterfaceLocationIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 7, 1, 1, 1),
    _A3ComSysInterfaceLocationIfIndex_Type()
)
a3ComSysInterfaceLocationIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysInterfaceLocationIfIndex.setStatus("mandatory")


class _A3ComSysInterfaceLocationInterfaceType_Type(Integer32):
    """Custom type a3ComSysInterfaceLocationInterfaceType based on Integer32"""
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


_A3ComSysInterfaceLocationInterfaceType_Type.__name__ = "Integer32"
_A3ComSysInterfaceLocationInterfaceType_Object = MibTableColumn
a3ComSysInterfaceLocationInterfaceType = _A3ComSysInterfaceLocationInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 7, 1, 1, 2),
    _A3ComSysInterfaceLocationInterfaceType_Type()
)
a3ComSysInterfaceLocationInterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysInterfaceLocationInterfaceType.setStatus("mandatory")


class _A3ComSysInterfaceLocationType_Type(Integer32):
    """Custom type a3ComSysInterfaceLocationType based on Integer32"""
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


_A3ComSysInterfaceLocationType_Type.__name__ = "Integer32"
_A3ComSysInterfaceLocationType_Object = MibTableColumn
a3ComSysInterfaceLocationType = _A3ComSysInterfaceLocationType_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 7, 1, 1, 3),
    _A3ComSysInterfaceLocationType_Type()
)
a3ComSysInterfaceLocationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysInterfaceLocationType.setStatus("mandatory")
_A3ComSysInterfaceLocationTypeIndex_Type = Integer32
_A3ComSysInterfaceLocationTypeIndex_Object = MibTableColumn
a3ComSysInterfaceLocationTypeIndex = _A3ComSysInterfaceLocationTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 7, 1, 1, 4),
    _A3ComSysInterfaceLocationTypeIndex_Type()
)
a3ComSysInterfaceLocationTypeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysInterfaceLocationTypeIndex.setStatus("mandatory")
_A3ComSysInterfaceLocationLocalIndex_Type = Integer32
_A3ComSysInterfaceLocationLocalIndex_Object = MibTableColumn
a3ComSysInterfaceLocationLocalIndex = _A3ComSysInterfaceLocationLocalIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 7, 1, 1, 5),
    _A3ComSysInterfaceLocationLocalIndex_Type()
)
a3ComSysInterfaceLocationLocalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysInterfaceLocationLocalIndex.setStatus("mandatory")
_A3ComSysInterfaceLocationSystemModuleIndex_Type = Integer32
_A3ComSysInterfaceLocationSystemModuleIndex_Object = MibTableColumn
a3ComSysInterfaceLocationSystemModuleIndex = _A3ComSysInterfaceLocationSystemModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 7, 1, 1, 6),
    _A3ComSysInterfaceLocationSystemModuleIndex_Type()
)
a3ComSysInterfaceLocationSystemModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysInterfaceLocationSystemModuleIndex.setStatus("mandatory")
_A3ComSysEthernetPort_ObjectIdentity = ObjectIdentity
a3ComSysEthernetPort = _A3ComSysEthernetPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 8)
)
_A3ComSysEthernetPortCount_Type = Integer32
_A3ComSysEthernetPortCount_Object = MibScalar
a3ComSysEthernetPortCount = _A3ComSysEthernetPortCount_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 8, 1),
    _A3ComSysEthernetPortCount_Type()
)
a3ComSysEthernetPortCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysEthernetPortCount.setStatus("mandatory")
_A3ComSysEthernetPortTable_Object = MibTable
a3ComSysEthernetPortTable = _A3ComSysEthernetPortTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 8, 2)
)
if mibBuilder.loadTexts:
    a3ComSysEthernetPortTable.setStatus("mandatory")
_A3ComSysEthernetPortEntry_Object = MibTableRow
a3ComSysEthernetPortEntry = _A3ComSysEthernetPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 8, 2, 1)
)
a3ComSysEthernetPortEntry.setIndexNames(
    (0, "A3COM-SWITCHING-SYSTEMS-MIB", "a3ComSysEthernetPortIndex"),
)
if mibBuilder.loadTexts:
    a3ComSysEthernetPortEntry.setStatus("mandatory")
_A3ComSysEthernetPortIndex_Type = Integer32
_A3ComSysEthernetPortIndex_Object = MibTableColumn
a3ComSysEthernetPortIndex = _A3ComSysEthernetPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 8, 2, 1, 1),
    _A3ComSysEthernetPortIndex_Type()
)
a3ComSysEthernetPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysEthernetPortIndex.setStatus("mandatory")
_A3ComSysEthernetPortIfIndex_Type = Integer32
_A3ComSysEthernetPortIfIndex_Object = MibTableColumn
a3ComSysEthernetPortIfIndex = _A3ComSysEthernetPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 8, 2, 1, 2),
    _A3ComSysEthernetPortIfIndex_Type()
)
a3ComSysEthernetPortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysEthernetPortIfIndex.setStatus("mandatory")


class _A3ComSysEthernetPortLabel_Type(DisplayString):
    """Custom type a3ComSysEthernetPortLabel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_A3ComSysEthernetPortLabel_Type.__name__ = "DisplayString"
_A3ComSysEthernetPortLabel_Object = MibTableColumn
a3ComSysEthernetPortLabel = _A3ComSysEthernetPortLabel_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 8, 2, 1, 3),
    _A3ComSysEthernetPortLabel_Type()
)
a3ComSysEthernetPortLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComSysEthernetPortLabel.setStatus("mandatory")


class _A3ComSysEthernetPortLinkStatus_Type(Integer32):
    """Custom type a3ComSysEthernetPortLinkStatus based on Integer32"""
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


_A3ComSysEthernetPortLinkStatus_Type.__name__ = "Integer32"
_A3ComSysEthernetPortLinkStatus_Object = MibTableColumn
a3ComSysEthernetPortLinkStatus = _A3ComSysEthernetPortLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 8, 2, 1, 4),
    _A3ComSysEthernetPortLinkStatus_Type()
)
a3ComSysEthernetPortLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysEthernetPortLinkStatus.setStatus("mandatory")


class _A3ComSysEthernetPortType_Type(Integer32):
    """Custom type a3ComSysEthernetPortType based on Integer32"""
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
              23,
              24)
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
          ("port1000NotPresent", 24),
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


_A3ComSysEthernetPortType_Type.__name__ = "Integer32"
_A3ComSysEthernetPortType_Object = MibTableColumn
a3ComSysEthernetPortType = _A3ComSysEthernetPortType_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 8, 2, 1, 5),
    _A3ComSysEthernetPortType_Type()
)
a3ComSysEthernetPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysEthernetPortType.setStatus("mandatory")
_A3ComSysEthernetPortRateTable_Object = MibTable
a3ComSysEthernetPortRateTable = _A3ComSysEthernetPortRateTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 8, 3)
)
if mibBuilder.loadTexts:
    a3ComSysEthernetPortRateTable.setStatus("mandatory")
_A3ComSysEthernetPortRateEntry_Object = MibTableRow
a3ComSysEthernetPortRateEntry = _A3ComSysEthernetPortRateEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 8, 3, 1)
)
a3ComSysEthernetPortRateEntry.setIndexNames(
    (0, "A3COM-SWITCHING-SYSTEMS-MIB", "a3ComSysEthernetPortRateIndex"),
)
if mibBuilder.loadTexts:
    a3ComSysEthernetPortRateEntry.setStatus("mandatory")
_A3ComSysEthernetPortRateIndex_Type = Integer32
_A3ComSysEthernetPortRateIndex_Object = MibTableColumn
a3ComSysEthernetPortRateIndex = _A3ComSysEthernetPortRateIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 8, 3, 1, 1),
    _A3ComSysEthernetPortRateIndex_Type()
)
a3ComSysEthernetPortRateIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysEthernetPortRateIndex.setStatus("mandatory")
_A3ComSysEthernetPortRateByteReceiveRate_Type = Integer32
_A3ComSysEthernetPortRateByteReceiveRate_Object = MibTableColumn
a3ComSysEthernetPortRateByteReceiveRate = _A3ComSysEthernetPortRateByteReceiveRate_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 8, 3, 1, 2),
    _A3ComSysEthernetPortRateByteReceiveRate_Type()
)
a3ComSysEthernetPortRateByteReceiveRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysEthernetPortRateByteReceiveRate.setStatus("mandatory")
_A3ComSysEthernetPortRatePeakByteReceiveRate_Type = Integer32
_A3ComSysEthernetPortRatePeakByteReceiveRate_Object = MibTableColumn
a3ComSysEthernetPortRatePeakByteReceiveRate = _A3ComSysEthernetPortRatePeakByteReceiveRate_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 8, 3, 1, 3),
    _A3ComSysEthernetPortRatePeakByteReceiveRate_Type()
)
a3ComSysEthernetPortRatePeakByteReceiveRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysEthernetPortRatePeakByteReceiveRate.setStatus("mandatory")
_A3ComSysEthernetPortRateFrameReceiveRate_Type = Integer32
_A3ComSysEthernetPortRateFrameReceiveRate_Object = MibTableColumn
a3ComSysEthernetPortRateFrameReceiveRate = _A3ComSysEthernetPortRateFrameReceiveRate_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 8, 3, 1, 4),
    _A3ComSysEthernetPortRateFrameReceiveRate_Type()
)
a3ComSysEthernetPortRateFrameReceiveRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysEthernetPortRateFrameReceiveRate.setStatus("mandatory")
_A3ComSysEthernetPortRatePeakFrameReceiveRate_Type = Integer32
_A3ComSysEthernetPortRatePeakFrameReceiveRate_Object = MibTableColumn
a3ComSysEthernetPortRatePeakFrameReceiveRate = _A3ComSysEthernetPortRatePeakFrameReceiveRate_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 8, 3, 1, 5),
    _A3ComSysEthernetPortRatePeakFrameReceiveRate_Type()
)
a3ComSysEthernetPortRatePeakFrameReceiveRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysEthernetPortRatePeakFrameReceiveRate.setStatus("mandatory")
_A3ComSysEthernetPortRateByteTransmitRate_Type = Integer32
_A3ComSysEthernetPortRateByteTransmitRate_Object = MibTableColumn
a3ComSysEthernetPortRateByteTransmitRate = _A3ComSysEthernetPortRateByteTransmitRate_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 8, 3, 1, 6),
    _A3ComSysEthernetPortRateByteTransmitRate_Type()
)
a3ComSysEthernetPortRateByteTransmitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysEthernetPortRateByteTransmitRate.setStatus("mandatory")
_A3ComSysEthernetPortRatePeakByteTransmitRate_Type = Integer32
_A3ComSysEthernetPortRatePeakByteTransmitRate_Object = MibTableColumn
a3ComSysEthernetPortRatePeakByteTransmitRate = _A3ComSysEthernetPortRatePeakByteTransmitRate_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 8, 3, 1, 7),
    _A3ComSysEthernetPortRatePeakByteTransmitRate_Type()
)
a3ComSysEthernetPortRatePeakByteTransmitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysEthernetPortRatePeakByteTransmitRate.setStatus("mandatory")
_A3ComSysEthernetPortRateFrameTransmitRate_Type = Integer32
_A3ComSysEthernetPortRateFrameTransmitRate_Object = MibTableColumn
a3ComSysEthernetPortRateFrameTransmitRate = _A3ComSysEthernetPortRateFrameTransmitRate_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 8, 3, 1, 8),
    _A3ComSysEthernetPortRateFrameTransmitRate_Type()
)
a3ComSysEthernetPortRateFrameTransmitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysEthernetPortRateFrameTransmitRate.setStatus("mandatory")
_A3ComSysEthernetPortRatePeakFrameTransmitRate_Type = Integer32
_A3ComSysEthernetPortRatePeakFrameTransmitRate_Object = MibTableColumn
a3ComSysEthernetPortRatePeakFrameTransmitRate = _A3ComSysEthernetPortRatePeakFrameTransmitRate_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 8, 3, 1, 9),
    _A3ComSysEthernetPortRatePeakFrameTransmitRate_Type()
)
a3ComSysEthernetPortRatePeakFrameTransmitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysEthernetPortRatePeakFrameTransmitRate.setStatus("mandatory")
_A3ComSysSmt_ObjectIdentity = ObjectIdentity
a3ComSysSmt = _A3ComSysSmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 9)
)
_A3ComSysSmtCount_Type = Integer32
_A3ComSysSmtCount_Object = MibScalar
a3ComSysSmtCount = _A3ComSysSmtCount_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 9, 1),
    _A3ComSysSmtCount_Type()
)
a3ComSysSmtCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysSmtCount.setStatus("mandatory")
_A3ComSysSmtFddiMacBeaconTable_Object = MibTable
a3ComSysSmtFddiMacBeaconTable = _A3ComSysSmtFddiMacBeaconTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 9, 4)
)
if mibBuilder.loadTexts:
    a3ComSysSmtFddiMacBeaconTable.setStatus("mandatory")
_A3ComSysSmtFddiMacBeaconEntry_Object = MibTableRow
a3ComSysSmtFddiMacBeaconEntry = _A3ComSysSmtFddiMacBeaconEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 9, 4, 1)
)
a3ComSysSmtFddiMacBeaconEntry.setIndexNames(
    (0, "A3COM-SWITCHING-SYSTEMS-MIB", "a3ComSysSmtFddiMacBeaconSmtIndex"),
    (0, "A3COM-SWITCHING-SYSTEMS-MIB", "a3ComSysSmtFddiMacBeaconIndex"),
)
if mibBuilder.loadTexts:
    a3ComSysSmtFddiMacBeaconEntry.setStatus("mandatory")
_A3ComSysSmtFddiMacBeaconSmtIndex_Type = Integer32
_A3ComSysSmtFddiMacBeaconSmtIndex_Object = MibTableColumn
a3ComSysSmtFddiMacBeaconSmtIndex = _A3ComSysSmtFddiMacBeaconSmtIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 9, 4, 1, 1),
    _A3ComSysSmtFddiMacBeaconSmtIndex_Type()
)
a3ComSysSmtFddiMacBeaconSmtIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysSmtFddiMacBeaconSmtIndex.setStatus("mandatory")
_A3ComSysSmtFddiMacBeaconIndex_Type = Integer32
_A3ComSysSmtFddiMacBeaconIndex_Object = MibTableColumn
a3ComSysSmtFddiMacBeaconIndex = _A3ComSysSmtFddiMacBeaconIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 9, 4, 1, 2),
    _A3ComSysSmtFddiMacBeaconIndex_Type()
)
a3ComSysSmtFddiMacBeaconIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysSmtFddiMacBeaconIndex.setStatus("mandatory")


class _A3ComSysSmtFddiMacBeaconHistory_Type(OctetString):
    """Custom type a3ComSysSmtFddiMacBeaconHistory based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_A3ComSysSmtFddiMacBeaconHistory_Type.__name__ = "OctetString"
_A3ComSysSmtFddiMacBeaconHistory_Object = MibTableColumn
a3ComSysSmtFddiMacBeaconHistory = _A3ComSysSmtFddiMacBeaconHistory_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 9, 4, 1, 3),
    _A3ComSysSmtFddiMacBeaconHistory_Type()
)
a3ComSysSmtFddiMacBeaconHistory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysSmtFddiMacBeaconHistory.setStatus("mandatory")
_A3ComSysSmtFddiMacRateTable_Object = MibTable
a3ComSysSmtFddiMacRateTable = _A3ComSysSmtFddiMacRateTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 9, 5)
)
if mibBuilder.loadTexts:
    a3ComSysSmtFddiMacRateTable.setStatus("mandatory")
_A3ComSysSmtFddiMacRateEntry_Object = MibTableRow
a3ComSysSmtFddiMacRateEntry = _A3ComSysSmtFddiMacRateEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 9, 5, 1)
)
a3ComSysSmtFddiMacRateEntry.setIndexNames(
    (0, "A3COM-SWITCHING-SYSTEMS-MIB", "a3ComSysSmtFddiMacRateSmtIndex"),
    (0, "A3COM-SWITCHING-SYSTEMS-MIB", "a3ComSysSmtFddiMacRateIndex"),
)
if mibBuilder.loadTexts:
    a3ComSysSmtFddiMacRateEntry.setStatus("mandatory")
_A3ComSysSmtFddiMacRateSmtIndex_Type = Integer32
_A3ComSysSmtFddiMacRateSmtIndex_Object = MibTableColumn
a3ComSysSmtFddiMacRateSmtIndex = _A3ComSysSmtFddiMacRateSmtIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 9, 5, 1, 1),
    _A3ComSysSmtFddiMacRateSmtIndex_Type()
)
a3ComSysSmtFddiMacRateSmtIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysSmtFddiMacRateSmtIndex.setStatus("mandatory")
_A3ComSysSmtFddiMacRateIndex_Type = Integer32
_A3ComSysSmtFddiMacRateIndex_Object = MibTableColumn
a3ComSysSmtFddiMacRateIndex = _A3ComSysSmtFddiMacRateIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 9, 5, 1, 2),
    _A3ComSysSmtFddiMacRateIndex_Type()
)
a3ComSysSmtFddiMacRateIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysSmtFddiMacRateIndex.setStatus("mandatory")
_A3ComSysSmtFddiMacRateByteReceiveRate_Type = Integer32
_A3ComSysSmtFddiMacRateByteReceiveRate_Object = MibTableColumn
a3ComSysSmtFddiMacRateByteReceiveRate = _A3ComSysSmtFddiMacRateByteReceiveRate_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 9, 5, 1, 3),
    _A3ComSysSmtFddiMacRateByteReceiveRate_Type()
)
a3ComSysSmtFddiMacRateByteReceiveRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysSmtFddiMacRateByteReceiveRate.setStatus("mandatory")
_A3ComSysSmtFddiMacRatePeakByteReceiveRate_Type = Integer32
_A3ComSysSmtFddiMacRatePeakByteReceiveRate_Object = MibTableColumn
a3ComSysSmtFddiMacRatePeakByteReceiveRate = _A3ComSysSmtFddiMacRatePeakByteReceiveRate_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 9, 5, 1, 4),
    _A3ComSysSmtFddiMacRatePeakByteReceiveRate_Type()
)
a3ComSysSmtFddiMacRatePeakByteReceiveRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysSmtFddiMacRatePeakByteReceiveRate.setStatus("mandatory")
_A3ComSysSmtFddiMacRateFrameReceiveRate_Type = Integer32
_A3ComSysSmtFddiMacRateFrameReceiveRate_Object = MibTableColumn
a3ComSysSmtFddiMacRateFrameReceiveRate = _A3ComSysSmtFddiMacRateFrameReceiveRate_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 9, 5, 1, 5),
    _A3ComSysSmtFddiMacRateFrameReceiveRate_Type()
)
a3ComSysSmtFddiMacRateFrameReceiveRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysSmtFddiMacRateFrameReceiveRate.setStatus("mandatory")
_A3ComSysSmtFddiMacRatePeakFrameReceiveRate_Type = Integer32
_A3ComSysSmtFddiMacRatePeakFrameReceiveRate_Object = MibTableColumn
a3ComSysSmtFddiMacRatePeakFrameReceiveRate = _A3ComSysSmtFddiMacRatePeakFrameReceiveRate_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 9, 5, 1, 6),
    _A3ComSysSmtFddiMacRatePeakFrameReceiveRate_Type()
)
a3ComSysSmtFddiMacRatePeakFrameReceiveRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysSmtFddiMacRatePeakFrameReceiveRate.setStatus("mandatory")
_A3ComSysSmtFddiMacRateByteTransmitRate_Type = Integer32
_A3ComSysSmtFddiMacRateByteTransmitRate_Object = MibTableColumn
a3ComSysSmtFddiMacRateByteTransmitRate = _A3ComSysSmtFddiMacRateByteTransmitRate_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 9, 5, 1, 7),
    _A3ComSysSmtFddiMacRateByteTransmitRate_Type()
)
a3ComSysSmtFddiMacRateByteTransmitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysSmtFddiMacRateByteTransmitRate.setStatus("mandatory")
_A3ComSysSmtFddiMacRatePeakByteTransmitRate_Type = Integer32
_A3ComSysSmtFddiMacRatePeakByteTransmitRate_Object = MibTableColumn
a3ComSysSmtFddiMacRatePeakByteTransmitRate = _A3ComSysSmtFddiMacRatePeakByteTransmitRate_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 9, 5, 1, 8),
    _A3ComSysSmtFddiMacRatePeakByteTransmitRate_Type()
)
a3ComSysSmtFddiMacRatePeakByteTransmitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysSmtFddiMacRatePeakByteTransmitRate.setStatus("mandatory")
_A3ComSysSmtFddiMacRateFrameTransmitRate_Type = Integer32
_A3ComSysSmtFddiMacRateFrameTransmitRate_Object = MibTableColumn
a3ComSysSmtFddiMacRateFrameTransmitRate = _A3ComSysSmtFddiMacRateFrameTransmitRate_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 9, 5, 1, 9),
    _A3ComSysSmtFddiMacRateFrameTransmitRate_Type()
)
a3ComSysSmtFddiMacRateFrameTransmitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysSmtFddiMacRateFrameTransmitRate.setStatus("mandatory")
_A3ComSysSmtFddiMacRatePeakFrameTransmitRate_Type = Integer32
_A3ComSysSmtFddiMacRatePeakFrameTransmitRate_Object = MibTableColumn
a3ComSysSmtFddiMacRatePeakFrameTransmitRate = _A3ComSysSmtFddiMacRatePeakFrameTransmitRate_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 9, 5, 1, 10),
    _A3ComSysSmtFddiMacRatePeakFrameTransmitRate_Type()
)
a3ComSysSmtFddiMacRatePeakFrameTransmitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysSmtFddiMacRatePeakFrameTransmitRate.setStatus("mandatory")
_A3ComSysSmtFddiPortTable_Object = MibTable
a3ComSysSmtFddiPortTable = _A3ComSysSmtFddiPortTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 9, 6)
)
if mibBuilder.loadTexts:
    a3ComSysSmtFddiPortTable.setStatus("mandatory")
_A3ComSysSmtFddiPortEntry_Object = MibTableRow
a3ComSysSmtFddiPortEntry = _A3ComSysSmtFddiPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 9, 6, 1)
)
a3ComSysSmtFddiPortEntry.setIndexNames(
    (0, "A3COM-SWITCHING-SYSTEMS-MIB", "a3ComSysSmtFddiPortSmtIndex"),
    (0, "A3COM-SWITCHING-SYSTEMS-MIB", "a3ComSysSmtFddiPortIndex"),
)
if mibBuilder.loadTexts:
    a3ComSysSmtFddiPortEntry.setStatus("mandatory")
_A3ComSysSmtFddiPortSmtIndex_Type = Integer32
_A3ComSysSmtFddiPortSmtIndex_Object = MibTableColumn
a3ComSysSmtFddiPortSmtIndex = _A3ComSysSmtFddiPortSmtIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 9, 6, 1, 1),
    _A3ComSysSmtFddiPortSmtIndex_Type()
)
a3ComSysSmtFddiPortSmtIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysSmtFddiPortSmtIndex.setStatus("mandatory")
_A3ComSysSmtFddiPortIndex_Type = Integer32
_A3ComSysSmtFddiPortIndex_Object = MibTableColumn
a3ComSysSmtFddiPortIndex = _A3ComSysSmtFddiPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 9, 6, 1, 2),
    _A3ComSysSmtFddiPortIndex_Type()
)
a3ComSysSmtFddiPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysSmtFddiPortIndex.setStatus("mandatory")


class _A3ComSysSmtFddiPortLocationType_Type(Integer32):
    """Custom type a3ComSysSmtFddiPortLocationType based on Integer32"""
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


_A3ComSysSmtFddiPortLocationType_Type.__name__ = "Integer32"
_A3ComSysSmtFddiPortLocationType_Object = MibTableColumn
a3ComSysSmtFddiPortLocationType = _A3ComSysSmtFddiPortLocationType_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 9, 6, 1, 3),
    _A3ComSysSmtFddiPortLocationType_Type()
)
a3ComSysSmtFddiPortLocationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysSmtFddiPortLocationType.setStatus("mandatory")
_A3ComSysSmtFddiPortLocationTypeIndex_Type = Integer32
_A3ComSysSmtFddiPortLocationTypeIndex_Object = MibTableColumn
a3ComSysSmtFddiPortLocationTypeIndex = _A3ComSysSmtFddiPortLocationTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 9, 6, 1, 4),
    _A3ComSysSmtFddiPortLocationTypeIndex_Type()
)
a3ComSysSmtFddiPortLocationTypeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysSmtFddiPortLocationTypeIndex.setStatus("mandatory")
_A3ComSysSmtFddiPortLocationLocalIndex_Type = Integer32
_A3ComSysSmtFddiPortLocationLocalIndex_Object = MibTableColumn
a3ComSysSmtFddiPortLocationLocalIndex = _A3ComSysSmtFddiPortLocationLocalIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 9, 6, 1, 5),
    _A3ComSysSmtFddiPortLocationLocalIndex_Type()
)
a3ComSysSmtFddiPortLocationLocalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysSmtFddiPortLocationLocalIndex.setStatus("mandatory")


class _A3ComSysSmtFddiPortLabel_Type(DisplayString):
    """Custom type a3ComSysSmtFddiPortLabel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_A3ComSysSmtFddiPortLabel_Type.__name__ = "DisplayString"
_A3ComSysSmtFddiPortLabel_Object = MibTableColumn
a3ComSysSmtFddiPortLabel = _A3ComSysSmtFddiPortLabel_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 9, 6, 1, 6),
    _A3ComSysSmtFddiPortLabel_Type()
)
a3ComSysSmtFddiPortLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComSysSmtFddiPortLabel.setStatus("mandatory")
_A3ComSysSmtFddiMacLocationTable_Object = MibTable
a3ComSysSmtFddiMacLocationTable = _A3ComSysSmtFddiMacLocationTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 9, 7)
)
if mibBuilder.loadTexts:
    a3ComSysSmtFddiMacLocationTable.setStatus("mandatory")
_A3ComSysSmtFddiMacLocationEntry_Object = MibTableRow
a3ComSysSmtFddiMacLocationEntry = _A3ComSysSmtFddiMacLocationEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 9, 7, 1)
)
a3ComSysSmtFddiMacLocationEntry.setIndexNames(
    (0, "A3COM-SWITCHING-SYSTEMS-MIB", "a3ComSysSmtFddiMacLocationSmtIndex"),
    (0, "A3COM-SWITCHING-SYSTEMS-MIB", "a3ComSysSmtFddiMacLocationIndex"),
)
if mibBuilder.loadTexts:
    a3ComSysSmtFddiMacLocationEntry.setStatus("mandatory")
_A3ComSysSmtFddiMacLocationSmtIndex_Type = Integer32
_A3ComSysSmtFddiMacLocationSmtIndex_Object = MibTableColumn
a3ComSysSmtFddiMacLocationSmtIndex = _A3ComSysSmtFddiMacLocationSmtIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 9, 7, 1, 1),
    _A3ComSysSmtFddiMacLocationSmtIndex_Type()
)
a3ComSysSmtFddiMacLocationSmtIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysSmtFddiMacLocationSmtIndex.setStatus("mandatory")
_A3ComSysSmtFddiMacLocationIndex_Type = Integer32
_A3ComSysSmtFddiMacLocationIndex_Object = MibTableColumn
a3ComSysSmtFddiMacLocationIndex = _A3ComSysSmtFddiMacLocationIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 9, 7, 1, 2),
    _A3ComSysSmtFddiMacLocationIndex_Type()
)
a3ComSysSmtFddiMacLocationIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysSmtFddiMacLocationIndex.setStatus("mandatory")


class _A3ComSysSmtFddiMacCurrentLocation_Type(Integer32):
    """Custom type a3ComSysSmtFddiMacCurrentLocation based on Integer32"""
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


_A3ComSysSmtFddiMacCurrentLocation_Type.__name__ = "Integer32"
_A3ComSysSmtFddiMacCurrentLocation_Object = MibTableColumn
a3ComSysSmtFddiMacCurrentLocation = _A3ComSysSmtFddiMacCurrentLocation_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 9, 7, 1, 3),
    _A3ComSysSmtFddiMacCurrentLocation_Type()
)
a3ComSysSmtFddiMacCurrentLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysSmtFddiMacCurrentLocation.setStatus("mandatory")


class _A3ComSysSmtFddiMacRequestedLocation_Type(Integer32):
    """Custom type a3ComSysSmtFddiMacRequestedLocation based on Integer32"""
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


_A3ComSysSmtFddiMacRequestedLocation_Type.__name__ = "Integer32"
_A3ComSysSmtFddiMacRequestedLocation_Object = MibTableColumn
a3ComSysSmtFddiMacRequestedLocation = _A3ComSysSmtFddiMacRequestedLocation_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 9, 7, 1, 4),
    _A3ComSysSmtFddiMacRequestedLocation_Type()
)
a3ComSysSmtFddiMacRequestedLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComSysSmtFddiMacRequestedLocation.setStatus("mandatory")


class _A3ComSysSmtFddiMacAvailableLocation_Type(Integer32):
    """Custom type a3ComSysSmtFddiMacAvailableLocation based on Integer32"""
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


_A3ComSysSmtFddiMacAvailableLocation_Type.__name__ = "Integer32"
_A3ComSysSmtFddiMacAvailableLocation_Object = MibTableColumn
a3ComSysSmtFddiMacAvailableLocation = _A3ComSysSmtFddiMacAvailableLocation_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 9, 7, 1, 5),
    _A3ComSysSmtFddiMacAvailableLocation_Type()
)
a3ComSysSmtFddiMacAvailableLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysSmtFddiMacAvailableLocation.setStatus("mandatory")
_A3ComSysSmtFddiMacStationTable_Object = MibTable
a3ComSysSmtFddiMacStationTable = _A3ComSysSmtFddiMacStationTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 9, 8)
)
if mibBuilder.loadTexts:
    a3ComSysSmtFddiMacStationTable.setStatus("mandatory")
_A3ComSysSmtFddiMacStationEntry_Object = MibTableRow
a3ComSysSmtFddiMacStationEntry = _A3ComSysSmtFddiMacStationEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 9, 8, 1)
)
a3ComSysSmtFddiMacStationEntry.setIndexNames(
    (0, "A3COM-SWITCHING-SYSTEMS-MIB", "a3ComSysSmtFddiMacStationSmtIndex"),
    (0, "A3COM-SWITCHING-SYSTEMS-MIB", "a3ComSysSmtFddiMacStationIndex"),
)
if mibBuilder.loadTexts:
    a3ComSysSmtFddiMacStationEntry.setStatus("mandatory")
_A3ComSysSmtFddiMacStationSmtIndex_Type = Integer32
_A3ComSysSmtFddiMacStationSmtIndex_Object = MibTableColumn
a3ComSysSmtFddiMacStationSmtIndex = _A3ComSysSmtFddiMacStationSmtIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 9, 8, 1, 1),
    _A3ComSysSmtFddiMacStationSmtIndex_Type()
)
a3ComSysSmtFddiMacStationSmtIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysSmtFddiMacStationSmtIndex.setStatus("mandatory")
_A3ComSysSmtFddiMacStationIndex_Type = Integer32
_A3ComSysSmtFddiMacStationIndex_Object = MibTableColumn
a3ComSysSmtFddiMacStationIndex = _A3ComSysSmtFddiMacStationIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 9, 8, 1, 2),
    _A3ComSysSmtFddiMacStationIndex_Type()
)
a3ComSysSmtFddiMacStationIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysSmtFddiMacStationIndex.setStatus("mandatory")
_A3ComSysSmtFddiMacCurrentStation_Type = Integer32
_A3ComSysSmtFddiMacCurrentStation_Object = MibTableColumn
a3ComSysSmtFddiMacCurrentStation = _A3ComSysSmtFddiMacCurrentStation_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 9, 8, 1, 3),
    _A3ComSysSmtFddiMacCurrentStation_Type()
)
a3ComSysSmtFddiMacCurrentStation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysSmtFddiMacCurrentStation.setStatus("mandatory")
_A3ComSysSmtFddiMacRequestedStation_Type = Integer32
_A3ComSysSmtFddiMacRequestedStation_Object = MibTableColumn
a3ComSysSmtFddiMacRequestedStation = _A3ComSysSmtFddiMacRequestedStation_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 9, 8, 1, 4),
    _A3ComSysSmtFddiMacRequestedStation_Type()
)
a3ComSysSmtFddiMacRequestedStation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComSysSmtFddiMacRequestedStation.setStatus("mandatory")
_A3ComSysSmtFddiMacAvailableStations_Type = Integer32
_A3ComSysSmtFddiMacAvailableStations_Object = MibTableColumn
a3ComSysSmtFddiMacAvailableStations = _A3ComSysSmtFddiMacAvailableStations_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 9, 8, 1, 5),
    _A3ComSysSmtFddiMacAvailableStations_Type()
)
a3ComSysSmtFddiMacAvailableStations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysSmtFddiMacAvailableStations.setStatus("mandatory")
_A3ComSysSmtFddiPortStationTable_Object = MibTable
a3ComSysSmtFddiPortStationTable = _A3ComSysSmtFddiPortStationTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 9, 9)
)
if mibBuilder.loadTexts:
    a3ComSysSmtFddiPortStationTable.setStatus("mandatory")
_A3ComSysSmtFddiPortStationEntry_Object = MibTableRow
a3ComSysSmtFddiPortStationEntry = _A3ComSysSmtFddiPortStationEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 9, 9, 1)
)
a3ComSysSmtFddiPortStationEntry.setIndexNames(
    (0, "A3COM-SWITCHING-SYSTEMS-MIB", "a3ComSysSmtFddiPortStationSmtIndex"),
    (0, "A3COM-SWITCHING-SYSTEMS-MIB", "a3ComSysSmtFddiPortStationIndex"),
)
if mibBuilder.loadTexts:
    a3ComSysSmtFddiPortStationEntry.setStatus("mandatory")
_A3ComSysSmtFddiPortStationSmtIndex_Type = Integer32
_A3ComSysSmtFddiPortStationSmtIndex_Object = MibTableColumn
a3ComSysSmtFddiPortStationSmtIndex = _A3ComSysSmtFddiPortStationSmtIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 9, 9, 1, 1),
    _A3ComSysSmtFddiPortStationSmtIndex_Type()
)
a3ComSysSmtFddiPortStationSmtIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysSmtFddiPortStationSmtIndex.setStatus("mandatory")
_A3ComSysSmtFddiPortStationIndex_Type = Integer32
_A3ComSysSmtFddiPortStationIndex_Object = MibTableColumn
a3ComSysSmtFddiPortStationIndex = _A3ComSysSmtFddiPortStationIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 9, 9, 1, 2),
    _A3ComSysSmtFddiPortStationIndex_Type()
)
a3ComSysSmtFddiPortStationIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysSmtFddiPortStationIndex.setStatus("mandatory")
_A3ComSysSmtFddiPortCurrentStation_Type = Integer32
_A3ComSysSmtFddiPortCurrentStation_Object = MibTableColumn
a3ComSysSmtFddiPortCurrentStation = _A3ComSysSmtFddiPortCurrentStation_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 9, 9, 1, 3),
    _A3ComSysSmtFddiPortCurrentStation_Type()
)
a3ComSysSmtFddiPortCurrentStation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysSmtFddiPortCurrentStation.setStatus("mandatory")
_A3ComSysSmtFddiPortRequestedStation_Type = Integer32
_A3ComSysSmtFddiPortRequestedStation_Object = MibTableColumn
a3ComSysSmtFddiPortRequestedStation = _A3ComSysSmtFddiPortRequestedStation_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 9, 9, 1, 4),
    _A3ComSysSmtFddiPortRequestedStation_Type()
)
a3ComSysSmtFddiPortRequestedStation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComSysSmtFddiPortRequestedStation.setStatus("mandatory")
_A3ComSysSmtFddiPortAvailableStations_Type = Integer32
_A3ComSysSmtFddiPortAvailableStations_Object = MibTableColumn
a3ComSysSmtFddiPortAvailableStations = _A3ComSysSmtFddiPortAvailableStations_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 9, 9, 1, 5),
    _A3ComSysSmtFddiPortAvailableStations_Type()
)
a3ComSysSmtFddiPortAvailableStations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysSmtFddiPortAvailableStations.setStatus("mandatory")
_A3ComSysBridge_ObjectIdentity = ObjectIdentity
a3ComSysBridge = _A3ComSysBridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 10)
)
_A3ComSysBridgeCount_Type = Integer32
_A3ComSysBridgeCount_Object = MibScalar
a3ComSysBridgeCount = _A3ComSysBridgeCount_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 10, 1),
    _A3ComSysBridgeCount_Type()
)
a3ComSysBridgeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysBridgeCount.setStatus("mandatory")
_A3ComSysBridgeTable_Object = MibTable
a3ComSysBridgeTable = _A3ComSysBridgeTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 10, 2)
)
if mibBuilder.loadTexts:
    a3ComSysBridgeTable.setStatus("mandatory")
_A3ComSysBridgeEntry_Object = MibTableRow
a3ComSysBridgeEntry = _A3ComSysBridgeEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 10, 2, 1)
)
a3ComSysBridgeEntry.setIndexNames(
    (0, "A3COM-SWITCHING-SYSTEMS-MIB", "a3ComSysBridgeIndex"),
)
if mibBuilder.loadTexts:
    a3ComSysBridgeEntry.setStatus("mandatory")
_A3ComSysBridgeIndex_Type = Integer32
_A3ComSysBridgeIndex_Object = MibTableColumn
a3ComSysBridgeIndex = _A3ComSysBridgeIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 10, 2, 1, 1),
    _A3ComSysBridgeIndex_Type()
)
a3ComSysBridgeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysBridgeIndex.setStatus("mandatory")
_A3ComSysBridgePortCount_Type = Integer32
_A3ComSysBridgePortCount_Object = MibTableColumn
a3ComSysBridgePortCount = _A3ComSysBridgePortCount_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 10, 2, 1, 2),
    _A3ComSysBridgePortCount_Type()
)
a3ComSysBridgePortCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysBridgePortCount.setStatus("mandatory")
_A3ComSysBridgeAddressTableSize_Type = Integer32
_A3ComSysBridgeAddressTableSize_Object = MibTableColumn
a3ComSysBridgeAddressTableSize = _A3ComSysBridgeAddressTableSize_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 10, 2, 1, 3),
    _A3ComSysBridgeAddressTableSize_Type()
)
a3ComSysBridgeAddressTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysBridgeAddressTableSize.setStatus("mandatory")
_A3ComSysBridgeAddressTableCount_Type = Integer32
_A3ComSysBridgeAddressTableCount_Object = MibTableColumn
a3ComSysBridgeAddressTableCount = _A3ComSysBridgeAddressTableCount_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 10, 2, 1, 4),
    _A3ComSysBridgeAddressTableCount_Type()
)
a3ComSysBridgeAddressTableCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysBridgeAddressTableCount.setStatus("mandatory")
_A3ComSysBridgeAddressTablePeakCount_Type = Integer32
_A3ComSysBridgeAddressTablePeakCount_Object = MibTableColumn
a3ComSysBridgeAddressTablePeakCount = _A3ComSysBridgeAddressTablePeakCount_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 10, 2, 1, 5),
    _A3ComSysBridgeAddressTablePeakCount_Type()
)
a3ComSysBridgeAddressTablePeakCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysBridgeAddressTablePeakCount.setStatus("mandatory")
_A3ComSysBridgeAddressThreshold_Type = Integer32
_A3ComSysBridgeAddressThreshold_Object = MibTableColumn
a3ComSysBridgeAddressThreshold = _A3ComSysBridgeAddressThreshold_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 10, 2, 1, 6),
    _A3ComSysBridgeAddressThreshold_Type()
)
a3ComSysBridgeAddressThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComSysBridgeAddressThreshold.setStatus("mandatory")


class _A3ComSysBridgeMode_Type(Integer32):
    """Custom type a3ComSysBridgeMode based on Integer32"""
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


_A3ComSysBridgeMode_Type.__name__ = "Integer32"
_A3ComSysBridgeMode_Object = MibTableColumn
a3ComSysBridgeMode = _A3ComSysBridgeMode_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 10, 2, 1, 7),
    _A3ComSysBridgeMode_Type()
)
a3ComSysBridgeMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComSysBridgeMode.setStatus("mandatory")
_A3ComSysBridgeBackbonePort_Type = Integer32
_A3ComSysBridgeBackbonePort_Object = MibTableColumn
a3ComSysBridgeBackbonePort = _A3ComSysBridgeBackbonePort_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 10, 2, 1, 8),
    _A3ComSysBridgeBackbonePort_Type()
)
a3ComSysBridgeBackbonePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComSysBridgeBackbonePort.setStatus("mandatory")


class _A3ComSysBridgeIpFragmentationEnabled_Type(Integer32):
    """Custom type a3ComSysBridgeIpFragmentationEnabled based on Integer32"""
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


_A3ComSysBridgeIpFragmentationEnabled_Type.__name__ = "Integer32"
_A3ComSysBridgeIpFragmentationEnabled_Object = MibTableColumn
a3ComSysBridgeIpFragmentationEnabled = _A3ComSysBridgeIpFragmentationEnabled_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 10, 2, 1, 9),
    _A3ComSysBridgeIpFragmentationEnabled_Type()
)
a3ComSysBridgeIpFragmentationEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComSysBridgeIpFragmentationEnabled.setStatus("mandatory")


class _A3ComSysBridgeTrFddiTranslationMode_Type(Integer32):
    """Custom type a3ComSysBridgeTrFddiTranslationMode based on Integer32"""
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


_A3ComSysBridgeTrFddiTranslationMode_Type.__name__ = "Integer32"
_A3ComSysBridgeTrFddiTranslationMode_Object = MibTableColumn
a3ComSysBridgeTrFddiTranslationMode = _A3ComSysBridgeTrFddiTranslationMode_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 10, 2, 1, 10),
    _A3ComSysBridgeTrFddiTranslationMode_Type()
)
a3ComSysBridgeTrFddiTranslationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComSysBridgeTrFddiTranslationMode.setStatus("mandatory")


class _A3ComSysBridgeSTPGroupAddress_Type(OctetString):
    """Custom type a3ComSysBridgeSTPGroupAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_A3ComSysBridgeSTPGroupAddress_Type.__name__ = "OctetString"
_A3ComSysBridgeSTPGroupAddress_Object = MibTableColumn
a3ComSysBridgeSTPGroupAddress = _A3ComSysBridgeSTPGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 10, 2, 1, 11),
    _A3ComSysBridgeSTPGroupAddress_Type()
)
a3ComSysBridgeSTPGroupAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComSysBridgeSTPGroupAddress.setStatus("mandatory")


class _A3ComSysBridgeSTPEnable_Type(Integer32):
    """Custom type a3ComSysBridgeSTPEnable based on Integer32"""
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


_A3ComSysBridgeSTPEnable_Type.__name__ = "Integer32"
_A3ComSysBridgeSTPEnable_Object = MibTableColumn
a3ComSysBridgeSTPEnable = _A3ComSysBridgeSTPEnable_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 10, 2, 1, 12),
    _A3ComSysBridgeSTPEnable_Type()
)
a3ComSysBridgeSTPEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComSysBridgeSTPEnable.setStatus("mandatory")


class _A3ComSysBridgeIpxSnapTranslationEnable_Type(Integer32):
    """Custom type a3ComSysBridgeIpxSnapTranslationEnable based on Integer32"""
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


_A3ComSysBridgeIpxSnapTranslationEnable_Type.__name__ = "Integer32"
_A3ComSysBridgeIpxSnapTranslationEnable_Object = MibTableColumn
a3ComSysBridgeIpxSnapTranslationEnable = _A3ComSysBridgeIpxSnapTranslationEnable_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 10, 2, 1, 13),
    _A3ComSysBridgeIpxSnapTranslationEnable_Type()
)
a3ComSysBridgeIpxSnapTranslationEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComSysBridgeIpxSnapTranslationEnable.setStatus("mandatory")


class _A3ComSysBridgeLowLatencyEnable_Type(Integer32):
    """Custom type a3ComSysBridgeLowLatencyEnable based on Integer32"""
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


_A3ComSysBridgeLowLatencyEnable_Type.__name__ = "Integer32"
_A3ComSysBridgeLowLatencyEnable_Object = MibTableColumn
a3ComSysBridgeLowLatencyEnable = _A3ComSysBridgeLowLatencyEnable_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 10, 2, 1, 14),
    _A3ComSysBridgeLowLatencyEnable_Type()
)
a3ComSysBridgeLowLatencyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComSysBridgeLowLatencyEnable.setStatus("mandatory")


class _A3ComSysBridgeVlanMode_Type(Integer32):
    """Custom type a3ComSysBridgeVlanMode based on Integer32"""
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


_A3ComSysBridgeVlanMode_Type.__name__ = "Integer32"
_A3ComSysBridgeVlanMode_Object = MibTableColumn
a3ComSysBridgeVlanMode = _A3ComSysBridgeVlanMode_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 10, 2, 1, 15),
    _A3ComSysBridgeVlanMode_Type()
)
a3ComSysBridgeVlanMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComSysBridgeVlanMode.setStatus("mandatory")
_A3ComSysBridgePortTable_Object = MibTable
a3ComSysBridgePortTable = _A3ComSysBridgePortTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 10, 3)
)
if mibBuilder.loadTexts:
    a3ComSysBridgePortTable.setStatus("mandatory")
_A3ComSysBridgePortEntry_Object = MibTableRow
a3ComSysBridgePortEntry = _A3ComSysBridgePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 10, 3, 1)
)
a3ComSysBridgePortEntry.setIndexNames(
    (0, "A3COM-SWITCHING-SYSTEMS-MIB", "a3ComSysBridgePortBridgeIndex"),
    (0, "A3COM-SWITCHING-SYSTEMS-MIB", "a3ComSysBridgePortIndex"),
)
if mibBuilder.loadTexts:
    a3ComSysBridgePortEntry.setStatus("mandatory")
_A3ComSysBridgePortBridgeIndex_Type = Integer32
_A3ComSysBridgePortBridgeIndex_Object = MibTableColumn
a3ComSysBridgePortBridgeIndex = _A3ComSysBridgePortBridgeIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 10, 3, 1, 1),
    _A3ComSysBridgePortBridgeIndex_Type()
)
a3ComSysBridgePortBridgeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysBridgePortBridgeIndex.setStatus("mandatory")
_A3ComSysBridgePortIndex_Type = Integer32
_A3ComSysBridgePortIndex_Object = MibTableColumn
a3ComSysBridgePortIndex = _A3ComSysBridgePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 10, 3, 1, 2),
    _A3ComSysBridgePortIndex_Type()
)
a3ComSysBridgePortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysBridgePortIndex.setStatus("mandatory")
_A3ComSysBridgePortIfIndex_Type = Integer32
_A3ComSysBridgePortIfIndex_Object = MibTableColumn
a3ComSysBridgePortIfIndex = _A3ComSysBridgePortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 10, 3, 1, 3),
    _A3ComSysBridgePortIfIndex_Type()
)
a3ComSysBridgePortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysBridgePortIfIndex.setStatus("mandatory")


class _A3ComSysBridgePortReceiveMulticastLimit_Type(Integer32):
    """Custom type a3ComSysBridgePortReceiveMulticastLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_A3ComSysBridgePortReceiveMulticastLimit_Type.__name__ = "Integer32"
_A3ComSysBridgePortReceiveMulticastLimit_Object = MibTableColumn
a3ComSysBridgePortReceiveMulticastLimit = _A3ComSysBridgePortReceiveMulticastLimit_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 10, 3, 1, 4),
    _A3ComSysBridgePortReceiveMulticastLimit_Type()
)
a3ComSysBridgePortReceiveMulticastLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComSysBridgePortReceiveMulticastLimit.setStatus("mandatory")


class _A3ComSysBridgePortAddressAction_Type(Integer32):
    """Custom type a3ComSysBridgePortAddressAction based on Integer32"""
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


_A3ComSysBridgePortAddressAction_Type.__name__ = "Integer32"
_A3ComSysBridgePortAddressAction_Object = MibTableColumn
a3ComSysBridgePortAddressAction = _A3ComSysBridgePortAddressAction_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 10, 3, 1, 5),
    _A3ComSysBridgePortAddressAction_Type()
)
a3ComSysBridgePortAddressAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComSysBridgePortAddressAction.setStatus("mandatory")
_A3ComSysBridgePortSpanningTreeFrameReceivedCounts_Type = Counter32
_A3ComSysBridgePortSpanningTreeFrameReceivedCounts_Object = MibTableColumn
a3ComSysBridgePortSpanningTreeFrameReceivedCounts = _A3ComSysBridgePortSpanningTreeFrameReceivedCounts_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 10, 3, 1, 6),
    _A3ComSysBridgePortSpanningTreeFrameReceivedCounts_Type()
)
a3ComSysBridgePortSpanningTreeFrameReceivedCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysBridgePortSpanningTreeFrameReceivedCounts.setStatus("mandatory")
_A3ComSysBridgePortReceiveBlockedDiscards_Type = Counter32
_A3ComSysBridgePortReceiveBlockedDiscards_Object = MibTableColumn
a3ComSysBridgePortReceiveBlockedDiscards = _A3ComSysBridgePortReceiveBlockedDiscards_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 10, 3, 1, 7),
    _A3ComSysBridgePortReceiveBlockedDiscards_Type()
)
a3ComSysBridgePortReceiveBlockedDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysBridgePortReceiveBlockedDiscards.setStatus("mandatory")
_A3ComSysBridgePortReceiveMulticastLimitExceededs_Type = Counter32
_A3ComSysBridgePortReceiveMulticastLimitExceededs_Object = MibTableColumn
a3ComSysBridgePortReceiveMulticastLimitExceededs = _A3ComSysBridgePortReceiveMulticastLimitExceededs_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 10, 3, 1, 8),
    _A3ComSysBridgePortReceiveMulticastLimitExceededs_Type()
)
a3ComSysBridgePortReceiveMulticastLimitExceededs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysBridgePortReceiveMulticastLimitExceededs.setStatus("mandatory")
_A3ComSysBridgePortReceiveMulticastLimitExceededDiscards_Type = Counter32
_A3ComSysBridgePortReceiveMulticastLimitExceededDiscards_Object = MibTableColumn
a3ComSysBridgePortReceiveMulticastLimitExceededDiscards = _A3ComSysBridgePortReceiveMulticastLimitExceededDiscards_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 10, 3, 1, 9),
    _A3ComSysBridgePortReceiveMulticastLimitExceededDiscards_Type()
)
a3ComSysBridgePortReceiveMulticastLimitExceededDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysBridgePortReceiveMulticastLimitExceededDiscards.setStatus("mandatory")
_A3ComSysBridgePortReceiveSecurityDiscards_Type = Counter32
_A3ComSysBridgePortReceiveSecurityDiscards_Object = MibTableColumn
a3ComSysBridgePortReceiveSecurityDiscards = _A3ComSysBridgePortReceiveSecurityDiscards_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 10, 3, 1, 10),
    _A3ComSysBridgePortReceiveSecurityDiscards_Type()
)
a3ComSysBridgePortReceiveSecurityDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysBridgePortReceiveSecurityDiscards.setStatus("mandatory")
_A3ComSysBridgePortReceiveUnknownDiscards_Type = Counter32
_A3ComSysBridgePortReceiveUnknownDiscards_Object = MibTableColumn
a3ComSysBridgePortReceiveUnknownDiscards = _A3ComSysBridgePortReceiveUnknownDiscards_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 10, 3, 1, 11),
    _A3ComSysBridgePortReceiveUnknownDiscards_Type()
)
a3ComSysBridgePortReceiveUnknownDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysBridgePortReceiveUnknownDiscards.setStatus("mandatory")
_A3ComSysBridgePortReceiveOtherDiscards_Type = Counter32
_A3ComSysBridgePortReceiveOtherDiscards_Object = MibTableColumn
a3ComSysBridgePortReceiveOtherDiscards = _A3ComSysBridgePortReceiveOtherDiscards_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 10, 3, 1, 12),
    _A3ComSysBridgePortReceiveOtherDiscards_Type()
)
a3ComSysBridgePortReceiveOtherDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysBridgePortReceiveOtherDiscards.setStatus("mandatory")
_A3ComSysBridgePortReceiveErrorDiscards_Type = Counter32
_A3ComSysBridgePortReceiveErrorDiscards_Object = MibTableColumn
a3ComSysBridgePortReceiveErrorDiscards = _A3ComSysBridgePortReceiveErrorDiscards_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 10, 3, 1, 13),
    _A3ComSysBridgePortReceiveErrorDiscards_Type()
)
a3ComSysBridgePortReceiveErrorDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysBridgePortReceiveErrorDiscards.setStatus("mandatory")
_A3ComSysBridgePortSameSegmentDiscards_Type = Counter32
_A3ComSysBridgePortSameSegmentDiscards_Object = MibTableColumn
a3ComSysBridgePortSameSegmentDiscards = _A3ComSysBridgePortSameSegmentDiscards_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 10, 3, 1, 14),
    _A3ComSysBridgePortSameSegmentDiscards_Type()
)
a3ComSysBridgePortSameSegmentDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysBridgePortSameSegmentDiscards.setStatus("mandatory")
_A3ComSysBridgePortTransmitBlockedDiscards_Type = Counter32
_A3ComSysBridgePortTransmitBlockedDiscards_Object = MibTableColumn
a3ComSysBridgePortTransmitBlockedDiscards = _A3ComSysBridgePortTransmitBlockedDiscards_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 10, 3, 1, 15),
    _A3ComSysBridgePortTransmitBlockedDiscards_Type()
)
a3ComSysBridgePortTransmitBlockedDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysBridgePortTransmitBlockedDiscards.setStatus("mandatory")
_A3ComSysBridgePortReceiveAllPathFilteredFrames_Type = Counter32
_A3ComSysBridgePortReceiveAllPathFilteredFrames_Object = MibTableColumn
a3ComSysBridgePortReceiveAllPathFilteredFrames = _A3ComSysBridgePortReceiveAllPathFilteredFrames_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 10, 3, 1, 16),
    _A3ComSysBridgePortReceiveAllPathFilteredFrames_Type()
)
a3ComSysBridgePortReceiveAllPathFilteredFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysBridgePortReceiveAllPathFilteredFrames.setStatus("mandatory")
_A3ComSysBridgePortReceiveMulticastPathFilteredFrames_Type = Counter32
_A3ComSysBridgePortReceiveMulticastPathFilteredFrames_Object = MibTableColumn
a3ComSysBridgePortReceiveMulticastPathFilteredFrames = _A3ComSysBridgePortReceiveMulticastPathFilteredFrames_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 10, 3, 1, 17),
    _A3ComSysBridgePortReceiveMulticastPathFilteredFrames_Type()
)
a3ComSysBridgePortReceiveMulticastPathFilteredFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysBridgePortReceiveMulticastPathFilteredFrames.setStatus("mandatory")
_A3ComSysBridgePortTransmitAllPathFilteredFrames_Type = Counter32
_A3ComSysBridgePortTransmitAllPathFilteredFrames_Object = MibTableColumn
a3ComSysBridgePortTransmitAllPathFilteredFrames = _A3ComSysBridgePortTransmitAllPathFilteredFrames_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 10, 3, 1, 18),
    _A3ComSysBridgePortTransmitAllPathFilteredFrames_Type()
)
a3ComSysBridgePortTransmitAllPathFilteredFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysBridgePortTransmitAllPathFilteredFrames.setStatus("mandatory")
_A3ComSysBridgePortTransmitMulticastPathFilteredFrames_Type = Counter32
_A3ComSysBridgePortTransmitMulticastPathFilteredFrames_Object = MibTableColumn
a3ComSysBridgePortTransmitMulticastPathFilteredFrames = _A3ComSysBridgePortTransmitMulticastPathFilteredFrames_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 10, 3, 1, 19),
    _A3ComSysBridgePortTransmitMulticastPathFilteredFrames_Type()
)
a3ComSysBridgePortTransmitMulticastPathFilteredFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysBridgePortTransmitMulticastPathFilteredFrames.setStatus("mandatory")
_A3ComSysBridgePortForwardedUnicastFrames_Type = Counter32
_A3ComSysBridgePortForwardedUnicastFrames_Object = MibTableColumn
a3ComSysBridgePortForwardedUnicastFrames = _A3ComSysBridgePortForwardedUnicastFrames_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 10, 3, 1, 20),
    _A3ComSysBridgePortForwardedUnicastFrames_Type()
)
a3ComSysBridgePortForwardedUnicastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysBridgePortForwardedUnicastFrames.setStatus("mandatory")
_A3ComSysBridgePortForwardedUnicastOctets_Type = Counter32
_A3ComSysBridgePortForwardedUnicastOctets_Object = MibTableColumn
a3ComSysBridgePortForwardedUnicastOctets = _A3ComSysBridgePortForwardedUnicastOctets_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 10, 3, 1, 21),
    _A3ComSysBridgePortForwardedUnicastOctets_Type()
)
a3ComSysBridgePortForwardedUnicastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysBridgePortForwardedUnicastOctets.setStatus("mandatory")
_A3ComSysBridgePortForwardedMulticastFrames_Type = Counter32
_A3ComSysBridgePortForwardedMulticastFrames_Object = MibTableColumn
a3ComSysBridgePortForwardedMulticastFrames = _A3ComSysBridgePortForwardedMulticastFrames_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 10, 3, 1, 22),
    _A3ComSysBridgePortForwardedMulticastFrames_Type()
)
a3ComSysBridgePortForwardedMulticastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysBridgePortForwardedMulticastFrames.setStatus("mandatory")
_A3ComSysBridgePortForwardedMulticastOctets_Type = Counter32
_A3ComSysBridgePortForwardedMulticastOctets_Object = MibTableColumn
a3ComSysBridgePortForwardedMulticastOctets = _A3ComSysBridgePortForwardedMulticastOctets_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 10, 3, 1, 23),
    _A3ComSysBridgePortForwardedMulticastOctets_Type()
)
a3ComSysBridgePortForwardedMulticastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysBridgePortForwardedMulticastOctets.setStatus("mandatory")
_A3ComSysBridgePortFloodedUnicastFrames_Type = Counter32
_A3ComSysBridgePortFloodedUnicastFrames_Object = MibTableColumn
a3ComSysBridgePortFloodedUnicastFrames = _A3ComSysBridgePortFloodedUnicastFrames_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 10, 3, 1, 24),
    _A3ComSysBridgePortFloodedUnicastFrames_Type()
)
a3ComSysBridgePortFloodedUnicastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysBridgePortFloodedUnicastFrames.setStatus("mandatory")
_A3ComSysBridgePortFloodedUnicastOctets_Type = Counter32
_A3ComSysBridgePortFloodedUnicastOctets_Object = MibTableColumn
a3ComSysBridgePortFloodedUnicastOctets = _A3ComSysBridgePortFloodedUnicastOctets_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 10, 3, 1, 25),
    _A3ComSysBridgePortFloodedUnicastOctets_Type()
)
a3ComSysBridgePortFloodedUnicastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysBridgePortFloodedUnicastOctets.setStatus("mandatory")


class _A3ComSysBridgePortStpMode_Type(Integer32):
    """Custom type a3ComSysBridgePortStpMode based on Integer32"""
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


_A3ComSysBridgePortStpMode_Type.__name__ = "Integer32"
_A3ComSysBridgePortStpMode_Object = MibTableColumn
a3ComSysBridgePortStpMode = _A3ComSysBridgePortStpMode_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 10, 3, 1, 26),
    _A3ComSysBridgePortStpMode_Type()
)
a3ComSysBridgePortStpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComSysBridgePortStpMode.setStatus("mandatory")


class _A3ComSysBridgePortReceiveMulticastLimitFrameType_Type(Integer32):
    """Custom type a3ComSysBridgePortReceiveMulticastLimitFrameType based on Integer32"""
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


_A3ComSysBridgePortReceiveMulticastLimitFrameType_Type.__name__ = "Integer32"
_A3ComSysBridgePortReceiveMulticastLimitFrameType_Object = MibTableColumn
a3ComSysBridgePortReceiveMulticastLimitFrameType = _A3ComSysBridgePortReceiveMulticastLimitFrameType_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 10, 3, 1, 27),
    _A3ComSysBridgePortReceiveMulticastLimitFrameType_Type()
)
a3ComSysBridgePortReceiveMulticastLimitFrameType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComSysBridgePortReceiveMulticastLimitFrameType.setStatus("mandatory")
_A3ComSysBridgePortForwardedFrames_Type = Counter32
_A3ComSysBridgePortForwardedFrames_Object = MibTableColumn
a3ComSysBridgePortForwardedFrames = _A3ComSysBridgePortForwardedFrames_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 10, 3, 1, 28),
    _A3ComSysBridgePortForwardedFrames_Type()
)
a3ComSysBridgePortForwardedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysBridgePortForwardedFrames.setStatus("mandatory")
_A3ComSysBridgePortReceiveMulticastLimitMultiplier_Type = Integer32
_A3ComSysBridgePortReceiveMulticastLimitMultiplier_Object = MibTableColumn
a3ComSysBridgePortReceiveMulticastLimitMultiplier = _A3ComSysBridgePortReceiveMulticastLimitMultiplier_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 10, 3, 1, 29),
    _A3ComSysBridgePortReceiveMulticastLimitMultiplier_Type()
)
a3ComSysBridgePortReceiveMulticastLimitMultiplier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysBridgePortReceiveMulticastLimitMultiplier.setStatus("mandatory")
_A3ComSysBridgePortAddressTable_Object = MibTable
a3ComSysBridgePortAddressTable = _A3ComSysBridgePortAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 10, 5)
)
if mibBuilder.loadTexts:
    a3ComSysBridgePortAddressTable.setStatus("mandatory")
_A3ComSysBridgePortAddressEntry_Object = MibTableRow
a3ComSysBridgePortAddressEntry = _A3ComSysBridgePortAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 10, 5, 1)
)
a3ComSysBridgePortAddressEntry.setIndexNames(
    (0, "A3COM-SWITCHING-SYSTEMS-MIB", "a3ComSysBridgePortAddressBridgeIndex"),
    (0, "A3COM-SWITCHING-SYSTEMS-MIB", "a3ComSysBridgePortAddressPortIndex"),
    (0, "A3COM-SWITCHING-SYSTEMS-MIB", "a3ComSysBridgePortAddressIndex"),
)
if mibBuilder.loadTexts:
    a3ComSysBridgePortAddressEntry.setStatus("mandatory")
_A3ComSysBridgePortAddressBridgeIndex_Type = Integer32
_A3ComSysBridgePortAddressBridgeIndex_Object = MibTableColumn
a3ComSysBridgePortAddressBridgeIndex = _A3ComSysBridgePortAddressBridgeIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 10, 5, 1, 1),
    _A3ComSysBridgePortAddressBridgeIndex_Type()
)
a3ComSysBridgePortAddressBridgeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysBridgePortAddressBridgeIndex.setStatus("mandatory")
_A3ComSysBridgePortAddressPortIndex_Type = Integer32
_A3ComSysBridgePortAddressPortIndex_Object = MibTableColumn
a3ComSysBridgePortAddressPortIndex = _A3ComSysBridgePortAddressPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 10, 5, 1, 2),
    _A3ComSysBridgePortAddressPortIndex_Type()
)
a3ComSysBridgePortAddressPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysBridgePortAddressPortIndex.setStatus("mandatory")
_A3ComSysBridgePortAddressIndex_Type = Integer32
_A3ComSysBridgePortAddressIndex_Object = MibTableColumn
a3ComSysBridgePortAddressIndex = _A3ComSysBridgePortAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 10, 5, 1, 3),
    _A3ComSysBridgePortAddressIndex_Type()
)
a3ComSysBridgePortAddressIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysBridgePortAddressIndex.setStatus("mandatory")


class _A3ComSysBridgePortAddressRemoteAddress_Type(OctetString):
    """Custom type a3ComSysBridgePortAddressRemoteAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_A3ComSysBridgePortAddressRemoteAddress_Type.__name__ = "OctetString"
_A3ComSysBridgePortAddressRemoteAddress_Object = MibTableColumn
a3ComSysBridgePortAddressRemoteAddress = _A3ComSysBridgePortAddressRemoteAddress_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 10, 5, 1, 4),
    _A3ComSysBridgePortAddressRemoteAddress_Type()
)
a3ComSysBridgePortAddressRemoteAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComSysBridgePortAddressRemoteAddress.setStatus("mandatory")


class _A3ComSysBridgePortAddressType_Type(Integer32):
    """Custom type a3ComSysBridgePortAddressType based on Integer32"""
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


_A3ComSysBridgePortAddressType_Type.__name__ = "Integer32"
_A3ComSysBridgePortAddressType_Object = MibTableColumn
a3ComSysBridgePortAddressType = _A3ComSysBridgePortAddressType_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 10, 5, 1, 5),
    _A3ComSysBridgePortAddressType_Type()
)
a3ComSysBridgePortAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComSysBridgePortAddressType.setStatus("mandatory")


class _A3ComSysBridgePortAddressIsStatic_Type(Integer32):
    """Custom type a3ComSysBridgePortAddressIsStatic based on Integer32"""
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


_A3ComSysBridgePortAddressIsStatic_Type.__name__ = "Integer32"
_A3ComSysBridgePortAddressIsStatic_Object = MibTableColumn
a3ComSysBridgePortAddressIsStatic = _A3ComSysBridgePortAddressIsStatic_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 10, 5, 1, 6),
    _A3ComSysBridgePortAddressIsStatic_Type()
)
a3ComSysBridgePortAddressIsStatic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComSysBridgePortAddressIsStatic.setStatus("mandatory")
_A3ComSysBridgePortAddressStaticPort_Type = Integer32
_A3ComSysBridgePortAddressStaticPort_Object = MibTableColumn
a3ComSysBridgePortAddressStaticPort = _A3ComSysBridgePortAddressStaticPort_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 10, 5, 1, 7),
    _A3ComSysBridgePortAddressStaticPort_Type()
)
a3ComSysBridgePortAddressStaticPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysBridgePortAddressStaticPort.setStatus("mandatory")
_A3ComSysBridgePortAddressAge_Type = Integer32
_A3ComSysBridgePortAddressAge_Object = MibTableColumn
a3ComSysBridgePortAddressAge = _A3ComSysBridgePortAddressAge_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 10, 5, 1, 8),
    _A3ComSysBridgePortAddressAge_Type()
)
a3ComSysBridgePortAddressAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysBridgePortAddressAge.setStatus("mandatory")


class _A3ComSysBridgeStpGroupAddress_Type(OctetString):
    """Custom type a3ComSysBridgeStpGroupAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_A3ComSysBridgeStpGroupAddress_Type.__name__ = "OctetString"
_A3ComSysBridgeStpGroupAddress_Object = MibScalar
a3ComSysBridgeStpGroupAddress = _A3ComSysBridgeStpGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 10, 6),
    _A3ComSysBridgeStpGroupAddress_Type()
)
a3ComSysBridgeStpGroupAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComSysBridgeStpGroupAddress.setStatus("obsolete")


class _A3ComSysBridgeStpEnable_Type(Integer32):
    """Custom type a3ComSysBridgeStpEnable based on Integer32"""
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


_A3ComSysBridgeStpEnable_Type.__name__ = "Integer32"
_A3ComSysBridgeStpEnable_Object = MibScalar
a3ComSysBridgeStpEnable = _A3ComSysBridgeStpEnable_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 10, 7),
    _A3ComSysBridgeStpEnable_Type()
)
a3ComSysBridgeStpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComSysBridgeStpEnable.setStatus("obsolete")
_A3ComSysIpRouter_ObjectIdentity = ObjectIdentity
a3ComSysIpRouter = _A3ComSysIpRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 11)
)
_A3ComSysNetworkMonitor_ObjectIdentity = ObjectIdentity
a3ComSysNetworkMonitor = _A3ComSysNetworkMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 12)
)
_A3ComSysNetworkAnalyzerTable_Object = MibTable
a3ComSysNetworkAnalyzerTable = _A3ComSysNetworkAnalyzerTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 12, 1)
)
if mibBuilder.loadTexts:
    a3ComSysNetworkAnalyzerTable.setStatus("mandatory")
_A3ComSysNetworkAnalyzerTableEntry_Object = MibTableRow
a3ComSysNetworkAnalyzerTableEntry = _A3ComSysNetworkAnalyzerTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 12, 1, 1)
)
a3ComSysNetworkAnalyzerTableEntry.setIndexNames(
    (0, "A3COM-SWITCHING-SYSTEMS-MIB", "a3ComSysNetworkAnalyzerBridgeIndex"),
    (0, "A3COM-SWITCHING-SYSTEMS-MIB", "a3ComSysNetworkAnalyzerBridgePortIndex"),
)
if mibBuilder.loadTexts:
    a3ComSysNetworkAnalyzerTableEntry.setStatus("mandatory")
_A3ComSysNetworkAnalyzerBridgeIndex_Type = Integer32
_A3ComSysNetworkAnalyzerBridgeIndex_Object = MibTableColumn
a3ComSysNetworkAnalyzerBridgeIndex = _A3ComSysNetworkAnalyzerBridgeIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 12, 1, 1, 1),
    _A3ComSysNetworkAnalyzerBridgeIndex_Type()
)
a3ComSysNetworkAnalyzerBridgeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysNetworkAnalyzerBridgeIndex.setStatus("mandatory")
_A3ComSysNetworkAnalyzerBridgePortIndex_Type = Integer32
_A3ComSysNetworkAnalyzerBridgePortIndex_Object = MibTableColumn
a3ComSysNetworkAnalyzerBridgePortIndex = _A3ComSysNetworkAnalyzerBridgePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 12, 1, 1, 2),
    _A3ComSysNetworkAnalyzerBridgePortIndex_Type()
)
a3ComSysNetworkAnalyzerBridgePortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysNetworkAnalyzerBridgePortIndex.setStatus("mandatory")


class _A3ComSysNetworkAnalyzerPhysicalAddress_Type(OctetString):
    """Custom type a3ComSysNetworkAnalyzerPhysicalAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_A3ComSysNetworkAnalyzerPhysicalAddress_Type.__name__ = "OctetString"
_A3ComSysNetworkAnalyzerPhysicalAddress_Object = MibTableColumn
a3ComSysNetworkAnalyzerPhysicalAddress = _A3ComSysNetworkAnalyzerPhysicalAddress_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 12, 1, 1, 3),
    _A3ComSysNetworkAnalyzerPhysicalAddress_Type()
)
a3ComSysNetworkAnalyzerPhysicalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysNetworkAnalyzerPhysicalAddress.setStatus("mandatory")


class _A3ComSysNetworkAnalyzerStatus_Type(Integer32):
    """Custom type a3ComSysNetworkAnalyzerStatus based on Integer32"""
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


_A3ComSysNetworkAnalyzerStatus_Type.__name__ = "Integer32"
_A3ComSysNetworkAnalyzerStatus_Object = MibTableColumn
a3ComSysNetworkAnalyzerStatus = _A3ComSysNetworkAnalyzerStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 12, 1, 1, 4),
    _A3ComSysNetworkAnalyzerStatus_Type()
)
a3ComSysNetworkAnalyzerStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComSysNetworkAnalyzerStatus.setStatus("mandatory")
_A3ComSysNetworkPortMonitorTable_Object = MibTable
a3ComSysNetworkPortMonitorTable = _A3ComSysNetworkPortMonitorTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 12, 2)
)
if mibBuilder.loadTexts:
    a3ComSysNetworkPortMonitorTable.setStatus("mandatory")
_A3ComSysNetworkPortMonitorTableEntry_Object = MibTableRow
a3ComSysNetworkPortMonitorTableEntry = _A3ComSysNetworkPortMonitorTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 12, 2, 1)
)
a3ComSysNetworkPortMonitorTableEntry.setIndexNames(
    (0, "A3COM-SWITCHING-SYSTEMS-MIB", "a3ComSysNetworkPortMonitorBridgeIndex"),
    (0, "A3COM-SWITCHING-SYSTEMS-MIB", "a3ComSysNetworkPortMonitorBridgePortIndex"),
)
if mibBuilder.loadTexts:
    a3ComSysNetworkPortMonitorTableEntry.setStatus("mandatory")
_A3ComSysNetworkPortMonitorBridgeIndex_Type = Integer32
_A3ComSysNetworkPortMonitorBridgeIndex_Object = MibTableColumn
a3ComSysNetworkPortMonitorBridgeIndex = _A3ComSysNetworkPortMonitorBridgeIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 12, 2, 1, 1),
    _A3ComSysNetworkPortMonitorBridgeIndex_Type()
)
a3ComSysNetworkPortMonitorBridgeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysNetworkPortMonitorBridgeIndex.setStatus("mandatory")
_A3ComSysNetworkPortMonitorBridgePortIndex_Type = Integer32
_A3ComSysNetworkPortMonitorBridgePortIndex_Object = MibTableColumn
a3ComSysNetworkPortMonitorBridgePortIndex = _A3ComSysNetworkPortMonitorBridgePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 12, 2, 1, 2),
    _A3ComSysNetworkPortMonitorBridgePortIndex_Type()
)
a3ComSysNetworkPortMonitorBridgePortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysNetworkPortMonitorBridgePortIndex.setStatus("mandatory")


class _A3ComSysNetworkPortMonitorAnalyzerAddress_Type(OctetString):
    """Custom type a3ComSysNetworkPortMonitorAnalyzerAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_A3ComSysNetworkPortMonitorAnalyzerAddress_Type.__name__ = "OctetString"
_A3ComSysNetworkPortMonitorAnalyzerAddress_Object = MibTableColumn
a3ComSysNetworkPortMonitorAnalyzerAddress = _A3ComSysNetworkPortMonitorAnalyzerAddress_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 12, 2, 1, 3),
    _A3ComSysNetworkPortMonitorAnalyzerAddress_Type()
)
a3ComSysNetworkPortMonitorAnalyzerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComSysNetworkPortMonitorAnalyzerAddress.setStatus("mandatory")


class _A3ComSysNetworkPortMonitorStatus_Type(Integer32):
    """Custom type a3ComSysNetworkPortMonitorStatus based on Integer32"""
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


_A3ComSysNetworkPortMonitorStatus_Type.__name__ = "Integer32"
_A3ComSysNetworkPortMonitorStatus_Object = MibTableColumn
a3ComSysNetworkPortMonitorStatus = _A3ComSysNetworkPortMonitorStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 12, 2, 1, 4),
    _A3ComSysNetworkPortMonitorStatus_Type()
)
a3ComSysNetworkPortMonitorStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComSysNetworkPortMonitorStatus.setStatus("mandatory")
_A3ComSysTokenRingPort_ObjectIdentity = ObjectIdentity
a3ComSysTokenRingPort = _A3ComSysTokenRingPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 13)
)
_A3ComSysTokenRingPortCount_Type = Integer32
_A3ComSysTokenRingPortCount_Object = MibScalar
a3ComSysTokenRingPortCount = _A3ComSysTokenRingPortCount_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 13, 1),
    _A3ComSysTokenRingPortCount_Type()
)
a3ComSysTokenRingPortCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysTokenRingPortCount.setStatus("mandatory")
_A3ComSysTokenRingPortTable_Object = MibTable
a3ComSysTokenRingPortTable = _A3ComSysTokenRingPortTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 13, 2)
)
if mibBuilder.loadTexts:
    a3ComSysTokenRingPortTable.setStatus("mandatory")
_A3ComSysTokenRingPortEntry_Object = MibTableRow
a3ComSysTokenRingPortEntry = _A3ComSysTokenRingPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 13, 2, 1)
)
a3ComSysTokenRingPortEntry.setIndexNames(
    (0, "A3COM-SWITCHING-SYSTEMS-MIB", "a3ComSysTokenRingPortIndex"),
)
if mibBuilder.loadTexts:
    a3ComSysTokenRingPortEntry.setStatus("mandatory")
_A3ComSysTokenRingPortIndex_Type = Integer32
_A3ComSysTokenRingPortIndex_Object = MibTableColumn
a3ComSysTokenRingPortIndex = _A3ComSysTokenRingPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 13, 2, 1, 1),
    _A3ComSysTokenRingPortIndex_Type()
)
a3ComSysTokenRingPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysTokenRingPortIndex.setStatus("mandatory")
_A3ComSysTokenRingPortIfIndex_Type = Integer32
_A3ComSysTokenRingPortIfIndex_Object = MibTableColumn
a3ComSysTokenRingPortIfIndex = _A3ComSysTokenRingPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 13, 2, 1, 2),
    _A3ComSysTokenRingPortIfIndex_Type()
)
a3ComSysTokenRingPortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysTokenRingPortIfIndex.setStatus("mandatory")


class _A3ComSysTokenRingPortLabel_Type(DisplayString):
    """Custom type a3ComSysTokenRingPortLabel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_A3ComSysTokenRingPortLabel_Type.__name__ = "DisplayString"
_A3ComSysTokenRingPortLabel_Object = MibTableColumn
a3ComSysTokenRingPortLabel = _A3ComSysTokenRingPortLabel_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 13, 2, 1, 3),
    _A3ComSysTokenRingPortLabel_Type()
)
a3ComSysTokenRingPortLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComSysTokenRingPortLabel.setStatus("mandatory")


class _A3ComSysTokenRingPortInsertStatus_Type(Integer32):
    """Custom type a3ComSysTokenRingPortInsertStatus based on Integer32"""
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


_A3ComSysTokenRingPortInsertStatus_Type.__name__ = "Integer32"
_A3ComSysTokenRingPortInsertStatus_Object = MibTableColumn
a3ComSysTokenRingPortInsertStatus = _A3ComSysTokenRingPortInsertStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 13, 2, 1, 4),
    _A3ComSysTokenRingPortInsertStatus_Type()
)
a3ComSysTokenRingPortInsertStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysTokenRingPortInsertStatus.setStatus("mandatory")


class _A3ComSysTokenRingPortType_Type(Integer32):
    """Custom type a3ComSysTokenRingPortType based on Integer32"""
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


_A3ComSysTokenRingPortType_Type.__name__ = "Integer32"
_A3ComSysTokenRingPortType_Object = MibTableColumn
a3ComSysTokenRingPortType = _A3ComSysTokenRingPortType_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 13, 2, 1, 5),
    _A3ComSysTokenRingPortType_Type()
)
a3ComSysTokenRingPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysTokenRingPortType.setStatus("mandatory")


class _A3ComSysTokenRingPortMode_Type(Integer32):
    """Custom type a3ComSysTokenRingPortMode based on Integer32"""
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


_A3ComSysTokenRingPortMode_Type.__name__ = "Integer32"
_A3ComSysTokenRingPortMode_Object = MibTableColumn
a3ComSysTokenRingPortMode = _A3ComSysTokenRingPortMode_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 13, 2, 1, 6),
    _A3ComSysTokenRingPortMode_Type()
)
a3ComSysTokenRingPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComSysTokenRingPortMode.setStatus("mandatory")


class _A3ComSysTokenRingPortSpeed_Type(Integer32):
    """Custom type a3ComSysTokenRingPortSpeed based on Integer32"""
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


_A3ComSysTokenRingPortSpeed_Type.__name__ = "Integer32"
_A3ComSysTokenRingPortSpeed_Object = MibTableColumn
a3ComSysTokenRingPortSpeed = _A3ComSysTokenRingPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 13, 2, 1, 7),
    _A3ComSysTokenRingPortSpeed_Type()
)
a3ComSysTokenRingPortSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComSysTokenRingPortSpeed.setStatus("mandatory")
_A3ComSysTokenRingPortLineErrors_Type = Counter32
_A3ComSysTokenRingPortLineErrors_Object = MibTableColumn
a3ComSysTokenRingPortLineErrors = _A3ComSysTokenRingPortLineErrors_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 13, 2, 1, 8),
    _A3ComSysTokenRingPortLineErrors_Type()
)
a3ComSysTokenRingPortLineErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysTokenRingPortLineErrors.setStatus("mandatory")
_A3ComSysTokenRingPortBurstErrors_Type = Counter32
_A3ComSysTokenRingPortBurstErrors_Object = MibTableColumn
a3ComSysTokenRingPortBurstErrors = _A3ComSysTokenRingPortBurstErrors_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 13, 2, 1, 9),
    _A3ComSysTokenRingPortBurstErrors_Type()
)
a3ComSysTokenRingPortBurstErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysTokenRingPortBurstErrors.setStatus("mandatory")
_A3ComSysTokenRingPortACErrors_Type = Counter32
_A3ComSysTokenRingPortACErrors_Object = MibTableColumn
a3ComSysTokenRingPortACErrors = _A3ComSysTokenRingPortACErrors_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 13, 2, 1, 10),
    _A3ComSysTokenRingPortACErrors_Type()
)
a3ComSysTokenRingPortACErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysTokenRingPortACErrors.setStatus("mandatory")
_A3ComSysTokenRingPortAbortTransErrors_Type = Counter32
_A3ComSysTokenRingPortAbortTransErrors_Object = MibTableColumn
a3ComSysTokenRingPortAbortTransErrors = _A3ComSysTokenRingPortAbortTransErrors_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 13, 2, 1, 11),
    _A3ComSysTokenRingPortAbortTransErrors_Type()
)
a3ComSysTokenRingPortAbortTransErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysTokenRingPortAbortTransErrors.setStatus("mandatory")
_A3ComSysTokenRingPortInternalErrors_Type = Counter32
_A3ComSysTokenRingPortInternalErrors_Object = MibTableColumn
a3ComSysTokenRingPortInternalErrors = _A3ComSysTokenRingPortInternalErrors_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 13, 2, 1, 12),
    _A3ComSysTokenRingPortInternalErrors_Type()
)
a3ComSysTokenRingPortInternalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysTokenRingPortInternalErrors.setStatus("mandatory")
_A3ComSysTokenRingPortLostFrameErrors_Type = Counter32
_A3ComSysTokenRingPortLostFrameErrors_Object = MibTableColumn
a3ComSysTokenRingPortLostFrameErrors = _A3ComSysTokenRingPortLostFrameErrors_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 13, 2, 1, 13),
    _A3ComSysTokenRingPortLostFrameErrors_Type()
)
a3ComSysTokenRingPortLostFrameErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysTokenRingPortLostFrameErrors.setStatus("mandatory")
_A3ComSysTokenRingPortReceiveCongestionErrors_Type = Counter32
_A3ComSysTokenRingPortReceiveCongestionErrors_Object = MibTableColumn
a3ComSysTokenRingPortReceiveCongestionErrors = _A3ComSysTokenRingPortReceiveCongestionErrors_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 13, 2, 1, 14),
    _A3ComSysTokenRingPortReceiveCongestionErrors_Type()
)
a3ComSysTokenRingPortReceiveCongestionErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysTokenRingPortReceiveCongestionErrors.setStatus("mandatory")
_A3ComSysTokenRingPortFrameCopiedErrors_Type = Counter32
_A3ComSysTokenRingPortFrameCopiedErrors_Object = MibTableColumn
a3ComSysTokenRingPortFrameCopiedErrors = _A3ComSysTokenRingPortFrameCopiedErrors_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 13, 2, 1, 15),
    _A3ComSysTokenRingPortFrameCopiedErrors_Type()
)
a3ComSysTokenRingPortFrameCopiedErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysTokenRingPortFrameCopiedErrors.setStatus("mandatory")
_A3ComSysTokenRingPortTokenErrors_Type = Counter32
_A3ComSysTokenRingPortTokenErrors_Object = MibTableColumn
a3ComSysTokenRingPortTokenErrors = _A3ComSysTokenRingPortTokenErrors_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 13, 2, 1, 16),
    _A3ComSysTokenRingPortTokenErrors_Type()
)
a3ComSysTokenRingPortTokenErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysTokenRingPortTokenErrors.setStatus("mandatory")
_A3ComSysTokenRingPortSoftErrors_Type = Counter32
_A3ComSysTokenRingPortSoftErrors_Object = MibTableColumn
a3ComSysTokenRingPortSoftErrors = _A3ComSysTokenRingPortSoftErrors_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 13, 2, 1, 17),
    _A3ComSysTokenRingPortSoftErrors_Type()
)
a3ComSysTokenRingPortSoftErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysTokenRingPortSoftErrors.setStatus("mandatory")
_A3ComSysTokenRingPortHardErrors_Type = Counter32
_A3ComSysTokenRingPortHardErrors_Object = MibTableColumn
a3ComSysTokenRingPortHardErrors = _A3ComSysTokenRingPortHardErrors_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 13, 2, 1, 18),
    _A3ComSysTokenRingPortHardErrors_Type()
)
a3ComSysTokenRingPortHardErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysTokenRingPortHardErrors.setStatus("mandatory")
_A3ComSysTokenRingPortTransmitBeacons_Type = Counter32
_A3ComSysTokenRingPortTransmitBeacons_Object = MibTableColumn
a3ComSysTokenRingPortTransmitBeacons = _A3ComSysTokenRingPortTransmitBeacons_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 13, 2, 1, 19),
    _A3ComSysTokenRingPortTransmitBeacons_Type()
)
a3ComSysTokenRingPortTransmitBeacons.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysTokenRingPortTransmitBeacons.setStatus("mandatory")
_A3ComSysTokenRingPortLobeWires_Type = Counter32
_A3ComSysTokenRingPortLobeWires_Object = MibTableColumn
a3ComSysTokenRingPortLobeWires = _A3ComSysTokenRingPortLobeWires_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 13, 2, 1, 20),
    _A3ComSysTokenRingPortLobeWires_Type()
)
a3ComSysTokenRingPortLobeWires.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysTokenRingPortLobeWires.setStatus("mandatory")
_A3ComSysTokenRingPortRemoves_Type = Counter32
_A3ComSysTokenRingPortRemoves_Object = MibTableColumn
a3ComSysTokenRingPortRemoves = _A3ComSysTokenRingPortRemoves_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 13, 2, 1, 21),
    _A3ComSysTokenRingPortRemoves_Type()
)
a3ComSysTokenRingPortRemoves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysTokenRingPortRemoves.setStatus("mandatory")
_A3ComSysTokenRingPortSingles_Type = Counter32
_A3ComSysTokenRingPortSingles_Object = MibTableColumn
a3ComSysTokenRingPortSingles = _A3ComSysTokenRingPortSingles_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 13, 2, 1, 22),
    _A3ComSysTokenRingPortSingles_Type()
)
a3ComSysTokenRingPortSingles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysTokenRingPortSingles.setStatus("mandatory")
_A3ComSysTokenRingPortFreqErrors_Type = Counter32
_A3ComSysTokenRingPortFreqErrors_Object = MibTableColumn
a3ComSysTokenRingPortFreqErrors = _A3ComSysTokenRingPortFreqErrors_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 13, 2, 1, 23),
    _A3ComSysTokenRingPortFreqErrors_Type()
)
a3ComSysTokenRingPortFreqErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysTokenRingPortFreqErrors.setStatus("optional")
_A3ComSysTokenRingPortRingStatus_Type = Integer32
_A3ComSysTokenRingPortRingStatus_Object = MibTableColumn
a3ComSysTokenRingPortRingStatus = _A3ComSysTokenRingPortRingStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 13, 2, 1, 24),
    _A3ComSysTokenRingPortRingStatus_Type()
)
a3ComSysTokenRingPortRingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysTokenRingPortRingStatus.setStatus("mandatory")
_A3ComSysFtGroup_ObjectIdentity = ObjectIdentity
a3ComSysFtGroup = _A3ComSysFtGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 14)
)
_A3ComSysFtTable_Object = MibTable
a3ComSysFtTable = _A3ComSysFtTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 14, 1)
)
if mibBuilder.loadTexts:
    a3ComSysFtTable.setStatus("mandatory")
_A3ComSysFtTableEntry_Object = MibTableRow
a3ComSysFtTableEntry = _A3ComSysFtTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 14, 1, 1)
)
a3ComSysFtTableEntry.setIndexNames(
    (0, "A3COM-SWITCHING-SYSTEMS-MIB", "a3ComSysFtIndex"),
)
if mibBuilder.loadTexts:
    a3ComSysFtTableEntry.setStatus("mandatory")


class _A3ComSysFtIndex_Type(Integer32):
    """Custom type a3ComSysFtIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_A3ComSysFtIndex_Type.__name__ = "Integer32"
_A3ComSysFtIndex_Object = MibTableColumn
a3ComSysFtIndex = _A3ComSysFtIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 14, 1, 1, 1),
    _A3ComSysFtIndex_Type()
)
a3ComSysFtIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysFtIndex.setStatus("mandatory")


class _A3ComSysFtDirection_Type(Integer32):
    """Custom type a3ComSysFtDirection based on Integer32"""
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


_A3ComSysFtDirection_Type.__name__ = "Integer32"
_A3ComSysFtDirection_Object = MibTableColumn
a3ComSysFtDirection = _A3ComSysFtDirection_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 14, 1, 1, 2),
    _A3ComSysFtDirection_Type()
)
a3ComSysFtDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComSysFtDirection.setStatus("mandatory")


class _A3ComSysFtLocalStorageType_Type(A3ComSysStorageType):
    """Custom type a3ComSysFtLocalStorageType based on A3ComSysStorageType"""
    defaultValue = 3


_A3ComSysFtLocalStorageType_Object = MibTableColumn
a3ComSysFtLocalStorageType = _A3ComSysFtLocalStorageType_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 14, 1, 1, 3),
    _A3ComSysFtLocalStorageType_Type()
)
a3ComSysFtLocalStorageType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComSysFtLocalStorageType.setStatus("mandatory")


class _A3ComSysFtLocalResourceType_Type(A3ComSysResourceType):
    """Custom type a3ComSysFtLocalResourceType based on A3ComSysResourceType"""
    defaultValue = 2


_A3ComSysFtLocalResourceType_Object = MibTableColumn
a3ComSysFtLocalResourceType = _A3ComSysFtLocalResourceType_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 14, 1, 1, 4),
    _A3ComSysFtLocalResourceType_Type()
)
a3ComSysFtLocalResourceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComSysFtLocalResourceType.setStatus("mandatory")


class _A3ComSysFtLocalResourceMask_Type(A3ComSysResourceBitMask):
    """Custom type a3ComSysFtLocalResourceMask based on A3ComSysResourceBitMask"""
    defaultValue = 128


_A3ComSysFtLocalResourceMask_Object = MibTableColumn
a3ComSysFtLocalResourceMask = _A3ComSysFtLocalResourceMask_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 14, 1, 1, 5),
    _A3ComSysFtLocalResourceMask_Type()
)
a3ComSysFtLocalResourceMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComSysFtLocalResourceMask.setStatus("mandatory")


class _A3ComSysFtLocalResourceAttribute_Type(ObjectIdentifier):
    """Custom type a3ComSysFtLocalResourceAttribute based on ObjectIdentifier"""
    defaultValue = (1, 3, 6, 1, 4, 1, 43, 29, 4, 14, 2, 1, 1)


_A3ComSysFtLocalResourceAttribute_Object = MibTableColumn
a3ComSysFtLocalResourceAttribute = _A3ComSysFtLocalResourceAttribute_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 14, 1, 1, 6),
    _A3ComSysFtLocalResourceAttribute_Type()
)
a3ComSysFtLocalResourceAttribute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComSysFtLocalResourceAttribute.setStatus("mandatory")


class _A3ComSysFtRemoteAddressType_Type(A3ComSysAddressType):
    """Custom type a3ComSysFtRemoteAddressType based on A3ComSysAddressType"""
    defaultValue = 2


_A3ComSysFtRemoteAddressType_Object = MibTableColumn
a3ComSysFtRemoteAddressType = _A3ComSysFtRemoteAddressType_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 14, 1, 1, 7),
    _A3ComSysFtRemoteAddressType_Type()
)
a3ComSysFtRemoteAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComSysFtRemoteAddressType.setStatus("mandatory")


class _A3ComSysFtRemoteAddress_Type(OctetString):
    """Custom type a3ComSysFtRemoteAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_A3ComSysFtRemoteAddress_Type.__name__ = "OctetString"
_A3ComSysFtRemoteAddress_Object = MibTableColumn
a3ComSysFtRemoteAddress = _A3ComSysFtRemoteAddress_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 14, 1, 1, 8),
    _A3ComSysFtRemoteAddress_Type()
)
a3ComSysFtRemoteAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComSysFtRemoteAddress.setStatus("mandatory")


class _A3ComSysFtRemoteFileName_Type(DisplayString):
    """Custom type a3ComSysFtRemoteFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_A3ComSysFtRemoteFileName_Type.__name__ = "DisplayString"
_A3ComSysFtRemoteFileName_Object = MibTableColumn
a3ComSysFtRemoteFileName = _A3ComSysFtRemoteFileName_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 14, 1, 1, 9),
    _A3ComSysFtRemoteFileName_Type()
)
a3ComSysFtRemoteFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComSysFtRemoteFileName.setStatus("mandatory")


class _A3ComSysFtRemoteUserName_Type(DisplayString):
    """Custom type a3ComSysFtRemoteUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_A3ComSysFtRemoteUserName_Type.__name__ = "DisplayString"
_A3ComSysFtRemoteUserName_Object = MibTableColumn
a3ComSysFtRemoteUserName = _A3ComSysFtRemoteUserName_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 14, 1, 1, 10),
    _A3ComSysFtRemoteUserName_Type()
)
a3ComSysFtRemoteUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComSysFtRemoteUserName.setStatus("mandatory")


class _A3ComSysFtRemoteUserPassword_Type(OctetString):
    """Custom type a3ComSysFtRemoteUserPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_A3ComSysFtRemoteUserPassword_Type.__name__ = "OctetString"
_A3ComSysFtRemoteUserPassword_Object = MibTableColumn
a3ComSysFtRemoteUserPassword = _A3ComSysFtRemoteUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 14, 1, 1, 11),
    _A3ComSysFtRemoteUserPassword_Type()
)
a3ComSysFtRemoteUserPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComSysFtRemoteUserPassword.setStatus("mandatory")


class _A3ComSysFtForceTransfer_Type(Integer32):
    """Custom type a3ComSysFtForceTransfer based on Integer32"""
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


_A3ComSysFtForceTransfer_Type.__name__ = "Integer32"
_A3ComSysFtForceTransfer_Object = MibTableColumn
a3ComSysFtForceTransfer = _A3ComSysFtForceTransfer_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 14, 1, 1, 12),
    _A3ComSysFtForceTransfer_Type()
)
a3ComSysFtForceTransfer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComSysFtForceTransfer.setStatus("mandatory")
_A3ComSysFtBytesTransferred_Type = Counter32
_A3ComSysFtBytesTransferred_Object = MibTableColumn
a3ComSysFtBytesTransferred = _A3ComSysFtBytesTransferred_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 14, 1, 1, 13),
    _A3ComSysFtBytesTransferred_Type()
)
a3ComSysFtBytesTransferred.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysFtBytesTransferred.setStatus("mandatory")


class _A3ComSysFtStatus_Type(Integer32):
    """Custom type a3ComSysFtStatus based on Integer32"""
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


_A3ComSysFtStatus_Type.__name__ = "Integer32"
_A3ComSysFtStatus_Object = MibTableColumn
a3ComSysFtStatus = _A3ComSysFtStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 14, 1, 1, 14),
    _A3ComSysFtStatus_Type()
)
a3ComSysFtStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysFtStatus.setStatus("mandatory")
_A3ComSysFtDetailedStatus_Type = ObjectIdentifier
_A3ComSysFtDetailedStatus_Object = MibTableColumn
a3ComSysFtDetailedStatus = _A3ComSysFtDetailedStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 14, 1, 1, 15),
    _A3ComSysFtDetailedStatus_Type()
)
a3ComSysFtDetailedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysFtDetailedStatus.setStatus("mandatory")
_A3ComSysFtDetailedStatusString_Type = DisplayString
_A3ComSysFtDetailedStatusString_Object = MibTableColumn
a3ComSysFtDetailedStatusString = _A3ComSysFtDetailedStatusString_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 14, 1, 1, 16),
    _A3ComSysFtDetailedStatusString_Type()
)
a3ComSysFtDetailedStatusString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysFtDetailedStatusString.setStatus("mandatory")


class _A3ComSysFtOwnerString_Type(DisplayString):
    """Custom type a3ComSysFtOwnerString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_A3ComSysFtOwnerString_Type.__name__ = "DisplayString"
_A3ComSysFtOwnerString_Object = MibTableColumn
a3ComSysFtOwnerString = _A3ComSysFtOwnerString_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 14, 1, 1, 17),
    _A3ComSysFtOwnerString_Type()
)
a3ComSysFtOwnerString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComSysFtOwnerString.setStatus("mandatory")
_A3ComSysFtRowStatus_Type = RowStatus
_A3ComSysFtRowStatus_Object = MibTableColumn
a3ComSysFtRowStatus = _A3ComSysFtRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 14, 1, 1, 18),
    _A3ComSysFtRowStatus_Type()
)
a3ComSysFtRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComSysFtRowStatus.setStatus("mandatory")
_A3ComSysFtResourceAttributes_ObjectIdentity = ObjectIdentity
a3ComSysFtResourceAttributes = _A3ComSysFtResourceAttributes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 14, 2)
)
_A3ComSysFtSystemAttributes_ObjectIdentity = ObjectIdentity
a3ComSysFtSystemAttributes = _A3ComSysFtSystemAttributes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 14, 2, 1)
)
_A3ComSysFtSystemOperationalCode_ObjectIdentity = ObjectIdentity
a3ComSysFtSystemOperationalCode = _A3ComSysFtSystemOperationalCode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 14, 2, 1, 1)
)
_A3ComSysFtSystemConfiguration_ObjectIdentity = ObjectIdentity
a3ComSysFtSystemConfiguration = _A3ComSysFtSystemConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 14, 2, 1, 2)
)
_A3ComSysFtSystemBridgeFilterCode_ObjectIdentity = ObjectIdentity
a3ComSysFtSystemBridgeFilterCode = _A3ComSysFtSystemBridgeFilterCode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 14, 2, 1, 3)
)
_A3ComSysFtDetailedResourceStatus_ObjectIdentity = ObjectIdentity
a3ComSysFtDetailedResourceStatus = _A3ComSysFtDetailedResourceStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 14, 3)
)
_A3ComSysFtSystemDetailedStatus_ObjectIdentity = ObjectIdentity
a3ComSysFtSystemDetailedStatus = _A3ComSysFtSystemDetailedStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 14, 3, 1)
)
_A3ComSysFtSysStatusNotApplicable_ObjectIdentity = ObjectIdentity
a3ComSysFtSysStatusNotApplicable = _A3ComSysFtSysStatusNotApplicable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 14, 3, 1, 1)
)
_A3ComSysFtSysStatusNoImageLabel_ObjectIdentity = ObjectIdentity
a3ComSysFtSysStatusNoImageLabel = _A3ComSysFtSysStatusNoImageLabel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 14, 3, 1, 2)
)
_A3ComSysFtSysStatusConfigIdMismatch_ObjectIdentity = ObjectIdentity
a3ComSysFtSysStatusConfigIdMismatch = _A3ComSysFtSysStatusConfigIdMismatch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 14, 3, 1, 3)
)
_A3ComSysFtSysStatusChecksumError_ObjectIdentity = ObjectIdentity
a3ComSysFtSysStatusChecksumError = _A3ComSysFtSysStatusChecksumError_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 14, 3, 1, 4)
)
_A3ComSysFtSysStatusNvRamError_ObjectIdentity = ObjectIdentity
a3ComSysFtSysStatusNvRamError = _A3ComSysFtSysStatusNvRamError_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 14, 3, 1, 5)
)
_A3ComSysFtSysStatusFlashError_ObjectIdentity = ObjectIdentity
a3ComSysFtSysStatusFlashError = _A3ComSysFtSysStatusFlashError_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 14, 3, 1, 6)
)
_A3ComSysFtSysStatusNoRoom_ObjectIdentity = ObjectIdentity
a3ComSysFtSysStatusNoRoom = _A3ComSysFtSysStatusNoRoom_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 14, 3, 1, 7)
)
_A3ComSysFtSysBridgeFilterNotApplicable_ObjectIdentity = ObjectIdentity
a3ComSysFtSysBridgeFilterNotApplicable = _A3ComSysFtSysBridgeFilterNotApplicable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 14, 3, 1, 8)
)
_A3ComSysFtSysBridgeFilterSyntaxError_ObjectIdentity = ObjectIdentity
a3ComSysFtSysBridgeFilterSyntaxError = _A3ComSysFtSysBridgeFilterSyntaxError_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 14, 3, 1, 9)
)
_A3ComSysFtSysBridgeFilterdownloadError_ObjectIdentity = ObjectIdentity
a3ComSysFtSysBridgeFilterdownloadError = _A3ComSysFtSysBridgeFilterdownloadError_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 14, 3, 1, 10)
)
_A3ComSysFtSysBridgeFilterNoRoom_ObjectIdentity = ObjectIdentity
a3ComSysFtSysBridgeFilterNoRoom = _A3ComSysFtSysBridgeFilterNoRoom_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 14, 3, 1, 11)
)
_A3ComSysIpGroup_ObjectIdentity = ObjectIdentity
a3ComSysIpGroup = _A3ComSysIpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 15)
)
_A3ComSysIpBaseGroup_ObjectIdentity = ObjectIdentity
a3ComSysIpBaseGroup = _A3ComSysIpBaseGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 15, 1)
)
_A3ComSysIpInterfaceGroup_ObjectIdentity = ObjectIdentity
a3ComSysIpInterfaceGroup = _A3ComSysIpInterfaceGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 15, 2)
)
_A3ComSysIpInterfaceCount_Type = Integer32
_A3ComSysIpInterfaceCount_Object = MibScalar
a3ComSysIpInterfaceCount = _A3ComSysIpInterfaceCount_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 15, 2, 1),
    _A3ComSysIpInterfaceCount_Type()
)
a3ComSysIpInterfaceCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysIpInterfaceCount.setStatus("mandatory")
_A3ComSysIpInterfaceTable_Object = MibTable
a3ComSysIpInterfaceTable = _A3ComSysIpInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 15, 2, 2)
)
if mibBuilder.loadTexts:
    a3ComSysIpInterfaceTable.setStatus("mandatory")
_A3ComSysIpInterfaceEntry_Object = MibTableRow
a3ComSysIpInterfaceEntry = _A3ComSysIpInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 15, 2, 2, 1)
)
a3ComSysIpInterfaceEntry.setIndexNames(
    (0, "A3COM-SWITCHING-SYSTEMS-MIB", "a3ComSysIpInterfaceIpStackIndex"),
    (0, "A3COM-SWITCHING-SYSTEMS-MIB", "a3ComSysIpInterfaceAddr"),
    (0, "A3COM-SWITCHING-SYSTEMS-MIB", "a3ComSysIpInterfaceNetMask"),
)
if mibBuilder.loadTexts:
    a3ComSysIpInterfaceEntry.setStatus("mandatory")
_A3ComSysIpInterfaceIpStackIndex_Type = Integer32
_A3ComSysIpInterfaceIpStackIndex_Object = MibTableColumn
a3ComSysIpInterfaceIpStackIndex = _A3ComSysIpInterfaceIpStackIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 15, 2, 2, 1, 1),
    _A3ComSysIpInterfaceIpStackIndex_Type()
)
a3ComSysIpInterfaceIpStackIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysIpInterfaceIpStackIndex.setStatus("mandatory")
_A3ComSysIpInterfaceAddr_Type = IpAddress
_A3ComSysIpInterfaceAddr_Object = MibTableColumn
a3ComSysIpInterfaceAddr = _A3ComSysIpInterfaceAddr_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 15, 2, 2, 1, 2),
    _A3ComSysIpInterfaceAddr_Type()
)
a3ComSysIpInterfaceAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysIpInterfaceAddr.setStatus("mandatory")
_A3ComSysIpInterfaceNetMask_Type = IpAddress
_A3ComSysIpInterfaceNetMask_Object = MibTableColumn
a3ComSysIpInterfaceNetMask = _A3ComSysIpInterfaceNetMask_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 15, 2, 2, 1, 3),
    _A3ComSysIpInterfaceNetMask_Type()
)
a3ComSysIpInterfaceNetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysIpInterfaceNetMask.setStatus("mandatory")
_A3ComSysIpInterfaceIndex_Type = Integer32
_A3ComSysIpInterfaceIndex_Object = MibTableColumn
a3ComSysIpInterfaceIndex = _A3ComSysIpInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 15, 2, 2, 1, 4),
    _A3ComSysIpInterfaceIndex_Type()
)
a3ComSysIpInterfaceIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComSysIpInterfaceIndex.setStatus("mandatory")


class _A3ComSysIpInterfaceBcastAddr_Type(Integer32):
    """Custom type a3ComSysIpInterfaceBcastAddr based on Integer32"""
    defaultValue = 1


_A3ComSysIpInterfaceBcastAddr_Object = MibTableColumn
a3ComSysIpInterfaceBcastAddr = _A3ComSysIpInterfaceBcastAddr_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 15, 2, 2, 1, 5),
    _A3ComSysIpInterfaceBcastAddr_Type()
)
a3ComSysIpInterfaceBcastAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComSysIpInterfaceBcastAddr.setStatus("mandatory")


class _A3ComSysIpInterfaceCost_Type(Integer32):
    """Custom type a3ComSysIpInterfaceCost based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_A3ComSysIpInterfaceCost_Type.__name__ = "Integer32"
_A3ComSysIpInterfaceCost_Object = MibTableColumn
a3ComSysIpInterfaceCost = _A3ComSysIpInterfaceCost_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 15, 2, 2, 1, 6),
    _A3ComSysIpInterfaceCost_Type()
)
a3ComSysIpInterfaceCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComSysIpInterfaceCost.setStatus("mandatory")
_A3ComSysIpInterfaceStatus_Type = RowStatus
_A3ComSysIpInterfaceStatus_Object = MibTableColumn
a3ComSysIpInterfaceStatus = _A3ComSysIpInterfaceStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 15, 2, 2, 1, 7),
    _A3ComSysIpInterfaceStatus_Type()
)
a3ComSysIpInterfaceStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComSysIpInterfaceStatus.setStatus("mandatory")
_A3ComSysIpxGroup_ObjectIdentity = ObjectIdentity
a3ComSysIpxGroup = _A3ComSysIpxGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 16)
)
_A3ComSysIpxBaseGroup_ObjectIdentity = ObjectIdentity
a3ComSysIpxBaseGroup = _A3ComSysIpxBaseGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 16, 1)
)
_A3ComSysIpxInterfaceGroup_ObjectIdentity = ObjectIdentity
a3ComSysIpxInterfaceGroup = _A3ComSysIpxInterfaceGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 16, 2)
)
_A3ComSysIpxInterfaceCount_Type = Integer32
_A3ComSysIpxInterfaceCount_Object = MibScalar
a3ComSysIpxInterfaceCount = _A3ComSysIpxInterfaceCount_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 16, 2, 1),
    _A3ComSysIpxInterfaceCount_Type()
)
a3ComSysIpxInterfaceCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysIpxInterfaceCount.setStatus("mandatory")
_A3ComSysIpxInterfaceTable_Object = MibTable
a3ComSysIpxInterfaceTable = _A3ComSysIpxInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 16, 2, 2)
)
if mibBuilder.loadTexts:
    a3ComSysIpxInterfaceTable.setStatus("mandatory")
_A3ComSysIpxInterfaceEntry_Object = MibTableRow
a3ComSysIpxInterfaceEntry = _A3ComSysIpxInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 16, 2, 2, 1)
)
a3ComSysIpxInterfaceEntry.setIndexNames(
    (0, "A3COM-SWITCHING-SYSTEMS-MIB", "a3ComSysIpxInterfaceIpxStackIndex"),
    (0, "A3COM-SWITCHING-SYSTEMS-MIB", "a3ComSysIpxInterfaceNetNumber"),
)
if mibBuilder.loadTexts:
    a3ComSysIpxInterfaceEntry.setStatus("mandatory")
_A3ComSysIpxInterfaceIpxStackIndex_Type = Integer32
_A3ComSysIpxInterfaceIpxStackIndex_Object = MibTableColumn
a3ComSysIpxInterfaceIpxStackIndex = _A3ComSysIpxInterfaceIpxStackIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 16, 2, 2, 1, 1),
    _A3ComSysIpxInterfaceIpxStackIndex_Type()
)
a3ComSysIpxInterfaceIpxStackIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysIpxInterfaceIpxStackIndex.setStatus("mandatory")
_A3ComSysIpxInterfaceNetNumber_Type = IpxNetworkNumber
_A3ComSysIpxInterfaceNetNumber_Object = MibTableColumn
a3ComSysIpxInterfaceNetNumber = _A3ComSysIpxInterfaceNetNumber_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 16, 2, 2, 1, 2),
    _A3ComSysIpxInterfaceNetNumber_Type()
)
a3ComSysIpxInterfaceNetNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysIpxInterfaceNetNumber.setStatus("mandatory")
_A3ComSysIpxInterfaceIfIndex_Type = Integer32
_A3ComSysIpxInterfaceIfIndex_Object = MibTableColumn
a3ComSysIpxInterfaceIfIndex = _A3ComSysIpxInterfaceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 16, 2, 2, 1, 3),
    _A3ComSysIpxInterfaceIfIndex_Type()
)
a3ComSysIpxInterfaceIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComSysIpxInterfaceIfIndex.setStatus("mandatory")


class _A3ComSysIpxInterfaceCost_Type(Integer32):
    """Custom type a3ComSysIpxInterfaceCost based on Integer32"""
    defaultValue = 1


_A3ComSysIpxInterfaceCost_Object = MibTableColumn
a3ComSysIpxInterfaceCost = _A3ComSysIpxInterfaceCost_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 16, 2, 2, 1, 4),
    _A3ComSysIpxInterfaceCost_Type()
)
a3ComSysIpxInterfaceCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComSysIpxInterfaceCost.setStatus("mandatory")


class _A3ComSysIpxInterfaceFrameType_Type(Integer32):
    """Custom type a3ComSysIpxInterfaceFrameType based on Integer32"""
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


_A3ComSysIpxInterfaceFrameType_Type.__name__ = "Integer32"
_A3ComSysIpxInterfaceFrameType_Object = MibTableColumn
a3ComSysIpxInterfaceFrameType = _A3ComSysIpxInterfaceFrameType_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 16, 2, 2, 1, 5),
    _A3ComSysIpxInterfaceFrameType_Type()
)
a3ComSysIpxInterfaceFrameType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComSysIpxInterfaceFrameType.setStatus("mandatory")
_A3ComSysIpxInterfaceStatus_Type = RowStatus
_A3ComSysIpxInterfaceStatus_Object = MibTableColumn
a3ComSysIpxInterfaceStatus = _A3ComSysIpxInterfaceStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 16, 2, 2, 1, 6),
    _A3ComSysIpxInterfaceStatus_Type()
)
a3ComSysIpxInterfaceStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComSysIpxInterfaceStatus.setStatus("mandatory")
_A3ComSysAppleTalkGroup_ObjectIdentity = ObjectIdentity
a3ComSysAppleTalkGroup = _A3ComSysAppleTalkGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 17)
)
_A3ComSysAppleTalkBaseGroup_ObjectIdentity = ObjectIdentity
a3ComSysAppleTalkBaseGroup = _A3ComSysAppleTalkBaseGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 17, 1)
)
_A3ComSysAppleTalkInterfaceGroup_ObjectIdentity = ObjectIdentity
a3ComSysAppleTalkInterfaceGroup = _A3ComSysAppleTalkInterfaceGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 17, 2)
)
_A3ComSysAtInterfaceCount_Type = Integer32
_A3ComSysAtInterfaceCount_Object = MibScalar
a3ComSysAtInterfaceCount = _A3ComSysAtInterfaceCount_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 17, 2, 1),
    _A3ComSysAtInterfaceCount_Type()
)
a3ComSysAtInterfaceCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysAtInterfaceCount.setStatus("mandatory")
_A3ComSysAtInterfaceTable_Object = MibTable
a3ComSysAtInterfaceTable = _A3ComSysAtInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 17, 2, 2)
)
if mibBuilder.loadTexts:
    a3ComSysAtInterfaceTable.setStatus("mandatory")
_A3ComSysAtInterfaceEntry_Object = MibTableRow
a3ComSysAtInterfaceEntry = _A3ComSysAtInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 17, 2, 2, 1)
)
a3ComSysAtInterfaceEntry.setIndexNames(
    (0, "A3COM-SWITCHING-SYSTEMS-MIB", "a3ComSysAtInterfaceAtStackIndex"),
    (0, "A3COM-SWITCHING-SYSTEMS-MIB", "a3ComSysAtInterfaceIfIndex"),
)
if mibBuilder.loadTexts:
    a3ComSysAtInterfaceEntry.setStatus("mandatory")
_A3ComSysAtInterfaceAtStackIndex_Type = Integer32
_A3ComSysAtInterfaceAtStackIndex_Object = MibTableColumn
a3ComSysAtInterfaceAtStackIndex = _A3ComSysAtInterfaceAtStackIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 17, 2, 2, 1, 1),
    _A3ComSysAtInterfaceAtStackIndex_Type()
)
a3ComSysAtInterfaceAtStackIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComSysAtInterfaceAtStackIndex.setStatus("mandatory")
_A3ComSysAtInterfaceNetAddress_Type = DdpNodeAddress
_A3ComSysAtInterfaceNetAddress_Object = MibTableColumn
a3ComSysAtInterfaceNetAddress = _A3ComSysAtInterfaceNetAddress_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 17, 2, 2, 1, 2),
    _A3ComSysAtInterfaceNetAddress_Type()
)
a3ComSysAtInterfaceNetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysAtInterfaceNetAddress.setStatus("mandatory")


class _A3ComSysAtInterfaceType_Type(Integer32):
    """Custom type a3ComSysAtInterfaceType based on Integer32"""
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


_A3ComSysAtInterfaceType_Type.__name__ = "Integer32"
_A3ComSysAtInterfaceType_Object = MibTableColumn
a3ComSysAtInterfaceType = _A3ComSysAtInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 17, 2, 2, 1, 3),
    _A3ComSysAtInterfaceType_Type()
)
a3ComSysAtInterfaceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComSysAtInterfaceType.setStatus("mandatory")
_A3ComSysAtInterfaceNetStart_Type = ATNetworkNumber
_A3ComSysAtInterfaceNetStart_Object = MibTableColumn
a3ComSysAtInterfaceNetStart = _A3ComSysAtInterfaceNetStart_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 17, 2, 2, 1, 4),
    _A3ComSysAtInterfaceNetStart_Type()
)
a3ComSysAtInterfaceNetStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComSysAtInterfaceNetStart.setStatus("mandatory")
_A3ComSysAtInterfaceNetEnd_Type = ATNetworkNumber
_A3ComSysAtInterfaceNetEnd_Object = MibTableColumn
a3ComSysAtInterfaceNetEnd = _A3ComSysAtInterfaceNetEnd_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 17, 2, 2, 1, 5),
    _A3ComSysAtInterfaceNetEnd_Type()
)
a3ComSysAtInterfaceNetEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComSysAtInterfaceNetEnd.setStatus("mandatory")
_A3ComSysAtInterfaceZoneDefault_Type = ATName
_A3ComSysAtInterfaceZoneDefault_Object = MibTableColumn
a3ComSysAtInterfaceZoneDefault = _A3ComSysAtInterfaceZoneDefault_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 17, 2, 2, 1, 6),
    _A3ComSysAtInterfaceZoneDefault_Type()
)
a3ComSysAtInterfaceZoneDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComSysAtInterfaceZoneDefault.setStatus("mandatory")
_A3ComSysAtInterfaceZone1_Type = ATName
_A3ComSysAtInterfaceZone1_Object = MibTableColumn
a3ComSysAtInterfaceZone1 = _A3ComSysAtInterfaceZone1_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 17, 2, 2, 1, 7),
    _A3ComSysAtInterfaceZone1_Type()
)
a3ComSysAtInterfaceZone1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComSysAtInterfaceZone1.setStatus("mandatory")
_A3ComSysAtInterfaceZone2_Type = ATName
_A3ComSysAtInterfaceZone2_Object = MibTableColumn
a3ComSysAtInterfaceZone2 = _A3ComSysAtInterfaceZone2_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 17, 2, 2, 1, 8),
    _A3ComSysAtInterfaceZone2_Type()
)
a3ComSysAtInterfaceZone2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComSysAtInterfaceZone2.setStatus("mandatory")
_A3ComSysAtInterfaceZone3_Type = ATName
_A3ComSysAtInterfaceZone3_Object = MibTableColumn
a3ComSysAtInterfaceZone3 = _A3ComSysAtInterfaceZone3_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 17, 2, 2, 1, 9),
    _A3ComSysAtInterfaceZone3_Type()
)
a3ComSysAtInterfaceZone3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComSysAtInterfaceZone3.setStatus("mandatory")
_A3ComSysAtInterfaceZone4_Type = ATName
_A3ComSysAtInterfaceZone4_Object = MibTableColumn
a3ComSysAtInterfaceZone4 = _A3ComSysAtInterfaceZone4_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 17, 2, 2, 1, 10),
    _A3ComSysAtInterfaceZone4_Type()
)
a3ComSysAtInterfaceZone4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComSysAtInterfaceZone4.setStatus("mandatory")
_A3ComSysAtInterfaceZone5_Type = ATName
_A3ComSysAtInterfaceZone5_Object = MibTableColumn
a3ComSysAtInterfaceZone5 = _A3ComSysAtInterfaceZone5_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 17, 2, 2, 1, 11),
    _A3ComSysAtInterfaceZone5_Type()
)
a3ComSysAtInterfaceZone5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComSysAtInterfaceZone5.setStatus("mandatory")
_A3ComSysAtInterfaceZone6_Type = ATName
_A3ComSysAtInterfaceZone6_Object = MibTableColumn
a3ComSysAtInterfaceZone6 = _A3ComSysAtInterfaceZone6_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 17, 2, 2, 1, 12),
    _A3ComSysAtInterfaceZone6_Type()
)
a3ComSysAtInterfaceZone6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComSysAtInterfaceZone6.setStatus("mandatory")
_A3ComSysAtInterfaceZone7_Type = ATName
_A3ComSysAtInterfaceZone7_Object = MibTableColumn
a3ComSysAtInterfaceZone7 = _A3ComSysAtInterfaceZone7_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 17, 2, 2, 1, 13),
    _A3ComSysAtInterfaceZone7_Type()
)
a3ComSysAtInterfaceZone7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComSysAtInterfaceZone7.setStatus("mandatory")
_A3ComSysAtInterfaceZone8_Type = ATName
_A3ComSysAtInterfaceZone8_Object = MibTableColumn
a3ComSysAtInterfaceZone8 = _A3ComSysAtInterfaceZone8_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 17, 2, 2, 1, 14),
    _A3ComSysAtInterfaceZone8_Type()
)
a3ComSysAtInterfaceZone8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComSysAtInterfaceZone8.setStatus("mandatory")
_A3ComSysAtInterfaceZone9_Type = ATName
_A3ComSysAtInterfaceZone9_Object = MibTableColumn
a3ComSysAtInterfaceZone9 = _A3ComSysAtInterfaceZone9_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 17, 2, 2, 1, 15),
    _A3ComSysAtInterfaceZone9_Type()
)
a3ComSysAtInterfaceZone9.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComSysAtInterfaceZone9.setStatus("mandatory")
_A3ComSysAtInterfaceZone10_Type = ATName
_A3ComSysAtInterfaceZone10_Object = MibTableColumn
a3ComSysAtInterfaceZone10 = _A3ComSysAtInterfaceZone10_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 17, 2, 2, 1, 16),
    _A3ComSysAtInterfaceZone10_Type()
)
a3ComSysAtInterfaceZone10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComSysAtInterfaceZone10.setStatus("mandatory")
_A3ComSysAtInterfaceZone11_Type = ATName
_A3ComSysAtInterfaceZone11_Object = MibTableColumn
a3ComSysAtInterfaceZone11 = _A3ComSysAtInterfaceZone11_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 17, 2, 2, 1, 17),
    _A3ComSysAtInterfaceZone11_Type()
)
a3ComSysAtInterfaceZone11.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComSysAtInterfaceZone11.setStatus("mandatory")
_A3ComSysAtInterfaceZone12_Type = ATName
_A3ComSysAtInterfaceZone12_Object = MibTableColumn
a3ComSysAtInterfaceZone12 = _A3ComSysAtInterfaceZone12_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 17, 2, 2, 1, 18),
    _A3ComSysAtInterfaceZone12_Type()
)
a3ComSysAtInterfaceZone12.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComSysAtInterfaceZone12.setStatus("mandatory")
_A3ComSysAtInterfaceZone13_Type = ATName
_A3ComSysAtInterfaceZone13_Object = MibTableColumn
a3ComSysAtInterfaceZone13 = _A3ComSysAtInterfaceZone13_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 17, 2, 2, 1, 19),
    _A3ComSysAtInterfaceZone13_Type()
)
a3ComSysAtInterfaceZone13.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComSysAtInterfaceZone13.setStatus("mandatory")
_A3ComSysAtInterfaceZone14_Type = ATName
_A3ComSysAtInterfaceZone14_Object = MibTableColumn
a3ComSysAtInterfaceZone14 = _A3ComSysAtInterfaceZone14_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 17, 2, 2, 1, 20),
    _A3ComSysAtInterfaceZone14_Type()
)
a3ComSysAtInterfaceZone14.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComSysAtInterfaceZone14.setStatus("mandatory")
_A3ComSysAtInterfaceZone15_Type = ATName
_A3ComSysAtInterfaceZone15_Object = MibTableColumn
a3ComSysAtInterfaceZone15 = _A3ComSysAtInterfaceZone15_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 17, 2, 2, 1, 21),
    _A3ComSysAtInterfaceZone15_Type()
)
a3ComSysAtInterfaceZone15.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComSysAtInterfaceZone15.setStatus("mandatory")
_A3ComSysAtInterfaceIfIndex_Type = Integer32
_A3ComSysAtInterfaceIfIndex_Object = MibTableColumn
a3ComSysAtInterfaceIfIndex = _A3ComSysAtInterfaceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 17, 2, 2, 1, 22),
    _A3ComSysAtInterfaceIfIndex_Type()
)
a3ComSysAtInterfaceIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComSysAtInterfaceIfIndex.setStatus("mandatory")


class _A3ComSysAtInterfaceState_Type(Integer32):
    """Custom type a3ComSysAtInterfaceState based on Integer32"""
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


_A3ComSysAtInterfaceState_Type.__name__ = "Integer32"
_A3ComSysAtInterfaceState_Object = MibTableColumn
a3ComSysAtInterfaceState = _A3ComSysAtInterfaceState_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 17, 2, 2, 1, 23),
    _A3ComSysAtInterfaceState_Type()
)
a3ComSysAtInterfaceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysAtInterfaceState.setStatus("mandatory")
_A3ComSysAtInterfaceStatus_Type = RowStatus
_A3ComSysAtInterfaceStatus_Object = MibTableColumn
a3ComSysAtInterfaceStatus = _A3ComSysAtInterfaceStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 17, 2, 2, 1, 24),
    _A3ComSysAtInterfaceStatus_Type()
)
a3ComSysAtInterfaceStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComSysAtInterfaceStatus.setStatus("mandatory")
_A3ComSysModuleCardGroup_ObjectIdentity = ObjectIdentity
a3ComSysModuleCardGroup = _A3ComSysModuleCardGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 18)
)
_A3ComSysModuleCardCount_Type = Integer32
_A3ComSysModuleCardCount_Object = MibScalar
a3ComSysModuleCardCount = _A3ComSysModuleCardCount_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 18, 1),
    _A3ComSysModuleCardCount_Type()
)
a3ComSysModuleCardCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysModuleCardCount.setStatus("mandatory")
_A3ComSysModuleCardInfoTable_Object = MibTable
a3ComSysModuleCardInfoTable = _A3ComSysModuleCardInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 18, 2)
)
if mibBuilder.loadTexts:
    a3ComSysModuleCardInfoTable.setStatus("mandatory")
_A3ComSysModuleCardInfoEntry_Object = MibTableRow
a3ComSysModuleCardInfoEntry = _A3ComSysModuleCardInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 18, 2, 1)
)
a3ComSysModuleCardInfoEntry.setIndexNames(
    (0, "A3COM-SWITCHING-SYSTEMS-MIB", "a3ComSysModuleCardInfoIndex"),
)
if mibBuilder.loadTexts:
    a3ComSysModuleCardInfoEntry.setStatus("mandatory")
_A3ComSysModuleCardInfoIndex_Type = Integer32
_A3ComSysModuleCardInfoIndex_Object = MibTableColumn
a3ComSysModuleCardInfoIndex = _A3ComSysModuleCardInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 18, 2, 1, 1),
    _A3ComSysModuleCardInfoIndex_Type()
)
a3ComSysModuleCardInfoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysModuleCardInfoIndex.setStatus("mandatory")


class _A3ComSysModuleCardInfoFamily_Type(Integer32):
    """Custom type a3ComSysModuleCardInfoFamily based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25)
        )
    )
    namedValues = NamedValues(
        *(("coreBuilder3500", 1),
          ("coreBuilder9000-FG24", 22),
          ("coreBuilder9000-FG9", 23),
          ("coreBuilder9000-LF10MC", 20),
          ("coreBuilder9000-LF20R", 19),
          ("coreBuilder9000-LF36T", 21),
          ("coreBuilder9000-LG9", 25),
          ("coreBuilder9000-LG9MC", 24),
          ("coreBuilder9000-RF12R", 17),
          ("coreBuilder9000-RF6MC", 18),
          ("superStack7000", 2),
          ("superStack9000", 3))
    )


_A3ComSysModuleCardInfoFamily_Type.__name__ = "Integer32"
_A3ComSysModuleCardInfoFamily_Object = MibTableColumn
a3ComSysModuleCardInfoFamily = _A3ComSysModuleCardInfoFamily_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 18, 2, 1, 2),
    _A3ComSysModuleCardInfoFamily_Type()
)
a3ComSysModuleCardInfoFamily.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysModuleCardInfoFamily.setStatus("mandatory")


class _A3ComSysModuleCardInfoGenericType_Type(Integer32):
    """Custom type a3ComSysModuleCardInfoGenericType based on Integer32"""
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


_A3ComSysModuleCardInfoGenericType_Type.__name__ = "Integer32"
_A3ComSysModuleCardInfoGenericType_Object = MibTableColumn
a3ComSysModuleCardInfoGenericType = _A3ComSysModuleCardInfoGenericType_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 18, 2, 1, 3),
    _A3ComSysModuleCardInfoGenericType_Type()
)
a3ComSysModuleCardInfoGenericType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysModuleCardInfoGenericType.setStatus("mandatory")


class _A3ComSysModuleCardInfoSpecificType_Type(Integer32):
    """Custom type a3ComSysModuleCardInfoSpecificType based on Integer32"""
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
              181,
              183,
              225,
              226,
              227,
              228,
              229,
              230,
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
          ("enet1000BaseSxMmfSCandGBIC", 183),
          ("enet100Mb100BaseFx", 227),
          ("enet100Mb100BaseT2", 230),
          ("enet100Mb100BaseT4", 228),
          ("enet100Mb100BaseTx", 225),
          ("enet100Mb100BaseTxSTP", 229),
          ("enet10or100BaseTxTelco", 226),
          ("enet1Gb1000BaseTx", 181),
          ("enet1Gb1300nMFiber", 178),
          ("enet1Gb850nMMultimodeFiber", 177),
          ("enet1GbCoax", 179),
          ("fddiCopperSTP", 244),
          ("fddiCopperUTP", 243),
          ("fddiMultimodeSC", 241),
          ("fddiSingleModeSC", 242),
          ("notApplicable", 1),
          ("packetSwitchingFabric1000BaseBackplane", 180))
    )


_A3ComSysModuleCardInfoSpecificType_Type.__name__ = "Integer32"
_A3ComSysModuleCardInfoSpecificType_Object = MibTableColumn
a3ComSysModuleCardInfoSpecificType = _A3ComSysModuleCardInfoSpecificType_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 18, 2, 1, 4),
    _A3ComSysModuleCardInfoSpecificType_Type()
)
a3ComSysModuleCardInfoSpecificType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysModuleCardInfoSpecificType.setStatus("mandatory")
_A3ComSysModuleCardInfoPartNumber_Type = DisplayString
_A3ComSysModuleCardInfoPartNumber_Object = MibTableColumn
a3ComSysModuleCardInfoPartNumber = _A3ComSysModuleCardInfoPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 18, 2, 1, 5),
    _A3ComSysModuleCardInfoPartNumber_Type()
)
a3ComSysModuleCardInfoPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysModuleCardInfoPartNumber.setStatus("mandatory")
_A3ComSysModuleCardInfoManufacturingDate_Type = DisplayString
_A3ComSysModuleCardInfoManufacturingDate_Object = MibTableColumn
a3ComSysModuleCardInfoManufacturingDate = _A3ComSysModuleCardInfoManufacturingDate_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 18, 2, 1, 6),
    _A3ComSysModuleCardInfoManufacturingDate_Type()
)
a3ComSysModuleCardInfoManufacturingDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysModuleCardInfoManufacturingDate.setStatus("mandatory")


class _A3ComSysModuleCardInfoModuleSerialNumber_Type(DisplayString):
    """Custom type a3ComSysModuleCardInfoModuleSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )


_A3ComSysModuleCardInfoModuleSerialNumber_Type.__name__ = "DisplayString"
_A3ComSysModuleCardInfoModuleSerialNumber_Object = MibTableColumn
a3ComSysModuleCardInfoModuleSerialNumber = _A3ComSysModuleCardInfoModuleSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 18, 2, 1, 7),
    _A3ComSysModuleCardInfoModuleSerialNumber_Type()
)
a3ComSysModuleCardInfoModuleSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysModuleCardInfoModuleSerialNumber.setStatus("mandatory")


class _A3ComSysModuleCardInfoTLASerialNumber_Type(DisplayString):
    """Custom type a3ComSysModuleCardInfoTLASerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )


_A3ComSysModuleCardInfoTLASerialNumber_Type.__name__ = "DisplayString"
_A3ComSysModuleCardInfoTLASerialNumber_Object = MibTableColumn
a3ComSysModuleCardInfoTLASerialNumber = _A3ComSysModuleCardInfoTLASerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 18, 2, 1, 8),
    _A3ComSysModuleCardInfoTLASerialNumber_Type()
)
a3ComSysModuleCardInfoTLASerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysModuleCardInfoTLASerialNumber.setStatus("mandatory")


class _A3ComSysModuleCardInfo3CNumber_Type(DisplayString):
    """Custom type a3ComSysModuleCardInfo3CNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )


_A3ComSysModuleCardInfo3CNumber_Type.__name__ = "DisplayString"
_A3ComSysModuleCardInfo3CNumber_Object = MibTableColumn
a3ComSysModuleCardInfo3CNumber = _A3ComSysModuleCardInfo3CNumber_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 18, 2, 1, 9),
    _A3ComSysModuleCardInfo3CNumber_Type()
)
a3ComSysModuleCardInfo3CNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysModuleCardInfo3CNumber.setStatus("mandatory")
_A3ComSysModuleCardInfoICTTestStatus_Type = Integer32
_A3ComSysModuleCardInfoICTTestStatus_Object = MibTableColumn
a3ComSysModuleCardInfoICTTestStatus = _A3ComSysModuleCardInfoICTTestStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 18, 2, 1, 10),
    _A3ComSysModuleCardInfoICTTestStatus_Type()
)
a3ComSysModuleCardInfoICTTestStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysModuleCardInfoICTTestStatus.setStatus("mandatory")
_A3ComSysModuleCardInfoICTTestRevision_Type = DisplayString
_A3ComSysModuleCardInfoICTTestRevision_Object = MibTableColumn
a3ComSysModuleCardInfoICTTestRevision = _A3ComSysModuleCardInfoICTTestRevision_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 18, 2, 1, 11),
    _A3ComSysModuleCardInfoICTTestRevision_Type()
)
a3ComSysModuleCardInfoICTTestRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysModuleCardInfoICTTestRevision.setStatus("mandatory")
_A3ComSysModuleCardInfoSystemTestStatus_Type = Integer32
_A3ComSysModuleCardInfoSystemTestStatus_Object = MibTableColumn
a3ComSysModuleCardInfoSystemTestStatus = _A3ComSysModuleCardInfoSystemTestStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 18, 2, 1, 12),
    _A3ComSysModuleCardInfoSystemTestStatus_Type()
)
a3ComSysModuleCardInfoSystemTestStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysModuleCardInfoSystemTestStatus.setStatus("mandatory")
_A3ComSysModuleCardInfoFunctionalTestStatus_Type = Integer32
_A3ComSysModuleCardInfoFunctionalTestStatus_Object = MibTableColumn
a3ComSysModuleCardInfoFunctionalTestStatus = _A3ComSysModuleCardInfoFunctionalTestStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 18, 2, 1, 13),
    _A3ComSysModuleCardInfoFunctionalTestStatus_Type()
)
a3ComSysModuleCardInfoFunctionalTestStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysModuleCardInfoFunctionalTestStatus.setStatus("mandatory")
_A3ComSysModuleCardInfoFunctionalTestRevision_Type = DisplayString
_A3ComSysModuleCardInfoFunctionalTestRevision_Object = MibTableColumn
a3ComSysModuleCardInfoFunctionalTestRevision = _A3ComSysModuleCardInfoFunctionalTestRevision_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 18, 2, 1, 14),
    _A3ComSysModuleCardInfoFunctionalTestRevision_Type()
)
a3ComSysModuleCardInfoFunctionalTestRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysModuleCardInfoFunctionalTestRevision.setStatus("mandatory")
_A3ComSysModuleCardInfoBoardRevision_Type = DisplayString
_A3ComSysModuleCardInfoBoardRevision_Object = MibTableColumn
a3ComSysModuleCardInfoBoardRevision = _A3ComSysModuleCardInfoBoardRevision_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 18, 2, 1, 15),
    _A3ComSysModuleCardInfoBoardRevision_Type()
)
a3ComSysModuleCardInfoBoardRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysModuleCardInfoBoardRevision.setStatus("mandatory")
_A3ComSysModuleCardInfoRuntimeHours_Type = Integer32
_A3ComSysModuleCardInfoRuntimeHours_Object = MibTableColumn
a3ComSysModuleCardInfoRuntimeHours = _A3ComSysModuleCardInfoRuntimeHours_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 18, 2, 1, 16),
    _A3ComSysModuleCardInfoRuntimeHours_Type()
)
a3ComSysModuleCardInfoRuntimeHours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysModuleCardInfoRuntimeHours.setStatus("mandatory")
_A3ComSysDiagnosticsGroup_ObjectIdentity = ObjectIdentity
a3ComSysDiagnosticsGroup = _A3ComSysDiagnosticsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 19)
)
_A3ComSysDiagnosticsInfoTable_Object = MibTable
a3ComSysDiagnosticsInfoTable = _A3ComSysDiagnosticsInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 19, 1)
)
if mibBuilder.loadTexts:
    a3ComSysDiagnosticsInfoTable.setStatus("mandatory")
_A3ComSysDiagnosticsInfoEntry_Object = MibTableRow
a3ComSysDiagnosticsInfoEntry = _A3ComSysDiagnosticsInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 19, 1, 1)
)
a3ComSysDiagnosticsInfoEntry.setIndexNames(
    (0, "A3COM-SWITCHING-SYSTEMS-MIB", "a3ComSysDiagnosticsInfoIndex"),
)
if mibBuilder.loadTexts:
    a3ComSysDiagnosticsInfoEntry.setStatus("mandatory")
_A3ComSysDiagnosticsInfoIndex_Type = Integer32
_A3ComSysDiagnosticsInfoIndex_Object = MibTableColumn
a3ComSysDiagnosticsInfoIndex = _A3ComSysDiagnosticsInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 19, 1, 1, 1),
    _A3ComSysDiagnosticsInfoIndex_Type()
)
a3ComSysDiagnosticsInfoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysDiagnosticsInfoIndex.setStatus("mandatory")
_A3ComSysDiagnosticsInfoPOVDiagnosticsRevision_Type = DisplayString
_A3ComSysDiagnosticsInfoPOVDiagnosticsRevision_Object = MibTableColumn
a3ComSysDiagnosticsInfoPOVDiagnosticsRevision = _A3ComSysDiagnosticsInfoPOVDiagnosticsRevision_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 19, 1, 1, 2),
    _A3ComSysDiagnosticsInfoPOVDiagnosticsRevision_Type()
)
a3ComSysDiagnosticsInfoPOVDiagnosticsRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysDiagnosticsInfoPOVDiagnosticsRevision.setStatus("mandatory")
_A3ComSysDiagnosticsInfoExtendedDiagnosticsRevision_Type = DisplayString
_A3ComSysDiagnosticsInfoExtendedDiagnosticsRevision_Object = MibTableColumn
a3ComSysDiagnosticsInfoExtendedDiagnosticsRevision = _A3ComSysDiagnosticsInfoExtendedDiagnosticsRevision_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 19, 1, 1, 3),
    _A3ComSysDiagnosticsInfoExtendedDiagnosticsRevision_Type()
)
a3ComSysDiagnosticsInfoExtendedDiagnosticsRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysDiagnosticsInfoExtendedDiagnosticsRevision.setStatus("mandatory")
_A3ComSysDiagnosticsInfoDiagnosticFailureCode_Type = DisplayString
_A3ComSysDiagnosticsInfoDiagnosticFailureCode_Object = MibTableColumn
a3ComSysDiagnosticsInfoDiagnosticFailureCode = _A3ComSysDiagnosticsInfoDiagnosticFailureCode_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 19, 1, 1, 4),
    _A3ComSysDiagnosticsInfoDiagnosticFailureCode_Type()
)
a3ComSysDiagnosticsInfoDiagnosticFailureCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysDiagnosticsInfoDiagnosticFailureCode.setStatus("mandatory")
_A3ComSysDiagnosticsInfoDiagnosticFailureDateTime_Type = DisplayString
_A3ComSysDiagnosticsInfoDiagnosticFailureDateTime_Object = MibTableColumn
a3ComSysDiagnosticsInfoDiagnosticFailureDateTime = _A3ComSysDiagnosticsInfoDiagnosticFailureDateTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 19, 1, 1, 5),
    _A3ComSysDiagnosticsInfoDiagnosticFailureDateTime_Type()
)
a3ComSysDiagnosticsInfoDiagnosticFailureDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysDiagnosticsInfoDiagnosticFailureDateTime.setStatus("mandatory")
_A3ComSysDiagnosticsInfoDiagnosticFailureSlotNumber_Type = Integer32
_A3ComSysDiagnosticsInfoDiagnosticFailureSlotNumber_Object = MibTableColumn
a3ComSysDiagnosticsInfoDiagnosticFailureSlotNumber = _A3ComSysDiagnosticsInfoDiagnosticFailureSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 19, 1, 1, 6),
    _A3ComSysDiagnosticsInfoDiagnosticFailureSlotNumber_Type()
)
a3ComSysDiagnosticsInfoDiagnosticFailureSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysDiagnosticsInfoDiagnosticFailureSlotNumber.setStatus("mandatory")
_A3ComSysDiagnosticsInfoDiagnosticFailureCounter_Type = Integer32
_A3ComSysDiagnosticsInfoDiagnosticFailureCounter_Object = MibTableColumn
a3ComSysDiagnosticsInfoDiagnosticFailureCounter = _A3ComSysDiagnosticsInfoDiagnosticFailureCounter_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 19, 1, 1, 7),
    _A3ComSysDiagnosticsInfoDiagnosticFailureCounter_Type()
)
a3ComSysDiagnosticsInfoDiagnosticFailureCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysDiagnosticsInfoDiagnosticFailureCounter.setStatus("mandatory")
_A3ComSysDiagnosticsInfoDiagnosticFieldDOACounter_Type = Integer32
_A3ComSysDiagnosticsInfoDiagnosticFieldDOACounter_Object = MibTableColumn
a3ComSysDiagnosticsInfoDiagnosticFieldDOACounter = _A3ComSysDiagnosticsInfoDiagnosticFieldDOACounter_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 19, 1, 1, 8),
    _A3ComSysDiagnosticsInfoDiagnosticFieldDOACounter_Type()
)
a3ComSysDiagnosticsInfoDiagnosticFieldDOACounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysDiagnosticsInfoDiagnosticFieldDOACounter.setStatus("mandatory")
_SwitchingSystemsFddiMibGroups_ObjectIdentity = ObjectIdentity
switchingSystemsFddiMibGroups = _SwitchingSystemsFddiMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 29, 10)
)

# Managed Objects groups


# Notification objects

a3ComSysSystemOverTemperatureEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 0, 1)
)
a3ComSysSystemOverTemperatureEvent.setObjects(
    ("A3COM-SWITCHING-SYSTEMS-MIB", "a3ComSysSystemOvertemperature")
)
if mibBuilder.loadTexts:
    a3ComSysSystemOverTemperatureEvent.setStatus(
        ""
    )

a3ComSysPowerSupplyFailureEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 0, 2)
)
a3ComSysPowerSupplyFailureEvent.setObjects(
      *(("A3COM-SWITCHING-SYSTEMS-MIB", "a3ComSysPowerSupplyStatusIndex"),
        ("A3COM-SWITCHING-SYSTEMS-MIB", "a3ComSysPowerSupplyStatus"),
        ("A3COM-SWITCHING-SYSTEMS-MIB", "a3ComSysPowerSupplyStatusSupported"))
)
if mibBuilder.loadTexts:
    a3ComSysPowerSupplyFailureEvent.setStatus(
        ""
    )

a3ComSysChassisSlotOverTemperatureEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 0, 3)
)
a3ComSysChassisSlotOverTemperatureEvent.setObjects(
      *(("A3COM-SWITCHING-SYSTEMS-MIB", "a3ComSysSlotIndex"),
        ("A3COM-SWITCHING-SYSTEMS-MIB", "a3ComSysSlotBoardType"),
        ("A3COM-SWITCHING-SYSTEMS-MIB", "a3ComSysSlotBoardRevision"),
        ("A3COM-SWITCHING-SYSTEMS-MIB", "a3ComSysSlotBoardStatus"),
        ("A3COM-SWITCHING-SYSTEMS-MIB", "a3ComSysSlotOvertemperature"),
        ("A3COM-SWITCHING-SYSTEMS-MIB", "a3ComSysSlotConverterBad"))
)
if mibBuilder.loadTexts:
    a3ComSysChassisSlotOverTemperatureEvent.setStatus(
        ""
    )

a3ComSysChassisSlotInsertEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 0, 4)
)
a3ComSysChassisSlotInsertEvent.setObjects(
      *(("A3COM-SWITCHING-SYSTEMS-MIB", "a3ComSysSlotIndex"),
        ("A3COM-SWITCHING-SYSTEMS-MIB", "a3ComSysSlotBoardType"),
        ("A3COM-SWITCHING-SYSTEMS-MIB", "a3ComSysSlotBoardRevision"))
)
if mibBuilder.loadTexts:
    a3ComSysChassisSlotInsertEvent.setStatus(
        ""
    )

a3ComSysChassisSlotExtractEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 0, 5)
)
a3ComSysChassisSlotExtractEvent.setObjects(
    ("A3COM-SWITCHING-SYSTEMS-MIB", "a3ComSysSlotIndex")
)
if mibBuilder.loadTexts:
    a3ComSysChassisSlotExtractEvent.setStatus(
        ""
    )

a3ComSysBridgeAddressThresholdEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 0, 6)
)
a3ComSysBridgeAddressThresholdEvent.setObjects(
    ("A3COM-SWITCHING-SYSTEMS-MIB", "a3ComSysBridgeIndex")
)
if mibBuilder.loadTexts:
    a3ComSysBridgeAddressThresholdEvent.setStatus(
        ""
    )

a3ComSysSystemFanFailureEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 0, 7)
)
a3ComSysSystemFanFailureEvent.setObjects(
    ("A3COM-SWITCHING-SYSTEMS-MIB", "a3ComSysSystemFanFailure")
)
if mibBuilder.loadTexts:
    a3ComSysSystemFanFailureEvent.setStatus(
        ""
    )

a3ComSysModuleCardSysOverTemperatureEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 0, 8)
)
a3ComSysModuleCardSysOverTemperatureEvent.setObjects(
      *(("A3COM-SWITCHING-SYSTEMS-MIB", "a3ComSysModuleCardInfoIndex"),
        ("A3COM-SWITCHING-SYSTEMS-MIB", "a3ComSysModuleCardInfoFamily"),
        ("A3COM-SWITCHING-SYSTEMS-MIB", "a3ComSysModuleCardInfoGenericType"))
)
if mibBuilder.loadTexts:
    a3ComSysModuleCardSysOverTemperatureEvent.setStatus(
        ""
    )

a3ComSysModuleCardInsertEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 0, 9)
)
a3ComSysModuleCardInsertEvent.setObjects(
      *(("A3COM-SWITCHING-SYSTEMS-MIB", "a3ComSysModuleCardInfoIndex"),
        ("A3COM-SWITCHING-SYSTEMS-MIB", "a3ComSysModuleCardInfoFamily"),
        ("A3COM-SWITCHING-SYSTEMS-MIB", "a3ComSysModuleCardInfoGenericType"),
        ("A3COM-SWITCHING-SYSTEMS-MIB", "a3ComSysModuleCardInfoSpecificType"))
)
if mibBuilder.loadTexts:
    a3ComSysModuleCardInsertEvent.setStatus(
        ""
    )

a3ComSysModuleCardExtractEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 0, 10)
)
a3ComSysModuleCardExtractEvent.setObjects(
    ("A3COM-SWITCHING-SYSTEMS-MIB", "a3ComSysModuleCardInfoIndex")
)
if mibBuilder.loadTexts:
    a3ComSysModuleCardExtractEvent.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "A3COM-SWITCHING-SYSTEMS-MIB",
    **{"RowStatus": RowStatus,
       "A3ComSysStorageType": A3ComSysStorageType,
       "A3ComSysAddressType": A3ComSysAddressType,
       "A3ComSysResourceType": A3ComSysResourceType,
       "A3ComSysResourceBitMask": A3ComSysResourceBitMask,
       "IpxNetworkNumber": IpxNetworkNumber,
       "ATNetworkNumber": ATNetworkNumber,
       "ATName": ATName,
       "DdpNodeAddress": DdpNodeAddress,
       "MacAddress": MacAddress,
       "a3Com": a3Com,
       "switchingSystems-mib": switchingSystems_mib,
       "switchingSystemsMibGroups": switchingSystemsMibGroups,
       "a3ComSysSystemOverTemperatureEvent": a3ComSysSystemOverTemperatureEvent,
       "a3ComSysPowerSupplyFailureEvent": a3ComSysPowerSupplyFailureEvent,
       "a3ComSysChassisSlotOverTemperatureEvent": a3ComSysChassisSlotOverTemperatureEvent,
       "a3ComSysChassisSlotInsertEvent": a3ComSysChassisSlotInsertEvent,
       "a3ComSysChassisSlotExtractEvent": a3ComSysChassisSlotExtractEvent,
       "a3ComSysBridgeAddressThresholdEvent": a3ComSysBridgeAddressThresholdEvent,
       "a3ComSysSystemFanFailureEvent": a3ComSysSystemFanFailureEvent,
       "a3ComSysModuleCardSysOverTemperatureEvent": a3ComSysModuleCardSysOverTemperatureEvent,
       "a3ComSysModuleCardInsertEvent": a3ComSysModuleCardInsertEvent,
       "a3ComSysModuleCardExtractEvent": a3ComSysModuleCardExtractEvent,
       "a3ComSysSystem": a3ComSysSystem,
       "a3ComSysSystemId": a3ComSysSystemId,
       "a3ComSysSystemType": a3ComSysSystemType,
       "a3ComSysSystemName": a3ComSysSystemName,
       "a3ComSysSystemManufacturer": a3ComSysSystemManufacturer,
       "a3ComSysSystemHardwareRevision": a3ComSysSystemHardwareRevision,
       "a3ComSysSystemMemorySize": a3ComSysSystemMemorySize,
       "a3ComSysSystemFlashMemorySize": a3ComSysSystemFlashMemorySize,
       "a3ComSysSystemNvMemorySize": a3ComSysSystemNvMemorySize,
       "a3ComSysSystemSoftwareRevision": a3ComSysSystemSoftwareRevision,
       "a3ComSysSystemBuildTime": a3ComSysSystemBuildTime,
       "a3ComSysSystemSnmpRevision": a3ComSysSystemSnmpRevision,
       "a3ComSysSystemRequestedSnmpMode": a3ComSysSystemRequestedSnmpMode,
       "a3ComSysSystemCurrentSnmpMode": a3ComSysSystemCurrentSnmpMode,
       "a3ComSysSystemAction": a3ComSysSystemAction,
       "a3ComSysSystemOvertemperature": a3ComSysSystemOvertemperature,
       "a3ComSysSystemFanFailure": a3ComSysSystemFanFailure,
       "a3ComSysSystemProtocolMask": a3ComSysSystemProtocolMask,
       "a3ComSysSystemConsoleAccess": a3ComSysSystemConsoleAccess,
       "a3ComSysSystemConsoleReadPwd": a3ComSysSystemConsoleReadPwd,
       "a3ComSysSystemConsoleWritePwd": a3ComSysSystemConsoleWritePwd,
       "a3ComSysSystemConsoleAdminPwd": a3ComSysSystemConsoleAdminPwd,
       "a3ComSysSystemDateTime": a3ComSysSystemDateTime,
       "a3ComSysSystemDSTime": a3ComSysSystemDSTime,
       "a3ComSysSystemTimeZone": a3ComSysSystemTimeZone,
       "a3ComSysSystemCurrentFddiStationMode": a3ComSysSystemCurrentFddiStationMode,
       "a3ComSysSystemRequestedFddiStationMode": a3ComSysSystemRequestedFddiStationMode,
       "a3ComSysSystemLog": a3ComSysSystemLog,
       "a3ComSysSystemLogEntryCurrentCount": a3ComSysSystemLogEntryCurrentCount,
       "a3ComSysSystemLogMaxSize": a3ComSysSystemLogMaxSize,
       "a3ComSysSystemLogSeverityThreshold": a3ComSysSystemLogSeverityThreshold,
       "a3ComSysSystemLogTable": a3ComSysSystemLogTable,
       "a3ComSysSystemLogEntry": a3ComSysSystemLogEntry,
       "a3ComSysSystemLogIndex": a3ComSysSystemLogIndex,
       "a3ComSysSystemLogSeverityLevel": a3ComSysSystemLogSeverityLevel,
       "a3ComSysSystemLogDateTime": a3ComSysSystemLogDateTime,
       "a3ComSysSystemLogFacility": a3ComSysSystemLogFacility,
       "a3ComSysSystemLogMessage": a3ComSysSystemLogMessage,
       "a3ComSysSystemBaseMACAddress": a3ComSysSystemBaseMACAddress,
       "a3ComSysSystemMACAddressCount": a3ComSysSystemMACAddressCount,
       "a3ComSysSystemChassisSerialNumber": a3ComSysSystemChassisSerialNumber,
       "a3ComSysSystemFPMemorySize": a3ComSysSystemFPMemorySize,
       "a3ComSysSystemBufferSize": a3ComSysSystemBufferSize,
       "a3ComSysSlot": a3ComSysSlot,
       "a3ComSysSlotCount": a3ComSysSlotCount,
       "a3ComSysSlotTable": a3ComSysSlotTable,
       "a3ComSysSlotEntry": a3ComSysSlotEntry,
       "a3ComSysSlotIndex": a3ComSysSlotIndex,
       "a3ComSysSlotBoardType": a3ComSysSlotBoardType,
       "a3ComSysSlotBoardRevision": a3ComSysSlotBoardRevision,
       "a3ComSysSlotBoardStatus": a3ComSysSlotBoardStatus,
       "a3ComSysSlotBoardName": a3ComSysSlotBoardName,
       "a3ComSysSlotBoardNameAbbrev": a3ComSysSlotBoardNameAbbrev,
       "a3ComSysSlotEthernetPortCount": a3ComSysSlotEthernetPortCount,
       "a3ComSysSlotFddiMacCount": a3ComSysSlotFddiMacCount,
       "a3ComSysSlotFddiPortCount": a3ComSysSlotFddiPortCount,
       "a3ComSysSlotOvertemperature": a3ComSysSlotOvertemperature,
       "a3ComSysSlotTokenRingPortCount": a3ComSysSlotTokenRingPortCount,
       "a3ComSysSlotBoardRevStr": a3ComSysSlotBoardRevStr,
       "a3ComSysSlotConverterBad": a3ComSysSlotConverterBad,
       "a3ComSysControlPanel": a3ComSysControlPanel,
       "a3ComSysControlPanelHardwareRevision": a3ComSysControlPanelHardwareRevision,
       "a3ComSysControlPanelSoftwareRevision": a3ComSysControlPanelSoftwareRevision,
       "a3ComSysControlPanelLines": a3ComSysControlPanelLines,
       "a3ComSysControlPanelColumns": a3ComSysControlPanelColumns,
       "a3ComSysControlPanelText": a3ComSysControlPanelText,
       "a3ComSysControlPanelAccess": a3ComSysControlPanelAccess,
       "a3ComSysPowerSupply": a3ComSysPowerSupply,
       "a3ComSysPowerSupplyCount": a3ComSysPowerSupplyCount,
       "a3ComSysPowerSupplyStatusTable": a3ComSysPowerSupplyStatusTable,
       "a3ComSysPowerSupplyStatusEntry": a3ComSysPowerSupplyStatusEntry,
       "a3ComSysPowerSupplyStatusIndex": a3ComSysPowerSupplyStatusIndex,
       "a3ComSysPowerSupplyStatus": a3ComSysPowerSupplyStatus,
       "a3ComSysPowerSupplyStatusSupported": a3ComSysPowerSupplyStatusSupported,
       "a3ComSysSnmp": a3ComSysSnmp,
       "a3ComSysSnmpAgentId": a3ComSysSnmpAgentId,
       "a3ComSysSnmpInternalAgentTrapMask": a3ComSysSnmpInternalAgentTrapMask,
       "a3ComSysSnmpInternalAgentTrapDestinationMask": a3ComSysSnmpInternalAgentTrapDestinationMask,
       "a3ComSysSnmpProxyInternalRequests": a3ComSysSnmpProxyInternalRequests,
       "a3ComSysSnmpInternalProxyRequestMaxAge": a3ComSysSnmpInternalProxyRequestMaxAge,
       "a3ComSysSnmpProxyInternalTraps": a3ComSysSnmpProxyInternalTraps,
       "a3ComSysSnmpInternalProxyTable": a3ComSysSnmpInternalProxyTable,
       "a3ComSysSnmpInternalProxyEntry": a3ComSysSnmpInternalProxyEntry,
       "a3ComSysSnmpInternalProxyAgentId": a3ComSysSnmpInternalProxyAgentId,
       "a3ComSysSnmpInternalProxyAccessClass": a3ComSysSnmpInternalProxyAccessClass,
       "a3ComSysSnmpInternalProxyCommunity": a3ComSysSnmpInternalProxyCommunity,
       "a3ComSysAgent": a3ComSysAgent,
       "a3ComSysAgentRequestMaxAge": a3ComSysAgentRequestMaxAge,
       "a3ComSysAgentProxyRemoteSmtRequests": a3ComSysAgentProxyRemoteSmtRequests,
       "a3ComSysAgentRemoteSmtProxyRequestMaxAge": a3ComSysAgentRemoteSmtProxyRequestMaxAge,
       "a3ComSysAgentProxyRemoteSmtEvents": a3ComSysAgentProxyRemoteSmtEvents,
       "a3ComSysAgentTrapDescriptionTable": a3ComSysAgentTrapDescriptionTable,
       "a3ComSysAgentTrapDescriptionTableEntry": a3ComSysAgentTrapDescriptionTableEntry,
       "a3ComSysAgentTrapDescriptionIndex": a3ComSysAgentTrapDescriptionIndex,
       "a3ComSysAgentTrapEnterprise": a3ComSysAgentTrapEnterprise,
       "a3ComSysAgentTrapNumber": a3ComSysAgentTrapNumber,
       "a3ComSysAgentTrapDestinationTable": a3ComSysAgentTrapDestinationTable,
       "a3ComSysAgentTrapDestinationTableEntry": a3ComSysAgentTrapDestinationTableEntry,
       "a3ComSysAgentTrapDestinationAddressType": a3ComSysAgentTrapDestinationAddressType,
       "a3ComSysAgentTrapDestinationAddress": a3ComSysAgentTrapDestinationAddress,
       "a3ComSysAgentTrapDestinationTrapMask": a3ComSysAgentTrapDestinationTrapMask,
       "a3ComSysAgentTrapDestinationEntryStatus": a3ComSysAgentTrapDestinationEntryStatus,
       "a3ComSysAgentReadCommunity": a3ComSysAgentReadCommunity,
       "a3ComSysAgentReadWriteCommunity": a3ComSysAgentReadWriteCommunity,
       "a3ComSysInterface": a3ComSysInterface,
       "a3ComSysInterfaceLocationTable": a3ComSysInterfaceLocationTable,
       "a3ComSysInterfaceLocationEntry": a3ComSysInterfaceLocationEntry,
       "a3ComSysInterfaceLocationIfIndex": a3ComSysInterfaceLocationIfIndex,
       "a3ComSysInterfaceLocationInterfaceType": a3ComSysInterfaceLocationInterfaceType,
       "a3ComSysInterfaceLocationType": a3ComSysInterfaceLocationType,
       "a3ComSysInterfaceLocationTypeIndex": a3ComSysInterfaceLocationTypeIndex,
       "a3ComSysInterfaceLocationLocalIndex": a3ComSysInterfaceLocationLocalIndex,
       "a3ComSysInterfaceLocationSystemModuleIndex": a3ComSysInterfaceLocationSystemModuleIndex,
       "a3ComSysEthernetPort": a3ComSysEthernetPort,
       "a3ComSysEthernetPortCount": a3ComSysEthernetPortCount,
       "a3ComSysEthernetPortTable": a3ComSysEthernetPortTable,
       "a3ComSysEthernetPortEntry": a3ComSysEthernetPortEntry,
       "a3ComSysEthernetPortIndex": a3ComSysEthernetPortIndex,
       "a3ComSysEthernetPortIfIndex": a3ComSysEthernetPortIfIndex,
       "a3ComSysEthernetPortLabel": a3ComSysEthernetPortLabel,
       "a3ComSysEthernetPortLinkStatus": a3ComSysEthernetPortLinkStatus,
       "a3ComSysEthernetPortType": a3ComSysEthernetPortType,
       "a3ComSysEthernetPortRateTable": a3ComSysEthernetPortRateTable,
       "a3ComSysEthernetPortRateEntry": a3ComSysEthernetPortRateEntry,
       "a3ComSysEthernetPortRateIndex": a3ComSysEthernetPortRateIndex,
       "a3ComSysEthernetPortRateByteReceiveRate": a3ComSysEthernetPortRateByteReceiveRate,
       "a3ComSysEthernetPortRatePeakByteReceiveRate": a3ComSysEthernetPortRatePeakByteReceiveRate,
       "a3ComSysEthernetPortRateFrameReceiveRate": a3ComSysEthernetPortRateFrameReceiveRate,
       "a3ComSysEthernetPortRatePeakFrameReceiveRate": a3ComSysEthernetPortRatePeakFrameReceiveRate,
       "a3ComSysEthernetPortRateByteTransmitRate": a3ComSysEthernetPortRateByteTransmitRate,
       "a3ComSysEthernetPortRatePeakByteTransmitRate": a3ComSysEthernetPortRatePeakByteTransmitRate,
       "a3ComSysEthernetPortRateFrameTransmitRate": a3ComSysEthernetPortRateFrameTransmitRate,
       "a3ComSysEthernetPortRatePeakFrameTransmitRate": a3ComSysEthernetPortRatePeakFrameTransmitRate,
       "a3ComSysSmt": a3ComSysSmt,
       "a3ComSysSmtCount": a3ComSysSmtCount,
       "a3ComSysSmtFddiMacBeaconTable": a3ComSysSmtFddiMacBeaconTable,
       "a3ComSysSmtFddiMacBeaconEntry": a3ComSysSmtFddiMacBeaconEntry,
       "a3ComSysSmtFddiMacBeaconSmtIndex": a3ComSysSmtFddiMacBeaconSmtIndex,
       "a3ComSysSmtFddiMacBeaconIndex": a3ComSysSmtFddiMacBeaconIndex,
       "a3ComSysSmtFddiMacBeaconHistory": a3ComSysSmtFddiMacBeaconHistory,
       "a3ComSysSmtFddiMacRateTable": a3ComSysSmtFddiMacRateTable,
       "a3ComSysSmtFddiMacRateEntry": a3ComSysSmtFddiMacRateEntry,
       "a3ComSysSmtFddiMacRateSmtIndex": a3ComSysSmtFddiMacRateSmtIndex,
       "a3ComSysSmtFddiMacRateIndex": a3ComSysSmtFddiMacRateIndex,
       "a3ComSysSmtFddiMacRateByteReceiveRate": a3ComSysSmtFddiMacRateByteReceiveRate,
       "a3ComSysSmtFddiMacRatePeakByteReceiveRate": a3ComSysSmtFddiMacRatePeakByteReceiveRate,
       "a3ComSysSmtFddiMacRateFrameReceiveRate": a3ComSysSmtFddiMacRateFrameReceiveRate,
       "a3ComSysSmtFddiMacRatePeakFrameReceiveRate": a3ComSysSmtFddiMacRatePeakFrameReceiveRate,
       "a3ComSysSmtFddiMacRateByteTransmitRate": a3ComSysSmtFddiMacRateByteTransmitRate,
       "a3ComSysSmtFddiMacRatePeakByteTransmitRate": a3ComSysSmtFddiMacRatePeakByteTransmitRate,
       "a3ComSysSmtFddiMacRateFrameTransmitRate": a3ComSysSmtFddiMacRateFrameTransmitRate,
       "a3ComSysSmtFddiMacRatePeakFrameTransmitRate": a3ComSysSmtFddiMacRatePeakFrameTransmitRate,
       "a3ComSysSmtFddiPortTable": a3ComSysSmtFddiPortTable,
       "a3ComSysSmtFddiPortEntry": a3ComSysSmtFddiPortEntry,
       "a3ComSysSmtFddiPortSmtIndex": a3ComSysSmtFddiPortSmtIndex,
       "a3ComSysSmtFddiPortIndex": a3ComSysSmtFddiPortIndex,
       "a3ComSysSmtFddiPortLocationType": a3ComSysSmtFddiPortLocationType,
       "a3ComSysSmtFddiPortLocationTypeIndex": a3ComSysSmtFddiPortLocationTypeIndex,
       "a3ComSysSmtFddiPortLocationLocalIndex": a3ComSysSmtFddiPortLocationLocalIndex,
       "a3ComSysSmtFddiPortLabel": a3ComSysSmtFddiPortLabel,
       "a3ComSysSmtFddiMacLocationTable": a3ComSysSmtFddiMacLocationTable,
       "a3ComSysSmtFddiMacLocationEntry": a3ComSysSmtFddiMacLocationEntry,
       "a3ComSysSmtFddiMacLocationSmtIndex": a3ComSysSmtFddiMacLocationSmtIndex,
       "a3ComSysSmtFddiMacLocationIndex": a3ComSysSmtFddiMacLocationIndex,
       "a3ComSysSmtFddiMacCurrentLocation": a3ComSysSmtFddiMacCurrentLocation,
       "a3ComSysSmtFddiMacRequestedLocation": a3ComSysSmtFddiMacRequestedLocation,
       "a3ComSysSmtFddiMacAvailableLocation": a3ComSysSmtFddiMacAvailableLocation,
       "a3ComSysSmtFddiMacStationTable": a3ComSysSmtFddiMacStationTable,
       "a3ComSysSmtFddiMacStationEntry": a3ComSysSmtFddiMacStationEntry,
       "a3ComSysSmtFddiMacStationSmtIndex": a3ComSysSmtFddiMacStationSmtIndex,
       "a3ComSysSmtFddiMacStationIndex": a3ComSysSmtFddiMacStationIndex,
       "a3ComSysSmtFddiMacCurrentStation": a3ComSysSmtFddiMacCurrentStation,
       "a3ComSysSmtFddiMacRequestedStation": a3ComSysSmtFddiMacRequestedStation,
       "a3ComSysSmtFddiMacAvailableStations": a3ComSysSmtFddiMacAvailableStations,
       "a3ComSysSmtFddiPortStationTable": a3ComSysSmtFddiPortStationTable,
       "a3ComSysSmtFddiPortStationEntry": a3ComSysSmtFddiPortStationEntry,
       "a3ComSysSmtFddiPortStationSmtIndex": a3ComSysSmtFddiPortStationSmtIndex,
       "a3ComSysSmtFddiPortStationIndex": a3ComSysSmtFddiPortStationIndex,
       "a3ComSysSmtFddiPortCurrentStation": a3ComSysSmtFddiPortCurrentStation,
       "a3ComSysSmtFddiPortRequestedStation": a3ComSysSmtFddiPortRequestedStation,
       "a3ComSysSmtFddiPortAvailableStations": a3ComSysSmtFddiPortAvailableStations,
       "a3ComSysBridge": a3ComSysBridge,
       "a3ComSysBridgeCount": a3ComSysBridgeCount,
       "a3ComSysBridgeTable": a3ComSysBridgeTable,
       "a3ComSysBridgeEntry": a3ComSysBridgeEntry,
       "a3ComSysBridgeIndex": a3ComSysBridgeIndex,
       "a3ComSysBridgePortCount": a3ComSysBridgePortCount,
       "a3ComSysBridgeAddressTableSize": a3ComSysBridgeAddressTableSize,
       "a3ComSysBridgeAddressTableCount": a3ComSysBridgeAddressTableCount,
       "a3ComSysBridgeAddressTablePeakCount": a3ComSysBridgeAddressTablePeakCount,
       "a3ComSysBridgeAddressThreshold": a3ComSysBridgeAddressThreshold,
       "a3ComSysBridgeMode": a3ComSysBridgeMode,
       "a3ComSysBridgeBackbonePort": a3ComSysBridgeBackbonePort,
       "a3ComSysBridgeIpFragmentationEnabled": a3ComSysBridgeIpFragmentationEnabled,
       "a3ComSysBridgeTrFddiTranslationMode": a3ComSysBridgeTrFddiTranslationMode,
       "a3ComSysBridgeSTPGroupAddress": a3ComSysBridgeSTPGroupAddress,
       "a3ComSysBridgeSTPEnable": a3ComSysBridgeSTPEnable,
       "a3ComSysBridgeIpxSnapTranslationEnable": a3ComSysBridgeIpxSnapTranslationEnable,
       "a3ComSysBridgeLowLatencyEnable": a3ComSysBridgeLowLatencyEnable,
       "a3ComSysBridgeVlanMode": a3ComSysBridgeVlanMode,
       "a3ComSysBridgePortTable": a3ComSysBridgePortTable,
       "a3ComSysBridgePortEntry": a3ComSysBridgePortEntry,
       "a3ComSysBridgePortBridgeIndex": a3ComSysBridgePortBridgeIndex,
       "a3ComSysBridgePortIndex": a3ComSysBridgePortIndex,
       "a3ComSysBridgePortIfIndex": a3ComSysBridgePortIfIndex,
       "a3ComSysBridgePortReceiveMulticastLimit": a3ComSysBridgePortReceiveMulticastLimit,
       "a3ComSysBridgePortAddressAction": a3ComSysBridgePortAddressAction,
       "a3ComSysBridgePortSpanningTreeFrameReceivedCounts": a3ComSysBridgePortSpanningTreeFrameReceivedCounts,
       "a3ComSysBridgePortReceiveBlockedDiscards": a3ComSysBridgePortReceiveBlockedDiscards,
       "a3ComSysBridgePortReceiveMulticastLimitExceededs": a3ComSysBridgePortReceiveMulticastLimitExceededs,
       "a3ComSysBridgePortReceiveMulticastLimitExceededDiscards": a3ComSysBridgePortReceiveMulticastLimitExceededDiscards,
       "a3ComSysBridgePortReceiveSecurityDiscards": a3ComSysBridgePortReceiveSecurityDiscards,
       "a3ComSysBridgePortReceiveUnknownDiscards": a3ComSysBridgePortReceiveUnknownDiscards,
       "a3ComSysBridgePortReceiveOtherDiscards": a3ComSysBridgePortReceiveOtherDiscards,
       "a3ComSysBridgePortReceiveErrorDiscards": a3ComSysBridgePortReceiveErrorDiscards,
       "a3ComSysBridgePortSameSegmentDiscards": a3ComSysBridgePortSameSegmentDiscards,
       "a3ComSysBridgePortTransmitBlockedDiscards": a3ComSysBridgePortTransmitBlockedDiscards,
       "a3ComSysBridgePortReceiveAllPathFilteredFrames": a3ComSysBridgePortReceiveAllPathFilteredFrames,
       "a3ComSysBridgePortReceiveMulticastPathFilteredFrames": a3ComSysBridgePortReceiveMulticastPathFilteredFrames,
       "a3ComSysBridgePortTransmitAllPathFilteredFrames": a3ComSysBridgePortTransmitAllPathFilteredFrames,
       "a3ComSysBridgePortTransmitMulticastPathFilteredFrames": a3ComSysBridgePortTransmitMulticastPathFilteredFrames,
       "a3ComSysBridgePortForwardedUnicastFrames": a3ComSysBridgePortForwardedUnicastFrames,
       "a3ComSysBridgePortForwardedUnicastOctets": a3ComSysBridgePortForwardedUnicastOctets,
       "a3ComSysBridgePortForwardedMulticastFrames": a3ComSysBridgePortForwardedMulticastFrames,
       "a3ComSysBridgePortForwardedMulticastOctets": a3ComSysBridgePortForwardedMulticastOctets,
       "a3ComSysBridgePortFloodedUnicastFrames": a3ComSysBridgePortFloodedUnicastFrames,
       "a3ComSysBridgePortFloodedUnicastOctets": a3ComSysBridgePortFloodedUnicastOctets,
       "a3ComSysBridgePortStpMode": a3ComSysBridgePortStpMode,
       "a3ComSysBridgePortReceiveMulticastLimitFrameType": a3ComSysBridgePortReceiveMulticastLimitFrameType,
       "a3ComSysBridgePortForwardedFrames": a3ComSysBridgePortForwardedFrames,
       "a3ComSysBridgePortReceiveMulticastLimitMultiplier": a3ComSysBridgePortReceiveMulticastLimitMultiplier,
       "a3ComSysBridgePortAddressTable": a3ComSysBridgePortAddressTable,
       "a3ComSysBridgePortAddressEntry": a3ComSysBridgePortAddressEntry,
       "a3ComSysBridgePortAddressBridgeIndex": a3ComSysBridgePortAddressBridgeIndex,
       "a3ComSysBridgePortAddressPortIndex": a3ComSysBridgePortAddressPortIndex,
       "a3ComSysBridgePortAddressIndex": a3ComSysBridgePortAddressIndex,
       "a3ComSysBridgePortAddressRemoteAddress": a3ComSysBridgePortAddressRemoteAddress,
       "a3ComSysBridgePortAddressType": a3ComSysBridgePortAddressType,
       "a3ComSysBridgePortAddressIsStatic": a3ComSysBridgePortAddressIsStatic,
       "a3ComSysBridgePortAddressStaticPort": a3ComSysBridgePortAddressStaticPort,
       "a3ComSysBridgePortAddressAge": a3ComSysBridgePortAddressAge,
       "a3ComSysBridgeStpGroupAddress": a3ComSysBridgeStpGroupAddress,
       "a3ComSysBridgeStpEnable": a3ComSysBridgeStpEnable,
       "a3ComSysIpRouter": a3ComSysIpRouter,
       "a3ComSysNetworkMonitor": a3ComSysNetworkMonitor,
       "a3ComSysNetworkAnalyzerTable": a3ComSysNetworkAnalyzerTable,
       "a3ComSysNetworkAnalyzerTableEntry": a3ComSysNetworkAnalyzerTableEntry,
       "a3ComSysNetworkAnalyzerBridgeIndex": a3ComSysNetworkAnalyzerBridgeIndex,
       "a3ComSysNetworkAnalyzerBridgePortIndex": a3ComSysNetworkAnalyzerBridgePortIndex,
       "a3ComSysNetworkAnalyzerPhysicalAddress": a3ComSysNetworkAnalyzerPhysicalAddress,
       "a3ComSysNetworkAnalyzerStatus": a3ComSysNetworkAnalyzerStatus,
       "a3ComSysNetworkPortMonitorTable": a3ComSysNetworkPortMonitorTable,
       "a3ComSysNetworkPortMonitorTableEntry": a3ComSysNetworkPortMonitorTableEntry,
       "a3ComSysNetworkPortMonitorBridgeIndex": a3ComSysNetworkPortMonitorBridgeIndex,
       "a3ComSysNetworkPortMonitorBridgePortIndex": a3ComSysNetworkPortMonitorBridgePortIndex,
       "a3ComSysNetworkPortMonitorAnalyzerAddress": a3ComSysNetworkPortMonitorAnalyzerAddress,
       "a3ComSysNetworkPortMonitorStatus": a3ComSysNetworkPortMonitorStatus,
       "a3ComSysTokenRingPort": a3ComSysTokenRingPort,
       "a3ComSysTokenRingPortCount": a3ComSysTokenRingPortCount,
       "a3ComSysTokenRingPortTable": a3ComSysTokenRingPortTable,
       "a3ComSysTokenRingPortEntry": a3ComSysTokenRingPortEntry,
       "a3ComSysTokenRingPortIndex": a3ComSysTokenRingPortIndex,
       "a3ComSysTokenRingPortIfIndex": a3ComSysTokenRingPortIfIndex,
       "a3ComSysTokenRingPortLabel": a3ComSysTokenRingPortLabel,
       "a3ComSysTokenRingPortInsertStatus": a3ComSysTokenRingPortInsertStatus,
       "a3ComSysTokenRingPortType": a3ComSysTokenRingPortType,
       "a3ComSysTokenRingPortMode": a3ComSysTokenRingPortMode,
       "a3ComSysTokenRingPortSpeed": a3ComSysTokenRingPortSpeed,
       "a3ComSysTokenRingPortLineErrors": a3ComSysTokenRingPortLineErrors,
       "a3ComSysTokenRingPortBurstErrors": a3ComSysTokenRingPortBurstErrors,
       "a3ComSysTokenRingPortACErrors": a3ComSysTokenRingPortACErrors,
       "a3ComSysTokenRingPortAbortTransErrors": a3ComSysTokenRingPortAbortTransErrors,
       "a3ComSysTokenRingPortInternalErrors": a3ComSysTokenRingPortInternalErrors,
       "a3ComSysTokenRingPortLostFrameErrors": a3ComSysTokenRingPortLostFrameErrors,
       "a3ComSysTokenRingPortReceiveCongestionErrors": a3ComSysTokenRingPortReceiveCongestionErrors,
       "a3ComSysTokenRingPortFrameCopiedErrors": a3ComSysTokenRingPortFrameCopiedErrors,
       "a3ComSysTokenRingPortTokenErrors": a3ComSysTokenRingPortTokenErrors,
       "a3ComSysTokenRingPortSoftErrors": a3ComSysTokenRingPortSoftErrors,
       "a3ComSysTokenRingPortHardErrors": a3ComSysTokenRingPortHardErrors,
       "a3ComSysTokenRingPortTransmitBeacons": a3ComSysTokenRingPortTransmitBeacons,
       "a3ComSysTokenRingPortLobeWires": a3ComSysTokenRingPortLobeWires,
       "a3ComSysTokenRingPortRemoves": a3ComSysTokenRingPortRemoves,
       "a3ComSysTokenRingPortSingles": a3ComSysTokenRingPortSingles,
       "a3ComSysTokenRingPortFreqErrors": a3ComSysTokenRingPortFreqErrors,
       "a3ComSysTokenRingPortRingStatus": a3ComSysTokenRingPortRingStatus,
       "a3ComSysFtGroup": a3ComSysFtGroup,
       "a3ComSysFtTable": a3ComSysFtTable,
       "a3ComSysFtTableEntry": a3ComSysFtTableEntry,
       "a3ComSysFtIndex": a3ComSysFtIndex,
       "a3ComSysFtDirection": a3ComSysFtDirection,
       "a3ComSysFtLocalStorageType": a3ComSysFtLocalStorageType,
       "a3ComSysFtLocalResourceType": a3ComSysFtLocalResourceType,
       "a3ComSysFtLocalResourceMask": a3ComSysFtLocalResourceMask,
       "a3ComSysFtLocalResourceAttribute": a3ComSysFtLocalResourceAttribute,
       "a3ComSysFtRemoteAddressType": a3ComSysFtRemoteAddressType,
       "a3ComSysFtRemoteAddress": a3ComSysFtRemoteAddress,
       "a3ComSysFtRemoteFileName": a3ComSysFtRemoteFileName,
       "a3ComSysFtRemoteUserName": a3ComSysFtRemoteUserName,
       "a3ComSysFtRemoteUserPassword": a3ComSysFtRemoteUserPassword,
       "a3ComSysFtForceTransfer": a3ComSysFtForceTransfer,
       "a3ComSysFtBytesTransferred": a3ComSysFtBytesTransferred,
       "a3ComSysFtStatus": a3ComSysFtStatus,
       "a3ComSysFtDetailedStatus": a3ComSysFtDetailedStatus,
       "a3ComSysFtDetailedStatusString": a3ComSysFtDetailedStatusString,
       "a3ComSysFtOwnerString": a3ComSysFtOwnerString,
       "a3ComSysFtRowStatus": a3ComSysFtRowStatus,
       "a3ComSysFtResourceAttributes": a3ComSysFtResourceAttributes,
       "a3ComSysFtSystemAttributes": a3ComSysFtSystemAttributes,
       "a3ComSysFtSystemOperationalCode": a3ComSysFtSystemOperationalCode,
       "a3ComSysFtSystemConfiguration": a3ComSysFtSystemConfiguration,
       "a3ComSysFtSystemBridgeFilterCode": a3ComSysFtSystemBridgeFilterCode,
       "a3ComSysFtDetailedResourceStatus": a3ComSysFtDetailedResourceStatus,
       "a3ComSysFtSystemDetailedStatus": a3ComSysFtSystemDetailedStatus,
       "a3ComSysFtSysStatusNotApplicable": a3ComSysFtSysStatusNotApplicable,
       "a3ComSysFtSysStatusNoImageLabel": a3ComSysFtSysStatusNoImageLabel,
       "a3ComSysFtSysStatusConfigIdMismatch": a3ComSysFtSysStatusConfigIdMismatch,
       "a3ComSysFtSysStatusChecksumError": a3ComSysFtSysStatusChecksumError,
       "a3ComSysFtSysStatusNvRamError": a3ComSysFtSysStatusNvRamError,
       "a3ComSysFtSysStatusFlashError": a3ComSysFtSysStatusFlashError,
       "a3ComSysFtSysStatusNoRoom": a3ComSysFtSysStatusNoRoom,
       "a3ComSysFtSysBridgeFilterNotApplicable": a3ComSysFtSysBridgeFilterNotApplicable,
       "a3ComSysFtSysBridgeFilterSyntaxError": a3ComSysFtSysBridgeFilterSyntaxError,
       "a3ComSysFtSysBridgeFilterdownloadError": a3ComSysFtSysBridgeFilterdownloadError,
       "a3ComSysFtSysBridgeFilterNoRoom": a3ComSysFtSysBridgeFilterNoRoom,
       "a3ComSysIpGroup": a3ComSysIpGroup,
       "a3ComSysIpBaseGroup": a3ComSysIpBaseGroup,
       "a3ComSysIpInterfaceGroup": a3ComSysIpInterfaceGroup,
       "a3ComSysIpInterfaceCount": a3ComSysIpInterfaceCount,
       "a3ComSysIpInterfaceTable": a3ComSysIpInterfaceTable,
       "a3ComSysIpInterfaceEntry": a3ComSysIpInterfaceEntry,
       "a3ComSysIpInterfaceIpStackIndex": a3ComSysIpInterfaceIpStackIndex,
       "a3ComSysIpInterfaceAddr": a3ComSysIpInterfaceAddr,
       "a3ComSysIpInterfaceNetMask": a3ComSysIpInterfaceNetMask,
       "a3ComSysIpInterfaceIndex": a3ComSysIpInterfaceIndex,
       "a3ComSysIpInterfaceBcastAddr": a3ComSysIpInterfaceBcastAddr,
       "a3ComSysIpInterfaceCost": a3ComSysIpInterfaceCost,
       "a3ComSysIpInterfaceStatus": a3ComSysIpInterfaceStatus,
       "a3ComSysIpxGroup": a3ComSysIpxGroup,
       "a3ComSysIpxBaseGroup": a3ComSysIpxBaseGroup,
       "a3ComSysIpxInterfaceGroup": a3ComSysIpxInterfaceGroup,
       "a3ComSysIpxInterfaceCount": a3ComSysIpxInterfaceCount,
       "a3ComSysIpxInterfaceTable": a3ComSysIpxInterfaceTable,
       "a3ComSysIpxInterfaceEntry": a3ComSysIpxInterfaceEntry,
       "a3ComSysIpxInterfaceIpxStackIndex": a3ComSysIpxInterfaceIpxStackIndex,
       "a3ComSysIpxInterfaceNetNumber": a3ComSysIpxInterfaceNetNumber,
       "a3ComSysIpxInterfaceIfIndex": a3ComSysIpxInterfaceIfIndex,
       "a3ComSysIpxInterfaceCost": a3ComSysIpxInterfaceCost,
       "a3ComSysIpxInterfaceFrameType": a3ComSysIpxInterfaceFrameType,
       "a3ComSysIpxInterfaceStatus": a3ComSysIpxInterfaceStatus,
       "a3ComSysAppleTalkGroup": a3ComSysAppleTalkGroup,
       "a3ComSysAppleTalkBaseGroup": a3ComSysAppleTalkBaseGroup,
       "a3ComSysAppleTalkInterfaceGroup": a3ComSysAppleTalkInterfaceGroup,
       "a3ComSysAtInterfaceCount": a3ComSysAtInterfaceCount,
       "a3ComSysAtInterfaceTable": a3ComSysAtInterfaceTable,
       "a3ComSysAtInterfaceEntry": a3ComSysAtInterfaceEntry,
       "a3ComSysAtInterfaceAtStackIndex": a3ComSysAtInterfaceAtStackIndex,
       "a3ComSysAtInterfaceNetAddress": a3ComSysAtInterfaceNetAddress,
       "a3ComSysAtInterfaceType": a3ComSysAtInterfaceType,
       "a3ComSysAtInterfaceNetStart": a3ComSysAtInterfaceNetStart,
       "a3ComSysAtInterfaceNetEnd": a3ComSysAtInterfaceNetEnd,
       "a3ComSysAtInterfaceZoneDefault": a3ComSysAtInterfaceZoneDefault,
       "a3ComSysAtInterfaceZone1": a3ComSysAtInterfaceZone1,
       "a3ComSysAtInterfaceZone2": a3ComSysAtInterfaceZone2,
       "a3ComSysAtInterfaceZone3": a3ComSysAtInterfaceZone3,
       "a3ComSysAtInterfaceZone4": a3ComSysAtInterfaceZone4,
       "a3ComSysAtInterfaceZone5": a3ComSysAtInterfaceZone5,
       "a3ComSysAtInterfaceZone6": a3ComSysAtInterfaceZone6,
       "a3ComSysAtInterfaceZone7": a3ComSysAtInterfaceZone7,
       "a3ComSysAtInterfaceZone8": a3ComSysAtInterfaceZone8,
       "a3ComSysAtInterfaceZone9": a3ComSysAtInterfaceZone9,
       "a3ComSysAtInterfaceZone10": a3ComSysAtInterfaceZone10,
       "a3ComSysAtInterfaceZone11": a3ComSysAtInterfaceZone11,
       "a3ComSysAtInterfaceZone12": a3ComSysAtInterfaceZone12,
       "a3ComSysAtInterfaceZone13": a3ComSysAtInterfaceZone13,
       "a3ComSysAtInterfaceZone14": a3ComSysAtInterfaceZone14,
       "a3ComSysAtInterfaceZone15": a3ComSysAtInterfaceZone15,
       "a3ComSysAtInterfaceIfIndex": a3ComSysAtInterfaceIfIndex,
       "a3ComSysAtInterfaceState": a3ComSysAtInterfaceState,
       "a3ComSysAtInterfaceStatus": a3ComSysAtInterfaceStatus,
       "a3ComSysModuleCardGroup": a3ComSysModuleCardGroup,
       "a3ComSysModuleCardCount": a3ComSysModuleCardCount,
       "a3ComSysModuleCardInfoTable": a3ComSysModuleCardInfoTable,
       "a3ComSysModuleCardInfoEntry": a3ComSysModuleCardInfoEntry,
       "a3ComSysModuleCardInfoIndex": a3ComSysModuleCardInfoIndex,
       "a3ComSysModuleCardInfoFamily": a3ComSysModuleCardInfoFamily,
       "a3ComSysModuleCardInfoGenericType": a3ComSysModuleCardInfoGenericType,
       "a3ComSysModuleCardInfoSpecificType": a3ComSysModuleCardInfoSpecificType,
       "a3ComSysModuleCardInfoPartNumber": a3ComSysModuleCardInfoPartNumber,
       "a3ComSysModuleCardInfoManufacturingDate": a3ComSysModuleCardInfoManufacturingDate,
       "a3ComSysModuleCardInfoModuleSerialNumber": a3ComSysModuleCardInfoModuleSerialNumber,
       "a3ComSysModuleCardInfoTLASerialNumber": a3ComSysModuleCardInfoTLASerialNumber,
       "a3ComSysModuleCardInfo3CNumber": a3ComSysModuleCardInfo3CNumber,
       "a3ComSysModuleCardInfoICTTestStatus": a3ComSysModuleCardInfoICTTestStatus,
       "a3ComSysModuleCardInfoICTTestRevision": a3ComSysModuleCardInfoICTTestRevision,
       "a3ComSysModuleCardInfoSystemTestStatus": a3ComSysModuleCardInfoSystemTestStatus,
       "a3ComSysModuleCardInfoFunctionalTestStatus": a3ComSysModuleCardInfoFunctionalTestStatus,
       "a3ComSysModuleCardInfoFunctionalTestRevision": a3ComSysModuleCardInfoFunctionalTestRevision,
       "a3ComSysModuleCardInfoBoardRevision": a3ComSysModuleCardInfoBoardRevision,
       "a3ComSysModuleCardInfoRuntimeHours": a3ComSysModuleCardInfoRuntimeHours,
       "a3ComSysDiagnosticsGroup": a3ComSysDiagnosticsGroup,
       "a3ComSysDiagnosticsInfoTable": a3ComSysDiagnosticsInfoTable,
       "a3ComSysDiagnosticsInfoEntry": a3ComSysDiagnosticsInfoEntry,
       "a3ComSysDiagnosticsInfoIndex": a3ComSysDiagnosticsInfoIndex,
       "a3ComSysDiagnosticsInfoPOVDiagnosticsRevision": a3ComSysDiagnosticsInfoPOVDiagnosticsRevision,
       "a3ComSysDiagnosticsInfoExtendedDiagnosticsRevision": a3ComSysDiagnosticsInfoExtendedDiagnosticsRevision,
       "a3ComSysDiagnosticsInfoDiagnosticFailureCode": a3ComSysDiagnosticsInfoDiagnosticFailureCode,
       "a3ComSysDiagnosticsInfoDiagnosticFailureDateTime": a3ComSysDiagnosticsInfoDiagnosticFailureDateTime,
       "a3ComSysDiagnosticsInfoDiagnosticFailureSlotNumber": a3ComSysDiagnosticsInfoDiagnosticFailureSlotNumber,
       "a3ComSysDiagnosticsInfoDiagnosticFailureCounter": a3ComSysDiagnosticsInfoDiagnosticFailureCounter,
       "a3ComSysDiagnosticsInfoDiagnosticFieldDOACounter": a3ComSysDiagnosticsInfoDiagnosticFieldDOACounter,
       "switchingSystemsFddiMibGroups": switchingSystemsFddiMibGroups}
)
