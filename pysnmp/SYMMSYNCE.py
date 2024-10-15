# SNMP MIB module (SYMMSYNCE) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SYMMSYNCE
# Produced by pysmi-1.5.4 at Mon Oct 14 22:59:56 2024
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

(entPhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalIndex")

(ifIndex,
 ifNumber) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex",
    "ifNumber")

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

(EnableValue,
 symmPhysicalSignal) = mibBuilder.importSymbols(
    "SYMM-COMMON-SMI",
    "EnableValue",
    "symmPhysicalSignal")


# MODULE-IDENTITY

symmSyncE = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 8)
)
symmSyncE.setRevisions(
        ("2011-02-24 17:47",)
)


# Types definitions



class SYNCEPQLMODE(Integer32):
    """Custom type SYNCEPQLMODE based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bidirectional", 1),
          ("unidirectional", 2))
    )




# TEXTUAL-CONVENTIONS



class DateAndTime(OctetString, TextualConvention):
    status = "current"
    displayHint = "2d-1d-1d,1d:1d:1d.1d,1a1d:1d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(11, 11),
    )



class TLatAndLon(OctetString, TextualConvention):
    status = "current"
    displayHint = "1a1d:1d:1d.1d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )



class TAntHeight(OctetString, TextualConvention):
    status = "current"
    displayHint = "1a2d.1d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )



class TLocalTimeOffset(OctetString, TextualConvention):
    status = "current"
    displayHint = "1a1d:1d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )



class TSsm(Integer32, TextualConvention):
    status = "current"
    displayHint = "x"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



# MIB Managed Objects in the order of their OIDs

_SyncEStatus_ObjectIdentity = ObjectIdentity
syncEStatus = _SyncEStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 8, 1)
)
_SyncEOutputStatusTable_Object = MibTable
syncEOutputStatusTable = _SyncEOutputStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 8, 1, 1)
)
if mibBuilder.loadTexts:
    syncEOutputStatusTable.setStatus("current")
_SyncEOutputStatusEntry_Object = MibTableRow
syncEOutputStatusEntry = _SyncEOutputStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 8, 1, 1, 1)
)
syncEOutputStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "SYMMSYNCE", "syncEOutputStatusIndex"),
)
if mibBuilder.loadTexts:
    syncEOutputStatusEntry.setStatus("current")


class _SyncEOutputStatusIndex_Type(Integer32):
    """Custom type syncEOutputStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_SyncEOutputStatusIndex_Type.__name__ = "Integer32"
_SyncEOutputStatusIndex_Object = MibTableColumn
syncEOutputStatusIndex = _SyncEOutputStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 8, 1, 1, 1, 1),
    _SyncEOutputStatusIndex_Type()
)
syncEOutputStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    syncEOutputStatusIndex.setStatus("current")
_SyncEOutputEsmcStatus_Type = DisplayString
_SyncEOutputEsmcStatus_Object = MibTableColumn
syncEOutputEsmcStatus = _SyncEOutputEsmcStatus_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 8, 1, 1, 1, 2),
    _SyncEOutputEsmcStatus_Type()
)
syncEOutputEsmcStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syncEOutputEsmcStatus.setStatus("current")
_SyncEOutputStatusRxQL_Type = Integer32
_SyncEOutputStatusRxQL_Object = MibTableColumn
syncEOutputStatusRxQL = _SyncEOutputStatusRxQL_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 8, 1, 1, 1, 3),
    _SyncEOutputStatusRxQL_Type()
)
syncEOutputStatusRxQL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syncEOutputStatusRxQL.setStatus("current")
_SyncEOutputStatusTxQL_Type = Integer32
_SyncEOutputStatusTxQL_Object = MibTableColumn
syncEOutputStatusTxQL = _SyncEOutputStatusTxQL_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 8, 1, 1, 1, 4),
    _SyncEOutputStatusTxQL_Type()
)
syncEOutputStatusTxQL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syncEOutputStatusTxQL.setStatus("current")
_SyncEConfig_ObjectIdentity = ObjectIdentity
syncEConfig = _SyncEConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 8, 2)
)
_SyncEOutputConfigTable_Object = MibTable
syncEOutputConfigTable = _SyncEOutputConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 8, 2, 1)
)
if mibBuilder.loadTexts:
    syncEOutputConfigTable.setStatus("current")
_SyncEOutputConfigEntry_Object = MibTableRow
syncEOutputConfigEntry = _SyncEOutputConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 8, 2, 1, 1)
)
syncEOutputConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "SYMMSYNCE", "syncEOutputConfigIndex"),
)
if mibBuilder.loadTexts:
    syncEOutputConfigEntry.setStatus("current")


class _SyncEOutputConfigIndex_Type(Integer32):
    """Custom type syncEOutputConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_SyncEOutputConfigIndex_Type.__name__ = "Integer32"
_SyncEOutputConfigIndex_Object = MibTableColumn
syncEOutputConfigIndex = _SyncEOutputConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 8, 2, 1, 1, 1),
    _SyncEOutputConfigIndex_Type()
)
syncEOutputConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    syncEOutputConfigIndex.setStatus("current")


class _SyncEOutputEsmcState_Type(EnableValue):
    """Custom type syncEOutputEsmcState based on EnableValue"""
    defaultValue = 2


_SyncEOutputEsmcState_Object = MibTableColumn
syncEOutputEsmcState = _SyncEOutputEsmcState_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 8, 2, 1, 1, 2),
    _SyncEOutputEsmcState_Type()
)
syncEOutputEsmcState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syncEOutputEsmcState.setStatus("current")


class _SyncEOutputQLState_Type(EnableValue):
    """Custom type syncEOutputQLState based on EnableValue"""
    defaultValue = 2


_SyncEOutputQLState_Object = MibTableColumn
syncEOutputQLState = _SyncEOutputQLState_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 8, 2, 1, 1, 3),
    _SyncEOutputQLState_Type()
)
syncEOutputQLState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syncEOutputQLState.setStatus("current")


class _SyncEOutputQLMode_Type(SYNCEPQLMODE):
    """Custom type syncEOutputQLMode based on SYNCEPQLMODE"""
    defaultValue = 1


_SyncEOutputQLMode_Object = MibTableColumn
syncEOutputQLMode = _SyncEOutputQLMode_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 8, 2, 1, 1, 4),
    _SyncEOutputQLMode_Type()
)
syncEOutputQLMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syncEOutputQLMode.setStatus("current")
_SyncEConformance_ObjectIdentity = ObjectIdentity
syncEConformance = _SyncEConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 8, 3)
)
if mibBuilder.loadTexts:
    syncEConformance.setStatus("current")
_SyncECompliances_ObjectIdentity = ObjectIdentity
syncECompliances = _SyncECompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 8, 3, 1)
)
_SyncEUocGroups_ObjectIdentity = ObjectIdentity
syncEUocGroups = _SyncEUocGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 8, 3, 2)
)

# Managed Objects groups

syncEOutputStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 8, 3, 2, 1)
)
syncEOutputStatusGroup.setObjects(
      *(("SYMMSYNCE", "syncEOutputEsmcStatus"),
        ("SYMMSYNCE", "syncEOutputStatusRxQL"),
        ("SYMMSYNCE", "syncEOutputStatusTxQL"))
)
if mibBuilder.loadTexts:
    syncEOutputStatusGroup.setStatus("current")

syncEConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 8, 3, 2, 2)
)
syncEConfigGroup.setObjects(
      *(("SYMMSYNCE", "syncEOutputEsmcState"),
        ("SYMMSYNCE", "syncEOutputQLState"),
        ("SYMMSYNCE", "syncEOutputQLMode"))
)
if mibBuilder.loadTexts:
    syncEConfigGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

syncEBasicCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 8, 3, 1, 1)
)
if mibBuilder.loadTexts:
    syncEBasicCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SYMMSYNCE",
    **{"SYNCEPQLMODE": SYNCEPQLMODE,
       "DateAndTime": DateAndTime,
       "TLatAndLon": TLatAndLon,
       "TAntHeight": TAntHeight,
       "TLocalTimeOffset": TLocalTimeOffset,
       "TSsm": TSsm,
       "symmSyncE": symmSyncE,
       "syncEStatus": syncEStatus,
       "syncEOutputStatusTable": syncEOutputStatusTable,
       "syncEOutputStatusEntry": syncEOutputStatusEntry,
       "syncEOutputStatusIndex": syncEOutputStatusIndex,
       "syncEOutputEsmcStatus": syncEOutputEsmcStatus,
       "syncEOutputStatusRxQL": syncEOutputStatusRxQL,
       "syncEOutputStatusTxQL": syncEOutputStatusTxQL,
       "syncEConfig": syncEConfig,
       "syncEOutputConfigTable": syncEOutputConfigTable,
       "syncEOutputConfigEntry": syncEOutputConfigEntry,
       "syncEOutputConfigIndex": syncEOutputConfigIndex,
       "syncEOutputEsmcState": syncEOutputEsmcState,
       "syncEOutputQLState": syncEOutputQLState,
       "syncEOutputQLMode": syncEOutputQLMode,
       "syncEConformance": syncEConformance,
       "syncECompliances": syncECompliances,
       "syncEBasicCompliance": syncEBasicCompliance,
       "syncEUocGroups": syncEUocGroups,
       "syncEOutputStatusGroup": syncEOutputStatusGroup,
       "syncEConfigGroup": syncEConfigGroup}
)
