# SNMP MIB module (EQLCONTROLLER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/EQLCONTROLLER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:40:01 2024
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

(eqlGroupId,) = mibBuilder.importSymbols(
    "EQLGROUP-MIB",
    "eqlGroupId")

(eqlMemberIndex,) = mibBuilder.importSymbols(
    "EQLMEMBER-MIB",
    "eqlMemberIndex")

(equalLogic,) = mibBuilder.importSymbols(
    "EQUALLOGIC-SMI",
    "equalLogic")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

eqlcontrollerModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 12740, 4)
)
eqlcontrollerModule.setRevisions(
        ("2002-09-06 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EqlcontrollerObjects_ObjectIdentity = ObjectIdentity
eqlcontrollerObjects = _EqlcontrollerObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12740, 4, 1)
)
_EqlControllerTable_Object = MibTable
eqlControllerTable = _EqlControllerTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 4, 1, 1)
)
if mibBuilder.loadTexts:
    eqlControllerTable.setStatus("current")
_EqlControllerEntry_Object = MibTableRow
eqlControllerEntry = _EqlControllerEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 4, 1, 1, 1)
)
eqlControllerEntry.setIndexNames(
    (0, "EQLGROUP-MIB", "eqlGroupId"),
    (0, "EQLMEMBER-MIB", "eqlMemberIndex"),
    (0, "EQLCONTROLLER-MIB", "eqlControllerIndex"),
)
if mibBuilder.loadTexts:
    eqlControllerEntry.setStatus("current")


class _EqlControllerIndex_Type(Integer32):
    """Custom type eqlControllerIndex based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_EqlControllerIndex_Type.__name__ = "Integer32"
_EqlControllerIndex_Object = MibTableColumn
eqlControllerIndex = _EqlControllerIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 4, 1, 1, 1, 1),
    _EqlControllerIndex_Type()
)
eqlControllerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqlControllerIndex.setStatus("current")


class _EqlControllerModel_Type(DisplayString):
    """Custom type eqlControllerModel based on DisplayString"""
    defaultValue = OctetString("unknown model")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_EqlControllerModel_Type.__name__ = "DisplayString"
_EqlControllerModel_Object = MibTableColumn
eqlControllerModel = _EqlControllerModel_Object(
    (1, 3, 6, 1, 4, 1, 12740, 4, 1, 1, 1, 2),
    _EqlControllerModel_Type()
)
eqlControllerModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlControllerModel.setStatus("current")


class _EqlControllerCMRevision_Type(DisplayString):
    """Custom type eqlControllerCMRevision based on DisplayString"""
    defaultValue = OctetString("unknown rev")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 9),
    )


_EqlControllerCMRevision_Type.__name__ = "DisplayString"
_EqlControllerCMRevision_Object = MibTableColumn
eqlControllerCMRevision = _EqlControllerCMRevision_Object(
    (1, 3, 6, 1, 4, 1, 12740, 4, 1, 1, 1, 3),
    _EqlControllerCMRevision_Type()
)
eqlControllerCMRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlControllerCMRevision.setStatus("current")


class _EqlControllerSwRevision_Type(DisplayString):
    """Custom type eqlControllerSwRevision based on DisplayString"""
    defaultValue = OctetString("unknown sw rev")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 96),
    )


_EqlControllerSwRevision_Type.__name__ = "DisplayString"
_EqlControllerSwRevision_Object = MibTableColumn
eqlControllerSwRevision = _EqlControllerSwRevision_Object(
    (1, 3, 6, 1, 4, 1, 12740, 4, 1, 1, 1, 4),
    _EqlControllerSwRevision_Type()
)
eqlControllerSwRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlControllerSwRevision.setStatus("current")


class _EqlControllerBatteryStatus_Type(Integer32):
    """Custom type eqlControllerBatteryStatus based on Integer32"""
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
        *(("failed", 2),
          ("good-battery-is-charging", 3),
          ("low-voltage-is-charging", 5),
          ("low-voltage-status", 4),
          ("missing-battery", 6),
          ("ok", 1))
    )


_EqlControllerBatteryStatus_Type.__name__ = "Integer32"
_EqlControllerBatteryStatus_Object = MibTableColumn
eqlControllerBatteryStatus = _EqlControllerBatteryStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 4, 1, 1, 1, 5),
    _EqlControllerBatteryStatus_Type()
)
eqlControllerBatteryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlControllerBatteryStatus.setStatus("current")
_EqlControllerUpTime_Type = Counter32
_EqlControllerUpTime_Object = MibTableColumn
eqlControllerUpTime = _EqlControllerUpTime_Object(
    (1, 3, 6, 1, 4, 1, 12740, 4, 1, 1, 1, 6),
    _EqlControllerUpTime_Type()
)
eqlControllerUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlControllerUpTime.setStatus("current")
if mibBuilder.loadTexts:
    eqlControllerUpTime.setUnits("seconds")
_EqlControllerProcessorTemp_Type = Integer32
_EqlControllerProcessorTemp_Object = MibTableColumn
eqlControllerProcessorTemp = _EqlControllerProcessorTemp_Object(
    (1, 3, 6, 1, 4, 1, 12740, 4, 1, 1, 1, 7),
    _EqlControllerProcessorTemp_Type()
)
eqlControllerProcessorTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlControllerProcessorTemp.setStatus("current")
_EqlControllerChipsetTemp_Type = Integer32
_EqlControllerChipsetTemp_Object = MibTableColumn
eqlControllerChipsetTemp = _EqlControllerChipsetTemp_Object(
    (1, 3, 6, 1, 4, 1, 12740, 4, 1, 1, 1, 8),
    _EqlControllerChipsetTemp_Type()
)
eqlControllerChipsetTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlControllerChipsetTemp.setStatus("current")


class _EqlControllerPrimaryOrSecondary_Type(Integer32):
    """Custom type eqlControllerPrimaryOrSecondary based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("secondary", 2))
    )


_EqlControllerPrimaryOrSecondary_Type.__name__ = "Integer32"
_EqlControllerPrimaryOrSecondary_Object = MibTableColumn
eqlControllerPrimaryOrSecondary = _EqlControllerPrimaryOrSecondary_Object(
    (1, 3, 6, 1, 4, 1, 12740, 4, 1, 1, 1, 9),
    _EqlControllerPrimaryOrSecondary_Type()
)
eqlControllerPrimaryOrSecondary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlControllerPrimaryOrSecondary.setStatus("current")


class _EqlControllerPrimaryFlashImageRev_Type(DisplayString):
    """Custom type eqlControllerPrimaryFlashImageRev based on DisplayString"""
    defaultValue = OctetString("unknown")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_EqlControllerPrimaryFlashImageRev_Type.__name__ = "DisplayString"
_EqlControllerPrimaryFlashImageRev_Object = MibTableColumn
eqlControllerPrimaryFlashImageRev = _EqlControllerPrimaryFlashImageRev_Object(
    (1, 3, 6, 1, 4, 1, 12740, 4, 1, 1, 1, 10),
    _EqlControllerPrimaryFlashImageRev_Type()
)
eqlControllerPrimaryFlashImageRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlControllerPrimaryFlashImageRev.setStatus("current")


class _EqlControllerSecondaryFlashImageRev_Type(DisplayString):
    """Custom type eqlControllerSecondaryFlashImageRev based on DisplayString"""
    defaultValue = OctetString("unknown")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_EqlControllerSecondaryFlashImageRev_Type.__name__ = "DisplayString"
_EqlControllerSecondaryFlashImageRev_Object = MibTableColumn
eqlControllerSecondaryFlashImageRev = _EqlControllerSecondaryFlashImageRev_Object(
    (1, 3, 6, 1, 4, 1, 12740, 4, 1, 1, 1, 11),
    _EqlControllerSecondaryFlashImageRev_Type()
)
eqlControllerSecondaryFlashImageRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlControllerSecondaryFlashImageRev.setStatus("current")


class _EqlControllerSerialNumber_Type(DisplayString):
    """Custom type eqlControllerSerialNumber based on DisplayString"""
    defaultValue = OctetString("unknown")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_EqlControllerSerialNumber_Type.__name__ = "DisplayString"
_EqlControllerSerialNumber_Object = MibTableColumn
eqlControllerSerialNumber = _EqlControllerSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 12740, 4, 1, 1, 1, 12),
    _EqlControllerSerialNumber_Type()
)
eqlControllerSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlControllerSerialNumber.setStatus("current")


class _EqlControllerDate_Type(DisplayString):
    """Custom type eqlControllerDate based on DisplayString"""
    defaultValue = OctetString("unknown")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_EqlControllerDate_Type.__name__ = "DisplayString"
_EqlControllerDate_Object = MibTableColumn
eqlControllerDate = _EqlControllerDate_Object(
    (1, 3, 6, 1, 4, 1, 12740, 4, 1, 1, 1, 13),
    _EqlControllerDate_Type()
)
eqlControllerDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlControllerDate.setStatus("current")


class _EqlControllerECO_Type(DisplayString):
    """Custom type eqlControllerECO based on DisplayString"""
    defaultValue = OctetString("unknown")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_EqlControllerECO_Type.__name__ = "DisplayString"
_EqlControllerECO_Object = MibTableColumn
eqlControllerECO = _EqlControllerECO_Object(
    (1, 3, 6, 1, 4, 1, 12740, 4, 1, 1, 1, 14),
    _EqlControllerECO_Type()
)
eqlControllerECO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlControllerECO.setStatus("current")


class _EqlControllerEEprom_Type(OctetString):
    """Custom type eqlControllerEEprom based on OctetString"""
    defaultValue = OctetString("unknown")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(256, 256),
    )


_EqlControllerEEprom_Type.__name__ = "OctetString"
_EqlControllerEEprom_Object = MibTableColumn
eqlControllerEEprom = _EqlControllerEEprom_Object(
    (1, 3, 6, 1, 4, 1, 12740, 4, 1, 1, 1, 15),
    _EqlControllerEEprom_Type()
)
eqlControllerEEprom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlControllerEEprom.setStatus("current")


class _EqlControllerPLDrev_Type(Unsigned32):
    """Custom type eqlControllerPLDrev based on Unsigned32"""
    defaultValue = 0


_EqlControllerPLDrev_Object = MibTableColumn
eqlControllerPLDrev = _EqlControllerPLDrev_Object(
    (1, 3, 6, 1, 4, 1, 12740, 4, 1, 1, 1, 16),
    _EqlControllerPLDrev_Type()
)
eqlControllerPLDrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlControllerPLDrev.setStatus("current")


class _EqlControllerPlatformType_Type(Unsigned32):
    """Custom type eqlControllerPlatformType based on Unsigned32"""
    defaultValue = 0


_EqlControllerPlatformType_Object = MibTableColumn
eqlControllerPlatformType = _EqlControllerPlatformType_Object(
    (1, 3, 6, 1, 4, 1, 12740, 4, 1, 1, 1, 17),
    _EqlControllerPlatformType_Type()
)
eqlControllerPlatformType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlControllerPlatformType.setStatus("current")


class _EqlControllerPlatformVersion_Type(Unsigned32):
    """Custom type eqlControllerPlatformVersion based on Unsigned32"""
    defaultValue = 0


_EqlControllerPlatformVersion_Object = MibTableColumn
eqlControllerPlatformVersion = _EqlControllerPlatformVersion_Object(
    (1, 3, 6, 1, 4, 1, 12740, 4, 1, 1, 1, 18),
    _EqlControllerPlatformVersion_Type()
)
eqlControllerPlatformVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlControllerPlatformVersion.setStatus("current")


class _EqlControllerCPUPass_Type(Unsigned32):
    """Custom type eqlControllerCPUPass based on Unsigned32"""
    defaultValue = 0


_EqlControllerCPUPass_Object = MibTableColumn
eqlControllerCPUPass = _EqlControllerCPUPass_Object(
    (1, 3, 6, 1, 4, 1, 12740, 4, 1, 1, 1, 19),
    _EqlControllerCPUPass_Type()
)
eqlControllerCPUPass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlControllerCPUPass.setStatus("current")


class _EqlControllerCPUrev_Type(Unsigned32):
    """Custom type eqlControllerCPUrev based on Unsigned32"""
    defaultValue = 0


_EqlControllerCPUrev_Object = MibTableColumn
eqlControllerCPUrev = _EqlControllerCPUrev_Object(
    (1, 3, 6, 1, 4, 1, 12740, 4, 1, 1, 1, 20),
    _EqlControllerCPUrev_Type()
)
eqlControllerCPUrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlControllerCPUrev.setStatus("current")


class _EqlControllerCPUfreq_Type(Unsigned32):
    """Custom type eqlControllerCPUfreq based on Unsigned32"""
    defaultValue = 0


_EqlControllerCPUfreq_Object = MibTableColumn
eqlControllerCPUfreq = _EqlControllerCPUfreq_Object(
    (1, 3, 6, 1, 4, 1, 12740, 4, 1, 1, 1, 21),
    _EqlControllerCPUfreq_Type()
)
eqlControllerCPUfreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlControllerCPUfreq.setStatus("current")


class _EqlControllerPhysRam_Type(Unsigned32):
    """Custom type eqlControllerPhysRam based on Unsigned32"""
    defaultValue = 0


_EqlControllerPhysRam_Object = MibTableColumn
eqlControllerPhysRam = _EqlControllerPhysRam_Object(
    (1, 3, 6, 1, 4, 1, 12740, 4, 1, 1, 1, 22),
    _EqlControllerPhysRam_Type()
)
eqlControllerPhysRam.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlControllerPhysRam.setStatus("current")


class _EqlControllerBootRomVersion_Type(DisplayString):
    """Custom type eqlControllerBootRomVersion based on DisplayString"""
    defaultValue = OctetString("unknown")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_EqlControllerBootRomVersion_Type.__name__ = "DisplayString"
_EqlControllerBootRomVersion_Object = MibTableColumn
eqlControllerBootRomVersion = _EqlControllerBootRomVersion_Object(
    (1, 3, 6, 1, 4, 1, 12740, 4, 1, 1, 1, 23),
    _EqlControllerBootRomVersion_Type()
)
eqlControllerBootRomVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlControllerBootRomVersion.setStatus("current")


class _EqlControllerBootRomBuildDate_Type(DisplayString):
    """Custom type eqlControllerBootRomBuildDate based on DisplayString"""
    defaultValue = OctetString("unknown")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(128, 128),
    )


_EqlControllerBootRomBuildDate_Type.__name__ = "DisplayString"
_EqlControllerBootRomBuildDate_Object = MibTableColumn
eqlControllerBootRomBuildDate = _EqlControllerBootRomBuildDate_Object(
    (1, 3, 6, 1, 4, 1, 12740, 4, 1, 1, 1, 24),
    _EqlControllerBootRomBuildDate_Type()
)
eqlControllerBootRomBuildDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlControllerBootRomBuildDate.setStatus("current")


class _EqlControllerInfoMsg_Type(DisplayString):
    """Custom type eqlControllerInfoMsg based on DisplayString"""
    defaultValue = OctetString("unknown")


_EqlControllerInfoMsg_Object = MibTableColumn
eqlControllerInfoMsg = _EqlControllerInfoMsg_Object(
    (1, 3, 6, 1, 4, 1, 12740, 4, 1, 1, 1, 25),
    _EqlControllerInfoMsg_Type()
)
eqlControllerInfoMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlControllerInfoMsg.setStatus("current")


class _EqlControllerAthenaSataVersion_Type(DisplayString):
    """Custom type eqlControllerAthenaSataVersion based on DisplayString"""
    defaultValue = OctetString("unknown")


_EqlControllerAthenaSataVersion_Object = MibTableColumn
eqlControllerAthenaSataVersion = _EqlControllerAthenaSataVersion_Object(
    (1, 3, 6, 1, 4, 1, 12740, 4, 1, 1, 1, 26),
    _EqlControllerAthenaSataVersion_Type()
)
eqlControllerAthenaSataVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlControllerAthenaSataVersion.setStatus("current")


class _EqlControllerMajorVersion_Type(Unsigned32):
    """Custom type eqlControllerMajorVersion based on Unsigned32"""
    defaultValue = 1


_EqlControllerMajorVersion_Object = MibTableColumn
eqlControllerMajorVersion = _EqlControllerMajorVersion_Object(
    (1, 3, 6, 1, 4, 1, 12740, 4, 1, 1, 1, 27),
    _EqlControllerMajorVersion_Type()
)
eqlControllerMajorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlControllerMajorVersion.setStatus("current")


class _EqlControllerMinorVersion_Type(Unsigned32):
    """Custom type eqlControllerMinorVersion based on Unsigned32"""
    defaultValue = 1


_EqlControllerMinorVersion_Object = MibTableColumn
eqlControllerMinorVersion = _EqlControllerMinorVersion_Object(
    (1, 3, 6, 1, 4, 1, 12740, 4, 1, 1, 1, 28),
    _EqlControllerMinorVersion_Type()
)
eqlControllerMinorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlControllerMinorVersion.setStatus("current")


class _EqlControllerMaintenanceVersion_Type(Unsigned32):
    """Custom type eqlControllerMaintenanceVersion based on Unsigned32"""
    defaultValue = 0


_EqlControllerMaintenanceVersion_Object = MibTableColumn
eqlControllerMaintenanceVersion = _EqlControllerMaintenanceVersion_Object(
    (1, 3, 6, 1, 4, 1, 12740, 4, 1, 1, 1, 29),
    _EqlControllerMaintenanceVersion_Type()
)
eqlControllerMaintenanceVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlControllerMaintenanceVersion.setStatus("current")
_EqlControllerSWCompatibilityLevel_Type = Unsigned32
_EqlControllerSWCompatibilityLevel_Object = MibTableColumn
eqlControllerSWCompatibilityLevel = _EqlControllerSWCompatibilityLevel_Object(
    (1, 3, 6, 1, 4, 1, 12740, 4, 1, 1, 1, 30),
    _EqlControllerSWCompatibilityLevel_Type()
)
eqlControllerSWCompatibilityLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlControllerSWCompatibilityLevel.setStatus("current")


class _EqlControllerFullSwRevision_Type(DisplayString):
    """Custom type eqlControllerFullSwRevision based on DisplayString"""
    defaultValue = OctetString("unknown sw rev")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 96),
    )


_EqlControllerFullSwRevision_Type.__name__ = "DisplayString"
_EqlControllerFullSwRevision_Object = MibTableColumn
eqlControllerFullSwRevision = _EqlControllerFullSwRevision_Object(
    (1, 3, 6, 1, 4, 1, 12740, 4, 1, 1, 1, 31),
    _EqlControllerFullSwRevision_Type()
)
eqlControllerFullSwRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlControllerFullSwRevision.setStatus("current")


class _EqlControllerNVRAMBattery_Type(Integer32):
    """Custom type eqlControllerNVRAMBattery based on Integer32"""
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
        *(("bad", 2),
          ("good", 1),
          ("not-present", 0),
          ("unknown", 3))
    )


_EqlControllerNVRAMBattery_Type.__name__ = "Integer32"
_EqlControllerNVRAMBattery_Object = MibTableColumn
eqlControllerNVRAMBattery = _EqlControllerNVRAMBattery_Object(
    (1, 3, 6, 1, 4, 1, 12740, 4, 1, 1, 1, 32),
    _EqlControllerNVRAMBattery_Type()
)
eqlControllerNVRAMBattery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlControllerNVRAMBattery.setStatus("current")


class _EqlControllerSerialNumber2_Type(DisplayString):
    """Custom type eqlControllerSerialNumber2 based on DisplayString"""
    defaultValue = OctetString("unknown")


_EqlControllerSerialNumber2_Object = MibTableColumn
eqlControllerSerialNumber2 = _EqlControllerSerialNumber2_Object(
    (1, 3, 6, 1, 4, 1, 12740, 4, 1, 1, 1, 33),
    _EqlControllerSerialNumber2_Type()
)
eqlControllerSerialNumber2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlControllerSerialNumber2.setStatus("current")


class _EqlControllerType_Type(DisplayString):
    """Custom type eqlControllerType based on DisplayString"""
    defaultValue = OctetString("unknown")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_EqlControllerType_Type.__name__ = "DisplayString"
_EqlControllerType_Object = MibTableColumn
eqlControllerType = _EqlControllerType_Object(
    (1, 3, 6, 1, 4, 1, 12740, 4, 1, 1, 1, 34),
    _EqlControllerType_Type()
)
eqlControllerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlControllerType.setStatus("current")
_EqlControllerBootTime_Type = Counter32
_EqlControllerBootTime_Object = MibTableColumn
eqlControllerBootTime = _EqlControllerBootTime_Object(
    (1, 3, 6, 1, 4, 1, 12740, 4, 1, 1, 1, 35),
    _EqlControllerBootTime_Type()
)
eqlControllerBootTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlControllerBootTime.setStatus("current")
if mibBuilder.loadTexts:
    eqlControllerBootTime.setUnits("seconds")
_EqlcontrollerNotifications_ObjectIdentity = ObjectIdentity
eqlcontrollerNotifications = _EqlcontrollerNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12740, 4, 2)
)
_EqlcontrollerConformance_ObjectIdentity = ObjectIdentity
eqlcontrollerConformance = _EqlcontrollerConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12740, 4, 3)
)
_EqlbackplaneObjects_ObjectIdentity = ObjectIdentity
eqlbackplaneObjects = _EqlbackplaneObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12740, 4, 4)
)
_EqlBackplaneTable_Object = MibTable
eqlBackplaneTable = _EqlBackplaneTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 4, 4, 1)
)
if mibBuilder.loadTexts:
    eqlBackplaneTable.setStatus("current")
_EqlBackplaneEntry_Object = MibTableRow
eqlBackplaneEntry = _EqlBackplaneEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 4, 4, 1, 1)
)
eqlBackplaneEntry.setIndexNames(
    (0, "EQLGROUP-MIB", "eqlGroupId"),
    (0, "EQLMEMBER-MIB", "eqlMemberIndex"),
    (0, "EQLCONTROLLER-MIB", "eqlBackplaneIndex"),
)
if mibBuilder.loadTexts:
    eqlBackplaneEntry.setStatus("current")


class _EqlBackplaneIndex_Type(Integer32):
    """Custom type eqlBackplaneIndex based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_EqlBackplaneIndex_Type.__name__ = "Integer32"
_EqlBackplaneIndex_Object = MibTableColumn
eqlBackplaneIndex = _EqlBackplaneIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 4, 4, 1, 1, 1),
    _EqlBackplaneIndex_Type()
)
eqlBackplaneIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqlBackplaneIndex.setStatus("current")


class _EqlBackplanePartNum_Type(DisplayString):
    """Custom type eqlBackplanePartNum based on DisplayString"""
    defaultValue = OctetString("unknown")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_EqlBackplanePartNum_Type.__name__ = "DisplayString"
_EqlBackplanePartNum_Object = MibTableColumn
eqlBackplanePartNum = _EqlBackplanePartNum_Object(
    (1, 3, 6, 1, 4, 1, 12740, 4, 4, 1, 1, 2),
    _EqlBackplanePartNum_Type()
)
eqlBackplanePartNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlBackplanePartNum.setStatus("current")


class _EqlBackplaneRev_Type(DisplayString):
    """Custom type eqlBackplaneRev based on DisplayString"""
    defaultValue = OctetString("unknown")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_EqlBackplaneRev_Type.__name__ = "DisplayString"
_EqlBackplaneRev_Object = MibTableColumn
eqlBackplaneRev = _EqlBackplaneRev_Object(
    (1, 3, 6, 1, 4, 1, 12740, 4, 4, 1, 1, 3),
    _EqlBackplaneRev_Type()
)
eqlBackplaneRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlBackplaneRev.setStatus("current")


class _EqlBackplaneDate_Type(DisplayString):
    """Custom type eqlBackplaneDate based on DisplayString"""
    defaultValue = OctetString("unknown")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_EqlBackplaneDate_Type.__name__ = "DisplayString"
_EqlBackplaneDate_Object = MibTableColumn
eqlBackplaneDate = _EqlBackplaneDate_Object(
    (1, 3, 6, 1, 4, 1, 12740, 4, 4, 1, 1, 4),
    _EqlBackplaneDate_Type()
)
eqlBackplaneDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlBackplaneDate.setStatus("current")


class _EqlBackplaneSN_Type(DisplayString):
    """Custom type eqlBackplaneSN based on DisplayString"""
    defaultValue = OctetString("unknown")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_EqlBackplaneSN_Type.__name__ = "DisplayString"
_EqlBackplaneSN_Object = MibTableColumn
eqlBackplaneSN = _EqlBackplaneSN_Object(
    (1, 3, 6, 1, 4, 1, 12740, 4, 4, 1, 1, 5),
    _EqlBackplaneSN_Type()
)
eqlBackplaneSN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlBackplaneSN.setStatus("current")


class _EqlBackplaneECO_Type(DisplayString):
    """Custom type eqlBackplaneECO based on DisplayString"""
    defaultValue = OctetString("unknown")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_EqlBackplaneECO_Type.__name__ = "DisplayString"
_EqlBackplaneECO_Object = MibTableColumn
eqlBackplaneECO = _EqlBackplaneECO_Object(
    (1, 3, 6, 1, 4, 1, 12740, 4, 4, 1, 1, 6),
    _EqlBackplaneECO_Type()
)
eqlBackplaneECO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlBackplaneECO.setStatus("current")


class _EqlBackplaneEEprom_Type(OctetString):
    """Custom type eqlBackplaneEEprom based on OctetString"""
    defaultValue = OctetString("unknown")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(256, 256),
    )


_EqlBackplaneEEprom_Type.__name__ = "OctetString"
_EqlBackplaneEEprom_Object = MibTableColumn
eqlBackplaneEEprom = _EqlBackplaneEEprom_Object(
    (1, 3, 6, 1, 4, 1, 12740, 4, 4, 1, 1, 7),
    _EqlBackplaneEEprom_Type()
)
eqlBackplaneEEprom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlBackplaneEEprom.setStatus("current")


class _EqlBackplaneSN2_Type(DisplayString):
    """Custom type eqlBackplaneSN2 based on DisplayString"""
    defaultValue = OctetString("unknown")


_EqlBackplaneSN2_Object = MibTableColumn
eqlBackplaneSN2 = _EqlBackplaneSN2_Object(
    (1, 3, 6, 1, 4, 1, 12740, 4, 4, 1, 1, 8),
    _EqlBackplaneSN2_Type()
)
eqlBackplaneSN2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlBackplaneSN2.setStatus("current")


class _EqlBackplaneType_Type(DisplayString):
    """Custom type eqlBackplaneType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_EqlBackplaneType_Type.__name__ = "DisplayString"
_EqlBackplaneType_Object = MibTableColumn
eqlBackplaneType = _EqlBackplaneType_Object(
    (1, 3, 6, 1, 4, 1, 12740, 4, 4, 1, 1, 9),
    _EqlBackplaneType_Type()
)
eqlBackplaneType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlBackplaneType.setStatus("current")
_EqlBackplaneTypeId_Type = Integer32
_EqlBackplaneTypeId_Object = MibTableColumn
eqlBackplaneTypeId = _EqlBackplaneTypeId_Object(
    (1, 3, 6, 1, 4, 1, 12740, 4, 4, 1, 1, 10),
    _EqlBackplaneTypeId_Type()
)
eqlBackplaneTypeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlBackplaneTypeId.setStatus("current")
_EqlbackplaneNotifications_ObjectIdentity = ObjectIdentity
eqlbackplaneNotifications = _EqlbackplaneNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12740, 4, 5)
)
_EqlbackplaneConformance_ObjectIdentity = ObjectIdentity
eqlbackplaneConformance = _EqlbackplaneConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12740, 4, 6)
)
_EqlemmObjects_ObjectIdentity = ObjectIdentity
eqlemmObjects = _EqlemmObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12740, 4, 7)
)
_EqlEMMTable_Object = MibTable
eqlEMMTable = _EqlEMMTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 4, 7, 1)
)
if mibBuilder.loadTexts:
    eqlEMMTable.setStatus("current")
_EqlEMMEntry_Object = MibTableRow
eqlEMMEntry = _EqlEMMEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 4, 7, 1, 1)
)
eqlEMMEntry.setIndexNames(
    (0, "EQLGROUP-MIB", "eqlGroupId"),
    (0, "EQLMEMBER-MIB", "eqlMemberIndex"),
    (0, "EQLCONTROLLER-MIB", "eqlEMMIndex"),
)
if mibBuilder.loadTexts:
    eqlEMMEntry.setStatus("current")


class _EqlEMMIndex_Type(Integer32):
    """Custom type eqlEMMIndex based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_EqlEMMIndex_Type.__name__ = "Integer32"
_EqlEMMIndex_Object = MibTableColumn
eqlEMMIndex = _EqlEMMIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 4, 7, 1, 1, 1),
    _EqlEMMIndex_Type()
)
eqlEMMIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqlEMMIndex.setStatus("current")


class _EqlEMMModel_Type(DisplayString):
    """Custom type eqlEMMModel based on DisplayString"""
    defaultValue = OctetString("unknown model")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_EqlEMMModel_Type.__name__ = "DisplayString"
_EqlEMMModel_Object = MibTableColumn
eqlEMMModel = _EqlEMMModel_Object(
    (1, 3, 6, 1, 4, 1, 12740, 4, 7, 1, 1, 2),
    _EqlEMMModel_Type()
)
eqlEMMModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlEMMModel.setStatus("current")


class _EqlEMMPartNum_Type(DisplayString):
    """Custom type eqlEMMPartNum based on DisplayString"""
    defaultValue = OctetString("unknown")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_EqlEMMPartNum_Type.__name__ = "DisplayString"
_EqlEMMPartNum_Object = MibTableColumn
eqlEMMPartNum = _EqlEMMPartNum_Object(
    (1, 3, 6, 1, 4, 1, 12740, 4, 7, 1, 1, 3),
    _EqlEMMPartNum_Type()
)
eqlEMMPartNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlEMMPartNum.setStatus("current")


class _EqlEMMRev_Type(DisplayString):
    """Custom type eqlEMMRev based on DisplayString"""
    defaultValue = OctetString("unknown")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_EqlEMMRev_Type.__name__ = "DisplayString"
_EqlEMMRev_Object = MibTableColumn
eqlEMMRev = _EqlEMMRev_Object(
    (1, 3, 6, 1, 4, 1, 12740, 4, 7, 1, 1, 4),
    _EqlEMMRev_Type()
)
eqlEMMRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlEMMRev.setStatus("current")


class _EqlEMMDate_Type(DisplayString):
    """Custom type eqlEMMDate based on DisplayString"""
    defaultValue = OctetString("unknown")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_EqlEMMDate_Type.__name__ = "DisplayString"
_EqlEMMDate_Object = MibTableColumn
eqlEMMDate = _EqlEMMDate_Object(
    (1, 3, 6, 1, 4, 1, 12740, 4, 7, 1, 1, 5),
    _EqlEMMDate_Type()
)
eqlEMMDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlEMMDate.setStatus("current")


class _EqlEMMSN_Type(DisplayString):
    """Custom type eqlEMMSN based on DisplayString"""
    defaultValue = OctetString("unknown")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_EqlEMMSN_Type.__name__ = "DisplayString"
_EqlEMMSN_Object = MibTableColumn
eqlEMMSN = _EqlEMMSN_Object(
    (1, 3, 6, 1, 4, 1, 12740, 4, 7, 1, 1, 6),
    _EqlEMMSN_Type()
)
eqlEMMSN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlEMMSN.setStatus("current")


class _EqlEMMECO_Type(DisplayString):
    """Custom type eqlEMMECO based on DisplayString"""
    defaultValue = OctetString("unknown")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_EqlEMMECO_Type.__name__ = "DisplayString"
_EqlEMMECO_Object = MibTableColumn
eqlEMMECO = _EqlEMMECO_Object(
    (1, 3, 6, 1, 4, 1, 12740, 4, 7, 1, 1, 7),
    _EqlEMMECO_Type()
)
eqlEMMECO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlEMMECO.setStatus("current")


class _EqlEMMEEprom_Type(OctetString):
    """Custom type eqlEMMEEprom based on OctetString"""
    defaultValue = OctetString("unknown")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(256, 256),
    )


_EqlEMMEEprom_Type.__name__ = "OctetString"
_EqlEMMEEprom_Object = MibTableColumn
eqlEMMEEprom = _EqlEMMEEprom_Object(
    (1, 3, 6, 1, 4, 1, 12740, 4, 7, 1, 1, 8),
    _EqlEMMEEprom_Type()
)
eqlEMMEEprom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlEMMEEprom.setStatus("current")


class _EqlEMMSN2_Type(DisplayString):
    """Custom type eqlEMMSN2 based on DisplayString"""
    defaultValue = OctetString("unknown")


_EqlEMMSN2_Object = MibTableColumn
eqlEMMSN2 = _EqlEMMSN2_Object(
    (1, 3, 6, 1, 4, 1, 12740, 4, 7, 1, 1, 9),
    _EqlEMMSN2_Type()
)
eqlEMMSN2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlEMMSN2.setStatus("current")
_EqlemmNotifications_ObjectIdentity = ObjectIdentity
eqlemmNotifications = _EqlemmNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12740, 4, 8)
)
_EqlemmConformance_ObjectIdentity = ObjectIdentity
eqlemmConformance = _EqlemmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12740, 4, 9)
)
_EqldaughtercardObjects_ObjectIdentity = ObjectIdentity
eqldaughtercardObjects = _EqldaughtercardObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12740, 4, 10)
)
_EqlDaughterCardTable_Object = MibTable
eqlDaughterCardTable = _EqlDaughterCardTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 4, 10, 1)
)
if mibBuilder.loadTexts:
    eqlDaughterCardTable.setStatus("current")
_EqlDaughterCardEntry_Object = MibTableRow
eqlDaughterCardEntry = _EqlDaughterCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 4, 10, 1, 1)
)
eqlDaughterCardEntry.setIndexNames(
    (0, "EQLGROUP-MIB", "eqlGroupId"),
    (0, "EQLMEMBER-MIB", "eqlMemberIndex"),
    (0, "EQLCONTROLLER-MIB", "eqlDaughterCardIndex"),
)
if mibBuilder.loadTexts:
    eqlDaughterCardEntry.setStatus("current")


class _EqlDaughterCardIndex_Type(Integer32):
    """Custom type eqlDaughterCardIndex based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_EqlDaughterCardIndex_Type.__name__ = "Integer32"
_EqlDaughterCardIndex_Object = MibTableColumn
eqlDaughterCardIndex = _EqlDaughterCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 4, 10, 1, 1, 1),
    _EqlDaughterCardIndex_Type()
)
eqlDaughterCardIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqlDaughterCardIndex.setStatus("current")


class _EqlDaughterCardModel_Type(DisplayString):
    """Custom type eqlDaughterCardModel based on DisplayString"""
    defaultValue = OctetString("unknown model")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_EqlDaughterCardModel_Type.__name__ = "DisplayString"
_EqlDaughterCardModel_Object = MibTableColumn
eqlDaughterCardModel = _EqlDaughterCardModel_Object(
    (1, 3, 6, 1, 4, 1, 12740, 4, 10, 1, 1, 2),
    _EqlDaughterCardModel_Type()
)
eqlDaughterCardModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDaughterCardModel.setStatus("current")


class _EqlDaughterCardPartNum_Type(DisplayString):
    """Custom type eqlDaughterCardPartNum based on DisplayString"""
    defaultValue = OctetString("unknown")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_EqlDaughterCardPartNum_Type.__name__ = "DisplayString"
_EqlDaughterCardPartNum_Object = MibTableColumn
eqlDaughterCardPartNum = _EqlDaughterCardPartNum_Object(
    (1, 3, 6, 1, 4, 1, 12740, 4, 10, 1, 1, 3),
    _EqlDaughterCardPartNum_Type()
)
eqlDaughterCardPartNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDaughterCardPartNum.setStatus("current")


class _EqlDaughterCardRev_Type(DisplayString):
    """Custom type eqlDaughterCardRev based on DisplayString"""
    defaultValue = OctetString("unknown")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_EqlDaughterCardRev_Type.__name__ = "DisplayString"
_EqlDaughterCardRev_Object = MibTableColumn
eqlDaughterCardRev = _EqlDaughterCardRev_Object(
    (1, 3, 6, 1, 4, 1, 12740, 4, 10, 1, 1, 4),
    _EqlDaughterCardRev_Type()
)
eqlDaughterCardRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDaughterCardRev.setStatus("current")


class _EqlDaughterCardDate_Type(DisplayString):
    """Custom type eqlDaughterCardDate based on DisplayString"""
    defaultValue = OctetString("unknown")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_EqlDaughterCardDate_Type.__name__ = "DisplayString"
_EqlDaughterCardDate_Object = MibTableColumn
eqlDaughterCardDate = _EqlDaughterCardDate_Object(
    (1, 3, 6, 1, 4, 1, 12740, 4, 10, 1, 1, 5),
    _EqlDaughterCardDate_Type()
)
eqlDaughterCardDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDaughterCardDate.setStatus("current")


class _EqlDaughterCardSN_Type(DisplayString):
    """Custom type eqlDaughterCardSN based on DisplayString"""
    defaultValue = OctetString("unknown")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_EqlDaughterCardSN_Type.__name__ = "DisplayString"
_EqlDaughterCardSN_Object = MibTableColumn
eqlDaughterCardSN = _EqlDaughterCardSN_Object(
    (1, 3, 6, 1, 4, 1, 12740, 4, 10, 1, 1, 6),
    _EqlDaughterCardSN_Type()
)
eqlDaughterCardSN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDaughterCardSN.setStatus("current")


class _EqlDaughterCardECO_Type(DisplayString):
    """Custom type eqlDaughterCardECO based on DisplayString"""
    defaultValue = OctetString("unknown")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_EqlDaughterCardECO_Type.__name__ = "DisplayString"
_EqlDaughterCardECO_Object = MibTableColumn
eqlDaughterCardECO = _EqlDaughterCardECO_Object(
    (1, 3, 6, 1, 4, 1, 12740, 4, 10, 1, 1, 7),
    _EqlDaughterCardECO_Type()
)
eqlDaughterCardECO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDaughterCardECO.setStatus("current")


class _EqlDaughterCardEEprom_Type(OctetString):
    """Custom type eqlDaughterCardEEprom based on OctetString"""
    defaultValue = OctetString("unknown")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(256, 256),
    )


_EqlDaughterCardEEprom_Type.__name__ = "OctetString"
_EqlDaughterCardEEprom_Object = MibTableColumn
eqlDaughterCardEEprom = _EqlDaughterCardEEprom_Object(
    (1, 3, 6, 1, 4, 1, 12740, 4, 10, 1, 1, 8),
    _EqlDaughterCardEEprom_Type()
)
eqlDaughterCardEEprom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDaughterCardEEprom.setStatus("current")
_EqldaughtercardNotifications_ObjectIdentity = ObjectIdentity
eqldaughtercardNotifications = _EqldaughtercardNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12740, 4, 11)
)
_EqldaughtercardConformance_ObjectIdentity = ObjectIdentity
eqldaughtercardConformance = _EqldaughtercardConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12740, 4, 12)
)
_EqlchannelcardObjects_ObjectIdentity = ObjectIdentity
eqlchannelcardObjects = _EqlchannelcardObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12740, 4, 13)
)
_EqlChannelCardTable_Object = MibTable
eqlChannelCardTable = _EqlChannelCardTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 4, 13, 1)
)
if mibBuilder.loadTexts:
    eqlChannelCardTable.setStatus("current")
_EqlChannelCardEntry_Object = MibTableRow
eqlChannelCardEntry = _EqlChannelCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 4, 13, 1, 1)
)
eqlChannelCardEntry.setIndexNames(
    (0, "EQLGROUP-MIB", "eqlGroupId"),
    (0, "EQLMEMBER-MIB", "eqlMemberIndex"),
    (0, "EQLCONTROLLER-MIB", "eqlChannelCardIndex"),
)
if mibBuilder.loadTexts:
    eqlChannelCardEntry.setStatus("current")


class _EqlChannelCardIndex_Type(Unsigned32):
    """Custom type eqlChannelCardIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_EqlChannelCardIndex_Type.__name__ = "Unsigned32"
_EqlChannelCardIndex_Object = MibTableColumn
eqlChannelCardIndex = _EqlChannelCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 4, 13, 1, 1, 1),
    _EqlChannelCardIndex_Type()
)
eqlChannelCardIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqlChannelCardIndex.setStatus("current")


class _EqlChannelCardSerialNumber_Type(DisplayString):
    """Custom type eqlChannelCardSerialNumber based on DisplayString"""
    defaultValue = OctetString("unknown")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_EqlChannelCardSerialNumber_Type.__name__ = "DisplayString"
_EqlChannelCardSerialNumber_Object = MibTableColumn
eqlChannelCardSerialNumber = _EqlChannelCardSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 12740, 4, 13, 1, 1, 2),
    _EqlChannelCardSerialNumber_Type()
)
eqlChannelCardSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlChannelCardSerialNumber.setStatus("current")


class _EqlChannelCardFirmwareRev_Type(DisplayString):
    """Custom type eqlChannelCardFirmwareRev based on DisplayString"""
    defaultValue = OctetString("unknown")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_EqlChannelCardFirmwareRev_Type.__name__ = "DisplayString"
_EqlChannelCardFirmwareRev_Object = MibTableColumn
eqlChannelCardFirmwareRev = _EqlChannelCardFirmwareRev_Object(
    (1, 3, 6, 1, 4, 1, 12740, 4, 13, 1, 1, 3),
    _EqlChannelCardFirmwareRev_Type()
)
eqlChannelCardFirmwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlChannelCardFirmwareRev.setStatus("current")


class _EqlChannelCardInitRev_Type(DisplayString):
    """Custom type eqlChannelCardInitRev based on DisplayString"""
    defaultValue = OctetString("unknown")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_EqlChannelCardInitRev_Type.__name__ = "DisplayString"
_EqlChannelCardInitRev_Object = MibTableColumn
eqlChannelCardInitRev = _EqlChannelCardInitRev_Object(
    (1, 3, 6, 1, 4, 1, 12740, 4, 13, 1, 1, 4),
    _EqlChannelCardInitRev_Type()
)
eqlChannelCardInitRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlChannelCardInitRev.setStatus("current")


class _EqlChannelCardStatus_Type(Integer32):
    """Custom type eqlChannelCardStatus based on Integer32"""
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
        *(("failed", 2),
          ("good", 3),
          ("not-present", 1),
          ("unknown", 0))
    )


_EqlChannelCardStatus_Type.__name__ = "Integer32"
_EqlChannelCardStatus_Object = MibTableColumn
eqlChannelCardStatus = _EqlChannelCardStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 4, 13, 1, 1, 5),
    _EqlChannelCardStatus_Type()
)
eqlChannelCardStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlChannelCardStatus.setStatus("current")
_EqlsfpObjects_ObjectIdentity = ObjectIdentity
eqlsfpObjects = _EqlsfpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12740, 4, 14)
)
_EqlSFPTable_Object = MibTable
eqlSFPTable = _EqlSFPTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 4, 14, 1)
)
if mibBuilder.loadTexts:
    eqlSFPTable.setStatus("current")
_EqlSFPEntry_Object = MibTableRow
eqlSFPEntry = _EqlSFPEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 4, 14, 1, 1)
)
eqlSFPEntry.setIndexNames(
    (0, "EQLGROUP-MIB", "eqlGroupId"),
    (0, "EQLMEMBER-MIB", "eqlMemberIndex"),
    (0, "EQLCONTROLLER-MIB", "eqlSFPIndex"),
)
if mibBuilder.loadTexts:
    eqlSFPEntry.setStatus("current")


class _EqlSFPIndex_Type(Unsigned32):
    """Custom type eqlSFPIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_EqlSFPIndex_Type.__name__ = "Unsigned32"
_EqlSFPIndex_Object = MibTableColumn
eqlSFPIndex = _EqlSFPIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 4, 14, 1, 1, 1),
    _EqlSFPIndex_Type()
)
eqlSFPIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqlSFPIndex.setStatus("current")


class _EqlSFPMode_Type(Integer32):
    """Custom type eqlSFPMode based on Integer32"""
    defaultValue = 0

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
        *(("copper", 3),
          ("multi-mode", 2),
          ("not-present", 4),
          ("single-mode", 1),
          ("unknown", 0))
    )


_EqlSFPMode_Type.__name__ = "Integer32"
_EqlSFPMode_Object = MibTableColumn
eqlSFPMode = _EqlSFPMode_Object(
    (1, 3, 6, 1, 4, 1, 12740, 4, 14, 1, 1, 2),
    _EqlSFPMode_Type()
)
eqlSFPMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlSFPMode.setStatus("current")
_EqlSFPIfIndex_Type = Integer32
_EqlSFPIfIndex_Object = MibTableColumn
eqlSFPIfIndex = _EqlSFPIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 4, 14, 1, 1, 3),
    _EqlSFPIfIndex_Type()
)
eqlSFPIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlSFPIfIndex.setStatus("current")


class _EqlSFPIdentifier_Type(Integer32):
    """Custom type eqlSFPIdentifier based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              3)
        )
    )
    namedValues = NamedValues(
        *(("sfp-transceiver", 3),
          ("unknown", 0))
    )


_EqlSFPIdentifier_Type.__name__ = "Integer32"
_EqlSFPIdentifier_Object = MibTableColumn
eqlSFPIdentifier = _EqlSFPIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 12740, 4, 14, 1, 1, 4),
    _EqlSFPIdentifier_Type()
)
eqlSFPIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlSFPIdentifier.setStatus("current")


class _EqlSFPConnector_Type(Integer32):
    """Custom type eqlSFPConnector based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              7,
              33)
        )
    )
    namedValues = NamedValues(
        *(("copper", 33),
          ("lc", 7),
          ("unknown", 0))
    )


_EqlSFPConnector_Type.__name__ = "Integer32"
_EqlSFPConnector_Object = MibTableColumn
eqlSFPConnector = _EqlSFPConnector_Object(
    (1, 3, 6, 1, 4, 1, 12740, 4, 14, 1, 1, 5),
    _EqlSFPConnector_Type()
)
eqlSFPConnector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlSFPConnector.setStatus("current")
_EqlSFPBitrate_Type = Integer32
_EqlSFPBitrate_Object = MibTableColumn
eqlSFPBitrate = _EqlSFPBitrate_Object(
    (1, 3, 6, 1, 4, 1, 12740, 4, 14, 1, 1, 6),
    _EqlSFPBitrate_Type()
)
eqlSFPBitrate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlSFPBitrate.setStatus("current")
_EqlSFPLength1_Type = Integer32
_EqlSFPLength1_Object = MibTableColumn
eqlSFPLength1 = _EqlSFPLength1_Object(
    (1, 3, 6, 1, 4, 1, 12740, 4, 14, 1, 1, 7),
    _EqlSFPLength1_Type()
)
eqlSFPLength1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlSFPLength1.setStatus("current")
_EqlSFPLength2_Type = Integer32
_EqlSFPLength2_Object = MibTableColumn
eqlSFPLength2 = _EqlSFPLength2_Object(
    (1, 3, 6, 1, 4, 1, 12740, 4, 14, 1, 1, 8),
    _EqlSFPLength2_Type()
)
eqlSFPLength2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlSFPLength2.setStatus("current")


class _EqlSFPVendorName_Type(DisplayString):
    """Custom type eqlSFPVendorName based on DisplayString"""
    defaultValue = OctetString("unknown")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_EqlSFPVendorName_Type.__name__ = "DisplayString"
_EqlSFPVendorName_Object = MibTableColumn
eqlSFPVendorName = _EqlSFPVendorName_Object(
    (1, 3, 6, 1, 4, 1, 12740, 4, 14, 1, 1, 9),
    _EqlSFPVendorName_Type()
)
eqlSFPVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlSFPVendorName.setStatus("current")


class _EqlSFPPartNumber_Type(DisplayString):
    """Custom type eqlSFPPartNumber based on DisplayString"""
    defaultValue = OctetString("unknown")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_EqlSFPPartNumber_Type.__name__ = "DisplayString"
_EqlSFPPartNumber_Object = MibTableColumn
eqlSFPPartNumber = _EqlSFPPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 12740, 4, 14, 1, 1, 10),
    _EqlSFPPartNumber_Type()
)
eqlSFPPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlSFPPartNumber.setStatus("current")


class _EqlSFPFirmwareRev_Type(DisplayString):
    """Custom type eqlSFPFirmwareRev based on DisplayString"""
    defaultValue = OctetString("unknown")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_EqlSFPFirmwareRev_Type.__name__ = "DisplayString"
_EqlSFPFirmwareRev_Object = MibTableColumn
eqlSFPFirmwareRev = _EqlSFPFirmwareRev_Object(
    (1, 3, 6, 1, 4, 1, 12740, 4, 14, 1, 1, 11),
    _EqlSFPFirmwareRev_Type()
)
eqlSFPFirmwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlSFPFirmwareRev.setStatus("current")


class _EqlSFPSerialNumber_Type(DisplayString):
    """Custom type eqlSFPSerialNumber based on DisplayString"""
    defaultValue = OctetString("unknown")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_EqlSFPSerialNumber_Type.__name__ = "DisplayString"
_EqlSFPSerialNumber_Object = MibTableColumn
eqlSFPSerialNumber = _EqlSFPSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 12740, 4, 14, 1, 1, 12),
    _EqlSFPSerialNumber_Type()
)
eqlSFPSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlSFPSerialNumber.setStatus("current")


class _EqlSFPDateCode_Type(DisplayString):
    """Custom type eqlSFPDateCode based on DisplayString"""
    defaultValue = OctetString("unknown")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_EqlSFPDateCode_Type.__name__ = "DisplayString"
_EqlSFPDateCode_Object = MibTableColumn
eqlSFPDateCode = _EqlSFPDateCode_Object(
    (1, 3, 6, 1, 4, 1, 12740, 4, 14, 1, 1, 13),
    _EqlSFPDateCode_Type()
)
eqlSFPDateCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlSFPDateCode.setStatus("current")


class _EqlSFPStatus_Type(Integer32):
    """Custom type eqlSFPStatus based on Integer32"""
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
        *(("failed", 2),
          ("good", 3),
          ("not-present", 1),
          ("unknown", 0))
    )


_EqlSFPStatus_Type.__name__ = "Integer32"
_EqlSFPStatus_Object = MibTableColumn
eqlSFPStatus = _EqlSFPStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 4, 14, 1, 1, 14),
    _EqlSFPStatus_Type()
)
eqlSFPStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlSFPStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EQLCONTROLLER-MIB",
    **{"eqlcontrollerModule": eqlcontrollerModule,
       "eqlcontrollerObjects": eqlcontrollerObjects,
       "eqlControllerTable": eqlControllerTable,
       "eqlControllerEntry": eqlControllerEntry,
       "eqlControllerIndex": eqlControllerIndex,
       "eqlControllerModel": eqlControllerModel,
       "eqlControllerCMRevision": eqlControllerCMRevision,
       "eqlControllerSwRevision": eqlControllerSwRevision,
       "eqlControllerBatteryStatus": eqlControllerBatteryStatus,
       "eqlControllerUpTime": eqlControllerUpTime,
       "eqlControllerProcessorTemp": eqlControllerProcessorTemp,
       "eqlControllerChipsetTemp": eqlControllerChipsetTemp,
       "eqlControllerPrimaryOrSecondary": eqlControllerPrimaryOrSecondary,
       "eqlControllerPrimaryFlashImageRev": eqlControllerPrimaryFlashImageRev,
       "eqlControllerSecondaryFlashImageRev": eqlControllerSecondaryFlashImageRev,
       "eqlControllerSerialNumber": eqlControllerSerialNumber,
       "eqlControllerDate": eqlControllerDate,
       "eqlControllerECO": eqlControllerECO,
       "eqlControllerEEprom": eqlControllerEEprom,
       "eqlControllerPLDrev": eqlControllerPLDrev,
       "eqlControllerPlatformType": eqlControllerPlatformType,
       "eqlControllerPlatformVersion": eqlControllerPlatformVersion,
       "eqlControllerCPUPass": eqlControllerCPUPass,
       "eqlControllerCPUrev": eqlControllerCPUrev,
       "eqlControllerCPUfreq": eqlControllerCPUfreq,
       "eqlControllerPhysRam": eqlControllerPhysRam,
       "eqlControllerBootRomVersion": eqlControllerBootRomVersion,
       "eqlControllerBootRomBuildDate": eqlControllerBootRomBuildDate,
       "eqlControllerInfoMsg": eqlControllerInfoMsg,
       "eqlControllerAthenaSataVersion": eqlControllerAthenaSataVersion,
       "eqlControllerMajorVersion": eqlControllerMajorVersion,
       "eqlControllerMinorVersion": eqlControllerMinorVersion,
       "eqlControllerMaintenanceVersion": eqlControllerMaintenanceVersion,
       "eqlControllerSWCompatibilityLevel": eqlControllerSWCompatibilityLevel,
       "eqlControllerFullSwRevision": eqlControllerFullSwRevision,
       "eqlControllerNVRAMBattery": eqlControllerNVRAMBattery,
       "eqlControllerSerialNumber2": eqlControllerSerialNumber2,
       "eqlControllerType": eqlControllerType,
       "eqlControllerBootTime": eqlControllerBootTime,
       "eqlcontrollerNotifications": eqlcontrollerNotifications,
       "eqlcontrollerConformance": eqlcontrollerConformance,
       "eqlbackplaneObjects": eqlbackplaneObjects,
       "eqlBackplaneTable": eqlBackplaneTable,
       "eqlBackplaneEntry": eqlBackplaneEntry,
       "eqlBackplaneIndex": eqlBackplaneIndex,
       "eqlBackplanePartNum": eqlBackplanePartNum,
       "eqlBackplaneRev": eqlBackplaneRev,
       "eqlBackplaneDate": eqlBackplaneDate,
       "eqlBackplaneSN": eqlBackplaneSN,
       "eqlBackplaneECO": eqlBackplaneECO,
       "eqlBackplaneEEprom": eqlBackplaneEEprom,
       "eqlBackplaneSN2": eqlBackplaneSN2,
       "eqlBackplaneType": eqlBackplaneType,
       "eqlBackplaneTypeId": eqlBackplaneTypeId,
       "eqlbackplaneNotifications": eqlbackplaneNotifications,
       "eqlbackplaneConformance": eqlbackplaneConformance,
       "eqlemmObjects": eqlemmObjects,
       "eqlEMMTable": eqlEMMTable,
       "eqlEMMEntry": eqlEMMEntry,
       "eqlEMMIndex": eqlEMMIndex,
       "eqlEMMModel": eqlEMMModel,
       "eqlEMMPartNum": eqlEMMPartNum,
       "eqlEMMRev": eqlEMMRev,
       "eqlEMMDate": eqlEMMDate,
       "eqlEMMSN": eqlEMMSN,
       "eqlEMMECO": eqlEMMECO,
       "eqlEMMEEprom": eqlEMMEEprom,
       "eqlEMMSN2": eqlEMMSN2,
       "eqlemmNotifications": eqlemmNotifications,
       "eqlemmConformance": eqlemmConformance,
       "eqldaughtercardObjects": eqldaughtercardObjects,
       "eqlDaughterCardTable": eqlDaughterCardTable,
       "eqlDaughterCardEntry": eqlDaughterCardEntry,
       "eqlDaughterCardIndex": eqlDaughterCardIndex,
       "eqlDaughterCardModel": eqlDaughterCardModel,
       "eqlDaughterCardPartNum": eqlDaughterCardPartNum,
       "eqlDaughterCardRev": eqlDaughterCardRev,
       "eqlDaughterCardDate": eqlDaughterCardDate,
       "eqlDaughterCardSN": eqlDaughterCardSN,
       "eqlDaughterCardECO": eqlDaughterCardECO,
       "eqlDaughterCardEEprom": eqlDaughterCardEEprom,
       "eqldaughtercardNotifications": eqldaughtercardNotifications,
       "eqldaughtercardConformance": eqldaughtercardConformance,
       "eqlchannelcardObjects": eqlchannelcardObjects,
       "eqlChannelCardTable": eqlChannelCardTable,
       "eqlChannelCardEntry": eqlChannelCardEntry,
       "eqlChannelCardIndex": eqlChannelCardIndex,
       "eqlChannelCardSerialNumber": eqlChannelCardSerialNumber,
       "eqlChannelCardFirmwareRev": eqlChannelCardFirmwareRev,
       "eqlChannelCardInitRev": eqlChannelCardInitRev,
       "eqlChannelCardStatus": eqlChannelCardStatus,
       "eqlsfpObjects": eqlsfpObjects,
       "eqlSFPTable": eqlSFPTable,
       "eqlSFPEntry": eqlSFPEntry,
       "eqlSFPIndex": eqlSFPIndex,
       "eqlSFPMode": eqlSFPMode,
       "eqlSFPIfIndex": eqlSFPIfIndex,
       "eqlSFPIdentifier": eqlSFPIdentifier,
       "eqlSFPConnector": eqlSFPConnector,
       "eqlSFPBitrate": eqlSFPBitrate,
       "eqlSFPLength1": eqlSFPLength1,
       "eqlSFPLength2": eqlSFPLength2,
       "eqlSFPVendorName": eqlSFPVendorName,
       "eqlSFPPartNumber": eqlSFPPartNumber,
       "eqlSFPFirmwareRev": eqlSFPFirmwareRev,
       "eqlSFPSerialNumber": eqlSFPSerialNumber,
       "eqlSFPDateCode": eqlSFPDateCode,
       "eqlSFPStatus": eqlSFPStatus}
)
