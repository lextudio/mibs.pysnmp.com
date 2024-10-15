# SNMP MIB module (ERI-DNX-NEST-SYS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ERI-DNX-NEST-SYS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:40:25 2024
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

(DecisionType,
 NestSlotAddress,
 UnsignedInt,
 database,
 devices,
 dnx,
 dnxTrapEnterprise,
 sysMgr,
 trapSequence) = mibBuilder.importSymbols(
    "ERI-DNX-SMC-MIB",
    "DecisionType",
    "NestSlotAddress",
    "UnsignedInt",
    "database",
    "devices",
    "dnx",
    "dnxTrapEnterprise",
    "sysMgr",
    "trapSequence")

(eriMibs,) = mibBuilder.importSymbols(
    "ERI-ROOT-SMI",
    "eriMibs")

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

eriDNXNestSysMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 644, 3, 14)
)
eriDNXNestSysMIB.setRevisions(
        ("2003-07-17 00:00",
         "2002-05-13 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class DnxSlotDeviceType(Integer32, TextualConvention):
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
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              25,
              26,
              27,
              28,
              29,
              30,
              31)
        )
    )
    namedValues = NamedValues(
        *(("ds0dp", 25),
          ("ds3", 7),
          ("e3", 28),
          ("gr303", 19),
          ("hds3", 18),
          ("oc3", 27),
          ("oc3X", 31),
          ("octal-t1e1", 1),
          ("octalHighSpeed", 3),
          ("octalVoice", 9),
          ("powerSupply", 14),
          ("psx", 15),
          ("quad-t1", 6),
          ("quadHighSpeed", 2),
          ("quadOcu", 4),
          ("router", 16),
          ("slot", 0),
          ("smc", 5),
          ("stm1", 26),
          ("stm1X", 30),
          ("sts1", 17),
          ("testAccess", 8),
          ("xcc", 20),
          ("xlc", 21),
          ("xlc-ot1e1", 29),
          ("xnm", 22))
    )



class DnxSlotDeviceState(Integer32, TextualConvention):
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
        *(("busError", 6),
          ("configError", 8),
          ("defective", 5),
          ("disabled", 3),
          ("not-present", 0),
          ("offline", 2),
          ("online", 1),
          ("online-busError", 15),
          ("online-cfgError", 23),
          ("online-defective", 14),
          ("online-offline", 12),
          ("online-online", 11),
          ("online-oos", 16),
          ("online-standby", 13),
          ("outOfService", 7),
          ("standby", 4),
          ("standby-busError", 21),
          ("standby-cfgError", 24),
          ("standby-defective", 20),
          ("standby-offline", 18),
          ("standby-online", 17),
          ("standby-oos", 22),
          ("standby-standby", 19))
    )



# MIB Managed Objects in the order of their OIDs

_SlotConfigTable_Object = MibTable
slotConfigTable = _SlotConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 3)
)
if mibBuilder.loadTexts:
    slotConfigTable.setStatus("current")
_SlotConfigEntry_Object = MibTableRow
slotConfigEntry = _SlotConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 3, 1)
)
slotConfigEntry.setIndexNames(
    (0, "ERI-DNX-NEST-SYS-MIB", "slotNbr"),
)
if mibBuilder.loadTexts:
    slotConfigEntry.setStatus("current")


class _SlotNbr_Type(Integer32):
    """Custom type slotNbr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_SlotNbr_Type.__name__ = "Integer32"
_SlotNbr_Object = MibTableColumn
slotNbr = _SlotNbr_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 3, 1, 1),
    _SlotNbr_Type()
)
slotNbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotNbr.setStatus("current")
_SlotConfigDeviceType_Type = DnxSlotDeviceType
_SlotConfigDeviceType_Object = MibTableColumn
slotConfigDeviceType = _SlotConfigDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 3, 1, 2),
    _SlotConfigDeviceType_Type()
)
slotConfigDeviceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slotConfigDeviceType.setStatus("current")
_SlotActualDeviceType_Type = DnxSlotDeviceType
_SlotActualDeviceType_Object = MibTableColumn
slotActualDeviceType = _SlotActualDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 3, 1, 3),
    _SlotActualDeviceType_Type()
)
slotActualDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotActualDeviceType.setStatus("current")
_SlotDeviceState_Type = DnxSlotDeviceState
_SlotDeviceState_Object = MibTableColumn
slotDeviceState = _SlotDeviceState_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 3, 1, 4),
    _SlotDeviceState_Type()
)
slotDeviceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotDeviceState.setStatus("current")


class _SlotAlarmLevel_Type(Integer32):
    """Custom type slotAlarmLevel based on Integer32"""
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
              99)
        )
    )
    namedValues = NamedValues(
        *(("critical-level", 4),
          ("critical-major", 6),
          ("critical-major-minor", 7),
          ("critical-minor", 5),
          ("major-level", 2),
          ("major-minor", 3),
          ("minor-level", 1),
          ("no-alarm", 0),
          ("unknown", 99))
    )


_SlotAlarmLevel_Type.__name__ = "Integer32"
_SlotAlarmLevel_Object = MibTableColumn
slotAlarmLevel = _SlotAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 3, 1, 5),
    _SlotAlarmLevel_Type()
)
slotAlarmLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotAlarmLevel.setStatus("current")


class _SlotDeviceName_Type(DisplayString):
    """Custom type slotDeviceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 11),
    )


_SlotDeviceName_Type.__name__ = "DisplayString"
_SlotDeviceName_Object = MibTableColumn
slotDeviceName = _SlotDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 3, 1, 6),
    _SlotDeviceName_Type()
)
slotDeviceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slotDeviceName.setStatus("current")


class _SlotDeviceVersion_Type(DisplayString):
    """Custom type slotDeviceVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_SlotDeviceVersion_Type.__name__ = "DisplayString"
_SlotDeviceVersion_Object = MibTableColumn
slotDeviceVersion = _SlotDeviceVersion_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 3, 1, 7),
    _SlotDeviceVersion_Type()
)
slotDeviceVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotDeviceVersion.setStatus("current")


class _SlotDeviceRedundancy_Type(Integer32):
    """Custom type slotDeviceRedundancy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1),
          ("notApplicable", 2))
    )


_SlotDeviceRedundancy_Type.__name__ = "Integer32"
_SlotDeviceRedundancy_Object = MibTableColumn
slotDeviceRedundancy = _SlotDeviceRedundancy_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 3, 1, 8),
    _SlotDeviceRedundancy_Type()
)
slotDeviceRedundancy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slotDeviceRedundancy.setStatus("current")


class _SlotMiscState_Type(Integer32):
    """Custom type slotMiscState based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("clockSrc", 4),
          ("errors", 1),
          ("errors-clockSrc", 5),
          ("errors-test", 3),
          ("errors-test-clockSrc", 7),
          ("none", 0),
          ("test", 2),
          ("test-clockSrc", 6))
    )


_SlotMiscState_Type.__name__ = "Integer32"
_SlotMiscState_Object = MibTableColumn
slotMiscState = _SlotMiscState_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 3, 1, 9),
    _SlotMiscState_Type()
)
slotMiscState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotMiscState.setStatus("current")


class _SlotConfigCmdStatus_Type(Integer32):
    """Custom type slotConfigCmdStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              10,
              11,
              101,
              102,
              110,
              111,
              200,
              201,
              202,
              203,
              204,
              205,
              207,
              208,
              450,
              500,
              501,
              502)
        )
    )
    namedValues = NamedValues(
        *(("delete-slot-config", 2),
          ("delete-successful", 102),
          ("err-cannot-chg-sys-device", 205),
          ("err-cannot-delete-online-device", 208),
          ("err-data-locked-by-another-user", 450),
          ("err-general-slot-config-error", 200),
          ("err-invalid-redundancy-state", 207),
          ("err-invalid-slot-command", 202),
          ("err-invalid-slot-name", 203),
          ("err-invalid-slot-type", 201),
          ("err-invalid-snmp-type", 501),
          ("err-invalid-snmp-var-size", 502),
          ("err-redundancy-disabled", 204),
          ("err-snmp-parse-failed", 500),
          ("ndr-restore", 11),
          ("ndr-switchover", 10),
          ("ready-for-command", 0),
          ("restore-successful", 111),
          ("switch-successful", 110),
          ("update-slot-config", 1),
          ("update-successful", 101))
    )


_SlotConfigCmdStatus_Type.__name__ = "Integer32"
_SlotConfigCmdStatus_Object = MibTableColumn
slotConfigCmdStatus = _SlotConfigCmdStatus_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 3, 1, 10),
    _SlotConfigCmdStatus_Type()
)
slotConfigCmdStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slotConfigCmdStatus.setStatus("current")
_NumberSlots_Type = Integer32
_NumberSlots_Object = MibScalar
numberSlots = _NumberSlots_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 4),
    _NumberSlots_Type()
)
numberSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numberSlots.setStatus("obsolete")
_SoftwareRelease_Type = DisplayString
_SoftwareRelease_Object = MibScalar
softwareRelease = _SoftwareRelease_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 5),
    _SoftwareRelease_Type()
)
softwareRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softwareRelease.setStatus("obsolete")
_Redundancy_ObjectIdentity = ObjectIdentity
redundancy = _Redundancy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 9)
)
_NdrEnabled_Type = DecisionType
_NdrEnabled_Object = MibScalar
ndrEnabled = _NdrEnabled_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 9, 1),
    _NdrEnabled_Type()
)
ndrEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ndrEnabled.setStatus("current")


class _NdrState_Type(Integer32):
    """Custom type ndrState based on Integer32"""
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
        *(("delayed", 3),
          ("disabled", 1),
          ("enabled", 4),
          ("frozen", 2))
    )


_NdrState_Type.__name__ = "Integer32"
_NdrState_Object = MibScalar
ndrState = _NdrState_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 9, 2),
    _NdrState_Type()
)
ndrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ndrState.setStatus("current")


class _NdrAutoSwitchover_Type(Integer32):
    """Custom type ndrAutoSwitchover based on Integer32"""
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
        *(("automatic", 1),
          ("broadband-1-auto", 3),
          ("broadband-2-auto", 4),
          ("manual", 0),
          ("narrowband-auto", 2))
    )


_NdrAutoSwitchover_Type.__name__ = "Integer32"
_NdrAutoSwitchover_Object = MibScalar
ndrAutoSwitchover = _NdrAutoSwitchover_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 9, 3),
    _NdrAutoSwitchover_Type()
)
ndrAutoSwitchover.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ndrAutoSwitchover.setStatus("current")


class _NdrAutoRestore_Type(Integer32):
    """Custom type ndrAutoRestore based on Integer32"""
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
        *(("automatic", 1),
          ("broadband-1-auto", 3),
          ("broadband-2-auto", 4),
          ("manual", 0),
          ("narrowband-auto", 2))
    )


_NdrAutoRestore_Type.__name__ = "Integer32"
_NdrAutoRestore_Object = MibScalar
ndrAutoRestore = _NdrAutoRestore_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 9, 4),
    _NdrAutoRestore_Type()
)
ndrAutoRestore.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ndrAutoRestore.setStatus("current")
_NdrBroadbandGroup1_Type = Integer32
_NdrBroadbandGroup1_Object = MibScalar
ndrBroadbandGroup1 = _NdrBroadbandGroup1_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 9, 5),
    _NdrBroadbandGroup1_Type()
)
ndrBroadbandGroup1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ndrBroadbandGroup1.setStatus("current")
_NdrNarrowbandGroup_Type = Integer32
_NdrNarrowbandGroup_Object = MibScalar
ndrNarrowbandGroup = _NdrNarrowbandGroup_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 9, 6),
    _NdrNarrowbandGroup_Type()
)
ndrNarrowbandGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ndrNarrowbandGroup.setStatus("current")


class _NdrBroadbandGroup1Protected_Type(Integer32):
    """Custom type ndrBroadbandGroup1Protected based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(8, 10),
    )


_NdrBroadbandGroup1Protected_Type.__name__ = "Integer32"
_NdrBroadbandGroup1Protected_Object = MibScalar
ndrBroadbandGroup1Protected = _NdrBroadbandGroup1Protected_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 9, 7),
    _NdrBroadbandGroup1Protected_Type()
)
ndrBroadbandGroup1Protected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ndrBroadbandGroup1Protected.setStatus("current")


class _NdrNarrowbandProtected_Type(Integer32):
    """Custom type ndrNarrowbandProtected based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2, 11),
    )


_NdrNarrowbandProtected_Type.__name__ = "Integer32"
_NdrNarrowbandProtected_Object = MibScalar
ndrNarrowbandProtected = _NdrNarrowbandProtected_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 9, 8),
    _NdrNarrowbandProtected_Type()
)
ndrNarrowbandProtected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ndrNarrowbandProtected.setStatus("current")


class _NdrBroadbandGroup1Type_Type(Integer32):
    """Custom type ndrBroadbandGroup1Type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(8,
              18,
              21,
              31)
        )
    )
    namedValues = NamedValues(
        *(("ds3", 8),
          ("e3", 31),
          ("hds3", 21),
          ("sts1", 18))
    )


_NdrBroadbandGroup1Type_Type.__name__ = "Integer32"
_NdrBroadbandGroup1Type_Object = MibScalar
ndrBroadbandGroup1Type = _NdrBroadbandGroup1Type_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 9, 9),
    _NdrBroadbandGroup1Type_Type()
)
ndrBroadbandGroup1Type.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ndrBroadbandGroup1Type.setStatus("current")


class _NdrNarrowbandType_Type(Integer32):
    """Custom type ndrNarrowbandType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(13,
              22)
        )
    )
    namedValues = NamedValues(
        *(("gr303", 22),
          ("octalT1E1", 13))
    )


_NdrNarrowbandType_Type.__name__ = "Integer32"
_NdrNarrowbandType_Object = MibScalar
ndrNarrowbandType = _NdrNarrowbandType_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 9, 10),
    _NdrNarrowbandType_Type()
)
ndrNarrowbandType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ndrNarrowbandType.setStatus("current")
_NdrDualBroadbandEnabled_Type = DecisionType
_NdrDualBroadbandEnabled_Object = MibScalar
ndrDualBroadbandEnabled = _NdrDualBroadbandEnabled_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 9, 11),
    _NdrDualBroadbandEnabled_Type()
)
ndrDualBroadbandEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ndrDualBroadbandEnabled.setStatus("current")
_NdrBroadbandGroup2_Type = Integer32
_NdrBroadbandGroup2_Object = MibScalar
ndrBroadbandGroup2 = _NdrBroadbandGroup2_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 9, 12),
    _NdrBroadbandGroup2_Type()
)
ndrBroadbandGroup2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ndrBroadbandGroup2.setStatus("current")


class _NdrBroadbandGroup2Protected_Type(Integer32):
    """Custom type ndrBroadbandGroup2Protected based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
    )


_NdrBroadbandGroup2Protected_Type.__name__ = "Integer32"
_NdrBroadbandGroup2Protected_Object = MibScalar
ndrBroadbandGroup2Protected = _NdrBroadbandGroup2Protected_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 9, 13),
    _NdrBroadbandGroup2Protected_Type()
)
ndrBroadbandGroup2Protected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ndrBroadbandGroup2Protected.setStatus("current")


class _NdrBroadbandGroup2Type_Type(Integer32):
    """Custom type ndrBroadbandGroup2Type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(8,
              18,
              21,
              31)
        )
    )
    namedValues = NamedValues(
        *(("ds3", 8),
          ("e3", 31),
          ("hds3", 21),
          ("sts1", 18))
    )


_NdrBroadbandGroup2Type_Type.__name__ = "Integer32"
_NdrBroadbandGroup2Type_Object = MibScalar
ndrBroadbandGroup2Type = _NdrBroadbandGroup2Type_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 9, 14),
    _NdrBroadbandGroup2Type_Type()
)
ndrBroadbandGroup2Type.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ndrBroadbandGroup2Type.setStatus("current")


class _NdrPsxChassisType_Type(Integer32):
    """Custom type ndrPsxChassisType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("psx5200", 0),
          ("psx5300", 1))
    )


_NdrPsxChassisType_Type.__name__ = "Integer32"
_NdrPsxChassisType_Object = MibScalar
ndrPsxChassisType = _NdrPsxChassisType_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 9, 15),
    _NdrPsxChassisType_Type()
)
ndrPsxChassisType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ndrPsxChassisType.setStatus("current")
_UpgradeSw_ObjectIdentity = ObjectIdentity
upgradeSw = _UpgradeSw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 10)
)
_DevDownloadTable_Object = MibTable
devDownloadTable = _DevDownloadTable_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 10, 1)
)
if mibBuilder.loadTexts:
    devDownloadTable.setStatus("current")
_DevDownloadEntry_Object = MibTableRow
devDownloadEntry = _DevDownloadEntry_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 10, 1, 1)
)
devDownloadEntry.setIndexNames(
    (0, "ERI-DNX-NEST-SYS-MIB", "programFileIndex"),
)
if mibBuilder.loadTexts:
    devDownloadEntry.setStatus("current")


class _ProgramFileIndex_Type(Integer32):
    """Custom type programFileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_ProgramFileIndex_Type.__name__ = "Integer32"
_ProgramFileIndex_Object = MibTableColumn
programFileIndex = _ProgramFileIndex_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 10, 1, 1, 1),
    _ProgramFileIndex_Type()
)
programFileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    programFileIndex.setStatus("current")
_ProgramFileName_Type = DisplayString
_ProgramFileName_Object = MibTableColumn
programFileName = _ProgramFileName_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 10, 1, 1, 2),
    _ProgramFileName_Type()
)
programFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    programFileName.setStatus("current")
_ProgramFileSize_Type = Integer32
_ProgramFileSize_Object = MibTableColumn
programFileSize = _ProgramFileSize_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 10, 1, 1, 3),
    _ProgramFileSize_Type()
)
programFileSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    programFileSize.setStatus("current")


class _ProgramLoadStatus_Type(Integer32):
    """Custom type programLoadStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("loadingProgramFile", 1),
          ("readyForProgramLoad", 2),
          ("swDownloadNotReady", 3))
    )


_ProgramLoadStatus_Type.__name__ = "Integer32"
_ProgramLoadStatus_Object = MibTableColumn
programLoadStatus = _ProgramLoadStatus_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 10, 1, 1, 4),
    _ProgramLoadStatus_Type()
)
programLoadStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    programLoadStatus.setStatus("current")
_ProgramLoadInitiator_Type = DisplayString
_ProgramLoadInitiator_Object = MibTableColumn
programLoadInitiator = _ProgramLoadInitiator_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 10, 1, 1, 5),
    _ProgramLoadInitiator_Type()
)
programLoadInitiator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    programLoadInitiator.setStatus("current")
_ProgramBytesSent_Type = Integer32
_ProgramBytesSent_Object = MibTableColumn
programBytesSent = _ProgramBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 10, 1, 1, 6),
    _ProgramBytesSent_Type()
)
programBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    programBytesSent.setStatus("current")
_ProgramSlotNumber_Type = Integer32
_ProgramSlotNumber_Object = MibTableColumn
programSlotNumber = _ProgramSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 10, 1, 1, 7),
    _ProgramSlotNumber_Type()
)
programSlotNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    programSlotNumber.setStatus("current")


class _ProgramFileCommand_Type(Integer32):
    """Custom type programFileCommand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              12,
              13,
              414,
              450,
              500,
              501,
              502)
        )
    )
    namedValues = NamedValues(
        *(("deleteProgramFile", 4),
          ("err-data-locked-by-another-user", 450),
          ("err-invalid-command", 414),
          ("err-invalid-nest-nbr", 13),
          ("err-invalid-slot-nbr", 6),
          ("err-invalid-snmp-type", 501),
          ("err-invalid-snmp-var-size", 502),
          ("err-snmp-parse-failed", 500),
          ("loadProgramFile", 1),
          ("loadProgramToAll", 2),
          ("noError", 9),
          ("noProgramFile", 7),
          ("programFileBusy", 8),
          ("programFileIdle", 12),
          ("readyForCommand", 5),
          ("slotNotReady", 10))
    )


_ProgramFileCommand_Type.__name__ = "Integer32"
_ProgramFileCommand_Object = MibTableColumn
programFileCommand = _ProgramFileCommand_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 10, 1, 1, 8),
    _ProgramFileCommand_Type()
)
programFileCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    programFileCommand.setStatus("current")


class _ProgramNestNumber_Type(Integer32):
    """Custom type programNestNumber based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("allNests", 10),
          ("nest1", 0),
          ("nest2", 1),
          ("nest3", 2),
          ("nest4", 3),
          ("nest5", 4),
          ("nest6", 5),
          ("nest7", 6),
          ("nest8", 7))
    )


_ProgramNestNumber_Type.__name__ = "Integer32"
_ProgramNestNumber_Object = MibTableColumn
programNestNumber = _ProgramNestNumber_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 10, 1, 1, 9),
    _ProgramNestNumber_Type()
)
programNestNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    programNestNumber.setStatus("current")
_EXpansionNestAdmin_ObjectIdentity = ObjectIdentity
eXpansionNestAdmin = _EXpansionNestAdmin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 11)
)
_XNestCfgTable_Object = MibTable
xNestCfgTable = _XNestCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 11, 1)
)
if mibBuilder.loadTexts:
    xNestCfgTable.setStatus("current")
_XNestCfgEntry_Object = MibTableRow
xNestCfgEntry = _XNestCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 11, 1, 1)
)
xNestCfgEntry.setIndexNames(
    (0, "ERI-DNX-NEST-SYS-MIB", "xNestIndex"),
)
if mibBuilder.loadTexts:
    xNestCfgEntry.setStatus("current")


class _XNestIndex_Type(Integer32):
    """Custom type xNestIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_XNestIndex_Type.__name__ = "Integer32"
_XNestIndex_Object = MibTableColumn
xNestIndex = _XNestIndex_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 11, 1, 1, 1),
    _XNestIndex_Type()
)
xNestIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xNestIndex.setStatus("current")


class _XNestUnitName_Type(DisplayString):
    """Custom type xNestUnitName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_XNestUnitName_Type.__name__ = "DisplayString"
_XNestUnitName_Object = MibTableColumn
xNestUnitName = _XNestUnitName_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 11, 1, 1, 2),
    _XNestUnitName_Type()
)
xNestUnitName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xNestUnitName.setStatus("current")


class _XNestType_Type(Integer32):
    """Custom type xNestType based on Integer32"""
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
        *(("dnx11", 2),
          ("dnx4", 1),
          ("notConfig", 0),
          ("stm1X-oc3X", 3))
    )


_XNestType_Type.__name__ = "Integer32"
_XNestType_Object = MibTableColumn
xNestType = _XNestType_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 11, 1, 1, 3),
    _XNestType_Type()
)
xNestType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xNestType.setStatus("current")


class _XNestState_Type(Integer32):
    """Custom type xNestState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              8,
              12,
              16,
              32)
        )
    )
    namedValues = NamedValues(
        *(("mismatch", 2),
          ("missing", 12),
          ("notPresent", 8),
          ("offline", 32),
          ("online", 16))
    )


_XNestState_Type.__name__ = "Integer32"
_XNestState_Object = MibTableColumn
xNestState = _XNestState_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 11, 1, 1, 4),
    _XNestState_Type()
)
xNestState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xNestState.setStatus("current")


class _XNestAlarmStatus_Type(Integer32):
    """Custom type xNestAlarmStatus based on Integer32"""
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
              99)
        )
    )
    namedValues = NamedValues(
        *(("critical-level", 4),
          ("critical-major", 6),
          ("critical-major-minor", 7),
          ("critical-minor", 5),
          ("major-level", 2),
          ("major-minor", 3),
          ("minor-level", 1),
          ("no-alarm", 0),
          ("unknown", 99))
    )


_XNestAlarmStatus_Type.__name__ = "Integer32"
_XNestAlarmStatus_Object = MibTableColumn
xNestAlarmStatus = _XNestAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 11, 1, 1, 5),
    _XNestAlarmStatus_Type()
)
xNestAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xNestAlarmStatus.setStatus("current")


class _XNestDeviceCards_Type(Integer32):
    """Custom type xNestDeviceCards based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 11),
    )


_XNestDeviceCards_Type.__name__ = "Integer32"
_XNestDeviceCards_Object = MibTableColumn
xNestDeviceCards = _XNestDeviceCards_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 11, 1, 1, 6),
    _XNestDeviceCards_Type()
)
xNestDeviceCards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xNestDeviceCards.setStatus("current")
_XNestNDRCapable_Type = DecisionType
_XNestNDRCapable_Object = MibTableColumn
xNestNDRCapable = _XNestNDRCapable_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 11, 1, 1, 7),
    _XNestNDRCapable_Type()
)
xNestNDRCapable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xNestNDRCapable.setStatus("current")


class _XNestAlarmContacts_Type(Integer32):
    """Custom type xNestAlarmContacts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("localAudio1", 1),
          ("localAudio2", 2),
          ("standard", 0))
    )


_XNestAlarmContacts_Type.__name__ = "Integer32"
_XNestAlarmContacts_Object = MibTableColumn
xNestAlarmContacts = _XNestAlarmContacts_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 11, 1, 1, 8),
    _XNestAlarmContacts_Type()
)
xNestAlarmContacts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xNestAlarmContacts.setStatus("current")
_XNestDualSMCs_Type = DecisionType
_XNestDualSMCs_Object = MibTableColumn
xNestDualSMCs = _XNestDualSMCs_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 11, 1, 1, 9),
    _XNestDualSMCs_Type()
)
xNestDualSMCs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xNestDualSMCs.setStatus("current")
_XNestDualXccXlc_Type = DecisionType
_XNestDualXccXlc_Object = MibTableColumn
xNestDualXccXlc = _XNestDualXccXlc_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 11, 1, 1, 10),
    _XNestDualXccXlc_Type()
)
xNestDualXccXlc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xNestDualXccXlc.setStatus("current")


class _XNestCmdStatus_Type(Integer32):
    """Custom type xNestCmdStatus based on Integer32"""
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
              101,
              102,
              103,
              104,
              105,
              106,
              107,
              200,
              201,
              202,
              203,
              204,
              205,
              206,
              207,
              208,
              450,
              500,
              501,
              502)
        )
    )
    namedValues = NamedValues(
        *(("clear-device-errors", 5),
          ("clear-successful", 105),
          ("delete-nest-config", 2),
          ("delete-successful", 102),
          ("err-cannot-delete-online-nest", 207),
          ("err-data-locked-by-another-user", 450),
          ("err-general-nest-config-error", 200),
          ("err-invalid-nest-alrm", 204),
          ("err-invalid-nest-command", 202),
          ("err-invalid-nest-name", 203),
          ("err-invalid-nest-ndr", 205),
          ("err-invalid-nest-option", 206),
          ("err-invalid-nest-type", 201),
          ("err-invalid-snmp-type", 501),
          ("err-invalid-snmp-var-size", 502),
          ("err-nest-not-present", 208),
          ("err-snmp-parse-failed", 500),
          ("ready-for-command", 0),
          ("reset-device-cards", 4),
          ("reset-successful", 104),
          ("switch-mgr-cards", 3),
          ("switch-mgr-successful", 103),
          ("switch-xcc-cards", 6),
          ("switch-xcc-successful", 106),
          ("switch-xlink-cards", 7),
          ("switch-xlink-successful", 107),
          ("update-nest-config", 1),
          ("update-successful", 101))
    )


_XNestCmdStatus_Type.__name__ = "Integer32"
_XNestCmdStatus_Object = MibTableColumn
xNestCmdStatus = _XNestCmdStatus_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 11, 1, 1, 11),
    _XNestCmdStatus_Type()
)
xNestCmdStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xNestCmdStatus.setStatus("current")
_XNestDualPower_Type = DecisionType
_XNestDualPower_Object = MibTableColumn
xNestDualPower = _XNestDualPower_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 11, 1, 1, 12),
    _XNestDualPower_Type()
)
xNestDualPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xNestDualPower.setStatus("current")
_XSlotTable_Object = MibTable
xSlotTable = _XSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 11, 2)
)
if mibBuilder.loadTexts:
    xSlotTable.setStatus("current")
_XSlotEntry_Object = MibTableRow
xSlotEntry = _XSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 11, 2, 1)
)
xSlotEntry.setIndexNames(
    (0, "ERI-DNX-NEST-SYS-MIB", "xSlotNestAddr"),
)
if mibBuilder.loadTexts:
    xSlotEntry.setStatus("current")
_XSlotNestAddr_Type = NestSlotAddress
_XSlotNestAddr_Object = MibTableColumn
xSlotNestAddr = _XSlotNestAddr_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 11, 2, 1, 1),
    _XSlotNestAddr_Type()
)
xSlotNestAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xSlotNestAddr.setStatus("current")
_XSlotDeviceType_Type = DnxSlotDeviceType
_XSlotDeviceType_Object = MibTableColumn
xSlotDeviceType = _XSlotDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 11, 2, 1, 2),
    _XSlotDeviceType_Type()
)
xSlotDeviceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xSlotDeviceType.setStatus("current")
_XSlotActualDeviceType_Type = DnxSlotDeviceType
_XSlotActualDeviceType_Object = MibTableColumn
xSlotActualDeviceType = _XSlotActualDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 11, 2, 1, 3),
    _XSlotActualDeviceType_Type()
)
xSlotActualDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xSlotActualDeviceType.setStatus("current")
_XSlotDeviceState_Type = DnxSlotDeviceState
_XSlotDeviceState_Object = MibTableColumn
xSlotDeviceState = _XSlotDeviceState_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 11, 2, 1, 4),
    _XSlotDeviceState_Type()
)
xSlotDeviceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xSlotDeviceState.setStatus("current")


class _XSlotAlarmLevel_Type(Integer32):
    """Custom type xSlotAlarmLevel based on Integer32"""
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
              99)
        )
    )
    namedValues = NamedValues(
        *(("critical-level", 4),
          ("critical-major", 6),
          ("critical-major-minor", 7),
          ("critical-minor", 5),
          ("major-level", 2),
          ("major-minor", 3),
          ("minor-level", 1),
          ("no-alarm", 0),
          ("unknown", 99))
    )


_XSlotAlarmLevel_Type.__name__ = "Integer32"
_XSlotAlarmLevel_Object = MibTableColumn
xSlotAlarmLevel = _XSlotAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 11, 2, 1, 5),
    _XSlotAlarmLevel_Type()
)
xSlotAlarmLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xSlotAlarmLevel.setStatus("current")


class _XSlotDeviceName_Type(DisplayString):
    """Custom type xSlotDeviceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 11),
    )


_XSlotDeviceName_Type.__name__ = "DisplayString"
_XSlotDeviceName_Object = MibTableColumn
xSlotDeviceName = _XSlotDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 11, 2, 1, 6),
    _XSlotDeviceName_Type()
)
xSlotDeviceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xSlotDeviceName.setStatus("current")


class _XSlotDeviceVersion_Type(DisplayString):
    """Custom type xSlotDeviceVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_XSlotDeviceVersion_Type.__name__ = "DisplayString"
_XSlotDeviceVersion_Object = MibTableColumn
xSlotDeviceVersion = _XSlotDeviceVersion_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 11, 2, 1, 7),
    _XSlotDeviceVersion_Type()
)
xSlotDeviceVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xSlotDeviceVersion.setStatus("current")


class _XSlotDeviceRedundancy_Type(Integer32):
    """Custom type xSlotDeviceRedundancy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1),
          ("notApplicable", 2))
    )


_XSlotDeviceRedundancy_Type.__name__ = "Integer32"
_XSlotDeviceRedundancy_Object = MibTableColumn
xSlotDeviceRedundancy = _XSlotDeviceRedundancy_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 11, 2, 1, 8),
    _XSlotDeviceRedundancy_Type()
)
xSlotDeviceRedundancy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xSlotDeviceRedundancy.setStatus("current")


class _XSlotMiscState_Type(Integer32):
    """Custom type xSlotMiscState based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("clockSrc", 4),
          ("errors", 1),
          ("errors-clockSrc", 5),
          ("errors-test", 3),
          ("errors-test-clockSrc", 7),
          ("none", 0),
          ("test", 2),
          ("test-clockSrc", 6))
    )


_XSlotMiscState_Type.__name__ = "Integer32"
_XSlotMiscState_Object = MibTableColumn
xSlotMiscState = _XSlotMiscState_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 11, 2, 1, 9),
    _XSlotMiscState_Type()
)
xSlotMiscState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xSlotMiscState.setStatus("current")


class _XSlotCmdStatus_Type(Integer32):
    """Custom type xSlotCmdStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              10,
              11,
              101,
              102,
              110,
              111,
              200,
              201,
              202,
              203,
              204,
              205,
              207,
              208,
              450,
              500,
              501,
              502)
        )
    )
    namedValues = NamedValues(
        *(("delete-slot-config", 2),
          ("delete-successful", 102),
          ("err-cannot-chg-sys-device", 205),
          ("err-cannot-delete-online-device", 208),
          ("err-data-locked-by-another-user", 450),
          ("err-general-slot-config-error", 200),
          ("err-invalid-redundancy-state", 207),
          ("err-invalid-slot-command", 202),
          ("err-invalid-slot-name", 203),
          ("err-invalid-slot-type", 201),
          ("err-invalid-snmp-type", 501),
          ("err-invalid-snmp-var-size", 502),
          ("err-redundancy-disabled", 204),
          ("err-snmp-parse-failed", 500),
          ("ndr-restore", 11),
          ("ndr-switchover", 10),
          ("ready-for-command", 0),
          ("restore-successful", 111),
          ("switch-successful", 110),
          ("update-slot-config", 1),
          ("update-successful", 101))
    )


_XSlotCmdStatus_Type.__name__ = "Integer32"
_XSlotCmdStatus_Object = MibTableColumn
xSlotCmdStatus = _XSlotCmdStatus_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 11, 2, 1, 10),
    _XSlotCmdStatus_Type()
)
xSlotCmdStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xSlotCmdStatus.setStatus("current")
_XSlotRawDeviceState_Type = UnsignedInt
_XSlotRawDeviceState_Object = MibTableColumn
xSlotRawDeviceState = _XSlotRawDeviceState_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 11, 2, 1, 11),
    _XSlotRawDeviceState_Type()
)
xSlotRawDeviceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xSlotRawDeviceState.setStatus("current")
_XNdrTable_Object = MibTable
xNdrTable = _XNdrTable_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 11, 3)
)
if mibBuilder.loadTexts:
    xNdrTable.setStatus("current")
_XNdrEntry_Object = MibTableRow
xNdrEntry = _XNdrEntry_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 11, 3, 1)
)
xNdrEntry.setIndexNames(
    (0, "ERI-DNX-NEST-SYS-MIB", "xNdrNestIndex"),
)
if mibBuilder.loadTexts:
    xNdrEntry.setStatus("current")


class _XNdrNestIndex_Type(Integer32):
    """Custom type xNdrNestIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_XNdrNestIndex_Type.__name__ = "Integer32"
_XNdrNestIndex_Object = MibTableColumn
xNdrNestIndex = _XNdrNestIndex_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 11, 3, 1, 1),
    _XNdrNestIndex_Type()
)
xNdrNestIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xNdrNestIndex.setStatus("current")


class _XNdrState_Type(Integer32):
    """Custom type xNdrState based on Integer32"""
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
        *(("delayed", 3),
          ("disabled", 1),
          ("enabled", 4),
          ("frozen", 2))
    )


_XNdrState_Type.__name__ = "Integer32"
_XNdrState_Object = MibTableColumn
xNdrState = _XNdrState_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 11, 3, 1, 2),
    _XNdrState_Type()
)
xNdrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xNdrState.setStatus("current")


class _XNdrAutoSwitchover_Type(Integer32):
    """Custom type xNdrAutoSwitchover based on Integer32"""
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
        *(("automatic", 1),
          ("broadband-1-auto", 3),
          ("broadband-2-auto", 4),
          ("manual", 0),
          ("narrowband-auto", 2))
    )


_XNdrAutoSwitchover_Type.__name__ = "Integer32"
_XNdrAutoSwitchover_Object = MibTableColumn
xNdrAutoSwitchover = _XNdrAutoSwitchover_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 11, 3, 1, 3),
    _XNdrAutoSwitchover_Type()
)
xNdrAutoSwitchover.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xNdrAutoSwitchover.setStatus("current")


class _XNdrAutoRestore_Type(Integer32):
    """Custom type xNdrAutoRestore based on Integer32"""
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
        *(("automatic", 1),
          ("broadband-1-auto", 3),
          ("broadband-2-auto", 4),
          ("manual", 0),
          ("narrowband-auto", 2))
    )


_XNdrAutoRestore_Type.__name__ = "Integer32"
_XNdrAutoRestore_Object = MibTableColumn
xNdrAutoRestore = _XNdrAutoRestore_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 11, 3, 1, 4),
    _XNdrAutoRestore_Type()
)
xNdrAutoRestore.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xNdrAutoRestore.setStatus("current")
_XNdrBroadbandGroup1_Type = Integer32
_XNdrBroadbandGroup1_Object = MibTableColumn
xNdrBroadbandGroup1 = _XNdrBroadbandGroup1_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 11, 3, 1, 5),
    _XNdrBroadbandGroup1_Type()
)
xNdrBroadbandGroup1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xNdrBroadbandGroup1.setStatus("current")
_XNdrNarrowbandGroup_Type = Integer32
_XNdrNarrowbandGroup_Object = MibTableColumn
xNdrNarrowbandGroup = _XNdrNarrowbandGroup_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 11, 3, 1, 6),
    _XNdrNarrowbandGroup_Type()
)
xNdrNarrowbandGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xNdrNarrowbandGroup.setStatus("current")


class _XNdrBroadbandGroup1Protected_Type(Integer32):
    """Custom type xNdrBroadbandGroup1Protected based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(8, 10),
    )


_XNdrBroadbandGroup1Protected_Type.__name__ = "Integer32"
_XNdrBroadbandGroup1Protected_Object = MibTableColumn
xNdrBroadbandGroup1Protected = _XNdrBroadbandGroup1Protected_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 11, 3, 1, 7),
    _XNdrBroadbandGroup1Protected_Type()
)
xNdrBroadbandGroup1Protected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xNdrBroadbandGroup1Protected.setStatus("current")


class _XNdrNarrowbandProtected_Type(Integer32):
    """Custom type xNdrNarrowbandProtected based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2, 11),
    )


_XNdrNarrowbandProtected_Type.__name__ = "Integer32"
_XNdrNarrowbandProtected_Object = MibTableColumn
xNdrNarrowbandProtected = _XNdrNarrowbandProtected_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 11, 3, 1, 8),
    _XNdrNarrowbandProtected_Type()
)
xNdrNarrowbandProtected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xNdrNarrowbandProtected.setStatus("current")


class _XNdrBroadbandGroup1Type_Type(Integer32):
    """Custom type xNdrBroadbandGroup1Type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(8,
              18,
              21,
              31)
        )
    )
    namedValues = NamedValues(
        *(("ds3", 8),
          ("e3", 31),
          ("hds3", 21),
          ("sts1", 18))
    )


_XNdrBroadbandGroup1Type_Type.__name__ = "Integer32"
_XNdrBroadbandGroup1Type_Object = MibTableColumn
xNdrBroadbandGroup1Type = _XNdrBroadbandGroup1Type_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 11, 3, 1, 9),
    _XNdrBroadbandGroup1Type_Type()
)
xNdrBroadbandGroup1Type.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xNdrBroadbandGroup1Type.setStatus("current")


class _XNdrNarrowbandType_Type(Integer32):
    """Custom type xNdrNarrowbandType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(13,
              22)
        )
    )
    namedValues = NamedValues(
        *(("gr303", 22),
          ("octalT1E1", 13))
    )


_XNdrNarrowbandType_Type.__name__ = "Integer32"
_XNdrNarrowbandType_Object = MibTableColumn
xNdrNarrowbandType = _XNdrNarrowbandType_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 11, 3, 1, 10),
    _XNdrNarrowbandType_Type()
)
xNdrNarrowbandType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xNdrNarrowbandType.setStatus("current")
_XNdrDualBroadbandEnabled_Type = DecisionType
_XNdrDualBroadbandEnabled_Object = MibTableColumn
xNdrDualBroadbandEnabled = _XNdrDualBroadbandEnabled_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 11, 3, 1, 11),
    _XNdrDualBroadbandEnabled_Type()
)
xNdrDualBroadbandEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xNdrDualBroadbandEnabled.setStatus("current")
_XNdrBroadbandGroup2_Type = Integer32
_XNdrBroadbandGroup2_Object = MibTableColumn
xNdrBroadbandGroup2 = _XNdrBroadbandGroup2_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 11, 3, 1, 12),
    _XNdrBroadbandGroup2_Type()
)
xNdrBroadbandGroup2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xNdrBroadbandGroup2.setStatus("current")


class _XNdrBroadbandGroup2Protected_Type(Integer32):
    """Custom type xNdrBroadbandGroup2Protected based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
    )


_XNdrBroadbandGroup2Protected_Type.__name__ = "Integer32"
_XNdrBroadbandGroup2Protected_Object = MibTableColumn
xNdrBroadbandGroup2Protected = _XNdrBroadbandGroup2Protected_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 11, 3, 1, 13),
    _XNdrBroadbandGroup2Protected_Type()
)
xNdrBroadbandGroup2Protected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xNdrBroadbandGroup2Protected.setStatus("current")


class _XNdrBroadbandGroup2Type_Type(Integer32):
    """Custom type xNdrBroadbandGroup2Type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(8,
              18,
              21,
              31)
        )
    )
    namedValues = NamedValues(
        *(("ds3", 8),
          ("e3", 31),
          ("hds3", 21),
          ("sts1", 18))
    )


_XNdrBroadbandGroup2Type_Type.__name__ = "Integer32"
_XNdrBroadbandGroup2Type_Object = MibTableColumn
xNdrBroadbandGroup2Type = _XNdrBroadbandGroup2Type_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 11, 3, 1, 14),
    _XNdrBroadbandGroup2Type_Type()
)
xNdrBroadbandGroup2Type.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xNdrBroadbandGroup2Type.setStatus("current")


class _XNdrPsxChassisType_Type(Integer32):
    """Custom type xNdrPsxChassisType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("psx5200", 0),
          ("psx5300", 1))
    )


_XNdrPsxChassisType_Type.__name__ = "Integer32"
_XNdrPsxChassisType_Object = MibTableColumn
xNdrPsxChassisType = _XNdrPsxChassisType_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 11, 3, 1, 15),
    _XNdrPsxChassisType_Type()
)
xNdrPsxChassisType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xNdrPsxChassisType.setStatus("current")


class _XNdrCmdStatus_Type(Integer32):
    """Custom type xNdrCmdStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              101,
              200,
              201,
              202,
              203,
              204,
              205,
              206,
              450,
              500,
              501,
              502)
        )
    )
    namedValues = NamedValues(
        *(("err-data-locked-by-another-user", 450),
          ("err-general-ndr-config-error", 200),
          ("err-invalid-ndr-autoswitch", 203),
          ("err-invalid-ndr-chassis", 204),
          ("err-invalid-ndr-command", 202),
          ("err-invalid-ndr-dual-bb", 205),
          ("err-invalid-ndr-dual-psx", 206),
          ("err-invalid-ndr-group-type", 201),
          ("err-invalid-snmp-type", 501),
          ("err-invalid-snmp-var-size", 502),
          ("err-snmp-parse-failed", 500),
          ("ready-for-command", 0),
          ("update-ndr", 1),
          ("update-successful", 101))
    )


_XNdrCmdStatus_Type.__name__ = "Integer32"
_XNdrCmdStatus_Object = MibTableColumn
xNdrCmdStatus = _XNdrCmdStatus_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 11, 3, 1, 16),
    _XNdrCmdStatus_Type()
)
xNdrCmdStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xNdrCmdStatus.setStatus("current")
_XNdrDualPowerSupply_Type = DecisionType
_XNdrDualPowerSupply_Object = MibTableColumn
xNdrDualPowerSupply = _XNdrDualPowerSupply_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 11, 3, 1, 17),
    _XNdrDualPowerSupply_Type()
)
xNdrDualPowerSupply.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xNdrDualPowerSupply.setStatus("current")
_DbSyncronize_ObjectIdentity = ObjectIdentity
dbSyncronize = _DbSyncronize_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 12, 1, 2)
)
_DbAutoSyncMode_Type = DecisionType
_DbAutoSyncMode_Object = MibScalar
dbAutoSyncMode = _DbAutoSyncMode_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 12, 1, 2, 1),
    _DbAutoSyncMode_Type()
)
dbAutoSyncMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dbAutoSyncMode.setStatus("current")


class _DbSyncStatus_Type(Integer32):
    """Custom type dbSyncStatus based on Integer32"""
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
        *(("autoSyncOff", 4),
          ("inSync", 1),
          ("notInSync", 2),
          ("standByNotPresent", 5),
          ("syncInProgress", 3))
    )


_DbSyncStatus_Type.__name__ = "Integer32"
_DbSyncStatus_Object = MibScalar
dbSyncStatus = _DbSyncStatus_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 12, 1, 2, 2),
    _DbSyncStatus_Type()
)
dbSyncStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dbSyncStatus.setStatus("current")
_DbSyncProgressTime_Type = Unsigned32
_DbSyncProgressTime_Object = MibScalar
dbSyncProgressTime = _DbSyncProgressTime_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 12, 1, 2, 3),
    _DbSyncProgressTime_Type()
)
dbSyncProgressTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dbSyncProgressTime.setStatus("current")


class _DbSyncCmdStatus_Type(Integer32):
    """Custom type dbSyncCmdStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              101,
              102,
              120,
              200,
              201,
              202,
              203,
              204,
              450,
              500,
              501,
              502)
        )
    )
    namedValues = NamedValues(
        *(("err-data-locked-by-another-user", 450),
          ("err-dbsync-failed", 202),
          ("err-gen-dbsync-cfg-error", 200),
          ("err-invalid-dbsync-command", 203),
          ("err-invalid-dbsync-mode", 204),
          ("err-invalid-snmp-type", 501),
          ("err-invalid-snmp-var-size", 502),
          ("err-snmp-parse-failed", 500),
          ("err-standby-not-present", 201),
          ("ready-for-command", 0),
          ("startDBSync", 2),
          ("sync-completed-successful", 120),
          ("sync-start-successful", 102),
          ("update", 1),
          ("update-successful", 101))
    )


_DbSyncCmdStatus_Type.__name__ = "Integer32"
_DbSyncCmdStatus_Object = MibScalar
dbSyncCmdStatus = _DbSyncCmdStatus_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 12, 1, 2, 4),
    _DbSyncCmdStatus_Type()
)
dbSyncCmdStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dbSyncCmdStatus.setStatus("current")
_DeviceAboutTable_Object = MibTable
deviceAboutTable = _DeviceAboutTable_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 225)
)
if mibBuilder.loadTexts:
    deviceAboutTable.setStatus("current")
_DeviceAboutEntry_Object = MibTableRow
deviceAboutEntry = _DeviceAboutEntry_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 225, 1)
)
deviceAboutEntry.setIndexNames(
    (0, "ERI-DNX-NEST-SYS-MIB", "devCardAddress"),
)
if mibBuilder.loadTexts:
    deviceAboutEntry.setStatus("current")
_DevCardAddress_Type = NestSlotAddress
_DevCardAddress_Object = MibTableColumn
devCardAddress = _DevCardAddress_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 225, 1, 1),
    _DevCardAddress_Type()
)
devCardAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devCardAddress.setStatus("current")
_DevSwReleaseDate_Type = DisplayString
_DevSwReleaseDate_Object = MibTableColumn
devSwReleaseDate = _DevSwReleaseDate_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 225, 1, 2),
    _DevSwReleaseDate_Type()
)
devSwReleaseDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devSwReleaseDate.setStatus("current")
_DevSwChecksum_Type = DisplayString
_DevSwChecksum_Object = MibTableColumn
devSwChecksum = _DevSwChecksum_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 225, 1, 3),
    _DevSwChecksum_Type()
)
devSwChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devSwChecksum.setStatus("current")
_DevFrontCardType_Type = DisplayString
_DevFrontCardType_Object = MibTableColumn
devFrontCardType = _DevFrontCardType_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 225, 1, 4),
    _DevFrontCardType_Type()
)
devFrontCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devFrontCardType.setStatus("current")
_DevFrontCardRev_Type = Integer32
_DevFrontCardRev_Object = MibTableColumn
devFrontCardRev = _DevFrontCardRev_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 225, 1, 5),
    _DevFrontCardRev_Type()
)
devFrontCardRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devFrontCardRev.setStatus("current")
_DevXilinxVersion_Type = DisplayString
_DevXilinxVersion_Object = MibTableColumn
devXilinxVersion = _DevXilinxVersion_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 225, 1, 6),
    _DevXilinxVersion_Type()
)
devXilinxVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devXilinxVersion.setStatus("current")
_DevRearCardType_Type = DisplayString
_DevRearCardType_Object = MibTableColumn
devRearCardType = _DevRearCardType_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 225, 1, 7),
    _DevRearCardType_Type()
)
devRearCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devRearCardType.setStatus("current")
_DevRearCardRev_Type = Integer32
_DevRearCardRev_Object = MibTableColumn
devRearCardRev = _DevRearCardRev_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 225, 1, 8),
    _DevRearCardRev_Type()
)
devRearCardRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devRearCardRev.setStatus("current")


class _DevSwVersion_Type(DisplayString):
    """Custom type devSwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_DevSwVersion_Type.__name__ = "DisplayString"
_DevSwVersion_Object = MibTableColumn
devSwVersion = _DevSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 225, 1, 9),
    _DevSwVersion_Type()
)
devSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devSwVersion.setStatus("current")

# Managed Objects groups


# Notification objects

slotConfigTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 5)
)
slotConfigTrap.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-NEST-SYS-MIB", "slotNbr"),
        ("ERI-DNX-NEST-SYS-MIB", "slotConfigCmdStatus"),
        ("ERI-DNX-NEST-SYS-MIB", "xNestIndex"))
)
if mibBuilder.loadTexts:
    slotConfigTrap.setStatus(
        "current"
    )

ndrGroupStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 8)
)
ndrGroupStatusTrap.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-NEST-SYS-MIB", "ndrState"),
        ("ERI-DNX-NEST-SYS-MIB", "ndrBroadbandGroup1"),
        ("ERI-DNX-NEST-SYS-MIB", "ndrNarrowbandGroup"),
        ("ERI-DNX-NEST-SYS-MIB", "ndrBroadbandGroup2"),
        ("ERI-DNX-NEST-SYS-MIB", "xNdrNestIndex"))
)
if mibBuilder.loadTexts:
    ndrGroupStatusTrap.setStatus(
        "current"
    )

nestConfigTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 9)
)
nestConfigTrap.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-NEST-SYS-MIB", "xNestIndex"),
        ("ERI-DNX-NEST-SYS-MIB", "xNestType"),
        ("ERI-DNX-NEST-SYS-MIB", "xNestCmdStatus"),
        ("ERI-DNX-NEST-SYS-MIB", "xNestUnitName"))
)
if mibBuilder.loadTexts:
    nestConfigTrap.setStatus(
        "current"
    )

dbSyncProgressTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 12)
)
dbSyncProgressTrap.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-NEST-SYS-MIB", "dbSyncStatus"),
        ("ERI-DNX-NEST-SYS-MIB", "dbSyncCmdStatus"))
)
if mibBuilder.loadTexts:
    dbSyncProgressTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ERI-DNX-NEST-SYS-MIB",
    **{"DnxSlotDeviceType": DnxSlotDeviceType,
       "DnxSlotDeviceState": DnxSlotDeviceState,
       "slotConfigTrap": slotConfigTrap,
       "ndrGroupStatusTrap": ndrGroupStatusTrap,
       "nestConfigTrap": nestConfigTrap,
       "dbSyncProgressTrap": dbSyncProgressTrap,
       "slotConfigTable": slotConfigTable,
       "slotConfigEntry": slotConfigEntry,
       "slotNbr": slotNbr,
       "slotConfigDeviceType": slotConfigDeviceType,
       "slotActualDeviceType": slotActualDeviceType,
       "slotDeviceState": slotDeviceState,
       "slotAlarmLevel": slotAlarmLevel,
       "slotDeviceName": slotDeviceName,
       "slotDeviceVersion": slotDeviceVersion,
       "slotDeviceRedundancy": slotDeviceRedundancy,
       "slotMiscState": slotMiscState,
       "slotConfigCmdStatus": slotConfigCmdStatus,
       "numberSlots": numberSlots,
       "softwareRelease": softwareRelease,
       "redundancy": redundancy,
       "ndrEnabled": ndrEnabled,
       "ndrState": ndrState,
       "ndrAutoSwitchover": ndrAutoSwitchover,
       "ndrAutoRestore": ndrAutoRestore,
       "ndrBroadbandGroup1": ndrBroadbandGroup1,
       "ndrNarrowbandGroup": ndrNarrowbandGroup,
       "ndrBroadbandGroup1Protected": ndrBroadbandGroup1Protected,
       "ndrNarrowbandProtected": ndrNarrowbandProtected,
       "ndrBroadbandGroup1Type": ndrBroadbandGroup1Type,
       "ndrNarrowbandType": ndrNarrowbandType,
       "ndrDualBroadbandEnabled": ndrDualBroadbandEnabled,
       "ndrBroadbandGroup2": ndrBroadbandGroup2,
       "ndrBroadbandGroup2Protected": ndrBroadbandGroup2Protected,
       "ndrBroadbandGroup2Type": ndrBroadbandGroup2Type,
       "ndrPsxChassisType": ndrPsxChassisType,
       "upgradeSw": upgradeSw,
       "devDownloadTable": devDownloadTable,
       "devDownloadEntry": devDownloadEntry,
       "programFileIndex": programFileIndex,
       "programFileName": programFileName,
       "programFileSize": programFileSize,
       "programLoadStatus": programLoadStatus,
       "programLoadInitiator": programLoadInitiator,
       "programBytesSent": programBytesSent,
       "programSlotNumber": programSlotNumber,
       "programFileCommand": programFileCommand,
       "programNestNumber": programNestNumber,
       "eXpansionNestAdmin": eXpansionNestAdmin,
       "xNestCfgTable": xNestCfgTable,
       "xNestCfgEntry": xNestCfgEntry,
       "xNestIndex": xNestIndex,
       "xNestUnitName": xNestUnitName,
       "xNestType": xNestType,
       "xNestState": xNestState,
       "xNestAlarmStatus": xNestAlarmStatus,
       "xNestDeviceCards": xNestDeviceCards,
       "xNestNDRCapable": xNestNDRCapable,
       "xNestAlarmContacts": xNestAlarmContacts,
       "xNestDualSMCs": xNestDualSMCs,
       "xNestDualXccXlc": xNestDualXccXlc,
       "xNestCmdStatus": xNestCmdStatus,
       "xNestDualPower": xNestDualPower,
       "xSlotTable": xSlotTable,
       "xSlotEntry": xSlotEntry,
       "xSlotNestAddr": xSlotNestAddr,
       "xSlotDeviceType": xSlotDeviceType,
       "xSlotActualDeviceType": xSlotActualDeviceType,
       "xSlotDeviceState": xSlotDeviceState,
       "xSlotAlarmLevel": xSlotAlarmLevel,
       "xSlotDeviceName": xSlotDeviceName,
       "xSlotDeviceVersion": xSlotDeviceVersion,
       "xSlotDeviceRedundancy": xSlotDeviceRedundancy,
       "xSlotMiscState": xSlotMiscState,
       "xSlotCmdStatus": xSlotCmdStatus,
       "xSlotRawDeviceState": xSlotRawDeviceState,
       "xNdrTable": xNdrTable,
       "xNdrEntry": xNdrEntry,
       "xNdrNestIndex": xNdrNestIndex,
       "xNdrState": xNdrState,
       "xNdrAutoSwitchover": xNdrAutoSwitchover,
       "xNdrAutoRestore": xNdrAutoRestore,
       "xNdrBroadbandGroup1": xNdrBroadbandGroup1,
       "xNdrNarrowbandGroup": xNdrNarrowbandGroup,
       "xNdrBroadbandGroup1Protected": xNdrBroadbandGroup1Protected,
       "xNdrNarrowbandProtected": xNdrNarrowbandProtected,
       "xNdrBroadbandGroup1Type": xNdrBroadbandGroup1Type,
       "xNdrNarrowbandType": xNdrNarrowbandType,
       "xNdrDualBroadbandEnabled": xNdrDualBroadbandEnabled,
       "xNdrBroadbandGroup2": xNdrBroadbandGroup2,
       "xNdrBroadbandGroup2Protected": xNdrBroadbandGroup2Protected,
       "xNdrBroadbandGroup2Type": xNdrBroadbandGroup2Type,
       "xNdrPsxChassisType": xNdrPsxChassisType,
       "xNdrCmdStatus": xNdrCmdStatus,
       "xNdrDualPowerSupply": xNdrDualPowerSupply,
       "dbSyncronize": dbSyncronize,
       "dbAutoSyncMode": dbAutoSyncMode,
       "dbSyncStatus": dbSyncStatus,
       "dbSyncProgressTime": dbSyncProgressTime,
       "dbSyncCmdStatus": dbSyncCmdStatus,
       "deviceAboutTable": deviceAboutTable,
       "deviceAboutEntry": deviceAboutEntry,
       "devCardAddress": devCardAddress,
       "devSwReleaseDate": devSwReleaseDate,
       "devSwChecksum": devSwChecksum,
       "devFrontCardType": devFrontCardType,
       "devFrontCardRev": devFrontCardRev,
       "devXilinxVersion": devXilinxVersion,
       "devRearCardType": devRearCardType,
       "devRearCardRev": devRearCardRev,
       "devSwVersion": devSwVersion,
       "eriDNXNestSysMIB": eriDNXNestSysMIB}
)
