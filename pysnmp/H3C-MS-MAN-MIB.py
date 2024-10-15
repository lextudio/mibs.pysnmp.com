# SNMP MIB module (H3C-MS-MAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/H3C-MS-MAN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:51:00 2024
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

(PhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "PhysicalIndex")

(h3cSurveillanceMIB,) = mibBuilder.importSymbols(
    "HUAWEI-3COM-OID-MIB",
    "h3cSurveillanceMIB")

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

h3cMSMan = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 9, 3)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_H3cMSManMIBObjects_ObjectIdentity = ObjectIdentity
h3cMSManMIBObjects = _H3cMSManMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 9, 3, 1)
)
_H3cMSStatisticalPeriod_Type = Unsigned32
_H3cMSStatisticalPeriod_Object = MibScalar
h3cMSStatisticalPeriod = _H3cMSStatisticalPeriod_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 9, 3, 1, 1),
    _H3cMSStatisticalPeriod_Type()
)
h3cMSStatisticalPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cMSStatisticalPeriod.setStatus("current")
_H3cMSManMIBTables_ObjectIdentity = ObjectIdentity
h3cMSManMIBTables = _H3cMSManMIBTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 9, 3, 2)
)
_H3cMSForwardTable_Object = MibTable
h3cMSForwardTable = _H3cMSForwardTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 9, 3, 2, 1)
)
if mibBuilder.loadTexts:
    h3cMSForwardTable.setStatus("current")
_H3cMSForwardEntry_Object = MibTableRow
h3cMSForwardEntry = _H3cMSForwardEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 9, 3, 2, 1, 1)
)
h3cMSForwardEntry.setIndexNames(
    (0, "H3C-MS-MAN-MIB", "h3cMSForwardIndex"),
)
if mibBuilder.loadTexts:
    h3cMSForwardEntry.setStatus("current")
_H3cMSForwardIndex_Type = PhysicalIndex
_H3cMSForwardIndex_Object = MibTableColumn
h3cMSForwardIndex = _H3cMSForwardIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 9, 3, 2, 1, 1, 1),
    _H3cMSForwardIndex_Type()
)
h3cMSForwardIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cMSForwardIndex.setStatus("current")
_H3cMSForwardMaxConnection_Type = Unsigned32
_H3cMSForwardMaxConnection_Object = MibTableColumn
h3cMSForwardMaxConnection = _H3cMSForwardMaxConnection_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 9, 3, 2, 1, 1, 2),
    _H3cMSForwardMaxConnection_Type()
)
h3cMSForwardMaxConnection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cMSForwardMaxConnection.setStatus("current")
_H3cMSForwardConnectionThreshold_Type = Unsigned32
_H3cMSForwardConnectionThreshold_Object = MibTableColumn
h3cMSForwardConnectionThreshold = _H3cMSForwardConnectionThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 9, 3, 2, 1, 1, 3),
    _H3cMSForwardConnectionThreshold_Type()
)
h3cMSForwardConnectionThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cMSForwardConnectionThreshold.setStatus("current")
_H3cMSCurrentForwardConnection_Type = Unsigned32
_H3cMSCurrentForwardConnection_Object = MibTableColumn
h3cMSCurrentForwardConnection = _H3cMSCurrentForwardConnection_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 9, 3, 2, 1, 1, 4),
    _H3cMSCurrentForwardConnection_Type()
)
h3cMSCurrentForwardConnection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cMSCurrentForwardConnection.setStatus("current")
_H3cMSPeriodForwardConnection_Type = Unsigned32
_H3cMSPeriodForwardConnection_Object = MibTableColumn
h3cMSPeriodForwardConnection = _H3cMSPeriodForwardConnection_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 9, 3, 2, 1, 1, 5),
    _H3cMSPeriodForwardConnection_Type()
)
h3cMSPeriodForwardConnection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cMSPeriodForwardConnection.setStatus("current")
_H3cMSForwardTotalTime_Type = Unsigned32
_H3cMSForwardTotalTime_Object = MibTableColumn
h3cMSForwardTotalTime = _H3cMSForwardTotalTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 9, 3, 2, 1, 1, 6),
    _H3cMSForwardTotalTime_Type()
)
h3cMSForwardTotalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cMSForwardTotalTime.setStatus("current")
_H3cMSForwardTotalConn_Type = Unsigned32
_H3cMSForwardTotalConn_Object = MibTableColumn
h3cMSForwardTotalConn = _H3cMSForwardTotalConn_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 9, 3, 2, 1, 1, 7),
    _H3cMSForwardTotalConn_Type()
)
h3cMSForwardTotalConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cMSForwardTotalConn.setStatus("current")
_H3cMSVODTable_Object = MibTable
h3cMSVODTable = _H3cMSVODTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 9, 3, 2, 2)
)
if mibBuilder.loadTexts:
    h3cMSVODTable.setStatus("current")
_H3cMSVODEntry_Object = MibTableRow
h3cMSVODEntry = _H3cMSVODEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 9, 3, 2, 2, 1)
)
h3cMSVODEntry.setIndexNames(
    (0, "H3C-MS-MAN-MIB", "h3cMSVODIndex"),
)
if mibBuilder.loadTexts:
    h3cMSVODEntry.setStatus("current")
_H3cMSVODIndex_Type = PhysicalIndex
_H3cMSVODIndex_Object = MibTableColumn
h3cMSVODIndex = _H3cMSVODIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 9, 3, 2, 2, 1, 1),
    _H3cMSVODIndex_Type()
)
h3cMSVODIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cMSVODIndex.setStatus("current")
_H3cMSVODMaxConnection_Type = Unsigned32
_H3cMSVODMaxConnection_Object = MibTableColumn
h3cMSVODMaxConnection = _H3cMSVODMaxConnection_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 9, 3, 2, 2, 1, 2),
    _H3cMSVODMaxConnection_Type()
)
h3cMSVODMaxConnection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cMSVODMaxConnection.setStatus("current")
_H3cMSVODConnectionThreshold_Type = Unsigned32
_H3cMSVODConnectionThreshold_Object = MibTableColumn
h3cMSVODConnectionThreshold = _H3cMSVODConnectionThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 9, 3, 2, 2, 1, 3),
    _H3cMSVODConnectionThreshold_Type()
)
h3cMSVODConnectionThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cMSVODConnectionThreshold.setStatus("current")
_H3cMSCurrentVODConnection_Type = Unsigned32
_H3cMSCurrentVODConnection_Object = MibTableColumn
h3cMSCurrentVODConnection = _H3cMSCurrentVODConnection_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 9, 3, 2, 2, 1, 4),
    _H3cMSCurrentVODConnection_Type()
)
h3cMSCurrentVODConnection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cMSCurrentVODConnection.setStatus("current")
_H3cMSPeriodVODMaxConnection_Type = Unsigned32
_H3cMSPeriodVODMaxConnection_Object = MibTableColumn
h3cMSPeriodVODMaxConnection = _H3cMSPeriodVODMaxConnection_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 9, 3, 2, 2, 1, 5),
    _H3cMSPeriodVODMaxConnection_Type()
)
h3cMSPeriodVODMaxConnection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cMSPeriodVODMaxConnection.setStatus("current")
_H3cMSVODTotalTime_Type = Unsigned32
_H3cMSVODTotalTime_Object = MibTableColumn
h3cMSVODTotalTime = _H3cMSVODTotalTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 9, 3, 2, 2, 1, 6),
    _H3cMSVODTotalTime_Type()
)
h3cMSVODTotalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cMSVODTotalTime.setStatus("current")
_H3cMSVODTotalConn_Type = Unsigned32
_H3cMSVODTotalConn_Object = MibTableColumn
h3cMSVODTotalConn = _H3cMSVODTotalConn_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 9, 3, 2, 2, 1, 7),
    _H3cMSVODTotalConn_Type()
)
h3cMSVODTotalConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cMSVODTotalConn.setStatus("current")
_H3cMSRecordTable_Object = MibTable
h3cMSRecordTable = _H3cMSRecordTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 9, 3, 2, 3)
)
if mibBuilder.loadTexts:
    h3cMSRecordTable.setStatus("current")
_H3cMSRecordEntry_Object = MibTableRow
h3cMSRecordEntry = _H3cMSRecordEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 9, 3, 2, 3, 1)
)
h3cMSRecordEntry.setIndexNames(
    (0, "H3C-MS-MAN-MIB", "h3cMSRecordIndex"),
)
if mibBuilder.loadTexts:
    h3cMSRecordEntry.setStatus("current")
_H3cMSRecordIndex_Type = PhysicalIndex
_H3cMSRecordIndex_Object = MibTableColumn
h3cMSRecordIndex = _H3cMSRecordIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 9, 3, 2, 3, 1, 1),
    _H3cMSRecordIndex_Type()
)
h3cMSRecordIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cMSRecordIndex.setStatus("current")
_H3cMSRecordMaxConnection_Type = Unsigned32
_H3cMSRecordMaxConnection_Object = MibTableColumn
h3cMSRecordMaxConnection = _H3cMSRecordMaxConnection_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 9, 3, 2, 3, 1, 2),
    _H3cMSRecordMaxConnection_Type()
)
h3cMSRecordMaxConnection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cMSRecordMaxConnection.setStatus("current")
_H3cMSRecordConnectionThreshold_Type = Unsigned32
_H3cMSRecordConnectionThreshold_Object = MibTableColumn
h3cMSRecordConnectionThreshold = _H3cMSRecordConnectionThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 9, 3, 2, 3, 1, 3),
    _H3cMSRecordConnectionThreshold_Type()
)
h3cMSRecordConnectionThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cMSRecordConnectionThreshold.setStatus("current")
_H3cMSCurrentRecordConnection_Type = Unsigned32
_H3cMSCurrentRecordConnection_Object = MibTableColumn
h3cMSCurrentRecordConnection = _H3cMSCurrentRecordConnection_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 9, 3, 2, 3, 1, 4),
    _H3cMSCurrentRecordConnection_Type()
)
h3cMSCurrentRecordConnection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cMSCurrentRecordConnection.setStatus("current")
_H3cMSPeriodRecordMaxConnection_Type = Unsigned32
_H3cMSPeriodRecordMaxConnection_Object = MibTableColumn
h3cMSPeriodRecordMaxConnection = _H3cMSPeriodRecordMaxConnection_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 9, 3, 2, 3, 1, 5),
    _H3cMSPeriodRecordMaxConnection_Type()
)
h3cMSPeriodRecordMaxConnection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cMSPeriodRecordMaxConnection.setStatus("current")
_H3cMSRecordTotalTime_Type = Unsigned32
_H3cMSRecordTotalTime_Object = MibTableColumn
h3cMSRecordTotalTime = _H3cMSRecordTotalTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 9, 3, 2, 3, 1, 6),
    _H3cMSRecordTotalTime_Type()
)
h3cMSRecordTotalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cMSRecordTotalTime.setStatus("current")
_H3cMSRecordTotalConn_Type = Unsigned32
_H3cMSRecordTotalConn_Object = MibTableColumn
h3cMSRecordTotalConn = _H3cMSRecordTotalConn_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 9, 3, 2, 3, 1, 7),
    _H3cMSRecordTotalConn_Type()
)
h3cMSRecordTotalConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cMSRecordTotalConn.setStatus("current")
_H3cMSManMIBTrap_ObjectIdentity = ObjectIdentity
h3cMSManMIBTrap = _H3cMSManMIBTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 9, 3, 3)
)
_H3cMSManTrapPrex_ObjectIdentity = ObjectIdentity
h3cMSManTrapPrex = _H3cMSManTrapPrex_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 9, 3, 3, 0)
)

# Managed Objects groups


# Notification objects

h3cMSManVODConnectionThresholdTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 9, 3, 3, 0, 1)
)
h3cMSManVODConnectionThresholdTrap.setObjects(
      *(("H3C-MS-MAN-MIB", "h3cMSVODIndex"),
        ("H3C-MS-MAN-MIB", "h3cMSCurrentVODConnection"),
        ("H3C-MS-MAN-MIB", "h3cMSVODConnectionThreshold"))
)
if mibBuilder.loadTexts:
    h3cMSManVODConnectionThresholdTrap.setStatus(
        "current"
    )

h3cMSManVODConnectionRecoverTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 9, 3, 3, 0, 2)
)
h3cMSManVODConnectionRecoverTrap.setObjects(
      *(("H3C-MS-MAN-MIB", "h3cMSVODIndex"),
        ("H3C-MS-MAN-MIB", "h3cMSCurrentVODConnection"),
        ("H3C-MS-MAN-MIB", "h3cMSVODConnectionThreshold"))
)
if mibBuilder.loadTexts:
    h3cMSManVODConnectionRecoverTrap.setStatus(
        "current"
    )

h3cMSManForwardConnectionThresholdTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 9, 3, 3, 0, 3)
)
h3cMSManForwardConnectionThresholdTrap.setObjects(
      *(("H3C-MS-MAN-MIB", "h3cMSForwardIndex"),
        ("H3C-MS-MAN-MIB", "h3cMSCurrentForwardConnection"),
        ("H3C-MS-MAN-MIB", "h3cMSForwardConnectionThreshold"))
)
if mibBuilder.loadTexts:
    h3cMSManForwardConnectionThresholdTrap.setStatus(
        "current"
    )

h3cMSManForwardConnectionRecoverTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 9, 3, 3, 0, 4)
)
h3cMSManForwardConnectionRecoverTrap.setObjects(
      *(("H3C-MS-MAN-MIB", "h3cMSForwardIndex"),
        ("H3C-MS-MAN-MIB", "h3cMSCurrentForwardConnection"),
        ("H3C-MS-MAN-MIB", "h3cMSForwardConnectionThreshold"))
)
if mibBuilder.loadTexts:
    h3cMSManForwardConnectionRecoverTrap.setStatus(
        "current"
    )

h3cMSManRecordConnectionThresholdTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 9, 3, 3, 0, 5)
)
h3cMSManRecordConnectionThresholdTrap.setObjects(
      *(("H3C-MS-MAN-MIB", "h3cMSRecordIndex"),
        ("H3C-MS-MAN-MIB", "h3cMSCurrentRecordConnection"),
        ("H3C-MS-MAN-MIB", "h3cMSRecordConnectionThreshold"))
)
if mibBuilder.loadTexts:
    h3cMSManRecordConnectionThresholdTrap.setStatus(
        "current"
    )

h3cMSManRecordConnectionRecoverTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 9, 3, 3, 0, 6)
)
h3cMSManRecordConnectionRecoverTrap.setObjects(
      *(("H3C-MS-MAN-MIB", "h3cMSRecordIndex"),
        ("H3C-MS-MAN-MIB", "h3cMSCurrentRecordConnection"),
        ("H3C-MS-MAN-MIB", "h3cMSRecordConnectionThreshold"))
)
if mibBuilder.loadTexts:
    h3cMSManRecordConnectionRecoverTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "H3C-MS-MAN-MIB",
    **{"h3cMSMan": h3cMSMan,
       "h3cMSManMIBObjects": h3cMSManMIBObjects,
       "h3cMSStatisticalPeriod": h3cMSStatisticalPeriod,
       "h3cMSManMIBTables": h3cMSManMIBTables,
       "h3cMSForwardTable": h3cMSForwardTable,
       "h3cMSForwardEntry": h3cMSForwardEntry,
       "h3cMSForwardIndex": h3cMSForwardIndex,
       "h3cMSForwardMaxConnection": h3cMSForwardMaxConnection,
       "h3cMSForwardConnectionThreshold": h3cMSForwardConnectionThreshold,
       "h3cMSCurrentForwardConnection": h3cMSCurrentForwardConnection,
       "h3cMSPeriodForwardConnection": h3cMSPeriodForwardConnection,
       "h3cMSForwardTotalTime": h3cMSForwardTotalTime,
       "h3cMSForwardTotalConn": h3cMSForwardTotalConn,
       "h3cMSVODTable": h3cMSVODTable,
       "h3cMSVODEntry": h3cMSVODEntry,
       "h3cMSVODIndex": h3cMSVODIndex,
       "h3cMSVODMaxConnection": h3cMSVODMaxConnection,
       "h3cMSVODConnectionThreshold": h3cMSVODConnectionThreshold,
       "h3cMSCurrentVODConnection": h3cMSCurrentVODConnection,
       "h3cMSPeriodVODMaxConnection": h3cMSPeriodVODMaxConnection,
       "h3cMSVODTotalTime": h3cMSVODTotalTime,
       "h3cMSVODTotalConn": h3cMSVODTotalConn,
       "h3cMSRecordTable": h3cMSRecordTable,
       "h3cMSRecordEntry": h3cMSRecordEntry,
       "h3cMSRecordIndex": h3cMSRecordIndex,
       "h3cMSRecordMaxConnection": h3cMSRecordMaxConnection,
       "h3cMSRecordConnectionThreshold": h3cMSRecordConnectionThreshold,
       "h3cMSCurrentRecordConnection": h3cMSCurrentRecordConnection,
       "h3cMSPeriodRecordMaxConnection": h3cMSPeriodRecordMaxConnection,
       "h3cMSRecordTotalTime": h3cMSRecordTotalTime,
       "h3cMSRecordTotalConn": h3cMSRecordTotalConn,
       "h3cMSManMIBTrap": h3cMSManMIBTrap,
       "h3cMSManTrapPrex": h3cMSManTrapPrex,
       "h3cMSManVODConnectionThresholdTrap": h3cMSManVODConnectionThresholdTrap,
       "h3cMSManVODConnectionRecoverTrap": h3cMSManVODConnectionRecoverTrap,
       "h3cMSManForwardConnectionThresholdTrap": h3cMSManForwardConnectionThresholdTrap,
       "h3cMSManForwardConnectionRecoverTrap": h3cMSManForwardConnectionRecoverTrap,
       "h3cMSManRecordConnectionThresholdTrap": h3cMSManRecordConnectionThresholdTrap,
       "h3cMSManRecordConnectionRecoverTrap": h3cMSManRecordConnectionRecoverTrap}
)
