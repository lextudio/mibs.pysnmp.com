# SNMP MIB module (Nortel-Magellan-Passport-AtmPnniMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-Magellan-Passport-AtmPnniMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:30:21 2024
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
 FixedPoint1,
 Hex,
 HexString,
 NonReplicated) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-TextualConventionsMIB",
    "AsciiStringIndex",
    "FixedPoint1",
    "Hex",
    "HexString",
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

_AtmIfVptPnni_ObjectIdentity = ObjectIdentity
atmIfVptPnni = _AtmIfVptPnni_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7)
)
_AtmIfVptPnniRowStatusTable_Object = MibTable
atmIfVptPnniRowStatusTable = _AtmIfVptPnniRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 1)
)
if mibBuilder.loadTexts:
    atmIfVptPnniRowStatusTable.setStatus("mandatory")
_AtmIfVptPnniRowStatusEntry_Object = MibTableRow
atmIfVptPnniRowStatusEntry = _AtmIfVptPnniRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 1, 1)
)
atmIfVptPnniRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfVptIndex"),
    (0, "Nortel-Magellan-Passport-AtmPnniMIB", "atmIfVptPnniIndex"),
)
if mibBuilder.loadTexts:
    atmIfVptPnniRowStatusEntry.setStatus("mandatory")
_AtmIfVptPnniRowStatus_Type = RowStatus
_AtmIfVptPnniRowStatus_Object = MibTableColumn
atmIfVptPnniRowStatus = _AtmIfVptPnniRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 1, 1, 1),
    _AtmIfVptPnniRowStatus_Type()
)
atmIfVptPnniRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfVptPnniRowStatus.setStatus("mandatory")
_AtmIfVptPnniComponentName_Type = DisplayString
_AtmIfVptPnniComponentName_Object = MibTableColumn
atmIfVptPnniComponentName = _AtmIfVptPnniComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 1, 1, 2),
    _AtmIfVptPnniComponentName_Type()
)
atmIfVptPnniComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVptPnniComponentName.setStatus("mandatory")
_AtmIfVptPnniStorageType_Type = StorageType
_AtmIfVptPnniStorageType_Object = MibTableColumn
atmIfVptPnniStorageType = _AtmIfVptPnniStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 1, 1, 4),
    _AtmIfVptPnniStorageType_Type()
)
atmIfVptPnniStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVptPnniStorageType.setStatus("mandatory")
_AtmIfVptPnniIndex_Type = NonReplicated
_AtmIfVptPnniIndex_Object = MibTableColumn
atmIfVptPnniIndex = _AtmIfVptPnniIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 1, 1, 10),
    _AtmIfVptPnniIndex_Type()
)
atmIfVptPnniIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmIfVptPnniIndex.setStatus("mandatory")
_AtmIfVptPnniSig_ObjectIdentity = ObjectIdentity
atmIfVptPnniSig = _AtmIfVptPnniSig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 2)
)
_AtmIfVptPnniSigRowStatusTable_Object = MibTable
atmIfVptPnniSigRowStatusTable = _AtmIfVptPnniSigRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 2, 1)
)
if mibBuilder.loadTexts:
    atmIfVptPnniSigRowStatusTable.setStatus("mandatory")
_AtmIfVptPnniSigRowStatusEntry_Object = MibTableRow
atmIfVptPnniSigRowStatusEntry = _AtmIfVptPnniSigRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 2, 1, 1)
)
atmIfVptPnniSigRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfVptIndex"),
    (0, "Nortel-Magellan-Passport-AtmPnniMIB", "atmIfVptPnniIndex"),
    (0, "Nortel-Magellan-Passport-AtmPnniMIB", "atmIfVptPnniSigIndex"),
)
if mibBuilder.loadTexts:
    atmIfVptPnniSigRowStatusEntry.setStatus("mandatory")
_AtmIfVptPnniSigRowStatus_Type = RowStatus
_AtmIfVptPnniSigRowStatus_Object = MibTableColumn
atmIfVptPnniSigRowStatus = _AtmIfVptPnniSigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 2, 1, 1, 1),
    _AtmIfVptPnniSigRowStatus_Type()
)
atmIfVptPnniSigRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVptPnniSigRowStatus.setStatus("mandatory")
_AtmIfVptPnniSigComponentName_Type = DisplayString
_AtmIfVptPnniSigComponentName_Object = MibTableColumn
atmIfVptPnniSigComponentName = _AtmIfVptPnniSigComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 2, 1, 1, 2),
    _AtmIfVptPnniSigComponentName_Type()
)
atmIfVptPnniSigComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVptPnniSigComponentName.setStatus("mandatory")
_AtmIfVptPnniSigStorageType_Type = StorageType
_AtmIfVptPnniSigStorageType_Object = MibTableColumn
atmIfVptPnniSigStorageType = _AtmIfVptPnniSigStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 2, 1, 1, 4),
    _AtmIfVptPnniSigStorageType_Type()
)
atmIfVptPnniSigStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVptPnniSigStorageType.setStatus("mandatory")
_AtmIfVptPnniSigIndex_Type = NonReplicated
_AtmIfVptPnniSigIndex_Object = MibTableColumn
atmIfVptPnniSigIndex = _AtmIfVptPnniSigIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 2, 1, 1, 10),
    _AtmIfVptPnniSigIndex_Type()
)
atmIfVptPnniSigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmIfVptPnniSigIndex.setStatus("mandatory")
_AtmIfVptPnniSigVcd_ObjectIdentity = ObjectIdentity
atmIfVptPnniSigVcd = _AtmIfVptPnniSigVcd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 2, 2)
)
_AtmIfVptPnniSigVcdRowStatusTable_Object = MibTable
atmIfVptPnniSigVcdRowStatusTable = _AtmIfVptPnniSigVcdRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 2, 2, 1)
)
if mibBuilder.loadTexts:
    atmIfVptPnniSigVcdRowStatusTable.setStatus("mandatory")
_AtmIfVptPnniSigVcdRowStatusEntry_Object = MibTableRow
atmIfVptPnniSigVcdRowStatusEntry = _AtmIfVptPnniSigVcdRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 2, 2, 1, 1)
)
atmIfVptPnniSigVcdRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfVptIndex"),
    (0, "Nortel-Magellan-Passport-AtmPnniMIB", "atmIfVptPnniIndex"),
    (0, "Nortel-Magellan-Passport-AtmPnniMIB", "atmIfVptPnniSigIndex"),
    (0, "Nortel-Magellan-Passport-AtmPnniMIB", "atmIfVptPnniSigVcdIndex"),
)
if mibBuilder.loadTexts:
    atmIfVptPnniSigVcdRowStatusEntry.setStatus("mandatory")
_AtmIfVptPnniSigVcdRowStatus_Type = RowStatus
_AtmIfVptPnniSigVcdRowStatus_Object = MibTableColumn
atmIfVptPnniSigVcdRowStatus = _AtmIfVptPnniSigVcdRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 2, 2, 1, 1, 1),
    _AtmIfVptPnniSigVcdRowStatus_Type()
)
atmIfVptPnniSigVcdRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfVptPnniSigVcdRowStatus.setStatus("mandatory")
_AtmIfVptPnniSigVcdComponentName_Type = DisplayString
_AtmIfVptPnniSigVcdComponentName_Object = MibTableColumn
atmIfVptPnniSigVcdComponentName = _AtmIfVptPnniSigVcdComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 2, 2, 1, 1, 2),
    _AtmIfVptPnniSigVcdComponentName_Type()
)
atmIfVptPnniSigVcdComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVptPnniSigVcdComponentName.setStatus("mandatory")
_AtmIfVptPnniSigVcdStorageType_Type = StorageType
_AtmIfVptPnniSigVcdStorageType_Object = MibTableColumn
atmIfVptPnniSigVcdStorageType = _AtmIfVptPnniSigVcdStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 2, 2, 1, 1, 4),
    _AtmIfVptPnniSigVcdStorageType_Type()
)
atmIfVptPnniSigVcdStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVptPnniSigVcdStorageType.setStatus("mandatory")
_AtmIfVptPnniSigVcdIndex_Type = NonReplicated
_AtmIfVptPnniSigVcdIndex_Object = MibTableColumn
atmIfVptPnniSigVcdIndex = _AtmIfVptPnniSigVcdIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 2, 2, 1, 1, 10),
    _AtmIfVptPnniSigVcdIndex_Type()
)
atmIfVptPnniSigVcdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmIfVptPnniSigVcdIndex.setStatus("mandatory")
_AtmIfVptPnniSigVcdProvTable_Object = MibTable
atmIfVptPnniSigVcdProvTable = _AtmIfVptPnniSigVcdProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 2, 2, 10)
)
if mibBuilder.loadTexts:
    atmIfVptPnniSigVcdProvTable.setStatus("mandatory")
_AtmIfVptPnniSigVcdProvEntry_Object = MibTableRow
atmIfVptPnniSigVcdProvEntry = _AtmIfVptPnniSigVcdProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 2, 2, 10, 1)
)
atmIfVptPnniSigVcdProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfVptIndex"),
    (0, "Nortel-Magellan-Passport-AtmPnniMIB", "atmIfVptPnniIndex"),
    (0, "Nortel-Magellan-Passport-AtmPnniMIB", "atmIfVptPnniSigIndex"),
    (0, "Nortel-Magellan-Passport-AtmPnniMIB", "atmIfVptPnniSigVcdIndex"),
)
if mibBuilder.loadTexts:
    atmIfVptPnniSigVcdProvEntry.setStatus("mandatory")


class _AtmIfVptPnniSigVcdTrafficDescType_Type(Integer32):
    """Custom type atmIfVptPnniSigVcdTrafficDescType based on Integer32"""
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


_AtmIfVptPnniSigVcdTrafficDescType_Type.__name__ = "Integer32"
_AtmIfVptPnniSigVcdTrafficDescType_Object = MibTableColumn
atmIfVptPnniSigVcdTrafficDescType = _AtmIfVptPnniSigVcdTrafficDescType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 2, 2, 10, 1, 1),
    _AtmIfVptPnniSigVcdTrafficDescType_Type()
)
atmIfVptPnniSigVcdTrafficDescType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfVptPnniSigVcdTrafficDescType.setStatus("mandatory")


class _AtmIfVptPnniSigVcdAtmServiceCategory_Type(Integer32):
    """Custom type atmIfVptPnniSigVcdAtmServiceCategory based on Integer32"""
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


_AtmIfVptPnniSigVcdAtmServiceCategory_Type.__name__ = "Integer32"
_AtmIfVptPnniSigVcdAtmServiceCategory_Object = MibTableColumn
atmIfVptPnniSigVcdAtmServiceCategory = _AtmIfVptPnniSigVcdAtmServiceCategory_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 2, 2, 10, 1, 3),
    _AtmIfVptPnniSigVcdAtmServiceCategory_Type()
)
atmIfVptPnniSigVcdAtmServiceCategory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfVptPnniSigVcdAtmServiceCategory.setStatus("mandatory")


class _AtmIfVptPnniSigVcdQosClass_Type(Integer32):
    """Custom type atmIfVptPnniSigVcdQosClass based on Integer32"""
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


_AtmIfVptPnniSigVcdQosClass_Type.__name__ = "Integer32"
_AtmIfVptPnniSigVcdQosClass_Object = MibTableColumn
atmIfVptPnniSigVcdQosClass = _AtmIfVptPnniSigVcdQosClass_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 2, 2, 10, 1, 21),
    _AtmIfVptPnniSigVcdQosClass_Type()
)
atmIfVptPnniSigVcdQosClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfVptPnniSigVcdQosClass.setStatus("mandatory")


class _AtmIfVptPnniSigVcdTrafficShaping_Type(Integer32):
    """Custom type atmIfVptPnniSigVcdTrafficShaping based on Integer32"""
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


_AtmIfVptPnniSigVcdTrafficShaping_Type.__name__ = "Integer32"
_AtmIfVptPnniSigVcdTrafficShaping_Object = MibTableColumn
atmIfVptPnniSigVcdTrafficShaping = _AtmIfVptPnniSigVcdTrafficShaping_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 2, 2, 10, 1, 50),
    _AtmIfVptPnniSigVcdTrafficShaping_Type()
)
atmIfVptPnniSigVcdTrafficShaping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfVptPnniSigVcdTrafficShaping.setStatus("mandatory")


class _AtmIfVptPnniSigVcdUnshapedTransmitQueueing_Type(Integer32):
    """Custom type atmIfVptPnniSigVcdUnshapedTransmitQueueing based on Integer32"""
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


_AtmIfVptPnniSigVcdUnshapedTransmitQueueing_Type.__name__ = "Integer32"
_AtmIfVptPnniSigVcdUnshapedTransmitQueueing_Object = MibTableColumn
atmIfVptPnniSigVcdUnshapedTransmitQueueing = _AtmIfVptPnniSigVcdUnshapedTransmitQueueing_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 2, 2, 10, 1, 60),
    _AtmIfVptPnniSigVcdUnshapedTransmitQueueing_Type()
)
atmIfVptPnniSigVcdUnshapedTransmitQueueing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfVptPnniSigVcdUnshapedTransmitQueueing.setStatus("mandatory")


class _AtmIfVptPnniSigVcdUsageParameterControl_Type(Integer32):
    """Custom type atmIfVptPnniSigVcdUsageParameterControl based on Integer32"""
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


_AtmIfVptPnniSigVcdUsageParameterControl_Type.__name__ = "Integer32"
_AtmIfVptPnniSigVcdUsageParameterControl_Object = MibTableColumn
atmIfVptPnniSigVcdUsageParameterControl = _AtmIfVptPnniSigVcdUsageParameterControl_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 2, 2, 10, 1, 70),
    _AtmIfVptPnniSigVcdUsageParameterControl_Type()
)
atmIfVptPnniSigVcdUsageParameterControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfVptPnniSigVcdUsageParameterControl.setStatus("mandatory")
_AtmIfVptPnniSigVcdTdpTable_Object = MibTable
atmIfVptPnniSigVcdTdpTable = _AtmIfVptPnniSigVcdTdpTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 2, 2, 387)
)
if mibBuilder.loadTexts:
    atmIfVptPnniSigVcdTdpTable.setStatus("mandatory")
_AtmIfVptPnniSigVcdTdpEntry_Object = MibTableRow
atmIfVptPnniSigVcdTdpEntry = _AtmIfVptPnniSigVcdTdpEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 2, 2, 387, 1)
)
atmIfVptPnniSigVcdTdpEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfVptIndex"),
    (0, "Nortel-Magellan-Passport-AtmPnniMIB", "atmIfVptPnniIndex"),
    (0, "Nortel-Magellan-Passport-AtmPnniMIB", "atmIfVptPnniSigIndex"),
    (0, "Nortel-Magellan-Passport-AtmPnniMIB", "atmIfVptPnniSigVcdIndex"),
    (0, "Nortel-Magellan-Passport-AtmPnniMIB", "atmIfVptPnniSigVcdTdpIndex"),
)
if mibBuilder.loadTexts:
    atmIfVptPnniSigVcdTdpEntry.setStatus("mandatory")


class _AtmIfVptPnniSigVcdTdpIndex_Type(Integer32):
    """Custom type atmIfVptPnniSigVcdTdpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_AtmIfVptPnniSigVcdTdpIndex_Type.__name__ = "Integer32"
_AtmIfVptPnniSigVcdTdpIndex_Object = MibTableColumn
atmIfVptPnniSigVcdTdpIndex = _AtmIfVptPnniSigVcdTdpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 2, 2, 387, 1, 1),
    _AtmIfVptPnniSigVcdTdpIndex_Type()
)
atmIfVptPnniSigVcdTdpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmIfVptPnniSigVcdTdpIndex.setStatus("mandatory")


class _AtmIfVptPnniSigVcdTdpValue_Type(Unsigned32):
    """Custom type atmIfVptPnniSigVcdTdpValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AtmIfVptPnniSigVcdTdpValue_Type.__name__ = "Unsigned32"
_AtmIfVptPnniSigVcdTdpValue_Object = MibTableColumn
atmIfVptPnniSigVcdTdpValue = _AtmIfVptPnniSigVcdTdpValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 2, 2, 387, 1, 2),
    _AtmIfVptPnniSigVcdTdpValue_Type()
)
atmIfVptPnniSigVcdTdpValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfVptPnniSigVcdTdpValue.setStatus("mandatory")
_AtmIfVptPnniSigProvTable_Object = MibTable
atmIfVptPnniSigProvTable = _AtmIfVptPnniSigProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 2, 10)
)
if mibBuilder.loadTexts:
    atmIfVptPnniSigProvTable.setStatus("mandatory")
_AtmIfVptPnniSigProvEntry_Object = MibTableRow
atmIfVptPnniSigProvEntry = _AtmIfVptPnniSigProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 2, 10, 1)
)
atmIfVptPnniSigProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfVptIndex"),
    (0, "Nortel-Magellan-Passport-AtmPnniMIB", "atmIfVptPnniIndex"),
    (0, "Nortel-Magellan-Passport-AtmPnniMIB", "atmIfVptPnniSigIndex"),
)
if mibBuilder.loadTexts:
    atmIfVptPnniSigProvEntry.setStatus("mandatory")


class _AtmIfVptPnniSigVci_Type(Unsigned32):
    """Custom type atmIfVptPnniSigVci based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AtmIfVptPnniSigVci_Type.__name__ = "Unsigned32"
_AtmIfVptPnniSigVci_Object = MibTableColumn
atmIfVptPnniSigVci = _AtmIfVptPnniSigVci_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 2, 10, 1, 1),
    _AtmIfVptPnniSigVci_Type()
)
atmIfVptPnniSigVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfVptPnniSigVci.setStatus("mandatory")


class _AtmIfVptPnniSigAddressConversion_Type(Integer32):
    """Custom type atmIfVptPnniSigAddressConversion based on Integer32"""
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


_AtmIfVptPnniSigAddressConversion_Type.__name__ = "Integer32"
_AtmIfVptPnniSigAddressConversion_Object = MibTableColumn
atmIfVptPnniSigAddressConversion = _AtmIfVptPnniSigAddressConversion_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 2, 10, 1, 2),
    _AtmIfVptPnniSigAddressConversion_Type()
)
atmIfVptPnniSigAddressConversion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfVptPnniSigAddressConversion.setStatus("mandatory")
_AtmIfVptPnniSigStateTable_Object = MibTable
atmIfVptPnniSigStateTable = _AtmIfVptPnniSigStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 2, 11)
)
if mibBuilder.loadTexts:
    atmIfVptPnniSigStateTable.setStatus("mandatory")
_AtmIfVptPnniSigStateEntry_Object = MibTableRow
atmIfVptPnniSigStateEntry = _AtmIfVptPnniSigStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 2, 11, 1)
)
atmIfVptPnniSigStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfVptIndex"),
    (0, "Nortel-Magellan-Passport-AtmPnniMIB", "atmIfVptPnniIndex"),
    (0, "Nortel-Magellan-Passport-AtmPnniMIB", "atmIfVptPnniSigIndex"),
)
if mibBuilder.loadTexts:
    atmIfVptPnniSigStateEntry.setStatus("mandatory")


class _AtmIfVptPnniSigAdminState_Type(Integer32):
    """Custom type atmIfVptPnniSigAdminState based on Integer32"""
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


_AtmIfVptPnniSigAdminState_Type.__name__ = "Integer32"
_AtmIfVptPnniSigAdminState_Object = MibTableColumn
atmIfVptPnniSigAdminState = _AtmIfVptPnniSigAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 2, 11, 1, 1),
    _AtmIfVptPnniSigAdminState_Type()
)
atmIfVptPnniSigAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVptPnniSigAdminState.setStatus("mandatory")


class _AtmIfVptPnniSigOperationalState_Type(Integer32):
    """Custom type atmIfVptPnniSigOperationalState based on Integer32"""
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


_AtmIfVptPnniSigOperationalState_Type.__name__ = "Integer32"
_AtmIfVptPnniSigOperationalState_Object = MibTableColumn
atmIfVptPnniSigOperationalState = _AtmIfVptPnniSigOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 2, 11, 1, 2),
    _AtmIfVptPnniSigOperationalState_Type()
)
atmIfVptPnniSigOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVptPnniSigOperationalState.setStatus("mandatory")


class _AtmIfVptPnniSigUsageState_Type(Integer32):
    """Custom type atmIfVptPnniSigUsageState based on Integer32"""
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


_AtmIfVptPnniSigUsageState_Type.__name__ = "Integer32"
_AtmIfVptPnniSigUsageState_Object = MibTableColumn
atmIfVptPnniSigUsageState = _AtmIfVptPnniSigUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 2, 11, 1, 3),
    _AtmIfVptPnniSigUsageState_Type()
)
atmIfVptPnniSigUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVptPnniSigUsageState.setStatus("mandatory")
_AtmIfVptPnniSigOperTable_Object = MibTable
atmIfVptPnniSigOperTable = _AtmIfVptPnniSigOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 2, 12)
)
if mibBuilder.loadTexts:
    atmIfVptPnniSigOperTable.setStatus("mandatory")
_AtmIfVptPnniSigOperEntry_Object = MibTableRow
atmIfVptPnniSigOperEntry = _AtmIfVptPnniSigOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 2, 12, 1)
)
atmIfVptPnniSigOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfVptIndex"),
    (0, "Nortel-Magellan-Passport-AtmPnniMIB", "atmIfVptPnniIndex"),
    (0, "Nortel-Magellan-Passport-AtmPnniMIB", "atmIfVptPnniSigIndex"),
)
if mibBuilder.loadTexts:
    atmIfVptPnniSigOperEntry.setStatus("mandatory")


class _AtmIfVptPnniSigLastTxCauseCode_Type(Unsigned32):
    """Custom type atmIfVptPnniSigLastTxCauseCode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AtmIfVptPnniSigLastTxCauseCode_Type.__name__ = "Unsigned32"
_AtmIfVptPnniSigLastTxCauseCode_Object = MibTableColumn
atmIfVptPnniSigLastTxCauseCode = _AtmIfVptPnniSigLastTxCauseCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 2, 12, 1, 1),
    _AtmIfVptPnniSigLastTxCauseCode_Type()
)
atmIfVptPnniSigLastTxCauseCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVptPnniSigLastTxCauseCode.setStatus("mandatory")


class _AtmIfVptPnniSigLastTxDiagCode_Type(Hex):
    """Custom type atmIfVptPnniSigLastTxDiagCode based on Hex"""
    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AtmIfVptPnniSigLastTxDiagCode_Type.__name__ = "Hex"
_AtmIfVptPnniSigLastTxDiagCode_Object = MibTableColumn
atmIfVptPnniSigLastTxDiagCode = _AtmIfVptPnniSigLastTxDiagCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 2, 12, 1, 2),
    _AtmIfVptPnniSigLastTxDiagCode_Type()
)
atmIfVptPnniSigLastTxDiagCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVptPnniSigLastTxDiagCode.setStatus("mandatory")


class _AtmIfVptPnniSigLastRxCauseCode_Type(Unsigned32):
    """Custom type atmIfVptPnniSigLastRxCauseCode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AtmIfVptPnniSigLastRxCauseCode_Type.__name__ = "Unsigned32"
_AtmIfVptPnniSigLastRxCauseCode_Object = MibTableColumn
atmIfVptPnniSigLastRxCauseCode = _AtmIfVptPnniSigLastRxCauseCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 2, 12, 1, 3),
    _AtmIfVptPnniSigLastRxCauseCode_Type()
)
atmIfVptPnniSigLastRxCauseCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVptPnniSigLastRxCauseCode.setStatus("mandatory")


class _AtmIfVptPnniSigLastRxDiagCode_Type(Hex):
    """Custom type atmIfVptPnniSigLastRxDiagCode based on Hex"""
    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AtmIfVptPnniSigLastRxDiagCode_Type.__name__ = "Hex"
_AtmIfVptPnniSigLastRxDiagCode_Object = MibTableColumn
atmIfVptPnniSigLastRxDiagCode = _AtmIfVptPnniSigLastRxDiagCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 2, 12, 1, 4),
    _AtmIfVptPnniSigLastRxDiagCode_Type()
)
atmIfVptPnniSigLastRxDiagCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVptPnniSigLastRxDiagCode.setStatus("mandatory")
_AtmIfVptPnniSigStatsTable_Object = MibTable
atmIfVptPnniSigStatsTable = _AtmIfVptPnniSigStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 2, 13)
)
if mibBuilder.loadTexts:
    atmIfVptPnniSigStatsTable.setStatus("mandatory")
_AtmIfVptPnniSigStatsEntry_Object = MibTableRow
atmIfVptPnniSigStatsEntry = _AtmIfVptPnniSigStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 2, 13, 1)
)
atmIfVptPnniSigStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfVptIndex"),
    (0, "Nortel-Magellan-Passport-AtmPnniMIB", "atmIfVptPnniIndex"),
    (0, "Nortel-Magellan-Passport-AtmPnniMIB", "atmIfVptPnniSigIndex"),
)
if mibBuilder.loadTexts:
    atmIfVptPnniSigStatsEntry.setStatus("mandatory")
_AtmIfVptPnniSigCurrentConnections_Type = Counter32
_AtmIfVptPnniSigCurrentConnections_Object = MibTableColumn
atmIfVptPnniSigCurrentConnections = _AtmIfVptPnniSigCurrentConnections_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 2, 13, 1, 1),
    _AtmIfVptPnniSigCurrentConnections_Type()
)
atmIfVptPnniSigCurrentConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVptPnniSigCurrentConnections.setStatus("obsolete")


class _AtmIfVptPnniSigPeakConnections_Type(Gauge32):
    """Custom type atmIfVptPnniSigPeakConnections based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AtmIfVptPnniSigPeakConnections_Type.__name__ = "Gauge32"
_AtmIfVptPnniSigPeakConnections_Object = MibTableColumn
atmIfVptPnniSigPeakConnections = _AtmIfVptPnniSigPeakConnections_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 2, 13, 1, 2),
    _AtmIfVptPnniSigPeakConnections_Type()
)
atmIfVptPnniSigPeakConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVptPnniSigPeakConnections.setStatus("mandatory")
_AtmIfVptPnniSigSuccessfulConnections_Type = Counter32
_AtmIfVptPnniSigSuccessfulConnections_Object = MibTableColumn
atmIfVptPnniSigSuccessfulConnections = _AtmIfVptPnniSigSuccessfulConnections_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 2, 13, 1, 3),
    _AtmIfVptPnniSigSuccessfulConnections_Type()
)
atmIfVptPnniSigSuccessfulConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVptPnniSigSuccessfulConnections.setStatus("mandatory")
_AtmIfVptPnniSigFailedConnections_Type = Counter32
_AtmIfVptPnniSigFailedConnections_Object = MibTableColumn
atmIfVptPnniSigFailedConnections = _AtmIfVptPnniSigFailedConnections_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 2, 13, 1, 4),
    _AtmIfVptPnniSigFailedConnections_Type()
)
atmIfVptPnniSigFailedConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVptPnniSigFailedConnections.setStatus("mandatory")
_AtmIfVptPnniSigTxPdus_Type = Counter32
_AtmIfVptPnniSigTxPdus_Object = MibTableColumn
atmIfVptPnniSigTxPdus = _AtmIfVptPnniSigTxPdus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 2, 13, 1, 5),
    _AtmIfVptPnniSigTxPdus_Type()
)
atmIfVptPnniSigTxPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVptPnniSigTxPdus.setStatus("mandatory")
_AtmIfVptPnniSigRxPdus_Type = Counter32
_AtmIfVptPnniSigRxPdus_Object = MibTableColumn
atmIfVptPnniSigRxPdus = _AtmIfVptPnniSigRxPdus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 2, 13, 1, 6),
    _AtmIfVptPnniSigRxPdus_Type()
)
atmIfVptPnniSigRxPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVptPnniSigRxPdus.setStatus("mandatory")


class _AtmIfVptPnniSigCurrentPmpConnections_Type(Gauge32):
    """Custom type atmIfVptPnniSigCurrentPmpConnections based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AtmIfVptPnniSigCurrentPmpConnections_Type.__name__ = "Gauge32"
_AtmIfVptPnniSigCurrentPmpConnections_Object = MibTableColumn
atmIfVptPnniSigCurrentPmpConnections = _AtmIfVptPnniSigCurrentPmpConnections_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 2, 13, 1, 7),
    _AtmIfVptPnniSigCurrentPmpConnections_Type()
)
atmIfVptPnniSigCurrentPmpConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVptPnniSigCurrentPmpConnections.setStatus("mandatory")


class _AtmIfVptPnniSigPeakPmpConnections_Type(Gauge32):
    """Custom type atmIfVptPnniSigPeakPmpConnections based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AtmIfVptPnniSigPeakPmpConnections_Type.__name__ = "Gauge32"
_AtmIfVptPnniSigPeakPmpConnections_Object = MibTableColumn
atmIfVptPnniSigPeakPmpConnections = _AtmIfVptPnniSigPeakPmpConnections_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 2, 13, 1, 8),
    _AtmIfVptPnniSigPeakPmpConnections_Type()
)
atmIfVptPnniSigPeakPmpConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVptPnniSigPeakPmpConnections.setStatus("mandatory")
_AtmIfVptPnniSigSuccessfulPmpConnections_Type = Counter32
_AtmIfVptPnniSigSuccessfulPmpConnections_Object = MibTableColumn
atmIfVptPnniSigSuccessfulPmpConnections = _AtmIfVptPnniSigSuccessfulPmpConnections_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 2, 13, 1, 9),
    _AtmIfVptPnniSigSuccessfulPmpConnections_Type()
)
atmIfVptPnniSigSuccessfulPmpConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVptPnniSigSuccessfulPmpConnections.setStatus("mandatory")
_AtmIfVptPnniSigFailedPmpConnections_Type = Counter32
_AtmIfVptPnniSigFailedPmpConnections_Object = MibTableColumn
atmIfVptPnniSigFailedPmpConnections = _AtmIfVptPnniSigFailedPmpConnections_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 2, 13, 1, 10),
    _AtmIfVptPnniSigFailedPmpConnections_Type()
)
atmIfVptPnniSigFailedPmpConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVptPnniSigFailedPmpConnections.setStatus("mandatory")


class _AtmIfVptPnniSigNewCurrentConnections_Type(Gauge32):
    """Custom type atmIfVptPnniSigNewCurrentConnections based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AtmIfVptPnniSigNewCurrentConnections_Type.__name__ = "Gauge32"
_AtmIfVptPnniSigNewCurrentConnections_Object = MibTableColumn
atmIfVptPnniSigNewCurrentConnections = _AtmIfVptPnniSigNewCurrentConnections_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 2, 13, 1, 11),
    _AtmIfVptPnniSigNewCurrentConnections_Type()
)
atmIfVptPnniSigNewCurrentConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVptPnniSigNewCurrentConnections.setStatus("mandatory")
_AtmIfVptPnniRcc_ObjectIdentity = ObjectIdentity
atmIfVptPnniRcc = _AtmIfVptPnniRcc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 3)
)
_AtmIfVptPnniRccRowStatusTable_Object = MibTable
atmIfVptPnniRccRowStatusTable = _AtmIfVptPnniRccRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 3, 1)
)
if mibBuilder.loadTexts:
    atmIfVptPnniRccRowStatusTable.setStatus("mandatory")
_AtmIfVptPnniRccRowStatusEntry_Object = MibTableRow
atmIfVptPnniRccRowStatusEntry = _AtmIfVptPnniRccRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 3, 1, 1)
)
atmIfVptPnniRccRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfVptIndex"),
    (0, "Nortel-Magellan-Passport-AtmPnniMIB", "atmIfVptPnniIndex"),
    (0, "Nortel-Magellan-Passport-AtmPnniMIB", "atmIfVptPnniRccIndex"),
)
if mibBuilder.loadTexts:
    atmIfVptPnniRccRowStatusEntry.setStatus("mandatory")
_AtmIfVptPnniRccRowStatus_Type = RowStatus
_AtmIfVptPnniRccRowStatus_Object = MibTableColumn
atmIfVptPnniRccRowStatus = _AtmIfVptPnniRccRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 3, 1, 1, 1),
    _AtmIfVptPnniRccRowStatus_Type()
)
atmIfVptPnniRccRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVptPnniRccRowStatus.setStatus("mandatory")
_AtmIfVptPnniRccComponentName_Type = DisplayString
_AtmIfVptPnniRccComponentName_Object = MibTableColumn
atmIfVptPnniRccComponentName = _AtmIfVptPnniRccComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 3, 1, 1, 2),
    _AtmIfVptPnniRccComponentName_Type()
)
atmIfVptPnniRccComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVptPnniRccComponentName.setStatus("mandatory")
_AtmIfVptPnniRccStorageType_Type = StorageType
_AtmIfVptPnniRccStorageType_Object = MibTableColumn
atmIfVptPnniRccStorageType = _AtmIfVptPnniRccStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 3, 1, 1, 4),
    _AtmIfVptPnniRccStorageType_Type()
)
atmIfVptPnniRccStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVptPnniRccStorageType.setStatus("mandatory")
_AtmIfVptPnniRccIndex_Type = NonReplicated
_AtmIfVptPnniRccIndex_Object = MibTableColumn
atmIfVptPnniRccIndex = _AtmIfVptPnniRccIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 3, 1, 1, 10),
    _AtmIfVptPnniRccIndex_Type()
)
atmIfVptPnniRccIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmIfVptPnniRccIndex.setStatus("mandatory")
_AtmIfVptPnniRccVcd_ObjectIdentity = ObjectIdentity
atmIfVptPnniRccVcd = _AtmIfVptPnniRccVcd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 3, 2)
)
_AtmIfVptPnniRccVcdRowStatusTable_Object = MibTable
atmIfVptPnniRccVcdRowStatusTable = _AtmIfVptPnniRccVcdRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 3, 2, 1)
)
if mibBuilder.loadTexts:
    atmIfVptPnniRccVcdRowStatusTable.setStatus("mandatory")
_AtmIfVptPnniRccVcdRowStatusEntry_Object = MibTableRow
atmIfVptPnniRccVcdRowStatusEntry = _AtmIfVptPnniRccVcdRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 3, 2, 1, 1)
)
atmIfVptPnniRccVcdRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfVptIndex"),
    (0, "Nortel-Magellan-Passport-AtmPnniMIB", "atmIfVptPnniIndex"),
    (0, "Nortel-Magellan-Passport-AtmPnniMIB", "atmIfVptPnniRccIndex"),
    (0, "Nortel-Magellan-Passport-AtmPnniMIB", "atmIfVptPnniRccVcdIndex"),
)
if mibBuilder.loadTexts:
    atmIfVptPnniRccVcdRowStatusEntry.setStatus("mandatory")
_AtmIfVptPnniRccVcdRowStatus_Type = RowStatus
_AtmIfVptPnniRccVcdRowStatus_Object = MibTableColumn
atmIfVptPnniRccVcdRowStatus = _AtmIfVptPnniRccVcdRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 3, 2, 1, 1, 1),
    _AtmIfVptPnniRccVcdRowStatus_Type()
)
atmIfVptPnniRccVcdRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfVptPnniRccVcdRowStatus.setStatus("mandatory")
_AtmIfVptPnniRccVcdComponentName_Type = DisplayString
_AtmIfVptPnniRccVcdComponentName_Object = MibTableColumn
atmIfVptPnniRccVcdComponentName = _AtmIfVptPnniRccVcdComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 3, 2, 1, 1, 2),
    _AtmIfVptPnniRccVcdComponentName_Type()
)
atmIfVptPnniRccVcdComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVptPnniRccVcdComponentName.setStatus("mandatory")
_AtmIfVptPnniRccVcdStorageType_Type = StorageType
_AtmIfVptPnniRccVcdStorageType_Object = MibTableColumn
atmIfVptPnniRccVcdStorageType = _AtmIfVptPnniRccVcdStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 3, 2, 1, 1, 4),
    _AtmIfVptPnniRccVcdStorageType_Type()
)
atmIfVptPnniRccVcdStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVptPnniRccVcdStorageType.setStatus("mandatory")
_AtmIfVptPnniRccVcdIndex_Type = NonReplicated
_AtmIfVptPnniRccVcdIndex_Object = MibTableColumn
atmIfVptPnniRccVcdIndex = _AtmIfVptPnniRccVcdIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 3, 2, 1, 1, 10),
    _AtmIfVptPnniRccVcdIndex_Type()
)
atmIfVptPnniRccVcdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmIfVptPnniRccVcdIndex.setStatus("mandatory")
_AtmIfVptPnniRccVcdProvTable_Object = MibTable
atmIfVptPnniRccVcdProvTable = _AtmIfVptPnniRccVcdProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 3, 2, 10)
)
if mibBuilder.loadTexts:
    atmIfVptPnniRccVcdProvTable.setStatus("mandatory")
_AtmIfVptPnniRccVcdProvEntry_Object = MibTableRow
atmIfVptPnniRccVcdProvEntry = _AtmIfVptPnniRccVcdProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 3, 2, 10, 1)
)
atmIfVptPnniRccVcdProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfVptIndex"),
    (0, "Nortel-Magellan-Passport-AtmPnniMIB", "atmIfVptPnniIndex"),
    (0, "Nortel-Magellan-Passport-AtmPnniMIB", "atmIfVptPnniRccIndex"),
    (0, "Nortel-Magellan-Passport-AtmPnniMIB", "atmIfVptPnniRccVcdIndex"),
)
if mibBuilder.loadTexts:
    atmIfVptPnniRccVcdProvEntry.setStatus("mandatory")


class _AtmIfVptPnniRccVcdTrafficDescType_Type(Integer32):
    """Custom type atmIfVptPnniRccVcdTrafficDescType based on Integer32"""
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


_AtmIfVptPnniRccVcdTrafficDescType_Type.__name__ = "Integer32"
_AtmIfVptPnniRccVcdTrafficDescType_Object = MibTableColumn
atmIfVptPnniRccVcdTrafficDescType = _AtmIfVptPnniRccVcdTrafficDescType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 3, 2, 10, 1, 1),
    _AtmIfVptPnniRccVcdTrafficDescType_Type()
)
atmIfVptPnniRccVcdTrafficDescType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfVptPnniRccVcdTrafficDescType.setStatus("mandatory")


class _AtmIfVptPnniRccVcdAtmServiceCategory_Type(Integer32):
    """Custom type atmIfVptPnniRccVcdAtmServiceCategory based on Integer32"""
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


_AtmIfVptPnniRccVcdAtmServiceCategory_Type.__name__ = "Integer32"
_AtmIfVptPnniRccVcdAtmServiceCategory_Object = MibTableColumn
atmIfVptPnniRccVcdAtmServiceCategory = _AtmIfVptPnniRccVcdAtmServiceCategory_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 3, 2, 10, 1, 3),
    _AtmIfVptPnniRccVcdAtmServiceCategory_Type()
)
atmIfVptPnniRccVcdAtmServiceCategory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfVptPnniRccVcdAtmServiceCategory.setStatus("mandatory")


class _AtmIfVptPnniRccVcdQosClass_Type(Integer32):
    """Custom type atmIfVptPnniRccVcdQosClass based on Integer32"""
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


_AtmIfVptPnniRccVcdQosClass_Type.__name__ = "Integer32"
_AtmIfVptPnniRccVcdQosClass_Object = MibTableColumn
atmIfVptPnniRccVcdQosClass = _AtmIfVptPnniRccVcdQosClass_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 3, 2, 10, 1, 21),
    _AtmIfVptPnniRccVcdQosClass_Type()
)
atmIfVptPnniRccVcdQosClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfVptPnniRccVcdQosClass.setStatus("mandatory")


class _AtmIfVptPnniRccVcdTrafficShaping_Type(Integer32):
    """Custom type atmIfVptPnniRccVcdTrafficShaping based on Integer32"""
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


_AtmIfVptPnniRccVcdTrafficShaping_Type.__name__ = "Integer32"
_AtmIfVptPnniRccVcdTrafficShaping_Object = MibTableColumn
atmIfVptPnniRccVcdTrafficShaping = _AtmIfVptPnniRccVcdTrafficShaping_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 3, 2, 10, 1, 50),
    _AtmIfVptPnniRccVcdTrafficShaping_Type()
)
atmIfVptPnniRccVcdTrafficShaping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfVptPnniRccVcdTrafficShaping.setStatus("mandatory")


class _AtmIfVptPnniRccVcdUnshapedTransmitQueueing_Type(Integer32):
    """Custom type atmIfVptPnniRccVcdUnshapedTransmitQueueing based on Integer32"""
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


_AtmIfVptPnniRccVcdUnshapedTransmitQueueing_Type.__name__ = "Integer32"
_AtmIfVptPnniRccVcdUnshapedTransmitQueueing_Object = MibTableColumn
atmIfVptPnniRccVcdUnshapedTransmitQueueing = _AtmIfVptPnniRccVcdUnshapedTransmitQueueing_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 3, 2, 10, 1, 60),
    _AtmIfVptPnniRccVcdUnshapedTransmitQueueing_Type()
)
atmIfVptPnniRccVcdUnshapedTransmitQueueing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfVptPnniRccVcdUnshapedTransmitQueueing.setStatus("mandatory")


class _AtmIfVptPnniRccVcdUsageParameterControl_Type(Integer32):
    """Custom type atmIfVptPnniRccVcdUsageParameterControl based on Integer32"""
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


_AtmIfVptPnniRccVcdUsageParameterControl_Type.__name__ = "Integer32"
_AtmIfVptPnniRccVcdUsageParameterControl_Object = MibTableColumn
atmIfVptPnniRccVcdUsageParameterControl = _AtmIfVptPnniRccVcdUsageParameterControl_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 3, 2, 10, 1, 70),
    _AtmIfVptPnniRccVcdUsageParameterControl_Type()
)
atmIfVptPnniRccVcdUsageParameterControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfVptPnniRccVcdUsageParameterControl.setStatus("mandatory")
_AtmIfVptPnniRccVcdTdpTable_Object = MibTable
atmIfVptPnniRccVcdTdpTable = _AtmIfVptPnniRccVcdTdpTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 3, 2, 387)
)
if mibBuilder.loadTexts:
    atmIfVptPnniRccVcdTdpTable.setStatus("mandatory")
_AtmIfVptPnniRccVcdTdpEntry_Object = MibTableRow
atmIfVptPnniRccVcdTdpEntry = _AtmIfVptPnniRccVcdTdpEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 3, 2, 387, 1)
)
atmIfVptPnniRccVcdTdpEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfVptIndex"),
    (0, "Nortel-Magellan-Passport-AtmPnniMIB", "atmIfVptPnniIndex"),
    (0, "Nortel-Magellan-Passport-AtmPnniMIB", "atmIfVptPnniRccIndex"),
    (0, "Nortel-Magellan-Passport-AtmPnniMIB", "atmIfVptPnniRccVcdIndex"),
    (0, "Nortel-Magellan-Passport-AtmPnniMIB", "atmIfVptPnniRccVcdTdpIndex"),
)
if mibBuilder.loadTexts:
    atmIfVptPnniRccVcdTdpEntry.setStatus("mandatory")


class _AtmIfVptPnniRccVcdTdpIndex_Type(Integer32):
    """Custom type atmIfVptPnniRccVcdTdpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_AtmIfVptPnniRccVcdTdpIndex_Type.__name__ = "Integer32"
_AtmIfVptPnniRccVcdTdpIndex_Object = MibTableColumn
atmIfVptPnniRccVcdTdpIndex = _AtmIfVptPnniRccVcdTdpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 3, 2, 387, 1, 1),
    _AtmIfVptPnniRccVcdTdpIndex_Type()
)
atmIfVptPnniRccVcdTdpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmIfVptPnniRccVcdTdpIndex.setStatus("mandatory")


class _AtmIfVptPnniRccVcdTdpValue_Type(Unsigned32):
    """Custom type atmIfVptPnniRccVcdTdpValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AtmIfVptPnniRccVcdTdpValue_Type.__name__ = "Unsigned32"
_AtmIfVptPnniRccVcdTdpValue_Object = MibTableColumn
atmIfVptPnniRccVcdTdpValue = _AtmIfVptPnniRccVcdTdpValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 3, 2, 387, 1, 2),
    _AtmIfVptPnniRccVcdTdpValue_Type()
)
atmIfVptPnniRccVcdTdpValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfVptPnniRccVcdTdpValue.setStatus("mandatory")
_AtmIfVptPnniRccProvTable_Object = MibTable
atmIfVptPnniRccProvTable = _AtmIfVptPnniRccProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 3, 10)
)
if mibBuilder.loadTexts:
    atmIfVptPnniRccProvTable.setStatus("mandatory")
_AtmIfVptPnniRccProvEntry_Object = MibTableRow
atmIfVptPnniRccProvEntry = _AtmIfVptPnniRccProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 3, 10, 1)
)
atmIfVptPnniRccProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfVptIndex"),
    (0, "Nortel-Magellan-Passport-AtmPnniMIB", "atmIfVptPnniIndex"),
    (0, "Nortel-Magellan-Passport-AtmPnniMIB", "atmIfVptPnniRccIndex"),
)
if mibBuilder.loadTexts:
    atmIfVptPnniRccProvEntry.setStatus("mandatory")


class _AtmIfVptPnniRccVci_Type(Unsigned32):
    """Custom type atmIfVptPnniRccVci based on Unsigned32"""
    defaultValue = 18

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AtmIfVptPnniRccVci_Type.__name__ = "Unsigned32"
_AtmIfVptPnniRccVci_Object = MibTableColumn
atmIfVptPnniRccVci = _AtmIfVptPnniRccVci_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 3, 10, 1, 1),
    _AtmIfVptPnniRccVci_Type()
)
atmIfVptPnniRccVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfVptPnniRccVci.setStatus("mandatory")
_AtmIfVptPnniRccHlParmsTable_Object = MibTable
atmIfVptPnniRccHlParmsTable = _AtmIfVptPnniRccHlParmsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 3, 11)
)
if mibBuilder.loadTexts:
    atmIfVptPnniRccHlParmsTable.setStatus("mandatory")
_AtmIfVptPnniRccHlParmsEntry_Object = MibTableRow
atmIfVptPnniRccHlParmsEntry = _AtmIfVptPnniRccHlParmsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 3, 11, 1)
)
atmIfVptPnniRccHlParmsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfVptIndex"),
    (0, "Nortel-Magellan-Passport-AtmPnniMIB", "atmIfVptPnniIndex"),
    (0, "Nortel-Magellan-Passport-AtmPnniMIB", "atmIfVptPnniRccIndex"),
)
if mibBuilder.loadTexts:
    atmIfVptPnniRccHlParmsEntry.setStatus("mandatory")


class _AtmIfVptPnniRccHelloHoldDown_Type(FixedPoint1):
    """Custom type atmIfVptPnniRccHelloHoldDown based on FixedPoint1"""
    defaultValue = 0

    subtypeSpec = FixedPoint1.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 655350),
    )


_AtmIfVptPnniRccHelloHoldDown_Type.__name__ = "FixedPoint1"
_AtmIfVptPnniRccHelloHoldDown_Object = MibTableColumn
atmIfVptPnniRccHelloHoldDown = _AtmIfVptPnniRccHelloHoldDown_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 3, 11, 1, 1),
    _AtmIfVptPnniRccHelloHoldDown_Type()
)
atmIfVptPnniRccHelloHoldDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfVptPnniRccHelloHoldDown.setStatus("mandatory")


class _AtmIfVptPnniRccHelloInterval_Type(Unsigned32):
    """Custom type atmIfVptPnniRccHelloInterval based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AtmIfVptPnniRccHelloInterval_Type.__name__ = "Unsigned32"
_AtmIfVptPnniRccHelloInterval_Object = MibTableColumn
atmIfVptPnniRccHelloInterval = _AtmIfVptPnniRccHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 3, 11, 1, 2),
    _AtmIfVptPnniRccHelloInterval_Type()
)
atmIfVptPnniRccHelloInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfVptPnniRccHelloInterval.setStatus("mandatory")


class _AtmIfVptPnniRccHelloInactivityFactor_Type(Unsigned32):
    """Custom type atmIfVptPnniRccHelloInactivityFactor based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AtmIfVptPnniRccHelloInactivityFactor_Type.__name__ = "Unsigned32"
_AtmIfVptPnniRccHelloInactivityFactor_Object = MibTableColumn
atmIfVptPnniRccHelloInactivityFactor = _AtmIfVptPnniRccHelloInactivityFactor_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 3, 11, 1, 3),
    _AtmIfVptPnniRccHelloInactivityFactor_Type()
)
atmIfVptPnniRccHelloInactivityFactor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfVptPnniRccHelloInactivityFactor.setStatus("mandatory")
_AtmIfVptPnniRccStateTable_Object = MibTable
atmIfVptPnniRccStateTable = _AtmIfVptPnniRccStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 3, 12)
)
if mibBuilder.loadTexts:
    atmIfVptPnniRccStateTable.setStatus("mandatory")
_AtmIfVptPnniRccStateEntry_Object = MibTableRow
atmIfVptPnniRccStateEntry = _AtmIfVptPnniRccStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 3, 12, 1)
)
atmIfVptPnniRccStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfVptIndex"),
    (0, "Nortel-Magellan-Passport-AtmPnniMIB", "atmIfVptPnniIndex"),
    (0, "Nortel-Magellan-Passport-AtmPnniMIB", "atmIfVptPnniRccIndex"),
)
if mibBuilder.loadTexts:
    atmIfVptPnniRccStateEntry.setStatus("mandatory")


class _AtmIfVptPnniRccAdminState_Type(Integer32):
    """Custom type atmIfVptPnniRccAdminState based on Integer32"""
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


_AtmIfVptPnniRccAdminState_Type.__name__ = "Integer32"
_AtmIfVptPnniRccAdminState_Object = MibTableColumn
atmIfVptPnniRccAdminState = _AtmIfVptPnniRccAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 3, 12, 1, 1),
    _AtmIfVptPnniRccAdminState_Type()
)
atmIfVptPnniRccAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVptPnniRccAdminState.setStatus("mandatory")


class _AtmIfVptPnniRccOperationalState_Type(Integer32):
    """Custom type atmIfVptPnniRccOperationalState based on Integer32"""
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


_AtmIfVptPnniRccOperationalState_Type.__name__ = "Integer32"
_AtmIfVptPnniRccOperationalState_Object = MibTableColumn
atmIfVptPnniRccOperationalState = _AtmIfVptPnniRccOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 3, 12, 1, 2),
    _AtmIfVptPnniRccOperationalState_Type()
)
atmIfVptPnniRccOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVptPnniRccOperationalState.setStatus("mandatory")


class _AtmIfVptPnniRccUsageState_Type(Integer32):
    """Custom type atmIfVptPnniRccUsageState based on Integer32"""
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


_AtmIfVptPnniRccUsageState_Type.__name__ = "Integer32"
_AtmIfVptPnniRccUsageState_Object = MibTableColumn
atmIfVptPnniRccUsageState = _AtmIfVptPnniRccUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 3, 12, 1, 3),
    _AtmIfVptPnniRccUsageState_Type()
)
atmIfVptPnniRccUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVptPnniRccUsageState.setStatus("mandatory")
_AtmIfVptPnniRccOperTable_Object = MibTable
atmIfVptPnniRccOperTable = _AtmIfVptPnniRccOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 3, 13)
)
if mibBuilder.loadTexts:
    atmIfVptPnniRccOperTable.setStatus("mandatory")
_AtmIfVptPnniRccOperEntry_Object = MibTableRow
atmIfVptPnniRccOperEntry = _AtmIfVptPnniRccOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 3, 13, 1)
)
atmIfVptPnniRccOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfVptIndex"),
    (0, "Nortel-Magellan-Passport-AtmPnniMIB", "atmIfVptPnniIndex"),
    (0, "Nortel-Magellan-Passport-AtmPnniMIB", "atmIfVptPnniRccIndex"),
)
if mibBuilder.loadTexts:
    atmIfVptPnniRccOperEntry.setStatus("mandatory")


class _AtmIfVptPnniRccType_Type(Integer32):
    """Custom type atmIfVptPnniRccType based on Integer32"""
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


_AtmIfVptPnniRccType_Type.__name__ = "Integer32"
_AtmIfVptPnniRccType_Object = MibTableColumn
atmIfVptPnniRccType = _AtmIfVptPnniRccType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 3, 13, 1, 1),
    _AtmIfVptPnniRccType_Type()
)
atmIfVptPnniRccType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVptPnniRccType.setStatus("mandatory")


class _AtmIfVptPnniRccNegotiatedVersion_Type(Integer32):
    """Custom type atmIfVptPnniRccNegotiatedVersion based on Integer32"""
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


_AtmIfVptPnniRccNegotiatedVersion_Type.__name__ = "Integer32"
_AtmIfVptPnniRccNegotiatedVersion_Object = MibTableColumn
atmIfVptPnniRccNegotiatedVersion = _AtmIfVptPnniRccNegotiatedVersion_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 3, 13, 1, 2),
    _AtmIfVptPnniRccNegotiatedVersion_Type()
)
atmIfVptPnniRccNegotiatedVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVptPnniRccNegotiatedVersion.setStatus("mandatory")


class _AtmIfVptPnniRccHelloState_Type(Integer32):
    """Custom type atmIfVptPnniRccHelloState based on Integer32"""
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


_AtmIfVptPnniRccHelloState_Type.__name__ = "Integer32"
_AtmIfVptPnniRccHelloState_Object = MibTableColumn
atmIfVptPnniRccHelloState = _AtmIfVptPnniRccHelloState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 3, 13, 1, 3),
    _AtmIfVptPnniRccHelloState_Type()
)
atmIfVptPnniRccHelloState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVptPnniRccHelloState.setStatus("mandatory")


class _AtmIfVptPnniRccRemoteNodeId_Type(HexString):
    """Custom type atmIfVptPnniRccRemoteNodeId based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(22, 22),
    )


_AtmIfVptPnniRccRemoteNodeId_Type.__name__ = "HexString"
_AtmIfVptPnniRccRemoteNodeId_Object = MibTableColumn
atmIfVptPnniRccRemoteNodeId = _AtmIfVptPnniRccRemoteNodeId_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 3, 13, 1, 4),
    _AtmIfVptPnniRccRemoteNodeId_Type()
)
atmIfVptPnniRccRemoteNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVptPnniRccRemoteNodeId.setStatus("mandatory")


class _AtmIfVptPnniRccRemotePortId_Type(Unsigned32):
    """Custom type atmIfVptPnniRccRemotePortId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AtmIfVptPnniRccRemotePortId_Type.__name__ = "Unsigned32"
_AtmIfVptPnniRccRemotePortId_Object = MibTableColumn
atmIfVptPnniRccRemotePortId = _AtmIfVptPnniRccRemotePortId_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 3, 13, 1, 5),
    _AtmIfVptPnniRccRemotePortId_Type()
)
atmIfVptPnniRccRemotePortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVptPnniRccRemotePortId.setStatus("mandatory")
_AtmIfVptPnniRccStatsTable_Object = MibTable
atmIfVptPnniRccStatsTable = _AtmIfVptPnniRccStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 3, 14)
)
if mibBuilder.loadTexts:
    atmIfVptPnniRccStatsTable.setStatus("mandatory")
_AtmIfVptPnniRccStatsEntry_Object = MibTableRow
atmIfVptPnniRccStatsEntry = _AtmIfVptPnniRccStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 3, 14, 1)
)
atmIfVptPnniRccStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfVptIndex"),
    (0, "Nortel-Magellan-Passport-AtmPnniMIB", "atmIfVptPnniIndex"),
    (0, "Nortel-Magellan-Passport-AtmPnniMIB", "atmIfVptPnniRccIndex"),
)
if mibBuilder.loadTexts:
    atmIfVptPnniRccStatsEntry.setStatus("mandatory")
_AtmIfVptPnniRccHelloPacketsRx_Type = Counter32
_AtmIfVptPnniRccHelloPacketsRx_Object = MibTableColumn
atmIfVptPnniRccHelloPacketsRx = _AtmIfVptPnniRccHelloPacketsRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 3, 14, 1, 1),
    _AtmIfVptPnniRccHelloPacketsRx_Type()
)
atmIfVptPnniRccHelloPacketsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVptPnniRccHelloPacketsRx.setStatus("mandatory")
_AtmIfVptPnniRccHelloPacketsTx_Type = Counter32
_AtmIfVptPnniRccHelloPacketsTx_Object = MibTableColumn
atmIfVptPnniRccHelloPacketsTx = _AtmIfVptPnniRccHelloPacketsTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 3, 14, 1, 2),
    _AtmIfVptPnniRccHelloPacketsTx_Type()
)
atmIfVptPnniRccHelloPacketsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVptPnniRccHelloPacketsTx.setStatus("mandatory")
_AtmIfVptPnniRccMismatchedHelloPacketsRx_Type = Counter32
_AtmIfVptPnniRccMismatchedHelloPacketsRx_Object = MibTableColumn
atmIfVptPnniRccMismatchedHelloPacketsRx = _AtmIfVptPnniRccMismatchedHelloPacketsRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 3, 14, 1, 3),
    _AtmIfVptPnniRccMismatchedHelloPacketsRx_Type()
)
atmIfVptPnniRccMismatchedHelloPacketsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVptPnniRccMismatchedHelloPacketsRx.setStatus("mandatory")
_AtmIfVptPnniRccBadHelloPacketsRx_Type = Counter32
_AtmIfVptPnniRccBadHelloPacketsRx_Object = MibTableColumn
atmIfVptPnniRccBadHelloPacketsRx = _AtmIfVptPnniRccBadHelloPacketsRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 3, 14, 1, 4),
    _AtmIfVptPnniRccBadHelloPacketsRx_Type()
)
atmIfVptPnniRccBadHelloPacketsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVptPnniRccBadHelloPacketsRx.setStatus("mandatory")
_AtmIfVptPnniAddr_ObjectIdentity = ObjectIdentity
atmIfVptPnniAddr = _AtmIfVptPnniAddr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 4)
)
_AtmIfVptPnniAddrRowStatusTable_Object = MibTable
atmIfVptPnniAddrRowStatusTable = _AtmIfVptPnniAddrRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 4, 1)
)
if mibBuilder.loadTexts:
    atmIfVptPnniAddrRowStatusTable.setStatus("mandatory")
_AtmIfVptPnniAddrRowStatusEntry_Object = MibTableRow
atmIfVptPnniAddrRowStatusEntry = _AtmIfVptPnniAddrRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 4, 1, 1)
)
atmIfVptPnniAddrRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfVptIndex"),
    (0, "Nortel-Magellan-Passport-AtmPnniMIB", "atmIfVptPnniIndex"),
    (0, "Nortel-Magellan-Passport-AtmPnniMIB", "atmIfVptPnniAddrAddressIndex"),
    (0, "Nortel-Magellan-Passport-AtmPnniMIB", "atmIfVptPnniAddrAddressTypeIndex"),
)
if mibBuilder.loadTexts:
    atmIfVptPnniAddrRowStatusEntry.setStatus("mandatory")
_AtmIfVptPnniAddrRowStatus_Type = RowStatus
_AtmIfVptPnniAddrRowStatus_Object = MibTableColumn
atmIfVptPnniAddrRowStatus = _AtmIfVptPnniAddrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 4, 1, 1, 1),
    _AtmIfVptPnniAddrRowStatus_Type()
)
atmIfVptPnniAddrRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfVptPnniAddrRowStatus.setStatus("mandatory")
_AtmIfVptPnniAddrComponentName_Type = DisplayString
_AtmIfVptPnniAddrComponentName_Object = MibTableColumn
atmIfVptPnniAddrComponentName = _AtmIfVptPnniAddrComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 4, 1, 1, 2),
    _AtmIfVptPnniAddrComponentName_Type()
)
atmIfVptPnniAddrComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVptPnniAddrComponentName.setStatus("mandatory")
_AtmIfVptPnniAddrStorageType_Type = StorageType
_AtmIfVptPnniAddrStorageType_Object = MibTableColumn
atmIfVptPnniAddrStorageType = _AtmIfVptPnniAddrStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 4, 1, 1, 4),
    _AtmIfVptPnniAddrStorageType_Type()
)
atmIfVptPnniAddrStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVptPnniAddrStorageType.setStatus("mandatory")


class _AtmIfVptPnniAddrAddressIndex_Type(AsciiStringIndex):
    """Custom type atmIfVptPnniAddrAddressIndex based on AsciiStringIndex"""
    subtypeSpec = AsciiStringIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_AtmIfVptPnniAddrAddressIndex_Type.__name__ = "AsciiStringIndex"
_AtmIfVptPnniAddrAddressIndex_Object = MibTableColumn
atmIfVptPnniAddrAddressIndex = _AtmIfVptPnniAddrAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 4, 1, 1, 10),
    _AtmIfVptPnniAddrAddressIndex_Type()
)
atmIfVptPnniAddrAddressIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmIfVptPnniAddrAddressIndex.setStatus("mandatory")


class _AtmIfVptPnniAddrAddressTypeIndex_Type(Integer32):
    """Custom type atmIfVptPnniAddrAddressTypeIndex based on Integer32"""
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


_AtmIfVptPnniAddrAddressTypeIndex_Type.__name__ = "Integer32"
_AtmIfVptPnniAddrAddressTypeIndex_Object = MibTableColumn
atmIfVptPnniAddrAddressTypeIndex = _AtmIfVptPnniAddrAddressTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 4, 1, 1, 11),
    _AtmIfVptPnniAddrAddressTypeIndex_Type()
)
atmIfVptPnniAddrAddressTypeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmIfVptPnniAddrAddressTypeIndex.setStatus("mandatory")
_AtmIfVptPnniAddrTermSP_ObjectIdentity = ObjectIdentity
atmIfVptPnniAddrTermSP = _AtmIfVptPnniAddrTermSP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 4, 2)
)
_AtmIfVptPnniAddrTermSPRowStatusTable_Object = MibTable
atmIfVptPnniAddrTermSPRowStatusTable = _AtmIfVptPnniAddrTermSPRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 4, 2, 1)
)
if mibBuilder.loadTexts:
    atmIfVptPnniAddrTermSPRowStatusTable.setStatus("mandatory")
_AtmIfVptPnniAddrTermSPRowStatusEntry_Object = MibTableRow
atmIfVptPnniAddrTermSPRowStatusEntry = _AtmIfVptPnniAddrTermSPRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 4, 2, 1, 1)
)
atmIfVptPnniAddrTermSPRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfVptIndex"),
    (0, "Nortel-Magellan-Passport-AtmPnniMIB", "atmIfVptPnniIndex"),
    (0, "Nortel-Magellan-Passport-AtmPnniMIB", "atmIfVptPnniAddrAddressIndex"),
    (0, "Nortel-Magellan-Passport-AtmPnniMIB", "atmIfVptPnniAddrAddressTypeIndex"),
    (0, "Nortel-Magellan-Passport-AtmPnniMIB", "atmIfVptPnniAddrTermSPIndex"),
)
if mibBuilder.loadTexts:
    atmIfVptPnniAddrTermSPRowStatusEntry.setStatus("mandatory")
_AtmIfVptPnniAddrTermSPRowStatus_Type = RowStatus
_AtmIfVptPnniAddrTermSPRowStatus_Object = MibTableColumn
atmIfVptPnniAddrTermSPRowStatus = _AtmIfVptPnniAddrTermSPRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 4, 2, 1, 1, 1),
    _AtmIfVptPnniAddrTermSPRowStatus_Type()
)
atmIfVptPnniAddrTermSPRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfVptPnniAddrTermSPRowStatus.setStatus("mandatory")
_AtmIfVptPnniAddrTermSPComponentName_Type = DisplayString
_AtmIfVptPnniAddrTermSPComponentName_Object = MibTableColumn
atmIfVptPnniAddrTermSPComponentName = _AtmIfVptPnniAddrTermSPComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 4, 2, 1, 1, 2),
    _AtmIfVptPnniAddrTermSPComponentName_Type()
)
atmIfVptPnniAddrTermSPComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVptPnniAddrTermSPComponentName.setStatus("mandatory")
_AtmIfVptPnniAddrTermSPStorageType_Type = StorageType
_AtmIfVptPnniAddrTermSPStorageType_Object = MibTableColumn
atmIfVptPnniAddrTermSPStorageType = _AtmIfVptPnniAddrTermSPStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 4, 2, 1, 1, 4),
    _AtmIfVptPnniAddrTermSPStorageType_Type()
)
atmIfVptPnniAddrTermSPStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVptPnniAddrTermSPStorageType.setStatus("mandatory")
_AtmIfVptPnniAddrTermSPIndex_Type = NonReplicated
_AtmIfVptPnniAddrTermSPIndex_Object = MibTableColumn
atmIfVptPnniAddrTermSPIndex = _AtmIfVptPnniAddrTermSPIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 4, 2, 1, 1, 10),
    _AtmIfVptPnniAddrTermSPIndex_Type()
)
atmIfVptPnniAddrTermSPIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmIfVptPnniAddrTermSPIndex.setStatus("mandatory")
_AtmIfVptPnniAddrPnniInfo_ObjectIdentity = ObjectIdentity
atmIfVptPnniAddrPnniInfo = _AtmIfVptPnniAddrPnniInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 4, 3)
)
_AtmIfVptPnniAddrPnniInfoRowStatusTable_Object = MibTable
atmIfVptPnniAddrPnniInfoRowStatusTable = _AtmIfVptPnniAddrPnniInfoRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 4, 3, 1)
)
if mibBuilder.loadTexts:
    atmIfVptPnniAddrPnniInfoRowStatusTable.setStatus("mandatory")
_AtmIfVptPnniAddrPnniInfoRowStatusEntry_Object = MibTableRow
atmIfVptPnniAddrPnniInfoRowStatusEntry = _AtmIfVptPnniAddrPnniInfoRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 4, 3, 1, 1)
)
atmIfVptPnniAddrPnniInfoRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfVptIndex"),
    (0, "Nortel-Magellan-Passport-AtmPnniMIB", "atmIfVptPnniIndex"),
    (0, "Nortel-Magellan-Passport-AtmPnniMIB", "atmIfVptPnniAddrAddressIndex"),
    (0, "Nortel-Magellan-Passport-AtmPnniMIB", "atmIfVptPnniAddrAddressTypeIndex"),
    (0, "Nortel-Magellan-Passport-AtmPnniMIB", "atmIfVptPnniAddrPnniInfoIndex"),
)
if mibBuilder.loadTexts:
    atmIfVptPnniAddrPnniInfoRowStatusEntry.setStatus("mandatory")
_AtmIfVptPnniAddrPnniInfoRowStatus_Type = RowStatus
_AtmIfVptPnniAddrPnniInfoRowStatus_Object = MibTableColumn
atmIfVptPnniAddrPnniInfoRowStatus = _AtmIfVptPnniAddrPnniInfoRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 4, 3, 1, 1, 1),
    _AtmIfVptPnniAddrPnniInfoRowStatus_Type()
)
atmIfVptPnniAddrPnniInfoRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfVptPnniAddrPnniInfoRowStatus.setStatus("mandatory")
_AtmIfVptPnniAddrPnniInfoComponentName_Type = DisplayString
_AtmIfVptPnniAddrPnniInfoComponentName_Object = MibTableColumn
atmIfVptPnniAddrPnniInfoComponentName = _AtmIfVptPnniAddrPnniInfoComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 4, 3, 1, 1, 2),
    _AtmIfVptPnniAddrPnniInfoComponentName_Type()
)
atmIfVptPnniAddrPnniInfoComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVptPnniAddrPnniInfoComponentName.setStatus("mandatory")
_AtmIfVptPnniAddrPnniInfoStorageType_Type = StorageType
_AtmIfVptPnniAddrPnniInfoStorageType_Object = MibTableColumn
atmIfVptPnniAddrPnniInfoStorageType = _AtmIfVptPnniAddrPnniInfoStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 4, 3, 1, 1, 4),
    _AtmIfVptPnniAddrPnniInfoStorageType_Type()
)
atmIfVptPnniAddrPnniInfoStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVptPnniAddrPnniInfoStorageType.setStatus("mandatory")
_AtmIfVptPnniAddrPnniInfoIndex_Type = NonReplicated
_AtmIfVptPnniAddrPnniInfoIndex_Object = MibTableColumn
atmIfVptPnniAddrPnniInfoIndex = _AtmIfVptPnniAddrPnniInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 4, 3, 1, 1, 10),
    _AtmIfVptPnniAddrPnniInfoIndex_Type()
)
atmIfVptPnniAddrPnniInfoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmIfVptPnniAddrPnniInfoIndex.setStatus("mandatory")
_AtmIfVptPnniAddrPnniInfoProvTable_Object = MibTable
atmIfVptPnniAddrPnniInfoProvTable = _AtmIfVptPnniAddrPnniInfoProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 4, 3, 10)
)
if mibBuilder.loadTexts:
    atmIfVptPnniAddrPnniInfoProvTable.setStatus("mandatory")
_AtmIfVptPnniAddrPnniInfoProvEntry_Object = MibTableRow
atmIfVptPnniAddrPnniInfoProvEntry = _AtmIfVptPnniAddrPnniInfoProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 4, 3, 10, 1)
)
atmIfVptPnniAddrPnniInfoProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfVptIndex"),
    (0, "Nortel-Magellan-Passport-AtmPnniMIB", "atmIfVptPnniIndex"),
    (0, "Nortel-Magellan-Passport-AtmPnniMIB", "atmIfVptPnniAddrAddressIndex"),
    (0, "Nortel-Magellan-Passport-AtmPnniMIB", "atmIfVptPnniAddrAddressTypeIndex"),
    (0, "Nortel-Magellan-Passport-AtmPnniMIB", "atmIfVptPnniAddrPnniInfoIndex"),
)
if mibBuilder.loadTexts:
    atmIfVptPnniAddrPnniInfoProvEntry.setStatus("mandatory")


class _AtmIfVptPnniAddrPnniInfoScope_Type(Integer32):
    """Custom type atmIfVptPnniAddrPnniInfoScope based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 104),
    )


_AtmIfVptPnniAddrPnniInfoScope_Type.__name__ = "Integer32"
_AtmIfVptPnniAddrPnniInfoScope_Object = MibTableColumn
atmIfVptPnniAddrPnniInfoScope = _AtmIfVptPnniAddrPnniInfoScope_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 4, 3, 10, 1, 1),
    _AtmIfVptPnniAddrPnniInfoScope_Type()
)
atmIfVptPnniAddrPnniInfoScope.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfVptPnniAddrPnniInfoScope.setStatus("mandatory")


class _AtmIfVptPnniAddrPnniInfoReachability_Type(Integer32):
    """Custom type atmIfVptPnniAddrPnniInfoReachability based on Integer32"""
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


_AtmIfVptPnniAddrPnniInfoReachability_Type.__name__ = "Integer32"
_AtmIfVptPnniAddrPnniInfoReachability_Object = MibTableColumn
atmIfVptPnniAddrPnniInfoReachability = _AtmIfVptPnniAddrPnniInfoReachability_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 4, 3, 10, 1, 2),
    _AtmIfVptPnniAddrPnniInfoReachability_Type()
)
atmIfVptPnniAddrPnniInfoReachability.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfVptPnniAddrPnniInfoReachability.setStatus("mandatory")
_AtmIfVptPnniAddrOperTable_Object = MibTable
atmIfVptPnniAddrOperTable = _AtmIfVptPnniAddrOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 4, 10)
)
if mibBuilder.loadTexts:
    atmIfVptPnniAddrOperTable.setStatus("mandatory")
_AtmIfVptPnniAddrOperEntry_Object = MibTableRow
atmIfVptPnniAddrOperEntry = _AtmIfVptPnniAddrOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 4, 10, 1)
)
atmIfVptPnniAddrOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfVptIndex"),
    (0, "Nortel-Magellan-Passport-AtmPnniMIB", "atmIfVptPnniIndex"),
    (0, "Nortel-Magellan-Passport-AtmPnniMIB", "atmIfVptPnniAddrAddressIndex"),
    (0, "Nortel-Magellan-Passport-AtmPnniMIB", "atmIfVptPnniAddrAddressTypeIndex"),
)
if mibBuilder.loadTexts:
    atmIfVptPnniAddrOperEntry.setStatus("mandatory")


class _AtmIfVptPnniAddrScope_Type(Integer32):
    """Custom type atmIfVptPnniAddrScope based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 104),
    )


_AtmIfVptPnniAddrScope_Type.__name__ = "Integer32"
_AtmIfVptPnniAddrScope_Object = MibTableColumn
atmIfVptPnniAddrScope = _AtmIfVptPnniAddrScope_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 4, 10, 1, 1),
    _AtmIfVptPnniAddrScope_Type()
)
atmIfVptPnniAddrScope.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVptPnniAddrScope.setStatus("mandatory")


class _AtmIfVptPnniAddrReachability_Type(Integer32):
    """Custom type atmIfVptPnniAddrReachability based on Integer32"""
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


_AtmIfVptPnniAddrReachability_Type.__name__ = "Integer32"
_AtmIfVptPnniAddrReachability_Object = MibTableColumn
atmIfVptPnniAddrReachability = _AtmIfVptPnniAddrReachability_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 4, 10, 1, 2),
    _AtmIfVptPnniAddrReachability_Type()
)
atmIfVptPnniAddrReachability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVptPnniAddrReachability.setStatus("mandatory")
_AtmIfVptPnniProvTable_Object = MibTable
atmIfVptPnniProvTable = _AtmIfVptPnniProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 10)
)
if mibBuilder.loadTexts:
    atmIfVptPnniProvTable.setStatus("mandatory")
_AtmIfVptPnniProvEntry_Object = MibTableRow
atmIfVptPnniProvEntry = _AtmIfVptPnniProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 10, 1)
)
atmIfVptPnniProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfVptIndex"),
    (0, "Nortel-Magellan-Passport-AtmPnniMIB", "atmIfVptPnniIndex"),
)
if mibBuilder.loadTexts:
    atmIfVptPnniProvEntry.setStatus("mandatory")


class _AtmIfVptPnniSoftPvcRetryPeriod_Type(Unsigned32):
    """Custom type atmIfVptPnniSoftPvcRetryPeriod based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 999999),
    )


_AtmIfVptPnniSoftPvcRetryPeriod_Type.__name__ = "Unsigned32"
_AtmIfVptPnniSoftPvcRetryPeriod_Object = MibTableColumn
atmIfVptPnniSoftPvcRetryPeriod = _AtmIfVptPnniSoftPvcRetryPeriod_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 10, 1, 1),
    _AtmIfVptPnniSoftPvcRetryPeriod_Type()
)
atmIfVptPnniSoftPvcRetryPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfVptPnniSoftPvcRetryPeriod.setStatus("obsolete")


class _AtmIfVptPnniSoftPvpAndPvcRetryPeriod_Type(Unsigned32):
    """Custom type atmIfVptPnniSoftPvpAndPvcRetryPeriod based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 999999),
    )


_AtmIfVptPnniSoftPvpAndPvcRetryPeriod_Type.__name__ = "Unsigned32"
_AtmIfVptPnniSoftPvpAndPvcRetryPeriod_Object = MibTableColumn
atmIfVptPnniSoftPvpAndPvcRetryPeriod = _AtmIfVptPnniSoftPvpAndPvcRetryPeriod_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 10, 1, 2),
    _AtmIfVptPnniSoftPvpAndPvcRetryPeriod_Type()
)
atmIfVptPnniSoftPvpAndPvcRetryPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfVptPnniSoftPvpAndPvcRetryPeriod.setStatus("mandatory")


class _AtmIfVptPnniSoftPvpAndPvcHoldOffTime_Type(Unsigned32):
    """Custom type atmIfVptPnniSoftPvpAndPvcHoldOffTime based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(50, 20000),
    )


_AtmIfVptPnniSoftPvpAndPvcHoldOffTime_Type.__name__ = "Unsigned32"
_AtmIfVptPnniSoftPvpAndPvcHoldOffTime_Object = MibTableColumn
atmIfVptPnniSoftPvpAndPvcHoldOffTime = _AtmIfVptPnniSoftPvpAndPvcHoldOffTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 10, 1, 5),
    _AtmIfVptPnniSoftPvpAndPvcHoldOffTime_Type()
)
atmIfVptPnniSoftPvpAndPvcHoldOffTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfVptPnniSoftPvpAndPvcHoldOffTime.setStatus("mandatory")
_AtmIfVptPnniAdminWeightsTable_Object = MibTable
atmIfVptPnniAdminWeightsTable = _AtmIfVptPnniAdminWeightsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 11)
)
if mibBuilder.loadTexts:
    atmIfVptPnniAdminWeightsTable.setStatus("mandatory")
_AtmIfVptPnniAdminWeightsEntry_Object = MibTableRow
atmIfVptPnniAdminWeightsEntry = _AtmIfVptPnniAdminWeightsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 11, 1)
)
atmIfVptPnniAdminWeightsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfVptIndex"),
    (0, "Nortel-Magellan-Passport-AtmPnniMIB", "atmIfVptPnniIndex"),
)
if mibBuilder.loadTexts:
    atmIfVptPnniAdminWeightsEntry.setStatus("mandatory")


class _AtmIfVptPnniCbrWeight_Type(Unsigned32):
    """Custom type atmIfVptPnniCbrWeight based on Unsigned32"""
    defaultValue = 5040

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AtmIfVptPnniCbrWeight_Type.__name__ = "Unsigned32"
_AtmIfVptPnniCbrWeight_Object = MibTableColumn
atmIfVptPnniCbrWeight = _AtmIfVptPnniCbrWeight_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 11, 1, 1),
    _AtmIfVptPnniCbrWeight_Type()
)
atmIfVptPnniCbrWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfVptPnniCbrWeight.setStatus("mandatory")


class _AtmIfVptPnniRtVbrWeight_Type(Unsigned32):
    """Custom type atmIfVptPnniRtVbrWeight based on Unsigned32"""
    defaultValue = 5040

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AtmIfVptPnniRtVbrWeight_Type.__name__ = "Unsigned32"
_AtmIfVptPnniRtVbrWeight_Object = MibTableColumn
atmIfVptPnniRtVbrWeight = _AtmIfVptPnniRtVbrWeight_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 11, 1, 2),
    _AtmIfVptPnniRtVbrWeight_Type()
)
atmIfVptPnniRtVbrWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfVptPnniRtVbrWeight.setStatus("mandatory")


class _AtmIfVptPnniNrtVbrWeight_Type(Unsigned32):
    """Custom type atmIfVptPnniNrtVbrWeight based on Unsigned32"""
    defaultValue = 5040

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AtmIfVptPnniNrtVbrWeight_Type.__name__ = "Unsigned32"
_AtmIfVptPnniNrtVbrWeight_Object = MibTableColumn
atmIfVptPnniNrtVbrWeight = _AtmIfVptPnniNrtVbrWeight_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 11, 1, 3),
    _AtmIfVptPnniNrtVbrWeight_Type()
)
atmIfVptPnniNrtVbrWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfVptPnniNrtVbrWeight.setStatus("mandatory")


class _AtmIfVptPnniUbrWeight_Type(Unsigned32):
    """Custom type atmIfVptPnniUbrWeight based on Unsigned32"""
    defaultValue = 5040

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AtmIfVptPnniUbrWeight_Type.__name__ = "Unsigned32"
_AtmIfVptPnniUbrWeight_Object = MibTableColumn
atmIfVptPnniUbrWeight = _AtmIfVptPnniUbrWeight_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 11, 1, 4),
    _AtmIfVptPnniUbrWeight_Type()
)
atmIfVptPnniUbrWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfVptPnniUbrWeight.setStatus("mandatory")
_AtmIfVptPnniAcctOptTable_Object = MibTable
atmIfVptPnniAcctOptTable = _AtmIfVptPnniAcctOptTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 12)
)
if mibBuilder.loadTexts:
    atmIfVptPnniAcctOptTable.setStatus("mandatory")
_AtmIfVptPnniAcctOptEntry_Object = MibTableRow
atmIfVptPnniAcctOptEntry = _AtmIfVptPnniAcctOptEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 12, 1)
)
atmIfVptPnniAcctOptEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfVptIndex"),
    (0, "Nortel-Magellan-Passport-AtmPnniMIB", "atmIfVptPnniIndex"),
)
if mibBuilder.loadTexts:
    atmIfVptPnniAcctOptEntry.setStatus("mandatory")


class _AtmIfVptPnniAccountCollection_Type(OctetString):
    """Custom type atmIfVptPnniAccountCollection based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_AtmIfVptPnniAccountCollection_Type.__name__ = "OctetString"
_AtmIfVptPnniAccountCollection_Object = MibTableColumn
atmIfVptPnniAccountCollection = _AtmIfVptPnniAccountCollection_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 12, 1, 1),
    _AtmIfVptPnniAccountCollection_Type()
)
atmIfVptPnniAccountCollection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfVptPnniAccountCollection.setStatus("mandatory")


class _AtmIfVptPnniAccountConnectionType_Type(Integer32):
    """Custom type atmIfVptPnniAccountConnectionType based on Integer32"""
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


_AtmIfVptPnniAccountConnectionType_Type.__name__ = "Integer32"
_AtmIfVptPnniAccountConnectionType_Object = MibTableColumn
atmIfVptPnniAccountConnectionType = _AtmIfVptPnniAccountConnectionType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 12, 1, 2),
    _AtmIfVptPnniAccountConnectionType_Type()
)
atmIfVptPnniAccountConnectionType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfVptPnniAccountConnectionType.setStatus("mandatory")


class _AtmIfVptPnniAccountClass_Type(Unsigned32):
    """Custom type atmIfVptPnniAccountClass based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AtmIfVptPnniAccountClass_Type.__name__ = "Unsigned32"
_AtmIfVptPnniAccountClass_Object = MibTableColumn
atmIfVptPnniAccountClass = _AtmIfVptPnniAccountClass_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 12, 1, 3),
    _AtmIfVptPnniAccountClass_Type()
)
atmIfVptPnniAccountClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfVptPnniAccountClass.setStatus("mandatory")


class _AtmIfVptPnniServiceExchange_Type(Unsigned32):
    """Custom type atmIfVptPnniServiceExchange based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AtmIfVptPnniServiceExchange_Type.__name__ = "Unsigned32"
_AtmIfVptPnniServiceExchange_Object = MibTableColumn
atmIfVptPnniServiceExchange = _AtmIfVptPnniServiceExchange_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 12, 1, 4),
    _AtmIfVptPnniServiceExchange_Type()
)
atmIfVptPnniServiceExchange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfVptPnniServiceExchange.setStatus("mandatory")
_AtmIfVptPnniOperationalTable_Object = MibTable
atmIfVptPnniOperationalTable = _AtmIfVptPnniOperationalTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 13)
)
if mibBuilder.loadTexts:
    atmIfVptPnniOperationalTable.setStatus("mandatory")
_AtmIfVptPnniOperationalEntry_Object = MibTableRow
atmIfVptPnniOperationalEntry = _AtmIfVptPnniOperationalEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 13, 1)
)
atmIfVptPnniOperationalEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfVptIndex"),
    (0, "Nortel-Magellan-Passport-AtmPnniMIB", "atmIfVptPnniIndex"),
)
if mibBuilder.loadTexts:
    atmIfVptPnniOperationalEntry.setStatus("mandatory")


class _AtmIfVptPnniPortId_Type(Unsigned32):
    """Custom type atmIfVptPnniPortId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AtmIfVptPnniPortId_Type.__name__ = "Unsigned32"
_AtmIfVptPnniPortId_Object = MibTableColumn
atmIfVptPnniPortId = _AtmIfVptPnniPortId_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 13, 1, 1),
    _AtmIfVptPnniPortId_Type()
)
atmIfVptPnniPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVptPnniPortId.setStatus("mandatory")
_AtmIfVptPnniVProvTable_Object = MibTable
atmIfVptPnniVProvTable = _AtmIfVptPnniVProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 14)
)
if mibBuilder.loadTexts:
    atmIfVptPnniVProvTable.setStatus("mandatory")
_AtmIfVptPnniVProvEntry_Object = MibTableRow
atmIfVptPnniVProvEntry = _AtmIfVptPnniVProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 14, 1)
)
atmIfVptPnniVProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfVptIndex"),
    (0, "Nortel-Magellan-Passport-AtmPnniMIB", "atmIfVptPnniIndex"),
)
if mibBuilder.loadTexts:
    atmIfVptPnniVProvEntry.setStatus("mandatory")


class _AtmIfVptPnniVpci_Type(Unsigned32):
    """Custom type atmIfVptPnniVpci based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AtmIfVptPnniVpci_Type.__name__ = "Unsigned32"
_AtmIfVptPnniVpci_Object = MibTableColumn
atmIfVptPnniVpci = _AtmIfVptPnniVpci_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 7, 14, 1, 1),
    _AtmIfVptPnniVpci_Type()
)
atmIfVptPnniVpci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfVptPnniVpci.setStatus("mandatory")
_AtmIfPnni_ObjectIdentity = ObjectIdentity
atmIfPnni = _AtmIfPnni_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96)
)
_AtmIfPnniRowStatusTable_Object = MibTable
atmIfPnniRowStatusTable = _AtmIfPnniRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 1)
)
if mibBuilder.loadTexts:
    atmIfPnniRowStatusTable.setStatus("mandatory")
_AtmIfPnniRowStatusEntry_Object = MibTableRow
atmIfPnniRowStatusEntry = _AtmIfPnniRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 1, 1)
)
atmIfPnniRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmPnniMIB", "atmIfPnniIndex"),
)
if mibBuilder.loadTexts:
    atmIfPnniRowStatusEntry.setStatus("mandatory")
_AtmIfPnniRowStatus_Type = RowStatus
_AtmIfPnniRowStatus_Object = MibTableColumn
atmIfPnniRowStatus = _AtmIfPnniRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 1, 1, 1),
    _AtmIfPnniRowStatus_Type()
)
atmIfPnniRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfPnniRowStatus.setStatus("mandatory")
_AtmIfPnniComponentName_Type = DisplayString
_AtmIfPnniComponentName_Object = MibTableColumn
atmIfPnniComponentName = _AtmIfPnniComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 1, 1, 2),
    _AtmIfPnniComponentName_Type()
)
atmIfPnniComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfPnniComponentName.setStatus("mandatory")
_AtmIfPnniStorageType_Type = StorageType
_AtmIfPnniStorageType_Object = MibTableColumn
atmIfPnniStorageType = _AtmIfPnniStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 1, 1, 4),
    _AtmIfPnniStorageType_Type()
)
atmIfPnniStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfPnniStorageType.setStatus("mandatory")
_AtmIfPnniIndex_Type = NonReplicated
_AtmIfPnniIndex_Object = MibTableColumn
atmIfPnniIndex = _AtmIfPnniIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 1, 1, 10),
    _AtmIfPnniIndex_Type()
)
atmIfPnniIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmIfPnniIndex.setStatus("mandatory")
_AtmIfPnniSig_ObjectIdentity = ObjectIdentity
atmIfPnniSig = _AtmIfPnniSig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 2)
)
_AtmIfPnniSigRowStatusTable_Object = MibTable
atmIfPnniSigRowStatusTable = _AtmIfPnniSigRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 2, 1)
)
if mibBuilder.loadTexts:
    atmIfPnniSigRowStatusTable.setStatus("mandatory")
_AtmIfPnniSigRowStatusEntry_Object = MibTableRow
atmIfPnniSigRowStatusEntry = _AtmIfPnniSigRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 2, 1, 1)
)
atmIfPnniSigRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmPnniMIB", "atmIfPnniIndex"),
    (0, "Nortel-Magellan-Passport-AtmPnniMIB", "atmIfPnniSigIndex"),
)
if mibBuilder.loadTexts:
    atmIfPnniSigRowStatusEntry.setStatus("mandatory")
_AtmIfPnniSigRowStatus_Type = RowStatus
_AtmIfPnniSigRowStatus_Object = MibTableColumn
atmIfPnniSigRowStatus = _AtmIfPnniSigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 2, 1, 1, 1),
    _AtmIfPnniSigRowStatus_Type()
)
atmIfPnniSigRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfPnniSigRowStatus.setStatus("mandatory")
_AtmIfPnniSigComponentName_Type = DisplayString
_AtmIfPnniSigComponentName_Object = MibTableColumn
atmIfPnniSigComponentName = _AtmIfPnniSigComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 2, 1, 1, 2),
    _AtmIfPnniSigComponentName_Type()
)
atmIfPnniSigComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfPnniSigComponentName.setStatus("mandatory")
_AtmIfPnniSigStorageType_Type = StorageType
_AtmIfPnniSigStorageType_Object = MibTableColumn
atmIfPnniSigStorageType = _AtmIfPnniSigStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 2, 1, 1, 4),
    _AtmIfPnniSigStorageType_Type()
)
atmIfPnniSigStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfPnniSigStorageType.setStatus("mandatory")
_AtmIfPnniSigIndex_Type = NonReplicated
_AtmIfPnniSigIndex_Object = MibTableColumn
atmIfPnniSigIndex = _AtmIfPnniSigIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 2, 1, 1, 10),
    _AtmIfPnniSigIndex_Type()
)
atmIfPnniSigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmIfPnniSigIndex.setStatus("mandatory")
_AtmIfPnniSigVcd_ObjectIdentity = ObjectIdentity
atmIfPnniSigVcd = _AtmIfPnniSigVcd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 2, 2)
)
_AtmIfPnniSigVcdRowStatusTable_Object = MibTable
atmIfPnniSigVcdRowStatusTable = _AtmIfPnniSigVcdRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 2, 2, 1)
)
if mibBuilder.loadTexts:
    atmIfPnniSigVcdRowStatusTable.setStatus("mandatory")
_AtmIfPnniSigVcdRowStatusEntry_Object = MibTableRow
atmIfPnniSigVcdRowStatusEntry = _AtmIfPnniSigVcdRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 2, 2, 1, 1)
)
atmIfPnniSigVcdRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmPnniMIB", "atmIfPnniIndex"),
    (0, "Nortel-Magellan-Passport-AtmPnniMIB", "atmIfPnniSigIndex"),
    (0, "Nortel-Magellan-Passport-AtmPnniMIB", "atmIfPnniSigVcdIndex"),
)
if mibBuilder.loadTexts:
    atmIfPnniSigVcdRowStatusEntry.setStatus("mandatory")
_AtmIfPnniSigVcdRowStatus_Type = RowStatus
_AtmIfPnniSigVcdRowStatus_Object = MibTableColumn
atmIfPnniSigVcdRowStatus = _AtmIfPnniSigVcdRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 2, 2, 1, 1, 1),
    _AtmIfPnniSigVcdRowStatus_Type()
)
atmIfPnniSigVcdRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfPnniSigVcdRowStatus.setStatus("mandatory")
_AtmIfPnniSigVcdComponentName_Type = DisplayString
_AtmIfPnniSigVcdComponentName_Object = MibTableColumn
atmIfPnniSigVcdComponentName = _AtmIfPnniSigVcdComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 2, 2, 1, 1, 2),
    _AtmIfPnniSigVcdComponentName_Type()
)
atmIfPnniSigVcdComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfPnniSigVcdComponentName.setStatus("mandatory")
_AtmIfPnniSigVcdStorageType_Type = StorageType
_AtmIfPnniSigVcdStorageType_Object = MibTableColumn
atmIfPnniSigVcdStorageType = _AtmIfPnniSigVcdStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 2, 2, 1, 1, 4),
    _AtmIfPnniSigVcdStorageType_Type()
)
atmIfPnniSigVcdStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfPnniSigVcdStorageType.setStatus("mandatory")
_AtmIfPnniSigVcdIndex_Type = NonReplicated
_AtmIfPnniSigVcdIndex_Object = MibTableColumn
atmIfPnniSigVcdIndex = _AtmIfPnniSigVcdIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 2, 2, 1, 1, 10),
    _AtmIfPnniSigVcdIndex_Type()
)
atmIfPnniSigVcdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmIfPnniSigVcdIndex.setStatus("mandatory")
_AtmIfPnniSigVcdProvTable_Object = MibTable
atmIfPnniSigVcdProvTable = _AtmIfPnniSigVcdProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 2, 2, 10)
)
if mibBuilder.loadTexts:
    atmIfPnniSigVcdProvTable.setStatus("mandatory")
_AtmIfPnniSigVcdProvEntry_Object = MibTableRow
atmIfPnniSigVcdProvEntry = _AtmIfPnniSigVcdProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 2, 2, 10, 1)
)
atmIfPnniSigVcdProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmPnniMIB", "atmIfPnniIndex"),
    (0, "Nortel-Magellan-Passport-AtmPnniMIB", "atmIfPnniSigIndex"),
    (0, "Nortel-Magellan-Passport-AtmPnniMIB", "atmIfPnniSigVcdIndex"),
)
if mibBuilder.loadTexts:
    atmIfPnniSigVcdProvEntry.setStatus("mandatory")


class _AtmIfPnniSigVcdTrafficDescType_Type(Integer32):
    """Custom type atmIfPnniSigVcdTrafficDescType based on Integer32"""
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


_AtmIfPnniSigVcdTrafficDescType_Type.__name__ = "Integer32"
_AtmIfPnniSigVcdTrafficDescType_Object = MibTableColumn
atmIfPnniSigVcdTrafficDescType = _AtmIfPnniSigVcdTrafficDescType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 2, 2, 10, 1, 1),
    _AtmIfPnniSigVcdTrafficDescType_Type()
)
atmIfPnniSigVcdTrafficDescType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfPnniSigVcdTrafficDescType.setStatus("mandatory")


class _AtmIfPnniSigVcdAtmServiceCategory_Type(Integer32):
    """Custom type atmIfPnniSigVcdAtmServiceCategory based on Integer32"""
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


_AtmIfPnniSigVcdAtmServiceCategory_Type.__name__ = "Integer32"
_AtmIfPnniSigVcdAtmServiceCategory_Object = MibTableColumn
atmIfPnniSigVcdAtmServiceCategory = _AtmIfPnniSigVcdAtmServiceCategory_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 2, 2, 10, 1, 3),
    _AtmIfPnniSigVcdAtmServiceCategory_Type()
)
atmIfPnniSigVcdAtmServiceCategory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfPnniSigVcdAtmServiceCategory.setStatus("mandatory")


class _AtmIfPnniSigVcdQosClass_Type(Integer32):
    """Custom type atmIfPnniSigVcdQosClass based on Integer32"""
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


_AtmIfPnniSigVcdQosClass_Type.__name__ = "Integer32"
_AtmIfPnniSigVcdQosClass_Object = MibTableColumn
atmIfPnniSigVcdQosClass = _AtmIfPnniSigVcdQosClass_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 2, 2, 10, 1, 21),
    _AtmIfPnniSigVcdQosClass_Type()
)
atmIfPnniSigVcdQosClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfPnniSigVcdQosClass.setStatus("mandatory")


class _AtmIfPnniSigVcdTrafficShaping_Type(Integer32):
    """Custom type atmIfPnniSigVcdTrafficShaping based on Integer32"""
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


_AtmIfPnniSigVcdTrafficShaping_Type.__name__ = "Integer32"
_AtmIfPnniSigVcdTrafficShaping_Object = MibTableColumn
atmIfPnniSigVcdTrafficShaping = _AtmIfPnniSigVcdTrafficShaping_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 2, 2, 10, 1, 50),
    _AtmIfPnniSigVcdTrafficShaping_Type()
)
atmIfPnniSigVcdTrafficShaping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfPnniSigVcdTrafficShaping.setStatus("mandatory")


class _AtmIfPnniSigVcdUnshapedTransmitQueueing_Type(Integer32):
    """Custom type atmIfPnniSigVcdUnshapedTransmitQueueing based on Integer32"""
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


_AtmIfPnniSigVcdUnshapedTransmitQueueing_Type.__name__ = "Integer32"
_AtmIfPnniSigVcdUnshapedTransmitQueueing_Object = MibTableColumn
atmIfPnniSigVcdUnshapedTransmitQueueing = _AtmIfPnniSigVcdUnshapedTransmitQueueing_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 2, 2, 10, 1, 60),
    _AtmIfPnniSigVcdUnshapedTransmitQueueing_Type()
)
atmIfPnniSigVcdUnshapedTransmitQueueing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfPnniSigVcdUnshapedTransmitQueueing.setStatus("mandatory")


class _AtmIfPnniSigVcdUsageParameterControl_Type(Integer32):
    """Custom type atmIfPnniSigVcdUsageParameterControl based on Integer32"""
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


_AtmIfPnniSigVcdUsageParameterControl_Type.__name__ = "Integer32"
_AtmIfPnniSigVcdUsageParameterControl_Object = MibTableColumn
atmIfPnniSigVcdUsageParameterControl = _AtmIfPnniSigVcdUsageParameterControl_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 2, 2, 10, 1, 70),
    _AtmIfPnniSigVcdUsageParameterControl_Type()
)
atmIfPnniSigVcdUsageParameterControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfPnniSigVcdUsageParameterControl.setStatus("mandatory")
_AtmIfPnniSigVcdTdpTable_Object = MibTable
atmIfPnniSigVcdTdpTable = _AtmIfPnniSigVcdTdpTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 2, 2, 387)
)
if mibBuilder.loadTexts:
    atmIfPnniSigVcdTdpTable.setStatus("mandatory")
_AtmIfPnniSigVcdTdpEntry_Object = MibTableRow
atmIfPnniSigVcdTdpEntry = _AtmIfPnniSigVcdTdpEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 2, 2, 387, 1)
)
atmIfPnniSigVcdTdpEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmPnniMIB", "atmIfPnniIndex"),
    (0, "Nortel-Magellan-Passport-AtmPnniMIB", "atmIfPnniSigIndex"),
    (0, "Nortel-Magellan-Passport-AtmPnniMIB", "atmIfPnniSigVcdIndex"),
    (0, "Nortel-Magellan-Passport-AtmPnniMIB", "atmIfPnniSigVcdTdpIndex"),
)
if mibBuilder.loadTexts:
    atmIfPnniSigVcdTdpEntry.setStatus("mandatory")


class _AtmIfPnniSigVcdTdpIndex_Type(Integer32):
    """Custom type atmIfPnniSigVcdTdpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_AtmIfPnniSigVcdTdpIndex_Type.__name__ = "Integer32"
_AtmIfPnniSigVcdTdpIndex_Object = MibTableColumn
atmIfPnniSigVcdTdpIndex = _AtmIfPnniSigVcdTdpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 2, 2, 387, 1, 1),
    _AtmIfPnniSigVcdTdpIndex_Type()
)
atmIfPnniSigVcdTdpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmIfPnniSigVcdTdpIndex.setStatus("mandatory")


class _AtmIfPnniSigVcdTdpValue_Type(Unsigned32):
    """Custom type atmIfPnniSigVcdTdpValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AtmIfPnniSigVcdTdpValue_Type.__name__ = "Unsigned32"
_AtmIfPnniSigVcdTdpValue_Object = MibTableColumn
atmIfPnniSigVcdTdpValue = _AtmIfPnniSigVcdTdpValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 2, 2, 387, 1, 2),
    _AtmIfPnniSigVcdTdpValue_Type()
)
atmIfPnniSigVcdTdpValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfPnniSigVcdTdpValue.setStatus("mandatory")
_AtmIfPnniSigProvTable_Object = MibTable
atmIfPnniSigProvTable = _AtmIfPnniSigProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 2, 10)
)
if mibBuilder.loadTexts:
    atmIfPnniSigProvTable.setStatus("mandatory")
_AtmIfPnniSigProvEntry_Object = MibTableRow
atmIfPnniSigProvEntry = _AtmIfPnniSigProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 2, 10, 1)
)
atmIfPnniSigProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmPnniMIB", "atmIfPnniIndex"),
    (0, "Nortel-Magellan-Passport-AtmPnniMIB", "atmIfPnniSigIndex"),
)
if mibBuilder.loadTexts:
    atmIfPnniSigProvEntry.setStatus("mandatory")


class _AtmIfPnniSigVci_Type(Unsigned32):
    """Custom type atmIfPnniSigVci based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AtmIfPnniSigVci_Type.__name__ = "Unsigned32"
_AtmIfPnniSigVci_Object = MibTableColumn
atmIfPnniSigVci = _AtmIfPnniSigVci_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 2, 10, 1, 1),
    _AtmIfPnniSigVci_Type()
)
atmIfPnniSigVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfPnniSigVci.setStatus("mandatory")


class _AtmIfPnniSigAddressConversion_Type(Integer32):
    """Custom type atmIfPnniSigAddressConversion based on Integer32"""
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


_AtmIfPnniSigAddressConversion_Type.__name__ = "Integer32"
_AtmIfPnniSigAddressConversion_Object = MibTableColumn
atmIfPnniSigAddressConversion = _AtmIfPnniSigAddressConversion_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 2, 10, 1, 2),
    _AtmIfPnniSigAddressConversion_Type()
)
atmIfPnniSigAddressConversion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfPnniSigAddressConversion.setStatus("mandatory")
_AtmIfPnniSigStateTable_Object = MibTable
atmIfPnniSigStateTable = _AtmIfPnniSigStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 2, 11)
)
if mibBuilder.loadTexts:
    atmIfPnniSigStateTable.setStatus("mandatory")
_AtmIfPnniSigStateEntry_Object = MibTableRow
atmIfPnniSigStateEntry = _AtmIfPnniSigStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 2, 11, 1)
)
atmIfPnniSigStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmPnniMIB", "atmIfPnniIndex"),
    (0, "Nortel-Magellan-Passport-AtmPnniMIB", "atmIfPnniSigIndex"),
)
if mibBuilder.loadTexts:
    atmIfPnniSigStateEntry.setStatus("mandatory")


class _AtmIfPnniSigAdminState_Type(Integer32):
    """Custom type atmIfPnniSigAdminState based on Integer32"""
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


_AtmIfPnniSigAdminState_Type.__name__ = "Integer32"
_AtmIfPnniSigAdminState_Object = MibTableColumn
atmIfPnniSigAdminState = _AtmIfPnniSigAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 2, 11, 1, 1),
    _AtmIfPnniSigAdminState_Type()
)
atmIfPnniSigAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfPnniSigAdminState.setStatus("mandatory")


class _AtmIfPnniSigOperationalState_Type(Integer32):
    """Custom type atmIfPnniSigOperationalState based on Integer32"""
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


_AtmIfPnniSigOperationalState_Type.__name__ = "Integer32"
_AtmIfPnniSigOperationalState_Object = MibTableColumn
atmIfPnniSigOperationalState = _AtmIfPnniSigOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 2, 11, 1, 2),
    _AtmIfPnniSigOperationalState_Type()
)
atmIfPnniSigOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfPnniSigOperationalState.setStatus("mandatory")


class _AtmIfPnniSigUsageState_Type(Integer32):
    """Custom type atmIfPnniSigUsageState based on Integer32"""
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


_AtmIfPnniSigUsageState_Type.__name__ = "Integer32"
_AtmIfPnniSigUsageState_Object = MibTableColumn
atmIfPnniSigUsageState = _AtmIfPnniSigUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 2, 11, 1, 3),
    _AtmIfPnniSigUsageState_Type()
)
atmIfPnniSigUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfPnniSigUsageState.setStatus("mandatory")
_AtmIfPnniSigOperTable_Object = MibTable
atmIfPnniSigOperTable = _AtmIfPnniSigOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 2, 12)
)
if mibBuilder.loadTexts:
    atmIfPnniSigOperTable.setStatus("mandatory")
_AtmIfPnniSigOperEntry_Object = MibTableRow
atmIfPnniSigOperEntry = _AtmIfPnniSigOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 2, 12, 1)
)
atmIfPnniSigOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmPnniMIB", "atmIfPnniIndex"),
    (0, "Nortel-Magellan-Passport-AtmPnniMIB", "atmIfPnniSigIndex"),
)
if mibBuilder.loadTexts:
    atmIfPnniSigOperEntry.setStatus("mandatory")


class _AtmIfPnniSigLastTxCauseCode_Type(Unsigned32):
    """Custom type atmIfPnniSigLastTxCauseCode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AtmIfPnniSigLastTxCauseCode_Type.__name__ = "Unsigned32"
_AtmIfPnniSigLastTxCauseCode_Object = MibTableColumn
atmIfPnniSigLastTxCauseCode = _AtmIfPnniSigLastTxCauseCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 2, 12, 1, 1),
    _AtmIfPnniSigLastTxCauseCode_Type()
)
atmIfPnniSigLastTxCauseCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfPnniSigLastTxCauseCode.setStatus("mandatory")


class _AtmIfPnniSigLastTxDiagCode_Type(Hex):
    """Custom type atmIfPnniSigLastTxDiagCode based on Hex"""
    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AtmIfPnniSigLastTxDiagCode_Type.__name__ = "Hex"
_AtmIfPnniSigLastTxDiagCode_Object = MibTableColumn
atmIfPnniSigLastTxDiagCode = _AtmIfPnniSigLastTxDiagCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 2, 12, 1, 2),
    _AtmIfPnniSigLastTxDiagCode_Type()
)
atmIfPnniSigLastTxDiagCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfPnniSigLastTxDiagCode.setStatus("mandatory")


class _AtmIfPnniSigLastRxCauseCode_Type(Unsigned32):
    """Custom type atmIfPnniSigLastRxCauseCode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AtmIfPnniSigLastRxCauseCode_Type.__name__ = "Unsigned32"
_AtmIfPnniSigLastRxCauseCode_Object = MibTableColumn
atmIfPnniSigLastRxCauseCode = _AtmIfPnniSigLastRxCauseCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 2, 12, 1, 3),
    _AtmIfPnniSigLastRxCauseCode_Type()
)
atmIfPnniSigLastRxCauseCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfPnniSigLastRxCauseCode.setStatus("mandatory")


class _AtmIfPnniSigLastRxDiagCode_Type(Hex):
    """Custom type atmIfPnniSigLastRxDiagCode based on Hex"""
    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AtmIfPnniSigLastRxDiagCode_Type.__name__ = "Hex"
_AtmIfPnniSigLastRxDiagCode_Object = MibTableColumn
atmIfPnniSigLastRxDiagCode = _AtmIfPnniSigLastRxDiagCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 2, 12, 1, 4),
    _AtmIfPnniSigLastRxDiagCode_Type()
)
atmIfPnniSigLastRxDiagCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfPnniSigLastRxDiagCode.setStatus("mandatory")
_AtmIfPnniSigStatsTable_Object = MibTable
atmIfPnniSigStatsTable = _AtmIfPnniSigStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 2, 13)
)
if mibBuilder.loadTexts:
    atmIfPnniSigStatsTable.setStatus("mandatory")
_AtmIfPnniSigStatsEntry_Object = MibTableRow
atmIfPnniSigStatsEntry = _AtmIfPnniSigStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 2, 13, 1)
)
atmIfPnniSigStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmPnniMIB", "atmIfPnniIndex"),
    (0, "Nortel-Magellan-Passport-AtmPnniMIB", "atmIfPnniSigIndex"),
)
if mibBuilder.loadTexts:
    atmIfPnniSigStatsEntry.setStatus("mandatory")
_AtmIfPnniSigCurrentConnections_Type = Counter32
_AtmIfPnniSigCurrentConnections_Object = MibTableColumn
atmIfPnniSigCurrentConnections = _AtmIfPnniSigCurrentConnections_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 2, 13, 1, 1),
    _AtmIfPnniSigCurrentConnections_Type()
)
atmIfPnniSigCurrentConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfPnniSigCurrentConnections.setStatus("obsolete")


class _AtmIfPnniSigPeakConnections_Type(Gauge32):
    """Custom type atmIfPnniSigPeakConnections based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AtmIfPnniSigPeakConnections_Type.__name__ = "Gauge32"
_AtmIfPnniSigPeakConnections_Object = MibTableColumn
atmIfPnniSigPeakConnections = _AtmIfPnniSigPeakConnections_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 2, 13, 1, 2),
    _AtmIfPnniSigPeakConnections_Type()
)
atmIfPnniSigPeakConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfPnniSigPeakConnections.setStatus("mandatory")
_AtmIfPnniSigSuccessfulConnections_Type = Counter32
_AtmIfPnniSigSuccessfulConnections_Object = MibTableColumn
atmIfPnniSigSuccessfulConnections = _AtmIfPnniSigSuccessfulConnections_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 2, 13, 1, 3),
    _AtmIfPnniSigSuccessfulConnections_Type()
)
atmIfPnniSigSuccessfulConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfPnniSigSuccessfulConnections.setStatus("mandatory")
_AtmIfPnniSigFailedConnections_Type = Counter32
_AtmIfPnniSigFailedConnections_Object = MibTableColumn
atmIfPnniSigFailedConnections = _AtmIfPnniSigFailedConnections_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 2, 13, 1, 4),
    _AtmIfPnniSigFailedConnections_Type()
)
atmIfPnniSigFailedConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfPnniSigFailedConnections.setStatus("mandatory")
_AtmIfPnniSigTxPdus_Type = Counter32
_AtmIfPnniSigTxPdus_Object = MibTableColumn
atmIfPnniSigTxPdus = _AtmIfPnniSigTxPdus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 2, 13, 1, 5),
    _AtmIfPnniSigTxPdus_Type()
)
atmIfPnniSigTxPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfPnniSigTxPdus.setStatus("mandatory")
_AtmIfPnniSigRxPdus_Type = Counter32
_AtmIfPnniSigRxPdus_Object = MibTableColumn
atmIfPnniSigRxPdus = _AtmIfPnniSigRxPdus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 2, 13, 1, 6),
    _AtmIfPnniSigRxPdus_Type()
)
atmIfPnniSigRxPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfPnniSigRxPdus.setStatus("mandatory")


class _AtmIfPnniSigCurrentPmpConnections_Type(Gauge32):
    """Custom type atmIfPnniSigCurrentPmpConnections based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AtmIfPnniSigCurrentPmpConnections_Type.__name__ = "Gauge32"
_AtmIfPnniSigCurrentPmpConnections_Object = MibTableColumn
atmIfPnniSigCurrentPmpConnections = _AtmIfPnniSigCurrentPmpConnections_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 2, 13, 1, 7),
    _AtmIfPnniSigCurrentPmpConnections_Type()
)
atmIfPnniSigCurrentPmpConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfPnniSigCurrentPmpConnections.setStatus("mandatory")


class _AtmIfPnniSigPeakPmpConnections_Type(Gauge32):
    """Custom type atmIfPnniSigPeakPmpConnections based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AtmIfPnniSigPeakPmpConnections_Type.__name__ = "Gauge32"
_AtmIfPnniSigPeakPmpConnections_Object = MibTableColumn
atmIfPnniSigPeakPmpConnections = _AtmIfPnniSigPeakPmpConnections_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 2, 13, 1, 8),
    _AtmIfPnniSigPeakPmpConnections_Type()
)
atmIfPnniSigPeakPmpConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfPnniSigPeakPmpConnections.setStatus("mandatory")
_AtmIfPnniSigSuccessfulPmpConnections_Type = Counter32
_AtmIfPnniSigSuccessfulPmpConnections_Object = MibTableColumn
atmIfPnniSigSuccessfulPmpConnections = _AtmIfPnniSigSuccessfulPmpConnections_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 2, 13, 1, 9),
    _AtmIfPnniSigSuccessfulPmpConnections_Type()
)
atmIfPnniSigSuccessfulPmpConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfPnniSigSuccessfulPmpConnections.setStatus("mandatory")
_AtmIfPnniSigFailedPmpConnections_Type = Counter32
_AtmIfPnniSigFailedPmpConnections_Object = MibTableColumn
atmIfPnniSigFailedPmpConnections = _AtmIfPnniSigFailedPmpConnections_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 2, 13, 1, 10),
    _AtmIfPnniSigFailedPmpConnections_Type()
)
atmIfPnniSigFailedPmpConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfPnniSigFailedPmpConnections.setStatus("mandatory")


class _AtmIfPnniSigNewCurrentConnections_Type(Gauge32):
    """Custom type atmIfPnniSigNewCurrentConnections based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AtmIfPnniSigNewCurrentConnections_Type.__name__ = "Gauge32"
_AtmIfPnniSigNewCurrentConnections_Object = MibTableColumn
atmIfPnniSigNewCurrentConnections = _AtmIfPnniSigNewCurrentConnections_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 2, 13, 1, 11),
    _AtmIfPnniSigNewCurrentConnections_Type()
)
atmIfPnniSigNewCurrentConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfPnniSigNewCurrentConnections.setStatus("mandatory")
_AtmIfPnniRcc_ObjectIdentity = ObjectIdentity
atmIfPnniRcc = _AtmIfPnniRcc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 3)
)
_AtmIfPnniRccRowStatusTable_Object = MibTable
atmIfPnniRccRowStatusTable = _AtmIfPnniRccRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 3, 1)
)
if mibBuilder.loadTexts:
    atmIfPnniRccRowStatusTable.setStatus("mandatory")
_AtmIfPnniRccRowStatusEntry_Object = MibTableRow
atmIfPnniRccRowStatusEntry = _AtmIfPnniRccRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 3, 1, 1)
)
atmIfPnniRccRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmPnniMIB", "atmIfPnniIndex"),
    (0, "Nortel-Magellan-Passport-AtmPnniMIB", "atmIfPnniRccIndex"),
)
if mibBuilder.loadTexts:
    atmIfPnniRccRowStatusEntry.setStatus("mandatory")
_AtmIfPnniRccRowStatus_Type = RowStatus
_AtmIfPnniRccRowStatus_Object = MibTableColumn
atmIfPnniRccRowStatus = _AtmIfPnniRccRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 3, 1, 1, 1),
    _AtmIfPnniRccRowStatus_Type()
)
atmIfPnniRccRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfPnniRccRowStatus.setStatus("mandatory")
_AtmIfPnniRccComponentName_Type = DisplayString
_AtmIfPnniRccComponentName_Object = MibTableColumn
atmIfPnniRccComponentName = _AtmIfPnniRccComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 3, 1, 1, 2),
    _AtmIfPnniRccComponentName_Type()
)
atmIfPnniRccComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfPnniRccComponentName.setStatus("mandatory")
_AtmIfPnniRccStorageType_Type = StorageType
_AtmIfPnniRccStorageType_Object = MibTableColumn
atmIfPnniRccStorageType = _AtmIfPnniRccStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 3, 1, 1, 4),
    _AtmIfPnniRccStorageType_Type()
)
atmIfPnniRccStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfPnniRccStorageType.setStatus("mandatory")
_AtmIfPnniRccIndex_Type = NonReplicated
_AtmIfPnniRccIndex_Object = MibTableColumn
atmIfPnniRccIndex = _AtmIfPnniRccIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 3, 1, 1, 10),
    _AtmIfPnniRccIndex_Type()
)
atmIfPnniRccIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmIfPnniRccIndex.setStatus("mandatory")
_AtmIfPnniRccVcd_ObjectIdentity = ObjectIdentity
atmIfPnniRccVcd = _AtmIfPnniRccVcd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 3, 2)
)
_AtmIfPnniRccVcdRowStatusTable_Object = MibTable
atmIfPnniRccVcdRowStatusTable = _AtmIfPnniRccVcdRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 3, 2, 1)
)
if mibBuilder.loadTexts:
    atmIfPnniRccVcdRowStatusTable.setStatus("mandatory")
_AtmIfPnniRccVcdRowStatusEntry_Object = MibTableRow
atmIfPnniRccVcdRowStatusEntry = _AtmIfPnniRccVcdRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 3, 2, 1, 1)
)
atmIfPnniRccVcdRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmPnniMIB", "atmIfPnniIndex"),
    (0, "Nortel-Magellan-Passport-AtmPnniMIB", "atmIfPnniRccIndex"),
    (0, "Nortel-Magellan-Passport-AtmPnniMIB", "atmIfPnniRccVcdIndex"),
)
if mibBuilder.loadTexts:
    atmIfPnniRccVcdRowStatusEntry.setStatus("mandatory")
_AtmIfPnniRccVcdRowStatus_Type = RowStatus
_AtmIfPnniRccVcdRowStatus_Object = MibTableColumn
atmIfPnniRccVcdRowStatus = _AtmIfPnniRccVcdRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 3, 2, 1, 1, 1),
    _AtmIfPnniRccVcdRowStatus_Type()
)
atmIfPnniRccVcdRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfPnniRccVcdRowStatus.setStatus("mandatory")
_AtmIfPnniRccVcdComponentName_Type = DisplayString
_AtmIfPnniRccVcdComponentName_Object = MibTableColumn
atmIfPnniRccVcdComponentName = _AtmIfPnniRccVcdComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 3, 2, 1, 1, 2),
    _AtmIfPnniRccVcdComponentName_Type()
)
atmIfPnniRccVcdComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfPnniRccVcdComponentName.setStatus("mandatory")
_AtmIfPnniRccVcdStorageType_Type = StorageType
_AtmIfPnniRccVcdStorageType_Object = MibTableColumn
atmIfPnniRccVcdStorageType = _AtmIfPnniRccVcdStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 3, 2, 1, 1, 4),
    _AtmIfPnniRccVcdStorageType_Type()
)
atmIfPnniRccVcdStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfPnniRccVcdStorageType.setStatus("mandatory")
_AtmIfPnniRccVcdIndex_Type = NonReplicated
_AtmIfPnniRccVcdIndex_Object = MibTableColumn
atmIfPnniRccVcdIndex = _AtmIfPnniRccVcdIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 3, 2, 1, 1, 10),
    _AtmIfPnniRccVcdIndex_Type()
)
atmIfPnniRccVcdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmIfPnniRccVcdIndex.setStatus("mandatory")
_AtmIfPnniRccVcdProvTable_Object = MibTable
atmIfPnniRccVcdProvTable = _AtmIfPnniRccVcdProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 3, 2, 10)
)
if mibBuilder.loadTexts:
    atmIfPnniRccVcdProvTable.setStatus("mandatory")
_AtmIfPnniRccVcdProvEntry_Object = MibTableRow
atmIfPnniRccVcdProvEntry = _AtmIfPnniRccVcdProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 3, 2, 10, 1)
)
atmIfPnniRccVcdProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmPnniMIB", "atmIfPnniIndex"),
    (0, "Nortel-Magellan-Passport-AtmPnniMIB", "atmIfPnniRccIndex"),
    (0, "Nortel-Magellan-Passport-AtmPnniMIB", "atmIfPnniRccVcdIndex"),
)
if mibBuilder.loadTexts:
    atmIfPnniRccVcdProvEntry.setStatus("mandatory")


class _AtmIfPnniRccVcdTrafficDescType_Type(Integer32):
    """Custom type atmIfPnniRccVcdTrafficDescType based on Integer32"""
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


_AtmIfPnniRccVcdTrafficDescType_Type.__name__ = "Integer32"
_AtmIfPnniRccVcdTrafficDescType_Object = MibTableColumn
atmIfPnniRccVcdTrafficDescType = _AtmIfPnniRccVcdTrafficDescType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 3, 2, 10, 1, 1),
    _AtmIfPnniRccVcdTrafficDescType_Type()
)
atmIfPnniRccVcdTrafficDescType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfPnniRccVcdTrafficDescType.setStatus("mandatory")


class _AtmIfPnniRccVcdAtmServiceCategory_Type(Integer32):
    """Custom type atmIfPnniRccVcdAtmServiceCategory based on Integer32"""
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


_AtmIfPnniRccVcdAtmServiceCategory_Type.__name__ = "Integer32"
_AtmIfPnniRccVcdAtmServiceCategory_Object = MibTableColumn
atmIfPnniRccVcdAtmServiceCategory = _AtmIfPnniRccVcdAtmServiceCategory_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 3, 2, 10, 1, 3),
    _AtmIfPnniRccVcdAtmServiceCategory_Type()
)
atmIfPnniRccVcdAtmServiceCategory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfPnniRccVcdAtmServiceCategory.setStatus("mandatory")


class _AtmIfPnniRccVcdQosClass_Type(Integer32):
    """Custom type atmIfPnniRccVcdQosClass based on Integer32"""
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


_AtmIfPnniRccVcdQosClass_Type.__name__ = "Integer32"
_AtmIfPnniRccVcdQosClass_Object = MibTableColumn
atmIfPnniRccVcdQosClass = _AtmIfPnniRccVcdQosClass_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 3, 2, 10, 1, 21),
    _AtmIfPnniRccVcdQosClass_Type()
)
atmIfPnniRccVcdQosClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfPnniRccVcdQosClass.setStatus("mandatory")


class _AtmIfPnniRccVcdTrafficShaping_Type(Integer32):
    """Custom type atmIfPnniRccVcdTrafficShaping based on Integer32"""
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


_AtmIfPnniRccVcdTrafficShaping_Type.__name__ = "Integer32"
_AtmIfPnniRccVcdTrafficShaping_Object = MibTableColumn
atmIfPnniRccVcdTrafficShaping = _AtmIfPnniRccVcdTrafficShaping_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 3, 2, 10, 1, 50),
    _AtmIfPnniRccVcdTrafficShaping_Type()
)
atmIfPnniRccVcdTrafficShaping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfPnniRccVcdTrafficShaping.setStatus("mandatory")


class _AtmIfPnniRccVcdUnshapedTransmitQueueing_Type(Integer32):
    """Custom type atmIfPnniRccVcdUnshapedTransmitQueueing based on Integer32"""
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


_AtmIfPnniRccVcdUnshapedTransmitQueueing_Type.__name__ = "Integer32"
_AtmIfPnniRccVcdUnshapedTransmitQueueing_Object = MibTableColumn
atmIfPnniRccVcdUnshapedTransmitQueueing = _AtmIfPnniRccVcdUnshapedTransmitQueueing_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 3, 2, 10, 1, 60),
    _AtmIfPnniRccVcdUnshapedTransmitQueueing_Type()
)
atmIfPnniRccVcdUnshapedTransmitQueueing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfPnniRccVcdUnshapedTransmitQueueing.setStatus("mandatory")


class _AtmIfPnniRccVcdUsageParameterControl_Type(Integer32):
    """Custom type atmIfPnniRccVcdUsageParameterControl based on Integer32"""
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


_AtmIfPnniRccVcdUsageParameterControl_Type.__name__ = "Integer32"
_AtmIfPnniRccVcdUsageParameterControl_Object = MibTableColumn
atmIfPnniRccVcdUsageParameterControl = _AtmIfPnniRccVcdUsageParameterControl_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 3, 2, 10, 1, 70),
    _AtmIfPnniRccVcdUsageParameterControl_Type()
)
atmIfPnniRccVcdUsageParameterControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfPnniRccVcdUsageParameterControl.setStatus("mandatory")
_AtmIfPnniRccVcdTdpTable_Object = MibTable
atmIfPnniRccVcdTdpTable = _AtmIfPnniRccVcdTdpTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 3, 2, 387)
)
if mibBuilder.loadTexts:
    atmIfPnniRccVcdTdpTable.setStatus("mandatory")
_AtmIfPnniRccVcdTdpEntry_Object = MibTableRow
atmIfPnniRccVcdTdpEntry = _AtmIfPnniRccVcdTdpEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 3, 2, 387, 1)
)
atmIfPnniRccVcdTdpEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmPnniMIB", "atmIfPnniIndex"),
    (0, "Nortel-Magellan-Passport-AtmPnniMIB", "atmIfPnniRccIndex"),
    (0, "Nortel-Magellan-Passport-AtmPnniMIB", "atmIfPnniRccVcdIndex"),
    (0, "Nortel-Magellan-Passport-AtmPnniMIB", "atmIfPnniRccVcdTdpIndex"),
)
if mibBuilder.loadTexts:
    atmIfPnniRccVcdTdpEntry.setStatus("mandatory")


class _AtmIfPnniRccVcdTdpIndex_Type(Integer32):
    """Custom type atmIfPnniRccVcdTdpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_AtmIfPnniRccVcdTdpIndex_Type.__name__ = "Integer32"
_AtmIfPnniRccVcdTdpIndex_Object = MibTableColumn
atmIfPnniRccVcdTdpIndex = _AtmIfPnniRccVcdTdpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 3, 2, 387, 1, 1),
    _AtmIfPnniRccVcdTdpIndex_Type()
)
atmIfPnniRccVcdTdpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmIfPnniRccVcdTdpIndex.setStatus("mandatory")


class _AtmIfPnniRccVcdTdpValue_Type(Unsigned32):
    """Custom type atmIfPnniRccVcdTdpValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AtmIfPnniRccVcdTdpValue_Type.__name__ = "Unsigned32"
_AtmIfPnniRccVcdTdpValue_Object = MibTableColumn
atmIfPnniRccVcdTdpValue = _AtmIfPnniRccVcdTdpValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 3, 2, 387, 1, 2),
    _AtmIfPnniRccVcdTdpValue_Type()
)
atmIfPnniRccVcdTdpValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfPnniRccVcdTdpValue.setStatus("mandatory")
_AtmIfPnniRccProvTable_Object = MibTable
atmIfPnniRccProvTable = _AtmIfPnniRccProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 3, 10)
)
if mibBuilder.loadTexts:
    atmIfPnniRccProvTable.setStatus("mandatory")
_AtmIfPnniRccProvEntry_Object = MibTableRow
atmIfPnniRccProvEntry = _AtmIfPnniRccProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 3, 10, 1)
)
atmIfPnniRccProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmPnniMIB", "atmIfPnniIndex"),
    (0, "Nortel-Magellan-Passport-AtmPnniMIB", "atmIfPnniRccIndex"),
)
if mibBuilder.loadTexts:
    atmIfPnniRccProvEntry.setStatus("mandatory")


class _AtmIfPnniRccVci_Type(Unsigned32):
    """Custom type atmIfPnniRccVci based on Unsigned32"""
    defaultValue = 18

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AtmIfPnniRccVci_Type.__name__ = "Unsigned32"
_AtmIfPnniRccVci_Object = MibTableColumn
atmIfPnniRccVci = _AtmIfPnniRccVci_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 3, 10, 1, 1),
    _AtmIfPnniRccVci_Type()
)
atmIfPnniRccVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfPnniRccVci.setStatus("mandatory")
_AtmIfPnniRccHlParmsTable_Object = MibTable
atmIfPnniRccHlParmsTable = _AtmIfPnniRccHlParmsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 3, 11)
)
if mibBuilder.loadTexts:
    atmIfPnniRccHlParmsTable.setStatus("mandatory")
_AtmIfPnniRccHlParmsEntry_Object = MibTableRow
atmIfPnniRccHlParmsEntry = _AtmIfPnniRccHlParmsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 3, 11, 1)
)
atmIfPnniRccHlParmsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmPnniMIB", "atmIfPnniIndex"),
    (0, "Nortel-Magellan-Passport-AtmPnniMIB", "atmIfPnniRccIndex"),
)
if mibBuilder.loadTexts:
    atmIfPnniRccHlParmsEntry.setStatus("mandatory")


class _AtmIfPnniRccHelloHoldDown_Type(FixedPoint1):
    """Custom type atmIfPnniRccHelloHoldDown based on FixedPoint1"""
    defaultValue = 0

    subtypeSpec = FixedPoint1.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 655350),
    )


_AtmIfPnniRccHelloHoldDown_Type.__name__ = "FixedPoint1"
_AtmIfPnniRccHelloHoldDown_Object = MibTableColumn
atmIfPnniRccHelloHoldDown = _AtmIfPnniRccHelloHoldDown_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 3, 11, 1, 1),
    _AtmIfPnniRccHelloHoldDown_Type()
)
atmIfPnniRccHelloHoldDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfPnniRccHelloHoldDown.setStatus("mandatory")


class _AtmIfPnniRccHelloInterval_Type(Unsigned32):
    """Custom type atmIfPnniRccHelloInterval based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AtmIfPnniRccHelloInterval_Type.__name__ = "Unsigned32"
_AtmIfPnniRccHelloInterval_Object = MibTableColumn
atmIfPnniRccHelloInterval = _AtmIfPnniRccHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 3, 11, 1, 2),
    _AtmIfPnniRccHelloInterval_Type()
)
atmIfPnniRccHelloInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfPnniRccHelloInterval.setStatus("mandatory")


class _AtmIfPnniRccHelloInactivityFactor_Type(Unsigned32):
    """Custom type atmIfPnniRccHelloInactivityFactor based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AtmIfPnniRccHelloInactivityFactor_Type.__name__ = "Unsigned32"
_AtmIfPnniRccHelloInactivityFactor_Object = MibTableColumn
atmIfPnniRccHelloInactivityFactor = _AtmIfPnniRccHelloInactivityFactor_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 3, 11, 1, 3),
    _AtmIfPnniRccHelloInactivityFactor_Type()
)
atmIfPnniRccHelloInactivityFactor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfPnniRccHelloInactivityFactor.setStatus("mandatory")
_AtmIfPnniRccStateTable_Object = MibTable
atmIfPnniRccStateTable = _AtmIfPnniRccStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 3, 12)
)
if mibBuilder.loadTexts:
    atmIfPnniRccStateTable.setStatus("mandatory")
_AtmIfPnniRccStateEntry_Object = MibTableRow
atmIfPnniRccStateEntry = _AtmIfPnniRccStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 3, 12, 1)
)
atmIfPnniRccStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmPnniMIB", "atmIfPnniIndex"),
    (0, "Nortel-Magellan-Passport-AtmPnniMIB", "atmIfPnniRccIndex"),
)
if mibBuilder.loadTexts:
    atmIfPnniRccStateEntry.setStatus("mandatory")


class _AtmIfPnniRccAdminState_Type(Integer32):
    """Custom type atmIfPnniRccAdminState based on Integer32"""
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


_AtmIfPnniRccAdminState_Type.__name__ = "Integer32"
_AtmIfPnniRccAdminState_Object = MibTableColumn
atmIfPnniRccAdminState = _AtmIfPnniRccAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 3, 12, 1, 1),
    _AtmIfPnniRccAdminState_Type()
)
atmIfPnniRccAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfPnniRccAdminState.setStatus("mandatory")


class _AtmIfPnniRccOperationalState_Type(Integer32):
    """Custom type atmIfPnniRccOperationalState based on Integer32"""
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


_AtmIfPnniRccOperationalState_Type.__name__ = "Integer32"
_AtmIfPnniRccOperationalState_Object = MibTableColumn
atmIfPnniRccOperationalState = _AtmIfPnniRccOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 3, 12, 1, 2),
    _AtmIfPnniRccOperationalState_Type()
)
atmIfPnniRccOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfPnniRccOperationalState.setStatus("mandatory")


class _AtmIfPnniRccUsageState_Type(Integer32):
    """Custom type atmIfPnniRccUsageState based on Integer32"""
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


_AtmIfPnniRccUsageState_Type.__name__ = "Integer32"
_AtmIfPnniRccUsageState_Object = MibTableColumn
atmIfPnniRccUsageState = _AtmIfPnniRccUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 3, 12, 1, 3),
    _AtmIfPnniRccUsageState_Type()
)
atmIfPnniRccUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfPnniRccUsageState.setStatus("mandatory")
_AtmIfPnniRccOperTable_Object = MibTable
atmIfPnniRccOperTable = _AtmIfPnniRccOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 3, 13)
)
if mibBuilder.loadTexts:
    atmIfPnniRccOperTable.setStatus("mandatory")
_AtmIfPnniRccOperEntry_Object = MibTableRow
atmIfPnniRccOperEntry = _AtmIfPnniRccOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 3, 13, 1)
)
atmIfPnniRccOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmPnniMIB", "atmIfPnniIndex"),
    (0, "Nortel-Magellan-Passport-AtmPnniMIB", "atmIfPnniRccIndex"),
)
if mibBuilder.loadTexts:
    atmIfPnniRccOperEntry.setStatus("mandatory")


class _AtmIfPnniRccType_Type(Integer32):
    """Custom type atmIfPnniRccType based on Integer32"""
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


_AtmIfPnniRccType_Type.__name__ = "Integer32"
_AtmIfPnniRccType_Object = MibTableColumn
atmIfPnniRccType = _AtmIfPnniRccType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 3, 13, 1, 1),
    _AtmIfPnniRccType_Type()
)
atmIfPnniRccType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfPnniRccType.setStatus("mandatory")


class _AtmIfPnniRccNegotiatedVersion_Type(Integer32):
    """Custom type atmIfPnniRccNegotiatedVersion based on Integer32"""
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


_AtmIfPnniRccNegotiatedVersion_Type.__name__ = "Integer32"
_AtmIfPnniRccNegotiatedVersion_Object = MibTableColumn
atmIfPnniRccNegotiatedVersion = _AtmIfPnniRccNegotiatedVersion_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 3, 13, 1, 2),
    _AtmIfPnniRccNegotiatedVersion_Type()
)
atmIfPnniRccNegotiatedVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfPnniRccNegotiatedVersion.setStatus("mandatory")


class _AtmIfPnniRccHelloState_Type(Integer32):
    """Custom type atmIfPnniRccHelloState based on Integer32"""
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


_AtmIfPnniRccHelloState_Type.__name__ = "Integer32"
_AtmIfPnniRccHelloState_Object = MibTableColumn
atmIfPnniRccHelloState = _AtmIfPnniRccHelloState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 3, 13, 1, 3),
    _AtmIfPnniRccHelloState_Type()
)
atmIfPnniRccHelloState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfPnniRccHelloState.setStatus("mandatory")


class _AtmIfPnniRccRemoteNodeId_Type(HexString):
    """Custom type atmIfPnniRccRemoteNodeId based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(22, 22),
    )


_AtmIfPnniRccRemoteNodeId_Type.__name__ = "HexString"
_AtmIfPnniRccRemoteNodeId_Object = MibTableColumn
atmIfPnniRccRemoteNodeId = _AtmIfPnniRccRemoteNodeId_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 3, 13, 1, 4),
    _AtmIfPnniRccRemoteNodeId_Type()
)
atmIfPnniRccRemoteNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfPnniRccRemoteNodeId.setStatus("mandatory")


class _AtmIfPnniRccRemotePortId_Type(Unsigned32):
    """Custom type atmIfPnniRccRemotePortId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AtmIfPnniRccRemotePortId_Type.__name__ = "Unsigned32"
_AtmIfPnniRccRemotePortId_Object = MibTableColumn
atmIfPnniRccRemotePortId = _AtmIfPnniRccRemotePortId_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 3, 13, 1, 5),
    _AtmIfPnniRccRemotePortId_Type()
)
atmIfPnniRccRemotePortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfPnniRccRemotePortId.setStatus("mandatory")
_AtmIfPnniRccStatsTable_Object = MibTable
atmIfPnniRccStatsTable = _AtmIfPnniRccStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 3, 14)
)
if mibBuilder.loadTexts:
    atmIfPnniRccStatsTable.setStatus("mandatory")
_AtmIfPnniRccStatsEntry_Object = MibTableRow
atmIfPnniRccStatsEntry = _AtmIfPnniRccStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 3, 14, 1)
)
atmIfPnniRccStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmPnniMIB", "atmIfPnniIndex"),
    (0, "Nortel-Magellan-Passport-AtmPnniMIB", "atmIfPnniRccIndex"),
)
if mibBuilder.loadTexts:
    atmIfPnniRccStatsEntry.setStatus("mandatory")
_AtmIfPnniRccHelloPacketsRx_Type = Counter32
_AtmIfPnniRccHelloPacketsRx_Object = MibTableColumn
atmIfPnniRccHelloPacketsRx = _AtmIfPnniRccHelloPacketsRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 3, 14, 1, 1),
    _AtmIfPnniRccHelloPacketsRx_Type()
)
atmIfPnniRccHelloPacketsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfPnniRccHelloPacketsRx.setStatus("mandatory")
_AtmIfPnniRccHelloPacketsTx_Type = Counter32
_AtmIfPnniRccHelloPacketsTx_Object = MibTableColumn
atmIfPnniRccHelloPacketsTx = _AtmIfPnniRccHelloPacketsTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 3, 14, 1, 2),
    _AtmIfPnniRccHelloPacketsTx_Type()
)
atmIfPnniRccHelloPacketsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfPnniRccHelloPacketsTx.setStatus("mandatory")
_AtmIfPnniRccMismatchedHelloPacketsRx_Type = Counter32
_AtmIfPnniRccMismatchedHelloPacketsRx_Object = MibTableColumn
atmIfPnniRccMismatchedHelloPacketsRx = _AtmIfPnniRccMismatchedHelloPacketsRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 3, 14, 1, 3),
    _AtmIfPnniRccMismatchedHelloPacketsRx_Type()
)
atmIfPnniRccMismatchedHelloPacketsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfPnniRccMismatchedHelloPacketsRx.setStatus("mandatory")
_AtmIfPnniRccBadHelloPacketsRx_Type = Counter32
_AtmIfPnniRccBadHelloPacketsRx_Object = MibTableColumn
atmIfPnniRccBadHelloPacketsRx = _AtmIfPnniRccBadHelloPacketsRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 3, 14, 1, 4),
    _AtmIfPnniRccBadHelloPacketsRx_Type()
)
atmIfPnniRccBadHelloPacketsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfPnniRccBadHelloPacketsRx.setStatus("mandatory")
_AtmIfPnniAddr_ObjectIdentity = ObjectIdentity
atmIfPnniAddr = _AtmIfPnniAddr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 4)
)
_AtmIfPnniAddrRowStatusTable_Object = MibTable
atmIfPnniAddrRowStatusTable = _AtmIfPnniAddrRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 4, 1)
)
if mibBuilder.loadTexts:
    atmIfPnniAddrRowStatusTable.setStatus("mandatory")
_AtmIfPnniAddrRowStatusEntry_Object = MibTableRow
atmIfPnniAddrRowStatusEntry = _AtmIfPnniAddrRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 4, 1, 1)
)
atmIfPnniAddrRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmPnniMIB", "atmIfPnniIndex"),
    (0, "Nortel-Magellan-Passport-AtmPnniMIB", "atmIfPnniAddrAddressIndex"),
    (0, "Nortel-Magellan-Passport-AtmPnniMIB", "atmIfPnniAddrAddressTypeIndex"),
)
if mibBuilder.loadTexts:
    atmIfPnniAddrRowStatusEntry.setStatus("mandatory")
_AtmIfPnniAddrRowStatus_Type = RowStatus
_AtmIfPnniAddrRowStatus_Object = MibTableColumn
atmIfPnniAddrRowStatus = _AtmIfPnniAddrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 4, 1, 1, 1),
    _AtmIfPnniAddrRowStatus_Type()
)
atmIfPnniAddrRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfPnniAddrRowStatus.setStatus("mandatory")
_AtmIfPnniAddrComponentName_Type = DisplayString
_AtmIfPnniAddrComponentName_Object = MibTableColumn
atmIfPnniAddrComponentName = _AtmIfPnniAddrComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 4, 1, 1, 2),
    _AtmIfPnniAddrComponentName_Type()
)
atmIfPnniAddrComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfPnniAddrComponentName.setStatus("mandatory")
_AtmIfPnniAddrStorageType_Type = StorageType
_AtmIfPnniAddrStorageType_Object = MibTableColumn
atmIfPnniAddrStorageType = _AtmIfPnniAddrStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 4, 1, 1, 4),
    _AtmIfPnniAddrStorageType_Type()
)
atmIfPnniAddrStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfPnniAddrStorageType.setStatus("mandatory")


class _AtmIfPnniAddrAddressIndex_Type(AsciiStringIndex):
    """Custom type atmIfPnniAddrAddressIndex based on AsciiStringIndex"""
    subtypeSpec = AsciiStringIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_AtmIfPnniAddrAddressIndex_Type.__name__ = "AsciiStringIndex"
_AtmIfPnniAddrAddressIndex_Object = MibTableColumn
atmIfPnniAddrAddressIndex = _AtmIfPnniAddrAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 4, 1, 1, 10),
    _AtmIfPnniAddrAddressIndex_Type()
)
atmIfPnniAddrAddressIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmIfPnniAddrAddressIndex.setStatus("mandatory")


class _AtmIfPnniAddrAddressTypeIndex_Type(Integer32):
    """Custom type atmIfPnniAddrAddressTypeIndex based on Integer32"""
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


_AtmIfPnniAddrAddressTypeIndex_Type.__name__ = "Integer32"
_AtmIfPnniAddrAddressTypeIndex_Object = MibTableColumn
atmIfPnniAddrAddressTypeIndex = _AtmIfPnniAddrAddressTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 4, 1, 1, 11),
    _AtmIfPnniAddrAddressTypeIndex_Type()
)
atmIfPnniAddrAddressTypeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmIfPnniAddrAddressTypeIndex.setStatus("mandatory")
_AtmIfPnniAddrTermSP_ObjectIdentity = ObjectIdentity
atmIfPnniAddrTermSP = _AtmIfPnniAddrTermSP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 4, 2)
)
_AtmIfPnniAddrTermSPRowStatusTable_Object = MibTable
atmIfPnniAddrTermSPRowStatusTable = _AtmIfPnniAddrTermSPRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 4, 2, 1)
)
if mibBuilder.loadTexts:
    atmIfPnniAddrTermSPRowStatusTable.setStatus("mandatory")
_AtmIfPnniAddrTermSPRowStatusEntry_Object = MibTableRow
atmIfPnniAddrTermSPRowStatusEntry = _AtmIfPnniAddrTermSPRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 4, 2, 1, 1)
)
atmIfPnniAddrTermSPRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmPnniMIB", "atmIfPnniIndex"),
    (0, "Nortel-Magellan-Passport-AtmPnniMIB", "atmIfPnniAddrAddressIndex"),
    (0, "Nortel-Magellan-Passport-AtmPnniMIB", "atmIfPnniAddrAddressTypeIndex"),
    (0, "Nortel-Magellan-Passport-AtmPnniMIB", "atmIfPnniAddrTermSPIndex"),
)
if mibBuilder.loadTexts:
    atmIfPnniAddrTermSPRowStatusEntry.setStatus("mandatory")
_AtmIfPnniAddrTermSPRowStatus_Type = RowStatus
_AtmIfPnniAddrTermSPRowStatus_Object = MibTableColumn
atmIfPnniAddrTermSPRowStatus = _AtmIfPnniAddrTermSPRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 4, 2, 1, 1, 1),
    _AtmIfPnniAddrTermSPRowStatus_Type()
)
atmIfPnniAddrTermSPRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfPnniAddrTermSPRowStatus.setStatus("mandatory")
_AtmIfPnniAddrTermSPComponentName_Type = DisplayString
_AtmIfPnniAddrTermSPComponentName_Object = MibTableColumn
atmIfPnniAddrTermSPComponentName = _AtmIfPnniAddrTermSPComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 4, 2, 1, 1, 2),
    _AtmIfPnniAddrTermSPComponentName_Type()
)
atmIfPnniAddrTermSPComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfPnniAddrTermSPComponentName.setStatus("mandatory")
_AtmIfPnniAddrTermSPStorageType_Type = StorageType
_AtmIfPnniAddrTermSPStorageType_Object = MibTableColumn
atmIfPnniAddrTermSPStorageType = _AtmIfPnniAddrTermSPStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 4, 2, 1, 1, 4),
    _AtmIfPnniAddrTermSPStorageType_Type()
)
atmIfPnniAddrTermSPStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfPnniAddrTermSPStorageType.setStatus("mandatory")
_AtmIfPnniAddrTermSPIndex_Type = NonReplicated
_AtmIfPnniAddrTermSPIndex_Object = MibTableColumn
atmIfPnniAddrTermSPIndex = _AtmIfPnniAddrTermSPIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 4, 2, 1, 1, 10),
    _AtmIfPnniAddrTermSPIndex_Type()
)
atmIfPnniAddrTermSPIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmIfPnniAddrTermSPIndex.setStatus("mandatory")
_AtmIfPnniAddrPnniInfo_ObjectIdentity = ObjectIdentity
atmIfPnniAddrPnniInfo = _AtmIfPnniAddrPnniInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 4, 3)
)
_AtmIfPnniAddrPnniInfoRowStatusTable_Object = MibTable
atmIfPnniAddrPnniInfoRowStatusTable = _AtmIfPnniAddrPnniInfoRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 4, 3, 1)
)
if mibBuilder.loadTexts:
    atmIfPnniAddrPnniInfoRowStatusTable.setStatus("mandatory")
_AtmIfPnniAddrPnniInfoRowStatusEntry_Object = MibTableRow
atmIfPnniAddrPnniInfoRowStatusEntry = _AtmIfPnniAddrPnniInfoRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 4, 3, 1, 1)
)
atmIfPnniAddrPnniInfoRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmPnniMIB", "atmIfPnniIndex"),
    (0, "Nortel-Magellan-Passport-AtmPnniMIB", "atmIfPnniAddrAddressIndex"),
    (0, "Nortel-Magellan-Passport-AtmPnniMIB", "atmIfPnniAddrAddressTypeIndex"),
    (0, "Nortel-Magellan-Passport-AtmPnniMIB", "atmIfPnniAddrPnniInfoIndex"),
)
if mibBuilder.loadTexts:
    atmIfPnniAddrPnniInfoRowStatusEntry.setStatus("mandatory")
_AtmIfPnniAddrPnniInfoRowStatus_Type = RowStatus
_AtmIfPnniAddrPnniInfoRowStatus_Object = MibTableColumn
atmIfPnniAddrPnniInfoRowStatus = _AtmIfPnniAddrPnniInfoRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 4, 3, 1, 1, 1),
    _AtmIfPnniAddrPnniInfoRowStatus_Type()
)
atmIfPnniAddrPnniInfoRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfPnniAddrPnniInfoRowStatus.setStatus("mandatory")
_AtmIfPnniAddrPnniInfoComponentName_Type = DisplayString
_AtmIfPnniAddrPnniInfoComponentName_Object = MibTableColumn
atmIfPnniAddrPnniInfoComponentName = _AtmIfPnniAddrPnniInfoComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 4, 3, 1, 1, 2),
    _AtmIfPnniAddrPnniInfoComponentName_Type()
)
atmIfPnniAddrPnniInfoComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfPnniAddrPnniInfoComponentName.setStatus("mandatory")
_AtmIfPnniAddrPnniInfoStorageType_Type = StorageType
_AtmIfPnniAddrPnniInfoStorageType_Object = MibTableColumn
atmIfPnniAddrPnniInfoStorageType = _AtmIfPnniAddrPnniInfoStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 4, 3, 1, 1, 4),
    _AtmIfPnniAddrPnniInfoStorageType_Type()
)
atmIfPnniAddrPnniInfoStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfPnniAddrPnniInfoStorageType.setStatus("mandatory")
_AtmIfPnniAddrPnniInfoIndex_Type = NonReplicated
_AtmIfPnniAddrPnniInfoIndex_Object = MibTableColumn
atmIfPnniAddrPnniInfoIndex = _AtmIfPnniAddrPnniInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 4, 3, 1, 1, 10),
    _AtmIfPnniAddrPnniInfoIndex_Type()
)
atmIfPnniAddrPnniInfoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmIfPnniAddrPnniInfoIndex.setStatus("mandatory")
_AtmIfPnniAddrPnniInfoProvTable_Object = MibTable
atmIfPnniAddrPnniInfoProvTable = _AtmIfPnniAddrPnniInfoProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 4, 3, 10)
)
if mibBuilder.loadTexts:
    atmIfPnniAddrPnniInfoProvTable.setStatus("mandatory")
_AtmIfPnniAddrPnniInfoProvEntry_Object = MibTableRow
atmIfPnniAddrPnniInfoProvEntry = _AtmIfPnniAddrPnniInfoProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 4, 3, 10, 1)
)
atmIfPnniAddrPnniInfoProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmPnniMIB", "atmIfPnniIndex"),
    (0, "Nortel-Magellan-Passport-AtmPnniMIB", "atmIfPnniAddrAddressIndex"),
    (0, "Nortel-Magellan-Passport-AtmPnniMIB", "atmIfPnniAddrAddressTypeIndex"),
    (0, "Nortel-Magellan-Passport-AtmPnniMIB", "atmIfPnniAddrPnniInfoIndex"),
)
if mibBuilder.loadTexts:
    atmIfPnniAddrPnniInfoProvEntry.setStatus("mandatory")


class _AtmIfPnniAddrPnniInfoScope_Type(Integer32):
    """Custom type atmIfPnniAddrPnniInfoScope based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 104),
    )


_AtmIfPnniAddrPnniInfoScope_Type.__name__ = "Integer32"
_AtmIfPnniAddrPnniInfoScope_Object = MibTableColumn
atmIfPnniAddrPnniInfoScope = _AtmIfPnniAddrPnniInfoScope_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 4, 3, 10, 1, 1),
    _AtmIfPnniAddrPnniInfoScope_Type()
)
atmIfPnniAddrPnniInfoScope.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfPnniAddrPnniInfoScope.setStatus("mandatory")


class _AtmIfPnniAddrPnniInfoReachability_Type(Integer32):
    """Custom type atmIfPnniAddrPnniInfoReachability based on Integer32"""
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


_AtmIfPnniAddrPnniInfoReachability_Type.__name__ = "Integer32"
_AtmIfPnniAddrPnniInfoReachability_Object = MibTableColumn
atmIfPnniAddrPnniInfoReachability = _AtmIfPnniAddrPnniInfoReachability_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 4, 3, 10, 1, 2),
    _AtmIfPnniAddrPnniInfoReachability_Type()
)
atmIfPnniAddrPnniInfoReachability.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfPnniAddrPnniInfoReachability.setStatus("mandatory")
_AtmIfPnniAddrOperTable_Object = MibTable
atmIfPnniAddrOperTable = _AtmIfPnniAddrOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 4, 10)
)
if mibBuilder.loadTexts:
    atmIfPnniAddrOperTable.setStatus("mandatory")
_AtmIfPnniAddrOperEntry_Object = MibTableRow
atmIfPnniAddrOperEntry = _AtmIfPnniAddrOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 4, 10, 1)
)
atmIfPnniAddrOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmPnniMIB", "atmIfPnniIndex"),
    (0, "Nortel-Magellan-Passport-AtmPnniMIB", "atmIfPnniAddrAddressIndex"),
    (0, "Nortel-Magellan-Passport-AtmPnniMIB", "atmIfPnniAddrAddressTypeIndex"),
)
if mibBuilder.loadTexts:
    atmIfPnniAddrOperEntry.setStatus("mandatory")


class _AtmIfPnniAddrScope_Type(Integer32):
    """Custom type atmIfPnniAddrScope based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 104),
    )


_AtmIfPnniAddrScope_Type.__name__ = "Integer32"
_AtmIfPnniAddrScope_Object = MibTableColumn
atmIfPnniAddrScope = _AtmIfPnniAddrScope_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 4, 10, 1, 1),
    _AtmIfPnniAddrScope_Type()
)
atmIfPnniAddrScope.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfPnniAddrScope.setStatus("mandatory")


class _AtmIfPnniAddrReachability_Type(Integer32):
    """Custom type atmIfPnniAddrReachability based on Integer32"""
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


_AtmIfPnniAddrReachability_Type.__name__ = "Integer32"
_AtmIfPnniAddrReachability_Object = MibTableColumn
atmIfPnniAddrReachability = _AtmIfPnniAddrReachability_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 4, 10, 1, 2),
    _AtmIfPnniAddrReachability_Type()
)
atmIfPnniAddrReachability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfPnniAddrReachability.setStatus("mandatory")
_AtmIfPnniProvTable_Object = MibTable
atmIfPnniProvTable = _AtmIfPnniProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 10)
)
if mibBuilder.loadTexts:
    atmIfPnniProvTable.setStatus("mandatory")
_AtmIfPnniProvEntry_Object = MibTableRow
atmIfPnniProvEntry = _AtmIfPnniProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 10, 1)
)
atmIfPnniProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmPnniMIB", "atmIfPnniIndex"),
)
if mibBuilder.loadTexts:
    atmIfPnniProvEntry.setStatus("mandatory")


class _AtmIfPnniSoftPvcRetryPeriod_Type(Unsigned32):
    """Custom type atmIfPnniSoftPvcRetryPeriod based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 999999),
    )


_AtmIfPnniSoftPvcRetryPeriod_Type.__name__ = "Unsigned32"
_AtmIfPnniSoftPvcRetryPeriod_Object = MibTableColumn
atmIfPnniSoftPvcRetryPeriod = _AtmIfPnniSoftPvcRetryPeriod_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 10, 1, 1),
    _AtmIfPnniSoftPvcRetryPeriod_Type()
)
atmIfPnniSoftPvcRetryPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfPnniSoftPvcRetryPeriod.setStatus("obsolete")


class _AtmIfPnniSoftPvpAndPvcRetryPeriod_Type(Unsigned32):
    """Custom type atmIfPnniSoftPvpAndPvcRetryPeriod based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 999999),
    )


_AtmIfPnniSoftPvpAndPvcRetryPeriod_Type.__name__ = "Unsigned32"
_AtmIfPnniSoftPvpAndPvcRetryPeriod_Object = MibTableColumn
atmIfPnniSoftPvpAndPvcRetryPeriod = _AtmIfPnniSoftPvpAndPvcRetryPeriod_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 10, 1, 2),
    _AtmIfPnniSoftPvpAndPvcRetryPeriod_Type()
)
atmIfPnniSoftPvpAndPvcRetryPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfPnniSoftPvpAndPvcRetryPeriod.setStatus("mandatory")


class _AtmIfPnniSoftPvpAndPvcHoldOffTime_Type(Unsigned32):
    """Custom type atmIfPnniSoftPvpAndPvcHoldOffTime based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(50, 20000),
    )


_AtmIfPnniSoftPvpAndPvcHoldOffTime_Type.__name__ = "Unsigned32"
_AtmIfPnniSoftPvpAndPvcHoldOffTime_Object = MibTableColumn
atmIfPnniSoftPvpAndPvcHoldOffTime = _AtmIfPnniSoftPvpAndPvcHoldOffTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 10, 1, 5),
    _AtmIfPnniSoftPvpAndPvcHoldOffTime_Type()
)
atmIfPnniSoftPvpAndPvcHoldOffTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfPnniSoftPvpAndPvcHoldOffTime.setStatus("mandatory")
_AtmIfPnniAdminWeightsTable_Object = MibTable
atmIfPnniAdminWeightsTable = _AtmIfPnniAdminWeightsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 11)
)
if mibBuilder.loadTexts:
    atmIfPnniAdminWeightsTable.setStatus("mandatory")
_AtmIfPnniAdminWeightsEntry_Object = MibTableRow
atmIfPnniAdminWeightsEntry = _AtmIfPnniAdminWeightsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 11, 1)
)
atmIfPnniAdminWeightsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmPnniMIB", "atmIfPnniIndex"),
)
if mibBuilder.loadTexts:
    atmIfPnniAdminWeightsEntry.setStatus("mandatory")


class _AtmIfPnniCbrWeight_Type(Unsigned32):
    """Custom type atmIfPnniCbrWeight based on Unsigned32"""
    defaultValue = 5040

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AtmIfPnniCbrWeight_Type.__name__ = "Unsigned32"
_AtmIfPnniCbrWeight_Object = MibTableColumn
atmIfPnniCbrWeight = _AtmIfPnniCbrWeight_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 11, 1, 1),
    _AtmIfPnniCbrWeight_Type()
)
atmIfPnniCbrWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfPnniCbrWeight.setStatus("mandatory")


class _AtmIfPnniRtVbrWeight_Type(Unsigned32):
    """Custom type atmIfPnniRtVbrWeight based on Unsigned32"""
    defaultValue = 5040

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AtmIfPnniRtVbrWeight_Type.__name__ = "Unsigned32"
_AtmIfPnniRtVbrWeight_Object = MibTableColumn
atmIfPnniRtVbrWeight = _AtmIfPnniRtVbrWeight_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 11, 1, 2),
    _AtmIfPnniRtVbrWeight_Type()
)
atmIfPnniRtVbrWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfPnniRtVbrWeight.setStatus("mandatory")


class _AtmIfPnniNrtVbrWeight_Type(Unsigned32):
    """Custom type atmIfPnniNrtVbrWeight based on Unsigned32"""
    defaultValue = 5040

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AtmIfPnniNrtVbrWeight_Type.__name__ = "Unsigned32"
_AtmIfPnniNrtVbrWeight_Object = MibTableColumn
atmIfPnniNrtVbrWeight = _AtmIfPnniNrtVbrWeight_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 11, 1, 3),
    _AtmIfPnniNrtVbrWeight_Type()
)
atmIfPnniNrtVbrWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfPnniNrtVbrWeight.setStatus("mandatory")


class _AtmIfPnniUbrWeight_Type(Unsigned32):
    """Custom type atmIfPnniUbrWeight based on Unsigned32"""
    defaultValue = 5040

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AtmIfPnniUbrWeight_Type.__name__ = "Unsigned32"
_AtmIfPnniUbrWeight_Object = MibTableColumn
atmIfPnniUbrWeight = _AtmIfPnniUbrWeight_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 11, 1, 4),
    _AtmIfPnniUbrWeight_Type()
)
atmIfPnniUbrWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfPnniUbrWeight.setStatus("mandatory")
_AtmIfPnniAcctOptTable_Object = MibTable
atmIfPnniAcctOptTable = _AtmIfPnniAcctOptTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 12)
)
if mibBuilder.loadTexts:
    atmIfPnniAcctOptTable.setStatus("mandatory")
_AtmIfPnniAcctOptEntry_Object = MibTableRow
atmIfPnniAcctOptEntry = _AtmIfPnniAcctOptEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 12, 1)
)
atmIfPnniAcctOptEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmPnniMIB", "atmIfPnniIndex"),
)
if mibBuilder.loadTexts:
    atmIfPnniAcctOptEntry.setStatus("mandatory")


class _AtmIfPnniAccountCollection_Type(OctetString):
    """Custom type atmIfPnniAccountCollection based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_AtmIfPnniAccountCollection_Type.__name__ = "OctetString"
_AtmIfPnniAccountCollection_Object = MibTableColumn
atmIfPnniAccountCollection = _AtmIfPnniAccountCollection_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 12, 1, 1),
    _AtmIfPnniAccountCollection_Type()
)
atmIfPnniAccountCollection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfPnniAccountCollection.setStatus("mandatory")


class _AtmIfPnniAccountConnectionType_Type(Integer32):
    """Custom type atmIfPnniAccountConnectionType based on Integer32"""
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


_AtmIfPnniAccountConnectionType_Type.__name__ = "Integer32"
_AtmIfPnniAccountConnectionType_Object = MibTableColumn
atmIfPnniAccountConnectionType = _AtmIfPnniAccountConnectionType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 12, 1, 2),
    _AtmIfPnniAccountConnectionType_Type()
)
atmIfPnniAccountConnectionType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfPnniAccountConnectionType.setStatus("mandatory")


class _AtmIfPnniAccountClass_Type(Unsigned32):
    """Custom type atmIfPnniAccountClass based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AtmIfPnniAccountClass_Type.__name__ = "Unsigned32"
_AtmIfPnniAccountClass_Object = MibTableColumn
atmIfPnniAccountClass = _AtmIfPnniAccountClass_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 12, 1, 3),
    _AtmIfPnniAccountClass_Type()
)
atmIfPnniAccountClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfPnniAccountClass.setStatus("mandatory")


class _AtmIfPnniServiceExchange_Type(Unsigned32):
    """Custom type atmIfPnniServiceExchange based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AtmIfPnniServiceExchange_Type.__name__ = "Unsigned32"
_AtmIfPnniServiceExchange_Object = MibTableColumn
atmIfPnniServiceExchange = _AtmIfPnniServiceExchange_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 12, 1, 4),
    _AtmIfPnniServiceExchange_Type()
)
atmIfPnniServiceExchange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfPnniServiceExchange.setStatus("mandatory")
_AtmIfPnniOperationalTable_Object = MibTable
atmIfPnniOperationalTable = _AtmIfPnniOperationalTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 13)
)
if mibBuilder.loadTexts:
    atmIfPnniOperationalTable.setStatus("mandatory")
_AtmIfPnniOperationalEntry_Object = MibTableRow
atmIfPnniOperationalEntry = _AtmIfPnniOperationalEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 13, 1)
)
atmIfPnniOperationalEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmPnniMIB", "atmIfPnniIndex"),
)
if mibBuilder.loadTexts:
    atmIfPnniOperationalEntry.setStatus("mandatory")


class _AtmIfPnniPortId_Type(Unsigned32):
    """Custom type atmIfPnniPortId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AtmIfPnniPortId_Type.__name__ = "Unsigned32"
_AtmIfPnniPortId_Object = MibTableColumn
atmIfPnniPortId = _AtmIfPnniPortId_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 96, 13, 1, 1),
    _AtmIfPnniPortId_Type()
)
atmIfPnniPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfPnniPortId.setStatus("mandatory")
_AtmPnniMIB_ObjectIdentity = ObjectIdentity
atmPnniMIB = _AtmPnniMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 72)
)
_AtmPnniGroup_ObjectIdentity = ObjectIdentity
atmPnniGroup = _AtmPnniGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 72, 1)
)
_AtmPnniGroupBE_ObjectIdentity = ObjectIdentity
atmPnniGroupBE = _AtmPnniGroupBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 72, 1, 5)
)
_AtmPnniGroupBE00_ObjectIdentity = ObjectIdentity
atmPnniGroupBE00 = _AtmPnniGroupBE00_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 72, 1, 5, 1)
)
_AtmPnniGroupBE00A_ObjectIdentity = ObjectIdentity
atmPnniGroupBE00A = _AtmPnniGroupBE00A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 72, 1, 5, 1, 2)
)
_AtmPnniCapabilities_ObjectIdentity = ObjectIdentity
atmPnniCapabilities = _AtmPnniCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 72, 3)
)
_AtmPnniCapabilitiesBE_ObjectIdentity = ObjectIdentity
atmPnniCapabilitiesBE = _AtmPnniCapabilitiesBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 72, 3, 5)
)
_AtmPnniCapabilitiesBE00_ObjectIdentity = ObjectIdentity
atmPnniCapabilitiesBE00 = _AtmPnniCapabilitiesBE00_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 72, 3, 5, 1)
)
_AtmPnniCapabilitiesBE00A_ObjectIdentity = ObjectIdentity
atmPnniCapabilitiesBE00A = _AtmPnniCapabilitiesBE00A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 72, 3, 5, 1, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-Magellan-Passport-AtmPnniMIB",
    **{"atmIfVptPnni": atmIfVptPnni,
       "atmIfVptPnniRowStatusTable": atmIfVptPnniRowStatusTable,
       "atmIfVptPnniRowStatusEntry": atmIfVptPnniRowStatusEntry,
       "atmIfVptPnniRowStatus": atmIfVptPnniRowStatus,
       "atmIfVptPnniComponentName": atmIfVptPnniComponentName,
       "atmIfVptPnniStorageType": atmIfVptPnniStorageType,
       "atmIfVptPnniIndex": atmIfVptPnniIndex,
       "atmIfVptPnniSig": atmIfVptPnniSig,
       "atmIfVptPnniSigRowStatusTable": atmIfVptPnniSigRowStatusTable,
       "atmIfVptPnniSigRowStatusEntry": atmIfVptPnniSigRowStatusEntry,
       "atmIfVptPnniSigRowStatus": atmIfVptPnniSigRowStatus,
       "atmIfVptPnniSigComponentName": atmIfVptPnniSigComponentName,
       "atmIfVptPnniSigStorageType": atmIfVptPnniSigStorageType,
       "atmIfVptPnniSigIndex": atmIfVptPnniSigIndex,
       "atmIfVptPnniSigVcd": atmIfVptPnniSigVcd,
       "atmIfVptPnniSigVcdRowStatusTable": atmIfVptPnniSigVcdRowStatusTable,
       "atmIfVptPnniSigVcdRowStatusEntry": atmIfVptPnniSigVcdRowStatusEntry,
       "atmIfVptPnniSigVcdRowStatus": atmIfVptPnniSigVcdRowStatus,
       "atmIfVptPnniSigVcdComponentName": atmIfVptPnniSigVcdComponentName,
       "atmIfVptPnniSigVcdStorageType": atmIfVptPnniSigVcdStorageType,
       "atmIfVptPnniSigVcdIndex": atmIfVptPnniSigVcdIndex,
       "atmIfVptPnniSigVcdProvTable": atmIfVptPnniSigVcdProvTable,
       "atmIfVptPnniSigVcdProvEntry": atmIfVptPnniSigVcdProvEntry,
       "atmIfVptPnniSigVcdTrafficDescType": atmIfVptPnniSigVcdTrafficDescType,
       "atmIfVptPnniSigVcdAtmServiceCategory": atmIfVptPnniSigVcdAtmServiceCategory,
       "atmIfVptPnniSigVcdQosClass": atmIfVptPnniSigVcdQosClass,
       "atmIfVptPnniSigVcdTrafficShaping": atmIfVptPnniSigVcdTrafficShaping,
       "atmIfVptPnniSigVcdUnshapedTransmitQueueing": atmIfVptPnniSigVcdUnshapedTransmitQueueing,
       "atmIfVptPnniSigVcdUsageParameterControl": atmIfVptPnniSigVcdUsageParameterControl,
       "atmIfVptPnniSigVcdTdpTable": atmIfVptPnniSigVcdTdpTable,
       "atmIfVptPnniSigVcdTdpEntry": atmIfVptPnniSigVcdTdpEntry,
       "atmIfVptPnniSigVcdTdpIndex": atmIfVptPnniSigVcdTdpIndex,
       "atmIfVptPnniSigVcdTdpValue": atmIfVptPnniSigVcdTdpValue,
       "atmIfVptPnniSigProvTable": atmIfVptPnniSigProvTable,
       "atmIfVptPnniSigProvEntry": atmIfVptPnniSigProvEntry,
       "atmIfVptPnniSigVci": atmIfVptPnniSigVci,
       "atmIfVptPnniSigAddressConversion": atmIfVptPnniSigAddressConversion,
       "atmIfVptPnniSigStateTable": atmIfVptPnniSigStateTable,
       "atmIfVptPnniSigStateEntry": atmIfVptPnniSigStateEntry,
       "atmIfVptPnniSigAdminState": atmIfVptPnniSigAdminState,
       "atmIfVptPnniSigOperationalState": atmIfVptPnniSigOperationalState,
       "atmIfVptPnniSigUsageState": atmIfVptPnniSigUsageState,
       "atmIfVptPnniSigOperTable": atmIfVptPnniSigOperTable,
       "atmIfVptPnniSigOperEntry": atmIfVptPnniSigOperEntry,
       "atmIfVptPnniSigLastTxCauseCode": atmIfVptPnniSigLastTxCauseCode,
       "atmIfVptPnniSigLastTxDiagCode": atmIfVptPnniSigLastTxDiagCode,
       "atmIfVptPnniSigLastRxCauseCode": atmIfVptPnniSigLastRxCauseCode,
       "atmIfVptPnniSigLastRxDiagCode": atmIfVptPnniSigLastRxDiagCode,
       "atmIfVptPnniSigStatsTable": atmIfVptPnniSigStatsTable,
       "atmIfVptPnniSigStatsEntry": atmIfVptPnniSigStatsEntry,
       "atmIfVptPnniSigCurrentConnections": atmIfVptPnniSigCurrentConnections,
       "atmIfVptPnniSigPeakConnections": atmIfVptPnniSigPeakConnections,
       "atmIfVptPnniSigSuccessfulConnections": atmIfVptPnniSigSuccessfulConnections,
       "atmIfVptPnniSigFailedConnections": atmIfVptPnniSigFailedConnections,
       "atmIfVptPnniSigTxPdus": atmIfVptPnniSigTxPdus,
       "atmIfVptPnniSigRxPdus": atmIfVptPnniSigRxPdus,
       "atmIfVptPnniSigCurrentPmpConnections": atmIfVptPnniSigCurrentPmpConnections,
       "atmIfVptPnniSigPeakPmpConnections": atmIfVptPnniSigPeakPmpConnections,
       "atmIfVptPnniSigSuccessfulPmpConnections": atmIfVptPnniSigSuccessfulPmpConnections,
       "atmIfVptPnniSigFailedPmpConnections": atmIfVptPnniSigFailedPmpConnections,
       "atmIfVptPnniSigNewCurrentConnections": atmIfVptPnniSigNewCurrentConnections,
       "atmIfVptPnniRcc": atmIfVptPnniRcc,
       "atmIfVptPnniRccRowStatusTable": atmIfVptPnniRccRowStatusTable,
       "atmIfVptPnniRccRowStatusEntry": atmIfVptPnniRccRowStatusEntry,
       "atmIfVptPnniRccRowStatus": atmIfVptPnniRccRowStatus,
       "atmIfVptPnniRccComponentName": atmIfVptPnniRccComponentName,
       "atmIfVptPnniRccStorageType": atmIfVptPnniRccStorageType,
       "atmIfVptPnniRccIndex": atmIfVptPnniRccIndex,
       "atmIfVptPnniRccVcd": atmIfVptPnniRccVcd,
       "atmIfVptPnniRccVcdRowStatusTable": atmIfVptPnniRccVcdRowStatusTable,
       "atmIfVptPnniRccVcdRowStatusEntry": atmIfVptPnniRccVcdRowStatusEntry,
       "atmIfVptPnniRccVcdRowStatus": atmIfVptPnniRccVcdRowStatus,
       "atmIfVptPnniRccVcdComponentName": atmIfVptPnniRccVcdComponentName,
       "atmIfVptPnniRccVcdStorageType": atmIfVptPnniRccVcdStorageType,
       "atmIfVptPnniRccVcdIndex": atmIfVptPnniRccVcdIndex,
       "atmIfVptPnniRccVcdProvTable": atmIfVptPnniRccVcdProvTable,
       "atmIfVptPnniRccVcdProvEntry": atmIfVptPnniRccVcdProvEntry,
       "atmIfVptPnniRccVcdTrafficDescType": atmIfVptPnniRccVcdTrafficDescType,
       "atmIfVptPnniRccVcdAtmServiceCategory": atmIfVptPnniRccVcdAtmServiceCategory,
       "atmIfVptPnniRccVcdQosClass": atmIfVptPnniRccVcdQosClass,
       "atmIfVptPnniRccVcdTrafficShaping": atmIfVptPnniRccVcdTrafficShaping,
       "atmIfVptPnniRccVcdUnshapedTransmitQueueing": atmIfVptPnniRccVcdUnshapedTransmitQueueing,
       "atmIfVptPnniRccVcdUsageParameterControl": atmIfVptPnniRccVcdUsageParameterControl,
       "atmIfVptPnniRccVcdTdpTable": atmIfVptPnniRccVcdTdpTable,
       "atmIfVptPnniRccVcdTdpEntry": atmIfVptPnniRccVcdTdpEntry,
       "atmIfVptPnniRccVcdTdpIndex": atmIfVptPnniRccVcdTdpIndex,
       "atmIfVptPnniRccVcdTdpValue": atmIfVptPnniRccVcdTdpValue,
       "atmIfVptPnniRccProvTable": atmIfVptPnniRccProvTable,
       "atmIfVptPnniRccProvEntry": atmIfVptPnniRccProvEntry,
       "atmIfVptPnniRccVci": atmIfVptPnniRccVci,
       "atmIfVptPnniRccHlParmsTable": atmIfVptPnniRccHlParmsTable,
       "atmIfVptPnniRccHlParmsEntry": atmIfVptPnniRccHlParmsEntry,
       "atmIfVptPnniRccHelloHoldDown": atmIfVptPnniRccHelloHoldDown,
       "atmIfVptPnniRccHelloInterval": atmIfVptPnniRccHelloInterval,
       "atmIfVptPnniRccHelloInactivityFactor": atmIfVptPnniRccHelloInactivityFactor,
       "atmIfVptPnniRccStateTable": atmIfVptPnniRccStateTable,
       "atmIfVptPnniRccStateEntry": atmIfVptPnniRccStateEntry,
       "atmIfVptPnniRccAdminState": atmIfVptPnniRccAdminState,
       "atmIfVptPnniRccOperationalState": atmIfVptPnniRccOperationalState,
       "atmIfVptPnniRccUsageState": atmIfVptPnniRccUsageState,
       "atmIfVptPnniRccOperTable": atmIfVptPnniRccOperTable,
       "atmIfVptPnniRccOperEntry": atmIfVptPnniRccOperEntry,
       "atmIfVptPnniRccType": atmIfVptPnniRccType,
       "atmIfVptPnniRccNegotiatedVersion": atmIfVptPnniRccNegotiatedVersion,
       "atmIfVptPnniRccHelloState": atmIfVptPnniRccHelloState,
       "atmIfVptPnniRccRemoteNodeId": atmIfVptPnniRccRemoteNodeId,
       "atmIfVptPnniRccRemotePortId": atmIfVptPnniRccRemotePortId,
       "atmIfVptPnniRccStatsTable": atmIfVptPnniRccStatsTable,
       "atmIfVptPnniRccStatsEntry": atmIfVptPnniRccStatsEntry,
       "atmIfVptPnniRccHelloPacketsRx": atmIfVptPnniRccHelloPacketsRx,
       "atmIfVptPnniRccHelloPacketsTx": atmIfVptPnniRccHelloPacketsTx,
       "atmIfVptPnniRccMismatchedHelloPacketsRx": atmIfVptPnniRccMismatchedHelloPacketsRx,
       "atmIfVptPnniRccBadHelloPacketsRx": atmIfVptPnniRccBadHelloPacketsRx,
       "atmIfVptPnniAddr": atmIfVptPnniAddr,
       "atmIfVptPnniAddrRowStatusTable": atmIfVptPnniAddrRowStatusTable,
       "atmIfVptPnniAddrRowStatusEntry": atmIfVptPnniAddrRowStatusEntry,
       "atmIfVptPnniAddrRowStatus": atmIfVptPnniAddrRowStatus,
       "atmIfVptPnniAddrComponentName": atmIfVptPnniAddrComponentName,
       "atmIfVptPnniAddrStorageType": atmIfVptPnniAddrStorageType,
       "atmIfVptPnniAddrAddressIndex": atmIfVptPnniAddrAddressIndex,
       "atmIfVptPnniAddrAddressTypeIndex": atmIfVptPnniAddrAddressTypeIndex,
       "atmIfVptPnniAddrTermSP": atmIfVptPnniAddrTermSP,
       "atmIfVptPnniAddrTermSPRowStatusTable": atmIfVptPnniAddrTermSPRowStatusTable,
       "atmIfVptPnniAddrTermSPRowStatusEntry": atmIfVptPnniAddrTermSPRowStatusEntry,
       "atmIfVptPnniAddrTermSPRowStatus": atmIfVptPnniAddrTermSPRowStatus,
       "atmIfVptPnniAddrTermSPComponentName": atmIfVptPnniAddrTermSPComponentName,
       "atmIfVptPnniAddrTermSPStorageType": atmIfVptPnniAddrTermSPStorageType,
       "atmIfVptPnniAddrTermSPIndex": atmIfVptPnniAddrTermSPIndex,
       "atmIfVptPnniAddrPnniInfo": atmIfVptPnniAddrPnniInfo,
       "atmIfVptPnniAddrPnniInfoRowStatusTable": atmIfVptPnniAddrPnniInfoRowStatusTable,
       "atmIfVptPnniAddrPnniInfoRowStatusEntry": atmIfVptPnniAddrPnniInfoRowStatusEntry,
       "atmIfVptPnniAddrPnniInfoRowStatus": atmIfVptPnniAddrPnniInfoRowStatus,
       "atmIfVptPnniAddrPnniInfoComponentName": atmIfVptPnniAddrPnniInfoComponentName,
       "atmIfVptPnniAddrPnniInfoStorageType": atmIfVptPnniAddrPnniInfoStorageType,
       "atmIfVptPnniAddrPnniInfoIndex": atmIfVptPnniAddrPnniInfoIndex,
       "atmIfVptPnniAddrPnniInfoProvTable": atmIfVptPnniAddrPnniInfoProvTable,
       "atmIfVptPnniAddrPnniInfoProvEntry": atmIfVptPnniAddrPnniInfoProvEntry,
       "atmIfVptPnniAddrPnniInfoScope": atmIfVptPnniAddrPnniInfoScope,
       "atmIfVptPnniAddrPnniInfoReachability": atmIfVptPnniAddrPnniInfoReachability,
       "atmIfVptPnniAddrOperTable": atmIfVptPnniAddrOperTable,
       "atmIfVptPnniAddrOperEntry": atmIfVptPnniAddrOperEntry,
       "atmIfVptPnniAddrScope": atmIfVptPnniAddrScope,
       "atmIfVptPnniAddrReachability": atmIfVptPnniAddrReachability,
       "atmIfVptPnniProvTable": atmIfVptPnniProvTable,
       "atmIfVptPnniProvEntry": atmIfVptPnniProvEntry,
       "atmIfVptPnniSoftPvcRetryPeriod": atmIfVptPnniSoftPvcRetryPeriod,
       "atmIfVptPnniSoftPvpAndPvcRetryPeriod": atmIfVptPnniSoftPvpAndPvcRetryPeriod,
       "atmIfVptPnniSoftPvpAndPvcHoldOffTime": atmIfVptPnniSoftPvpAndPvcHoldOffTime,
       "atmIfVptPnniAdminWeightsTable": atmIfVptPnniAdminWeightsTable,
       "atmIfVptPnniAdminWeightsEntry": atmIfVptPnniAdminWeightsEntry,
       "atmIfVptPnniCbrWeight": atmIfVptPnniCbrWeight,
       "atmIfVptPnniRtVbrWeight": atmIfVptPnniRtVbrWeight,
       "atmIfVptPnniNrtVbrWeight": atmIfVptPnniNrtVbrWeight,
       "atmIfVptPnniUbrWeight": atmIfVptPnniUbrWeight,
       "atmIfVptPnniAcctOptTable": atmIfVptPnniAcctOptTable,
       "atmIfVptPnniAcctOptEntry": atmIfVptPnniAcctOptEntry,
       "atmIfVptPnniAccountCollection": atmIfVptPnniAccountCollection,
       "atmIfVptPnniAccountConnectionType": atmIfVptPnniAccountConnectionType,
       "atmIfVptPnniAccountClass": atmIfVptPnniAccountClass,
       "atmIfVptPnniServiceExchange": atmIfVptPnniServiceExchange,
       "atmIfVptPnniOperationalTable": atmIfVptPnniOperationalTable,
       "atmIfVptPnniOperationalEntry": atmIfVptPnniOperationalEntry,
       "atmIfVptPnniPortId": atmIfVptPnniPortId,
       "atmIfVptPnniVProvTable": atmIfVptPnniVProvTable,
       "atmIfVptPnniVProvEntry": atmIfVptPnniVProvEntry,
       "atmIfVptPnniVpci": atmIfVptPnniVpci,
       "atmIfPnni": atmIfPnni,
       "atmIfPnniRowStatusTable": atmIfPnniRowStatusTable,
       "atmIfPnniRowStatusEntry": atmIfPnniRowStatusEntry,
       "atmIfPnniRowStatus": atmIfPnniRowStatus,
       "atmIfPnniComponentName": atmIfPnniComponentName,
       "atmIfPnniStorageType": atmIfPnniStorageType,
       "atmIfPnniIndex": atmIfPnniIndex,
       "atmIfPnniSig": atmIfPnniSig,
       "atmIfPnniSigRowStatusTable": atmIfPnniSigRowStatusTable,
       "atmIfPnniSigRowStatusEntry": atmIfPnniSigRowStatusEntry,
       "atmIfPnniSigRowStatus": atmIfPnniSigRowStatus,
       "atmIfPnniSigComponentName": atmIfPnniSigComponentName,
       "atmIfPnniSigStorageType": atmIfPnniSigStorageType,
       "atmIfPnniSigIndex": atmIfPnniSigIndex,
       "atmIfPnniSigVcd": atmIfPnniSigVcd,
       "atmIfPnniSigVcdRowStatusTable": atmIfPnniSigVcdRowStatusTable,
       "atmIfPnniSigVcdRowStatusEntry": atmIfPnniSigVcdRowStatusEntry,
       "atmIfPnniSigVcdRowStatus": atmIfPnniSigVcdRowStatus,
       "atmIfPnniSigVcdComponentName": atmIfPnniSigVcdComponentName,
       "atmIfPnniSigVcdStorageType": atmIfPnniSigVcdStorageType,
       "atmIfPnniSigVcdIndex": atmIfPnniSigVcdIndex,
       "atmIfPnniSigVcdProvTable": atmIfPnniSigVcdProvTable,
       "atmIfPnniSigVcdProvEntry": atmIfPnniSigVcdProvEntry,
       "atmIfPnniSigVcdTrafficDescType": atmIfPnniSigVcdTrafficDescType,
       "atmIfPnniSigVcdAtmServiceCategory": atmIfPnniSigVcdAtmServiceCategory,
       "atmIfPnniSigVcdQosClass": atmIfPnniSigVcdQosClass,
       "atmIfPnniSigVcdTrafficShaping": atmIfPnniSigVcdTrafficShaping,
       "atmIfPnniSigVcdUnshapedTransmitQueueing": atmIfPnniSigVcdUnshapedTransmitQueueing,
       "atmIfPnniSigVcdUsageParameterControl": atmIfPnniSigVcdUsageParameterControl,
       "atmIfPnniSigVcdTdpTable": atmIfPnniSigVcdTdpTable,
       "atmIfPnniSigVcdTdpEntry": atmIfPnniSigVcdTdpEntry,
       "atmIfPnniSigVcdTdpIndex": atmIfPnniSigVcdTdpIndex,
       "atmIfPnniSigVcdTdpValue": atmIfPnniSigVcdTdpValue,
       "atmIfPnniSigProvTable": atmIfPnniSigProvTable,
       "atmIfPnniSigProvEntry": atmIfPnniSigProvEntry,
       "atmIfPnniSigVci": atmIfPnniSigVci,
       "atmIfPnniSigAddressConversion": atmIfPnniSigAddressConversion,
       "atmIfPnniSigStateTable": atmIfPnniSigStateTable,
       "atmIfPnniSigStateEntry": atmIfPnniSigStateEntry,
       "atmIfPnniSigAdminState": atmIfPnniSigAdminState,
       "atmIfPnniSigOperationalState": atmIfPnniSigOperationalState,
       "atmIfPnniSigUsageState": atmIfPnniSigUsageState,
       "atmIfPnniSigOperTable": atmIfPnniSigOperTable,
       "atmIfPnniSigOperEntry": atmIfPnniSigOperEntry,
       "atmIfPnniSigLastTxCauseCode": atmIfPnniSigLastTxCauseCode,
       "atmIfPnniSigLastTxDiagCode": atmIfPnniSigLastTxDiagCode,
       "atmIfPnniSigLastRxCauseCode": atmIfPnniSigLastRxCauseCode,
       "atmIfPnniSigLastRxDiagCode": atmIfPnniSigLastRxDiagCode,
       "atmIfPnniSigStatsTable": atmIfPnniSigStatsTable,
       "atmIfPnniSigStatsEntry": atmIfPnniSigStatsEntry,
       "atmIfPnniSigCurrentConnections": atmIfPnniSigCurrentConnections,
       "atmIfPnniSigPeakConnections": atmIfPnniSigPeakConnections,
       "atmIfPnniSigSuccessfulConnections": atmIfPnniSigSuccessfulConnections,
       "atmIfPnniSigFailedConnections": atmIfPnniSigFailedConnections,
       "atmIfPnniSigTxPdus": atmIfPnniSigTxPdus,
       "atmIfPnniSigRxPdus": atmIfPnniSigRxPdus,
       "atmIfPnniSigCurrentPmpConnections": atmIfPnniSigCurrentPmpConnections,
       "atmIfPnniSigPeakPmpConnections": atmIfPnniSigPeakPmpConnections,
       "atmIfPnniSigSuccessfulPmpConnections": atmIfPnniSigSuccessfulPmpConnections,
       "atmIfPnniSigFailedPmpConnections": atmIfPnniSigFailedPmpConnections,
       "atmIfPnniSigNewCurrentConnections": atmIfPnniSigNewCurrentConnections,
       "atmIfPnniRcc": atmIfPnniRcc,
       "atmIfPnniRccRowStatusTable": atmIfPnniRccRowStatusTable,
       "atmIfPnniRccRowStatusEntry": atmIfPnniRccRowStatusEntry,
       "atmIfPnniRccRowStatus": atmIfPnniRccRowStatus,
       "atmIfPnniRccComponentName": atmIfPnniRccComponentName,
       "atmIfPnniRccStorageType": atmIfPnniRccStorageType,
       "atmIfPnniRccIndex": atmIfPnniRccIndex,
       "atmIfPnniRccVcd": atmIfPnniRccVcd,
       "atmIfPnniRccVcdRowStatusTable": atmIfPnniRccVcdRowStatusTable,
       "atmIfPnniRccVcdRowStatusEntry": atmIfPnniRccVcdRowStatusEntry,
       "atmIfPnniRccVcdRowStatus": atmIfPnniRccVcdRowStatus,
       "atmIfPnniRccVcdComponentName": atmIfPnniRccVcdComponentName,
       "atmIfPnniRccVcdStorageType": atmIfPnniRccVcdStorageType,
       "atmIfPnniRccVcdIndex": atmIfPnniRccVcdIndex,
       "atmIfPnniRccVcdProvTable": atmIfPnniRccVcdProvTable,
       "atmIfPnniRccVcdProvEntry": atmIfPnniRccVcdProvEntry,
       "atmIfPnniRccVcdTrafficDescType": atmIfPnniRccVcdTrafficDescType,
       "atmIfPnniRccVcdAtmServiceCategory": atmIfPnniRccVcdAtmServiceCategory,
       "atmIfPnniRccVcdQosClass": atmIfPnniRccVcdQosClass,
       "atmIfPnniRccVcdTrafficShaping": atmIfPnniRccVcdTrafficShaping,
       "atmIfPnniRccVcdUnshapedTransmitQueueing": atmIfPnniRccVcdUnshapedTransmitQueueing,
       "atmIfPnniRccVcdUsageParameterControl": atmIfPnniRccVcdUsageParameterControl,
       "atmIfPnniRccVcdTdpTable": atmIfPnniRccVcdTdpTable,
       "atmIfPnniRccVcdTdpEntry": atmIfPnniRccVcdTdpEntry,
       "atmIfPnniRccVcdTdpIndex": atmIfPnniRccVcdTdpIndex,
       "atmIfPnniRccVcdTdpValue": atmIfPnniRccVcdTdpValue,
       "atmIfPnniRccProvTable": atmIfPnniRccProvTable,
       "atmIfPnniRccProvEntry": atmIfPnniRccProvEntry,
       "atmIfPnniRccVci": atmIfPnniRccVci,
       "atmIfPnniRccHlParmsTable": atmIfPnniRccHlParmsTable,
       "atmIfPnniRccHlParmsEntry": atmIfPnniRccHlParmsEntry,
       "atmIfPnniRccHelloHoldDown": atmIfPnniRccHelloHoldDown,
       "atmIfPnniRccHelloInterval": atmIfPnniRccHelloInterval,
       "atmIfPnniRccHelloInactivityFactor": atmIfPnniRccHelloInactivityFactor,
       "atmIfPnniRccStateTable": atmIfPnniRccStateTable,
       "atmIfPnniRccStateEntry": atmIfPnniRccStateEntry,
       "atmIfPnniRccAdminState": atmIfPnniRccAdminState,
       "atmIfPnniRccOperationalState": atmIfPnniRccOperationalState,
       "atmIfPnniRccUsageState": atmIfPnniRccUsageState,
       "atmIfPnniRccOperTable": atmIfPnniRccOperTable,
       "atmIfPnniRccOperEntry": atmIfPnniRccOperEntry,
       "atmIfPnniRccType": atmIfPnniRccType,
       "atmIfPnniRccNegotiatedVersion": atmIfPnniRccNegotiatedVersion,
       "atmIfPnniRccHelloState": atmIfPnniRccHelloState,
       "atmIfPnniRccRemoteNodeId": atmIfPnniRccRemoteNodeId,
       "atmIfPnniRccRemotePortId": atmIfPnniRccRemotePortId,
       "atmIfPnniRccStatsTable": atmIfPnniRccStatsTable,
       "atmIfPnniRccStatsEntry": atmIfPnniRccStatsEntry,
       "atmIfPnniRccHelloPacketsRx": atmIfPnniRccHelloPacketsRx,
       "atmIfPnniRccHelloPacketsTx": atmIfPnniRccHelloPacketsTx,
       "atmIfPnniRccMismatchedHelloPacketsRx": atmIfPnniRccMismatchedHelloPacketsRx,
       "atmIfPnniRccBadHelloPacketsRx": atmIfPnniRccBadHelloPacketsRx,
       "atmIfPnniAddr": atmIfPnniAddr,
       "atmIfPnniAddrRowStatusTable": atmIfPnniAddrRowStatusTable,
       "atmIfPnniAddrRowStatusEntry": atmIfPnniAddrRowStatusEntry,
       "atmIfPnniAddrRowStatus": atmIfPnniAddrRowStatus,
       "atmIfPnniAddrComponentName": atmIfPnniAddrComponentName,
       "atmIfPnniAddrStorageType": atmIfPnniAddrStorageType,
       "atmIfPnniAddrAddressIndex": atmIfPnniAddrAddressIndex,
       "atmIfPnniAddrAddressTypeIndex": atmIfPnniAddrAddressTypeIndex,
       "atmIfPnniAddrTermSP": atmIfPnniAddrTermSP,
       "atmIfPnniAddrTermSPRowStatusTable": atmIfPnniAddrTermSPRowStatusTable,
       "atmIfPnniAddrTermSPRowStatusEntry": atmIfPnniAddrTermSPRowStatusEntry,
       "atmIfPnniAddrTermSPRowStatus": atmIfPnniAddrTermSPRowStatus,
       "atmIfPnniAddrTermSPComponentName": atmIfPnniAddrTermSPComponentName,
       "atmIfPnniAddrTermSPStorageType": atmIfPnniAddrTermSPStorageType,
       "atmIfPnniAddrTermSPIndex": atmIfPnniAddrTermSPIndex,
       "atmIfPnniAddrPnniInfo": atmIfPnniAddrPnniInfo,
       "atmIfPnniAddrPnniInfoRowStatusTable": atmIfPnniAddrPnniInfoRowStatusTable,
       "atmIfPnniAddrPnniInfoRowStatusEntry": atmIfPnniAddrPnniInfoRowStatusEntry,
       "atmIfPnniAddrPnniInfoRowStatus": atmIfPnniAddrPnniInfoRowStatus,
       "atmIfPnniAddrPnniInfoComponentName": atmIfPnniAddrPnniInfoComponentName,
       "atmIfPnniAddrPnniInfoStorageType": atmIfPnniAddrPnniInfoStorageType,
       "atmIfPnniAddrPnniInfoIndex": atmIfPnniAddrPnniInfoIndex,
       "atmIfPnniAddrPnniInfoProvTable": atmIfPnniAddrPnniInfoProvTable,
       "atmIfPnniAddrPnniInfoProvEntry": atmIfPnniAddrPnniInfoProvEntry,
       "atmIfPnniAddrPnniInfoScope": atmIfPnniAddrPnniInfoScope,
       "atmIfPnniAddrPnniInfoReachability": atmIfPnniAddrPnniInfoReachability,
       "atmIfPnniAddrOperTable": atmIfPnniAddrOperTable,
       "atmIfPnniAddrOperEntry": atmIfPnniAddrOperEntry,
       "atmIfPnniAddrScope": atmIfPnniAddrScope,
       "atmIfPnniAddrReachability": atmIfPnniAddrReachability,
       "atmIfPnniProvTable": atmIfPnniProvTable,
       "atmIfPnniProvEntry": atmIfPnniProvEntry,
       "atmIfPnniSoftPvcRetryPeriod": atmIfPnniSoftPvcRetryPeriod,
       "atmIfPnniSoftPvpAndPvcRetryPeriod": atmIfPnniSoftPvpAndPvcRetryPeriod,
       "atmIfPnniSoftPvpAndPvcHoldOffTime": atmIfPnniSoftPvpAndPvcHoldOffTime,
       "atmIfPnniAdminWeightsTable": atmIfPnniAdminWeightsTable,
       "atmIfPnniAdminWeightsEntry": atmIfPnniAdminWeightsEntry,
       "atmIfPnniCbrWeight": atmIfPnniCbrWeight,
       "atmIfPnniRtVbrWeight": atmIfPnniRtVbrWeight,
       "atmIfPnniNrtVbrWeight": atmIfPnniNrtVbrWeight,
       "atmIfPnniUbrWeight": atmIfPnniUbrWeight,
       "atmIfPnniAcctOptTable": atmIfPnniAcctOptTable,
       "atmIfPnniAcctOptEntry": atmIfPnniAcctOptEntry,
       "atmIfPnniAccountCollection": atmIfPnniAccountCollection,
       "atmIfPnniAccountConnectionType": atmIfPnniAccountConnectionType,
       "atmIfPnniAccountClass": atmIfPnniAccountClass,
       "atmIfPnniServiceExchange": atmIfPnniServiceExchange,
       "atmIfPnniOperationalTable": atmIfPnniOperationalTable,
       "atmIfPnniOperationalEntry": atmIfPnniOperationalEntry,
       "atmIfPnniPortId": atmIfPnniPortId,
       "atmPnniMIB": atmPnniMIB,
       "atmPnniGroup": atmPnniGroup,
       "atmPnniGroupBE": atmPnniGroupBE,
       "atmPnniGroupBE00": atmPnniGroupBE00,
       "atmPnniGroupBE00A": atmPnniGroupBE00A,
       "atmPnniCapabilities": atmPnniCapabilities,
       "atmPnniCapabilitiesBE": atmPnniCapabilitiesBE,
       "atmPnniCapabilitiesBE00": atmPnniCapabilitiesBE00,
       "atmPnniCapabilitiesBE00A": atmPnniCapabilitiesBE00A}
)
