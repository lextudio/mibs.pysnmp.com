# SNMP MIB module (HP-ICF-UDLD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HP-ICF-UDLD-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:58:20 2024
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

(hpSwitch,) = mibBuilder.importSymbols(
    "HP-ICF-OID",
    "hpSwitch")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 MacAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hpicfUdldMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 33)
)
hpicfUdldMIB.setRevisions(
        ("2014-06-15 00:00",
         "2009-08-07 00:00",
         "2006-04-10 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpicfUdldNotifications_ObjectIdentity = ObjectIdentity
hpicfUdldNotifications = _HpicfUdldNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 33, 0)
)
_HpicfUdldNotificationPrefix_ObjectIdentity = ObjectIdentity
hpicfUdldNotificationPrefix = _HpicfUdldNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 33, 0, 0)
)
_HpicfUdldObjects_ObjectIdentity = ObjectIdentity
hpicfUdldObjects = _HpicfUdldObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 33, 1)
)
_HpicfUdldConfig_ObjectIdentity = ObjectIdentity
hpicfUdldConfig = _HpicfUdldConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 33, 1, 1)
)


class _HpicfUdldConfigTimeInterval_Type(Unsigned32):
    """Custom type hpicfUdldConfigTimeInterval based on Unsigned32"""
    defaultValue = 50

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 100),
    )


_HpicfUdldConfigTimeInterval_Type.__name__ = "Unsigned32"
_HpicfUdldConfigTimeInterval_Object = MibScalar
hpicfUdldConfigTimeInterval = _HpicfUdldConfigTimeInterval_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 33, 1, 1, 1),
    _HpicfUdldConfigTimeInterval_Type()
)
hpicfUdldConfigTimeInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfUdldConfigTimeInterval.setStatus("current")


class _HpicfUdldConfigMaxRetries_Type(Unsigned32):
    """Custom type hpicfUdldConfigMaxRetries based on Unsigned32"""
    defaultValue = 4

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 10),
    )


_HpicfUdldConfigMaxRetries_Type.__name__ = "Unsigned32"
_HpicfUdldConfigMaxRetries_Object = MibScalar
hpicfUdldConfigMaxRetries = _HpicfUdldConfigMaxRetries_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 33, 1, 1, 2),
    _HpicfUdldConfigMaxRetries_Type()
)
hpicfUdldConfigMaxRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfUdldConfigMaxRetries.setStatus("current")
_HpicfUdldPortConfigTable_Object = MibTable
hpicfUdldPortConfigTable = _HpicfUdldPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 33, 1, 1, 3)
)
if mibBuilder.loadTexts:
    hpicfUdldPortConfigTable.setStatus("current")
_HpicfUdldPortConfigEntry_Object = MibTableRow
hpicfUdldPortConfigEntry = _HpicfUdldPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 33, 1, 1, 3, 1)
)
hpicfUdldPortConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hpicfUdldPortConfigEntry.setStatus("current")


class _HpicfUdldPortAdminStatus_Type(Integer32):
    """Custom type hpicfUdldPortAdminStatus based on Integer32"""
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


_HpicfUdldPortAdminStatus_Type.__name__ = "Integer32"
_HpicfUdldPortAdminStatus_Object = MibTableColumn
hpicfUdldPortAdminStatus = _HpicfUdldPortAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 33, 1, 1, 3, 1, 1),
    _HpicfUdldPortAdminStatus_Type()
)
hpicfUdldPortAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfUdldPortAdminStatus.setStatus("current")


class _HpicfUdldPortVlanId_Type(Integer32):
    """Custom type hpicfUdldPortVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_HpicfUdldPortVlanId_Type.__name__ = "Integer32"
_HpicfUdldPortVlanId_Object = MibTableColumn
hpicfUdldPortVlanId = _HpicfUdldPortVlanId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 33, 1, 1, 3, 1, 2),
    _HpicfUdldPortVlanId_Type()
)
hpicfUdldPortVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfUdldPortVlanId.setStatus("current")


class _HpicfUdldConfigForwardMode_Type(Integer32):
    """Custom type hpicfUdldConfigForwardMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forwardThenVerify", 2),
          ("verifyThenForward", 1))
    )


_HpicfUdldConfigForwardMode_Type.__name__ = "Integer32"
_HpicfUdldConfigForwardMode_Object = MibScalar
hpicfUdldConfigForwardMode = _HpicfUdldConfigForwardMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 33, 1, 1, 4),
    _HpicfUdldConfigForwardMode_Type()
)
hpicfUdldConfigForwardMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfUdldConfigForwardMode.setStatus("current")


class _HpicfUdldConfigTimeIntervalMs_Type(Unsigned32):
    """Custom type hpicfUdldConfigTimeIntervalMs based on Unsigned32"""
    defaultValue = 5000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_HpicfUdldConfigTimeIntervalMs_Type.__name__ = "Unsigned32"
_HpicfUdldConfigTimeIntervalMs_Object = MibScalar
hpicfUdldConfigTimeIntervalMs = _HpicfUdldConfigTimeIntervalMs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 33, 1, 1, 5),
    _HpicfUdldConfigTimeIntervalMs_Type()
)
hpicfUdldConfigTimeIntervalMs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfUdldConfigTimeIntervalMs.setStatus("current")
_HpicfUdldStats_ObjectIdentity = ObjectIdentity
hpicfUdldStats = _HpicfUdldStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 33, 1, 2)
)
_HpicfUdldPortStatsTable_Object = MibTable
hpicfUdldPortStatsTable = _HpicfUdldPortStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 33, 1, 2, 1)
)
if mibBuilder.loadTexts:
    hpicfUdldPortStatsTable.setStatus("current")
_HpicfUdldPortStatsEntry_Object = MibTableRow
hpicfUdldPortStatsEntry = _HpicfUdldPortStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 33, 1, 2, 1, 1)
)
hpicfUdldPortStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hpicfUdldPortStatsEntry.setStatus("current")


class _HpicfUdldStatsPortCurrentState_Type(Integer32):
    """Custom type hpicfUdldStatsPortCurrentState based on Integer32"""
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
        *(("failure", 2),
          ("offline", 1),
          ("unknown", 0),
          ("up", 3))
    )


_HpicfUdldStatsPortCurrentState_Type.__name__ = "Integer32"
_HpicfUdldStatsPortCurrentState_Object = MibTableColumn
hpicfUdldStatsPortCurrentState = _HpicfUdldStatsPortCurrentState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 33, 1, 2, 1, 1, 1),
    _HpicfUdldStatsPortCurrentState_Type()
)
hpicfUdldStatsPortCurrentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfUdldStatsPortCurrentState.setStatus("current")
_HpicfUdldStatsPortNeighborMAC_Type = MacAddress
_HpicfUdldStatsPortNeighborMAC_Object = MibTableColumn
hpicfUdldStatsPortNeighborMAC = _HpicfUdldStatsPortNeighborMAC_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 33, 1, 2, 1, 1, 2),
    _HpicfUdldStatsPortNeighborMAC_Type()
)
hpicfUdldStatsPortNeighborMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfUdldStatsPortNeighborMAC.setStatus("current")
_HpicfUdldStatsPortNeighborPort_Type = Integer32
_HpicfUdldStatsPortNeighborPort_Object = MibTableColumn
hpicfUdldStatsPortNeighborPort = _HpicfUdldStatsPortNeighborPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 33, 1, 2, 1, 1, 3),
    _HpicfUdldStatsPortNeighborPort_Type()
)
hpicfUdldStatsPortNeighborPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfUdldStatsPortNeighborPort.setStatus("current")
_HpicfUdldStatsPortTotalTx_Type = Counter32
_HpicfUdldStatsPortTotalTx_Object = MibTableColumn
hpicfUdldStatsPortTotalTx = _HpicfUdldStatsPortTotalTx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 33, 1, 2, 1, 1, 4),
    _HpicfUdldStatsPortTotalTx_Type()
)
hpicfUdldStatsPortTotalTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfUdldStatsPortTotalTx.setStatus("current")
_HpicfUdldStatsPortTotalRx_Type = Counter32
_HpicfUdldStatsPortTotalRx_Object = MibTableColumn
hpicfUdldStatsPortTotalRx = _HpicfUdldStatsPortTotalRx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 33, 1, 2, 1, 1, 5),
    _HpicfUdldStatsPortTotalRx_Type()
)
hpicfUdldStatsPortTotalRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfUdldStatsPortTotalRx.setStatus("current")
_HpicfUdldStatsPortNumStateChange_Type = Counter32
_HpicfUdldStatsPortNumStateChange_Object = MibTableColumn
hpicfUdldStatsPortNumStateChange = _HpicfUdldStatsPortNumStateChange_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 33, 1, 2, 1, 1, 6),
    _HpicfUdldStatsPortNumStateChange_Type()
)
hpicfUdldStatsPortNumStateChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfUdldStatsPortNumStateChange.setStatus("current")
_HpicfUdldStatsPortStatus_Type = Integer32
_HpicfUdldStatsPortStatus_Object = MibTableColumn
hpicfUdldStatsPortStatus = _HpicfUdldStatsPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 33, 1, 2, 1, 1, 7),
    _HpicfUdldStatsPortStatus_Type()
)
hpicfUdldStatsPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfUdldStatsPortStatus.setStatus("current")
_HpicfUdldStatsClearAll_Type = TruthValue
_HpicfUdldStatsClearAll_Object = MibScalar
hpicfUdldStatsClearAll = _HpicfUdldStatsClearAll_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 33, 1, 2, 2),
    _HpicfUdldStatsClearAll_Type()
)
hpicfUdldStatsClearAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfUdldStatsClearAll.setStatus("current")
_HpicfUdldConformance_ObjectIdentity = ObjectIdentity
hpicfUdldConformance = _HpicfUdldConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 33, 2)
)
_HpicfUdldCompliances_ObjectIdentity = ObjectIdentity
hpicfUdldCompliances = _HpicfUdldCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 33, 2, 1)
)
_HpicfUdldGroups_ObjectIdentity = ObjectIdentity
hpicfUdldGroups = _HpicfUdldGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 33, 2, 2)
)

# Managed Objects groups

hpicfUdldPortConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 33, 2, 2, 1)
)
hpicfUdldPortConfigGroup.setObjects(
      *(("HP-ICF-UDLD-MIB", "hpicfUdldConfigTimeInterval"),
        ("HP-ICF-UDLD-MIB", "hpicfUdldConfigMaxRetries"),
        ("HP-ICF-UDLD-MIB", "hpicfUdldPortAdminStatus"),
        ("HP-ICF-UDLD-MIB", "hpicfUdldPortVlanId"))
)
if mibBuilder.loadTexts:
    hpicfUdldPortConfigGroup.setStatus("deprecated")

hpicfUdldPortStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 33, 2, 2, 2)
)
hpicfUdldPortStatsGroup.setObjects(
      *(("HP-ICF-UDLD-MIB", "hpicfUdldStatsPortCurrentState"),
        ("HP-ICF-UDLD-MIB", "hpicfUdldStatsPortNeighborMAC"),
        ("HP-ICF-UDLD-MIB", "hpicfUdldStatsPortNeighborPort"),
        ("HP-ICF-UDLD-MIB", "hpicfUdldStatsPortTotalTx"),
        ("HP-ICF-UDLD-MIB", "hpicfUdldStatsPortTotalRx"),
        ("HP-ICF-UDLD-MIB", "hpicfUdldStatsPortNumStateChange"),
        ("HP-ICF-UDLD-MIB", "hpicfUdldStatsPortStatus"))
)
if mibBuilder.loadTexts:
    hpicfUdldPortStatsGroup.setStatus("current")

hpicfUdldStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 33, 2, 2, 4)
)
hpicfUdldStatsGroup.setObjects(
    ("HP-ICF-UDLD-MIB", "hpicfUdldStatsClearAll")
)
if mibBuilder.loadTexts:
    hpicfUdldStatsGroup.setStatus("current")

hpicfUdldPortConfigGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 33, 2, 2, 5)
)
hpicfUdldPortConfigGroup1.setObjects(
      *(("HP-ICF-UDLD-MIB", "hpicfUdldConfigTimeInterval"),
        ("HP-ICF-UDLD-MIB", "hpicfUdldConfigMaxRetries"),
        ("HP-ICF-UDLD-MIB", "hpicfUdldPortAdminStatus"),
        ("HP-ICF-UDLD-MIB", "hpicfUdldPortVlanId"),
        ("HP-ICF-UDLD-MIB", "hpicfUdldConfigForwardMode"),
        ("HP-ICF-UDLD-MIB", "hpicfUdldConfigTimeIntervalMs"))
)
if mibBuilder.loadTexts:
    hpicfUdldPortConfigGroup1.setStatus("current")


# Notification objects

hpicfUdldLinkfault = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 33, 0, 0, 1)
)
hpicfUdldLinkfault.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    hpicfUdldLinkfault.setStatus(
        "current"
    )

hpicfUdldLinkUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 33, 0, 0, 2)
)
hpicfUdldLinkUp.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    hpicfUdldLinkUp.setStatus(
        "current"
    )


# Notifications groups

hpicfUdldNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 33, 2, 2, 3)
)
hpicfUdldNotificationGroup.setObjects(
      *(("HP-ICF-UDLD-MIB", "hpicfUdldLinkfault"),
        ("HP-ICF-UDLD-MIB", "hpicfUdldLinkUp"))
)
if mibBuilder.loadTexts:
    hpicfUdldNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hpicfUdldCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 33, 2, 1, 1)
)
if mibBuilder.loadTexts:
    hpicfUdldCompliance.setStatus(
        "deprecated"
    )

hpicfUdldCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 33, 2, 1, 2)
)
if mibBuilder.loadTexts:
    hpicfUdldCompliance2.setStatus(
        "current"
    )

hpicfUdldCompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 33, 2, 1, 3)
)
if mibBuilder.loadTexts:
    hpicfUdldCompliance3.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HP-ICF-UDLD-MIB",
    **{"hpicfUdldMIB": hpicfUdldMIB,
       "hpicfUdldNotifications": hpicfUdldNotifications,
       "hpicfUdldNotificationPrefix": hpicfUdldNotificationPrefix,
       "hpicfUdldLinkfault": hpicfUdldLinkfault,
       "hpicfUdldLinkUp": hpicfUdldLinkUp,
       "hpicfUdldObjects": hpicfUdldObjects,
       "hpicfUdldConfig": hpicfUdldConfig,
       "hpicfUdldConfigTimeInterval": hpicfUdldConfigTimeInterval,
       "hpicfUdldConfigMaxRetries": hpicfUdldConfigMaxRetries,
       "hpicfUdldPortConfigTable": hpicfUdldPortConfigTable,
       "hpicfUdldPortConfigEntry": hpicfUdldPortConfigEntry,
       "hpicfUdldPortAdminStatus": hpicfUdldPortAdminStatus,
       "hpicfUdldPortVlanId": hpicfUdldPortVlanId,
       "hpicfUdldConfigForwardMode": hpicfUdldConfigForwardMode,
       "hpicfUdldConfigTimeIntervalMs": hpicfUdldConfigTimeIntervalMs,
       "hpicfUdldStats": hpicfUdldStats,
       "hpicfUdldPortStatsTable": hpicfUdldPortStatsTable,
       "hpicfUdldPortStatsEntry": hpicfUdldPortStatsEntry,
       "hpicfUdldStatsPortCurrentState": hpicfUdldStatsPortCurrentState,
       "hpicfUdldStatsPortNeighborMAC": hpicfUdldStatsPortNeighborMAC,
       "hpicfUdldStatsPortNeighborPort": hpicfUdldStatsPortNeighborPort,
       "hpicfUdldStatsPortTotalTx": hpicfUdldStatsPortTotalTx,
       "hpicfUdldStatsPortTotalRx": hpicfUdldStatsPortTotalRx,
       "hpicfUdldStatsPortNumStateChange": hpicfUdldStatsPortNumStateChange,
       "hpicfUdldStatsPortStatus": hpicfUdldStatsPortStatus,
       "hpicfUdldStatsClearAll": hpicfUdldStatsClearAll,
       "hpicfUdldConformance": hpicfUdldConformance,
       "hpicfUdldCompliances": hpicfUdldCompliances,
       "hpicfUdldCompliance": hpicfUdldCompliance,
       "hpicfUdldCompliance2": hpicfUdldCompliance2,
       "hpicfUdldCompliance3": hpicfUdldCompliance3,
       "hpicfUdldGroups": hpicfUdldGroups,
       "hpicfUdldPortConfigGroup": hpicfUdldPortConfigGroup,
       "hpicfUdldPortStatsGroup": hpicfUdldPortStatsGroup,
       "hpicfUdldNotificationGroup": hpicfUdldNotificationGroup,
       "hpicfUdldStatsGroup": hpicfUdldStatsGroup,
       "hpicfUdldPortConfigGroup1": hpicfUdldPortConfigGroup1}
)
