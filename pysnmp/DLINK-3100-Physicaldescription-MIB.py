# SNMP MIB module (DLINK-3100-Physicaldescription-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DLINK-3100-Physicaldescription-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:30:13 2024
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

(rndErrorDesc,
 rndErrorSeverity) = mibBuilder.importSymbols(
    "DLINK-3100-DEVICEPARAMS-MIB",
    "rndErrorDesc",
    "rndErrorSeverity")

(RlEnvMonState,) = mibBuilder.importSymbols(
    "DLINK-3100-HWENVIROMENT",
    "RlEnvMonState")

(rnd,
 rndNotifications) = mibBuilder.importSymbols(
    "DLINK-3100-MIB",
    "rnd",
    "rndNotifications")

(EntitySensorStatus,
 EntitySensorValue) = mibBuilder.importSymbols(
    "ENTITY-SENSOR-MIB",
    "EntitySensorStatus",
    "EntitySensorValue")

(InterfaceIndex,
 InterfaceIndexOrZero,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero",
    "ifIndex")

(JackType,) = mibBuilder.importSymbols(
    "MAU-MIB",
    "JackType")

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
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

rlPhysicalDescription = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 53)
)
rlPhysicalDescription.setRevisions(
        ("2006-02-12 00:00",
         "2003-10-18 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RlPhdMibVersion_Type = Integer32
_RlPhdMibVersion_Object = MibScalar
rlPhdMibVersion = _RlPhdMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 53, 1),
    _RlPhdMibVersion_Type()
)
rlPhdMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPhdMibVersion.setStatus("current")
_RlPhdModuleTable_Object = MibTable
rlPhdModuleTable = _RlPhdModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 53, 2)
)
if mibBuilder.loadTexts:
    rlPhdModuleTable.setStatus("current")
_RlPhdModuleEntry_Object = MibTableRow
rlPhdModuleEntry = _RlPhdModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 53, 2, 1)
)
rlPhdModuleEntry.setIndexNames(
    (0, "DLINK-3100-Physicaldescription-MIB", "rlPhdModuleStackUnit"),
    (0, "DLINK-3100-Physicaldescription-MIB", "rlPhdModuleIndex"),
)
if mibBuilder.loadTexts:
    rlPhdModuleEntry.setStatus("current")
_RlPhdModuleStackUnit_Type = Integer32
_RlPhdModuleStackUnit_Object = MibTableColumn
rlPhdModuleStackUnit = _RlPhdModuleStackUnit_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 53, 2, 1, 1),
    _RlPhdModuleStackUnit_Type()
)
rlPhdModuleStackUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPhdModuleStackUnit.setStatus("current")
_RlPhdModuleIndex_Type = Integer32
_RlPhdModuleIndex_Object = MibTableColumn
rlPhdModuleIndex = _RlPhdModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 53, 2, 1, 2),
    _RlPhdModuleIndex_Type()
)
rlPhdModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPhdModuleIndex.setStatus("current")
_RlPhdModuleType_Type = Integer32
_RlPhdModuleType_Object = MibTableColumn
rlPhdModuleType = _RlPhdModuleType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 53, 2, 1, 3),
    _RlPhdModuleType_Type()
)
rlPhdModuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPhdModuleType.setStatus("current")
_RlPhdModuleStartingPort_Type = Integer32
_RlPhdModuleStartingPort_Object = MibTableColumn
rlPhdModuleStartingPort = _RlPhdModuleStartingPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 53, 2, 1, 4),
    _RlPhdModuleStartingPort_Type()
)
rlPhdModuleStartingPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPhdModuleStartingPort.setStatus("current")
_RlPhdModuleNumberOfPorts_Type = Integer32
_RlPhdModuleNumberOfPorts_Object = MibTableColumn
rlPhdModuleNumberOfPorts = _RlPhdModuleNumberOfPorts_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 53, 2, 1, 5),
    _RlPhdModuleNumberOfPorts_Type()
)
rlPhdModuleNumberOfPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPhdModuleNumberOfPorts.setStatus("current")
_RlPhdModuleRow_Type = Integer32
_RlPhdModuleRow_Object = MibTableColumn
rlPhdModuleRow = _RlPhdModuleRow_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 53, 2, 1, 6),
    _RlPhdModuleRow_Type()
)
rlPhdModuleRow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPhdModuleRow.setStatus("current")
_RlPhdModuleColumn_Type = Integer32
_RlPhdModuleColumn_Object = MibTableColumn
rlPhdModuleColumn = _RlPhdModuleColumn_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 53, 2, 1, 7),
    _RlPhdModuleColumn_Type()
)
rlPhdModuleColumn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPhdModuleColumn.setStatus("current")


class _RlPhdModuleRole_Type(Integer32):
    """Custom type rlPhdModuleRole based on Integer32"""
    defaultValue = 1

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
        *(("backup", 3),
          ("master", 2),
          ("slave", 4),
          ("standalone", 1))
    )


_RlPhdModuleRole_Type.__name__ = "Integer32"
_RlPhdModuleRole_Object = MibTableColumn
rlPhdModuleRole = _RlPhdModuleRole_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 53, 2, 1, 8),
    _RlPhdModuleRole_Type()
)
rlPhdModuleRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPhdModuleRole.setStatus("current")
_RlPhdPortsTable_Object = MibTable
rlPhdPortsTable = _RlPhdPortsTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 53, 3)
)
if mibBuilder.loadTexts:
    rlPhdPortsTable.setStatus("current")
_RlPhdPortsEntry_Object = MibTableRow
rlPhdPortsEntry = _RlPhdPortsEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 53, 3, 1)
)
rlPhdPortsEntry.setIndexNames(
    (0, "DLINK-3100-Physicaldescription-MIB", "rlPhdPortsIfIndex"),
)
if mibBuilder.loadTexts:
    rlPhdPortsEntry.setStatus("current")
_RlPhdPortsIfIndex_Type = Integer32
_RlPhdPortsIfIndex_Object = MibTableColumn
rlPhdPortsIfIndex = _RlPhdPortsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 53, 3, 1, 1),
    _RlPhdPortsIfIndex_Type()
)
rlPhdPortsIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPhdPortsIfIndex.setStatus("current")


class _RlPhdPortsIfIndexName_Type(DisplayString):
    """Custom type rlPhdPortsIfIndexName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_RlPhdPortsIfIndexName_Type.__name__ = "DisplayString"
_RlPhdPortsIfIndexName_Object = MibTableColumn
rlPhdPortsIfIndexName = _RlPhdPortsIfIndexName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 53, 3, 1, 2),
    _RlPhdPortsIfIndexName_Type()
)
rlPhdPortsIfIndexName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPhdPortsIfIndexName.setStatus("current")


class _RlPhdPortsMediaType_Type(Integer32):
    """Custom type rlPhdPortsMediaType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("combo", 3),
          ("copper", 1),
          ("optic-fiber", 2))
    )


_RlPhdPortsMediaType_Type.__name__ = "Integer32"
_RlPhdPortsMediaType_Object = MibTableColumn
rlPhdPortsMediaType = _RlPhdPortsMediaType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 53, 3, 1, 3),
    _RlPhdPortsMediaType_Type()
)
rlPhdPortsMediaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPhdPortsMediaType.setStatus("current")
_RlPhdPortsStackUnit_Type = Integer32
_RlPhdPortsStackUnit_Object = MibTableColumn
rlPhdPortsStackUnit = _RlPhdPortsStackUnit_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 53, 3, 1, 4),
    _RlPhdPortsStackUnit_Type()
)
rlPhdPortsStackUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPhdPortsStackUnit.setStatus("current")
_RlPhdPortsModuleNumber_Type = Integer32
_RlPhdPortsModuleNumber_Object = MibTableColumn
rlPhdPortsModuleNumber = _RlPhdPortsModuleNumber_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 53, 3, 1, 5),
    _RlPhdPortsModuleNumber_Type()
)
rlPhdPortsModuleNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPhdPortsModuleNumber.setStatus("current")
_RlPhdPortsRow_Type = Integer32
_RlPhdPortsRow_Object = MibTableColumn
rlPhdPortsRow = _RlPhdPortsRow_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 53, 3, 1, 6),
    _RlPhdPortsRow_Type()
)
rlPhdPortsRow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPhdPortsRow.setStatus("current")
_RlPhdPortsColumn_Type = Integer32
_RlPhdPortsColumn_Object = MibTableColumn
rlPhdPortsColumn = _RlPhdPortsColumn_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 53, 3, 1, 7),
    _RlPhdPortsColumn_Type()
)
rlPhdPortsColumn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPhdPortsColumn.setStatus("current")
_RlPhdConnectorType_Type = JackType
_RlPhdConnectorType_Object = MibTableColumn
rlPhdConnectorType = _RlPhdConnectorType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 53, 3, 1, 8),
    _RlPhdConnectorType_Type()
)
rlPhdConnectorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPhdConnectorType.setStatus("current")


class _RlPhdPortHaul_Type(Integer32):
    """Custom type rlPhdPortHaul based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("long", 3),
          ("not-relevant", 1),
          ("short", 2))
    )


_RlPhdPortHaul_Type.__name__ = "Integer32"
_RlPhdPortHaul_Object = MibTableColumn
rlPhdPortHaul = _RlPhdPortHaul_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 53, 3, 1, 9),
    _RlPhdPortHaul_Type()
)
rlPhdPortHaul.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPhdPortHaul.setStatus("current")
_RlPhdStackTable_Object = MibTable
rlPhdStackTable = _RlPhdStackTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 53, 4)
)
if mibBuilder.loadTexts:
    rlPhdStackTable.setStatus("current")
_RlPhdStackEntry_Object = MibTableRow
rlPhdStackEntry = _RlPhdStackEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 53, 4, 1)
)
rlPhdStackEntry.setIndexNames(
    (0, "DLINK-3100-Physicaldescription-MIB", "rlPhdStackUnit"),
)
if mibBuilder.loadTexts:
    rlPhdStackEntry.setStatus("current")
_RlPhdStackUnit_Type = Integer32
_RlPhdStackUnit_Object = MibTableColumn
rlPhdStackUnit = _RlPhdStackUnit_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 53, 4, 1, 1),
    _RlPhdStackUnit_Type()
)
rlPhdStackUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPhdStackUnit.setStatus("current")
_RlPhdStackType_Type = Integer32
_RlPhdStackType_Object = MibTableColumn
rlPhdStackType = _RlPhdStackType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 53, 4, 1, 2),
    _RlPhdStackType_Type()
)
rlPhdStackType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPhdStackType.setStatus("current")


class _RlPhdStackConnect1_Type(Integer32):
    """Custom type rlPhdStackConnect1 based on Integer32"""
    defaultValue = 0


_RlPhdStackConnect1_Object = MibTableColumn
rlPhdStackConnect1 = _RlPhdStackConnect1_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 53, 4, 1, 3),
    _RlPhdStackConnect1_Type()
)
rlPhdStackConnect1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPhdStackConnect1.setStatus("current")


class _RlPhdStackConnect2_Type(Integer32):
    """Custom type rlPhdStackConnect2 based on Integer32"""
    defaultValue = 0


_RlPhdStackConnect2_Object = MibTableColumn
rlPhdStackConnect2 = _RlPhdStackConnect2_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 53, 4, 1, 4),
    _RlPhdStackConnect2_Type()
)
rlPhdStackConnect2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPhdStackConnect2.setStatus("current")


class _RlPhdStackSofrwareVer_Type(DisplayString):
    """Custom type rlPhdStackSofrwareVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_RlPhdStackSofrwareVer_Type.__name__ = "DisplayString"
_RlPhdStackSofrwareVer_Object = MibTableColumn
rlPhdStackSofrwareVer = _RlPhdStackSofrwareVer_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 53, 4, 1, 5),
    _RlPhdStackSofrwareVer_Type()
)
rlPhdStackSofrwareVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPhdStackSofrwareVer.setStatus("current")


class _RlPhdStackProductID_Type(DisplayString):
    """Custom type rlPhdStackProductID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_RlPhdStackProductID_Type.__name__ = "DisplayString"
_RlPhdStackProductID_Object = MibTableColumn
rlPhdStackProductID = _RlPhdStackProductID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 53, 4, 1, 6),
    _RlPhdStackProductID_Type()
)
rlPhdStackProductID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPhdStackProductID.setStatus("current")
_RlPhdStackMacAddr_Type = PhysAddress
_RlPhdStackMacAddr_Object = MibTableColumn
rlPhdStackMacAddr = _RlPhdStackMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 53, 4, 1, 7),
    _RlPhdStackMacAddr_Type()
)
rlPhdStackMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPhdStackMacAddr.setStatus("current")
_RlPhdModuleHotSwapTable_Object = MibTable
rlPhdModuleHotSwapTable = _RlPhdModuleHotSwapTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 53, 5)
)
if mibBuilder.loadTexts:
    rlPhdModuleHotSwapTable.setStatus("current")
_RlPhdModuleHotSwapEntry_Object = MibTableRow
rlPhdModuleHotSwapEntry = _RlPhdModuleHotSwapEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 53, 5, 1)
)
rlPhdModuleHotSwapEntry.setIndexNames(
    (0, "DLINK-3100-Physicaldescription-MIB", "rlPhdModuleStackUnit"),
    (0, "DLINK-3100-Physicaldescription-MIB", "rlPhdModuleIndex"),
)
if mibBuilder.loadTexts:
    rlPhdModuleHotSwapEntry.setStatus("current")


class _RlPhdModuleHotSwapAdminStatus_Type(Integer32):
    """Custom type rlPhdModuleHotSwapAdminStatus based on Integer32"""
    defaultValue = 1

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


_RlPhdModuleHotSwapAdminStatus_Type.__name__ = "Integer32"
_RlPhdModuleHotSwapAdminStatus_Object = MibTableColumn
rlPhdModuleHotSwapAdminStatus = _RlPhdModuleHotSwapAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 53, 5, 1, 1),
    _RlPhdModuleHotSwapAdminStatus_Type()
)
rlPhdModuleHotSwapAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPhdModuleHotSwapAdminStatus.setStatus("current")


class _RlPhdModuleHotSwapOperStatus_Type(Integer32):
    """Custom type rlPhdModuleHotSwapOperStatus based on Integer32"""
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


_RlPhdModuleHotSwapOperStatus_Type.__name__ = "Integer32"
_RlPhdModuleHotSwapOperStatus_Object = MibTableColumn
rlPhdModuleHotSwapOperStatus = _RlPhdModuleHotSwapOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 53, 5, 1, 2),
    _RlPhdModuleHotSwapOperStatus_Type()
)
rlPhdModuleHotSwapOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPhdModuleHotSwapOperStatus.setStatus("current")
_RlPhdStackOrderTable_Object = MibTable
rlPhdStackOrderTable = _RlPhdStackOrderTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 53, 6)
)
if mibBuilder.loadTexts:
    rlPhdStackOrderTable.setStatus("current")
_RlPhdStackOrderEntry_Object = MibTableRow
rlPhdStackOrderEntry = _RlPhdStackOrderEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 53, 6, 1)
)
rlPhdStackOrderEntry.setIndexNames(
    (0, "DLINK-3100-Physicaldescription-MIB", "rlPhdStackOrderCurrentUnitPosition"),
)
if mibBuilder.loadTexts:
    rlPhdStackOrderEntry.setStatus("current")
_RlPhdStackOrderCurrentUnitPosition_Type = Integer32
_RlPhdStackOrderCurrentUnitPosition_Object = MibTableColumn
rlPhdStackOrderCurrentUnitPosition = _RlPhdStackOrderCurrentUnitPosition_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 53, 6, 1, 1),
    _RlPhdStackOrderCurrentUnitPosition_Type()
)
rlPhdStackOrderCurrentUnitPosition.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlPhdStackOrderCurrentUnitPosition.setStatus("current")
_RlPhdStackOrderDesiredUnitPosition_Type = Integer32
_RlPhdStackOrderDesiredUnitPosition_Object = MibTableColumn
rlPhdStackOrderDesiredUnitPosition = _RlPhdStackOrderDesiredUnitPosition_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 53, 6, 1, 2),
    _RlPhdStackOrderDesiredUnitPosition_Type()
)
rlPhdStackOrderDesiredUnitPosition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPhdStackOrderDesiredUnitPosition.setStatus("current")
_RlPhdStackOrderUnitIndex_Type = Integer32
_RlPhdStackOrderUnitIndex_Object = MibTableColumn
rlPhdStackOrderUnitIndex = _RlPhdStackOrderUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 53, 6, 1, 3),
    _RlPhdStackOrderUnitIndex_Type()
)
rlPhdStackOrderUnitIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlPhdStackOrderUnitIndex.setStatus("current")
_RlPhdStackOrderUnitType_Type = Integer32
_RlPhdStackOrderUnitType_Object = MibTableColumn
rlPhdStackOrderUnitType = _RlPhdStackOrderUnitType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 53, 6, 1, 4),
    _RlPhdStackOrderUnitType_Type()
)
rlPhdStackOrderUnitType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPhdStackOrderUnitType.setStatus("current")


class _RlPhdStackReorder_Type(Integer32):
    """Custom type rlPhdStackReorder based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reorder", 1)
    )


_RlPhdStackReorder_Type.__name__ = "Integer32"
_RlPhdStackReorder_Object = MibScalar
rlPhdStackReorder = _RlPhdStackReorder_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 53, 7),
    _RlPhdStackReorder_Type()
)
rlPhdStackReorder.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPhdStackReorder.setStatus("current")
_RlPhdNumberOfUnits_Type = Integer32
_RlPhdNumberOfUnits_Object = MibScalar
rlPhdNumberOfUnits = _RlPhdNumberOfUnits_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 53, 8),
    _RlPhdNumberOfUnits_Type()
)
rlPhdNumberOfUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPhdNumberOfUnits.setStatus("current")
_RlPhdMaxNumberOfUnits_Type = Integer32
_RlPhdMaxNumberOfUnits_Object = MibScalar
rlPhdMaxNumberOfUnits = _RlPhdMaxNumberOfUnits_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 53, 9),
    _RlPhdMaxNumberOfUnits_Type()
)
rlPhdMaxNumberOfUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPhdMaxNumberOfUnits.setStatus("current")
_RlPhdForceMasterUnit_Type = Integer32
_RlPhdForceMasterUnit_Object = MibScalar
rlPhdForceMasterUnit = _RlPhdForceMasterUnit_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 53, 10),
    _RlPhdForceMasterUnit_Type()
)
rlPhdForceMasterUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPhdForceMasterUnit.setStatus("current")
_RlPhdStackFixedUnit_Type = Integer32
_RlPhdStackFixedUnit_Object = MibScalar
rlPhdStackFixedUnit = _RlPhdStackFixedUnit_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 53, 11),
    _RlPhdStackFixedUnit_Type()
)
rlPhdStackFixedUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPhdStackFixedUnit.setStatus("current")


class _RlPhdStackFixedUnitLocation_Type(Integer32):
    """Custom type rlPhdStackFixedUnitLocation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bottom", 1),
          ("top", 2))
    )


_RlPhdStackFixedUnitLocation_Type.__name__ = "Integer32"
_RlPhdStackFixedUnitLocation_Object = MibScalar
rlPhdStackFixedUnitLocation = _RlPhdStackFixedUnitLocation_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 53, 12),
    _RlPhdStackFixedUnitLocation_Type()
)
rlPhdStackFixedUnitLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPhdStackFixedUnitLocation.setStatus("current")
_RlPhdStackReloadUnit_Type = Integer32
_RlPhdStackReloadUnit_Object = MibScalar
rlPhdStackReloadUnit = _RlPhdStackReloadUnit_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 53, 13),
    _RlPhdStackReloadUnit_Type()
)
rlPhdStackReloadUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPhdStackReloadUnit.setStatus("current")
_RlPhdUnitGenParamTable_Object = MibTable
rlPhdUnitGenParamTable = _RlPhdUnitGenParamTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 53, 14)
)
if mibBuilder.loadTexts:
    rlPhdUnitGenParamTable.setStatus("current")
_RlPhdUnitGenParamEntry_Object = MibTableRow
rlPhdUnitGenParamEntry = _RlPhdUnitGenParamEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 53, 14, 1)
)
rlPhdUnitGenParamEntry.setIndexNames(
    (0, "DLINK-3100-Physicaldescription-MIB", "rlPhdUnitGenParamStackUnit"),
)
if mibBuilder.loadTexts:
    rlPhdUnitGenParamEntry.setStatus("current")
_RlPhdUnitGenParamStackUnit_Type = Integer32
_RlPhdUnitGenParamStackUnit_Object = MibTableColumn
rlPhdUnitGenParamStackUnit = _RlPhdUnitGenParamStackUnit_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 53, 14, 1, 1),
    _RlPhdUnitGenParamStackUnit_Type()
)
rlPhdUnitGenParamStackUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPhdUnitGenParamStackUnit.setStatus("current")
_RlPhdUnitGenParamSoftwareVersion_Type = DisplayString
_RlPhdUnitGenParamSoftwareVersion_Object = MibTableColumn
rlPhdUnitGenParamSoftwareVersion = _RlPhdUnitGenParamSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 53, 14, 1, 2),
    _RlPhdUnitGenParamSoftwareVersion_Type()
)
rlPhdUnitGenParamSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPhdUnitGenParamSoftwareVersion.setStatus("current")
_RlPhdUnitGenParamFirmwareVersion_Type = DisplayString
_RlPhdUnitGenParamFirmwareVersion_Object = MibTableColumn
rlPhdUnitGenParamFirmwareVersion = _RlPhdUnitGenParamFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 53, 14, 1, 3),
    _RlPhdUnitGenParamFirmwareVersion_Type()
)
rlPhdUnitGenParamFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPhdUnitGenParamFirmwareVersion.setStatus("current")
_RlPhdUnitGenParamHardwareVersion_Type = DisplayString
_RlPhdUnitGenParamHardwareVersion_Object = MibTableColumn
rlPhdUnitGenParamHardwareVersion = _RlPhdUnitGenParamHardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 53, 14, 1, 4),
    _RlPhdUnitGenParamHardwareVersion_Type()
)
rlPhdUnitGenParamHardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPhdUnitGenParamHardwareVersion.setStatus("current")
_RlPhdUnitGenParamSerialNum_Type = DisplayString
_RlPhdUnitGenParamSerialNum_Object = MibTableColumn
rlPhdUnitGenParamSerialNum = _RlPhdUnitGenParamSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 53, 14, 1, 5),
    _RlPhdUnitGenParamSerialNum_Type()
)
rlPhdUnitGenParamSerialNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPhdUnitGenParamSerialNum.setStatus("current")
_RlPhdUnitGenParamAssetTag_Type = DisplayString
_RlPhdUnitGenParamAssetTag_Object = MibTableColumn
rlPhdUnitGenParamAssetTag = _RlPhdUnitGenParamAssetTag_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 53, 14, 1, 6),
    _RlPhdUnitGenParamAssetTag_Type()
)
rlPhdUnitGenParamAssetTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPhdUnitGenParamAssetTag.setStatus("current")
_RlPhdUnitGenParamServiceTag_Type = DisplayString
_RlPhdUnitGenParamServiceTag_Object = MibTableColumn
rlPhdUnitGenParamServiceTag = _RlPhdUnitGenParamServiceTag_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 53, 14, 1, 7),
    _RlPhdUnitGenParamServiceTag_Type()
)
rlPhdUnitGenParamServiceTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPhdUnitGenParamServiceTag.setStatus("current")
_RlPhdUnitGenParamSoftwareDate_Type = DisplayString
_RlPhdUnitGenParamSoftwareDate_Object = MibTableColumn
rlPhdUnitGenParamSoftwareDate = _RlPhdUnitGenParamSoftwareDate_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 53, 14, 1, 8),
    _RlPhdUnitGenParamSoftwareDate_Type()
)
rlPhdUnitGenParamSoftwareDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPhdUnitGenParamSoftwareDate.setStatus("current")
_RlPhdUnitGenParamFirmwareDate_Type = DisplayString
_RlPhdUnitGenParamFirmwareDate_Object = MibTableColumn
rlPhdUnitGenParamFirmwareDate = _RlPhdUnitGenParamFirmwareDate_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 53, 14, 1, 9),
    _RlPhdUnitGenParamFirmwareDate_Type()
)
rlPhdUnitGenParamFirmwareDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPhdUnitGenParamFirmwareDate.setStatus("current")
_RlPhdUnitGenParamManufacturer_Type = DisplayString
_RlPhdUnitGenParamManufacturer_Object = MibTableColumn
rlPhdUnitGenParamManufacturer = _RlPhdUnitGenParamManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 53, 14, 1, 10),
    _RlPhdUnitGenParamManufacturer_Type()
)
rlPhdUnitGenParamManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPhdUnitGenParamManufacturer.setStatus("current")
_RlPhdUnitGenParamModelName_Type = DisplayString
_RlPhdUnitGenParamModelName_Object = MibTableColumn
rlPhdUnitGenParamModelName = _RlPhdUnitGenParamModelName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 53, 14, 1, 11),
    _RlPhdUnitGenParamModelName_Type()
)
rlPhdUnitGenParamModelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPhdUnitGenParamModelName.setStatus("current")
_RlPhdUnitEnvParamTable_Object = MibTable
rlPhdUnitEnvParamTable = _RlPhdUnitEnvParamTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 53, 15)
)
if mibBuilder.loadTexts:
    rlPhdUnitEnvParamTable.setStatus("current")
_RlPhdUnitEnvParamEntry_Object = MibTableRow
rlPhdUnitEnvParamEntry = _RlPhdUnitEnvParamEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 53, 15, 1)
)
rlPhdUnitEnvParamEntry.setIndexNames(
    (0, "DLINK-3100-Physicaldescription-MIB", "rlPhdUnitEnvParamStackUnit"),
)
if mibBuilder.loadTexts:
    rlPhdUnitEnvParamEntry.setStatus("current")
_RlPhdUnitEnvParamStackUnit_Type = Integer32
_RlPhdUnitEnvParamStackUnit_Object = MibTableColumn
rlPhdUnitEnvParamStackUnit = _RlPhdUnitEnvParamStackUnit_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 53, 15, 1, 1),
    _RlPhdUnitEnvParamStackUnit_Type()
)
rlPhdUnitEnvParamStackUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPhdUnitEnvParamStackUnit.setStatus("current")
_RlPhdUnitEnvParamMainPSStatus_Type = RlEnvMonState
_RlPhdUnitEnvParamMainPSStatus_Object = MibTableColumn
rlPhdUnitEnvParamMainPSStatus = _RlPhdUnitEnvParamMainPSStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 53, 15, 1, 2),
    _RlPhdUnitEnvParamMainPSStatus_Type()
)
rlPhdUnitEnvParamMainPSStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPhdUnitEnvParamMainPSStatus.setStatus("current")
_RlPhdUnitEnvParamRedundantPSStatus_Type = RlEnvMonState
_RlPhdUnitEnvParamRedundantPSStatus_Object = MibTableColumn
rlPhdUnitEnvParamRedundantPSStatus = _RlPhdUnitEnvParamRedundantPSStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 53, 15, 1, 3),
    _RlPhdUnitEnvParamRedundantPSStatus_Type()
)
rlPhdUnitEnvParamRedundantPSStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPhdUnitEnvParamRedundantPSStatus.setStatus("current")
_RlPhdUnitEnvParamFan1Status_Type = RlEnvMonState
_RlPhdUnitEnvParamFan1Status_Object = MibTableColumn
rlPhdUnitEnvParamFan1Status = _RlPhdUnitEnvParamFan1Status_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 53, 15, 1, 4),
    _RlPhdUnitEnvParamFan1Status_Type()
)
rlPhdUnitEnvParamFan1Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPhdUnitEnvParamFan1Status.setStatus("current")
_RlPhdUnitEnvParamFan2Status_Type = RlEnvMonState
_RlPhdUnitEnvParamFan2Status_Object = MibTableColumn
rlPhdUnitEnvParamFan2Status = _RlPhdUnitEnvParamFan2Status_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 53, 15, 1, 5),
    _RlPhdUnitEnvParamFan2Status_Type()
)
rlPhdUnitEnvParamFan2Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPhdUnitEnvParamFan2Status.setStatus("current")
_RlPhdUnitEnvParamFan3Status_Type = RlEnvMonState
_RlPhdUnitEnvParamFan3Status_Object = MibTableColumn
rlPhdUnitEnvParamFan3Status = _RlPhdUnitEnvParamFan3Status_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 53, 15, 1, 6),
    _RlPhdUnitEnvParamFan3Status_Type()
)
rlPhdUnitEnvParamFan3Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPhdUnitEnvParamFan3Status.setStatus("current")
_RlPhdUnitEnvParamFan4Status_Type = RlEnvMonState
_RlPhdUnitEnvParamFan4Status_Object = MibTableColumn
rlPhdUnitEnvParamFan4Status = _RlPhdUnitEnvParamFan4Status_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 53, 15, 1, 7),
    _RlPhdUnitEnvParamFan4Status_Type()
)
rlPhdUnitEnvParamFan4Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPhdUnitEnvParamFan4Status.setStatus("current")
_RlPhdUnitEnvParamFan5Status_Type = RlEnvMonState
_RlPhdUnitEnvParamFan5Status_Object = MibTableColumn
rlPhdUnitEnvParamFan5Status = _RlPhdUnitEnvParamFan5Status_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 53, 15, 1, 8),
    _RlPhdUnitEnvParamFan5Status_Type()
)
rlPhdUnitEnvParamFan5Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPhdUnitEnvParamFan5Status.setStatus("current")
_RlPhdUnitEnvParamTempSensorValue_Type = EntitySensorValue
_RlPhdUnitEnvParamTempSensorValue_Object = MibTableColumn
rlPhdUnitEnvParamTempSensorValue = _RlPhdUnitEnvParamTempSensorValue_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 53, 15, 1, 9),
    _RlPhdUnitEnvParamTempSensorValue_Type()
)
rlPhdUnitEnvParamTempSensorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPhdUnitEnvParamTempSensorValue.setStatus("current")
_RlPhdUnitEnvParamTempSensorStatus_Type = EntitySensorStatus
_RlPhdUnitEnvParamTempSensorStatus_Object = MibTableColumn
rlPhdUnitEnvParamTempSensorStatus = _RlPhdUnitEnvParamTempSensorStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 53, 15, 1, 10),
    _RlPhdUnitEnvParamTempSensorStatus_Type()
)
rlPhdUnitEnvParamTempSensorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPhdUnitEnvParamTempSensorStatus.setStatus("current")
_RlPhdUnitEnvParamUpTime_Type = TimeTicks
_RlPhdUnitEnvParamUpTime_Object = MibTableColumn
rlPhdUnitEnvParamUpTime = _RlPhdUnitEnvParamUpTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 53, 15, 1, 11),
    _RlPhdUnitEnvParamUpTime_Type()
)
rlPhdUnitEnvParamUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPhdUnitEnvParamUpTime.setStatus("current")
_RlPhdStackOrderTopUnit_Type = Integer32
_RlPhdStackOrderTopUnit_Object = MibScalar
rlPhdStackOrderTopUnit = _RlPhdStackOrderTopUnit_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 53, 16),
    _RlPhdStackOrderTopUnit_Type()
)
rlPhdStackOrderTopUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPhdStackOrderTopUnit.setStatus("current")
_RlPhdStackOrderBottomUnit_Type = Integer32
_RlPhdStackOrderBottomUnit_Object = MibScalar
rlPhdStackOrderBottomUnit = _RlPhdStackOrderBottomUnit_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 53, 17),
    _RlPhdStackOrderBottomUnit_Type()
)
rlPhdStackOrderBottomUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPhdStackOrderBottomUnit.setStatus("current")


class _RlPhdStackOrderPermutation_Type(OctetString):
    """Custom type rlPhdStackOrderPermutation based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RlPhdStackOrderPermutation_Type.__name__ = "OctetString"
_RlPhdStackOrderPermutation_Object = MibScalar
rlPhdStackOrderPermutation = _RlPhdStackOrderPermutation_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 53, 18),
    _RlPhdStackOrderPermutation_Type()
)
rlPhdStackOrderPermutation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPhdStackOrderPermutation.setStatus("current")
_RlPhdNumberOfPoeUnits_Type = Integer32
_RlPhdNumberOfPoeUnits_Object = MibScalar
rlPhdNumberOfPoeUnits = _RlPhdNumberOfPoeUnits_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 53, 19),
    _RlPhdNumberOfPoeUnits_Type()
)
rlPhdNumberOfPoeUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPhdNumberOfPoeUnits.setStatus("current")
_RlPhdPoeTable_Object = MibTable
rlPhdPoeTable = _RlPhdPoeTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 53, 20)
)
if mibBuilder.loadTexts:
    rlPhdPoeTable.setStatus("current")
_RlPhdPoeEntry_Object = MibTableRow
rlPhdPoeEntry = _RlPhdPoeEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 53, 20, 1)
)
rlPhdPoeEntry.setIndexNames(
    (0, "DLINK-3100-Physicaldescription-MIB", "rlPhdPoeStackUnit"),
)
if mibBuilder.loadTexts:
    rlPhdPoeEntry.setStatus("current")
_RlPhdPoeStackUnit_Type = Integer32
_RlPhdPoeStackUnit_Object = MibTableColumn
rlPhdPoeStackUnit = _RlPhdPoeStackUnit_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 53, 20, 1, 1),
    _RlPhdPoeStackUnit_Type()
)
rlPhdPoeStackUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPhdPoeStackUnit.setStatus("current")


class _RlPhdPoePresent_Type(Integer32):
    """Custom type rlPhdPoePresent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_RlPhdPoePresent_Type.__name__ = "Integer32"
_RlPhdPoePresent_Object = MibTableColumn
rlPhdPoePresent = _RlPhdPoePresent_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 53, 20, 1, 2),
    _RlPhdPoePresent_Type()
)
rlPhdPoePresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPhdPoePresent.setStatus("current")
_RlPhdPhyLedStackUnit_Type = Integer32
_RlPhdPhyLedStackUnit_Object = MibScalar
rlPhdPhyLedStackUnit = _RlPhdPhyLedStackUnit_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 53, 21),
    _RlPhdPhyLedStackUnit_Type()
)
rlPhdPhyLedStackUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPhdPhyLedStackUnit.setStatus("current")
_RlPhdPhyLedTimeout_Type = Integer32
_RlPhdPhyLedTimeout_Object = MibScalar
rlPhdPhyLedTimeout = _RlPhdPhyLedTimeout_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 53, 22),
    _RlPhdPhyLedTimeout_Type()
)
rlPhdPhyLedTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPhdPhyLedTimeout.setStatus("current")
_RlCascadeTable_Object = MibTable
rlCascadeTable = _RlCascadeTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 53, 23)
)
if mibBuilder.loadTexts:
    rlCascadeTable.setStatus("current")
_RlCascadeEntry_Object = MibTableRow
rlCascadeEntry = _RlCascadeEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 53, 23, 1)
)
rlCascadeEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    rlCascadeEntry.setStatus("current")
_RlCascadeNeighborIfIndex_Type = InterfaceIndexOrZero
_RlCascadeNeighborIfIndex_Object = MibTableColumn
rlCascadeNeighborIfIndex = _RlCascadeNeighborIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 53, 23, 1, 1),
    _RlCascadeNeighborIfIndex_Type()
)
rlCascadeNeighborIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlCascadeNeighborIfIndex.setStatus("current")
_RlCascadeNeighborUnit_Type = Integer32
_RlCascadeNeighborUnit_Object = MibTableColumn
rlCascadeNeighborUnit = _RlCascadeNeighborUnit_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 53, 23, 1, 2),
    _RlCascadeNeighborUnit_Type()
)
rlCascadeNeighborUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlCascadeNeighborUnit.setStatus("current")
_RlCascadeTrunkId_Type = Integer32
_RlCascadeTrunkId_Object = MibTableColumn
rlCascadeTrunkId = _RlCascadeTrunkId_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 53, 23, 1, 3),
    _RlCascadeTrunkId_Type()
)
rlCascadeTrunkId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlCascadeTrunkId.setStatus("current")
_RlCascadeUnitId_Type = Integer32
_RlCascadeUnitId_Object = MibTableColumn
rlCascadeUnitId = _RlCascadeUnitId_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 53, 23, 1, 4),
    _RlCascadeUnitId_Type()
)
rlCascadeUnitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlCascadeUnitId.setStatus("current")
_RlCascadeAfterResetTable_Object = MibTable
rlCascadeAfterResetTable = _RlCascadeAfterResetTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 53, 24)
)
if mibBuilder.loadTexts:
    rlCascadeAfterResetTable.setStatus("current")
_RlCascadeAfterResetEntry_Object = MibTableRow
rlCascadeAfterResetEntry = _RlCascadeAfterResetEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 53, 24, 1)
)
rlCascadeAfterResetEntry.setIndexNames(
    (0, "DLINK-3100-Physicaldescription-MIB", "rlCascadeIfIndexAfterReset"),
)
if mibBuilder.loadTexts:
    rlCascadeAfterResetEntry.setStatus("current")
_RlCascadeIfIndexAfterReset_Type = InterfaceIndex
_RlCascadeIfIndexAfterReset_Object = MibTableColumn
rlCascadeIfIndexAfterReset = _RlCascadeIfIndexAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 53, 24, 1, 1),
    _RlCascadeIfIndexAfterReset_Type()
)
rlCascadeIfIndexAfterReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlCascadeIfIndexAfterReset.setStatus("current")
_RlCascadeTrunkIdAfterReset_Type = Integer32
_RlCascadeTrunkIdAfterReset_Object = MibTableColumn
rlCascadeTrunkIdAfterReset = _RlCascadeTrunkIdAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 53, 24, 1, 2),
    _RlCascadeTrunkIdAfterReset_Type()
)
rlCascadeTrunkIdAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlCascadeTrunkIdAfterReset.setStatus("current")
_RlCascadeRowStatus_Type = RowStatus
_RlCascadeRowStatus_Object = MibTableColumn
rlCascadeRowStatus = _RlCascadeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 53, 24, 1, 3),
    _RlCascadeRowStatus_Type()
)
rlCascadeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlCascadeRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects

rlStackUnitRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 0, 186)
)
rlStackUnitRemoved.setObjects(
      *(("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorDesc"),
        ("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rlStackUnitRemoved.setStatus(
        "current"
    )

rlStackConfigChangedRingChain = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 0, 187)
)
rlStackConfigChangedRingChain.setObjects(
      *(("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorDesc"),
        ("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rlStackConfigChangedRingChain.setStatus(
        "current"
    )

rlStackBackupUnitRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 0, 188)
)
rlStackBackupUnitRemoved.setObjects(
      *(("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorDesc"),
        ("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rlStackBackupUnitRemoved.setStatus(
        "current"
    )

rlStackMasterSwitchover = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 0, 189)
)
rlStackMasterSwitchover.setObjects(
      *(("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorDesc"),
        ("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rlStackMasterSwitchover.setStatus(
        "current"
    )

rlStackUnitDifferentSwVersion = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 0, 190)
)
rlStackUnitDifferentSwVersion.setObjects(
      *(("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorDesc"),
        ("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rlStackUnitDifferentSwVersion.setStatus(
        "current"
    )

rlStackDuplicateUnitNotJoin = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 0, 191)
)
rlStackDuplicateUnitNotJoin.setObjects(
      *(("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorDesc"),
        ("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rlStackDuplicateUnitNotJoin.setStatus(
        "current"
    )

rlStackLinkChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 0, 195)
)
rlStackLinkChange.setObjects(
      *(("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorDesc"),
        ("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rlStackLinkChange.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DLINK-3100-Physicaldescription-MIB",
    **{"rlStackUnitRemoved": rlStackUnitRemoved,
       "rlStackConfigChangedRingChain": rlStackConfigChangedRingChain,
       "rlStackBackupUnitRemoved": rlStackBackupUnitRemoved,
       "rlStackMasterSwitchover": rlStackMasterSwitchover,
       "rlStackUnitDifferentSwVersion": rlStackUnitDifferentSwVersion,
       "rlStackDuplicateUnitNotJoin": rlStackDuplicateUnitNotJoin,
       "rlStackLinkChange": rlStackLinkChange,
       "rlPhysicalDescription": rlPhysicalDescription,
       "rlPhdMibVersion": rlPhdMibVersion,
       "rlPhdModuleTable": rlPhdModuleTable,
       "rlPhdModuleEntry": rlPhdModuleEntry,
       "rlPhdModuleStackUnit": rlPhdModuleStackUnit,
       "rlPhdModuleIndex": rlPhdModuleIndex,
       "rlPhdModuleType": rlPhdModuleType,
       "rlPhdModuleStartingPort": rlPhdModuleStartingPort,
       "rlPhdModuleNumberOfPorts": rlPhdModuleNumberOfPorts,
       "rlPhdModuleRow": rlPhdModuleRow,
       "rlPhdModuleColumn": rlPhdModuleColumn,
       "rlPhdModuleRole": rlPhdModuleRole,
       "rlPhdPortsTable": rlPhdPortsTable,
       "rlPhdPortsEntry": rlPhdPortsEntry,
       "rlPhdPortsIfIndex": rlPhdPortsIfIndex,
       "rlPhdPortsIfIndexName": rlPhdPortsIfIndexName,
       "rlPhdPortsMediaType": rlPhdPortsMediaType,
       "rlPhdPortsStackUnit": rlPhdPortsStackUnit,
       "rlPhdPortsModuleNumber": rlPhdPortsModuleNumber,
       "rlPhdPortsRow": rlPhdPortsRow,
       "rlPhdPortsColumn": rlPhdPortsColumn,
       "rlPhdConnectorType": rlPhdConnectorType,
       "rlPhdPortHaul": rlPhdPortHaul,
       "rlPhdStackTable": rlPhdStackTable,
       "rlPhdStackEntry": rlPhdStackEntry,
       "rlPhdStackUnit": rlPhdStackUnit,
       "rlPhdStackType": rlPhdStackType,
       "rlPhdStackConnect1": rlPhdStackConnect1,
       "rlPhdStackConnect2": rlPhdStackConnect2,
       "rlPhdStackSofrwareVer": rlPhdStackSofrwareVer,
       "rlPhdStackProductID": rlPhdStackProductID,
       "rlPhdStackMacAddr": rlPhdStackMacAddr,
       "rlPhdModuleHotSwapTable": rlPhdModuleHotSwapTable,
       "rlPhdModuleHotSwapEntry": rlPhdModuleHotSwapEntry,
       "rlPhdModuleHotSwapAdminStatus": rlPhdModuleHotSwapAdminStatus,
       "rlPhdModuleHotSwapOperStatus": rlPhdModuleHotSwapOperStatus,
       "rlPhdStackOrderTable": rlPhdStackOrderTable,
       "rlPhdStackOrderEntry": rlPhdStackOrderEntry,
       "rlPhdStackOrderCurrentUnitPosition": rlPhdStackOrderCurrentUnitPosition,
       "rlPhdStackOrderDesiredUnitPosition": rlPhdStackOrderDesiredUnitPosition,
       "rlPhdStackOrderUnitIndex": rlPhdStackOrderUnitIndex,
       "rlPhdStackOrderUnitType": rlPhdStackOrderUnitType,
       "rlPhdStackReorder": rlPhdStackReorder,
       "rlPhdNumberOfUnits": rlPhdNumberOfUnits,
       "rlPhdMaxNumberOfUnits": rlPhdMaxNumberOfUnits,
       "rlPhdForceMasterUnit": rlPhdForceMasterUnit,
       "rlPhdStackFixedUnit": rlPhdStackFixedUnit,
       "rlPhdStackFixedUnitLocation": rlPhdStackFixedUnitLocation,
       "rlPhdStackReloadUnit": rlPhdStackReloadUnit,
       "rlPhdUnitGenParamTable": rlPhdUnitGenParamTable,
       "rlPhdUnitGenParamEntry": rlPhdUnitGenParamEntry,
       "rlPhdUnitGenParamStackUnit": rlPhdUnitGenParamStackUnit,
       "rlPhdUnitGenParamSoftwareVersion": rlPhdUnitGenParamSoftwareVersion,
       "rlPhdUnitGenParamFirmwareVersion": rlPhdUnitGenParamFirmwareVersion,
       "rlPhdUnitGenParamHardwareVersion": rlPhdUnitGenParamHardwareVersion,
       "rlPhdUnitGenParamSerialNum": rlPhdUnitGenParamSerialNum,
       "rlPhdUnitGenParamAssetTag": rlPhdUnitGenParamAssetTag,
       "rlPhdUnitGenParamServiceTag": rlPhdUnitGenParamServiceTag,
       "rlPhdUnitGenParamSoftwareDate": rlPhdUnitGenParamSoftwareDate,
       "rlPhdUnitGenParamFirmwareDate": rlPhdUnitGenParamFirmwareDate,
       "rlPhdUnitGenParamManufacturer": rlPhdUnitGenParamManufacturer,
       "rlPhdUnitGenParamModelName": rlPhdUnitGenParamModelName,
       "rlPhdUnitEnvParamTable": rlPhdUnitEnvParamTable,
       "rlPhdUnitEnvParamEntry": rlPhdUnitEnvParamEntry,
       "rlPhdUnitEnvParamStackUnit": rlPhdUnitEnvParamStackUnit,
       "rlPhdUnitEnvParamMainPSStatus": rlPhdUnitEnvParamMainPSStatus,
       "rlPhdUnitEnvParamRedundantPSStatus": rlPhdUnitEnvParamRedundantPSStatus,
       "rlPhdUnitEnvParamFan1Status": rlPhdUnitEnvParamFan1Status,
       "rlPhdUnitEnvParamFan2Status": rlPhdUnitEnvParamFan2Status,
       "rlPhdUnitEnvParamFan3Status": rlPhdUnitEnvParamFan3Status,
       "rlPhdUnitEnvParamFan4Status": rlPhdUnitEnvParamFan4Status,
       "rlPhdUnitEnvParamFan5Status": rlPhdUnitEnvParamFan5Status,
       "rlPhdUnitEnvParamTempSensorValue": rlPhdUnitEnvParamTempSensorValue,
       "rlPhdUnitEnvParamTempSensorStatus": rlPhdUnitEnvParamTempSensorStatus,
       "rlPhdUnitEnvParamUpTime": rlPhdUnitEnvParamUpTime,
       "rlPhdStackOrderTopUnit": rlPhdStackOrderTopUnit,
       "rlPhdStackOrderBottomUnit": rlPhdStackOrderBottomUnit,
       "rlPhdStackOrderPermutation": rlPhdStackOrderPermutation,
       "rlPhdNumberOfPoeUnits": rlPhdNumberOfPoeUnits,
       "rlPhdPoeTable": rlPhdPoeTable,
       "rlPhdPoeEntry": rlPhdPoeEntry,
       "rlPhdPoeStackUnit": rlPhdPoeStackUnit,
       "rlPhdPoePresent": rlPhdPoePresent,
       "rlPhdPhyLedStackUnit": rlPhdPhyLedStackUnit,
       "rlPhdPhyLedTimeout": rlPhdPhyLedTimeout,
       "rlCascadeTable": rlCascadeTable,
       "rlCascadeEntry": rlCascadeEntry,
       "rlCascadeNeighborIfIndex": rlCascadeNeighborIfIndex,
       "rlCascadeNeighborUnit": rlCascadeNeighborUnit,
       "rlCascadeTrunkId": rlCascadeTrunkId,
       "rlCascadeUnitId": rlCascadeUnitId,
       "rlCascadeAfterResetTable": rlCascadeAfterResetTable,
       "rlCascadeAfterResetEntry": rlCascadeAfterResetEntry,
       "rlCascadeIfIndexAfterReset": rlCascadeIfIndexAfterReset,
       "rlCascadeTrunkIdAfterReset": rlCascadeTrunkIdAfterReset,
       "rlCascadeRowStatus": rlCascadeRowStatus}
)
