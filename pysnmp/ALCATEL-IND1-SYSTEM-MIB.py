# SNMP MIB module (ALCATEL-IND1-SYSTEM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALCATEL-IND1-SYSTEM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:36:30 2024
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

(hardentIND1System,) = mibBuilder.importSymbols(
    "ALCATEL-IND1-BASE",
    "hardentIND1System")

(Ipv6Address,) = mibBuilder.importSymbols(
    "IPV6-TC",
    "Ipv6Address")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

alcatelIND1SystemMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1)
)
alcatelIND1SystemMIB.setRevisions(
        ("2011-01-23 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class SystemFileType(Integer32, TextualConvention):
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
        *(("directory", 2),
          ("file", 1),
          ("tarArchive", 4),
          ("undefined", 3))
    )



class SwitchLoggingIndex(Integer32, TextualConvention):
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
        *(("console", 1),
          ("flash", 2),
          ("ipaddr", 4),
          ("socket", 3))
    )



class AppIdIndex(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 254),
    )



class Enable(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )



class FileSystemIndex(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("flash", 1),
          ("uflash", 2))
    )



class SeverityLevel(Integer32, TextualConvention):
    status = "current"
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
        *(("severityLevelAlarm", 1),
          ("severityLevelAlert", 3),
          ("severityLevelDbg1", 6),
          ("severityLevelDbg2", 7),
          ("severityLevelDbg3", 8),
          ("severityLevelError", 2),
          ("severityLevelInfo", 5),
          ("severityLevelOff", 0),
          ("severityLevelWarn", 4))
    )



class SysLogFacilityId(Integer32, TextualConvention):
    status = "current"
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
        *(("clock1", 23),
          ("clock2", 22),
          ("ftp", 21),
          ("kernel", 20),
          ("local0", 19),
          ("local1", 18),
          ("local2", 17),
          ("local3", 16),
          ("local4", 15),
          ("local5", 14),
          ("local6", 13),
          ("local7", 12),
          ("logAlert", 11),
          ("logAudit", 10),
          ("lptr", 9),
          ("mail", 8),
          ("netNews", 7),
          ("ntp", 6),
          ("secAuth1", 5),
          ("secAuth2", 4),
          ("syslog", 3),
          ("system", 2),
          ("user", 1),
          ("uucp", 0))
    )



class CommandPercentComplete(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )



class VrfId(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )



class AgeLimit(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )



# MIB Managed Objects in the order of their OIDs

_AlcatelIND1SystemMIBObjects_ObjectIdentity = ObjectIdentity
alcatelIND1SystemMIBObjects = _AlcatelIND1SystemMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1SystemMIBObjects.setStatus("current")
_SystemMicrocode_ObjectIdentity = ObjectIdentity
systemMicrocode = _SystemMicrocode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 1)
)
_SystemMicrocodePackageTable_Object = MibTable
systemMicrocodePackageTable = _SystemMicrocodePackageTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    systemMicrocodePackageTable.setStatus("current")
_SystemMicrocodePackageEntry_Object = MibTableRow
systemMicrocodePackageEntry = _SystemMicrocodePackageEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 1, 1, 1)
)
systemMicrocodePackageEntry.setIndexNames(
    (0, "ALCATEL-IND1-SYSTEM-MIB", "systemMicrocodePackageDirectoryIndex"),
    (0, "ALCATEL-IND1-SYSTEM-MIB", "systemMicrocodePackageDirectory"),
    (0, "ALCATEL-IND1-SYSTEM-MIB", "systemMicrocodePackageIndex"),
)
if mibBuilder.loadTexts:
    systemMicrocodePackageEntry.setStatus("current")
_SystemMicrocodePackageDirectoryIndex_Type = Unsigned32
_SystemMicrocodePackageDirectoryIndex_Object = MibTableColumn
systemMicrocodePackageDirectoryIndex = _SystemMicrocodePackageDirectoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1),
    _SystemMicrocodePackageDirectoryIndex_Type()
)
systemMicrocodePackageDirectoryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    systemMicrocodePackageDirectoryIndex.setStatus("current")


class _SystemMicrocodePackageDirectory_Type(SnmpAdminString):
    """Custom type systemMicrocodePackageDirectory based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 108),
    )


_SystemMicrocodePackageDirectory_Type.__name__ = "SnmpAdminString"
_SystemMicrocodePackageDirectory_Object = MibTableColumn
systemMicrocodePackageDirectory = _SystemMicrocodePackageDirectory_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2),
    _SystemMicrocodePackageDirectory_Type()
)
systemMicrocodePackageDirectory.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    systemMicrocodePackageDirectory.setStatus("current")
_SystemMicrocodePackageIndex_Type = Unsigned32
_SystemMicrocodePackageIndex_Object = MibTableColumn
systemMicrocodePackageIndex = _SystemMicrocodePackageIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 1, 1, 1, 3),
    _SystemMicrocodePackageIndex_Type()
)
systemMicrocodePackageIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    systemMicrocodePackageIndex.setStatus("current")


class _SystemMicrocodePackageVersion_Type(SnmpAdminString):
    """Custom type systemMicrocodePackageVersion based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SystemMicrocodePackageVersion_Type.__name__ = "SnmpAdminString"
_SystemMicrocodePackageVersion_Object = MibTableColumn
systemMicrocodePackageVersion = _SystemMicrocodePackageVersion_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 1, 1, 1, 4),
    _SystemMicrocodePackageVersion_Type()
)
systemMicrocodePackageVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemMicrocodePackageVersion.setStatus("current")


class _SystemMicrocodePackageName_Type(SnmpAdminString):
    """Custom type systemMicrocodePackageName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SystemMicrocodePackageName_Type.__name__ = "SnmpAdminString"
_SystemMicrocodePackageName_Object = MibTableColumn
systemMicrocodePackageName = _SystemMicrocodePackageName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 1, 1, 1, 5),
    _SystemMicrocodePackageName_Type()
)
systemMicrocodePackageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemMicrocodePackageName.setStatus("current")


class _SystemMicrocodePackageDescription_Type(SnmpAdminString):
    """Custom type systemMicrocodePackageDescription based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SystemMicrocodePackageDescription_Type.__name__ = "SnmpAdminString"
_SystemMicrocodePackageDescription_Object = MibTableColumn
systemMicrocodePackageDescription = _SystemMicrocodePackageDescription_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 1, 1, 1, 6),
    _SystemMicrocodePackageDescription_Type()
)
systemMicrocodePackageDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemMicrocodePackageDescription.setStatus("current")


class _SystemMicrocodePackageStatus_Type(Integer32):
    """Custom type systemMicrocodePackageStatus based on Integer32"""
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
        *(("inuse", 3),
          ("ok", 2),
          ("undefined", 1))
    )


_SystemMicrocodePackageStatus_Type.__name__ = "Integer32"
_SystemMicrocodePackageStatus_Object = MibTableColumn
systemMicrocodePackageStatus = _SystemMicrocodePackageStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 1, 1, 1, 7),
    _SystemMicrocodePackageStatus_Type()
)
systemMicrocodePackageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemMicrocodePackageStatus.setStatus("current")


class _SystemMicrocodePackageSize_Type(Unsigned32):
    """Custom type systemMicrocodePackageSize based on Unsigned32"""
    defaultValue = 0


_SystemMicrocodePackageSize_Object = MibTableColumn
systemMicrocodePackageSize = _SystemMicrocodePackageSize_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 1, 1, 1, 8),
    _SystemMicrocodePackageSize_Type()
)
systemMicrocodePackageSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemMicrocodePackageSize.setStatus("current")
_SystemBootParams_ObjectIdentity = ObjectIdentity
systemBootParams = _SystemBootParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 2)
)
_SystemBootNetwork_Type = IpAddress
_SystemBootNetwork_Object = MibScalar
systemBootNetwork = _SystemBootNetwork_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 2, 1),
    _SystemBootNetwork_Type()
)
systemBootNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemBootNetwork.setStatus("current")
_SystemBootNetworkGateway_Type = IpAddress
_SystemBootNetworkGateway_Object = MibScalar
systemBootNetworkGateway = _SystemBootNetworkGateway_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 2, 2),
    _SystemBootNetworkGateway_Type()
)
systemBootNetworkGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemBootNetworkGateway.setStatus("current")
_SystemBootNetworkNetmask_Type = IpAddress
_SystemBootNetworkNetmask_Object = MibScalar
systemBootNetworkNetmask = _SystemBootNetworkNetmask_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 2, 3),
    _SystemBootNetworkNetmask_Type()
)
systemBootNetworkNetmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemBootNetworkNetmask.setStatus("current")
_SystemHardware_ObjectIdentity = ObjectIdentity
systemHardware = _SystemHardware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 3)
)


class _SystemHardwareFlashMfg_Type(Integer32):
    """Custom type systemHardwareFlashMfg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              7,
              8,
              9,
              10,
              13)
        )
    )
    namedValues = NamedValues(
        *(("amd", 2),
          ("atmel", 4),
          ("intel", 3),
          ("other", 1),
          ("sandisk", 8),
          ("spansion", 10),
          ("sst", 9),
          ("toshiba", 7),
          ("wintec", 13))
    )


_SystemHardwareFlashMfg_Type.__name__ = "Integer32"
_SystemHardwareFlashMfg_Object = MibScalar
systemHardwareFlashMfg = _SystemHardwareFlashMfg_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 3, 1),
    _SystemHardwareFlashMfg_Type()
)
systemHardwareFlashMfg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemHardwareFlashMfg.setStatus("current")
_SystemHardwareFlashSize_Type = Unsigned32
_SystemHardwareFlashSize_Object = MibScalar
systemHardwareFlashSize = _SystemHardwareFlashSize_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 3, 2),
    _SystemHardwareFlashSize_Type()
)
systemHardwareFlashSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemHardwareFlashSize.setStatus("current")


class _SystemHardwareMemoryMfg_Type(Integer32):
    """Custom type systemHardwareMemoryMfg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("amd", 2),
          ("atmel", 4),
          ("dataram", 10),
          ("intel", 3),
          ("interward", 11),
          ("kingston", 6),
          ("micron", 5),
          ("notreadable", 12),
          ("other", 1))
    )


_SystemHardwareMemoryMfg_Type.__name__ = "Integer32"
_SystemHardwareMemoryMfg_Object = MibScalar
systemHardwareMemoryMfg = _SystemHardwareMemoryMfg_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 3, 3),
    _SystemHardwareMemoryMfg_Type()
)
systemHardwareMemoryMfg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemHardwareMemoryMfg.setStatus("current")
_SystemHardwareMemorySize_Type = Unsigned32
_SystemHardwareMemorySize_Object = MibScalar
systemHardwareMemorySize = _SystemHardwareMemorySize_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 3, 4),
    _SystemHardwareMemorySize_Type()
)
systemHardwareMemorySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemHardwareMemorySize.setStatus("current")
_SystemHardwareNVRAMBatteryLow_Type = TruthValue
_SystemHardwareNVRAMBatteryLow_Object = MibScalar
systemHardwareNVRAMBatteryLow = _SystemHardwareNVRAMBatteryLow_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 3, 5),
    _SystemHardwareNVRAMBatteryLow_Type()
)
systemHardwareNVRAMBatteryLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemHardwareNVRAMBatteryLow.setStatus("current")


class _SystemHardwareBootCpuType_Type(Integer32):
    """Custom type systemHardwareBootCpuType based on Integer32"""
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
        *(("other", 1),
          ("ppc", 4),
          ("ppc8540", 5),
          ("ppc8572", 6),
          ("sparc380", 2),
          ("sparcV9", 3))
    )


_SystemHardwareBootCpuType_Type.__name__ = "Integer32"
_SystemHardwareBootCpuType_Object = MibScalar
systemHardwareBootCpuType = _SystemHardwareBootCpuType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 3, 6),
    _SystemHardwareBootCpuType_Type()
)
systemHardwareBootCpuType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemHardwareBootCpuType.setStatus("current")


class _SystemHardwareJumperInterruptBoot_Type(TruthValue):
    """Custom type systemHardwareJumperInterruptBoot based on TruthValue"""


_SystemHardwareJumperInterruptBoot_Object = MibScalar
systemHardwareJumperInterruptBoot = _SystemHardwareJumperInterruptBoot_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 3, 7),
    _SystemHardwareJumperInterruptBoot_Type()
)
systemHardwareJumperInterruptBoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemHardwareJumperInterruptBoot.setStatus("current")


class _SystemHardwareJumperForceUartDefaults_Type(TruthValue):
    """Custom type systemHardwareJumperForceUartDefaults based on TruthValue"""


_SystemHardwareJumperForceUartDefaults_Object = MibScalar
systemHardwareJumperForceUartDefaults = _SystemHardwareJumperForceUartDefaults_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 3, 8),
    _SystemHardwareJumperForceUartDefaults_Type()
)
systemHardwareJumperForceUartDefaults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemHardwareJumperForceUartDefaults.setStatus("current")


class _SystemHardwareJumperRunExtendedMemoryDiagnostics_Type(TruthValue):
    """Custom type systemHardwareJumperRunExtendedMemoryDiagnostics based on TruthValue"""


_SystemHardwareJumperRunExtendedMemoryDiagnostics_Object = MibScalar
systemHardwareJumperRunExtendedMemoryDiagnostics = _SystemHardwareJumperRunExtendedMemoryDiagnostics_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 3, 9),
    _SystemHardwareJumperRunExtendedMemoryDiagnostics_Type()
)
systemHardwareJumperRunExtendedMemoryDiagnostics.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemHardwareJumperRunExtendedMemoryDiagnostics.setStatus("current")


class _SystemHardwareJumperSpare_Type(TruthValue):
    """Custom type systemHardwareJumperSpare based on TruthValue"""


_SystemHardwareJumperSpare_Object = MibScalar
systemHardwareJumperSpare = _SystemHardwareJumperSpare_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 3, 10),
    _SystemHardwareJumperSpare_Type()
)
systemHardwareJumperSpare.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemHardwareJumperSpare.setStatus("current")
_SystemHardwareFpgaVersionTable_Object = MibTable
systemHardwareFpgaVersionTable = _SystemHardwareFpgaVersionTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 3, 11)
)
if mibBuilder.loadTexts:
    systemHardwareFpgaVersionTable.setStatus("current")
_SystemHardwareFpgaVersionEntry_Object = MibTableRow
systemHardwareFpgaVersionEntry = _SystemHardwareFpgaVersionEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 3, 11, 1)
)
systemHardwareFpgaVersionEntry.setIndexNames(
    (0, "ALCATEL-IND1-SYSTEM-MIB", "systemHardwareFpgaVersionIndex"),
)
if mibBuilder.loadTexts:
    systemHardwareFpgaVersionEntry.setStatus("current")


class _SystemHardwareFpgaVersionIndex_Type(Integer32):
    """Custom type systemHardwareFpgaVersionIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_SystemHardwareFpgaVersionIndex_Type.__name__ = "Integer32"
_SystemHardwareFpgaVersionIndex_Object = MibTableColumn
systemHardwareFpgaVersionIndex = _SystemHardwareFpgaVersionIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 3, 11, 1, 1),
    _SystemHardwareFpgaVersionIndex_Type()
)
systemHardwareFpgaVersionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemHardwareFpgaVersionIndex.setStatus("current")
_SystemHardwareFpgaVersion_Type = Unsigned32
_SystemHardwareFpgaVersion_Object = MibTableColumn
systemHardwareFpgaVersion = _SystemHardwareFpgaVersion_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 3, 11, 1, 2),
    _SystemHardwareFpgaVersion_Type()
)
systemHardwareFpgaVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemHardwareFpgaVersion.setStatus("current")


class _SystemHardwareBootRomVersion_Type(SnmpAdminString):
    """Custom type systemHardwareBootRomVersion based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SystemHardwareBootRomVersion_Type.__name__ = "SnmpAdminString"
_SystemHardwareBootRomVersion_Object = MibScalar
systemHardwareBootRomVersion = _SystemHardwareBootRomVersion_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 3, 12),
    _SystemHardwareBootRomVersion_Type()
)
systemHardwareBootRomVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemHardwareBootRomVersion.setStatus("current")


class _SystemHardwareBackupMiniBootVersion_Type(SnmpAdminString):
    """Custom type systemHardwareBackupMiniBootVersion based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SystemHardwareBackupMiniBootVersion_Type.__name__ = "SnmpAdminString"
_SystemHardwareBackupMiniBootVersion_Object = MibScalar
systemHardwareBackupMiniBootVersion = _SystemHardwareBackupMiniBootVersion_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 3, 13),
    _SystemHardwareBackupMiniBootVersion_Type()
)
systemHardwareBackupMiniBootVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemHardwareBackupMiniBootVersion.setStatus("current")


class _SystemHardwareDefaultMiniBootVersion_Type(SnmpAdminString):
    """Custom type systemHardwareDefaultMiniBootVersion based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SystemHardwareDefaultMiniBootVersion_Type.__name__ = "SnmpAdminString"
_SystemHardwareDefaultMiniBootVersion_Object = MibScalar
systemHardwareDefaultMiniBootVersion = _SystemHardwareDefaultMiniBootVersion_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 3, 14),
    _SystemHardwareDefaultMiniBootVersion_Type()
)
systemHardwareDefaultMiniBootVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemHardwareDefaultMiniBootVersion.setStatus("current")


class _SystemHardwareMinorFpgaVersion_Type(SnmpAdminString):
    """Custom type systemHardwareMinorFpgaVersion based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SystemHardwareMinorFpgaVersion_Type.__name__ = "SnmpAdminString"
_SystemHardwareMinorFpgaVersion_Object = MibScalar
systemHardwareMinorFpgaVersion = _SystemHardwareMinorFpgaVersion_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 3, 15),
    _SystemHardwareMinorFpgaVersion_Type()
)
systemHardwareMinorFpgaVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemHardwareMinorFpgaVersion.setStatus("current")


class _SystemHardwareCpldVersion_Type(SnmpAdminString):
    """Custom type systemHardwareCpldVersion based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SystemHardwareCpldVersion_Type.__name__ = "SnmpAdminString"
_SystemHardwareCpldVersion_Object = MibScalar
systemHardwareCpldVersion = _SystemHardwareCpldVersion_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 3, 16),
    _SystemHardwareCpldVersion_Type()
)
systemHardwareCpldVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemHardwareCpldVersion.setStatus("current")


class _SystemHardwareUbootVersion_Type(SnmpAdminString):
    """Custom type systemHardwareUbootVersion based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SystemHardwareUbootVersion_Type.__name__ = "SnmpAdminString"
_SystemHardwareUbootVersion_Object = MibScalar
systemHardwareUbootVersion = _SystemHardwareUbootVersion_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 3, 17),
    _SystemHardwareUbootVersion_Type()
)
systemHardwareUbootVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemHardwareUbootVersion.setStatus("current")


class _SystemHardwareProdRegId_Type(SnmpAdminString):
    """Custom type systemHardwareProdRegId based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SystemHardwareProdRegId_Type.__name__ = "SnmpAdminString"
_SystemHardwareProdRegId_Object = MibScalar
systemHardwareProdRegId = _SystemHardwareProdRegId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 3, 18),
    _SystemHardwareProdRegId_Type()
)
systemHardwareProdRegId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemHardwareProdRegId.setStatus("current")


class _SystemHardwareRevisionRegister_Type(SnmpAdminString):
    """Custom type systemHardwareRevisionRegister based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SystemHardwareRevisionRegister_Type.__name__ = "SnmpAdminString"
_SystemHardwareRevisionRegister_Object = MibScalar
systemHardwareRevisionRegister = _SystemHardwareRevisionRegister_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 3, 19),
    _SystemHardwareRevisionRegister_Type()
)
systemHardwareRevisionRegister.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemHardwareRevisionRegister.setStatus("current")


class _SystemHardwareXfpId_Type(SnmpAdminString):
    """Custom type systemHardwareXfpId based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SystemHardwareXfpId_Type.__name__ = "SnmpAdminString"
_SystemHardwareXfpId_Object = MibScalar
systemHardwareXfpId = _SystemHardwareXfpId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 3, 20),
    _SystemHardwareXfpId_Type()
)
systemHardwareXfpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemHardwareXfpId.setStatus("current")


class _SystemHardwareUbootMinibootVersion_Type(SnmpAdminString):
    """Custom type systemHardwareUbootMinibootVersion based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SystemHardwareUbootMinibootVersion_Type.__name__ = "SnmpAdminString"
_SystemHardwareUbootMinibootVersion_Object = MibScalar
systemHardwareUbootMinibootVersion = _SystemHardwareUbootMinibootVersion_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 3, 21),
    _SystemHardwareUbootMinibootVersion_Type()
)
systemHardwareUbootMinibootVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemHardwareUbootMinibootVersion.setStatus("current")
_SystemFileSystem_ObjectIdentity = ObjectIdentity
systemFileSystem = _SystemFileSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 4)
)
_SystemFileSystemTable_Object = MibTable
systemFileSystemTable = _SystemFileSystemTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    systemFileSystemTable.setStatus("current")
_SystemFileSystemEntry_Object = MibTableRow
systemFileSystemEntry = _SystemFileSystemEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 4, 1, 1)
)
systemFileSystemEntry.setIndexNames(
    (0, "ALCATEL-IND1-SYSTEM-MIB", "systemFileSystemIndex"),
)
if mibBuilder.loadTexts:
    systemFileSystemEntry.setStatus("current")
_SystemFileSystemIndex_Type = FileSystemIndex
_SystemFileSystemIndex_Object = MibTableColumn
systemFileSystemIndex = _SystemFileSystemIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 4, 1, 1, 1),
    _SystemFileSystemIndex_Type()
)
systemFileSystemIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemFileSystemIndex.setStatus("current")


class _SystemFileSystemName_Type(SnmpAdminString):
    """Custom type systemFileSystemName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SystemFileSystemName_Type.__name__ = "SnmpAdminString"
_SystemFileSystemName_Object = MibTableColumn
systemFileSystemName = _SystemFileSystemName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 4, 1, 1, 2),
    _SystemFileSystemName_Type()
)
systemFileSystemName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemFileSystemName.setStatus("current")


class _SystemFileSystemFreeSpace_Type(Unsigned32):
    """Custom type systemFileSystemFreeSpace based on Unsigned32"""
    defaultValue = 0


_SystemFileSystemFreeSpace_Object = MibTableColumn
systemFileSystemFreeSpace = _SystemFileSystemFreeSpace_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 4, 1, 1, 3),
    _SystemFileSystemFreeSpace_Type()
)
systemFileSystemFreeSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemFileSystemFreeSpace.setStatus("current")


class _SystemFileSystemDirectoryName_Type(SnmpAdminString):
    """Custom type systemFileSystemDirectoryName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SystemFileSystemDirectoryName_Type.__name__ = "SnmpAdminString"
_SystemFileSystemDirectoryName_Object = MibScalar
systemFileSystemDirectoryName = _SystemFileSystemDirectoryName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 4, 2),
    _SystemFileSystemDirectoryName_Type()
)
systemFileSystemDirectoryName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemFileSystemDirectoryName.setStatus("current")


class _SystemFileSystemDirectoryDateTime_Type(SnmpAdminString):
    """Custom type systemFileSystemDirectoryDateTime based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SystemFileSystemDirectoryDateTime_Type.__name__ = "SnmpAdminString"
_SystemFileSystemDirectoryDateTime_Object = MibScalar
systemFileSystemDirectoryDateTime = _SystemFileSystemDirectoryDateTime_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 4, 3),
    _SystemFileSystemDirectoryDateTime_Type()
)
systemFileSystemDirectoryDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemFileSystemDirectoryDateTime.setStatus("current")
_SystemFileSystemFileTable_Object = MibTable
systemFileSystemFileTable = _SystemFileSystemFileTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 4, 4)
)
if mibBuilder.loadTexts:
    systemFileSystemFileTable.setStatus("current")
_SystemFileSystemFileEntry_Object = MibTableRow
systemFileSystemFileEntry = _SystemFileSystemFileEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 4, 4, 1)
)
systemFileSystemFileEntry.setIndexNames(
    (0, "ALCATEL-IND1-SYSTEM-MIB", "systemFileSystemFileIndex"),
)
if mibBuilder.loadTexts:
    systemFileSystemFileEntry.setStatus("current")
_SystemFileSystemFileIndex_Type = Unsigned32
_SystemFileSystemFileIndex_Object = MibTableColumn
systemFileSystemFileIndex = _SystemFileSystemFileIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 4, 4, 1, 1),
    _SystemFileSystemFileIndex_Type()
)
systemFileSystemFileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemFileSystemFileIndex.setStatus("current")


class _SystemFileSystemFileName_Type(SnmpAdminString):
    """Custom type systemFileSystemFileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SystemFileSystemFileName_Type.__name__ = "SnmpAdminString"
_SystemFileSystemFileName_Object = MibTableColumn
systemFileSystemFileName = _SystemFileSystemFileName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 4, 4, 1, 2),
    _SystemFileSystemFileName_Type()
)
systemFileSystemFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemFileSystemFileName.setStatus("current")


class _SystemFileSystemFileType_Type(SystemFileType):
    """Custom type systemFileSystemFileType based on SystemFileType"""


_SystemFileSystemFileType_Object = MibTableColumn
systemFileSystemFileType = _SystemFileSystemFileType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 4, 4, 1, 3),
    _SystemFileSystemFileType_Type()
)
systemFileSystemFileType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemFileSystemFileType.setStatus("current")


class _SystemFileSystemFileSize_Type(Unsigned32):
    """Custom type systemFileSystemFileSize based on Unsigned32"""
    defaultValue = 0


_SystemFileSystemFileSize_Object = MibTableColumn
systemFileSystemFileSize = _SystemFileSystemFileSize_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 4, 4, 1, 4),
    _SystemFileSystemFileSize_Type()
)
systemFileSystemFileSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemFileSystemFileSize.setStatus("current")


class _SystemFileSystemFileAttr_Type(Integer32):
    """Custom type systemFileSystemFileAttr based on Integer32"""
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
        *(("readOnly", 2),
          ("readWrite", 3),
          ("undefined", 1),
          ("writeOnly", 4))
    )


_SystemFileSystemFileAttr_Type.__name__ = "Integer32"
_SystemFileSystemFileAttr_Object = MibTableColumn
systemFileSystemFileAttr = _SystemFileSystemFileAttr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 4, 4, 1, 5),
    _SystemFileSystemFileAttr_Type()
)
systemFileSystemFileAttr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemFileSystemFileAttr.setStatus("current")


class _SystemFileSystemFileDateTime_Type(SnmpAdminString):
    """Custom type systemFileSystemFileDateTime based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SystemFileSystemFileDateTime_Type.__name__ = "SnmpAdminString"
_SystemFileSystemFileDateTime_Object = MibTableColumn
systemFileSystemFileDateTime = _SystemFileSystemFileDateTime_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 4, 4, 1, 6),
    _SystemFileSystemFileDateTime_Type()
)
systemFileSystemFileDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemFileSystemFileDateTime.setStatus("current")
_SystemServices_ObjectIdentity = ObjectIdentity
systemServices = _SystemServices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 5)
)


class _SystemServicesDate_Type(SnmpAdminString):
    """Custom type systemServicesDate based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SystemServicesDate_Type.__name__ = "SnmpAdminString"
_SystemServicesDate_Object = MibScalar
systemServicesDate = _SystemServicesDate_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 5, 1),
    _SystemServicesDate_Type()
)
systemServicesDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemServicesDate.setStatus("current")


class _SystemServicesTime_Type(SnmpAdminString):
    """Custom type systemServicesTime based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SystemServicesTime_Type.__name__ = "SnmpAdminString"
_SystemServicesTime_Object = MibScalar
systemServicesTime = _SystemServicesTime_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 5, 2),
    _SystemServicesTime_Type()
)
systemServicesTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemServicesTime.setStatus("current")


class _SystemServicesTimezone_Type(SnmpAdminString):
    """Custom type systemServicesTimezone based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SystemServicesTimezone_Type.__name__ = "SnmpAdminString"
_SystemServicesTimezone_Object = MibScalar
systemServicesTimezone = _SystemServicesTimezone_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 5, 3),
    _SystemServicesTimezone_Type()
)
systemServicesTimezone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemServicesTimezone.setStatus("current")


class _SystemServicesTimezoneStartWeek_Type(Unsigned32):
    """Custom type systemServicesTimezoneStartWeek based on Unsigned32"""
    defaultValue = 0


_SystemServicesTimezoneStartWeek_Object = MibScalar
systemServicesTimezoneStartWeek = _SystemServicesTimezoneStartWeek_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 5, 4),
    _SystemServicesTimezoneStartWeek_Type()
)
systemServicesTimezoneStartWeek.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemServicesTimezoneStartWeek.setStatus("current")


class _SystemServicesTimezoneStartDay_Type(Unsigned32):
    """Custom type systemServicesTimezoneStartDay based on Unsigned32"""
    defaultValue = 0


_SystemServicesTimezoneStartDay_Object = MibScalar
systemServicesTimezoneStartDay = _SystemServicesTimezoneStartDay_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 5, 5),
    _SystemServicesTimezoneStartDay_Type()
)
systemServicesTimezoneStartDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemServicesTimezoneStartDay.setStatus("current")


class _SystemServicesTimezoneStartMonth_Type(Unsigned32):
    """Custom type systemServicesTimezoneStartMonth based on Unsigned32"""
    defaultValue = 0


_SystemServicesTimezoneStartMonth_Object = MibScalar
systemServicesTimezoneStartMonth = _SystemServicesTimezoneStartMonth_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 5, 6),
    _SystemServicesTimezoneStartMonth_Type()
)
systemServicesTimezoneStartMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemServicesTimezoneStartMonth.setStatus("current")


class _SystemServicesTimezoneStartTime_Type(Unsigned32):
    """Custom type systemServicesTimezoneStartTime based on Unsigned32"""
    defaultValue = 0


_SystemServicesTimezoneStartTime_Object = MibScalar
systemServicesTimezoneStartTime = _SystemServicesTimezoneStartTime_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 5, 7),
    _SystemServicesTimezoneStartTime_Type()
)
systemServicesTimezoneStartTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemServicesTimezoneStartTime.setStatus("current")


class _SystemServicesTimezoneOffset_Type(Unsigned32):
    """Custom type systemServicesTimezoneOffset based on Unsigned32"""
    defaultValue = 0


_SystemServicesTimezoneOffset_Object = MibScalar
systemServicesTimezoneOffset = _SystemServicesTimezoneOffset_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 5, 8),
    _SystemServicesTimezoneOffset_Type()
)
systemServicesTimezoneOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemServicesTimezoneOffset.setStatus("current")


class _SystemServicesTimezoneEndWeek_Type(Unsigned32):
    """Custom type systemServicesTimezoneEndWeek based on Unsigned32"""
    defaultValue = 0


_SystemServicesTimezoneEndWeek_Object = MibScalar
systemServicesTimezoneEndWeek = _SystemServicesTimezoneEndWeek_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 5, 9),
    _SystemServicesTimezoneEndWeek_Type()
)
systemServicesTimezoneEndWeek.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemServicesTimezoneEndWeek.setStatus("current")


class _SystemServicesTimezoneEndDay_Type(Unsigned32):
    """Custom type systemServicesTimezoneEndDay based on Unsigned32"""
    defaultValue = 0


_SystemServicesTimezoneEndDay_Object = MibScalar
systemServicesTimezoneEndDay = _SystemServicesTimezoneEndDay_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 5, 10),
    _SystemServicesTimezoneEndDay_Type()
)
systemServicesTimezoneEndDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemServicesTimezoneEndDay.setStatus("current")


class _SystemServicesTimezoneEndMonth_Type(Unsigned32):
    """Custom type systemServicesTimezoneEndMonth based on Unsigned32"""
    defaultValue = 0


_SystemServicesTimezoneEndMonth_Object = MibScalar
systemServicesTimezoneEndMonth = _SystemServicesTimezoneEndMonth_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 5, 11),
    _SystemServicesTimezoneEndMonth_Type()
)
systemServicesTimezoneEndMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemServicesTimezoneEndMonth.setStatus("current")


class _SystemServicesTimezoneEndTime_Type(Unsigned32):
    """Custom type systemServicesTimezoneEndTime based on Unsigned32"""
    defaultValue = 0


_SystemServicesTimezoneEndTime_Object = MibScalar
systemServicesTimezoneEndTime = _SystemServicesTimezoneEndTime_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 5, 12),
    _SystemServicesTimezoneEndTime_Type()
)
systemServicesTimezoneEndTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemServicesTimezoneEndTime.setStatus("current")


class _SystemServicesEnableDST_Type(Enable):
    """Custom type systemServicesEnableDST based on Enable"""


_SystemServicesEnableDST_Object = MibScalar
systemServicesEnableDST = _SystemServicesEnableDST_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 5, 13),
    _SystemServicesEnableDST_Type()
)
systemServicesEnableDST.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemServicesEnableDST.setStatus("current")


class _SystemServicesWorkingDirectory_Type(SnmpAdminString):
    """Custom type systemServicesWorkingDirectory based on SnmpAdminString"""
    defaultValue = OctetString("/flash")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SystemServicesWorkingDirectory_Type.__name__ = "SnmpAdminString"
_SystemServicesWorkingDirectory_Object = MibScalar
systemServicesWorkingDirectory = _SystemServicesWorkingDirectory_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 5, 14),
    _SystemServicesWorkingDirectory_Type()
)
systemServicesWorkingDirectory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemServicesWorkingDirectory.setStatus("current")


class _SystemServicesArg1_Type(SnmpAdminString):
    """Custom type systemServicesArg1 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SystemServicesArg1_Type.__name__ = "SnmpAdminString"
_SystemServicesArg1_Object = MibScalar
systemServicesArg1 = _SystemServicesArg1_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 5, 15),
    _SystemServicesArg1_Type()
)
systemServicesArg1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemServicesArg1.setStatus("current")


class _SystemServicesArg2_Type(SnmpAdminString):
    """Custom type systemServicesArg2 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SystemServicesArg2_Type.__name__ = "SnmpAdminString"
_SystemServicesArg2_Object = MibScalar
systemServicesArg2 = _SystemServicesArg2_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 5, 16),
    _SystemServicesArg2_Type()
)
systemServicesArg2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemServicesArg2.setStatus("current")


class _SystemServicesArg3_Type(SnmpAdminString):
    """Custom type systemServicesArg3 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SystemServicesArg3_Type.__name__ = "SnmpAdminString"
_SystemServicesArg3_Object = MibScalar
systemServicesArg3 = _SystemServicesArg3_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 5, 17),
    _SystemServicesArg3_Type()
)
systemServicesArg3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemServicesArg3.setStatus("current")


class _SystemServicesArg4_Type(SnmpAdminString):
    """Custom type systemServicesArg4 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SystemServicesArg4_Type.__name__ = "SnmpAdminString"
_SystemServicesArg4_Object = MibScalar
systemServicesArg4 = _SystemServicesArg4_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 5, 18),
    _SystemServicesArg4_Type()
)
systemServicesArg4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemServicesArg4.setStatus("current")


class _SystemServicesArg5_Type(SnmpAdminString):
    """Custom type systemServicesArg5 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SystemServicesArg5_Type.__name__ = "SnmpAdminString"
_SystemServicesArg5_Object = MibScalar
systemServicesArg5 = _SystemServicesArg5_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 5, 19),
    _SystemServicesArg5_Type()
)
systemServicesArg5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemServicesArg5.setStatus("current")


class _SystemServicesArg6_Type(SnmpAdminString):
    """Custom type systemServicesArg6 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SystemServicesArg6_Type.__name__ = "SnmpAdminString"
_SystemServicesArg6_Object = MibScalar
systemServicesArg6 = _SystemServicesArg6_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 5, 20),
    _SystemServicesArg6_Type()
)
systemServicesArg6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemServicesArg6.setStatus("current")


class _SystemServicesArg7_Type(SnmpAdminString):
    """Custom type systemServicesArg7 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SystemServicesArg7_Type.__name__ = "SnmpAdminString"
_SystemServicesArg7_Object = MibScalar
systemServicesArg7 = _SystemServicesArg7_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 5, 21),
    _SystemServicesArg7_Type()
)
systemServicesArg7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemServicesArg7.setStatus("current")


class _SystemServicesArg8_Type(SnmpAdminString):
    """Custom type systemServicesArg8 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SystemServicesArg8_Type.__name__ = "SnmpAdminString"
_SystemServicesArg8_Object = MibScalar
systemServicesArg8 = _SystemServicesArg8_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 5, 22),
    _SystemServicesArg8_Type()
)
systemServicesArg8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemServicesArg8.setStatus("current")


class _SystemServicesArg9_Type(SnmpAdminString):
    """Custom type systemServicesArg9 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SystemServicesArg9_Type.__name__ = "SnmpAdminString"
_SystemServicesArg9_Object = MibScalar
systemServicesArg9 = _SystemServicesArg9_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 5, 23),
    _SystemServicesArg9_Type()
)
systemServicesArg9.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemServicesArg9.setStatus("current")


class _SystemServicesAction_Type(Integer32):
    """Custom type systemServicesAction based on Integer32"""
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
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49)
        )
    )
    namedValues = NamedValues(
        *(("aclman", 33),
          ("backup", 45),
          ("backupminiboot", 28),
          ("bootrom", 26),
          ("chmodmw", 9),
          ("chmodpw", 8),
          ("cp", 6),
          ("cpr", 7),
          ("debugPmdNi", 25),
          ("defaultminiboot", 27),
          ("dshell", 19),
          ("ed", 16),
          ("filedir", 22),
          ("fpgacmm", 29),
          ("fpgani", 49),
          ("fsck", 10),
          ("fscollect", 48),
          ("ftp", 11),
          ("ftp6", 39),
          ("install", 15),
          ("miniboot", 35),
          ("mkdir", 1),
          ("modbootparams", 21),
          ("more", 17),
          ("mount", 43),
          ("mv", 3),
          ("newfs", 18),
          ("noaction", 0),
          ("restore", 46),
          ("restoreLicence", 37),
          ("rm", 4),
          ("rmdir", 2),
          ("rmr", 5),
          ("rz", 12),
          ("scp", 32),
          ("sftp", 24),
          ("sftp6", 42),
          ("ssh", 23),
          ("ssh6", 41),
          ("telnet", 14),
          ("telnet6", 40),
          ("tftp", 47),
          ("ubootMinibootAllSlots", 34),
          ("ubootcmm", 30),
          ("ubootni", 31),
          ("unmount", 44),
          ("updateDSineXtroller", 38),
          ("upgradeLicence", 36),
          ("vi", 13),
          ("view", 20))
    )


_SystemServicesAction_Type.__name__ = "Integer32"
_SystemServicesAction_Object = MibScalar
systemServicesAction = _SystemServicesAction_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 5, 24),
    _SystemServicesAction_Type()
)
systemServicesAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemServicesAction.setStatus("current")
_SystemServicesResultCode_Type = Unsigned32
_SystemServicesResultCode_Object = MibScalar
systemServicesResultCode = _SystemServicesResultCode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 5, 25),
    _SystemServicesResultCode_Type()
)
systemServicesResultCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemServicesResultCode.setStatus("current")


class _SystemServicesResultString_Type(SnmpAdminString):
    """Custom type systemServicesResultString based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SystemServicesResultString_Type.__name__ = "SnmpAdminString"
_SystemServicesResultString_Object = MibScalar
systemServicesResultString = _SystemServicesResultString_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 5, 26),
    _SystemServicesResultString_Type()
)
systemServicesResultString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemServicesResultString.setStatus("current")


class _SystemServicesKtraceEnable_Type(Enable):
    """Custom type systemServicesKtraceEnable based on Enable"""


_SystemServicesKtraceEnable_Object = MibScalar
systemServicesKtraceEnable = _SystemServicesKtraceEnable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 5, 27),
    _SystemServicesKtraceEnable_Type()
)
systemServicesKtraceEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemServicesKtraceEnable.setStatus("obsolete")


class _SystemServicesSystraceEnable_Type(Enable):
    """Custom type systemServicesSystraceEnable based on Enable"""


_SystemServicesSystraceEnable_Object = MibScalar
systemServicesSystraceEnable = _SystemServicesSystraceEnable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 5, 28),
    _SystemServicesSystraceEnable_Type()
)
systemServicesSystraceEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemServicesSystraceEnable.setStatus("obsolete")


class _SystemServicesTtyLines_Type(Unsigned32):
    """Custom type systemServicesTtyLines based on Unsigned32"""
    defaultValue = 24

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SystemServicesTtyLines_Type.__name__ = "Unsigned32"
_SystemServicesTtyLines_Object = MibScalar
systemServicesTtyLines = _SystemServicesTtyLines_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 5, 29),
    _SystemServicesTtyLines_Type()
)
systemServicesTtyLines.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemServicesTtyLines.setStatus("current")


class _SystemServicesTtyColumns_Type(Unsigned32):
    """Custom type systemServicesTtyColumns based on Unsigned32"""
    defaultValue = 80

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SystemServicesTtyColumns_Type.__name__ = "Unsigned32"
_SystemServicesTtyColumns_Object = MibScalar
systemServicesTtyColumns = _SystemServicesTtyColumns_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 5, 30),
    _SystemServicesTtyColumns_Type()
)
systemServicesTtyColumns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemServicesTtyColumns.setStatus("current")


class _SystemServicesMemMonitorEnable_Type(Enable):
    """Custom type systemServicesMemMonitorEnable based on Enable"""


_SystemServicesMemMonitorEnable_Object = MibScalar
systemServicesMemMonitorEnable = _SystemServicesMemMonitorEnable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 5, 31),
    _SystemServicesMemMonitorEnable_Type()
)
systemServicesMemMonitorEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemServicesMemMonitorEnable.setStatus("current")
_SystemServicesKtraceLevelTable_Object = MibTable
systemServicesKtraceLevelTable = _SystemServicesKtraceLevelTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 5, 32)
)
if mibBuilder.loadTexts:
    systemServicesKtraceLevelTable.setStatus("obsolete")
_SystemServicesKtraceLevelEntry_Object = MibTableRow
systemServicesKtraceLevelEntry = _SystemServicesKtraceLevelEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 5, 32, 1)
)
systemServicesKtraceLevelEntry.setIndexNames(
    (0, "ALCATEL-IND1-SYSTEM-MIB", "systemServicesKtraceLevelAppId"),
)
if mibBuilder.loadTexts:
    systemServicesKtraceLevelEntry.setStatus("obsolete")
_SystemServicesKtraceLevelAppId_Type = AppIdIndex
_SystemServicesKtraceLevelAppId_Object = MibTableColumn
systemServicesKtraceLevelAppId = _SystemServicesKtraceLevelAppId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 5, 32, 1, 1),
    _SystemServicesKtraceLevelAppId_Type()
)
systemServicesKtraceLevelAppId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemServicesKtraceLevelAppId.setStatus("obsolete")


class _SystemServicesKtraceLevel_Type(SeverityLevel):
    """Custom type systemServicesKtraceLevel based on SeverityLevel"""


_SystemServicesKtraceLevel_Object = MibTableColumn
systemServicesKtraceLevel = _SystemServicesKtraceLevel_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 5, 32, 1, 2),
    _SystemServicesKtraceLevel_Type()
)
systemServicesKtraceLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemServicesKtraceLevel.setStatus("obsolete")
_SystemServicesSystraceLevelTable_Object = MibTable
systemServicesSystraceLevelTable = _SystemServicesSystraceLevelTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 5, 33)
)
if mibBuilder.loadTexts:
    systemServicesSystraceLevelTable.setStatus("obsolete")
_SystemServicesSystraceLevelEntry_Object = MibTableRow
systemServicesSystraceLevelEntry = _SystemServicesSystraceLevelEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 5, 33, 1)
)
systemServicesSystraceLevelEntry.setIndexNames(
    (0, "ALCATEL-IND1-SYSTEM-MIB", "systemServicesSystraceLevelAppId"),
)
if mibBuilder.loadTexts:
    systemServicesSystraceLevelEntry.setStatus("obsolete")
_SystemServicesSystraceLevelAppId_Type = AppIdIndex
_SystemServicesSystraceLevelAppId_Object = MibTableColumn
systemServicesSystraceLevelAppId = _SystemServicesSystraceLevelAppId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 5, 33, 1, 1),
    _SystemServicesSystraceLevelAppId_Type()
)
systemServicesSystraceLevelAppId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemServicesSystraceLevelAppId.setStatus("obsolete")


class _SystemServicesSystraceLevel_Type(SeverityLevel):
    """Custom type systemServicesSystraceLevel based on SeverityLevel"""


_SystemServicesSystraceLevel_Object = MibTableColumn
systemServicesSystraceLevel = _SystemServicesSystraceLevel_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 5, 33, 1, 2),
    _SystemServicesSystraceLevel_Type()
)
systemServicesSystraceLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemServicesSystraceLevel.setStatus("obsolete")
_SystemUpdateStatusTable_Object = MibTable
systemUpdateStatusTable = _SystemUpdateStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 5, 34)
)
if mibBuilder.loadTexts:
    systemUpdateStatusTable.setStatus("current")
_SystemUpdateStatusEntry_Object = MibTableRow
systemUpdateStatusEntry = _SystemUpdateStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 5, 34, 1)
)
systemUpdateStatusEntry.setIndexNames(
    (0, "ALCATEL-IND1-SYSTEM-MIB", "systemUpdateIndex"),
)
if mibBuilder.loadTexts:
    systemUpdateStatusEntry.setStatus("current")


class _SystemUpdateIndex_Type(Integer32):
    """Custom type systemUpdateIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 72),
    )


_SystemUpdateIndex_Type.__name__ = "Integer32"
_SystemUpdateIndex_Object = MibTableColumn
systemUpdateIndex = _SystemUpdateIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 5, 34, 1, 1),
    _SystemUpdateIndex_Type()
)
systemUpdateIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    systemUpdateIndex.setStatus("current")


class _SystemUpdateStatus_Type(Integer32):
    """Custom type systemUpdateStatus based on Integer32"""
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
        *(("doneNok", 3),
          ("doneOk", 2),
          ("inProgress", 1),
          ("noOp", 4))
    )


_SystemUpdateStatus_Type.__name__ = "Integer32"
_SystemUpdateStatus_Object = MibTableColumn
systemUpdateStatus = _SystemUpdateStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 5, 34, 1, 2),
    _SystemUpdateStatus_Type()
)
systemUpdateStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemUpdateStatus.setStatus("current")


class _SystemUpdateErrorCode_Type(Integer32):
    """Custom type systemUpdateErrorCode based on Integer32"""
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
              24,
              25,
              26,
              27,
              28)
        )
    )
    namedValues = NamedValues(
        *(("commandBlocked", 19),
          ("dupSerialNum", 23),
          ("fXferFcloseErr", 8),
          ("fXferFtpErr", 3),
          ("fXferOPenErr", 2),
          ("fXferQuitErr", 7),
          ("fXferReadErr", 4),
          ("fXferReplyErr", 6),
          ("fXferWriteErr", 5),
          ("fileNameErr", 9),
          ("fileNotFound", 17),
          ("installDrvErr", 16),
          ("invalidKey", 27),
          ("invalidModType", 25),
          ("invalidNi", 21),
          ("invalidValue", 14),
          ("maxFaiCount", 26),
          ("msgSendIpcErr", 1),
          ("niLocked", 28),
          ("niNotPresent", 22),
          ("noError", 20),
          ("noInstallComp", 11),
          ("notPrimary", 18),
          ("notSupported", 13),
          ("notSysResource", 12),
          ("rmFileErr", 10),
          ("upToDate", 24),
          ("waitMsgMaxTry", 15))
    )


_SystemUpdateErrorCode_Type.__name__ = "Integer32"
_SystemUpdateErrorCode_Object = MibTableColumn
systemUpdateErrorCode = _SystemUpdateErrorCode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 5, 34, 1, 3),
    _SystemUpdateErrorCode_Type()
)
systemUpdateErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemUpdateErrorCode.setStatus("current")
_SystemServicesActionPercentComplete_Type = CommandPercentComplete
_SystemServicesActionPercentComplete_Object = MibScalar
systemServicesActionPercentComplete = _SystemServicesActionPercentComplete_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 5, 35),
    _SystemServicesActionPercentComplete_Type()
)
systemServicesActionPercentComplete.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemServicesActionPercentComplete.setStatus("current")


class _SystemServicesCurrentArchivePathName_Type(SnmpAdminString):
    """Custom type systemServicesCurrentArchivePathName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SystemServicesCurrentArchivePathName_Type.__name__ = "SnmpAdminString"
_SystemServicesCurrentArchivePathName_Object = MibScalar
systemServicesCurrentArchivePathName = _SystemServicesCurrentArchivePathName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 5, 36),
    _SystemServicesCurrentArchivePathName_Type()
)
systemServicesCurrentArchivePathName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemServicesCurrentArchivePathName.setStatus("current")
_SystemServicesArchiveTable_Object = MibTable
systemServicesArchiveTable = _SystemServicesArchiveTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 5, 37)
)
if mibBuilder.loadTexts:
    systemServicesArchiveTable.setStatus("current")
_SystemServicesArchiveEntry_Object = MibTableRow
systemServicesArchiveEntry = _SystemServicesArchiveEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 5, 37, 1)
)
systemServicesArchiveEntry.setIndexNames(
    (0, "ALCATEL-IND1-SYSTEM-MIB", "systemServicesArchiveIndex"),
)
if mibBuilder.loadTexts:
    systemServicesArchiveEntry.setStatus("current")
_SystemServicesArchiveIndex_Type = Unsigned32
_SystemServicesArchiveIndex_Object = MibTableColumn
systemServicesArchiveIndex = _SystemServicesArchiveIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 5, 37, 1, 1),
    _SystemServicesArchiveIndex_Type()
)
systemServicesArchiveIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemServicesArchiveIndex.setStatus("current")


class _SystemServicesArchiveName_Type(SnmpAdminString):
    """Custom type systemServicesArchiveName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SystemServicesArchiveName_Type.__name__ = "SnmpAdminString"
_SystemServicesArchiveName_Object = MibTableColumn
systemServicesArchiveName = _SystemServicesArchiveName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 5, 37, 1, 2),
    _SystemServicesArchiveName_Type()
)
systemServicesArchiveName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemServicesArchiveName.setStatus("current")


class _SystemServicesArchiveType_Type(SystemFileType):
    """Custom type systemServicesArchiveType based on SystemFileType"""


_SystemServicesArchiveType_Object = MibTableColumn
systemServicesArchiveType = _SystemServicesArchiveType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 5, 37, 1, 3),
    _SystemServicesArchiveType_Type()
)
systemServicesArchiveType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemServicesArchiveType.setStatus("current")


class _SystemServicesArchiveSize_Type(Unsigned32):
    """Custom type systemServicesArchiveSize based on Unsigned32"""
    defaultValue = 0


_SystemServicesArchiveSize_Object = MibTableColumn
systemServicesArchiveSize = _SystemServicesArchiveSize_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 5, 37, 1, 4),
    _SystemServicesArchiveSize_Type()
)
systemServicesArchiveSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemServicesArchiveSize.setStatus("current")


class _SystemServicesArchiveAttr_Type(Integer32):
    """Custom type systemServicesArchiveAttr based on Integer32"""
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
        *(("readOnly", 2),
          ("readWrite", 3),
          ("undefined", 1),
          ("writeOnly", 4))
    )


_SystemServicesArchiveAttr_Type.__name__ = "Integer32"
_SystemServicesArchiveAttr_Object = MibTableColumn
systemServicesArchiveAttr = _SystemServicesArchiveAttr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 5, 37, 1, 5),
    _SystemServicesArchiveAttr_Type()
)
systemServicesArchiveAttr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemServicesArchiveAttr.setStatus("current")
_SystemServicesUsbEnable_Type = Enable
_SystemServicesUsbEnable_Object = MibScalar
systemServicesUsbEnable = _SystemServicesUsbEnable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 5, 38),
    _SystemServicesUsbEnable_Type()
)
systemServicesUsbEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemServicesUsbEnable.setStatus("current")
_SystemServicesUsbAutoCopyEnable_Type = Enable
_SystemServicesUsbAutoCopyEnable_Object = MibScalar
systemServicesUsbAutoCopyEnable = _SystemServicesUsbAutoCopyEnable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 5, 39),
    _SystemServicesUsbAutoCopyEnable_Type()
)
systemServicesUsbAutoCopyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemServicesUsbAutoCopyEnable.setStatus("current")
_SystemServicesUsbMounted_Type = Enable
_SystemServicesUsbMounted_Object = MibScalar
systemServicesUsbMounted = _SystemServicesUsbMounted_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 5, 40),
    _SystemServicesUsbMounted_Type()
)
systemServicesUsbMounted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemServicesUsbMounted.setStatus("current")
_SystemSwitchLogging_ObjectIdentity = ObjectIdentity
systemSwitchLogging = _SystemSwitchLogging_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 6)
)


class _SystemSwitchLoggingIndex_Type(SwitchLoggingIndex):
    """Custom type systemSwitchLoggingIndex based on SwitchLoggingIndex"""


_SystemSwitchLoggingIndex_Object = MibScalar
systemSwitchLoggingIndex = _SystemSwitchLoggingIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 6, 1),
    _SystemSwitchLoggingIndex_Type()
)
systemSwitchLoggingIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemSwitchLoggingIndex.setStatus("current")


class _SystemSwitchLoggingEnable_Type(Enable):
    """Custom type systemSwitchLoggingEnable based on Enable"""


_SystemSwitchLoggingEnable_Object = MibScalar
systemSwitchLoggingEnable = _SystemSwitchLoggingEnable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 6, 2),
    _SystemSwitchLoggingEnable_Type()
)
systemSwitchLoggingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemSwitchLoggingEnable.setStatus("current")


class _SystemSwitchLoggingFlash_Type(Enable):
    """Custom type systemSwitchLoggingFlash based on Enable"""


_SystemSwitchLoggingFlash_Object = MibScalar
systemSwitchLoggingFlash = _SystemSwitchLoggingFlash_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 6, 3),
    _SystemSwitchLoggingFlash_Type()
)
systemSwitchLoggingFlash.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemSwitchLoggingFlash.setStatus("current")


class _SystemSwitchLoggingSocket_Type(Enable):
    """Custom type systemSwitchLoggingSocket based on Enable"""


_SystemSwitchLoggingSocket_Object = MibScalar
systemSwitchLoggingSocket = _SystemSwitchLoggingSocket_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 6, 4),
    _SystemSwitchLoggingSocket_Type()
)
systemSwitchLoggingSocket.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemSwitchLoggingSocket.setStatus("current")
_SystemSwitchLoggingSocketIpAddr_Type = IpAddress
_SystemSwitchLoggingSocketIpAddr_Object = MibScalar
systemSwitchLoggingSocketIpAddr = _SystemSwitchLoggingSocketIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 6, 5),
    _SystemSwitchLoggingSocketIpAddr_Type()
)
systemSwitchLoggingSocketIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemSwitchLoggingSocketIpAddr.setStatus("deprecated")


class _SystemSwitchLoggingConsole_Type(Enable):
    """Custom type systemSwitchLoggingConsole based on Enable"""


_SystemSwitchLoggingConsole_Object = MibScalar
systemSwitchLoggingConsole = _SystemSwitchLoggingConsole_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 6, 6),
    _SystemSwitchLoggingConsole_Type()
)
systemSwitchLoggingConsole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemSwitchLoggingConsole.setStatus("current")
_SystemSwitchLoggingApplicationTable_Object = MibTable
systemSwitchLoggingApplicationTable = _SystemSwitchLoggingApplicationTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 6, 7)
)
if mibBuilder.loadTexts:
    systemSwitchLoggingApplicationTable.setStatus("current")
_SystemSwitchLoggingLevelEntry_Object = MibTableRow
systemSwitchLoggingLevelEntry = _SystemSwitchLoggingLevelEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 6, 7, 1)
)
systemSwitchLoggingLevelEntry.setIndexNames(
    (0, "ALCATEL-IND1-SYSTEM-MIB", "systemSwitchLoggingApplicationAppId"),
    (0, "ALCATEL-IND1-SYSTEM-MIB", "systemSwitchLoggingApplicationSubAppId"),
    (0, "ALCATEL-IND1-SYSTEM-MIB", "systemSwitchLoggingApplicationSubAppVrfLevelIndex"),
)
if mibBuilder.loadTexts:
    systemSwitchLoggingLevelEntry.setStatus("current")
_SystemSwitchLoggingApplicationAppId_Type = AppIdIndex
_SystemSwitchLoggingApplicationAppId_Object = MibTableColumn
systemSwitchLoggingApplicationAppId = _SystemSwitchLoggingApplicationAppId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 6, 7, 1, 1),
    _SystemSwitchLoggingApplicationAppId_Type()
)
systemSwitchLoggingApplicationAppId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemSwitchLoggingApplicationAppId.setStatus("current")
_SystemSwitchLoggingApplicationSubAppId_Type = AppIdIndex
_SystemSwitchLoggingApplicationSubAppId_Object = MibTableColumn
systemSwitchLoggingApplicationSubAppId = _SystemSwitchLoggingApplicationSubAppId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 6, 7, 1, 2),
    _SystemSwitchLoggingApplicationSubAppId_Type()
)
systemSwitchLoggingApplicationSubAppId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemSwitchLoggingApplicationSubAppId.setStatus("current")


class _SystemSwitchLoggingApplicationSubAppVrfLevelIndex_Type(Integer32):
    """Custom type systemSwitchLoggingApplicationSubAppVrfLevelIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_SystemSwitchLoggingApplicationSubAppVrfLevelIndex_Type.__name__ = "Integer32"
_SystemSwitchLoggingApplicationSubAppVrfLevelIndex_Object = MibTableColumn
systemSwitchLoggingApplicationSubAppVrfLevelIndex = _SystemSwitchLoggingApplicationSubAppVrfLevelIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 6, 7, 1, 3),
    _SystemSwitchLoggingApplicationSubAppVrfLevelIndex_Type()
)
systemSwitchLoggingApplicationSubAppVrfLevelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemSwitchLoggingApplicationSubAppVrfLevelIndex.setStatus("current")


class _SystemSwitchLoggingApplicationAppName_Type(SnmpAdminString):
    """Custom type systemSwitchLoggingApplicationAppName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SystemSwitchLoggingApplicationAppName_Type.__name__ = "SnmpAdminString"
_SystemSwitchLoggingApplicationAppName_Object = MibTableColumn
systemSwitchLoggingApplicationAppName = _SystemSwitchLoggingApplicationAppName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 6, 7, 1, 4),
    _SystemSwitchLoggingApplicationAppName_Type()
)
systemSwitchLoggingApplicationAppName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemSwitchLoggingApplicationAppName.setStatus("current")


class _SystemSwitchLoggingApplicationSubAppName_Type(SnmpAdminString):
    """Custom type systemSwitchLoggingApplicationSubAppName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SystemSwitchLoggingApplicationSubAppName_Type.__name__ = "SnmpAdminString"
_SystemSwitchLoggingApplicationSubAppName_Object = MibTableColumn
systemSwitchLoggingApplicationSubAppName = _SystemSwitchLoggingApplicationSubAppName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 6, 7, 1, 5),
    _SystemSwitchLoggingApplicationSubAppName_Type()
)
systemSwitchLoggingApplicationSubAppName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemSwitchLoggingApplicationSubAppName.setStatus("current")


class _SystemSwitchLoggingApplicationSubAppLevel_Type(SeverityLevel):
    """Custom type systemSwitchLoggingApplicationSubAppLevel based on SeverityLevel"""


_SystemSwitchLoggingApplicationSubAppLevel_Object = MibTableColumn
systemSwitchLoggingApplicationSubAppLevel = _SystemSwitchLoggingApplicationSubAppLevel_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 6, 7, 1, 6),
    _SystemSwitchLoggingApplicationSubAppLevel_Type()
)
systemSwitchLoggingApplicationSubAppLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemSwitchLoggingApplicationSubAppLevel.setStatus("current")


class _SystemSwitchLoggingApplicationSubAppVrfLevelString_Type(SnmpAdminString):
    """Custom type systemSwitchLoggingApplicationSubAppVrfLevelString based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SystemSwitchLoggingApplicationSubAppVrfLevelString_Type.__name__ = "SnmpAdminString"
_SystemSwitchLoggingApplicationSubAppVrfLevelString_Object = MibTableColumn
systemSwitchLoggingApplicationSubAppVrfLevelString = _SystemSwitchLoggingApplicationSubAppVrfLevelString_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 6, 7, 1, 7),
    _SystemSwitchLoggingApplicationSubAppVrfLevelString_Type()
)
systemSwitchLoggingApplicationSubAppVrfLevelString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemSwitchLoggingApplicationSubAppVrfLevelString.setStatus("current")
_SystemSwitchLoggingClear_Type = Unsigned32
_SystemSwitchLoggingClear_Object = MibScalar
systemSwitchLoggingClear = _SystemSwitchLoggingClear_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 6, 8),
    _SystemSwitchLoggingClear_Type()
)
systemSwitchLoggingClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemSwitchLoggingClear.setStatus("current")
_SystemSwitchLoggingFileSize_Type = Unsigned32
_SystemSwitchLoggingFileSize_Object = MibScalar
systemSwitchLoggingFileSize = _SystemSwitchLoggingFileSize_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 6, 9),
    _SystemSwitchLoggingFileSize_Type()
)
systemSwitchLoggingFileSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemSwitchLoggingFileSize.setStatus("current")
_SystemSwitchLoggingHostTable_Object = MibTable
systemSwitchLoggingHostTable = _SystemSwitchLoggingHostTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 6, 10)
)
if mibBuilder.loadTexts:
    systemSwitchLoggingHostTable.setStatus("current")
_SystemSwitchLoggingHostEntry_Object = MibTableRow
systemSwitchLoggingHostEntry = _SystemSwitchLoggingHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 6, 10, 1)
)
systemSwitchLoggingHostEntry.setIndexNames(
    (0, "ALCATEL-IND1-SYSTEM-MIB", "systemSwitchLoggingHostIpAddr"),
)
if mibBuilder.loadTexts:
    systemSwitchLoggingHostEntry.setStatus("current")
_SystemSwitchLoggingHostIpAddr_Type = IpAddress
_SystemSwitchLoggingHostIpAddr_Object = MibTableColumn
systemSwitchLoggingHostIpAddr = _SystemSwitchLoggingHostIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 6, 10, 1, 1),
    _SystemSwitchLoggingHostIpAddr_Type()
)
systemSwitchLoggingHostIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemSwitchLoggingHostIpAddr.setStatus("current")


class _SystemSwitchLoggingHostPort_Type(Integer32):
    """Custom type systemSwitchLoggingHostPort based on Integer32"""
    defaultValue = 514

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SystemSwitchLoggingHostPort_Type.__name__ = "Integer32"
_SystemSwitchLoggingHostPort_Object = MibTableColumn
systemSwitchLoggingHostPort = _SystemSwitchLoggingHostPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 6, 10, 1, 2),
    _SystemSwitchLoggingHostPort_Type()
)
systemSwitchLoggingHostPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    systemSwitchLoggingHostPort.setStatus("current")
_SystemSwitchLoggingHostStatus_Type = RowStatus
_SystemSwitchLoggingHostStatus_Object = MibTableColumn
systemSwitchLoggingHostStatus = _SystemSwitchLoggingHostStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 6, 10, 1, 3),
    _SystemSwitchLoggingHostStatus_Type()
)
systemSwitchLoggingHostStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    systemSwitchLoggingHostStatus.setStatus("current")


class _SystemSwitchLoggingHostUserCommandHost_Type(Enable):
    """Custom type systemSwitchLoggingHostUserCommandHost based on Enable"""


_SystemSwitchLoggingHostUserCommandHost_Object = MibTableColumn
systemSwitchLoggingHostUserCommandHost = _SystemSwitchLoggingHostUserCommandHost_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 6, 10, 1, 4),
    _SystemSwitchLoggingHostUserCommandHost_Type()
)
systemSwitchLoggingHostUserCommandHost.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    systemSwitchLoggingHostUserCommandHost.setStatus("current")


class _SystemSwitchLoggingHostVrfName_Type(SnmpAdminString):
    """Custom type systemSwitchLoggingHostVrfName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_SystemSwitchLoggingHostVrfName_Type.__name__ = "SnmpAdminString"
_SystemSwitchLoggingHostVrfName_Object = MibTableColumn
systemSwitchLoggingHostVrfName = _SystemSwitchLoggingHostVrfName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 6, 10, 1, 5),
    _SystemSwitchLoggingHostVrfName_Type()
)
systemSwitchLoggingHostVrfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    systemSwitchLoggingHostVrfName.setStatus("current")
_SystemSwitchLoggingHostv6Table_Object = MibTable
systemSwitchLoggingHostv6Table = _SystemSwitchLoggingHostv6Table_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 6, 11)
)
if mibBuilder.loadTexts:
    systemSwitchLoggingHostv6Table.setStatus("current")
_SystemSwitchLoggingHostv6Entry_Object = MibTableRow
systemSwitchLoggingHostv6Entry = _SystemSwitchLoggingHostv6Entry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 6, 11, 1)
)
systemSwitchLoggingHostv6Entry.setIndexNames(
    (0, "ALCATEL-IND1-SYSTEM-MIB", "systemSwitchLoggingHostv6IpAddr"),
)
if mibBuilder.loadTexts:
    systemSwitchLoggingHostv6Entry.setStatus("current")
_SystemSwitchLoggingHostv6IpAddr_Type = Ipv6Address
_SystemSwitchLoggingHostv6IpAddr_Object = MibTableColumn
systemSwitchLoggingHostv6IpAddr = _SystemSwitchLoggingHostv6IpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 6, 11, 1, 1),
    _SystemSwitchLoggingHostv6IpAddr_Type()
)
systemSwitchLoggingHostv6IpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemSwitchLoggingHostv6IpAddr.setStatus("current")


class _SystemSwitchLoggingHostv6Port_Type(Integer32):
    """Custom type systemSwitchLoggingHostv6Port based on Integer32"""
    defaultValue = 514

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SystemSwitchLoggingHostv6Port_Type.__name__ = "Integer32"
_SystemSwitchLoggingHostv6Port_Object = MibTableColumn
systemSwitchLoggingHostv6Port = _SystemSwitchLoggingHostv6Port_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 6, 11, 1, 2),
    _SystemSwitchLoggingHostv6Port_Type()
)
systemSwitchLoggingHostv6Port.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    systemSwitchLoggingHostv6Port.setStatus("current")
_SystemSwitchLoggingHostv6Status_Type = RowStatus
_SystemSwitchLoggingHostv6Status_Object = MibTableColumn
systemSwitchLoggingHostv6Status = _SystemSwitchLoggingHostv6Status_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 6, 11, 1, 3),
    _SystemSwitchLoggingHostv6Status_Type()
)
systemSwitchLoggingHostv6Status.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    systemSwitchLoggingHostv6Status.setStatus("current")


class _SystemSwitchLoggingHostv6UserCommandHost_Type(Enable):
    """Custom type systemSwitchLoggingHostv6UserCommandHost based on Enable"""


_SystemSwitchLoggingHostv6UserCommandHost_Object = MibTableColumn
systemSwitchLoggingHostv6UserCommandHost = _SystemSwitchLoggingHostv6UserCommandHost_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 6, 11, 1, 4),
    _SystemSwitchLoggingHostv6UserCommandHost_Type()
)
systemSwitchLoggingHostv6UserCommandHost.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    systemSwitchLoggingHostv6UserCommandHost.setStatus("current")


class _SystemSwitchLoggingHostv6VrfName_Type(SnmpAdminString):
    """Custom type systemSwitchLoggingHostv6VrfName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_SystemSwitchLoggingHostv6VrfName_Type.__name__ = "SnmpAdminString"
_SystemSwitchLoggingHostv6VrfName_Object = MibTableColumn
systemSwitchLoggingHostv6VrfName = _SystemSwitchLoggingHostv6VrfName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 6, 11, 1, 5),
    _SystemSwitchLoggingHostv6VrfName_Type()
)
systemSwitchLoggingHostv6VrfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    systemSwitchLoggingHostv6VrfName.setStatus("current")


class _SystemSwitchLoggingHostCount_Type(Integer32):
    """Custom type systemSwitchLoggingHostCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_SystemSwitchLoggingHostCount_Type.__name__ = "Integer32"
_SystemSwitchLoggingHostCount_Object = MibScalar
systemSwitchLoggingHostCount = _SystemSwitchLoggingHostCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 6, 12),
    _SystemSwitchLoggingHostCount_Type()
)
systemSwitchLoggingHostCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemSwitchLoggingHostCount.setStatus("current")


class _SystemSwitchLoggingConsoleLevel_Type(SeverityLevel):
    """Custom type systemSwitchLoggingConsoleLevel based on SeverityLevel"""


_SystemSwitchLoggingConsoleLevel_Object = MibScalar
systemSwitchLoggingConsoleLevel = _SystemSwitchLoggingConsoleLevel_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 6, 13),
    _SystemSwitchLoggingConsoleLevel_Type()
)
systemSwitchLoggingConsoleLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    systemSwitchLoggingConsoleLevel.setStatus("current")


class _SystemSwitchLoggingUserCommandStatus_Type(Enable):
    """Custom type systemSwitchLoggingUserCommandStatus based on Enable"""


_SystemSwitchLoggingUserCommandStatus_Object = MibScalar
systemSwitchLoggingUserCommandStatus = _SystemSwitchLoggingUserCommandStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 6, 14),
    _SystemSwitchLoggingUserCommandStatus_Type()
)
systemSwitchLoggingUserCommandStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    systemSwitchLoggingUserCommandStatus.setStatus("current")


class _SystemSwitchLoggingSysLogFacilityId_Type(SysLogFacilityId):
    """Custom type systemSwitchLoggingSysLogFacilityId based on SysLogFacilityId"""


_SystemSwitchLoggingSysLogFacilityId_Object = MibScalar
systemSwitchLoggingSysLogFacilityId = _SystemSwitchLoggingSysLogFacilityId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 6, 15),
    _SystemSwitchLoggingSysLogFacilityId_Type()
)
systemSwitchLoggingSysLogFacilityId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemSwitchLoggingSysLogFacilityId.setStatus("current")
_SystemSwitchLoggingLevel_Type = SeverityLevel
_SystemSwitchLoggingLevel_Object = MibScalar
systemSwitchLoggingLevel = _SystemSwitchLoggingLevel_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 6, 16),
    _SystemSwitchLoggingLevel_Type()
)
systemSwitchLoggingLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemSwitchLoggingLevel.setStatus("current")


class _SystemSwitchLoggingAppName_Type(SnmpAdminString):
    """Custom type systemSwitchLoggingAppName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SystemSwitchLoggingAppName_Type.__name__ = "SnmpAdminString"
_SystemSwitchLoggingAppName_Object = MibScalar
systemSwitchLoggingAppName = _SystemSwitchLoggingAppName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 6, 17),
    _SystemSwitchLoggingAppName_Type()
)
systemSwitchLoggingAppName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemSwitchLoggingAppName.setStatus("current")


class _SystemSwitchLoggingDuplicateDetect_Type(Enable):
    """Custom type systemSwitchLoggingDuplicateDetect based on Enable"""


_SystemSwitchLoggingDuplicateDetect_Object = MibScalar
systemSwitchLoggingDuplicateDetect = _SystemSwitchLoggingDuplicateDetect_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 6, 18),
    _SystemSwitchLoggingDuplicateDetect_Type()
)
systemSwitchLoggingDuplicateDetect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemSwitchLoggingDuplicateDetect.setStatus("current")


class _SystemSwitchLoggingPreamble_Type(Enable):
    """Custom type systemSwitchLoggingPreamble based on Enable"""


_SystemSwitchLoggingPreamble_Object = MibScalar
systemSwitchLoggingPreamble = _SystemSwitchLoggingPreamble_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 6, 19),
    _SystemSwitchLoggingPreamble_Type()
)
systemSwitchLoggingPreamble.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemSwitchLoggingPreamble.setStatus("current")


class _SystemSwitchLoggingDebug_Type(Enable):
    """Custom type systemSwitchLoggingDebug based on Enable"""


_SystemSwitchLoggingDebug_Object = MibScalar
systemSwitchLoggingDebug = _SystemSwitchLoggingDebug_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 6, 20),
    _SystemSwitchLoggingDebug_Type()
)
systemSwitchLoggingDebug.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemSwitchLoggingDebug.setStatus("current")


class _SystemSwitchLoggingVrf_Type(VrfId):
    """Custom type systemSwitchLoggingVrf based on VrfId"""
    defaultValue = 1


_SystemSwitchLoggingVrf_Object = MibScalar
systemSwitchLoggingVrf = _SystemSwitchLoggingVrf_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 6, 21),
    _SystemSwitchLoggingVrf_Type()
)
systemSwitchLoggingVrf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemSwitchLoggingVrf.setStatus("current")


class _SystemSwitchLoggingHashAgeLimit_Type(AgeLimit):
    """Custom type systemSwitchLoggingHashAgeLimit based on AgeLimit"""
    defaultValue = 1


_SystemSwitchLoggingHashAgeLimit_Object = MibScalar
systemSwitchLoggingHashAgeLimit = _SystemSwitchLoggingHashAgeLimit_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 6, 22),
    _SystemSwitchLoggingHashAgeLimit_Type()
)
systemSwitchLoggingHashAgeLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemSwitchLoggingHashAgeLimit.setStatus("current")


class _SystemSwitchLoggingTty_Type(Enable):
    """Custom type systemSwitchLoggingTty based on Enable"""


_SystemSwitchLoggingTty_Object = MibScalar
systemSwitchLoggingTty = _SystemSwitchLoggingTty_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 6, 23),
    _SystemSwitchLoggingTty_Type()
)
systemSwitchLoggingTty.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemSwitchLoggingTty.setStatus("current")
_SystemSwitchLoggingSubAppNbr_Type = AppIdIndex
_SystemSwitchLoggingSubAppNbr_Object = MibScalar
systemSwitchLoggingSubAppNbr = _SystemSwitchLoggingSubAppNbr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 6, 24),
    _SystemSwitchLoggingSubAppNbr_Type()
)
systemSwitchLoggingSubAppNbr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemSwitchLoggingSubAppNbr.setStatus("current")


class _SystemSwitchLoggingLibraryName_Type(SnmpAdminString):
    """Custom type systemSwitchLoggingLibraryName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SystemSwitchLoggingLibraryName_Type.__name__ = "SnmpAdminString"
_SystemSwitchLoggingLibraryName_Object = MibScalar
systemSwitchLoggingLibraryName = _SystemSwitchLoggingLibraryName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 6, 25),
    _SystemSwitchLoggingLibraryName_Type()
)
systemSwitchLoggingLibraryName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemSwitchLoggingLibraryName.setStatus("current")


class _SystemSwitchLoggingLoopback0_Type(Enable):
    """Custom type systemSwitchLoggingLoopback0 based on Enable"""


_SystemSwitchLoggingLoopback0_Object = MibScalar
systemSwitchLoggingLoopback0 = _SystemSwitchLoggingLoopback0_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 6, 26),
    _SystemSwitchLoggingLoopback0_Type()
)
systemSwitchLoggingLoopback0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemSwitchLoggingLoopback0.setStatus("current")
_SystemDNS_ObjectIdentity = ObjectIdentity
systemDNS = _SystemDNS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 7)
)


class _SystemDNSEnableDnsResolver_Type(Enable):
    """Custom type systemDNSEnableDnsResolver based on Enable"""


_SystemDNSEnableDnsResolver_Object = MibScalar
systemDNSEnableDnsResolver = _SystemDNSEnableDnsResolver_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 7, 1),
    _SystemDNSEnableDnsResolver_Type()
)
systemDNSEnableDnsResolver.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    systemDNSEnableDnsResolver.setStatus("current")


class _SystemDNSDomainName_Type(SnmpAdminString):
    """Custom type systemDNSDomainName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SystemDNSDomainName_Type.__name__ = "SnmpAdminString"
_SystemDNSDomainName_Object = MibScalar
systemDNSDomainName = _SystemDNSDomainName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 7, 2),
    _SystemDNSDomainName_Type()
)
systemDNSDomainName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    systemDNSDomainName.setStatus("current")


class _SystemDNSNsAddr1_Type(IpAddress):
    """Custom type systemDNSNsAddr1 based on IpAddress"""
    defaultHexValue = "00000000"


_SystemDNSNsAddr1_Object = MibScalar
systemDNSNsAddr1 = _SystemDNSNsAddr1_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 7, 3),
    _SystemDNSNsAddr1_Type()
)
systemDNSNsAddr1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    systemDNSNsAddr1.setStatus("current")


class _SystemDNSNsAddr2_Type(IpAddress):
    """Custom type systemDNSNsAddr2 based on IpAddress"""
    defaultHexValue = "00000000"


_SystemDNSNsAddr2_Object = MibScalar
systemDNSNsAddr2 = _SystemDNSNsAddr2_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 7, 4),
    _SystemDNSNsAddr2_Type()
)
systemDNSNsAddr2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    systemDNSNsAddr2.setStatus("current")


class _SystemDNSNsAddr3_Type(IpAddress):
    """Custom type systemDNSNsAddr3 based on IpAddress"""
    defaultHexValue = "00000000"


_SystemDNSNsAddr3_Object = MibScalar
systemDNSNsAddr3 = _SystemDNSNsAddr3_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 7, 5),
    _SystemDNSNsAddr3_Type()
)
systemDNSNsAddr3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    systemDNSNsAddr3.setStatus("current")


class _SystemDNSNsIPv6Addr1_Type(Ipv6Address):
    """Custom type systemDNSNsIPv6Addr1 based on Ipv6Address"""
    defaultHexValue = "00000000000000000000000000000000"


_SystemDNSNsIPv6Addr1_Object = MibScalar
systemDNSNsIPv6Addr1 = _SystemDNSNsIPv6Addr1_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 7, 6),
    _SystemDNSNsIPv6Addr1_Type()
)
systemDNSNsIPv6Addr1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    systemDNSNsIPv6Addr1.setStatus("current")


class _SystemDNSNsIPv6Addr2_Type(Ipv6Address):
    """Custom type systemDNSNsIPv6Addr2 based on Ipv6Address"""
    defaultHexValue = "00000000000000000000000000000000"


_SystemDNSNsIPv6Addr2_Object = MibScalar
systemDNSNsIPv6Addr2 = _SystemDNSNsIPv6Addr2_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 7, 7),
    _SystemDNSNsIPv6Addr2_Type()
)
systemDNSNsIPv6Addr2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    systemDNSNsIPv6Addr2.setStatus("current")


class _SystemDNSNsIPv6Addr3_Type(Ipv6Address):
    """Custom type systemDNSNsIPv6Addr3 based on Ipv6Address"""
    defaultHexValue = "00000000000000000000000000000000"


_SystemDNSNsIPv6Addr3_Object = MibScalar
systemDNSNsIPv6Addr3 = _SystemDNSNsIPv6Addr3_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 7, 8),
    _SystemDNSNsIPv6Addr3_Type()
)
systemDNSNsIPv6Addr3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    systemDNSNsIPv6Addr3.setStatus("current")
_AlcatelIND1SystemMIBConformance_ObjectIdentity = ObjectIdentity
alcatelIND1SystemMIBConformance = _AlcatelIND1SystemMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1SystemMIBConformance.setStatus("current")
_AlcatelIND1SystemMIBGroups_ObjectIdentity = ObjectIdentity
alcatelIND1SystemMIBGroups = _AlcatelIND1SystemMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 2, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1SystemMIBGroups.setStatus("current")
_AlcatelIND1SystemMIBCompliances_ObjectIdentity = ObjectIdentity
alcatelIND1SystemMIBCompliances = _AlcatelIND1SystemMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 2, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1SystemMIBCompliances.setStatus("current")

# Managed Objects groups

systemMicrocodeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 2, 1, 1)
)
systemMicrocodeGroup.setObjects(
      *(("ALCATEL-IND1-SYSTEM-MIB", "systemMicrocodePackageVersion"),
        ("ALCATEL-IND1-SYSTEM-MIB", "systemMicrocodePackageName"),
        ("ALCATEL-IND1-SYSTEM-MIB", "systemMicrocodePackageDescription"),
        ("ALCATEL-IND1-SYSTEM-MIB", "systemMicrocodePackageStatus"),
        ("ALCATEL-IND1-SYSTEM-MIB", "systemMicrocodePackageSize"))
)
if mibBuilder.loadTexts:
    systemMicrocodeGroup.setStatus("current")

systemBootParamsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 2, 1, 2)
)
systemBootParamsGroup.setObjects(
      *(("ALCATEL-IND1-SYSTEM-MIB", "systemBootNetwork"),
        ("ALCATEL-IND1-SYSTEM-MIB", "systemBootNetworkGateway"),
        ("ALCATEL-IND1-SYSTEM-MIB", "systemBootNetworkNetmask"))
)
if mibBuilder.loadTexts:
    systemBootParamsGroup.setStatus("current")

systemHardwareGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 2, 1, 3)
)
systemHardwareGroup.setObjects(
      *(("ALCATEL-IND1-SYSTEM-MIB", "systemHardwareFlashMfg"),
        ("ALCATEL-IND1-SYSTEM-MIB", "systemHardwareFlashSize"),
        ("ALCATEL-IND1-SYSTEM-MIB", "systemHardwareMemoryMfg"),
        ("ALCATEL-IND1-SYSTEM-MIB", "systemHardwareMemorySize"),
        ("ALCATEL-IND1-SYSTEM-MIB", "systemHardwareNVRAMBatteryLow"),
        ("ALCATEL-IND1-SYSTEM-MIB", "systemHardwareBootCpuType"),
        ("ALCATEL-IND1-SYSTEM-MIB", "systemHardwareJumperInterruptBoot"),
        ("ALCATEL-IND1-SYSTEM-MIB", "systemHardwareJumperForceUartDefaults"),
        ("ALCATEL-IND1-SYSTEM-MIB", "systemHardwareJumperRunExtendedMemoryDiagnostics"),
        ("ALCATEL-IND1-SYSTEM-MIB", "systemHardwareJumperSpare"),
        ("ALCATEL-IND1-SYSTEM-MIB", "systemHardwareFpgaVersionIndex"),
        ("ALCATEL-IND1-SYSTEM-MIB", "systemHardwareFpgaVersion"),
        ("ALCATEL-IND1-SYSTEM-MIB", "systemHardwareBootRomVersion"),
        ("ALCATEL-IND1-SYSTEM-MIB", "systemHardwareDefaultMiniBootVersion"),
        ("ALCATEL-IND1-SYSTEM-MIB", "systemHardwareBackupMiniBootVersion"),
        ("ALCATEL-IND1-SYSTEM-MIB", "systemHardwareCpldVersion"),
        ("ALCATEL-IND1-SYSTEM-MIB", "systemHardwareMinorFpgaVersion"),
        ("ALCATEL-IND1-SYSTEM-MIB", "systemHardwareProdRegId"),
        ("ALCATEL-IND1-SYSTEM-MIB", "systemHardwareRevisionRegister"),
        ("ALCATEL-IND1-SYSTEM-MIB", "systemHardwareUbootMinibootVersion"),
        ("ALCATEL-IND1-SYSTEM-MIB", "systemHardwareUbootVersion"),
        ("ALCATEL-IND1-SYSTEM-MIB", "systemHardwareXfpId"))
)
if mibBuilder.loadTexts:
    systemHardwareGroup.setStatus("current")

systemServicesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 2, 1, 4)
)
systemServicesGroup.setObjects(
      *(("ALCATEL-IND1-SYSTEM-MIB", "systemServicesDate"),
        ("ALCATEL-IND1-SYSTEM-MIB", "systemServicesTime"),
        ("ALCATEL-IND1-SYSTEM-MIB", "systemServicesTimezone"),
        ("ALCATEL-IND1-SYSTEM-MIB", "systemServicesTimezoneStartWeek"),
        ("ALCATEL-IND1-SYSTEM-MIB", "systemServicesTimezoneStartDay"),
        ("ALCATEL-IND1-SYSTEM-MIB", "systemServicesTimezoneStartMonth"),
        ("ALCATEL-IND1-SYSTEM-MIB", "systemServicesTimezoneStartTime"),
        ("ALCATEL-IND1-SYSTEM-MIB", "systemServicesTimezoneOffset"),
        ("ALCATEL-IND1-SYSTEM-MIB", "systemServicesTimezoneEndWeek"),
        ("ALCATEL-IND1-SYSTEM-MIB", "systemServicesTimezoneEndDay"),
        ("ALCATEL-IND1-SYSTEM-MIB", "systemServicesTimezoneEndMonth"),
        ("ALCATEL-IND1-SYSTEM-MIB", "systemServicesTimezoneEndTime"),
        ("ALCATEL-IND1-SYSTEM-MIB", "systemServicesEnableDST"),
        ("ALCATEL-IND1-SYSTEM-MIB", "systemServicesWorkingDirectory"),
        ("ALCATEL-IND1-SYSTEM-MIB", "systemServicesArg1"),
        ("ALCATEL-IND1-SYSTEM-MIB", "systemServicesArg2"),
        ("ALCATEL-IND1-SYSTEM-MIB", "systemServicesArg3"),
        ("ALCATEL-IND1-SYSTEM-MIB", "systemServicesArg4"),
        ("ALCATEL-IND1-SYSTEM-MIB", "systemServicesArg5"),
        ("ALCATEL-IND1-SYSTEM-MIB", "systemServicesArg6"),
        ("ALCATEL-IND1-SYSTEM-MIB", "systemServicesArg7"),
        ("ALCATEL-IND1-SYSTEM-MIB", "systemServicesArg8"),
        ("ALCATEL-IND1-SYSTEM-MIB", "systemServicesArg9"),
        ("ALCATEL-IND1-SYSTEM-MIB", "systemServicesAction"),
        ("ALCATEL-IND1-SYSTEM-MIB", "systemServicesResultCode"),
        ("ALCATEL-IND1-SYSTEM-MIB", "systemServicesResultString"),
        ("ALCATEL-IND1-SYSTEM-MIB", "systemServicesKtraceEnable"),
        ("ALCATEL-IND1-SYSTEM-MIB", "systemServicesSystraceEnable"),
        ("ALCATEL-IND1-SYSTEM-MIB", "systemServicesTtyLines"),
        ("ALCATEL-IND1-SYSTEM-MIB", "systemServicesTtyColumns"),
        ("ALCATEL-IND1-SYSTEM-MIB", "systemServicesMemMonitorEnable"),
        ("ALCATEL-IND1-SYSTEM-MIB", "systemServicesKtraceLevelAppId"),
        ("ALCATEL-IND1-SYSTEM-MIB", "systemServicesKtraceLevel"),
        ("ALCATEL-IND1-SYSTEM-MIB", "systemServicesSystraceLevelAppId"),
        ("ALCATEL-IND1-SYSTEM-MIB", "systemServicesSystraceLevel"),
        ("ALCATEL-IND1-SYSTEM-MIB", "systemUpdateStatus"),
        ("ALCATEL-IND1-SYSTEM-MIB", "systemUpdateErrorCode"),
        ("ALCATEL-IND1-SYSTEM-MIB", "systemServicesActionPercentComplete"),
        ("ALCATEL-IND1-SYSTEM-MIB", "systemServicesArchiveName"),
        ("ALCATEL-IND1-SYSTEM-MIB", "systemServicesArchiveType"),
        ("ALCATEL-IND1-SYSTEM-MIB", "systemServicesArchiveSize"),
        ("ALCATEL-IND1-SYSTEM-MIB", "systemServicesArchiveAttr"),
        ("ALCATEL-IND1-SYSTEM-MIB", "systemServicesUsbEnable"),
        ("ALCATEL-IND1-SYSTEM-MIB", "systemServicesUsbAutoCopyEnable"),
        ("ALCATEL-IND1-SYSTEM-MIB", "systemServicesUsbMounted"),
        ("ALCATEL-IND1-SYSTEM-MIB", "systemServicesArchiveIndex"),
        ("ALCATEL-IND1-SYSTEM-MIB", "systemServicesCurrentArchivePathName"))
)
if mibBuilder.loadTexts:
    systemServicesGroup.setStatus("current")

systemFileSystemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 2, 1, 5)
)
systemFileSystemGroup.setObjects(
      *(("ALCATEL-IND1-SYSTEM-MIB", "systemFileSystemIndex"),
        ("ALCATEL-IND1-SYSTEM-MIB", "systemFileSystemFreeSpace"),
        ("ALCATEL-IND1-SYSTEM-MIB", "systemFileSystemName"),
        ("ALCATEL-IND1-SYSTEM-MIB", "systemFileSystemDirectoryName"),
        ("ALCATEL-IND1-SYSTEM-MIB", "systemFileSystemDirectoryDateTime"),
        ("ALCATEL-IND1-SYSTEM-MIB", "systemFileSystemFileIndex"),
        ("ALCATEL-IND1-SYSTEM-MIB", "systemFileSystemFileName"),
        ("ALCATEL-IND1-SYSTEM-MIB", "systemFileSystemFileType"),
        ("ALCATEL-IND1-SYSTEM-MIB", "systemFileSystemFileSize"),
        ("ALCATEL-IND1-SYSTEM-MIB", "systemFileSystemFileAttr"),
        ("ALCATEL-IND1-SYSTEM-MIB", "systemFileSystemFileDateTime"))
)
if mibBuilder.loadTexts:
    systemFileSystemGroup.setStatus("current")

systemSwitchLoggingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 2, 1, 6)
)
systemSwitchLoggingGroup.setObjects(
      *(("ALCATEL-IND1-SYSTEM-MIB", "systemSwitchLoggingIndex"),
        ("ALCATEL-IND1-SYSTEM-MIB", "systemSwitchLoggingEnable"),
        ("ALCATEL-IND1-SYSTEM-MIB", "systemSwitchLoggingFlash"),
        ("ALCATEL-IND1-SYSTEM-MIB", "systemSwitchLoggingSocket"),
        ("ALCATEL-IND1-SYSTEM-MIB", "systemSwitchLoggingSocketIpAddr"),
        ("ALCATEL-IND1-SYSTEM-MIB", "systemSwitchLoggingConsole"),
        ("ALCATEL-IND1-SYSTEM-MIB", "systemSwitchLoggingClear"),
        ("ALCATEL-IND1-SYSTEM-MIB", "systemSwitchLoggingFileSize"),
        ("ALCATEL-IND1-SYSTEM-MIB", "systemSwitchLoggingLevel"),
        ("ALCATEL-IND1-SYSTEM-MIB", "systemSwitchLoggingApplicationAppId"),
        ("ALCATEL-IND1-SYSTEM-MIB", "systemSwitchLoggingApplicationAppName"),
        ("ALCATEL-IND1-SYSTEM-MIB", "systemSwitchLoggingApplicationSubAppId"),
        ("ALCATEL-IND1-SYSTEM-MIB", "systemSwitchLoggingApplicationSubAppName"),
        ("ALCATEL-IND1-SYSTEM-MIB", "systemSwitchLoggingApplicationSubAppLevel"),
        ("ALCATEL-IND1-SYSTEM-MIB", "systemSwitchLoggingApplicationSubAppVrfLevelIndex"),
        ("ALCATEL-IND1-SYSTEM-MIB", "systemSwitchLoggingApplicationSubAppVrfLevelString"),
        ("ALCATEL-IND1-SYSTEM-MIB", "systemSwitchLoggingAppName"),
        ("ALCATEL-IND1-SYSTEM-MIB", "systemSwitchLoggingDuplicateDetect"),
        ("ALCATEL-IND1-SYSTEM-MIB", "systemSwitchLoggingPreamble"),
        ("ALCATEL-IND1-SYSTEM-MIB", "systemSwitchLoggingDebug"),
        ("ALCATEL-IND1-SYSTEM-MIB", "systemSwitchLoggingVrf"),
        ("ALCATEL-IND1-SYSTEM-MIB", "systemSwitchLoggingHashAgeLimit"),
        ("ALCATEL-IND1-SYSTEM-MIB", "systemSwitchLoggingTty"),
        ("ALCATEL-IND1-SYSTEM-MIB", "systemSwitchLoggingSubAppNbr"),
        ("ALCATEL-IND1-SYSTEM-MIB", "systemSwitchLoggingLibraryName"),
        ("ALCATEL-IND1-SYSTEM-MIB", "systemSwitchLoggingLoopback0"),
        ("ALCATEL-IND1-SYSTEM-MIB", "systemSwitchLoggingConsoleLevel"),
        ("ALCATEL-IND1-SYSTEM-MIB", "systemSwitchLoggingHostCount"),
        ("ALCATEL-IND1-SYSTEM-MIB", "systemSwitchLoggingUserCommandStatus"),
        ("ALCATEL-IND1-SYSTEM-MIB", "systemSwitchLoggingSysLogFacilityId"),
        ("ALCATEL-IND1-SYSTEM-MIB", "systemSwitchLoggingHostIpAddr"),
        ("ALCATEL-IND1-SYSTEM-MIB", "systemSwitchLoggingHostPort"),
        ("ALCATEL-IND1-SYSTEM-MIB", "systemSwitchLoggingHostStatus"),
        ("ALCATEL-IND1-SYSTEM-MIB", "systemSwitchLoggingHostUserCommandHost"),
        ("ALCATEL-IND1-SYSTEM-MIB", "systemSwitchLoggingHostVrfName"),
        ("ALCATEL-IND1-SYSTEM-MIB", "systemSwitchLoggingHostv6IpAddr"),
        ("ALCATEL-IND1-SYSTEM-MIB", "systemSwitchLoggingHostv6Port"),
        ("ALCATEL-IND1-SYSTEM-MIB", "systemSwitchLoggingHostv6Status"),
        ("ALCATEL-IND1-SYSTEM-MIB", "systemSwitchLoggingHostv6UserCommandHost"),
        ("ALCATEL-IND1-SYSTEM-MIB", "systemSwitchLoggingHostv6VrfName"))
)
if mibBuilder.loadTexts:
    systemSwitchLoggingGroup.setStatus("current")

systemDNSGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 2, 1, 7)
)
systemDNSGroup.setObjects(
      *(("ALCATEL-IND1-SYSTEM-MIB", "systemDNSEnableDnsResolver"),
        ("ALCATEL-IND1-SYSTEM-MIB", "systemDNSDomainName"),
        ("ALCATEL-IND1-SYSTEM-MIB", "systemDNSNsAddr1"),
        ("ALCATEL-IND1-SYSTEM-MIB", "systemDNSNsAddr2"),
        ("ALCATEL-IND1-SYSTEM-MIB", "systemDNSNsAddr3"),
        ("ALCATEL-IND1-SYSTEM-MIB", "systemDNSNsIPv6Addr1"),
        ("ALCATEL-IND1-SYSTEM-MIB", "systemDNSNsIPv6Addr2"),
        ("ALCATEL-IND1-SYSTEM-MIB", "systemDNSNsIPv6Addr3"))
)
if mibBuilder.loadTexts:
    systemDNSGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

alcatelIND1SystemMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1SystemMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-IND1-SYSTEM-MIB",
    **{"SystemFileType": SystemFileType,
       "SwitchLoggingIndex": SwitchLoggingIndex,
       "AppIdIndex": AppIdIndex,
       "Enable": Enable,
       "FileSystemIndex": FileSystemIndex,
       "SeverityLevel": SeverityLevel,
       "SysLogFacilityId": SysLogFacilityId,
       "CommandPercentComplete": CommandPercentComplete,
       "VrfId": VrfId,
       "AgeLimit": AgeLimit,
       "alcatelIND1SystemMIB": alcatelIND1SystemMIB,
       "alcatelIND1SystemMIBObjects": alcatelIND1SystemMIBObjects,
       "systemMicrocode": systemMicrocode,
       "systemMicrocodePackageTable": systemMicrocodePackageTable,
       "systemMicrocodePackageEntry": systemMicrocodePackageEntry,
       "systemMicrocodePackageDirectoryIndex": systemMicrocodePackageDirectoryIndex,
       "systemMicrocodePackageDirectory": systemMicrocodePackageDirectory,
       "systemMicrocodePackageIndex": systemMicrocodePackageIndex,
       "systemMicrocodePackageVersion": systemMicrocodePackageVersion,
       "systemMicrocodePackageName": systemMicrocodePackageName,
       "systemMicrocodePackageDescription": systemMicrocodePackageDescription,
       "systemMicrocodePackageStatus": systemMicrocodePackageStatus,
       "systemMicrocodePackageSize": systemMicrocodePackageSize,
       "systemBootParams": systemBootParams,
       "systemBootNetwork": systemBootNetwork,
       "systemBootNetworkGateway": systemBootNetworkGateway,
       "systemBootNetworkNetmask": systemBootNetworkNetmask,
       "systemHardware": systemHardware,
       "systemHardwareFlashMfg": systemHardwareFlashMfg,
       "systemHardwareFlashSize": systemHardwareFlashSize,
       "systemHardwareMemoryMfg": systemHardwareMemoryMfg,
       "systemHardwareMemorySize": systemHardwareMemorySize,
       "systemHardwareNVRAMBatteryLow": systemHardwareNVRAMBatteryLow,
       "systemHardwareBootCpuType": systemHardwareBootCpuType,
       "systemHardwareJumperInterruptBoot": systemHardwareJumperInterruptBoot,
       "systemHardwareJumperForceUartDefaults": systemHardwareJumperForceUartDefaults,
       "systemHardwareJumperRunExtendedMemoryDiagnostics": systemHardwareJumperRunExtendedMemoryDiagnostics,
       "systemHardwareJumperSpare": systemHardwareJumperSpare,
       "systemHardwareFpgaVersionTable": systemHardwareFpgaVersionTable,
       "systemHardwareFpgaVersionEntry": systemHardwareFpgaVersionEntry,
       "systemHardwareFpgaVersionIndex": systemHardwareFpgaVersionIndex,
       "systemHardwareFpgaVersion": systemHardwareFpgaVersion,
       "systemHardwareBootRomVersion": systemHardwareBootRomVersion,
       "systemHardwareBackupMiniBootVersion": systemHardwareBackupMiniBootVersion,
       "systemHardwareDefaultMiniBootVersion": systemHardwareDefaultMiniBootVersion,
       "systemHardwareMinorFpgaVersion": systemHardwareMinorFpgaVersion,
       "systemHardwareCpldVersion": systemHardwareCpldVersion,
       "systemHardwareUbootVersion": systemHardwareUbootVersion,
       "systemHardwareProdRegId": systemHardwareProdRegId,
       "systemHardwareRevisionRegister": systemHardwareRevisionRegister,
       "systemHardwareXfpId": systemHardwareXfpId,
       "systemHardwareUbootMinibootVersion": systemHardwareUbootMinibootVersion,
       "systemFileSystem": systemFileSystem,
       "systemFileSystemTable": systemFileSystemTable,
       "systemFileSystemEntry": systemFileSystemEntry,
       "systemFileSystemIndex": systemFileSystemIndex,
       "systemFileSystemName": systemFileSystemName,
       "systemFileSystemFreeSpace": systemFileSystemFreeSpace,
       "systemFileSystemDirectoryName": systemFileSystemDirectoryName,
       "systemFileSystemDirectoryDateTime": systemFileSystemDirectoryDateTime,
       "systemFileSystemFileTable": systemFileSystemFileTable,
       "systemFileSystemFileEntry": systemFileSystemFileEntry,
       "systemFileSystemFileIndex": systemFileSystemFileIndex,
       "systemFileSystemFileName": systemFileSystemFileName,
       "systemFileSystemFileType": systemFileSystemFileType,
       "systemFileSystemFileSize": systemFileSystemFileSize,
       "systemFileSystemFileAttr": systemFileSystemFileAttr,
       "systemFileSystemFileDateTime": systemFileSystemFileDateTime,
       "systemServices": systemServices,
       "systemServicesDate": systemServicesDate,
       "systemServicesTime": systemServicesTime,
       "systemServicesTimezone": systemServicesTimezone,
       "systemServicesTimezoneStartWeek": systemServicesTimezoneStartWeek,
       "systemServicesTimezoneStartDay": systemServicesTimezoneStartDay,
       "systemServicesTimezoneStartMonth": systemServicesTimezoneStartMonth,
       "systemServicesTimezoneStartTime": systemServicesTimezoneStartTime,
       "systemServicesTimezoneOffset": systemServicesTimezoneOffset,
       "systemServicesTimezoneEndWeek": systemServicesTimezoneEndWeek,
       "systemServicesTimezoneEndDay": systemServicesTimezoneEndDay,
       "systemServicesTimezoneEndMonth": systemServicesTimezoneEndMonth,
       "systemServicesTimezoneEndTime": systemServicesTimezoneEndTime,
       "systemServicesEnableDST": systemServicesEnableDST,
       "systemServicesWorkingDirectory": systemServicesWorkingDirectory,
       "systemServicesArg1": systemServicesArg1,
       "systemServicesArg2": systemServicesArg2,
       "systemServicesArg3": systemServicesArg3,
       "systemServicesArg4": systemServicesArg4,
       "systemServicesArg5": systemServicesArg5,
       "systemServicesArg6": systemServicesArg6,
       "systemServicesArg7": systemServicesArg7,
       "systemServicesArg8": systemServicesArg8,
       "systemServicesArg9": systemServicesArg9,
       "systemServicesAction": systemServicesAction,
       "systemServicesResultCode": systemServicesResultCode,
       "systemServicesResultString": systemServicesResultString,
       "systemServicesKtraceEnable": systemServicesKtraceEnable,
       "systemServicesSystraceEnable": systemServicesSystraceEnable,
       "systemServicesTtyLines": systemServicesTtyLines,
       "systemServicesTtyColumns": systemServicesTtyColumns,
       "systemServicesMemMonitorEnable": systemServicesMemMonitorEnable,
       "systemServicesKtraceLevelTable": systemServicesKtraceLevelTable,
       "systemServicesKtraceLevelEntry": systemServicesKtraceLevelEntry,
       "systemServicesKtraceLevelAppId": systemServicesKtraceLevelAppId,
       "systemServicesKtraceLevel": systemServicesKtraceLevel,
       "systemServicesSystraceLevelTable": systemServicesSystraceLevelTable,
       "systemServicesSystraceLevelEntry": systemServicesSystraceLevelEntry,
       "systemServicesSystraceLevelAppId": systemServicesSystraceLevelAppId,
       "systemServicesSystraceLevel": systemServicesSystraceLevel,
       "systemUpdateStatusTable": systemUpdateStatusTable,
       "systemUpdateStatusEntry": systemUpdateStatusEntry,
       "systemUpdateIndex": systemUpdateIndex,
       "systemUpdateStatus": systemUpdateStatus,
       "systemUpdateErrorCode": systemUpdateErrorCode,
       "systemServicesActionPercentComplete": systemServicesActionPercentComplete,
       "systemServicesCurrentArchivePathName": systemServicesCurrentArchivePathName,
       "systemServicesArchiveTable": systemServicesArchiveTable,
       "systemServicesArchiveEntry": systemServicesArchiveEntry,
       "systemServicesArchiveIndex": systemServicesArchiveIndex,
       "systemServicesArchiveName": systemServicesArchiveName,
       "systemServicesArchiveType": systemServicesArchiveType,
       "systemServicesArchiveSize": systemServicesArchiveSize,
       "systemServicesArchiveAttr": systemServicesArchiveAttr,
       "systemServicesUsbEnable": systemServicesUsbEnable,
       "systemServicesUsbAutoCopyEnable": systemServicesUsbAutoCopyEnable,
       "systemServicesUsbMounted": systemServicesUsbMounted,
       "systemSwitchLogging": systemSwitchLogging,
       "systemSwitchLoggingIndex": systemSwitchLoggingIndex,
       "systemSwitchLoggingEnable": systemSwitchLoggingEnable,
       "systemSwitchLoggingFlash": systemSwitchLoggingFlash,
       "systemSwitchLoggingSocket": systemSwitchLoggingSocket,
       "systemSwitchLoggingSocketIpAddr": systemSwitchLoggingSocketIpAddr,
       "systemSwitchLoggingConsole": systemSwitchLoggingConsole,
       "systemSwitchLoggingApplicationTable": systemSwitchLoggingApplicationTable,
       "systemSwitchLoggingLevelEntry": systemSwitchLoggingLevelEntry,
       "systemSwitchLoggingApplicationAppId": systemSwitchLoggingApplicationAppId,
       "systemSwitchLoggingApplicationSubAppId": systemSwitchLoggingApplicationSubAppId,
       "systemSwitchLoggingApplicationSubAppVrfLevelIndex": systemSwitchLoggingApplicationSubAppVrfLevelIndex,
       "systemSwitchLoggingApplicationAppName": systemSwitchLoggingApplicationAppName,
       "systemSwitchLoggingApplicationSubAppName": systemSwitchLoggingApplicationSubAppName,
       "systemSwitchLoggingApplicationSubAppLevel": systemSwitchLoggingApplicationSubAppLevel,
       "systemSwitchLoggingApplicationSubAppVrfLevelString": systemSwitchLoggingApplicationSubAppVrfLevelString,
       "systemSwitchLoggingClear": systemSwitchLoggingClear,
       "systemSwitchLoggingFileSize": systemSwitchLoggingFileSize,
       "systemSwitchLoggingHostTable": systemSwitchLoggingHostTable,
       "systemSwitchLoggingHostEntry": systemSwitchLoggingHostEntry,
       "systemSwitchLoggingHostIpAddr": systemSwitchLoggingHostIpAddr,
       "systemSwitchLoggingHostPort": systemSwitchLoggingHostPort,
       "systemSwitchLoggingHostStatus": systemSwitchLoggingHostStatus,
       "systemSwitchLoggingHostUserCommandHost": systemSwitchLoggingHostUserCommandHost,
       "systemSwitchLoggingHostVrfName": systemSwitchLoggingHostVrfName,
       "systemSwitchLoggingHostv6Table": systemSwitchLoggingHostv6Table,
       "systemSwitchLoggingHostv6Entry": systemSwitchLoggingHostv6Entry,
       "systemSwitchLoggingHostv6IpAddr": systemSwitchLoggingHostv6IpAddr,
       "systemSwitchLoggingHostv6Port": systemSwitchLoggingHostv6Port,
       "systemSwitchLoggingHostv6Status": systemSwitchLoggingHostv6Status,
       "systemSwitchLoggingHostv6UserCommandHost": systemSwitchLoggingHostv6UserCommandHost,
       "systemSwitchLoggingHostv6VrfName": systemSwitchLoggingHostv6VrfName,
       "systemSwitchLoggingHostCount": systemSwitchLoggingHostCount,
       "systemSwitchLoggingConsoleLevel": systemSwitchLoggingConsoleLevel,
       "systemSwitchLoggingUserCommandStatus": systemSwitchLoggingUserCommandStatus,
       "systemSwitchLoggingSysLogFacilityId": systemSwitchLoggingSysLogFacilityId,
       "systemSwitchLoggingLevel": systemSwitchLoggingLevel,
       "systemSwitchLoggingAppName": systemSwitchLoggingAppName,
       "systemSwitchLoggingDuplicateDetect": systemSwitchLoggingDuplicateDetect,
       "systemSwitchLoggingPreamble": systemSwitchLoggingPreamble,
       "systemSwitchLoggingDebug": systemSwitchLoggingDebug,
       "systemSwitchLoggingVrf": systemSwitchLoggingVrf,
       "systemSwitchLoggingHashAgeLimit": systemSwitchLoggingHashAgeLimit,
       "systemSwitchLoggingTty": systemSwitchLoggingTty,
       "systemSwitchLoggingSubAppNbr": systemSwitchLoggingSubAppNbr,
       "systemSwitchLoggingLibraryName": systemSwitchLoggingLibraryName,
       "systemSwitchLoggingLoopback0": systemSwitchLoggingLoopback0,
       "systemDNS": systemDNS,
       "systemDNSEnableDnsResolver": systemDNSEnableDnsResolver,
       "systemDNSDomainName": systemDNSDomainName,
       "systemDNSNsAddr1": systemDNSNsAddr1,
       "systemDNSNsAddr2": systemDNSNsAddr2,
       "systemDNSNsAddr3": systemDNSNsAddr3,
       "systemDNSNsIPv6Addr1": systemDNSNsIPv6Addr1,
       "systemDNSNsIPv6Addr2": systemDNSNsIPv6Addr2,
       "systemDNSNsIPv6Addr3": systemDNSNsIPv6Addr3,
       "alcatelIND1SystemMIBConformance": alcatelIND1SystemMIBConformance,
       "alcatelIND1SystemMIBGroups": alcatelIND1SystemMIBGroups,
       "systemMicrocodeGroup": systemMicrocodeGroup,
       "systemBootParamsGroup": systemBootParamsGroup,
       "systemHardwareGroup": systemHardwareGroup,
       "systemServicesGroup": systemServicesGroup,
       "systemFileSystemGroup": systemFileSystemGroup,
       "systemSwitchLoggingGroup": systemSwitchLoggingGroup,
       "systemDNSGroup": systemDNSGroup,
       "alcatelIND1SystemMIBCompliances": alcatelIND1SystemMIBCompliances,
       "alcatelIND1SystemMIBCompliance": alcatelIND1SystemMIBCompliance}
)
