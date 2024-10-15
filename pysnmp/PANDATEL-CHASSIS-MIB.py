# SNMP MIB module (PANDATEL-CHASSIS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PANDATEL-CHASSIS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:36:42 2024
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

_Pandatel_ObjectIdentity = ObjectIdentity
pandatel = _Pandatel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 760)
)
_Mibs_ObjectIdentity = ObjectIdentity
mibs = _Mibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 760, 1)
)
_Chassis_ObjectIdentity = ObjectIdentity
chassis = _Chassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 760, 1, 20000)
)
_ChassisTypeID_Type = ObjectIdentifier
_ChassisTypeID_Object = MibScalar
chassisTypeID = _ChassisTypeID_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 20000, 1),
    _ChassisTypeID_Type()
)
chassisTypeID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisTypeID.setStatus("mandatory")


class _ChassisComponents_Type(Integer32):
    """Custom type chassisComponents based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("stand-alone", 0)
    )


_ChassisComponents_Type.__name__ = "Integer32"
_ChassisComponents_Object = MibScalar
chassisComponents = _ChassisComponents_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 20000, 2),
    _ChassisComponents_Type()
)
chassisComponents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisComponents.setStatus("mandatory")
_ChassisDevices_Type = Integer32
_ChassisDevices_Object = MibScalar
chassisDevices = _ChassisDevices_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 20000, 3),
    _ChassisDevices_Type()
)
chassisDevices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisDevices.setStatus("mandatory")


class _ChassisSlots_Type(Integer32):
    """Custom type chassisSlots based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("no-slots", 0)
    )


_ChassisSlots_Type.__name__ = "Integer32"
_ChassisSlots_Object = MibScalar
chassisSlots = _ChassisSlots_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 20000, 4),
    _ChassisSlots_Type()
)
chassisSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisSlots.setStatus("mandatory")
_ChassisModules_Type = Integer32
_ChassisModules_Object = MibScalar
chassisModules = _ChassisModules_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 20000, 5),
    _ChassisModules_Type()
)
chassisModules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisModules.setStatus("mandatory")


class _ChassisPorts_Type(Integer32):
    """Custom type chassisPorts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("no-ports", 0)
    )


_ChassisPorts_Type.__name__ = "Integer32"
_ChassisPorts_Object = MibScalar
chassisPorts = _ChassisPorts_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 20000, 6),
    _ChassisPorts_Type()
)
chassisPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisPorts.setStatus("mandatory")
_ChassisComponentTable_Object = MibTable
chassisComponentTable = _ChassisComponentTable_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 20000, 10)
)
if mibBuilder.loadTexts:
    chassisComponentTable.setStatus("optional")
_CompEntry_Object = MibTableRow
compEntry = _CompEntry_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 20000, 10, 1)
)
compEntry.setIndexNames(
    (0, "PANDATEL-CHASSIS-MIB", "compComp"),
)
if mibBuilder.loadTexts:
    compEntry.setStatus("mandatory")


class _CompComp_Type(Integer32):
    """Custom type compComp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("main", 0)
    )


_CompComp_Type.__name__ = "Integer32"
_CompComp_Object = MibTableColumn
compComp = _CompComp_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 20000, 10, 1, 1),
    _CompComp_Type()
)
compComp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    compComp.setStatus("mandatory")


class _CompDesign_Type(Integer32):
    """Custom type compDesign based on Integer32"""
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
        *(("device", 3),
          ("other", 1),
          ("rack", 2),
          ("stack", 4))
    )


_CompDesign_Type.__name__ = "Integer32"
_CompDesign_Object = MibTableColumn
compDesign = _CompDesign_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 20000, 10, 1, 2),
    _CompDesign_Type()
)
compDesign.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    compDesign.setStatus("mandatory")
_CompTypeID_Type = ObjectIdentifier
_CompTypeID_Object = MibTableColumn
compTypeID = _CompTypeID_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 20000, 10, 1, 3),
    _CompTypeID_Type()
)
compTypeID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    compTypeID.setStatus("mandatory")
_CompSlots_Type = Integer32
_CompSlots_Object = MibTableColumn
compSlots = _CompSlots_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 20000, 10, 1, 4),
    _CompSlots_Type()
)
compSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    compSlots.setStatus("mandatory")
_CompModules_Type = Integer32
_CompModules_Object = MibTableColumn
compModules = _CompModules_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 20000, 10, 1, 5),
    _CompModules_Type()
)
compModules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    compModules.setStatus("mandatory")
_ChassisDeviceTable_Object = MibTable
chassisDeviceTable = _ChassisDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 20000, 11)
)
if mibBuilder.loadTexts:
    chassisDeviceTable.setStatus("mandatory")
_DevcEntry_Object = MibTableRow
devcEntry = _DevcEntry_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 20000, 11, 1)
)
devcEntry.setIndexNames(
    (0, "PANDATEL-CHASSIS-MIB", "devcComp"),
    (0, "PANDATEL-CHASSIS-MIB", "devcSlot"),
)
if mibBuilder.loadTexts:
    devcEntry.setStatus("mandatory")


class _DevcComp_Type(Integer32):
    """Custom type devcComp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("main", 0)
    )


_DevcComp_Type.__name__ = "Integer32"
_DevcComp_Object = MibTableColumn
devcComp = _DevcComp_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 20000, 11, 1, 1),
    _DevcComp_Type()
)
devcComp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devcComp.setStatus("mandatory")


class _DevcSlot_Type(Integer32):
    """Custom type devcSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("main", 0)
    )


_DevcSlot_Type.__name__ = "Integer32"
_DevcSlot_Object = MibTableColumn
devcSlot = _DevcSlot_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 20000, 11, 1, 2),
    _DevcSlot_Type()
)
devcSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devcSlot.setStatus("mandatory")
_DevcTypeID_Type = ObjectIdentifier
_DevcTypeID_Object = MibTableColumn
devcTypeID = _DevcTypeID_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 20000, 11, 1, 3),
    _DevcTypeID_Type()
)
devcTypeID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devcTypeID.setStatus("mandatory")
_DevcMgmtAddress_Type = IpAddress
_DevcMgmtAddress_Object = MibTableColumn
devcMgmtAddress = _DevcMgmtAddress_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 20000, 11, 1, 4),
    _DevcMgmtAddress_Type()
)
devcMgmtAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devcMgmtAddress.setStatus("mandatory")
_DevcDescr_Type = DisplayString
_DevcDescr_Object = MibTableColumn
devcDescr = _DevcDescr_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 20000, 11, 1, 5),
    _DevcDescr_Type()
)
devcDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devcDescr.setStatus("mandatory")
_DevcModules_Type = Integer32
_DevcModules_Object = MibTableColumn
devcModules = _DevcModules_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 20000, 11, 1, 6),
    _DevcModules_Type()
)
devcModules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devcModules.setStatus("mandatory")
_DevcPorts_Type = Integer32
_DevcPorts_Object = MibTableColumn
devcPorts = _DevcPorts_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 20000, 11, 1, 7),
    _DevcPorts_Type()
)
devcPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devcPorts.setStatus("mandatory")
_DevcLastChange_Type = TimeTicks
_DevcLastChange_Object = MibTableColumn
devcLastChange = _DevcLastChange_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 20000, 11, 1, 8),
    _DevcLastChange_Type()
)
devcLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devcLastChange.setStatus("mandatory")
_ChassisSlotTable_Object = MibTable
chassisSlotTable = _ChassisSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 20000, 12)
)
if mibBuilder.loadTexts:
    chassisSlotTable.setStatus("optional")
_SlotEntry_Object = MibTableRow
slotEntry = _SlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 20000, 12, 1)
)
slotEntry.setIndexNames(
    (0, "PANDATEL-CHASSIS-MIB", "slotComp"),
    (0, "PANDATEL-CHASSIS-MIB", "slotSlot"),
)
if mibBuilder.loadTexts:
    slotEntry.setStatus("mandatory")


class _SlotComp_Type(Integer32):
    """Custom type slotComp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("main", 0)
    )


_SlotComp_Type.__name__ = "Integer32"
_SlotComp_Object = MibTableColumn
slotComp = _SlotComp_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 20000, 12, 1, 1),
    _SlotComp_Type()
)
slotComp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotComp.setStatus("mandatory")


class _SlotSlot_Type(Integer32):
    """Custom type slotSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("main", 0)
    )


_SlotSlot_Type.__name__ = "Integer32"
_SlotSlot_Object = MibTableColumn
slotSlot = _SlotSlot_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 20000, 12, 1, 2),
    _SlotSlot_Type()
)
slotSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotSlot.setStatus("mandatory")
_SlotOwnerDeviceID_Type = ObjectIdentifier
_SlotOwnerDeviceID_Object = MibTableColumn
slotOwnerDeviceID = _SlotOwnerDeviceID_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 20000, 12, 1, 3),
    _SlotOwnerDeviceID_Type()
)
slotOwnerDeviceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotOwnerDeviceID.setStatus("mandatory")
_SlotSlotTypeID_Type = ObjectIdentifier
_SlotSlotTypeID_Object = MibTableColumn
slotSlotTypeID = _SlotSlotTypeID_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 20000, 12, 1, 4),
    _SlotSlotTypeID_Type()
)
slotSlotTypeID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotSlotTypeID.setStatus("mandatory")
_SlotModuleTypeID_Type = ObjectIdentifier
_SlotModuleTypeID_Object = MibTableColumn
slotModuleTypeID = _SlotModuleTypeID_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 20000, 12, 1, 5),
    _SlotModuleTypeID_Type()
)
slotModuleTypeID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotModuleTypeID.setStatus("mandatory")
_SlotModuleName_Type = DisplayString
_SlotModuleName_Object = MibTableColumn
slotModuleName = _SlotModuleName_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 20000, 12, 1, 6),
    _SlotModuleName_Type()
)
slotModuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotModuleName.setStatus("mandatory")
_SlotPorts_Type = Integer32
_SlotPorts_Object = MibTableColumn
slotPorts = _SlotPorts_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 20000, 12, 1, 7),
    _SlotPorts_Type()
)
slotPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotPorts.setStatus("mandatory")
_ChassisPortTable_Object = MibTable
chassisPortTable = _ChassisPortTable_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 20000, 13)
)
if mibBuilder.loadTexts:
    chassisPortTable.setStatus("optional")
_PortEntry_Object = MibTableRow
portEntry = _PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 20000, 13, 1)
)
portEntry.setIndexNames(
    (0, "PANDATEL-CHASSIS-MIB", "portComp"),
    (0, "PANDATEL-CHASSIS-MIB", "portSlot"),
    (0, "PANDATEL-CHASSIS-MIB", "portPort"),
)
if mibBuilder.loadTexts:
    portEntry.setStatus("mandatory")
_PortComp_Type = Integer32
_PortComp_Object = MibTableColumn
portComp = _PortComp_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 20000, 13, 1, 1),
    _PortComp_Type()
)
portComp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portComp.setStatus("mandatory")


class _PortSlot_Type(Integer32):
    """Custom type portSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("main", 0)
    )


_PortSlot_Type.__name__ = "Integer32"
_PortSlot_Object = MibTableColumn
portSlot = _PortSlot_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 20000, 13, 1, 2),
    _PortSlot_Type()
)
portSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portSlot.setStatus("mandatory")
_PortPort_Type = Integer32
_PortPort_Object = MibTableColumn
portPort = _PortPort_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 20000, 13, 1, 3),
    _PortPort_Type()
)
portPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portPort.setStatus("mandatory")
_PortOwnerDeviceID_Type = ObjectIdentifier
_PortOwnerDeviceID_Object = MibTableColumn
portOwnerDeviceID = _PortOwnerDeviceID_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 20000, 13, 1, 4),
    _PortOwnerDeviceID_Type()
)
portOwnerDeviceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portOwnerDeviceID.setStatus("mandatory")
_PortFunctionalTypeID_Type = ObjectIdentifier
_PortFunctionalTypeID_Object = MibTableColumn
portFunctionalTypeID = _PortFunctionalTypeID_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 20000, 13, 1, 5),
    _PortFunctionalTypeID_Type()
)
portFunctionalTypeID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portFunctionalTypeID.setStatus("mandatory")


class _PortPhysicalType_Type(Integer32):
    """Custom type portPhysicalType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
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
              997,
              998,
              999)
        )
    )
    namedValues = NamedValues(
        *(("bnc", 4),
          ("db-15-f", 12),
          ("db-15-m", 13),
          ("db-25-f", 14),
          ("db-25-m", 15),
          ("db-37-f", 16),
          ("db-37-m", 17),
          ("db-9-f", 10),
          ("db-9-m", 11),
          ("dpc", 5),
          ("dual-fc", 28),
          ("dual-fc-apc", 33),
          ("dual-fiber", 3),
          ("dual-lc", 36),
          ("dual-lc-apc", 37),
          ("dual-sc", 27),
          ("dual-sc-45", 40),
          ("dual-sc-apc", 32),
          ("dual-st", 29),
          ("e2000", 23),
          ("escon", 22),
          ("ics", 8),
          ("mic", 9),
          ("mini-c", 20),
          ("minimicro", 21),
          ("mt-rj", 38),
          ("not-installed", 999),
          ("other", 1),
          ("rj45", 7),
          ("single-fc", 25),
          ("single-fc-apc", 31),
          ("single-fiber", 2),
          ("single-lc", 34),
          ("single-lc-apc", 35),
          ("single-sc", 24),
          ("single-sc-45", 39),
          ("single-sc-apc", 30),
          ("single-st", 26),
          ("unknown", 997),
          ("virtual", 998),
          ("winch-f", 18),
          ("winch-m", 19))
    )


_PortPhysicalType_Type.__name__ = "Integer32"
_PortPhysicalType_Object = MibTableColumn
portPhysicalType = _PortPhysicalType_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 20000, 13, 1, 6),
    _PortPhysicalType_Type()
)
portPhysicalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portPhysicalType.setStatus("mandatory")
_ChassisPowerSupplyTable_Object = MibTable
chassisPowerSupplyTable = _ChassisPowerSupplyTable_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 20000, 14)
)
if mibBuilder.loadTexts:
    chassisPowerSupplyTable.setStatus("optional")
_PsupplyEntry_Object = MibTableRow
psupplyEntry = _PsupplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 20000, 14, 1)
)
psupplyEntry.setIndexNames(
    (0, "PANDATEL-CHASSIS-MIB", "psupplyRack"),
    (0, "PANDATEL-CHASSIS-MIB", "psupplySlot"),
    (0, "PANDATEL-CHASSIS-MIB", "psupplyIndex"),
)
if mibBuilder.loadTexts:
    psupplyEntry.setStatus("mandatory")
_PsupplyRack_Type = Integer32
_PsupplyRack_Object = MibTableColumn
psupplyRack = _PsupplyRack_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 20000, 14, 1, 1),
    _PsupplyRack_Type()
)
psupplyRack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psupplyRack.setStatus("mandatory")


class _PsupplySlot_Type(Integer32):
    """Custom type psupplySlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("main", 0)
    )


_PsupplySlot_Type.__name__ = "Integer32"
_PsupplySlot_Object = MibTableColumn
psupplySlot = _PsupplySlot_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 20000, 14, 1, 2),
    _PsupplySlot_Type()
)
psupplySlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psupplySlot.setStatus("mandatory")
_PsupplyIndex_Type = Integer32
_PsupplyIndex_Object = MibTableColumn
psupplyIndex = _PsupplyIndex_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 20000, 14, 1, 3),
    _PsupplyIndex_Type()
)
psupplyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psupplyIndex.setStatus("mandatory")
_PsupplyTypeID_Type = ObjectIdentifier
_PsupplyTypeID_Object = MibTableColumn
psupplyTypeID = _PsupplyTypeID_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 20000, 14, 1, 4),
    _PsupplyTypeID_Type()
)
psupplyTypeID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psupplyTypeID.setStatus("mandatory")
_PsupplyDescr_Type = DisplayString
_PsupplyDescr_Object = MibTableColumn
psupplyDescr = _PsupplyDescr_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 20000, 14, 1, 5),
    _PsupplyDescr_Type()
)
psupplyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psupplyDescr.setStatus("mandatory")


class _PsupplyStatus_Type(Integer32):
    """Custom type psupplyStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              98,
              99)
        )
    )
    namedValues = NamedValues(
        *(("down", 3),
          ("fail", 4),
          ("not-present", 99),
          ("other", 1),
          ("unknown", 98),
          ("up", 2))
    )


_PsupplyStatus_Type.__name__ = "Integer32"
_PsupplyStatus_Object = MibTableColumn
psupplyStatus = _PsupplyStatus_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 20000, 14, 1, 6),
    _PsupplyStatus_Type()
)
psupplyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psupplyStatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects

componentAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 760, 1, 20000, 0, 1)
)
componentAdded.setObjects(
    ("PANDATEL-CHASSIS-MIB", "compTypeID")
)
if mibBuilder.loadTexts:
    componentAdded.setStatus(
        ""
    )

componentRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 760, 1, 20000, 0, 2)
)
componentRemoved.setObjects(
    ("PANDATEL-CHASSIS-MIB", "compTypeID")
)
if mibBuilder.loadTexts:
    componentRemoved.setStatus(
        ""
    )

moduleAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 760, 1, 20000, 0, 3)
)
moduleAdded.setObjects(
    ("PANDATEL-CHASSIS-MIB", "slotModuleTypeID")
)
if mibBuilder.loadTexts:
    moduleAdded.setStatus(
        ""
    )

moduleRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 760, 1, 20000, 0, 4)
)
moduleRemoved.setObjects(
    ("PANDATEL-CHASSIS-MIB", "slotModuleTypeID")
)
if mibBuilder.loadTexts:
    moduleRemoved.setStatus(
        ""
    )

powerSupplyAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 760, 1, 20000, 0, 21)
)
powerSupplyAdded.setObjects(
    ("PANDATEL-CHASSIS-MIB", "psupplyTypeID")
)
if mibBuilder.loadTexts:
    powerSupplyAdded.setStatus(
        ""
    )

powerSupplyRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 760, 1, 20000, 0, 22)
)
powerSupplyRemoved.setObjects(
    ("PANDATEL-CHASSIS-MIB", "psupplyTypeID")
)
if mibBuilder.loadTexts:
    powerSupplyRemoved.setStatus(
        ""
    )

powerSupplyFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 760, 1, 20000, 0, 23)
)
powerSupplyFailed.setObjects(
    ("PANDATEL-CHASSIS-MIB", "psupplyTypeID")
)
if mibBuilder.loadTexts:
    powerSupplyFailed.setStatus(
        ""
    )

powerSupplyRecovered = NotificationType(
    (1, 3, 6, 1, 4, 1, 760, 1, 20000, 0, 24)
)
powerSupplyRecovered.setObjects(
    ("PANDATEL-CHASSIS-MIB", "psupplyTypeID")
)
if mibBuilder.loadTexts:
    powerSupplyRecovered.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PANDATEL-CHASSIS-MIB",
    **{"pandatel": pandatel,
       "mibs": mibs,
       "chassis": chassis,
       "componentAdded": componentAdded,
       "componentRemoved": componentRemoved,
       "moduleAdded": moduleAdded,
       "moduleRemoved": moduleRemoved,
       "powerSupplyAdded": powerSupplyAdded,
       "powerSupplyRemoved": powerSupplyRemoved,
       "powerSupplyFailed": powerSupplyFailed,
       "powerSupplyRecovered": powerSupplyRecovered,
       "chassisTypeID": chassisTypeID,
       "chassisComponents": chassisComponents,
       "chassisDevices": chassisDevices,
       "chassisSlots": chassisSlots,
       "chassisModules": chassisModules,
       "chassisPorts": chassisPorts,
       "chassisComponentTable": chassisComponentTable,
       "compEntry": compEntry,
       "compComp": compComp,
       "compDesign": compDesign,
       "compTypeID": compTypeID,
       "compSlots": compSlots,
       "compModules": compModules,
       "chassisDeviceTable": chassisDeviceTable,
       "devcEntry": devcEntry,
       "devcComp": devcComp,
       "devcSlot": devcSlot,
       "devcTypeID": devcTypeID,
       "devcMgmtAddress": devcMgmtAddress,
       "devcDescr": devcDescr,
       "devcModules": devcModules,
       "devcPorts": devcPorts,
       "devcLastChange": devcLastChange,
       "chassisSlotTable": chassisSlotTable,
       "slotEntry": slotEntry,
       "slotComp": slotComp,
       "slotSlot": slotSlot,
       "slotOwnerDeviceID": slotOwnerDeviceID,
       "slotSlotTypeID": slotSlotTypeID,
       "slotModuleTypeID": slotModuleTypeID,
       "slotModuleName": slotModuleName,
       "slotPorts": slotPorts,
       "chassisPortTable": chassisPortTable,
       "portEntry": portEntry,
       "portComp": portComp,
       "portSlot": portSlot,
       "portPort": portPort,
       "portOwnerDeviceID": portOwnerDeviceID,
       "portFunctionalTypeID": portFunctionalTypeID,
       "portPhysicalType": portPhysicalType,
       "chassisPowerSupplyTable": chassisPowerSupplyTable,
       "psupplyEntry": psupplyEntry,
       "psupplyRack": psupplyRack,
       "psupplySlot": psupplySlot,
       "psupplyIndex": psupplyIndex,
       "psupplyTypeID": psupplyTypeID,
       "psupplyDescr": psupplyDescr,
       "psupplyStatus": psupplyStatus}
)
