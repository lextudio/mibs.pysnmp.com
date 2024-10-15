# SNMP MIB module (CHASSISMGREXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CHASSISMGREXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:54:36 2024
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

(chassisMgrExt,) = mibBuilder.importSymbols(
    "APENT-MIB",
    "chassisMgrExt")

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

chassisMgrExtMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2467, 1, 34, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _ApChassisMgrExtChassisType_Type(Integer32):
    """Custom type apChassisMgrExtChassisType based on Integer32"""
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
        *(("unknown", 4),
          ("ws100", 0),
          ("ws150", 2),
          ("ws50", 3),
          ("ws800", 1))
    )


_ApChassisMgrExtChassisType_Type.__name__ = "Integer32"
_ApChassisMgrExtChassisType_Object = MibScalar
apChassisMgrExtChassisType = _ApChassisMgrExtChassisType_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 34, 2),
    _ApChassisMgrExtChassisType_Type()
)
apChassisMgrExtChassisType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apChassisMgrExtChassisType.setStatus("current")


class _ApChassisMgrExtChassisName_Type(DisplayString):
    """Custom type apChassisMgrExtChassisName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_ApChassisMgrExtChassisName_Type.__name__ = "DisplayString"
_ApChassisMgrExtChassisName_Object = MibScalar
apChassisMgrExtChassisName = _ApChassisMgrExtChassisName_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 34, 3),
    _ApChassisMgrExtChassisName_Type()
)
apChassisMgrExtChassisName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apChassisMgrExtChassisName.setStatus("current")


class _ApChassisMgrExtChassisSerialNumber_Type(DisplayString):
    """Custom type apChassisMgrExtChassisSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ApChassisMgrExtChassisSerialNumber_Type.__name__ = "DisplayString"
_ApChassisMgrExtChassisSerialNumber_Object = MibScalar
apChassisMgrExtChassisSerialNumber = _ApChassisMgrExtChassisSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 34, 4),
    _ApChassisMgrExtChassisSerialNumber_Type()
)
apChassisMgrExtChassisSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apChassisMgrExtChassisSerialNumber.setStatus("current")


class _ApChassisMgrExtNumberSlots_Type(Integer32):
    """Custom type apChassisMgrExtNumberSlots based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 14),
    )


_ApChassisMgrExtNumberSlots_Type.__name__ = "Integer32"
_ApChassisMgrExtNumberSlots_Object = MibScalar
apChassisMgrExtNumberSlots = _ApChassisMgrExtNumberSlots_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 34, 5),
    _ApChassisMgrExtNumberSlots_Type()
)
apChassisMgrExtNumberSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apChassisMgrExtNumberSlots.setStatus("current")
_ApChassisMgrExtNumberModules_Type = Integer32
_ApChassisMgrExtNumberModules_Object = MibScalar
apChassisMgrExtNumberModules = _ApChassisMgrExtNumberModules_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 34, 6),
    _ApChassisMgrExtNumberModules_Type()
)
apChassisMgrExtNumberModules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apChassisMgrExtNumberModules.setStatus("current")


class _ApChassisMgrExtNumberPowerSupplies_Type(Integer32):
    """Custom type apChassisMgrExtNumberPowerSupplies based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_ApChassisMgrExtNumberPowerSupplies_Type.__name__ = "Integer32"
_ApChassisMgrExtNumberPowerSupplies_Object = MibScalar
apChassisMgrExtNumberPowerSupplies = _ApChassisMgrExtNumberPowerSupplies_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 34, 7),
    _ApChassisMgrExtNumberPowerSupplies_Type()
)
apChassisMgrExtNumberPowerSupplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apChassisMgrExtNumberPowerSupplies.setStatus("current")


class _ApChassisMgrExtNumberFans_Type(Integer32):
    """Custom type apChassisMgrExtNumberFans based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_ApChassisMgrExtNumberFans_Type.__name__ = "Integer32"
_ApChassisMgrExtNumberFans_Object = MibScalar
apChassisMgrExtNumberFans = _ApChassisMgrExtNumberFans_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 34, 8),
    _ApChassisMgrExtNumberFans_Type()
)
apChassisMgrExtNumberFans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apChassisMgrExtNumberFans.setStatus("current")


class _ApChassisMgrExtSoftwareVersionNumber_Type(DisplayString):
    """Custom type apChassisMgrExtSoftwareVersionNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_ApChassisMgrExtSoftwareVersionNumber_Type.__name__ = "DisplayString"
_ApChassisMgrExtSoftwareVersionNumber_Object = MibScalar
apChassisMgrExtSoftwareVersionNumber = _ApChassisMgrExtSoftwareVersionNumber_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 34, 9),
    _ApChassisMgrExtSoftwareVersionNumber_Type()
)
apChassisMgrExtSoftwareVersionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apChassisMgrExtSoftwareVersionNumber.setStatus("current")


class _ApChassisMgrExtBootpState_Type(Integer32):
    """Custom type apChassisMgrExtBootpState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("bootp-disabled", 0),
          ("bootp-enabled", 1))
    )


_ApChassisMgrExtBootpState_Type.__name__ = "Integer32"
_ApChassisMgrExtBootpState_Object = MibScalar
apChassisMgrExtBootpState = _ApChassisMgrExtBootpState_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 34, 10),
    _ApChassisMgrExtBootpState_Type()
)
apChassisMgrExtBootpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apChassisMgrExtBootpState.setStatus("current")
_ApChassisMgrExtMgmtPortIpAddress_Type = IpAddress
_ApChassisMgrExtMgmtPortIpAddress_Object = MibScalar
apChassisMgrExtMgmtPortIpAddress = _ApChassisMgrExtMgmtPortIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 34, 11),
    _ApChassisMgrExtMgmtPortIpAddress_Type()
)
apChassisMgrExtMgmtPortIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apChassisMgrExtMgmtPortIpAddress.setStatus("current")


class _ApChassisMgrExtBaseEthernetAddress_Type(DisplayString):
    """Custom type apChassisMgrExtBaseEthernetAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 18),
    )


_ApChassisMgrExtBaseEthernetAddress_Type.__name__ = "DisplayString"
_ApChassisMgrExtBaseEthernetAddress_Object = MibScalar
apChassisMgrExtBaseEthernetAddress = _ApChassisMgrExtBaseEthernetAddress_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 34, 12),
    _ApChassisMgrExtBaseEthernetAddress_Type()
)
apChassisMgrExtBaseEthernetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apChassisMgrExtBaseEthernetAddress.setStatus("current")
_ApChassisMgrExtCpuUtilization_Type = Integer32
_ApChassisMgrExtCpuUtilization_Object = MibScalar
apChassisMgrExtCpuUtilization = _ApChassisMgrExtCpuUtilization_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 34, 13),
    _ApChassisMgrExtCpuUtilization_Type()
)
apChassisMgrExtCpuUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apChassisMgrExtCpuUtilization.setStatus("current")


class _ApChassisMgrExtMajorHwVersion_Type(DisplayString):
    """Custom type apChassisMgrExtMajorHwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ApChassisMgrExtMajorHwVersion_Type.__name__ = "DisplayString"
_ApChassisMgrExtMajorHwVersion_Object = MibScalar
apChassisMgrExtMajorHwVersion = _ApChassisMgrExtMajorHwVersion_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 34, 14),
    _ApChassisMgrExtMajorHwVersion_Type()
)
apChassisMgrExtMajorHwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apChassisMgrExtMajorHwVersion.setStatus("current")


class _ApChassisMgrExtMinorHwVersion_Type(DisplayString):
    """Custom type apChassisMgrExtMinorHwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ApChassisMgrExtMinorHwVersion_Type.__name__ = "DisplayString"
_ApChassisMgrExtMinorHwVersion_Object = MibScalar
apChassisMgrExtMinorHwVersion = _ApChassisMgrExtMinorHwVersion_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 34, 15),
    _ApChassisMgrExtMinorHwVersion_Type()
)
apChassisMgrExtMinorHwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apChassisMgrExtMinorHwVersion.setStatus("current")
_ApChassisMgrExtModuleTable_Object = MibTable
apChassisMgrExtModuleTable = _ApChassisMgrExtModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 34, 16)
)
if mibBuilder.loadTexts:
    apChassisMgrExtModuleTable.setStatus("current")
_ApChassisMgrExtModuleEntry_Object = MibTableRow
apChassisMgrExtModuleEntry = _ApChassisMgrExtModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 34, 16, 1)
)
apChassisMgrExtModuleEntry.setIndexNames(
    (0, "CHASSISMGREXT-MIB", "apChassisMgrExtModuleSlotNumber"),
)
if mibBuilder.loadTexts:
    apChassisMgrExtModuleEntry.setStatus("current")


class _ApChassisMgrExtModuleSlotNumber_Type(Integer32):
    """Custom type apChassisMgrExtModuleSlotNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
    )


_ApChassisMgrExtModuleSlotNumber_Type.__name__ = "Integer32"
_ApChassisMgrExtModuleSlotNumber_Object = MibTableColumn
apChassisMgrExtModuleSlotNumber = _ApChassisMgrExtModuleSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 34, 16, 1, 2),
    _ApChassisMgrExtModuleSlotNumber_Type()
)
apChassisMgrExtModuleSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apChassisMgrExtModuleSlotNumber.setStatus("current")


class _ApChassisMgrExtModuleType_Type(Integer32):
    """Custom type apChassisMgrExtModuleType based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("dual-hssi", 4),
          ("fem", 5),
          ("fem-t1", 3),
          ("fenic", 6),
          ("gem", 8),
          ("genic", 7),
          ("scfm", 2),
          ("scm", 0),
          ("sfm", 1),
          ("unknown", 9))
    )


_ApChassisMgrExtModuleType_Type.__name__ = "Integer32"
_ApChassisMgrExtModuleType_Object = MibTableColumn
apChassisMgrExtModuleType = _ApChassisMgrExtModuleType_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 34, 16, 1, 3),
    _ApChassisMgrExtModuleType_Type()
)
apChassisMgrExtModuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apChassisMgrExtModuleType.setStatus("current")


class _ApChassisMgrExtModuleName_Type(DisplayString):
    """Custom type apChassisMgrExtModuleName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ApChassisMgrExtModuleName_Type.__name__ = "DisplayString"
_ApChassisMgrExtModuleName_Object = MibTableColumn
apChassisMgrExtModuleName = _ApChassisMgrExtModuleName_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 34, 16, 1, 4),
    _ApChassisMgrExtModuleName_Type()
)
apChassisMgrExtModuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apChassisMgrExtModuleName.setStatus("current")


class _ApChassisMgrExtModuleSerialNumber_Type(DisplayString):
    """Custom type apChassisMgrExtModuleSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ApChassisMgrExtModuleSerialNumber_Type.__name__ = "DisplayString"
_ApChassisMgrExtModuleSerialNumber_Object = MibTableColumn
apChassisMgrExtModuleSerialNumber = _ApChassisMgrExtModuleSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 34, 16, 1, 5),
    _ApChassisMgrExtModuleSerialNumber_Type()
)
apChassisMgrExtModuleSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apChassisMgrExtModuleSerialNumber.setStatus("current")


class _ApChassisMgrExtModuleOpStatus_Type(Integer32):
    """Custom type apChassisMgrExtModuleOpStatus based on Integer32"""
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
        *(("backup", 3),
          ("bad", 4),
          ("powered-off", 0),
          ("powered-on", 1),
          ("primary", 2),
          ("unknown", 5))
    )


_ApChassisMgrExtModuleOpStatus_Type.__name__ = "Integer32"
_ApChassisMgrExtModuleOpStatus_Object = MibTableColumn
apChassisMgrExtModuleOpStatus = _ApChassisMgrExtModuleOpStatus_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 34, 16, 1, 6),
    _ApChassisMgrExtModuleOpStatus_Type()
)
apChassisMgrExtModuleOpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apChassisMgrExtModuleOpStatus.setStatus("current")


class _ApChassisMgrExtModuleNumSubModules_Type(Integer32):
    """Custom type apChassisMgrExtModuleNumSubModules based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_ApChassisMgrExtModuleNumSubModules_Type.__name__ = "Integer32"
_ApChassisMgrExtModuleNumSubModules_Object = MibTableColumn
apChassisMgrExtModuleNumSubModules = _ApChassisMgrExtModuleNumSubModules_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 34, 16, 1, 7),
    _ApChassisMgrExtModuleNumSubModules_Type()
)
apChassisMgrExtModuleNumSubModules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apChassisMgrExtModuleNumSubModules.setStatus("current")


class _ApChassisMgrExtModuleMajorHwVersion_Type(DisplayString):
    """Custom type apChassisMgrExtModuleMajorHwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ApChassisMgrExtModuleMajorHwVersion_Type.__name__ = "DisplayString"
_ApChassisMgrExtModuleMajorHwVersion_Object = MibTableColumn
apChassisMgrExtModuleMajorHwVersion = _ApChassisMgrExtModuleMajorHwVersion_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 34, 16, 1, 8),
    _ApChassisMgrExtModuleMajorHwVersion_Type()
)
apChassisMgrExtModuleMajorHwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apChassisMgrExtModuleMajorHwVersion.setStatus("current")


class _ApChassisMgrExtModuleMinorHwVersion_Type(DisplayString):
    """Custom type apChassisMgrExtModuleMinorHwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ApChassisMgrExtModuleMinorHwVersion_Type.__name__ = "DisplayString"
_ApChassisMgrExtModuleMinorHwVersion_Object = MibTableColumn
apChassisMgrExtModuleMinorHwVersion = _ApChassisMgrExtModuleMinorHwVersion_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 34, 16, 1, 9),
    _ApChassisMgrExtModuleMinorHwVersion_Type()
)
apChassisMgrExtModuleMinorHwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apChassisMgrExtModuleMinorHwVersion.setStatus("current")
_ApChassisMgrExtSubModuleTable_Object = MibTable
apChassisMgrExtSubModuleTable = _ApChassisMgrExtSubModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 34, 17)
)
if mibBuilder.loadTexts:
    apChassisMgrExtSubModuleTable.setStatus("current")
_ApChassisMgrExtSubModuleEntry_Object = MibTableRow
apChassisMgrExtSubModuleEntry = _ApChassisMgrExtSubModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 34, 17, 1)
)
apChassisMgrExtSubModuleEntry.setIndexNames(
    (0, "CHASSISMGREXT-MIB", "apChassisMgrExtSubModuleSlot"),
    (0, "CHASSISMGREXT-MIB", "apChassisMgrExtSubModuleSubSlot"),
)
if mibBuilder.loadTexts:
    apChassisMgrExtSubModuleEntry.setStatus("current")


class _ApChassisMgrExtSubModuleSlot_Type(Integer32):
    """Custom type apChassisMgrExtSubModuleSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
    )


_ApChassisMgrExtSubModuleSlot_Type.__name__ = "Integer32"
_ApChassisMgrExtSubModuleSlot_Object = MibTableColumn
apChassisMgrExtSubModuleSlot = _ApChassisMgrExtSubModuleSlot_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 34, 17, 1, 1),
    _ApChassisMgrExtSubModuleSlot_Type()
)
apChassisMgrExtSubModuleSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apChassisMgrExtSubModuleSlot.setStatus("current")


class _ApChassisMgrExtSubModuleSubSlot_Type(Integer32):
    """Custom type apChassisMgrExtSubModuleSubSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_ApChassisMgrExtSubModuleSubSlot_Type.__name__ = "Integer32"
_ApChassisMgrExtSubModuleSubSlot_Object = MibTableColumn
apChassisMgrExtSubModuleSubSlot = _ApChassisMgrExtSubModuleSubSlot_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 34, 17, 1, 2),
    _ApChassisMgrExtSubModuleSubSlot_Type()
)
apChassisMgrExtSubModuleSubSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apChassisMgrExtSubModuleSubSlot.setStatus("current")


class _ApChassisMgrExtSubModuleType_Type(Integer32):
    """Custom type apChassisMgrExtSubModuleType based on Integer32"""
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("epif-submodule", 5),
          ("genic-1port-submodule", 11),
          ("genic-2port-submodule", 10),
          ("hssi-submodule", 4),
          ("scfm-submodule", 2),
          ("scfm2-submodule", 9),
          ("scm-submodule", 0),
          ("sfm-submodule", 1),
          ("sfm2-submodule", 8),
          ("t1-submodule", 3),
          ("unknown-submodule", 12),
          ("v35-submodule", 6),
          ("xpif-submodule", 7))
    )


_ApChassisMgrExtSubModuleType_Type.__name__ = "Integer32"
_ApChassisMgrExtSubModuleType_Object = MibTableColumn
apChassisMgrExtSubModuleType = _ApChassisMgrExtSubModuleType_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 34, 17, 1, 3),
    _ApChassisMgrExtSubModuleType_Type()
)
apChassisMgrExtSubModuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apChassisMgrExtSubModuleType.setStatus("current")


class _ApChassisMgrExtSubModuleName_Type(DisplayString):
    """Custom type apChassisMgrExtSubModuleName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_ApChassisMgrExtSubModuleName_Type.__name__ = "DisplayString"
_ApChassisMgrExtSubModuleName_Object = MibTableColumn
apChassisMgrExtSubModuleName = _ApChassisMgrExtSubModuleName_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 34, 17, 1, 4),
    _ApChassisMgrExtSubModuleName_Type()
)
apChassisMgrExtSubModuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apChassisMgrExtSubModuleName.setStatus("current")


class _ApChassisMgrExtSubModuleOpStatus_Type(Integer32):
    """Custom type apChassisMgrExtSubModuleOpStatus based on Integer32"""
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("any", 11),
          ("bad", 3),
          ("going-offline", 5),
          ("going-online", 4),
          ("inserted", 6),
          ("offline-bad", 1),
          ("offline-ok", 0),
          ("online", 2),
          ("post", 7),
          ("post-bad-comm", 10),
          ("post-fail", 9),
          ("post-ok", 8),
          ("unknown-state", 12))
    )


_ApChassisMgrExtSubModuleOpStatus_Type.__name__ = "Integer32"
_ApChassisMgrExtSubModuleOpStatus_Object = MibTableColumn
apChassisMgrExtSubModuleOpStatus = _ApChassisMgrExtSubModuleOpStatus_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 34, 17, 1, 5),
    _ApChassisMgrExtSubModuleOpStatus_Type()
)
apChassisMgrExtSubModuleOpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apChassisMgrExtSubModuleOpStatus.setStatus("current")


class _ApChassisMgrExtSubModuleSsCardType_Type(Integer32):
    """Custom type apChassisMgrExtSubModuleSsCardType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hifen-hssi", 1),
          ("hifen-t1", 0),
          ("unknown", 2))
    )


_ApChassisMgrExtSubModuleSsCardType_Type.__name__ = "Integer32"
_ApChassisMgrExtSubModuleSsCardType_Object = MibTableColumn
apChassisMgrExtSubModuleSsCardType = _ApChassisMgrExtSubModuleSsCardType_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 34, 17, 1, 6),
    _ApChassisMgrExtSubModuleSsCardType_Type()
)
apChassisMgrExtSubModuleSsCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apChassisMgrExtSubModuleSsCardType.setStatus("current")


class _ApChassisMgrExtSubModuleSsCardOpStatus_Type(Integer32):
    """Custom type apChassisMgrExtSubModuleSsCardOpStatus based on Integer32"""
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
        *(("offline-bad", 1),
          ("offline-ok", 0),
          ("online", 2),
          ("unknown-state", 3))
    )


_ApChassisMgrExtSubModuleSsCardOpStatus_Type.__name__ = "Integer32"
_ApChassisMgrExtSubModuleSsCardOpStatus_Object = MibTableColumn
apChassisMgrExtSubModuleSsCardOpStatus = _ApChassisMgrExtSubModuleSsCardOpStatus_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 34, 17, 1, 7),
    _ApChassisMgrExtSubModuleSsCardOpStatus_Type()
)
apChassisMgrExtSubModuleSsCardOpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apChassisMgrExtSubModuleSsCardOpStatus.setStatus("current")


class _ApChassisMgrExtSubModulePortName_Type(DisplayString):
    """Custom type apChassisMgrExtSubModulePortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ApChassisMgrExtSubModulePortName_Type.__name__ = "DisplayString"
_ApChassisMgrExtSubModulePortName_Object = MibTableColumn
apChassisMgrExtSubModulePortName = _ApChassisMgrExtSubModulePortName_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 34, 17, 1, 8),
    _ApChassisMgrExtSubModulePortName_Type()
)
apChassisMgrExtSubModulePortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apChassisMgrExtSubModulePortName.setStatus("current")


class _ApChassisMgrExtSubModulePortNumber_Type(Integer32):
    """Custom type apChassisMgrExtSubModulePortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_ApChassisMgrExtSubModulePortNumber_Type.__name__ = "Integer32"
_ApChassisMgrExtSubModulePortNumber_Object = MibTableColumn
apChassisMgrExtSubModulePortNumber = _ApChassisMgrExtSubModulePortNumber_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 34, 17, 1, 9),
    _ApChassisMgrExtSubModulePortNumber_Type()
)
apChassisMgrExtSubModulePortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apChassisMgrExtSubModulePortNumber.setStatus("current")
_ApChassisMgrExtSubModuleSystemHeapFree_Type = Integer32
_ApChassisMgrExtSubModuleSystemHeapFree_Object = MibTableColumn
apChassisMgrExtSubModuleSystemHeapFree = _ApChassisMgrExtSubModuleSystemHeapFree_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 34, 17, 1, 10),
    _ApChassisMgrExtSubModuleSystemHeapFree_Type()
)
apChassisMgrExtSubModuleSystemHeapFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apChassisMgrExtSubModuleSystemHeapFree.setStatus("current")
_ApChassisMgrExtSubModuleSystemHeapChainDepth_Type = Integer32
_ApChassisMgrExtSubModuleSystemHeapChainDepth_Object = MibTableColumn
apChassisMgrExtSubModuleSystemHeapChainDepth = _ApChassisMgrExtSubModuleSystemHeapChainDepth_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 34, 17, 1, 11),
    _ApChassisMgrExtSubModuleSystemHeapChainDepth_Type()
)
apChassisMgrExtSubModuleSystemHeapChainDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apChassisMgrExtSubModuleSystemHeapChainDepth.setStatus("current")
_ApChassisMgrExtSubModuleInstalledMemory_Type = Integer32
_ApChassisMgrExtSubModuleInstalledMemory_Object = MibTableColumn
apChassisMgrExtSubModuleInstalledMemory = _ApChassisMgrExtSubModuleInstalledMemory_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 34, 17, 1, 12),
    _ApChassisMgrExtSubModuleInstalledMemory_Type()
)
apChassisMgrExtSubModuleInstalledMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apChassisMgrExtSubModuleInstalledMemory.setStatus("current")


class _ApChassisMgrExtSubModuleCPUInstantaneous_Type(Integer32):
    """Custom type apChassisMgrExtSubModuleCPUInstantaneous based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ApChassisMgrExtSubModuleCPUInstantaneous_Type.__name__ = "Integer32"
_ApChassisMgrExtSubModuleCPUInstantaneous_Object = MibTableColumn
apChassisMgrExtSubModuleCPUInstantaneous = _ApChassisMgrExtSubModuleCPUInstantaneous_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 34, 17, 1, 13),
    _ApChassisMgrExtSubModuleCPUInstantaneous_Type()
)
apChassisMgrExtSubModuleCPUInstantaneous.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apChassisMgrExtSubModuleCPUInstantaneous.setStatus("current")


class _ApChassisMgrExtSubModuleCPUAverage_Type(Integer32):
    """Custom type apChassisMgrExtSubModuleCPUAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ApChassisMgrExtSubModuleCPUAverage_Type.__name__ = "Integer32"
_ApChassisMgrExtSubModuleCPUAverage_Object = MibTableColumn
apChassisMgrExtSubModuleCPUAverage = _ApChassisMgrExtSubModuleCPUAverage_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 34, 17, 1, 14),
    _ApChassisMgrExtSubModuleCPUAverage_Type()
)
apChassisMgrExtSubModuleCPUAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apChassisMgrExtSubModuleCPUAverage.setStatus("current")
_ApChassisMgrExtSubModuleBufferTable_Object = MibTable
apChassisMgrExtSubModuleBufferTable = _ApChassisMgrExtSubModuleBufferTable_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 34, 18)
)
if mibBuilder.loadTexts:
    apChassisMgrExtSubModuleBufferTable.setStatus("current")
_ApChassisMgrExtSubModuleBufferEntry_Object = MibTableRow
apChassisMgrExtSubModuleBufferEntry = _ApChassisMgrExtSubModuleBufferEntry_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 34, 18, 1)
)
apChassisMgrExtSubModuleBufferEntry.setIndexNames(
    (0, "CHASSISMGREXT-MIB", "apChassisMgrExtSubModuleBufferPool"),
    (0, "CHASSISMGREXT-MIB", "apChassisMgrExtSubModuleBufferSlot"),
    (0, "CHASSISMGREXT-MIB", "apChassisMgrExtSubModuleBufferSubSlot"),
)
if mibBuilder.loadTexts:
    apChassisMgrExtSubModuleBufferEntry.setStatus("current")


class _ApChassisMgrExtSubModuleBufferPool_Type(Integer32):
    """Custom type apChassisMgrExtSubModuleBufferPool based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ApChassisMgrExtSubModuleBufferPool_Type.__name__ = "Integer32"
_ApChassisMgrExtSubModuleBufferPool_Object = MibTableColumn
apChassisMgrExtSubModuleBufferPool = _ApChassisMgrExtSubModuleBufferPool_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 34, 18, 1, 1),
    _ApChassisMgrExtSubModuleBufferPool_Type()
)
apChassisMgrExtSubModuleBufferPool.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apChassisMgrExtSubModuleBufferPool.setStatus("current")


class _ApChassisMgrExtSubModuleBufferSlot_Type(Integer32):
    """Custom type apChassisMgrExtSubModuleBufferSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
    )


_ApChassisMgrExtSubModuleBufferSlot_Type.__name__ = "Integer32"
_ApChassisMgrExtSubModuleBufferSlot_Object = MibTableColumn
apChassisMgrExtSubModuleBufferSlot = _ApChassisMgrExtSubModuleBufferSlot_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 34, 18, 1, 2),
    _ApChassisMgrExtSubModuleBufferSlot_Type()
)
apChassisMgrExtSubModuleBufferSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apChassisMgrExtSubModuleBufferSlot.setStatus("current")


class _ApChassisMgrExtSubModuleBufferSubSlot_Type(Integer32):
    """Custom type apChassisMgrExtSubModuleBufferSubSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_ApChassisMgrExtSubModuleBufferSubSlot_Type.__name__ = "Integer32"
_ApChassisMgrExtSubModuleBufferSubSlot_Object = MibTableColumn
apChassisMgrExtSubModuleBufferSubSlot = _ApChassisMgrExtSubModuleBufferSubSlot_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 34, 18, 1, 3),
    _ApChassisMgrExtSubModuleBufferSubSlot_Type()
)
apChassisMgrExtSubModuleBufferSubSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apChassisMgrExtSubModuleBufferSubSlot.setStatus("current")
_ApChassisMgrExtSubModuleBufferSize_Type = Integer32
_ApChassisMgrExtSubModuleBufferSize_Object = MibTableColumn
apChassisMgrExtSubModuleBufferSize = _ApChassisMgrExtSubModuleBufferSize_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 34, 18, 1, 4),
    _ApChassisMgrExtSubModuleBufferSize_Type()
)
apChassisMgrExtSubModuleBufferSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apChassisMgrExtSubModuleBufferSize.setStatus("current")
_ApChassisMgrExtSubModuleBufferCount_Type = Integer32
_ApChassisMgrExtSubModuleBufferCount_Object = MibTableColumn
apChassisMgrExtSubModuleBufferCount = _ApChassisMgrExtSubModuleBufferCount_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 34, 18, 1, 5),
    _ApChassisMgrExtSubModuleBufferCount_Type()
)
apChassisMgrExtSubModuleBufferCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apChassisMgrExtSubModuleBufferCount.setStatus("current")
_ApChassisMgrExtSubModuleBufferAvailable_Type = Integer32
_ApChassisMgrExtSubModuleBufferAvailable_Object = MibTableColumn
apChassisMgrExtSubModuleBufferAvailable = _ApChassisMgrExtSubModuleBufferAvailable_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 34, 18, 1, 6),
    _ApChassisMgrExtSubModuleBufferAvailable_Type()
)
apChassisMgrExtSubModuleBufferAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apChassisMgrExtSubModuleBufferAvailable.setStatus("current")
_ApChassisMgrExtSubModuleBufferFailures_Type = Integer32
_ApChassisMgrExtSubModuleBufferFailures_Object = MibTableColumn
apChassisMgrExtSubModuleBufferFailures = _ApChassisMgrExtSubModuleBufferFailures_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 34, 18, 1, 7),
    _ApChassisMgrExtSubModuleBufferFailures_Type()
)
apChassisMgrExtSubModuleBufferFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apChassisMgrExtSubModuleBufferFailures.setStatus("current")
_ApChassisMgrExtSubModuleBufferLowBufferCount_Type = Integer32
_ApChassisMgrExtSubModuleBufferLowBufferCount_Object = MibTableColumn
apChassisMgrExtSubModuleBufferLowBufferCount = _ApChassisMgrExtSubModuleBufferLowBufferCount_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 34, 18, 1, 8),
    _ApChassisMgrExtSubModuleBufferLowBufferCount_Type()
)
apChassisMgrExtSubModuleBufferLowBufferCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apChassisMgrExtSubModuleBufferLowBufferCount.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CHASSISMGREXT-MIB",
    **{"chassisMgrExtMib": chassisMgrExtMib,
       "apChassisMgrExtChassisType": apChassisMgrExtChassisType,
       "apChassisMgrExtChassisName": apChassisMgrExtChassisName,
       "apChassisMgrExtChassisSerialNumber": apChassisMgrExtChassisSerialNumber,
       "apChassisMgrExtNumberSlots": apChassisMgrExtNumberSlots,
       "apChassisMgrExtNumberModules": apChassisMgrExtNumberModules,
       "apChassisMgrExtNumberPowerSupplies": apChassisMgrExtNumberPowerSupplies,
       "apChassisMgrExtNumberFans": apChassisMgrExtNumberFans,
       "apChassisMgrExtSoftwareVersionNumber": apChassisMgrExtSoftwareVersionNumber,
       "apChassisMgrExtBootpState": apChassisMgrExtBootpState,
       "apChassisMgrExtMgmtPortIpAddress": apChassisMgrExtMgmtPortIpAddress,
       "apChassisMgrExtBaseEthernetAddress": apChassisMgrExtBaseEthernetAddress,
       "apChassisMgrExtCpuUtilization": apChassisMgrExtCpuUtilization,
       "apChassisMgrExtMajorHwVersion": apChassisMgrExtMajorHwVersion,
       "apChassisMgrExtMinorHwVersion": apChassisMgrExtMinorHwVersion,
       "apChassisMgrExtModuleTable": apChassisMgrExtModuleTable,
       "apChassisMgrExtModuleEntry": apChassisMgrExtModuleEntry,
       "apChassisMgrExtModuleSlotNumber": apChassisMgrExtModuleSlotNumber,
       "apChassisMgrExtModuleType": apChassisMgrExtModuleType,
       "apChassisMgrExtModuleName": apChassisMgrExtModuleName,
       "apChassisMgrExtModuleSerialNumber": apChassisMgrExtModuleSerialNumber,
       "apChassisMgrExtModuleOpStatus": apChassisMgrExtModuleOpStatus,
       "apChassisMgrExtModuleNumSubModules": apChassisMgrExtModuleNumSubModules,
       "apChassisMgrExtModuleMajorHwVersion": apChassisMgrExtModuleMajorHwVersion,
       "apChassisMgrExtModuleMinorHwVersion": apChassisMgrExtModuleMinorHwVersion,
       "apChassisMgrExtSubModuleTable": apChassisMgrExtSubModuleTable,
       "apChassisMgrExtSubModuleEntry": apChassisMgrExtSubModuleEntry,
       "apChassisMgrExtSubModuleSlot": apChassisMgrExtSubModuleSlot,
       "apChassisMgrExtSubModuleSubSlot": apChassisMgrExtSubModuleSubSlot,
       "apChassisMgrExtSubModuleType": apChassisMgrExtSubModuleType,
       "apChassisMgrExtSubModuleName": apChassisMgrExtSubModuleName,
       "apChassisMgrExtSubModuleOpStatus": apChassisMgrExtSubModuleOpStatus,
       "apChassisMgrExtSubModuleSsCardType": apChassisMgrExtSubModuleSsCardType,
       "apChassisMgrExtSubModuleSsCardOpStatus": apChassisMgrExtSubModuleSsCardOpStatus,
       "apChassisMgrExtSubModulePortName": apChassisMgrExtSubModulePortName,
       "apChassisMgrExtSubModulePortNumber": apChassisMgrExtSubModulePortNumber,
       "apChassisMgrExtSubModuleSystemHeapFree": apChassisMgrExtSubModuleSystemHeapFree,
       "apChassisMgrExtSubModuleSystemHeapChainDepth": apChassisMgrExtSubModuleSystemHeapChainDepth,
       "apChassisMgrExtSubModuleInstalledMemory": apChassisMgrExtSubModuleInstalledMemory,
       "apChassisMgrExtSubModuleCPUInstantaneous": apChassisMgrExtSubModuleCPUInstantaneous,
       "apChassisMgrExtSubModuleCPUAverage": apChassisMgrExtSubModuleCPUAverage,
       "apChassisMgrExtSubModuleBufferTable": apChassisMgrExtSubModuleBufferTable,
       "apChassisMgrExtSubModuleBufferEntry": apChassisMgrExtSubModuleBufferEntry,
       "apChassisMgrExtSubModuleBufferPool": apChassisMgrExtSubModuleBufferPool,
       "apChassisMgrExtSubModuleBufferSlot": apChassisMgrExtSubModuleBufferSlot,
       "apChassisMgrExtSubModuleBufferSubSlot": apChassisMgrExtSubModuleBufferSubSlot,
       "apChassisMgrExtSubModuleBufferSize": apChassisMgrExtSubModuleBufferSize,
       "apChassisMgrExtSubModuleBufferCount": apChassisMgrExtSubModuleBufferCount,
       "apChassisMgrExtSubModuleBufferAvailable": apChassisMgrExtSubModuleBufferAvailable,
       "apChassisMgrExtSubModuleBufferFailures": apChassisMgrExtSubModuleBufferFailures,
       "apChassisMgrExtSubModuleBufferLowBufferCount": apChassisMgrExtSubModuleBufferLowBufferCount}
)
