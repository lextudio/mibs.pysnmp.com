# SNMP MIB module (LB3GH-1-0-7) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/LB3GH-1-0-7
# Produced by pysmi-1.5.4 at Mon Oct 14 22:17:22 2024
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

_A3Com_ObjectIdentity = ObjectIdentity
a3Com = _A3Com_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43)
)
_Lb3gh_ObjectIdentity = ObjectIdentity
lb3gh = _Lb3gh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 7)
)
_Lb3ghMib_ObjectIdentity = ObjectIdentity
lb3ghMib = _Lb3ghMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 7, 1)
)
_Chassis_ObjectIdentity = ObjectIdentity
chassis = _Chassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 1)
)
_ChassisId_Type = Integer32
_ChassisId_Object = MibScalar
chassisId = _ChassisId_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 1, 1),
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
              2)
        )
    )
    namedValues = NamedValues(
        *(("linkBuilder3GH", 2),
          ("other", 1))
    )


_ChassisType_Type.__name__ = "Integer32"
_ChassisType_Object = MibScalar
chassisType = _ChassisType_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 1, 6),
    _ChassisManufacturer_Type()
)
chassisManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisManufacturer.setStatus("deprecated")
_ChassisSlotCount_Type = Integer32
_ChassisSlotCount_Object = MibScalar
chassisSlotCount = _ChassisSlotCount_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 1, 7),
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
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 1, 8),
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
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 1, 9),
    _ChassisSoftwareRevision_Type()
)
chassisSoftwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisSoftwareRevision.setStatus("deprecated")
_ChassisControlPanelColumns_Type = Integer32
_ChassisControlPanelColumns_Object = MibScalar
chassisControlPanelColumns = _ChassisControlPanelColumns_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 1, 10),
    _ChassisControlPanelColumns_Type()
)
chassisControlPanelColumns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisControlPanelColumns.setStatus("deprecated")
_ChassisControlPanelLines_Type = Integer32
_ChassisControlPanelLines_Object = MibScalar
chassisControlPanelLines = _ChassisControlPanelLines_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 1, 11),
    _ChassisControlPanelLines_Type()
)
chassisControlPanelLines.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisControlPanelLines.setStatus("deprecated")


class _ChassisControlPanelText_Type(DisplayString):
    """Custom type chassisControlPanelText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_ChassisControlPanelText_Type.__name__ = "DisplayString"
_ChassisControlPanelText_Object = MibScalar
chassisControlPanelText = _ChassisControlPanelText_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 1, 12),
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
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 1, 13),
    _ChassisAction_Type()
)
chassisAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chassisAction.setStatus("deprecated")
_Slot_ObjectIdentity = ObjectIdentity
slot = _Slot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 2)
)
_SlotTable_Object = MibTable
slotTable = _SlotTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 2, 1)
)
if mibBuilder.loadTexts:
    slotTable.setStatus("deprecated")
_SlotEntry_Object = MibTableRow
slotEntry = _SlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 2, 1, 1)
)
slotEntry.setIndexNames(
    (0, "LB3GH-1-0-7", "slotIndex"),
)
if mibBuilder.loadTexts:
    slotEntry.setStatus("deprecated")
_SlotIndex_Type = Integer32
_SlotIndex_Object = MibTableColumn
slotIndex = _SlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 2, 1, 1, 1),
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
        *(("elm", 6),
          ("emptySlot", 2),
          ("esm", 7),
          ("fbcm", 4),
          ("fcm", 5),
          ("fcm2", 8),
          ("smm", 3),
          ("unknown", 1))
    )


_SlotBoardType_Type.__name__ = "Integer32"
_SlotBoardType_Object = MibTableColumn
slotBoardType = _SlotBoardType_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 2, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 2, 1, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 2, 1, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 2, 1, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 2, 1, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 2, 1, 1, 7),
    _SlotBoardAction_Type()
)
slotBoardAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slotBoardAction.setStatus("deprecated")
_Smm_ObjectIdentity = ObjectIdentity
smm = _Smm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 3)
)
_SmmTable_Object = MibTable
smmTable = _SmmTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 3, 1)
)
if mibBuilder.loadTexts:
    smmTable.setStatus("deprecated")
_SmmEntry_Object = MibTableRow
smmEntry = _SmmEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 3, 1, 1)
)
smmEntry.setIndexNames(
    (0, "LB3GH-1-0-7", "smmSlotIndex"),
)
if mibBuilder.loadTexts:
    smmEntry.setStatus("deprecated")
_SmmSlotIndex_Type = Integer32
_SmmSlotIndex_Object = MibTableColumn
smmSlotIndex = _SmmSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 3, 1, 1, 1),
    _SmmSlotIndex_Type()
)
smmSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smmSlotIndex.setStatus("deprecated")
_SmmEthernetPortCount_Type = Integer32
_SmmEthernetPortCount_Object = MibTableColumn
smmEthernetPortCount = _SmmEthernetPortCount_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 3, 1, 1, 2),
    _SmmEthernetPortCount_Type()
)
smmEthernetPortCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smmEthernetPortCount.setStatus("deprecated")
_SmmBaseEthernetPortIndex_Type = Integer32
_SmmBaseEthernetPortIndex_Object = MibTableColumn
smmBaseEthernetPortIndex = _SmmBaseEthernetPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 3, 1, 1, 3),
    _SmmBaseEthernetPortIndex_Type()
)
smmBaseEthernetPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smmBaseEthernetPortIndex.setStatus("deprecated")
_Fbcm_ObjectIdentity = ObjectIdentity
fbcm = _Fbcm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 4)
)
_FbcmTable_Object = MibTable
fbcmTable = _FbcmTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 4, 1)
)
if mibBuilder.loadTexts:
    fbcmTable.setStatus("deprecated")
_FbcmEntry_Object = MibTableRow
fbcmEntry = _FbcmEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 4, 1, 1)
)
fbcmEntry.setIndexNames(
    (0, "LB3GH-1-0-7", "fbcmSlotIndex"),
)
if mibBuilder.loadTexts:
    fbcmEntry.setStatus("deprecated")
_FbcmSlotIndex_Type = Integer32
_FbcmSlotIndex_Object = MibTableColumn
fbcmSlotIndex = _FbcmSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 4, 1, 1, 1),
    _FbcmSlotIndex_Type()
)
fbcmSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fbcmSlotIndex.setStatus("deprecated")
_FbcmMACCount_Type = Integer32
_FbcmMACCount_Object = MibTableColumn
fbcmMACCount = _FbcmMACCount_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 4, 1, 1, 2),
    _FbcmMACCount_Type()
)
fbcmMACCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fbcmMACCount.setStatus("deprecated")
_FbcmBaseMACIndex_Type = Integer32
_FbcmBaseMACIndex_Object = MibTableColumn
fbcmBaseMACIndex = _FbcmBaseMACIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 4, 1, 1, 3),
    _FbcmBaseMACIndex_Type()
)
fbcmBaseMACIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fbcmBaseMACIndex.setStatus("deprecated")
_FbcmPortCount_Type = Integer32
_FbcmPortCount_Object = MibTableColumn
fbcmPortCount = _FbcmPortCount_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 4, 1, 1, 4),
    _FbcmPortCount_Type()
)
fbcmPortCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fbcmPortCount.setStatus("deprecated")
_FbcmBasePortIndex_Type = Integer32
_FbcmBasePortIndex_Object = MibTableColumn
fbcmBasePortIndex = _FbcmBasePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 4, 1, 1, 5),
    _FbcmBasePortIndex_Type()
)
fbcmBasePortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fbcmBasePortIndex.setStatus("deprecated")
_Fcm_ObjectIdentity = ObjectIdentity
fcm = _Fcm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 5)
)
_FcmTable_Object = MibTable
fcmTable = _FcmTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 5, 1)
)
if mibBuilder.loadTexts:
    fcmTable.setStatus("deprecated")
_FcmEntry_Object = MibTableRow
fcmEntry = _FcmEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 5, 1, 1)
)
fcmEntry.setIndexNames(
    (0, "LB3GH-1-0-7", "fcmSlotIndex"),
)
if mibBuilder.loadTexts:
    fcmEntry.setStatus("deprecated")
_FcmSlotIndex_Type = Integer32
_FcmSlotIndex_Object = MibTableColumn
fcmSlotIndex = _FcmSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 5, 1, 1, 1),
    _FcmSlotIndex_Type()
)
fcmSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcmSlotIndex.setStatus("deprecated")
_FcmPortCount_Type = Integer32
_FcmPortCount_Object = MibTableColumn
fcmPortCount = _FcmPortCount_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 5, 1, 1, 2),
    _FcmPortCount_Type()
)
fcmPortCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcmPortCount.setStatus("deprecated")
_FcmBasePortIndex_Type = Integer32
_FcmBasePortIndex_Object = MibTableColumn
fcmBasePortIndex = _FcmBasePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 5, 1, 1, 3),
    _FcmBasePortIndex_Type()
)
fcmBasePortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcmBasePortIndex.setStatus("deprecated")
_Port_ObjectIdentity = ObjectIdentity
port = _Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 6)
)
_PortTable_Object = MibTable
portTable = _PortTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 6, 1)
)
if mibBuilder.loadTexts:
    portTable.setStatus("deprecated")
_PortEntry_Object = MibTableRow
portEntry = _PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 6, 1, 1)
)
portEntry.setIndexNames(
    (0, "LB3GH-1-0-7", "portSlotIndex"),
    (0, "LB3GH-1-0-7", "portIndex"),
)
if mibBuilder.loadTexts:
    portEntry.setStatus("deprecated")
_PortSlotIndex_Type = Integer32
_PortSlotIndex_Object = MibTableColumn
portSlotIndex = _PortSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 6, 1, 1, 1),
    _PortSlotIndex_Type()
)
portSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portSlotIndex.setStatus("deprecated")
_PortIndex_Type = Integer32
_PortIndex_Object = MibTableColumn
portIndex = _PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 6, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 6, 1, 1, 3),
    _PortLabel_Type()
)
portLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portLabel.setStatus("deprecated")
_Elm_ObjectIdentity = ObjectIdentity
elm = _Elm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 7)
)
_ElmTable_Object = MibTable
elmTable = _ElmTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 7, 1)
)
if mibBuilder.loadTexts:
    elmTable.setStatus("deprecated")
_ElmEntry_Object = MibTableRow
elmEntry = _ElmEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 7, 1, 1)
)
elmEntry.setIndexNames(
    (0, "LB3GH-1-0-7", "elmSlotIndex"),
)
if mibBuilder.loadTexts:
    elmEntry.setStatus("deprecated")
_ElmSlotIndex_Type = Integer32
_ElmSlotIndex_Object = MibTableColumn
elmSlotIndex = _ElmSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 7, 1, 1, 1),
    _ElmSlotIndex_Type()
)
elmSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elmSlotIndex.setStatus("deprecated")
_ElmFddiMACCount_Type = Integer32
_ElmFddiMACCount_Object = MibTableColumn
elmFddiMACCount = _ElmFddiMACCount_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 7, 1, 1, 2),
    _ElmFddiMACCount_Type()
)
elmFddiMACCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elmFddiMACCount.setStatus("deprecated")
_ElmBaseFddiMACIndex_Type = Integer32
_ElmBaseFddiMACIndex_Object = MibTableColumn
elmBaseFddiMACIndex = _ElmBaseFddiMACIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 7, 1, 1, 3),
    _ElmBaseFddiMACIndex_Type()
)
elmBaseFddiMACIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elmBaseFddiMACIndex.setStatus("deprecated")
_ElmEthernetPortCount_Type = Integer32
_ElmEthernetPortCount_Object = MibTableColumn
elmEthernetPortCount = _ElmEthernetPortCount_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 7, 1, 1, 4),
    _ElmEthernetPortCount_Type()
)
elmEthernetPortCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elmEthernetPortCount.setStatus("deprecated")
_ElmBaseEthernetPortIndex_Type = Integer32
_ElmBaseEthernetPortIndex_Object = MibTableColumn
elmBaseEthernetPortIndex = _ElmBaseEthernetPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 7, 1, 1, 5),
    _ElmBaseEthernetPortIndex_Type()
)
elmBaseEthernetPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elmBaseEthernetPortIndex.setStatus("deprecated")
_ElmAddressThreshold_Type = Integer32
_ElmAddressThreshold_Object = MibTableColumn
elmAddressThreshold = _ElmAddressThreshold_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 7, 1, 1, 6),
    _ElmAddressThreshold_Type()
)
elmAddressThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    elmAddressThreshold.setStatus("deprecated")
_ElmFddiMAC_ObjectIdentity = ObjectIdentity
elmFddiMAC = _ElmFddiMAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 8)
)
_ElmFddiMACTable_Object = MibTable
elmFddiMACTable = _ElmFddiMACTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 8, 1)
)
if mibBuilder.loadTexts:
    elmFddiMACTable.setStatus("deprecated")
_ElmFddiMACEntry_Object = MibTableRow
elmFddiMACEntry = _ElmFddiMACEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 8, 1, 1)
)
elmFddiMACEntry.setIndexNames(
    (0, "LB3GH-1-0-7", "elmFddiSlotIndex"),
    (0, "LB3GH-1-0-7", "elmFddiMACIndex"),
)
if mibBuilder.loadTexts:
    elmFddiMACEntry.setStatus("deprecated")
_ElmFddiSlotIndex_Type = Integer32
_ElmFddiSlotIndex_Object = MibTableColumn
elmFddiSlotIndex = _ElmFddiSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 8, 1, 1, 1),
    _ElmFddiSlotIndex_Type()
)
elmFddiSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elmFddiSlotIndex.setStatus("deprecated")
_ElmFddiMACIndex_Type = Integer32
_ElmFddiMACIndex_Object = MibTableColumn
elmFddiMACIndex = _ElmFddiMACIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 8, 1, 1, 2),
    _ElmFddiMACIndex_Type()
)
elmFddiMACIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elmFddiMACIndex.setStatus("deprecated")
_ElmFddiMACForwardedCts_Type = Counter32
_ElmFddiMACForwardedCts_Object = MibTableColumn
elmFddiMACForwardedCts = _ElmFddiMACForwardedCts_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 8, 1, 1, 3),
    _ElmFddiMACForwardedCts_Type()
)
elmFddiMACForwardedCts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elmFddiMACForwardedCts.setStatus("deprecated")
_ElmFddiMACDroppedCts_Type = Counter32
_ElmFddiMACDroppedCts_Object = MibTableColumn
elmFddiMACDroppedCts = _ElmFddiMACDroppedCts_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 8, 1, 1, 4),
    _ElmFddiMACDroppedCts_Type()
)
elmFddiMACDroppedCts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elmFddiMACDroppedCts.setStatus("deprecated")
_ElmEthernetPort_ObjectIdentity = ObjectIdentity
elmEthernetPort = _ElmEthernetPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 9)
)
_ElmEthernetPortTable_Object = MibTable
elmEthernetPortTable = _ElmEthernetPortTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 9, 1)
)
if mibBuilder.loadTexts:
    elmEthernetPortTable.setStatus("deprecated")
_ElmEthernetPortEntry_Object = MibTableRow
elmEthernetPortEntry = _ElmEthernetPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 9, 1, 1)
)
elmEthernetPortEntry.setIndexNames(
    (0, "LB3GH-1-0-7", "elmEthernetPortSlotIndex"),
    (0, "LB3GH-1-0-7", "elmEthernetPortIndex"),
)
if mibBuilder.loadTexts:
    elmEthernetPortEntry.setStatus("deprecated")
_ElmEthernetPortSlotIndex_Type = Integer32
_ElmEthernetPortSlotIndex_Object = MibTableColumn
elmEthernetPortSlotIndex = _ElmEthernetPortSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 9, 1, 1, 1),
    _ElmEthernetPortSlotIndex_Type()
)
elmEthernetPortSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elmEthernetPortSlotIndex.setStatus("deprecated")
_ElmEthernetPortIndex_Type = Integer32
_ElmEthernetPortIndex_Object = MibTableColumn
elmEthernetPortIndex = _ElmEthernetPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 9, 1, 1, 2),
    _ElmEthernetPortIndex_Type()
)
elmEthernetPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elmEthernetPortIndex.setStatus("deprecated")


class _ElmEthernetPortLabel_Type(DisplayString):
    """Custom type elmEthernetPortLabel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ElmEthernetPortLabel_Type.__name__ = "DisplayString"
_ElmEthernetPortLabel_Object = MibTableColumn
elmEthernetPortLabel = _ElmEthernetPortLabel_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 9, 1, 1, 3),
    _ElmEthernetPortLabel_Type()
)
elmEthernetPortLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    elmEthernetPortLabel.setStatus("deprecated")
_ElmEthernetPortForwardedCts_Type = Counter32
_ElmEthernetPortForwardedCts_Object = MibTableColumn
elmEthernetPortForwardedCts = _ElmEthernetPortForwardedCts_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 9, 1, 1, 4),
    _ElmEthernetPortForwardedCts_Type()
)
elmEthernetPortForwardedCts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elmEthernetPortForwardedCts.setStatus("deprecated")
_ElmEthernetPortDroppedCts_Type = Counter32
_ElmEthernetPortDroppedCts_Object = MibTableColumn
elmEthernetPortDroppedCts = _ElmEthernetPortDroppedCts_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 9, 1, 1, 5),
    _ElmEthernetPortDroppedCts_Type()
)
elmEthernetPortDroppedCts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elmEthernetPortDroppedCts.setStatus("deprecated")
_ElmEthernetPortUTurnCts_Type = Counter32
_ElmEthernetPortUTurnCts_Object = MibTableColumn
elmEthernetPortUTurnCts = _ElmEthernetPortUTurnCts_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 9, 1, 1, 6),
    _ElmEthernetPortUTurnCts_Type()
)
elmEthernetPortUTurnCts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elmEthernetPortUTurnCts.setStatus("deprecated")


class _ElmEthernetPortState_Type(Integer32):
    """Custom type elmEthernetPortState based on Integer32"""
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


_ElmEthernetPortState_Type.__name__ = "Integer32"
_ElmEthernetPortState_Object = MibTableColumn
elmEthernetPortState = _ElmEthernetPortState_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 9, 1, 1, 7),
    _ElmEthernetPortState_Type()
)
elmEthernetPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    elmEthernetPortState.setStatus("deprecated")


class _ElmEthernetPortAction_Type(Integer32):
    """Custom type elmEthernetPortAction based on Integer32"""
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


_ElmEthernetPortAction_Type.__name__ = "Integer32"
_ElmEthernetPortAction_Object = MibTableColumn
elmEthernetPortAction = _ElmEthernetPortAction_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 9, 1, 1, 8),
    _ElmEthernetPortAction_Type()
)
elmEthernetPortAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    elmEthernetPortAction.setStatus("deprecated")
_ElmMACAddress_ObjectIdentity = ObjectIdentity
elmMACAddress = _ElmMACAddress_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 10)
)
_ElmEthernetMACAddressTable_Object = MibTable
elmEthernetMACAddressTable = _ElmEthernetMACAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 10, 1)
)
if mibBuilder.loadTexts:
    elmEthernetMACAddressTable.setStatus("deprecated")
_ElmEthernetMACAddressEntry_Object = MibTableRow
elmEthernetMACAddressEntry = _ElmEthernetMACAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 10, 1, 1)
)
elmEthernetMACAddressEntry.setIndexNames(
    (0, "LB3GH-1-0-7", "elmEthernetMACAddressSlotIndex"),
    (0, "LB3GH-1-0-7", "elmEthernetMACAddressPortIndex"),
    (0, "LB3GH-1-0-7", "elmEthernetMACAddressIndex"),
)
if mibBuilder.loadTexts:
    elmEthernetMACAddressEntry.setStatus("deprecated")
_ElmEthernetMACAddressSlotIndex_Type = Integer32
_ElmEthernetMACAddressSlotIndex_Object = MibTableColumn
elmEthernetMACAddressSlotIndex = _ElmEthernetMACAddressSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 10, 1, 1, 1),
    _ElmEthernetMACAddressSlotIndex_Type()
)
elmEthernetMACAddressSlotIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    elmEthernetMACAddressSlotIndex.setStatus("deprecated")
_ElmEthernetMACAddressPortIndex_Type = Integer32
_ElmEthernetMACAddressPortIndex_Object = MibTableColumn
elmEthernetMACAddressPortIndex = _ElmEthernetMACAddressPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 10, 1, 1, 2),
    _ElmEthernetMACAddressPortIndex_Type()
)
elmEthernetMACAddressPortIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    elmEthernetMACAddressPortIndex.setStatus("deprecated")
_ElmEthernetMACAddressIndex_Type = Integer32
_ElmEthernetMACAddressIndex_Object = MibTableColumn
elmEthernetMACAddressIndex = _ElmEthernetMACAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 10, 1, 1, 3),
    _ElmEthernetMACAddressIndex_Type()
)
elmEthernetMACAddressIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    elmEthernetMACAddressIndex.setStatus("deprecated")


class _ElmEthernetMACAddressType_Type(Integer32):
    """Custom type elmEthernetMACAddressType based on Integer32"""
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


_ElmEthernetMACAddressType_Type.__name__ = "Integer32"
_ElmEthernetMACAddressType_Object = MibTableColumn
elmEthernetMACAddressType = _ElmEthernetMACAddressType_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 10, 1, 1, 4),
    _ElmEthernetMACAddressType_Type()
)
elmEthernetMACAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    elmEthernetMACAddressType.setStatus("deprecated")


class _ElmEthernetMACAddressRemoteAddress_Type(OctetString):
    """Custom type elmEthernetMACAddressRemoteAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_ElmEthernetMACAddressRemoteAddress_Type.__name__ = "OctetString"
_ElmEthernetMACAddressRemoteAddress_Object = MibTableColumn
elmEthernetMACAddressRemoteAddress = _ElmEthernetMACAddressRemoteAddress_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 10, 1, 1, 5),
    _ElmEthernetMACAddressRemoteAddress_Type()
)
elmEthernetMACAddressRemoteAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    elmEthernetMACAddressRemoteAddress.setStatus("deprecated")


class _ElmEthernetMACAddressIsStatic_Type(Integer32):
    """Custom type elmEthernetMACAddressIsStatic based on Integer32"""
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


_ElmEthernetMACAddressIsStatic_Type.__name__ = "Integer32"
_ElmEthernetMACAddressIsStatic_Object = MibTableColumn
elmEthernetMACAddressIsStatic = _ElmEthernetMACAddressIsStatic_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 10, 1, 1, 6),
    _ElmEthernetMACAddressIsStatic_Type()
)
elmEthernetMACAddressIsStatic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    elmEthernetMACAddressIsStatic.setStatus("deprecated")
_ElmEthernetMACAddressStaticPort_Type = Integer32
_ElmEthernetMACAddressStaticPort_Object = MibTableColumn
elmEthernetMACAddressStaticPort = _ElmEthernetMACAddressStaticPort_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 10, 1, 1, 7),
    _ElmEthernetMACAddressStaticPort_Type()
)
elmEthernetMACAddressStaticPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    elmEthernetMACAddressStaticPort.setStatus("deprecated")
_ElmEthernetMACAddressAge_Type = Integer32
_ElmEthernetMACAddressAge_Object = MibTableColumn
elmEthernetMACAddressAge = _ElmEthernetMACAddressAge_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 10, 1, 1, 8),
    _ElmEthernetMACAddressAge_Type()
)
elmEthernetMACAddressAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    elmEthernetMACAddressAge.setStatus("deprecated")
_LbSystem_ObjectIdentity = ObjectIdentity
lbSystem = _LbSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 11)
)
_LbSystemId_Type = Integer32
_LbSystemId_Object = MibScalar
lbSystemId = _LbSystemId_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 11, 1),
    _LbSystemId_Type()
)
lbSystemId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbSystemId.setStatus("mandatory")


class _LbSystemType_Type(Integer32):
    """Custom type lbSystemType based on Integer32"""
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


_LbSystemType_Type.__name__ = "Integer32"
_LbSystemType_Object = MibScalar
lbSystemType = _LbSystemType_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 11, 2),
    _LbSystemType_Type()
)
lbSystemType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbSystemType.setStatus("mandatory")


class _LbSystemName_Type(DisplayString):
    """Custom type lbSystemName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_LbSystemName_Type.__name__ = "DisplayString"
_LbSystemName_Object = MibScalar
lbSystemName = _LbSystemName_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 11, 3),
    _LbSystemName_Type()
)
lbSystemName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbSystemName.setStatus("mandatory")


class _LbSystemManufacturer_Type(DisplayString):
    """Custom type lbSystemManufacturer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_LbSystemManufacturer_Type.__name__ = "DisplayString"
_LbSystemManufacturer_Object = MibScalar
lbSystemManufacturer = _LbSystemManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 11, 4),
    _LbSystemManufacturer_Type()
)
lbSystemManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbSystemManufacturer.setStatus("mandatory")


class _LbSystemBackplaneRevision_Type(OctetString):
    """Custom type lbSystemBackplaneRevision based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_LbSystemBackplaneRevision_Type.__name__ = "OctetString"
_LbSystemBackplaneRevision_Object = MibScalar
lbSystemBackplaneRevision = _LbSystemBackplaneRevision_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 11, 5),
    _LbSystemBackplaneRevision_Type()
)
lbSystemBackplaneRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbSystemBackplaneRevision.setStatus("mandatory")
_LbSystemSlotCount_Type = Integer32
_LbSystemSlotCount_Object = MibScalar
lbSystemSlotCount = _LbSystemSlotCount_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 11, 6),
    _LbSystemSlotCount_Type()
)
lbSystemSlotCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbSystemSlotCount.setStatus("mandatory")
_LbSystemMemorySize_Type = Integer32
_LbSystemMemorySize_Object = MibScalar
lbSystemMemorySize = _LbSystemMemorySize_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 11, 7),
    _LbSystemMemorySize_Type()
)
lbSystemMemorySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbSystemMemorySize.setStatus("mandatory")
_LbSystemFlashMemorySize_Type = Integer32
_LbSystemFlashMemorySize_Object = MibScalar
lbSystemFlashMemorySize = _LbSystemFlashMemorySize_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 11, 8),
    _LbSystemFlashMemorySize_Type()
)
lbSystemFlashMemorySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbSystemFlashMemorySize.setStatus("mandatory")
_LbSystemNvMemorySize_Type = Integer32
_LbSystemNvMemorySize_Object = MibScalar
lbSystemNvMemorySize = _LbSystemNvMemorySize_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 11, 9),
    _LbSystemNvMemorySize_Type()
)
lbSystemNvMemorySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbSystemNvMemorySize.setStatus("mandatory")


class _LbSystemSoftwareRevision_Type(OctetString):
    """Custom type lbSystemSoftwareRevision based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_LbSystemSoftwareRevision_Type.__name__ = "OctetString"
_LbSystemSoftwareRevision_Object = MibScalar
lbSystemSoftwareRevision = _LbSystemSoftwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 11, 10),
    _LbSystemSoftwareRevision_Type()
)
lbSystemSoftwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbSystemSoftwareRevision.setStatus("mandatory")


class _LbSystemBuildTime_Type(DisplayString):
    """Custom type lbSystemBuildTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_LbSystemBuildTime_Type.__name__ = "DisplayString"
_LbSystemBuildTime_Object = MibScalar
lbSystemBuildTime = _LbSystemBuildTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 11, 11),
    _LbSystemBuildTime_Type()
)
lbSystemBuildTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbSystemBuildTime.setStatus("mandatory")


class _LbSystemControlPanelHardwareRevision_Type(OctetString):
    """Custom type lbSystemControlPanelHardwareRevision based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_LbSystemControlPanelHardwareRevision_Type.__name__ = "OctetString"
_LbSystemControlPanelHardwareRevision_Object = MibScalar
lbSystemControlPanelHardwareRevision = _LbSystemControlPanelHardwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 11, 12),
    _LbSystemControlPanelHardwareRevision_Type()
)
lbSystemControlPanelHardwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbSystemControlPanelHardwareRevision.setStatus("mandatory")


class _LbSystemControlPanelSoftwareRevision_Type(OctetString):
    """Custom type lbSystemControlPanelSoftwareRevision based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_LbSystemControlPanelSoftwareRevision_Type.__name__ = "OctetString"
_LbSystemControlPanelSoftwareRevision_Object = MibScalar
lbSystemControlPanelSoftwareRevision = _LbSystemControlPanelSoftwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 11, 13),
    _LbSystemControlPanelSoftwareRevision_Type()
)
lbSystemControlPanelSoftwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbSystemControlPanelSoftwareRevision.setStatus("mandatory")
_LbSystemControlPanelLines_Type = Integer32
_LbSystemControlPanelLines_Object = MibScalar
lbSystemControlPanelLines = _LbSystemControlPanelLines_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 11, 14),
    _LbSystemControlPanelLines_Type()
)
lbSystemControlPanelLines.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbSystemControlPanelLines.setStatus("mandatory")
_LbSystemControlPanelColumns_Type = Integer32
_LbSystemControlPanelColumns_Object = MibScalar
lbSystemControlPanelColumns = _LbSystemControlPanelColumns_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 11, 15),
    _LbSystemControlPanelColumns_Type()
)
lbSystemControlPanelColumns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbSystemControlPanelColumns.setStatus("mandatory")


class _LbSystemControlPanelText_Type(OctetString):
    """Custom type lbSystemControlPanelText based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_LbSystemControlPanelText_Type.__name__ = "OctetString"
_LbSystemControlPanelText_Object = MibScalar
lbSystemControlPanelText = _LbSystemControlPanelText_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 11, 16),
    _LbSystemControlPanelText_Type()
)
lbSystemControlPanelText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbSystemControlPanelText.setStatus("mandatory")
_LbSystemFddiMacCount_Type = Integer32
_LbSystemFddiMacCount_Object = MibScalar
lbSystemFddiMacCount = _LbSystemFddiMacCount_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 11, 17),
    _LbSystemFddiMacCount_Type()
)
lbSystemFddiMacCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbSystemFddiMacCount.setStatus("mandatory")
_LbSystemFddiPortCount_Type = Integer32
_LbSystemFddiPortCount_Object = MibScalar
lbSystemFddiPortCount = _LbSystemFddiPortCount_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 11, 18),
    _LbSystemFddiPortCount_Type()
)
lbSystemFddiPortCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbSystemFddiPortCount.setStatus("mandatory")
_LbSystemEthernetPortCount_Type = Integer32
_LbSystemEthernetPortCount_Object = MibScalar
lbSystemEthernetPortCount = _LbSystemEthernetPortCount_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 11, 19),
    _LbSystemEthernetPortCount_Type()
)
lbSystemEthernetPortCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbSystemEthernetPortCount.setStatus("mandatory")
_LbSystemExpressFunctionCount_Type = Integer32
_LbSystemExpressFunctionCount_Object = MibScalar
lbSystemExpressFunctionCount = _LbSystemExpressFunctionCount_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 11, 20),
    _LbSystemExpressFunctionCount_Type()
)
lbSystemExpressFunctionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbSystemExpressFunctionCount.setStatus("deprecated")
_LbSystemExpressFddiPortCount_Type = Integer32
_LbSystemExpressFddiPortCount_Object = MibScalar
lbSystemExpressFddiPortCount = _LbSystemExpressFddiPortCount_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 11, 21),
    _LbSystemExpressFddiPortCount_Type()
)
lbSystemExpressFddiPortCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbSystemExpressFddiPortCount.setStatus("deprecated")
_LbSystemExpressEthernetPortCount_Type = Integer32
_LbSystemExpressEthernetPortCount_Object = MibScalar
lbSystemExpressEthernetPortCount = _LbSystemExpressEthernetPortCount_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 11, 22),
    _LbSystemExpressEthernetPortCount_Type()
)
lbSystemExpressEthernetPortCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbSystemExpressEthernetPortCount.setStatus("deprecated")
_LbSystemPowerSupplyCount_Type = Integer32
_LbSystemPowerSupplyCount_Object = MibScalar
lbSystemPowerSupplyCount = _LbSystemPowerSupplyCount_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 11, 23),
    _LbSystemPowerSupplyCount_Type()
)
lbSystemPowerSupplyCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbSystemPowerSupplyCount.setStatus("mandatory")


class _LbSystemAction_Type(Integer32):
    """Custom type lbSystemAction based on Integer32"""
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


_LbSystemAction_Type.__name__ = "Integer32"
_LbSystemAction_Object = MibScalar
lbSystemAction = _LbSystemAction_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 11, 24),
    _LbSystemAction_Type()
)
lbSystemAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lbSystemAction.setStatus("mandatory")
_LbSystemBridgeFunctionCount_Type = Integer32
_LbSystemBridgeFunctionCount_Object = MibScalar
lbSystemBridgeFunctionCount = _LbSystemBridgeFunctionCount_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 11, 25),
    _LbSystemBridgeFunctionCount_Type()
)
lbSystemBridgeFunctionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbSystemBridgeFunctionCount.setStatus("mandatory")


class _LbSystemSmtProxyTimeoutBase_Type(Integer32):
    """Custom type lbSystemSmtProxyTimeoutBase based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_LbSystemSmtProxyTimeoutBase_Type.__name__ = "Integer32"
_LbSystemSmtProxyTimeoutBase_Object = MibScalar
lbSystemSmtProxyTimeoutBase = _LbSystemSmtProxyTimeoutBase_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 11, 26),
    _LbSystemSmtProxyTimeoutBase_Type()
)
lbSystemSmtProxyTimeoutBase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lbSystemSmtProxyTimeoutBase.setStatus("mandatory")


class _LbSystemSmtProxyEvents_Type(Integer32):
    """Custom type lbSystemSmtProxyEvents based on Integer32"""
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


_LbSystemSmtProxyEvents_Type.__name__ = "Integer32"
_LbSystemSmtProxyEvents_Object = MibScalar
lbSystemSmtProxyEvents = _LbSystemSmtProxyEvents_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 11, 27),
    _LbSystemSmtProxyEvents_Type()
)
lbSystemSmtProxyEvents.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lbSystemSmtProxyEvents.setStatus("mandatory")
_LbSlot_ObjectIdentity = ObjectIdentity
lbSlot = _LbSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 12)
)
_LbSlotTable_Object = MibTable
lbSlotTable = _LbSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 12, 1)
)
if mibBuilder.loadTexts:
    lbSlotTable.setStatus("mandatory")
_LbSlotEntry_Object = MibTableRow
lbSlotEntry = _LbSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 12, 1, 1)
)
lbSlotEntry.setIndexNames(
    (0, "LB3GH-1-0-7", "lbSlotIndex"),
)
if mibBuilder.loadTexts:
    lbSlotEntry.setStatus("mandatory")
_LbSlotIndex_Type = Integer32
_LbSlotIndex_Object = MibTableColumn
lbSlotIndex = _LbSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 12, 1, 1, 1),
    _LbSlotIndex_Type()
)
lbSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbSlotIndex.setStatus("mandatory")


class _LbSlotBoardType_Type(Integer32):
    """Custom type lbSlotBoardType based on Integer32"""
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
        *(("elm", 6),
          ("emptySlot", 2),
          ("esm", 7),
          ("fcm", 5),
          ("fcm2", 8),
          ("feam", 4),
          ("spm", 3),
          ("unknown", 1))
    )


_LbSlotBoardType_Type.__name__ = "Integer32"
_LbSlotBoardType_Object = MibTableColumn
lbSlotBoardType = _LbSlotBoardType_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 12, 1, 1, 2),
    _LbSlotBoardType_Type()
)
lbSlotBoardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbSlotBoardType.setStatus("mandatory")


class _LbSlotBoardRevision_Type(OctetString):
    """Custom type lbSlotBoardRevision based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_LbSlotBoardRevision_Type.__name__ = "OctetString"
_LbSlotBoardRevision_Object = MibTableColumn
lbSlotBoardRevision = _LbSlotBoardRevision_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 12, 1, 1, 3),
    _LbSlotBoardRevision_Type()
)
lbSlotBoardRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbSlotBoardRevision.setStatus("mandatory")


class _LbSlotBoardStatus_Type(Integer32):
    """Custom type lbSlotBoardStatus based on Integer32"""
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


_LbSlotBoardStatus_Type.__name__ = "Integer32"
_LbSlotBoardStatus_Object = MibTableColumn
lbSlotBoardStatus = _LbSlotBoardStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 12, 1, 1, 4),
    _LbSlotBoardStatus_Type()
)
lbSlotBoardStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbSlotBoardStatus.setStatus("mandatory")


class _LbSlotBoardName_Type(DisplayString):
    """Custom type lbSlotBoardName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_LbSlotBoardName_Type.__name__ = "DisplayString"
_LbSlotBoardName_Object = MibTableColumn
lbSlotBoardName = _LbSlotBoardName_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 12, 1, 1, 5),
    _LbSlotBoardName_Type()
)
lbSlotBoardName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbSlotBoardName.setStatus("mandatory")


class _LbSlotBoardNameAbbrev_Type(DisplayString):
    """Custom type lbSlotBoardNameAbbrev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LbSlotBoardNameAbbrev_Type.__name__ = "DisplayString"
_LbSlotBoardNameAbbrev_Object = MibTableColumn
lbSlotBoardNameAbbrev = _LbSlotBoardNameAbbrev_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 12, 1, 1, 6),
    _LbSlotBoardNameAbbrev_Type()
)
lbSlotBoardNameAbbrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbSlotBoardNameAbbrev.setStatus("mandatory")
_LbSlotFddiMacCount_Type = Integer32
_LbSlotFddiMacCount_Object = MibTableColumn
lbSlotFddiMacCount = _LbSlotFddiMacCount_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 12, 1, 1, 7),
    _LbSlotFddiMacCount_Type()
)
lbSlotFddiMacCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbSlotFddiMacCount.setStatus("mandatory")
_LbSlotFddiMacBaseIndex_Type = Integer32
_LbSlotFddiMacBaseIndex_Object = MibTableColumn
lbSlotFddiMacBaseIndex = _LbSlotFddiMacBaseIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 12, 1, 1, 8),
    _LbSlotFddiMacBaseIndex_Type()
)
lbSlotFddiMacBaseIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbSlotFddiMacBaseIndex.setStatus("mandatory")
_LbSlotFddiPortCount_Type = Integer32
_LbSlotFddiPortCount_Object = MibTableColumn
lbSlotFddiPortCount = _LbSlotFddiPortCount_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 12, 1, 1, 9),
    _LbSlotFddiPortCount_Type()
)
lbSlotFddiPortCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbSlotFddiPortCount.setStatus("mandatory")
_LbSlotFddiPortBaseIndex_Type = Integer32
_LbSlotFddiPortBaseIndex_Object = MibTableColumn
lbSlotFddiPortBaseIndex = _LbSlotFddiPortBaseIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 12, 1, 1, 10),
    _LbSlotFddiPortBaseIndex_Type()
)
lbSlotFddiPortBaseIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbSlotFddiPortBaseIndex.setStatus("mandatory")
_LbSlotEthernetPortCount_Type = Integer32
_LbSlotEthernetPortCount_Object = MibTableColumn
lbSlotEthernetPortCount = _LbSlotEthernetPortCount_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 12, 1, 1, 11),
    _LbSlotEthernetPortCount_Type()
)
lbSlotEthernetPortCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbSlotEthernetPortCount.setStatus("mandatory")
_LbSlotEthernetPortBaseIndex_Type = Integer32
_LbSlotEthernetPortBaseIndex_Object = MibTableColumn
lbSlotEthernetPortBaseIndex = _LbSlotEthernetPortBaseIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 12, 1, 1, 12),
    _LbSlotEthernetPortBaseIndex_Type()
)
lbSlotEthernetPortBaseIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbSlotEthernetPortBaseIndex.setStatus("mandatory")
_LbSlotExpressFunctionCount_Type = Integer32
_LbSlotExpressFunctionCount_Object = MibTableColumn
lbSlotExpressFunctionCount = _LbSlotExpressFunctionCount_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 12, 1, 1, 13),
    _LbSlotExpressFunctionCount_Type()
)
lbSlotExpressFunctionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbSlotExpressFunctionCount.setStatus("deprecated")
_LbSlotExpressFunctionBaseIndex_Type = Integer32
_LbSlotExpressFunctionBaseIndex_Object = MibTableColumn
lbSlotExpressFunctionBaseIndex = _LbSlotExpressFunctionBaseIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 12, 1, 1, 14),
    _LbSlotExpressFunctionBaseIndex_Type()
)
lbSlotExpressFunctionBaseIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbSlotExpressFunctionBaseIndex.setStatus("deprecated")
_LbSlotExpressFddiPortCount_Type = Integer32
_LbSlotExpressFddiPortCount_Object = MibTableColumn
lbSlotExpressFddiPortCount = _LbSlotExpressFddiPortCount_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 12, 1, 1, 15),
    _LbSlotExpressFddiPortCount_Type()
)
lbSlotExpressFddiPortCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbSlotExpressFddiPortCount.setStatus("deprecated")
_LbSlotExpressFddiPortBaseIndex_Type = Integer32
_LbSlotExpressFddiPortBaseIndex_Object = MibTableColumn
lbSlotExpressFddiPortBaseIndex = _LbSlotExpressFddiPortBaseIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 12, 1, 1, 16),
    _LbSlotExpressFddiPortBaseIndex_Type()
)
lbSlotExpressFddiPortBaseIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbSlotExpressFddiPortBaseIndex.setStatus("deprecated")
_LbSlotExpressEthernetPortCount_Type = Integer32
_LbSlotExpressEthernetPortCount_Object = MibTableColumn
lbSlotExpressEthernetPortCount = _LbSlotExpressEthernetPortCount_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 12, 1, 1, 17),
    _LbSlotExpressEthernetPortCount_Type()
)
lbSlotExpressEthernetPortCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbSlotExpressEthernetPortCount.setStatus("deprecated")
_LbSlotExpressEthernetPortBaseIndex_Type = Integer32
_LbSlotExpressEthernetPortBaseIndex_Object = MibTableColumn
lbSlotExpressEthernetPortBaseIndex = _LbSlotExpressEthernetPortBaseIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 12, 1, 1, 18),
    _LbSlotExpressEthernetPortBaseIndex_Type()
)
lbSlotExpressEthernetPortBaseIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbSlotExpressEthernetPortBaseIndex.setStatus("deprecated")


class _LbSlotBoardAction_Type(Integer32):
    """Custom type lbSlotBoardAction based on Integer32"""
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


_LbSlotBoardAction_Type.__name__ = "Integer32"
_LbSlotBoardAction_Object = MibTableColumn
lbSlotBoardAction = _LbSlotBoardAction_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 12, 1, 1, 19),
    _LbSlotBoardAction_Type()
)
lbSlotBoardAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lbSlotBoardAction.setStatus("mandatory")
_LbSlotBridgeFunctionCount_Type = Integer32
_LbSlotBridgeFunctionCount_Object = MibTableColumn
lbSlotBridgeFunctionCount = _LbSlotBridgeFunctionCount_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 12, 1, 1, 20),
    _LbSlotBridgeFunctionCount_Type()
)
lbSlotBridgeFunctionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbSlotBridgeFunctionCount.setStatus("mandatory")
_LbSlotBridgeFunctionBaseIndex_Type = Integer32
_LbSlotBridgeFunctionBaseIndex_Object = MibTableColumn
lbSlotBridgeFunctionBaseIndex = _LbSlotBridgeFunctionBaseIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 12, 1, 1, 21),
    _LbSlotBridgeFunctionBaseIndex_Type()
)
lbSlotBridgeFunctionBaseIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbSlotBridgeFunctionBaseIndex.setStatus("mandatory")
_LbFddiMac_ObjectIdentity = ObjectIdentity
lbFddiMac = _LbFddiMac_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 13)
)
_LbFddiMacTable_Object = MibTable
lbFddiMacTable = _LbFddiMacTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 13, 1)
)
if mibBuilder.loadTexts:
    lbFddiMacTable.setStatus("mandatory")
_LbFddiMacEntry_Object = MibTableRow
lbFddiMacEntry = _LbFddiMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 13, 1, 1)
)
lbFddiMacEntry.setIndexNames(
    (0, "LB3GH-1-0-7", "lbFddiMacIndex"),
)
if mibBuilder.loadTexts:
    lbFddiMacEntry.setStatus("mandatory")
_LbFddiMacIndex_Type = Integer32
_LbFddiMacIndex_Object = MibTableColumn
lbFddiMacIndex = _LbFddiMacIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 13, 1, 1, 1),
    _LbFddiMacIndex_Type()
)
lbFddiMacIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbFddiMacIndex.setStatus("mandatory")
_LbFddiMacSlotIndex_Type = Integer32
_LbFddiMacSlotIndex_Object = MibTableColumn
lbFddiMacSlotIndex = _LbFddiMacSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 13, 1, 1, 2),
    _LbFddiMacSlotIndex_Type()
)
lbFddiMacSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbFddiMacSlotIndex.setStatus("mandatory")
_LbFddiMacLocalIndex_Type = Integer32
_LbFddiMacLocalIndex_Object = MibTableColumn
lbFddiMacLocalIndex = _LbFddiMacLocalIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 13, 1, 1, 3),
    _LbFddiMacLocalIndex_Type()
)
lbFddiMacLocalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbFddiMacLocalIndex.setStatus("mandatory")
_LbFddiMacByteReceiveRate_Type = Integer32
_LbFddiMacByteReceiveRate_Object = MibTableColumn
lbFddiMacByteReceiveRate = _LbFddiMacByteReceiveRate_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 13, 1, 1, 4),
    _LbFddiMacByteReceiveRate_Type()
)
lbFddiMacByteReceiveRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbFddiMacByteReceiveRate.setStatus("mandatory")
_LbFddiMacPeakByteReceiveRate_Type = Integer32
_LbFddiMacPeakByteReceiveRate_Object = MibTableColumn
lbFddiMacPeakByteReceiveRate = _LbFddiMacPeakByteReceiveRate_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 13, 1, 1, 5),
    _LbFddiMacPeakByteReceiveRate_Type()
)
lbFddiMacPeakByteReceiveRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbFddiMacPeakByteReceiveRate.setStatus("mandatory")
_LbFddiMacFrameReceiveRate_Type = Integer32
_LbFddiMacFrameReceiveRate_Object = MibTableColumn
lbFddiMacFrameReceiveRate = _LbFddiMacFrameReceiveRate_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 13, 1, 1, 6),
    _LbFddiMacFrameReceiveRate_Type()
)
lbFddiMacFrameReceiveRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbFddiMacFrameReceiveRate.setStatus("mandatory")
_LbFddiMacPeakFrameReceiveRate_Type = Integer32
_LbFddiMacPeakFrameReceiveRate_Object = MibTableColumn
lbFddiMacPeakFrameReceiveRate = _LbFddiMacPeakFrameReceiveRate_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 13, 1, 1, 7),
    _LbFddiMacPeakFrameReceiveRate_Type()
)
lbFddiMacPeakFrameReceiveRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbFddiMacPeakFrameReceiveRate.setStatus("mandatory")
_LbFddiMacByteTransmitRate_Type = Integer32
_LbFddiMacByteTransmitRate_Object = MibTableColumn
lbFddiMacByteTransmitRate = _LbFddiMacByteTransmitRate_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 13, 1, 1, 8),
    _LbFddiMacByteTransmitRate_Type()
)
lbFddiMacByteTransmitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbFddiMacByteTransmitRate.setStatus("mandatory")
_LbFddiMacPeakByteTransmitRate_Type = Integer32
_LbFddiMacPeakByteTransmitRate_Object = MibTableColumn
lbFddiMacPeakByteTransmitRate = _LbFddiMacPeakByteTransmitRate_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 13, 1, 1, 9),
    _LbFddiMacPeakByteTransmitRate_Type()
)
lbFddiMacPeakByteTransmitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbFddiMacPeakByteTransmitRate.setStatus("mandatory")
_LbFddiMacFrameTransmitRate_Type = Integer32
_LbFddiMacFrameTransmitRate_Object = MibTableColumn
lbFddiMacFrameTransmitRate = _LbFddiMacFrameTransmitRate_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 13, 1, 1, 10),
    _LbFddiMacFrameTransmitRate_Type()
)
lbFddiMacFrameTransmitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbFddiMacFrameTransmitRate.setStatus("mandatory")
_LbFddiMacPeakFrameTransmitRate_Type = Integer32
_LbFddiMacPeakFrameTransmitRate_Object = MibTableColumn
lbFddiMacPeakFrameTransmitRate = _LbFddiMacPeakFrameTransmitRate_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 13, 1, 1, 11),
    _LbFddiMacPeakFrameTransmitRate_Type()
)
lbFddiMacPeakFrameTransmitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbFddiMacPeakFrameTransmitRate.setStatus("mandatory")
_LbFddiMacReceiveMulticastThreshold_Type = Integer32
_LbFddiMacReceiveMulticastThreshold_Object = MibTableColumn
lbFddiMacReceiveMulticastThreshold = _LbFddiMacReceiveMulticastThreshold_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 13, 1, 1, 12),
    _LbFddiMacReceiveMulticastThreshold_Type()
)
lbFddiMacReceiveMulticastThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lbFddiMacReceiveMulticastThreshold.setStatus("mandatory")


class _LbFddiMacBeaconHistory_Type(OctetString):
    """Custom type lbFddiMacBeaconHistory based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_LbFddiMacBeaconHistory_Type.__name__ = "OctetString"
_LbFddiMacBeaconHistory_Object = MibTableColumn
lbFddiMacBeaconHistory = _LbFddiMacBeaconHistory_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 13, 1, 1, 13),
    _LbFddiMacBeaconHistory_Type()
)
lbFddiMacBeaconHistory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbFddiMacBeaconHistory.setStatus("mandatory")
_LbEthernetPort_ObjectIdentity = ObjectIdentity
lbEthernetPort = _LbEthernetPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 14)
)
_LbEthernetPortTable_Object = MibTable
lbEthernetPortTable = _LbEthernetPortTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 14, 1)
)
if mibBuilder.loadTexts:
    lbEthernetPortTable.setStatus("mandatory")
_LbEthernetPortEntry_Object = MibTableRow
lbEthernetPortEntry = _LbEthernetPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 14, 1, 1)
)
lbEthernetPortEntry.setIndexNames(
    (0, "LB3GH-1-0-7", "lbEthernetPortIndex"),
)
if mibBuilder.loadTexts:
    lbEthernetPortEntry.setStatus("mandatory")
_LbEthernetPortIndex_Type = Integer32
_LbEthernetPortIndex_Object = MibTableColumn
lbEthernetPortIndex = _LbEthernetPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 14, 1, 1, 1),
    _LbEthernetPortIndex_Type()
)
lbEthernetPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbEthernetPortIndex.setStatus("mandatory")
_LbEthernetPortSlotIndex_Type = Integer32
_LbEthernetPortSlotIndex_Object = MibTableColumn
lbEthernetPortSlotIndex = _LbEthernetPortSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 14, 1, 1, 2),
    _LbEthernetPortSlotIndex_Type()
)
lbEthernetPortSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbEthernetPortSlotIndex.setStatus("mandatory")
_LbEthernetPortLocalIndex_Type = Integer32
_LbEthernetPortLocalIndex_Object = MibTableColumn
lbEthernetPortLocalIndex = _LbEthernetPortLocalIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 14, 1, 1, 3),
    _LbEthernetPortLocalIndex_Type()
)
lbEthernetPortLocalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbEthernetPortLocalIndex.setStatus("mandatory")


class _LbEthernetPortLabel_Type(DisplayString):
    """Custom type lbEthernetPortLabel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LbEthernetPortLabel_Type.__name__ = "DisplayString"
_LbEthernetPortLabel_Object = MibTableColumn
lbEthernetPortLabel = _LbEthernetPortLabel_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 14, 1, 1, 4),
    _LbEthernetPortLabel_Type()
)
lbEthernetPortLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lbEthernetPortLabel.setStatus("mandatory")


class _LbEthernetPortChipsetType_Type(Integer32):
    """Custom type lbEthernetPortChipsetType based on Integer32"""
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


_LbEthernetPortChipsetType_Type.__name__ = "Integer32"
_LbEthernetPortChipsetType_Object = MibTableColumn
lbEthernetPortChipsetType = _LbEthernetPortChipsetType_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 14, 1, 1, 5),
    _LbEthernetPortChipsetType_Type()
)
lbEthernetPortChipsetType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbEthernetPortChipsetType.setStatus("mandatory")


class _LbEthernetPortLinkStatus_Type(Integer32):
    """Custom type lbEthernetPortLinkStatus based on Integer32"""
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


_LbEthernetPortLinkStatus_Type.__name__ = "Integer32"
_LbEthernetPortLinkStatus_Object = MibTableColumn
lbEthernetPortLinkStatus = _LbEthernetPortLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 14, 1, 1, 6),
    _LbEthernetPortLinkStatus_Type()
)
lbEthernetPortLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbEthernetPortLinkStatus.setStatus("mandatory")
_LbEthernetPortByteReceiveRate_Type = Integer32
_LbEthernetPortByteReceiveRate_Object = MibTableColumn
lbEthernetPortByteReceiveRate = _LbEthernetPortByteReceiveRate_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 14, 1, 1, 7),
    _LbEthernetPortByteReceiveRate_Type()
)
lbEthernetPortByteReceiveRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbEthernetPortByteReceiveRate.setStatus("mandatory")
_LbEthernetPortPeakByteReceiveRate_Type = Integer32
_LbEthernetPortPeakByteReceiveRate_Object = MibTableColumn
lbEthernetPortPeakByteReceiveRate = _LbEthernetPortPeakByteReceiveRate_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 14, 1, 1, 8),
    _LbEthernetPortPeakByteReceiveRate_Type()
)
lbEthernetPortPeakByteReceiveRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbEthernetPortPeakByteReceiveRate.setStatus("mandatory")
_LbEthernetPortFrameReceiveRate_Type = Integer32
_LbEthernetPortFrameReceiveRate_Object = MibTableColumn
lbEthernetPortFrameReceiveRate = _LbEthernetPortFrameReceiveRate_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 14, 1, 1, 9),
    _LbEthernetPortFrameReceiveRate_Type()
)
lbEthernetPortFrameReceiveRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbEthernetPortFrameReceiveRate.setStatus("mandatory")
_LbEthernetPortPeakFrameReceiveRate_Type = Integer32
_LbEthernetPortPeakFrameReceiveRate_Object = MibTableColumn
lbEthernetPortPeakFrameReceiveRate = _LbEthernetPortPeakFrameReceiveRate_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 14, 1, 1, 10),
    _LbEthernetPortPeakFrameReceiveRate_Type()
)
lbEthernetPortPeakFrameReceiveRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbEthernetPortPeakFrameReceiveRate.setStatus("mandatory")
_LbEthernetPortByteTransmitRate_Type = Integer32
_LbEthernetPortByteTransmitRate_Object = MibTableColumn
lbEthernetPortByteTransmitRate = _LbEthernetPortByteTransmitRate_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 14, 1, 1, 11),
    _LbEthernetPortByteTransmitRate_Type()
)
lbEthernetPortByteTransmitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbEthernetPortByteTransmitRate.setStatus("mandatory")
_LbEthernetPortPeakByteTransmitRate_Type = Integer32
_LbEthernetPortPeakByteTransmitRate_Object = MibTableColumn
lbEthernetPortPeakByteTransmitRate = _LbEthernetPortPeakByteTransmitRate_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 14, 1, 1, 12),
    _LbEthernetPortPeakByteTransmitRate_Type()
)
lbEthernetPortPeakByteTransmitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbEthernetPortPeakByteTransmitRate.setStatus("mandatory")
_LbEthernetPortFrameTransmitRate_Type = Integer32
_LbEthernetPortFrameTransmitRate_Object = MibTableColumn
lbEthernetPortFrameTransmitRate = _LbEthernetPortFrameTransmitRate_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 14, 1, 1, 13),
    _LbEthernetPortFrameTransmitRate_Type()
)
lbEthernetPortFrameTransmitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbEthernetPortFrameTransmitRate.setStatus("mandatory")
_LbEthernetPortPeakFrameTransmitRate_Type = Integer32
_LbEthernetPortPeakFrameTransmitRate_Object = MibTableColumn
lbEthernetPortPeakFrameTransmitRate = _LbEthernetPortPeakFrameTransmitRate_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 14, 1, 1, 14),
    _LbEthernetPortPeakFrameTransmitRate_Type()
)
lbEthernetPortPeakFrameTransmitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbEthernetPortPeakFrameTransmitRate.setStatus("mandatory")
_LbEthernetPortReceiveMulticastThreshold_Type = Integer32
_LbEthernetPortReceiveMulticastThreshold_Object = MibTableColumn
lbEthernetPortReceiveMulticastThreshold = _LbEthernetPortReceiveMulticastThreshold_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 14, 1, 1, 15),
    _LbEthernetPortReceiveMulticastThreshold_Type()
)
lbEthernetPortReceiveMulticastThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lbEthernetPortReceiveMulticastThreshold.setStatus("mandatory")


class _LbEthernetPortType_Type(Integer32):
    """Custom type lbEthernetPortType based on Integer32"""
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


_LbEthernetPortType_Type.__name__ = "Integer32"
_LbEthernetPortType_Object = MibTableColumn
lbEthernetPortType = _LbEthernetPortType_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 14, 1, 1, 16),
    _LbEthernetPortType_Type()
)
lbEthernetPortType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lbEthernetPortType.setStatus("mandatory")
_LbFddiPort_ObjectIdentity = ObjectIdentity
lbFddiPort = _LbFddiPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 15)
)
_LbFddiPortTable_Object = MibTable
lbFddiPortTable = _LbFddiPortTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 15, 1)
)
if mibBuilder.loadTexts:
    lbFddiPortTable.setStatus("mandatory")
_LbFddiPortEntry_Object = MibTableRow
lbFddiPortEntry = _LbFddiPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 15, 1, 1)
)
lbFddiPortEntry.setIndexNames(
    (0, "LB3GH-1-0-7", "lbFddiPortIndex"),
)
if mibBuilder.loadTexts:
    lbFddiPortEntry.setStatus("mandatory")
_LbFddiPortIndex_Type = Integer32
_LbFddiPortIndex_Object = MibTableColumn
lbFddiPortIndex = _LbFddiPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 15, 1, 1, 1),
    _LbFddiPortIndex_Type()
)
lbFddiPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbFddiPortIndex.setStatus("mandatory")
_LbFddiPortSlotIndex_Type = Integer32
_LbFddiPortSlotIndex_Object = MibTableColumn
lbFddiPortSlotIndex = _LbFddiPortSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 15, 1, 1, 2),
    _LbFddiPortSlotIndex_Type()
)
lbFddiPortSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbFddiPortSlotIndex.setStatus("mandatory")
_LbFddiPortLocalIndex_Type = Integer32
_LbFddiPortLocalIndex_Object = MibTableColumn
lbFddiPortLocalIndex = _LbFddiPortLocalIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 15, 1, 1, 3),
    _LbFddiPortLocalIndex_Type()
)
lbFddiPortLocalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbFddiPortLocalIndex.setStatus("mandatory")


class _LbFddiPortLabel_Type(DisplayString):
    """Custom type lbFddiPortLabel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LbFddiPortLabel_Type.__name__ = "DisplayString"
_LbFddiPortLabel_Object = MibTableColumn
lbFddiPortLabel = _LbFddiPortLabel_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 15, 1, 1, 4),
    _LbFddiPortLabel_Type()
)
lbFddiPortLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lbFddiPortLabel.setStatus("mandatory")
_LbExpress_ObjectIdentity = ObjectIdentity
lbExpress = _LbExpress_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 16)
)
_LbExpressTable_Object = MibTable
lbExpressTable = _LbExpressTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 16, 1)
)
if mibBuilder.loadTexts:
    lbExpressTable.setStatus("deprecated")
_LbExpressEntry_Object = MibTableRow
lbExpressEntry = _LbExpressEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 16, 1, 1)
)
lbExpressEntry.setIndexNames(
    (0, "LB3GH-1-0-7", "lbExpressIndex"),
)
if mibBuilder.loadTexts:
    lbExpressEntry.setStatus("deprecated")
_LbExpressIndex_Type = Integer32
_LbExpressIndex_Object = MibTableColumn
lbExpressIndex = _LbExpressIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 16, 1, 1, 1),
    _LbExpressIndex_Type()
)
lbExpressIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbExpressIndex.setStatus("deprecated")
_LbExpressSlotIndex_Type = Integer32
_LbExpressSlotIndex_Object = MibTableColumn
lbExpressSlotIndex = _LbExpressSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 16, 1, 1, 2),
    _LbExpressSlotIndex_Type()
)
lbExpressSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbExpressSlotIndex.setStatus("deprecated")
_LbExpressLocalIndex_Type = Integer32
_LbExpressLocalIndex_Object = MibTableColumn
lbExpressLocalIndex = _LbExpressLocalIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 16, 1, 1, 3),
    _LbExpressLocalIndex_Type()
)
lbExpressLocalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbExpressLocalIndex.setStatus("deprecated")
_LbExpressAddressThreshold_Type = Integer32
_LbExpressAddressThreshold_Object = MibTableColumn
lbExpressAddressThreshold = _LbExpressAddressThreshold_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 16, 1, 1, 4),
    _LbExpressAddressThreshold_Type()
)
lbExpressAddressThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lbExpressAddressThreshold.setStatus("deprecated")
_LbExpressFddiPort_ObjectIdentity = ObjectIdentity
lbExpressFddiPort = _LbExpressFddiPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 17)
)
_LbExpressFddiPortTable_Object = MibTable
lbExpressFddiPortTable = _LbExpressFddiPortTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 17, 1)
)
if mibBuilder.loadTexts:
    lbExpressFddiPortTable.setStatus("deprecated")
_LbExpressFddiPortEntry_Object = MibTableRow
lbExpressFddiPortEntry = _LbExpressFddiPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 17, 1, 1)
)
lbExpressFddiPortEntry.setIndexNames(
    (0, "LB3GH-1-0-7", "lbExpressFddiPortIndex"),
)
if mibBuilder.loadTexts:
    lbExpressFddiPortEntry.setStatus("deprecated")
_LbExpressFddiPortIndex_Type = Integer32
_LbExpressFddiPortIndex_Object = MibTableColumn
lbExpressFddiPortIndex = _LbExpressFddiPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 17, 1, 1, 1),
    _LbExpressFddiPortIndex_Type()
)
lbExpressFddiPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbExpressFddiPortIndex.setStatus("deprecated")
_LbExpressFddiPortSlotIndex_Type = Integer32
_LbExpressFddiPortSlotIndex_Object = MibTableColumn
lbExpressFddiPortSlotIndex = _LbExpressFddiPortSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 17, 1, 1, 2),
    _LbExpressFddiPortSlotIndex_Type()
)
lbExpressFddiPortSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbExpressFddiPortSlotIndex.setStatus("deprecated")
_LbExpressFddiPortLocalIndex_Type = Integer32
_LbExpressFddiPortLocalIndex_Object = MibTableColumn
lbExpressFddiPortLocalIndex = _LbExpressFddiPortLocalIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 17, 1, 1, 3),
    _LbExpressFddiPortLocalIndex_Type()
)
lbExpressFddiPortLocalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbExpressFddiPortLocalIndex.setStatus("deprecated")
_LbExpressFddiPortForwardedCts_Type = Counter32
_LbExpressFddiPortForwardedCts_Object = MibTableColumn
lbExpressFddiPortForwardedCts = _LbExpressFddiPortForwardedCts_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 17, 1, 1, 4),
    _LbExpressFddiPortForwardedCts_Type()
)
lbExpressFddiPortForwardedCts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbExpressFddiPortForwardedCts.setStatus("deprecated")
_LbExpressFddiPortDroppedCts_Type = Counter32
_LbExpressFddiPortDroppedCts_Object = MibTableColumn
lbExpressFddiPortDroppedCts = _LbExpressFddiPortDroppedCts_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 17, 1, 1, 5),
    _LbExpressFddiPortDroppedCts_Type()
)
lbExpressFddiPortDroppedCts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbExpressFddiPortDroppedCts.setStatus("deprecated")
_LbExpressEthernetPort_ObjectIdentity = ObjectIdentity
lbExpressEthernetPort = _LbExpressEthernetPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 18)
)
_LbExpressEthernetPortTable_Object = MibTable
lbExpressEthernetPortTable = _LbExpressEthernetPortTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 18, 1)
)
if mibBuilder.loadTexts:
    lbExpressEthernetPortTable.setStatus("deprecated")
_LbExpressEthernetPortEntry_Object = MibTableRow
lbExpressEthernetPortEntry = _LbExpressEthernetPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 18, 1, 1)
)
lbExpressEthernetPortEntry.setIndexNames(
    (0, "LB3GH-1-0-7", "lbExpressEthernetPortIndex"),
)
if mibBuilder.loadTexts:
    lbExpressEthernetPortEntry.setStatus("deprecated")
_LbExpressEthernetPortIndex_Type = Integer32
_LbExpressEthernetPortIndex_Object = MibTableColumn
lbExpressEthernetPortIndex = _LbExpressEthernetPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 18, 1, 1, 1),
    _LbExpressEthernetPortIndex_Type()
)
lbExpressEthernetPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbExpressEthernetPortIndex.setStatus("deprecated")
_LbExpressEthernetPortSlotIndex_Type = Integer32
_LbExpressEthernetPortSlotIndex_Object = MibTableColumn
lbExpressEthernetPortSlotIndex = _LbExpressEthernetPortSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 18, 1, 1, 2),
    _LbExpressEthernetPortSlotIndex_Type()
)
lbExpressEthernetPortSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbExpressEthernetPortSlotIndex.setStatus("deprecated")
_LbExpressEthernetPortLocalIndex_Type = Integer32
_LbExpressEthernetPortLocalIndex_Object = MibTableColumn
lbExpressEthernetPortLocalIndex = _LbExpressEthernetPortLocalIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 18, 1, 1, 3),
    _LbExpressEthernetPortLocalIndex_Type()
)
lbExpressEthernetPortLocalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbExpressEthernetPortLocalIndex.setStatus("deprecated")
_LbExpressEthernetPortForwardedCts_Type = Counter32
_LbExpressEthernetPortForwardedCts_Object = MibTableColumn
lbExpressEthernetPortForwardedCts = _LbExpressEthernetPortForwardedCts_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 18, 1, 1, 4),
    _LbExpressEthernetPortForwardedCts_Type()
)
lbExpressEthernetPortForwardedCts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbExpressEthernetPortForwardedCts.setStatus("deprecated")
_LbExpressEthernetPortDroppedCts_Type = Counter32
_LbExpressEthernetPortDroppedCts_Object = MibTableColumn
lbExpressEthernetPortDroppedCts = _LbExpressEthernetPortDroppedCts_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 18, 1, 1, 5),
    _LbExpressEthernetPortDroppedCts_Type()
)
lbExpressEthernetPortDroppedCts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbExpressEthernetPortDroppedCts.setStatus("deprecated")
_LbExpressEthernetPortUTurnCts_Type = Counter32
_LbExpressEthernetPortUTurnCts_Object = MibTableColumn
lbExpressEthernetPortUTurnCts = _LbExpressEthernetPortUTurnCts_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 18, 1, 1, 6),
    _LbExpressEthernetPortUTurnCts_Type()
)
lbExpressEthernetPortUTurnCts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbExpressEthernetPortUTurnCts.setStatus("deprecated")


class _LbExpressEthernetPortAction_Type(Integer32):
    """Custom type lbExpressEthernetPortAction based on Integer32"""
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


_LbExpressEthernetPortAction_Type.__name__ = "Integer32"
_LbExpressEthernetPortAction_Object = MibTableColumn
lbExpressEthernetPortAction = _LbExpressEthernetPortAction_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 18, 1, 1, 7),
    _LbExpressEthernetPortAction_Type()
)
lbExpressEthernetPortAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lbExpressEthernetPortAction.setStatus("deprecated")
_LbExpressEthernetPortAddress_ObjectIdentity = ObjectIdentity
lbExpressEthernetPortAddress = _LbExpressEthernetPortAddress_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 19)
)
_LbExpressEthernetPortAddressTable_Object = MibTable
lbExpressEthernetPortAddressTable = _LbExpressEthernetPortAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 19, 1)
)
if mibBuilder.loadTexts:
    lbExpressEthernetPortAddressTable.setStatus("deprecated")
_LbExpressEthernetPortAddressEntry_Object = MibTableRow
lbExpressEthernetPortAddressEntry = _LbExpressEthernetPortAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 19, 1, 1)
)
lbExpressEthernetPortAddressEntry.setIndexNames(
    (0, "LB3GH-1-0-7", "lbExpressEthernetPortAddressPortIndex"),
    (0, "LB3GH-1-0-7", "lbExpressEthernetPortAddressIndex"),
)
if mibBuilder.loadTexts:
    lbExpressEthernetPortAddressEntry.setStatus("deprecated")
_LbExpressEthernetPortAddressPortIndex_Type = Integer32
_LbExpressEthernetPortAddressPortIndex_Object = MibTableColumn
lbExpressEthernetPortAddressPortIndex = _LbExpressEthernetPortAddressPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 19, 1, 1, 1),
    _LbExpressEthernetPortAddressPortIndex_Type()
)
lbExpressEthernetPortAddressPortIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lbExpressEthernetPortAddressPortIndex.setStatus("deprecated")
_LbExpressEthernetPortAddressIndex_Type = Integer32
_LbExpressEthernetPortAddressIndex_Object = MibTableColumn
lbExpressEthernetPortAddressIndex = _LbExpressEthernetPortAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 19, 1, 1, 2),
    _LbExpressEthernetPortAddressIndex_Type()
)
lbExpressEthernetPortAddressIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lbExpressEthernetPortAddressIndex.setStatus("deprecated")
_LbExpressEthernetPortAddressSlotIndex_Type = Integer32
_LbExpressEthernetPortAddressSlotIndex_Object = MibTableColumn
lbExpressEthernetPortAddressSlotIndex = _LbExpressEthernetPortAddressSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 19, 1, 1, 3),
    _LbExpressEthernetPortAddressSlotIndex_Type()
)
lbExpressEthernetPortAddressSlotIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lbExpressEthernetPortAddressSlotIndex.setStatus("deprecated")


class _LbExpressEthernetPortAddressType_Type(Integer32):
    """Custom type lbExpressEthernetPortAddressType based on Integer32"""
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


_LbExpressEthernetPortAddressType_Type.__name__ = "Integer32"
_LbExpressEthernetPortAddressType_Object = MibTableColumn
lbExpressEthernetPortAddressType = _LbExpressEthernetPortAddressType_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 19, 1, 1, 4),
    _LbExpressEthernetPortAddressType_Type()
)
lbExpressEthernetPortAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lbExpressEthernetPortAddressType.setStatus("deprecated")


class _LbExpressEthernetPortAddressRemoteAddress_Type(OctetString):
    """Custom type lbExpressEthernetPortAddressRemoteAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_LbExpressEthernetPortAddressRemoteAddress_Type.__name__ = "OctetString"
_LbExpressEthernetPortAddressRemoteAddress_Object = MibTableColumn
lbExpressEthernetPortAddressRemoteAddress = _LbExpressEthernetPortAddressRemoteAddress_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 19, 1, 1, 5),
    _LbExpressEthernetPortAddressRemoteAddress_Type()
)
lbExpressEthernetPortAddressRemoteAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lbExpressEthernetPortAddressRemoteAddress.setStatus("deprecated")


class _LbExpressEthernetPortAddressIsStatic_Type(Integer32):
    """Custom type lbExpressEthernetPortAddressIsStatic based on Integer32"""
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


_LbExpressEthernetPortAddressIsStatic_Type.__name__ = "Integer32"
_LbExpressEthernetPortAddressIsStatic_Object = MibTableColumn
lbExpressEthernetPortAddressIsStatic = _LbExpressEthernetPortAddressIsStatic_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 19, 1, 1, 6),
    _LbExpressEthernetPortAddressIsStatic_Type()
)
lbExpressEthernetPortAddressIsStatic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lbExpressEthernetPortAddressIsStatic.setStatus("deprecated")
_LbExpressEthernetPortAddressStaticPort_Type = Integer32
_LbExpressEthernetPortAddressStaticPort_Object = MibTableColumn
lbExpressEthernetPortAddressStaticPort = _LbExpressEthernetPortAddressStaticPort_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 19, 1, 1, 7),
    _LbExpressEthernetPortAddressStaticPort_Type()
)
lbExpressEthernetPortAddressStaticPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lbExpressEthernetPortAddressStaticPort.setStatus("deprecated")
_LbExpressEthernetPortAddressAge_Type = Integer32
_LbExpressEthernetPortAddressAge_Object = MibTableColumn
lbExpressEthernetPortAddressAge = _LbExpressEthernetPortAddressAge_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 19, 1, 1, 8),
    _LbExpressEthernetPortAddressAge_Type()
)
lbExpressEthernetPortAddressAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lbExpressEthernetPortAddressAge.setStatus("deprecated")
_LbPowerSupply_ObjectIdentity = ObjectIdentity
lbPowerSupply = _LbPowerSupply_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 20)
)
_LbPowerSupplyTable_Object = MibTable
lbPowerSupplyTable = _LbPowerSupplyTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 20, 1)
)
if mibBuilder.loadTexts:
    lbPowerSupplyTable.setStatus("mandatory")
_LbPowerSupplyEntry_Object = MibTableRow
lbPowerSupplyEntry = _LbPowerSupplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 20, 1, 1)
)
lbPowerSupplyEntry.setIndexNames(
    (0, "LB3GH-1-0-7", "lbPowerSupplyIndex"),
)
if mibBuilder.loadTexts:
    lbPowerSupplyEntry.setStatus("mandatory")
_LbPowerSupplyIndex_Type = Integer32
_LbPowerSupplyIndex_Object = MibTableColumn
lbPowerSupplyIndex = _LbPowerSupplyIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 20, 1, 1, 1),
    _LbPowerSupplyIndex_Type()
)
lbPowerSupplyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbPowerSupplyIndex.setStatus("mandatory")
_LbPowerSupplyLocation_Type = Integer32
_LbPowerSupplyLocation_Object = MibTableColumn
lbPowerSupplyLocation = _LbPowerSupplyLocation_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 20, 1, 1, 2),
    _LbPowerSupplyLocation_Type()
)
lbPowerSupplyLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbPowerSupplyLocation.setStatus("mandatory")
_LbPowerSupplyStatus_Type = Integer32
_LbPowerSupplyStatus_Object = MibTableColumn
lbPowerSupplyStatus = _LbPowerSupplyStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 20, 1, 1, 3),
    _LbPowerSupplyStatus_Type()
)
lbPowerSupplyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbPowerSupplyStatus.setStatus("mandatory")


class _LbPowerSupplyFailureType_Type(Integer32):
    """Custom type lbPowerSupplyFailureType based on Integer32"""
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


_LbPowerSupplyFailureType_Type.__name__ = "Integer32"
_LbPowerSupplyFailureType_Object = MibTableColumn
lbPowerSupplyFailureType = _LbPowerSupplyFailureType_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 20, 1, 1, 4),
    _LbPowerSupplyFailureType_Type()
)
lbPowerSupplyFailureType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lbPowerSupplyFailureType.setStatus("deprecated")


class _LbPowerSupplyLastFailure_Type(Integer32):
    """Custom type lbPowerSupplyLastFailure based on Integer32"""
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


_LbPowerSupplyLastFailure_Type.__name__ = "Integer32"
_LbPowerSupplyLastFailure_Object = MibTableColumn
lbPowerSupplyLastFailure = _LbPowerSupplyLastFailure_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 20, 1, 1, 5),
    _LbPowerSupplyLastFailure_Type()
)
lbPowerSupplyLastFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbPowerSupplyLastFailure.setStatus("mandatory")
_LbBridge_ObjectIdentity = ObjectIdentity
lbBridge = _LbBridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 21)
)
_LbBridgeTable_Object = MibTable
lbBridgeTable = _LbBridgeTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 21, 1)
)
if mibBuilder.loadTexts:
    lbBridgeTable.setStatus("mandatory")
_LbBridgeEntry_Object = MibTableRow
lbBridgeEntry = _LbBridgeEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 21, 1, 1)
)
lbBridgeEntry.setIndexNames(
    (0, "LB3GH-1-0-7", "lbBridgeIndex"),
)
if mibBuilder.loadTexts:
    lbBridgeEntry.setStatus("mandatory")
_LbBridgeIndex_Type = Integer32
_LbBridgeIndex_Object = MibTableColumn
lbBridgeIndex = _LbBridgeIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 21, 1, 1, 1),
    _LbBridgeIndex_Type()
)
lbBridgeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbBridgeIndex.setStatus("mandatory")
_LbBridgeBaseSlotIndex_Type = Integer32
_LbBridgeBaseSlotIndex_Object = MibTableColumn
lbBridgeBaseSlotIndex = _LbBridgeBaseSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 21, 1, 1, 2),
    _LbBridgeBaseSlotIndex_Type()
)
lbBridgeBaseSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbBridgeBaseSlotIndex.setStatus("mandatory")
_LbBridgePortCount_Type = Integer32
_LbBridgePortCount_Object = MibTableColumn
lbBridgePortCount = _LbBridgePortCount_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 21, 1, 1, 3),
    _LbBridgePortCount_Type()
)
lbBridgePortCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbBridgePortCount.setStatus("mandatory")
_LbBridgeAddressTableSize_Type = Integer32
_LbBridgeAddressTableSize_Object = MibTableColumn
lbBridgeAddressTableSize = _LbBridgeAddressTableSize_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 21, 1, 1, 4),
    _LbBridgeAddressTableSize_Type()
)
lbBridgeAddressTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbBridgeAddressTableSize.setStatus("mandatory")
_LbBridgeAddressThreshold_Type = Integer32
_LbBridgeAddressThreshold_Object = MibTableColumn
lbBridgeAddressThreshold = _LbBridgeAddressThreshold_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 21, 1, 1, 5),
    _LbBridgeAddressThreshold_Type()
)
lbBridgeAddressThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lbBridgeAddressThreshold.setStatus("mandatory")


class _LbBridgeMode_Type(Integer32):
    """Custom type lbBridgeMode based on Integer32"""
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


_LbBridgeMode_Type.__name__ = "Integer32"
_LbBridgeMode_Object = MibTableColumn
lbBridgeMode = _LbBridgeMode_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 21, 1, 1, 6),
    _LbBridgeMode_Type()
)
lbBridgeMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lbBridgeMode.setStatus("mandatory")
_LbBridgeLocalIndex_Type = Integer32
_LbBridgeLocalIndex_Object = MibTableColumn
lbBridgeLocalIndex = _LbBridgeLocalIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 21, 1, 1, 7),
    _LbBridgeLocalIndex_Type()
)
lbBridgeLocalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbBridgeLocalIndex.setStatus("mandatory")
_LbBridgePortTable_Object = MibTable
lbBridgePortTable = _LbBridgePortTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 21, 2)
)
if mibBuilder.loadTexts:
    lbBridgePortTable.setStatus("mandatory")
_LbBridgePortEntry_Object = MibTableRow
lbBridgePortEntry = _LbBridgePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 21, 2, 1)
)
lbBridgePortEntry.setIndexNames(
    (0, "LB3GH-1-0-7", "lbBridgePortBridgeIndex"),
    (0, "LB3GH-1-0-7", "lbBridgePortIndex"),
)
if mibBuilder.loadTexts:
    lbBridgePortEntry.setStatus("mandatory")
_LbBridgePortBridgeIndex_Type = Integer32
_LbBridgePortBridgeIndex_Object = MibTableColumn
lbBridgePortBridgeIndex = _LbBridgePortBridgeIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 21, 2, 1, 1),
    _LbBridgePortBridgeIndex_Type()
)
lbBridgePortBridgeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbBridgePortBridgeIndex.setStatus("mandatory")
_LbBridgePortIndex_Type = Integer32
_LbBridgePortIndex_Object = MibTableColumn
lbBridgePortIndex = _LbBridgePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 21, 2, 1, 2),
    _LbBridgePortIndex_Type()
)
lbBridgePortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbBridgePortIndex.setStatus("mandatory")
_LbBridgePortSlotIndex_Type = Integer32
_LbBridgePortSlotIndex_Object = MibTableColumn
lbBridgePortSlotIndex = _LbBridgePortSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 21, 2, 1, 3),
    _LbBridgePortSlotIndex_Type()
)
lbBridgePortSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbBridgePortSlotIndex.setStatus("mandatory")
_LbBridgePortLocalIndex_Type = Integer32
_LbBridgePortLocalIndex_Object = MibTableColumn
lbBridgePortLocalIndex = _LbBridgePortLocalIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 21, 2, 1, 4),
    _LbBridgePortLocalIndex_Type()
)
lbBridgePortLocalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbBridgePortLocalIndex.setStatus("mandatory")


class _LbBridgePortType_Type(Integer32):
    """Custom type lbBridgePortType based on Integer32"""
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


_LbBridgePortType_Type.__name__ = "Integer32"
_LbBridgePortType_Object = MibTableColumn
lbBridgePortType = _LbBridgePortType_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 21, 2, 1, 5),
    _LbBridgePortType_Type()
)
lbBridgePortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbBridgePortType.setStatus("mandatory")


class _LbBridgePortIpFragmentationEnabled_Type(Integer32):
    """Custom type lbBridgePortIpFragmentationEnabled based on Integer32"""
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


_LbBridgePortIpFragmentationEnabled_Type.__name__ = "Integer32"
_LbBridgePortIpFragmentationEnabled_Object = MibTableColumn
lbBridgePortIpFragmentationEnabled = _LbBridgePortIpFragmentationEnabled_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 21, 2, 1, 6),
    _LbBridgePortIpFragmentationEnabled_Type()
)
lbBridgePortIpFragmentationEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lbBridgePortIpFragmentationEnabled.setStatus("mandatory")


class _LbBridgePortReceiveMulticastLimit_Type(Integer32):
    """Custom type lbBridgePortReceiveMulticastLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_LbBridgePortReceiveMulticastLimit_Type.__name__ = "Integer32"
_LbBridgePortReceiveMulticastLimit_Object = MibTableColumn
lbBridgePortReceiveMulticastLimit = _LbBridgePortReceiveMulticastLimit_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 21, 2, 1, 7),
    _LbBridgePortReceiveMulticastLimit_Type()
)
lbBridgePortReceiveMulticastLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lbBridgePortReceiveMulticastLimit.setStatus("mandatory")


class _LbBridgePortAddressAction_Type(Integer32):
    """Custom type lbBridgePortAddressAction based on Integer32"""
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


_LbBridgePortAddressAction_Type.__name__ = "Integer32"
_LbBridgePortAddressAction_Object = MibTableColumn
lbBridgePortAddressAction = _LbBridgePortAddressAction_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 21, 2, 1, 8),
    _LbBridgePortAddressAction_Type()
)
lbBridgePortAddressAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lbBridgePortAddressAction.setStatus("mandatory")
_LbBridgePortTotalForwardedCts_Type = Counter32
_LbBridgePortTotalForwardedCts_Object = MibTableColumn
lbBridgePortTotalForwardedCts = _LbBridgePortTotalForwardedCts_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 21, 2, 1, 9),
    _LbBridgePortTotalForwardedCts_Type()
)
lbBridgePortTotalForwardedCts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbBridgePortTotalForwardedCts.setStatus("mandatory")
_LbBridgePortManagementFramesReceived_Type = Counter32
_LbBridgePortManagementFramesReceived_Object = MibTableColumn
lbBridgePortManagementFramesReceived = _LbBridgePortManagementFramesReceived_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 21, 2, 1, 10),
    _LbBridgePortManagementFramesReceived_Type()
)
lbBridgePortManagementFramesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbBridgePortManagementFramesReceived.setStatus("mandatory")
_LbBridgePortTotalDiscards_Type = Counter32
_LbBridgePortTotalDiscards_Object = MibTableColumn
lbBridgePortTotalDiscards = _LbBridgePortTotalDiscards_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 21, 2, 1, 11),
    _LbBridgePortTotalDiscards_Type()
)
lbBridgePortTotalDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbBridgePortTotalDiscards.setStatus("mandatory")
_LbBridgePortReceiveBlockedDiscards_Type = Counter32
_LbBridgePortReceiveBlockedDiscards_Object = MibTableColumn
lbBridgePortReceiveBlockedDiscards = _LbBridgePortReceiveBlockedDiscards_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 21, 2, 1, 12),
    _LbBridgePortReceiveBlockedDiscards_Type()
)
lbBridgePortReceiveBlockedDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbBridgePortReceiveBlockedDiscards.setStatus("mandatory")
_LbBridgePortReceiveMulticastLimitExceededs_Type = Counter32
_LbBridgePortReceiveMulticastLimitExceededs_Object = MibTableColumn
lbBridgePortReceiveMulticastLimitExceededs = _LbBridgePortReceiveMulticastLimitExceededs_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 21, 2, 1, 13),
    _LbBridgePortReceiveMulticastLimitExceededs_Type()
)
lbBridgePortReceiveMulticastLimitExceededs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbBridgePortReceiveMulticastLimitExceededs.setStatus("mandatory")
_LbBridgePortReceiveSecurityDiscards_Type = Counter32
_LbBridgePortReceiveSecurityDiscards_Object = MibTableColumn
lbBridgePortReceiveSecurityDiscards = _LbBridgePortReceiveSecurityDiscards_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 21, 2, 1, 14),
    _LbBridgePortReceiveSecurityDiscards_Type()
)
lbBridgePortReceiveSecurityDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbBridgePortReceiveSecurityDiscards.setStatus("mandatory")
_LbBridgePortReceiveUnknownDiscards_Type = Counter32
_LbBridgePortReceiveUnknownDiscards_Object = MibTableColumn
lbBridgePortReceiveUnknownDiscards = _LbBridgePortReceiveUnknownDiscards_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 21, 2, 1, 15),
    _LbBridgePortReceiveUnknownDiscards_Type()
)
lbBridgePortReceiveUnknownDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbBridgePortReceiveUnknownDiscards.setStatus("mandatory")
_LbBridgePortReceiveOtherDiscards_Type = Counter32
_LbBridgePortReceiveOtherDiscards_Object = MibTableColumn
lbBridgePortReceiveOtherDiscards = _LbBridgePortReceiveOtherDiscards_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 21, 2, 1, 16),
    _LbBridgePortReceiveOtherDiscards_Type()
)
lbBridgePortReceiveOtherDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbBridgePortReceiveOtherDiscards.setStatus("mandatory")
_LbBridgePortReceiveErrorDiscards_Type = Counter32
_LbBridgePortReceiveErrorDiscards_Object = MibTableColumn
lbBridgePortReceiveErrorDiscards = _LbBridgePortReceiveErrorDiscards_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 21, 2, 1, 17),
    _LbBridgePortReceiveErrorDiscards_Type()
)
lbBridgePortReceiveErrorDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbBridgePortReceiveErrorDiscards.setStatus("mandatory")
_LbBridgePortSameSegmentDiscards_Type = Counter32
_LbBridgePortSameSegmentDiscards_Object = MibTableColumn
lbBridgePortSameSegmentDiscards = _LbBridgePortSameSegmentDiscards_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 21, 2, 1, 18),
    _LbBridgePortSameSegmentDiscards_Type()
)
lbBridgePortSameSegmentDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbBridgePortSameSegmentDiscards.setStatus("mandatory")
_LbBridgePortTransmitBlockedDiscards_Type = Counter32
_LbBridgePortTransmitBlockedDiscards_Object = MibTableColumn
lbBridgePortTransmitBlockedDiscards = _LbBridgePortTransmitBlockedDiscards_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 21, 2, 1, 19),
    _LbBridgePortTransmitBlockedDiscards_Type()
)
lbBridgePortTransmitBlockedDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbBridgePortTransmitBlockedDiscards.setStatus("mandatory")
_LbBridgePortTotalFiltered_Type = Counter32
_LbBridgePortTotalFiltered_Object = MibTableColumn
lbBridgePortTotalFiltered = _LbBridgePortTotalFiltered_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 21, 2, 1, 20),
    _LbBridgePortTotalFiltered_Type()
)
lbBridgePortTotalFiltered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbBridgePortTotalFiltered.setStatus("mandatory")
_LbBridgePortReceiveUnicastFiltered_Type = Counter32
_LbBridgePortReceiveUnicastFiltered_Object = MibTableColumn
lbBridgePortReceiveUnicastFiltered = _LbBridgePortReceiveUnicastFiltered_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 21, 2, 1, 21),
    _LbBridgePortReceiveUnicastFiltered_Type()
)
lbBridgePortReceiveUnicastFiltered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbBridgePortReceiveUnicastFiltered.setStatus("mandatory")
_LbBridgePortReceiveMulticastFiltered_Type = Counter32
_LbBridgePortReceiveMulticastFiltered_Object = MibTableColumn
lbBridgePortReceiveMulticastFiltered = _LbBridgePortReceiveMulticastFiltered_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 21, 2, 1, 22),
    _LbBridgePortReceiveMulticastFiltered_Type()
)
lbBridgePortReceiveMulticastFiltered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbBridgePortReceiveMulticastFiltered.setStatus("mandatory")
_LbBridgePortTransmitUnicastFiltered_Type = Counter32
_LbBridgePortTransmitUnicastFiltered_Object = MibTableColumn
lbBridgePortTransmitUnicastFiltered = _LbBridgePortTransmitUnicastFiltered_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 21, 2, 1, 23),
    _LbBridgePortTransmitUnicastFiltered_Type()
)
lbBridgePortTransmitUnicastFiltered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbBridgePortTransmitUnicastFiltered.setStatus("mandatory")
_LbBridgePortTransmitMulticastFiltered_Type = Counter32
_LbBridgePortTransmitMulticastFiltered_Object = MibTableColumn
lbBridgePortTransmitMulticastFiltered = _LbBridgePortTransmitMulticastFiltered_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 21, 2, 1, 24),
    _LbBridgePortTransmitMulticastFiltered_Type()
)
lbBridgePortTransmitMulticastFiltered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbBridgePortTransmitMulticastFiltered.setStatus("mandatory")
_LbBridgePortReceiveMulticastLimitExceededCount_Type = Counter32
_LbBridgePortReceiveMulticastLimitExceededCount_Object = MibTableColumn
lbBridgePortReceiveMulticastLimitExceededCount = _LbBridgePortReceiveMulticastLimitExceededCount_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 21, 2, 1, 25),
    _LbBridgePortReceiveMulticastLimitExceededCount_Type()
)
lbBridgePortReceiveMulticastLimitExceededCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbBridgePortReceiveMulticastLimitExceededCount.setStatus("mandatory")
_LbBridgePortForwardedToTable_Object = MibTable
lbBridgePortForwardedToTable = _LbBridgePortForwardedToTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 21, 3)
)
if mibBuilder.loadTexts:
    lbBridgePortForwardedToTable.setStatus("mandatory")
_LbBridgePortForwardedToEntry_Object = MibTableRow
lbBridgePortForwardedToEntry = _LbBridgePortForwardedToEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 21, 3, 1)
)
lbBridgePortForwardedToEntry.setIndexNames(
    (0, "LB3GH-1-0-7", "lbBridgePortForwardedToBridgeIndex"),
    (0, "LB3GH-1-0-7", "lbBridgePortForwardedToReceivePortIndex"),
    (0, "LB3GH-1-0-7", "lbBridgePortForwardedToDstPortIndex"),
)
if mibBuilder.loadTexts:
    lbBridgePortForwardedToEntry.setStatus("mandatory")
_LbBridgePortForwardedToBridgeIndex_Type = Integer32
_LbBridgePortForwardedToBridgeIndex_Object = MibTableColumn
lbBridgePortForwardedToBridgeIndex = _LbBridgePortForwardedToBridgeIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 21, 3, 1, 1),
    _LbBridgePortForwardedToBridgeIndex_Type()
)
lbBridgePortForwardedToBridgeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbBridgePortForwardedToBridgeIndex.setStatus("mandatory")
_LbBridgePortForwardedToReceivePortIndex_Type = Integer32
_LbBridgePortForwardedToReceivePortIndex_Object = MibTableColumn
lbBridgePortForwardedToReceivePortIndex = _LbBridgePortForwardedToReceivePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 21, 3, 1, 2),
    _LbBridgePortForwardedToReceivePortIndex_Type()
)
lbBridgePortForwardedToReceivePortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbBridgePortForwardedToReceivePortIndex.setStatus("mandatory")
_LbBridgePortForwardedToDstPortIndex_Type = Integer32
_LbBridgePortForwardedToDstPortIndex_Object = MibTableColumn
lbBridgePortForwardedToDstPortIndex = _LbBridgePortForwardedToDstPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 21, 3, 1, 3),
    _LbBridgePortForwardedToDstPortIndex_Type()
)
lbBridgePortForwardedToDstPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbBridgePortForwardedToDstPortIndex.setStatus("mandatory")
_LbBridgePortForwardedToCount_Type = Counter32
_LbBridgePortForwardedToCount_Object = MibTableColumn
lbBridgePortForwardedToCount = _LbBridgePortForwardedToCount_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 21, 3, 1, 4),
    _LbBridgePortForwardedToCount_Type()
)
lbBridgePortForwardedToCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbBridgePortForwardedToCount.setStatus("mandatory")
_LbBridgePortFilteredToTable_Object = MibTable
lbBridgePortFilteredToTable = _LbBridgePortFilteredToTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 21, 4)
)
if mibBuilder.loadTexts:
    lbBridgePortFilteredToTable.setStatus("mandatory")
_LbBridgePortFilteredToEntry_Object = MibTableRow
lbBridgePortFilteredToEntry = _LbBridgePortFilteredToEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 21, 4, 1)
)
lbBridgePortFilteredToEntry.setIndexNames(
    (0, "LB3GH-1-0-7", "lbBridgePortFilteredToBridgeIndex"),
    (0, "LB3GH-1-0-7", "lbBridgePortFilteredToReceivePortIndex"),
    (0, "LB3GH-1-0-7", "lbBridgePortFilteredToDstPortIndex"),
)
if mibBuilder.loadTexts:
    lbBridgePortFilteredToEntry.setStatus("mandatory")
_LbBridgePortFilteredToBridgeIndex_Type = Integer32
_LbBridgePortFilteredToBridgeIndex_Object = MibTableColumn
lbBridgePortFilteredToBridgeIndex = _LbBridgePortFilteredToBridgeIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 21, 4, 1, 1),
    _LbBridgePortFilteredToBridgeIndex_Type()
)
lbBridgePortFilteredToBridgeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbBridgePortFilteredToBridgeIndex.setStatus("mandatory")
_LbBridgePortFilteredToReceivePortIndex_Type = Integer32
_LbBridgePortFilteredToReceivePortIndex_Object = MibTableColumn
lbBridgePortFilteredToReceivePortIndex = _LbBridgePortFilteredToReceivePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 21, 4, 1, 2),
    _LbBridgePortFilteredToReceivePortIndex_Type()
)
lbBridgePortFilteredToReceivePortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbBridgePortFilteredToReceivePortIndex.setStatus("mandatory")
_LbBridgePortFilteredToDstPortIndex_Type = Integer32
_LbBridgePortFilteredToDstPortIndex_Object = MibTableColumn
lbBridgePortFilteredToDstPortIndex = _LbBridgePortFilteredToDstPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 21, 4, 1, 3),
    _LbBridgePortFilteredToDstPortIndex_Type()
)
lbBridgePortFilteredToDstPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbBridgePortFilteredToDstPortIndex.setStatus("mandatory")
_LbBridgePortFilteredToCount_Type = Counter32
_LbBridgePortFilteredToCount_Object = MibTableColumn
lbBridgePortFilteredToCount = _LbBridgePortFilteredToCount_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 21, 4, 1, 4),
    _LbBridgePortFilteredToCount_Type()
)
lbBridgePortFilteredToCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbBridgePortFilteredToCount.setStatus("mandatory")
_LbBridgePortAddressTable_Object = MibTable
lbBridgePortAddressTable = _LbBridgePortAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 21, 5)
)
if mibBuilder.loadTexts:
    lbBridgePortAddressTable.setStatus("mandatory")
_LbBridgePortAddressEntry_Object = MibTableRow
lbBridgePortAddressEntry = _LbBridgePortAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 21, 5, 1)
)
lbBridgePortAddressEntry.setIndexNames(
    (0, "LB3GH-1-0-7", "lbBridgePortAddressBridgeIndex"),
    (0, "LB3GH-1-0-7", "lbBridgePortAddressPortIndex"),
    (0, "LB3GH-1-0-7", "lbBridgePortAddressIndex"),
)
if mibBuilder.loadTexts:
    lbBridgePortAddressEntry.setStatus("mandatory")
_LbBridgePortAddressBridgeIndex_Type = Integer32
_LbBridgePortAddressBridgeIndex_Object = MibTableColumn
lbBridgePortAddressBridgeIndex = _LbBridgePortAddressBridgeIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 21, 5, 1, 1),
    _LbBridgePortAddressBridgeIndex_Type()
)
lbBridgePortAddressBridgeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbBridgePortAddressBridgeIndex.setStatus("mandatory")
_LbBridgePortAddressPortIndex_Type = Integer32
_LbBridgePortAddressPortIndex_Object = MibTableColumn
lbBridgePortAddressPortIndex = _LbBridgePortAddressPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 21, 5, 1, 2),
    _LbBridgePortAddressPortIndex_Type()
)
lbBridgePortAddressPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbBridgePortAddressPortIndex.setStatus("mandatory")
_LbBridgePortAddressIndex_Type = Integer32
_LbBridgePortAddressIndex_Object = MibTableColumn
lbBridgePortAddressIndex = _LbBridgePortAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 21, 5, 1, 3),
    _LbBridgePortAddressIndex_Type()
)
lbBridgePortAddressIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbBridgePortAddressIndex.setStatus("mandatory")


class _LbBridgePortAddressRemoteAddress_Type(OctetString):
    """Custom type lbBridgePortAddressRemoteAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_LbBridgePortAddressRemoteAddress_Type.__name__ = "OctetString"
_LbBridgePortAddressRemoteAddress_Object = MibTableColumn
lbBridgePortAddressRemoteAddress = _LbBridgePortAddressRemoteAddress_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 21, 5, 1, 4),
    _LbBridgePortAddressRemoteAddress_Type()
)
lbBridgePortAddressRemoteAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lbBridgePortAddressRemoteAddress.setStatus("mandatory")


class _LbBridgePortAddressType_Type(Integer32):
    """Custom type lbBridgePortAddressType based on Integer32"""
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


_LbBridgePortAddressType_Type.__name__ = "Integer32"
_LbBridgePortAddressType_Object = MibTableColumn
lbBridgePortAddressType = _LbBridgePortAddressType_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 21, 5, 1, 5),
    _LbBridgePortAddressType_Type()
)
lbBridgePortAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lbBridgePortAddressType.setStatus("mandatory")


class _LbBridgePortAddressIsStatic_Type(Integer32):
    """Custom type lbBridgePortAddressIsStatic based on Integer32"""
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


_LbBridgePortAddressIsStatic_Type.__name__ = "Integer32"
_LbBridgePortAddressIsStatic_Object = MibTableColumn
lbBridgePortAddressIsStatic = _LbBridgePortAddressIsStatic_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 21, 5, 1, 6),
    _LbBridgePortAddressIsStatic_Type()
)
lbBridgePortAddressIsStatic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lbBridgePortAddressIsStatic.setStatus("mandatory")
_LbBridgePortAddressStaticPort_Type = Integer32
_LbBridgePortAddressStaticPort_Object = MibTableColumn
lbBridgePortAddressStaticPort = _LbBridgePortAddressStaticPort_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 21, 5, 1, 7),
    _LbBridgePortAddressStaticPort_Type()
)
lbBridgePortAddressStaticPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbBridgePortAddressStaticPort.setStatus("mandatory")
_LbBridgePortAddressAge_Type = Integer32
_LbBridgePortAddressAge_Object = MibTableColumn
lbBridgePortAddressAge = _LbBridgePortAddressAge_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 21, 5, 1, 8),
    _LbBridgePortAddressAge_Type()
)
lbBridgePortAddressAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbBridgePortAddressAge.setStatus("mandatory")
_LbTrapEnterprise_ObjectIdentity = ObjectIdentity
lbTrapEnterprise = _LbTrapEnterprise_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 22)
)
_LbTrapEnterpriseTable_Object = MibTable
lbTrapEnterpriseTable = _LbTrapEnterpriseTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 22, 1)
)
if mibBuilder.loadTexts:
    lbTrapEnterpriseTable.setStatus("mandatory")
_LbTrapEnterpriseTableEntry_Object = MibTableRow
lbTrapEnterpriseTableEntry = _LbTrapEnterpriseTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 22, 1, 1)
)
lbTrapEnterpriseTableEntry.setIndexNames(
    (0, "LB3GH-1-0-7", "lbTrapEnterpriseIndex"),
)
if mibBuilder.loadTexts:
    lbTrapEnterpriseTableEntry.setStatus("mandatory")
_LbTrapEnterpriseIndex_Type = Integer32
_LbTrapEnterpriseIndex_Object = MibTableColumn
lbTrapEnterpriseIndex = _LbTrapEnterpriseIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 22, 1, 1, 1),
    _LbTrapEnterpriseIndex_Type()
)
lbTrapEnterpriseIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbTrapEnterpriseIndex.setStatus("mandatory")
_LbTrapEnterpriseOID_Type = ObjectIdentifier
_LbTrapEnterpriseOID_Object = MibTableColumn
lbTrapEnterpriseOID = _LbTrapEnterpriseOID_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 22, 1, 1, 2),
    _LbTrapEnterpriseOID_Type()
)
lbTrapEnterpriseOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbTrapEnterpriseOID.setStatus("mandatory")
_LbTrapDest_ObjectIdentity = ObjectIdentity
lbTrapDest = _LbTrapDest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 23)
)
_LbTrapDestTable_Object = MibTable
lbTrapDestTable = _LbTrapDestTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 23, 1)
)
if mibBuilder.loadTexts:
    lbTrapDestTable.setStatus("mandatory")
_LbTrapDestTableEntry_Object = MibTableRow
lbTrapDestTableEntry = _LbTrapDestTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 23, 1, 1)
)
lbTrapDestTableEntry.setIndexNames(
    (0, "LB3GH-1-0-7", "lbTrapDestAddr"),
    (0, "LB3GH-1-0-7", "lbTrapDestEnterpriseIndex"),
    (0, "LB3GH-1-0-7", "lbTrapNumber"),
)
if mibBuilder.loadTexts:
    lbTrapDestTableEntry.setStatus("mandatory")
_LbTrapDestAddr_Type = IpAddress
_LbTrapDestAddr_Object = MibTableColumn
lbTrapDestAddr = _LbTrapDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 23, 1, 1, 1),
    _LbTrapDestAddr_Type()
)
lbTrapDestAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbTrapDestAddr.setStatus("mandatory")
_LbTrapDestEnterpriseIndex_Type = Integer32
_LbTrapDestEnterpriseIndex_Object = MibTableColumn
lbTrapDestEnterpriseIndex = _LbTrapDestEnterpriseIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 23, 1, 1, 2),
    _LbTrapDestEnterpriseIndex_Type()
)
lbTrapDestEnterpriseIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbTrapDestEnterpriseIndex.setStatus("mandatory")
_LbTrapNumber_Type = Integer32
_LbTrapNumber_Object = MibTableColumn
lbTrapNumber = _LbTrapNumber_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 23, 1, 1, 3),
    _LbTrapNumber_Type()
)
lbTrapNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbTrapNumber.setStatus("mandatory")


class _LbTrapEntryStatus_Type(Integer32):
    """Custom type lbTrapEntryStatus based on Integer32"""
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


_LbTrapEntryStatus_Type.__name__ = "Integer32"
_LbTrapEntryStatus_Object = MibTableColumn
lbTrapEntryStatus = _LbTrapEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 23, 1, 1, 4),
    _LbTrapEntryStatus_Type()
)
lbTrapEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lbTrapEntryStatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects

lbSlotInsertEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 0, 1)
)
lbSlotInsertEvent.setObjects(
      *(("LB3GH-1-0-7", "lbSlotIndex"),
        ("LB3GH-1-0-7", "lbSlotBoardType"),
        ("LB3GH-1-0-7", "lbSlotBoardRevision"))
)
if mibBuilder.loadTexts:
    lbSlotInsertEvent.setStatus(
        ""
    )

lbSlotExtractEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 0, 2)
)
lbSlotExtractEvent.setObjects(
    ("LB3GH-1-0-7", "lbSlotIndex")
)
if mibBuilder.loadTexts:
    lbSlotExtractEvent.setStatus(
        ""
    )

lbBridgeAddressThresholdEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 0, 3)
)
lbBridgeAddressThresholdEvent.setObjects(
      *(("LB3GH-1-0-7", "lbBridgeIndex"),
        ("LB3GH-1-0-7", "lbBridgeBaseSlotIndex"))
)
if mibBuilder.loadTexts:
    lbBridgeAddressThresholdEvent.setStatus(
        ""
    )

lbSystemOverTemperatureEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 0, 6)
)
if mibBuilder.loadTexts:
    lbSystemOverTemperatureEvent.setStatus(
        ""
    )

lbSlotOverTemperatureEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 0, 7)
)
lbSlotOverTemperatureEvent.setObjects(
      *(("LB3GH-1-0-7", "lbSlotIndex"),
        ("LB3GH-1-0-7", "lbSlotBoardType"),
        ("LB3GH-1-0-7", "lbSlotBoardRevision"),
        ("LB3GH-1-0-7", "lbSlotBoardStatus"))
)
if mibBuilder.loadTexts:
    lbSlotOverTemperatureEvent.setStatus(
        ""
    )

lbPowerSupplyFailureEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 7, 1, 0, 8)
)
lbPowerSupplyFailureEvent.setObjects(
      *(("LB3GH-1-0-7", "lbPowerSupplyIndex"),
        ("LB3GH-1-0-7", "lbPowerSupplyLocation"),
        ("LB3GH-1-0-7", "lbPowerSupplyLastFailure"),
        ("LB3GH-1-0-7", "lbSystemPowerSupplyCount"))
)
if mibBuilder.loadTexts:
    lbPowerSupplyFailureEvent.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LB3GH-1-0-7",
    **{"a3Com": a3Com,
       "lb3gh": lb3gh,
       "lb3ghMib": lb3ghMib,
       "lbSlotInsertEvent": lbSlotInsertEvent,
       "lbSlotExtractEvent": lbSlotExtractEvent,
       "lbBridgeAddressThresholdEvent": lbBridgeAddressThresholdEvent,
       "lbSystemOverTemperatureEvent": lbSystemOverTemperatureEvent,
       "lbSlotOverTemperatureEvent": lbSlotOverTemperatureEvent,
       "lbPowerSupplyFailureEvent": lbPowerSupplyFailureEvent,
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
       "smm": smm,
       "smmTable": smmTable,
       "smmEntry": smmEntry,
       "smmSlotIndex": smmSlotIndex,
       "smmEthernetPortCount": smmEthernetPortCount,
       "smmBaseEthernetPortIndex": smmBaseEthernetPortIndex,
       "fbcm": fbcm,
       "fbcmTable": fbcmTable,
       "fbcmEntry": fbcmEntry,
       "fbcmSlotIndex": fbcmSlotIndex,
       "fbcmMACCount": fbcmMACCount,
       "fbcmBaseMACIndex": fbcmBaseMACIndex,
       "fbcmPortCount": fbcmPortCount,
       "fbcmBasePortIndex": fbcmBasePortIndex,
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
       "elm": elm,
       "elmTable": elmTable,
       "elmEntry": elmEntry,
       "elmSlotIndex": elmSlotIndex,
       "elmFddiMACCount": elmFddiMACCount,
       "elmBaseFddiMACIndex": elmBaseFddiMACIndex,
       "elmEthernetPortCount": elmEthernetPortCount,
       "elmBaseEthernetPortIndex": elmBaseEthernetPortIndex,
       "elmAddressThreshold": elmAddressThreshold,
       "elmFddiMAC": elmFddiMAC,
       "elmFddiMACTable": elmFddiMACTable,
       "elmFddiMACEntry": elmFddiMACEntry,
       "elmFddiSlotIndex": elmFddiSlotIndex,
       "elmFddiMACIndex": elmFddiMACIndex,
       "elmFddiMACForwardedCts": elmFddiMACForwardedCts,
       "elmFddiMACDroppedCts": elmFddiMACDroppedCts,
       "elmEthernetPort": elmEthernetPort,
       "elmEthernetPortTable": elmEthernetPortTable,
       "elmEthernetPortEntry": elmEthernetPortEntry,
       "elmEthernetPortSlotIndex": elmEthernetPortSlotIndex,
       "elmEthernetPortIndex": elmEthernetPortIndex,
       "elmEthernetPortLabel": elmEthernetPortLabel,
       "elmEthernetPortForwardedCts": elmEthernetPortForwardedCts,
       "elmEthernetPortDroppedCts": elmEthernetPortDroppedCts,
       "elmEthernetPortUTurnCts": elmEthernetPortUTurnCts,
       "elmEthernetPortState": elmEthernetPortState,
       "elmEthernetPortAction": elmEthernetPortAction,
       "elmMACAddress": elmMACAddress,
       "elmEthernetMACAddressTable": elmEthernetMACAddressTable,
       "elmEthernetMACAddressEntry": elmEthernetMACAddressEntry,
       "elmEthernetMACAddressSlotIndex": elmEthernetMACAddressSlotIndex,
       "elmEthernetMACAddressPortIndex": elmEthernetMACAddressPortIndex,
       "elmEthernetMACAddressIndex": elmEthernetMACAddressIndex,
       "elmEthernetMACAddressType": elmEthernetMACAddressType,
       "elmEthernetMACAddressRemoteAddress": elmEthernetMACAddressRemoteAddress,
       "elmEthernetMACAddressIsStatic": elmEthernetMACAddressIsStatic,
       "elmEthernetMACAddressStaticPort": elmEthernetMACAddressStaticPort,
       "elmEthernetMACAddressAge": elmEthernetMACAddressAge,
       "lbSystem": lbSystem,
       "lbSystemId": lbSystemId,
       "lbSystemType": lbSystemType,
       "lbSystemName": lbSystemName,
       "lbSystemManufacturer": lbSystemManufacturer,
       "lbSystemBackplaneRevision": lbSystemBackplaneRevision,
       "lbSystemSlotCount": lbSystemSlotCount,
       "lbSystemMemorySize": lbSystemMemorySize,
       "lbSystemFlashMemorySize": lbSystemFlashMemorySize,
       "lbSystemNvMemorySize": lbSystemNvMemorySize,
       "lbSystemSoftwareRevision": lbSystemSoftwareRevision,
       "lbSystemBuildTime": lbSystemBuildTime,
       "lbSystemControlPanelHardwareRevision": lbSystemControlPanelHardwareRevision,
       "lbSystemControlPanelSoftwareRevision": lbSystemControlPanelSoftwareRevision,
       "lbSystemControlPanelLines": lbSystemControlPanelLines,
       "lbSystemControlPanelColumns": lbSystemControlPanelColumns,
       "lbSystemControlPanelText": lbSystemControlPanelText,
       "lbSystemFddiMacCount": lbSystemFddiMacCount,
       "lbSystemFddiPortCount": lbSystemFddiPortCount,
       "lbSystemEthernetPortCount": lbSystemEthernetPortCount,
       "lbSystemExpressFunctionCount": lbSystemExpressFunctionCount,
       "lbSystemExpressFddiPortCount": lbSystemExpressFddiPortCount,
       "lbSystemExpressEthernetPortCount": lbSystemExpressEthernetPortCount,
       "lbSystemPowerSupplyCount": lbSystemPowerSupplyCount,
       "lbSystemAction": lbSystemAction,
       "lbSystemBridgeFunctionCount": lbSystemBridgeFunctionCount,
       "lbSystemSmtProxyTimeoutBase": lbSystemSmtProxyTimeoutBase,
       "lbSystemSmtProxyEvents": lbSystemSmtProxyEvents,
       "lbSlot": lbSlot,
       "lbSlotTable": lbSlotTable,
       "lbSlotEntry": lbSlotEntry,
       "lbSlotIndex": lbSlotIndex,
       "lbSlotBoardType": lbSlotBoardType,
       "lbSlotBoardRevision": lbSlotBoardRevision,
       "lbSlotBoardStatus": lbSlotBoardStatus,
       "lbSlotBoardName": lbSlotBoardName,
       "lbSlotBoardNameAbbrev": lbSlotBoardNameAbbrev,
       "lbSlotFddiMacCount": lbSlotFddiMacCount,
       "lbSlotFddiMacBaseIndex": lbSlotFddiMacBaseIndex,
       "lbSlotFddiPortCount": lbSlotFddiPortCount,
       "lbSlotFddiPortBaseIndex": lbSlotFddiPortBaseIndex,
       "lbSlotEthernetPortCount": lbSlotEthernetPortCount,
       "lbSlotEthernetPortBaseIndex": lbSlotEthernetPortBaseIndex,
       "lbSlotExpressFunctionCount": lbSlotExpressFunctionCount,
       "lbSlotExpressFunctionBaseIndex": lbSlotExpressFunctionBaseIndex,
       "lbSlotExpressFddiPortCount": lbSlotExpressFddiPortCount,
       "lbSlotExpressFddiPortBaseIndex": lbSlotExpressFddiPortBaseIndex,
       "lbSlotExpressEthernetPortCount": lbSlotExpressEthernetPortCount,
       "lbSlotExpressEthernetPortBaseIndex": lbSlotExpressEthernetPortBaseIndex,
       "lbSlotBoardAction": lbSlotBoardAction,
       "lbSlotBridgeFunctionCount": lbSlotBridgeFunctionCount,
       "lbSlotBridgeFunctionBaseIndex": lbSlotBridgeFunctionBaseIndex,
       "lbFddiMac": lbFddiMac,
       "lbFddiMacTable": lbFddiMacTable,
       "lbFddiMacEntry": lbFddiMacEntry,
       "lbFddiMacIndex": lbFddiMacIndex,
       "lbFddiMacSlotIndex": lbFddiMacSlotIndex,
       "lbFddiMacLocalIndex": lbFddiMacLocalIndex,
       "lbFddiMacByteReceiveRate": lbFddiMacByteReceiveRate,
       "lbFddiMacPeakByteReceiveRate": lbFddiMacPeakByteReceiveRate,
       "lbFddiMacFrameReceiveRate": lbFddiMacFrameReceiveRate,
       "lbFddiMacPeakFrameReceiveRate": lbFddiMacPeakFrameReceiveRate,
       "lbFddiMacByteTransmitRate": lbFddiMacByteTransmitRate,
       "lbFddiMacPeakByteTransmitRate": lbFddiMacPeakByteTransmitRate,
       "lbFddiMacFrameTransmitRate": lbFddiMacFrameTransmitRate,
       "lbFddiMacPeakFrameTransmitRate": lbFddiMacPeakFrameTransmitRate,
       "lbFddiMacReceiveMulticastThreshold": lbFddiMacReceiveMulticastThreshold,
       "lbFddiMacBeaconHistory": lbFddiMacBeaconHistory,
       "lbEthernetPort": lbEthernetPort,
       "lbEthernetPortTable": lbEthernetPortTable,
       "lbEthernetPortEntry": lbEthernetPortEntry,
       "lbEthernetPortIndex": lbEthernetPortIndex,
       "lbEthernetPortSlotIndex": lbEthernetPortSlotIndex,
       "lbEthernetPortLocalIndex": lbEthernetPortLocalIndex,
       "lbEthernetPortLabel": lbEthernetPortLabel,
       "lbEthernetPortChipsetType": lbEthernetPortChipsetType,
       "lbEthernetPortLinkStatus": lbEthernetPortLinkStatus,
       "lbEthernetPortByteReceiveRate": lbEthernetPortByteReceiveRate,
       "lbEthernetPortPeakByteReceiveRate": lbEthernetPortPeakByteReceiveRate,
       "lbEthernetPortFrameReceiveRate": lbEthernetPortFrameReceiveRate,
       "lbEthernetPortPeakFrameReceiveRate": lbEthernetPortPeakFrameReceiveRate,
       "lbEthernetPortByteTransmitRate": lbEthernetPortByteTransmitRate,
       "lbEthernetPortPeakByteTransmitRate": lbEthernetPortPeakByteTransmitRate,
       "lbEthernetPortFrameTransmitRate": lbEthernetPortFrameTransmitRate,
       "lbEthernetPortPeakFrameTransmitRate": lbEthernetPortPeakFrameTransmitRate,
       "lbEthernetPortReceiveMulticastThreshold": lbEthernetPortReceiveMulticastThreshold,
       "lbEthernetPortType": lbEthernetPortType,
       "lbFddiPort": lbFddiPort,
       "lbFddiPortTable": lbFddiPortTable,
       "lbFddiPortEntry": lbFddiPortEntry,
       "lbFddiPortIndex": lbFddiPortIndex,
       "lbFddiPortSlotIndex": lbFddiPortSlotIndex,
       "lbFddiPortLocalIndex": lbFddiPortLocalIndex,
       "lbFddiPortLabel": lbFddiPortLabel,
       "lbExpress": lbExpress,
       "lbExpressTable": lbExpressTable,
       "lbExpressEntry": lbExpressEntry,
       "lbExpressIndex": lbExpressIndex,
       "lbExpressSlotIndex": lbExpressSlotIndex,
       "lbExpressLocalIndex": lbExpressLocalIndex,
       "lbExpressAddressThreshold": lbExpressAddressThreshold,
       "lbExpressFddiPort": lbExpressFddiPort,
       "lbExpressFddiPortTable": lbExpressFddiPortTable,
       "lbExpressFddiPortEntry": lbExpressFddiPortEntry,
       "lbExpressFddiPortIndex": lbExpressFddiPortIndex,
       "lbExpressFddiPortSlotIndex": lbExpressFddiPortSlotIndex,
       "lbExpressFddiPortLocalIndex": lbExpressFddiPortLocalIndex,
       "lbExpressFddiPortForwardedCts": lbExpressFddiPortForwardedCts,
       "lbExpressFddiPortDroppedCts": lbExpressFddiPortDroppedCts,
       "lbExpressEthernetPort": lbExpressEthernetPort,
       "lbExpressEthernetPortTable": lbExpressEthernetPortTable,
       "lbExpressEthernetPortEntry": lbExpressEthernetPortEntry,
       "lbExpressEthernetPortIndex": lbExpressEthernetPortIndex,
       "lbExpressEthernetPortSlotIndex": lbExpressEthernetPortSlotIndex,
       "lbExpressEthernetPortLocalIndex": lbExpressEthernetPortLocalIndex,
       "lbExpressEthernetPortForwardedCts": lbExpressEthernetPortForwardedCts,
       "lbExpressEthernetPortDroppedCts": lbExpressEthernetPortDroppedCts,
       "lbExpressEthernetPortUTurnCts": lbExpressEthernetPortUTurnCts,
       "lbExpressEthernetPortAction": lbExpressEthernetPortAction,
       "lbExpressEthernetPortAddress": lbExpressEthernetPortAddress,
       "lbExpressEthernetPortAddressTable": lbExpressEthernetPortAddressTable,
       "lbExpressEthernetPortAddressEntry": lbExpressEthernetPortAddressEntry,
       "lbExpressEthernetPortAddressPortIndex": lbExpressEthernetPortAddressPortIndex,
       "lbExpressEthernetPortAddressIndex": lbExpressEthernetPortAddressIndex,
       "lbExpressEthernetPortAddressSlotIndex": lbExpressEthernetPortAddressSlotIndex,
       "lbExpressEthernetPortAddressType": lbExpressEthernetPortAddressType,
       "lbExpressEthernetPortAddressRemoteAddress": lbExpressEthernetPortAddressRemoteAddress,
       "lbExpressEthernetPortAddressIsStatic": lbExpressEthernetPortAddressIsStatic,
       "lbExpressEthernetPortAddressStaticPort": lbExpressEthernetPortAddressStaticPort,
       "lbExpressEthernetPortAddressAge": lbExpressEthernetPortAddressAge,
       "lbPowerSupply": lbPowerSupply,
       "lbPowerSupplyTable": lbPowerSupplyTable,
       "lbPowerSupplyEntry": lbPowerSupplyEntry,
       "lbPowerSupplyIndex": lbPowerSupplyIndex,
       "lbPowerSupplyLocation": lbPowerSupplyLocation,
       "lbPowerSupplyStatus": lbPowerSupplyStatus,
       "lbPowerSupplyFailureType": lbPowerSupplyFailureType,
       "lbPowerSupplyLastFailure": lbPowerSupplyLastFailure,
       "lbBridge": lbBridge,
       "lbBridgeTable": lbBridgeTable,
       "lbBridgeEntry": lbBridgeEntry,
       "lbBridgeIndex": lbBridgeIndex,
       "lbBridgeBaseSlotIndex": lbBridgeBaseSlotIndex,
       "lbBridgePortCount": lbBridgePortCount,
       "lbBridgeAddressTableSize": lbBridgeAddressTableSize,
       "lbBridgeAddressThreshold": lbBridgeAddressThreshold,
       "lbBridgeMode": lbBridgeMode,
       "lbBridgeLocalIndex": lbBridgeLocalIndex,
       "lbBridgePortTable": lbBridgePortTable,
       "lbBridgePortEntry": lbBridgePortEntry,
       "lbBridgePortBridgeIndex": lbBridgePortBridgeIndex,
       "lbBridgePortIndex": lbBridgePortIndex,
       "lbBridgePortSlotIndex": lbBridgePortSlotIndex,
       "lbBridgePortLocalIndex": lbBridgePortLocalIndex,
       "lbBridgePortType": lbBridgePortType,
       "lbBridgePortIpFragmentationEnabled": lbBridgePortIpFragmentationEnabled,
       "lbBridgePortReceiveMulticastLimit": lbBridgePortReceiveMulticastLimit,
       "lbBridgePortAddressAction": lbBridgePortAddressAction,
       "lbBridgePortTotalForwardedCts": lbBridgePortTotalForwardedCts,
       "lbBridgePortManagementFramesReceived": lbBridgePortManagementFramesReceived,
       "lbBridgePortTotalDiscards": lbBridgePortTotalDiscards,
       "lbBridgePortReceiveBlockedDiscards": lbBridgePortReceiveBlockedDiscards,
       "lbBridgePortReceiveMulticastLimitExceededs": lbBridgePortReceiveMulticastLimitExceededs,
       "lbBridgePortReceiveSecurityDiscards": lbBridgePortReceiveSecurityDiscards,
       "lbBridgePortReceiveUnknownDiscards": lbBridgePortReceiveUnknownDiscards,
       "lbBridgePortReceiveOtherDiscards": lbBridgePortReceiveOtherDiscards,
       "lbBridgePortReceiveErrorDiscards": lbBridgePortReceiveErrorDiscards,
       "lbBridgePortSameSegmentDiscards": lbBridgePortSameSegmentDiscards,
       "lbBridgePortTransmitBlockedDiscards": lbBridgePortTransmitBlockedDiscards,
       "lbBridgePortTotalFiltered": lbBridgePortTotalFiltered,
       "lbBridgePortReceiveUnicastFiltered": lbBridgePortReceiveUnicastFiltered,
       "lbBridgePortReceiveMulticastFiltered": lbBridgePortReceiveMulticastFiltered,
       "lbBridgePortTransmitUnicastFiltered": lbBridgePortTransmitUnicastFiltered,
       "lbBridgePortTransmitMulticastFiltered": lbBridgePortTransmitMulticastFiltered,
       "lbBridgePortReceiveMulticastLimitExceededCount": lbBridgePortReceiveMulticastLimitExceededCount,
       "lbBridgePortForwardedToTable": lbBridgePortForwardedToTable,
       "lbBridgePortForwardedToEntry": lbBridgePortForwardedToEntry,
       "lbBridgePortForwardedToBridgeIndex": lbBridgePortForwardedToBridgeIndex,
       "lbBridgePortForwardedToReceivePortIndex": lbBridgePortForwardedToReceivePortIndex,
       "lbBridgePortForwardedToDstPortIndex": lbBridgePortForwardedToDstPortIndex,
       "lbBridgePortForwardedToCount": lbBridgePortForwardedToCount,
       "lbBridgePortFilteredToTable": lbBridgePortFilteredToTable,
       "lbBridgePortFilteredToEntry": lbBridgePortFilteredToEntry,
       "lbBridgePortFilteredToBridgeIndex": lbBridgePortFilteredToBridgeIndex,
       "lbBridgePortFilteredToReceivePortIndex": lbBridgePortFilteredToReceivePortIndex,
       "lbBridgePortFilteredToDstPortIndex": lbBridgePortFilteredToDstPortIndex,
       "lbBridgePortFilteredToCount": lbBridgePortFilteredToCount,
       "lbBridgePortAddressTable": lbBridgePortAddressTable,
       "lbBridgePortAddressEntry": lbBridgePortAddressEntry,
       "lbBridgePortAddressBridgeIndex": lbBridgePortAddressBridgeIndex,
       "lbBridgePortAddressPortIndex": lbBridgePortAddressPortIndex,
       "lbBridgePortAddressIndex": lbBridgePortAddressIndex,
       "lbBridgePortAddressRemoteAddress": lbBridgePortAddressRemoteAddress,
       "lbBridgePortAddressType": lbBridgePortAddressType,
       "lbBridgePortAddressIsStatic": lbBridgePortAddressIsStatic,
       "lbBridgePortAddressStaticPort": lbBridgePortAddressStaticPort,
       "lbBridgePortAddressAge": lbBridgePortAddressAge,
       "lbTrapEnterprise": lbTrapEnterprise,
       "lbTrapEnterpriseTable": lbTrapEnterpriseTable,
       "lbTrapEnterpriseTableEntry": lbTrapEnterpriseTableEntry,
       "lbTrapEnterpriseIndex": lbTrapEnterpriseIndex,
       "lbTrapEnterpriseOID": lbTrapEnterpriseOID,
       "lbTrapDest": lbTrapDest,
       "lbTrapDestTable": lbTrapDestTable,
       "lbTrapDestTableEntry": lbTrapDestTableEntry,
       "lbTrapDestAddr": lbTrapDestAddr,
       "lbTrapDestEnterpriseIndex": lbTrapDestEnterpriseIndex,
       "lbTrapNumber": lbTrapNumber,
       "lbTrapEntryStatus": lbTrapEntryStatus}
)
