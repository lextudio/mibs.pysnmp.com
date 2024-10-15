# SNMP MIB module (Nortel-Magellan-Passport-AtmNetworkingMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-Magellan-Passport-AtmNetworkingMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:30:20 2024
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

(atmIfIndex,
 atmIfVcc,
 atmIfVccIndex,
 atmIfVpc,
 atmIfVpcIndex,
 atmIfVptIndex,
 atmIfVptVcc,
 atmIfVptVccIndex) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-AtmCoreMIB",
    "atmIfIndex",
    "atmIfVcc",
    "atmIfVccIndex",
    "atmIfVpc",
    "atmIfVpcIndex",
    "atmIfVptIndex",
    "atmIfVptVcc",
    "atmIfVptVccIndex")

(Counter32,
 DisplayString,
 Gauge32,
 Integer32,
 RowPointer,
 RowStatus,
 StorageType,
 Unsigned32) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-StandardTextualConventionsMIB",
    "Counter32",
    "DisplayString",
    "Gauge32",
    "Integer32",
    "RowPointer",
    "RowStatus",
    "StorageType",
    "Unsigned32")

(AsciiString,
 AsciiStringIndex,
 FixedPoint1,
 HexString,
 IntegerSequence,
 NonReplicated) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-TextualConventionsMIB",
    "AsciiString",
    "AsciiStringIndex",
    "FixedPoint1",
    "HexString",
    "IntegerSequence",
    "NonReplicated")

(components,
 passportMIBs) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-UsefulDefinitionsMIB",
    "components",
    "passportMIBs")

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

_ARtg_ObjectIdentity = ObjectIdentity
aRtg = _ARtg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95)
)
_ARtgRowStatusTable_Object = MibTable
aRtgRowStatusTable = _ARtgRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 1)
)
if mibBuilder.loadTexts:
    aRtgRowStatusTable.setStatus("mandatory")
_ARtgRowStatusEntry_Object = MibTableRow
aRtgRowStatusEntry = _ARtgRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 1, 1)
)
aRtgRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "aRtgIndex"),
)
if mibBuilder.loadTexts:
    aRtgRowStatusEntry.setStatus("mandatory")
_ARtgRowStatus_Type = RowStatus
_ARtgRowStatus_Object = MibTableColumn
aRtgRowStatus = _ARtgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 1, 1, 1),
    _ARtgRowStatus_Type()
)
aRtgRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aRtgRowStatus.setStatus("mandatory")
_ARtgComponentName_Type = DisplayString
_ARtgComponentName_Object = MibTableColumn
aRtgComponentName = _ARtgComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 1, 1, 2),
    _ARtgComponentName_Type()
)
aRtgComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aRtgComponentName.setStatus("mandatory")
_ARtgStorageType_Type = StorageType
_ARtgStorageType_Object = MibTableColumn
aRtgStorageType = _ARtgStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 1, 1, 4),
    _ARtgStorageType_Type()
)
aRtgStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aRtgStorageType.setStatus("mandatory")
_ARtgIndex_Type = NonReplicated
_ARtgIndex_Object = MibTableColumn
aRtgIndex = _ARtgIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 1, 1, 10),
    _ARtgIndex_Type()
)
aRtgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aRtgIndex.setStatus("mandatory")
_ARtgDna_ObjectIdentity = ObjectIdentity
aRtgDna = _ARtgDna_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 2)
)
_ARtgDnaRowStatusTable_Object = MibTable
aRtgDnaRowStatusTable = _ARtgDnaRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 2, 1)
)
if mibBuilder.loadTexts:
    aRtgDnaRowStatusTable.setStatus("mandatory")
_ARtgDnaRowStatusEntry_Object = MibTableRow
aRtgDnaRowStatusEntry = _ARtgDnaRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 2, 1, 1)
)
aRtgDnaRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "aRtgIndex"),
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "aRtgDnaIndex"),
)
if mibBuilder.loadTexts:
    aRtgDnaRowStatusEntry.setStatus("mandatory")
_ARtgDnaRowStatus_Type = RowStatus
_ARtgDnaRowStatus_Object = MibTableColumn
aRtgDnaRowStatus = _ARtgDnaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 2, 1, 1, 1),
    _ARtgDnaRowStatus_Type()
)
aRtgDnaRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aRtgDnaRowStatus.setStatus("mandatory")
_ARtgDnaComponentName_Type = DisplayString
_ARtgDnaComponentName_Object = MibTableColumn
aRtgDnaComponentName = _ARtgDnaComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 2, 1, 1, 2),
    _ARtgDnaComponentName_Type()
)
aRtgDnaComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aRtgDnaComponentName.setStatus("mandatory")
_ARtgDnaStorageType_Type = StorageType
_ARtgDnaStorageType_Object = MibTableColumn
aRtgDnaStorageType = _ARtgDnaStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 2, 1, 1, 4),
    _ARtgDnaStorageType_Type()
)
aRtgDnaStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aRtgDnaStorageType.setStatus("mandatory")


class _ARtgDnaIndex_Type(AsciiStringIndex):
    """Custom type aRtgDnaIndex based on AsciiStringIndex"""
    subtypeSpec = AsciiStringIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_ARtgDnaIndex_Type.__name__ = "AsciiStringIndex"
_ARtgDnaIndex_Object = MibTableColumn
aRtgDnaIndex = _ARtgDnaIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 2, 1, 1, 10),
    _ARtgDnaIndex_Type()
)
aRtgDnaIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aRtgDnaIndex.setStatus("mandatory")
_ARtgDnaDestInfo_ObjectIdentity = ObjectIdentity
aRtgDnaDestInfo = _ARtgDnaDestInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 2, 2)
)
_ARtgDnaDestInfoRowStatusTable_Object = MibTable
aRtgDnaDestInfoRowStatusTable = _ARtgDnaDestInfoRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 2, 2, 1)
)
if mibBuilder.loadTexts:
    aRtgDnaDestInfoRowStatusTable.setStatus("mandatory")
_ARtgDnaDestInfoRowStatusEntry_Object = MibTableRow
aRtgDnaDestInfoRowStatusEntry = _ARtgDnaDestInfoRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 2, 2, 1, 1)
)
aRtgDnaDestInfoRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "aRtgIndex"),
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "aRtgDnaIndex"),
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "aRtgDnaDestInfoIndex"),
)
if mibBuilder.loadTexts:
    aRtgDnaDestInfoRowStatusEntry.setStatus("mandatory")
_ARtgDnaDestInfoRowStatus_Type = RowStatus
_ARtgDnaDestInfoRowStatus_Object = MibTableColumn
aRtgDnaDestInfoRowStatus = _ARtgDnaDestInfoRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 2, 2, 1, 1, 1),
    _ARtgDnaDestInfoRowStatus_Type()
)
aRtgDnaDestInfoRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aRtgDnaDestInfoRowStatus.setStatus("mandatory")
_ARtgDnaDestInfoComponentName_Type = DisplayString
_ARtgDnaDestInfoComponentName_Object = MibTableColumn
aRtgDnaDestInfoComponentName = _ARtgDnaDestInfoComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 2, 2, 1, 1, 2),
    _ARtgDnaDestInfoComponentName_Type()
)
aRtgDnaDestInfoComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aRtgDnaDestInfoComponentName.setStatus("mandatory")
_ARtgDnaDestInfoStorageType_Type = StorageType
_ARtgDnaDestInfoStorageType_Object = MibTableColumn
aRtgDnaDestInfoStorageType = _ARtgDnaDestInfoStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 2, 2, 1, 1, 4),
    _ARtgDnaDestInfoStorageType_Type()
)
aRtgDnaDestInfoStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aRtgDnaDestInfoStorageType.setStatus("mandatory")


class _ARtgDnaDestInfoIndex_Type(Integer32):
    """Custom type aRtgDnaDestInfoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50),
    )


_ARtgDnaDestInfoIndex_Type.__name__ = "Integer32"
_ARtgDnaDestInfoIndex_Object = MibTableColumn
aRtgDnaDestInfoIndex = _ARtgDnaDestInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 2, 2, 1, 1, 10),
    _ARtgDnaDestInfoIndex_Type()
)
aRtgDnaDestInfoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aRtgDnaDestInfoIndex.setStatus("mandatory")
_ARtgDnaDestInfoOperTable_Object = MibTable
aRtgDnaDestInfoOperTable = _ARtgDnaDestInfoOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 2, 2, 10)
)
if mibBuilder.loadTexts:
    aRtgDnaDestInfoOperTable.setStatus("mandatory")
_ARtgDnaDestInfoOperEntry_Object = MibTableRow
aRtgDnaDestInfoOperEntry = _ARtgDnaDestInfoOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 2, 2, 10, 1)
)
aRtgDnaDestInfoOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "aRtgIndex"),
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "aRtgDnaIndex"),
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "aRtgDnaDestInfoIndex"),
)
if mibBuilder.loadTexts:
    aRtgDnaDestInfoOperEntry.setStatus("mandatory")


class _ARtgDnaDestInfoType_Type(Integer32):
    """Custom type aRtgDnaDestInfoType based on Integer32"""
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
        *(("alternate", 1),
          ("default", 3),
          ("primary", 0),
          ("registered", 2))
    )


_ARtgDnaDestInfoType_Type.__name__ = "Integer32"
_ARtgDnaDestInfoType_Object = MibTableColumn
aRtgDnaDestInfoType = _ARtgDnaDestInfoType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 2, 2, 10, 1, 1),
    _ARtgDnaDestInfoType_Type()
)
aRtgDnaDestInfoType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aRtgDnaDestInfoType.setStatus("mandatory")


class _ARtgDnaDestInfoScope_Type(Integer32):
    """Custom type aRtgDnaDestInfoScope based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 104),
    )


_ARtgDnaDestInfoScope_Type.__name__ = "Integer32"
_ARtgDnaDestInfoScope_Object = MibTableColumn
aRtgDnaDestInfoScope = _ARtgDnaDestInfoScope_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 2, 2, 10, 1, 2),
    _ARtgDnaDestInfoScope_Type()
)
aRtgDnaDestInfoScope.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aRtgDnaDestInfoScope.setStatus("mandatory")
_ARtgDnaDestInfoStdComponentName_Type = RowPointer
_ARtgDnaDestInfoStdComponentName_Object = MibTableColumn
aRtgDnaDestInfoStdComponentName = _ARtgDnaDestInfoStdComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 2, 2, 10, 1, 3),
    _ARtgDnaDestInfoStdComponentName_Type()
)
aRtgDnaDestInfoStdComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aRtgDnaDestInfoStdComponentName.setStatus("mandatory")


class _ARtgDnaDestInfoReachability_Type(Integer32):
    """Custom type aRtgDnaDestInfoReachability based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("exterior", 1),
          ("internal", 0))
    )


_ARtgDnaDestInfoReachability_Type.__name__ = "Integer32"
_ARtgDnaDestInfoReachability_Object = MibTableColumn
aRtgDnaDestInfoReachability = _ARtgDnaDestInfoReachability_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 2, 2, 10, 1, 4),
    _ARtgDnaDestInfoReachability_Type()
)
aRtgDnaDestInfoReachability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aRtgDnaDestInfoReachability.setStatus("mandatory")
_ARtgPnni_ObjectIdentity = ObjectIdentity
aRtgPnni = _ARtgPnni_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3)
)
_ARtgPnniRowStatusTable_Object = MibTable
aRtgPnniRowStatusTable = _ARtgPnniRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 1)
)
if mibBuilder.loadTexts:
    aRtgPnniRowStatusTable.setStatus("mandatory")
_ARtgPnniRowStatusEntry_Object = MibTableRow
aRtgPnniRowStatusEntry = _ARtgPnniRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 1, 1)
)
aRtgPnniRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "aRtgIndex"),
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "aRtgPnniIndex"),
)
if mibBuilder.loadTexts:
    aRtgPnniRowStatusEntry.setStatus("mandatory")
_ARtgPnniRowStatus_Type = RowStatus
_ARtgPnniRowStatus_Object = MibTableColumn
aRtgPnniRowStatus = _ARtgPnniRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 1, 1, 1),
    _ARtgPnniRowStatus_Type()
)
aRtgPnniRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aRtgPnniRowStatus.setStatus("mandatory")
_ARtgPnniComponentName_Type = DisplayString
_ARtgPnniComponentName_Object = MibTableColumn
aRtgPnniComponentName = _ARtgPnniComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 1, 1, 2),
    _ARtgPnniComponentName_Type()
)
aRtgPnniComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aRtgPnniComponentName.setStatus("mandatory")
_ARtgPnniStorageType_Type = StorageType
_ARtgPnniStorageType_Object = MibTableColumn
aRtgPnniStorageType = _ARtgPnniStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 1, 1, 4),
    _ARtgPnniStorageType_Type()
)
aRtgPnniStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aRtgPnniStorageType.setStatus("mandatory")
_ARtgPnniIndex_Type = NonReplicated
_ARtgPnniIndex_Object = MibTableColumn
aRtgPnniIndex = _ARtgPnniIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 1, 1, 10),
    _ARtgPnniIndex_Type()
)
aRtgPnniIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aRtgPnniIndex.setStatus("mandatory")
_ARtgPnniRf_ObjectIdentity = ObjectIdentity
aRtgPnniRf = _ARtgPnniRf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 2)
)
_ARtgPnniRfRowStatusTable_Object = MibTable
aRtgPnniRfRowStatusTable = _ARtgPnniRfRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 2, 1)
)
if mibBuilder.loadTexts:
    aRtgPnniRfRowStatusTable.setStatus("mandatory")
_ARtgPnniRfRowStatusEntry_Object = MibTableRow
aRtgPnniRfRowStatusEntry = _ARtgPnniRfRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 2, 1, 1)
)
aRtgPnniRfRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "aRtgIndex"),
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "aRtgPnniIndex"),
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "aRtgPnniRfIndex"),
)
if mibBuilder.loadTexts:
    aRtgPnniRfRowStatusEntry.setStatus("mandatory")
_ARtgPnniRfRowStatus_Type = RowStatus
_ARtgPnniRfRowStatus_Object = MibTableColumn
aRtgPnniRfRowStatus = _ARtgPnniRfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 2, 1, 1, 1),
    _ARtgPnniRfRowStatus_Type()
)
aRtgPnniRfRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aRtgPnniRfRowStatus.setStatus("mandatory")
_ARtgPnniRfComponentName_Type = DisplayString
_ARtgPnniRfComponentName_Object = MibTableColumn
aRtgPnniRfComponentName = _ARtgPnniRfComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 2, 1, 1, 2),
    _ARtgPnniRfComponentName_Type()
)
aRtgPnniRfComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aRtgPnniRfComponentName.setStatus("mandatory")
_ARtgPnniRfStorageType_Type = StorageType
_ARtgPnniRfStorageType_Object = MibTableColumn
aRtgPnniRfStorageType = _ARtgPnniRfStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 2, 1, 1, 4),
    _ARtgPnniRfStorageType_Type()
)
aRtgPnniRfStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aRtgPnniRfStorageType.setStatus("mandatory")
_ARtgPnniRfIndex_Type = NonReplicated
_ARtgPnniRfIndex_Object = MibTableColumn
aRtgPnniRfIndex = _ARtgPnniRfIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 2, 1, 1, 10),
    _ARtgPnniRfIndex_Type()
)
aRtgPnniRfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aRtgPnniRfIndex.setStatus("mandatory")
_ARtgPnniRfCriteriaTable_Object = MibTable
aRtgPnniRfCriteriaTable = _ARtgPnniRfCriteriaTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 2, 10)
)
if mibBuilder.loadTexts:
    aRtgPnniRfCriteriaTable.setStatus("mandatory")
_ARtgPnniRfCriteriaEntry_Object = MibTableRow
aRtgPnniRfCriteriaEntry = _ARtgPnniRfCriteriaEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 2, 10, 1)
)
aRtgPnniRfCriteriaEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "aRtgIndex"),
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "aRtgPnniIndex"),
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "aRtgPnniRfIndex"),
)
if mibBuilder.loadTexts:
    aRtgPnniRfCriteriaEntry.setStatus("mandatory")


class _ARtgPnniRfDestinationAddress_Type(HexString):
    """Custom type aRtgPnniRfDestinationAddress based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_ARtgPnniRfDestinationAddress_Type.__name__ = "HexString"
_ARtgPnniRfDestinationAddress_Object = MibTableColumn
aRtgPnniRfDestinationAddress = _ARtgPnniRfDestinationAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 2, 10, 1, 1),
    _ARtgPnniRfDestinationAddress_Type()
)
aRtgPnniRfDestinationAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aRtgPnniRfDestinationAddress.setStatus("mandatory")


class _ARtgPnniRfMaxRoutes_Type(Unsigned32):
    """Custom type aRtgPnniRfMaxRoutes based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_ARtgPnniRfMaxRoutes_Type.__name__ = "Unsigned32"
_ARtgPnniRfMaxRoutes_Object = MibTableColumn
aRtgPnniRfMaxRoutes = _ARtgPnniRfMaxRoutes_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 2, 10, 1, 2),
    _ARtgPnniRfMaxRoutes_Type()
)
aRtgPnniRfMaxRoutes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aRtgPnniRfMaxRoutes.setStatus("mandatory")


class _ARtgPnniRfTxTrafficDescType_Type(Integer32):
    """Custom type aRtgPnniRfTxTrafficDescType based on Integer32"""
    defaultValue = 1

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
              8)
        )
    )
    namedValues = NamedValues(
        *(("n1", 1),
          ("n2", 2),
          ("n3", 3),
          ("n4", 4),
          ("n5", 5),
          ("n6", 6),
          ("n7", 7),
          ("n8", 8))
    )


_ARtgPnniRfTxTrafficDescType_Type.__name__ = "Integer32"
_ARtgPnniRfTxTrafficDescType_Object = MibTableColumn
aRtgPnniRfTxTrafficDescType = _ARtgPnniRfTxTrafficDescType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 2, 10, 1, 3),
    _ARtgPnniRfTxTrafficDescType_Type()
)
aRtgPnniRfTxTrafficDescType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aRtgPnniRfTxTrafficDescType.setStatus("mandatory")


class _ARtgPnniRfRxTrafficDescType_Type(Integer32):
    """Custom type aRtgPnniRfRxTrafficDescType based on Integer32"""
    defaultValue = 15

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
              15)
        )
    )
    namedValues = NamedValues(
        *(("n1", 1),
          ("n2", 2),
          ("n3", 3),
          ("n4", 4),
          ("n5", 5),
          ("n6", 6),
          ("n7", 7),
          ("n8", 8),
          ("sameAsTx", 15))
    )


_ARtgPnniRfRxTrafficDescType_Type.__name__ = "Integer32"
_ARtgPnniRfRxTrafficDescType_Object = MibTableColumn
aRtgPnniRfRxTrafficDescType = _ARtgPnniRfRxTrafficDescType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 2, 10, 1, 5),
    _ARtgPnniRfRxTrafficDescType_Type()
)
aRtgPnniRfRxTrafficDescType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aRtgPnniRfRxTrafficDescType.setStatus("mandatory")


class _ARtgPnniRfAtmServiceCategory_Type(Integer32):
    """Custom type aRtgPnniRfAtmServiceCategory based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              15)
        )
    )
    namedValues = NamedValues(
        *(("constantBitRate", 1),
          ("derivedFromBBC", 15),
          ("nrtVariableBitRate", 3),
          ("rtVariableBitRate", 2),
          ("unspecifiedBitRate", 0))
    )


_ARtgPnniRfAtmServiceCategory_Type.__name__ = "Integer32"
_ARtgPnniRfAtmServiceCategory_Object = MibTableColumn
aRtgPnniRfAtmServiceCategory = _ARtgPnniRfAtmServiceCategory_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 2, 10, 1, 6),
    _ARtgPnniRfAtmServiceCategory_Type()
)
aRtgPnniRfAtmServiceCategory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aRtgPnniRfAtmServiceCategory.setStatus("mandatory")


class _ARtgPnniRfFwdQosClass_Type(Integer32):
    """Custom type aRtgPnniRfFwdQosClass based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("n0", 0),
          ("n1", 1),
          ("n2", 2),
          ("n3", 3),
          ("n4", 4))
    )


_ARtgPnniRfFwdQosClass_Type.__name__ = "Integer32"
_ARtgPnniRfFwdQosClass_Object = MibTableColumn
aRtgPnniRfFwdQosClass = _ARtgPnniRfFwdQosClass_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 2, 10, 1, 10),
    _ARtgPnniRfFwdQosClass_Type()
)
aRtgPnniRfFwdQosClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aRtgPnniRfFwdQosClass.setStatus("mandatory")


class _ARtgPnniRfBwdQosClass_Type(Integer32):
    """Custom type aRtgPnniRfBwdQosClass based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              15)
        )
    )
    namedValues = NamedValues(
        *(("n0", 0),
          ("n1", 1),
          ("n2", 2),
          ("n3", 3),
          ("n4", 4),
          ("sameAsFwd", 15))
    )


_ARtgPnniRfBwdQosClass_Type.__name__ = "Integer32"
_ARtgPnniRfBwdQosClass_Object = MibTableColumn
aRtgPnniRfBwdQosClass = _ARtgPnniRfBwdQosClass_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 2, 10, 1, 11),
    _ARtgPnniRfBwdQosClass_Type()
)
aRtgPnniRfBwdQosClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aRtgPnniRfBwdQosClass.setStatus("mandatory")


class _ARtgPnniRfBearerClassBbc_Type(Integer32):
    """Custom type aRtgPnniRfBearerClassBbc based on Integer32"""
    defaultValue = 31

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              16,
              31)
        )
    )
    namedValues = NamedValues(
        *(("a", 1),
          ("c", 3),
          ("derivedFromServiceCategory", 31),
          ("x", 16))
    )


_ARtgPnniRfBearerClassBbc_Type.__name__ = "Integer32"
_ARtgPnniRfBearerClassBbc_Object = MibTableColumn
aRtgPnniRfBearerClassBbc = _ARtgPnniRfBearerClassBbc_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 2, 10, 1, 12),
    _ARtgPnniRfBearerClassBbc_Type()
)
aRtgPnniRfBearerClassBbc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aRtgPnniRfBearerClassBbc.setStatus("mandatory")


class _ARtgPnniRfTransferCapabilityBbc_Type(Integer32):
    """Custom type aRtgPnniRfTransferCapabilityBbc based on Integer32"""
    defaultValue = 31

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              5,
              8,
              9,
              10,
              30,
              31)
        )
    )
    namedValues = NamedValues(
        *(("derivedFromServiceCategory", 31),
          ("n0", 0),
          ("n1", 1),
          ("n10", 10),
          ("n2", 2),
          ("n5", 5),
          ("n8", 8),
          ("n9", 9),
          ("notApplicable", 30))
    )


_ARtgPnniRfTransferCapabilityBbc_Type.__name__ = "Integer32"
_ARtgPnniRfTransferCapabilityBbc_Object = MibTableColumn
aRtgPnniRfTransferCapabilityBbc = _ARtgPnniRfTransferCapabilityBbc_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 2, 10, 1, 13),
    _ARtgPnniRfTransferCapabilityBbc_Type()
)
aRtgPnniRfTransferCapabilityBbc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aRtgPnniRfTransferCapabilityBbc.setStatus("mandatory")


class _ARtgPnniRfClippingBbc_Type(Integer32):
    """Custom type aRtgPnniRfClippingBbc based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_ARtgPnniRfClippingBbc_Type.__name__ = "Integer32"
_ARtgPnniRfClippingBbc_Object = MibTableColumn
aRtgPnniRfClippingBbc = _ARtgPnniRfClippingBbc_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 2, 10, 1, 14),
    _ARtgPnniRfClippingBbc_Type()
)
aRtgPnniRfClippingBbc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aRtgPnniRfClippingBbc.setStatus("mandatory")


class _ARtgPnniRfBestEffort_Type(Integer32):
    """Custom type aRtgPnniRfBestEffort based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              15)
        )
    )
    namedValues = NamedValues(
        *(("derivedFromServiceCategory", 15),
          ("indicated", 0),
          ("notIndicated", 1))
    )


_ARtgPnniRfBestEffort_Type.__name__ = "Integer32"
_ARtgPnniRfBestEffort_Object = MibTableColumn
aRtgPnniRfBestEffort = _ARtgPnniRfBestEffort_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 2, 10, 1, 15),
    _ARtgPnniRfBestEffort_Type()
)
aRtgPnniRfBestEffort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aRtgPnniRfBestEffort.setStatus("mandatory")


class _ARtgPnniRfOptimizationMetric_Type(Integer32):
    """Custom type aRtgPnniRfOptimizationMetric based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("aw", 2),
          ("cdv", 0),
          ("maxCtd", 1))
    )


_ARtgPnniRfOptimizationMetric_Type.__name__ = "Integer32"
_ARtgPnniRfOptimizationMetric_Object = MibTableColumn
aRtgPnniRfOptimizationMetric = _ARtgPnniRfOptimizationMetric_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 2, 10, 1, 16),
    _ARtgPnniRfOptimizationMetric_Type()
)
aRtgPnniRfOptimizationMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aRtgPnniRfOptimizationMetric.setStatus("mandatory")
_ARtgPnniRfRxTdpTable_Object = MibTable
aRtgPnniRfRxTdpTable = _ARtgPnniRfRxTdpTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 2, 388)
)
if mibBuilder.loadTexts:
    aRtgPnniRfRxTdpTable.setStatus("mandatory")
_ARtgPnniRfRxTdpEntry_Object = MibTableRow
aRtgPnniRfRxTdpEntry = _ARtgPnniRfRxTdpEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 2, 388, 1)
)
aRtgPnniRfRxTdpEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "aRtgIndex"),
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "aRtgPnniIndex"),
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "aRtgPnniRfIndex"),
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "aRtgPnniRfRxTdpIndex"),
)
if mibBuilder.loadTexts:
    aRtgPnniRfRxTdpEntry.setStatus("mandatory")


class _ARtgPnniRfRxTdpIndex_Type(Integer32):
    """Custom type aRtgPnniRfRxTdpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_ARtgPnniRfRxTdpIndex_Type.__name__ = "Integer32"
_ARtgPnniRfRxTdpIndex_Object = MibTableColumn
aRtgPnniRfRxTdpIndex = _ARtgPnniRfRxTdpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 2, 388, 1, 1),
    _ARtgPnniRfRxTdpIndex_Type()
)
aRtgPnniRfRxTdpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aRtgPnniRfRxTdpIndex.setStatus("mandatory")


class _ARtgPnniRfRxTdpValue_Type(Unsigned32):
    """Custom type aRtgPnniRfRxTdpValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ARtgPnniRfRxTdpValue_Type.__name__ = "Unsigned32"
_ARtgPnniRfRxTdpValue_Object = MibTableColumn
aRtgPnniRfRxTdpValue = _ARtgPnniRfRxTdpValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 2, 388, 1, 2),
    _ARtgPnniRfRxTdpValue_Type()
)
aRtgPnniRfRxTdpValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aRtgPnniRfRxTdpValue.setStatus("mandatory")
_ARtgPnniRfTxTdpTable_Object = MibTable
aRtgPnniRfTxTdpTable = _ARtgPnniRfTxTdpTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 2, 389)
)
if mibBuilder.loadTexts:
    aRtgPnniRfTxTdpTable.setStatus("mandatory")
_ARtgPnniRfTxTdpEntry_Object = MibTableRow
aRtgPnniRfTxTdpEntry = _ARtgPnniRfTxTdpEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 2, 389, 1)
)
aRtgPnniRfTxTdpEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "aRtgIndex"),
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "aRtgPnniIndex"),
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "aRtgPnniRfIndex"),
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "aRtgPnniRfTxTdpIndex"),
)
if mibBuilder.loadTexts:
    aRtgPnniRfTxTdpEntry.setStatus("mandatory")


class _ARtgPnniRfTxTdpIndex_Type(Integer32):
    """Custom type aRtgPnniRfTxTdpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_ARtgPnniRfTxTdpIndex_Type.__name__ = "Integer32"
_ARtgPnniRfTxTdpIndex_Object = MibTableColumn
aRtgPnniRfTxTdpIndex = _ARtgPnniRfTxTdpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 2, 389, 1, 1),
    _ARtgPnniRfTxTdpIndex_Type()
)
aRtgPnniRfTxTdpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aRtgPnniRfTxTdpIndex.setStatus("mandatory")


class _ARtgPnniRfTxTdpValue_Type(Unsigned32):
    """Custom type aRtgPnniRfTxTdpValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ARtgPnniRfTxTdpValue_Type.__name__ = "Unsigned32"
_ARtgPnniRfTxTdpValue_Object = MibTableColumn
aRtgPnniRfTxTdpValue = _ARtgPnniRfTxTdpValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 2, 389, 1, 2),
    _ARtgPnniRfTxTdpValue_Type()
)
aRtgPnniRfTxTdpValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aRtgPnniRfTxTdpValue.setStatus("mandatory")
_ARtgPnniRfFqpTable_Object = MibTable
aRtgPnniRfFqpTable = _ARtgPnniRfFqpTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 2, 390)
)
if mibBuilder.loadTexts:
    aRtgPnniRfFqpTable.setStatus("mandatory")
_ARtgPnniRfFqpEntry_Object = MibTableRow
aRtgPnniRfFqpEntry = _ARtgPnniRfFqpEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 2, 390, 1)
)
aRtgPnniRfFqpEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "aRtgIndex"),
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "aRtgPnniIndex"),
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "aRtgPnniRfIndex"),
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "aRtgPnniRfFqpIndex"),
)
if mibBuilder.loadTexts:
    aRtgPnniRfFqpEntry.setStatus("mandatory")


class _ARtgPnniRfFqpIndex_Type(Integer32):
    """Custom type aRtgPnniRfFqpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cdv", 0),
          ("clr", 2),
          ("ctd", 1))
    )


_ARtgPnniRfFqpIndex_Type.__name__ = "Integer32"
_ARtgPnniRfFqpIndex_Object = MibTableColumn
aRtgPnniRfFqpIndex = _ARtgPnniRfFqpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 2, 390, 1, 1),
    _ARtgPnniRfFqpIndex_Type()
)
aRtgPnniRfFqpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aRtgPnniRfFqpIndex.setStatus("mandatory")


class _ARtgPnniRfFqpValue_Type(Unsigned32):
    """Custom type aRtgPnniRfFqpValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ARtgPnniRfFqpValue_Type.__name__ = "Unsigned32"
_ARtgPnniRfFqpValue_Object = MibTableColumn
aRtgPnniRfFqpValue = _ARtgPnniRfFqpValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 2, 390, 1, 2),
    _ARtgPnniRfFqpValue_Type()
)
aRtgPnniRfFqpValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aRtgPnniRfFqpValue.setStatus("mandatory")
_ARtgPnniRfBqpTable_Object = MibTable
aRtgPnniRfBqpTable = _ARtgPnniRfBqpTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 2, 393)
)
if mibBuilder.loadTexts:
    aRtgPnniRfBqpTable.setStatus("mandatory")
_ARtgPnniRfBqpEntry_Object = MibTableRow
aRtgPnniRfBqpEntry = _ARtgPnniRfBqpEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 2, 393, 1)
)
aRtgPnniRfBqpEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "aRtgIndex"),
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "aRtgPnniIndex"),
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "aRtgPnniRfIndex"),
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "aRtgPnniRfBqpIndex"),
)
if mibBuilder.loadTexts:
    aRtgPnniRfBqpEntry.setStatus("mandatory")


class _ARtgPnniRfBqpIndex_Type(Integer32):
    """Custom type aRtgPnniRfBqpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cdv", 0),
          ("clr", 2),
          ("ctd", 1))
    )


_ARtgPnniRfBqpIndex_Type.__name__ = "Integer32"
_ARtgPnniRfBqpIndex_Object = MibTableColumn
aRtgPnniRfBqpIndex = _ARtgPnniRfBqpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 2, 393, 1, 1),
    _ARtgPnniRfBqpIndex_Type()
)
aRtgPnniRfBqpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aRtgPnniRfBqpIndex.setStatus("mandatory")


class _ARtgPnniRfBqpValue_Type(Unsigned32):
    """Custom type aRtgPnniRfBqpValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ARtgPnniRfBqpValue_Type.__name__ = "Unsigned32"
_ARtgPnniRfBqpValue_Object = MibTableColumn
aRtgPnniRfBqpValue = _ARtgPnniRfBqpValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 2, 393, 1, 2),
    _ARtgPnniRfBqpValue_Type()
)
aRtgPnniRfBqpValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aRtgPnniRfBqpValue.setStatus("mandatory")
_ARtgPnniCfgNode_ObjectIdentity = ObjectIdentity
aRtgPnniCfgNode = _ARtgPnniCfgNode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 3)
)
_ARtgPnniCfgNodeRowStatusTable_Object = MibTable
aRtgPnniCfgNodeRowStatusTable = _ARtgPnniCfgNodeRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 3, 1)
)
if mibBuilder.loadTexts:
    aRtgPnniCfgNodeRowStatusTable.setStatus("mandatory")
_ARtgPnniCfgNodeRowStatusEntry_Object = MibTableRow
aRtgPnniCfgNodeRowStatusEntry = _ARtgPnniCfgNodeRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 3, 1, 1)
)
aRtgPnniCfgNodeRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "aRtgIndex"),
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "aRtgPnniIndex"),
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "aRtgPnniCfgNodeIndex"),
)
if mibBuilder.loadTexts:
    aRtgPnniCfgNodeRowStatusEntry.setStatus("mandatory")
_ARtgPnniCfgNodeRowStatus_Type = RowStatus
_ARtgPnniCfgNodeRowStatus_Object = MibTableColumn
aRtgPnniCfgNodeRowStatus = _ARtgPnniCfgNodeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 3, 1, 1, 1),
    _ARtgPnniCfgNodeRowStatus_Type()
)
aRtgPnniCfgNodeRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aRtgPnniCfgNodeRowStatus.setStatus("mandatory")
_ARtgPnniCfgNodeComponentName_Type = DisplayString
_ARtgPnniCfgNodeComponentName_Object = MibTableColumn
aRtgPnniCfgNodeComponentName = _ARtgPnniCfgNodeComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 3, 1, 1, 2),
    _ARtgPnniCfgNodeComponentName_Type()
)
aRtgPnniCfgNodeComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aRtgPnniCfgNodeComponentName.setStatus("mandatory")
_ARtgPnniCfgNodeStorageType_Type = StorageType
_ARtgPnniCfgNodeStorageType_Object = MibTableColumn
aRtgPnniCfgNodeStorageType = _ARtgPnniCfgNodeStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 3, 1, 1, 4),
    _ARtgPnniCfgNodeStorageType_Type()
)
aRtgPnniCfgNodeStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aRtgPnniCfgNodeStorageType.setStatus("mandatory")


class _ARtgPnniCfgNodeIndex_Type(Integer32):
    """Custom type aRtgPnniCfgNodeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 104),
    )


_ARtgPnniCfgNodeIndex_Type.__name__ = "Integer32"
_ARtgPnniCfgNodeIndex_Object = MibTableColumn
aRtgPnniCfgNodeIndex = _ARtgPnniCfgNodeIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 3, 1, 1, 10),
    _ARtgPnniCfgNodeIndex_Type()
)
aRtgPnniCfgNodeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aRtgPnniCfgNodeIndex.setStatus("mandatory")
_ARtgPnniCfgNodeSAddr_ObjectIdentity = ObjectIdentity
aRtgPnniCfgNodeSAddr = _ARtgPnniCfgNodeSAddr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 3, 2)
)
_ARtgPnniCfgNodeSAddrRowStatusTable_Object = MibTable
aRtgPnniCfgNodeSAddrRowStatusTable = _ARtgPnniCfgNodeSAddrRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 3, 2, 1)
)
if mibBuilder.loadTexts:
    aRtgPnniCfgNodeSAddrRowStatusTable.setStatus("mandatory")
_ARtgPnniCfgNodeSAddrRowStatusEntry_Object = MibTableRow
aRtgPnniCfgNodeSAddrRowStatusEntry = _ARtgPnniCfgNodeSAddrRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 3, 2, 1, 1)
)
aRtgPnniCfgNodeSAddrRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "aRtgIndex"),
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "aRtgPnniIndex"),
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "aRtgPnniCfgNodeIndex"),
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "aRtgPnniCfgNodeSAddrAddressIndex"),
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "aRtgPnniCfgNodeSAddrPrefixLengthIndex"),
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "aRtgPnniCfgNodeSAddrReachabilityIndex"),
)
if mibBuilder.loadTexts:
    aRtgPnniCfgNodeSAddrRowStatusEntry.setStatus("mandatory")
_ARtgPnniCfgNodeSAddrRowStatus_Type = RowStatus
_ARtgPnniCfgNodeSAddrRowStatus_Object = MibTableColumn
aRtgPnniCfgNodeSAddrRowStatus = _ARtgPnniCfgNodeSAddrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 3, 2, 1, 1, 1),
    _ARtgPnniCfgNodeSAddrRowStatus_Type()
)
aRtgPnniCfgNodeSAddrRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aRtgPnniCfgNodeSAddrRowStatus.setStatus("mandatory")
_ARtgPnniCfgNodeSAddrComponentName_Type = DisplayString
_ARtgPnniCfgNodeSAddrComponentName_Object = MibTableColumn
aRtgPnniCfgNodeSAddrComponentName = _ARtgPnniCfgNodeSAddrComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 3, 2, 1, 1, 2),
    _ARtgPnniCfgNodeSAddrComponentName_Type()
)
aRtgPnniCfgNodeSAddrComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aRtgPnniCfgNodeSAddrComponentName.setStatus("mandatory")
_ARtgPnniCfgNodeSAddrStorageType_Type = StorageType
_ARtgPnniCfgNodeSAddrStorageType_Object = MibTableColumn
aRtgPnniCfgNodeSAddrStorageType = _ARtgPnniCfgNodeSAddrStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 3, 2, 1, 1, 4),
    _ARtgPnniCfgNodeSAddrStorageType_Type()
)
aRtgPnniCfgNodeSAddrStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aRtgPnniCfgNodeSAddrStorageType.setStatus("mandatory")


class _ARtgPnniCfgNodeSAddrAddressIndex_Type(HexString):
    """Custom type aRtgPnniCfgNodeSAddrAddressIndex based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(19, 19),
    )


_ARtgPnniCfgNodeSAddrAddressIndex_Type.__name__ = "HexString"
_ARtgPnniCfgNodeSAddrAddressIndex_Object = MibTableColumn
aRtgPnniCfgNodeSAddrAddressIndex = _ARtgPnniCfgNodeSAddrAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 3, 2, 1, 1, 10),
    _ARtgPnniCfgNodeSAddrAddressIndex_Type()
)
aRtgPnniCfgNodeSAddrAddressIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aRtgPnniCfgNodeSAddrAddressIndex.setStatus("mandatory")


class _ARtgPnniCfgNodeSAddrPrefixLengthIndex_Type(Integer32):
    """Custom type aRtgPnniCfgNodeSAddrPrefixLengthIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 152),
    )


_ARtgPnniCfgNodeSAddrPrefixLengthIndex_Type.__name__ = "Integer32"
_ARtgPnniCfgNodeSAddrPrefixLengthIndex_Object = MibTableColumn
aRtgPnniCfgNodeSAddrPrefixLengthIndex = _ARtgPnniCfgNodeSAddrPrefixLengthIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 3, 2, 1, 1, 11),
    _ARtgPnniCfgNodeSAddrPrefixLengthIndex_Type()
)
aRtgPnniCfgNodeSAddrPrefixLengthIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aRtgPnniCfgNodeSAddrPrefixLengthIndex.setStatus("mandatory")


class _ARtgPnniCfgNodeSAddrReachabilityIndex_Type(Integer32):
    """Custom type aRtgPnniCfgNodeSAddrReachabilityIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("exterior", 1),
          ("internal", 0))
    )


_ARtgPnniCfgNodeSAddrReachabilityIndex_Type.__name__ = "Integer32"
_ARtgPnniCfgNodeSAddrReachabilityIndex_Object = MibTableColumn
aRtgPnniCfgNodeSAddrReachabilityIndex = _ARtgPnniCfgNodeSAddrReachabilityIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 3, 2, 1, 1, 12),
    _ARtgPnniCfgNodeSAddrReachabilityIndex_Type()
)
aRtgPnniCfgNodeSAddrReachabilityIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aRtgPnniCfgNodeSAddrReachabilityIndex.setStatus("mandatory")
_ARtgPnniCfgNodeSAddrProvTable_Object = MibTable
aRtgPnniCfgNodeSAddrProvTable = _ARtgPnniCfgNodeSAddrProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 3, 2, 10)
)
if mibBuilder.loadTexts:
    aRtgPnniCfgNodeSAddrProvTable.setStatus("mandatory")
_ARtgPnniCfgNodeSAddrProvEntry_Object = MibTableRow
aRtgPnniCfgNodeSAddrProvEntry = _ARtgPnniCfgNodeSAddrProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 3, 2, 10, 1)
)
aRtgPnniCfgNodeSAddrProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "aRtgIndex"),
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "aRtgPnniIndex"),
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "aRtgPnniCfgNodeIndex"),
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "aRtgPnniCfgNodeSAddrAddressIndex"),
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "aRtgPnniCfgNodeSAddrPrefixLengthIndex"),
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "aRtgPnniCfgNodeSAddrReachabilityIndex"),
)
if mibBuilder.loadTexts:
    aRtgPnniCfgNodeSAddrProvEntry.setStatus("mandatory")


class _ARtgPnniCfgNodeSAddrSuppress_Type(Integer32):
    """Custom type aRtgPnniCfgNodeSAddrSuppress based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_ARtgPnniCfgNodeSAddrSuppress_Type.__name__ = "Integer32"
_ARtgPnniCfgNodeSAddrSuppress_Object = MibTableColumn
aRtgPnniCfgNodeSAddrSuppress = _ARtgPnniCfgNodeSAddrSuppress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 3, 2, 10, 1, 2),
    _ARtgPnniCfgNodeSAddrSuppress_Type()
)
aRtgPnniCfgNodeSAddrSuppress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aRtgPnniCfgNodeSAddrSuppress.setStatus("mandatory")
_ARtgPnniCfgNodeSAddrOperTable_Object = MibTable
aRtgPnniCfgNodeSAddrOperTable = _ARtgPnniCfgNodeSAddrOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 3, 2, 11)
)
if mibBuilder.loadTexts:
    aRtgPnniCfgNodeSAddrOperTable.setStatus("mandatory")
_ARtgPnniCfgNodeSAddrOperEntry_Object = MibTableRow
aRtgPnniCfgNodeSAddrOperEntry = _ARtgPnniCfgNodeSAddrOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 3, 2, 11, 1)
)
aRtgPnniCfgNodeSAddrOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "aRtgIndex"),
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "aRtgPnniIndex"),
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "aRtgPnniCfgNodeIndex"),
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "aRtgPnniCfgNodeSAddrAddressIndex"),
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "aRtgPnniCfgNodeSAddrPrefixLengthIndex"),
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "aRtgPnniCfgNodeSAddrReachabilityIndex"),
)
if mibBuilder.loadTexts:
    aRtgPnniCfgNodeSAddrOperEntry.setStatus("mandatory")


class _ARtgPnniCfgNodeSAddrState_Type(Integer32):
    """Custom type aRtgPnniCfgNodeSAddrState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("advertising", 0),
          ("inactive", 2),
          ("suppressing", 1))
    )


_ARtgPnniCfgNodeSAddrState_Type.__name__ = "Integer32"
_ARtgPnniCfgNodeSAddrState_Object = MibTableColumn
aRtgPnniCfgNodeSAddrState = _ARtgPnniCfgNodeSAddrState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 3, 2, 11, 1, 1),
    _ARtgPnniCfgNodeSAddrState_Type()
)
aRtgPnniCfgNodeSAddrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aRtgPnniCfgNodeSAddrState.setStatus("mandatory")


class _ARtgPnniCfgNodeSAddrScope_Type(Integer32):
    """Custom type aRtgPnniCfgNodeSAddrScope based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 104),
    )


_ARtgPnniCfgNodeSAddrScope_Type.__name__ = "Integer32"
_ARtgPnniCfgNodeSAddrScope_Object = MibTableColumn
aRtgPnniCfgNodeSAddrScope = _ARtgPnniCfgNodeSAddrScope_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 3, 2, 11, 1, 2),
    _ARtgPnniCfgNodeSAddrScope_Type()
)
aRtgPnniCfgNodeSAddrScope.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aRtgPnniCfgNodeSAddrScope.setStatus("mandatory")
_ARtgPnniCfgNodeNbr_ObjectIdentity = ObjectIdentity
aRtgPnniCfgNodeNbr = _ARtgPnniCfgNodeNbr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 3, 3)
)
_ARtgPnniCfgNodeNbrRowStatusTable_Object = MibTable
aRtgPnniCfgNodeNbrRowStatusTable = _ARtgPnniCfgNodeNbrRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 3, 3, 1)
)
if mibBuilder.loadTexts:
    aRtgPnniCfgNodeNbrRowStatusTable.setStatus("mandatory")
_ARtgPnniCfgNodeNbrRowStatusEntry_Object = MibTableRow
aRtgPnniCfgNodeNbrRowStatusEntry = _ARtgPnniCfgNodeNbrRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 3, 3, 1, 1)
)
aRtgPnniCfgNodeNbrRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "aRtgIndex"),
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "aRtgPnniIndex"),
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "aRtgPnniCfgNodeIndex"),
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "aRtgPnniCfgNodeNbrIndex"),
)
if mibBuilder.loadTexts:
    aRtgPnniCfgNodeNbrRowStatusEntry.setStatus("mandatory")
_ARtgPnniCfgNodeNbrRowStatus_Type = RowStatus
_ARtgPnniCfgNodeNbrRowStatus_Object = MibTableColumn
aRtgPnniCfgNodeNbrRowStatus = _ARtgPnniCfgNodeNbrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 3, 3, 1, 1, 1),
    _ARtgPnniCfgNodeNbrRowStatus_Type()
)
aRtgPnniCfgNodeNbrRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aRtgPnniCfgNodeNbrRowStatus.setStatus("mandatory")
_ARtgPnniCfgNodeNbrComponentName_Type = DisplayString
_ARtgPnniCfgNodeNbrComponentName_Object = MibTableColumn
aRtgPnniCfgNodeNbrComponentName = _ARtgPnniCfgNodeNbrComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 3, 3, 1, 1, 2),
    _ARtgPnniCfgNodeNbrComponentName_Type()
)
aRtgPnniCfgNodeNbrComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aRtgPnniCfgNodeNbrComponentName.setStatus("mandatory")
_ARtgPnniCfgNodeNbrStorageType_Type = StorageType
_ARtgPnniCfgNodeNbrStorageType_Object = MibTableColumn
aRtgPnniCfgNodeNbrStorageType = _ARtgPnniCfgNodeNbrStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 3, 3, 1, 1, 4),
    _ARtgPnniCfgNodeNbrStorageType_Type()
)
aRtgPnniCfgNodeNbrStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aRtgPnniCfgNodeNbrStorageType.setStatus("mandatory")


class _ARtgPnniCfgNodeNbrIndex_Type(HexString):
    """Custom type aRtgPnniCfgNodeNbrIndex based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(22, 22),
    )


_ARtgPnniCfgNodeNbrIndex_Type.__name__ = "HexString"
_ARtgPnniCfgNodeNbrIndex_Object = MibTableColumn
aRtgPnniCfgNodeNbrIndex = _ARtgPnniCfgNodeNbrIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 3, 3, 1, 1, 10),
    _ARtgPnniCfgNodeNbrIndex_Type()
)
aRtgPnniCfgNodeNbrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aRtgPnniCfgNodeNbrIndex.setStatus("mandatory")
_ARtgPnniCfgNodeNbrOperTable_Object = MibTable
aRtgPnniCfgNodeNbrOperTable = _ARtgPnniCfgNodeNbrOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 3, 3, 10)
)
if mibBuilder.loadTexts:
    aRtgPnniCfgNodeNbrOperTable.setStatus("mandatory")
_ARtgPnniCfgNodeNbrOperEntry_Object = MibTableRow
aRtgPnniCfgNodeNbrOperEntry = _ARtgPnniCfgNodeNbrOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 3, 3, 10, 1)
)
aRtgPnniCfgNodeNbrOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "aRtgIndex"),
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "aRtgPnniIndex"),
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "aRtgPnniCfgNodeIndex"),
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "aRtgPnniCfgNodeNbrIndex"),
)
if mibBuilder.loadTexts:
    aRtgPnniCfgNodeNbrOperEntry.setStatus("mandatory")


class _ARtgPnniCfgNodeNbrPeerState_Type(Integer32):
    """Custom type aRtgPnniCfgNodeNbrPeerState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("exchanging", 2),
          ("full", 4),
          ("loading", 3),
          ("negotiating", 1),
          ("npDown", 0))
    )


_ARtgPnniCfgNodeNbrPeerState_Type.__name__ = "Integer32"
_ARtgPnniCfgNodeNbrPeerState_Object = MibTableColumn
aRtgPnniCfgNodeNbrPeerState = _ARtgPnniCfgNodeNbrPeerState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 3, 3, 10, 1, 2),
    _ARtgPnniCfgNodeNbrPeerState_Type()
)
aRtgPnniCfgNodeNbrPeerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aRtgPnniCfgNodeNbrPeerState.setStatus("mandatory")
_ARtgPnniCfgNodeNbrStatsTable_Object = MibTable
aRtgPnniCfgNodeNbrStatsTable = _ARtgPnniCfgNodeNbrStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 3, 3, 11)
)
if mibBuilder.loadTexts:
    aRtgPnniCfgNodeNbrStatsTable.setStatus("mandatory")
_ARtgPnniCfgNodeNbrStatsEntry_Object = MibTableRow
aRtgPnniCfgNodeNbrStatsEntry = _ARtgPnniCfgNodeNbrStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 3, 3, 11, 1)
)
aRtgPnniCfgNodeNbrStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "aRtgIndex"),
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "aRtgPnniIndex"),
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "aRtgPnniCfgNodeIndex"),
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "aRtgPnniCfgNodeNbrIndex"),
)
if mibBuilder.loadTexts:
    aRtgPnniCfgNodeNbrStatsEntry.setStatus("mandatory")
_ARtgPnniCfgNodeNbrPtspRx_Type = Counter32
_ARtgPnniCfgNodeNbrPtspRx_Object = MibTableColumn
aRtgPnniCfgNodeNbrPtspRx = _ARtgPnniCfgNodeNbrPtspRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 3, 3, 11, 1, 1),
    _ARtgPnniCfgNodeNbrPtspRx_Type()
)
aRtgPnniCfgNodeNbrPtspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aRtgPnniCfgNodeNbrPtspRx.setStatus("mandatory")
_ARtgPnniCfgNodeNbrPtspTx_Type = Counter32
_ARtgPnniCfgNodeNbrPtspTx_Object = MibTableColumn
aRtgPnniCfgNodeNbrPtspTx = _ARtgPnniCfgNodeNbrPtspTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 3, 3, 11, 1, 2),
    _ARtgPnniCfgNodeNbrPtspTx_Type()
)
aRtgPnniCfgNodeNbrPtspTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aRtgPnniCfgNodeNbrPtspTx.setStatus("mandatory")
_ARtgPnniCfgNodeNbrPtseRx_Type = Counter32
_ARtgPnniCfgNodeNbrPtseRx_Object = MibTableColumn
aRtgPnniCfgNodeNbrPtseRx = _ARtgPnniCfgNodeNbrPtseRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 3, 3, 11, 1, 3),
    _ARtgPnniCfgNodeNbrPtseRx_Type()
)
aRtgPnniCfgNodeNbrPtseRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aRtgPnniCfgNodeNbrPtseRx.setStatus("mandatory")
_ARtgPnniCfgNodeNbrPtseTx_Type = Counter32
_ARtgPnniCfgNodeNbrPtseTx_Object = MibTableColumn
aRtgPnniCfgNodeNbrPtseTx = _ARtgPnniCfgNodeNbrPtseTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 3, 3, 11, 1, 4),
    _ARtgPnniCfgNodeNbrPtseTx_Type()
)
aRtgPnniCfgNodeNbrPtseTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aRtgPnniCfgNodeNbrPtseTx.setStatus("mandatory")
_ARtgPnniCfgNodeNbrPtseReqRx_Type = Counter32
_ARtgPnniCfgNodeNbrPtseReqRx_Object = MibTableColumn
aRtgPnniCfgNodeNbrPtseReqRx = _ARtgPnniCfgNodeNbrPtseReqRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 3, 3, 11, 1, 5),
    _ARtgPnniCfgNodeNbrPtseReqRx_Type()
)
aRtgPnniCfgNodeNbrPtseReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aRtgPnniCfgNodeNbrPtseReqRx.setStatus("mandatory")
_ARtgPnniCfgNodeNbrPtseReqTx_Type = Counter32
_ARtgPnniCfgNodeNbrPtseReqTx_Object = MibTableColumn
aRtgPnniCfgNodeNbrPtseReqTx = _ARtgPnniCfgNodeNbrPtseReqTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 3, 3, 11, 1, 6),
    _ARtgPnniCfgNodeNbrPtseReqTx_Type()
)
aRtgPnniCfgNodeNbrPtseReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aRtgPnniCfgNodeNbrPtseReqTx.setStatus("mandatory")
_ARtgPnniCfgNodeNbrPtseAcksRx_Type = Counter32
_ARtgPnniCfgNodeNbrPtseAcksRx_Object = MibTableColumn
aRtgPnniCfgNodeNbrPtseAcksRx = _ARtgPnniCfgNodeNbrPtseAcksRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 3, 3, 11, 1, 7),
    _ARtgPnniCfgNodeNbrPtseAcksRx_Type()
)
aRtgPnniCfgNodeNbrPtseAcksRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aRtgPnniCfgNodeNbrPtseAcksRx.setStatus("mandatory")
_ARtgPnniCfgNodeNbrPtseAcksTx_Type = Counter32
_ARtgPnniCfgNodeNbrPtseAcksTx_Object = MibTableColumn
aRtgPnniCfgNodeNbrPtseAcksTx = _ARtgPnniCfgNodeNbrPtseAcksTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 3, 3, 11, 1, 8),
    _ARtgPnniCfgNodeNbrPtseAcksTx_Type()
)
aRtgPnniCfgNodeNbrPtseAcksTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aRtgPnniCfgNodeNbrPtseAcksTx.setStatus("mandatory")
_ARtgPnniCfgNodeNbrDbSummariesRx_Type = Counter32
_ARtgPnniCfgNodeNbrDbSummariesRx_Object = MibTableColumn
aRtgPnniCfgNodeNbrDbSummariesRx = _ARtgPnniCfgNodeNbrDbSummariesRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 3, 3, 11, 1, 9),
    _ARtgPnniCfgNodeNbrDbSummariesRx_Type()
)
aRtgPnniCfgNodeNbrDbSummariesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aRtgPnniCfgNodeNbrDbSummariesRx.setStatus("mandatory")
_ARtgPnniCfgNodeNbrDbSummariesTx_Type = Counter32
_ARtgPnniCfgNodeNbrDbSummariesTx_Object = MibTableColumn
aRtgPnniCfgNodeNbrDbSummariesTx = _ARtgPnniCfgNodeNbrDbSummariesTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 3, 3, 11, 1, 10),
    _ARtgPnniCfgNodeNbrDbSummariesTx_Type()
)
aRtgPnniCfgNodeNbrDbSummariesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aRtgPnniCfgNodeNbrDbSummariesTx.setStatus("mandatory")
_ARtgPnniCfgNodeNbrBadPtspRx_Type = Counter32
_ARtgPnniCfgNodeNbrBadPtspRx_Object = MibTableColumn
aRtgPnniCfgNodeNbrBadPtspRx = _ARtgPnniCfgNodeNbrBadPtspRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 3, 3, 11, 1, 11),
    _ARtgPnniCfgNodeNbrBadPtspRx_Type()
)
aRtgPnniCfgNodeNbrBadPtspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aRtgPnniCfgNodeNbrBadPtspRx.setStatus("mandatory")
_ARtgPnniCfgNodeNbrBadPtseRx_Type = Counter32
_ARtgPnniCfgNodeNbrBadPtseRx_Object = MibTableColumn
aRtgPnniCfgNodeNbrBadPtseRx = _ARtgPnniCfgNodeNbrBadPtseRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 3, 3, 11, 1, 12),
    _ARtgPnniCfgNodeNbrBadPtseRx_Type()
)
aRtgPnniCfgNodeNbrBadPtseRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aRtgPnniCfgNodeNbrBadPtseRx.setStatus("mandatory")
_ARtgPnniCfgNodeNbrBadPtseReqRx_Type = Counter32
_ARtgPnniCfgNodeNbrBadPtseReqRx_Object = MibTableColumn
aRtgPnniCfgNodeNbrBadPtseReqRx = _ARtgPnniCfgNodeNbrBadPtseReqRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 3, 3, 11, 1, 13),
    _ARtgPnniCfgNodeNbrBadPtseReqRx_Type()
)
aRtgPnniCfgNodeNbrBadPtseReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aRtgPnniCfgNodeNbrBadPtseReqRx.setStatus("mandatory")
_ARtgPnniCfgNodeNbrBadPtseAckRx_Type = Counter32
_ARtgPnniCfgNodeNbrBadPtseAckRx_Object = MibTableColumn
aRtgPnniCfgNodeNbrBadPtseAckRx = _ARtgPnniCfgNodeNbrBadPtseAckRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 3, 3, 11, 1, 14),
    _ARtgPnniCfgNodeNbrBadPtseAckRx_Type()
)
aRtgPnniCfgNodeNbrBadPtseAckRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aRtgPnniCfgNodeNbrBadPtseAckRx.setStatus("mandatory")
_ARtgPnniCfgNodeNbrBadDbSummariesRx_Type = Counter32
_ARtgPnniCfgNodeNbrBadDbSummariesRx_Object = MibTableColumn
aRtgPnniCfgNodeNbrBadDbSummariesRx = _ARtgPnniCfgNodeNbrBadDbSummariesRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 3, 3, 11, 1, 15),
    _ARtgPnniCfgNodeNbrBadDbSummariesRx_Type()
)
aRtgPnniCfgNodeNbrBadDbSummariesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aRtgPnniCfgNodeNbrBadDbSummariesRx.setStatus("mandatory")
_ARtgPnniCfgNodeNbrRccListTable_Object = MibTable
aRtgPnniCfgNodeNbrRccListTable = _ARtgPnniCfgNodeNbrRccListTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 3, 3, 385)
)
if mibBuilder.loadTexts:
    aRtgPnniCfgNodeNbrRccListTable.setStatus("mandatory")
_ARtgPnniCfgNodeNbrRccListEntry_Object = MibTableRow
aRtgPnniCfgNodeNbrRccListEntry = _ARtgPnniCfgNodeNbrRccListEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 3, 3, 385, 1)
)
aRtgPnniCfgNodeNbrRccListEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "aRtgIndex"),
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "aRtgPnniIndex"),
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "aRtgPnniCfgNodeIndex"),
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "aRtgPnniCfgNodeNbrIndex"),
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "aRtgPnniCfgNodeNbrRccListValue"),
)
if mibBuilder.loadTexts:
    aRtgPnniCfgNodeNbrRccListEntry.setStatus("mandatory")
_ARtgPnniCfgNodeNbrRccListValue_Type = RowPointer
_ARtgPnniCfgNodeNbrRccListValue_Object = MibTableColumn
aRtgPnniCfgNodeNbrRccListValue = _ARtgPnniCfgNodeNbrRccListValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 3, 3, 385, 1, 1),
    _ARtgPnniCfgNodeNbrRccListValue_Type()
)
aRtgPnniCfgNodeNbrRccListValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aRtgPnniCfgNodeNbrRccListValue.setStatus("mandatory")
_ARtgPnniCfgNodeDefSAddr_ObjectIdentity = ObjectIdentity
aRtgPnniCfgNodeDefSAddr = _ARtgPnniCfgNodeDefSAddr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 3, 4)
)
_ARtgPnniCfgNodeDefSAddrRowStatusTable_Object = MibTable
aRtgPnniCfgNodeDefSAddrRowStatusTable = _ARtgPnniCfgNodeDefSAddrRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 3, 4, 1)
)
if mibBuilder.loadTexts:
    aRtgPnniCfgNodeDefSAddrRowStatusTable.setStatus("mandatory")
_ARtgPnniCfgNodeDefSAddrRowStatusEntry_Object = MibTableRow
aRtgPnniCfgNodeDefSAddrRowStatusEntry = _ARtgPnniCfgNodeDefSAddrRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 3, 4, 1, 1)
)
aRtgPnniCfgNodeDefSAddrRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "aRtgIndex"),
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "aRtgPnniIndex"),
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "aRtgPnniCfgNodeIndex"),
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "aRtgPnniCfgNodeDefSAddrIndex"),
)
if mibBuilder.loadTexts:
    aRtgPnniCfgNodeDefSAddrRowStatusEntry.setStatus("mandatory")
_ARtgPnniCfgNodeDefSAddrRowStatus_Type = RowStatus
_ARtgPnniCfgNodeDefSAddrRowStatus_Object = MibTableColumn
aRtgPnniCfgNodeDefSAddrRowStatus = _ARtgPnniCfgNodeDefSAddrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 3, 4, 1, 1, 1),
    _ARtgPnniCfgNodeDefSAddrRowStatus_Type()
)
aRtgPnniCfgNodeDefSAddrRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aRtgPnniCfgNodeDefSAddrRowStatus.setStatus("mandatory")
_ARtgPnniCfgNodeDefSAddrComponentName_Type = DisplayString
_ARtgPnniCfgNodeDefSAddrComponentName_Object = MibTableColumn
aRtgPnniCfgNodeDefSAddrComponentName = _ARtgPnniCfgNodeDefSAddrComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 3, 4, 1, 1, 2),
    _ARtgPnniCfgNodeDefSAddrComponentName_Type()
)
aRtgPnniCfgNodeDefSAddrComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aRtgPnniCfgNodeDefSAddrComponentName.setStatus("mandatory")
_ARtgPnniCfgNodeDefSAddrStorageType_Type = StorageType
_ARtgPnniCfgNodeDefSAddrStorageType_Object = MibTableColumn
aRtgPnniCfgNodeDefSAddrStorageType = _ARtgPnniCfgNodeDefSAddrStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 3, 4, 1, 1, 4),
    _ARtgPnniCfgNodeDefSAddrStorageType_Type()
)
aRtgPnniCfgNodeDefSAddrStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aRtgPnniCfgNodeDefSAddrStorageType.setStatus("mandatory")
_ARtgPnniCfgNodeDefSAddrIndex_Type = NonReplicated
_ARtgPnniCfgNodeDefSAddrIndex_Object = MibTableColumn
aRtgPnniCfgNodeDefSAddrIndex = _ARtgPnniCfgNodeDefSAddrIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 3, 4, 1, 1, 10),
    _ARtgPnniCfgNodeDefSAddrIndex_Type()
)
aRtgPnniCfgNodeDefSAddrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aRtgPnniCfgNodeDefSAddrIndex.setStatus("mandatory")
_ARtgPnniCfgNodeDefSAddrDefAddrTable_Object = MibTable
aRtgPnniCfgNodeDefSAddrDefAddrTable = _ARtgPnniCfgNodeDefSAddrDefAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 3, 4, 10)
)
if mibBuilder.loadTexts:
    aRtgPnniCfgNodeDefSAddrDefAddrTable.setStatus("mandatory")
_ARtgPnniCfgNodeDefSAddrDefAddrEntry_Object = MibTableRow
aRtgPnniCfgNodeDefSAddrDefAddrEntry = _ARtgPnniCfgNodeDefSAddrDefAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 3, 4, 10, 1)
)
aRtgPnniCfgNodeDefSAddrDefAddrEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "aRtgIndex"),
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "aRtgPnniIndex"),
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "aRtgPnniCfgNodeIndex"),
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "aRtgPnniCfgNodeDefSAddrIndex"),
)
if mibBuilder.loadTexts:
    aRtgPnniCfgNodeDefSAddrDefAddrEntry.setStatus("mandatory")


class _ARtgPnniCfgNodeDefSAddrAddress_Type(HexString):
    """Custom type aRtgPnniCfgNodeDefSAddrAddress based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(13, 13),
    )


_ARtgPnniCfgNodeDefSAddrAddress_Type.__name__ = "HexString"
_ARtgPnniCfgNodeDefSAddrAddress_Object = MibTableColumn
aRtgPnniCfgNodeDefSAddrAddress = _ARtgPnniCfgNodeDefSAddrAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 3, 4, 10, 1, 1),
    _ARtgPnniCfgNodeDefSAddrAddress_Type()
)
aRtgPnniCfgNodeDefSAddrAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aRtgPnniCfgNodeDefSAddrAddress.setStatus("mandatory")
_ARtgPnniCfgNodeDefSAddrOperTable_Object = MibTable
aRtgPnniCfgNodeDefSAddrOperTable = _ARtgPnniCfgNodeDefSAddrOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 3, 4, 11)
)
if mibBuilder.loadTexts:
    aRtgPnniCfgNodeDefSAddrOperTable.setStatus("mandatory")
_ARtgPnniCfgNodeDefSAddrOperEntry_Object = MibTableRow
aRtgPnniCfgNodeDefSAddrOperEntry = _ARtgPnniCfgNodeDefSAddrOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 3, 4, 11, 1)
)
aRtgPnniCfgNodeDefSAddrOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "aRtgIndex"),
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "aRtgPnniIndex"),
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "aRtgPnniCfgNodeIndex"),
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "aRtgPnniCfgNodeDefSAddrIndex"),
)
if mibBuilder.loadTexts:
    aRtgPnniCfgNodeDefSAddrOperEntry.setStatus("mandatory")


class _ARtgPnniCfgNodeDefSAddrState_Type(Integer32):
    """Custom type aRtgPnniCfgNodeDefSAddrState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("advertising", 0),
          ("inactive", 2),
          ("suppressing", 1))
    )


_ARtgPnniCfgNodeDefSAddrState_Type.__name__ = "Integer32"
_ARtgPnniCfgNodeDefSAddrState_Object = MibTableColumn
aRtgPnniCfgNodeDefSAddrState = _ARtgPnniCfgNodeDefSAddrState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 3, 4, 11, 1, 1),
    _ARtgPnniCfgNodeDefSAddrState_Type()
)
aRtgPnniCfgNodeDefSAddrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aRtgPnniCfgNodeDefSAddrState.setStatus("mandatory")


class _ARtgPnniCfgNodeDefSAddrScope_Type(Integer32):
    """Custom type aRtgPnniCfgNodeDefSAddrScope based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 104),
    )


_ARtgPnniCfgNodeDefSAddrScope_Type.__name__ = "Integer32"
_ARtgPnniCfgNodeDefSAddrScope_Object = MibTableColumn
aRtgPnniCfgNodeDefSAddrScope = _ARtgPnniCfgNodeDefSAddrScope_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 3, 4, 11, 1, 2),
    _ARtgPnniCfgNodeDefSAddrScope_Type()
)
aRtgPnniCfgNodeDefSAddrScope.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aRtgPnniCfgNodeDefSAddrScope.setStatus("mandatory")
_ARtgPnniCfgNodeProvTable_Object = MibTable
aRtgPnniCfgNodeProvTable = _ARtgPnniCfgNodeProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 3, 10)
)
if mibBuilder.loadTexts:
    aRtgPnniCfgNodeProvTable.setStatus("mandatory")
_ARtgPnniCfgNodeProvEntry_Object = MibTableRow
aRtgPnniCfgNodeProvEntry = _ARtgPnniCfgNodeProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 3, 10, 1)
)
aRtgPnniCfgNodeProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "aRtgIndex"),
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "aRtgPnniIndex"),
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "aRtgPnniCfgNodeIndex"),
)
if mibBuilder.loadTexts:
    aRtgPnniCfgNodeProvEntry.setStatus("mandatory")


class _ARtgPnniCfgNodeNodeId_Type(HexString):
    """Custom type aRtgPnniCfgNodeNodeId based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 22),
    )


_ARtgPnniCfgNodeNodeId_Type.__name__ = "HexString"
_ARtgPnniCfgNodeNodeId_Object = MibTableColumn
aRtgPnniCfgNodeNodeId = _ARtgPnniCfgNodeNodeId_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 3, 10, 1, 2),
    _ARtgPnniCfgNodeNodeId_Type()
)
aRtgPnniCfgNodeNodeId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aRtgPnniCfgNodeNodeId.setStatus("mandatory")


class _ARtgPnniCfgNodePeerGroupId_Type(HexString):
    """Custom type aRtgPnniCfgNodePeerGroupId based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_ARtgPnniCfgNodePeerGroupId_Type.__name__ = "HexString"
_ARtgPnniCfgNodePeerGroupId_Object = MibTableColumn
aRtgPnniCfgNodePeerGroupId = _ARtgPnniCfgNodePeerGroupId_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 3, 10, 1, 3),
    _ARtgPnniCfgNodePeerGroupId_Type()
)
aRtgPnniCfgNodePeerGroupId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aRtgPnniCfgNodePeerGroupId.setStatus("mandatory")
_ARtgPnniCfgNodeOperTable_Object = MibTable
aRtgPnniCfgNodeOperTable = _ARtgPnniCfgNodeOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 3, 11)
)
if mibBuilder.loadTexts:
    aRtgPnniCfgNodeOperTable.setStatus("mandatory")
_ARtgPnniCfgNodeOperEntry_Object = MibTableRow
aRtgPnniCfgNodeOperEntry = _ARtgPnniCfgNodeOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 3, 11, 1)
)
aRtgPnniCfgNodeOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "aRtgIndex"),
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "aRtgPnniIndex"),
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "aRtgPnniCfgNodeIndex"),
)
if mibBuilder.loadTexts:
    aRtgPnniCfgNodeOperEntry.setStatus("mandatory")


class _ARtgPnniCfgNodeNodeAddress_Type(HexString):
    """Custom type aRtgPnniCfgNodeNodeAddress based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_ARtgPnniCfgNodeNodeAddress_Type.__name__ = "HexString"
_ARtgPnniCfgNodeNodeAddress_Object = MibTableColumn
aRtgPnniCfgNodeNodeAddress = _ARtgPnniCfgNodeNodeAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 3, 11, 1, 1),
    _ARtgPnniCfgNodeNodeAddress_Type()
)
aRtgPnniCfgNodeNodeAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aRtgPnniCfgNodeNodeAddress.setStatus("mandatory")


class _ARtgPnniCfgNodeOpNodeId_Type(HexString):
    """Custom type aRtgPnniCfgNodeOpNodeId based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(22, 22),
    )


_ARtgPnniCfgNodeOpNodeId_Type.__name__ = "HexString"
_ARtgPnniCfgNodeOpNodeId_Object = MibTableColumn
aRtgPnniCfgNodeOpNodeId = _ARtgPnniCfgNodeOpNodeId_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 3, 11, 1, 2),
    _ARtgPnniCfgNodeOpNodeId_Type()
)
aRtgPnniCfgNodeOpNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aRtgPnniCfgNodeOpNodeId.setStatus("mandatory")


class _ARtgPnniCfgNodeOpPeerGroupId_Type(HexString):
    """Custom type aRtgPnniCfgNodeOpPeerGroupId based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(14, 14),
    )


_ARtgPnniCfgNodeOpPeerGroupId_Type.__name__ = "HexString"
_ARtgPnniCfgNodeOpPeerGroupId_Object = MibTableColumn
aRtgPnniCfgNodeOpPeerGroupId = _ARtgPnniCfgNodeOpPeerGroupId_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 3, 11, 1, 3),
    _ARtgPnniCfgNodeOpPeerGroupId_Type()
)
aRtgPnniCfgNodeOpPeerGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aRtgPnniCfgNodeOpPeerGroupId.setStatus("mandatory")


class _ARtgPnniCfgNodeNumNeighbors_Type(Unsigned32):
    """Custom type aRtgPnniCfgNodeNumNeighbors based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ARtgPnniCfgNodeNumNeighbors_Type.__name__ = "Unsigned32"
_ARtgPnniCfgNodeNumNeighbors_Object = MibTableColumn
aRtgPnniCfgNodeNumNeighbors = _ARtgPnniCfgNodeNumNeighbors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 3, 11, 1, 4),
    _ARtgPnniCfgNodeNumNeighbors_Type()
)
aRtgPnniCfgNodeNumNeighbors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aRtgPnniCfgNodeNumNeighbors.setStatus("mandatory")


class _ARtgPnniCfgNodeNumRccs_Type(Unsigned32):
    """Custom type aRtgPnniCfgNodeNumRccs based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ARtgPnniCfgNodeNumRccs_Type.__name__ = "Unsigned32"
_ARtgPnniCfgNodeNumRccs_Object = MibTableColumn
aRtgPnniCfgNodeNumRccs = _ARtgPnniCfgNodeNumRccs_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 3, 11, 1, 5),
    _ARtgPnniCfgNodeNumRccs_Type()
)
aRtgPnniCfgNodeNumRccs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aRtgPnniCfgNodeNumRccs.setStatus("mandatory")


class _ARtgPnniCfgNodeCurrentLeadershipPriority_Type(Unsigned32):
    """Custom type aRtgPnniCfgNodeCurrentLeadershipPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 205),
    )


_ARtgPnniCfgNodeCurrentLeadershipPriority_Type.__name__ = "Unsigned32"
_ARtgPnniCfgNodeCurrentLeadershipPriority_Object = MibTableColumn
aRtgPnniCfgNodeCurrentLeadershipPriority = _ARtgPnniCfgNodeCurrentLeadershipPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 3, 11, 1, 6),
    _ARtgPnniCfgNodeCurrentLeadershipPriority_Type()
)
aRtgPnniCfgNodeCurrentLeadershipPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aRtgPnniCfgNodeCurrentLeadershipPriority.setStatus("mandatory")


class _ARtgPnniCfgNodePglElectionState_Type(Integer32):
    """Custom type aRtgPnniCfgNodePglElectionState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("awaitReElection", 9),
          ("awaitUnanimity", 7),
          ("awaiting", 1),
          ("awaitingFull", 2),
          ("calculating", 4),
          ("hungElection", 8),
          ("initialDelay", 3),
          ("operNotPgl", 5),
          ("operPgl", 6),
          ("starting", 0))
    )


_ARtgPnniCfgNodePglElectionState_Type.__name__ = "Integer32"
_ARtgPnniCfgNodePglElectionState_Object = MibTableColumn
aRtgPnniCfgNodePglElectionState = _ARtgPnniCfgNodePglElectionState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 3, 11, 1, 7),
    _ARtgPnniCfgNodePglElectionState_Type()
)
aRtgPnniCfgNodePglElectionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aRtgPnniCfgNodePglElectionState.setStatus("mandatory")
_ARtgPnniTop_ObjectIdentity = ObjectIdentity
aRtgPnniTop = _ARtgPnniTop_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 4)
)
_ARtgPnniTopRowStatusTable_Object = MibTable
aRtgPnniTopRowStatusTable = _ARtgPnniTopRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 4, 1)
)
if mibBuilder.loadTexts:
    aRtgPnniTopRowStatusTable.setStatus("mandatory")
_ARtgPnniTopRowStatusEntry_Object = MibTableRow
aRtgPnniTopRowStatusEntry = _ARtgPnniTopRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 4, 1, 1)
)
aRtgPnniTopRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "aRtgIndex"),
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "aRtgPnniIndex"),
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "aRtgPnniTopIndex"),
)
if mibBuilder.loadTexts:
    aRtgPnniTopRowStatusEntry.setStatus("mandatory")
_ARtgPnniTopRowStatus_Type = RowStatus
_ARtgPnniTopRowStatus_Object = MibTableColumn
aRtgPnniTopRowStatus = _ARtgPnniTopRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 4, 1, 1, 1),
    _ARtgPnniTopRowStatus_Type()
)
aRtgPnniTopRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aRtgPnniTopRowStatus.setStatus("mandatory")
_ARtgPnniTopComponentName_Type = DisplayString
_ARtgPnniTopComponentName_Object = MibTableColumn
aRtgPnniTopComponentName = _ARtgPnniTopComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 4, 1, 1, 2),
    _ARtgPnniTopComponentName_Type()
)
aRtgPnniTopComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aRtgPnniTopComponentName.setStatus("mandatory")
_ARtgPnniTopStorageType_Type = StorageType
_ARtgPnniTopStorageType_Object = MibTableColumn
aRtgPnniTopStorageType = _ARtgPnniTopStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 4, 1, 1, 4),
    _ARtgPnniTopStorageType_Type()
)
aRtgPnniTopStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aRtgPnniTopStorageType.setStatus("mandatory")


class _ARtgPnniTopIndex_Type(Integer32):
    """Custom type aRtgPnniTopIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 104),
    )


_ARtgPnniTopIndex_Type.__name__ = "Integer32"
_ARtgPnniTopIndex_Object = MibTableColumn
aRtgPnniTopIndex = _ARtgPnniTopIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 4, 1, 1, 10),
    _ARtgPnniTopIndex_Type()
)
aRtgPnniTopIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aRtgPnniTopIndex.setStatus("mandatory")
_ARtgPnniTopNode_ObjectIdentity = ObjectIdentity
aRtgPnniTopNode = _ARtgPnniTopNode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 4, 2)
)
_ARtgPnniTopNodeRowStatusTable_Object = MibTable
aRtgPnniTopNodeRowStatusTable = _ARtgPnniTopNodeRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 4, 2, 1)
)
if mibBuilder.loadTexts:
    aRtgPnniTopNodeRowStatusTable.setStatus("mandatory")
_ARtgPnniTopNodeRowStatusEntry_Object = MibTableRow
aRtgPnniTopNodeRowStatusEntry = _ARtgPnniTopNodeRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 4, 2, 1, 1)
)
aRtgPnniTopNodeRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "aRtgIndex"),
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "aRtgPnniIndex"),
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "aRtgPnniTopIndex"),
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "aRtgPnniTopNodeIndex"),
)
if mibBuilder.loadTexts:
    aRtgPnniTopNodeRowStatusEntry.setStatus("mandatory")
_ARtgPnniTopNodeRowStatus_Type = RowStatus
_ARtgPnniTopNodeRowStatus_Object = MibTableColumn
aRtgPnniTopNodeRowStatus = _ARtgPnniTopNodeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 4, 2, 1, 1, 1),
    _ARtgPnniTopNodeRowStatus_Type()
)
aRtgPnniTopNodeRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aRtgPnniTopNodeRowStatus.setStatus("mandatory")
_ARtgPnniTopNodeComponentName_Type = DisplayString
_ARtgPnniTopNodeComponentName_Object = MibTableColumn
aRtgPnniTopNodeComponentName = _ARtgPnniTopNodeComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 4, 2, 1, 1, 2),
    _ARtgPnniTopNodeComponentName_Type()
)
aRtgPnniTopNodeComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aRtgPnniTopNodeComponentName.setStatus("mandatory")
_ARtgPnniTopNodeStorageType_Type = StorageType
_ARtgPnniTopNodeStorageType_Object = MibTableColumn
aRtgPnniTopNodeStorageType = _ARtgPnniTopNodeStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 4, 2, 1, 1, 4),
    _ARtgPnniTopNodeStorageType_Type()
)
aRtgPnniTopNodeStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aRtgPnniTopNodeStorageType.setStatus("mandatory")


class _ARtgPnniTopNodeIndex_Type(HexString):
    """Custom type aRtgPnniTopNodeIndex based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(22, 22),
    )


_ARtgPnniTopNodeIndex_Type.__name__ = "HexString"
_ARtgPnniTopNodeIndex_Object = MibTableColumn
aRtgPnniTopNodeIndex = _ARtgPnniTopNodeIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 4, 2, 1, 1, 10),
    _ARtgPnniTopNodeIndex_Type()
)
aRtgPnniTopNodeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aRtgPnniTopNodeIndex.setStatus("mandatory")
_ARtgPnniTopNodeAddr_ObjectIdentity = ObjectIdentity
aRtgPnniTopNodeAddr = _ARtgPnniTopNodeAddr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 4, 2, 2)
)
_ARtgPnniTopNodeAddrRowStatusTable_Object = MibTable
aRtgPnniTopNodeAddrRowStatusTable = _ARtgPnniTopNodeAddrRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 4, 2, 2, 1)
)
if mibBuilder.loadTexts:
    aRtgPnniTopNodeAddrRowStatusTable.setStatus("mandatory")
_ARtgPnniTopNodeAddrRowStatusEntry_Object = MibTableRow
aRtgPnniTopNodeAddrRowStatusEntry = _ARtgPnniTopNodeAddrRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 4, 2, 2, 1, 1)
)
aRtgPnniTopNodeAddrRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "aRtgIndex"),
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "aRtgPnniIndex"),
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "aRtgPnniTopIndex"),
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "aRtgPnniTopNodeIndex"),
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "aRtgPnniTopNodeAddrAddressIndex"),
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "aRtgPnniTopNodeAddrPrefixLengthIndex"),
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "aRtgPnniTopNodeAddrReachabilityIndex"),
)
if mibBuilder.loadTexts:
    aRtgPnniTopNodeAddrRowStatusEntry.setStatus("mandatory")
_ARtgPnniTopNodeAddrRowStatus_Type = RowStatus
_ARtgPnniTopNodeAddrRowStatus_Object = MibTableColumn
aRtgPnniTopNodeAddrRowStatus = _ARtgPnniTopNodeAddrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 4, 2, 2, 1, 1, 1),
    _ARtgPnniTopNodeAddrRowStatus_Type()
)
aRtgPnniTopNodeAddrRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aRtgPnniTopNodeAddrRowStatus.setStatus("mandatory")
_ARtgPnniTopNodeAddrComponentName_Type = DisplayString
_ARtgPnniTopNodeAddrComponentName_Object = MibTableColumn
aRtgPnniTopNodeAddrComponentName = _ARtgPnniTopNodeAddrComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 4, 2, 2, 1, 1, 2),
    _ARtgPnniTopNodeAddrComponentName_Type()
)
aRtgPnniTopNodeAddrComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aRtgPnniTopNodeAddrComponentName.setStatus("mandatory")
_ARtgPnniTopNodeAddrStorageType_Type = StorageType
_ARtgPnniTopNodeAddrStorageType_Object = MibTableColumn
aRtgPnniTopNodeAddrStorageType = _ARtgPnniTopNodeAddrStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 4, 2, 2, 1, 1, 4),
    _ARtgPnniTopNodeAddrStorageType_Type()
)
aRtgPnniTopNodeAddrStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aRtgPnniTopNodeAddrStorageType.setStatus("mandatory")


class _ARtgPnniTopNodeAddrAddressIndex_Type(HexString):
    """Custom type aRtgPnniTopNodeAddrAddressIndex based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(19, 19),
    )


_ARtgPnniTopNodeAddrAddressIndex_Type.__name__ = "HexString"
_ARtgPnniTopNodeAddrAddressIndex_Object = MibTableColumn
aRtgPnniTopNodeAddrAddressIndex = _ARtgPnniTopNodeAddrAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 4, 2, 2, 1, 1, 10),
    _ARtgPnniTopNodeAddrAddressIndex_Type()
)
aRtgPnniTopNodeAddrAddressIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aRtgPnniTopNodeAddrAddressIndex.setStatus("mandatory")


class _ARtgPnniTopNodeAddrPrefixLengthIndex_Type(Integer32):
    """Custom type aRtgPnniTopNodeAddrPrefixLengthIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 152),
    )


_ARtgPnniTopNodeAddrPrefixLengthIndex_Type.__name__ = "Integer32"
_ARtgPnniTopNodeAddrPrefixLengthIndex_Object = MibTableColumn
aRtgPnniTopNodeAddrPrefixLengthIndex = _ARtgPnniTopNodeAddrPrefixLengthIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 4, 2, 2, 1, 1, 11),
    _ARtgPnniTopNodeAddrPrefixLengthIndex_Type()
)
aRtgPnniTopNodeAddrPrefixLengthIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aRtgPnniTopNodeAddrPrefixLengthIndex.setStatus("mandatory")


class _ARtgPnniTopNodeAddrReachabilityIndex_Type(Integer32):
    """Custom type aRtgPnniTopNodeAddrReachabilityIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("exterior", 1),
          ("internal", 0))
    )


_ARtgPnniTopNodeAddrReachabilityIndex_Type.__name__ = "Integer32"
_ARtgPnniTopNodeAddrReachabilityIndex_Object = MibTableColumn
aRtgPnniTopNodeAddrReachabilityIndex = _ARtgPnniTopNodeAddrReachabilityIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 4, 2, 2, 1, 1, 12),
    _ARtgPnniTopNodeAddrReachabilityIndex_Type()
)
aRtgPnniTopNodeAddrReachabilityIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aRtgPnniTopNodeAddrReachabilityIndex.setStatus("mandatory")
_ARtgPnniTopNodeAddrOperTable_Object = MibTable
aRtgPnniTopNodeAddrOperTable = _ARtgPnniTopNodeAddrOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 4, 2, 2, 10)
)
if mibBuilder.loadTexts:
    aRtgPnniTopNodeAddrOperTable.setStatus("mandatory")
_ARtgPnniTopNodeAddrOperEntry_Object = MibTableRow
aRtgPnniTopNodeAddrOperEntry = _ARtgPnniTopNodeAddrOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 4, 2, 2, 10, 1)
)
aRtgPnniTopNodeAddrOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "aRtgIndex"),
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "aRtgPnniIndex"),
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "aRtgPnniTopIndex"),
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "aRtgPnniTopNodeIndex"),
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "aRtgPnniTopNodeAddrAddressIndex"),
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "aRtgPnniTopNodeAddrPrefixLengthIndex"),
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "aRtgPnniTopNodeAddrReachabilityIndex"),
)
if mibBuilder.loadTexts:
    aRtgPnniTopNodeAddrOperEntry.setStatus("mandatory")


class _ARtgPnniTopNodeAddrScope_Type(Unsigned32):
    """Custom type aRtgPnniTopNodeAddrScope based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 104),
    )


_ARtgPnniTopNodeAddrScope_Type.__name__ = "Unsigned32"
_ARtgPnniTopNodeAddrScope_Object = MibTableColumn
aRtgPnniTopNodeAddrScope = _ARtgPnniTopNodeAddrScope_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 4, 2, 2, 10, 1, 1),
    _ARtgPnniTopNodeAddrScope_Type()
)
aRtgPnniTopNodeAddrScope.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aRtgPnniTopNodeAddrScope.setStatus("mandatory")
_ARtgPnniTopNodeLink_ObjectIdentity = ObjectIdentity
aRtgPnniTopNodeLink = _ARtgPnniTopNodeLink_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 4, 2, 3)
)
_ARtgPnniTopNodeLinkRowStatusTable_Object = MibTable
aRtgPnniTopNodeLinkRowStatusTable = _ARtgPnniTopNodeLinkRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 4, 2, 3, 1)
)
if mibBuilder.loadTexts:
    aRtgPnniTopNodeLinkRowStatusTable.setStatus("mandatory")
_ARtgPnniTopNodeLinkRowStatusEntry_Object = MibTableRow
aRtgPnniTopNodeLinkRowStatusEntry = _ARtgPnniTopNodeLinkRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 4, 2, 3, 1, 1)
)
aRtgPnniTopNodeLinkRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "aRtgIndex"),
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "aRtgPnniIndex"),
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "aRtgPnniTopIndex"),
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "aRtgPnniTopNodeIndex"),
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "aRtgPnniTopNodeLinkIndex"),
)
if mibBuilder.loadTexts:
    aRtgPnniTopNodeLinkRowStatusEntry.setStatus("mandatory")
_ARtgPnniTopNodeLinkRowStatus_Type = RowStatus
_ARtgPnniTopNodeLinkRowStatus_Object = MibTableColumn
aRtgPnniTopNodeLinkRowStatus = _ARtgPnniTopNodeLinkRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 4, 2, 3, 1, 1, 1),
    _ARtgPnniTopNodeLinkRowStatus_Type()
)
aRtgPnniTopNodeLinkRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aRtgPnniTopNodeLinkRowStatus.setStatus("mandatory")
_ARtgPnniTopNodeLinkComponentName_Type = DisplayString
_ARtgPnniTopNodeLinkComponentName_Object = MibTableColumn
aRtgPnniTopNodeLinkComponentName = _ARtgPnniTopNodeLinkComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 4, 2, 3, 1, 1, 2),
    _ARtgPnniTopNodeLinkComponentName_Type()
)
aRtgPnniTopNodeLinkComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aRtgPnniTopNodeLinkComponentName.setStatus("mandatory")
_ARtgPnniTopNodeLinkStorageType_Type = StorageType
_ARtgPnniTopNodeLinkStorageType_Object = MibTableColumn
aRtgPnniTopNodeLinkStorageType = _ARtgPnniTopNodeLinkStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 4, 2, 3, 1, 1, 4),
    _ARtgPnniTopNodeLinkStorageType_Type()
)
aRtgPnniTopNodeLinkStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aRtgPnniTopNodeLinkStorageType.setStatus("mandatory")


class _ARtgPnniTopNodeLinkIndex_Type(Integer32):
    """Custom type aRtgPnniTopNodeLinkIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 268435455),
    )


_ARtgPnniTopNodeLinkIndex_Type.__name__ = "Integer32"
_ARtgPnniTopNodeLinkIndex_Object = MibTableColumn
aRtgPnniTopNodeLinkIndex = _ARtgPnniTopNodeLinkIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 4, 2, 3, 1, 1, 10),
    _ARtgPnniTopNodeLinkIndex_Type()
)
aRtgPnniTopNodeLinkIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aRtgPnniTopNodeLinkIndex.setStatus("mandatory")
_ARtgPnniTopNodeLinkOperTable_Object = MibTable
aRtgPnniTopNodeLinkOperTable = _ARtgPnniTopNodeLinkOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 4, 2, 3, 10)
)
if mibBuilder.loadTexts:
    aRtgPnniTopNodeLinkOperTable.setStatus("mandatory")
_ARtgPnniTopNodeLinkOperEntry_Object = MibTableRow
aRtgPnniTopNodeLinkOperEntry = _ARtgPnniTopNodeLinkOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 4, 2, 3, 10, 1)
)
aRtgPnniTopNodeLinkOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "aRtgIndex"),
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "aRtgPnniIndex"),
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "aRtgPnniTopIndex"),
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "aRtgPnniTopNodeIndex"),
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "aRtgPnniTopNodeLinkIndex"),
)
if mibBuilder.loadTexts:
    aRtgPnniTopNodeLinkOperEntry.setStatus("mandatory")


class _ARtgPnniTopNodeLinkRemoteNodeId_Type(HexString):
    """Custom type aRtgPnniTopNodeLinkRemoteNodeId based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(22, 22),
    )


_ARtgPnniTopNodeLinkRemoteNodeId_Type.__name__ = "HexString"
_ARtgPnniTopNodeLinkRemoteNodeId_Object = MibTableColumn
aRtgPnniTopNodeLinkRemoteNodeId = _ARtgPnniTopNodeLinkRemoteNodeId_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 4, 2, 3, 10, 1, 1),
    _ARtgPnniTopNodeLinkRemoteNodeId_Type()
)
aRtgPnniTopNodeLinkRemoteNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aRtgPnniTopNodeLinkRemoteNodeId.setStatus("mandatory")


class _ARtgPnniTopNodeLinkRemotePortId_Type(Unsigned32):
    """Custom type aRtgPnniTopNodeLinkRemotePortId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_ARtgPnniTopNodeLinkRemotePortId_Type.__name__ = "Unsigned32"
_ARtgPnniTopNodeLinkRemotePortId_Object = MibTableColumn
aRtgPnniTopNodeLinkRemotePortId = _ARtgPnniTopNodeLinkRemotePortId_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 4, 2, 3, 10, 1, 2),
    _ARtgPnniTopNodeLinkRemotePortId_Type()
)
aRtgPnniTopNodeLinkRemotePortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aRtgPnniTopNodeLinkRemotePortId.setStatus("mandatory")
_ARtgPnniTopOperTable_Object = MibTable
aRtgPnniTopOperTable = _ARtgPnniTopOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 4, 10)
)
if mibBuilder.loadTexts:
    aRtgPnniTopOperTable.setStatus("mandatory")
_ARtgPnniTopOperEntry_Object = MibTableRow
aRtgPnniTopOperEntry = _ARtgPnniTopOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 4, 10, 1)
)
aRtgPnniTopOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "aRtgIndex"),
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "aRtgPnniIndex"),
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "aRtgPnniTopIndex"),
)
if mibBuilder.loadTexts:
    aRtgPnniTopOperEntry.setStatus("mandatory")


class _ARtgPnniTopPtsesInDatabase_Type(Gauge32):
    """Custom type aRtgPnniTopPtsesInDatabase based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_ARtgPnniTopPtsesInDatabase_Type.__name__ = "Gauge32"
_ARtgPnniTopPtsesInDatabase_Object = MibTableColumn
aRtgPnniTopPtsesInDatabase = _ARtgPnniTopPtsesInDatabase_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 4, 10, 1, 1),
    _ARtgPnniTopPtsesInDatabase_Type()
)
aRtgPnniTopPtsesInDatabase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aRtgPnniTopPtsesInDatabase.setStatus("mandatory")


class _ARtgPnniTopPglNodeId_Type(HexString):
    """Custom type aRtgPnniTopPglNodeId based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 22),
    )


_ARtgPnniTopPglNodeId_Type.__name__ = "HexString"
_ARtgPnniTopPglNodeId_Object = MibTableColumn
aRtgPnniTopPglNodeId = _ARtgPnniTopPglNodeId_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 4, 10, 1, 2),
    _ARtgPnniTopPglNodeId_Type()
)
aRtgPnniTopPglNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aRtgPnniTopPglNodeId.setStatus("mandatory")


class _ARtgPnniTopActiveParentNodeId_Type(HexString):
    """Custom type aRtgPnniTopActiveParentNodeId based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 22),
    )


_ARtgPnniTopActiveParentNodeId_Type.__name__ = "HexString"
_ARtgPnniTopActiveParentNodeId_Object = MibTableColumn
aRtgPnniTopActiveParentNodeId = _ARtgPnniTopActiveParentNodeId_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 4, 10, 1, 3),
    _ARtgPnniTopActiveParentNodeId_Type()
)
aRtgPnniTopActiveParentNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aRtgPnniTopActiveParentNodeId.setStatus("mandatory")


class _ARtgPnniTopPreferredPglNodeId_Type(HexString):
    """Custom type aRtgPnniTopPreferredPglNodeId based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 22),
    )


_ARtgPnniTopPreferredPglNodeId_Type.__name__ = "HexString"
_ARtgPnniTopPreferredPglNodeId_Object = MibTableColumn
aRtgPnniTopPreferredPglNodeId = _ARtgPnniTopPreferredPglNodeId_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 4, 10, 1, 4),
    _ARtgPnniTopPreferredPglNodeId_Type()
)
aRtgPnniTopPreferredPglNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aRtgPnniTopPreferredPglNodeId.setStatus("mandatory")
_ARtgPnniPort_ObjectIdentity = ObjectIdentity
aRtgPnniPort = _ARtgPnniPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 5)
)
_ARtgPnniPortRowStatusTable_Object = MibTable
aRtgPnniPortRowStatusTable = _ARtgPnniPortRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 5, 1)
)
if mibBuilder.loadTexts:
    aRtgPnniPortRowStatusTable.setStatus("mandatory")
_ARtgPnniPortRowStatusEntry_Object = MibTableRow
aRtgPnniPortRowStatusEntry = _ARtgPnniPortRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 5, 1, 1)
)
aRtgPnniPortRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "aRtgIndex"),
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "aRtgPnniIndex"),
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "aRtgPnniPortIndex"),
)
if mibBuilder.loadTexts:
    aRtgPnniPortRowStatusEntry.setStatus("mandatory")
_ARtgPnniPortRowStatus_Type = RowStatus
_ARtgPnniPortRowStatus_Object = MibTableColumn
aRtgPnniPortRowStatus = _ARtgPnniPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 5, 1, 1, 1),
    _ARtgPnniPortRowStatus_Type()
)
aRtgPnniPortRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aRtgPnniPortRowStatus.setStatus("mandatory")
_ARtgPnniPortComponentName_Type = DisplayString
_ARtgPnniPortComponentName_Object = MibTableColumn
aRtgPnniPortComponentName = _ARtgPnniPortComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 5, 1, 1, 2),
    _ARtgPnniPortComponentName_Type()
)
aRtgPnniPortComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aRtgPnniPortComponentName.setStatus("mandatory")
_ARtgPnniPortStorageType_Type = StorageType
_ARtgPnniPortStorageType_Object = MibTableColumn
aRtgPnniPortStorageType = _ARtgPnniPortStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 5, 1, 1, 4),
    _ARtgPnniPortStorageType_Type()
)
aRtgPnniPortStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aRtgPnniPortStorageType.setStatus("mandatory")


class _ARtgPnniPortIndex_Type(Integer32):
    """Custom type aRtgPnniPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 268435455),
    )


_ARtgPnniPortIndex_Type.__name__ = "Integer32"
_ARtgPnniPortIndex_Object = MibTableColumn
aRtgPnniPortIndex = _ARtgPnniPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 5, 1, 1, 10),
    _ARtgPnniPortIndex_Type()
)
aRtgPnniPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aRtgPnniPortIndex.setStatus("mandatory")
_ARtgPnniPortOperTable_Object = MibTable
aRtgPnniPortOperTable = _ARtgPnniPortOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 5, 10)
)
if mibBuilder.loadTexts:
    aRtgPnniPortOperTable.setStatus("mandatory")
_ARtgPnniPortOperEntry_Object = MibTableRow
aRtgPnniPortOperEntry = _ARtgPnniPortOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 5, 10, 1)
)
aRtgPnniPortOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "aRtgIndex"),
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "aRtgPnniIndex"),
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "aRtgPnniPortIndex"),
)
if mibBuilder.loadTexts:
    aRtgPnniPortOperEntry.setStatus("mandatory")
_ARtgPnniPortStdComponentName_Type = RowPointer
_ARtgPnniPortStdComponentName_Object = MibTableColumn
aRtgPnniPortStdComponentName = _ARtgPnniPortStdComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 5, 10, 1, 1),
    _ARtgPnniPortStdComponentName_Type()
)
aRtgPnniPortStdComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aRtgPnniPortStdComponentName.setStatus("mandatory")
_ARtgPnniProvTable_Object = MibTable
aRtgPnniProvTable = _ARtgPnniProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 10)
)
if mibBuilder.loadTexts:
    aRtgPnniProvTable.setStatus("mandatory")
_ARtgPnniProvEntry_Object = MibTableRow
aRtgPnniProvEntry = _ARtgPnniProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 10, 1)
)
aRtgPnniProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "aRtgIndex"),
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "aRtgPnniIndex"),
)
if mibBuilder.loadTexts:
    aRtgPnniProvEntry.setStatus("mandatory")


class _ARtgPnniNodeAddressPrefix_Type(HexString):
    """Custom type aRtgPnniNodeAddressPrefix based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_ARtgPnniNodeAddressPrefix_Type.__name__ = "HexString"
_ARtgPnniNodeAddressPrefix_Object = MibTableColumn
aRtgPnniNodeAddressPrefix = _ARtgPnniNodeAddressPrefix_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 10, 1, 1),
    _ARtgPnniNodeAddressPrefix_Type()
)
aRtgPnniNodeAddressPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aRtgPnniNodeAddressPrefix.setStatus("mandatory")


class _ARtgPnniDefaultScope_Type(Unsigned32):
    """Custom type aRtgPnniDefaultScope based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 104),
    )


_ARtgPnniDefaultScope_Type.__name__ = "Unsigned32"
_ARtgPnniDefaultScope_Object = MibTableColumn
aRtgPnniDefaultScope = _ARtgPnniDefaultScope_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 10, 1, 2),
    _ARtgPnniDefaultScope_Type()
)
aRtgPnniDefaultScope.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aRtgPnniDefaultScope.setStatus("mandatory")


class _ARtgPnniDomain_Type(AsciiString):
    """Custom type aRtgPnniDomain based on AsciiString"""
    defaultHexValue = "31"

    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ARtgPnniDomain_Type.__name__ = "AsciiString"
_ARtgPnniDomain_Object = MibTableColumn
aRtgPnniDomain = _ARtgPnniDomain_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 10, 1, 3),
    _ARtgPnniDomain_Type()
)
aRtgPnniDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aRtgPnniDomain.setStatus("mandatory")


class _ARtgPnniRestrictTransit_Type(Integer32):
    """Custom type aRtgPnniRestrictTransit based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_ARtgPnniRestrictTransit_Type.__name__ = "Integer32"
_ARtgPnniRestrictTransit_Object = MibTableColumn
aRtgPnniRestrictTransit = _ARtgPnniRestrictTransit_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 10, 1, 4),
    _ARtgPnniRestrictTransit_Type()
)
aRtgPnniRestrictTransit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aRtgPnniRestrictTransit.setStatus("mandatory")


class _ARtgPnniMaxReroutesOnCrankback_Type(Unsigned32):
    """Custom type aRtgPnniMaxReroutesOnCrankback based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_ARtgPnniMaxReroutesOnCrankback_Type.__name__ = "Unsigned32"
_ARtgPnniMaxReroutesOnCrankback_Object = MibTableColumn
aRtgPnniMaxReroutesOnCrankback = _ARtgPnniMaxReroutesOnCrankback_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 10, 1, 5),
    _ARtgPnniMaxReroutesOnCrankback_Type()
)
aRtgPnniMaxReroutesOnCrankback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aRtgPnniMaxReroutesOnCrankback.setStatus("mandatory")
_ARtgPnniPglParmsTable_Object = MibTable
aRtgPnniPglParmsTable = _ARtgPnniPglParmsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 11)
)
if mibBuilder.loadTexts:
    aRtgPnniPglParmsTable.setStatus("mandatory")
_ARtgPnniPglParmsEntry_Object = MibTableRow
aRtgPnniPglParmsEntry = _ARtgPnniPglParmsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 11, 1)
)
aRtgPnniPglParmsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "aRtgIndex"),
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "aRtgPnniIndex"),
)
if mibBuilder.loadTexts:
    aRtgPnniPglParmsEntry.setStatus("mandatory")


class _ARtgPnniPglInitTime_Type(Unsigned32):
    """Custom type aRtgPnniPglInitTime based on Unsigned32"""
    defaultValue = 15

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ARtgPnniPglInitTime_Type.__name__ = "Unsigned32"
_ARtgPnniPglInitTime_Object = MibTableColumn
aRtgPnniPglInitTime = _ARtgPnniPglInitTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 11, 1, 1),
    _ARtgPnniPglInitTime_Type()
)
aRtgPnniPglInitTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aRtgPnniPglInitTime.setStatus("mandatory")


class _ARtgPnniOverrideDelay_Type(Unsigned32):
    """Custom type aRtgPnniOverrideDelay based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ARtgPnniOverrideDelay_Type.__name__ = "Unsigned32"
_ARtgPnniOverrideDelay_Object = MibTableColumn
aRtgPnniOverrideDelay = _ARtgPnniOverrideDelay_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 11, 1, 2),
    _ARtgPnniOverrideDelay_Type()
)
aRtgPnniOverrideDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aRtgPnniOverrideDelay.setStatus("mandatory")


class _ARtgPnniReElectionInterval_Type(Unsigned32):
    """Custom type aRtgPnniReElectionInterval based on Unsigned32"""
    defaultValue = 15

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ARtgPnniReElectionInterval_Type.__name__ = "Unsigned32"
_ARtgPnniReElectionInterval_Object = MibTableColumn
aRtgPnniReElectionInterval = _ARtgPnniReElectionInterval_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 11, 1, 3),
    _ARtgPnniReElectionInterval_Type()
)
aRtgPnniReElectionInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aRtgPnniReElectionInterval.setStatus("mandatory")
_ARtgPnniHlParmsTable_Object = MibTable
aRtgPnniHlParmsTable = _ARtgPnniHlParmsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 12)
)
if mibBuilder.loadTexts:
    aRtgPnniHlParmsTable.setStatus("mandatory")
_ARtgPnniHlParmsEntry_Object = MibTableRow
aRtgPnniHlParmsEntry = _ARtgPnniHlParmsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 12, 1)
)
aRtgPnniHlParmsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "aRtgIndex"),
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "aRtgPnniIndex"),
)
if mibBuilder.loadTexts:
    aRtgPnniHlParmsEntry.setStatus("mandatory")


class _ARtgPnniHelloHoldDown_Type(FixedPoint1):
    """Custom type aRtgPnniHelloHoldDown based on FixedPoint1"""
    defaultValue = 10

    subtypeSpec = FixedPoint1.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 655350),
    )


_ARtgPnniHelloHoldDown_Type.__name__ = "FixedPoint1"
_ARtgPnniHelloHoldDown_Object = MibTableColumn
aRtgPnniHelloHoldDown = _ARtgPnniHelloHoldDown_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 12, 1, 1),
    _ARtgPnniHelloHoldDown_Type()
)
aRtgPnniHelloHoldDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aRtgPnniHelloHoldDown.setStatus("mandatory")


class _ARtgPnniHelloInterval_Type(Unsigned32):
    """Custom type aRtgPnniHelloInterval based on Unsigned32"""
    defaultValue = 15

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ARtgPnniHelloInterval_Type.__name__ = "Unsigned32"
_ARtgPnniHelloInterval_Object = MibTableColumn
aRtgPnniHelloInterval = _ARtgPnniHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 12, 1, 2),
    _ARtgPnniHelloInterval_Type()
)
aRtgPnniHelloInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aRtgPnniHelloInterval.setStatus("mandatory")


class _ARtgPnniHelloInactivityFactor_Type(Unsigned32):
    """Custom type aRtgPnniHelloInactivityFactor based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ARtgPnniHelloInactivityFactor_Type.__name__ = "Unsigned32"
_ARtgPnniHelloInactivityFactor_Object = MibTableColumn
aRtgPnniHelloInactivityFactor = _ARtgPnniHelloInactivityFactor_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 12, 1, 3),
    _ARtgPnniHelloInactivityFactor_Type()
)
aRtgPnniHelloInactivityFactor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aRtgPnniHelloInactivityFactor.setStatus("mandatory")
_ARtgPnniPtseParmsTable_Object = MibTable
aRtgPnniPtseParmsTable = _ARtgPnniPtseParmsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 13)
)
if mibBuilder.loadTexts:
    aRtgPnniPtseParmsTable.setStatus("mandatory")
_ARtgPnniPtseParmsEntry_Object = MibTableRow
aRtgPnniPtseParmsEntry = _ARtgPnniPtseParmsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 13, 1)
)
aRtgPnniPtseParmsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "aRtgIndex"),
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "aRtgPnniIndex"),
)
if mibBuilder.loadTexts:
    aRtgPnniPtseParmsEntry.setStatus("mandatory")


class _ARtgPnniPtseHoldDown_Type(FixedPoint1):
    """Custom type aRtgPnniPtseHoldDown based on FixedPoint1"""
    defaultValue = 10

    subtypeSpec = FixedPoint1.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 655350),
    )


_ARtgPnniPtseHoldDown_Type.__name__ = "FixedPoint1"
_ARtgPnniPtseHoldDown_Object = MibTableColumn
aRtgPnniPtseHoldDown = _ARtgPnniPtseHoldDown_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 13, 1, 1),
    _ARtgPnniPtseHoldDown_Type()
)
aRtgPnniPtseHoldDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aRtgPnniPtseHoldDown.setStatus("mandatory")


class _ARtgPnniPtseRefreshInterval_Type(Unsigned32):
    """Custom type aRtgPnniPtseRefreshInterval based on Unsigned32"""
    defaultValue = 1800

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 65535),
    )


_ARtgPnniPtseRefreshInterval_Type.__name__ = "Unsigned32"
_ARtgPnniPtseRefreshInterval_Object = MibTableColumn
aRtgPnniPtseRefreshInterval = _ARtgPnniPtseRefreshInterval_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 13, 1, 2),
    _ARtgPnniPtseRefreshInterval_Type()
)
aRtgPnniPtseRefreshInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aRtgPnniPtseRefreshInterval.setStatus("mandatory")


class _ARtgPnniPtseLifetimeFactor_Type(Unsigned32):
    """Custom type aRtgPnniPtseLifetimeFactor based on Unsigned32"""
    defaultValue = 200

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(101, 1000),
    )


_ARtgPnniPtseLifetimeFactor_Type.__name__ = "Unsigned32"
_ARtgPnniPtseLifetimeFactor_Object = MibTableColumn
aRtgPnniPtseLifetimeFactor = _ARtgPnniPtseLifetimeFactor_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 13, 1, 3),
    _ARtgPnniPtseLifetimeFactor_Type()
)
aRtgPnniPtseLifetimeFactor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aRtgPnniPtseLifetimeFactor.setStatus("mandatory")


class _ARtgPnniRequestRxmtInterval_Type(Unsigned32):
    """Custom type aRtgPnniRequestRxmtInterval based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ARtgPnniRequestRxmtInterval_Type.__name__ = "Unsigned32"
_ARtgPnniRequestRxmtInterval_Object = MibTableColumn
aRtgPnniRequestRxmtInterval = _ARtgPnniRequestRxmtInterval_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 13, 1, 4),
    _ARtgPnniRequestRxmtInterval_Type()
)
aRtgPnniRequestRxmtInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aRtgPnniRequestRxmtInterval.setStatus("mandatory")


class _ARtgPnniPeerDelayedAckInterval_Type(FixedPoint1):
    """Custom type aRtgPnniPeerDelayedAckInterval based on FixedPoint1"""
    defaultValue = 1

    subtypeSpec = FixedPoint1.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 655350),
    )


_ARtgPnniPeerDelayedAckInterval_Type.__name__ = "FixedPoint1"
_ARtgPnniPeerDelayedAckInterval_Object = MibTableColumn
aRtgPnniPeerDelayedAckInterval = _ARtgPnniPeerDelayedAckInterval_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 13, 1, 5),
    _ARtgPnniPeerDelayedAckInterval_Type()
)
aRtgPnniPeerDelayedAckInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aRtgPnniPeerDelayedAckInterval.setStatus("mandatory")
_ARtgPnniThreshParmsTable_Object = MibTable
aRtgPnniThreshParmsTable = _ARtgPnniThreshParmsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 14)
)
if mibBuilder.loadTexts:
    aRtgPnniThreshParmsTable.setStatus("mandatory")
_ARtgPnniThreshParmsEntry_Object = MibTableRow
aRtgPnniThreshParmsEntry = _ARtgPnniThreshParmsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 14, 1)
)
aRtgPnniThreshParmsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "aRtgIndex"),
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "aRtgPnniIndex"),
)
if mibBuilder.loadTexts:
    aRtgPnniThreshParmsEntry.setStatus("mandatory")


class _ARtgPnniAvcrMt_Type(Unsigned32):
    """Custom type aRtgPnniAvcrMt based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_ARtgPnniAvcrMt_Type.__name__ = "Unsigned32"
_ARtgPnniAvcrMt_Object = MibTableColumn
aRtgPnniAvcrMt = _ARtgPnniAvcrMt_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 14, 1, 1),
    _ARtgPnniAvcrMt_Type()
)
aRtgPnniAvcrMt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aRtgPnniAvcrMt.setStatus("mandatory")


class _ARtgPnniAvcrPm_Type(Unsigned32):
    """Custom type aRtgPnniAvcrPm based on Unsigned32"""
    defaultValue = 50

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_ARtgPnniAvcrPm_Type.__name__ = "Unsigned32"
_ARtgPnniAvcrPm_Object = MibTableColumn
aRtgPnniAvcrPm = _ARtgPnniAvcrPm_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 14, 1, 2),
    _ARtgPnniAvcrPm_Type()
)
aRtgPnniAvcrPm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aRtgPnniAvcrPm.setStatus("mandatory")
_ARtgPnniOperTable_Object = MibTable
aRtgPnniOperTable = _ARtgPnniOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 15)
)
if mibBuilder.loadTexts:
    aRtgPnniOperTable.setStatus("mandatory")
_ARtgPnniOperEntry_Object = MibTableRow
aRtgPnniOperEntry = _ARtgPnniOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 15, 1)
)
aRtgPnniOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "aRtgIndex"),
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "aRtgPnniIndex"),
)
if mibBuilder.loadTexts:
    aRtgPnniOperEntry.setStatus("mandatory")


class _ARtgPnniTopologyMemoryExhaustion_Type(Integer32):
    """Custom type aRtgPnniTopologyMemoryExhaustion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_ARtgPnniTopologyMemoryExhaustion_Type.__name__ = "Integer32"
_ARtgPnniTopologyMemoryExhaustion_Object = MibTableColumn
aRtgPnniTopologyMemoryExhaustion = _ARtgPnniTopologyMemoryExhaustion_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 15, 1, 2),
    _ARtgPnniTopologyMemoryExhaustion_Type()
)
aRtgPnniTopologyMemoryExhaustion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aRtgPnniTopologyMemoryExhaustion.setStatus("mandatory")
_ARtgPnniStatsTable_Object = MibTable
aRtgPnniStatsTable = _ARtgPnniStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 16)
)
if mibBuilder.loadTexts:
    aRtgPnniStatsTable.setStatus("mandatory")
_ARtgPnniStatsEntry_Object = MibTableRow
aRtgPnniStatsEntry = _ARtgPnniStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 16, 1)
)
aRtgPnniStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "aRtgIndex"),
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "aRtgPnniIndex"),
)
if mibBuilder.loadTexts:
    aRtgPnniStatsEntry.setStatus("mandatory")
_ARtgPnniRoutingAttempts_Type = Counter32
_ARtgPnniRoutingAttempts_Object = MibTableColumn
aRtgPnniRoutingAttempts = _ARtgPnniRoutingAttempts_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 16, 1, 1),
    _ARtgPnniRoutingAttempts_Type()
)
aRtgPnniRoutingAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aRtgPnniRoutingAttempts.setStatus("mandatory")
_ARtgPnniFailedRoutingAttempts_Type = Counter32
_ARtgPnniFailedRoutingAttempts_Object = MibTableColumn
aRtgPnniFailedRoutingAttempts = _ARtgPnniFailedRoutingAttempts_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 16, 1, 2),
    _ARtgPnniFailedRoutingAttempts_Type()
)
aRtgPnniFailedRoutingAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aRtgPnniFailedRoutingAttempts.setStatus("mandatory")
_ARtgPnniCallsRerouted_Type = Counter32
_ARtgPnniCallsRerouted_Object = MibTableColumn
aRtgPnniCallsRerouted = _ARtgPnniCallsRerouted_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 16, 1, 3),
    _ARtgPnniCallsRerouted_Type()
)
aRtgPnniCallsRerouted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aRtgPnniCallsRerouted.setStatus("mandatory")
_ARtgPnniOptMetricTable_Object = MibTable
aRtgPnniOptMetricTable = _ARtgPnniOptMetricTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 386)
)
if mibBuilder.loadTexts:
    aRtgPnniOptMetricTable.setStatus("mandatory")
_ARtgPnniOptMetricEntry_Object = MibTableRow
aRtgPnniOptMetricEntry = _ARtgPnniOptMetricEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 386, 1)
)
aRtgPnniOptMetricEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "aRtgIndex"),
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "aRtgPnniIndex"),
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "aRtgPnniOptMetricIndex"),
)
if mibBuilder.loadTexts:
    aRtgPnniOptMetricEntry.setStatus("mandatory")


class _ARtgPnniOptMetricIndex_Type(Integer32):
    """Custom type aRtgPnniOptMetricIndex based on Integer32"""
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
        *(("cbr", 1),
          ("nrtVbr", 3),
          ("rtVbr", 2),
          ("ubr", 4))
    )


_ARtgPnniOptMetricIndex_Type.__name__ = "Integer32"
_ARtgPnniOptMetricIndex_Object = MibTableColumn
aRtgPnniOptMetricIndex = _ARtgPnniOptMetricIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 386, 1, 1),
    _ARtgPnniOptMetricIndex_Type()
)
aRtgPnniOptMetricIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aRtgPnniOptMetricIndex.setStatus("mandatory")


class _ARtgPnniOptMetricValue_Type(Integer32):
    """Custom type aRtgPnniOptMetricValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("aw", 2),
          ("cdv", 0),
          ("maxCtd", 1))
    )


_ARtgPnniOptMetricValue_Type.__name__ = "Integer32"
_ARtgPnniOptMetricValue_Object = MibTableColumn
aRtgPnniOptMetricValue = _ARtgPnniOptMetricValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 3, 386, 1, 2),
    _ARtgPnniOptMetricValue_Type()
)
aRtgPnniOptMetricValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aRtgPnniOptMetricValue.setStatus("mandatory")
_ARtgStatsTable_Object = MibTable
aRtgStatsTable = _ARtgStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 10)
)
if mibBuilder.loadTexts:
    aRtgStatsTable.setStatus("mandatory")
_ARtgStatsEntry_Object = MibTableRow
aRtgStatsEntry = _ARtgStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 10, 1)
)
aRtgStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "aRtgIndex"),
)
if mibBuilder.loadTexts:
    aRtgStatsEntry.setStatus("mandatory")
_ARtgRoutingAttempts_Type = Counter32
_ARtgRoutingAttempts_Object = MibTableColumn
aRtgRoutingAttempts = _ARtgRoutingAttempts_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 10, 1, 1),
    _ARtgRoutingAttempts_Type()
)
aRtgRoutingAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aRtgRoutingAttempts.setStatus("mandatory")
_ARtgFailedRoutingAttempts_Type = Counter32
_ARtgFailedRoutingAttempts_Object = MibTableColumn
aRtgFailedRoutingAttempts = _ARtgFailedRoutingAttempts_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 95, 10, 1, 2),
    _ARtgFailedRoutingAttempts_Type()
)
aRtgFailedRoutingAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aRtgFailedRoutingAttempts.setStatus("mandatory")
_AtmCR_ObjectIdentity = ObjectIdentity
atmCR = _AtmCR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 113)
)
_AtmCRRowStatusTable_Object = MibTable
atmCRRowStatusTable = _AtmCRRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 113, 1)
)
if mibBuilder.loadTexts:
    atmCRRowStatusTable.setStatus("mandatory")
_AtmCRRowStatusEntry_Object = MibTableRow
atmCRRowStatusEntry = _AtmCRRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 113, 1, 1)
)
atmCRRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "atmCRIndex"),
)
if mibBuilder.loadTexts:
    atmCRRowStatusEntry.setStatus("mandatory")
_AtmCRRowStatus_Type = RowStatus
_AtmCRRowStatus_Object = MibTableColumn
atmCRRowStatus = _AtmCRRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 113, 1, 1, 1),
    _AtmCRRowStatus_Type()
)
atmCRRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmCRRowStatus.setStatus("mandatory")
_AtmCRComponentName_Type = DisplayString
_AtmCRComponentName_Object = MibTableColumn
atmCRComponentName = _AtmCRComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 113, 1, 1, 2),
    _AtmCRComponentName_Type()
)
atmCRComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmCRComponentName.setStatus("mandatory")
_AtmCRStorageType_Type = StorageType
_AtmCRStorageType_Object = MibTableColumn
atmCRStorageType = _AtmCRStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 113, 1, 1, 4),
    _AtmCRStorageType_Type()
)
atmCRStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmCRStorageType.setStatus("mandatory")
_AtmCRIndex_Type = NonReplicated
_AtmCRIndex_Object = MibTableColumn
atmCRIndex = _AtmCRIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 113, 1, 1, 10),
    _AtmCRIndex_Type()
)
atmCRIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmCRIndex.setStatus("mandatory")
_AtmCRDna_ObjectIdentity = ObjectIdentity
atmCRDna = _AtmCRDna_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 113, 2)
)
_AtmCRDnaRowStatusTable_Object = MibTable
atmCRDnaRowStatusTable = _AtmCRDnaRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 113, 2, 1)
)
if mibBuilder.loadTexts:
    atmCRDnaRowStatusTable.setStatus("mandatory")
_AtmCRDnaRowStatusEntry_Object = MibTableRow
atmCRDnaRowStatusEntry = _AtmCRDnaRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 113, 2, 1, 1)
)
atmCRDnaRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "atmCRIndex"),
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "atmCRDnaIndex"),
)
if mibBuilder.loadTexts:
    atmCRDnaRowStatusEntry.setStatus("mandatory")
_AtmCRDnaRowStatus_Type = RowStatus
_AtmCRDnaRowStatus_Object = MibTableColumn
atmCRDnaRowStatus = _AtmCRDnaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 113, 2, 1, 1, 1),
    _AtmCRDnaRowStatus_Type()
)
atmCRDnaRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmCRDnaRowStatus.setStatus("mandatory")
_AtmCRDnaComponentName_Type = DisplayString
_AtmCRDnaComponentName_Object = MibTableColumn
atmCRDnaComponentName = _AtmCRDnaComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 113, 2, 1, 1, 2),
    _AtmCRDnaComponentName_Type()
)
atmCRDnaComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmCRDnaComponentName.setStatus("mandatory")
_AtmCRDnaStorageType_Type = StorageType
_AtmCRDnaStorageType_Object = MibTableColumn
atmCRDnaStorageType = _AtmCRDnaStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 113, 2, 1, 1, 4),
    _AtmCRDnaStorageType_Type()
)
atmCRDnaStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmCRDnaStorageType.setStatus("mandatory")


class _AtmCRDnaIndex_Type(AsciiStringIndex):
    """Custom type atmCRDnaIndex based on AsciiStringIndex"""
    subtypeSpec = AsciiStringIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_AtmCRDnaIndex_Type.__name__ = "AsciiStringIndex"
_AtmCRDnaIndex_Object = MibTableColumn
atmCRDnaIndex = _AtmCRDnaIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 113, 2, 1, 1, 10),
    _AtmCRDnaIndex_Type()
)
atmCRDnaIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmCRDnaIndex.setStatus("mandatory")
_AtmCRDnaDestinationNameTable_Object = MibTable
atmCRDnaDestinationNameTable = _AtmCRDnaDestinationNameTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 113, 2, 289)
)
if mibBuilder.loadTexts:
    atmCRDnaDestinationNameTable.setStatus("obsolete")
_AtmCRDnaDestinationNameEntry_Object = MibTableRow
atmCRDnaDestinationNameEntry = _AtmCRDnaDestinationNameEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 113, 2, 289, 1)
)
atmCRDnaDestinationNameEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "atmCRIndex"),
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "atmCRDnaIndex"),
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "atmCRDnaDestinationNameValue"),
)
if mibBuilder.loadTexts:
    atmCRDnaDestinationNameEntry.setStatus("obsolete")
_AtmCRDnaDestinationNameValue_Type = RowPointer
_AtmCRDnaDestinationNameValue_Object = MibTableColumn
atmCRDnaDestinationNameValue = _AtmCRDnaDestinationNameValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 113, 2, 289, 1, 1),
    _AtmCRDnaDestinationNameValue_Type()
)
atmCRDnaDestinationNameValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmCRDnaDestinationNameValue.setStatus("obsolete")
_AtmCRProvTable_Object = MibTable
atmCRProvTable = _AtmCRProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 113, 10)
)
if mibBuilder.loadTexts:
    atmCRProvTable.setStatus("mandatory")
_AtmCRProvEntry_Object = MibTableRow
atmCRProvEntry = _AtmCRProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 113, 10, 1)
)
atmCRProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "atmCRIndex"),
)
if mibBuilder.loadTexts:
    atmCRProvEntry.setStatus("mandatory")


class _AtmCRNodeAddress_Type(AsciiString):
    """Custom type atmCRNodeAddress based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(26, 26),
    )


_AtmCRNodeAddress_Type.__name__ = "AsciiString"
_AtmCRNodeAddress_Object = MibTableColumn
atmCRNodeAddress = _AtmCRNodeAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 113, 10, 1, 1),
    _AtmCRNodeAddress_Type()
)
atmCRNodeAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmCRNodeAddress.setStatus("obsolete")
_AtmCRStatsTable_Object = MibTable
atmCRStatsTable = _AtmCRStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 113, 11)
)
if mibBuilder.loadTexts:
    atmCRStatsTable.setStatus("obsolete")
_AtmCRStatsEntry_Object = MibTableRow
atmCRStatsEntry = _AtmCRStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 113, 11, 1)
)
atmCRStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "atmCRIndex"),
)
if mibBuilder.loadTexts:
    atmCRStatsEntry.setStatus("obsolete")
_AtmCRCallsRouted_Type = Counter32
_AtmCRCallsRouted_Object = MibTableColumn
atmCRCallsRouted = _AtmCRCallsRouted_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 113, 11, 1, 1),
    _AtmCRCallsRouted_Type()
)
atmCRCallsRouted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmCRCallsRouted.setStatus("obsolete")
_AtmCRCallsFailed_Type = Counter32
_AtmCRCallsFailed_Object = MibTableColumn
atmCRCallsFailed = _AtmCRCallsFailed_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 113, 11, 1, 2),
    _AtmCRCallsFailed_Type()
)
atmCRCallsFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmCRCallsFailed.setStatus("obsolete")
_AtmIfVpcSrc_ObjectIdentity = ObjectIdentity
atmIfVpcSrc = _AtmIfVpcSrc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 4, 6)
)
_AtmIfVpcSrcRowStatusTable_Object = MibTable
atmIfVpcSrcRowStatusTable = _AtmIfVpcSrcRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 4, 6, 1)
)
if mibBuilder.loadTexts:
    atmIfVpcSrcRowStatusTable.setStatus("mandatory")
_AtmIfVpcSrcRowStatusEntry_Object = MibTableRow
atmIfVpcSrcRowStatusEntry = _AtmIfVpcSrcRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 4, 6, 1, 1)
)
atmIfVpcSrcRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfVpcIndex"),
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "atmIfVpcSrcIndex"),
)
if mibBuilder.loadTexts:
    atmIfVpcSrcRowStatusEntry.setStatus("mandatory")
_AtmIfVpcSrcRowStatus_Type = RowStatus
_AtmIfVpcSrcRowStatus_Object = MibTableColumn
atmIfVpcSrcRowStatus = _AtmIfVpcSrcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 4, 6, 1, 1, 1),
    _AtmIfVpcSrcRowStatus_Type()
)
atmIfVpcSrcRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfVpcSrcRowStatus.setStatus("mandatory")
_AtmIfVpcSrcComponentName_Type = DisplayString
_AtmIfVpcSrcComponentName_Object = MibTableColumn
atmIfVpcSrcComponentName = _AtmIfVpcSrcComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 4, 6, 1, 1, 2),
    _AtmIfVpcSrcComponentName_Type()
)
atmIfVpcSrcComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVpcSrcComponentName.setStatus("mandatory")
_AtmIfVpcSrcStorageType_Type = StorageType
_AtmIfVpcSrcStorageType_Object = MibTableColumn
atmIfVpcSrcStorageType = _AtmIfVpcSrcStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 4, 6, 1, 1, 4),
    _AtmIfVpcSrcStorageType_Type()
)
atmIfVpcSrcStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVpcSrcStorageType.setStatus("mandatory")
_AtmIfVpcSrcIndex_Type = NonReplicated
_AtmIfVpcSrcIndex_Object = MibTableColumn
atmIfVpcSrcIndex = _AtmIfVpcSrcIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 4, 6, 1, 1, 10),
    _AtmIfVpcSrcIndex_Type()
)
atmIfVpcSrcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmIfVpcSrcIndex.setStatus("mandatory")
_AtmIfVpcSrcProvTable_Object = MibTable
atmIfVpcSrcProvTable = _AtmIfVpcSrcProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 4, 6, 10)
)
if mibBuilder.loadTexts:
    atmIfVpcSrcProvTable.setStatus("mandatory")
_AtmIfVpcSrcProvEntry_Object = MibTableRow
atmIfVpcSrcProvEntry = _AtmIfVpcSrcProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 4, 6, 10, 1)
)
atmIfVpcSrcProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfVpcIndex"),
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "atmIfVpcSrcIndex"),
)
if mibBuilder.loadTexts:
    atmIfVpcSrcProvEntry.setStatus("mandatory")


class _AtmIfVpcSrcCallingAddress_Type(HexString):
    """Custom type atmIfVpcSrcCallingAddress based on HexString"""
    defaultHexValue = ""

    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_AtmIfVpcSrcCallingAddress_Type.__name__ = "HexString"
_AtmIfVpcSrcCallingAddress_Object = MibTableColumn
atmIfVpcSrcCallingAddress = _AtmIfVpcSrcCallingAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 4, 6, 10, 1, 1),
    _AtmIfVpcSrcCallingAddress_Type()
)
atmIfVpcSrcCallingAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfVpcSrcCallingAddress.setStatus("mandatory")


class _AtmIfVpcSrcCalledAddress_Type(HexString):
    """Custom type atmIfVpcSrcCalledAddress based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_AtmIfVpcSrcCalledAddress_Type.__name__ = "HexString"
_AtmIfVpcSrcCalledAddress_Object = MibTableColumn
atmIfVpcSrcCalledAddress = _AtmIfVpcSrcCalledAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 4, 6, 10, 1, 2),
    _AtmIfVpcSrcCalledAddress_Type()
)
atmIfVpcSrcCalledAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfVpcSrcCalledAddress.setStatus("mandatory")


class _AtmIfVpcSrcCalledVpi_Type(Unsigned32):
    """Custom type atmIfVpcSrcCalledVpi based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_AtmIfVpcSrcCalledVpi_Type.__name__ = "Unsigned32"
_AtmIfVpcSrcCalledVpi_Object = MibTableColumn
atmIfVpcSrcCalledVpi = _AtmIfVpcSrcCalledVpi_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 4, 6, 10, 1, 3),
    _AtmIfVpcSrcCalledVpi_Type()
)
atmIfVpcSrcCalledVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfVpcSrcCalledVpi.setStatus("mandatory")
_AtmIfVpcSrcOperTable_Object = MibTable
atmIfVpcSrcOperTable = _AtmIfVpcSrcOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 4, 6, 11)
)
if mibBuilder.loadTexts:
    atmIfVpcSrcOperTable.setStatus("mandatory")
_AtmIfVpcSrcOperEntry_Object = MibTableRow
atmIfVpcSrcOperEntry = _AtmIfVpcSrcOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 4, 6, 11, 1)
)
atmIfVpcSrcOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfVpcIndex"),
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "atmIfVpcSrcIndex"),
)
if mibBuilder.loadTexts:
    atmIfVpcSrcOperEntry.setStatus("mandatory")


class _AtmIfVpcSrcState_Type(Integer32):
    """Custom type atmIfVpcSrcState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("active", 0),
          ("inactive", 1))
    )


_AtmIfVpcSrcState_Type.__name__ = "Integer32"
_AtmIfVpcSrcState_Object = MibTableColumn
atmIfVpcSrcState = _AtmIfVpcSrcState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 4, 6, 11, 1, 1),
    _AtmIfVpcSrcState_Type()
)
atmIfVpcSrcState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVpcSrcState.setStatus("mandatory")
_AtmIfVpcSrcRetryCount_Type = Counter32
_AtmIfVpcSrcRetryCount_Object = MibTableColumn
atmIfVpcSrcRetryCount = _AtmIfVpcSrcRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 4, 6, 11, 1, 2),
    _AtmIfVpcSrcRetryCount_Type()
)
atmIfVpcSrcRetryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVpcSrcRetryCount.setStatus("mandatory")


class _AtmIfVpcSrcLastFailureCauseCode_Type(Unsigned32):
    """Custom type atmIfVpcSrcLastFailureCauseCode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AtmIfVpcSrcLastFailureCauseCode_Type.__name__ = "Unsigned32"
_AtmIfVpcSrcLastFailureCauseCode_Object = MibTableColumn
atmIfVpcSrcLastFailureCauseCode = _AtmIfVpcSrcLastFailureCauseCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 4, 6, 11, 1, 3),
    _AtmIfVpcSrcLastFailureCauseCode_Type()
)
atmIfVpcSrcLastFailureCauseCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVpcSrcLastFailureCauseCode.setStatus("mandatory")


class _AtmIfVpcSrcLastFailureDiagCode_Type(AsciiString):
    """Custom type atmIfVpcSrcLastFailureDiagCode based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_AtmIfVpcSrcLastFailureDiagCode_Type.__name__ = "AsciiString"
_AtmIfVpcSrcLastFailureDiagCode_Object = MibTableColumn
atmIfVpcSrcLastFailureDiagCode = _AtmIfVpcSrcLastFailureDiagCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 4, 6, 11, 1, 4),
    _AtmIfVpcSrcLastFailureDiagCode_Type()
)
atmIfVpcSrcLastFailureDiagCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVpcSrcLastFailureDiagCode.setStatus("mandatory")
_AtmIfVpcRp_ObjectIdentity = ObjectIdentity
atmIfVpcRp = _AtmIfVpcRp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 4, 7)
)
_AtmIfVpcRpRowStatusTable_Object = MibTable
atmIfVpcRpRowStatusTable = _AtmIfVpcRpRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 4, 7, 1)
)
if mibBuilder.loadTexts:
    atmIfVpcRpRowStatusTable.setStatus("mandatory")
_AtmIfVpcRpRowStatusEntry_Object = MibTableRow
atmIfVpcRpRowStatusEntry = _AtmIfVpcRpRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 4, 7, 1, 1)
)
atmIfVpcRpRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfVpcIndex"),
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "atmIfVpcRpIndex"),
)
if mibBuilder.loadTexts:
    atmIfVpcRpRowStatusEntry.setStatus("mandatory")
_AtmIfVpcRpRowStatus_Type = RowStatus
_AtmIfVpcRpRowStatus_Object = MibTableColumn
atmIfVpcRpRowStatus = _AtmIfVpcRpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 4, 7, 1, 1, 1),
    _AtmIfVpcRpRowStatus_Type()
)
atmIfVpcRpRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVpcRpRowStatus.setStatus("mandatory")
_AtmIfVpcRpComponentName_Type = DisplayString
_AtmIfVpcRpComponentName_Object = MibTableColumn
atmIfVpcRpComponentName = _AtmIfVpcRpComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 4, 7, 1, 1, 2),
    _AtmIfVpcRpComponentName_Type()
)
atmIfVpcRpComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVpcRpComponentName.setStatus("mandatory")
_AtmIfVpcRpStorageType_Type = StorageType
_AtmIfVpcRpStorageType_Object = MibTableColumn
atmIfVpcRpStorageType = _AtmIfVpcRpStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 4, 7, 1, 1, 4),
    _AtmIfVpcRpStorageType_Type()
)
atmIfVpcRpStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVpcRpStorageType.setStatus("mandatory")
_AtmIfVpcRpIndex_Type = NonReplicated
_AtmIfVpcRpIndex_Object = MibTableColumn
atmIfVpcRpIndex = _AtmIfVpcRpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 4, 7, 1, 1, 10),
    _AtmIfVpcRpIndex_Type()
)
atmIfVpcRpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmIfVpcRpIndex.setStatus("mandatory")
_AtmIfVpcRpOperTable_Object = MibTable
atmIfVpcRpOperTable = _AtmIfVpcRpOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 4, 7, 10)
)
if mibBuilder.loadTexts:
    atmIfVpcRpOperTable.setStatus("mandatory")
_AtmIfVpcRpOperEntry_Object = MibTableRow
atmIfVpcRpOperEntry = _AtmIfVpcRpOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 4, 7, 10, 1)
)
atmIfVpcRpOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfVpcIndex"),
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "atmIfVpcRpIndex"),
)
if mibBuilder.loadTexts:
    atmIfVpcRpOperEntry.setStatus("mandatory")
_AtmIfVpcRpNextHop_Type = RowPointer
_AtmIfVpcRpNextHop_Object = MibTableColumn
atmIfVpcRpNextHop = _AtmIfVpcRpNextHop_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 4, 7, 10, 1, 1),
    _AtmIfVpcRpNextHop_Type()
)
atmIfVpcRpNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVpcRpNextHop.setStatus("obsolete")
_AtmIfVpcRpNextHopsTable_Object = MibTable
atmIfVpcRpNextHopsTable = _AtmIfVpcRpNextHopsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 4, 7, 430)
)
if mibBuilder.loadTexts:
    atmIfVpcRpNextHopsTable.setStatus("mandatory")
_AtmIfVpcRpNextHopsEntry_Object = MibTableRow
atmIfVpcRpNextHopsEntry = _AtmIfVpcRpNextHopsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 4, 7, 430, 1)
)
atmIfVpcRpNextHopsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfVpcIndex"),
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "atmIfVpcRpIndex"),
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "atmIfVpcRpNextHopsValue"),
)
if mibBuilder.loadTexts:
    atmIfVpcRpNextHopsEntry.setStatus("mandatory")
_AtmIfVpcRpNextHopsValue_Type = RowPointer
_AtmIfVpcRpNextHopsValue_Object = MibTableColumn
atmIfVpcRpNextHopsValue = _AtmIfVpcRpNextHopsValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 4, 7, 430, 1, 1),
    _AtmIfVpcRpNextHopsValue_Type()
)
atmIfVpcRpNextHopsValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVpcRpNextHopsValue.setStatus("mandatory")
_AtmIfVpcDst_ObjectIdentity = ObjectIdentity
atmIfVpcDst = _AtmIfVpcDst_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 4, 8)
)
_AtmIfVpcDstRowStatusTable_Object = MibTable
atmIfVpcDstRowStatusTable = _AtmIfVpcDstRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 4, 8, 1)
)
if mibBuilder.loadTexts:
    atmIfVpcDstRowStatusTable.setStatus("mandatory")
_AtmIfVpcDstRowStatusEntry_Object = MibTableRow
atmIfVpcDstRowStatusEntry = _AtmIfVpcDstRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 4, 8, 1, 1)
)
atmIfVpcDstRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfVpcIndex"),
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "atmIfVpcDstIndex"),
)
if mibBuilder.loadTexts:
    atmIfVpcDstRowStatusEntry.setStatus("mandatory")
_AtmIfVpcDstRowStatus_Type = RowStatus
_AtmIfVpcDstRowStatus_Object = MibTableColumn
atmIfVpcDstRowStatus = _AtmIfVpcDstRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 4, 8, 1, 1, 1),
    _AtmIfVpcDstRowStatus_Type()
)
atmIfVpcDstRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVpcDstRowStatus.setStatus("mandatory")
_AtmIfVpcDstComponentName_Type = DisplayString
_AtmIfVpcDstComponentName_Object = MibTableColumn
atmIfVpcDstComponentName = _AtmIfVpcDstComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 4, 8, 1, 1, 2),
    _AtmIfVpcDstComponentName_Type()
)
atmIfVpcDstComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVpcDstComponentName.setStatus("mandatory")
_AtmIfVpcDstStorageType_Type = StorageType
_AtmIfVpcDstStorageType_Object = MibTableColumn
atmIfVpcDstStorageType = _AtmIfVpcDstStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 4, 8, 1, 1, 4),
    _AtmIfVpcDstStorageType_Type()
)
atmIfVpcDstStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVpcDstStorageType.setStatus("mandatory")
_AtmIfVpcDstIndex_Type = NonReplicated
_AtmIfVpcDstIndex_Object = MibTableColumn
atmIfVpcDstIndex = _AtmIfVpcDstIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 4, 8, 1, 1, 10),
    _AtmIfVpcDstIndex_Type()
)
atmIfVpcDstIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmIfVpcDstIndex.setStatus("mandatory")
_AtmIfVpcDstOperTable_Object = MibTable
atmIfVpcDstOperTable = _AtmIfVpcDstOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 4, 8, 10)
)
if mibBuilder.loadTexts:
    atmIfVpcDstOperTable.setStatus("mandatory")
_AtmIfVpcDstOperEntry_Object = MibTableRow
atmIfVpcDstOperEntry = _AtmIfVpcDstOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 4, 8, 10, 1)
)
atmIfVpcDstOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfVpcIndex"),
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "atmIfVpcDstIndex"),
)
if mibBuilder.loadTexts:
    atmIfVpcDstOperEntry.setStatus("mandatory")


class _AtmIfVpcDstCalledAddress_Type(HexString):
    """Custom type atmIfVpcDstCalledAddress based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_AtmIfVpcDstCalledAddress_Type.__name__ = "HexString"
_AtmIfVpcDstCalledAddress_Object = MibTableColumn
atmIfVpcDstCalledAddress = _AtmIfVpcDstCalledAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 4, 8, 10, 1, 1),
    _AtmIfVpcDstCalledAddress_Type()
)
atmIfVpcDstCalledAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVpcDstCalledAddress.setStatus("mandatory")


class _AtmIfVpcDstCallingAddress_Type(AsciiString):
    """Custom type atmIfVpcDstCallingAddress based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 40),
    )


_AtmIfVpcDstCallingAddress_Type.__name__ = "AsciiString"
_AtmIfVpcDstCallingAddress_Object = MibTableColumn
atmIfVpcDstCallingAddress = _AtmIfVpcDstCallingAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 4, 8, 10, 1, 2),
    _AtmIfVpcDstCallingAddress_Type()
)
atmIfVpcDstCallingAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVpcDstCallingAddress.setStatus("mandatory")


class _AtmIfVpcDstCallingVpi_Type(AsciiString):
    """Custom type atmIfVpcDstCallingVpi based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 7),
    )


_AtmIfVpcDstCallingVpi_Type.__name__ = "AsciiString"
_AtmIfVpcDstCallingVpi_Object = MibTableColumn
atmIfVpcDstCallingVpi = _AtmIfVpcDstCallingVpi_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 4, 8, 10, 1, 3),
    _AtmIfVpcDstCallingVpi_Type()
)
atmIfVpcDstCallingVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVpcDstCallingVpi.setStatus("mandatory")
_AtmIfVccSrc_ObjectIdentity = ObjectIdentity
atmIfVccSrc = _AtmIfVccSrc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 5, 8)
)
_AtmIfVccSrcRowStatusTable_Object = MibTable
atmIfVccSrcRowStatusTable = _AtmIfVccSrcRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 5, 8, 1)
)
if mibBuilder.loadTexts:
    atmIfVccSrcRowStatusTable.setStatus("mandatory")
_AtmIfVccSrcRowStatusEntry_Object = MibTableRow
atmIfVccSrcRowStatusEntry = _AtmIfVccSrcRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 5, 8, 1, 1)
)
atmIfVccSrcRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfVccIndex"),
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "atmIfVccSrcIndex"),
)
if mibBuilder.loadTexts:
    atmIfVccSrcRowStatusEntry.setStatus("mandatory")
_AtmIfVccSrcRowStatus_Type = RowStatus
_AtmIfVccSrcRowStatus_Object = MibTableColumn
atmIfVccSrcRowStatus = _AtmIfVccSrcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 5, 8, 1, 1, 1),
    _AtmIfVccSrcRowStatus_Type()
)
atmIfVccSrcRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfVccSrcRowStatus.setStatus("mandatory")
_AtmIfVccSrcComponentName_Type = DisplayString
_AtmIfVccSrcComponentName_Object = MibTableColumn
atmIfVccSrcComponentName = _AtmIfVccSrcComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 5, 8, 1, 1, 2),
    _AtmIfVccSrcComponentName_Type()
)
atmIfVccSrcComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVccSrcComponentName.setStatus("mandatory")
_AtmIfVccSrcStorageType_Type = StorageType
_AtmIfVccSrcStorageType_Object = MibTableColumn
atmIfVccSrcStorageType = _AtmIfVccSrcStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 5, 8, 1, 1, 4),
    _AtmIfVccSrcStorageType_Type()
)
atmIfVccSrcStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVccSrcStorageType.setStatus("mandatory")
_AtmIfVccSrcIndex_Type = NonReplicated
_AtmIfVccSrcIndex_Object = MibTableColumn
atmIfVccSrcIndex = _AtmIfVccSrcIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 5, 8, 1, 1, 10),
    _AtmIfVccSrcIndex_Type()
)
atmIfVccSrcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmIfVccSrcIndex.setStatus("mandatory")
_AtmIfVccSrcProvTable_Object = MibTable
atmIfVccSrcProvTable = _AtmIfVccSrcProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 5, 8, 10)
)
if mibBuilder.loadTexts:
    atmIfVccSrcProvTable.setStatus("mandatory")
_AtmIfVccSrcProvEntry_Object = MibTableRow
atmIfVccSrcProvEntry = _AtmIfVccSrcProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 5, 8, 10, 1)
)
atmIfVccSrcProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfVccIndex"),
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "atmIfVccSrcIndex"),
)
if mibBuilder.loadTexts:
    atmIfVccSrcProvEntry.setStatus("mandatory")


class _AtmIfVccSrcRemoteAddress_Type(HexString):
    """Custom type atmIfVccSrcRemoteAddress based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_AtmIfVccSrcRemoteAddress_Type.__name__ = "HexString"
_AtmIfVccSrcRemoteAddress_Object = MibTableColumn
atmIfVccSrcRemoteAddress = _AtmIfVccSrcRemoteAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 5, 8, 10, 1, 1),
    _AtmIfVccSrcRemoteAddress_Type()
)
atmIfVccSrcRemoteAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfVccSrcRemoteAddress.setStatus("obsolete")


class _AtmIfVccSrcRemoteVpiVci_Type(IntegerSequence):
    """Custom type atmIfVccSrcRemoteVpiVci based on IntegerSequence"""
    subtypeSpec = IntegerSequence.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 9),
    )


_AtmIfVccSrcRemoteVpiVci_Type.__name__ = "IntegerSequence"
_AtmIfVccSrcRemoteVpiVci_Object = MibTableColumn
atmIfVccSrcRemoteVpiVci = _AtmIfVccSrcRemoteVpiVci_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 5, 8, 10, 1, 2),
    _AtmIfVccSrcRemoteVpiVci_Type()
)
atmIfVccSrcRemoteVpiVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfVccSrcRemoteVpiVci.setStatus("obsolete")


class _AtmIfVccSrcCallingAddress_Type(HexString):
    """Custom type atmIfVccSrcCallingAddress based on HexString"""
    defaultHexValue = ""

    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_AtmIfVccSrcCallingAddress_Type.__name__ = "HexString"
_AtmIfVccSrcCallingAddress_Object = MibTableColumn
atmIfVccSrcCallingAddress = _AtmIfVccSrcCallingAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 5, 8, 10, 1, 3),
    _AtmIfVccSrcCallingAddress_Type()
)
atmIfVccSrcCallingAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfVccSrcCallingAddress.setStatus("mandatory")


class _AtmIfVccSrcCalledAddress_Type(HexString):
    """Custom type atmIfVccSrcCalledAddress based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_AtmIfVccSrcCalledAddress_Type.__name__ = "HexString"
_AtmIfVccSrcCalledAddress_Object = MibTableColumn
atmIfVccSrcCalledAddress = _AtmIfVccSrcCalledAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 5, 8, 10, 1, 4),
    _AtmIfVccSrcCalledAddress_Type()
)
atmIfVccSrcCalledAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfVccSrcCalledAddress.setStatus("mandatory")


class _AtmIfVccSrcCalledVpiVci_Type(IntegerSequence):
    """Custom type atmIfVccSrcCalledVpiVci based on IntegerSequence"""
    subtypeSpec = IntegerSequence.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 10),
    )


_AtmIfVccSrcCalledVpiVci_Type.__name__ = "IntegerSequence"
_AtmIfVccSrcCalledVpiVci_Object = MibTableColumn
atmIfVccSrcCalledVpiVci = _AtmIfVccSrcCalledVpiVci_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 5, 8, 10, 1, 5),
    _AtmIfVccSrcCalledVpiVci_Type()
)
atmIfVccSrcCalledVpiVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfVccSrcCalledVpiVci.setStatus("mandatory")
_AtmIfVccSrcOperTable_Object = MibTable
atmIfVccSrcOperTable = _AtmIfVccSrcOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 5, 8, 11)
)
if mibBuilder.loadTexts:
    atmIfVccSrcOperTable.setStatus("mandatory")
_AtmIfVccSrcOperEntry_Object = MibTableRow
atmIfVccSrcOperEntry = _AtmIfVccSrcOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 5, 8, 11, 1)
)
atmIfVccSrcOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfVccIndex"),
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "atmIfVccSrcIndex"),
)
if mibBuilder.loadTexts:
    atmIfVccSrcOperEntry.setStatus("mandatory")


class _AtmIfVccSrcState_Type(Integer32):
    """Custom type atmIfVccSrcState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("active", 0),
          ("inactive", 1))
    )


_AtmIfVccSrcState_Type.__name__ = "Integer32"
_AtmIfVccSrcState_Object = MibTableColumn
atmIfVccSrcState = _AtmIfVccSrcState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 5, 8, 11, 1, 1),
    _AtmIfVccSrcState_Type()
)
atmIfVccSrcState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVccSrcState.setStatus("mandatory")
_AtmIfVccSrcRetryCount_Type = Counter32
_AtmIfVccSrcRetryCount_Object = MibTableColumn
atmIfVccSrcRetryCount = _AtmIfVccSrcRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 5, 8, 11, 1, 2),
    _AtmIfVccSrcRetryCount_Type()
)
atmIfVccSrcRetryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVccSrcRetryCount.setStatus("mandatory")


class _AtmIfVccSrcLastFailureCauseCode_Type(Unsigned32):
    """Custom type atmIfVccSrcLastFailureCauseCode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AtmIfVccSrcLastFailureCauseCode_Type.__name__ = "Unsigned32"
_AtmIfVccSrcLastFailureCauseCode_Object = MibTableColumn
atmIfVccSrcLastFailureCauseCode = _AtmIfVccSrcLastFailureCauseCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 5, 8, 11, 1, 3),
    _AtmIfVccSrcLastFailureCauseCode_Type()
)
atmIfVccSrcLastFailureCauseCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVccSrcLastFailureCauseCode.setStatus("mandatory")


class _AtmIfVccSrcLastFailureDiagCode_Type(AsciiString):
    """Custom type atmIfVccSrcLastFailureDiagCode based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_AtmIfVccSrcLastFailureDiagCode_Type.__name__ = "AsciiString"
_AtmIfVccSrcLastFailureDiagCode_Object = MibTableColumn
atmIfVccSrcLastFailureDiagCode = _AtmIfVccSrcLastFailureDiagCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 5, 8, 11, 1, 4),
    _AtmIfVccSrcLastFailureDiagCode_Type()
)
atmIfVccSrcLastFailureDiagCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVccSrcLastFailureDiagCode.setStatus("mandatory")
_AtmIfVccEp_ObjectIdentity = ObjectIdentity
atmIfVccEp = _AtmIfVccEp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 5, 9)
)
_AtmIfVccEpRowStatusTable_Object = MibTable
atmIfVccEpRowStatusTable = _AtmIfVccEpRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 5, 9, 1)
)
if mibBuilder.loadTexts:
    atmIfVccEpRowStatusTable.setStatus("mandatory")
_AtmIfVccEpRowStatusEntry_Object = MibTableRow
atmIfVccEpRowStatusEntry = _AtmIfVccEpRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 5, 9, 1, 1)
)
atmIfVccEpRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfVccIndex"),
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "atmIfVccEpIndex"),
)
if mibBuilder.loadTexts:
    atmIfVccEpRowStatusEntry.setStatus("mandatory")
_AtmIfVccEpRowStatus_Type = RowStatus
_AtmIfVccEpRowStatus_Object = MibTableColumn
atmIfVccEpRowStatus = _AtmIfVccEpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 5, 9, 1, 1, 1),
    _AtmIfVccEpRowStatus_Type()
)
atmIfVccEpRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVccEpRowStatus.setStatus("mandatory")
_AtmIfVccEpComponentName_Type = DisplayString
_AtmIfVccEpComponentName_Object = MibTableColumn
atmIfVccEpComponentName = _AtmIfVccEpComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 5, 9, 1, 1, 2),
    _AtmIfVccEpComponentName_Type()
)
atmIfVccEpComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVccEpComponentName.setStatus("mandatory")
_AtmIfVccEpStorageType_Type = StorageType
_AtmIfVccEpStorageType_Object = MibTableColumn
atmIfVccEpStorageType = _AtmIfVccEpStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 5, 9, 1, 1, 4),
    _AtmIfVccEpStorageType_Type()
)
atmIfVccEpStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVccEpStorageType.setStatus("mandatory")
_AtmIfVccEpIndex_Type = NonReplicated
_AtmIfVccEpIndex_Object = MibTableColumn
atmIfVccEpIndex = _AtmIfVccEpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 5, 9, 1, 1, 10),
    _AtmIfVccEpIndex_Type()
)
atmIfVccEpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmIfVccEpIndex.setStatus("mandatory")
_AtmIfVccEpOperTable_Object = MibTable
atmIfVccEpOperTable = _AtmIfVccEpOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 5, 9, 10)
)
if mibBuilder.loadTexts:
    atmIfVccEpOperTable.setStatus("mandatory")
_AtmIfVccEpOperEntry_Object = MibTableRow
atmIfVccEpOperEntry = _AtmIfVccEpOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 5, 9, 10, 1)
)
atmIfVccEpOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfVccIndex"),
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "atmIfVccEpIndex"),
)
if mibBuilder.loadTexts:
    atmIfVccEpOperEntry.setStatus("mandatory")
_AtmIfVccEpApplicationName_Type = RowPointer
_AtmIfVccEpApplicationName_Object = MibTableColumn
atmIfVccEpApplicationName = _AtmIfVccEpApplicationName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 5, 9, 10, 1, 1),
    _AtmIfVccEpApplicationName_Type()
)
atmIfVccEpApplicationName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVccEpApplicationName.setStatus("mandatory")
_AtmIfVccRp_ObjectIdentity = ObjectIdentity
atmIfVccRp = _AtmIfVccRp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 5, 10)
)
_AtmIfVccRpRowStatusTable_Object = MibTable
atmIfVccRpRowStatusTable = _AtmIfVccRpRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 5, 10, 1)
)
if mibBuilder.loadTexts:
    atmIfVccRpRowStatusTable.setStatus("mandatory")
_AtmIfVccRpRowStatusEntry_Object = MibTableRow
atmIfVccRpRowStatusEntry = _AtmIfVccRpRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 5, 10, 1, 1)
)
atmIfVccRpRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfVccIndex"),
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "atmIfVccRpIndex"),
)
if mibBuilder.loadTexts:
    atmIfVccRpRowStatusEntry.setStatus("mandatory")
_AtmIfVccRpRowStatus_Type = RowStatus
_AtmIfVccRpRowStatus_Object = MibTableColumn
atmIfVccRpRowStatus = _AtmIfVccRpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 5, 10, 1, 1, 1),
    _AtmIfVccRpRowStatus_Type()
)
atmIfVccRpRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVccRpRowStatus.setStatus("mandatory")
_AtmIfVccRpComponentName_Type = DisplayString
_AtmIfVccRpComponentName_Object = MibTableColumn
atmIfVccRpComponentName = _AtmIfVccRpComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 5, 10, 1, 1, 2),
    _AtmIfVccRpComponentName_Type()
)
atmIfVccRpComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVccRpComponentName.setStatus("mandatory")
_AtmIfVccRpStorageType_Type = StorageType
_AtmIfVccRpStorageType_Object = MibTableColumn
atmIfVccRpStorageType = _AtmIfVccRpStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 5, 10, 1, 1, 4),
    _AtmIfVccRpStorageType_Type()
)
atmIfVccRpStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVccRpStorageType.setStatus("mandatory")
_AtmIfVccRpIndex_Type = NonReplicated
_AtmIfVccRpIndex_Object = MibTableColumn
atmIfVccRpIndex = _AtmIfVccRpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 5, 10, 1, 1, 10),
    _AtmIfVccRpIndex_Type()
)
atmIfVccRpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmIfVccRpIndex.setStatus("mandatory")
_AtmIfVccRpOperTable_Object = MibTable
atmIfVccRpOperTable = _AtmIfVccRpOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 5, 10, 10)
)
if mibBuilder.loadTexts:
    atmIfVccRpOperTable.setStatus("mandatory")
_AtmIfVccRpOperEntry_Object = MibTableRow
atmIfVccRpOperEntry = _AtmIfVccRpOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 5, 10, 10, 1)
)
atmIfVccRpOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfVccIndex"),
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "atmIfVccRpIndex"),
)
if mibBuilder.loadTexts:
    atmIfVccRpOperEntry.setStatus("mandatory")
_AtmIfVccRpNextHop_Type = RowPointer
_AtmIfVccRpNextHop_Object = MibTableColumn
atmIfVccRpNextHop = _AtmIfVccRpNextHop_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 5, 10, 10, 1, 1),
    _AtmIfVccRpNextHop_Type()
)
atmIfVccRpNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVccRpNextHop.setStatus("obsolete")
_AtmIfVccRpNextHopsTable_Object = MibTable
atmIfVccRpNextHopsTable = _AtmIfVccRpNextHopsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 5, 10, 430)
)
if mibBuilder.loadTexts:
    atmIfVccRpNextHopsTable.setStatus("mandatory")
_AtmIfVccRpNextHopsEntry_Object = MibTableRow
atmIfVccRpNextHopsEntry = _AtmIfVccRpNextHopsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 5, 10, 430, 1)
)
atmIfVccRpNextHopsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfVccIndex"),
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "atmIfVccRpIndex"),
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "atmIfVccRpNextHopsValue"),
)
if mibBuilder.loadTexts:
    atmIfVccRpNextHopsEntry.setStatus("mandatory")
_AtmIfVccRpNextHopsValue_Type = RowPointer
_AtmIfVccRpNextHopsValue_Object = MibTableColumn
atmIfVccRpNextHopsValue = _AtmIfVccRpNextHopsValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 5, 10, 430, 1, 1),
    _AtmIfVccRpNextHopsValue_Type()
)
atmIfVccRpNextHopsValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVccRpNextHopsValue.setStatus("mandatory")
_AtmIfVccDst_ObjectIdentity = ObjectIdentity
atmIfVccDst = _AtmIfVccDst_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 5, 11)
)
_AtmIfVccDstRowStatusTable_Object = MibTable
atmIfVccDstRowStatusTable = _AtmIfVccDstRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 5, 11, 1)
)
if mibBuilder.loadTexts:
    atmIfVccDstRowStatusTable.setStatus("mandatory")
_AtmIfVccDstRowStatusEntry_Object = MibTableRow
atmIfVccDstRowStatusEntry = _AtmIfVccDstRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 5, 11, 1, 1)
)
atmIfVccDstRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfVccIndex"),
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "atmIfVccDstIndex"),
)
if mibBuilder.loadTexts:
    atmIfVccDstRowStatusEntry.setStatus("mandatory")
_AtmIfVccDstRowStatus_Type = RowStatus
_AtmIfVccDstRowStatus_Object = MibTableColumn
atmIfVccDstRowStatus = _AtmIfVccDstRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 5, 11, 1, 1, 1),
    _AtmIfVccDstRowStatus_Type()
)
atmIfVccDstRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVccDstRowStatus.setStatus("mandatory")
_AtmIfVccDstComponentName_Type = DisplayString
_AtmIfVccDstComponentName_Object = MibTableColumn
atmIfVccDstComponentName = _AtmIfVccDstComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 5, 11, 1, 1, 2),
    _AtmIfVccDstComponentName_Type()
)
atmIfVccDstComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVccDstComponentName.setStatus("mandatory")
_AtmIfVccDstStorageType_Type = StorageType
_AtmIfVccDstStorageType_Object = MibTableColumn
atmIfVccDstStorageType = _AtmIfVccDstStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 5, 11, 1, 1, 4),
    _AtmIfVccDstStorageType_Type()
)
atmIfVccDstStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVccDstStorageType.setStatus("mandatory")
_AtmIfVccDstIndex_Type = NonReplicated
_AtmIfVccDstIndex_Object = MibTableColumn
atmIfVccDstIndex = _AtmIfVccDstIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 5, 11, 1, 1, 10),
    _AtmIfVccDstIndex_Type()
)
atmIfVccDstIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmIfVccDstIndex.setStatus("mandatory")
_AtmIfVccDstOperTable_Object = MibTable
atmIfVccDstOperTable = _AtmIfVccDstOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 5, 11, 10)
)
if mibBuilder.loadTexts:
    atmIfVccDstOperTable.setStatus("mandatory")
_AtmIfVccDstOperEntry_Object = MibTableRow
atmIfVccDstOperEntry = _AtmIfVccDstOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 5, 11, 10, 1)
)
atmIfVccDstOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfVccIndex"),
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "atmIfVccDstIndex"),
)
if mibBuilder.loadTexts:
    atmIfVccDstOperEntry.setStatus("mandatory")


class _AtmIfVccDstCalledAddress_Type(HexString):
    """Custom type atmIfVccDstCalledAddress based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_AtmIfVccDstCalledAddress_Type.__name__ = "HexString"
_AtmIfVccDstCalledAddress_Object = MibTableColumn
atmIfVccDstCalledAddress = _AtmIfVccDstCalledAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 5, 11, 10, 1, 3),
    _AtmIfVccDstCalledAddress_Type()
)
atmIfVccDstCalledAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVccDstCalledAddress.setStatus("mandatory")


class _AtmIfVccDstCallingAddress_Type(AsciiString):
    """Custom type atmIfVccDstCallingAddress based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 40),
    )


_AtmIfVccDstCallingAddress_Type.__name__ = "AsciiString"
_AtmIfVccDstCallingAddress_Object = MibTableColumn
atmIfVccDstCallingAddress = _AtmIfVccDstCallingAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 5, 11, 10, 1, 4),
    _AtmIfVccDstCallingAddress_Type()
)
atmIfVccDstCallingAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVccDstCallingAddress.setStatus("mandatory")


class _AtmIfVccDstCallingVpiVci_Type(AsciiString):
    """Custom type atmIfVccDstCallingVpiVci based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 9),
    )


_AtmIfVccDstCallingVpiVci_Type.__name__ = "AsciiString"
_AtmIfVccDstCallingVpiVci_Object = MibTableColumn
atmIfVccDstCallingVpiVci = _AtmIfVccDstCallingVpiVci_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 5, 11, 10, 1, 5),
    _AtmIfVccDstCallingVpiVci_Type()
)
atmIfVccDstCallingVpiVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVccDstCallingVpiVci.setStatus("mandatory")
_AtmIfVptVccSrc_ObjectIdentity = ObjectIdentity
atmIfVptVccSrc = _AtmIfVptVccSrc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 20, 8)
)
_AtmIfVptVccSrcRowStatusTable_Object = MibTable
atmIfVptVccSrcRowStatusTable = _AtmIfVptVccSrcRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 20, 8, 1)
)
if mibBuilder.loadTexts:
    atmIfVptVccSrcRowStatusTable.setStatus("mandatory")
_AtmIfVptVccSrcRowStatusEntry_Object = MibTableRow
atmIfVptVccSrcRowStatusEntry = _AtmIfVptVccSrcRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 20, 8, 1, 1)
)
atmIfVptVccSrcRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfVptIndex"),
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfVptVccIndex"),
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "atmIfVptVccSrcIndex"),
)
if mibBuilder.loadTexts:
    atmIfVptVccSrcRowStatusEntry.setStatus("mandatory")
_AtmIfVptVccSrcRowStatus_Type = RowStatus
_AtmIfVptVccSrcRowStatus_Object = MibTableColumn
atmIfVptVccSrcRowStatus = _AtmIfVptVccSrcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 20, 8, 1, 1, 1),
    _AtmIfVptVccSrcRowStatus_Type()
)
atmIfVptVccSrcRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfVptVccSrcRowStatus.setStatus("mandatory")
_AtmIfVptVccSrcComponentName_Type = DisplayString
_AtmIfVptVccSrcComponentName_Object = MibTableColumn
atmIfVptVccSrcComponentName = _AtmIfVptVccSrcComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 20, 8, 1, 1, 2),
    _AtmIfVptVccSrcComponentName_Type()
)
atmIfVptVccSrcComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVptVccSrcComponentName.setStatus("mandatory")
_AtmIfVptVccSrcStorageType_Type = StorageType
_AtmIfVptVccSrcStorageType_Object = MibTableColumn
atmIfVptVccSrcStorageType = _AtmIfVptVccSrcStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 20, 8, 1, 1, 4),
    _AtmIfVptVccSrcStorageType_Type()
)
atmIfVptVccSrcStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVptVccSrcStorageType.setStatus("mandatory")
_AtmIfVptVccSrcIndex_Type = NonReplicated
_AtmIfVptVccSrcIndex_Object = MibTableColumn
atmIfVptVccSrcIndex = _AtmIfVptVccSrcIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 20, 8, 1, 1, 10),
    _AtmIfVptVccSrcIndex_Type()
)
atmIfVptVccSrcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmIfVptVccSrcIndex.setStatus("mandatory")
_AtmIfVptVccSrcProvTable_Object = MibTable
atmIfVptVccSrcProvTable = _AtmIfVptVccSrcProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 20, 8, 10)
)
if mibBuilder.loadTexts:
    atmIfVptVccSrcProvTable.setStatus("mandatory")
_AtmIfVptVccSrcProvEntry_Object = MibTableRow
atmIfVptVccSrcProvEntry = _AtmIfVptVccSrcProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 20, 8, 10, 1)
)
atmIfVptVccSrcProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfVptIndex"),
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfVptVccIndex"),
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "atmIfVptVccSrcIndex"),
)
if mibBuilder.loadTexts:
    atmIfVptVccSrcProvEntry.setStatus("mandatory")


class _AtmIfVptVccSrcRemoteAddress_Type(HexString):
    """Custom type atmIfVptVccSrcRemoteAddress based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_AtmIfVptVccSrcRemoteAddress_Type.__name__ = "HexString"
_AtmIfVptVccSrcRemoteAddress_Object = MibTableColumn
atmIfVptVccSrcRemoteAddress = _AtmIfVptVccSrcRemoteAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 20, 8, 10, 1, 1),
    _AtmIfVptVccSrcRemoteAddress_Type()
)
atmIfVptVccSrcRemoteAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfVptVccSrcRemoteAddress.setStatus("obsolete")


class _AtmIfVptVccSrcRemoteVpiVci_Type(IntegerSequence):
    """Custom type atmIfVptVccSrcRemoteVpiVci based on IntegerSequence"""
    subtypeSpec = IntegerSequence.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 9),
    )


_AtmIfVptVccSrcRemoteVpiVci_Type.__name__ = "IntegerSequence"
_AtmIfVptVccSrcRemoteVpiVci_Object = MibTableColumn
atmIfVptVccSrcRemoteVpiVci = _AtmIfVptVccSrcRemoteVpiVci_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 20, 8, 10, 1, 2),
    _AtmIfVptVccSrcRemoteVpiVci_Type()
)
atmIfVptVccSrcRemoteVpiVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfVptVccSrcRemoteVpiVci.setStatus("obsolete")


class _AtmIfVptVccSrcCallingAddress_Type(HexString):
    """Custom type atmIfVptVccSrcCallingAddress based on HexString"""
    defaultHexValue = ""

    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_AtmIfVptVccSrcCallingAddress_Type.__name__ = "HexString"
_AtmIfVptVccSrcCallingAddress_Object = MibTableColumn
atmIfVptVccSrcCallingAddress = _AtmIfVptVccSrcCallingAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 20, 8, 10, 1, 3),
    _AtmIfVptVccSrcCallingAddress_Type()
)
atmIfVptVccSrcCallingAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfVptVccSrcCallingAddress.setStatus("mandatory")


class _AtmIfVptVccSrcCalledAddress_Type(HexString):
    """Custom type atmIfVptVccSrcCalledAddress based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_AtmIfVptVccSrcCalledAddress_Type.__name__ = "HexString"
_AtmIfVptVccSrcCalledAddress_Object = MibTableColumn
atmIfVptVccSrcCalledAddress = _AtmIfVptVccSrcCalledAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 20, 8, 10, 1, 4),
    _AtmIfVptVccSrcCalledAddress_Type()
)
atmIfVptVccSrcCalledAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfVptVccSrcCalledAddress.setStatus("mandatory")


class _AtmIfVptVccSrcCalledVpiVci_Type(IntegerSequence):
    """Custom type atmIfVptVccSrcCalledVpiVci based on IntegerSequence"""
    subtypeSpec = IntegerSequence.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 10),
    )


_AtmIfVptVccSrcCalledVpiVci_Type.__name__ = "IntegerSequence"
_AtmIfVptVccSrcCalledVpiVci_Object = MibTableColumn
atmIfVptVccSrcCalledVpiVci = _AtmIfVptVccSrcCalledVpiVci_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 20, 8, 10, 1, 5),
    _AtmIfVptVccSrcCalledVpiVci_Type()
)
atmIfVptVccSrcCalledVpiVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfVptVccSrcCalledVpiVci.setStatus("mandatory")
_AtmIfVptVccSrcOperTable_Object = MibTable
atmIfVptVccSrcOperTable = _AtmIfVptVccSrcOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 20, 8, 11)
)
if mibBuilder.loadTexts:
    atmIfVptVccSrcOperTable.setStatus("mandatory")
_AtmIfVptVccSrcOperEntry_Object = MibTableRow
atmIfVptVccSrcOperEntry = _AtmIfVptVccSrcOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 20, 8, 11, 1)
)
atmIfVptVccSrcOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfVptIndex"),
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfVptVccIndex"),
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "atmIfVptVccSrcIndex"),
)
if mibBuilder.loadTexts:
    atmIfVptVccSrcOperEntry.setStatus("mandatory")


class _AtmIfVptVccSrcState_Type(Integer32):
    """Custom type atmIfVptVccSrcState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("active", 0),
          ("inactive", 1))
    )


_AtmIfVptVccSrcState_Type.__name__ = "Integer32"
_AtmIfVptVccSrcState_Object = MibTableColumn
atmIfVptVccSrcState = _AtmIfVptVccSrcState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 20, 8, 11, 1, 1),
    _AtmIfVptVccSrcState_Type()
)
atmIfVptVccSrcState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVptVccSrcState.setStatus("mandatory")
_AtmIfVptVccSrcRetryCount_Type = Counter32
_AtmIfVptVccSrcRetryCount_Object = MibTableColumn
atmIfVptVccSrcRetryCount = _AtmIfVptVccSrcRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 20, 8, 11, 1, 2),
    _AtmIfVptVccSrcRetryCount_Type()
)
atmIfVptVccSrcRetryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVptVccSrcRetryCount.setStatus("mandatory")


class _AtmIfVptVccSrcLastFailureCauseCode_Type(Unsigned32):
    """Custom type atmIfVptVccSrcLastFailureCauseCode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AtmIfVptVccSrcLastFailureCauseCode_Type.__name__ = "Unsigned32"
_AtmIfVptVccSrcLastFailureCauseCode_Object = MibTableColumn
atmIfVptVccSrcLastFailureCauseCode = _AtmIfVptVccSrcLastFailureCauseCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 20, 8, 11, 1, 3),
    _AtmIfVptVccSrcLastFailureCauseCode_Type()
)
atmIfVptVccSrcLastFailureCauseCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVptVccSrcLastFailureCauseCode.setStatus("mandatory")


class _AtmIfVptVccSrcLastFailureDiagCode_Type(AsciiString):
    """Custom type atmIfVptVccSrcLastFailureDiagCode based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_AtmIfVptVccSrcLastFailureDiagCode_Type.__name__ = "AsciiString"
_AtmIfVptVccSrcLastFailureDiagCode_Object = MibTableColumn
atmIfVptVccSrcLastFailureDiagCode = _AtmIfVptVccSrcLastFailureDiagCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 20, 8, 11, 1, 4),
    _AtmIfVptVccSrcLastFailureDiagCode_Type()
)
atmIfVptVccSrcLastFailureDiagCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVptVccSrcLastFailureDiagCode.setStatus("mandatory")
_AtmIfVptVccEp_ObjectIdentity = ObjectIdentity
atmIfVptVccEp = _AtmIfVptVccEp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 20, 9)
)
_AtmIfVptVccEpRowStatusTable_Object = MibTable
atmIfVptVccEpRowStatusTable = _AtmIfVptVccEpRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 20, 9, 1)
)
if mibBuilder.loadTexts:
    atmIfVptVccEpRowStatusTable.setStatus("mandatory")
_AtmIfVptVccEpRowStatusEntry_Object = MibTableRow
atmIfVptVccEpRowStatusEntry = _AtmIfVptVccEpRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 20, 9, 1, 1)
)
atmIfVptVccEpRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfVptIndex"),
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfVptVccIndex"),
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "atmIfVptVccEpIndex"),
)
if mibBuilder.loadTexts:
    atmIfVptVccEpRowStatusEntry.setStatus("mandatory")
_AtmIfVptVccEpRowStatus_Type = RowStatus
_AtmIfVptVccEpRowStatus_Object = MibTableColumn
atmIfVptVccEpRowStatus = _AtmIfVptVccEpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 20, 9, 1, 1, 1),
    _AtmIfVptVccEpRowStatus_Type()
)
atmIfVptVccEpRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVptVccEpRowStatus.setStatus("mandatory")
_AtmIfVptVccEpComponentName_Type = DisplayString
_AtmIfVptVccEpComponentName_Object = MibTableColumn
atmIfVptVccEpComponentName = _AtmIfVptVccEpComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 20, 9, 1, 1, 2),
    _AtmIfVptVccEpComponentName_Type()
)
atmIfVptVccEpComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVptVccEpComponentName.setStatus("mandatory")
_AtmIfVptVccEpStorageType_Type = StorageType
_AtmIfVptVccEpStorageType_Object = MibTableColumn
atmIfVptVccEpStorageType = _AtmIfVptVccEpStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 20, 9, 1, 1, 4),
    _AtmIfVptVccEpStorageType_Type()
)
atmIfVptVccEpStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVptVccEpStorageType.setStatus("mandatory")
_AtmIfVptVccEpIndex_Type = NonReplicated
_AtmIfVptVccEpIndex_Object = MibTableColumn
atmIfVptVccEpIndex = _AtmIfVptVccEpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 20, 9, 1, 1, 10),
    _AtmIfVptVccEpIndex_Type()
)
atmIfVptVccEpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmIfVptVccEpIndex.setStatus("mandatory")
_AtmIfVptVccEpOperTable_Object = MibTable
atmIfVptVccEpOperTable = _AtmIfVptVccEpOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 20, 9, 10)
)
if mibBuilder.loadTexts:
    atmIfVptVccEpOperTable.setStatus("mandatory")
_AtmIfVptVccEpOperEntry_Object = MibTableRow
atmIfVptVccEpOperEntry = _AtmIfVptVccEpOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 20, 9, 10, 1)
)
atmIfVptVccEpOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfVptIndex"),
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfVptVccIndex"),
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "atmIfVptVccEpIndex"),
)
if mibBuilder.loadTexts:
    atmIfVptVccEpOperEntry.setStatus("mandatory")
_AtmIfVptVccEpApplicationName_Type = RowPointer
_AtmIfVptVccEpApplicationName_Object = MibTableColumn
atmIfVptVccEpApplicationName = _AtmIfVptVccEpApplicationName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 20, 9, 10, 1, 1),
    _AtmIfVptVccEpApplicationName_Type()
)
atmIfVptVccEpApplicationName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVptVccEpApplicationName.setStatus("mandatory")
_AtmIfVptVccRp_ObjectIdentity = ObjectIdentity
atmIfVptVccRp = _AtmIfVptVccRp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 20, 10)
)
_AtmIfVptVccRpRowStatusTable_Object = MibTable
atmIfVptVccRpRowStatusTable = _AtmIfVptVccRpRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 20, 10, 1)
)
if mibBuilder.loadTexts:
    atmIfVptVccRpRowStatusTable.setStatus("mandatory")
_AtmIfVptVccRpRowStatusEntry_Object = MibTableRow
atmIfVptVccRpRowStatusEntry = _AtmIfVptVccRpRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 20, 10, 1, 1)
)
atmIfVptVccRpRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfVptIndex"),
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfVptVccIndex"),
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "atmIfVptVccRpIndex"),
)
if mibBuilder.loadTexts:
    atmIfVptVccRpRowStatusEntry.setStatus("mandatory")
_AtmIfVptVccRpRowStatus_Type = RowStatus
_AtmIfVptVccRpRowStatus_Object = MibTableColumn
atmIfVptVccRpRowStatus = _AtmIfVptVccRpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 20, 10, 1, 1, 1),
    _AtmIfVptVccRpRowStatus_Type()
)
atmIfVptVccRpRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVptVccRpRowStatus.setStatus("mandatory")
_AtmIfVptVccRpComponentName_Type = DisplayString
_AtmIfVptVccRpComponentName_Object = MibTableColumn
atmIfVptVccRpComponentName = _AtmIfVptVccRpComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 20, 10, 1, 1, 2),
    _AtmIfVptVccRpComponentName_Type()
)
atmIfVptVccRpComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVptVccRpComponentName.setStatus("mandatory")
_AtmIfVptVccRpStorageType_Type = StorageType
_AtmIfVptVccRpStorageType_Object = MibTableColumn
atmIfVptVccRpStorageType = _AtmIfVptVccRpStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 20, 10, 1, 1, 4),
    _AtmIfVptVccRpStorageType_Type()
)
atmIfVptVccRpStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVptVccRpStorageType.setStatus("mandatory")
_AtmIfVptVccRpIndex_Type = NonReplicated
_AtmIfVptVccRpIndex_Object = MibTableColumn
atmIfVptVccRpIndex = _AtmIfVptVccRpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 20, 10, 1, 1, 10),
    _AtmIfVptVccRpIndex_Type()
)
atmIfVptVccRpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmIfVptVccRpIndex.setStatus("mandatory")
_AtmIfVptVccRpOperTable_Object = MibTable
atmIfVptVccRpOperTable = _AtmIfVptVccRpOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 20, 10, 10)
)
if mibBuilder.loadTexts:
    atmIfVptVccRpOperTable.setStatus("mandatory")
_AtmIfVptVccRpOperEntry_Object = MibTableRow
atmIfVptVccRpOperEntry = _AtmIfVptVccRpOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 20, 10, 10, 1)
)
atmIfVptVccRpOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfVptIndex"),
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfVptVccIndex"),
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "atmIfVptVccRpIndex"),
)
if mibBuilder.loadTexts:
    atmIfVptVccRpOperEntry.setStatus("mandatory")
_AtmIfVptVccRpNextHop_Type = RowPointer
_AtmIfVptVccRpNextHop_Object = MibTableColumn
atmIfVptVccRpNextHop = _AtmIfVptVccRpNextHop_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 20, 10, 10, 1, 1),
    _AtmIfVptVccRpNextHop_Type()
)
atmIfVptVccRpNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVptVccRpNextHop.setStatus("obsolete")
_AtmIfVptVccRpNextHopsTable_Object = MibTable
atmIfVptVccRpNextHopsTable = _AtmIfVptVccRpNextHopsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 20, 10, 430)
)
if mibBuilder.loadTexts:
    atmIfVptVccRpNextHopsTable.setStatus("mandatory")
_AtmIfVptVccRpNextHopsEntry_Object = MibTableRow
atmIfVptVccRpNextHopsEntry = _AtmIfVptVccRpNextHopsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 20, 10, 430, 1)
)
atmIfVptVccRpNextHopsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfVptIndex"),
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfVptVccIndex"),
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "atmIfVptVccRpIndex"),
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "atmIfVptVccRpNextHopsValue"),
)
if mibBuilder.loadTexts:
    atmIfVptVccRpNextHopsEntry.setStatus("mandatory")
_AtmIfVptVccRpNextHopsValue_Type = RowPointer
_AtmIfVptVccRpNextHopsValue_Object = MibTableColumn
atmIfVptVccRpNextHopsValue = _AtmIfVptVccRpNextHopsValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 20, 10, 430, 1, 1),
    _AtmIfVptVccRpNextHopsValue_Type()
)
atmIfVptVccRpNextHopsValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVptVccRpNextHopsValue.setStatus("mandatory")
_AtmIfVptVccDst_ObjectIdentity = ObjectIdentity
atmIfVptVccDst = _AtmIfVptVccDst_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 20, 11)
)
_AtmIfVptVccDstRowStatusTable_Object = MibTable
atmIfVptVccDstRowStatusTable = _AtmIfVptVccDstRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 20, 11, 1)
)
if mibBuilder.loadTexts:
    atmIfVptVccDstRowStatusTable.setStatus("mandatory")
_AtmIfVptVccDstRowStatusEntry_Object = MibTableRow
atmIfVptVccDstRowStatusEntry = _AtmIfVptVccDstRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 20, 11, 1, 1)
)
atmIfVptVccDstRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfVptIndex"),
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfVptVccIndex"),
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "atmIfVptVccDstIndex"),
)
if mibBuilder.loadTexts:
    atmIfVptVccDstRowStatusEntry.setStatus("mandatory")
_AtmIfVptVccDstRowStatus_Type = RowStatus
_AtmIfVptVccDstRowStatus_Object = MibTableColumn
atmIfVptVccDstRowStatus = _AtmIfVptVccDstRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 20, 11, 1, 1, 1),
    _AtmIfVptVccDstRowStatus_Type()
)
atmIfVptVccDstRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVptVccDstRowStatus.setStatus("mandatory")
_AtmIfVptVccDstComponentName_Type = DisplayString
_AtmIfVptVccDstComponentName_Object = MibTableColumn
atmIfVptVccDstComponentName = _AtmIfVptVccDstComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 20, 11, 1, 1, 2),
    _AtmIfVptVccDstComponentName_Type()
)
atmIfVptVccDstComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVptVccDstComponentName.setStatus("mandatory")
_AtmIfVptVccDstStorageType_Type = StorageType
_AtmIfVptVccDstStorageType_Object = MibTableColumn
atmIfVptVccDstStorageType = _AtmIfVptVccDstStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 20, 11, 1, 1, 4),
    _AtmIfVptVccDstStorageType_Type()
)
atmIfVptVccDstStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVptVccDstStorageType.setStatus("mandatory")
_AtmIfVptVccDstIndex_Type = NonReplicated
_AtmIfVptVccDstIndex_Object = MibTableColumn
atmIfVptVccDstIndex = _AtmIfVptVccDstIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 20, 11, 1, 1, 10),
    _AtmIfVptVccDstIndex_Type()
)
atmIfVptVccDstIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmIfVptVccDstIndex.setStatus("mandatory")
_AtmIfVptVccDstOperTable_Object = MibTable
atmIfVptVccDstOperTable = _AtmIfVptVccDstOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 20, 11, 10)
)
if mibBuilder.loadTexts:
    atmIfVptVccDstOperTable.setStatus("mandatory")
_AtmIfVptVccDstOperEntry_Object = MibTableRow
atmIfVptVccDstOperEntry = _AtmIfVptVccDstOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 20, 11, 10, 1)
)
atmIfVptVccDstOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfVptIndex"),
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfVptVccIndex"),
    (0, "Nortel-Magellan-Passport-AtmNetworkingMIB", "atmIfVptVccDstIndex"),
)
if mibBuilder.loadTexts:
    atmIfVptVccDstOperEntry.setStatus("mandatory")


class _AtmIfVptVccDstCalledAddress_Type(HexString):
    """Custom type atmIfVptVccDstCalledAddress based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_AtmIfVptVccDstCalledAddress_Type.__name__ = "HexString"
_AtmIfVptVccDstCalledAddress_Object = MibTableColumn
atmIfVptVccDstCalledAddress = _AtmIfVptVccDstCalledAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 20, 11, 10, 1, 3),
    _AtmIfVptVccDstCalledAddress_Type()
)
atmIfVptVccDstCalledAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVptVccDstCalledAddress.setStatus("mandatory")


class _AtmIfVptVccDstCallingAddress_Type(AsciiString):
    """Custom type atmIfVptVccDstCallingAddress based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 40),
    )


_AtmIfVptVccDstCallingAddress_Type.__name__ = "AsciiString"
_AtmIfVptVccDstCallingAddress_Object = MibTableColumn
atmIfVptVccDstCallingAddress = _AtmIfVptVccDstCallingAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 20, 11, 10, 1, 4),
    _AtmIfVptVccDstCallingAddress_Type()
)
atmIfVptVccDstCallingAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVptVccDstCallingAddress.setStatus("mandatory")


class _AtmIfVptVccDstCallingVpiVci_Type(AsciiString):
    """Custom type atmIfVptVccDstCallingVpiVci based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 9),
    )


_AtmIfVptVccDstCallingVpiVci_Type.__name__ = "AsciiString"
_AtmIfVptVccDstCallingVpiVci_Object = MibTableColumn
atmIfVptVccDstCallingVpiVci = _AtmIfVptVccDstCallingVpiVci_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 20, 11, 10, 1, 5),
    _AtmIfVptVccDstCallingVpiVci_Type()
)
atmIfVptVccDstCallingVpiVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVptVccDstCallingVpiVci.setStatus("mandatory")
_AtmNetworkingMIB_ObjectIdentity = ObjectIdentity
atmNetworkingMIB = _AtmNetworkingMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 42)
)
_AtmNetworkingGroup_ObjectIdentity = ObjectIdentity
atmNetworkingGroup = _AtmNetworkingGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 42, 1)
)
_AtmNetworkingGroupBE_ObjectIdentity = ObjectIdentity
atmNetworkingGroupBE = _AtmNetworkingGroupBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 42, 1, 5)
)
_AtmNetworkingGroupBE01_ObjectIdentity = ObjectIdentity
atmNetworkingGroupBE01 = _AtmNetworkingGroupBE01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 42, 1, 5, 2)
)
_AtmNetworkingGroupBE01A_ObjectIdentity = ObjectIdentity
atmNetworkingGroupBE01A = _AtmNetworkingGroupBE01A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 42, 1, 5, 2, 2)
)
_AtmNetworkingCapabilities_ObjectIdentity = ObjectIdentity
atmNetworkingCapabilities = _AtmNetworkingCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 42, 3)
)
_AtmNetworkingCapabilitiesBE_ObjectIdentity = ObjectIdentity
atmNetworkingCapabilitiesBE = _AtmNetworkingCapabilitiesBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 42, 3, 5)
)
_AtmNetworkingCapabilitiesBE01_ObjectIdentity = ObjectIdentity
atmNetworkingCapabilitiesBE01 = _AtmNetworkingCapabilitiesBE01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 42, 3, 5, 2)
)
_AtmNetworkingCapabilitiesBE01A_ObjectIdentity = ObjectIdentity
atmNetworkingCapabilitiesBE01A = _AtmNetworkingCapabilitiesBE01A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 42, 3, 5, 2, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-Magellan-Passport-AtmNetworkingMIB",
    **{"aRtg": aRtg,
       "aRtgRowStatusTable": aRtgRowStatusTable,
       "aRtgRowStatusEntry": aRtgRowStatusEntry,
       "aRtgRowStatus": aRtgRowStatus,
       "aRtgComponentName": aRtgComponentName,
       "aRtgStorageType": aRtgStorageType,
       "aRtgIndex": aRtgIndex,
       "aRtgDna": aRtgDna,
       "aRtgDnaRowStatusTable": aRtgDnaRowStatusTable,
       "aRtgDnaRowStatusEntry": aRtgDnaRowStatusEntry,
       "aRtgDnaRowStatus": aRtgDnaRowStatus,
       "aRtgDnaComponentName": aRtgDnaComponentName,
       "aRtgDnaStorageType": aRtgDnaStorageType,
       "aRtgDnaIndex": aRtgDnaIndex,
       "aRtgDnaDestInfo": aRtgDnaDestInfo,
       "aRtgDnaDestInfoRowStatusTable": aRtgDnaDestInfoRowStatusTable,
       "aRtgDnaDestInfoRowStatusEntry": aRtgDnaDestInfoRowStatusEntry,
       "aRtgDnaDestInfoRowStatus": aRtgDnaDestInfoRowStatus,
       "aRtgDnaDestInfoComponentName": aRtgDnaDestInfoComponentName,
       "aRtgDnaDestInfoStorageType": aRtgDnaDestInfoStorageType,
       "aRtgDnaDestInfoIndex": aRtgDnaDestInfoIndex,
       "aRtgDnaDestInfoOperTable": aRtgDnaDestInfoOperTable,
       "aRtgDnaDestInfoOperEntry": aRtgDnaDestInfoOperEntry,
       "aRtgDnaDestInfoType": aRtgDnaDestInfoType,
       "aRtgDnaDestInfoScope": aRtgDnaDestInfoScope,
       "aRtgDnaDestInfoStdComponentName": aRtgDnaDestInfoStdComponentName,
       "aRtgDnaDestInfoReachability": aRtgDnaDestInfoReachability,
       "aRtgPnni": aRtgPnni,
       "aRtgPnniRowStatusTable": aRtgPnniRowStatusTable,
       "aRtgPnniRowStatusEntry": aRtgPnniRowStatusEntry,
       "aRtgPnniRowStatus": aRtgPnniRowStatus,
       "aRtgPnniComponentName": aRtgPnniComponentName,
       "aRtgPnniStorageType": aRtgPnniStorageType,
       "aRtgPnniIndex": aRtgPnniIndex,
       "aRtgPnniRf": aRtgPnniRf,
       "aRtgPnniRfRowStatusTable": aRtgPnniRfRowStatusTable,
       "aRtgPnniRfRowStatusEntry": aRtgPnniRfRowStatusEntry,
       "aRtgPnniRfRowStatus": aRtgPnniRfRowStatus,
       "aRtgPnniRfComponentName": aRtgPnniRfComponentName,
       "aRtgPnniRfStorageType": aRtgPnniRfStorageType,
       "aRtgPnniRfIndex": aRtgPnniRfIndex,
       "aRtgPnniRfCriteriaTable": aRtgPnniRfCriteriaTable,
       "aRtgPnniRfCriteriaEntry": aRtgPnniRfCriteriaEntry,
       "aRtgPnniRfDestinationAddress": aRtgPnniRfDestinationAddress,
       "aRtgPnniRfMaxRoutes": aRtgPnniRfMaxRoutes,
       "aRtgPnniRfTxTrafficDescType": aRtgPnniRfTxTrafficDescType,
       "aRtgPnniRfRxTrafficDescType": aRtgPnniRfRxTrafficDescType,
       "aRtgPnniRfAtmServiceCategory": aRtgPnniRfAtmServiceCategory,
       "aRtgPnniRfFwdQosClass": aRtgPnniRfFwdQosClass,
       "aRtgPnniRfBwdQosClass": aRtgPnniRfBwdQosClass,
       "aRtgPnniRfBearerClassBbc": aRtgPnniRfBearerClassBbc,
       "aRtgPnniRfTransferCapabilityBbc": aRtgPnniRfTransferCapabilityBbc,
       "aRtgPnniRfClippingBbc": aRtgPnniRfClippingBbc,
       "aRtgPnniRfBestEffort": aRtgPnniRfBestEffort,
       "aRtgPnniRfOptimizationMetric": aRtgPnniRfOptimizationMetric,
       "aRtgPnniRfRxTdpTable": aRtgPnniRfRxTdpTable,
       "aRtgPnniRfRxTdpEntry": aRtgPnniRfRxTdpEntry,
       "aRtgPnniRfRxTdpIndex": aRtgPnniRfRxTdpIndex,
       "aRtgPnniRfRxTdpValue": aRtgPnniRfRxTdpValue,
       "aRtgPnniRfTxTdpTable": aRtgPnniRfTxTdpTable,
       "aRtgPnniRfTxTdpEntry": aRtgPnniRfTxTdpEntry,
       "aRtgPnniRfTxTdpIndex": aRtgPnniRfTxTdpIndex,
       "aRtgPnniRfTxTdpValue": aRtgPnniRfTxTdpValue,
       "aRtgPnniRfFqpTable": aRtgPnniRfFqpTable,
       "aRtgPnniRfFqpEntry": aRtgPnniRfFqpEntry,
       "aRtgPnniRfFqpIndex": aRtgPnniRfFqpIndex,
       "aRtgPnniRfFqpValue": aRtgPnniRfFqpValue,
       "aRtgPnniRfBqpTable": aRtgPnniRfBqpTable,
       "aRtgPnniRfBqpEntry": aRtgPnniRfBqpEntry,
       "aRtgPnniRfBqpIndex": aRtgPnniRfBqpIndex,
       "aRtgPnniRfBqpValue": aRtgPnniRfBqpValue,
       "aRtgPnniCfgNode": aRtgPnniCfgNode,
       "aRtgPnniCfgNodeRowStatusTable": aRtgPnniCfgNodeRowStatusTable,
       "aRtgPnniCfgNodeRowStatusEntry": aRtgPnniCfgNodeRowStatusEntry,
       "aRtgPnniCfgNodeRowStatus": aRtgPnniCfgNodeRowStatus,
       "aRtgPnniCfgNodeComponentName": aRtgPnniCfgNodeComponentName,
       "aRtgPnniCfgNodeStorageType": aRtgPnniCfgNodeStorageType,
       "aRtgPnniCfgNodeIndex": aRtgPnniCfgNodeIndex,
       "aRtgPnniCfgNodeSAddr": aRtgPnniCfgNodeSAddr,
       "aRtgPnniCfgNodeSAddrRowStatusTable": aRtgPnniCfgNodeSAddrRowStatusTable,
       "aRtgPnniCfgNodeSAddrRowStatusEntry": aRtgPnniCfgNodeSAddrRowStatusEntry,
       "aRtgPnniCfgNodeSAddrRowStatus": aRtgPnniCfgNodeSAddrRowStatus,
       "aRtgPnniCfgNodeSAddrComponentName": aRtgPnniCfgNodeSAddrComponentName,
       "aRtgPnniCfgNodeSAddrStorageType": aRtgPnniCfgNodeSAddrStorageType,
       "aRtgPnniCfgNodeSAddrAddressIndex": aRtgPnniCfgNodeSAddrAddressIndex,
       "aRtgPnniCfgNodeSAddrPrefixLengthIndex": aRtgPnniCfgNodeSAddrPrefixLengthIndex,
       "aRtgPnniCfgNodeSAddrReachabilityIndex": aRtgPnniCfgNodeSAddrReachabilityIndex,
       "aRtgPnniCfgNodeSAddrProvTable": aRtgPnniCfgNodeSAddrProvTable,
       "aRtgPnniCfgNodeSAddrProvEntry": aRtgPnniCfgNodeSAddrProvEntry,
       "aRtgPnniCfgNodeSAddrSuppress": aRtgPnniCfgNodeSAddrSuppress,
       "aRtgPnniCfgNodeSAddrOperTable": aRtgPnniCfgNodeSAddrOperTable,
       "aRtgPnniCfgNodeSAddrOperEntry": aRtgPnniCfgNodeSAddrOperEntry,
       "aRtgPnniCfgNodeSAddrState": aRtgPnniCfgNodeSAddrState,
       "aRtgPnniCfgNodeSAddrScope": aRtgPnniCfgNodeSAddrScope,
       "aRtgPnniCfgNodeNbr": aRtgPnniCfgNodeNbr,
       "aRtgPnniCfgNodeNbrRowStatusTable": aRtgPnniCfgNodeNbrRowStatusTable,
       "aRtgPnniCfgNodeNbrRowStatusEntry": aRtgPnniCfgNodeNbrRowStatusEntry,
       "aRtgPnniCfgNodeNbrRowStatus": aRtgPnniCfgNodeNbrRowStatus,
       "aRtgPnniCfgNodeNbrComponentName": aRtgPnniCfgNodeNbrComponentName,
       "aRtgPnniCfgNodeNbrStorageType": aRtgPnniCfgNodeNbrStorageType,
       "aRtgPnniCfgNodeNbrIndex": aRtgPnniCfgNodeNbrIndex,
       "aRtgPnniCfgNodeNbrOperTable": aRtgPnniCfgNodeNbrOperTable,
       "aRtgPnniCfgNodeNbrOperEntry": aRtgPnniCfgNodeNbrOperEntry,
       "aRtgPnniCfgNodeNbrPeerState": aRtgPnniCfgNodeNbrPeerState,
       "aRtgPnniCfgNodeNbrStatsTable": aRtgPnniCfgNodeNbrStatsTable,
       "aRtgPnniCfgNodeNbrStatsEntry": aRtgPnniCfgNodeNbrStatsEntry,
       "aRtgPnniCfgNodeNbrPtspRx": aRtgPnniCfgNodeNbrPtspRx,
       "aRtgPnniCfgNodeNbrPtspTx": aRtgPnniCfgNodeNbrPtspTx,
       "aRtgPnniCfgNodeNbrPtseRx": aRtgPnniCfgNodeNbrPtseRx,
       "aRtgPnniCfgNodeNbrPtseTx": aRtgPnniCfgNodeNbrPtseTx,
       "aRtgPnniCfgNodeNbrPtseReqRx": aRtgPnniCfgNodeNbrPtseReqRx,
       "aRtgPnniCfgNodeNbrPtseReqTx": aRtgPnniCfgNodeNbrPtseReqTx,
       "aRtgPnniCfgNodeNbrPtseAcksRx": aRtgPnniCfgNodeNbrPtseAcksRx,
       "aRtgPnniCfgNodeNbrPtseAcksTx": aRtgPnniCfgNodeNbrPtseAcksTx,
       "aRtgPnniCfgNodeNbrDbSummariesRx": aRtgPnniCfgNodeNbrDbSummariesRx,
       "aRtgPnniCfgNodeNbrDbSummariesTx": aRtgPnniCfgNodeNbrDbSummariesTx,
       "aRtgPnniCfgNodeNbrBadPtspRx": aRtgPnniCfgNodeNbrBadPtspRx,
       "aRtgPnniCfgNodeNbrBadPtseRx": aRtgPnniCfgNodeNbrBadPtseRx,
       "aRtgPnniCfgNodeNbrBadPtseReqRx": aRtgPnniCfgNodeNbrBadPtseReqRx,
       "aRtgPnniCfgNodeNbrBadPtseAckRx": aRtgPnniCfgNodeNbrBadPtseAckRx,
       "aRtgPnniCfgNodeNbrBadDbSummariesRx": aRtgPnniCfgNodeNbrBadDbSummariesRx,
       "aRtgPnniCfgNodeNbrRccListTable": aRtgPnniCfgNodeNbrRccListTable,
       "aRtgPnniCfgNodeNbrRccListEntry": aRtgPnniCfgNodeNbrRccListEntry,
       "aRtgPnniCfgNodeNbrRccListValue": aRtgPnniCfgNodeNbrRccListValue,
       "aRtgPnniCfgNodeDefSAddr": aRtgPnniCfgNodeDefSAddr,
       "aRtgPnniCfgNodeDefSAddrRowStatusTable": aRtgPnniCfgNodeDefSAddrRowStatusTable,
       "aRtgPnniCfgNodeDefSAddrRowStatusEntry": aRtgPnniCfgNodeDefSAddrRowStatusEntry,
       "aRtgPnniCfgNodeDefSAddrRowStatus": aRtgPnniCfgNodeDefSAddrRowStatus,
       "aRtgPnniCfgNodeDefSAddrComponentName": aRtgPnniCfgNodeDefSAddrComponentName,
       "aRtgPnniCfgNodeDefSAddrStorageType": aRtgPnniCfgNodeDefSAddrStorageType,
       "aRtgPnniCfgNodeDefSAddrIndex": aRtgPnniCfgNodeDefSAddrIndex,
       "aRtgPnniCfgNodeDefSAddrDefAddrTable": aRtgPnniCfgNodeDefSAddrDefAddrTable,
       "aRtgPnniCfgNodeDefSAddrDefAddrEntry": aRtgPnniCfgNodeDefSAddrDefAddrEntry,
       "aRtgPnniCfgNodeDefSAddrAddress": aRtgPnniCfgNodeDefSAddrAddress,
       "aRtgPnniCfgNodeDefSAddrOperTable": aRtgPnniCfgNodeDefSAddrOperTable,
       "aRtgPnniCfgNodeDefSAddrOperEntry": aRtgPnniCfgNodeDefSAddrOperEntry,
       "aRtgPnniCfgNodeDefSAddrState": aRtgPnniCfgNodeDefSAddrState,
       "aRtgPnniCfgNodeDefSAddrScope": aRtgPnniCfgNodeDefSAddrScope,
       "aRtgPnniCfgNodeProvTable": aRtgPnniCfgNodeProvTable,
       "aRtgPnniCfgNodeProvEntry": aRtgPnniCfgNodeProvEntry,
       "aRtgPnniCfgNodeNodeId": aRtgPnniCfgNodeNodeId,
       "aRtgPnniCfgNodePeerGroupId": aRtgPnniCfgNodePeerGroupId,
       "aRtgPnniCfgNodeOperTable": aRtgPnniCfgNodeOperTable,
       "aRtgPnniCfgNodeOperEntry": aRtgPnniCfgNodeOperEntry,
       "aRtgPnniCfgNodeNodeAddress": aRtgPnniCfgNodeNodeAddress,
       "aRtgPnniCfgNodeOpNodeId": aRtgPnniCfgNodeOpNodeId,
       "aRtgPnniCfgNodeOpPeerGroupId": aRtgPnniCfgNodeOpPeerGroupId,
       "aRtgPnniCfgNodeNumNeighbors": aRtgPnniCfgNodeNumNeighbors,
       "aRtgPnniCfgNodeNumRccs": aRtgPnniCfgNodeNumRccs,
       "aRtgPnniCfgNodeCurrentLeadershipPriority": aRtgPnniCfgNodeCurrentLeadershipPriority,
       "aRtgPnniCfgNodePglElectionState": aRtgPnniCfgNodePglElectionState,
       "aRtgPnniTop": aRtgPnniTop,
       "aRtgPnniTopRowStatusTable": aRtgPnniTopRowStatusTable,
       "aRtgPnniTopRowStatusEntry": aRtgPnniTopRowStatusEntry,
       "aRtgPnniTopRowStatus": aRtgPnniTopRowStatus,
       "aRtgPnniTopComponentName": aRtgPnniTopComponentName,
       "aRtgPnniTopStorageType": aRtgPnniTopStorageType,
       "aRtgPnniTopIndex": aRtgPnniTopIndex,
       "aRtgPnniTopNode": aRtgPnniTopNode,
       "aRtgPnniTopNodeRowStatusTable": aRtgPnniTopNodeRowStatusTable,
       "aRtgPnniTopNodeRowStatusEntry": aRtgPnniTopNodeRowStatusEntry,
       "aRtgPnniTopNodeRowStatus": aRtgPnniTopNodeRowStatus,
       "aRtgPnniTopNodeComponentName": aRtgPnniTopNodeComponentName,
       "aRtgPnniTopNodeStorageType": aRtgPnniTopNodeStorageType,
       "aRtgPnniTopNodeIndex": aRtgPnniTopNodeIndex,
       "aRtgPnniTopNodeAddr": aRtgPnniTopNodeAddr,
       "aRtgPnniTopNodeAddrRowStatusTable": aRtgPnniTopNodeAddrRowStatusTable,
       "aRtgPnniTopNodeAddrRowStatusEntry": aRtgPnniTopNodeAddrRowStatusEntry,
       "aRtgPnniTopNodeAddrRowStatus": aRtgPnniTopNodeAddrRowStatus,
       "aRtgPnniTopNodeAddrComponentName": aRtgPnniTopNodeAddrComponentName,
       "aRtgPnniTopNodeAddrStorageType": aRtgPnniTopNodeAddrStorageType,
       "aRtgPnniTopNodeAddrAddressIndex": aRtgPnniTopNodeAddrAddressIndex,
       "aRtgPnniTopNodeAddrPrefixLengthIndex": aRtgPnniTopNodeAddrPrefixLengthIndex,
       "aRtgPnniTopNodeAddrReachabilityIndex": aRtgPnniTopNodeAddrReachabilityIndex,
       "aRtgPnniTopNodeAddrOperTable": aRtgPnniTopNodeAddrOperTable,
       "aRtgPnniTopNodeAddrOperEntry": aRtgPnniTopNodeAddrOperEntry,
       "aRtgPnniTopNodeAddrScope": aRtgPnniTopNodeAddrScope,
       "aRtgPnniTopNodeLink": aRtgPnniTopNodeLink,
       "aRtgPnniTopNodeLinkRowStatusTable": aRtgPnniTopNodeLinkRowStatusTable,
       "aRtgPnniTopNodeLinkRowStatusEntry": aRtgPnniTopNodeLinkRowStatusEntry,
       "aRtgPnniTopNodeLinkRowStatus": aRtgPnniTopNodeLinkRowStatus,
       "aRtgPnniTopNodeLinkComponentName": aRtgPnniTopNodeLinkComponentName,
       "aRtgPnniTopNodeLinkStorageType": aRtgPnniTopNodeLinkStorageType,
       "aRtgPnniTopNodeLinkIndex": aRtgPnniTopNodeLinkIndex,
       "aRtgPnniTopNodeLinkOperTable": aRtgPnniTopNodeLinkOperTable,
       "aRtgPnniTopNodeLinkOperEntry": aRtgPnniTopNodeLinkOperEntry,
       "aRtgPnniTopNodeLinkRemoteNodeId": aRtgPnniTopNodeLinkRemoteNodeId,
       "aRtgPnniTopNodeLinkRemotePortId": aRtgPnniTopNodeLinkRemotePortId,
       "aRtgPnniTopOperTable": aRtgPnniTopOperTable,
       "aRtgPnniTopOperEntry": aRtgPnniTopOperEntry,
       "aRtgPnniTopPtsesInDatabase": aRtgPnniTopPtsesInDatabase,
       "aRtgPnniTopPglNodeId": aRtgPnniTopPglNodeId,
       "aRtgPnniTopActiveParentNodeId": aRtgPnniTopActiveParentNodeId,
       "aRtgPnniTopPreferredPglNodeId": aRtgPnniTopPreferredPglNodeId,
       "aRtgPnniPort": aRtgPnniPort,
       "aRtgPnniPortRowStatusTable": aRtgPnniPortRowStatusTable,
       "aRtgPnniPortRowStatusEntry": aRtgPnniPortRowStatusEntry,
       "aRtgPnniPortRowStatus": aRtgPnniPortRowStatus,
       "aRtgPnniPortComponentName": aRtgPnniPortComponentName,
       "aRtgPnniPortStorageType": aRtgPnniPortStorageType,
       "aRtgPnniPortIndex": aRtgPnniPortIndex,
       "aRtgPnniPortOperTable": aRtgPnniPortOperTable,
       "aRtgPnniPortOperEntry": aRtgPnniPortOperEntry,
       "aRtgPnniPortStdComponentName": aRtgPnniPortStdComponentName,
       "aRtgPnniProvTable": aRtgPnniProvTable,
       "aRtgPnniProvEntry": aRtgPnniProvEntry,
       "aRtgPnniNodeAddressPrefix": aRtgPnniNodeAddressPrefix,
       "aRtgPnniDefaultScope": aRtgPnniDefaultScope,
       "aRtgPnniDomain": aRtgPnniDomain,
       "aRtgPnniRestrictTransit": aRtgPnniRestrictTransit,
       "aRtgPnniMaxReroutesOnCrankback": aRtgPnniMaxReroutesOnCrankback,
       "aRtgPnniPglParmsTable": aRtgPnniPglParmsTable,
       "aRtgPnniPglParmsEntry": aRtgPnniPglParmsEntry,
       "aRtgPnniPglInitTime": aRtgPnniPglInitTime,
       "aRtgPnniOverrideDelay": aRtgPnniOverrideDelay,
       "aRtgPnniReElectionInterval": aRtgPnniReElectionInterval,
       "aRtgPnniHlParmsTable": aRtgPnniHlParmsTable,
       "aRtgPnniHlParmsEntry": aRtgPnniHlParmsEntry,
       "aRtgPnniHelloHoldDown": aRtgPnniHelloHoldDown,
       "aRtgPnniHelloInterval": aRtgPnniHelloInterval,
       "aRtgPnniHelloInactivityFactor": aRtgPnniHelloInactivityFactor,
       "aRtgPnniPtseParmsTable": aRtgPnniPtseParmsTable,
       "aRtgPnniPtseParmsEntry": aRtgPnniPtseParmsEntry,
       "aRtgPnniPtseHoldDown": aRtgPnniPtseHoldDown,
       "aRtgPnniPtseRefreshInterval": aRtgPnniPtseRefreshInterval,
       "aRtgPnniPtseLifetimeFactor": aRtgPnniPtseLifetimeFactor,
       "aRtgPnniRequestRxmtInterval": aRtgPnniRequestRxmtInterval,
       "aRtgPnniPeerDelayedAckInterval": aRtgPnniPeerDelayedAckInterval,
       "aRtgPnniThreshParmsTable": aRtgPnniThreshParmsTable,
       "aRtgPnniThreshParmsEntry": aRtgPnniThreshParmsEntry,
       "aRtgPnniAvcrMt": aRtgPnniAvcrMt,
       "aRtgPnniAvcrPm": aRtgPnniAvcrPm,
       "aRtgPnniOperTable": aRtgPnniOperTable,
       "aRtgPnniOperEntry": aRtgPnniOperEntry,
       "aRtgPnniTopologyMemoryExhaustion": aRtgPnniTopologyMemoryExhaustion,
       "aRtgPnniStatsTable": aRtgPnniStatsTable,
       "aRtgPnniStatsEntry": aRtgPnniStatsEntry,
       "aRtgPnniRoutingAttempts": aRtgPnniRoutingAttempts,
       "aRtgPnniFailedRoutingAttempts": aRtgPnniFailedRoutingAttempts,
       "aRtgPnniCallsRerouted": aRtgPnniCallsRerouted,
       "aRtgPnniOptMetricTable": aRtgPnniOptMetricTable,
       "aRtgPnniOptMetricEntry": aRtgPnniOptMetricEntry,
       "aRtgPnniOptMetricIndex": aRtgPnniOptMetricIndex,
       "aRtgPnniOptMetricValue": aRtgPnniOptMetricValue,
       "aRtgStatsTable": aRtgStatsTable,
       "aRtgStatsEntry": aRtgStatsEntry,
       "aRtgRoutingAttempts": aRtgRoutingAttempts,
       "aRtgFailedRoutingAttempts": aRtgFailedRoutingAttempts,
       "atmCR": atmCR,
       "atmCRRowStatusTable": atmCRRowStatusTable,
       "atmCRRowStatusEntry": atmCRRowStatusEntry,
       "atmCRRowStatus": atmCRRowStatus,
       "atmCRComponentName": atmCRComponentName,
       "atmCRStorageType": atmCRStorageType,
       "atmCRIndex": atmCRIndex,
       "atmCRDna": atmCRDna,
       "atmCRDnaRowStatusTable": atmCRDnaRowStatusTable,
       "atmCRDnaRowStatusEntry": atmCRDnaRowStatusEntry,
       "atmCRDnaRowStatus": atmCRDnaRowStatus,
       "atmCRDnaComponentName": atmCRDnaComponentName,
       "atmCRDnaStorageType": atmCRDnaStorageType,
       "atmCRDnaIndex": atmCRDnaIndex,
       "atmCRDnaDestinationNameTable": atmCRDnaDestinationNameTable,
       "atmCRDnaDestinationNameEntry": atmCRDnaDestinationNameEntry,
       "atmCRDnaDestinationNameValue": atmCRDnaDestinationNameValue,
       "atmCRProvTable": atmCRProvTable,
       "atmCRProvEntry": atmCRProvEntry,
       "atmCRNodeAddress": atmCRNodeAddress,
       "atmCRStatsTable": atmCRStatsTable,
       "atmCRStatsEntry": atmCRStatsEntry,
       "atmCRCallsRouted": atmCRCallsRouted,
       "atmCRCallsFailed": atmCRCallsFailed,
       "atmIfVpcSrc": atmIfVpcSrc,
       "atmIfVpcSrcRowStatusTable": atmIfVpcSrcRowStatusTable,
       "atmIfVpcSrcRowStatusEntry": atmIfVpcSrcRowStatusEntry,
       "atmIfVpcSrcRowStatus": atmIfVpcSrcRowStatus,
       "atmIfVpcSrcComponentName": atmIfVpcSrcComponentName,
       "atmIfVpcSrcStorageType": atmIfVpcSrcStorageType,
       "atmIfVpcSrcIndex": atmIfVpcSrcIndex,
       "atmIfVpcSrcProvTable": atmIfVpcSrcProvTable,
       "atmIfVpcSrcProvEntry": atmIfVpcSrcProvEntry,
       "atmIfVpcSrcCallingAddress": atmIfVpcSrcCallingAddress,
       "atmIfVpcSrcCalledAddress": atmIfVpcSrcCalledAddress,
       "atmIfVpcSrcCalledVpi": atmIfVpcSrcCalledVpi,
       "atmIfVpcSrcOperTable": atmIfVpcSrcOperTable,
       "atmIfVpcSrcOperEntry": atmIfVpcSrcOperEntry,
       "atmIfVpcSrcState": atmIfVpcSrcState,
       "atmIfVpcSrcRetryCount": atmIfVpcSrcRetryCount,
       "atmIfVpcSrcLastFailureCauseCode": atmIfVpcSrcLastFailureCauseCode,
       "atmIfVpcSrcLastFailureDiagCode": atmIfVpcSrcLastFailureDiagCode,
       "atmIfVpcRp": atmIfVpcRp,
       "atmIfVpcRpRowStatusTable": atmIfVpcRpRowStatusTable,
       "atmIfVpcRpRowStatusEntry": atmIfVpcRpRowStatusEntry,
       "atmIfVpcRpRowStatus": atmIfVpcRpRowStatus,
       "atmIfVpcRpComponentName": atmIfVpcRpComponentName,
       "atmIfVpcRpStorageType": atmIfVpcRpStorageType,
       "atmIfVpcRpIndex": atmIfVpcRpIndex,
       "atmIfVpcRpOperTable": atmIfVpcRpOperTable,
       "atmIfVpcRpOperEntry": atmIfVpcRpOperEntry,
       "atmIfVpcRpNextHop": atmIfVpcRpNextHop,
       "atmIfVpcRpNextHopsTable": atmIfVpcRpNextHopsTable,
       "atmIfVpcRpNextHopsEntry": atmIfVpcRpNextHopsEntry,
       "atmIfVpcRpNextHopsValue": atmIfVpcRpNextHopsValue,
       "atmIfVpcDst": atmIfVpcDst,
       "atmIfVpcDstRowStatusTable": atmIfVpcDstRowStatusTable,
       "atmIfVpcDstRowStatusEntry": atmIfVpcDstRowStatusEntry,
       "atmIfVpcDstRowStatus": atmIfVpcDstRowStatus,
       "atmIfVpcDstComponentName": atmIfVpcDstComponentName,
       "atmIfVpcDstStorageType": atmIfVpcDstStorageType,
       "atmIfVpcDstIndex": atmIfVpcDstIndex,
       "atmIfVpcDstOperTable": atmIfVpcDstOperTable,
       "atmIfVpcDstOperEntry": atmIfVpcDstOperEntry,
       "atmIfVpcDstCalledAddress": atmIfVpcDstCalledAddress,
       "atmIfVpcDstCallingAddress": atmIfVpcDstCallingAddress,
       "atmIfVpcDstCallingVpi": atmIfVpcDstCallingVpi,
       "atmIfVccSrc": atmIfVccSrc,
       "atmIfVccSrcRowStatusTable": atmIfVccSrcRowStatusTable,
       "atmIfVccSrcRowStatusEntry": atmIfVccSrcRowStatusEntry,
       "atmIfVccSrcRowStatus": atmIfVccSrcRowStatus,
       "atmIfVccSrcComponentName": atmIfVccSrcComponentName,
       "atmIfVccSrcStorageType": atmIfVccSrcStorageType,
       "atmIfVccSrcIndex": atmIfVccSrcIndex,
       "atmIfVccSrcProvTable": atmIfVccSrcProvTable,
       "atmIfVccSrcProvEntry": atmIfVccSrcProvEntry,
       "atmIfVccSrcRemoteAddress": atmIfVccSrcRemoteAddress,
       "atmIfVccSrcRemoteVpiVci": atmIfVccSrcRemoteVpiVci,
       "atmIfVccSrcCallingAddress": atmIfVccSrcCallingAddress,
       "atmIfVccSrcCalledAddress": atmIfVccSrcCalledAddress,
       "atmIfVccSrcCalledVpiVci": atmIfVccSrcCalledVpiVci,
       "atmIfVccSrcOperTable": atmIfVccSrcOperTable,
       "atmIfVccSrcOperEntry": atmIfVccSrcOperEntry,
       "atmIfVccSrcState": atmIfVccSrcState,
       "atmIfVccSrcRetryCount": atmIfVccSrcRetryCount,
       "atmIfVccSrcLastFailureCauseCode": atmIfVccSrcLastFailureCauseCode,
       "atmIfVccSrcLastFailureDiagCode": atmIfVccSrcLastFailureDiagCode,
       "atmIfVccEp": atmIfVccEp,
       "atmIfVccEpRowStatusTable": atmIfVccEpRowStatusTable,
       "atmIfVccEpRowStatusEntry": atmIfVccEpRowStatusEntry,
       "atmIfVccEpRowStatus": atmIfVccEpRowStatus,
       "atmIfVccEpComponentName": atmIfVccEpComponentName,
       "atmIfVccEpStorageType": atmIfVccEpStorageType,
       "atmIfVccEpIndex": atmIfVccEpIndex,
       "atmIfVccEpOperTable": atmIfVccEpOperTable,
       "atmIfVccEpOperEntry": atmIfVccEpOperEntry,
       "atmIfVccEpApplicationName": atmIfVccEpApplicationName,
       "atmIfVccRp": atmIfVccRp,
       "atmIfVccRpRowStatusTable": atmIfVccRpRowStatusTable,
       "atmIfVccRpRowStatusEntry": atmIfVccRpRowStatusEntry,
       "atmIfVccRpRowStatus": atmIfVccRpRowStatus,
       "atmIfVccRpComponentName": atmIfVccRpComponentName,
       "atmIfVccRpStorageType": atmIfVccRpStorageType,
       "atmIfVccRpIndex": atmIfVccRpIndex,
       "atmIfVccRpOperTable": atmIfVccRpOperTable,
       "atmIfVccRpOperEntry": atmIfVccRpOperEntry,
       "atmIfVccRpNextHop": atmIfVccRpNextHop,
       "atmIfVccRpNextHopsTable": atmIfVccRpNextHopsTable,
       "atmIfVccRpNextHopsEntry": atmIfVccRpNextHopsEntry,
       "atmIfVccRpNextHopsValue": atmIfVccRpNextHopsValue,
       "atmIfVccDst": atmIfVccDst,
       "atmIfVccDstRowStatusTable": atmIfVccDstRowStatusTable,
       "atmIfVccDstRowStatusEntry": atmIfVccDstRowStatusEntry,
       "atmIfVccDstRowStatus": atmIfVccDstRowStatus,
       "atmIfVccDstComponentName": atmIfVccDstComponentName,
       "atmIfVccDstStorageType": atmIfVccDstStorageType,
       "atmIfVccDstIndex": atmIfVccDstIndex,
       "atmIfVccDstOperTable": atmIfVccDstOperTable,
       "atmIfVccDstOperEntry": atmIfVccDstOperEntry,
       "atmIfVccDstCalledAddress": atmIfVccDstCalledAddress,
       "atmIfVccDstCallingAddress": atmIfVccDstCallingAddress,
       "atmIfVccDstCallingVpiVci": atmIfVccDstCallingVpiVci,
       "atmIfVptVccSrc": atmIfVptVccSrc,
       "atmIfVptVccSrcRowStatusTable": atmIfVptVccSrcRowStatusTable,
       "atmIfVptVccSrcRowStatusEntry": atmIfVptVccSrcRowStatusEntry,
       "atmIfVptVccSrcRowStatus": atmIfVptVccSrcRowStatus,
       "atmIfVptVccSrcComponentName": atmIfVptVccSrcComponentName,
       "atmIfVptVccSrcStorageType": atmIfVptVccSrcStorageType,
       "atmIfVptVccSrcIndex": atmIfVptVccSrcIndex,
       "atmIfVptVccSrcProvTable": atmIfVptVccSrcProvTable,
       "atmIfVptVccSrcProvEntry": atmIfVptVccSrcProvEntry,
       "atmIfVptVccSrcRemoteAddress": atmIfVptVccSrcRemoteAddress,
       "atmIfVptVccSrcRemoteVpiVci": atmIfVptVccSrcRemoteVpiVci,
       "atmIfVptVccSrcCallingAddress": atmIfVptVccSrcCallingAddress,
       "atmIfVptVccSrcCalledAddress": atmIfVptVccSrcCalledAddress,
       "atmIfVptVccSrcCalledVpiVci": atmIfVptVccSrcCalledVpiVci,
       "atmIfVptVccSrcOperTable": atmIfVptVccSrcOperTable,
       "atmIfVptVccSrcOperEntry": atmIfVptVccSrcOperEntry,
       "atmIfVptVccSrcState": atmIfVptVccSrcState,
       "atmIfVptVccSrcRetryCount": atmIfVptVccSrcRetryCount,
       "atmIfVptVccSrcLastFailureCauseCode": atmIfVptVccSrcLastFailureCauseCode,
       "atmIfVptVccSrcLastFailureDiagCode": atmIfVptVccSrcLastFailureDiagCode,
       "atmIfVptVccEp": atmIfVptVccEp,
       "atmIfVptVccEpRowStatusTable": atmIfVptVccEpRowStatusTable,
       "atmIfVptVccEpRowStatusEntry": atmIfVptVccEpRowStatusEntry,
       "atmIfVptVccEpRowStatus": atmIfVptVccEpRowStatus,
       "atmIfVptVccEpComponentName": atmIfVptVccEpComponentName,
       "atmIfVptVccEpStorageType": atmIfVptVccEpStorageType,
       "atmIfVptVccEpIndex": atmIfVptVccEpIndex,
       "atmIfVptVccEpOperTable": atmIfVptVccEpOperTable,
       "atmIfVptVccEpOperEntry": atmIfVptVccEpOperEntry,
       "atmIfVptVccEpApplicationName": atmIfVptVccEpApplicationName,
       "atmIfVptVccRp": atmIfVptVccRp,
       "atmIfVptVccRpRowStatusTable": atmIfVptVccRpRowStatusTable,
       "atmIfVptVccRpRowStatusEntry": atmIfVptVccRpRowStatusEntry,
       "atmIfVptVccRpRowStatus": atmIfVptVccRpRowStatus,
       "atmIfVptVccRpComponentName": atmIfVptVccRpComponentName,
       "atmIfVptVccRpStorageType": atmIfVptVccRpStorageType,
       "atmIfVptVccRpIndex": atmIfVptVccRpIndex,
       "atmIfVptVccRpOperTable": atmIfVptVccRpOperTable,
       "atmIfVptVccRpOperEntry": atmIfVptVccRpOperEntry,
       "atmIfVptVccRpNextHop": atmIfVptVccRpNextHop,
       "atmIfVptVccRpNextHopsTable": atmIfVptVccRpNextHopsTable,
       "atmIfVptVccRpNextHopsEntry": atmIfVptVccRpNextHopsEntry,
       "atmIfVptVccRpNextHopsValue": atmIfVptVccRpNextHopsValue,
       "atmIfVptVccDst": atmIfVptVccDst,
       "atmIfVptVccDstRowStatusTable": atmIfVptVccDstRowStatusTable,
       "atmIfVptVccDstRowStatusEntry": atmIfVptVccDstRowStatusEntry,
       "atmIfVptVccDstRowStatus": atmIfVptVccDstRowStatus,
       "atmIfVptVccDstComponentName": atmIfVptVccDstComponentName,
       "atmIfVptVccDstStorageType": atmIfVptVccDstStorageType,
       "atmIfVptVccDstIndex": atmIfVptVccDstIndex,
       "atmIfVptVccDstOperTable": atmIfVptVccDstOperTable,
       "atmIfVptVccDstOperEntry": atmIfVptVccDstOperEntry,
       "atmIfVptVccDstCalledAddress": atmIfVptVccDstCalledAddress,
       "atmIfVptVccDstCallingAddress": atmIfVptVccDstCallingAddress,
       "atmIfVptVccDstCallingVpiVci": atmIfVptVccDstCallingVpiVci,
       "atmNetworkingMIB": atmNetworkingMIB,
       "atmNetworkingGroup": atmNetworkingGroup,
       "atmNetworkingGroupBE": atmNetworkingGroupBE,
       "atmNetworkingGroupBE01": atmNetworkingGroupBE01,
       "atmNetworkingGroupBE01A": atmNetworkingGroupBE01A,
       "atmNetworkingCapabilities": atmNetworkingCapabilities,
       "atmNetworkingCapabilitiesBE": atmNetworkingCapabilitiesBE,
       "atmNetworkingCapabilitiesBE01": atmNetworkingCapabilitiesBE01,
       "atmNetworkingCapabilitiesBE01A": atmNetworkingCapabilitiesBE01A}
)
