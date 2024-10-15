# SNMP MIB module (NET-SNMP-EXTEND-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NET-SNMP-EXTEND-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:25:22 2024
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

(nsExtensions,) = mibBuilder.importSymbols(
    "NET-SNMP-AGENT-MIB",
    "nsExtensions")

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
 StorageType,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "TextualConvention")


# MODULE-IDENTITY

netSnmpExtendMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8072, 1, 3, 1)
)
netSnmpExtendMIB.setRevisions(
        ("2010-03-17 00:00",
         "2004-05-08 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NsExtendObjects_ObjectIdentity = ObjectIdentity
nsExtendObjects = _NsExtendObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8072, 1, 3, 2)
)
_NsExtendNumEntries_Type = Integer32
_NsExtendNumEntries_Object = MibScalar
nsExtendNumEntries = _NsExtendNumEntries_Object(
    (1, 3, 6, 1, 4, 1, 8072, 1, 3, 2, 1),
    _NsExtendNumEntries_Type()
)
nsExtendNumEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsExtendNumEntries.setStatus("current")
_NsExtendConfigTable_Object = MibTable
nsExtendConfigTable = _NsExtendConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 8072, 1, 3, 2, 2)
)
if mibBuilder.loadTexts:
    nsExtendConfigTable.setStatus("current")
_NsExtendConfigEntry_Object = MibTableRow
nsExtendConfigEntry = _NsExtendConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 8072, 1, 3, 2, 2, 1)
)
nsExtendConfigEntry.setIndexNames(
    (0, "NET-SNMP-EXTEND-MIB", "nsExtendToken"),
)
if mibBuilder.loadTexts:
    nsExtendConfigEntry.setStatus("current")
_NsExtendToken_Type = DisplayString
_NsExtendToken_Object = MibTableColumn
nsExtendToken = _NsExtendToken_Object(
    (1, 3, 6, 1, 4, 1, 8072, 1, 3, 2, 2, 1, 1),
    _NsExtendToken_Type()
)
nsExtendToken.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nsExtendToken.setStatus("current")
_NsExtendCommand_Type = DisplayString
_NsExtendCommand_Object = MibTableColumn
nsExtendCommand = _NsExtendCommand_Object(
    (1, 3, 6, 1, 4, 1, 8072, 1, 3, 2, 2, 1, 2),
    _NsExtendCommand_Type()
)
nsExtendCommand.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsExtendCommand.setStatus("current")


class _NsExtendArgs_Type(DisplayString):
    """Custom type nsExtendArgs based on DisplayString"""
    defaultHexValue = ""


_NsExtendArgs_Object = MibTableColumn
nsExtendArgs = _NsExtendArgs_Object(
    (1, 3, 6, 1, 4, 1, 8072, 1, 3, 2, 2, 1, 3),
    _NsExtendArgs_Type()
)
nsExtendArgs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsExtendArgs.setStatus("current")


class _NsExtendInput_Type(DisplayString):
    """Custom type nsExtendInput based on DisplayString"""
    defaultHexValue = ""


_NsExtendInput_Object = MibTableColumn
nsExtendInput = _NsExtendInput_Object(
    (1, 3, 6, 1, 4, 1, 8072, 1, 3, 2, 2, 1, 4),
    _NsExtendInput_Type()
)
nsExtendInput.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsExtendInput.setStatus("current")


class _NsExtendCacheTime_Type(Integer32):
    """Custom type nsExtendCacheTime based on Integer32"""
    defaultValue = 5


_NsExtendCacheTime_Object = MibTableColumn
nsExtendCacheTime = _NsExtendCacheTime_Object(
    (1, 3, 6, 1, 4, 1, 8072, 1, 3, 2, 2, 1, 5),
    _NsExtendCacheTime_Type()
)
nsExtendCacheTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsExtendCacheTime.setStatus("current")


class _NsExtendExecType_Type(Integer32):
    """Custom type nsExtendExecType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("exec", 1),
          ("shell", 2))
    )


_NsExtendExecType_Type.__name__ = "Integer32"
_NsExtendExecType_Object = MibTableColumn
nsExtendExecType = _NsExtendExecType_Object(
    (1, 3, 6, 1, 4, 1, 8072, 1, 3, 2, 2, 1, 6),
    _NsExtendExecType_Type()
)
nsExtendExecType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsExtendExecType.setStatus("current")


class _NsExtendRunType_Type(Integer32):
    """Custom type nsExtendRunType based on Integer32"""
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
        *(("run-command", 3),
          ("run-on-read", 1),
          ("run-on-set", 2))
    )


_NsExtendRunType_Type.__name__ = "Integer32"
_NsExtendRunType_Object = MibTableColumn
nsExtendRunType = _NsExtendRunType_Object(
    (1, 3, 6, 1, 4, 1, 8072, 1, 3, 2, 2, 1, 7),
    _NsExtendRunType_Type()
)
nsExtendRunType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsExtendRunType.setStatus("current")


class _NsExtendStorage_Type(StorageType):
    """Custom type nsExtendStorage based on StorageType"""


_NsExtendStorage_Object = MibTableColumn
nsExtendStorage = _NsExtendStorage_Object(
    (1, 3, 6, 1, 4, 1, 8072, 1, 3, 2, 2, 1, 20),
    _NsExtendStorage_Type()
)
nsExtendStorage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsExtendStorage.setStatus("current")
_NsExtendStatus_Type = RowStatus
_NsExtendStatus_Object = MibTableColumn
nsExtendStatus = _NsExtendStatus_Object(
    (1, 3, 6, 1, 4, 1, 8072, 1, 3, 2, 2, 1, 21),
    _NsExtendStatus_Type()
)
nsExtendStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsExtendStatus.setStatus("current")
_NsExtendOutput1Table_Object = MibTable
nsExtendOutput1Table = _NsExtendOutput1Table_Object(
    (1, 3, 6, 1, 4, 1, 8072, 1, 3, 2, 3)
)
if mibBuilder.loadTexts:
    nsExtendOutput1Table.setStatus("current")
_NsExtendOutput1Entry_Object = MibTableRow
nsExtendOutput1Entry = _NsExtendOutput1Entry_Object(
    (1, 3, 6, 1, 4, 1, 8072, 1, 3, 2, 3, 1)
)
if mibBuilder.loadTexts:
    nsExtendOutput1Entry.setStatus("current")
_NsExtendOutput1Line_Type = DisplayString
_NsExtendOutput1Line_Object = MibTableColumn
nsExtendOutput1Line = _NsExtendOutput1Line_Object(
    (1, 3, 6, 1, 4, 1, 8072, 1, 3, 2, 3, 1, 1),
    _NsExtendOutput1Line_Type()
)
nsExtendOutput1Line.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsExtendOutput1Line.setStatus("current")
_NsExtendOutputFull_Type = DisplayString
_NsExtendOutputFull_Object = MibTableColumn
nsExtendOutputFull = _NsExtendOutputFull_Object(
    (1, 3, 6, 1, 4, 1, 8072, 1, 3, 2, 3, 1, 2),
    _NsExtendOutputFull_Type()
)
nsExtendOutputFull.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsExtendOutputFull.setStatus("current")
_NsExtendOutNumLines_Type = Integer32
_NsExtendOutNumLines_Object = MibTableColumn
nsExtendOutNumLines = _NsExtendOutNumLines_Object(
    (1, 3, 6, 1, 4, 1, 8072, 1, 3, 2, 3, 1, 3),
    _NsExtendOutNumLines_Type()
)
nsExtendOutNumLines.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsExtendOutNumLines.setStatus("current")
_NsExtendResult_Type = Integer32
_NsExtendResult_Object = MibTableColumn
nsExtendResult = _NsExtendResult_Object(
    (1, 3, 6, 1, 4, 1, 8072, 1, 3, 2, 3, 1, 4),
    _NsExtendResult_Type()
)
nsExtendResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsExtendResult.setStatus("current")
_NsExtendOutput2Table_Object = MibTable
nsExtendOutput2Table = _NsExtendOutput2Table_Object(
    (1, 3, 6, 1, 4, 1, 8072, 1, 3, 2, 4)
)
if mibBuilder.loadTexts:
    nsExtendOutput2Table.setStatus("current")
_NsExtendOutput2Entry_Object = MibTableRow
nsExtendOutput2Entry = _NsExtendOutput2Entry_Object(
    (1, 3, 6, 1, 4, 1, 8072, 1, 3, 2, 4, 1)
)
nsExtendOutput2Entry.setIndexNames(
    (0, "NET-SNMP-EXTEND-MIB", "nsExtendToken"),
    (0, "NET-SNMP-EXTEND-MIB", "nsExtendLineIndex"),
)
if mibBuilder.loadTexts:
    nsExtendOutput2Entry.setStatus("current")


class _NsExtendLineIndex_Type(Integer32):
    """Custom type nsExtendLineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_NsExtendLineIndex_Type.__name__ = "Integer32"
_NsExtendLineIndex_Object = MibTableColumn
nsExtendLineIndex = _NsExtendLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 8072, 1, 3, 2, 4, 1, 1),
    _NsExtendLineIndex_Type()
)
nsExtendLineIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nsExtendLineIndex.setStatus("current")
_NsExtendOutLine_Type = DisplayString
_NsExtendOutLine_Object = MibTableColumn
nsExtendOutLine = _NsExtendOutLine_Object(
    (1, 3, 6, 1, 4, 1, 8072, 1, 3, 2, 4, 1, 2),
    _NsExtendOutLine_Type()
)
nsExtendOutLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsExtendOutLine.setStatus("current")
_NsExtendGroups_ObjectIdentity = ObjectIdentity
nsExtendGroups = _NsExtendGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8072, 1, 3, 3)
)
nsExtendConfigEntry.registerAugmentions(
    ("NET-SNMP-EXTEND-MIB",
     "nsExtendOutput1Entry")
)
nsExtendOutput1Entry.setIndexNames(*nsExtendConfigEntry.getIndexNames())

# Managed Objects groups

nsExtendConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8072, 1, 3, 3, 1)
)
nsExtendConfigGroup.setObjects(
      *(("NET-SNMP-EXTEND-MIB", "nsExtendCommand"),
        ("NET-SNMP-EXTEND-MIB", "nsExtendArgs"),
        ("NET-SNMP-EXTEND-MIB", "nsExtendInput"),
        ("NET-SNMP-EXTEND-MIB", "nsExtendCacheTime"),
        ("NET-SNMP-EXTEND-MIB", "nsExtendExecType"),
        ("NET-SNMP-EXTEND-MIB", "nsExtendRunType"),
        ("NET-SNMP-EXTEND-MIB", "nsExtendStorage"),
        ("NET-SNMP-EXTEND-MIB", "nsExtendStatus"),
        ("NET-SNMP-EXTEND-MIB", "nsExtendNumEntries"))
)
if mibBuilder.loadTexts:
    nsExtendConfigGroup.setStatus("current")

nsExtendOutputGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8072, 1, 3, 3, 2)
)
nsExtendOutputGroup.setObjects(
      *(("NET-SNMP-EXTEND-MIB", "nsExtendOutNumLines"),
        ("NET-SNMP-EXTEND-MIB", "nsExtendResult"),
        ("NET-SNMP-EXTEND-MIB", "nsExtendOutLine"),
        ("NET-SNMP-EXTEND-MIB", "nsExtendOutput1Line"),
        ("NET-SNMP-EXTEND-MIB", "nsExtendOutputFull"))
)
if mibBuilder.loadTexts:
    nsExtendOutputGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NET-SNMP-EXTEND-MIB",
    **{"netSnmpExtendMIB": netSnmpExtendMIB,
       "nsExtendObjects": nsExtendObjects,
       "nsExtendNumEntries": nsExtendNumEntries,
       "nsExtendConfigTable": nsExtendConfigTable,
       "nsExtendConfigEntry": nsExtendConfigEntry,
       "nsExtendToken": nsExtendToken,
       "nsExtendCommand": nsExtendCommand,
       "nsExtendArgs": nsExtendArgs,
       "nsExtendInput": nsExtendInput,
       "nsExtendCacheTime": nsExtendCacheTime,
       "nsExtendExecType": nsExtendExecType,
       "nsExtendRunType": nsExtendRunType,
       "nsExtendStorage": nsExtendStorage,
       "nsExtendStatus": nsExtendStatus,
       "nsExtendOutput1Table": nsExtendOutput1Table,
       "nsExtendOutput1Entry": nsExtendOutput1Entry,
       "nsExtendOutput1Line": nsExtendOutput1Line,
       "nsExtendOutputFull": nsExtendOutputFull,
       "nsExtendOutNumLines": nsExtendOutNumLines,
       "nsExtendResult": nsExtendResult,
       "nsExtendOutput2Table": nsExtendOutput2Table,
       "nsExtendOutput2Entry": nsExtendOutput2Entry,
       "nsExtendLineIndex": nsExtendLineIndex,
       "nsExtendOutLine": nsExtendOutLine,
       "nsExtendGroups": nsExtendGroups,
       "nsExtendConfigGroup": nsExtendConfigGroup,
       "nsExtendOutputGroup": nsExtendOutputGroup}
)
