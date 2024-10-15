# SNMP MIB module (LANPLEX-MIB-1-2-9) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/LANPLEX-MIB-1-2-9
# Produced by pysmi-1.5.4 at Mon Oct 14 22:17:17 2024
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

_Synernetics_ObjectIdentity = ObjectIdentity
synernetics = _Synernetics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114)
)
_Lanplex_ObjectIdentity = ObjectIdentity
lanplex = _Lanplex_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1)
)
_LanplexMib_ObjectIdentity = ObjectIdentity
lanplexMib = _LanplexMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 1)
)
_Chassis_ObjectIdentity = ObjectIdentity
chassis = _Chassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 1)
)
_ChassisId_Type = Integer32
_ChassisId_Object = MibScalar
chassisId = _ChassisId_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 1, 1),
    _ChassisId_Type()
)
chassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisId.setStatus("deprecated")


class _ChassisType_Type(Integer32):
    """Custom type chassisType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fourSlot", 3),
          ("other", 1),
          ("tweleveSlot", 2))
    )


_ChassisType_Type.__name__ = "Integer32"
_ChassisType_Object = MibScalar
chassisType = _ChassisType_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 1, 2),
    _ChassisType_Type()
)
chassisType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisType.setStatus("deprecated")


class _ChassisRevision_Type(OctetString):
    """Custom type chassisRevision based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_ChassisRevision_Type.__name__ = "OctetString"
_ChassisRevision_Object = MibScalar
chassisRevision = _ChassisRevision_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 1, 3),
    _ChassisRevision_Type()
)
chassisRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisRevision.setStatus("deprecated")


class _ChassisName_Type(DisplayString):
    """Custom type chassisName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_ChassisName_Type.__name__ = "DisplayString"
_ChassisName_Object = MibScalar
chassisName = _ChassisName_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 1, 4),
    _ChassisName_Type()
)
chassisName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisName.setStatus("deprecated")


class _ChassisNameAbbrev_Type(DisplayString):
    """Custom type chassisNameAbbrev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_ChassisNameAbbrev_Type.__name__ = "DisplayString"
_ChassisNameAbbrev_Object = MibScalar
chassisNameAbbrev = _ChassisNameAbbrev_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 1, 5),
    _ChassisNameAbbrev_Type()
)
chassisNameAbbrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisNameAbbrev.setStatus("deprecated")


class _ChassisManufacturer_Type(DisplayString):
    """Custom type chassisManufacturer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_ChassisManufacturer_Type.__name__ = "DisplayString"
_ChassisManufacturer_Object = MibScalar
chassisManufacturer = _ChassisManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 1, 6),
    _ChassisManufacturer_Type()
)
chassisManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisManufacturer.setStatus("deprecated")
_ChassisSlotCount_Type = Integer32
_ChassisSlotCount_Object = MibScalar
chassisSlotCount = _ChassisSlotCount_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 1, 7),
    _ChassisSlotCount_Type()
)
chassisSlotCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisSlotCount.setStatus("deprecated")


class _ChassisBuildTime_Type(DisplayString):
    """Custom type chassisBuildTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_ChassisBuildTime_Type.__name__ = "DisplayString"
_ChassisBuildTime_Object = MibScalar
chassisBuildTime = _ChassisBuildTime_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 1, 8),
    _ChassisBuildTime_Type()
)
chassisBuildTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisBuildTime.setStatus("deprecated")


class _ChassisSoftwareRevision_Type(OctetString):
    """Custom type chassisSoftwareRevision based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_ChassisSoftwareRevision_Type.__name__ = "OctetString"
_ChassisSoftwareRevision_Object = MibScalar
chassisSoftwareRevision = _ChassisSoftwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 1, 9),
    _ChassisSoftwareRevision_Type()
)
chassisSoftwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisSoftwareRevision.setStatus("deprecated")
_ChassisControlPanelColumns_Type = Integer32
_ChassisControlPanelColumns_Object = MibScalar
chassisControlPanelColumns = _ChassisControlPanelColumns_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 1, 10),
    _ChassisControlPanelColumns_Type()
)
chassisControlPanelColumns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisControlPanelColumns.setStatus("deprecated")
_ChassisControlPanelLines_Type = Integer32
_ChassisControlPanelLines_Object = MibScalar
chassisControlPanelLines = _ChassisControlPanelLines_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 1, 11),
    _ChassisControlPanelLines_Type()
)
chassisControlPanelLines.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisControlPanelLines.setStatus("deprecated")


class _ChassisControlPanelText_Type(OctetString):
    """Custom type chassisControlPanelText based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_ChassisControlPanelText_Type.__name__ = "OctetString"
_ChassisControlPanelText_Object = MibScalar
chassisControlPanelText = _ChassisControlPanelText_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 1, 12),
    _ChassisControlPanelText_Type()
)
chassisControlPanelText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisControlPanelText.setStatus("deprecated")


class _ChassisAction_Type(Integer32):
    """Custom type chassisAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("reset", 2))
    )


_ChassisAction_Type.__name__ = "Integer32"
_ChassisAction_Object = MibScalar
chassisAction = _ChassisAction_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 1, 13),
    _ChassisAction_Type()
)
chassisAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chassisAction.setStatus("deprecated")
_Slot_ObjectIdentity = ObjectIdentity
slot = _Slot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 2)
)
_SlotTable_Object = MibTable
slotTable = _SlotTable_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    slotTable.setStatus("deprecated")
_SlotEntry_Object = MibTableRow
slotEntry = _SlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 2, 1, 1)
)
slotEntry.setIndexNames(
    (0, "LANPLEX-MIB-1-2-9", "slotIndex"),
)
if mibBuilder.loadTexts:
    slotEntry.setStatus("deprecated")
_SlotIndex_Type = Integer32
_SlotIndex_Object = MibTableColumn
slotIndex = _SlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 2, 1, 1, 1),
    _SlotIndex_Type()
)
slotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotIndex.setStatus("deprecated")


class _SlotBoardType_Type(Integer32):
    """Custom type slotBoardType based on Integer32"""
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
        *(("eem", 6),
          ("emptySlot", 2),
          ("esm", 7),
          ("fcm", 5),
          ("fcm2", 8),
          ("feam", 4),
          ("spm", 3),
          ("unknown", 1))
    )


_SlotBoardType_Type.__name__ = "Integer32"
_SlotBoardType_Object = MibTableColumn
slotBoardType = _SlotBoardType_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 2, 1, 1, 2),
    _SlotBoardType_Type()
)
slotBoardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotBoardType.setStatus("deprecated")


class _SlotBoardRevision_Type(OctetString):
    """Custom type slotBoardRevision based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_SlotBoardRevision_Type.__name__ = "OctetString"
_SlotBoardRevision_Object = MibTableColumn
slotBoardRevision = _SlotBoardRevision_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 2, 1, 1, 3),
    _SlotBoardRevision_Type()
)
slotBoardRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotBoardRevision.setStatus("deprecated")


class _SlotBoardStatus_Type(Integer32):
    """Custom type slotBoardStatus based on Integer32"""
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


_SlotBoardStatus_Type.__name__ = "Integer32"
_SlotBoardStatus_Object = MibTableColumn
slotBoardStatus = _SlotBoardStatus_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 2, 1, 1, 4),
    _SlotBoardStatus_Type()
)
slotBoardStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotBoardStatus.setStatus("deprecated")


class _SlotBoardName_Type(DisplayString):
    """Custom type slotBoardName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_SlotBoardName_Type.__name__ = "DisplayString"
_SlotBoardName_Object = MibTableColumn
slotBoardName = _SlotBoardName_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 2, 1, 1, 5),
    _SlotBoardName_Type()
)
slotBoardName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotBoardName.setStatus("deprecated")


class _SlotBoardNameAbbrev_Type(DisplayString):
    """Custom type slotBoardNameAbbrev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SlotBoardNameAbbrev_Type.__name__ = "DisplayString"
_SlotBoardNameAbbrev_Object = MibTableColumn
slotBoardNameAbbrev = _SlotBoardNameAbbrev_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 2, 1, 1, 6),
    _SlotBoardNameAbbrev_Type()
)
slotBoardNameAbbrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotBoardNameAbbrev.setStatus("deprecated")


class _SlotBoardAction_Type(Integer32):
    """Custom type slotBoardAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("runDiagnostics", 2))
    )


_SlotBoardAction_Type.__name__ = "Integer32"
_SlotBoardAction_Object = MibTableColumn
slotBoardAction = _SlotBoardAction_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 2, 1, 1, 7),
    _SlotBoardAction_Type()
)
slotBoardAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slotBoardAction.setStatus("deprecated")
_Spm_ObjectIdentity = ObjectIdentity
spm = _Spm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 3)
)
_SpmTable_Object = MibTable
spmTable = _SpmTable_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    spmTable.setStatus("deprecated")
_SpmEntry_Object = MibTableRow
spmEntry = _SpmEntry_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 3, 1, 1)
)
spmEntry.setIndexNames(
    (0, "LANPLEX-MIB-1-2-9", "spmSlotIndex"),
)
if mibBuilder.loadTexts:
    spmEntry.setStatus("deprecated")
_SpmSlotIndex_Type = Integer32
_SpmSlotIndex_Object = MibTableColumn
spmSlotIndex = _SpmSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 3, 1, 1, 1),
    _SpmSlotIndex_Type()
)
spmSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spmSlotIndex.setStatus("deprecated")
_SpmEthernetPortCount_Type = Integer32
_SpmEthernetPortCount_Object = MibTableColumn
spmEthernetPortCount = _SpmEthernetPortCount_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 3, 1, 1, 2),
    _SpmEthernetPortCount_Type()
)
spmEthernetPortCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spmEthernetPortCount.setStatus("deprecated")
_SpmBaseEthernetPortIndex_Type = Integer32
_SpmBaseEthernetPortIndex_Object = MibTableColumn
spmBaseEthernetPortIndex = _SpmBaseEthernetPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 3, 1, 1, 3),
    _SpmBaseEthernetPortIndex_Type()
)
spmBaseEthernetPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spmBaseEthernetPortIndex.setStatus("deprecated")
_Feam_ObjectIdentity = ObjectIdentity
feam = _Feam_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 4)
)
_FeamTable_Object = MibTable
feamTable = _FeamTable_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    feamTable.setStatus("deprecated")
_FeamEntry_Object = MibTableRow
feamEntry = _FeamEntry_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 4, 1, 1)
)
feamEntry.setIndexNames(
    (0, "LANPLEX-MIB-1-2-9", "feamSlotIndex"),
)
if mibBuilder.loadTexts:
    feamEntry.setStatus("deprecated")
_FeamSlotIndex_Type = Integer32
_FeamSlotIndex_Object = MibTableColumn
feamSlotIndex = _FeamSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 4, 1, 1, 1),
    _FeamSlotIndex_Type()
)
feamSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feamSlotIndex.setStatus("deprecated")
_FeamMACCount_Type = Integer32
_FeamMACCount_Object = MibTableColumn
feamMACCount = _FeamMACCount_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 4, 1, 1, 2),
    _FeamMACCount_Type()
)
feamMACCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feamMACCount.setStatus("deprecated")
_FeamBaseMACIndex_Type = Integer32
_FeamBaseMACIndex_Object = MibTableColumn
feamBaseMACIndex = _FeamBaseMACIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 4, 1, 1, 3),
    _FeamBaseMACIndex_Type()
)
feamBaseMACIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feamBaseMACIndex.setStatus("deprecated")
_FeamPortCount_Type = Integer32
_FeamPortCount_Object = MibTableColumn
feamPortCount = _FeamPortCount_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 4, 1, 1, 4),
    _FeamPortCount_Type()
)
feamPortCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feamPortCount.setStatus("deprecated")
_FeamBasePortIndex_Type = Integer32
_FeamBasePortIndex_Object = MibTableColumn
feamBasePortIndex = _FeamBasePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 4, 1, 1, 5),
    _FeamBasePortIndex_Type()
)
feamBasePortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feamBasePortIndex.setStatus("deprecated")
_Fcm_ObjectIdentity = ObjectIdentity
fcm = _Fcm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 5)
)
_FcmTable_Object = MibTable
fcmTable = _FcmTable_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 5, 1)
)
if mibBuilder.loadTexts:
    fcmTable.setStatus("deprecated")
_FcmEntry_Object = MibTableRow
fcmEntry = _FcmEntry_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 5, 1, 1)
)
fcmEntry.setIndexNames(
    (0, "LANPLEX-MIB-1-2-9", "fcmSlotIndex"),
)
if mibBuilder.loadTexts:
    fcmEntry.setStatus("deprecated")
_FcmSlotIndex_Type = Integer32
_FcmSlotIndex_Object = MibTableColumn
fcmSlotIndex = _FcmSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 5, 1, 1, 1),
    _FcmSlotIndex_Type()
)
fcmSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcmSlotIndex.setStatus("deprecated")
_FcmPortCount_Type = Integer32
_FcmPortCount_Object = MibTableColumn
fcmPortCount = _FcmPortCount_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 5, 1, 1, 2),
    _FcmPortCount_Type()
)
fcmPortCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcmPortCount.setStatus("deprecated")
_FcmBasePortIndex_Type = Integer32
_FcmBasePortIndex_Object = MibTableColumn
fcmBasePortIndex = _FcmBasePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 5, 1, 1, 3),
    _FcmBasePortIndex_Type()
)
fcmBasePortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcmBasePortIndex.setStatus("deprecated")
_Port_ObjectIdentity = ObjectIdentity
port = _Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 6)
)
_PortTable_Object = MibTable
portTable = _PortTable_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 6, 1)
)
if mibBuilder.loadTexts:
    portTable.setStatus("deprecated")
_PortEntry_Object = MibTableRow
portEntry = _PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 6, 1, 1)
)
portEntry.setIndexNames(
    (0, "LANPLEX-MIB-1-2-9", "portSlotIndex"),
    (0, "LANPLEX-MIB-1-2-9", "portIndex"),
)
if mibBuilder.loadTexts:
    portEntry.setStatus("deprecated")
_PortSlotIndex_Type = Integer32
_PortSlotIndex_Object = MibTableColumn
portSlotIndex = _PortSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 6, 1, 1, 1),
    _PortSlotIndex_Type()
)
portSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portSlotIndex.setStatus("deprecated")
_PortIndex_Type = Integer32
_PortIndex_Object = MibTableColumn
portIndex = _PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 6, 1, 1, 2),
    _PortIndex_Type()
)
portIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portIndex.setStatus("deprecated")


class _PortLabel_Type(DisplayString):
    """Custom type portLabel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PortLabel_Type.__name__ = "DisplayString"
_PortLabel_Object = MibTableColumn
portLabel = _PortLabel_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 6, 1, 1, 3),
    _PortLabel_Type()
)
portLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portLabel.setStatus("deprecated")
_Eem_ObjectIdentity = ObjectIdentity
eem = _Eem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 7)
)
_EemTable_Object = MibTable
eemTable = _EemTable_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 7, 1)
)
if mibBuilder.loadTexts:
    eemTable.setStatus("deprecated")
_EemEntry_Object = MibTableRow
eemEntry = _EemEntry_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 7, 1, 1)
)
eemEntry.setIndexNames(
    (0, "LANPLEX-MIB-1-2-9", "eemSlotIndex"),
)
if mibBuilder.loadTexts:
    eemEntry.setStatus("deprecated")
_EemSlotIndex_Type = Integer32
_EemSlotIndex_Object = MibTableColumn
eemSlotIndex = _EemSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 7, 1, 1, 1),
    _EemSlotIndex_Type()
)
eemSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eemSlotIndex.setStatus("deprecated")
_EemFddiMACCount_Type = Integer32
_EemFddiMACCount_Object = MibTableColumn
eemFddiMACCount = _EemFddiMACCount_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 7, 1, 1, 2),
    _EemFddiMACCount_Type()
)
eemFddiMACCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eemFddiMACCount.setStatus("deprecated")
_EemBaseFddiMACIndex_Type = Integer32
_EemBaseFddiMACIndex_Object = MibTableColumn
eemBaseFddiMACIndex = _EemBaseFddiMACIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 7, 1, 1, 3),
    _EemBaseFddiMACIndex_Type()
)
eemBaseFddiMACIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eemBaseFddiMACIndex.setStatus("deprecated")
_EemEthernetPortCount_Type = Integer32
_EemEthernetPortCount_Object = MibTableColumn
eemEthernetPortCount = _EemEthernetPortCount_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 7, 1, 1, 4),
    _EemEthernetPortCount_Type()
)
eemEthernetPortCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eemEthernetPortCount.setStatus("deprecated")
_EemBaseEthernetPortIndex_Type = Integer32
_EemBaseEthernetPortIndex_Object = MibTableColumn
eemBaseEthernetPortIndex = _EemBaseEthernetPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 7, 1, 1, 5),
    _EemBaseEthernetPortIndex_Type()
)
eemBaseEthernetPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eemBaseEthernetPortIndex.setStatus("deprecated")
_EemAddressThreshold_Type = Integer32
_EemAddressThreshold_Object = MibTableColumn
eemAddressThreshold = _EemAddressThreshold_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 7, 1, 1, 6),
    _EemAddressThreshold_Type()
)
eemAddressThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eemAddressThreshold.setStatus("deprecated")
_EemFddiMAC_ObjectIdentity = ObjectIdentity
eemFddiMAC = _EemFddiMAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 8)
)
_EemFddiMACTable_Object = MibTable
eemFddiMACTable = _EemFddiMACTable_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 8, 1)
)
if mibBuilder.loadTexts:
    eemFddiMACTable.setStatus("deprecated")
_EemFddiMACEntry_Object = MibTableRow
eemFddiMACEntry = _EemFddiMACEntry_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 8, 1, 1)
)
eemFddiMACEntry.setIndexNames(
    (0, "LANPLEX-MIB-1-2-9", "eemFddiSlotIndex"),
    (0, "LANPLEX-MIB-1-2-9", "eemFddiMACIndex"),
)
if mibBuilder.loadTexts:
    eemFddiMACEntry.setStatus("deprecated")
_EemFddiSlotIndex_Type = Integer32
_EemFddiSlotIndex_Object = MibTableColumn
eemFddiSlotIndex = _EemFddiSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 8, 1, 1, 1),
    _EemFddiSlotIndex_Type()
)
eemFddiSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eemFddiSlotIndex.setStatus("deprecated")
_EemFddiMACIndex_Type = Integer32
_EemFddiMACIndex_Object = MibTableColumn
eemFddiMACIndex = _EemFddiMACIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 8, 1, 1, 2),
    _EemFddiMACIndex_Type()
)
eemFddiMACIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eemFddiMACIndex.setStatus("deprecated")
_EemFddiMACForwardedCts_Type = Counter32
_EemFddiMACForwardedCts_Object = MibTableColumn
eemFddiMACForwardedCts = _EemFddiMACForwardedCts_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 8, 1, 1, 3),
    _EemFddiMACForwardedCts_Type()
)
eemFddiMACForwardedCts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eemFddiMACForwardedCts.setStatus("deprecated")
_EemFddiMACDroppedCts_Type = Counter32
_EemFddiMACDroppedCts_Object = MibTableColumn
eemFddiMACDroppedCts = _EemFddiMACDroppedCts_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 8, 1, 1, 4),
    _EemFddiMACDroppedCts_Type()
)
eemFddiMACDroppedCts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eemFddiMACDroppedCts.setStatus("deprecated")
_EemEthernetPort_ObjectIdentity = ObjectIdentity
eemEthernetPort = _EemEthernetPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 9)
)
_EemEthernetPortTable_Object = MibTable
eemEthernetPortTable = _EemEthernetPortTable_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 9, 1)
)
if mibBuilder.loadTexts:
    eemEthernetPortTable.setStatus("deprecated")
_EemEthernetPortEntry_Object = MibTableRow
eemEthernetPortEntry = _EemEthernetPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 9, 1, 1)
)
eemEthernetPortEntry.setIndexNames(
    (0, "LANPLEX-MIB-1-2-9", "eemEthernetPortSlotIndex"),
    (0, "LANPLEX-MIB-1-2-9", "eemEthernetPortIndex"),
)
if mibBuilder.loadTexts:
    eemEthernetPortEntry.setStatus("deprecated")
_EemEthernetPortSlotIndex_Type = Integer32
_EemEthernetPortSlotIndex_Object = MibTableColumn
eemEthernetPortSlotIndex = _EemEthernetPortSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 9, 1, 1, 1),
    _EemEthernetPortSlotIndex_Type()
)
eemEthernetPortSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eemEthernetPortSlotIndex.setStatus("deprecated")
_EemEthernetPortIndex_Type = Integer32
_EemEthernetPortIndex_Object = MibTableColumn
eemEthernetPortIndex = _EemEthernetPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 9, 1, 1, 2),
    _EemEthernetPortIndex_Type()
)
eemEthernetPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eemEthernetPortIndex.setStatus("deprecated")


class _EemEthernetPortLabel_Type(DisplayString):
    """Custom type eemEthernetPortLabel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_EemEthernetPortLabel_Type.__name__ = "DisplayString"
_EemEthernetPortLabel_Object = MibTableColumn
eemEthernetPortLabel = _EemEthernetPortLabel_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 9, 1, 1, 3),
    _EemEthernetPortLabel_Type()
)
eemEthernetPortLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eemEthernetPortLabel.setStatus("deprecated")
_EemEthernetPortForwardedCts_Type = Counter32
_EemEthernetPortForwardedCts_Object = MibTableColumn
eemEthernetPortForwardedCts = _EemEthernetPortForwardedCts_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 9, 1, 1, 4),
    _EemEthernetPortForwardedCts_Type()
)
eemEthernetPortForwardedCts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eemEthernetPortForwardedCts.setStatus("deprecated")
_EemEthernetPortDroppedCts_Type = Counter32
_EemEthernetPortDroppedCts_Object = MibTableColumn
eemEthernetPortDroppedCts = _EemEthernetPortDroppedCts_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 9, 1, 1, 5),
    _EemEthernetPortDroppedCts_Type()
)
eemEthernetPortDroppedCts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eemEthernetPortDroppedCts.setStatus("deprecated")
_EemEthernetPortUTurnCts_Type = Counter32
_EemEthernetPortUTurnCts_Object = MibTableColumn
eemEthernetPortUTurnCts = _EemEthernetPortUTurnCts_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 9, 1, 1, 6),
    _EemEthernetPortUTurnCts_Type()
)
eemEthernetPortUTurnCts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eemEthernetPortUTurnCts.setStatus("deprecated")


class _EemEthernetPortState_Type(Integer32):
    """Custom type eemEthernetPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("offline", 3),
          ("onlineActive", 1),
          ("onlineInactive", 2))
    )


_EemEthernetPortState_Type.__name__ = "Integer32"
_EemEthernetPortState_Object = MibTableColumn
eemEthernetPortState = _EemEthernetPortState_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 9, 1, 1, 7),
    _EemEthernetPortState_Type()
)
eemEthernetPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eemEthernetPortState.setStatus("deprecated")


class _EemEthernetPortAction_Type(Integer32):
    """Custom type eemEthernetPortAction based on Integer32"""
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


_EemEthernetPortAction_Type.__name__ = "Integer32"
_EemEthernetPortAction_Object = MibTableColumn
eemEthernetPortAction = _EemEthernetPortAction_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 9, 1, 1, 8),
    _EemEthernetPortAction_Type()
)
eemEthernetPortAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eemEthernetPortAction.setStatus("deprecated")
_EemMACAddress_ObjectIdentity = ObjectIdentity
eemMACAddress = _EemMACAddress_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 10)
)
_EemEthernetMACAddressTable_Object = MibTable
eemEthernetMACAddressTable = _EemEthernetMACAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 10, 1)
)
if mibBuilder.loadTexts:
    eemEthernetMACAddressTable.setStatus("deprecated")
_EemEthernetMACAddressEntry_Object = MibTableRow
eemEthernetMACAddressEntry = _EemEthernetMACAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 10, 1, 1)
)
eemEthernetMACAddressEntry.setIndexNames(
    (0, "LANPLEX-MIB-1-2-9", "eemEthernetMACAddressSlotIndex"),
    (0, "LANPLEX-MIB-1-2-9", "eemEthernetMACAddressPortIndex"),
    (0, "LANPLEX-MIB-1-2-9", "eemEthernetMACAddressIndex"),
)
if mibBuilder.loadTexts:
    eemEthernetMACAddressEntry.setStatus("deprecated")
_EemEthernetMACAddressSlotIndex_Type = Integer32
_EemEthernetMACAddressSlotIndex_Object = MibTableColumn
eemEthernetMACAddressSlotIndex = _EemEthernetMACAddressSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 10, 1, 1, 1),
    _EemEthernetMACAddressSlotIndex_Type()
)
eemEthernetMACAddressSlotIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eemEthernetMACAddressSlotIndex.setStatus("deprecated")
_EemEthernetMACAddressPortIndex_Type = Integer32
_EemEthernetMACAddressPortIndex_Object = MibTableColumn
eemEthernetMACAddressPortIndex = _EemEthernetMACAddressPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 10, 1, 1, 2),
    _EemEthernetMACAddressPortIndex_Type()
)
eemEthernetMACAddressPortIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eemEthernetMACAddressPortIndex.setStatus("deprecated")
_EemEthernetMACAddressIndex_Type = Integer32
_EemEthernetMACAddressIndex_Object = MibTableColumn
eemEthernetMACAddressIndex = _EemEthernetMACAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 10, 1, 1, 3),
    _EemEthernetMACAddressIndex_Type()
)
eemEthernetMACAddressIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eemEthernetMACAddressIndex.setStatus("deprecated")


class _EemEthernetMACAddressType_Type(Integer32):
    """Custom type eemEthernetMACAddressType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("other", 1))
    )


_EemEthernetMACAddressType_Type.__name__ = "Integer32"
_EemEthernetMACAddressType_Object = MibTableColumn
eemEthernetMACAddressType = _EemEthernetMACAddressType_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 10, 1, 1, 4),
    _EemEthernetMACAddressType_Type()
)
eemEthernetMACAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eemEthernetMACAddressType.setStatus("deprecated")


class _EemEthernetMACAddressRemoteAddress_Type(OctetString):
    """Custom type eemEthernetMACAddressRemoteAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_EemEthernetMACAddressRemoteAddress_Type.__name__ = "OctetString"
_EemEthernetMACAddressRemoteAddress_Object = MibTableColumn
eemEthernetMACAddressRemoteAddress = _EemEthernetMACAddressRemoteAddress_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 10, 1, 1, 5),
    _EemEthernetMACAddressRemoteAddress_Type()
)
eemEthernetMACAddressRemoteAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eemEthernetMACAddressRemoteAddress.setStatus("deprecated")


class _EemEthernetMACAddressIsStatic_Type(Integer32):
    """Custom type eemEthernetMACAddressIsStatic based on Integer32"""
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


_EemEthernetMACAddressIsStatic_Type.__name__ = "Integer32"
_EemEthernetMACAddressIsStatic_Object = MibTableColumn
eemEthernetMACAddressIsStatic = _EemEthernetMACAddressIsStatic_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 10, 1, 1, 6),
    _EemEthernetMACAddressIsStatic_Type()
)
eemEthernetMACAddressIsStatic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eemEthernetMACAddressIsStatic.setStatus("deprecated")
_EemEthernetMACAddressStaticPort_Type = Integer32
_EemEthernetMACAddressStaticPort_Object = MibTableColumn
eemEthernetMACAddressStaticPort = _EemEthernetMACAddressStaticPort_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 10, 1, 1, 7),
    _EemEthernetMACAddressStaticPort_Type()
)
eemEthernetMACAddressStaticPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eemEthernetMACAddressStaticPort.setStatus("deprecated")
_EemEthernetMACAddressAge_Type = Integer32
_EemEthernetMACAddressAge_Object = MibTableColumn
eemEthernetMACAddressAge = _EemEthernetMACAddressAge_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 10, 1, 1, 8),
    _EemEthernetMACAddressAge_Type()
)
eemEthernetMACAddressAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eemEthernetMACAddressAge.setStatus("deprecated")
_LpSystem_ObjectIdentity = ObjectIdentity
lpSystem = _LpSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 11)
)
_LpSystemId_Type = Integer32
_LpSystemId_Object = MibScalar
lpSystemId = _LpSystemId_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 11, 1),
    _LpSystemId_Type()
)
lpSystemId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSystemId.setStatus("mandatory")


class _LpSystemType_Type(Integer32):
    """Custom type lpSystemType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fourSlot", 3),
          ("other", 1),
          ("tweleveSlot", 2))
    )


_LpSystemType_Type.__name__ = "Integer32"
_LpSystemType_Object = MibScalar
lpSystemType = _LpSystemType_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 11, 2),
    _LpSystemType_Type()
)
lpSystemType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSystemType.setStatus("mandatory")


class _LpSystemName_Type(DisplayString):
    """Custom type lpSystemName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_LpSystemName_Type.__name__ = "DisplayString"
_LpSystemName_Object = MibScalar
lpSystemName = _LpSystemName_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 11, 3),
    _LpSystemName_Type()
)
lpSystemName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSystemName.setStatus("mandatory")


class _LpSystemManufacturer_Type(DisplayString):
    """Custom type lpSystemManufacturer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_LpSystemManufacturer_Type.__name__ = "DisplayString"
_LpSystemManufacturer_Object = MibScalar
lpSystemManufacturer = _LpSystemManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 11, 4),
    _LpSystemManufacturer_Type()
)
lpSystemManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSystemManufacturer.setStatus("mandatory")


class _LpSystemBackplaneRevision_Type(OctetString):
    """Custom type lpSystemBackplaneRevision based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_LpSystemBackplaneRevision_Type.__name__ = "OctetString"
_LpSystemBackplaneRevision_Object = MibScalar
lpSystemBackplaneRevision = _LpSystemBackplaneRevision_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 11, 5),
    _LpSystemBackplaneRevision_Type()
)
lpSystemBackplaneRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSystemBackplaneRevision.setStatus("mandatory")
_LpSystemSlotCount_Type = Integer32
_LpSystemSlotCount_Object = MibScalar
lpSystemSlotCount = _LpSystemSlotCount_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 11, 6),
    _LpSystemSlotCount_Type()
)
lpSystemSlotCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSystemSlotCount.setStatus("mandatory")
_LpSystemMemorySize_Type = Integer32
_LpSystemMemorySize_Object = MibScalar
lpSystemMemorySize = _LpSystemMemorySize_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 11, 7),
    _LpSystemMemorySize_Type()
)
lpSystemMemorySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSystemMemorySize.setStatus("mandatory")
_LpSystemFlashMemorySize_Type = Integer32
_LpSystemFlashMemorySize_Object = MibScalar
lpSystemFlashMemorySize = _LpSystemFlashMemorySize_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 11, 8),
    _LpSystemFlashMemorySize_Type()
)
lpSystemFlashMemorySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSystemFlashMemorySize.setStatus("mandatory")
_LpSystemNvMemorySize_Type = Integer32
_LpSystemNvMemorySize_Object = MibScalar
lpSystemNvMemorySize = _LpSystemNvMemorySize_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 11, 9),
    _LpSystemNvMemorySize_Type()
)
lpSystemNvMemorySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSystemNvMemorySize.setStatus("mandatory")


class _LpSystemSoftwareRevision_Type(OctetString):
    """Custom type lpSystemSoftwareRevision based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_LpSystemSoftwareRevision_Type.__name__ = "OctetString"
_LpSystemSoftwareRevision_Object = MibScalar
lpSystemSoftwareRevision = _LpSystemSoftwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 11, 10),
    _LpSystemSoftwareRevision_Type()
)
lpSystemSoftwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSystemSoftwareRevision.setStatus("mandatory")


class _LpSystemBuildTime_Type(DisplayString):
    """Custom type lpSystemBuildTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_LpSystemBuildTime_Type.__name__ = "DisplayString"
_LpSystemBuildTime_Object = MibScalar
lpSystemBuildTime = _LpSystemBuildTime_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 11, 11),
    _LpSystemBuildTime_Type()
)
lpSystemBuildTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSystemBuildTime.setStatus("mandatory")


class _LpSystemControlPanelHardwareRevision_Type(OctetString):
    """Custom type lpSystemControlPanelHardwareRevision based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_LpSystemControlPanelHardwareRevision_Type.__name__ = "OctetString"
_LpSystemControlPanelHardwareRevision_Object = MibScalar
lpSystemControlPanelHardwareRevision = _LpSystemControlPanelHardwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 11, 12),
    _LpSystemControlPanelHardwareRevision_Type()
)
lpSystemControlPanelHardwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSystemControlPanelHardwareRevision.setStatus("mandatory")


class _LpSystemControlPanelSoftwareRevision_Type(OctetString):
    """Custom type lpSystemControlPanelSoftwareRevision based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_LpSystemControlPanelSoftwareRevision_Type.__name__ = "OctetString"
_LpSystemControlPanelSoftwareRevision_Object = MibScalar
lpSystemControlPanelSoftwareRevision = _LpSystemControlPanelSoftwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 11, 13),
    _LpSystemControlPanelSoftwareRevision_Type()
)
lpSystemControlPanelSoftwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSystemControlPanelSoftwareRevision.setStatus("mandatory")
_LpSystemControlPanelLines_Type = Integer32
_LpSystemControlPanelLines_Object = MibScalar
lpSystemControlPanelLines = _LpSystemControlPanelLines_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 11, 14),
    _LpSystemControlPanelLines_Type()
)
lpSystemControlPanelLines.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSystemControlPanelLines.setStatus("mandatory")
_LpSystemControlPanelColumns_Type = Integer32
_LpSystemControlPanelColumns_Object = MibScalar
lpSystemControlPanelColumns = _LpSystemControlPanelColumns_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 11, 15),
    _LpSystemControlPanelColumns_Type()
)
lpSystemControlPanelColumns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSystemControlPanelColumns.setStatus("mandatory")


class _LpSystemControlPanelText_Type(OctetString):
    """Custom type lpSystemControlPanelText based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_LpSystemControlPanelText_Type.__name__ = "OctetString"
_LpSystemControlPanelText_Object = MibScalar
lpSystemControlPanelText = _LpSystemControlPanelText_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 11, 16),
    _LpSystemControlPanelText_Type()
)
lpSystemControlPanelText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSystemControlPanelText.setStatus("mandatory")
_LpSystemFddiMacCount_Type = Integer32
_LpSystemFddiMacCount_Object = MibScalar
lpSystemFddiMacCount = _LpSystemFddiMacCount_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 11, 17),
    _LpSystemFddiMacCount_Type()
)
lpSystemFddiMacCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSystemFddiMacCount.setStatus("mandatory")
_LpSystemFddiPortCount_Type = Integer32
_LpSystemFddiPortCount_Object = MibScalar
lpSystemFddiPortCount = _LpSystemFddiPortCount_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 11, 18),
    _LpSystemFddiPortCount_Type()
)
lpSystemFddiPortCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSystemFddiPortCount.setStatus("mandatory")
_LpSystemEthernetPortCount_Type = Integer32
_LpSystemEthernetPortCount_Object = MibScalar
lpSystemEthernetPortCount = _LpSystemEthernetPortCount_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 11, 19),
    _LpSystemEthernetPortCount_Type()
)
lpSystemEthernetPortCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSystemEthernetPortCount.setStatus("mandatory")
_LpSystemExpressFunctionCount_Type = Integer32
_LpSystemExpressFunctionCount_Object = MibScalar
lpSystemExpressFunctionCount = _LpSystemExpressFunctionCount_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 11, 20),
    _LpSystemExpressFunctionCount_Type()
)
lpSystemExpressFunctionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSystemExpressFunctionCount.setStatus("deprecated")
_LpSystemExpressFddiPortCount_Type = Integer32
_LpSystemExpressFddiPortCount_Object = MibScalar
lpSystemExpressFddiPortCount = _LpSystemExpressFddiPortCount_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 11, 21),
    _LpSystemExpressFddiPortCount_Type()
)
lpSystemExpressFddiPortCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSystemExpressFddiPortCount.setStatus("deprecated")
_LpSystemExpressEthernetPortCount_Type = Integer32
_LpSystemExpressEthernetPortCount_Object = MibScalar
lpSystemExpressEthernetPortCount = _LpSystemExpressEthernetPortCount_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 11, 22),
    _LpSystemExpressEthernetPortCount_Type()
)
lpSystemExpressEthernetPortCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSystemExpressEthernetPortCount.setStatus("deprecated")
_LpSystemPowerSupplyCount_Type = Integer32
_LpSystemPowerSupplyCount_Object = MibScalar
lpSystemPowerSupplyCount = _LpSystemPowerSupplyCount_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 11, 23),
    _LpSystemPowerSupplyCount_Type()
)
lpSystemPowerSupplyCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSystemPowerSupplyCount.setStatus("mandatory")


class _LpSystemAction_Type(Integer32):
    """Custom type lpSystemAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("reset", 2))
    )


_LpSystemAction_Type.__name__ = "Integer32"
_LpSystemAction_Object = MibScalar
lpSystemAction = _LpSystemAction_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 11, 24),
    _LpSystemAction_Type()
)
lpSystemAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpSystemAction.setStatus("mandatory")
_LpSystemBridgeFunctionCount_Type = Integer32
_LpSystemBridgeFunctionCount_Object = MibScalar
lpSystemBridgeFunctionCount = _LpSystemBridgeFunctionCount_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 11, 25),
    _LpSystemBridgeFunctionCount_Type()
)
lpSystemBridgeFunctionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSystemBridgeFunctionCount.setStatus("mandatory")


class _LpSystemSmtProxyTimeoutBase_Type(Integer32):
    """Custom type lpSystemSmtProxyTimeoutBase based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_LpSystemSmtProxyTimeoutBase_Type.__name__ = "Integer32"
_LpSystemSmtProxyTimeoutBase_Object = MibScalar
lpSystemSmtProxyTimeoutBase = _LpSystemSmtProxyTimeoutBase_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 11, 26),
    _LpSystemSmtProxyTimeoutBase_Type()
)
lpSystemSmtProxyTimeoutBase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpSystemSmtProxyTimeoutBase.setStatus("mandatory")


class _LpSystemSmtProxyEvents_Type(Integer32):
    """Custom type lpSystemSmtProxyEvents based on Integer32"""
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


_LpSystemSmtProxyEvents_Type.__name__ = "Integer32"
_LpSystemSmtProxyEvents_Object = MibScalar
lpSystemSmtProxyEvents = _LpSystemSmtProxyEvents_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 11, 27),
    _LpSystemSmtProxyEvents_Type()
)
lpSystemSmtProxyEvents.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpSystemSmtProxyEvents.setStatus("mandatory")
_LpSlot_ObjectIdentity = ObjectIdentity
lpSlot = _LpSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 12)
)
_LpSlotTable_Object = MibTable
lpSlotTable = _LpSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 12, 1)
)
if mibBuilder.loadTexts:
    lpSlotTable.setStatus("mandatory")
_LpSlotEntry_Object = MibTableRow
lpSlotEntry = _LpSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 12, 1, 1)
)
lpSlotEntry.setIndexNames(
    (0, "LANPLEX-MIB-1-2-9", "lpSlotIndex"),
)
if mibBuilder.loadTexts:
    lpSlotEntry.setStatus("mandatory")
_LpSlotIndex_Type = Integer32
_LpSlotIndex_Object = MibTableColumn
lpSlotIndex = _LpSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 12, 1, 1, 1),
    _LpSlotIndex_Type()
)
lpSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSlotIndex.setStatus("mandatory")


class _LpSlotBoardType_Type(Integer32):
    """Custom type lpSlotBoardType based on Integer32"""
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
        *(("eem", 6),
          ("emptySlot", 2),
          ("esm", 7),
          ("fcm", 5),
          ("fcm2", 8),
          ("feam", 4),
          ("spm", 3),
          ("unknown", 1))
    )


_LpSlotBoardType_Type.__name__ = "Integer32"
_LpSlotBoardType_Object = MibTableColumn
lpSlotBoardType = _LpSlotBoardType_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 12, 1, 1, 2),
    _LpSlotBoardType_Type()
)
lpSlotBoardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSlotBoardType.setStatus("mandatory")


class _LpSlotBoardRevision_Type(OctetString):
    """Custom type lpSlotBoardRevision based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_LpSlotBoardRevision_Type.__name__ = "OctetString"
_LpSlotBoardRevision_Object = MibTableColumn
lpSlotBoardRevision = _LpSlotBoardRevision_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 12, 1, 1, 3),
    _LpSlotBoardRevision_Type()
)
lpSlotBoardRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSlotBoardRevision.setStatus("mandatory")


class _LpSlotBoardStatus_Type(Integer32):
    """Custom type lpSlotBoardStatus based on Integer32"""
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


_LpSlotBoardStatus_Type.__name__ = "Integer32"
_LpSlotBoardStatus_Object = MibTableColumn
lpSlotBoardStatus = _LpSlotBoardStatus_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 12, 1, 1, 4),
    _LpSlotBoardStatus_Type()
)
lpSlotBoardStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSlotBoardStatus.setStatus("mandatory")


class _LpSlotBoardName_Type(DisplayString):
    """Custom type lpSlotBoardName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_LpSlotBoardName_Type.__name__ = "DisplayString"
_LpSlotBoardName_Object = MibTableColumn
lpSlotBoardName = _LpSlotBoardName_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 12, 1, 1, 5),
    _LpSlotBoardName_Type()
)
lpSlotBoardName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSlotBoardName.setStatus("mandatory")


class _LpSlotBoardNameAbbrev_Type(DisplayString):
    """Custom type lpSlotBoardNameAbbrev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LpSlotBoardNameAbbrev_Type.__name__ = "DisplayString"
_LpSlotBoardNameAbbrev_Object = MibTableColumn
lpSlotBoardNameAbbrev = _LpSlotBoardNameAbbrev_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 12, 1, 1, 6),
    _LpSlotBoardNameAbbrev_Type()
)
lpSlotBoardNameAbbrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSlotBoardNameAbbrev.setStatus("mandatory")
_LpSlotFddiMacCount_Type = Integer32
_LpSlotFddiMacCount_Object = MibTableColumn
lpSlotFddiMacCount = _LpSlotFddiMacCount_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 12, 1, 1, 7),
    _LpSlotFddiMacCount_Type()
)
lpSlotFddiMacCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSlotFddiMacCount.setStatus("mandatory")
_LpSlotFddiMacBaseIndex_Type = Integer32
_LpSlotFddiMacBaseIndex_Object = MibTableColumn
lpSlotFddiMacBaseIndex = _LpSlotFddiMacBaseIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 12, 1, 1, 8),
    _LpSlotFddiMacBaseIndex_Type()
)
lpSlotFddiMacBaseIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSlotFddiMacBaseIndex.setStatus("mandatory")
_LpSlotFddiPortCount_Type = Integer32
_LpSlotFddiPortCount_Object = MibTableColumn
lpSlotFddiPortCount = _LpSlotFddiPortCount_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 12, 1, 1, 9),
    _LpSlotFddiPortCount_Type()
)
lpSlotFddiPortCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSlotFddiPortCount.setStatus("mandatory")
_LpSlotFddiPortBaseIndex_Type = Integer32
_LpSlotFddiPortBaseIndex_Object = MibTableColumn
lpSlotFddiPortBaseIndex = _LpSlotFddiPortBaseIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 12, 1, 1, 10),
    _LpSlotFddiPortBaseIndex_Type()
)
lpSlotFddiPortBaseIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSlotFddiPortBaseIndex.setStatus("mandatory")
_LpSlotEthernetPortCount_Type = Integer32
_LpSlotEthernetPortCount_Object = MibTableColumn
lpSlotEthernetPortCount = _LpSlotEthernetPortCount_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 12, 1, 1, 11),
    _LpSlotEthernetPortCount_Type()
)
lpSlotEthernetPortCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSlotEthernetPortCount.setStatus("mandatory")
_LpSlotEthernetPortBaseIndex_Type = Integer32
_LpSlotEthernetPortBaseIndex_Object = MibTableColumn
lpSlotEthernetPortBaseIndex = _LpSlotEthernetPortBaseIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 12, 1, 1, 12),
    _LpSlotEthernetPortBaseIndex_Type()
)
lpSlotEthernetPortBaseIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSlotEthernetPortBaseIndex.setStatus("mandatory")
_LpSlotExpressFunctionCount_Type = Integer32
_LpSlotExpressFunctionCount_Object = MibTableColumn
lpSlotExpressFunctionCount = _LpSlotExpressFunctionCount_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 12, 1, 1, 13),
    _LpSlotExpressFunctionCount_Type()
)
lpSlotExpressFunctionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSlotExpressFunctionCount.setStatus("deprecated")
_LpSlotExpressFunctionBaseIndex_Type = Integer32
_LpSlotExpressFunctionBaseIndex_Object = MibTableColumn
lpSlotExpressFunctionBaseIndex = _LpSlotExpressFunctionBaseIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 12, 1, 1, 14),
    _LpSlotExpressFunctionBaseIndex_Type()
)
lpSlotExpressFunctionBaseIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSlotExpressFunctionBaseIndex.setStatus("deprecated")
_LpSlotExpressFddiPortCount_Type = Integer32
_LpSlotExpressFddiPortCount_Object = MibTableColumn
lpSlotExpressFddiPortCount = _LpSlotExpressFddiPortCount_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 12, 1, 1, 15),
    _LpSlotExpressFddiPortCount_Type()
)
lpSlotExpressFddiPortCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSlotExpressFddiPortCount.setStatus("deprecated")
_LpSlotExpressFddiPortBaseIndex_Type = Integer32
_LpSlotExpressFddiPortBaseIndex_Object = MibTableColumn
lpSlotExpressFddiPortBaseIndex = _LpSlotExpressFddiPortBaseIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 12, 1, 1, 16),
    _LpSlotExpressFddiPortBaseIndex_Type()
)
lpSlotExpressFddiPortBaseIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSlotExpressFddiPortBaseIndex.setStatus("deprecated")
_LpSlotExpressEthernetPortCount_Type = Integer32
_LpSlotExpressEthernetPortCount_Object = MibTableColumn
lpSlotExpressEthernetPortCount = _LpSlotExpressEthernetPortCount_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 12, 1, 1, 17),
    _LpSlotExpressEthernetPortCount_Type()
)
lpSlotExpressEthernetPortCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSlotExpressEthernetPortCount.setStatus("deprecated")
_LpSlotExpressEthernetPortBaseIndex_Type = Integer32
_LpSlotExpressEthernetPortBaseIndex_Object = MibTableColumn
lpSlotExpressEthernetPortBaseIndex = _LpSlotExpressEthernetPortBaseIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 12, 1, 1, 18),
    _LpSlotExpressEthernetPortBaseIndex_Type()
)
lpSlotExpressEthernetPortBaseIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSlotExpressEthernetPortBaseIndex.setStatus("deprecated")


class _LpSlotBoardAction_Type(Integer32):
    """Custom type lpSlotBoardAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("runDiagnostics", 2))
    )


_LpSlotBoardAction_Type.__name__ = "Integer32"
_LpSlotBoardAction_Object = MibTableColumn
lpSlotBoardAction = _LpSlotBoardAction_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 12, 1, 1, 19),
    _LpSlotBoardAction_Type()
)
lpSlotBoardAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpSlotBoardAction.setStatus("mandatory")
_LpSlotBridgeFunctionCount_Type = Integer32
_LpSlotBridgeFunctionCount_Object = MibTableColumn
lpSlotBridgeFunctionCount = _LpSlotBridgeFunctionCount_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 12, 1, 1, 20),
    _LpSlotBridgeFunctionCount_Type()
)
lpSlotBridgeFunctionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSlotBridgeFunctionCount.setStatus("mandatory")
_LpSlotBridgeFunctionBaseIndex_Type = Integer32
_LpSlotBridgeFunctionBaseIndex_Object = MibTableColumn
lpSlotBridgeFunctionBaseIndex = _LpSlotBridgeFunctionBaseIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 12, 1, 1, 21),
    _LpSlotBridgeFunctionBaseIndex_Type()
)
lpSlotBridgeFunctionBaseIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSlotBridgeFunctionBaseIndex.setStatus("mandatory")
_LpFddiMac_ObjectIdentity = ObjectIdentity
lpFddiMac = _LpFddiMac_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 13)
)
_LpFddiMacTable_Object = MibTable
lpFddiMacTable = _LpFddiMacTable_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 13, 1)
)
if mibBuilder.loadTexts:
    lpFddiMacTable.setStatus("mandatory")
_LpFddiMacEntry_Object = MibTableRow
lpFddiMacEntry = _LpFddiMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 13, 1, 1)
)
lpFddiMacEntry.setIndexNames(
    (0, "LANPLEX-MIB-1-2-9", "lpFddiMacIndex"),
)
if mibBuilder.loadTexts:
    lpFddiMacEntry.setStatus("mandatory")
_LpFddiMacIndex_Type = Integer32
_LpFddiMacIndex_Object = MibTableColumn
lpFddiMacIndex = _LpFddiMacIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 13, 1, 1, 1),
    _LpFddiMacIndex_Type()
)
lpFddiMacIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpFddiMacIndex.setStatus("mandatory")
_LpFddiMacSlotIndex_Type = Integer32
_LpFddiMacSlotIndex_Object = MibTableColumn
lpFddiMacSlotIndex = _LpFddiMacSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 13, 1, 1, 2),
    _LpFddiMacSlotIndex_Type()
)
lpFddiMacSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpFddiMacSlotIndex.setStatus("mandatory")
_LpFddiMacLocalIndex_Type = Integer32
_LpFddiMacLocalIndex_Object = MibTableColumn
lpFddiMacLocalIndex = _LpFddiMacLocalIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 13, 1, 1, 3),
    _LpFddiMacLocalIndex_Type()
)
lpFddiMacLocalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpFddiMacLocalIndex.setStatus("mandatory")
_LpFddiMacByteReceiveRate_Type = Integer32
_LpFddiMacByteReceiveRate_Object = MibTableColumn
lpFddiMacByteReceiveRate = _LpFddiMacByteReceiveRate_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 13, 1, 1, 4),
    _LpFddiMacByteReceiveRate_Type()
)
lpFddiMacByteReceiveRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpFddiMacByteReceiveRate.setStatus("mandatory")
_LpFddiMacPeakByteReceiveRate_Type = Integer32
_LpFddiMacPeakByteReceiveRate_Object = MibTableColumn
lpFddiMacPeakByteReceiveRate = _LpFddiMacPeakByteReceiveRate_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 13, 1, 1, 5),
    _LpFddiMacPeakByteReceiveRate_Type()
)
lpFddiMacPeakByteReceiveRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpFddiMacPeakByteReceiveRate.setStatus("mandatory")
_LpFddiMacFrameReceiveRate_Type = Integer32
_LpFddiMacFrameReceiveRate_Object = MibTableColumn
lpFddiMacFrameReceiveRate = _LpFddiMacFrameReceiveRate_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 13, 1, 1, 6),
    _LpFddiMacFrameReceiveRate_Type()
)
lpFddiMacFrameReceiveRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpFddiMacFrameReceiveRate.setStatus("mandatory")
_LpFddiMacPeakFrameReceiveRate_Type = Integer32
_LpFddiMacPeakFrameReceiveRate_Object = MibTableColumn
lpFddiMacPeakFrameReceiveRate = _LpFddiMacPeakFrameReceiveRate_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 13, 1, 1, 7),
    _LpFddiMacPeakFrameReceiveRate_Type()
)
lpFddiMacPeakFrameReceiveRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpFddiMacPeakFrameReceiveRate.setStatus("mandatory")
_LpFddiMacByteTransmitRate_Type = Integer32
_LpFddiMacByteTransmitRate_Object = MibTableColumn
lpFddiMacByteTransmitRate = _LpFddiMacByteTransmitRate_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 13, 1, 1, 8),
    _LpFddiMacByteTransmitRate_Type()
)
lpFddiMacByteTransmitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpFddiMacByteTransmitRate.setStatus("mandatory")
_LpFddiMacPeakByteTransmitRate_Type = Integer32
_LpFddiMacPeakByteTransmitRate_Object = MibTableColumn
lpFddiMacPeakByteTransmitRate = _LpFddiMacPeakByteTransmitRate_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 13, 1, 1, 9),
    _LpFddiMacPeakByteTransmitRate_Type()
)
lpFddiMacPeakByteTransmitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpFddiMacPeakByteTransmitRate.setStatus("mandatory")
_LpFddiMacFrameTransmitRate_Type = Integer32
_LpFddiMacFrameTransmitRate_Object = MibTableColumn
lpFddiMacFrameTransmitRate = _LpFddiMacFrameTransmitRate_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 13, 1, 1, 10),
    _LpFddiMacFrameTransmitRate_Type()
)
lpFddiMacFrameTransmitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpFddiMacFrameTransmitRate.setStatus("mandatory")
_LpFddiMacPeakFrameTransmitRate_Type = Integer32
_LpFddiMacPeakFrameTransmitRate_Object = MibTableColumn
lpFddiMacPeakFrameTransmitRate = _LpFddiMacPeakFrameTransmitRate_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 13, 1, 1, 11),
    _LpFddiMacPeakFrameTransmitRate_Type()
)
lpFddiMacPeakFrameTransmitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpFddiMacPeakFrameTransmitRate.setStatus("mandatory")
_LpFddiMacReceiveMulticastThreshold_Type = Integer32
_LpFddiMacReceiveMulticastThreshold_Object = MibTableColumn
lpFddiMacReceiveMulticastThreshold = _LpFddiMacReceiveMulticastThreshold_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 13, 1, 1, 12),
    _LpFddiMacReceiveMulticastThreshold_Type()
)
lpFddiMacReceiveMulticastThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpFddiMacReceiveMulticastThreshold.setStatus("deprecated")


class _LpFddiMacBeaconHistory_Type(OctetString):
    """Custom type lpFddiMacBeaconHistory based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_LpFddiMacBeaconHistory_Type.__name__ = "OctetString"
_LpFddiMacBeaconHistory_Object = MibTableColumn
lpFddiMacBeaconHistory = _LpFddiMacBeaconHistory_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 13, 1, 1, 13),
    _LpFddiMacBeaconHistory_Type()
)
lpFddiMacBeaconHistory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpFddiMacBeaconHistory.setStatus("mandatory")
_LpEthernetPort_ObjectIdentity = ObjectIdentity
lpEthernetPort = _LpEthernetPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 14)
)
_LpEthernetPortTable_Object = MibTable
lpEthernetPortTable = _LpEthernetPortTable_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 14, 1)
)
if mibBuilder.loadTexts:
    lpEthernetPortTable.setStatus("mandatory")
_LpEthernetPortEntry_Object = MibTableRow
lpEthernetPortEntry = _LpEthernetPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 14, 1, 1)
)
lpEthernetPortEntry.setIndexNames(
    (0, "LANPLEX-MIB-1-2-9", "lpEthernetPortIndex"),
)
if mibBuilder.loadTexts:
    lpEthernetPortEntry.setStatus("mandatory")
_LpEthernetPortIndex_Type = Integer32
_LpEthernetPortIndex_Object = MibTableColumn
lpEthernetPortIndex = _LpEthernetPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 14, 1, 1, 1),
    _LpEthernetPortIndex_Type()
)
lpEthernetPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEthernetPortIndex.setStatus("mandatory")
_LpEthernetPortSlotIndex_Type = Integer32
_LpEthernetPortSlotIndex_Object = MibTableColumn
lpEthernetPortSlotIndex = _LpEthernetPortSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 14, 1, 1, 2),
    _LpEthernetPortSlotIndex_Type()
)
lpEthernetPortSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEthernetPortSlotIndex.setStatus("mandatory")
_LpEthernetPortLocalIndex_Type = Integer32
_LpEthernetPortLocalIndex_Object = MibTableColumn
lpEthernetPortLocalIndex = _LpEthernetPortLocalIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 14, 1, 1, 3),
    _LpEthernetPortLocalIndex_Type()
)
lpEthernetPortLocalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEthernetPortLocalIndex.setStatus("mandatory")


class _LpEthernetPortLabel_Type(DisplayString):
    """Custom type lpEthernetPortLabel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LpEthernetPortLabel_Type.__name__ = "DisplayString"
_LpEthernetPortLabel_Object = MibTableColumn
lpEthernetPortLabel = _LpEthernetPortLabel_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 14, 1, 1, 4),
    _LpEthernetPortLabel_Type()
)
lpEthernetPortLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpEthernetPortLabel.setStatus("mandatory")


class _LpEthernetPortChipsetType_Type(Integer32):
    """Custom type lpEthernetPortChipsetType based on Integer32"""
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
        *(("chipsetAMD79900", 2),
          ("chipsetFujitsu86950", 8),
          ("chipsetIntel82586", 3),
          ("chipsetIntel82596", 4),
          ("chipsetNational8390", 6),
          ("chipsetNationalSonic", 7),
          ("chipsetSEEQ8003", 5),
          ("other", 1))
    )


_LpEthernetPortChipsetType_Type.__name__ = "Integer32"
_LpEthernetPortChipsetType_Object = MibTableColumn
lpEthernetPortChipsetType = _LpEthernetPortChipsetType_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 14, 1, 1, 5),
    _LpEthernetPortChipsetType_Type()
)
lpEthernetPortChipsetType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEthernetPortChipsetType.setStatus("mandatory")


class _LpEthernetPortLinkStatus_Type(Integer32):
    """Custom type lpEthernetPortLinkStatus based on Integer32"""
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


_LpEthernetPortLinkStatus_Type.__name__ = "Integer32"
_LpEthernetPortLinkStatus_Object = MibTableColumn
lpEthernetPortLinkStatus = _LpEthernetPortLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 14, 1, 1, 6),
    _LpEthernetPortLinkStatus_Type()
)
lpEthernetPortLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEthernetPortLinkStatus.setStatus("mandatory")
_LpEthernetPortByteReceiveRate_Type = Integer32
_LpEthernetPortByteReceiveRate_Object = MibTableColumn
lpEthernetPortByteReceiveRate = _LpEthernetPortByteReceiveRate_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 14, 1, 1, 7),
    _LpEthernetPortByteReceiveRate_Type()
)
lpEthernetPortByteReceiveRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEthernetPortByteReceiveRate.setStatus("mandatory")
_LpEthernetPortPeakByteReceiveRate_Type = Integer32
_LpEthernetPortPeakByteReceiveRate_Object = MibTableColumn
lpEthernetPortPeakByteReceiveRate = _LpEthernetPortPeakByteReceiveRate_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 14, 1, 1, 8),
    _LpEthernetPortPeakByteReceiveRate_Type()
)
lpEthernetPortPeakByteReceiveRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEthernetPortPeakByteReceiveRate.setStatus("mandatory")
_LpEthernetPortFrameReceiveRate_Type = Integer32
_LpEthernetPortFrameReceiveRate_Object = MibTableColumn
lpEthernetPortFrameReceiveRate = _LpEthernetPortFrameReceiveRate_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 14, 1, 1, 9),
    _LpEthernetPortFrameReceiveRate_Type()
)
lpEthernetPortFrameReceiveRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEthernetPortFrameReceiveRate.setStatus("mandatory")
_LpEthernetPortPeakFrameReceiveRate_Type = Integer32
_LpEthernetPortPeakFrameReceiveRate_Object = MibTableColumn
lpEthernetPortPeakFrameReceiveRate = _LpEthernetPortPeakFrameReceiveRate_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 14, 1, 1, 10),
    _LpEthernetPortPeakFrameReceiveRate_Type()
)
lpEthernetPortPeakFrameReceiveRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEthernetPortPeakFrameReceiveRate.setStatus("mandatory")
_LpEthernetPortByteTransmitRate_Type = Integer32
_LpEthernetPortByteTransmitRate_Object = MibTableColumn
lpEthernetPortByteTransmitRate = _LpEthernetPortByteTransmitRate_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 14, 1, 1, 11),
    _LpEthernetPortByteTransmitRate_Type()
)
lpEthernetPortByteTransmitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEthernetPortByteTransmitRate.setStatus("mandatory")
_LpEthernetPortPeakByteTransmitRate_Type = Integer32
_LpEthernetPortPeakByteTransmitRate_Object = MibTableColumn
lpEthernetPortPeakByteTransmitRate = _LpEthernetPortPeakByteTransmitRate_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 14, 1, 1, 12),
    _LpEthernetPortPeakByteTransmitRate_Type()
)
lpEthernetPortPeakByteTransmitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEthernetPortPeakByteTransmitRate.setStatus("mandatory")
_LpEthernetPortFrameTransmitRate_Type = Integer32
_LpEthernetPortFrameTransmitRate_Object = MibTableColumn
lpEthernetPortFrameTransmitRate = _LpEthernetPortFrameTransmitRate_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 14, 1, 1, 13),
    _LpEthernetPortFrameTransmitRate_Type()
)
lpEthernetPortFrameTransmitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEthernetPortFrameTransmitRate.setStatus("mandatory")
_LpEthernetPortPeakFrameTransmitRate_Type = Integer32
_LpEthernetPortPeakFrameTransmitRate_Object = MibTableColumn
lpEthernetPortPeakFrameTransmitRate = _LpEthernetPortPeakFrameTransmitRate_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 14, 1, 1, 14),
    _LpEthernetPortPeakFrameTransmitRate_Type()
)
lpEthernetPortPeakFrameTransmitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEthernetPortPeakFrameTransmitRate.setStatus("mandatory")
_LpEthernetPortReceiveMulticastThreshold_Type = Integer32
_LpEthernetPortReceiveMulticastThreshold_Object = MibTableColumn
lpEthernetPortReceiveMulticastThreshold = _LpEthernetPortReceiveMulticastThreshold_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 14, 1, 1, 15),
    _LpEthernetPortReceiveMulticastThreshold_Type()
)
lpEthernetPortReceiveMulticastThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpEthernetPortReceiveMulticastThreshold.setStatus("deprecated")


class _LpEthernetPortType_Type(Integer32):
    """Custom type lpEthernetPortType based on Integer32"""
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
        *(("aui", 4),
          ("foirl", 3),
          ("other", 5),
          ("rj4510BaseT", 2),
          ("telco10BaseT", 1))
    )


_LpEthernetPortType_Type.__name__ = "Integer32"
_LpEthernetPortType_Object = MibTableColumn
lpEthernetPortType = _LpEthernetPortType_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 14, 1, 1, 16),
    _LpEthernetPortType_Type()
)
lpEthernetPortType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpEthernetPortType.setStatus("mandatory")
_LpFddiPort_ObjectIdentity = ObjectIdentity
lpFddiPort = _LpFddiPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 15)
)
_LpFddiPortTable_Object = MibTable
lpFddiPortTable = _LpFddiPortTable_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 15, 1)
)
if mibBuilder.loadTexts:
    lpFddiPortTable.setStatus("mandatory")
_LpFddiPortEntry_Object = MibTableRow
lpFddiPortEntry = _LpFddiPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 15, 1, 1)
)
lpFddiPortEntry.setIndexNames(
    (0, "LANPLEX-MIB-1-2-9", "lpFddiPortIndex"),
)
if mibBuilder.loadTexts:
    lpFddiPortEntry.setStatus("mandatory")
_LpFddiPortIndex_Type = Integer32
_LpFddiPortIndex_Object = MibTableColumn
lpFddiPortIndex = _LpFddiPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 15, 1, 1, 1),
    _LpFddiPortIndex_Type()
)
lpFddiPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpFddiPortIndex.setStatus("mandatory")
_LpFddiPortSlotIndex_Type = Integer32
_LpFddiPortSlotIndex_Object = MibTableColumn
lpFddiPortSlotIndex = _LpFddiPortSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 15, 1, 1, 2),
    _LpFddiPortSlotIndex_Type()
)
lpFddiPortSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpFddiPortSlotIndex.setStatus("mandatory")
_LpFddiPortLocalIndex_Type = Integer32
_LpFddiPortLocalIndex_Object = MibTableColumn
lpFddiPortLocalIndex = _LpFddiPortLocalIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 15, 1, 1, 3),
    _LpFddiPortLocalIndex_Type()
)
lpFddiPortLocalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpFddiPortLocalIndex.setStatus("mandatory")


class _LpFddiPortLabel_Type(DisplayString):
    """Custom type lpFddiPortLabel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LpFddiPortLabel_Type.__name__ = "DisplayString"
_LpFddiPortLabel_Object = MibTableColumn
lpFddiPortLabel = _LpFddiPortLabel_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 15, 1, 1, 4),
    _LpFddiPortLabel_Type()
)
lpFddiPortLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpFddiPortLabel.setStatus("mandatory")
_LpExpress_ObjectIdentity = ObjectIdentity
lpExpress = _LpExpress_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 16)
)
_LpExpressTable_Object = MibTable
lpExpressTable = _LpExpressTable_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 16, 1)
)
if mibBuilder.loadTexts:
    lpExpressTable.setStatus("deprecated")
_LpExpressEntry_Object = MibTableRow
lpExpressEntry = _LpExpressEntry_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 16, 1, 1)
)
lpExpressEntry.setIndexNames(
    (0, "LANPLEX-MIB-1-2-9", "lpExpressIndex"),
)
if mibBuilder.loadTexts:
    lpExpressEntry.setStatus("deprecated")
_LpExpressIndex_Type = Integer32
_LpExpressIndex_Object = MibTableColumn
lpExpressIndex = _LpExpressIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 16, 1, 1, 1),
    _LpExpressIndex_Type()
)
lpExpressIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpExpressIndex.setStatus("deprecated")
_LpExpressSlotIndex_Type = Integer32
_LpExpressSlotIndex_Object = MibTableColumn
lpExpressSlotIndex = _LpExpressSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 16, 1, 1, 2),
    _LpExpressSlotIndex_Type()
)
lpExpressSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpExpressSlotIndex.setStatus("deprecated")
_LpExpressLocalIndex_Type = Integer32
_LpExpressLocalIndex_Object = MibTableColumn
lpExpressLocalIndex = _LpExpressLocalIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 16, 1, 1, 3),
    _LpExpressLocalIndex_Type()
)
lpExpressLocalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpExpressLocalIndex.setStatus("deprecated")
_LpExpressAddressThreshold_Type = Integer32
_LpExpressAddressThreshold_Object = MibTableColumn
lpExpressAddressThreshold = _LpExpressAddressThreshold_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 16, 1, 1, 4),
    _LpExpressAddressThreshold_Type()
)
lpExpressAddressThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpExpressAddressThreshold.setStatus("deprecated")
_LpExpressFddiPort_ObjectIdentity = ObjectIdentity
lpExpressFddiPort = _LpExpressFddiPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 17)
)
_LpExpressFddiPortTable_Object = MibTable
lpExpressFddiPortTable = _LpExpressFddiPortTable_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 17, 1)
)
if mibBuilder.loadTexts:
    lpExpressFddiPortTable.setStatus("deprecated")
_LpExpressFddiPortEntry_Object = MibTableRow
lpExpressFddiPortEntry = _LpExpressFddiPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 17, 1, 1)
)
lpExpressFddiPortEntry.setIndexNames(
    (0, "LANPLEX-MIB-1-2-9", "lpExpressFddiPortIndex"),
)
if mibBuilder.loadTexts:
    lpExpressFddiPortEntry.setStatus("deprecated")
_LpExpressFddiPortIndex_Type = Integer32
_LpExpressFddiPortIndex_Object = MibTableColumn
lpExpressFddiPortIndex = _LpExpressFddiPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 17, 1, 1, 1),
    _LpExpressFddiPortIndex_Type()
)
lpExpressFddiPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpExpressFddiPortIndex.setStatus("deprecated")
_LpExpressFddiPortSlotIndex_Type = Integer32
_LpExpressFddiPortSlotIndex_Object = MibTableColumn
lpExpressFddiPortSlotIndex = _LpExpressFddiPortSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 17, 1, 1, 2),
    _LpExpressFddiPortSlotIndex_Type()
)
lpExpressFddiPortSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpExpressFddiPortSlotIndex.setStatus("deprecated")
_LpExpressFddiPortLocalIndex_Type = Integer32
_LpExpressFddiPortLocalIndex_Object = MibTableColumn
lpExpressFddiPortLocalIndex = _LpExpressFddiPortLocalIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 17, 1, 1, 3),
    _LpExpressFddiPortLocalIndex_Type()
)
lpExpressFddiPortLocalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpExpressFddiPortLocalIndex.setStatus("deprecated")
_LpExpressFddiPortForwardedCts_Type = Counter32
_LpExpressFddiPortForwardedCts_Object = MibTableColumn
lpExpressFddiPortForwardedCts = _LpExpressFddiPortForwardedCts_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 17, 1, 1, 4),
    _LpExpressFddiPortForwardedCts_Type()
)
lpExpressFddiPortForwardedCts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpExpressFddiPortForwardedCts.setStatus("deprecated")
_LpExpressFddiPortDroppedCts_Type = Counter32
_LpExpressFddiPortDroppedCts_Object = MibTableColumn
lpExpressFddiPortDroppedCts = _LpExpressFddiPortDroppedCts_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 17, 1, 1, 5),
    _LpExpressFddiPortDroppedCts_Type()
)
lpExpressFddiPortDroppedCts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpExpressFddiPortDroppedCts.setStatus("deprecated")
_LpExpressEthernetPort_ObjectIdentity = ObjectIdentity
lpExpressEthernetPort = _LpExpressEthernetPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 18)
)
_LpExpressEthernetPortTable_Object = MibTable
lpExpressEthernetPortTable = _LpExpressEthernetPortTable_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 18, 1)
)
if mibBuilder.loadTexts:
    lpExpressEthernetPortTable.setStatus("deprecated")
_LpExpressEthernetPortEntry_Object = MibTableRow
lpExpressEthernetPortEntry = _LpExpressEthernetPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 18, 1, 1)
)
lpExpressEthernetPortEntry.setIndexNames(
    (0, "LANPLEX-MIB-1-2-9", "lpExpressEthernetPortIndex"),
)
if mibBuilder.loadTexts:
    lpExpressEthernetPortEntry.setStatus("deprecated")
_LpExpressEthernetPortIndex_Type = Integer32
_LpExpressEthernetPortIndex_Object = MibTableColumn
lpExpressEthernetPortIndex = _LpExpressEthernetPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 18, 1, 1, 1),
    _LpExpressEthernetPortIndex_Type()
)
lpExpressEthernetPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpExpressEthernetPortIndex.setStatus("deprecated")
_LpExpressEthernetPortSlotIndex_Type = Integer32
_LpExpressEthernetPortSlotIndex_Object = MibTableColumn
lpExpressEthernetPortSlotIndex = _LpExpressEthernetPortSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 18, 1, 1, 2),
    _LpExpressEthernetPortSlotIndex_Type()
)
lpExpressEthernetPortSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpExpressEthernetPortSlotIndex.setStatus("deprecated")
_LpExpressEthernetPortLocalIndex_Type = Integer32
_LpExpressEthernetPortLocalIndex_Object = MibTableColumn
lpExpressEthernetPortLocalIndex = _LpExpressEthernetPortLocalIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 18, 1, 1, 3),
    _LpExpressEthernetPortLocalIndex_Type()
)
lpExpressEthernetPortLocalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpExpressEthernetPortLocalIndex.setStatus("deprecated")
_LpExpressEthernetPortForwardedCts_Type = Counter32
_LpExpressEthernetPortForwardedCts_Object = MibTableColumn
lpExpressEthernetPortForwardedCts = _LpExpressEthernetPortForwardedCts_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 18, 1, 1, 4),
    _LpExpressEthernetPortForwardedCts_Type()
)
lpExpressEthernetPortForwardedCts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpExpressEthernetPortForwardedCts.setStatus("deprecated")
_LpExpressEthernetPortDroppedCts_Type = Counter32
_LpExpressEthernetPortDroppedCts_Object = MibTableColumn
lpExpressEthernetPortDroppedCts = _LpExpressEthernetPortDroppedCts_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 18, 1, 1, 5),
    _LpExpressEthernetPortDroppedCts_Type()
)
lpExpressEthernetPortDroppedCts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpExpressEthernetPortDroppedCts.setStatus("deprecated")
_LpExpressEthernetPortUTurnCts_Type = Counter32
_LpExpressEthernetPortUTurnCts_Object = MibTableColumn
lpExpressEthernetPortUTurnCts = _LpExpressEthernetPortUTurnCts_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 18, 1, 1, 6),
    _LpExpressEthernetPortUTurnCts_Type()
)
lpExpressEthernetPortUTurnCts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpExpressEthernetPortUTurnCts.setStatus("deprecated")


class _LpExpressEthernetPortAction_Type(Integer32):
    """Custom type lpExpressEthernetPortAction based on Integer32"""
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


_LpExpressEthernetPortAction_Type.__name__ = "Integer32"
_LpExpressEthernetPortAction_Object = MibTableColumn
lpExpressEthernetPortAction = _LpExpressEthernetPortAction_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 18, 1, 1, 7),
    _LpExpressEthernetPortAction_Type()
)
lpExpressEthernetPortAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpExpressEthernetPortAction.setStatus("deprecated")
_LpExpressEthernetPortAddress_ObjectIdentity = ObjectIdentity
lpExpressEthernetPortAddress = _LpExpressEthernetPortAddress_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 19)
)
_LpExpressEthernetPortAddressTable_Object = MibTable
lpExpressEthernetPortAddressTable = _LpExpressEthernetPortAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 19, 1)
)
if mibBuilder.loadTexts:
    lpExpressEthernetPortAddressTable.setStatus("deprecated")
_LpExpressEthernetPortAddressEntry_Object = MibTableRow
lpExpressEthernetPortAddressEntry = _LpExpressEthernetPortAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 19, 1, 1)
)
lpExpressEthernetPortAddressEntry.setIndexNames(
    (0, "LANPLEX-MIB-1-2-9", "lpExpressEthernetPortAddressPortIndex"),
    (0, "LANPLEX-MIB-1-2-9", "lpExpressEthernetPortAddressIndex"),
)
if mibBuilder.loadTexts:
    lpExpressEthernetPortAddressEntry.setStatus("deprecated")
_LpExpressEthernetPortAddressPortIndex_Type = Integer32
_LpExpressEthernetPortAddressPortIndex_Object = MibTableColumn
lpExpressEthernetPortAddressPortIndex = _LpExpressEthernetPortAddressPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 19, 1, 1, 1),
    _LpExpressEthernetPortAddressPortIndex_Type()
)
lpExpressEthernetPortAddressPortIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpExpressEthernetPortAddressPortIndex.setStatus("deprecated")
_LpExpressEthernetPortAddressIndex_Type = Integer32
_LpExpressEthernetPortAddressIndex_Object = MibTableColumn
lpExpressEthernetPortAddressIndex = _LpExpressEthernetPortAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 19, 1, 1, 2),
    _LpExpressEthernetPortAddressIndex_Type()
)
lpExpressEthernetPortAddressIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpExpressEthernetPortAddressIndex.setStatus("deprecated")
_LpExpressEthernetPortAddressSlotIndex_Type = Integer32
_LpExpressEthernetPortAddressSlotIndex_Object = MibTableColumn
lpExpressEthernetPortAddressSlotIndex = _LpExpressEthernetPortAddressSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 19, 1, 1, 3),
    _LpExpressEthernetPortAddressSlotIndex_Type()
)
lpExpressEthernetPortAddressSlotIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpExpressEthernetPortAddressSlotIndex.setStatus("deprecated")


class _LpExpressEthernetPortAddressType_Type(Integer32):
    """Custom type lpExpressEthernetPortAddressType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("other", 1))
    )


_LpExpressEthernetPortAddressType_Type.__name__ = "Integer32"
_LpExpressEthernetPortAddressType_Object = MibTableColumn
lpExpressEthernetPortAddressType = _LpExpressEthernetPortAddressType_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 19, 1, 1, 4),
    _LpExpressEthernetPortAddressType_Type()
)
lpExpressEthernetPortAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpExpressEthernetPortAddressType.setStatus("deprecated")


class _LpExpressEthernetPortAddressRemoteAddress_Type(OctetString):
    """Custom type lpExpressEthernetPortAddressRemoteAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_LpExpressEthernetPortAddressRemoteAddress_Type.__name__ = "OctetString"
_LpExpressEthernetPortAddressRemoteAddress_Object = MibTableColumn
lpExpressEthernetPortAddressRemoteAddress = _LpExpressEthernetPortAddressRemoteAddress_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 19, 1, 1, 5),
    _LpExpressEthernetPortAddressRemoteAddress_Type()
)
lpExpressEthernetPortAddressRemoteAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpExpressEthernetPortAddressRemoteAddress.setStatus("deprecated")


class _LpExpressEthernetPortAddressIsStatic_Type(Integer32):
    """Custom type lpExpressEthernetPortAddressIsStatic based on Integer32"""
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


_LpExpressEthernetPortAddressIsStatic_Type.__name__ = "Integer32"
_LpExpressEthernetPortAddressIsStatic_Object = MibTableColumn
lpExpressEthernetPortAddressIsStatic = _LpExpressEthernetPortAddressIsStatic_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 19, 1, 1, 6),
    _LpExpressEthernetPortAddressIsStatic_Type()
)
lpExpressEthernetPortAddressIsStatic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpExpressEthernetPortAddressIsStatic.setStatus("deprecated")
_LpExpressEthernetPortAddressStaticPort_Type = Integer32
_LpExpressEthernetPortAddressStaticPort_Object = MibTableColumn
lpExpressEthernetPortAddressStaticPort = _LpExpressEthernetPortAddressStaticPort_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 19, 1, 1, 7),
    _LpExpressEthernetPortAddressStaticPort_Type()
)
lpExpressEthernetPortAddressStaticPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpExpressEthernetPortAddressStaticPort.setStatus("deprecated")
_LpExpressEthernetPortAddressAge_Type = Integer32
_LpExpressEthernetPortAddressAge_Object = MibTableColumn
lpExpressEthernetPortAddressAge = _LpExpressEthernetPortAddressAge_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 19, 1, 1, 8),
    _LpExpressEthernetPortAddressAge_Type()
)
lpExpressEthernetPortAddressAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpExpressEthernetPortAddressAge.setStatus("deprecated")
_LpPowerSupply_ObjectIdentity = ObjectIdentity
lpPowerSupply = _LpPowerSupply_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 20)
)
_LpPowerSupplyTable_Object = MibTable
lpPowerSupplyTable = _LpPowerSupplyTable_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 20, 1)
)
if mibBuilder.loadTexts:
    lpPowerSupplyTable.setStatus("mandatory")
_LpPowerSupplyEntry_Object = MibTableRow
lpPowerSupplyEntry = _LpPowerSupplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 20, 1, 1)
)
lpPowerSupplyEntry.setIndexNames(
    (0, "LANPLEX-MIB-1-2-9", "lpPowerSupplyIndex"),
)
if mibBuilder.loadTexts:
    lpPowerSupplyEntry.setStatus("mandatory")
_LpPowerSupplyIndex_Type = Integer32
_LpPowerSupplyIndex_Object = MibTableColumn
lpPowerSupplyIndex = _LpPowerSupplyIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 20, 1, 1, 1),
    _LpPowerSupplyIndex_Type()
)
lpPowerSupplyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpPowerSupplyIndex.setStatus("mandatory")
_LpPowerSupplyLocation_Type = Integer32
_LpPowerSupplyLocation_Object = MibTableColumn
lpPowerSupplyLocation = _LpPowerSupplyLocation_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 20, 1, 1, 2),
    _LpPowerSupplyLocation_Type()
)
lpPowerSupplyLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpPowerSupplyLocation.setStatus("mandatory")
_LpPowerSupplyStatus_Type = Integer32
_LpPowerSupplyStatus_Object = MibTableColumn
lpPowerSupplyStatus = _LpPowerSupplyStatus_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 20, 1, 1, 3),
    _LpPowerSupplyStatus_Type()
)
lpPowerSupplyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpPowerSupplyStatus.setStatus("mandatory")


class _LpPowerSupplyFailureType_Type(Integer32):
    """Custom type lpPowerSupplyFailureType based on Integer32"""
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
        *(("systemAcFailure", 1),
          ("systemOverTemperatureFailure", 4),
          ("systemPlus12Failure", 3),
          ("systemPlus5Failure", 2))
    )


_LpPowerSupplyFailureType_Type.__name__ = "Integer32"
_LpPowerSupplyFailureType_Object = MibTableColumn
lpPowerSupplyFailureType = _LpPowerSupplyFailureType_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 20, 1, 1, 4),
    _LpPowerSupplyFailureType_Type()
)
lpPowerSupplyFailureType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpPowerSupplyFailureType.setStatus("deprecated")


class _LpPowerSupplyLastFailure_Type(Integer32):
    """Custom type lpPowerSupplyLastFailure based on Integer32"""
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
        *(("none", 5),
          ("systemAcFailure", 1),
          ("systemOverTemperatureFailure", 4),
          ("systemPlus12Failure", 3),
          ("systemPlus5Failure", 2))
    )


_LpPowerSupplyLastFailure_Type.__name__ = "Integer32"
_LpPowerSupplyLastFailure_Object = MibTableColumn
lpPowerSupplyLastFailure = _LpPowerSupplyLastFailure_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 20, 1, 1, 5),
    _LpPowerSupplyLastFailure_Type()
)
lpPowerSupplyLastFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpPowerSupplyLastFailure.setStatus("mandatory")
_LpBridge_ObjectIdentity = ObjectIdentity
lpBridge = _LpBridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 21)
)
_LpBridgeTable_Object = MibTable
lpBridgeTable = _LpBridgeTable_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 21, 1)
)
if mibBuilder.loadTexts:
    lpBridgeTable.setStatus("mandatory")
_LpBridgeEntry_Object = MibTableRow
lpBridgeEntry = _LpBridgeEntry_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 21, 1, 1)
)
lpBridgeEntry.setIndexNames(
    (0, "LANPLEX-MIB-1-2-9", "lpBridgeIndex"),
)
if mibBuilder.loadTexts:
    lpBridgeEntry.setStatus("mandatory")
_LpBridgeIndex_Type = Integer32
_LpBridgeIndex_Object = MibTableColumn
lpBridgeIndex = _LpBridgeIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 21, 1, 1, 1),
    _LpBridgeIndex_Type()
)
lpBridgeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpBridgeIndex.setStatus("mandatory")
_LpBridgeBaseSlotIndex_Type = Integer32
_LpBridgeBaseSlotIndex_Object = MibTableColumn
lpBridgeBaseSlotIndex = _LpBridgeBaseSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 21, 1, 1, 2),
    _LpBridgeBaseSlotIndex_Type()
)
lpBridgeBaseSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpBridgeBaseSlotIndex.setStatus("mandatory")
_LpBridgePortCount_Type = Integer32
_LpBridgePortCount_Object = MibTableColumn
lpBridgePortCount = _LpBridgePortCount_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 21, 1, 1, 3),
    _LpBridgePortCount_Type()
)
lpBridgePortCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpBridgePortCount.setStatus("mandatory")
_LpBridgeAddressTableSize_Type = Integer32
_LpBridgeAddressTableSize_Object = MibTableColumn
lpBridgeAddressTableSize = _LpBridgeAddressTableSize_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 21, 1, 1, 4),
    _LpBridgeAddressTableSize_Type()
)
lpBridgeAddressTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpBridgeAddressTableSize.setStatus("mandatory")
_LpBridgeAddressThreshold_Type = Integer32
_LpBridgeAddressThreshold_Object = MibTableColumn
lpBridgeAddressThreshold = _LpBridgeAddressThreshold_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 21, 1, 1, 5),
    _LpBridgeAddressThreshold_Type()
)
lpBridgeAddressThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpBridgeAddressThreshold.setStatus("mandatory")


class _LpBridgeMode_Type(Integer32):
    """Custom type lpBridgeMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("expressMode", 1),
          ("ieee8021dBridgeMode", 2),
          ("notSupported", 3))
    )


_LpBridgeMode_Type.__name__ = "Integer32"
_LpBridgeMode_Object = MibTableColumn
lpBridgeMode = _LpBridgeMode_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 21, 1, 1, 6),
    _LpBridgeMode_Type()
)
lpBridgeMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpBridgeMode.setStatus("mandatory")
_LpBridgeLocalIndex_Type = Integer32
_LpBridgeLocalIndex_Object = MibTableColumn
lpBridgeLocalIndex = _LpBridgeLocalIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 21, 1, 1, 7),
    _LpBridgeLocalIndex_Type()
)
lpBridgeLocalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpBridgeLocalIndex.setStatus("mandatory")
_LpBridgePortTable_Object = MibTable
lpBridgePortTable = _LpBridgePortTable_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 21, 2)
)
if mibBuilder.loadTexts:
    lpBridgePortTable.setStatus("mandatory")
_LpBridgePortEntry_Object = MibTableRow
lpBridgePortEntry = _LpBridgePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 21, 2, 1)
)
lpBridgePortEntry.setIndexNames(
    (0, "LANPLEX-MIB-1-2-9", "lpBridgePortBridgeIndex"),
    (0, "LANPLEX-MIB-1-2-9", "lpBridgePortIndex"),
)
if mibBuilder.loadTexts:
    lpBridgePortEntry.setStatus("mandatory")
_LpBridgePortBridgeIndex_Type = Integer32
_LpBridgePortBridgeIndex_Object = MibTableColumn
lpBridgePortBridgeIndex = _LpBridgePortBridgeIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 21, 2, 1, 1),
    _LpBridgePortBridgeIndex_Type()
)
lpBridgePortBridgeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpBridgePortBridgeIndex.setStatus("mandatory")
_LpBridgePortIndex_Type = Integer32
_LpBridgePortIndex_Object = MibTableColumn
lpBridgePortIndex = _LpBridgePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 21, 2, 1, 2),
    _LpBridgePortIndex_Type()
)
lpBridgePortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpBridgePortIndex.setStatus("mandatory")
_LpBridgePortSlotIndex_Type = Integer32
_LpBridgePortSlotIndex_Object = MibTableColumn
lpBridgePortSlotIndex = _LpBridgePortSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 21, 2, 1, 3),
    _LpBridgePortSlotIndex_Type()
)
lpBridgePortSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpBridgePortSlotIndex.setStatus("mandatory")
_LpBridgePortLocalIndex_Type = Integer32
_LpBridgePortLocalIndex_Object = MibTableColumn
lpBridgePortLocalIndex = _LpBridgePortLocalIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 21, 2, 1, 4),
    _LpBridgePortLocalIndex_Type()
)
lpBridgePortLocalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpBridgePortLocalIndex.setStatus("mandatory")


class _LpBridgePortType_Type(Integer32):
    """Custom type lpBridgePortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ethernet", 1),
          ("fddi", 2),
          ("other", 3))
    )


_LpBridgePortType_Type.__name__ = "Integer32"
_LpBridgePortType_Object = MibTableColumn
lpBridgePortType = _LpBridgePortType_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 21, 2, 1, 5),
    _LpBridgePortType_Type()
)
lpBridgePortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpBridgePortType.setStatus("mandatory")


class _LpBridgePortIpFragmentationEnabled_Type(Integer32):
    """Custom type lpBridgePortIpFragmentationEnabled based on Integer32"""
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


_LpBridgePortIpFragmentationEnabled_Type.__name__ = "Integer32"
_LpBridgePortIpFragmentationEnabled_Object = MibTableColumn
lpBridgePortIpFragmentationEnabled = _LpBridgePortIpFragmentationEnabled_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 21, 2, 1, 6),
    _LpBridgePortIpFragmentationEnabled_Type()
)
lpBridgePortIpFragmentationEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpBridgePortIpFragmentationEnabled.setStatus("mandatory")


class _LpBridgePortReceiveMulticastLimit_Type(Integer32):
    """Custom type lpBridgePortReceiveMulticastLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_LpBridgePortReceiveMulticastLimit_Type.__name__ = "Integer32"
_LpBridgePortReceiveMulticastLimit_Object = MibTableColumn
lpBridgePortReceiveMulticastLimit = _LpBridgePortReceiveMulticastLimit_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 21, 2, 1, 7),
    _LpBridgePortReceiveMulticastLimit_Type()
)
lpBridgePortReceiveMulticastLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpBridgePortReceiveMulticastLimit.setStatus("mandatory")


class _LpBridgePortAddressAction_Type(Integer32):
    """Custom type lpBridgePortAddressAction based on Integer32"""
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


_LpBridgePortAddressAction_Type.__name__ = "Integer32"
_LpBridgePortAddressAction_Object = MibTableColumn
lpBridgePortAddressAction = _LpBridgePortAddressAction_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 21, 2, 1, 8),
    _LpBridgePortAddressAction_Type()
)
lpBridgePortAddressAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpBridgePortAddressAction.setStatus("mandatory")
_LpBridgePortTotalForwardedCts_Type = Counter32
_LpBridgePortTotalForwardedCts_Object = MibTableColumn
lpBridgePortTotalForwardedCts = _LpBridgePortTotalForwardedCts_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 21, 2, 1, 9),
    _LpBridgePortTotalForwardedCts_Type()
)
lpBridgePortTotalForwardedCts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpBridgePortTotalForwardedCts.setStatus("mandatory")
_LpBridgePortManagementFramesReceived_Type = Counter32
_LpBridgePortManagementFramesReceived_Object = MibTableColumn
lpBridgePortManagementFramesReceived = _LpBridgePortManagementFramesReceived_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 21, 2, 1, 10),
    _LpBridgePortManagementFramesReceived_Type()
)
lpBridgePortManagementFramesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpBridgePortManagementFramesReceived.setStatus("mandatory")
_LpBridgePortTotalDiscards_Type = Counter32
_LpBridgePortTotalDiscards_Object = MibTableColumn
lpBridgePortTotalDiscards = _LpBridgePortTotalDiscards_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 21, 2, 1, 11),
    _LpBridgePortTotalDiscards_Type()
)
lpBridgePortTotalDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpBridgePortTotalDiscards.setStatus("mandatory")
_LpBridgePortReceiveBlockedDiscards_Type = Counter32
_LpBridgePortReceiveBlockedDiscards_Object = MibTableColumn
lpBridgePortReceiveBlockedDiscards = _LpBridgePortReceiveBlockedDiscards_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 21, 2, 1, 12),
    _LpBridgePortReceiveBlockedDiscards_Type()
)
lpBridgePortReceiveBlockedDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpBridgePortReceiveBlockedDiscards.setStatus("mandatory")
_LpBridgePortReceiveMulticastLimitExceededs_Type = Counter32
_LpBridgePortReceiveMulticastLimitExceededs_Object = MibTableColumn
lpBridgePortReceiveMulticastLimitExceededs = _LpBridgePortReceiveMulticastLimitExceededs_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 21, 2, 1, 13),
    _LpBridgePortReceiveMulticastLimitExceededs_Type()
)
lpBridgePortReceiveMulticastLimitExceededs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpBridgePortReceiveMulticastLimitExceededs.setStatus("mandatory")
_LpBridgePortReceiveSecurityDiscards_Type = Counter32
_LpBridgePortReceiveSecurityDiscards_Object = MibTableColumn
lpBridgePortReceiveSecurityDiscards = _LpBridgePortReceiveSecurityDiscards_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 21, 2, 1, 14),
    _LpBridgePortReceiveSecurityDiscards_Type()
)
lpBridgePortReceiveSecurityDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpBridgePortReceiveSecurityDiscards.setStatus("mandatory")
_LpBridgePortReceiveUnknownDiscards_Type = Counter32
_LpBridgePortReceiveUnknownDiscards_Object = MibTableColumn
lpBridgePortReceiveUnknownDiscards = _LpBridgePortReceiveUnknownDiscards_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 21, 2, 1, 15),
    _LpBridgePortReceiveUnknownDiscards_Type()
)
lpBridgePortReceiveUnknownDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpBridgePortReceiveUnknownDiscards.setStatus("mandatory")
_LpBridgePortReceiveOtherDiscards_Type = Counter32
_LpBridgePortReceiveOtherDiscards_Object = MibTableColumn
lpBridgePortReceiveOtherDiscards = _LpBridgePortReceiveOtherDiscards_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 21, 2, 1, 16),
    _LpBridgePortReceiveOtherDiscards_Type()
)
lpBridgePortReceiveOtherDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpBridgePortReceiveOtherDiscards.setStatus("mandatory")
_LpBridgePortReceiveErrorDiscards_Type = Counter32
_LpBridgePortReceiveErrorDiscards_Object = MibTableColumn
lpBridgePortReceiveErrorDiscards = _LpBridgePortReceiveErrorDiscards_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 21, 2, 1, 17),
    _LpBridgePortReceiveErrorDiscards_Type()
)
lpBridgePortReceiveErrorDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpBridgePortReceiveErrorDiscards.setStatus("mandatory")
_LpBridgePortSameSegmentDiscards_Type = Counter32
_LpBridgePortSameSegmentDiscards_Object = MibTableColumn
lpBridgePortSameSegmentDiscards = _LpBridgePortSameSegmentDiscards_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 21, 2, 1, 18),
    _LpBridgePortSameSegmentDiscards_Type()
)
lpBridgePortSameSegmentDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpBridgePortSameSegmentDiscards.setStatus("mandatory")
_LpBridgePortTransmitBlockedDiscards_Type = Counter32
_LpBridgePortTransmitBlockedDiscards_Object = MibTableColumn
lpBridgePortTransmitBlockedDiscards = _LpBridgePortTransmitBlockedDiscards_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 21, 2, 1, 19),
    _LpBridgePortTransmitBlockedDiscards_Type()
)
lpBridgePortTransmitBlockedDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpBridgePortTransmitBlockedDiscards.setStatus("mandatory")
_LpBridgePortTotalFiltered_Type = Counter32
_LpBridgePortTotalFiltered_Object = MibTableColumn
lpBridgePortTotalFiltered = _LpBridgePortTotalFiltered_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 21, 2, 1, 20),
    _LpBridgePortTotalFiltered_Type()
)
lpBridgePortTotalFiltered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpBridgePortTotalFiltered.setStatus("mandatory")
_LpBridgePortReceiveUnicastFiltered_Type = Counter32
_LpBridgePortReceiveUnicastFiltered_Object = MibTableColumn
lpBridgePortReceiveUnicastFiltered = _LpBridgePortReceiveUnicastFiltered_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 21, 2, 1, 21),
    _LpBridgePortReceiveUnicastFiltered_Type()
)
lpBridgePortReceiveUnicastFiltered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpBridgePortReceiveUnicastFiltered.setStatus("mandatory")
_LpBridgePortReceiveMulticastFiltered_Type = Counter32
_LpBridgePortReceiveMulticastFiltered_Object = MibTableColumn
lpBridgePortReceiveMulticastFiltered = _LpBridgePortReceiveMulticastFiltered_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 21, 2, 1, 22),
    _LpBridgePortReceiveMulticastFiltered_Type()
)
lpBridgePortReceiveMulticastFiltered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpBridgePortReceiveMulticastFiltered.setStatus("mandatory")
_LpBridgePortTransmitUnicastFiltered_Type = Counter32
_LpBridgePortTransmitUnicastFiltered_Object = MibTableColumn
lpBridgePortTransmitUnicastFiltered = _LpBridgePortTransmitUnicastFiltered_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 21, 2, 1, 23),
    _LpBridgePortTransmitUnicastFiltered_Type()
)
lpBridgePortTransmitUnicastFiltered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpBridgePortTransmitUnicastFiltered.setStatus("mandatory")
_LpBridgePortTransmitMulticastFiltered_Type = Counter32
_LpBridgePortTransmitMulticastFiltered_Object = MibTableColumn
lpBridgePortTransmitMulticastFiltered = _LpBridgePortTransmitMulticastFiltered_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 21, 2, 1, 24),
    _LpBridgePortTransmitMulticastFiltered_Type()
)
lpBridgePortTransmitMulticastFiltered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpBridgePortTransmitMulticastFiltered.setStatus("mandatory")
_LpBridgePortReceiveMulticastLimitExceededCount_Type = Counter32
_LpBridgePortReceiveMulticastLimitExceededCount_Object = MibTableColumn
lpBridgePortReceiveMulticastLimitExceededCount = _LpBridgePortReceiveMulticastLimitExceededCount_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 21, 2, 1, 25),
    _LpBridgePortReceiveMulticastLimitExceededCount_Type()
)
lpBridgePortReceiveMulticastLimitExceededCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpBridgePortReceiveMulticastLimitExceededCount.setStatus("mandatory")
_LpBridgePortForwardedToTable_Object = MibTable
lpBridgePortForwardedToTable = _LpBridgePortForwardedToTable_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 21, 3)
)
if mibBuilder.loadTexts:
    lpBridgePortForwardedToTable.setStatus("mandatory")
_LpBridgePortForwardedToEntry_Object = MibTableRow
lpBridgePortForwardedToEntry = _LpBridgePortForwardedToEntry_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 21, 3, 1)
)
lpBridgePortForwardedToEntry.setIndexNames(
    (0, "LANPLEX-MIB-1-2-9", "lpBridgePortForwardedToBridgeIndex"),
    (0, "LANPLEX-MIB-1-2-9", "lpBridgePortForwardedToReceivePortIndex"),
    (0, "LANPLEX-MIB-1-2-9", "lpBridgePortForwardedToDstPortIndex"),
)
if mibBuilder.loadTexts:
    lpBridgePortForwardedToEntry.setStatus("mandatory")
_LpBridgePortForwardedToBridgeIndex_Type = Integer32
_LpBridgePortForwardedToBridgeIndex_Object = MibTableColumn
lpBridgePortForwardedToBridgeIndex = _LpBridgePortForwardedToBridgeIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 21, 3, 1, 1),
    _LpBridgePortForwardedToBridgeIndex_Type()
)
lpBridgePortForwardedToBridgeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpBridgePortForwardedToBridgeIndex.setStatus("mandatory")
_LpBridgePortForwardedToReceivePortIndex_Type = Integer32
_LpBridgePortForwardedToReceivePortIndex_Object = MibTableColumn
lpBridgePortForwardedToReceivePortIndex = _LpBridgePortForwardedToReceivePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 21, 3, 1, 2),
    _LpBridgePortForwardedToReceivePortIndex_Type()
)
lpBridgePortForwardedToReceivePortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpBridgePortForwardedToReceivePortIndex.setStatus("mandatory")
_LpBridgePortForwardedToDstPortIndex_Type = Integer32
_LpBridgePortForwardedToDstPortIndex_Object = MibTableColumn
lpBridgePortForwardedToDstPortIndex = _LpBridgePortForwardedToDstPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 21, 3, 1, 3),
    _LpBridgePortForwardedToDstPortIndex_Type()
)
lpBridgePortForwardedToDstPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpBridgePortForwardedToDstPortIndex.setStatus("mandatory")
_LpBridgePortForwardedToCount_Type = Counter32
_LpBridgePortForwardedToCount_Object = MibTableColumn
lpBridgePortForwardedToCount = _LpBridgePortForwardedToCount_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 21, 3, 1, 4),
    _LpBridgePortForwardedToCount_Type()
)
lpBridgePortForwardedToCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpBridgePortForwardedToCount.setStatus("mandatory")
_LpBridgePortFilteredToTable_Object = MibTable
lpBridgePortFilteredToTable = _LpBridgePortFilteredToTable_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 21, 4)
)
if mibBuilder.loadTexts:
    lpBridgePortFilteredToTable.setStatus("mandatory")
_LpBridgePortFilteredToEntry_Object = MibTableRow
lpBridgePortFilteredToEntry = _LpBridgePortFilteredToEntry_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 21, 4, 1)
)
lpBridgePortFilteredToEntry.setIndexNames(
    (0, "LANPLEX-MIB-1-2-9", "lpBridgePortFilteredToBridgeIndex"),
    (0, "LANPLEX-MIB-1-2-9", "lpBridgePortFilteredToReceivePortIndex"),
    (0, "LANPLEX-MIB-1-2-9", "lpBridgePortFilteredToDstPortIndex"),
)
if mibBuilder.loadTexts:
    lpBridgePortFilteredToEntry.setStatus("mandatory")
_LpBridgePortFilteredToBridgeIndex_Type = Integer32
_LpBridgePortFilteredToBridgeIndex_Object = MibTableColumn
lpBridgePortFilteredToBridgeIndex = _LpBridgePortFilteredToBridgeIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 21, 4, 1, 1),
    _LpBridgePortFilteredToBridgeIndex_Type()
)
lpBridgePortFilteredToBridgeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpBridgePortFilteredToBridgeIndex.setStatus("mandatory")
_LpBridgePortFilteredToReceivePortIndex_Type = Integer32
_LpBridgePortFilteredToReceivePortIndex_Object = MibTableColumn
lpBridgePortFilteredToReceivePortIndex = _LpBridgePortFilteredToReceivePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 21, 4, 1, 2),
    _LpBridgePortFilteredToReceivePortIndex_Type()
)
lpBridgePortFilteredToReceivePortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpBridgePortFilteredToReceivePortIndex.setStatus("mandatory")
_LpBridgePortFilteredToDstPortIndex_Type = Integer32
_LpBridgePortFilteredToDstPortIndex_Object = MibTableColumn
lpBridgePortFilteredToDstPortIndex = _LpBridgePortFilteredToDstPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 21, 4, 1, 3),
    _LpBridgePortFilteredToDstPortIndex_Type()
)
lpBridgePortFilteredToDstPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpBridgePortFilteredToDstPortIndex.setStatus("mandatory")
_LpBridgePortFilteredToCount_Type = Counter32
_LpBridgePortFilteredToCount_Object = MibTableColumn
lpBridgePortFilteredToCount = _LpBridgePortFilteredToCount_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 21, 4, 1, 4),
    _LpBridgePortFilteredToCount_Type()
)
lpBridgePortFilteredToCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpBridgePortFilteredToCount.setStatus("mandatory")
_LpBridgePortAddressTable_Object = MibTable
lpBridgePortAddressTable = _LpBridgePortAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 21, 5)
)
if mibBuilder.loadTexts:
    lpBridgePortAddressTable.setStatus("mandatory")
_LpBridgePortAddressEntry_Object = MibTableRow
lpBridgePortAddressEntry = _LpBridgePortAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 21, 5, 1)
)
lpBridgePortAddressEntry.setIndexNames(
    (0, "LANPLEX-MIB-1-2-9", "lpBridgePortAddressBridgeIndex"),
    (0, "LANPLEX-MIB-1-2-9", "lpBridgePortAddressPortIndex"),
    (0, "LANPLEX-MIB-1-2-9", "lpBridgePortAddressIndex"),
)
if mibBuilder.loadTexts:
    lpBridgePortAddressEntry.setStatus("mandatory")
_LpBridgePortAddressBridgeIndex_Type = Integer32
_LpBridgePortAddressBridgeIndex_Object = MibTableColumn
lpBridgePortAddressBridgeIndex = _LpBridgePortAddressBridgeIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 21, 5, 1, 1),
    _LpBridgePortAddressBridgeIndex_Type()
)
lpBridgePortAddressBridgeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpBridgePortAddressBridgeIndex.setStatus("mandatory")
_LpBridgePortAddressPortIndex_Type = Integer32
_LpBridgePortAddressPortIndex_Object = MibTableColumn
lpBridgePortAddressPortIndex = _LpBridgePortAddressPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 21, 5, 1, 2),
    _LpBridgePortAddressPortIndex_Type()
)
lpBridgePortAddressPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpBridgePortAddressPortIndex.setStatus("mandatory")
_LpBridgePortAddressIndex_Type = Integer32
_LpBridgePortAddressIndex_Object = MibTableColumn
lpBridgePortAddressIndex = _LpBridgePortAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 21, 5, 1, 3),
    _LpBridgePortAddressIndex_Type()
)
lpBridgePortAddressIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpBridgePortAddressIndex.setStatus("mandatory")


class _LpBridgePortAddressRemoteAddress_Type(OctetString):
    """Custom type lpBridgePortAddressRemoteAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_LpBridgePortAddressRemoteAddress_Type.__name__ = "OctetString"
_LpBridgePortAddressRemoteAddress_Object = MibTableColumn
lpBridgePortAddressRemoteAddress = _LpBridgePortAddressRemoteAddress_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 21, 5, 1, 4),
    _LpBridgePortAddressRemoteAddress_Type()
)
lpBridgePortAddressRemoteAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpBridgePortAddressRemoteAddress.setStatus("mandatory")


class _LpBridgePortAddressType_Type(Integer32):
    """Custom type lpBridgePortAddressType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("other", 1))
    )


_LpBridgePortAddressType_Type.__name__ = "Integer32"
_LpBridgePortAddressType_Object = MibTableColumn
lpBridgePortAddressType = _LpBridgePortAddressType_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 21, 5, 1, 5),
    _LpBridgePortAddressType_Type()
)
lpBridgePortAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpBridgePortAddressType.setStatus("mandatory")


class _LpBridgePortAddressIsStatic_Type(Integer32):
    """Custom type lpBridgePortAddressIsStatic based on Integer32"""
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


_LpBridgePortAddressIsStatic_Type.__name__ = "Integer32"
_LpBridgePortAddressIsStatic_Object = MibTableColumn
lpBridgePortAddressIsStatic = _LpBridgePortAddressIsStatic_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 21, 5, 1, 6),
    _LpBridgePortAddressIsStatic_Type()
)
lpBridgePortAddressIsStatic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpBridgePortAddressIsStatic.setStatus("mandatory")
_LpBridgePortAddressStaticPort_Type = Integer32
_LpBridgePortAddressStaticPort_Object = MibTableColumn
lpBridgePortAddressStaticPort = _LpBridgePortAddressStaticPort_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 21, 5, 1, 7),
    _LpBridgePortAddressStaticPort_Type()
)
lpBridgePortAddressStaticPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpBridgePortAddressStaticPort.setStatus("mandatory")
_LpBridgePortAddressAge_Type = Integer32
_LpBridgePortAddressAge_Object = MibTableColumn
lpBridgePortAddressAge = _LpBridgePortAddressAge_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 21, 5, 1, 8),
    _LpBridgePortAddressAge_Type()
)
lpBridgePortAddressAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpBridgePortAddressAge.setStatus("mandatory")
_LpTrapEnterprise_ObjectIdentity = ObjectIdentity
lpTrapEnterprise = _LpTrapEnterprise_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 22)
)
_LpTrapEnterpriseTable_Object = MibTable
lpTrapEnterpriseTable = _LpTrapEnterpriseTable_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 22, 1)
)
if mibBuilder.loadTexts:
    lpTrapEnterpriseTable.setStatus("mandatory")
_LpTrapEnterpriseTableEntry_Object = MibTableRow
lpTrapEnterpriseTableEntry = _LpTrapEnterpriseTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 22, 1, 1)
)
lpTrapEnterpriseTableEntry.setIndexNames(
    (0, "LANPLEX-MIB-1-2-9", "lpTrapEnterpriseIndex"),
)
if mibBuilder.loadTexts:
    lpTrapEnterpriseTableEntry.setStatus("mandatory")
_LpTrapEnterpriseIndex_Type = Integer32
_LpTrapEnterpriseIndex_Object = MibTableColumn
lpTrapEnterpriseIndex = _LpTrapEnterpriseIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 22, 1, 1, 1),
    _LpTrapEnterpriseIndex_Type()
)
lpTrapEnterpriseIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpTrapEnterpriseIndex.setStatus("mandatory")
_LpTrapEnterpriseOID_Type = ObjectIdentifier
_LpTrapEnterpriseOID_Object = MibTableColumn
lpTrapEnterpriseOID = _LpTrapEnterpriseOID_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 22, 1, 1, 2),
    _LpTrapEnterpriseOID_Type()
)
lpTrapEnterpriseOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpTrapEnterpriseOID.setStatus("mandatory")
_LpTrapDest_ObjectIdentity = ObjectIdentity
lpTrapDest = _LpTrapDest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 23)
)
_LpTrapDestTable_Object = MibTable
lpTrapDestTable = _LpTrapDestTable_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 23, 1)
)
if mibBuilder.loadTexts:
    lpTrapDestTable.setStatus("mandatory")
_LpTrapDestTableEntry_Object = MibTableRow
lpTrapDestTableEntry = _LpTrapDestTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 23, 1, 1)
)
lpTrapDestTableEntry.setIndexNames(
    (0, "LANPLEX-MIB-1-2-9", "lpTrapDestAddr"),
    (0, "LANPLEX-MIB-1-2-9", "lpTrapDestEnterpriseIndex"),
    (0, "LANPLEX-MIB-1-2-9", "lpTrapNumber"),
)
if mibBuilder.loadTexts:
    lpTrapDestTableEntry.setStatus("mandatory")
_LpTrapDestAddr_Type = IpAddress
_LpTrapDestAddr_Object = MibTableColumn
lpTrapDestAddr = _LpTrapDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 23, 1, 1, 1),
    _LpTrapDestAddr_Type()
)
lpTrapDestAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpTrapDestAddr.setStatus("mandatory")
_LpTrapDestEnterpriseIndex_Type = Integer32
_LpTrapDestEnterpriseIndex_Object = MibTableColumn
lpTrapDestEnterpriseIndex = _LpTrapDestEnterpriseIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 23, 1, 1, 2),
    _LpTrapDestEnterpriseIndex_Type()
)
lpTrapDestEnterpriseIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpTrapDestEnterpriseIndex.setStatus("mandatory")
_LpTrapNumber_Type = Integer32
_LpTrapNumber_Object = MibTableColumn
lpTrapNumber = _LpTrapNumber_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 23, 1, 1, 3),
    _LpTrapNumber_Type()
)
lpTrapNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpTrapNumber.setStatus("mandatory")


class _LpTrapEntryStatus_Type(Integer32):
    """Custom type lpTrapEntryStatus based on Integer32"""
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


_LpTrapEntryStatus_Type.__name__ = "Integer32"
_LpTrapEntryStatus_Object = MibTableColumn
lpTrapEntryStatus = _LpTrapEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 23, 1, 1, 4),
    _LpTrapEntryStatus_Type()
)
lpTrapEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpTrapEntryStatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects

lpSlotInsertEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 0, 1)
)
lpSlotInsertEvent.setObjects(
      *(("LANPLEX-MIB-1-2-9", "lpSlotIndex"),
        ("LANPLEX-MIB-1-2-9", "lpSlotBoardType"),
        ("LANPLEX-MIB-1-2-9", "lpSlotBoardRevision"))
)
if mibBuilder.loadTexts:
    lpSlotInsertEvent.setStatus(
        ""
    )

lpSlotExtractEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 0, 2)
)
lpSlotExtractEvent.setObjects(
    ("LANPLEX-MIB-1-2-9", "lpSlotIndex")
)
if mibBuilder.loadTexts:
    lpSlotExtractEvent.setStatus(
        ""
    )

lpBridgeAddressThresholdEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 0, 3)
)
lpBridgeAddressThresholdEvent.setObjects(
      *(("LANPLEX-MIB-1-2-9", "lpBridgeIndex"),
        ("LANPLEX-MIB-1-2-9", "lpBridgeBaseSlotIndex"))
)
if mibBuilder.loadTexts:
    lpBridgeAddressThresholdEvent.setStatus(
        ""
    )

lpSystemOverTemperatureEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 0, 6)
)
if mibBuilder.loadTexts:
    lpSystemOverTemperatureEvent.setStatus(
        ""
    )

lpSlotOverTemperatureEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 0, 7)
)
lpSlotOverTemperatureEvent.setObjects(
      *(("LANPLEX-MIB-1-2-9", "lpSlotIndex"),
        ("LANPLEX-MIB-1-2-9", "lpSlotBoardType"),
        ("LANPLEX-MIB-1-2-9", "lpSlotBoardRevision"),
        ("LANPLEX-MIB-1-2-9", "lpSlotBoardStatus"))
)
if mibBuilder.loadTexts:
    lpSlotOverTemperatureEvent.setStatus(
        ""
    )

lpPowerSupplyFailureEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 114, 1, 1, 0, 8)
)
lpPowerSupplyFailureEvent.setObjects(
      *(("LANPLEX-MIB-1-2-9", "lpPowerSupplyIndex"),
        ("LANPLEX-MIB-1-2-9", "lpPowerSupplyLocation"),
        ("LANPLEX-MIB-1-2-9", "lpPowerSupplyLastFailure"),
        ("LANPLEX-MIB-1-2-9", "lpSystemPowerSupplyCount"))
)
if mibBuilder.loadTexts:
    lpPowerSupplyFailureEvent.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LANPLEX-MIB-1-2-9",
    **{"synernetics": synernetics,
       "lanplex": lanplex,
       "lanplexMib": lanplexMib,
       "lpSlotInsertEvent": lpSlotInsertEvent,
       "lpSlotExtractEvent": lpSlotExtractEvent,
       "lpBridgeAddressThresholdEvent": lpBridgeAddressThresholdEvent,
       "lpSystemOverTemperatureEvent": lpSystemOverTemperatureEvent,
       "lpSlotOverTemperatureEvent": lpSlotOverTemperatureEvent,
       "lpPowerSupplyFailureEvent": lpPowerSupplyFailureEvent,
       "chassis": chassis,
       "chassisId": chassisId,
       "chassisType": chassisType,
       "chassisRevision": chassisRevision,
       "chassisName": chassisName,
       "chassisNameAbbrev": chassisNameAbbrev,
       "chassisManufacturer": chassisManufacturer,
       "chassisSlotCount": chassisSlotCount,
       "chassisBuildTime": chassisBuildTime,
       "chassisSoftwareRevision": chassisSoftwareRevision,
       "chassisControlPanelColumns": chassisControlPanelColumns,
       "chassisControlPanelLines": chassisControlPanelLines,
       "chassisControlPanelText": chassisControlPanelText,
       "chassisAction": chassisAction,
       "slot": slot,
       "slotTable": slotTable,
       "slotEntry": slotEntry,
       "slotIndex": slotIndex,
       "slotBoardType": slotBoardType,
       "slotBoardRevision": slotBoardRevision,
       "slotBoardStatus": slotBoardStatus,
       "slotBoardName": slotBoardName,
       "slotBoardNameAbbrev": slotBoardNameAbbrev,
       "slotBoardAction": slotBoardAction,
       "spm": spm,
       "spmTable": spmTable,
       "spmEntry": spmEntry,
       "spmSlotIndex": spmSlotIndex,
       "spmEthernetPortCount": spmEthernetPortCount,
       "spmBaseEthernetPortIndex": spmBaseEthernetPortIndex,
       "feam": feam,
       "feamTable": feamTable,
       "feamEntry": feamEntry,
       "feamSlotIndex": feamSlotIndex,
       "feamMACCount": feamMACCount,
       "feamBaseMACIndex": feamBaseMACIndex,
       "feamPortCount": feamPortCount,
       "feamBasePortIndex": feamBasePortIndex,
       "fcm": fcm,
       "fcmTable": fcmTable,
       "fcmEntry": fcmEntry,
       "fcmSlotIndex": fcmSlotIndex,
       "fcmPortCount": fcmPortCount,
       "fcmBasePortIndex": fcmBasePortIndex,
       "port": port,
       "portTable": portTable,
       "portEntry": portEntry,
       "portSlotIndex": portSlotIndex,
       "portIndex": portIndex,
       "portLabel": portLabel,
       "eem": eem,
       "eemTable": eemTable,
       "eemEntry": eemEntry,
       "eemSlotIndex": eemSlotIndex,
       "eemFddiMACCount": eemFddiMACCount,
       "eemBaseFddiMACIndex": eemBaseFddiMACIndex,
       "eemEthernetPortCount": eemEthernetPortCount,
       "eemBaseEthernetPortIndex": eemBaseEthernetPortIndex,
       "eemAddressThreshold": eemAddressThreshold,
       "eemFddiMAC": eemFddiMAC,
       "eemFddiMACTable": eemFddiMACTable,
       "eemFddiMACEntry": eemFddiMACEntry,
       "eemFddiSlotIndex": eemFddiSlotIndex,
       "eemFddiMACIndex": eemFddiMACIndex,
       "eemFddiMACForwardedCts": eemFddiMACForwardedCts,
       "eemFddiMACDroppedCts": eemFddiMACDroppedCts,
       "eemEthernetPort": eemEthernetPort,
       "eemEthernetPortTable": eemEthernetPortTable,
       "eemEthernetPortEntry": eemEthernetPortEntry,
       "eemEthernetPortSlotIndex": eemEthernetPortSlotIndex,
       "eemEthernetPortIndex": eemEthernetPortIndex,
       "eemEthernetPortLabel": eemEthernetPortLabel,
       "eemEthernetPortForwardedCts": eemEthernetPortForwardedCts,
       "eemEthernetPortDroppedCts": eemEthernetPortDroppedCts,
       "eemEthernetPortUTurnCts": eemEthernetPortUTurnCts,
       "eemEthernetPortState": eemEthernetPortState,
       "eemEthernetPortAction": eemEthernetPortAction,
       "eemMACAddress": eemMACAddress,
       "eemEthernetMACAddressTable": eemEthernetMACAddressTable,
       "eemEthernetMACAddressEntry": eemEthernetMACAddressEntry,
       "eemEthernetMACAddressSlotIndex": eemEthernetMACAddressSlotIndex,
       "eemEthernetMACAddressPortIndex": eemEthernetMACAddressPortIndex,
       "eemEthernetMACAddressIndex": eemEthernetMACAddressIndex,
       "eemEthernetMACAddressType": eemEthernetMACAddressType,
       "eemEthernetMACAddressRemoteAddress": eemEthernetMACAddressRemoteAddress,
       "eemEthernetMACAddressIsStatic": eemEthernetMACAddressIsStatic,
       "eemEthernetMACAddressStaticPort": eemEthernetMACAddressStaticPort,
       "eemEthernetMACAddressAge": eemEthernetMACAddressAge,
       "lpSystem": lpSystem,
       "lpSystemId": lpSystemId,
       "lpSystemType": lpSystemType,
       "lpSystemName": lpSystemName,
       "lpSystemManufacturer": lpSystemManufacturer,
       "lpSystemBackplaneRevision": lpSystemBackplaneRevision,
       "lpSystemSlotCount": lpSystemSlotCount,
       "lpSystemMemorySize": lpSystemMemorySize,
       "lpSystemFlashMemorySize": lpSystemFlashMemorySize,
       "lpSystemNvMemorySize": lpSystemNvMemorySize,
       "lpSystemSoftwareRevision": lpSystemSoftwareRevision,
       "lpSystemBuildTime": lpSystemBuildTime,
       "lpSystemControlPanelHardwareRevision": lpSystemControlPanelHardwareRevision,
       "lpSystemControlPanelSoftwareRevision": lpSystemControlPanelSoftwareRevision,
       "lpSystemControlPanelLines": lpSystemControlPanelLines,
       "lpSystemControlPanelColumns": lpSystemControlPanelColumns,
       "lpSystemControlPanelText": lpSystemControlPanelText,
       "lpSystemFddiMacCount": lpSystemFddiMacCount,
       "lpSystemFddiPortCount": lpSystemFddiPortCount,
       "lpSystemEthernetPortCount": lpSystemEthernetPortCount,
       "lpSystemExpressFunctionCount": lpSystemExpressFunctionCount,
       "lpSystemExpressFddiPortCount": lpSystemExpressFddiPortCount,
       "lpSystemExpressEthernetPortCount": lpSystemExpressEthernetPortCount,
       "lpSystemPowerSupplyCount": lpSystemPowerSupplyCount,
       "lpSystemAction": lpSystemAction,
       "lpSystemBridgeFunctionCount": lpSystemBridgeFunctionCount,
       "lpSystemSmtProxyTimeoutBase": lpSystemSmtProxyTimeoutBase,
       "lpSystemSmtProxyEvents": lpSystemSmtProxyEvents,
       "lpSlot": lpSlot,
       "lpSlotTable": lpSlotTable,
       "lpSlotEntry": lpSlotEntry,
       "lpSlotIndex": lpSlotIndex,
       "lpSlotBoardType": lpSlotBoardType,
       "lpSlotBoardRevision": lpSlotBoardRevision,
       "lpSlotBoardStatus": lpSlotBoardStatus,
       "lpSlotBoardName": lpSlotBoardName,
       "lpSlotBoardNameAbbrev": lpSlotBoardNameAbbrev,
       "lpSlotFddiMacCount": lpSlotFddiMacCount,
       "lpSlotFddiMacBaseIndex": lpSlotFddiMacBaseIndex,
       "lpSlotFddiPortCount": lpSlotFddiPortCount,
       "lpSlotFddiPortBaseIndex": lpSlotFddiPortBaseIndex,
       "lpSlotEthernetPortCount": lpSlotEthernetPortCount,
       "lpSlotEthernetPortBaseIndex": lpSlotEthernetPortBaseIndex,
       "lpSlotExpressFunctionCount": lpSlotExpressFunctionCount,
       "lpSlotExpressFunctionBaseIndex": lpSlotExpressFunctionBaseIndex,
       "lpSlotExpressFddiPortCount": lpSlotExpressFddiPortCount,
       "lpSlotExpressFddiPortBaseIndex": lpSlotExpressFddiPortBaseIndex,
       "lpSlotExpressEthernetPortCount": lpSlotExpressEthernetPortCount,
       "lpSlotExpressEthernetPortBaseIndex": lpSlotExpressEthernetPortBaseIndex,
       "lpSlotBoardAction": lpSlotBoardAction,
       "lpSlotBridgeFunctionCount": lpSlotBridgeFunctionCount,
       "lpSlotBridgeFunctionBaseIndex": lpSlotBridgeFunctionBaseIndex,
       "lpFddiMac": lpFddiMac,
       "lpFddiMacTable": lpFddiMacTable,
       "lpFddiMacEntry": lpFddiMacEntry,
       "lpFddiMacIndex": lpFddiMacIndex,
       "lpFddiMacSlotIndex": lpFddiMacSlotIndex,
       "lpFddiMacLocalIndex": lpFddiMacLocalIndex,
       "lpFddiMacByteReceiveRate": lpFddiMacByteReceiveRate,
       "lpFddiMacPeakByteReceiveRate": lpFddiMacPeakByteReceiveRate,
       "lpFddiMacFrameReceiveRate": lpFddiMacFrameReceiveRate,
       "lpFddiMacPeakFrameReceiveRate": lpFddiMacPeakFrameReceiveRate,
       "lpFddiMacByteTransmitRate": lpFddiMacByteTransmitRate,
       "lpFddiMacPeakByteTransmitRate": lpFddiMacPeakByteTransmitRate,
       "lpFddiMacFrameTransmitRate": lpFddiMacFrameTransmitRate,
       "lpFddiMacPeakFrameTransmitRate": lpFddiMacPeakFrameTransmitRate,
       "lpFddiMacReceiveMulticastThreshold": lpFddiMacReceiveMulticastThreshold,
       "lpFddiMacBeaconHistory": lpFddiMacBeaconHistory,
       "lpEthernetPort": lpEthernetPort,
       "lpEthernetPortTable": lpEthernetPortTable,
       "lpEthernetPortEntry": lpEthernetPortEntry,
       "lpEthernetPortIndex": lpEthernetPortIndex,
       "lpEthernetPortSlotIndex": lpEthernetPortSlotIndex,
       "lpEthernetPortLocalIndex": lpEthernetPortLocalIndex,
       "lpEthernetPortLabel": lpEthernetPortLabel,
       "lpEthernetPortChipsetType": lpEthernetPortChipsetType,
       "lpEthernetPortLinkStatus": lpEthernetPortLinkStatus,
       "lpEthernetPortByteReceiveRate": lpEthernetPortByteReceiveRate,
       "lpEthernetPortPeakByteReceiveRate": lpEthernetPortPeakByteReceiveRate,
       "lpEthernetPortFrameReceiveRate": lpEthernetPortFrameReceiveRate,
       "lpEthernetPortPeakFrameReceiveRate": lpEthernetPortPeakFrameReceiveRate,
       "lpEthernetPortByteTransmitRate": lpEthernetPortByteTransmitRate,
       "lpEthernetPortPeakByteTransmitRate": lpEthernetPortPeakByteTransmitRate,
       "lpEthernetPortFrameTransmitRate": lpEthernetPortFrameTransmitRate,
       "lpEthernetPortPeakFrameTransmitRate": lpEthernetPortPeakFrameTransmitRate,
       "lpEthernetPortReceiveMulticastThreshold": lpEthernetPortReceiveMulticastThreshold,
       "lpEthernetPortType": lpEthernetPortType,
       "lpFddiPort": lpFddiPort,
       "lpFddiPortTable": lpFddiPortTable,
       "lpFddiPortEntry": lpFddiPortEntry,
       "lpFddiPortIndex": lpFddiPortIndex,
       "lpFddiPortSlotIndex": lpFddiPortSlotIndex,
       "lpFddiPortLocalIndex": lpFddiPortLocalIndex,
       "lpFddiPortLabel": lpFddiPortLabel,
       "lpExpress": lpExpress,
       "lpExpressTable": lpExpressTable,
       "lpExpressEntry": lpExpressEntry,
       "lpExpressIndex": lpExpressIndex,
       "lpExpressSlotIndex": lpExpressSlotIndex,
       "lpExpressLocalIndex": lpExpressLocalIndex,
       "lpExpressAddressThreshold": lpExpressAddressThreshold,
       "lpExpressFddiPort": lpExpressFddiPort,
       "lpExpressFddiPortTable": lpExpressFddiPortTable,
       "lpExpressFddiPortEntry": lpExpressFddiPortEntry,
       "lpExpressFddiPortIndex": lpExpressFddiPortIndex,
       "lpExpressFddiPortSlotIndex": lpExpressFddiPortSlotIndex,
       "lpExpressFddiPortLocalIndex": lpExpressFddiPortLocalIndex,
       "lpExpressFddiPortForwardedCts": lpExpressFddiPortForwardedCts,
       "lpExpressFddiPortDroppedCts": lpExpressFddiPortDroppedCts,
       "lpExpressEthernetPort": lpExpressEthernetPort,
       "lpExpressEthernetPortTable": lpExpressEthernetPortTable,
       "lpExpressEthernetPortEntry": lpExpressEthernetPortEntry,
       "lpExpressEthernetPortIndex": lpExpressEthernetPortIndex,
       "lpExpressEthernetPortSlotIndex": lpExpressEthernetPortSlotIndex,
       "lpExpressEthernetPortLocalIndex": lpExpressEthernetPortLocalIndex,
       "lpExpressEthernetPortForwardedCts": lpExpressEthernetPortForwardedCts,
       "lpExpressEthernetPortDroppedCts": lpExpressEthernetPortDroppedCts,
       "lpExpressEthernetPortUTurnCts": lpExpressEthernetPortUTurnCts,
       "lpExpressEthernetPortAction": lpExpressEthernetPortAction,
       "lpExpressEthernetPortAddress": lpExpressEthernetPortAddress,
       "lpExpressEthernetPortAddressTable": lpExpressEthernetPortAddressTable,
       "lpExpressEthernetPortAddressEntry": lpExpressEthernetPortAddressEntry,
       "lpExpressEthernetPortAddressPortIndex": lpExpressEthernetPortAddressPortIndex,
       "lpExpressEthernetPortAddressIndex": lpExpressEthernetPortAddressIndex,
       "lpExpressEthernetPortAddressSlotIndex": lpExpressEthernetPortAddressSlotIndex,
       "lpExpressEthernetPortAddressType": lpExpressEthernetPortAddressType,
       "lpExpressEthernetPortAddressRemoteAddress": lpExpressEthernetPortAddressRemoteAddress,
       "lpExpressEthernetPortAddressIsStatic": lpExpressEthernetPortAddressIsStatic,
       "lpExpressEthernetPortAddressStaticPort": lpExpressEthernetPortAddressStaticPort,
       "lpExpressEthernetPortAddressAge": lpExpressEthernetPortAddressAge,
       "lpPowerSupply": lpPowerSupply,
       "lpPowerSupplyTable": lpPowerSupplyTable,
       "lpPowerSupplyEntry": lpPowerSupplyEntry,
       "lpPowerSupplyIndex": lpPowerSupplyIndex,
       "lpPowerSupplyLocation": lpPowerSupplyLocation,
       "lpPowerSupplyStatus": lpPowerSupplyStatus,
       "lpPowerSupplyFailureType": lpPowerSupplyFailureType,
       "lpPowerSupplyLastFailure": lpPowerSupplyLastFailure,
       "lpBridge": lpBridge,
       "lpBridgeTable": lpBridgeTable,
       "lpBridgeEntry": lpBridgeEntry,
       "lpBridgeIndex": lpBridgeIndex,
       "lpBridgeBaseSlotIndex": lpBridgeBaseSlotIndex,
       "lpBridgePortCount": lpBridgePortCount,
       "lpBridgeAddressTableSize": lpBridgeAddressTableSize,
       "lpBridgeAddressThreshold": lpBridgeAddressThreshold,
       "lpBridgeMode": lpBridgeMode,
       "lpBridgeLocalIndex": lpBridgeLocalIndex,
       "lpBridgePortTable": lpBridgePortTable,
       "lpBridgePortEntry": lpBridgePortEntry,
       "lpBridgePortBridgeIndex": lpBridgePortBridgeIndex,
       "lpBridgePortIndex": lpBridgePortIndex,
       "lpBridgePortSlotIndex": lpBridgePortSlotIndex,
       "lpBridgePortLocalIndex": lpBridgePortLocalIndex,
       "lpBridgePortType": lpBridgePortType,
       "lpBridgePortIpFragmentationEnabled": lpBridgePortIpFragmentationEnabled,
       "lpBridgePortReceiveMulticastLimit": lpBridgePortReceiveMulticastLimit,
       "lpBridgePortAddressAction": lpBridgePortAddressAction,
       "lpBridgePortTotalForwardedCts": lpBridgePortTotalForwardedCts,
       "lpBridgePortManagementFramesReceived": lpBridgePortManagementFramesReceived,
       "lpBridgePortTotalDiscards": lpBridgePortTotalDiscards,
       "lpBridgePortReceiveBlockedDiscards": lpBridgePortReceiveBlockedDiscards,
       "lpBridgePortReceiveMulticastLimitExceededs": lpBridgePortReceiveMulticastLimitExceededs,
       "lpBridgePortReceiveSecurityDiscards": lpBridgePortReceiveSecurityDiscards,
       "lpBridgePortReceiveUnknownDiscards": lpBridgePortReceiveUnknownDiscards,
       "lpBridgePortReceiveOtherDiscards": lpBridgePortReceiveOtherDiscards,
       "lpBridgePortReceiveErrorDiscards": lpBridgePortReceiveErrorDiscards,
       "lpBridgePortSameSegmentDiscards": lpBridgePortSameSegmentDiscards,
       "lpBridgePortTransmitBlockedDiscards": lpBridgePortTransmitBlockedDiscards,
       "lpBridgePortTotalFiltered": lpBridgePortTotalFiltered,
       "lpBridgePortReceiveUnicastFiltered": lpBridgePortReceiveUnicastFiltered,
       "lpBridgePortReceiveMulticastFiltered": lpBridgePortReceiveMulticastFiltered,
       "lpBridgePortTransmitUnicastFiltered": lpBridgePortTransmitUnicastFiltered,
       "lpBridgePortTransmitMulticastFiltered": lpBridgePortTransmitMulticastFiltered,
       "lpBridgePortReceiveMulticastLimitExceededCount": lpBridgePortReceiveMulticastLimitExceededCount,
       "lpBridgePortForwardedToTable": lpBridgePortForwardedToTable,
       "lpBridgePortForwardedToEntry": lpBridgePortForwardedToEntry,
       "lpBridgePortForwardedToBridgeIndex": lpBridgePortForwardedToBridgeIndex,
       "lpBridgePortForwardedToReceivePortIndex": lpBridgePortForwardedToReceivePortIndex,
       "lpBridgePortForwardedToDstPortIndex": lpBridgePortForwardedToDstPortIndex,
       "lpBridgePortForwardedToCount": lpBridgePortForwardedToCount,
       "lpBridgePortFilteredToTable": lpBridgePortFilteredToTable,
       "lpBridgePortFilteredToEntry": lpBridgePortFilteredToEntry,
       "lpBridgePortFilteredToBridgeIndex": lpBridgePortFilteredToBridgeIndex,
       "lpBridgePortFilteredToReceivePortIndex": lpBridgePortFilteredToReceivePortIndex,
       "lpBridgePortFilteredToDstPortIndex": lpBridgePortFilteredToDstPortIndex,
       "lpBridgePortFilteredToCount": lpBridgePortFilteredToCount,
       "lpBridgePortAddressTable": lpBridgePortAddressTable,
       "lpBridgePortAddressEntry": lpBridgePortAddressEntry,
       "lpBridgePortAddressBridgeIndex": lpBridgePortAddressBridgeIndex,
       "lpBridgePortAddressPortIndex": lpBridgePortAddressPortIndex,
       "lpBridgePortAddressIndex": lpBridgePortAddressIndex,
       "lpBridgePortAddressRemoteAddress": lpBridgePortAddressRemoteAddress,
       "lpBridgePortAddressType": lpBridgePortAddressType,
       "lpBridgePortAddressIsStatic": lpBridgePortAddressIsStatic,
       "lpBridgePortAddressStaticPort": lpBridgePortAddressStaticPort,
       "lpBridgePortAddressAge": lpBridgePortAddressAge,
       "lpTrapEnterprise": lpTrapEnterprise,
       "lpTrapEnterpriseTable": lpTrapEnterpriseTable,
       "lpTrapEnterpriseTableEntry": lpTrapEnterpriseTableEntry,
       "lpTrapEnterpriseIndex": lpTrapEnterpriseIndex,
       "lpTrapEnterpriseOID": lpTrapEnterpriseOID,
       "lpTrapDest": lpTrapDest,
       "lpTrapDestTable": lpTrapDestTable,
       "lpTrapDestTableEntry": lpTrapDestTableEntry,
       "lpTrapDestAddr": lpTrapDestAddr,
       "lpTrapDestEnterpriseIndex": lpTrapDestEnterpriseIndex,
       "lpTrapNumber": lpTrapNumber,
       "lpTrapEntryStatus": lpTrapEntryStatus}
)
