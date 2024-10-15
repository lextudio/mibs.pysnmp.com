# SNMP MIB module (Nortel-MsCarrier-MscPassport-AtmIispMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-MsCarrier-MscPassport-AtmIispMIB
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
 Hex,
 HexString,
 NonReplicated) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-TextualConventionsMIB",
    "AsciiStringIndex",
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

_MscAtmIfIisp_ObjectIdentity = ObjectIdentity
mscAtmIfIisp = _MscAtmIfIisp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7)
)
_MscAtmIfIispRowStatusTable_Object = MibTable
mscAtmIfIispRowStatusTable = _MscAtmIfIispRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 1)
)
if mibBuilder.loadTexts:
    mscAtmIfIispRowStatusTable.setStatus("mandatory")
_MscAtmIfIispRowStatusEntry_Object = MibTableRow
mscAtmIfIispRowStatusEntry = _MscAtmIfIispRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 1, 1)
)
mscAtmIfIispRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmIispMIB", "mscAtmIfIispIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfIispRowStatusEntry.setStatus("mandatory")
_MscAtmIfIispRowStatus_Type = RowStatus
_MscAtmIfIispRowStatus_Object = MibTableColumn
mscAtmIfIispRowStatus = _MscAtmIfIispRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 1, 1, 1),
    _MscAtmIfIispRowStatus_Type()
)
mscAtmIfIispRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfIispRowStatus.setStatus("mandatory")
_MscAtmIfIispComponentName_Type = DisplayString
_MscAtmIfIispComponentName_Object = MibTableColumn
mscAtmIfIispComponentName = _MscAtmIfIispComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 1, 1, 2),
    _MscAtmIfIispComponentName_Type()
)
mscAtmIfIispComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfIispComponentName.setStatus("mandatory")
_MscAtmIfIispStorageType_Type = StorageType
_MscAtmIfIispStorageType_Object = MibTableColumn
mscAtmIfIispStorageType = _MscAtmIfIispStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 1, 1, 4),
    _MscAtmIfIispStorageType_Type()
)
mscAtmIfIispStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfIispStorageType.setStatus("mandatory")
_MscAtmIfIispIndex_Type = NonReplicated
_MscAtmIfIispIndex_Object = MibTableColumn
mscAtmIfIispIndex = _MscAtmIfIispIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 1, 1, 10),
    _MscAtmIfIispIndex_Type()
)
mscAtmIfIispIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAtmIfIispIndex.setStatus("mandatory")
_MscAtmIfIispSig_ObjectIdentity = ObjectIdentity
mscAtmIfIispSig = _MscAtmIfIispSig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 3)
)
_MscAtmIfIispSigRowStatusTable_Object = MibTable
mscAtmIfIispSigRowStatusTable = _MscAtmIfIispSigRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 3, 1)
)
if mibBuilder.loadTexts:
    mscAtmIfIispSigRowStatusTable.setStatus("mandatory")
_MscAtmIfIispSigRowStatusEntry_Object = MibTableRow
mscAtmIfIispSigRowStatusEntry = _MscAtmIfIispSigRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 3, 1, 1)
)
mscAtmIfIispSigRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmIispMIB", "mscAtmIfIispIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmIispMIB", "mscAtmIfIispSigIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfIispSigRowStatusEntry.setStatus("mandatory")
_MscAtmIfIispSigRowStatus_Type = RowStatus
_MscAtmIfIispSigRowStatus_Object = MibTableColumn
mscAtmIfIispSigRowStatus = _MscAtmIfIispSigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 3, 1, 1, 1),
    _MscAtmIfIispSigRowStatus_Type()
)
mscAtmIfIispSigRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfIispSigRowStatus.setStatus("mandatory")
_MscAtmIfIispSigComponentName_Type = DisplayString
_MscAtmIfIispSigComponentName_Object = MibTableColumn
mscAtmIfIispSigComponentName = _MscAtmIfIispSigComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 3, 1, 1, 2),
    _MscAtmIfIispSigComponentName_Type()
)
mscAtmIfIispSigComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfIispSigComponentName.setStatus("mandatory")
_MscAtmIfIispSigStorageType_Type = StorageType
_MscAtmIfIispSigStorageType_Object = MibTableColumn
mscAtmIfIispSigStorageType = _MscAtmIfIispSigStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 3, 1, 1, 4),
    _MscAtmIfIispSigStorageType_Type()
)
mscAtmIfIispSigStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfIispSigStorageType.setStatus("mandatory")
_MscAtmIfIispSigIndex_Type = NonReplicated
_MscAtmIfIispSigIndex_Object = MibTableColumn
mscAtmIfIispSigIndex = _MscAtmIfIispSigIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 3, 1, 1, 10),
    _MscAtmIfIispSigIndex_Type()
)
mscAtmIfIispSigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAtmIfIispSigIndex.setStatus("mandatory")
_MscAtmIfIispSigVcd_ObjectIdentity = ObjectIdentity
mscAtmIfIispSigVcd = _MscAtmIfIispSigVcd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 3, 2)
)
_MscAtmIfIispSigVcdRowStatusTable_Object = MibTable
mscAtmIfIispSigVcdRowStatusTable = _MscAtmIfIispSigVcdRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 3, 2, 1)
)
if mibBuilder.loadTexts:
    mscAtmIfIispSigVcdRowStatusTable.setStatus("mandatory")
_MscAtmIfIispSigVcdRowStatusEntry_Object = MibTableRow
mscAtmIfIispSigVcdRowStatusEntry = _MscAtmIfIispSigVcdRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 3, 2, 1, 1)
)
mscAtmIfIispSigVcdRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmIispMIB", "mscAtmIfIispIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmIispMIB", "mscAtmIfIispSigIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmIispMIB", "mscAtmIfIispSigVcdIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfIispSigVcdRowStatusEntry.setStatus("mandatory")
_MscAtmIfIispSigVcdRowStatus_Type = RowStatus
_MscAtmIfIispSigVcdRowStatus_Object = MibTableColumn
mscAtmIfIispSigVcdRowStatus = _MscAtmIfIispSigVcdRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 3, 2, 1, 1, 1),
    _MscAtmIfIispSigVcdRowStatus_Type()
)
mscAtmIfIispSigVcdRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfIispSigVcdRowStatus.setStatus("mandatory")
_MscAtmIfIispSigVcdComponentName_Type = DisplayString
_MscAtmIfIispSigVcdComponentName_Object = MibTableColumn
mscAtmIfIispSigVcdComponentName = _MscAtmIfIispSigVcdComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 3, 2, 1, 1, 2),
    _MscAtmIfIispSigVcdComponentName_Type()
)
mscAtmIfIispSigVcdComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfIispSigVcdComponentName.setStatus("mandatory")
_MscAtmIfIispSigVcdStorageType_Type = StorageType
_MscAtmIfIispSigVcdStorageType_Object = MibTableColumn
mscAtmIfIispSigVcdStorageType = _MscAtmIfIispSigVcdStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 3, 2, 1, 1, 4),
    _MscAtmIfIispSigVcdStorageType_Type()
)
mscAtmIfIispSigVcdStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfIispSigVcdStorageType.setStatus("mandatory")
_MscAtmIfIispSigVcdIndex_Type = NonReplicated
_MscAtmIfIispSigVcdIndex_Object = MibTableColumn
mscAtmIfIispSigVcdIndex = _MscAtmIfIispSigVcdIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 3, 2, 1, 1, 10),
    _MscAtmIfIispSigVcdIndex_Type()
)
mscAtmIfIispSigVcdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAtmIfIispSigVcdIndex.setStatus("mandatory")
_MscAtmIfIispSigVcdProvTable_Object = MibTable
mscAtmIfIispSigVcdProvTable = _MscAtmIfIispSigVcdProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 3, 2, 10)
)
if mibBuilder.loadTexts:
    mscAtmIfIispSigVcdProvTable.setStatus("mandatory")
_MscAtmIfIispSigVcdProvEntry_Object = MibTableRow
mscAtmIfIispSigVcdProvEntry = _MscAtmIfIispSigVcdProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 3, 2, 10, 1)
)
mscAtmIfIispSigVcdProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmIispMIB", "mscAtmIfIispIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmIispMIB", "mscAtmIfIispSigIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmIispMIB", "mscAtmIfIispSigVcdIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfIispSigVcdProvEntry.setStatus("mandatory")


class _MscAtmIfIispSigVcdTrafficDescType_Type(Integer32):
    """Custom type mscAtmIfIispSigVcdTrafficDescType based on Integer32"""
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


_MscAtmIfIispSigVcdTrafficDescType_Type.__name__ = "Integer32"
_MscAtmIfIispSigVcdTrafficDescType_Object = MibTableColumn
mscAtmIfIispSigVcdTrafficDescType = _MscAtmIfIispSigVcdTrafficDescType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 3, 2, 10, 1, 1),
    _MscAtmIfIispSigVcdTrafficDescType_Type()
)
mscAtmIfIispSigVcdTrafficDescType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfIispSigVcdTrafficDescType.setStatus("mandatory")


class _MscAtmIfIispSigVcdAtmServiceCategory_Type(Integer32):
    """Custom type mscAtmIfIispSigVcdAtmServiceCategory based on Integer32"""
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


_MscAtmIfIispSigVcdAtmServiceCategory_Type.__name__ = "Integer32"
_MscAtmIfIispSigVcdAtmServiceCategory_Object = MibTableColumn
mscAtmIfIispSigVcdAtmServiceCategory = _MscAtmIfIispSigVcdAtmServiceCategory_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 3, 2, 10, 1, 3),
    _MscAtmIfIispSigVcdAtmServiceCategory_Type()
)
mscAtmIfIispSigVcdAtmServiceCategory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfIispSigVcdAtmServiceCategory.setStatus("mandatory")


class _MscAtmIfIispSigVcdWeight_Type(Unsigned32):
    """Custom type mscAtmIfIispSigVcdWeight based on Unsigned32"""
    defaultValue = 65535

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4095),
        ValueRangeConstraint(65535, 65535),
    )


_MscAtmIfIispSigVcdWeight_Type.__name__ = "Unsigned32"
_MscAtmIfIispSigVcdWeight_Object = MibTableColumn
mscAtmIfIispSigVcdWeight = _MscAtmIfIispSigVcdWeight_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 3, 2, 10, 1, 4),
    _MscAtmIfIispSigVcdWeight_Type()
)
mscAtmIfIispSigVcdWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfIispSigVcdWeight.setStatus("mandatory")


class _MscAtmIfIispSigVcdQosClass_Type(Integer32):
    """Custom type mscAtmIfIispSigVcdQosClass based on Integer32"""
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


_MscAtmIfIispSigVcdQosClass_Type.__name__ = "Integer32"
_MscAtmIfIispSigVcdQosClass_Object = MibTableColumn
mscAtmIfIispSigVcdQosClass = _MscAtmIfIispSigVcdQosClass_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 3, 2, 10, 1, 21),
    _MscAtmIfIispSigVcdQosClass_Type()
)
mscAtmIfIispSigVcdQosClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfIispSigVcdQosClass.setStatus("mandatory")


class _MscAtmIfIispSigVcdTrafficShaping_Type(Integer32):
    """Custom type mscAtmIfIispSigVcdTrafficShaping based on Integer32"""
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


_MscAtmIfIispSigVcdTrafficShaping_Type.__name__ = "Integer32"
_MscAtmIfIispSigVcdTrafficShaping_Object = MibTableColumn
mscAtmIfIispSigVcdTrafficShaping = _MscAtmIfIispSigVcdTrafficShaping_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 3, 2, 10, 1, 50),
    _MscAtmIfIispSigVcdTrafficShaping_Type()
)
mscAtmIfIispSigVcdTrafficShaping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfIispSigVcdTrafficShaping.setStatus("mandatory")


class _MscAtmIfIispSigVcdUnshapedTransmitQueueing_Type(Integer32):
    """Custom type mscAtmIfIispSigVcdUnshapedTransmitQueueing based on Integer32"""
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


_MscAtmIfIispSigVcdUnshapedTransmitQueueing_Type.__name__ = "Integer32"
_MscAtmIfIispSigVcdUnshapedTransmitQueueing_Object = MibTableColumn
mscAtmIfIispSigVcdUnshapedTransmitQueueing = _MscAtmIfIispSigVcdUnshapedTransmitQueueing_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 3, 2, 10, 1, 60),
    _MscAtmIfIispSigVcdUnshapedTransmitQueueing_Type()
)
mscAtmIfIispSigVcdUnshapedTransmitQueueing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfIispSigVcdUnshapedTransmitQueueing.setStatus("mandatory")


class _MscAtmIfIispSigVcdUsageParameterControl_Type(Integer32):
    """Custom type mscAtmIfIispSigVcdUsageParameterControl based on Integer32"""
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


_MscAtmIfIispSigVcdUsageParameterControl_Type.__name__ = "Integer32"
_MscAtmIfIispSigVcdUsageParameterControl_Object = MibTableColumn
mscAtmIfIispSigVcdUsageParameterControl = _MscAtmIfIispSigVcdUsageParameterControl_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 3, 2, 10, 1, 70),
    _MscAtmIfIispSigVcdUsageParameterControl_Type()
)
mscAtmIfIispSigVcdUsageParameterControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfIispSigVcdUsageParameterControl.setStatus("mandatory")
_MscAtmIfIispSigVcdTdpTable_Object = MibTable
mscAtmIfIispSigVcdTdpTable = _MscAtmIfIispSigVcdTdpTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 3, 2, 387)
)
if mibBuilder.loadTexts:
    mscAtmIfIispSigVcdTdpTable.setStatus("mandatory")
_MscAtmIfIispSigVcdTdpEntry_Object = MibTableRow
mscAtmIfIispSigVcdTdpEntry = _MscAtmIfIispSigVcdTdpEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 3, 2, 387, 1)
)
mscAtmIfIispSigVcdTdpEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmIispMIB", "mscAtmIfIispIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmIispMIB", "mscAtmIfIispSigIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmIispMIB", "mscAtmIfIispSigVcdIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmIispMIB", "mscAtmIfIispSigVcdTdpIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfIispSigVcdTdpEntry.setStatus("mandatory")


class _MscAtmIfIispSigVcdTdpIndex_Type(Integer32):
    """Custom type mscAtmIfIispSigVcdTdpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_MscAtmIfIispSigVcdTdpIndex_Type.__name__ = "Integer32"
_MscAtmIfIispSigVcdTdpIndex_Object = MibTableColumn
mscAtmIfIispSigVcdTdpIndex = _MscAtmIfIispSigVcdTdpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 3, 2, 387, 1, 1),
    _MscAtmIfIispSigVcdTdpIndex_Type()
)
mscAtmIfIispSigVcdTdpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAtmIfIispSigVcdTdpIndex.setStatus("mandatory")


class _MscAtmIfIispSigVcdTdpValue_Type(Unsigned32):
    """Custom type mscAtmIfIispSigVcdTdpValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MscAtmIfIispSigVcdTdpValue_Type.__name__ = "Unsigned32"
_MscAtmIfIispSigVcdTdpValue_Object = MibTableColumn
mscAtmIfIispSigVcdTdpValue = _MscAtmIfIispSigVcdTdpValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 3, 2, 387, 1, 2),
    _MscAtmIfIispSigVcdTdpValue_Type()
)
mscAtmIfIispSigVcdTdpValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfIispSigVcdTdpValue.setStatus("mandatory")
_MscAtmIfIispSigProvTable_Object = MibTable
mscAtmIfIispSigProvTable = _MscAtmIfIispSigProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 3, 10)
)
if mibBuilder.loadTexts:
    mscAtmIfIispSigProvTable.setStatus("mandatory")
_MscAtmIfIispSigProvEntry_Object = MibTableRow
mscAtmIfIispSigProvEntry = _MscAtmIfIispSigProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 3, 10, 1)
)
mscAtmIfIispSigProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmIispMIB", "mscAtmIfIispIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmIispMIB", "mscAtmIfIispSigIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfIispSigProvEntry.setStatus("mandatory")


class _MscAtmIfIispSigVci_Type(Unsigned32):
    """Custom type mscAtmIfIispSigVci based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscAtmIfIispSigVci_Type.__name__ = "Unsigned32"
_MscAtmIfIispSigVci_Object = MibTableColumn
mscAtmIfIispSigVci = _MscAtmIfIispSigVci_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 3, 10, 1, 1),
    _MscAtmIfIispSigVci_Type()
)
mscAtmIfIispSigVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfIispSigVci.setStatus("mandatory")


class _MscAtmIfIispSigAddressConversion_Type(Integer32):
    """Custom type mscAtmIfIispSigAddressConversion based on Integer32"""
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


_MscAtmIfIispSigAddressConversion_Type.__name__ = "Integer32"
_MscAtmIfIispSigAddressConversion_Object = MibTableColumn
mscAtmIfIispSigAddressConversion = _MscAtmIfIispSigAddressConversion_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 3, 10, 1, 2),
    _MscAtmIfIispSigAddressConversion_Type()
)
mscAtmIfIispSigAddressConversion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfIispSigAddressConversion.setStatus("mandatory")


class _MscAtmIfIispSigOperatingMode_Type(Integer32):
    """Custom type mscAtmIfIispSigOperatingMode based on Integer32"""
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


_MscAtmIfIispSigOperatingMode_Type.__name__ = "Integer32"
_MscAtmIfIispSigOperatingMode_Object = MibTableColumn
mscAtmIfIispSigOperatingMode = _MscAtmIfIispSigOperatingMode_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 3, 10, 1, 3),
    _MscAtmIfIispSigOperatingMode_Type()
)
mscAtmIfIispSigOperatingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfIispSigOperatingMode.setStatus("mandatory")
_MscAtmIfIispSigStateTable_Object = MibTable
mscAtmIfIispSigStateTable = _MscAtmIfIispSigStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 3, 11)
)
if mibBuilder.loadTexts:
    mscAtmIfIispSigStateTable.setStatus("mandatory")
_MscAtmIfIispSigStateEntry_Object = MibTableRow
mscAtmIfIispSigStateEntry = _MscAtmIfIispSigStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 3, 11, 1)
)
mscAtmIfIispSigStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmIispMIB", "mscAtmIfIispIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmIispMIB", "mscAtmIfIispSigIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfIispSigStateEntry.setStatus("mandatory")


class _MscAtmIfIispSigAdminState_Type(Integer32):
    """Custom type mscAtmIfIispSigAdminState based on Integer32"""
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


_MscAtmIfIispSigAdminState_Type.__name__ = "Integer32"
_MscAtmIfIispSigAdminState_Object = MibTableColumn
mscAtmIfIispSigAdminState = _MscAtmIfIispSigAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 3, 11, 1, 1),
    _MscAtmIfIispSigAdminState_Type()
)
mscAtmIfIispSigAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfIispSigAdminState.setStatus("mandatory")


class _MscAtmIfIispSigOperationalState_Type(Integer32):
    """Custom type mscAtmIfIispSigOperationalState based on Integer32"""
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


_MscAtmIfIispSigOperationalState_Type.__name__ = "Integer32"
_MscAtmIfIispSigOperationalState_Object = MibTableColumn
mscAtmIfIispSigOperationalState = _MscAtmIfIispSigOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 3, 11, 1, 2),
    _MscAtmIfIispSigOperationalState_Type()
)
mscAtmIfIispSigOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfIispSigOperationalState.setStatus("mandatory")


class _MscAtmIfIispSigUsageState_Type(Integer32):
    """Custom type mscAtmIfIispSigUsageState based on Integer32"""
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


_MscAtmIfIispSigUsageState_Type.__name__ = "Integer32"
_MscAtmIfIispSigUsageState_Object = MibTableColumn
mscAtmIfIispSigUsageState = _MscAtmIfIispSigUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 3, 11, 1, 3),
    _MscAtmIfIispSigUsageState_Type()
)
mscAtmIfIispSigUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfIispSigUsageState.setStatus("mandatory")
_MscAtmIfIispSigOperTable_Object = MibTable
mscAtmIfIispSigOperTable = _MscAtmIfIispSigOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 3, 12)
)
if mibBuilder.loadTexts:
    mscAtmIfIispSigOperTable.setStatus("mandatory")
_MscAtmIfIispSigOperEntry_Object = MibTableRow
mscAtmIfIispSigOperEntry = _MscAtmIfIispSigOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 3, 12, 1)
)
mscAtmIfIispSigOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmIispMIB", "mscAtmIfIispIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmIispMIB", "mscAtmIfIispSigIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfIispSigOperEntry.setStatus("mandatory")


class _MscAtmIfIispSigLastTxCauseCode_Type(Unsigned32):
    """Custom type mscAtmIfIispSigLastTxCauseCode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscAtmIfIispSigLastTxCauseCode_Type.__name__ = "Unsigned32"
_MscAtmIfIispSigLastTxCauseCode_Object = MibTableColumn
mscAtmIfIispSigLastTxCauseCode = _MscAtmIfIispSigLastTxCauseCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 3, 12, 1, 1),
    _MscAtmIfIispSigLastTxCauseCode_Type()
)
mscAtmIfIispSigLastTxCauseCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfIispSigLastTxCauseCode.setStatus("mandatory")


class _MscAtmIfIispSigLastTxDiagCode_Type(Hex):
    """Custom type mscAtmIfIispSigLastTxDiagCode based on Hex"""
    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscAtmIfIispSigLastTxDiagCode_Type.__name__ = "Hex"
_MscAtmIfIispSigLastTxDiagCode_Object = MibTableColumn
mscAtmIfIispSigLastTxDiagCode = _MscAtmIfIispSigLastTxDiagCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 3, 12, 1, 2),
    _MscAtmIfIispSigLastTxDiagCode_Type()
)
mscAtmIfIispSigLastTxDiagCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfIispSigLastTxDiagCode.setStatus("mandatory")


class _MscAtmIfIispSigLastRxCauseCode_Type(Unsigned32):
    """Custom type mscAtmIfIispSigLastRxCauseCode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscAtmIfIispSigLastRxCauseCode_Type.__name__ = "Unsigned32"
_MscAtmIfIispSigLastRxCauseCode_Object = MibTableColumn
mscAtmIfIispSigLastRxCauseCode = _MscAtmIfIispSigLastRxCauseCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 3, 12, 1, 3),
    _MscAtmIfIispSigLastRxCauseCode_Type()
)
mscAtmIfIispSigLastRxCauseCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfIispSigLastRxCauseCode.setStatus("mandatory")


class _MscAtmIfIispSigLastRxDiagCode_Type(Hex):
    """Custom type mscAtmIfIispSigLastRxDiagCode based on Hex"""
    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscAtmIfIispSigLastRxDiagCode_Type.__name__ = "Hex"
_MscAtmIfIispSigLastRxDiagCode_Object = MibTableColumn
mscAtmIfIispSigLastRxDiagCode = _MscAtmIfIispSigLastRxDiagCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 3, 12, 1, 4),
    _MscAtmIfIispSigLastRxDiagCode_Type()
)
mscAtmIfIispSigLastRxDiagCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfIispSigLastRxDiagCode.setStatus("mandatory")
_MscAtmIfIispSigStatsTable_Object = MibTable
mscAtmIfIispSigStatsTable = _MscAtmIfIispSigStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 3, 13)
)
if mibBuilder.loadTexts:
    mscAtmIfIispSigStatsTable.setStatus("mandatory")
_MscAtmIfIispSigStatsEntry_Object = MibTableRow
mscAtmIfIispSigStatsEntry = _MscAtmIfIispSigStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 3, 13, 1)
)
mscAtmIfIispSigStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmIispMIB", "mscAtmIfIispIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmIispMIB", "mscAtmIfIispSigIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfIispSigStatsEntry.setStatus("mandatory")
_MscAtmIfIispSigCurrentConnections_Type = Counter32
_MscAtmIfIispSigCurrentConnections_Object = MibTableColumn
mscAtmIfIispSigCurrentConnections = _MscAtmIfIispSigCurrentConnections_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 3, 13, 1, 1),
    _MscAtmIfIispSigCurrentConnections_Type()
)
mscAtmIfIispSigCurrentConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfIispSigCurrentConnections.setStatus("obsolete")


class _MscAtmIfIispSigPeakConnections_Type(Gauge32):
    """Custom type mscAtmIfIispSigPeakConnections based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscAtmIfIispSigPeakConnections_Type.__name__ = "Gauge32"
_MscAtmIfIispSigPeakConnections_Object = MibTableColumn
mscAtmIfIispSigPeakConnections = _MscAtmIfIispSigPeakConnections_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 3, 13, 1, 2),
    _MscAtmIfIispSigPeakConnections_Type()
)
mscAtmIfIispSigPeakConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfIispSigPeakConnections.setStatus("mandatory")
_MscAtmIfIispSigSuccessfulConnections_Type = Counter32
_MscAtmIfIispSigSuccessfulConnections_Object = MibTableColumn
mscAtmIfIispSigSuccessfulConnections = _MscAtmIfIispSigSuccessfulConnections_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 3, 13, 1, 3),
    _MscAtmIfIispSigSuccessfulConnections_Type()
)
mscAtmIfIispSigSuccessfulConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfIispSigSuccessfulConnections.setStatus("mandatory")
_MscAtmIfIispSigFailedConnections_Type = Counter32
_MscAtmIfIispSigFailedConnections_Object = MibTableColumn
mscAtmIfIispSigFailedConnections = _MscAtmIfIispSigFailedConnections_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 3, 13, 1, 4),
    _MscAtmIfIispSigFailedConnections_Type()
)
mscAtmIfIispSigFailedConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfIispSigFailedConnections.setStatus("mandatory")
_MscAtmIfIispSigTxPdus_Type = Counter32
_MscAtmIfIispSigTxPdus_Object = MibTableColumn
mscAtmIfIispSigTxPdus = _MscAtmIfIispSigTxPdus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 3, 13, 1, 5),
    _MscAtmIfIispSigTxPdus_Type()
)
mscAtmIfIispSigTxPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfIispSigTxPdus.setStatus("mandatory")
_MscAtmIfIispSigRxPdus_Type = Counter32
_MscAtmIfIispSigRxPdus_Object = MibTableColumn
mscAtmIfIispSigRxPdus = _MscAtmIfIispSigRxPdus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 3, 13, 1, 6),
    _MscAtmIfIispSigRxPdus_Type()
)
mscAtmIfIispSigRxPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfIispSigRxPdus.setStatus("mandatory")


class _MscAtmIfIispSigCurrentPmpConnections_Type(Gauge32):
    """Custom type mscAtmIfIispSigCurrentPmpConnections based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscAtmIfIispSigCurrentPmpConnections_Type.__name__ = "Gauge32"
_MscAtmIfIispSigCurrentPmpConnections_Object = MibTableColumn
mscAtmIfIispSigCurrentPmpConnections = _MscAtmIfIispSigCurrentPmpConnections_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 3, 13, 1, 7),
    _MscAtmIfIispSigCurrentPmpConnections_Type()
)
mscAtmIfIispSigCurrentPmpConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfIispSigCurrentPmpConnections.setStatus("mandatory")


class _MscAtmIfIispSigPeakPmpConnections_Type(Gauge32):
    """Custom type mscAtmIfIispSigPeakPmpConnections based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscAtmIfIispSigPeakPmpConnections_Type.__name__ = "Gauge32"
_MscAtmIfIispSigPeakPmpConnections_Object = MibTableColumn
mscAtmIfIispSigPeakPmpConnections = _MscAtmIfIispSigPeakPmpConnections_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 3, 13, 1, 8),
    _MscAtmIfIispSigPeakPmpConnections_Type()
)
mscAtmIfIispSigPeakPmpConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfIispSigPeakPmpConnections.setStatus("mandatory")
_MscAtmIfIispSigSuccessfulPmpConnections_Type = Counter32
_MscAtmIfIispSigSuccessfulPmpConnections_Object = MibTableColumn
mscAtmIfIispSigSuccessfulPmpConnections = _MscAtmIfIispSigSuccessfulPmpConnections_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 3, 13, 1, 9),
    _MscAtmIfIispSigSuccessfulPmpConnections_Type()
)
mscAtmIfIispSigSuccessfulPmpConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfIispSigSuccessfulPmpConnections.setStatus("mandatory")
_MscAtmIfIispSigFailedPmpConnections_Type = Counter32
_MscAtmIfIispSigFailedPmpConnections_Object = MibTableColumn
mscAtmIfIispSigFailedPmpConnections = _MscAtmIfIispSigFailedPmpConnections_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 3, 13, 1, 10),
    _MscAtmIfIispSigFailedPmpConnections_Type()
)
mscAtmIfIispSigFailedPmpConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfIispSigFailedPmpConnections.setStatus("mandatory")


class _MscAtmIfIispSigNewCurrentConnections_Type(Gauge32):
    """Custom type mscAtmIfIispSigNewCurrentConnections based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscAtmIfIispSigNewCurrentConnections_Type.__name__ = "Gauge32"
_MscAtmIfIispSigNewCurrentConnections_Object = MibTableColumn
mscAtmIfIispSigNewCurrentConnections = _MscAtmIfIispSigNewCurrentConnections_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 3, 13, 1, 11),
    _MscAtmIfIispSigNewCurrentConnections_Type()
)
mscAtmIfIispSigNewCurrentConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfIispSigNewCurrentConnections.setStatus("mandatory")
_MscAtmIfIispAddr_ObjectIdentity = ObjectIdentity
mscAtmIfIispAddr = _MscAtmIfIispAddr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 4)
)
_MscAtmIfIispAddrRowStatusTable_Object = MibTable
mscAtmIfIispAddrRowStatusTable = _MscAtmIfIispAddrRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 4, 1)
)
if mibBuilder.loadTexts:
    mscAtmIfIispAddrRowStatusTable.setStatus("mandatory")
_MscAtmIfIispAddrRowStatusEntry_Object = MibTableRow
mscAtmIfIispAddrRowStatusEntry = _MscAtmIfIispAddrRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 4, 1, 1)
)
mscAtmIfIispAddrRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmIispMIB", "mscAtmIfIispIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmIispMIB", "mscAtmIfIispAddrAddressIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmIispMIB", "mscAtmIfIispAddrAddressTypeIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfIispAddrRowStatusEntry.setStatus("mandatory")
_MscAtmIfIispAddrRowStatus_Type = RowStatus
_MscAtmIfIispAddrRowStatus_Object = MibTableColumn
mscAtmIfIispAddrRowStatus = _MscAtmIfIispAddrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 4, 1, 1, 1),
    _MscAtmIfIispAddrRowStatus_Type()
)
mscAtmIfIispAddrRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfIispAddrRowStatus.setStatus("mandatory")
_MscAtmIfIispAddrComponentName_Type = DisplayString
_MscAtmIfIispAddrComponentName_Object = MibTableColumn
mscAtmIfIispAddrComponentName = _MscAtmIfIispAddrComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 4, 1, 1, 2),
    _MscAtmIfIispAddrComponentName_Type()
)
mscAtmIfIispAddrComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfIispAddrComponentName.setStatus("mandatory")
_MscAtmIfIispAddrStorageType_Type = StorageType
_MscAtmIfIispAddrStorageType_Object = MibTableColumn
mscAtmIfIispAddrStorageType = _MscAtmIfIispAddrStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 4, 1, 1, 4),
    _MscAtmIfIispAddrStorageType_Type()
)
mscAtmIfIispAddrStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfIispAddrStorageType.setStatus("mandatory")


class _MscAtmIfIispAddrAddressIndex_Type(AsciiStringIndex):
    """Custom type mscAtmIfIispAddrAddressIndex based on AsciiStringIndex"""
    subtypeSpec = AsciiStringIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_MscAtmIfIispAddrAddressIndex_Type.__name__ = "AsciiStringIndex"
_MscAtmIfIispAddrAddressIndex_Object = MibTableColumn
mscAtmIfIispAddrAddressIndex = _MscAtmIfIispAddrAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 4, 1, 1, 10),
    _MscAtmIfIispAddrAddressIndex_Type()
)
mscAtmIfIispAddrAddressIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAtmIfIispAddrAddressIndex.setStatus("mandatory")


class _MscAtmIfIispAddrAddressTypeIndex_Type(Integer32):
    """Custom type mscAtmIfIispAddrAddressTypeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("alternate", 1),
          ("default", 3),
          ("primary", 0))
    )


_MscAtmIfIispAddrAddressTypeIndex_Type.__name__ = "Integer32"
_MscAtmIfIispAddrAddressTypeIndex_Object = MibTableColumn
mscAtmIfIispAddrAddressTypeIndex = _MscAtmIfIispAddrAddressTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 4, 1, 1, 11),
    _MscAtmIfIispAddrAddressTypeIndex_Type()
)
mscAtmIfIispAddrAddressTypeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAtmIfIispAddrAddressTypeIndex.setStatus("mandatory")
_MscAtmIfIispAddrTermSP_ObjectIdentity = ObjectIdentity
mscAtmIfIispAddrTermSP = _MscAtmIfIispAddrTermSP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 4, 2)
)
_MscAtmIfIispAddrTermSPRowStatusTable_Object = MibTable
mscAtmIfIispAddrTermSPRowStatusTable = _MscAtmIfIispAddrTermSPRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 4, 2, 1)
)
if mibBuilder.loadTexts:
    mscAtmIfIispAddrTermSPRowStatusTable.setStatus("mandatory")
_MscAtmIfIispAddrTermSPRowStatusEntry_Object = MibTableRow
mscAtmIfIispAddrTermSPRowStatusEntry = _MscAtmIfIispAddrTermSPRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 4, 2, 1, 1)
)
mscAtmIfIispAddrTermSPRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmIispMIB", "mscAtmIfIispIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmIispMIB", "mscAtmIfIispAddrAddressIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmIispMIB", "mscAtmIfIispAddrAddressTypeIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmIispMIB", "mscAtmIfIispAddrTermSPIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfIispAddrTermSPRowStatusEntry.setStatus("mandatory")
_MscAtmIfIispAddrTermSPRowStatus_Type = RowStatus
_MscAtmIfIispAddrTermSPRowStatus_Object = MibTableColumn
mscAtmIfIispAddrTermSPRowStatus = _MscAtmIfIispAddrTermSPRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 4, 2, 1, 1, 1),
    _MscAtmIfIispAddrTermSPRowStatus_Type()
)
mscAtmIfIispAddrTermSPRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfIispAddrTermSPRowStatus.setStatus("mandatory")
_MscAtmIfIispAddrTermSPComponentName_Type = DisplayString
_MscAtmIfIispAddrTermSPComponentName_Object = MibTableColumn
mscAtmIfIispAddrTermSPComponentName = _MscAtmIfIispAddrTermSPComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 4, 2, 1, 1, 2),
    _MscAtmIfIispAddrTermSPComponentName_Type()
)
mscAtmIfIispAddrTermSPComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfIispAddrTermSPComponentName.setStatus("mandatory")
_MscAtmIfIispAddrTermSPStorageType_Type = StorageType
_MscAtmIfIispAddrTermSPStorageType_Object = MibTableColumn
mscAtmIfIispAddrTermSPStorageType = _MscAtmIfIispAddrTermSPStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 4, 2, 1, 1, 4),
    _MscAtmIfIispAddrTermSPStorageType_Type()
)
mscAtmIfIispAddrTermSPStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfIispAddrTermSPStorageType.setStatus("mandatory")
_MscAtmIfIispAddrTermSPIndex_Type = NonReplicated
_MscAtmIfIispAddrTermSPIndex_Object = MibTableColumn
mscAtmIfIispAddrTermSPIndex = _MscAtmIfIispAddrTermSPIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 4, 2, 1, 1, 10),
    _MscAtmIfIispAddrTermSPIndex_Type()
)
mscAtmIfIispAddrTermSPIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAtmIfIispAddrTermSPIndex.setStatus("mandatory")
_MscAtmIfIispAddrPnniInfo_ObjectIdentity = ObjectIdentity
mscAtmIfIispAddrPnniInfo = _MscAtmIfIispAddrPnniInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 4, 3)
)
_MscAtmIfIispAddrPnniInfoRowStatusTable_Object = MibTable
mscAtmIfIispAddrPnniInfoRowStatusTable = _MscAtmIfIispAddrPnniInfoRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 4, 3, 1)
)
if mibBuilder.loadTexts:
    mscAtmIfIispAddrPnniInfoRowStatusTable.setStatus("mandatory")
_MscAtmIfIispAddrPnniInfoRowStatusEntry_Object = MibTableRow
mscAtmIfIispAddrPnniInfoRowStatusEntry = _MscAtmIfIispAddrPnniInfoRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 4, 3, 1, 1)
)
mscAtmIfIispAddrPnniInfoRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmIispMIB", "mscAtmIfIispIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmIispMIB", "mscAtmIfIispAddrAddressIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmIispMIB", "mscAtmIfIispAddrAddressTypeIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmIispMIB", "mscAtmIfIispAddrPnniInfoIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfIispAddrPnniInfoRowStatusEntry.setStatus("mandatory")
_MscAtmIfIispAddrPnniInfoRowStatus_Type = RowStatus
_MscAtmIfIispAddrPnniInfoRowStatus_Object = MibTableColumn
mscAtmIfIispAddrPnniInfoRowStatus = _MscAtmIfIispAddrPnniInfoRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 4, 3, 1, 1, 1),
    _MscAtmIfIispAddrPnniInfoRowStatus_Type()
)
mscAtmIfIispAddrPnniInfoRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfIispAddrPnniInfoRowStatus.setStatus("mandatory")
_MscAtmIfIispAddrPnniInfoComponentName_Type = DisplayString
_MscAtmIfIispAddrPnniInfoComponentName_Object = MibTableColumn
mscAtmIfIispAddrPnniInfoComponentName = _MscAtmIfIispAddrPnniInfoComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 4, 3, 1, 1, 2),
    _MscAtmIfIispAddrPnniInfoComponentName_Type()
)
mscAtmIfIispAddrPnniInfoComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfIispAddrPnniInfoComponentName.setStatus("mandatory")
_MscAtmIfIispAddrPnniInfoStorageType_Type = StorageType
_MscAtmIfIispAddrPnniInfoStorageType_Object = MibTableColumn
mscAtmIfIispAddrPnniInfoStorageType = _MscAtmIfIispAddrPnniInfoStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 4, 3, 1, 1, 4),
    _MscAtmIfIispAddrPnniInfoStorageType_Type()
)
mscAtmIfIispAddrPnniInfoStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfIispAddrPnniInfoStorageType.setStatus("mandatory")
_MscAtmIfIispAddrPnniInfoIndex_Type = NonReplicated
_MscAtmIfIispAddrPnniInfoIndex_Object = MibTableColumn
mscAtmIfIispAddrPnniInfoIndex = _MscAtmIfIispAddrPnniInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 4, 3, 1, 1, 10),
    _MscAtmIfIispAddrPnniInfoIndex_Type()
)
mscAtmIfIispAddrPnniInfoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAtmIfIispAddrPnniInfoIndex.setStatus("mandatory")
_MscAtmIfIispAddrPnniInfoProvTable_Object = MibTable
mscAtmIfIispAddrPnniInfoProvTable = _MscAtmIfIispAddrPnniInfoProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 4, 3, 10)
)
if mibBuilder.loadTexts:
    mscAtmIfIispAddrPnniInfoProvTable.setStatus("mandatory")
_MscAtmIfIispAddrPnniInfoProvEntry_Object = MibTableRow
mscAtmIfIispAddrPnniInfoProvEntry = _MscAtmIfIispAddrPnniInfoProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 4, 3, 10, 1)
)
mscAtmIfIispAddrPnniInfoProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmIispMIB", "mscAtmIfIispIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmIispMIB", "mscAtmIfIispAddrAddressIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmIispMIB", "mscAtmIfIispAddrAddressTypeIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmIispMIB", "mscAtmIfIispAddrPnniInfoIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfIispAddrPnniInfoProvEntry.setStatus("mandatory")


class _MscAtmIfIispAddrPnniInfoScope_Type(Integer32):
    """Custom type mscAtmIfIispAddrPnniInfoScope based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 104),
    )


_MscAtmIfIispAddrPnniInfoScope_Type.__name__ = "Integer32"
_MscAtmIfIispAddrPnniInfoScope_Object = MibTableColumn
mscAtmIfIispAddrPnniInfoScope = _MscAtmIfIispAddrPnniInfoScope_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 4, 3, 10, 1, 1),
    _MscAtmIfIispAddrPnniInfoScope_Type()
)
mscAtmIfIispAddrPnniInfoScope.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfIispAddrPnniInfoScope.setStatus("mandatory")


class _MscAtmIfIispAddrPnniInfoReachability_Type(Integer32):
    """Custom type mscAtmIfIispAddrPnniInfoReachability based on Integer32"""
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


_MscAtmIfIispAddrPnniInfoReachability_Type.__name__ = "Integer32"
_MscAtmIfIispAddrPnniInfoReachability_Object = MibTableColumn
mscAtmIfIispAddrPnniInfoReachability = _MscAtmIfIispAddrPnniInfoReachability_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 4, 3, 10, 1, 2),
    _MscAtmIfIispAddrPnniInfoReachability_Type()
)
mscAtmIfIispAddrPnniInfoReachability.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfIispAddrPnniInfoReachability.setStatus("mandatory")
_MscAtmIfIispAddrOperTable_Object = MibTable
mscAtmIfIispAddrOperTable = _MscAtmIfIispAddrOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 4, 10)
)
if mibBuilder.loadTexts:
    mscAtmIfIispAddrOperTable.setStatus("mandatory")
_MscAtmIfIispAddrOperEntry_Object = MibTableRow
mscAtmIfIispAddrOperEntry = _MscAtmIfIispAddrOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 4, 10, 1)
)
mscAtmIfIispAddrOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmIispMIB", "mscAtmIfIispIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmIispMIB", "mscAtmIfIispAddrAddressIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmIispMIB", "mscAtmIfIispAddrAddressTypeIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfIispAddrOperEntry.setStatus("mandatory")


class _MscAtmIfIispAddrScope_Type(Integer32):
    """Custom type mscAtmIfIispAddrScope based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 104),
    )


_MscAtmIfIispAddrScope_Type.__name__ = "Integer32"
_MscAtmIfIispAddrScope_Object = MibTableColumn
mscAtmIfIispAddrScope = _MscAtmIfIispAddrScope_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 4, 10, 1, 1),
    _MscAtmIfIispAddrScope_Type()
)
mscAtmIfIispAddrScope.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfIispAddrScope.setStatus("mandatory")


class _MscAtmIfIispAddrReachability_Type(Integer32):
    """Custom type mscAtmIfIispAddrReachability based on Integer32"""
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


_MscAtmIfIispAddrReachability_Type.__name__ = "Integer32"
_MscAtmIfIispAddrReachability_Object = MibTableColumn
mscAtmIfIispAddrReachability = _MscAtmIfIispAddrReachability_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 4, 10, 1, 2),
    _MscAtmIfIispAddrReachability_Type()
)
mscAtmIfIispAddrReachability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfIispAddrReachability.setStatus("mandatory")
_MscAtmIfIispCallingAScr_ObjectIdentity = ObjectIdentity
mscAtmIfIispCallingAScr = _MscAtmIfIispCallingAScr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 5)
)
_MscAtmIfIispCallingAScrRowStatusTable_Object = MibTable
mscAtmIfIispCallingAScrRowStatusTable = _MscAtmIfIispCallingAScrRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 5, 1)
)
if mibBuilder.loadTexts:
    mscAtmIfIispCallingAScrRowStatusTable.setStatus("mandatory")
_MscAtmIfIispCallingAScrRowStatusEntry_Object = MibTableRow
mscAtmIfIispCallingAScrRowStatusEntry = _MscAtmIfIispCallingAScrRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 5, 1, 1)
)
mscAtmIfIispCallingAScrRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmIispMIB", "mscAtmIfIispIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmIispMIB", "mscAtmIfIispCallingAScrIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfIispCallingAScrRowStatusEntry.setStatus("mandatory")
_MscAtmIfIispCallingAScrRowStatus_Type = RowStatus
_MscAtmIfIispCallingAScrRowStatus_Object = MibTableColumn
mscAtmIfIispCallingAScrRowStatus = _MscAtmIfIispCallingAScrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 5, 1, 1, 1),
    _MscAtmIfIispCallingAScrRowStatus_Type()
)
mscAtmIfIispCallingAScrRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfIispCallingAScrRowStatus.setStatus("mandatory")
_MscAtmIfIispCallingAScrComponentName_Type = DisplayString
_MscAtmIfIispCallingAScrComponentName_Object = MibTableColumn
mscAtmIfIispCallingAScrComponentName = _MscAtmIfIispCallingAScrComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 5, 1, 1, 2),
    _MscAtmIfIispCallingAScrComponentName_Type()
)
mscAtmIfIispCallingAScrComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfIispCallingAScrComponentName.setStatus("mandatory")
_MscAtmIfIispCallingAScrStorageType_Type = StorageType
_MscAtmIfIispCallingAScrStorageType_Object = MibTableColumn
mscAtmIfIispCallingAScrStorageType = _MscAtmIfIispCallingAScrStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 5, 1, 1, 4),
    _MscAtmIfIispCallingAScrStorageType_Type()
)
mscAtmIfIispCallingAScrStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfIispCallingAScrStorageType.setStatus("mandatory")
_MscAtmIfIispCallingAScrIndex_Type = NonReplicated
_MscAtmIfIispCallingAScrIndex_Object = MibTableColumn
mscAtmIfIispCallingAScrIndex = _MscAtmIfIispCallingAScrIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 5, 1, 1, 10),
    _MscAtmIfIispCallingAScrIndex_Type()
)
mscAtmIfIispCallingAScrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAtmIfIispCallingAScrIndex.setStatus("mandatory")
_MscAtmIfIispCallingAScrAddr_ObjectIdentity = ObjectIdentity
mscAtmIfIispCallingAScrAddr = _MscAtmIfIispCallingAScrAddr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 5, 2)
)
_MscAtmIfIispCallingAScrAddrRowStatusTable_Object = MibTable
mscAtmIfIispCallingAScrAddrRowStatusTable = _MscAtmIfIispCallingAScrAddrRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 5, 2, 1)
)
if mibBuilder.loadTexts:
    mscAtmIfIispCallingAScrAddrRowStatusTable.setStatus("mandatory")
_MscAtmIfIispCallingAScrAddrRowStatusEntry_Object = MibTableRow
mscAtmIfIispCallingAScrAddrRowStatusEntry = _MscAtmIfIispCallingAScrAddrRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 5, 2, 1, 1)
)
mscAtmIfIispCallingAScrAddrRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmIispMIB", "mscAtmIfIispIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmIispMIB", "mscAtmIfIispCallingAScrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmIispMIB", "mscAtmIfIispCallingAScrAddrAddressIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmIispMIB", "mscAtmIfIispCallingAScrAddrAddressActionIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfIispCallingAScrAddrRowStatusEntry.setStatus("mandatory")
_MscAtmIfIispCallingAScrAddrRowStatus_Type = RowStatus
_MscAtmIfIispCallingAScrAddrRowStatus_Object = MibTableColumn
mscAtmIfIispCallingAScrAddrRowStatus = _MscAtmIfIispCallingAScrAddrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 5, 2, 1, 1, 1),
    _MscAtmIfIispCallingAScrAddrRowStatus_Type()
)
mscAtmIfIispCallingAScrAddrRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfIispCallingAScrAddrRowStatus.setStatus("mandatory")
_MscAtmIfIispCallingAScrAddrComponentName_Type = DisplayString
_MscAtmIfIispCallingAScrAddrComponentName_Object = MibTableColumn
mscAtmIfIispCallingAScrAddrComponentName = _MscAtmIfIispCallingAScrAddrComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 5, 2, 1, 1, 2),
    _MscAtmIfIispCallingAScrAddrComponentName_Type()
)
mscAtmIfIispCallingAScrAddrComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfIispCallingAScrAddrComponentName.setStatus("mandatory")
_MscAtmIfIispCallingAScrAddrStorageType_Type = StorageType
_MscAtmIfIispCallingAScrAddrStorageType_Object = MibTableColumn
mscAtmIfIispCallingAScrAddrStorageType = _MscAtmIfIispCallingAScrAddrStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 5, 2, 1, 1, 4),
    _MscAtmIfIispCallingAScrAddrStorageType_Type()
)
mscAtmIfIispCallingAScrAddrStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfIispCallingAScrAddrStorageType.setStatus("mandatory")


class _MscAtmIfIispCallingAScrAddrAddressIndex_Type(AsciiStringIndex):
    """Custom type mscAtmIfIispCallingAScrAddrAddressIndex based on AsciiStringIndex"""
    subtypeSpec = AsciiStringIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_MscAtmIfIispCallingAScrAddrAddressIndex_Type.__name__ = "AsciiStringIndex"
_MscAtmIfIispCallingAScrAddrAddressIndex_Object = MibTableColumn
mscAtmIfIispCallingAScrAddrAddressIndex = _MscAtmIfIispCallingAScrAddrAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 5, 2, 1, 1, 10),
    _MscAtmIfIispCallingAScrAddrAddressIndex_Type()
)
mscAtmIfIispCallingAScrAddrAddressIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAtmIfIispCallingAScrAddrAddressIndex.setStatus("mandatory")


class _MscAtmIfIispCallingAScrAddrAddressActionIndex_Type(Integer32):
    """Custom type mscAtmIfIispCallingAScrAddrAddressActionIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("accept", 0),
          ("reject", 1))
    )


_MscAtmIfIispCallingAScrAddrAddressActionIndex_Type.__name__ = "Integer32"
_MscAtmIfIispCallingAScrAddrAddressActionIndex_Object = MibTableColumn
mscAtmIfIispCallingAScrAddrAddressActionIndex = _MscAtmIfIispCallingAScrAddrAddressActionIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 5, 2, 1, 1, 11),
    _MscAtmIfIispCallingAScrAddrAddressActionIndex_Type()
)
mscAtmIfIispCallingAScrAddrAddressActionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAtmIfIispCallingAScrAddrAddressActionIndex.setStatus("mandatory")
_MscAtmIfIispCallingAScrProvTable_Object = MibTable
mscAtmIfIispCallingAScrProvTable = _MscAtmIfIispCallingAScrProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 5, 10)
)
if mibBuilder.loadTexts:
    mscAtmIfIispCallingAScrProvTable.setStatus("mandatory")
_MscAtmIfIispCallingAScrProvEntry_Object = MibTableRow
mscAtmIfIispCallingAScrProvEntry = _MscAtmIfIispCallingAScrProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 5, 10, 1)
)
mscAtmIfIispCallingAScrProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmIispMIB", "mscAtmIfIispIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmIispMIB", "mscAtmIfIispCallingAScrIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfIispCallingAScrProvEntry.setStatus("mandatory")


class _MscAtmIfIispCallingAScrAdminStatus_Type(Integer32):
    """Custom type mscAtmIfIispCallingAScrAdminStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 0))
    )


_MscAtmIfIispCallingAScrAdminStatus_Type.__name__ = "Integer32"
_MscAtmIfIispCallingAScrAdminStatus_Object = MibTableColumn
mscAtmIfIispCallingAScrAdminStatus = _MscAtmIfIispCallingAScrAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 5, 10, 1, 1),
    _MscAtmIfIispCallingAScrAdminStatus_Type()
)
mscAtmIfIispCallingAScrAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfIispCallingAScrAdminStatus.setStatus("mandatory")


class _MscAtmIfIispCallingAScrDefaultInsertionAddress_Type(HexString):
    """Custom type mscAtmIfIispCallingAScrDefaultInsertionAddress based on HexString"""
    defaultHexValue = ""

    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_MscAtmIfIispCallingAScrDefaultInsertionAddress_Type.__name__ = "HexString"
_MscAtmIfIispCallingAScrDefaultInsertionAddress_Object = MibTableColumn
mscAtmIfIispCallingAScrDefaultInsertionAddress = _MscAtmIfIispCallingAScrDefaultInsertionAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 5, 10, 1, 2),
    _MscAtmIfIispCallingAScrDefaultInsertionAddress_Type()
)
mscAtmIfIispCallingAScrDefaultInsertionAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfIispCallingAScrDefaultInsertionAddress.setStatus("mandatory")
_MscAtmIfIispCallingAScrStatTable_Object = MibTable
mscAtmIfIispCallingAScrStatTable = _MscAtmIfIispCallingAScrStatTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 5, 11)
)
if mibBuilder.loadTexts:
    mscAtmIfIispCallingAScrStatTable.setStatus("mandatory")
_MscAtmIfIispCallingAScrStatEntry_Object = MibTableRow
mscAtmIfIispCallingAScrStatEntry = _MscAtmIfIispCallingAScrStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 5, 11, 1)
)
mscAtmIfIispCallingAScrStatEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmIispMIB", "mscAtmIfIispIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmIispMIB", "mscAtmIfIispCallingAScrIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfIispCallingAScrStatEntry.setStatus("mandatory")
_MscAtmIfIispCallingAScrAcceptedCalls_Type = Counter32
_MscAtmIfIispCallingAScrAcceptedCalls_Object = MibTableColumn
mscAtmIfIispCallingAScrAcceptedCalls = _MscAtmIfIispCallingAScrAcceptedCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 5, 11, 1, 1),
    _MscAtmIfIispCallingAScrAcceptedCalls_Type()
)
mscAtmIfIispCallingAScrAcceptedCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfIispCallingAScrAcceptedCalls.setStatus("mandatory")
_MscAtmIfIispCallingAScrRejectedCalls_Type = Counter32
_MscAtmIfIispCallingAScrRejectedCalls_Object = MibTableColumn
mscAtmIfIispCallingAScrRejectedCalls = _MscAtmIfIispCallingAScrRejectedCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 5, 11, 1, 2),
    _MscAtmIfIispCallingAScrRejectedCalls_Type()
)
mscAtmIfIispCallingAScrRejectedCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfIispCallingAScrRejectedCalls.setStatus("mandatory")
_MscAtmIfIispCallingAScrUnmatchedCalls_Type = Counter32
_MscAtmIfIispCallingAScrUnmatchedCalls_Object = MibTableColumn
mscAtmIfIispCallingAScrUnmatchedCalls = _MscAtmIfIispCallingAScrUnmatchedCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 5, 11, 1, 3),
    _MscAtmIfIispCallingAScrUnmatchedCalls_Type()
)
mscAtmIfIispCallingAScrUnmatchedCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfIispCallingAScrUnmatchedCalls.setStatus("mandatory")
_MscAtmIfIispCalledAScr_ObjectIdentity = ObjectIdentity
mscAtmIfIispCalledAScr = _MscAtmIfIispCalledAScr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 6)
)
_MscAtmIfIispCalledAScrRowStatusTable_Object = MibTable
mscAtmIfIispCalledAScrRowStatusTable = _MscAtmIfIispCalledAScrRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 6, 1)
)
if mibBuilder.loadTexts:
    mscAtmIfIispCalledAScrRowStatusTable.setStatus("mandatory")
_MscAtmIfIispCalledAScrRowStatusEntry_Object = MibTableRow
mscAtmIfIispCalledAScrRowStatusEntry = _MscAtmIfIispCalledAScrRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 6, 1, 1)
)
mscAtmIfIispCalledAScrRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmIispMIB", "mscAtmIfIispIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmIispMIB", "mscAtmIfIispCalledAScrIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfIispCalledAScrRowStatusEntry.setStatus("mandatory")
_MscAtmIfIispCalledAScrRowStatus_Type = RowStatus
_MscAtmIfIispCalledAScrRowStatus_Object = MibTableColumn
mscAtmIfIispCalledAScrRowStatus = _MscAtmIfIispCalledAScrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 6, 1, 1, 1),
    _MscAtmIfIispCalledAScrRowStatus_Type()
)
mscAtmIfIispCalledAScrRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfIispCalledAScrRowStatus.setStatus("mandatory")
_MscAtmIfIispCalledAScrComponentName_Type = DisplayString
_MscAtmIfIispCalledAScrComponentName_Object = MibTableColumn
mscAtmIfIispCalledAScrComponentName = _MscAtmIfIispCalledAScrComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 6, 1, 1, 2),
    _MscAtmIfIispCalledAScrComponentName_Type()
)
mscAtmIfIispCalledAScrComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfIispCalledAScrComponentName.setStatus("mandatory")
_MscAtmIfIispCalledAScrStorageType_Type = StorageType
_MscAtmIfIispCalledAScrStorageType_Object = MibTableColumn
mscAtmIfIispCalledAScrStorageType = _MscAtmIfIispCalledAScrStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 6, 1, 1, 4),
    _MscAtmIfIispCalledAScrStorageType_Type()
)
mscAtmIfIispCalledAScrStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfIispCalledAScrStorageType.setStatus("mandatory")
_MscAtmIfIispCalledAScrIndex_Type = NonReplicated
_MscAtmIfIispCalledAScrIndex_Object = MibTableColumn
mscAtmIfIispCalledAScrIndex = _MscAtmIfIispCalledAScrIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 6, 1, 1, 10),
    _MscAtmIfIispCalledAScrIndex_Type()
)
mscAtmIfIispCalledAScrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAtmIfIispCalledAScrIndex.setStatus("mandatory")
_MscAtmIfIispCalledAScrAddr_ObjectIdentity = ObjectIdentity
mscAtmIfIispCalledAScrAddr = _MscAtmIfIispCalledAScrAddr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 6, 2)
)
_MscAtmIfIispCalledAScrAddrRowStatusTable_Object = MibTable
mscAtmIfIispCalledAScrAddrRowStatusTable = _MscAtmIfIispCalledAScrAddrRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 6, 2, 1)
)
if mibBuilder.loadTexts:
    mscAtmIfIispCalledAScrAddrRowStatusTable.setStatus("mandatory")
_MscAtmIfIispCalledAScrAddrRowStatusEntry_Object = MibTableRow
mscAtmIfIispCalledAScrAddrRowStatusEntry = _MscAtmIfIispCalledAScrAddrRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 6, 2, 1, 1)
)
mscAtmIfIispCalledAScrAddrRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmIispMIB", "mscAtmIfIispIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmIispMIB", "mscAtmIfIispCalledAScrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmIispMIB", "mscAtmIfIispCalledAScrAddrAddressIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmIispMIB", "mscAtmIfIispCalledAScrAddrAddressActionIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfIispCalledAScrAddrRowStatusEntry.setStatus("mandatory")
_MscAtmIfIispCalledAScrAddrRowStatus_Type = RowStatus
_MscAtmIfIispCalledAScrAddrRowStatus_Object = MibTableColumn
mscAtmIfIispCalledAScrAddrRowStatus = _MscAtmIfIispCalledAScrAddrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 6, 2, 1, 1, 1),
    _MscAtmIfIispCalledAScrAddrRowStatus_Type()
)
mscAtmIfIispCalledAScrAddrRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfIispCalledAScrAddrRowStatus.setStatus("mandatory")
_MscAtmIfIispCalledAScrAddrComponentName_Type = DisplayString
_MscAtmIfIispCalledAScrAddrComponentName_Object = MibTableColumn
mscAtmIfIispCalledAScrAddrComponentName = _MscAtmIfIispCalledAScrAddrComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 6, 2, 1, 1, 2),
    _MscAtmIfIispCalledAScrAddrComponentName_Type()
)
mscAtmIfIispCalledAScrAddrComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfIispCalledAScrAddrComponentName.setStatus("mandatory")
_MscAtmIfIispCalledAScrAddrStorageType_Type = StorageType
_MscAtmIfIispCalledAScrAddrStorageType_Object = MibTableColumn
mscAtmIfIispCalledAScrAddrStorageType = _MscAtmIfIispCalledAScrAddrStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 6, 2, 1, 1, 4),
    _MscAtmIfIispCalledAScrAddrStorageType_Type()
)
mscAtmIfIispCalledAScrAddrStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfIispCalledAScrAddrStorageType.setStatus("mandatory")


class _MscAtmIfIispCalledAScrAddrAddressIndex_Type(AsciiStringIndex):
    """Custom type mscAtmIfIispCalledAScrAddrAddressIndex based on AsciiStringIndex"""
    subtypeSpec = AsciiStringIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_MscAtmIfIispCalledAScrAddrAddressIndex_Type.__name__ = "AsciiStringIndex"
_MscAtmIfIispCalledAScrAddrAddressIndex_Object = MibTableColumn
mscAtmIfIispCalledAScrAddrAddressIndex = _MscAtmIfIispCalledAScrAddrAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 6, 2, 1, 1, 10),
    _MscAtmIfIispCalledAScrAddrAddressIndex_Type()
)
mscAtmIfIispCalledAScrAddrAddressIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAtmIfIispCalledAScrAddrAddressIndex.setStatus("mandatory")


class _MscAtmIfIispCalledAScrAddrAddressActionIndex_Type(Integer32):
    """Custom type mscAtmIfIispCalledAScrAddrAddressActionIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("accept", 0),
          ("reject", 1))
    )


_MscAtmIfIispCalledAScrAddrAddressActionIndex_Type.__name__ = "Integer32"
_MscAtmIfIispCalledAScrAddrAddressActionIndex_Object = MibTableColumn
mscAtmIfIispCalledAScrAddrAddressActionIndex = _MscAtmIfIispCalledAScrAddrAddressActionIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 6, 2, 1, 1, 11),
    _MscAtmIfIispCalledAScrAddrAddressActionIndex_Type()
)
mscAtmIfIispCalledAScrAddrAddressActionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAtmIfIispCalledAScrAddrAddressActionIndex.setStatus("mandatory")
_MscAtmIfIispCalledAScrProvTable_Object = MibTable
mscAtmIfIispCalledAScrProvTable = _MscAtmIfIispCalledAScrProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 6, 10)
)
if mibBuilder.loadTexts:
    mscAtmIfIispCalledAScrProvTable.setStatus("mandatory")
_MscAtmIfIispCalledAScrProvEntry_Object = MibTableRow
mscAtmIfIispCalledAScrProvEntry = _MscAtmIfIispCalledAScrProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 6, 10, 1)
)
mscAtmIfIispCalledAScrProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmIispMIB", "mscAtmIfIispIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmIispMIB", "mscAtmIfIispCalledAScrIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfIispCalledAScrProvEntry.setStatus("mandatory")


class _MscAtmIfIispCalledAScrAdminStatus_Type(Integer32):
    """Custom type mscAtmIfIispCalledAScrAdminStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 0))
    )


_MscAtmIfIispCalledAScrAdminStatus_Type.__name__ = "Integer32"
_MscAtmIfIispCalledAScrAdminStatus_Object = MibTableColumn
mscAtmIfIispCalledAScrAdminStatus = _MscAtmIfIispCalledAScrAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 6, 10, 1, 1),
    _MscAtmIfIispCalledAScrAdminStatus_Type()
)
mscAtmIfIispCalledAScrAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfIispCalledAScrAdminStatus.setStatus("mandatory")
_MscAtmIfIispCalledAScrStatTable_Object = MibTable
mscAtmIfIispCalledAScrStatTable = _MscAtmIfIispCalledAScrStatTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 6, 11)
)
if mibBuilder.loadTexts:
    mscAtmIfIispCalledAScrStatTable.setStatus("mandatory")
_MscAtmIfIispCalledAScrStatEntry_Object = MibTableRow
mscAtmIfIispCalledAScrStatEntry = _MscAtmIfIispCalledAScrStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 6, 11, 1)
)
mscAtmIfIispCalledAScrStatEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmIispMIB", "mscAtmIfIispIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmIispMIB", "mscAtmIfIispCalledAScrIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfIispCalledAScrStatEntry.setStatus("mandatory")
_MscAtmIfIispCalledAScrAcceptedCalls_Type = Counter32
_MscAtmIfIispCalledAScrAcceptedCalls_Object = MibTableColumn
mscAtmIfIispCalledAScrAcceptedCalls = _MscAtmIfIispCalledAScrAcceptedCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 6, 11, 1, 1),
    _MscAtmIfIispCalledAScrAcceptedCalls_Type()
)
mscAtmIfIispCalledAScrAcceptedCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfIispCalledAScrAcceptedCalls.setStatus("mandatory")
_MscAtmIfIispCalledAScrRejectedCalls_Type = Counter32
_MscAtmIfIispCalledAScrRejectedCalls_Object = MibTableColumn
mscAtmIfIispCalledAScrRejectedCalls = _MscAtmIfIispCalledAScrRejectedCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 6, 11, 1, 2),
    _MscAtmIfIispCalledAScrRejectedCalls_Type()
)
mscAtmIfIispCalledAScrRejectedCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfIispCalledAScrRejectedCalls.setStatus("mandatory")
_MscAtmIfIispCalledAScrUnmatchedCalls_Type = Counter32
_MscAtmIfIispCalledAScrUnmatchedCalls_Object = MibTableColumn
mscAtmIfIispCalledAScrUnmatchedCalls = _MscAtmIfIispCalledAScrUnmatchedCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 6, 11, 1, 3),
    _MscAtmIfIispCalledAScrUnmatchedCalls_Type()
)
mscAtmIfIispCalledAScrUnmatchedCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfIispCalledAScrUnmatchedCalls.setStatus("mandatory")
_MscAtmIfIispProvTable_Object = MibTable
mscAtmIfIispProvTable = _MscAtmIfIispProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 10)
)
if mibBuilder.loadTexts:
    mscAtmIfIispProvTable.setStatus("mandatory")
_MscAtmIfIispProvEntry_Object = MibTableRow
mscAtmIfIispProvEntry = _MscAtmIfIispProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 10, 1)
)
mscAtmIfIispProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmIispMIB", "mscAtmIfIispIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfIispProvEntry.setStatus("mandatory")


class _MscAtmIfIispVersion_Type(Integer32):
    """Custom type mscAtmIfIispVersion based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("iisp10Sig30", 2),
          ("iisp10Sig31", 3))
    )


_MscAtmIfIispVersion_Type.__name__ = "Integer32"
_MscAtmIfIispVersion_Object = MibTableColumn
mscAtmIfIispVersion = _MscAtmIfIispVersion_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 10, 1, 1),
    _MscAtmIfIispVersion_Type()
)
mscAtmIfIispVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfIispVersion.setStatus("mandatory")


class _MscAtmIfIispSide_Type(Integer32):
    """Custom type mscAtmIfIispSide based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("networkSide", 0),
          ("userSide", 1))
    )


_MscAtmIfIispSide_Type.__name__ = "Integer32"
_MscAtmIfIispSide_Object = MibTableColumn
mscAtmIfIispSide = _MscAtmIfIispSide_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 10, 1, 2),
    _MscAtmIfIispSide_Type()
)
mscAtmIfIispSide.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfIispSide.setStatus("mandatory")


class _MscAtmIfIispSoftPvcRetryPeriod_Type(Unsigned32):
    """Custom type mscAtmIfIispSoftPvcRetryPeriod based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 999999),
    )


_MscAtmIfIispSoftPvcRetryPeriod_Type.__name__ = "Unsigned32"
_MscAtmIfIispSoftPvcRetryPeriod_Object = MibTableColumn
mscAtmIfIispSoftPvcRetryPeriod = _MscAtmIfIispSoftPvcRetryPeriod_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 10, 1, 3),
    _MscAtmIfIispSoftPvcRetryPeriod_Type()
)
mscAtmIfIispSoftPvcRetryPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfIispSoftPvcRetryPeriod.setStatus("obsolete")


class _MscAtmIfIispSoftPvpAndPvcRetryPeriod_Type(Unsigned32):
    """Custom type mscAtmIfIispSoftPvpAndPvcRetryPeriod based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 999999),
    )


_MscAtmIfIispSoftPvpAndPvcRetryPeriod_Type.__name__ = "Unsigned32"
_MscAtmIfIispSoftPvpAndPvcRetryPeriod_Object = MibTableColumn
mscAtmIfIispSoftPvpAndPvcRetryPeriod = _MscAtmIfIispSoftPvpAndPvcRetryPeriod_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 10, 1, 4),
    _MscAtmIfIispSoftPvpAndPvcRetryPeriod_Type()
)
mscAtmIfIispSoftPvpAndPvcRetryPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfIispSoftPvpAndPvcRetryPeriod.setStatus("mandatory")


class _MscAtmIfIispSoftPvpAndPvcHoldOffTime_Type(Unsigned32):
    """Custom type mscAtmIfIispSoftPvpAndPvcHoldOffTime based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(50, 20000),
    )


_MscAtmIfIispSoftPvpAndPvcHoldOffTime_Type.__name__ = "Unsigned32"
_MscAtmIfIispSoftPvpAndPvcHoldOffTime_Object = MibTableColumn
mscAtmIfIispSoftPvpAndPvcHoldOffTime = _MscAtmIfIispSoftPvpAndPvcHoldOffTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 10, 1, 5),
    _MscAtmIfIispSoftPvpAndPvcHoldOffTime_Type()
)
mscAtmIfIispSoftPvpAndPvcHoldOffTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfIispSoftPvpAndPvcHoldOffTime.setStatus("mandatory")
_MscAtmIfIispAcctOptTable_Object = MibTable
mscAtmIfIispAcctOptTable = _MscAtmIfIispAcctOptTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 11)
)
if mibBuilder.loadTexts:
    mscAtmIfIispAcctOptTable.setStatus("mandatory")
_MscAtmIfIispAcctOptEntry_Object = MibTableRow
mscAtmIfIispAcctOptEntry = _MscAtmIfIispAcctOptEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 11, 1)
)
mscAtmIfIispAcctOptEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmIispMIB", "mscAtmIfIispIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfIispAcctOptEntry.setStatus("mandatory")


class _MscAtmIfIispAccountCollection_Type(OctetString):
    """Custom type mscAtmIfIispAccountCollection based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscAtmIfIispAccountCollection_Type.__name__ = "OctetString"
_MscAtmIfIispAccountCollection_Object = MibTableColumn
mscAtmIfIispAccountCollection = _MscAtmIfIispAccountCollection_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 11, 1, 1),
    _MscAtmIfIispAccountCollection_Type()
)
mscAtmIfIispAccountCollection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfIispAccountCollection.setStatus("mandatory")


class _MscAtmIfIispAccountConnectionType_Type(Integer32):
    """Custom type mscAtmIfIispAccountConnectionType based on Integer32"""
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


_MscAtmIfIispAccountConnectionType_Type.__name__ = "Integer32"
_MscAtmIfIispAccountConnectionType_Object = MibTableColumn
mscAtmIfIispAccountConnectionType = _MscAtmIfIispAccountConnectionType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 11, 1, 2),
    _MscAtmIfIispAccountConnectionType_Type()
)
mscAtmIfIispAccountConnectionType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfIispAccountConnectionType.setStatus("mandatory")


class _MscAtmIfIispAccountClass_Type(Unsigned32):
    """Custom type mscAtmIfIispAccountClass based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscAtmIfIispAccountClass_Type.__name__ = "Unsigned32"
_MscAtmIfIispAccountClass_Object = MibTableColumn
mscAtmIfIispAccountClass = _MscAtmIfIispAccountClass_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 11, 1, 3),
    _MscAtmIfIispAccountClass_Type()
)
mscAtmIfIispAccountClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfIispAccountClass.setStatus("mandatory")


class _MscAtmIfIispServiceExchange_Type(Unsigned32):
    """Custom type mscAtmIfIispServiceExchange based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscAtmIfIispServiceExchange_Type.__name__ = "Unsigned32"
_MscAtmIfIispServiceExchange_Object = MibTableColumn
mscAtmIfIispServiceExchange = _MscAtmIfIispServiceExchange_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 7, 11, 1, 4),
    _MscAtmIfIispServiceExchange_Type()
)
mscAtmIfIispServiceExchange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfIispServiceExchange.setStatus("mandatory")
_MscAtmIfVptIisp_ObjectIdentity = ObjectIdentity
mscAtmIfVptIisp = _MscAtmIfVptIisp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6)
)
_MscAtmIfVptIispRowStatusTable_Object = MibTable
mscAtmIfVptIispRowStatusTable = _MscAtmIfVptIispRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 1)
)
if mibBuilder.loadTexts:
    mscAtmIfVptIispRowStatusTable.setStatus("mandatory")
_MscAtmIfVptIispRowStatusEntry_Object = MibTableRow
mscAtmIfVptIispRowStatusEntry = _MscAtmIfVptIispRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 1, 1)
)
mscAtmIfVptIispRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVptIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmIispMIB", "mscAtmIfVptIispIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfVptIispRowStatusEntry.setStatus("mandatory")
_MscAtmIfVptIispRowStatus_Type = RowStatus
_MscAtmIfVptIispRowStatus_Object = MibTableColumn
mscAtmIfVptIispRowStatus = _MscAtmIfVptIispRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 1, 1, 1),
    _MscAtmIfVptIispRowStatus_Type()
)
mscAtmIfVptIispRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVptIispRowStatus.setStatus("mandatory")
_MscAtmIfVptIispComponentName_Type = DisplayString
_MscAtmIfVptIispComponentName_Object = MibTableColumn
mscAtmIfVptIispComponentName = _MscAtmIfVptIispComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 1, 1, 2),
    _MscAtmIfVptIispComponentName_Type()
)
mscAtmIfVptIispComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptIispComponentName.setStatus("mandatory")
_MscAtmIfVptIispStorageType_Type = StorageType
_MscAtmIfVptIispStorageType_Object = MibTableColumn
mscAtmIfVptIispStorageType = _MscAtmIfVptIispStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 1, 1, 4),
    _MscAtmIfVptIispStorageType_Type()
)
mscAtmIfVptIispStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptIispStorageType.setStatus("mandatory")
_MscAtmIfVptIispIndex_Type = NonReplicated
_MscAtmIfVptIispIndex_Object = MibTableColumn
mscAtmIfVptIispIndex = _MscAtmIfVptIispIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 1, 1, 10),
    _MscAtmIfVptIispIndex_Type()
)
mscAtmIfVptIispIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAtmIfVptIispIndex.setStatus("mandatory")
_MscAtmIfVptIispSig_ObjectIdentity = ObjectIdentity
mscAtmIfVptIispSig = _MscAtmIfVptIispSig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 3)
)
_MscAtmIfVptIispSigRowStatusTable_Object = MibTable
mscAtmIfVptIispSigRowStatusTable = _MscAtmIfVptIispSigRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 3, 1)
)
if mibBuilder.loadTexts:
    mscAtmIfVptIispSigRowStatusTable.setStatus("mandatory")
_MscAtmIfVptIispSigRowStatusEntry_Object = MibTableRow
mscAtmIfVptIispSigRowStatusEntry = _MscAtmIfVptIispSigRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 3, 1, 1)
)
mscAtmIfVptIispSigRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVptIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmIispMIB", "mscAtmIfVptIispIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmIispMIB", "mscAtmIfVptIispSigIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfVptIispSigRowStatusEntry.setStatus("mandatory")
_MscAtmIfVptIispSigRowStatus_Type = RowStatus
_MscAtmIfVptIispSigRowStatus_Object = MibTableColumn
mscAtmIfVptIispSigRowStatus = _MscAtmIfVptIispSigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 3, 1, 1, 1),
    _MscAtmIfVptIispSigRowStatus_Type()
)
mscAtmIfVptIispSigRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptIispSigRowStatus.setStatus("mandatory")
_MscAtmIfVptIispSigComponentName_Type = DisplayString
_MscAtmIfVptIispSigComponentName_Object = MibTableColumn
mscAtmIfVptIispSigComponentName = _MscAtmIfVptIispSigComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 3, 1, 1, 2),
    _MscAtmIfVptIispSigComponentName_Type()
)
mscAtmIfVptIispSigComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptIispSigComponentName.setStatus("mandatory")
_MscAtmIfVptIispSigStorageType_Type = StorageType
_MscAtmIfVptIispSigStorageType_Object = MibTableColumn
mscAtmIfVptIispSigStorageType = _MscAtmIfVptIispSigStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 3, 1, 1, 4),
    _MscAtmIfVptIispSigStorageType_Type()
)
mscAtmIfVptIispSigStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptIispSigStorageType.setStatus("mandatory")
_MscAtmIfVptIispSigIndex_Type = NonReplicated
_MscAtmIfVptIispSigIndex_Object = MibTableColumn
mscAtmIfVptIispSigIndex = _MscAtmIfVptIispSigIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 3, 1, 1, 10),
    _MscAtmIfVptIispSigIndex_Type()
)
mscAtmIfVptIispSigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAtmIfVptIispSigIndex.setStatus("mandatory")
_MscAtmIfVptIispSigVcd_ObjectIdentity = ObjectIdentity
mscAtmIfVptIispSigVcd = _MscAtmIfVptIispSigVcd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 3, 2)
)
_MscAtmIfVptIispSigVcdRowStatusTable_Object = MibTable
mscAtmIfVptIispSigVcdRowStatusTable = _MscAtmIfVptIispSigVcdRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 3, 2, 1)
)
if mibBuilder.loadTexts:
    mscAtmIfVptIispSigVcdRowStatusTable.setStatus("mandatory")
_MscAtmIfVptIispSigVcdRowStatusEntry_Object = MibTableRow
mscAtmIfVptIispSigVcdRowStatusEntry = _MscAtmIfVptIispSigVcdRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 3, 2, 1, 1)
)
mscAtmIfVptIispSigVcdRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVptIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmIispMIB", "mscAtmIfVptIispIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmIispMIB", "mscAtmIfVptIispSigIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmIispMIB", "mscAtmIfVptIispSigVcdIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfVptIispSigVcdRowStatusEntry.setStatus("mandatory")
_MscAtmIfVptIispSigVcdRowStatus_Type = RowStatus
_MscAtmIfVptIispSigVcdRowStatus_Object = MibTableColumn
mscAtmIfVptIispSigVcdRowStatus = _MscAtmIfVptIispSigVcdRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 3, 2, 1, 1, 1),
    _MscAtmIfVptIispSigVcdRowStatus_Type()
)
mscAtmIfVptIispSigVcdRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVptIispSigVcdRowStatus.setStatus("mandatory")
_MscAtmIfVptIispSigVcdComponentName_Type = DisplayString
_MscAtmIfVptIispSigVcdComponentName_Object = MibTableColumn
mscAtmIfVptIispSigVcdComponentName = _MscAtmIfVptIispSigVcdComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 3, 2, 1, 1, 2),
    _MscAtmIfVptIispSigVcdComponentName_Type()
)
mscAtmIfVptIispSigVcdComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptIispSigVcdComponentName.setStatus("mandatory")
_MscAtmIfVptIispSigVcdStorageType_Type = StorageType
_MscAtmIfVptIispSigVcdStorageType_Object = MibTableColumn
mscAtmIfVptIispSigVcdStorageType = _MscAtmIfVptIispSigVcdStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 3, 2, 1, 1, 4),
    _MscAtmIfVptIispSigVcdStorageType_Type()
)
mscAtmIfVptIispSigVcdStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptIispSigVcdStorageType.setStatus("mandatory")
_MscAtmIfVptIispSigVcdIndex_Type = NonReplicated
_MscAtmIfVptIispSigVcdIndex_Object = MibTableColumn
mscAtmIfVptIispSigVcdIndex = _MscAtmIfVptIispSigVcdIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 3, 2, 1, 1, 10),
    _MscAtmIfVptIispSigVcdIndex_Type()
)
mscAtmIfVptIispSigVcdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAtmIfVptIispSigVcdIndex.setStatus("mandatory")
_MscAtmIfVptIispSigVcdProvTable_Object = MibTable
mscAtmIfVptIispSigVcdProvTable = _MscAtmIfVptIispSigVcdProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 3, 2, 10)
)
if mibBuilder.loadTexts:
    mscAtmIfVptIispSigVcdProvTable.setStatus("mandatory")
_MscAtmIfVptIispSigVcdProvEntry_Object = MibTableRow
mscAtmIfVptIispSigVcdProvEntry = _MscAtmIfVptIispSigVcdProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 3, 2, 10, 1)
)
mscAtmIfVptIispSigVcdProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVptIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmIispMIB", "mscAtmIfVptIispIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmIispMIB", "mscAtmIfVptIispSigIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmIispMIB", "mscAtmIfVptIispSigVcdIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfVptIispSigVcdProvEntry.setStatus("mandatory")


class _MscAtmIfVptIispSigVcdTrafficDescType_Type(Integer32):
    """Custom type mscAtmIfVptIispSigVcdTrafficDescType based on Integer32"""
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


_MscAtmIfVptIispSigVcdTrafficDescType_Type.__name__ = "Integer32"
_MscAtmIfVptIispSigVcdTrafficDescType_Object = MibTableColumn
mscAtmIfVptIispSigVcdTrafficDescType = _MscAtmIfVptIispSigVcdTrafficDescType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 3, 2, 10, 1, 1),
    _MscAtmIfVptIispSigVcdTrafficDescType_Type()
)
mscAtmIfVptIispSigVcdTrafficDescType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVptIispSigVcdTrafficDescType.setStatus("mandatory")


class _MscAtmIfVptIispSigVcdAtmServiceCategory_Type(Integer32):
    """Custom type mscAtmIfVptIispSigVcdAtmServiceCategory based on Integer32"""
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


_MscAtmIfVptIispSigVcdAtmServiceCategory_Type.__name__ = "Integer32"
_MscAtmIfVptIispSigVcdAtmServiceCategory_Object = MibTableColumn
mscAtmIfVptIispSigVcdAtmServiceCategory = _MscAtmIfVptIispSigVcdAtmServiceCategory_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 3, 2, 10, 1, 3),
    _MscAtmIfVptIispSigVcdAtmServiceCategory_Type()
)
mscAtmIfVptIispSigVcdAtmServiceCategory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVptIispSigVcdAtmServiceCategory.setStatus("mandatory")


class _MscAtmIfVptIispSigVcdWeight_Type(Unsigned32):
    """Custom type mscAtmIfVptIispSigVcdWeight based on Unsigned32"""
    defaultValue = 65535

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4095),
        ValueRangeConstraint(65535, 65535),
    )


_MscAtmIfVptIispSigVcdWeight_Type.__name__ = "Unsigned32"
_MscAtmIfVptIispSigVcdWeight_Object = MibTableColumn
mscAtmIfVptIispSigVcdWeight = _MscAtmIfVptIispSigVcdWeight_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 3, 2, 10, 1, 4),
    _MscAtmIfVptIispSigVcdWeight_Type()
)
mscAtmIfVptIispSigVcdWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVptIispSigVcdWeight.setStatus("mandatory")


class _MscAtmIfVptIispSigVcdQosClass_Type(Integer32):
    """Custom type mscAtmIfVptIispSigVcdQosClass based on Integer32"""
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


_MscAtmIfVptIispSigVcdQosClass_Type.__name__ = "Integer32"
_MscAtmIfVptIispSigVcdQosClass_Object = MibTableColumn
mscAtmIfVptIispSigVcdQosClass = _MscAtmIfVptIispSigVcdQosClass_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 3, 2, 10, 1, 21),
    _MscAtmIfVptIispSigVcdQosClass_Type()
)
mscAtmIfVptIispSigVcdQosClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVptIispSigVcdQosClass.setStatus("mandatory")


class _MscAtmIfVptIispSigVcdTrafficShaping_Type(Integer32):
    """Custom type mscAtmIfVptIispSigVcdTrafficShaping based on Integer32"""
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


_MscAtmIfVptIispSigVcdTrafficShaping_Type.__name__ = "Integer32"
_MscAtmIfVptIispSigVcdTrafficShaping_Object = MibTableColumn
mscAtmIfVptIispSigVcdTrafficShaping = _MscAtmIfVptIispSigVcdTrafficShaping_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 3, 2, 10, 1, 50),
    _MscAtmIfVptIispSigVcdTrafficShaping_Type()
)
mscAtmIfVptIispSigVcdTrafficShaping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVptIispSigVcdTrafficShaping.setStatus("mandatory")


class _MscAtmIfVptIispSigVcdUnshapedTransmitQueueing_Type(Integer32):
    """Custom type mscAtmIfVptIispSigVcdUnshapedTransmitQueueing based on Integer32"""
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


_MscAtmIfVptIispSigVcdUnshapedTransmitQueueing_Type.__name__ = "Integer32"
_MscAtmIfVptIispSigVcdUnshapedTransmitQueueing_Object = MibTableColumn
mscAtmIfVptIispSigVcdUnshapedTransmitQueueing = _MscAtmIfVptIispSigVcdUnshapedTransmitQueueing_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 3, 2, 10, 1, 60),
    _MscAtmIfVptIispSigVcdUnshapedTransmitQueueing_Type()
)
mscAtmIfVptIispSigVcdUnshapedTransmitQueueing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVptIispSigVcdUnshapedTransmitQueueing.setStatus("mandatory")


class _MscAtmIfVptIispSigVcdUsageParameterControl_Type(Integer32):
    """Custom type mscAtmIfVptIispSigVcdUsageParameterControl based on Integer32"""
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


_MscAtmIfVptIispSigVcdUsageParameterControl_Type.__name__ = "Integer32"
_MscAtmIfVptIispSigVcdUsageParameterControl_Object = MibTableColumn
mscAtmIfVptIispSigVcdUsageParameterControl = _MscAtmIfVptIispSigVcdUsageParameterControl_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 3, 2, 10, 1, 70),
    _MscAtmIfVptIispSigVcdUsageParameterControl_Type()
)
mscAtmIfVptIispSigVcdUsageParameterControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVptIispSigVcdUsageParameterControl.setStatus("mandatory")
_MscAtmIfVptIispSigVcdTdpTable_Object = MibTable
mscAtmIfVptIispSigVcdTdpTable = _MscAtmIfVptIispSigVcdTdpTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 3, 2, 387)
)
if mibBuilder.loadTexts:
    mscAtmIfVptIispSigVcdTdpTable.setStatus("mandatory")
_MscAtmIfVptIispSigVcdTdpEntry_Object = MibTableRow
mscAtmIfVptIispSigVcdTdpEntry = _MscAtmIfVptIispSigVcdTdpEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 3, 2, 387, 1)
)
mscAtmIfVptIispSigVcdTdpEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVptIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmIispMIB", "mscAtmIfVptIispIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmIispMIB", "mscAtmIfVptIispSigIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmIispMIB", "mscAtmIfVptIispSigVcdIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmIispMIB", "mscAtmIfVptIispSigVcdTdpIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfVptIispSigVcdTdpEntry.setStatus("mandatory")


class _MscAtmIfVptIispSigVcdTdpIndex_Type(Integer32):
    """Custom type mscAtmIfVptIispSigVcdTdpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_MscAtmIfVptIispSigVcdTdpIndex_Type.__name__ = "Integer32"
_MscAtmIfVptIispSigVcdTdpIndex_Object = MibTableColumn
mscAtmIfVptIispSigVcdTdpIndex = _MscAtmIfVptIispSigVcdTdpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 3, 2, 387, 1, 1),
    _MscAtmIfVptIispSigVcdTdpIndex_Type()
)
mscAtmIfVptIispSigVcdTdpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAtmIfVptIispSigVcdTdpIndex.setStatus("mandatory")


class _MscAtmIfVptIispSigVcdTdpValue_Type(Unsigned32):
    """Custom type mscAtmIfVptIispSigVcdTdpValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MscAtmIfVptIispSigVcdTdpValue_Type.__name__ = "Unsigned32"
_MscAtmIfVptIispSigVcdTdpValue_Object = MibTableColumn
mscAtmIfVptIispSigVcdTdpValue = _MscAtmIfVptIispSigVcdTdpValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 3, 2, 387, 1, 2),
    _MscAtmIfVptIispSigVcdTdpValue_Type()
)
mscAtmIfVptIispSigVcdTdpValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVptIispSigVcdTdpValue.setStatus("mandatory")
_MscAtmIfVptIispSigProvTable_Object = MibTable
mscAtmIfVptIispSigProvTable = _MscAtmIfVptIispSigProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 3, 10)
)
if mibBuilder.loadTexts:
    mscAtmIfVptIispSigProvTable.setStatus("mandatory")
_MscAtmIfVptIispSigProvEntry_Object = MibTableRow
mscAtmIfVptIispSigProvEntry = _MscAtmIfVptIispSigProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 3, 10, 1)
)
mscAtmIfVptIispSigProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVptIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmIispMIB", "mscAtmIfVptIispIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmIispMIB", "mscAtmIfVptIispSigIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfVptIispSigProvEntry.setStatus("mandatory")


class _MscAtmIfVptIispSigVci_Type(Unsigned32):
    """Custom type mscAtmIfVptIispSigVci based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscAtmIfVptIispSigVci_Type.__name__ = "Unsigned32"
_MscAtmIfVptIispSigVci_Object = MibTableColumn
mscAtmIfVptIispSigVci = _MscAtmIfVptIispSigVci_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 3, 10, 1, 1),
    _MscAtmIfVptIispSigVci_Type()
)
mscAtmIfVptIispSigVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVptIispSigVci.setStatus("mandatory")


class _MscAtmIfVptIispSigAddressConversion_Type(Integer32):
    """Custom type mscAtmIfVptIispSigAddressConversion based on Integer32"""
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


_MscAtmIfVptIispSigAddressConversion_Type.__name__ = "Integer32"
_MscAtmIfVptIispSigAddressConversion_Object = MibTableColumn
mscAtmIfVptIispSigAddressConversion = _MscAtmIfVptIispSigAddressConversion_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 3, 10, 1, 2),
    _MscAtmIfVptIispSigAddressConversion_Type()
)
mscAtmIfVptIispSigAddressConversion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVptIispSigAddressConversion.setStatus("mandatory")


class _MscAtmIfVptIispSigOperatingMode_Type(Integer32):
    """Custom type mscAtmIfVptIispSigOperatingMode based on Integer32"""
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


_MscAtmIfVptIispSigOperatingMode_Type.__name__ = "Integer32"
_MscAtmIfVptIispSigOperatingMode_Object = MibTableColumn
mscAtmIfVptIispSigOperatingMode = _MscAtmIfVptIispSigOperatingMode_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 3, 10, 1, 3),
    _MscAtmIfVptIispSigOperatingMode_Type()
)
mscAtmIfVptIispSigOperatingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVptIispSigOperatingMode.setStatus("mandatory")
_MscAtmIfVptIispSigStateTable_Object = MibTable
mscAtmIfVptIispSigStateTable = _MscAtmIfVptIispSigStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 3, 11)
)
if mibBuilder.loadTexts:
    mscAtmIfVptIispSigStateTable.setStatus("mandatory")
_MscAtmIfVptIispSigStateEntry_Object = MibTableRow
mscAtmIfVptIispSigStateEntry = _MscAtmIfVptIispSigStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 3, 11, 1)
)
mscAtmIfVptIispSigStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVptIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmIispMIB", "mscAtmIfVptIispIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmIispMIB", "mscAtmIfVptIispSigIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfVptIispSigStateEntry.setStatus("mandatory")


class _MscAtmIfVptIispSigAdminState_Type(Integer32):
    """Custom type mscAtmIfVptIispSigAdminState based on Integer32"""
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


_MscAtmIfVptIispSigAdminState_Type.__name__ = "Integer32"
_MscAtmIfVptIispSigAdminState_Object = MibTableColumn
mscAtmIfVptIispSigAdminState = _MscAtmIfVptIispSigAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 3, 11, 1, 1),
    _MscAtmIfVptIispSigAdminState_Type()
)
mscAtmIfVptIispSigAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptIispSigAdminState.setStatus("mandatory")


class _MscAtmIfVptIispSigOperationalState_Type(Integer32):
    """Custom type mscAtmIfVptIispSigOperationalState based on Integer32"""
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


_MscAtmIfVptIispSigOperationalState_Type.__name__ = "Integer32"
_MscAtmIfVptIispSigOperationalState_Object = MibTableColumn
mscAtmIfVptIispSigOperationalState = _MscAtmIfVptIispSigOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 3, 11, 1, 2),
    _MscAtmIfVptIispSigOperationalState_Type()
)
mscAtmIfVptIispSigOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptIispSigOperationalState.setStatus("mandatory")


class _MscAtmIfVptIispSigUsageState_Type(Integer32):
    """Custom type mscAtmIfVptIispSigUsageState based on Integer32"""
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


_MscAtmIfVptIispSigUsageState_Type.__name__ = "Integer32"
_MscAtmIfVptIispSigUsageState_Object = MibTableColumn
mscAtmIfVptIispSigUsageState = _MscAtmIfVptIispSigUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 3, 11, 1, 3),
    _MscAtmIfVptIispSigUsageState_Type()
)
mscAtmIfVptIispSigUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptIispSigUsageState.setStatus("mandatory")
_MscAtmIfVptIispSigOperTable_Object = MibTable
mscAtmIfVptIispSigOperTable = _MscAtmIfVptIispSigOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 3, 12)
)
if mibBuilder.loadTexts:
    mscAtmIfVptIispSigOperTable.setStatus("mandatory")
_MscAtmIfVptIispSigOperEntry_Object = MibTableRow
mscAtmIfVptIispSigOperEntry = _MscAtmIfVptIispSigOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 3, 12, 1)
)
mscAtmIfVptIispSigOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVptIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmIispMIB", "mscAtmIfVptIispIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmIispMIB", "mscAtmIfVptIispSigIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfVptIispSigOperEntry.setStatus("mandatory")


class _MscAtmIfVptIispSigLastTxCauseCode_Type(Unsigned32):
    """Custom type mscAtmIfVptIispSigLastTxCauseCode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscAtmIfVptIispSigLastTxCauseCode_Type.__name__ = "Unsigned32"
_MscAtmIfVptIispSigLastTxCauseCode_Object = MibTableColumn
mscAtmIfVptIispSigLastTxCauseCode = _MscAtmIfVptIispSigLastTxCauseCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 3, 12, 1, 1),
    _MscAtmIfVptIispSigLastTxCauseCode_Type()
)
mscAtmIfVptIispSigLastTxCauseCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptIispSigLastTxCauseCode.setStatus("mandatory")


class _MscAtmIfVptIispSigLastTxDiagCode_Type(Hex):
    """Custom type mscAtmIfVptIispSigLastTxDiagCode based on Hex"""
    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscAtmIfVptIispSigLastTxDiagCode_Type.__name__ = "Hex"
_MscAtmIfVptIispSigLastTxDiagCode_Object = MibTableColumn
mscAtmIfVptIispSigLastTxDiagCode = _MscAtmIfVptIispSigLastTxDiagCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 3, 12, 1, 2),
    _MscAtmIfVptIispSigLastTxDiagCode_Type()
)
mscAtmIfVptIispSigLastTxDiagCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptIispSigLastTxDiagCode.setStatus("mandatory")


class _MscAtmIfVptIispSigLastRxCauseCode_Type(Unsigned32):
    """Custom type mscAtmIfVptIispSigLastRxCauseCode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscAtmIfVptIispSigLastRxCauseCode_Type.__name__ = "Unsigned32"
_MscAtmIfVptIispSigLastRxCauseCode_Object = MibTableColumn
mscAtmIfVptIispSigLastRxCauseCode = _MscAtmIfVptIispSigLastRxCauseCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 3, 12, 1, 3),
    _MscAtmIfVptIispSigLastRxCauseCode_Type()
)
mscAtmIfVptIispSigLastRxCauseCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptIispSigLastRxCauseCode.setStatus("mandatory")


class _MscAtmIfVptIispSigLastRxDiagCode_Type(Hex):
    """Custom type mscAtmIfVptIispSigLastRxDiagCode based on Hex"""
    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscAtmIfVptIispSigLastRxDiagCode_Type.__name__ = "Hex"
_MscAtmIfVptIispSigLastRxDiagCode_Object = MibTableColumn
mscAtmIfVptIispSigLastRxDiagCode = _MscAtmIfVptIispSigLastRxDiagCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 3, 12, 1, 4),
    _MscAtmIfVptIispSigLastRxDiagCode_Type()
)
mscAtmIfVptIispSigLastRxDiagCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptIispSigLastRxDiagCode.setStatus("mandatory")
_MscAtmIfVptIispSigStatsTable_Object = MibTable
mscAtmIfVptIispSigStatsTable = _MscAtmIfVptIispSigStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 3, 13)
)
if mibBuilder.loadTexts:
    mscAtmIfVptIispSigStatsTable.setStatus("mandatory")
_MscAtmIfVptIispSigStatsEntry_Object = MibTableRow
mscAtmIfVptIispSigStatsEntry = _MscAtmIfVptIispSigStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 3, 13, 1)
)
mscAtmIfVptIispSigStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVptIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmIispMIB", "mscAtmIfVptIispIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmIispMIB", "mscAtmIfVptIispSigIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfVptIispSigStatsEntry.setStatus("mandatory")
_MscAtmIfVptIispSigCurrentConnections_Type = Counter32
_MscAtmIfVptIispSigCurrentConnections_Object = MibTableColumn
mscAtmIfVptIispSigCurrentConnections = _MscAtmIfVptIispSigCurrentConnections_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 3, 13, 1, 1),
    _MscAtmIfVptIispSigCurrentConnections_Type()
)
mscAtmIfVptIispSigCurrentConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptIispSigCurrentConnections.setStatus("obsolete")


class _MscAtmIfVptIispSigPeakConnections_Type(Gauge32):
    """Custom type mscAtmIfVptIispSigPeakConnections based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscAtmIfVptIispSigPeakConnections_Type.__name__ = "Gauge32"
_MscAtmIfVptIispSigPeakConnections_Object = MibTableColumn
mscAtmIfVptIispSigPeakConnections = _MscAtmIfVptIispSigPeakConnections_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 3, 13, 1, 2),
    _MscAtmIfVptIispSigPeakConnections_Type()
)
mscAtmIfVptIispSigPeakConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptIispSigPeakConnections.setStatus("mandatory")
_MscAtmIfVptIispSigSuccessfulConnections_Type = Counter32
_MscAtmIfVptIispSigSuccessfulConnections_Object = MibTableColumn
mscAtmIfVptIispSigSuccessfulConnections = _MscAtmIfVptIispSigSuccessfulConnections_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 3, 13, 1, 3),
    _MscAtmIfVptIispSigSuccessfulConnections_Type()
)
mscAtmIfVptIispSigSuccessfulConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptIispSigSuccessfulConnections.setStatus("mandatory")
_MscAtmIfVptIispSigFailedConnections_Type = Counter32
_MscAtmIfVptIispSigFailedConnections_Object = MibTableColumn
mscAtmIfVptIispSigFailedConnections = _MscAtmIfVptIispSigFailedConnections_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 3, 13, 1, 4),
    _MscAtmIfVptIispSigFailedConnections_Type()
)
mscAtmIfVptIispSigFailedConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptIispSigFailedConnections.setStatus("mandatory")
_MscAtmIfVptIispSigTxPdus_Type = Counter32
_MscAtmIfVptIispSigTxPdus_Object = MibTableColumn
mscAtmIfVptIispSigTxPdus = _MscAtmIfVptIispSigTxPdus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 3, 13, 1, 5),
    _MscAtmIfVptIispSigTxPdus_Type()
)
mscAtmIfVptIispSigTxPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptIispSigTxPdus.setStatus("mandatory")
_MscAtmIfVptIispSigRxPdus_Type = Counter32
_MscAtmIfVptIispSigRxPdus_Object = MibTableColumn
mscAtmIfVptIispSigRxPdus = _MscAtmIfVptIispSigRxPdus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 3, 13, 1, 6),
    _MscAtmIfVptIispSigRxPdus_Type()
)
mscAtmIfVptIispSigRxPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptIispSigRxPdus.setStatus("mandatory")


class _MscAtmIfVptIispSigCurrentPmpConnections_Type(Gauge32):
    """Custom type mscAtmIfVptIispSigCurrentPmpConnections based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscAtmIfVptIispSigCurrentPmpConnections_Type.__name__ = "Gauge32"
_MscAtmIfVptIispSigCurrentPmpConnections_Object = MibTableColumn
mscAtmIfVptIispSigCurrentPmpConnections = _MscAtmIfVptIispSigCurrentPmpConnections_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 3, 13, 1, 7),
    _MscAtmIfVptIispSigCurrentPmpConnections_Type()
)
mscAtmIfVptIispSigCurrentPmpConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptIispSigCurrentPmpConnections.setStatus("mandatory")


class _MscAtmIfVptIispSigPeakPmpConnections_Type(Gauge32):
    """Custom type mscAtmIfVptIispSigPeakPmpConnections based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscAtmIfVptIispSigPeakPmpConnections_Type.__name__ = "Gauge32"
_MscAtmIfVptIispSigPeakPmpConnections_Object = MibTableColumn
mscAtmIfVptIispSigPeakPmpConnections = _MscAtmIfVptIispSigPeakPmpConnections_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 3, 13, 1, 8),
    _MscAtmIfVptIispSigPeakPmpConnections_Type()
)
mscAtmIfVptIispSigPeakPmpConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptIispSigPeakPmpConnections.setStatus("mandatory")
_MscAtmIfVptIispSigSuccessfulPmpConnections_Type = Counter32
_MscAtmIfVptIispSigSuccessfulPmpConnections_Object = MibTableColumn
mscAtmIfVptIispSigSuccessfulPmpConnections = _MscAtmIfVptIispSigSuccessfulPmpConnections_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 3, 13, 1, 9),
    _MscAtmIfVptIispSigSuccessfulPmpConnections_Type()
)
mscAtmIfVptIispSigSuccessfulPmpConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptIispSigSuccessfulPmpConnections.setStatus("mandatory")
_MscAtmIfVptIispSigFailedPmpConnections_Type = Counter32
_MscAtmIfVptIispSigFailedPmpConnections_Object = MibTableColumn
mscAtmIfVptIispSigFailedPmpConnections = _MscAtmIfVptIispSigFailedPmpConnections_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 3, 13, 1, 10),
    _MscAtmIfVptIispSigFailedPmpConnections_Type()
)
mscAtmIfVptIispSigFailedPmpConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptIispSigFailedPmpConnections.setStatus("mandatory")


class _MscAtmIfVptIispSigNewCurrentConnections_Type(Gauge32):
    """Custom type mscAtmIfVptIispSigNewCurrentConnections based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscAtmIfVptIispSigNewCurrentConnections_Type.__name__ = "Gauge32"
_MscAtmIfVptIispSigNewCurrentConnections_Object = MibTableColumn
mscAtmIfVptIispSigNewCurrentConnections = _MscAtmIfVptIispSigNewCurrentConnections_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 3, 13, 1, 11),
    _MscAtmIfVptIispSigNewCurrentConnections_Type()
)
mscAtmIfVptIispSigNewCurrentConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptIispSigNewCurrentConnections.setStatus("mandatory")
_MscAtmIfVptIispAddr_ObjectIdentity = ObjectIdentity
mscAtmIfVptIispAddr = _MscAtmIfVptIispAddr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 4)
)
_MscAtmIfVptIispAddrRowStatusTable_Object = MibTable
mscAtmIfVptIispAddrRowStatusTable = _MscAtmIfVptIispAddrRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 4, 1)
)
if mibBuilder.loadTexts:
    mscAtmIfVptIispAddrRowStatusTable.setStatus("mandatory")
_MscAtmIfVptIispAddrRowStatusEntry_Object = MibTableRow
mscAtmIfVptIispAddrRowStatusEntry = _MscAtmIfVptIispAddrRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 4, 1, 1)
)
mscAtmIfVptIispAddrRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVptIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmIispMIB", "mscAtmIfVptIispIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmIispMIB", "mscAtmIfVptIispAddrAddressIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmIispMIB", "mscAtmIfVptIispAddrAddressTypeIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfVptIispAddrRowStatusEntry.setStatus("mandatory")
_MscAtmIfVptIispAddrRowStatus_Type = RowStatus
_MscAtmIfVptIispAddrRowStatus_Object = MibTableColumn
mscAtmIfVptIispAddrRowStatus = _MscAtmIfVptIispAddrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 4, 1, 1, 1),
    _MscAtmIfVptIispAddrRowStatus_Type()
)
mscAtmIfVptIispAddrRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVptIispAddrRowStatus.setStatus("mandatory")
_MscAtmIfVptIispAddrComponentName_Type = DisplayString
_MscAtmIfVptIispAddrComponentName_Object = MibTableColumn
mscAtmIfVptIispAddrComponentName = _MscAtmIfVptIispAddrComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 4, 1, 1, 2),
    _MscAtmIfVptIispAddrComponentName_Type()
)
mscAtmIfVptIispAddrComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptIispAddrComponentName.setStatus("mandatory")
_MscAtmIfVptIispAddrStorageType_Type = StorageType
_MscAtmIfVptIispAddrStorageType_Object = MibTableColumn
mscAtmIfVptIispAddrStorageType = _MscAtmIfVptIispAddrStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 4, 1, 1, 4),
    _MscAtmIfVptIispAddrStorageType_Type()
)
mscAtmIfVptIispAddrStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptIispAddrStorageType.setStatus("mandatory")


class _MscAtmIfVptIispAddrAddressIndex_Type(AsciiStringIndex):
    """Custom type mscAtmIfVptIispAddrAddressIndex based on AsciiStringIndex"""
    subtypeSpec = AsciiStringIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_MscAtmIfVptIispAddrAddressIndex_Type.__name__ = "AsciiStringIndex"
_MscAtmIfVptIispAddrAddressIndex_Object = MibTableColumn
mscAtmIfVptIispAddrAddressIndex = _MscAtmIfVptIispAddrAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 4, 1, 1, 10),
    _MscAtmIfVptIispAddrAddressIndex_Type()
)
mscAtmIfVptIispAddrAddressIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAtmIfVptIispAddrAddressIndex.setStatus("mandatory")


class _MscAtmIfVptIispAddrAddressTypeIndex_Type(Integer32):
    """Custom type mscAtmIfVptIispAddrAddressTypeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("alternate", 1),
          ("default", 3),
          ("primary", 0))
    )


_MscAtmIfVptIispAddrAddressTypeIndex_Type.__name__ = "Integer32"
_MscAtmIfVptIispAddrAddressTypeIndex_Object = MibTableColumn
mscAtmIfVptIispAddrAddressTypeIndex = _MscAtmIfVptIispAddrAddressTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 4, 1, 1, 11),
    _MscAtmIfVptIispAddrAddressTypeIndex_Type()
)
mscAtmIfVptIispAddrAddressTypeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAtmIfVptIispAddrAddressTypeIndex.setStatus("mandatory")
_MscAtmIfVptIispAddrTermSP_ObjectIdentity = ObjectIdentity
mscAtmIfVptIispAddrTermSP = _MscAtmIfVptIispAddrTermSP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 4, 2)
)
_MscAtmIfVptIispAddrTermSPRowStatusTable_Object = MibTable
mscAtmIfVptIispAddrTermSPRowStatusTable = _MscAtmIfVptIispAddrTermSPRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 4, 2, 1)
)
if mibBuilder.loadTexts:
    mscAtmIfVptIispAddrTermSPRowStatusTable.setStatus("mandatory")
_MscAtmIfVptIispAddrTermSPRowStatusEntry_Object = MibTableRow
mscAtmIfVptIispAddrTermSPRowStatusEntry = _MscAtmIfVptIispAddrTermSPRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 4, 2, 1, 1)
)
mscAtmIfVptIispAddrTermSPRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVptIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmIispMIB", "mscAtmIfVptIispIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmIispMIB", "mscAtmIfVptIispAddrAddressIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmIispMIB", "mscAtmIfVptIispAddrAddressTypeIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmIispMIB", "mscAtmIfVptIispAddrTermSPIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfVptIispAddrTermSPRowStatusEntry.setStatus("mandatory")
_MscAtmIfVptIispAddrTermSPRowStatus_Type = RowStatus
_MscAtmIfVptIispAddrTermSPRowStatus_Object = MibTableColumn
mscAtmIfVptIispAddrTermSPRowStatus = _MscAtmIfVptIispAddrTermSPRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 4, 2, 1, 1, 1),
    _MscAtmIfVptIispAddrTermSPRowStatus_Type()
)
mscAtmIfVptIispAddrTermSPRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVptIispAddrTermSPRowStatus.setStatus("mandatory")
_MscAtmIfVptIispAddrTermSPComponentName_Type = DisplayString
_MscAtmIfVptIispAddrTermSPComponentName_Object = MibTableColumn
mscAtmIfVptIispAddrTermSPComponentName = _MscAtmIfVptIispAddrTermSPComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 4, 2, 1, 1, 2),
    _MscAtmIfVptIispAddrTermSPComponentName_Type()
)
mscAtmIfVptIispAddrTermSPComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptIispAddrTermSPComponentName.setStatus("mandatory")
_MscAtmIfVptIispAddrTermSPStorageType_Type = StorageType
_MscAtmIfVptIispAddrTermSPStorageType_Object = MibTableColumn
mscAtmIfVptIispAddrTermSPStorageType = _MscAtmIfVptIispAddrTermSPStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 4, 2, 1, 1, 4),
    _MscAtmIfVptIispAddrTermSPStorageType_Type()
)
mscAtmIfVptIispAddrTermSPStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptIispAddrTermSPStorageType.setStatus("mandatory")
_MscAtmIfVptIispAddrTermSPIndex_Type = NonReplicated
_MscAtmIfVptIispAddrTermSPIndex_Object = MibTableColumn
mscAtmIfVptIispAddrTermSPIndex = _MscAtmIfVptIispAddrTermSPIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 4, 2, 1, 1, 10),
    _MscAtmIfVptIispAddrTermSPIndex_Type()
)
mscAtmIfVptIispAddrTermSPIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAtmIfVptIispAddrTermSPIndex.setStatus("mandatory")
_MscAtmIfVptIispAddrPnniInfo_ObjectIdentity = ObjectIdentity
mscAtmIfVptIispAddrPnniInfo = _MscAtmIfVptIispAddrPnniInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 4, 3)
)
_MscAtmIfVptIispAddrPnniInfoRowStatusTable_Object = MibTable
mscAtmIfVptIispAddrPnniInfoRowStatusTable = _MscAtmIfVptIispAddrPnniInfoRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 4, 3, 1)
)
if mibBuilder.loadTexts:
    mscAtmIfVptIispAddrPnniInfoRowStatusTable.setStatus("mandatory")
_MscAtmIfVptIispAddrPnniInfoRowStatusEntry_Object = MibTableRow
mscAtmIfVptIispAddrPnniInfoRowStatusEntry = _MscAtmIfVptIispAddrPnniInfoRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 4, 3, 1, 1)
)
mscAtmIfVptIispAddrPnniInfoRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVptIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmIispMIB", "mscAtmIfVptIispIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmIispMIB", "mscAtmIfVptIispAddrAddressIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmIispMIB", "mscAtmIfVptIispAddrAddressTypeIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmIispMIB", "mscAtmIfVptIispAddrPnniInfoIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfVptIispAddrPnniInfoRowStatusEntry.setStatus("mandatory")
_MscAtmIfVptIispAddrPnniInfoRowStatus_Type = RowStatus
_MscAtmIfVptIispAddrPnniInfoRowStatus_Object = MibTableColumn
mscAtmIfVptIispAddrPnniInfoRowStatus = _MscAtmIfVptIispAddrPnniInfoRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 4, 3, 1, 1, 1),
    _MscAtmIfVptIispAddrPnniInfoRowStatus_Type()
)
mscAtmIfVptIispAddrPnniInfoRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVptIispAddrPnniInfoRowStatus.setStatus("mandatory")
_MscAtmIfVptIispAddrPnniInfoComponentName_Type = DisplayString
_MscAtmIfVptIispAddrPnniInfoComponentName_Object = MibTableColumn
mscAtmIfVptIispAddrPnniInfoComponentName = _MscAtmIfVptIispAddrPnniInfoComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 4, 3, 1, 1, 2),
    _MscAtmIfVptIispAddrPnniInfoComponentName_Type()
)
mscAtmIfVptIispAddrPnniInfoComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptIispAddrPnniInfoComponentName.setStatus("mandatory")
_MscAtmIfVptIispAddrPnniInfoStorageType_Type = StorageType
_MscAtmIfVptIispAddrPnniInfoStorageType_Object = MibTableColumn
mscAtmIfVptIispAddrPnniInfoStorageType = _MscAtmIfVptIispAddrPnniInfoStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 4, 3, 1, 1, 4),
    _MscAtmIfVptIispAddrPnniInfoStorageType_Type()
)
mscAtmIfVptIispAddrPnniInfoStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptIispAddrPnniInfoStorageType.setStatus("mandatory")
_MscAtmIfVptIispAddrPnniInfoIndex_Type = NonReplicated
_MscAtmIfVptIispAddrPnniInfoIndex_Object = MibTableColumn
mscAtmIfVptIispAddrPnniInfoIndex = _MscAtmIfVptIispAddrPnniInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 4, 3, 1, 1, 10),
    _MscAtmIfVptIispAddrPnniInfoIndex_Type()
)
mscAtmIfVptIispAddrPnniInfoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAtmIfVptIispAddrPnniInfoIndex.setStatus("mandatory")
_MscAtmIfVptIispAddrPnniInfoProvTable_Object = MibTable
mscAtmIfVptIispAddrPnniInfoProvTable = _MscAtmIfVptIispAddrPnniInfoProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 4, 3, 10)
)
if mibBuilder.loadTexts:
    mscAtmIfVptIispAddrPnniInfoProvTable.setStatus("mandatory")
_MscAtmIfVptIispAddrPnniInfoProvEntry_Object = MibTableRow
mscAtmIfVptIispAddrPnniInfoProvEntry = _MscAtmIfVptIispAddrPnniInfoProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 4, 3, 10, 1)
)
mscAtmIfVptIispAddrPnniInfoProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVptIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmIispMIB", "mscAtmIfVptIispIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmIispMIB", "mscAtmIfVptIispAddrAddressIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmIispMIB", "mscAtmIfVptIispAddrAddressTypeIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmIispMIB", "mscAtmIfVptIispAddrPnniInfoIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfVptIispAddrPnniInfoProvEntry.setStatus("mandatory")


class _MscAtmIfVptIispAddrPnniInfoScope_Type(Integer32):
    """Custom type mscAtmIfVptIispAddrPnniInfoScope based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 104),
    )


_MscAtmIfVptIispAddrPnniInfoScope_Type.__name__ = "Integer32"
_MscAtmIfVptIispAddrPnniInfoScope_Object = MibTableColumn
mscAtmIfVptIispAddrPnniInfoScope = _MscAtmIfVptIispAddrPnniInfoScope_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 4, 3, 10, 1, 1),
    _MscAtmIfVptIispAddrPnniInfoScope_Type()
)
mscAtmIfVptIispAddrPnniInfoScope.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVptIispAddrPnniInfoScope.setStatus("mandatory")


class _MscAtmIfVptIispAddrPnniInfoReachability_Type(Integer32):
    """Custom type mscAtmIfVptIispAddrPnniInfoReachability based on Integer32"""
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


_MscAtmIfVptIispAddrPnniInfoReachability_Type.__name__ = "Integer32"
_MscAtmIfVptIispAddrPnniInfoReachability_Object = MibTableColumn
mscAtmIfVptIispAddrPnniInfoReachability = _MscAtmIfVptIispAddrPnniInfoReachability_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 4, 3, 10, 1, 2),
    _MscAtmIfVptIispAddrPnniInfoReachability_Type()
)
mscAtmIfVptIispAddrPnniInfoReachability.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVptIispAddrPnniInfoReachability.setStatus("mandatory")
_MscAtmIfVptIispAddrOperTable_Object = MibTable
mscAtmIfVptIispAddrOperTable = _MscAtmIfVptIispAddrOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 4, 10)
)
if mibBuilder.loadTexts:
    mscAtmIfVptIispAddrOperTable.setStatus("mandatory")
_MscAtmIfVptIispAddrOperEntry_Object = MibTableRow
mscAtmIfVptIispAddrOperEntry = _MscAtmIfVptIispAddrOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 4, 10, 1)
)
mscAtmIfVptIispAddrOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVptIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmIispMIB", "mscAtmIfVptIispIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmIispMIB", "mscAtmIfVptIispAddrAddressIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmIispMIB", "mscAtmIfVptIispAddrAddressTypeIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfVptIispAddrOperEntry.setStatus("mandatory")


class _MscAtmIfVptIispAddrScope_Type(Integer32):
    """Custom type mscAtmIfVptIispAddrScope based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 104),
    )


_MscAtmIfVptIispAddrScope_Type.__name__ = "Integer32"
_MscAtmIfVptIispAddrScope_Object = MibTableColumn
mscAtmIfVptIispAddrScope = _MscAtmIfVptIispAddrScope_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 4, 10, 1, 1),
    _MscAtmIfVptIispAddrScope_Type()
)
mscAtmIfVptIispAddrScope.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptIispAddrScope.setStatus("mandatory")


class _MscAtmIfVptIispAddrReachability_Type(Integer32):
    """Custom type mscAtmIfVptIispAddrReachability based on Integer32"""
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


_MscAtmIfVptIispAddrReachability_Type.__name__ = "Integer32"
_MscAtmIfVptIispAddrReachability_Object = MibTableColumn
mscAtmIfVptIispAddrReachability = _MscAtmIfVptIispAddrReachability_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 4, 10, 1, 2),
    _MscAtmIfVptIispAddrReachability_Type()
)
mscAtmIfVptIispAddrReachability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptIispAddrReachability.setStatus("mandatory")
_MscAtmIfVptIispCallingAScr_ObjectIdentity = ObjectIdentity
mscAtmIfVptIispCallingAScr = _MscAtmIfVptIispCallingAScr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 5)
)
_MscAtmIfVptIispCallingAScrRowStatusTable_Object = MibTable
mscAtmIfVptIispCallingAScrRowStatusTable = _MscAtmIfVptIispCallingAScrRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 5, 1)
)
if mibBuilder.loadTexts:
    mscAtmIfVptIispCallingAScrRowStatusTable.setStatus("mandatory")
_MscAtmIfVptIispCallingAScrRowStatusEntry_Object = MibTableRow
mscAtmIfVptIispCallingAScrRowStatusEntry = _MscAtmIfVptIispCallingAScrRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 5, 1, 1)
)
mscAtmIfVptIispCallingAScrRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVptIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmIispMIB", "mscAtmIfVptIispIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmIispMIB", "mscAtmIfVptIispCallingAScrIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfVptIispCallingAScrRowStatusEntry.setStatus("mandatory")
_MscAtmIfVptIispCallingAScrRowStatus_Type = RowStatus
_MscAtmIfVptIispCallingAScrRowStatus_Object = MibTableColumn
mscAtmIfVptIispCallingAScrRowStatus = _MscAtmIfVptIispCallingAScrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 5, 1, 1, 1),
    _MscAtmIfVptIispCallingAScrRowStatus_Type()
)
mscAtmIfVptIispCallingAScrRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVptIispCallingAScrRowStatus.setStatus("mandatory")
_MscAtmIfVptIispCallingAScrComponentName_Type = DisplayString
_MscAtmIfVptIispCallingAScrComponentName_Object = MibTableColumn
mscAtmIfVptIispCallingAScrComponentName = _MscAtmIfVptIispCallingAScrComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 5, 1, 1, 2),
    _MscAtmIfVptIispCallingAScrComponentName_Type()
)
mscAtmIfVptIispCallingAScrComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptIispCallingAScrComponentName.setStatus("mandatory")
_MscAtmIfVptIispCallingAScrStorageType_Type = StorageType
_MscAtmIfVptIispCallingAScrStorageType_Object = MibTableColumn
mscAtmIfVptIispCallingAScrStorageType = _MscAtmIfVptIispCallingAScrStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 5, 1, 1, 4),
    _MscAtmIfVptIispCallingAScrStorageType_Type()
)
mscAtmIfVptIispCallingAScrStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptIispCallingAScrStorageType.setStatus("mandatory")
_MscAtmIfVptIispCallingAScrIndex_Type = NonReplicated
_MscAtmIfVptIispCallingAScrIndex_Object = MibTableColumn
mscAtmIfVptIispCallingAScrIndex = _MscAtmIfVptIispCallingAScrIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 5, 1, 1, 10),
    _MscAtmIfVptIispCallingAScrIndex_Type()
)
mscAtmIfVptIispCallingAScrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAtmIfVptIispCallingAScrIndex.setStatus("mandatory")
_MscAtmIfVptIispCallingAScrAddr_ObjectIdentity = ObjectIdentity
mscAtmIfVptIispCallingAScrAddr = _MscAtmIfVptIispCallingAScrAddr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 5, 2)
)
_MscAtmIfVptIispCallingAScrAddrRowStatusTable_Object = MibTable
mscAtmIfVptIispCallingAScrAddrRowStatusTable = _MscAtmIfVptIispCallingAScrAddrRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 5, 2, 1)
)
if mibBuilder.loadTexts:
    mscAtmIfVptIispCallingAScrAddrRowStatusTable.setStatus("mandatory")
_MscAtmIfVptIispCallingAScrAddrRowStatusEntry_Object = MibTableRow
mscAtmIfVptIispCallingAScrAddrRowStatusEntry = _MscAtmIfVptIispCallingAScrAddrRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 5, 2, 1, 1)
)
mscAtmIfVptIispCallingAScrAddrRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVptIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmIispMIB", "mscAtmIfVptIispIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmIispMIB", "mscAtmIfVptIispCallingAScrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmIispMIB", "mscAtmIfVptIispCallingAScrAddrAddressIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmIispMIB", "mscAtmIfVptIispCallingAScrAddrAddressActionIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfVptIispCallingAScrAddrRowStatusEntry.setStatus("mandatory")
_MscAtmIfVptIispCallingAScrAddrRowStatus_Type = RowStatus
_MscAtmIfVptIispCallingAScrAddrRowStatus_Object = MibTableColumn
mscAtmIfVptIispCallingAScrAddrRowStatus = _MscAtmIfVptIispCallingAScrAddrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 5, 2, 1, 1, 1),
    _MscAtmIfVptIispCallingAScrAddrRowStatus_Type()
)
mscAtmIfVptIispCallingAScrAddrRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVptIispCallingAScrAddrRowStatus.setStatus("mandatory")
_MscAtmIfVptIispCallingAScrAddrComponentName_Type = DisplayString
_MscAtmIfVptIispCallingAScrAddrComponentName_Object = MibTableColumn
mscAtmIfVptIispCallingAScrAddrComponentName = _MscAtmIfVptIispCallingAScrAddrComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 5, 2, 1, 1, 2),
    _MscAtmIfVptIispCallingAScrAddrComponentName_Type()
)
mscAtmIfVptIispCallingAScrAddrComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptIispCallingAScrAddrComponentName.setStatus("mandatory")
_MscAtmIfVptIispCallingAScrAddrStorageType_Type = StorageType
_MscAtmIfVptIispCallingAScrAddrStorageType_Object = MibTableColumn
mscAtmIfVptIispCallingAScrAddrStorageType = _MscAtmIfVptIispCallingAScrAddrStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 5, 2, 1, 1, 4),
    _MscAtmIfVptIispCallingAScrAddrStorageType_Type()
)
mscAtmIfVptIispCallingAScrAddrStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptIispCallingAScrAddrStorageType.setStatus("mandatory")


class _MscAtmIfVptIispCallingAScrAddrAddressIndex_Type(AsciiStringIndex):
    """Custom type mscAtmIfVptIispCallingAScrAddrAddressIndex based on AsciiStringIndex"""
    subtypeSpec = AsciiStringIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_MscAtmIfVptIispCallingAScrAddrAddressIndex_Type.__name__ = "AsciiStringIndex"
_MscAtmIfVptIispCallingAScrAddrAddressIndex_Object = MibTableColumn
mscAtmIfVptIispCallingAScrAddrAddressIndex = _MscAtmIfVptIispCallingAScrAddrAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 5, 2, 1, 1, 10),
    _MscAtmIfVptIispCallingAScrAddrAddressIndex_Type()
)
mscAtmIfVptIispCallingAScrAddrAddressIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAtmIfVptIispCallingAScrAddrAddressIndex.setStatus("mandatory")


class _MscAtmIfVptIispCallingAScrAddrAddressActionIndex_Type(Integer32):
    """Custom type mscAtmIfVptIispCallingAScrAddrAddressActionIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("accept", 0),
          ("reject", 1))
    )


_MscAtmIfVptIispCallingAScrAddrAddressActionIndex_Type.__name__ = "Integer32"
_MscAtmIfVptIispCallingAScrAddrAddressActionIndex_Object = MibTableColumn
mscAtmIfVptIispCallingAScrAddrAddressActionIndex = _MscAtmIfVptIispCallingAScrAddrAddressActionIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 5, 2, 1, 1, 11),
    _MscAtmIfVptIispCallingAScrAddrAddressActionIndex_Type()
)
mscAtmIfVptIispCallingAScrAddrAddressActionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAtmIfVptIispCallingAScrAddrAddressActionIndex.setStatus("mandatory")
_MscAtmIfVptIispCallingAScrProvTable_Object = MibTable
mscAtmIfVptIispCallingAScrProvTable = _MscAtmIfVptIispCallingAScrProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 5, 10)
)
if mibBuilder.loadTexts:
    mscAtmIfVptIispCallingAScrProvTable.setStatus("mandatory")
_MscAtmIfVptIispCallingAScrProvEntry_Object = MibTableRow
mscAtmIfVptIispCallingAScrProvEntry = _MscAtmIfVptIispCallingAScrProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 5, 10, 1)
)
mscAtmIfVptIispCallingAScrProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVptIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmIispMIB", "mscAtmIfVptIispIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmIispMIB", "mscAtmIfVptIispCallingAScrIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfVptIispCallingAScrProvEntry.setStatus("mandatory")


class _MscAtmIfVptIispCallingAScrAdminStatus_Type(Integer32):
    """Custom type mscAtmIfVptIispCallingAScrAdminStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 0))
    )


_MscAtmIfVptIispCallingAScrAdminStatus_Type.__name__ = "Integer32"
_MscAtmIfVptIispCallingAScrAdminStatus_Object = MibTableColumn
mscAtmIfVptIispCallingAScrAdminStatus = _MscAtmIfVptIispCallingAScrAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 5, 10, 1, 1),
    _MscAtmIfVptIispCallingAScrAdminStatus_Type()
)
mscAtmIfVptIispCallingAScrAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVptIispCallingAScrAdminStatus.setStatus("mandatory")


class _MscAtmIfVptIispCallingAScrDefaultInsertionAddress_Type(HexString):
    """Custom type mscAtmIfVptIispCallingAScrDefaultInsertionAddress based on HexString"""
    defaultHexValue = ""

    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_MscAtmIfVptIispCallingAScrDefaultInsertionAddress_Type.__name__ = "HexString"
_MscAtmIfVptIispCallingAScrDefaultInsertionAddress_Object = MibTableColumn
mscAtmIfVptIispCallingAScrDefaultInsertionAddress = _MscAtmIfVptIispCallingAScrDefaultInsertionAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 5, 10, 1, 2),
    _MscAtmIfVptIispCallingAScrDefaultInsertionAddress_Type()
)
mscAtmIfVptIispCallingAScrDefaultInsertionAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVptIispCallingAScrDefaultInsertionAddress.setStatus("mandatory")
_MscAtmIfVptIispCallingAScrStatTable_Object = MibTable
mscAtmIfVptIispCallingAScrStatTable = _MscAtmIfVptIispCallingAScrStatTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 5, 11)
)
if mibBuilder.loadTexts:
    mscAtmIfVptIispCallingAScrStatTable.setStatus("mandatory")
_MscAtmIfVptIispCallingAScrStatEntry_Object = MibTableRow
mscAtmIfVptIispCallingAScrStatEntry = _MscAtmIfVptIispCallingAScrStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 5, 11, 1)
)
mscAtmIfVptIispCallingAScrStatEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVptIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmIispMIB", "mscAtmIfVptIispIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmIispMIB", "mscAtmIfVptIispCallingAScrIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfVptIispCallingAScrStatEntry.setStatus("mandatory")
_MscAtmIfVptIispCallingAScrAcceptedCalls_Type = Counter32
_MscAtmIfVptIispCallingAScrAcceptedCalls_Object = MibTableColumn
mscAtmIfVptIispCallingAScrAcceptedCalls = _MscAtmIfVptIispCallingAScrAcceptedCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 5, 11, 1, 1),
    _MscAtmIfVptIispCallingAScrAcceptedCalls_Type()
)
mscAtmIfVptIispCallingAScrAcceptedCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptIispCallingAScrAcceptedCalls.setStatus("mandatory")
_MscAtmIfVptIispCallingAScrRejectedCalls_Type = Counter32
_MscAtmIfVptIispCallingAScrRejectedCalls_Object = MibTableColumn
mscAtmIfVptIispCallingAScrRejectedCalls = _MscAtmIfVptIispCallingAScrRejectedCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 5, 11, 1, 2),
    _MscAtmIfVptIispCallingAScrRejectedCalls_Type()
)
mscAtmIfVptIispCallingAScrRejectedCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptIispCallingAScrRejectedCalls.setStatus("mandatory")
_MscAtmIfVptIispCallingAScrUnmatchedCalls_Type = Counter32
_MscAtmIfVptIispCallingAScrUnmatchedCalls_Object = MibTableColumn
mscAtmIfVptIispCallingAScrUnmatchedCalls = _MscAtmIfVptIispCallingAScrUnmatchedCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 5, 11, 1, 3),
    _MscAtmIfVptIispCallingAScrUnmatchedCalls_Type()
)
mscAtmIfVptIispCallingAScrUnmatchedCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptIispCallingAScrUnmatchedCalls.setStatus("mandatory")
_MscAtmIfVptIispCalledAScr_ObjectIdentity = ObjectIdentity
mscAtmIfVptIispCalledAScr = _MscAtmIfVptIispCalledAScr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 6)
)
_MscAtmIfVptIispCalledAScrRowStatusTable_Object = MibTable
mscAtmIfVptIispCalledAScrRowStatusTable = _MscAtmIfVptIispCalledAScrRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 6, 1)
)
if mibBuilder.loadTexts:
    mscAtmIfVptIispCalledAScrRowStatusTable.setStatus("mandatory")
_MscAtmIfVptIispCalledAScrRowStatusEntry_Object = MibTableRow
mscAtmIfVptIispCalledAScrRowStatusEntry = _MscAtmIfVptIispCalledAScrRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 6, 1, 1)
)
mscAtmIfVptIispCalledAScrRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVptIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmIispMIB", "mscAtmIfVptIispIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmIispMIB", "mscAtmIfVptIispCalledAScrIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfVptIispCalledAScrRowStatusEntry.setStatus("mandatory")
_MscAtmIfVptIispCalledAScrRowStatus_Type = RowStatus
_MscAtmIfVptIispCalledAScrRowStatus_Object = MibTableColumn
mscAtmIfVptIispCalledAScrRowStatus = _MscAtmIfVptIispCalledAScrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 6, 1, 1, 1),
    _MscAtmIfVptIispCalledAScrRowStatus_Type()
)
mscAtmIfVptIispCalledAScrRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVptIispCalledAScrRowStatus.setStatus("mandatory")
_MscAtmIfVptIispCalledAScrComponentName_Type = DisplayString
_MscAtmIfVptIispCalledAScrComponentName_Object = MibTableColumn
mscAtmIfVptIispCalledAScrComponentName = _MscAtmIfVptIispCalledAScrComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 6, 1, 1, 2),
    _MscAtmIfVptIispCalledAScrComponentName_Type()
)
mscAtmIfVptIispCalledAScrComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptIispCalledAScrComponentName.setStatus("mandatory")
_MscAtmIfVptIispCalledAScrStorageType_Type = StorageType
_MscAtmIfVptIispCalledAScrStorageType_Object = MibTableColumn
mscAtmIfVptIispCalledAScrStorageType = _MscAtmIfVptIispCalledAScrStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 6, 1, 1, 4),
    _MscAtmIfVptIispCalledAScrStorageType_Type()
)
mscAtmIfVptIispCalledAScrStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptIispCalledAScrStorageType.setStatus("mandatory")
_MscAtmIfVptIispCalledAScrIndex_Type = NonReplicated
_MscAtmIfVptIispCalledAScrIndex_Object = MibTableColumn
mscAtmIfVptIispCalledAScrIndex = _MscAtmIfVptIispCalledAScrIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 6, 1, 1, 10),
    _MscAtmIfVptIispCalledAScrIndex_Type()
)
mscAtmIfVptIispCalledAScrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAtmIfVptIispCalledAScrIndex.setStatus("mandatory")
_MscAtmIfVptIispCalledAScrAddr_ObjectIdentity = ObjectIdentity
mscAtmIfVptIispCalledAScrAddr = _MscAtmIfVptIispCalledAScrAddr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 6, 2)
)
_MscAtmIfVptIispCalledAScrAddrRowStatusTable_Object = MibTable
mscAtmIfVptIispCalledAScrAddrRowStatusTable = _MscAtmIfVptIispCalledAScrAddrRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 6, 2, 1)
)
if mibBuilder.loadTexts:
    mscAtmIfVptIispCalledAScrAddrRowStatusTable.setStatus("mandatory")
_MscAtmIfVptIispCalledAScrAddrRowStatusEntry_Object = MibTableRow
mscAtmIfVptIispCalledAScrAddrRowStatusEntry = _MscAtmIfVptIispCalledAScrAddrRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 6, 2, 1, 1)
)
mscAtmIfVptIispCalledAScrAddrRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVptIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmIispMIB", "mscAtmIfVptIispIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmIispMIB", "mscAtmIfVptIispCalledAScrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmIispMIB", "mscAtmIfVptIispCalledAScrAddrAddressIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmIispMIB", "mscAtmIfVptIispCalledAScrAddrAddressActionIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfVptIispCalledAScrAddrRowStatusEntry.setStatus("mandatory")
_MscAtmIfVptIispCalledAScrAddrRowStatus_Type = RowStatus
_MscAtmIfVptIispCalledAScrAddrRowStatus_Object = MibTableColumn
mscAtmIfVptIispCalledAScrAddrRowStatus = _MscAtmIfVptIispCalledAScrAddrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 6, 2, 1, 1, 1),
    _MscAtmIfVptIispCalledAScrAddrRowStatus_Type()
)
mscAtmIfVptIispCalledAScrAddrRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVptIispCalledAScrAddrRowStatus.setStatus("mandatory")
_MscAtmIfVptIispCalledAScrAddrComponentName_Type = DisplayString
_MscAtmIfVptIispCalledAScrAddrComponentName_Object = MibTableColumn
mscAtmIfVptIispCalledAScrAddrComponentName = _MscAtmIfVptIispCalledAScrAddrComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 6, 2, 1, 1, 2),
    _MscAtmIfVptIispCalledAScrAddrComponentName_Type()
)
mscAtmIfVptIispCalledAScrAddrComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptIispCalledAScrAddrComponentName.setStatus("mandatory")
_MscAtmIfVptIispCalledAScrAddrStorageType_Type = StorageType
_MscAtmIfVptIispCalledAScrAddrStorageType_Object = MibTableColumn
mscAtmIfVptIispCalledAScrAddrStorageType = _MscAtmIfVptIispCalledAScrAddrStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 6, 2, 1, 1, 4),
    _MscAtmIfVptIispCalledAScrAddrStorageType_Type()
)
mscAtmIfVptIispCalledAScrAddrStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptIispCalledAScrAddrStorageType.setStatus("mandatory")


class _MscAtmIfVptIispCalledAScrAddrAddressIndex_Type(AsciiStringIndex):
    """Custom type mscAtmIfVptIispCalledAScrAddrAddressIndex based on AsciiStringIndex"""
    subtypeSpec = AsciiStringIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_MscAtmIfVptIispCalledAScrAddrAddressIndex_Type.__name__ = "AsciiStringIndex"
_MscAtmIfVptIispCalledAScrAddrAddressIndex_Object = MibTableColumn
mscAtmIfVptIispCalledAScrAddrAddressIndex = _MscAtmIfVptIispCalledAScrAddrAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 6, 2, 1, 1, 10),
    _MscAtmIfVptIispCalledAScrAddrAddressIndex_Type()
)
mscAtmIfVptIispCalledAScrAddrAddressIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAtmIfVptIispCalledAScrAddrAddressIndex.setStatus("mandatory")


class _MscAtmIfVptIispCalledAScrAddrAddressActionIndex_Type(Integer32):
    """Custom type mscAtmIfVptIispCalledAScrAddrAddressActionIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("accept", 0),
          ("reject", 1))
    )


_MscAtmIfVptIispCalledAScrAddrAddressActionIndex_Type.__name__ = "Integer32"
_MscAtmIfVptIispCalledAScrAddrAddressActionIndex_Object = MibTableColumn
mscAtmIfVptIispCalledAScrAddrAddressActionIndex = _MscAtmIfVptIispCalledAScrAddrAddressActionIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 6, 2, 1, 1, 11),
    _MscAtmIfVptIispCalledAScrAddrAddressActionIndex_Type()
)
mscAtmIfVptIispCalledAScrAddrAddressActionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAtmIfVptIispCalledAScrAddrAddressActionIndex.setStatus("mandatory")
_MscAtmIfVptIispCalledAScrProvTable_Object = MibTable
mscAtmIfVptIispCalledAScrProvTable = _MscAtmIfVptIispCalledAScrProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 6, 10)
)
if mibBuilder.loadTexts:
    mscAtmIfVptIispCalledAScrProvTable.setStatus("mandatory")
_MscAtmIfVptIispCalledAScrProvEntry_Object = MibTableRow
mscAtmIfVptIispCalledAScrProvEntry = _MscAtmIfVptIispCalledAScrProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 6, 10, 1)
)
mscAtmIfVptIispCalledAScrProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVptIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmIispMIB", "mscAtmIfVptIispIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmIispMIB", "mscAtmIfVptIispCalledAScrIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfVptIispCalledAScrProvEntry.setStatus("mandatory")


class _MscAtmIfVptIispCalledAScrAdminStatus_Type(Integer32):
    """Custom type mscAtmIfVptIispCalledAScrAdminStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 0))
    )


_MscAtmIfVptIispCalledAScrAdminStatus_Type.__name__ = "Integer32"
_MscAtmIfVptIispCalledAScrAdminStatus_Object = MibTableColumn
mscAtmIfVptIispCalledAScrAdminStatus = _MscAtmIfVptIispCalledAScrAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 6, 10, 1, 1),
    _MscAtmIfVptIispCalledAScrAdminStatus_Type()
)
mscAtmIfVptIispCalledAScrAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVptIispCalledAScrAdminStatus.setStatus("mandatory")
_MscAtmIfVptIispCalledAScrStatTable_Object = MibTable
mscAtmIfVptIispCalledAScrStatTable = _MscAtmIfVptIispCalledAScrStatTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 6, 11)
)
if mibBuilder.loadTexts:
    mscAtmIfVptIispCalledAScrStatTable.setStatus("mandatory")
_MscAtmIfVptIispCalledAScrStatEntry_Object = MibTableRow
mscAtmIfVptIispCalledAScrStatEntry = _MscAtmIfVptIispCalledAScrStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 6, 11, 1)
)
mscAtmIfVptIispCalledAScrStatEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVptIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmIispMIB", "mscAtmIfVptIispIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmIispMIB", "mscAtmIfVptIispCalledAScrIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfVptIispCalledAScrStatEntry.setStatus("mandatory")
_MscAtmIfVptIispCalledAScrAcceptedCalls_Type = Counter32
_MscAtmIfVptIispCalledAScrAcceptedCalls_Object = MibTableColumn
mscAtmIfVptIispCalledAScrAcceptedCalls = _MscAtmIfVptIispCalledAScrAcceptedCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 6, 11, 1, 1),
    _MscAtmIfVptIispCalledAScrAcceptedCalls_Type()
)
mscAtmIfVptIispCalledAScrAcceptedCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptIispCalledAScrAcceptedCalls.setStatus("mandatory")
_MscAtmIfVptIispCalledAScrRejectedCalls_Type = Counter32
_MscAtmIfVptIispCalledAScrRejectedCalls_Object = MibTableColumn
mscAtmIfVptIispCalledAScrRejectedCalls = _MscAtmIfVptIispCalledAScrRejectedCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 6, 11, 1, 2),
    _MscAtmIfVptIispCalledAScrRejectedCalls_Type()
)
mscAtmIfVptIispCalledAScrRejectedCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptIispCalledAScrRejectedCalls.setStatus("mandatory")
_MscAtmIfVptIispCalledAScrUnmatchedCalls_Type = Counter32
_MscAtmIfVptIispCalledAScrUnmatchedCalls_Object = MibTableColumn
mscAtmIfVptIispCalledAScrUnmatchedCalls = _MscAtmIfVptIispCalledAScrUnmatchedCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 6, 11, 1, 3),
    _MscAtmIfVptIispCalledAScrUnmatchedCalls_Type()
)
mscAtmIfVptIispCalledAScrUnmatchedCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptIispCalledAScrUnmatchedCalls.setStatus("mandatory")
_MscAtmIfVptIispProvTable_Object = MibTable
mscAtmIfVptIispProvTable = _MscAtmIfVptIispProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 10)
)
if mibBuilder.loadTexts:
    mscAtmIfVptIispProvTable.setStatus("mandatory")
_MscAtmIfVptIispProvEntry_Object = MibTableRow
mscAtmIfVptIispProvEntry = _MscAtmIfVptIispProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 10, 1)
)
mscAtmIfVptIispProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVptIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmIispMIB", "mscAtmIfVptIispIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfVptIispProvEntry.setStatus("mandatory")


class _MscAtmIfVptIispVersion_Type(Integer32):
    """Custom type mscAtmIfVptIispVersion based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("iisp10Sig30", 2),
          ("iisp10Sig31", 3))
    )


_MscAtmIfVptIispVersion_Type.__name__ = "Integer32"
_MscAtmIfVptIispVersion_Object = MibTableColumn
mscAtmIfVptIispVersion = _MscAtmIfVptIispVersion_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 10, 1, 1),
    _MscAtmIfVptIispVersion_Type()
)
mscAtmIfVptIispVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVptIispVersion.setStatus("mandatory")


class _MscAtmIfVptIispSide_Type(Integer32):
    """Custom type mscAtmIfVptIispSide based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("networkSide", 0),
          ("userSide", 1))
    )


_MscAtmIfVptIispSide_Type.__name__ = "Integer32"
_MscAtmIfVptIispSide_Object = MibTableColumn
mscAtmIfVptIispSide = _MscAtmIfVptIispSide_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 10, 1, 2),
    _MscAtmIfVptIispSide_Type()
)
mscAtmIfVptIispSide.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVptIispSide.setStatus("mandatory")


class _MscAtmIfVptIispSoftPvcRetryPeriod_Type(Unsigned32):
    """Custom type mscAtmIfVptIispSoftPvcRetryPeriod based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 999999),
    )


_MscAtmIfVptIispSoftPvcRetryPeriod_Type.__name__ = "Unsigned32"
_MscAtmIfVptIispSoftPvcRetryPeriod_Object = MibTableColumn
mscAtmIfVptIispSoftPvcRetryPeriod = _MscAtmIfVptIispSoftPvcRetryPeriod_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 10, 1, 3),
    _MscAtmIfVptIispSoftPvcRetryPeriod_Type()
)
mscAtmIfVptIispSoftPvcRetryPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVptIispSoftPvcRetryPeriod.setStatus("obsolete")


class _MscAtmIfVptIispSoftPvpAndPvcRetryPeriod_Type(Unsigned32):
    """Custom type mscAtmIfVptIispSoftPvpAndPvcRetryPeriod based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 999999),
    )


_MscAtmIfVptIispSoftPvpAndPvcRetryPeriod_Type.__name__ = "Unsigned32"
_MscAtmIfVptIispSoftPvpAndPvcRetryPeriod_Object = MibTableColumn
mscAtmIfVptIispSoftPvpAndPvcRetryPeriod = _MscAtmIfVptIispSoftPvpAndPvcRetryPeriod_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 10, 1, 4),
    _MscAtmIfVptIispSoftPvpAndPvcRetryPeriod_Type()
)
mscAtmIfVptIispSoftPvpAndPvcRetryPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVptIispSoftPvpAndPvcRetryPeriod.setStatus("mandatory")


class _MscAtmIfVptIispSoftPvpAndPvcHoldOffTime_Type(Unsigned32):
    """Custom type mscAtmIfVptIispSoftPvpAndPvcHoldOffTime based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(50, 20000),
    )


_MscAtmIfVptIispSoftPvpAndPvcHoldOffTime_Type.__name__ = "Unsigned32"
_MscAtmIfVptIispSoftPvpAndPvcHoldOffTime_Object = MibTableColumn
mscAtmIfVptIispSoftPvpAndPvcHoldOffTime = _MscAtmIfVptIispSoftPvpAndPvcHoldOffTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 10, 1, 5),
    _MscAtmIfVptIispSoftPvpAndPvcHoldOffTime_Type()
)
mscAtmIfVptIispSoftPvpAndPvcHoldOffTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVptIispSoftPvpAndPvcHoldOffTime.setStatus("mandatory")
_MscAtmIfVptIispAcctOptTable_Object = MibTable
mscAtmIfVptIispAcctOptTable = _MscAtmIfVptIispAcctOptTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 11)
)
if mibBuilder.loadTexts:
    mscAtmIfVptIispAcctOptTable.setStatus("mandatory")
_MscAtmIfVptIispAcctOptEntry_Object = MibTableRow
mscAtmIfVptIispAcctOptEntry = _MscAtmIfVptIispAcctOptEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 11, 1)
)
mscAtmIfVptIispAcctOptEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVptIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmIispMIB", "mscAtmIfVptIispIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfVptIispAcctOptEntry.setStatus("mandatory")


class _MscAtmIfVptIispAccountCollection_Type(OctetString):
    """Custom type mscAtmIfVptIispAccountCollection based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscAtmIfVptIispAccountCollection_Type.__name__ = "OctetString"
_MscAtmIfVptIispAccountCollection_Object = MibTableColumn
mscAtmIfVptIispAccountCollection = _MscAtmIfVptIispAccountCollection_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 11, 1, 1),
    _MscAtmIfVptIispAccountCollection_Type()
)
mscAtmIfVptIispAccountCollection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVptIispAccountCollection.setStatus("mandatory")


class _MscAtmIfVptIispAccountConnectionType_Type(Integer32):
    """Custom type mscAtmIfVptIispAccountConnectionType based on Integer32"""
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


_MscAtmIfVptIispAccountConnectionType_Type.__name__ = "Integer32"
_MscAtmIfVptIispAccountConnectionType_Object = MibTableColumn
mscAtmIfVptIispAccountConnectionType = _MscAtmIfVptIispAccountConnectionType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 11, 1, 2),
    _MscAtmIfVptIispAccountConnectionType_Type()
)
mscAtmIfVptIispAccountConnectionType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVptIispAccountConnectionType.setStatus("mandatory")


class _MscAtmIfVptIispAccountClass_Type(Unsigned32):
    """Custom type mscAtmIfVptIispAccountClass based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscAtmIfVptIispAccountClass_Type.__name__ = "Unsigned32"
_MscAtmIfVptIispAccountClass_Object = MibTableColumn
mscAtmIfVptIispAccountClass = _MscAtmIfVptIispAccountClass_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 11, 1, 3),
    _MscAtmIfVptIispAccountClass_Type()
)
mscAtmIfVptIispAccountClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVptIispAccountClass.setStatus("mandatory")


class _MscAtmIfVptIispServiceExchange_Type(Unsigned32):
    """Custom type mscAtmIfVptIispServiceExchange based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscAtmIfVptIispServiceExchange_Type.__name__ = "Unsigned32"
_MscAtmIfVptIispServiceExchange_Object = MibTableColumn
mscAtmIfVptIispServiceExchange = _MscAtmIfVptIispServiceExchange_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 11, 1, 4),
    _MscAtmIfVptIispServiceExchange_Type()
)
mscAtmIfVptIispServiceExchange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVptIispServiceExchange.setStatus("mandatory")
_MscAtmIfVptIispVProvTable_Object = MibTable
mscAtmIfVptIispVProvTable = _MscAtmIfVptIispVProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 12)
)
if mibBuilder.loadTexts:
    mscAtmIfVptIispVProvTable.setStatus("mandatory")
_MscAtmIfVptIispVProvEntry_Object = MibTableRow
mscAtmIfVptIispVProvEntry = _MscAtmIfVptIispVProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 12, 1)
)
mscAtmIfVptIispVProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVptIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmIispMIB", "mscAtmIfVptIispIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfVptIispVProvEntry.setStatus("mandatory")


class _MscAtmIfVptIispVpci_Type(Unsigned32):
    """Custom type mscAtmIfVptIispVpci based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscAtmIfVptIispVpci_Type.__name__ = "Unsigned32"
_MscAtmIfVptIispVpci_Object = MibTableColumn
mscAtmIfVptIispVpci = _MscAtmIfVptIispVpci_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 6, 12, 1, 1),
    _MscAtmIfVptIispVpci_Type()
)
mscAtmIfVptIispVpci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVptIispVpci.setStatus("mandatory")
_AtmIispMIB_ObjectIdentity = ObjectIdentity
atmIispMIB = _AtmIispMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 70)
)
_AtmIispGroup_ObjectIdentity = ObjectIdentity
atmIispGroup = _AtmIispGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 70, 1)
)
_AtmIispGroupCA_ObjectIdentity = ObjectIdentity
atmIispGroupCA = _AtmIispGroupCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 70, 1, 1)
)
_AtmIispGroupCA02_ObjectIdentity = ObjectIdentity
atmIispGroupCA02 = _AtmIispGroupCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 70, 1, 1, 3)
)
_AtmIispGroupCA02A_ObjectIdentity = ObjectIdentity
atmIispGroupCA02A = _AtmIispGroupCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 70, 1, 1, 3, 2)
)
_AtmIispCapabilities_ObjectIdentity = ObjectIdentity
atmIispCapabilities = _AtmIispCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 70, 3)
)
_AtmIispCapabilitiesCA_ObjectIdentity = ObjectIdentity
atmIispCapabilitiesCA = _AtmIispCapabilitiesCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 70, 3, 1)
)
_AtmIispCapabilitiesCA02_ObjectIdentity = ObjectIdentity
atmIispCapabilitiesCA02 = _AtmIispCapabilitiesCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 70, 3, 1, 3)
)
_AtmIispCapabilitiesCA02A_ObjectIdentity = ObjectIdentity
atmIispCapabilitiesCA02A = _AtmIispCapabilitiesCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 70, 3, 1, 3, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-MsCarrier-MscPassport-AtmIispMIB",
    **{"mscAtmIfIisp": mscAtmIfIisp,
       "mscAtmIfIispRowStatusTable": mscAtmIfIispRowStatusTable,
       "mscAtmIfIispRowStatusEntry": mscAtmIfIispRowStatusEntry,
       "mscAtmIfIispRowStatus": mscAtmIfIispRowStatus,
       "mscAtmIfIispComponentName": mscAtmIfIispComponentName,
       "mscAtmIfIispStorageType": mscAtmIfIispStorageType,
       "mscAtmIfIispIndex": mscAtmIfIispIndex,
       "mscAtmIfIispSig": mscAtmIfIispSig,
       "mscAtmIfIispSigRowStatusTable": mscAtmIfIispSigRowStatusTable,
       "mscAtmIfIispSigRowStatusEntry": mscAtmIfIispSigRowStatusEntry,
       "mscAtmIfIispSigRowStatus": mscAtmIfIispSigRowStatus,
       "mscAtmIfIispSigComponentName": mscAtmIfIispSigComponentName,
       "mscAtmIfIispSigStorageType": mscAtmIfIispSigStorageType,
       "mscAtmIfIispSigIndex": mscAtmIfIispSigIndex,
       "mscAtmIfIispSigVcd": mscAtmIfIispSigVcd,
       "mscAtmIfIispSigVcdRowStatusTable": mscAtmIfIispSigVcdRowStatusTable,
       "mscAtmIfIispSigVcdRowStatusEntry": mscAtmIfIispSigVcdRowStatusEntry,
       "mscAtmIfIispSigVcdRowStatus": mscAtmIfIispSigVcdRowStatus,
       "mscAtmIfIispSigVcdComponentName": mscAtmIfIispSigVcdComponentName,
       "mscAtmIfIispSigVcdStorageType": mscAtmIfIispSigVcdStorageType,
       "mscAtmIfIispSigVcdIndex": mscAtmIfIispSigVcdIndex,
       "mscAtmIfIispSigVcdProvTable": mscAtmIfIispSigVcdProvTable,
       "mscAtmIfIispSigVcdProvEntry": mscAtmIfIispSigVcdProvEntry,
       "mscAtmIfIispSigVcdTrafficDescType": mscAtmIfIispSigVcdTrafficDescType,
       "mscAtmIfIispSigVcdAtmServiceCategory": mscAtmIfIispSigVcdAtmServiceCategory,
       "mscAtmIfIispSigVcdWeight": mscAtmIfIispSigVcdWeight,
       "mscAtmIfIispSigVcdQosClass": mscAtmIfIispSigVcdQosClass,
       "mscAtmIfIispSigVcdTrafficShaping": mscAtmIfIispSigVcdTrafficShaping,
       "mscAtmIfIispSigVcdUnshapedTransmitQueueing": mscAtmIfIispSigVcdUnshapedTransmitQueueing,
       "mscAtmIfIispSigVcdUsageParameterControl": mscAtmIfIispSigVcdUsageParameterControl,
       "mscAtmIfIispSigVcdTdpTable": mscAtmIfIispSigVcdTdpTable,
       "mscAtmIfIispSigVcdTdpEntry": mscAtmIfIispSigVcdTdpEntry,
       "mscAtmIfIispSigVcdTdpIndex": mscAtmIfIispSigVcdTdpIndex,
       "mscAtmIfIispSigVcdTdpValue": mscAtmIfIispSigVcdTdpValue,
       "mscAtmIfIispSigProvTable": mscAtmIfIispSigProvTable,
       "mscAtmIfIispSigProvEntry": mscAtmIfIispSigProvEntry,
       "mscAtmIfIispSigVci": mscAtmIfIispSigVci,
       "mscAtmIfIispSigAddressConversion": mscAtmIfIispSigAddressConversion,
       "mscAtmIfIispSigOperatingMode": mscAtmIfIispSigOperatingMode,
       "mscAtmIfIispSigStateTable": mscAtmIfIispSigStateTable,
       "mscAtmIfIispSigStateEntry": mscAtmIfIispSigStateEntry,
       "mscAtmIfIispSigAdminState": mscAtmIfIispSigAdminState,
       "mscAtmIfIispSigOperationalState": mscAtmIfIispSigOperationalState,
       "mscAtmIfIispSigUsageState": mscAtmIfIispSigUsageState,
       "mscAtmIfIispSigOperTable": mscAtmIfIispSigOperTable,
       "mscAtmIfIispSigOperEntry": mscAtmIfIispSigOperEntry,
       "mscAtmIfIispSigLastTxCauseCode": mscAtmIfIispSigLastTxCauseCode,
       "mscAtmIfIispSigLastTxDiagCode": mscAtmIfIispSigLastTxDiagCode,
       "mscAtmIfIispSigLastRxCauseCode": mscAtmIfIispSigLastRxCauseCode,
       "mscAtmIfIispSigLastRxDiagCode": mscAtmIfIispSigLastRxDiagCode,
       "mscAtmIfIispSigStatsTable": mscAtmIfIispSigStatsTable,
       "mscAtmIfIispSigStatsEntry": mscAtmIfIispSigStatsEntry,
       "mscAtmIfIispSigCurrentConnections": mscAtmIfIispSigCurrentConnections,
       "mscAtmIfIispSigPeakConnections": mscAtmIfIispSigPeakConnections,
       "mscAtmIfIispSigSuccessfulConnections": mscAtmIfIispSigSuccessfulConnections,
       "mscAtmIfIispSigFailedConnections": mscAtmIfIispSigFailedConnections,
       "mscAtmIfIispSigTxPdus": mscAtmIfIispSigTxPdus,
       "mscAtmIfIispSigRxPdus": mscAtmIfIispSigRxPdus,
       "mscAtmIfIispSigCurrentPmpConnections": mscAtmIfIispSigCurrentPmpConnections,
       "mscAtmIfIispSigPeakPmpConnections": mscAtmIfIispSigPeakPmpConnections,
       "mscAtmIfIispSigSuccessfulPmpConnections": mscAtmIfIispSigSuccessfulPmpConnections,
       "mscAtmIfIispSigFailedPmpConnections": mscAtmIfIispSigFailedPmpConnections,
       "mscAtmIfIispSigNewCurrentConnections": mscAtmIfIispSigNewCurrentConnections,
       "mscAtmIfIispAddr": mscAtmIfIispAddr,
       "mscAtmIfIispAddrRowStatusTable": mscAtmIfIispAddrRowStatusTable,
       "mscAtmIfIispAddrRowStatusEntry": mscAtmIfIispAddrRowStatusEntry,
       "mscAtmIfIispAddrRowStatus": mscAtmIfIispAddrRowStatus,
       "mscAtmIfIispAddrComponentName": mscAtmIfIispAddrComponentName,
       "mscAtmIfIispAddrStorageType": mscAtmIfIispAddrStorageType,
       "mscAtmIfIispAddrAddressIndex": mscAtmIfIispAddrAddressIndex,
       "mscAtmIfIispAddrAddressTypeIndex": mscAtmIfIispAddrAddressTypeIndex,
       "mscAtmIfIispAddrTermSP": mscAtmIfIispAddrTermSP,
       "mscAtmIfIispAddrTermSPRowStatusTable": mscAtmIfIispAddrTermSPRowStatusTable,
       "mscAtmIfIispAddrTermSPRowStatusEntry": mscAtmIfIispAddrTermSPRowStatusEntry,
       "mscAtmIfIispAddrTermSPRowStatus": mscAtmIfIispAddrTermSPRowStatus,
       "mscAtmIfIispAddrTermSPComponentName": mscAtmIfIispAddrTermSPComponentName,
       "mscAtmIfIispAddrTermSPStorageType": mscAtmIfIispAddrTermSPStorageType,
       "mscAtmIfIispAddrTermSPIndex": mscAtmIfIispAddrTermSPIndex,
       "mscAtmIfIispAddrPnniInfo": mscAtmIfIispAddrPnniInfo,
       "mscAtmIfIispAddrPnniInfoRowStatusTable": mscAtmIfIispAddrPnniInfoRowStatusTable,
       "mscAtmIfIispAddrPnniInfoRowStatusEntry": mscAtmIfIispAddrPnniInfoRowStatusEntry,
       "mscAtmIfIispAddrPnniInfoRowStatus": mscAtmIfIispAddrPnniInfoRowStatus,
       "mscAtmIfIispAddrPnniInfoComponentName": mscAtmIfIispAddrPnniInfoComponentName,
       "mscAtmIfIispAddrPnniInfoStorageType": mscAtmIfIispAddrPnniInfoStorageType,
       "mscAtmIfIispAddrPnniInfoIndex": mscAtmIfIispAddrPnniInfoIndex,
       "mscAtmIfIispAddrPnniInfoProvTable": mscAtmIfIispAddrPnniInfoProvTable,
       "mscAtmIfIispAddrPnniInfoProvEntry": mscAtmIfIispAddrPnniInfoProvEntry,
       "mscAtmIfIispAddrPnniInfoScope": mscAtmIfIispAddrPnniInfoScope,
       "mscAtmIfIispAddrPnniInfoReachability": mscAtmIfIispAddrPnniInfoReachability,
       "mscAtmIfIispAddrOperTable": mscAtmIfIispAddrOperTable,
       "mscAtmIfIispAddrOperEntry": mscAtmIfIispAddrOperEntry,
       "mscAtmIfIispAddrScope": mscAtmIfIispAddrScope,
       "mscAtmIfIispAddrReachability": mscAtmIfIispAddrReachability,
       "mscAtmIfIispCallingAScr": mscAtmIfIispCallingAScr,
       "mscAtmIfIispCallingAScrRowStatusTable": mscAtmIfIispCallingAScrRowStatusTable,
       "mscAtmIfIispCallingAScrRowStatusEntry": mscAtmIfIispCallingAScrRowStatusEntry,
       "mscAtmIfIispCallingAScrRowStatus": mscAtmIfIispCallingAScrRowStatus,
       "mscAtmIfIispCallingAScrComponentName": mscAtmIfIispCallingAScrComponentName,
       "mscAtmIfIispCallingAScrStorageType": mscAtmIfIispCallingAScrStorageType,
       "mscAtmIfIispCallingAScrIndex": mscAtmIfIispCallingAScrIndex,
       "mscAtmIfIispCallingAScrAddr": mscAtmIfIispCallingAScrAddr,
       "mscAtmIfIispCallingAScrAddrRowStatusTable": mscAtmIfIispCallingAScrAddrRowStatusTable,
       "mscAtmIfIispCallingAScrAddrRowStatusEntry": mscAtmIfIispCallingAScrAddrRowStatusEntry,
       "mscAtmIfIispCallingAScrAddrRowStatus": mscAtmIfIispCallingAScrAddrRowStatus,
       "mscAtmIfIispCallingAScrAddrComponentName": mscAtmIfIispCallingAScrAddrComponentName,
       "mscAtmIfIispCallingAScrAddrStorageType": mscAtmIfIispCallingAScrAddrStorageType,
       "mscAtmIfIispCallingAScrAddrAddressIndex": mscAtmIfIispCallingAScrAddrAddressIndex,
       "mscAtmIfIispCallingAScrAddrAddressActionIndex": mscAtmIfIispCallingAScrAddrAddressActionIndex,
       "mscAtmIfIispCallingAScrProvTable": mscAtmIfIispCallingAScrProvTable,
       "mscAtmIfIispCallingAScrProvEntry": mscAtmIfIispCallingAScrProvEntry,
       "mscAtmIfIispCallingAScrAdminStatus": mscAtmIfIispCallingAScrAdminStatus,
       "mscAtmIfIispCallingAScrDefaultInsertionAddress": mscAtmIfIispCallingAScrDefaultInsertionAddress,
       "mscAtmIfIispCallingAScrStatTable": mscAtmIfIispCallingAScrStatTable,
       "mscAtmIfIispCallingAScrStatEntry": mscAtmIfIispCallingAScrStatEntry,
       "mscAtmIfIispCallingAScrAcceptedCalls": mscAtmIfIispCallingAScrAcceptedCalls,
       "mscAtmIfIispCallingAScrRejectedCalls": mscAtmIfIispCallingAScrRejectedCalls,
       "mscAtmIfIispCallingAScrUnmatchedCalls": mscAtmIfIispCallingAScrUnmatchedCalls,
       "mscAtmIfIispCalledAScr": mscAtmIfIispCalledAScr,
       "mscAtmIfIispCalledAScrRowStatusTable": mscAtmIfIispCalledAScrRowStatusTable,
       "mscAtmIfIispCalledAScrRowStatusEntry": mscAtmIfIispCalledAScrRowStatusEntry,
       "mscAtmIfIispCalledAScrRowStatus": mscAtmIfIispCalledAScrRowStatus,
       "mscAtmIfIispCalledAScrComponentName": mscAtmIfIispCalledAScrComponentName,
       "mscAtmIfIispCalledAScrStorageType": mscAtmIfIispCalledAScrStorageType,
       "mscAtmIfIispCalledAScrIndex": mscAtmIfIispCalledAScrIndex,
       "mscAtmIfIispCalledAScrAddr": mscAtmIfIispCalledAScrAddr,
       "mscAtmIfIispCalledAScrAddrRowStatusTable": mscAtmIfIispCalledAScrAddrRowStatusTable,
       "mscAtmIfIispCalledAScrAddrRowStatusEntry": mscAtmIfIispCalledAScrAddrRowStatusEntry,
       "mscAtmIfIispCalledAScrAddrRowStatus": mscAtmIfIispCalledAScrAddrRowStatus,
       "mscAtmIfIispCalledAScrAddrComponentName": mscAtmIfIispCalledAScrAddrComponentName,
       "mscAtmIfIispCalledAScrAddrStorageType": mscAtmIfIispCalledAScrAddrStorageType,
       "mscAtmIfIispCalledAScrAddrAddressIndex": mscAtmIfIispCalledAScrAddrAddressIndex,
       "mscAtmIfIispCalledAScrAddrAddressActionIndex": mscAtmIfIispCalledAScrAddrAddressActionIndex,
       "mscAtmIfIispCalledAScrProvTable": mscAtmIfIispCalledAScrProvTable,
       "mscAtmIfIispCalledAScrProvEntry": mscAtmIfIispCalledAScrProvEntry,
       "mscAtmIfIispCalledAScrAdminStatus": mscAtmIfIispCalledAScrAdminStatus,
       "mscAtmIfIispCalledAScrStatTable": mscAtmIfIispCalledAScrStatTable,
       "mscAtmIfIispCalledAScrStatEntry": mscAtmIfIispCalledAScrStatEntry,
       "mscAtmIfIispCalledAScrAcceptedCalls": mscAtmIfIispCalledAScrAcceptedCalls,
       "mscAtmIfIispCalledAScrRejectedCalls": mscAtmIfIispCalledAScrRejectedCalls,
       "mscAtmIfIispCalledAScrUnmatchedCalls": mscAtmIfIispCalledAScrUnmatchedCalls,
       "mscAtmIfIispProvTable": mscAtmIfIispProvTable,
       "mscAtmIfIispProvEntry": mscAtmIfIispProvEntry,
       "mscAtmIfIispVersion": mscAtmIfIispVersion,
       "mscAtmIfIispSide": mscAtmIfIispSide,
       "mscAtmIfIispSoftPvcRetryPeriod": mscAtmIfIispSoftPvcRetryPeriod,
       "mscAtmIfIispSoftPvpAndPvcRetryPeriod": mscAtmIfIispSoftPvpAndPvcRetryPeriod,
       "mscAtmIfIispSoftPvpAndPvcHoldOffTime": mscAtmIfIispSoftPvpAndPvcHoldOffTime,
       "mscAtmIfIispAcctOptTable": mscAtmIfIispAcctOptTable,
       "mscAtmIfIispAcctOptEntry": mscAtmIfIispAcctOptEntry,
       "mscAtmIfIispAccountCollection": mscAtmIfIispAccountCollection,
       "mscAtmIfIispAccountConnectionType": mscAtmIfIispAccountConnectionType,
       "mscAtmIfIispAccountClass": mscAtmIfIispAccountClass,
       "mscAtmIfIispServiceExchange": mscAtmIfIispServiceExchange,
       "mscAtmIfVptIisp": mscAtmIfVptIisp,
       "mscAtmIfVptIispRowStatusTable": mscAtmIfVptIispRowStatusTable,
       "mscAtmIfVptIispRowStatusEntry": mscAtmIfVptIispRowStatusEntry,
       "mscAtmIfVptIispRowStatus": mscAtmIfVptIispRowStatus,
       "mscAtmIfVptIispComponentName": mscAtmIfVptIispComponentName,
       "mscAtmIfVptIispStorageType": mscAtmIfVptIispStorageType,
       "mscAtmIfVptIispIndex": mscAtmIfVptIispIndex,
       "mscAtmIfVptIispSig": mscAtmIfVptIispSig,
       "mscAtmIfVptIispSigRowStatusTable": mscAtmIfVptIispSigRowStatusTable,
       "mscAtmIfVptIispSigRowStatusEntry": mscAtmIfVptIispSigRowStatusEntry,
       "mscAtmIfVptIispSigRowStatus": mscAtmIfVptIispSigRowStatus,
       "mscAtmIfVptIispSigComponentName": mscAtmIfVptIispSigComponentName,
       "mscAtmIfVptIispSigStorageType": mscAtmIfVptIispSigStorageType,
       "mscAtmIfVptIispSigIndex": mscAtmIfVptIispSigIndex,
       "mscAtmIfVptIispSigVcd": mscAtmIfVptIispSigVcd,
       "mscAtmIfVptIispSigVcdRowStatusTable": mscAtmIfVptIispSigVcdRowStatusTable,
       "mscAtmIfVptIispSigVcdRowStatusEntry": mscAtmIfVptIispSigVcdRowStatusEntry,
       "mscAtmIfVptIispSigVcdRowStatus": mscAtmIfVptIispSigVcdRowStatus,
       "mscAtmIfVptIispSigVcdComponentName": mscAtmIfVptIispSigVcdComponentName,
       "mscAtmIfVptIispSigVcdStorageType": mscAtmIfVptIispSigVcdStorageType,
       "mscAtmIfVptIispSigVcdIndex": mscAtmIfVptIispSigVcdIndex,
       "mscAtmIfVptIispSigVcdProvTable": mscAtmIfVptIispSigVcdProvTable,
       "mscAtmIfVptIispSigVcdProvEntry": mscAtmIfVptIispSigVcdProvEntry,
       "mscAtmIfVptIispSigVcdTrafficDescType": mscAtmIfVptIispSigVcdTrafficDescType,
       "mscAtmIfVptIispSigVcdAtmServiceCategory": mscAtmIfVptIispSigVcdAtmServiceCategory,
       "mscAtmIfVptIispSigVcdWeight": mscAtmIfVptIispSigVcdWeight,
       "mscAtmIfVptIispSigVcdQosClass": mscAtmIfVptIispSigVcdQosClass,
       "mscAtmIfVptIispSigVcdTrafficShaping": mscAtmIfVptIispSigVcdTrafficShaping,
       "mscAtmIfVptIispSigVcdUnshapedTransmitQueueing": mscAtmIfVptIispSigVcdUnshapedTransmitQueueing,
       "mscAtmIfVptIispSigVcdUsageParameterControl": mscAtmIfVptIispSigVcdUsageParameterControl,
       "mscAtmIfVptIispSigVcdTdpTable": mscAtmIfVptIispSigVcdTdpTable,
       "mscAtmIfVptIispSigVcdTdpEntry": mscAtmIfVptIispSigVcdTdpEntry,
       "mscAtmIfVptIispSigVcdTdpIndex": mscAtmIfVptIispSigVcdTdpIndex,
       "mscAtmIfVptIispSigVcdTdpValue": mscAtmIfVptIispSigVcdTdpValue,
       "mscAtmIfVptIispSigProvTable": mscAtmIfVptIispSigProvTable,
       "mscAtmIfVptIispSigProvEntry": mscAtmIfVptIispSigProvEntry,
       "mscAtmIfVptIispSigVci": mscAtmIfVptIispSigVci,
       "mscAtmIfVptIispSigAddressConversion": mscAtmIfVptIispSigAddressConversion,
       "mscAtmIfVptIispSigOperatingMode": mscAtmIfVptIispSigOperatingMode,
       "mscAtmIfVptIispSigStateTable": mscAtmIfVptIispSigStateTable,
       "mscAtmIfVptIispSigStateEntry": mscAtmIfVptIispSigStateEntry,
       "mscAtmIfVptIispSigAdminState": mscAtmIfVptIispSigAdminState,
       "mscAtmIfVptIispSigOperationalState": mscAtmIfVptIispSigOperationalState,
       "mscAtmIfVptIispSigUsageState": mscAtmIfVptIispSigUsageState,
       "mscAtmIfVptIispSigOperTable": mscAtmIfVptIispSigOperTable,
       "mscAtmIfVptIispSigOperEntry": mscAtmIfVptIispSigOperEntry,
       "mscAtmIfVptIispSigLastTxCauseCode": mscAtmIfVptIispSigLastTxCauseCode,
       "mscAtmIfVptIispSigLastTxDiagCode": mscAtmIfVptIispSigLastTxDiagCode,
       "mscAtmIfVptIispSigLastRxCauseCode": mscAtmIfVptIispSigLastRxCauseCode,
       "mscAtmIfVptIispSigLastRxDiagCode": mscAtmIfVptIispSigLastRxDiagCode,
       "mscAtmIfVptIispSigStatsTable": mscAtmIfVptIispSigStatsTable,
       "mscAtmIfVptIispSigStatsEntry": mscAtmIfVptIispSigStatsEntry,
       "mscAtmIfVptIispSigCurrentConnections": mscAtmIfVptIispSigCurrentConnections,
       "mscAtmIfVptIispSigPeakConnections": mscAtmIfVptIispSigPeakConnections,
       "mscAtmIfVptIispSigSuccessfulConnections": mscAtmIfVptIispSigSuccessfulConnections,
       "mscAtmIfVptIispSigFailedConnections": mscAtmIfVptIispSigFailedConnections,
       "mscAtmIfVptIispSigTxPdus": mscAtmIfVptIispSigTxPdus,
       "mscAtmIfVptIispSigRxPdus": mscAtmIfVptIispSigRxPdus,
       "mscAtmIfVptIispSigCurrentPmpConnections": mscAtmIfVptIispSigCurrentPmpConnections,
       "mscAtmIfVptIispSigPeakPmpConnections": mscAtmIfVptIispSigPeakPmpConnections,
       "mscAtmIfVptIispSigSuccessfulPmpConnections": mscAtmIfVptIispSigSuccessfulPmpConnections,
       "mscAtmIfVptIispSigFailedPmpConnections": mscAtmIfVptIispSigFailedPmpConnections,
       "mscAtmIfVptIispSigNewCurrentConnections": mscAtmIfVptIispSigNewCurrentConnections,
       "mscAtmIfVptIispAddr": mscAtmIfVptIispAddr,
       "mscAtmIfVptIispAddrRowStatusTable": mscAtmIfVptIispAddrRowStatusTable,
       "mscAtmIfVptIispAddrRowStatusEntry": mscAtmIfVptIispAddrRowStatusEntry,
       "mscAtmIfVptIispAddrRowStatus": mscAtmIfVptIispAddrRowStatus,
       "mscAtmIfVptIispAddrComponentName": mscAtmIfVptIispAddrComponentName,
       "mscAtmIfVptIispAddrStorageType": mscAtmIfVptIispAddrStorageType,
       "mscAtmIfVptIispAddrAddressIndex": mscAtmIfVptIispAddrAddressIndex,
       "mscAtmIfVptIispAddrAddressTypeIndex": mscAtmIfVptIispAddrAddressTypeIndex,
       "mscAtmIfVptIispAddrTermSP": mscAtmIfVptIispAddrTermSP,
       "mscAtmIfVptIispAddrTermSPRowStatusTable": mscAtmIfVptIispAddrTermSPRowStatusTable,
       "mscAtmIfVptIispAddrTermSPRowStatusEntry": mscAtmIfVptIispAddrTermSPRowStatusEntry,
       "mscAtmIfVptIispAddrTermSPRowStatus": mscAtmIfVptIispAddrTermSPRowStatus,
       "mscAtmIfVptIispAddrTermSPComponentName": mscAtmIfVptIispAddrTermSPComponentName,
       "mscAtmIfVptIispAddrTermSPStorageType": mscAtmIfVptIispAddrTermSPStorageType,
       "mscAtmIfVptIispAddrTermSPIndex": mscAtmIfVptIispAddrTermSPIndex,
       "mscAtmIfVptIispAddrPnniInfo": mscAtmIfVptIispAddrPnniInfo,
       "mscAtmIfVptIispAddrPnniInfoRowStatusTable": mscAtmIfVptIispAddrPnniInfoRowStatusTable,
       "mscAtmIfVptIispAddrPnniInfoRowStatusEntry": mscAtmIfVptIispAddrPnniInfoRowStatusEntry,
       "mscAtmIfVptIispAddrPnniInfoRowStatus": mscAtmIfVptIispAddrPnniInfoRowStatus,
       "mscAtmIfVptIispAddrPnniInfoComponentName": mscAtmIfVptIispAddrPnniInfoComponentName,
       "mscAtmIfVptIispAddrPnniInfoStorageType": mscAtmIfVptIispAddrPnniInfoStorageType,
       "mscAtmIfVptIispAddrPnniInfoIndex": mscAtmIfVptIispAddrPnniInfoIndex,
       "mscAtmIfVptIispAddrPnniInfoProvTable": mscAtmIfVptIispAddrPnniInfoProvTable,
       "mscAtmIfVptIispAddrPnniInfoProvEntry": mscAtmIfVptIispAddrPnniInfoProvEntry,
       "mscAtmIfVptIispAddrPnniInfoScope": mscAtmIfVptIispAddrPnniInfoScope,
       "mscAtmIfVptIispAddrPnniInfoReachability": mscAtmIfVptIispAddrPnniInfoReachability,
       "mscAtmIfVptIispAddrOperTable": mscAtmIfVptIispAddrOperTable,
       "mscAtmIfVptIispAddrOperEntry": mscAtmIfVptIispAddrOperEntry,
       "mscAtmIfVptIispAddrScope": mscAtmIfVptIispAddrScope,
       "mscAtmIfVptIispAddrReachability": mscAtmIfVptIispAddrReachability,
       "mscAtmIfVptIispCallingAScr": mscAtmIfVptIispCallingAScr,
       "mscAtmIfVptIispCallingAScrRowStatusTable": mscAtmIfVptIispCallingAScrRowStatusTable,
       "mscAtmIfVptIispCallingAScrRowStatusEntry": mscAtmIfVptIispCallingAScrRowStatusEntry,
       "mscAtmIfVptIispCallingAScrRowStatus": mscAtmIfVptIispCallingAScrRowStatus,
       "mscAtmIfVptIispCallingAScrComponentName": mscAtmIfVptIispCallingAScrComponentName,
       "mscAtmIfVptIispCallingAScrStorageType": mscAtmIfVptIispCallingAScrStorageType,
       "mscAtmIfVptIispCallingAScrIndex": mscAtmIfVptIispCallingAScrIndex,
       "mscAtmIfVptIispCallingAScrAddr": mscAtmIfVptIispCallingAScrAddr,
       "mscAtmIfVptIispCallingAScrAddrRowStatusTable": mscAtmIfVptIispCallingAScrAddrRowStatusTable,
       "mscAtmIfVptIispCallingAScrAddrRowStatusEntry": mscAtmIfVptIispCallingAScrAddrRowStatusEntry,
       "mscAtmIfVptIispCallingAScrAddrRowStatus": mscAtmIfVptIispCallingAScrAddrRowStatus,
       "mscAtmIfVptIispCallingAScrAddrComponentName": mscAtmIfVptIispCallingAScrAddrComponentName,
       "mscAtmIfVptIispCallingAScrAddrStorageType": mscAtmIfVptIispCallingAScrAddrStorageType,
       "mscAtmIfVptIispCallingAScrAddrAddressIndex": mscAtmIfVptIispCallingAScrAddrAddressIndex,
       "mscAtmIfVptIispCallingAScrAddrAddressActionIndex": mscAtmIfVptIispCallingAScrAddrAddressActionIndex,
       "mscAtmIfVptIispCallingAScrProvTable": mscAtmIfVptIispCallingAScrProvTable,
       "mscAtmIfVptIispCallingAScrProvEntry": mscAtmIfVptIispCallingAScrProvEntry,
       "mscAtmIfVptIispCallingAScrAdminStatus": mscAtmIfVptIispCallingAScrAdminStatus,
       "mscAtmIfVptIispCallingAScrDefaultInsertionAddress": mscAtmIfVptIispCallingAScrDefaultInsertionAddress,
       "mscAtmIfVptIispCallingAScrStatTable": mscAtmIfVptIispCallingAScrStatTable,
       "mscAtmIfVptIispCallingAScrStatEntry": mscAtmIfVptIispCallingAScrStatEntry,
       "mscAtmIfVptIispCallingAScrAcceptedCalls": mscAtmIfVptIispCallingAScrAcceptedCalls,
       "mscAtmIfVptIispCallingAScrRejectedCalls": mscAtmIfVptIispCallingAScrRejectedCalls,
       "mscAtmIfVptIispCallingAScrUnmatchedCalls": mscAtmIfVptIispCallingAScrUnmatchedCalls,
       "mscAtmIfVptIispCalledAScr": mscAtmIfVptIispCalledAScr,
       "mscAtmIfVptIispCalledAScrRowStatusTable": mscAtmIfVptIispCalledAScrRowStatusTable,
       "mscAtmIfVptIispCalledAScrRowStatusEntry": mscAtmIfVptIispCalledAScrRowStatusEntry,
       "mscAtmIfVptIispCalledAScrRowStatus": mscAtmIfVptIispCalledAScrRowStatus,
       "mscAtmIfVptIispCalledAScrComponentName": mscAtmIfVptIispCalledAScrComponentName,
       "mscAtmIfVptIispCalledAScrStorageType": mscAtmIfVptIispCalledAScrStorageType,
       "mscAtmIfVptIispCalledAScrIndex": mscAtmIfVptIispCalledAScrIndex,
       "mscAtmIfVptIispCalledAScrAddr": mscAtmIfVptIispCalledAScrAddr,
       "mscAtmIfVptIispCalledAScrAddrRowStatusTable": mscAtmIfVptIispCalledAScrAddrRowStatusTable,
       "mscAtmIfVptIispCalledAScrAddrRowStatusEntry": mscAtmIfVptIispCalledAScrAddrRowStatusEntry,
       "mscAtmIfVptIispCalledAScrAddrRowStatus": mscAtmIfVptIispCalledAScrAddrRowStatus,
       "mscAtmIfVptIispCalledAScrAddrComponentName": mscAtmIfVptIispCalledAScrAddrComponentName,
       "mscAtmIfVptIispCalledAScrAddrStorageType": mscAtmIfVptIispCalledAScrAddrStorageType,
       "mscAtmIfVptIispCalledAScrAddrAddressIndex": mscAtmIfVptIispCalledAScrAddrAddressIndex,
       "mscAtmIfVptIispCalledAScrAddrAddressActionIndex": mscAtmIfVptIispCalledAScrAddrAddressActionIndex,
       "mscAtmIfVptIispCalledAScrProvTable": mscAtmIfVptIispCalledAScrProvTable,
       "mscAtmIfVptIispCalledAScrProvEntry": mscAtmIfVptIispCalledAScrProvEntry,
       "mscAtmIfVptIispCalledAScrAdminStatus": mscAtmIfVptIispCalledAScrAdminStatus,
       "mscAtmIfVptIispCalledAScrStatTable": mscAtmIfVptIispCalledAScrStatTable,
       "mscAtmIfVptIispCalledAScrStatEntry": mscAtmIfVptIispCalledAScrStatEntry,
       "mscAtmIfVptIispCalledAScrAcceptedCalls": mscAtmIfVptIispCalledAScrAcceptedCalls,
       "mscAtmIfVptIispCalledAScrRejectedCalls": mscAtmIfVptIispCalledAScrRejectedCalls,
       "mscAtmIfVptIispCalledAScrUnmatchedCalls": mscAtmIfVptIispCalledAScrUnmatchedCalls,
       "mscAtmIfVptIispProvTable": mscAtmIfVptIispProvTable,
       "mscAtmIfVptIispProvEntry": mscAtmIfVptIispProvEntry,
       "mscAtmIfVptIispVersion": mscAtmIfVptIispVersion,
       "mscAtmIfVptIispSide": mscAtmIfVptIispSide,
       "mscAtmIfVptIispSoftPvcRetryPeriod": mscAtmIfVptIispSoftPvcRetryPeriod,
       "mscAtmIfVptIispSoftPvpAndPvcRetryPeriod": mscAtmIfVptIispSoftPvpAndPvcRetryPeriod,
       "mscAtmIfVptIispSoftPvpAndPvcHoldOffTime": mscAtmIfVptIispSoftPvpAndPvcHoldOffTime,
       "mscAtmIfVptIispAcctOptTable": mscAtmIfVptIispAcctOptTable,
       "mscAtmIfVptIispAcctOptEntry": mscAtmIfVptIispAcctOptEntry,
       "mscAtmIfVptIispAccountCollection": mscAtmIfVptIispAccountCollection,
       "mscAtmIfVptIispAccountConnectionType": mscAtmIfVptIispAccountConnectionType,
       "mscAtmIfVptIispAccountClass": mscAtmIfVptIispAccountClass,
       "mscAtmIfVptIispServiceExchange": mscAtmIfVptIispServiceExchange,
       "mscAtmIfVptIispVProvTable": mscAtmIfVptIispVProvTable,
       "mscAtmIfVptIispVProvEntry": mscAtmIfVptIispVProvEntry,
       "mscAtmIfVptIispVpci": mscAtmIfVptIispVpci,
       "atmIispMIB": atmIispMIB,
       "atmIispGroup": atmIispGroup,
       "atmIispGroupCA": atmIispGroupCA,
       "atmIispGroupCA02": atmIispGroupCA02,
       "atmIispGroupCA02A": atmIispGroupCA02A,
       "atmIispCapabilities": atmIispCapabilities,
       "atmIispCapabilitiesCA": atmIispCapabilitiesCA,
       "atmIispCapabilitiesCA02": atmIispCapabilitiesCA02,
       "atmIispCapabilitiesCA02A": atmIispCapabilitiesCA02A}
)
