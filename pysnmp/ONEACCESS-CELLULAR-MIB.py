# SNMP MIB module (ONEACCESS-CELLULAR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ONEACCESS-CELLULAR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:34:49 2024
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

(oacExpIMCellRadio,
 oacMIBModules) = mibBuilder.importSymbols(
    "ONEACCESS-GLOBAL-REG",
    "oacExpIMCellRadio",
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

oacCellularMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 1, 100, 1000)
)
oacCellularMIBModule.setRevisions(
        ("2014-04-07 00:00",
         "2013-10-15 00:00",
         "2011-10-27 00:00",
         "2010-07-08 00:01")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_OacCellRadioRssi_ObjectIdentity = ObjectIdentity
oacCellRadioRssi = _OacCellRadioRssi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 9, 1)
)
_OacCellRssiLastHourTable_Object = MibTable
oacCellRssiLastHourTable = _OacCellRssiLastHourTable_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 9, 1, 1)
)
if mibBuilder.loadTexts:
    oacCellRssiLastHourTable.setStatus("current")
_OacCellRssiLastHourEntry_Object = MibTableRow
oacCellRssiLastHourEntry = _OacCellRssiLastHourEntry_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 9, 1, 1, 1)
)
oacCellRssiLastHourEntry.setIndexNames(
    (0, "ONEACCESS-CELLULAR-MIB", "oacCellRssiLastHourMinutes"),
)
if mibBuilder.loadTexts:
    oacCellRssiLastHourEntry.setStatus("current")
_OacCellRssiLastHourMinutes_Type = Unsigned32
_OacCellRssiLastHourMinutes_Object = MibTableColumn
oacCellRssiLastHourMinutes = _OacCellRssiLastHourMinutes_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 9, 1, 1, 1, 1),
    _OacCellRssiLastHourMinutes_Type()
)
oacCellRssiLastHourMinutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacCellRssiLastHourMinutes.setStatus("current")
_OacCellRssiLastHourMin_Type = Integer32
_OacCellRssiLastHourMin_Object = MibTableColumn
oacCellRssiLastHourMin = _OacCellRssiLastHourMin_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 9, 1, 1, 1, 2),
    _OacCellRssiLastHourMin_Type()
)
oacCellRssiLastHourMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacCellRssiLastHourMin.setStatus("current")
_OacCellRssiLastHourAvg_Type = Integer32
_OacCellRssiLastHourAvg_Object = MibTableColumn
oacCellRssiLastHourAvg = _OacCellRssiLastHourAvg_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 9, 1, 1, 1, 3),
    _OacCellRssiLastHourAvg_Type()
)
oacCellRssiLastHourAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacCellRssiLastHourAvg.setStatus("current")
_OacCellRssiLastHourMax_Type = Integer32
_OacCellRssiLastHourMax_Object = MibTableColumn
oacCellRssiLastHourMax = _OacCellRssiLastHourMax_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 9, 1, 1, 1, 4),
    _OacCellRssiLastHourMax_Type()
)
oacCellRssiLastHourMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacCellRssiLastHourMax.setStatus("current")
_OacCellRssiLastDayTable_Object = MibTable
oacCellRssiLastDayTable = _OacCellRssiLastDayTable_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 9, 1, 2)
)
if mibBuilder.loadTexts:
    oacCellRssiLastDayTable.setStatus("current")
_OacCellRssiLastDayEntry_Object = MibTableRow
oacCellRssiLastDayEntry = _OacCellRssiLastDayEntry_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 9, 1, 2, 1)
)
oacCellRssiLastDayEntry.setIndexNames(
    (0, "ONEACCESS-CELLULAR-MIB", "oacCellRssiLastDayHours"),
)
if mibBuilder.loadTexts:
    oacCellRssiLastDayEntry.setStatus("current")
_OacCellRssiLastDayHours_Type = Unsigned32
_OacCellRssiLastDayHours_Object = MibTableColumn
oacCellRssiLastDayHours = _OacCellRssiLastDayHours_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 9, 1, 2, 1, 1),
    _OacCellRssiLastDayHours_Type()
)
oacCellRssiLastDayHours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacCellRssiLastDayHours.setStatus("current")
_OacCellRssiLastDayMin_Type = Integer32
_OacCellRssiLastDayMin_Object = MibTableColumn
oacCellRssiLastDayMin = _OacCellRssiLastDayMin_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 9, 1, 2, 1, 2),
    _OacCellRssiLastDayMin_Type()
)
oacCellRssiLastDayMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacCellRssiLastDayMin.setStatus("current")
_OacCellRssiLastDayAvg_Type = Integer32
_OacCellRssiLastDayAvg_Object = MibTableColumn
oacCellRssiLastDayAvg = _OacCellRssiLastDayAvg_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 9, 1, 2, 1, 3),
    _OacCellRssiLastDayAvg_Type()
)
oacCellRssiLastDayAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacCellRssiLastDayAvg.setStatus("current")
_OacCellRssiLastDayMax_Type = Integer32
_OacCellRssiLastDayMax_Object = MibTableColumn
oacCellRssiLastDayMax = _OacCellRssiLastDayMax_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 9, 1, 2, 1, 4),
    _OacCellRssiLastDayMax_Type()
)
oacCellRssiLastDayMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacCellRssiLastDayMax.setStatus("current")
_OacCellRssiLastMonthTable_Object = MibTable
oacCellRssiLastMonthTable = _OacCellRssiLastMonthTable_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 9, 1, 3)
)
if mibBuilder.loadTexts:
    oacCellRssiLastMonthTable.setStatus("current")
_OacCellRssiLastMonthEntry_Object = MibTableRow
oacCellRssiLastMonthEntry = _OacCellRssiLastMonthEntry_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 9, 1, 3, 1)
)
oacCellRssiLastMonthEntry.setIndexNames(
    (0, "ONEACCESS-CELLULAR-MIB", "oacCellRssiLastMonthDays"),
)
if mibBuilder.loadTexts:
    oacCellRssiLastMonthEntry.setStatus("current")
_OacCellRssiLastMonthDays_Type = Unsigned32
_OacCellRssiLastMonthDays_Object = MibTableColumn
oacCellRssiLastMonthDays = _OacCellRssiLastMonthDays_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 9, 1, 3, 1, 1),
    _OacCellRssiLastMonthDays_Type()
)
oacCellRssiLastMonthDays.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacCellRssiLastMonthDays.setStatus("current")
_OacCellRssiLastMonthMin_Type = Integer32
_OacCellRssiLastMonthMin_Object = MibTableColumn
oacCellRssiLastMonthMin = _OacCellRssiLastMonthMin_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 9, 1, 3, 1, 2),
    _OacCellRssiLastMonthMin_Type()
)
oacCellRssiLastMonthMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacCellRssiLastMonthMin.setStatus("current")
_OacCellRssiLastMonthAvg_Type = Integer32
_OacCellRssiLastMonthAvg_Object = MibTableColumn
oacCellRssiLastMonthAvg = _OacCellRssiLastMonthAvg_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 9, 1, 3, 1, 3),
    _OacCellRssiLastMonthAvg_Type()
)
oacCellRssiLastMonthAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacCellRssiLastMonthAvg.setStatus("current")
_OacCellRssiLastMonthMax_Type = Integer32
_OacCellRssiLastMonthMax_Object = MibTableColumn
oacCellRssiLastMonthMax = _OacCellRssiLastMonthMax_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 9, 1, 3, 1, 4),
    _OacCellRssiLastMonthMax_Type()
)
oacCellRssiLastMonthMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacCellRssiLastMonthMax.setStatus("current")
_OacCellRadioModuleTable_Object = MibTable
oacCellRadioModuleTable = _OacCellRadioModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 9, 2)
)
if mibBuilder.loadTexts:
    oacCellRadioModuleTable.setStatus("current")
_OacCellRadioModuleEntry_Object = MibTableRow
oacCellRadioModuleEntry = _OacCellRadioModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 9, 2, 1)
)
oacCellRadioModuleEntry.setIndexNames(
    (0, "ONEACCESS-CELLULAR-MIB", "oacCellModuleIndex"),
)
if mibBuilder.loadTexts:
    oacCellRadioModuleEntry.setStatus("current")
_OacCellModuleIndex_Type = Unsigned32
_OacCellModuleIndex_Object = MibTableColumn
oacCellModuleIndex = _OacCellModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 9, 2, 1, 1),
    _OacCellModuleIndex_Type()
)
oacCellModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacCellModuleIndex.setStatus("current")
_OacCellManufacturer_Type = DisplayString
_OacCellManufacturer_Object = MibTableColumn
oacCellManufacturer = _OacCellManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 9, 2, 1, 10),
    _OacCellManufacturer_Type()
)
oacCellManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacCellManufacturer.setStatus("current")
_OacCellEquipment_Type = DisplayString
_OacCellEquipment_Object = MibTableColumn
oacCellEquipment = _OacCellEquipment_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 9, 2, 1, 11),
    _OacCellEquipment_Type()
)
oacCellEquipment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacCellEquipment.setStatus("current")
_OacCellBootRevision_Type = DisplayString
_OacCellBootRevision_Object = MibTableColumn
oacCellBootRevision = _OacCellBootRevision_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 9, 2, 1, 12),
    _OacCellBootRevision_Type()
)
oacCellBootRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacCellBootRevision.setStatus("current")
_OacCellRevision_Type = DisplayString
_OacCellRevision_Object = MibTableColumn
oacCellRevision = _OacCellRevision_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 9, 2, 1, 13),
    _OacCellRevision_Type()
)
oacCellRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacCellRevision.setStatus("current")
_OacCellIMEI_Type = DisplayString
_OacCellIMEI_Object = MibTableColumn
oacCellIMEI = _OacCellIMEI_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 9, 2, 1, 14),
    _OacCellIMEI_Type()
)
oacCellIMEI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacCellIMEI.setStatus("current")
_OacCellMEID_Type = DisplayString
_OacCellMEID_Object = MibTableColumn
oacCellMEID = _OacCellMEID_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 9, 2, 1, 15),
    _OacCellMEID_Type()
)
oacCellMEID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacCellMEID.setStatus("current")
_OacCellSIMStatus_Type = DisplayString
_OacCellSIMStatus_Object = MibTableColumn
oacCellSIMStatus = _OacCellSIMStatus_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 9, 2, 1, 20),
    _OacCellSIMStatus_Type()
)
oacCellSIMStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacCellSIMStatus.setStatus("current")
_OacCellIMSI_Type = DisplayString
_OacCellIMSI_Object = MibTableColumn
oacCellIMSI = _OacCellIMSI_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 9, 2, 1, 21),
    _OacCellIMSI_Type()
)
oacCellIMSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacCellIMSI.setStatus("current")
_OacCellICCI_Type = DisplayString
_OacCellICCI_Object = MibTableColumn
oacCellICCI = _OacCellICCI_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 9, 2, 1, 22),
    _OacCellICCI_Type()
)
oacCellICCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacCellICCI.setStatus("current")
_OacCellPinStatus_Type = DisplayString
_OacCellPinStatus_Object = MibTableColumn
oacCellPinStatus = _OacCellPinStatus_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 9, 2, 1, 30),
    _OacCellPinStatus_Type()
)
oacCellPinStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacCellPinStatus.setStatus("current")
_OacCellSelectedOperator_Type = DisplayString
_OacCellSelectedOperator_Object = MibTableColumn
oacCellSelectedOperator = _OacCellSelectedOperator_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 9, 2, 1, 40),
    _OacCellSelectedOperator_Type()
)
oacCellSelectedOperator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacCellSelectedOperator.setStatus("current")
_OacCellSignalStrength_Type = Integer32
_OacCellSignalStrength_Object = MibTableColumn
oacCellSignalStrength = _OacCellSignalStrength_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 9, 2, 1, 41),
    _OacCellSignalStrength_Type()
)
oacCellSignalStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacCellSignalStrength.setStatus("current")
_OacCellEcIo_Type = Integer32
_OacCellEcIo_Object = MibTableColumn
oacCellEcIo = _OacCellEcIo_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 9, 2, 1, 42),
    _OacCellEcIo_Type()
)
oacCellEcIo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacCellEcIo.setStatus("current")
_OacCellRSRQ_Type = Integer32
_OacCellRSRQ_Object = MibTableColumn
oacCellRSRQ = _OacCellRSRQ_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 9, 2, 1, 43),
    _OacCellRSRQ_Type()
)
oacCellRSRQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacCellRSRQ.setStatus("current")
_OacCellRSRP_Type = Integer32
_OacCellRSRP_Object = MibTableColumn
oacCellRSRP = _OacCellRSRP_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 9, 2, 1, 44),
    _OacCellRSRP_Type()
)
oacCellRSRP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacCellRSRP.setStatus("current")
_OacCellSNR_Type = Integer32
_OacCellSNR_Object = MibTableColumn
oacCellSNR = _OacCellSNR_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 9, 2, 1, 45),
    _OacCellSNR_Type()
)
oacCellSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacCellSNR.setStatus("current")
_OacCellRadioAccessTechnology_Type = DisplayString
_OacCellRadioAccessTechnology_Object = MibTableColumn
oacCellRadioAccessTechnology = _OacCellRadioAccessTechnology_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 9, 2, 1, 46),
    _OacCellRadioAccessTechnology_Type()
)
oacCellRadioAccessTechnology.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacCellRadioAccessTechnology.setStatus("current")
_OacCellCircuitSwitchedState_Type = DisplayString
_OacCellCircuitSwitchedState_Object = MibTableColumn
oacCellCircuitSwitchedState = _OacCellCircuitSwitchedState_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 9, 2, 1, 47),
    _OacCellCircuitSwitchedState_Type()
)
oacCellCircuitSwitchedState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacCellCircuitSwitchedState.setStatus("current")
_OacCellPacketSwitchedState_Type = DisplayString
_OacCellPacketSwitchedState_Object = MibTableColumn
oacCellPacketSwitchedState = _OacCellPacketSwitchedState_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 9, 2, 1, 48),
    _OacCellPacketSwitchedState_Type()
)
oacCellPacketSwitchedState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacCellPacketSwitchedState.setStatus("current")
_OacCellResetOnLossOfRegistration_Type = Unsigned32
_OacCellResetOnLossOfRegistration_Object = MibTableColumn
oacCellResetOnLossOfRegistration = _OacCellResetOnLossOfRegistration_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 9, 2, 1, 60),
    _OacCellResetOnLossOfRegistration_Type()
)
oacCellResetOnLossOfRegistration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacCellResetOnLossOfRegistration.setStatus("current")
_OacCellResetOnFailedRegistration_Type = Unsigned32
_OacCellResetOnFailedRegistration_Object = MibTableColumn
oacCellResetOnFailedRegistration = _OacCellResetOnFailedRegistration_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 9, 2, 1, 61),
    _OacCellResetOnFailedRegistration_Type()
)
oacCellResetOnFailedRegistration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacCellResetOnFailedRegistration.setStatus("current")
_OacCellHardwareReset_Type = Unsigned32
_OacCellHardwareReset_Object = MibTableColumn
oacCellHardwareReset = _OacCellHardwareReset_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 9, 2, 1, 62),
    _OacCellHardwareReset_Type()
)
oacCellHardwareReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacCellHardwareReset.setStatus("current")
_OacCellLAC_Type = DisplayString
_OacCellLAC_Object = MibTableColumn
oacCellLAC = _OacCellLAC_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 9, 2, 1, 70),
    _OacCellLAC_Type()
)
oacCellLAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacCellLAC.setStatus("current")
_OacCellCellID_Type = DisplayString
_OacCellCellID_Object = MibTableColumn
oacCellCellID = _OacCellCellID_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 9, 2, 1, 71),
    _OacCellCellID_Type()
)
oacCellCellID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacCellCellID.setStatus("current")
_OacCellTAC_Type = DisplayString
_OacCellTAC_Object = MibTableColumn
oacCellTAC = _OacCellTAC_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 9, 2, 1, 72),
    _OacCellTAC_Type()
)
oacCellTAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacCellTAC.setStatus("current")
_OacCellPLMN_Type = DisplayString
_OacCellPLMN_Object = MibTableColumn
oacCellPLMN = _OacCellPLMN_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 9, 2, 1, 73),
    _OacCellPLMN_Type()
)
oacCellPLMN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacCellPLMN.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ONEACCESS-CELLULAR-MIB",
    **{"oacCellularMIBModule": oacCellularMIBModule,
       "oacCellRadioRssi": oacCellRadioRssi,
       "oacCellRssiLastHourTable": oacCellRssiLastHourTable,
       "oacCellRssiLastHourEntry": oacCellRssiLastHourEntry,
       "oacCellRssiLastHourMinutes": oacCellRssiLastHourMinutes,
       "oacCellRssiLastHourMin": oacCellRssiLastHourMin,
       "oacCellRssiLastHourAvg": oacCellRssiLastHourAvg,
       "oacCellRssiLastHourMax": oacCellRssiLastHourMax,
       "oacCellRssiLastDayTable": oacCellRssiLastDayTable,
       "oacCellRssiLastDayEntry": oacCellRssiLastDayEntry,
       "oacCellRssiLastDayHours": oacCellRssiLastDayHours,
       "oacCellRssiLastDayMin": oacCellRssiLastDayMin,
       "oacCellRssiLastDayAvg": oacCellRssiLastDayAvg,
       "oacCellRssiLastDayMax": oacCellRssiLastDayMax,
       "oacCellRssiLastMonthTable": oacCellRssiLastMonthTable,
       "oacCellRssiLastMonthEntry": oacCellRssiLastMonthEntry,
       "oacCellRssiLastMonthDays": oacCellRssiLastMonthDays,
       "oacCellRssiLastMonthMin": oacCellRssiLastMonthMin,
       "oacCellRssiLastMonthAvg": oacCellRssiLastMonthAvg,
       "oacCellRssiLastMonthMax": oacCellRssiLastMonthMax,
       "oacCellRadioModuleTable": oacCellRadioModuleTable,
       "oacCellRadioModuleEntry": oacCellRadioModuleEntry,
       "oacCellModuleIndex": oacCellModuleIndex,
       "oacCellManufacturer": oacCellManufacturer,
       "oacCellEquipment": oacCellEquipment,
       "oacCellBootRevision": oacCellBootRevision,
       "oacCellRevision": oacCellRevision,
       "oacCellIMEI": oacCellIMEI,
       "oacCellMEID": oacCellMEID,
       "oacCellSIMStatus": oacCellSIMStatus,
       "oacCellIMSI": oacCellIMSI,
       "oacCellICCI": oacCellICCI,
       "oacCellPinStatus": oacCellPinStatus,
       "oacCellSelectedOperator": oacCellSelectedOperator,
       "oacCellSignalStrength": oacCellSignalStrength,
       "oacCellEcIo": oacCellEcIo,
       "oacCellRSRQ": oacCellRSRQ,
       "oacCellRSRP": oacCellRSRP,
       "oacCellSNR": oacCellSNR,
       "oacCellRadioAccessTechnology": oacCellRadioAccessTechnology,
       "oacCellCircuitSwitchedState": oacCellCircuitSwitchedState,
       "oacCellPacketSwitchedState": oacCellPacketSwitchedState,
       "oacCellResetOnLossOfRegistration": oacCellResetOnLossOfRegistration,
       "oacCellResetOnFailedRegistration": oacCellResetOnFailedRegistration,
       "oacCellHardwareReset": oacCellHardwareReset,
       "oacCellLAC": oacCellLAC,
       "oacCellCellID": oacCellCellID,
       "oacCellTAC": oacCellTAC,
       "oacCellPLMN": oacCellPLMN}
)
