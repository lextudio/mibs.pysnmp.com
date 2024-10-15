# SNMP MIB module (DS3-3COM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DS3-3COM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:33:31 2024
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
 experimental,
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
    "experimental",
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

_Usr_ObjectIdentity = ObjectIdentity
usr = _Usr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429)
)
_Nas_ObjectIdentity = ObjectIdentity
nas = _Nas_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1)
)
_Ds3_ObjectIdentity = ObjectIdentity
ds3 = _Ds3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 44)
)
_Ds3Cfg_ObjectIdentity = ObjectIdentity
ds3Cfg = _Ds3Cfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 44, 1)
)
_Ds3CfgTable_Object = MibTable
ds3CfgTable = _Ds3CfgTable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 44, 1, 1)
)
if mibBuilder.loadTexts:
    ds3CfgTable.setStatus("mandatory")
_Ds3CfgEntry_Object = MibTableRow
ds3CfgEntry = _Ds3CfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 44, 1, 1, 1)
)
ds3CfgEntry.setIndexNames(
    (0, "DS3-3COM-MIB", "ds3CfgIndex"),
)
if mibBuilder.loadTexts:
    ds3CfgEntry.setStatus("mandatory")
_Ds3CfgIndex_Type = Integer32
_Ds3CfgIndex_Object = MibTableColumn
ds3CfgIndex = _Ds3CfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 44, 1, 1, 1, 1),
    _Ds3CfgIndex_Type()
)
ds3CfgIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds3CfgIndex.setStatus("mandatory")


class _Ds3CfgXmitLineBuildOut_Type(Integer32):
    """Custom type ds3CfgXmitLineBuildOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fourHundredFifty", 2),
          ("twoHundredTwentyFive", 1))
    )


_Ds3CfgXmitLineBuildOut_Type.__name__ = "Integer32"
_Ds3CfgXmitLineBuildOut_Object = MibTableColumn
ds3CfgXmitLineBuildOut = _Ds3CfgXmitLineBuildOut_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 44, 1, 1, 1, 2),
    _Ds3CfgXmitLineBuildOut_Type()
)
ds3CfgXmitLineBuildOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds3CfgXmitLineBuildOut.setStatus("mandatory")


class _Ds3CfgMonitorPortSource_Type(Integer32):
    """Custom type ds3CfgMonitorPortSource based on Integer32"""
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
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29)
        )
    )
    namedValues = NamedValues(
        *(("spanBITS", 29),
          ("spanLine1", 1),
          ("spanLine10", 10),
          ("spanLine11", 11),
          ("spanLine12", 12),
          ("spanLine13", 13),
          ("spanLine14", 14),
          ("spanLine15", 15),
          ("spanLine16", 16),
          ("spanLine17", 17),
          ("spanLine18", 18),
          ("spanLine19", 19),
          ("spanLine2", 2),
          ("spanLine20", 20),
          ("spanLine21", 21),
          ("spanLine22", 22),
          ("spanLine23", 23),
          ("spanLine24", 24),
          ("spanLine25", 25),
          ("spanLine26", 26),
          ("spanLine27", 27),
          ("spanLine28", 28),
          ("spanLine3", 3),
          ("spanLine4", 4),
          ("spanLine5", 5),
          ("spanLine6", 6),
          ("spanLine7", 7),
          ("spanLine8", 8),
          ("spanLine9", 9))
    )


_Ds3CfgMonitorPortSource_Type.__name__ = "Integer32"
_Ds3CfgMonitorPortSource_Object = MibTableColumn
ds3CfgMonitorPortSource = _Ds3CfgMonitorPortSource_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 44, 1, 1, 1, 3),
    _Ds3CfgMonitorPortSource_Type()
)
ds3CfgMonitorPortSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds3CfgMonitorPortSource.setStatus("mandatory")
_Ds3Current_ObjectIdentity = ObjectIdentity
ds3Current = _Ds3Current_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 44, 2)
)
_Ds3CurrentTable_Object = MibTable
ds3CurrentTable = _Ds3CurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 44, 2, 1)
)
if mibBuilder.loadTexts:
    ds3CurrentTable.setStatus("mandatory")
_Ds3CurrentEntry_Object = MibTableRow
ds3CurrentEntry = _Ds3CurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 44, 2, 1, 1)
)
ds3CurrentEntry.setIndexNames(
    (0, "DS3-3COM-MIB", "ds3CurrentIndex"),
)
if mibBuilder.loadTexts:
    ds3CurrentEntry.setStatus("mandatory")
_Ds3CurrentIndex_Type = Integer32
_Ds3CurrentIndex_Object = MibTableColumn
ds3CurrentIndex = _Ds3CurrentIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 44, 2, 1, 1, 1),
    _Ds3CurrentIndex_Type()
)
ds3CurrentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3CurrentIndex.setStatus("mandatory")
_Ds3CurrentFCPs_Type = Gauge32
_Ds3CurrentFCPs_Object = MibTableColumn
ds3CurrentFCPs = _Ds3CurrentFCPs_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 44, 2, 1, 1, 2),
    _Ds3CurrentFCPs_Type()
)
ds3CurrentFCPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3CurrentFCPs.setStatus("mandatory")
_Ds3CurrentFCCPs_Type = Gauge32
_Ds3CurrentFCCPs_Object = MibTableColumn
ds3CurrentFCCPs = _Ds3CurrentFCCPs_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 44, 2, 1, 1, 3),
    _Ds3CurrentFCCPs_Type()
)
ds3CurrentFCCPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3CurrentFCCPs.setStatus("mandatory")
_Ds3CurrentSESLs_Type = Gauge32
_Ds3CurrentSESLs_Object = MibTableColumn
ds3CurrentSESLs = _Ds3CurrentSESLs_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 44, 2, 1, 1, 4),
    _Ds3CurrentSESLs_Type()
)
ds3CurrentSESLs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3CurrentSESLs.setStatus("mandatory")
_Ds3CurrentUASCPs_Type = Gauge32
_Ds3CurrentUASCPs_Object = MibTableColumn
ds3CurrentUASCPs = _Ds3CurrentUASCPs_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 44, 2, 1, 1, 5),
    _Ds3CurrentUASCPs_Type()
)
ds3CurrentUASCPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3CurrentUASCPs.setStatus("mandatory")
_Ds3Interval_ObjectIdentity = ObjectIdentity
ds3Interval = _Ds3Interval_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 44, 3)
)
_Ds3IntervalTable_Object = MibTable
ds3IntervalTable = _Ds3IntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 44, 3, 1)
)
if mibBuilder.loadTexts:
    ds3IntervalTable.setStatus("mandatory")
_Ds3IntervalEntry_Object = MibTableRow
ds3IntervalEntry = _Ds3IntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 44, 3, 1, 1)
)
ds3IntervalEntry.setIndexNames(
    (0, "DS3-3COM-MIB", "ds3IntervalIndex"),
    (0, "DS3-3COM-MIB", "ds3IntervalNumber"),
)
if mibBuilder.loadTexts:
    ds3IntervalEntry.setStatus("mandatory")
_Ds3IntervalIndex_Type = Integer32
_Ds3IntervalIndex_Object = MibTableColumn
ds3IntervalIndex = _Ds3IntervalIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 44, 3, 1, 1, 1),
    _Ds3IntervalIndex_Type()
)
ds3IntervalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3IntervalIndex.setStatus("mandatory")


class _Ds3IntervalNumber_Type(Integer32):
    """Custom type ds3IntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_Ds3IntervalNumber_Type.__name__ = "Integer32"
_Ds3IntervalNumber_Object = MibTableColumn
ds3IntervalNumber = _Ds3IntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 44, 3, 1, 1, 2),
    _Ds3IntervalNumber_Type()
)
ds3IntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3IntervalNumber.setStatus("mandatory")
_Ds3IntervalSESLs_Type = Gauge32
_Ds3IntervalSESLs_Object = MibTableColumn
ds3IntervalSESLs = _Ds3IntervalSESLs_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 44, 3, 1, 1, 3),
    _Ds3IntervalSESLs_Type()
)
ds3IntervalSESLs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3IntervalSESLs.setStatus("mandatory")
_Ds3IntervalCVCPs_Type = Gauge32
_Ds3IntervalCVCPs_Object = MibTableColumn
ds3IntervalCVCPs = _Ds3IntervalCVCPs_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 44, 3, 1, 1, 4),
    _Ds3IntervalCVCPs_Type()
)
ds3IntervalCVCPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3IntervalCVCPs.setStatus("mandatory")
_Ds3IntervalUASCPs_Type = Gauge32
_Ds3IntervalUASCPs_Object = MibTableColumn
ds3IntervalUASCPs = _Ds3IntervalUASCPs_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 44, 3, 1, 1, 5),
    _Ds3IntervalUASCPs_Type()
)
ds3IntervalUASCPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3IntervalUASCPs.setStatus("mandatory")
_Ds3Total_ObjectIdentity = ObjectIdentity
ds3Total = _Ds3Total_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 44, 4)
)
_Ds3TotalTable_Object = MibTable
ds3TotalTable = _Ds3TotalTable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 44, 4, 1)
)
if mibBuilder.loadTexts:
    ds3TotalTable.setStatus("mandatory")
_Ds3TotalEntry_Object = MibTableRow
ds3TotalEntry = _Ds3TotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 44, 4, 1, 1)
)
ds3TotalEntry.setIndexNames(
    (0, "DS3-3COM-MIB", "ds3TotalIndex"),
)
if mibBuilder.loadTexts:
    ds3TotalEntry.setStatus("mandatory")
_Ds3TotalIndex_Type = Integer32
_Ds3TotalIndex_Object = MibTableColumn
ds3TotalIndex = _Ds3TotalIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 44, 4, 1, 1, 1),
    _Ds3TotalIndex_Type()
)
ds3TotalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3TotalIndex.setStatus("mandatory")
_Ds3TotalSESLs_Type = Gauge32
_Ds3TotalSESLs_Object = MibTableColumn
ds3TotalSESLs = _Ds3TotalSESLs_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 44, 4, 1, 1, 2),
    _Ds3TotalSESLs_Type()
)
ds3TotalSESLs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3TotalSESLs.setStatus("mandatory")
_Ds3TotalCVCPs_Type = Gauge32
_Ds3TotalCVCPs_Object = MibTableColumn
ds3TotalCVCPs = _Ds3TotalCVCPs_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 44, 4, 1, 1, 3),
    _Ds3TotalCVCPs_Type()
)
ds3TotalCVCPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3TotalCVCPs.setStatus("mandatory")
_Ds3TotalUASCPs_Type = Gauge32
_Ds3TotalUASCPs_Object = MibTableColumn
ds3TotalUASCPs = _Ds3TotalUASCPs_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 44, 4, 1, 1, 4),
    _Ds3TotalUASCPs_Type()
)
ds3TotalUASCPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3TotalUASCPs.setStatus("mandatory")
_Ds3TrapEnable_ObjectIdentity = ObjectIdentity
ds3TrapEnable = _Ds3TrapEnable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 44, 5)
)
_Ds3TrapEnableTable_Object = MibTable
ds3TrapEnableTable = _Ds3TrapEnableTable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 44, 5, 1)
)
if mibBuilder.loadTexts:
    ds3TrapEnableTable.setStatus("mandatory")
_Ds3TrapEnableEntry_Object = MibTableRow
ds3TrapEnableEntry = _Ds3TrapEnableEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 44, 5, 1, 1)
)
ds3TrapEnableEntry.setIndexNames(
    (0, "DS3-3COM-MIB", "ds3TrapEnableIndex"),
)
if mibBuilder.loadTexts:
    ds3TrapEnableEntry.setStatus("mandatory")
_Ds3TrapEnableIndex_Type = Integer32
_Ds3TrapEnableIndex_Object = MibTableColumn
ds3TrapEnableIndex = _Ds3TrapEnableIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 44, 5, 1, 1, 1),
    _Ds3TrapEnableIndex_Type()
)
ds3TrapEnableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3TrapEnableIndex.setStatus("mandatory")


class _Ds3LineStatusChangeTE_Type(Integer32):
    """Custom type ds3LineStatusChangeTE based on Integer32"""
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
        *(("disableAll", 2),
          ("enableAll", 4),
          ("enableLog", 3),
          ("enableTrap", 1))
    )


_Ds3LineStatusChangeTE_Type.__name__ = "Integer32"
_Ds3LineStatusChangeTE_Object = MibTableColumn
ds3LineStatusChangeTE = _Ds3LineStatusChangeTE_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 44, 5, 1, 1, 2),
    _Ds3LineStatusChangeTE_Type()
)
ds3LineStatusChangeTE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds3LineStatusChangeTE.setStatus("mandatory")
_Ds3TrapObj_ObjectIdentity = ObjectIdentity
ds3TrapObj = _Ds3TrapObj_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 44, 6)
)
_Ds3TrapObjTable_Object = MibTable
ds3TrapObjTable = _Ds3TrapObjTable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 44, 6, 1)
)
if mibBuilder.loadTexts:
    ds3TrapObjTable.setStatus("mandatory")
_Ds3TrapObjEntry_Object = MibTableRow
ds3TrapObjEntry = _Ds3TrapObjEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 44, 6, 1, 1)
)
ds3TrapObjEntry.setIndexNames(
    (0, "DS3-3COM-MIB", "ds3TrapObjIndex"),
)
if mibBuilder.loadTexts:
    ds3TrapObjEntry.setStatus("mandatory")
_Ds3TrapObjIndex_Type = Integer32
_Ds3TrapObjIndex_Object = MibTableColumn
ds3TrapObjIndex = _Ds3TrapObjIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 44, 6, 1, 1, 1),
    _Ds3TrapObjIndex_Type()
)
ds3TrapObjIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3TrapObjIndex.setStatus("mandatory")


class _Ds3StatusObjString_Type(DisplayString):
    """Custom type ds3StatusObjString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_Ds3StatusObjString_Type.__name__ = "DisplayString"
_Ds3StatusObjString_Object = MibTableColumn
ds3StatusObjString = _Ds3StatusObjString_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 44, 6, 1, 1, 2),
    _Ds3StatusObjString_Type()
)
ds3StatusObjString.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ds3StatusObjString.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DS3-3COM-MIB",
    **{"usr": usr,
       "nas": nas,
       "ds3": ds3,
       "ds3Cfg": ds3Cfg,
       "ds3CfgTable": ds3CfgTable,
       "ds3CfgEntry": ds3CfgEntry,
       "ds3CfgIndex": ds3CfgIndex,
       "ds3CfgXmitLineBuildOut": ds3CfgXmitLineBuildOut,
       "ds3CfgMonitorPortSource": ds3CfgMonitorPortSource,
       "ds3Current": ds3Current,
       "ds3CurrentTable": ds3CurrentTable,
       "ds3CurrentEntry": ds3CurrentEntry,
       "ds3CurrentIndex": ds3CurrentIndex,
       "ds3CurrentFCPs": ds3CurrentFCPs,
       "ds3CurrentFCCPs": ds3CurrentFCCPs,
       "ds3CurrentSESLs": ds3CurrentSESLs,
       "ds3CurrentUASCPs": ds3CurrentUASCPs,
       "ds3Interval": ds3Interval,
       "ds3IntervalTable": ds3IntervalTable,
       "ds3IntervalEntry": ds3IntervalEntry,
       "ds3IntervalIndex": ds3IntervalIndex,
       "ds3IntervalNumber": ds3IntervalNumber,
       "ds3IntervalSESLs": ds3IntervalSESLs,
       "ds3IntervalCVCPs": ds3IntervalCVCPs,
       "ds3IntervalUASCPs": ds3IntervalUASCPs,
       "ds3Total": ds3Total,
       "ds3TotalTable": ds3TotalTable,
       "ds3TotalEntry": ds3TotalEntry,
       "ds3TotalIndex": ds3TotalIndex,
       "ds3TotalSESLs": ds3TotalSESLs,
       "ds3TotalCVCPs": ds3TotalCVCPs,
       "ds3TotalUASCPs": ds3TotalUASCPs,
       "ds3TrapEnable": ds3TrapEnable,
       "ds3TrapEnableTable": ds3TrapEnableTable,
       "ds3TrapEnableEntry": ds3TrapEnableEntry,
       "ds3TrapEnableIndex": ds3TrapEnableIndex,
       "ds3LineStatusChangeTE": ds3LineStatusChangeTE,
       "ds3TrapObj": ds3TrapObj,
       "ds3TrapObjTable": ds3TrapObjTable,
       "ds3TrapObjEntry": ds3TrapObjEntry,
       "ds3TrapObjIndex": ds3TrapObjIndex,
       "ds3StatusObjString": ds3StatusObjString}
)
