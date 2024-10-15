# SNMP MIB module (Nortel-Magellan-Passport-GeneralVcInterfaceMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-Magellan-Passport-GeneralVcInterfaceMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:30:52 2024
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

(Counter32,
 DisplayString,
 Gauge32,
 Integer32,
 InterfaceIndex,
 RowPointer,
 RowStatus,
 StorageType,
 Unsigned32) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-StandardTextualConventionsMIB",
    "Counter32",
    "DisplayString",
    "Gauge32",
    "Integer32",
    "InterfaceIndex",
    "RowPointer",
    "RowStatus",
    "StorageType",
    "Unsigned32")

(AsciiString,
 DashedHexString,
 DigitString,
 EnterpriseDateAndTime,
 Hex,
 HexString,
 Link,
 NonReplicated) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-TextualConventionsMIB",
    "AsciiString",
    "DashedHexString",
    "DigitString",
    "EnterpriseDateAndTime",
    "Hex",
    "HexString",
    "Link",
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

_GvcIf_ObjectIdentity = ObjectIdentity
gvcIf = _GvcIf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107)
)
_GvcIfRowStatusTable_Object = MibTable
gvcIfRowStatusTable = _GvcIfRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 1)
)
if mibBuilder.loadTexts:
    gvcIfRowStatusTable.setStatus("mandatory")
_GvcIfRowStatusEntry_Object = MibTableRow
gvcIfRowStatusEntry = _GvcIfRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 1, 1)
)
gvcIfRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfIndex"),
)
if mibBuilder.loadTexts:
    gvcIfRowStatusEntry.setStatus("mandatory")
_GvcIfRowStatus_Type = RowStatus
_GvcIfRowStatus_Object = MibTableColumn
gvcIfRowStatus = _GvcIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 1, 1, 1),
    _GvcIfRowStatus_Type()
)
gvcIfRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gvcIfRowStatus.setStatus("mandatory")
_GvcIfComponentName_Type = DisplayString
_GvcIfComponentName_Object = MibTableColumn
gvcIfComponentName = _GvcIfComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 1, 1, 2),
    _GvcIfComponentName_Type()
)
gvcIfComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfComponentName.setStatus("mandatory")
_GvcIfStorageType_Type = StorageType
_GvcIfStorageType_Object = MibTableColumn
gvcIfStorageType = _GvcIfStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 1, 1, 4),
    _GvcIfStorageType_Type()
)
gvcIfStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfStorageType.setStatus("mandatory")


class _GvcIfIndex_Type(Integer32):
    """Custom type gvcIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_GvcIfIndex_Type.__name__ = "Integer32"
_GvcIfIndex_Object = MibTableColumn
gvcIfIndex = _GvcIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 1, 1, 10),
    _GvcIfIndex_Type()
)
gvcIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gvcIfIndex.setStatus("mandatory")
_GvcIfDc_ObjectIdentity = ObjectIdentity
gvcIfDc = _GvcIfDc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 2)
)
_GvcIfDcRowStatusTable_Object = MibTable
gvcIfDcRowStatusTable = _GvcIfDcRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 2, 1)
)
if mibBuilder.loadTexts:
    gvcIfDcRowStatusTable.setStatus("mandatory")
_GvcIfDcRowStatusEntry_Object = MibTableRow
gvcIfDcRowStatusEntry = _GvcIfDcRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 2, 1, 1)
)
gvcIfDcRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfIndex"),
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfDcMacIndex"),
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfDcSapIndex"),
)
if mibBuilder.loadTexts:
    gvcIfDcRowStatusEntry.setStatus("mandatory")
_GvcIfDcRowStatus_Type = RowStatus
_GvcIfDcRowStatus_Object = MibTableColumn
gvcIfDcRowStatus = _GvcIfDcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 2, 1, 1, 1),
    _GvcIfDcRowStatus_Type()
)
gvcIfDcRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gvcIfDcRowStatus.setStatus("mandatory")
_GvcIfDcComponentName_Type = DisplayString
_GvcIfDcComponentName_Object = MibTableColumn
gvcIfDcComponentName = _GvcIfDcComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 2, 1, 1, 2),
    _GvcIfDcComponentName_Type()
)
gvcIfDcComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfDcComponentName.setStatus("mandatory")
_GvcIfDcStorageType_Type = StorageType
_GvcIfDcStorageType_Object = MibTableColumn
gvcIfDcStorageType = _GvcIfDcStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 2, 1, 1, 4),
    _GvcIfDcStorageType_Type()
)
gvcIfDcStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfDcStorageType.setStatus("mandatory")


class _GvcIfDcMacIndex_Type(DashedHexString):
    """Custom type gvcIfDcMacIndex based on DashedHexString"""
    subtypeSpec = DashedHexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_GvcIfDcMacIndex_Type.__name__ = "DashedHexString"
_GvcIfDcMacIndex_Object = MibTableColumn
gvcIfDcMacIndex = _GvcIfDcMacIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 2, 1, 1, 10),
    _GvcIfDcMacIndex_Type()
)
gvcIfDcMacIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gvcIfDcMacIndex.setStatus("mandatory")


class _GvcIfDcSapIndex_Type(Integer32):
    """Custom type gvcIfDcSapIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 254),
    )


_GvcIfDcSapIndex_Type.__name__ = "Integer32"
_GvcIfDcSapIndex_Object = MibTableColumn
gvcIfDcSapIndex = _GvcIfDcSapIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 2, 1, 1, 11),
    _GvcIfDcSapIndex_Type()
)
gvcIfDcSapIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gvcIfDcSapIndex.setStatus("mandatory")
_GvcIfDcOptionsTable_Object = MibTable
gvcIfDcOptionsTable = _GvcIfDcOptionsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 2, 10)
)
if mibBuilder.loadTexts:
    gvcIfDcOptionsTable.setStatus("mandatory")
_GvcIfDcOptionsEntry_Object = MibTableRow
gvcIfDcOptionsEntry = _GvcIfDcOptionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 2, 10, 1)
)
gvcIfDcOptionsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfIndex"),
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfDcMacIndex"),
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfDcSapIndex"),
)
if mibBuilder.loadTexts:
    gvcIfDcOptionsEntry.setStatus("mandatory")


class _GvcIfDcRemoteNpi_Type(Integer32):
    """Custom type gvcIfDcRemoteNpi based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("e164", 1),
          ("x121", 0))
    )


_GvcIfDcRemoteNpi_Type.__name__ = "Integer32"
_GvcIfDcRemoteNpi_Object = MibTableColumn
gvcIfDcRemoteNpi = _GvcIfDcRemoteNpi_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 2, 10, 1, 3),
    _GvcIfDcRemoteNpi_Type()
)
gvcIfDcRemoteNpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gvcIfDcRemoteNpi.setStatus("mandatory")


class _GvcIfDcRemoteDna_Type(DigitString):
    """Custom type gvcIfDcRemoteDna based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_GvcIfDcRemoteDna_Type.__name__ = "DigitString"
_GvcIfDcRemoteDna_Object = MibTableColumn
gvcIfDcRemoteDna = _GvcIfDcRemoteDna_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 2, 10, 1, 4),
    _GvcIfDcRemoteDna_Type()
)
gvcIfDcRemoteDna.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gvcIfDcRemoteDna.setStatus("mandatory")


class _GvcIfDcUserData_Type(HexString):
    """Custom type gvcIfDcUserData based on HexString"""
    defaultHexValue = "C3000000"

    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_GvcIfDcUserData_Type.__name__ = "HexString"
_GvcIfDcUserData_Object = MibTableColumn
gvcIfDcUserData = _GvcIfDcUserData_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 2, 10, 1, 8),
    _GvcIfDcUserData_Type()
)
gvcIfDcUserData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gvcIfDcUserData.setStatus("mandatory")


class _GvcIfDcTransferPriority_Type(Integer32):
    """Custom type gvcIfDcTransferPriority based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              9,
              255)
        )
    )
    namedValues = NamedValues(
        *(("high", 9),
          ("normal", 0),
          ("useDnaDefTP", 255))
    )


_GvcIfDcTransferPriority_Type.__name__ = "Integer32"
_GvcIfDcTransferPriority_Object = MibTableColumn
gvcIfDcTransferPriority = _GvcIfDcTransferPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 2, 10, 1, 9),
    _GvcIfDcTransferPriority_Type()
)
gvcIfDcTransferPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gvcIfDcTransferPriority.setStatus("mandatory")


class _GvcIfDcDiscardPriority_Type(Integer32):
    """Custom type gvcIfDcDiscardPriority based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("high", 1),
          ("normal", 0),
          ("useDnaDefPriority", 3))
    )


_GvcIfDcDiscardPriority_Type.__name__ = "Integer32"
_GvcIfDcDiscardPriority_Object = MibTableColumn
gvcIfDcDiscardPriority = _GvcIfDcDiscardPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 2, 10, 1, 10),
    _GvcIfDcDiscardPriority_Type()
)
gvcIfDcDiscardPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gvcIfDcDiscardPriority.setStatus("mandatory")
_GvcIfDcCfaTable_Object = MibTable
gvcIfDcCfaTable = _GvcIfDcCfaTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 2, 490)
)
if mibBuilder.loadTexts:
    gvcIfDcCfaTable.setStatus("mandatory")
_GvcIfDcCfaEntry_Object = MibTableRow
gvcIfDcCfaEntry = _GvcIfDcCfaEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 2, 490, 1)
)
gvcIfDcCfaEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfIndex"),
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfDcMacIndex"),
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfDcSapIndex"),
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfDcCfaIndex"),
)
if mibBuilder.loadTexts:
    gvcIfDcCfaEntry.setStatus("mandatory")


class _GvcIfDcCfaIndex_Type(Integer32):
    """Custom type gvcIfDcCfaIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
        ValueRangeConstraint(3, 3),
        ValueRangeConstraint(4, 4),
        ValueRangeConstraint(9, 9),
        ValueRangeConstraint(66, 66),
        ValueRangeConstraint(67, 67),
        ValueRangeConstraint(68, 68),
        ValueRangeConstraint(71, 71),
        ValueRangeConstraint(72, 72),
        ValueRangeConstraint(73, 73),
        ValueRangeConstraint(196, 196),
        ValueRangeConstraint(198, 198),
    )


_GvcIfDcCfaIndex_Type.__name__ = "Integer32"
_GvcIfDcCfaIndex_Object = MibTableColumn
gvcIfDcCfaIndex = _GvcIfDcCfaIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 2, 490, 1, 1),
    _GvcIfDcCfaIndex_Type()
)
gvcIfDcCfaIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gvcIfDcCfaIndex.setStatus("mandatory")


class _GvcIfDcCfaValue_Type(HexString):
    """Custom type gvcIfDcCfaValue based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_GvcIfDcCfaValue_Type.__name__ = "HexString"
_GvcIfDcCfaValue_Object = MibTableColumn
gvcIfDcCfaValue = _GvcIfDcCfaValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 2, 490, 1, 2),
    _GvcIfDcCfaValue_Type()
)
gvcIfDcCfaValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gvcIfDcCfaValue.setStatus("mandatory")
_GvcIfDcCfaRowStatus_Type = RowStatus
_GvcIfDcCfaRowStatus_Object = MibTableColumn
gvcIfDcCfaRowStatus = _GvcIfDcCfaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 2, 490, 1, 3),
    _GvcIfDcCfaRowStatus_Type()
)
gvcIfDcCfaRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    gvcIfDcCfaRowStatus.setStatus("mandatory")
_GvcIfRDnaMap_ObjectIdentity = ObjectIdentity
gvcIfRDnaMap = _GvcIfRDnaMap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 3)
)
_GvcIfRDnaMapRowStatusTable_Object = MibTable
gvcIfRDnaMapRowStatusTable = _GvcIfRDnaMapRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 3, 1)
)
if mibBuilder.loadTexts:
    gvcIfRDnaMapRowStatusTable.setStatus("mandatory")
_GvcIfRDnaMapRowStatusEntry_Object = MibTableRow
gvcIfRDnaMapRowStatusEntry = _GvcIfRDnaMapRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 3, 1, 1)
)
gvcIfRDnaMapRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfIndex"),
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfRDnaMapNpiIndex"),
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfRDnaMapDnaIndex"),
)
if mibBuilder.loadTexts:
    gvcIfRDnaMapRowStatusEntry.setStatus("mandatory")
_GvcIfRDnaMapRowStatus_Type = RowStatus
_GvcIfRDnaMapRowStatus_Object = MibTableColumn
gvcIfRDnaMapRowStatus = _GvcIfRDnaMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 3, 1, 1, 1),
    _GvcIfRDnaMapRowStatus_Type()
)
gvcIfRDnaMapRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gvcIfRDnaMapRowStatus.setStatus("mandatory")
_GvcIfRDnaMapComponentName_Type = DisplayString
_GvcIfRDnaMapComponentName_Object = MibTableColumn
gvcIfRDnaMapComponentName = _GvcIfRDnaMapComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 3, 1, 1, 2),
    _GvcIfRDnaMapComponentName_Type()
)
gvcIfRDnaMapComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfRDnaMapComponentName.setStatus("mandatory")
_GvcIfRDnaMapStorageType_Type = StorageType
_GvcIfRDnaMapStorageType_Object = MibTableColumn
gvcIfRDnaMapStorageType = _GvcIfRDnaMapStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 3, 1, 1, 4),
    _GvcIfRDnaMapStorageType_Type()
)
gvcIfRDnaMapStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfRDnaMapStorageType.setStatus("mandatory")


class _GvcIfRDnaMapNpiIndex_Type(Integer32):
    """Custom type gvcIfRDnaMapNpiIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("e164", 1),
          ("x121", 0))
    )


_GvcIfRDnaMapNpiIndex_Type.__name__ = "Integer32"
_GvcIfRDnaMapNpiIndex_Object = MibTableColumn
gvcIfRDnaMapNpiIndex = _GvcIfRDnaMapNpiIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 3, 1, 1, 10),
    _GvcIfRDnaMapNpiIndex_Type()
)
gvcIfRDnaMapNpiIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gvcIfRDnaMapNpiIndex.setStatus("mandatory")


class _GvcIfRDnaMapDnaIndex_Type(DigitString):
    """Custom type gvcIfRDnaMapDnaIndex based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_GvcIfRDnaMapDnaIndex_Type.__name__ = "DigitString"
_GvcIfRDnaMapDnaIndex_Object = MibTableColumn
gvcIfRDnaMapDnaIndex = _GvcIfRDnaMapDnaIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 3, 1, 1, 11),
    _GvcIfRDnaMapDnaIndex_Type()
)
gvcIfRDnaMapDnaIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gvcIfRDnaMapDnaIndex.setStatus("mandatory")
_GvcIfRDnaMapLanAdTable_Object = MibTable
gvcIfRDnaMapLanAdTable = _GvcIfRDnaMapLanAdTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 3, 10)
)
if mibBuilder.loadTexts:
    gvcIfRDnaMapLanAdTable.setStatus("mandatory")
_GvcIfRDnaMapLanAdEntry_Object = MibTableRow
gvcIfRDnaMapLanAdEntry = _GvcIfRDnaMapLanAdEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 3, 10, 1)
)
gvcIfRDnaMapLanAdEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfIndex"),
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfRDnaMapNpiIndex"),
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfRDnaMapDnaIndex"),
)
if mibBuilder.loadTexts:
    gvcIfRDnaMapLanAdEntry.setStatus("mandatory")


class _GvcIfRDnaMapMac_Type(DashedHexString):
    """Custom type gvcIfRDnaMapMac based on DashedHexString"""
    subtypeSpec = DashedHexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_GvcIfRDnaMapMac_Type.__name__ = "DashedHexString"
_GvcIfRDnaMapMac_Object = MibTableColumn
gvcIfRDnaMapMac = _GvcIfRDnaMapMac_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 3, 10, 1, 2),
    _GvcIfRDnaMapMac_Type()
)
gvcIfRDnaMapMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gvcIfRDnaMapMac.setStatus("mandatory")


class _GvcIfRDnaMapSap_Type(Hex):
    """Custom type gvcIfRDnaMapSap based on Hex"""
    defaultValue = 4

    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 254),
    )


_GvcIfRDnaMapSap_Type.__name__ = "Hex"
_GvcIfRDnaMapSap_Object = MibTableColumn
gvcIfRDnaMapSap = _GvcIfRDnaMapSap_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 3, 10, 1, 3),
    _GvcIfRDnaMapSap_Type()
)
gvcIfRDnaMapSap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gvcIfRDnaMapSap.setStatus("mandatory")
_GvcIfLcn_ObjectIdentity = ObjectIdentity
gvcIfLcn = _GvcIfLcn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 4)
)
_GvcIfLcnRowStatusTable_Object = MibTable
gvcIfLcnRowStatusTable = _GvcIfLcnRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 4, 1)
)
if mibBuilder.loadTexts:
    gvcIfLcnRowStatusTable.setStatus("mandatory")
_GvcIfLcnRowStatusEntry_Object = MibTableRow
gvcIfLcnRowStatusEntry = _GvcIfLcnRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 4, 1, 1)
)
gvcIfLcnRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfIndex"),
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfLcnIndex"),
)
if mibBuilder.loadTexts:
    gvcIfLcnRowStatusEntry.setStatus("mandatory")
_GvcIfLcnRowStatus_Type = RowStatus
_GvcIfLcnRowStatus_Object = MibTableColumn
gvcIfLcnRowStatus = _GvcIfLcnRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 4, 1, 1, 1),
    _GvcIfLcnRowStatus_Type()
)
gvcIfLcnRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfLcnRowStatus.setStatus("mandatory")
_GvcIfLcnComponentName_Type = DisplayString
_GvcIfLcnComponentName_Object = MibTableColumn
gvcIfLcnComponentName = _GvcIfLcnComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 4, 1, 1, 2),
    _GvcIfLcnComponentName_Type()
)
gvcIfLcnComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfLcnComponentName.setStatus("mandatory")
_GvcIfLcnStorageType_Type = StorageType
_GvcIfLcnStorageType_Object = MibTableColumn
gvcIfLcnStorageType = _GvcIfLcnStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 4, 1, 1, 4),
    _GvcIfLcnStorageType_Type()
)
gvcIfLcnStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfLcnStorageType.setStatus("mandatory")


class _GvcIfLcnIndex_Type(Integer32):
    """Custom type gvcIfLcnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_GvcIfLcnIndex_Type.__name__ = "Integer32"
_GvcIfLcnIndex_Object = MibTableColumn
gvcIfLcnIndex = _GvcIfLcnIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 4, 1, 1, 10),
    _GvcIfLcnIndex_Type()
)
gvcIfLcnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gvcIfLcnIndex.setStatus("mandatory")
_GvcIfLcnVc_ObjectIdentity = ObjectIdentity
gvcIfLcnVc = _GvcIfLcnVc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 4, 2)
)
_GvcIfLcnVcRowStatusTable_Object = MibTable
gvcIfLcnVcRowStatusTable = _GvcIfLcnVcRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 4, 2, 1)
)
if mibBuilder.loadTexts:
    gvcIfLcnVcRowStatusTable.setStatus("mandatory")
_GvcIfLcnVcRowStatusEntry_Object = MibTableRow
gvcIfLcnVcRowStatusEntry = _GvcIfLcnVcRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 4, 2, 1, 1)
)
gvcIfLcnVcRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfIndex"),
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfLcnIndex"),
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfLcnVcIndex"),
)
if mibBuilder.loadTexts:
    gvcIfLcnVcRowStatusEntry.setStatus("mandatory")
_GvcIfLcnVcRowStatus_Type = RowStatus
_GvcIfLcnVcRowStatus_Object = MibTableColumn
gvcIfLcnVcRowStatus = _GvcIfLcnVcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 4, 2, 1, 1, 1),
    _GvcIfLcnVcRowStatus_Type()
)
gvcIfLcnVcRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfLcnVcRowStatus.setStatus("mandatory")
_GvcIfLcnVcComponentName_Type = DisplayString
_GvcIfLcnVcComponentName_Object = MibTableColumn
gvcIfLcnVcComponentName = _GvcIfLcnVcComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 4, 2, 1, 1, 2),
    _GvcIfLcnVcComponentName_Type()
)
gvcIfLcnVcComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfLcnVcComponentName.setStatus("mandatory")
_GvcIfLcnVcStorageType_Type = StorageType
_GvcIfLcnVcStorageType_Object = MibTableColumn
gvcIfLcnVcStorageType = _GvcIfLcnVcStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 4, 2, 1, 1, 4),
    _GvcIfLcnVcStorageType_Type()
)
gvcIfLcnVcStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfLcnVcStorageType.setStatus("mandatory")
_GvcIfLcnVcIndex_Type = NonReplicated
_GvcIfLcnVcIndex_Object = MibTableColumn
gvcIfLcnVcIndex = _GvcIfLcnVcIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 4, 2, 1, 1, 10),
    _GvcIfLcnVcIndex_Type()
)
gvcIfLcnVcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gvcIfLcnVcIndex.setStatus("mandatory")
_GvcIfLcnVcCadTable_Object = MibTable
gvcIfLcnVcCadTable = _GvcIfLcnVcCadTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 4, 2, 10)
)
if mibBuilder.loadTexts:
    gvcIfLcnVcCadTable.setStatus("mandatory")
_GvcIfLcnVcCadEntry_Object = MibTableRow
gvcIfLcnVcCadEntry = _GvcIfLcnVcCadEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 4, 2, 10, 1)
)
gvcIfLcnVcCadEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfIndex"),
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfLcnIndex"),
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfLcnVcIndex"),
)
if mibBuilder.loadTexts:
    gvcIfLcnVcCadEntry.setStatus("mandatory")


class _GvcIfLcnVcType_Type(Integer32):
    """Custom type gvcIfLcnVcType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("pvc", 1),
          ("svc", 0))
    )


_GvcIfLcnVcType_Type.__name__ = "Integer32"
_GvcIfLcnVcType_Object = MibTableColumn
gvcIfLcnVcType = _GvcIfLcnVcType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 4, 2, 10, 1, 1),
    _GvcIfLcnVcType_Type()
)
gvcIfLcnVcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfLcnVcType.setStatus("mandatory")


class _GvcIfLcnVcState_Type(Integer32):
    """Custom type gvcIfLcnVcState based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("creating", 0),
          ("dataTransferP4", 4),
          ("dceClearIndicationP7", 7),
          ("dceWaitingP3", 3),
          ("dteClearRequestP6", 6),
          ("dteWaitingP2", 2),
          ("readyP1", 1),
          ("termination", 8),
          ("unsupportedP5", 5))
    )


_GvcIfLcnVcState_Type.__name__ = "Integer32"
_GvcIfLcnVcState_Object = MibTableColumn
gvcIfLcnVcState = _GvcIfLcnVcState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 4, 2, 10, 1, 2),
    _GvcIfLcnVcState_Type()
)
gvcIfLcnVcState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfLcnVcState.setStatus("mandatory")


class _GvcIfLcnVcPreviousState_Type(Integer32):
    """Custom type gvcIfLcnVcPreviousState based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("creating", 0),
          ("dataTransferP4", 4),
          ("dceClearIndicationP7", 7),
          ("dceWaitingP3", 3),
          ("dteClearRequestP6", 6),
          ("dteWaitingP2", 2),
          ("readyP1", 1),
          ("termination", 8),
          ("unsupportedP5", 5))
    )


_GvcIfLcnVcPreviousState_Type.__name__ = "Integer32"
_GvcIfLcnVcPreviousState_Object = MibTableColumn
gvcIfLcnVcPreviousState = _GvcIfLcnVcPreviousState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 4, 2, 10, 1, 3),
    _GvcIfLcnVcPreviousState_Type()
)
gvcIfLcnVcPreviousState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfLcnVcPreviousState.setStatus("mandatory")


class _GvcIfLcnVcDiagnosticCode_Type(Unsigned32):
    """Custom type gvcIfLcnVcDiagnosticCode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_GvcIfLcnVcDiagnosticCode_Type.__name__ = "Unsigned32"
_GvcIfLcnVcDiagnosticCode_Object = MibTableColumn
gvcIfLcnVcDiagnosticCode = _GvcIfLcnVcDiagnosticCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 4, 2, 10, 1, 4),
    _GvcIfLcnVcDiagnosticCode_Type()
)
gvcIfLcnVcDiagnosticCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfLcnVcDiagnosticCode.setStatus("mandatory")


class _GvcIfLcnVcPreviousDiagnosticCode_Type(Unsigned32):
    """Custom type gvcIfLcnVcPreviousDiagnosticCode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_GvcIfLcnVcPreviousDiagnosticCode_Type.__name__ = "Unsigned32"
_GvcIfLcnVcPreviousDiagnosticCode_Object = MibTableColumn
gvcIfLcnVcPreviousDiagnosticCode = _GvcIfLcnVcPreviousDiagnosticCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 4, 2, 10, 1, 5),
    _GvcIfLcnVcPreviousDiagnosticCode_Type()
)
gvcIfLcnVcPreviousDiagnosticCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfLcnVcPreviousDiagnosticCode.setStatus("mandatory")


class _GvcIfLcnVcCalledNpi_Type(Integer32):
    """Custom type gvcIfLcnVcCalledNpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("e164", 1),
          ("x121", 0))
    )


_GvcIfLcnVcCalledNpi_Type.__name__ = "Integer32"
_GvcIfLcnVcCalledNpi_Object = MibTableColumn
gvcIfLcnVcCalledNpi = _GvcIfLcnVcCalledNpi_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 4, 2, 10, 1, 6),
    _GvcIfLcnVcCalledNpi_Type()
)
gvcIfLcnVcCalledNpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfLcnVcCalledNpi.setStatus("mandatory")


class _GvcIfLcnVcCalledDna_Type(DigitString):
    """Custom type gvcIfLcnVcCalledDna based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_GvcIfLcnVcCalledDna_Type.__name__ = "DigitString"
_GvcIfLcnVcCalledDna_Object = MibTableColumn
gvcIfLcnVcCalledDna = _GvcIfLcnVcCalledDna_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 4, 2, 10, 1, 7),
    _GvcIfLcnVcCalledDna_Type()
)
gvcIfLcnVcCalledDna.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfLcnVcCalledDna.setStatus("mandatory")


class _GvcIfLcnVcCalledLcn_Type(Unsigned32):
    """Custom type gvcIfLcnVcCalledLcn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_GvcIfLcnVcCalledLcn_Type.__name__ = "Unsigned32"
_GvcIfLcnVcCalledLcn_Object = MibTableColumn
gvcIfLcnVcCalledLcn = _GvcIfLcnVcCalledLcn_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 4, 2, 10, 1, 8),
    _GvcIfLcnVcCalledLcn_Type()
)
gvcIfLcnVcCalledLcn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfLcnVcCalledLcn.setStatus("mandatory")


class _GvcIfLcnVcCallingNpi_Type(Integer32):
    """Custom type gvcIfLcnVcCallingNpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("e164", 1),
          ("x121", 0))
    )


_GvcIfLcnVcCallingNpi_Type.__name__ = "Integer32"
_GvcIfLcnVcCallingNpi_Object = MibTableColumn
gvcIfLcnVcCallingNpi = _GvcIfLcnVcCallingNpi_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 4, 2, 10, 1, 9),
    _GvcIfLcnVcCallingNpi_Type()
)
gvcIfLcnVcCallingNpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfLcnVcCallingNpi.setStatus("mandatory")


class _GvcIfLcnVcCallingDna_Type(DigitString):
    """Custom type gvcIfLcnVcCallingDna based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_GvcIfLcnVcCallingDna_Type.__name__ = "DigitString"
_GvcIfLcnVcCallingDna_Object = MibTableColumn
gvcIfLcnVcCallingDna = _GvcIfLcnVcCallingDna_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 4, 2, 10, 1, 10),
    _GvcIfLcnVcCallingDna_Type()
)
gvcIfLcnVcCallingDna.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfLcnVcCallingDna.setStatus("mandatory")


class _GvcIfLcnVcCallingLcn_Type(Unsigned32):
    """Custom type gvcIfLcnVcCallingLcn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_GvcIfLcnVcCallingLcn_Type.__name__ = "Unsigned32"
_GvcIfLcnVcCallingLcn_Object = MibTableColumn
gvcIfLcnVcCallingLcn = _GvcIfLcnVcCallingLcn_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 4, 2, 10, 1, 11),
    _GvcIfLcnVcCallingLcn_Type()
)
gvcIfLcnVcCallingLcn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfLcnVcCallingLcn.setStatus("mandatory")


class _GvcIfLcnVcAccountingEnabled_Type(Integer32):
    """Custom type gvcIfLcnVcAccountingEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 0))
    )


_GvcIfLcnVcAccountingEnabled_Type.__name__ = "Integer32"
_GvcIfLcnVcAccountingEnabled_Object = MibTableColumn
gvcIfLcnVcAccountingEnabled = _GvcIfLcnVcAccountingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 4, 2, 10, 1, 12),
    _GvcIfLcnVcAccountingEnabled_Type()
)
gvcIfLcnVcAccountingEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfLcnVcAccountingEnabled.setStatus("mandatory")


class _GvcIfLcnVcFastSelectCall_Type(Integer32):
    """Custom type gvcIfLcnVcFastSelectCall based on Integer32"""
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


_GvcIfLcnVcFastSelectCall_Type.__name__ = "Integer32"
_GvcIfLcnVcFastSelectCall_Object = MibTableColumn
gvcIfLcnVcFastSelectCall = _GvcIfLcnVcFastSelectCall_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 4, 2, 10, 1, 13),
    _GvcIfLcnVcFastSelectCall_Type()
)
gvcIfLcnVcFastSelectCall.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfLcnVcFastSelectCall.setStatus("mandatory")


class _GvcIfLcnVcLocalRxPktSize_Type(Integer32):
    """Custom type gvcIfLcnVcLocalRxPktSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("n1024", 10),
          ("n128", 7),
          ("n16", 4),
          ("n2048", 11),
          ("n256", 8),
          ("n32", 5),
          ("n4096", 12),
          ("n512", 9),
          ("n64", 6),
          ("unknown", 0))
    )


_GvcIfLcnVcLocalRxPktSize_Type.__name__ = "Integer32"
_GvcIfLcnVcLocalRxPktSize_Object = MibTableColumn
gvcIfLcnVcLocalRxPktSize = _GvcIfLcnVcLocalRxPktSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 4, 2, 10, 1, 14),
    _GvcIfLcnVcLocalRxPktSize_Type()
)
gvcIfLcnVcLocalRxPktSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfLcnVcLocalRxPktSize.setStatus("mandatory")


class _GvcIfLcnVcLocalTxPktSize_Type(Integer32):
    """Custom type gvcIfLcnVcLocalTxPktSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("n1024", 10),
          ("n128", 7),
          ("n16", 4),
          ("n2048", 11),
          ("n256", 8),
          ("n32", 5),
          ("n4096", 12),
          ("n512", 9),
          ("n64", 6),
          ("unknown", 0))
    )


_GvcIfLcnVcLocalTxPktSize_Type.__name__ = "Integer32"
_GvcIfLcnVcLocalTxPktSize_Object = MibTableColumn
gvcIfLcnVcLocalTxPktSize = _GvcIfLcnVcLocalTxPktSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 4, 2, 10, 1, 15),
    _GvcIfLcnVcLocalTxPktSize_Type()
)
gvcIfLcnVcLocalTxPktSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfLcnVcLocalTxPktSize.setStatus("mandatory")


class _GvcIfLcnVcLocalTxWindowSize_Type(Unsigned32):
    """Custom type gvcIfLcnVcLocalTxWindowSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_GvcIfLcnVcLocalTxWindowSize_Type.__name__ = "Unsigned32"
_GvcIfLcnVcLocalTxWindowSize_Object = MibTableColumn
gvcIfLcnVcLocalTxWindowSize = _GvcIfLcnVcLocalTxWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 4, 2, 10, 1, 16),
    _GvcIfLcnVcLocalTxWindowSize_Type()
)
gvcIfLcnVcLocalTxWindowSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfLcnVcLocalTxWindowSize.setStatus("mandatory")


class _GvcIfLcnVcLocalRxWindowSize_Type(Unsigned32):
    """Custom type gvcIfLcnVcLocalRxWindowSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_GvcIfLcnVcLocalRxWindowSize_Type.__name__ = "Unsigned32"
_GvcIfLcnVcLocalRxWindowSize_Object = MibTableColumn
gvcIfLcnVcLocalRxWindowSize = _GvcIfLcnVcLocalRxWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 4, 2, 10, 1, 17),
    _GvcIfLcnVcLocalRxWindowSize_Type()
)
gvcIfLcnVcLocalRxWindowSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfLcnVcLocalRxWindowSize.setStatus("mandatory")


class _GvcIfLcnVcPathReliability_Type(Integer32):
    """Custom type gvcIfLcnVcPathReliability based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("high", 0),
          ("normal", 1))
    )


_GvcIfLcnVcPathReliability_Type.__name__ = "Integer32"
_GvcIfLcnVcPathReliability_Object = MibTableColumn
gvcIfLcnVcPathReliability = _GvcIfLcnVcPathReliability_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 4, 2, 10, 1, 19),
    _GvcIfLcnVcPathReliability_Type()
)
gvcIfLcnVcPathReliability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfLcnVcPathReliability.setStatus("mandatory")


class _GvcIfLcnVcAccountingEnd_Type(Integer32):
    """Custom type gvcIfLcnVcAccountingEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("calledEnd", 1),
          ("callingEnd", 0))
    )


_GvcIfLcnVcAccountingEnd_Type.__name__ = "Integer32"
_GvcIfLcnVcAccountingEnd_Object = MibTableColumn
gvcIfLcnVcAccountingEnd = _GvcIfLcnVcAccountingEnd_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 4, 2, 10, 1, 20),
    _GvcIfLcnVcAccountingEnd_Type()
)
gvcIfLcnVcAccountingEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfLcnVcAccountingEnd.setStatus("mandatory")


class _GvcIfLcnVcPriority_Type(Integer32):
    """Custom type gvcIfLcnVcPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("high", 1),
          ("normal", 0))
    )


_GvcIfLcnVcPriority_Type.__name__ = "Integer32"
_GvcIfLcnVcPriority_Object = MibTableColumn
gvcIfLcnVcPriority = _GvcIfLcnVcPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 4, 2, 10, 1, 21),
    _GvcIfLcnVcPriority_Type()
)
gvcIfLcnVcPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfLcnVcPriority.setStatus("mandatory")


class _GvcIfLcnVcSegmentSize_Type(Unsigned32):
    """Custom type gvcIfLcnVcSegmentSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_GvcIfLcnVcSegmentSize_Type.__name__ = "Unsigned32"
_GvcIfLcnVcSegmentSize_Object = MibTableColumn
gvcIfLcnVcSegmentSize = _GvcIfLcnVcSegmentSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 4, 2, 10, 1, 22),
    _GvcIfLcnVcSegmentSize_Type()
)
gvcIfLcnVcSegmentSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfLcnVcSegmentSize.setStatus("mandatory")


class _GvcIfLcnVcSubnetTxPktSize_Type(Integer32):
    """Custom type gvcIfLcnVcSubnetTxPktSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("n1024", 10),
          ("n128", 7),
          ("n16", 4),
          ("n2048", 11),
          ("n256", 8),
          ("n32", 5),
          ("n4096", 12),
          ("n512", 9),
          ("n64", 6),
          ("unknown", 0))
    )


_GvcIfLcnVcSubnetTxPktSize_Type.__name__ = "Integer32"
_GvcIfLcnVcSubnetTxPktSize_Object = MibTableColumn
gvcIfLcnVcSubnetTxPktSize = _GvcIfLcnVcSubnetTxPktSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 4, 2, 10, 1, 23),
    _GvcIfLcnVcSubnetTxPktSize_Type()
)
gvcIfLcnVcSubnetTxPktSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfLcnVcSubnetTxPktSize.setStatus("mandatory")


class _GvcIfLcnVcSubnetTxWindowSize_Type(Unsigned32):
    """Custom type gvcIfLcnVcSubnetTxWindowSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_GvcIfLcnVcSubnetTxWindowSize_Type.__name__ = "Unsigned32"
_GvcIfLcnVcSubnetTxWindowSize_Object = MibTableColumn
gvcIfLcnVcSubnetTxWindowSize = _GvcIfLcnVcSubnetTxWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 4, 2, 10, 1, 24),
    _GvcIfLcnVcSubnetTxWindowSize_Type()
)
gvcIfLcnVcSubnetTxWindowSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfLcnVcSubnetTxWindowSize.setStatus("mandatory")


class _GvcIfLcnVcSubnetRxPktSize_Type(Integer32):
    """Custom type gvcIfLcnVcSubnetRxPktSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("n1024", 10),
          ("n128", 7),
          ("n16", 4),
          ("n2048", 11),
          ("n256", 8),
          ("n32", 5),
          ("n4096", 12),
          ("n512", 9),
          ("n64", 6),
          ("unknown", 0))
    )


_GvcIfLcnVcSubnetRxPktSize_Type.__name__ = "Integer32"
_GvcIfLcnVcSubnetRxPktSize_Object = MibTableColumn
gvcIfLcnVcSubnetRxPktSize = _GvcIfLcnVcSubnetRxPktSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 4, 2, 10, 1, 25),
    _GvcIfLcnVcSubnetRxPktSize_Type()
)
gvcIfLcnVcSubnetRxPktSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfLcnVcSubnetRxPktSize.setStatus("mandatory")


class _GvcIfLcnVcSubnetRxWindowSize_Type(Unsigned32):
    """Custom type gvcIfLcnVcSubnetRxWindowSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_GvcIfLcnVcSubnetRxWindowSize_Type.__name__ = "Unsigned32"
_GvcIfLcnVcSubnetRxWindowSize_Object = MibTableColumn
gvcIfLcnVcSubnetRxWindowSize = _GvcIfLcnVcSubnetRxWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 4, 2, 10, 1, 26),
    _GvcIfLcnVcSubnetRxWindowSize_Type()
)
gvcIfLcnVcSubnetRxWindowSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfLcnVcSubnetRxWindowSize.setStatus("mandatory")


class _GvcIfLcnVcMaxSubnetPktSize_Type(Unsigned32):
    """Custom type gvcIfLcnVcMaxSubnetPktSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_GvcIfLcnVcMaxSubnetPktSize_Type.__name__ = "Unsigned32"
_GvcIfLcnVcMaxSubnetPktSize_Object = MibTableColumn
gvcIfLcnVcMaxSubnetPktSize = _GvcIfLcnVcMaxSubnetPktSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 4, 2, 10, 1, 27),
    _GvcIfLcnVcMaxSubnetPktSize_Type()
)
gvcIfLcnVcMaxSubnetPktSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfLcnVcMaxSubnetPktSize.setStatus("mandatory")


class _GvcIfLcnVcTransferPriorityToNetwork_Type(Integer32):
    """Custom type gvcIfLcnVcTransferPriorityToNetwork based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              9)
        )
    )
    namedValues = NamedValues(
        *(("high", 9),
          ("normal", 0))
    )


_GvcIfLcnVcTransferPriorityToNetwork_Type.__name__ = "Integer32"
_GvcIfLcnVcTransferPriorityToNetwork_Object = MibTableColumn
gvcIfLcnVcTransferPriorityToNetwork = _GvcIfLcnVcTransferPriorityToNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 4, 2, 10, 1, 28),
    _GvcIfLcnVcTransferPriorityToNetwork_Type()
)
gvcIfLcnVcTransferPriorityToNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfLcnVcTransferPriorityToNetwork.setStatus("mandatory")


class _GvcIfLcnVcTransferPriorityFromNetwork_Type(Integer32):
    """Custom type gvcIfLcnVcTransferPriorityFromNetwork based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              9)
        )
    )
    namedValues = NamedValues(
        *(("high", 9),
          ("normal", 0))
    )


_GvcIfLcnVcTransferPriorityFromNetwork_Type.__name__ = "Integer32"
_GvcIfLcnVcTransferPriorityFromNetwork_Object = MibTableColumn
gvcIfLcnVcTransferPriorityFromNetwork = _GvcIfLcnVcTransferPriorityFromNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 4, 2, 10, 1, 29),
    _GvcIfLcnVcTransferPriorityFromNetwork_Type()
)
gvcIfLcnVcTransferPriorityFromNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfLcnVcTransferPriorityFromNetwork.setStatus("mandatory")
_GvcIfLcnVcIntdTable_Object = MibTable
gvcIfLcnVcIntdTable = _GvcIfLcnVcIntdTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 4, 2, 11)
)
if mibBuilder.loadTexts:
    gvcIfLcnVcIntdTable.setStatus("mandatory")
_GvcIfLcnVcIntdEntry_Object = MibTableRow
gvcIfLcnVcIntdEntry = _GvcIfLcnVcIntdEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 4, 2, 11, 1)
)
gvcIfLcnVcIntdEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfIndex"),
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfLcnIndex"),
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfLcnVcIndex"),
)
if mibBuilder.loadTexts:
    gvcIfLcnVcIntdEntry.setStatus("mandatory")


class _GvcIfLcnVcCallReferenceNumber_Type(Hex):
    """Custom type gvcIfLcnVcCallReferenceNumber based on Hex"""
    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_GvcIfLcnVcCallReferenceNumber_Type.__name__ = "Hex"
_GvcIfLcnVcCallReferenceNumber_Object = MibTableColumn
gvcIfLcnVcCallReferenceNumber = _GvcIfLcnVcCallReferenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 4, 2, 11, 1, 1),
    _GvcIfLcnVcCallReferenceNumber_Type()
)
gvcIfLcnVcCallReferenceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfLcnVcCallReferenceNumber.setStatus("mandatory")


class _GvcIfLcnVcElapsedTimeTillNow_Type(Unsigned32):
    """Custom type gvcIfLcnVcElapsedTimeTillNow based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_GvcIfLcnVcElapsedTimeTillNow_Type.__name__ = "Unsigned32"
_GvcIfLcnVcElapsedTimeTillNow_Object = MibTableColumn
gvcIfLcnVcElapsedTimeTillNow = _GvcIfLcnVcElapsedTimeTillNow_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 4, 2, 11, 1, 2),
    _GvcIfLcnVcElapsedTimeTillNow_Type()
)
gvcIfLcnVcElapsedTimeTillNow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfLcnVcElapsedTimeTillNow.setStatus("mandatory")


class _GvcIfLcnVcSegmentsRx_Type(Unsigned32):
    """Custom type gvcIfLcnVcSegmentsRx based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_GvcIfLcnVcSegmentsRx_Type.__name__ = "Unsigned32"
_GvcIfLcnVcSegmentsRx_Object = MibTableColumn
gvcIfLcnVcSegmentsRx = _GvcIfLcnVcSegmentsRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 4, 2, 11, 1, 3),
    _GvcIfLcnVcSegmentsRx_Type()
)
gvcIfLcnVcSegmentsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfLcnVcSegmentsRx.setStatus("mandatory")


class _GvcIfLcnVcSegmentsSent_Type(Unsigned32):
    """Custom type gvcIfLcnVcSegmentsSent based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_GvcIfLcnVcSegmentsSent_Type.__name__ = "Unsigned32"
_GvcIfLcnVcSegmentsSent_Object = MibTableColumn
gvcIfLcnVcSegmentsSent = _GvcIfLcnVcSegmentsSent_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 4, 2, 11, 1, 4),
    _GvcIfLcnVcSegmentsSent_Type()
)
gvcIfLcnVcSegmentsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfLcnVcSegmentsSent.setStatus("mandatory")


class _GvcIfLcnVcStartTime_Type(EnterpriseDateAndTime):
    """Custom type gvcIfLcnVcStartTime based on EnterpriseDateAndTime"""
    subtypeSpec = EnterpriseDateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(19, 19),
    )


_GvcIfLcnVcStartTime_Type.__name__ = "EnterpriseDateAndTime"
_GvcIfLcnVcStartTime_Object = MibTableColumn
gvcIfLcnVcStartTime = _GvcIfLcnVcStartTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 4, 2, 11, 1, 5),
    _GvcIfLcnVcStartTime_Type()
)
gvcIfLcnVcStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfLcnVcStartTime.setStatus("mandatory")
_GvcIfLcnVcStatsTable_Object = MibTable
gvcIfLcnVcStatsTable = _GvcIfLcnVcStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 4, 2, 12)
)
if mibBuilder.loadTexts:
    gvcIfLcnVcStatsTable.setStatus("mandatory")
_GvcIfLcnVcStatsEntry_Object = MibTableRow
gvcIfLcnVcStatsEntry = _GvcIfLcnVcStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 4, 2, 12, 1)
)
gvcIfLcnVcStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfIndex"),
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfLcnIndex"),
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfLcnVcIndex"),
)
if mibBuilder.loadTexts:
    gvcIfLcnVcStatsEntry.setStatus("mandatory")


class _GvcIfLcnVcAckStackingTimeouts_Type(Unsigned32):
    """Custom type gvcIfLcnVcAckStackingTimeouts based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_GvcIfLcnVcAckStackingTimeouts_Type.__name__ = "Unsigned32"
_GvcIfLcnVcAckStackingTimeouts_Object = MibTableColumn
gvcIfLcnVcAckStackingTimeouts = _GvcIfLcnVcAckStackingTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 4, 2, 12, 1, 1),
    _GvcIfLcnVcAckStackingTimeouts_Type()
)
gvcIfLcnVcAckStackingTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfLcnVcAckStackingTimeouts.setStatus("mandatory")


class _GvcIfLcnVcOutOfRangeFrmFromSubnet_Type(Unsigned32):
    """Custom type gvcIfLcnVcOutOfRangeFrmFromSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_GvcIfLcnVcOutOfRangeFrmFromSubnet_Type.__name__ = "Unsigned32"
_GvcIfLcnVcOutOfRangeFrmFromSubnet_Object = MibTableColumn
gvcIfLcnVcOutOfRangeFrmFromSubnet = _GvcIfLcnVcOutOfRangeFrmFromSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 4, 2, 12, 1, 2),
    _GvcIfLcnVcOutOfRangeFrmFromSubnet_Type()
)
gvcIfLcnVcOutOfRangeFrmFromSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfLcnVcOutOfRangeFrmFromSubnet.setStatus("mandatory")


class _GvcIfLcnVcDuplicatesFromSubnet_Type(Unsigned32):
    """Custom type gvcIfLcnVcDuplicatesFromSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_GvcIfLcnVcDuplicatesFromSubnet_Type.__name__ = "Unsigned32"
_GvcIfLcnVcDuplicatesFromSubnet_Object = MibTableColumn
gvcIfLcnVcDuplicatesFromSubnet = _GvcIfLcnVcDuplicatesFromSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 4, 2, 12, 1, 3),
    _GvcIfLcnVcDuplicatesFromSubnet_Type()
)
gvcIfLcnVcDuplicatesFromSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfLcnVcDuplicatesFromSubnet.setStatus("mandatory")


class _GvcIfLcnVcFrmRetryTimeouts_Type(Unsigned32):
    """Custom type gvcIfLcnVcFrmRetryTimeouts based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_GvcIfLcnVcFrmRetryTimeouts_Type.__name__ = "Unsigned32"
_GvcIfLcnVcFrmRetryTimeouts_Object = MibTableColumn
gvcIfLcnVcFrmRetryTimeouts = _GvcIfLcnVcFrmRetryTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 4, 2, 12, 1, 4),
    _GvcIfLcnVcFrmRetryTimeouts_Type()
)
gvcIfLcnVcFrmRetryTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfLcnVcFrmRetryTimeouts.setStatus("mandatory")


class _GvcIfLcnVcPeakRetryQueueSize_Type(Unsigned32):
    """Custom type gvcIfLcnVcPeakRetryQueueSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_GvcIfLcnVcPeakRetryQueueSize_Type.__name__ = "Unsigned32"
_GvcIfLcnVcPeakRetryQueueSize_Object = MibTableColumn
gvcIfLcnVcPeakRetryQueueSize = _GvcIfLcnVcPeakRetryQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 4, 2, 12, 1, 5),
    _GvcIfLcnVcPeakRetryQueueSize_Type()
)
gvcIfLcnVcPeakRetryQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfLcnVcPeakRetryQueueSize.setStatus("mandatory")


class _GvcIfLcnVcPeakOoSeqQueueSize_Type(Unsigned32):
    """Custom type gvcIfLcnVcPeakOoSeqQueueSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_GvcIfLcnVcPeakOoSeqQueueSize_Type.__name__ = "Unsigned32"
_GvcIfLcnVcPeakOoSeqQueueSize_Object = MibTableColumn
gvcIfLcnVcPeakOoSeqQueueSize = _GvcIfLcnVcPeakOoSeqQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 4, 2, 12, 1, 6),
    _GvcIfLcnVcPeakOoSeqQueueSize_Type()
)
gvcIfLcnVcPeakOoSeqQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfLcnVcPeakOoSeqQueueSize.setStatus("mandatory")


class _GvcIfLcnVcPeakOoSeqFrmForwarded_Type(Unsigned32):
    """Custom type gvcIfLcnVcPeakOoSeqFrmForwarded based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_GvcIfLcnVcPeakOoSeqFrmForwarded_Type.__name__ = "Unsigned32"
_GvcIfLcnVcPeakOoSeqFrmForwarded_Object = MibTableColumn
gvcIfLcnVcPeakOoSeqFrmForwarded = _GvcIfLcnVcPeakOoSeqFrmForwarded_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 4, 2, 12, 1, 7),
    _GvcIfLcnVcPeakOoSeqFrmForwarded_Type()
)
gvcIfLcnVcPeakOoSeqFrmForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfLcnVcPeakOoSeqFrmForwarded.setStatus("mandatory")


class _GvcIfLcnVcPeakStackedAcksRx_Type(Unsigned32):
    """Custom type gvcIfLcnVcPeakStackedAcksRx based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_GvcIfLcnVcPeakStackedAcksRx_Type.__name__ = "Unsigned32"
_GvcIfLcnVcPeakStackedAcksRx_Object = MibTableColumn
gvcIfLcnVcPeakStackedAcksRx = _GvcIfLcnVcPeakStackedAcksRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 4, 2, 12, 1, 8),
    _GvcIfLcnVcPeakStackedAcksRx_Type()
)
gvcIfLcnVcPeakStackedAcksRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfLcnVcPeakStackedAcksRx.setStatus("mandatory")


class _GvcIfLcnVcSubnetRecoveries_Type(Unsigned32):
    """Custom type gvcIfLcnVcSubnetRecoveries based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_GvcIfLcnVcSubnetRecoveries_Type.__name__ = "Unsigned32"
_GvcIfLcnVcSubnetRecoveries_Object = MibTableColumn
gvcIfLcnVcSubnetRecoveries = _GvcIfLcnVcSubnetRecoveries_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 4, 2, 12, 1, 9),
    _GvcIfLcnVcSubnetRecoveries_Type()
)
gvcIfLcnVcSubnetRecoveries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfLcnVcSubnetRecoveries.setStatus("mandatory")


class _GvcIfLcnVcWindowClosuresToSubnet_Type(Unsigned32):
    """Custom type gvcIfLcnVcWindowClosuresToSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_GvcIfLcnVcWindowClosuresToSubnet_Type.__name__ = "Unsigned32"
_GvcIfLcnVcWindowClosuresToSubnet_Object = MibTableColumn
gvcIfLcnVcWindowClosuresToSubnet = _GvcIfLcnVcWindowClosuresToSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 4, 2, 12, 1, 10),
    _GvcIfLcnVcWindowClosuresToSubnet_Type()
)
gvcIfLcnVcWindowClosuresToSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfLcnVcWindowClosuresToSubnet.setStatus("mandatory")


class _GvcIfLcnVcWindowClosuresFromSubnet_Type(Unsigned32):
    """Custom type gvcIfLcnVcWindowClosuresFromSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_GvcIfLcnVcWindowClosuresFromSubnet_Type.__name__ = "Unsigned32"
_GvcIfLcnVcWindowClosuresFromSubnet_Object = MibTableColumn
gvcIfLcnVcWindowClosuresFromSubnet = _GvcIfLcnVcWindowClosuresFromSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 4, 2, 12, 1, 11),
    _GvcIfLcnVcWindowClosuresFromSubnet_Type()
)
gvcIfLcnVcWindowClosuresFromSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfLcnVcWindowClosuresFromSubnet.setStatus("mandatory")


class _GvcIfLcnVcWrTriggers_Type(Unsigned32):
    """Custom type gvcIfLcnVcWrTriggers based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_GvcIfLcnVcWrTriggers_Type.__name__ = "Unsigned32"
_GvcIfLcnVcWrTriggers_Object = MibTableColumn
gvcIfLcnVcWrTriggers = _GvcIfLcnVcWrTriggers_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 4, 2, 12, 1, 12),
    _GvcIfLcnVcWrTriggers_Type()
)
gvcIfLcnVcWrTriggers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfLcnVcWrTriggers.setStatus("mandatory")
_GvcIfLcnStateTable_Object = MibTable
gvcIfLcnStateTable = _GvcIfLcnStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 4, 11)
)
if mibBuilder.loadTexts:
    gvcIfLcnStateTable.setStatus("mandatory")
_GvcIfLcnStateEntry_Object = MibTableRow
gvcIfLcnStateEntry = _GvcIfLcnStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 4, 11, 1)
)
gvcIfLcnStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfIndex"),
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfLcnIndex"),
)
if mibBuilder.loadTexts:
    gvcIfLcnStateEntry.setStatus("mandatory")


class _GvcIfLcnAdminState_Type(Integer32):
    """Custom type gvcIfLcnAdminState based on Integer32"""
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


_GvcIfLcnAdminState_Type.__name__ = "Integer32"
_GvcIfLcnAdminState_Object = MibTableColumn
gvcIfLcnAdminState = _GvcIfLcnAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 4, 11, 1, 1),
    _GvcIfLcnAdminState_Type()
)
gvcIfLcnAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfLcnAdminState.setStatus("mandatory")


class _GvcIfLcnOperationalState_Type(Integer32):
    """Custom type gvcIfLcnOperationalState based on Integer32"""
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


_GvcIfLcnOperationalState_Type.__name__ = "Integer32"
_GvcIfLcnOperationalState_Object = MibTableColumn
gvcIfLcnOperationalState = _GvcIfLcnOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 4, 11, 1, 2),
    _GvcIfLcnOperationalState_Type()
)
gvcIfLcnOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfLcnOperationalState.setStatus("mandatory")


class _GvcIfLcnUsageState_Type(Integer32):
    """Custom type gvcIfLcnUsageState based on Integer32"""
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


_GvcIfLcnUsageState_Type.__name__ = "Integer32"
_GvcIfLcnUsageState_Object = MibTableColumn
gvcIfLcnUsageState = _GvcIfLcnUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 4, 11, 1, 3),
    _GvcIfLcnUsageState_Type()
)
gvcIfLcnUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfLcnUsageState.setStatus("mandatory")
_GvcIfLcnLcnCIdTable_Object = MibTable
gvcIfLcnLcnCIdTable = _GvcIfLcnLcnCIdTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 4, 12)
)
if mibBuilder.loadTexts:
    gvcIfLcnLcnCIdTable.setStatus("mandatory")
_GvcIfLcnLcnCIdEntry_Object = MibTableRow
gvcIfLcnLcnCIdEntry = _GvcIfLcnLcnCIdEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 4, 12, 1)
)
gvcIfLcnLcnCIdEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfIndex"),
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfLcnIndex"),
)
if mibBuilder.loadTexts:
    gvcIfLcnLcnCIdEntry.setStatus("mandatory")
_GvcIfLcnCircuitId_Type = RowPointer
_GvcIfLcnCircuitId_Object = MibTableColumn
gvcIfLcnCircuitId = _GvcIfLcnCircuitId_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 4, 12, 1, 1),
    _GvcIfLcnCircuitId_Type()
)
gvcIfLcnCircuitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfLcnCircuitId.setStatus("mandatory")
_GvcIfLcnOperTable_Object = MibTable
gvcIfLcnOperTable = _GvcIfLcnOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 4, 13)
)
if mibBuilder.loadTexts:
    gvcIfLcnOperTable.setStatus("mandatory")
_GvcIfLcnOperEntry_Object = MibTableRow
gvcIfLcnOperEntry = _GvcIfLcnOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 4, 13, 1)
)
gvcIfLcnOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfIndex"),
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfLcnIndex"),
)
if mibBuilder.loadTexts:
    gvcIfLcnOperEntry.setStatus("mandatory")


class _GvcIfLcnState_Type(Integer32):
    """Custom type gvcIfLcnState based on Integer32"""
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
        *(("callUp", 3),
          ("deviceMonitoring", 8),
          ("deviceMonitoringSuspended", 9),
          ("idle", 0),
          ("localDeviceCalling", 1),
          ("localDeviceClearing", 5),
          ("remoteDeviceCalling", 2),
          ("remoteDeviceClearing", 6),
          ("serviceInitiatedClear", 4),
          ("terminating", 7))
    )


_GvcIfLcnState_Type.__name__ = "Integer32"
_GvcIfLcnState_Object = MibTableColumn
gvcIfLcnState = _GvcIfLcnState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 4, 13, 1, 1),
    _GvcIfLcnState_Type()
)
gvcIfLcnState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfLcnState.setStatus("mandatory")
_GvcIfLcnDnaMap_Type = RowPointer
_GvcIfLcnDnaMap_Object = MibTableColumn
gvcIfLcnDnaMap = _GvcIfLcnDnaMap_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 4, 13, 1, 2),
    _GvcIfLcnDnaMap_Type()
)
gvcIfLcnDnaMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfLcnDnaMap.setStatus("mandatory")


class _GvcIfLcnSourceMac_Type(DashedHexString):
    """Custom type gvcIfLcnSourceMac based on DashedHexString"""
    subtypeSpec = DashedHexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_GvcIfLcnSourceMac_Type.__name__ = "DashedHexString"
_GvcIfLcnSourceMac_Object = MibTableColumn
gvcIfLcnSourceMac = _GvcIfLcnSourceMac_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 4, 13, 1, 3),
    _GvcIfLcnSourceMac_Type()
)
gvcIfLcnSourceMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfLcnSourceMac.setStatus("mandatory")
_GvcIfDna_ObjectIdentity = ObjectIdentity
gvcIfDna = _GvcIfDna_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 5)
)
_GvcIfDnaRowStatusTable_Object = MibTable
gvcIfDnaRowStatusTable = _GvcIfDnaRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 5, 1)
)
if mibBuilder.loadTexts:
    gvcIfDnaRowStatusTable.setStatus("mandatory")
_GvcIfDnaRowStatusEntry_Object = MibTableRow
gvcIfDnaRowStatusEntry = _GvcIfDnaRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 5, 1, 1)
)
gvcIfDnaRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfIndex"),
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfDnaIndex"),
)
if mibBuilder.loadTexts:
    gvcIfDnaRowStatusEntry.setStatus("mandatory")
_GvcIfDnaRowStatus_Type = RowStatus
_GvcIfDnaRowStatus_Object = MibTableColumn
gvcIfDnaRowStatus = _GvcIfDnaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 5, 1, 1, 1),
    _GvcIfDnaRowStatus_Type()
)
gvcIfDnaRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gvcIfDnaRowStatus.setStatus("mandatory")
_GvcIfDnaComponentName_Type = DisplayString
_GvcIfDnaComponentName_Object = MibTableColumn
gvcIfDnaComponentName = _GvcIfDnaComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 5, 1, 1, 2),
    _GvcIfDnaComponentName_Type()
)
gvcIfDnaComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfDnaComponentName.setStatus("mandatory")
_GvcIfDnaStorageType_Type = StorageType
_GvcIfDnaStorageType_Object = MibTableColumn
gvcIfDnaStorageType = _GvcIfDnaStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 5, 1, 1, 4),
    _GvcIfDnaStorageType_Type()
)
gvcIfDnaStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfDnaStorageType.setStatus("mandatory")


class _GvcIfDnaIndex_Type(Integer32):
    """Custom type gvcIfDnaIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_GvcIfDnaIndex_Type.__name__ = "Integer32"
_GvcIfDnaIndex_Object = MibTableColumn
gvcIfDnaIndex = _GvcIfDnaIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 5, 1, 1, 10),
    _GvcIfDnaIndex_Type()
)
gvcIfDnaIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gvcIfDnaIndex.setStatus("mandatory")
_GvcIfDnaCug_ObjectIdentity = ObjectIdentity
gvcIfDnaCug = _GvcIfDnaCug_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 5, 2)
)
_GvcIfDnaCugRowStatusTable_Object = MibTable
gvcIfDnaCugRowStatusTable = _GvcIfDnaCugRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 5, 2, 1)
)
if mibBuilder.loadTexts:
    gvcIfDnaCugRowStatusTable.setStatus("mandatory")
_GvcIfDnaCugRowStatusEntry_Object = MibTableRow
gvcIfDnaCugRowStatusEntry = _GvcIfDnaCugRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 5, 2, 1, 1)
)
gvcIfDnaCugRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfIndex"),
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfDnaIndex"),
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfDnaCugIndex"),
)
if mibBuilder.loadTexts:
    gvcIfDnaCugRowStatusEntry.setStatus("mandatory")
_GvcIfDnaCugRowStatus_Type = RowStatus
_GvcIfDnaCugRowStatus_Object = MibTableColumn
gvcIfDnaCugRowStatus = _GvcIfDnaCugRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 5, 2, 1, 1, 1),
    _GvcIfDnaCugRowStatus_Type()
)
gvcIfDnaCugRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gvcIfDnaCugRowStatus.setStatus("mandatory")
_GvcIfDnaCugComponentName_Type = DisplayString
_GvcIfDnaCugComponentName_Object = MibTableColumn
gvcIfDnaCugComponentName = _GvcIfDnaCugComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 5, 2, 1, 1, 2),
    _GvcIfDnaCugComponentName_Type()
)
gvcIfDnaCugComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfDnaCugComponentName.setStatus("mandatory")
_GvcIfDnaCugStorageType_Type = StorageType
_GvcIfDnaCugStorageType_Object = MibTableColumn
gvcIfDnaCugStorageType = _GvcIfDnaCugStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 5, 2, 1, 1, 4),
    _GvcIfDnaCugStorageType_Type()
)
gvcIfDnaCugStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfDnaCugStorageType.setStatus("mandatory")


class _GvcIfDnaCugIndex_Type(Integer32):
    """Custom type gvcIfDnaCugIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_GvcIfDnaCugIndex_Type.__name__ = "Integer32"
_GvcIfDnaCugIndex_Object = MibTableColumn
gvcIfDnaCugIndex = _GvcIfDnaCugIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 5, 2, 1, 1, 10),
    _GvcIfDnaCugIndex_Type()
)
gvcIfDnaCugIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gvcIfDnaCugIndex.setStatus("mandatory")
_GvcIfDnaCugCugOptionsTable_Object = MibTable
gvcIfDnaCugCugOptionsTable = _GvcIfDnaCugCugOptionsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 5, 2, 10)
)
if mibBuilder.loadTexts:
    gvcIfDnaCugCugOptionsTable.setStatus("mandatory")
_GvcIfDnaCugCugOptionsEntry_Object = MibTableRow
gvcIfDnaCugCugOptionsEntry = _GvcIfDnaCugCugOptionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 5, 2, 10, 1)
)
gvcIfDnaCugCugOptionsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfIndex"),
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfDnaIndex"),
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfDnaCugIndex"),
)
if mibBuilder.loadTexts:
    gvcIfDnaCugCugOptionsEntry.setStatus("mandatory")


class _GvcIfDnaCugType_Type(Integer32):
    """Custom type gvcIfDnaCugType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("international", 1),
          ("national", 0))
    )


_GvcIfDnaCugType_Type.__name__ = "Integer32"
_GvcIfDnaCugType_Object = MibTableColumn
gvcIfDnaCugType = _GvcIfDnaCugType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 5, 2, 10, 1, 1),
    _GvcIfDnaCugType_Type()
)
gvcIfDnaCugType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gvcIfDnaCugType.setStatus("mandatory")


class _GvcIfDnaCugDnic_Type(DigitString):
    """Custom type gvcIfDnaCugDnic based on DigitString"""
    defaultHexValue = "30303030"

    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_GvcIfDnaCugDnic_Type.__name__ = "DigitString"
_GvcIfDnaCugDnic_Object = MibTableColumn
gvcIfDnaCugDnic = _GvcIfDnaCugDnic_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 5, 2, 10, 1, 2),
    _GvcIfDnaCugDnic_Type()
)
gvcIfDnaCugDnic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gvcIfDnaCugDnic.setStatus("mandatory")


class _GvcIfDnaCugInterlockCode_Type(Unsigned32):
    """Custom type gvcIfDnaCugInterlockCode based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_GvcIfDnaCugInterlockCode_Type.__name__ = "Unsigned32"
_GvcIfDnaCugInterlockCode_Object = MibTableColumn
gvcIfDnaCugInterlockCode = _GvcIfDnaCugInterlockCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 5, 2, 10, 1, 3),
    _GvcIfDnaCugInterlockCode_Type()
)
gvcIfDnaCugInterlockCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gvcIfDnaCugInterlockCode.setStatus("mandatory")


class _GvcIfDnaCugPreferential_Type(Integer32):
    """Custom type gvcIfDnaCugPreferential based on Integer32"""
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


_GvcIfDnaCugPreferential_Type.__name__ = "Integer32"
_GvcIfDnaCugPreferential_Object = MibTableColumn
gvcIfDnaCugPreferential = _GvcIfDnaCugPreferential_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 5, 2, 10, 1, 4),
    _GvcIfDnaCugPreferential_Type()
)
gvcIfDnaCugPreferential.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gvcIfDnaCugPreferential.setStatus("mandatory")


class _GvcIfDnaCugOutCalls_Type(Integer32):
    """Custom type gvcIfDnaCugOutCalls based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("allowed", 1),
          ("disallowed", 0))
    )


_GvcIfDnaCugOutCalls_Type.__name__ = "Integer32"
_GvcIfDnaCugOutCalls_Object = MibTableColumn
gvcIfDnaCugOutCalls = _GvcIfDnaCugOutCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 5, 2, 10, 1, 5),
    _GvcIfDnaCugOutCalls_Type()
)
gvcIfDnaCugOutCalls.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gvcIfDnaCugOutCalls.setStatus("mandatory")


class _GvcIfDnaCugIncCalls_Type(Integer32):
    """Custom type gvcIfDnaCugIncCalls based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("allowed", 1),
          ("disallowed", 0))
    )


_GvcIfDnaCugIncCalls_Type.__name__ = "Integer32"
_GvcIfDnaCugIncCalls_Object = MibTableColumn
gvcIfDnaCugIncCalls = _GvcIfDnaCugIncCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 5, 2, 10, 1, 6),
    _GvcIfDnaCugIncCalls_Type()
)
gvcIfDnaCugIncCalls.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gvcIfDnaCugIncCalls.setStatus("mandatory")


class _GvcIfDnaCugPrivileged_Type(Integer32):
    """Custom type gvcIfDnaCugPrivileged based on Integer32"""
    defaultValue = 1

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


_GvcIfDnaCugPrivileged_Type.__name__ = "Integer32"
_GvcIfDnaCugPrivileged_Object = MibTableColumn
gvcIfDnaCugPrivileged = _GvcIfDnaCugPrivileged_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 5, 2, 10, 1, 7),
    _GvcIfDnaCugPrivileged_Type()
)
gvcIfDnaCugPrivileged.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gvcIfDnaCugPrivileged.setStatus("mandatory")
_GvcIfDnaHgM_ObjectIdentity = ObjectIdentity
gvcIfDnaHgM = _GvcIfDnaHgM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 5, 3)
)
_GvcIfDnaHgMRowStatusTable_Object = MibTable
gvcIfDnaHgMRowStatusTable = _GvcIfDnaHgMRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 5, 3, 1)
)
if mibBuilder.loadTexts:
    gvcIfDnaHgMRowStatusTable.setStatus("mandatory")
_GvcIfDnaHgMRowStatusEntry_Object = MibTableRow
gvcIfDnaHgMRowStatusEntry = _GvcIfDnaHgMRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 5, 3, 1, 1)
)
gvcIfDnaHgMRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfIndex"),
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfDnaIndex"),
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfDnaHgMIndex"),
)
if mibBuilder.loadTexts:
    gvcIfDnaHgMRowStatusEntry.setStatus("mandatory")
_GvcIfDnaHgMRowStatus_Type = RowStatus
_GvcIfDnaHgMRowStatus_Object = MibTableColumn
gvcIfDnaHgMRowStatus = _GvcIfDnaHgMRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 5, 3, 1, 1, 1),
    _GvcIfDnaHgMRowStatus_Type()
)
gvcIfDnaHgMRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gvcIfDnaHgMRowStatus.setStatus("mandatory")
_GvcIfDnaHgMComponentName_Type = DisplayString
_GvcIfDnaHgMComponentName_Object = MibTableColumn
gvcIfDnaHgMComponentName = _GvcIfDnaHgMComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 5, 3, 1, 1, 2),
    _GvcIfDnaHgMComponentName_Type()
)
gvcIfDnaHgMComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfDnaHgMComponentName.setStatus("mandatory")
_GvcIfDnaHgMStorageType_Type = StorageType
_GvcIfDnaHgMStorageType_Object = MibTableColumn
gvcIfDnaHgMStorageType = _GvcIfDnaHgMStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 5, 3, 1, 1, 4),
    _GvcIfDnaHgMStorageType_Type()
)
gvcIfDnaHgMStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfDnaHgMStorageType.setStatus("mandatory")
_GvcIfDnaHgMIndex_Type = NonReplicated
_GvcIfDnaHgMIndex_Object = MibTableColumn
gvcIfDnaHgMIndex = _GvcIfDnaHgMIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 5, 3, 1, 1, 10),
    _GvcIfDnaHgMIndex_Type()
)
gvcIfDnaHgMIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gvcIfDnaHgMIndex.setStatus("mandatory")
_GvcIfDnaHgMHgAddr_ObjectIdentity = ObjectIdentity
gvcIfDnaHgMHgAddr = _GvcIfDnaHgMHgAddr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 5, 3, 2)
)
_GvcIfDnaHgMHgAddrRowStatusTable_Object = MibTable
gvcIfDnaHgMHgAddrRowStatusTable = _GvcIfDnaHgMHgAddrRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 5, 3, 2, 1)
)
if mibBuilder.loadTexts:
    gvcIfDnaHgMHgAddrRowStatusTable.setStatus("mandatory")
_GvcIfDnaHgMHgAddrRowStatusEntry_Object = MibTableRow
gvcIfDnaHgMHgAddrRowStatusEntry = _GvcIfDnaHgMHgAddrRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 5, 3, 2, 1, 1)
)
gvcIfDnaHgMHgAddrRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfIndex"),
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfDnaIndex"),
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfDnaHgMIndex"),
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfDnaHgMHgAddrIndex"),
)
if mibBuilder.loadTexts:
    gvcIfDnaHgMHgAddrRowStatusEntry.setStatus("mandatory")
_GvcIfDnaHgMHgAddrRowStatus_Type = RowStatus
_GvcIfDnaHgMHgAddrRowStatus_Object = MibTableColumn
gvcIfDnaHgMHgAddrRowStatus = _GvcIfDnaHgMHgAddrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 5, 3, 2, 1, 1, 1),
    _GvcIfDnaHgMHgAddrRowStatus_Type()
)
gvcIfDnaHgMHgAddrRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gvcIfDnaHgMHgAddrRowStatus.setStatus("mandatory")
_GvcIfDnaHgMHgAddrComponentName_Type = DisplayString
_GvcIfDnaHgMHgAddrComponentName_Object = MibTableColumn
gvcIfDnaHgMHgAddrComponentName = _GvcIfDnaHgMHgAddrComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 5, 3, 2, 1, 1, 2),
    _GvcIfDnaHgMHgAddrComponentName_Type()
)
gvcIfDnaHgMHgAddrComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfDnaHgMHgAddrComponentName.setStatus("mandatory")
_GvcIfDnaHgMHgAddrStorageType_Type = StorageType
_GvcIfDnaHgMHgAddrStorageType_Object = MibTableColumn
gvcIfDnaHgMHgAddrStorageType = _GvcIfDnaHgMHgAddrStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 5, 3, 2, 1, 1, 4),
    _GvcIfDnaHgMHgAddrStorageType_Type()
)
gvcIfDnaHgMHgAddrStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfDnaHgMHgAddrStorageType.setStatus("mandatory")


class _GvcIfDnaHgMHgAddrIndex_Type(Integer32):
    """Custom type gvcIfDnaHgMHgAddrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_GvcIfDnaHgMHgAddrIndex_Type.__name__ = "Integer32"
_GvcIfDnaHgMHgAddrIndex_Object = MibTableColumn
gvcIfDnaHgMHgAddrIndex = _GvcIfDnaHgMHgAddrIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 5, 3, 2, 1, 1, 10),
    _GvcIfDnaHgMHgAddrIndex_Type()
)
gvcIfDnaHgMHgAddrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gvcIfDnaHgMHgAddrIndex.setStatus("mandatory")
_GvcIfDnaHgMHgAddrAddrTable_Object = MibTable
gvcIfDnaHgMHgAddrAddrTable = _GvcIfDnaHgMHgAddrAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 5, 3, 2, 10)
)
if mibBuilder.loadTexts:
    gvcIfDnaHgMHgAddrAddrTable.setStatus("mandatory")
_GvcIfDnaHgMHgAddrAddrEntry_Object = MibTableRow
gvcIfDnaHgMHgAddrAddrEntry = _GvcIfDnaHgMHgAddrAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 5, 3, 2, 10, 1)
)
gvcIfDnaHgMHgAddrAddrEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfIndex"),
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfDnaIndex"),
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfDnaHgMIndex"),
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfDnaHgMHgAddrIndex"),
)
if mibBuilder.loadTexts:
    gvcIfDnaHgMHgAddrAddrEntry.setStatus("mandatory")


class _GvcIfDnaHgMHgAddrNumberingPlanIndicator_Type(Integer32):
    """Custom type gvcIfDnaHgMHgAddrNumberingPlanIndicator based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("e164", 1),
          ("x121", 0))
    )


_GvcIfDnaHgMHgAddrNumberingPlanIndicator_Type.__name__ = "Integer32"
_GvcIfDnaHgMHgAddrNumberingPlanIndicator_Object = MibTableColumn
gvcIfDnaHgMHgAddrNumberingPlanIndicator = _GvcIfDnaHgMHgAddrNumberingPlanIndicator_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 5, 3, 2, 10, 1, 1),
    _GvcIfDnaHgMHgAddrNumberingPlanIndicator_Type()
)
gvcIfDnaHgMHgAddrNumberingPlanIndicator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gvcIfDnaHgMHgAddrNumberingPlanIndicator.setStatus("mandatory")


class _GvcIfDnaHgMHgAddrDataNetworkAddress_Type(DigitString):
    """Custom type gvcIfDnaHgMHgAddrDataNetworkAddress based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_GvcIfDnaHgMHgAddrDataNetworkAddress_Type.__name__ = "DigitString"
_GvcIfDnaHgMHgAddrDataNetworkAddress_Object = MibTableColumn
gvcIfDnaHgMHgAddrDataNetworkAddress = _GvcIfDnaHgMHgAddrDataNetworkAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 5, 3, 2, 10, 1, 2),
    _GvcIfDnaHgMHgAddrDataNetworkAddress_Type()
)
gvcIfDnaHgMHgAddrDataNetworkAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gvcIfDnaHgMHgAddrDataNetworkAddress.setStatus("mandatory")
_GvcIfDnaHgMIfTable_Object = MibTable
gvcIfDnaHgMIfTable = _GvcIfDnaHgMIfTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 5, 3, 10)
)
if mibBuilder.loadTexts:
    gvcIfDnaHgMIfTable.setStatus("mandatory")
_GvcIfDnaHgMIfEntry_Object = MibTableRow
gvcIfDnaHgMIfEntry = _GvcIfDnaHgMIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 5, 3, 10, 1)
)
gvcIfDnaHgMIfEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfIndex"),
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfDnaIndex"),
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfDnaHgMIndex"),
)
if mibBuilder.loadTexts:
    gvcIfDnaHgMIfEntry.setStatus("mandatory")


class _GvcIfDnaHgMAvailabilityUpdateThreshold_Type(Unsigned32):
    """Custom type gvcIfDnaHgMAvailabilityUpdateThreshold based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_GvcIfDnaHgMAvailabilityUpdateThreshold_Type.__name__ = "Unsigned32"
_GvcIfDnaHgMAvailabilityUpdateThreshold_Object = MibTableColumn
gvcIfDnaHgMAvailabilityUpdateThreshold = _GvcIfDnaHgMAvailabilityUpdateThreshold_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 5, 3, 10, 1, 1),
    _GvcIfDnaHgMAvailabilityUpdateThreshold_Type()
)
gvcIfDnaHgMAvailabilityUpdateThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gvcIfDnaHgMAvailabilityUpdateThreshold.setStatus("mandatory")
_GvcIfDnaHgMOpTable_Object = MibTable
gvcIfDnaHgMOpTable = _GvcIfDnaHgMOpTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 5, 3, 11)
)
if mibBuilder.loadTexts:
    gvcIfDnaHgMOpTable.setStatus("mandatory")
_GvcIfDnaHgMOpEntry_Object = MibTableRow
gvcIfDnaHgMOpEntry = _GvcIfDnaHgMOpEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 5, 3, 11, 1)
)
gvcIfDnaHgMOpEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfIndex"),
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfDnaIndex"),
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfDnaHgMIndex"),
)
if mibBuilder.loadTexts:
    gvcIfDnaHgMOpEntry.setStatus("mandatory")


class _GvcIfDnaHgMAvailabilityDelta_Type(Integer32):
    """Custom type gvcIfDnaHgMAvailabilityDelta based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-4096, 4096),
    )


_GvcIfDnaHgMAvailabilityDelta_Type.__name__ = "Integer32"
_GvcIfDnaHgMAvailabilityDelta_Object = MibTableColumn
gvcIfDnaHgMAvailabilityDelta = _GvcIfDnaHgMAvailabilityDelta_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 5, 3, 11, 1, 3),
    _GvcIfDnaHgMAvailabilityDelta_Type()
)
gvcIfDnaHgMAvailabilityDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfDnaHgMAvailabilityDelta.setStatus("mandatory")


class _GvcIfDnaHgMMaxAvailableLinkStations_Type(Unsigned32):
    """Custom type gvcIfDnaHgMMaxAvailableLinkStations based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_GvcIfDnaHgMMaxAvailableLinkStations_Type.__name__ = "Unsigned32"
_GvcIfDnaHgMMaxAvailableLinkStations_Object = MibTableColumn
gvcIfDnaHgMMaxAvailableLinkStations = _GvcIfDnaHgMMaxAvailableLinkStations_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 5, 3, 11, 1, 4),
    _GvcIfDnaHgMMaxAvailableLinkStations_Type()
)
gvcIfDnaHgMMaxAvailableLinkStations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfDnaHgMMaxAvailableLinkStations.setStatus("mandatory")


class _GvcIfDnaHgMAvailableLinkStations_Type(Unsigned32):
    """Custom type gvcIfDnaHgMAvailableLinkStations based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_GvcIfDnaHgMAvailableLinkStations_Type.__name__ = "Unsigned32"
_GvcIfDnaHgMAvailableLinkStations_Object = MibTableColumn
gvcIfDnaHgMAvailableLinkStations = _GvcIfDnaHgMAvailableLinkStations_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 5, 3, 11, 1, 6),
    _GvcIfDnaHgMAvailableLinkStations_Type()
)
gvcIfDnaHgMAvailableLinkStations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfDnaHgMAvailableLinkStations.setStatus("mandatory")
_GvcIfDnaDdm_ObjectIdentity = ObjectIdentity
gvcIfDnaDdm = _GvcIfDnaDdm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 5, 4)
)
_GvcIfDnaDdmRowStatusTable_Object = MibTable
gvcIfDnaDdmRowStatusTable = _GvcIfDnaDdmRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 5, 4, 1)
)
if mibBuilder.loadTexts:
    gvcIfDnaDdmRowStatusTable.setStatus("mandatory")
_GvcIfDnaDdmRowStatusEntry_Object = MibTableRow
gvcIfDnaDdmRowStatusEntry = _GvcIfDnaDdmRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 5, 4, 1, 1)
)
gvcIfDnaDdmRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfIndex"),
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfDnaIndex"),
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfDnaDdmIndex"),
)
if mibBuilder.loadTexts:
    gvcIfDnaDdmRowStatusEntry.setStatus("mandatory")
_GvcIfDnaDdmRowStatus_Type = RowStatus
_GvcIfDnaDdmRowStatus_Object = MibTableColumn
gvcIfDnaDdmRowStatus = _GvcIfDnaDdmRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 5, 4, 1, 1, 1),
    _GvcIfDnaDdmRowStatus_Type()
)
gvcIfDnaDdmRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gvcIfDnaDdmRowStatus.setStatus("mandatory")
_GvcIfDnaDdmComponentName_Type = DisplayString
_GvcIfDnaDdmComponentName_Object = MibTableColumn
gvcIfDnaDdmComponentName = _GvcIfDnaDdmComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 5, 4, 1, 1, 2),
    _GvcIfDnaDdmComponentName_Type()
)
gvcIfDnaDdmComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfDnaDdmComponentName.setStatus("mandatory")
_GvcIfDnaDdmStorageType_Type = StorageType
_GvcIfDnaDdmStorageType_Object = MibTableColumn
gvcIfDnaDdmStorageType = _GvcIfDnaDdmStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 5, 4, 1, 1, 4),
    _GvcIfDnaDdmStorageType_Type()
)
gvcIfDnaDdmStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfDnaDdmStorageType.setStatus("mandatory")
_GvcIfDnaDdmIndex_Type = NonReplicated
_GvcIfDnaDdmIndex_Object = MibTableColumn
gvcIfDnaDdmIndex = _GvcIfDnaDdmIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 5, 4, 1, 1, 10),
    _GvcIfDnaDdmIndex_Type()
)
gvcIfDnaDdmIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gvcIfDnaDdmIndex.setStatus("mandatory")
_GvcIfDnaDdmLanAdTable_Object = MibTable
gvcIfDnaDdmLanAdTable = _GvcIfDnaDdmLanAdTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 5, 4, 10)
)
if mibBuilder.loadTexts:
    gvcIfDnaDdmLanAdTable.setStatus("mandatory")
_GvcIfDnaDdmLanAdEntry_Object = MibTableRow
gvcIfDnaDdmLanAdEntry = _GvcIfDnaDdmLanAdEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 5, 4, 10, 1)
)
gvcIfDnaDdmLanAdEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfIndex"),
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfDnaIndex"),
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfDnaDdmIndex"),
)
if mibBuilder.loadTexts:
    gvcIfDnaDdmLanAdEntry.setStatus("mandatory")


class _GvcIfDnaDdmMac_Type(DashedHexString):
    """Custom type gvcIfDnaDdmMac based on DashedHexString"""
    subtypeSpec = DashedHexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_GvcIfDnaDdmMac_Type.__name__ = "DashedHexString"
_GvcIfDnaDdmMac_Object = MibTableColumn
gvcIfDnaDdmMac = _GvcIfDnaDdmMac_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 5, 4, 10, 1, 2),
    _GvcIfDnaDdmMac_Type()
)
gvcIfDnaDdmMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gvcIfDnaDdmMac.setStatus("mandatory")


class _GvcIfDnaDdmSap_Type(Hex):
    """Custom type gvcIfDnaDdmSap based on Hex"""
    defaultValue = 4

    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 254),
    )


_GvcIfDnaDdmSap_Type.__name__ = "Hex"
_GvcIfDnaDdmSap_Object = MibTableColumn
gvcIfDnaDdmSap = _GvcIfDnaDdmSap_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 5, 4, 10, 1, 3),
    _GvcIfDnaDdmSap_Type()
)
gvcIfDnaDdmSap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gvcIfDnaDdmSap.setStatus("mandatory")
_GvcIfDnaDdmDmoTable_Object = MibTable
gvcIfDnaDdmDmoTable = _GvcIfDnaDdmDmoTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 5, 4, 11)
)
if mibBuilder.loadTexts:
    gvcIfDnaDdmDmoTable.setStatus("mandatory")
_GvcIfDnaDdmDmoEntry_Object = MibTableRow
gvcIfDnaDdmDmoEntry = _GvcIfDnaDdmDmoEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 5, 4, 11, 1)
)
gvcIfDnaDdmDmoEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfIndex"),
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfDnaIndex"),
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfDnaDdmIndex"),
)
if mibBuilder.loadTexts:
    gvcIfDnaDdmDmoEntry.setStatus("mandatory")


class _GvcIfDnaDdmDeviceMonitoring_Type(Integer32):
    """Custom type gvcIfDnaDdmDeviceMonitoring based on Integer32"""
    defaultValue = 1

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


_GvcIfDnaDdmDeviceMonitoring_Type.__name__ = "Integer32"
_GvcIfDnaDdmDeviceMonitoring_Object = MibTableColumn
gvcIfDnaDdmDeviceMonitoring = _GvcIfDnaDdmDeviceMonitoring_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 5, 4, 11, 1, 1),
    _GvcIfDnaDdmDeviceMonitoring_Type()
)
gvcIfDnaDdmDeviceMonitoring.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gvcIfDnaDdmDeviceMonitoring.setStatus("mandatory")


class _GvcIfDnaDdmClearVcsWhenUnreachable_Type(Integer32):
    """Custom type gvcIfDnaDdmClearVcsWhenUnreachable based on Integer32"""
    defaultValue = 1

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


_GvcIfDnaDdmClearVcsWhenUnreachable_Type.__name__ = "Integer32"
_GvcIfDnaDdmClearVcsWhenUnreachable_Object = MibTableColumn
gvcIfDnaDdmClearVcsWhenUnreachable = _GvcIfDnaDdmClearVcsWhenUnreachable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 5, 4, 11, 1, 2),
    _GvcIfDnaDdmClearVcsWhenUnreachable_Type()
)
gvcIfDnaDdmClearVcsWhenUnreachable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gvcIfDnaDdmClearVcsWhenUnreachable.setStatus("mandatory")


class _GvcIfDnaDdmDeviceMonitoringTimer_Type(Unsigned32):
    """Custom type gvcIfDnaDdmDeviceMonitoringTimer based on Unsigned32"""
    defaultValue = 15

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_GvcIfDnaDdmDeviceMonitoringTimer_Type.__name__ = "Unsigned32"
_GvcIfDnaDdmDeviceMonitoringTimer_Object = MibTableColumn
gvcIfDnaDdmDeviceMonitoringTimer = _GvcIfDnaDdmDeviceMonitoringTimer_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 5, 4, 11, 1, 3),
    _GvcIfDnaDdmDeviceMonitoringTimer_Type()
)
gvcIfDnaDdmDeviceMonitoringTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gvcIfDnaDdmDeviceMonitoringTimer.setStatus("mandatory")


class _GvcIfDnaDdmTestResponseTimer_Type(Unsigned32):
    """Custom type gvcIfDnaDdmTestResponseTimer based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_GvcIfDnaDdmTestResponseTimer_Type.__name__ = "Unsigned32"
_GvcIfDnaDdmTestResponseTimer_Object = MibTableColumn
gvcIfDnaDdmTestResponseTimer = _GvcIfDnaDdmTestResponseTimer_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 5, 4, 11, 1, 4),
    _GvcIfDnaDdmTestResponseTimer_Type()
)
gvcIfDnaDdmTestResponseTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gvcIfDnaDdmTestResponseTimer.setStatus("mandatory")


class _GvcIfDnaDdmMaximumTestRetry_Type(Unsigned32):
    """Custom type gvcIfDnaDdmMaximumTestRetry based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_GvcIfDnaDdmMaximumTestRetry_Type.__name__ = "Unsigned32"
_GvcIfDnaDdmMaximumTestRetry_Object = MibTableColumn
gvcIfDnaDdmMaximumTestRetry = _GvcIfDnaDdmMaximumTestRetry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 5, 4, 11, 1, 5),
    _GvcIfDnaDdmMaximumTestRetry_Type()
)
gvcIfDnaDdmMaximumTestRetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gvcIfDnaDdmMaximumTestRetry.setStatus("mandatory")
_GvcIfDnaDdmDevOpTable_Object = MibTable
gvcIfDnaDdmDevOpTable = _GvcIfDnaDdmDevOpTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 5, 4, 12)
)
if mibBuilder.loadTexts:
    gvcIfDnaDdmDevOpTable.setStatus("mandatory")
_GvcIfDnaDdmDevOpEntry_Object = MibTableRow
gvcIfDnaDdmDevOpEntry = _GvcIfDnaDdmDevOpEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 5, 4, 12, 1)
)
gvcIfDnaDdmDevOpEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfIndex"),
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfDnaIndex"),
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfDnaDdmIndex"),
)
if mibBuilder.loadTexts:
    gvcIfDnaDdmDevOpEntry.setStatus("mandatory")


class _GvcIfDnaDdmDeviceStatus_Type(Integer32):
    """Custom type gvcIfDnaDdmDeviceStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("reachable", 1),
          ("unreachable", 0))
    )


_GvcIfDnaDdmDeviceStatus_Type.__name__ = "Integer32"
_GvcIfDnaDdmDeviceStatus_Object = MibTableColumn
gvcIfDnaDdmDeviceStatus = _GvcIfDnaDdmDeviceStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 5, 4, 12, 1, 1),
    _GvcIfDnaDdmDeviceStatus_Type()
)
gvcIfDnaDdmDeviceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfDnaDdmDeviceStatus.setStatus("mandatory")


class _GvcIfDnaDdmActiveLinkStations_Type(Unsigned32):
    """Custom type gvcIfDnaDdmActiveLinkStations based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_GvcIfDnaDdmActiveLinkStations_Type.__name__ = "Unsigned32"
_GvcIfDnaDdmActiveLinkStations_Object = MibTableColumn
gvcIfDnaDdmActiveLinkStations = _GvcIfDnaDdmActiveLinkStations_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 5, 4, 12, 1, 2),
    _GvcIfDnaDdmActiveLinkStations_Type()
)
gvcIfDnaDdmActiveLinkStations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfDnaDdmActiveLinkStations.setStatus("mandatory")


class _GvcIfDnaDdmLastTimeUnreachable_Type(EnterpriseDateAndTime):
    """Custom type gvcIfDnaDdmLastTimeUnreachable based on EnterpriseDateAndTime"""
    subtypeSpec = EnterpriseDateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(19, 19),
    )


_GvcIfDnaDdmLastTimeUnreachable_Type.__name__ = "EnterpriseDateAndTime"
_GvcIfDnaDdmLastTimeUnreachable_Object = MibTableColumn
gvcIfDnaDdmLastTimeUnreachable = _GvcIfDnaDdmLastTimeUnreachable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 5, 4, 12, 1, 3),
    _GvcIfDnaDdmLastTimeUnreachable_Type()
)
gvcIfDnaDdmLastTimeUnreachable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfDnaDdmLastTimeUnreachable.setStatus("mandatory")


class _GvcIfDnaDdmLastTimeReachable_Type(EnterpriseDateAndTime):
    """Custom type gvcIfDnaDdmLastTimeReachable based on EnterpriseDateAndTime"""
    subtypeSpec = EnterpriseDateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(19, 19),
    )


_GvcIfDnaDdmLastTimeReachable_Type.__name__ = "EnterpriseDateAndTime"
_GvcIfDnaDdmLastTimeReachable_Object = MibTableColumn
gvcIfDnaDdmLastTimeReachable = _GvcIfDnaDdmLastTimeReachable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 5, 4, 12, 1, 4),
    _GvcIfDnaDdmLastTimeReachable_Type()
)
gvcIfDnaDdmLastTimeReachable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfDnaDdmLastTimeReachable.setStatus("mandatory")
_GvcIfDnaDdmDeviceUnreachable_Type = Counter32
_GvcIfDnaDdmDeviceUnreachable_Object = MibTableColumn
gvcIfDnaDdmDeviceUnreachable = _GvcIfDnaDdmDeviceUnreachable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 5, 4, 12, 1, 5),
    _GvcIfDnaDdmDeviceUnreachable_Type()
)
gvcIfDnaDdmDeviceUnreachable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfDnaDdmDeviceUnreachable.setStatus("mandatory")


class _GvcIfDnaDdmMonitoringLcn_Type(Integer32):
    """Custom type gvcIfDnaDdmMonitoringLcn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_GvcIfDnaDdmMonitoringLcn_Type.__name__ = "Integer32"
_GvcIfDnaDdmMonitoringLcn_Object = MibTableColumn
gvcIfDnaDdmMonitoringLcn = _GvcIfDnaDdmMonitoringLcn_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 5, 4, 12, 1, 6),
    _GvcIfDnaDdmMonitoringLcn_Type()
)
gvcIfDnaDdmMonitoringLcn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfDnaDdmMonitoringLcn.setStatus("mandatory")
_GvcIfDnaSdm_ObjectIdentity = ObjectIdentity
gvcIfDnaSdm = _GvcIfDnaSdm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 5, 5)
)
_GvcIfDnaSdmRowStatusTable_Object = MibTable
gvcIfDnaSdmRowStatusTable = _GvcIfDnaSdmRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 5, 5, 1)
)
if mibBuilder.loadTexts:
    gvcIfDnaSdmRowStatusTable.setStatus("mandatory")
_GvcIfDnaSdmRowStatusEntry_Object = MibTableRow
gvcIfDnaSdmRowStatusEntry = _GvcIfDnaSdmRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 5, 5, 1, 1)
)
gvcIfDnaSdmRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfIndex"),
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfDnaIndex"),
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfDnaSdmIndex"),
)
if mibBuilder.loadTexts:
    gvcIfDnaSdmRowStatusEntry.setStatus("mandatory")
_GvcIfDnaSdmRowStatus_Type = RowStatus
_GvcIfDnaSdmRowStatus_Object = MibTableColumn
gvcIfDnaSdmRowStatus = _GvcIfDnaSdmRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 5, 5, 1, 1, 1),
    _GvcIfDnaSdmRowStatus_Type()
)
gvcIfDnaSdmRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gvcIfDnaSdmRowStatus.setStatus("mandatory")
_GvcIfDnaSdmComponentName_Type = DisplayString
_GvcIfDnaSdmComponentName_Object = MibTableColumn
gvcIfDnaSdmComponentName = _GvcIfDnaSdmComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 5, 5, 1, 1, 2),
    _GvcIfDnaSdmComponentName_Type()
)
gvcIfDnaSdmComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfDnaSdmComponentName.setStatus("mandatory")
_GvcIfDnaSdmStorageType_Type = StorageType
_GvcIfDnaSdmStorageType_Object = MibTableColumn
gvcIfDnaSdmStorageType = _GvcIfDnaSdmStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 5, 5, 1, 1, 4),
    _GvcIfDnaSdmStorageType_Type()
)
gvcIfDnaSdmStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfDnaSdmStorageType.setStatus("mandatory")


class _GvcIfDnaSdmIndex_Type(DigitString):
    """Custom type gvcIfDnaSdmIndex based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_GvcIfDnaSdmIndex_Type.__name__ = "DigitString"
_GvcIfDnaSdmIndex_Object = MibTableColumn
gvcIfDnaSdmIndex = _GvcIfDnaSdmIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 5, 5, 1, 1, 10),
    _GvcIfDnaSdmIndex_Type()
)
gvcIfDnaSdmIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gvcIfDnaSdmIndex.setStatus("mandatory")
_GvcIfDnaSdmLanAdTable_Object = MibTable
gvcIfDnaSdmLanAdTable = _GvcIfDnaSdmLanAdTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 5, 5, 10)
)
if mibBuilder.loadTexts:
    gvcIfDnaSdmLanAdTable.setStatus("mandatory")
_GvcIfDnaSdmLanAdEntry_Object = MibTableRow
gvcIfDnaSdmLanAdEntry = _GvcIfDnaSdmLanAdEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 5, 5, 10, 1)
)
gvcIfDnaSdmLanAdEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfIndex"),
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfDnaIndex"),
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfDnaSdmIndex"),
)
if mibBuilder.loadTexts:
    gvcIfDnaSdmLanAdEntry.setStatus("mandatory")


class _GvcIfDnaSdmMac_Type(DashedHexString):
    """Custom type gvcIfDnaSdmMac based on DashedHexString"""
    subtypeSpec = DashedHexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_GvcIfDnaSdmMac_Type.__name__ = "DashedHexString"
_GvcIfDnaSdmMac_Object = MibTableColumn
gvcIfDnaSdmMac = _GvcIfDnaSdmMac_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 5, 5, 10, 1, 2),
    _GvcIfDnaSdmMac_Type()
)
gvcIfDnaSdmMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gvcIfDnaSdmMac.setStatus("mandatory")


class _GvcIfDnaSdmSap_Type(Hex):
    """Custom type gvcIfDnaSdmSap based on Hex"""
    defaultValue = 4

    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 254),
    )


_GvcIfDnaSdmSap_Type.__name__ = "Hex"
_GvcIfDnaSdmSap_Object = MibTableColumn
gvcIfDnaSdmSap = _GvcIfDnaSdmSap_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 5, 5, 10, 1, 3),
    _GvcIfDnaSdmSap_Type()
)
gvcIfDnaSdmSap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gvcIfDnaSdmSap.setStatus("mandatory")
_GvcIfDnaSdmDmoTable_Object = MibTable
gvcIfDnaSdmDmoTable = _GvcIfDnaSdmDmoTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 5, 5, 11)
)
if mibBuilder.loadTexts:
    gvcIfDnaSdmDmoTable.setStatus("mandatory")
_GvcIfDnaSdmDmoEntry_Object = MibTableRow
gvcIfDnaSdmDmoEntry = _GvcIfDnaSdmDmoEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 5, 5, 11, 1)
)
gvcIfDnaSdmDmoEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfIndex"),
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfDnaIndex"),
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfDnaSdmIndex"),
)
if mibBuilder.loadTexts:
    gvcIfDnaSdmDmoEntry.setStatus("mandatory")


class _GvcIfDnaSdmDeviceMonitoring_Type(Integer32):
    """Custom type gvcIfDnaSdmDeviceMonitoring based on Integer32"""
    defaultValue = 1

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


_GvcIfDnaSdmDeviceMonitoring_Type.__name__ = "Integer32"
_GvcIfDnaSdmDeviceMonitoring_Object = MibTableColumn
gvcIfDnaSdmDeviceMonitoring = _GvcIfDnaSdmDeviceMonitoring_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 5, 5, 11, 1, 1),
    _GvcIfDnaSdmDeviceMonitoring_Type()
)
gvcIfDnaSdmDeviceMonitoring.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gvcIfDnaSdmDeviceMonitoring.setStatus("mandatory")


class _GvcIfDnaSdmClearVcsWhenUnreachable_Type(Integer32):
    """Custom type gvcIfDnaSdmClearVcsWhenUnreachable based on Integer32"""
    defaultValue = 1

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


_GvcIfDnaSdmClearVcsWhenUnreachable_Type.__name__ = "Integer32"
_GvcIfDnaSdmClearVcsWhenUnreachable_Object = MibTableColumn
gvcIfDnaSdmClearVcsWhenUnreachable = _GvcIfDnaSdmClearVcsWhenUnreachable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 5, 5, 11, 1, 2),
    _GvcIfDnaSdmClearVcsWhenUnreachable_Type()
)
gvcIfDnaSdmClearVcsWhenUnreachable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gvcIfDnaSdmClearVcsWhenUnreachable.setStatus("mandatory")


class _GvcIfDnaSdmDeviceMonitoringTimer_Type(Unsigned32):
    """Custom type gvcIfDnaSdmDeviceMonitoringTimer based on Unsigned32"""
    defaultValue = 15

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_GvcIfDnaSdmDeviceMonitoringTimer_Type.__name__ = "Unsigned32"
_GvcIfDnaSdmDeviceMonitoringTimer_Object = MibTableColumn
gvcIfDnaSdmDeviceMonitoringTimer = _GvcIfDnaSdmDeviceMonitoringTimer_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 5, 5, 11, 1, 3),
    _GvcIfDnaSdmDeviceMonitoringTimer_Type()
)
gvcIfDnaSdmDeviceMonitoringTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gvcIfDnaSdmDeviceMonitoringTimer.setStatus("mandatory")


class _GvcIfDnaSdmTestResponseTimer_Type(Unsigned32):
    """Custom type gvcIfDnaSdmTestResponseTimer based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_GvcIfDnaSdmTestResponseTimer_Type.__name__ = "Unsigned32"
_GvcIfDnaSdmTestResponseTimer_Object = MibTableColumn
gvcIfDnaSdmTestResponseTimer = _GvcIfDnaSdmTestResponseTimer_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 5, 5, 11, 1, 4),
    _GvcIfDnaSdmTestResponseTimer_Type()
)
gvcIfDnaSdmTestResponseTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gvcIfDnaSdmTestResponseTimer.setStatus("mandatory")


class _GvcIfDnaSdmMaximumTestRetry_Type(Unsigned32):
    """Custom type gvcIfDnaSdmMaximumTestRetry based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_GvcIfDnaSdmMaximumTestRetry_Type.__name__ = "Unsigned32"
_GvcIfDnaSdmMaximumTestRetry_Object = MibTableColumn
gvcIfDnaSdmMaximumTestRetry = _GvcIfDnaSdmMaximumTestRetry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 5, 5, 11, 1, 5),
    _GvcIfDnaSdmMaximumTestRetry_Type()
)
gvcIfDnaSdmMaximumTestRetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gvcIfDnaSdmMaximumTestRetry.setStatus("mandatory")
_GvcIfDnaSdmDevOpTable_Object = MibTable
gvcIfDnaSdmDevOpTable = _GvcIfDnaSdmDevOpTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 5, 5, 12)
)
if mibBuilder.loadTexts:
    gvcIfDnaSdmDevOpTable.setStatus("mandatory")
_GvcIfDnaSdmDevOpEntry_Object = MibTableRow
gvcIfDnaSdmDevOpEntry = _GvcIfDnaSdmDevOpEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 5, 5, 12, 1)
)
gvcIfDnaSdmDevOpEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfIndex"),
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfDnaIndex"),
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfDnaSdmIndex"),
)
if mibBuilder.loadTexts:
    gvcIfDnaSdmDevOpEntry.setStatus("mandatory")


class _GvcIfDnaSdmDeviceStatus_Type(Integer32):
    """Custom type gvcIfDnaSdmDeviceStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("reachable", 1),
          ("unreachable", 0))
    )


_GvcIfDnaSdmDeviceStatus_Type.__name__ = "Integer32"
_GvcIfDnaSdmDeviceStatus_Object = MibTableColumn
gvcIfDnaSdmDeviceStatus = _GvcIfDnaSdmDeviceStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 5, 5, 12, 1, 1),
    _GvcIfDnaSdmDeviceStatus_Type()
)
gvcIfDnaSdmDeviceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfDnaSdmDeviceStatus.setStatus("mandatory")


class _GvcIfDnaSdmActiveLinkStations_Type(Unsigned32):
    """Custom type gvcIfDnaSdmActiveLinkStations based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_GvcIfDnaSdmActiveLinkStations_Type.__name__ = "Unsigned32"
_GvcIfDnaSdmActiveLinkStations_Object = MibTableColumn
gvcIfDnaSdmActiveLinkStations = _GvcIfDnaSdmActiveLinkStations_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 5, 5, 12, 1, 2),
    _GvcIfDnaSdmActiveLinkStations_Type()
)
gvcIfDnaSdmActiveLinkStations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfDnaSdmActiveLinkStations.setStatus("mandatory")


class _GvcIfDnaSdmLastTimeUnreachable_Type(EnterpriseDateAndTime):
    """Custom type gvcIfDnaSdmLastTimeUnreachable based on EnterpriseDateAndTime"""
    subtypeSpec = EnterpriseDateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(19, 19),
    )


_GvcIfDnaSdmLastTimeUnreachable_Type.__name__ = "EnterpriseDateAndTime"
_GvcIfDnaSdmLastTimeUnreachable_Object = MibTableColumn
gvcIfDnaSdmLastTimeUnreachable = _GvcIfDnaSdmLastTimeUnreachable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 5, 5, 12, 1, 3),
    _GvcIfDnaSdmLastTimeUnreachable_Type()
)
gvcIfDnaSdmLastTimeUnreachable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfDnaSdmLastTimeUnreachable.setStatus("mandatory")


class _GvcIfDnaSdmLastTimeReachable_Type(EnterpriseDateAndTime):
    """Custom type gvcIfDnaSdmLastTimeReachable based on EnterpriseDateAndTime"""
    subtypeSpec = EnterpriseDateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(19, 19),
    )


_GvcIfDnaSdmLastTimeReachable_Type.__name__ = "EnterpriseDateAndTime"
_GvcIfDnaSdmLastTimeReachable_Object = MibTableColumn
gvcIfDnaSdmLastTimeReachable = _GvcIfDnaSdmLastTimeReachable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 5, 5, 12, 1, 4),
    _GvcIfDnaSdmLastTimeReachable_Type()
)
gvcIfDnaSdmLastTimeReachable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfDnaSdmLastTimeReachable.setStatus("mandatory")
_GvcIfDnaSdmDeviceUnreachable_Type = Counter32
_GvcIfDnaSdmDeviceUnreachable_Object = MibTableColumn
gvcIfDnaSdmDeviceUnreachable = _GvcIfDnaSdmDeviceUnreachable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 5, 5, 12, 1, 5),
    _GvcIfDnaSdmDeviceUnreachable_Type()
)
gvcIfDnaSdmDeviceUnreachable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfDnaSdmDeviceUnreachable.setStatus("mandatory")


class _GvcIfDnaSdmMonitoringLcn_Type(Integer32):
    """Custom type gvcIfDnaSdmMonitoringLcn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_GvcIfDnaSdmMonitoringLcn_Type.__name__ = "Integer32"
_GvcIfDnaSdmMonitoringLcn_Object = MibTableColumn
gvcIfDnaSdmMonitoringLcn = _GvcIfDnaSdmMonitoringLcn_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 5, 5, 12, 1, 6),
    _GvcIfDnaSdmMonitoringLcn_Type()
)
gvcIfDnaSdmMonitoringLcn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfDnaSdmMonitoringLcn.setStatus("mandatory")
_GvcIfDnaAddrTable_Object = MibTable
gvcIfDnaAddrTable = _GvcIfDnaAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 5, 11)
)
if mibBuilder.loadTexts:
    gvcIfDnaAddrTable.setStatus("mandatory")
_GvcIfDnaAddrEntry_Object = MibTableRow
gvcIfDnaAddrEntry = _GvcIfDnaAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 5, 11, 1)
)
gvcIfDnaAddrEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfIndex"),
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfDnaIndex"),
)
if mibBuilder.loadTexts:
    gvcIfDnaAddrEntry.setStatus("mandatory")


class _GvcIfDnaNumberingPlanIndicator_Type(Integer32):
    """Custom type gvcIfDnaNumberingPlanIndicator based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("e164", 1),
          ("x121", 0))
    )


_GvcIfDnaNumberingPlanIndicator_Type.__name__ = "Integer32"
_GvcIfDnaNumberingPlanIndicator_Object = MibTableColumn
gvcIfDnaNumberingPlanIndicator = _GvcIfDnaNumberingPlanIndicator_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 5, 11, 1, 1),
    _GvcIfDnaNumberingPlanIndicator_Type()
)
gvcIfDnaNumberingPlanIndicator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gvcIfDnaNumberingPlanIndicator.setStatus("mandatory")


class _GvcIfDnaDataNetworkAddress_Type(DigitString):
    """Custom type gvcIfDnaDataNetworkAddress based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_GvcIfDnaDataNetworkAddress_Type.__name__ = "DigitString"
_GvcIfDnaDataNetworkAddress_Object = MibTableColumn
gvcIfDnaDataNetworkAddress = _GvcIfDnaDataNetworkAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 5, 11, 1, 2),
    _GvcIfDnaDataNetworkAddress_Type()
)
gvcIfDnaDataNetworkAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gvcIfDnaDataNetworkAddress.setStatus("mandatory")
_GvcIfDnaOutgoingOptionsTable_Object = MibTable
gvcIfDnaOutgoingOptionsTable = _GvcIfDnaOutgoingOptionsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 5, 12)
)
if mibBuilder.loadTexts:
    gvcIfDnaOutgoingOptionsTable.setStatus("mandatory")
_GvcIfDnaOutgoingOptionsEntry_Object = MibTableRow
gvcIfDnaOutgoingOptionsEntry = _GvcIfDnaOutgoingOptionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 5, 12, 1)
)
gvcIfDnaOutgoingOptionsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfIndex"),
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfDnaIndex"),
)
if mibBuilder.loadTexts:
    gvcIfDnaOutgoingOptionsEntry.setStatus("mandatory")


class _GvcIfDnaOutDefaultPriority_Type(Integer32):
    """Custom type gvcIfDnaOutDefaultPriority based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("high", 1),
          ("normal", 0))
    )


_GvcIfDnaOutDefaultPriority_Type.__name__ = "Integer32"
_GvcIfDnaOutDefaultPriority_Object = MibTableColumn
gvcIfDnaOutDefaultPriority = _GvcIfDnaOutDefaultPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 5, 12, 1, 7),
    _GvcIfDnaOutDefaultPriority_Type()
)
gvcIfDnaOutDefaultPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gvcIfDnaOutDefaultPriority.setStatus("mandatory")


class _GvcIfDnaOutDefaultPathSensitivity_Type(Integer32):
    """Custom type gvcIfDnaOutDefaultPathSensitivity based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("delay", 1),
          ("throughput", 0))
    )


_GvcIfDnaOutDefaultPathSensitivity_Type.__name__ = "Integer32"
_GvcIfDnaOutDefaultPathSensitivity_Object = MibTableColumn
gvcIfDnaOutDefaultPathSensitivity = _GvcIfDnaOutDefaultPathSensitivity_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 5, 12, 1, 11),
    _GvcIfDnaOutDefaultPathSensitivity_Type()
)
gvcIfDnaOutDefaultPathSensitivity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gvcIfDnaOutDefaultPathSensitivity.setStatus("mandatory")


class _GvcIfDnaOutDefaultPathReliability_Type(Integer32):
    """Custom type gvcIfDnaOutDefaultPathReliability based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("high", 0),
          ("normal", 1))
    )


_GvcIfDnaOutDefaultPathReliability_Type.__name__ = "Integer32"
_GvcIfDnaOutDefaultPathReliability_Object = MibTableColumn
gvcIfDnaOutDefaultPathReliability = _GvcIfDnaOutDefaultPathReliability_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 5, 12, 1, 14),
    _GvcIfDnaOutDefaultPathReliability_Type()
)
gvcIfDnaOutDefaultPathReliability.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gvcIfDnaOutDefaultPathReliability.setStatus("mandatory")


class _GvcIfDnaOutAccess_Type(Integer32):
    """Custom type gvcIfDnaOutAccess based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("allowed", 1),
          ("disallowed", 0))
    )


_GvcIfDnaOutAccess_Type.__name__ = "Integer32"
_GvcIfDnaOutAccess_Object = MibTableColumn
gvcIfDnaOutAccess = _GvcIfDnaOutAccess_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 5, 12, 1, 17),
    _GvcIfDnaOutAccess_Type()
)
gvcIfDnaOutAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gvcIfDnaOutAccess.setStatus("mandatory")


class _GvcIfDnaDefaultTransferPriority_Type(Integer32):
    """Custom type gvcIfDnaDefaultTransferPriority based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              9)
        )
    )
    namedValues = NamedValues(
        *(("high", 9),
          ("normal", 0))
    )


_GvcIfDnaDefaultTransferPriority_Type.__name__ = "Integer32"
_GvcIfDnaDefaultTransferPriority_Object = MibTableColumn
gvcIfDnaDefaultTransferPriority = _GvcIfDnaDefaultTransferPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 5, 12, 1, 18),
    _GvcIfDnaDefaultTransferPriority_Type()
)
gvcIfDnaDefaultTransferPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gvcIfDnaDefaultTransferPriority.setStatus("mandatory")


class _GvcIfDnaTransferPriorityOverRide_Type(Integer32):
    """Custom type gvcIfDnaTransferPriorityOverRide based on Integer32"""
    defaultValue = 1

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


_GvcIfDnaTransferPriorityOverRide_Type.__name__ = "Integer32"
_GvcIfDnaTransferPriorityOverRide_Object = MibTableColumn
gvcIfDnaTransferPriorityOverRide = _GvcIfDnaTransferPriorityOverRide_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 5, 12, 1, 19),
    _GvcIfDnaTransferPriorityOverRide_Type()
)
gvcIfDnaTransferPriorityOverRide.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gvcIfDnaTransferPriorityOverRide.setStatus("mandatory")
_GvcIfDnaIncomingOptionsTable_Object = MibTable
gvcIfDnaIncomingOptionsTable = _GvcIfDnaIncomingOptionsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 5, 13)
)
if mibBuilder.loadTexts:
    gvcIfDnaIncomingOptionsTable.setStatus("mandatory")
_GvcIfDnaIncomingOptionsEntry_Object = MibTableRow
gvcIfDnaIncomingOptionsEntry = _GvcIfDnaIncomingOptionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 5, 13, 1)
)
gvcIfDnaIncomingOptionsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfIndex"),
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfDnaIndex"),
)
if mibBuilder.loadTexts:
    gvcIfDnaIncomingOptionsEntry.setStatus("mandatory")


class _GvcIfDnaIncCalls_Type(Integer32):
    """Custom type gvcIfDnaIncCalls based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("allowed", 1),
          ("disallowed", 0))
    )


_GvcIfDnaIncCalls_Type.__name__ = "Integer32"
_GvcIfDnaIncCalls_Object = MibTableColumn
gvcIfDnaIncCalls = _GvcIfDnaIncCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 5, 13, 1, 1),
    _GvcIfDnaIncCalls_Type()
)
gvcIfDnaIncCalls.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gvcIfDnaIncCalls.setStatus("mandatory")


class _GvcIfDnaIncHighPriorityReverseCharge_Type(Integer32):
    """Custom type gvcIfDnaIncHighPriorityReverseCharge based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("allowed", 1),
          ("disallowed", 0))
    )


_GvcIfDnaIncHighPriorityReverseCharge_Type.__name__ = "Integer32"
_GvcIfDnaIncHighPriorityReverseCharge_Object = MibTableColumn
gvcIfDnaIncHighPriorityReverseCharge = _GvcIfDnaIncHighPriorityReverseCharge_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 5, 13, 1, 2),
    _GvcIfDnaIncHighPriorityReverseCharge_Type()
)
gvcIfDnaIncHighPriorityReverseCharge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gvcIfDnaIncHighPriorityReverseCharge.setStatus("mandatory")


class _GvcIfDnaIncNormalPriorityReverseCharge_Type(Integer32):
    """Custom type gvcIfDnaIncNormalPriorityReverseCharge based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("allowed", 1),
          ("disallowed", 0))
    )


_GvcIfDnaIncNormalPriorityReverseCharge_Type.__name__ = "Integer32"
_GvcIfDnaIncNormalPriorityReverseCharge_Object = MibTableColumn
gvcIfDnaIncNormalPriorityReverseCharge = _GvcIfDnaIncNormalPriorityReverseCharge_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 5, 13, 1, 3),
    _GvcIfDnaIncNormalPriorityReverseCharge_Type()
)
gvcIfDnaIncNormalPriorityReverseCharge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gvcIfDnaIncNormalPriorityReverseCharge.setStatus("mandatory")


class _GvcIfDnaIncIntlNormalCharge_Type(Integer32):
    """Custom type gvcIfDnaIncIntlNormalCharge based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("allowed", 1),
          ("disallowed", 0))
    )


_GvcIfDnaIncIntlNormalCharge_Type.__name__ = "Integer32"
_GvcIfDnaIncIntlNormalCharge_Object = MibTableColumn
gvcIfDnaIncIntlNormalCharge = _GvcIfDnaIncIntlNormalCharge_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 5, 13, 1, 4),
    _GvcIfDnaIncIntlNormalCharge_Type()
)
gvcIfDnaIncIntlNormalCharge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gvcIfDnaIncIntlNormalCharge.setStatus("mandatory")


class _GvcIfDnaIncIntlReverseCharge_Type(Integer32):
    """Custom type gvcIfDnaIncIntlReverseCharge based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("allowed", 1),
          ("disallowed", 0))
    )


_GvcIfDnaIncIntlReverseCharge_Type.__name__ = "Integer32"
_GvcIfDnaIncIntlReverseCharge_Object = MibTableColumn
gvcIfDnaIncIntlReverseCharge = _GvcIfDnaIncIntlReverseCharge_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 5, 13, 1, 5),
    _GvcIfDnaIncIntlReverseCharge_Type()
)
gvcIfDnaIncIntlReverseCharge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gvcIfDnaIncIntlReverseCharge.setStatus("mandatory")


class _GvcIfDnaIncSameService_Type(Integer32):
    """Custom type gvcIfDnaIncSameService based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("allowed", 1),
          ("disallowed", 0))
    )


_GvcIfDnaIncSameService_Type.__name__ = "Integer32"
_GvcIfDnaIncSameService_Object = MibTableColumn
gvcIfDnaIncSameService = _GvcIfDnaIncSameService_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 5, 13, 1, 7),
    _GvcIfDnaIncSameService_Type()
)
gvcIfDnaIncSameService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfDnaIncSameService.setStatus("mandatory")


class _GvcIfDnaIncAccess_Type(Integer32):
    """Custom type gvcIfDnaIncAccess based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("allowed", 1),
          ("disallowed", 0))
    )


_GvcIfDnaIncAccess_Type.__name__ = "Integer32"
_GvcIfDnaIncAccess_Object = MibTableColumn
gvcIfDnaIncAccess = _GvcIfDnaIncAccess_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 5, 13, 1, 9),
    _GvcIfDnaIncAccess_Type()
)
gvcIfDnaIncAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gvcIfDnaIncAccess.setStatus("mandatory")
_GvcIfDnaCallOptionsTable_Object = MibTable
gvcIfDnaCallOptionsTable = _GvcIfDnaCallOptionsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 5, 14)
)
if mibBuilder.loadTexts:
    gvcIfDnaCallOptionsTable.setStatus("mandatory")
_GvcIfDnaCallOptionsEntry_Object = MibTableRow
gvcIfDnaCallOptionsEntry = _GvcIfDnaCallOptionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 5, 14, 1)
)
gvcIfDnaCallOptionsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfIndex"),
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfDnaIndex"),
)
if mibBuilder.loadTexts:
    gvcIfDnaCallOptionsEntry.setStatus("mandatory")


class _GvcIfDnaServiceCategory_Type(Integer32):
    """Custom type gvcIfDnaServiceCategory based on Integer32"""
    defaultValue = 32

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
              9,
              10,
              11,
              13,
              14,
              15,
              16,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              28,
              29,
              30,
              31,
              32)
        )
    )
    namedValues = NamedValues(
        *(("api3201", 20),
          ("bsi", 13),
          ("dsp3270", 7),
          ("enhancedIti", 2),
          ("frameRelay", 30),
          ("gasServer", 26),
          ("gsp", 0),
          ("gvcIf", 32),
          ("hdsp3270", 16),
          ("hostIti", 14),
          ("iam", 8),
          ("ici", 6),
          ("ipiVc", 31),
          ("iti", 11),
          ("mlhi", 9),
          ("mlti", 4),
          ("ncs", 3),
          ("offnetNui", 25),
          ("redirectionServ", 23),
          ("sdlc", 21),
          ("sm", 5),
          ("snaMultiHost", 22),
          ("term3270", 10),
          ("trSnaTpad", 24),
          ("vapAgent", 29),
          ("vapServer", 28),
          ("x25", 1),
          ("x75", 15))
    )


_GvcIfDnaServiceCategory_Type.__name__ = "Integer32"
_GvcIfDnaServiceCategory_Object = MibTableColumn
gvcIfDnaServiceCategory = _GvcIfDnaServiceCategory_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 5, 14, 1, 1),
    _GvcIfDnaServiceCategory_Type()
)
gvcIfDnaServiceCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfDnaServiceCategory.setStatus("mandatory")


class _GvcIfDnaPacketSizes_Type(OctetString):
    """Custom type gvcIfDnaPacketSizes based on OctetString"""
    defaultHexValue = "ff80"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_GvcIfDnaPacketSizes_Type.__name__ = "OctetString"
_GvcIfDnaPacketSizes_Object = MibTableColumn
gvcIfDnaPacketSizes = _GvcIfDnaPacketSizes_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 5, 14, 1, 2),
    _GvcIfDnaPacketSizes_Type()
)
gvcIfDnaPacketSizes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gvcIfDnaPacketSizes.setStatus("mandatory")


class _GvcIfDnaDefaultRecvFrmNetworkPacketSize_Type(Integer32):
    """Custom type gvcIfDnaDefaultRecvFrmNetworkPacketSize based on Integer32"""
    defaultValue = 12

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("n1024", 10),
          ("n128", 7),
          ("n16", 4),
          ("n2048", 11),
          ("n256", 8),
          ("n32", 5),
          ("n4096", 12),
          ("n512", 9),
          ("n64", 6))
    )


_GvcIfDnaDefaultRecvFrmNetworkPacketSize_Type.__name__ = "Integer32"
_GvcIfDnaDefaultRecvFrmNetworkPacketSize_Object = MibTableColumn
gvcIfDnaDefaultRecvFrmNetworkPacketSize = _GvcIfDnaDefaultRecvFrmNetworkPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 5, 14, 1, 3),
    _GvcIfDnaDefaultRecvFrmNetworkPacketSize_Type()
)
gvcIfDnaDefaultRecvFrmNetworkPacketSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gvcIfDnaDefaultRecvFrmNetworkPacketSize.setStatus("mandatory")


class _GvcIfDnaDefaultSendToNetworkPacketSize_Type(Integer32):
    """Custom type gvcIfDnaDefaultSendToNetworkPacketSize based on Integer32"""
    defaultValue = 12

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("n1024", 10),
          ("n128", 7),
          ("n16", 4),
          ("n2048", 11),
          ("n256", 8),
          ("n32", 5),
          ("n4096", 12),
          ("n512", 9),
          ("n64", 6))
    )


_GvcIfDnaDefaultSendToNetworkPacketSize_Type.__name__ = "Integer32"
_GvcIfDnaDefaultSendToNetworkPacketSize_Object = MibTableColumn
gvcIfDnaDefaultSendToNetworkPacketSize = _GvcIfDnaDefaultSendToNetworkPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 5, 14, 1, 4),
    _GvcIfDnaDefaultSendToNetworkPacketSize_Type()
)
gvcIfDnaDefaultSendToNetworkPacketSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gvcIfDnaDefaultSendToNetworkPacketSize.setStatus("mandatory")


class _GvcIfDnaDefaultRecvFrmNetworkThruputClass_Type(Unsigned32):
    """Custom type gvcIfDnaDefaultRecvFrmNetworkThruputClass based on Unsigned32"""
    defaultValue = 13

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_GvcIfDnaDefaultRecvFrmNetworkThruputClass_Type.__name__ = "Unsigned32"
_GvcIfDnaDefaultRecvFrmNetworkThruputClass_Object = MibTableColumn
gvcIfDnaDefaultRecvFrmNetworkThruputClass = _GvcIfDnaDefaultRecvFrmNetworkThruputClass_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 5, 14, 1, 5),
    _GvcIfDnaDefaultRecvFrmNetworkThruputClass_Type()
)
gvcIfDnaDefaultRecvFrmNetworkThruputClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gvcIfDnaDefaultRecvFrmNetworkThruputClass.setStatus("mandatory")


class _GvcIfDnaDefaultSendToNetworkThruputClass_Type(Unsigned32):
    """Custom type gvcIfDnaDefaultSendToNetworkThruputClass based on Unsigned32"""
    defaultValue = 13

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_GvcIfDnaDefaultSendToNetworkThruputClass_Type.__name__ = "Unsigned32"
_GvcIfDnaDefaultSendToNetworkThruputClass_Object = MibTableColumn
gvcIfDnaDefaultSendToNetworkThruputClass = _GvcIfDnaDefaultSendToNetworkThruputClass_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 5, 14, 1, 6),
    _GvcIfDnaDefaultSendToNetworkThruputClass_Type()
)
gvcIfDnaDefaultSendToNetworkThruputClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gvcIfDnaDefaultSendToNetworkThruputClass.setStatus("mandatory")


class _GvcIfDnaDefaultRecvFrmNetworkWindowSize_Type(Unsigned32):
    """Custom type gvcIfDnaDefaultRecvFrmNetworkWindowSize based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_GvcIfDnaDefaultRecvFrmNetworkWindowSize_Type.__name__ = "Unsigned32"
_GvcIfDnaDefaultRecvFrmNetworkWindowSize_Object = MibTableColumn
gvcIfDnaDefaultRecvFrmNetworkWindowSize = _GvcIfDnaDefaultRecvFrmNetworkWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 5, 14, 1, 7),
    _GvcIfDnaDefaultRecvFrmNetworkWindowSize_Type()
)
gvcIfDnaDefaultRecvFrmNetworkWindowSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gvcIfDnaDefaultRecvFrmNetworkWindowSize.setStatus("mandatory")


class _GvcIfDnaDefaultSendToNetworkWindowSize_Type(Unsigned32):
    """Custom type gvcIfDnaDefaultSendToNetworkWindowSize based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_GvcIfDnaDefaultSendToNetworkWindowSize_Type.__name__ = "Unsigned32"
_GvcIfDnaDefaultSendToNetworkWindowSize_Object = MibTableColumn
gvcIfDnaDefaultSendToNetworkWindowSize = _GvcIfDnaDefaultSendToNetworkWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 5, 14, 1, 8),
    _GvcIfDnaDefaultSendToNetworkWindowSize_Type()
)
gvcIfDnaDefaultSendToNetworkWindowSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gvcIfDnaDefaultSendToNetworkWindowSize.setStatus("mandatory")


class _GvcIfDnaPacketSizeNegotiation_Type(Integer32):
    """Custom type gvcIfDnaPacketSizeNegotiation based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("endToEnd", 0),
          ("local", 1))
    )


_GvcIfDnaPacketSizeNegotiation_Type.__name__ = "Integer32"
_GvcIfDnaPacketSizeNegotiation_Object = MibTableColumn
gvcIfDnaPacketSizeNegotiation = _GvcIfDnaPacketSizeNegotiation_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 5, 14, 1, 9),
    _GvcIfDnaPacketSizeNegotiation_Type()
)
gvcIfDnaPacketSizeNegotiation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gvcIfDnaPacketSizeNegotiation.setStatus("mandatory")


class _GvcIfDnaCugFormat_Type(Integer32):
    """Custom type gvcIfDnaCugFormat based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("basic", 0),
          ("extended", 1))
    )


_GvcIfDnaCugFormat_Type.__name__ = "Integer32"
_GvcIfDnaCugFormat_Object = MibTableColumn
gvcIfDnaCugFormat = _GvcIfDnaCugFormat_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 5, 14, 1, 10),
    _GvcIfDnaCugFormat_Type()
)
gvcIfDnaCugFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gvcIfDnaCugFormat.setStatus("mandatory")


class _GvcIfDnaAccountClass_Type(Unsigned32):
    """Custom type gvcIfDnaAccountClass based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_GvcIfDnaAccountClass_Type.__name__ = "Unsigned32"
_GvcIfDnaAccountClass_Object = MibTableColumn
gvcIfDnaAccountClass = _GvcIfDnaAccountClass_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 5, 14, 1, 16),
    _GvcIfDnaAccountClass_Type()
)
gvcIfDnaAccountClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gvcIfDnaAccountClass.setStatus("mandatory")


class _GvcIfDnaAccountCollection_Type(OctetString):
    """Custom type gvcIfDnaAccountCollection based on OctetString"""
    defaultHexValue = "80"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_GvcIfDnaAccountCollection_Type.__name__ = "OctetString"
_GvcIfDnaAccountCollection_Object = MibTableColumn
gvcIfDnaAccountCollection = _GvcIfDnaAccountCollection_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 5, 14, 1, 17),
    _GvcIfDnaAccountCollection_Type()
)
gvcIfDnaAccountCollection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gvcIfDnaAccountCollection.setStatus("mandatory")


class _GvcIfDnaServiceExchange_Type(Unsigned32):
    """Custom type gvcIfDnaServiceExchange based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_GvcIfDnaServiceExchange_Type.__name__ = "Unsigned32"
_GvcIfDnaServiceExchange_Object = MibTableColumn
gvcIfDnaServiceExchange = _GvcIfDnaServiceExchange_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 5, 14, 1, 18),
    _GvcIfDnaServiceExchange_Type()
)
gvcIfDnaServiceExchange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gvcIfDnaServiceExchange.setStatus("mandatory")
_GvcIfRg_ObjectIdentity = ObjectIdentity
gvcIfRg = _GvcIfRg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 6)
)
_GvcIfRgRowStatusTable_Object = MibTable
gvcIfRgRowStatusTable = _GvcIfRgRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 6, 1)
)
if mibBuilder.loadTexts:
    gvcIfRgRowStatusTable.setStatus("mandatory")
_GvcIfRgRowStatusEntry_Object = MibTableRow
gvcIfRgRowStatusEntry = _GvcIfRgRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 6, 1, 1)
)
gvcIfRgRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfIndex"),
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfRgIndex"),
)
if mibBuilder.loadTexts:
    gvcIfRgRowStatusEntry.setStatus("mandatory")
_GvcIfRgRowStatus_Type = RowStatus
_GvcIfRgRowStatus_Object = MibTableColumn
gvcIfRgRowStatus = _GvcIfRgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 6, 1, 1, 1),
    _GvcIfRgRowStatus_Type()
)
gvcIfRgRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gvcIfRgRowStatus.setStatus("mandatory")
_GvcIfRgComponentName_Type = DisplayString
_GvcIfRgComponentName_Object = MibTableColumn
gvcIfRgComponentName = _GvcIfRgComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 6, 1, 1, 2),
    _GvcIfRgComponentName_Type()
)
gvcIfRgComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfRgComponentName.setStatus("mandatory")
_GvcIfRgStorageType_Type = StorageType
_GvcIfRgStorageType_Object = MibTableColumn
gvcIfRgStorageType = _GvcIfRgStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 6, 1, 1, 4),
    _GvcIfRgStorageType_Type()
)
gvcIfRgStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfRgStorageType.setStatus("mandatory")


class _GvcIfRgIndex_Type(Integer32):
    """Custom type gvcIfRgIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
    )


_GvcIfRgIndex_Type.__name__ = "Integer32"
_GvcIfRgIndex_Object = MibTableColumn
gvcIfRgIndex = _GvcIfRgIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 6, 1, 1, 10),
    _GvcIfRgIndex_Type()
)
gvcIfRgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gvcIfRgIndex.setStatus("mandatory")
_GvcIfRgIfEntryTable_Object = MibTable
gvcIfRgIfEntryTable = _GvcIfRgIfEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 6, 10)
)
if mibBuilder.loadTexts:
    gvcIfRgIfEntryTable.setStatus("mandatory")
_GvcIfRgIfEntryEntry_Object = MibTableRow
gvcIfRgIfEntryEntry = _GvcIfRgIfEntryEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 6, 10, 1)
)
gvcIfRgIfEntryEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfIndex"),
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfRgIndex"),
)
if mibBuilder.loadTexts:
    gvcIfRgIfEntryEntry.setStatus("mandatory")


class _GvcIfRgIfAdminStatus_Type(Integer32):
    """Custom type gvcIfRgIfAdminStatus based on Integer32"""
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
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_GvcIfRgIfAdminStatus_Type.__name__ = "Integer32"
_GvcIfRgIfAdminStatus_Object = MibTableColumn
gvcIfRgIfAdminStatus = _GvcIfRgIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 6, 10, 1, 1),
    _GvcIfRgIfAdminStatus_Type()
)
gvcIfRgIfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gvcIfRgIfAdminStatus.setStatus("mandatory")


class _GvcIfRgIfIndex_Type(InterfaceIndex):
    """Custom type gvcIfRgIfIndex based on InterfaceIndex"""
    subtypeSpec = InterfaceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_GvcIfRgIfIndex_Type.__name__ = "InterfaceIndex"
_GvcIfRgIfIndex_Object = MibTableColumn
gvcIfRgIfIndex = _GvcIfRgIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 6, 10, 1, 2),
    _GvcIfRgIfIndex_Type()
)
gvcIfRgIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfRgIfIndex.setStatus("mandatory")
_GvcIfRgProvTable_Object = MibTable
gvcIfRgProvTable = _GvcIfRgProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 6, 11)
)
if mibBuilder.loadTexts:
    gvcIfRgProvTable.setStatus("mandatory")
_GvcIfRgProvEntry_Object = MibTableRow
gvcIfRgProvEntry = _GvcIfRgProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 6, 11, 1)
)
gvcIfRgProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfIndex"),
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfRgIndex"),
)
if mibBuilder.loadTexts:
    gvcIfRgProvEntry.setStatus("mandatory")
_GvcIfRgLinkToProtocolPort_Type = Link
_GvcIfRgLinkToProtocolPort_Object = MibTableColumn
gvcIfRgLinkToProtocolPort = _GvcIfRgLinkToProtocolPort_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 6, 11, 1, 1),
    _GvcIfRgLinkToProtocolPort_Type()
)
gvcIfRgLinkToProtocolPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gvcIfRgLinkToProtocolPort.setStatus("mandatory")
_GvcIfRgOperStatusTable_Object = MibTable
gvcIfRgOperStatusTable = _GvcIfRgOperStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 6, 12)
)
if mibBuilder.loadTexts:
    gvcIfRgOperStatusTable.setStatus("mandatory")
_GvcIfRgOperStatusEntry_Object = MibTableRow
gvcIfRgOperStatusEntry = _GvcIfRgOperStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 6, 12, 1)
)
gvcIfRgOperStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfIndex"),
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfRgIndex"),
)
if mibBuilder.loadTexts:
    gvcIfRgOperStatusEntry.setStatus("mandatory")


class _GvcIfRgSnmpOperStatus_Type(Integer32):
    """Custom type gvcIfRgSnmpOperStatus based on Integer32"""
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
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_GvcIfRgSnmpOperStatus_Type.__name__ = "Integer32"
_GvcIfRgSnmpOperStatus_Object = MibTableColumn
gvcIfRgSnmpOperStatus = _GvcIfRgSnmpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 6, 12, 1, 1),
    _GvcIfRgSnmpOperStatus_Type()
)
gvcIfRgSnmpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfRgSnmpOperStatus.setStatus("mandatory")
_GvcIfDlci_ObjectIdentity = ObjectIdentity
gvcIfDlci = _GvcIfDlci_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7)
)
_GvcIfDlciRowStatusTable_Object = MibTable
gvcIfDlciRowStatusTable = _GvcIfDlciRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 1)
)
if mibBuilder.loadTexts:
    gvcIfDlciRowStatusTable.setStatus("mandatory")
_GvcIfDlciRowStatusEntry_Object = MibTableRow
gvcIfDlciRowStatusEntry = _GvcIfDlciRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 1, 1)
)
gvcIfDlciRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfIndex"),
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfDlciIndex"),
)
if mibBuilder.loadTexts:
    gvcIfDlciRowStatusEntry.setStatus("mandatory")
_GvcIfDlciRowStatus_Type = RowStatus
_GvcIfDlciRowStatus_Object = MibTableColumn
gvcIfDlciRowStatus = _GvcIfDlciRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 1, 1, 1),
    _GvcIfDlciRowStatus_Type()
)
gvcIfDlciRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gvcIfDlciRowStatus.setStatus("mandatory")
_GvcIfDlciComponentName_Type = DisplayString
_GvcIfDlciComponentName_Object = MibTableColumn
gvcIfDlciComponentName = _GvcIfDlciComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 1, 1, 2),
    _GvcIfDlciComponentName_Type()
)
gvcIfDlciComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfDlciComponentName.setStatus("mandatory")
_GvcIfDlciStorageType_Type = StorageType
_GvcIfDlciStorageType_Object = MibTableColumn
gvcIfDlciStorageType = _GvcIfDlciStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 1, 1, 4),
    _GvcIfDlciStorageType_Type()
)
gvcIfDlciStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfDlciStorageType.setStatus("mandatory")


class _GvcIfDlciIndex_Type(Integer32):
    """Custom type gvcIfDlciIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 4095),
    )


_GvcIfDlciIndex_Type.__name__ = "Integer32"
_GvcIfDlciIndex_Object = MibTableColumn
gvcIfDlciIndex = _GvcIfDlciIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 1, 1, 10),
    _GvcIfDlciIndex_Type()
)
gvcIfDlciIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gvcIfDlciIndex.setStatus("mandatory")
_GvcIfDlciDc_ObjectIdentity = ObjectIdentity
gvcIfDlciDc = _GvcIfDlciDc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 2)
)
_GvcIfDlciDcRowStatusTable_Object = MibTable
gvcIfDlciDcRowStatusTable = _GvcIfDlciDcRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 2, 1)
)
if mibBuilder.loadTexts:
    gvcIfDlciDcRowStatusTable.setStatus("mandatory")
_GvcIfDlciDcRowStatusEntry_Object = MibTableRow
gvcIfDlciDcRowStatusEntry = _GvcIfDlciDcRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 2, 1, 1)
)
gvcIfDlciDcRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfIndex"),
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfDlciIndex"),
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfDlciDcIndex"),
)
if mibBuilder.loadTexts:
    gvcIfDlciDcRowStatusEntry.setStatus("mandatory")
_GvcIfDlciDcRowStatus_Type = RowStatus
_GvcIfDlciDcRowStatus_Object = MibTableColumn
gvcIfDlciDcRowStatus = _GvcIfDlciDcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 2, 1, 1, 1),
    _GvcIfDlciDcRowStatus_Type()
)
gvcIfDlciDcRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfDlciDcRowStatus.setStatus("mandatory")
_GvcIfDlciDcComponentName_Type = DisplayString
_GvcIfDlciDcComponentName_Object = MibTableColumn
gvcIfDlciDcComponentName = _GvcIfDlciDcComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 2, 1, 1, 2),
    _GvcIfDlciDcComponentName_Type()
)
gvcIfDlciDcComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfDlciDcComponentName.setStatus("mandatory")
_GvcIfDlciDcStorageType_Type = StorageType
_GvcIfDlciDcStorageType_Object = MibTableColumn
gvcIfDlciDcStorageType = _GvcIfDlciDcStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 2, 1, 1, 4),
    _GvcIfDlciDcStorageType_Type()
)
gvcIfDlciDcStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfDlciDcStorageType.setStatus("mandatory")
_GvcIfDlciDcIndex_Type = NonReplicated
_GvcIfDlciDcIndex_Object = MibTableColumn
gvcIfDlciDcIndex = _GvcIfDlciDcIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 2, 1, 1, 10),
    _GvcIfDlciDcIndex_Type()
)
gvcIfDlciDcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gvcIfDlciDcIndex.setStatus("mandatory")
_GvcIfDlciDcOptionsTable_Object = MibTable
gvcIfDlciDcOptionsTable = _GvcIfDlciDcOptionsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 2, 10)
)
if mibBuilder.loadTexts:
    gvcIfDlciDcOptionsTable.setStatus("mandatory")
_GvcIfDlciDcOptionsEntry_Object = MibTableRow
gvcIfDlciDcOptionsEntry = _GvcIfDlciDcOptionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 2, 10, 1)
)
gvcIfDlciDcOptionsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfIndex"),
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfDlciIndex"),
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfDlciDcIndex"),
)
if mibBuilder.loadTexts:
    gvcIfDlciDcOptionsEntry.setStatus("mandatory")


class _GvcIfDlciDcRemoteNpi_Type(Integer32):
    """Custom type gvcIfDlciDcRemoteNpi based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("e164", 1),
          ("x121", 0))
    )


_GvcIfDlciDcRemoteNpi_Type.__name__ = "Integer32"
_GvcIfDlciDcRemoteNpi_Object = MibTableColumn
gvcIfDlciDcRemoteNpi = _GvcIfDlciDcRemoteNpi_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 2, 10, 1, 3),
    _GvcIfDlciDcRemoteNpi_Type()
)
gvcIfDlciDcRemoteNpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gvcIfDlciDcRemoteNpi.setStatus("mandatory")


class _GvcIfDlciDcRemoteDna_Type(DigitString):
    """Custom type gvcIfDlciDcRemoteDna based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_GvcIfDlciDcRemoteDna_Type.__name__ = "DigitString"
_GvcIfDlciDcRemoteDna_Object = MibTableColumn
gvcIfDlciDcRemoteDna = _GvcIfDlciDcRemoteDna_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 2, 10, 1, 4),
    _GvcIfDlciDcRemoteDna_Type()
)
gvcIfDlciDcRemoteDna.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gvcIfDlciDcRemoteDna.setStatus("mandatory")


class _GvcIfDlciDcRemoteDlci_Type(Unsigned32):
    """Custom type gvcIfDlciDcRemoteDlci based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_GvcIfDlciDcRemoteDlci_Type.__name__ = "Unsigned32"
_GvcIfDlciDcRemoteDlci_Object = MibTableColumn
gvcIfDlciDcRemoteDlci = _GvcIfDlciDcRemoteDlci_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 2, 10, 1, 5),
    _GvcIfDlciDcRemoteDlci_Type()
)
gvcIfDlciDcRemoteDlci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gvcIfDlciDcRemoteDlci.setStatus("mandatory")


class _GvcIfDlciDcType_Type(Integer32):
    """Custom type gvcIfDlciDcType based on Integer32"""
    defaultValue = 1

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
        *(("permanentBackupSlave", 3),
          ("permanentMaster", 1),
          ("permanentSlave", 2),
          ("permanentSlaveWithBackup", 4))
    )


_GvcIfDlciDcType_Type.__name__ = "Integer32"
_GvcIfDlciDcType_Object = MibTableColumn
gvcIfDlciDcType = _GvcIfDlciDcType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 2, 10, 1, 6),
    _GvcIfDlciDcType_Type()
)
gvcIfDlciDcType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gvcIfDlciDcType.setStatus("mandatory")


class _GvcIfDlciDcTransferPriority_Type(Integer32):
    """Custom type gvcIfDlciDcTransferPriority based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              9,
              255)
        )
    )
    namedValues = NamedValues(
        *(("high", 9),
          ("normal", 0),
          ("useDnaDefTP", 255))
    )


_GvcIfDlciDcTransferPriority_Type.__name__ = "Integer32"
_GvcIfDlciDcTransferPriority_Object = MibTableColumn
gvcIfDlciDcTransferPriority = _GvcIfDlciDcTransferPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 2, 10, 1, 9),
    _GvcIfDlciDcTransferPriority_Type()
)
gvcIfDlciDcTransferPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gvcIfDlciDcTransferPriority.setStatus("mandatory")


class _GvcIfDlciDcDiscardPriority_Type(Integer32):
    """Custom type gvcIfDlciDcDiscardPriority based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("high", 1),
          ("normal", 0),
          ("useDnaDefPriority", 3))
    )


_GvcIfDlciDcDiscardPriority_Type.__name__ = "Integer32"
_GvcIfDlciDcDiscardPriority_Object = MibTableColumn
gvcIfDlciDcDiscardPriority = _GvcIfDlciDcDiscardPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 2, 10, 1, 10),
    _GvcIfDlciDcDiscardPriority_Type()
)
gvcIfDlciDcDiscardPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gvcIfDlciDcDiscardPriority.setStatus("mandatory")
_GvcIfDlciDcNfaTable_Object = MibTable
gvcIfDlciDcNfaTable = _GvcIfDlciDcNfaTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 2, 482)
)
if mibBuilder.loadTexts:
    gvcIfDlciDcNfaTable.setStatus("obsolete")
_GvcIfDlciDcNfaEntry_Object = MibTableRow
gvcIfDlciDcNfaEntry = _GvcIfDlciDcNfaEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 2, 482, 1)
)
gvcIfDlciDcNfaEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfIndex"),
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfDlciIndex"),
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfDlciDcIndex"),
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfDlciDcNfaIndex"),
)
if mibBuilder.loadTexts:
    gvcIfDlciDcNfaEntry.setStatus("obsolete")


class _GvcIfDlciDcNfaIndex_Type(Integer32):
    """Custom type gvcIfDlciDcNfaIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(48, 48),
    )


_GvcIfDlciDcNfaIndex_Type.__name__ = "Integer32"
_GvcIfDlciDcNfaIndex_Object = MibTableColumn
gvcIfDlciDcNfaIndex = _GvcIfDlciDcNfaIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 2, 482, 1, 1),
    _GvcIfDlciDcNfaIndex_Type()
)
gvcIfDlciDcNfaIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gvcIfDlciDcNfaIndex.setStatus("obsolete")


class _GvcIfDlciDcNfaValue_Type(HexString):
    """Custom type gvcIfDlciDcNfaValue based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_GvcIfDlciDcNfaValue_Type.__name__ = "HexString"
_GvcIfDlciDcNfaValue_Object = MibTableColumn
gvcIfDlciDcNfaValue = _GvcIfDlciDcNfaValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 2, 482, 1, 2),
    _GvcIfDlciDcNfaValue_Type()
)
gvcIfDlciDcNfaValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gvcIfDlciDcNfaValue.setStatus("obsolete")
_GvcIfDlciDcNfaRowStatus_Type = RowStatus
_GvcIfDlciDcNfaRowStatus_Object = MibTableColumn
gvcIfDlciDcNfaRowStatus = _GvcIfDlciDcNfaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 2, 482, 1, 3),
    _GvcIfDlciDcNfaRowStatus_Type()
)
gvcIfDlciDcNfaRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    gvcIfDlciDcNfaRowStatus.setStatus("obsolete")
_GvcIfDlciVc_ObjectIdentity = ObjectIdentity
gvcIfDlciVc = _GvcIfDlciVc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 3)
)
_GvcIfDlciVcRowStatusTable_Object = MibTable
gvcIfDlciVcRowStatusTable = _GvcIfDlciVcRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 3, 1)
)
if mibBuilder.loadTexts:
    gvcIfDlciVcRowStatusTable.setStatus("mandatory")
_GvcIfDlciVcRowStatusEntry_Object = MibTableRow
gvcIfDlciVcRowStatusEntry = _GvcIfDlciVcRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 3, 1, 1)
)
gvcIfDlciVcRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfIndex"),
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfDlciIndex"),
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfDlciVcIndex"),
)
if mibBuilder.loadTexts:
    gvcIfDlciVcRowStatusEntry.setStatus("mandatory")
_GvcIfDlciVcRowStatus_Type = RowStatus
_GvcIfDlciVcRowStatus_Object = MibTableColumn
gvcIfDlciVcRowStatus = _GvcIfDlciVcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 3, 1, 1, 1),
    _GvcIfDlciVcRowStatus_Type()
)
gvcIfDlciVcRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfDlciVcRowStatus.setStatus("mandatory")
_GvcIfDlciVcComponentName_Type = DisplayString
_GvcIfDlciVcComponentName_Object = MibTableColumn
gvcIfDlciVcComponentName = _GvcIfDlciVcComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 3, 1, 1, 2),
    _GvcIfDlciVcComponentName_Type()
)
gvcIfDlciVcComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfDlciVcComponentName.setStatus("mandatory")
_GvcIfDlciVcStorageType_Type = StorageType
_GvcIfDlciVcStorageType_Object = MibTableColumn
gvcIfDlciVcStorageType = _GvcIfDlciVcStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 3, 1, 1, 4),
    _GvcIfDlciVcStorageType_Type()
)
gvcIfDlciVcStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfDlciVcStorageType.setStatus("mandatory")
_GvcIfDlciVcIndex_Type = NonReplicated
_GvcIfDlciVcIndex_Object = MibTableColumn
gvcIfDlciVcIndex = _GvcIfDlciVcIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 3, 1, 1, 10),
    _GvcIfDlciVcIndex_Type()
)
gvcIfDlciVcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gvcIfDlciVcIndex.setStatus("mandatory")
_GvcIfDlciVcCadTable_Object = MibTable
gvcIfDlciVcCadTable = _GvcIfDlciVcCadTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 3, 10)
)
if mibBuilder.loadTexts:
    gvcIfDlciVcCadTable.setStatus("mandatory")
_GvcIfDlciVcCadEntry_Object = MibTableRow
gvcIfDlciVcCadEntry = _GvcIfDlciVcCadEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 3, 10, 1)
)
gvcIfDlciVcCadEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfIndex"),
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfDlciIndex"),
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfDlciVcIndex"),
)
if mibBuilder.loadTexts:
    gvcIfDlciVcCadEntry.setStatus("mandatory")


class _GvcIfDlciVcType_Type(Integer32):
    """Custom type gvcIfDlciVcType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pvc", 1),
          ("spvc", 2),
          ("svc", 0))
    )


_GvcIfDlciVcType_Type.__name__ = "Integer32"
_GvcIfDlciVcType_Object = MibTableColumn
gvcIfDlciVcType = _GvcIfDlciVcType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 3, 10, 1, 1),
    _GvcIfDlciVcType_Type()
)
gvcIfDlciVcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfDlciVcType.setStatus("mandatory")


class _GvcIfDlciVcState_Type(Integer32):
    """Custom type gvcIfDlciVcState based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("creating", 0),
          ("dataTransferP4", 4),
          ("dceClearIndicationP7", 7),
          ("dceWaitingP3", 3),
          ("dteClearRequestP6", 6),
          ("dteWaitingP2", 2),
          ("readyP1", 1),
          ("termination", 8),
          ("unsupportedP5", 5))
    )


_GvcIfDlciVcState_Type.__name__ = "Integer32"
_GvcIfDlciVcState_Object = MibTableColumn
gvcIfDlciVcState = _GvcIfDlciVcState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 3, 10, 1, 2),
    _GvcIfDlciVcState_Type()
)
gvcIfDlciVcState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfDlciVcState.setStatus("mandatory")


class _GvcIfDlciVcPreviousState_Type(Integer32):
    """Custom type gvcIfDlciVcPreviousState based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("creating", 0),
          ("dataTransferP4", 4),
          ("dceClearIndicationP7", 7),
          ("dceWaitingP3", 3),
          ("dteClearRequestP6", 6),
          ("dteWaitingP2", 2),
          ("readyP1", 1),
          ("termination", 8),
          ("unsupportedP5", 5))
    )


_GvcIfDlciVcPreviousState_Type.__name__ = "Integer32"
_GvcIfDlciVcPreviousState_Object = MibTableColumn
gvcIfDlciVcPreviousState = _GvcIfDlciVcPreviousState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 3, 10, 1, 3),
    _GvcIfDlciVcPreviousState_Type()
)
gvcIfDlciVcPreviousState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfDlciVcPreviousState.setStatus("mandatory")


class _GvcIfDlciVcDiagnosticCode_Type(Unsigned32):
    """Custom type gvcIfDlciVcDiagnosticCode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_GvcIfDlciVcDiagnosticCode_Type.__name__ = "Unsigned32"
_GvcIfDlciVcDiagnosticCode_Object = MibTableColumn
gvcIfDlciVcDiagnosticCode = _GvcIfDlciVcDiagnosticCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 3, 10, 1, 4),
    _GvcIfDlciVcDiagnosticCode_Type()
)
gvcIfDlciVcDiagnosticCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfDlciVcDiagnosticCode.setStatus("mandatory")


class _GvcIfDlciVcPreviousDiagnosticCode_Type(Unsigned32):
    """Custom type gvcIfDlciVcPreviousDiagnosticCode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_GvcIfDlciVcPreviousDiagnosticCode_Type.__name__ = "Unsigned32"
_GvcIfDlciVcPreviousDiagnosticCode_Object = MibTableColumn
gvcIfDlciVcPreviousDiagnosticCode = _GvcIfDlciVcPreviousDiagnosticCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 3, 10, 1, 5),
    _GvcIfDlciVcPreviousDiagnosticCode_Type()
)
gvcIfDlciVcPreviousDiagnosticCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfDlciVcPreviousDiagnosticCode.setStatus("mandatory")


class _GvcIfDlciVcCalledNpi_Type(Integer32):
    """Custom type gvcIfDlciVcCalledNpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("e164", 1),
          ("x121", 0))
    )


_GvcIfDlciVcCalledNpi_Type.__name__ = "Integer32"
_GvcIfDlciVcCalledNpi_Object = MibTableColumn
gvcIfDlciVcCalledNpi = _GvcIfDlciVcCalledNpi_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 3, 10, 1, 6),
    _GvcIfDlciVcCalledNpi_Type()
)
gvcIfDlciVcCalledNpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfDlciVcCalledNpi.setStatus("mandatory")


class _GvcIfDlciVcCalledDna_Type(DigitString):
    """Custom type gvcIfDlciVcCalledDna based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_GvcIfDlciVcCalledDna_Type.__name__ = "DigitString"
_GvcIfDlciVcCalledDna_Object = MibTableColumn
gvcIfDlciVcCalledDna = _GvcIfDlciVcCalledDna_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 3, 10, 1, 7),
    _GvcIfDlciVcCalledDna_Type()
)
gvcIfDlciVcCalledDna.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfDlciVcCalledDna.setStatus("mandatory")


class _GvcIfDlciVcCalledLcn_Type(Unsigned32):
    """Custom type gvcIfDlciVcCalledLcn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_GvcIfDlciVcCalledLcn_Type.__name__ = "Unsigned32"
_GvcIfDlciVcCalledLcn_Object = MibTableColumn
gvcIfDlciVcCalledLcn = _GvcIfDlciVcCalledLcn_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 3, 10, 1, 8),
    _GvcIfDlciVcCalledLcn_Type()
)
gvcIfDlciVcCalledLcn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfDlciVcCalledLcn.setStatus("mandatory")


class _GvcIfDlciVcCallingNpi_Type(Integer32):
    """Custom type gvcIfDlciVcCallingNpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("e164", 1),
          ("x121", 0))
    )


_GvcIfDlciVcCallingNpi_Type.__name__ = "Integer32"
_GvcIfDlciVcCallingNpi_Object = MibTableColumn
gvcIfDlciVcCallingNpi = _GvcIfDlciVcCallingNpi_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 3, 10, 1, 9),
    _GvcIfDlciVcCallingNpi_Type()
)
gvcIfDlciVcCallingNpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfDlciVcCallingNpi.setStatus("mandatory")


class _GvcIfDlciVcCallingDna_Type(DigitString):
    """Custom type gvcIfDlciVcCallingDna based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_GvcIfDlciVcCallingDna_Type.__name__ = "DigitString"
_GvcIfDlciVcCallingDna_Object = MibTableColumn
gvcIfDlciVcCallingDna = _GvcIfDlciVcCallingDna_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 3, 10, 1, 10),
    _GvcIfDlciVcCallingDna_Type()
)
gvcIfDlciVcCallingDna.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfDlciVcCallingDna.setStatus("mandatory")


class _GvcIfDlciVcCallingLcn_Type(Unsigned32):
    """Custom type gvcIfDlciVcCallingLcn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_GvcIfDlciVcCallingLcn_Type.__name__ = "Unsigned32"
_GvcIfDlciVcCallingLcn_Object = MibTableColumn
gvcIfDlciVcCallingLcn = _GvcIfDlciVcCallingLcn_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 3, 10, 1, 11),
    _GvcIfDlciVcCallingLcn_Type()
)
gvcIfDlciVcCallingLcn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfDlciVcCallingLcn.setStatus("mandatory")


class _GvcIfDlciVcAccountingEnabled_Type(Integer32):
    """Custom type gvcIfDlciVcAccountingEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 0))
    )


_GvcIfDlciVcAccountingEnabled_Type.__name__ = "Integer32"
_GvcIfDlciVcAccountingEnabled_Object = MibTableColumn
gvcIfDlciVcAccountingEnabled = _GvcIfDlciVcAccountingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 3, 10, 1, 12),
    _GvcIfDlciVcAccountingEnabled_Type()
)
gvcIfDlciVcAccountingEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfDlciVcAccountingEnabled.setStatus("mandatory")


class _GvcIfDlciVcFastSelectCall_Type(Integer32):
    """Custom type gvcIfDlciVcFastSelectCall based on Integer32"""
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


_GvcIfDlciVcFastSelectCall_Type.__name__ = "Integer32"
_GvcIfDlciVcFastSelectCall_Object = MibTableColumn
gvcIfDlciVcFastSelectCall = _GvcIfDlciVcFastSelectCall_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 3, 10, 1, 13),
    _GvcIfDlciVcFastSelectCall_Type()
)
gvcIfDlciVcFastSelectCall.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfDlciVcFastSelectCall.setStatus("mandatory")


class _GvcIfDlciVcPathReliability_Type(Integer32):
    """Custom type gvcIfDlciVcPathReliability based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("high", 0),
          ("normal", 1))
    )


_GvcIfDlciVcPathReliability_Type.__name__ = "Integer32"
_GvcIfDlciVcPathReliability_Object = MibTableColumn
gvcIfDlciVcPathReliability = _GvcIfDlciVcPathReliability_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 3, 10, 1, 19),
    _GvcIfDlciVcPathReliability_Type()
)
gvcIfDlciVcPathReliability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfDlciVcPathReliability.setStatus("mandatory")


class _GvcIfDlciVcAccountingEnd_Type(Integer32):
    """Custom type gvcIfDlciVcAccountingEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("calledEnd", 1),
          ("callingEnd", 0))
    )


_GvcIfDlciVcAccountingEnd_Type.__name__ = "Integer32"
_GvcIfDlciVcAccountingEnd_Object = MibTableColumn
gvcIfDlciVcAccountingEnd = _GvcIfDlciVcAccountingEnd_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 3, 10, 1, 20),
    _GvcIfDlciVcAccountingEnd_Type()
)
gvcIfDlciVcAccountingEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfDlciVcAccountingEnd.setStatus("mandatory")


class _GvcIfDlciVcPriority_Type(Integer32):
    """Custom type gvcIfDlciVcPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("high", 1),
          ("normal", 0))
    )


_GvcIfDlciVcPriority_Type.__name__ = "Integer32"
_GvcIfDlciVcPriority_Object = MibTableColumn
gvcIfDlciVcPriority = _GvcIfDlciVcPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 3, 10, 1, 21),
    _GvcIfDlciVcPriority_Type()
)
gvcIfDlciVcPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfDlciVcPriority.setStatus("mandatory")


class _GvcIfDlciVcSegmentSize_Type(Unsigned32):
    """Custom type gvcIfDlciVcSegmentSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_GvcIfDlciVcSegmentSize_Type.__name__ = "Unsigned32"
_GvcIfDlciVcSegmentSize_Object = MibTableColumn
gvcIfDlciVcSegmentSize = _GvcIfDlciVcSegmentSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 3, 10, 1, 22),
    _GvcIfDlciVcSegmentSize_Type()
)
gvcIfDlciVcSegmentSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfDlciVcSegmentSize.setStatus("mandatory")


class _GvcIfDlciVcMaxSubnetPktSize_Type(Unsigned32):
    """Custom type gvcIfDlciVcMaxSubnetPktSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_GvcIfDlciVcMaxSubnetPktSize_Type.__name__ = "Unsigned32"
_GvcIfDlciVcMaxSubnetPktSize_Object = MibTableColumn
gvcIfDlciVcMaxSubnetPktSize = _GvcIfDlciVcMaxSubnetPktSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 3, 10, 1, 27),
    _GvcIfDlciVcMaxSubnetPktSize_Type()
)
gvcIfDlciVcMaxSubnetPktSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfDlciVcMaxSubnetPktSize.setStatus("mandatory")


class _GvcIfDlciVcRcosToNetwork_Type(Integer32):
    """Custom type gvcIfDlciVcRcosToNetwork based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("delay", 1),
          ("multimedia", 2),
          ("throughput", 0))
    )


_GvcIfDlciVcRcosToNetwork_Type.__name__ = "Integer32"
_GvcIfDlciVcRcosToNetwork_Object = MibTableColumn
gvcIfDlciVcRcosToNetwork = _GvcIfDlciVcRcosToNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 3, 10, 1, 28),
    _GvcIfDlciVcRcosToNetwork_Type()
)
gvcIfDlciVcRcosToNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfDlciVcRcosToNetwork.setStatus("mandatory")


class _GvcIfDlciVcRcosFromNetwork_Type(Integer32):
    """Custom type gvcIfDlciVcRcosFromNetwork based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("delay", 1),
          ("multimedia", 2),
          ("throughput", 0))
    )


_GvcIfDlciVcRcosFromNetwork_Type.__name__ = "Integer32"
_GvcIfDlciVcRcosFromNetwork_Object = MibTableColumn
gvcIfDlciVcRcosFromNetwork = _GvcIfDlciVcRcosFromNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 3, 10, 1, 29),
    _GvcIfDlciVcRcosFromNetwork_Type()
)
gvcIfDlciVcRcosFromNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfDlciVcRcosFromNetwork.setStatus("mandatory")


class _GvcIfDlciVcEmissionPriorityToNetwork_Type(Integer32):
    """Custom type gvcIfDlciVcEmissionPriorityToNetwork based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("high", 1),
          ("interrupting", 2),
          ("normal", 0))
    )


_GvcIfDlciVcEmissionPriorityToNetwork_Type.__name__ = "Integer32"
_GvcIfDlciVcEmissionPriorityToNetwork_Object = MibTableColumn
gvcIfDlciVcEmissionPriorityToNetwork = _GvcIfDlciVcEmissionPriorityToNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 3, 10, 1, 30),
    _GvcIfDlciVcEmissionPriorityToNetwork_Type()
)
gvcIfDlciVcEmissionPriorityToNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfDlciVcEmissionPriorityToNetwork.setStatus("mandatory")


class _GvcIfDlciVcEmissionPriorityFromNetwork_Type(Integer32):
    """Custom type gvcIfDlciVcEmissionPriorityFromNetwork based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("high", 1),
          ("interrupting", 2),
          ("normal", 0))
    )


_GvcIfDlciVcEmissionPriorityFromNetwork_Type.__name__ = "Integer32"
_GvcIfDlciVcEmissionPriorityFromNetwork_Object = MibTableColumn
gvcIfDlciVcEmissionPriorityFromNetwork = _GvcIfDlciVcEmissionPriorityFromNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 3, 10, 1, 31),
    _GvcIfDlciVcEmissionPriorityFromNetwork_Type()
)
gvcIfDlciVcEmissionPriorityFromNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfDlciVcEmissionPriorityFromNetwork.setStatus("mandatory")


class _GvcIfDlciVcDataPath_Type(AsciiString):
    """Custom type gvcIfDlciVcDataPath based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_GvcIfDlciVcDataPath_Type.__name__ = "AsciiString"
_GvcIfDlciVcDataPath_Object = MibTableColumn
gvcIfDlciVcDataPath = _GvcIfDlciVcDataPath_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 3, 10, 1, 32),
    _GvcIfDlciVcDataPath_Type()
)
gvcIfDlciVcDataPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfDlciVcDataPath.setStatus("mandatory")
_GvcIfDlciVcIntdTable_Object = MibTable
gvcIfDlciVcIntdTable = _GvcIfDlciVcIntdTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 3, 11)
)
if mibBuilder.loadTexts:
    gvcIfDlciVcIntdTable.setStatus("mandatory")
_GvcIfDlciVcIntdEntry_Object = MibTableRow
gvcIfDlciVcIntdEntry = _GvcIfDlciVcIntdEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 3, 11, 1)
)
gvcIfDlciVcIntdEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfIndex"),
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfDlciIndex"),
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfDlciVcIndex"),
)
if mibBuilder.loadTexts:
    gvcIfDlciVcIntdEntry.setStatus("mandatory")


class _GvcIfDlciVcCallReferenceNumber_Type(Hex):
    """Custom type gvcIfDlciVcCallReferenceNumber based on Hex"""
    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_GvcIfDlciVcCallReferenceNumber_Type.__name__ = "Hex"
_GvcIfDlciVcCallReferenceNumber_Object = MibTableColumn
gvcIfDlciVcCallReferenceNumber = _GvcIfDlciVcCallReferenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 3, 11, 1, 1),
    _GvcIfDlciVcCallReferenceNumber_Type()
)
gvcIfDlciVcCallReferenceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfDlciVcCallReferenceNumber.setStatus("mandatory")


class _GvcIfDlciVcElapsedTimeTillNow_Type(Unsigned32):
    """Custom type gvcIfDlciVcElapsedTimeTillNow based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_GvcIfDlciVcElapsedTimeTillNow_Type.__name__ = "Unsigned32"
_GvcIfDlciVcElapsedTimeTillNow_Object = MibTableColumn
gvcIfDlciVcElapsedTimeTillNow = _GvcIfDlciVcElapsedTimeTillNow_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 3, 11, 1, 2),
    _GvcIfDlciVcElapsedTimeTillNow_Type()
)
gvcIfDlciVcElapsedTimeTillNow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfDlciVcElapsedTimeTillNow.setStatus("mandatory")


class _GvcIfDlciVcSegmentsRx_Type(Unsigned32):
    """Custom type gvcIfDlciVcSegmentsRx based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_GvcIfDlciVcSegmentsRx_Type.__name__ = "Unsigned32"
_GvcIfDlciVcSegmentsRx_Object = MibTableColumn
gvcIfDlciVcSegmentsRx = _GvcIfDlciVcSegmentsRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 3, 11, 1, 3),
    _GvcIfDlciVcSegmentsRx_Type()
)
gvcIfDlciVcSegmentsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfDlciVcSegmentsRx.setStatus("mandatory")


class _GvcIfDlciVcSegmentsSent_Type(Unsigned32):
    """Custom type gvcIfDlciVcSegmentsSent based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_GvcIfDlciVcSegmentsSent_Type.__name__ = "Unsigned32"
_GvcIfDlciVcSegmentsSent_Object = MibTableColumn
gvcIfDlciVcSegmentsSent = _GvcIfDlciVcSegmentsSent_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 3, 11, 1, 4),
    _GvcIfDlciVcSegmentsSent_Type()
)
gvcIfDlciVcSegmentsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfDlciVcSegmentsSent.setStatus("mandatory")


class _GvcIfDlciVcStartTime_Type(EnterpriseDateAndTime):
    """Custom type gvcIfDlciVcStartTime based on EnterpriseDateAndTime"""
    subtypeSpec = EnterpriseDateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(19, 19),
    )


_GvcIfDlciVcStartTime_Type.__name__ = "EnterpriseDateAndTime"
_GvcIfDlciVcStartTime_Object = MibTableColumn
gvcIfDlciVcStartTime = _GvcIfDlciVcStartTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 3, 11, 1, 5),
    _GvcIfDlciVcStartTime_Type()
)
gvcIfDlciVcStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfDlciVcStartTime.setStatus("mandatory")
_GvcIfDlciVcFrdTable_Object = MibTable
gvcIfDlciVcFrdTable = _GvcIfDlciVcFrdTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 3, 12)
)
if mibBuilder.loadTexts:
    gvcIfDlciVcFrdTable.setStatus("mandatory")
_GvcIfDlciVcFrdEntry_Object = MibTableRow
gvcIfDlciVcFrdEntry = _GvcIfDlciVcFrdEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 3, 12, 1)
)
gvcIfDlciVcFrdEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfIndex"),
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfDlciIndex"),
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfDlciVcIndex"),
)
if mibBuilder.loadTexts:
    gvcIfDlciVcFrdEntry.setStatus("mandatory")


class _GvcIfDlciVcFrmCongestedToSubnet_Type(Unsigned32):
    """Custom type gvcIfDlciVcFrmCongestedToSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_GvcIfDlciVcFrmCongestedToSubnet_Type.__name__ = "Unsigned32"
_GvcIfDlciVcFrmCongestedToSubnet_Object = MibTableColumn
gvcIfDlciVcFrmCongestedToSubnet = _GvcIfDlciVcFrmCongestedToSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 3, 12, 1, 2),
    _GvcIfDlciVcFrmCongestedToSubnet_Type()
)
gvcIfDlciVcFrmCongestedToSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfDlciVcFrmCongestedToSubnet.setStatus("mandatory")


class _GvcIfDlciVcCannotForwardToSubnet_Type(Unsigned32):
    """Custom type gvcIfDlciVcCannotForwardToSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_GvcIfDlciVcCannotForwardToSubnet_Type.__name__ = "Unsigned32"
_GvcIfDlciVcCannotForwardToSubnet_Object = MibTableColumn
gvcIfDlciVcCannotForwardToSubnet = _GvcIfDlciVcCannotForwardToSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 3, 12, 1, 3),
    _GvcIfDlciVcCannotForwardToSubnet_Type()
)
gvcIfDlciVcCannotForwardToSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfDlciVcCannotForwardToSubnet.setStatus("mandatory")


class _GvcIfDlciVcNotDataXferToSubnet_Type(Unsigned32):
    """Custom type gvcIfDlciVcNotDataXferToSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_GvcIfDlciVcNotDataXferToSubnet_Type.__name__ = "Unsigned32"
_GvcIfDlciVcNotDataXferToSubnet_Object = MibTableColumn
gvcIfDlciVcNotDataXferToSubnet = _GvcIfDlciVcNotDataXferToSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 3, 12, 1, 4),
    _GvcIfDlciVcNotDataXferToSubnet_Type()
)
gvcIfDlciVcNotDataXferToSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfDlciVcNotDataXferToSubnet.setStatus("mandatory")


class _GvcIfDlciVcOutOfRangeFrmFromSubnet_Type(Unsigned32):
    """Custom type gvcIfDlciVcOutOfRangeFrmFromSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_GvcIfDlciVcOutOfRangeFrmFromSubnet_Type.__name__ = "Unsigned32"
_GvcIfDlciVcOutOfRangeFrmFromSubnet_Object = MibTableColumn
gvcIfDlciVcOutOfRangeFrmFromSubnet = _GvcIfDlciVcOutOfRangeFrmFromSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 3, 12, 1, 5),
    _GvcIfDlciVcOutOfRangeFrmFromSubnet_Type()
)
gvcIfDlciVcOutOfRangeFrmFromSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfDlciVcOutOfRangeFrmFromSubnet.setStatus("mandatory")


class _GvcIfDlciVcCombErrorsFromSubnet_Type(Unsigned32):
    """Custom type gvcIfDlciVcCombErrorsFromSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_GvcIfDlciVcCombErrorsFromSubnet_Type.__name__ = "Unsigned32"
_GvcIfDlciVcCombErrorsFromSubnet_Object = MibTableColumn
gvcIfDlciVcCombErrorsFromSubnet = _GvcIfDlciVcCombErrorsFromSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 3, 12, 1, 6),
    _GvcIfDlciVcCombErrorsFromSubnet_Type()
)
gvcIfDlciVcCombErrorsFromSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfDlciVcCombErrorsFromSubnet.setStatus("mandatory")


class _GvcIfDlciVcDuplicatesFromSubnet_Type(Unsigned32):
    """Custom type gvcIfDlciVcDuplicatesFromSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_GvcIfDlciVcDuplicatesFromSubnet_Type.__name__ = "Unsigned32"
_GvcIfDlciVcDuplicatesFromSubnet_Object = MibTableColumn
gvcIfDlciVcDuplicatesFromSubnet = _GvcIfDlciVcDuplicatesFromSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 3, 12, 1, 7),
    _GvcIfDlciVcDuplicatesFromSubnet_Type()
)
gvcIfDlciVcDuplicatesFromSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfDlciVcDuplicatesFromSubnet.setStatus("mandatory")


class _GvcIfDlciVcNotDataXferFromSubnet_Type(Unsigned32):
    """Custom type gvcIfDlciVcNotDataXferFromSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_GvcIfDlciVcNotDataXferFromSubnet_Type.__name__ = "Unsigned32"
_GvcIfDlciVcNotDataXferFromSubnet_Object = MibTableColumn
gvcIfDlciVcNotDataXferFromSubnet = _GvcIfDlciVcNotDataXferFromSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 3, 12, 1, 8),
    _GvcIfDlciVcNotDataXferFromSubnet_Type()
)
gvcIfDlciVcNotDataXferFromSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfDlciVcNotDataXferFromSubnet.setStatus("mandatory")


class _GvcIfDlciVcFrmLossTimeouts_Type(Unsigned32):
    """Custom type gvcIfDlciVcFrmLossTimeouts based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_GvcIfDlciVcFrmLossTimeouts_Type.__name__ = "Unsigned32"
_GvcIfDlciVcFrmLossTimeouts_Object = MibTableColumn
gvcIfDlciVcFrmLossTimeouts = _GvcIfDlciVcFrmLossTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 3, 12, 1, 9),
    _GvcIfDlciVcFrmLossTimeouts_Type()
)
gvcIfDlciVcFrmLossTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfDlciVcFrmLossTimeouts.setStatus("mandatory")


class _GvcIfDlciVcOoSeqByteCntExceeded_Type(Unsigned32):
    """Custom type gvcIfDlciVcOoSeqByteCntExceeded based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_GvcIfDlciVcOoSeqByteCntExceeded_Type.__name__ = "Unsigned32"
_GvcIfDlciVcOoSeqByteCntExceeded_Object = MibTableColumn
gvcIfDlciVcOoSeqByteCntExceeded = _GvcIfDlciVcOoSeqByteCntExceeded_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 3, 12, 1, 10),
    _GvcIfDlciVcOoSeqByteCntExceeded_Type()
)
gvcIfDlciVcOoSeqByteCntExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfDlciVcOoSeqByteCntExceeded.setStatus("mandatory")


class _GvcIfDlciVcPeakOoSeqPktCount_Type(Unsigned32):
    """Custom type gvcIfDlciVcPeakOoSeqPktCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_GvcIfDlciVcPeakOoSeqPktCount_Type.__name__ = "Unsigned32"
_GvcIfDlciVcPeakOoSeqPktCount_Object = MibTableColumn
gvcIfDlciVcPeakOoSeqPktCount = _GvcIfDlciVcPeakOoSeqPktCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 3, 12, 1, 11),
    _GvcIfDlciVcPeakOoSeqPktCount_Type()
)
gvcIfDlciVcPeakOoSeqPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfDlciVcPeakOoSeqPktCount.setStatus("mandatory")


class _GvcIfDlciVcPeakOoSeqFrmForwarded_Type(Unsigned32):
    """Custom type gvcIfDlciVcPeakOoSeqFrmForwarded based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_GvcIfDlciVcPeakOoSeqFrmForwarded_Type.__name__ = "Unsigned32"
_GvcIfDlciVcPeakOoSeqFrmForwarded_Object = MibTableColumn
gvcIfDlciVcPeakOoSeqFrmForwarded = _GvcIfDlciVcPeakOoSeqFrmForwarded_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 3, 12, 1, 12),
    _GvcIfDlciVcPeakOoSeqFrmForwarded_Type()
)
gvcIfDlciVcPeakOoSeqFrmForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfDlciVcPeakOoSeqFrmForwarded.setStatus("mandatory")


class _GvcIfDlciVcSendSequenceNumber_Type(Unsigned32):
    """Custom type gvcIfDlciVcSendSequenceNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_GvcIfDlciVcSendSequenceNumber_Type.__name__ = "Unsigned32"
_GvcIfDlciVcSendSequenceNumber_Object = MibTableColumn
gvcIfDlciVcSendSequenceNumber = _GvcIfDlciVcSendSequenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 3, 12, 1, 13),
    _GvcIfDlciVcSendSequenceNumber_Type()
)
gvcIfDlciVcSendSequenceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfDlciVcSendSequenceNumber.setStatus("mandatory")


class _GvcIfDlciVcPktRetryTimeouts_Type(Unsigned32):
    """Custom type gvcIfDlciVcPktRetryTimeouts based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_GvcIfDlciVcPktRetryTimeouts_Type.__name__ = "Unsigned32"
_GvcIfDlciVcPktRetryTimeouts_Object = MibTableColumn
gvcIfDlciVcPktRetryTimeouts = _GvcIfDlciVcPktRetryTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 3, 12, 1, 15),
    _GvcIfDlciVcPktRetryTimeouts_Type()
)
gvcIfDlciVcPktRetryTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfDlciVcPktRetryTimeouts.setStatus("mandatory")


class _GvcIfDlciVcPeakRetryQueueSize_Type(Unsigned32):
    """Custom type gvcIfDlciVcPeakRetryQueueSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_GvcIfDlciVcPeakRetryQueueSize_Type.__name__ = "Unsigned32"
_GvcIfDlciVcPeakRetryQueueSize_Object = MibTableColumn
gvcIfDlciVcPeakRetryQueueSize = _GvcIfDlciVcPeakRetryQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 3, 12, 1, 16),
    _GvcIfDlciVcPeakRetryQueueSize_Type()
)
gvcIfDlciVcPeakRetryQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfDlciVcPeakRetryQueueSize.setStatus("mandatory")


class _GvcIfDlciVcSubnetRecoveries_Type(Unsigned32):
    """Custom type gvcIfDlciVcSubnetRecoveries based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_GvcIfDlciVcSubnetRecoveries_Type.__name__ = "Unsigned32"
_GvcIfDlciVcSubnetRecoveries_Object = MibTableColumn
gvcIfDlciVcSubnetRecoveries = _GvcIfDlciVcSubnetRecoveries_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 3, 12, 1, 17),
    _GvcIfDlciVcSubnetRecoveries_Type()
)
gvcIfDlciVcSubnetRecoveries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfDlciVcSubnetRecoveries.setStatus("mandatory")


class _GvcIfDlciVcOoSeqPktCntExceeded_Type(Unsigned32):
    """Custom type gvcIfDlciVcOoSeqPktCntExceeded based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_GvcIfDlciVcOoSeqPktCntExceeded_Type.__name__ = "Unsigned32"
_GvcIfDlciVcOoSeqPktCntExceeded_Object = MibTableColumn
gvcIfDlciVcOoSeqPktCntExceeded = _GvcIfDlciVcOoSeqPktCntExceeded_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 3, 12, 1, 19),
    _GvcIfDlciVcOoSeqPktCntExceeded_Type()
)
gvcIfDlciVcOoSeqPktCntExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfDlciVcOoSeqPktCntExceeded.setStatus("mandatory")


class _GvcIfDlciVcPeakOoSeqByteCount_Type(Unsigned32):
    """Custom type gvcIfDlciVcPeakOoSeqByteCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50000),
    )


_GvcIfDlciVcPeakOoSeqByteCount_Type.__name__ = "Unsigned32"
_GvcIfDlciVcPeakOoSeqByteCount_Object = MibTableColumn
gvcIfDlciVcPeakOoSeqByteCount = _GvcIfDlciVcPeakOoSeqByteCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 3, 12, 1, 20),
    _GvcIfDlciVcPeakOoSeqByteCount_Type()
)
gvcIfDlciVcPeakOoSeqByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfDlciVcPeakOoSeqByteCount.setStatus("mandatory")
_GvcIfDlciVcDmepTable_Object = MibTable
gvcIfDlciVcDmepTable = _GvcIfDlciVcDmepTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 3, 417)
)
if mibBuilder.loadTexts:
    gvcIfDlciVcDmepTable.setStatus("mandatory")
_GvcIfDlciVcDmepEntry_Object = MibTableRow
gvcIfDlciVcDmepEntry = _GvcIfDlciVcDmepEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 3, 417, 1)
)
gvcIfDlciVcDmepEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfIndex"),
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfDlciIndex"),
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfDlciVcIndex"),
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfDlciVcDmepValue"),
)
if mibBuilder.loadTexts:
    gvcIfDlciVcDmepEntry.setStatus("mandatory")
_GvcIfDlciVcDmepValue_Type = RowPointer
_GvcIfDlciVcDmepValue_Object = MibTableColumn
gvcIfDlciVcDmepValue = _GvcIfDlciVcDmepValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 3, 417, 1, 1),
    _GvcIfDlciVcDmepValue_Type()
)
gvcIfDlciVcDmepValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfDlciVcDmepValue.setStatus("mandatory")
_GvcIfDlciSp_ObjectIdentity = ObjectIdentity
gvcIfDlciSp = _GvcIfDlciSp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 4)
)
_GvcIfDlciSpRowStatusTable_Object = MibTable
gvcIfDlciSpRowStatusTable = _GvcIfDlciSpRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 4, 1)
)
if mibBuilder.loadTexts:
    gvcIfDlciSpRowStatusTable.setStatus("mandatory")
_GvcIfDlciSpRowStatusEntry_Object = MibTableRow
gvcIfDlciSpRowStatusEntry = _GvcIfDlciSpRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 4, 1, 1)
)
gvcIfDlciSpRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfIndex"),
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfDlciIndex"),
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfDlciSpIndex"),
)
if mibBuilder.loadTexts:
    gvcIfDlciSpRowStatusEntry.setStatus("mandatory")
_GvcIfDlciSpRowStatus_Type = RowStatus
_GvcIfDlciSpRowStatus_Object = MibTableColumn
gvcIfDlciSpRowStatus = _GvcIfDlciSpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 4, 1, 1, 1),
    _GvcIfDlciSpRowStatus_Type()
)
gvcIfDlciSpRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gvcIfDlciSpRowStatus.setStatus("mandatory")
_GvcIfDlciSpComponentName_Type = DisplayString
_GvcIfDlciSpComponentName_Object = MibTableColumn
gvcIfDlciSpComponentName = _GvcIfDlciSpComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 4, 1, 1, 2),
    _GvcIfDlciSpComponentName_Type()
)
gvcIfDlciSpComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfDlciSpComponentName.setStatus("mandatory")
_GvcIfDlciSpStorageType_Type = StorageType
_GvcIfDlciSpStorageType_Object = MibTableColumn
gvcIfDlciSpStorageType = _GvcIfDlciSpStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 4, 1, 1, 4),
    _GvcIfDlciSpStorageType_Type()
)
gvcIfDlciSpStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfDlciSpStorageType.setStatus("mandatory")
_GvcIfDlciSpIndex_Type = NonReplicated
_GvcIfDlciSpIndex_Object = MibTableColumn
gvcIfDlciSpIndex = _GvcIfDlciSpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 4, 1, 1, 10),
    _GvcIfDlciSpIndex_Type()
)
gvcIfDlciSpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gvcIfDlciSpIndex.setStatus("mandatory")
_GvcIfDlciSpParmsTable_Object = MibTable
gvcIfDlciSpParmsTable = _GvcIfDlciSpParmsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 4, 11)
)
if mibBuilder.loadTexts:
    gvcIfDlciSpParmsTable.setStatus("mandatory")
_GvcIfDlciSpParmsEntry_Object = MibTableRow
gvcIfDlciSpParmsEntry = _GvcIfDlciSpParmsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 4, 11, 1)
)
gvcIfDlciSpParmsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfIndex"),
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfDlciIndex"),
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfDlciSpIndex"),
)
if mibBuilder.loadTexts:
    gvcIfDlciSpParmsEntry.setStatus("mandatory")


class _GvcIfDlciSpRateEnforcement_Type(Integer32):
    """Custom type gvcIfDlciSpRateEnforcement based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_GvcIfDlciSpRateEnforcement_Type.__name__ = "Integer32"
_GvcIfDlciSpRateEnforcement_Object = MibTableColumn
gvcIfDlciSpRateEnforcement = _GvcIfDlciSpRateEnforcement_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 4, 11, 1, 1),
    _GvcIfDlciSpRateEnforcement_Type()
)
gvcIfDlciSpRateEnforcement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gvcIfDlciSpRateEnforcement.setStatus("mandatory")


class _GvcIfDlciSpCommittedInformationRate_Type(Unsigned32):
    """Custom type gvcIfDlciSpCommittedInformationRate based on Unsigned32"""
    defaultValue = 64000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50000000),
    )


_GvcIfDlciSpCommittedInformationRate_Type.__name__ = "Unsigned32"
_GvcIfDlciSpCommittedInformationRate_Object = MibTableColumn
gvcIfDlciSpCommittedInformationRate = _GvcIfDlciSpCommittedInformationRate_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 4, 11, 1, 2),
    _GvcIfDlciSpCommittedInformationRate_Type()
)
gvcIfDlciSpCommittedInformationRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gvcIfDlciSpCommittedInformationRate.setStatus("mandatory")


class _GvcIfDlciSpCommittedBurstSize_Type(Unsigned32):
    """Custom type gvcIfDlciSpCommittedBurstSize based on Unsigned32"""
    defaultValue = 64000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50000000),
    )


_GvcIfDlciSpCommittedBurstSize_Type.__name__ = "Unsigned32"
_GvcIfDlciSpCommittedBurstSize_Object = MibTableColumn
gvcIfDlciSpCommittedBurstSize = _GvcIfDlciSpCommittedBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 4, 11, 1, 3),
    _GvcIfDlciSpCommittedBurstSize_Type()
)
gvcIfDlciSpCommittedBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gvcIfDlciSpCommittedBurstSize.setStatus("mandatory")


class _GvcIfDlciSpExcessBurstSize_Type(Unsigned32):
    """Custom type gvcIfDlciSpExcessBurstSize based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50000000),
    )


_GvcIfDlciSpExcessBurstSize_Type.__name__ = "Unsigned32"
_GvcIfDlciSpExcessBurstSize_Object = MibTableColumn
gvcIfDlciSpExcessBurstSize = _GvcIfDlciSpExcessBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 4, 11, 1, 4),
    _GvcIfDlciSpExcessBurstSize_Type()
)
gvcIfDlciSpExcessBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gvcIfDlciSpExcessBurstSize.setStatus("mandatory")


class _GvcIfDlciSpMeasurementInterval_Type(Unsigned32):
    """Custom type gvcIfDlciSpMeasurementInterval based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 25500),
    )


_GvcIfDlciSpMeasurementInterval_Type.__name__ = "Unsigned32"
_GvcIfDlciSpMeasurementInterval_Object = MibTableColumn
gvcIfDlciSpMeasurementInterval = _GvcIfDlciSpMeasurementInterval_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 4, 11, 1, 5),
    _GvcIfDlciSpMeasurementInterval_Type()
)
gvcIfDlciSpMeasurementInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gvcIfDlciSpMeasurementInterval.setStatus("mandatory")
_GvcIfDlciBnn_ObjectIdentity = ObjectIdentity
gvcIfDlciBnn = _GvcIfDlciBnn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 5)
)
_GvcIfDlciBnnRowStatusTable_Object = MibTable
gvcIfDlciBnnRowStatusTable = _GvcIfDlciBnnRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 5, 1)
)
if mibBuilder.loadTexts:
    gvcIfDlciBnnRowStatusTable.setStatus("mandatory")
_GvcIfDlciBnnRowStatusEntry_Object = MibTableRow
gvcIfDlciBnnRowStatusEntry = _GvcIfDlciBnnRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 5, 1, 1)
)
gvcIfDlciBnnRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfIndex"),
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfDlciIndex"),
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfDlciBnnIndex"),
)
if mibBuilder.loadTexts:
    gvcIfDlciBnnRowStatusEntry.setStatus("mandatory")
_GvcIfDlciBnnRowStatus_Type = RowStatus
_GvcIfDlciBnnRowStatus_Object = MibTableColumn
gvcIfDlciBnnRowStatus = _GvcIfDlciBnnRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 5, 1, 1, 1),
    _GvcIfDlciBnnRowStatus_Type()
)
gvcIfDlciBnnRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gvcIfDlciBnnRowStatus.setStatus("mandatory")
_GvcIfDlciBnnComponentName_Type = DisplayString
_GvcIfDlciBnnComponentName_Object = MibTableColumn
gvcIfDlciBnnComponentName = _GvcIfDlciBnnComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 5, 1, 1, 2),
    _GvcIfDlciBnnComponentName_Type()
)
gvcIfDlciBnnComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfDlciBnnComponentName.setStatus("mandatory")
_GvcIfDlciBnnStorageType_Type = StorageType
_GvcIfDlciBnnStorageType_Object = MibTableColumn
gvcIfDlciBnnStorageType = _GvcIfDlciBnnStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 5, 1, 1, 4),
    _GvcIfDlciBnnStorageType_Type()
)
gvcIfDlciBnnStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfDlciBnnStorageType.setStatus("mandatory")
_GvcIfDlciBnnIndex_Type = NonReplicated
_GvcIfDlciBnnIndex_Object = MibTableColumn
gvcIfDlciBnnIndex = _GvcIfDlciBnnIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 5, 1, 1, 10),
    _GvcIfDlciBnnIndex_Type()
)
gvcIfDlciBnnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gvcIfDlciBnnIndex.setStatus("mandatory")
_GvcIfDlciLdev_ObjectIdentity = ObjectIdentity
gvcIfDlciLdev = _GvcIfDlciLdev_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 6)
)
_GvcIfDlciLdevRowStatusTable_Object = MibTable
gvcIfDlciLdevRowStatusTable = _GvcIfDlciLdevRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 6, 1)
)
if mibBuilder.loadTexts:
    gvcIfDlciLdevRowStatusTable.setStatus("mandatory")
_GvcIfDlciLdevRowStatusEntry_Object = MibTableRow
gvcIfDlciLdevRowStatusEntry = _GvcIfDlciLdevRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 6, 1, 1)
)
gvcIfDlciLdevRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfIndex"),
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfDlciIndex"),
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfDlciLdevIndex"),
)
if mibBuilder.loadTexts:
    gvcIfDlciLdevRowStatusEntry.setStatus("mandatory")
_GvcIfDlciLdevRowStatus_Type = RowStatus
_GvcIfDlciLdevRowStatus_Object = MibTableColumn
gvcIfDlciLdevRowStatus = _GvcIfDlciLdevRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 6, 1, 1, 1),
    _GvcIfDlciLdevRowStatus_Type()
)
gvcIfDlciLdevRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gvcIfDlciLdevRowStatus.setStatus("mandatory")
_GvcIfDlciLdevComponentName_Type = DisplayString
_GvcIfDlciLdevComponentName_Object = MibTableColumn
gvcIfDlciLdevComponentName = _GvcIfDlciLdevComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 6, 1, 1, 2),
    _GvcIfDlciLdevComponentName_Type()
)
gvcIfDlciLdevComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfDlciLdevComponentName.setStatus("mandatory")
_GvcIfDlciLdevStorageType_Type = StorageType
_GvcIfDlciLdevStorageType_Object = MibTableColumn
gvcIfDlciLdevStorageType = _GvcIfDlciLdevStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 6, 1, 1, 4),
    _GvcIfDlciLdevStorageType_Type()
)
gvcIfDlciLdevStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfDlciLdevStorageType.setStatus("mandatory")
_GvcIfDlciLdevIndex_Type = NonReplicated
_GvcIfDlciLdevIndex_Object = MibTableColumn
gvcIfDlciLdevIndex = _GvcIfDlciLdevIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 6, 1, 1, 10),
    _GvcIfDlciLdevIndex_Type()
)
gvcIfDlciLdevIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gvcIfDlciLdevIndex.setStatus("mandatory")
_GvcIfDlciLdevAddrTable_Object = MibTable
gvcIfDlciLdevAddrTable = _GvcIfDlciLdevAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 6, 10)
)
if mibBuilder.loadTexts:
    gvcIfDlciLdevAddrTable.setStatus("mandatory")
_GvcIfDlciLdevAddrEntry_Object = MibTableRow
gvcIfDlciLdevAddrEntry = _GvcIfDlciLdevAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 6, 10, 1)
)
gvcIfDlciLdevAddrEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfIndex"),
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfDlciIndex"),
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfDlciLdevIndex"),
)
if mibBuilder.loadTexts:
    gvcIfDlciLdevAddrEntry.setStatus("mandatory")


class _GvcIfDlciLdevMac_Type(DashedHexString):
    """Custom type gvcIfDlciLdevMac based on DashedHexString"""
    subtypeSpec = DashedHexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_GvcIfDlciLdevMac_Type.__name__ = "DashedHexString"
_GvcIfDlciLdevMac_Object = MibTableColumn
gvcIfDlciLdevMac = _GvcIfDlciLdevMac_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 6, 10, 1, 1),
    _GvcIfDlciLdevMac_Type()
)
gvcIfDlciLdevMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gvcIfDlciLdevMac.setStatus("mandatory")
_GvcIfDlciLdevDevOpTable_Object = MibTable
gvcIfDlciLdevDevOpTable = _GvcIfDlciLdevDevOpTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 6, 11)
)
if mibBuilder.loadTexts:
    gvcIfDlciLdevDevOpTable.setStatus("mandatory")
_GvcIfDlciLdevDevOpEntry_Object = MibTableRow
gvcIfDlciLdevDevOpEntry = _GvcIfDlciLdevDevOpEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 6, 11, 1)
)
gvcIfDlciLdevDevOpEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfIndex"),
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfDlciIndex"),
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfDlciLdevIndex"),
)
if mibBuilder.loadTexts:
    gvcIfDlciLdevDevOpEntry.setStatus("mandatory")


class _GvcIfDlciLdevDeviceStatus_Type(Integer32):
    """Custom type gvcIfDlciLdevDeviceStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("reachable", 1),
          ("unreachable", 0))
    )


_GvcIfDlciLdevDeviceStatus_Type.__name__ = "Integer32"
_GvcIfDlciLdevDeviceStatus_Object = MibTableColumn
gvcIfDlciLdevDeviceStatus = _GvcIfDlciLdevDeviceStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 6, 11, 1, 1),
    _GvcIfDlciLdevDeviceStatus_Type()
)
gvcIfDlciLdevDeviceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfDlciLdevDeviceStatus.setStatus("mandatory")


class _GvcIfDlciLdevActiveLinkStations_Type(Unsigned32):
    """Custom type gvcIfDlciLdevActiveLinkStations based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_GvcIfDlciLdevActiveLinkStations_Type.__name__ = "Unsigned32"
_GvcIfDlciLdevActiveLinkStations_Object = MibTableColumn
gvcIfDlciLdevActiveLinkStations = _GvcIfDlciLdevActiveLinkStations_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 6, 11, 1, 2),
    _GvcIfDlciLdevActiveLinkStations_Type()
)
gvcIfDlciLdevActiveLinkStations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfDlciLdevActiveLinkStations.setStatus("mandatory")


class _GvcIfDlciLdevLastTimeUnreachable_Type(EnterpriseDateAndTime):
    """Custom type gvcIfDlciLdevLastTimeUnreachable based on EnterpriseDateAndTime"""
    subtypeSpec = EnterpriseDateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(19, 19),
    )


_GvcIfDlciLdevLastTimeUnreachable_Type.__name__ = "EnterpriseDateAndTime"
_GvcIfDlciLdevLastTimeUnreachable_Object = MibTableColumn
gvcIfDlciLdevLastTimeUnreachable = _GvcIfDlciLdevLastTimeUnreachable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 6, 11, 1, 3),
    _GvcIfDlciLdevLastTimeUnreachable_Type()
)
gvcIfDlciLdevLastTimeUnreachable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfDlciLdevLastTimeUnreachable.setStatus("mandatory")


class _GvcIfDlciLdevLastTimeReachable_Type(EnterpriseDateAndTime):
    """Custom type gvcIfDlciLdevLastTimeReachable based on EnterpriseDateAndTime"""
    subtypeSpec = EnterpriseDateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(19, 19),
    )


_GvcIfDlciLdevLastTimeReachable_Type.__name__ = "EnterpriseDateAndTime"
_GvcIfDlciLdevLastTimeReachable_Object = MibTableColumn
gvcIfDlciLdevLastTimeReachable = _GvcIfDlciLdevLastTimeReachable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 6, 11, 1, 4),
    _GvcIfDlciLdevLastTimeReachable_Type()
)
gvcIfDlciLdevLastTimeReachable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfDlciLdevLastTimeReachable.setStatus("mandatory")
_GvcIfDlciLdevDeviceUnreachable_Type = Counter32
_GvcIfDlciLdevDeviceUnreachable_Object = MibTableColumn
gvcIfDlciLdevDeviceUnreachable = _GvcIfDlciLdevDeviceUnreachable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 6, 11, 1, 5),
    _GvcIfDlciLdevDeviceUnreachable_Type()
)
gvcIfDlciLdevDeviceUnreachable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfDlciLdevDeviceUnreachable.setStatus("mandatory")


class _GvcIfDlciLdevMonitoringLcn_Type(Integer32):
    """Custom type gvcIfDlciLdevMonitoringLcn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_GvcIfDlciLdevMonitoringLcn_Type.__name__ = "Integer32"
_GvcIfDlciLdevMonitoringLcn_Object = MibTableColumn
gvcIfDlciLdevMonitoringLcn = _GvcIfDlciLdevMonitoringLcn_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 6, 11, 1, 6),
    _GvcIfDlciLdevMonitoringLcn_Type()
)
gvcIfDlciLdevMonitoringLcn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfDlciLdevMonitoringLcn.setStatus("mandatory")
_GvcIfDlciLdevDmoTable_Object = MibTable
gvcIfDlciLdevDmoTable = _GvcIfDlciLdevDmoTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 6, 12)
)
if mibBuilder.loadTexts:
    gvcIfDlciLdevDmoTable.setStatus("mandatory")
_GvcIfDlciLdevDmoEntry_Object = MibTableRow
gvcIfDlciLdevDmoEntry = _GvcIfDlciLdevDmoEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 6, 12, 1)
)
gvcIfDlciLdevDmoEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfIndex"),
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfDlciIndex"),
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfDlciLdevIndex"),
)
if mibBuilder.loadTexts:
    gvcIfDlciLdevDmoEntry.setStatus("mandatory")


class _GvcIfDlciLdevDeviceMonitoring_Type(Integer32):
    """Custom type gvcIfDlciLdevDeviceMonitoring based on Integer32"""
    defaultValue = 1

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


_GvcIfDlciLdevDeviceMonitoring_Type.__name__ = "Integer32"
_GvcIfDlciLdevDeviceMonitoring_Object = MibTableColumn
gvcIfDlciLdevDeviceMonitoring = _GvcIfDlciLdevDeviceMonitoring_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 6, 12, 1, 1),
    _GvcIfDlciLdevDeviceMonitoring_Type()
)
gvcIfDlciLdevDeviceMonitoring.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gvcIfDlciLdevDeviceMonitoring.setStatus("mandatory")


class _GvcIfDlciLdevClearVcsWhenUnreachable_Type(Integer32):
    """Custom type gvcIfDlciLdevClearVcsWhenUnreachable based on Integer32"""
    defaultValue = 1

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


_GvcIfDlciLdevClearVcsWhenUnreachable_Type.__name__ = "Integer32"
_GvcIfDlciLdevClearVcsWhenUnreachable_Object = MibTableColumn
gvcIfDlciLdevClearVcsWhenUnreachable = _GvcIfDlciLdevClearVcsWhenUnreachable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 6, 12, 1, 2),
    _GvcIfDlciLdevClearVcsWhenUnreachable_Type()
)
gvcIfDlciLdevClearVcsWhenUnreachable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gvcIfDlciLdevClearVcsWhenUnreachable.setStatus("mandatory")


class _GvcIfDlciLdevDeviceMonitoringTimer_Type(Unsigned32):
    """Custom type gvcIfDlciLdevDeviceMonitoringTimer based on Unsigned32"""
    defaultValue = 15

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_GvcIfDlciLdevDeviceMonitoringTimer_Type.__name__ = "Unsigned32"
_GvcIfDlciLdevDeviceMonitoringTimer_Object = MibTableColumn
gvcIfDlciLdevDeviceMonitoringTimer = _GvcIfDlciLdevDeviceMonitoringTimer_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 6, 12, 1, 3),
    _GvcIfDlciLdevDeviceMonitoringTimer_Type()
)
gvcIfDlciLdevDeviceMonitoringTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gvcIfDlciLdevDeviceMonitoringTimer.setStatus("mandatory")


class _GvcIfDlciLdevTestResponseTimer_Type(Unsigned32):
    """Custom type gvcIfDlciLdevTestResponseTimer based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_GvcIfDlciLdevTestResponseTimer_Type.__name__ = "Unsigned32"
_GvcIfDlciLdevTestResponseTimer_Object = MibTableColumn
gvcIfDlciLdevTestResponseTimer = _GvcIfDlciLdevTestResponseTimer_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 6, 12, 1, 4),
    _GvcIfDlciLdevTestResponseTimer_Type()
)
gvcIfDlciLdevTestResponseTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gvcIfDlciLdevTestResponseTimer.setStatus("mandatory")


class _GvcIfDlciLdevMaximumTestRetry_Type(Unsigned32):
    """Custom type gvcIfDlciLdevMaximumTestRetry based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_GvcIfDlciLdevMaximumTestRetry_Type.__name__ = "Unsigned32"
_GvcIfDlciLdevMaximumTestRetry_Object = MibTableColumn
gvcIfDlciLdevMaximumTestRetry = _GvcIfDlciLdevMaximumTestRetry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 6, 12, 1, 5),
    _GvcIfDlciLdevMaximumTestRetry_Type()
)
gvcIfDlciLdevMaximumTestRetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gvcIfDlciLdevMaximumTestRetry.setStatus("mandatory")
_GvcIfDlciRdev_ObjectIdentity = ObjectIdentity
gvcIfDlciRdev = _GvcIfDlciRdev_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 7)
)
_GvcIfDlciRdevRowStatusTable_Object = MibTable
gvcIfDlciRdevRowStatusTable = _GvcIfDlciRdevRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 7, 1)
)
if mibBuilder.loadTexts:
    gvcIfDlciRdevRowStatusTable.setStatus("mandatory")
_GvcIfDlciRdevRowStatusEntry_Object = MibTableRow
gvcIfDlciRdevRowStatusEntry = _GvcIfDlciRdevRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 7, 1, 1)
)
gvcIfDlciRdevRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfIndex"),
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfDlciIndex"),
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfDlciRdevIndex"),
)
if mibBuilder.loadTexts:
    gvcIfDlciRdevRowStatusEntry.setStatus("mandatory")
_GvcIfDlciRdevRowStatus_Type = RowStatus
_GvcIfDlciRdevRowStatus_Object = MibTableColumn
gvcIfDlciRdevRowStatus = _GvcIfDlciRdevRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 7, 1, 1, 1),
    _GvcIfDlciRdevRowStatus_Type()
)
gvcIfDlciRdevRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gvcIfDlciRdevRowStatus.setStatus("mandatory")
_GvcIfDlciRdevComponentName_Type = DisplayString
_GvcIfDlciRdevComponentName_Object = MibTableColumn
gvcIfDlciRdevComponentName = _GvcIfDlciRdevComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 7, 1, 1, 2),
    _GvcIfDlciRdevComponentName_Type()
)
gvcIfDlciRdevComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfDlciRdevComponentName.setStatus("mandatory")
_GvcIfDlciRdevStorageType_Type = StorageType
_GvcIfDlciRdevStorageType_Object = MibTableColumn
gvcIfDlciRdevStorageType = _GvcIfDlciRdevStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 7, 1, 1, 4),
    _GvcIfDlciRdevStorageType_Type()
)
gvcIfDlciRdevStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfDlciRdevStorageType.setStatus("mandatory")
_GvcIfDlciRdevIndex_Type = NonReplicated
_GvcIfDlciRdevIndex_Object = MibTableColumn
gvcIfDlciRdevIndex = _GvcIfDlciRdevIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 7, 1, 1, 10),
    _GvcIfDlciRdevIndex_Type()
)
gvcIfDlciRdevIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gvcIfDlciRdevIndex.setStatus("mandatory")
_GvcIfDlciRdevAddrTable_Object = MibTable
gvcIfDlciRdevAddrTable = _GvcIfDlciRdevAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 7, 10)
)
if mibBuilder.loadTexts:
    gvcIfDlciRdevAddrTable.setStatus("mandatory")
_GvcIfDlciRdevAddrEntry_Object = MibTableRow
gvcIfDlciRdevAddrEntry = _GvcIfDlciRdevAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 7, 10, 1)
)
gvcIfDlciRdevAddrEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfIndex"),
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfDlciIndex"),
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfDlciRdevIndex"),
)
if mibBuilder.loadTexts:
    gvcIfDlciRdevAddrEntry.setStatus("mandatory")


class _GvcIfDlciRdevMac_Type(DashedHexString):
    """Custom type gvcIfDlciRdevMac based on DashedHexString"""
    subtypeSpec = DashedHexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_GvcIfDlciRdevMac_Type.__name__ = "DashedHexString"
_GvcIfDlciRdevMac_Object = MibTableColumn
gvcIfDlciRdevMac = _GvcIfDlciRdevMac_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 7, 10, 1, 1),
    _GvcIfDlciRdevMac_Type()
)
gvcIfDlciRdevMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gvcIfDlciRdevMac.setStatus("mandatory")
_GvcIfDlciSap_ObjectIdentity = ObjectIdentity
gvcIfDlciSap = _GvcIfDlciSap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 8)
)
_GvcIfDlciSapRowStatusTable_Object = MibTable
gvcIfDlciSapRowStatusTable = _GvcIfDlciSapRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 8, 1)
)
if mibBuilder.loadTexts:
    gvcIfDlciSapRowStatusTable.setStatus("mandatory")
_GvcIfDlciSapRowStatusEntry_Object = MibTableRow
gvcIfDlciSapRowStatusEntry = _GvcIfDlciSapRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 8, 1, 1)
)
gvcIfDlciSapRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfIndex"),
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfDlciIndex"),
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfDlciSapLocalSapIndex"),
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfDlciSapRemoteSapIndex"),
)
if mibBuilder.loadTexts:
    gvcIfDlciSapRowStatusEntry.setStatus("mandatory")
_GvcIfDlciSapRowStatus_Type = RowStatus
_GvcIfDlciSapRowStatus_Object = MibTableColumn
gvcIfDlciSapRowStatus = _GvcIfDlciSapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 8, 1, 1, 1),
    _GvcIfDlciSapRowStatus_Type()
)
gvcIfDlciSapRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfDlciSapRowStatus.setStatus("mandatory")
_GvcIfDlciSapComponentName_Type = DisplayString
_GvcIfDlciSapComponentName_Object = MibTableColumn
gvcIfDlciSapComponentName = _GvcIfDlciSapComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 8, 1, 1, 2),
    _GvcIfDlciSapComponentName_Type()
)
gvcIfDlciSapComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfDlciSapComponentName.setStatus("mandatory")
_GvcIfDlciSapStorageType_Type = StorageType
_GvcIfDlciSapStorageType_Object = MibTableColumn
gvcIfDlciSapStorageType = _GvcIfDlciSapStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 8, 1, 1, 4),
    _GvcIfDlciSapStorageType_Type()
)
gvcIfDlciSapStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfDlciSapStorageType.setStatus("mandatory")


class _GvcIfDlciSapLocalSapIndex_Type(Integer32):
    """Custom type gvcIfDlciSapLocalSapIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 4),
        ValueRangeConstraint(8, 8),
        ValueRangeConstraint(12, 12),
        ValueRangeConstraint(16, 16),
        ValueRangeConstraint(20, 20),
        ValueRangeConstraint(24, 24),
        ValueRangeConstraint(28, 28),
        ValueRangeConstraint(32, 32),
        ValueRangeConstraint(36, 36),
        ValueRangeConstraint(40, 40),
        ValueRangeConstraint(44, 44),
        ValueRangeConstraint(48, 48),
        ValueRangeConstraint(52, 52),
        ValueRangeConstraint(56, 56),
        ValueRangeConstraint(60, 60),
        ValueRangeConstraint(64, 64),
        ValueRangeConstraint(68, 68),
        ValueRangeConstraint(72, 72),
        ValueRangeConstraint(76, 76),
        ValueRangeConstraint(80, 80),
        ValueRangeConstraint(84, 84),
        ValueRangeConstraint(88, 88),
        ValueRangeConstraint(92, 92),
        ValueRangeConstraint(96, 96),
        ValueRangeConstraint(100, 100),
        ValueRangeConstraint(104, 104),
        ValueRangeConstraint(108, 108),
        ValueRangeConstraint(112, 112),
        ValueRangeConstraint(116, 116),
        ValueRangeConstraint(120, 120),
        ValueRangeConstraint(124, 124),
        ValueRangeConstraint(128, 128),
        ValueRangeConstraint(132, 132),
        ValueRangeConstraint(136, 136),
        ValueRangeConstraint(140, 140),
        ValueRangeConstraint(144, 144),
        ValueRangeConstraint(148, 148),
        ValueRangeConstraint(152, 152),
        ValueRangeConstraint(156, 156),
        ValueRangeConstraint(160, 160),
        ValueRangeConstraint(164, 164),
        ValueRangeConstraint(168, 168),
        ValueRangeConstraint(172, 172),
        ValueRangeConstraint(176, 176),
        ValueRangeConstraint(180, 180),
        ValueRangeConstraint(184, 184),
        ValueRangeConstraint(188, 188),
        ValueRangeConstraint(192, 192),
        ValueRangeConstraint(196, 196),
        ValueRangeConstraint(200, 200),
        ValueRangeConstraint(204, 204),
        ValueRangeConstraint(208, 208),
        ValueRangeConstraint(212, 212),
        ValueRangeConstraint(216, 216),
        ValueRangeConstraint(220, 220),
        ValueRangeConstraint(232, 232),
        ValueRangeConstraint(236, 236),
        ValueRangeConstraint(248, 248),
        ValueRangeConstraint(252, 252),
    )


_GvcIfDlciSapLocalSapIndex_Type.__name__ = "Integer32"
_GvcIfDlciSapLocalSapIndex_Object = MibTableColumn
gvcIfDlciSapLocalSapIndex = _GvcIfDlciSapLocalSapIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 8, 1, 1, 10),
    _GvcIfDlciSapLocalSapIndex_Type()
)
gvcIfDlciSapLocalSapIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gvcIfDlciSapLocalSapIndex.setStatus("mandatory")


class _GvcIfDlciSapRemoteSapIndex_Type(Integer32):
    """Custom type gvcIfDlciSapRemoteSapIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 4),
        ValueRangeConstraint(8, 8),
        ValueRangeConstraint(12, 12),
        ValueRangeConstraint(16, 16),
        ValueRangeConstraint(20, 20),
        ValueRangeConstraint(24, 24),
        ValueRangeConstraint(28, 28),
        ValueRangeConstraint(32, 32),
        ValueRangeConstraint(36, 36),
        ValueRangeConstraint(40, 40),
        ValueRangeConstraint(44, 44),
        ValueRangeConstraint(48, 48),
        ValueRangeConstraint(52, 52),
        ValueRangeConstraint(56, 56),
        ValueRangeConstraint(60, 60),
        ValueRangeConstraint(64, 64),
        ValueRangeConstraint(68, 68),
        ValueRangeConstraint(72, 72),
        ValueRangeConstraint(76, 76),
        ValueRangeConstraint(80, 80),
        ValueRangeConstraint(84, 84),
        ValueRangeConstraint(88, 88),
        ValueRangeConstraint(92, 92),
        ValueRangeConstraint(96, 96),
        ValueRangeConstraint(100, 100),
        ValueRangeConstraint(104, 104),
        ValueRangeConstraint(108, 108),
        ValueRangeConstraint(112, 112),
        ValueRangeConstraint(116, 116),
        ValueRangeConstraint(120, 120),
        ValueRangeConstraint(124, 124),
        ValueRangeConstraint(128, 128),
        ValueRangeConstraint(132, 132),
        ValueRangeConstraint(136, 136),
        ValueRangeConstraint(140, 140),
        ValueRangeConstraint(144, 144),
        ValueRangeConstraint(148, 148),
        ValueRangeConstraint(152, 152),
        ValueRangeConstraint(156, 156),
        ValueRangeConstraint(160, 160),
        ValueRangeConstraint(164, 164),
        ValueRangeConstraint(168, 168),
        ValueRangeConstraint(172, 172),
        ValueRangeConstraint(176, 176),
        ValueRangeConstraint(180, 180),
        ValueRangeConstraint(184, 184),
        ValueRangeConstraint(188, 188),
        ValueRangeConstraint(192, 192),
        ValueRangeConstraint(196, 196),
        ValueRangeConstraint(200, 200),
        ValueRangeConstraint(204, 204),
        ValueRangeConstraint(208, 208),
        ValueRangeConstraint(212, 212),
        ValueRangeConstraint(216, 216),
        ValueRangeConstraint(220, 220),
        ValueRangeConstraint(232, 232),
        ValueRangeConstraint(236, 236),
        ValueRangeConstraint(248, 248),
        ValueRangeConstraint(252, 252),
    )


_GvcIfDlciSapRemoteSapIndex_Type.__name__ = "Integer32"
_GvcIfDlciSapRemoteSapIndex_Object = MibTableColumn
gvcIfDlciSapRemoteSapIndex = _GvcIfDlciSapRemoteSapIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 8, 1, 1, 11),
    _GvcIfDlciSapRemoteSapIndex_Type()
)
gvcIfDlciSapRemoteSapIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gvcIfDlciSapRemoteSapIndex.setStatus("mandatory")
_GvcIfDlciSapCircuit_ObjectIdentity = ObjectIdentity
gvcIfDlciSapCircuit = _GvcIfDlciSapCircuit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 8, 2)
)
_GvcIfDlciSapCircuitRowStatusTable_Object = MibTable
gvcIfDlciSapCircuitRowStatusTable = _GvcIfDlciSapCircuitRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 8, 2, 1)
)
if mibBuilder.loadTexts:
    gvcIfDlciSapCircuitRowStatusTable.setStatus("mandatory")
_GvcIfDlciSapCircuitRowStatusEntry_Object = MibTableRow
gvcIfDlciSapCircuitRowStatusEntry = _GvcIfDlciSapCircuitRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 8, 2, 1, 1)
)
gvcIfDlciSapCircuitRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfIndex"),
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfDlciIndex"),
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfDlciSapLocalSapIndex"),
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfDlciSapRemoteSapIndex"),
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfDlciSapCircuitS1MacIndex"),
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfDlciSapCircuitS1SapIndex"),
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfDlciSapCircuitS2MacIndex"),
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfDlciSapCircuitS2SapIndex"),
)
if mibBuilder.loadTexts:
    gvcIfDlciSapCircuitRowStatusEntry.setStatus("mandatory")
_GvcIfDlciSapCircuitRowStatus_Type = RowStatus
_GvcIfDlciSapCircuitRowStatus_Object = MibTableColumn
gvcIfDlciSapCircuitRowStatus = _GvcIfDlciSapCircuitRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 8, 2, 1, 1, 1),
    _GvcIfDlciSapCircuitRowStatus_Type()
)
gvcIfDlciSapCircuitRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfDlciSapCircuitRowStatus.setStatus("mandatory")
_GvcIfDlciSapCircuitComponentName_Type = DisplayString
_GvcIfDlciSapCircuitComponentName_Object = MibTableColumn
gvcIfDlciSapCircuitComponentName = _GvcIfDlciSapCircuitComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 8, 2, 1, 1, 2),
    _GvcIfDlciSapCircuitComponentName_Type()
)
gvcIfDlciSapCircuitComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfDlciSapCircuitComponentName.setStatus("mandatory")
_GvcIfDlciSapCircuitStorageType_Type = StorageType
_GvcIfDlciSapCircuitStorageType_Object = MibTableColumn
gvcIfDlciSapCircuitStorageType = _GvcIfDlciSapCircuitStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 8, 2, 1, 1, 4),
    _GvcIfDlciSapCircuitStorageType_Type()
)
gvcIfDlciSapCircuitStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfDlciSapCircuitStorageType.setStatus("mandatory")


class _GvcIfDlciSapCircuitS1MacIndex_Type(DashedHexString):
    """Custom type gvcIfDlciSapCircuitS1MacIndex based on DashedHexString"""
    subtypeSpec = DashedHexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_GvcIfDlciSapCircuitS1MacIndex_Type.__name__ = "DashedHexString"
_GvcIfDlciSapCircuitS1MacIndex_Object = MibTableColumn
gvcIfDlciSapCircuitS1MacIndex = _GvcIfDlciSapCircuitS1MacIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 8, 2, 1, 1, 10),
    _GvcIfDlciSapCircuitS1MacIndex_Type()
)
gvcIfDlciSapCircuitS1MacIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gvcIfDlciSapCircuitS1MacIndex.setStatus("mandatory")


class _GvcIfDlciSapCircuitS1SapIndex_Type(Integer32):
    """Custom type gvcIfDlciSapCircuitS1SapIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 254),
    )


_GvcIfDlciSapCircuitS1SapIndex_Type.__name__ = "Integer32"
_GvcIfDlciSapCircuitS1SapIndex_Object = MibTableColumn
gvcIfDlciSapCircuitS1SapIndex = _GvcIfDlciSapCircuitS1SapIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 8, 2, 1, 1, 11),
    _GvcIfDlciSapCircuitS1SapIndex_Type()
)
gvcIfDlciSapCircuitS1SapIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gvcIfDlciSapCircuitS1SapIndex.setStatus("mandatory")


class _GvcIfDlciSapCircuitS2MacIndex_Type(DashedHexString):
    """Custom type gvcIfDlciSapCircuitS2MacIndex based on DashedHexString"""
    subtypeSpec = DashedHexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_GvcIfDlciSapCircuitS2MacIndex_Type.__name__ = "DashedHexString"
_GvcIfDlciSapCircuitS2MacIndex_Object = MibTableColumn
gvcIfDlciSapCircuitS2MacIndex = _GvcIfDlciSapCircuitS2MacIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 8, 2, 1, 1, 12),
    _GvcIfDlciSapCircuitS2MacIndex_Type()
)
gvcIfDlciSapCircuitS2MacIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gvcIfDlciSapCircuitS2MacIndex.setStatus("mandatory")


class _GvcIfDlciSapCircuitS2SapIndex_Type(Integer32):
    """Custom type gvcIfDlciSapCircuitS2SapIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 254),
    )


_GvcIfDlciSapCircuitS2SapIndex_Type.__name__ = "Integer32"
_GvcIfDlciSapCircuitS2SapIndex_Object = MibTableColumn
gvcIfDlciSapCircuitS2SapIndex = _GvcIfDlciSapCircuitS2SapIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 8, 2, 1, 1, 13),
    _GvcIfDlciSapCircuitS2SapIndex_Type()
)
gvcIfDlciSapCircuitS2SapIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gvcIfDlciSapCircuitS2SapIndex.setStatus("mandatory")
_GvcIfDlciStateTable_Object = MibTable
gvcIfDlciStateTable = _GvcIfDlciStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 10)
)
if mibBuilder.loadTexts:
    gvcIfDlciStateTable.setStatus("mandatory")
_GvcIfDlciStateEntry_Object = MibTableRow
gvcIfDlciStateEntry = _GvcIfDlciStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 10, 1)
)
gvcIfDlciStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfIndex"),
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfDlciIndex"),
)
if mibBuilder.loadTexts:
    gvcIfDlciStateEntry.setStatus("mandatory")


class _GvcIfDlciAdminState_Type(Integer32):
    """Custom type gvcIfDlciAdminState based on Integer32"""
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


_GvcIfDlciAdminState_Type.__name__ = "Integer32"
_GvcIfDlciAdminState_Object = MibTableColumn
gvcIfDlciAdminState = _GvcIfDlciAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 10, 1, 1),
    _GvcIfDlciAdminState_Type()
)
gvcIfDlciAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfDlciAdminState.setStatus("mandatory")


class _GvcIfDlciOperationalState_Type(Integer32):
    """Custom type gvcIfDlciOperationalState based on Integer32"""
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


_GvcIfDlciOperationalState_Type.__name__ = "Integer32"
_GvcIfDlciOperationalState_Object = MibTableColumn
gvcIfDlciOperationalState = _GvcIfDlciOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 10, 1, 2),
    _GvcIfDlciOperationalState_Type()
)
gvcIfDlciOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfDlciOperationalState.setStatus("mandatory")


class _GvcIfDlciUsageState_Type(Integer32):
    """Custom type gvcIfDlciUsageState based on Integer32"""
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


_GvcIfDlciUsageState_Type.__name__ = "Integer32"
_GvcIfDlciUsageState_Object = MibTableColumn
gvcIfDlciUsageState = _GvcIfDlciUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 10, 1, 3),
    _GvcIfDlciUsageState_Type()
)
gvcIfDlciUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfDlciUsageState.setStatus("mandatory")
_GvcIfDlciAbitTable_Object = MibTable
gvcIfDlciAbitTable = _GvcIfDlciAbitTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 11)
)
if mibBuilder.loadTexts:
    gvcIfDlciAbitTable.setStatus("mandatory")
_GvcIfDlciAbitEntry_Object = MibTableRow
gvcIfDlciAbitEntry = _GvcIfDlciAbitEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 11, 1)
)
gvcIfDlciAbitEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfIndex"),
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfDlciIndex"),
)
if mibBuilder.loadTexts:
    gvcIfDlciAbitEntry.setStatus("mandatory")


class _GvcIfDlciABitStatusFromNetwork_Type(Integer32):
    """Custom type gvcIfDlciABitStatusFromNetwork based on Integer32"""
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
          ("inactive", 0),
          ("notApplicable", 2))
    )


_GvcIfDlciABitStatusFromNetwork_Type.__name__ = "Integer32"
_GvcIfDlciABitStatusFromNetwork_Object = MibTableColumn
gvcIfDlciABitStatusFromNetwork = _GvcIfDlciABitStatusFromNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 11, 1, 1),
    _GvcIfDlciABitStatusFromNetwork_Type()
)
gvcIfDlciABitStatusFromNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfDlciABitStatusFromNetwork.setStatus("mandatory")


class _GvcIfDlciABitReasonFromNetwork_Type(Integer32):
    """Custom type gvcIfDlciABitReasonFromNetwork based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("localLinkDown", 4),
          ("localLmiError", 2),
          ("notApplicable", 0),
          ("pvcDown", 6),
          ("remoteLinkDown", 5),
          ("remoteLmiError", 3),
          ("remoteUserSignaled", 1))
    )


_GvcIfDlciABitReasonFromNetwork_Type.__name__ = "Integer32"
_GvcIfDlciABitReasonFromNetwork_Object = MibTableColumn
gvcIfDlciABitReasonFromNetwork = _GvcIfDlciABitReasonFromNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 11, 1, 2),
    _GvcIfDlciABitReasonFromNetwork_Type()
)
gvcIfDlciABitReasonFromNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfDlciABitReasonFromNetwork.setStatus("mandatory")


class _GvcIfDlciABitStatusToNetwork_Type(Integer32):
    """Custom type gvcIfDlciABitStatusToNetwork based on Integer32"""
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
          ("inactive", 0),
          ("notApplicable", 2))
    )


_GvcIfDlciABitStatusToNetwork_Type.__name__ = "Integer32"
_GvcIfDlciABitStatusToNetwork_Object = MibTableColumn
gvcIfDlciABitStatusToNetwork = _GvcIfDlciABitStatusToNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 11, 1, 3),
    _GvcIfDlciABitStatusToNetwork_Type()
)
gvcIfDlciABitStatusToNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfDlciABitStatusToNetwork.setStatus("mandatory")


class _GvcIfDlciABitReasonToNetwork_Type(Integer32):
    """Custom type gvcIfDlciABitReasonToNetwork based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4,
              7)
        )
    )
    namedValues = NamedValues(
        *(("localLinkDown", 4),
          ("localLmiError", 2),
          ("missingFromLmiReport", 7),
          ("notApplicable", 0),
          ("remoteUserSignaled", 1))
    )


_GvcIfDlciABitReasonToNetwork_Type.__name__ = "Integer32"
_GvcIfDlciABitReasonToNetwork_Object = MibTableColumn
gvcIfDlciABitReasonToNetwork = _GvcIfDlciABitReasonToNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 11, 1, 4),
    _GvcIfDlciABitReasonToNetwork_Type()
)
gvcIfDlciABitReasonToNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfDlciABitReasonToNetwork.setStatus("mandatory")
_GvcIfDlciStatsTable_Object = MibTable
gvcIfDlciStatsTable = _GvcIfDlciStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 12)
)
if mibBuilder.loadTexts:
    gvcIfDlciStatsTable.setStatus("mandatory")
_GvcIfDlciStatsEntry_Object = MibTableRow
gvcIfDlciStatsEntry = _GvcIfDlciStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 12, 1)
)
gvcIfDlciStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfIndex"),
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfDlciIndex"),
)
if mibBuilder.loadTexts:
    gvcIfDlciStatsEntry.setStatus("mandatory")
_GvcIfDlciFrmFromNetwork_Type = Counter32
_GvcIfDlciFrmFromNetwork_Object = MibTableColumn
gvcIfDlciFrmFromNetwork = _GvcIfDlciFrmFromNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 12, 1, 1),
    _GvcIfDlciFrmFromNetwork_Type()
)
gvcIfDlciFrmFromNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfDlciFrmFromNetwork.setStatus("mandatory")
_GvcIfDlciFrmToNetwork_Type = Counter32
_GvcIfDlciFrmToNetwork_Object = MibTableColumn
gvcIfDlciFrmToNetwork = _GvcIfDlciFrmToNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 12, 1, 2),
    _GvcIfDlciFrmToNetwork_Type()
)
gvcIfDlciFrmToNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfDlciFrmToNetwork.setStatus("mandatory")
_GvcIfDlciFrmDiscardToNetwork_Type = Counter32
_GvcIfDlciFrmDiscardToNetwork_Object = MibTableColumn
gvcIfDlciFrmDiscardToNetwork = _GvcIfDlciFrmDiscardToNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 12, 1, 3),
    _GvcIfDlciFrmDiscardToNetwork_Type()
)
gvcIfDlciFrmDiscardToNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfDlciFrmDiscardToNetwork.setStatus("mandatory")
_GvcIfDlciFramesWithUnknownSaps_Type = Counter32
_GvcIfDlciFramesWithUnknownSaps_Object = MibTableColumn
gvcIfDlciFramesWithUnknownSaps = _GvcIfDlciFramesWithUnknownSaps_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 12, 1, 4),
    _GvcIfDlciFramesWithUnknownSaps_Type()
)
gvcIfDlciFramesWithUnknownSaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfDlciFramesWithUnknownSaps.setStatus("mandatory")
_GvcIfDlciOperTable_Object = MibTable
gvcIfDlciOperTable = _GvcIfDlciOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 13)
)
if mibBuilder.loadTexts:
    gvcIfDlciOperTable.setStatus("mandatory")
_GvcIfDlciOperEntry_Object = MibTableRow
gvcIfDlciOperEntry = _GvcIfDlciOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 13, 1)
)
gvcIfDlciOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfIndex"),
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfDlciIndex"),
)
if mibBuilder.loadTexts:
    gvcIfDlciOperEntry.setStatus("mandatory")


class _GvcIfDlciEncapsulationType_Type(Integer32):
    """Custom type gvcIfDlciEncapsulationType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ban", 0),
          ("bnn", 1))
    )


_GvcIfDlciEncapsulationType_Type.__name__ = "Integer32"
_GvcIfDlciEncapsulationType_Object = MibTableColumn
gvcIfDlciEncapsulationType = _GvcIfDlciEncapsulationType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 13, 1, 1),
    _GvcIfDlciEncapsulationType_Type()
)
gvcIfDlciEncapsulationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfDlciEncapsulationType.setStatus("mandatory")


class _GvcIfDlciLocalDeviceMac_Type(DashedHexString):
    """Custom type gvcIfDlciLocalDeviceMac based on DashedHexString"""
    subtypeSpec = DashedHexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_GvcIfDlciLocalDeviceMac_Type.__name__ = "DashedHexString"
_GvcIfDlciLocalDeviceMac_Object = MibTableColumn
gvcIfDlciLocalDeviceMac = _GvcIfDlciLocalDeviceMac_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 13, 1, 2),
    _GvcIfDlciLocalDeviceMac_Type()
)
gvcIfDlciLocalDeviceMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfDlciLocalDeviceMac.setStatus("mandatory")


class _GvcIfDlciRemoteDeviceMac_Type(DashedHexString):
    """Custom type gvcIfDlciRemoteDeviceMac based on DashedHexString"""
    subtypeSpec = DashedHexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_GvcIfDlciRemoteDeviceMac_Type.__name__ = "DashedHexString"
_GvcIfDlciRemoteDeviceMac_Object = MibTableColumn
gvcIfDlciRemoteDeviceMac = _GvcIfDlciRemoteDeviceMac_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 13, 1, 3),
    _GvcIfDlciRemoteDeviceMac_Type()
)
gvcIfDlciRemoteDeviceMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfDlciRemoteDeviceMac.setStatus("mandatory")
_GvcIfDlciSpOpTable_Object = MibTable
gvcIfDlciSpOpTable = _GvcIfDlciSpOpTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 14)
)
if mibBuilder.loadTexts:
    gvcIfDlciSpOpTable.setStatus("mandatory")
_GvcIfDlciSpOpEntry_Object = MibTableRow
gvcIfDlciSpOpEntry = _GvcIfDlciSpOpEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 14, 1)
)
gvcIfDlciSpOpEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfIndex"),
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfDlciIndex"),
)
if mibBuilder.loadTexts:
    gvcIfDlciSpOpEntry.setStatus("mandatory")


class _GvcIfDlciRateEnforcement_Type(Integer32):
    """Custom type gvcIfDlciRateEnforcement based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_GvcIfDlciRateEnforcement_Type.__name__ = "Integer32"
_GvcIfDlciRateEnforcement_Object = MibTableColumn
gvcIfDlciRateEnforcement = _GvcIfDlciRateEnforcement_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 14, 1, 1),
    _GvcIfDlciRateEnforcement_Type()
)
gvcIfDlciRateEnforcement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfDlciRateEnforcement.setStatus("mandatory")


class _GvcIfDlciCommittedInformationRate_Type(Gauge32):
    """Custom type gvcIfDlciCommittedInformationRate based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_GvcIfDlciCommittedInformationRate_Type.__name__ = "Gauge32"
_GvcIfDlciCommittedInformationRate_Object = MibTableColumn
gvcIfDlciCommittedInformationRate = _GvcIfDlciCommittedInformationRate_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 14, 1, 2),
    _GvcIfDlciCommittedInformationRate_Type()
)
gvcIfDlciCommittedInformationRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfDlciCommittedInformationRate.setStatus("mandatory")


class _GvcIfDlciCommittedBurstSize_Type(Gauge32):
    """Custom type gvcIfDlciCommittedBurstSize based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_GvcIfDlciCommittedBurstSize_Type.__name__ = "Gauge32"
_GvcIfDlciCommittedBurstSize_Object = MibTableColumn
gvcIfDlciCommittedBurstSize = _GvcIfDlciCommittedBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 14, 1, 3),
    _GvcIfDlciCommittedBurstSize_Type()
)
gvcIfDlciCommittedBurstSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfDlciCommittedBurstSize.setStatus("mandatory")


class _GvcIfDlciExcessInformationRate_Type(Gauge32):
    """Custom type gvcIfDlciExcessInformationRate based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_GvcIfDlciExcessInformationRate_Type.__name__ = "Gauge32"
_GvcIfDlciExcessInformationRate_Object = MibTableColumn
gvcIfDlciExcessInformationRate = _GvcIfDlciExcessInformationRate_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 14, 1, 4),
    _GvcIfDlciExcessInformationRate_Type()
)
gvcIfDlciExcessInformationRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfDlciExcessInformationRate.setStatus("mandatory")


class _GvcIfDlciExcessBurstSize_Type(Gauge32):
    """Custom type gvcIfDlciExcessBurstSize based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2048000),
    )


_GvcIfDlciExcessBurstSize_Type.__name__ = "Gauge32"
_GvcIfDlciExcessBurstSize_Object = MibTableColumn
gvcIfDlciExcessBurstSize = _GvcIfDlciExcessBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 14, 1, 5),
    _GvcIfDlciExcessBurstSize_Type()
)
gvcIfDlciExcessBurstSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfDlciExcessBurstSize.setStatus("mandatory")


class _GvcIfDlciMeasurementInterval_Type(Gauge32):
    """Custom type gvcIfDlciMeasurementInterval based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 25500),
    )


_GvcIfDlciMeasurementInterval_Type.__name__ = "Gauge32"
_GvcIfDlciMeasurementInterval_Object = MibTableColumn
gvcIfDlciMeasurementInterval = _GvcIfDlciMeasurementInterval_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 7, 14, 1, 6),
    _GvcIfDlciMeasurementInterval_Type()
)
gvcIfDlciMeasurementInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfDlciMeasurementInterval.setStatus("mandatory")
_GvcIfFrSvc_ObjectIdentity = ObjectIdentity
gvcIfFrSvc = _GvcIfFrSvc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 8)
)
_GvcIfFrSvcRowStatusTable_Object = MibTable
gvcIfFrSvcRowStatusTable = _GvcIfFrSvcRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 8, 1)
)
if mibBuilder.loadTexts:
    gvcIfFrSvcRowStatusTable.setStatus("mandatory")
_GvcIfFrSvcRowStatusEntry_Object = MibTableRow
gvcIfFrSvcRowStatusEntry = _GvcIfFrSvcRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 8, 1, 1)
)
gvcIfFrSvcRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfIndex"),
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfFrSvcIndex"),
)
if mibBuilder.loadTexts:
    gvcIfFrSvcRowStatusEntry.setStatus("mandatory")
_GvcIfFrSvcRowStatus_Type = RowStatus
_GvcIfFrSvcRowStatus_Object = MibTableColumn
gvcIfFrSvcRowStatus = _GvcIfFrSvcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 8, 1, 1, 1),
    _GvcIfFrSvcRowStatus_Type()
)
gvcIfFrSvcRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gvcIfFrSvcRowStatus.setStatus("mandatory")
_GvcIfFrSvcComponentName_Type = DisplayString
_GvcIfFrSvcComponentName_Object = MibTableColumn
gvcIfFrSvcComponentName = _GvcIfFrSvcComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 8, 1, 1, 2),
    _GvcIfFrSvcComponentName_Type()
)
gvcIfFrSvcComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfFrSvcComponentName.setStatus("mandatory")
_GvcIfFrSvcStorageType_Type = StorageType
_GvcIfFrSvcStorageType_Object = MibTableColumn
gvcIfFrSvcStorageType = _GvcIfFrSvcStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 8, 1, 1, 4),
    _GvcIfFrSvcStorageType_Type()
)
gvcIfFrSvcStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfFrSvcStorageType.setStatus("mandatory")
_GvcIfFrSvcIndex_Type = NonReplicated
_GvcIfFrSvcIndex_Object = MibTableColumn
gvcIfFrSvcIndex = _GvcIfFrSvcIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 8, 1, 1, 10),
    _GvcIfFrSvcIndex_Type()
)
gvcIfFrSvcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gvcIfFrSvcIndex.setStatus("mandatory")
_GvcIfFrSvcProvisionedTable_Object = MibTable
gvcIfFrSvcProvisionedTable = _GvcIfFrSvcProvisionedTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 8, 11)
)
if mibBuilder.loadTexts:
    gvcIfFrSvcProvisionedTable.setStatus("mandatory")
_GvcIfFrSvcProvisionedEntry_Object = MibTableRow
gvcIfFrSvcProvisionedEntry = _GvcIfFrSvcProvisionedEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 8, 11, 1)
)
gvcIfFrSvcProvisionedEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfIndex"),
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfFrSvcIndex"),
)
if mibBuilder.loadTexts:
    gvcIfFrSvcProvisionedEntry.setStatus("mandatory")


class _GvcIfFrSvcMaximumFrameRelaySvcs_Type(Unsigned32):
    """Custom type gvcIfFrSvcMaximumFrameRelaySvcs based on Unsigned32"""
    defaultValue = 1000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3072),
    )


_GvcIfFrSvcMaximumFrameRelaySvcs_Type.__name__ = "Unsigned32"
_GvcIfFrSvcMaximumFrameRelaySvcs_Object = MibTableColumn
gvcIfFrSvcMaximumFrameRelaySvcs = _GvcIfFrSvcMaximumFrameRelaySvcs_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 8, 11, 1, 1),
    _GvcIfFrSvcMaximumFrameRelaySvcs_Type()
)
gvcIfFrSvcMaximumFrameRelaySvcs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gvcIfFrSvcMaximumFrameRelaySvcs.setStatus("mandatory")


class _GvcIfFrSvcRateEnforcement_Type(Integer32):
    """Custom type gvcIfFrSvcRateEnforcement based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_GvcIfFrSvcRateEnforcement_Type.__name__ = "Integer32"
_GvcIfFrSvcRateEnforcement_Object = MibTableColumn
gvcIfFrSvcRateEnforcement = _GvcIfFrSvcRateEnforcement_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 8, 11, 1, 2),
    _GvcIfFrSvcRateEnforcement_Type()
)
gvcIfFrSvcRateEnforcement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gvcIfFrSvcRateEnforcement.setStatus("mandatory")


class _GvcIfFrSvcMaximumCir_Type(Unsigned32):
    """Custom type gvcIfFrSvcMaximumCir based on Unsigned32"""
    defaultValue = 2048000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 52000000),
    )


_GvcIfFrSvcMaximumCir_Type.__name__ = "Unsigned32"
_GvcIfFrSvcMaximumCir_Object = MibTableColumn
gvcIfFrSvcMaximumCir = _GvcIfFrSvcMaximumCir_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 8, 11, 1, 4),
    _GvcIfFrSvcMaximumCir_Type()
)
gvcIfFrSvcMaximumCir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gvcIfFrSvcMaximumCir.setStatus("mandatory")
_GvcIfFrSvcOperationalTable_Object = MibTable
gvcIfFrSvcOperationalTable = _GvcIfFrSvcOperationalTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 8, 12)
)
if mibBuilder.loadTexts:
    gvcIfFrSvcOperationalTable.setStatus("mandatory")
_GvcIfFrSvcOperationalEntry_Object = MibTableRow
gvcIfFrSvcOperationalEntry = _GvcIfFrSvcOperationalEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 8, 12, 1)
)
gvcIfFrSvcOperationalEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfIndex"),
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfFrSvcIndex"),
)
if mibBuilder.loadTexts:
    gvcIfFrSvcOperationalEntry.setStatus("mandatory")


class _GvcIfFrSvcCurrentNumberOfSvcCalls_Type(Gauge32):
    """Custom type gvcIfFrSvcCurrentNumberOfSvcCalls based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3072),
    )


_GvcIfFrSvcCurrentNumberOfSvcCalls_Type.__name__ = "Gauge32"
_GvcIfFrSvcCurrentNumberOfSvcCalls_Object = MibTableColumn
gvcIfFrSvcCurrentNumberOfSvcCalls = _GvcIfFrSvcCurrentNumberOfSvcCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 8, 12, 1, 1),
    _GvcIfFrSvcCurrentNumberOfSvcCalls_Type()
)
gvcIfFrSvcCurrentNumberOfSvcCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfFrSvcCurrentNumberOfSvcCalls.setStatus("mandatory")
_GvcIfSMacF_ObjectIdentity = ObjectIdentity
gvcIfSMacF = _GvcIfSMacF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 9)
)
_GvcIfSMacFRowStatusTable_Object = MibTable
gvcIfSMacFRowStatusTable = _GvcIfSMacFRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 9, 1)
)
if mibBuilder.loadTexts:
    gvcIfSMacFRowStatusTable.setStatus("mandatory")
_GvcIfSMacFRowStatusEntry_Object = MibTableRow
gvcIfSMacFRowStatusEntry = _GvcIfSMacFRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 9, 1, 1)
)
gvcIfSMacFRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfIndex"),
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfSMacFIndex"),
)
if mibBuilder.loadTexts:
    gvcIfSMacFRowStatusEntry.setStatus("mandatory")
_GvcIfSMacFRowStatus_Type = RowStatus
_GvcIfSMacFRowStatus_Object = MibTableColumn
gvcIfSMacFRowStatus = _GvcIfSMacFRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 9, 1, 1, 1),
    _GvcIfSMacFRowStatus_Type()
)
gvcIfSMacFRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gvcIfSMacFRowStatus.setStatus("mandatory")
_GvcIfSMacFComponentName_Type = DisplayString
_GvcIfSMacFComponentName_Object = MibTableColumn
gvcIfSMacFComponentName = _GvcIfSMacFComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 9, 1, 1, 2),
    _GvcIfSMacFComponentName_Type()
)
gvcIfSMacFComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfSMacFComponentName.setStatus("mandatory")
_GvcIfSMacFStorageType_Type = StorageType
_GvcIfSMacFStorageType_Object = MibTableColumn
gvcIfSMacFStorageType = _GvcIfSMacFStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 9, 1, 1, 4),
    _GvcIfSMacFStorageType_Type()
)
gvcIfSMacFStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfSMacFStorageType.setStatus("mandatory")


class _GvcIfSMacFIndex_Type(DashedHexString):
    """Custom type gvcIfSMacFIndex based on DashedHexString"""
    subtypeSpec = DashedHexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_GvcIfSMacFIndex_Type.__name__ = "DashedHexString"
_GvcIfSMacFIndex_Object = MibTableColumn
gvcIfSMacFIndex = _GvcIfSMacFIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 9, 1, 1, 10),
    _GvcIfSMacFIndex_Type()
)
gvcIfSMacFIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gvcIfSMacFIndex.setStatus("mandatory")
_GvcIfSMacFOperTable_Object = MibTable
gvcIfSMacFOperTable = _GvcIfSMacFOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 9, 11)
)
if mibBuilder.loadTexts:
    gvcIfSMacFOperTable.setStatus("mandatory")
_GvcIfSMacFOperEntry_Object = MibTableRow
gvcIfSMacFOperEntry = _GvcIfSMacFOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 9, 11, 1)
)
gvcIfSMacFOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfIndex"),
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfSMacFIndex"),
)
if mibBuilder.loadTexts:
    gvcIfSMacFOperEntry.setStatus("mandatory")
_GvcIfSMacFFramesMatchingFilter_Type = Counter32
_GvcIfSMacFFramesMatchingFilter_Object = MibTableColumn
gvcIfSMacFFramesMatchingFilter = _GvcIfSMacFFramesMatchingFilter_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 9, 11, 1, 1),
    _GvcIfSMacFFramesMatchingFilter_Type()
)
gvcIfSMacFFramesMatchingFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfSMacFFramesMatchingFilter.setStatus("mandatory")
_GvcIfDMacF_ObjectIdentity = ObjectIdentity
gvcIfDMacF = _GvcIfDMacF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 10)
)
_GvcIfDMacFRowStatusTable_Object = MibTable
gvcIfDMacFRowStatusTable = _GvcIfDMacFRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 10, 1)
)
if mibBuilder.loadTexts:
    gvcIfDMacFRowStatusTable.setStatus("mandatory")
_GvcIfDMacFRowStatusEntry_Object = MibTableRow
gvcIfDMacFRowStatusEntry = _GvcIfDMacFRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 10, 1, 1)
)
gvcIfDMacFRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfIndex"),
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfDMacFIndex"),
)
if mibBuilder.loadTexts:
    gvcIfDMacFRowStatusEntry.setStatus("mandatory")
_GvcIfDMacFRowStatus_Type = RowStatus
_GvcIfDMacFRowStatus_Object = MibTableColumn
gvcIfDMacFRowStatus = _GvcIfDMacFRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 10, 1, 1, 1),
    _GvcIfDMacFRowStatus_Type()
)
gvcIfDMacFRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gvcIfDMacFRowStatus.setStatus("mandatory")
_GvcIfDMacFComponentName_Type = DisplayString
_GvcIfDMacFComponentName_Object = MibTableColumn
gvcIfDMacFComponentName = _GvcIfDMacFComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 10, 1, 1, 2),
    _GvcIfDMacFComponentName_Type()
)
gvcIfDMacFComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfDMacFComponentName.setStatus("mandatory")
_GvcIfDMacFStorageType_Type = StorageType
_GvcIfDMacFStorageType_Object = MibTableColumn
gvcIfDMacFStorageType = _GvcIfDMacFStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 10, 1, 1, 4),
    _GvcIfDMacFStorageType_Type()
)
gvcIfDMacFStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfDMacFStorageType.setStatus("mandatory")


class _GvcIfDMacFIndex_Type(DashedHexString):
    """Custom type gvcIfDMacFIndex based on DashedHexString"""
    subtypeSpec = DashedHexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_GvcIfDMacFIndex_Type.__name__ = "DashedHexString"
_GvcIfDMacFIndex_Object = MibTableColumn
gvcIfDMacFIndex = _GvcIfDMacFIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 10, 1, 1, 10),
    _GvcIfDMacFIndex_Type()
)
gvcIfDMacFIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gvcIfDMacFIndex.setStatus("mandatory")
_GvcIfDMacFOperTable_Object = MibTable
gvcIfDMacFOperTable = _GvcIfDMacFOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 10, 11)
)
if mibBuilder.loadTexts:
    gvcIfDMacFOperTable.setStatus("mandatory")
_GvcIfDMacFOperEntry_Object = MibTableRow
gvcIfDMacFOperEntry = _GvcIfDMacFOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 10, 11, 1)
)
gvcIfDMacFOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfIndex"),
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfDMacFIndex"),
)
if mibBuilder.loadTexts:
    gvcIfDMacFOperEntry.setStatus("mandatory")
_GvcIfDMacFFramesMatchingFilter_Type = Counter32
_GvcIfDMacFFramesMatchingFilter_Object = MibTableColumn
gvcIfDMacFFramesMatchingFilter = _GvcIfDMacFFramesMatchingFilter_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 10, 11, 1, 1),
    _GvcIfDMacFFramesMatchingFilter_Type()
)
gvcIfDMacFFramesMatchingFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfDMacFFramesMatchingFilter.setStatus("mandatory")
_GvcIfCidDataTable_Object = MibTable
gvcIfCidDataTable = _GvcIfCidDataTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 30)
)
if mibBuilder.loadTexts:
    gvcIfCidDataTable.setStatus("mandatory")
_GvcIfCidDataEntry_Object = MibTableRow
gvcIfCidDataEntry = _GvcIfCidDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 30, 1)
)
gvcIfCidDataEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfIndex"),
)
if mibBuilder.loadTexts:
    gvcIfCidDataEntry.setStatus("mandatory")


class _GvcIfCustomerIdentifier_Type(Unsigned32):
    """Custom type gvcIfCustomerIdentifier based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 8191),
    )


_GvcIfCustomerIdentifier_Type.__name__ = "Unsigned32"
_GvcIfCustomerIdentifier_Object = MibTableColumn
gvcIfCustomerIdentifier = _GvcIfCustomerIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 30, 1, 1),
    _GvcIfCustomerIdentifier_Type()
)
gvcIfCustomerIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gvcIfCustomerIdentifier.setStatus("mandatory")
_GvcIfProvTable_Object = MibTable
gvcIfProvTable = _GvcIfProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 31)
)
if mibBuilder.loadTexts:
    gvcIfProvTable.setStatus("mandatory")
_GvcIfProvEntry_Object = MibTableRow
gvcIfProvEntry = _GvcIfProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 31, 1)
)
gvcIfProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfIndex"),
)
if mibBuilder.loadTexts:
    gvcIfProvEntry.setStatus("mandatory")
_GvcIfLogicalProcessor_Type = Link
_GvcIfLogicalProcessor_Object = MibTableColumn
gvcIfLogicalProcessor = _GvcIfLogicalProcessor_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 31, 1, 1),
    _GvcIfLogicalProcessor_Type()
)
gvcIfLogicalProcessor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gvcIfLogicalProcessor.setStatus("mandatory")


class _GvcIfMaxActiveLinkStation_Type(Unsigned32):
    """Custom type gvcIfMaxActiveLinkStation based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5000),
    )


_GvcIfMaxActiveLinkStation_Type.__name__ = "Unsigned32"
_GvcIfMaxActiveLinkStation_Object = MibTableColumn
gvcIfMaxActiveLinkStation = _GvcIfMaxActiveLinkStation_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 31, 1, 3),
    _GvcIfMaxActiveLinkStation_Type()
)
gvcIfMaxActiveLinkStation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gvcIfMaxActiveLinkStation.setStatus("mandatory")
_GvcIfStateTable_Object = MibTable
gvcIfStateTable = _GvcIfStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 32)
)
if mibBuilder.loadTexts:
    gvcIfStateTable.setStatus("mandatory")
_GvcIfStateEntry_Object = MibTableRow
gvcIfStateEntry = _GvcIfStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 32, 1)
)
gvcIfStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfIndex"),
)
if mibBuilder.loadTexts:
    gvcIfStateEntry.setStatus("mandatory")


class _GvcIfAdminState_Type(Integer32):
    """Custom type gvcIfAdminState based on Integer32"""
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


_GvcIfAdminState_Type.__name__ = "Integer32"
_GvcIfAdminState_Object = MibTableColumn
gvcIfAdminState = _GvcIfAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 32, 1, 1),
    _GvcIfAdminState_Type()
)
gvcIfAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfAdminState.setStatus("mandatory")


class _GvcIfOperationalState_Type(Integer32):
    """Custom type gvcIfOperationalState based on Integer32"""
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


_GvcIfOperationalState_Type.__name__ = "Integer32"
_GvcIfOperationalState_Object = MibTableColumn
gvcIfOperationalState = _GvcIfOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 32, 1, 2),
    _GvcIfOperationalState_Type()
)
gvcIfOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfOperationalState.setStatus("mandatory")


class _GvcIfUsageState_Type(Integer32):
    """Custom type gvcIfUsageState based on Integer32"""
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


_GvcIfUsageState_Type.__name__ = "Integer32"
_GvcIfUsageState_Object = MibTableColumn
gvcIfUsageState = _GvcIfUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 32, 1, 3),
    _GvcIfUsageState_Type()
)
gvcIfUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfUsageState.setStatus("mandatory")
_GvcIfOpTable_Object = MibTable
gvcIfOpTable = _GvcIfOpTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 33)
)
if mibBuilder.loadTexts:
    gvcIfOpTable.setStatus("mandatory")
_GvcIfOpEntry_Object = MibTableRow
gvcIfOpEntry = _GvcIfOpEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 33, 1)
)
gvcIfOpEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfIndex"),
)
if mibBuilder.loadTexts:
    gvcIfOpEntry.setStatus("mandatory")


class _GvcIfActiveLinkStations_Type(Unsigned32):
    """Custom type gvcIfActiveLinkStations based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_GvcIfActiveLinkStations_Type.__name__ = "Unsigned32"
_GvcIfActiveLinkStations_Object = MibTableColumn
gvcIfActiveLinkStations = _GvcIfActiveLinkStations_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 33, 1, 2),
    _GvcIfActiveLinkStations_Type()
)
gvcIfActiveLinkStations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfActiveLinkStations.setStatus("mandatory")


class _GvcIfIssueLcnClearAlarm_Type(Integer32):
    """Custom type gvcIfIssueLcnClearAlarm based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("allowed", 1),
          ("disallowed", 0))
    )


_GvcIfIssueLcnClearAlarm_Type.__name__ = "Integer32"
_GvcIfIssueLcnClearAlarm_Object = MibTableColumn
gvcIfIssueLcnClearAlarm = _GvcIfIssueLcnClearAlarm_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 33, 1, 5),
    _GvcIfIssueLcnClearAlarm_Type()
)
gvcIfIssueLcnClearAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gvcIfIssueLcnClearAlarm.setStatus("mandatory")


class _GvcIfActiveQllcCalls_Type(Unsigned32):
    """Custom type gvcIfActiveQllcCalls based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_GvcIfActiveQllcCalls_Type.__name__ = "Unsigned32"
_GvcIfActiveQllcCalls_Object = MibTableColumn
gvcIfActiveQllcCalls = _GvcIfActiveQllcCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 33, 1, 6),
    _GvcIfActiveQllcCalls_Type()
)
gvcIfActiveQllcCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfActiveQllcCalls.setStatus("mandatory")
_GvcIfStatsTable_Object = MibTable
gvcIfStatsTable = _GvcIfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 34)
)
if mibBuilder.loadTexts:
    gvcIfStatsTable.setStatus("mandatory")
_GvcIfStatsEntry_Object = MibTableRow
gvcIfStatsEntry = _GvcIfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 34, 1)
)
gvcIfStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-GeneralVcInterfaceMIB", "gvcIfIndex"),
)
if mibBuilder.loadTexts:
    gvcIfStatsEntry.setStatus("mandatory")
_GvcIfCallsToNetwork_Type = Counter32
_GvcIfCallsToNetwork_Object = MibTableColumn
gvcIfCallsToNetwork = _GvcIfCallsToNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 34, 1, 1),
    _GvcIfCallsToNetwork_Type()
)
gvcIfCallsToNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfCallsToNetwork.setStatus("mandatory")
_GvcIfCallsFromNetwork_Type = Counter32
_GvcIfCallsFromNetwork_Object = MibTableColumn
gvcIfCallsFromNetwork = _GvcIfCallsFromNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 34, 1, 2),
    _GvcIfCallsFromNetwork_Type()
)
gvcIfCallsFromNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfCallsFromNetwork.setStatus("mandatory")
_GvcIfCallsRefusedByNetwork_Type = Counter32
_GvcIfCallsRefusedByNetwork_Object = MibTableColumn
gvcIfCallsRefusedByNetwork = _GvcIfCallsRefusedByNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 34, 1, 3),
    _GvcIfCallsRefusedByNetwork_Type()
)
gvcIfCallsRefusedByNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfCallsRefusedByNetwork.setStatus("mandatory")
_GvcIfCallsRefusedByInterface_Type = Counter32
_GvcIfCallsRefusedByInterface_Object = MibTableColumn
gvcIfCallsRefusedByInterface = _GvcIfCallsRefusedByInterface_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 34, 1, 4),
    _GvcIfCallsRefusedByInterface_Type()
)
gvcIfCallsRefusedByInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfCallsRefusedByInterface.setStatus("mandatory")


class _GvcIfPeakActiveLinkStations_Type(Unsigned32):
    """Custom type gvcIfPeakActiveLinkStations based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_GvcIfPeakActiveLinkStations_Type.__name__ = "Unsigned32"
_GvcIfPeakActiveLinkStations_Object = MibTableColumn
gvcIfPeakActiveLinkStations = _GvcIfPeakActiveLinkStations_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 34, 1, 6),
    _GvcIfPeakActiveLinkStations_Type()
)
gvcIfPeakActiveLinkStations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfPeakActiveLinkStations.setStatus("mandatory")
_GvcIfBcastFramesDiscarded_Type = Counter32
_GvcIfBcastFramesDiscarded_Object = MibTableColumn
gvcIfBcastFramesDiscarded = _GvcIfBcastFramesDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 34, 1, 7),
    _GvcIfBcastFramesDiscarded_Type()
)
gvcIfBcastFramesDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfBcastFramesDiscarded.setStatus("mandatory")
_GvcIfDiscardedQllcCalls_Type = Counter32
_GvcIfDiscardedQllcCalls_Object = MibTableColumn
gvcIfDiscardedQllcCalls = _GvcIfDiscardedQllcCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 107, 34, 1, 8),
    _GvcIfDiscardedQllcCalls_Type()
)
gvcIfDiscardedQllcCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvcIfDiscardedQllcCalls.setStatus("mandatory")
_GeneralVcInterfaceMIB_ObjectIdentity = ObjectIdentity
generalVcInterfaceMIB = _GeneralVcInterfaceMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 58)
)
_GeneralVcInterfaceGroup_ObjectIdentity = ObjectIdentity
generalVcInterfaceGroup = _GeneralVcInterfaceGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 58, 1)
)
_GeneralVcInterfaceGroupBE_ObjectIdentity = ObjectIdentity
generalVcInterfaceGroupBE = _GeneralVcInterfaceGroupBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 58, 1, 5)
)
_GeneralVcInterfaceGroupBE01_ObjectIdentity = ObjectIdentity
generalVcInterfaceGroupBE01 = _GeneralVcInterfaceGroupBE01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 58, 1, 5, 2)
)
_GeneralVcInterfaceGroupBE01A_ObjectIdentity = ObjectIdentity
generalVcInterfaceGroupBE01A = _GeneralVcInterfaceGroupBE01A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 58, 1, 5, 2, 2)
)
_GeneralVcInterfaceCapabilities_ObjectIdentity = ObjectIdentity
generalVcInterfaceCapabilities = _GeneralVcInterfaceCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 58, 3)
)
_GeneralVcInterfaceCapabilitiesBE_ObjectIdentity = ObjectIdentity
generalVcInterfaceCapabilitiesBE = _GeneralVcInterfaceCapabilitiesBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 58, 3, 5)
)
_GeneralVcInterfaceCapabilitiesBE01_ObjectIdentity = ObjectIdentity
generalVcInterfaceCapabilitiesBE01 = _GeneralVcInterfaceCapabilitiesBE01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 58, 3, 5, 2)
)
_GeneralVcInterfaceCapabilitiesBE01A_ObjectIdentity = ObjectIdentity
generalVcInterfaceCapabilitiesBE01A = _GeneralVcInterfaceCapabilitiesBE01A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 58, 3, 5, 2, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-Magellan-Passport-GeneralVcInterfaceMIB",
    **{"gvcIf": gvcIf,
       "gvcIfRowStatusTable": gvcIfRowStatusTable,
       "gvcIfRowStatusEntry": gvcIfRowStatusEntry,
       "gvcIfRowStatus": gvcIfRowStatus,
       "gvcIfComponentName": gvcIfComponentName,
       "gvcIfStorageType": gvcIfStorageType,
       "gvcIfIndex": gvcIfIndex,
       "gvcIfDc": gvcIfDc,
       "gvcIfDcRowStatusTable": gvcIfDcRowStatusTable,
       "gvcIfDcRowStatusEntry": gvcIfDcRowStatusEntry,
       "gvcIfDcRowStatus": gvcIfDcRowStatus,
       "gvcIfDcComponentName": gvcIfDcComponentName,
       "gvcIfDcStorageType": gvcIfDcStorageType,
       "gvcIfDcMacIndex": gvcIfDcMacIndex,
       "gvcIfDcSapIndex": gvcIfDcSapIndex,
       "gvcIfDcOptionsTable": gvcIfDcOptionsTable,
       "gvcIfDcOptionsEntry": gvcIfDcOptionsEntry,
       "gvcIfDcRemoteNpi": gvcIfDcRemoteNpi,
       "gvcIfDcRemoteDna": gvcIfDcRemoteDna,
       "gvcIfDcUserData": gvcIfDcUserData,
       "gvcIfDcTransferPriority": gvcIfDcTransferPriority,
       "gvcIfDcDiscardPriority": gvcIfDcDiscardPriority,
       "gvcIfDcCfaTable": gvcIfDcCfaTable,
       "gvcIfDcCfaEntry": gvcIfDcCfaEntry,
       "gvcIfDcCfaIndex": gvcIfDcCfaIndex,
       "gvcIfDcCfaValue": gvcIfDcCfaValue,
       "gvcIfDcCfaRowStatus": gvcIfDcCfaRowStatus,
       "gvcIfRDnaMap": gvcIfRDnaMap,
       "gvcIfRDnaMapRowStatusTable": gvcIfRDnaMapRowStatusTable,
       "gvcIfRDnaMapRowStatusEntry": gvcIfRDnaMapRowStatusEntry,
       "gvcIfRDnaMapRowStatus": gvcIfRDnaMapRowStatus,
       "gvcIfRDnaMapComponentName": gvcIfRDnaMapComponentName,
       "gvcIfRDnaMapStorageType": gvcIfRDnaMapStorageType,
       "gvcIfRDnaMapNpiIndex": gvcIfRDnaMapNpiIndex,
       "gvcIfRDnaMapDnaIndex": gvcIfRDnaMapDnaIndex,
       "gvcIfRDnaMapLanAdTable": gvcIfRDnaMapLanAdTable,
       "gvcIfRDnaMapLanAdEntry": gvcIfRDnaMapLanAdEntry,
       "gvcIfRDnaMapMac": gvcIfRDnaMapMac,
       "gvcIfRDnaMapSap": gvcIfRDnaMapSap,
       "gvcIfLcn": gvcIfLcn,
       "gvcIfLcnRowStatusTable": gvcIfLcnRowStatusTable,
       "gvcIfLcnRowStatusEntry": gvcIfLcnRowStatusEntry,
       "gvcIfLcnRowStatus": gvcIfLcnRowStatus,
       "gvcIfLcnComponentName": gvcIfLcnComponentName,
       "gvcIfLcnStorageType": gvcIfLcnStorageType,
       "gvcIfLcnIndex": gvcIfLcnIndex,
       "gvcIfLcnVc": gvcIfLcnVc,
       "gvcIfLcnVcRowStatusTable": gvcIfLcnVcRowStatusTable,
       "gvcIfLcnVcRowStatusEntry": gvcIfLcnVcRowStatusEntry,
       "gvcIfLcnVcRowStatus": gvcIfLcnVcRowStatus,
       "gvcIfLcnVcComponentName": gvcIfLcnVcComponentName,
       "gvcIfLcnVcStorageType": gvcIfLcnVcStorageType,
       "gvcIfLcnVcIndex": gvcIfLcnVcIndex,
       "gvcIfLcnVcCadTable": gvcIfLcnVcCadTable,
       "gvcIfLcnVcCadEntry": gvcIfLcnVcCadEntry,
       "gvcIfLcnVcType": gvcIfLcnVcType,
       "gvcIfLcnVcState": gvcIfLcnVcState,
       "gvcIfLcnVcPreviousState": gvcIfLcnVcPreviousState,
       "gvcIfLcnVcDiagnosticCode": gvcIfLcnVcDiagnosticCode,
       "gvcIfLcnVcPreviousDiagnosticCode": gvcIfLcnVcPreviousDiagnosticCode,
       "gvcIfLcnVcCalledNpi": gvcIfLcnVcCalledNpi,
       "gvcIfLcnVcCalledDna": gvcIfLcnVcCalledDna,
       "gvcIfLcnVcCalledLcn": gvcIfLcnVcCalledLcn,
       "gvcIfLcnVcCallingNpi": gvcIfLcnVcCallingNpi,
       "gvcIfLcnVcCallingDna": gvcIfLcnVcCallingDna,
       "gvcIfLcnVcCallingLcn": gvcIfLcnVcCallingLcn,
       "gvcIfLcnVcAccountingEnabled": gvcIfLcnVcAccountingEnabled,
       "gvcIfLcnVcFastSelectCall": gvcIfLcnVcFastSelectCall,
       "gvcIfLcnVcLocalRxPktSize": gvcIfLcnVcLocalRxPktSize,
       "gvcIfLcnVcLocalTxPktSize": gvcIfLcnVcLocalTxPktSize,
       "gvcIfLcnVcLocalTxWindowSize": gvcIfLcnVcLocalTxWindowSize,
       "gvcIfLcnVcLocalRxWindowSize": gvcIfLcnVcLocalRxWindowSize,
       "gvcIfLcnVcPathReliability": gvcIfLcnVcPathReliability,
       "gvcIfLcnVcAccountingEnd": gvcIfLcnVcAccountingEnd,
       "gvcIfLcnVcPriority": gvcIfLcnVcPriority,
       "gvcIfLcnVcSegmentSize": gvcIfLcnVcSegmentSize,
       "gvcIfLcnVcSubnetTxPktSize": gvcIfLcnVcSubnetTxPktSize,
       "gvcIfLcnVcSubnetTxWindowSize": gvcIfLcnVcSubnetTxWindowSize,
       "gvcIfLcnVcSubnetRxPktSize": gvcIfLcnVcSubnetRxPktSize,
       "gvcIfLcnVcSubnetRxWindowSize": gvcIfLcnVcSubnetRxWindowSize,
       "gvcIfLcnVcMaxSubnetPktSize": gvcIfLcnVcMaxSubnetPktSize,
       "gvcIfLcnVcTransferPriorityToNetwork": gvcIfLcnVcTransferPriorityToNetwork,
       "gvcIfLcnVcTransferPriorityFromNetwork": gvcIfLcnVcTransferPriorityFromNetwork,
       "gvcIfLcnVcIntdTable": gvcIfLcnVcIntdTable,
       "gvcIfLcnVcIntdEntry": gvcIfLcnVcIntdEntry,
       "gvcIfLcnVcCallReferenceNumber": gvcIfLcnVcCallReferenceNumber,
       "gvcIfLcnVcElapsedTimeTillNow": gvcIfLcnVcElapsedTimeTillNow,
       "gvcIfLcnVcSegmentsRx": gvcIfLcnVcSegmentsRx,
       "gvcIfLcnVcSegmentsSent": gvcIfLcnVcSegmentsSent,
       "gvcIfLcnVcStartTime": gvcIfLcnVcStartTime,
       "gvcIfLcnVcStatsTable": gvcIfLcnVcStatsTable,
       "gvcIfLcnVcStatsEntry": gvcIfLcnVcStatsEntry,
       "gvcIfLcnVcAckStackingTimeouts": gvcIfLcnVcAckStackingTimeouts,
       "gvcIfLcnVcOutOfRangeFrmFromSubnet": gvcIfLcnVcOutOfRangeFrmFromSubnet,
       "gvcIfLcnVcDuplicatesFromSubnet": gvcIfLcnVcDuplicatesFromSubnet,
       "gvcIfLcnVcFrmRetryTimeouts": gvcIfLcnVcFrmRetryTimeouts,
       "gvcIfLcnVcPeakRetryQueueSize": gvcIfLcnVcPeakRetryQueueSize,
       "gvcIfLcnVcPeakOoSeqQueueSize": gvcIfLcnVcPeakOoSeqQueueSize,
       "gvcIfLcnVcPeakOoSeqFrmForwarded": gvcIfLcnVcPeakOoSeqFrmForwarded,
       "gvcIfLcnVcPeakStackedAcksRx": gvcIfLcnVcPeakStackedAcksRx,
       "gvcIfLcnVcSubnetRecoveries": gvcIfLcnVcSubnetRecoveries,
       "gvcIfLcnVcWindowClosuresToSubnet": gvcIfLcnVcWindowClosuresToSubnet,
       "gvcIfLcnVcWindowClosuresFromSubnet": gvcIfLcnVcWindowClosuresFromSubnet,
       "gvcIfLcnVcWrTriggers": gvcIfLcnVcWrTriggers,
       "gvcIfLcnStateTable": gvcIfLcnStateTable,
       "gvcIfLcnStateEntry": gvcIfLcnStateEntry,
       "gvcIfLcnAdminState": gvcIfLcnAdminState,
       "gvcIfLcnOperationalState": gvcIfLcnOperationalState,
       "gvcIfLcnUsageState": gvcIfLcnUsageState,
       "gvcIfLcnLcnCIdTable": gvcIfLcnLcnCIdTable,
       "gvcIfLcnLcnCIdEntry": gvcIfLcnLcnCIdEntry,
       "gvcIfLcnCircuitId": gvcIfLcnCircuitId,
       "gvcIfLcnOperTable": gvcIfLcnOperTable,
       "gvcIfLcnOperEntry": gvcIfLcnOperEntry,
       "gvcIfLcnState": gvcIfLcnState,
       "gvcIfLcnDnaMap": gvcIfLcnDnaMap,
       "gvcIfLcnSourceMac": gvcIfLcnSourceMac,
       "gvcIfDna": gvcIfDna,
       "gvcIfDnaRowStatusTable": gvcIfDnaRowStatusTable,
       "gvcIfDnaRowStatusEntry": gvcIfDnaRowStatusEntry,
       "gvcIfDnaRowStatus": gvcIfDnaRowStatus,
       "gvcIfDnaComponentName": gvcIfDnaComponentName,
       "gvcIfDnaStorageType": gvcIfDnaStorageType,
       "gvcIfDnaIndex": gvcIfDnaIndex,
       "gvcIfDnaCug": gvcIfDnaCug,
       "gvcIfDnaCugRowStatusTable": gvcIfDnaCugRowStatusTable,
       "gvcIfDnaCugRowStatusEntry": gvcIfDnaCugRowStatusEntry,
       "gvcIfDnaCugRowStatus": gvcIfDnaCugRowStatus,
       "gvcIfDnaCugComponentName": gvcIfDnaCugComponentName,
       "gvcIfDnaCugStorageType": gvcIfDnaCugStorageType,
       "gvcIfDnaCugIndex": gvcIfDnaCugIndex,
       "gvcIfDnaCugCugOptionsTable": gvcIfDnaCugCugOptionsTable,
       "gvcIfDnaCugCugOptionsEntry": gvcIfDnaCugCugOptionsEntry,
       "gvcIfDnaCugType": gvcIfDnaCugType,
       "gvcIfDnaCugDnic": gvcIfDnaCugDnic,
       "gvcIfDnaCugInterlockCode": gvcIfDnaCugInterlockCode,
       "gvcIfDnaCugPreferential": gvcIfDnaCugPreferential,
       "gvcIfDnaCugOutCalls": gvcIfDnaCugOutCalls,
       "gvcIfDnaCugIncCalls": gvcIfDnaCugIncCalls,
       "gvcIfDnaCugPrivileged": gvcIfDnaCugPrivileged,
       "gvcIfDnaHgM": gvcIfDnaHgM,
       "gvcIfDnaHgMRowStatusTable": gvcIfDnaHgMRowStatusTable,
       "gvcIfDnaHgMRowStatusEntry": gvcIfDnaHgMRowStatusEntry,
       "gvcIfDnaHgMRowStatus": gvcIfDnaHgMRowStatus,
       "gvcIfDnaHgMComponentName": gvcIfDnaHgMComponentName,
       "gvcIfDnaHgMStorageType": gvcIfDnaHgMStorageType,
       "gvcIfDnaHgMIndex": gvcIfDnaHgMIndex,
       "gvcIfDnaHgMHgAddr": gvcIfDnaHgMHgAddr,
       "gvcIfDnaHgMHgAddrRowStatusTable": gvcIfDnaHgMHgAddrRowStatusTable,
       "gvcIfDnaHgMHgAddrRowStatusEntry": gvcIfDnaHgMHgAddrRowStatusEntry,
       "gvcIfDnaHgMHgAddrRowStatus": gvcIfDnaHgMHgAddrRowStatus,
       "gvcIfDnaHgMHgAddrComponentName": gvcIfDnaHgMHgAddrComponentName,
       "gvcIfDnaHgMHgAddrStorageType": gvcIfDnaHgMHgAddrStorageType,
       "gvcIfDnaHgMHgAddrIndex": gvcIfDnaHgMHgAddrIndex,
       "gvcIfDnaHgMHgAddrAddrTable": gvcIfDnaHgMHgAddrAddrTable,
       "gvcIfDnaHgMHgAddrAddrEntry": gvcIfDnaHgMHgAddrAddrEntry,
       "gvcIfDnaHgMHgAddrNumberingPlanIndicator": gvcIfDnaHgMHgAddrNumberingPlanIndicator,
       "gvcIfDnaHgMHgAddrDataNetworkAddress": gvcIfDnaHgMHgAddrDataNetworkAddress,
       "gvcIfDnaHgMIfTable": gvcIfDnaHgMIfTable,
       "gvcIfDnaHgMIfEntry": gvcIfDnaHgMIfEntry,
       "gvcIfDnaHgMAvailabilityUpdateThreshold": gvcIfDnaHgMAvailabilityUpdateThreshold,
       "gvcIfDnaHgMOpTable": gvcIfDnaHgMOpTable,
       "gvcIfDnaHgMOpEntry": gvcIfDnaHgMOpEntry,
       "gvcIfDnaHgMAvailabilityDelta": gvcIfDnaHgMAvailabilityDelta,
       "gvcIfDnaHgMMaxAvailableLinkStations": gvcIfDnaHgMMaxAvailableLinkStations,
       "gvcIfDnaHgMAvailableLinkStations": gvcIfDnaHgMAvailableLinkStations,
       "gvcIfDnaDdm": gvcIfDnaDdm,
       "gvcIfDnaDdmRowStatusTable": gvcIfDnaDdmRowStatusTable,
       "gvcIfDnaDdmRowStatusEntry": gvcIfDnaDdmRowStatusEntry,
       "gvcIfDnaDdmRowStatus": gvcIfDnaDdmRowStatus,
       "gvcIfDnaDdmComponentName": gvcIfDnaDdmComponentName,
       "gvcIfDnaDdmStorageType": gvcIfDnaDdmStorageType,
       "gvcIfDnaDdmIndex": gvcIfDnaDdmIndex,
       "gvcIfDnaDdmLanAdTable": gvcIfDnaDdmLanAdTable,
       "gvcIfDnaDdmLanAdEntry": gvcIfDnaDdmLanAdEntry,
       "gvcIfDnaDdmMac": gvcIfDnaDdmMac,
       "gvcIfDnaDdmSap": gvcIfDnaDdmSap,
       "gvcIfDnaDdmDmoTable": gvcIfDnaDdmDmoTable,
       "gvcIfDnaDdmDmoEntry": gvcIfDnaDdmDmoEntry,
       "gvcIfDnaDdmDeviceMonitoring": gvcIfDnaDdmDeviceMonitoring,
       "gvcIfDnaDdmClearVcsWhenUnreachable": gvcIfDnaDdmClearVcsWhenUnreachable,
       "gvcIfDnaDdmDeviceMonitoringTimer": gvcIfDnaDdmDeviceMonitoringTimer,
       "gvcIfDnaDdmTestResponseTimer": gvcIfDnaDdmTestResponseTimer,
       "gvcIfDnaDdmMaximumTestRetry": gvcIfDnaDdmMaximumTestRetry,
       "gvcIfDnaDdmDevOpTable": gvcIfDnaDdmDevOpTable,
       "gvcIfDnaDdmDevOpEntry": gvcIfDnaDdmDevOpEntry,
       "gvcIfDnaDdmDeviceStatus": gvcIfDnaDdmDeviceStatus,
       "gvcIfDnaDdmActiveLinkStations": gvcIfDnaDdmActiveLinkStations,
       "gvcIfDnaDdmLastTimeUnreachable": gvcIfDnaDdmLastTimeUnreachable,
       "gvcIfDnaDdmLastTimeReachable": gvcIfDnaDdmLastTimeReachable,
       "gvcIfDnaDdmDeviceUnreachable": gvcIfDnaDdmDeviceUnreachable,
       "gvcIfDnaDdmMonitoringLcn": gvcIfDnaDdmMonitoringLcn,
       "gvcIfDnaSdm": gvcIfDnaSdm,
       "gvcIfDnaSdmRowStatusTable": gvcIfDnaSdmRowStatusTable,
       "gvcIfDnaSdmRowStatusEntry": gvcIfDnaSdmRowStatusEntry,
       "gvcIfDnaSdmRowStatus": gvcIfDnaSdmRowStatus,
       "gvcIfDnaSdmComponentName": gvcIfDnaSdmComponentName,
       "gvcIfDnaSdmStorageType": gvcIfDnaSdmStorageType,
       "gvcIfDnaSdmIndex": gvcIfDnaSdmIndex,
       "gvcIfDnaSdmLanAdTable": gvcIfDnaSdmLanAdTable,
       "gvcIfDnaSdmLanAdEntry": gvcIfDnaSdmLanAdEntry,
       "gvcIfDnaSdmMac": gvcIfDnaSdmMac,
       "gvcIfDnaSdmSap": gvcIfDnaSdmSap,
       "gvcIfDnaSdmDmoTable": gvcIfDnaSdmDmoTable,
       "gvcIfDnaSdmDmoEntry": gvcIfDnaSdmDmoEntry,
       "gvcIfDnaSdmDeviceMonitoring": gvcIfDnaSdmDeviceMonitoring,
       "gvcIfDnaSdmClearVcsWhenUnreachable": gvcIfDnaSdmClearVcsWhenUnreachable,
       "gvcIfDnaSdmDeviceMonitoringTimer": gvcIfDnaSdmDeviceMonitoringTimer,
       "gvcIfDnaSdmTestResponseTimer": gvcIfDnaSdmTestResponseTimer,
       "gvcIfDnaSdmMaximumTestRetry": gvcIfDnaSdmMaximumTestRetry,
       "gvcIfDnaSdmDevOpTable": gvcIfDnaSdmDevOpTable,
       "gvcIfDnaSdmDevOpEntry": gvcIfDnaSdmDevOpEntry,
       "gvcIfDnaSdmDeviceStatus": gvcIfDnaSdmDeviceStatus,
       "gvcIfDnaSdmActiveLinkStations": gvcIfDnaSdmActiveLinkStations,
       "gvcIfDnaSdmLastTimeUnreachable": gvcIfDnaSdmLastTimeUnreachable,
       "gvcIfDnaSdmLastTimeReachable": gvcIfDnaSdmLastTimeReachable,
       "gvcIfDnaSdmDeviceUnreachable": gvcIfDnaSdmDeviceUnreachable,
       "gvcIfDnaSdmMonitoringLcn": gvcIfDnaSdmMonitoringLcn,
       "gvcIfDnaAddrTable": gvcIfDnaAddrTable,
       "gvcIfDnaAddrEntry": gvcIfDnaAddrEntry,
       "gvcIfDnaNumberingPlanIndicator": gvcIfDnaNumberingPlanIndicator,
       "gvcIfDnaDataNetworkAddress": gvcIfDnaDataNetworkAddress,
       "gvcIfDnaOutgoingOptionsTable": gvcIfDnaOutgoingOptionsTable,
       "gvcIfDnaOutgoingOptionsEntry": gvcIfDnaOutgoingOptionsEntry,
       "gvcIfDnaOutDefaultPriority": gvcIfDnaOutDefaultPriority,
       "gvcIfDnaOutDefaultPathSensitivity": gvcIfDnaOutDefaultPathSensitivity,
       "gvcIfDnaOutDefaultPathReliability": gvcIfDnaOutDefaultPathReliability,
       "gvcIfDnaOutAccess": gvcIfDnaOutAccess,
       "gvcIfDnaDefaultTransferPriority": gvcIfDnaDefaultTransferPriority,
       "gvcIfDnaTransferPriorityOverRide": gvcIfDnaTransferPriorityOverRide,
       "gvcIfDnaIncomingOptionsTable": gvcIfDnaIncomingOptionsTable,
       "gvcIfDnaIncomingOptionsEntry": gvcIfDnaIncomingOptionsEntry,
       "gvcIfDnaIncCalls": gvcIfDnaIncCalls,
       "gvcIfDnaIncHighPriorityReverseCharge": gvcIfDnaIncHighPriorityReverseCharge,
       "gvcIfDnaIncNormalPriorityReverseCharge": gvcIfDnaIncNormalPriorityReverseCharge,
       "gvcIfDnaIncIntlNormalCharge": gvcIfDnaIncIntlNormalCharge,
       "gvcIfDnaIncIntlReverseCharge": gvcIfDnaIncIntlReverseCharge,
       "gvcIfDnaIncSameService": gvcIfDnaIncSameService,
       "gvcIfDnaIncAccess": gvcIfDnaIncAccess,
       "gvcIfDnaCallOptionsTable": gvcIfDnaCallOptionsTable,
       "gvcIfDnaCallOptionsEntry": gvcIfDnaCallOptionsEntry,
       "gvcIfDnaServiceCategory": gvcIfDnaServiceCategory,
       "gvcIfDnaPacketSizes": gvcIfDnaPacketSizes,
       "gvcIfDnaDefaultRecvFrmNetworkPacketSize": gvcIfDnaDefaultRecvFrmNetworkPacketSize,
       "gvcIfDnaDefaultSendToNetworkPacketSize": gvcIfDnaDefaultSendToNetworkPacketSize,
       "gvcIfDnaDefaultRecvFrmNetworkThruputClass": gvcIfDnaDefaultRecvFrmNetworkThruputClass,
       "gvcIfDnaDefaultSendToNetworkThruputClass": gvcIfDnaDefaultSendToNetworkThruputClass,
       "gvcIfDnaDefaultRecvFrmNetworkWindowSize": gvcIfDnaDefaultRecvFrmNetworkWindowSize,
       "gvcIfDnaDefaultSendToNetworkWindowSize": gvcIfDnaDefaultSendToNetworkWindowSize,
       "gvcIfDnaPacketSizeNegotiation": gvcIfDnaPacketSizeNegotiation,
       "gvcIfDnaCugFormat": gvcIfDnaCugFormat,
       "gvcIfDnaAccountClass": gvcIfDnaAccountClass,
       "gvcIfDnaAccountCollection": gvcIfDnaAccountCollection,
       "gvcIfDnaServiceExchange": gvcIfDnaServiceExchange,
       "gvcIfRg": gvcIfRg,
       "gvcIfRgRowStatusTable": gvcIfRgRowStatusTable,
       "gvcIfRgRowStatusEntry": gvcIfRgRowStatusEntry,
       "gvcIfRgRowStatus": gvcIfRgRowStatus,
       "gvcIfRgComponentName": gvcIfRgComponentName,
       "gvcIfRgStorageType": gvcIfRgStorageType,
       "gvcIfRgIndex": gvcIfRgIndex,
       "gvcIfRgIfEntryTable": gvcIfRgIfEntryTable,
       "gvcIfRgIfEntryEntry": gvcIfRgIfEntryEntry,
       "gvcIfRgIfAdminStatus": gvcIfRgIfAdminStatus,
       "gvcIfRgIfIndex": gvcIfRgIfIndex,
       "gvcIfRgProvTable": gvcIfRgProvTable,
       "gvcIfRgProvEntry": gvcIfRgProvEntry,
       "gvcIfRgLinkToProtocolPort": gvcIfRgLinkToProtocolPort,
       "gvcIfRgOperStatusTable": gvcIfRgOperStatusTable,
       "gvcIfRgOperStatusEntry": gvcIfRgOperStatusEntry,
       "gvcIfRgSnmpOperStatus": gvcIfRgSnmpOperStatus,
       "gvcIfDlci": gvcIfDlci,
       "gvcIfDlciRowStatusTable": gvcIfDlciRowStatusTable,
       "gvcIfDlciRowStatusEntry": gvcIfDlciRowStatusEntry,
       "gvcIfDlciRowStatus": gvcIfDlciRowStatus,
       "gvcIfDlciComponentName": gvcIfDlciComponentName,
       "gvcIfDlciStorageType": gvcIfDlciStorageType,
       "gvcIfDlciIndex": gvcIfDlciIndex,
       "gvcIfDlciDc": gvcIfDlciDc,
       "gvcIfDlciDcRowStatusTable": gvcIfDlciDcRowStatusTable,
       "gvcIfDlciDcRowStatusEntry": gvcIfDlciDcRowStatusEntry,
       "gvcIfDlciDcRowStatus": gvcIfDlciDcRowStatus,
       "gvcIfDlciDcComponentName": gvcIfDlciDcComponentName,
       "gvcIfDlciDcStorageType": gvcIfDlciDcStorageType,
       "gvcIfDlciDcIndex": gvcIfDlciDcIndex,
       "gvcIfDlciDcOptionsTable": gvcIfDlciDcOptionsTable,
       "gvcIfDlciDcOptionsEntry": gvcIfDlciDcOptionsEntry,
       "gvcIfDlciDcRemoteNpi": gvcIfDlciDcRemoteNpi,
       "gvcIfDlciDcRemoteDna": gvcIfDlciDcRemoteDna,
       "gvcIfDlciDcRemoteDlci": gvcIfDlciDcRemoteDlci,
       "gvcIfDlciDcType": gvcIfDlciDcType,
       "gvcIfDlciDcTransferPriority": gvcIfDlciDcTransferPriority,
       "gvcIfDlciDcDiscardPriority": gvcIfDlciDcDiscardPriority,
       "gvcIfDlciDcNfaTable": gvcIfDlciDcNfaTable,
       "gvcIfDlciDcNfaEntry": gvcIfDlciDcNfaEntry,
       "gvcIfDlciDcNfaIndex": gvcIfDlciDcNfaIndex,
       "gvcIfDlciDcNfaValue": gvcIfDlciDcNfaValue,
       "gvcIfDlciDcNfaRowStatus": gvcIfDlciDcNfaRowStatus,
       "gvcIfDlciVc": gvcIfDlciVc,
       "gvcIfDlciVcRowStatusTable": gvcIfDlciVcRowStatusTable,
       "gvcIfDlciVcRowStatusEntry": gvcIfDlciVcRowStatusEntry,
       "gvcIfDlciVcRowStatus": gvcIfDlciVcRowStatus,
       "gvcIfDlciVcComponentName": gvcIfDlciVcComponentName,
       "gvcIfDlciVcStorageType": gvcIfDlciVcStorageType,
       "gvcIfDlciVcIndex": gvcIfDlciVcIndex,
       "gvcIfDlciVcCadTable": gvcIfDlciVcCadTable,
       "gvcIfDlciVcCadEntry": gvcIfDlciVcCadEntry,
       "gvcIfDlciVcType": gvcIfDlciVcType,
       "gvcIfDlciVcState": gvcIfDlciVcState,
       "gvcIfDlciVcPreviousState": gvcIfDlciVcPreviousState,
       "gvcIfDlciVcDiagnosticCode": gvcIfDlciVcDiagnosticCode,
       "gvcIfDlciVcPreviousDiagnosticCode": gvcIfDlciVcPreviousDiagnosticCode,
       "gvcIfDlciVcCalledNpi": gvcIfDlciVcCalledNpi,
       "gvcIfDlciVcCalledDna": gvcIfDlciVcCalledDna,
       "gvcIfDlciVcCalledLcn": gvcIfDlciVcCalledLcn,
       "gvcIfDlciVcCallingNpi": gvcIfDlciVcCallingNpi,
       "gvcIfDlciVcCallingDna": gvcIfDlciVcCallingDna,
       "gvcIfDlciVcCallingLcn": gvcIfDlciVcCallingLcn,
       "gvcIfDlciVcAccountingEnabled": gvcIfDlciVcAccountingEnabled,
       "gvcIfDlciVcFastSelectCall": gvcIfDlciVcFastSelectCall,
       "gvcIfDlciVcPathReliability": gvcIfDlciVcPathReliability,
       "gvcIfDlciVcAccountingEnd": gvcIfDlciVcAccountingEnd,
       "gvcIfDlciVcPriority": gvcIfDlciVcPriority,
       "gvcIfDlciVcSegmentSize": gvcIfDlciVcSegmentSize,
       "gvcIfDlciVcMaxSubnetPktSize": gvcIfDlciVcMaxSubnetPktSize,
       "gvcIfDlciVcRcosToNetwork": gvcIfDlciVcRcosToNetwork,
       "gvcIfDlciVcRcosFromNetwork": gvcIfDlciVcRcosFromNetwork,
       "gvcIfDlciVcEmissionPriorityToNetwork": gvcIfDlciVcEmissionPriorityToNetwork,
       "gvcIfDlciVcEmissionPriorityFromNetwork": gvcIfDlciVcEmissionPriorityFromNetwork,
       "gvcIfDlciVcDataPath": gvcIfDlciVcDataPath,
       "gvcIfDlciVcIntdTable": gvcIfDlciVcIntdTable,
       "gvcIfDlciVcIntdEntry": gvcIfDlciVcIntdEntry,
       "gvcIfDlciVcCallReferenceNumber": gvcIfDlciVcCallReferenceNumber,
       "gvcIfDlciVcElapsedTimeTillNow": gvcIfDlciVcElapsedTimeTillNow,
       "gvcIfDlciVcSegmentsRx": gvcIfDlciVcSegmentsRx,
       "gvcIfDlciVcSegmentsSent": gvcIfDlciVcSegmentsSent,
       "gvcIfDlciVcStartTime": gvcIfDlciVcStartTime,
       "gvcIfDlciVcFrdTable": gvcIfDlciVcFrdTable,
       "gvcIfDlciVcFrdEntry": gvcIfDlciVcFrdEntry,
       "gvcIfDlciVcFrmCongestedToSubnet": gvcIfDlciVcFrmCongestedToSubnet,
       "gvcIfDlciVcCannotForwardToSubnet": gvcIfDlciVcCannotForwardToSubnet,
       "gvcIfDlciVcNotDataXferToSubnet": gvcIfDlciVcNotDataXferToSubnet,
       "gvcIfDlciVcOutOfRangeFrmFromSubnet": gvcIfDlciVcOutOfRangeFrmFromSubnet,
       "gvcIfDlciVcCombErrorsFromSubnet": gvcIfDlciVcCombErrorsFromSubnet,
       "gvcIfDlciVcDuplicatesFromSubnet": gvcIfDlciVcDuplicatesFromSubnet,
       "gvcIfDlciVcNotDataXferFromSubnet": gvcIfDlciVcNotDataXferFromSubnet,
       "gvcIfDlciVcFrmLossTimeouts": gvcIfDlciVcFrmLossTimeouts,
       "gvcIfDlciVcOoSeqByteCntExceeded": gvcIfDlciVcOoSeqByteCntExceeded,
       "gvcIfDlciVcPeakOoSeqPktCount": gvcIfDlciVcPeakOoSeqPktCount,
       "gvcIfDlciVcPeakOoSeqFrmForwarded": gvcIfDlciVcPeakOoSeqFrmForwarded,
       "gvcIfDlciVcSendSequenceNumber": gvcIfDlciVcSendSequenceNumber,
       "gvcIfDlciVcPktRetryTimeouts": gvcIfDlciVcPktRetryTimeouts,
       "gvcIfDlciVcPeakRetryQueueSize": gvcIfDlciVcPeakRetryQueueSize,
       "gvcIfDlciVcSubnetRecoveries": gvcIfDlciVcSubnetRecoveries,
       "gvcIfDlciVcOoSeqPktCntExceeded": gvcIfDlciVcOoSeqPktCntExceeded,
       "gvcIfDlciVcPeakOoSeqByteCount": gvcIfDlciVcPeakOoSeqByteCount,
       "gvcIfDlciVcDmepTable": gvcIfDlciVcDmepTable,
       "gvcIfDlciVcDmepEntry": gvcIfDlciVcDmepEntry,
       "gvcIfDlciVcDmepValue": gvcIfDlciVcDmepValue,
       "gvcIfDlciSp": gvcIfDlciSp,
       "gvcIfDlciSpRowStatusTable": gvcIfDlciSpRowStatusTable,
       "gvcIfDlciSpRowStatusEntry": gvcIfDlciSpRowStatusEntry,
       "gvcIfDlciSpRowStatus": gvcIfDlciSpRowStatus,
       "gvcIfDlciSpComponentName": gvcIfDlciSpComponentName,
       "gvcIfDlciSpStorageType": gvcIfDlciSpStorageType,
       "gvcIfDlciSpIndex": gvcIfDlciSpIndex,
       "gvcIfDlciSpParmsTable": gvcIfDlciSpParmsTable,
       "gvcIfDlciSpParmsEntry": gvcIfDlciSpParmsEntry,
       "gvcIfDlciSpRateEnforcement": gvcIfDlciSpRateEnforcement,
       "gvcIfDlciSpCommittedInformationRate": gvcIfDlciSpCommittedInformationRate,
       "gvcIfDlciSpCommittedBurstSize": gvcIfDlciSpCommittedBurstSize,
       "gvcIfDlciSpExcessBurstSize": gvcIfDlciSpExcessBurstSize,
       "gvcIfDlciSpMeasurementInterval": gvcIfDlciSpMeasurementInterval,
       "gvcIfDlciBnn": gvcIfDlciBnn,
       "gvcIfDlciBnnRowStatusTable": gvcIfDlciBnnRowStatusTable,
       "gvcIfDlciBnnRowStatusEntry": gvcIfDlciBnnRowStatusEntry,
       "gvcIfDlciBnnRowStatus": gvcIfDlciBnnRowStatus,
       "gvcIfDlciBnnComponentName": gvcIfDlciBnnComponentName,
       "gvcIfDlciBnnStorageType": gvcIfDlciBnnStorageType,
       "gvcIfDlciBnnIndex": gvcIfDlciBnnIndex,
       "gvcIfDlciLdev": gvcIfDlciLdev,
       "gvcIfDlciLdevRowStatusTable": gvcIfDlciLdevRowStatusTable,
       "gvcIfDlciLdevRowStatusEntry": gvcIfDlciLdevRowStatusEntry,
       "gvcIfDlciLdevRowStatus": gvcIfDlciLdevRowStatus,
       "gvcIfDlciLdevComponentName": gvcIfDlciLdevComponentName,
       "gvcIfDlciLdevStorageType": gvcIfDlciLdevStorageType,
       "gvcIfDlciLdevIndex": gvcIfDlciLdevIndex,
       "gvcIfDlciLdevAddrTable": gvcIfDlciLdevAddrTable,
       "gvcIfDlciLdevAddrEntry": gvcIfDlciLdevAddrEntry,
       "gvcIfDlciLdevMac": gvcIfDlciLdevMac,
       "gvcIfDlciLdevDevOpTable": gvcIfDlciLdevDevOpTable,
       "gvcIfDlciLdevDevOpEntry": gvcIfDlciLdevDevOpEntry,
       "gvcIfDlciLdevDeviceStatus": gvcIfDlciLdevDeviceStatus,
       "gvcIfDlciLdevActiveLinkStations": gvcIfDlciLdevActiveLinkStations,
       "gvcIfDlciLdevLastTimeUnreachable": gvcIfDlciLdevLastTimeUnreachable,
       "gvcIfDlciLdevLastTimeReachable": gvcIfDlciLdevLastTimeReachable,
       "gvcIfDlciLdevDeviceUnreachable": gvcIfDlciLdevDeviceUnreachable,
       "gvcIfDlciLdevMonitoringLcn": gvcIfDlciLdevMonitoringLcn,
       "gvcIfDlciLdevDmoTable": gvcIfDlciLdevDmoTable,
       "gvcIfDlciLdevDmoEntry": gvcIfDlciLdevDmoEntry,
       "gvcIfDlciLdevDeviceMonitoring": gvcIfDlciLdevDeviceMonitoring,
       "gvcIfDlciLdevClearVcsWhenUnreachable": gvcIfDlciLdevClearVcsWhenUnreachable,
       "gvcIfDlciLdevDeviceMonitoringTimer": gvcIfDlciLdevDeviceMonitoringTimer,
       "gvcIfDlciLdevTestResponseTimer": gvcIfDlciLdevTestResponseTimer,
       "gvcIfDlciLdevMaximumTestRetry": gvcIfDlciLdevMaximumTestRetry,
       "gvcIfDlciRdev": gvcIfDlciRdev,
       "gvcIfDlciRdevRowStatusTable": gvcIfDlciRdevRowStatusTable,
       "gvcIfDlciRdevRowStatusEntry": gvcIfDlciRdevRowStatusEntry,
       "gvcIfDlciRdevRowStatus": gvcIfDlciRdevRowStatus,
       "gvcIfDlciRdevComponentName": gvcIfDlciRdevComponentName,
       "gvcIfDlciRdevStorageType": gvcIfDlciRdevStorageType,
       "gvcIfDlciRdevIndex": gvcIfDlciRdevIndex,
       "gvcIfDlciRdevAddrTable": gvcIfDlciRdevAddrTable,
       "gvcIfDlciRdevAddrEntry": gvcIfDlciRdevAddrEntry,
       "gvcIfDlciRdevMac": gvcIfDlciRdevMac,
       "gvcIfDlciSap": gvcIfDlciSap,
       "gvcIfDlciSapRowStatusTable": gvcIfDlciSapRowStatusTable,
       "gvcIfDlciSapRowStatusEntry": gvcIfDlciSapRowStatusEntry,
       "gvcIfDlciSapRowStatus": gvcIfDlciSapRowStatus,
       "gvcIfDlciSapComponentName": gvcIfDlciSapComponentName,
       "gvcIfDlciSapStorageType": gvcIfDlciSapStorageType,
       "gvcIfDlciSapLocalSapIndex": gvcIfDlciSapLocalSapIndex,
       "gvcIfDlciSapRemoteSapIndex": gvcIfDlciSapRemoteSapIndex,
       "gvcIfDlciSapCircuit": gvcIfDlciSapCircuit,
       "gvcIfDlciSapCircuitRowStatusTable": gvcIfDlciSapCircuitRowStatusTable,
       "gvcIfDlciSapCircuitRowStatusEntry": gvcIfDlciSapCircuitRowStatusEntry,
       "gvcIfDlciSapCircuitRowStatus": gvcIfDlciSapCircuitRowStatus,
       "gvcIfDlciSapCircuitComponentName": gvcIfDlciSapCircuitComponentName,
       "gvcIfDlciSapCircuitStorageType": gvcIfDlciSapCircuitStorageType,
       "gvcIfDlciSapCircuitS1MacIndex": gvcIfDlciSapCircuitS1MacIndex,
       "gvcIfDlciSapCircuitS1SapIndex": gvcIfDlciSapCircuitS1SapIndex,
       "gvcIfDlciSapCircuitS2MacIndex": gvcIfDlciSapCircuitS2MacIndex,
       "gvcIfDlciSapCircuitS2SapIndex": gvcIfDlciSapCircuitS2SapIndex,
       "gvcIfDlciStateTable": gvcIfDlciStateTable,
       "gvcIfDlciStateEntry": gvcIfDlciStateEntry,
       "gvcIfDlciAdminState": gvcIfDlciAdminState,
       "gvcIfDlciOperationalState": gvcIfDlciOperationalState,
       "gvcIfDlciUsageState": gvcIfDlciUsageState,
       "gvcIfDlciAbitTable": gvcIfDlciAbitTable,
       "gvcIfDlciAbitEntry": gvcIfDlciAbitEntry,
       "gvcIfDlciABitStatusFromNetwork": gvcIfDlciABitStatusFromNetwork,
       "gvcIfDlciABitReasonFromNetwork": gvcIfDlciABitReasonFromNetwork,
       "gvcIfDlciABitStatusToNetwork": gvcIfDlciABitStatusToNetwork,
       "gvcIfDlciABitReasonToNetwork": gvcIfDlciABitReasonToNetwork,
       "gvcIfDlciStatsTable": gvcIfDlciStatsTable,
       "gvcIfDlciStatsEntry": gvcIfDlciStatsEntry,
       "gvcIfDlciFrmFromNetwork": gvcIfDlciFrmFromNetwork,
       "gvcIfDlciFrmToNetwork": gvcIfDlciFrmToNetwork,
       "gvcIfDlciFrmDiscardToNetwork": gvcIfDlciFrmDiscardToNetwork,
       "gvcIfDlciFramesWithUnknownSaps": gvcIfDlciFramesWithUnknownSaps,
       "gvcIfDlciOperTable": gvcIfDlciOperTable,
       "gvcIfDlciOperEntry": gvcIfDlciOperEntry,
       "gvcIfDlciEncapsulationType": gvcIfDlciEncapsulationType,
       "gvcIfDlciLocalDeviceMac": gvcIfDlciLocalDeviceMac,
       "gvcIfDlciRemoteDeviceMac": gvcIfDlciRemoteDeviceMac,
       "gvcIfDlciSpOpTable": gvcIfDlciSpOpTable,
       "gvcIfDlciSpOpEntry": gvcIfDlciSpOpEntry,
       "gvcIfDlciRateEnforcement": gvcIfDlciRateEnforcement,
       "gvcIfDlciCommittedInformationRate": gvcIfDlciCommittedInformationRate,
       "gvcIfDlciCommittedBurstSize": gvcIfDlciCommittedBurstSize,
       "gvcIfDlciExcessInformationRate": gvcIfDlciExcessInformationRate,
       "gvcIfDlciExcessBurstSize": gvcIfDlciExcessBurstSize,
       "gvcIfDlciMeasurementInterval": gvcIfDlciMeasurementInterval,
       "gvcIfFrSvc": gvcIfFrSvc,
       "gvcIfFrSvcRowStatusTable": gvcIfFrSvcRowStatusTable,
       "gvcIfFrSvcRowStatusEntry": gvcIfFrSvcRowStatusEntry,
       "gvcIfFrSvcRowStatus": gvcIfFrSvcRowStatus,
       "gvcIfFrSvcComponentName": gvcIfFrSvcComponentName,
       "gvcIfFrSvcStorageType": gvcIfFrSvcStorageType,
       "gvcIfFrSvcIndex": gvcIfFrSvcIndex,
       "gvcIfFrSvcProvisionedTable": gvcIfFrSvcProvisionedTable,
       "gvcIfFrSvcProvisionedEntry": gvcIfFrSvcProvisionedEntry,
       "gvcIfFrSvcMaximumFrameRelaySvcs": gvcIfFrSvcMaximumFrameRelaySvcs,
       "gvcIfFrSvcRateEnforcement": gvcIfFrSvcRateEnforcement,
       "gvcIfFrSvcMaximumCir": gvcIfFrSvcMaximumCir,
       "gvcIfFrSvcOperationalTable": gvcIfFrSvcOperationalTable,
       "gvcIfFrSvcOperationalEntry": gvcIfFrSvcOperationalEntry,
       "gvcIfFrSvcCurrentNumberOfSvcCalls": gvcIfFrSvcCurrentNumberOfSvcCalls,
       "gvcIfSMacF": gvcIfSMacF,
       "gvcIfSMacFRowStatusTable": gvcIfSMacFRowStatusTable,
       "gvcIfSMacFRowStatusEntry": gvcIfSMacFRowStatusEntry,
       "gvcIfSMacFRowStatus": gvcIfSMacFRowStatus,
       "gvcIfSMacFComponentName": gvcIfSMacFComponentName,
       "gvcIfSMacFStorageType": gvcIfSMacFStorageType,
       "gvcIfSMacFIndex": gvcIfSMacFIndex,
       "gvcIfSMacFOperTable": gvcIfSMacFOperTable,
       "gvcIfSMacFOperEntry": gvcIfSMacFOperEntry,
       "gvcIfSMacFFramesMatchingFilter": gvcIfSMacFFramesMatchingFilter,
       "gvcIfDMacF": gvcIfDMacF,
       "gvcIfDMacFRowStatusTable": gvcIfDMacFRowStatusTable,
       "gvcIfDMacFRowStatusEntry": gvcIfDMacFRowStatusEntry,
       "gvcIfDMacFRowStatus": gvcIfDMacFRowStatus,
       "gvcIfDMacFComponentName": gvcIfDMacFComponentName,
       "gvcIfDMacFStorageType": gvcIfDMacFStorageType,
       "gvcIfDMacFIndex": gvcIfDMacFIndex,
       "gvcIfDMacFOperTable": gvcIfDMacFOperTable,
       "gvcIfDMacFOperEntry": gvcIfDMacFOperEntry,
       "gvcIfDMacFFramesMatchingFilter": gvcIfDMacFFramesMatchingFilter,
       "gvcIfCidDataTable": gvcIfCidDataTable,
       "gvcIfCidDataEntry": gvcIfCidDataEntry,
       "gvcIfCustomerIdentifier": gvcIfCustomerIdentifier,
       "gvcIfProvTable": gvcIfProvTable,
       "gvcIfProvEntry": gvcIfProvEntry,
       "gvcIfLogicalProcessor": gvcIfLogicalProcessor,
       "gvcIfMaxActiveLinkStation": gvcIfMaxActiveLinkStation,
       "gvcIfStateTable": gvcIfStateTable,
       "gvcIfStateEntry": gvcIfStateEntry,
       "gvcIfAdminState": gvcIfAdminState,
       "gvcIfOperationalState": gvcIfOperationalState,
       "gvcIfUsageState": gvcIfUsageState,
       "gvcIfOpTable": gvcIfOpTable,
       "gvcIfOpEntry": gvcIfOpEntry,
       "gvcIfActiveLinkStations": gvcIfActiveLinkStations,
       "gvcIfIssueLcnClearAlarm": gvcIfIssueLcnClearAlarm,
       "gvcIfActiveQllcCalls": gvcIfActiveQllcCalls,
       "gvcIfStatsTable": gvcIfStatsTable,
       "gvcIfStatsEntry": gvcIfStatsEntry,
       "gvcIfCallsToNetwork": gvcIfCallsToNetwork,
       "gvcIfCallsFromNetwork": gvcIfCallsFromNetwork,
       "gvcIfCallsRefusedByNetwork": gvcIfCallsRefusedByNetwork,
       "gvcIfCallsRefusedByInterface": gvcIfCallsRefusedByInterface,
       "gvcIfPeakActiveLinkStations": gvcIfPeakActiveLinkStations,
       "gvcIfBcastFramesDiscarded": gvcIfBcastFramesDiscarded,
       "gvcIfDiscardedQllcCalls": gvcIfDiscardedQllcCalls,
       "generalVcInterfaceMIB": generalVcInterfaceMIB,
       "generalVcInterfaceGroup": generalVcInterfaceGroup,
       "generalVcInterfaceGroupBE": generalVcInterfaceGroupBE,
       "generalVcInterfaceGroupBE01": generalVcInterfaceGroupBE01,
       "generalVcInterfaceGroupBE01A": generalVcInterfaceGroupBE01A,
       "generalVcInterfaceCapabilities": generalVcInterfaceCapabilities,
       "generalVcInterfaceCapabilitiesBE": generalVcInterfaceCapabilitiesBE,
       "generalVcInterfaceCapabilitiesBE01": generalVcInterfaceCapabilitiesBE01,
       "generalVcInterfaceCapabilitiesBE01A": generalVcInterfaceCapabilitiesBE01A}
)
