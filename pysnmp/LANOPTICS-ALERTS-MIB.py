# SNMP MIB module (LANOPTICS-ALERTS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/LANOPTICS-ALERTS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:17:12 2024
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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_LanOptics_ObjectIdentity = ObjectIdentity
lanOptics = _LanOptics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 224)
)
_Alerts_ObjectIdentity = ObjectIdentity
alerts = _Alerts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 224, 9)
)
_Alerts_mgmt_ObjectIdentity = ObjectIdentity
alerts_mgmt = _Alerts_mgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 224, 9, 2)
)


class _LanOpticsAlertsEnabled_Type(Integer32):
    """Custom type lanOpticsAlertsEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("enabled", 1)
    )


_LanOpticsAlertsEnabled_Type.__name__ = "Integer32"
_LanOpticsAlertsEnabled_Object = MibScalar
lanOpticsAlertsEnabled = _LanOpticsAlertsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 224, 9, 2, 1),
    _LanOpticsAlertsEnabled_Type()
)
lanOpticsAlertsEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanOpticsAlertsEnabled.setStatus("mandatory")
_LanOpticsMaxAlertsPerTime_Type = Integer32
_LanOpticsMaxAlertsPerTime_Object = MibScalar
lanOpticsMaxAlertsPerTime = _LanOpticsMaxAlertsPerTime_Object(
    (1, 3, 6, 1, 4, 1, 224, 9, 2, 2),
    _LanOpticsMaxAlertsPerTime_Type()
)
lanOpticsMaxAlertsPerTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanOpticsMaxAlertsPerTime.setStatus("mandatory")
_LanOpticsWindowTime_Type = TimeTicks
_LanOpticsWindowTime_Object = MibScalar
lanOpticsWindowTime = _LanOpticsWindowTime_Object(
    (1, 3, 6, 1, 4, 1, 224, 9, 2, 3),
    _LanOpticsWindowTime_Type()
)
lanOpticsWindowTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanOpticsWindowTime.setStatus("mandatory")
_LanOpticsMaxLogTableEntries_Type = Integer32
_LanOpticsMaxLogTableEntries_Object = MibScalar
lanOpticsMaxLogTableEntries = _LanOpticsMaxLogTableEntries_Object(
    (1, 3, 6, 1, 4, 1, 224, 9, 2, 4),
    _LanOpticsMaxLogTableEntries_Type()
)
lanOpticsMaxLogTableEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanOpticsMaxLogTableEntries.setStatus("mandatory")
_LanOpticsCurrentAlertId_Type = Integer32
_LanOpticsCurrentAlertId_Object = MibScalar
lanOpticsCurrentAlertId = _LanOpticsCurrentAlertId_Object(
    (1, 3, 6, 1, 4, 1, 224, 9, 2, 5),
    _LanOpticsCurrentAlertId_Type()
)
lanOpticsCurrentAlertId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanOpticsCurrentAlertId.setStatus("mandatory")
_LanOpticsAlertsRegisterTable_Object = MibTable
lanOpticsAlertsRegisterTable = _LanOpticsAlertsRegisterTable_Object(
    (1, 3, 6, 1, 4, 1, 224, 9, 2, 10)
)
if mibBuilder.loadTexts:
    lanOpticsAlertsRegisterTable.setStatus("mandatory")
_LanOpticsAlertsRegisterEntry_Object = MibTableRow
lanOpticsAlertsRegisterEntry = _LanOpticsAlertsRegisterEntry_Object(
    (1, 3, 6, 1, 4, 1, 224, 9, 2, 10, 1)
)
lanOpticsAlertsRegisterEntry.setIndexNames(
    (0, "LANOPTICS-ALERTS-MIB", "pysmiFakeCol1"),
    (0, "LANOPTICS-ALERTS-MIB", "pysmiFakeCol2"),
    (0, "LANOPTICS-ALERTS-MIB", "pysmiFakeCol3"),
    (0, "LANOPTICS-ALERTS-MIB", "pysmiFakeCol4"),
)
if mibBuilder.loadTexts:
    lanOpticsAlertsRegisterEntry.setStatus("mandatory")


class _LanOpticsAlertsRegister_Type(Integer32):
    """Custom type lanOpticsAlertsRegister based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("register", 1)
    )


_LanOpticsAlertsRegister_Type.__name__ = "Integer32"
_LanOpticsAlertsRegister_Object = MibTableColumn
lanOpticsAlertsRegister = _LanOpticsAlertsRegister_Object(
    (1, 3, 6, 1, 4, 1, 224, 9, 2, 10, 1, 1),
    _LanOpticsAlertsRegister_Type()
)
lanOpticsAlertsRegister.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanOpticsAlertsRegister.setStatus("mandatory")
_PysmiFakeCol4_Type = Integer32
_PysmiFakeCol4_Object = MibTableColumn
pysmiFakeCol4 = _PysmiFakeCol4_Object(
    (1, 3, 6, 1, 4, 1, 224, 9, 2, 10, 1, 4294967292),
    _PysmiFakeCol4_Type()
)
pysmiFakeCol4.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pysmiFakeCol4.setStatus("mandatory")
_PysmiFakeCol3_Type = Integer32
_PysmiFakeCol3_Object = MibTableColumn
pysmiFakeCol3 = _PysmiFakeCol3_Object(
    (1, 3, 6, 1, 4, 1, 224, 9, 2, 10, 1, 4294967293),
    _PysmiFakeCol3_Type()
)
pysmiFakeCol3.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pysmiFakeCol3.setStatus("mandatory")
_PysmiFakeCol2_Type = Integer32
_PysmiFakeCol2_Object = MibTableColumn
pysmiFakeCol2 = _PysmiFakeCol2_Object(
    (1, 3, 6, 1, 4, 1, 224, 9, 2, 10, 1, 4294967294),
    _PysmiFakeCol2_Type()
)
pysmiFakeCol2.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pysmiFakeCol2.setStatus("mandatory")
_PysmiFakeCol1_Type = Integer32
_PysmiFakeCol1_Object = MibTableColumn
pysmiFakeCol1 = _PysmiFakeCol1_Object(
    (1, 3, 6, 1, 4, 1, 224, 9, 2, 10, 1, 4294967295),
    _PysmiFakeCol1_Type()
)
pysmiFakeCol1.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pysmiFakeCol1.setStatus("mandatory")
_LanOpticsAlertsTable_Object = MibTable
lanOpticsAlertsTable = _LanOpticsAlertsTable_Object(
    (1, 3, 6, 1, 4, 1, 224, 9, 2, 11)
)
if mibBuilder.loadTexts:
    lanOpticsAlertsTable.setStatus("mandatory")
_LanOpticsAlertsEntry_Object = MibTableRow
lanOpticsAlertsEntry = _LanOpticsAlertsEntry_Object(
    (1, 3, 6, 1, 4, 1, 224, 9, 2, 11, 1)
)
lanOpticsAlertsEntry.setIndexNames(
    (0, "LANOPTICS-ALERTS-MIB", "lanOpticsAlertId"),
)
if mibBuilder.loadTexts:
    lanOpticsAlertsEntry.setStatus("mandatory")
_LanOpticsAlertId_Type = Integer32
_LanOpticsAlertId_Object = MibTableColumn
lanOpticsAlertId = _LanOpticsAlertId_Object(
    (1, 3, 6, 1, 4, 1, 224, 9, 2, 11, 1, 1),
    _LanOpticsAlertId_Type()
)
lanOpticsAlertId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanOpticsAlertId.setStatus("mandatory")
_LanOpticsAlertData_Type = OctetString
_LanOpticsAlertData_Object = MibTableColumn
lanOpticsAlertData = _LanOpticsAlertData_Object(
    (1, 3, 6, 1, 4, 1, 224, 9, 2, 11, 1, 2),
    _LanOpticsAlertData_Type()
)
lanOpticsAlertData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanOpticsAlertData.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LANOPTICS-ALERTS-MIB",
    **{"lanOptics": lanOptics,
       "alerts": alerts,
       "alerts-mgmt": alerts_mgmt,
       "lanOpticsAlertsEnabled": lanOpticsAlertsEnabled,
       "lanOpticsMaxAlertsPerTime": lanOpticsMaxAlertsPerTime,
       "lanOpticsWindowTime": lanOpticsWindowTime,
       "lanOpticsMaxLogTableEntries": lanOpticsMaxLogTableEntries,
       "lanOpticsCurrentAlertId": lanOpticsCurrentAlertId,
       "lanOpticsAlertsRegisterTable": lanOpticsAlertsRegisterTable,
       "lanOpticsAlertsRegisterEntry": lanOpticsAlertsRegisterEntry,
       "lanOpticsAlertsRegister": lanOpticsAlertsRegister,
       "pysmiFakeCol4": pysmiFakeCol4,
       "pysmiFakeCol3": pysmiFakeCol3,
       "pysmiFakeCol2": pysmiFakeCol2,
       "pysmiFakeCol1": pysmiFakeCol1,
       "lanOpticsAlertsTable": lanOpticsAlertsTable,
       "lanOpticsAlertsEntry": lanOpticsAlertsEntry,
       "lanOpticsAlertId": lanOpticsAlertId,
       "lanOpticsAlertData": lanOpticsAlertData}
)
