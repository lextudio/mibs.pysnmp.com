# SNMP MIB module (Nortel-Magellan-Passport-AtmIispMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-Magellan-Passport-AtmIispMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:30:19 2024
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

(atmIf,
 atmIfIndex,
 atmIfVpt,
 atmIfVptIndex) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-AtmCoreMIB",
    "atmIf",
    "atmIfIndex",
    "atmIfVpt",
    "atmIfVptIndex")

(Counter32,
 DisplayString,
 Gauge32,
 Integer32,
 RowStatus,
 StorageType,
 Unsigned32) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-StandardTextualConventionsMIB",
    "Counter32",
    "DisplayString",
    "Gauge32",
    "Integer32",
    "RowStatus",
    "StorageType",
    "Unsigned32")

(AsciiStringIndex,
 Hex,
 NonReplicated) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-TextualConventionsMIB",
    "AsciiStringIndex",
    "Hex",
    "NonReplicated")

(passportMIBs,) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-UsefulDefinitionsMIB",
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

_AtmIfIisp_ObjectIdentity = ObjectIdentity
atmIfIisp = _AtmIfIisp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 7)
)
_AtmIfIispRowStatusTable_Object = MibTable
atmIfIispRowStatusTable = _AtmIfIispRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 7, 1)
)
if mibBuilder.loadTexts:
    atmIfIispRowStatusTable.setStatus("mandatory")
_AtmIfIispRowStatusEntry_Object = MibTableRow
atmIfIispRowStatusEntry = _AtmIfIispRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 7, 1, 1)
)
atmIfIispRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmIispMIB", "atmIfIispIndex"),
)
if mibBuilder.loadTexts:
    atmIfIispRowStatusEntry.setStatus("mandatory")
_AtmIfIispRowStatus_Type = RowStatus
_AtmIfIispRowStatus_Object = MibTableColumn
atmIfIispRowStatus = _AtmIfIispRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 7, 1, 1, 1),
    _AtmIfIispRowStatus_Type()
)
atmIfIispRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfIispRowStatus.setStatus("mandatory")
_AtmIfIispComponentName_Type = DisplayString
_AtmIfIispComponentName_Object = MibTableColumn
atmIfIispComponentName = _AtmIfIispComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 7, 1, 1, 2),
    _AtmIfIispComponentName_Type()
)
atmIfIispComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfIispComponentName.setStatus("mandatory")
_AtmIfIispStorageType_Type = StorageType
_AtmIfIispStorageType_Object = MibTableColumn
atmIfIispStorageType = _AtmIfIispStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 7, 1, 1, 4),
    _AtmIfIispStorageType_Type()
)
atmIfIispStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfIispStorageType.setStatus("mandatory")
_AtmIfIispIndex_Type = NonReplicated
_AtmIfIispIndex_Object = MibTableColumn
atmIfIispIndex = _AtmIfIispIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 7, 1, 1, 10),
    _AtmIfIispIndex_Type()
)
atmIfIispIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmIfIispIndex.setStatus("mandatory")
_AtmIfIispSig_ObjectIdentity = ObjectIdentity
atmIfIispSig = _AtmIfIispSig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 7, 3)
)
_AtmIfIispSigRowStatusTable_Object = MibTable
atmIfIispSigRowStatusTable = _AtmIfIispSigRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 7, 3, 1)
)
if mibBuilder.loadTexts:
    atmIfIispSigRowStatusTable.setStatus("mandatory")
_AtmIfIispSigRowStatusEntry_Object = MibTableRow
atmIfIispSigRowStatusEntry = _AtmIfIispSigRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 7, 3, 1, 1)
)
atmIfIispSigRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmIispMIB", "atmIfIispIndex"),
    (0, "Nortel-Magellan-Passport-AtmIispMIB", "atmIfIispSigIndex"),
)
if mibBuilder.loadTexts:
    atmIfIispSigRowStatusEntry.setStatus("mandatory")
_AtmIfIispSigRowStatus_Type = RowStatus
_AtmIfIispSigRowStatus_Object = MibTableColumn
atmIfIispSigRowStatus = _AtmIfIispSigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 7, 3, 1, 1, 1),
    _AtmIfIispSigRowStatus_Type()
)
atmIfIispSigRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfIispSigRowStatus.setStatus("mandatory")
_AtmIfIispSigComponentName_Type = DisplayString
_AtmIfIispSigComponentName_Object = MibTableColumn
atmIfIispSigComponentName = _AtmIfIispSigComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 7, 3, 1, 1, 2),
    _AtmIfIispSigComponentName_Type()
)
atmIfIispSigComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfIispSigComponentName.setStatus("mandatory")
_AtmIfIispSigStorageType_Type = StorageType
_AtmIfIispSigStorageType_Object = MibTableColumn
atmIfIispSigStorageType = _AtmIfIispSigStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 7, 3, 1, 1, 4),
    _AtmIfIispSigStorageType_Type()
)
atmIfIispSigStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfIispSigStorageType.setStatus("mandatory")
_AtmIfIispSigIndex_Type = NonReplicated
_AtmIfIispSigIndex_Object = MibTableColumn
atmIfIispSigIndex = _AtmIfIispSigIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 7, 3, 1, 1, 10),
    _AtmIfIispSigIndex_Type()
)
atmIfIispSigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmIfIispSigIndex.setStatus("mandatory")
_AtmIfIispSigVcd_ObjectIdentity = ObjectIdentity
atmIfIispSigVcd = _AtmIfIispSigVcd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 7, 3, 2)
)
_AtmIfIispSigVcdRowStatusTable_Object = MibTable
atmIfIispSigVcdRowStatusTable = _AtmIfIispSigVcdRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 7, 3, 2, 1)
)
if mibBuilder.loadTexts:
    atmIfIispSigVcdRowStatusTable.setStatus("mandatory")
_AtmIfIispSigVcdRowStatusEntry_Object = MibTableRow
atmIfIispSigVcdRowStatusEntry = _AtmIfIispSigVcdRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 7, 3, 2, 1, 1)
)
atmIfIispSigVcdRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmIispMIB", "atmIfIispIndex"),
    (0, "Nortel-Magellan-Passport-AtmIispMIB", "atmIfIispSigIndex"),
    (0, "Nortel-Magellan-Passport-AtmIispMIB", "atmIfIispSigVcdIndex"),
)
if mibBuilder.loadTexts:
    atmIfIispSigVcdRowStatusEntry.setStatus("mandatory")
_AtmIfIispSigVcdRowStatus_Type = RowStatus
_AtmIfIispSigVcdRowStatus_Object = MibTableColumn
atmIfIispSigVcdRowStatus = _AtmIfIispSigVcdRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 7, 3, 2, 1, 1, 1),
    _AtmIfIispSigVcdRowStatus_Type()
)
atmIfIispSigVcdRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfIispSigVcdRowStatus.setStatus("mandatory")
_AtmIfIispSigVcdComponentName_Type = DisplayString
_AtmIfIispSigVcdComponentName_Object = MibTableColumn
atmIfIispSigVcdComponentName = _AtmIfIispSigVcdComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 7, 3, 2, 1, 1, 2),
    _AtmIfIispSigVcdComponentName_Type()
)
atmIfIispSigVcdComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfIispSigVcdComponentName.setStatus("mandatory")
_AtmIfIispSigVcdStorageType_Type = StorageType
_AtmIfIispSigVcdStorageType_Object = MibTableColumn
atmIfIispSigVcdStorageType = _AtmIfIispSigVcdStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 7, 3, 2, 1, 1, 4),
    _AtmIfIispSigVcdStorageType_Type()
)
atmIfIispSigVcdStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfIispSigVcdStorageType.setStatus("mandatory")
_AtmIfIispSigVcdIndex_Type = NonReplicated
_AtmIfIispSigVcdIndex_Object = MibTableColumn
atmIfIispSigVcdIndex = _AtmIfIispSigVcdIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 7, 3, 2, 1, 1, 10),
    _AtmIfIispSigVcdIndex_Type()
)
atmIfIispSigVcdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmIfIispSigVcdIndex.setStatus("mandatory")
_AtmIfIispSigVcdProvTable_Object = MibTable
atmIfIispSigVcdProvTable = _AtmIfIispSigVcdProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 7, 3, 2, 10)
)
if mibBuilder.loadTexts:
    atmIfIispSigVcdProvTable.setStatus("mandatory")
_AtmIfIispSigVcdProvEntry_Object = MibTableRow
atmIfIispSigVcdProvEntry = _AtmIfIispSigVcdProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 7, 3, 2, 10, 1)
)
atmIfIispSigVcdProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmIispMIB", "atmIfIispIndex"),
    (0, "Nortel-Magellan-Passport-AtmIispMIB", "atmIfIispSigIndex"),
    (0, "Nortel-Magellan-Passport-AtmIispMIB", "atmIfIispSigVcdIndex"),
)
if mibBuilder.loadTexts:
    atmIfIispSigVcdProvEntry.setStatus("mandatory")


class _AtmIfIispSigVcdTrafficDescType_Type(Integer32):
    """Custom type atmIfIispSigVcdTrafficDescType based on Integer32"""
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


_AtmIfIispSigVcdTrafficDescType_Type.__name__ = "Integer32"
_AtmIfIispSigVcdTrafficDescType_Object = MibTableColumn
atmIfIispSigVcdTrafficDescType = _AtmIfIispSigVcdTrafficDescType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 7, 3, 2, 10, 1, 1),
    _AtmIfIispSigVcdTrafficDescType_Type()
)
atmIfIispSigVcdTrafficDescType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfIispSigVcdTrafficDescType.setStatus("mandatory")


class _AtmIfIispSigVcdAtmServiceCategory_Type(Integer32):
    """Custom type atmIfIispSigVcdAtmServiceCategory based on Integer32"""
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


_AtmIfIispSigVcdAtmServiceCategory_Type.__name__ = "Integer32"
_AtmIfIispSigVcdAtmServiceCategory_Object = MibTableColumn
atmIfIispSigVcdAtmServiceCategory = _AtmIfIispSigVcdAtmServiceCategory_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 7, 3, 2, 10, 1, 3),
    _AtmIfIispSigVcdAtmServiceCategory_Type()
)
atmIfIispSigVcdAtmServiceCategory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfIispSigVcdAtmServiceCategory.setStatus("mandatory")


class _AtmIfIispSigVcdQosClass_Type(Integer32):
    """Custom type atmIfIispSigVcdQosClass based on Integer32"""
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


_AtmIfIispSigVcdQosClass_Type.__name__ = "Integer32"
_AtmIfIispSigVcdQosClass_Object = MibTableColumn
atmIfIispSigVcdQosClass = _AtmIfIispSigVcdQosClass_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 7, 3, 2, 10, 1, 21),
    _AtmIfIispSigVcdQosClass_Type()
)
atmIfIispSigVcdQosClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfIispSigVcdQosClass.setStatus("mandatory")


class _AtmIfIispSigVcdTrafficShaping_Type(Integer32):
    """Custom type atmIfIispSigVcdTrafficShaping based on Integer32"""
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


_AtmIfIispSigVcdTrafficShaping_Type.__name__ = "Integer32"
_AtmIfIispSigVcdTrafficShaping_Object = MibTableColumn
atmIfIispSigVcdTrafficShaping = _AtmIfIispSigVcdTrafficShaping_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 7, 3, 2, 10, 1, 50),
    _AtmIfIispSigVcdTrafficShaping_Type()
)
atmIfIispSigVcdTrafficShaping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfIispSigVcdTrafficShaping.setStatus("mandatory")


class _AtmIfIispSigVcdUnshapedTransmitQueueing_Type(Integer32):
    """Custom type atmIfIispSigVcdUnshapedTransmitQueueing based on Integer32"""
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


_AtmIfIispSigVcdUnshapedTransmitQueueing_Type.__name__ = "Integer32"
_AtmIfIispSigVcdUnshapedTransmitQueueing_Object = MibTableColumn
atmIfIispSigVcdUnshapedTransmitQueueing = _AtmIfIispSigVcdUnshapedTransmitQueueing_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 7, 3, 2, 10, 1, 60),
    _AtmIfIispSigVcdUnshapedTransmitQueueing_Type()
)
atmIfIispSigVcdUnshapedTransmitQueueing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfIispSigVcdUnshapedTransmitQueueing.setStatus("mandatory")


class _AtmIfIispSigVcdUsageParameterControl_Type(Integer32):
    """Custom type atmIfIispSigVcdUsageParameterControl based on Integer32"""
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


_AtmIfIispSigVcdUsageParameterControl_Type.__name__ = "Integer32"
_AtmIfIispSigVcdUsageParameterControl_Object = MibTableColumn
atmIfIispSigVcdUsageParameterControl = _AtmIfIispSigVcdUsageParameterControl_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 7, 3, 2, 10, 1, 70),
    _AtmIfIispSigVcdUsageParameterControl_Type()
)
atmIfIispSigVcdUsageParameterControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfIispSigVcdUsageParameterControl.setStatus("mandatory")
_AtmIfIispSigVcdTdpTable_Object = MibTable
atmIfIispSigVcdTdpTable = _AtmIfIispSigVcdTdpTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 7, 3, 2, 387)
)
if mibBuilder.loadTexts:
    atmIfIispSigVcdTdpTable.setStatus("mandatory")
_AtmIfIispSigVcdTdpEntry_Object = MibTableRow
atmIfIispSigVcdTdpEntry = _AtmIfIispSigVcdTdpEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 7, 3, 2, 387, 1)
)
atmIfIispSigVcdTdpEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmIispMIB", "atmIfIispIndex"),
    (0, "Nortel-Magellan-Passport-AtmIispMIB", "atmIfIispSigIndex"),
    (0, "Nortel-Magellan-Passport-AtmIispMIB", "atmIfIispSigVcdIndex"),
    (0, "Nortel-Magellan-Passport-AtmIispMIB", "atmIfIispSigVcdTdpIndex"),
)
if mibBuilder.loadTexts:
    atmIfIispSigVcdTdpEntry.setStatus("mandatory")


class _AtmIfIispSigVcdTdpIndex_Type(Integer32):
    """Custom type atmIfIispSigVcdTdpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_AtmIfIispSigVcdTdpIndex_Type.__name__ = "Integer32"
_AtmIfIispSigVcdTdpIndex_Object = MibTableColumn
atmIfIispSigVcdTdpIndex = _AtmIfIispSigVcdTdpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 7, 3, 2, 387, 1, 1),
    _AtmIfIispSigVcdTdpIndex_Type()
)
atmIfIispSigVcdTdpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmIfIispSigVcdTdpIndex.setStatus("mandatory")


class _AtmIfIispSigVcdTdpValue_Type(Unsigned32):
    """Custom type atmIfIispSigVcdTdpValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AtmIfIispSigVcdTdpValue_Type.__name__ = "Unsigned32"
_AtmIfIispSigVcdTdpValue_Object = MibTableColumn
atmIfIispSigVcdTdpValue = _AtmIfIispSigVcdTdpValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 7, 3, 2, 387, 1, 2),
    _AtmIfIispSigVcdTdpValue_Type()
)
atmIfIispSigVcdTdpValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfIispSigVcdTdpValue.setStatus("mandatory")
_AtmIfIispSigProvTable_Object = MibTable
atmIfIispSigProvTable = _AtmIfIispSigProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 7, 3, 10)
)
if mibBuilder.loadTexts:
    atmIfIispSigProvTable.setStatus("mandatory")
_AtmIfIispSigProvEntry_Object = MibTableRow
atmIfIispSigProvEntry = _AtmIfIispSigProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 7, 3, 10, 1)
)
atmIfIispSigProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmIispMIB", "atmIfIispIndex"),
    (0, "Nortel-Magellan-Passport-AtmIispMIB", "atmIfIispSigIndex"),
)
if mibBuilder.loadTexts:
    atmIfIispSigProvEntry.setStatus("mandatory")


class _AtmIfIispSigVci_Type(Unsigned32):
    """Custom type atmIfIispSigVci based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AtmIfIispSigVci_Type.__name__ = "Unsigned32"
_AtmIfIispSigVci_Object = MibTableColumn
atmIfIispSigVci = _AtmIfIispSigVci_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 7, 3, 10, 1, 1),
    _AtmIfIispSigVci_Type()
)
atmIfIispSigVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfIispSigVci.setStatus("mandatory")


class _AtmIfIispSigAddressConversion_Type(Integer32):
    """Custom type atmIfIispSigAddressConversion based on Integer32"""
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


_AtmIfIispSigAddressConversion_Type.__name__ = "Integer32"
_AtmIfIispSigAddressConversion_Object = MibTableColumn
atmIfIispSigAddressConversion = _AtmIfIispSigAddressConversion_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 7, 3, 10, 1, 2),
    _AtmIfIispSigAddressConversion_Type()
)
atmIfIispSigAddressConversion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfIispSigAddressConversion.setStatus("mandatory")
_AtmIfIispSigStateTable_Object = MibTable
atmIfIispSigStateTable = _AtmIfIispSigStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 7, 3, 11)
)
if mibBuilder.loadTexts:
    atmIfIispSigStateTable.setStatus("mandatory")
_AtmIfIispSigStateEntry_Object = MibTableRow
atmIfIispSigStateEntry = _AtmIfIispSigStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 7, 3, 11, 1)
)
atmIfIispSigStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmIispMIB", "atmIfIispIndex"),
    (0, "Nortel-Magellan-Passport-AtmIispMIB", "atmIfIispSigIndex"),
)
if mibBuilder.loadTexts:
    atmIfIispSigStateEntry.setStatus("mandatory")


class _AtmIfIispSigAdminState_Type(Integer32):
    """Custom type atmIfIispSigAdminState based on Integer32"""
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


_AtmIfIispSigAdminState_Type.__name__ = "Integer32"
_AtmIfIispSigAdminState_Object = MibTableColumn
atmIfIispSigAdminState = _AtmIfIispSigAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 7, 3, 11, 1, 1),
    _AtmIfIispSigAdminState_Type()
)
atmIfIispSigAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfIispSigAdminState.setStatus("mandatory")


class _AtmIfIispSigOperationalState_Type(Integer32):
    """Custom type atmIfIispSigOperationalState based on Integer32"""
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


_AtmIfIispSigOperationalState_Type.__name__ = "Integer32"
_AtmIfIispSigOperationalState_Object = MibTableColumn
atmIfIispSigOperationalState = _AtmIfIispSigOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 7, 3, 11, 1, 2),
    _AtmIfIispSigOperationalState_Type()
)
atmIfIispSigOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfIispSigOperationalState.setStatus("mandatory")


class _AtmIfIispSigUsageState_Type(Integer32):
    """Custom type atmIfIispSigUsageState based on Integer32"""
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


_AtmIfIispSigUsageState_Type.__name__ = "Integer32"
_AtmIfIispSigUsageState_Object = MibTableColumn
atmIfIispSigUsageState = _AtmIfIispSigUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 7, 3, 11, 1, 3),
    _AtmIfIispSigUsageState_Type()
)
atmIfIispSigUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfIispSigUsageState.setStatus("mandatory")
_AtmIfIispSigOperTable_Object = MibTable
atmIfIispSigOperTable = _AtmIfIispSigOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 7, 3, 12)
)
if mibBuilder.loadTexts:
    atmIfIispSigOperTable.setStatus("mandatory")
_AtmIfIispSigOperEntry_Object = MibTableRow
atmIfIispSigOperEntry = _AtmIfIispSigOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 7, 3, 12, 1)
)
atmIfIispSigOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmIispMIB", "atmIfIispIndex"),
    (0, "Nortel-Magellan-Passport-AtmIispMIB", "atmIfIispSigIndex"),
)
if mibBuilder.loadTexts:
    atmIfIispSigOperEntry.setStatus("mandatory")


class _AtmIfIispSigLastTxCauseCode_Type(Unsigned32):
    """Custom type atmIfIispSigLastTxCauseCode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AtmIfIispSigLastTxCauseCode_Type.__name__ = "Unsigned32"
_AtmIfIispSigLastTxCauseCode_Object = MibTableColumn
atmIfIispSigLastTxCauseCode = _AtmIfIispSigLastTxCauseCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 7, 3, 12, 1, 1),
    _AtmIfIispSigLastTxCauseCode_Type()
)
atmIfIispSigLastTxCauseCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfIispSigLastTxCauseCode.setStatus("mandatory")


class _AtmIfIispSigLastTxDiagCode_Type(Hex):
    """Custom type atmIfIispSigLastTxDiagCode based on Hex"""
    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AtmIfIispSigLastTxDiagCode_Type.__name__ = "Hex"
_AtmIfIispSigLastTxDiagCode_Object = MibTableColumn
atmIfIispSigLastTxDiagCode = _AtmIfIispSigLastTxDiagCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 7, 3, 12, 1, 2),
    _AtmIfIispSigLastTxDiagCode_Type()
)
atmIfIispSigLastTxDiagCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfIispSigLastTxDiagCode.setStatus("mandatory")


class _AtmIfIispSigLastRxCauseCode_Type(Unsigned32):
    """Custom type atmIfIispSigLastRxCauseCode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AtmIfIispSigLastRxCauseCode_Type.__name__ = "Unsigned32"
_AtmIfIispSigLastRxCauseCode_Object = MibTableColumn
atmIfIispSigLastRxCauseCode = _AtmIfIispSigLastRxCauseCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 7, 3, 12, 1, 3),
    _AtmIfIispSigLastRxCauseCode_Type()
)
atmIfIispSigLastRxCauseCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfIispSigLastRxCauseCode.setStatus("mandatory")


class _AtmIfIispSigLastRxDiagCode_Type(Hex):
    """Custom type atmIfIispSigLastRxDiagCode based on Hex"""
    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AtmIfIispSigLastRxDiagCode_Type.__name__ = "Hex"
_AtmIfIispSigLastRxDiagCode_Object = MibTableColumn
atmIfIispSigLastRxDiagCode = _AtmIfIispSigLastRxDiagCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 7, 3, 12, 1, 4),
    _AtmIfIispSigLastRxDiagCode_Type()
)
atmIfIispSigLastRxDiagCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfIispSigLastRxDiagCode.setStatus("mandatory")
_AtmIfIispSigStatsTable_Object = MibTable
atmIfIispSigStatsTable = _AtmIfIispSigStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 7, 3, 13)
)
if mibBuilder.loadTexts:
    atmIfIispSigStatsTable.setStatus("mandatory")
_AtmIfIispSigStatsEntry_Object = MibTableRow
atmIfIispSigStatsEntry = _AtmIfIispSigStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 7, 3, 13, 1)
)
atmIfIispSigStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmIispMIB", "atmIfIispIndex"),
    (0, "Nortel-Magellan-Passport-AtmIispMIB", "atmIfIispSigIndex"),
)
if mibBuilder.loadTexts:
    atmIfIispSigStatsEntry.setStatus("mandatory")
_AtmIfIispSigCurrentConnections_Type = Counter32
_AtmIfIispSigCurrentConnections_Object = MibTableColumn
atmIfIispSigCurrentConnections = _AtmIfIispSigCurrentConnections_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 7, 3, 13, 1, 1),
    _AtmIfIispSigCurrentConnections_Type()
)
atmIfIispSigCurrentConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfIispSigCurrentConnections.setStatus("obsolete")


class _AtmIfIispSigPeakConnections_Type(Gauge32):
    """Custom type atmIfIispSigPeakConnections based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AtmIfIispSigPeakConnections_Type.__name__ = "Gauge32"
_AtmIfIispSigPeakConnections_Object = MibTableColumn
atmIfIispSigPeakConnections = _AtmIfIispSigPeakConnections_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 7, 3, 13, 1, 2),
    _AtmIfIispSigPeakConnections_Type()
)
atmIfIispSigPeakConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfIispSigPeakConnections.setStatus("mandatory")
_AtmIfIispSigSuccessfulConnections_Type = Counter32
_AtmIfIispSigSuccessfulConnections_Object = MibTableColumn
atmIfIispSigSuccessfulConnections = _AtmIfIispSigSuccessfulConnections_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 7, 3, 13, 1, 3),
    _AtmIfIispSigSuccessfulConnections_Type()
)
atmIfIispSigSuccessfulConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfIispSigSuccessfulConnections.setStatus("mandatory")
_AtmIfIispSigFailedConnections_Type = Counter32
_AtmIfIispSigFailedConnections_Object = MibTableColumn
atmIfIispSigFailedConnections = _AtmIfIispSigFailedConnections_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 7, 3, 13, 1, 4),
    _AtmIfIispSigFailedConnections_Type()
)
atmIfIispSigFailedConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfIispSigFailedConnections.setStatus("mandatory")
_AtmIfIispSigTxPdus_Type = Counter32
_AtmIfIispSigTxPdus_Object = MibTableColumn
atmIfIispSigTxPdus = _AtmIfIispSigTxPdus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 7, 3, 13, 1, 5),
    _AtmIfIispSigTxPdus_Type()
)
atmIfIispSigTxPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfIispSigTxPdus.setStatus("mandatory")
_AtmIfIispSigRxPdus_Type = Counter32
_AtmIfIispSigRxPdus_Object = MibTableColumn
atmIfIispSigRxPdus = _AtmIfIispSigRxPdus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 7, 3, 13, 1, 6),
    _AtmIfIispSigRxPdus_Type()
)
atmIfIispSigRxPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfIispSigRxPdus.setStatus("mandatory")


class _AtmIfIispSigCurrentPmpConnections_Type(Gauge32):
    """Custom type atmIfIispSigCurrentPmpConnections based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AtmIfIispSigCurrentPmpConnections_Type.__name__ = "Gauge32"
_AtmIfIispSigCurrentPmpConnections_Object = MibTableColumn
atmIfIispSigCurrentPmpConnections = _AtmIfIispSigCurrentPmpConnections_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 7, 3, 13, 1, 7),
    _AtmIfIispSigCurrentPmpConnections_Type()
)
atmIfIispSigCurrentPmpConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfIispSigCurrentPmpConnections.setStatus("mandatory")


class _AtmIfIispSigPeakPmpConnections_Type(Gauge32):
    """Custom type atmIfIispSigPeakPmpConnections based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AtmIfIispSigPeakPmpConnections_Type.__name__ = "Gauge32"
_AtmIfIispSigPeakPmpConnections_Object = MibTableColumn
atmIfIispSigPeakPmpConnections = _AtmIfIispSigPeakPmpConnections_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 7, 3, 13, 1, 8),
    _AtmIfIispSigPeakPmpConnections_Type()
)
atmIfIispSigPeakPmpConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfIispSigPeakPmpConnections.setStatus("mandatory")
_AtmIfIispSigSuccessfulPmpConnections_Type = Counter32
_AtmIfIispSigSuccessfulPmpConnections_Object = MibTableColumn
atmIfIispSigSuccessfulPmpConnections = _AtmIfIispSigSuccessfulPmpConnections_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 7, 3, 13, 1, 9),
    _AtmIfIispSigSuccessfulPmpConnections_Type()
)
atmIfIispSigSuccessfulPmpConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfIispSigSuccessfulPmpConnections.setStatus("mandatory")
_AtmIfIispSigFailedPmpConnections_Type = Counter32
_AtmIfIispSigFailedPmpConnections_Object = MibTableColumn
atmIfIispSigFailedPmpConnections = _AtmIfIispSigFailedPmpConnections_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 7, 3, 13, 1, 10),
    _AtmIfIispSigFailedPmpConnections_Type()
)
atmIfIispSigFailedPmpConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfIispSigFailedPmpConnections.setStatus("mandatory")


class _AtmIfIispSigNewCurrentConnections_Type(Gauge32):
    """Custom type atmIfIispSigNewCurrentConnections based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AtmIfIispSigNewCurrentConnections_Type.__name__ = "Gauge32"
_AtmIfIispSigNewCurrentConnections_Object = MibTableColumn
atmIfIispSigNewCurrentConnections = _AtmIfIispSigNewCurrentConnections_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 7, 3, 13, 1, 11),
    _AtmIfIispSigNewCurrentConnections_Type()
)
atmIfIispSigNewCurrentConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfIispSigNewCurrentConnections.setStatus("mandatory")
_AtmIfIispAddr_ObjectIdentity = ObjectIdentity
atmIfIispAddr = _AtmIfIispAddr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 7, 4)
)
_AtmIfIispAddrRowStatusTable_Object = MibTable
atmIfIispAddrRowStatusTable = _AtmIfIispAddrRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 7, 4, 1)
)
if mibBuilder.loadTexts:
    atmIfIispAddrRowStatusTable.setStatus("mandatory")
_AtmIfIispAddrRowStatusEntry_Object = MibTableRow
atmIfIispAddrRowStatusEntry = _AtmIfIispAddrRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 7, 4, 1, 1)
)
atmIfIispAddrRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmIispMIB", "atmIfIispIndex"),
    (0, "Nortel-Magellan-Passport-AtmIispMIB", "atmIfIispAddrAddressIndex"),
    (0, "Nortel-Magellan-Passport-AtmIispMIB", "atmIfIispAddrAddressTypeIndex"),
)
if mibBuilder.loadTexts:
    atmIfIispAddrRowStatusEntry.setStatus("mandatory")
_AtmIfIispAddrRowStatus_Type = RowStatus
_AtmIfIispAddrRowStatus_Object = MibTableColumn
atmIfIispAddrRowStatus = _AtmIfIispAddrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 7, 4, 1, 1, 1),
    _AtmIfIispAddrRowStatus_Type()
)
atmIfIispAddrRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfIispAddrRowStatus.setStatus("mandatory")
_AtmIfIispAddrComponentName_Type = DisplayString
_AtmIfIispAddrComponentName_Object = MibTableColumn
atmIfIispAddrComponentName = _AtmIfIispAddrComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 7, 4, 1, 1, 2),
    _AtmIfIispAddrComponentName_Type()
)
atmIfIispAddrComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfIispAddrComponentName.setStatus("mandatory")
_AtmIfIispAddrStorageType_Type = StorageType
_AtmIfIispAddrStorageType_Object = MibTableColumn
atmIfIispAddrStorageType = _AtmIfIispAddrStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 7, 4, 1, 1, 4),
    _AtmIfIispAddrStorageType_Type()
)
atmIfIispAddrStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfIispAddrStorageType.setStatus("mandatory")


class _AtmIfIispAddrAddressIndex_Type(AsciiStringIndex):
    """Custom type atmIfIispAddrAddressIndex based on AsciiStringIndex"""
    subtypeSpec = AsciiStringIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_AtmIfIispAddrAddressIndex_Type.__name__ = "AsciiStringIndex"
_AtmIfIispAddrAddressIndex_Object = MibTableColumn
atmIfIispAddrAddressIndex = _AtmIfIispAddrAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 7, 4, 1, 1, 10),
    _AtmIfIispAddrAddressIndex_Type()
)
atmIfIispAddrAddressIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmIfIispAddrAddressIndex.setStatus("mandatory")


class _AtmIfIispAddrAddressTypeIndex_Type(Integer32):
    """Custom type atmIfIispAddrAddressTypeIndex based on Integer32"""
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


_AtmIfIispAddrAddressTypeIndex_Type.__name__ = "Integer32"
_AtmIfIispAddrAddressTypeIndex_Object = MibTableColumn
atmIfIispAddrAddressTypeIndex = _AtmIfIispAddrAddressTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 7, 4, 1, 1, 11),
    _AtmIfIispAddrAddressTypeIndex_Type()
)
atmIfIispAddrAddressTypeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmIfIispAddrAddressTypeIndex.setStatus("mandatory")
_AtmIfIispAddrTermSP_ObjectIdentity = ObjectIdentity
atmIfIispAddrTermSP = _AtmIfIispAddrTermSP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 7, 4, 2)
)
_AtmIfIispAddrTermSPRowStatusTable_Object = MibTable
atmIfIispAddrTermSPRowStatusTable = _AtmIfIispAddrTermSPRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 7, 4, 2, 1)
)
if mibBuilder.loadTexts:
    atmIfIispAddrTermSPRowStatusTable.setStatus("mandatory")
_AtmIfIispAddrTermSPRowStatusEntry_Object = MibTableRow
atmIfIispAddrTermSPRowStatusEntry = _AtmIfIispAddrTermSPRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 7, 4, 2, 1, 1)
)
atmIfIispAddrTermSPRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmIispMIB", "atmIfIispIndex"),
    (0, "Nortel-Magellan-Passport-AtmIispMIB", "atmIfIispAddrAddressIndex"),
    (0, "Nortel-Magellan-Passport-AtmIispMIB", "atmIfIispAddrAddressTypeIndex"),
    (0, "Nortel-Magellan-Passport-AtmIispMIB", "atmIfIispAddrTermSPIndex"),
)
if mibBuilder.loadTexts:
    atmIfIispAddrTermSPRowStatusEntry.setStatus("mandatory")
_AtmIfIispAddrTermSPRowStatus_Type = RowStatus
_AtmIfIispAddrTermSPRowStatus_Object = MibTableColumn
atmIfIispAddrTermSPRowStatus = _AtmIfIispAddrTermSPRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 7, 4, 2, 1, 1, 1),
    _AtmIfIispAddrTermSPRowStatus_Type()
)
atmIfIispAddrTermSPRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfIispAddrTermSPRowStatus.setStatus("mandatory")
_AtmIfIispAddrTermSPComponentName_Type = DisplayString
_AtmIfIispAddrTermSPComponentName_Object = MibTableColumn
atmIfIispAddrTermSPComponentName = _AtmIfIispAddrTermSPComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 7, 4, 2, 1, 1, 2),
    _AtmIfIispAddrTermSPComponentName_Type()
)
atmIfIispAddrTermSPComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfIispAddrTermSPComponentName.setStatus("mandatory")
_AtmIfIispAddrTermSPStorageType_Type = StorageType
_AtmIfIispAddrTermSPStorageType_Object = MibTableColumn
atmIfIispAddrTermSPStorageType = _AtmIfIispAddrTermSPStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 7, 4, 2, 1, 1, 4),
    _AtmIfIispAddrTermSPStorageType_Type()
)
atmIfIispAddrTermSPStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfIispAddrTermSPStorageType.setStatus("mandatory")
_AtmIfIispAddrTermSPIndex_Type = NonReplicated
_AtmIfIispAddrTermSPIndex_Object = MibTableColumn
atmIfIispAddrTermSPIndex = _AtmIfIispAddrTermSPIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 7, 4, 2, 1, 1, 10),
    _AtmIfIispAddrTermSPIndex_Type()
)
atmIfIispAddrTermSPIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmIfIispAddrTermSPIndex.setStatus("mandatory")
_AtmIfIispAddrPnniInfo_ObjectIdentity = ObjectIdentity
atmIfIispAddrPnniInfo = _AtmIfIispAddrPnniInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 7, 4, 3)
)
_AtmIfIispAddrPnniInfoRowStatusTable_Object = MibTable
atmIfIispAddrPnniInfoRowStatusTable = _AtmIfIispAddrPnniInfoRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 7, 4, 3, 1)
)
if mibBuilder.loadTexts:
    atmIfIispAddrPnniInfoRowStatusTable.setStatus("mandatory")
_AtmIfIispAddrPnniInfoRowStatusEntry_Object = MibTableRow
atmIfIispAddrPnniInfoRowStatusEntry = _AtmIfIispAddrPnniInfoRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 7, 4, 3, 1, 1)
)
atmIfIispAddrPnniInfoRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmIispMIB", "atmIfIispIndex"),
    (0, "Nortel-Magellan-Passport-AtmIispMIB", "atmIfIispAddrAddressIndex"),
    (0, "Nortel-Magellan-Passport-AtmIispMIB", "atmIfIispAddrAddressTypeIndex"),
    (0, "Nortel-Magellan-Passport-AtmIispMIB", "atmIfIispAddrPnniInfoIndex"),
)
if mibBuilder.loadTexts:
    atmIfIispAddrPnniInfoRowStatusEntry.setStatus("mandatory")
_AtmIfIispAddrPnniInfoRowStatus_Type = RowStatus
_AtmIfIispAddrPnniInfoRowStatus_Object = MibTableColumn
atmIfIispAddrPnniInfoRowStatus = _AtmIfIispAddrPnniInfoRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 7, 4, 3, 1, 1, 1),
    _AtmIfIispAddrPnniInfoRowStatus_Type()
)
atmIfIispAddrPnniInfoRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfIispAddrPnniInfoRowStatus.setStatus("mandatory")
_AtmIfIispAddrPnniInfoComponentName_Type = DisplayString
_AtmIfIispAddrPnniInfoComponentName_Object = MibTableColumn
atmIfIispAddrPnniInfoComponentName = _AtmIfIispAddrPnniInfoComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 7, 4, 3, 1, 1, 2),
    _AtmIfIispAddrPnniInfoComponentName_Type()
)
atmIfIispAddrPnniInfoComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfIispAddrPnniInfoComponentName.setStatus("mandatory")
_AtmIfIispAddrPnniInfoStorageType_Type = StorageType
_AtmIfIispAddrPnniInfoStorageType_Object = MibTableColumn
atmIfIispAddrPnniInfoStorageType = _AtmIfIispAddrPnniInfoStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 7, 4, 3, 1, 1, 4),
    _AtmIfIispAddrPnniInfoStorageType_Type()
)
atmIfIispAddrPnniInfoStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfIispAddrPnniInfoStorageType.setStatus("mandatory")
_AtmIfIispAddrPnniInfoIndex_Type = NonReplicated
_AtmIfIispAddrPnniInfoIndex_Object = MibTableColumn
atmIfIispAddrPnniInfoIndex = _AtmIfIispAddrPnniInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 7, 4, 3, 1, 1, 10),
    _AtmIfIispAddrPnniInfoIndex_Type()
)
atmIfIispAddrPnniInfoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmIfIispAddrPnniInfoIndex.setStatus("mandatory")
_AtmIfIispAddrPnniInfoProvTable_Object = MibTable
atmIfIispAddrPnniInfoProvTable = _AtmIfIispAddrPnniInfoProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 7, 4, 3, 10)
)
if mibBuilder.loadTexts:
    atmIfIispAddrPnniInfoProvTable.setStatus("mandatory")
_AtmIfIispAddrPnniInfoProvEntry_Object = MibTableRow
atmIfIispAddrPnniInfoProvEntry = _AtmIfIispAddrPnniInfoProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 7, 4, 3, 10, 1)
)
atmIfIispAddrPnniInfoProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmIispMIB", "atmIfIispIndex"),
    (0, "Nortel-Magellan-Passport-AtmIispMIB", "atmIfIispAddrAddressIndex"),
    (0, "Nortel-Magellan-Passport-AtmIispMIB", "atmIfIispAddrAddressTypeIndex"),
    (0, "Nortel-Magellan-Passport-AtmIispMIB", "atmIfIispAddrPnniInfoIndex"),
)
if mibBuilder.loadTexts:
    atmIfIispAddrPnniInfoProvEntry.setStatus("mandatory")


class _AtmIfIispAddrPnniInfoScope_Type(Integer32):
    """Custom type atmIfIispAddrPnniInfoScope based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 104),
    )


_AtmIfIispAddrPnniInfoScope_Type.__name__ = "Integer32"
_AtmIfIispAddrPnniInfoScope_Object = MibTableColumn
atmIfIispAddrPnniInfoScope = _AtmIfIispAddrPnniInfoScope_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 7, 4, 3, 10, 1, 1),
    _AtmIfIispAddrPnniInfoScope_Type()
)
atmIfIispAddrPnniInfoScope.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfIispAddrPnniInfoScope.setStatus("mandatory")


class _AtmIfIispAddrPnniInfoReachability_Type(Integer32):
    """Custom type atmIfIispAddrPnniInfoReachability based on Integer32"""
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


_AtmIfIispAddrPnniInfoReachability_Type.__name__ = "Integer32"
_AtmIfIispAddrPnniInfoReachability_Object = MibTableColumn
atmIfIispAddrPnniInfoReachability = _AtmIfIispAddrPnniInfoReachability_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 7, 4, 3, 10, 1, 2),
    _AtmIfIispAddrPnniInfoReachability_Type()
)
atmIfIispAddrPnniInfoReachability.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfIispAddrPnniInfoReachability.setStatus("mandatory")
_AtmIfIispAddrOperTable_Object = MibTable
atmIfIispAddrOperTable = _AtmIfIispAddrOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 7, 4, 10)
)
if mibBuilder.loadTexts:
    atmIfIispAddrOperTable.setStatus("mandatory")
_AtmIfIispAddrOperEntry_Object = MibTableRow
atmIfIispAddrOperEntry = _AtmIfIispAddrOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 7, 4, 10, 1)
)
atmIfIispAddrOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmIispMIB", "atmIfIispIndex"),
    (0, "Nortel-Magellan-Passport-AtmIispMIB", "atmIfIispAddrAddressIndex"),
    (0, "Nortel-Magellan-Passport-AtmIispMIB", "atmIfIispAddrAddressTypeIndex"),
)
if mibBuilder.loadTexts:
    atmIfIispAddrOperEntry.setStatus("mandatory")


class _AtmIfIispAddrScope_Type(Integer32):
    """Custom type atmIfIispAddrScope based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 104),
    )


_AtmIfIispAddrScope_Type.__name__ = "Integer32"
_AtmIfIispAddrScope_Object = MibTableColumn
atmIfIispAddrScope = _AtmIfIispAddrScope_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 7, 4, 10, 1, 1),
    _AtmIfIispAddrScope_Type()
)
atmIfIispAddrScope.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfIispAddrScope.setStatus("mandatory")


class _AtmIfIispAddrReachability_Type(Integer32):
    """Custom type atmIfIispAddrReachability based on Integer32"""
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


_AtmIfIispAddrReachability_Type.__name__ = "Integer32"
_AtmIfIispAddrReachability_Object = MibTableColumn
atmIfIispAddrReachability = _AtmIfIispAddrReachability_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 7, 4, 10, 1, 2),
    _AtmIfIispAddrReachability_Type()
)
atmIfIispAddrReachability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfIispAddrReachability.setStatus("mandatory")
_AtmIfIispProvTable_Object = MibTable
atmIfIispProvTable = _AtmIfIispProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 7, 10)
)
if mibBuilder.loadTexts:
    atmIfIispProvTable.setStatus("mandatory")
_AtmIfIispProvEntry_Object = MibTableRow
atmIfIispProvEntry = _AtmIfIispProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 7, 10, 1)
)
atmIfIispProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmIispMIB", "atmIfIispIndex"),
)
if mibBuilder.loadTexts:
    atmIfIispProvEntry.setStatus("mandatory")


class _AtmIfIispVersion_Type(Integer32):
    """Custom type atmIfIispVersion based on Integer32"""
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


_AtmIfIispVersion_Type.__name__ = "Integer32"
_AtmIfIispVersion_Object = MibTableColumn
atmIfIispVersion = _AtmIfIispVersion_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 7, 10, 1, 1),
    _AtmIfIispVersion_Type()
)
atmIfIispVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfIispVersion.setStatus("mandatory")


class _AtmIfIispSide_Type(Integer32):
    """Custom type atmIfIispSide based on Integer32"""
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


_AtmIfIispSide_Type.__name__ = "Integer32"
_AtmIfIispSide_Object = MibTableColumn
atmIfIispSide = _AtmIfIispSide_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 7, 10, 1, 2),
    _AtmIfIispSide_Type()
)
atmIfIispSide.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfIispSide.setStatus("mandatory")


class _AtmIfIispSoftPvcRetryPeriod_Type(Unsigned32):
    """Custom type atmIfIispSoftPvcRetryPeriod based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 999999),
    )


_AtmIfIispSoftPvcRetryPeriod_Type.__name__ = "Unsigned32"
_AtmIfIispSoftPvcRetryPeriod_Object = MibTableColumn
atmIfIispSoftPvcRetryPeriod = _AtmIfIispSoftPvcRetryPeriod_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 7, 10, 1, 3),
    _AtmIfIispSoftPvcRetryPeriod_Type()
)
atmIfIispSoftPvcRetryPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfIispSoftPvcRetryPeriod.setStatus("obsolete")


class _AtmIfIispSoftPvpAndPvcRetryPeriod_Type(Unsigned32):
    """Custom type atmIfIispSoftPvpAndPvcRetryPeriod based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 999999),
    )


_AtmIfIispSoftPvpAndPvcRetryPeriod_Type.__name__ = "Unsigned32"
_AtmIfIispSoftPvpAndPvcRetryPeriod_Object = MibTableColumn
atmIfIispSoftPvpAndPvcRetryPeriod = _AtmIfIispSoftPvpAndPvcRetryPeriod_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 7, 10, 1, 4),
    _AtmIfIispSoftPvpAndPvcRetryPeriod_Type()
)
atmIfIispSoftPvpAndPvcRetryPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfIispSoftPvpAndPvcRetryPeriod.setStatus("mandatory")


class _AtmIfIispSoftPvpAndPvcHoldOffTime_Type(Unsigned32):
    """Custom type atmIfIispSoftPvpAndPvcHoldOffTime based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(50, 20000),
    )


_AtmIfIispSoftPvpAndPvcHoldOffTime_Type.__name__ = "Unsigned32"
_AtmIfIispSoftPvpAndPvcHoldOffTime_Object = MibTableColumn
atmIfIispSoftPvpAndPvcHoldOffTime = _AtmIfIispSoftPvpAndPvcHoldOffTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 7, 10, 1, 5),
    _AtmIfIispSoftPvpAndPvcHoldOffTime_Type()
)
atmIfIispSoftPvpAndPvcHoldOffTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfIispSoftPvpAndPvcHoldOffTime.setStatus("mandatory")
_AtmIfIispAcctOptTable_Object = MibTable
atmIfIispAcctOptTable = _AtmIfIispAcctOptTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 7, 11)
)
if mibBuilder.loadTexts:
    atmIfIispAcctOptTable.setStatus("mandatory")
_AtmIfIispAcctOptEntry_Object = MibTableRow
atmIfIispAcctOptEntry = _AtmIfIispAcctOptEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 7, 11, 1)
)
atmIfIispAcctOptEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmIispMIB", "atmIfIispIndex"),
)
if mibBuilder.loadTexts:
    atmIfIispAcctOptEntry.setStatus("mandatory")


class _AtmIfIispAccountCollection_Type(OctetString):
    """Custom type atmIfIispAccountCollection based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_AtmIfIispAccountCollection_Type.__name__ = "OctetString"
_AtmIfIispAccountCollection_Object = MibTableColumn
atmIfIispAccountCollection = _AtmIfIispAccountCollection_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 7, 11, 1, 1),
    _AtmIfIispAccountCollection_Type()
)
atmIfIispAccountCollection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfIispAccountCollection.setStatus("mandatory")


class _AtmIfIispAccountConnectionType_Type(Integer32):
    """Custom type atmIfIispAccountConnectionType based on Integer32"""
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


_AtmIfIispAccountConnectionType_Type.__name__ = "Integer32"
_AtmIfIispAccountConnectionType_Object = MibTableColumn
atmIfIispAccountConnectionType = _AtmIfIispAccountConnectionType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 7, 11, 1, 2),
    _AtmIfIispAccountConnectionType_Type()
)
atmIfIispAccountConnectionType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfIispAccountConnectionType.setStatus("mandatory")


class _AtmIfIispAccountClass_Type(Unsigned32):
    """Custom type atmIfIispAccountClass based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AtmIfIispAccountClass_Type.__name__ = "Unsigned32"
_AtmIfIispAccountClass_Object = MibTableColumn
atmIfIispAccountClass = _AtmIfIispAccountClass_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 7, 11, 1, 3),
    _AtmIfIispAccountClass_Type()
)
atmIfIispAccountClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfIispAccountClass.setStatus("mandatory")


class _AtmIfIispServiceExchange_Type(Unsigned32):
    """Custom type atmIfIispServiceExchange based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AtmIfIispServiceExchange_Type.__name__ = "Unsigned32"
_AtmIfIispServiceExchange_Object = MibTableColumn
atmIfIispServiceExchange = _AtmIfIispServiceExchange_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 7, 11, 1, 4),
    _AtmIfIispServiceExchange_Type()
)
atmIfIispServiceExchange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfIispServiceExchange.setStatus("mandatory")
_AtmIfVptIisp_ObjectIdentity = ObjectIdentity
atmIfVptIisp = _AtmIfVptIisp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 6)
)
_AtmIfVptIispRowStatusTable_Object = MibTable
atmIfVptIispRowStatusTable = _AtmIfVptIispRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 6, 1)
)
if mibBuilder.loadTexts:
    atmIfVptIispRowStatusTable.setStatus("mandatory")
_AtmIfVptIispRowStatusEntry_Object = MibTableRow
atmIfVptIispRowStatusEntry = _AtmIfVptIispRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 6, 1, 1)
)
atmIfVptIispRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfVptIndex"),
    (0, "Nortel-Magellan-Passport-AtmIispMIB", "atmIfVptIispIndex"),
)
if mibBuilder.loadTexts:
    atmIfVptIispRowStatusEntry.setStatus("mandatory")
_AtmIfVptIispRowStatus_Type = RowStatus
_AtmIfVptIispRowStatus_Object = MibTableColumn
atmIfVptIispRowStatus = _AtmIfVptIispRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 6, 1, 1, 1),
    _AtmIfVptIispRowStatus_Type()
)
atmIfVptIispRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfVptIispRowStatus.setStatus("mandatory")
_AtmIfVptIispComponentName_Type = DisplayString
_AtmIfVptIispComponentName_Object = MibTableColumn
atmIfVptIispComponentName = _AtmIfVptIispComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 6, 1, 1, 2),
    _AtmIfVptIispComponentName_Type()
)
atmIfVptIispComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVptIispComponentName.setStatus("mandatory")
_AtmIfVptIispStorageType_Type = StorageType
_AtmIfVptIispStorageType_Object = MibTableColumn
atmIfVptIispStorageType = _AtmIfVptIispStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 6, 1, 1, 4),
    _AtmIfVptIispStorageType_Type()
)
atmIfVptIispStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVptIispStorageType.setStatus("mandatory")
_AtmIfVptIispIndex_Type = NonReplicated
_AtmIfVptIispIndex_Object = MibTableColumn
atmIfVptIispIndex = _AtmIfVptIispIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 6, 1, 1, 10),
    _AtmIfVptIispIndex_Type()
)
atmIfVptIispIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmIfVptIispIndex.setStatus("mandatory")
_AtmIfVptIispSig_ObjectIdentity = ObjectIdentity
atmIfVptIispSig = _AtmIfVptIispSig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 6, 3)
)
_AtmIfVptIispSigRowStatusTable_Object = MibTable
atmIfVptIispSigRowStatusTable = _AtmIfVptIispSigRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 6, 3, 1)
)
if mibBuilder.loadTexts:
    atmIfVptIispSigRowStatusTable.setStatus("mandatory")
_AtmIfVptIispSigRowStatusEntry_Object = MibTableRow
atmIfVptIispSigRowStatusEntry = _AtmIfVptIispSigRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 6, 3, 1, 1)
)
atmIfVptIispSigRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfVptIndex"),
    (0, "Nortel-Magellan-Passport-AtmIispMIB", "atmIfVptIispIndex"),
    (0, "Nortel-Magellan-Passport-AtmIispMIB", "atmIfVptIispSigIndex"),
)
if mibBuilder.loadTexts:
    atmIfVptIispSigRowStatusEntry.setStatus("mandatory")
_AtmIfVptIispSigRowStatus_Type = RowStatus
_AtmIfVptIispSigRowStatus_Object = MibTableColumn
atmIfVptIispSigRowStatus = _AtmIfVptIispSigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 6, 3, 1, 1, 1),
    _AtmIfVptIispSigRowStatus_Type()
)
atmIfVptIispSigRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVptIispSigRowStatus.setStatus("mandatory")
_AtmIfVptIispSigComponentName_Type = DisplayString
_AtmIfVptIispSigComponentName_Object = MibTableColumn
atmIfVptIispSigComponentName = _AtmIfVptIispSigComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 6, 3, 1, 1, 2),
    _AtmIfVptIispSigComponentName_Type()
)
atmIfVptIispSigComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVptIispSigComponentName.setStatus("mandatory")
_AtmIfVptIispSigStorageType_Type = StorageType
_AtmIfVptIispSigStorageType_Object = MibTableColumn
atmIfVptIispSigStorageType = _AtmIfVptIispSigStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 6, 3, 1, 1, 4),
    _AtmIfVptIispSigStorageType_Type()
)
atmIfVptIispSigStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVptIispSigStorageType.setStatus("mandatory")
_AtmIfVptIispSigIndex_Type = NonReplicated
_AtmIfVptIispSigIndex_Object = MibTableColumn
atmIfVptIispSigIndex = _AtmIfVptIispSigIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 6, 3, 1, 1, 10),
    _AtmIfVptIispSigIndex_Type()
)
atmIfVptIispSigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmIfVptIispSigIndex.setStatus("mandatory")
_AtmIfVptIispSigVcd_ObjectIdentity = ObjectIdentity
atmIfVptIispSigVcd = _AtmIfVptIispSigVcd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 6, 3, 2)
)
_AtmIfVptIispSigVcdRowStatusTable_Object = MibTable
atmIfVptIispSigVcdRowStatusTable = _AtmIfVptIispSigVcdRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 6, 3, 2, 1)
)
if mibBuilder.loadTexts:
    atmIfVptIispSigVcdRowStatusTable.setStatus("mandatory")
_AtmIfVptIispSigVcdRowStatusEntry_Object = MibTableRow
atmIfVptIispSigVcdRowStatusEntry = _AtmIfVptIispSigVcdRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 6, 3, 2, 1, 1)
)
atmIfVptIispSigVcdRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfVptIndex"),
    (0, "Nortel-Magellan-Passport-AtmIispMIB", "atmIfVptIispIndex"),
    (0, "Nortel-Magellan-Passport-AtmIispMIB", "atmIfVptIispSigIndex"),
    (0, "Nortel-Magellan-Passport-AtmIispMIB", "atmIfVptIispSigVcdIndex"),
)
if mibBuilder.loadTexts:
    atmIfVptIispSigVcdRowStatusEntry.setStatus("mandatory")
_AtmIfVptIispSigVcdRowStatus_Type = RowStatus
_AtmIfVptIispSigVcdRowStatus_Object = MibTableColumn
atmIfVptIispSigVcdRowStatus = _AtmIfVptIispSigVcdRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 6, 3, 2, 1, 1, 1),
    _AtmIfVptIispSigVcdRowStatus_Type()
)
atmIfVptIispSigVcdRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfVptIispSigVcdRowStatus.setStatus("mandatory")
_AtmIfVptIispSigVcdComponentName_Type = DisplayString
_AtmIfVptIispSigVcdComponentName_Object = MibTableColumn
atmIfVptIispSigVcdComponentName = _AtmIfVptIispSigVcdComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 6, 3, 2, 1, 1, 2),
    _AtmIfVptIispSigVcdComponentName_Type()
)
atmIfVptIispSigVcdComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVptIispSigVcdComponentName.setStatus("mandatory")
_AtmIfVptIispSigVcdStorageType_Type = StorageType
_AtmIfVptIispSigVcdStorageType_Object = MibTableColumn
atmIfVptIispSigVcdStorageType = _AtmIfVptIispSigVcdStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 6, 3, 2, 1, 1, 4),
    _AtmIfVptIispSigVcdStorageType_Type()
)
atmIfVptIispSigVcdStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVptIispSigVcdStorageType.setStatus("mandatory")
_AtmIfVptIispSigVcdIndex_Type = NonReplicated
_AtmIfVptIispSigVcdIndex_Object = MibTableColumn
atmIfVptIispSigVcdIndex = _AtmIfVptIispSigVcdIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 6, 3, 2, 1, 1, 10),
    _AtmIfVptIispSigVcdIndex_Type()
)
atmIfVptIispSigVcdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmIfVptIispSigVcdIndex.setStatus("mandatory")
_AtmIfVptIispSigVcdProvTable_Object = MibTable
atmIfVptIispSigVcdProvTable = _AtmIfVptIispSigVcdProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 6, 3, 2, 10)
)
if mibBuilder.loadTexts:
    atmIfVptIispSigVcdProvTable.setStatus("mandatory")
_AtmIfVptIispSigVcdProvEntry_Object = MibTableRow
atmIfVptIispSigVcdProvEntry = _AtmIfVptIispSigVcdProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 6, 3, 2, 10, 1)
)
atmIfVptIispSigVcdProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfVptIndex"),
    (0, "Nortel-Magellan-Passport-AtmIispMIB", "atmIfVptIispIndex"),
    (0, "Nortel-Magellan-Passport-AtmIispMIB", "atmIfVptIispSigIndex"),
    (0, "Nortel-Magellan-Passport-AtmIispMIB", "atmIfVptIispSigVcdIndex"),
)
if mibBuilder.loadTexts:
    atmIfVptIispSigVcdProvEntry.setStatus("mandatory")


class _AtmIfVptIispSigVcdTrafficDescType_Type(Integer32):
    """Custom type atmIfVptIispSigVcdTrafficDescType based on Integer32"""
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


_AtmIfVptIispSigVcdTrafficDescType_Type.__name__ = "Integer32"
_AtmIfVptIispSigVcdTrafficDescType_Object = MibTableColumn
atmIfVptIispSigVcdTrafficDescType = _AtmIfVptIispSigVcdTrafficDescType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 6, 3, 2, 10, 1, 1),
    _AtmIfVptIispSigVcdTrafficDescType_Type()
)
atmIfVptIispSigVcdTrafficDescType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfVptIispSigVcdTrafficDescType.setStatus("mandatory")


class _AtmIfVptIispSigVcdAtmServiceCategory_Type(Integer32):
    """Custom type atmIfVptIispSigVcdAtmServiceCategory based on Integer32"""
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


_AtmIfVptIispSigVcdAtmServiceCategory_Type.__name__ = "Integer32"
_AtmIfVptIispSigVcdAtmServiceCategory_Object = MibTableColumn
atmIfVptIispSigVcdAtmServiceCategory = _AtmIfVptIispSigVcdAtmServiceCategory_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 6, 3, 2, 10, 1, 3),
    _AtmIfVptIispSigVcdAtmServiceCategory_Type()
)
atmIfVptIispSigVcdAtmServiceCategory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfVptIispSigVcdAtmServiceCategory.setStatus("mandatory")


class _AtmIfVptIispSigVcdQosClass_Type(Integer32):
    """Custom type atmIfVptIispSigVcdQosClass based on Integer32"""
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


_AtmIfVptIispSigVcdQosClass_Type.__name__ = "Integer32"
_AtmIfVptIispSigVcdQosClass_Object = MibTableColumn
atmIfVptIispSigVcdQosClass = _AtmIfVptIispSigVcdQosClass_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 6, 3, 2, 10, 1, 21),
    _AtmIfVptIispSigVcdQosClass_Type()
)
atmIfVptIispSigVcdQosClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfVptIispSigVcdQosClass.setStatus("mandatory")


class _AtmIfVptIispSigVcdTrafficShaping_Type(Integer32):
    """Custom type atmIfVptIispSigVcdTrafficShaping based on Integer32"""
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


_AtmIfVptIispSigVcdTrafficShaping_Type.__name__ = "Integer32"
_AtmIfVptIispSigVcdTrafficShaping_Object = MibTableColumn
atmIfVptIispSigVcdTrafficShaping = _AtmIfVptIispSigVcdTrafficShaping_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 6, 3, 2, 10, 1, 50),
    _AtmIfVptIispSigVcdTrafficShaping_Type()
)
atmIfVptIispSigVcdTrafficShaping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfVptIispSigVcdTrafficShaping.setStatus("mandatory")


class _AtmIfVptIispSigVcdUnshapedTransmitQueueing_Type(Integer32):
    """Custom type atmIfVptIispSigVcdUnshapedTransmitQueueing based on Integer32"""
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


_AtmIfVptIispSigVcdUnshapedTransmitQueueing_Type.__name__ = "Integer32"
_AtmIfVptIispSigVcdUnshapedTransmitQueueing_Object = MibTableColumn
atmIfVptIispSigVcdUnshapedTransmitQueueing = _AtmIfVptIispSigVcdUnshapedTransmitQueueing_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 6, 3, 2, 10, 1, 60),
    _AtmIfVptIispSigVcdUnshapedTransmitQueueing_Type()
)
atmIfVptIispSigVcdUnshapedTransmitQueueing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfVptIispSigVcdUnshapedTransmitQueueing.setStatus("mandatory")


class _AtmIfVptIispSigVcdUsageParameterControl_Type(Integer32):
    """Custom type atmIfVptIispSigVcdUsageParameterControl based on Integer32"""
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


_AtmIfVptIispSigVcdUsageParameterControl_Type.__name__ = "Integer32"
_AtmIfVptIispSigVcdUsageParameterControl_Object = MibTableColumn
atmIfVptIispSigVcdUsageParameterControl = _AtmIfVptIispSigVcdUsageParameterControl_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 6, 3, 2, 10, 1, 70),
    _AtmIfVptIispSigVcdUsageParameterControl_Type()
)
atmIfVptIispSigVcdUsageParameterControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfVptIispSigVcdUsageParameterControl.setStatus("mandatory")
_AtmIfVptIispSigVcdTdpTable_Object = MibTable
atmIfVptIispSigVcdTdpTable = _AtmIfVptIispSigVcdTdpTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 6, 3, 2, 387)
)
if mibBuilder.loadTexts:
    atmIfVptIispSigVcdTdpTable.setStatus("mandatory")
_AtmIfVptIispSigVcdTdpEntry_Object = MibTableRow
atmIfVptIispSigVcdTdpEntry = _AtmIfVptIispSigVcdTdpEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 6, 3, 2, 387, 1)
)
atmIfVptIispSigVcdTdpEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfVptIndex"),
    (0, "Nortel-Magellan-Passport-AtmIispMIB", "atmIfVptIispIndex"),
    (0, "Nortel-Magellan-Passport-AtmIispMIB", "atmIfVptIispSigIndex"),
    (0, "Nortel-Magellan-Passport-AtmIispMIB", "atmIfVptIispSigVcdIndex"),
    (0, "Nortel-Magellan-Passport-AtmIispMIB", "atmIfVptIispSigVcdTdpIndex"),
)
if mibBuilder.loadTexts:
    atmIfVptIispSigVcdTdpEntry.setStatus("mandatory")


class _AtmIfVptIispSigVcdTdpIndex_Type(Integer32):
    """Custom type atmIfVptIispSigVcdTdpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_AtmIfVptIispSigVcdTdpIndex_Type.__name__ = "Integer32"
_AtmIfVptIispSigVcdTdpIndex_Object = MibTableColumn
atmIfVptIispSigVcdTdpIndex = _AtmIfVptIispSigVcdTdpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 6, 3, 2, 387, 1, 1),
    _AtmIfVptIispSigVcdTdpIndex_Type()
)
atmIfVptIispSigVcdTdpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmIfVptIispSigVcdTdpIndex.setStatus("mandatory")


class _AtmIfVptIispSigVcdTdpValue_Type(Unsigned32):
    """Custom type atmIfVptIispSigVcdTdpValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AtmIfVptIispSigVcdTdpValue_Type.__name__ = "Unsigned32"
_AtmIfVptIispSigVcdTdpValue_Object = MibTableColumn
atmIfVptIispSigVcdTdpValue = _AtmIfVptIispSigVcdTdpValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 6, 3, 2, 387, 1, 2),
    _AtmIfVptIispSigVcdTdpValue_Type()
)
atmIfVptIispSigVcdTdpValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfVptIispSigVcdTdpValue.setStatus("mandatory")
_AtmIfVptIispSigProvTable_Object = MibTable
atmIfVptIispSigProvTable = _AtmIfVptIispSigProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 6, 3, 10)
)
if mibBuilder.loadTexts:
    atmIfVptIispSigProvTable.setStatus("mandatory")
_AtmIfVptIispSigProvEntry_Object = MibTableRow
atmIfVptIispSigProvEntry = _AtmIfVptIispSigProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 6, 3, 10, 1)
)
atmIfVptIispSigProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfVptIndex"),
    (0, "Nortel-Magellan-Passport-AtmIispMIB", "atmIfVptIispIndex"),
    (0, "Nortel-Magellan-Passport-AtmIispMIB", "atmIfVptIispSigIndex"),
)
if mibBuilder.loadTexts:
    atmIfVptIispSigProvEntry.setStatus("mandatory")


class _AtmIfVptIispSigVci_Type(Unsigned32):
    """Custom type atmIfVptIispSigVci based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AtmIfVptIispSigVci_Type.__name__ = "Unsigned32"
_AtmIfVptIispSigVci_Object = MibTableColumn
atmIfVptIispSigVci = _AtmIfVptIispSigVci_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 6, 3, 10, 1, 1),
    _AtmIfVptIispSigVci_Type()
)
atmIfVptIispSigVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfVptIispSigVci.setStatus("mandatory")


class _AtmIfVptIispSigAddressConversion_Type(Integer32):
    """Custom type atmIfVptIispSigAddressConversion based on Integer32"""
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


_AtmIfVptIispSigAddressConversion_Type.__name__ = "Integer32"
_AtmIfVptIispSigAddressConversion_Object = MibTableColumn
atmIfVptIispSigAddressConversion = _AtmIfVptIispSigAddressConversion_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 6, 3, 10, 1, 2),
    _AtmIfVptIispSigAddressConversion_Type()
)
atmIfVptIispSigAddressConversion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfVptIispSigAddressConversion.setStatus("mandatory")
_AtmIfVptIispSigStateTable_Object = MibTable
atmIfVptIispSigStateTable = _AtmIfVptIispSigStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 6, 3, 11)
)
if mibBuilder.loadTexts:
    atmIfVptIispSigStateTable.setStatus("mandatory")
_AtmIfVptIispSigStateEntry_Object = MibTableRow
atmIfVptIispSigStateEntry = _AtmIfVptIispSigStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 6, 3, 11, 1)
)
atmIfVptIispSigStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfVptIndex"),
    (0, "Nortel-Magellan-Passport-AtmIispMIB", "atmIfVptIispIndex"),
    (0, "Nortel-Magellan-Passport-AtmIispMIB", "atmIfVptIispSigIndex"),
)
if mibBuilder.loadTexts:
    atmIfVptIispSigStateEntry.setStatus("mandatory")


class _AtmIfVptIispSigAdminState_Type(Integer32):
    """Custom type atmIfVptIispSigAdminState based on Integer32"""
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


_AtmIfVptIispSigAdminState_Type.__name__ = "Integer32"
_AtmIfVptIispSigAdminState_Object = MibTableColumn
atmIfVptIispSigAdminState = _AtmIfVptIispSigAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 6, 3, 11, 1, 1),
    _AtmIfVptIispSigAdminState_Type()
)
atmIfVptIispSigAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVptIispSigAdminState.setStatus("mandatory")


class _AtmIfVptIispSigOperationalState_Type(Integer32):
    """Custom type atmIfVptIispSigOperationalState based on Integer32"""
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


_AtmIfVptIispSigOperationalState_Type.__name__ = "Integer32"
_AtmIfVptIispSigOperationalState_Object = MibTableColumn
atmIfVptIispSigOperationalState = _AtmIfVptIispSigOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 6, 3, 11, 1, 2),
    _AtmIfVptIispSigOperationalState_Type()
)
atmIfVptIispSigOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVptIispSigOperationalState.setStatus("mandatory")


class _AtmIfVptIispSigUsageState_Type(Integer32):
    """Custom type atmIfVptIispSigUsageState based on Integer32"""
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


_AtmIfVptIispSigUsageState_Type.__name__ = "Integer32"
_AtmIfVptIispSigUsageState_Object = MibTableColumn
atmIfVptIispSigUsageState = _AtmIfVptIispSigUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 6, 3, 11, 1, 3),
    _AtmIfVptIispSigUsageState_Type()
)
atmIfVptIispSigUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVptIispSigUsageState.setStatus("mandatory")
_AtmIfVptIispSigOperTable_Object = MibTable
atmIfVptIispSigOperTable = _AtmIfVptIispSigOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 6, 3, 12)
)
if mibBuilder.loadTexts:
    atmIfVptIispSigOperTable.setStatus("mandatory")
_AtmIfVptIispSigOperEntry_Object = MibTableRow
atmIfVptIispSigOperEntry = _AtmIfVptIispSigOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 6, 3, 12, 1)
)
atmIfVptIispSigOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfVptIndex"),
    (0, "Nortel-Magellan-Passport-AtmIispMIB", "atmIfVptIispIndex"),
    (0, "Nortel-Magellan-Passport-AtmIispMIB", "atmIfVptIispSigIndex"),
)
if mibBuilder.loadTexts:
    atmIfVptIispSigOperEntry.setStatus("mandatory")


class _AtmIfVptIispSigLastTxCauseCode_Type(Unsigned32):
    """Custom type atmIfVptIispSigLastTxCauseCode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AtmIfVptIispSigLastTxCauseCode_Type.__name__ = "Unsigned32"
_AtmIfVptIispSigLastTxCauseCode_Object = MibTableColumn
atmIfVptIispSigLastTxCauseCode = _AtmIfVptIispSigLastTxCauseCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 6, 3, 12, 1, 1),
    _AtmIfVptIispSigLastTxCauseCode_Type()
)
atmIfVptIispSigLastTxCauseCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVptIispSigLastTxCauseCode.setStatus("mandatory")


class _AtmIfVptIispSigLastTxDiagCode_Type(Hex):
    """Custom type atmIfVptIispSigLastTxDiagCode based on Hex"""
    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AtmIfVptIispSigLastTxDiagCode_Type.__name__ = "Hex"
_AtmIfVptIispSigLastTxDiagCode_Object = MibTableColumn
atmIfVptIispSigLastTxDiagCode = _AtmIfVptIispSigLastTxDiagCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 6, 3, 12, 1, 2),
    _AtmIfVptIispSigLastTxDiagCode_Type()
)
atmIfVptIispSigLastTxDiagCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVptIispSigLastTxDiagCode.setStatus("mandatory")


class _AtmIfVptIispSigLastRxCauseCode_Type(Unsigned32):
    """Custom type atmIfVptIispSigLastRxCauseCode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AtmIfVptIispSigLastRxCauseCode_Type.__name__ = "Unsigned32"
_AtmIfVptIispSigLastRxCauseCode_Object = MibTableColumn
atmIfVptIispSigLastRxCauseCode = _AtmIfVptIispSigLastRxCauseCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 6, 3, 12, 1, 3),
    _AtmIfVptIispSigLastRxCauseCode_Type()
)
atmIfVptIispSigLastRxCauseCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVptIispSigLastRxCauseCode.setStatus("mandatory")


class _AtmIfVptIispSigLastRxDiagCode_Type(Hex):
    """Custom type atmIfVptIispSigLastRxDiagCode based on Hex"""
    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AtmIfVptIispSigLastRxDiagCode_Type.__name__ = "Hex"
_AtmIfVptIispSigLastRxDiagCode_Object = MibTableColumn
atmIfVptIispSigLastRxDiagCode = _AtmIfVptIispSigLastRxDiagCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 6, 3, 12, 1, 4),
    _AtmIfVptIispSigLastRxDiagCode_Type()
)
atmIfVptIispSigLastRxDiagCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVptIispSigLastRxDiagCode.setStatus("mandatory")
_AtmIfVptIispSigStatsTable_Object = MibTable
atmIfVptIispSigStatsTable = _AtmIfVptIispSigStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 6, 3, 13)
)
if mibBuilder.loadTexts:
    atmIfVptIispSigStatsTable.setStatus("mandatory")
_AtmIfVptIispSigStatsEntry_Object = MibTableRow
atmIfVptIispSigStatsEntry = _AtmIfVptIispSigStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 6, 3, 13, 1)
)
atmIfVptIispSigStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfVptIndex"),
    (0, "Nortel-Magellan-Passport-AtmIispMIB", "atmIfVptIispIndex"),
    (0, "Nortel-Magellan-Passport-AtmIispMIB", "atmIfVptIispSigIndex"),
)
if mibBuilder.loadTexts:
    atmIfVptIispSigStatsEntry.setStatus("mandatory")
_AtmIfVptIispSigCurrentConnections_Type = Counter32
_AtmIfVptIispSigCurrentConnections_Object = MibTableColumn
atmIfVptIispSigCurrentConnections = _AtmIfVptIispSigCurrentConnections_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 6, 3, 13, 1, 1),
    _AtmIfVptIispSigCurrentConnections_Type()
)
atmIfVptIispSigCurrentConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVptIispSigCurrentConnections.setStatus("obsolete")


class _AtmIfVptIispSigPeakConnections_Type(Gauge32):
    """Custom type atmIfVptIispSigPeakConnections based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AtmIfVptIispSigPeakConnections_Type.__name__ = "Gauge32"
_AtmIfVptIispSigPeakConnections_Object = MibTableColumn
atmIfVptIispSigPeakConnections = _AtmIfVptIispSigPeakConnections_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 6, 3, 13, 1, 2),
    _AtmIfVptIispSigPeakConnections_Type()
)
atmIfVptIispSigPeakConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVptIispSigPeakConnections.setStatus("mandatory")
_AtmIfVptIispSigSuccessfulConnections_Type = Counter32
_AtmIfVptIispSigSuccessfulConnections_Object = MibTableColumn
atmIfVptIispSigSuccessfulConnections = _AtmIfVptIispSigSuccessfulConnections_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 6, 3, 13, 1, 3),
    _AtmIfVptIispSigSuccessfulConnections_Type()
)
atmIfVptIispSigSuccessfulConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVptIispSigSuccessfulConnections.setStatus("mandatory")
_AtmIfVptIispSigFailedConnections_Type = Counter32
_AtmIfVptIispSigFailedConnections_Object = MibTableColumn
atmIfVptIispSigFailedConnections = _AtmIfVptIispSigFailedConnections_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 6, 3, 13, 1, 4),
    _AtmIfVptIispSigFailedConnections_Type()
)
atmIfVptIispSigFailedConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVptIispSigFailedConnections.setStatus("mandatory")
_AtmIfVptIispSigTxPdus_Type = Counter32
_AtmIfVptIispSigTxPdus_Object = MibTableColumn
atmIfVptIispSigTxPdus = _AtmIfVptIispSigTxPdus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 6, 3, 13, 1, 5),
    _AtmIfVptIispSigTxPdus_Type()
)
atmIfVptIispSigTxPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVptIispSigTxPdus.setStatus("mandatory")
_AtmIfVptIispSigRxPdus_Type = Counter32
_AtmIfVptIispSigRxPdus_Object = MibTableColumn
atmIfVptIispSigRxPdus = _AtmIfVptIispSigRxPdus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 6, 3, 13, 1, 6),
    _AtmIfVptIispSigRxPdus_Type()
)
atmIfVptIispSigRxPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVptIispSigRxPdus.setStatus("mandatory")


class _AtmIfVptIispSigCurrentPmpConnections_Type(Gauge32):
    """Custom type atmIfVptIispSigCurrentPmpConnections based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AtmIfVptIispSigCurrentPmpConnections_Type.__name__ = "Gauge32"
_AtmIfVptIispSigCurrentPmpConnections_Object = MibTableColumn
atmIfVptIispSigCurrentPmpConnections = _AtmIfVptIispSigCurrentPmpConnections_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 6, 3, 13, 1, 7),
    _AtmIfVptIispSigCurrentPmpConnections_Type()
)
atmIfVptIispSigCurrentPmpConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVptIispSigCurrentPmpConnections.setStatus("mandatory")


class _AtmIfVptIispSigPeakPmpConnections_Type(Gauge32):
    """Custom type atmIfVptIispSigPeakPmpConnections based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AtmIfVptIispSigPeakPmpConnections_Type.__name__ = "Gauge32"
_AtmIfVptIispSigPeakPmpConnections_Object = MibTableColumn
atmIfVptIispSigPeakPmpConnections = _AtmIfVptIispSigPeakPmpConnections_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 6, 3, 13, 1, 8),
    _AtmIfVptIispSigPeakPmpConnections_Type()
)
atmIfVptIispSigPeakPmpConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVptIispSigPeakPmpConnections.setStatus("mandatory")
_AtmIfVptIispSigSuccessfulPmpConnections_Type = Counter32
_AtmIfVptIispSigSuccessfulPmpConnections_Object = MibTableColumn
atmIfVptIispSigSuccessfulPmpConnections = _AtmIfVptIispSigSuccessfulPmpConnections_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 6, 3, 13, 1, 9),
    _AtmIfVptIispSigSuccessfulPmpConnections_Type()
)
atmIfVptIispSigSuccessfulPmpConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVptIispSigSuccessfulPmpConnections.setStatus("mandatory")
_AtmIfVptIispSigFailedPmpConnections_Type = Counter32
_AtmIfVptIispSigFailedPmpConnections_Object = MibTableColumn
atmIfVptIispSigFailedPmpConnections = _AtmIfVptIispSigFailedPmpConnections_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 6, 3, 13, 1, 10),
    _AtmIfVptIispSigFailedPmpConnections_Type()
)
atmIfVptIispSigFailedPmpConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVptIispSigFailedPmpConnections.setStatus("mandatory")


class _AtmIfVptIispSigNewCurrentConnections_Type(Gauge32):
    """Custom type atmIfVptIispSigNewCurrentConnections based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AtmIfVptIispSigNewCurrentConnections_Type.__name__ = "Gauge32"
_AtmIfVptIispSigNewCurrentConnections_Object = MibTableColumn
atmIfVptIispSigNewCurrentConnections = _AtmIfVptIispSigNewCurrentConnections_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 6, 3, 13, 1, 11),
    _AtmIfVptIispSigNewCurrentConnections_Type()
)
atmIfVptIispSigNewCurrentConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVptIispSigNewCurrentConnections.setStatus("mandatory")
_AtmIfVptIispAddr_ObjectIdentity = ObjectIdentity
atmIfVptIispAddr = _AtmIfVptIispAddr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 6, 4)
)
_AtmIfVptIispAddrRowStatusTable_Object = MibTable
atmIfVptIispAddrRowStatusTable = _AtmIfVptIispAddrRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 6, 4, 1)
)
if mibBuilder.loadTexts:
    atmIfVptIispAddrRowStatusTable.setStatus("mandatory")
_AtmIfVptIispAddrRowStatusEntry_Object = MibTableRow
atmIfVptIispAddrRowStatusEntry = _AtmIfVptIispAddrRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 6, 4, 1, 1)
)
atmIfVptIispAddrRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfVptIndex"),
    (0, "Nortel-Magellan-Passport-AtmIispMIB", "atmIfVptIispIndex"),
    (0, "Nortel-Magellan-Passport-AtmIispMIB", "atmIfVptIispAddrAddressIndex"),
    (0, "Nortel-Magellan-Passport-AtmIispMIB", "atmIfVptIispAddrAddressTypeIndex"),
)
if mibBuilder.loadTexts:
    atmIfVptIispAddrRowStatusEntry.setStatus("mandatory")
_AtmIfVptIispAddrRowStatus_Type = RowStatus
_AtmIfVptIispAddrRowStatus_Object = MibTableColumn
atmIfVptIispAddrRowStatus = _AtmIfVptIispAddrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 6, 4, 1, 1, 1),
    _AtmIfVptIispAddrRowStatus_Type()
)
atmIfVptIispAddrRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfVptIispAddrRowStatus.setStatus("mandatory")
_AtmIfVptIispAddrComponentName_Type = DisplayString
_AtmIfVptIispAddrComponentName_Object = MibTableColumn
atmIfVptIispAddrComponentName = _AtmIfVptIispAddrComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 6, 4, 1, 1, 2),
    _AtmIfVptIispAddrComponentName_Type()
)
atmIfVptIispAddrComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVptIispAddrComponentName.setStatus("mandatory")
_AtmIfVptIispAddrStorageType_Type = StorageType
_AtmIfVptIispAddrStorageType_Object = MibTableColumn
atmIfVptIispAddrStorageType = _AtmIfVptIispAddrStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 6, 4, 1, 1, 4),
    _AtmIfVptIispAddrStorageType_Type()
)
atmIfVptIispAddrStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVptIispAddrStorageType.setStatus("mandatory")


class _AtmIfVptIispAddrAddressIndex_Type(AsciiStringIndex):
    """Custom type atmIfVptIispAddrAddressIndex based on AsciiStringIndex"""
    subtypeSpec = AsciiStringIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_AtmIfVptIispAddrAddressIndex_Type.__name__ = "AsciiStringIndex"
_AtmIfVptIispAddrAddressIndex_Object = MibTableColumn
atmIfVptIispAddrAddressIndex = _AtmIfVptIispAddrAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 6, 4, 1, 1, 10),
    _AtmIfVptIispAddrAddressIndex_Type()
)
atmIfVptIispAddrAddressIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmIfVptIispAddrAddressIndex.setStatus("mandatory")


class _AtmIfVptIispAddrAddressTypeIndex_Type(Integer32):
    """Custom type atmIfVptIispAddrAddressTypeIndex based on Integer32"""
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


_AtmIfVptIispAddrAddressTypeIndex_Type.__name__ = "Integer32"
_AtmIfVptIispAddrAddressTypeIndex_Object = MibTableColumn
atmIfVptIispAddrAddressTypeIndex = _AtmIfVptIispAddrAddressTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 6, 4, 1, 1, 11),
    _AtmIfVptIispAddrAddressTypeIndex_Type()
)
atmIfVptIispAddrAddressTypeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmIfVptIispAddrAddressTypeIndex.setStatus("mandatory")
_AtmIfVptIispAddrTermSP_ObjectIdentity = ObjectIdentity
atmIfVptIispAddrTermSP = _AtmIfVptIispAddrTermSP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 6, 4, 2)
)
_AtmIfVptIispAddrTermSPRowStatusTable_Object = MibTable
atmIfVptIispAddrTermSPRowStatusTable = _AtmIfVptIispAddrTermSPRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 6, 4, 2, 1)
)
if mibBuilder.loadTexts:
    atmIfVptIispAddrTermSPRowStatusTable.setStatus("mandatory")
_AtmIfVptIispAddrTermSPRowStatusEntry_Object = MibTableRow
atmIfVptIispAddrTermSPRowStatusEntry = _AtmIfVptIispAddrTermSPRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 6, 4, 2, 1, 1)
)
atmIfVptIispAddrTermSPRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfVptIndex"),
    (0, "Nortel-Magellan-Passport-AtmIispMIB", "atmIfVptIispIndex"),
    (0, "Nortel-Magellan-Passport-AtmIispMIB", "atmIfVptIispAddrAddressIndex"),
    (0, "Nortel-Magellan-Passport-AtmIispMIB", "atmIfVptIispAddrAddressTypeIndex"),
    (0, "Nortel-Magellan-Passport-AtmIispMIB", "atmIfVptIispAddrTermSPIndex"),
)
if mibBuilder.loadTexts:
    atmIfVptIispAddrTermSPRowStatusEntry.setStatus("mandatory")
_AtmIfVptIispAddrTermSPRowStatus_Type = RowStatus
_AtmIfVptIispAddrTermSPRowStatus_Object = MibTableColumn
atmIfVptIispAddrTermSPRowStatus = _AtmIfVptIispAddrTermSPRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 6, 4, 2, 1, 1, 1),
    _AtmIfVptIispAddrTermSPRowStatus_Type()
)
atmIfVptIispAddrTermSPRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfVptIispAddrTermSPRowStatus.setStatus("mandatory")
_AtmIfVptIispAddrTermSPComponentName_Type = DisplayString
_AtmIfVptIispAddrTermSPComponentName_Object = MibTableColumn
atmIfVptIispAddrTermSPComponentName = _AtmIfVptIispAddrTermSPComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 6, 4, 2, 1, 1, 2),
    _AtmIfVptIispAddrTermSPComponentName_Type()
)
atmIfVptIispAddrTermSPComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVptIispAddrTermSPComponentName.setStatus("mandatory")
_AtmIfVptIispAddrTermSPStorageType_Type = StorageType
_AtmIfVptIispAddrTermSPStorageType_Object = MibTableColumn
atmIfVptIispAddrTermSPStorageType = _AtmIfVptIispAddrTermSPStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 6, 4, 2, 1, 1, 4),
    _AtmIfVptIispAddrTermSPStorageType_Type()
)
atmIfVptIispAddrTermSPStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVptIispAddrTermSPStorageType.setStatus("mandatory")
_AtmIfVptIispAddrTermSPIndex_Type = NonReplicated
_AtmIfVptIispAddrTermSPIndex_Object = MibTableColumn
atmIfVptIispAddrTermSPIndex = _AtmIfVptIispAddrTermSPIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 6, 4, 2, 1, 1, 10),
    _AtmIfVptIispAddrTermSPIndex_Type()
)
atmIfVptIispAddrTermSPIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmIfVptIispAddrTermSPIndex.setStatus("mandatory")
_AtmIfVptIispAddrPnniInfo_ObjectIdentity = ObjectIdentity
atmIfVptIispAddrPnniInfo = _AtmIfVptIispAddrPnniInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 6, 4, 3)
)
_AtmIfVptIispAddrPnniInfoRowStatusTable_Object = MibTable
atmIfVptIispAddrPnniInfoRowStatusTable = _AtmIfVptIispAddrPnniInfoRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 6, 4, 3, 1)
)
if mibBuilder.loadTexts:
    atmIfVptIispAddrPnniInfoRowStatusTable.setStatus("mandatory")
_AtmIfVptIispAddrPnniInfoRowStatusEntry_Object = MibTableRow
atmIfVptIispAddrPnniInfoRowStatusEntry = _AtmIfVptIispAddrPnniInfoRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 6, 4, 3, 1, 1)
)
atmIfVptIispAddrPnniInfoRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfVptIndex"),
    (0, "Nortel-Magellan-Passport-AtmIispMIB", "atmIfVptIispIndex"),
    (0, "Nortel-Magellan-Passport-AtmIispMIB", "atmIfVptIispAddrAddressIndex"),
    (0, "Nortel-Magellan-Passport-AtmIispMIB", "atmIfVptIispAddrAddressTypeIndex"),
    (0, "Nortel-Magellan-Passport-AtmIispMIB", "atmIfVptIispAddrPnniInfoIndex"),
)
if mibBuilder.loadTexts:
    atmIfVptIispAddrPnniInfoRowStatusEntry.setStatus("mandatory")
_AtmIfVptIispAddrPnniInfoRowStatus_Type = RowStatus
_AtmIfVptIispAddrPnniInfoRowStatus_Object = MibTableColumn
atmIfVptIispAddrPnniInfoRowStatus = _AtmIfVptIispAddrPnniInfoRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 6, 4, 3, 1, 1, 1),
    _AtmIfVptIispAddrPnniInfoRowStatus_Type()
)
atmIfVptIispAddrPnniInfoRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfVptIispAddrPnniInfoRowStatus.setStatus("mandatory")
_AtmIfVptIispAddrPnniInfoComponentName_Type = DisplayString
_AtmIfVptIispAddrPnniInfoComponentName_Object = MibTableColumn
atmIfVptIispAddrPnniInfoComponentName = _AtmIfVptIispAddrPnniInfoComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 6, 4, 3, 1, 1, 2),
    _AtmIfVptIispAddrPnniInfoComponentName_Type()
)
atmIfVptIispAddrPnniInfoComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVptIispAddrPnniInfoComponentName.setStatus("mandatory")
_AtmIfVptIispAddrPnniInfoStorageType_Type = StorageType
_AtmIfVptIispAddrPnniInfoStorageType_Object = MibTableColumn
atmIfVptIispAddrPnniInfoStorageType = _AtmIfVptIispAddrPnniInfoStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 6, 4, 3, 1, 1, 4),
    _AtmIfVptIispAddrPnniInfoStorageType_Type()
)
atmIfVptIispAddrPnniInfoStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVptIispAddrPnniInfoStorageType.setStatus("mandatory")
_AtmIfVptIispAddrPnniInfoIndex_Type = NonReplicated
_AtmIfVptIispAddrPnniInfoIndex_Object = MibTableColumn
atmIfVptIispAddrPnniInfoIndex = _AtmIfVptIispAddrPnniInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 6, 4, 3, 1, 1, 10),
    _AtmIfVptIispAddrPnniInfoIndex_Type()
)
atmIfVptIispAddrPnniInfoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmIfVptIispAddrPnniInfoIndex.setStatus("mandatory")
_AtmIfVptIispAddrPnniInfoProvTable_Object = MibTable
atmIfVptIispAddrPnniInfoProvTable = _AtmIfVptIispAddrPnniInfoProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 6, 4, 3, 10)
)
if mibBuilder.loadTexts:
    atmIfVptIispAddrPnniInfoProvTable.setStatus("mandatory")
_AtmIfVptIispAddrPnniInfoProvEntry_Object = MibTableRow
atmIfVptIispAddrPnniInfoProvEntry = _AtmIfVptIispAddrPnniInfoProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 6, 4, 3, 10, 1)
)
atmIfVptIispAddrPnniInfoProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfVptIndex"),
    (0, "Nortel-Magellan-Passport-AtmIispMIB", "atmIfVptIispIndex"),
    (0, "Nortel-Magellan-Passport-AtmIispMIB", "atmIfVptIispAddrAddressIndex"),
    (0, "Nortel-Magellan-Passport-AtmIispMIB", "atmIfVptIispAddrAddressTypeIndex"),
    (0, "Nortel-Magellan-Passport-AtmIispMIB", "atmIfVptIispAddrPnniInfoIndex"),
)
if mibBuilder.loadTexts:
    atmIfVptIispAddrPnniInfoProvEntry.setStatus("mandatory")


class _AtmIfVptIispAddrPnniInfoScope_Type(Integer32):
    """Custom type atmIfVptIispAddrPnniInfoScope based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 104),
    )


_AtmIfVptIispAddrPnniInfoScope_Type.__name__ = "Integer32"
_AtmIfVptIispAddrPnniInfoScope_Object = MibTableColumn
atmIfVptIispAddrPnniInfoScope = _AtmIfVptIispAddrPnniInfoScope_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 6, 4, 3, 10, 1, 1),
    _AtmIfVptIispAddrPnniInfoScope_Type()
)
atmIfVptIispAddrPnniInfoScope.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfVptIispAddrPnniInfoScope.setStatus("mandatory")


class _AtmIfVptIispAddrPnniInfoReachability_Type(Integer32):
    """Custom type atmIfVptIispAddrPnniInfoReachability based on Integer32"""
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


_AtmIfVptIispAddrPnniInfoReachability_Type.__name__ = "Integer32"
_AtmIfVptIispAddrPnniInfoReachability_Object = MibTableColumn
atmIfVptIispAddrPnniInfoReachability = _AtmIfVptIispAddrPnniInfoReachability_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 6, 4, 3, 10, 1, 2),
    _AtmIfVptIispAddrPnniInfoReachability_Type()
)
atmIfVptIispAddrPnniInfoReachability.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfVptIispAddrPnniInfoReachability.setStatus("mandatory")
_AtmIfVptIispAddrOperTable_Object = MibTable
atmIfVptIispAddrOperTable = _AtmIfVptIispAddrOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 6, 4, 10)
)
if mibBuilder.loadTexts:
    atmIfVptIispAddrOperTable.setStatus("mandatory")
_AtmIfVptIispAddrOperEntry_Object = MibTableRow
atmIfVptIispAddrOperEntry = _AtmIfVptIispAddrOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 6, 4, 10, 1)
)
atmIfVptIispAddrOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfVptIndex"),
    (0, "Nortel-Magellan-Passport-AtmIispMIB", "atmIfVptIispIndex"),
    (0, "Nortel-Magellan-Passport-AtmIispMIB", "atmIfVptIispAddrAddressIndex"),
    (0, "Nortel-Magellan-Passport-AtmIispMIB", "atmIfVptIispAddrAddressTypeIndex"),
)
if mibBuilder.loadTexts:
    atmIfVptIispAddrOperEntry.setStatus("mandatory")


class _AtmIfVptIispAddrScope_Type(Integer32):
    """Custom type atmIfVptIispAddrScope based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 104),
    )


_AtmIfVptIispAddrScope_Type.__name__ = "Integer32"
_AtmIfVptIispAddrScope_Object = MibTableColumn
atmIfVptIispAddrScope = _AtmIfVptIispAddrScope_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 6, 4, 10, 1, 1),
    _AtmIfVptIispAddrScope_Type()
)
atmIfVptIispAddrScope.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVptIispAddrScope.setStatus("mandatory")


class _AtmIfVptIispAddrReachability_Type(Integer32):
    """Custom type atmIfVptIispAddrReachability based on Integer32"""
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


_AtmIfVptIispAddrReachability_Type.__name__ = "Integer32"
_AtmIfVptIispAddrReachability_Object = MibTableColumn
atmIfVptIispAddrReachability = _AtmIfVptIispAddrReachability_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 6, 4, 10, 1, 2),
    _AtmIfVptIispAddrReachability_Type()
)
atmIfVptIispAddrReachability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVptIispAddrReachability.setStatus("mandatory")
_AtmIfVptIispProvTable_Object = MibTable
atmIfVptIispProvTable = _AtmIfVptIispProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 6, 10)
)
if mibBuilder.loadTexts:
    atmIfVptIispProvTable.setStatus("mandatory")
_AtmIfVptIispProvEntry_Object = MibTableRow
atmIfVptIispProvEntry = _AtmIfVptIispProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 6, 10, 1)
)
atmIfVptIispProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfVptIndex"),
    (0, "Nortel-Magellan-Passport-AtmIispMIB", "atmIfVptIispIndex"),
)
if mibBuilder.loadTexts:
    atmIfVptIispProvEntry.setStatus("mandatory")


class _AtmIfVptIispVersion_Type(Integer32):
    """Custom type atmIfVptIispVersion based on Integer32"""
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


_AtmIfVptIispVersion_Type.__name__ = "Integer32"
_AtmIfVptIispVersion_Object = MibTableColumn
atmIfVptIispVersion = _AtmIfVptIispVersion_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 6, 10, 1, 1),
    _AtmIfVptIispVersion_Type()
)
atmIfVptIispVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfVptIispVersion.setStatus("mandatory")


class _AtmIfVptIispSide_Type(Integer32):
    """Custom type atmIfVptIispSide based on Integer32"""
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


_AtmIfVptIispSide_Type.__name__ = "Integer32"
_AtmIfVptIispSide_Object = MibTableColumn
atmIfVptIispSide = _AtmIfVptIispSide_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 6, 10, 1, 2),
    _AtmIfVptIispSide_Type()
)
atmIfVptIispSide.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfVptIispSide.setStatus("mandatory")


class _AtmIfVptIispSoftPvcRetryPeriod_Type(Unsigned32):
    """Custom type atmIfVptIispSoftPvcRetryPeriod based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 999999),
    )


_AtmIfVptIispSoftPvcRetryPeriod_Type.__name__ = "Unsigned32"
_AtmIfVptIispSoftPvcRetryPeriod_Object = MibTableColumn
atmIfVptIispSoftPvcRetryPeriod = _AtmIfVptIispSoftPvcRetryPeriod_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 6, 10, 1, 3),
    _AtmIfVptIispSoftPvcRetryPeriod_Type()
)
atmIfVptIispSoftPvcRetryPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfVptIispSoftPvcRetryPeriod.setStatus("obsolete")


class _AtmIfVptIispSoftPvpAndPvcRetryPeriod_Type(Unsigned32):
    """Custom type atmIfVptIispSoftPvpAndPvcRetryPeriod based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 999999),
    )


_AtmIfVptIispSoftPvpAndPvcRetryPeriod_Type.__name__ = "Unsigned32"
_AtmIfVptIispSoftPvpAndPvcRetryPeriod_Object = MibTableColumn
atmIfVptIispSoftPvpAndPvcRetryPeriod = _AtmIfVptIispSoftPvpAndPvcRetryPeriod_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 6, 10, 1, 4),
    _AtmIfVptIispSoftPvpAndPvcRetryPeriod_Type()
)
atmIfVptIispSoftPvpAndPvcRetryPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfVptIispSoftPvpAndPvcRetryPeriod.setStatus("mandatory")


class _AtmIfVptIispSoftPvpAndPvcHoldOffTime_Type(Unsigned32):
    """Custom type atmIfVptIispSoftPvpAndPvcHoldOffTime based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(50, 20000),
    )


_AtmIfVptIispSoftPvpAndPvcHoldOffTime_Type.__name__ = "Unsigned32"
_AtmIfVptIispSoftPvpAndPvcHoldOffTime_Object = MibTableColumn
atmIfVptIispSoftPvpAndPvcHoldOffTime = _AtmIfVptIispSoftPvpAndPvcHoldOffTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 6, 10, 1, 5),
    _AtmIfVptIispSoftPvpAndPvcHoldOffTime_Type()
)
atmIfVptIispSoftPvpAndPvcHoldOffTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfVptIispSoftPvpAndPvcHoldOffTime.setStatus("mandatory")
_AtmIfVptIispAcctOptTable_Object = MibTable
atmIfVptIispAcctOptTable = _AtmIfVptIispAcctOptTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 6, 11)
)
if mibBuilder.loadTexts:
    atmIfVptIispAcctOptTable.setStatus("mandatory")
_AtmIfVptIispAcctOptEntry_Object = MibTableRow
atmIfVptIispAcctOptEntry = _AtmIfVptIispAcctOptEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 6, 11, 1)
)
atmIfVptIispAcctOptEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfVptIndex"),
    (0, "Nortel-Magellan-Passport-AtmIispMIB", "atmIfVptIispIndex"),
)
if mibBuilder.loadTexts:
    atmIfVptIispAcctOptEntry.setStatus("mandatory")


class _AtmIfVptIispAccountCollection_Type(OctetString):
    """Custom type atmIfVptIispAccountCollection based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_AtmIfVptIispAccountCollection_Type.__name__ = "OctetString"
_AtmIfVptIispAccountCollection_Object = MibTableColumn
atmIfVptIispAccountCollection = _AtmIfVptIispAccountCollection_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 6, 11, 1, 1),
    _AtmIfVptIispAccountCollection_Type()
)
atmIfVptIispAccountCollection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfVptIispAccountCollection.setStatus("mandatory")


class _AtmIfVptIispAccountConnectionType_Type(Integer32):
    """Custom type atmIfVptIispAccountConnectionType based on Integer32"""
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


_AtmIfVptIispAccountConnectionType_Type.__name__ = "Integer32"
_AtmIfVptIispAccountConnectionType_Object = MibTableColumn
atmIfVptIispAccountConnectionType = _AtmIfVptIispAccountConnectionType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 6, 11, 1, 2),
    _AtmIfVptIispAccountConnectionType_Type()
)
atmIfVptIispAccountConnectionType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfVptIispAccountConnectionType.setStatus("mandatory")


class _AtmIfVptIispAccountClass_Type(Unsigned32):
    """Custom type atmIfVptIispAccountClass based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AtmIfVptIispAccountClass_Type.__name__ = "Unsigned32"
_AtmIfVptIispAccountClass_Object = MibTableColumn
atmIfVptIispAccountClass = _AtmIfVptIispAccountClass_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 6, 11, 1, 3),
    _AtmIfVptIispAccountClass_Type()
)
atmIfVptIispAccountClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfVptIispAccountClass.setStatus("mandatory")


class _AtmIfVptIispServiceExchange_Type(Unsigned32):
    """Custom type atmIfVptIispServiceExchange based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AtmIfVptIispServiceExchange_Type.__name__ = "Unsigned32"
_AtmIfVptIispServiceExchange_Object = MibTableColumn
atmIfVptIispServiceExchange = _AtmIfVptIispServiceExchange_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 6, 11, 1, 4),
    _AtmIfVptIispServiceExchange_Type()
)
atmIfVptIispServiceExchange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfVptIispServiceExchange.setStatus("mandatory")
_AtmIfVptIispVProvTable_Object = MibTable
atmIfVptIispVProvTable = _AtmIfVptIispVProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 6, 12)
)
if mibBuilder.loadTexts:
    atmIfVptIispVProvTable.setStatus("mandatory")
_AtmIfVptIispVProvEntry_Object = MibTableRow
atmIfVptIispVProvEntry = _AtmIfVptIispVProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 6, 12, 1)
)
atmIfVptIispVProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfVptIndex"),
    (0, "Nortel-Magellan-Passport-AtmIispMIB", "atmIfVptIispIndex"),
)
if mibBuilder.loadTexts:
    atmIfVptIispVProvEntry.setStatus("mandatory")


class _AtmIfVptIispVpci_Type(Unsigned32):
    """Custom type atmIfVptIispVpci based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AtmIfVptIispVpci_Type.__name__ = "Unsigned32"
_AtmIfVptIispVpci_Object = MibTableColumn
atmIfVptIispVpci = _AtmIfVptIispVpci_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 6, 12, 1, 1),
    _AtmIfVptIispVpci_Type()
)
atmIfVptIispVpci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfVptIispVpci.setStatus("mandatory")
_AtmIispMIB_ObjectIdentity = ObjectIdentity
atmIispMIB = _AtmIispMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 70)
)
_AtmIispGroup_ObjectIdentity = ObjectIdentity
atmIispGroup = _AtmIispGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 70, 1)
)
_AtmIispGroupBE_ObjectIdentity = ObjectIdentity
atmIispGroupBE = _AtmIispGroupBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 70, 1, 5)
)
_AtmIispGroupBE00_ObjectIdentity = ObjectIdentity
atmIispGroupBE00 = _AtmIispGroupBE00_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 70, 1, 5, 1)
)
_AtmIispGroupBE00A_ObjectIdentity = ObjectIdentity
atmIispGroupBE00A = _AtmIispGroupBE00A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 70, 1, 5, 1, 2)
)
_AtmIispCapabilities_ObjectIdentity = ObjectIdentity
atmIispCapabilities = _AtmIispCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 70, 3)
)
_AtmIispCapabilitiesBE_ObjectIdentity = ObjectIdentity
atmIispCapabilitiesBE = _AtmIispCapabilitiesBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 70, 3, 5)
)
_AtmIispCapabilitiesBE00_ObjectIdentity = ObjectIdentity
atmIispCapabilitiesBE00 = _AtmIispCapabilitiesBE00_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 70, 3, 5, 1)
)
_AtmIispCapabilitiesBE00A_ObjectIdentity = ObjectIdentity
atmIispCapabilitiesBE00A = _AtmIispCapabilitiesBE00A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 70, 3, 5, 1, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-Magellan-Passport-AtmIispMIB",
    **{"atmIfIisp": atmIfIisp,
       "atmIfIispRowStatusTable": atmIfIispRowStatusTable,
       "atmIfIispRowStatusEntry": atmIfIispRowStatusEntry,
       "atmIfIispRowStatus": atmIfIispRowStatus,
       "atmIfIispComponentName": atmIfIispComponentName,
       "atmIfIispStorageType": atmIfIispStorageType,
       "atmIfIispIndex": atmIfIispIndex,
       "atmIfIispSig": atmIfIispSig,
       "atmIfIispSigRowStatusTable": atmIfIispSigRowStatusTable,
       "atmIfIispSigRowStatusEntry": atmIfIispSigRowStatusEntry,
       "atmIfIispSigRowStatus": atmIfIispSigRowStatus,
       "atmIfIispSigComponentName": atmIfIispSigComponentName,
       "atmIfIispSigStorageType": atmIfIispSigStorageType,
       "atmIfIispSigIndex": atmIfIispSigIndex,
       "atmIfIispSigVcd": atmIfIispSigVcd,
       "atmIfIispSigVcdRowStatusTable": atmIfIispSigVcdRowStatusTable,
       "atmIfIispSigVcdRowStatusEntry": atmIfIispSigVcdRowStatusEntry,
       "atmIfIispSigVcdRowStatus": atmIfIispSigVcdRowStatus,
       "atmIfIispSigVcdComponentName": atmIfIispSigVcdComponentName,
       "atmIfIispSigVcdStorageType": atmIfIispSigVcdStorageType,
       "atmIfIispSigVcdIndex": atmIfIispSigVcdIndex,
       "atmIfIispSigVcdProvTable": atmIfIispSigVcdProvTable,
       "atmIfIispSigVcdProvEntry": atmIfIispSigVcdProvEntry,
       "atmIfIispSigVcdTrafficDescType": atmIfIispSigVcdTrafficDescType,
       "atmIfIispSigVcdAtmServiceCategory": atmIfIispSigVcdAtmServiceCategory,
       "atmIfIispSigVcdQosClass": atmIfIispSigVcdQosClass,
       "atmIfIispSigVcdTrafficShaping": atmIfIispSigVcdTrafficShaping,
       "atmIfIispSigVcdUnshapedTransmitQueueing": atmIfIispSigVcdUnshapedTransmitQueueing,
       "atmIfIispSigVcdUsageParameterControl": atmIfIispSigVcdUsageParameterControl,
       "atmIfIispSigVcdTdpTable": atmIfIispSigVcdTdpTable,
       "atmIfIispSigVcdTdpEntry": atmIfIispSigVcdTdpEntry,
       "atmIfIispSigVcdTdpIndex": atmIfIispSigVcdTdpIndex,
       "atmIfIispSigVcdTdpValue": atmIfIispSigVcdTdpValue,
       "atmIfIispSigProvTable": atmIfIispSigProvTable,
       "atmIfIispSigProvEntry": atmIfIispSigProvEntry,
       "atmIfIispSigVci": atmIfIispSigVci,
       "atmIfIispSigAddressConversion": atmIfIispSigAddressConversion,
       "atmIfIispSigStateTable": atmIfIispSigStateTable,
       "atmIfIispSigStateEntry": atmIfIispSigStateEntry,
       "atmIfIispSigAdminState": atmIfIispSigAdminState,
       "atmIfIispSigOperationalState": atmIfIispSigOperationalState,
       "atmIfIispSigUsageState": atmIfIispSigUsageState,
       "atmIfIispSigOperTable": atmIfIispSigOperTable,
       "atmIfIispSigOperEntry": atmIfIispSigOperEntry,
       "atmIfIispSigLastTxCauseCode": atmIfIispSigLastTxCauseCode,
       "atmIfIispSigLastTxDiagCode": atmIfIispSigLastTxDiagCode,
       "atmIfIispSigLastRxCauseCode": atmIfIispSigLastRxCauseCode,
       "atmIfIispSigLastRxDiagCode": atmIfIispSigLastRxDiagCode,
       "atmIfIispSigStatsTable": atmIfIispSigStatsTable,
       "atmIfIispSigStatsEntry": atmIfIispSigStatsEntry,
       "atmIfIispSigCurrentConnections": atmIfIispSigCurrentConnections,
       "atmIfIispSigPeakConnections": atmIfIispSigPeakConnections,
       "atmIfIispSigSuccessfulConnections": atmIfIispSigSuccessfulConnections,
       "atmIfIispSigFailedConnections": atmIfIispSigFailedConnections,
       "atmIfIispSigTxPdus": atmIfIispSigTxPdus,
       "atmIfIispSigRxPdus": atmIfIispSigRxPdus,
       "atmIfIispSigCurrentPmpConnections": atmIfIispSigCurrentPmpConnections,
       "atmIfIispSigPeakPmpConnections": atmIfIispSigPeakPmpConnections,
       "atmIfIispSigSuccessfulPmpConnections": atmIfIispSigSuccessfulPmpConnections,
       "atmIfIispSigFailedPmpConnections": atmIfIispSigFailedPmpConnections,
       "atmIfIispSigNewCurrentConnections": atmIfIispSigNewCurrentConnections,
       "atmIfIispAddr": atmIfIispAddr,
       "atmIfIispAddrRowStatusTable": atmIfIispAddrRowStatusTable,
       "atmIfIispAddrRowStatusEntry": atmIfIispAddrRowStatusEntry,
       "atmIfIispAddrRowStatus": atmIfIispAddrRowStatus,
       "atmIfIispAddrComponentName": atmIfIispAddrComponentName,
       "atmIfIispAddrStorageType": atmIfIispAddrStorageType,
       "atmIfIispAddrAddressIndex": atmIfIispAddrAddressIndex,
       "atmIfIispAddrAddressTypeIndex": atmIfIispAddrAddressTypeIndex,
       "atmIfIispAddrTermSP": atmIfIispAddrTermSP,
       "atmIfIispAddrTermSPRowStatusTable": atmIfIispAddrTermSPRowStatusTable,
       "atmIfIispAddrTermSPRowStatusEntry": atmIfIispAddrTermSPRowStatusEntry,
       "atmIfIispAddrTermSPRowStatus": atmIfIispAddrTermSPRowStatus,
       "atmIfIispAddrTermSPComponentName": atmIfIispAddrTermSPComponentName,
       "atmIfIispAddrTermSPStorageType": atmIfIispAddrTermSPStorageType,
       "atmIfIispAddrTermSPIndex": atmIfIispAddrTermSPIndex,
       "atmIfIispAddrPnniInfo": atmIfIispAddrPnniInfo,
       "atmIfIispAddrPnniInfoRowStatusTable": atmIfIispAddrPnniInfoRowStatusTable,
       "atmIfIispAddrPnniInfoRowStatusEntry": atmIfIispAddrPnniInfoRowStatusEntry,
       "atmIfIispAddrPnniInfoRowStatus": atmIfIispAddrPnniInfoRowStatus,
       "atmIfIispAddrPnniInfoComponentName": atmIfIispAddrPnniInfoComponentName,
       "atmIfIispAddrPnniInfoStorageType": atmIfIispAddrPnniInfoStorageType,
       "atmIfIispAddrPnniInfoIndex": atmIfIispAddrPnniInfoIndex,
       "atmIfIispAddrPnniInfoProvTable": atmIfIispAddrPnniInfoProvTable,
       "atmIfIispAddrPnniInfoProvEntry": atmIfIispAddrPnniInfoProvEntry,
       "atmIfIispAddrPnniInfoScope": atmIfIispAddrPnniInfoScope,
       "atmIfIispAddrPnniInfoReachability": atmIfIispAddrPnniInfoReachability,
       "atmIfIispAddrOperTable": atmIfIispAddrOperTable,
       "atmIfIispAddrOperEntry": atmIfIispAddrOperEntry,
       "atmIfIispAddrScope": atmIfIispAddrScope,
       "atmIfIispAddrReachability": atmIfIispAddrReachability,
       "atmIfIispProvTable": atmIfIispProvTable,
       "atmIfIispProvEntry": atmIfIispProvEntry,
       "atmIfIispVersion": atmIfIispVersion,
       "atmIfIispSide": atmIfIispSide,
       "atmIfIispSoftPvcRetryPeriod": atmIfIispSoftPvcRetryPeriod,
       "atmIfIispSoftPvpAndPvcRetryPeriod": atmIfIispSoftPvpAndPvcRetryPeriod,
       "atmIfIispSoftPvpAndPvcHoldOffTime": atmIfIispSoftPvpAndPvcHoldOffTime,
       "atmIfIispAcctOptTable": atmIfIispAcctOptTable,
       "atmIfIispAcctOptEntry": atmIfIispAcctOptEntry,
       "atmIfIispAccountCollection": atmIfIispAccountCollection,
       "atmIfIispAccountConnectionType": atmIfIispAccountConnectionType,
       "atmIfIispAccountClass": atmIfIispAccountClass,
       "atmIfIispServiceExchange": atmIfIispServiceExchange,
       "atmIfVptIisp": atmIfVptIisp,
       "atmIfVptIispRowStatusTable": atmIfVptIispRowStatusTable,
       "atmIfVptIispRowStatusEntry": atmIfVptIispRowStatusEntry,
       "atmIfVptIispRowStatus": atmIfVptIispRowStatus,
       "atmIfVptIispComponentName": atmIfVptIispComponentName,
       "atmIfVptIispStorageType": atmIfVptIispStorageType,
       "atmIfVptIispIndex": atmIfVptIispIndex,
       "atmIfVptIispSig": atmIfVptIispSig,
       "atmIfVptIispSigRowStatusTable": atmIfVptIispSigRowStatusTable,
       "atmIfVptIispSigRowStatusEntry": atmIfVptIispSigRowStatusEntry,
       "atmIfVptIispSigRowStatus": atmIfVptIispSigRowStatus,
       "atmIfVptIispSigComponentName": atmIfVptIispSigComponentName,
       "atmIfVptIispSigStorageType": atmIfVptIispSigStorageType,
       "atmIfVptIispSigIndex": atmIfVptIispSigIndex,
       "atmIfVptIispSigVcd": atmIfVptIispSigVcd,
       "atmIfVptIispSigVcdRowStatusTable": atmIfVptIispSigVcdRowStatusTable,
       "atmIfVptIispSigVcdRowStatusEntry": atmIfVptIispSigVcdRowStatusEntry,
       "atmIfVptIispSigVcdRowStatus": atmIfVptIispSigVcdRowStatus,
       "atmIfVptIispSigVcdComponentName": atmIfVptIispSigVcdComponentName,
       "atmIfVptIispSigVcdStorageType": atmIfVptIispSigVcdStorageType,
       "atmIfVptIispSigVcdIndex": atmIfVptIispSigVcdIndex,
       "atmIfVptIispSigVcdProvTable": atmIfVptIispSigVcdProvTable,
       "atmIfVptIispSigVcdProvEntry": atmIfVptIispSigVcdProvEntry,
       "atmIfVptIispSigVcdTrafficDescType": atmIfVptIispSigVcdTrafficDescType,
       "atmIfVptIispSigVcdAtmServiceCategory": atmIfVptIispSigVcdAtmServiceCategory,
       "atmIfVptIispSigVcdQosClass": atmIfVptIispSigVcdQosClass,
       "atmIfVptIispSigVcdTrafficShaping": atmIfVptIispSigVcdTrafficShaping,
       "atmIfVptIispSigVcdUnshapedTransmitQueueing": atmIfVptIispSigVcdUnshapedTransmitQueueing,
       "atmIfVptIispSigVcdUsageParameterControl": atmIfVptIispSigVcdUsageParameterControl,
       "atmIfVptIispSigVcdTdpTable": atmIfVptIispSigVcdTdpTable,
       "atmIfVptIispSigVcdTdpEntry": atmIfVptIispSigVcdTdpEntry,
       "atmIfVptIispSigVcdTdpIndex": atmIfVptIispSigVcdTdpIndex,
       "atmIfVptIispSigVcdTdpValue": atmIfVptIispSigVcdTdpValue,
       "atmIfVptIispSigProvTable": atmIfVptIispSigProvTable,
       "atmIfVptIispSigProvEntry": atmIfVptIispSigProvEntry,
       "atmIfVptIispSigVci": atmIfVptIispSigVci,
       "atmIfVptIispSigAddressConversion": atmIfVptIispSigAddressConversion,
       "atmIfVptIispSigStateTable": atmIfVptIispSigStateTable,
       "atmIfVptIispSigStateEntry": atmIfVptIispSigStateEntry,
       "atmIfVptIispSigAdminState": atmIfVptIispSigAdminState,
       "atmIfVptIispSigOperationalState": atmIfVptIispSigOperationalState,
       "atmIfVptIispSigUsageState": atmIfVptIispSigUsageState,
       "atmIfVptIispSigOperTable": atmIfVptIispSigOperTable,
       "atmIfVptIispSigOperEntry": atmIfVptIispSigOperEntry,
       "atmIfVptIispSigLastTxCauseCode": atmIfVptIispSigLastTxCauseCode,
       "atmIfVptIispSigLastTxDiagCode": atmIfVptIispSigLastTxDiagCode,
       "atmIfVptIispSigLastRxCauseCode": atmIfVptIispSigLastRxCauseCode,
       "atmIfVptIispSigLastRxDiagCode": atmIfVptIispSigLastRxDiagCode,
       "atmIfVptIispSigStatsTable": atmIfVptIispSigStatsTable,
       "atmIfVptIispSigStatsEntry": atmIfVptIispSigStatsEntry,
       "atmIfVptIispSigCurrentConnections": atmIfVptIispSigCurrentConnections,
       "atmIfVptIispSigPeakConnections": atmIfVptIispSigPeakConnections,
       "atmIfVptIispSigSuccessfulConnections": atmIfVptIispSigSuccessfulConnections,
       "atmIfVptIispSigFailedConnections": atmIfVptIispSigFailedConnections,
       "atmIfVptIispSigTxPdus": atmIfVptIispSigTxPdus,
       "atmIfVptIispSigRxPdus": atmIfVptIispSigRxPdus,
       "atmIfVptIispSigCurrentPmpConnections": atmIfVptIispSigCurrentPmpConnections,
       "atmIfVptIispSigPeakPmpConnections": atmIfVptIispSigPeakPmpConnections,
       "atmIfVptIispSigSuccessfulPmpConnections": atmIfVptIispSigSuccessfulPmpConnections,
       "atmIfVptIispSigFailedPmpConnections": atmIfVptIispSigFailedPmpConnections,
       "atmIfVptIispSigNewCurrentConnections": atmIfVptIispSigNewCurrentConnections,
       "atmIfVptIispAddr": atmIfVptIispAddr,
       "atmIfVptIispAddrRowStatusTable": atmIfVptIispAddrRowStatusTable,
       "atmIfVptIispAddrRowStatusEntry": atmIfVptIispAddrRowStatusEntry,
       "atmIfVptIispAddrRowStatus": atmIfVptIispAddrRowStatus,
       "atmIfVptIispAddrComponentName": atmIfVptIispAddrComponentName,
       "atmIfVptIispAddrStorageType": atmIfVptIispAddrStorageType,
       "atmIfVptIispAddrAddressIndex": atmIfVptIispAddrAddressIndex,
       "atmIfVptIispAddrAddressTypeIndex": atmIfVptIispAddrAddressTypeIndex,
       "atmIfVptIispAddrTermSP": atmIfVptIispAddrTermSP,
       "atmIfVptIispAddrTermSPRowStatusTable": atmIfVptIispAddrTermSPRowStatusTable,
       "atmIfVptIispAddrTermSPRowStatusEntry": atmIfVptIispAddrTermSPRowStatusEntry,
       "atmIfVptIispAddrTermSPRowStatus": atmIfVptIispAddrTermSPRowStatus,
       "atmIfVptIispAddrTermSPComponentName": atmIfVptIispAddrTermSPComponentName,
       "atmIfVptIispAddrTermSPStorageType": atmIfVptIispAddrTermSPStorageType,
       "atmIfVptIispAddrTermSPIndex": atmIfVptIispAddrTermSPIndex,
       "atmIfVptIispAddrPnniInfo": atmIfVptIispAddrPnniInfo,
       "atmIfVptIispAddrPnniInfoRowStatusTable": atmIfVptIispAddrPnniInfoRowStatusTable,
       "atmIfVptIispAddrPnniInfoRowStatusEntry": atmIfVptIispAddrPnniInfoRowStatusEntry,
       "atmIfVptIispAddrPnniInfoRowStatus": atmIfVptIispAddrPnniInfoRowStatus,
       "atmIfVptIispAddrPnniInfoComponentName": atmIfVptIispAddrPnniInfoComponentName,
       "atmIfVptIispAddrPnniInfoStorageType": atmIfVptIispAddrPnniInfoStorageType,
       "atmIfVptIispAddrPnniInfoIndex": atmIfVptIispAddrPnniInfoIndex,
       "atmIfVptIispAddrPnniInfoProvTable": atmIfVptIispAddrPnniInfoProvTable,
       "atmIfVptIispAddrPnniInfoProvEntry": atmIfVptIispAddrPnniInfoProvEntry,
       "atmIfVptIispAddrPnniInfoScope": atmIfVptIispAddrPnniInfoScope,
       "atmIfVptIispAddrPnniInfoReachability": atmIfVptIispAddrPnniInfoReachability,
       "atmIfVptIispAddrOperTable": atmIfVptIispAddrOperTable,
       "atmIfVptIispAddrOperEntry": atmIfVptIispAddrOperEntry,
       "atmIfVptIispAddrScope": atmIfVptIispAddrScope,
       "atmIfVptIispAddrReachability": atmIfVptIispAddrReachability,
       "atmIfVptIispProvTable": atmIfVptIispProvTable,
       "atmIfVptIispProvEntry": atmIfVptIispProvEntry,
       "atmIfVptIispVersion": atmIfVptIispVersion,
       "atmIfVptIispSide": atmIfVptIispSide,
       "atmIfVptIispSoftPvcRetryPeriod": atmIfVptIispSoftPvcRetryPeriod,
       "atmIfVptIispSoftPvpAndPvcRetryPeriod": atmIfVptIispSoftPvpAndPvcRetryPeriod,
       "atmIfVptIispSoftPvpAndPvcHoldOffTime": atmIfVptIispSoftPvpAndPvcHoldOffTime,
       "atmIfVptIispAcctOptTable": atmIfVptIispAcctOptTable,
       "atmIfVptIispAcctOptEntry": atmIfVptIispAcctOptEntry,
       "atmIfVptIispAccountCollection": atmIfVptIispAccountCollection,
       "atmIfVptIispAccountConnectionType": atmIfVptIispAccountConnectionType,
       "atmIfVptIispAccountClass": atmIfVptIispAccountClass,
       "atmIfVptIispServiceExchange": atmIfVptIispServiceExchange,
       "atmIfVptIispVProvTable": atmIfVptIispVProvTable,
       "atmIfVptIispVProvEntry": atmIfVptIispVProvEntry,
       "atmIfVptIispVpci": atmIfVptIispVpci,
       "atmIispMIB": atmIispMIB,
       "atmIispGroup": atmIispGroup,
       "atmIispGroupBE": atmIispGroupBE,
       "atmIispGroupBE00": atmIispGroupBE00,
       "atmIispGroupBE00A": atmIispGroupBE00A,
       "atmIispCapabilities": atmIispCapabilities,
       "atmIispCapabilitiesBE": atmIispCapabilitiesBE,
       "atmIispCapabilitiesBE00": atmIispCapabilitiesBE00,
       "atmIispCapabilitiesBE00A": atmIispCapabilitiesBE00A}
)
