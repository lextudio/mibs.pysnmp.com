# SNMP MIB module (SCA-DIAG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SCA-DIAG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:49:51 2024
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

(scanet,) = mibBuilder.importSymbols(
    "SCANET-MIB",
    "scanet")

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
    (1, 3, 6, 1, 4, 1, 208, 47)
)
_DiagList_ObjectIdentity = ObjectIdentity
diagList = _DiagList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 208, 47, 1)
)
_DiagListNumberOfEntries_Type = Integer32
_DiagListNumberOfEntries_Object = MibScalar
diagListNumberOfEntries = _DiagListNumberOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 208, 47, 1, 1),
    _DiagListNumberOfEntries_Type()
)
diagListNumberOfEntries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    diagListNumberOfEntries.setStatus("mandatory")
_DiagListNumberOfErrorEntries_Type = Integer32
_DiagListNumberOfErrorEntries_Object = MibScalar
diagListNumberOfErrorEntries = _DiagListNumberOfErrorEntries_Object(
    (1, 3, 6, 1, 4, 1, 208, 47, 1, 2),
    _DiagListNumberOfErrorEntries_Type()
)
diagListNumberOfErrorEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diagListNumberOfErrorEntries.setStatus("mandatory")
_DiagListLastUpdateTime_Type = TimeTicks
_DiagListLastUpdateTime_Object = MibScalar
diagListLastUpdateTime = _DiagListLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 208, 47, 1, 3),
    _DiagListLastUpdateTime_Type()
)
diagListLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diagListLastUpdateTime.setStatus("mandatory")
_DiagListTable_Object = MibTable
diagListTable = _DiagListTable_Object(
    (1, 3, 6, 1, 4, 1, 208, 47, 1, 4)
)
if mibBuilder.loadTexts:
    diagListTable.setStatus("mandatory")
_DiagListEntry_Object = MibTableRow
diagListEntry = _DiagListEntry_Object(
    (1, 3, 6, 1, 4, 1, 208, 47, 1, 4, 1)
)
diagListEntry.setIndexNames(
    (0, "SCA-DIAG-MIB", "diagListIndex"),
)
if mibBuilder.loadTexts:
    diagListEntry.setStatus("mandatory")
_DiagListIndex_Type = Integer32
_DiagListIndex_Object = MibTableColumn
diagListIndex = _DiagListIndex_Object(
    (1, 3, 6, 1, 4, 1, 208, 47, 1, 4, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 208, 47, 1, 4, 1, 2),
    _DiagListLevel_Type()
)
diagListLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diagListLevel.setStatus("mandatory")
_DiagListCode_Type = Integer32
_DiagListCode_Object = MibTableColumn
diagListCode = _DiagListCode_Object(
    (1, 3, 6, 1, 4, 1, 208, 47, 1, 4, 1, 3),
    _DiagListCode_Type()
)
diagListCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diagListCode.setStatus("mandatory")
_DiagListIfindex_Type = Integer32
_DiagListIfindex_Object = MibTableColumn
diagListIfindex = _DiagListIfindex_Object(
    (1, 3, 6, 1, 4, 1, 208, 47, 1, 4, 1, 4),
    _DiagListIfindex_Type()
)
diagListIfindex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diagListIfindex.setStatus("mandatory")
_DiagListTimeStamp_Type = TimeTicks
_DiagListTimeStamp_Object = MibTableColumn
diagListTimeStamp = _DiagListTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 208, 47, 1, 4, 1, 5),
    _DiagListTimeStamp_Type()
)
diagListTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diagListTimeStamp.setStatus("mandatory")


class _DiagListDescription_Type(OctetString):
    """Custom type diagListDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(160, 160),
    )


_DiagListDescription_Type.__name__ = "OctetString"
_DiagListDescription_Object = MibTableColumn
diagListDescription = _DiagListDescription_Object(
    (1, 3, 6, 1, 4, 1, 208, 47, 1, 4, 1, 6),
    _DiagListDescription_Type()
)
diagListDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diagListDescription.setStatus("mandatory")


class _DiagListAdvice_Type(OctetString):
    """Custom type diagListAdvice based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(160, 160),
    )


_DiagListAdvice_Type.__name__ = "OctetString"
_DiagListAdvice_Object = MibTableColumn
diagListAdvice = _DiagListAdvice_Object(
    (1, 3, 6, 1, 4, 1, 208, 47, 1, 4, 1, 7),
    _DiagListAdvice_Type()
)
diagListAdvice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diagListAdvice.setStatus("mandatory")
_DiagTest_ObjectIdentity = ObjectIdentity
diagTest = _DiagTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 208, 47, 2)
)
_DiagTestTable_Object = MibTable
diagTestTable = _DiagTestTable_Object(
    (1, 3, 6, 1, 4, 1, 208, 47, 2, 1)
)
if mibBuilder.loadTexts:
    diagTestTable.setStatus("mandatory")
_DiagTestEntry_Object = MibTableRow
diagTestEntry = _DiagTestEntry_Object(
    (1, 3, 6, 1, 4, 1, 208, 47, 2, 1, 1)
)
diagTestEntry.setIndexNames(
    (0, "SCA-DIAG-MIB", "diagTestType"),
)
if mibBuilder.loadTexts:
    diagTestEntry.setStatus("mandatory")
_DiagTestType_Type = Integer32
_DiagTestType_Object = MibTableColumn
diagTestType = _DiagTestType_Object(
    (1, 3, 6, 1, 4, 1, 208, 47, 2, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 208, 47, 2, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 208, 47, 2, 1, 1, 3),
    _DiagTestStatus_Type()
)
diagTestStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    diagTestStatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SCA-DIAG-MIB",
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
       "diagTest": diagTest,
       "diagTestTable": diagTestTable,
       "diagTestEntry": diagTestEntry,
       "diagTestType": diagTestType,
       "diagTestDescription": diagTestDescription,
       "diagTestStatus": diagTestStatus}
)
