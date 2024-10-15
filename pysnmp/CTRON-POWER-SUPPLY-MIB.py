# SNMP MIB module (CTRON-POWER-SUPPLY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CTRON-POWER-SUPPLY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:19:06 2024
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

(ctps,) = mibBuilder.importSymbols(
    "CTRON-MIB-NAMES",
    "ctps")

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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ChPower_ObjectIdentity = ObjectIdentity
chPower = _ChPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 1)
)


class _ChPowerOperationalStatus_Type(Integer32):
    """Custom type chPowerOperationalStatus based on Integer32"""
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
        *(("battery", 5),
          ("powerAC", 1),
          ("powerACRedundant", 2),
          ("powerDC", 3),
          ("powerDCRedundant", 4))
    )


_ChPowerOperationalStatus_Type.__name__ = "Integer32"
_ChPowerOperationalStatus_Object = MibScalar
chPowerOperationalStatus = _ChPowerOperationalStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 1, 1),
    _ChPowerOperationalStatus_Type()
)
chPowerOperationalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chPowerOperationalStatus.setStatus("mandatory")


class _ChPowerMainVoltageStatus_Type(Integer32):
    """Custom type chPowerMainVoltageStatus based on Integer32"""
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
        *(("overCurrent", 2),
          ("overVoltage", 3),
          ("powerOK", 1),
          ("underVoltage", 4))
    )


_ChPowerMainVoltageStatus_Type.__name__ = "Integer32"
_ChPowerMainVoltageStatus_Object = MibScalar
chPowerMainVoltageStatus = _ChPowerMainVoltageStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 1, 2),
    _ChPowerMainVoltageStatus_Type()
)
chPowerMainVoltageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chPowerMainVoltageStatus.setStatus("mandatory")
_ChPowerMainVoltage_Type = Integer32
_ChPowerMainVoltage_Object = MibScalar
chPowerMainVoltage = _ChPowerMainVoltage_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 1, 3),
    _ChPowerMainVoltage_Type()
)
chPowerMainVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chPowerMainVoltage.setStatus("mandatory")
_ChPowerTotalSupply_Type = Integer32
_ChPowerTotalSupply_Object = MibScalar
chPowerTotalSupply = _ChPowerTotalSupply_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 1, 4),
    _ChPowerTotalSupply_Type()
)
chPowerTotalSupply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chPowerTotalSupply.setStatus("mandatory")
_ChPowerTotalLoad_Type = Integer32
_ChPowerTotalLoad_Object = MibScalar
chPowerTotalLoad = _ChPowerTotalLoad_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 1, 5),
    _ChPowerTotalLoad_Type()
)
chPowerTotalLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chPowerTotalLoad.setStatus("mandatory")
_ChPowerMaxSupply_Type = Integer32
_ChPowerMaxSupply_Object = MibScalar
chPowerMaxSupply = _ChPowerMaxSupply_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 1, 6),
    _ChPowerMaxSupply_Type()
)
chPowerMaxSupply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chPowerMaxSupply.setStatus("mandatory")
_ChPowerMaxLoad_Type = Integer32
_ChPowerMaxLoad_Object = MibScalar
chPowerMaxLoad = _ChPowerMaxLoad_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 1, 7),
    _ChPowerMaxLoad_Type()
)
chPowerMaxLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chPowerMaxLoad.setStatus("mandatory")
_ChPowerTable_Object = MibTable
chPowerTable = _ChPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 1, 8)
)
if mibBuilder.loadTexts:
    chPowerTable.setStatus("mandatory")
_ChPowerEntry_Object = MibTableRow
chPowerEntry = _ChPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 1, 8, 1)
)
chPowerEntry.setIndexNames(
    (0, "CTRON-POWER-SUPPLY-MIB", "chPowerLineID"),
)
if mibBuilder.loadTexts:
    chPowerEntry.setStatus("mandatory")
_ChPowerLineID_Type = Integer32
_ChPowerLineID_Object = MibTableColumn
chPowerLineID = _ChPowerLineID_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 1, 8, 1, 1),
    _ChPowerLineID_Type()
)
chPowerLineID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chPowerLineID.setStatus("mandatory")
_ChPowerLineType_Type = ObjectIdentifier
_ChPowerLineType_Object = MibTableColumn
chPowerLineType = _ChPowerLineType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 1, 8, 1, 2),
    _ChPowerLineType_Type()
)
chPowerLineType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chPowerLineType.setStatus("mandatory")
_ChPowerLineTotalSupply_Type = Integer32
_ChPowerLineTotalSupply_Object = MibTableColumn
chPowerLineTotalSupply = _ChPowerLineTotalSupply_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 1, 8, 1, 3),
    _ChPowerLineTotalSupply_Type()
)
chPowerLineTotalSupply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chPowerLineTotalSupply.setStatus("mandatory")
_ChPowerLineTotalLoad_Type = Integer32
_ChPowerLineTotalLoad_Object = MibTableColumn
chPowerLineTotalLoad = _ChPowerLineTotalLoad_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 1, 8, 1, 4),
    _ChPowerLineTotalLoad_Type()
)
chPowerLineTotalLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chPowerLineTotalLoad.setStatus("mandatory")
_ChPowerLineMaxSupply_Type = Integer32
_ChPowerLineMaxSupply_Object = MibTableColumn
chPowerLineMaxSupply = _ChPowerLineMaxSupply_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 1, 8, 1, 5),
    _ChPowerLineMaxSupply_Type()
)
chPowerLineMaxSupply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chPowerLineMaxSupply.setStatus("mandatory")
_ChPowerLineMaxLoad_Type = Integer32
_ChPowerLineMaxLoad_Object = MibTableColumn
chPowerLineMaxLoad = _ChPowerLineMaxLoad_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 1, 8, 1, 6),
    _ChPowerLineMaxLoad_Type()
)
chPowerLineMaxLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chPowerLineMaxLoad.setStatus("mandatory")


class _ChPowerDiagVoltageStatus_Type(Integer32):
    """Custom type chPowerDiagVoltageStatus based on Integer32"""
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
        *(("overCurrent", 2),
          ("overVoltage", 3),
          ("powerOK", 1),
          ("underVoltage", 4))
    )


_ChPowerDiagVoltageStatus_Type.__name__ = "Integer32"
_ChPowerDiagVoltageStatus_Object = MibScalar
chPowerDiagVoltageStatus = _ChPowerDiagVoltageStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 1, 9),
    _ChPowerDiagVoltageStatus_Type()
)
chPowerDiagVoltageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chPowerDiagVoltageStatus.setStatus("mandatory")
_ChPowerDiagVoltage_Type = Integer32
_ChPowerDiagVoltage_Object = MibScalar
chPowerDiagVoltage = _ChPowerDiagVoltage_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 1, 10),
    _ChPowerDiagVoltage_Type()
)
chPowerDiagVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chPowerDiagVoltage.setStatus("mandatory")
_BoardPower_ObjectIdentity = ObjectIdentity
boardPower = _BoardPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 2)
)
_BoardPowerSlotStatusTable_Object = MibTable
boardPowerSlotStatusTable = _BoardPowerSlotStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 2, 1)
)
if mibBuilder.loadTexts:
    boardPowerSlotStatusTable.setStatus("mandatory")
_BoardPowerSlotStatusEntry_Object = MibTableRow
boardPowerSlotStatusEntry = _BoardPowerSlotStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 2, 1, 1)
)
boardPowerSlotStatusEntry.setIndexNames(
    (0, "CTRON-POWER-SUPPLY-MIB", "boardPowerSlotStatusID"),
)
if mibBuilder.loadTexts:
    boardPowerSlotStatusEntry.setStatus("mandatory")
_BoardPowerSlotStatusID_Type = Integer32
_BoardPowerSlotStatusID_Object = MibTableColumn
boardPowerSlotStatusID = _BoardPowerSlotStatusID_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 2, 1, 1, 1),
    _BoardPowerSlotStatusID_Type()
)
boardPowerSlotStatusID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boardPowerSlotStatusID.setStatus("mandatory")


class _BoardPowerOperationalStatus_Type(Integer32):
    """Custom type boardPowerOperationalStatus based on Integer32"""
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
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("frontPanelPowerOff", 11),
          ("overCurrent", 6),
          ("overCurrentShutdown", 7),
          ("overVoltage", 4),
          ("powerConservationShutdown", 10),
          ("powerOff", 2),
          ("powerOn", 1),
          ("remotePowerOff", 9),
          ("reset", 3),
          ("temperatureShutdown", 8),
          ("underVoltage", 5))
    )


_BoardPowerOperationalStatus_Type.__name__ = "Integer32"
_BoardPowerOperationalStatus_Object = MibTableColumn
boardPowerOperationalStatus = _BoardPowerOperationalStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 2, 1, 1, 2),
    _BoardPowerOperationalStatus_Type()
)
boardPowerOperationalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boardPowerOperationalStatus.setStatus("mandatory")


class _BoardPowerAdminStatus_Type(Integer32):
    """Custom type boardPowerAdminStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("powerOff", 2),
          ("powerOn", 1),
          ("reset", 3))
    )


_BoardPowerAdminStatus_Type.__name__ = "Integer32"
_BoardPowerAdminStatus_Object = MibTableColumn
boardPowerAdminStatus = _BoardPowerAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 2, 1, 1, 3),
    _BoardPowerAdminStatus_Type()
)
boardPowerAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    boardPowerAdminStatus.setStatus("mandatory")


class _BoardPowerLocalAdminStatus_Type(Integer32):
    """Custom type boardPowerLocalAdminStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("localMode", 1),
          ("secureMode", 2))
    )


_BoardPowerLocalAdminStatus_Type.__name__ = "Integer32"
_BoardPowerLocalAdminStatus_Object = MibTableColumn
boardPowerLocalAdminStatus = _BoardPowerLocalAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 2, 1, 1, 4),
    _BoardPowerLocalAdminStatus_Type()
)
boardPowerLocalAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    boardPowerLocalAdminStatus.setStatus("mandatory")


class _BoardPowerLocalStatus_Type(Integer32):
    """Custom type boardPowerLocalStatus based on Integer32"""
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
        *(("normal", 4),
          ("powerDownRequest", 2),
          ("powerOnRequest", 3),
          ("resetRequest", 1))
    )


_BoardPowerLocalStatus_Type.__name__ = "Integer32"
_BoardPowerLocalStatus_Object = MibTableColumn
boardPowerLocalStatus = _BoardPowerLocalStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 2, 1, 1, 5),
    _BoardPowerLocalStatus_Type()
)
boardPowerLocalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boardPowerLocalStatus.setStatus("mandatory")


class _BoardPowerShutdownAdmin_Type(Integer32):
    """Custom type boardPowerShutdownAdmin based on Integer32"""
    defaultValue = 2

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


_BoardPowerShutdownAdmin_Type.__name__ = "Integer32"
_BoardPowerShutdownAdmin_Object = MibTableColumn
boardPowerShutdownAdmin = _BoardPowerShutdownAdmin_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 2, 1, 1, 6),
    _BoardPowerShutdownAdmin_Type()
)
boardPowerShutdownAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    boardPowerShutdownAdmin.setStatus("mandatory")


class _BoardPowerPriority_Type(Integer32):
    """Custom type boardPowerPriority based on Integer32"""
    defaultValue = 14

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
    )


_BoardPowerPriority_Type.__name__ = "Integer32"
_BoardPowerPriority_Object = MibTableColumn
boardPowerPriority = _BoardPowerPriority_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 2, 1, 1, 7),
    _BoardPowerPriority_Type()
)
boardPowerPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    boardPowerPriority.setStatus("mandatory")
_BoardPowerMaxInputPower_Type = Integer32
_BoardPowerMaxInputPower_Object = MibTableColumn
boardPowerMaxInputPower = _BoardPowerMaxInputPower_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 2, 1, 1, 8),
    _BoardPowerMaxInputPower_Type()
)
boardPowerMaxInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boardPowerMaxInputPower.setStatus("mandatory")


class _BoardPowerManagement_Type(Integer32):
    """Custom type boardPowerManagement based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              7)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2),
          ("not-supported", 7))
    )


_BoardPowerManagement_Type.__name__ = "Integer32"
_BoardPowerManagement_Object = MibTableColumn
boardPowerManagement = _BoardPowerManagement_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 2, 1, 1, 9),
    _BoardPowerManagement_Type()
)
boardPowerManagement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    boardPowerManagement.setStatus("mandatory")
_BoardPowerSlotTable_Object = MibTable
boardPowerSlotTable = _BoardPowerSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 2, 2)
)
if mibBuilder.loadTexts:
    boardPowerSlotTable.setStatus("mandatory")
_BoardPowerSlotEntry_Object = MibTableRow
boardPowerSlotEntry = _BoardPowerSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 2, 2, 1)
)
boardPowerSlotEntry.setIndexNames(
    (0, "CTRON-POWER-SUPPLY-MIB", "boardPowerSlotID"),
    (0, "CTRON-POWER-SUPPLY-MIB", "boardPowerID"),
)
if mibBuilder.loadTexts:
    boardPowerSlotEntry.setStatus("mandatory")
_BoardPowerSlotID_Type = Integer32
_BoardPowerSlotID_Object = MibTableColumn
boardPowerSlotID = _BoardPowerSlotID_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 2, 2, 1, 1),
    _BoardPowerSlotID_Type()
)
boardPowerSlotID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boardPowerSlotID.setStatus("mandatory")
_BoardPowerID_Type = Integer32
_BoardPowerID_Object = MibTableColumn
boardPowerID = _BoardPowerID_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 2, 2, 1, 2),
    _BoardPowerID_Type()
)
boardPowerID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boardPowerID.setStatus("mandatory")
_BoardPowerType_Type = ObjectIdentifier
_BoardPowerType_Object = MibTableColumn
boardPowerType = _BoardPowerType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 2, 2, 1, 3),
    _BoardPowerType_Type()
)
boardPowerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boardPowerType.setStatus("mandatory")


class _BoardPowerStatus_Type(Integer32):
    """Custom type boardPowerStatus based on Integer32"""
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
        *(("overCurrent", 3),
          ("overVoltage", 4),
          ("powerOK", 1),
          ("powerOff", 2),
          ("underVoltage", 5))
    )


_BoardPowerStatus_Type.__name__ = "Integer32"
_BoardPowerStatus_Object = MibTableColumn
boardPowerStatus = _BoardPowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 2, 2, 1, 4),
    _BoardPowerStatus_Type()
)
boardPowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boardPowerStatus.setStatus("mandatory")
_BoardPowerVoltage_Type = Integer32
_BoardPowerVoltage_Object = MibTableColumn
boardPowerVoltage = _BoardPowerVoltage_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 2, 2, 1, 5),
    _BoardPowerVoltage_Type()
)
boardPowerVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boardPowerVoltage.setStatus("mandatory")
_BoardPowerCurrent_Type = Integer32
_BoardPowerCurrent_Object = MibTableColumn
boardPowerCurrent = _BoardPowerCurrent_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 2, 2, 1, 6),
    _BoardPowerCurrent_Type()
)
boardPowerCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boardPowerCurrent.setStatus("mandatory")
_BoardPowerMaxVoltage_Type = Integer32
_BoardPowerMaxVoltage_Object = MibTableColumn
boardPowerMaxVoltage = _BoardPowerMaxVoltage_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 2, 2, 1, 7),
    _BoardPowerMaxVoltage_Type()
)
boardPowerMaxVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boardPowerMaxVoltage.setStatus("mandatory")
_BoardPowerMinVoltage_Type = Integer32
_BoardPowerMinVoltage_Object = MibTableColumn
boardPowerMinVoltage = _BoardPowerMinVoltage_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 2, 2, 1, 8),
    _BoardPowerMinVoltage_Type()
)
boardPowerMinVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boardPowerMinVoltage.setStatus("mandatory")
_BoardPowerMaxPower_Type = Integer32
_BoardPowerMaxPower_Object = MibTableColumn
boardPowerMaxPower = _BoardPowerMaxPower_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 2, 2, 1, 9),
    _BoardPowerMaxPower_Type()
)
boardPowerMaxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boardPowerMaxPower.setStatus("mandatory")
_PsPower_ObjectIdentity = ObjectIdentity
psPower = _PsPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 3)
)
_PsPowerSlotStatusTable_Object = MibTable
psPowerSlotStatusTable = _PsPowerSlotStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 3, 1)
)
if mibBuilder.loadTexts:
    psPowerSlotStatusTable.setStatus("mandatory")
_PsPowerSlotStatusEntry_Object = MibTableRow
psPowerSlotStatusEntry = _PsPowerSlotStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 3, 1, 1)
)
psPowerSlotStatusEntry.setIndexNames(
    (0, "CTRON-POWER-SUPPLY-MIB", "psPowerSlotStatusID"),
)
if mibBuilder.loadTexts:
    psPowerSlotStatusEntry.setStatus("mandatory")
_PsPowerSlotStatusID_Type = Integer32
_PsPowerSlotStatusID_Object = MibTableColumn
psPowerSlotStatusID = _PsPowerSlotStatusID_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 3, 1, 1, 1),
    _PsPowerSlotStatusID_Type()
)
psPowerSlotStatusID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psPowerSlotStatusID.setStatus("mandatory")


class _PsPowerOperationalStatus_Type(Integer32):
    """Custom type psPowerOperationalStatus based on Integer32"""
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
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("overCurrent", 6),
          ("overCurrentShutdown", 7),
          ("overVoltage", 4),
          ("powerOff", 2),
          ("powerOn", 1),
          ("remotePowerOff", 9),
          ("reset", 3),
          ("temperatureShutdown", 8),
          ("underVoltage", 5))
    )


_PsPowerOperationalStatus_Type.__name__ = "Integer32"
_PsPowerOperationalStatus_Object = MibTableColumn
psPowerOperationalStatus = _PsPowerOperationalStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 3, 1, 1, 2),
    _PsPowerOperationalStatus_Type()
)
psPowerOperationalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psPowerOperationalStatus.setStatus("mandatory")


class _PsPowerAdminStatus_Type(Integer32):
    """Custom type psPowerAdminStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("powerOff", 2),
          ("powerOn", 1))
    )


_PsPowerAdminStatus_Type.__name__ = "Integer32"
_PsPowerAdminStatus_Object = MibTableColumn
psPowerAdminStatus = _PsPowerAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 3, 1, 1, 3),
    _PsPowerAdminStatus_Type()
)
psPowerAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    psPowerAdminStatus.setStatus("mandatory")
_PsPowerMaxOutputPower_Type = Integer32
_PsPowerMaxOutputPower_Object = MibTableColumn
psPowerMaxOutputPower = _PsPowerMaxOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 3, 1, 1, 4),
    _PsPowerMaxOutputPower_Type()
)
psPowerMaxOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psPowerMaxOutputPower.setStatus("mandatory")
_PsPowerSlotTable_Object = MibTable
psPowerSlotTable = _PsPowerSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 3, 2)
)
if mibBuilder.loadTexts:
    psPowerSlotTable.setStatus("mandatory")
_PsPowerSlotEntry_Object = MibTableRow
psPowerSlotEntry = _PsPowerSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 3, 2, 1)
)
psPowerSlotEntry.setIndexNames(
    (0, "CTRON-POWER-SUPPLY-MIB", "psPowerSlotID"),
    (0, "CTRON-POWER-SUPPLY-MIB", "psPowerID"),
)
if mibBuilder.loadTexts:
    psPowerSlotEntry.setStatus("mandatory")
_PsPowerSlotID_Type = Integer32
_PsPowerSlotID_Object = MibTableColumn
psPowerSlotID = _PsPowerSlotID_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 3, 2, 1, 1),
    _PsPowerSlotID_Type()
)
psPowerSlotID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psPowerSlotID.setStatus("mandatory")
_PsPowerID_Type = Integer32
_PsPowerID_Object = MibTableColumn
psPowerID = _PsPowerID_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 3, 2, 1, 2),
    _PsPowerID_Type()
)
psPowerID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psPowerID.setStatus("mandatory")
_PsPowerType_Type = ObjectIdentifier
_PsPowerType_Object = MibTableColumn
psPowerType = _PsPowerType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 3, 2, 1, 3),
    _PsPowerType_Type()
)
psPowerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psPowerType.setStatus("mandatory")


class _PsPowerStatus_Type(Integer32):
    """Custom type psPowerStatus based on Integer32"""
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
        *(("overCurrent", 3),
          ("overVoltage", 4),
          ("powerOK", 1),
          ("powerOff", 2),
          ("underVoltage", 5))
    )


_PsPowerStatus_Type.__name__ = "Integer32"
_PsPowerStatus_Object = MibTableColumn
psPowerStatus = _PsPowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 3, 2, 1, 4),
    _PsPowerStatus_Type()
)
psPowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psPowerStatus.setStatus("mandatory")


class _PsPowerAdmin_Type(Integer32):
    """Custom type psPowerAdmin based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("powerOff", 2),
          ("powerOn", 1))
    )


_PsPowerAdmin_Type.__name__ = "Integer32"
_PsPowerAdmin_Object = MibTableColumn
psPowerAdmin = _PsPowerAdmin_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 3, 2, 1, 5),
    _PsPowerAdmin_Type()
)
psPowerAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    psPowerAdmin.setStatus("mandatory")
_PsPowerVoltage_Type = Integer32
_PsPowerVoltage_Object = MibTableColumn
psPowerVoltage = _PsPowerVoltage_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 3, 2, 1, 6),
    _PsPowerVoltage_Type()
)
psPowerVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psPowerVoltage.setStatus("mandatory")
_PsPowerCurrent_Type = Integer32
_PsPowerCurrent_Object = MibTableColumn
psPowerCurrent = _PsPowerCurrent_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 3, 2, 1, 7),
    _PsPowerCurrent_Type()
)
psPowerCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psPowerCurrent.setStatus("mandatory")
_PsPowerLineFrequency_Type = Integer32
_PsPowerLineFrequency_Object = MibTableColumn
psPowerLineFrequency = _PsPowerLineFrequency_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 3, 2, 1, 8),
    _PsPowerLineFrequency_Type()
)
psPowerLineFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psPowerLineFrequency.setStatus("mandatory")
_PsPowerMaxVoltage_Type = Integer32
_PsPowerMaxVoltage_Object = MibTableColumn
psPowerMaxVoltage = _PsPowerMaxVoltage_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 3, 2, 1, 9),
    _PsPowerMaxVoltage_Type()
)
psPowerMaxVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psPowerMaxVoltage.setStatus("mandatory")
_PsPowerMinVoltage_Type = Integer32
_PsPowerMinVoltage_Object = MibTableColumn
psPowerMinVoltage = _PsPowerMinVoltage_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 3, 2, 1, 10),
    _PsPowerMinVoltage_Type()
)
psPowerMinVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psPowerMinVoltage.setStatus("mandatory")
_PsPowerMaxPower_Type = Integer32
_PsPowerMaxPower_Object = MibTableColumn
psPowerMaxPower = _PsPowerMaxPower_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 3, 2, 1, 11),
    _PsPowerMaxPower_Type()
)
psPowerMaxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psPowerMaxPower.setStatus("mandatory")
_BbuPower_ObjectIdentity = ObjectIdentity
bbuPower = _BbuPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 4)
)
_TermPower_ObjectIdentity = ObjectIdentity
termPower = _TermPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 5)
)


class _TermPowerStatus_Type(Integer32):
    """Custom type termPowerStatus based on Integer32"""
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
        *(("overCurrent", 2),
          ("overPower", 5),
          ("overVoltage", 3),
          ("powerOK", 1),
          ("underVolatge", 4))
    )


_TermPowerStatus_Type.__name__ = "Integer32"
_TermPowerStatus_Object = MibScalar
termPowerStatus = _TermPowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 5, 1),
    _TermPowerStatus_Type()
)
termPowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    termPowerStatus.setStatus("mandatory")
_TermPowerVoltage_Type = Integer32
_TermPowerVoltage_Object = MibScalar
termPowerVoltage = _TermPowerVoltage_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 5, 2),
    _TermPowerVoltage_Type()
)
termPowerVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    termPowerVoltage.setStatus("mandatory")
_TermPowerCurrent_Type = Integer32
_TermPowerCurrent_Object = MibScalar
termPowerCurrent = _TermPowerCurrent_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 5, 3),
    _TermPowerCurrent_Type()
)
termPowerCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    termPowerCurrent.setStatus("mandatory")


class _TermPowerModule1Status_Type(Integer32):
    """Custom type termPowerModule1Status based on Integer32"""
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
        *(("fault", 4),
          ("iNBaFault", 2),
          ("iNBbFault", 3),
          ("normal", 1),
          ("termModuleNotInstalled", 5),
          ("unknown", 6))
    )


_TermPowerModule1Status_Type.__name__ = "Integer32"
_TermPowerModule1Status_Object = MibScalar
termPowerModule1Status = _TermPowerModule1Status_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 5, 4),
    _TermPowerModule1Status_Type()
)
termPowerModule1Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    termPowerModule1Status.setStatus("mandatory")


class _TermPowerModule2Status_Type(Integer32):
    """Custom type termPowerModule2Status based on Integer32"""
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
        *(("fault", 4),
          ("iNBaFault", 2),
          ("iNBbFault", 3),
          ("normal", 1),
          ("termModuleNotInstalled", 5),
          ("unknown", 6))
    )


_TermPowerModule2Status_Type.__name__ = "Integer32"
_TermPowerModule2Status_Object = MibScalar
termPowerModule2Status = _TermPowerModule2Status_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 5, 5),
    _TermPowerModule2Status_Type()
)
termPowerModule2Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    termPowerModule2Status.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CTRON-POWER-SUPPLY-MIB",
    **{"chPower": chPower,
       "chPowerOperationalStatus": chPowerOperationalStatus,
       "chPowerMainVoltageStatus": chPowerMainVoltageStatus,
       "chPowerMainVoltage": chPowerMainVoltage,
       "chPowerTotalSupply": chPowerTotalSupply,
       "chPowerTotalLoad": chPowerTotalLoad,
       "chPowerMaxSupply": chPowerMaxSupply,
       "chPowerMaxLoad": chPowerMaxLoad,
       "chPowerTable": chPowerTable,
       "chPowerEntry": chPowerEntry,
       "chPowerLineID": chPowerLineID,
       "chPowerLineType": chPowerLineType,
       "chPowerLineTotalSupply": chPowerLineTotalSupply,
       "chPowerLineTotalLoad": chPowerLineTotalLoad,
       "chPowerLineMaxSupply": chPowerLineMaxSupply,
       "chPowerLineMaxLoad": chPowerLineMaxLoad,
       "chPowerDiagVoltageStatus": chPowerDiagVoltageStatus,
       "chPowerDiagVoltage": chPowerDiagVoltage,
       "boardPower": boardPower,
       "boardPowerSlotStatusTable": boardPowerSlotStatusTable,
       "boardPowerSlotStatusEntry": boardPowerSlotStatusEntry,
       "boardPowerSlotStatusID": boardPowerSlotStatusID,
       "boardPowerOperationalStatus": boardPowerOperationalStatus,
       "boardPowerAdminStatus": boardPowerAdminStatus,
       "boardPowerLocalAdminStatus": boardPowerLocalAdminStatus,
       "boardPowerLocalStatus": boardPowerLocalStatus,
       "boardPowerShutdownAdmin": boardPowerShutdownAdmin,
       "boardPowerPriority": boardPowerPriority,
       "boardPowerMaxInputPower": boardPowerMaxInputPower,
       "boardPowerManagement": boardPowerManagement,
       "boardPowerSlotTable": boardPowerSlotTable,
       "boardPowerSlotEntry": boardPowerSlotEntry,
       "boardPowerSlotID": boardPowerSlotID,
       "boardPowerID": boardPowerID,
       "boardPowerType": boardPowerType,
       "boardPowerStatus": boardPowerStatus,
       "boardPowerVoltage": boardPowerVoltage,
       "boardPowerCurrent": boardPowerCurrent,
       "boardPowerMaxVoltage": boardPowerMaxVoltage,
       "boardPowerMinVoltage": boardPowerMinVoltage,
       "boardPowerMaxPower": boardPowerMaxPower,
       "psPower": psPower,
       "psPowerSlotStatusTable": psPowerSlotStatusTable,
       "psPowerSlotStatusEntry": psPowerSlotStatusEntry,
       "psPowerSlotStatusID": psPowerSlotStatusID,
       "psPowerOperationalStatus": psPowerOperationalStatus,
       "psPowerAdminStatus": psPowerAdminStatus,
       "psPowerMaxOutputPower": psPowerMaxOutputPower,
       "psPowerSlotTable": psPowerSlotTable,
       "psPowerSlotEntry": psPowerSlotEntry,
       "psPowerSlotID": psPowerSlotID,
       "psPowerID": psPowerID,
       "psPowerType": psPowerType,
       "psPowerStatus": psPowerStatus,
       "psPowerAdmin": psPowerAdmin,
       "psPowerVoltage": psPowerVoltage,
       "psPowerCurrent": psPowerCurrent,
       "psPowerLineFrequency": psPowerLineFrequency,
       "psPowerMaxVoltage": psPowerMaxVoltage,
       "psPowerMinVoltage": psPowerMinVoltage,
       "psPowerMaxPower": psPowerMaxPower,
       "bbuPower": bbuPower,
       "termPower": termPower,
       "termPowerStatus": termPowerStatus,
       "termPowerVoltage": termPowerVoltage,
       "termPowerCurrent": termPowerCurrent,
       "termPowerModule1Status": termPowerModule1Status,
       "termPowerModule2Status": termPowerModule2Status}
)
