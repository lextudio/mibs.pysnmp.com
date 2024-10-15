# SNMP MIB module (ONEACCESS-SYS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ONEACCESS-SYS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:35:05 2024
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

(oacExpIMSystem,
 oacMIBModules) = mibBuilder.importSymbols(
    "ONEACCESS-GLOBAL-REG",
    "oacExpIMSystem",
    "oacMIBModules")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

oacSysMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 1, 100, 671)
)
oacSysMIBModule.setRevisions(
        ("2014-05-05 00:01",
         "2011-06-15 00:00",
         "2010-12-14 00:01",
         "2010-08-11 10:00",
         "2010-07-08 10:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class OASysHwcClass(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("board", 0),
          ("cpu", 1),
          ("slot", 2))
    )



class OASysHwcType(Integer32, TextualConvention):
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
              6)
        )
    )
    namedValues = NamedValues(
        *(("dsp", 4),
          ("flash", 3),
          ("mainboard", 0),
          ("microprocessor", 1),
          ("module", 6),
          ("ram", 2),
          ("uplink", 5))
    )



class OASysCoreType(Integer32, TextualConvention):
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
        *(("application", 2),
          ("controlplane", 0),
          ("dataforwarding", 1),
          ("mixed", 3))
    )



# MIB Managed Objects in the order of their OIDs

_OacExpIMSysStatistics_ObjectIdentity = ObjectIdentity
oacExpIMSysStatistics = _OacExpIMSysStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 1)
)
_OacSysMemStatistics_ObjectIdentity = ObjectIdentity
oacSysMemStatistics = _OacSysMemStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 1, 1)
)
_OacSysMemoryFree_Type = Unsigned32
_OacSysMemoryFree_Object = MibScalar
oacSysMemoryFree = _OacSysMemoryFree_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 1, 1, 1),
    _OacSysMemoryFree_Type()
)
oacSysMemoryFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacSysMemoryFree.setStatus("current")
_OacSysMemoryAllocated_Type = Unsigned32
_OacSysMemoryAllocated_Object = MibScalar
oacSysMemoryAllocated = _OacSysMemoryAllocated_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 1, 1, 2),
    _OacSysMemoryAllocated_Type()
)
oacSysMemoryAllocated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacSysMemoryAllocated.setStatus("current")
_OacSysMemoryTotal_Type = Unsigned32
_OacSysMemoryTotal_Object = MibScalar
oacSysMemoryTotal = _OacSysMemoryTotal_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 1, 1, 3),
    _OacSysMemoryTotal_Type()
)
oacSysMemoryTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacSysMemoryTotal.setStatus("current")
_OacSysMemoryUsed_Type = Unsigned32
_OacSysMemoryUsed_Object = MibScalar
oacSysMemoryUsed = _OacSysMemoryUsed_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 1, 1, 4),
    _OacSysMemoryUsed_Type()
)
oacSysMemoryUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacSysMemoryUsed.setStatus("current")
_OacSysCpuStatistics_ObjectIdentity = ObjectIdentity
oacSysCpuStatistics = _OacSysCpuStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 1, 2)
)
_OacSysCpuUsed_Type = Unsigned32
_OacSysCpuUsed_Object = MibScalar
oacSysCpuUsed = _OacSysCpuUsed_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 1, 2, 1),
    _OacSysCpuUsed_Type()
)
oacSysCpuUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacSysCpuUsed.setStatus("current")
_OacSysCpuUsedCoresCount_Type = Unsigned32
_OacSysCpuUsedCoresCount_Object = MibScalar
oacSysCpuUsedCoresCount = _OacSysCpuUsedCoresCount_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 1, 2, 2),
    _OacSysCpuUsedCoresCount_Type()
)
oacSysCpuUsedCoresCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacSysCpuUsedCoresCount.setStatus("current")
_OacSysCpuUsedCoresTable_Object = MibTable
oacSysCpuUsedCoresTable = _OacSysCpuUsedCoresTable_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 1, 2, 3)
)
if mibBuilder.loadTexts:
    oacSysCpuUsedCoresTable.setStatus("current")
_OacSysCpuUsedCoresEntry_Object = MibTableRow
oacSysCpuUsedCoresEntry = _OacSysCpuUsedCoresEntry_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 1, 2, 3, 1)
)
oacSysCpuUsedCoresEntry.setIndexNames(
    (0, "ONEACCESS-SYS-MIB", "oacSysCpuUsedIndex"),
)
if mibBuilder.loadTexts:
    oacSysCpuUsedCoresEntry.setStatus("current")
_OacSysCpuUsedIndex_Type = Unsigned32
_OacSysCpuUsedIndex_Object = MibTableColumn
oacSysCpuUsedIndex = _OacSysCpuUsedIndex_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 1, 2, 3, 1, 1),
    _OacSysCpuUsedIndex_Type()
)
oacSysCpuUsedIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacSysCpuUsedIndex.setStatus("current")
_OacSysCpuUsedCoreType_Type = OASysCoreType
_OacSysCpuUsedCoreType_Object = MibTableColumn
oacSysCpuUsedCoreType = _OacSysCpuUsedCoreType_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 1, 2, 3, 1, 2),
    _OacSysCpuUsedCoreType_Type()
)
oacSysCpuUsedCoreType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacSysCpuUsedCoreType.setStatus("current")
_OacSysCpuUsedValue_Type = Unsigned32
_OacSysCpuUsedValue_Object = MibTableColumn
oacSysCpuUsedValue = _OacSysCpuUsedValue_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 1, 2, 3, 1, 3),
    _OacSysCpuUsedValue_Type()
)
oacSysCpuUsedValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacSysCpuUsedValue.setStatus("current")
_OacSysCpuUsedOneMinuteValue_Type = Unsigned32
_OacSysCpuUsedOneMinuteValue_Object = MibTableColumn
oacSysCpuUsedOneMinuteValue = _OacSysCpuUsedOneMinuteValue_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 1, 2, 3, 1, 4),
    _OacSysCpuUsedOneMinuteValue_Type()
)
oacSysCpuUsedOneMinuteValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacSysCpuUsedOneMinuteValue.setStatus("current")
_OacSysLastRebootCause_Type = DisplayString
_OacSysLastRebootCause_Object = MibScalar
oacSysLastRebootCause = _OacSysLastRebootCause_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 1, 3),
    _OacSysLastRebootCause_Type()
)
oacSysLastRebootCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacSysLastRebootCause.setStatus("current")
_OacSysSecureCrashlogCount_Type = Integer32
_OacSysSecureCrashlogCount_Object = MibScalar
oacSysSecureCrashlogCount = _OacSysSecureCrashlogCount_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 1, 100),
    _OacSysSecureCrashlogCount_Type()
)
oacSysSecureCrashlogCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacSysSecureCrashlogCount.setStatus("current")


class _OacSysStartCaused_Type(DisplayString):
    """Custom type oacSysStartCaused based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_OacSysStartCaused_Type.__name__ = "DisplayString"
_OacSysStartCaused_Object = MibScalar
oacSysStartCaused = _OacSysStartCaused_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 1, 200),
    _OacSysStartCaused_Type()
)
oacSysStartCaused.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacSysStartCaused.setStatus("current")
_OacExpIMSysHardwareDescription_ObjectIdentity = ObjectIdentity
oacExpIMSysHardwareDescription = _OacExpIMSysHardwareDescription_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 2)
)
_OacSysIMSysMainBoard_ObjectIdentity = ObjectIdentity
oacSysIMSysMainBoard = _OacSysIMSysMainBoard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 2, 1)
)
_OacSysIMSysMainIdentifier_Type = ObjectIdentifier
_OacSysIMSysMainIdentifier_Object = MibScalar
oacSysIMSysMainIdentifier = _OacSysIMSysMainIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 2, 1, 1),
    _OacSysIMSysMainIdentifier_Type()
)
oacSysIMSysMainIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacSysIMSysMainIdentifier.setStatus("current")


class _OacSysIMSysMainManufacturedIdentity_Type(DisplayString):
    """Custom type oacSysIMSysMainManufacturedIdentity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_OacSysIMSysMainManufacturedIdentity_Type.__name__ = "DisplayString"
_OacSysIMSysMainManufacturedIdentity_Object = MibScalar
oacSysIMSysMainManufacturedIdentity = _OacSysIMSysMainManufacturedIdentity_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 2, 1, 2),
    _OacSysIMSysMainManufacturedIdentity_Type()
)
oacSysIMSysMainManufacturedIdentity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacSysIMSysMainManufacturedIdentity.setStatus("current")


class _OacSysIMSysMainManufacturedDate_Type(DisplayString):
    """Custom type oacSysIMSysMainManufacturedDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_OacSysIMSysMainManufacturedDate_Type.__name__ = "DisplayString"
_OacSysIMSysMainManufacturedDate_Object = MibScalar
oacSysIMSysMainManufacturedDate = _OacSysIMSysMainManufacturedDate_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 2, 1, 3),
    _OacSysIMSysMainManufacturedDate_Type()
)
oacSysIMSysMainManufacturedDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacSysIMSysMainManufacturedDate.setStatus("current")


class _OacSysIMSysMainCPU_Type(DisplayString):
    """Custom type oacSysIMSysMainCPU based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_OacSysIMSysMainCPU_Type.__name__ = "DisplayString"
_OacSysIMSysMainCPU_Object = MibScalar
oacSysIMSysMainCPU = _OacSysIMSysMainCPU_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 2, 1, 4),
    _OacSysIMSysMainCPU_Type()
)
oacSysIMSysMainCPU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacSysIMSysMainCPU.setStatus("current")


class _OacSysIMSysMainBSPVersion_Type(DisplayString):
    """Custom type oacSysIMSysMainBSPVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_OacSysIMSysMainBSPVersion_Type.__name__ = "DisplayString"
_OacSysIMSysMainBSPVersion_Object = MibScalar
oacSysIMSysMainBSPVersion = _OacSysIMSysMainBSPVersion_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 2, 1, 5),
    _OacSysIMSysMainBSPVersion_Type()
)
oacSysIMSysMainBSPVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacSysIMSysMainBSPVersion.setStatus("current")


class _OacSysIMSysMainBootVersion_Type(DisplayString):
    """Custom type oacSysIMSysMainBootVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_OacSysIMSysMainBootVersion_Type.__name__ = "DisplayString"
_OacSysIMSysMainBootVersion_Object = MibScalar
oacSysIMSysMainBootVersion = _OacSysIMSysMainBootVersion_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 2, 1, 6),
    _OacSysIMSysMainBootVersion_Type()
)
oacSysIMSysMainBootVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacSysIMSysMainBootVersion.setStatus("current")


class _OacSysIMSysMainBootDateCreation_Type(DisplayString):
    """Custom type oacSysIMSysMainBootDateCreation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_OacSysIMSysMainBootDateCreation_Type.__name__ = "DisplayString"
_OacSysIMSysMainBootDateCreation_Object = MibScalar
oacSysIMSysMainBootDateCreation = _OacSysIMSysMainBootDateCreation_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 2, 1, 7),
    _OacSysIMSysMainBootDateCreation_Type()
)
oacSysIMSysMainBootDateCreation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacSysIMSysMainBootDateCreation.setStatus("current")
_OacExpIMSysHwComponents_ObjectIdentity = ObjectIdentity
oacExpIMSysHwComponents = _OacExpIMSysHwComponents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 2, 2)
)
_OacExpIMSysHwComponentsCount_Type = Unsigned32
_OacExpIMSysHwComponentsCount_Object = MibScalar
oacExpIMSysHwComponentsCount = _OacExpIMSysHwComponentsCount_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 2, 2, 1),
    _OacExpIMSysHwComponentsCount_Type()
)
oacExpIMSysHwComponentsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacExpIMSysHwComponentsCount.setStatus("current")
_OacExpIMSysHwComponentsTable_Object = MibTable
oacExpIMSysHwComponentsTable = _OacExpIMSysHwComponentsTable_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 2, 2, 2)
)
if mibBuilder.loadTexts:
    oacExpIMSysHwComponentsTable.setStatus("current")
_OacExpIMSysHwComponentsEntry_Object = MibTableRow
oacExpIMSysHwComponentsEntry = _OacExpIMSysHwComponentsEntry_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 2, 2, 2, 1)
)
oacExpIMSysHwComponentsEntry.setIndexNames(
    (0, "ONEACCESS-SYS-MIB", "oacExpIMSysHwcIndex"),
)
if mibBuilder.loadTexts:
    oacExpIMSysHwComponentsEntry.setStatus("current")
_OacExpIMSysHwcIndex_Type = Unsigned32
_OacExpIMSysHwcIndex_Object = MibTableColumn
oacExpIMSysHwcIndex = _OacExpIMSysHwcIndex_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 2, 2, 2, 1, 1),
    _OacExpIMSysHwcIndex_Type()
)
oacExpIMSysHwcIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacExpIMSysHwcIndex.setStatus("current")
_OacExpIMSysHwcClass_Type = OASysHwcClass
_OacExpIMSysHwcClass_Object = MibTableColumn
oacExpIMSysHwcClass = _OacExpIMSysHwcClass_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 2, 2, 2, 1, 2),
    _OacExpIMSysHwcClass_Type()
)
oacExpIMSysHwcClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacExpIMSysHwcClass.setStatus("current")
_OacExpIMSysHwcType_Type = OASysHwcType
_OacExpIMSysHwcType_Object = MibTableColumn
oacExpIMSysHwcType = _OacExpIMSysHwcType_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 2, 2, 2, 1, 3),
    _OacExpIMSysHwcType_Type()
)
oacExpIMSysHwcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacExpIMSysHwcType.setStatus("current")
_OacExpIMSysHwcDescription_Type = DisplayString
_OacExpIMSysHwcDescription_Object = MibTableColumn
oacExpIMSysHwcDescription = _OacExpIMSysHwcDescription_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 2, 2, 2, 1, 4),
    _OacExpIMSysHwcDescription_Type()
)
oacExpIMSysHwcDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacExpIMSysHwcDescription.setStatus("current")
_OacExpIMSysHwcSerialNumber_Type = DisplayString
_OacExpIMSysHwcSerialNumber_Object = MibTableColumn
oacExpIMSysHwcSerialNumber = _OacExpIMSysHwcSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 2, 2, 2, 1, 5),
    _OacExpIMSysHwcSerialNumber_Type()
)
oacExpIMSysHwcSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacExpIMSysHwcSerialNumber.setStatus("current")
_OacExpIMSysHwcManufacturer_Type = DisplayString
_OacExpIMSysHwcManufacturer_Object = MibTableColumn
oacExpIMSysHwcManufacturer = _OacExpIMSysHwcManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 2, 2, 2, 1, 6),
    _OacExpIMSysHwcManufacturer_Type()
)
oacExpIMSysHwcManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacExpIMSysHwcManufacturer.setStatus("current")


class _OacExpIMSysHwcManufacturedDate_Type(DisplayString):
    """Custom type oacExpIMSysHwcManufacturedDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_OacExpIMSysHwcManufacturedDate_Type.__name__ = "DisplayString"
_OacExpIMSysHwcManufacturedDate_Object = MibTableColumn
oacExpIMSysHwcManufacturedDate = _OacExpIMSysHwcManufacturedDate_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 2, 2, 2, 1, 7),
    _OacExpIMSysHwcManufacturedDate_Type()
)
oacExpIMSysHwcManufacturedDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacExpIMSysHwcManufacturedDate.setStatus("current")


class _OacExpIMSysHwcProductName_Type(DisplayString):
    """Custom type oacExpIMSysHwcProductName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_OacExpIMSysHwcProductName_Type.__name__ = "DisplayString"
_OacExpIMSysHwcProductName_Object = MibTableColumn
oacExpIMSysHwcProductName = _OacExpIMSysHwcProductName_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 2, 2, 2, 1, 8),
    _OacExpIMSysHwcProductName_Type()
)
oacExpIMSysHwcProductName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacExpIMSysHwcProductName.setStatus("current")
_OacExpIMSysFactory_ObjectIdentity = ObjectIdentity
oacExpIMSysFactory = _OacExpIMSysFactory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 2, 3)
)


class _OacExpIMSysFactorySupplierID_Type(DisplayString):
    """Custom type oacExpIMSysFactorySupplierID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_OacExpIMSysFactorySupplierID_Type.__name__ = "DisplayString"
_OacExpIMSysFactorySupplierID_Object = MibScalar
oacExpIMSysFactorySupplierID = _OacExpIMSysFactorySupplierID_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 2, 3, 1),
    _OacExpIMSysFactorySupplierID_Type()
)
oacExpIMSysFactorySupplierID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacExpIMSysFactorySupplierID.setStatus("current")


class _OacExpIMSysFactoryProductSalesCode_Type(DisplayString):
    """Custom type oacExpIMSysFactoryProductSalesCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 22),
    )


_OacExpIMSysFactoryProductSalesCode_Type.__name__ = "DisplayString"
_OacExpIMSysFactoryProductSalesCode_Object = MibScalar
oacExpIMSysFactoryProductSalesCode = _OacExpIMSysFactoryProductSalesCode_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 2, 3, 2),
    _OacExpIMSysFactoryProductSalesCode_Type()
)
oacExpIMSysFactoryProductSalesCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacExpIMSysFactoryProductSalesCode.setStatus("current")


class _OacExpIMSysFactoryHwRevision_Type(DisplayString):
    """Custom type oacExpIMSysFactoryHwRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 7),
    )


_OacExpIMSysFactoryHwRevision_Type.__name__ = "DisplayString"
_OacExpIMSysFactoryHwRevision_Object = MibScalar
oacExpIMSysFactoryHwRevision = _OacExpIMSysFactoryHwRevision_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 2, 3, 3),
    _OacExpIMSysFactoryHwRevision_Type()
)
oacExpIMSysFactoryHwRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacExpIMSysFactoryHwRevision.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ONEACCESS-SYS-MIB",
    **{"OASysHwcClass": OASysHwcClass,
       "OASysHwcType": OASysHwcType,
       "OASysCoreType": OASysCoreType,
       "oacSysMIBModule": oacSysMIBModule,
       "oacExpIMSysStatistics": oacExpIMSysStatistics,
       "oacSysMemStatistics": oacSysMemStatistics,
       "oacSysMemoryFree": oacSysMemoryFree,
       "oacSysMemoryAllocated": oacSysMemoryAllocated,
       "oacSysMemoryTotal": oacSysMemoryTotal,
       "oacSysMemoryUsed": oacSysMemoryUsed,
       "oacSysCpuStatistics": oacSysCpuStatistics,
       "oacSysCpuUsed": oacSysCpuUsed,
       "oacSysCpuUsedCoresCount": oacSysCpuUsedCoresCount,
       "oacSysCpuUsedCoresTable": oacSysCpuUsedCoresTable,
       "oacSysCpuUsedCoresEntry": oacSysCpuUsedCoresEntry,
       "oacSysCpuUsedIndex": oacSysCpuUsedIndex,
       "oacSysCpuUsedCoreType": oacSysCpuUsedCoreType,
       "oacSysCpuUsedValue": oacSysCpuUsedValue,
       "oacSysCpuUsedOneMinuteValue": oacSysCpuUsedOneMinuteValue,
       "oacSysLastRebootCause": oacSysLastRebootCause,
       "oacSysSecureCrashlogCount": oacSysSecureCrashlogCount,
       "oacSysStartCaused": oacSysStartCaused,
       "oacExpIMSysHardwareDescription": oacExpIMSysHardwareDescription,
       "oacSysIMSysMainBoard": oacSysIMSysMainBoard,
       "oacSysIMSysMainIdentifier": oacSysIMSysMainIdentifier,
       "oacSysIMSysMainManufacturedIdentity": oacSysIMSysMainManufacturedIdentity,
       "oacSysIMSysMainManufacturedDate": oacSysIMSysMainManufacturedDate,
       "oacSysIMSysMainCPU": oacSysIMSysMainCPU,
       "oacSysIMSysMainBSPVersion": oacSysIMSysMainBSPVersion,
       "oacSysIMSysMainBootVersion": oacSysIMSysMainBootVersion,
       "oacSysIMSysMainBootDateCreation": oacSysIMSysMainBootDateCreation,
       "oacExpIMSysHwComponents": oacExpIMSysHwComponents,
       "oacExpIMSysHwComponentsCount": oacExpIMSysHwComponentsCount,
       "oacExpIMSysHwComponentsTable": oacExpIMSysHwComponentsTable,
       "oacExpIMSysHwComponentsEntry": oacExpIMSysHwComponentsEntry,
       "oacExpIMSysHwcIndex": oacExpIMSysHwcIndex,
       "oacExpIMSysHwcClass": oacExpIMSysHwcClass,
       "oacExpIMSysHwcType": oacExpIMSysHwcType,
       "oacExpIMSysHwcDescription": oacExpIMSysHwcDescription,
       "oacExpIMSysHwcSerialNumber": oacExpIMSysHwcSerialNumber,
       "oacExpIMSysHwcManufacturer": oacExpIMSysHwcManufacturer,
       "oacExpIMSysHwcManufacturedDate": oacExpIMSysHwcManufacturedDate,
       "oacExpIMSysHwcProductName": oacExpIMSysHwcProductName,
       "oacExpIMSysFactory": oacExpIMSysFactory,
       "oacExpIMSysFactorySupplierID": oacExpIMSysFactorySupplierID,
       "oacExpIMSysFactoryProductSalesCode": oacExpIMSysFactoryProductSalesCode,
       "oacExpIMSysFactoryHwRevision": oacExpIMSysFactoryHwRevision}
)
