# SNMP MIB module (HM2-POE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HM2-POE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:56:28 2024
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

(hm2IfacePhysIndex,) = mibBuilder.importSymbols(
    "HM2-DEVMGMT-MIB",
    "hm2IfacePhysIndex")

(HmEnabledStatus,
 HmTimeHHMM24,
 hm2ConfigurationMibs) = mibBuilder.importSymbols(
    "HM2-TC-MIB",
    "HmEnabledStatus",
    "HmTimeHHMM24",
    "hm2ConfigurationMibs")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

hm2PoeMgmtMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 12)
)
hm2PoeMgmtMib.setRevisions(
        ("2011-10-31 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hm2PoeMgmtMibNotifications_ObjectIdentity = ObjectIdentity
hm2PoeMgmtMibNotifications = _Hm2PoeMgmtMibNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 12, 0)
)
_Hm2PoeMgmtMibObjects_ObjectIdentity = ObjectIdentity
hm2PoeMgmtMibObjects = _Hm2PoeMgmtMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 12, 1)
)
_Hm2PoeMgmtGroup_ObjectIdentity = ObjectIdentity
hm2PoeMgmtGroup = _Hm2PoeMgmtGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 12, 1, 1)
)
_Hm2PoeMgmtGlobalGroup_ObjectIdentity = ObjectIdentity
hm2PoeMgmtGlobalGroup = _Hm2PoeMgmtGlobalGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 12, 1, 1, 1)
)


class _Hm2PoeMgmtAdminStatus_Type(HmEnabledStatus):
    """Custom type hm2PoeMgmtAdminStatus based on HmEnabledStatus"""


_Hm2PoeMgmtAdminStatus_Object = MibScalar
hm2PoeMgmtAdminStatus = _Hm2PoeMgmtAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 12, 1, 1, 1, 1),
    _Hm2PoeMgmtAdminStatus_Type()
)
hm2PoeMgmtAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2PoeMgmtAdminStatus.setStatus("current")
_Hm2PoeMgmtReservedPower_Type = Integer32
_Hm2PoeMgmtReservedPower_Object = MibScalar
hm2PoeMgmtReservedPower = _Hm2PoeMgmtReservedPower_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 12, 1, 1, 1, 2),
    _Hm2PoeMgmtReservedPower_Type()
)
hm2PoeMgmtReservedPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2PoeMgmtReservedPower.setStatus("current")
_Hm2PoeMgmtPsuTable_Object = MibTable
hm2PoeMgmtPsuTable = _Hm2PoeMgmtPsuTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 12, 1, 1, 2)
)
if mibBuilder.loadTexts:
    hm2PoeMgmtPsuTable.setStatus("current")
_Hm2PoeMgmtPsuEntry_Object = MibTableRow
hm2PoeMgmtPsuEntry = _Hm2PoeMgmtPsuEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 12, 1, 1, 2, 1)
)
hm2PoeMgmtPsuEntry.setIndexNames(
    (0, "HM2-POE-MIB", "hm2PoeMgmtModulePowerSource"),
)
if mibBuilder.loadTexts:
    hm2PoeMgmtPsuEntry.setStatus("current")
_Hm2PoeMgmtPsuPower_Type = Integer32
_Hm2PoeMgmtPsuPower_Object = MibTableColumn
hm2PoeMgmtPsuPower = _Hm2PoeMgmtPsuPower_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 12, 1, 1, 2, 1, 1),
    _Hm2PoeMgmtPsuPower_Type()
)
hm2PoeMgmtPsuPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2PoeMgmtPsuPower.setStatus("current")
_Hm2PoeMgmtPsuReservedPower_Type = Integer32
_Hm2PoeMgmtPsuReservedPower_Object = MibTableColumn
hm2PoeMgmtPsuReservedPower = _Hm2PoeMgmtPsuReservedPower_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 12, 1, 1, 2, 1, 2),
    _Hm2PoeMgmtPsuReservedPower_Type()
)
hm2PoeMgmtPsuReservedPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2PoeMgmtPsuReservedPower.setStatus("current")
_Hm2PoeMgmtPsuDeliveredPower_Type = Integer32
_Hm2PoeMgmtPsuDeliveredPower_Object = MibTableColumn
hm2PoeMgmtPsuDeliveredPower = _Hm2PoeMgmtPsuDeliveredPower_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 12, 1, 1, 2, 1, 3),
    _Hm2PoeMgmtPsuDeliveredPower_Type()
)
hm2PoeMgmtPsuDeliveredPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2PoeMgmtPsuDeliveredPower.setStatus("current")
_Hm2PoeMgmtPortTable_Object = MibTable
hm2PoeMgmtPortTable = _Hm2PoeMgmtPortTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 12, 1, 1, 3)
)
if mibBuilder.loadTexts:
    hm2PoeMgmtPortTable.setStatus("current")
_Hm2PoeMgmtPortEntry_Object = MibTableRow
hm2PoeMgmtPortEntry = _Hm2PoeMgmtPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 12, 1, 1, 3, 1)
)
hm2PoeMgmtPortEntry.setIndexNames(
    (0, "HM2-DEVMGMT-MIB", "hm2IfacePhysIndex"),
)
if mibBuilder.loadTexts:
    hm2PoeMgmtPortEntry.setStatus("current")


class _Hm2PoeMgmtPortAdminEnable_Type(HmEnabledStatus):
    """Custom type hm2PoeMgmtPortAdminEnable based on HmEnabledStatus"""


_Hm2PoeMgmtPortAdminEnable_Object = MibTableColumn
hm2PoeMgmtPortAdminEnable = _Hm2PoeMgmtPortAdminEnable_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 12, 1, 1, 3, 1, 1),
    _Hm2PoeMgmtPortAdminEnable_Type()
)
hm2PoeMgmtPortAdminEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2PoeMgmtPortAdminEnable.setStatus("current")
_Hm2PoeMgmtPortConsumptionPower_Type = Integer32
_Hm2PoeMgmtPortConsumptionPower_Object = MibTableColumn
hm2PoeMgmtPortConsumptionPower = _Hm2PoeMgmtPortConsumptionPower_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 12, 1, 1, 3, 1, 2),
    _Hm2PoeMgmtPortConsumptionPower_Type()
)
hm2PoeMgmtPortConsumptionPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2PoeMgmtPortConsumptionPower.setStatus("current")


class _Hm2PoeMgmtPortDetectionStatus_Type(Integer32):
    """Custom type hm2PoeMgmtPortDetectionStatus based on Integer32"""
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
        *(("deliveringPower", 3),
          ("disabled", 1),
          ("fault", 4),
          ("otherFault", 6),
          ("searching", 2),
          ("test", 5))
    )


_Hm2PoeMgmtPortDetectionStatus_Type.__name__ = "Integer32"
_Hm2PoeMgmtPortDetectionStatus_Object = MibTableColumn
hm2PoeMgmtPortDetectionStatus = _Hm2PoeMgmtPortDetectionStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 12, 1, 1, 3, 1, 3),
    _Hm2PoeMgmtPortDetectionStatus_Type()
)
hm2PoeMgmtPortDetectionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2PoeMgmtPortDetectionStatus.setStatus("current")


class _Hm2PoeMgmtPortPowerPriority_Type(Integer32):
    """Custom type hm2PoeMgmtPortPowerPriority based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("critical", 1),
          ("high", 2),
          ("low", 3))
    )


_Hm2PoeMgmtPortPowerPriority_Type.__name__ = "Integer32"
_Hm2PoeMgmtPortPowerPriority_Object = MibTableColumn
hm2PoeMgmtPortPowerPriority = _Hm2PoeMgmtPortPowerPriority_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 12, 1, 1, 3, 1, 4),
    _Hm2PoeMgmtPortPowerPriority_Type()
)
hm2PoeMgmtPortPowerPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2PoeMgmtPortPowerPriority.setStatus("current")


class _Hm2PoeMgmtPortPowerClassification_Type(Integer32):
    """Custom type hm2PoeMgmtPortPowerClassification based on Integer32"""
    defaultValue = 1

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
        *(("class0", 1),
          ("class1", 2),
          ("class2", 3),
          ("class3", 4),
          ("class4", 5))
    )


_Hm2PoeMgmtPortPowerClassification_Type.__name__ = "Integer32"
_Hm2PoeMgmtPortPowerClassification_Object = MibTableColumn
hm2PoeMgmtPortPowerClassification = _Hm2PoeMgmtPortPowerClassification_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 12, 1, 1, 3, 1, 5),
    _Hm2PoeMgmtPortPowerClassification_Type()
)
hm2PoeMgmtPortPowerClassification.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2PoeMgmtPortPowerClassification.setStatus("current")


class _Hm2PoeMgmtPortName_Type(SnmpAdminString):
    """Custom type hm2PoeMgmtPortName based on SnmpAdminString"""
    defaultValue = OctetString(" ")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Hm2PoeMgmtPortName_Type.__name__ = "SnmpAdminString"
_Hm2PoeMgmtPortName_Object = MibTableColumn
hm2PoeMgmtPortName = _Hm2PoeMgmtPortName_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 12, 1, 1, 3, 1, 6),
    _Hm2PoeMgmtPortName_Type()
)
hm2PoeMgmtPortName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2PoeMgmtPortName.setStatus("current")


class _Hm2PoeMgmtPortAllowedClassBits_Type(Bits):
    """Custom type hm2PoeMgmtPortAllowedClassBits based on Bits"""
    defaultBinValue = "11111"

    namedValues = NamedValues(
        *(("class0", 0),
          ("class1", 1),
          ("class2", 2),
          ("class3", 3),
          ("class4", 4))
    )

_Hm2PoeMgmtPortAllowedClassBits_Type.__name__ = "Bits"
_Hm2PoeMgmtPortAllowedClassBits_Object = MibTableColumn
hm2PoeMgmtPortAllowedClassBits = _Hm2PoeMgmtPortAllowedClassBits_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 12, 1, 1, 3, 1, 7),
    _Hm2PoeMgmtPortAllowedClassBits_Type()
)
hm2PoeMgmtPortAllowedClassBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2PoeMgmtPortAllowedClassBits.setStatus("current")


class _Hm2PoeMgmtPortAutoShutdown_Type(HmEnabledStatus):
    """Custom type hm2PoeMgmtPortAutoShutdown based on HmEnabledStatus"""


_Hm2PoeMgmtPortAutoShutdown_Object = MibTableColumn
hm2PoeMgmtPortAutoShutdown = _Hm2PoeMgmtPortAutoShutdown_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 12, 1, 1, 3, 1, 8),
    _Hm2PoeMgmtPortAutoShutdown_Type()
)
hm2PoeMgmtPortAutoShutdown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2PoeMgmtPortAutoShutdown.setStatus("current")


class _Hm2PoeMgmtPortAutoShutdownTimeStart_Type(HmTimeHHMM24):
    """Custom type hm2PoeMgmtPortAutoShutdownTimeStart based on HmTimeHHMM24"""
    defaultValue = OctetString("00:00")


_Hm2PoeMgmtPortAutoShutdownTimeStart_Object = MibTableColumn
hm2PoeMgmtPortAutoShutdownTimeStart = _Hm2PoeMgmtPortAutoShutdownTimeStart_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 12, 1, 1, 3, 1, 9),
    _Hm2PoeMgmtPortAutoShutdownTimeStart_Type()
)
hm2PoeMgmtPortAutoShutdownTimeStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2PoeMgmtPortAutoShutdownTimeStart.setStatus("current")


class _Hm2PoeMgmtPortAutoShutdownTimeEnd_Type(HmTimeHHMM24):
    """Custom type hm2PoeMgmtPortAutoShutdownTimeEnd based on HmTimeHHMM24"""
    defaultValue = OctetString("00:00")


_Hm2PoeMgmtPortAutoShutdownTimeEnd_Object = MibTableColumn
hm2PoeMgmtPortAutoShutdownTimeEnd = _Hm2PoeMgmtPortAutoShutdownTimeEnd_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 12, 1, 1, 3, 1, 10),
    _Hm2PoeMgmtPortAutoShutdownTimeEnd_Type()
)
hm2PoeMgmtPortAutoShutdownTimeEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2PoeMgmtPortAutoShutdownTimeEnd.setStatus("current")


class _Hm2PoeMgmtPortClassValid_Type(Integer32):
    """Custom type hm2PoeMgmtPortClassValid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("valid", 1))
    )


_Hm2PoeMgmtPortClassValid_Type.__name__ = "Integer32"
_Hm2PoeMgmtPortClassValid_Object = MibTableColumn
hm2PoeMgmtPortClassValid = _Hm2PoeMgmtPortClassValid_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 12, 1, 1, 3, 1, 11),
    _Hm2PoeMgmtPortClassValid_Type()
)
hm2PoeMgmtPortClassValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2PoeMgmtPortClassValid.setStatus("current")


class _Hm2PoeMgmtPortFastStartup_Type(HmEnabledStatus):
    """Custom type hm2PoeMgmtPortFastStartup based on HmEnabledStatus"""


_Hm2PoeMgmtPortFastStartup_Object = MibTableColumn
hm2PoeMgmtPortFastStartup = _Hm2PoeMgmtPortFastStartup_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 12, 1, 1, 3, 1, 12),
    _Hm2PoeMgmtPortFastStartup_Type()
)
hm2PoeMgmtPortFastStartup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2PoeMgmtPortFastStartup.setStatus("current")
_Hm2PoeMgmtPortMaxConsumptionPower_Type = Integer32
_Hm2PoeMgmtPortMaxConsumptionPower_Object = MibTableColumn
hm2PoeMgmtPortMaxConsumptionPower = _Hm2PoeMgmtPortMaxConsumptionPower_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 12, 1, 1, 3, 1, 13),
    _Hm2PoeMgmtPortMaxConsumptionPower_Type()
)
hm2PoeMgmtPortMaxConsumptionPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2PoeMgmtPortMaxConsumptionPower.setStatus("current")


class _Hm2PoeMgmtPortPowerLimit_Type(Integer32):
    """Custom type hm2PoeMgmtPortPowerLimit based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30000),
    )


_Hm2PoeMgmtPortPowerLimit_Type.__name__ = "Integer32"
_Hm2PoeMgmtPortPowerLimit_Object = MibTableColumn
hm2PoeMgmtPortPowerLimit = _Hm2PoeMgmtPortPowerLimit_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 12, 1, 1, 3, 1, 14),
    _Hm2PoeMgmtPortPowerLimit_Type()
)
hm2PoeMgmtPortPowerLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2PoeMgmtPortPowerLimit.setStatus("current")
_Hm2PoeMgmtModuleTable_Object = MibTable
hm2PoeMgmtModuleTable = _Hm2PoeMgmtModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 12, 1, 1, 4)
)
if mibBuilder.loadTexts:
    hm2PoeMgmtModuleTable.setStatus("current")
_Hm2PoeMgmtModuleEntry_Object = MibTableRow
hm2PoeMgmtModuleEntry = _Hm2PoeMgmtModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 12, 1, 1, 4, 1)
)
hm2PoeMgmtModuleEntry.setIndexNames(
    (0, "HM2-POE-MIB", "hm2PoeMgmtModuleUnitIndex"),
    (0, "HM2-POE-MIB", "hm2PoeMgmtModuleSlotIndex"),
)
if mibBuilder.loadTexts:
    hm2PoeMgmtModuleEntry.setStatus("current")
_Hm2PoeMgmtModuleUnitIndex_Type = Integer32
_Hm2PoeMgmtModuleUnitIndex_Object = MibTableColumn
hm2PoeMgmtModuleUnitIndex = _Hm2PoeMgmtModuleUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 12, 1, 1, 4, 1, 1),
    _Hm2PoeMgmtModuleUnitIndex_Type()
)
hm2PoeMgmtModuleUnitIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hm2PoeMgmtModuleUnitIndex.setStatus("current")
_Hm2PoeMgmtModuleSlotIndex_Type = Integer32
_Hm2PoeMgmtModuleSlotIndex_Object = MibTableColumn
hm2PoeMgmtModuleSlotIndex = _Hm2PoeMgmtModuleSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 12, 1, 1, 4, 1, 2),
    _Hm2PoeMgmtModuleSlotIndex_Type()
)
hm2PoeMgmtModuleSlotIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hm2PoeMgmtModuleSlotIndex.setStatus("current")


class _Hm2PoeMgmtModulePower_Type(Integer32):
    """Custom type hm2PoeMgmtModulePower based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Hm2PoeMgmtModulePower_Type.__name__ = "Integer32"
_Hm2PoeMgmtModulePower_Object = MibTableColumn
hm2PoeMgmtModulePower = _Hm2PoeMgmtModulePower_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 12, 1, 1, 4, 1, 3),
    _Hm2PoeMgmtModulePower_Type()
)
hm2PoeMgmtModulePower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2PoeMgmtModulePower.setStatus("current")


class _Hm2PoeMgmtModuleMaximumPower_Type(Integer32):
    """Custom type hm2PoeMgmtModuleMaximumPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Hm2PoeMgmtModuleMaximumPower_Type.__name__ = "Integer32"
_Hm2PoeMgmtModuleMaximumPower_Object = MibTableColumn
hm2PoeMgmtModuleMaximumPower = _Hm2PoeMgmtModuleMaximumPower_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 12, 1, 1, 4, 1, 4),
    _Hm2PoeMgmtModuleMaximumPower_Type()
)
hm2PoeMgmtModuleMaximumPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2PoeMgmtModuleMaximumPower.setStatus("current")
_Hm2PoeMgmtModuleReservedPower_Type = Integer32
_Hm2PoeMgmtModuleReservedPower_Object = MibTableColumn
hm2PoeMgmtModuleReservedPower = _Hm2PoeMgmtModuleReservedPower_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 12, 1, 1, 4, 1, 5),
    _Hm2PoeMgmtModuleReservedPower_Type()
)
hm2PoeMgmtModuleReservedPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2PoeMgmtModuleReservedPower.setStatus("current")
_Hm2PoeMgmtModuleDeliveredPower_Type = Integer32
_Hm2PoeMgmtModuleDeliveredPower_Object = MibTableColumn
hm2PoeMgmtModuleDeliveredPower = _Hm2PoeMgmtModuleDeliveredPower_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 12, 1, 1, 4, 1, 6),
    _Hm2PoeMgmtModuleDeliveredPower_Type()
)
hm2PoeMgmtModuleDeliveredPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2PoeMgmtModuleDeliveredPower.setStatus("current")


class _Hm2PoeMgmtModulePowerSource_Type(Integer32):
    """Custom type hm2PoeMgmtModulePowerSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("external", 1),
          ("internal", 0))
    )


_Hm2PoeMgmtModulePowerSource_Type.__name__ = "Integer32"
_Hm2PoeMgmtModulePowerSource_Object = MibTableColumn
hm2PoeMgmtModulePowerSource = _Hm2PoeMgmtModulePowerSource_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 12, 1, 1, 4, 1, 7),
    _Hm2PoeMgmtModulePowerSource_Type()
)
hm2PoeMgmtModulePowerSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2PoeMgmtModulePowerSource.setStatus("current")


class _Hm2PoeMgmtModuleUsageThreshold_Type(Integer32):
    """Custom type hm2PoeMgmtModuleUsageThreshold based on Integer32"""
    defaultValue = 90

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_Hm2PoeMgmtModuleUsageThreshold_Type.__name__ = "Integer32"
_Hm2PoeMgmtModuleUsageThreshold_Object = MibTableColumn
hm2PoeMgmtModuleUsageThreshold = _Hm2PoeMgmtModuleUsageThreshold_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 12, 1, 1, 4, 1, 8),
    _Hm2PoeMgmtModuleUsageThreshold_Type()
)
hm2PoeMgmtModuleUsageThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2PoeMgmtModuleUsageThreshold.setStatus("current")


class _Hm2PoeMgmtModuleNotificationControlEnable_Type(HmEnabledStatus):
    """Custom type hm2PoeMgmtModuleNotificationControlEnable based on HmEnabledStatus"""


_Hm2PoeMgmtModuleNotificationControlEnable_Object = MibTableColumn
hm2PoeMgmtModuleNotificationControlEnable = _Hm2PoeMgmtModuleNotificationControlEnable_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 12, 1, 1, 4, 1, 9),
    _Hm2PoeMgmtModuleNotificationControlEnable_Type()
)
hm2PoeMgmtModuleNotificationControlEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2PoeMgmtModuleNotificationControlEnable.setStatus("current")

# Managed Objects groups


# Notification objects

hm2PoeMgmtModulePowerUsageOnNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 11, 12, 0, 1)
)
hm2PoeMgmtModulePowerUsageOnNotification.setObjects(
    ("HM2-POE-MIB", "hm2PoeMgmtModuleDeliveredPower")
)
if mibBuilder.loadTexts:
    hm2PoeMgmtModulePowerUsageOnNotification.setStatus(
        "current"
    )

hm2PoeMgmtModulePowerUsageOffNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 11, 12, 0, 2)
)
hm2PoeMgmtModulePowerUsageOffNotification.setObjects(
    ("HM2-POE-MIB", "hm2PoeMgmtModuleDeliveredPower")
)
if mibBuilder.loadTexts:
    hm2PoeMgmtModulePowerUsageOffNotification.setStatus(
        "current"
    )

hm2PoeMgmtPortMaxConfiguredPowerLimitExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 11, 12, 0, 3)
)
hm2PoeMgmtPortMaxConfiguredPowerLimitExceeded.setObjects(
      *(("HM2-DEVMGMT-MIB", "hm2IfacePhysIndex"),
        ("HM2-POE-MIB", "hm2PoeMgmtPortMaxConsumptionPower"),
        ("HM2-POE-MIB", "hm2PoeMgmtPortPowerLimit"))
)
if mibBuilder.loadTexts:
    hm2PoeMgmtPortMaxConfiguredPowerLimitExceeded.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HM2-POE-MIB",
    **{"hm2PoeMgmtMib": hm2PoeMgmtMib,
       "hm2PoeMgmtMibNotifications": hm2PoeMgmtMibNotifications,
       "hm2PoeMgmtModulePowerUsageOnNotification": hm2PoeMgmtModulePowerUsageOnNotification,
       "hm2PoeMgmtModulePowerUsageOffNotification": hm2PoeMgmtModulePowerUsageOffNotification,
       "hm2PoeMgmtPortMaxConfiguredPowerLimitExceeded": hm2PoeMgmtPortMaxConfiguredPowerLimitExceeded,
       "hm2PoeMgmtMibObjects": hm2PoeMgmtMibObjects,
       "hm2PoeMgmtGroup": hm2PoeMgmtGroup,
       "hm2PoeMgmtGlobalGroup": hm2PoeMgmtGlobalGroup,
       "hm2PoeMgmtAdminStatus": hm2PoeMgmtAdminStatus,
       "hm2PoeMgmtReservedPower": hm2PoeMgmtReservedPower,
       "hm2PoeMgmtPsuTable": hm2PoeMgmtPsuTable,
       "hm2PoeMgmtPsuEntry": hm2PoeMgmtPsuEntry,
       "hm2PoeMgmtPsuPower": hm2PoeMgmtPsuPower,
       "hm2PoeMgmtPsuReservedPower": hm2PoeMgmtPsuReservedPower,
       "hm2PoeMgmtPsuDeliveredPower": hm2PoeMgmtPsuDeliveredPower,
       "hm2PoeMgmtPortTable": hm2PoeMgmtPortTable,
       "hm2PoeMgmtPortEntry": hm2PoeMgmtPortEntry,
       "hm2PoeMgmtPortAdminEnable": hm2PoeMgmtPortAdminEnable,
       "hm2PoeMgmtPortConsumptionPower": hm2PoeMgmtPortConsumptionPower,
       "hm2PoeMgmtPortDetectionStatus": hm2PoeMgmtPortDetectionStatus,
       "hm2PoeMgmtPortPowerPriority": hm2PoeMgmtPortPowerPriority,
       "hm2PoeMgmtPortPowerClassification": hm2PoeMgmtPortPowerClassification,
       "hm2PoeMgmtPortName": hm2PoeMgmtPortName,
       "hm2PoeMgmtPortAllowedClassBits": hm2PoeMgmtPortAllowedClassBits,
       "hm2PoeMgmtPortAutoShutdown": hm2PoeMgmtPortAutoShutdown,
       "hm2PoeMgmtPortAutoShutdownTimeStart": hm2PoeMgmtPortAutoShutdownTimeStart,
       "hm2PoeMgmtPortAutoShutdownTimeEnd": hm2PoeMgmtPortAutoShutdownTimeEnd,
       "hm2PoeMgmtPortClassValid": hm2PoeMgmtPortClassValid,
       "hm2PoeMgmtPortFastStartup": hm2PoeMgmtPortFastStartup,
       "hm2PoeMgmtPortMaxConsumptionPower": hm2PoeMgmtPortMaxConsumptionPower,
       "hm2PoeMgmtPortPowerLimit": hm2PoeMgmtPortPowerLimit,
       "hm2PoeMgmtModuleTable": hm2PoeMgmtModuleTable,
       "hm2PoeMgmtModuleEntry": hm2PoeMgmtModuleEntry,
       "hm2PoeMgmtModuleUnitIndex": hm2PoeMgmtModuleUnitIndex,
       "hm2PoeMgmtModuleSlotIndex": hm2PoeMgmtModuleSlotIndex,
       "hm2PoeMgmtModulePower": hm2PoeMgmtModulePower,
       "hm2PoeMgmtModuleMaximumPower": hm2PoeMgmtModuleMaximumPower,
       "hm2PoeMgmtModuleReservedPower": hm2PoeMgmtModuleReservedPower,
       "hm2PoeMgmtModuleDeliveredPower": hm2PoeMgmtModuleDeliveredPower,
       "hm2PoeMgmtModulePowerSource": hm2PoeMgmtModulePowerSource,
       "hm2PoeMgmtModuleUsageThreshold": hm2PoeMgmtModuleUsageThreshold,
       "hm2PoeMgmtModuleNotificationControlEnable": hm2PoeMgmtModuleNotificationControlEnable}
)
