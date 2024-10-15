# SNMP MIB module (Nortel-MsCarrier-MscPassport-AtmPnniMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-MsCarrier-MscPassport-AtmPnniMIB
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

(mscAtmIf,
 mscAtmIfIndex,
 mscAtmIfVpt,
 mscAtmIfVptIndex) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-AtmCoreMIB",
    "mscAtmIf",
    "mscAtmIfIndex",
    "mscAtmIfVpt",
    "mscAtmIfVptIndex")

(Counter32,
 DisplayString,
 Gauge32,
 Integer32,
 RowStatus,
 StorageType,
 Unsigned32) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-StandardTextualConventionsMIB",
    "Counter32",
    "DisplayString",
    "Gauge32",
    "Integer32",
    "RowStatus",
    "StorageType",
    "Unsigned32")

(AsciiStringIndex,
 FixedPoint1,
 Hex,
 HexString,
 NonReplicated) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-TextualConventionsMIB",
    "AsciiStringIndex",
    "FixedPoint1",
    "Hex",
    "HexString",
    "NonReplicated")

(mscPassportMIBs,) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-UsefulDefinitionsMIB",
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

_MscAtmIfVptPnni_ObjectIdentity = ObjectIdentity
mscAtmIfVptPnni = _MscAtmIfVptPnni_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7)
)
_MscAtmIfVptPnniRowStatusTable_Object = MibTable
mscAtmIfVptPnniRowStatusTable = _MscAtmIfVptPnniRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 1)
)
if mibBuilder.loadTexts:
    mscAtmIfVptPnniRowStatusTable.setStatus("mandatory")
_MscAtmIfVptPnniRowStatusEntry_Object = MibTableRow
mscAtmIfVptPnniRowStatusEntry = _MscAtmIfVptPnniRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 1, 1)
)
mscAtmIfVptPnniRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVptIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmPnniMIB", "mscAtmIfVptPnniIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfVptPnniRowStatusEntry.setStatus("mandatory")
_MscAtmIfVptPnniRowStatus_Type = RowStatus
_MscAtmIfVptPnniRowStatus_Object = MibTableColumn
mscAtmIfVptPnniRowStatus = _MscAtmIfVptPnniRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 1, 1, 1),
    _MscAtmIfVptPnniRowStatus_Type()
)
mscAtmIfVptPnniRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVptPnniRowStatus.setStatus("mandatory")
_MscAtmIfVptPnniComponentName_Type = DisplayString
_MscAtmIfVptPnniComponentName_Object = MibTableColumn
mscAtmIfVptPnniComponentName = _MscAtmIfVptPnniComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 1, 1, 2),
    _MscAtmIfVptPnniComponentName_Type()
)
mscAtmIfVptPnniComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptPnniComponentName.setStatus("mandatory")
_MscAtmIfVptPnniStorageType_Type = StorageType
_MscAtmIfVptPnniStorageType_Object = MibTableColumn
mscAtmIfVptPnniStorageType = _MscAtmIfVptPnniStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 1, 1, 4),
    _MscAtmIfVptPnniStorageType_Type()
)
mscAtmIfVptPnniStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptPnniStorageType.setStatus("mandatory")
_MscAtmIfVptPnniIndex_Type = NonReplicated
_MscAtmIfVptPnniIndex_Object = MibTableColumn
mscAtmIfVptPnniIndex = _MscAtmIfVptPnniIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 1, 1, 10),
    _MscAtmIfVptPnniIndex_Type()
)
mscAtmIfVptPnniIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAtmIfVptPnniIndex.setStatus("mandatory")
_MscAtmIfVptPnniSig_ObjectIdentity = ObjectIdentity
mscAtmIfVptPnniSig = _MscAtmIfVptPnniSig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 2)
)
_MscAtmIfVptPnniSigRowStatusTable_Object = MibTable
mscAtmIfVptPnniSigRowStatusTable = _MscAtmIfVptPnniSigRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 2, 1)
)
if mibBuilder.loadTexts:
    mscAtmIfVptPnniSigRowStatusTable.setStatus("mandatory")
_MscAtmIfVptPnniSigRowStatusEntry_Object = MibTableRow
mscAtmIfVptPnniSigRowStatusEntry = _MscAtmIfVptPnniSigRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 2, 1, 1)
)
mscAtmIfVptPnniSigRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVptIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmPnniMIB", "mscAtmIfVptPnniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmPnniMIB", "mscAtmIfVptPnniSigIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfVptPnniSigRowStatusEntry.setStatus("mandatory")
_MscAtmIfVptPnniSigRowStatus_Type = RowStatus
_MscAtmIfVptPnniSigRowStatus_Object = MibTableColumn
mscAtmIfVptPnniSigRowStatus = _MscAtmIfVptPnniSigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 2, 1, 1, 1),
    _MscAtmIfVptPnniSigRowStatus_Type()
)
mscAtmIfVptPnniSigRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptPnniSigRowStatus.setStatus("mandatory")
_MscAtmIfVptPnniSigComponentName_Type = DisplayString
_MscAtmIfVptPnniSigComponentName_Object = MibTableColumn
mscAtmIfVptPnniSigComponentName = _MscAtmIfVptPnniSigComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 2, 1, 1, 2),
    _MscAtmIfVptPnniSigComponentName_Type()
)
mscAtmIfVptPnniSigComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptPnniSigComponentName.setStatus("mandatory")
_MscAtmIfVptPnniSigStorageType_Type = StorageType
_MscAtmIfVptPnniSigStorageType_Object = MibTableColumn
mscAtmIfVptPnniSigStorageType = _MscAtmIfVptPnniSigStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 2, 1, 1, 4),
    _MscAtmIfVptPnniSigStorageType_Type()
)
mscAtmIfVptPnniSigStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptPnniSigStorageType.setStatus("mandatory")
_MscAtmIfVptPnniSigIndex_Type = NonReplicated
_MscAtmIfVptPnniSigIndex_Object = MibTableColumn
mscAtmIfVptPnniSigIndex = _MscAtmIfVptPnniSigIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 2, 1, 1, 10),
    _MscAtmIfVptPnniSigIndex_Type()
)
mscAtmIfVptPnniSigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAtmIfVptPnniSigIndex.setStatus("mandatory")
_MscAtmIfVptPnniSigVcd_ObjectIdentity = ObjectIdentity
mscAtmIfVptPnniSigVcd = _MscAtmIfVptPnniSigVcd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 2, 2)
)
_MscAtmIfVptPnniSigVcdRowStatusTable_Object = MibTable
mscAtmIfVptPnniSigVcdRowStatusTable = _MscAtmIfVptPnniSigVcdRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 2, 2, 1)
)
if mibBuilder.loadTexts:
    mscAtmIfVptPnniSigVcdRowStatusTable.setStatus("mandatory")
_MscAtmIfVptPnniSigVcdRowStatusEntry_Object = MibTableRow
mscAtmIfVptPnniSigVcdRowStatusEntry = _MscAtmIfVptPnniSigVcdRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 2, 2, 1, 1)
)
mscAtmIfVptPnniSigVcdRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVptIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmPnniMIB", "mscAtmIfVptPnniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmPnniMIB", "mscAtmIfVptPnniSigIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmPnniMIB", "mscAtmIfVptPnniSigVcdIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfVptPnniSigVcdRowStatusEntry.setStatus("mandatory")
_MscAtmIfVptPnniSigVcdRowStatus_Type = RowStatus
_MscAtmIfVptPnniSigVcdRowStatus_Object = MibTableColumn
mscAtmIfVptPnniSigVcdRowStatus = _MscAtmIfVptPnniSigVcdRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 2, 2, 1, 1, 1),
    _MscAtmIfVptPnniSigVcdRowStatus_Type()
)
mscAtmIfVptPnniSigVcdRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVptPnniSigVcdRowStatus.setStatus("mandatory")
_MscAtmIfVptPnniSigVcdComponentName_Type = DisplayString
_MscAtmIfVptPnniSigVcdComponentName_Object = MibTableColumn
mscAtmIfVptPnniSigVcdComponentName = _MscAtmIfVptPnniSigVcdComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 2, 2, 1, 1, 2),
    _MscAtmIfVptPnniSigVcdComponentName_Type()
)
mscAtmIfVptPnniSigVcdComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptPnniSigVcdComponentName.setStatus("mandatory")
_MscAtmIfVptPnniSigVcdStorageType_Type = StorageType
_MscAtmIfVptPnniSigVcdStorageType_Object = MibTableColumn
mscAtmIfVptPnniSigVcdStorageType = _MscAtmIfVptPnniSigVcdStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 2, 2, 1, 1, 4),
    _MscAtmIfVptPnniSigVcdStorageType_Type()
)
mscAtmIfVptPnniSigVcdStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptPnniSigVcdStorageType.setStatus("mandatory")
_MscAtmIfVptPnniSigVcdIndex_Type = NonReplicated
_MscAtmIfVptPnniSigVcdIndex_Object = MibTableColumn
mscAtmIfVptPnniSigVcdIndex = _MscAtmIfVptPnniSigVcdIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 2, 2, 1, 1, 10),
    _MscAtmIfVptPnniSigVcdIndex_Type()
)
mscAtmIfVptPnniSigVcdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAtmIfVptPnniSigVcdIndex.setStatus("mandatory")
_MscAtmIfVptPnniSigVcdProvTable_Object = MibTable
mscAtmIfVptPnniSigVcdProvTable = _MscAtmIfVptPnniSigVcdProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 2, 2, 10)
)
if mibBuilder.loadTexts:
    mscAtmIfVptPnniSigVcdProvTable.setStatus("mandatory")
_MscAtmIfVptPnniSigVcdProvEntry_Object = MibTableRow
mscAtmIfVptPnniSigVcdProvEntry = _MscAtmIfVptPnniSigVcdProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 2, 2, 10, 1)
)
mscAtmIfVptPnniSigVcdProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVptIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmPnniMIB", "mscAtmIfVptPnniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmPnniMIB", "mscAtmIfVptPnniSigIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmPnniMIB", "mscAtmIfVptPnniSigVcdIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfVptPnniSigVcdProvEntry.setStatus("mandatory")


class _MscAtmIfVptPnniSigVcdTrafficDescType_Type(Integer32):
    """Custom type mscAtmIfVptPnniSigVcdTrafficDescType based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("n3", 3),
          ("n6", 6),
          ("n7", 7),
          ("n8", 8))
    )


_MscAtmIfVptPnniSigVcdTrafficDescType_Type.__name__ = "Integer32"
_MscAtmIfVptPnniSigVcdTrafficDescType_Object = MibTableColumn
mscAtmIfVptPnniSigVcdTrafficDescType = _MscAtmIfVptPnniSigVcdTrafficDescType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 2, 2, 10, 1, 1),
    _MscAtmIfVptPnniSigVcdTrafficDescType_Type()
)
mscAtmIfVptPnniSigVcdTrafficDescType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVptPnniSigVcdTrafficDescType.setStatus("mandatory")


class _MscAtmIfVptPnniSigVcdAtmServiceCategory_Type(Integer32):
    """Custom type mscAtmIfVptPnniSigVcdAtmServiceCategory based on Integer32"""
    defaultValue = 2

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
        *(("constantBitRate", 1),
          ("nrtVariableBitRate", 3),
          ("rtVariableBitRate", 2),
          ("unspecifiedBitRate", 0))
    )


_MscAtmIfVptPnniSigVcdAtmServiceCategory_Type.__name__ = "Integer32"
_MscAtmIfVptPnniSigVcdAtmServiceCategory_Object = MibTableColumn
mscAtmIfVptPnniSigVcdAtmServiceCategory = _MscAtmIfVptPnniSigVcdAtmServiceCategory_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 2, 2, 10, 1, 3),
    _MscAtmIfVptPnniSigVcdAtmServiceCategory_Type()
)
mscAtmIfVptPnniSigVcdAtmServiceCategory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVptPnniSigVcdAtmServiceCategory.setStatus("mandatory")


class _MscAtmIfVptPnniSigVcdWeight_Type(Unsigned32):
    """Custom type mscAtmIfVptPnniSigVcdWeight based on Unsigned32"""
    defaultValue = 65535

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4095),
        ValueRangeConstraint(65535, 65535),
    )


_MscAtmIfVptPnniSigVcdWeight_Type.__name__ = "Unsigned32"
_MscAtmIfVptPnniSigVcdWeight_Object = MibTableColumn
mscAtmIfVptPnniSigVcdWeight = _MscAtmIfVptPnniSigVcdWeight_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 2, 2, 10, 1, 4),
    _MscAtmIfVptPnniSigVcdWeight_Type()
)
mscAtmIfVptPnniSigVcdWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVptPnniSigVcdWeight.setStatus("mandatory")


class _MscAtmIfVptPnniSigVcdQosClass_Type(Integer32):
    """Custom type mscAtmIfVptPnniSigVcdQosClass based on Integer32"""
    defaultValue = 2

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


_MscAtmIfVptPnniSigVcdQosClass_Type.__name__ = "Integer32"
_MscAtmIfVptPnniSigVcdQosClass_Object = MibTableColumn
mscAtmIfVptPnniSigVcdQosClass = _MscAtmIfVptPnniSigVcdQosClass_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 2, 2, 10, 1, 21),
    _MscAtmIfVptPnniSigVcdQosClass_Type()
)
mscAtmIfVptPnniSigVcdQosClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVptPnniSigVcdQosClass.setStatus("mandatory")


class _MscAtmIfVptPnniSigVcdTrafficShaping_Type(Integer32):
    """Custom type mscAtmIfVptPnniSigVcdTrafficShaping based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("sameAsCa", 2))
    )


_MscAtmIfVptPnniSigVcdTrafficShaping_Type.__name__ = "Integer32"
_MscAtmIfVptPnniSigVcdTrafficShaping_Object = MibTableColumn
mscAtmIfVptPnniSigVcdTrafficShaping = _MscAtmIfVptPnniSigVcdTrafficShaping_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 2, 2, 10, 1, 50),
    _MscAtmIfVptPnniSigVcdTrafficShaping_Type()
)
mscAtmIfVptPnniSigVcdTrafficShaping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVptPnniSigVcdTrafficShaping.setStatus("mandatory")


class _MscAtmIfVptPnniSigVcdUnshapedTransmitQueueing_Type(Integer32):
    """Custom type mscAtmIfVptPnniSigVcdUnshapedTransmitQueueing based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("common", 1),
          ("sameAsCa", 3))
    )


_MscAtmIfVptPnniSigVcdUnshapedTransmitQueueing_Type.__name__ = "Integer32"
_MscAtmIfVptPnniSigVcdUnshapedTransmitQueueing_Object = MibTableColumn
mscAtmIfVptPnniSigVcdUnshapedTransmitQueueing = _MscAtmIfVptPnniSigVcdUnshapedTransmitQueueing_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 2, 2, 10, 1, 60),
    _MscAtmIfVptPnniSigVcdUnshapedTransmitQueueing_Type()
)
mscAtmIfVptPnniSigVcdUnshapedTransmitQueueing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVptPnniSigVcdUnshapedTransmitQueueing.setStatus("mandatory")


class _MscAtmIfVptPnniSigVcdUsageParameterControl_Type(Integer32):
    """Custom type mscAtmIfVptPnniSigVcdUsageParameterControl based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("sameAsCa", 2))
    )


_MscAtmIfVptPnniSigVcdUsageParameterControl_Type.__name__ = "Integer32"
_MscAtmIfVptPnniSigVcdUsageParameterControl_Object = MibTableColumn
mscAtmIfVptPnniSigVcdUsageParameterControl = _MscAtmIfVptPnniSigVcdUsageParameterControl_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 2, 2, 10, 1, 70),
    _MscAtmIfVptPnniSigVcdUsageParameterControl_Type()
)
mscAtmIfVptPnniSigVcdUsageParameterControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVptPnniSigVcdUsageParameterControl.setStatus("mandatory")
_MscAtmIfVptPnniSigVcdTdpTable_Object = MibTable
mscAtmIfVptPnniSigVcdTdpTable = _MscAtmIfVptPnniSigVcdTdpTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 2, 2, 387)
)
if mibBuilder.loadTexts:
    mscAtmIfVptPnniSigVcdTdpTable.setStatus("mandatory")
_MscAtmIfVptPnniSigVcdTdpEntry_Object = MibTableRow
mscAtmIfVptPnniSigVcdTdpEntry = _MscAtmIfVptPnniSigVcdTdpEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 2, 2, 387, 1)
)
mscAtmIfVptPnniSigVcdTdpEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVptIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmPnniMIB", "mscAtmIfVptPnniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmPnniMIB", "mscAtmIfVptPnniSigIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmPnniMIB", "mscAtmIfVptPnniSigVcdIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmPnniMIB", "mscAtmIfVptPnniSigVcdTdpIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfVptPnniSigVcdTdpEntry.setStatus("mandatory")


class _MscAtmIfVptPnniSigVcdTdpIndex_Type(Integer32):
    """Custom type mscAtmIfVptPnniSigVcdTdpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_MscAtmIfVptPnniSigVcdTdpIndex_Type.__name__ = "Integer32"
_MscAtmIfVptPnniSigVcdTdpIndex_Object = MibTableColumn
mscAtmIfVptPnniSigVcdTdpIndex = _MscAtmIfVptPnniSigVcdTdpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 2, 2, 387, 1, 1),
    _MscAtmIfVptPnniSigVcdTdpIndex_Type()
)
mscAtmIfVptPnniSigVcdTdpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAtmIfVptPnniSigVcdTdpIndex.setStatus("mandatory")


class _MscAtmIfVptPnniSigVcdTdpValue_Type(Unsigned32):
    """Custom type mscAtmIfVptPnniSigVcdTdpValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MscAtmIfVptPnniSigVcdTdpValue_Type.__name__ = "Unsigned32"
_MscAtmIfVptPnniSigVcdTdpValue_Object = MibTableColumn
mscAtmIfVptPnniSigVcdTdpValue = _MscAtmIfVptPnniSigVcdTdpValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 2, 2, 387, 1, 2),
    _MscAtmIfVptPnniSigVcdTdpValue_Type()
)
mscAtmIfVptPnniSigVcdTdpValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVptPnniSigVcdTdpValue.setStatus("mandatory")
_MscAtmIfVptPnniSigProvTable_Object = MibTable
mscAtmIfVptPnniSigProvTable = _MscAtmIfVptPnniSigProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 2, 10)
)
if mibBuilder.loadTexts:
    mscAtmIfVptPnniSigProvTable.setStatus("mandatory")
_MscAtmIfVptPnniSigProvEntry_Object = MibTableRow
mscAtmIfVptPnniSigProvEntry = _MscAtmIfVptPnniSigProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 2, 10, 1)
)
mscAtmIfVptPnniSigProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVptIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmPnniMIB", "mscAtmIfVptPnniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmPnniMIB", "mscAtmIfVptPnniSigIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfVptPnniSigProvEntry.setStatus("mandatory")


class _MscAtmIfVptPnniSigVci_Type(Unsigned32):
    """Custom type mscAtmIfVptPnniSigVci based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscAtmIfVptPnniSigVci_Type.__name__ = "Unsigned32"
_MscAtmIfVptPnniSigVci_Object = MibTableColumn
mscAtmIfVptPnniSigVci = _MscAtmIfVptPnniSigVci_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 2, 10, 1, 1),
    _MscAtmIfVptPnniSigVci_Type()
)
mscAtmIfVptPnniSigVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVptPnniSigVci.setStatus("mandatory")


class _MscAtmIfVptPnniSigAddressConversion_Type(Integer32):
    """Custom type mscAtmIfVptPnniSigAddressConversion based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nativeE164", 1),
          ("none", 0),
          ("nsap", 2))
    )


_MscAtmIfVptPnniSigAddressConversion_Type.__name__ = "Integer32"
_MscAtmIfVptPnniSigAddressConversion_Object = MibTableColumn
mscAtmIfVptPnniSigAddressConversion = _MscAtmIfVptPnniSigAddressConversion_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 2, 10, 1, 2),
    _MscAtmIfVptPnniSigAddressConversion_Type()
)
mscAtmIfVptPnniSigAddressConversion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVptPnniSigAddressConversion.setStatus("mandatory")


class _MscAtmIfVptPnniSigOperatingMode_Type(Integer32):
    """Custom type mscAtmIfVptPnniSigOperatingMode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("provisionedOnly", 1))
    )


_MscAtmIfVptPnniSigOperatingMode_Type.__name__ = "Integer32"
_MscAtmIfVptPnniSigOperatingMode_Object = MibTableColumn
mscAtmIfVptPnniSigOperatingMode = _MscAtmIfVptPnniSigOperatingMode_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 2, 10, 1, 3),
    _MscAtmIfVptPnniSigOperatingMode_Type()
)
mscAtmIfVptPnniSigOperatingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVptPnniSigOperatingMode.setStatus("mandatory")
_MscAtmIfVptPnniSigStateTable_Object = MibTable
mscAtmIfVptPnniSigStateTable = _MscAtmIfVptPnniSigStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 2, 11)
)
if mibBuilder.loadTexts:
    mscAtmIfVptPnniSigStateTable.setStatus("mandatory")
_MscAtmIfVptPnniSigStateEntry_Object = MibTableRow
mscAtmIfVptPnniSigStateEntry = _MscAtmIfVptPnniSigStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 2, 11, 1)
)
mscAtmIfVptPnniSigStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVptIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmPnniMIB", "mscAtmIfVptPnniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmPnniMIB", "mscAtmIfVptPnniSigIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfVptPnniSigStateEntry.setStatus("mandatory")


class _MscAtmIfVptPnniSigAdminState_Type(Integer32):
    """Custom type mscAtmIfVptPnniSigAdminState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("locked", 0),
          ("shuttingDown", 2),
          ("unlocked", 1))
    )


_MscAtmIfVptPnniSigAdminState_Type.__name__ = "Integer32"
_MscAtmIfVptPnniSigAdminState_Object = MibTableColumn
mscAtmIfVptPnniSigAdminState = _MscAtmIfVptPnniSigAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 2, 11, 1, 1),
    _MscAtmIfVptPnniSigAdminState_Type()
)
mscAtmIfVptPnniSigAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptPnniSigAdminState.setStatus("mandatory")


class _MscAtmIfVptPnniSigOperationalState_Type(Integer32):
    """Custom type mscAtmIfVptPnniSigOperationalState based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_MscAtmIfVptPnniSigOperationalState_Type.__name__ = "Integer32"
_MscAtmIfVptPnniSigOperationalState_Object = MibTableColumn
mscAtmIfVptPnniSigOperationalState = _MscAtmIfVptPnniSigOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 2, 11, 1, 2),
    _MscAtmIfVptPnniSigOperationalState_Type()
)
mscAtmIfVptPnniSigOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptPnniSigOperationalState.setStatus("mandatory")


class _MscAtmIfVptPnniSigUsageState_Type(Integer32):
    """Custom type mscAtmIfVptPnniSigUsageState based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("busy", 2),
          ("idle", 0))
    )


_MscAtmIfVptPnniSigUsageState_Type.__name__ = "Integer32"
_MscAtmIfVptPnniSigUsageState_Object = MibTableColumn
mscAtmIfVptPnniSigUsageState = _MscAtmIfVptPnniSigUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 2, 11, 1, 3),
    _MscAtmIfVptPnniSigUsageState_Type()
)
mscAtmIfVptPnniSigUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptPnniSigUsageState.setStatus("mandatory")
_MscAtmIfVptPnniSigOperTable_Object = MibTable
mscAtmIfVptPnniSigOperTable = _MscAtmIfVptPnniSigOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 2, 12)
)
if mibBuilder.loadTexts:
    mscAtmIfVptPnniSigOperTable.setStatus("mandatory")
_MscAtmIfVptPnniSigOperEntry_Object = MibTableRow
mscAtmIfVptPnniSigOperEntry = _MscAtmIfVptPnniSigOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 2, 12, 1)
)
mscAtmIfVptPnniSigOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVptIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmPnniMIB", "mscAtmIfVptPnniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmPnniMIB", "mscAtmIfVptPnniSigIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfVptPnniSigOperEntry.setStatus("mandatory")


class _MscAtmIfVptPnniSigLastTxCauseCode_Type(Unsigned32):
    """Custom type mscAtmIfVptPnniSigLastTxCauseCode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscAtmIfVptPnniSigLastTxCauseCode_Type.__name__ = "Unsigned32"
_MscAtmIfVptPnniSigLastTxCauseCode_Object = MibTableColumn
mscAtmIfVptPnniSigLastTxCauseCode = _MscAtmIfVptPnniSigLastTxCauseCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 2, 12, 1, 1),
    _MscAtmIfVptPnniSigLastTxCauseCode_Type()
)
mscAtmIfVptPnniSigLastTxCauseCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptPnniSigLastTxCauseCode.setStatus("mandatory")


class _MscAtmIfVptPnniSigLastTxDiagCode_Type(Hex):
    """Custom type mscAtmIfVptPnniSigLastTxDiagCode based on Hex"""
    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscAtmIfVptPnniSigLastTxDiagCode_Type.__name__ = "Hex"
_MscAtmIfVptPnniSigLastTxDiagCode_Object = MibTableColumn
mscAtmIfVptPnniSigLastTxDiagCode = _MscAtmIfVptPnniSigLastTxDiagCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 2, 12, 1, 2),
    _MscAtmIfVptPnniSigLastTxDiagCode_Type()
)
mscAtmIfVptPnniSigLastTxDiagCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptPnniSigLastTxDiagCode.setStatus("mandatory")


class _MscAtmIfVptPnniSigLastRxCauseCode_Type(Unsigned32):
    """Custom type mscAtmIfVptPnniSigLastRxCauseCode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscAtmIfVptPnniSigLastRxCauseCode_Type.__name__ = "Unsigned32"
_MscAtmIfVptPnniSigLastRxCauseCode_Object = MibTableColumn
mscAtmIfVptPnniSigLastRxCauseCode = _MscAtmIfVptPnniSigLastRxCauseCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 2, 12, 1, 3),
    _MscAtmIfVptPnniSigLastRxCauseCode_Type()
)
mscAtmIfVptPnniSigLastRxCauseCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptPnniSigLastRxCauseCode.setStatus("mandatory")


class _MscAtmIfVptPnniSigLastRxDiagCode_Type(Hex):
    """Custom type mscAtmIfVptPnniSigLastRxDiagCode based on Hex"""
    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscAtmIfVptPnniSigLastRxDiagCode_Type.__name__ = "Hex"
_MscAtmIfVptPnniSigLastRxDiagCode_Object = MibTableColumn
mscAtmIfVptPnniSigLastRxDiagCode = _MscAtmIfVptPnniSigLastRxDiagCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 2, 12, 1, 4),
    _MscAtmIfVptPnniSigLastRxDiagCode_Type()
)
mscAtmIfVptPnniSigLastRxDiagCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptPnniSigLastRxDiagCode.setStatus("mandatory")
_MscAtmIfVptPnniSigStatsTable_Object = MibTable
mscAtmIfVptPnniSigStatsTable = _MscAtmIfVptPnniSigStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 2, 13)
)
if mibBuilder.loadTexts:
    mscAtmIfVptPnniSigStatsTable.setStatus("mandatory")
_MscAtmIfVptPnniSigStatsEntry_Object = MibTableRow
mscAtmIfVptPnniSigStatsEntry = _MscAtmIfVptPnniSigStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 2, 13, 1)
)
mscAtmIfVptPnniSigStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVptIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmPnniMIB", "mscAtmIfVptPnniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmPnniMIB", "mscAtmIfVptPnniSigIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfVptPnniSigStatsEntry.setStatus("mandatory")
_MscAtmIfVptPnniSigCurrentConnections_Type = Counter32
_MscAtmIfVptPnniSigCurrentConnections_Object = MibTableColumn
mscAtmIfVptPnniSigCurrentConnections = _MscAtmIfVptPnniSigCurrentConnections_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 2, 13, 1, 1),
    _MscAtmIfVptPnniSigCurrentConnections_Type()
)
mscAtmIfVptPnniSigCurrentConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptPnniSigCurrentConnections.setStatus("obsolete")


class _MscAtmIfVptPnniSigPeakConnections_Type(Gauge32):
    """Custom type mscAtmIfVptPnniSigPeakConnections based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscAtmIfVptPnniSigPeakConnections_Type.__name__ = "Gauge32"
_MscAtmIfVptPnniSigPeakConnections_Object = MibTableColumn
mscAtmIfVptPnniSigPeakConnections = _MscAtmIfVptPnniSigPeakConnections_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 2, 13, 1, 2),
    _MscAtmIfVptPnniSigPeakConnections_Type()
)
mscAtmIfVptPnniSigPeakConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptPnniSigPeakConnections.setStatus("mandatory")
_MscAtmIfVptPnniSigSuccessfulConnections_Type = Counter32
_MscAtmIfVptPnniSigSuccessfulConnections_Object = MibTableColumn
mscAtmIfVptPnniSigSuccessfulConnections = _MscAtmIfVptPnniSigSuccessfulConnections_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 2, 13, 1, 3),
    _MscAtmIfVptPnniSigSuccessfulConnections_Type()
)
mscAtmIfVptPnniSigSuccessfulConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptPnniSigSuccessfulConnections.setStatus("mandatory")
_MscAtmIfVptPnniSigFailedConnections_Type = Counter32
_MscAtmIfVptPnniSigFailedConnections_Object = MibTableColumn
mscAtmIfVptPnniSigFailedConnections = _MscAtmIfVptPnniSigFailedConnections_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 2, 13, 1, 4),
    _MscAtmIfVptPnniSigFailedConnections_Type()
)
mscAtmIfVptPnniSigFailedConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptPnniSigFailedConnections.setStatus("mandatory")
_MscAtmIfVptPnniSigTxPdus_Type = Counter32
_MscAtmIfVptPnniSigTxPdus_Object = MibTableColumn
mscAtmIfVptPnniSigTxPdus = _MscAtmIfVptPnniSigTxPdus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 2, 13, 1, 5),
    _MscAtmIfVptPnniSigTxPdus_Type()
)
mscAtmIfVptPnniSigTxPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptPnniSigTxPdus.setStatus("mandatory")
_MscAtmIfVptPnniSigRxPdus_Type = Counter32
_MscAtmIfVptPnniSigRxPdus_Object = MibTableColumn
mscAtmIfVptPnniSigRxPdus = _MscAtmIfVptPnniSigRxPdus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 2, 13, 1, 6),
    _MscAtmIfVptPnniSigRxPdus_Type()
)
mscAtmIfVptPnniSigRxPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptPnniSigRxPdus.setStatus("mandatory")


class _MscAtmIfVptPnniSigCurrentPmpConnections_Type(Gauge32):
    """Custom type mscAtmIfVptPnniSigCurrentPmpConnections based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscAtmIfVptPnniSigCurrentPmpConnections_Type.__name__ = "Gauge32"
_MscAtmIfVptPnniSigCurrentPmpConnections_Object = MibTableColumn
mscAtmIfVptPnniSigCurrentPmpConnections = _MscAtmIfVptPnniSigCurrentPmpConnections_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 2, 13, 1, 7),
    _MscAtmIfVptPnniSigCurrentPmpConnections_Type()
)
mscAtmIfVptPnniSigCurrentPmpConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptPnniSigCurrentPmpConnections.setStatus("mandatory")


class _MscAtmIfVptPnniSigPeakPmpConnections_Type(Gauge32):
    """Custom type mscAtmIfVptPnniSigPeakPmpConnections based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscAtmIfVptPnniSigPeakPmpConnections_Type.__name__ = "Gauge32"
_MscAtmIfVptPnniSigPeakPmpConnections_Object = MibTableColumn
mscAtmIfVptPnniSigPeakPmpConnections = _MscAtmIfVptPnniSigPeakPmpConnections_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 2, 13, 1, 8),
    _MscAtmIfVptPnniSigPeakPmpConnections_Type()
)
mscAtmIfVptPnniSigPeakPmpConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptPnniSigPeakPmpConnections.setStatus("mandatory")
_MscAtmIfVptPnniSigSuccessfulPmpConnections_Type = Counter32
_MscAtmIfVptPnniSigSuccessfulPmpConnections_Object = MibTableColumn
mscAtmIfVptPnniSigSuccessfulPmpConnections = _MscAtmIfVptPnniSigSuccessfulPmpConnections_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 2, 13, 1, 9),
    _MscAtmIfVptPnniSigSuccessfulPmpConnections_Type()
)
mscAtmIfVptPnniSigSuccessfulPmpConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptPnniSigSuccessfulPmpConnections.setStatus("mandatory")
_MscAtmIfVptPnniSigFailedPmpConnections_Type = Counter32
_MscAtmIfVptPnniSigFailedPmpConnections_Object = MibTableColumn
mscAtmIfVptPnniSigFailedPmpConnections = _MscAtmIfVptPnniSigFailedPmpConnections_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 2, 13, 1, 10),
    _MscAtmIfVptPnniSigFailedPmpConnections_Type()
)
mscAtmIfVptPnniSigFailedPmpConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptPnniSigFailedPmpConnections.setStatus("mandatory")


class _MscAtmIfVptPnniSigNewCurrentConnections_Type(Gauge32):
    """Custom type mscAtmIfVptPnniSigNewCurrentConnections based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscAtmIfVptPnniSigNewCurrentConnections_Type.__name__ = "Gauge32"
_MscAtmIfVptPnniSigNewCurrentConnections_Object = MibTableColumn
mscAtmIfVptPnniSigNewCurrentConnections = _MscAtmIfVptPnniSigNewCurrentConnections_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 2, 13, 1, 11),
    _MscAtmIfVptPnniSigNewCurrentConnections_Type()
)
mscAtmIfVptPnniSigNewCurrentConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptPnniSigNewCurrentConnections.setStatus("mandatory")
_MscAtmIfVptPnniRcc_ObjectIdentity = ObjectIdentity
mscAtmIfVptPnniRcc = _MscAtmIfVptPnniRcc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 3)
)
_MscAtmIfVptPnniRccRowStatusTable_Object = MibTable
mscAtmIfVptPnniRccRowStatusTable = _MscAtmIfVptPnniRccRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 3, 1)
)
if mibBuilder.loadTexts:
    mscAtmIfVptPnniRccRowStatusTable.setStatus("mandatory")
_MscAtmIfVptPnniRccRowStatusEntry_Object = MibTableRow
mscAtmIfVptPnniRccRowStatusEntry = _MscAtmIfVptPnniRccRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 3, 1, 1)
)
mscAtmIfVptPnniRccRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVptIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmPnniMIB", "mscAtmIfVptPnniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmPnniMIB", "mscAtmIfVptPnniRccIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfVptPnniRccRowStatusEntry.setStatus("mandatory")
_MscAtmIfVptPnniRccRowStatus_Type = RowStatus
_MscAtmIfVptPnniRccRowStatus_Object = MibTableColumn
mscAtmIfVptPnniRccRowStatus = _MscAtmIfVptPnniRccRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 3, 1, 1, 1),
    _MscAtmIfVptPnniRccRowStatus_Type()
)
mscAtmIfVptPnniRccRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptPnniRccRowStatus.setStatus("mandatory")
_MscAtmIfVptPnniRccComponentName_Type = DisplayString
_MscAtmIfVptPnniRccComponentName_Object = MibTableColumn
mscAtmIfVptPnniRccComponentName = _MscAtmIfVptPnniRccComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 3, 1, 1, 2),
    _MscAtmIfVptPnniRccComponentName_Type()
)
mscAtmIfVptPnniRccComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptPnniRccComponentName.setStatus("mandatory")
_MscAtmIfVptPnniRccStorageType_Type = StorageType
_MscAtmIfVptPnniRccStorageType_Object = MibTableColumn
mscAtmIfVptPnniRccStorageType = _MscAtmIfVptPnniRccStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 3, 1, 1, 4),
    _MscAtmIfVptPnniRccStorageType_Type()
)
mscAtmIfVptPnniRccStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptPnniRccStorageType.setStatus("mandatory")
_MscAtmIfVptPnniRccIndex_Type = NonReplicated
_MscAtmIfVptPnniRccIndex_Object = MibTableColumn
mscAtmIfVptPnniRccIndex = _MscAtmIfVptPnniRccIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 3, 1, 1, 10),
    _MscAtmIfVptPnniRccIndex_Type()
)
mscAtmIfVptPnniRccIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAtmIfVptPnniRccIndex.setStatus("mandatory")
_MscAtmIfVptPnniRccVcd_ObjectIdentity = ObjectIdentity
mscAtmIfVptPnniRccVcd = _MscAtmIfVptPnniRccVcd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 3, 2)
)
_MscAtmIfVptPnniRccVcdRowStatusTable_Object = MibTable
mscAtmIfVptPnniRccVcdRowStatusTable = _MscAtmIfVptPnniRccVcdRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 3, 2, 1)
)
if mibBuilder.loadTexts:
    mscAtmIfVptPnniRccVcdRowStatusTable.setStatus("mandatory")
_MscAtmIfVptPnniRccVcdRowStatusEntry_Object = MibTableRow
mscAtmIfVptPnniRccVcdRowStatusEntry = _MscAtmIfVptPnniRccVcdRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 3, 2, 1, 1)
)
mscAtmIfVptPnniRccVcdRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVptIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmPnniMIB", "mscAtmIfVptPnniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmPnniMIB", "mscAtmIfVptPnniRccIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmPnniMIB", "mscAtmIfVptPnniRccVcdIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfVptPnniRccVcdRowStatusEntry.setStatus("mandatory")
_MscAtmIfVptPnniRccVcdRowStatus_Type = RowStatus
_MscAtmIfVptPnniRccVcdRowStatus_Object = MibTableColumn
mscAtmIfVptPnniRccVcdRowStatus = _MscAtmIfVptPnniRccVcdRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 3, 2, 1, 1, 1),
    _MscAtmIfVptPnniRccVcdRowStatus_Type()
)
mscAtmIfVptPnniRccVcdRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVptPnniRccVcdRowStatus.setStatus("mandatory")
_MscAtmIfVptPnniRccVcdComponentName_Type = DisplayString
_MscAtmIfVptPnniRccVcdComponentName_Object = MibTableColumn
mscAtmIfVptPnniRccVcdComponentName = _MscAtmIfVptPnniRccVcdComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 3, 2, 1, 1, 2),
    _MscAtmIfVptPnniRccVcdComponentName_Type()
)
mscAtmIfVptPnniRccVcdComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptPnniRccVcdComponentName.setStatus("mandatory")
_MscAtmIfVptPnniRccVcdStorageType_Type = StorageType
_MscAtmIfVptPnniRccVcdStorageType_Object = MibTableColumn
mscAtmIfVptPnniRccVcdStorageType = _MscAtmIfVptPnniRccVcdStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 3, 2, 1, 1, 4),
    _MscAtmIfVptPnniRccVcdStorageType_Type()
)
mscAtmIfVptPnniRccVcdStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptPnniRccVcdStorageType.setStatus("mandatory")
_MscAtmIfVptPnniRccVcdIndex_Type = NonReplicated
_MscAtmIfVptPnniRccVcdIndex_Object = MibTableColumn
mscAtmIfVptPnniRccVcdIndex = _MscAtmIfVptPnniRccVcdIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 3, 2, 1, 1, 10),
    _MscAtmIfVptPnniRccVcdIndex_Type()
)
mscAtmIfVptPnniRccVcdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAtmIfVptPnniRccVcdIndex.setStatus("mandatory")
_MscAtmIfVptPnniRccVcdProvTable_Object = MibTable
mscAtmIfVptPnniRccVcdProvTable = _MscAtmIfVptPnniRccVcdProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 3, 2, 10)
)
if mibBuilder.loadTexts:
    mscAtmIfVptPnniRccVcdProvTable.setStatus("mandatory")
_MscAtmIfVptPnniRccVcdProvEntry_Object = MibTableRow
mscAtmIfVptPnniRccVcdProvEntry = _MscAtmIfVptPnniRccVcdProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 3, 2, 10, 1)
)
mscAtmIfVptPnniRccVcdProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVptIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmPnniMIB", "mscAtmIfVptPnniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmPnniMIB", "mscAtmIfVptPnniRccIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmPnniMIB", "mscAtmIfVptPnniRccVcdIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfVptPnniRccVcdProvEntry.setStatus("mandatory")


class _MscAtmIfVptPnniRccVcdTrafficDescType_Type(Integer32):
    """Custom type mscAtmIfVptPnniRccVcdTrafficDescType based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("n3", 3),
          ("n6", 6),
          ("n7", 7),
          ("n8", 8))
    )


_MscAtmIfVptPnniRccVcdTrafficDescType_Type.__name__ = "Integer32"
_MscAtmIfVptPnniRccVcdTrafficDescType_Object = MibTableColumn
mscAtmIfVptPnniRccVcdTrafficDescType = _MscAtmIfVptPnniRccVcdTrafficDescType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 3, 2, 10, 1, 1),
    _MscAtmIfVptPnniRccVcdTrafficDescType_Type()
)
mscAtmIfVptPnniRccVcdTrafficDescType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVptPnniRccVcdTrafficDescType.setStatus("mandatory")


class _MscAtmIfVptPnniRccVcdAtmServiceCategory_Type(Integer32):
    """Custom type mscAtmIfVptPnniRccVcdAtmServiceCategory based on Integer32"""
    defaultValue = 2

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
        *(("constantBitRate", 1),
          ("nrtVariableBitRate", 3),
          ("rtVariableBitRate", 2),
          ("unspecifiedBitRate", 0))
    )


_MscAtmIfVptPnniRccVcdAtmServiceCategory_Type.__name__ = "Integer32"
_MscAtmIfVptPnniRccVcdAtmServiceCategory_Object = MibTableColumn
mscAtmIfVptPnniRccVcdAtmServiceCategory = _MscAtmIfVptPnniRccVcdAtmServiceCategory_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 3, 2, 10, 1, 3),
    _MscAtmIfVptPnniRccVcdAtmServiceCategory_Type()
)
mscAtmIfVptPnniRccVcdAtmServiceCategory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVptPnniRccVcdAtmServiceCategory.setStatus("mandatory")


class _MscAtmIfVptPnniRccVcdWeight_Type(Unsigned32):
    """Custom type mscAtmIfVptPnniRccVcdWeight based on Unsigned32"""
    defaultValue = 65535

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4095),
        ValueRangeConstraint(65535, 65535),
    )


_MscAtmIfVptPnniRccVcdWeight_Type.__name__ = "Unsigned32"
_MscAtmIfVptPnniRccVcdWeight_Object = MibTableColumn
mscAtmIfVptPnniRccVcdWeight = _MscAtmIfVptPnniRccVcdWeight_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 3, 2, 10, 1, 4),
    _MscAtmIfVptPnniRccVcdWeight_Type()
)
mscAtmIfVptPnniRccVcdWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVptPnniRccVcdWeight.setStatus("mandatory")


class _MscAtmIfVptPnniRccVcdQosClass_Type(Integer32):
    """Custom type mscAtmIfVptPnniRccVcdQosClass based on Integer32"""
    defaultValue = 2

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


_MscAtmIfVptPnniRccVcdQosClass_Type.__name__ = "Integer32"
_MscAtmIfVptPnniRccVcdQosClass_Object = MibTableColumn
mscAtmIfVptPnniRccVcdQosClass = _MscAtmIfVptPnniRccVcdQosClass_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 3, 2, 10, 1, 21),
    _MscAtmIfVptPnniRccVcdQosClass_Type()
)
mscAtmIfVptPnniRccVcdQosClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVptPnniRccVcdQosClass.setStatus("mandatory")


class _MscAtmIfVptPnniRccVcdTrafficShaping_Type(Integer32):
    """Custom type mscAtmIfVptPnniRccVcdTrafficShaping based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("sameAsCa", 2))
    )


_MscAtmIfVptPnniRccVcdTrafficShaping_Type.__name__ = "Integer32"
_MscAtmIfVptPnniRccVcdTrafficShaping_Object = MibTableColumn
mscAtmIfVptPnniRccVcdTrafficShaping = _MscAtmIfVptPnniRccVcdTrafficShaping_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 3, 2, 10, 1, 50),
    _MscAtmIfVptPnniRccVcdTrafficShaping_Type()
)
mscAtmIfVptPnniRccVcdTrafficShaping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVptPnniRccVcdTrafficShaping.setStatus("mandatory")


class _MscAtmIfVptPnniRccVcdUnshapedTransmitQueueing_Type(Integer32):
    """Custom type mscAtmIfVptPnniRccVcdUnshapedTransmitQueueing based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("common", 1),
          ("sameAsCa", 3))
    )


_MscAtmIfVptPnniRccVcdUnshapedTransmitQueueing_Type.__name__ = "Integer32"
_MscAtmIfVptPnniRccVcdUnshapedTransmitQueueing_Object = MibTableColumn
mscAtmIfVptPnniRccVcdUnshapedTransmitQueueing = _MscAtmIfVptPnniRccVcdUnshapedTransmitQueueing_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 3, 2, 10, 1, 60),
    _MscAtmIfVptPnniRccVcdUnshapedTransmitQueueing_Type()
)
mscAtmIfVptPnniRccVcdUnshapedTransmitQueueing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVptPnniRccVcdUnshapedTransmitQueueing.setStatus("mandatory")


class _MscAtmIfVptPnniRccVcdUsageParameterControl_Type(Integer32):
    """Custom type mscAtmIfVptPnniRccVcdUsageParameterControl based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("sameAsCa", 2))
    )


_MscAtmIfVptPnniRccVcdUsageParameterControl_Type.__name__ = "Integer32"
_MscAtmIfVptPnniRccVcdUsageParameterControl_Object = MibTableColumn
mscAtmIfVptPnniRccVcdUsageParameterControl = _MscAtmIfVptPnniRccVcdUsageParameterControl_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 3, 2, 10, 1, 70),
    _MscAtmIfVptPnniRccVcdUsageParameterControl_Type()
)
mscAtmIfVptPnniRccVcdUsageParameterControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVptPnniRccVcdUsageParameterControl.setStatus("mandatory")
_MscAtmIfVptPnniRccVcdTdpTable_Object = MibTable
mscAtmIfVptPnniRccVcdTdpTable = _MscAtmIfVptPnniRccVcdTdpTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 3, 2, 387)
)
if mibBuilder.loadTexts:
    mscAtmIfVptPnniRccVcdTdpTable.setStatus("mandatory")
_MscAtmIfVptPnniRccVcdTdpEntry_Object = MibTableRow
mscAtmIfVptPnniRccVcdTdpEntry = _MscAtmIfVptPnniRccVcdTdpEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 3, 2, 387, 1)
)
mscAtmIfVptPnniRccVcdTdpEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVptIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmPnniMIB", "mscAtmIfVptPnniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmPnniMIB", "mscAtmIfVptPnniRccIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmPnniMIB", "mscAtmIfVptPnniRccVcdIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmPnniMIB", "mscAtmIfVptPnniRccVcdTdpIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfVptPnniRccVcdTdpEntry.setStatus("mandatory")


class _MscAtmIfVptPnniRccVcdTdpIndex_Type(Integer32):
    """Custom type mscAtmIfVptPnniRccVcdTdpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_MscAtmIfVptPnniRccVcdTdpIndex_Type.__name__ = "Integer32"
_MscAtmIfVptPnniRccVcdTdpIndex_Object = MibTableColumn
mscAtmIfVptPnniRccVcdTdpIndex = _MscAtmIfVptPnniRccVcdTdpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 3, 2, 387, 1, 1),
    _MscAtmIfVptPnniRccVcdTdpIndex_Type()
)
mscAtmIfVptPnniRccVcdTdpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAtmIfVptPnniRccVcdTdpIndex.setStatus("mandatory")


class _MscAtmIfVptPnniRccVcdTdpValue_Type(Unsigned32):
    """Custom type mscAtmIfVptPnniRccVcdTdpValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MscAtmIfVptPnniRccVcdTdpValue_Type.__name__ = "Unsigned32"
_MscAtmIfVptPnniRccVcdTdpValue_Object = MibTableColumn
mscAtmIfVptPnniRccVcdTdpValue = _MscAtmIfVptPnniRccVcdTdpValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 3, 2, 387, 1, 2),
    _MscAtmIfVptPnniRccVcdTdpValue_Type()
)
mscAtmIfVptPnniRccVcdTdpValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVptPnniRccVcdTdpValue.setStatus("mandatory")
_MscAtmIfVptPnniRccProvTable_Object = MibTable
mscAtmIfVptPnniRccProvTable = _MscAtmIfVptPnniRccProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 3, 10)
)
if mibBuilder.loadTexts:
    mscAtmIfVptPnniRccProvTable.setStatus("mandatory")
_MscAtmIfVptPnniRccProvEntry_Object = MibTableRow
mscAtmIfVptPnniRccProvEntry = _MscAtmIfVptPnniRccProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 3, 10, 1)
)
mscAtmIfVptPnniRccProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVptIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmPnniMIB", "mscAtmIfVptPnniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmPnniMIB", "mscAtmIfVptPnniRccIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfVptPnniRccProvEntry.setStatus("mandatory")


class _MscAtmIfVptPnniRccVci_Type(Unsigned32):
    """Custom type mscAtmIfVptPnniRccVci based on Unsigned32"""
    defaultValue = 18

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscAtmIfVptPnniRccVci_Type.__name__ = "Unsigned32"
_MscAtmIfVptPnniRccVci_Object = MibTableColumn
mscAtmIfVptPnniRccVci = _MscAtmIfVptPnniRccVci_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 3, 10, 1, 1),
    _MscAtmIfVptPnniRccVci_Type()
)
mscAtmIfVptPnniRccVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVptPnniRccVci.setStatus("mandatory")
_MscAtmIfVptPnniRccHlParmsTable_Object = MibTable
mscAtmIfVptPnniRccHlParmsTable = _MscAtmIfVptPnniRccHlParmsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 3, 11)
)
if mibBuilder.loadTexts:
    mscAtmIfVptPnniRccHlParmsTable.setStatus("mandatory")
_MscAtmIfVptPnniRccHlParmsEntry_Object = MibTableRow
mscAtmIfVptPnniRccHlParmsEntry = _MscAtmIfVptPnniRccHlParmsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 3, 11, 1)
)
mscAtmIfVptPnniRccHlParmsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVptIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmPnniMIB", "mscAtmIfVptPnniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmPnniMIB", "mscAtmIfVptPnniRccIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfVptPnniRccHlParmsEntry.setStatus("mandatory")


class _MscAtmIfVptPnniRccHelloHoldDown_Type(FixedPoint1):
    """Custom type mscAtmIfVptPnniRccHelloHoldDown based on FixedPoint1"""
    defaultValue = 0

    subtypeSpec = FixedPoint1.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 655350),
    )


_MscAtmIfVptPnniRccHelloHoldDown_Type.__name__ = "FixedPoint1"
_MscAtmIfVptPnniRccHelloHoldDown_Object = MibTableColumn
mscAtmIfVptPnniRccHelloHoldDown = _MscAtmIfVptPnniRccHelloHoldDown_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 3, 11, 1, 1),
    _MscAtmIfVptPnniRccHelloHoldDown_Type()
)
mscAtmIfVptPnniRccHelloHoldDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVptPnniRccHelloHoldDown.setStatus("mandatory")


class _MscAtmIfVptPnniRccHelloInterval_Type(Unsigned32):
    """Custom type mscAtmIfVptPnniRccHelloInterval based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscAtmIfVptPnniRccHelloInterval_Type.__name__ = "Unsigned32"
_MscAtmIfVptPnniRccHelloInterval_Object = MibTableColumn
mscAtmIfVptPnniRccHelloInterval = _MscAtmIfVptPnniRccHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 3, 11, 1, 2),
    _MscAtmIfVptPnniRccHelloInterval_Type()
)
mscAtmIfVptPnniRccHelloInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVptPnniRccHelloInterval.setStatus("mandatory")


class _MscAtmIfVptPnniRccHelloInactivityFactor_Type(Unsigned32):
    """Custom type mscAtmIfVptPnniRccHelloInactivityFactor based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscAtmIfVptPnniRccHelloInactivityFactor_Type.__name__ = "Unsigned32"
_MscAtmIfVptPnniRccHelloInactivityFactor_Object = MibTableColumn
mscAtmIfVptPnniRccHelloInactivityFactor = _MscAtmIfVptPnniRccHelloInactivityFactor_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 3, 11, 1, 3),
    _MscAtmIfVptPnniRccHelloInactivityFactor_Type()
)
mscAtmIfVptPnniRccHelloInactivityFactor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVptPnniRccHelloInactivityFactor.setStatus("mandatory")
_MscAtmIfVptPnniRccStateTable_Object = MibTable
mscAtmIfVptPnniRccStateTable = _MscAtmIfVptPnniRccStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 3, 12)
)
if mibBuilder.loadTexts:
    mscAtmIfVptPnniRccStateTable.setStatus("mandatory")
_MscAtmIfVptPnniRccStateEntry_Object = MibTableRow
mscAtmIfVptPnniRccStateEntry = _MscAtmIfVptPnniRccStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 3, 12, 1)
)
mscAtmIfVptPnniRccStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVptIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmPnniMIB", "mscAtmIfVptPnniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmPnniMIB", "mscAtmIfVptPnniRccIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfVptPnniRccStateEntry.setStatus("mandatory")


class _MscAtmIfVptPnniRccAdminState_Type(Integer32):
    """Custom type mscAtmIfVptPnniRccAdminState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("locked", 0),
          ("shuttingDown", 2),
          ("unlocked", 1))
    )


_MscAtmIfVptPnniRccAdminState_Type.__name__ = "Integer32"
_MscAtmIfVptPnniRccAdminState_Object = MibTableColumn
mscAtmIfVptPnniRccAdminState = _MscAtmIfVptPnniRccAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 3, 12, 1, 1),
    _MscAtmIfVptPnniRccAdminState_Type()
)
mscAtmIfVptPnniRccAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptPnniRccAdminState.setStatus("mandatory")


class _MscAtmIfVptPnniRccOperationalState_Type(Integer32):
    """Custom type mscAtmIfVptPnniRccOperationalState based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_MscAtmIfVptPnniRccOperationalState_Type.__name__ = "Integer32"
_MscAtmIfVptPnniRccOperationalState_Object = MibTableColumn
mscAtmIfVptPnniRccOperationalState = _MscAtmIfVptPnniRccOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 3, 12, 1, 2),
    _MscAtmIfVptPnniRccOperationalState_Type()
)
mscAtmIfVptPnniRccOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptPnniRccOperationalState.setStatus("mandatory")


class _MscAtmIfVptPnniRccUsageState_Type(Integer32):
    """Custom type mscAtmIfVptPnniRccUsageState based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("busy", 2),
          ("idle", 0))
    )


_MscAtmIfVptPnniRccUsageState_Type.__name__ = "Integer32"
_MscAtmIfVptPnniRccUsageState_Object = MibTableColumn
mscAtmIfVptPnniRccUsageState = _MscAtmIfVptPnniRccUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 3, 12, 1, 3),
    _MscAtmIfVptPnniRccUsageState_Type()
)
mscAtmIfVptPnniRccUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptPnniRccUsageState.setStatus("mandatory")
_MscAtmIfVptPnniRccOperTable_Object = MibTable
mscAtmIfVptPnniRccOperTable = _MscAtmIfVptPnniRccOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 3, 13)
)
if mibBuilder.loadTexts:
    mscAtmIfVptPnniRccOperTable.setStatus("mandatory")
_MscAtmIfVptPnniRccOperEntry_Object = MibTableRow
mscAtmIfVptPnniRccOperEntry = _MscAtmIfVptPnniRccOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 3, 13, 1)
)
mscAtmIfVptPnniRccOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVptIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmPnniMIB", "mscAtmIfVptPnniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmPnniMIB", "mscAtmIfVptPnniRccIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfVptPnniRccOperEntry.setStatus("mandatory")


class _MscAtmIfVptPnniRccType_Type(Integer32):
    """Custom type mscAtmIfVptPnniRccType based on Integer32"""
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
        *(("horizontalLinkToLGN", 3),
          ("lowestLevelHorizLink", 1),
          ("lowestLevelOutsideLink", 2),
          ("unknown", 0),
          ("uplink", 4))
    )


_MscAtmIfVptPnniRccType_Type.__name__ = "Integer32"
_MscAtmIfVptPnniRccType_Object = MibTableColumn
mscAtmIfVptPnniRccType = _MscAtmIfVptPnniRccType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 3, 13, 1, 1),
    _MscAtmIfVptPnniRccType_Type()
)
mscAtmIfVptPnniRccType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptPnniRccType.setStatus("mandatory")


class _MscAtmIfVptPnniRccNegotiatedVersion_Type(Integer32):
    """Custom type mscAtmIfVptPnniRccNegotiatedVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("unsupported", 0),
          ("version1point0", 1))
    )


_MscAtmIfVptPnniRccNegotiatedVersion_Type.__name__ = "Integer32"
_MscAtmIfVptPnniRccNegotiatedVersion_Object = MibTableColumn
mscAtmIfVptPnniRccNegotiatedVersion = _MscAtmIfVptPnniRccNegotiatedVersion_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 3, 13, 1, 2),
    _MscAtmIfVptPnniRccNegotiatedVersion_Type()
)
mscAtmIfVptPnniRccNegotiatedVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptPnniRccNegotiatedVersion.setStatus("mandatory")


class _MscAtmIfVptPnniRccHelloState_Type(Integer32):
    """Custom type mscAtmIfVptPnniRccHelloState based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("attempt", 2),
          ("commonOutside", 7),
          ("down", 1),
          ("notApplicable", 0),
          ("oneWayInside", 3),
          ("oneWayOutside", 5),
          ("twoWayInside", 4),
          ("twoWayOutside", 6))
    )


_MscAtmIfVptPnniRccHelloState_Type.__name__ = "Integer32"
_MscAtmIfVptPnniRccHelloState_Object = MibTableColumn
mscAtmIfVptPnniRccHelloState = _MscAtmIfVptPnniRccHelloState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 3, 13, 1, 3),
    _MscAtmIfVptPnniRccHelloState_Type()
)
mscAtmIfVptPnniRccHelloState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptPnniRccHelloState.setStatus("mandatory")


class _MscAtmIfVptPnniRccRemoteNodeId_Type(HexString):
    """Custom type mscAtmIfVptPnniRccRemoteNodeId based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(22, 22),
    )


_MscAtmIfVptPnniRccRemoteNodeId_Type.__name__ = "HexString"
_MscAtmIfVptPnniRccRemoteNodeId_Object = MibTableColumn
mscAtmIfVptPnniRccRemoteNodeId = _MscAtmIfVptPnniRccRemoteNodeId_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 3, 13, 1, 4),
    _MscAtmIfVptPnniRccRemoteNodeId_Type()
)
mscAtmIfVptPnniRccRemoteNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptPnniRccRemoteNodeId.setStatus("mandatory")


class _MscAtmIfVptPnniRccRemotePortId_Type(Unsigned32):
    """Custom type mscAtmIfVptPnniRccRemotePortId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscAtmIfVptPnniRccRemotePortId_Type.__name__ = "Unsigned32"
_MscAtmIfVptPnniRccRemotePortId_Object = MibTableColumn
mscAtmIfVptPnniRccRemotePortId = _MscAtmIfVptPnniRccRemotePortId_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 3, 13, 1, 5),
    _MscAtmIfVptPnniRccRemotePortId_Type()
)
mscAtmIfVptPnniRccRemotePortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptPnniRccRemotePortId.setStatus("mandatory")
_MscAtmIfVptPnniRccStatsTable_Object = MibTable
mscAtmIfVptPnniRccStatsTable = _MscAtmIfVptPnniRccStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 3, 14)
)
if mibBuilder.loadTexts:
    mscAtmIfVptPnniRccStatsTable.setStatus("mandatory")
_MscAtmIfVptPnniRccStatsEntry_Object = MibTableRow
mscAtmIfVptPnniRccStatsEntry = _MscAtmIfVptPnniRccStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 3, 14, 1)
)
mscAtmIfVptPnniRccStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVptIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmPnniMIB", "mscAtmIfVptPnniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmPnniMIB", "mscAtmIfVptPnniRccIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfVptPnniRccStatsEntry.setStatus("mandatory")
_MscAtmIfVptPnniRccHelloPacketsRx_Type = Counter32
_MscAtmIfVptPnniRccHelloPacketsRx_Object = MibTableColumn
mscAtmIfVptPnniRccHelloPacketsRx = _MscAtmIfVptPnniRccHelloPacketsRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 3, 14, 1, 1),
    _MscAtmIfVptPnniRccHelloPacketsRx_Type()
)
mscAtmIfVptPnniRccHelloPacketsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptPnniRccHelloPacketsRx.setStatus("mandatory")
_MscAtmIfVptPnniRccHelloPacketsTx_Type = Counter32
_MscAtmIfVptPnniRccHelloPacketsTx_Object = MibTableColumn
mscAtmIfVptPnniRccHelloPacketsTx = _MscAtmIfVptPnniRccHelloPacketsTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 3, 14, 1, 2),
    _MscAtmIfVptPnniRccHelloPacketsTx_Type()
)
mscAtmIfVptPnniRccHelloPacketsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptPnniRccHelloPacketsTx.setStatus("mandatory")
_MscAtmIfVptPnniRccMismatchedHelloPacketsRx_Type = Counter32
_MscAtmIfVptPnniRccMismatchedHelloPacketsRx_Object = MibTableColumn
mscAtmIfVptPnniRccMismatchedHelloPacketsRx = _MscAtmIfVptPnniRccMismatchedHelloPacketsRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 3, 14, 1, 3),
    _MscAtmIfVptPnniRccMismatchedHelloPacketsRx_Type()
)
mscAtmIfVptPnniRccMismatchedHelloPacketsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptPnniRccMismatchedHelloPacketsRx.setStatus("mandatory")
_MscAtmIfVptPnniRccBadHelloPacketsRx_Type = Counter32
_MscAtmIfVptPnniRccBadHelloPacketsRx_Object = MibTableColumn
mscAtmIfVptPnniRccBadHelloPacketsRx = _MscAtmIfVptPnniRccBadHelloPacketsRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 3, 14, 1, 4),
    _MscAtmIfVptPnniRccBadHelloPacketsRx_Type()
)
mscAtmIfVptPnniRccBadHelloPacketsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptPnniRccBadHelloPacketsRx.setStatus("mandatory")
_MscAtmIfVptPnniAddr_ObjectIdentity = ObjectIdentity
mscAtmIfVptPnniAddr = _MscAtmIfVptPnniAddr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 4)
)
_MscAtmIfVptPnniAddrRowStatusTable_Object = MibTable
mscAtmIfVptPnniAddrRowStatusTable = _MscAtmIfVptPnniAddrRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 4, 1)
)
if mibBuilder.loadTexts:
    mscAtmIfVptPnniAddrRowStatusTable.setStatus("mandatory")
_MscAtmIfVptPnniAddrRowStatusEntry_Object = MibTableRow
mscAtmIfVptPnniAddrRowStatusEntry = _MscAtmIfVptPnniAddrRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 4, 1, 1)
)
mscAtmIfVptPnniAddrRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVptIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmPnniMIB", "mscAtmIfVptPnniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmPnniMIB", "mscAtmIfVptPnniAddrAddressIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmPnniMIB", "mscAtmIfVptPnniAddrAddressTypeIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfVptPnniAddrRowStatusEntry.setStatus("mandatory")
_MscAtmIfVptPnniAddrRowStatus_Type = RowStatus
_MscAtmIfVptPnniAddrRowStatus_Object = MibTableColumn
mscAtmIfVptPnniAddrRowStatus = _MscAtmIfVptPnniAddrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 4, 1, 1, 1),
    _MscAtmIfVptPnniAddrRowStatus_Type()
)
mscAtmIfVptPnniAddrRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVptPnniAddrRowStatus.setStatus("mandatory")
_MscAtmIfVptPnniAddrComponentName_Type = DisplayString
_MscAtmIfVptPnniAddrComponentName_Object = MibTableColumn
mscAtmIfVptPnniAddrComponentName = _MscAtmIfVptPnniAddrComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 4, 1, 1, 2),
    _MscAtmIfVptPnniAddrComponentName_Type()
)
mscAtmIfVptPnniAddrComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptPnniAddrComponentName.setStatus("mandatory")
_MscAtmIfVptPnniAddrStorageType_Type = StorageType
_MscAtmIfVptPnniAddrStorageType_Object = MibTableColumn
mscAtmIfVptPnniAddrStorageType = _MscAtmIfVptPnniAddrStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 4, 1, 1, 4),
    _MscAtmIfVptPnniAddrStorageType_Type()
)
mscAtmIfVptPnniAddrStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptPnniAddrStorageType.setStatus("mandatory")


class _MscAtmIfVptPnniAddrAddressIndex_Type(AsciiStringIndex):
    """Custom type mscAtmIfVptPnniAddrAddressIndex based on AsciiStringIndex"""
    subtypeSpec = AsciiStringIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_MscAtmIfVptPnniAddrAddressIndex_Type.__name__ = "AsciiStringIndex"
_MscAtmIfVptPnniAddrAddressIndex_Object = MibTableColumn
mscAtmIfVptPnniAddrAddressIndex = _MscAtmIfVptPnniAddrAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 4, 1, 1, 10),
    _MscAtmIfVptPnniAddrAddressIndex_Type()
)
mscAtmIfVptPnniAddrAddressIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAtmIfVptPnniAddrAddressIndex.setStatus("mandatory")


class _MscAtmIfVptPnniAddrAddressTypeIndex_Type(Integer32):
    """Custom type mscAtmIfVptPnniAddrAddressTypeIndex based on Integer32"""
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


_MscAtmIfVptPnniAddrAddressTypeIndex_Type.__name__ = "Integer32"
_MscAtmIfVptPnniAddrAddressTypeIndex_Object = MibTableColumn
mscAtmIfVptPnniAddrAddressTypeIndex = _MscAtmIfVptPnniAddrAddressTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 4, 1, 1, 11),
    _MscAtmIfVptPnniAddrAddressTypeIndex_Type()
)
mscAtmIfVptPnniAddrAddressTypeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAtmIfVptPnniAddrAddressTypeIndex.setStatus("mandatory")
_MscAtmIfVptPnniAddrTermSP_ObjectIdentity = ObjectIdentity
mscAtmIfVptPnniAddrTermSP = _MscAtmIfVptPnniAddrTermSP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 4, 2)
)
_MscAtmIfVptPnniAddrTermSPRowStatusTable_Object = MibTable
mscAtmIfVptPnniAddrTermSPRowStatusTable = _MscAtmIfVptPnniAddrTermSPRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 4, 2, 1)
)
if mibBuilder.loadTexts:
    mscAtmIfVptPnniAddrTermSPRowStatusTable.setStatus("mandatory")
_MscAtmIfVptPnniAddrTermSPRowStatusEntry_Object = MibTableRow
mscAtmIfVptPnniAddrTermSPRowStatusEntry = _MscAtmIfVptPnniAddrTermSPRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 4, 2, 1, 1)
)
mscAtmIfVptPnniAddrTermSPRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVptIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmPnniMIB", "mscAtmIfVptPnniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmPnniMIB", "mscAtmIfVptPnniAddrAddressIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmPnniMIB", "mscAtmIfVptPnniAddrAddressTypeIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmPnniMIB", "mscAtmIfVptPnniAddrTermSPIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfVptPnniAddrTermSPRowStatusEntry.setStatus("mandatory")
_MscAtmIfVptPnniAddrTermSPRowStatus_Type = RowStatus
_MscAtmIfVptPnniAddrTermSPRowStatus_Object = MibTableColumn
mscAtmIfVptPnniAddrTermSPRowStatus = _MscAtmIfVptPnniAddrTermSPRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 4, 2, 1, 1, 1),
    _MscAtmIfVptPnniAddrTermSPRowStatus_Type()
)
mscAtmIfVptPnniAddrTermSPRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVptPnniAddrTermSPRowStatus.setStatus("mandatory")
_MscAtmIfVptPnniAddrTermSPComponentName_Type = DisplayString
_MscAtmIfVptPnniAddrTermSPComponentName_Object = MibTableColumn
mscAtmIfVptPnniAddrTermSPComponentName = _MscAtmIfVptPnniAddrTermSPComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 4, 2, 1, 1, 2),
    _MscAtmIfVptPnniAddrTermSPComponentName_Type()
)
mscAtmIfVptPnniAddrTermSPComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptPnniAddrTermSPComponentName.setStatus("mandatory")
_MscAtmIfVptPnniAddrTermSPStorageType_Type = StorageType
_MscAtmIfVptPnniAddrTermSPStorageType_Object = MibTableColumn
mscAtmIfVptPnniAddrTermSPStorageType = _MscAtmIfVptPnniAddrTermSPStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 4, 2, 1, 1, 4),
    _MscAtmIfVptPnniAddrTermSPStorageType_Type()
)
mscAtmIfVptPnniAddrTermSPStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptPnniAddrTermSPStorageType.setStatus("mandatory")
_MscAtmIfVptPnniAddrTermSPIndex_Type = NonReplicated
_MscAtmIfVptPnniAddrTermSPIndex_Object = MibTableColumn
mscAtmIfVptPnniAddrTermSPIndex = _MscAtmIfVptPnniAddrTermSPIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 4, 2, 1, 1, 10),
    _MscAtmIfVptPnniAddrTermSPIndex_Type()
)
mscAtmIfVptPnniAddrTermSPIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAtmIfVptPnniAddrTermSPIndex.setStatus("mandatory")
_MscAtmIfVptPnniAddrPnniInfo_ObjectIdentity = ObjectIdentity
mscAtmIfVptPnniAddrPnniInfo = _MscAtmIfVptPnniAddrPnniInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 4, 3)
)
_MscAtmIfVptPnniAddrPnniInfoRowStatusTable_Object = MibTable
mscAtmIfVptPnniAddrPnniInfoRowStatusTable = _MscAtmIfVptPnniAddrPnniInfoRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 4, 3, 1)
)
if mibBuilder.loadTexts:
    mscAtmIfVptPnniAddrPnniInfoRowStatusTable.setStatus("mandatory")
_MscAtmIfVptPnniAddrPnniInfoRowStatusEntry_Object = MibTableRow
mscAtmIfVptPnniAddrPnniInfoRowStatusEntry = _MscAtmIfVptPnniAddrPnniInfoRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 4, 3, 1, 1)
)
mscAtmIfVptPnniAddrPnniInfoRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVptIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmPnniMIB", "mscAtmIfVptPnniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmPnniMIB", "mscAtmIfVptPnniAddrAddressIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmPnniMIB", "mscAtmIfVptPnniAddrAddressTypeIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmPnniMIB", "mscAtmIfVptPnniAddrPnniInfoIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfVptPnniAddrPnniInfoRowStatusEntry.setStatus("mandatory")
_MscAtmIfVptPnniAddrPnniInfoRowStatus_Type = RowStatus
_MscAtmIfVptPnniAddrPnniInfoRowStatus_Object = MibTableColumn
mscAtmIfVptPnniAddrPnniInfoRowStatus = _MscAtmIfVptPnniAddrPnniInfoRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 4, 3, 1, 1, 1),
    _MscAtmIfVptPnniAddrPnniInfoRowStatus_Type()
)
mscAtmIfVptPnniAddrPnniInfoRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVptPnniAddrPnniInfoRowStatus.setStatus("mandatory")
_MscAtmIfVptPnniAddrPnniInfoComponentName_Type = DisplayString
_MscAtmIfVptPnniAddrPnniInfoComponentName_Object = MibTableColumn
mscAtmIfVptPnniAddrPnniInfoComponentName = _MscAtmIfVptPnniAddrPnniInfoComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 4, 3, 1, 1, 2),
    _MscAtmIfVptPnniAddrPnniInfoComponentName_Type()
)
mscAtmIfVptPnniAddrPnniInfoComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptPnniAddrPnniInfoComponentName.setStatus("mandatory")
_MscAtmIfVptPnniAddrPnniInfoStorageType_Type = StorageType
_MscAtmIfVptPnniAddrPnniInfoStorageType_Object = MibTableColumn
mscAtmIfVptPnniAddrPnniInfoStorageType = _MscAtmIfVptPnniAddrPnniInfoStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 4, 3, 1, 1, 4),
    _MscAtmIfVptPnniAddrPnniInfoStorageType_Type()
)
mscAtmIfVptPnniAddrPnniInfoStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptPnniAddrPnniInfoStorageType.setStatus("mandatory")
_MscAtmIfVptPnniAddrPnniInfoIndex_Type = NonReplicated
_MscAtmIfVptPnniAddrPnniInfoIndex_Object = MibTableColumn
mscAtmIfVptPnniAddrPnniInfoIndex = _MscAtmIfVptPnniAddrPnniInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 4, 3, 1, 1, 10),
    _MscAtmIfVptPnniAddrPnniInfoIndex_Type()
)
mscAtmIfVptPnniAddrPnniInfoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAtmIfVptPnniAddrPnniInfoIndex.setStatus("mandatory")
_MscAtmIfVptPnniAddrPnniInfoProvTable_Object = MibTable
mscAtmIfVptPnniAddrPnniInfoProvTable = _MscAtmIfVptPnniAddrPnniInfoProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 4, 3, 10)
)
if mibBuilder.loadTexts:
    mscAtmIfVptPnniAddrPnniInfoProvTable.setStatus("mandatory")
_MscAtmIfVptPnniAddrPnniInfoProvEntry_Object = MibTableRow
mscAtmIfVptPnniAddrPnniInfoProvEntry = _MscAtmIfVptPnniAddrPnniInfoProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 4, 3, 10, 1)
)
mscAtmIfVptPnniAddrPnniInfoProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVptIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmPnniMIB", "mscAtmIfVptPnniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmPnniMIB", "mscAtmIfVptPnniAddrAddressIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmPnniMIB", "mscAtmIfVptPnniAddrAddressTypeIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmPnniMIB", "mscAtmIfVptPnniAddrPnniInfoIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfVptPnniAddrPnniInfoProvEntry.setStatus("mandatory")


class _MscAtmIfVptPnniAddrPnniInfoScope_Type(Integer32):
    """Custom type mscAtmIfVptPnniAddrPnniInfoScope based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 104),
    )


_MscAtmIfVptPnniAddrPnniInfoScope_Type.__name__ = "Integer32"
_MscAtmIfVptPnniAddrPnniInfoScope_Object = MibTableColumn
mscAtmIfVptPnniAddrPnniInfoScope = _MscAtmIfVptPnniAddrPnniInfoScope_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 4, 3, 10, 1, 1),
    _MscAtmIfVptPnniAddrPnniInfoScope_Type()
)
mscAtmIfVptPnniAddrPnniInfoScope.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVptPnniAddrPnniInfoScope.setStatus("mandatory")


class _MscAtmIfVptPnniAddrPnniInfoReachability_Type(Integer32):
    """Custom type mscAtmIfVptPnniAddrPnniInfoReachability based on Integer32"""
    defaultValue = 0

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


_MscAtmIfVptPnniAddrPnniInfoReachability_Type.__name__ = "Integer32"
_MscAtmIfVptPnniAddrPnniInfoReachability_Object = MibTableColumn
mscAtmIfVptPnniAddrPnniInfoReachability = _MscAtmIfVptPnniAddrPnniInfoReachability_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 4, 3, 10, 1, 2),
    _MscAtmIfVptPnniAddrPnniInfoReachability_Type()
)
mscAtmIfVptPnniAddrPnniInfoReachability.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVptPnniAddrPnniInfoReachability.setStatus("mandatory")
_MscAtmIfVptPnniAddrOperTable_Object = MibTable
mscAtmIfVptPnniAddrOperTable = _MscAtmIfVptPnniAddrOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 4, 10)
)
if mibBuilder.loadTexts:
    mscAtmIfVptPnniAddrOperTable.setStatus("mandatory")
_MscAtmIfVptPnniAddrOperEntry_Object = MibTableRow
mscAtmIfVptPnniAddrOperEntry = _MscAtmIfVptPnniAddrOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 4, 10, 1)
)
mscAtmIfVptPnniAddrOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVptIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmPnniMIB", "mscAtmIfVptPnniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmPnniMIB", "mscAtmIfVptPnniAddrAddressIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmPnniMIB", "mscAtmIfVptPnniAddrAddressTypeIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfVptPnniAddrOperEntry.setStatus("mandatory")


class _MscAtmIfVptPnniAddrScope_Type(Integer32):
    """Custom type mscAtmIfVptPnniAddrScope based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 104),
    )


_MscAtmIfVptPnniAddrScope_Type.__name__ = "Integer32"
_MscAtmIfVptPnniAddrScope_Object = MibTableColumn
mscAtmIfVptPnniAddrScope = _MscAtmIfVptPnniAddrScope_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 4, 10, 1, 1),
    _MscAtmIfVptPnniAddrScope_Type()
)
mscAtmIfVptPnniAddrScope.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptPnniAddrScope.setStatus("mandatory")


class _MscAtmIfVptPnniAddrReachability_Type(Integer32):
    """Custom type mscAtmIfVptPnniAddrReachability based on Integer32"""
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


_MscAtmIfVptPnniAddrReachability_Type.__name__ = "Integer32"
_MscAtmIfVptPnniAddrReachability_Object = MibTableColumn
mscAtmIfVptPnniAddrReachability = _MscAtmIfVptPnniAddrReachability_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 4, 10, 1, 2),
    _MscAtmIfVptPnniAddrReachability_Type()
)
mscAtmIfVptPnniAddrReachability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptPnniAddrReachability.setStatus("mandatory")
_MscAtmIfVptPnniProvTable_Object = MibTable
mscAtmIfVptPnniProvTable = _MscAtmIfVptPnniProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 10)
)
if mibBuilder.loadTexts:
    mscAtmIfVptPnniProvTable.setStatus("mandatory")
_MscAtmIfVptPnniProvEntry_Object = MibTableRow
mscAtmIfVptPnniProvEntry = _MscAtmIfVptPnniProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 10, 1)
)
mscAtmIfVptPnniProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVptIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmPnniMIB", "mscAtmIfVptPnniIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfVptPnniProvEntry.setStatus("mandatory")


class _MscAtmIfVptPnniSoftPvcRetryPeriod_Type(Unsigned32):
    """Custom type mscAtmIfVptPnniSoftPvcRetryPeriod based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 999999),
    )


_MscAtmIfVptPnniSoftPvcRetryPeriod_Type.__name__ = "Unsigned32"
_MscAtmIfVptPnniSoftPvcRetryPeriod_Object = MibTableColumn
mscAtmIfVptPnniSoftPvcRetryPeriod = _MscAtmIfVptPnniSoftPvcRetryPeriod_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 10, 1, 1),
    _MscAtmIfVptPnniSoftPvcRetryPeriod_Type()
)
mscAtmIfVptPnniSoftPvcRetryPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVptPnniSoftPvcRetryPeriod.setStatus("obsolete")


class _MscAtmIfVptPnniSoftPvpAndPvcRetryPeriod_Type(Unsigned32):
    """Custom type mscAtmIfVptPnniSoftPvpAndPvcRetryPeriod based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 999999),
    )


_MscAtmIfVptPnniSoftPvpAndPvcRetryPeriod_Type.__name__ = "Unsigned32"
_MscAtmIfVptPnniSoftPvpAndPvcRetryPeriod_Object = MibTableColumn
mscAtmIfVptPnniSoftPvpAndPvcRetryPeriod = _MscAtmIfVptPnniSoftPvpAndPvcRetryPeriod_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 10, 1, 2),
    _MscAtmIfVptPnniSoftPvpAndPvcRetryPeriod_Type()
)
mscAtmIfVptPnniSoftPvpAndPvcRetryPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVptPnniSoftPvpAndPvcRetryPeriod.setStatus("mandatory")


class _MscAtmIfVptPnniSoftPvpAndPvcHoldOffTime_Type(Unsigned32):
    """Custom type mscAtmIfVptPnniSoftPvpAndPvcHoldOffTime based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(50, 20000),
    )


_MscAtmIfVptPnniSoftPvpAndPvcHoldOffTime_Type.__name__ = "Unsigned32"
_MscAtmIfVptPnniSoftPvpAndPvcHoldOffTime_Object = MibTableColumn
mscAtmIfVptPnniSoftPvpAndPvcHoldOffTime = _MscAtmIfVptPnniSoftPvpAndPvcHoldOffTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 10, 1, 5),
    _MscAtmIfVptPnniSoftPvpAndPvcHoldOffTime_Type()
)
mscAtmIfVptPnniSoftPvpAndPvcHoldOffTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVptPnniSoftPvpAndPvcHoldOffTime.setStatus("mandatory")
_MscAtmIfVptPnniAdminWeightsTable_Object = MibTable
mscAtmIfVptPnniAdminWeightsTable = _MscAtmIfVptPnniAdminWeightsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 11)
)
if mibBuilder.loadTexts:
    mscAtmIfVptPnniAdminWeightsTable.setStatus("mandatory")
_MscAtmIfVptPnniAdminWeightsEntry_Object = MibTableRow
mscAtmIfVptPnniAdminWeightsEntry = _MscAtmIfVptPnniAdminWeightsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 11, 1)
)
mscAtmIfVptPnniAdminWeightsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVptIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmPnniMIB", "mscAtmIfVptPnniIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfVptPnniAdminWeightsEntry.setStatus("mandatory")


class _MscAtmIfVptPnniCbrWeight_Type(Unsigned32):
    """Custom type mscAtmIfVptPnniCbrWeight based on Unsigned32"""
    defaultValue = 5040

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscAtmIfVptPnniCbrWeight_Type.__name__ = "Unsigned32"
_MscAtmIfVptPnniCbrWeight_Object = MibTableColumn
mscAtmIfVptPnniCbrWeight = _MscAtmIfVptPnniCbrWeight_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 11, 1, 1),
    _MscAtmIfVptPnniCbrWeight_Type()
)
mscAtmIfVptPnniCbrWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVptPnniCbrWeight.setStatus("mandatory")


class _MscAtmIfVptPnniRtVbrWeight_Type(Unsigned32):
    """Custom type mscAtmIfVptPnniRtVbrWeight based on Unsigned32"""
    defaultValue = 5040

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscAtmIfVptPnniRtVbrWeight_Type.__name__ = "Unsigned32"
_MscAtmIfVptPnniRtVbrWeight_Object = MibTableColumn
mscAtmIfVptPnniRtVbrWeight = _MscAtmIfVptPnniRtVbrWeight_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 11, 1, 2),
    _MscAtmIfVptPnniRtVbrWeight_Type()
)
mscAtmIfVptPnniRtVbrWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVptPnniRtVbrWeight.setStatus("mandatory")


class _MscAtmIfVptPnniNrtVbrWeight_Type(Unsigned32):
    """Custom type mscAtmIfVptPnniNrtVbrWeight based on Unsigned32"""
    defaultValue = 5040

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscAtmIfVptPnniNrtVbrWeight_Type.__name__ = "Unsigned32"
_MscAtmIfVptPnniNrtVbrWeight_Object = MibTableColumn
mscAtmIfVptPnniNrtVbrWeight = _MscAtmIfVptPnniNrtVbrWeight_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 11, 1, 3),
    _MscAtmIfVptPnniNrtVbrWeight_Type()
)
mscAtmIfVptPnniNrtVbrWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVptPnniNrtVbrWeight.setStatus("mandatory")


class _MscAtmIfVptPnniUbrWeight_Type(Unsigned32):
    """Custom type mscAtmIfVptPnniUbrWeight based on Unsigned32"""
    defaultValue = 5040

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscAtmIfVptPnniUbrWeight_Type.__name__ = "Unsigned32"
_MscAtmIfVptPnniUbrWeight_Object = MibTableColumn
mscAtmIfVptPnniUbrWeight = _MscAtmIfVptPnniUbrWeight_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 11, 1, 4),
    _MscAtmIfVptPnniUbrWeight_Type()
)
mscAtmIfVptPnniUbrWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVptPnniUbrWeight.setStatus("mandatory")
_MscAtmIfVptPnniAcctOptTable_Object = MibTable
mscAtmIfVptPnniAcctOptTable = _MscAtmIfVptPnniAcctOptTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 12)
)
if mibBuilder.loadTexts:
    mscAtmIfVptPnniAcctOptTable.setStatus("mandatory")
_MscAtmIfVptPnniAcctOptEntry_Object = MibTableRow
mscAtmIfVptPnniAcctOptEntry = _MscAtmIfVptPnniAcctOptEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 12, 1)
)
mscAtmIfVptPnniAcctOptEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVptIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmPnniMIB", "mscAtmIfVptPnniIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfVptPnniAcctOptEntry.setStatus("mandatory")


class _MscAtmIfVptPnniAccountCollection_Type(OctetString):
    """Custom type mscAtmIfVptPnniAccountCollection based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscAtmIfVptPnniAccountCollection_Type.__name__ = "OctetString"
_MscAtmIfVptPnniAccountCollection_Object = MibTableColumn
mscAtmIfVptPnniAccountCollection = _MscAtmIfVptPnniAccountCollection_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 12, 1, 1),
    _MscAtmIfVptPnniAccountCollection_Type()
)
mscAtmIfVptPnniAccountCollection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVptPnniAccountCollection.setStatus("mandatory")


class _MscAtmIfVptPnniAccountConnectionType_Type(Integer32):
    """Custom type mscAtmIfVptPnniAccountConnectionType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("intermediate", 1),
          ("origTerm", 0))
    )


_MscAtmIfVptPnniAccountConnectionType_Type.__name__ = "Integer32"
_MscAtmIfVptPnniAccountConnectionType_Object = MibTableColumn
mscAtmIfVptPnniAccountConnectionType = _MscAtmIfVptPnniAccountConnectionType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 12, 1, 2),
    _MscAtmIfVptPnniAccountConnectionType_Type()
)
mscAtmIfVptPnniAccountConnectionType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVptPnniAccountConnectionType.setStatus("mandatory")


class _MscAtmIfVptPnniAccountClass_Type(Unsigned32):
    """Custom type mscAtmIfVptPnniAccountClass based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscAtmIfVptPnniAccountClass_Type.__name__ = "Unsigned32"
_MscAtmIfVptPnniAccountClass_Object = MibTableColumn
mscAtmIfVptPnniAccountClass = _MscAtmIfVptPnniAccountClass_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 12, 1, 3),
    _MscAtmIfVptPnniAccountClass_Type()
)
mscAtmIfVptPnniAccountClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVptPnniAccountClass.setStatus("mandatory")


class _MscAtmIfVptPnniServiceExchange_Type(Unsigned32):
    """Custom type mscAtmIfVptPnniServiceExchange based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscAtmIfVptPnniServiceExchange_Type.__name__ = "Unsigned32"
_MscAtmIfVptPnniServiceExchange_Object = MibTableColumn
mscAtmIfVptPnniServiceExchange = _MscAtmIfVptPnniServiceExchange_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 12, 1, 4),
    _MscAtmIfVptPnniServiceExchange_Type()
)
mscAtmIfVptPnniServiceExchange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVptPnniServiceExchange.setStatus("mandatory")
_MscAtmIfVptPnniOperationalTable_Object = MibTable
mscAtmIfVptPnniOperationalTable = _MscAtmIfVptPnniOperationalTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 13)
)
if mibBuilder.loadTexts:
    mscAtmIfVptPnniOperationalTable.setStatus("mandatory")
_MscAtmIfVptPnniOperationalEntry_Object = MibTableRow
mscAtmIfVptPnniOperationalEntry = _MscAtmIfVptPnniOperationalEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 13, 1)
)
mscAtmIfVptPnniOperationalEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVptIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmPnniMIB", "mscAtmIfVptPnniIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfVptPnniOperationalEntry.setStatus("mandatory")


class _MscAtmIfVptPnniPortId_Type(Unsigned32):
    """Custom type mscAtmIfVptPnniPortId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscAtmIfVptPnniPortId_Type.__name__ = "Unsigned32"
_MscAtmIfVptPnniPortId_Object = MibTableColumn
mscAtmIfVptPnniPortId = _MscAtmIfVptPnniPortId_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 13, 1, 1),
    _MscAtmIfVptPnniPortId_Type()
)
mscAtmIfVptPnniPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptPnniPortId.setStatus("mandatory")
_MscAtmIfVptPnniVProvTable_Object = MibTable
mscAtmIfVptPnniVProvTable = _MscAtmIfVptPnniVProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 14)
)
if mibBuilder.loadTexts:
    mscAtmIfVptPnniVProvTable.setStatus("mandatory")
_MscAtmIfVptPnniVProvEntry_Object = MibTableRow
mscAtmIfVptPnniVProvEntry = _MscAtmIfVptPnniVProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 14, 1)
)
mscAtmIfVptPnniVProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVptIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmPnniMIB", "mscAtmIfVptPnniIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfVptPnniVProvEntry.setStatus("mandatory")


class _MscAtmIfVptPnniVpci_Type(Unsigned32):
    """Custom type mscAtmIfVptPnniVpci based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscAtmIfVptPnniVpci_Type.__name__ = "Unsigned32"
_MscAtmIfVptPnniVpci_Object = MibTableColumn
mscAtmIfVptPnniVpci = _MscAtmIfVptPnniVpci_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 7, 14, 1, 1),
    _MscAtmIfVptPnniVpci_Type()
)
mscAtmIfVptPnniVpci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVptPnniVpci.setStatus("mandatory")
_MscAtmIfPnni_ObjectIdentity = ObjectIdentity
mscAtmIfPnni = _MscAtmIfPnni_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96)
)
_MscAtmIfPnniRowStatusTable_Object = MibTable
mscAtmIfPnniRowStatusTable = _MscAtmIfPnniRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 1)
)
if mibBuilder.loadTexts:
    mscAtmIfPnniRowStatusTable.setStatus("mandatory")
_MscAtmIfPnniRowStatusEntry_Object = MibTableRow
mscAtmIfPnniRowStatusEntry = _MscAtmIfPnniRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 1, 1)
)
mscAtmIfPnniRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmPnniMIB", "mscAtmIfPnniIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfPnniRowStatusEntry.setStatus("mandatory")
_MscAtmIfPnniRowStatus_Type = RowStatus
_MscAtmIfPnniRowStatus_Object = MibTableColumn
mscAtmIfPnniRowStatus = _MscAtmIfPnniRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 1, 1, 1),
    _MscAtmIfPnniRowStatus_Type()
)
mscAtmIfPnniRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfPnniRowStatus.setStatus("mandatory")
_MscAtmIfPnniComponentName_Type = DisplayString
_MscAtmIfPnniComponentName_Object = MibTableColumn
mscAtmIfPnniComponentName = _MscAtmIfPnniComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 1, 1, 2),
    _MscAtmIfPnniComponentName_Type()
)
mscAtmIfPnniComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfPnniComponentName.setStatus("mandatory")
_MscAtmIfPnniStorageType_Type = StorageType
_MscAtmIfPnniStorageType_Object = MibTableColumn
mscAtmIfPnniStorageType = _MscAtmIfPnniStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 1, 1, 4),
    _MscAtmIfPnniStorageType_Type()
)
mscAtmIfPnniStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfPnniStorageType.setStatus("mandatory")
_MscAtmIfPnniIndex_Type = NonReplicated
_MscAtmIfPnniIndex_Object = MibTableColumn
mscAtmIfPnniIndex = _MscAtmIfPnniIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 1, 1, 10),
    _MscAtmIfPnniIndex_Type()
)
mscAtmIfPnniIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAtmIfPnniIndex.setStatus("mandatory")
_MscAtmIfPnniSig_ObjectIdentity = ObjectIdentity
mscAtmIfPnniSig = _MscAtmIfPnniSig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 2)
)
_MscAtmIfPnniSigRowStatusTable_Object = MibTable
mscAtmIfPnniSigRowStatusTable = _MscAtmIfPnniSigRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 2, 1)
)
if mibBuilder.loadTexts:
    mscAtmIfPnniSigRowStatusTable.setStatus("mandatory")
_MscAtmIfPnniSigRowStatusEntry_Object = MibTableRow
mscAtmIfPnniSigRowStatusEntry = _MscAtmIfPnniSigRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 2, 1, 1)
)
mscAtmIfPnniSigRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmPnniMIB", "mscAtmIfPnniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmPnniMIB", "mscAtmIfPnniSigIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfPnniSigRowStatusEntry.setStatus("mandatory")
_MscAtmIfPnniSigRowStatus_Type = RowStatus
_MscAtmIfPnniSigRowStatus_Object = MibTableColumn
mscAtmIfPnniSigRowStatus = _MscAtmIfPnniSigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 2, 1, 1, 1),
    _MscAtmIfPnniSigRowStatus_Type()
)
mscAtmIfPnniSigRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfPnniSigRowStatus.setStatus("mandatory")
_MscAtmIfPnniSigComponentName_Type = DisplayString
_MscAtmIfPnniSigComponentName_Object = MibTableColumn
mscAtmIfPnniSigComponentName = _MscAtmIfPnniSigComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 2, 1, 1, 2),
    _MscAtmIfPnniSigComponentName_Type()
)
mscAtmIfPnniSigComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfPnniSigComponentName.setStatus("mandatory")
_MscAtmIfPnniSigStorageType_Type = StorageType
_MscAtmIfPnniSigStorageType_Object = MibTableColumn
mscAtmIfPnniSigStorageType = _MscAtmIfPnniSigStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 2, 1, 1, 4),
    _MscAtmIfPnniSigStorageType_Type()
)
mscAtmIfPnniSigStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfPnniSigStorageType.setStatus("mandatory")
_MscAtmIfPnniSigIndex_Type = NonReplicated
_MscAtmIfPnniSigIndex_Object = MibTableColumn
mscAtmIfPnniSigIndex = _MscAtmIfPnniSigIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 2, 1, 1, 10),
    _MscAtmIfPnniSigIndex_Type()
)
mscAtmIfPnniSigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAtmIfPnniSigIndex.setStatus("mandatory")
_MscAtmIfPnniSigVcd_ObjectIdentity = ObjectIdentity
mscAtmIfPnniSigVcd = _MscAtmIfPnniSigVcd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 2, 2)
)
_MscAtmIfPnniSigVcdRowStatusTable_Object = MibTable
mscAtmIfPnniSigVcdRowStatusTable = _MscAtmIfPnniSigVcdRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 2, 2, 1)
)
if mibBuilder.loadTexts:
    mscAtmIfPnniSigVcdRowStatusTable.setStatus("mandatory")
_MscAtmIfPnniSigVcdRowStatusEntry_Object = MibTableRow
mscAtmIfPnniSigVcdRowStatusEntry = _MscAtmIfPnniSigVcdRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 2, 2, 1, 1)
)
mscAtmIfPnniSigVcdRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmPnniMIB", "mscAtmIfPnniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmPnniMIB", "mscAtmIfPnniSigIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmPnniMIB", "mscAtmIfPnniSigVcdIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfPnniSigVcdRowStatusEntry.setStatus("mandatory")
_MscAtmIfPnniSigVcdRowStatus_Type = RowStatus
_MscAtmIfPnniSigVcdRowStatus_Object = MibTableColumn
mscAtmIfPnniSigVcdRowStatus = _MscAtmIfPnniSigVcdRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 2, 2, 1, 1, 1),
    _MscAtmIfPnniSigVcdRowStatus_Type()
)
mscAtmIfPnniSigVcdRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfPnniSigVcdRowStatus.setStatus("mandatory")
_MscAtmIfPnniSigVcdComponentName_Type = DisplayString
_MscAtmIfPnniSigVcdComponentName_Object = MibTableColumn
mscAtmIfPnniSigVcdComponentName = _MscAtmIfPnniSigVcdComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 2, 2, 1, 1, 2),
    _MscAtmIfPnniSigVcdComponentName_Type()
)
mscAtmIfPnniSigVcdComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfPnniSigVcdComponentName.setStatus("mandatory")
_MscAtmIfPnniSigVcdStorageType_Type = StorageType
_MscAtmIfPnniSigVcdStorageType_Object = MibTableColumn
mscAtmIfPnniSigVcdStorageType = _MscAtmIfPnniSigVcdStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 2, 2, 1, 1, 4),
    _MscAtmIfPnniSigVcdStorageType_Type()
)
mscAtmIfPnniSigVcdStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfPnniSigVcdStorageType.setStatus("mandatory")
_MscAtmIfPnniSigVcdIndex_Type = NonReplicated
_MscAtmIfPnniSigVcdIndex_Object = MibTableColumn
mscAtmIfPnniSigVcdIndex = _MscAtmIfPnniSigVcdIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 2, 2, 1, 1, 10),
    _MscAtmIfPnniSigVcdIndex_Type()
)
mscAtmIfPnniSigVcdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAtmIfPnniSigVcdIndex.setStatus("mandatory")
_MscAtmIfPnniSigVcdProvTable_Object = MibTable
mscAtmIfPnniSigVcdProvTable = _MscAtmIfPnniSigVcdProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 2, 2, 10)
)
if mibBuilder.loadTexts:
    mscAtmIfPnniSigVcdProvTable.setStatus("mandatory")
_MscAtmIfPnniSigVcdProvEntry_Object = MibTableRow
mscAtmIfPnniSigVcdProvEntry = _MscAtmIfPnniSigVcdProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 2, 2, 10, 1)
)
mscAtmIfPnniSigVcdProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmPnniMIB", "mscAtmIfPnniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmPnniMIB", "mscAtmIfPnniSigIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmPnniMIB", "mscAtmIfPnniSigVcdIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfPnniSigVcdProvEntry.setStatus("mandatory")


class _MscAtmIfPnniSigVcdTrafficDescType_Type(Integer32):
    """Custom type mscAtmIfPnniSigVcdTrafficDescType based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("n3", 3),
          ("n6", 6),
          ("n7", 7),
          ("n8", 8))
    )


_MscAtmIfPnniSigVcdTrafficDescType_Type.__name__ = "Integer32"
_MscAtmIfPnniSigVcdTrafficDescType_Object = MibTableColumn
mscAtmIfPnniSigVcdTrafficDescType = _MscAtmIfPnniSigVcdTrafficDescType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 2, 2, 10, 1, 1),
    _MscAtmIfPnniSigVcdTrafficDescType_Type()
)
mscAtmIfPnniSigVcdTrafficDescType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfPnniSigVcdTrafficDescType.setStatus("mandatory")


class _MscAtmIfPnniSigVcdAtmServiceCategory_Type(Integer32):
    """Custom type mscAtmIfPnniSigVcdAtmServiceCategory based on Integer32"""
    defaultValue = 2

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
        *(("constantBitRate", 1),
          ("nrtVariableBitRate", 3),
          ("rtVariableBitRate", 2),
          ("unspecifiedBitRate", 0))
    )


_MscAtmIfPnniSigVcdAtmServiceCategory_Type.__name__ = "Integer32"
_MscAtmIfPnniSigVcdAtmServiceCategory_Object = MibTableColumn
mscAtmIfPnniSigVcdAtmServiceCategory = _MscAtmIfPnniSigVcdAtmServiceCategory_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 2, 2, 10, 1, 3),
    _MscAtmIfPnniSigVcdAtmServiceCategory_Type()
)
mscAtmIfPnniSigVcdAtmServiceCategory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfPnniSigVcdAtmServiceCategory.setStatus("mandatory")


class _MscAtmIfPnniSigVcdWeight_Type(Unsigned32):
    """Custom type mscAtmIfPnniSigVcdWeight based on Unsigned32"""
    defaultValue = 65535

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4095),
        ValueRangeConstraint(65535, 65535),
    )


_MscAtmIfPnniSigVcdWeight_Type.__name__ = "Unsigned32"
_MscAtmIfPnniSigVcdWeight_Object = MibTableColumn
mscAtmIfPnniSigVcdWeight = _MscAtmIfPnniSigVcdWeight_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 2, 2, 10, 1, 4),
    _MscAtmIfPnniSigVcdWeight_Type()
)
mscAtmIfPnniSigVcdWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfPnniSigVcdWeight.setStatus("mandatory")


class _MscAtmIfPnniSigVcdQosClass_Type(Integer32):
    """Custom type mscAtmIfPnniSigVcdQosClass based on Integer32"""
    defaultValue = 2

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


_MscAtmIfPnniSigVcdQosClass_Type.__name__ = "Integer32"
_MscAtmIfPnniSigVcdQosClass_Object = MibTableColumn
mscAtmIfPnniSigVcdQosClass = _MscAtmIfPnniSigVcdQosClass_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 2, 2, 10, 1, 21),
    _MscAtmIfPnniSigVcdQosClass_Type()
)
mscAtmIfPnniSigVcdQosClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfPnniSigVcdQosClass.setStatus("mandatory")


class _MscAtmIfPnniSigVcdTrafficShaping_Type(Integer32):
    """Custom type mscAtmIfPnniSigVcdTrafficShaping based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("sameAsCa", 2))
    )


_MscAtmIfPnniSigVcdTrafficShaping_Type.__name__ = "Integer32"
_MscAtmIfPnniSigVcdTrafficShaping_Object = MibTableColumn
mscAtmIfPnniSigVcdTrafficShaping = _MscAtmIfPnniSigVcdTrafficShaping_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 2, 2, 10, 1, 50),
    _MscAtmIfPnniSigVcdTrafficShaping_Type()
)
mscAtmIfPnniSigVcdTrafficShaping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfPnniSigVcdTrafficShaping.setStatus("mandatory")


class _MscAtmIfPnniSigVcdUnshapedTransmitQueueing_Type(Integer32):
    """Custom type mscAtmIfPnniSigVcdUnshapedTransmitQueueing based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("common", 1),
          ("sameAsCa", 3))
    )


_MscAtmIfPnniSigVcdUnshapedTransmitQueueing_Type.__name__ = "Integer32"
_MscAtmIfPnniSigVcdUnshapedTransmitQueueing_Object = MibTableColumn
mscAtmIfPnniSigVcdUnshapedTransmitQueueing = _MscAtmIfPnniSigVcdUnshapedTransmitQueueing_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 2, 2, 10, 1, 60),
    _MscAtmIfPnniSigVcdUnshapedTransmitQueueing_Type()
)
mscAtmIfPnniSigVcdUnshapedTransmitQueueing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfPnniSigVcdUnshapedTransmitQueueing.setStatus("mandatory")


class _MscAtmIfPnniSigVcdUsageParameterControl_Type(Integer32):
    """Custom type mscAtmIfPnniSigVcdUsageParameterControl based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("sameAsCa", 2))
    )


_MscAtmIfPnniSigVcdUsageParameterControl_Type.__name__ = "Integer32"
_MscAtmIfPnniSigVcdUsageParameterControl_Object = MibTableColumn
mscAtmIfPnniSigVcdUsageParameterControl = _MscAtmIfPnniSigVcdUsageParameterControl_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 2, 2, 10, 1, 70),
    _MscAtmIfPnniSigVcdUsageParameterControl_Type()
)
mscAtmIfPnniSigVcdUsageParameterControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfPnniSigVcdUsageParameterControl.setStatus("mandatory")
_MscAtmIfPnniSigVcdTdpTable_Object = MibTable
mscAtmIfPnniSigVcdTdpTable = _MscAtmIfPnniSigVcdTdpTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 2, 2, 387)
)
if mibBuilder.loadTexts:
    mscAtmIfPnniSigVcdTdpTable.setStatus("mandatory")
_MscAtmIfPnniSigVcdTdpEntry_Object = MibTableRow
mscAtmIfPnniSigVcdTdpEntry = _MscAtmIfPnniSigVcdTdpEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 2, 2, 387, 1)
)
mscAtmIfPnniSigVcdTdpEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmPnniMIB", "mscAtmIfPnniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmPnniMIB", "mscAtmIfPnniSigIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmPnniMIB", "mscAtmIfPnniSigVcdIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmPnniMIB", "mscAtmIfPnniSigVcdTdpIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfPnniSigVcdTdpEntry.setStatus("mandatory")


class _MscAtmIfPnniSigVcdTdpIndex_Type(Integer32):
    """Custom type mscAtmIfPnniSigVcdTdpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_MscAtmIfPnniSigVcdTdpIndex_Type.__name__ = "Integer32"
_MscAtmIfPnniSigVcdTdpIndex_Object = MibTableColumn
mscAtmIfPnniSigVcdTdpIndex = _MscAtmIfPnniSigVcdTdpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 2, 2, 387, 1, 1),
    _MscAtmIfPnniSigVcdTdpIndex_Type()
)
mscAtmIfPnniSigVcdTdpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAtmIfPnniSigVcdTdpIndex.setStatus("mandatory")


class _MscAtmIfPnniSigVcdTdpValue_Type(Unsigned32):
    """Custom type mscAtmIfPnniSigVcdTdpValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MscAtmIfPnniSigVcdTdpValue_Type.__name__ = "Unsigned32"
_MscAtmIfPnniSigVcdTdpValue_Object = MibTableColumn
mscAtmIfPnniSigVcdTdpValue = _MscAtmIfPnniSigVcdTdpValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 2, 2, 387, 1, 2),
    _MscAtmIfPnniSigVcdTdpValue_Type()
)
mscAtmIfPnniSigVcdTdpValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfPnniSigVcdTdpValue.setStatus("mandatory")
_MscAtmIfPnniSigProvTable_Object = MibTable
mscAtmIfPnniSigProvTable = _MscAtmIfPnniSigProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 2, 10)
)
if mibBuilder.loadTexts:
    mscAtmIfPnniSigProvTable.setStatus("mandatory")
_MscAtmIfPnniSigProvEntry_Object = MibTableRow
mscAtmIfPnniSigProvEntry = _MscAtmIfPnniSigProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 2, 10, 1)
)
mscAtmIfPnniSigProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmPnniMIB", "mscAtmIfPnniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmPnniMIB", "mscAtmIfPnniSigIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfPnniSigProvEntry.setStatus("mandatory")


class _MscAtmIfPnniSigVci_Type(Unsigned32):
    """Custom type mscAtmIfPnniSigVci based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscAtmIfPnniSigVci_Type.__name__ = "Unsigned32"
_MscAtmIfPnniSigVci_Object = MibTableColumn
mscAtmIfPnniSigVci = _MscAtmIfPnniSigVci_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 2, 10, 1, 1),
    _MscAtmIfPnniSigVci_Type()
)
mscAtmIfPnniSigVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfPnniSigVci.setStatus("mandatory")


class _MscAtmIfPnniSigAddressConversion_Type(Integer32):
    """Custom type mscAtmIfPnniSigAddressConversion based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nativeE164", 1),
          ("none", 0),
          ("nsap", 2))
    )


_MscAtmIfPnniSigAddressConversion_Type.__name__ = "Integer32"
_MscAtmIfPnniSigAddressConversion_Object = MibTableColumn
mscAtmIfPnniSigAddressConversion = _MscAtmIfPnniSigAddressConversion_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 2, 10, 1, 2),
    _MscAtmIfPnniSigAddressConversion_Type()
)
mscAtmIfPnniSigAddressConversion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfPnniSigAddressConversion.setStatus("mandatory")


class _MscAtmIfPnniSigOperatingMode_Type(Integer32):
    """Custom type mscAtmIfPnniSigOperatingMode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("provisionedOnly", 1))
    )


_MscAtmIfPnniSigOperatingMode_Type.__name__ = "Integer32"
_MscAtmIfPnniSigOperatingMode_Object = MibTableColumn
mscAtmIfPnniSigOperatingMode = _MscAtmIfPnniSigOperatingMode_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 2, 10, 1, 3),
    _MscAtmIfPnniSigOperatingMode_Type()
)
mscAtmIfPnniSigOperatingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfPnniSigOperatingMode.setStatus("mandatory")
_MscAtmIfPnniSigStateTable_Object = MibTable
mscAtmIfPnniSigStateTable = _MscAtmIfPnniSigStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 2, 11)
)
if mibBuilder.loadTexts:
    mscAtmIfPnniSigStateTable.setStatus("mandatory")
_MscAtmIfPnniSigStateEntry_Object = MibTableRow
mscAtmIfPnniSigStateEntry = _MscAtmIfPnniSigStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 2, 11, 1)
)
mscAtmIfPnniSigStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmPnniMIB", "mscAtmIfPnniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmPnniMIB", "mscAtmIfPnniSigIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfPnniSigStateEntry.setStatus("mandatory")


class _MscAtmIfPnniSigAdminState_Type(Integer32):
    """Custom type mscAtmIfPnniSigAdminState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("locked", 0),
          ("shuttingDown", 2),
          ("unlocked", 1))
    )


_MscAtmIfPnniSigAdminState_Type.__name__ = "Integer32"
_MscAtmIfPnniSigAdminState_Object = MibTableColumn
mscAtmIfPnniSigAdminState = _MscAtmIfPnniSigAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 2, 11, 1, 1),
    _MscAtmIfPnniSigAdminState_Type()
)
mscAtmIfPnniSigAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfPnniSigAdminState.setStatus("mandatory")


class _MscAtmIfPnniSigOperationalState_Type(Integer32):
    """Custom type mscAtmIfPnniSigOperationalState based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_MscAtmIfPnniSigOperationalState_Type.__name__ = "Integer32"
_MscAtmIfPnniSigOperationalState_Object = MibTableColumn
mscAtmIfPnniSigOperationalState = _MscAtmIfPnniSigOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 2, 11, 1, 2),
    _MscAtmIfPnniSigOperationalState_Type()
)
mscAtmIfPnniSigOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfPnniSigOperationalState.setStatus("mandatory")


class _MscAtmIfPnniSigUsageState_Type(Integer32):
    """Custom type mscAtmIfPnniSigUsageState based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("busy", 2),
          ("idle", 0))
    )


_MscAtmIfPnniSigUsageState_Type.__name__ = "Integer32"
_MscAtmIfPnniSigUsageState_Object = MibTableColumn
mscAtmIfPnniSigUsageState = _MscAtmIfPnniSigUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 2, 11, 1, 3),
    _MscAtmIfPnniSigUsageState_Type()
)
mscAtmIfPnniSigUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfPnniSigUsageState.setStatus("mandatory")
_MscAtmIfPnniSigOperTable_Object = MibTable
mscAtmIfPnniSigOperTable = _MscAtmIfPnniSigOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 2, 12)
)
if mibBuilder.loadTexts:
    mscAtmIfPnniSigOperTable.setStatus("mandatory")
_MscAtmIfPnniSigOperEntry_Object = MibTableRow
mscAtmIfPnniSigOperEntry = _MscAtmIfPnniSigOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 2, 12, 1)
)
mscAtmIfPnniSigOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmPnniMIB", "mscAtmIfPnniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmPnniMIB", "mscAtmIfPnniSigIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfPnniSigOperEntry.setStatus("mandatory")


class _MscAtmIfPnniSigLastTxCauseCode_Type(Unsigned32):
    """Custom type mscAtmIfPnniSigLastTxCauseCode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscAtmIfPnniSigLastTxCauseCode_Type.__name__ = "Unsigned32"
_MscAtmIfPnniSigLastTxCauseCode_Object = MibTableColumn
mscAtmIfPnniSigLastTxCauseCode = _MscAtmIfPnniSigLastTxCauseCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 2, 12, 1, 1),
    _MscAtmIfPnniSigLastTxCauseCode_Type()
)
mscAtmIfPnniSigLastTxCauseCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfPnniSigLastTxCauseCode.setStatus("mandatory")


class _MscAtmIfPnniSigLastTxDiagCode_Type(Hex):
    """Custom type mscAtmIfPnniSigLastTxDiagCode based on Hex"""
    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscAtmIfPnniSigLastTxDiagCode_Type.__name__ = "Hex"
_MscAtmIfPnniSigLastTxDiagCode_Object = MibTableColumn
mscAtmIfPnniSigLastTxDiagCode = _MscAtmIfPnniSigLastTxDiagCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 2, 12, 1, 2),
    _MscAtmIfPnniSigLastTxDiagCode_Type()
)
mscAtmIfPnniSigLastTxDiagCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfPnniSigLastTxDiagCode.setStatus("mandatory")


class _MscAtmIfPnniSigLastRxCauseCode_Type(Unsigned32):
    """Custom type mscAtmIfPnniSigLastRxCauseCode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscAtmIfPnniSigLastRxCauseCode_Type.__name__ = "Unsigned32"
_MscAtmIfPnniSigLastRxCauseCode_Object = MibTableColumn
mscAtmIfPnniSigLastRxCauseCode = _MscAtmIfPnniSigLastRxCauseCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 2, 12, 1, 3),
    _MscAtmIfPnniSigLastRxCauseCode_Type()
)
mscAtmIfPnniSigLastRxCauseCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfPnniSigLastRxCauseCode.setStatus("mandatory")


class _MscAtmIfPnniSigLastRxDiagCode_Type(Hex):
    """Custom type mscAtmIfPnniSigLastRxDiagCode based on Hex"""
    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscAtmIfPnniSigLastRxDiagCode_Type.__name__ = "Hex"
_MscAtmIfPnniSigLastRxDiagCode_Object = MibTableColumn
mscAtmIfPnniSigLastRxDiagCode = _MscAtmIfPnniSigLastRxDiagCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 2, 12, 1, 4),
    _MscAtmIfPnniSigLastRxDiagCode_Type()
)
mscAtmIfPnniSigLastRxDiagCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfPnniSigLastRxDiagCode.setStatus("mandatory")
_MscAtmIfPnniSigStatsTable_Object = MibTable
mscAtmIfPnniSigStatsTable = _MscAtmIfPnniSigStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 2, 13)
)
if mibBuilder.loadTexts:
    mscAtmIfPnniSigStatsTable.setStatus("mandatory")
_MscAtmIfPnniSigStatsEntry_Object = MibTableRow
mscAtmIfPnniSigStatsEntry = _MscAtmIfPnniSigStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 2, 13, 1)
)
mscAtmIfPnniSigStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmPnniMIB", "mscAtmIfPnniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmPnniMIB", "mscAtmIfPnniSigIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfPnniSigStatsEntry.setStatus("mandatory")
_MscAtmIfPnniSigCurrentConnections_Type = Counter32
_MscAtmIfPnniSigCurrentConnections_Object = MibTableColumn
mscAtmIfPnniSigCurrentConnections = _MscAtmIfPnniSigCurrentConnections_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 2, 13, 1, 1),
    _MscAtmIfPnniSigCurrentConnections_Type()
)
mscAtmIfPnniSigCurrentConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfPnniSigCurrentConnections.setStatus("obsolete")


class _MscAtmIfPnniSigPeakConnections_Type(Gauge32):
    """Custom type mscAtmIfPnniSigPeakConnections based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscAtmIfPnniSigPeakConnections_Type.__name__ = "Gauge32"
_MscAtmIfPnniSigPeakConnections_Object = MibTableColumn
mscAtmIfPnniSigPeakConnections = _MscAtmIfPnniSigPeakConnections_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 2, 13, 1, 2),
    _MscAtmIfPnniSigPeakConnections_Type()
)
mscAtmIfPnniSigPeakConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfPnniSigPeakConnections.setStatus("mandatory")
_MscAtmIfPnniSigSuccessfulConnections_Type = Counter32
_MscAtmIfPnniSigSuccessfulConnections_Object = MibTableColumn
mscAtmIfPnniSigSuccessfulConnections = _MscAtmIfPnniSigSuccessfulConnections_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 2, 13, 1, 3),
    _MscAtmIfPnniSigSuccessfulConnections_Type()
)
mscAtmIfPnniSigSuccessfulConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfPnniSigSuccessfulConnections.setStatus("mandatory")
_MscAtmIfPnniSigFailedConnections_Type = Counter32
_MscAtmIfPnniSigFailedConnections_Object = MibTableColumn
mscAtmIfPnniSigFailedConnections = _MscAtmIfPnniSigFailedConnections_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 2, 13, 1, 4),
    _MscAtmIfPnniSigFailedConnections_Type()
)
mscAtmIfPnniSigFailedConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfPnniSigFailedConnections.setStatus("mandatory")
_MscAtmIfPnniSigTxPdus_Type = Counter32
_MscAtmIfPnniSigTxPdus_Object = MibTableColumn
mscAtmIfPnniSigTxPdus = _MscAtmIfPnniSigTxPdus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 2, 13, 1, 5),
    _MscAtmIfPnniSigTxPdus_Type()
)
mscAtmIfPnniSigTxPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfPnniSigTxPdus.setStatus("mandatory")
_MscAtmIfPnniSigRxPdus_Type = Counter32
_MscAtmIfPnniSigRxPdus_Object = MibTableColumn
mscAtmIfPnniSigRxPdus = _MscAtmIfPnniSigRxPdus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 2, 13, 1, 6),
    _MscAtmIfPnniSigRxPdus_Type()
)
mscAtmIfPnniSigRxPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfPnniSigRxPdus.setStatus("mandatory")


class _MscAtmIfPnniSigCurrentPmpConnections_Type(Gauge32):
    """Custom type mscAtmIfPnniSigCurrentPmpConnections based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscAtmIfPnniSigCurrentPmpConnections_Type.__name__ = "Gauge32"
_MscAtmIfPnniSigCurrentPmpConnections_Object = MibTableColumn
mscAtmIfPnniSigCurrentPmpConnections = _MscAtmIfPnniSigCurrentPmpConnections_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 2, 13, 1, 7),
    _MscAtmIfPnniSigCurrentPmpConnections_Type()
)
mscAtmIfPnniSigCurrentPmpConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfPnniSigCurrentPmpConnections.setStatus("mandatory")


class _MscAtmIfPnniSigPeakPmpConnections_Type(Gauge32):
    """Custom type mscAtmIfPnniSigPeakPmpConnections based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscAtmIfPnniSigPeakPmpConnections_Type.__name__ = "Gauge32"
_MscAtmIfPnniSigPeakPmpConnections_Object = MibTableColumn
mscAtmIfPnniSigPeakPmpConnections = _MscAtmIfPnniSigPeakPmpConnections_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 2, 13, 1, 8),
    _MscAtmIfPnniSigPeakPmpConnections_Type()
)
mscAtmIfPnniSigPeakPmpConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfPnniSigPeakPmpConnections.setStatus("mandatory")
_MscAtmIfPnniSigSuccessfulPmpConnections_Type = Counter32
_MscAtmIfPnniSigSuccessfulPmpConnections_Object = MibTableColumn
mscAtmIfPnniSigSuccessfulPmpConnections = _MscAtmIfPnniSigSuccessfulPmpConnections_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 2, 13, 1, 9),
    _MscAtmIfPnniSigSuccessfulPmpConnections_Type()
)
mscAtmIfPnniSigSuccessfulPmpConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfPnniSigSuccessfulPmpConnections.setStatus("mandatory")
_MscAtmIfPnniSigFailedPmpConnections_Type = Counter32
_MscAtmIfPnniSigFailedPmpConnections_Object = MibTableColumn
mscAtmIfPnniSigFailedPmpConnections = _MscAtmIfPnniSigFailedPmpConnections_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 2, 13, 1, 10),
    _MscAtmIfPnniSigFailedPmpConnections_Type()
)
mscAtmIfPnniSigFailedPmpConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfPnniSigFailedPmpConnections.setStatus("mandatory")


class _MscAtmIfPnniSigNewCurrentConnections_Type(Gauge32):
    """Custom type mscAtmIfPnniSigNewCurrentConnections based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscAtmIfPnniSigNewCurrentConnections_Type.__name__ = "Gauge32"
_MscAtmIfPnniSigNewCurrentConnections_Object = MibTableColumn
mscAtmIfPnniSigNewCurrentConnections = _MscAtmIfPnniSigNewCurrentConnections_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 2, 13, 1, 11),
    _MscAtmIfPnniSigNewCurrentConnections_Type()
)
mscAtmIfPnniSigNewCurrentConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfPnniSigNewCurrentConnections.setStatus("mandatory")
_MscAtmIfPnniRcc_ObjectIdentity = ObjectIdentity
mscAtmIfPnniRcc = _MscAtmIfPnniRcc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 3)
)
_MscAtmIfPnniRccRowStatusTable_Object = MibTable
mscAtmIfPnniRccRowStatusTable = _MscAtmIfPnniRccRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 3, 1)
)
if mibBuilder.loadTexts:
    mscAtmIfPnniRccRowStatusTable.setStatus("mandatory")
_MscAtmIfPnniRccRowStatusEntry_Object = MibTableRow
mscAtmIfPnniRccRowStatusEntry = _MscAtmIfPnniRccRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 3, 1, 1)
)
mscAtmIfPnniRccRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmPnniMIB", "mscAtmIfPnniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmPnniMIB", "mscAtmIfPnniRccIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfPnniRccRowStatusEntry.setStatus("mandatory")
_MscAtmIfPnniRccRowStatus_Type = RowStatus
_MscAtmIfPnniRccRowStatus_Object = MibTableColumn
mscAtmIfPnniRccRowStatus = _MscAtmIfPnniRccRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 3, 1, 1, 1),
    _MscAtmIfPnniRccRowStatus_Type()
)
mscAtmIfPnniRccRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfPnniRccRowStatus.setStatus("mandatory")
_MscAtmIfPnniRccComponentName_Type = DisplayString
_MscAtmIfPnniRccComponentName_Object = MibTableColumn
mscAtmIfPnniRccComponentName = _MscAtmIfPnniRccComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 3, 1, 1, 2),
    _MscAtmIfPnniRccComponentName_Type()
)
mscAtmIfPnniRccComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfPnniRccComponentName.setStatus("mandatory")
_MscAtmIfPnniRccStorageType_Type = StorageType
_MscAtmIfPnniRccStorageType_Object = MibTableColumn
mscAtmIfPnniRccStorageType = _MscAtmIfPnniRccStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 3, 1, 1, 4),
    _MscAtmIfPnniRccStorageType_Type()
)
mscAtmIfPnniRccStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfPnniRccStorageType.setStatus("mandatory")
_MscAtmIfPnniRccIndex_Type = NonReplicated
_MscAtmIfPnniRccIndex_Object = MibTableColumn
mscAtmIfPnniRccIndex = _MscAtmIfPnniRccIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 3, 1, 1, 10),
    _MscAtmIfPnniRccIndex_Type()
)
mscAtmIfPnniRccIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAtmIfPnniRccIndex.setStatus("mandatory")
_MscAtmIfPnniRccVcd_ObjectIdentity = ObjectIdentity
mscAtmIfPnniRccVcd = _MscAtmIfPnniRccVcd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 3, 2)
)
_MscAtmIfPnniRccVcdRowStatusTable_Object = MibTable
mscAtmIfPnniRccVcdRowStatusTable = _MscAtmIfPnniRccVcdRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 3, 2, 1)
)
if mibBuilder.loadTexts:
    mscAtmIfPnniRccVcdRowStatusTable.setStatus("mandatory")
_MscAtmIfPnniRccVcdRowStatusEntry_Object = MibTableRow
mscAtmIfPnniRccVcdRowStatusEntry = _MscAtmIfPnniRccVcdRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 3, 2, 1, 1)
)
mscAtmIfPnniRccVcdRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmPnniMIB", "mscAtmIfPnniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmPnniMIB", "mscAtmIfPnniRccIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmPnniMIB", "mscAtmIfPnniRccVcdIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfPnniRccVcdRowStatusEntry.setStatus("mandatory")
_MscAtmIfPnniRccVcdRowStatus_Type = RowStatus
_MscAtmIfPnniRccVcdRowStatus_Object = MibTableColumn
mscAtmIfPnniRccVcdRowStatus = _MscAtmIfPnniRccVcdRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 3, 2, 1, 1, 1),
    _MscAtmIfPnniRccVcdRowStatus_Type()
)
mscAtmIfPnniRccVcdRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfPnniRccVcdRowStatus.setStatus("mandatory")
_MscAtmIfPnniRccVcdComponentName_Type = DisplayString
_MscAtmIfPnniRccVcdComponentName_Object = MibTableColumn
mscAtmIfPnniRccVcdComponentName = _MscAtmIfPnniRccVcdComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 3, 2, 1, 1, 2),
    _MscAtmIfPnniRccVcdComponentName_Type()
)
mscAtmIfPnniRccVcdComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfPnniRccVcdComponentName.setStatus("mandatory")
_MscAtmIfPnniRccVcdStorageType_Type = StorageType
_MscAtmIfPnniRccVcdStorageType_Object = MibTableColumn
mscAtmIfPnniRccVcdStorageType = _MscAtmIfPnniRccVcdStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 3, 2, 1, 1, 4),
    _MscAtmIfPnniRccVcdStorageType_Type()
)
mscAtmIfPnniRccVcdStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfPnniRccVcdStorageType.setStatus("mandatory")
_MscAtmIfPnniRccVcdIndex_Type = NonReplicated
_MscAtmIfPnniRccVcdIndex_Object = MibTableColumn
mscAtmIfPnniRccVcdIndex = _MscAtmIfPnniRccVcdIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 3, 2, 1, 1, 10),
    _MscAtmIfPnniRccVcdIndex_Type()
)
mscAtmIfPnniRccVcdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAtmIfPnniRccVcdIndex.setStatus("mandatory")
_MscAtmIfPnniRccVcdProvTable_Object = MibTable
mscAtmIfPnniRccVcdProvTable = _MscAtmIfPnniRccVcdProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 3, 2, 10)
)
if mibBuilder.loadTexts:
    mscAtmIfPnniRccVcdProvTable.setStatus("mandatory")
_MscAtmIfPnniRccVcdProvEntry_Object = MibTableRow
mscAtmIfPnniRccVcdProvEntry = _MscAtmIfPnniRccVcdProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 3, 2, 10, 1)
)
mscAtmIfPnniRccVcdProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmPnniMIB", "mscAtmIfPnniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmPnniMIB", "mscAtmIfPnniRccIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmPnniMIB", "mscAtmIfPnniRccVcdIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfPnniRccVcdProvEntry.setStatus("mandatory")


class _MscAtmIfPnniRccVcdTrafficDescType_Type(Integer32):
    """Custom type mscAtmIfPnniRccVcdTrafficDescType based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("n3", 3),
          ("n6", 6),
          ("n7", 7),
          ("n8", 8))
    )


_MscAtmIfPnniRccVcdTrafficDescType_Type.__name__ = "Integer32"
_MscAtmIfPnniRccVcdTrafficDescType_Object = MibTableColumn
mscAtmIfPnniRccVcdTrafficDescType = _MscAtmIfPnniRccVcdTrafficDescType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 3, 2, 10, 1, 1),
    _MscAtmIfPnniRccVcdTrafficDescType_Type()
)
mscAtmIfPnniRccVcdTrafficDescType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfPnniRccVcdTrafficDescType.setStatus("mandatory")


class _MscAtmIfPnniRccVcdAtmServiceCategory_Type(Integer32):
    """Custom type mscAtmIfPnniRccVcdAtmServiceCategory based on Integer32"""
    defaultValue = 2

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
        *(("constantBitRate", 1),
          ("nrtVariableBitRate", 3),
          ("rtVariableBitRate", 2),
          ("unspecifiedBitRate", 0))
    )


_MscAtmIfPnniRccVcdAtmServiceCategory_Type.__name__ = "Integer32"
_MscAtmIfPnniRccVcdAtmServiceCategory_Object = MibTableColumn
mscAtmIfPnniRccVcdAtmServiceCategory = _MscAtmIfPnniRccVcdAtmServiceCategory_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 3, 2, 10, 1, 3),
    _MscAtmIfPnniRccVcdAtmServiceCategory_Type()
)
mscAtmIfPnniRccVcdAtmServiceCategory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfPnniRccVcdAtmServiceCategory.setStatus("mandatory")


class _MscAtmIfPnniRccVcdWeight_Type(Unsigned32):
    """Custom type mscAtmIfPnniRccVcdWeight based on Unsigned32"""
    defaultValue = 65535

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4095),
        ValueRangeConstraint(65535, 65535),
    )


_MscAtmIfPnniRccVcdWeight_Type.__name__ = "Unsigned32"
_MscAtmIfPnniRccVcdWeight_Object = MibTableColumn
mscAtmIfPnniRccVcdWeight = _MscAtmIfPnniRccVcdWeight_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 3, 2, 10, 1, 4),
    _MscAtmIfPnniRccVcdWeight_Type()
)
mscAtmIfPnniRccVcdWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfPnniRccVcdWeight.setStatus("mandatory")


class _MscAtmIfPnniRccVcdQosClass_Type(Integer32):
    """Custom type mscAtmIfPnniRccVcdQosClass based on Integer32"""
    defaultValue = 2

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


_MscAtmIfPnniRccVcdQosClass_Type.__name__ = "Integer32"
_MscAtmIfPnniRccVcdQosClass_Object = MibTableColumn
mscAtmIfPnniRccVcdQosClass = _MscAtmIfPnniRccVcdQosClass_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 3, 2, 10, 1, 21),
    _MscAtmIfPnniRccVcdQosClass_Type()
)
mscAtmIfPnniRccVcdQosClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfPnniRccVcdQosClass.setStatus("mandatory")


class _MscAtmIfPnniRccVcdTrafficShaping_Type(Integer32):
    """Custom type mscAtmIfPnniRccVcdTrafficShaping based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("sameAsCa", 2))
    )


_MscAtmIfPnniRccVcdTrafficShaping_Type.__name__ = "Integer32"
_MscAtmIfPnniRccVcdTrafficShaping_Object = MibTableColumn
mscAtmIfPnniRccVcdTrafficShaping = _MscAtmIfPnniRccVcdTrafficShaping_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 3, 2, 10, 1, 50),
    _MscAtmIfPnniRccVcdTrafficShaping_Type()
)
mscAtmIfPnniRccVcdTrafficShaping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfPnniRccVcdTrafficShaping.setStatus("mandatory")


class _MscAtmIfPnniRccVcdUnshapedTransmitQueueing_Type(Integer32):
    """Custom type mscAtmIfPnniRccVcdUnshapedTransmitQueueing based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("common", 1),
          ("sameAsCa", 3))
    )


_MscAtmIfPnniRccVcdUnshapedTransmitQueueing_Type.__name__ = "Integer32"
_MscAtmIfPnniRccVcdUnshapedTransmitQueueing_Object = MibTableColumn
mscAtmIfPnniRccVcdUnshapedTransmitQueueing = _MscAtmIfPnniRccVcdUnshapedTransmitQueueing_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 3, 2, 10, 1, 60),
    _MscAtmIfPnniRccVcdUnshapedTransmitQueueing_Type()
)
mscAtmIfPnniRccVcdUnshapedTransmitQueueing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfPnniRccVcdUnshapedTransmitQueueing.setStatus("mandatory")


class _MscAtmIfPnniRccVcdUsageParameterControl_Type(Integer32):
    """Custom type mscAtmIfPnniRccVcdUsageParameterControl based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("sameAsCa", 2))
    )


_MscAtmIfPnniRccVcdUsageParameterControl_Type.__name__ = "Integer32"
_MscAtmIfPnniRccVcdUsageParameterControl_Object = MibTableColumn
mscAtmIfPnniRccVcdUsageParameterControl = _MscAtmIfPnniRccVcdUsageParameterControl_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 3, 2, 10, 1, 70),
    _MscAtmIfPnniRccVcdUsageParameterControl_Type()
)
mscAtmIfPnniRccVcdUsageParameterControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfPnniRccVcdUsageParameterControl.setStatus("mandatory")
_MscAtmIfPnniRccVcdTdpTable_Object = MibTable
mscAtmIfPnniRccVcdTdpTable = _MscAtmIfPnniRccVcdTdpTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 3, 2, 387)
)
if mibBuilder.loadTexts:
    mscAtmIfPnniRccVcdTdpTable.setStatus("mandatory")
_MscAtmIfPnniRccVcdTdpEntry_Object = MibTableRow
mscAtmIfPnniRccVcdTdpEntry = _MscAtmIfPnniRccVcdTdpEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 3, 2, 387, 1)
)
mscAtmIfPnniRccVcdTdpEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmPnniMIB", "mscAtmIfPnniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmPnniMIB", "mscAtmIfPnniRccIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmPnniMIB", "mscAtmIfPnniRccVcdIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmPnniMIB", "mscAtmIfPnniRccVcdTdpIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfPnniRccVcdTdpEntry.setStatus("mandatory")


class _MscAtmIfPnniRccVcdTdpIndex_Type(Integer32):
    """Custom type mscAtmIfPnniRccVcdTdpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_MscAtmIfPnniRccVcdTdpIndex_Type.__name__ = "Integer32"
_MscAtmIfPnniRccVcdTdpIndex_Object = MibTableColumn
mscAtmIfPnniRccVcdTdpIndex = _MscAtmIfPnniRccVcdTdpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 3, 2, 387, 1, 1),
    _MscAtmIfPnniRccVcdTdpIndex_Type()
)
mscAtmIfPnniRccVcdTdpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAtmIfPnniRccVcdTdpIndex.setStatus("mandatory")


class _MscAtmIfPnniRccVcdTdpValue_Type(Unsigned32):
    """Custom type mscAtmIfPnniRccVcdTdpValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MscAtmIfPnniRccVcdTdpValue_Type.__name__ = "Unsigned32"
_MscAtmIfPnniRccVcdTdpValue_Object = MibTableColumn
mscAtmIfPnniRccVcdTdpValue = _MscAtmIfPnniRccVcdTdpValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 3, 2, 387, 1, 2),
    _MscAtmIfPnniRccVcdTdpValue_Type()
)
mscAtmIfPnniRccVcdTdpValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfPnniRccVcdTdpValue.setStatus("mandatory")
_MscAtmIfPnniRccProvTable_Object = MibTable
mscAtmIfPnniRccProvTable = _MscAtmIfPnniRccProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 3, 10)
)
if mibBuilder.loadTexts:
    mscAtmIfPnniRccProvTable.setStatus("mandatory")
_MscAtmIfPnniRccProvEntry_Object = MibTableRow
mscAtmIfPnniRccProvEntry = _MscAtmIfPnniRccProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 3, 10, 1)
)
mscAtmIfPnniRccProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmPnniMIB", "mscAtmIfPnniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmPnniMIB", "mscAtmIfPnniRccIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfPnniRccProvEntry.setStatus("mandatory")


class _MscAtmIfPnniRccVci_Type(Unsigned32):
    """Custom type mscAtmIfPnniRccVci based on Unsigned32"""
    defaultValue = 18

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscAtmIfPnniRccVci_Type.__name__ = "Unsigned32"
_MscAtmIfPnniRccVci_Object = MibTableColumn
mscAtmIfPnniRccVci = _MscAtmIfPnniRccVci_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 3, 10, 1, 1),
    _MscAtmIfPnniRccVci_Type()
)
mscAtmIfPnniRccVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfPnniRccVci.setStatus("mandatory")
_MscAtmIfPnniRccHlParmsTable_Object = MibTable
mscAtmIfPnniRccHlParmsTable = _MscAtmIfPnniRccHlParmsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 3, 11)
)
if mibBuilder.loadTexts:
    mscAtmIfPnniRccHlParmsTable.setStatus("mandatory")
_MscAtmIfPnniRccHlParmsEntry_Object = MibTableRow
mscAtmIfPnniRccHlParmsEntry = _MscAtmIfPnniRccHlParmsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 3, 11, 1)
)
mscAtmIfPnniRccHlParmsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmPnniMIB", "mscAtmIfPnniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmPnniMIB", "mscAtmIfPnniRccIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfPnniRccHlParmsEntry.setStatus("mandatory")


class _MscAtmIfPnniRccHelloHoldDown_Type(FixedPoint1):
    """Custom type mscAtmIfPnniRccHelloHoldDown based on FixedPoint1"""
    defaultValue = 0

    subtypeSpec = FixedPoint1.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 655350),
    )


_MscAtmIfPnniRccHelloHoldDown_Type.__name__ = "FixedPoint1"
_MscAtmIfPnniRccHelloHoldDown_Object = MibTableColumn
mscAtmIfPnniRccHelloHoldDown = _MscAtmIfPnniRccHelloHoldDown_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 3, 11, 1, 1),
    _MscAtmIfPnniRccHelloHoldDown_Type()
)
mscAtmIfPnniRccHelloHoldDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfPnniRccHelloHoldDown.setStatus("mandatory")


class _MscAtmIfPnniRccHelloInterval_Type(Unsigned32):
    """Custom type mscAtmIfPnniRccHelloInterval based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscAtmIfPnniRccHelloInterval_Type.__name__ = "Unsigned32"
_MscAtmIfPnniRccHelloInterval_Object = MibTableColumn
mscAtmIfPnniRccHelloInterval = _MscAtmIfPnniRccHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 3, 11, 1, 2),
    _MscAtmIfPnniRccHelloInterval_Type()
)
mscAtmIfPnniRccHelloInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfPnniRccHelloInterval.setStatus("mandatory")


class _MscAtmIfPnniRccHelloInactivityFactor_Type(Unsigned32):
    """Custom type mscAtmIfPnniRccHelloInactivityFactor based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscAtmIfPnniRccHelloInactivityFactor_Type.__name__ = "Unsigned32"
_MscAtmIfPnniRccHelloInactivityFactor_Object = MibTableColumn
mscAtmIfPnniRccHelloInactivityFactor = _MscAtmIfPnniRccHelloInactivityFactor_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 3, 11, 1, 3),
    _MscAtmIfPnniRccHelloInactivityFactor_Type()
)
mscAtmIfPnniRccHelloInactivityFactor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfPnniRccHelloInactivityFactor.setStatus("mandatory")
_MscAtmIfPnniRccStateTable_Object = MibTable
mscAtmIfPnniRccStateTable = _MscAtmIfPnniRccStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 3, 12)
)
if mibBuilder.loadTexts:
    mscAtmIfPnniRccStateTable.setStatus("mandatory")
_MscAtmIfPnniRccStateEntry_Object = MibTableRow
mscAtmIfPnniRccStateEntry = _MscAtmIfPnniRccStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 3, 12, 1)
)
mscAtmIfPnniRccStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmPnniMIB", "mscAtmIfPnniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmPnniMIB", "mscAtmIfPnniRccIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfPnniRccStateEntry.setStatus("mandatory")


class _MscAtmIfPnniRccAdminState_Type(Integer32):
    """Custom type mscAtmIfPnniRccAdminState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("locked", 0),
          ("shuttingDown", 2),
          ("unlocked", 1))
    )


_MscAtmIfPnniRccAdminState_Type.__name__ = "Integer32"
_MscAtmIfPnniRccAdminState_Object = MibTableColumn
mscAtmIfPnniRccAdminState = _MscAtmIfPnniRccAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 3, 12, 1, 1),
    _MscAtmIfPnniRccAdminState_Type()
)
mscAtmIfPnniRccAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfPnniRccAdminState.setStatus("mandatory")


class _MscAtmIfPnniRccOperationalState_Type(Integer32):
    """Custom type mscAtmIfPnniRccOperationalState based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_MscAtmIfPnniRccOperationalState_Type.__name__ = "Integer32"
_MscAtmIfPnniRccOperationalState_Object = MibTableColumn
mscAtmIfPnniRccOperationalState = _MscAtmIfPnniRccOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 3, 12, 1, 2),
    _MscAtmIfPnniRccOperationalState_Type()
)
mscAtmIfPnniRccOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfPnniRccOperationalState.setStatus("mandatory")


class _MscAtmIfPnniRccUsageState_Type(Integer32):
    """Custom type mscAtmIfPnniRccUsageState based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("busy", 2),
          ("idle", 0))
    )


_MscAtmIfPnniRccUsageState_Type.__name__ = "Integer32"
_MscAtmIfPnniRccUsageState_Object = MibTableColumn
mscAtmIfPnniRccUsageState = _MscAtmIfPnniRccUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 3, 12, 1, 3),
    _MscAtmIfPnniRccUsageState_Type()
)
mscAtmIfPnniRccUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfPnniRccUsageState.setStatus("mandatory")
_MscAtmIfPnniRccOperTable_Object = MibTable
mscAtmIfPnniRccOperTable = _MscAtmIfPnniRccOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 3, 13)
)
if mibBuilder.loadTexts:
    mscAtmIfPnniRccOperTable.setStatus("mandatory")
_MscAtmIfPnniRccOperEntry_Object = MibTableRow
mscAtmIfPnniRccOperEntry = _MscAtmIfPnniRccOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 3, 13, 1)
)
mscAtmIfPnniRccOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmPnniMIB", "mscAtmIfPnniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmPnniMIB", "mscAtmIfPnniRccIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfPnniRccOperEntry.setStatus("mandatory")


class _MscAtmIfPnniRccType_Type(Integer32):
    """Custom type mscAtmIfPnniRccType based on Integer32"""
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
        *(("horizontalLinkToLGN", 3),
          ("lowestLevelHorizLink", 1),
          ("lowestLevelOutsideLink", 2),
          ("unknown", 0),
          ("uplink", 4))
    )


_MscAtmIfPnniRccType_Type.__name__ = "Integer32"
_MscAtmIfPnniRccType_Object = MibTableColumn
mscAtmIfPnniRccType = _MscAtmIfPnniRccType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 3, 13, 1, 1),
    _MscAtmIfPnniRccType_Type()
)
mscAtmIfPnniRccType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfPnniRccType.setStatus("mandatory")


class _MscAtmIfPnniRccNegotiatedVersion_Type(Integer32):
    """Custom type mscAtmIfPnniRccNegotiatedVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("unsupported", 0),
          ("version1point0", 1))
    )


_MscAtmIfPnniRccNegotiatedVersion_Type.__name__ = "Integer32"
_MscAtmIfPnniRccNegotiatedVersion_Object = MibTableColumn
mscAtmIfPnniRccNegotiatedVersion = _MscAtmIfPnniRccNegotiatedVersion_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 3, 13, 1, 2),
    _MscAtmIfPnniRccNegotiatedVersion_Type()
)
mscAtmIfPnniRccNegotiatedVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfPnniRccNegotiatedVersion.setStatus("mandatory")


class _MscAtmIfPnniRccHelloState_Type(Integer32):
    """Custom type mscAtmIfPnniRccHelloState based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("attempt", 2),
          ("commonOutside", 7),
          ("down", 1),
          ("notApplicable", 0),
          ("oneWayInside", 3),
          ("oneWayOutside", 5),
          ("twoWayInside", 4),
          ("twoWayOutside", 6))
    )


_MscAtmIfPnniRccHelloState_Type.__name__ = "Integer32"
_MscAtmIfPnniRccHelloState_Object = MibTableColumn
mscAtmIfPnniRccHelloState = _MscAtmIfPnniRccHelloState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 3, 13, 1, 3),
    _MscAtmIfPnniRccHelloState_Type()
)
mscAtmIfPnniRccHelloState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfPnniRccHelloState.setStatus("mandatory")


class _MscAtmIfPnniRccRemoteNodeId_Type(HexString):
    """Custom type mscAtmIfPnniRccRemoteNodeId based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(22, 22),
    )


_MscAtmIfPnniRccRemoteNodeId_Type.__name__ = "HexString"
_MscAtmIfPnniRccRemoteNodeId_Object = MibTableColumn
mscAtmIfPnniRccRemoteNodeId = _MscAtmIfPnniRccRemoteNodeId_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 3, 13, 1, 4),
    _MscAtmIfPnniRccRemoteNodeId_Type()
)
mscAtmIfPnniRccRemoteNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfPnniRccRemoteNodeId.setStatus("mandatory")


class _MscAtmIfPnniRccRemotePortId_Type(Unsigned32):
    """Custom type mscAtmIfPnniRccRemotePortId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscAtmIfPnniRccRemotePortId_Type.__name__ = "Unsigned32"
_MscAtmIfPnniRccRemotePortId_Object = MibTableColumn
mscAtmIfPnniRccRemotePortId = _MscAtmIfPnniRccRemotePortId_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 3, 13, 1, 5),
    _MscAtmIfPnniRccRemotePortId_Type()
)
mscAtmIfPnniRccRemotePortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfPnniRccRemotePortId.setStatus("mandatory")
_MscAtmIfPnniRccStatsTable_Object = MibTable
mscAtmIfPnniRccStatsTable = _MscAtmIfPnniRccStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 3, 14)
)
if mibBuilder.loadTexts:
    mscAtmIfPnniRccStatsTable.setStatus("mandatory")
_MscAtmIfPnniRccStatsEntry_Object = MibTableRow
mscAtmIfPnniRccStatsEntry = _MscAtmIfPnniRccStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 3, 14, 1)
)
mscAtmIfPnniRccStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmPnniMIB", "mscAtmIfPnniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmPnniMIB", "mscAtmIfPnniRccIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfPnniRccStatsEntry.setStatus("mandatory")
_MscAtmIfPnniRccHelloPacketsRx_Type = Counter32
_MscAtmIfPnniRccHelloPacketsRx_Object = MibTableColumn
mscAtmIfPnniRccHelloPacketsRx = _MscAtmIfPnniRccHelloPacketsRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 3, 14, 1, 1),
    _MscAtmIfPnniRccHelloPacketsRx_Type()
)
mscAtmIfPnniRccHelloPacketsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfPnniRccHelloPacketsRx.setStatus("mandatory")
_MscAtmIfPnniRccHelloPacketsTx_Type = Counter32
_MscAtmIfPnniRccHelloPacketsTx_Object = MibTableColumn
mscAtmIfPnniRccHelloPacketsTx = _MscAtmIfPnniRccHelloPacketsTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 3, 14, 1, 2),
    _MscAtmIfPnniRccHelloPacketsTx_Type()
)
mscAtmIfPnniRccHelloPacketsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfPnniRccHelloPacketsTx.setStatus("mandatory")
_MscAtmIfPnniRccMismatchedHelloPacketsRx_Type = Counter32
_MscAtmIfPnniRccMismatchedHelloPacketsRx_Object = MibTableColumn
mscAtmIfPnniRccMismatchedHelloPacketsRx = _MscAtmIfPnniRccMismatchedHelloPacketsRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 3, 14, 1, 3),
    _MscAtmIfPnniRccMismatchedHelloPacketsRx_Type()
)
mscAtmIfPnniRccMismatchedHelloPacketsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfPnniRccMismatchedHelloPacketsRx.setStatus("mandatory")
_MscAtmIfPnniRccBadHelloPacketsRx_Type = Counter32
_MscAtmIfPnniRccBadHelloPacketsRx_Object = MibTableColumn
mscAtmIfPnniRccBadHelloPacketsRx = _MscAtmIfPnniRccBadHelloPacketsRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 3, 14, 1, 4),
    _MscAtmIfPnniRccBadHelloPacketsRx_Type()
)
mscAtmIfPnniRccBadHelloPacketsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfPnniRccBadHelloPacketsRx.setStatus("mandatory")
_MscAtmIfPnniAddr_ObjectIdentity = ObjectIdentity
mscAtmIfPnniAddr = _MscAtmIfPnniAddr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 4)
)
_MscAtmIfPnniAddrRowStatusTable_Object = MibTable
mscAtmIfPnniAddrRowStatusTable = _MscAtmIfPnniAddrRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 4, 1)
)
if mibBuilder.loadTexts:
    mscAtmIfPnniAddrRowStatusTable.setStatus("mandatory")
_MscAtmIfPnniAddrRowStatusEntry_Object = MibTableRow
mscAtmIfPnniAddrRowStatusEntry = _MscAtmIfPnniAddrRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 4, 1, 1)
)
mscAtmIfPnniAddrRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmPnniMIB", "mscAtmIfPnniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmPnniMIB", "mscAtmIfPnniAddrAddressIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmPnniMIB", "mscAtmIfPnniAddrAddressTypeIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfPnniAddrRowStatusEntry.setStatus("mandatory")
_MscAtmIfPnniAddrRowStatus_Type = RowStatus
_MscAtmIfPnniAddrRowStatus_Object = MibTableColumn
mscAtmIfPnniAddrRowStatus = _MscAtmIfPnniAddrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 4, 1, 1, 1),
    _MscAtmIfPnniAddrRowStatus_Type()
)
mscAtmIfPnniAddrRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfPnniAddrRowStatus.setStatus("mandatory")
_MscAtmIfPnniAddrComponentName_Type = DisplayString
_MscAtmIfPnniAddrComponentName_Object = MibTableColumn
mscAtmIfPnniAddrComponentName = _MscAtmIfPnniAddrComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 4, 1, 1, 2),
    _MscAtmIfPnniAddrComponentName_Type()
)
mscAtmIfPnniAddrComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfPnniAddrComponentName.setStatus("mandatory")
_MscAtmIfPnniAddrStorageType_Type = StorageType
_MscAtmIfPnniAddrStorageType_Object = MibTableColumn
mscAtmIfPnniAddrStorageType = _MscAtmIfPnniAddrStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 4, 1, 1, 4),
    _MscAtmIfPnniAddrStorageType_Type()
)
mscAtmIfPnniAddrStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfPnniAddrStorageType.setStatus("mandatory")


class _MscAtmIfPnniAddrAddressIndex_Type(AsciiStringIndex):
    """Custom type mscAtmIfPnniAddrAddressIndex based on AsciiStringIndex"""
    subtypeSpec = AsciiStringIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_MscAtmIfPnniAddrAddressIndex_Type.__name__ = "AsciiStringIndex"
_MscAtmIfPnniAddrAddressIndex_Object = MibTableColumn
mscAtmIfPnniAddrAddressIndex = _MscAtmIfPnniAddrAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 4, 1, 1, 10),
    _MscAtmIfPnniAddrAddressIndex_Type()
)
mscAtmIfPnniAddrAddressIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAtmIfPnniAddrAddressIndex.setStatus("mandatory")


class _MscAtmIfPnniAddrAddressTypeIndex_Type(Integer32):
    """Custom type mscAtmIfPnniAddrAddressTypeIndex based on Integer32"""
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


_MscAtmIfPnniAddrAddressTypeIndex_Type.__name__ = "Integer32"
_MscAtmIfPnniAddrAddressTypeIndex_Object = MibTableColumn
mscAtmIfPnniAddrAddressTypeIndex = _MscAtmIfPnniAddrAddressTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 4, 1, 1, 11),
    _MscAtmIfPnniAddrAddressTypeIndex_Type()
)
mscAtmIfPnniAddrAddressTypeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAtmIfPnniAddrAddressTypeIndex.setStatus("mandatory")
_MscAtmIfPnniAddrTermSP_ObjectIdentity = ObjectIdentity
mscAtmIfPnniAddrTermSP = _MscAtmIfPnniAddrTermSP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 4, 2)
)
_MscAtmIfPnniAddrTermSPRowStatusTable_Object = MibTable
mscAtmIfPnniAddrTermSPRowStatusTable = _MscAtmIfPnniAddrTermSPRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 4, 2, 1)
)
if mibBuilder.loadTexts:
    mscAtmIfPnniAddrTermSPRowStatusTable.setStatus("mandatory")
_MscAtmIfPnniAddrTermSPRowStatusEntry_Object = MibTableRow
mscAtmIfPnniAddrTermSPRowStatusEntry = _MscAtmIfPnniAddrTermSPRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 4, 2, 1, 1)
)
mscAtmIfPnniAddrTermSPRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmPnniMIB", "mscAtmIfPnniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmPnniMIB", "mscAtmIfPnniAddrAddressIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmPnniMIB", "mscAtmIfPnniAddrAddressTypeIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmPnniMIB", "mscAtmIfPnniAddrTermSPIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfPnniAddrTermSPRowStatusEntry.setStatus("mandatory")
_MscAtmIfPnniAddrTermSPRowStatus_Type = RowStatus
_MscAtmIfPnniAddrTermSPRowStatus_Object = MibTableColumn
mscAtmIfPnniAddrTermSPRowStatus = _MscAtmIfPnniAddrTermSPRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 4, 2, 1, 1, 1),
    _MscAtmIfPnniAddrTermSPRowStatus_Type()
)
mscAtmIfPnniAddrTermSPRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfPnniAddrTermSPRowStatus.setStatus("mandatory")
_MscAtmIfPnniAddrTermSPComponentName_Type = DisplayString
_MscAtmIfPnniAddrTermSPComponentName_Object = MibTableColumn
mscAtmIfPnniAddrTermSPComponentName = _MscAtmIfPnniAddrTermSPComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 4, 2, 1, 1, 2),
    _MscAtmIfPnniAddrTermSPComponentName_Type()
)
mscAtmIfPnniAddrTermSPComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfPnniAddrTermSPComponentName.setStatus("mandatory")
_MscAtmIfPnniAddrTermSPStorageType_Type = StorageType
_MscAtmIfPnniAddrTermSPStorageType_Object = MibTableColumn
mscAtmIfPnniAddrTermSPStorageType = _MscAtmIfPnniAddrTermSPStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 4, 2, 1, 1, 4),
    _MscAtmIfPnniAddrTermSPStorageType_Type()
)
mscAtmIfPnniAddrTermSPStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfPnniAddrTermSPStorageType.setStatus("mandatory")
_MscAtmIfPnniAddrTermSPIndex_Type = NonReplicated
_MscAtmIfPnniAddrTermSPIndex_Object = MibTableColumn
mscAtmIfPnniAddrTermSPIndex = _MscAtmIfPnniAddrTermSPIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 4, 2, 1, 1, 10),
    _MscAtmIfPnniAddrTermSPIndex_Type()
)
mscAtmIfPnniAddrTermSPIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAtmIfPnniAddrTermSPIndex.setStatus("mandatory")
_MscAtmIfPnniAddrPnniInfo_ObjectIdentity = ObjectIdentity
mscAtmIfPnniAddrPnniInfo = _MscAtmIfPnniAddrPnniInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 4, 3)
)
_MscAtmIfPnniAddrPnniInfoRowStatusTable_Object = MibTable
mscAtmIfPnniAddrPnniInfoRowStatusTable = _MscAtmIfPnniAddrPnniInfoRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 4, 3, 1)
)
if mibBuilder.loadTexts:
    mscAtmIfPnniAddrPnniInfoRowStatusTable.setStatus("mandatory")
_MscAtmIfPnniAddrPnniInfoRowStatusEntry_Object = MibTableRow
mscAtmIfPnniAddrPnniInfoRowStatusEntry = _MscAtmIfPnniAddrPnniInfoRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 4, 3, 1, 1)
)
mscAtmIfPnniAddrPnniInfoRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmPnniMIB", "mscAtmIfPnniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmPnniMIB", "mscAtmIfPnniAddrAddressIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmPnniMIB", "mscAtmIfPnniAddrAddressTypeIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmPnniMIB", "mscAtmIfPnniAddrPnniInfoIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfPnniAddrPnniInfoRowStatusEntry.setStatus("mandatory")
_MscAtmIfPnniAddrPnniInfoRowStatus_Type = RowStatus
_MscAtmIfPnniAddrPnniInfoRowStatus_Object = MibTableColumn
mscAtmIfPnniAddrPnniInfoRowStatus = _MscAtmIfPnniAddrPnniInfoRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 4, 3, 1, 1, 1),
    _MscAtmIfPnniAddrPnniInfoRowStatus_Type()
)
mscAtmIfPnniAddrPnniInfoRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfPnniAddrPnniInfoRowStatus.setStatus("mandatory")
_MscAtmIfPnniAddrPnniInfoComponentName_Type = DisplayString
_MscAtmIfPnniAddrPnniInfoComponentName_Object = MibTableColumn
mscAtmIfPnniAddrPnniInfoComponentName = _MscAtmIfPnniAddrPnniInfoComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 4, 3, 1, 1, 2),
    _MscAtmIfPnniAddrPnniInfoComponentName_Type()
)
mscAtmIfPnniAddrPnniInfoComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfPnniAddrPnniInfoComponentName.setStatus("mandatory")
_MscAtmIfPnniAddrPnniInfoStorageType_Type = StorageType
_MscAtmIfPnniAddrPnniInfoStorageType_Object = MibTableColumn
mscAtmIfPnniAddrPnniInfoStorageType = _MscAtmIfPnniAddrPnniInfoStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 4, 3, 1, 1, 4),
    _MscAtmIfPnniAddrPnniInfoStorageType_Type()
)
mscAtmIfPnniAddrPnniInfoStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfPnniAddrPnniInfoStorageType.setStatus("mandatory")
_MscAtmIfPnniAddrPnniInfoIndex_Type = NonReplicated
_MscAtmIfPnniAddrPnniInfoIndex_Object = MibTableColumn
mscAtmIfPnniAddrPnniInfoIndex = _MscAtmIfPnniAddrPnniInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 4, 3, 1, 1, 10),
    _MscAtmIfPnniAddrPnniInfoIndex_Type()
)
mscAtmIfPnniAddrPnniInfoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAtmIfPnniAddrPnniInfoIndex.setStatus("mandatory")
_MscAtmIfPnniAddrPnniInfoProvTable_Object = MibTable
mscAtmIfPnniAddrPnniInfoProvTable = _MscAtmIfPnniAddrPnniInfoProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 4, 3, 10)
)
if mibBuilder.loadTexts:
    mscAtmIfPnniAddrPnniInfoProvTable.setStatus("mandatory")
_MscAtmIfPnniAddrPnniInfoProvEntry_Object = MibTableRow
mscAtmIfPnniAddrPnniInfoProvEntry = _MscAtmIfPnniAddrPnniInfoProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 4, 3, 10, 1)
)
mscAtmIfPnniAddrPnniInfoProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmPnniMIB", "mscAtmIfPnniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmPnniMIB", "mscAtmIfPnniAddrAddressIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmPnniMIB", "mscAtmIfPnniAddrAddressTypeIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmPnniMIB", "mscAtmIfPnniAddrPnniInfoIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfPnniAddrPnniInfoProvEntry.setStatus("mandatory")


class _MscAtmIfPnniAddrPnniInfoScope_Type(Integer32):
    """Custom type mscAtmIfPnniAddrPnniInfoScope based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 104),
    )


_MscAtmIfPnniAddrPnniInfoScope_Type.__name__ = "Integer32"
_MscAtmIfPnniAddrPnniInfoScope_Object = MibTableColumn
mscAtmIfPnniAddrPnniInfoScope = _MscAtmIfPnniAddrPnniInfoScope_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 4, 3, 10, 1, 1),
    _MscAtmIfPnniAddrPnniInfoScope_Type()
)
mscAtmIfPnniAddrPnniInfoScope.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfPnniAddrPnniInfoScope.setStatus("mandatory")


class _MscAtmIfPnniAddrPnniInfoReachability_Type(Integer32):
    """Custom type mscAtmIfPnniAddrPnniInfoReachability based on Integer32"""
    defaultValue = 0

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


_MscAtmIfPnniAddrPnniInfoReachability_Type.__name__ = "Integer32"
_MscAtmIfPnniAddrPnniInfoReachability_Object = MibTableColumn
mscAtmIfPnniAddrPnniInfoReachability = _MscAtmIfPnniAddrPnniInfoReachability_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 4, 3, 10, 1, 2),
    _MscAtmIfPnniAddrPnniInfoReachability_Type()
)
mscAtmIfPnniAddrPnniInfoReachability.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfPnniAddrPnniInfoReachability.setStatus("mandatory")
_MscAtmIfPnniAddrOperTable_Object = MibTable
mscAtmIfPnniAddrOperTable = _MscAtmIfPnniAddrOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 4, 10)
)
if mibBuilder.loadTexts:
    mscAtmIfPnniAddrOperTable.setStatus("mandatory")
_MscAtmIfPnniAddrOperEntry_Object = MibTableRow
mscAtmIfPnniAddrOperEntry = _MscAtmIfPnniAddrOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 4, 10, 1)
)
mscAtmIfPnniAddrOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmPnniMIB", "mscAtmIfPnniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmPnniMIB", "mscAtmIfPnniAddrAddressIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmPnniMIB", "mscAtmIfPnniAddrAddressTypeIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfPnniAddrOperEntry.setStatus("mandatory")


class _MscAtmIfPnniAddrScope_Type(Integer32):
    """Custom type mscAtmIfPnniAddrScope based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 104),
    )


_MscAtmIfPnniAddrScope_Type.__name__ = "Integer32"
_MscAtmIfPnniAddrScope_Object = MibTableColumn
mscAtmIfPnniAddrScope = _MscAtmIfPnniAddrScope_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 4, 10, 1, 1),
    _MscAtmIfPnniAddrScope_Type()
)
mscAtmIfPnniAddrScope.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfPnniAddrScope.setStatus("mandatory")


class _MscAtmIfPnniAddrReachability_Type(Integer32):
    """Custom type mscAtmIfPnniAddrReachability based on Integer32"""
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


_MscAtmIfPnniAddrReachability_Type.__name__ = "Integer32"
_MscAtmIfPnniAddrReachability_Object = MibTableColumn
mscAtmIfPnniAddrReachability = _MscAtmIfPnniAddrReachability_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 4, 10, 1, 2),
    _MscAtmIfPnniAddrReachability_Type()
)
mscAtmIfPnniAddrReachability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfPnniAddrReachability.setStatus("mandatory")
_MscAtmIfPnniProvTable_Object = MibTable
mscAtmIfPnniProvTable = _MscAtmIfPnniProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 10)
)
if mibBuilder.loadTexts:
    mscAtmIfPnniProvTable.setStatus("mandatory")
_MscAtmIfPnniProvEntry_Object = MibTableRow
mscAtmIfPnniProvEntry = _MscAtmIfPnniProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 10, 1)
)
mscAtmIfPnniProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmPnniMIB", "mscAtmIfPnniIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfPnniProvEntry.setStatus("mandatory")


class _MscAtmIfPnniSoftPvcRetryPeriod_Type(Unsigned32):
    """Custom type mscAtmIfPnniSoftPvcRetryPeriod based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 999999),
    )


_MscAtmIfPnniSoftPvcRetryPeriod_Type.__name__ = "Unsigned32"
_MscAtmIfPnniSoftPvcRetryPeriod_Object = MibTableColumn
mscAtmIfPnniSoftPvcRetryPeriod = _MscAtmIfPnniSoftPvcRetryPeriod_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 10, 1, 1),
    _MscAtmIfPnniSoftPvcRetryPeriod_Type()
)
mscAtmIfPnniSoftPvcRetryPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfPnniSoftPvcRetryPeriod.setStatus("obsolete")


class _MscAtmIfPnniSoftPvpAndPvcRetryPeriod_Type(Unsigned32):
    """Custom type mscAtmIfPnniSoftPvpAndPvcRetryPeriod based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 999999),
    )


_MscAtmIfPnniSoftPvpAndPvcRetryPeriod_Type.__name__ = "Unsigned32"
_MscAtmIfPnniSoftPvpAndPvcRetryPeriod_Object = MibTableColumn
mscAtmIfPnniSoftPvpAndPvcRetryPeriod = _MscAtmIfPnniSoftPvpAndPvcRetryPeriod_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 10, 1, 2),
    _MscAtmIfPnniSoftPvpAndPvcRetryPeriod_Type()
)
mscAtmIfPnniSoftPvpAndPvcRetryPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfPnniSoftPvpAndPvcRetryPeriod.setStatus("mandatory")


class _MscAtmIfPnniSoftPvpAndPvcHoldOffTime_Type(Unsigned32):
    """Custom type mscAtmIfPnniSoftPvpAndPvcHoldOffTime based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(50, 20000),
    )


_MscAtmIfPnniSoftPvpAndPvcHoldOffTime_Type.__name__ = "Unsigned32"
_MscAtmIfPnniSoftPvpAndPvcHoldOffTime_Object = MibTableColumn
mscAtmIfPnniSoftPvpAndPvcHoldOffTime = _MscAtmIfPnniSoftPvpAndPvcHoldOffTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 10, 1, 5),
    _MscAtmIfPnniSoftPvpAndPvcHoldOffTime_Type()
)
mscAtmIfPnniSoftPvpAndPvcHoldOffTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfPnniSoftPvpAndPvcHoldOffTime.setStatus("mandatory")
_MscAtmIfPnniAdminWeightsTable_Object = MibTable
mscAtmIfPnniAdminWeightsTable = _MscAtmIfPnniAdminWeightsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 11)
)
if mibBuilder.loadTexts:
    mscAtmIfPnniAdminWeightsTable.setStatus("mandatory")
_MscAtmIfPnniAdminWeightsEntry_Object = MibTableRow
mscAtmIfPnniAdminWeightsEntry = _MscAtmIfPnniAdminWeightsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 11, 1)
)
mscAtmIfPnniAdminWeightsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmPnniMIB", "mscAtmIfPnniIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfPnniAdminWeightsEntry.setStatus("mandatory")


class _MscAtmIfPnniCbrWeight_Type(Unsigned32):
    """Custom type mscAtmIfPnniCbrWeight based on Unsigned32"""
    defaultValue = 5040

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscAtmIfPnniCbrWeight_Type.__name__ = "Unsigned32"
_MscAtmIfPnniCbrWeight_Object = MibTableColumn
mscAtmIfPnniCbrWeight = _MscAtmIfPnniCbrWeight_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 11, 1, 1),
    _MscAtmIfPnniCbrWeight_Type()
)
mscAtmIfPnniCbrWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfPnniCbrWeight.setStatus("mandatory")


class _MscAtmIfPnniRtVbrWeight_Type(Unsigned32):
    """Custom type mscAtmIfPnniRtVbrWeight based on Unsigned32"""
    defaultValue = 5040

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscAtmIfPnniRtVbrWeight_Type.__name__ = "Unsigned32"
_MscAtmIfPnniRtVbrWeight_Object = MibTableColumn
mscAtmIfPnniRtVbrWeight = _MscAtmIfPnniRtVbrWeight_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 11, 1, 2),
    _MscAtmIfPnniRtVbrWeight_Type()
)
mscAtmIfPnniRtVbrWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfPnniRtVbrWeight.setStatus("mandatory")


class _MscAtmIfPnniNrtVbrWeight_Type(Unsigned32):
    """Custom type mscAtmIfPnniNrtVbrWeight based on Unsigned32"""
    defaultValue = 5040

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscAtmIfPnniNrtVbrWeight_Type.__name__ = "Unsigned32"
_MscAtmIfPnniNrtVbrWeight_Object = MibTableColumn
mscAtmIfPnniNrtVbrWeight = _MscAtmIfPnniNrtVbrWeight_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 11, 1, 3),
    _MscAtmIfPnniNrtVbrWeight_Type()
)
mscAtmIfPnniNrtVbrWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfPnniNrtVbrWeight.setStatus("mandatory")


class _MscAtmIfPnniUbrWeight_Type(Unsigned32):
    """Custom type mscAtmIfPnniUbrWeight based on Unsigned32"""
    defaultValue = 5040

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscAtmIfPnniUbrWeight_Type.__name__ = "Unsigned32"
_MscAtmIfPnniUbrWeight_Object = MibTableColumn
mscAtmIfPnniUbrWeight = _MscAtmIfPnniUbrWeight_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 11, 1, 4),
    _MscAtmIfPnniUbrWeight_Type()
)
mscAtmIfPnniUbrWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfPnniUbrWeight.setStatus("mandatory")
_MscAtmIfPnniAcctOptTable_Object = MibTable
mscAtmIfPnniAcctOptTable = _MscAtmIfPnniAcctOptTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 12)
)
if mibBuilder.loadTexts:
    mscAtmIfPnniAcctOptTable.setStatus("mandatory")
_MscAtmIfPnniAcctOptEntry_Object = MibTableRow
mscAtmIfPnniAcctOptEntry = _MscAtmIfPnniAcctOptEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 12, 1)
)
mscAtmIfPnniAcctOptEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmPnniMIB", "mscAtmIfPnniIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfPnniAcctOptEntry.setStatus("mandatory")


class _MscAtmIfPnniAccountCollection_Type(OctetString):
    """Custom type mscAtmIfPnniAccountCollection based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscAtmIfPnniAccountCollection_Type.__name__ = "OctetString"
_MscAtmIfPnniAccountCollection_Object = MibTableColumn
mscAtmIfPnniAccountCollection = _MscAtmIfPnniAccountCollection_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 12, 1, 1),
    _MscAtmIfPnniAccountCollection_Type()
)
mscAtmIfPnniAccountCollection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfPnniAccountCollection.setStatus("mandatory")


class _MscAtmIfPnniAccountConnectionType_Type(Integer32):
    """Custom type mscAtmIfPnniAccountConnectionType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("intermediate", 1),
          ("origTerm", 0))
    )


_MscAtmIfPnniAccountConnectionType_Type.__name__ = "Integer32"
_MscAtmIfPnniAccountConnectionType_Object = MibTableColumn
mscAtmIfPnniAccountConnectionType = _MscAtmIfPnniAccountConnectionType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 12, 1, 2),
    _MscAtmIfPnniAccountConnectionType_Type()
)
mscAtmIfPnniAccountConnectionType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfPnniAccountConnectionType.setStatus("mandatory")


class _MscAtmIfPnniAccountClass_Type(Unsigned32):
    """Custom type mscAtmIfPnniAccountClass based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscAtmIfPnniAccountClass_Type.__name__ = "Unsigned32"
_MscAtmIfPnniAccountClass_Object = MibTableColumn
mscAtmIfPnniAccountClass = _MscAtmIfPnniAccountClass_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 12, 1, 3),
    _MscAtmIfPnniAccountClass_Type()
)
mscAtmIfPnniAccountClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfPnniAccountClass.setStatus("mandatory")


class _MscAtmIfPnniServiceExchange_Type(Unsigned32):
    """Custom type mscAtmIfPnniServiceExchange based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscAtmIfPnniServiceExchange_Type.__name__ = "Unsigned32"
_MscAtmIfPnniServiceExchange_Object = MibTableColumn
mscAtmIfPnniServiceExchange = _MscAtmIfPnniServiceExchange_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 12, 1, 4),
    _MscAtmIfPnniServiceExchange_Type()
)
mscAtmIfPnniServiceExchange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfPnniServiceExchange.setStatus("mandatory")
_MscAtmIfPnniOperationalTable_Object = MibTable
mscAtmIfPnniOperationalTable = _MscAtmIfPnniOperationalTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 13)
)
if mibBuilder.loadTexts:
    mscAtmIfPnniOperationalTable.setStatus("mandatory")
_MscAtmIfPnniOperationalEntry_Object = MibTableRow
mscAtmIfPnniOperationalEntry = _MscAtmIfPnniOperationalEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 13, 1)
)
mscAtmIfPnniOperationalEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmPnniMIB", "mscAtmIfPnniIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfPnniOperationalEntry.setStatus("mandatory")


class _MscAtmIfPnniPortId_Type(Unsigned32):
    """Custom type mscAtmIfPnniPortId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscAtmIfPnniPortId_Type.__name__ = "Unsigned32"
_MscAtmIfPnniPortId_Object = MibTableColumn
mscAtmIfPnniPortId = _MscAtmIfPnniPortId_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 96, 13, 1, 1),
    _MscAtmIfPnniPortId_Type()
)
mscAtmIfPnniPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfPnniPortId.setStatus("mandatory")
_AtmPnniMIB_ObjectIdentity = ObjectIdentity
atmPnniMIB = _AtmPnniMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 72)
)
_AtmPnniGroup_ObjectIdentity = ObjectIdentity
atmPnniGroup = _AtmPnniGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 72, 1)
)
_AtmPnniGroupCA_ObjectIdentity = ObjectIdentity
atmPnniGroupCA = _AtmPnniGroupCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 72, 1, 1)
)
_AtmPnniGroupCA02_ObjectIdentity = ObjectIdentity
atmPnniGroupCA02 = _AtmPnniGroupCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 72, 1, 1, 3)
)
_AtmPnniGroupCA02A_ObjectIdentity = ObjectIdentity
atmPnniGroupCA02A = _AtmPnniGroupCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 72, 1, 1, 3, 2)
)
_AtmPnniCapabilities_ObjectIdentity = ObjectIdentity
atmPnniCapabilities = _AtmPnniCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 72, 3)
)
_AtmPnniCapabilitiesCA_ObjectIdentity = ObjectIdentity
atmPnniCapabilitiesCA = _AtmPnniCapabilitiesCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 72, 3, 1)
)
_AtmPnniCapabilitiesCA02_ObjectIdentity = ObjectIdentity
atmPnniCapabilitiesCA02 = _AtmPnniCapabilitiesCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 72, 3, 1, 3)
)
_AtmPnniCapabilitiesCA02A_ObjectIdentity = ObjectIdentity
atmPnniCapabilitiesCA02A = _AtmPnniCapabilitiesCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 72, 3, 1, 3, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-MsCarrier-MscPassport-AtmPnniMIB",
    **{"mscAtmIfVptPnni": mscAtmIfVptPnni,
       "mscAtmIfVptPnniRowStatusTable": mscAtmIfVptPnniRowStatusTable,
       "mscAtmIfVptPnniRowStatusEntry": mscAtmIfVptPnniRowStatusEntry,
       "mscAtmIfVptPnniRowStatus": mscAtmIfVptPnniRowStatus,
       "mscAtmIfVptPnniComponentName": mscAtmIfVptPnniComponentName,
       "mscAtmIfVptPnniStorageType": mscAtmIfVptPnniStorageType,
       "mscAtmIfVptPnniIndex": mscAtmIfVptPnniIndex,
       "mscAtmIfVptPnniSig": mscAtmIfVptPnniSig,
       "mscAtmIfVptPnniSigRowStatusTable": mscAtmIfVptPnniSigRowStatusTable,
       "mscAtmIfVptPnniSigRowStatusEntry": mscAtmIfVptPnniSigRowStatusEntry,
       "mscAtmIfVptPnniSigRowStatus": mscAtmIfVptPnniSigRowStatus,
       "mscAtmIfVptPnniSigComponentName": mscAtmIfVptPnniSigComponentName,
       "mscAtmIfVptPnniSigStorageType": mscAtmIfVptPnniSigStorageType,
       "mscAtmIfVptPnniSigIndex": mscAtmIfVptPnniSigIndex,
       "mscAtmIfVptPnniSigVcd": mscAtmIfVptPnniSigVcd,
       "mscAtmIfVptPnniSigVcdRowStatusTable": mscAtmIfVptPnniSigVcdRowStatusTable,
       "mscAtmIfVptPnniSigVcdRowStatusEntry": mscAtmIfVptPnniSigVcdRowStatusEntry,
       "mscAtmIfVptPnniSigVcdRowStatus": mscAtmIfVptPnniSigVcdRowStatus,
       "mscAtmIfVptPnniSigVcdComponentName": mscAtmIfVptPnniSigVcdComponentName,
       "mscAtmIfVptPnniSigVcdStorageType": mscAtmIfVptPnniSigVcdStorageType,
       "mscAtmIfVptPnniSigVcdIndex": mscAtmIfVptPnniSigVcdIndex,
       "mscAtmIfVptPnniSigVcdProvTable": mscAtmIfVptPnniSigVcdProvTable,
       "mscAtmIfVptPnniSigVcdProvEntry": mscAtmIfVptPnniSigVcdProvEntry,
       "mscAtmIfVptPnniSigVcdTrafficDescType": mscAtmIfVptPnniSigVcdTrafficDescType,
       "mscAtmIfVptPnniSigVcdAtmServiceCategory": mscAtmIfVptPnniSigVcdAtmServiceCategory,
       "mscAtmIfVptPnniSigVcdWeight": mscAtmIfVptPnniSigVcdWeight,
       "mscAtmIfVptPnniSigVcdQosClass": mscAtmIfVptPnniSigVcdQosClass,
       "mscAtmIfVptPnniSigVcdTrafficShaping": mscAtmIfVptPnniSigVcdTrafficShaping,
       "mscAtmIfVptPnniSigVcdUnshapedTransmitQueueing": mscAtmIfVptPnniSigVcdUnshapedTransmitQueueing,
       "mscAtmIfVptPnniSigVcdUsageParameterControl": mscAtmIfVptPnniSigVcdUsageParameterControl,
       "mscAtmIfVptPnniSigVcdTdpTable": mscAtmIfVptPnniSigVcdTdpTable,
       "mscAtmIfVptPnniSigVcdTdpEntry": mscAtmIfVptPnniSigVcdTdpEntry,
       "mscAtmIfVptPnniSigVcdTdpIndex": mscAtmIfVptPnniSigVcdTdpIndex,
       "mscAtmIfVptPnniSigVcdTdpValue": mscAtmIfVptPnniSigVcdTdpValue,
       "mscAtmIfVptPnniSigProvTable": mscAtmIfVptPnniSigProvTable,
       "mscAtmIfVptPnniSigProvEntry": mscAtmIfVptPnniSigProvEntry,
       "mscAtmIfVptPnniSigVci": mscAtmIfVptPnniSigVci,
       "mscAtmIfVptPnniSigAddressConversion": mscAtmIfVptPnniSigAddressConversion,
       "mscAtmIfVptPnniSigOperatingMode": mscAtmIfVptPnniSigOperatingMode,
       "mscAtmIfVptPnniSigStateTable": mscAtmIfVptPnniSigStateTable,
       "mscAtmIfVptPnniSigStateEntry": mscAtmIfVptPnniSigStateEntry,
       "mscAtmIfVptPnniSigAdminState": mscAtmIfVptPnniSigAdminState,
       "mscAtmIfVptPnniSigOperationalState": mscAtmIfVptPnniSigOperationalState,
       "mscAtmIfVptPnniSigUsageState": mscAtmIfVptPnniSigUsageState,
       "mscAtmIfVptPnniSigOperTable": mscAtmIfVptPnniSigOperTable,
       "mscAtmIfVptPnniSigOperEntry": mscAtmIfVptPnniSigOperEntry,
       "mscAtmIfVptPnniSigLastTxCauseCode": mscAtmIfVptPnniSigLastTxCauseCode,
       "mscAtmIfVptPnniSigLastTxDiagCode": mscAtmIfVptPnniSigLastTxDiagCode,
       "mscAtmIfVptPnniSigLastRxCauseCode": mscAtmIfVptPnniSigLastRxCauseCode,
       "mscAtmIfVptPnniSigLastRxDiagCode": mscAtmIfVptPnniSigLastRxDiagCode,
       "mscAtmIfVptPnniSigStatsTable": mscAtmIfVptPnniSigStatsTable,
       "mscAtmIfVptPnniSigStatsEntry": mscAtmIfVptPnniSigStatsEntry,
       "mscAtmIfVptPnniSigCurrentConnections": mscAtmIfVptPnniSigCurrentConnections,
       "mscAtmIfVptPnniSigPeakConnections": mscAtmIfVptPnniSigPeakConnections,
       "mscAtmIfVptPnniSigSuccessfulConnections": mscAtmIfVptPnniSigSuccessfulConnections,
       "mscAtmIfVptPnniSigFailedConnections": mscAtmIfVptPnniSigFailedConnections,
       "mscAtmIfVptPnniSigTxPdus": mscAtmIfVptPnniSigTxPdus,
       "mscAtmIfVptPnniSigRxPdus": mscAtmIfVptPnniSigRxPdus,
       "mscAtmIfVptPnniSigCurrentPmpConnections": mscAtmIfVptPnniSigCurrentPmpConnections,
       "mscAtmIfVptPnniSigPeakPmpConnections": mscAtmIfVptPnniSigPeakPmpConnections,
       "mscAtmIfVptPnniSigSuccessfulPmpConnections": mscAtmIfVptPnniSigSuccessfulPmpConnections,
       "mscAtmIfVptPnniSigFailedPmpConnections": mscAtmIfVptPnniSigFailedPmpConnections,
       "mscAtmIfVptPnniSigNewCurrentConnections": mscAtmIfVptPnniSigNewCurrentConnections,
       "mscAtmIfVptPnniRcc": mscAtmIfVptPnniRcc,
       "mscAtmIfVptPnniRccRowStatusTable": mscAtmIfVptPnniRccRowStatusTable,
       "mscAtmIfVptPnniRccRowStatusEntry": mscAtmIfVptPnniRccRowStatusEntry,
       "mscAtmIfVptPnniRccRowStatus": mscAtmIfVptPnniRccRowStatus,
       "mscAtmIfVptPnniRccComponentName": mscAtmIfVptPnniRccComponentName,
       "mscAtmIfVptPnniRccStorageType": mscAtmIfVptPnniRccStorageType,
       "mscAtmIfVptPnniRccIndex": mscAtmIfVptPnniRccIndex,
       "mscAtmIfVptPnniRccVcd": mscAtmIfVptPnniRccVcd,
       "mscAtmIfVptPnniRccVcdRowStatusTable": mscAtmIfVptPnniRccVcdRowStatusTable,
       "mscAtmIfVptPnniRccVcdRowStatusEntry": mscAtmIfVptPnniRccVcdRowStatusEntry,
       "mscAtmIfVptPnniRccVcdRowStatus": mscAtmIfVptPnniRccVcdRowStatus,
       "mscAtmIfVptPnniRccVcdComponentName": mscAtmIfVptPnniRccVcdComponentName,
       "mscAtmIfVptPnniRccVcdStorageType": mscAtmIfVptPnniRccVcdStorageType,
       "mscAtmIfVptPnniRccVcdIndex": mscAtmIfVptPnniRccVcdIndex,
       "mscAtmIfVptPnniRccVcdProvTable": mscAtmIfVptPnniRccVcdProvTable,
       "mscAtmIfVptPnniRccVcdProvEntry": mscAtmIfVptPnniRccVcdProvEntry,
       "mscAtmIfVptPnniRccVcdTrafficDescType": mscAtmIfVptPnniRccVcdTrafficDescType,
       "mscAtmIfVptPnniRccVcdAtmServiceCategory": mscAtmIfVptPnniRccVcdAtmServiceCategory,
       "mscAtmIfVptPnniRccVcdWeight": mscAtmIfVptPnniRccVcdWeight,
       "mscAtmIfVptPnniRccVcdQosClass": mscAtmIfVptPnniRccVcdQosClass,
       "mscAtmIfVptPnniRccVcdTrafficShaping": mscAtmIfVptPnniRccVcdTrafficShaping,
       "mscAtmIfVptPnniRccVcdUnshapedTransmitQueueing": mscAtmIfVptPnniRccVcdUnshapedTransmitQueueing,
       "mscAtmIfVptPnniRccVcdUsageParameterControl": mscAtmIfVptPnniRccVcdUsageParameterControl,
       "mscAtmIfVptPnniRccVcdTdpTable": mscAtmIfVptPnniRccVcdTdpTable,
       "mscAtmIfVptPnniRccVcdTdpEntry": mscAtmIfVptPnniRccVcdTdpEntry,
       "mscAtmIfVptPnniRccVcdTdpIndex": mscAtmIfVptPnniRccVcdTdpIndex,
       "mscAtmIfVptPnniRccVcdTdpValue": mscAtmIfVptPnniRccVcdTdpValue,
       "mscAtmIfVptPnniRccProvTable": mscAtmIfVptPnniRccProvTable,
       "mscAtmIfVptPnniRccProvEntry": mscAtmIfVptPnniRccProvEntry,
       "mscAtmIfVptPnniRccVci": mscAtmIfVptPnniRccVci,
       "mscAtmIfVptPnniRccHlParmsTable": mscAtmIfVptPnniRccHlParmsTable,
       "mscAtmIfVptPnniRccHlParmsEntry": mscAtmIfVptPnniRccHlParmsEntry,
       "mscAtmIfVptPnniRccHelloHoldDown": mscAtmIfVptPnniRccHelloHoldDown,
       "mscAtmIfVptPnniRccHelloInterval": mscAtmIfVptPnniRccHelloInterval,
       "mscAtmIfVptPnniRccHelloInactivityFactor": mscAtmIfVptPnniRccHelloInactivityFactor,
       "mscAtmIfVptPnniRccStateTable": mscAtmIfVptPnniRccStateTable,
       "mscAtmIfVptPnniRccStateEntry": mscAtmIfVptPnniRccStateEntry,
       "mscAtmIfVptPnniRccAdminState": mscAtmIfVptPnniRccAdminState,
       "mscAtmIfVptPnniRccOperationalState": mscAtmIfVptPnniRccOperationalState,
       "mscAtmIfVptPnniRccUsageState": mscAtmIfVptPnniRccUsageState,
       "mscAtmIfVptPnniRccOperTable": mscAtmIfVptPnniRccOperTable,
       "mscAtmIfVptPnniRccOperEntry": mscAtmIfVptPnniRccOperEntry,
       "mscAtmIfVptPnniRccType": mscAtmIfVptPnniRccType,
       "mscAtmIfVptPnniRccNegotiatedVersion": mscAtmIfVptPnniRccNegotiatedVersion,
       "mscAtmIfVptPnniRccHelloState": mscAtmIfVptPnniRccHelloState,
       "mscAtmIfVptPnniRccRemoteNodeId": mscAtmIfVptPnniRccRemoteNodeId,
       "mscAtmIfVptPnniRccRemotePortId": mscAtmIfVptPnniRccRemotePortId,
       "mscAtmIfVptPnniRccStatsTable": mscAtmIfVptPnniRccStatsTable,
       "mscAtmIfVptPnniRccStatsEntry": mscAtmIfVptPnniRccStatsEntry,
       "mscAtmIfVptPnniRccHelloPacketsRx": mscAtmIfVptPnniRccHelloPacketsRx,
       "mscAtmIfVptPnniRccHelloPacketsTx": mscAtmIfVptPnniRccHelloPacketsTx,
       "mscAtmIfVptPnniRccMismatchedHelloPacketsRx": mscAtmIfVptPnniRccMismatchedHelloPacketsRx,
       "mscAtmIfVptPnniRccBadHelloPacketsRx": mscAtmIfVptPnniRccBadHelloPacketsRx,
       "mscAtmIfVptPnniAddr": mscAtmIfVptPnniAddr,
       "mscAtmIfVptPnniAddrRowStatusTable": mscAtmIfVptPnniAddrRowStatusTable,
       "mscAtmIfVptPnniAddrRowStatusEntry": mscAtmIfVptPnniAddrRowStatusEntry,
       "mscAtmIfVptPnniAddrRowStatus": mscAtmIfVptPnniAddrRowStatus,
       "mscAtmIfVptPnniAddrComponentName": mscAtmIfVptPnniAddrComponentName,
       "mscAtmIfVptPnniAddrStorageType": mscAtmIfVptPnniAddrStorageType,
       "mscAtmIfVptPnniAddrAddressIndex": mscAtmIfVptPnniAddrAddressIndex,
       "mscAtmIfVptPnniAddrAddressTypeIndex": mscAtmIfVptPnniAddrAddressTypeIndex,
       "mscAtmIfVptPnniAddrTermSP": mscAtmIfVptPnniAddrTermSP,
       "mscAtmIfVptPnniAddrTermSPRowStatusTable": mscAtmIfVptPnniAddrTermSPRowStatusTable,
       "mscAtmIfVptPnniAddrTermSPRowStatusEntry": mscAtmIfVptPnniAddrTermSPRowStatusEntry,
       "mscAtmIfVptPnniAddrTermSPRowStatus": mscAtmIfVptPnniAddrTermSPRowStatus,
       "mscAtmIfVptPnniAddrTermSPComponentName": mscAtmIfVptPnniAddrTermSPComponentName,
       "mscAtmIfVptPnniAddrTermSPStorageType": mscAtmIfVptPnniAddrTermSPStorageType,
       "mscAtmIfVptPnniAddrTermSPIndex": mscAtmIfVptPnniAddrTermSPIndex,
       "mscAtmIfVptPnniAddrPnniInfo": mscAtmIfVptPnniAddrPnniInfo,
       "mscAtmIfVptPnniAddrPnniInfoRowStatusTable": mscAtmIfVptPnniAddrPnniInfoRowStatusTable,
       "mscAtmIfVptPnniAddrPnniInfoRowStatusEntry": mscAtmIfVptPnniAddrPnniInfoRowStatusEntry,
       "mscAtmIfVptPnniAddrPnniInfoRowStatus": mscAtmIfVptPnniAddrPnniInfoRowStatus,
       "mscAtmIfVptPnniAddrPnniInfoComponentName": mscAtmIfVptPnniAddrPnniInfoComponentName,
       "mscAtmIfVptPnniAddrPnniInfoStorageType": mscAtmIfVptPnniAddrPnniInfoStorageType,
       "mscAtmIfVptPnniAddrPnniInfoIndex": mscAtmIfVptPnniAddrPnniInfoIndex,
       "mscAtmIfVptPnniAddrPnniInfoProvTable": mscAtmIfVptPnniAddrPnniInfoProvTable,
       "mscAtmIfVptPnniAddrPnniInfoProvEntry": mscAtmIfVptPnniAddrPnniInfoProvEntry,
       "mscAtmIfVptPnniAddrPnniInfoScope": mscAtmIfVptPnniAddrPnniInfoScope,
       "mscAtmIfVptPnniAddrPnniInfoReachability": mscAtmIfVptPnniAddrPnniInfoReachability,
       "mscAtmIfVptPnniAddrOperTable": mscAtmIfVptPnniAddrOperTable,
       "mscAtmIfVptPnniAddrOperEntry": mscAtmIfVptPnniAddrOperEntry,
       "mscAtmIfVptPnniAddrScope": mscAtmIfVptPnniAddrScope,
       "mscAtmIfVptPnniAddrReachability": mscAtmIfVptPnniAddrReachability,
       "mscAtmIfVptPnniProvTable": mscAtmIfVptPnniProvTable,
       "mscAtmIfVptPnniProvEntry": mscAtmIfVptPnniProvEntry,
       "mscAtmIfVptPnniSoftPvcRetryPeriod": mscAtmIfVptPnniSoftPvcRetryPeriod,
       "mscAtmIfVptPnniSoftPvpAndPvcRetryPeriod": mscAtmIfVptPnniSoftPvpAndPvcRetryPeriod,
       "mscAtmIfVptPnniSoftPvpAndPvcHoldOffTime": mscAtmIfVptPnniSoftPvpAndPvcHoldOffTime,
       "mscAtmIfVptPnniAdminWeightsTable": mscAtmIfVptPnniAdminWeightsTable,
       "mscAtmIfVptPnniAdminWeightsEntry": mscAtmIfVptPnniAdminWeightsEntry,
       "mscAtmIfVptPnniCbrWeight": mscAtmIfVptPnniCbrWeight,
       "mscAtmIfVptPnniRtVbrWeight": mscAtmIfVptPnniRtVbrWeight,
       "mscAtmIfVptPnniNrtVbrWeight": mscAtmIfVptPnniNrtVbrWeight,
       "mscAtmIfVptPnniUbrWeight": mscAtmIfVptPnniUbrWeight,
       "mscAtmIfVptPnniAcctOptTable": mscAtmIfVptPnniAcctOptTable,
       "mscAtmIfVptPnniAcctOptEntry": mscAtmIfVptPnniAcctOptEntry,
       "mscAtmIfVptPnniAccountCollection": mscAtmIfVptPnniAccountCollection,
       "mscAtmIfVptPnniAccountConnectionType": mscAtmIfVptPnniAccountConnectionType,
       "mscAtmIfVptPnniAccountClass": mscAtmIfVptPnniAccountClass,
       "mscAtmIfVptPnniServiceExchange": mscAtmIfVptPnniServiceExchange,
       "mscAtmIfVptPnniOperationalTable": mscAtmIfVptPnniOperationalTable,
       "mscAtmIfVptPnniOperationalEntry": mscAtmIfVptPnniOperationalEntry,
       "mscAtmIfVptPnniPortId": mscAtmIfVptPnniPortId,
       "mscAtmIfVptPnniVProvTable": mscAtmIfVptPnniVProvTable,
       "mscAtmIfVptPnniVProvEntry": mscAtmIfVptPnniVProvEntry,
       "mscAtmIfVptPnniVpci": mscAtmIfVptPnniVpci,
       "mscAtmIfPnni": mscAtmIfPnni,
       "mscAtmIfPnniRowStatusTable": mscAtmIfPnniRowStatusTable,
       "mscAtmIfPnniRowStatusEntry": mscAtmIfPnniRowStatusEntry,
       "mscAtmIfPnniRowStatus": mscAtmIfPnniRowStatus,
       "mscAtmIfPnniComponentName": mscAtmIfPnniComponentName,
       "mscAtmIfPnniStorageType": mscAtmIfPnniStorageType,
       "mscAtmIfPnniIndex": mscAtmIfPnniIndex,
       "mscAtmIfPnniSig": mscAtmIfPnniSig,
       "mscAtmIfPnniSigRowStatusTable": mscAtmIfPnniSigRowStatusTable,
       "mscAtmIfPnniSigRowStatusEntry": mscAtmIfPnniSigRowStatusEntry,
       "mscAtmIfPnniSigRowStatus": mscAtmIfPnniSigRowStatus,
       "mscAtmIfPnniSigComponentName": mscAtmIfPnniSigComponentName,
       "mscAtmIfPnniSigStorageType": mscAtmIfPnniSigStorageType,
       "mscAtmIfPnniSigIndex": mscAtmIfPnniSigIndex,
       "mscAtmIfPnniSigVcd": mscAtmIfPnniSigVcd,
       "mscAtmIfPnniSigVcdRowStatusTable": mscAtmIfPnniSigVcdRowStatusTable,
       "mscAtmIfPnniSigVcdRowStatusEntry": mscAtmIfPnniSigVcdRowStatusEntry,
       "mscAtmIfPnniSigVcdRowStatus": mscAtmIfPnniSigVcdRowStatus,
       "mscAtmIfPnniSigVcdComponentName": mscAtmIfPnniSigVcdComponentName,
       "mscAtmIfPnniSigVcdStorageType": mscAtmIfPnniSigVcdStorageType,
       "mscAtmIfPnniSigVcdIndex": mscAtmIfPnniSigVcdIndex,
       "mscAtmIfPnniSigVcdProvTable": mscAtmIfPnniSigVcdProvTable,
       "mscAtmIfPnniSigVcdProvEntry": mscAtmIfPnniSigVcdProvEntry,
       "mscAtmIfPnniSigVcdTrafficDescType": mscAtmIfPnniSigVcdTrafficDescType,
       "mscAtmIfPnniSigVcdAtmServiceCategory": mscAtmIfPnniSigVcdAtmServiceCategory,
       "mscAtmIfPnniSigVcdWeight": mscAtmIfPnniSigVcdWeight,
       "mscAtmIfPnniSigVcdQosClass": mscAtmIfPnniSigVcdQosClass,
       "mscAtmIfPnniSigVcdTrafficShaping": mscAtmIfPnniSigVcdTrafficShaping,
       "mscAtmIfPnniSigVcdUnshapedTransmitQueueing": mscAtmIfPnniSigVcdUnshapedTransmitQueueing,
       "mscAtmIfPnniSigVcdUsageParameterControl": mscAtmIfPnniSigVcdUsageParameterControl,
       "mscAtmIfPnniSigVcdTdpTable": mscAtmIfPnniSigVcdTdpTable,
       "mscAtmIfPnniSigVcdTdpEntry": mscAtmIfPnniSigVcdTdpEntry,
       "mscAtmIfPnniSigVcdTdpIndex": mscAtmIfPnniSigVcdTdpIndex,
       "mscAtmIfPnniSigVcdTdpValue": mscAtmIfPnniSigVcdTdpValue,
       "mscAtmIfPnniSigProvTable": mscAtmIfPnniSigProvTable,
       "mscAtmIfPnniSigProvEntry": mscAtmIfPnniSigProvEntry,
       "mscAtmIfPnniSigVci": mscAtmIfPnniSigVci,
       "mscAtmIfPnniSigAddressConversion": mscAtmIfPnniSigAddressConversion,
       "mscAtmIfPnniSigOperatingMode": mscAtmIfPnniSigOperatingMode,
       "mscAtmIfPnniSigStateTable": mscAtmIfPnniSigStateTable,
       "mscAtmIfPnniSigStateEntry": mscAtmIfPnniSigStateEntry,
       "mscAtmIfPnniSigAdminState": mscAtmIfPnniSigAdminState,
       "mscAtmIfPnniSigOperationalState": mscAtmIfPnniSigOperationalState,
       "mscAtmIfPnniSigUsageState": mscAtmIfPnniSigUsageState,
       "mscAtmIfPnniSigOperTable": mscAtmIfPnniSigOperTable,
       "mscAtmIfPnniSigOperEntry": mscAtmIfPnniSigOperEntry,
       "mscAtmIfPnniSigLastTxCauseCode": mscAtmIfPnniSigLastTxCauseCode,
       "mscAtmIfPnniSigLastTxDiagCode": mscAtmIfPnniSigLastTxDiagCode,
       "mscAtmIfPnniSigLastRxCauseCode": mscAtmIfPnniSigLastRxCauseCode,
       "mscAtmIfPnniSigLastRxDiagCode": mscAtmIfPnniSigLastRxDiagCode,
       "mscAtmIfPnniSigStatsTable": mscAtmIfPnniSigStatsTable,
       "mscAtmIfPnniSigStatsEntry": mscAtmIfPnniSigStatsEntry,
       "mscAtmIfPnniSigCurrentConnections": mscAtmIfPnniSigCurrentConnections,
       "mscAtmIfPnniSigPeakConnections": mscAtmIfPnniSigPeakConnections,
       "mscAtmIfPnniSigSuccessfulConnections": mscAtmIfPnniSigSuccessfulConnections,
       "mscAtmIfPnniSigFailedConnections": mscAtmIfPnniSigFailedConnections,
       "mscAtmIfPnniSigTxPdus": mscAtmIfPnniSigTxPdus,
       "mscAtmIfPnniSigRxPdus": mscAtmIfPnniSigRxPdus,
       "mscAtmIfPnniSigCurrentPmpConnections": mscAtmIfPnniSigCurrentPmpConnections,
       "mscAtmIfPnniSigPeakPmpConnections": mscAtmIfPnniSigPeakPmpConnections,
       "mscAtmIfPnniSigSuccessfulPmpConnections": mscAtmIfPnniSigSuccessfulPmpConnections,
       "mscAtmIfPnniSigFailedPmpConnections": mscAtmIfPnniSigFailedPmpConnections,
       "mscAtmIfPnniSigNewCurrentConnections": mscAtmIfPnniSigNewCurrentConnections,
       "mscAtmIfPnniRcc": mscAtmIfPnniRcc,
       "mscAtmIfPnniRccRowStatusTable": mscAtmIfPnniRccRowStatusTable,
       "mscAtmIfPnniRccRowStatusEntry": mscAtmIfPnniRccRowStatusEntry,
       "mscAtmIfPnniRccRowStatus": mscAtmIfPnniRccRowStatus,
       "mscAtmIfPnniRccComponentName": mscAtmIfPnniRccComponentName,
       "mscAtmIfPnniRccStorageType": mscAtmIfPnniRccStorageType,
       "mscAtmIfPnniRccIndex": mscAtmIfPnniRccIndex,
       "mscAtmIfPnniRccVcd": mscAtmIfPnniRccVcd,
       "mscAtmIfPnniRccVcdRowStatusTable": mscAtmIfPnniRccVcdRowStatusTable,
       "mscAtmIfPnniRccVcdRowStatusEntry": mscAtmIfPnniRccVcdRowStatusEntry,
       "mscAtmIfPnniRccVcdRowStatus": mscAtmIfPnniRccVcdRowStatus,
       "mscAtmIfPnniRccVcdComponentName": mscAtmIfPnniRccVcdComponentName,
       "mscAtmIfPnniRccVcdStorageType": mscAtmIfPnniRccVcdStorageType,
       "mscAtmIfPnniRccVcdIndex": mscAtmIfPnniRccVcdIndex,
       "mscAtmIfPnniRccVcdProvTable": mscAtmIfPnniRccVcdProvTable,
       "mscAtmIfPnniRccVcdProvEntry": mscAtmIfPnniRccVcdProvEntry,
       "mscAtmIfPnniRccVcdTrafficDescType": mscAtmIfPnniRccVcdTrafficDescType,
       "mscAtmIfPnniRccVcdAtmServiceCategory": mscAtmIfPnniRccVcdAtmServiceCategory,
       "mscAtmIfPnniRccVcdWeight": mscAtmIfPnniRccVcdWeight,
       "mscAtmIfPnniRccVcdQosClass": mscAtmIfPnniRccVcdQosClass,
       "mscAtmIfPnniRccVcdTrafficShaping": mscAtmIfPnniRccVcdTrafficShaping,
       "mscAtmIfPnniRccVcdUnshapedTransmitQueueing": mscAtmIfPnniRccVcdUnshapedTransmitQueueing,
       "mscAtmIfPnniRccVcdUsageParameterControl": mscAtmIfPnniRccVcdUsageParameterControl,
       "mscAtmIfPnniRccVcdTdpTable": mscAtmIfPnniRccVcdTdpTable,
       "mscAtmIfPnniRccVcdTdpEntry": mscAtmIfPnniRccVcdTdpEntry,
       "mscAtmIfPnniRccVcdTdpIndex": mscAtmIfPnniRccVcdTdpIndex,
       "mscAtmIfPnniRccVcdTdpValue": mscAtmIfPnniRccVcdTdpValue,
       "mscAtmIfPnniRccProvTable": mscAtmIfPnniRccProvTable,
       "mscAtmIfPnniRccProvEntry": mscAtmIfPnniRccProvEntry,
       "mscAtmIfPnniRccVci": mscAtmIfPnniRccVci,
       "mscAtmIfPnniRccHlParmsTable": mscAtmIfPnniRccHlParmsTable,
       "mscAtmIfPnniRccHlParmsEntry": mscAtmIfPnniRccHlParmsEntry,
       "mscAtmIfPnniRccHelloHoldDown": mscAtmIfPnniRccHelloHoldDown,
       "mscAtmIfPnniRccHelloInterval": mscAtmIfPnniRccHelloInterval,
       "mscAtmIfPnniRccHelloInactivityFactor": mscAtmIfPnniRccHelloInactivityFactor,
       "mscAtmIfPnniRccStateTable": mscAtmIfPnniRccStateTable,
       "mscAtmIfPnniRccStateEntry": mscAtmIfPnniRccStateEntry,
       "mscAtmIfPnniRccAdminState": mscAtmIfPnniRccAdminState,
       "mscAtmIfPnniRccOperationalState": mscAtmIfPnniRccOperationalState,
       "mscAtmIfPnniRccUsageState": mscAtmIfPnniRccUsageState,
       "mscAtmIfPnniRccOperTable": mscAtmIfPnniRccOperTable,
       "mscAtmIfPnniRccOperEntry": mscAtmIfPnniRccOperEntry,
       "mscAtmIfPnniRccType": mscAtmIfPnniRccType,
       "mscAtmIfPnniRccNegotiatedVersion": mscAtmIfPnniRccNegotiatedVersion,
       "mscAtmIfPnniRccHelloState": mscAtmIfPnniRccHelloState,
       "mscAtmIfPnniRccRemoteNodeId": mscAtmIfPnniRccRemoteNodeId,
       "mscAtmIfPnniRccRemotePortId": mscAtmIfPnniRccRemotePortId,
       "mscAtmIfPnniRccStatsTable": mscAtmIfPnniRccStatsTable,
       "mscAtmIfPnniRccStatsEntry": mscAtmIfPnniRccStatsEntry,
       "mscAtmIfPnniRccHelloPacketsRx": mscAtmIfPnniRccHelloPacketsRx,
       "mscAtmIfPnniRccHelloPacketsTx": mscAtmIfPnniRccHelloPacketsTx,
       "mscAtmIfPnniRccMismatchedHelloPacketsRx": mscAtmIfPnniRccMismatchedHelloPacketsRx,
       "mscAtmIfPnniRccBadHelloPacketsRx": mscAtmIfPnniRccBadHelloPacketsRx,
       "mscAtmIfPnniAddr": mscAtmIfPnniAddr,
       "mscAtmIfPnniAddrRowStatusTable": mscAtmIfPnniAddrRowStatusTable,
       "mscAtmIfPnniAddrRowStatusEntry": mscAtmIfPnniAddrRowStatusEntry,
       "mscAtmIfPnniAddrRowStatus": mscAtmIfPnniAddrRowStatus,
       "mscAtmIfPnniAddrComponentName": mscAtmIfPnniAddrComponentName,
       "mscAtmIfPnniAddrStorageType": mscAtmIfPnniAddrStorageType,
       "mscAtmIfPnniAddrAddressIndex": mscAtmIfPnniAddrAddressIndex,
       "mscAtmIfPnniAddrAddressTypeIndex": mscAtmIfPnniAddrAddressTypeIndex,
       "mscAtmIfPnniAddrTermSP": mscAtmIfPnniAddrTermSP,
       "mscAtmIfPnniAddrTermSPRowStatusTable": mscAtmIfPnniAddrTermSPRowStatusTable,
       "mscAtmIfPnniAddrTermSPRowStatusEntry": mscAtmIfPnniAddrTermSPRowStatusEntry,
       "mscAtmIfPnniAddrTermSPRowStatus": mscAtmIfPnniAddrTermSPRowStatus,
       "mscAtmIfPnniAddrTermSPComponentName": mscAtmIfPnniAddrTermSPComponentName,
       "mscAtmIfPnniAddrTermSPStorageType": mscAtmIfPnniAddrTermSPStorageType,
       "mscAtmIfPnniAddrTermSPIndex": mscAtmIfPnniAddrTermSPIndex,
       "mscAtmIfPnniAddrPnniInfo": mscAtmIfPnniAddrPnniInfo,
       "mscAtmIfPnniAddrPnniInfoRowStatusTable": mscAtmIfPnniAddrPnniInfoRowStatusTable,
       "mscAtmIfPnniAddrPnniInfoRowStatusEntry": mscAtmIfPnniAddrPnniInfoRowStatusEntry,
       "mscAtmIfPnniAddrPnniInfoRowStatus": mscAtmIfPnniAddrPnniInfoRowStatus,
       "mscAtmIfPnniAddrPnniInfoComponentName": mscAtmIfPnniAddrPnniInfoComponentName,
       "mscAtmIfPnniAddrPnniInfoStorageType": mscAtmIfPnniAddrPnniInfoStorageType,
       "mscAtmIfPnniAddrPnniInfoIndex": mscAtmIfPnniAddrPnniInfoIndex,
       "mscAtmIfPnniAddrPnniInfoProvTable": mscAtmIfPnniAddrPnniInfoProvTable,
       "mscAtmIfPnniAddrPnniInfoProvEntry": mscAtmIfPnniAddrPnniInfoProvEntry,
       "mscAtmIfPnniAddrPnniInfoScope": mscAtmIfPnniAddrPnniInfoScope,
       "mscAtmIfPnniAddrPnniInfoReachability": mscAtmIfPnniAddrPnniInfoReachability,
       "mscAtmIfPnniAddrOperTable": mscAtmIfPnniAddrOperTable,
       "mscAtmIfPnniAddrOperEntry": mscAtmIfPnniAddrOperEntry,
       "mscAtmIfPnniAddrScope": mscAtmIfPnniAddrScope,
       "mscAtmIfPnniAddrReachability": mscAtmIfPnniAddrReachability,
       "mscAtmIfPnniProvTable": mscAtmIfPnniProvTable,
       "mscAtmIfPnniProvEntry": mscAtmIfPnniProvEntry,
       "mscAtmIfPnniSoftPvcRetryPeriod": mscAtmIfPnniSoftPvcRetryPeriod,
       "mscAtmIfPnniSoftPvpAndPvcRetryPeriod": mscAtmIfPnniSoftPvpAndPvcRetryPeriod,
       "mscAtmIfPnniSoftPvpAndPvcHoldOffTime": mscAtmIfPnniSoftPvpAndPvcHoldOffTime,
       "mscAtmIfPnniAdminWeightsTable": mscAtmIfPnniAdminWeightsTable,
       "mscAtmIfPnniAdminWeightsEntry": mscAtmIfPnniAdminWeightsEntry,
       "mscAtmIfPnniCbrWeight": mscAtmIfPnniCbrWeight,
       "mscAtmIfPnniRtVbrWeight": mscAtmIfPnniRtVbrWeight,
       "mscAtmIfPnniNrtVbrWeight": mscAtmIfPnniNrtVbrWeight,
       "mscAtmIfPnniUbrWeight": mscAtmIfPnniUbrWeight,
       "mscAtmIfPnniAcctOptTable": mscAtmIfPnniAcctOptTable,
       "mscAtmIfPnniAcctOptEntry": mscAtmIfPnniAcctOptEntry,
       "mscAtmIfPnniAccountCollection": mscAtmIfPnniAccountCollection,
       "mscAtmIfPnniAccountConnectionType": mscAtmIfPnniAccountConnectionType,
       "mscAtmIfPnniAccountClass": mscAtmIfPnniAccountClass,
       "mscAtmIfPnniServiceExchange": mscAtmIfPnniServiceExchange,
       "mscAtmIfPnniOperationalTable": mscAtmIfPnniOperationalTable,
       "mscAtmIfPnniOperationalEntry": mscAtmIfPnniOperationalEntry,
       "mscAtmIfPnniPortId": mscAtmIfPnniPortId,
       "atmPnniMIB": atmPnniMIB,
       "atmPnniGroup": atmPnniGroup,
       "atmPnniGroupCA": atmPnniGroupCA,
       "atmPnniGroupCA02": atmPnniGroupCA02,
       "atmPnniGroupCA02A": atmPnniGroupCA02A,
       "atmPnniCapabilities": atmPnniCapabilities,
       "atmPnniCapabilitiesCA": atmPnniCapabilitiesCA,
       "atmPnniCapabilitiesCA02": atmPnniCapabilitiesCA02,
       "atmPnniCapabilitiesCA02A": atmPnniCapabilitiesCA02A}
)
