# SNMP MIB module (REDSTONE-ACCOUNTING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/REDSTONE-ACCOUNTING-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:46:32 2024
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

(acctngFileEntry,
 acctngSelectionEntry) = mibBuilder.importSymbols(
    "ACCOUNTING-CONTROL-MIB",
    "acctngFileEntry",
    "acctngSelectionEntry")

(rsIfType,) = mibBuilder.importSymbols(
    "REDSTONE-IF-MIB",
    "rsIfType")

(rsMgmt,) = mibBuilder.importSymbols(
    "REDSTONE-SMI",
    "rsMgmt")

(RsAcctngAdminType,
 RsAcctngOperType) = mibBuilder.importSymbols(
    "REDSTONE-TC",
    "RsAcctngAdminType",
    "RsAcctngOperType")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

rsAcctngMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 24)
)
rsAcctngMIB.setRevisions(
        ("1999-01-01 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RsAcctngMIBObjects_ObjectIdentity = ObjectIdentity
rsAcctngMIBObjects = _RsAcctngMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 24, 1)
)
_RsAcctngSelectionControl_ObjectIdentity = ObjectIdentity
rsAcctngSelectionControl = _RsAcctngSelectionControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 24, 1, 1)
)
_RsAcctngSelectionTable_Object = MibTable
rsAcctngSelectionTable = _RsAcctngSelectionTable_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 24, 1, 1, 1)
)
if mibBuilder.loadTexts:
    rsAcctngSelectionTable.setStatus("current")
_RsAcctngSelectionEntry_Object = MibTableRow
rsAcctngSelectionEntry = _RsAcctngSelectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 24, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    rsAcctngSelectionEntry.setStatus("current")


class _RsAcctngSelectionType_Type(Bits):
    """Custom type rsAcctngSelectionType based on Bits"""
    namedValues = NamedValues(
        *(("connectionLessLayer2", 1),
          ("ietfAccountControl", 0))
    )

_RsAcctngSelectionType_Type.__name__ = "Bits"
_RsAcctngSelectionType_Object = MibTableColumn
rsAcctngSelectionType = _RsAcctngSelectionType_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 24, 1, 1, 1, 1, 1),
    _RsAcctngSelectionType_Type()
)
rsAcctngSelectionType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsAcctngSelectionType.setStatus("current")


class _RsAcctngSelectionMode_Type(Integer32):
    """Custom type rsAcctngSelectionMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("absoluteCounterValues", 1),
          ("deltaCounterValues", 2))
    )


_RsAcctngSelectionMode_Type.__name__ = "Integer32"
_RsAcctngSelectionMode_Object = MibTableColumn
rsAcctngSelectionMode = _RsAcctngSelectionMode_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 24, 1, 1, 1, 1, 2),
    _RsAcctngSelectionMode_Type()
)
rsAcctngSelectionMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsAcctngSelectionMode.setStatus("current")
_RsAcctngFileControl_ObjectIdentity = ObjectIdentity
rsAcctngFileControl = _RsAcctngFileControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 24, 1, 2)
)
_RsAcctngFileTable_Object = MibTable
rsAcctngFileTable = _RsAcctngFileTable_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 24, 1, 2, 1)
)
if mibBuilder.loadTexts:
    rsAcctngFileTable.setStatus("current")
_RsAcctngFileEntry_Object = MibTableRow
rsAcctngFileEntry = _RsAcctngFileEntry_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 24, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    rsAcctngFileEntry.setStatus("current")


class _RsAcctngFileXferMode_Type(Integer32):
    """Custom type rsAcctngFileXferMode based on Integer32"""
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
        *(("rsAcctngAutomatedTransfer", 2),
          ("rsAcctngManualTransfer", 1),
          ("rsAcctngRedundantTransfer", 4),
          ("rsAcctngTransferOnFileFull", 3))
    )


_RsAcctngFileXferMode_Type.__name__ = "Integer32"
_RsAcctngFileXferMode_Object = MibTableColumn
rsAcctngFileXferMode = _RsAcctngFileXferMode_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 24, 1, 2, 1, 1, 1),
    _RsAcctngFileXferMode_Type()
)
rsAcctngFileXferMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsAcctngFileXferMode.setStatus("current")
_RsAcctngFileXferIndex_Type = Integer32
_RsAcctngFileXferIndex_Object = MibTableColumn
rsAcctngFileXferIndex = _RsAcctngFileXferIndex_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 24, 1, 2, 1, 1, 2),
    _RsAcctngFileXferIndex_Type()
)
rsAcctngFileXferIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsAcctngFileXferIndex.setStatus("current")
_RsAcctngFileXferSecondaryIndex_Type = Integer32
_RsAcctngFileXferSecondaryIndex_Object = MibTableColumn
rsAcctngFileXferSecondaryIndex = _RsAcctngFileXferSecondaryIndex_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 24, 1, 2, 1, 1, 3),
    _RsAcctngFileXferSecondaryIndex_Type()
)
rsAcctngFileXferSecondaryIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsAcctngFileXferSecondaryIndex.setStatus("current")
_RsAcctngInterfaceControl_ObjectIdentity = ObjectIdentity
rsAcctngInterfaceControl = _RsAcctngInterfaceControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 24, 1, 3)
)
_RsAcctngInterfaceTable_Object = MibTable
rsAcctngInterfaceTable = _RsAcctngInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 24, 1, 3, 1)
)
if mibBuilder.loadTexts:
    rsAcctngInterfaceTable.setStatus("current")
_RsAcctngInterfaceEntry_Object = MibTableRow
rsAcctngInterfaceEntry = _RsAcctngInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 24, 1, 3, 1, 1)
)
rsAcctngInterfaceEntry.setIndexNames(
    (0, "REDSTONE-IF-MIB", "rsIfType"),
)
if mibBuilder.loadTexts:
    rsAcctngInterfaceEntry.setStatus("current")
_RsAcctngInterfaceAdminStatus_Type = RsAcctngAdminType
_RsAcctngInterfaceAdminStatus_Object = MibTableColumn
rsAcctngInterfaceAdminStatus = _RsAcctngInterfaceAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 24, 1, 3, 1, 1, 1),
    _RsAcctngInterfaceAdminStatus_Type()
)
rsAcctngInterfaceAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsAcctngInterfaceAdminStatus.setStatus("current")
_RsAcctngInterfaceOperStatus_Type = RsAcctngOperType
_RsAcctngInterfaceOperStatus_Object = MibTableColumn
rsAcctngInterfaceOperStatus = _RsAcctngInterfaceOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 24, 1, 3, 1, 1, 2),
    _RsAcctngInterfaceOperStatus_Type()
)
rsAcctngInterfaceOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsAcctngInterfaceOperStatus.setStatus("current")
_RsAcctngInterfaceRowStatus_Type = RowStatus
_RsAcctngInterfaceRowStatus_Object = MibTableColumn
rsAcctngInterfaceRowStatus = _RsAcctngInterfaceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 24, 1, 3, 1, 1, 3),
    _RsAcctngInterfaceRowStatus_Type()
)
rsAcctngInterfaceRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsAcctngInterfaceRowStatus.setStatus("current")
_RsAcctngConformance_ObjectIdentity = ObjectIdentity
rsAcctngConformance = _RsAcctngConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 24, 3)
)
_RsAcctngGroups_ObjectIdentity = ObjectIdentity
rsAcctngGroups = _RsAcctngGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 24, 3, 1)
)
_RsAcctngCompliances_ObjectIdentity = ObjectIdentity
rsAcctngCompliances = _RsAcctngCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 24, 3, 2)
)
acctngSelectionEntry.registerAugmentions(
    ("REDSTONE-ACCOUNTING-MIB",
     "rsAcctngSelectionEntry")
)
rsAcctngSelectionEntry.setIndexNames(*acctngSelectionEntry.getIndexNames())
acctngFileEntry.registerAugmentions(
    ("REDSTONE-ACCOUNTING-MIB",
     "rsAcctngFileEntry")
)
rsAcctngFileEntry.setIndexNames(*acctngFileEntry.getIndexNames())

# Managed Objects groups

rsAcctngBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2773, 2, 24, 3, 1, 1)
)
rsAcctngBasicGroup.setObjects(
      *(("REDSTONE-ACCOUNTING-MIB", "rsAcctngSelectionType"),
        ("REDSTONE-ACCOUNTING-MIB", "rsAcctngSelectionMode"),
        ("REDSTONE-ACCOUNTING-MIB", "rsAcctngFileXferMode"),
        ("REDSTONE-ACCOUNTING-MIB", "rsAcctngFileXferIndex"),
        ("REDSTONE-ACCOUNTING-MIB", "rsAcctngInterfaceAdminStatus"),
        ("REDSTONE-ACCOUNTING-MIB", "rsAcctngInterfaceOperStatus"))
)
if mibBuilder.loadTexts:
    rsAcctngBasicGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

rsAcctngCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2773, 2, 24, 3, 2, 1)
)
if mibBuilder.loadTexts:
    rsAcctngCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "REDSTONE-ACCOUNTING-MIB",
    **{"rsAcctngMIB": rsAcctngMIB,
       "rsAcctngMIBObjects": rsAcctngMIBObjects,
       "rsAcctngSelectionControl": rsAcctngSelectionControl,
       "rsAcctngSelectionTable": rsAcctngSelectionTable,
       "rsAcctngSelectionEntry": rsAcctngSelectionEntry,
       "rsAcctngSelectionType": rsAcctngSelectionType,
       "rsAcctngSelectionMode": rsAcctngSelectionMode,
       "rsAcctngFileControl": rsAcctngFileControl,
       "rsAcctngFileTable": rsAcctngFileTable,
       "rsAcctngFileEntry": rsAcctngFileEntry,
       "rsAcctngFileXferMode": rsAcctngFileXferMode,
       "rsAcctngFileXferIndex": rsAcctngFileXferIndex,
       "rsAcctngFileXferSecondaryIndex": rsAcctngFileXferSecondaryIndex,
       "rsAcctngInterfaceControl": rsAcctngInterfaceControl,
       "rsAcctngInterfaceTable": rsAcctngInterfaceTable,
       "rsAcctngInterfaceEntry": rsAcctngInterfaceEntry,
       "rsAcctngInterfaceAdminStatus": rsAcctngInterfaceAdminStatus,
       "rsAcctngInterfaceOperStatus": rsAcctngInterfaceOperStatus,
       "rsAcctngInterfaceRowStatus": rsAcctngInterfaceRowStatus,
       "rsAcctngConformance": rsAcctngConformance,
       "rsAcctngGroups": rsAcctngGroups,
       "rsAcctngBasicGroup": rsAcctngBasicGroup,
       "rsAcctngCompliances": rsAcctngCompliances,
       "rsAcctngCompliance": rsAcctngCompliance}
)
