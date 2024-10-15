# SNMP MIB module (INTEL-DIAG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/INTEL-DIAG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:09:35 2024
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

(mib2ext,) = mibBuilder.importSymbols(
    "INTEL-GEN-MIB",
    "mib2ext")

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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Diag_ObjectIdentity = ObjectIdentity
diag = _Diag_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 4)
)
_DiagList_ObjectIdentity = ObjectIdentity
diagList = _DiagList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 4, 1)
)
_DiagListNumberOfEntries_Type = Integer32
_DiagListNumberOfEntries_Object = MibScalar
diagListNumberOfEntries = _DiagListNumberOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 4, 1, 1),
    _DiagListNumberOfEntries_Type()
)
diagListNumberOfEntries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    diagListNumberOfEntries.setStatus("mandatory")
_DiagListNumberOfErrorEntries_Type = Integer32
_DiagListNumberOfErrorEntries_Object = MibScalar
diagListNumberOfErrorEntries = _DiagListNumberOfErrorEntries_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 4, 1, 2),
    _DiagListNumberOfErrorEntries_Type()
)
diagListNumberOfErrorEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diagListNumberOfErrorEntries.setStatus("mandatory")
_DiagListLastUpdateTime_Type = TimeTicks
_DiagListLastUpdateTime_Object = MibScalar
diagListLastUpdateTime = _DiagListLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 4, 1, 3),
    _DiagListLastUpdateTime_Type()
)
diagListLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diagListLastUpdateTime.setStatus("mandatory")
_DiagListTable_Object = MibTable
diagListTable = _DiagListTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 4, 1, 4)
)
if mibBuilder.loadTexts:
    diagListTable.setStatus("mandatory")
_DiagListEntry_Object = MibTableRow
diagListEntry = _DiagListEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 4, 1, 4, 1)
)
diagListEntry.setIndexNames(
    (0, "INTEL-DIAG-MIB", "diagListIndex"),
)
if mibBuilder.loadTexts:
    diagListEntry.setStatus("mandatory")
_DiagListIndex_Type = Integer32
_DiagListIndex_Object = MibTableColumn
diagListIndex = _DiagListIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 4, 1, 4, 1, 1),
    _DiagListIndex_Type()
)
diagListIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diagListIndex.setStatus("mandatory")


class _DiagListLevel_Type(Integer32):
    """Custom type diagListLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(32,
              64,
              96)
        )
    )
    namedValues = NamedValues(
        *(("error", 64),
          ("fatalError", 96),
          ("warning", 32))
    )


_DiagListLevel_Type.__name__ = "Integer32"
_DiagListLevel_Object = MibTableColumn
diagListLevel = _DiagListLevel_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 4, 1, 4, 1, 2),
    _DiagListLevel_Type()
)
diagListLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diagListLevel.setStatus("mandatory")
_DiagListCode_Type = Integer32
_DiagListCode_Object = MibTableColumn
diagListCode = _DiagListCode_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 4, 1, 4, 1, 3),
    _DiagListCode_Type()
)
diagListCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diagListCode.setStatus("mandatory")
_DiagListIfindex_Type = Integer32
_DiagListIfindex_Object = MibTableColumn
diagListIfindex = _DiagListIfindex_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 4, 1, 4, 1, 4),
    _DiagListIfindex_Type()
)
diagListIfindex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diagListIfindex.setStatus("mandatory")
_DiagListTimeStamp_Type = TimeTicks
_DiagListTimeStamp_Object = MibTableColumn
diagListTimeStamp = _DiagListTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 4, 1, 4, 1, 5),
    _DiagListTimeStamp_Type()
)
diagListTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diagListTimeStamp.setStatus("mandatory")


class _DiagListDescription_Type(DisplayString):
    """Custom type diagListDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(240, 240),
    )


_DiagListDescription_Type.__name__ = "DisplayString"
_DiagListDescription_Object = MibTableColumn
diagListDescription = _DiagListDescription_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 4, 1, 4, 1, 6),
    _DiagListDescription_Type()
)
diagListDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diagListDescription.setStatus("mandatory")


class _DiagListAdvice_Type(DisplayString):
    """Custom type diagListAdvice based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(240, 240),
    )


_DiagListAdvice_Type.__name__ = "DisplayString"
_DiagListAdvice_Object = MibTableColumn
diagListAdvice = _DiagListAdvice_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 4, 1, 4, 1, 7),
    _DiagListAdvice_Type()
)
diagListAdvice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diagListAdvice.setStatus("mandatory")


class _DiagListAutoFixAvailable_Type(Integer32):
    """Custom type diagListAutoFixAvailable based on Integer32"""
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


_DiagListAutoFixAvailable_Type.__name__ = "Integer32"
_DiagListAutoFixAvailable_Object = MibTableColumn
diagListAutoFixAvailable = _DiagListAutoFixAvailable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 4, 1, 4, 1, 8),
    _DiagListAutoFixAvailable_Type()
)
diagListAutoFixAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diagListAutoFixAvailable.setStatus("mandatory")


class _DiagListAutoFixState_Type(OctetString):
    """Custom type diagListAutoFixState based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_DiagListAutoFixState_Type.__name__ = "OctetString"
_DiagListAutoFixState_Object = MibTableColumn
diagListAutoFixState = _DiagListAutoFixState_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 4, 1, 4, 1, 9),
    _DiagListAutoFixState_Type()
)
diagListAutoFixState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    diagListAutoFixState.setStatus("mandatory")
_DiagTest_ObjectIdentity = ObjectIdentity
diagTest = _DiagTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 4, 2)
)
_DiagTestTable_Object = MibTable
diagTestTable = _DiagTestTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 4, 2, 1)
)
if mibBuilder.loadTexts:
    diagTestTable.setStatus("mandatory")
_DiagTestEntry_Object = MibTableRow
diagTestEntry = _DiagTestEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 4, 2, 1, 1)
)
diagTestEntry.setIndexNames(
    (0, "INTEL-DIAG-MIB", "diagTestType"),
)
if mibBuilder.loadTexts:
    diagTestEntry.setStatus("mandatory")
_DiagTestType_Type = Integer32
_DiagTestType_Object = MibTableColumn
diagTestType = _DiagTestType_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 4, 2, 1, 1, 1),
    _DiagTestType_Type()
)
diagTestType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diagTestType.setStatus("mandatory")


class _DiagTestDescription_Type(OctetString):
    """Custom type diagTestDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(40, 40),
    )


_DiagTestDescription_Type.__name__ = "OctetString"
_DiagTestDescription_Object = MibTableColumn
diagTestDescription = _DiagTestDescription_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 4, 2, 1, 1, 2),
    _DiagTestDescription_Type()
)
diagTestDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diagTestDescription.setStatus("mandatory")


class _DiagTestStatus_Type(Integer32):
    """Custom type diagTestStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ready", 1),
          ("test", 2),
          ("testing", 3))
    )


_DiagTestStatus_Type.__name__ = "Integer32"
_DiagTestStatus_Object = MibTableColumn
diagTestStatus = _DiagTestStatus_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 4, 2, 1, 1, 3),
    _DiagTestStatus_Type()
)
diagTestStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    diagTestStatus.setStatus("mandatory")
_DiagAutodetect_ObjectIdentity = ObjectIdentity
diagAutodetect = _DiagAutodetect_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 4, 3)
)
_DiagAutodetectTable_Object = MibTable
diagAutodetectTable = _DiagAutodetectTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 4, 3, 1)
)
if mibBuilder.loadTexts:
    diagAutodetectTable.setStatus("mandatory")
_DiagAutodetectEntry_Object = MibTableRow
diagAutodetectEntry = _DiagAutodetectEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 4, 3, 1, 1)
)
diagAutodetectEntry.setIndexNames(
    (0, "INTEL-DIAG-MIB", "diagAutodetectType"),
    (0, "INTEL-DIAG-MIB", "diagAutodetectIndex1"),
    (0, "INTEL-DIAG-MIB", "diagAutodetectIndex2"),
    (0, "INTEL-DIAG-MIB", "diagAutodetectIndex3"),
)
if mibBuilder.loadTexts:
    diagAutodetectEntry.setStatus("mandatory")
_DiagAutodetectType_Type = Integer32
_DiagAutodetectType_Object = MibTableColumn
diagAutodetectType = _DiagAutodetectType_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 4, 3, 1, 1, 1),
    _DiagAutodetectType_Type()
)
diagAutodetectType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diagAutodetectType.setStatus("mandatory")
_DiagAutodetectIndex1_Type = Integer32
_DiagAutodetectIndex1_Object = MibTableColumn
diagAutodetectIndex1 = _DiagAutodetectIndex1_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 4, 3, 1, 1, 2),
    _DiagAutodetectIndex1_Type()
)
diagAutodetectIndex1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diagAutodetectIndex1.setStatus("mandatory")
_DiagAutodetectIndex2_Type = Integer32
_DiagAutodetectIndex2_Object = MibTableColumn
diagAutodetectIndex2 = _DiagAutodetectIndex2_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 4, 3, 1, 1, 3),
    _DiagAutodetectIndex2_Type()
)
diagAutodetectIndex2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diagAutodetectIndex2.setStatus("mandatory")
_DiagAutodetectIndex3_Type = Integer32
_DiagAutodetectIndex3_Object = MibTableColumn
diagAutodetectIndex3 = _DiagAutodetectIndex3_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 4, 3, 1, 1, 4),
    _DiagAutodetectIndex3_Type()
)
diagAutodetectIndex3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diagAutodetectIndex3.setStatus("mandatory")


class _DiagAutodetectState_Type(Integer32):
    """Custom type diagAutodetectState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("ready", 1),
          ("startTest", 2),
          ("stopTest", 3),
          ("testFailed", 5),
          ("testInProgress", 6),
          ("testSucceeded", 4))
    )


_DiagAutodetectState_Type.__name__ = "Integer32"
_DiagAutodetectState_Object = MibTableColumn
diagAutodetectState = _DiagAutodetectState_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 4, 3, 1, 1, 5),
    _DiagAutodetectState_Type()
)
diagAutodetectState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    diagAutodetectState.setStatus("mandatory")
_DiagAutodetectDuration_Type = Integer32
_DiagAutodetectDuration_Object = MibTableColumn
diagAutodetectDuration = _DiagAutodetectDuration_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 4, 3, 1, 1, 6),
    _DiagAutodetectDuration_Type()
)
diagAutodetectDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diagAutodetectDuration.setStatus("mandatory")
_DiagAutodetectRes1_Type = Counter32
_DiagAutodetectRes1_Object = MibTableColumn
diagAutodetectRes1 = _DiagAutodetectRes1_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 4, 3, 1, 1, 7),
    _DiagAutodetectRes1_Type()
)
diagAutodetectRes1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diagAutodetectRes1.setStatus("mandatory")


class _DiagAutodetectRes2a_Type(OctetString):
    """Custom type diagAutodetectRes2a based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(255, 255),
    )


_DiagAutodetectRes2a_Type.__name__ = "OctetString"
_DiagAutodetectRes2a_Object = MibTableColumn
diagAutodetectRes2a = _DiagAutodetectRes2a_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 4, 3, 1, 1, 8),
    _DiagAutodetectRes2a_Type()
)
diagAutodetectRes2a.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diagAutodetectRes2a.setStatus("mandatory")


class _DiagAutodetectRes2b_Type(OctetString):
    """Custom type diagAutodetectRes2b based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(255, 255),
    )


_DiagAutodetectRes2b_Type.__name__ = "OctetString"
_DiagAutodetectRes2b_Object = MibTableColumn
diagAutodetectRes2b = _DiagAutodetectRes2b_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 4, 3, 1, 1, 9),
    _DiagAutodetectRes2b_Type()
)
diagAutodetectRes2b.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diagAutodetectRes2b.setStatus("mandatory")


class _DiagAutodetectPreInput_Type(OctetString):
    """Custom type diagAutodetectPreInput based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(255, 255),
    )


_DiagAutodetectPreInput_Type.__name__ = "OctetString"
_DiagAutodetectPreInput_Object = MibTableColumn
diagAutodetectPreInput = _DiagAutodetectPreInput_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 4, 3, 1, 1, 10),
    _DiagAutodetectPreInput_Type()
)
diagAutodetectPreInput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    diagAutodetectPreInput.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INTEL-DIAG-MIB",
    **{"diag": diag,
       "diagList": diagList,
       "diagListNumberOfEntries": diagListNumberOfEntries,
       "diagListNumberOfErrorEntries": diagListNumberOfErrorEntries,
       "diagListLastUpdateTime": diagListLastUpdateTime,
       "diagListTable": diagListTable,
       "diagListEntry": diagListEntry,
       "diagListIndex": diagListIndex,
       "diagListLevel": diagListLevel,
       "diagListCode": diagListCode,
       "diagListIfindex": diagListIfindex,
       "diagListTimeStamp": diagListTimeStamp,
       "diagListDescription": diagListDescription,
       "diagListAdvice": diagListAdvice,
       "diagListAutoFixAvailable": diagListAutoFixAvailable,
       "diagListAutoFixState": diagListAutoFixState,
       "diagTest": diagTest,
       "diagTestTable": diagTestTable,
       "diagTestEntry": diagTestEntry,
       "diagTestType": diagTestType,
       "diagTestDescription": diagTestDescription,
       "diagTestStatus": diagTestStatus,
       "diagAutodetect": diagAutodetect,
       "diagAutodetectTable": diagAutodetectTable,
       "diagAutodetectEntry": diagAutodetectEntry,
       "diagAutodetectType": diagAutodetectType,
       "diagAutodetectIndex1": diagAutodetectIndex1,
       "diagAutodetectIndex2": diagAutodetectIndex2,
       "diagAutodetectIndex3": diagAutodetectIndex3,
       "diagAutodetectState": diagAutodetectState,
       "diagAutodetectDuration": diagAutodetectDuration,
       "diagAutodetectRes1": diagAutodetectRes1,
       "diagAutodetectRes2a": diagAutodetectRes2a,
       "diagAutodetectRes2b": diagAutodetectRes2b,
       "diagAutodetectPreInput": diagAutodetectPreInput}
)
