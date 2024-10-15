# SNMP MIB module (DLINK-MCB-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DLINK-MCB-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:30:49 2024
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

_Company_ObjectIdentity = ObjectIdentity
company = _Company_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171)
)
_McbMediaConverterFamily_ObjectIdentity = ObjectIdentity
mcbMediaConverterFamily = _McbMediaConverterFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 41)
)
_McbMediaConverterChassis_ObjectIdentity = ObjectIdentity
mcbMediaConverterChassis = _McbMediaConverterChassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 41, 1)
)
_McbSNMPMIB_ObjectIdentity = ObjectIdentity
mcbSNMPMIB = _McbSNMPMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 41, 1, 1)
)


class _McbSNMPTrapPowerFail_Type(Integer32):
    """Custom type mcbSNMPTrapPowerFail based on Integer32"""
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


_McbSNMPTrapPowerFail_Type.__name__ = "Integer32"
_McbSNMPTrapPowerFail_Object = MibScalar
mcbSNMPTrapPowerFail = _McbSNMPTrapPowerFail_Object(
    (1, 3, 6, 1, 4, 1, 171, 41, 1, 1, 1),
    _McbSNMPTrapPowerFail_Type()
)
mcbSNMPTrapPowerFail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcbSNMPTrapPowerFail.setStatus("mandatory")


class _McbSNMPTrapFanFail_Type(Integer32):
    """Custom type mcbSNMPTrapFanFail based on Integer32"""
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


_McbSNMPTrapFanFail_Type.__name__ = "Integer32"
_McbSNMPTrapFanFail_Object = MibScalar
mcbSNMPTrapFanFail = _McbSNMPTrapFanFail_Object(
    (1, 3, 6, 1, 4, 1, 171, 41, 1, 1, 2),
    _McbSNMPTrapFanFail_Type()
)
mcbSNMPTrapFanFail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcbSNMPTrapFanFail.setStatus("mandatory")


class _McbSNMPTrapMCPlugin_Type(Integer32):
    """Custom type mcbSNMPTrapMCPlugin based on Integer32"""
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


_McbSNMPTrapMCPlugin_Type.__name__ = "Integer32"
_McbSNMPTrapMCPlugin_Object = MibScalar
mcbSNMPTrapMCPlugin = _McbSNMPTrapMCPlugin_Object(
    (1, 3, 6, 1, 4, 1, 171, 41, 1, 1, 3),
    _McbSNMPTrapMCPlugin_Type()
)
mcbSNMPTrapMCPlugin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcbSNMPTrapMCPlugin.setStatus("mandatory")


class _McbSNMPTrapMCPullout_Type(Integer32):
    """Custom type mcbSNMPTrapMCPullout based on Integer32"""
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


_McbSNMPTrapMCPullout_Type.__name__ = "Integer32"
_McbSNMPTrapMCPullout_Object = MibScalar
mcbSNMPTrapMCPullout = _McbSNMPTrapMCPullout_Object(
    (1, 3, 6, 1, 4, 1, 171, 41, 1, 1, 4),
    _McbSNMPTrapMCPullout_Type()
)
mcbSNMPTrapMCPullout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcbSNMPTrapMCPullout.setStatus("mandatory")


class _McbSNMPTrapMCLinkDown_Type(Integer32):
    """Custom type mcbSNMPTrapMCLinkDown based on Integer32"""
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


_McbSNMPTrapMCLinkDown_Type.__name__ = "Integer32"
_McbSNMPTrapMCLinkDown_Object = MibScalar
mcbSNMPTrapMCLinkDown = _McbSNMPTrapMCLinkDown_Object(
    (1, 3, 6, 1, 4, 1, 171, 41, 1, 1, 5),
    _McbSNMPTrapMCLinkDown_Type()
)
mcbSNMPTrapMCLinkDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcbSNMPTrapMCLinkDown.setStatus("mandatory")


class _McbSNMPTrapMCLinkUp_Type(Integer32):
    """Custom type mcbSNMPTrapMCLinkUp based on Integer32"""
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


_McbSNMPTrapMCLinkUp_Type.__name__ = "Integer32"
_McbSNMPTrapMCLinkUp_Object = MibScalar
mcbSNMPTrapMCLinkUp = _McbSNMPTrapMCLinkUp_Object(
    (1, 3, 6, 1, 4, 1, 171, 41, 1, 1, 6),
    _McbSNMPTrapMCLinkUp_Type()
)
mcbSNMPTrapMCLinkUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcbSNMPTrapMCLinkUp.setStatus("mandatory")


class _McbSNMPTrapMCLinkBroken_Type(Integer32):
    """Custom type mcbSNMPTrapMCLinkBroken based on Integer32"""
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


_McbSNMPTrapMCLinkBroken_Type.__name__ = "Integer32"
_McbSNMPTrapMCLinkBroken_Object = MibScalar
mcbSNMPTrapMCLinkBroken = _McbSNMPTrapMCLinkBroken_Object(
    (1, 3, 6, 1, 4, 1, 171, 41, 1, 1, 7),
    _McbSNMPTrapMCLinkBroken_Type()
)
mcbSNMPTrapMCLinkBroken.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcbSNMPTrapMCLinkBroken.setStatus("mandatory")


class _McbSNMPTrapMCActiveSlotChange_Type(Integer32):
    """Custom type mcbSNMPTrapMCActiveSlotChange based on Integer32"""
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


_McbSNMPTrapMCActiveSlotChange_Type.__name__ = "Integer32"
_McbSNMPTrapMCActiveSlotChange_Object = MibScalar
mcbSNMPTrapMCActiveSlotChange = _McbSNMPTrapMCActiveSlotChange_Object(
    (1, 3, 6, 1, 4, 1, 171, 41, 1, 1, 8),
    _McbSNMPTrapMCActiveSlotChange_Type()
)
mcbSNMPTrapMCActiveSlotChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcbSNMPTrapMCActiveSlotChange.setStatus("mandatory")


class _McbSNMPTrapMCActiveSlotLose_Type(Integer32):
    """Custom type mcbSNMPTrapMCActiveSlotLose based on Integer32"""
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


_McbSNMPTrapMCActiveSlotLose_Type.__name__ = "Integer32"
_McbSNMPTrapMCActiveSlotLose_Object = MibScalar
mcbSNMPTrapMCActiveSlotLose = _McbSNMPTrapMCActiveSlotLose_Object(
    (1, 3, 6, 1, 4, 1, 171, 41, 1, 1, 9),
    _McbSNMPTrapMCActiveSlotLose_Type()
)
mcbSNMPTrapMCActiveSlotLose.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcbSNMPTrapMCActiveSlotLose.setStatus("mandatory")
_McbAdministrator_ObjectIdentity = ObjectIdentity
mcbAdministrator = _McbAdministrator_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 41, 1, 2)
)
_McbAdministratorHardwareRev_Type = DisplayString
_McbAdministratorHardwareRev_Object = MibScalar
mcbAdministratorHardwareRev = _McbAdministratorHardwareRev_Object(
    (1, 3, 6, 1, 4, 1, 171, 41, 1, 2, 1),
    _McbAdministratorHardwareRev_Type()
)
mcbAdministratorHardwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcbAdministratorHardwareRev.setStatus("mandatory")
_McbAdministratorSoftwareRev_Type = DisplayString
_McbAdministratorSoftwareRev_Object = MibScalar
mcbAdministratorSoftwareRev = _McbAdministratorSoftwareRev_Object(
    (1, 3, 6, 1, 4, 1, 171, 41, 1, 2, 2),
    _McbAdministratorSoftwareRev_Type()
)
mcbAdministratorSoftwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcbAdministratorSoftwareRev.setStatus("mandatory")
_McbAdministratorBiosRev_Type = DisplayString
_McbAdministratorBiosRev_Object = MibScalar
mcbAdministratorBiosRev = _McbAdministratorBiosRev_Object(
    (1, 3, 6, 1, 4, 1, 171, 41, 1, 2, 3),
    _McbAdministratorBiosRev_Type()
)
mcbAdministratorBiosRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcbAdministratorBiosRev.setStatus("mandatory")


class _McbAdministratorFactoryReset_Type(Integer32):
    """Custom type mcbAdministratorFactoryReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("action", 1)
    )


_McbAdministratorFactoryReset_Type.__name__ = "Integer32"
_McbAdministratorFactoryReset_Object = MibScalar
mcbAdministratorFactoryReset = _McbAdministratorFactoryReset_Object(
    (1, 3, 6, 1, 4, 1, 171, 41, 1, 2, 4),
    _McbAdministratorFactoryReset_Type()
)
mcbAdministratorFactoryReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcbAdministratorFactoryReset.setStatus("mandatory")


class _McbAdministratorFactoryResetCPU_Type(Integer32):
    """Custom type mcbAdministratorFactoryResetCPU based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("action", 1)
    )


_McbAdministratorFactoryResetCPU_Type.__name__ = "Integer32"
_McbAdministratorFactoryResetCPU_Object = MibScalar
mcbAdministratorFactoryResetCPU = _McbAdministratorFactoryResetCPU_Object(
    (1, 3, 6, 1, 4, 1, 171, 41, 1, 2, 5),
    _McbAdministratorFactoryResetCPU_Type()
)
mcbAdministratorFactoryResetCPU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcbAdministratorFactoryResetCPU.setStatus("mandatory")


class _McbAdministratorSoftwareReboot_Type(Integer32):
    """Custom type mcbAdministratorSoftwareReboot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("action", 1)
    )


_McbAdministratorSoftwareReboot_Type.__name__ = "Integer32"
_McbAdministratorSoftwareReboot_Object = MibScalar
mcbAdministratorSoftwareReboot = _McbAdministratorSoftwareReboot_Object(
    (1, 3, 6, 1, 4, 1, 171, 41, 1, 2, 6),
    _McbAdministratorSoftwareReboot_Type()
)
mcbAdministratorSoftwareReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcbAdministratorSoftwareReboot.setStatus("mandatory")
_McbMCFrame_ObjectIdentity = ObjectIdentity
mcbMCFrame = _McbMCFrame_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 41, 1, 3)
)


class _McbFramePowerOneOnStatus_Type(Integer32):
    """Custom type mcbFramePowerOneOnStatus based on Integer32"""
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


_McbFramePowerOneOnStatus_Type.__name__ = "Integer32"
_McbFramePowerOneOnStatus_Object = MibScalar
mcbFramePowerOneOnStatus = _McbFramePowerOneOnStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 41, 1, 3, 1),
    _McbFramePowerOneOnStatus_Type()
)
mcbFramePowerOneOnStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcbFramePowerOneOnStatus.setStatus("mandatory")


class _McbFramePowerTwoOnStatus_Type(Integer32):
    """Custom type mcbFramePowerTwoOnStatus based on Integer32"""
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


_McbFramePowerTwoOnStatus_Type.__name__ = "Integer32"
_McbFramePowerTwoOnStatus_Object = MibScalar
mcbFramePowerTwoOnStatus = _McbFramePowerTwoOnStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 41, 1, 3, 2),
    _McbFramePowerTwoOnStatus_Type()
)
mcbFramePowerTwoOnStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcbFramePowerTwoOnStatus.setStatus("mandatory")


class _McbFramePowerOneFailStatus_Type(Integer32):
    """Custom type mcbFramePowerOneFailStatus based on Integer32"""
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


_McbFramePowerOneFailStatus_Type.__name__ = "Integer32"
_McbFramePowerOneFailStatus_Object = MibScalar
mcbFramePowerOneFailStatus = _McbFramePowerOneFailStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 41, 1, 3, 3),
    _McbFramePowerOneFailStatus_Type()
)
mcbFramePowerOneFailStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcbFramePowerOneFailStatus.setStatus("mandatory")


class _McbFramePowerTwoFailStatus_Type(Integer32):
    """Custom type mcbFramePowerTwoFailStatus based on Integer32"""
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


_McbFramePowerTwoFailStatus_Type.__name__ = "Integer32"
_McbFramePowerTwoFailStatus_Object = MibScalar
mcbFramePowerTwoFailStatus = _McbFramePowerTwoFailStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 41, 1, 3, 4),
    _McbFramePowerTwoFailStatus_Type()
)
mcbFramePowerTwoFailStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcbFramePowerTwoFailStatus.setStatus("mandatory")


class _McbFrameFanOneFailStatus_Type(Integer32):
    """Custom type mcbFrameFanOneFailStatus based on Integer32"""
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


_McbFrameFanOneFailStatus_Type.__name__ = "Integer32"
_McbFrameFanOneFailStatus_Object = MibScalar
mcbFrameFanOneFailStatus = _McbFrameFanOneFailStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 41, 1, 3, 5),
    _McbFrameFanOneFailStatus_Type()
)
mcbFrameFanOneFailStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcbFrameFanOneFailStatus.setStatus("mandatory")


class _McbFrameFanTwoFailStatus_Type(Integer32):
    """Custom type mcbFrameFanTwoFailStatus based on Integer32"""
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


_McbFrameFanTwoFailStatus_Type.__name__ = "Integer32"
_McbFrameFanTwoFailStatus_Object = MibScalar
mcbFrameFanTwoFailStatus = _McbFrameFanTwoFailStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 41, 1, 3, 6),
    _McbFrameFanTwoFailStatus_Type()
)
mcbFrameFanTwoFailStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcbFrameFanTwoFailStatus.setStatus("mandatory")
_McbMCSlots_ObjectIdentity = ObjectIdentity
mcbMCSlots = _McbMCSlots_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 41, 1, 4)
)
_McbMCSlotCount_Type = Integer32
_McbMCSlotCount_Object = MibScalar
mcbMCSlotCount = _McbMCSlotCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 41, 1, 4, 1),
    _McbMCSlotCount_Type()
)
mcbMCSlotCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcbMCSlotCount.setStatus("mandatory")
_McbMCSlotTable_Object = MibTable
mcbMCSlotTable = _McbMCSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 41, 1, 4, 2)
)
if mibBuilder.loadTexts:
    mcbMCSlotTable.setStatus("mandatory")
_McbMCSlotEntry_Object = MibTableRow
mcbMCSlotEntry = _McbMCSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 41, 1, 4, 2, 1)
)
mcbMCSlotEntry.setIndexNames(
    (0, "DLINK-MCB-MIB", "mcbMCSlotNo"),
)
if mibBuilder.loadTexts:
    mcbMCSlotEntry.setStatus("mandatory")
_McbMCSlotNo_Type = Integer32
_McbMCSlotNo_Object = MibTableColumn
mcbMCSlotNo = _McbMCSlotNo_Object(
    (1, 3, 6, 1, 4, 1, 171, 41, 1, 4, 2, 1, 1),
    _McbMCSlotNo_Type()
)
mcbMCSlotNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcbMCSlotNo.setStatus("mandatory")


class _McbMCSlotExist_Type(Integer32):
    """Custom type mcbMCSlotExist based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("exist", 1),
          ("nonexist", 2),
          ("unsupported", 3))
    )


_McbMCSlotExist_Type.__name__ = "Integer32"
_McbMCSlotExist_Object = MibTableColumn
mcbMCSlotExist = _McbMCSlotExist_Object(
    (1, 3, 6, 1, 4, 1, 171, 41, 1, 4, 2, 1, 2),
    _McbMCSlotExist_Type()
)
mcbMCSlotExist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcbMCSlotExist.setStatus("mandatory")
_McbMCModelName_Type = DisplayString
_McbMCModelName_Object = MibTableColumn
mcbMCModelName = _McbMCModelName_Object(
    (1, 3, 6, 1, 4, 1, 171, 41, 1, 4, 2, 1, 3),
    _McbMCModelName_Type()
)
mcbMCModelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcbMCModelName.setStatus("mandatory")


class _McbMCMediaOneType_Type(Integer32):
    """Custom type mcbMCMediaOneType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fiber", 2),
          ("tp", 1),
          ("unsupported", 3))
    )


_McbMCMediaOneType_Type.__name__ = "Integer32"
_McbMCMediaOneType_Object = MibTableColumn
mcbMCMediaOneType = _McbMCMediaOneType_Object(
    (1, 3, 6, 1, 4, 1, 171, 41, 1, 4, 2, 1, 4),
    _McbMCMediaOneType_Type()
)
mcbMCMediaOneType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcbMCMediaOneType.setStatus("mandatory")


class _McbMCMediaTwoType_Type(Integer32):
    """Custom type mcbMCMediaTwoType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fiber", 2),
          ("tp", 1),
          ("unsupported", 3))
    )


_McbMCMediaTwoType_Type.__name__ = "Integer32"
_McbMCMediaTwoType_Object = MibTableColumn
mcbMCMediaTwoType = _McbMCMediaTwoType_Object(
    (1, 3, 6, 1, 4, 1, 171, 41, 1, 4, 2, 1, 5),
    _McbMCMediaTwoType_Type()
)
mcbMCMediaTwoType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcbMCMediaTwoType.setStatus("mandatory")


class _McbMCMediaOneLinkStatus_Type(Integer32):
    """Custom type mcbMCMediaOneLinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("offline", 2),
          ("online", 1),
          ("unsupported", 3))
    )


_McbMCMediaOneLinkStatus_Type.__name__ = "Integer32"
_McbMCMediaOneLinkStatus_Object = MibTableColumn
mcbMCMediaOneLinkStatus = _McbMCMediaOneLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 41, 1, 4, 2, 1, 6),
    _McbMCMediaOneLinkStatus_Type()
)
mcbMCMediaOneLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcbMCMediaOneLinkStatus.setStatus("mandatory")


class _McbMCMediaTwoLinkStatus_Type(Integer32):
    """Custom type mcbMCMediaTwoLinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("offline", 2),
          ("online", 1),
          ("unsupported", 3))
    )


_McbMCMediaTwoLinkStatus_Type.__name__ = "Integer32"
_McbMCMediaTwoLinkStatus_Object = MibTableColumn
mcbMCMediaTwoLinkStatus = _McbMCMediaTwoLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 41, 1, 4, 2, 1, 7),
    _McbMCMediaTwoLinkStatus_Type()
)
mcbMCMediaTwoLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcbMCMediaTwoLinkStatus.setStatus("mandatory")


class _McbMCMediaOneDupStatus_Type(Integer32):
    """Custom type mcbMCMediaOneDupStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("full", 2),
          ("half", 1),
          ("unsupported", 3))
    )


_McbMCMediaOneDupStatus_Type.__name__ = "Integer32"
_McbMCMediaOneDupStatus_Object = MibTableColumn
mcbMCMediaOneDupStatus = _McbMCMediaOneDupStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 41, 1, 4, 2, 1, 8),
    _McbMCMediaOneDupStatus_Type()
)
mcbMCMediaOneDupStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcbMCMediaOneDupStatus.setStatus("mandatory")


class _McbMCMediaTwoDupStatus_Type(Integer32):
    """Custom type mcbMCMediaTwoDupStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("full", 2),
          ("half", 1),
          ("unsupported", 3))
    )


_McbMCMediaTwoDupStatus_Type.__name__ = "Integer32"
_McbMCMediaTwoDupStatus_Object = MibTableColumn
mcbMCMediaTwoDupStatus = _McbMCMediaTwoDupStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 41, 1, 4, 2, 1, 9),
    _McbMCMediaTwoDupStatus_Type()
)
mcbMCMediaTwoDupStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcbMCMediaTwoDupStatus.setStatus("mandatory")


class _McbMCMediaOneSpeedStatus_Type(Integer32):
    """Custom type mcbMCMediaOneSpeedStatus based on Integer32"""
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
        *(("speed1000M", 3),
          ("speed100M", 2),
          ("speed10M", 1),
          ("unsupported", 4))
    )


_McbMCMediaOneSpeedStatus_Type.__name__ = "Integer32"
_McbMCMediaOneSpeedStatus_Object = MibTableColumn
mcbMCMediaOneSpeedStatus = _McbMCMediaOneSpeedStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 41, 1, 4, 2, 1, 10),
    _McbMCMediaOneSpeedStatus_Type()
)
mcbMCMediaOneSpeedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcbMCMediaOneSpeedStatus.setStatus("mandatory")


class _McbMCMediaTwoSpeedStatus_Type(Integer32):
    """Custom type mcbMCMediaTwoSpeedStatus based on Integer32"""
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
        *(("speed1000M", 3),
          ("speed100M", 2),
          ("speed10M", 1),
          ("unsupported", 4))
    )


_McbMCMediaTwoSpeedStatus_Type.__name__ = "Integer32"
_McbMCMediaTwoSpeedStatus_Object = MibTableColumn
mcbMCMediaTwoSpeedStatus = _McbMCMediaTwoSpeedStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 41, 1, 4, 2, 1, 11),
    _McbMCMediaTwoSpeedStatus_Type()
)
mcbMCMediaTwoSpeedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcbMCMediaTwoSpeedStatus.setStatus("mandatory")


class _McbMCSlotName_Type(DisplayString):
    """Custom type mcbMCSlotName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_McbMCSlotName_Type.__name__ = "DisplayString"
_McbMCSlotName_Object = MibTableColumn
mcbMCSlotName = _McbMCSlotName_Object(
    (1, 3, 6, 1, 4, 1, 171, 41, 1, 4, 2, 1, 12),
    _McbMCSlotName_Type()
)
mcbMCSlotName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcbMCSlotName.setStatus("mandatory")


class _McbMCEnable_Type(Integer32):
    """Custom type mcbMCEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("unsupported", 3))
    )


_McbMCEnable_Type.__name__ = "Integer32"
_McbMCEnable_Object = MibTableColumn
mcbMCEnable = _McbMCEnable_Object(
    (1, 3, 6, 1, 4, 1, 171, 41, 1, 4, 2, 1, 13),
    _McbMCEnable_Type()
)
mcbMCEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcbMCEnable.setStatus("mandatory")


class _McbMCSetLLCF_Type(Integer32):
    """Custom type mcbMCSetLLCF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("unsupported", 3))
    )


_McbMCSetLLCF_Type.__name__ = "Integer32"
_McbMCSetLLCF_Object = MibTableColumn
mcbMCSetLLCF = _McbMCSetLLCF_Object(
    (1, 3, 6, 1, 4, 1, 171, 41, 1, 4, 2, 1, 14),
    _McbMCSetLLCF_Type()
)
mcbMCSetLLCF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcbMCSetLLCF.setStatus("mandatory")


class _McbMCEnableMediaOne_Type(Integer32):
    """Custom type mcbMCEnableMediaOne based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("unsupported", 3))
    )


_McbMCEnableMediaOne_Type.__name__ = "Integer32"
_McbMCEnableMediaOne_Object = MibTableColumn
mcbMCEnableMediaOne = _McbMCEnableMediaOne_Object(
    (1, 3, 6, 1, 4, 1, 171, 41, 1, 4, 2, 1, 15),
    _McbMCEnableMediaOne_Type()
)
mcbMCEnableMediaOne.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcbMCEnableMediaOne.setStatus("mandatory")


class _McbMCEnableMediaTwo_Type(Integer32):
    """Custom type mcbMCEnableMediaTwo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("unsupported", 3))
    )


_McbMCEnableMediaTwo_Type.__name__ = "Integer32"
_McbMCEnableMediaTwo_Object = MibTableColumn
mcbMCEnableMediaTwo = _McbMCEnableMediaTwo_Object(
    (1, 3, 6, 1, 4, 1, 171, 41, 1, 4, 2, 1, 16),
    _McbMCEnableMediaTwo_Type()
)
mcbMCEnableMediaTwo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcbMCEnableMediaTwo.setStatus("mandatory")


class _McbMCSetMediaOneAutoNegotiate_Type(Integer32):
    """Custom type mcbMCSetMediaOneAutoNegotiate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto-negotiate", 1),
          ("force", 2),
          ("unsupported", 3))
    )


_McbMCSetMediaOneAutoNegotiate_Type.__name__ = "Integer32"
_McbMCSetMediaOneAutoNegotiate_Object = MibTableColumn
mcbMCSetMediaOneAutoNegotiate = _McbMCSetMediaOneAutoNegotiate_Object(
    (1, 3, 6, 1, 4, 1, 171, 41, 1, 4, 2, 1, 17),
    _McbMCSetMediaOneAutoNegotiate_Type()
)
mcbMCSetMediaOneAutoNegotiate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcbMCSetMediaOneAutoNegotiate.setStatus("mandatory")


class _McbMCSetMediaTwoAutoNegotiate_Type(Integer32):
    """Custom type mcbMCSetMediaTwoAutoNegotiate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto-negotiate", 1),
          ("force", 2),
          ("unsupported", 3))
    )


_McbMCSetMediaTwoAutoNegotiate_Type.__name__ = "Integer32"
_McbMCSetMediaTwoAutoNegotiate_Object = MibTableColumn
mcbMCSetMediaTwoAutoNegotiate = _McbMCSetMediaTwoAutoNegotiate_Object(
    (1, 3, 6, 1, 4, 1, 171, 41, 1, 4, 2, 1, 18),
    _McbMCSetMediaTwoAutoNegotiate_Type()
)
mcbMCSetMediaTwoAutoNegotiate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcbMCSetMediaTwoAutoNegotiate.setStatus("mandatory")


class _McbMCSetMediaOneSpeed_Type(Integer32):
    """Custom type mcbMCSetMediaOneSpeed based on Integer32"""
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
        *(("speed1000M", 3),
          ("speed100M", 2),
          ("speed10M", 1),
          ("unsupported", 4))
    )


_McbMCSetMediaOneSpeed_Type.__name__ = "Integer32"
_McbMCSetMediaOneSpeed_Object = MibTableColumn
mcbMCSetMediaOneSpeed = _McbMCSetMediaOneSpeed_Object(
    (1, 3, 6, 1, 4, 1, 171, 41, 1, 4, 2, 1, 19),
    _McbMCSetMediaOneSpeed_Type()
)
mcbMCSetMediaOneSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcbMCSetMediaOneSpeed.setStatus("mandatory")


class _McbMCSetMediaTwoSpeed_Type(Integer32):
    """Custom type mcbMCSetMediaTwoSpeed based on Integer32"""
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
        *(("speed1000M", 3),
          ("speed100M", 2),
          ("speed10M", 1),
          ("unsupported", 4))
    )


_McbMCSetMediaTwoSpeed_Type.__name__ = "Integer32"
_McbMCSetMediaTwoSpeed_Object = MibTableColumn
mcbMCSetMediaTwoSpeed = _McbMCSetMediaTwoSpeed_Object(
    (1, 3, 6, 1, 4, 1, 171, 41, 1, 4, 2, 1, 20),
    _McbMCSetMediaTwoSpeed_Type()
)
mcbMCSetMediaTwoSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcbMCSetMediaTwoSpeed.setStatus("mandatory")


class _McbMCSetMediaOneDuplex_Type(Integer32):
    """Custom type mcbMCSetMediaOneDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("full", 2),
          ("half", 1),
          ("unsupported", 3))
    )


_McbMCSetMediaOneDuplex_Type.__name__ = "Integer32"
_McbMCSetMediaOneDuplex_Object = MibTableColumn
mcbMCSetMediaOneDuplex = _McbMCSetMediaOneDuplex_Object(
    (1, 3, 6, 1, 4, 1, 171, 41, 1, 4, 2, 1, 21),
    _McbMCSetMediaOneDuplex_Type()
)
mcbMCSetMediaOneDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcbMCSetMediaOneDuplex.setStatus("mandatory")


class _McbMCSetMediaTwoDuplex_Type(Integer32):
    """Custom type mcbMCSetMediaTwoDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("full", 2),
          ("half", 1),
          ("unsupported", 3))
    )


_McbMCSetMediaTwoDuplex_Type.__name__ = "Integer32"
_McbMCSetMediaTwoDuplex_Object = MibTableColumn
mcbMCSetMediaTwoDuplex = _McbMCSetMediaTwoDuplex_Object(
    (1, 3, 6, 1, 4, 1, 171, 41, 1, 4, 2, 1, 22),
    _McbMCSetMediaTwoDuplex_Type()
)
mcbMCSetMediaTwoDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcbMCSetMediaTwoDuplex.setStatus("mandatory")


class _McbMCSetMediaOneFlowControl_Type(Integer32):
    """Custom type mcbMCSetMediaOneFlowControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("unsupported", 3))
    )


_McbMCSetMediaOneFlowControl_Type.__name__ = "Integer32"
_McbMCSetMediaOneFlowControl_Object = MibTableColumn
mcbMCSetMediaOneFlowControl = _McbMCSetMediaOneFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 171, 41, 1, 4, 2, 1, 23),
    _McbMCSetMediaOneFlowControl_Type()
)
mcbMCSetMediaOneFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcbMCSetMediaOneFlowControl.setStatus("mandatory")


class _McbMCSetMediaTwoFlowControl_Type(Integer32):
    """Custom type mcbMCSetMediaTwoFlowControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("unsupported", 3))
    )


_McbMCSetMediaTwoFlowControl_Type.__name__ = "Integer32"
_McbMCSetMediaTwoFlowControl_Object = MibTableColumn
mcbMCSetMediaTwoFlowControl = _McbMCSetMediaTwoFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 171, 41, 1, 4, 2, 1, 24),
    _McbMCSetMediaTwoFlowControl_Type()
)
mcbMCSetMediaTwoFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcbMCSetMediaTwoFlowControl.setStatus("mandatory")


class _McbMCSetMediaOneLLR_Type(Integer32):
    """Custom type mcbMCSetMediaOneLLR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("unsupported", 3))
    )


_McbMCSetMediaOneLLR_Type.__name__ = "Integer32"
_McbMCSetMediaOneLLR_Object = MibTableColumn
mcbMCSetMediaOneLLR = _McbMCSetMediaOneLLR_Object(
    (1, 3, 6, 1, 4, 1, 171, 41, 1, 4, 2, 1, 25),
    _McbMCSetMediaOneLLR_Type()
)
mcbMCSetMediaOneLLR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcbMCSetMediaOneLLR.setStatus("mandatory")


class _McbMCSetMediaTwoLLR_Type(Integer32):
    """Custom type mcbMCSetMediaTwoLLR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("unsupported", 3))
    )


_McbMCSetMediaTwoLLR_Type.__name__ = "Integer32"
_McbMCSetMediaTwoLLR_Object = MibTableColumn
mcbMCSetMediaTwoLLR = _McbMCSetMediaTwoLLR_Object(
    (1, 3, 6, 1, 4, 1, 171, 41, 1, 4, 2, 1, 26),
    _McbMCSetMediaTwoLLR_Type()
)
mcbMCSetMediaTwoLLR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcbMCSetMediaTwoLLR.setStatus("mandatory")


class _McbMCMediaOneBrokenStatus_Type(Integer32):
    """Custom type mcbMCMediaOneBrokenStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("broken", 2),
          ("unbroken", 1),
          ("unsupported", 3))
    )


_McbMCMediaOneBrokenStatus_Type.__name__ = "Integer32"
_McbMCMediaOneBrokenStatus_Object = MibTableColumn
mcbMCMediaOneBrokenStatus = _McbMCMediaOneBrokenStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 41, 1, 4, 2, 1, 27),
    _McbMCMediaOneBrokenStatus_Type()
)
mcbMCMediaOneBrokenStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcbMCMediaOneBrokenStatus.setStatus("mandatory")


class _McbMCMediaTwoBrokenStatus_Type(Integer32):
    """Custom type mcbMCMediaTwoBrokenStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("broken", 2),
          ("unbroken", 1),
          ("unsupported", 3))
    )


_McbMCMediaTwoBrokenStatus_Type.__name__ = "Integer32"
_McbMCMediaTwoBrokenStatus_Object = MibTableColumn
mcbMCMediaTwoBrokenStatus = _McbMCMediaTwoBrokenStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 41, 1, 4, 2, 1, 28),
    _McbMCMediaTwoBrokenStatus_Type()
)
mcbMCMediaTwoBrokenStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcbMCMediaTwoBrokenStatus.setStatus("mandatory")
_McbMCMediaOneTxPacketCount_Type = Counter32
_McbMCMediaOneTxPacketCount_Object = MibTableColumn
mcbMCMediaOneTxPacketCount = _McbMCMediaOneTxPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 41, 1, 4, 2, 1, 29),
    _McbMCMediaOneTxPacketCount_Type()
)
mcbMCMediaOneTxPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcbMCMediaOneTxPacketCount.setStatus("mandatory")
_McbMCMediaOneRxPacketCount_Type = Counter32
_McbMCMediaOneRxPacketCount_Object = MibTableColumn
mcbMCMediaOneRxPacketCount = _McbMCMediaOneRxPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 41, 1, 4, 2, 1, 30),
    _McbMCMediaOneRxPacketCount_Type()
)
mcbMCMediaOneRxPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcbMCMediaOneRxPacketCount.setStatus("mandatory")
_McbMCMediaTwoTxPacketCount_Type = Counter32
_McbMCMediaTwoTxPacketCount_Object = MibTableColumn
mcbMCMediaTwoTxPacketCount = _McbMCMediaTwoTxPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 41, 1, 4, 2, 1, 31),
    _McbMCMediaTwoTxPacketCount_Type()
)
mcbMCMediaTwoTxPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcbMCMediaTwoTxPacketCount.setStatus("mandatory")
_McbMCMediaTwoRxPacketCount_Type = Counter32
_McbMCMediaTwoRxPacketCount_Object = MibTableColumn
mcbMCMediaTwoRxPacketCount = _McbMCMediaTwoRxPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 41, 1, 4, 2, 1, 32),
    _McbMCMediaTwoRxPacketCount_Type()
)
mcbMCMediaTwoRxPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcbMCMediaTwoRxPacketCount.setStatus("mandatory")
_McbMCRedundantGroups_ObjectIdentity = ObjectIdentity
mcbMCRedundantGroups = _McbMCRedundantGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 41, 1, 5)
)
_McbMCRedundantGroupCount_Type = Integer32
_McbMCRedundantGroupCount_Object = MibScalar
mcbMCRedundantGroupCount = _McbMCRedundantGroupCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 41, 1, 5, 1),
    _McbMCRedundantGroupCount_Type()
)
mcbMCRedundantGroupCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcbMCRedundantGroupCount.setStatus("mandatory")
_McbMCRedundantGroupTable_Object = MibTable
mcbMCRedundantGroupTable = _McbMCRedundantGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 41, 1, 5, 2)
)
if mibBuilder.loadTexts:
    mcbMCRedundantGroupTable.setStatus("mandatory")
_McbMCRedundantGroupEntry_Object = MibTableRow
mcbMCRedundantGroupEntry = _McbMCRedundantGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 41, 1, 5, 2, 1)
)
mcbMCRedundantGroupEntry.setIndexNames(
    (0, "DLINK-MCB-MIB", "mcbMCRedundantGroupNo"),
)
if mibBuilder.loadTexts:
    mcbMCRedundantGroupEntry.setStatus("mandatory")
_McbMCRedundantGroupNo_Type = Integer32
_McbMCRedundantGroupNo_Object = MibTableColumn
mcbMCRedundantGroupNo = _McbMCRedundantGroupNo_Object(
    (1, 3, 6, 1, 4, 1, 171, 41, 1, 5, 2, 1, 1),
    _McbMCRedundantGroupNo_Type()
)
mcbMCRedundantGroupNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcbMCRedundantGroupNo.setStatus("mandatory")
_McbMCRedundantGroupPrimarySlot_Type = Integer32
_McbMCRedundantGroupPrimarySlot_Object = MibTableColumn
mcbMCRedundantGroupPrimarySlot = _McbMCRedundantGroupPrimarySlot_Object(
    (1, 3, 6, 1, 4, 1, 171, 41, 1, 5, 2, 1, 2),
    _McbMCRedundantGroupPrimarySlot_Type()
)
mcbMCRedundantGroupPrimarySlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcbMCRedundantGroupPrimarySlot.setStatus("mandatory")
_McbMCRedundantGroupSecondarySlot_Type = Integer32
_McbMCRedundantGroupSecondarySlot_Object = MibTableColumn
mcbMCRedundantGroupSecondarySlot = _McbMCRedundantGroupSecondarySlot_Object(
    (1, 3, 6, 1, 4, 1, 171, 41, 1, 5, 2, 1, 3),
    _McbMCRedundantGroupSecondarySlot_Type()
)
mcbMCRedundantGroupSecondarySlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcbMCRedundantGroupSecondarySlot.setStatus("mandatory")


class _McbMCRedundantGroupEnable_Type(Integer32):
    """Custom type mcbMCRedundantGroupEnable based on Integer32"""
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


_McbMCRedundantGroupEnable_Type.__name__ = "Integer32"
_McbMCRedundantGroupEnable_Object = MibTableColumn
mcbMCRedundantGroupEnable = _McbMCRedundantGroupEnable_Object(
    (1, 3, 6, 1, 4, 1, 171, 41, 1, 5, 2, 1, 4),
    _McbMCRedundantGroupEnable_Type()
)
mcbMCRedundantGroupEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcbMCRedundantGroupEnable.setStatus("mandatory")
_McbMCRedundantGroupActiveSlot_Type = Integer32
_McbMCRedundantGroupActiveSlot_Object = MibTableColumn
mcbMCRedundantGroupActiveSlot = _McbMCRedundantGroupActiveSlot_Object(
    (1, 3, 6, 1, 4, 1, 171, 41, 1, 5, 2, 1, 5),
    _McbMCRedundantGroupActiveSlot_Type()
)
mcbMCRedundantGroupActiveSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcbMCRedundantGroupActiveSlot.setStatus("mandatory")


class _McbMCRedundantGroupRestart_Type(Integer32):
    """Custom type mcbMCRedundantGroupRestart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("action", 1)
    )


_McbMCRedundantGroupRestart_Type.__name__ = "Integer32"
_McbMCRedundantGroupRestart_Object = MibTableColumn
mcbMCRedundantGroupRestart = _McbMCRedundantGroupRestart_Object(
    (1, 3, 6, 1, 4, 1, 171, 41, 1, 5, 2, 1, 6),
    _McbMCRedundantGroupRestart_Type()
)
mcbMCRedundantGroupRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcbMCRedundantGroupRestart.setStatus("mandatory")

# Managed Objects groups


# Notification objects

mcbPowerOneFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 41, 1, 0, 1)
)
if mibBuilder.loadTexts:
    mcbPowerOneFail.setStatus(
        ""
    )

mcbFanOneFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 41, 1, 0, 2)
)
if mibBuilder.loadTexts:
    mcbFanOneFail.setStatus(
        ""
    )

mcbPowerTwoFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 41, 1, 0, 3)
)
if mibBuilder.loadTexts:
    mcbPowerTwoFail.setStatus(
        ""
    )

mcbFanTwoFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 41, 1, 0, 4)
)
if mibBuilder.loadTexts:
    mcbFanTwoFail.setStatus(
        ""
    )

mcbMediaConverterPlugin = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 41, 1, 0, 5)
)
mcbMediaConverterPlugin.setObjects(
    ("DLINK-MCB-MIB", "mcbMCSlotNo")
)
if mibBuilder.loadTexts:
    mcbMediaConverterPlugin.setStatus(
        ""
    )

mcbMediaConverterPullout = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 41, 1, 0, 6)
)
mcbMediaConverterPullout.setObjects(
    ("DLINK-MCB-MIB", "mcbMCSlotNo")
)
if mibBuilder.loadTexts:
    mcbMediaConverterPullout.setStatus(
        ""
    )

mcbMCMediaOneLinkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 41, 1, 0, 7)
)
mcbMCMediaOneLinkDown.setObjects(
    ("DLINK-MCB-MIB", "mcbMCSlotNo")
)
if mibBuilder.loadTexts:
    mcbMCMediaOneLinkDown.setStatus(
        ""
    )

mcbMCMediaTwoLinkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 41, 1, 0, 8)
)
mcbMCMediaTwoLinkDown.setObjects(
    ("DLINK-MCB-MIB", "mcbMCSlotNo")
)
if mibBuilder.loadTexts:
    mcbMCMediaTwoLinkDown.setStatus(
        ""
    )

mcbMCMediaOneLinkUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 41, 1, 0, 9)
)
mcbMCMediaOneLinkUp.setObjects(
    ("DLINK-MCB-MIB", "mcbMCSlotNo")
)
if mibBuilder.loadTexts:
    mcbMCMediaOneLinkUp.setStatus(
        ""
    )

mcbMCMediaTwoLinkUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 41, 1, 0, 10)
)
mcbMCMediaTwoLinkUp.setObjects(
    ("DLINK-MCB-MIB", "mcbMCSlotNo")
)
if mibBuilder.loadTexts:
    mcbMCMediaTwoLinkUp.setStatus(
        ""
    )

mcbMCMediaOneBroken = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 41, 1, 0, 11)
)
mcbMCMediaOneBroken.setObjects(
    ("DLINK-MCB-MIB", "mcbMCSlotNo")
)
if mibBuilder.loadTexts:
    mcbMCMediaOneBroken.setStatus(
        ""
    )

mcbMCMediaTwoBroken = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 41, 1, 0, 12)
)
mcbMCMediaTwoBroken.setObjects(
    ("DLINK-MCB-MIB", "mcbMCSlotNo")
)
if mibBuilder.loadTexts:
    mcbMCMediaTwoBroken.setStatus(
        ""
    )

mcbMCActiveSlotChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 41, 1, 0, 13)
)
mcbMCActiveSlotChange.setObjects(
    ("DLINK-MCB-MIB", "mcbMCRedundantGroupNo")
)
if mibBuilder.loadTexts:
    mcbMCActiveSlotChange.setStatus(
        ""
    )

mcbMCActiveSlotLose = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 41, 1, 0, 14)
)
mcbMCActiveSlotLose.setObjects(
    ("DLINK-MCB-MIB", "mcbMCRedundantGroupNo")
)
if mibBuilder.loadTexts:
    mcbMCActiveSlotLose.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DLINK-MCB-MIB",
    **{"company": company,
       "mcbMediaConverterFamily": mcbMediaConverterFamily,
       "mcbMediaConverterChassis": mcbMediaConverterChassis,
       "mcbPowerOneFail": mcbPowerOneFail,
       "mcbFanOneFail": mcbFanOneFail,
       "mcbPowerTwoFail": mcbPowerTwoFail,
       "mcbFanTwoFail": mcbFanTwoFail,
       "mcbMediaConverterPlugin": mcbMediaConverterPlugin,
       "mcbMediaConverterPullout": mcbMediaConverterPullout,
       "mcbMCMediaOneLinkDown": mcbMCMediaOneLinkDown,
       "mcbMCMediaTwoLinkDown": mcbMCMediaTwoLinkDown,
       "mcbMCMediaOneLinkUp": mcbMCMediaOneLinkUp,
       "mcbMCMediaTwoLinkUp": mcbMCMediaTwoLinkUp,
       "mcbMCMediaOneBroken": mcbMCMediaOneBroken,
       "mcbMCMediaTwoBroken": mcbMCMediaTwoBroken,
       "mcbMCActiveSlotChange": mcbMCActiveSlotChange,
       "mcbMCActiveSlotLose": mcbMCActiveSlotLose,
       "mcbSNMPMIB": mcbSNMPMIB,
       "mcbSNMPTrapPowerFail": mcbSNMPTrapPowerFail,
       "mcbSNMPTrapFanFail": mcbSNMPTrapFanFail,
       "mcbSNMPTrapMCPlugin": mcbSNMPTrapMCPlugin,
       "mcbSNMPTrapMCPullout": mcbSNMPTrapMCPullout,
       "mcbSNMPTrapMCLinkDown": mcbSNMPTrapMCLinkDown,
       "mcbSNMPTrapMCLinkUp": mcbSNMPTrapMCLinkUp,
       "mcbSNMPTrapMCLinkBroken": mcbSNMPTrapMCLinkBroken,
       "mcbSNMPTrapMCActiveSlotChange": mcbSNMPTrapMCActiveSlotChange,
       "mcbSNMPTrapMCActiveSlotLose": mcbSNMPTrapMCActiveSlotLose,
       "mcbAdministrator": mcbAdministrator,
       "mcbAdministratorHardwareRev": mcbAdministratorHardwareRev,
       "mcbAdministratorSoftwareRev": mcbAdministratorSoftwareRev,
       "mcbAdministratorBiosRev": mcbAdministratorBiosRev,
       "mcbAdministratorFactoryReset": mcbAdministratorFactoryReset,
       "mcbAdministratorFactoryResetCPU": mcbAdministratorFactoryResetCPU,
       "mcbAdministratorSoftwareReboot": mcbAdministratorSoftwareReboot,
       "mcbMCFrame": mcbMCFrame,
       "mcbFramePowerOneOnStatus": mcbFramePowerOneOnStatus,
       "mcbFramePowerTwoOnStatus": mcbFramePowerTwoOnStatus,
       "mcbFramePowerOneFailStatus": mcbFramePowerOneFailStatus,
       "mcbFramePowerTwoFailStatus": mcbFramePowerTwoFailStatus,
       "mcbFrameFanOneFailStatus": mcbFrameFanOneFailStatus,
       "mcbFrameFanTwoFailStatus": mcbFrameFanTwoFailStatus,
       "mcbMCSlots": mcbMCSlots,
       "mcbMCSlotCount": mcbMCSlotCount,
       "mcbMCSlotTable": mcbMCSlotTable,
       "mcbMCSlotEntry": mcbMCSlotEntry,
       "mcbMCSlotNo": mcbMCSlotNo,
       "mcbMCSlotExist": mcbMCSlotExist,
       "mcbMCModelName": mcbMCModelName,
       "mcbMCMediaOneType": mcbMCMediaOneType,
       "mcbMCMediaTwoType": mcbMCMediaTwoType,
       "mcbMCMediaOneLinkStatus": mcbMCMediaOneLinkStatus,
       "mcbMCMediaTwoLinkStatus": mcbMCMediaTwoLinkStatus,
       "mcbMCMediaOneDupStatus": mcbMCMediaOneDupStatus,
       "mcbMCMediaTwoDupStatus": mcbMCMediaTwoDupStatus,
       "mcbMCMediaOneSpeedStatus": mcbMCMediaOneSpeedStatus,
       "mcbMCMediaTwoSpeedStatus": mcbMCMediaTwoSpeedStatus,
       "mcbMCSlotName": mcbMCSlotName,
       "mcbMCEnable": mcbMCEnable,
       "mcbMCSetLLCF": mcbMCSetLLCF,
       "mcbMCEnableMediaOne": mcbMCEnableMediaOne,
       "mcbMCEnableMediaTwo": mcbMCEnableMediaTwo,
       "mcbMCSetMediaOneAutoNegotiate": mcbMCSetMediaOneAutoNegotiate,
       "mcbMCSetMediaTwoAutoNegotiate": mcbMCSetMediaTwoAutoNegotiate,
       "mcbMCSetMediaOneSpeed": mcbMCSetMediaOneSpeed,
       "mcbMCSetMediaTwoSpeed": mcbMCSetMediaTwoSpeed,
       "mcbMCSetMediaOneDuplex": mcbMCSetMediaOneDuplex,
       "mcbMCSetMediaTwoDuplex": mcbMCSetMediaTwoDuplex,
       "mcbMCSetMediaOneFlowControl": mcbMCSetMediaOneFlowControl,
       "mcbMCSetMediaTwoFlowControl": mcbMCSetMediaTwoFlowControl,
       "mcbMCSetMediaOneLLR": mcbMCSetMediaOneLLR,
       "mcbMCSetMediaTwoLLR": mcbMCSetMediaTwoLLR,
       "mcbMCMediaOneBrokenStatus": mcbMCMediaOneBrokenStatus,
       "mcbMCMediaTwoBrokenStatus": mcbMCMediaTwoBrokenStatus,
       "mcbMCMediaOneTxPacketCount": mcbMCMediaOneTxPacketCount,
       "mcbMCMediaOneRxPacketCount": mcbMCMediaOneRxPacketCount,
       "mcbMCMediaTwoTxPacketCount": mcbMCMediaTwoTxPacketCount,
       "mcbMCMediaTwoRxPacketCount": mcbMCMediaTwoRxPacketCount,
       "mcbMCRedundantGroups": mcbMCRedundantGroups,
       "mcbMCRedundantGroupCount": mcbMCRedundantGroupCount,
       "mcbMCRedundantGroupTable": mcbMCRedundantGroupTable,
       "mcbMCRedundantGroupEntry": mcbMCRedundantGroupEntry,
       "mcbMCRedundantGroupNo": mcbMCRedundantGroupNo,
       "mcbMCRedundantGroupPrimarySlot": mcbMCRedundantGroupPrimarySlot,
       "mcbMCRedundantGroupSecondarySlot": mcbMCRedundantGroupSecondarySlot,
       "mcbMCRedundantGroupEnable": mcbMCRedundantGroupEnable,
       "mcbMCRedundantGroupActiveSlot": mcbMCRedundantGroupActiveSlot,
       "mcbMCRedundantGroupRestart": mcbMCRedundantGroupRestart}
)
