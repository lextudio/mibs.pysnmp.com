# SNMP MIB module (RBN-ATM-PVC-OAM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RBN-ATM-PVC-OAM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:44:55 2024
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

(rbnMgmt,) = mibBuilder.importSymbols(
    "RBN-SMI",
    "rbnMgmt")

(RbnPort,
 RbnSlot) = mibBuilder.importSymbols(
    "RBN-TC",
    "RbnPort",
    "RbnSlot")

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

rbnAtmPvcOamMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 19)
)
rbnAtmPvcOamMib.setRevisions(
        ("2002-11-13 00:00",
         "2002-02-05 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RbnAtmPvcOamMibNotifications_ObjectIdentity = ObjectIdentity
rbnAtmPvcOamMibNotifications = _RbnAtmPvcOamMibNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 19, 0)
)
_RbnAtmPvcOamMibObjects_ObjectIdentity = ObjectIdentity
rbnAtmPvcOamMibObjects = _RbnAtmPvcOamMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 19, 1)
)
_RbnAtmPvcOamStatusTable_Object = MibTable
rbnAtmPvcOamStatusTable = _RbnAtmPvcOamStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 19, 1, 1)
)
if mibBuilder.loadTexts:
    rbnAtmPvcOamStatusTable.setStatus("current")
_RbnAtmPvcOamStatusEntry_Object = MibTableRow
rbnAtmPvcOamStatusEntry = _RbnAtmPvcOamStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 19, 1, 1, 1)
)
rbnAtmPvcOamStatusEntry.setIndexNames(
    (0, "RBN-ATM-PVC-OAM-MIB", "rbnAtmPvcOamStatusSlot"),
    (0, "RBN-ATM-PVC-OAM-MIB", "rbnAtmPvcOamStatusPort"),
    (0, "RBN-ATM-PVC-OAM-MIB", "rbnAtmPvcOamStatusVpi"),
    (0, "RBN-ATM-PVC-OAM-MIB", "rbnAtmPvcOamStatusVci"),
)
if mibBuilder.loadTexts:
    rbnAtmPvcOamStatusEntry.setStatus("current")
_RbnAtmPvcOamStatusSlot_Type = RbnSlot
_RbnAtmPvcOamStatusSlot_Object = MibTableColumn
rbnAtmPvcOamStatusSlot = _RbnAtmPvcOamStatusSlot_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 19, 1, 1, 1, 1),
    _RbnAtmPvcOamStatusSlot_Type()
)
rbnAtmPvcOamStatusSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbnAtmPvcOamStatusSlot.setStatus("current")
_RbnAtmPvcOamStatusPort_Type = RbnPort
_RbnAtmPvcOamStatusPort_Object = MibTableColumn
rbnAtmPvcOamStatusPort = _RbnAtmPvcOamStatusPort_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 19, 1, 1, 1, 2),
    _RbnAtmPvcOamStatusPort_Type()
)
rbnAtmPvcOamStatusPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbnAtmPvcOamStatusPort.setStatus("current")


class _RbnAtmPvcOamStatusVpi_Type(Integer32):
    """Custom type rbnAtmPvcOamStatusVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_RbnAtmPvcOamStatusVpi_Type.__name__ = "Integer32"
_RbnAtmPvcOamStatusVpi_Object = MibTableColumn
rbnAtmPvcOamStatusVpi = _RbnAtmPvcOamStatusVpi_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 19, 1, 1, 1, 3),
    _RbnAtmPvcOamStatusVpi_Type()
)
rbnAtmPvcOamStatusVpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbnAtmPvcOamStatusVpi.setStatus("current")


class _RbnAtmPvcOamStatusVci_Type(Integer32):
    """Custom type rbnAtmPvcOamStatusVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RbnAtmPvcOamStatusVci_Type.__name__ = "Integer32"
_RbnAtmPvcOamStatusVci_Object = MibTableColumn
rbnAtmPvcOamStatusVci = _RbnAtmPvcOamStatusVci_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 19, 1, 1, 1, 4),
    _RbnAtmPvcOamStatusVci_Type()
)
rbnAtmPvcOamStatusVci.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbnAtmPvcOamStatusVci.setStatus("current")


class _RbnAtmPvcOamStatusState_Type(Integer32):
    """Custom type rbnAtmPvcOamStatusState based on Integer32"""
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
        *(("noOam", 1),
          ("oamDownAis", 4),
          ("oamDownLoopback", 3),
          ("oamDownRdi", 5),
          ("oamUp", 2))
    )


_RbnAtmPvcOamStatusState_Type.__name__ = "Integer32"
_RbnAtmPvcOamStatusState_Object = MibTableColumn
rbnAtmPvcOamStatusState = _RbnAtmPvcOamStatusState_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 19, 1, 1, 1, 5),
    _RbnAtmPvcOamStatusState_Type()
)
rbnAtmPvcOamStatusState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnAtmPvcOamStatusState.setStatus("current")
_RbnAtmPvcOamMibConformance_ObjectIdentity = ObjectIdentity
rbnAtmPvcOamMibConformance = _RbnAtmPvcOamMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 19, 2)
)
_RbnAtmPvcOamCompliances_ObjectIdentity = ObjectIdentity
rbnAtmPvcOamCompliances = _RbnAtmPvcOamCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 19, 2, 1)
)
_RbnAtmPvcOamGroups_ObjectIdentity = ObjectIdentity
rbnAtmPvcOamGroups = _RbnAtmPvcOamGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 19, 2, 2)
)

# Managed Objects groups

rbnAtmPvcOamGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 19, 2, 2, 1)
)
rbnAtmPvcOamGroup.setObjects(
    ("RBN-ATM-PVC-OAM-MIB", "rbnAtmPvcOamStatusState")
)
if mibBuilder.loadTexts:
    rbnAtmPvcOamGroup.setStatus("current")


# Notification objects

rbnAtmPvcOamStatusStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2352, 2, 19, 0, 1)
)
rbnAtmPvcOamStatusStateChange.setObjects(
    ("RBN-ATM-PVC-OAM-MIB", "rbnAtmPvcOamStatusState")
)
if mibBuilder.loadTexts:
    rbnAtmPvcOamStatusStateChange.setStatus(
        "current"
    )


# Notifications groups

rbnAtmPvcOamNotifyGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 19, 2, 2, 2)
)
rbnAtmPvcOamNotifyGroup.setObjects(
    ("RBN-ATM-PVC-OAM-MIB", "rbnAtmPvcOamStatusStateChange")
)
if mibBuilder.loadTexts:
    rbnAtmPvcOamNotifyGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

rbnAtmPvcOamCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2352, 2, 19, 2, 1, 1)
)
if mibBuilder.loadTexts:
    rbnAtmPvcOamCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RBN-ATM-PVC-OAM-MIB",
    **{"rbnAtmPvcOamMib": rbnAtmPvcOamMib,
       "rbnAtmPvcOamMibNotifications": rbnAtmPvcOamMibNotifications,
       "rbnAtmPvcOamStatusStateChange": rbnAtmPvcOamStatusStateChange,
       "rbnAtmPvcOamMibObjects": rbnAtmPvcOamMibObjects,
       "rbnAtmPvcOamStatusTable": rbnAtmPvcOamStatusTable,
       "rbnAtmPvcOamStatusEntry": rbnAtmPvcOamStatusEntry,
       "rbnAtmPvcOamStatusSlot": rbnAtmPvcOamStatusSlot,
       "rbnAtmPvcOamStatusPort": rbnAtmPvcOamStatusPort,
       "rbnAtmPvcOamStatusVpi": rbnAtmPvcOamStatusVpi,
       "rbnAtmPvcOamStatusVci": rbnAtmPvcOamStatusVci,
       "rbnAtmPvcOamStatusState": rbnAtmPvcOamStatusState,
       "rbnAtmPvcOamMibConformance": rbnAtmPvcOamMibConformance,
       "rbnAtmPvcOamCompliances": rbnAtmPvcOamCompliances,
       "rbnAtmPvcOamCompliance": rbnAtmPvcOamCompliance,
       "rbnAtmPvcOamGroups": rbnAtmPvcOamGroups,
       "rbnAtmPvcOamGroup": rbnAtmPvcOamGroup,
       "rbnAtmPvcOamNotifyGroup": rbnAtmPvcOamNotifyGroup}
)
