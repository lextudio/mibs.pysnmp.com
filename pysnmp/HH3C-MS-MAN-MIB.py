# SNMP MIB module (HH3C-MS-MAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-MS-MAN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:54:16 2024
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

(hh3cSurveillanceMIB,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cSurveillanceMIB")

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

hh3cMSMan = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 9, 3)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cMSManMIBObjects_ObjectIdentity = ObjectIdentity
hh3cMSManMIBObjects = _Hh3cMSManMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 9, 3, 1)
)
_Hh3cMSStatisticalPeriod_Type = Unsigned32
_Hh3cMSStatisticalPeriod_Object = MibScalar
hh3cMSStatisticalPeriod = _Hh3cMSStatisticalPeriod_Object(
    (1, 3, 6, 1, 4, 1, 25506, 9, 3, 1, 1),
    _Hh3cMSStatisticalPeriod_Type()
)
hh3cMSStatisticalPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cMSStatisticalPeriod.setStatus("current")
_Hh3cMSManMIBTables_ObjectIdentity = ObjectIdentity
hh3cMSManMIBTables = _Hh3cMSManMIBTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 9, 3, 2)
)
_Hh3cMSForwardTable_Object = MibTable
hh3cMSForwardTable = _Hh3cMSForwardTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 9, 3, 2, 1)
)
if mibBuilder.loadTexts:
    hh3cMSForwardTable.setStatus("current")
_Hh3cMSForwardEntry_Object = MibTableRow
hh3cMSForwardEntry = _Hh3cMSForwardEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 9, 3, 2, 1, 1)
)
hh3cMSForwardEntry.setIndexNames(
    (0, "HH3C-MS-MAN-MIB", "hh3cMSForwardIndex"),
)
if mibBuilder.loadTexts:
    hh3cMSForwardEntry.setStatus("current")
_Hh3cMSForwardIndex_Type = PhysicalIndex
_Hh3cMSForwardIndex_Object = MibTableColumn
hh3cMSForwardIndex = _Hh3cMSForwardIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 9, 3, 2, 1, 1, 1),
    _Hh3cMSForwardIndex_Type()
)
hh3cMSForwardIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cMSForwardIndex.setStatus("current")
_Hh3cMSForwardMaxConnection_Type = Unsigned32
_Hh3cMSForwardMaxConnection_Object = MibTableColumn
hh3cMSForwardMaxConnection = _Hh3cMSForwardMaxConnection_Object(
    (1, 3, 6, 1, 4, 1, 25506, 9, 3, 2, 1, 1, 2),
    _Hh3cMSForwardMaxConnection_Type()
)
hh3cMSForwardMaxConnection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMSForwardMaxConnection.setStatus("current")
_Hh3cMSForwardConnectionThreshold_Type = Unsigned32
_Hh3cMSForwardConnectionThreshold_Object = MibTableColumn
hh3cMSForwardConnectionThreshold = _Hh3cMSForwardConnectionThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25506, 9, 3, 2, 1, 1, 3),
    _Hh3cMSForwardConnectionThreshold_Type()
)
hh3cMSForwardConnectionThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cMSForwardConnectionThreshold.setStatus("current")
_Hh3cMSCurrentForwardConnection_Type = Unsigned32
_Hh3cMSCurrentForwardConnection_Object = MibTableColumn
hh3cMSCurrentForwardConnection = _Hh3cMSCurrentForwardConnection_Object(
    (1, 3, 6, 1, 4, 1, 25506, 9, 3, 2, 1, 1, 4),
    _Hh3cMSCurrentForwardConnection_Type()
)
hh3cMSCurrentForwardConnection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMSCurrentForwardConnection.setStatus("current")
_Hh3cMSPeriodForwardConnection_Type = Unsigned32
_Hh3cMSPeriodForwardConnection_Object = MibTableColumn
hh3cMSPeriodForwardConnection = _Hh3cMSPeriodForwardConnection_Object(
    (1, 3, 6, 1, 4, 1, 25506, 9, 3, 2, 1, 1, 5),
    _Hh3cMSPeriodForwardConnection_Type()
)
hh3cMSPeriodForwardConnection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMSPeriodForwardConnection.setStatus("current")
_Hh3cMSForwardTotalTime_Type = Unsigned32
_Hh3cMSForwardTotalTime_Object = MibTableColumn
hh3cMSForwardTotalTime = _Hh3cMSForwardTotalTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 9, 3, 2, 1, 1, 6),
    _Hh3cMSForwardTotalTime_Type()
)
hh3cMSForwardTotalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMSForwardTotalTime.setStatus("current")
_Hh3cMSForwardTotalConn_Type = Unsigned32
_Hh3cMSForwardTotalConn_Object = MibTableColumn
hh3cMSForwardTotalConn = _Hh3cMSForwardTotalConn_Object(
    (1, 3, 6, 1, 4, 1, 25506, 9, 3, 2, 1, 1, 7),
    _Hh3cMSForwardTotalConn_Type()
)
hh3cMSForwardTotalConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMSForwardTotalConn.setStatus("current")
_Hh3cMSVODTable_Object = MibTable
hh3cMSVODTable = _Hh3cMSVODTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 9, 3, 2, 2)
)
if mibBuilder.loadTexts:
    hh3cMSVODTable.setStatus("current")
_Hh3cMSVODEntry_Object = MibTableRow
hh3cMSVODEntry = _Hh3cMSVODEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 9, 3, 2, 2, 1)
)
hh3cMSVODEntry.setIndexNames(
    (0, "HH3C-MS-MAN-MIB", "hh3cMSVODIndex"),
)
if mibBuilder.loadTexts:
    hh3cMSVODEntry.setStatus("current")
_Hh3cMSVODIndex_Type = PhysicalIndex
_Hh3cMSVODIndex_Object = MibTableColumn
hh3cMSVODIndex = _Hh3cMSVODIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 9, 3, 2, 2, 1, 1),
    _Hh3cMSVODIndex_Type()
)
hh3cMSVODIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cMSVODIndex.setStatus("current")
_Hh3cMSVODMaxConnection_Type = Unsigned32
_Hh3cMSVODMaxConnection_Object = MibTableColumn
hh3cMSVODMaxConnection = _Hh3cMSVODMaxConnection_Object(
    (1, 3, 6, 1, 4, 1, 25506, 9, 3, 2, 2, 1, 2),
    _Hh3cMSVODMaxConnection_Type()
)
hh3cMSVODMaxConnection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMSVODMaxConnection.setStatus("current")
_Hh3cMSVODConnectionThreshold_Type = Unsigned32
_Hh3cMSVODConnectionThreshold_Object = MibTableColumn
hh3cMSVODConnectionThreshold = _Hh3cMSVODConnectionThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25506, 9, 3, 2, 2, 1, 3),
    _Hh3cMSVODConnectionThreshold_Type()
)
hh3cMSVODConnectionThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cMSVODConnectionThreshold.setStatus("current")
_Hh3cMSCurrentVODConnection_Type = Unsigned32
_Hh3cMSCurrentVODConnection_Object = MibTableColumn
hh3cMSCurrentVODConnection = _Hh3cMSCurrentVODConnection_Object(
    (1, 3, 6, 1, 4, 1, 25506, 9, 3, 2, 2, 1, 4),
    _Hh3cMSCurrentVODConnection_Type()
)
hh3cMSCurrentVODConnection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMSCurrentVODConnection.setStatus("current")
_Hh3cMSPeriodVODMaxConnection_Type = Unsigned32
_Hh3cMSPeriodVODMaxConnection_Object = MibTableColumn
hh3cMSPeriodVODMaxConnection = _Hh3cMSPeriodVODMaxConnection_Object(
    (1, 3, 6, 1, 4, 1, 25506, 9, 3, 2, 2, 1, 5),
    _Hh3cMSPeriodVODMaxConnection_Type()
)
hh3cMSPeriodVODMaxConnection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMSPeriodVODMaxConnection.setStatus("current")
_Hh3cMSVODTotalTime_Type = Unsigned32
_Hh3cMSVODTotalTime_Object = MibTableColumn
hh3cMSVODTotalTime = _Hh3cMSVODTotalTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 9, 3, 2, 2, 1, 6),
    _Hh3cMSVODTotalTime_Type()
)
hh3cMSVODTotalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMSVODTotalTime.setStatus("current")
_Hh3cMSVODTotalConn_Type = Unsigned32
_Hh3cMSVODTotalConn_Object = MibTableColumn
hh3cMSVODTotalConn = _Hh3cMSVODTotalConn_Object(
    (1, 3, 6, 1, 4, 1, 25506, 9, 3, 2, 2, 1, 7),
    _Hh3cMSVODTotalConn_Type()
)
hh3cMSVODTotalConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMSVODTotalConn.setStatus("current")
_Hh3cMSRecordTable_Object = MibTable
hh3cMSRecordTable = _Hh3cMSRecordTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 9, 3, 2, 3)
)
if mibBuilder.loadTexts:
    hh3cMSRecordTable.setStatus("current")
_Hh3cMSRecordEntry_Object = MibTableRow
hh3cMSRecordEntry = _Hh3cMSRecordEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 9, 3, 2, 3, 1)
)
hh3cMSRecordEntry.setIndexNames(
    (0, "HH3C-MS-MAN-MIB", "hh3cMSRecordIndex"),
)
if mibBuilder.loadTexts:
    hh3cMSRecordEntry.setStatus("current")
_Hh3cMSRecordIndex_Type = PhysicalIndex
_Hh3cMSRecordIndex_Object = MibTableColumn
hh3cMSRecordIndex = _Hh3cMSRecordIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 9, 3, 2, 3, 1, 1),
    _Hh3cMSRecordIndex_Type()
)
hh3cMSRecordIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cMSRecordIndex.setStatus("current")
_Hh3cMSRecordMaxConnection_Type = Unsigned32
_Hh3cMSRecordMaxConnection_Object = MibTableColumn
hh3cMSRecordMaxConnection = _Hh3cMSRecordMaxConnection_Object(
    (1, 3, 6, 1, 4, 1, 25506, 9, 3, 2, 3, 1, 2),
    _Hh3cMSRecordMaxConnection_Type()
)
hh3cMSRecordMaxConnection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMSRecordMaxConnection.setStatus("current")
_Hh3cMSRecordConnectionThreshold_Type = Unsigned32
_Hh3cMSRecordConnectionThreshold_Object = MibTableColumn
hh3cMSRecordConnectionThreshold = _Hh3cMSRecordConnectionThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25506, 9, 3, 2, 3, 1, 3),
    _Hh3cMSRecordConnectionThreshold_Type()
)
hh3cMSRecordConnectionThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cMSRecordConnectionThreshold.setStatus("current")
_Hh3cMSCurrentRecordConnection_Type = Unsigned32
_Hh3cMSCurrentRecordConnection_Object = MibTableColumn
hh3cMSCurrentRecordConnection = _Hh3cMSCurrentRecordConnection_Object(
    (1, 3, 6, 1, 4, 1, 25506, 9, 3, 2, 3, 1, 4),
    _Hh3cMSCurrentRecordConnection_Type()
)
hh3cMSCurrentRecordConnection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMSCurrentRecordConnection.setStatus("current")
_Hh3cMSPeriodRecordMaxConnection_Type = Unsigned32
_Hh3cMSPeriodRecordMaxConnection_Object = MibTableColumn
hh3cMSPeriodRecordMaxConnection = _Hh3cMSPeriodRecordMaxConnection_Object(
    (1, 3, 6, 1, 4, 1, 25506, 9, 3, 2, 3, 1, 5),
    _Hh3cMSPeriodRecordMaxConnection_Type()
)
hh3cMSPeriodRecordMaxConnection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMSPeriodRecordMaxConnection.setStatus("current")
_Hh3cMSRecordTotalTime_Type = Unsigned32
_Hh3cMSRecordTotalTime_Object = MibTableColumn
hh3cMSRecordTotalTime = _Hh3cMSRecordTotalTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 9, 3, 2, 3, 1, 6),
    _Hh3cMSRecordTotalTime_Type()
)
hh3cMSRecordTotalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMSRecordTotalTime.setStatus("current")
_Hh3cMSRecordTotalConn_Type = Unsigned32
_Hh3cMSRecordTotalConn_Object = MibTableColumn
hh3cMSRecordTotalConn = _Hh3cMSRecordTotalConn_Object(
    (1, 3, 6, 1, 4, 1, 25506, 9, 3, 2, 3, 1, 7),
    _Hh3cMSRecordTotalConn_Type()
)
hh3cMSRecordTotalConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMSRecordTotalConn.setStatus("current")
_Hh3cMSManMIBTrap_ObjectIdentity = ObjectIdentity
hh3cMSManMIBTrap = _Hh3cMSManMIBTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 9, 3, 3)
)
_Hh3cMSManTrapPrex_ObjectIdentity = ObjectIdentity
hh3cMSManTrapPrex = _Hh3cMSManTrapPrex_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 9, 3, 3, 0)
)

# Managed Objects groups


# Notification objects

hh3cMSManVODConnectionThresholdTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 9, 3, 3, 0, 1)
)
hh3cMSManVODConnectionThresholdTrap.setObjects(
      *(("HH3C-MS-MAN-MIB", "hh3cMSVODIndex"),
        ("HH3C-MS-MAN-MIB", "hh3cMSCurrentVODConnection"),
        ("HH3C-MS-MAN-MIB", "hh3cMSVODConnectionThreshold"))
)
if mibBuilder.loadTexts:
    hh3cMSManVODConnectionThresholdTrap.setStatus(
        "current"
    )

hh3cMSManVODConnectionRecoverTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 9, 3, 3, 0, 2)
)
hh3cMSManVODConnectionRecoverTrap.setObjects(
      *(("HH3C-MS-MAN-MIB", "hh3cMSVODIndex"),
        ("HH3C-MS-MAN-MIB", "hh3cMSCurrentVODConnection"),
        ("HH3C-MS-MAN-MIB", "hh3cMSVODConnectionThreshold"))
)
if mibBuilder.loadTexts:
    hh3cMSManVODConnectionRecoverTrap.setStatus(
        "current"
    )

hh3cMSManForwardConnectionThresholdTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 9, 3, 3, 0, 3)
)
hh3cMSManForwardConnectionThresholdTrap.setObjects(
      *(("HH3C-MS-MAN-MIB", "hh3cMSForwardIndex"),
        ("HH3C-MS-MAN-MIB", "hh3cMSCurrentForwardConnection"),
        ("HH3C-MS-MAN-MIB", "hh3cMSForwardConnectionThreshold"))
)
if mibBuilder.loadTexts:
    hh3cMSManForwardConnectionThresholdTrap.setStatus(
        "current"
    )

hh3cMSManForwardConnectionRecoverTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 9, 3, 3, 0, 4)
)
hh3cMSManForwardConnectionRecoverTrap.setObjects(
      *(("HH3C-MS-MAN-MIB", "hh3cMSForwardIndex"),
        ("HH3C-MS-MAN-MIB", "hh3cMSCurrentForwardConnection"),
        ("HH3C-MS-MAN-MIB", "hh3cMSForwardConnectionThreshold"))
)
if mibBuilder.loadTexts:
    hh3cMSManForwardConnectionRecoverTrap.setStatus(
        "current"
    )

hh3cMSManRecordConnectionThresholdTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 9, 3, 3, 0, 5)
)
hh3cMSManRecordConnectionThresholdTrap.setObjects(
      *(("HH3C-MS-MAN-MIB", "hh3cMSRecordIndex"),
        ("HH3C-MS-MAN-MIB", "hh3cMSCurrentRecordConnection"),
        ("HH3C-MS-MAN-MIB", "hh3cMSRecordConnectionThreshold"))
)
if mibBuilder.loadTexts:
    hh3cMSManRecordConnectionThresholdTrap.setStatus(
        "current"
    )

hh3cMSManRecordConnectionRecoverTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 9, 3, 3, 0, 6)
)
hh3cMSManRecordConnectionRecoverTrap.setObjects(
      *(("HH3C-MS-MAN-MIB", "hh3cMSRecordIndex"),
        ("HH3C-MS-MAN-MIB", "hh3cMSCurrentRecordConnection"),
        ("HH3C-MS-MAN-MIB", "hh3cMSRecordConnectionThreshold"))
)
if mibBuilder.loadTexts:
    hh3cMSManRecordConnectionRecoverTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-MS-MAN-MIB",
    **{"hh3cMSMan": hh3cMSMan,
       "hh3cMSManMIBObjects": hh3cMSManMIBObjects,
       "hh3cMSStatisticalPeriod": hh3cMSStatisticalPeriod,
       "hh3cMSManMIBTables": hh3cMSManMIBTables,
       "hh3cMSForwardTable": hh3cMSForwardTable,
       "hh3cMSForwardEntry": hh3cMSForwardEntry,
       "hh3cMSForwardIndex": hh3cMSForwardIndex,
       "hh3cMSForwardMaxConnection": hh3cMSForwardMaxConnection,
       "hh3cMSForwardConnectionThreshold": hh3cMSForwardConnectionThreshold,
       "hh3cMSCurrentForwardConnection": hh3cMSCurrentForwardConnection,
       "hh3cMSPeriodForwardConnection": hh3cMSPeriodForwardConnection,
       "hh3cMSForwardTotalTime": hh3cMSForwardTotalTime,
       "hh3cMSForwardTotalConn": hh3cMSForwardTotalConn,
       "hh3cMSVODTable": hh3cMSVODTable,
       "hh3cMSVODEntry": hh3cMSVODEntry,
       "hh3cMSVODIndex": hh3cMSVODIndex,
       "hh3cMSVODMaxConnection": hh3cMSVODMaxConnection,
       "hh3cMSVODConnectionThreshold": hh3cMSVODConnectionThreshold,
       "hh3cMSCurrentVODConnection": hh3cMSCurrentVODConnection,
       "hh3cMSPeriodVODMaxConnection": hh3cMSPeriodVODMaxConnection,
       "hh3cMSVODTotalTime": hh3cMSVODTotalTime,
       "hh3cMSVODTotalConn": hh3cMSVODTotalConn,
       "hh3cMSRecordTable": hh3cMSRecordTable,
       "hh3cMSRecordEntry": hh3cMSRecordEntry,
       "hh3cMSRecordIndex": hh3cMSRecordIndex,
       "hh3cMSRecordMaxConnection": hh3cMSRecordMaxConnection,
       "hh3cMSRecordConnectionThreshold": hh3cMSRecordConnectionThreshold,
       "hh3cMSCurrentRecordConnection": hh3cMSCurrentRecordConnection,
       "hh3cMSPeriodRecordMaxConnection": hh3cMSPeriodRecordMaxConnection,
       "hh3cMSRecordTotalTime": hh3cMSRecordTotalTime,
       "hh3cMSRecordTotalConn": hh3cMSRecordTotalConn,
       "hh3cMSManMIBTrap": hh3cMSManMIBTrap,
       "hh3cMSManTrapPrex": hh3cMSManTrapPrex,
       "hh3cMSManVODConnectionThresholdTrap": hh3cMSManVODConnectionThresholdTrap,
       "hh3cMSManVODConnectionRecoverTrap": hh3cMSManVODConnectionRecoverTrap,
       "hh3cMSManForwardConnectionThresholdTrap": hh3cMSManForwardConnectionThresholdTrap,
       "hh3cMSManForwardConnectionRecoverTrap": hh3cMSManForwardConnectionRecoverTrap,
       "hh3cMSManRecordConnectionThresholdTrap": hh3cMSManRecordConnectionThresholdTrap,
       "hh3cMSManRecordConnectionRecoverTrap": hh3cMSManRecordConnectionRecoverTrap}
)
