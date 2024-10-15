# SNMP MIB module (Nortel-MsCarrier-MscPassport-AtmNetworkingMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-MsCarrier-MscPassport-AtmNetworkingMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:31:51 2024
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

(mscAtmIfIndex,
 mscAtmIfVcc,
 mscAtmIfVccIndex,
 mscAtmIfVpc,
 mscAtmIfVpcIndex,
 mscAtmIfVptIndex,
 mscAtmIfVptVcc,
 mscAtmIfVptVccIndex) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-AtmCoreMIB",
    "mscAtmIfIndex",
    "mscAtmIfVcc",
    "mscAtmIfVccIndex",
    "mscAtmIfVpc",
    "mscAtmIfVpcIndex",
    "mscAtmIfVptIndex",
    "mscAtmIfVptVcc",
    "mscAtmIfVptVccIndex")

(Counter32,
 DisplayString,
 Gauge32,
 Integer32,
 RowPointer,
 RowStatus,
 StorageType,
 Unsigned32) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-StandardTextualConventionsMIB",
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
    "Nortel-MsCarrier-MscPassport-TextualConventionsMIB",
    "AsciiString",
    "AsciiStringIndex",
    "FixedPoint1",
    "HexString",
    "IntegerSequence",
    "NonReplicated")

(mscComponents,
 mscPassportMIBs) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-UsefulDefinitionsMIB",
    "mscComponents",
    "mscPassportMIBs")

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

_MscARtg_ObjectIdentity = ObjectIdentity
mscARtg = _MscARtg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95)
)
_MscARtgRowStatusTable_Object = MibTable
mscARtgRowStatusTable = _MscARtgRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 1)
)
if mibBuilder.loadTexts:
    mscARtgRowStatusTable.setStatus("mandatory")
_MscARtgRowStatusEntry_Object = MibTableRow
mscARtgRowStatusEntry = _MscARtgRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 1, 1)
)
mscARtgRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscARtgIndex"),
)
if mibBuilder.loadTexts:
    mscARtgRowStatusEntry.setStatus("mandatory")
_MscARtgRowStatus_Type = RowStatus
_MscARtgRowStatus_Object = MibTableColumn
mscARtgRowStatus = _MscARtgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 1, 1, 1),
    _MscARtgRowStatus_Type()
)
mscARtgRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscARtgRowStatus.setStatus("mandatory")
_MscARtgComponentName_Type = DisplayString
_MscARtgComponentName_Object = MibTableColumn
mscARtgComponentName = _MscARtgComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 1, 1, 2),
    _MscARtgComponentName_Type()
)
mscARtgComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscARtgComponentName.setStatus("mandatory")
_MscARtgStorageType_Type = StorageType
_MscARtgStorageType_Object = MibTableColumn
mscARtgStorageType = _MscARtgStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 1, 1, 4),
    _MscARtgStorageType_Type()
)
mscARtgStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscARtgStorageType.setStatus("mandatory")
_MscARtgIndex_Type = NonReplicated
_MscARtgIndex_Object = MibTableColumn
mscARtgIndex = _MscARtgIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 1, 1, 10),
    _MscARtgIndex_Type()
)
mscARtgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscARtgIndex.setStatus("mandatory")
_MscARtgDna_ObjectIdentity = ObjectIdentity
mscARtgDna = _MscARtgDna_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 2)
)
_MscARtgDnaRowStatusTable_Object = MibTable
mscARtgDnaRowStatusTable = _MscARtgDnaRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 2, 1)
)
if mibBuilder.loadTexts:
    mscARtgDnaRowStatusTable.setStatus("mandatory")
_MscARtgDnaRowStatusEntry_Object = MibTableRow
mscARtgDnaRowStatusEntry = _MscARtgDnaRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 2, 1, 1)
)
mscARtgDnaRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscARtgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscARtgDnaIndex"),
)
if mibBuilder.loadTexts:
    mscARtgDnaRowStatusEntry.setStatus("mandatory")
_MscARtgDnaRowStatus_Type = RowStatus
_MscARtgDnaRowStatus_Object = MibTableColumn
mscARtgDnaRowStatus = _MscARtgDnaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 2, 1, 1, 1),
    _MscARtgDnaRowStatus_Type()
)
mscARtgDnaRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscARtgDnaRowStatus.setStatus("mandatory")
_MscARtgDnaComponentName_Type = DisplayString
_MscARtgDnaComponentName_Object = MibTableColumn
mscARtgDnaComponentName = _MscARtgDnaComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 2, 1, 1, 2),
    _MscARtgDnaComponentName_Type()
)
mscARtgDnaComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscARtgDnaComponentName.setStatus("mandatory")
_MscARtgDnaStorageType_Type = StorageType
_MscARtgDnaStorageType_Object = MibTableColumn
mscARtgDnaStorageType = _MscARtgDnaStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 2, 1, 1, 4),
    _MscARtgDnaStorageType_Type()
)
mscARtgDnaStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscARtgDnaStorageType.setStatus("mandatory")


class _MscARtgDnaIndex_Type(AsciiStringIndex):
    """Custom type mscARtgDnaIndex based on AsciiStringIndex"""
    subtypeSpec = AsciiStringIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_MscARtgDnaIndex_Type.__name__ = "AsciiStringIndex"
_MscARtgDnaIndex_Object = MibTableColumn
mscARtgDnaIndex = _MscARtgDnaIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 2, 1, 1, 10),
    _MscARtgDnaIndex_Type()
)
mscARtgDnaIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscARtgDnaIndex.setStatus("mandatory")
_MscARtgDnaDestInfo_ObjectIdentity = ObjectIdentity
mscARtgDnaDestInfo = _MscARtgDnaDestInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 2, 2)
)
_MscARtgDnaDestInfoRowStatusTable_Object = MibTable
mscARtgDnaDestInfoRowStatusTable = _MscARtgDnaDestInfoRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 2, 2, 1)
)
if mibBuilder.loadTexts:
    mscARtgDnaDestInfoRowStatusTable.setStatus("mandatory")
_MscARtgDnaDestInfoRowStatusEntry_Object = MibTableRow
mscARtgDnaDestInfoRowStatusEntry = _MscARtgDnaDestInfoRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 2, 2, 1, 1)
)
mscARtgDnaDestInfoRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscARtgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscARtgDnaIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscARtgDnaDestInfoIndex"),
)
if mibBuilder.loadTexts:
    mscARtgDnaDestInfoRowStatusEntry.setStatus("mandatory")
_MscARtgDnaDestInfoRowStatus_Type = RowStatus
_MscARtgDnaDestInfoRowStatus_Object = MibTableColumn
mscARtgDnaDestInfoRowStatus = _MscARtgDnaDestInfoRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 2, 2, 1, 1, 1),
    _MscARtgDnaDestInfoRowStatus_Type()
)
mscARtgDnaDestInfoRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscARtgDnaDestInfoRowStatus.setStatus("mandatory")
_MscARtgDnaDestInfoComponentName_Type = DisplayString
_MscARtgDnaDestInfoComponentName_Object = MibTableColumn
mscARtgDnaDestInfoComponentName = _MscARtgDnaDestInfoComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 2, 2, 1, 1, 2),
    _MscARtgDnaDestInfoComponentName_Type()
)
mscARtgDnaDestInfoComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscARtgDnaDestInfoComponentName.setStatus("mandatory")
_MscARtgDnaDestInfoStorageType_Type = StorageType
_MscARtgDnaDestInfoStorageType_Object = MibTableColumn
mscARtgDnaDestInfoStorageType = _MscARtgDnaDestInfoStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 2, 2, 1, 1, 4),
    _MscARtgDnaDestInfoStorageType_Type()
)
mscARtgDnaDestInfoStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscARtgDnaDestInfoStorageType.setStatus("mandatory")


class _MscARtgDnaDestInfoIndex_Type(Integer32):
    """Custom type mscARtgDnaDestInfoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50),
    )


_MscARtgDnaDestInfoIndex_Type.__name__ = "Integer32"
_MscARtgDnaDestInfoIndex_Object = MibTableColumn
mscARtgDnaDestInfoIndex = _MscARtgDnaDestInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 2, 2, 1, 1, 10),
    _MscARtgDnaDestInfoIndex_Type()
)
mscARtgDnaDestInfoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscARtgDnaDestInfoIndex.setStatus("mandatory")
_MscARtgDnaDestInfoOperTable_Object = MibTable
mscARtgDnaDestInfoOperTable = _MscARtgDnaDestInfoOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 2, 2, 10)
)
if mibBuilder.loadTexts:
    mscARtgDnaDestInfoOperTable.setStatus("mandatory")
_MscARtgDnaDestInfoOperEntry_Object = MibTableRow
mscARtgDnaDestInfoOperEntry = _MscARtgDnaDestInfoOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 2, 2, 10, 1)
)
mscARtgDnaDestInfoOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscARtgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscARtgDnaIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscARtgDnaDestInfoIndex"),
)
if mibBuilder.loadTexts:
    mscARtgDnaDestInfoOperEntry.setStatus("mandatory")


class _MscARtgDnaDestInfoType_Type(Integer32):
    """Custom type mscARtgDnaDestInfoType based on Integer32"""
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
        *(("alternate", 1),
          ("default", 3),
          ("ebr", 4),
          ("primary", 0),
          ("registered", 2))
    )


_MscARtgDnaDestInfoType_Type.__name__ = "Integer32"
_MscARtgDnaDestInfoType_Object = MibTableColumn
mscARtgDnaDestInfoType = _MscARtgDnaDestInfoType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 2, 2, 10, 1, 1),
    _MscARtgDnaDestInfoType_Type()
)
mscARtgDnaDestInfoType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscARtgDnaDestInfoType.setStatus("mandatory")


class _MscARtgDnaDestInfoScope_Type(Integer32):
    """Custom type mscARtgDnaDestInfoScope based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 104),
    )


_MscARtgDnaDestInfoScope_Type.__name__ = "Integer32"
_MscARtgDnaDestInfoScope_Object = MibTableColumn
mscARtgDnaDestInfoScope = _MscARtgDnaDestInfoScope_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 2, 2, 10, 1, 2),
    _MscARtgDnaDestInfoScope_Type()
)
mscARtgDnaDestInfoScope.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscARtgDnaDestInfoScope.setStatus("mandatory")
_MscARtgDnaDestInfoStdComponentName_Type = RowPointer
_MscARtgDnaDestInfoStdComponentName_Object = MibTableColumn
mscARtgDnaDestInfoStdComponentName = _MscARtgDnaDestInfoStdComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 2, 2, 10, 1, 3),
    _MscARtgDnaDestInfoStdComponentName_Type()
)
mscARtgDnaDestInfoStdComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscARtgDnaDestInfoStdComponentName.setStatus("mandatory")


class _MscARtgDnaDestInfoReachability_Type(Integer32):
    """Custom type mscARtgDnaDestInfoReachability based on Integer32"""
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


_MscARtgDnaDestInfoReachability_Type.__name__ = "Integer32"
_MscARtgDnaDestInfoReachability_Object = MibTableColumn
mscARtgDnaDestInfoReachability = _MscARtgDnaDestInfoReachability_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 2, 2, 10, 1, 4),
    _MscARtgDnaDestInfoReachability_Type()
)
mscARtgDnaDestInfoReachability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscARtgDnaDestInfoReachability.setStatus("mandatory")
_MscARtgPnni_ObjectIdentity = ObjectIdentity
mscARtgPnni = _MscARtgPnni_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3)
)
_MscARtgPnniRowStatusTable_Object = MibTable
mscARtgPnniRowStatusTable = _MscARtgPnniRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 1)
)
if mibBuilder.loadTexts:
    mscARtgPnniRowStatusTable.setStatus("mandatory")
_MscARtgPnniRowStatusEntry_Object = MibTableRow
mscARtgPnniRowStatusEntry = _MscARtgPnniRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 1, 1)
)
mscARtgPnniRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscARtgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscARtgPnniIndex"),
)
if mibBuilder.loadTexts:
    mscARtgPnniRowStatusEntry.setStatus("mandatory")
_MscARtgPnniRowStatus_Type = RowStatus
_MscARtgPnniRowStatus_Object = MibTableColumn
mscARtgPnniRowStatus = _MscARtgPnniRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 1, 1, 1),
    _MscARtgPnniRowStatus_Type()
)
mscARtgPnniRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscARtgPnniRowStatus.setStatus("mandatory")
_MscARtgPnniComponentName_Type = DisplayString
_MscARtgPnniComponentName_Object = MibTableColumn
mscARtgPnniComponentName = _MscARtgPnniComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 1, 1, 2),
    _MscARtgPnniComponentName_Type()
)
mscARtgPnniComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscARtgPnniComponentName.setStatus("mandatory")
_MscARtgPnniStorageType_Type = StorageType
_MscARtgPnniStorageType_Object = MibTableColumn
mscARtgPnniStorageType = _MscARtgPnniStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 1, 1, 4),
    _MscARtgPnniStorageType_Type()
)
mscARtgPnniStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscARtgPnniStorageType.setStatus("mandatory")
_MscARtgPnniIndex_Type = NonReplicated
_MscARtgPnniIndex_Object = MibTableColumn
mscARtgPnniIndex = _MscARtgPnniIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 1, 1, 10),
    _MscARtgPnniIndex_Type()
)
mscARtgPnniIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscARtgPnniIndex.setStatus("mandatory")
_MscARtgPnniRf_ObjectIdentity = ObjectIdentity
mscARtgPnniRf = _MscARtgPnniRf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 2)
)
_MscARtgPnniRfRowStatusTable_Object = MibTable
mscARtgPnniRfRowStatusTable = _MscARtgPnniRfRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 2, 1)
)
if mibBuilder.loadTexts:
    mscARtgPnniRfRowStatusTable.setStatus("mandatory")
_MscARtgPnniRfRowStatusEntry_Object = MibTableRow
mscARtgPnniRfRowStatusEntry = _MscARtgPnniRfRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 2, 1, 1)
)
mscARtgPnniRfRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscARtgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscARtgPnniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscARtgPnniRfIndex"),
)
if mibBuilder.loadTexts:
    mscARtgPnniRfRowStatusEntry.setStatus("mandatory")
_MscARtgPnniRfRowStatus_Type = RowStatus
_MscARtgPnniRfRowStatus_Object = MibTableColumn
mscARtgPnniRfRowStatus = _MscARtgPnniRfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 2, 1, 1, 1),
    _MscARtgPnniRfRowStatus_Type()
)
mscARtgPnniRfRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscARtgPnniRfRowStatus.setStatus("mandatory")
_MscARtgPnniRfComponentName_Type = DisplayString
_MscARtgPnniRfComponentName_Object = MibTableColumn
mscARtgPnniRfComponentName = _MscARtgPnniRfComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 2, 1, 1, 2),
    _MscARtgPnniRfComponentName_Type()
)
mscARtgPnniRfComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscARtgPnniRfComponentName.setStatus("mandatory")
_MscARtgPnniRfStorageType_Type = StorageType
_MscARtgPnniRfStorageType_Object = MibTableColumn
mscARtgPnniRfStorageType = _MscARtgPnniRfStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 2, 1, 1, 4),
    _MscARtgPnniRfStorageType_Type()
)
mscARtgPnniRfStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscARtgPnniRfStorageType.setStatus("mandatory")
_MscARtgPnniRfIndex_Type = NonReplicated
_MscARtgPnniRfIndex_Object = MibTableColumn
mscARtgPnniRfIndex = _MscARtgPnniRfIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 2, 1, 1, 10),
    _MscARtgPnniRfIndex_Type()
)
mscARtgPnniRfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscARtgPnniRfIndex.setStatus("mandatory")
_MscARtgPnniRfCriteriaTable_Object = MibTable
mscARtgPnniRfCriteriaTable = _MscARtgPnniRfCriteriaTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 2, 10)
)
if mibBuilder.loadTexts:
    mscARtgPnniRfCriteriaTable.setStatus("mandatory")
_MscARtgPnniRfCriteriaEntry_Object = MibTableRow
mscARtgPnniRfCriteriaEntry = _MscARtgPnniRfCriteriaEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 2, 10, 1)
)
mscARtgPnniRfCriteriaEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscARtgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscARtgPnniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscARtgPnniRfIndex"),
)
if mibBuilder.loadTexts:
    mscARtgPnniRfCriteriaEntry.setStatus("mandatory")


class _MscARtgPnniRfDestinationAddress_Type(HexString):
    """Custom type mscARtgPnniRfDestinationAddress based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_MscARtgPnniRfDestinationAddress_Type.__name__ = "HexString"
_MscARtgPnniRfDestinationAddress_Object = MibTableColumn
mscARtgPnniRfDestinationAddress = _MscARtgPnniRfDestinationAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 2, 10, 1, 1),
    _MscARtgPnniRfDestinationAddress_Type()
)
mscARtgPnniRfDestinationAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscARtgPnniRfDestinationAddress.setStatus("mandatory")


class _MscARtgPnniRfMaxRoutes_Type(Unsigned32):
    """Custom type mscARtgPnniRfMaxRoutes based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_MscARtgPnniRfMaxRoutes_Type.__name__ = "Unsigned32"
_MscARtgPnniRfMaxRoutes_Object = MibTableColumn
mscARtgPnniRfMaxRoutes = _MscARtgPnniRfMaxRoutes_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 2, 10, 1, 2),
    _MscARtgPnniRfMaxRoutes_Type()
)
mscARtgPnniRfMaxRoutes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscARtgPnniRfMaxRoutes.setStatus("mandatory")


class _MscARtgPnniRfTxTrafficDescType_Type(Integer32):
    """Custom type mscARtgPnniRfTxTrafficDescType based on Integer32"""
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


_MscARtgPnniRfTxTrafficDescType_Type.__name__ = "Integer32"
_MscARtgPnniRfTxTrafficDescType_Object = MibTableColumn
mscARtgPnniRfTxTrafficDescType = _MscARtgPnniRfTxTrafficDescType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 2, 10, 1, 3),
    _MscARtgPnniRfTxTrafficDescType_Type()
)
mscARtgPnniRfTxTrafficDescType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscARtgPnniRfTxTrafficDescType.setStatus("mandatory")


class _MscARtgPnniRfRxTrafficDescType_Type(Integer32):
    """Custom type mscARtgPnniRfRxTrafficDescType based on Integer32"""
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


_MscARtgPnniRfRxTrafficDescType_Type.__name__ = "Integer32"
_MscARtgPnniRfRxTrafficDescType_Object = MibTableColumn
mscARtgPnniRfRxTrafficDescType = _MscARtgPnniRfRxTrafficDescType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 2, 10, 1, 5),
    _MscARtgPnniRfRxTrafficDescType_Type()
)
mscARtgPnniRfRxTrafficDescType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscARtgPnniRfRxTrafficDescType.setStatus("mandatory")


class _MscARtgPnniRfAtmServiceCategory_Type(Integer32):
    """Custom type mscARtgPnniRfAtmServiceCategory based on Integer32"""
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


_MscARtgPnniRfAtmServiceCategory_Type.__name__ = "Integer32"
_MscARtgPnniRfAtmServiceCategory_Object = MibTableColumn
mscARtgPnniRfAtmServiceCategory = _MscARtgPnniRfAtmServiceCategory_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 2, 10, 1, 6),
    _MscARtgPnniRfAtmServiceCategory_Type()
)
mscARtgPnniRfAtmServiceCategory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscARtgPnniRfAtmServiceCategory.setStatus("mandatory")


class _MscARtgPnniRfFwdQosClass_Type(Integer32):
    """Custom type mscARtgPnniRfFwdQosClass based on Integer32"""
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


_MscARtgPnniRfFwdQosClass_Type.__name__ = "Integer32"
_MscARtgPnniRfFwdQosClass_Object = MibTableColumn
mscARtgPnniRfFwdQosClass = _MscARtgPnniRfFwdQosClass_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 2, 10, 1, 10),
    _MscARtgPnniRfFwdQosClass_Type()
)
mscARtgPnniRfFwdQosClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscARtgPnniRfFwdQosClass.setStatus("mandatory")


class _MscARtgPnniRfBwdQosClass_Type(Integer32):
    """Custom type mscARtgPnniRfBwdQosClass based on Integer32"""
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


_MscARtgPnniRfBwdQosClass_Type.__name__ = "Integer32"
_MscARtgPnniRfBwdQosClass_Object = MibTableColumn
mscARtgPnniRfBwdQosClass = _MscARtgPnniRfBwdQosClass_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 2, 10, 1, 11),
    _MscARtgPnniRfBwdQosClass_Type()
)
mscARtgPnniRfBwdQosClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscARtgPnniRfBwdQosClass.setStatus("mandatory")


class _MscARtgPnniRfBearerClassBbc_Type(Integer32):
    """Custom type mscARtgPnniRfBearerClassBbc based on Integer32"""
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


_MscARtgPnniRfBearerClassBbc_Type.__name__ = "Integer32"
_MscARtgPnniRfBearerClassBbc_Object = MibTableColumn
mscARtgPnniRfBearerClassBbc = _MscARtgPnniRfBearerClassBbc_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 2, 10, 1, 12),
    _MscARtgPnniRfBearerClassBbc_Type()
)
mscARtgPnniRfBearerClassBbc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscARtgPnniRfBearerClassBbc.setStatus("mandatory")


class _MscARtgPnniRfTransferCapabilityBbc_Type(Integer32):
    """Custom type mscARtgPnniRfTransferCapabilityBbc based on Integer32"""
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


_MscARtgPnniRfTransferCapabilityBbc_Type.__name__ = "Integer32"
_MscARtgPnniRfTransferCapabilityBbc_Object = MibTableColumn
mscARtgPnniRfTransferCapabilityBbc = _MscARtgPnniRfTransferCapabilityBbc_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 2, 10, 1, 13),
    _MscARtgPnniRfTransferCapabilityBbc_Type()
)
mscARtgPnniRfTransferCapabilityBbc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscARtgPnniRfTransferCapabilityBbc.setStatus("mandatory")


class _MscARtgPnniRfClippingBbc_Type(Integer32):
    """Custom type mscARtgPnniRfClippingBbc based on Integer32"""
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


_MscARtgPnniRfClippingBbc_Type.__name__ = "Integer32"
_MscARtgPnniRfClippingBbc_Object = MibTableColumn
mscARtgPnniRfClippingBbc = _MscARtgPnniRfClippingBbc_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 2, 10, 1, 14),
    _MscARtgPnniRfClippingBbc_Type()
)
mscARtgPnniRfClippingBbc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscARtgPnniRfClippingBbc.setStatus("mandatory")


class _MscARtgPnniRfBestEffort_Type(Integer32):
    """Custom type mscARtgPnniRfBestEffort based on Integer32"""
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


_MscARtgPnniRfBestEffort_Type.__name__ = "Integer32"
_MscARtgPnniRfBestEffort_Object = MibTableColumn
mscARtgPnniRfBestEffort = _MscARtgPnniRfBestEffort_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 2, 10, 1, 15),
    _MscARtgPnniRfBestEffort_Type()
)
mscARtgPnniRfBestEffort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscARtgPnniRfBestEffort.setStatus("mandatory")


class _MscARtgPnniRfOptimizationMetric_Type(Integer32):
    """Custom type mscARtgPnniRfOptimizationMetric based on Integer32"""
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


_MscARtgPnniRfOptimizationMetric_Type.__name__ = "Integer32"
_MscARtgPnniRfOptimizationMetric_Object = MibTableColumn
mscARtgPnniRfOptimizationMetric = _MscARtgPnniRfOptimizationMetric_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 2, 10, 1, 16),
    _MscARtgPnniRfOptimizationMetric_Type()
)
mscARtgPnniRfOptimizationMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscARtgPnniRfOptimizationMetric.setStatus("mandatory")
_MscARtgPnniRfRxTdpTable_Object = MibTable
mscARtgPnniRfRxTdpTable = _MscARtgPnniRfRxTdpTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 2, 388)
)
if mibBuilder.loadTexts:
    mscARtgPnniRfRxTdpTable.setStatus("mandatory")
_MscARtgPnniRfRxTdpEntry_Object = MibTableRow
mscARtgPnniRfRxTdpEntry = _MscARtgPnniRfRxTdpEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 2, 388, 1)
)
mscARtgPnniRfRxTdpEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscARtgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscARtgPnniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscARtgPnniRfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscARtgPnniRfRxTdpIndex"),
)
if mibBuilder.loadTexts:
    mscARtgPnniRfRxTdpEntry.setStatus("mandatory")


class _MscARtgPnniRfRxTdpIndex_Type(Integer32):
    """Custom type mscARtgPnniRfRxTdpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_MscARtgPnniRfRxTdpIndex_Type.__name__ = "Integer32"
_MscARtgPnniRfRxTdpIndex_Object = MibTableColumn
mscARtgPnniRfRxTdpIndex = _MscARtgPnniRfRxTdpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 2, 388, 1, 1),
    _MscARtgPnniRfRxTdpIndex_Type()
)
mscARtgPnniRfRxTdpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscARtgPnniRfRxTdpIndex.setStatus("mandatory")


class _MscARtgPnniRfRxTdpValue_Type(Unsigned32):
    """Custom type mscARtgPnniRfRxTdpValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MscARtgPnniRfRxTdpValue_Type.__name__ = "Unsigned32"
_MscARtgPnniRfRxTdpValue_Object = MibTableColumn
mscARtgPnniRfRxTdpValue = _MscARtgPnniRfRxTdpValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 2, 388, 1, 2),
    _MscARtgPnniRfRxTdpValue_Type()
)
mscARtgPnniRfRxTdpValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscARtgPnniRfRxTdpValue.setStatus("mandatory")
_MscARtgPnniRfTxTdpTable_Object = MibTable
mscARtgPnniRfTxTdpTable = _MscARtgPnniRfTxTdpTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 2, 389)
)
if mibBuilder.loadTexts:
    mscARtgPnniRfTxTdpTable.setStatus("mandatory")
_MscARtgPnniRfTxTdpEntry_Object = MibTableRow
mscARtgPnniRfTxTdpEntry = _MscARtgPnniRfTxTdpEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 2, 389, 1)
)
mscARtgPnniRfTxTdpEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscARtgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscARtgPnniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscARtgPnniRfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscARtgPnniRfTxTdpIndex"),
)
if mibBuilder.loadTexts:
    mscARtgPnniRfTxTdpEntry.setStatus("mandatory")


class _MscARtgPnniRfTxTdpIndex_Type(Integer32):
    """Custom type mscARtgPnniRfTxTdpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_MscARtgPnniRfTxTdpIndex_Type.__name__ = "Integer32"
_MscARtgPnniRfTxTdpIndex_Object = MibTableColumn
mscARtgPnniRfTxTdpIndex = _MscARtgPnniRfTxTdpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 2, 389, 1, 1),
    _MscARtgPnniRfTxTdpIndex_Type()
)
mscARtgPnniRfTxTdpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscARtgPnniRfTxTdpIndex.setStatus("mandatory")


class _MscARtgPnniRfTxTdpValue_Type(Unsigned32):
    """Custom type mscARtgPnniRfTxTdpValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MscARtgPnniRfTxTdpValue_Type.__name__ = "Unsigned32"
_MscARtgPnniRfTxTdpValue_Object = MibTableColumn
mscARtgPnniRfTxTdpValue = _MscARtgPnniRfTxTdpValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 2, 389, 1, 2),
    _MscARtgPnniRfTxTdpValue_Type()
)
mscARtgPnniRfTxTdpValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscARtgPnniRfTxTdpValue.setStatus("mandatory")
_MscARtgPnniRfFqpTable_Object = MibTable
mscARtgPnniRfFqpTable = _MscARtgPnniRfFqpTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 2, 390)
)
if mibBuilder.loadTexts:
    mscARtgPnniRfFqpTable.setStatus("mandatory")
_MscARtgPnniRfFqpEntry_Object = MibTableRow
mscARtgPnniRfFqpEntry = _MscARtgPnniRfFqpEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 2, 390, 1)
)
mscARtgPnniRfFqpEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscARtgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscARtgPnniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscARtgPnniRfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscARtgPnniRfFqpIndex"),
)
if mibBuilder.loadTexts:
    mscARtgPnniRfFqpEntry.setStatus("mandatory")


class _MscARtgPnniRfFqpIndex_Type(Integer32):
    """Custom type mscARtgPnniRfFqpIndex based on Integer32"""
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


_MscARtgPnniRfFqpIndex_Type.__name__ = "Integer32"
_MscARtgPnniRfFqpIndex_Object = MibTableColumn
mscARtgPnniRfFqpIndex = _MscARtgPnniRfFqpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 2, 390, 1, 1),
    _MscARtgPnniRfFqpIndex_Type()
)
mscARtgPnniRfFqpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscARtgPnniRfFqpIndex.setStatus("mandatory")


class _MscARtgPnniRfFqpValue_Type(Unsigned32):
    """Custom type mscARtgPnniRfFqpValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MscARtgPnniRfFqpValue_Type.__name__ = "Unsigned32"
_MscARtgPnniRfFqpValue_Object = MibTableColumn
mscARtgPnniRfFqpValue = _MscARtgPnniRfFqpValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 2, 390, 1, 2),
    _MscARtgPnniRfFqpValue_Type()
)
mscARtgPnniRfFqpValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscARtgPnniRfFqpValue.setStatus("mandatory")
_MscARtgPnniRfBqpTable_Object = MibTable
mscARtgPnniRfBqpTable = _MscARtgPnniRfBqpTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 2, 393)
)
if mibBuilder.loadTexts:
    mscARtgPnniRfBqpTable.setStatus("mandatory")
_MscARtgPnniRfBqpEntry_Object = MibTableRow
mscARtgPnniRfBqpEntry = _MscARtgPnniRfBqpEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 2, 393, 1)
)
mscARtgPnniRfBqpEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscARtgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscARtgPnniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscARtgPnniRfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscARtgPnniRfBqpIndex"),
)
if mibBuilder.loadTexts:
    mscARtgPnniRfBqpEntry.setStatus("mandatory")


class _MscARtgPnniRfBqpIndex_Type(Integer32):
    """Custom type mscARtgPnniRfBqpIndex based on Integer32"""
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


_MscARtgPnniRfBqpIndex_Type.__name__ = "Integer32"
_MscARtgPnniRfBqpIndex_Object = MibTableColumn
mscARtgPnniRfBqpIndex = _MscARtgPnniRfBqpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 2, 393, 1, 1),
    _MscARtgPnniRfBqpIndex_Type()
)
mscARtgPnniRfBqpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscARtgPnniRfBqpIndex.setStatus("mandatory")


class _MscARtgPnniRfBqpValue_Type(Unsigned32):
    """Custom type mscARtgPnniRfBqpValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MscARtgPnniRfBqpValue_Type.__name__ = "Unsigned32"
_MscARtgPnniRfBqpValue_Object = MibTableColumn
mscARtgPnniRfBqpValue = _MscARtgPnniRfBqpValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 2, 393, 1, 2),
    _MscARtgPnniRfBqpValue_Type()
)
mscARtgPnniRfBqpValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscARtgPnniRfBqpValue.setStatus("mandatory")
_MscARtgPnniCfgNode_ObjectIdentity = ObjectIdentity
mscARtgPnniCfgNode = _MscARtgPnniCfgNode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 3)
)
_MscARtgPnniCfgNodeRowStatusTable_Object = MibTable
mscARtgPnniCfgNodeRowStatusTable = _MscARtgPnniCfgNodeRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 3, 1)
)
if mibBuilder.loadTexts:
    mscARtgPnniCfgNodeRowStatusTable.setStatus("mandatory")
_MscARtgPnniCfgNodeRowStatusEntry_Object = MibTableRow
mscARtgPnniCfgNodeRowStatusEntry = _MscARtgPnniCfgNodeRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 3, 1, 1)
)
mscARtgPnniCfgNodeRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscARtgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscARtgPnniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscARtgPnniCfgNodeIndex"),
)
if mibBuilder.loadTexts:
    mscARtgPnniCfgNodeRowStatusEntry.setStatus("mandatory")
_MscARtgPnniCfgNodeRowStatus_Type = RowStatus
_MscARtgPnniCfgNodeRowStatus_Object = MibTableColumn
mscARtgPnniCfgNodeRowStatus = _MscARtgPnniCfgNodeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 3, 1, 1, 1),
    _MscARtgPnniCfgNodeRowStatus_Type()
)
mscARtgPnniCfgNodeRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscARtgPnniCfgNodeRowStatus.setStatus("mandatory")
_MscARtgPnniCfgNodeComponentName_Type = DisplayString
_MscARtgPnniCfgNodeComponentName_Object = MibTableColumn
mscARtgPnniCfgNodeComponentName = _MscARtgPnniCfgNodeComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 3, 1, 1, 2),
    _MscARtgPnniCfgNodeComponentName_Type()
)
mscARtgPnniCfgNodeComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscARtgPnniCfgNodeComponentName.setStatus("mandatory")
_MscARtgPnniCfgNodeStorageType_Type = StorageType
_MscARtgPnniCfgNodeStorageType_Object = MibTableColumn
mscARtgPnniCfgNodeStorageType = _MscARtgPnniCfgNodeStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 3, 1, 1, 4),
    _MscARtgPnniCfgNodeStorageType_Type()
)
mscARtgPnniCfgNodeStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscARtgPnniCfgNodeStorageType.setStatus("mandatory")


class _MscARtgPnniCfgNodeIndex_Type(Integer32):
    """Custom type mscARtgPnniCfgNodeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 104),
    )


_MscARtgPnniCfgNodeIndex_Type.__name__ = "Integer32"
_MscARtgPnniCfgNodeIndex_Object = MibTableColumn
mscARtgPnniCfgNodeIndex = _MscARtgPnniCfgNodeIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 3, 1, 1, 10),
    _MscARtgPnniCfgNodeIndex_Type()
)
mscARtgPnniCfgNodeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscARtgPnniCfgNodeIndex.setStatus("mandatory")
_MscARtgPnniCfgNodeSAddr_ObjectIdentity = ObjectIdentity
mscARtgPnniCfgNodeSAddr = _MscARtgPnniCfgNodeSAddr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 3, 2)
)
_MscARtgPnniCfgNodeSAddrRowStatusTable_Object = MibTable
mscARtgPnniCfgNodeSAddrRowStatusTable = _MscARtgPnniCfgNodeSAddrRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 3, 2, 1)
)
if mibBuilder.loadTexts:
    mscARtgPnniCfgNodeSAddrRowStatusTable.setStatus("mandatory")
_MscARtgPnniCfgNodeSAddrRowStatusEntry_Object = MibTableRow
mscARtgPnniCfgNodeSAddrRowStatusEntry = _MscARtgPnniCfgNodeSAddrRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 3, 2, 1, 1)
)
mscARtgPnniCfgNodeSAddrRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscARtgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscARtgPnniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscARtgPnniCfgNodeIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscARtgPnniCfgNodeSAddrAddressIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscARtgPnniCfgNodeSAddrPrefixLengthIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscARtgPnniCfgNodeSAddrReachabilityIndex"),
)
if mibBuilder.loadTexts:
    mscARtgPnniCfgNodeSAddrRowStatusEntry.setStatus("mandatory")
_MscARtgPnniCfgNodeSAddrRowStatus_Type = RowStatus
_MscARtgPnniCfgNodeSAddrRowStatus_Object = MibTableColumn
mscARtgPnniCfgNodeSAddrRowStatus = _MscARtgPnniCfgNodeSAddrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 3, 2, 1, 1, 1),
    _MscARtgPnniCfgNodeSAddrRowStatus_Type()
)
mscARtgPnniCfgNodeSAddrRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscARtgPnniCfgNodeSAddrRowStatus.setStatus("mandatory")
_MscARtgPnniCfgNodeSAddrComponentName_Type = DisplayString
_MscARtgPnniCfgNodeSAddrComponentName_Object = MibTableColumn
mscARtgPnniCfgNodeSAddrComponentName = _MscARtgPnniCfgNodeSAddrComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 3, 2, 1, 1, 2),
    _MscARtgPnniCfgNodeSAddrComponentName_Type()
)
mscARtgPnniCfgNodeSAddrComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscARtgPnniCfgNodeSAddrComponentName.setStatus("mandatory")
_MscARtgPnniCfgNodeSAddrStorageType_Type = StorageType
_MscARtgPnniCfgNodeSAddrStorageType_Object = MibTableColumn
mscARtgPnniCfgNodeSAddrStorageType = _MscARtgPnniCfgNodeSAddrStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 3, 2, 1, 1, 4),
    _MscARtgPnniCfgNodeSAddrStorageType_Type()
)
mscARtgPnniCfgNodeSAddrStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscARtgPnniCfgNodeSAddrStorageType.setStatus("mandatory")


class _MscARtgPnniCfgNodeSAddrAddressIndex_Type(HexString):
    """Custom type mscARtgPnniCfgNodeSAddrAddressIndex based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(19, 19),
    )


_MscARtgPnniCfgNodeSAddrAddressIndex_Type.__name__ = "HexString"
_MscARtgPnniCfgNodeSAddrAddressIndex_Object = MibTableColumn
mscARtgPnniCfgNodeSAddrAddressIndex = _MscARtgPnniCfgNodeSAddrAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 3, 2, 1, 1, 10),
    _MscARtgPnniCfgNodeSAddrAddressIndex_Type()
)
mscARtgPnniCfgNodeSAddrAddressIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscARtgPnniCfgNodeSAddrAddressIndex.setStatus("mandatory")


class _MscARtgPnniCfgNodeSAddrPrefixLengthIndex_Type(Integer32):
    """Custom type mscARtgPnniCfgNodeSAddrPrefixLengthIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 152),
    )


_MscARtgPnniCfgNodeSAddrPrefixLengthIndex_Type.__name__ = "Integer32"
_MscARtgPnniCfgNodeSAddrPrefixLengthIndex_Object = MibTableColumn
mscARtgPnniCfgNodeSAddrPrefixLengthIndex = _MscARtgPnniCfgNodeSAddrPrefixLengthIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 3, 2, 1, 1, 11),
    _MscARtgPnniCfgNodeSAddrPrefixLengthIndex_Type()
)
mscARtgPnniCfgNodeSAddrPrefixLengthIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscARtgPnniCfgNodeSAddrPrefixLengthIndex.setStatus("mandatory")


class _MscARtgPnniCfgNodeSAddrReachabilityIndex_Type(Integer32):
    """Custom type mscARtgPnniCfgNodeSAddrReachabilityIndex based on Integer32"""
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


_MscARtgPnniCfgNodeSAddrReachabilityIndex_Type.__name__ = "Integer32"
_MscARtgPnniCfgNodeSAddrReachabilityIndex_Object = MibTableColumn
mscARtgPnniCfgNodeSAddrReachabilityIndex = _MscARtgPnniCfgNodeSAddrReachabilityIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 3, 2, 1, 1, 12),
    _MscARtgPnniCfgNodeSAddrReachabilityIndex_Type()
)
mscARtgPnniCfgNodeSAddrReachabilityIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscARtgPnniCfgNodeSAddrReachabilityIndex.setStatus("mandatory")
_MscARtgPnniCfgNodeSAddrProvTable_Object = MibTable
mscARtgPnniCfgNodeSAddrProvTable = _MscARtgPnniCfgNodeSAddrProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 3, 2, 10)
)
if mibBuilder.loadTexts:
    mscARtgPnniCfgNodeSAddrProvTable.setStatus("mandatory")
_MscARtgPnniCfgNodeSAddrProvEntry_Object = MibTableRow
mscARtgPnniCfgNodeSAddrProvEntry = _MscARtgPnniCfgNodeSAddrProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 3, 2, 10, 1)
)
mscARtgPnniCfgNodeSAddrProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscARtgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscARtgPnniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscARtgPnniCfgNodeIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscARtgPnniCfgNodeSAddrAddressIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscARtgPnniCfgNodeSAddrPrefixLengthIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscARtgPnniCfgNodeSAddrReachabilityIndex"),
)
if mibBuilder.loadTexts:
    mscARtgPnniCfgNodeSAddrProvEntry.setStatus("mandatory")


class _MscARtgPnniCfgNodeSAddrSuppress_Type(Integer32):
    """Custom type mscARtgPnniCfgNodeSAddrSuppress based on Integer32"""
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


_MscARtgPnniCfgNodeSAddrSuppress_Type.__name__ = "Integer32"
_MscARtgPnniCfgNodeSAddrSuppress_Object = MibTableColumn
mscARtgPnniCfgNodeSAddrSuppress = _MscARtgPnniCfgNodeSAddrSuppress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 3, 2, 10, 1, 2),
    _MscARtgPnniCfgNodeSAddrSuppress_Type()
)
mscARtgPnniCfgNodeSAddrSuppress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscARtgPnniCfgNodeSAddrSuppress.setStatus("mandatory")
_MscARtgPnniCfgNodeSAddrOperTable_Object = MibTable
mscARtgPnniCfgNodeSAddrOperTable = _MscARtgPnniCfgNodeSAddrOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 3, 2, 11)
)
if mibBuilder.loadTexts:
    mscARtgPnniCfgNodeSAddrOperTable.setStatus("mandatory")
_MscARtgPnniCfgNodeSAddrOperEntry_Object = MibTableRow
mscARtgPnniCfgNodeSAddrOperEntry = _MscARtgPnniCfgNodeSAddrOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 3, 2, 11, 1)
)
mscARtgPnniCfgNodeSAddrOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscARtgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscARtgPnniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscARtgPnniCfgNodeIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscARtgPnniCfgNodeSAddrAddressIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscARtgPnniCfgNodeSAddrPrefixLengthIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscARtgPnniCfgNodeSAddrReachabilityIndex"),
)
if mibBuilder.loadTexts:
    mscARtgPnniCfgNodeSAddrOperEntry.setStatus("mandatory")


class _MscARtgPnniCfgNodeSAddrState_Type(Integer32):
    """Custom type mscARtgPnniCfgNodeSAddrState based on Integer32"""
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


_MscARtgPnniCfgNodeSAddrState_Type.__name__ = "Integer32"
_MscARtgPnniCfgNodeSAddrState_Object = MibTableColumn
mscARtgPnniCfgNodeSAddrState = _MscARtgPnniCfgNodeSAddrState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 3, 2, 11, 1, 1),
    _MscARtgPnniCfgNodeSAddrState_Type()
)
mscARtgPnniCfgNodeSAddrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscARtgPnniCfgNodeSAddrState.setStatus("mandatory")


class _MscARtgPnniCfgNodeSAddrScope_Type(Integer32):
    """Custom type mscARtgPnniCfgNodeSAddrScope based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 104),
    )


_MscARtgPnniCfgNodeSAddrScope_Type.__name__ = "Integer32"
_MscARtgPnniCfgNodeSAddrScope_Object = MibTableColumn
mscARtgPnniCfgNodeSAddrScope = _MscARtgPnniCfgNodeSAddrScope_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 3, 2, 11, 1, 2),
    _MscARtgPnniCfgNodeSAddrScope_Type()
)
mscARtgPnniCfgNodeSAddrScope.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscARtgPnniCfgNodeSAddrScope.setStatus("mandatory")
_MscARtgPnniCfgNodeNbr_ObjectIdentity = ObjectIdentity
mscARtgPnniCfgNodeNbr = _MscARtgPnniCfgNodeNbr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 3, 3)
)
_MscARtgPnniCfgNodeNbrRowStatusTable_Object = MibTable
mscARtgPnniCfgNodeNbrRowStatusTable = _MscARtgPnniCfgNodeNbrRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 3, 3, 1)
)
if mibBuilder.loadTexts:
    mscARtgPnniCfgNodeNbrRowStatusTable.setStatus("mandatory")
_MscARtgPnniCfgNodeNbrRowStatusEntry_Object = MibTableRow
mscARtgPnniCfgNodeNbrRowStatusEntry = _MscARtgPnniCfgNodeNbrRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 3, 3, 1, 1)
)
mscARtgPnniCfgNodeNbrRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscARtgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscARtgPnniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscARtgPnniCfgNodeIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscARtgPnniCfgNodeNbrIndex"),
)
if mibBuilder.loadTexts:
    mscARtgPnniCfgNodeNbrRowStatusEntry.setStatus("mandatory")
_MscARtgPnniCfgNodeNbrRowStatus_Type = RowStatus
_MscARtgPnniCfgNodeNbrRowStatus_Object = MibTableColumn
mscARtgPnniCfgNodeNbrRowStatus = _MscARtgPnniCfgNodeNbrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 3, 3, 1, 1, 1),
    _MscARtgPnniCfgNodeNbrRowStatus_Type()
)
mscARtgPnniCfgNodeNbrRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscARtgPnniCfgNodeNbrRowStatus.setStatus("mandatory")
_MscARtgPnniCfgNodeNbrComponentName_Type = DisplayString
_MscARtgPnniCfgNodeNbrComponentName_Object = MibTableColumn
mscARtgPnniCfgNodeNbrComponentName = _MscARtgPnniCfgNodeNbrComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 3, 3, 1, 1, 2),
    _MscARtgPnniCfgNodeNbrComponentName_Type()
)
mscARtgPnniCfgNodeNbrComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscARtgPnniCfgNodeNbrComponentName.setStatus("mandatory")
_MscARtgPnniCfgNodeNbrStorageType_Type = StorageType
_MscARtgPnniCfgNodeNbrStorageType_Object = MibTableColumn
mscARtgPnniCfgNodeNbrStorageType = _MscARtgPnniCfgNodeNbrStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 3, 3, 1, 1, 4),
    _MscARtgPnniCfgNodeNbrStorageType_Type()
)
mscARtgPnniCfgNodeNbrStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscARtgPnniCfgNodeNbrStorageType.setStatus("mandatory")


class _MscARtgPnniCfgNodeNbrIndex_Type(HexString):
    """Custom type mscARtgPnniCfgNodeNbrIndex based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(22, 22),
    )


_MscARtgPnniCfgNodeNbrIndex_Type.__name__ = "HexString"
_MscARtgPnniCfgNodeNbrIndex_Object = MibTableColumn
mscARtgPnniCfgNodeNbrIndex = _MscARtgPnniCfgNodeNbrIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 3, 3, 1, 1, 10),
    _MscARtgPnniCfgNodeNbrIndex_Type()
)
mscARtgPnniCfgNodeNbrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscARtgPnniCfgNodeNbrIndex.setStatus("mandatory")
_MscARtgPnniCfgNodeNbrOperTable_Object = MibTable
mscARtgPnniCfgNodeNbrOperTable = _MscARtgPnniCfgNodeNbrOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 3, 3, 10)
)
if mibBuilder.loadTexts:
    mscARtgPnniCfgNodeNbrOperTable.setStatus("mandatory")
_MscARtgPnniCfgNodeNbrOperEntry_Object = MibTableRow
mscARtgPnniCfgNodeNbrOperEntry = _MscARtgPnniCfgNodeNbrOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 3, 3, 10, 1)
)
mscARtgPnniCfgNodeNbrOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscARtgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscARtgPnniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscARtgPnniCfgNodeIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscARtgPnniCfgNodeNbrIndex"),
)
if mibBuilder.loadTexts:
    mscARtgPnniCfgNodeNbrOperEntry.setStatus("mandatory")


class _MscARtgPnniCfgNodeNbrPeerState_Type(Integer32):
    """Custom type mscARtgPnniCfgNodeNbrPeerState based on Integer32"""
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


_MscARtgPnniCfgNodeNbrPeerState_Type.__name__ = "Integer32"
_MscARtgPnniCfgNodeNbrPeerState_Object = MibTableColumn
mscARtgPnniCfgNodeNbrPeerState = _MscARtgPnniCfgNodeNbrPeerState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 3, 3, 10, 1, 2),
    _MscARtgPnniCfgNodeNbrPeerState_Type()
)
mscARtgPnniCfgNodeNbrPeerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscARtgPnniCfgNodeNbrPeerState.setStatus("mandatory")
_MscARtgPnniCfgNodeNbrStatsTable_Object = MibTable
mscARtgPnniCfgNodeNbrStatsTable = _MscARtgPnniCfgNodeNbrStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 3, 3, 11)
)
if mibBuilder.loadTexts:
    mscARtgPnniCfgNodeNbrStatsTable.setStatus("mandatory")
_MscARtgPnniCfgNodeNbrStatsEntry_Object = MibTableRow
mscARtgPnniCfgNodeNbrStatsEntry = _MscARtgPnniCfgNodeNbrStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 3, 3, 11, 1)
)
mscARtgPnniCfgNodeNbrStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscARtgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscARtgPnniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscARtgPnniCfgNodeIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscARtgPnniCfgNodeNbrIndex"),
)
if mibBuilder.loadTexts:
    mscARtgPnniCfgNodeNbrStatsEntry.setStatus("mandatory")
_MscARtgPnniCfgNodeNbrPtspRx_Type = Counter32
_MscARtgPnniCfgNodeNbrPtspRx_Object = MibTableColumn
mscARtgPnniCfgNodeNbrPtspRx = _MscARtgPnniCfgNodeNbrPtspRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 3, 3, 11, 1, 1),
    _MscARtgPnniCfgNodeNbrPtspRx_Type()
)
mscARtgPnniCfgNodeNbrPtspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscARtgPnniCfgNodeNbrPtspRx.setStatus("mandatory")
_MscARtgPnniCfgNodeNbrPtspTx_Type = Counter32
_MscARtgPnniCfgNodeNbrPtspTx_Object = MibTableColumn
mscARtgPnniCfgNodeNbrPtspTx = _MscARtgPnniCfgNodeNbrPtspTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 3, 3, 11, 1, 2),
    _MscARtgPnniCfgNodeNbrPtspTx_Type()
)
mscARtgPnniCfgNodeNbrPtspTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscARtgPnniCfgNodeNbrPtspTx.setStatus("mandatory")
_MscARtgPnniCfgNodeNbrPtseRx_Type = Counter32
_MscARtgPnniCfgNodeNbrPtseRx_Object = MibTableColumn
mscARtgPnniCfgNodeNbrPtseRx = _MscARtgPnniCfgNodeNbrPtseRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 3, 3, 11, 1, 3),
    _MscARtgPnniCfgNodeNbrPtseRx_Type()
)
mscARtgPnniCfgNodeNbrPtseRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscARtgPnniCfgNodeNbrPtseRx.setStatus("mandatory")
_MscARtgPnniCfgNodeNbrPtseTx_Type = Counter32
_MscARtgPnniCfgNodeNbrPtseTx_Object = MibTableColumn
mscARtgPnniCfgNodeNbrPtseTx = _MscARtgPnniCfgNodeNbrPtseTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 3, 3, 11, 1, 4),
    _MscARtgPnniCfgNodeNbrPtseTx_Type()
)
mscARtgPnniCfgNodeNbrPtseTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscARtgPnniCfgNodeNbrPtseTx.setStatus("mandatory")
_MscARtgPnniCfgNodeNbrPtseReqRx_Type = Counter32
_MscARtgPnniCfgNodeNbrPtseReqRx_Object = MibTableColumn
mscARtgPnniCfgNodeNbrPtseReqRx = _MscARtgPnniCfgNodeNbrPtseReqRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 3, 3, 11, 1, 5),
    _MscARtgPnniCfgNodeNbrPtseReqRx_Type()
)
mscARtgPnniCfgNodeNbrPtseReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscARtgPnniCfgNodeNbrPtseReqRx.setStatus("mandatory")
_MscARtgPnniCfgNodeNbrPtseReqTx_Type = Counter32
_MscARtgPnniCfgNodeNbrPtseReqTx_Object = MibTableColumn
mscARtgPnniCfgNodeNbrPtseReqTx = _MscARtgPnniCfgNodeNbrPtseReqTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 3, 3, 11, 1, 6),
    _MscARtgPnniCfgNodeNbrPtseReqTx_Type()
)
mscARtgPnniCfgNodeNbrPtseReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscARtgPnniCfgNodeNbrPtseReqTx.setStatus("mandatory")
_MscARtgPnniCfgNodeNbrPtseAcksRx_Type = Counter32
_MscARtgPnniCfgNodeNbrPtseAcksRx_Object = MibTableColumn
mscARtgPnniCfgNodeNbrPtseAcksRx = _MscARtgPnniCfgNodeNbrPtseAcksRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 3, 3, 11, 1, 7),
    _MscARtgPnniCfgNodeNbrPtseAcksRx_Type()
)
mscARtgPnniCfgNodeNbrPtseAcksRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscARtgPnniCfgNodeNbrPtseAcksRx.setStatus("mandatory")
_MscARtgPnniCfgNodeNbrPtseAcksTx_Type = Counter32
_MscARtgPnniCfgNodeNbrPtseAcksTx_Object = MibTableColumn
mscARtgPnniCfgNodeNbrPtseAcksTx = _MscARtgPnniCfgNodeNbrPtseAcksTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 3, 3, 11, 1, 8),
    _MscARtgPnniCfgNodeNbrPtseAcksTx_Type()
)
mscARtgPnniCfgNodeNbrPtseAcksTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscARtgPnniCfgNodeNbrPtseAcksTx.setStatus("mandatory")
_MscARtgPnniCfgNodeNbrDbSummariesRx_Type = Counter32
_MscARtgPnniCfgNodeNbrDbSummariesRx_Object = MibTableColumn
mscARtgPnniCfgNodeNbrDbSummariesRx = _MscARtgPnniCfgNodeNbrDbSummariesRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 3, 3, 11, 1, 9),
    _MscARtgPnniCfgNodeNbrDbSummariesRx_Type()
)
mscARtgPnniCfgNodeNbrDbSummariesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscARtgPnniCfgNodeNbrDbSummariesRx.setStatus("mandatory")
_MscARtgPnniCfgNodeNbrDbSummariesTx_Type = Counter32
_MscARtgPnniCfgNodeNbrDbSummariesTx_Object = MibTableColumn
mscARtgPnniCfgNodeNbrDbSummariesTx = _MscARtgPnniCfgNodeNbrDbSummariesTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 3, 3, 11, 1, 10),
    _MscARtgPnniCfgNodeNbrDbSummariesTx_Type()
)
mscARtgPnniCfgNodeNbrDbSummariesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscARtgPnniCfgNodeNbrDbSummariesTx.setStatus("mandatory")
_MscARtgPnniCfgNodeNbrBadPtspRx_Type = Counter32
_MscARtgPnniCfgNodeNbrBadPtspRx_Object = MibTableColumn
mscARtgPnniCfgNodeNbrBadPtspRx = _MscARtgPnniCfgNodeNbrBadPtspRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 3, 3, 11, 1, 11),
    _MscARtgPnniCfgNodeNbrBadPtspRx_Type()
)
mscARtgPnniCfgNodeNbrBadPtspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscARtgPnniCfgNodeNbrBadPtspRx.setStatus("mandatory")
_MscARtgPnniCfgNodeNbrBadPtseRx_Type = Counter32
_MscARtgPnniCfgNodeNbrBadPtseRx_Object = MibTableColumn
mscARtgPnniCfgNodeNbrBadPtseRx = _MscARtgPnniCfgNodeNbrBadPtseRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 3, 3, 11, 1, 12),
    _MscARtgPnniCfgNodeNbrBadPtseRx_Type()
)
mscARtgPnniCfgNodeNbrBadPtseRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscARtgPnniCfgNodeNbrBadPtseRx.setStatus("mandatory")
_MscARtgPnniCfgNodeNbrBadPtseReqRx_Type = Counter32
_MscARtgPnniCfgNodeNbrBadPtseReqRx_Object = MibTableColumn
mscARtgPnniCfgNodeNbrBadPtseReqRx = _MscARtgPnniCfgNodeNbrBadPtseReqRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 3, 3, 11, 1, 13),
    _MscARtgPnniCfgNodeNbrBadPtseReqRx_Type()
)
mscARtgPnniCfgNodeNbrBadPtseReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscARtgPnniCfgNodeNbrBadPtseReqRx.setStatus("mandatory")
_MscARtgPnniCfgNodeNbrBadPtseAckRx_Type = Counter32
_MscARtgPnniCfgNodeNbrBadPtseAckRx_Object = MibTableColumn
mscARtgPnniCfgNodeNbrBadPtseAckRx = _MscARtgPnniCfgNodeNbrBadPtseAckRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 3, 3, 11, 1, 14),
    _MscARtgPnniCfgNodeNbrBadPtseAckRx_Type()
)
mscARtgPnniCfgNodeNbrBadPtseAckRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscARtgPnniCfgNodeNbrBadPtseAckRx.setStatus("mandatory")
_MscARtgPnniCfgNodeNbrBadDbSummariesRx_Type = Counter32
_MscARtgPnniCfgNodeNbrBadDbSummariesRx_Object = MibTableColumn
mscARtgPnniCfgNodeNbrBadDbSummariesRx = _MscARtgPnniCfgNodeNbrBadDbSummariesRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 3, 3, 11, 1, 15),
    _MscARtgPnniCfgNodeNbrBadDbSummariesRx_Type()
)
mscARtgPnniCfgNodeNbrBadDbSummariesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscARtgPnniCfgNodeNbrBadDbSummariesRx.setStatus("mandatory")
_MscARtgPnniCfgNodeNbrRccListTable_Object = MibTable
mscARtgPnniCfgNodeNbrRccListTable = _MscARtgPnniCfgNodeNbrRccListTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 3, 3, 385)
)
if mibBuilder.loadTexts:
    mscARtgPnniCfgNodeNbrRccListTable.setStatus("mandatory")
_MscARtgPnniCfgNodeNbrRccListEntry_Object = MibTableRow
mscARtgPnniCfgNodeNbrRccListEntry = _MscARtgPnniCfgNodeNbrRccListEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 3, 3, 385, 1)
)
mscARtgPnniCfgNodeNbrRccListEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscARtgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscARtgPnniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscARtgPnniCfgNodeIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscARtgPnniCfgNodeNbrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscARtgPnniCfgNodeNbrRccListValue"),
)
if mibBuilder.loadTexts:
    mscARtgPnniCfgNodeNbrRccListEntry.setStatus("mandatory")
_MscARtgPnniCfgNodeNbrRccListValue_Type = RowPointer
_MscARtgPnniCfgNodeNbrRccListValue_Object = MibTableColumn
mscARtgPnniCfgNodeNbrRccListValue = _MscARtgPnniCfgNodeNbrRccListValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 3, 3, 385, 1, 1),
    _MscARtgPnniCfgNodeNbrRccListValue_Type()
)
mscARtgPnniCfgNodeNbrRccListValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscARtgPnniCfgNodeNbrRccListValue.setStatus("mandatory")
_MscARtgPnniCfgNodeDefSAddr_ObjectIdentity = ObjectIdentity
mscARtgPnniCfgNodeDefSAddr = _MscARtgPnniCfgNodeDefSAddr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 3, 4)
)
_MscARtgPnniCfgNodeDefSAddrRowStatusTable_Object = MibTable
mscARtgPnniCfgNodeDefSAddrRowStatusTable = _MscARtgPnniCfgNodeDefSAddrRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 3, 4, 1)
)
if mibBuilder.loadTexts:
    mscARtgPnniCfgNodeDefSAddrRowStatusTable.setStatus("mandatory")
_MscARtgPnniCfgNodeDefSAddrRowStatusEntry_Object = MibTableRow
mscARtgPnniCfgNodeDefSAddrRowStatusEntry = _MscARtgPnniCfgNodeDefSAddrRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 3, 4, 1, 1)
)
mscARtgPnniCfgNodeDefSAddrRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscARtgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscARtgPnniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscARtgPnniCfgNodeIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscARtgPnniCfgNodeDefSAddrIndex"),
)
if mibBuilder.loadTexts:
    mscARtgPnniCfgNodeDefSAddrRowStatusEntry.setStatus("mandatory")
_MscARtgPnniCfgNodeDefSAddrRowStatus_Type = RowStatus
_MscARtgPnniCfgNodeDefSAddrRowStatus_Object = MibTableColumn
mscARtgPnniCfgNodeDefSAddrRowStatus = _MscARtgPnniCfgNodeDefSAddrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 3, 4, 1, 1, 1),
    _MscARtgPnniCfgNodeDefSAddrRowStatus_Type()
)
mscARtgPnniCfgNodeDefSAddrRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscARtgPnniCfgNodeDefSAddrRowStatus.setStatus("mandatory")
_MscARtgPnniCfgNodeDefSAddrComponentName_Type = DisplayString
_MscARtgPnniCfgNodeDefSAddrComponentName_Object = MibTableColumn
mscARtgPnniCfgNodeDefSAddrComponentName = _MscARtgPnniCfgNodeDefSAddrComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 3, 4, 1, 1, 2),
    _MscARtgPnniCfgNodeDefSAddrComponentName_Type()
)
mscARtgPnniCfgNodeDefSAddrComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscARtgPnniCfgNodeDefSAddrComponentName.setStatus("mandatory")
_MscARtgPnniCfgNodeDefSAddrStorageType_Type = StorageType
_MscARtgPnniCfgNodeDefSAddrStorageType_Object = MibTableColumn
mscARtgPnniCfgNodeDefSAddrStorageType = _MscARtgPnniCfgNodeDefSAddrStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 3, 4, 1, 1, 4),
    _MscARtgPnniCfgNodeDefSAddrStorageType_Type()
)
mscARtgPnniCfgNodeDefSAddrStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscARtgPnniCfgNodeDefSAddrStorageType.setStatus("mandatory")
_MscARtgPnniCfgNodeDefSAddrIndex_Type = NonReplicated
_MscARtgPnniCfgNodeDefSAddrIndex_Object = MibTableColumn
mscARtgPnniCfgNodeDefSAddrIndex = _MscARtgPnniCfgNodeDefSAddrIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 3, 4, 1, 1, 10),
    _MscARtgPnniCfgNodeDefSAddrIndex_Type()
)
mscARtgPnniCfgNodeDefSAddrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscARtgPnniCfgNodeDefSAddrIndex.setStatus("mandatory")
_MscARtgPnniCfgNodeDefSAddrDefAddrTable_Object = MibTable
mscARtgPnniCfgNodeDefSAddrDefAddrTable = _MscARtgPnniCfgNodeDefSAddrDefAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 3, 4, 10)
)
if mibBuilder.loadTexts:
    mscARtgPnniCfgNodeDefSAddrDefAddrTable.setStatus("mandatory")
_MscARtgPnniCfgNodeDefSAddrDefAddrEntry_Object = MibTableRow
mscARtgPnniCfgNodeDefSAddrDefAddrEntry = _MscARtgPnniCfgNodeDefSAddrDefAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 3, 4, 10, 1)
)
mscARtgPnniCfgNodeDefSAddrDefAddrEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscARtgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscARtgPnniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscARtgPnniCfgNodeIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscARtgPnniCfgNodeDefSAddrIndex"),
)
if mibBuilder.loadTexts:
    mscARtgPnniCfgNodeDefSAddrDefAddrEntry.setStatus("mandatory")


class _MscARtgPnniCfgNodeDefSAddrAddress_Type(HexString):
    """Custom type mscARtgPnniCfgNodeDefSAddrAddress based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(13, 13),
    )


_MscARtgPnniCfgNodeDefSAddrAddress_Type.__name__ = "HexString"
_MscARtgPnniCfgNodeDefSAddrAddress_Object = MibTableColumn
mscARtgPnniCfgNodeDefSAddrAddress = _MscARtgPnniCfgNodeDefSAddrAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 3, 4, 10, 1, 1),
    _MscARtgPnniCfgNodeDefSAddrAddress_Type()
)
mscARtgPnniCfgNodeDefSAddrAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscARtgPnniCfgNodeDefSAddrAddress.setStatus("mandatory")
_MscARtgPnniCfgNodeDefSAddrOperTable_Object = MibTable
mscARtgPnniCfgNodeDefSAddrOperTable = _MscARtgPnniCfgNodeDefSAddrOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 3, 4, 11)
)
if mibBuilder.loadTexts:
    mscARtgPnniCfgNodeDefSAddrOperTable.setStatus("mandatory")
_MscARtgPnniCfgNodeDefSAddrOperEntry_Object = MibTableRow
mscARtgPnniCfgNodeDefSAddrOperEntry = _MscARtgPnniCfgNodeDefSAddrOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 3, 4, 11, 1)
)
mscARtgPnniCfgNodeDefSAddrOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscARtgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscARtgPnniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscARtgPnniCfgNodeIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscARtgPnniCfgNodeDefSAddrIndex"),
)
if mibBuilder.loadTexts:
    mscARtgPnniCfgNodeDefSAddrOperEntry.setStatus("mandatory")


class _MscARtgPnniCfgNodeDefSAddrState_Type(Integer32):
    """Custom type mscARtgPnniCfgNodeDefSAddrState based on Integer32"""
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


_MscARtgPnniCfgNodeDefSAddrState_Type.__name__ = "Integer32"
_MscARtgPnniCfgNodeDefSAddrState_Object = MibTableColumn
mscARtgPnniCfgNodeDefSAddrState = _MscARtgPnniCfgNodeDefSAddrState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 3, 4, 11, 1, 1),
    _MscARtgPnniCfgNodeDefSAddrState_Type()
)
mscARtgPnniCfgNodeDefSAddrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscARtgPnniCfgNodeDefSAddrState.setStatus("mandatory")


class _MscARtgPnniCfgNodeDefSAddrScope_Type(Integer32):
    """Custom type mscARtgPnniCfgNodeDefSAddrScope based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 104),
    )


_MscARtgPnniCfgNodeDefSAddrScope_Type.__name__ = "Integer32"
_MscARtgPnniCfgNodeDefSAddrScope_Object = MibTableColumn
mscARtgPnniCfgNodeDefSAddrScope = _MscARtgPnniCfgNodeDefSAddrScope_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 3, 4, 11, 1, 2),
    _MscARtgPnniCfgNodeDefSAddrScope_Type()
)
mscARtgPnniCfgNodeDefSAddrScope.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscARtgPnniCfgNodeDefSAddrScope.setStatus("mandatory")
_MscARtgPnniCfgNodeProvTable_Object = MibTable
mscARtgPnniCfgNodeProvTable = _MscARtgPnniCfgNodeProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 3, 10)
)
if mibBuilder.loadTexts:
    mscARtgPnniCfgNodeProvTable.setStatus("mandatory")
_MscARtgPnniCfgNodeProvEntry_Object = MibTableRow
mscARtgPnniCfgNodeProvEntry = _MscARtgPnniCfgNodeProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 3, 10, 1)
)
mscARtgPnniCfgNodeProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscARtgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscARtgPnniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscARtgPnniCfgNodeIndex"),
)
if mibBuilder.loadTexts:
    mscARtgPnniCfgNodeProvEntry.setStatus("mandatory")


class _MscARtgPnniCfgNodeNodeId_Type(HexString):
    """Custom type mscARtgPnniCfgNodeNodeId based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 22),
    )


_MscARtgPnniCfgNodeNodeId_Type.__name__ = "HexString"
_MscARtgPnniCfgNodeNodeId_Object = MibTableColumn
mscARtgPnniCfgNodeNodeId = _MscARtgPnniCfgNodeNodeId_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 3, 10, 1, 2),
    _MscARtgPnniCfgNodeNodeId_Type()
)
mscARtgPnniCfgNodeNodeId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscARtgPnniCfgNodeNodeId.setStatus("mandatory")


class _MscARtgPnniCfgNodePeerGroupId_Type(HexString):
    """Custom type mscARtgPnniCfgNodePeerGroupId based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_MscARtgPnniCfgNodePeerGroupId_Type.__name__ = "HexString"
_MscARtgPnniCfgNodePeerGroupId_Object = MibTableColumn
mscARtgPnniCfgNodePeerGroupId = _MscARtgPnniCfgNodePeerGroupId_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 3, 10, 1, 3),
    _MscARtgPnniCfgNodePeerGroupId_Type()
)
mscARtgPnniCfgNodePeerGroupId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscARtgPnniCfgNodePeerGroupId.setStatus("mandatory")
_MscARtgPnniCfgNodeOperTable_Object = MibTable
mscARtgPnniCfgNodeOperTable = _MscARtgPnniCfgNodeOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 3, 11)
)
if mibBuilder.loadTexts:
    mscARtgPnniCfgNodeOperTable.setStatus("mandatory")
_MscARtgPnniCfgNodeOperEntry_Object = MibTableRow
mscARtgPnniCfgNodeOperEntry = _MscARtgPnniCfgNodeOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 3, 11, 1)
)
mscARtgPnniCfgNodeOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscARtgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscARtgPnniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscARtgPnniCfgNodeIndex"),
)
if mibBuilder.loadTexts:
    mscARtgPnniCfgNodeOperEntry.setStatus("mandatory")


class _MscARtgPnniCfgNodeNodeAddress_Type(HexString):
    """Custom type mscARtgPnniCfgNodeNodeAddress based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_MscARtgPnniCfgNodeNodeAddress_Type.__name__ = "HexString"
_MscARtgPnniCfgNodeNodeAddress_Object = MibTableColumn
mscARtgPnniCfgNodeNodeAddress = _MscARtgPnniCfgNodeNodeAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 3, 11, 1, 1),
    _MscARtgPnniCfgNodeNodeAddress_Type()
)
mscARtgPnniCfgNodeNodeAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscARtgPnniCfgNodeNodeAddress.setStatus("mandatory")


class _MscARtgPnniCfgNodeOpNodeId_Type(HexString):
    """Custom type mscARtgPnniCfgNodeOpNodeId based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(22, 22),
    )


_MscARtgPnniCfgNodeOpNodeId_Type.__name__ = "HexString"
_MscARtgPnniCfgNodeOpNodeId_Object = MibTableColumn
mscARtgPnniCfgNodeOpNodeId = _MscARtgPnniCfgNodeOpNodeId_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 3, 11, 1, 2),
    _MscARtgPnniCfgNodeOpNodeId_Type()
)
mscARtgPnniCfgNodeOpNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscARtgPnniCfgNodeOpNodeId.setStatus("mandatory")


class _MscARtgPnniCfgNodeOpPeerGroupId_Type(HexString):
    """Custom type mscARtgPnniCfgNodeOpPeerGroupId based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(14, 14),
    )


_MscARtgPnniCfgNodeOpPeerGroupId_Type.__name__ = "HexString"
_MscARtgPnniCfgNodeOpPeerGroupId_Object = MibTableColumn
mscARtgPnniCfgNodeOpPeerGroupId = _MscARtgPnniCfgNodeOpPeerGroupId_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 3, 11, 1, 3),
    _MscARtgPnniCfgNodeOpPeerGroupId_Type()
)
mscARtgPnniCfgNodeOpPeerGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscARtgPnniCfgNodeOpPeerGroupId.setStatus("mandatory")


class _MscARtgPnniCfgNodeNumNeighbors_Type(Unsigned32):
    """Custom type mscARtgPnniCfgNodeNumNeighbors based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscARtgPnniCfgNodeNumNeighbors_Type.__name__ = "Unsigned32"
_MscARtgPnniCfgNodeNumNeighbors_Object = MibTableColumn
mscARtgPnniCfgNodeNumNeighbors = _MscARtgPnniCfgNodeNumNeighbors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 3, 11, 1, 4),
    _MscARtgPnniCfgNodeNumNeighbors_Type()
)
mscARtgPnniCfgNodeNumNeighbors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscARtgPnniCfgNodeNumNeighbors.setStatus("mandatory")


class _MscARtgPnniCfgNodeNumRccs_Type(Unsigned32):
    """Custom type mscARtgPnniCfgNodeNumRccs based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscARtgPnniCfgNodeNumRccs_Type.__name__ = "Unsigned32"
_MscARtgPnniCfgNodeNumRccs_Object = MibTableColumn
mscARtgPnniCfgNodeNumRccs = _MscARtgPnniCfgNodeNumRccs_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 3, 11, 1, 5),
    _MscARtgPnniCfgNodeNumRccs_Type()
)
mscARtgPnniCfgNodeNumRccs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscARtgPnniCfgNodeNumRccs.setStatus("mandatory")


class _MscARtgPnniCfgNodeCurrentLeadershipPriority_Type(Unsigned32):
    """Custom type mscARtgPnniCfgNodeCurrentLeadershipPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 205),
    )


_MscARtgPnniCfgNodeCurrentLeadershipPriority_Type.__name__ = "Unsigned32"
_MscARtgPnniCfgNodeCurrentLeadershipPriority_Object = MibTableColumn
mscARtgPnniCfgNodeCurrentLeadershipPriority = _MscARtgPnniCfgNodeCurrentLeadershipPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 3, 11, 1, 6),
    _MscARtgPnniCfgNodeCurrentLeadershipPriority_Type()
)
mscARtgPnniCfgNodeCurrentLeadershipPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscARtgPnniCfgNodeCurrentLeadershipPriority.setStatus("mandatory")


class _MscARtgPnniCfgNodePglElectionState_Type(Integer32):
    """Custom type mscARtgPnniCfgNodePglElectionState based on Integer32"""
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


_MscARtgPnniCfgNodePglElectionState_Type.__name__ = "Integer32"
_MscARtgPnniCfgNodePglElectionState_Object = MibTableColumn
mscARtgPnniCfgNodePglElectionState = _MscARtgPnniCfgNodePglElectionState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 3, 11, 1, 7),
    _MscARtgPnniCfgNodePglElectionState_Type()
)
mscARtgPnniCfgNodePglElectionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscARtgPnniCfgNodePglElectionState.setStatus("mandatory")
_MscARtgPnniTop_ObjectIdentity = ObjectIdentity
mscARtgPnniTop = _MscARtgPnniTop_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 4)
)
_MscARtgPnniTopRowStatusTable_Object = MibTable
mscARtgPnniTopRowStatusTable = _MscARtgPnniTopRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 4, 1)
)
if mibBuilder.loadTexts:
    mscARtgPnniTopRowStatusTable.setStatus("mandatory")
_MscARtgPnniTopRowStatusEntry_Object = MibTableRow
mscARtgPnniTopRowStatusEntry = _MscARtgPnniTopRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 4, 1, 1)
)
mscARtgPnniTopRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscARtgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscARtgPnniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscARtgPnniTopIndex"),
)
if mibBuilder.loadTexts:
    mscARtgPnniTopRowStatusEntry.setStatus("mandatory")
_MscARtgPnniTopRowStatus_Type = RowStatus
_MscARtgPnniTopRowStatus_Object = MibTableColumn
mscARtgPnniTopRowStatus = _MscARtgPnniTopRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 4, 1, 1, 1),
    _MscARtgPnniTopRowStatus_Type()
)
mscARtgPnniTopRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscARtgPnniTopRowStatus.setStatus("mandatory")
_MscARtgPnniTopComponentName_Type = DisplayString
_MscARtgPnniTopComponentName_Object = MibTableColumn
mscARtgPnniTopComponentName = _MscARtgPnniTopComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 4, 1, 1, 2),
    _MscARtgPnniTopComponentName_Type()
)
mscARtgPnniTopComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscARtgPnniTopComponentName.setStatus("mandatory")
_MscARtgPnniTopStorageType_Type = StorageType
_MscARtgPnniTopStorageType_Object = MibTableColumn
mscARtgPnniTopStorageType = _MscARtgPnniTopStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 4, 1, 1, 4),
    _MscARtgPnniTopStorageType_Type()
)
mscARtgPnniTopStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscARtgPnniTopStorageType.setStatus("mandatory")


class _MscARtgPnniTopIndex_Type(Integer32):
    """Custom type mscARtgPnniTopIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 104),
    )


_MscARtgPnniTopIndex_Type.__name__ = "Integer32"
_MscARtgPnniTopIndex_Object = MibTableColumn
mscARtgPnniTopIndex = _MscARtgPnniTopIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 4, 1, 1, 10),
    _MscARtgPnniTopIndex_Type()
)
mscARtgPnniTopIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscARtgPnniTopIndex.setStatus("mandatory")
_MscARtgPnniTopNode_ObjectIdentity = ObjectIdentity
mscARtgPnniTopNode = _MscARtgPnniTopNode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 4, 2)
)
_MscARtgPnniTopNodeRowStatusTable_Object = MibTable
mscARtgPnniTopNodeRowStatusTable = _MscARtgPnniTopNodeRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 4, 2, 1)
)
if mibBuilder.loadTexts:
    mscARtgPnniTopNodeRowStatusTable.setStatus("mandatory")
_MscARtgPnniTopNodeRowStatusEntry_Object = MibTableRow
mscARtgPnniTopNodeRowStatusEntry = _MscARtgPnniTopNodeRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 4, 2, 1, 1)
)
mscARtgPnniTopNodeRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscARtgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscARtgPnniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscARtgPnniTopIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscARtgPnniTopNodeIndex"),
)
if mibBuilder.loadTexts:
    mscARtgPnniTopNodeRowStatusEntry.setStatus("mandatory")
_MscARtgPnniTopNodeRowStatus_Type = RowStatus
_MscARtgPnniTopNodeRowStatus_Object = MibTableColumn
mscARtgPnniTopNodeRowStatus = _MscARtgPnniTopNodeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 4, 2, 1, 1, 1),
    _MscARtgPnniTopNodeRowStatus_Type()
)
mscARtgPnniTopNodeRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscARtgPnniTopNodeRowStatus.setStatus("mandatory")
_MscARtgPnniTopNodeComponentName_Type = DisplayString
_MscARtgPnniTopNodeComponentName_Object = MibTableColumn
mscARtgPnniTopNodeComponentName = _MscARtgPnniTopNodeComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 4, 2, 1, 1, 2),
    _MscARtgPnniTopNodeComponentName_Type()
)
mscARtgPnniTopNodeComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscARtgPnniTopNodeComponentName.setStatus("mandatory")
_MscARtgPnniTopNodeStorageType_Type = StorageType
_MscARtgPnniTopNodeStorageType_Object = MibTableColumn
mscARtgPnniTopNodeStorageType = _MscARtgPnniTopNodeStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 4, 2, 1, 1, 4),
    _MscARtgPnniTopNodeStorageType_Type()
)
mscARtgPnniTopNodeStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscARtgPnniTopNodeStorageType.setStatus("mandatory")


class _MscARtgPnniTopNodeIndex_Type(HexString):
    """Custom type mscARtgPnniTopNodeIndex based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(22, 22),
    )


_MscARtgPnniTopNodeIndex_Type.__name__ = "HexString"
_MscARtgPnniTopNodeIndex_Object = MibTableColumn
mscARtgPnniTopNodeIndex = _MscARtgPnniTopNodeIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 4, 2, 1, 1, 10),
    _MscARtgPnniTopNodeIndex_Type()
)
mscARtgPnniTopNodeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscARtgPnniTopNodeIndex.setStatus("mandatory")
_MscARtgPnniTopNodeAddr_ObjectIdentity = ObjectIdentity
mscARtgPnniTopNodeAddr = _MscARtgPnniTopNodeAddr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 4, 2, 2)
)
_MscARtgPnniTopNodeAddrRowStatusTable_Object = MibTable
mscARtgPnniTopNodeAddrRowStatusTable = _MscARtgPnniTopNodeAddrRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 4, 2, 2, 1)
)
if mibBuilder.loadTexts:
    mscARtgPnniTopNodeAddrRowStatusTable.setStatus("mandatory")
_MscARtgPnniTopNodeAddrRowStatusEntry_Object = MibTableRow
mscARtgPnniTopNodeAddrRowStatusEntry = _MscARtgPnniTopNodeAddrRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 4, 2, 2, 1, 1)
)
mscARtgPnniTopNodeAddrRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscARtgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscARtgPnniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscARtgPnniTopIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscARtgPnniTopNodeIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscARtgPnniTopNodeAddrAddressIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscARtgPnniTopNodeAddrPrefixLengthIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscARtgPnniTopNodeAddrReachabilityIndex"),
)
if mibBuilder.loadTexts:
    mscARtgPnniTopNodeAddrRowStatusEntry.setStatus("mandatory")
_MscARtgPnniTopNodeAddrRowStatus_Type = RowStatus
_MscARtgPnniTopNodeAddrRowStatus_Object = MibTableColumn
mscARtgPnniTopNodeAddrRowStatus = _MscARtgPnniTopNodeAddrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 4, 2, 2, 1, 1, 1),
    _MscARtgPnniTopNodeAddrRowStatus_Type()
)
mscARtgPnniTopNodeAddrRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscARtgPnniTopNodeAddrRowStatus.setStatus("mandatory")
_MscARtgPnniTopNodeAddrComponentName_Type = DisplayString
_MscARtgPnniTopNodeAddrComponentName_Object = MibTableColumn
mscARtgPnniTopNodeAddrComponentName = _MscARtgPnniTopNodeAddrComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 4, 2, 2, 1, 1, 2),
    _MscARtgPnniTopNodeAddrComponentName_Type()
)
mscARtgPnniTopNodeAddrComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscARtgPnniTopNodeAddrComponentName.setStatus("mandatory")
_MscARtgPnniTopNodeAddrStorageType_Type = StorageType
_MscARtgPnniTopNodeAddrStorageType_Object = MibTableColumn
mscARtgPnniTopNodeAddrStorageType = _MscARtgPnniTopNodeAddrStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 4, 2, 2, 1, 1, 4),
    _MscARtgPnniTopNodeAddrStorageType_Type()
)
mscARtgPnniTopNodeAddrStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscARtgPnniTopNodeAddrStorageType.setStatus("mandatory")


class _MscARtgPnniTopNodeAddrAddressIndex_Type(HexString):
    """Custom type mscARtgPnniTopNodeAddrAddressIndex based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(19, 19),
    )


_MscARtgPnniTopNodeAddrAddressIndex_Type.__name__ = "HexString"
_MscARtgPnniTopNodeAddrAddressIndex_Object = MibTableColumn
mscARtgPnniTopNodeAddrAddressIndex = _MscARtgPnniTopNodeAddrAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 4, 2, 2, 1, 1, 10),
    _MscARtgPnniTopNodeAddrAddressIndex_Type()
)
mscARtgPnniTopNodeAddrAddressIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscARtgPnniTopNodeAddrAddressIndex.setStatus("mandatory")


class _MscARtgPnniTopNodeAddrPrefixLengthIndex_Type(Integer32):
    """Custom type mscARtgPnniTopNodeAddrPrefixLengthIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 152),
    )


_MscARtgPnniTopNodeAddrPrefixLengthIndex_Type.__name__ = "Integer32"
_MscARtgPnniTopNodeAddrPrefixLengthIndex_Object = MibTableColumn
mscARtgPnniTopNodeAddrPrefixLengthIndex = _MscARtgPnniTopNodeAddrPrefixLengthIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 4, 2, 2, 1, 1, 11),
    _MscARtgPnniTopNodeAddrPrefixLengthIndex_Type()
)
mscARtgPnniTopNodeAddrPrefixLengthIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscARtgPnniTopNodeAddrPrefixLengthIndex.setStatus("mandatory")


class _MscARtgPnniTopNodeAddrReachabilityIndex_Type(Integer32):
    """Custom type mscARtgPnniTopNodeAddrReachabilityIndex based on Integer32"""
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


_MscARtgPnniTopNodeAddrReachabilityIndex_Type.__name__ = "Integer32"
_MscARtgPnniTopNodeAddrReachabilityIndex_Object = MibTableColumn
mscARtgPnniTopNodeAddrReachabilityIndex = _MscARtgPnniTopNodeAddrReachabilityIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 4, 2, 2, 1, 1, 12),
    _MscARtgPnniTopNodeAddrReachabilityIndex_Type()
)
mscARtgPnniTopNodeAddrReachabilityIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscARtgPnniTopNodeAddrReachabilityIndex.setStatus("mandatory")
_MscARtgPnniTopNodeAddrOperTable_Object = MibTable
mscARtgPnniTopNodeAddrOperTable = _MscARtgPnniTopNodeAddrOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 4, 2, 2, 10)
)
if mibBuilder.loadTexts:
    mscARtgPnniTopNodeAddrOperTable.setStatus("mandatory")
_MscARtgPnniTopNodeAddrOperEntry_Object = MibTableRow
mscARtgPnniTopNodeAddrOperEntry = _MscARtgPnniTopNodeAddrOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 4, 2, 2, 10, 1)
)
mscARtgPnniTopNodeAddrOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscARtgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscARtgPnniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscARtgPnniTopIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscARtgPnniTopNodeIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscARtgPnniTopNodeAddrAddressIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscARtgPnniTopNodeAddrPrefixLengthIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscARtgPnniTopNodeAddrReachabilityIndex"),
)
if mibBuilder.loadTexts:
    mscARtgPnniTopNodeAddrOperEntry.setStatus("mandatory")


class _MscARtgPnniTopNodeAddrScope_Type(Unsigned32):
    """Custom type mscARtgPnniTopNodeAddrScope based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 104),
    )


_MscARtgPnniTopNodeAddrScope_Type.__name__ = "Unsigned32"
_MscARtgPnniTopNodeAddrScope_Object = MibTableColumn
mscARtgPnniTopNodeAddrScope = _MscARtgPnniTopNodeAddrScope_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 4, 2, 2, 10, 1, 1),
    _MscARtgPnniTopNodeAddrScope_Type()
)
mscARtgPnniTopNodeAddrScope.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscARtgPnniTopNodeAddrScope.setStatus("mandatory")
_MscARtgPnniTopNodeLink_ObjectIdentity = ObjectIdentity
mscARtgPnniTopNodeLink = _MscARtgPnniTopNodeLink_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 4, 2, 3)
)
_MscARtgPnniTopNodeLinkRowStatusTable_Object = MibTable
mscARtgPnniTopNodeLinkRowStatusTable = _MscARtgPnniTopNodeLinkRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 4, 2, 3, 1)
)
if mibBuilder.loadTexts:
    mscARtgPnniTopNodeLinkRowStatusTable.setStatus("mandatory")
_MscARtgPnniTopNodeLinkRowStatusEntry_Object = MibTableRow
mscARtgPnniTopNodeLinkRowStatusEntry = _MscARtgPnniTopNodeLinkRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 4, 2, 3, 1, 1)
)
mscARtgPnniTopNodeLinkRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscARtgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscARtgPnniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscARtgPnniTopIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscARtgPnniTopNodeIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscARtgPnniTopNodeLinkIndex"),
)
if mibBuilder.loadTexts:
    mscARtgPnniTopNodeLinkRowStatusEntry.setStatus("mandatory")
_MscARtgPnniTopNodeLinkRowStatus_Type = RowStatus
_MscARtgPnniTopNodeLinkRowStatus_Object = MibTableColumn
mscARtgPnniTopNodeLinkRowStatus = _MscARtgPnniTopNodeLinkRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 4, 2, 3, 1, 1, 1),
    _MscARtgPnniTopNodeLinkRowStatus_Type()
)
mscARtgPnniTopNodeLinkRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscARtgPnniTopNodeLinkRowStatus.setStatus("mandatory")
_MscARtgPnniTopNodeLinkComponentName_Type = DisplayString
_MscARtgPnniTopNodeLinkComponentName_Object = MibTableColumn
mscARtgPnniTopNodeLinkComponentName = _MscARtgPnniTopNodeLinkComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 4, 2, 3, 1, 1, 2),
    _MscARtgPnniTopNodeLinkComponentName_Type()
)
mscARtgPnniTopNodeLinkComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscARtgPnniTopNodeLinkComponentName.setStatus("mandatory")
_MscARtgPnniTopNodeLinkStorageType_Type = StorageType
_MscARtgPnniTopNodeLinkStorageType_Object = MibTableColumn
mscARtgPnniTopNodeLinkStorageType = _MscARtgPnniTopNodeLinkStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 4, 2, 3, 1, 1, 4),
    _MscARtgPnniTopNodeLinkStorageType_Type()
)
mscARtgPnniTopNodeLinkStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscARtgPnniTopNodeLinkStorageType.setStatus("mandatory")


class _MscARtgPnniTopNodeLinkIndex_Type(Integer32):
    """Custom type mscARtgPnniTopNodeLinkIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 268435455),
    )


_MscARtgPnniTopNodeLinkIndex_Type.__name__ = "Integer32"
_MscARtgPnniTopNodeLinkIndex_Object = MibTableColumn
mscARtgPnniTopNodeLinkIndex = _MscARtgPnniTopNodeLinkIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 4, 2, 3, 1, 1, 10),
    _MscARtgPnniTopNodeLinkIndex_Type()
)
mscARtgPnniTopNodeLinkIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscARtgPnniTopNodeLinkIndex.setStatus("mandatory")
_MscARtgPnniTopNodeLinkOperTable_Object = MibTable
mscARtgPnniTopNodeLinkOperTable = _MscARtgPnniTopNodeLinkOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 4, 2, 3, 10)
)
if mibBuilder.loadTexts:
    mscARtgPnniTopNodeLinkOperTable.setStatus("mandatory")
_MscARtgPnniTopNodeLinkOperEntry_Object = MibTableRow
mscARtgPnniTopNodeLinkOperEntry = _MscARtgPnniTopNodeLinkOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 4, 2, 3, 10, 1)
)
mscARtgPnniTopNodeLinkOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscARtgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscARtgPnniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscARtgPnniTopIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscARtgPnniTopNodeIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscARtgPnniTopNodeLinkIndex"),
)
if mibBuilder.loadTexts:
    mscARtgPnniTopNodeLinkOperEntry.setStatus("mandatory")


class _MscARtgPnniTopNodeLinkRemoteNodeId_Type(HexString):
    """Custom type mscARtgPnniTopNodeLinkRemoteNodeId based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(22, 22),
    )


_MscARtgPnniTopNodeLinkRemoteNodeId_Type.__name__ = "HexString"
_MscARtgPnniTopNodeLinkRemoteNodeId_Object = MibTableColumn
mscARtgPnniTopNodeLinkRemoteNodeId = _MscARtgPnniTopNodeLinkRemoteNodeId_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 4, 2, 3, 10, 1, 1),
    _MscARtgPnniTopNodeLinkRemoteNodeId_Type()
)
mscARtgPnniTopNodeLinkRemoteNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscARtgPnniTopNodeLinkRemoteNodeId.setStatus("mandatory")


class _MscARtgPnniTopNodeLinkRemotePortId_Type(Unsigned32):
    """Custom type mscARtgPnniTopNodeLinkRemotePortId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscARtgPnniTopNodeLinkRemotePortId_Type.__name__ = "Unsigned32"
_MscARtgPnniTopNodeLinkRemotePortId_Object = MibTableColumn
mscARtgPnniTopNodeLinkRemotePortId = _MscARtgPnniTopNodeLinkRemotePortId_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 4, 2, 3, 10, 1, 2),
    _MscARtgPnniTopNodeLinkRemotePortId_Type()
)
mscARtgPnniTopNodeLinkRemotePortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscARtgPnniTopNodeLinkRemotePortId.setStatus("mandatory")
_MscARtgPnniTopOperTable_Object = MibTable
mscARtgPnniTopOperTable = _MscARtgPnniTopOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 4, 10)
)
if mibBuilder.loadTexts:
    mscARtgPnniTopOperTable.setStatus("mandatory")
_MscARtgPnniTopOperEntry_Object = MibTableRow
mscARtgPnniTopOperEntry = _MscARtgPnniTopOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 4, 10, 1)
)
mscARtgPnniTopOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscARtgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscARtgPnniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscARtgPnniTopIndex"),
)
if mibBuilder.loadTexts:
    mscARtgPnniTopOperEntry.setStatus("mandatory")


class _MscARtgPnniTopPtsesInDatabase_Type(Gauge32):
    """Custom type mscARtgPnniTopPtsesInDatabase based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscARtgPnniTopPtsesInDatabase_Type.__name__ = "Gauge32"
_MscARtgPnniTopPtsesInDatabase_Object = MibTableColumn
mscARtgPnniTopPtsesInDatabase = _MscARtgPnniTopPtsesInDatabase_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 4, 10, 1, 1),
    _MscARtgPnniTopPtsesInDatabase_Type()
)
mscARtgPnniTopPtsesInDatabase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscARtgPnniTopPtsesInDatabase.setStatus("mandatory")


class _MscARtgPnniTopPglNodeId_Type(HexString):
    """Custom type mscARtgPnniTopPglNodeId based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 22),
    )


_MscARtgPnniTopPglNodeId_Type.__name__ = "HexString"
_MscARtgPnniTopPglNodeId_Object = MibTableColumn
mscARtgPnniTopPglNodeId = _MscARtgPnniTopPglNodeId_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 4, 10, 1, 2),
    _MscARtgPnniTopPglNodeId_Type()
)
mscARtgPnniTopPglNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscARtgPnniTopPglNodeId.setStatus("mandatory")


class _MscARtgPnniTopActiveParentNodeId_Type(HexString):
    """Custom type mscARtgPnniTopActiveParentNodeId based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 22),
    )


_MscARtgPnniTopActiveParentNodeId_Type.__name__ = "HexString"
_MscARtgPnniTopActiveParentNodeId_Object = MibTableColumn
mscARtgPnniTopActiveParentNodeId = _MscARtgPnniTopActiveParentNodeId_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 4, 10, 1, 3),
    _MscARtgPnniTopActiveParentNodeId_Type()
)
mscARtgPnniTopActiveParentNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscARtgPnniTopActiveParentNodeId.setStatus("mandatory")


class _MscARtgPnniTopPreferredPglNodeId_Type(HexString):
    """Custom type mscARtgPnniTopPreferredPglNodeId based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 22),
    )


_MscARtgPnniTopPreferredPglNodeId_Type.__name__ = "HexString"
_MscARtgPnniTopPreferredPglNodeId_Object = MibTableColumn
mscARtgPnniTopPreferredPglNodeId = _MscARtgPnniTopPreferredPglNodeId_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 4, 10, 1, 4),
    _MscARtgPnniTopPreferredPglNodeId_Type()
)
mscARtgPnniTopPreferredPglNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscARtgPnniTopPreferredPglNodeId.setStatus("mandatory")
_MscARtgPnniPort_ObjectIdentity = ObjectIdentity
mscARtgPnniPort = _MscARtgPnniPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 5)
)
_MscARtgPnniPortRowStatusTable_Object = MibTable
mscARtgPnniPortRowStatusTable = _MscARtgPnniPortRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 5, 1)
)
if mibBuilder.loadTexts:
    mscARtgPnniPortRowStatusTable.setStatus("mandatory")
_MscARtgPnniPortRowStatusEntry_Object = MibTableRow
mscARtgPnniPortRowStatusEntry = _MscARtgPnniPortRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 5, 1, 1)
)
mscARtgPnniPortRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscARtgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscARtgPnniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscARtgPnniPortIndex"),
)
if mibBuilder.loadTexts:
    mscARtgPnniPortRowStatusEntry.setStatus("mandatory")
_MscARtgPnniPortRowStatus_Type = RowStatus
_MscARtgPnniPortRowStatus_Object = MibTableColumn
mscARtgPnniPortRowStatus = _MscARtgPnniPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 5, 1, 1, 1),
    _MscARtgPnniPortRowStatus_Type()
)
mscARtgPnniPortRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscARtgPnniPortRowStatus.setStatus("mandatory")
_MscARtgPnniPortComponentName_Type = DisplayString
_MscARtgPnniPortComponentName_Object = MibTableColumn
mscARtgPnniPortComponentName = _MscARtgPnniPortComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 5, 1, 1, 2),
    _MscARtgPnniPortComponentName_Type()
)
mscARtgPnniPortComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscARtgPnniPortComponentName.setStatus("mandatory")
_MscARtgPnniPortStorageType_Type = StorageType
_MscARtgPnniPortStorageType_Object = MibTableColumn
mscARtgPnniPortStorageType = _MscARtgPnniPortStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 5, 1, 1, 4),
    _MscARtgPnniPortStorageType_Type()
)
mscARtgPnniPortStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscARtgPnniPortStorageType.setStatus("mandatory")


class _MscARtgPnniPortIndex_Type(Integer32):
    """Custom type mscARtgPnniPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 268435455),
    )


_MscARtgPnniPortIndex_Type.__name__ = "Integer32"
_MscARtgPnniPortIndex_Object = MibTableColumn
mscARtgPnniPortIndex = _MscARtgPnniPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 5, 1, 1, 10),
    _MscARtgPnniPortIndex_Type()
)
mscARtgPnniPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscARtgPnniPortIndex.setStatus("mandatory")
_MscARtgPnniPortOperTable_Object = MibTable
mscARtgPnniPortOperTable = _MscARtgPnniPortOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 5, 10)
)
if mibBuilder.loadTexts:
    mscARtgPnniPortOperTable.setStatus("mandatory")
_MscARtgPnniPortOperEntry_Object = MibTableRow
mscARtgPnniPortOperEntry = _MscARtgPnniPortOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 5, 10, 1)
)
mscARtgPnniPortOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscARtgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscARtgPnniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscARtgPnniPortIndex"),
)
if mibBuilder.loadTexts:
    mscARtgPnniPortOperEntry.setStatus("mandatory")
_MscARtgPnniPortStdComponentName_Type = RowPointer
_MscARtgPnniPortStdComponentName_Object = MibTableColumn
mscARtgPnniPortStdComponentName = _MscARtgPnniPortStdComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 5, 10, 1, 1),
    _MscARtgPnniPortStdComponentName_Type()
)
mscARtgPnniPortStdComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscARtgPnniPortStdComponentName.setStatus("mandatory")
_MscARtgPnniProvTable_Object = MibTable
mscARtgPnniProvTable = _MscARtgPnniProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 10)
)
if mibBuilder.loadTexts:
    mscARtgPnniProvTable.setStatus("mandatory")
_MscARtgPnniProvEntry_Object = MibTableRow
mscARtgPnniProvEntry = _MscARtgPnniProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 10, 1)
)
mscARtgPnniProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscARtgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscARtgPnniIndex"),
)
if mibBuilder.loadTexts:
    mscARtgPnniProvEntry.setStatus("mandatory")


class _MscARtgPnniNodeAddressPrefix_Type(HexString):
    """Custom type mscARtgPnniNodeAddressPrefix based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_MscARtgPnniNodeAddressPrefix_Type.__name__ = "HexString"
_MscARtgPnniNodeAddressPrefix_Object = MibTableColumn
mscARtgPnniNodeAddressPrefix = _MscARtgPnniNodeAddressPrefix_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 10, 1, 1),
    _MscARtgPnniNodeAddressPrefix_Type()
)
mscARtgPnniNodeAddressPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscARtgPnniNodeAddressPrefix.setStatus("mandatory")


class _MscARtgPnniDefaultScope_Type(Unsigned32):
    """Custom type mscARtgPnniDefaultScope based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 104),
    )


_MscARtgPnniDefaultScope_Type.__name__ = "Unsigned32"
_MscARtgPnniDefaultScope_Object = MibTableColumn
mscARtgPnniDefaultScope = _MscARtgPnniDefaultScope_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 10, 1, 2),
    _MscARtgPnniDefaultScope_Type()
)
mscARtgPnniDefaultScope.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscARtgPnniDefaultScope.setStatus("mandatory")


class _MscARtgPnniDomain_Type(AsciiString):
    """Custom type mscARtgPnniDomain based on AsciiString"""
    defaultHexValue = "31"

    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_MscARtgPnniDomain_Type.__name__ = "AsciiString"
_MscARtgPnniDomain_Object = MibTableColumn
mscARtgPnniDomain = _MscARtgPnniDomain_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 10, 1, 3),
    _MscARtgPnniDomain_Type()
)
mscARtgPnniDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscARtgPnniDomain.setStatus("mandatory")


class _MscARtgPnniRestrictTransit_Type(Integer32):
    """Custom type mscARtgPnniRestrictTransit based on Integer32"""
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


_MscARtgPnniRestrictTransit_Type.__name__ = "Integer32"
_MscARtgPnniRestrictTransit_Object = MibTableColumn
mscARtgPnniRestrictTransit = _MscARtgPnniRestrictTransit_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 10, 1, 4),
    _MscARtgPnniRestrictTransit_Type()
)
mscARtgPnniRestrictTransit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscARtgPnniRestrictTransit.setStatus("mandatory")


class _MscARtgPnniMaxAlternateRoutesOnCrankback_Type(Unsigned32):
    """Custom type mscARtgPnniMaxAlternateRoutesOnCrankback based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_MscARtgPnniMaxAlternateRoutesOnCrankback_Type.__name__ = "Unsigned32"
_MscARtgPnniMaxAlternateRoutesOnCrankback_Object = MibTableColumn
mscARtgPnniMaxAlternateRoutesOnCrankback = _MscARtgPnniMaxAlternateRoutesOnCrankback_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 10, 1, 5),
    _MscARtgPnniMaxAlternateRoutesOnCrankback_Type()
)
mscARtgPnniMaxAlternateRoutesOnCrankback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscARtgPnniMaxAlternateRoutesOnCrankback.setStatus("mandatory")
_MscARtgPnniPglParmsTable_Object = MibTable
mscARtgPnniPglParmsTable = _MscARtgPnniPglParmsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 11)
)
if mibBuilder.loadTexts:
    mscARtgPnniPglParmsTable.setStatus("mandatory")
_MscARtgPnniPglParmsEntry_Object = MibTableRow
mscARtgPnniPglParmsEntry = _MscARtgPnniPglParmsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 11, 1)
)
mscARtgPnniPglParmsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscARtgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscARtgPnniIndex"),
)
if mibBuilder.loadTexts:
    mscARtgPnniPglParmsEntry.setStatus("mandatory")


class _MscARtgPnniPglInitTime_Type(Unsigned32):
    """Custom type mscARtgPnniPglInitTime based on Unsigned32"""
    defaultValue = 15

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscARtgPnniPglInitTime_Type.__name__ = "Unsigned32"
_MscARtgPnniPglInitTime_Object = MibTableColumn
mscARtgPnniPglInitTime = _MscARtgPnniPglInitTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 11, 1, 1),
    _MscARtgPnniPglInitTime_Type()
)
mscARtgPnniPglInitTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscARtgPnniPglInitTime.setStatus("mandatory")


class _MscARtgPnniOverrideDelay_Type(Unsigned32):
    """Custom type mscARtgPnniOverrideDelay based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MscARtgPnniOverrideDelay_Type.__name__ = "Unsigned32"
_MscARtgPnniOverrideDelay_Object = MibTableColumn
mscARtgPnniOverrideDelay = _MscARtgPnniOverrideDelay_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 11, 1, 2),
    _MscARtgPnniOverrideDelay_Type()
)
mscARtgPnniOverrideDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscARtgPnniOverrideDelay.setStatus("mandatory")


class _MscARtgPnniReElectionInterval_Type(Unsigned32):
    """Custom type mscARtgPnniReElectionInterval based on Unsigned32"""
    defaultValue = 15

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MscARtgPnniReElectionInterval_Type.__name__ = "Unsigned32"
_MscARtgPnniReElectionInterval_Object = MibTableColumn
mscARtgPnniReElectionInterval = _MscARtgPnniReElectionInterval_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 11, 1, 3),
    _MscARtgPnniReElectionInterval_Type()
)
mscARtgPnniReElectionInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscARtgPnniReElectionInterval.setStatus("mandatory")
_MscARtgPnniHlParmsTable_Object = MibTable
mscARtgPnniHlParmsTable = _MscARtgPnniHlParmsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 12)
)
if mibBuilder.loadTexts:
    mscARtgPnniHlParmsTable.setStatus("mandatory")
_MscARtgPnniHlParmsEntry_Object = MibTableRow
mscARtgPnniHlParmsEntry = _MscARtgPnniHlParmsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 12, 1)
)
mscARtgPnniHlParmsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscARtgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscARtgPnniIndex"),
)
if mibBuilder.loadTexts:
    mscARtgPnniHlParmsEntry.setStatus("mandatory")


class _MscARtgPnniHelloHoldDown_Type(FixedPoint1):
    """Custom type mscARtgPnniHelloHoldDown based on FixedPoint1"""
    defaultValue = 10

    subtypeSpec = FixedPoint1.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 655350),
    )


_MscARtgPnniHelloHoldDown_Type.__name__ = "FixedPoint1"
_MscARtgPnniHelloHoldDown_Object = MibTableColumn
mscARtgPnniHelloHoldDown = _MscARtgPnniHelloHoldDown_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 12, 1, 1),
    _MscARtgPnniHelloHoldDown_Type()
)
mscARtgPnniHelloHoldDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscARtgPnniHelloHoldDown.setStatus("mandatory")


class _MscARtgPnniHelloInterval_Type(Unsigned32):
    """Custom type mscARtgPnniHelloInterval based on Unsigned32"""
    defaultValue = 15

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MscARtgPnniHelloInterval_Type.__name__ = "Unsigned32"
_MscARtgPnniHelloInterval_Object = MibTableColumn
mscARtgPnniHelloInterval = _MscARtgPnniHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 12, 1, 2),
    _MscARtgPnniHelloInterval_Type()
)
mscARtgPnniHelloInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscARtgPnniHelloInterval.setStatus("mandatory")


class _MscARtgPnniHelloInactivityFactor_Type(Unsigned32):
    """Custom type mscARtgPnniHelloInactivityFactor based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MscARtgPnniHelloInactivityFactor_Type.__name__ = "Unsigned32"
_MscARtgPnniHelloInactivityFactor_Object = MibTableColumn
mscARtgPnniHelloInactivityFactor = _MscARtgPnniHelloInactivityFactor_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 12, 1, 3),
    _MscARtgPnniHelloInactivityFactor_Type()
)
mscARtgPnniHelloInactivityFactor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscARtgPnniHelloInactivityFactor.setStatus("mandatory")
_MscARtgPnniPtseParmsTable_Object = MibTable
mscARtgPnniPtseParmsTable = _MscARtgPnniPtseParmsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 13)
)
if mibBuilder.loadTexts:
    mscARtgPnniPtseParmsTable.setStatus("mandatory")
_MscARtgPnniPtseParmsEntry_Object = MibTableRow
mscARtgPnniPtseParmsEntry = _MscARtgPnniPtseParmsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 13, 1)
)
mscARtgPnniPtseParmsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscARtgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscARtgPnniIndex"),
)
if mibBuilder.loadTexts:
    mscARtgPnniPtseParmsEntry.setStatus("mandatory")


class _MscARtgPnniPtseHoldDown_Type(FixedPoint1):
    """Custom type mscARtgPnniPtseHoldDown based on FixedPoint1"""
    defaultValue = 10

    subtypeSpec = FixedPoint1.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 655350),
    )


_MscARtgPnniPtseHoldDown_Type.__name__ = "FixedPoint1"
_MscARtgPnniPtseHoldDown_Object = MibTableColumn
mscARtgPnniPtseHoldDown = _MscARtgPnniPtseHoldDown_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 13, 1, 1),
    _MscARtgPnniPtseHoldDown_Type()
)
mscARtgPnniPtseHoldDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscARtgPnniPtseHoldDown.setStatus("mandatory")


class _MscARtgPnniPtseRefreshInterval_Type(Unsigned32):
    """Custom type mscARtgPnniPtseRefreshInterval based on Unsigned32"""
    defaultValue = 1800

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 65535),
    )


_MscARtgPnniPtseRefreshInterval_Type.__name__ = "Unsigned32"
_MscARtgPnniPtseRefreshInterval_Object = MibTableColumn
mscARtgPnniPtseRefreshInterval = _MscARtgPnniPtseRefreshInterval_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 13, 1, 2),
    _MscARtgPnniPtseRefreshInterval_Type()
)
mscARtgPnniPtseRefreshInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscARtgPnniPtseRefreshInterval.setStatus("mandatory")


class _MscARtgPnniPtseLifetimeFactor_Type(Unsigned32):
    """Custom type mscARtgPnniPtseLifetimeFactor based on Unsigned32"""
    defaultValue = 200

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(101, 1000),
    )


_MscARtgPnniPtseLifetimeFactor_Type.__name__ = "Unsigned32"
_MscARtgPnniPtseLifetimeFactor_Object = MibTableColumn
mscARtgPnniPtseLifetimeFactor = _MscARtgPnniPtseLifetimeFactor_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 13, 1, 3),
    _MscARtgPnniPtseLifetimeFactor_Type()
)
mscARtgPnniPtseLifetimeFactor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscARtgPnniPtseLifetimeFactor.setStatus("mandatory")


class _MscARtgPnniRequestRxmtInterval_Type(Unsigned32):
    """Custom type mscARtgPnniRequestRxmtInterval based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MscARtgPnniRequestRxmtInterval_Type.__name__ = "Unsigned32"
_MscARtgPnniRequestRxmtInterval_Object = MibTableColumn
mscARtgPnniRequestRxmtInterval = _MscARtgPnniRequestRxmtInterval_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 13, 1, 4),
    _MscARtgPnniRequestRxmtInterval_Type()
)
mscARtgPnniRequestRxmtInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscARtgPnniRequestRxmtInterval.setStatus("mandatory")


class _MscARtgPnniPeerDelayedAckInterval_Type(FixedPoint1):
    """Custom type mscARtgPnniPeerDelayedAckInterval based on FixedPoint1"""
    defaultValue = 1

    subtypeSpec = FixedPoint1.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 655350),
    )


_MscARtgPnniPeerDelayedAckInterval_Type.__name__ = "FixedPoint1"
_MscARtgPnniPeerDelayedAckInterval_Object = MibTableColumn
mscARtgPnniPeerDelayedAckInterval = _MscARtgPnniPeerDelayedAckInterval_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 13, 1, 5),
    _MscARtgPnniPeerDelayedAckInterval_Type()
)
mscARtgPnniPeerDelayedAckInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscARtgPnniPeerDelayedAckInterval.setStatus("mandatory")
_MscARtgPnniThreshParmsTable_Object = MibTable
mscARtgPnniThreshParmsTable = _MscARtgPnniThreshParmsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 14)
)
if mibBuilder.loadTexts:
    mscARtgPnniThreshParmsTable.setStatus("mandatory")
_MscARtgPnniThreshParmsEntry_Object = MibTableRow
mscARtgPnniThreshParmsEntry = _MscARtgPnniThreshParmsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 14, 1)
)
mscARtgPnniThreshParmsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscARtgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscARtgPnniIndex"),
)
if mibBuilder.loadTexts:
    mscARtgPnniThreshParmsEntry.setStatus("mandatory")


class _MscARtgPnniAvcrMt_Type(Unsigned32):
    """Custom type mscARtgPnniAvcrMt based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_MscARtgPnniAvcrMt_Type.__name__ = "Unsigned32"
_MscARtgPnniAvcrMt_Object = MibTableColumn
mscARtgPnniAvcrMt = _MscARtgPnniAvcrMt_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 14, 1, 1),
    _MscARtgPnniAvcrMt_Type()
)
mscARtgPnniAvcrMt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscARtgPnniAvcrMt.setStatus("mandatory")


class _MscARtgPnniAvcrPm_Type(Unsigned32):
    """Custom type mscARtgPnniAvcrPm based on Unsigned32"""
    defaultValue = 50

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_MscARtgPnniAvcrPm_Type.__name__ = "Unsigned32"
_MscARtgPnniAvcrPm_Object = MibTableColumn
mscARtgPnniAvcrPm = _MscARtgPnniAvcrPm_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 14, 1, 2),
    _MscARtgPnniAvcrPm_Type()
)
mscARtgPnniAvcrPm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscARtgPnniAvcrPm.setStatus("mandatory")
_MscARtgPnniOperTable_Object = MibTable
mscARtgPnniOperTable = _MscARtgPnniOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 15)
)
if mibBuilder.loadTexts:
    mscARtgPnniOperTable.setStatus("mandatory")
_MscARtgPnniOperEntry_Object = MibTableRow
mscARtgPnniOperEntry = _MscARtgPnniOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 15, 1)
)
mscARtgPnniOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscARtgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscARtgPnniIndex"),
)
if mibBuilder.loadTexts:
    mscARtgPnniOperEntry.setStatus("mandatory")


class _MscARtgPnniTopologyMemoryExhaustion_Type(Integer32):
    """Custom type mscARtgPnniTopologyMemoryExhaustion based on Integer32"""
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


_MscARtgPnniTopologyMemoryExhaustion_Type.__name__ = "Integer32"
_MscARtgPnniTopologyMemoryExhaustion_Object = MibTableColumn
mscARtgPnniTopologyMemoryExhaustion = _MscARtgPnniTopologyMemoryExhaustion_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 15, 1, 2),
    _MscARtgPnniTopologyMemoryExhaustion_Type()
)
mscARtgPnniTopologyMemoryExhaustion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscARtgPnniTopologyMemoryExhaustion.setStatus("mandatory")
_MscARtgPnniStatsTable_Object = MibTable
mscARtgPnniStatsTable = _MscARtgPnniStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 16)
)
if mibBuilder.loadTexts:
    mscARtgPnniStatsTable.setStatus("mandatory")
_MscARtgPnniStatsEntry_Object = MibTableRow
mscARtgPnniStatsEntry = _MscARtgPnniStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 16, 1)
)
mscARtgPnniStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscARtgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscARtgPnniIndex"),
)
if mibBuilder.loadTexts:
    mscARtgPnniStatsEntry.setStatus("mandatory")
_MscARtgPnniSuccessfulRoutingAttempts_Type = Counter32
_MscARtgPnniSuccessfulRoutingAttempts_Object = MibTableColumn
mscARtgPnniSuccessfulRoutingAttempts = _MscARtgPnniSuccessfulRoutingAttempts_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 16, 1, 1),
    _MscARtgPnniSuccessfulRoutingAttempts_Type()
)
mscARtgPnniSuccessfulRoutingAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscARtgPnniSuccessfulRoutingAttempts.setStatus("mandatory")
_MscARtgPnniFailedRoutingAttempts_Type = Counter32
_MscARtgPnniFailedRoutingAttempts_Object = MibTableColumn
mscARtgPnniFailedRoutingAttempts = _MscARtgPnniFailedRoutingAttempts_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 16, 1, 2),
    _MscARtgPnniFailedRoutingAttempts_Type()
)
mscARtgPnniFailedRoutingAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscARtgPnniFailedRoutingAttempts.setStatus("mandatory")
_MscARtgPnniAlternateRoutingAttempts_Type = Counter32
_MscARtgPnniAlternateRoutingAttempts_Object = MibTableColumn
mscARtgPnniAlternateRoutingAttempts = _MscARtgPnniAlternateRoutingAttempts_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 16, 1, 3),
    _MscARtgPnniAlternateRoutingAttempts_Type()
)
mscARtgPnniAlternateRoutingAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscARtgPnniAlternateRoutingAttempts.setStatus("mandatory")
_MscARtgPnniOptMetricTable_Object = MibTable
mscARtgPnniOptMetricTable = _MscARtgPnniOptMetricTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 386)
)
if mibBuilder.loadTexts:
    mscARtgPnniOptMetricTable.setStatus("mandatory")
_MscARtgPnniOptMetricEntry_Object = MibTableRow
mscARtgPnniOptMetricEntry = _MscARtgPnniOptMetricEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 386, 1)
)
mscARtgPnniOptMetricEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscARtgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscARtgPnniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscARtgPnniOptMetricIndex"),
)
if mibBuilder.loadTexts:
    mscARtgPnniOptMetricEntry.setStatus("mandatory")


class _MscARtgPnniOptMetricIndex_Type(Integer32):
    """Custom type mscARtgPnniOptMetricIndex based on Integer32"""
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


_MscARtgPnniOptMetricIndex_Type.__name__ = "Integer32"
_MscARtgPnniOptMetricIndex_Object = MibTableColumn
mscARtgPnniOptMetricIndex = _MscARtgPnniOptMetricIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 386, 1, 1),
    _MscARtgPnniOptMetricIndex_Type()
)
mscARtgPnniOptMetricIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscARtgPnniOptMetricIndex.setStatus("mandatory")


class _MscARtgPnniOptMetricValue_Type(Integer32):
    """Custom type mscARtgPnniOptMetricValue based on Integer32"""
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


_MscARtgPnniOptMetricValue_Type.__name__ = "Integer32"
_MscARtgPnniOptMetricValue_Object = MibTableColumn
mscARtgPnniOptMetricValue = _MscARtgPnniOptMetricValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 3, 386, 1, 2),
    _MscARtgPnniOptMetricValue_Type()
)
mscARtgPnniOptMetricValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscARtgPnniOptMetricValue.setStatus("mandatory")
_MscARtgStatsTable_Object = MibTable
mscARtgStatsTable = _MscARtgStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 10)
)
if mibBuilder.loadTexts:
    mscARtgStatsTable.setStatus("mandatory")
_MscARtgStatsEntry_Object = MibTableRow
mscARtgStatsEntry = _MscARtgStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 10, 1)
)
mscARtgStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscARtgIndex"),
)
if mibBuilder.loadTexts:
    mscARtgStatsEntry.setStatus("mandatory")
_MscARtgRoutingAttempts_Type = Counter32
_MscARtgRoutingAttempts_Object = MibTableColumn
mscARtgRoutingAttempts = _MscARtgRoutingAttempts_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 10, 1, 1),
    _MscARtgRoutingAttempts_Type()
)
mscARtgRoutingAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscARtgRoutingAttempts.setStatus("mandatory")
_MscARtgFailedRoutingAttempts_Type = Counter32
_MscARtgFailedRoutingAttempts_Object = MibTableColumn
mscARtgFailedRoutingAttempts = _MscARtgFailedRoutingAttempts_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 95, 10, 1, 2),
    _MscARtgFailedRoutingAttempts_Type()
)
mscARtgFailedRoutingAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscARtgFailedRoutingAttempts.setStatus("mandatory")
_MscAtmCR_ObjectIdentity = ObjectIdentity
mscAtmCR = _MscAtmCR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 113)
)
_MscAtmCRRowStatusTable_Object = MibTable
mscAtmCRRowStatusTable = _MscAtmCRRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 113, 1)
)
if mibBuilder.loadTexts:
    mscAtmCRRowStatusTable.setStatus("mandatory")
_MscAtmCRRowStatusEntry_Object = MibTableRow
mscAtmCRRowStatusEntry = _MscAtmCRRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 113, 1, 1)
)
mscAtmCRRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscAtmCRIndex"),
)
if mibBuilder.loadTexts:
    mscAtmCRRowStatusEntry.setStatus("mandatory")
_MscAtmCRRowStatus_Type = RowStatus
_MscAtmCRRowStatus_Object = MibTableColumn
mscAtmCRRowStatus = _MscAtmCRRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 113, 1, 1, 1),
    _MscAtmCRRowStatus_Type()
)
mscAtmCRRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmCRRowStatus.setStatus("mandatory")
_MscAtmCRComponentName_Type = DisplayString
_MscAtmCRComponentName_Object = MibTableColumn
mscAtmCRComponentName = _MscAtmCRComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 113, 1, 1, 2),
    _MscAtmCRComponentName_Type()
)
mscAtmCRComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmCRComponentName.setStatus("mandatory")
_MscAtmCRStorageType_Type = StorageType
_MscAtmCRStorageType_Object = MibTableColumn
mscAtmCRStorageType = _MscAtmCRStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 113, 1, 1, 4),
    _MscAtmCRStorageType_Type()
)
mscAtmCRStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmCRStorageType.setStatus("mandatory")
_MscAtmCRIndex_Type = NonReplicated
_MscAtmCRIndex_Object = MibTableColumn
mscAtmCRIndex = _MscAtmCRIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 113, 1, 1, 10),
    _MscAtmCRIndex_Type()
)
mscAtmCRIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAtmCRIndex.setStatus("mandatory")
_MscAtmCRDna_ObjectIdentity = ObjectIdentity
mscAtmCRDna = _MscAtmCRDna_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 113, 2)
)
_MscAtmCRDnaRowStatusTable_Object = MibTable
mscAtmCRDnaRowStatusTable = _MscAtmCRDnaRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 113, 2, 1)
)
if mibBuilder.loadTexts:
    mscAtmCRDnaRowStatusTable.setStatus("mandatory")
_MscAtmCRDnaRowStatusEntry_Object = MibTableRow
mscAtmCRDnaRowStatusEntry = _MscAtmCRDnaRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 113, 2, 1, 1)
)
mscAtmCRDnaRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscAtmCRIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscAtmCRDnaIndex"),
)
if mibBuilder.loadTexts:
    mscAtmCRDnaRowStatusEntry.setStatus("mandatory")
_MscAtmCRDnaRowStatus_Type = RowStatus
_MscAtmCRDnaRowStatus_Object = MibTableColumn
mscAtmCRDnaRowStatus = _MscAtmCRDnaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 113, 2, 1, 1, 1),
    _MscAtmCRDnaRowStatus_Type()
)
mscAtmCRDnaRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmCRDnaRowStatus.setStatus("mandatory")
_MscAtmCRDnaComponentName_Type = DisplayString
_MscAtmCRDnaComponentName_Object = MibTableColumn
mscAtmCRDnaComponentName = _MscAtmCRDnaComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 113, 2, 1, 1, 2),
    _MscAtmCRDnaComponentName_Type()
)
mscAtmCRDnaComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmCRDnaComponentName.setStatus("mandatory")
_MscAtmCRDnaStorageType_Type = StorageType
_MscAtmCRDnaStorageType_Object = MibTableColumn
mscAtmCRDnaStorageType = _MscAtmCRDnaStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 113, 2, 1, 1, 4),
    _MscAtmCRDnaStorageType_Type()
)
mscAtmCRDnaStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmCRDnaStorageType.setStatus("mandatory")


class _MscAtmCRDnaIndex_Type(AsciiStringIndex):
    """Custom type mscAtmCRDnaIndex based on AsciiStringIndex"""
    subtypeSpec = AsciiStringIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_MscAtmCRDnaIndex_Type.__name__ = "AsciiStringIndex"
_MscAtmCRDnaIndex_Object = MibTableColumn
mscAtmCRDnaIndex = _MscAtmCRDnaIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 113, 2, 1, 1, 10),
    _MscAtmCRDnaIndex_Type()
)
mscAtmCRDnaIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAtmCRDnaIndex.setStatus("mandatory")
_MscAtmCRDnaDestinationNameTable_Object = MibTable
mscAtmCRDnaDestinationNameTable = _MscAtmCRDnaDestinationNameTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 113, 2, 289)
)
if mibBuilder.loadTexts:
    mscAtmCRDnaDestinationNameTable.setStatus("obsolete")
_MscAtmCRDnaDestinationNameEntry_Object = MibTableRow
mscAtmCRDnaDestinationNameEntry = _MscAtmCRDnaDestinationNameEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 113, 2, 289, 1)
)
mscAtmCRDnaDestinationNameEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscAtmCRIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscAtmCRDnaIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscAtmCRDnaDestinationNameValue"),
)
if mibBuilder.loadTexts:
    mscAtmCRDnaDestinationNameEntry.setStatus("obsolete")
_MscAtmCRDnaDestinationNameValue_Type = RowPointer
_MscAtmCRDnaDestinationNameValue_Object = MibTableColumn
mscAtmCRDnaDestinationNameValue = _MscAtmCRDnaDestinationNameValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 113, 2, 289, 1, 1),
    _MscAtmCRDnaDestinationNameValue_Type()
)
mscAtmCRDnaDestinationNameValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmCRDnaDestinationNameValue.setStatus("obsolete")
_MscAtmCRProvTable_Object = MibTable
mscAtmCRProvTable = _MscAtmCRProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 113, 10)
)
if mibBuilder.loadTexts:
    mscAtmCRProvTable.setStatus("mandatory")
_MscAtmCRProvEntry_Object = MibTableRow
mscAtmCRProvEntry = _MscAtmCRProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 113, 10, 1)
)
mscAtmCRProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscAtmCRIndex"),
)
if mibBuilder.loadTexts:
    mscAtmCRProvEntry.setStatus("mandatory")


class _MscAtmCRNodeAddress_Type(AsciiString):
    """Custom type mscAtmCRNodeAddress based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(26, 26),
    )


_MscAtmCRNodeAddress_Type.__name__ = "AsciiString"
_MscAtmCRNodeAddress_Object = MibTableColumn
mscAtmCRNodeAddress = _MscAtmCRNodeAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 113, 10, 1, 1),
    _MscAtmCRNodeAddress_Type()
)
mscAtmCRNodeAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmCRNodeAddress.setStatus("obsolete")
_MscAtmCRStatsTable_Object = MibTable
mscAtmCRStatsTable = _MscAtmCRStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 113, 11)
)
if mibBuilder.loadTexts:
    mscAtmCRStatsTable.setStatus("obsolete")
_MscAtmCRStatsEntry_Object = MibTableRow
mscAtmCRStatsEntry = _MscAtmCRStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 113, 11, 1)
)
mscAtmCRStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscAtmCRIndex"),
)
if mibBuilder.loadTexts:
    mscAtmCRStatsEntry.setStatus("obsolete")
_MscAtmCRCallsRouted_Type = Counter32
_MscAtmCRCallsRouted_Object = MibTableColumn
mscAtmCRCallsRouted = _MscAtmCRCallsRouted_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 113, 11, 1, 1),
    _MscAtmCRCallsRouted_Type()
)
mscAtmCRCallsRouted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmCRCallsRouted.setStatus("obsolete")
_MscAtmCRCallsFailed_Type = Counter32
_MscAtmCRCallsFailed_Object = MibTableColumn
mscAtmCRCallsFailed = _MscAtmCRCallsFailed_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 113, 11, 1, 2),
    _MscAtmCRCallsFailed_Type()
)
mscAtmCRCallsFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmCRCallsFailed.setStatus("obsolete")
_MscAtmIfVpcSrc_ObjectIdentity = ObjectIdentity
mscAtmIfVpcSrc = _MscAtmIfVpcSrc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 4, 6)
)
_MscAtmIfVpcSrcRowStatusTable_Object = MibTable
mscAtmIfVpcSrcRowStatusTable = _MscAtmIfVpcSrcRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 4, 6, 1)
)
if mibBuilder.loadTexts:
    mscAtmIfVpcSrcRowStatusTable.setStatus("mandatory")
_MscAtmIfVpcSrcRowStatusEntry_Object = MibTableRow
mscAtmIfVpcSrcRowStatusEntry = _MscAtmIfVpcSrcRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 4, 6, 1, 1)
)
mscAtmIfVpcSrcRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVpcIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscAtmIfVpcSrcIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfVpcSrcRowStatusEntry.setStatus("mandatory")
_MscAtmIfVpcSrcRowStatus_Type = RowStatus
_MscAtmIfVpcSrcRowStatus_Object = MibTableColumn
mscAtmIfVpcSrcRowStatus = _MscAtmIfVpcSrcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 4, 6, 1, 1, 1),
    _MscAtmIfVpcSrcRowStatus_Type()
)
mscAtmIfVpcSrcRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVpcSrcRowStatus.setStatus("mandatory")
_MscAtmIfVpcSrcComponentName_Type = DisplayString
_MscAtmIfVpcSrcComponentName_Object = MibTableColumn
mscAtmIfVpcSrcComponentName = _MscAtmIfVpcSrcComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 4, 6, 1, 1, 2),
    _MscAtmIfVpcSrcComponentName_Type()
)
mscAtmIfVpcSrcComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVpcSrcComponentName.setStatus("mandatory")
_MscAtmIfVpcSrcStorageType_Type = StorageType
_MscAtmIfVpcSrcStorageType_Object = MibTableColumn
mscAtmIfVpcSrcStorageType = _MscAtmIfVpcSrcStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 4, 6, 1, 1, 4),
    _MscAtmIfVpcSrcStorageType_Type()
)
mscAtmIfVpcSrcStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVpcSrcStorageType.setStatus("mandatory")
_MscAtmIfVpcSrcIndex_Type = NonReplicated
_MscAtmIfVpcSrcIndex_Object = MibTableColumn
mscAtmIfVpcSrcIndex = _MscAtmIfVpcSrcIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 4, 6, 1, 1, 10),
    _MscAtmIfVpcSrcIndex_Type()
)
mscAtmIfVpcSrcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAtmIfVpcSrcIndex.setStatus("mandatory")
_MscAtmIfVpcSrcProvTable_Object = MibTable
mscAtmIfVpcSrcProvTable = _MscAtmIfVpcSrcProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 4, 6, 10)
)
if mibBuilder.loadTexts:
    mscAtmIfVpcSrcProvTable.setStatus("mandatory")
_MscAtmIfVpcSrcProvEntry_Object = MibTableRow
mscAtmIfVpcSrcProvEntry = _MscAtmIfVpcSrcProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 4, 6, 10, 1)
)
mscAtmIfVpcSrcProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVpcIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscAtmIfVpcSrcIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfVpcSrcProvEntry.setStatus("mandatory")


class _MscAtmIfVpcSrcCallingAddress_Type(HexString):
    """Custom type mscAtmIfVpcSrcCallingAddress based on HexString"""
    defaultHexValue = ""

    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_MscAtmIfVpcSrcCallingAddress_Type.__name__ = "HexString"
_MscAtmIfVpcSrcCallingAddress_Object = MibTableColumn
mscAtmIfVpcSrcCallingAddress = _MscAtmIfVpcSrcCallingAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 4, 6, 10, 1, 1),
    _MscAtmIfVpcSrcCallingAddress_Type()
)
mscAtmIfVpcSrcCallingAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVpcSrcCallingAddress.setStatus("mandatory")


class _MscAtmIfVpcSrcCalledAddress_Type(HexString):
    """Custom type mscAtmIfVpcSrcCalledAddress based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_MscAtmIfVpcSrcCalledAddress_Type.__name__ = "HexString"
_MscAtmIfVpcSrcCalledAddress_Object = MibTableColumn
mscAtmIfVpcSrcCalledAddress = _MscAtmIfVpcSrcCalledAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 4, 6, 10, 1, 2),
    _MscAtmIfVpcSrcCalledAddress_Type()
)
mscAtmIfVpcSrcCalledAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVpcSrcCalledAddress.setStatus("mandatory")


class _MscAtmIfVpcSrcCalledVpi_Type(Unsigned32):
    """Custom type mscAtmIfVpcSrcCalledVpi based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_MscAtmIfVpcSrcCalledVpi_Type.__name__ = "Unsigned32"
_MscAtmIfVpcSrcCalledVpi_Object = MibTableColumn
mscAtmIfVpcSrcCalledVpi = _MscAtmIfVpcSrcCalledVpi_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 4, 6, 10, 1, 3),
    _MscAtmIfVpcSrcCalledVpi_Type()
)
mscAtmIfVpcSrcCalledVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVpcSrcCalledVpi.setStatus("mandatory")
_MscAtmIfVpcSrcOperTable_Object = MibTable
mscAtmIfVpcSrcOperTable = _MscAtmIfVpcSrcOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 4, 6, 11)
)
if mibBuilder.loadTexts:
    mscAtmIfVpcSrcOperTable.setStatus("mandatory")
_MscAtmIfVpcSrcOperEntry_Object = MibTableRow
mscAtmIfVpcSrcOperEntry = _MscAtmIfVpcSrcOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 4, 6, 11, 1)
)
mscAtmIfVpcSrcOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVpcIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscAtmIfVpcSrcIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfVpcSrcOperEntry.setStatus("mandatory")


class _MscAtmIfVpcSrcState_Type(Integer32):
    """Custom type mscAtmIfVpcSrcState based on Integer32"""
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


_MscAtmIfVpcSrcState_Type.__name__ = "Integer32"
_MscAtmIfVpcSrcState_Object = MibTableColumn
mscAtmIfVpcSrcState = _MscAtmIfVpcSrcState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 4, 6, 11, 1, 1),
    _MscAtmIfVpcSrcState_Type()
)
mscAtmIfVpcSrcState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVpcSrcState.setStatus("mandatory")
_MscAtmIfVpcSrcRetryCount_Type = Counter32
_MscAtmIfVpcSrcRetryCount_Object = MibTableColumn
mscAtmIfVpcSrcRetryCount = _MscAtmIfVpcSrcRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 4, 6, 11, 1, 2),
    _MscAtmIfVpcSrcRetryCount_Type()
)
mscAtmIfVpcSrcRetryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVpcSrcRetryCount.setStatus("mandatory")


class _MscAtmIfVpcSrcLastFailureCauseCode_Type(Unsigned32):
    """Custom type mscAtmIfVpcSrcLastFailureCauseCode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscAtmIfVpcSrcLastFailureCauseCode_Type.__name__ = "Unsigned32"
_MscAtmIfVpcSrcLastFailureCauseCode_Object = MibTableColumn
mscAtmIfVpcSrcLastFailureCauseCode = _MscAtmIfVpcSrcLastFailureCauseCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 4, 6, 11, 1, 3),
    _MscAtmIfVpcSrcLastFailureCauseCode_Type()
)
mscAtmIfVpcSrcLastFailureCauseCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVpcSrcLastFailureCauseCode.setStatus("mandatory")


class _MscAtmIfVpcSrcLastFailureDiagCode_Type(AsciiString):
    """Custom type mscAtmIfVpcSrcLastFailureDiagCode based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_MscAtmIfVpcSrcLastFailureDiagCode_Type.__name__ = "AsciiString"
_MscAtmIfVpcSrcLastFailureDiagCode_Object = MibTableColumn
mscAtmIfVpcSrcLastFailureDiagCode = _MscAtmIfVpcSrcLastFailureDiagCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 4, 6, 11, 1, 4),
    _MscAtmIfVpcSrcLastFailureDiagCode_Type()
)
mscAtmIfVpcSrcLastFailureDiagCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVpcSrcLastFailureDiagCode.setStatus("mandatory")
_MscAtmIfVpcRp_ObjectIdentity = ObjectIdentity
mscAtmIfVpcRp = _MscAtmIfVpcRp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 4, 7)
)
_MscAtmIfVpcRpRowStatusTable_Object = MibTable
mscAtmIfVpcRpRowStatusTable = _MscAtmIfVpcRpRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 4, 7, 1)
)
if mibBuilder.loadTexts:
    mscAtmIfVpcRpRowStatusTable.setStatus("mandatory")
_MscAtmIfVpcRpRowStatusEntry_Object = MibTableRow
mscAtmIfVpcRpRowStatusEntry = _MscAtmIfVpcRpRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 4, 7, 1, 1)
)
mscAtmIfVpcRpRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVpcIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscAtmIfVpcRpIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfVpcRpRowStatusEntry.setStatus("mandatory")
_MscAtmIfVpcRpRowStatus_Type = RowStatus
_MscAtmIfVpcRpRowStatus_Object = MibTableColumn
mscAtmIfVpcRpRowStatus = _MscAtmIfVpcRpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 4, 7, 1, 1, 1),
    _MscAtmIfVpcRpRowStatus_Type()
)
mscAtmIfVpcRpRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVpcRpRowStatus.setStatus("mandatory")
_MscAtmIfVpcRpComponentName_Type = DisplayString
_MscAtmIfVpcRpComponentName_Object = MibTableColumn
mscAtmIfVpcRpComponentName = _MscAtmIfVpcRpComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 4, 7, 1, 1, 2),
    _MscAtmIfVpcRpComponentName_Type()
)
mscAtmIfVpcRpComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVpcRpComponentName.setStatus("mandatory")
_MscAtmIfVpcRpStorageType_Type = StorageType
_MscAtmIfVpcRpStorageType_Object = MibTableColumn
mscAtmIfVpcRpStorageType = _MscAtmIfVpcRpStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 4, 7, 1, 1, 4),
    _MscAtmIfVpcRpStorageType_Type()
)
mscAtmIfVpcRpStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVpcRpStorageType.setStatus("mandatory")
_MscAtmIfVpcRpIndex_Type = NonReplicated
_MscAtmIfVpcRpIndex_Object = MibTableColumn
mscAtmIfVpcRpIndex = _MscAtmIfVpcRpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 4, 7, 1, 1, 10),
    _MscAtmIfVpcRpIndex_Type()
)
mscAtmIfVpcRpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAtmIfVpcRpIndex.setStatus("mandatory")
_MscAtmIfVpcRpOperTable_Object = MibTable
mscAtmIfVpcRpOperTable = _MscAtmIfVpcRpOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 4, 7, 10)
)
if mibBuilder.loadTexts:
    mscAtmIfVpcRpOperTable.setStatus("mandatory")
_MscAtmIfVpcRpOperEntry_Object = MibTableRow
mscAtmIfVpcRpOperEntry = _MscAtmIfVpcRpOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 4, 7, 10, 1)
)
mscAtmIfVpcRpOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVpcIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscAtmIfVpcRpIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfVpcRpOperEntry.setStatus("mandatory")
_MscAtmIfVpcRpNextHop_Type = RowPointer
_MscAtmIfVpcRpNextHop_Object = MibTableColumn
mscAtmIfVpcRpNextHop = _MscAtmIfVpcRpNextHop_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 4, 7, 10, 1, 1),
    _MscAtmIfVpcRpNextHop_Type()
)
mscAtmIfVpcRpNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVpcRpNextHop.setStatus("obsolete")
_MscAtmIfVpcRpNextHopsTable_Object = MibTable
mscAtmIfVpcRpNextHopsTable = _MscAtmIfVpcRpNextHopsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 4, 7, 430)
)
if mibBuilder.loadTexts:
    mscAtmIfVpcRpNextHopsTable.setStatus("mandatory")
_MscAtmIfVpcRpNextHopsEntry_Object = MibTableRow
mscAtmIfVpcRpNextHopsEntry = _MscAtmIfVpcRpNextHopsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 4, 7, 430, 1)
)
mscAtmIfVpcRpNextHopsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVpcIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscAtmIfVpcRpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscAtmIfVpcRpNextHopsValue"),
)
if mibBuilder.loadTexts:
    mscAtmIfVpcRpNextHopsEntry.setStatus("mandatory")
_MscAtmIfVpcRpNextHopsValue_Type = RowPointer
_MscAtmIfVpcRpNextHopsValue_Object = MibTableColumn
mscAtmIfVpcRpNextHopsValue = _MscAtmIfVpcRpNextHopsValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 4, 7, 430, 1, 1),
    _MscAtmIfVpcRpNextHopsValue_Type()
)
mscAtmIfVpcRpNextHopsValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVpcRpNextHopsValue.setStatus("mandatory")
_MscAtmIfVpcDst_ObjectIdentity = ObjectIdentity
mscAtmIfVpcDst = _MscAtmIfVpcDst_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 4, 8)
)
_MscAtmIfVpcDstRowStatusTable_Object = MibTable
mscAtmIfVpcDstRowStatusTable = _MscAtmIfVpcDstRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 4, 8, 1)
)
if mibBuilder.loadTexts:
    mscAtmIfVpcDstRowStatusTable.setStatus("mandatory")
_MscAtmIfVpcDstRowStatusEntry_Object = MibTableRow
mscAtmIfVpcDstRowStatusEntry = _MscAtmIfVpcDstRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 4, 8, 1, 1)
)
mscAtmIfVpcDstRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVpcIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscAtmIfVpcDstIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfVpcDstRowStatusEntry.setStatus("mandatory")
_MscAtmIfVpcDstRowStatus_Type = RowStatus
_MscAtmIfVpcDstRowStatus_Object = MibTableColumn
mscAtmIfVpcDstRowStatus = _MscAtmIfVpcDstRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 4, 8, 1, 1, 1),
    _MscAtmIfVpcDstRowStatus_Type()
)
mscAtmIfVpcDstRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVpcDstRowStatus.setStatus("mandatory")
_MscAtmIfVpcDstComponentName_Type = DisplayString
_MscAtmIfVpcDstComponentName_Object = MibTableColumn
mscAtmIfVpcDstComponentName = _MscAtmIfVpcDstComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 4, 8, 1, 1, 2),
    _MscAtmIfVpcDstComponentName_Type()
)
mscAtmIfVpcDstComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVpcDstComponentName.setStatus("mandatory")
_MscAtmIfVpcDstStorageType_Type = StorageType
_MscAtmIfVpcDstStorageType_Object = MibTableColumn
mscAtmIfVpcDstStorageType = _MscAtmIfVpcDstStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 4, 8, 1, 1, 4),
    _MscAtmIfVpcDstStorageType_Type()
)
mscAtmIfVpcDstStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVpcDstStorageType.setStatus("mandatory")
_MscAtmIfVpcDstIndex_Type = NonReplicated
_MscAtmIfVpcDstIndex_Object = MibTableColumn
mscAtmIfVpcDstIndex = _MscAtmIfVpcDstIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 4, 8, 1, 1, 10),
    _MscAtmIfVpcDstIndex_Type()
)
mscAtmIfVpcDstIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAtmIfVpcDstIndex.setStatus("mandatory")
_MscAtmIfVpcDstOperTable_Object = MibTable
mscAtmIfVpcDstOperTable = _MscAtmIfVpcDstOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 4, 8, 10)
)
if mibBuilder.loadTexts:
    mscAtmIfVpcDstOperTable.setStatus("mandatory")
_MscAtmIfVpcDstOperEntry_Object = MibTableRow
mscAtmIfVpcDstOperEntry = _MscAtmIfVpcDstOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 4, 8, 10, 1)
)
mscAtmIfVpcDstOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVpcIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscAtmIfVpcDstIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfVpcDstOperEntry.setStatus("mandatory")


class _MscAtmIfVpcDstCalledAddress_Type(HexString):
    """Custom type mscAtmIfVpcDstCalledAddress based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_MscAtmIfVpcDstCalledAddress_Type.__name__ = "HexString"
_MscAtmIfVpcDstCalledAddress_Object = MibTableColumn
mscAtmIfVpcDstCalledAddress = _MscAtmIfVpcDstCalledAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 4, 8, 10, 1, 1),
    _MscAtmIfVpcDstCalledAddress_Type()
)
mscAtmIfVpcDstCalledAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVpcDstCalledAddress.setStatus("mandatory")


class _MscAtmIfVpcDstCallingAddress_Type(AsciiString):
    """Custom type mscAtmIfVpcDstCallingAddress based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 40),
    )


_MscAtmIfVpcDstCallingAddress_Type.__name__ = "AsciiString"
_MscAtmIfVpcDstCallingAddress_Object = MibTableColumn
mscAtmIfVpcDstCallingAddress = _MscAtmIfVpcDstCallingAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 4, 8, 10, 1, 2),
    _MscAtmIfVpcDstCallingAddress_Type()
)
mscAtmIfVpcDstCallingAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVpcDstCallingAddress.setStatus("mandatory")


class _MscAtmIfVpcDstCallingVpi_Type(AsciiString):
    """Custom type mscAtmIfVpcDstCallingVpi based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 7),
    )


_MscAtmIfVpcDstCallingVpi_Type.__name__ = "AsciiString"
_MscAtmIfVpcDstCallingVpi_Object = MibTableColumn
mscAtmIfVpcDstCallingVpi = _MscAtmIfVpcDstCallingVpi_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 4, 8, 10, 1, 3),
    _MscAtmIfVpcDstCallingVpi_Type()
)
mscAtmIfVpcDstCallingVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVpcDstCallingVpi.setStatus("mandatory")
_MscAtmIfVccSrc_ObjectIdentity = ObjectIdentity
mscAtmIfVccSrc = _MscAtmIfVccSrc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 5, 8)
)
_MscAtmIfVccSrcRowStatusTable_Object = MibTable
mscAtmIfVccSrcRowStatusTable = _MscAtmIfVccSrcRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 5, 8, 1)
)
if mibBuilder.loadTexts:
    mscAtmIfVccSrcRowStatusTable.setStatus("mandatory")
_MscAtmIfVccSrcRowStatusEntry_Object = MibTableRow
mscAtmIfVccSrcRowStatusEntry = _MscAtmIfVccSrcRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 5, 8, 1, 1)
)
mscAtmIfVccSrcRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVccIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscAtmIfVccSrcIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfVccSrcRowStatusEntry.setStatus("mandatory")
_MscAtmIfVccSrcRowStatus_Type = RowStatus
_MscAtmIfVccSrcRowStatus_Object = MibTableColumn
mscAtmIfVccSrcRowStatus = _MscAtmIfVccSrcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 5, 8, 1, 1, 1),
    _MscAtmIfVccSrcRowStatus_Type()
)
mscAtmIfVccSrcRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVccSrcRowStatus.setStatus("mandatory")
_MscAtmIfVccSrcComponentName_Type = DisplayString
_MscAtmIfVccSrcComponentName_Object = MibTableColumn
mscAtmIfVccSrcComponentName = _MscAtmIfVccSrcComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 5, 8, 1, 1, 2),
    _MscAtmIfVccSrcComponentName_Type()
)
mscAtmIfVccSrcComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVccSrcComponentName.setStatus("mandatory")
_MscAtmIfVccSrcStorageType_Type = StorageType
_MscAtmIfVccSrcStorageType_Object = MibTableColumn
mscAtmIfVccSrcStorageType = _MscAtmIfVccSrcStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 5, 8, 1, 1, 4),
    _MscAtmIfVccSrcStorageType_Type()
)
mscAtmIfVccSrcStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVccSrcStorageType.setStatus("mandatory")
_MscAtmIfVccSrcIndex_Type = NonReplicated
_MscAtmIfVccSrcIndex_Object = MibTableColumn
mscAtmIfVccSrcIndex = _MscAtmIfVccSrcIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 5, 8, 1, 1, 10),
    _MscAtmIfVccSrcIndex_Type()
)
mscAtmIfVccSrcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAtmIfVccSrcIndex.setStatus("mandatory")
_MscAtmIfVccSrcProvTable_Object = MibTable
mscAtmIfVccSrcProvTable = _MscAtmIfVccSrcProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 5, 8, 10)
)
if mibBuilder.loadTexts:
    mscAtmIfVccSrcProvTable.setStatus("mandatory")
_MscAtmIfVccSrcProvEntry_Object = MibTableRow
mscAtmIfVccSrcProvEntry = _MscAtmIfVccSrcProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 5, 8, 10, 1)
)
mscAtmIfVccSrcProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVccIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscAtmIfVccSrcIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfVccSrcProvEntry.setStatus("mandatory")


class _MscAtmIfVccSrcRemoteAddress_Type(HexString):
    """Custom type mscAtmIfVccSrcRemoteAddress based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_MscAtmIfVccSrcRemoteAddress_Type.__name__ = "HexString"
_MscAtmIfVccSrcRemoteAddress_Object = MibTableColumn
mscAtmIfVccSrcRemoteAddress = _MscAtmIfVccSrcRemoteAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 5, 8, 10, 1, 1),
    _MscAtmIfVccSrcRemoteAddress_Type()
)
mscAtmIfVccSrcRemoteAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVccSrcRemoteAddress.setStatus("obsolete")


class _MscAtmIfVccSrcRemoteVpiVci_Type(IntegerSequence):
    """Custom type mscAtmIfVccSrcRemoteVpiVci based on IntegerSequence"""
    subtypeSpec = IntegerSequence.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 9),
    )


_MscAtmIfVccSrcRemoteVpiVci_Type.__name__ = "IntegerSequence"
_MscAtmIfVccSrcRemoteVpiVci_Object = MibTableColumn
mscAtmIfVccSrcRemoteVpiVci = _MscAtmIfVccSrcRemoteVpiVci_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 5, 8, 10, 1, 2),
    _MscAtmIfVccSrcRemoteVpiVci_Type()
)
mscAtmIfVccSrcRemoteVpiVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVccSrcRemoteVpiVci.setStatus("obsolete")


class _MscAtmIfVccSrcCallingAddress_Type(HexString):
    """Custom type mscAtmIfVccSrcCallingAddress based on HexString"""
    defaultHexValue = ""

    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_MscAtmIfVccSrcCallingAddress_Type.__name__ = "HexString"
_MscAtmIfVccSrcCallingAddress_Object = MibTableColumn
mscAtmIfVccSrcCallingAddress = _MscAtmIfVccSrcCallingAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 5, 8, 10, 1, 3),
    _MscAtmIfVccSrcCallingAddress_Type()
)
mscAtmIfVccSrcCallingAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVccSrcCallingAddress.setStatus("mandatory")


class _MscAtmIfVccSrcCalledAddress_Type(HexString):
    """Custom type mscAtmIfVccSrcCalledAddress based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_MscAtmIfVccSrcCalledAddress_Type.__name__ = "HexString"
_MscAtmIfVccSrcCalledAddress_Object = MibTableColumn
mscAtmIfVccSrcCalledAddress = _MscAtmIfVccSrcCalledAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 5, 8, 10, 1, 4),
    _MscAtmIfVccSrcCalledAddress_Type()
)
mscAtmIfVccSrcCalledAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVccSrcCalledAddress.setStatus("mandatory")


class _MscAtmIfVccSrcCalledVpiVci_Type(IntegerSequence):
    """Custom type mscAtmIfVccSrcCalledVpiVci based on IntegerSequence"""
    subtypeSpec = IntegerSequence.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 10),
    )


_MscAtmIfVccSrcCalledVpiVci_Type.__name__ = "IntegerSequence"
_MscAtmIfVccSrcCalledVpiVci_Object = MibTableColumn
mscAtmIfVccSrcCalledVpiVci = _MscAtmIfVccSrcCalledVpiVci_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 5, 8, 10, 1, 5),
    _MscAtmIfVccSrcCalledVpiVci_Type()
)
mscAtmIfVccSrcCalledVpiVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVccSrcCalledVpiVci.setStatus("mandatory")
_MscAtmIfVccSrcOperTable_Object = MibTable
mscAtmIfVccSrcOperTable = _MscAtmIfVccSrcOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 5, 8, 11)
)
if mibBuilder.loadTexts:
    mscAtmIfVccSrcOperTable.setStatus("mandatory")
_MscAtmIfVccSrcOperEntry_Object = MibTableRow
mscAtmIfVccSrcOperEntry = _MscAtmIfVccSrcOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 5, 8, 11, 1)
)
mscAtmIfVccSrcOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVccIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscAtmIfVccSrcIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfVccSrcOperEntry.setStatus("mandatory")


class _MscAtmIfVccSrcState_Type(Integer32):
    """Custom type mscAtmIfVccSrcState based on Integer32"""
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


_MscAtmIfVccSrcState_Type.__name__ = "Integer32"
_MscAtmIfVccSrcState_Object = MibTableColumn
mscAtmIfVccSrcState = _MscAtmIfVccSrcState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 5, 8, 11, 1, 1),
    _MscAtmIfVccSrcState_Type()
)
mscAtmIfVccSrcState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVccSrcState.setStatus("mandatory")
_MscAtmIfVccSrcRetryCount_Type = Counter32
_MscAtmIfVccSrcRetryCount_Object = MibTableColumn
mscAtmIfVccSrcRetryCount = _MscAtmIfVccSrcRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 5, 8, 11, 1, 2),
    _MscAtmIfVccSrcRetryCount_Type()
)
mscAtmIfVccSrcRetryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVccSrcRetryCount.setStatus("mandatory")


class _MscAtmIfVccSrcLastFailureCauseCode_Type(Unsigned32):
    """Custom type mscAtmIfVccSrcLastFailureCauseCode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscAtmIfVccSrcLastFailureCauseCode_Type.__name__ = "Unsigned32"
_MscAtmIfVccSrcLastFailureCauseCode_Object = MibTableColumn
mscAtmIfVccSrcLastFailureCauseCode = _MscAtmIfVccSrcLastFailureCauseCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 5, 8, 11, 1, 3),
    _MscAtmIfVccSrcLastFailureCauseCode_Type()
)
mscAtmIfVccSrcLastFailureCauseCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVccSrcLastFailureCauseCode.setStatus("mandatory")


class _MscAtmIfVccSrcLastFailureDiagCode_Type(AsciiString):
    """Custom type mscAtmIfVccSrcLastFailureDiagCode based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_MscAtmIfVccSrcLastFailureDiagCode_Type.__name__ = "AsciiString"
_MscAtmIfVccSrcLastFailureDiagCode_Object = MibTableColumn
mscAtmIfVccSrcLastFailureDiagCode = _MscAtmIfVccSrcLastFailureDiagCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 5, 8, 11, 1, 4),
    _MscAtmIfVccSrcLastFailureDiagCode_Type()
)
mscAtmIfVccSrcLastFailureDiagCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVccSrcLastFailureDiagCode.setStatus("mandatory")
_MscAtmIfVccEp_ObjectIdentity = ObjectIdentity
mscAtmIfVccEp = _MscAtmIfVccEp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 5, 9)
)
_MscAtmIfVccEpRowStatusTable_Object = MibTable
mscAtmIfVccEpRowStatusTable = _MscAtmIfVccEpRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 5, 9, 1)
)
if mibBuilder.loadTexts:
    mscAtmIfVccEpRowStatusTable.setStatus("mandatory")
_MscAtmIfVccEpRowStatusEntry_Object = MibTableRow
mscAtmIfVccEpRowStatusEntry = _MscAtmIfVccEpRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 5, 9, 1, 1)
)
mscAtmIfVccEpRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVccIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscAtmIfVccEpIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfVccEpRowStatusEntry.setStatus("mandatory")
_MscAtmIfVccEpRowStatus_Type = RowStatus
_MscAtmIfVccEpRowStatus_Object = MibTableColumn
mscAtmIfVccEpRowStatus = _MscAtmIfVccEpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 5, 9, 1, 1, 1),
    _MscAtmIfVccEpRowStatus_Type()
)
mscAtmIfVccEpRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVccEpRowStatus.setStatus("mandatory")
_MscAtmIfVccEpComponentName_Type = DisplayString
_MscAtmIfVccEpComponentName_Object = MibTableColumn
mscAtmIfVccEpComponentName = _MscAtmIfVccEpComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 5, 9, 1, 1, 2),
    _MscAtmIfVccEpComponentName_Type()
)
mscAtmIfVccEpComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVccEpComponentName.setStatus("mandatory")
_MscAtmIfVccEpStorageType_Type = StorageType
_MscAtmIfVccEpStorageType_Object = MibTableColumn
mscAtmIfVccEpStorageType = _MscAtmIfVccEpStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 5, 9, 1, 1, 4),
    _MscAtmIfVccEpStorageType_Type()
)
mscAtmIfVccEpStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVccEpStorageType.setStatus("mandatory")
_MscAtmIfVccEpIndex_Type = NonReplicated
_MscAtmIfVccEpIndex_Object = MibTableColumn
mscAtmIfVccEpIndex = _MscAtmIfVccEpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 5, 9, 1, 1, 10),
    _MscAtmIfVccEpIndex_Type()
)
mscAtmIfVccEpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAtmIfVccEpIndex.setStatus("mandatory")
_MscAtmIfVccEpOperTable_Object = MibTable
mscAtmIfVccEpOperTable = _MscAtmIfVccEpOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 5, 9, 10)
)
if mibBuilder.loadTexts:
    mscAtmIfVccEpOperTable.setStatus("mandatory")
_MscAtmIfVccEpOperEntry_Object = MibTableRow
mscAtmIfVccEpOperEntry = _MscAtmIfVccEpOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 5, 9, 10, 1)
)
mscAtmIfVccEpOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVccIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscAtmIfVccEpIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfVccEpOperEntry.setStatus("mandatory")
_MscAtmIfVccEpApplicationName_Type = RowPointer
_MscAtmIfVccEpApplicationName_Object = MibTableColumn
mscAtmIfVccEpApplicationName = _MscAtmIfVccEpApplicationName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 5, 9, 10, 1, 1),
    _MscAtmIfVccEpApplicationName_Type()
)
mscAtmIfVccEpApplicationName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVccEpApplicationName.setStatus("mandatory")
_MscAtmIfVccRp_ObjectIdentity = ObjectIdentity
mscAtmIfVccRp = _MscAtmIfVccRp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 5, 10)
)
_MscAtmIfVccRpRowStatusTable_Object = MibTable
mscAtmIfVccRpRowStatusTable = _MscAtmIfVccRpRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 5, 10, 1)
)
if mibBuilder.loadTexts:
    mscAtmIfVccRpRowStatusTable.setStatus("mandatory")
_MscAtmIfVccRpRowStatusEntry_Object = MibTableRow
mscAtmIfVccRpRowStatusEntry = _MscAtmIfVccRpRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 5, 10, 1, 1)
)
mscAtmIfVccRpRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVccIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscAtmIfVccRpIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfVccRpRowStatusEntry.setStatus("mandatory")
_MscAtmIfVccRpRowStatus_Type = RowStatus
_MscAtmIfVccRpRowStatus_Object = MibTableColumn
mscAtmIfVccRpRowStatus = _MscAtmIfVccRpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 5, 10, 1, 1, 1),
    _MscAtmIfVccRpRowStatus_Type()
)
mscAtmIfVccRpRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVccRpRowStatus.setStatus("mandatory")
_MscAtmIfVccRpComponentName_Type = DisplayString
_MscAtmIfVccRpComponentName_Object = MibTableColumn
mscAtmIfVccRpComponentName = _MscAtmIfVccRpComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 5, 10, 1, 1, 2),
    _MscAtmIfVccRpComponentName_Type()
)
mscAtmIfVccRpComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVccRpComponentName.setStatus("mandatory")
_MscAtmIfVccRpStorageType_Type = StorageType
_MscAtmIfVccRpStorageType_Object = MibTableColumn
mscAtmIfVccRpStorageType = _MscAtmIfVccRpStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 5, 10, 1, 1, 4),
    _MscAtmIfVccRpStorageType_Type()
)
mscAtmIfVccRpStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVccRpStorageType.setStatus("mandatory")
_MscAtmIfVccRpIndex_Type = NonReplicated
_MscAtmIfVccRpIndex_Object = MibTableColumn
mscAtmIfVccRpIndex = _MscAtmIfVccRpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 5, 10, 1, 1, 10),
    _MscAtmIfVccRpIndex_Type()
)
mscAtmIfVccRpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAtmIfVccRpIndex.setStatus("mandatory")
_MscAtmIfVccRpOperTable_Object = MibTable
mscAtmIfVccRpOperTable = _MscAtmIfVccRpOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 5, 10, 10)
)
if mibBuilder.loadTexts:
    mscAtmIfVccRpOperTable.setStatus("mandatory")
_MscAtmIfVccRpOperEntry_Object = MibTableRow
mscAtmIfVccRpOperEntry = _MscAtmIfVccRpOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 5, 10, 10, 1)
)
mscAtmIfVccRpOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVccIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscAtmIfVccRpIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfVccRpOperEntry.setStatus("mandatory")
_MscAtmIfVccRpNextHop_Type = RowPointer
_MscAtmIfVccRpNextHop_Object = MibTableColumn
mscAtmIfVccRpNextHop = _MscAtmIfVccRpNextHop_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 5, 10, 10, 1, 1),
    _MscAtmIfVccRpNextHop_Type()
)
mscAtmIfVccRpNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVccRpNextHop.setStatus("obsolete")
_MscAtmIfVccRpNextHopsTable_Object = MibTable
mscAtmIfVccRpNextHopsTable = _MscAtmIfVccRpNextHopsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 5, 10, 430)
)
if mibBuilder.loadTexts:
    mscAtmIfVccRpNextHopsTable.setStatus("mandatory")
_MscAtmIfVccRpNextHopsEntry_Object = MibTableRow
mscAtmIfVccRpNextHopsEntry = _MscAtmIfVccRpNextHopsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 5, 10, 430, 1)
)
mscAtmIfVccRpNextHopsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVccIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscAtmIfVccRpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscAtmIfVccRpNextHopsValue"),
)
if mibBuilder.loadTexts:
    mscAtmIfVccRpNextHopsEntry.setStatus("mandatory")
_MscAtmIfVccRpNextHopsValue_Type = RowPointer
_MscAtmIfVccRpNextHopsValue_Object = MibTableColumn
mscAtmIfVccRpNextHopsValue = _MscAtmIfVccRpNextHopsValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 5, 10, 430, 1, 1),
    _MscAtmIfVccRpNextHopsValue_Type()
)
mscAtmIfVccRpNextHopsValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVccRpNextHopsValue.setStatus("mandatory")
_MscAtmIfVccDst_ObjectIdentity = ObjectIdentity
mscAtmIfVccDst = _MscAtmIfVccDst_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 5, 11)
)
_MscAtmIfVccDstRowStatusTable_Object = MibTable
mscAtmIfVccDstRowStatusTable = _MscAtmIfVccDstRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 5, 11, 1)
)
if mibBuilder.loadTexts:
    mscAtmIfVccDstRowStatusTable.setStatus("mandatory")
_MscAtmIfVccDstRowStatusEntry_Object = MibTableRow
mscAtmIfVccDstRowStatusEntry = _MscAtmIfVccDstRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 5, 11, 1, 1)
)
mscAtmIfVccDstRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVccIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscAtmIfVccDstIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfVccDstRowStatusEntry.setStatus("mandatory")
_MscAtmIfVccDstRowStatus_Type = RowStatus
_MscAtmIfVccDstRowStatus_Object = MibTableColumn
mscAtmIfVccDstRowStatus = _MscAtmIfVccDstRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 5, 11, 1, 1, 1),
    _MscAtmIfVccDstRowStatus_Type()
)
mscAtmIfVccDstRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVccDstRowStatus.setStatus("mandatory")
_MscAtmIfVccDstComponentName_Type = DisplayString
_MscAtmIfVccDstComponentName_Object = MibTableColumn
mscAtmIfVccDstComponentName = _MscAtmIfVccDstComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 5, 11, 1, 1, 2),
    _MscAtmIfVccDstComponentName_Type()
)
mscAtmIfVccDstComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVccDstComponentName.setStatus("mandatory")
_MscAtmIfVccDstStorageType_Type = StorageType
_MscAtmIfVccDstStorageType_Object = MibTableColumn
mscAtmIfVccDstStorageType = _MscAtmIfVccDstStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 5, 11, 1, 1, 4),
    _MscAtmIfVccDstStorageType_Type()
)
mscAtmIfVccDstStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVccDstStorageType.setStatus("mandatory")
_MscAtmIfVccDstIndex_Type = NonReplicated
_MscAtmIfVccDstIndex_Object = MibTableColumn
mscAtmIfVccDstIndex = _MscAtmIfVccDstIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 5, 11, 1, 1, 10),
    _MscAtmIfVccDstIndex_Type()
)
mscAtmIfVccDstIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAtmIfVccDstIndex.setStatus("mandatory")
_MscAtmIfVccDstOperTable_Object = MibTable
mscAtmIfVccDstOperTable = _MscAtmIfVccDstOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 5, 11, 10)
)
if mibBuilder.loadTexts:
    mscAtmIfVccDstOperTable.setStatus("mandatory")
_MscAtmIfVccDstOperEntry_Object = MibTableRow
mscAtmIfVccDstOperEntry = _MscAtmIfVccDstOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 5, 11, 10, 1)
)
mscAtmIfVccDstOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVccIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscAtmIfVccDstIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfVccDstOperEntry.setStatus("mandatory")


class _MscAtmIfVccDstCalledAddress_Type(HexString):
    """Custom type mscAtmIfVccDstCalledAddress based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_MscAtmIfVccDstCalledAddress_Type.__name__ = "HexString"
_MscAtmIfVccDstCalledAddress_Object = MibTableColumn
mscAtmIfVccDstCalledAddress = _MscAtmIfVccDstCalledAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 5, 11, 10, 1, 3),
    _MscAtmIfVccDstCalledAddress_Type()
)
mscAtmIfVccDstCalledAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVccDstCalledAddress.setStatus("mandatory")


class _MscAtmIfVccDstCallingAddress_Type(AsciiString):
    """Custom type mscAtmIfVccDstCallingAddress based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 40),
    )


_MscAtmIfVccDstCallingAddress_Type.__name__ = "AsciiString"
_MscAtmIfVccDstCallingAddress_Object = MibTableColumn
mscAtmIfVccDstCallingAddress = _MscAtmIfVccDstCallingAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 5, 11, 10, 1, 4),
    _MscAtmIfVccDstCallingAddress_Type()
)
mscAtmIfVccDstCallingAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVccDstCallingAddress.setStatus("mandatory")


class _MscAtmIfVccDstCallingVpiVci_Type(AsciiString):
    """Custom type mscAtmIfVccDstCallingVpiVci based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 9),
    )


_MscAtmIfVccDstCallingVpiVci_Type.__name__ = "AsciiString"
_MscAtmIfVccDstCallingVpiVci_Object = MibTableColumn
mscAtmIfVccDstCallingVpiVci = _MscAtmIfVccDstCallingVpiVci_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 5, 11, 10, 1, 5),
    _MscAtmIfVccDstCallingVpiVci_Type()
)
mscAtmIfVccDstCallingVpiVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVccDstCallingVpiVci.setStatus("mandatory")
_MscAtmIfVptVccSrc_ObjectIdentity = ObjectIdentity
mscAtmIfVptVccSrc = _MscAtmIfVptVccSrc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 20, 8)
)
_MscAtmIfVptVccSrcRowStatusTable_Object = MibTable
mscAtmIfVptVccSrcRowStatusTable = _MscAtmIfVptVccSrcRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 20, 8, 1)
)
if mibBuilder.loadTexts:
    mscAtmIfVptVccSrcRowStatusTable.setStatus("mandatory")
_MscAtmIfVptVccSrcRowStatusEntry_Object = MibTableRow
mscAtmIfVptVccSrcRowStatusEntry = _MscAtmIfVptVccSrcRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 20, 8, 1, 1)
)
mscAtmIfVptVccSrcRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVptIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVptVccIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscAtmIfVptVccSrcIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfVptVccSrcRowStatusEntry.setStatus("mandatory")
_MscAtmIfVptVccSrcRowStatus_Type = RowStatus
_MscAtmIfVptVccSrcRowStatus_Object = MibTableColumn
mscAtmIfVptVccSrcRowStatus = _MscAtmIfVptVccSrcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 20, 8, 1, 1, 1),
    _MscAtmIfVptVccSrcRowStatus_Type()
)
mscAtmIfVptVccSrcRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVptVccSrcRowStatus.setStatus("mandatory")
_MscAtmIfVptVccSrcComponentName_Type = DisplayString
_MscAtmIfVptVccSrcComponentName_Object = MibTableColumn
mscAtmIfVptVccSrcComponentName = _MscAtmIfVptVccSrcComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 20, 8, 1, 1, 2),
    _MscAtmIfVptVccSrcComponentName_Type()
)
mscAtmIfVptVccSrcComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptVccSrcComponentName.setStatus("mandatory")
_MscAtmIfVptVccSrcStorageType_Type = StorageType
_MscAtmIfVptVccSrcStorageType_Object = MibTableColumn
mscAtmIfVptVccSrcStorageType = _MscAtmIfVptVccSrcStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 20, 8, 1, 1, 4),
    _MscAtmIfVptVccSrcStorageType_Type()
)
mscAtmIfVptVccSrcStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptVccSrcStorageType.setStatus("mandatory")
_MscAtmIfVptVccSrcIndex_Type = NonReplicated
_MscAtmIfVptVccSrcIndex_Object = MibTableColumn
mscAtmIfVptVccSrcIndex = _MscAtmIfVptVccSrcIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 20, 8, 1, 1, 10),
    _MscAtmIfVptVccSrcIndex_Type()
)
mscAtmIfVptVccSrcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAtmIfVptVccSrcIndex.setStatus("mandatory")
_MscAtmIfVptVccSrcProvTable_Object = MibTable
mscAtmIfVptVccSrcProvTable = _MscAtmIfVptVccSrcProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 20, 8, 10)
)
if mibBuilder.loadTexts:
    mscAtmIfVptVccSrcProvTable.setStatus("mandatory")
_MscAtmIfVptVccSrcProvEntry_Object = MibTableRow
mscAtmIfVptVccSrcProvEntry = _MscAtmIfVptVccSrcProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 20, 8, 10, 1)
)
mscAtmIfVptVccSrcProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVptIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVptVccIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscAtmIfVptVccSrcIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfVptVccSrcProvEntry.setStatus("mandatory")


class _MscAtmIfVptVccSrcRemoteAddress_Type(HexString):
    """Custom type mscAtmIfVptVccSrcRemoteAddress based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_MscAtmIfVptVccSrcRemoteAddress_Type.__name__ = "HexString"
_MscAtmIfVptVccSrcRemoteAddress_Object = MibTableColumn
mscAtmIfVptVccSrcRemoteAddress = _MscAtmIfVptVccSrcRemoteAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 20, 8, 10, 1, 1),
    _MscAtmIfVptVccSrcRemoteAddress_Type()
)
mscAtmIfVptVccSrcRemoteAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVptVccSrcRemoteAddress.setStatus("obsolete")


class _MscAtmIfVptVccSrcRemoteVpiVci_Type(IntegerSequence):
    """Custom type mscAtmIfVptVccSrcRemoteVpiVci based on IntegerSequence"""
    subtypeSpec = IntegerSequence.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 9),
    )


_MscAtmIfVptVccSrcRemoteVpiVci_Type.__name__ = "IntegerSequence"
_MscAtmIfVptVccSrcRemoteVpiVci_Object = MibTableColumn
mscAtmIfVptVccSrcRemoteVpiVci = _MscAtmIfVptVccSrcRemoteVpiVci_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 20, 8, 10, 1, 2),
    _MscAtmIfVptVccSrcRemoteVpiVci_Type()
)
mscAtmIfVptVccSrcRemoteVpiVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVptVccSrcRemoteVpiVci.setStatus("obsolete")


class _MscAtmIfVptVccSrcCallingAddress_Type(HexString):
    """Custom type mscAtmIfVptVccSrcCallingAddress based on HexString"""
    defaultHexValue = ""

    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_MscAtmIfVptVccSrcCallingAddress_Type.__name__ = "HexString"
_MscAtmIfVptVccSrcCallingAddress_Object = MibTableColumn
mscAtmIfVptVccSrcCallingAddress = _MscAtmIfVptVccSrcCallingAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 20, 8, 10, 1, 3),
    _MscAtmIfVptVccSrcCallingAddress_Type()
)
mscAtmIfVptVccSrcCallingAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVptVccSrcCallingAddress.setStatus("mandatory")


class _MscAtmIfVptVccSrcCalledAddress_Type(HexString):
    """Custom type mscAtmIfVptVccSrcCalledAddress based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_MscAtmIfVptVccSrcCalledAddress_Type.__name__ = "HexString"
_MscAtmIfVptVccSrcCalledAddress_Object = MibTableColumn
mscAtmIfVptVccSrcCalledAddress = _MscAtmIfVptVccSrcCalledAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 20, 8, 10, 1, 4),
    _MscAtmIfVptVccSrcCalledAddress_Type()
)
mscAtmIfVptVccSrcCalledAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVptVccSrcCalledAddress.setStatus("mandatory")


class _MscAtmIfVptVccSrcCalledVpiVci_Type(IntegerSequence):
    """Custom type mscAtmIfVptVccSrcCalledVpiVci based on IntegerSequence"""
    subtypeSpec = IntegerSequence.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 10),
    )


_MscAtmIfVptVccSrcCalledVpiVci_Type.__name__ = "IntegerSequence"
_MscAtmIfVptVccSrcCalledVpiVci_Object = MibTableColumn
mscAtmIfVptVccSrcCalledVpiVci = _MscAtmIfVptVccSrcCalledVpiVci_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 20, 8, 10, 1, 5),
    _MscAtmIfVptVccSrcCalledVpiVci_Type()
)
mscAtmIfVptVccSrcCalledVpiVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVptVccSrcCalledVpiVci.setStatus("mandatory")
_MscAtmIfVptVccSrcOperTable_Object = MibTable
mscAtmIfVptVccSrcOperTable = _MscAtmIfVptVccSrcOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 20, 8, 11)
)
if mibBuilder.loadTexts:
    mscAtmIfVptVccSrcOperTable.setStatus("mandatory")
_MscAtmIfVptVccSrcOperEntry_Object = MibTableRow
mscAtmIfVptVccSrcOperEntry = _MscAtmIfVptVccSrcOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 20, 8, 11, 1)
)
mscAtmIfVptVccSrcOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVptIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVptVccIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscAtmIfVptVccSrcIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfVptVccSrcOperEntry.setStatus("mandatory")


class _MscAtmIfVptVccSrcState_Type(Integer32):
    """Custom type mscAtmIfVptVccSrcState based on Integer32"""
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


_MscAtmIfVptVccSrcState_Type.__name__ = "Integer32"
_MscAtmIfVptVccSrcState_Object = MibTableColumn
mscAtmIfVptVccSrcState = _MscAtmIfVptVccSrcState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 20, 8, 11, 1, 1),
    _MscAtmIfVptVccSrcState_Type()
)
mscAtmIfVptVccSrcState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptVccSrcState.setStatus("mandatory")
_MscAtmIfVptVccSrcRetryCount_Type = Counter32
_MscAtmIfVptVccSrcRetryCount_Object = MibTableColumn
mscAtmIfVptVccSrcRetryCount = _MscAtmIfVptVccSrcRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 20, 8, 11, 1, 2),
    _MscAtmIfVptVccSrcRetryCount_Type()
)
mscAtmIfVptVccSrcRetryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptVccSrcRetryCount.setStatus("mandatory")


class _MscAtmIfVptVccSrcLastFailureCauseCode_Type(Unsigned32):
    """Custom type mscAtmIfVptVccSrcLastFailureCauseCode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscAtmIfVptVccSrcLastFailureCauseCode_Type.__name__ = "Unsigned32"
_MscAtmIfVptVccSrcLastFailureCauseCode_Object = MibTableColumn
mscAtmIfVptVccSrcLastFailureCauseCode = _MscAtmIfVptVccSrcLastFailureCauseCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 20, 8, 11, 1, 3),
    _MscAtmIfVptVccSrcLastFailureCauseCode_Type()
)
mscAtmIfVptVccSrcLastFailureCauseCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptVccSrcLastFailureCauseCode.setStatus("mandatory")


class _MscAtmIfVptVccSrcLastFailureDiagCode_Type(AsciiString):
    """Custom type mscAtmIfVptVccSrcLastFailureDiagCode based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_MscAtmIfVptVccSrcLastFailureDiagCode_Type.__name__ = "AsciiString"
_MscAtmIfVptVccSrcLastFailureDiagCode_Object = MibTableColumn
mscAtmIfVptVccSrcLastFailureDiagCode = _MscAtmIfVptVccSrcLastFailureDiagCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 20, 8, 11, 1, 4),
    _MscAtmIfVptVccSrcLastFailureDiagCode_Type()
)
mscAtmIfVptVccSrcLastFailureDiagCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptVccSrcLastFailureDiagCode.setStatus("mandatory")
_MscAtmIfVptVccEp_ObjectIdentity = ObjectIdentity
mscAtmIfVptVccEp = _MscAtmIfVptVccEp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 20, 9)
)
_MscAtmIfVptVccEpRowStatusTable_Object = MibTable
mscAtmIfVptVccEpRowStatusTable = _MscAtmIfVptVccEpRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 20, 9, 1)
)
if mibBuilder.loadTexts:
    mscAtmIfVptVccEpRowStatusTable.setStatus("mandatory")
_MscAtmIfVptVccEpRowStatusEntry_Object = MibTableRow
mscAtmIfVptVccEpRowStatusEntry = _MscAtmIfVptVccEpRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 20, 9, 1, 1)
)
mscAtmIfVptVccEpRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVptIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVptVccIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscAtmIfVptVccEpIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfVptVccEpRowStatusEntry.setStatus("mandatory")
_MscAtmIfVptVccEpRowStatus_Type = RowStatus
_MscAtmIfVptVccEpRowStatus_Object = MibTableColumn
mscAtmIfVptVccEpRowStatus = _MscAtmIfVptVccEpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 20, 9, 1, 1, 1),
    _MscAtmIfVptVccEpRowStatus_Type()
)
mscAtmIfVptVccEpRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptVccEpRowStatus.setStatus("mandatory")
_MscAtmIfVptVccEpComponentName_Type = DisplayString
_MscAtmIfVptVccEpComponentName_Object = MibTableColumn
mscAtmIfVptVccEpComponentName = _MscAtmIfVptVccEpComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 20, 9, 1, 1, 2),
    _MscAtmIfVptVccEpComponentName_Type()
)
mscAtmIfVptVccEpComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptVccEpComponentName.setStatus("mandatory")
_MscAtmIfVptVccEpStorageType_Type = StorageType
_MscAtmIfVptVccEpStorageType_Object = MibTableColumn
mscAtmIfVptVccEpStorageType = _MscAtmIfVptVccEpStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 20, 9, 1, 1, 4),
    _MscAtmIfVptVccEpStorageType_Type()
)
mscAtmIfVptVccEpStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptVccEpStorageType.setStatus("mandatory")
_MscAtmIfVptVccEpIndex_Type = NonReplicated
_MscAtmIfVptVccEpIndex_Object = MibTableColumn
mscAtmIfVptVccEpIndex = _MscAtmIfVptVccEpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 20, 9, 1, 1, 10),
    _MscAtmIfVptVccEpIndex_Type()
)
mscAtmIfVptVccEpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAtmIfVptVccEpIndex.setStatus("mandatory")
_MscAtmIfVptVccEpOperTable_Object = MibTable
mscAtmIfVptVccEpOperTable = _MscAtmIfVptVccEpOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 20, 9, 10)
)
if mibBuilder.loadTexts:
    mscAtmIfVptVccEpOperTable.setStatus("mandatory")
_MscAtmIfVptVccEpOperEntry_Object = MibTableRow
mscAtmIfVptVccEpOperEntry = _MscAtmIfVptVccEpOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 20, 9, 10, 1)
)
mscAtmIfVptVccEpOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVptIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVptVccIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscAtmIfVptVccEpIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfVptVccEpOperEntry.setStatus("mandatory")
_MscAtmIfVptVccEpApplicationName_Type = RowPointer
_MscAtmIfVptVccEpApplicationName_Object = MibTableColumn
mscAtmIfVptVccEpApplicationName = _MscAtmIfVptVccEpApplicationName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 20, 9, 10, 1, 1),
    _MscAtmIfVptVccEpApplicationName_Type()
)
mscAtmIfVptVccEpApplicationName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptVccEpApplicationName.setStatus("mandatory")
_MscAtmIfVptVccRp_ObjectIdentity = ObjectIdentity
mscAtmIfVptVccRp = _MscAtmIfVptVccRp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 20, 10)
)
_MscAtmIfVptVccRpRowStatusTable_Object = MibTable
mscAtmIfVptVccRpRowStatusTable = _MscAtmIfVptVccRpRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 20, 10, 1)
)
if mibBuilder.loadTexts:
    mscAtmIfVptVccRpRowStatusTable.setStatus("mandatory")
_MscAtmIfVptVccRpRowStatusEntry_Object = MibTableRow
mscAtmIfVptVccRpRowStatusEntry = _MscAtmIfVptVccRpRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 20, 10, 1, 1)
)
mscAtmIfVptVccRpRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVptIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVptVccIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscAtmIfVptVccRpIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfVptVccRpRowStatusEntry.setStatus("mandatory")
_MscAtmIfVptVccRpRowStatus_Type = RowStatus
_MscAtmIfVptVccRpRowStatus_Object = MibTableColumn
mscAtmIfVptVccRpRowStatus = _MscAtmIfVptVccRpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 20, 10, 1, 1, 1),
    _MscAtmIfVptVccRpRowStatus_Type()
)
mscAtmIfVptVccRpRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptVccRpRowStatus.setStatus("mandatory")
_MscAtmIfVptVccRpComponentName_Type = DisplayString
_MscAtmIfVptVccRpComponentName_Object = MibTableColumn
mscAtmIfVptVccRpComponentName = _MscAtmIfVptVccRpComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 20, 10, 1, 1, 2),
    _MscAtmIfVptVccRpComponentName_Type()
)
mscAtmIfVptVccRpComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptVccRpComponentName.setStatus("mandatory")
_MscAtmIfVptVccRpStorageType_Type = StorageType
_MscAtmIfVptVccRpStorageType_Object = MibTableColumn
mscAtmIfVptVccRpStorageType = _MscAtmIfVptVccRpStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 20, 10, 1, 1, 4),
    _MscAtmIfVptVccRpStorageType_Type()
)
mscAtmIfVptVccRpStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptVccRpStorageType.setStatus("mandatory")
_MscAtmIfVptVccRpIndex_Type = NonReplicated
_MscAtmIfVptVccRpIndex_Object = MibTableColumn
mscAtmIfVptVccRpIndex = _MscAtmIfVptVccRpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 20, 10, 1, 1, 10),
    _MscAtmIfVptVccRpIndex_Type()
)
mscAtmIfVptVccRpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAtmIfVptVccRpIndex.setStatus("mandatory")
_MscAtmIfVptVccRpOperTable_Object = MibTable
mscAtmIfVptVccRpOperTable = _MscAtmIfVptVccRpOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 20, 10, 10)
)
if mibBuilder.loadTexts:
    mscAtmIfVptVccRpOperTable.setStatus("mandatory")
_MscAtmIfVptVccRpOperEntry_Object = MibTableRow
mscAtmIfVptVccRpOperEntry = _MscAtmIfVptVccRpOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 20, 10, 10, 1)
)
mscAtmIfVptVccRpOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVptIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVptVccIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscAtmIfVptVccRpIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfVptVccRpOperEntry.setStatus("mandatory")
_MscAtmIfVptVccRpNextHop_Type = RowPointer
_MscAtmIfVptVccRpNextHop_Object = MibTableColumn
mscAtmIfVptVccRpNextHop = _MscAtmIfVptVccRpNextHop_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 20, 10, 10, 1, 1),
    _MscAtmIfVptVccRpNextHop_Type()
)
mscAtmIfVptVccRpNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptVccRpNextHop.setStatus("obsolete")
_MscAtmIfVptVccRpNextHopsTable_Object = MibTable
mscAtmIfVptVccRpNextHopsTable = _MscAtmIfVptVccRpNextHopsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 20, 10, 430)
)
if mibBuilder.loadTexts:
    mscAtmIfVptVccRpNextHopsTable.setStatus("mandatory")
_MscAtmIfVptVccRpNextHopsEntry_Object = MibTableRow
mscAtmIfVptVccRpNextHopsEntry = _MscAtmIfVptVccRpNextHopsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 20, 10, 430, 1)
)
mscAtmIfVptVccRpNextHopsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVptIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVptVccIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscAtmIfVptVccRpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscAtmIfVptVccRpNextHopsValue"),
)
if mibBuilder.loadTexts:
    mscAtmIfVptVccRpNextHopsEntry.setStatus("mandatory")
_MscAtmIfVptVccRpNextHopsValue_Type = RowPointer
_MscAtmIfVptVccRpNextHopsValue_Object = MibTableColumn
mscAtmIfVptVccRpNextHopsValue = _MscAtmIfVptVccRpNextHopsValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 20, 10, 430, 1, 1),
    _MscAtmIfVptVccRpNextHopsValue_Type()
)
mscAtmIfVptVccRpNextHopsValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptVccRpNextHopsValue.setStatus("mandatory")
_MscAtmIfVptVccDst_ObjectIdentity = ObjectIdentity
mscAtmIfVptVccDst = _MscAtmIfVptVccDst_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 20, 11)
)
_MscAtmIfVptVccDstRowStatusTable_Object = MibTable
mscAtmIfVptVccDstRowStatusTable = _MscAtmIfVptVccDstRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 20, 11, 1)
)
if mibBuilder.loadTexts:
    mscAtmIfVptVccDstRowStatusTable.setStatus("mandatory")
_MscAtmIfVptVccDstRowStatusEntry_Object = MibTableRow
mscAtmIfVptVccDstRowStatusEntry = _MscAtmIfVptVccDstRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 20, 11, 1, 1)
)
mscAtmIfVptVccDstRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVptIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVptVccIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscAtmIfVptVccDstIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfVptVccDstRowStatusEntry.setStatus("mandatory")
_MscAtmIfVptVccDstRowStatus_Type = RowStatus
_MscAtmIfVptVccDstRowStatus_Object = MibTableColumn
mscAtmIfVptVccDstRowStatus = _MscAtmIfVptVccDstRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 20, 11, 1, 1, 1),
    _MscAtmIfVptVccDstRowStatus_Type()
)
mscAtmIfVptVccDstRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptVccDstRowStatus.setStatus("mandatory")
_MscAtmIfVptVccDstComponentName_Type = DisplayString
_MscAtmIfVptVccDstComponentName_Object = MibTableColumn
mscAtmIfVptVccDstComponentName = _MscAtmIfVptVccDstComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 20, 11, 1, 1, 2),
    _MscAtmIfVptVccDstComponentName_Type()
)
mscAtmIfVptVccDstComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptVccDstComponentName.setStatus("mandatory")
_MscAtmIfVptVccDstStorageType_Type = StorageType
_MscAtmIfVptVccDstStorageType_Object = MibTableColumn
mscAtmIfVptVccDstStorageType = _MscAtmIfVptVccDstStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 20, 11, 1, 1, 4),
    _MscAtmIfVptVccDstStorageType_Type()
)
mscAtmIfVptVccDstStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptVccDstStorageType.setStatus("mandatory")
_MscAtmIfVptVccDstIndex_Type = NonReplicated
_MscAtmIfVptVccDstIndex_Object = MibTableColumn
mscAtmIfVptVccDstIndex = _MscAtmIfVptVccDstIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 20, 11, 1, 1, 10),
    _MscAtmIfVptVccDstIndex_Type()
)
mscAtmIfVptVccDstIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAtmIfVptVccDstIndex.setStatus("mandatory")
_MscAtmIfVptVccDstOperTable_Object = MibTable
mscAtmIfVptVccDstOperTable = _MscAtmIfVptVccDstOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 20, 11, 10)
)
if mibBuilder.loadTexts:
    mscAtmIfVptVccDstOperTable.setStatus("mandatory")
_MscAtmIfVptVccDstOperEntry_Object = MibTableRow
mscAtmIfVptVccDstOperEntry = _MscAtmIfVptVccDstOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 20, 11, 10, 1)
)
mscAtmIfVptVccDstOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVptIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVptVccIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB", "mscAtmIfVptVccDstIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfVptVccDstOperEntry.setStatus("mandatory")


class _MscAtmIfVptVccDstCalledAddress_Type(HexString):
    """Custom type mscAtmIfVptVccDstCalledAddress based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_MscAtmIfVptVccDstCalledAddress_Type.__name__ = "HexString"
_MscAtmIfVptVccDstCalledAddress_Object = MibTableColumn
mscAtmIfVptVccDstCalledAddress = _MscAtmIfVptVccDstCalledAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 20, 11, 10, 1, 3),
    _MscAtmIfVptVccDstCalledAddress_Type()
)
mscAtmIfVptVccDstCalledAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptVccDstCalledAddress.setStatus("mandatory")


class _MscAtmIfVptVccDstCallingAddress_Type(AsciiString):
    """Custom type mscAtmIfVptVccDstCallingAddress based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 40),
    )


_MscAtmIfVptVccDstCallingAddress_Type.__name__ = "AsciiString"
_MscAtmIfVptVccDstCallingAddress_Object = MibTableColumn
mscAtmIfVptVccDstCallingAddress = _MscAtmIfVptVccDstCallingAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 20, 11, 10, 1, 4),
    _MscAtmIfVptVccDstCallingAddress_Type()
)
mscAtmIfVptVccDstCallingAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptVccDstCallingAddress.setStatus("mandatory")


class _MscAtmIfVptVccDstCallingVpiVci_Type(AsciiString):
    """Custom type mscAtmIfVptVccDstCallingVpiVci based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 9),
    )


_MscAtmIfVptVccDstCallingVpiVci_Type.__name__ = "AsciiString"
_MscAtmIfVptVccDstCallingVpiVci_Object = MibTableColumn
mscAtmIfVptVccDstCallingVpiVci = _MscAtmIfVptVccDstCallingVpiVci_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 20, 11, 10, 1, 5),
    _MscAtmIfVptVccDstCallingVpiVci_Type()
)
mscAtmIfVptVccDstCallingVpiVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptVccDstCallingVpiVci.setStatus("mandatory")
_AtmNetworkingMIB_ObjectIdentity = ObjectIdentity
atmNetworkingMIB = _AtmNetworkingMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 42)
)
_AtmNetworkingGroup_ObjectIdentity = ObjectIdentity
atmNetworkingGroup = _AtmNetworkingGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 42, 1)
)
_AtmNetworkingGroupCA_ObjectIdentity = ObjectIdentity
atmNetworkingGroupCA = _AtmNetworkingGroupCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 42, 1, 1)
)
_AtmNetworkingGroupCA02_ObjectIdentity = ObjectIdentity
atmNetworkingGroupCA02 = _AtmNetworkingGroupCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 42, 1, 1, 3)
)
_AtmNetworkingGroupCA02A_ObjectIdentity = ObjectIdentity
atmNetworkingGroupCA02A = _AtmNetworkingGroupCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 42, 1, 1, 3, 2)
)
_AtmNetworkingCapabilities_ObjectIdentity = ObjectIdentity
atmNetworkingCapabilities = _AtmNetworkingCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 42, 3)
)
_AtmNetworkingCapabilitiesCA_ObjectIdentity = ObjectIdentity
atmNetworkingCapabilitiesCA = _AtmNetworkingCapabilitiesCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 42, 3, 1)
)
_AtmNetworkingCapabilitiesCA02_ObjectIdentity = ObjectIdentity
atmNetworkingCapabilitiesCA02 = _AtmNetworkingCapabilitiesCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 42, 3, 1, 3)
)
_AtmNetworkingCapabilitiesCA02A_ObjectIdentity = ObjectIdentity
atmNetworkingCapabilitiesCA02A = _AtmNetworkingCapabilitiesCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 42, 3, 1, 3, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-MsCarrier-MscPassport-AtmNetworkingMIB",
    **{"mscARtg": mscARtg,
       "mscARtgRowStatusTable": mscARtgRowStatusTable,
       "mscARtgRowStatusEntry": mscARtgRowStatusEntry,
       "mscARtgRowStatus": mscARtgRowStatus,
       "mscARtgComponentName": mscARtgComponentName,
       "mscARtgStorageType": mscARtgStorageType,
       "mscARtgIndex": mscARtgIndex,
       "mscARtgDna": mscARtgDna,
       "mscARtgDnaRowStatusTable": mscARtgDnaRowStatusTable,
       "mscARtgDnaRowStatusEntry": mscARtgDnaRowStatusEntry,
       "mscARtgDnaRowStatus": mscARtgDnaRowStatus,
       "mscARtgDnaComponentName": mscARtgDnaComponentName,
       "mscARtgDnaStorageType": mscARtgDnaStorageType,
       "mscARtgDnaIndex": mscARtgDnaIndex,
       "mscARtgDnaDestInfo": mscARtgDnaDestInfo,
       "mscARtgDnaDestInfoRowStatusTable": mscARtgDnaDestInfoRowStatusTable,
       "mscARtgDnaDestInfoRowStatusEntry": mscARtgDnaDestInfoRowStatusEntry,
       "mscARtgDnaDestInfoRowStatus": mscARtgDnaDestInfoRowStatus,
       "mscARtgDnaDestInfoComponentName": mscARtgDnaDestInfoComponentName,
       "mscARtgDnaDestInfoStorageType": mscARtgDnaDestInfoStorageType,
       "mscARtgDnaDestInfoIndex": mscARtgDnaDestInfoIndex,
       "mscARtgDnaDestInfoOperTable": mscARtgDnaDestInfoOperTable,
       "mscARtgDnaDestInfoOperEntry": mscARtgDnaDestInfoOperEntry,
       "mscARtgDnaDestInfoType": mscARtgDnaDestInfoType,
       "mscARtgDnaDestInfoScope": mscARtgDnaDestInfoScope,
       "mscARtgDnaDestInfoStdComponentName": mscARtgDnaDestInfoStdComponentName,
       "mscARtgDnaDestInfoReachability": mscARtgDnaDestInfoReachability,
       "mscARtgPnni": mscARtgPnni,
       "mscARtgPnniRowStatusTable": mscARtgPnniRowStatusTable,
       "mscARtgPnniRowStatusEntry": mscARtgPnniRowStatusEntry,
       "mscARtgPnniRowStatus": mscARtgPnniRowStatus,
       "mscARtgPnniComponentName": mscARtgPnniComponentName,
       "mscARtgPnniStorageType": mscARtgPnniStorageType,
       "mscARtgPnniIndex": mscARtgPnniIndex,
       "mscARtgPnniRf": mscARtgPnniRf,
       "mscARtgPnniRfRowStatusTable": mscARtgPnniRfRowStatusTable,
       "mscARtgPnniRfRowStatusEntry": mscARtgPnniRfRowStatusEntry,
       "mscARtgPnniRfRowStatus": mscARtgPnniRfRowStatus,
       "mscARtgPnniRfComponentName": mscARtgPnniRfComponentName,
       "mscARtgPnniRfStorageType": mscARtgPnniRfStorageType,
       "mscARtgPnniRfIndex": mscARtgPnniRfIndex,
       "mscARtgPnniRfCriteriaTable": mscARtgPnniRfCriteriaTable,
       "mscARtgPnniRfCriteriaEntry": mscARtgPnniRfCriteriaEntry,
       "mscARtgPnniRfDestinationAddress": mscARtgPnniRfDestinationAddress,
       "mscARtgPnniRfMaxRoutes": mscARtgPnniRfMaxRoutes,
       "mscARtgPnniRfTxTrafficDescType": mscARtgPnniRfTxTrafficDescType,
       "mscARtgPnniRfRxTrafficDescType": mscARtgPnniRfRxTrafficDescType,
       "mscARtgPnniRfAtmServiceCategory": mscARtgPnniRfAtmServiceCategory,
       "mscARtgPnniRfFwdQosClass": mscARtgPnniRfFwdQosClass,
       "mscARtgPnniRfBwdQosClass": mscARtgPnniRfBwdQosClass,
       "mscARtgPnniRfBearerClassBbc": mscARtgPnniRfBearerClassBbc,
       "mscARtgPnniRfTransferCapabilityBbc": mscARtgPnniRfTransferCapabilityBbc,
       "mscARtgPnniRfClippingBbc": mscARtgPnniRfClippingBbc,
       "mscARtgPnniRfBestEffort": mscARtgPnniRfBestEffort,
       "mscARtgPnniRfOptimizationMetric": mscARtgPnniRfOptimizationMetric,
       "mscARtgPnniRfRxTdpTable": mscARtgPnniRfRxTdpTable,
       "mscARtgPnniRfRxTdpEntry": mscARtgPnniRfRxTdpEntry,
       "mscARtgPnniRfRxTdpIndex": mscARtgPnniRfRxTdpIndex,
       "mscARtgPnniRfRxTdpValue": mscARtgPnniRfRxTdpValue,
       "mscARtgPnniRfTxTdpTable": mscARtgPnniRfTxTdpTable,
       "mscARtgPnniRfTxTdpEntry": mscARtgPnniRfTxTdpEntry,
       "mscARtgPnniRfTxTdpIndex": mscARtgPnniRfTxTdpIndex,
       "mscARtgPnniRfTxTdpValue": mscARtgPnniRfTxTdpValue,
       "mscARtgPnniRfFqpTable": mscARtgPnniRfFqpTable,
       "mscARtgPnniRfFqpEntry": mscARtgPnniRfFqpEntry,
       "mscARtgPnniRfFqpIndex": mscARtgPnniRfFqpIndex,
       "mscARtgPnniRfFqpValue": mscARtgPnniRfFqpValue,
       "mscARtgPnniRfBqpTable": mscARtgPnniRfBqpTable,
       "mscARtgPnniRfBqpEntry": mscARtgPnniRfBqpEntry,
       "mscARtgPnniRfBqpIndex": mscARtgPnniRfBqpIndex,
       "mscARtgPnniRfBqpValue": mscARtgPnniRfBqpValue,
       "mscARtgPnniCfgNode": mscARtgPnniCfgNode,
       "mscARtgPnniCfgNodeRowStatusTable": mscARtgPnniCfgNodeRowStatusTable,
       "mscARtgPnniCfgNodeRowStatusEntry": mscARtgPnniCfgNodeRowStatusEntry,
       "mscARtgPnniCfgNodeRowStatus": mscARtgPnniCfgNodeRowStatus,
       "mscARtgPnniCfgNodeComponentName": mscARtgPnniCfgNodeComponentName,
       "mscARtgPnniCfgNodeStorageType": mscARtgPnniCfgNodeStorageType,
       "mscARtgPnniCfgNodeIndex": mscARtgPnniCfgNodeIndex,
       "mscARtgPnniCfgNodeSAddr": mscARtgPnniCfgNodeSAddr,
       "mscARtgPnniCfgNodeSAddrRowStatusTable": mscARtgPnniCfgNodeSAddrRowStatusTable,
       "mscARtgPnniCfgNodeSAddrRowStatusEntry": mscARtgPnniCfgNodeSAddrRowStatusEntry,
       "mscARtgPnniCfgNodeSAddrRowStatus": mscARtgPnniCfgNodeSAddrRowStatus,
       "mscARtgPnniCfgNodeSAddrComponentName": mscARtgPnniCfgNodeSAddrComponentName,
       "mscARtgPnniCfgNodeSAddrStorageType": mscARtgPnniCfgNodeSAddrStorageType,
       "mscARtgPnniCfgNodeSAddrAddressIndex": mscARtgPnniCfgNodeSAddrAddressIndex,
       "mscARtgPnniCfgNodeSAddrPrefixLengthIndex": mscARtgPnniCfgNodeSAddrPrefixLengthIndex,
       "mscARtgPnniCfgNodeSAddrReachabilityIndex": mscARtgPnniCfgNodeSAddrReachabilityIndex,
       "mscARtgPnniCfgNodeSAddrProvTable": mscARtgPnniCfgNodeSAddrProvTable,
       "mscARtgPnniCfgNodeSAddrProvEntry": mscARtgPnniCfgNodeSAddrProvEntry,
       "mscARtgPnniCfgNodeSAddrSuppress": mscARtgPnniCfgNodeSAddrSuppress,
       "mscARtgPnniCfgNodeSAddrOperTable": mscARtgPnniCfgNodeSAddrOperTable,
       "mscARtgPnniCfgNodeSAddrOperEntry": mscARtgPnniCfgNodeSAddrOperEntry,
       "mscARtgPnniCfgNodeSAddrState": mscARtgPnniCfgNodeSAddrState,
       "mscARtgPnniCfgNodeSAddrScope": mscARtgPnniCfgNodeSAddrScope,
       "mscARtgPnniCfgNodeNbr": mscARtgPnniCfgNodeNbr,
       "mscARtgPnniCfgNodeNbrRowStatusTable": mscARtgPnniCfgNodeNbrRowStatusTable,
       "mscARtgPnniCfgNodeNbrRowStatusEntry": mscARtgPnniCfgNodeNbrRowStatusEntry,
       "mscARtgPnniCfgNodeNbrRowStatus": mscARtgPnniCfgNodeNbrRowStatus,
       "mscARtgPnniCfgNodeNbrComponentName": mscARtgPnniCfgNodeNbrComponentName,
       "mscARtgPnniCfgNodeNbrStorageType": mscARtgPnniCfgNodeNbrStorageType,
       "mscARtgPnniCfgNodeNbrIndex": mscARtgPnniCfgNodeNbrIndex,
       "mscARtgPnniCfgNodeNbrOperTable": mscARtgPnniCfgNodeNbrOperTable,
       "mscARtgPnniCfgNodeNbrOperEntry": mscARtgPnniCfgNodeNbrOperEntry,
       "mscARtgPnniCfgNodeNbrPeerState": mscARtgPnniCfgNodeNbrPeerState,
       "mscARtgPnniCfgNodeNbrStatsTable": mscARtgPnniCfgNodeNbrStatsTable,
       "mscARtgPnniCfgNodeNbrStatsEntry": mscARtgPnniCfgNodeNbrStatsEntry,
       "mscARtgPnniCfgNodeNbrPtspRx": mscARtgPnniCfgNodeNbrPtspRx,
       "mscARtgPnniCfgNodeNbrPtspTx": mscARtgPnniCfgNodeNbrPtspTx,
       "mscARtgPnniCfgNodeNbrPtseRx": mscARtgPnniCfgNodeNbrPtseRx,
       "mscARtgPnniCfgNodeNbrPtseTx": mscARtgPnniCfgNodeNbrPtseTx,
       "mscARtgPnniCfgNodeNbrPtseReqRx": mscARtgPnniCfgNodeNbrPtseReqRx,
       "mscARtgPnniCfgNodeNbrPtseReqTx": mscARtgPnniCfgNodeNbrPtseReqTx,
       "mscARtgPnniCfgNodeNbrPtseAcksRx": mscARtgPnniCfgNodeNbrPtseAcksRx,
       "mscARtgPnniCfgNodeNbrPtseAcksTx": mscARtgPnniCfgNodeNbrPtseAcksTx,
       "mscARtgPnniCfgNodeNbrDbSummariesRx": mscARtgPnniCfgNodeNbrDbSummariesRx,
       "mscARtgPnniCfgNodeNbrDbSummariesTx": mscARtgPnniCfgNodeNbrDbSummariesTx,
       "mscARtgPnniCfgNodeNbrBadPtspRx": mscARtgPnniCfgNodeNbrBadPtspRx,
       "mscARtgPnniCfgNodeNbrBadPtseRx": mscARtgPnniCfgNodeNbrBadPtseRx,
       "mscARtgPnniCfgNodeNbrBadPtseReqRx": mscARtgPnniCfgNodeNbrBadPtseReqRx,
       "mscARtgPnniCfgNodeNbrBadPtseAckRx": mscARtgPnniCfgNodeNbrBadPtseAckRx,
       "mscARtgPnniCfgNodeNbrBadDbSummariesRx": mscARtgPnniCfgNodeNbrBadDbSummariesRx,
       "mscARtgPnniCfgNodeNbrRccListTable": mscARtgPnniCfgNodeNbrRccListTable,
       "mscARtgPnniCfgNodeNbrRccListEntry": mscARtgPnniCfgNodeNbrRccListEntry,
       "mscARtgPnniCfgNodeNbrRccListValue": mscARtgPnniCfgNodeNbrRccListValue,
       "mscARtgPnniCfgNodeDefSAddr": mscARtgPnniCfgNodeDefSAddr,
       "mscARtgPnniCfgNodeDefSAddrRowStatusTable": mscARtgPnniCfgNodeDefSAddrRowStatusTable,
       "mscARtgPnniCfgNodeDefSAddrRowStatusEntry": mscARtgPnniCfgNodeDefSAddrRowStatusEntry,
       "mscARtgPnniCfgNodeDefSAddrRowStatus": mscARtgPnniCfgNodeDefSAddrRowStatus,
       "mscARtgPnniCfgNodeDefSAddrComponentName": mscARtgPnniCfgNodeDefSAddrComponentName,
       "mscARtgPnniCfgNodeDefSAddrStorageType": mscARtgPnniCfgNodeDefSAddrStorageType,
       "mscARtgPnniCfgNodeDefSAddrIndex": mscARtgPnniCfgNodeDefSAddrIndex,
       "mscARtgPnniCfgNodeDefSAddrDefAddrTable": mscARtgPnniCfgNodeDefSAddrDefAddrTable,
       "mscARtgPnniCfgNodeDefSAddrDefAddrEntry": mscARtgPnniCfgNodeDefSAddrDefAddrEntry,
       "mscARtgPnniCfgNodeDefSAddrAddress": mscARtgPnniCfgNodeDefSAddrAddress,
       "mscARtgPnniCfgNodeDefSAddrOperTable": mscARtgPnniCfgNodeDefSAddrOperTable,
       "mscARtgPnniCfgNodeDefSAddrOperEntry": mscARtgPnniCfgNodeDefSAddrOperEntry,
       "mscARtgPnniCfgNodeDefSAddrState": mscARtgPnniCfgNodeDefSAddrState,
       "mscARtgPnniCfgNodeDefSAddrScope": mscARtgPnniCfgNodeDefSAddrScope,
       "mscARtgPnniCfgNodeProvTable": mscARtgPnniCfgNodeProvTable,
       "mscARtgPnniCfgNodeProvEntry": mscARtgPnniCfgNodeProvEntry,
       "mscARtgPnniCfgNodeNodeId": mscARtgPnniCfgNodeNodeId,
       "mscARtgPnniCfgNodePeerGroupId": mscARtgPnniCfgNodePeerGroupId,
       "mscARtgPnniCfgNodeOperTable": mscARtgPnniCfgNodeOperTable,
       "mscARtgPnniCfgNodeOperEntry": mscARtgPnniCfgNodeOperEntry,
       "mscARtgPnniCfgNodeNodeAddress": mscARtgPnniCfgNodeNodeAddress,
       "mscARtgPnniCfgNodeOpNodeId": mscARtgPnniCfgNodeOpNodeId,
       "mscARtgPnniCfgNodeOpPeerGroupId": mscARtgPnniCfgNodeOpPeerGroupId,
       "mscARtgPnniCfgNodeNumNeighbors": mscARtgPnniCfgNodeNumNeighbors,
       "mscARtgPnniCfgNodeNumRccs": mscARtgPnniCfgNodeNumRccs,
       "mscARtgPnniCfgNodeCurrentLeadershipPriority": mscARtgPnniCfgNodeCurrentLeadershipPriority,
       "mscARtgPnniCfgNodePglElectionState": mscARtgPnniCfgNodePglElectionState,
       "mscARtgPnniTop": mscARtgPnniTop,
       "mscARtgPnniTopRowStatusTable": mscARtgPnniTopRowStatusTable,
       "mscARtgPnniTopRowStatusEntry": mscARtgPnniTopRowStatusEntry,
       "mscARtgPnniTopRowStatus": mscARtgPnniTopRowStatus,
       "mscARtgPnniTopComponentName": mscARtgPnniTopComponentName,
       "mscARtgPnniTopStorageType": mscARtgPnniTopStorageType,
       "mscARtgPnniTopIndex": mscARtgPnniTopIndex,
       "mscARtgPnniTopNode": mscARtgPnniTopNode,
       "mscARtgPnniTopNodeRowStatusTable": mscARtgPnniTopNodeRowStatusTable,
       "mscARtgPnniTopNodeRowStatusEntry": mscARtgPnniTopNodeRowStatusEntry,
       "mscARtgPnniTopNodeRowStatus": mscARtgPnniTopNodeRowStatus,
       "mscARtgPnniTopNodeComponentName": mscARtgPnniTopNodeComponentName,
       "mscARtgPnniTopNodeStorageType": mscARtgPnniTopNodeStorageType,
       "mscARtgPnniTopNodeIndex": mscARtgPnniTopNodeIndex,
       "mscARtgPnniTopNodeAddr": mscARtgPnniTopNodeAddr,
       "mscARtgPnniTopNodeAddrRowStatusTable": mscARtgPnniTopNodeAddrRowStatusTable,
       "mscARtgPnniTopNodeAddrRowStatusEntry": mscARtgPnniTopNodeAddrRowStatusEntry,
       "mscARtgPnniTopNodeAddrRowStatus": mscARtgPnniTopNodeAddrRowStatus,
       "mscARtgPnniTopNodeAddrComponentName": mscARtgPnniTopNodeAddrComponentName,
       "mscARtgPnniTopNodeAddrStorageType": mscARtgPnniTopNodeAddrStorageType,
       "mscARtgPnniTopNodeAddrAddressIndex": mscARtgPnniTopNodeAddrAddressIndex,
       "mscARtgPnniTopNodeAddrPrefixLengthIndex": mscARtgPnniTopNodeAddrPrefixLengthIndex,
       "mscARtgPnniTopNodeAddrReachabilityIndex": mscARtgPnniTopNodeAddrReachabilityIndex,
       "mscARtgPnniTopNodeAddrOperTable": mscARtgPnniTopNodeAddrOperTable,
       "mscARtgPnniTopNodeAddrOperEntry": mscARtgPnniTopNodeAddrOperEntry,
       "mscARtgPnniTopNodeAddrScope": mscARtgPnniTopNodeAddrScope,
       "mscARtgPnniTopNodeLink": mscARtgPnniTopNodeLink,
       "mscARtgPnniTopNodeLinkRowStatusTable": mscARtgPnniTopNodeLinkRowStatusTable,
       "mscARtgPnniTopNodeLinkRowStatusEntry": mscARtgPnniTopNodeLinkRowStatusEntry,
       "mscARtgPnniTopNodeLinkRowStatus": mscARtgPnniTopNodeLinkRowStatus,
       "mscARtgPnniTopNodeLinkComponentName": mscARtgPnniTopNodeLinkComponentName,
       "mscARtgPnniTopNodeLinkStorageType": mscARtgPnniTopNodeLinkStorageType,
       "mscARtgPnniTopNodeLinkIndex": mscARtgPnniTopNodeLinkIndex,
       "mscARtgPnniTopNodeLinkOperTable": mscARtgPnniTopNodeLinkOperTable,
       "mscARtgPnniTopNodeLinkOperEntry": mscARtgPnniTopNodeLinkOperEntry,
       "mscARtgPnniTopNodeLinkRemoteNodeId": mscARtgPnniTopNodeLinkRemoteNodeId,
       "mscARtgPnniTopNodeLinkRemotePortId": mscARtgPnniTopNodeLinkRemotePortId,
       "mscARtgPnniTopOperTable": mscARtgPnniTopOperTable,
       "mscARtgPnniTopOperEntry": mscARtgPnniTopOperEntry,
       "mscARtgPnniTopPtsesInDatabase": mscARtgPnniTopPtsesInDatabase,
       "mscARtgPnniTopPglNodeId": mscARtgPnniTopPglNodeId,
       "mscARtgPnniTopActiveParentNodeId": mscARtgPnniTopActiveParentNodeId,
       "mscARtgPnniTopPreferredPglNodeId": mscARtgPnniTopPreferredPglNodeId,
       "mscARtgPnniPort": mscARtgPnniPort,
       "mscARtgPnniPortRowStatusTable": mscARtgPnniPortRowStatusTable,
       "mscARtgPnniPortRowStatusEntry": mscARtgPnniPortRowStatusEntry,
       "mscARtgPnniPortRowStatus": mscARtgPnniPortRowStatus,
       "mscARtgPnniPortComponentName": mscARtgPnniPortComponentName,
       "mscARtgPnniPortStorageType": mscARtgPnniPortStorageType,
       "mscARtgPnniPortIndex": mscARtgPnniPortIndex,
       "mscARtgPnniPortOperTable": mscARtgPnniPortOperTable,
       "mscARtgPnniPortOperEntry": mscARtgPnniPortOperEntry,
       "mscARtgPnniPortStdComponentName": mscARtgPnniPortStdComponentName,
       "mscARtgPnniProvTable": mscARtgPnniProvTable,
       "mscARtgPnniProvEntry": mscARtgPnniProvEntry,
       "mscARtgPnniNodeAddressPrefix": mscARtgPnniNodeAddressPrefix,
       "mscARtgPnniDefaultScope": mscARtgPnniDefaultScope,
       "mscARtgPnniDomain": mscARtgPnniDomain,
       "mscARtgPnniRestrictTransit": mscARtgPnniRestrictTransit,
       "mscARtgPnniMaxAlternateRoutesOnCrankback": mscARtgPnniMaxAlternateRoutesOnCrankback,
       "mscARtgPnniPglParmsTable": mscARtgPnniPglParmsTable,
       "mscARtgPnniPglParmsEntry": mscARtgPnniPglParmsEntry,
       "mscARtgPnniPglInitTime": mscARtgPnniPglInitTime,
       "mscARtgPnniOverrideDelay": mscARtgPnniOverrideDelay,
       "mscARtgPnniReElectionInterval": mscARtgPnniReElectionInterval,
       "mscARtgPnniHlParmsTable": mscARtgPnniHlParmsTable,
       "mscARtgPnniHlParmsEntry": mscARtgPnniHlParmsEntry,
       "mscARtgPnniHelloHoldDown": mscARtgPnniHelloHoldDown,
       "mscARtgPnniHelloInterval": mscARtgPnniHelloInterval,
       "mscARtgPnniHelloInactivityFactor": mscARtgPnniHelloInactivityFactor,
       "mscARtgPnniPtseParmsTable": mscARtgPnniPtseParmsTable,
       "mscARtgPnniPtseParmsEntry": mscARtgPnniPtseParmsEntry,
       "mscARtgPnniPtseHoldDown": mscARtgPnniPtseHoldDown,
       "mscARtgPnniPtseRefreshInterval": mscARtgPnniPtseRefreshInterval,
       "mscARtgPnniPtseLifetimeFactor": mscARtgPnniPtseLifetimeFactor,
       "mscARtgPnniRequestRxmtInterval": mscARtgPnniRequestRxmtInterval,
       "mscARtgPnniPeerDelayedAckInterval": mscARtgPnniPeerDelayedAckInterval,
       "mscARtgPnniThreshParmsTable": mscARtgPnniThreshParmsTable,
       "mscARtgPnniThreshParmsEntry": mscARtgPnniThreshParmsEntry,
       "mscARtgPnniAvcrMt": mscARtgPnniAvcrMt,
       "mscARtgPnniAvcrPm": mscARtgPnniAvcrPm,
       "mscARtgPnniOperTable": mscARtgPnniOperTable,
       "mscARtgPnniOperEntry": mscARtgPnniOperEntry,
       "mscARtgPnniTopologyMemoryExhaustion": mscARtgPnniTopologyMemoryExhaustion,
       "mscARtgPnniStatsTable": mscARtgPnniStatsTable,
       "mscARtgPnniStatsEntry": mscARtgPnniStatsEntry,
       "mscARtgPnniSuccessfulRoutingAttempts": mscARtgPnniSuccessfulRoutingAttempts,
       "mscARtgPnniFailedRoutingAttempts": mscARtgPnniFailedRoutingAttempts,
       "mscARtgPnniAlternateRoutingAttempts": mscARtgPnniAlternateRoutingAttempts,
       "mscARtgPnniOptMetricTable": mscARtgPnniOptMetricTable,
       "mscARtgPnniOptMetricEntry": mscARtgPnniOptMetricEntry,
       "mscARtgPnniOptMetricIndex": mscARtgPnniOptMetricIndex,
       "mscARtgPnniOptMetricValue": mscARtgPnniOptMetricValue,
       "mscARtgStatsTable": mscARtgStatsTable,
       "mscARtgStatsEntry": mscARtgStatsEntry,
       "mscARtgRoutingAttempts": mscARtgRoutingAttempts,
       "mscARtgFailedRoutingAttempts": mscARtgFailedRoutingAttempts,
       "mscAtmCR": mscAtmCR,
       "mscAtmCRRowStatusTable": mscAtmCRRowStatusTable,
       "mscAtmCRRowStatusEntry": mscAtmCRRowStatusEntry,
       "mscAtmCRRowStatus": mscAtmCRRowStatus,
       "mscAtmCRComponentName": mscAtmCRComponentName,
       "mscAtmCRStorageType": mscAtmCRStorageType,
       "mscAtmCRIndex": mscAtmCRIndex,
       "mscAtmCRDna": mscAtmCRDna,
       "mscAtmCRDnaRowStatusTable": mscAtmCRDnaRowStatusTable,
       "mscAtmCRDnaRowStatusEntry": mscAtmCRDnaRowStatusEntry,
       "mscAtmCRDnaRowStatus": mscAtmCRDnaRowStatus,
       "mscAtmCRDnaComponentName": mscAtmCRDnaComponentName,
       "mscAtmCRDnaStorageType": mscAtmCRDnaStorageType,
       "mscAtmCRDnaIndex": mscAtmCRDnaIndex,
       "mscAtmCRDnaDestinationNameTable": mscAtmCRDnaDestinationNameTable,
       "mscAtmCRDnaDestinationNameEntry": mscAtmCRDnaDestinationNameEntry,
       "mscAtmCRDnaDestinationNameValue": mscAtmCRDnaDestinationNameValue,
       "mscAtmCRProvTable": mscAtmCRProvTable,
       "mscAtmCRProvEntry": mscAtmCRProvEntry,
       "mscAtmCRNodeAddress": mscAtmCRNodeAddress,
       "mscAtmCRStatsTable": mscAtmCRStatsTable,
       "mscAtmCRStatsEntry": mscAtmCRStatsEntry,
       "mscAtmCRCallsRouted": mscAtmCRCallsRouted,
       "mscAtmCRCallsFailed": mscAtmCRCallsFailed,
       "mscAtmIfVpcSrc": mscAtmIfVpcSrc,
       "mscAtmIfVpcSrcRowStatusTable": mscAtmIfVpcSrcRowStatusTable,
       "mscAtmIfVpcSrcRowStatusEntry": mscAtmIfVpcSrcRowStatusEntry,
       "mscAtmIfVpcSrcRowStatus": mscAtmIfVpcSrcRowStatus,
       "mscAtmIfVpcSrcComponentName": mscAtmIfVpcSrcComponentName,
       "mscAtmIfVpcSrcStorageType": mscAtmIfVpcSrcStorageType,
       "mscAtmIfVpcSrcIndex": mscAtmIfVpcSrcIndex,
       "mscAtmIfVpcSrcProvTable": mscAtmIfVpcSrcProvTable,
       "mscAtmIfVpcSrcProvEntry": mscAtmIfVpcSrcProvEntry,
       "mscAtmIfVpcSrcCallingAddress": mscAtmIfVpcSrcCallingAddress,
       "mscAtmIfVpcSrcCalledAddress": mscAtmIfVpcSrcCalledAddress,
       "mscAtmIfVpcSrcCalledVpi": mscAtmIfVpcSrcCalledVpi,
       "mscAtmIfVpcSrcOperTable": mscAtmIfVpcSrcOperTable,
       "mscAtmIfVpcSrcOperEntry": mscAtmIfVpcSrcOperEntry,
       "mscAtmIfVpcSrcState": mscAtmIfVpcSrcState,
       "mscAtmIfVpcSrcRetryCount": mscAtmIfVpcSrcRetryCount,
       "mscAtmIfVpcSrcLastFailureCauseCode": mscAtmIfVpcSrcLastFailureCauseCode,
       "mscAtmIfVpcSrcLastFailureDiagCode": mscAtmIfVpcSrcLastFailureDiagCode,
       "mscAtmIfVpcRp": mscAtmIfVpcRp,
       "mscAtmIfVpcRpRowStatusTable": mscAtmIfVpcRpRowStatusTable,
       "mscAtmIfVpcRpRowStatusEntry": mscAtmIfVpcRpRowStatusEntry,
       "mscAtmIfVpcRpRowStatus": mscAtmIfVpcRpRowStatus,
       "mscAtmIfVpcRpComponentName": mscAtmIfVpcRpComponentName,
       "mscAtmIfVpcRpStorageType": mscAtmIfVpcRpStorageType,
       "mscAtmIfVpcRpIndex": mscAtmIfVpcRpIndex,
       "mscAtmIfVpcRpOperTable": mscAtmIfVpcRpOperTable,
       "mscAtmIfVpcRpOperEntry": mscAtmIfVpcRpOperEntry,
       "mscAtmIfVpcRpNextHop": mscAtmIfVpcRpNextHop,
       "mscAtmIfVpcRpNextHopsTable": mscAtmIfVpcRpNextHopsTable,
       "mscAtmIfVpcRpNextHopsEntry": mscAtmIfVpcRpNextHopsEntry,
       "mscAtmIfVpcRpNextHopsValue": mscAtmIfVpcRpNextHopsValue,
       "mscAtmIfVpcDst": mscAtmIfVpcDst,
       "mscAtmIfVpcDstRowStatusTable": mscAtmIfVpcDstRowStatusTable,
       "mscAtmIfVpcDstRowStatusEntry": mscAtmIfVpcDstRowStatusEntry,
       "mscAtmIfVpcDstRowStatus": mscAtmIfVpcDstRowStatus,
       "mscAtmIfVpcDstComponentName": mscAtmIfVpcDstComponentName,
       "mscAtmIfVpcDstStorageType": mscAtmIfVpcDstStorageType,
       "mscAtmIfVpcDstIndex": mscAtmIfVpcDstIndex,
       "mscAtmIfVpcDstOperTable": mscAtmIfVpcDstOperTable,
       "mscAtmIfVpcDstOperEntry": mscAtmIfVpcDstOperEntry,
       "mscAtmIfVpcDstCalledAddress": mscAtmIfVpcDstCalledAddress,
       "mscAtmIfVpcDstCallingAddress": mscAtmIfVpcDstCallingAddress,
       "mscAtmIfVpcDstCallingVpi": mscAtmIfVpcDstCallingVpi,
       "mscAtmIfVccSrc": mscAtmIfVccSrc,
       "mscAtmIfVccSrcRowStatusTable": mscAtmIfVccSrcRowStatusTable,
       "mscAtmIfVccSrcRowStatusEntry": mscAtmIfVccSrcRowStatusEntry,
       "mscAtmIfVccSrcRowStatus": mscAtmIfVccSrcRowStatus,
       "mscAtmIfVccSrcComponentName": mscAtmIfVccSrcComponentName,
       "mscAtmIfVccSrcStorageType": mscAtmIfVccSrcStorageType,
       "mscAtmIfVccSrcIndex": mscAtmIfVccSrcIndex,
       "mscAtmIfVccSrcProvTable": mscAtmIfVccSrcProvTable,
       "mscAtmIfVccSrcProvEntry": mscAtmIfVccSrcProvEntry,
       "mscAtmIfVccSrcRemoteAddress": mscAtmIfVccSrcRemoteAddress,
       "mscAtmIfVccSrcRemoteVpiVci": mscAtmIfVccSrcRemoteVpiVci,
       "mscAtmIfVccSrcCallingAddress": mscAtmIfVccSrcCallingAddress,
       "mscAtmIfVccSrcCalledAddress": mscAtmIfVccSrcCalledAddress,
       "mscAtmIfVccSrcCalledVpiVci": mscAtmIfVccSrcCalledVpiVci,
       "mscAtmIfVccSrcOperTable": mscAtmIfVccSrcOperTable,
       "mscAtmIfVccSrcOperEntry": mscAtmIfVccSrcOperEntry,
       "mscAtmIfVccSrcState": mscAtmIfVccSrcState,
       "mscAtmIfVccSrcRetryCount": mscAtmIfVccSrcRetryCount,
       "mscAtmIfVccSrcLastFailureCauseCode": mscAtmIfVccSrcLastFailureCauseCode,
       "mscAtmIfVccSrcLastFailureDiagCode": mscAtmIfVccSrcLastFailureDiagCode,
       "mscAtmIfVccEp": mscAtmIfVccEp,
       "mscAtmIfVccEpRowStatusTable": mscAtmIfVccEpRowStatusTable,
       "mscAtmIfVccEpRowStatusEntry": mscAtmIfVccEpRowStatusEntry,
       "mscAtmIfVccEpRowStatus": mscAtmIfVccEpRowStatus,
       "mscAtmIfVccEpComponentName": mscAtmIfVccEpComponentName,
       "mscAtmIfVccEpStorageType": mscAtmIfVccEpStorageType,
       "mscAtmIfVccEpIndex": mscAtmIfVccEpIndex,
       "mscAtmIfVccEpOperTable": mscAtmIfVccEpOperTable,
       "mscAtmIfVccEpOperEntry": mscAtmIfVccEpOperEntry,
       "mscAtmIfVccEpApplicationName": mscAtmIfVccEpApplicationName,
       "mscAtmIfVccRp": mscAtmIfVccRp,
       "mscAtmIfVccRpRowStatusTable": mscAtmIfVccRpRowStatusTable,
       "mscAtmIfVccRpRowStatusEntry": mscAtmIfVccRpRowStatusEntry,
       "mscAtmIfVccRpRowStatus": mscAtmIfVccRpRowStatus,
       "mscAtmIfVccRpComponentName": mscAtmIfVccRpComponentName,
       "mscAtmIfVccRpStorageType": mscAtmIfVccRpStorageType,
       "mscAtmIfVccRpIndex": mscAtmIfVccRpIndex,
       "mscAtmIfVccRpOperTable": mscAtmIfVccRpOperTable,
       "mscAtmIfVccRpOperEntry": mscAtmIfVccRpOperEntry,
       "mscAtmIfVccRpNextHop": mscAtmIfVccRpNextHop,
       "mscAtmIfVccRpNextHopsTable": mscAtmIfVccRpNextHopsTable,
       "mscAtmIfVccRpNextHopsEntry": mscAtmIfVccRpNextHopsEntry,
       "mscAtmIfVccRpNextHopsValue": mscAtmIfVccRpNextHopsValue,
       "mscAtmIfVccDst": mscAtmIfVccDst,
       "mscAtmIfVccDstRowStatusTable": mscAtmIfVccDstRowStatusTable,
       "mscAtmIfVccDstRowStatusEntry": mscAtmIfVccDstRowStatusEntry,
       "mscAtmIfVccDstRowStatus": mscAtmIfVccDstRowStatus,
       "mscAtmIfVccDstComponentName": mscAtmIfVccDstComponentName,
       "mscAtmIfVccDstStorageType": mscAtmIfVccDstStorageType,
       "mscAtmIfVccDstIndex": mscAtmIfVccDstIndex,
       "mscAtmIfVccDstOperTable": mscAtmIfVccDstOperTable,
       "mscAtmIfVccDstOperEntry": mscAtmIfVccDstOperEntry,
       "mscAtmIfVccDstCalledAddress": mscAtmIfVccDstCalledAddress,
       "mscAtmIfVccDstCallingAddress": mscAtmIfVccDstCallingAddress,
       "mscAtmIfVccDstCallingVpiVci": mscAtmIfVccDstCallingVpiVci,
       "mscAtmIfVptVccSrc": mscAtmIfVptVccSrc,
       "mscAtmIfVptVccSrcRowStatusTable": mscAtmIfVptVccSrcRowStatusTable,
       "mscAtmIfVptVccSrcRowStatusEntry": mscAtmIfVptVccSrcRowStatusEntry,
       "mscAtmIfVptVccSrcRowStatus": mscAtmIfVptVccSrcRowStatus,
       "mscAtmIfVptVccSrcComponentName": mscAtmIfVptVccSrcComponentName,
       "mscAtmIfVptVccSrcStorageType": mscAtmIfVptVccSrcStorageType,
       "mscAtmIfVptVccSrcIndex": mscAtmIfVptVccSrcIndex,
       "mscAtmIfVptVccSrcProvTable": mscAtmIfVptVccSrcProvTable,
       "mscAtmIfVptVccSrcProvEntry": mscAtmIfVptVccSrcProvEntry,
       "mscAtmIfVptVccSrcRemoteAddress": mscAtmIfVptVccSrcRemoteAddress,
       "mscAtmIfVptVccSrcRemoteVpiVci": mscAtmIfVptVccSrcRemoteVpiVci,
       "mscAtmIfVptVccSrcCallingAddress": mscAtmIfVptVccSrcCallingAddress,
       "mscAtmIfVptVccSrcCalledAddress": mscAtmIfVptVccSrcCalledAddress,
       "mscAtmIfVptVccSrcCalledVpiVci": mscAtmIfVptVccSrcCalledVpiVci,
       "mscAtmIfVptVccSrcOperTable": mscAtmIfVptVccSrcOperTable,
       "mscAtmIfVptVccSrcOperEntry": mscAtmIfVptVccSrcOperEntry,
       "mscAtmIfVptVccSrcState": mscAtmIfVptVccSrcState,
       "mscAtmIfVptVccSrcRetryCount": mscAtmIfVptVccSrcRetryCount,
       "mscAtmIfVptVccSrcLastFailureCauseCode": mscAtmIfVptVccSrcLastFailureCauseCode,
       "mscAtmIfVptVccSrcLastFailureDiagCode": mscAtmIfVptVccSrcLastFailureDiagCode,
       "mscAtmIfVptVccEp": mscAtmIfVptVccEp,
       "mscAtmIfVptVccEpRowStatusTable": mscAtmIfVptVccEpRowStatusTable,
       "mscAtmIfVptVccEpRowStatusEntry": mscAtmIfVptVccEpRowStatusEntry,
       "mscAtmIfVptVccEpRowStatus": mscAtmIfVptVccEpRowStatus,
       "mscAtmIfVptVccEpComponentName": mscAtmIfVptVccEpComponentName,
       "mscAtmIfVptVccEpStorageType": mscAtmIfVptVccEpStorageType,
       "mscAtmIfVptVccEpIndex": mscAtmIfVptVccEpIndex,
       "mscAtmIfVptVccEpOperTable": mscAtmIfVptVccEpOperTable,
       "mscAtmIfVptVccEpOperEntry": mscAtmIfVptVccEpOperEntry,
       "mscAtmIfVptVccEpApplicationName": mscAtmIfVptVccEpApplicationName,
       "mscAtmIfVptVccRp": mscAtmIfVptVccRp,
       "mscAtmIfVptVccRpRowStatusTable": mscAtmIfVptVccRpRowStatusTable,
       "mscAtmIfVptVccRpRowStatusEntry": mscAtmIfVptVccRpRowStatusEntry,
       "mscAtmIfVptVccRpRowStatus": mscAtmIfVptVccRpRowStatus,
       "mscAtmIfVptVccRpComponentName": mscAtmIfVptVccRpComponentName,
       "mscAtmIfVptVccRpStorageType": mscAtmIfVptVccRpStorageType,
       "mscAtmIfVptVccRpIndex": mscAtmIfVptVccRpIndex,
       "mscAtmIfVptVccRpOperTable": mscAtmIfVptVccRpOperTable,
       "mscAtmIfVptVccRpOperEntry": mscAtmIfVptVccRpOperEntry,
       "mscAtmIfVptVccRpNextHop": mscAtmIfVptVccRpNextHop,
       "mscAtmIfVptVccRpNextHopsTable": mscAtmIfVptVccRpNextHopsTable,
       "mscAtmIfVptVccRpNextHopsEntry": mscAtmIfVptVccRpNextHopsEntry,
       "mscAtmIfVptVccRpNextHopsValue": mscAtmIfVptVccRpNextHopsValue,
       "mscAtmIfVptVccDst": mscAtmIfVptVccDst,
       "mscAtmIfVptVccDstRowStatusTable": mscAtmIfVptVccDstRowStatusTable,
       "mscAtmIfVptVccDstRowStatusEntry": mscAtmIfVptVccDstRowStatusEntry,
       "mscAtmIfVptVccDstRowStatus": mscAtmIfVptVccDstRowStatus,
       "mscAtmIfVptVccDstComponentName": mscAtmIfVptVccDstComponentName,
       "mscAtmIfVptVccDstStorageType": mscAtmIfVptVccDstStorageType,
       "mscAtmIfVptVccDstIndex": mscAtmIfVptVccDstIndex,
       "mscAtmIfVptVccDstOperTable": mscAtmIfVptVccDstOperTable,
       "mscAtmIfVptVccDstOperEntry": mscAtmIfVptVccDstOperEntry,
       "mscAtmIfVptVccDstCalledAddress": mscAtmIfVptVccDstCalledAddress,
       "mscAtmIfVptVccDstCallingAddress": mscAtmIfVptVccDstCallingAddress,
       "mscAtmIfVptVccDstCallingVpiVci": mscAtmIfVptVccDstCallingVpiVci,
       "atmNetworkingMIB": atmNetworkingMIB,
       "atmNetworkingGroup": atmNetworkingGroup,
       "atmNetworkingGroupCA": atmNetworkingGroupCA,
       "atmNetworkingGroupCA02": atmNetworkingGroupCA02,
       "atmNetworkingGroupCA02A": atmNetworkingGroupCA02A,
       "atmNetworkingCapabilities": atmNetworkingCapabilities,
       "atmNetworkingCapabilitiesCA": atmNetworkingCapabilitiesCA,
       "atmNetworkingCapabilitiesCA02": atmNetworkingCapabilitiesCA02,
       "atmNetworkingCapabilitiesCA02A": atmNetworkingCapabilitiesCA02A}
)
