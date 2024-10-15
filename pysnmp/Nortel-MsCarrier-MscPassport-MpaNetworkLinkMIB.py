# SNMP MIB module (Nortel-MsCarrier-MscPassport-MpaNetworkLinkMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-MsCarrier-MscPassport-MpaNetworkLinkMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:32:52 2024
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
    "Nortel-MsCarrier-MscPassport-StandardTextualConventionsMIB",
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
 DigitString,
 EnterpriseDateAndTime,
 Hex,
 HexString,
 Link,
 NonReplicated,
 PassportCounter64,
 Unsigned64) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-TextualConventionsMIB",
    "AsciiString",
    "DigitString",
    "EnterpriseDateAndTime",
    "Hex",
    "HexString",
    "Link",
    "NonReplicated",
    "PassportCounter64",
    "Unsigned64")

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

_MscMpanl_ObjectIdentity = ObjectIdentity
mscMpanl = _MscMpanl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123)
)
_MscMpanlRowStatusTable_Object = MibTable
mscMpanlRowStatusTable = _MscMpanlRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 1)
)
if mibBuilder.loadTexts:
    mscMpanlRowStatusTable.setStatus("mandatory")
_MscMpanlRowStatusEntry_Object = MibTableRow
mscMpanlRowStatusEntry = _MscMpanlRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 1, 1)
)
mscMpanlRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-MpaNetworkLinkMIB", "mscMpanlIndex"),
)
if mibBuilder.loadTexts:
    mscMpanlRowStatusEntry.setStatus("mandatory")
_MscMpanlRowStatus_Type = RowStatus
_MscMpanlRowStatus_Object = MibTableColumn
mscMpanlRowStatus = _MscMpanlRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 1, 1, 1),
    _MscMpanlRowStatus_Type()
)
mscMpanlRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscMpanlRowStatus.setStatus("mandatory")
_MscMpanlComponentName_Type = DisplayString
_MscMpanlComponentName_Object = MibTableColumn
mscMpanlComponentName = _MscMpanlComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 1, 1, 2),
    _MscMpanlComponentName_Type()
)
mscMpanlComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlComponentName.setStatus("mandatory")
_MscMpanlStorageType_Type = StorageType
_MscMpanlStorageType_Object = MibTableColumn
mscMpanlStorageType = _MscMpanlStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 1, 1, 4),
    _MscMpanlStorageType_Type()
)
mscMpanlStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlStorageType.setStatus("mandatory")


class _MscMpanlIndex_Type(Integer32):
    """Custom type mscMpanlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MscMpanlIndex_Type.__name__ = "Integer32"
_MscMpanlIndex_Object = MibTableColumn
mscMpanlIndex = _MscMpanlIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 1, 1, 10),
    _MscMpanlIndex_Type()
)
mscMpanlIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscMpanlIndex.setStatus("mandatory")
_MscMpanlDna_ObjectIdentity = ObjectIdentity
mscMpanlDna = _MscMpanlDna_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 2)
)
_MscMpanlDnaRowStatusTable_Object = MibTable
mscMpanlDnaRowStatusTable = _MscMpanlDnaRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 2, 1)
)
if mibBuilder.loadTexts:
    mscMpanlDnaRowStatusTable.setStatus("mandatory")
_MscMpanlDnaRowStatusEntry_Object = MibTableRow
mscMpanlDnaRowStatusEntry = _MscMpanlDnaRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 2, 1, 1)
)
mscMpanlDnaRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-MpaNetworkLinkMIB", "mscMpanlIndex"),
    (0, "Nortel-MsCarrier-MscPassport-MpaNetworkLinkMIB", "mscMpanlDnaIndex"),
)
if mibBuilder.loadTexts:
    mscMpanlDnaRowStatusEntry.setStatus("mandatory")
_MscMpanlDnaRowStatus_Type = RowStatus
_MscMpanlDnaRowStatus_Object = MibTableColumn
mscMpanlDnaRowStatus = _MscMpanlDnaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 2, 1, 1, 1),
    _MscMpanlDnaRowStatus_Type()
)
mscMpanlDnaRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDnaRowStatus.setStatus("mandatory")
_MscMpanlDnaComponentName_Type = DisplayString
_MscMpanlDnaComponentName_Object = MibTableColumn
mscMpanlDnaComponentName = _MscMpanlDnaComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 2, 1, 1, 2),
    _MscMpanlDnaComponentName_Type()
)
mscMpanlDnaComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDnaComponentName.setStatus("mandatory")
_MscMpanlDnaStorageType_Type = StorageType
_MscMpanlDnaStorageType_Object = MibTableColumn
mscMpanlDnaStorageType = _MscMpanlDnaStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 2, 1, 1, 4),
    _MscMpanlDnaStorageType_Type()
)
mscMpanlDnaStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDnaStorageType.setStatus("mandatory")
_MscMpanlDnaIndex_Type = NonReplicated
_MscMpanlDnaIndex_Object = MibTableColumn
mscMpanlDnaIndex = _MscMpanlDnaIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 2, 1, 1, 10),
    _MscMpanlDnaIndex_Type()
)
mscMpanlDnaIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscMpanlDnaIndex.setStatus("mandatory")
_MscMpanlDnaOutgoingOptionsTable_Object = MibTable
mscMpanlDnaOutgoingOptionsTable = _MscMpanlDnaOutgoingOptionsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 2, 11)
)
if mibBuilder.loadTexts:
    mscMpanlDnaOutgoingOptionsTable.setStatus("mandatory")
_MscMpanlDnaOutgoingOptionsEntry_Object = MibTableRow
mscMpanlDnaOutgoingOptionsEntry = _MscMpanlDnaOutgoingOptionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 2, 11, 1)
)
mscMpanlDnaOutgoingOptionsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-MpaNetworkLinkMIB", "mscMpanlIndex"),
    (0, "Nortel-MsCarrier-MscPassport-MpaNetworkLinkMIB", "mscMpanlDnaIndex"),
)
if mibBuilder.loadTexts:
    mscMpanlDnaOutgoingOptionsEntry.setStatus("mandatory")


class _MscMpanlDnaDefaultTransferPriority_Type(Integer32):
    """Custom type mscMpanlDnaDefaultTransferPriority based on Integer32"""
    defaultValue = 0

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
              12,
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("n0", 0),
          ("n1", 1),
          ("n10", 10),
          ("n11", 11),
          ("n12", 12),
          ("n13", 13),
          ("n14", 14),
          ("n15", 15),
          ("n2", 2),
          ("n3", 3),
          ("n4", 4),
          ("n5", 5),
          ("n6", 6),
          ("n7", 7),
          ("n8", 8),
          ("n9", 9))
    )


_MscMpanlDnaDefaultTransferPriority_Type.__name__ = "Integer32"
_MscMpanlDnaDefaultTransferPriority_Object = MibTableColumn
mscMpanlDnaDefaultTransferPriority = _MscMpanlDnaDefaultTransferPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 2, 11, 1, 18),
    _MscMpanlDnaDefaultTransferPriority_Type()
)
mscMpanlDnaDefaultTransferPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscMpanlDnaDefaultTransferPriority.setStatus("mandatory")
_MscMpanlDnaCallOptionsTable_Object = MibTable
mscMpanlDnaCallOptionsTable = _MscMpanlDnaCallOptionsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 2, 13)
)
if mibBuilder.loadTexts:
    mscMpanlDnaCallOptionsTable.setStatus("mandatory")
_MscMpanlDnaCallOptionsEntry_Object = MibTableRow
mscMpanlDnaCallOptionsEntry = _MscMpanlDnaCallOptionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 2, 13, 1)
)
mscMpanlDnaCallOptionsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-MpaNetworkLinkMIB", "mscMpanlIndex"),
    (0, "Nortel-MsCarrier-MscPassport-MpaNetworkLinkMIB", "mscMpanlDnaIndex"),
)
if mibBuilder.loadTexts:
    mscMpanlDnaCallOptionsEntry.setStatus("mandatory")


class _MscMpanlDnaAccountClass_Type(Unsigned32):
    """Custom type mscMpanlDnaAccountClass based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscMpanlDnaAccountClass_Type.__name__ = "Unsigned32"
_MscMpanlDnaAccountClass_Object = MibTableColumn
mscMpanlDnaAccountClass = _MscMpanlDnaAccountClass_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 2, 13, 1, 10),
    _MscMpanlDnaAccountClass_Type()
)
mscMpanlDnaAccountClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscMpanlDnaAccountClass.setStatus("mandatory")


class _MscMpanlDnaAccountCollection_Type(OctetString):
    """Custom type mscMpanlDnaAccountCollection based on OctetString"""
    defaultHexValue = "80"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscMpanlDnaAccountCollection_Type.__name__ = "OctetString"
_MscMpanlDnaAccountCollection_Object = MibTableColumn
mscMpanlDnaAccountCollection = _MscMpanlDnaAccountCollection_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 2, 13, 1, 11),
    _MscMpanlDnaAccountCollection_Type()
)
mscMpanlDnaAccountCollection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscMpanlDnaAccountCollection.setStatus("mandatory")


class _MscMpanlDnaServiceExchange_Type(Unsigned32):
    """Custom type mscMpanlDnaServiceExchange based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscMpanlDnaServiceExchange_Type.__name__ = "Unsigned32"
_MscMpanlDnaServiceExchange_Object = MibTableColumn
mscMpanlDnaServiceExchange = _MscMpanlDnaServiceExchange_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 2, 13, 1, 12),
    _MscMpanlDnaServiceExchange_Type()
)
mscMpanlDnaServiceExchange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscMpanlDnaServiceExchange.setStatus("mandatory")


class _MscMpanlDnaEgressAccounting_Type(Integer32):
    """Custom type mscMpanlDnaEgressAccounting based on Integer32"""
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


_MscMpanlDnaEgressAccounting_Type.__name__ = "Integer32"
_MscMpanlDnaEgressAccounting_Object = MibTableColumn
mscMpanlDnaEgressAccounting = _MscMpanlDnaEgressAccounting_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 2, 13, 1, 13),
    _MscMpanlDnaEgressAccounting_Type()
)
mscMpanlDnaEgressAccounting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscMpanlDnaEgressAccounting.setStatus("mandatory")
_MscMpanlFramer_ObjectIdentity = ObjectIdentity
mscMpanlFramer = _MscMpanlFramer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 3)
)
_MscMpanlFramerRowStatusTable_Object = MibTable
mscMpanlFramerRowStatusTable = _MscMpanlFramerRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 3, 1)
)
if mibBuilder.loadTexts:
    mscMpanlFramerRowStatusTable.setStatus("mandatory")
_MscMpanlFramerRowStatusEntry_Object = MibTableRow
mscMpanlFramerRowStatusEntry = _MscMpanlFramerRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 3, 1, 1)
)
mscMpanlFramerRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-MpaNetworkLinkMIB", "mscMpanlIndex"),
    (0, "Nortel-MsCarrier-MscPassport-MpaNetworkLinkMIB", "mscMpanlFramerIndex"),
)
if mibBuilder.loadTexts:
    mscMpanlFramerRowStatusEntry.setStatus("mandatory")
_MscMpanlFramerRowStatus_Type = RowStatus
_MscMpanlFramerRowStatus_Object = MibTableColumn
mscMpanlFramerRowStatus = _MscMpanlFramerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 3, 1, 1, 1),
    _MscMpanlFramerRowStatus_Type()
)
mscMpanlFramerRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscMpanlFramerRowStatus.setStatus("mandatory")
_MscMpanlFramerComponentName_Type = DisplayString
_MscMpanlFramerComponentName_Object = MibTableColumn
mscMpanlFramerComponentName = _MscMpanlFramerComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 3, 1, 1, 2),
    _MscMpanlFramerComponentName_Type()
)
mscMpanlFramerComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlFramerComponentName.setStatus("mandatory")
_MscMpanlFramerStorageType_Type = StorageType
_MscMpanlFramerStorageType_Object = MibTableColumn
mscMpanlFramerStorageType = _MscMpanlFramerStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 3, 1, 1, 4),
    _MscMpanlFramerStorageType_Type()
)
mscMpanlFramerStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlFramerStorageType.setStatus("mandatory")
_MscMpanlFramerIndex_Type = NonReplicated
_MscMpanlFramerIndex_Object = MibTableColumn
mscMpanlFramerIndex = _MscMpanlFramerIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 3, 1, 1, 10),
    _MscMpanlFramerIndex_Type()
)
mscMpanlFramerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscMpanlFramerIndex.setStatus("mandatory")
_MscMpanlFramerProvTable_Object = MibTable
mscMpanlFramerProvTable = _MscMpanlFramerProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 3, 10)
)
if mibBuilder.loadTexts:
    mscMpanlFramerProvTable.setStatus("mandatory")
_MscMpanlFramerProvEntry_Object = MibTableRow
mscMpanlFramerProvEntry = _MscMpanlFramerProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 3, 10, 1)
)
mscMpanlFramerProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-MpaNetworkLinkMIB", "mscMpanlIndex"),
    (0, "Nortel-MsCarrier-MscPassport-MpaNetworkLinkMIB", "mscMpanlFramerIndex"),
)
if mibBuilder.loadTexts:
    mscMpanlFramerProvEntry.setStatus("mandatory")
_MscMpanlFramerInterfaceName_Type = Link
_MscMpanlFramerInterfaceName_Object = MibTableColumn
mscMpanlFramerInterfaceName = _MscMpanlFramerInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 3, 10, 1, 1),
    _MscMpanlFramerInterfaceName_Type()
)
mscMpanlFramerInterfaceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscMpanlFramerInterfaceName.setStatus("mandatory")
_MscMpanlFramerLinkTable_Object = MibTable
mscMpanlFramerLinkTable = _MscMpanlFramerLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 3, 11)
)
if mibBuilder.loadTexts:
    mscMpanlFramerLinkTable.setStatus("mandatory")
_MscMpanlFramerLinkEntry_Object = MibTableRow
mscMpanlFramerLinkEntry = _MscMpanlFramerLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 3, 11, 1)
)
mscMpanlFramerLinkEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-MpaNetworkLinkMIB", "mscMpanlIndex"),
    (0, "Nortel-MsCarrier-MscPassport-MpaNetworkLinkMIB", "mscMpanlFramerIndex"),
)
if mibBuilder.loadTexts:
    mscMpanlFramerLinkEntry.setStatus("mandatory")


class _MscMpanlFramerDataInversion_Type(Integer32):
    """Custom type mscMpanlFramerDataInversion based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              16)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 16))
    )


_MscMpanlFramerDataInversion_Type.__name__ = "Integer32"
_MscMpanlFramerDataInversion_Object = MibTableColumn
mscMpanlFramerDataInversion = _MscMpanlFramerDataInversion_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 3, 11, 1, 2),
    _MscMpanlFramerDataInversion_Type()
)
mscMpanlFramerDataInversion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscMpanlFramerDataInversion.setStatus("mandatory")


class _MscMpanlFramerFrameCrcType_Type(Integer32):
    """Custom type mscMpanlFramerFrameCrcType based on Integer32"""
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
        *(("crc16", 0),
          ("crc32", 1),
          ("noCrc", 2))
    )


_MscMpanlFramerFrameCrcType_Type.__name__ = "Integer32"
_MscMpanlFramerFrameCrcType_Object = MibTableColumn
mscMpanlFramerFrameCrcType = _MscMpanlFramerFrameCrcType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 3, 11, 1, 3),
    _MscMpanlFramerFrameCrcType_Type()
)
mscMpanlFramerFrameCrcType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscMpanlFramerFrameCrcType.setStatus("mandatory")


class _MscMpanlFramerFlagsBetweenFrames_Type(Unsigned32):
    """Custom type mscMpanlFramerFlagsBetweenFrames based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_MscMpanlFramerFlagsBetweenFrames_Type.__name__ = "Unsigned32"
_MscMpanlFramerFlagsBetweenFrames_Object = MibTableColumn
mscMpanlFramerFlagsBetweenFrames = _MscMpanlFramerFlagsBetweenFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 3, 11, 1, 4),
    _MscMpanlFramerFlagsBetweenFrames_Type()
)
mscMpanlFramerFlagsBetweenFrames.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscMpanlFramerFlagsBetweenFrames.setStatus("mandatory")
_MscMpanlFramerStateTable_Object = MibTable
mscMpanlFramerStateTable = _MscMpanlFramerStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 3, 12)
)
if mibBuilder.loadTexts:
    mscMpanlFramerStateTable.setStatus("mandatory")
_MscMpanlFramerStateEntry_Object = MibTableRow
mscMpanlFramerStateEntry = _MscMpanlFramerStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 3, 12, 1)
)
mscMpanlFramerStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-MpaNetworkLinkMIB", "mscMpanlIndex"),
    (0, "Nortel-MsCarrier-MscPassport-MpaNetworkLinkMIB", "mscMpanlFramerIndex"),
)
if mibBuilder.loadTexts:
    mscMpanlFramerStateEntry.setStatus("mandatory")


class _MscMpanlFramerAdminState_Type(Integer32):
    """Custom type mscMpanlFramerAdminState based on Integer32"""
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


_MscMpanlFramerAdminState_Type.__name__ = "Integer32"
_MscMpanlFramerAdminState_Object = MibTableColumn
mscMpanlFramerAdminState = _MscMpanlFramerAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 3, 12, 1, 1),
    _MscMpanlFramerAdminState_Type()
)
mscMpanlFramerAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlFramerAdminState.setStatus("mandatory")


class _MscMpanlFramerOperationalState_Type(Integer32):
    """Custom type mscMpanlFramerOperationalState based on Integer32"""
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


_MscMpanlFramerOperationalState_Type.__name__ = "Integer32"
_MscMpanlFramerOperationalState_Object = MibTableColumn
mscMpanlFramerOperationalState = _MscMpanlFramerOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 3, 12, 1, 2),
    _MscMpanlFramerOperationalState_Type()
)
mscMpanlFramerOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlFramerOperationalState.setStatus("mandatory")


class _MscMpanlFramerUsageState_Type(Integer32):
    """Custom type mscMpanlFramerUsageState based on Integer32"""
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


_MscMpanlFramerUsageState_Type.__name__ = "Integer32"
_MscMpanlFramerUsageState_Object = MibTableColumn
mscMpanlFramerUsageState = _MscMpanlFramerUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 3, 12, 1, 3),
    _MscMpanlFramerUsageState_Type()
)
mscMpanlFramerUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlFramerUsageState.setStatus("mandatory")
_MscMpanlFramerStatsTable_Object = MibTable
mscMpanlFramerStatsTable = _MscMpanlFramerStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 3, 13)
)
if mibBuilder.loadTexts:
    mscMpanlFramerStatsTable.setStatus("mandatory")
_MscMpanlFramerStatsEntry_Object = MibTableRow
mscMpanlFramerStatsEntry = _MscMpanlFramerStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 3, 13, 1)
)
mscMpanlFramerStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-MpaNetworkLinkMIB", "mscMpanlIndex"),
    (0, "Nortel-MsCarrier-MscPassport-MpaNetworkLinkMIB", "mscMpanlFramerIndex"),
)
if mibBuilder.loadTexts:
    mscMpanlFramerStatsEntry.setStatus("mandatory")
_MscMpanlFramerFrmToIf_Type = Counter32
_MscMpanlFramerFrmToIf_Object = MibTableColumn
mscMpanlFramerFrmToIf = _MscMpanlFramerFrmToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 3, 13, 1, 1),
    _MscMpanlFramerFrmToIf_Type()
)
mscMpanlFramerFrmToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlFramerFrmToIf.setStatus("obsolete")
_MscMpanlFramerFrmFromIf_Type = Counter32
_MscMpanlFramerFrmFromIf_Object = MibTableColumn
mscMpanlFramerFrmFromIf = _MscMpanlFramerFrmFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 3, 13, 1, 2),
    _MscMpanlFramerFrmFromIf_Type()
)
mscMpanlFramerFrmFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlFramerFrmFromIf.setStatus("obsolete")
_MscMpanlFramerOctetFromIf_Type = Counter32
_MscMpanlFramerOctetFromIf_Object = MibTableColumn
mscMpanlFramerOctetFromIf = _MscMpanlFramerOctetFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 3, 13, 1, 3),
    _MscMpanlFramerOctetFromIf_Type()
)
mscMpanlFramerOctetFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlFramerOctetFromIf.setStatus("obsolete")
_MscMpanlFramerAborts_Type = Counter32
_MscMpanlFramerAborts_Object = MibTableColumn
mscMpanlFramerAborts = _MscMpanlFramerAborts_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 3, 13, 1, 4),
    _MscMpanlFramerAborts_Type()
)
mscMpanlFramerAborts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlFramerAborts.setStatus("mandatory")
_MscMpanlFramerCrcErrors_Type = Counter32
_MscMpanlFramerCrcErrors_Object = MibTableColumn
mscMpanlFramerCrcErrors = _MscMpanlFramerCrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 3, 13, 1, 5),
    _MscMpanlFramerCrcErrors_Type()
)
mscMpanlFramerCrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlFramerCrcErrors.setStatus("mandatory")
_MscMpanlFramerLrcErrors_Type = Counter32
_MscMpanlFramerLrcErrors_Object = MibTableColumn
mscMpanlFramerLrcErrors = _MscMpanlFramerLrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 3, 13, 1, 6),
    _MscMpanlFramerLrcErrors_Type()
)
mscMpanlFramerLrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlFramerLrcErrors.setStatus("mandatory")
_MscMpanlFramerNonOctetErrors_Type = Counter32
_MscMpanlFramerNonOctetErrors_Object = MibTableColumn
mscMpanlFramerNonOctetErrors = _MscMpanlFramerNonOctetErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 3, 13, 1, 7),
    _MscMpanlFramerNonOctetErrors_Type()
)
mscMpanlFramerNonOctetErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlFramerNonOctetErrors.setStatus("mandatory")
_MscMpanlFramerOverruns_Type = Counter32
_MscMpanlFramerOverruns_Object = MibTableColumn
mscMpanlFramerOverruns = _MscMpanlFramerOverruns_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 3, 13, 1, 8),
    _MscMpanlFramerOverruns_Type()
)
mscMpanlFramerOverruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlFramerOverruns.setStatus("mandatory")
_MscMpanlFramerUnderruns_Type = Counter32
_MscMpanlFramerUnderruns_Object = MibTableColumn
mscMpanlFramerUnderruns = _MscMpanlFramerUnderruns_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 3, 13, 1, 9),
    _MscMpanlFramerUnderruns_Type()
)
mscMpanlFramerUnderruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlFramerUnderruns.setStatus("mandatory")
_MscMpanlFramerLargeFrmErrors_Type = Counter32
_MscMpanlFramerLargeFrmErrors_Object = MibTableColumn
mscMpanlFramerLargeFrmErrors = _MscMpanlFramerLargeFrmErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 3, 13, 1, 10),
    _MscMpanlFramerLargeFrmErrors_Type()
)
mscMpanlFramerLargeFrmErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlFramerLargeFrmErrors.setStatus("mandatory")
_MscMpanlFramerFrmModeErrors_Type = Counter32
_MscMpanlFramerFrmModeErrors_Object = MibTableColumn
mscMpanlFramerFrmModeErrors = _MscMpanlFramerFrmModeErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 3, 13, 1, 11),
    _MscMpanlFramerFrmModeErrors_Type()
)
mscMpanlFramerFrmModeErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlFramerFrmModeErrors.setStatus("mandatory")
_MscMpanlFramerFrmToIf64_Type = PassportCounter64
_MscMpanlFramerFrmToIf64_Object = MibTableColumn
mscMpanlFramerFrmToIf64 = _MscMpanlFramerFrmToIf64_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 3, 13, 1, 14),
    _MscMpanlFramerFrmToIf64_Type()
)
mscMpanlFramerFrmToIf64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlFramerFrmToIf64.setStatus("mandatory")
_MscMpanlFramerFrmFromIf64_Type = PassportCounter64
_MscMpanlFramerFrmFromIf64_Object = MibTableColumn
mscMpanlFramerFrmFromIf64 = _MscMpanlFramerFrmFromIf64_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 3, 13, 1, 15),
    _MscMpanlFramerFrmFromIf64_Type()
)
mscMpanlFramerFrmFromIf64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlFramerFrmFromIf64.setStatus("mandatory")
_MscMpanlFramerOctetFromIf64_Type = PassportCounter64
_MscMpanlFramerOctetFromIf64_Object = MibTableColumn
mscMpanlFramerOctetFromIf64 = _MscMpanlFramerOctetFromIf64_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 3, 13, 1, 16),
    _MscMpanlFramerOctetFromIf64_Type()
)
mscMpanlFramerOctetFromIf64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlFramerOctetFromIf64.setStatus("mandatory")
_MscMpanlFramerUtilTable_Object = MibTable
mscMpanlFramerUtilTable = _MscMpanlFramerUtilTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 3, 14)
)
if mibBuilder.loadTexts:
    mscMpanlFramerUtilTable.setStatus("mandatory")
_MscMpanlFramerUtilEntry_Object = MibTableRow
mscMpanlFramerUtilEntry = _MscMpanlFramerUtilEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 3, 14, 1)
)
mscMpanlFramerUtilEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-MpaNetworkLinkMIB", "mscMpanlIndex"),
    (0, "Nortel-MsCarrier-MscPassport-MpaNetworkLinkMIB", "mscMpanlFramerIndex"),
)
if mibBuilder.loadTexts:
    mscMpanlFramerUtilEntry.setStatus("mandatory")


class _MscMpanlFramerNormPrioLinkUtilToIf_Type(Gauge32):
    """Custom type mscMpanlFramerNormPrioLinkUtilToIf based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_MscMpanlFramerNormPrioLinkUtilToIf_Type.__name__ = "Gauge32"
_MscMpanlFramerNormPrioLinkUtilToIf_Object = MibTableColumn
mscMpanlFramerNormPrioLinkUtilToIf = _MscMpanlFramerNormPrioLinkUtilToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 3, 14, 1, 1),
    _MscMpanlFramerNormPrioLinkUtilToIf_Type()
)
mscMpanlFramerNormPrioLinkUtilToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlFramerNormPrioLinkUtilToIf.setStatus("mandatory")


class _MscMpanlFramerNormPrioLinkUtilFromIf_Type(Gauge32):
    """Custom type mscMpanlFramerNormPrioLinkUtilFromIf based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_MscMpanlFramerNormPrioLinkUtilFromIf_Type.__name__ = "Gauge32"
_MscMpanlFramerNormPrioLinkUtilFromIf_Object = MibTableColumn
mscMpanlFramerNormPrioLinkUtilFromIf = _MscMpanlFramerNormPrioLinkUtilFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 3, 14, 1, 3),
    _MscMpanlFramerNormPrioLinkUtilFromIf_Type()
)
mscMpanlFramerNormPrioLinkUtilFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlFramerNormPrioLinkUtilFromIf.setStatus("mandatory")
_MscMpanlPrefixDna_ObjectIdentity = ObjectIdentity
mscMpanlPrefixDna = _MscMpanlPrefixDna_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 4)
)
_MscMpanlPrefixDnaRowStatusTable_Object = MibTable
mscMpanlPrefixDnaRowStatusTable = _MscMpanlPrefixDnaRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 4, 1)
)
if mibBuilder.loadTexts:
    mscMpanlPrefixDnaRowStatusTable.setStatus("mandatory")
_MscMpanlPrefixDnaRowStatusEntry_Object = MibTableRow
mscMpanlPrefixDnaRowStatusEntry = _MscMpanlPrefixDnaRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 4, 1, 1)
)
mscMpanlPrefixDnaRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-MpaNetworkLinkMIB", "mscMpanlIndex"),
    (0, "Nortel-MsCarrier-MscPassport-MpaNetworkLinkMIB", "mscMpanlPrefixDnaNumberingPlanIndicatorIndex"),
    (0, "Nortel-MsCarrier-MscPassport-MpaNetworkLinkMIB", "mscMpanlPrefixDnaDataNetworkAddressIndex"),
)
if mibBuilder.loadTexts:
    mscMpanlPrefixDnaRowStatusEntry.setStatus("mandatory")
_MscMpanlPrefixDnaRowStatus_Type = RowStatus
_MscMpanlPrefixDnaRowStatus_Object = MibTableColumn
mscMpanlPrefixDnaRowStatus = _MscMpanlPrefixDnaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 4, 1, 1, 1),
    _MscMpanlPrefixDnaRowStatus_Type()
)
mscMpanlPrefixDnaRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlPrefixDnaRowStatus.setStatus("mandatory")
_MscMpanlPrefixDnaComponentName_Type = DisplayString
_MscMpanlPrefixDnaComponentName_Object = MibTableColumn
mscMpanlPrefixDnaComponentName = _MscMpanlPrefixDnaComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 4, 1, 1, 2),
    _MscMpanlPrefixDnaComponentName_Type()
)
mscMpanlPrefixDnaComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlPrefixDnaComponentName.setStatus("mandatory")
_MscMpanlPrefixDnaStorageType_Type = StorageType
_MscMpanlPrefixDnaStorageType_Object = MibTableColumn
mscMpanlPrefixDnaStorageType = _MscMpanlPrefixDnaStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 4, 1, 1, 4),
    _MscMpanlPrefixDnaStorageType_Type()
)
mscMpanlPrefixDnaStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlPrefixDnaStorageType.setStatus("mandatory")


class _MscMpanlPrefixDnaNumberingPlanIndicatorIndex_Type(Integer32):
    """Custom type mscMpanlPrefixDnaNumberingPlanIndicatorIndex based on Integer32"""
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


_MscMpanlPrefixDnaNumberingPlanIndicatorIndex_Type.__name__ = "Integer32"
_MscMpanlPrefixDnaNumberingPlanIndicatorIndex_Object = MibTableColumn
mscMpanlPrefixDnaNumberingPlanIndicatorIndex = _MscMpanlPrefixDnaNumberingPlanIndicatorIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 4, 1, 1, 10),
    _MscMpanlPrefixDnaNumberingPlanIndicatorIndex_Type()
)
mscMpanlPrefixDnaNumberingPlanIndicatorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscMpanlPrefixDnaNumberingPlanIndicatorIndex.setStatus("mandatory")


class _MscMpanlPrefixDnaDataNetworkAddressIndex_Type(DigitString):
    """Custom type mscMpanlPrefixDnaDataNetworkAddressIndex based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_MscMpanlPrefixDnaDataNetworkAddressIndex_Type.__name__ = "DigitString"
_MscMpanlPrefixDnaDataNetworkAddressIndex_Object = MibTableColumn
mscMpanlPrefixDnaDataNetworkAddressIndex = _MscMpanlPrefixDnaDataNetworkAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 4, 1, 1, 11),
    _MscMpanlPrefixDnaDataNetworkAddressIndex_Type()
)
mscMpanlPrefixDnaDataNetworkAddressIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscMpanlPrefixDnaDataNetworkAddressIndex.setStatus("mandatory")
_MscMpanlDlci_ObjectIdentity = ObjectIdentity
mscMpanlDlci = _MscMpanlDlci_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5)
)
_MscMpanlDlciRowStatusTable_Object = MibTable
mscMpanlDlciRowStatusTable = _MscMpanlDlciRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 1)
)
if mibBuilder.loadTexts:
    mscMpanlDlciRowStatusTable.setStatus("mandatory")
_MscMpanlDlciRowStatusEntry_Object = MibTableRow
mscMpanlDlciRowStatusEntry = _MscMpanlDlciRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 1, 1)
)
mscMpanlDlciRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-MpaNetworkLinkMIB", "mscMpanlIndex"),
    (0, "Nortel-MsCarrier-MscPassport-MpaNetworkLinkMIB", "mscMpanlDlciIndex"),
)
if mibBuilder.loadTexts:
    mscMpanlDlciRowStatusEntry.setStatus("mandatory")
_MscMpanlDlciRowStatus_Type = RowStatus
_MscMpanlDlciRowStatus_Object = MibTableColumn
mscMpanlDlciRowStatus = _MscMpanlDlciRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 1, 1, 1),
    _MscMpanlDlciRowStatus_Type()
)
mscMpanlDlciRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciRowStatus.setStatus("mandatory")
_MscMpanlDlciComponentName_Type = DisplayString
_MscMpanlDlciComponentName_Object = MibTableColumn
mscMpanlDlciComponentName = _MscMpanlDlciComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 1, 1, 2),
    _MscMpanlDlciComponentName_Type()
)
mscMpanlDlciComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciComponentName.setStatus("mandatory")
_MscMpanlDlciStorageType_Type = StorageType
_MscMpanlDlciStorageType_Object = MibTableColumn
mscMpanlDlciStorageType = _MscMpanlDlciStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 1, 1, 4),
    _MscMpanlDlciStorageType_Type()
)
mscMpanlDlciStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciStorageType.setStatus("mandatory")


class _MscMpanlDlciIndex_Type(Integer32):
    """Custom type mscMpanlDlciIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(17, 1007),
    )


_MscMpanlDlciIndex_Type.__name__ = "Integer32"
_MscMpanlDlciIndex_Object = MibTableColumn
mscMpanlDlciIndex = _MscMpanlDlciIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 1, 1, 10),
    _MscMpanlDlciIndex_Type()
)
mscMpanlDlciIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscMpanlDlciIndex.setStatus("mandatory")
_MscMpanlDlciLb_ObjectIdentity = ObjectIdentity
mscMpanlDlciLb = _MscMpanlDlciLb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 2)
)
_MscMpanlDlciLbRowStatusTable_Object = MibTable
mscMpanlDlciLbRowStatusTable = _MscMpanlDlciLbRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 2, 1)
)
if mibBuilder.loadTexts:
    mscMpanlDlciLbRowStatusTable.setStatus("mandatory")
_MscMpanlDlciLbRowStatusEntry_Object = MibTableRow
mscMpanlDlciLbRowStatusEntry = _MscMpanlDlciLbRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 2, 1, 1)
)
mscMpanlDlciLbRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-MpaNetworkLinkMIB", "mscMpanlIndex"),
    (0, "Nortel-MsCarrier-MscPassport-MpaNetworkLinkMIB", "mscMpanlDlciIndex"),
    (0, "Nortel-MsCarrier-MscPassport-MpaNetworkLinkMIB", "mscMpanlDlciLbIndex"),
)
if mibBuilder.loadTexts:
    mscMpanlDlciLbRowStatusEntry.setStatus("mandatory")
_MscMpanlDlciLbRowStatus_Type = RowStatus
_MscMpanlDlciLbRowStatus_Object = MibTableColumn
mscMpanlDlciLbRowStatus = _MscMpanlDlciLbRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 2, 1, 1, 1),
    _MscMpanlDlciLbRowStatus_Type()
)
mscMpanlDlciLbRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciLbRowStatus.setStatus("mandatory")
_MscMpanlDlciLbComponentName_Type = DisplayString
_MscMpanlDlciLbComponentName_Object = MibTableColumn
mscMpanlDlciLbComponentName = _MscMpanlDlciLbComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 2, 1, 1, 2),
    _MscMpanlDlciLbComponentName_Type()
)
mscMpanlDlciLbComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciLbComponentName.setStatus("mandatory")
_MscMpanlDlciLbStorageType_Type = StorageType
_MscMpanlDlciLbStorageType_Object = MibTableColumn
mscMpanlDlciLbStorageType = _MscMpanlDlciLbStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 2, 1, 1, 4),
    _MscMpanlDlciLbStorageType_Type()
)
mscMpanlDlciLbStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciLbStorageType.setStatus("mandatory")
_MscMpanlDlciLbIndex_Type = NonReplicated
_MscMpanlDlciLbIndex_Object = MibTableColumn
mscMpanlDlciLbIndex = _MscMpanlDlciLbIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 2, 1, 1, 10),
    _MscMpanlDlciLbIndex_Type()
)
mscMpanlDlciLbIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscMpanlDlciLbIndex.setStatus("mandatory")
_MscMpanlDlciLbStatsTable_Object = MibTable
mscMpanlDlciLbStatsTable = _MscMpanlDlciLbStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 2, 10)
)
if mibBuilder.loadTexts:
    mscMpanlDlciLbStatsTable.setStatus("mandatory")
_MscMpanlDlciLbStatsEntry_Object = MibTableRow
mscMpanlDlciLbStatsEntry = _MscMpanlDlciLbStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 2, 10, 1)
)
mscMpanlDlciLbStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-MpaNetworkLinkMIB", "mscMpanlIndex"),
    (0, "Nortel-MsCarrier-MscPassport-MpaNetworkLinkMIB", "mscMpanlDlciIndex"),
    (0, "Nortel-MsCarrier-MscPassport-MpaNetworkLinkMIB", "mscMpanlDlciLbIndex"),
)
if mibBuilder.loadTexts:
    mscMpanlDlciLbStatsEntry.setStatus("mandatory")


class _MscMpanlDlciLbLocalTotalFrm_Type(Unsigned32):
    """Custom type mscMpanlDlciLbLocalTotalFrm based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscMpanlDlciLbLocalTotalFrm_Type.__name__ = "Unsigned32"
_MscMpanlDlciLbLocalTotalFrm_Object = MibTableColumn
mscMpanlDlciLbLocalTotalFrm = _MscMpanlDlciLbLocalTotalFrm_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 2, 10, 1, 1),
    _MscMpanlDlciLbLocalTotalFrm_Type()
)
mscMpanlDlciLbLocalTotalFrm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciLbLocalTotalFrm.setStatus("mandatory")


class _MscMpanlDlciLbLocalTotalBytes_Type(Unsigned32):
    """Custom type mscMpanlDlciLbLocalTotalBytes based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscMpanlDlciLbLocalTotalBytes_Type.__name__ = "Unsigned32"
_MscMpanlDlciLbLocalTotalBytes_Object = MibTableColumn
mscMpanlDlciLbLocalTotalBytes = _MscMpanlDlciLbLocalTotalBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 2, 10, 1, 2),
    _MscMpanlDlciLbLocalTotalBytes_Type()
)
mscMpanlDlciLbLocalTotalBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciLbLocalTotalBytes.setStatus("mandatory")


class _MscMpanlDlciLbLocalFecnFrm_Type(Unsigned32):
    """Custom type mscMpanlDlciLbLocalFecnFrm based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscMpanlDlciLbLocalFecnFrm_Type.__name__ = "Unsigned32"
_MscMpanlDlciLbLocalFecnFrm_Object = MibTableColumn
mscMpanlDlciLbLocalFecnFrm = _MscMpanlDlciLbLocalFecnFrm_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 2, 10, 1, 3),
    _MscMpanlDlciLbLocalFecnFrm_Type()
)
mscMpanlDlciLbLocalFecnFrm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciLbLocalFecnFrm.setStatus("mandatory")


class _MscMpanlDlciLbLocalBecnFrm_Type(Unsigned32):
    """Custom type mscMpanlDlciLbLocalBecnFrm based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscMpanlDlciLbLocalBecnFrm_Type.__name__ = "Unsigned32"
_MscMpanlDlciLbLocalBecnFrm_Object = MibTableColumn
mscMpanlDlciLbLocalBecnFrm = _MscMpanlDlciLbLocalBecnFrm_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 2, 10, 1, 4),
    _MscMpanlDlciLbLocalBecnFrm_Type()
)
mscMpanlDlciLbLocalBecnFrm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciLbLocalBecnFrm.setStatus("mandatory")


class _MscMpanlDlciLbLocalDeFrm_Type(Unsigned32):
    """Custom type mscMpanlDlciLbLocalDeFrm based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscMpanlDlciLbLocalDeFrm_Type.__name__ = "Unsigned32"
_MscMpanlDlciLbLocalDeFrm_Object = MibTableColumn
mscMpanlDlciLbLocalDeFrm = _MscMpanlDlciLbLocalDeFrm_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 2, 10, 1, 5),
    _MscMpanlDlciLbLocalDeFrm_Type()
)
mscMpanlDlciLbLocalDeFrm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciLbLocalDeFrm.setStatus("mandatory")


class _MscMpanlDlciLbLocalDeBytes_Type(Unsigned32):
    """Custom type mscMpanlDlciLbLocalDeBytes based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscMpanlDlciLbLocalDeBytes_Type.__name__ = "Unsigned32"
_MscMpanlDlciLbLocalDeBytes_Object = MibTableColumn
mscMpanlDlciLbLocalDeBytes = _MscMpanlDlciLbLocalDeBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 2, 10, 1, 6),
    _MscMpanlDlciLbLocalDeBytes_Type()
)
mscMpanlDlciLbLocalDeBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciLbLocalDeBytes.setStatus("mandatory")


class _MscMpanlDlciLbRemoteTotalFrm_Type(Unsigned32):
    """Custom type mscMpanlDlciLbRemoteTotalFrm based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscMpanlDlciLbRemoteTotalFrm_Type.__name__ = "Unsigned32"
_MscMpanlDlciLbRemoteTotalFrm_Object = MibTableColumn
mscMpanlDlciLbRemoteTotalFrm = _MscMpanlDlciLbRemoteTotalFrm_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 2, 10, 1, 7),
    _MscMpanlDlciLbRemoteTotalFrm_Type()
)
mscMpanlDlciLbRemoteTotalFrm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciLbRemoteTotalFrm.setStatus("mandatory")


class _MscMpanlDlciLbRemoteTotalBytes_Type(Unsigned32):
    """Custom type mscMpanlDlciLbRemoteTotalBytes based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscMpanlDlciLbRemoteTotalBytes_Type.__name__ = "Unsigned32"
_MscMpanlDlciLbRemoteTotalBytes_Object = MibTableColumn
mscMpanlDlciLbRemoteTotalBytes = _MscMpanlDlciLbRemoteTotalBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 2, 10, 1, 8),
    _MscMpanlDlciLbRemoteTotalBytes_Type()
)
mscMpanlDlciLbRemoteTotalBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciLbRemoteTotalBytes.setStatus("mandatory")


class _MscMpanlDlciLbRemoteFecnFrm_Type(Unsigned32):
    """Custom type mscMpanlDlciLbRemoteFecnFrm based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscMpanlDlciLbRemoteFecnFrm_Type.__name__ = "Unsigned32"
_MscMpanlDlciLbRemoteFecnFrm_Object = MibTableColumn
mscMpanlDlciLbRemoteFecnFrm = _MscMpanlDlciLbRemoteFecnFrm_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 2, 10, 1, 9),
    _MscMpanlDlciLbRemoteFecnFrm_Type()
)
mscMpanlDlciLbRemoteFecnFrm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciLbRemoteFecnFrm.setStatus("mandatory")


class _MscMpanlDlciLbRemoteBecnFrm_Type(Unsigned32):
    """Custom type mscMpanlDlciLbRemoteBecnFrm based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscMpanlDlciLbRemoteBecnFrm_Type.__name__ = "Unsigned32"
_MscMpanlDlciLbRemoteBecnFrm_Object = MibTableColumn
mscMpanlDlciLbRemoteBecnFrm = _MscMpanlDlciLbRemoteBecnFrm_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 2, 10, 1, 10),
    _MscMpanlDlciLbRemoteBecnFrm_Type()
)
mscMpanlDlciLbRemoteBecnFrm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciLbRemoteBecnFrm.setStatus("mandatory")


class _MscMpanlDlciLbRemoteDeFrm_Type(Unsigned32):
    """Custom type mscMpanlDlciLbRemoteDeFrm based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscMpanlDlciLbRemoteDeFrm_Type.__name__ = "Unsigned32"
_MscMpanlDlciLbRemoteDeFrm_Object = MibTableColumn
mscMpanlDlciLbRemoteDeFrm = _MscMpanlDlciLbRemoteDeFrm_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 2, 10, 1, 13),
    _MscMpanlDlciLbRemoteDeFrm_Type()
)
mscMpanlDlciLbRemoteDeFrm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciLbRemoteDeFrm.setStatus("mandatory")


class _MscMpanlDlciLbRemoteDeBytes_Type(Unsigned32):
    """Custom type mscMpanlDlciLbRemoteDeBytes based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscMpanlDlciLbRemoteDeBytes_Type.__name__ = "Unsigned32"
_MscMpanlDlciLbRemoteDeBytes_Object = MibTableColumn
mscMpanlDlciLbRemoteDeBytes = _MscMpanlDlciLbRemoteDeBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 2, 10, 1, 14),
    _MscMpanlDlciLbRemoteDeBytes_Type()
)
mscMpanlDlciLbRemoteDeBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciLbRemoteDeBytes.setStatus("mandatory")
_MscMpanlDlciVc_ObjectIdentity = ObjectIdentity
mscMpanlDlciVc = _MscMpanlDlciVc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 3)
)
_MscMpanlDlciVcRowStatusTable_Object = MibTable
mscMpanlDlciVcRowStatusTable = _MscMpanlDlciVcRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 3, 1)
)
if mibBuilder.loadTexts:
    mscMpanlDlciVcRowStatusTable.setStatus("mandatory")
_MscMpanlDlciVcRowStatusEntry_Object = MibTableRow
mscMpanlDlciVcRowStatusEntry = _MscMpanlDlciVcRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 3, 1, 1)
)
mscMpanlDlciVcRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-MpaNetworkLinkMIB", "mscMpanlIndex"),
    (0, "Nortel-MsCarrier-MscPassport-MpaNetworkLinkMIB", "mscMpanlDlciIndex"),
    (0, "Nortel-MsCarrier-MscPassport-MpaNetworkLinkMIB", "mscMpanlDlciVcIndex"),
)
if mibBuilder.loadTexts:
    mscMpanlDlciVcRowStatusEntry.setStatus("mandatory")
_MscMpanlDlciVcRowStatus_Type = RowStatus
_MscMpanlDlciVcRowStatus_Object = MibTableColumn
mscMpanlDlciVcRowStatus = _MscMpanlDlciVcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 3, 1, 1, 1),
    _MscMpanlDlciVcRowStatus_Type()
)
mscMpanlDlciVcRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciVcRowStatus.setStatus("mandatory")
_MscMpanlDlciVcComponentName_Type = DisplayString
_MscMpanlDlciVcComponentName_Object = MibTableColumn
mscMpanlDlciVcComponentName = _MscMpanlDlciVcComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 3, 1, 1, 2),
    _MscMpanlDlciVcComponentName_Type()
)
mscMpanlDlciVcComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciVcComponentName.setStatus("mandatory")
_MscMpanlDlciVcStorageType_Type = StorageType
_MscMpanlDlciVcStorageType_Object = MibTableColumn
mscMpanlDlciVcStorageType = _MscMpanlDlciVcStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 3, 1, 1, 4),
    _MscMpanlDlciVcStorageType_Type()
)
mscMpanlDlciVcStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciVcStorageType.setStatus("mandatory")
_MscMpanlDlciVcIndex_Type = NonReplicated
_MscMpanlDlciVcIndex_Object = MibTableColumn
mscMpanlDlciVcIndex = _MscMpanlDlciVcIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 3, 1, 1, 10),
    _MscMpanlDlciVcIndex_Type()
)
mscMpanlDlciVcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscMpanlDlciVcIndex.setStatus("mandatory")
_MscMpanlDlciVcCadTable_Object = MibTable
mscMpanlDlciVcCadTable = _MscMpanlDlciVcCadTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 3, 10)
)
if mibBuilder.loadTexts:
    mscMpanlDlciVcCadTable.setStatus("mandatory")
_MscMpanlDlciVcCadEntry_Object = MibTableRow
mscMpanlDlciVcCadEntry = _MscMpanlDlciVcCadEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 3, 10, 1)
)
mscMpanlDlciVcCadEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-MpaNetworkLinkMIB", "mscMpanlIndex"),
    (0, "Nortel-MsCarrier-MscPassport-MpaNetworkLinkMIB", "mscMpanlDlciIndex"),
    (0, "Nortel-MsCarrier-MscPassport-MpaNetworkLinkMIB", "mscMpanlDlciVcIndex"),
)
if mibBuilder.loadTexts:
    mscMpanlDlciVcCadEntry.setStatus("mandatory")


class _MscMpanlDlciVcType_Type(Integer32):
    """Custom type mscMpanlDlciVcType based on Integer32"""
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
        *(("frf10spvc", 3),
          ("pvc", 1),
          ("spvc", 2),
          ("svc", 0))
    )


_MscMpanlDlciVcType_Type.__name__ = "Integer32"
_MscMpanlDlciVcType_Object = MibTableColumn
mscMpanlDlciVcType = _MscMpanlDlciVcType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 3, 10, 1, 1),
    _MscMpanlDlciVcType_Type()
)
mscMpanlDlciVcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciVcType.setStatus("mandatory")


class _MscMpanlDlciVcState_Type(Integer32):
    """Custom type mscMpanlDlciVcState based on Integer32"""
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


_MscMpanlDlciVcState_Type.__name__ = "Integer32"
_MscMpanlDlciVcState_Object = MibTableColumn
mscMpanlDlciVcState = _MscMpanlDlciVcState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 3, 10, 1, 2),
    _MscMpanlDlciVcState_Type()
)
mscMpanlDlciVcState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciVcState.setStatus("mandatory")


class _MscMpanlDlciVcPreviousState_Type(Integer32):
    """Custom type mscMpanlDlciVcPreviousState based on Integer32"""
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


_MscMpanlDlciVcPreviousState_Type.__name__ = "Integer32"
_MscMpanlDlciVcPreviousState_Object = MibTableColumn
mscMpanlDlciVcPreviousState = _MscMpanlDlciVcPreviousState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 3, 10, 1, 3),
    _MscMpanlDlciVcPreviousState_Type()
)
mscMpanlDlciVcPreviousState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciVcPreviousState.setStatus("mandatory")


class _MscMpanlDlciVcDiagnosticCode_Type(Unsigned32):
    """Custom type mscMpanlDlciVcDiagnosticCode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscMpanlDlciVcDiagnosticCode_Type.__name__ = "Unsigned32"
_MscMpanlDlciVcDiagnosticCode_Object = MibTableColumn
mscMpanlDlciVcDiagnosticCode = _MscMpanlDlciVcDiagnosticCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 3, 10, 1, 4),
    _MscMpanlDlciVcDiagnosticCode_Type()
)
mscMpanlDlciVcDiagnosticCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciVcDiagnosticCode.setStatus("mandatory")


class _MscMpanlDlciVcPreviousDiagnosticCode_Type(Unsigned32):
    """Custom type mscMpanlDlciVcPreviousDiagnosticCode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscMpanlDlciVcPreviousDiagnosticCode_Type.__name__ = "Unsigned32"
_MscMpanlDlciVcPreviousDiagnosticCode_Object = MibTableColumn
mscMpanlDlciVcPreviousDiagnosticCode = _MscMpanlDlciVcPreviousDiagnosticCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 3, 10, 1, 5),
    _MscMpanlDlciVcPreviousDiagnosticCode_Type()
)
mscMpanlDlciVcPreviousDiagnosticCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciVcPreviousDiagnosticCode.setStatus("mandatory")


class _MscMpanlDlciVcCalledNpi_Type(Integer32):
    """Custom type mscMpanlDlciVcCalledNpi based on Integer32"""
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


_MscMpanlDlciVcCalledNpi_Type.__name__ = "Integer32"
_MscMpanlDlciVcCalledNpi_Object = MibTableColumn
mscMpanlDlciVcCalledNpi = _MscMpanlDlciVcCalledNpi_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 3, 10, 1, 6),
    _MscMpanlDlciVcCalledNpi_Type()
)
mscMpanlDlciVcCalledNpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciVcCalledNpi.setStatus("mandatory")


class _MscMpanlDlciVcCalledDna_Type(DigitString):
    """Custom type mscMpanlDlciVcCalledDna based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_MscMpanlDlciVcCalledDna_Type.__name__ = "DigitString"
_MscMpanlDlciVcCalledDna_Object = MibTableColumn
mscMpanlDlciVcCalledDna = _MscMpanlDlciVcCalledDna_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 3, 10, 1, 7),
    _MscMpanlDlciVcCalledDna_Type()
)
mscMpanlDlciVcCalledDna.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciVcCalledDna.setStatus("mandatory")


class _MscMpanlDlciVcCalledLcn_Type(Unsigned32):
    """Custom type mscMpanlDlciVcCalledLcn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MscMpanlDlciVcCalledLcn_Type.__name__ = "Unsigned32"
_MscMpanlDlciVcCalledLcn_Object = MibTableColumn
mscMpanlDlciVcCalledLcn = _MscMpanlDlciVcCalledLcn_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 3, 10, 1, 8),
    _MscMpanlDlciVcCalledLcn_Type()
)
mscMpanlDlciVcCalledLcn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciVcCalledLcn.setStatus("mandatory")


class _MscMpanlDlciVcCallingNpi_Type(Integer32):
    """Custom type mscMpanlDlciVcCallingNpi based on Integer32"""
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


_MscMpanlDlciVcCallingNpi_Type.__name__ = "Integer32"
_MscMpanlDlciVcCallingNpi_Object = MibTableColumn
mscMpanlDlciVcCallingNpi = _MscMpanlDlciVcCallingNpi_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 3, 10, 1, 9),
    _MscMpanlDlciVcCallingNpi_Type()
)
mscMpanlDlciVcCallingNpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciVcCallingNpi.setStatus("mandatory")


class _MscMpanlDlciVcCallingDna_Type(DigitString):
    """Custom type mscMpanlDlciVcCallingDna based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_MscMpanlDlciVcCallingDna_Type.__name__ = "DigitString"
_MscMpanlDlciVcCallingDna_Object = MibTableColumn
mscMpanlDlciVcCallingDna = _MscMpanlDlciVcCallingDna_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 3, 10, 1, 10),
    _MscMpanlDlciVcCallingDna_Type()
)
mscMpanlDlciVcCallingDna.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciVcCallingDna.setStatus("mandatory")


class _MscMpanlDlciVcCallingLcn_Type(Unsigned32):
    """Custom type mscMpanlDlciVcCallingLcn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MscMpanlDlciVcCallingLcn_Type.__name__ = "Unsigned32"
_MscMpanlDlciVcCallingLcn_Object = MibTableColumn
mscMpanlDlciVcCallingLcn = _MscMpanlDlciVcCallingLcn_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 3, 10, 1, 11),
    _MscMpanlDlciVcCallingLcn_Type()
)
mscMpanlDlciVcCallingLcn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciVcCallingLcn.setStatus("mandatory")


class _MscMpanlDlciVcAccountingEnabled_Type(Integer32):
    """Custom type mscMpanlDlciVcAccountingEnabled based on Integer32"""
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


_MscMpanlDlciVcAccountingEnabled_Type.__name__ = "Integer32"
_MscMpanlDlciVcAccountingEnabled_Object = MibTableColumn
mscMpanlDlciVcAccountingEnabled = _MscMpanlDlciVcAccountingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 3, 10, 1, 12),
    _MscMpanlDlciVcAccountingEnabled_Type()
)
mscMpanlDlciVcAccountingEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciVcAccountingEnabled.setStatus("mandatory")


class _MscMpanlDlciVcFastSelectCall_Type(Integer32):
    """Custom type mscMpanlDlciVcFastSelectCall based on Integer32"""
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


_MscMpanlDlciVcFastSelectCall_Type.__name__ = "Integer32"
_MscMpanlDlciVcFastSelectCall_Object = MibTableColumn
mscMpanlDlciVcFastSelectCall = _MscMpanlDlciVcFastSelectCall_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 3, 10, 1, 13),
    _MscMpanlDlciVcFastSelectCall_Type()
)
mscMpanlDlciVcFastSelectCall.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciVcFastSelectCall.setStatus("mandatory")


class _MscMpanlDlciVcPathReliability_Type(Integer32):
    """Custom type mscMpanlDlciVcPathReliability based on Integer32"""
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


_MscMpanlDlciVcPathReliability_Type.__name__ = "Integer32"
_MscMpanlDlciVcPathReliability_Object = MibTableColumn
mscMpanlDlciVcPathReliability = _MscMpanlDlciVcPathReliability_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 3, 10, 1, 19),
    _MscMpanlDlciVcPathReliability_Type()
)
mscMpanlDlciVcPathReliability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciVcPathReliability.setStatus("mandatory")


class _MscMpanlDlciVcAccountingEnd_Type(Integer32):
    """Custom type mscMpanlDlciVcAccountingEnd based on Integer32"""
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


_MscMpanlDlciVcAccountingEnd_Type.__name__ = "Integer32"
_MscMpanlDlciVcAccountingEnd_Object = MibTableColumn
mscMpanlDlciVcAccountingEnd = _MscMpanlDlciVcAccountingEnd_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 3, 10, 1, 20),
    _MscMpanlDlciVcAccountingEnd_Type()
)
mscMpanlDlciVcAccountingEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciVcAccountingEnd.setStatus("mandatory")


class _MscMpanlDlciVcPriority_Type(Integer32):
    """Custom type mscMpanlDlciVcPriority based on Integer32"""
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


_MscMpanlDlciVcPriority_Type.__name__ = "Integer32"
_MscMpanlDlciVcPriority_Object = MibTableColumn
mscMpanlDlciVcPriority = _MscMpanlDlciVcPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 3, 10, 1, 21),
    _MscMpanlDlciVcPriority_Type()
)
mscMpanlDlciVcPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciVcPriority.setStatus("mandatory")


class _MscMpanlDlciVcSegmentSize_Type(Unsigned32):
    """Custom type mscMpanlDlciVcSegmentSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_MscMpanlDlciVcSegmentSize_Type.__name__ = "Unsigned32"
_MscMpanlDlciVcSegmentSize_Object = MibTableColumn
mscMpanlDlciVcSegmentSize = _MscMpanlDlciVcSegmentSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 3, 10, 1, 22),
    _MscMpanlDlciVcSegmentSize_Type()
)
mscMpanlDlciVcSegmentSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciVcSegmentSize.setStatus("mandatory")


class _MscMpanlDlciVcMaxSubnetPktSize_Type(Unsigned32):
    """Custom type mscMpanlDlciVcMaxSubnetPktSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_MscMpanlDlciVcMaxSubnetPktSize_Type.__name__ = "Unsigned32"
_MscMpanlDlciVcMaxSubnetPktSize_Object = MibTableColumn
mscMpanlDlciVcMaxSubnetPktSize = _MscMpanlDlciVcMaxSubnetPktSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 3, 10, 1, 27),
    _MscMpanlDlciVcMaxSubnetPktSize_Type()
)
mscMpanlDlciVcMaxSubnetPktSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciVcMaxSubnetPktSize.setStatus("mandatory")


class _MscMpanlDlciVcRcosToNetwork_Type(Integer32):
    """Custom type mscMpanlDlciVcRcosToNetwork based on Integer32"""
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


_MscMpanlDlciVcRcosToNetwork_Type.__name__ = "Integer32"
_MscMpanlDlciVcRcosToNetwork_Object = MibTableColumn
mscMpanlDlciVcRcosToNetwork = _MscMpanlDlciVcRcosToNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 3, 10, 1, 28),
    _MscMpanlDlciVcRcosToNetwork_Type()
)
mscMpanlDlciVcRcosToNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciVcRcosToNetwork.setStatus("mandatory")


class _MscMpanlDlciVcRcosFromNetwork_Type(Integer32):
    """Custom type mscMpanlDlciVcRcosFromNetwork based on Integer32"""
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


_MscMpanlDlciVcRcosFromNetwork_Type.__name__ = "Integer32"
_MscMpanlDlciVcRcosFromNetwork_Object = MibTableColumn
mscMpanlDlciVcRcosFromNetwork = _MscMpanlDlciVcRcosFromNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 3, 10, 1, 29),
    _MscMpanlDlciVcRcosFromNetwork_Type()
)
mscMpanlDlciVcRcosFromNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciVcRcosFromNetwork.setStatus("mandatory")


class _MscMpanlDlciVcEmissionPriorityToNetwork_Type(Integer32):
    """Custom type mscMpanlDlciVcEmissionPriorityToNetwork based on Integer32"""
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


_MscMpanlDlciVcEmissionPriorityToNetwork_Type.__name__ = "Integer32"
_MscMpanlDlciVcEmissionPriorityToNetwork_Object = MibTableColumn
mscMpanlDlciVcEmissionPriorityToNetwork = _MscMpanlDlciVcEmissionPriorityToNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 3, 10, 1, 30),
    _MscMpanlDlciVcEmissionPriorityToNetwork_Type()
)
mscMpanlDlciVcEmissionPriorityToNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciVcEmissionPriorityToNetwork.setStatus("mandatory")


class _MscMpanlDlciVcEmissionPriorityFromNetwork_Type(Integer32):
    """Custom type mscMpanlDlciVcEmissionPriorityFromNetwork based on Integer32"""
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


_MscMpanlDlciVcEmissionPriorityFromNetwork_Type.__name__ = "Integer32"
_MscMpanlDlciVcEmissionPriorityFromNetwork_Object = MibTableColumn
mscMpanlDlciVcEmissionPriorityFromNetwork = _MscMpanlDlciVcEmissionPriorityFromNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 3, 10, 1, 31),
    _MscMpanlDlciVcEmissionPriorityFromNetwork_Type()
)
mscMpanlDlciVcEmissionPriorityFromNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciVcEmissionPriorityFromNetwork.setStatus("mandatory")


class _MscMpanlDlciVcDataPath_Type(AsciiString):
    """Custom type mscMpanlDlciVcDataPath based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MscMpanlDlciVcDataPath_Type.__name__ = "AsciiString"
_MscMpanlDlciVcDataPath_Object = MibTableColumn
mscMpanlDlciVcDataPath = _MscMpanlDlciVcDataPath_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 3, 10, 1, 32),
    _MscMpanlDlciVcDataPath_Type()
)
mscMpanlDlciVcDataPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciVcDataPath.setStatus("mandatory")
_MscMpanlDlciVcIntdTable_Object = MibTable
mscMpanlDlciVcIntdTable = _MscMpanlDlciVcIntdTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 3, 11)
)
if mibBuilder.loadTexts:
    mscMpanlDlciVcIntdTable.setStatus("mandatory")
_MscMpanlDlciVcIntdEntry_Object = MibTableRow
mscMpanlDlciVcIntdEntry = _MscMpanlDlciVcIntdEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 3, 11, 1)
)
mscMpanlDlciVcIntdEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-MpaNetworkLinkMIB", "mscMpanlIndex"),
    (0, "Nortel-MsCarrier-MscPassport-MpaNetworkLinkMIB", "mscMpanlDlciIndex"),
    (0, "Nortel-MsCarrier-MscPassport-MpaNetworkLinkMIB", "mscMpanlDlciVcIndex"),
)
if mibBuilder.loadTexts:
    mscMpanlDlciVcIntdEntry.setStatus("mandatory")


class _MscMpanlDlciVcCallReferenceNumber_Type(Hex):
    """Custom type mscMpanlDlciVcCallReferenceNumber based on Hex"""
    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_MscMpanlDlciVcCallReferenceNumber_Type.__name__ = "Hex"
_MscMpanlDlciVcCallReferenceNumber_Object = MibTableColumn
mscMpanlDlciVcCallReferenceNumber = _MscMpanlDlciVcCallReferenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 3, 11, 1, 1),
    _MscMpanlDlciVcCallReferenceNumber_Type()
)
mscMpanlDlciVcCallReferenceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciVcCallReferenceNumber.setStatus("obsolete")


class _MscMpanlDlciVcElapsedTimeTillNow_Type(Unsigned32):
    """Custom type mscMpanlDlciVcElapsedTimeTillNow based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_MscMpanlDlciVcElapsedTimeTillNow_Type.__name__ = "Unsigned32"
_MscMpanlDlciVcElapsedTimeTillNow_Object = MibTableColumn
mscMpanlDlciVcElapsedTimeTillNow = _MscMpanlDlciVcElapsedTimeTillNow_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 3, 11, 1, 2),
    _MscMpanlDlciVcElapsedTimeTillNow_Type()
)
mscMpanlDlciVcElapsedTimeTillNow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciVcElapsedTimeTillNow.setStatus("mandatory")


class _MscMpanlDlciVcSegmentsRx_Type(Unsigned32):
    """Custom type mscMpanlDlciVcSegmentsRx based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_MscMpanlDlciVcSegmentsRx_Type.__name__ = "Unsigned32"
_MscMpanlDlciVcSegmentsRx_Object = MibTableColumn
mscMpanlDlciVcSegmentsRx = _MscMpanlDlciVcSegmentsRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 3, 11, 1, 3),
    _MscMpanlDlciVcSegmentsRx_Type()
)
mscMpanlDlciVcSegmentsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciVcSegmentsRx.setStatus("mandatory")


class _MscMpanlDlciVcSegmentsSent_Type(Unsigned32):
    """Custom type mscMpanlDlciVcSegmentsSent based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_MscMpanlDlciVcSegmentsSent_Type.__name__ = "Unsigned32"
_MscMpanlDlciVcSegmentsSent_Object = MibTableColumn
mscMpanlDlciVcSegmentsSent = _MscMpanlDlciVcSegmentsSent_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 3, 11, 1, 4),
    _MscMpanlDlciVcSegmentsSent_Type()
)
mscMpanlDlciVcSegmentsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciVcSegmentsSent.setStatus("mandatory")


class _MscMpanlDlciVcStartTime_Type(EnterpriseDateAndTime):
    """Custom type mscMpanlDlciVcStartTime based on EnterpriseDateAndTime"""
    subtypeSpec = EnterpriseDateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(19, 19),
    )


_MscMpanlDlciVcStartTime_Type.__name__ = "EnterpriseDateAndTime"
_MscMpanlDlciVcStartTime_Object = MibTableColumn
mscMpanlDlciVcStartTime = _MscMpanlDlciVcStartTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 3, 11, 1, 5),
    _MscMpanlDlciVcStartTime_Type()
)
mscMpanlDlciVcStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciVcStartTime.setStatus("mandatory")


class _MscMpanlDlciVcCallReferenceNumberDecimal_Type(Unsigned32):
    """Custom type mscMpanlDlciVcCallReferenceNumberDecimal based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscMpanlDlciVcCallReferenceNumberDecimal_Type.__name__ = "Unsigned32"
_MscMpanlDlciVcCallReferenceNumberDecimal_Object = MibTableColumn
mscMpanlDlciVcCallReferenceNumberDecimal = _MscMpanlDlciVcCallReferenceNumberDecimal_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 3, 11, 1, 7),
    _MscMpanlDlciVcCallReferenceNumberDecimal_Type()
)
mscMpanlDlciVcCallReferenceNumberDecimal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciVcCallReferenceNumberDecimal.setStatus("mandatory")
_MscMpanlDlciVcFrdTable_Object = MibTable
mscMpanlDlciVcFrdTable = _MscMpanlDlciVcFrdTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 3, 12)
)
if mibBuilder.loadTexts:
    mscMpanlDlciVcFrdTable.setStatus("mandatory")
_MscMpanlDlciVcFrdEntry_Object = MibTableRow
mscMpanlDlciVcFrdEntry = _MscMpanlDlciVcFrdEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 3, 12, 1)
)
mscMpanlDlciVcFrdEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-MpaNetworkLinkMIB", "mscMpanlIndex"),
    (0, "Nortel-MsCarrier-MscPassport-MpaNetworkLinkMIB", "mscMpanlDlciIndex"),
    (0, "Nortel-MsCarrier-MscPassport-MpaNetworkLinkMIB", "mscMpanlDlciVcIndex"),
)
if mibBuilder.loadTexts:
    mscMpanlDlciVcFrdEntry.setStatus("mandatory")


class _MscMpanlDlciVcFrmCongestedToSubnet_Type(Unsigned32):
    """Custom type mscMpanlDlciVcFrmCongestedToSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscMpanlDlciVcFrmCongestedToSubnet_Type.__name__ = "Unsigned32"
_MscMpanlDlciVcFrmCongestedToSubnet_Object = MibTableColumn
mscMpanlDlciVcFrmCongestedToSubnet = _MscMpanlDlciVcFrmCongestedToSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 3, 12, 1, 2),
    _MscMpanlDlciVcFrmCongestedToSubnet_Type()
)
mscMpanlDlciVcFrmCongestedToSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciVcFrmCongestedToSubnet.setStatus("mandatory")


class _MscMpanlDlciVcCannotForwardToSubnet_Type(Unsigned32):
    """Custom type mscMpanlDlciVcCannotForwardToSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscMpanlDlciVcCannotForwardToSubnet_Type.__name__ = "Unsigned32"
_MscMpanlDlciVcCannotForwardToSubnet_Object = MibTableColumn
mscMpanlDlciVcCannotForwardToSubnet = _MscMpanlDlciVcCannotForwardToSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 3, 12, 1, 3),
    _MscMpanlDlciVcCannotForwardToSubnet_Type()
)
mscMpanlDlciVcCannotForwardToSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciVcCannotForwardToSubnet.setStatus("mandatory")


class _MscMpanlDlciVcNotDataXferToSubnet_Type(Unsigned32):
    """Custom type mscMpanlDlciVcNotDataXferToSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscMpanlDlciVcNotDataXferToSubnet_Type.__name__ = "Unsigned32"
_MscMpanlDlciVcNotDataXferToSubnet_Object = MibTableColumn
mscMpanlDlciVcNotDataXferToSubnet = _MscMpanlDlciVcNotDataXferToSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 3, 12, 1, 4),
    _MscMpanlDlciVcNotDataXferToSubnet_Type()
)
mscMpanlDlciVcNotDataXferToSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciVcNotDataXferToSubnet.setStatus("mandatory")


class _MscMpanlDlciVcOutOfRangeFrmFromSubnet_Type(Unsigned32):
    """Custom type mscMpanlDlciVcOutOfRangeFrmFromSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscMpanlDlciVcOutOfRangeFrmFromSubnet_Type.__name__ = "Unsigned32"
_MscMpanlDlciVcOutOfRangeFrmFromSubnet_Object = MibTableColumn
mscMpanlDlciVcOutOfRangeFrmFromSubnet = _MscMpanlDlciVcOutOfRangeFrmFromSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 3, 12, 1, 5),
    _MscMpanlDlciVcOutOfRangeFrmFromSubnet_Type()
)
mscMpanlDlciVcOutOfRangeFrmFromSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciVcOutOfRangeFrmFromSubnet.setStatus("mandatory")


class _MscMpanlDlciVcCombErrorsFromSubnet_Type(Unsigned32):
    """Custom type mscMpanlDlciVcCombErrorsFromSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscMpanlDlciVcCombErrorsFromSubnet_Type.__name__ = "Unsigned32"
_MscMpanlDlciVcCombErrorsFromSubnet_Object = MibTableColumn
mscMpanlDlciVcCombErrorsFromSubnet = _MscMpanlDlciVcCombErrorsFromSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 3, 12, 1, 6),
    _MscMpanlDlciVcCombErrorsFromSubnet_Type()
)
mscMpanlDlciVcCombErrorsFromSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciVcCombErrorsFromSubnet.setStatus("mandatory")


class _MscMpanlDlciVcDuplicatesFromSubnet_Type(Unsigned32):
    """Custom type mscMpanlDlciVcDuplicatesFromSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscMpanlDlciVcDuplicatesFromSubnet_Type.__name__ = "Unsigned32"
_MscMpanlDlciVcDuplicatesFromSubnet_Object = MibTableColumn
mscMpanlDlciVcDuplicatesFromSubnet = _MscMpanlDlciVcDuplicatesFromSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 3, 12, 1, 7),
    _MscMpanlDlciVcDuplicatesFromSubnet_Type()
)
mscMpanlDlciVcDuplicatesFromSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciVcDuplicatesFromSubnet.setStatus("mandatory")


class _MscMpanlDlciVcNotDataXferFromSubnet_Type(Unsigned32):
    """Custom type mscMpanlDlciVcNotDataXferFromSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscMpanlDlciVcNotDataXferFromSubnet_Type.__name__ = "Unsigned32"
_MscMpanlDlciVcNotDataXferFromSubnet_Object = MibTableColumn
mscMpanlDlciVcNotDataXferFromSubnet = _MscMpanlDlciVcNotDataXferFromSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 3, 12, 1, 8),
    _MscMpanlDlciVcNotDataXferFromSubnet_Type()
)
mscMpanlDlciVcNotDataXferFromSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciVcNotDataXferFromSubnet.setStatus("mandatory")


class _MscMpanlDlciVcFrmLossTimeouts_Type(Unsigned32):
    """Custom type mscMpanlDlciVcFrmLossTimeouts based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscMpanlDlciVcFrmLossTimeouts_Type.__name__ = "Unsigned32"
_MscMpanlDlciVcFrmLossTimeouts_Object = MibTableColumn
mscMpanlDlciVcFrmLossTimeouts = _MscMpanlDlciVcFrmLossTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 3, 12, 1, 9),
    _MscMpanlDlciVcFrmLossTimeouts_Type()
)
mscMpanlDlciVcFrmLossTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciVcFrmLossTimeouts.setStatus("mandatory")


class _MscMpanlDlciVcOoSeqByteCntExceeded_Type(Unsigned32):
    """Custom type mscMpanlDlciVcOoSeqByteCntExceeded based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscMpanlDlciVcOoSeqByteCntExceeded_Type.__name__ = "Unsigned32"
_MscMpanlDlciVcOoSeqByteCntExceeded_Object = MibTableColumn
mscMpanlDlciVcOoSeqByteCntExceeded = _MscMpanlDlciVcOoSeqByteCntExceeded_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 3, 12, 1, 10),
    _MscMpanlDlciVcOoSeqByteCntExceeded_Type()
)
mscMpanlDlciVcOoSeqByteCntExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciVcOoSeqByteCntExceeded.setStatus("mandatory")


class _MscMpanlDlciVcPeakOoSeqPktCount_Type(Unsigned32):
    """Custom type mscMpanlDlciVcPeakOoSeqPktCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscMpanlDlciVcPeakOoSeqPktCount_Type.__name__ = "Unsigned32"
_MscMpanlDlciVcPeakOoSeqPktCount_Object = MibTableColumn
mscMpanlDlciVcPeakOoSeqPktCount = _MscMpanlDlciVcPeakOoSeqPktCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 3, 12, 1, 11),
    _MscMpanlDlciVcPeakOoSeqPktCount_Type()
)
mscMpanlDlciVcPeakOoSeqPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciVcPeakOoSeqPktCount.setStatus("mandatory")


class _MscMpanlDlciVcPeakOoSeqFrmForwarded_Type(Unsigned32):
    """Custom type mscMpanlDlciVcPeakOoSeqFrmForwarded based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscMpanlDlciVcPeakOoSeqFrmForwarded_Type.__name__ = "Unsigned32"
_MscMpanlDlciVcPeakOoSeqFrmForwarded_Object = MibTableColumn
mscMpanlDlciVcPeakOoSeqFrmForwarded = _MscMpanlDlciVcPeakOoSeqFrmForwarded_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 3, 12, 1, 12),
    _MscMpanlDlciVcPeakOoSeqFrmForwarded_Type()
)
mscMpanlDlciVcPeakOoSeqFrmForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciVcPeakOoSeqFrmForwarded.setStatus("mandatory")


class _MscMpanlDlciVcSendSequenceNumber_Type(Unsigned32):
    """Custom type mscMpanlDlciVcSendSequenceNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscMpanlDlciVcSendSequenceNumber_Type.__name__ = "Unsigned32"
_MscMpanlDlciVcSendSequenceNumber_Object = MibTableColumn
mscMpanlDlciVcSendSequenceNumber = _MscMpanlDlciVcSendSequenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 3, 12, 1, 13),
    _MscMpanlDlciVcSendSequenceNumber_Type()
)
mscMpanlDlciVcSendSequenceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciVcSendSequenceNumber.setStatus("mandatory")


class _MscMpanlDlciVcPktRetryTimeouts_Type(Unsigned32):
    """Custom type mscMpanlDlciVcPktRetryTimeouts based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscMpanlDlciVcPktRetryTimeouts_Type.__name__ = "Unsigned32"
_MscMpanlDlciVcPktRetryTimeouts_Object = MibTableColumn
mscMpanlDlciVcPktRetryTimeouts = _MscMpanlDlciVcPktRetryTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 3, 12, 1, 15),
    _MscMpanlDlciVcPktRetryTimeouts_Type()
)
mscMpanlDlciVcPktRetryTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciVcPktRetryTimeouts.setStatus("mandatory")


class _MscMpanlDlciVcPeakRetryQueueSize_Type(Unsigned32):
    """Custom type mscMpanlDlciVcPeakRetryQueueSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscMpanlDlciVcPeakRetryQueueSize_Type.__name__ = "Unsigned32"
_MscMpanlDlciVcPeakRetryQueueSize_Object = MibTableColumn
mscMpanlDlciVcPeakRetryQueueSize = _MscMpanlDlciVcPeakRetryQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 3, 12, 1, 16),
    _MscMpanlDlciVcPeakRetryQueueSize_Type()
)
mscMpanlDlciVcPeakRetryQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciVcPeakRetryQueueSize.setStatus("mandatory")


class _MscMpanlDlciVcSubnetRecoveries_Type(Unsigned32):
    """Custom type mscMpanlDlciVcSubnetRecoveries based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscMpanlDlciVcSubnetRecoveries_Type.__name__ = "Unsigned32"
_MscMpanlDlciVcSubnetRecoveries_Object = MibTableColumn
mscMpanlDlciVcSubnetRecoveries = _MscMpanlDlciVcSubnetRecoveries_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 3, 12, 1, 17),
    _MscMpanlDlciVcSubnetRecoveries_Type()
)
mscMpanlDlciVcSubnetRecoveries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciVcSubnetRecoveries.setStatus("mandatory")


class _MscMpanlDlciVcOoSeqPktCntExceeded_Type(Unsigned32):
    """Custom type mscMpanlDlciVcOoSeqPktCntExceeded based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscMpanlDlciVcOoSeqPktCntExceeded_Type.__name__ = "Unsigned32"
_MscMpanlDlciVcOoSeqPktCntExceeded_Object = MibTableColumn
mscMpanlDlciVcOoSeqPktCntExceeded = _MscMpanlDlciVcOoSeqPktCntExceeded_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 3, 12, 1, 19),
    _MscMpanlDlciVcOoSeqPktCntExceeded_Type()
)
mscMpanlDlciVcOoSeqPktCntExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciVcOoSeqPktCntExceeded.setStatus("mandatory")


class _MscMpanlDlciVcPeakOoSeqByteCount_Type(Unsigned32):
    """Custom type mscMpanlDlciVcPeakOoSeqByteCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50000),
    )


_MscMpanlDlciVcPeakOoSeqByteCount_Type.__name__ = "Unsigned32"
_MscMpanlDlciVcPeakOoSeqByteCount_Object = MibTableColumn
mscMpanlDlciVcPeakOoSeqByteCount = _MscMpanlDlciVcPeakOoSeqByteCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 3, 12, 1, 20),
    _MscMpanlDlciVcPeakOoSeqByteCount_Type()
)
mscMpanlDlciVcPeakOoSeqByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciVcPeakOoSeqByteCount.setStatus("mandatory")
_MscMpanlDlciVcDmepTable_Object = MibTable
mscMpanlDlciVcDmepTable = _MscMpanlDlciVcDmepTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 3, 417)
)
if mibBuilder.loadTexts:
    mscMpanlDlciVcDmepTable.setStatus("mandatory")
_MscMpanlDlciVcDmepEntry_Object = MibTableRow
mscMpanlDlciVcDmepEntry = _MscMpanlDlciVcDmepEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 3, 417, 1)
)
mscMpanlDlciVcDmepEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-MpaNetworkLinkMIB", "mscMpanlIndex"),
    (0, "Nortel-MsCarrier-MscPassport-MpaNetworkLinkMIB", "mscMpanlDlciIndex"),
    (0, "Nortel-MsCarrier-MscPassport-MpaNetworkLinkMIB", "mscMpanlDlciVcIndex"),
    (0, "Nortel-MsCarrier-MscPassport-MpaNetworkLinkMIB", "mscMpanlDlciVcDmepValue"),
)
if mibBuilder.loadTexts:
    mscMpanlDlciVcDmepEntry.setStatus("mandatory")
_MscMpanlDlciVcDmepValue_Type = RowPointer
_MscMpanlDlciVcDmepValue_Object = MibTableColumn
mscMpanlDlciVcDmepValue = _MscMpanlDlciVcDmepValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 3, 417, 1, 1),
    _MscMpanlDlciVcDmepValue_Type()
)
mscMpanlDlciVcDmepValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciVcDmepValue.setStatus("mandatory")
_MscMpanlDlciLCo_ObjectIdentity = ObjectIdentity
mscMpanlDlciLCo = _MscMpanlDlciLCo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 4)
)
_MscMpanlDlciLCoRowStatusTable_Object = MibTable
mscMpanlDlciLCoRowStatusTable = _MscMpanlDlciLCoRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 4, 1)
)
if mibBuilder.loadTexts:
    mscMpanlDlciLCoRowStatusTable.setStatus("mandatory")
_MscMpanlDlciLCoRowStatusEntry_Object = MibTableRow
mscMpanlDlciLCoRowStatusEntry = _MscMpanlDlciLCoRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 4, 1, 1)
)
mscMpanlDlciLCoRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-MpaNetworkLinkMIB", "mscMpanlIndex"),
    (0, "Nortel-MsCarrier-MscPassport-MpaNetworkLinkMIB", "mscMpanlDlciIndex"),
    (0, "Nortel-MsCarrier-MscPassport-MpaNetworkLinkMIB", "mscMpanlDlciLCoIndex"),
)
if mibBuilder.loadTexts:
    mscMpanlDlciLCoRowStatusEntry.setStatus("mandatory")
_MscMpanlDlciLCoRowStatus_Type = RowStatus
_MscMpanlDlciLCoRowStatus_Object = MibTableColumn
mscMpanlDlciLCoRowStatus = _MscMpanlDlciLCoRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 4, 1, 1, 1),
    _MscMpanlDlciLCoRowStatus_Type()
)
mscMpanlDlciLCoRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciLCoRowStatus.setStatus("mandatory")
_MscMpanlDlciLCoComponentName_Type = DisplayString
_MscMpanlDlciLCoComponentName_Object = MibTableColumn
mscMpanlDlciLCoComponentName = _MscMpanlDlciLCoComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 4, 1, 1, 2),
    _MscMpanlDlciLCoComponentName_Type()
)
mscMpanlDlciLCoComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciLCoComponentName.setStatus("mandatory")
_MscMpanlDlciLCoStorageType_Type = StorageType
_MscMpanlDlciLCoStorageType_Object = MibTableColumn
mscMpanlDlciLCoStorageType = _MscMpanlDlciLCoStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 4, 1, 1, 4),
    _MscMpanlDlciLCoStorageType_Type()
)
mscMpanlDlciLCoStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciLCoStorageType.setStatus("mandatory")
_MscMpanlDlciLCoIndex_Type = NonReplicated
_MscMpanlDlciLCoIndex_Object = MibTableColumn
mscMpanlDlciLCoIndex = _MscMpanlDlciLCoIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 4, 1, 1, 10),
    _MscMpanlDlciLCoIndex_Type()
)
mscMpanlDlciLCoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscMpanlDlciLCoIndex.setStatus("mandatory")
_MscMpanlDlciLCoPathDataTable_Object = MibTable
mscMpanlDlciLCoPathDataTable = _MscMpanlDlciLCoPathDataTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 4, 10)
)
if mibBuilder.loadTexts:
    mscMpanlDlciLCoPathDataTable.setStatus("mandatory")
_MscMpanlDlciLCoPathDataEntry_Object = MibTableRow
mscMpanlDlciLCoPathDataEntry = _MscMpanlDlciLCoPathDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 4, 10, 1)
)
mscMpanlDlciLCoPathDataEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-MpaNetworkLinkMIB", "mscMpanlIndex"),
    (0, "Nortel-MsCarrier-MscPassport-MpaNetworkLinkMIB", "mscMpanlDlciIndex"),
    (0, "Nortel-MsCarrier-MscPassport-MpaNetworkLinkMIB", "mscMpanlDlciLCoIndex"),
)
if mibBuilder.loadTexts:
    mscMpanlDlciLCoPathDataEntry.setStatus("mandatory")


class _MscMpanlDlciLCoState_Type(Integer32):
    """Custom type mscMpanlDlciLCoState based on Integer32"""
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
        *(("connecting", 2),
          ("pathDown", 0),
          ("pathDownRetrying", 4),
          ("pathUp", 3),
          ("selectingRoute", 1))
    )


_MscMpanlDlciLCoState_Type.__name__ = "Integer32"
_MscMpanlDlciLCoState_Object = MibTableColumn
mscMpanlDlciLCoState = _MscMpanlDlciLCoState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 4, 10, 1, 1),
    _MscMpanlDlciLCoState_Type()
)
mscMpanlDlciLCoState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciLCoState.setStatus("mandatory")


class _MscMpanlDlciLCoEnd_Type(Integer32):
    """Custom type mscMpanlDlciLCoEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("called", 1),
          ("calling", 0))
    )


_MscMpanlDlciLCoEnd_Type.__name__ = "Integer32"
_MscMpanlDlciLCoEnd_Object = MibTableColumn
mscMpanlDlciLCoEnd = _MscMpanlDlciLCoEnd_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 4, 10, 1, 3),
    _MscMpanlDlciLCoEnd_Type()
)
mscMpanlDlciLCoEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciLCoEnd.setStatus("mandatory")


class _MscMpanlDlciLCoCostMetric_Type(Unsigned32):
    """Custom type mscMpanlDlciLCoCostMetric based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscMpanlDlciLCoCostMetric_Type.__name__ = "Unsigned32"
_MscMpanlDlciLCoCostMetric_Object = MibTableColumn
mscMpanlDlciLCoCostMetric = _MscMpanlDlciLCoCostMetric_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 4, 10, 1, 4),
    _MscMpanlDlciLCoCostMetric_Type()
)
mscMpanlDlciLCoCostMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciLCoCostMetric.setStatus("mandatory")


class _MscMpanlDlciLCoDelayMetric_Type(Unsigned32):
    """Custom type mscMpanlDlciLCoDelayMetric based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_MscMpanlDlciLCoDelayMetric_Type.__name__ = "Unsigned32"
_MscMpanlDlciLCoDelayMetric_Object = MibTableColumn
mscMpanlDlciLCoDelayMetric = _MscMpanlDlciLCoDelayMetric_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 4, 10, 1, 5),
    _MscMpanlDlciLCoDelayMetric_Type()
)
mscMpanlDlciLCoDelayMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciLCoDelayMetric.setStatus("mandatory")


class _MscMpanlDlciLCoRoundTripDelay_Type(Unsigned32):
    """Custom type mscMpanlDlciLCoRoundTripDelay based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000),
    )


_MscMpanlDlciLCoRoundTripDelay_Type.__name__ = "Unsigned32"
_MscMpanlDlciLCoRoundTripDelay_Object = MibTableColumn
mscMpanlDlciLCoRoundTripDelay = _MscMpanlDlciLCoRoundTripDelay_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 4, 10, 1, 6),
    _MscMpanlDlciLCoRoundTripDelay_Type()
)
mscMpanlDlciLCoRoundTripDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciLCoRoundTripDelay.setStatus("mandatory")


class _MscMpanlDlciLCoSetupPriority_Type(Unsigned32):
    """Custom type mscMpanlDlciLCoSetupPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_MscMpanlDlciLCoSetupPriority_Type.__name__ = "Unsigned32"
_MscMpanlDlciLCoSetupPriority_Object = MibTableColumn
mscMpanlDlciLCoSetupPriority = _MscMpanlDlciLCoSetupPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 4, 10, 1, 7),
    _MscMpanlDlciLCoSetupPriority_Type()
)
mscMpanlDlciLCoSetupPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciLCoSetupPriority.setStatus("mandatory")


class _MscMpanlDlciLCoHoldingPriority_Type(Unsigned32):
    """Custom type mscMpanlDlciLCoHoldingPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_MscMpanlDlciLCoHoldingPriority_Type.__name__ = "Unsigned32"
_MscMpanlDlciLCoHoldingPriority_Object = MibTableColumn
mscMpanlDlciLCoHoldingPriority = _MscMpanlDlciLCoHoldingPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 4, 10, 1, 8),
    _MscMpanlDlciLCoHoldingPriority_Type()
)
mscMpanlDlciLCoHoldingPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciLCoHoldingPriority.setStatus("mandatory")


class _MscMpanlDlciLCoRequiredTxBandwidth_Type(Gauge32):
    """Custom type mscMpanlDlciLCoRequiredTxBandwidth based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2048000),
    )


_MscMpanlDlciLCoRequiredTxBandwidth_Type.__name__ = "Gauge32"
_MscMpanlDlciLCoRequiredTxBandwidth_Object = MibTableColumn
mscMpanlDlciLCoRequiredTxBandwidth = _MscMpanlDlciLCoRequiredTxBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 4, 10, 1, 9),
    _MscMpanlDlciLCoRequiredTxBandwidth_Type()
)
mscMpanlDlciLCoRequiredTxBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciLCoRequiredTxBandwidth.setStatus("mandatory")


class _MscMpanlDlciLCoRequiredRxBandwidth_Type(Gauge32):
    """Custom type mscMpanlDlciLCoRequiredRxBandwidth based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2048000),
    )


_MscMpanlDlciLCoRequiredRxBandwidth_Type.__name__ = "Gauge32"
_MscMpanlDlciLCoRequiredRxBandwidth_Object = MibTableColumn
mscMpanlDlciLCoRequiredRxBandwidth = _MscMpanlDlciLCoRequiredRxBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 4, 10, 1, 10),
    _MscMpanlDlciLCoRequiredRxBandwidth_Type()
)
mscMpanlDlciLCoRequiredRxBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciLCoRequiredRxBandwidth.setStatus("mandatory")


class _MscMpanlDlciLCoRequiredTrafficType_Type(Integer32):
    """Custom type mscMpanlDlciLCoRequiredTrafficType based on Integer32"""
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
        *(("data", 1),
          ("trafficType1", 3),
          ("trafficType2", 4),
          ("trafficType3", 5),
          ("trafficType4", 6),
          ("trafficType5", 7),
          ("video", 2),
          ("voice", 0))
    )


_MscMpanlDlciLCoRequiredTrafficType_Type.__name__ = "Integer32"
_MscMpanlDlciLCoRequiredTrafficType_Object = MibTableColumn
mscMpanlDlciLCoRequiredTrafficType = _MscMpanlDlciLCoRequiredTrafficType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 4, 10, 1, 11),
    _MscMpanlDlciLCoRequiredTrafficType_Type()
)
mscMpanlDlciLCoRequiredTrafficType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciLCoRequiredTrafficType.setStatus("mandatory")


class _MscMpanlDlciLCoPermittedTrunkTypes_Type(OctetString):
    """Custom type mscMpanlDlciLCoPermittedTrunkTypes based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscMpanlDlciLCoPermittedTrunkTypes_Type.__name__ = "OctetString"
_MscMpanlDlciLCoPermittedTrunkTypes_Object = MibTableColumn
mscMpanlDlciLCoPermittedTrunkTypes = _MscMpanlDlciLCoPermittedTrunkTypes_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 4, 10, 1, 12),
    _MscMpanlDlciLCoPermittedTrunkTypes_Type()
)
mscMpanlDlciLCoPermittedTrunkTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciLCoPermittedTrunkTypes.setStatus("mandatory")


class _MscMpanlDlciLCoRequiredSecurity_Type(Unsigned32):
    """Custom type mscMpanlDlciLCoRequiredSecurity based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_MscMpanlDlciLCoRequiredSecurity_Type.__name__ = "Unsigned32"
_MscMpanlDlciLCoRequiredSecurity_Object = MibTableColumn
mscMpanlDlciLCoRequiredSecurity = _MscMpanlDlciLCoRequiredSecurity_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 4, 10, 1, 13),
    _MscMpanlDlciLCoRequiredSecurity_Type()
)
mscMpanlDlciLCoRequiredSecurity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciLCoRequiredSecurity.setStatus("mandatory")


class _MscMpanlDlciLCoRequiredCustomerParameter_Type(Unsigned32):
    """Custom type mscMpanlDlciLCoRequiredCustomerParameter based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_MscMpanlDlciLCoRequiredCustomerParameter_Type.__name__ = "Unsigned32"
_MscMpanlDlciLCoRequiredCustomerParameter_Object = MibTableColumn
mscMpanlDlciLCoRequiredCustomerParameter = _MscMpanlDlciLCoRequiredCustomerParameter_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 4, 10, 1, 14),
    _MscMpanlDlciLCoRequiredCustomerParameter_Type()
)
mscMpanlDlciLCoRequiredCustomerParameter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciLCoRequiredCustomerParameter.setStatus("mandatory")


class _MscMpanlDlciLCoEmissionPriority_Type(Unsigned32):
    """Custom type mscMpanlDlciLCoEmissionPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_MscMpanlDlciLCoEmissionPriority_Type.__name__ = "Unsigned32"
_MscMpanlDlciLCoEmissionPriority_Object = MibTableColumn
mscMpanlDlciLCoEmissionPriority = _MscMpanlDlciLCoEmissionPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 4, 10, 1, 15),
    _MscMpanlDlciLCoEmissionPriority_Type()
)
mscMpanlDlciLCoEmissionPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciLCoEmissionPriority.setStatus("mandatory")


class _MscMpanlDlciLCoDiscardPriority_Type(Unsigned32):
    """Custom type mscMpanlDlciLCoDiscardPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_MscMpanlDlciLCoDiscardPriority_Type.__name__ = "Unsigned32"
_MscMpanlDlciLCoDiscardPriority_Object = MibTableColumn
mscMpanlDlciLCoDiscardPriority = _MscMpanlDlciLCoDiscardPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 4, 10, 1, 16),
    _MscMpanlDlciLCoDiscardPriority_Type()
)
mscMpanlDlciLCoDiscardPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciLCoDiscardPriority.setStatus("mandatory")


class _MscMpanlDlciLCoRetryCount_Type(Unsigned32):
    """Custom type mscMpanlDlciLCoRetryCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscMpanlDlciLCoRetryCount_Type.__name__ = "Unsigned32"
_MscMpanlDlciLCoRetryCount_Object = MibTableColumn
mscMpanlDlciLCoRetryCount = _MscMpanlDlciLCoRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 4, 10, 1, 18),
    _MscMpanlDlciLCoRetryCount_Type()
)
mscMpanlDlciLCoRetryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciLCoRetryCount.setStatus("mandatory")


class _MscMpanlDlciLCoPathFailureCount_Type(Unsigned32):
    """Custom type mscMpanlDlciLCoPathFailureCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscMpanlDlciLCoPathFailureCount_Type.__name__ = "Unsigned32"
_MscMpanlDlciLCoPathFailureCount_Object = MibTableColumn
mscMpanlDlciLCoPathFailureCount = _MscMpanlDlciLCoPathFailureCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 4, 10, 1, 19),
    _MscMpanlDlciLCoPathFailureCount_Type()
)
mscMpanlDlciLCoPathFailureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciLCoPathFailureCount.setStatus("mandatory")


class _MscMpanlDlciLCoReasonForNoRoute_Type(Integer32):
    """Custom type mscMpanlDlciLCoReasonForNoRoute based on Integer32"""
    defaultValue = 0

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
              12,
              13,
              14)
        )
    )
    namedValues = NamedValues(
        *(("anError", 12),
          ("attributeProfileProblem", 13),
          ("attributesNotMet", 11),
          ("destinationNameTooLong", 1),
          ("destinationNotSpecified", 2),
          ("incorrectDestination", 4),
          ("incorrectDestinationEndPoint", 5),
          ("manualPathIndexProblem", 14),
          ("none", 0),
          ("routeCostTooMuch", 9),
          ("routesDelayTooLong", 10),
          ("sameNode", 8),
          ("unknownDestination", 7),
          ("unknownDestinationName", 3),
          ("unknownSource", 6))
    )


_MscMpanlDlciLCoReasonForNoRoute_Type.__name__ = "Integer32"
_MscMpanlDlciLCoReasonForNoRoute_Object = MibTableColumn
mscMpanlDlciLCoReasonForNoRoute = _MscMpanlDlciLCoReasonForNoRoute_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 4, 10, 1, 20),
    _MscMpanlDlciLCoReasonForNoRoute_Type()
)
mscMpanlDlciLCoReasonForNoRoute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciLCoReasonForNoRoute.setStatus("mandatory")


class _MscMpanlDlciLCoLastTearDownReason_Type(Integer32):
    """Custom type mscMpanlDlciLCoLastTearDownReason based on Integer32"""
    defaultValue = 0

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
              22)
        )
    )
    namedValues = NamedValues(
        *(("accessCardFailure", 20),
          ("bumped", 19),
          ("callLoopedBack", 13),
          ("farEndBusy", 12),
          ("farEndNotFound", 10),
          ("farEndNotReady", 15),
          ("insufficientRxLcOrBandwidth", 3),
          ("insufficientTxLcOrBandwidth", 2),
          ("lostLcnClash", 7),
          ("networkCongestion", 8),
          ("none", 0),
          ("normalShutDown", 1),
          ("operatorForced", 6),
          ("optimized", 21),
          ("overrideRemoteName", 22),
          ("reconnectFromFarEnd", 18),
          ("remoteNameMismatch", 16),
          ("serviceTypeMismatch", 17),
          ("trunkCardFailure", 5),
          ("trunkFailure", 4),
          ("trunkNotFound", 9),
          ("unknownReason", 14),
          ("wrongModuleReached", 11))
    )


_MscMpanlDlciLCoLastTearDownReason_Type.__name__ = "Integer32"
_MscMpanlDlciLCoLastTearDownReason_Object = MibTableColumn
mscMpanlDlciLCoLastTearDownReason = _MscMpanlDlciLCoLastTearDownReason_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 4, 10, 1, 21),
    _MscMpanlDlciLCoLastTearDownReason_Type()
)
mscMpanlDlciLCoLastTearDownReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciLCoLastTearDownReason.setStatus("mandatory")


class _MscMpanlDlciLCoPathFailureAction_Type(Integer32):
    """Custom type mscMpanlDlciLCoPathFailureAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disconnectConnection", 0),
          ("reRoutePath", 1))
    )


_MscMpanlDlciLCoPathFailureAction_Type.__name__ = "Integer32"
_MscMpanlDlciLCoPathFailureAction_Object = MibTableColumn
mscMpanlDlciLCoPathFailureAction = _MscMpanlDlciLCoPathFailureAction_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 4, 10, 1, 22),
    _MscMpanlDlciLCoPathFailureAction_Type()
)
mscMpanlDlciLCoPathFailureAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciLCoPathFailureAction.setStatus("mandatory")


class _MscMpanlDlciLCoBumpPreference_Type(Integer32):
    """Custom type mscMpanlDlciLCoBumpPreference based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("bumpToObtainBestRoute", 1),
          ("bumpWhenNecessary", 0))
    )


_MscMpanlDlciLCoBumpPreference_Type.__name__ = "Integer32"
_MscMpanlDlciLCoBumpPreference_Object = MibTableColumn
mscMpanlDlciLCoBumpPreference = _MscMpanlDlciLCoBumpPreference_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 4, 10, 1, 23),
    _MscMpanlDlciLCoBumpPreference_Type()
)
mscMpanlDlciLCoBumpPreference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciLCoBumpPreference.setStatus("mandatory")


class _MscMpanlDlciLCoOptimization_Type(Integer32):
    """Custom type mscMpanlDlciLCoOptimization based on Integer32"""
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


_MscMpanlDlciLCoOptimization_Type.__name__ = "Integer32"
_MscMpanlDlciLCoOptimization_Object = MibTableColumn
mscMpanlDlciLCoOptimization = _MscMpanlDlciLCoOptimization_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 4, 10, 1, 24),
    _MscMpanlDlciLCoOptimization_Type()
)
mscMpanlDlciLCoOptimization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciLCoOptimization.setStatus("mandatory")


class _MscMpanlDlciLCoPathUpDateTime_Type(EnterpriseDateAndTime):
    """Custom type mscMpanlDlciLCoPathUpDateTime based on EnterpriseDateAndTime"""
    subtypeSpec = EnterpriseDateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(19, 19),
    )


_MscMpanlDlciLCoPathUpDateTime_Type.__name__ = "EnterpriseDateAndTime"
_MscMpanlDlciLCoPathUpDateTime_Object = MibTableColumn
mscMpanlDlciLCoPathUpDateTime = _MscMpanlDlciLCoPathUpDateTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 4, 10, 1, 25),
    _MscMpanlDlciLCoPathUpDateTime_Type()
)
mscMpanlDlciLCoPathUpDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciLCoPathUpDateTime.setStatus("mandatory")
_MscMpanlDlciLCoStatsTable_Object = MibTable
mscMpanlDlciLCoStatsTable = _MscMpanlDlciLCoStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 4, 11)
)
if mibBuilder.loadTexts:
    mscMpanlDlciLCoStatsTable.setStatus("mandatory")
_MscMpanlDlciLCoStatsEntry_Object = MibTableRow
mscMpanlDlciLCoStatsEntry = _MscMpanlDlciLCoStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 4, 11, 1)
)
mscMpanlDlciLCoStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-MpaNetworkLinkMIB", "mscMpanlIndex"),
    (0, "Nortel-MsCarrier-MscPassport-MpaNetworkLinkMIB", "mscMpanlDlciIndex"),
    (0, "Nortel-MsCarrier-MscPassport-MpaNetworkLinkMIB", "mscMpanlDlciLCoIndex"),
)
if mibBuilder.loadTexts:
    mscMpanlDlciLCoStatsEntry.setStatus("mandatory")
_MscMpanlDlciLCoPktsToNetwork_Type = PassportCounter64
_MscMpanlDlciLCoPktsToNetwork_Object = MibTableColumn
mscMpanlDlciLCoPktsToNetwork = _MscMpanlDlciLCoPktsToNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 4, 11, 1, 1),
    _MscMpanlDlciLCoPktsToNetwork_Type()
)
mscMpanlDlciLCoPktsToNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciLCoPktsToNetwork.setStatus("mandatory")
_MscMpanlDlciLCoBytesToNetwork_Type = PassportCounter64
_MscMpanlDlciLCoBytesToNetwork_Object = MibTableColumn
mscMpanlDlciLCoBytesToNetwork = _MscMpanlDlciLCoBytesToNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 4, 11, 1, 2),
    _MscMpanlDlciLCoBytesToNetwork_Type()
)
mscMpanlDlciLCoBytesToNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciLCoBytesToNetwork.setStatus("mandatory")
_MscMpanlDlciLCoPktsFromNetwork_Type = PassportCounter64
_MscMpanlDlciLCoPktsFromNetwork_Object = MibTableColumn
mscMpanlDlciLCoPktsFromNetwork = _MscMpanlDlciLCoPktsFromNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 4, 11, 1, 3),
    _MscMpanlDlciLCoPktsFromNetwork_Type()
)
mscMpanlDlciLCoPktsFromNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciLCoPktsFromNetwork.setStatus("mandatory")
_MscMpanlDlciLCoBytesFromNetwork_Type = PassportCounter64
_MscMpanlDlciLCoBytesFromNetwork_Object = MibTableColumn
mscMpanlDlciLCoBytesFromNetwork = _MscMpanlDlciLCoBytesFromNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 4, 11, 1, 4),
    _MscMpanlDlciLCoBytesFromNetwork_Type()
)
mscMpanlDlciLCoBytesFromNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciLCoBytesFromNetwork.setStatus("mandatory")
_MscMpanlDlciLCoCallDataTable_Object = MibTable
mscMpanlDlciLCoCallDataTable = _MscMpanlDlciLCoCallDataTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 4, 12)
)
if mibBuilder.loadTexts:
    mscMpanlDlciLCoCallDataTable.setStatus("mandatory")
_MscMpanlDlciLCoCallDataEntry_Object = MibTableRow
mscMpanlDlciLCoCallDataEntry = _MscMpanlDlciLCoCallDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 4, 12, 1)
)
mscMpanlDlciLCoCallDataEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-MpaNetworkLinkMIB", "mscMpanlIndex"),
    (0, "Nortel-MsCarrier-MscPassport-MpaNetworkLinkMIB", "mscMpanlDlciIndex"),
    (0, "Nortel-MsCarrier-MscPassport-MpaNetworkLinkMIB", "mscMpanlDlciLCoIndex"),
)
if mibBuilder.loadTexts:
    mscMpanlDlciLCoCallDataEntry.setStatus("mandatory")


class _MscMpanlDlciLCoCallingNpi_Type(Integer32):
    """Custom type mscMpanlDlciLCoCallingNpi based on Integer32"""
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


_MscMpanlDlciLCoCallingNpi_Type.__name__ = "Integer32"
_MscMpanlDlciLCoCallingNpi_Object = MibTableColumn
mscMpanlDlciLCoCallingNpi = _MscMpanlDlciLCoCallingNpi_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 4, 12, 1, 27),
    _MscMpanlDlciLCoCallingNpi_Type()
)
mscMpanlDlciLCoCallingNpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciLCoCallingNpi.setStatus("mandatory")


class _MscMpanlDlciLCoCallingDna_Type(DigitString):
    """Custom type mscMpanlDlciLCoCallingDna based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_MscMpanlDlciLCoCallingDna_Type.__name__ = "DigitString"
_MscMpanlDlciLCoCallingDna_Object = MibTableColumn
mscMpanlDlciLCoCallingDna = _MscMpanlDlciLCoCallingDna_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 4, 12, 1, 28),
    _MscMpanlDlciLCoCallingDna_Type()
)
mscMpanlDlciLCoCallingDna.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciLCoCallingDna.setStatus("mandatory")


class _MscMpanlDlciLCoElapsedTimeTillNow_Type(Unsigned32):
    """Custom type mscMpanlDlciLCoElapsedTimeTillNow based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_MscMpanlDlciLCoElapsedTimeTillNow_Type.__name__ = "Unsigned32"
_MscMpanlDlciLCoElapsedTimeTillNow_Object = MibTableColumn
mscMpanlDlciLCoElapsedTimeTillNow = _MscMpanlDlciLCoElapsedTimeTillNow_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 4, 12, 1, 30),
    _MscMpanlDlciLCoElapsedTimeTillNow_Type()
)
mscMpanlDlciLCoElapsedTimeTillNow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciLCoElapsedTimeTillNow.setStatus("mandatory")


class _MscMpanlDlciLCoCallReferenceNumber_Type(Hex):
    """Custom type mscMpanlDlciLCoCallReferenceNumber based on Hex"""
    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_MscMpanlDlciLCoCallReferenceNumber_Type.__name__ = "Hex"
_MscMpanlDlciLCoCallReferenceNumber_Object = MibTableColumn
mscMpanlDlciLCoCallReferenceNumber = _MscMpanlDlciLCoCallReferenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 4, 12, 1, 31),
    _MscMpanlDlciLCoCallReferenceNumber_Type()
)
mscMpanlDlciLCoCallReferenceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciLCoCallReferenceNumber.setStatus("mandatory")


class _MscMpanlDlciLCoCalledNpi_Type(Integer32):
    """Custom type mscMpanlDlciLCoCalledNpi based on Integer32"""
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


_MscMpanlDlciLCoCalledNpi_Type.__name__ = "Integer32"
_MscMpanlDlciLCoCalledNpi_Object = MibTableColumn
mscMpanlDlciLCoCalledNpi = _MscMpanlDlciLCoCalledNpi_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 4, 12, 1, 33),
    _MscMpanlDlciLCoCalledNpi_Type()
)
mscMpanlDlciLCoCalledNpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciLCoCalledNpi.setStatus("mandatory")


class _MscMpanlDlciLCoCalledDna_Type(DigitString):
    """Custom type mscMpanlDlciLCoCalledDna based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_MscMpanlDlciLCoCalledDna_Type.__name__ = "DigitString"
_MscMpanlDlciLCoCalledDna_Object = MibTableColumn
mscMpanlDlciLCoCalledDna = _MscMpanlDlciLCoCalledDna_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 4, 12, 1, 34),
    _MscMpanlDlciLCoCalledDna_Type()
)
mscMpanlDlciLCoCalledDna.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciLCoCalledDna.setStatus("mandatory")
_MscMpanlDlciLCoPathTable_Object = MibTable
mscMpanlDlciLCoPathTable = _MscMpanlDlciLCoPathTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 4, 401)
)
if mibBuilder.loadTexts:
    mscMpanlDlciLCoPathTable.setStatus("mandatory")
_MscMpanlDlciLCoPathEntry_Object = MibTableRow
mscMpanlDlciLCoPathEntry = _MscMpanlDlciLCoPathEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 4, 401, 1)
)
mscMpanlDlciLCoPathEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-MpaNetworkLinkMIB", "mscMpanlIndex"),
    (0, "Nortel-MsCarrier-MscPassport-MpaNetworkLinkMIB", "mscMpanlDlciIndex"),
    (0, "Nortel-MsCarrier-MscPassport-MpaNetworkLinkMIB", "mscMpanlDlciLCoIndex"),
    (0, "Nortel-MsCarrier-MscPassport-MpaNetworkLinkMIB", "mscMpanlDlciLCoPathValue"),
)
if mibBuilder.loadTexts:
    mscMpanlDlciLCoPathEntry.setStatus("mandatory")


class _MscMpanlDlciLCoPathValue_Type(AsciiString):
    """Custom type mscMpanlDlciLCoPathValue based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_MscMpanlDlciLCoPathValue_Type.__name__ = "AsciiString"
_MscMpanlDlciLCoPathValue_Object = MibTableColumn
mscMpanlDlciLCoPathValue = _MscMpanlDlciLCoPathValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 4, 401, 1, 1),
    _MscMpanlDlciLCoPathValue_Type()
)
mscMpanlDlciLCoPathValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciLCoPathValue.setStatus("mandatory")
_MscMpanlDlciJvc_ObjectIdentity = ObjectIdentity
mscMpanlDlciJvc = _MscMpanlDlciJvc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 5)
)
_MscMpanlDlciJvcRowStatusTable_Object = MibTable
mscMpanlDlciJvcRowStatusTable = _MscMpanlDlciJvcRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 5, 1)
)
if mibBuilder.loadTexts:
    mscMpanlDlciJvcRowStatusTable.setStatus("mandatory")
_MscMpanlDlciJvcRowStatusEntry_Object = MibTableRow
mscMpanlDlciJvcRowStatusEntry = _MscMpanlDlciJvcRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 5, 1, 1)
)
mscMpanlDlciJvcRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-MpaNetworkLinkMIB", "mscMpanlIndex"),
    (0, "Nortel-MsCarrier-MscPassport-MpaNetworkLinkMIB", "mscMpanlDlciIndex"),
    (0, "Nortel-MsCarrier-MscPassport-MpaNetworkLinkMIB", "mscMpanlDlciJvcIndex"),
)
if mibBuilder.loadTexts:
    mscMpanlDlciJvcRowStatusEntry.setStatus("mandatory")
_MscMpanlDlciJvcRowStatus_Type = RowStatus
_MscMpanlDlciJvcRowStatus_Object = MibTableColumn
mscMpanlDlciJvcRowStatus = _MscMpanlDlciJvcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 5, 1, 1, 1),
    _MscMpanlDlciJvcRowStatus_Type()
)
mscMpanlDlciJvcRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciJvcRowStatus.setStatus("mandatory")
_MscMpanlDlciJvcComponentName_Type = DisplayString
_MscMpanlDlciJvcComponentName_Object = MibTableColumn
mscMpanlDlciJvcComponentName = _MscMpanlDlciJvcComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 5, 1, 1, 2),
    _MscMpanlDlciJvcComponentName_Type()
)
mscMpanlDlciJvcComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciJvcComponentName.setStatus("mandatory")
_MscMpanlDlciJvcStorageType_Type = StorageType
_MscMpanlDlciJvcStorageType_Object = MibTableColumn
mscMpanlDlciJvcStorageType = _MscMpanlDlciJvcStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 5, 1, 1, 4),
    _MscMpanlDlciJvcStorageType_Type()
)
mscMpanlDlciJvcStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciJvcStorageType.setStatus("mandatory")
_MscMpanlDlciJvcIndex_Type = NonReplicated
_MscMpanlDlciJvcIndex_Object = MibTableColumn
mscMpanlDlciJvcIndex = _MscMpanlDlciJvcIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 5, 1, 1, 10),
    _MscMpanlDlciJvcIndex_Type()
)
mscMpanlDlciJvcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscMpanlDlciJvcIndex.setStatus("mandatory")
_MscMpanlDlciJvcOperTable_Object = MibTable
mscMpanlDlciJvcOperTable = _MscMpanlDlciJvcOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 5, 10)
)
if mibBuilder.loadTexts:
    mscMpanlDlciJvcOperTable.setStatus("mandatory")
_MscMpanlDlciJvcOperEntry_Object = MibTableRow
mscMpanlDlciJvcOperEntry = _MscMpanlDlciJvcOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 5, 10, 1)
)
mscMpanlDlciJvcOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-MpaNetworkLinkMIB", "mscMpanlIndex"),
    (0, "Nortel-MsCarrier-MscPassport-MpaNetworkLinkMIB", "mscMpanlDlciIndex"),
    (0, "Nortel-MsCarrier-MscPassport-MpaNetworkLinkMIB", "mscMpanlDlciJvcIndex"),
)
if mibBuilder.loadTexts:
    mscMpanlDlciJvcOperEntry.setStatus("mandatory")


class _MscMpanlDlciJvcCurrentState_Type(Integer32):
    """Custom type mscMpanlDlciJvcCurrentState based on Integer32"""
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
        *(("active", 4),
          ("callBlockPresent", 3),
          ("callDisconnected", 7),
          ("callIndication", 2),
          ("callRequest", 1),
          ("callTerminated", 8),
          ("discInitiated", 5),
          ("discPktPresent", 6),
          ("null", 0))
    )


_MscMpanlDlciJvcCurrentState_Type.__name__ = "Integer32"
_MscMpanlDlciJvcCurrentState_Object = MibTableColumn
mscMpanlDlciJvcCurrentState = _MscMpanlDlciJvcCurrentState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 5, 10, 1, 1),
    _MscMpanlDlciJvcCurrentState_Type()
)
mscMpanlDlciJvcCurrentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciJvcCurrentState.setStatus("mandatory")


class _MscMpanlDlciJvcPreviousState_Type(Integer32):
    """Custom type mscMpanlDlciJvcPreviousState based on Integer32"""
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
        *(("active", 4),
          ("callBlockPresent", 3),
          ("callDisconnected", 7),
          ("callIndication", 2),
          ("callRequest", 1),
          ("callTerminated", 8),
          ("discInitiated", 5),
          ("discPktPresent", 6),
          ("null", 0))
    )


_MscMpanlDlciJvcPreviousState_Type.__name__ = "Integer32"
_MscMpanlDlciJvcPreviousState_Object = MibTableColumn
mscMpanlDlciJvcPreviousState = _MscMpanlDlciJvcPreviousState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 5, 10, 1, 2),
    _MscMpanlDlciJvcPreviousState_Type()
)
mscMpanlDlciJvcPreviousState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciJvcPreviousState.setStatus("mandatory")


class _MscMpanlDlciJvcCallingNpi_Type(Integer32):
    """Custom type mscMpanlDlciJvcCallingNpi based on Integer32"""
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


_MscMpanlDlciJvcCallingNpi_Type.__name__ = "Integer32"
_MscMpanlDlciJvcCallingNpi_Object = MibTableColumn
mscMpanlDlciJvcCallingNpi = _MscMpanlDlciJvcCallingNpi_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 5, 10, 1, 6),
    _MscMpanlDlciJvcCallingNpi_Type()
)
mscMpanlDlciJvcCallingNpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciJvcCallingNpi.setStatus("mandatory")


class _MscMpanlDlciJvcCallingAddress_Type(DigitString):
    """Custom type mscMpanlDlciJvcCallingAddress based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_MscMpanlDlciJvcCallingAddress_Type.__name__ = "DigitString"
_MscMpanlDlciJvcCallingAddress_Object = MibTableColumn
mscMpanlDlciJvcCallingAddress = _MscMpanlDlciJvcCallingAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 5, 10, 1, 7),
    _MscMpanlDlciJvcCallingAddress_Type()
)
mscMpanlDlciJvcCallingAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciJvcCallingAddress.setStatus("mandatory")


class _MscMpanlDlciJvcCallingLcn_Type(Unsigned32):
    """Custom type mscMpanlDlciJvcCallingLcn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_MscMpanlDlciJvcCallingLcn_Type.__name__ = "Unsigned32"
_MscMpanlDlciJvcCallingLcn_Object = MibTableColumn
mscMpanlDlciJvcCallingLcn = _MscMpanlDlciJvcCallingLcn_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 5, 10, 1, 8),
    _MscMpanlDlciJvcCallingLcn_Type()
)
mscMpanlDlciJvcCallingLcn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciJvcCallingLcn.setStatus("mandatory")


class _MscMpanlDlciJvcCalledNpi_Type(Integer32):
    """Custom type mscMpanlDlciJvcCalledNpi based on Integer32"""
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


_MscMpanlDlciJvcCalledNpi_Type.__name__ = "Integer32"
_MscMpanlDlciJvcCalledNpi_Object = MibTableColumn
mscMpanlDlciJvcCalledNpi = _MscMpanlDlciJvcCalledNpi_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 5, 10, 1, 9),
    _MscMpanlDlciJvcCalledNpi_Type()
)
mscMpanlDlciJvcCalledNpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciJvcCalledNpi.setStatus("mandatory")


class _MscMpanlDlciJvcCalledAddress_Type(DigitString):
    """Custom type mscMpanlDlciJvcCalledAddress based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_MscMpanlDlciJvcCalledAddress_Type.__name__ = "DigitString"
_MscMpanlDlciJvcCalledAddress_Object = MibTableColumn
mscMpanlDlciJvcCalledAddress = _MscMpanlDlciJvcCalledAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 5, 10, 1, 10),
    _MscMpanlDlciJvcCalledAddress_Type()
)
mscMpanlDlciJvcCalledAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciJvcCalledAddress.setStatus("mandatory")


class _MscMpanlDlciJvcCalledLcn_Type(Unsigned32):
    """Custom type mscMpanlDlciJvcCalledLcn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_MscMpanlDlciJvcCalledLcn_Type.__name__ = "Unsigned32"
_MscMpanlDlciJvcCalledLcn_Object = MibTableColumn
mscMpanlDlciJvcCalledLcn = _MscMpanlDlciJvcCalledLcn_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 5, 10, 1, 11),
    _MscMpanlDlciJvcCalledLcn_Type()
)
mscMpanlDlciJvcCalledLcn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciJvcCalledLcn.setStatus("mandatory")
_MscMpanlDlciJvcStatTable_Object = MibTable
mscMpanlDlciJvcStatTable = _MscMpanlDlciJvcStatTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 5, 11)
)
if mibBuilder.loadTexts:
    mscMpanlDlciJvcStatTable.setStatus("mandatory")
_MscMpanlDlciJvcStatEntry_Object = MibTableRow
mscMpanlDlciJvcStatEntry = _MscMpanlDlciJvcStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 5, 11, 1)
)
mscMpanlDlciJvcStatEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-MpaNetworkLinkMIB", "mscMpanlIndex"),
    (0, "Nortel-MsCarrier-MscPassport-MpaNetworkLinkMIB", "mscMpanlDlciIndex"),
    (0, "Nortel-MsCarrier-MscPassport-MpaNetworkLinkMIB", "mscMpanlDlciJvcIndex"),
)
if mibBuilder.loadTexts:
    mscMpanlDlciJvcStatEntry.setStatus("mandatory")


class _MscMpanlDlciJvcPacketsFromSubnet_Type(Unsigned32):
    """Custom type mscMpanlDlciJvcPacketsFromSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscMpanlDlciJvcPacketsFromSubnet_Type.__name__ = "Unsigned32"
_MscMpanlDlciJvcPacketsFromSubnet_Object = MibTableColumn
mscMpanlDlciJvcPacketsFromSubnet = _MscMpanlDlciJvcPacketsFromSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 5, 11, 1, 1),
    _MscMpanlDlciJvcPacketsFromSubnet_Type()
)
mscMpanlDlciJvcPacketsFromSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciJvcPacketsFromSubnet.setStatus("mandatory")


class _MscMpanlDlciJvcPacketsToSubnet_Type(Unsigned32):
    """Custom type mscMpanlDlciJvcPacketsToSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscMpanlDlciJvcPacketsToSubnet_Type.__name__ = "Unsigned32"
_MscMpanlDlciJvcPacketsToSubnet_Object = MibTableColumn
mscMpanlDlciJvcPacketsToSubnet = _MscMpanlDlciJvcPacketsToSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 5, 11, 1, 2),
    _MscMpanlDlciJvcPacketsToSubnet_Type()
)
mscMpanlDlciJvcPacketsToSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciJvcPacketsToSubnet.setStatus("mandatory")


class _MscMpanlDlciJvcPacketsDiscarded_Type(Unsigned32):
    """Custom type mscMpanlDlciJvcPacketsDiscarded based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscMpanlDlciJvcPacketsDiscarded_Type.__name__ = "Unsigned32"
_MscMpanlDlciJvcPacketsDiscarded_Object = MibTableColumn
mscMpanlDlciJvcPacketsDiscarded = _MscMpanlDlciJvcPacketsDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 5, 11, 1, 3),
    _MscMpanlDlciJvcPacketsDiscarded_Type()
)
mscMpanlDlciJvcPacketsDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciJvcPacketsDiscarded.setStatus("mandatory")


class _MscMpanlDlciJvcProtocolErrors_Type(Unsigned32):
    """Custom type mscMpanlDlciJvcProtocolErrors based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscMpanlDlciJvcProtocolErrors_Type.__name__ = "Unsigned32"
_MscMpanlDlciJvcProtocolErrors_Object = MibTableColumn
mscMpanlDlciJvcProtocolErrors = _MscMpanlDlciJvcProtocolErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 5, 11, 1, 4),
    _MscMpanlDlciJvcProtocolErrors_Type()
)
mscMpanlDlciJvcProtocolErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciJvcProtocolErrors.setStatus("mandatory")
_MscMpanlDlciStateTable_Object = MibTable
mscMpanlDlciStateTable = _MscMpanlDlciStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 10)
)
if mibBuilder.loadTexts:
    mscMpanlDlciStateTable.setStatus("mandatory")
_MscMpanlDlciStateEntry_Object = MibTableRow
mscMpanlDlciStateEntry = _MscMpanlDlciStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 10, 1)
)
mscMpanlDlciStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-MpaNetworkLinkMIB", "mscMpanlIndex"),
    (0, "Nortel-MsCarrier-MscPassport-MpaNetworkLinkMIB", "mscMpanlDlciIndex"),
)
if mibBuilder.loadTexts:
    mscMpanlDlciStateEntry.setStatus("mandatory")


class _MscMpanlDlciAdminState_Type(Integer32):
    """Custom type mscMpanlDlciAdminState based on Integer32"""
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


_MscMpanlDlciAdminState_Type.__name__ = "Integer32"
_MscMpanlDlciAdminState_Object = MibTableColumn
mscMpanlDlciAdminState = _MscMpanlDlciAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 10, 1, 1),
    _MscMpanlDlciAdminState_Type()
)
mscMpanlDlciAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciAdminState.setStatus("mandatory")


class _MscMpanlDlciOperationalState_Type(Integer32):
    """Custom type mscMpanlDlciOperationalState based on Integer32"""
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


_MscMpanlDlciOperationalState_Type.__name__ = "Integer32"
_MscMpanlDlciOperationalState_Object = MibTableColumn
mscMpanlDlciOperationalState = _MscMpanlDlciOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 10, 1, 2),
    _MscMpanlDlciOperationalState_Type()
)
mscMpanlDlciOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciOperationalState.setStatus("mandatory")


class _MscMpanlDlciUsageState_Type(Integer32):
    """Custom type mscMpanlDlciUsageState based on Integer32"""
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


_MscMpanlDlciUsageState_Type.__name__ = "Integer32"
_MscMpanlDlciUsageState_Object = MibTableColumn
mscMpanlDlciUsageState = _MscMpanlDlciUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 10, 1, 3),
    _MscMpanlDlciUsageState_Type()
)
mscMpanlDlciUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciUsageState.setStatus("mandatory")


class _MscMpanlDlciAvailabilityStatus_Type(OctetString):
    """Custom type mscMpanlDlciAvailabilityStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_MscMpanlDlciAvailabilityStatus_Type.__name__ = "OctetString"
_MscMpanlDlciAvailabilityStatus_Object = MibTableColumn
mscMpanlDlciAvailabilityStatus = _MscMpanlDlciAvailabilityStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 10, 1, 4),
    _MscMpanlDlciAvailabilityStatus_Type()
)
mscMpanlDlciAvailabilityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciAvailabilityStatus.setStatus("mandatory")


class _MscMpanlDlciProceduralStatus_Type(OctetString):
    """Custom type mscMpanlDlciProceduralStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscMpanlDlciProceduralStatus_Type.__name__ = "OctetString"
_MscMpanlDlciProceduralStatus_Object = MibTableColumn
mscMpanlDlciProceduralStatus = _MscMpanlDlciProceduralStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 10, 1, 5),
    _MscMpanlDlciProceduralStatus_Type()
)
mscMpanlDlciProceduralStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciProceduralStatus.setStatus("mandatory")


class _MscMpanlDlciControlStatus_Type(OctetString):
    """Custom type mscMpanlDlciControlStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscMpanlDlciControlStatus_Type.__name__ = "OctetString"
_MscMpanlDlciControlStatus_Object = MibTableColumn
mscMpanlDlciControlStatus = _MscMpanlDlciControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 10, 1, 6),
    _MscMpanlDlciControlStatus_Type()
)
mscMpanlDlciControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciControlStatus.setStatus("mandatory")


class _MscMpanlDlciAlarmStatus_Type(OctetString):
    """Custom type mscMpanlDlciAlarmStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscMpanlDlciAlarmStatus_Type.__name__ = "OctetString"
_MscMpanlDlciAlarmStatus_Object = MibTableColumn
mscMpanlDlciAlarmStatus = _MscMpanlDlciAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 10, 1, 7),
    _MscMpanlDlciAlarmStatus_Type()
)
mscMpanlDlciAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciAlarmStatus.setStatus("mandatory")


class _MscMpanlDlciStandbyStatus_Type(Integer32):
    """Custom type mscMpanlDlciStandbyStatus based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              15)
        )
    )
    namedValues = NamedValues(
        *(("coldStandby", 1),
          ("hotStandby", 0),
          ("notSet", 15),
          ("providingService", 2))
    )


_MscMpanlDlciStandbyStatus_Type.__name__ = "Integer32"
_MscMpanlDlciStandbyStatus_Object = MibTableColumn
mscMpanlDlciStandbyStatus = _MscMpanlDlciStandbyStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 10, 1, 8),
    _MscMpanlDlciStandbyStatus_Type()
)
mscMpanlDlciStandbyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciStandbyStatus.setStatus("mandatory")


class _MscMpanlDlciUnknownStatus_Type(Integer32):
    """Custom type mscMpanlDlciUnknownStatus based on Integer32"""
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


_MscMpanlDlciUnknownStatus_Type.__name__ = "Integer32"
_MscMpanlDlciUnknownStatus_Object = MibTableColumn
mscMpanlDlciUnknownStatus = _MscMpanlDlciUnknownStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 10, 1, 9),
    _MscMpanlDlciUnknownStatus_Type()
)
mscMpanlDlciUnknownStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciUnknownStatus.setStatus("mandatory")
_MscMpanlDlciCalldTable_Object = MibTable
mscMpanlDlciCalldTable = _MscMpanlDlciCalldTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 11)
)
if mibBuilder.loadTexts:
    mscMpanlDlciCalldTable.setStatus("mandatory")
_MscMpanlDlciCalldEntry_Object = MibTableRow
mscMpanlDlciCalldEntry = _MscMpanlDlciCalldEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 11, 1)
)
mscMpanlDlciCalldEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-MpaNetworkLinkMIB", "mscMpanlIndex"),
    (0, "Nortel-MsCarrier-MscPassport-MpaNetworkLinkMIB", "mscMpanlDlciIndex"),
)
if mibBuilder.loadTexts:
    mscMpanlDlciCalldEntry.setStatus("mandatory")


class _MscMpanlDlciQ933CallState_Type(Integer32):
    """Custom type mscMpanlDlciQ933CallState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3,
              6,
              9,
              10,
              11,
              12,
              19,
              20)
        )
    )
    namedValues = NamedValues(
        *(("active", 10),
          ("callInitiated", 1),
          ("callPresent", 6),
          ("disconnectIndication", 12),
          ("disconnectRequest", 11),
          ("incomingCallProceeding", 9),
          ("notApplicable", 20),
          ("null", 0),
          ("outgoingCallProceeding", 3),
          ("releaseRequest", 19))
    )


_MscMpanlDlciQ933CallState_Type.__name__ = "Integer32"
_MscMpanlDlciQ933CallState_Object = MibTableColumn
mscMpanlDlciQ933CallState = _MscMpanlDlciQ933CallState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 11, 1, 2),
    _MscMpanlDlciQ933CallState_Type()
)
mscMpanlDlciQ933CallState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciQ933CallState.setStatus("mandatory")


class _MscMpanlDlciQ933CallReference_Type(Unsigned32):
    """Custom type mscMpanlDlciQ933CallReference based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_MscMpanlDlciQ933CallReference_Type.__name__ = "Unsigned32"
_MscMpanlDlciQ933CallReference_Object = MibTableColumn
mscMpanlDlciQ933CallReference = _MscMpanlDlciQ933CallReference_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 11, 1, 3),
    _MscMpanlDlciQ933CallReference_Type()
)
mscMpanlDlciQ933CallReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciQ933CallReference.setStatus("mandatory")
_MscMpanlDlciSpOpTable_Object = MibTable
mscMpanlDlciSpOpTable = _MscMpanlDlciSpOpTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 12)
)
if mibBuilder.loadTexts:
    mscMpanlDlciSpOpTable.setStatus("mandatory")
_MscMpanlDlciSpOpEntry_Object = MibTableRow
mscMpanlDlciSpOpEntry = _MscMpanlDlciSpOpEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 12, 1)
)
mscMpanlDlciSpOpEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-MpaNetworkLinkMIB", "mscMpanlIndex"),
    (0, "Nortel-MsCarrier-MscPassport-MpaNetworkLinkMIB", "mscMpanlDlciIndex"),
)
if mibBuilder.loadTexts:
    mscMpanlDlciSpOpEntry.setStatus("mandatory")


class _MscMpanlDlciMaximumFrameSize_Type(Unsigned32):
    """Custom type mscMpanlDlciMaximumFrameSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_MscMpanlDlciMaximumFrameSize_Type.__name__ = "Unsigned32"
_MscMpanlDlciMaximumFrameSize_Object = MibTableColumn
mscMpanlDlciMaximumFrameSize = _MscMpanlDlciMaximumFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 12, 1, 1),
    _MscMpanlDlciMaximumFrameSize_Type()
)
mscMpanlDlciMaximumFrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciMaximumFrameSize.setStatus("mandatory")


class _MscMpanlDlciCommittedBurstSize_Type(Unsigned32):
    """Custom type mscMpanlDlciCommittedBurstSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50000000),
    )


_MscMpanlDlciCommittedBurstSize_Type.__name__ = "Unsigned32"
_MscMpanlDlciCommittedBurstSize_Object = MibTableColumn
mscMpanlDlciCommittedBurstSize = _MscMpanlDlciCommittedBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 12, 1, 4),
    _MscMpanlDlciCommittedBurstSize_Type()
)
mscMpanlDlciCommittedBurstSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciCommittedBurstSize.setStatus("mandatory")


class _MscMpanlDlciExcessBurstSize_Type(Unsigned32):
    """Custom type mscMpanlDlciExcessBurstSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50000000),
    )


_MscMpanlDlciExcessBurstSize_Type.__name__ = "Unsigned32"
_MscMpanlDlciExcessBurstSize_Object = MibTableColumn
mscMpanlDlciExcessBurstSize = _MscMpanlDlciExcessBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 12, 1, 5),
    _MscMpanlDlciExcessBurstSize_Type()
)
mscMpanlDlciExcessBurstSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciExcessBurstSize.setStatus("mandatory")


class _MscMpanlDlciAccounting_Type(Integer32):
    """Custom type mscMpanlDlciAccounting based on Integer32"""
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


_MscMpanlDlciAccounting_Type.__name__ = "Integer32"
_MscMpanlDlciAccounting_Object = MibTableColumn
mscMpanlDlciAccounting = _MscMpanlDlciAccounting_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 12, 1, 8),
    _MscMpanlDlciAccounting_Type()
)
mscMpanlDlciAccounting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciAccounting.setStatus("mandatory")


class _MscMpanlDlciEmissionPriorityToIf_Type(Integer32):
    """Custom type mscMpanlDlciEmissionPriorityToIf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
        ValueRangeConstraint(3, 3),
    )


_MscMpanlDlciEmissionPriorityToIf_Type.__name__ = "Integer32"
_MscMpanlDlciEmissionPriorityToIf_Object = MibTableColumn
mscMpanlDlciEmissionPriorityToIf = _MscMpanlDlciEmissionPriorityToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 12, 1, 9),
    _MscMpanlDlciEmissionPriorityToIf_Type()
)
mscMpanlDlciEmissionPriorityToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciEmissionPriorityToIf.setStatus("mandatory")


class _MscMpanlDlciTransferPriToNwk_Type(Unsigned32):
    """Custom type mscMpanlDlciTransferPriToNwk based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_MscMpanlDlciTransferPriToNwk_Type.__name__ = "Unsigned32"
_MscMpanlDlciTransferPriToNwk_Object = MibTableColumn
mscMpanlDlciTransferPriToNwk = _MscMpanlDlciTransferPriToNwk_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 12, 1, 10),
    _MscMpanlDlciTransferPriToNwk_Type()
)
mscMpanlDlciTransferPriToNwk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciTransferPriToNwk.setStatus("mandatory")


class _MscMpanlDlciTransferPriFromNwk_Type(Unsigned32):
    """Custom type mscMpanlDlciTransferPriFromNwk based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_MscMpanlDlciTransferPriFromNwk_Type.__name__ = "Unsigned32"
_MscMpanlDlciTransferPriFromNwk_Object = MibTableColumn
mscMpanlDlciTransferPriFromNwk = _MscMpanlDlciTransferPriFromNwk_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 12, 1, 11),
    _MscMpanlDlciTransferPriFromNwk_Type()
)
mscMpanlDlciTransferPriFromNwk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciTransferPriFromNwk.setStatus("mandatory")
_MscMpanlDlciStatsTable_Object = MibTable
mscMpanlDlciStatsTable = _MscMpanlDlciStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 13)
)
if mibBuilder.loadTexts:
    mscMpanlDlciStatsTable.setStatus("mandatory")
_MscMpanlDlciStatsEntry_Object = MibTableRow
mscMpanlDlciStatsEntry = _MscMpanlDlciStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 13, 1)
)
mscMpanlDlciStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-MpaNetworkLinkMIB", "mscMpanlIndex"),
    (0, "Nortel-MsCarrier-MscPassport-MpaNetworkLinkMIB", "mscMpanlDlciIndex"),
)
if mibBuilder.loadTexts:
    mscMpanlDlciStatsEntry.setStatus("mandatory")


class _MscMpanlDlciFrmToIf_Type(Unsigned32):
    """Custom type mscMpanlDlciFrmToIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscMpanlDlciFrmToIf_Type.__name__ = "Unsigned32"
_MscMpanlDlciFrmToIf_Object = MibTableColumn
mscMpanlDlciFrmToIf = _MscMpanlDlciFrmToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 13, 1, 1),
    _MscMpanlDlciFrmToIf_Type()
)
mscMpanlDlciFrmToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciFrmToIf.setStatus("mandatory")


class _MscMpanlDlciFecnFrmToIf_Type(Unsigned32):
    """Custom type mscMpanlDlciFecnFrmToIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscMpanlDlciFecnFrmToIf_Type.__name__ = "Unsigned32"
_MscMpanlDlciFecnFrmToIf_Object = MibTableColumn
mscMpanlDlciFecnFrmToIf = _MscMpanlDlciFecnFrmToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 13, 1, 2),
    _MscMpanlDlciFecnFrmToIf_Type()
)
mscMpanlDlciFecnFrmToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciFecnFrmToIf.setStatus("mandatory")


class _MscMpanlDlciBecnFrmToIf_Type(Unsigned32):
    """Custom type mscMpanlDlciBecnFrmToIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscMpanlDlciBecnFrmToIf_Type.__name__ = "Unsigned32"
_MscMpanlDlciBecnFrmToIf_Object = MibTableColumn
mscMpanlDlciBecnFrmToIf = _MscMpanlDlciBecnFrmToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 13, 1, 3),
    _MscMpanlDlciBecnFrmToIf_Type()
)
mscMpanlDlciBecnFrmToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciBecnFrmToIf.setStatus("mandatory")


class _MscMpanlDlciBciToSubnet_Type(Unsigned32):
    """Custom type mscMpanlDlciBciToSubnet based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscMpanlDlciBciToSubnet_Type.__name__ = "Unsigned32"
_MscMpanlDlciBciToSubnet_Object = MibTableColumn
mscMpanlDlciBciToSubnet = _MscMpanlDlciBciToSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 13, 1, 4),
    _MscMpanlDlciBciToSubnet_Type()
)
mscMpanlDlciBciToSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciBciToSubnet.setStatus("mandatory")


class _MscMpanlDlciDeFrmToIf_Type(Unsigned32):
    """Custom type mscMpanlDlciDeFrmToIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscMpanlDlciDeFrmToIf_Type.__name__ = "Unsigned32"
_MscMpanlDlciDeFrmToIf_Object = MibTableColumn
mscMpanlDlciDeFrmToIf = _MscMpanlDlciDeFrmToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 13, 1, 5),
    _MscMpanlDlciDeFrmToIf_Type()
)
mscMpanlDlciDeFrmToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciDeFrmToIf.setStatus("mandatory")


class _MscMpanlDlciDiscCongestedToIf_Type(Unsigned32):
    """Custom type mscMpanlDlciDiscCongestedToIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscMpanlDlciDiscCongestedToIf_Type.__name__ = "Unsigned32"
_MscMpanlDlciDiscCongestedToIf_Object = MibTableColumn
mscMpanlDlciDiscCongestedToIf = _MscMpanlDlciDiscCongestedToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 13, 1, 6),
    _MscMpanlDlciDiscCongestedToIf_Type()
)
mscMpanlDlciDiscCongestedToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciDiscCongestedToIf.setStatus("mandatory")


class _MscMpanlDlciDiscDeCongestedToIf_Type(Unsigned32):
    """Custom type mscMpanlDlciDiscDeCongestedToIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscMpanlDlciDiscDeCongestedToIf_Type.__name__ = "Unsigned32"
_MscMpanlDlciDiscDeCongestedToIf_Object = MibTableColumn
mscMpanlDlciDiscDeCongestedToIf = _MscMpanlDlciDiscDeCongestedToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 13, 1, 7),
    _MscMpanlDlciDiscDeCongestedToIf_Type()
)
mscMpanlDlciDiscDeCongestedToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciDiscDeCongestedToIf.setStatus("mandatory")


class _MscMpanlDlciFrmFromIf_Type(Unsigned32):
    """Custom type mscMpanlDlciFrmFromIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscMpanlDlciFrmFromIf_Type.__name__ = "Unsigned32"
_MscMpanlDlciFrmFromIf_Object = MibTableColumn
mscMpanlDlciFrmFromIf = _MscMpanlDlciFrmFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 13, 1, 8),
    _MscMpanlDlciFrmFromIf_Type()
)
mscMpanlDlciFrmFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciFrmFromIf.setStatus("mandatory")


class _MscMpanlDlciFecnFrmFromIf_Type(Unsigned32):
    """Custom type mscMpanlDlciFecnFrmFromIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscMpanlDlciFecnFrmFromIf_Type.__name__ = "Unsigned32"
_MscMpanlDlciFecnFrmFromIf_Object = MibTableColumn
mscMpanlDlciFecnFrmFromIf = _MscMpanlDlciFecnFrmFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 13, 1, 9),
    _MscMpanlDlciFecnFrmFromIf_Type()
)
mscMpanlDlciFecnFrmFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciFecnFrmFromIf.setStatus("mandatory")


class _MscMpanlDlciBecnFrmFromIf_Type(Unsigned32):
    """Custom type mscMpanlDlciBecnFrmFromIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscMpanlDlciBecnFrmFromIf_Type.__name__ = "Unsigned32"
_MscMpanlDlciBecnFrmFromIf_Object = MibTableColumn
mscMpanlDlciBecnFrmFromIf = _MscMpanlDlciBecnFrmFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 13, 1, 10),
    _MscMpanlDlciBecnFrmFromIf_Type()
)
mscMpanlDlciBecnFrmFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciBecnFrmFromIf.setStatus("mandatory")


class _MscMpanlDlciFciFromSubnet_Type(Unsigned32):
    """Custom type mscMpanlDlciFciFromSubnet based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscMpanlDlciFciFromSubnet_Type.__name__ = "Unsigned32"
_MscMpanlDlciFciFromSubnet_Object = MibTableColumn
mscMpanlDlciFciFromSubnet = _MscMpanlDlciFciFromSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 13, 1, 11),
    _MscMpanlDlciFciFromSubnet_Type()
)
mscMpanlDlciFciFromSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciFciFromSubnet.setStatus("mandatory")


class _MscMpanlDlciBciFromSubnet_Type(Unsigned32):
    """Custom type mscMpanlDlciBciFromSubnet based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscMpanlDlciBciFromSubnet_Type.__name__ = "Unsigned32"
_MscMpanlDlciBciFromSubnet_Object = MibTableColumn
mscMpanlDlciBciFromSubnet = _MscMpanlDlciBciFromSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 13, 1, 12),
    _MscMpanlDlciBciFromSubnet_Type()
)
mscMpanlDlciBciFromSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciBciFromSubnet.setStatus("mandatory")


class _MscMpanlDlciDeFrmFromIf_Type(Unsigned32):
    """Custom type mscMpanlDlciDeFrmFromIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscMpanlDlciDeFrmFromIf_Type.__name__ = "Unsigned32"
_MscMpanlDlciDeFrmFromIf_Object = MibTableColumn
mscMpanlDlciDeFrmFromIf = _MscMpanlDlciDeFrmFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 13, 1, 13),
    _MscMpanlDlciDeFrmFromIf_Type()
)
mscMpanlDlciDeFrmFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciDeFrmFromIf.setStatus("mandatory")


class _MscMpanlDlciExcessFrmFromIf_Type(Unsigned32):
    """Custom type mscMpanlDlciExcessFrmFromIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscMpanlDlciExcessFrmFromIf_Type.__name__ = "Unsigned32"
_MscMpanlDlciExcessFrmFromIf_Object = MibTableColumn
mscMpanlDlciExcessFrmFromIf = _MscMpanlDlciExcessFrmFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 13, 1, 14),
    _MscMpanlDlciExcessFrmFromIf_Type()
)
mscMpanlDlciExcessFrmFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciExcessFrmFromIf.setStatus("mandatory")


class _MscMpanlDlciDiscExcessFromIf_Type(Unsigned32):
    """Custom type mscMpanlDlciDiscExcessFromIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscMpanlDlciDiscExcessFromIf_Type.__name__ = "Unsigned32"
_MscMpanlDlciDiscExcessFromIf_Object = MibTableColumn
mscMpanlDlciDiscExcessFromIf = _MscMpanlDlciDiscExcessFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 13, 1, 15),
    _MscMpanlDlciDiscExcessFromIf_Type()
)
mscMpanlDlciDiscExcessFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciDiscExcessFromIf.setStatus("mandatory")


class _MscMpanlDlciDiscFrameAbit_Type(Unsigned32):
    """Custom type mscMpanlDlciDiscFrameAbit based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscMpanlDlciDiscFrameAbit_Type.__name__ = "Unsigned32"
_MscMpanlDlciDiscFrameAbit_Object = MibTableColumn
mscMpanlDlciDiscFrameAbit = _MscMpanlDlciDiscFrameAbit_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 13, 1, 16),
    _MscMpanlDlciDiscFrameAbit_Type()
)
mscMpanlDlciDiscFrameAbit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciDiscFrameAbit.setStatus("mandatory")


class _MscMpanlDlciDiscCongestedFromIf_Type(Unsigned32):
    """Custom type mscMpanlDlciDiscCongestedFromIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscMpanlDlciDiscCongestedFromIf_Type.__name__ = "Unsigned32"
_MscMpanlDlciDiscCongestedFromIf_Object = MibTableColumn
mscMpanlDlciDiscCongestedFromIf = _MscMpanlDlciDiscCongestedFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 13, 1, 17),
    _MscMpanlDlciDiscCongestedFromIf_Type()
)
mscMpanlDlciDiscCongestedFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciDiscCongestedFromIf.setStatus("mandatory")


class _MscMpanlDlciDiscDeCongestedFromIf_Type(Unsigned32):
    """Custom type mscMpanlDlciDiscDeCongestedFromIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscMpanlDlciDiscDeCongestedFromIf_Type.__name__ = "Unsigned32"
_MscMpanlDlciDiscDeCongestedFromIf_Object = MibTableColumn
mscMpanlDlciDiscDeCongestedFromIf = _MscMpanlDlciDiscDeCongestedFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 13, 1, 18),
    _MscMpanlDlciDiscDeCongestedFromIf_Type()
)
mscMpanlDlciDiscDeCongestedFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciDiscDeCongestedFromIf.setStatus("mandatory")


class _MscMpanlDlciErrorShortFrmFromIf_Type(Unsigned32):
    """Custom type mscMpanlDlciErrorShortFrmFromIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscMpanlDlciErrorShortFrmFromIf_Type.__name__ = "Unsigned32"
_MscMpanlDlciErrorShortFrmFromIf_Object = MibTableColumn
mscMpanlDlciErrorShortFrmFromIf = _MscMpanlDlciErrorShortFrmFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 13, 1, 19),
    _MscMpanlDlciErrorShortFrmFromIf_Type()
)
mscMpanlDlciErrorShortFrmFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciErrorShortFrmFromIf.setStatus("mandatory")


class _MscMpanlDlciErrorLongFrmFromIf_Type(Unsigned32):
    """Custom type mscMpanlDlciErrorLongFrmFromIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscMpanlDlciErrorLongFrmFromIf_Type.__name__ = "Unsigned32"
_MscMpanlDlciErrorLongFrmFromIf_Object = MibTableColumn
mscMpanlDlciErrorLongFrmFromIf = _MscMpanlDlciErrorLongFrmFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 13, 1, 20),
    _MscMpanlDlciErrorLongFrmFromIf_Type()
)
mscMpanlDlciErrorLongFrmFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciErrorLongFrmFromIf.setStatus("mandatory")


class _MscMpanlDlciBecnFrmSetByService_Type(Unsigned32):
    """Custom type mscMpanlDlciBecnFrmSetByService based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscMpanlDlciBecnFrmSetByService_Type.__name__ = "Unsigned32"
_MscMpanlDlciBecnFrmSetByService_Object = MibTableColumn
mscMpanlDlciBecnFrmSetByService = _MscMpanlDlciBecnFrmSetByService_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 13, 1, 21),
    _MscMpanlDlciBecnFrmSetByService_Type()
)
mscMpanlDlciBecnFrmSetByService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciBecnFrmSetByService.setStatus("mandatory")


class _MscMpanlDlciBytesToIf_Type(Unsigned32):
    """Custom type mscMpanlDlciBytesToIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscMpanlDlciBytesToIf_Type.__name__ = "Unsigned32"
_MscMpanlDlciBytesToIf_Object = MibTableColumn
mscMpanlDlciBytesToIf = _MscMpanlDlciBytesToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 13, 1, 22),
    _MscMpanlDlciBytesToIf_Type()
)
mscMpanlDlciBytesToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciBytesToIf.setStatus("mandatory")


class _MscMpanlDlciDeBytesToIf_Type(Unsigned32):
    """Custom type mscMpanlDlciDeBytesToIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscMpanlDlciDeBytesToIf_Type.__name__ = "Unsigned32"
_MscMpanlDlciDeBytesToIf_Object = MibTableColumn
mscMpanlDlciDeBytesToIf = _MscMpanlDlciDeBytesToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 13, 1, 23),
    _MscMpanlDlciDeBytesToIf_Type()
)
mscMpanlDlciDeBytesToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciDeBytesToIf.setStatus("mandatory")


class _MscMpanlDlciDiscCongestedToIfBytes_Type(Unsigned32):
    """Custom type mscMpanlDlciDiscCongestedToIfBytes based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscMpanlDlciDiscCongestedToIfBytes_Type.__name__ = "Unsigned32"
_MscMpanlDlciDiscCongestedToIfBytes_Object = MibTableColumn
mscMpanlDlciDiscCongestedToIfBytes = _MscMpanlDlciDiscCongestedToIfBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 13, 1, 24),
    _MscMpanlDlciDiscCongestedToIfBytes_Type()
)
mscMpanlDlciDiscCongestedToIfBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciDiscCongestedToIfBytes.setStatus("mandatory")


class _MscMpanlDlciDiscDeCongestedToIfBytes_Type(Unsigned32):
    """Custom type mscMpanlDlciDiscDeCongestedToIfBytes based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscMpanlDlciDiscDeCongestedToIfBytes_Type.__name__ = "Unsigned32"
_MscMpanlDlciDiscDeCongestedToIfBytes_Object = MibTableColumn
mscMpanlDlciDiscDeCongestedToIfBytes = _MscMpanlDlciDiscDeCongestedToIfBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 13, 1, 25),
    _MscMpanlDlciDiscDeCongestedToIfBytes_Type()
)
mscMpanlDlciDiscDeCongestedToIfBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciDiscDeCongestedToIfBytes.setStatus("mandatory")


class _MscMpanlDlciBytesFromIf_Type(Unsigned32):
    """Custom type mscMpanlDlciBytesFromIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscMpanlDlciBytesFromIf_Type.__name__ = "Unsigned32"
_MscMpanlDlciBytesFromIf_Object = MibTableColumn
mscMpanlDlciBytesFromIf = _MscMpanlDlciBytesFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 13, 1, 26),
    _MscMpanlDlciBytesFromIf_Type()
)
mscMpanlDlciBytesFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciBytesFromIf.setStatus("mandatory")


class _MscMpanlDlciDeBytesFromIf_Type(Unsigned32):
    """Custom type mscMpanlDlciDeBytesFromIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscMpanlDlciDeBytesFromIf_Type.__name__ = "Unsigned32"
_MscMpanlDlciDeBytesFromIf_Object = MibTableColumn
mscMpanlDlciDeBytesFromIf = _MscMpanlDlciDeBytesFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 13, 1, 27),
    _MscMpanlDlciDeBytesFromIf_Type()
)
mscMpanlDlciDeBytesFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciDeBytesFromIf.setStatus("mandatory")


class _MscMpanlDlciExcessBytesFromIf_Type(Unsigned32):
    """Custom type mscMpanlDlciExcessBytesFromIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscMpanlDlciExcessBytesFromIf_Type.__name__ = "Unsigned32"
_MscMpanlDlciExcessBytesFromIf_Object = MibTableColumn
mscMpanlDlciExcessBytesFromIf = _MscMpanlDlciExcessBytesFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 13, 1, 28),
    _MscMpanlDlciExcessBytesFromIf_Type()
)
mscMpanlDlciExcessBytesFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciExcessBytesFromIf.setStatus("mandatory")


class _MscMpanlDlciDiscExcessFromIfBytes_Type(Unsigned32):
    """Custom type mscMpanlDlciDiscExcessFromIfBytes based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscMpanlDlciDiscExcessFromIfBytes_Type.__name__ = "Unsigned32"
_MscMpanlDlciDiscExcessFromIfBytes_Object = MibTableColumn
mscMpanlDlciDiscExcessFromIfBytes = _MscMpanlDlciDiscExcessFromIfBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 13, 1, 29),
    _MscMpanlDlciDiscExcessFromIfBytes_Type()
)
mscMpanlDlciDiscExcessFromIfBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciDiscExcessFromIfBytes.setStatus("mandatory")


class _MscMpanlDlciDiscByteAbit_Type(Unsigned32):
    """Custom type mscMpanlDlciDiscByteAbit based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscMpanlDlciDiscByteAbit_Type.__name__ = "Unsigned32"
_MscMpanlDlciDiscByteAbit_Object = MibTableColumn
mscMpanlDlciDiscByteAbit = _MscMpanlDlciDiscByteAbit_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 13, 1, 30),
    _MscMpanlDlciDiscByteAbit_Type()
)
mscMpanlDlciDiscByteAbit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciDiscByteAbit.setStatus("mandatory")


class _MscMpanlDlciDiscCongestedFromIfBytes_Type(Unsigned32):
    """Custom type mscMpanlDlciDiscCongestedFromIfBytes based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscMpanlDlciDiscCongestedFromIfBytes_Type.__name__ = "Unsigned32"
_MscMpanlDlciDiscCongestedFromIfBytes_Object = MibTableColumn
mscMpanlDlciDiscCongestedFromIfBytes = _MscMpanlDlciDiscCongestedFromIfBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 13, 1, 31),
    _MscMpanlDlciDiscCongestedFromIfBytes_Type()
)
mscMpanlDlciDiscCongestedFromIfBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciDiscCongestedFromIfBytes.setStatus("mandatory")


class _MscMpanlDlciDiscDeCongestedFromIfBytes_Type(Unsigned32):
    """Custom type mscMpanlDlciDiscDeCongestedFromIfBytes based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscMpanlDlciDiscDeCongestedFromIfBytes_Type.__name__ = "Unsigned32"
_MscMpanlDlciDiscDeCongestedFromIfBytes_Object = MibTableColumn
mscMpanlDlciDiscDeCongestedFromIfBytes = _MscMpanlDlciDiscDeCongestedFromIfBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 13, 1, 32),
    _MscMpanlDlciDiscDeCongestedFromIfBytes_Type()
)
mscMpanlDlciDiscDeCongestedFromIfBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciDiscDeCongestedFromIfBytes.setStatus("mandatory")


class _MscMpanlDlciErrorLongBytesFromIf_Type(Unsigned32):
    """Custom type mscMpanlDlciErrorLongBytesFromIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscMpanlDlciErrorLongBytesFromIf_Type.__name__ = "Unsigned32"
_MscMpanlDlciErrorLongBytesFromIf_Object = MibTableColumn
mscMpanlDlciErrorLongBytesFromIf = _MscMpanlDlciErrorLongBytesFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 13, 1, 34),
    _MscMpanlDlciErrorLongBytesFromIf_Type()
)
mscMpanlDlciErrorLongBytesFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciErrorLongBytesFromIf.setStatus("mandatory")


class _MscMpanlDlciTransferPriorityToNetwork_Type(Integer32):
    """Custom type mscMpanlDlciTransferPriorityToNetwork based on Integer32"""
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
              12,
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("n0", 0),
          ("n1", 1),
          ("n10", 10),
          ("n11", 11),
          ("n12", 12),
          ("n13", 13),
          ("n14", 14),
          ("n15", 15),
          ("n2", 2),
          ("n3", 3),
          ("n4", 4),
          ("n5", 5),
          ("n6", 6),
          ("n7", 7),
          ("n8", 8),
          ("n9", 9))
    )


_MscMpanlDlciTransferPriorityToNetwork_Type.__name__ = "Integer32"
_MscMpanlDlciTransferPriorityToNetwork_Object = MibTableColumn
mscMpanlDlciTransferPriorityToNetwork = _MscMpanlDlciTransferPriorityToNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 13, 1, 37),
    _MscMpanlDlciTransferPriorityToNetwork_Type()
)
mscMpanlDlciTransferPriorityToNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciTransferPriorityToNetwork.setStatus("obsolete")


class _MscMpanlDlciTransferPriorityFromNetwork_Type(Integer32):
    """Custom type mscMpanlDlciTransferPriorityFromNetwork based on Integer32"""
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
              12,
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("n0", 0),
          ("n1", 1),
          ("n10", 10),
          ("n11", 11),
          ("n12", 12),
          ("n13", 13),
          ("n14", 14),
          ("n15", 15),
          ("n2", 2),
          ("n3", 3),
          ("n4", 4),
          ("n5", 5),
          ("n6", 6),
          ("n7", 7),
          ("n8", 8),
          ("n9", 9))
    )


_MscMpanlDlciTransferPriorityFromNetwork_Type.__name__ = "Integer32"
_MscMpanlDlciTransferPriorityFromNetwork_Object = MibTableColumn
mscMpanlDlciTransferPriorityFromNetwork = _MscMpanlDlciTransferPriorityFromNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 13, 1, 38),
    _MscMpanlDlciTransferPriorityFromNetwork_Type()
)
mscMpanlDlciTransferPriorityFromNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciTransferPriorityFromNetwork.setStatus("obsolete")
_MscMpanlDlciIntTable_Object = MibTable
mscMpanlDlciIntTable = _MscMpanlDlciIntTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 14)
)
if mibBuilder.loadTexts:
    mscMpanlDlciIntTable.setStatus("mandatory")
_MscMpanlDlciIntEntry_Object = MibTableRow
mscMpanlDlciIntEntry = _MscMpanlDlciIntEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 14, 1)
)
mscMpanlDlciIntEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-MpaNetworkLinkMIB", "mscMpanlIndex"),
    (0, "Nortel-MsCarrier-MscPassport-MpaNetworkLinkMIB", "mscMpanlDlciIndex"),
)
if mibBuilder.loadTexts:
    mscMpanlDlciIntEntry.setStatus("mandatory")


class _MscMpanlDlciStartTime_Type(EnterpriseDateAndTime):
    """Custom type mscMpanlDlciStartTime based on EnterpriseDateAndTime"""
    subtypeSpec = EnterpriseDateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(19, 19),
    )


_MscMpanlDlciStartTime_Type.__name__ = "EnterpriseDateAndTime"
_MscMpanlDlciStartTime_Object = MibTableColumn
mscMpanlDlciStartTime = _MscMpanlDlciStartTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 14, 1, 1),
    _MscMpanlDlciStartTime_Type()
)
mscMpanlDlciStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciStartTime.setStatus("mandatory")


class _MscMpanlDlciTotalIngressBytes_Type(Unsigned64):
    """Custom type mscMpanlDlciTotalIngressBytes based on Unsigned64"""
    subtypeSpec = Unsigned64.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_MscMpanlDlciTotalIngressBytes_Type.__name__ = "Unsigned64"
_MscMpanlDlciTotalIngressBytes_Object = MibTableColumn
mscMpanlDlciTotalIngressBytes = _MscMpanlDlciTotalIngressBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 14, 1, 2),
    _MscMpanlDlciTotalIngressBytes_Type()
)
mscMpanlDlciTotalIngressBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciTotalIngressBytes.setStatus("mandatory")


class _MscMpanlDlciTotalEgressBytes_Type(Unsigned64):
    """Custom type mscMpanlDlciTotalEgressBytes based on Unsigned64"""
    subtypeSpec = Unsigned64.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_MscMpanlDlciTotalEgressBytes_Type.__name__ = "Unsigned64"
_MscMpanlDlciTotalEgressBytes_Object = MibTableColumn
mscMpanlDlciTotalEgressBytes = _MscMpanlDlciTotalEgressBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 14, 1, 3),
    _MscMpanlDlciTotalEgressBytes_Type()
)
mscMpanlDlciTotalEgressBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciTotalEgressBytes.setStatus("mandatory")


class _MscMpanlDlciEirIngressBytes_Type(Unsigned64):
    """Custom type mscMpanlDlciEirIngressBytes based on Unsigned64"""
    subtypeSpec = Unsigned64.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_MscMpanlDlciEirIngressBytes_Type.__name__ = "Unsigned64"
_MscMpanlDlciEirIngressBytes_Object = MibTableColumn
mscMpanlDlciEirIngressBytes = _MscMpanlDlciEirIngressBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 14, 1, 4),
    _MscMpanlDlciEirIngressBytes_Type()
)
mscMpanlDlciEirIngressBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciEirIngressBytes.setStatus("mandatory")


class _MscMpanlDlciEirEgressBytes_Type(Unsigned64):
    """Custom type mscMpanlDlciEirEgressBytes based on Unsigned64"""
    subtypeSpec = Unsigned64.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_MscMpanlDlciEirEgressBytes_Type.__name__ = "Unsigned64"
_MscMpanlDlciEirEgressBytes_Object = MibTableColumn
mscMpanlDlciEirEgressBytes = _MscMpanlDlciEirEgressBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 14, 1, 5),
    _MscMpanlDlciEirEgressBytes_Type()
)
mscMpanlDlciEirEgressBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciEirEgressBytes.setStatus("mandatory")


class _MscMpanlDlciDiscardedBytes_Type(Unsigned64):
    """Custom type mscMpanlDlciDiscardedBytes based on Unsigned64"""
    subtypeSpec = Unsigned64.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_MscMpanlDlciDiscardedBytes_Type.__name__ = "Unsigned64"
_MscMpanlDlciDiscardedBytes_Object = MibTableColumn
mscMpanlDlciDiscardedBytes = _MscMpanlDlciDiscardedBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 14, 1, 6),
    _MscMpanlDlciDiscardedBytes_Type()
)
mscMpanlDlciDiscardedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciDiscardedBytes.setStatus("mandatory")


class _MscMpanlDlciTotalIngressSegFrm_Type(Unsigned32):
    """Custom type mscMpanlDlciTotalIngressSegFrm based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscMpanlDlciTotalIngressSegFrm_Type.__name__ = "Unsigned32"
_MscMpanlDlciTotalIngressSegFrm_Object = MibTableColumn
mscMpanlDlciTotalIngressSegFrm = _MscMpanlDlciTotalIngressSegFrm_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 14, 1, 7),
    _MscMpanlDlciTotalIngressSegFrm_Type()
)
mscMpanlDlciTotalIngressSegFrm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciTotalIngressSegFrm.setStatus("mandatory")


class _MscMpanlDlciTotalEgressSegFrm_Type(Unsigned32):
    """Custom type mscMpanlDlciTotalEgressSegFrm based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscMpanlDlciTotalEgressSegFrm_Type.__name__ = "Unsigned32"
_MscMpanlDlciTotalEgressSegFrm_Object = MibTableColumn
mscMpanlDlciTotalEgressSegFrm = _MscMpanlDlciTotalEgressSegFrm_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 14, 1, 8),
    _MscMpanlDlciTotalEgressSegFrm_Type()
)
mscMpanlDlciTotalEgressSegFrm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciTotalEgressSegFrm.setStatus("mandatory")


class _MscMpanlDlciEirIngressSegFrm_Type(Unsigned32):
    """Custom type mscMpanlDlciEirIngressSegFrm based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscMpanlDlciEirIngressSegFrm_Type.__name__ = "Unsigned32"
_MscMpanlDlciEirIngressSegFrm_Object = MibTableColumn
mscMpanlDlciEirIngressSegFrm = _MscMpanlDlciEirIngressSegFrm_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 14, 1, 9),
    _MscMpanlDlciEirIngressSegFrm_Type()
)
mscMpanlDlciEirIngressSegFrm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciEirIngressSegFrm.setStatus("mandatory")


class _MscMpanlDlciEirEgressSegFrm_Type(Unsigned32):
    """Custom type mscMpanlDlciEirEgressSegFrm based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscMpanlDlciEirEgressSegFrm_Type.__name__ = "Unsigned32"
_MscMpanlDlciEirEgressSegFrm_Object = MibTableColumn
mscMpanlDlciEirEgressSegFrm = _MscMpanlDlciEirEgressSegFrm_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 14, 1, 10),
    _MscMpanlDlciEirEgressSegFrm_Type()
)
mscMpanlDlciEirEgressSegFrm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciEirEgressSegFrm.setStatus("mandatory")


class _MscMpanlDlciDiscardedSegFrm_Type(Unsigned32):
    """Custom type mscMpanlDlciDiscardedSegFrm based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscMpanlDlciDiscardedSegFrm_Type.__name__ = "Unsigned32"
_MscMpanlDlciDiscardedSegFrm_Object = MibTableColumn
mscMpanlDlciDiscardedSegFrm = _MscMpanlDlciDiscardedSegFrm_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 14, 1, 11),
    _MscMpanlDlciDiscardedSegFrm_Type()
)
mscMpanlDlciDiscardedSegFrm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciDiscardedSegFrm.setStatus("mandatory")


class _MscMpanlDlciCallReferenceNumber_Type(Unsigned32):
    """Custom type mscMpanlDlciCallReferenceNumber based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscMpanlDlciCallReferenceNumber_Type.__name__ = "Unsigned32"
_MscMpanlDlciCallReferenceNumber_Object = MibTableColumn
mscMpanlDlciCallReferenceNumber = _MscMpanlDlciCallReferenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 14, 1, 17),
    _MscMpanlDlciCallReferenceNumber_Type()
)
mscMpanlDlciCallReferenceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciCallReferenceNumber.setStatus("mandatory")


class _MscMpanlDlciElapsedDifference_Type(Unsigned32):
    """Custom type mscMpanlDlciElapsedDifference based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscMpanlDlciElapsedDifference_Type.__name__ = "Unsigned32"
_MscMpanlDlciElapsedDifference_Object = MibTableColumn
mscMpanlDlciElapsedDifference = _MscMpanlDlciElapsedDifference_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 14, 1, 18),
    _MscMpanlDlciElapsedDifference_Type()
)
mscMpanlDlciElapsedDifference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciElapsedDifference.setStatus("mandatory")
_MscMpanlDlciAbitTable_Object = MibTable
mscMpanlDlciAbitTable = _MscMpanlDlciAbitTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 15)
)
if mibBuilder.loadTexts:
    mscMpanlDlciAbitTable.setStatus("mandatory")
_MscMpanlDlciAbitEntry_Object = MibTableRow
mscMpanlDlciAbitEntry = _MscMpanlDlciAbitEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 15, 1)
)
mscMpanlDlciAbitEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-MpaNetworkLinkMIB", "mscMpanlIndex"),
    (0, "Nortel-MsCarrier-MscPassport-MpaNetworkLinkMIB", "mscMpanlDlciIndex"),
)
if mibBuilder.loadTexts:
    mscMpanlDlciAbitEntry.setStatus("mandatory")


class _MscMpanlDlciABitStatusToIf_Type(Integer32):
    """Custom type mscMpanlDlciABitStatusToIf based on Integer32"""
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
          ("inactive", 0),
          ("notApplicable", 2))
    )


_MscMpanlDlciABitStatusToIf_Type.__name__ = "Integer32"
_MscMpanlDlciABitStatusToIf_Object = MibTableColumn
mscMpanlDlciABitStatusToIf = _MscMpanlDlciABitStatusToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 15, 1, 1),
    _MscMpanlDlciABitStatusToIf_Type()
)
mscMpanlDlciABitStatusToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciABitStatusToIf.setStatus("mandatory")


class _MscMpanlDlciABitReasonToIf_Type(Integer32):
    """Custom type mscMpanlDlciABitReasonToIf based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("remoteLinkDown", 5),
          ("remoteLmiError", 3),
          ("remoteUserSignaled", 1),
          ("vcDown", 6))
    )


_MscMpanlDlciABitReasonToIf_Type.__name__ = "Integer32"
_MscMpanlDlciABitReasonToIf_Object = MibTableColumn
mscMpanlDlciABitReasonToIf = _MscMpanlDlciABitReasonToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 15, 1, 2),
    _MscMpanlDlciABitReasonToIf_Type()
)
mscMpanlDlciABitReasonToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciABitReasonToIf.setStatus("mandatory")


class _MscMpanlDlciABitStatusFromIf_Type(Integer32):
    """Custom type mscMpanlDlciABitStatusFromIf based on Integer32"""
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
          ("inactive", 0),
          ("notApplicable", 2))
    )


_MscMpanlDlciABitStatusFromIf_Type.__name__ = "Integer32"
_MscMpanlDlciABitStatusFromIf_Object = MibTableColumn
mscMpanlDlciABitStatusFromIf = _MscMpanlDlciABitStatusFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 15, 1, 3),
    _MscMpanlDlciABitStatusFromIf_Type()
)
mscMpanlDlciABitStatusFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciABitStatusFromIf.setStatus("mandatory")


class _MscMpanlDlciABitReasonFromIf_Type(Integer32):
    """Custom type mscMpanlDlciABitReasonFromIf based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("remoteLinkDown", 5),
          ("remoteLmiError", 3),
          ("remoteUserSignaled", 1),
          ("vcDown", 6))
    )


_MscMpanlDlciABitReasonFromIf_Type.__name__ = "Integer32"
_MscMpanlDlciABitReasonFromIf_Object = MibTableColumn
mscMpanlDlciABitReasonFromIf = _MscMpanlDlciABitReasonFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 15, 1, 4),
    _MscMpanlDlciABitReasonFromIf_Type()
)
mscMpanlDlciABitReasonFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciABitReasonFromIf.setStatus("mandatory")


class _MscMpanlDlciLoopbackState_Type(Integer32):
    """Custom type mscMpanlDlciLoopbackState based on Integer32"""
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


_MscMpanlDlciLoopbackState_Type.__name__ = "Integer32"
_MscMpanlDlciLoopbackState_Object = MibTableColumn
mscMpanlDlciLoopbackState = _MscMpanlDlciLoopbackState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 5, 15, 1, 5),
    _MscMpanlDlciLoopbackState_Type()
)
mscMpanlDlciLoopbackState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlDlciLoopbackState.setStatus("mandatory")
_MscMpanlSig_ObjectIdentity = ObjectIdentity
mscMpanlSig = _MscMpanlSig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 6)
)
_MscMpanlSigRowStatusTable_Object = MibTable
mscMpanlSigRowStatusTable = _MscMpanlSigRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 6, 1)
)
if mibBuilder.loadTexts:
    mscMpanlSigRowStatusTable.setStatus("mandatory")
_MscMpanlSigRowStatusEntry_Object = MibTableRow
mscMpanlSigRowStatusEntry = _MscMpanlSigRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 6, 1, 1)
)
mscMpanlSigRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-MpaNetworkLinkMIB", "mscMpanlIndex"),
    (0, "Nortel-MsCarrier-MscPassport-MpaNetworkLinkMIB", "mscMpanlSigIndex"),
)
if mibBuilder.loadTexts:
    mscMpanlSigRowStatusEntry.setStatus("mandatory")
_MscMpanlSigRowStatus_Type = RowStatus
_MscMpanlSigRowStatus_Object = MibTableColumn
mscMpanlSigRowStatus = _MscMpanlSigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 6, 1, 1, 1),
    _MscMpanlSigRowStatus_Type()
)
mscMpanlSigRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlSigRowStatus.setStatus("mandatory")
_MscMpanlSigComponentName_Type = DisplayString
_MscMpanlSigComponentName_Object = MibTableColumn
mscMpanlSigComponentName = _MscMpanlSigComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 6, 1, 1, 2),
    _MscMpanlSigComponentName_Type()
)
mscMpanlSigComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlSigComponentName.setStatus("mandatory")
_MscMpanlSigStorageType_Type = StorageType
_MscMpanlSigStorageType_Object = MibTableColumn
mscMpanlSigStorageType = _MscMpanlSigStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 6, 1, 1, 4),
    _MscMpanlSigStorageType_Type()
)
mscMpanlSigStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlSigStorageType.setStatus("mandatory")
_MscMpanlSigIndex_Type = NonReplicated
_MscMpanlSigIndex_Object = MibTableColumn
mscMpanlSigIndex = _MscMpanlSigIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 6, 1, 1, 10),
    _MscMpanlSigIndex_Type()
)
mscMpanlSigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscMpanlSigIndex.setStatus("mandatory")
_MscMpanlSigSysParmsTable_Object = MibTable
mscMpanlSigSysParmsTable = _MscMpanlSigSysParmsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 6, 13)
)
if mibBuilder.loadTexts:
    mscMpanlSigSysParmsTable.setStatus("mandatory")
_MscMpanlSigSysParmsEntry_Object = MibTableRow
mscMpanlSigSysParmsEntry = _MscMpanlSigSysParmsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 6, 13, 1)
)
mscMpanlSigSysParmsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-MpaNetworkLinkMIB", "mscMpanlIndex"),
    (0, "Nortel-MsCarrier-MscPassport-MpaNetworkLinkMIB", "mscMpanlSigIndex"),
)
if mibBuilder.loadTexts:
    mscMpanlSigSysParmsEntry.setStatus("mandatory")


class _MscMpanlSigCallSetupTimer_Type(Unsigned32):
    """Custom type mscMpanlSigCallSetupTimer based on Unsigned32"""
    defaultValue = 4

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_MscMpanlSigCallSetupTimer_Type.__name__ = "Unsigned32"
_MscMpanlSigCallSetupTimer_Object = MibTableColumn
mscMpanlSigCallSetupTimer = _MscMpanlSigCallSetupTimer_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 6, 13, 1, 1),
    _MscMpanlSigCallSetupTimer_Type()
)
mscMpanlSigCallSetupTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscMpanlSigCallSetupTimer.setStatus("mandatory")


class _MscMpanlSigDisconnectTimer_Type(Unsigned32):
    """Custom type mscMpanlSigDisconnectTimer based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_MscMpanlSigDisconnectTimer_Type.__name__ = "Unsigned32"
_MscMpanlSigDisconnectTimer_Object = MibTableColumn
mscMpanlSigDisconnectTimer = _MscMpanlSigDisconnectTimer_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 6, 13, 1, 2),
    _MscMpanlSigDisconnectTimer_Type()
)
mscMpanlSigDisconnectTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscMpanlSigDisconnectTimer.setStatus("mandatory")


class _MscMpanlSigReleaseTimer_Type(Unsigned32):
    """Custom type mscMpanlSigReleaseTimer based on Unsigned32"""
    defaultValue = 4

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_MscMpanlSigReleaseTimer_Type.__name__ = "Unsigned32"
_MscMpanlSigReleaseTimer_Object = MibTableColumn
mscMpanlSigReleaseTimer = _MscMpanlSigReleaseTimer_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 6, 13, 1, 3),
    _MscMpanlSigReleaseTimer_Type()
)
mscMpanlSigReleaseTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscMpanlSigReleaseTimer.setStatus("mandatory")


class _MscMpanlSigCallProceedingTimer_Type(Unsigned32):
    """Custom type mscMpanlSigCallProceedingTimer based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_MscMpanlSigCallProceedingTimer_Type.__name__ = "Unsigned32"
_MscMpanlSigCallProceedingTimer_Object = MibTableColumn
mscMpanlSigCallProceedingTimer = _MscMpanlSigCallProceedingTimer_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 6, 13, 1, 4),
    _MscMpanlSigCallProceedingTimer_Type()
)
mscMpanlSigCallProceedingTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscMpanlSigCallProceedingTimer.setStatus("mandatory")


class _MscMpanlSigNetworkType_Type(Integer32):
    """Custom type mscMpanlSigNetworkType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("private", 1),
          ("public", 2))
    )


_MscMpanlSigNetworkType_Type.__name__ = "Integer32"
_MscMpanlSigNetworkType_Object = MibTableColumn
mscMpanlSigNetworkType = _MscMpanlSigNetworkType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 6, 13, 1, 5),
    _MscMpanlSigNetworkType_Type()
)
mscMpanlSigNetworkType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscMpanlSigNetworkType.setStatus("mandatory")
_MscMpanlSigLapfSysTable_Object = MibTable
mscMpanlSigLapfSysTable = _MscMpanlSigLapfSysTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 6, 14)
)
if mibBuilder.loadTexts:
    mscMpanlSigLapfSysTable.setStatus("mandatory")
_MscMpanlSigLapfSysEntry_Object = MibTableRow
mscMpanlSigLapfSysEntry = _MscMpanlSigLapfSysEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 6, 14, 1)
)
mscMpanlSigLapfSysEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-MpaNetworkLinkMIB", "mscMpanlIndex"),
    (0, "Nortel-MsCarrier-MscPassport-MpaNetworkLinkMIB", "mscMpanlSigIndex"),
)
if mibBuilder.loadTexts:
    mscMpanlSigLapfSysEntry.setStatus("mandatory")


class _MscMpanlSigWindowSize_Type(Unsigned32):
    """Custom type mscMpanlSigWindowSize based on Unsigned32"""
    defaultValue = 7

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_MscMpanlSigWindowSize_Type.__name__ = "Unsigned32"
_MscMpanlSigWindowSize_Object = MibTableColumn
mscMpanlSigWindowSize = _MscMpanlSigWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 6, 14, 1, 2),
    _MscMpanlSigWindowSize_Type()
)
mscMpanlSigWindowSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscMpanlSigWindowSize.setStatus("mandatory")


class _MscMpanlSigRetransmitLimit_Type(Unsigned32):
    """Custom type mscMpanlSigRetransmitLimit based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_MscMpanlSigRetransmitLimit_Type.__name__ = "Unsigned32"
_MscMpanlSigRetransmitLimit_Object = MibTableColumn
mscMpanlSigRetransmitLimit = _MscMpanlSigRetransmitLimit_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 6, 14, 1, 3),
    _MscMpanlSigRetransmitLimit_Type()
)
mscMpanlSigRetransmitLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscMpanlSigRetransmitLimit.setStatus("mandatory")


class _MscMpanlSigAckTimer_Type(Unsigned32):
    """Custom type mscMpanlSigAckTimer based on Unsigned32"""
    defaultValue = 1500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 10000),
    )


_MscMpanlSigAckTimer_Type.__name__ = "Unsigned32"
_MscMpanlSigAckTimer_Object = MibTableColumn
mscMpanlSigAckTimer = _MscMpanlSigAckTimer_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 6, 14, 1, 4),
    _MscMpanlSigAckTimer_Type()
)
mscMpanlSigAckTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscMpanlSigAckTimer.setStatus("mandatory")


class _MscMpanlSigAckDelayTimer_Type(Unsigned32):
    """Custom type mscMpanlSigAckDelayTimer based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_MscMpanlSigAckDelayTimer_Type.__name__ = "Unsigned32"
_MscMpanlSigAckDelayTimer_Object = MibTableColumn
mscMpanlSigAckDelayTimer = _MscMpanlSigAckDelayTimer_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 6, 14, 1, 5),
    _MscMpanlSigAckDelayTimer_Type()
)
mscMpanlSigAckDelayTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscMpanlSigAckDelayTimer.setStatus("mandatory")


class _MscMpanlSigIdleProbeTimer_Type(Unsigned32):
    """Custom type mscMpanlSigIdleProbeTimer based on Unsigned32"""
    defaultValue = 30000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 65535000),
    )


_MscMpanlSigIdleProbeTimer_Type.__name__ = "Unsigned32"
_MscMpanlSigIdleProbeTimer_Object = MibTableColumn
mscMpanlSigIdleProbeTimer = _MscMpanlSigIdleProbeTimer_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 6, 14, 1, 6),
    _MscMpanlSigIdleProbeTimer_Type()
)
mscMpanlSigIdleProbeTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscMpanlSigIdleProbeTimer.setStatus("mandatory")
_MscMpanlSigSvcaccTable_Object = MibTable
mscMpanlSigSvcaccTable = _MscMpanlSigSvcaccTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 6, 15)
)
if mibBuilder.loadTexts:
    mscMpanlSigSvcaccTable.setStatus("mandatory")
_MscMpanlSigSvcaccEntry_Object = MibTableRow
mscMpanlSigSvcaccEntry = _MscMpanlSigSvcaccEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 6, 15, 1)
)
mscMpanlSigSvcaccEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-MpaNetworkLinkMIB", "mscMpanlIndex"),
    (0, "Nortel-MsCarrier-MscPassport-MpaNetworkLinkMIB", "mscMpanlSigIndex"),
)
if mibBuilder.loadTexts:
    mscMpanlSigSvcaccEntry.setStatus("mandatory")


class _MscMpanlSigDefaultAccounting_Type(Integer32):
    """Custom type mscMpanlSigDefaultAccounting based on Integer32"""
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


_MscMpanlSigDefaultAccounting_Type.__name__ = "Integer32"
_MscMpanlSigDefaultAccounting_Object = MibTableColumn
mscMpanlSigDefaultAccounting = _MscMpanlSigDefaultAccounting_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 6, 15, 1, 1),
    _MscMpanlSigDefaultAccounting_Type()
)
mscMpanlSigDefaultAccounting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscMpanlSigDefaultAccounting.setStatus("mandatory")
_MscMpanlSigStateTable_Object = MibTable
mscMpanlSigStateTable = _MscMpanlSigStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 6, 16)
)
if mibBuilder.loadTexts:
    mscMpanlSigStateTable.setStatus("mandatory")
_MscMpanlSigStateEntry_Object = MibTableRow
mscMpanlSigStateEntry = _MscMpanlSigStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 6, 16, 1)
)
mscMpanlSigStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-MpaNetworkLinkMIB", "mscMpanlIndex"),
    (0, "Nortel-MsCarrier-MscPassport-MpaNetworkLinkMIB", "mscMpanlSigIndex"),
)
if mibBuilder.loadTexts:
    mscMpanlSigStateEntry.setStatus("mandatory")


class _MscMpanlSigAdminState_Type(Integer32):
    """Custom type mscMpanlSigAdminState based on Integer32"""
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


_MscMpanlSigAdminState_Type.__name__ = "Integer32"
_MscMpanlSigAdminState_Object = MibTableColumn
mscMpanlSigAdminState = _MscMpanlSigAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 6, 16, 1, 1),
    _MscMpanlSigAdminState_Type()
)
mscMpanlSigAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlSigAdminState.setStatus("mandatory")


class _MscMpanlSigOperationalState_Type(Integer32):
    """Custom type mscMpanlSigOperationalState based on Integer32"""
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


_MscMpanlSigOperationalState_Type.__name__ = "Integer32"
_MscMpanlSigOperationalState_Object = MibTableColumn
mscMpanlSigOperationalState = _MscMpanlSigOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 6, 16, 1, 2),
    _MscMpanlSigOperationalState_Type()
)
mscMpanlSigOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlSigOperationalState.setStatus("mandatory")


class _MscMpanlSigUsageState_Type(Integer32):
    """Custom type mscMpanlSigUsageState based on Integer32"""
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


_MscMpanlSigUsageState_Type.__name__ = "Integer32"
_MscMpanlSigUsageState_Object = MibTableColumn
mscMpanlSigUsageState = _MscMpanlSigUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 6, 16, 1, 3),
    _MscMpanlSigUsageState_Type()
)
mscMpanlSigUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlSigUsageState.setStatus("mandatory")
_MscMpanlSigStatsTable_Object = MibTable
mscMpanlSigStatsTable = _MscMpanlSigStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 6, 17)
)
if mibBuilder.loadTexts:
    mscMpanlSigStatsTable.setStatus("mandatory")
_MscMpanlSigStatsEntry_Object = MibTableRow
mscMpanlSigStatsEntry = _MscMpanlSigStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 6, 17, 1)
)
mscMpanlSigStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-MpaNetworkLinkMIB", "mscMpanlIndex"),
    (0, "Nortel-MsCarrier-MscPassport-MpaNetworkLinkMIB", "mscMpanlSigIndex"),
)
if mibBuilder.loadTexts:
    mscMpanlSigStatsEntry.setStatus("mandatory")


class _MscMpanlSigCurrentNumberOfSvcCalls_Type(Unsigned32):
    """Custom type mscMpanlSigCurrentNumberOfSvcCalls based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 991),
    )


_MscMpanlSigCurrentNumberOfSvcCalls_Type.__name__ = "Unsigned32"
_MscMpanlSigCurrentNumberOfSvcCalls_Object = MibTableColumn
mscMpanlSigCurrentNumberOfSvcCalls = _MscMpanlSigCurrentNumberOfSvcCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 6, 17, 1, 1),
    _MscMpanlSigCurrentNumberOfSvcCalls_Type()
)
mscMpanlSigCurrentNumberOfSvcCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlSigCurrentNumberOfSvcCalls.setStatus("mandatory")
_MscMpanlSigInCalls_Type = Counter32
_MscMpanlSigInCalls_Object = MibTableColumn
mscMpanlSigInCalls = _MscMpanlSigInCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 6, 17, 1, 4),
    _MscMpanlSigInCalls_Type()
)
mscMpanlSigInCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlSigInCalls.setStatus("mandatory")
_MscMpanlSigInCallsRefused_Type = Counter32
_MscMpanlSigInCallsRefused_Object = MibTableColumn
mscMpanlSigInCallsRefused = _MscMpanlSigInCallsRefused_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 6, 17, 1, 5),
    _MscMpanlSigInCallsRefused_Type()
)
mscMpanlSigInCallsRefused.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlSigInCallsRefused.setStatus("mandatory")
_MscMpanlSigOutCalls_Type = Counter32
_MscMpanlSigOutCalls_Object = MibTableColumn
mscMpanlSigOutCalls = _MscMpanlSigOutCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 6, 17, 1, 6),
    _MscMpanlSigOutCalls_Type()
)
mscMpanlSigOutCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlSigOutCalls.setStatus("mandatory")
_MscMpanlSigOutCallsFailed_Type = Counter32
_MscMpanlSigOutCallsFailed_Object = MibTableColumn
mscMpanlSigOutCallsFailed = _MscMpanlSigOutCallsFailed_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 6, 17, 1, 7),
    _MscMpanlSigOutCallsFailed_Type()
)
mscMpanlSigOutCallsFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlSigOutCallsFailed.setStatus("mandatory")
_MscMpanlSigProtocolErrors_Type = Counter32
_MscMpanlSigProtocolErrors_Object = MibTableColumn
mscMpanlSigProtocolErrors = _MscMpanlSigProtocolErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 6, 17, 1, 8),
    _MscMpanlSigProtocolErrors_Type()
)
mscMpanlSigProtocolErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlSigProtocolErrors.setStatus("mandatory")
_MscMpanlSigQualityOfServiceNotAvailable_Type = Counter32
_MscMpanlSigQualityOfServiceNotAvailable_Object = MibTableColumn
mscMpanlSigQualityOfServiceNotAvailable = _MscMpanlSigQualityOfServiceNotAvailable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 6, 17, 1, 9),
    _MscMpanlSigQualityOfServiceNotAvailable_Type()
)
mscMpanlSigQualityOfServiceNotAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlSigQualityOfServiceNotAvailable.setStatus("mandatory")
_MscMpanlSigSetupTimeout_Type = Counter32
_MscMpanlSigSetupTimeout_Object = MibTableColumn
mscMpanlSigSetupTimeout = _MscMpanlSigSetupTimeout_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 6, 17, 1, 10),
    _MscMpanlSigSetupTimeout_Type()
)
mscMpanlSigSetupTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlSigSetupTimeout.setStatus("mandatory")


class _MscMpanlSigLastCauseInStatusMsgReceived_Type(Unsigned32):
    """Custom type mscMpanlSigLastCauseInStatusMsgReceived based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscMpanlSigLastCauseInStatusMsgReceived_Type.__name__ = "Unsigned32"
_MscMpanlSigLastCauseInStatusMsgReceived_Object = MibTableColumn
mscMpanlSigLastCauseInStatusMsgReceived = _MscMpanlSigLastCauseInStatusMsgReceived_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 6, 17, 1, 11),
    _MscMpanlSigLastCauseInStatusMsgReceived_Type()
)
mscMpanlSigLastCauseInStatusMsgReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlSigLastCauseInStatusMsgReceived.setStatus("mandatory")


class _MscMpanlSigLastStateInStatusMsgReceived_Type(Integer32):
    """Custom type mscMpanlSigLastStateInStatusMsgReceived based on Integer32"""
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
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63)
        )
    )
    namedValues = NamedValues(
        *(("active", 10),
          ("callInitiated", 1),
          ("callPresent", 6),
          ("disconnectIndication", 12),
          ("disconnectRequest", 11),
          ("incomingCallProceeding", 9),
          ("n13", 13),
          ("n14", 14),
          ("n15", 15),
          ("n16", 16),
          ("n17", 17),
          ("n18", 18),
          ("n2", 2),
          ("n21", 21),
          ("n22", 22),
          ("n23", 23),
          ("n24", 24),
          ("n25", 25),
          ("n26", 26),
          ("n27", 27),
          ("n28", 28),
          ("n29", 29),
          ("n30", 30),
          ("n31", 31),
          ("n32", 32),
          ("n33", 33),
          ("n34", 34),
          ("n35", 35),
          ("n36", 36),
          ("n37", 37),
          ("n38", 38),
          ("n39", 39),
          ("n4", 4),
          ("n40", 40),
          ("n41", 41),
          ("n42", 42),
          ("n43", 43),
          ("n44", 44),
          ("n45", 45),
          ("n46", 46),
          ("n47", 47),
          ("n48", 48),
          ("n49", 49),
          ("n5", 5),
          ("n50", 50),
          ("n51", 51),
          ("n52", 52),
          ("n53", 53),
          ("n54", 54),
          ("n55", 55),
          ("n56", 56),
          ("n57", 57),
          ("n58", 58),
          ("n59", 59),
          ("n60", 60),
          ("n61", 61),
          ("n62", 62),
          ("n63", 63),
          ("n7", 7),
          ("n8", 8),
          ("notApplicable", 20),
          ("null", 0),
          ("outgoingCallProceeding", 3),
          ("releaseRequest", 19))
    )


_MscMpanlSigLastStateInStatusMsgReceived_Type.__name__ = "Integer32"
_MscMpanlSigLastStateInStatusMsgReceived_Object = MibTableColumn
mscMpanlSigLastStateInStatusMsgReceived = _MscMpanlSigLastStateInStatusMsgReceived_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 6, 17, 1, 12),
    _MscMpanlSigLastStateInStatusMsgReceived_Type()
)
mscMpanlSigLastStateInStatusMsgReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlSigLastStateInStatusMsgReceived.setStatus("mandatory")


class _MscMpanlSigLastDlciReceivedStatus_Type(Unsigned32):
    """Custom type mscMpanlSigLastDlciReceivedStatus based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(17, 1007),
    )


_MscMpanlSigLastDlciReceivedStatus_Type.__name__ = "Unsigned32"
_MscMpanlSigLastDlciReceivedStatus_Object = MibTableColumn
mscMpanlSigLastDlciReceivedStatus = _MscMpanlSigLastDlciReceivedStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 6, 17, 1, 13),
    _MscMpanlSigLastDlciReceivedStatus_Type()
)
mscMpanlSigLastDlciReceivedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlSigLastDlciReceivedStatus.setStatus("mandatory")


class _MscMpanlSigLastQ933StateReceivedStatus_Type(Integer32):
    """Custom type mscMpanlSigLastQ933StateReceivedStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3,
              6,
              9,
              10,
              11,
              12,
              19,
              20)
        )
    )
    namedValues = NamedValues(
        *(("active", 10),
          ("callInitiated", 1),
          ("callPresent", 6),
          ("disconnectIndication", 12),
          ("disconnectRequest", 11),
          ("incomingCallProceeding", 9),
          ("notApplicable", 20),
          ("null", 0),
          ("outgoingCallProceeding", 3),
          ("releaseRequest", 19))
    )


_MscMpanlSigLastQ933StateReceivedStatus_Type.__name__ = "Integer32"
_MscMpanlSigLastQ933StateReceivedStatus_Object = MibTableColumn
mscMpanlSigLastQ933StateReceivedStatus = _MscMpanlSigLastQ933StateReceivedStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 6, 17, 1, 14),
    _MscMpanlSigLastQ933StateReceivedStatus_Type()
)
mscMpanlSigLastQ933StateReceivedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlSigLastQ933StateReceivedStatus.setStatus("mandatory")


class _MscMpanlSigLastTimeMsgBlockCongested_Type(EnterpriseDateAndTime):
    """Custom type mscMpanlSigLastTimeMsgBlockCongested based on EnterpriseDateAndTime"""
    subtypeSpec = EnterpriseDateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(16, 16),
    )


_MscMpanlSigLastTimeMsgBlockCongested_Type.__name__ = "EnterpriseDateAndTime"
_MscMpanlSigLastTimeMsgBlockCongested_Object = MibTableColumn
mscMpanlSigLastTimeMsgBlockCongested = _MscMpanlSigLastTimeMsgBlockCongested_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 6, 17, 1, 15),
    _MscMpanlSigLastTimeMsgBlockCongested_Type()
)
mscMpanlSigLastTimeMsgBlockCongested.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlSigLastTimeMsgBlockCongested.setStatus("mandatory")


class _MscMpanlSigLastDlciWithMsgBlockCongestion_Type(Unsigned32):
    """Custom type mscMpanlSigLastDlciWithMsgBlockCongestion based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(16, 1007),
    )


_MscMpanlSigLastDlciWithMsgBlockCongestion_Type.__name__ = "Unsigned32"
_MscMpanlSigLastDlciWithMsgBlockCongestion_Object = MibTableColumn
mscMpanlSigLastDlciWithMsgBlockCongestion = _MscMpanlSigLastDlciWithMsgBlockCongestion_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 6, 17, 1, 16),
    _MscMpanlSigLastDlciWithMsgBlockCongestion_Type()
)
mscMpanlSigLastDlciWithMsgBlockCongestion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlSigLastDlciWithMsgBlockCongestion.setStatus("mandatory")
_MscMpanlSigLapfStatusTable_Object = MibTable
mscMpanlSigLapfStatusTable = _MscMpanlSigLapfStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 6, 18)
)
if mibBuilder.loadTexts:
    mscMpanlSigLapfStatusTable.setStatus("mandatory")
_MscMpanlSigLapfStatusEntry_Object = MibTableRow
mscMpanlSigLapfStatusEntry = _MscMpanlSigLapfStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 6, 18, 1)
)
mscMpanlSigLapfStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-MpaNetworkLinkMIB", "mscMpanlIndex"),
    (0, "Nortel-MsCarrier-MscPassport-MpaNetworkLinkMIB", "mscMpanlSigIndex"),
)
if mibBuilder.loadTexts:
    mscMpanlSigLapfStatusEntry.setStatus("mandatory")


class _MscMpanlSigCurrentState_Type(Integer32):
    """Custom type mscMpanlSigCurrentState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5,
              7)
        )
    )
    namedValues = NamedValues(
        *(("disconnectRequest", 4),
          ("disconnected", 1),
          ("informationTransfer", 5),
          ("linkSetup", 2),
          ("waitingAck", 7))
    )


_MscMpanlSigCurrentState_Type.__name__ = "Integer32"
_MscMpanlSigCurrentState_Object = MibTableColumn
mscMpanlSigCurrentState = _MscMpanlSigCurrentState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 6, 18, 1, 1),
    _MscMpanlSigCurrentState_Type()
)
mscMpanlSigCurrentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlSigCurrentState.setStatus("mandatory")


class _MscMpanlSigLastStateChangeReason_Type(Integer32):
    """Custom type mscMpanlSigLastStateChangeReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              5,
              6,
              7,
              8,
              9,
              10,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("abmeEntered", 3),
          ("abmeReset", 5),
          ("discReceived", 8),
          ("discSent", 9),
          ("dmReceived", 6),
          ("dmSent", 7),
          ("frmrReceived", 10),
          ("n200RetranTimeOut", 12),
          ("notStarted", 1),
          ("other", 13))
    )


_MscMpanlSigLastStateChangeReason_Type.__name__ = "Integer32"
_MscMpanlSigLastStateChangeReason_Object = MibTableColumn
mscMpanlSigLastStateChangeReason = _MscMpanlSigLastStateChangeReason_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 6, 18, 1, 2),
    _MscMpanlSigLastStateChangeReason_Type()
)
mscMpanlSigLastStateChangeReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlSigLastStateChangeReason.setStatus("mandatory")


class _MscMpanlSigFrmrReceive_Type(HexString):
    """Custom type mscMpanlSigFrmrReceive based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_MscMpanlSigFrmrReceive_Type.__name__ = "HexString"
_MscMpanlSigFrmrReceive_Object = MibTableColumn
mscMpanlSigFrmrReceive = _MscMpanlSigFrmrReceive_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 6, 18, 1, 3),
    _MscMpanlSigFrmrReceive_Type()
)
mscMpanlSigFrmrReceive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlSigFrmrReceive.setStatus("mandatory")
_MscMpanlSigCurrentQueueSize_Type = Counter32
_MscMpanlSigCurrentQueueSize_Object = MibTableColumn
mscMpanlSigCurrentQueueSize = _MscMpanlSigCurrentQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 6, 18, 1, 4),
    _MscMpanlSigCurrentQueueSize_Type()
)
mscMpanlSigCurrentQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlSigCurrentQueueSize.setStatus("mandatory")
_MscMpanlSigLapfStatsTable_Object = MibTable
mscMpanlSigLapfStatsTable = _MscMpanlSigLapfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 6, 19)
)
if mibBuilder.loadTexts:
    mscMpanlSigLapfStatsTable.setStatus("mandatory")
_MscMpanlSigLapfStatsEntry_Object = MibTableRow
mscMpanlSigLapfStatsEntry = _MscMpanlSigLapfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 6, 19, 1)
)
mscMpanlSigLapfStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-MpaNetworkLinkMIB", "mscMpanlIndex"),
    (0, "Nortel-MsCarrier-MscPassport-MpaNetworkLinkMIB", "mscMpanlSigIndex"),
)
if mibBuilder.loadTexts:
    mscMpanlSigLapfStatsEntry.setStatus("mandatory")
_MscMpanlSigStateChange_Type = Counter32
_MscMpanlSigStateChange_Object = MibTableColumn
mscMpanlSigStateChange = _MscMpanlSigStateChange_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 6, 19, 1, 1),
    _MscMpanlSigStateChange_Type()
)
mscMpanlSigStateChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlSigStateChange.setStatus("mandatory")
_MscMpanlSigRemoteBusy_Type = Counter32
_MscMpanlSigRemoteBusy_Object = MibTableColumn
mscMpanlSigRemoteBusy = _MscMpanlSigRemoteBusy_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 6, 19, 1, 2),
    _MscMpanlSigRemoteBusy_Type()
)
mscMpanlSigRemoteBusy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlSigRemoteBusy.setStatus("mandatory")
_MscMpanlSigReceiveRejectFrame_Type = Counter32
_MscMpanlSigReceiveRejectFrame_Object = MibTableColumn
mscMpanlSigReceiveRejectFrame = _MscMpanlSigReceiveRejectFrame_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 6, 19, 1, 3),
    _MscMpanlSigReceiveRejectFrame_Type()
)
mscMpanlSigReceiveRejectFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlSigReceiveRejectFrame.setStatus("mandatory")
_MscMpanlSigAckTimeout_Type = Counter32
_MscMpanlSigAckTimeout_Object = MibTableColumn
mscMpanlSigAckTimeout = _MscMpanlSigAckTimeout_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 6, 19, 1, 4),
    _MscMpanlSigAckTimeout_Type()
)
mscMpanlSigAckTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlSigAckTimeout.setStatus("mandatory")
_MscMpanlSigIFramesTransmitted_Type = Counter32
_MscMpanlSigIFramesTransmitted_Object = MibTableColumn
mscMpanlSigIFramesTransmitted = _MscMpanlSigIFramesTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 6, 19, 1, 5),
    _MscMpanlSigIFramesTransmitted_Type()
)
mscMpanlSigIFramesTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlSigIFramesTransmitted.setStatus("mandatory")
_MscMpanlSigIFramesTxDiscarded_Type = Counter32
_MscMpanlSigIFramesTxDiscarded_Object = MibTableColumn
mscMpanlSigIFramesTxDiscarded = _MscMpanlSigIFramesTxDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 6, 19, 1, 6),
    _MscMpanlSigIFramesTxDiscarded_Type()
)
mscMpanlSigIFramesTxDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlSigIFramesTxDiscarded.setStatus("mandatory")
_MscMpanlSigIFramesReceived_Type = Counter32
_MscMpanlSigIFramesReceived_Object = MibTableColumn
mscMpanlSigIFramesReceived = _MscMpanlSigIFramesReceived_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 6, 19, 1, 7),
    _MscMpanlSigIFramesReceived_Type()
)
mscMpanlSigIFramesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlSigIFramesReceived.setStatus("mandatory")
_MscMpanlSigIFramesRcvdDiscarded_Type = Counter32
_MscMpanlSigIFramesRcvdDiscarded_Object = MibTableColumn
mscMpanlSigIFramesRcvdDiscarded = _MscMpanlSigIFramesRcvdDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 6, 19, 1, 8),
    _MscMpanlSigIFramesRcvdDiscarded_Type()
)
mscMpanlSigIFramesRcvdDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlSigIFramesRcvdDiscarded.setStatus("mandatory")
_MscMpanlSigMpanl_ObjectIdentity = ObjectIdentity
mscMpanlSigMpanl = _MscMpanlSigMpanl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 7)
)
_MscMpanlSigMpanlRowStatusTable_Object = MibTable
mscMpanlSigMpanlRowStatusTable = _MscMpanlSigMpanlRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 7, 1)
)
if mibBuilder.loadTexts:
    mscMpanlSigMpanlRowStatusTable.setStatus("mandatory")
_MscMpanlSigMpanlRowStatusEntry_Object = MibTableRow
mscMpanlSigMpanlRowStatusEntry = _MscMpanlSigMpanlRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 7, 1, 1)
)
mscMpanlSigMpanlRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-MpaNetworkLinkMIB", "mscMpanlIndex"),
    (0, "Nortel-MsCarrier-MscPassport-MpaNetworkLinkMIB", "mscMpanlSigMpanlIndex"),
)
if mibBuilder.loadTexts:
    mscMpanlSigMpanlRowStatusEntry.setStatus("mandatory")
_MscMpanlSigMpanlRowStatus_Type = RowStatus
_MscMpanlSigMpanlRowStatus_Object = MibTableColumn
mscMpanlSigMpanlRowStatus = _MscMpanlSigMpanlRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 7, 1, 1, 1),
    _MscMpanlSigMpanlRowStatus_Type()
)
mscMpanlSigMpanlRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlSigMpanlRowStatus.setStatus("mandatory")
_MscMpanlSigMpanlComponentName_Type = DisplayString
_MscMpanlSigMpanlComponentName_Object = MibTableColumn
mscMpanlSigMpanlComponentName = _MscMpanlSigMpanlComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 7, 1, 1, 2),
    _MscMpanlSigMpanlComponentName_Type()
)
mscMpanlSigMpanlComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlSigMpanlComponentName.setStatus("mandatory")
_MscMpanlSigMpanlStorageType_Type = StorageType
_MscMpanlSigMpanlStorageType_Object = MibTableColumn
mscMpanlSigMpanlStorageType = _MscMpanlSigMpanlStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 7, 1, 1, 4),
    _MscMpanlSigMpanlStorageType_Type()
)
mscMpanlSigMpanlStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlSigMpanlStorageType.setStatus("mandatory")
_MscMpanlSigMpanlIndex_Type = NonReplicated
_MscMpanlSigMpanlIndex_Object = MibTableColumn
mscMpanlSigMpanlIndex = _MscMpanlSigMpanlIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 7, 1, 1, 10),
    _MscMpanlSigMpanlIndex_Type()
)
mscMpanlSigMpanlIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscMpanlSigMpanlIndex.setStatus("mandatory")
_MscMpanlSigMpanlStateTable_Object = MibTable
mscMpanlSigMpanlStateTable = _MscMpanlSigMpanlStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 7, 10)
)
if mibBuilder.loadTexts:
    mscMpanlSigMpanlStateTable.setStatus("mandatory")
_MscMpanlSigMpanlStateEntry_Object = MibTableRow
mscMpanlSigMpanlStateEntry = _MscMpanlSigMpanlStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 7, 10, 1)
)
mscMpanlSigMpanlStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-MpaNetworkLinkMIB", "mscMpanlIndex"),
    (0, "Nortel-MsCarrier-MscPassport-MpaNetworkLinkMIB", "mscMpanlSigMpanlIndex"),
)
if mibBuilder.loadTexts:
    mscMpanlSigMpanlStateEntry.setStatus("mandatory")


class _MscMpanlSigMpanlAdminState_Type(Integer32):
    """Custom type mscMpanlSigMpanlAdminState based on Integer32"""
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


_MscMpanlSigMpanlAdminState_Type.__name__ = "Integer32"
_MscMpanlSigMpanlAdminState_Object = MibTableColumn
mscMpanlSigMpanlAdminState = _MscMpanlSigMpanlAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 7, 10, 1, 1),
    _MscMpanlSigMpanlAdminState_Type()
)
mscMpanlSigMpanlAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlSigMpanlAdminState.setStatus("mandatory")


class _MscMpanlSigMpanlOperationalState_Type(Integer32):
    """Custom type mscMpanlSigMpanlOperationalState based on Integer32"""
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


_MscMpanlSigMpanlOperationalState_Type.__name__ = "Integer32"
_MscMpanlSigMpanlOperationalState_Object = MibTableColumn
mscMpanlSigMpanlOperationalState = _MscMpanlSigMpanlOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 7, 10, 1, 2),
    _MscMpanlSigMpanlOperationalState_Type()
)
mscMpanlSigMpanlOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlSigMpanlOperationalState.setStatus("mandatory")


class _MscMpanlSigMpanlUsageState_Type(Integer32):
    """Custom type mscMpanlSigMpanlUsageState based on Integer32"""
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


_MscMpanlSigMpanlUsageState_Type.__name__ = "Integer32"
_MscMpanlSigMpanlUsageState_Object = MibTableColumn
mscMpanlSigMpanlUsageState = _MscMpanlSigMpanlUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 7, 10, 1, 3),
    _MscMpanlSigMpanlUsageState_Type()
)
mscMpanlSigMpanlUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlSigMpanlUsageState.setStatus("mandatory")
_MscMpanlSigMpanlProfileTable_Object = MibTable
mscMpanlSigMpanlProfileTable = _MscMpanlSigMpanlProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 7, 11)
)
if mibBuilder.loadTexts:
    mscMpanlSigMpanlProfileTable.setStatus("mandatory")
_MscMpanlSigMpanlProfileEntry_Object = MibTableRow
mscMpanlSigMpanlProfileEntry = _MscMpanlSigMpanlProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 7, 11, 1)
)
mscMpanlSigMpanlProfileEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-MpaNetworkLinkMIB", "mscMpanlIndex"),
    (0, "Nortel-MsCarrier-MscPassport-MpaNetworkLinkMIB", "mscMpanlSigMpanlIndex"),
)
if mibBuilder.loadTexts:
    mscMpanlSigMpanlProfileEntry.setStatus("mandatory")


class _MscMpanlSigMpanlDteCustomerId_Type(Unsigned32):
    """Custom type mscMpanlSigMpanlDteCustomerId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 8191),
    )


_MscMpanlSigMpanlDteCustomerId_Type.__name__ = "Unsigned32"
_MscMpanlSigMpanlDteCustomerId_Object = MibTableColumn
mscMpanlSigMpanlDteCustomerId = _MscMpanlSigMpanlDteCustomerId_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 7, 11, 1, 1),
    _MscMpanlSigMpanlDteCustomerId_Type()
)
mscMpanlSigMpanlDteCustomerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlSigMpanlDteCustomerId.setStatus("mandatory")


class _MscMpanlSigMpanlDteNodeId_Type(Unsigned32):
    """Custom type mscMpanlSigMpanlDteNodeId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_MscMpanlSigMpanlDteNodeId_Type.__name__ = "Unsigned32"
_MscMpanlSigMpanlDteNodeId_Object = MibTableColumn
mscMpanlSigMpanlDteNodeId = _MscMpanlSigMpanlDteNodeId_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 7, 11, 1, 2),
    _MscMpanlSigMpanlDteNodeId_Type()
)
mscMpanlSigMpanlDteNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlSigMpanlDteNodeId.setStatus("mandatory")


class _MscMpanlSigMpanlDteComponentName_Type(AsciiString):
    """Custom type mscMpanlSigMpanlDteComponentName based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_MscMpanlSigMpanlDteComponentName_Type.__name__ = "AsciiString"
_MscMpanlSigMpanlDteComponentName_Object = MibTableColumn
mscMpanlSigMpanlDteComponentName = _MscMpanlSigMpanlDteComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 7, 11, 1, 3),
    _MscMpanlSigMpanlDteComponentName_Type()
)
mscMpanlSigMpanlDteComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlSigMpanlDteComponentName.setStatus("mandatory")


class _MscMpanlSigMpanlHighestDlci_Type(Unsigned32):
    """Custom type mscMpanlSigMpanlHighestDlci based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(17, 1007),
    )


_MscMpanlSigMpanlHighestDlci_Type.__name__ = "Unsigned32"
_MscMpanlSigMpanlHighestDlci_Object = MibTableColumn
mscMpanlSigMpanlHighestDlci = _MscMpanlSigMpanlHighestDlci_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 7, 11, 1, 4),
    _MscMpanlSigMpanlHighestDlci_Type()
)
mscMpanlSigMpanlHighestDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlSigMpanlHighestDlci.setStatus("mandatory")
_MscMpanlSigMpanlStatsTable_Object = MibTable
mscMpanlSigMpanlStatsTable = _MscMpanlSigMpanlStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 7, 12)
)
if mibBuilder.loadTexts:
    mscMpanlSigMpanlStatsTable.setStatus("mandatory")
_MscMpanlSigMpanlStatsEntry_Object = MibTableRow
mscMpanlSigMpanlStatsEntry = _MscMpanlSigMpanlStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 7, 12, 1)
)
mscMpanlSigMpanlStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-MpaNetworkLinkMIB", "mscMpanlIndex"),
    (0, "Nortel-MsCarrier-MscPassport-MpaNetworkLinkMIB", "mscMpanlSigMpanlIndex"),
)
if mibBuilder.loadTexts:
    mscMpanlSigMpanlStatsEntry.setStatus("mandatory")
_MscMpanlSigMpanlProtocolErrors_Type = Counter32
_MscMpanlSigMpanlProtocolErrors_Object = MibTableColumn
mscMpanlSigMpanlProtocolErrors = _MscMpanlSigMpanlProtocolErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 7, 12, 1, 1),
    _MscMpanlSigMpanlProtocolErrors_Type()
)
mscMpanlSigMpanlProtocolErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlSigMpanlProtocolErrors.setStatus("mandatory")
_MscMpanlSigMpanlSap0CommandsRx_Type = Counter32
_MscMpanlSigMpanlSap0CommandsRx_Object = MibTableColumn
mscMpanlSigMpanlSap0CommandsRx = _MscMpanlSigMpanlSap0CommandsRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 7, 12, 1, 2),
    _MscMpanlSigMpanlSap0CommandsRx_Type()
)
mscMpanlSigMpanlSap0CommandsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlSigMpanlSap0CommandsRx.setStatus("mandatory")
_MscMpanlSigMpanlSap0CommandsTx_Type = Counter32
_MscMpanlSigMpanlSap0CommandsTx_Object = MibTableColumn
mscMpanlSigMpanlSap0CommandsTx = _MscMpanlSigMpanlSap0CommandsTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 7, 12, 1, 3),
    _MscMpanlSigMpanlSap0CommandsTx_Type()
)
mscMpanlSigMpanlSap0CommandsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlSigMpanlSap0CommandsTx.setStatus("mandatory")
_MscMpanlSigMpanlSapXCommandsRx_Type = Counter32
_MscMpanlSigMpanlSapXCommandsRx_Object = MibTableColumn
mscMpanlSigMpanlSapXCommandsRx = _MscMpanlSigMpanlSapXCommandsRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 7, 12, 1, 4),
    _MscMpanlSigMpanlSapXCommandsRx_Type()
)
mscMpanlSigMpanlSapXCommandsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlSigMpanlSapXCommandsRx.setStatus("mandatory")
_MscMpanlSigMpanlSapXCommandsTx_Type = Counter32
_MscMpanlSigMpanlSapXCommandsTx_Object = MibTableColumn
mscMpanlSigMpanlSapXCommandsTx = _MscMpanlSigMpanlSapXCommandsTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 7, 12, 1, 5),
    _MscMpanlSigMpanlSapXCommandsTx_Type()
)
mscMpanlSigMpanlSapXCommandsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlSigMpanlSapXCommandsTx.setStatus("mandatory")
_MscMpanlSigMpanlLapfStatusTable_Object = MibTable
mscMpanlSigMpanlLapfStatusTable = _MscMpanlSigMpanlLapfStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 7, 13)
)
if mibBuilder.loadTexts:
    mscMpanlSigMpanlLapfStatusTable.setStatus("mandatory")
_MscMpanlSigMpanlLapfStatusEntry_Object = MibTableRow
mscMpanlSigMpanlLapfStatusEntry = _MscMpanlSigMpanlLapfStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 7, 13, 1)
)
mscMpanlSigMpanlLapfStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-MpaNetworkLinkMIB", "mscMpanlIndex"),
    (0, "Nortel-MsCarrier-MscPassport-MpaNetworkLinkMIB", "mscMpanlSigMpanlIndex"),
)
if mibBuilder.loadTexts:
    mscMpanlSigMpanlLapfStatusEntry.setStatus("mandatory")


class _MscMpanlSigMpanlCurrentState_Type(Integer32):
    """Custom type mscMpanlSigMpanlCurrentState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5,
              7)
        )
    )
    namedValues = NamedValues(
        *(("disconnectRequest", 4),
          ("disconnected", 1),
          ("informationTransfer", 5),
          ("linkSetup", 2),
          ("waitingAck", 7))
    )


_MscMpanlSigMpanlCurrentState_Type.__name__ = "Integer32"
_MscMpanlSigMpanlCurrentState_Object = MibTableColumn
mscMpanlSigMpanlCurrentState = _MscMpanlSigMpanlCurrentState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 7, 13, 1, 1),
    _MscMpanlSigMpanlCurrentState_Type()
)
mscMpanlSigMpanlCurrentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlSigMpanlCurrentState.setStatus("mandatory")


class _MscMpanlSigMpanlLastStateChangeReason_Type(Integer32):
    """Custom type mscMpanlSigMpanlLastStateChangeReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              5,
              6,
              7,
              8,
              9,
              10,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("abmeEntered", 3),
          ("abmeReset", 5),
          ("discReceived", 8),
          ("discSent", 9),
          ("dmReceived", 6),
          ("dmSent", 7),
          ("frmrReceived", 10),
          ("n200RetranTimeOut", 12),
          ("notStarted", 1),
          ("other", 13))
    )


_MscMpanlSigMpanlLastStateChangeReason_Type.__name__ = "Integer32"
_MscMpanlSigMpanlLastStateChangeReason_Object = MibTableColumn
mscMpanlSigMpanlLastStateChangeReason = _MscMpanlSigMpanlLastStateChangeReason_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 7, 13, 1, 2),
    _MscMpanlSigMpanlLastStateChangeReason_Type()
)
mscMpanlSigMpanlLastStateChangeReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlSigMpanlLastStateChangeReason.setStatus("mandatory")


class _MscMpanlSigMpanlFrmrReceive_Type(HexString):
    """Custom type mscMpanlSigMpanlFrmrReceive based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_MscMpanlSigMpanlFrmrReceive_Type.__name__ = "HexString"
_MscMpanlSigMpanlFrmrReceive_Object = MibTableColumn
mscMpanlSigMpanlFrmrReceive = _MscMpanlSigMpanlFrmrReceive_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 7, 13, 1, 3),
    _MscMpanlSigMpanlFrmrReceive_Type()
)
mscMpanlSigMpanlFrmrReceive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlSigMpanlFrmrReceive.setStatus("mandatory")
_MscMpanlSigMpanlCurrentQueueSize_Type = Counter32
_MscMpanlSigMpanlCurrentQueueSize_Object = MibTableColumn
mscMpanlSigMpanlCurrentQueueSize = _MscMpanlSigMpanlCurrentQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 7, 13, 1, 4),
    _MscMpanlSigMpanlCurrentQueueSize_Type()
)
mscMpanlSigMpanlCurrentQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlSigMpanlCurrentQueueSize.setStatus("mandatory")
_MscMpanlSigMpanlLapfStatsTable_Object = MibTable
mscMpanlSigMpanlLapfStatsTable = _MscMpanlSigMpanlLapfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 7, 14)
)
if mibBuilder.loadTexts:
    mscMpanlSigMpanlLapfStatsTable.setStatus("mandatory")
_MscMpanlSigMpanlLapfStatsEntry_Object = MibTableRow
mscMpanlSigMpanlLapfStatsEntry = _MscMpanlSigMpanlLapfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 7, 14, 1)
)
mscMpanlSigMpanlLapfStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-MpaNetworkLinkMIB", "mscMpanlIndex"),
    (0, "Nortel-MsCarrier-MscPassport-MpaNetworkLinkMIB", "mscMpanlSigMpanlIndex"),
)
if mibBuilder.loadTexts:
    mscMpanlSigMpanlLapfStatsEntry.setStatus("mandatory")
_MscMpanlSigMpanlStateChange_Type = Counter32
_MscMpanlSigMpanlStateChange_Object = MibTableColumn
mscMpanlSigMpanlStateChange = _MscMpanlSigMpanlStateChange_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 7, 14, 1, 1),
    _MscMpanlSigMpanlStateChange_Type()
)
mscMpanlSigMpanlStateChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlSigMpanlStateChange.setStatus("mandatory")
_MscMpanlSigMpanlRemoteBusy_Type = Counter32
_MscMpanlSigMpanlRemoteBusy_Object = MibTableColumn
mscMpanlSigMpanlRemoteBusy = _MscMpanlSigMpanlRemoteBusy_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 7, 14, 1, 2),
    _MscMpanlSigMpanlRemoteBusy_Type()
)
mscMpanlSigMpanlRemoteBusy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlSigMpanlRemoteBusy.setStatus("mandatory")
_MscMpanlSigMpanlReceiveRejectFrame_Type = Counter32
_MscMpanlSigMpanlReceiveRejectFrame_Object = MibTableColumn
mscMpanlSigMpanlReceiveRejectFrame = _MscMpanlSigMpanlReceiveRejectFrame_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 7, 14, 1, 3),
    _MscMpanlSigMpanlReceiveRejectFrame_Type()
)
mscMpanlSigMpanlReceiveRejectFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlSigMpanlReceiveRejectFrame.setStatus("mandatory")
_MscMpanlSigMpanlAckTimeout_Type = Counter32
_MscMpanlSigMpanlAckTimeout_Object = MibTableColumn
mscMpanlSigMpanlAckTimeout = _MscMpanlSigMpanlAckTimeout_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 7, 14, 1, 4),
    _MscMpanlSigMpanlAckTimeout_Type()
)
mscMpanlSigMpanlAckTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlSigMpanlAckTimeout.setStatus("mandatory")
_MscMpanlSigMpanlIFramesTransmitted_Type = Counter32
_MscMpanlSigMpanlIFramesTransmitted_Object = MibTableColumn
mscMpanlSigMpanlIFramesTransmitted = _MscMpanlSigMpanlIFramesTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 7, 14, 1, 5),
    _MscMpanlSigMpanlIFramesTransmitted_Type()
)
mscMpanlSigMpanlIFramesTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlSigMpanlIFramesTransmitted.setStatus("mandatory")
_MscMpanlSigMpanlIFramesTxDiscarded_Type = Counter32
_MscMpanlSigMpanlIFramesTxDiscarded_Object = MibTableColumn
mscMpanlSigMpanlIFramesTxDiscarded = _MscMpanlSigMpanlIFramesTxDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 7, 14, 1, 6),
    _MscMpanlSigMpanlIFramesTxDiscarded_Type()
)
mscMpanlSigMpanlIFramesTxDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlSigMpanlIFramesTxDiscarded.setStatus("mandatory")
_MscMpanlSigMpanlIFramesReceived_Type = Counter32
_MscMpanlSigMpanlIFramesReceived_Object = MibTableColumn
mscMpanlSigMpanlIFramesReceived = _MscMpanlSigMpanlIFramesReceived_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 7, 14, 1, 7),
    _MscMpanlSigMpanlIFramesReceived_Type()
)
mscMpanlSigMpanlIFramesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlSigMpanlIFramesReceived.setStatus("mandatory")
_MscMpanlSigMpanlIFramesRcvdDiscarded_Type = Counter32
_MscMpanlSigMpanlIFramesRcvdDiscarded_Object = MibTableColumn
mscMpanlSigMpanlIFramesRcvdDiscarded = _MscMpanlSigMpanlIFramesRcvdDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 7, 14, 1, 8),
    _MscMpanlSigMpanlIFramesRcvdDiscarded_Type()
)
mscMpanlSigMpanlIFramesRcvdDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlSigMpanlIFramesRcvdDiscarded.setStatus("mandatory")
_MscMpanlLmi_ObjectIdentity = ObjectIdentity
mscMpanlLmi = _MscMpanlLmi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 8)
)
_MscMpanlLmiRowStatusTable_Object = MibTable
mscMpanlLmiRowStatusTable = _MscMpanlLmiRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 8, 1)
)
if mibBuilder.loadTexts:
    mscMpanlLmiRowStatusTable.setStatus("mandatory")
_MscMpanlLmiRowStatusEntry_Object = MibTableRow
mscMpanlLmiRowStatusEntry = _MscMpanlLmiRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 8, 1, 1)
)
mscMpanlLmiRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-MpaNetworkLinkMIB", "mscMpanlIndex"),
    (0, "Nortel-MsCarrier-MscPassport-MpaNetworkLinkMIB", "mscMpanlLmiIndex"),
)
if mibBuilder.loadTexts:
    mscMpanlLmiRowStatusEntry.setStatus("mandatory")
_MscMpanlLmiRowStatus_Type = RowStatus
_MscMpanlLmiRowStatus_Object = MibTableColumn
mscMpanlLmiRowStatus = _MscMpanlLmiRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 8, 1, 1, 1),
    _MscMpanlLmiRowStatus_Type()
)
mscMpanlLmiRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlLmiRowStatus.setStatus("mandatory")
_MscMpanlLmiComponentName_Type = DisplayString
_MscMpanlLmiComponentName_Object = MibTableColumn
mscMpanlLmiComponentName = _MscMpanlLmiComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 8, 1, 1, 2),
    _MscMpanlLmiComponentName_Type()
)
mscMpanlLmiComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlLmiComponentName.setStatus("mandatory")
_MscMpanlLmiStorageType_Type = StorageType
_MscMpanlLmiStorageType_Object = MibTableColumn
mscMpanlLmiStorageType = _MscMpanlLmiStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 8, 1, 1, 4),
    _MscMpanlLmiStorageType_Type()
)
mscMpanlLmiStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlLmiStorageType.setStatus("mandatory")
_MscMpanlLmiIndex_Type = NonReplicated
_MscMpanlLmiIndex_Object = MibTableColumn
mscMpanlLmiIndex = _MscMpanlLmiIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 8, 1, 1, 10),
    _MscMpanlLmiIndex_Type()
)
mscMpanlLmiIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscMpanlLmiIndex.setStatus("mandatory")
_MscMpanlLmiParmsTable_Object = MibTable
mscMpanlLmiParmsTable = _MscMpanlLmiParmsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 8, 10)
)
if mibBuilder.loadTexts:
    mscMpanlLmiParmsTable.setStatus("mandatory")
_MscMpanlLmiParmsEntry_Object = MibTableRow
mscMpanlLmiParmsEntry = _MscMpanlLmiParmsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 8, 10, 1)
)
mscMpanlLmiParmsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-MpaNetworkLinkMIB", "mscMpanlIndex"),
    (0, "Nortel-MsCarrier-MscPassport-MpaNetworkLinkMIB", "mscMpanlLmiIndex"),
)
if mibBuilder.loadTexts:
    mscMpanlLmiParmsEntry.setStatus("mandatory")


class _MscMpanlLmiProcedures_Type(Integer32):
    """Custom type mscMpanlLmiProcedures based on Integer32"""
    defaultValue = 0

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
        *(("ansi", 2),
          ("ccitt", 3),
          ("none", 0),
          ("vendorForum", 1))
    )


_MscMpanlLmiProcedures_Type.__name__ = "Integer32"
_MscMpanlLmiProcedures_Object = MibTableColumn
mscMpanlLmiProcedures = _MscMpanlLmiProcedures_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 8, 10, 1, 1),
    _MscMpanlLmiProcedures_Type()
)
mscMpanlLmiProcedures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlLmiProcedures.setStatus("mandatory")
_MscMpanlLmiStateTable_Object = MibTable
mscMpanlLmiStateTable = _MscMpanlLmiStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 8, 12)
)
if mibBuilder.loadTexts:
    mscMpanlLmiStateTable.setStatus("mandatory")
_MscMpanlLmiStateEntry_Object = MibTableRow
mscMpanlLmiStateEntry = _MscMpanlLmiStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 8, 12, 1)
)
mscMpanlLmiStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-MpaNetworkLinkMIB", "mscMpanlIndex"),
    (0, "Nortel-MsCarrier-MscPassport-MpaNetworkLinkMIB", "mscMpanlLmiIndex"),
)
if mibBuilder.loadTexts:
    mscMpanlLmiStateEntry.setStatus("mandatory")


class _MscMpanlLmiAdminState_Type(Integer32):
    """Custom type mscMpanlLmiAdminState based on Integer32"""
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


_MscMpanlLmiAdminState_Type.__name__ = "Integer32"
_MscMpanlLmiAdminState_Object = MibTableColumn
mscMpanlLmiAdminState = _MscMpanlLmiAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 8, 12, 1, 1),
    _MscMpanlLmiAdminState_Type()
)
mscMpanlLmiAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlLmiAdminState.setStatus("mandatory")


class _MscMpanlLmiOperationalState_Type(Integer32):
    """Custom type mscMpanlLmiOperationalState based on Integer32"""
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


_MscMpanlLmiOperationalState_Type.__name__ = "Integer32"
_MscMpanlLmiOperationalState_Object = MibTableColumn
mscMpanlLmiOperationalState = _MscMpanlLmiOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 8, 12, 1, 2),
    _MscMpanlLmiOperationalState_Type()
)
mscMpanlLmiOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlLmiOperationalState.setStatus("mandatory")


class _MscMpanlLmiUsageState_Type(Integer32):
    """Custom type mscMpanlLmiUsageState based on Integer32"""
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


_MscMpanlLmiUsageState_Type.__name__ = "Integer32"
_MscMpanlLmiUsageState_Object = MibTableColumn
mscMpanlLmiUsageState = _MscMpanlLmiUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 8, 12, 1, 3),
    _MscMpanlLmiUsageState_Type()
)
mscMpanlLmiUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlLmiUsageState.setStatus("mandatory")
_MscMpanlCidDataTable_Object = MibTable
mscMpanlCidDataTable = _MscMpanlCidDataTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 10)
)
if mibBuilder.loadTexts:
    mscMpanlCidDataTable.setStatus("mandatory")
_MscMpanlCidDataEntry_Object = MibTableRow
mscMpanlCidDataEntry = _MscMpanlCidDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 10, 1)
)
mscMpanlCidDataEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-MpaNetworkLinkMIB", "mscMpanlIndex"),
)
if mibBuilder.loadTexts:
    mscMpanlCidDataEntry.setStatus("mandatory")


class _MscMpanlCustomerIdentifier_Type(Unsigned32):
    """Custom type mscMpanlCustomerIdentifier based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 8191),
    )


_MscMpanlCustomerIdentifier_Type.__name__ = "Unsigned32"
_MscMpanlCustomerIdentifier_Object = MibTableColumn
mscMpanlCustomerIdentifier = _MscMpanlCustomerIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 10, 1, 1),
    _MscMpanlCustomerIdentifier_Type()
)
mscMpanlCustomerIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlCustomerIdentifier.setStatus("mandatory")
_MscMpanlProvTable_Object = MibTable
mscMpanlProvTable = _MscMpanlProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 12)
)
if mibBuilder.loadTexts:
    mscMpanlProvTable.setStatus("mandatory")
_MscMpanlProvEntry_Object = MibTableRow
mscMpanlProvEntry = _MscMpanlProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 12, 1)
)
mscMpanlProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-MpaNetworkLinkMIB", "mscMpanlIndex"),
)
if mibBuilder.loadTexts:
    mscMpanlProvEntry.setStatus("mandatory")


class _MscMpanlCommentText_Type(AsciiString):
    """Custom type mscMpanlCommentText based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_MscMpanlCommentText_Type.__name__ = "AsciiString"
_MscMpanlCommentText_Object = MibTableColumn
mscMpanlCommentText = _MscMpanlCommentText_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 12, 1, 1),
    _MscMpanlCommentText_Type()
)
mscMpanlCommentText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscMpanlCommentText.setStatus("mandatory")
_MscMpanlEmissionPriorityQsTable_Object = MibTable
mscMpanlEmissionPriorityQsTable = _MscMpanlEmissionPriorityQsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 13)
)
if mibBuilder.loadTexts:
    mscMpanlEmissionPriorityQsTable.setStatus("mandatory")
_MscMpanlEmissionPriorityQsEntry_Object = MibTableRow
mscMpanlEmissionPriorityQsEntry = _MscMpanlEmissionPriorityQsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 13, 1)
)
mscMpanlEmissionPriorityQsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-MpaNetworkLinkMIB", "mscMpanlIndex"),
)
if mibBuilder.loadTexts:
    mscMpanlEmissionPriorityQsEntry.setStatus("mandatory")


class _MscMpanlNumberOfEmissionQs_Type(Unsigned32):
    """Custom type mscMpanlNumberOfEmissionQs based on Unsigned32"""
    defaultValue = 4

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 2),
        ValueRangeConstraint(4, 4),
    )


_MscMpanlNumberOfEmissionQs_Type.__name__ = "Unsigned32"
_MscMpanlNumberOfEmissionQs_Object = MibTableColumn
mscMpanlNumberOfEmissionQs = _MscMpanlNumberOfEmissionQs_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 13, 1, 1),
    _MscMpanlNumberOfEmissionQs_Type()
)
mscMpanlNumberOfEmissionQs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlNumberOfEmissionQs.setStatus("mandatory")
_MscMpanlStateTable_Object = MibTable
mscMpanlStateTable = _MscMpanlStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 14)
)
if mibBuilder.loadTexts:
    mscMpanlStateTable.setStatus("mandatory")
_MscMpanlStateEntry_Object = MibTableRow
mscMpanlStateEntry = _MscMpanlStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 14, 1)
)
mscMpanlStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-MpaNetworkLinkMIB", "mscMpanlIndex"),
)
if mibBuilder.loadTexts:
    mscMpanlStateEntry.setStatus("mandatory")


class _MscMpanlAdminState_Type(Integer32):
    """Custom type mscMpanlAdminState based on Integer32"""
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


_MscMpanlAdminState_Type.__name__ = "Integer32"
_MscMpanlAdminState_Object = MibTableColumn
mscMpanlAdminState = _MscMpanlAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 14, 1, 1),
    _MscMpanlAdminState_Type()
)
mscMpanlAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlAdminState.setStatus("mandatory")


class _MscMpanlOperationalState_Type(Integer32):
    """Custom type mscMpanlOperationalState based on Integer32"""
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


_MscMpanlOperationalState_Type.__name__ = "Integer32"
_MscMpanlOperationalState_Object = MibTableColumn
mscMpanlOperationalState = _MscMpanlOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 14, 1, 2),
    _MscMpanlOperationalState_Type()
)
mscMpanlOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlOperationalState.setStatus("mandatory")


class _MscMpanlUsageState_Type(Integer32):
    """Custom type mscMpanlUsageState based on Integer32"""
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


_MscMpanlUsageState_Type.__name__ = "Integer32"
_MscMpanlUsageState_Object = MibTableColumn
mscMpanlUsageState = _MscMpanlUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 14, 1, 3),
    _MscMpanlUsageState_Type()
)
mscMpanlUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlUsageState.setStatus("mandatory")


class _MscMpanlAvailabilityStatus_Type(OctetString):
    """Custom type mscMpanlAvailabilityStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_MscMpanlAvailabilityStatus_Type.__name__ = "OctetString"
_MscMpanlAvailabilityStatus_Object = MibTableColumn
mscMpanlAvailabilityStatus = _MscMpanlAvailabilityStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 14, 1, 4),
    _MscMpanlAvailabilityStatus_Type()
)
mscMpanlAvailabilityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlAvailabilityStatus.setStatus("mandatory")


class _MscMpanlProceduralStatus_Type(OctetString):
    """Custom type mscMpanlProceduralStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscMpanlProceduralStatus_Type.__name__ = "OctetString"
_MscMpanlProceduralStatus_Object = MibTableColumn
mscMpanlProceduralStatus = _MscMpanlProceduralStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 14, 1, 5),
    _MscMpanlProceduralStatus_Type()
)
mscMpanlProceduralStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlProceduralStatus.setStatus("mandatory")


class _MscMpanlControlStatus_Type(OctetString):
    """Custom type mscMpanlControlStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscMpanlControlStatus_Type.__name__ = "OctetString"
_MscMpanlControlStatus_Object = MibTableColumn
mscMpanlControlStatus = _MscMpanlControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 14, 1, 6),
    _MscMpanlControlStatus_Type()
)
mscMpanlControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlControlStatus.setStatus("mandatory")


class _MscMpanlAlarmStatus_Type(OctetString):
    """Custom type mscMpanlAlarmStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscMpanlAlarmStatus_Type.__name__ = "OctetString"
_MscMpanlAlarmStatus_Object = MibTableColumn
mscMpanlAlarmStatus = _MscMpanlAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 14, 1, 7),
    _MscMpanlAlarmStatus_Type()
)
mscMpanlAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlAlarmStatus.setStatus("mandatory")


class _MscMpanlStandbyStatus_Type(Integer32):
    """Custom type mscMpanlStandbyStatus based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              15)
        )
    )
    namedValues = NamedValues(
        *(("coldStandby", 1),
          ("hotStandby", 0),
          ("notSet", 15),
          ("providingService", 2))
    )


_MscMpanlStandbyStatus_Type.__name__ = "Integer32"
_MscMpanlStandbyStatus_Object = MibTableColumn
mscMpanlStandbyStatus = _MscMpanlStandbyStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 14, 1, 8),
    _MscMpanlStandbyStatus_Type()
)
mscMpanlStandbyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlStandbyStatus.setStatus("mandatory")


class _MscMpanlUnknownStatus_Type(Integer32):
    """Custom type mscMpanlUnknownStatus based on Integer32"""
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


_MscMpanlUnknownStatus_Type.__name__ = "Integer32"
_MscMpanlUnknownStatus_Object = MibTableColumn
mscMpanlUnknownStatus = _MscMpanlUnknownStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 14, 1, 9),
    _MscMpanlUnknownStatus_Type()
)
mscMpanlUnknownStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlUnknownStatus.setStatus("mandatory")
_MscMpanlStatsTable_Object = MibTable
mscMpanlStatsTable = _MscMpanlStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 16)
)
if mibBuilder.loadTexts:
    mscMpanlStatsTable.setStatus("mandatory")
_MscMpanlStatsEntry_Object = MibTableRow
mscMpanlStatsEntry = _MscMpanlStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 16, 1)
)
mscMpanlStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-MpaNetworkLinkMIB", "mscMpanlIndex"),
)
if mibBuilder.loadTexts:
    mscMpanlStatsEntry.setStatus("mandatory")


class _MscMpanlLastUnknownDlci_Type(Unsigned32):
    """Custom type mscMpanlLastUnknownDlci based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_MscMpanlLastUnknownDlci_Type.__name__ = "Unsigned32"
_MscMpanlLastUnknownDlci_Object = MibTableColumn
mscMpanlLastUnknownDlci = _MscMpanlLastUnknownDlci_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 16, 1, 1),
    _MscMpanlLastUnknownDlci_Type()
)
mscMpanlLastUnknownDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlLastUnknownDlci.setStatus("mandatory")
_MscMpanlUnknownDlciFramesFromIf_Type = Counter32
_MscMpanlUnknownDlciFramesFromIf_Object = MibTableColumn
mscMpanlUnknownDlciFramesFromIf = _MscMpanlUnknownDlciFramesFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 16, 1, 2),
    _MscMpanlUnknownDlciFramesFromIf_Type()
)
mscMpanlUnknownDlciFramesFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlUnknownDlciFramesFromIf.setStatus("mandatory")
_MscMpanlInvalidHeaderFramesFromIf_Type = Counter32
_MscMpanlInvalidHeaderFramesFromIf_Object = MibTableColumn
mscMpanlInvalidHeaderFramesFromIf = _MscMpanlInvalidHeaderFramesFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 16, 1, 3),
    _MscMpanlInvalidHeaderFramesFromIf_Type()
)
mscMpanlInvalidHeaderFramesFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlInvalidHeaderFramesFromIf.setStatus("mandatory")
_MscMpanlTrafficStatsTable_Object = MibTable
mscMpanlTrafficStatsTable = _MscMpanlTrafficStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 17)
)
if mibBuilder.loadTexts:
    mscMpanlTrafficStatsTable.setStatus("mandatory")
_MscMpanlTrafficStatsEntry_Object = MibTableRow
mscMpanlTrafficStatsEntry = _MscMpanlTrafficStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 17, 1)
)
mscMpanlTrafficStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-MpaNetworkLinkMIB", "mscMpanlIndex"),
)
if mibBuilder.loadTexts:
    mscMpanlTrafficStatsEntry.setStatus("mandatory")


class _MscMpanlFrmToIf_Type(Unsigned32):
    """Custom type mscMpanlFrmToIf based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscMpanlFrmToIf_Type.__name__ = "Unsigned32"
_MscMpanlFrmToIf_Object = MibTableColumn
mscMpanlFrmToIf = _MscMpanlFrmToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 17, 1, 1),
    _MscMpanlFrmToIf_Type()
)
mscMpanlFrmToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlFrmToIf.setStatus("mandatory")


class _MscMpanlOctetToIf_Type(Unsigned32):
    """Custom type mscMpanlOctetToIf based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscMpanlOctetToIf_Type.__name__ = "Unsigned32"
_MscMpanlOctetToIf_Object = MibTableColumn
mscMpanlOctetToIf = _MscMpanlOctetToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 17, 1, 2),
    _MscMpanlOctetToIf_Type()
)
mscMpanlOctetToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlOctetToIf.setStatus("mandatory")


class _MscMpanlFrmFromIf_Type(Unsigned32):
    """Custom type mscMpanlFrmFromIf based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscMpanlFrmFromIf_Type.__name__ = "Unsigned32"
_MscMpanlFrmFromIf_Object = MibTableColumn
mscMpanlFrmFromIf = _MscMpanlFrmFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 17, 1, 3),
    _MscMpanlFrmFromIf_Type()
)
mscMpanlFrmFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlFrmFromIf.setStatus("mandatory")


class _MscMpanlOctetFromIf_Type(Unsigned32):
    """Custom type mscMpanlOctetFromIf based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscMpanlOctetFromIf_Type.__name__ = "Unsigned32"
_MscMpanlOctetFromIf_Object = MibTableColumn
mscMpanlOctetFromIf = _MscMpanlOctetFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 17, 1, 4),
    _MscMpanlOctetFromIf_Type()
)
mscMpanlOctetFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlOctetFromIf.setStatus("mandatory")
_MscMpanlVoFr_ObjectIdentity = ObjectIdentity
mscMpanlVoFr = _MscMpanlVoFr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 18)
)
_MscMpanlVoFrRowStatusTable_Object = MibTable
mscMpanlVoFrRowStatusTable = _MscMpanlVoFrRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 18, 1)
)
if mibBuilder.loadTexts:
    mscMpanlVoFrRowStatusTable.setStatus("mandatory")
_MscMpanlVoFrRowStatusEntry_Object = MibTableRow
mscMpanlVoFrRowStatusEntry = _MscMpanlVoFrRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 18, 1, 1)
)
mscMpanlVoFrRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-MpaNetworkLinkMIB", "mscMpanlIndex"),
    (0, "Nortel-MsCarrier-MscPassport-MpaNetworkLinkMIB", "mscMpanlVoFrIndex"),
)
if mibBuilder.loadTexts:
    mscMpanlVoFrRowStatusEntry.setStatus("mandatory")
_MscMpanlVoFrRowStatus_Type = RowStatus
_MscMpanlVoFrRowStatus_Object = MibTableColumn
mscMpanlVoFrRowStatus = _MscMpanlVoFrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 18, 1, 1, 1),
    _MscMpanlVoFrRowStatus_Type()
)
mscMpanlVoFrRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlVoFrRowStatus.setStatus("mandatory")
_MscMpanlVoFrComponentName_Type = DisplayString
_MscMpanlVoFrComponentName_Object = MibTableColumn
mscMpanlVoFrComponentName = _MscMpanlVoFrComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 18, 1, 1, 2),
    _MscMpanlVoFrComponentName_Type()
)
mscMpanlVoFrComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlVoFrComponentName.setStatus("mandatory")
_MscMpanlVoFrStorageType_Type = StorageType
_MscMpanlVoFrStorageType_Object = MibTableColumn
mscMpanlVoFrStorageType = _MscMpanlVoFrStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 18, 1, 1, 4),
    _MscMpanlVoFrStorageType_Type()
)
mscMpanlVoFrStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlVoFrStorageType.setStatus("mandatory")
_MscMpanlVoFrIndex_Type = NonReplicated
_MscMpanlVoFrIndex_Object = MibTableColumn
mscMpanlVoFrIndex = _MscMpanlVoFrIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 18, 1, 1, 10),
    _MscMpanlVoFrIndex_Type()
)
mscMpanlVoFrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscMpanlVoFrIndex.setStatus("mandatory")
_MscMpanlVoFrOperTable_Object = MibTable
mscMpanlVoFrOperTable = _MscMpanlVoFrOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 18, 10)
)
if mibBuilder.loadTexts:
    mscMpanlVoFrOperTable.setStatus("mandatory")
_MscMpanlVoFrOperEntry_Object = MibTableRow
mscMpanlVoFrOperEntry = _MscMpanlVoFrOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 18, 10, 1)
)
mscMpanlVoFrOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-MpaNetworkLinkMIB", "mscMpanlIndex"),
    (0, "Nortel-MsCarrier-MscPassport-MpaNetworkLinkMIB", "mscMpanlVoFrIndex"),
)
if mibBuilder.loadTexts:
    mscMpanlVoFrOperEntry.setStatus("mandatory")
_MscMpanlVoFrMaximumFrameSize_Type = Counter32
_MscMpanlVoFrMaximumFrameSize_Object = MibTableColumn
mscMpanlVoFrMaximumFrameSize = _MscMpanlVoFrMaximumFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 18, 10, 1, 1),
    _MscMpanlVoFrMaximumFrameSize_Type()
)
mscMpanlVoFrMaximumFrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlVoFrMaximumFrameSize.setStatus("mandatory")
_MscMpanlVoFrTransmitInformationRate_Type = Counter32
_MscMpanlVoFrTransmitInformationRate_Object = MibTableColumn
mscMpanlVoFrTransmitInformationRate = _MscMpanlVoFrTransmitInformationRate_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 18, 10, 1, 2),
    _MscMpanlVoFrTransmitInformationRate_Type()
)
mscMpanlVoFrTransmitInformationRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlVoFrTransmitInformationRate.setStatus("mandatory")
_MscMpanlVoFrStatsTable_Object = MibTable
mscMpanlVoFrStatsTable = _MscMpanlVoFrStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 18, 11)
)
if mibBuilder.loadTexts:
    mscMpanlVoFrStatsTable.setStatus("mandatory")
_MscMpanlVoFrStatsEntry_Object = MibTableRow
mscMpanlVoFrStatsEntry = _MscMpanlVoFrStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 18, 11, 1)
)
mscMpanlVoFrStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-MpaNetworkLinkMIB", "mscMpanlIndex"),
    (0, "Nortel-MsCarrier-MscPassport-MpaNetworkLinkMIB", "mscMpanlVoFrIndex"),
)
if mibBuilder.loadTexts:
    mscMpanlVoFrStatsEntry.setStatus("mandatory")
_MscMpanlVoFrFragmentedHighestPriorityFrames_Type = Counter32
_MscMpanlVoFrFragmentedHighestPriorityFrames_Object = MibTableColumn
mscMpanlVoFrFragmentedHighestPriorityFrames = _MscMpanlVoFrFragmentedHighestPriorityFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 18, 11, 1, 1),
    _MscMpanlVoFrFragmentedHighestPriorityFrames_Type()
)
mscMpanlVoFrFragmentedHighestPriorityFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlVoFrFragmentedHighestPriorityFrames.setStatus("mandatory")
_MscMpanlVoFrLostFragmentsFromIf_Type = Counter32
_MscMpanlVoFrLostFragmentsFromIf_Object = MibTableColumn
mscMpanlVoFrLostFragmentsFromIf = _MscMpanlVoFrLostFragmentsFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 18, 11, 1, 5),
    _MscMpanlVoFrLostFragmentsFromIf_Type()
)
mscMpanlVoFrLostFragmentsFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlVoFrLostFragmentsFromIf.setStatus("mandatory")
_MscMpanlVoFrProtocolViolationsFromIf_Type = Counter32
_MscMpanlVoFrProtocolViolationsFromIf_Object = MibTableColumn
mscMpanlVoFrProtocolViolationsFromIf = _MscMpanlVoFrProtocolViolationsFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 18, 11, 1, 6),
    _MscMpanlVoFrProtocolViolationsFromIf_Type()
)
mscMpanlVoFrProtocolViolationsFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlVoFrProtocolViolationsFromIf.setStatus("mandatory")
_MscMpanlFrMuxSetup_ObjectIdentity = ObjectIdentity
mscMpanlFrMuxSetup = _MscMpanlFrMuxSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 19)
)
_MscMpanlFrMuxSetupRowStatusTable_Object = MibTable
mscMpanlFrMuxSetupRowStatusTable = _MscMpanlFrMuxSetupRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 19, 1)
)
if mibBuilder.loadTexts:
    mscMpanlFrMuxSetupRowStatusTable.setStatus("mandatory")
_MscMpanlFrMuxSetupRowStatusEntry_Object = MibTableRow
mscMpanlFrMuxSetupRowStatusEntry = _MscMpanlFrMuxSetupRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 19, 1, 1)
)
mscMpanlFrMuxSetupRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-MpaNetworkLinkMIB", "mscMpanlIndex"),
    (0, "Nortel-MsCarrier-MscPassport-MpaNetworkLinkMIB", "mscMpanlFrMuxSetupIndex"),
)
if mibBuilder.loadTexts:
    mscMpanlFrMuxSetupRowStatusEntry.setStatus("mandatory")
_MscMpanlFrMuxSetupRowStatus_Type = RowStatus
_MscMpanlFrMuxSetupRowStatus_Object = MibTableColumn
mscMpanlFrMuxSetupRowStatus = _MscMpanlFrMuxSetupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 19, 1, 1, 1),
    _MscMpanlFrMuxSetupRowStatus_Type()
)
mscMpanlFrMuxSetupRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscMpanlFrMuxSetupRowStatus.setStatus("mandatory")
_MscMpanlFrMuxSetupComponentName_Type = DisplayString
_MscMpanlFrMuxSetupComponentName_Object = MibTableColumn
mscMpanlFrMuxSetupComponentName = _MscMpanlFrMuxSetupComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 19, 1, 1, 2),
    _MscMpanlFrMuxSetupComponentName_Type()
)
mscMpanlFrMuxSetupComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlFrMuxSetupComponentName.setStatus("mandatory")
_MscMpanlFrMuxSetupStorageType_Type = StorageType
_MscMpanlFrMuxSetupStorageType_Object = MibTableColumn
mscMpanlFrMuxSetupStorageType = _MscMpanlFrMuxSetupStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 19, 1, 1, 4),
    _MscMpanlFrMuxSetupStorageType_Type()
)
mscMpanlFrMuxSetupStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlFrMuxSetupStorageType.setStatus("mandatory")
_MscMpanlFrMuxSetupIndex_Type = NonReplicated
_MscMpanlFrMuxSetupIndex_Object = MibTableColumn
mscMpanlFrMuxSetupIndex = _MscMpanlFrMuxSetupIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 19, 1, 1, 10),
    _MscMpanlFrMuxSetupIndex_Type()
)
mscMpanlFrMuxSetupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscMpanlFrMuxSetupIndex.setStatus("mandatory")
_MscMpanlFrMuxSetupPvcSetup_ObjectIdentity = ObjectIdentity
mscMpanlFrMuxSetupPvcSetup = _MscMpanlFrMuxSetupPvcSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 19, 2)
)
_MscMpanlFrMuxSetupPvcSetupRowStatusTable_Object = MibTable
mscMpanlFrMuxSetupPvcSetupRowStatusTable = _MscMpanlFrMuxSetupPvcSetupRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 19, 2, 1)
)
if mibBuilder.loadTexts:
    mscMpanlFrMuxSetupPvcSetupRowStatusTable.setStatus("mandatory")
_MscMpanlFrMuxSetupPvcSetupRowStatusEntry_Object = MibTableRow
mscMpanlFrMuxSetupPvcSetupRowStatusEntry = _MscMpanlFrMuxSetupPvcSetupRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 19, 2, 1, 1)
)
mscMpanlFrMuxSetupPvcSetupRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-MpaNetworkLinkMIB", "mscMpanlIndex"),
    (0, "Nortel-MsCarrier-MscPassport-MpaNetworkLinkMIB", "mscMpanlFrMuxSetupIndex"),
    (0, "Nortel-MsCarrier-MscPassport-MpaNetworkLinkMIB", "mscMpanlFrMuxSetupPvcSetupIndex"),
)
if mibBuilder.loadTexts:
    mscMpanlFrMuxSetupPvcSetupRowStatusEntry.setStatus("mandatory")
_MscMpanlFrMuxSetupPvcSetupRowStatus_Type = RowStatus
_MscMpanlFrMuxSetupPvcSetupRowStatus_Object = MibTableColumn
mscMpanlFrMuxSetupPvcSetupRowStatus = _MscMpanlFrMuxSetupPvcSetupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 19, 2, 1, 1, 1),
    _MscMpanlFrMuxSetupPvcSetupRowStatus_Type()
)
mscMpanlFrMuxSetupPvcSetupRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlFrMuxSetupPvcSetupRowStatus.setStatus("mandatory")
_MscMpanlFrMuxSetupPvcSetupComponentName_Type = DisplayString
_MscMpanlFrMuxSetupPvcSetupComponentName_Object = MibTableColumn
mscMpanlFrMuxSetupPvcSetupComponentName = _MscMpanlFrMuxSetupPvcSetupComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 19, 2, 1, 1, 2),
    _MscMpanlFrMuxSetupPvcSetupComponentName_Type()
)
mscMpanlFrMuxSetupPvcSetupComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlFrMuxSetupPvcSetupComponentName.setStatus("mandatory")
_MscMpanlFrMuxSetupPvcSetupStorageType_Type = StorageType
_MscMpanlFrMuxSetupPvcSetupStorageType_Object = MibTableColumn
mscMpanlFrMuxSetupPvcSetupStorageType = _MscMpanlFrMuxSetupPvcSetupStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 19, 2, 1, 1, 4),
    _MscMpanlFrMuxSetupPvcSetupStorageType_Type()
)
mscMpanlFrMuxSetupPvcSetupStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlFrMuxSetupPvcSetupStorageType.setStatus("mandatory")
_MscMpanlFrMuxSetupPvcSetupIndex_Type = NonReplicated
_MscMpanlFrMuxSetupPvcSetupIndex_Object = MibTableColumn
mscMpanlFrMuxSetupPvcSetupIndex = _MscMpanlFrMuxSetupPvcSetupIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 19, 2, 1, 1, 10),
    _MscMpanlFrMuxSetupPvcSetupIndex_Type()
)
mscMpanlFrMuxSetupPvcSetupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscMpanlFrMuxSetupPvcSetupIndex.setStatus("mandatory")
_MscMpanlFrMuxSetupPvcSetupProvTable_Object = MibTable
mscMpanlFrMuxSetupPvcSetupProvTable = _MscMpanlFrMuxSetupPvcSetupProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 19, 2, 10)
)
if mibBuilder.loadTexts:
    mscMpanlFrMuxSetupPvcSetupProvTable.setStatus("mandatory")
_MscMpanlFrMuxSetupPvcSetupProvEntry_Object = MibTableRow
mscMpanlFrMuxSetupPvcSetupProvEntry = _MscMpanlFrMuxSetupPvcSetupProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 19, 2, 10, 1)
)
mscMpanlFrMuxSetupPvcSetupProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-MpaNetworkLinkMIB", "mscMpanlIndex"),
    (0, "Nortel-MsCarrier-MscPassport-MpaNetworkLinkMIB", "mscMpanlFrMuxSetupIndex"),
    (0, "Nortel-MsCarrier-MscPassport-MpaNetworkLinkMIB", "mscMpanlFrMuxSetupPvcSetupIndex"),
)
if mibBuilder.loadTexts:
    mscMpanlFrMuxSetupPvcSetupProvEntry.setStatus("mandatory")
_MscMpanlFrMuxSetupPvcSetupDlciName_Type = Link
_MscMpanlFrMuxSetupPvcSetupDlciName_Object = MibTableColumn
mscMpanlFrMuxSetupPvcSetupDlciName = _MscMpanlFrMuxSetupPvcSetupDlciName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 19, 2, 10, 1, 1),
    _MscMpanlFrMuxSetupPvcSetupDlciName_Type()
)
mscMpanlFrMuxSetupPvcSetupDlciName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscMpanlFrMuxSetupPvcSetupDlciName.setStatus("mandatory")
_MscMpanlFrMuxSetupOpTable_Object = MibTable
mscMpanlFrMuxSetupOpTable = _MscMpanlFrMuxSetupOpTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 19, 11)
)
if mibBuilder.loadTexts:
    mscMpanlFrMuxSetupOpTable.setStatus("mandatory")
_MscMpanlFrMuxSetupOpEntry_Object = MibTableRow
mscMpanlFrMuxSetupOpEntry = _MscMpanlFrMuxSetupOpEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 19, 11, 1)
)
mscMpanlFrMuxSetupOpEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-MpaNetworkLinkMIB", "mscMpanlIndex"),
    (0, "Nortel-MsCarrier-MscPassport-MpaNetworkLinkMIB", "mscMpanlFrMuxSetupIndex"),
)
if mibBuilder.loadTexts:
    mscMpanlFrMuxSetupOpEntry.setStatus("mandatory")


class _MscMpanlFrMuxSetupCommittedInformationRate_Type(Unsigned32):
    """Custom type mscMpanlFrMuxSetupCommittedInformationRate based on Unsigned32"""
    defaultValue = 16000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16000, 4294967295),
    )


_MscMpanlFrMuxSetupCommittedInformationRate_Type.__name__ = "Unsigned32"
_MscMpanlFrMuxSetupCommittedInformationRate_Object = MibTableColumn
mscMpanlFrMuxSetupCommittedInformationRate = _MscMpanlFrMuxSetupCommittedInformationRate_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 19, 11, 1, 1),
    _MscMpanlFrMuxSetupCommittedInformationRate_Type()
)
mscMpanlFrMuxSetupCommittedInformationRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlFrMuxSetupCommittedInformationRate.setStatus("mandatory")
_MscMpanlFrMuxSetupDlciCompName_Type = RowPointer
_MscMpanlFrMuxSetupDlciCompName_Object = MibTableColumn
mscMpanlFrMuxSetupDlciCompName = _MscMpanlFrMuxSetupDlciCompName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 19, 11, 1, 2),
    _MscMpanlFrMuxSetupDlciCompName_Type()
)
mscMpanlFrMuxSetupDlciCompName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlFrMuxSetupDlciCompName.setStatus("mandatory")
_MscMpanlIsdn_ObjectIdentity = ObjectIdentity
mscMpanlIsdn = _MscMpanlIsdn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 22)
)
_MscMpanlIsdnRowStatusTable_Object = MibTable
mscMpanlIsdnRowStatusTable = _MscMpanlIsdnRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 22, 1)
)
if mibBuilder.loadTexts:
    mscMpanlIsdnRowStatusTable.setStatus("mandatory")
_MscMpanlIsdnRowStatusEntry_Object = MibTableRow
mscMpanlIsdnRowStatusEntry = _MscMpanlIsdnRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 22, 1, 1)
)
mscMpanlIsdnRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-MpaNetworkLinkMIB", "mscMpanlIndex"),
    (0, "Nortel-MsCarrier-MscPassport-MpaNetworkLinkMIB", "mscMpanlIsdnIndex"),
)
if mibBuilder.loadTexts:
    mscMpanlIsdnRowStatusEntry.setStatus("mandatory")
_MscMpanlIsdnRowStatus_Type = RowStatus
_MscMpanlIsdnRowStatus_Object = MibTableColumn
mscMpanlIsdnRowStatus = _MscMpanlIsdnRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 22, 1, 1, 1),
    _MscMpanlIsdnRowStatus_Type()
)
mscMpanlIsdnRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscMpanlIsdnRowStatus.setStatus("mandatory")
_MscMpanlIsdnComponentName_Type = DisplayString
_MscMpanlIsdnComponentName_Object = MibTableColumn
mscMpanlIsdnComponentName = _MscMpanlIsdnComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 22, 1, 1, 2),
    _MscMpanlIsdnComponentName_Type()
)
mscMpanlIsdnComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlIsdnComponentName.setStatus("mandatory")
_MscMpanlIsdnStorageType_Type = StorageType
_MscMpanlIsdnStorageType_Object = MibTableColumn
mscMpanlIsdnStorageType = _MscMpanlIsdnStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 22, 1, 1, 4),
    _MscMpanlIsdnStorageType_Type()
)
mscMpanlIsdnStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlIsdnStorageType.setStatus("mandatory")
_MscMpanlIsdnIndex_Type = NonReplicated
_MscMpanlIsdnIndex_Object = MibTableColumn
mscMpanlIsdnIndex = _MscMpanlIsdnIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 22, 1, 1, 10),
    _MscMpanlIsdnIndex_Type()
)
mscMpanlIsdnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscMpanlIsdnIndex.setStatus("mandatory")
_MscMpanlIsdnProvTable_Object = MibTable
mscMpanlIsdnProvTable = _MscMpanlIsdnProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 22, 11)
)
if mibBuilder.loadTexts:
    mscMpanlIsdnProvTable.setStatus("mandatory")
_MscMpanlIsdnProvEntry_Object = MibTableRow
mscMpanlIsdnProvEntry = _MscMpanlIsdnProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 22, 11, 1)
)
mscMpanlIsdnProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-MpaNetworkLinkMIB", "mscMpanlIndex"),
    (0, "Nortel-MsCarrier-MscPassport-MpaNetworkLinkMIB", "mscMpanlIsdnIndex"),
)
if mibBuilder.loadTexts:
    mscMpanlIsdnProvEntry.setStatus("mandatory")


class _MscMpanlIsdnT320_Type(Unsigned32):
    """Custom type mscMpanlIsdnT320 based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscMpanlIsdnT320_Type.__name__ = "Unsigned32"
_MscMpanlIsdnT320_Object = MibTableColumn
mscMpanlIsdnT320 = _MscMpanlIsdnT320_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 22, 11, 1, 1),
    _MscMpanlIsdnT320_Type()
)
mscMpanlIsdnT320.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscMpanlIsdnT320.setStatus("mandatory")


class _MscMpanlIsdnAddressSignalling_Type(Integer32):
    """Custom type mscMpanlIsdnAddressSignalling based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("isdnDna", 0),
          ("normalBehavior", 1))
    )


_MscMpanlIsdnAddressSignalling_Type.__name__ = "Integer32"
_MscMpanlIsdnAddressSignalling_Object = MibTableColumn
mscMpanlIsdnAddressSignalling = _MscMpanlIsdnAddressSignalling_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 22, 11, 1, 2),
    _MscMpanlIsdnAddressSignalling_Type()
)
mscMpanlIsdnAddressSignalling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscMpanlIsdnAddressSignalling.setStatus("mandatory")
_MscMpanlIsdnOperTable_Object = MibTable
mscMpanlIsdnOperTable = _MscMpanlIsdnOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 22, 12)
)
if mibBuilder.loadTexts:
    mscMpanlIsdnOperTable.setStatus("mandatory")
_MscMpanlIsdnOperEntry_Object = MibTableRow
mscMpanlIsdnOperEntry = _MscMpanlIsdnOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 22, 12, 1)
)
mscMpanlIsdnOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-MpaNetworkLinkMIB", "mscMpanlIndex"),
    (0, "Nortel-MsCarrier-MscPassport-MpaNetworkLinkMIB", "mscMpanlIsdnIndex"),
)
if mibBuilder.loadTexts:
    mscMpanlIsdnOperEntry.setStatus("mandatory")


class _MscMpanlIsdnDataSigChan_Type(Integer32):
    """Custom type mscMpanlIsdnDataSigChan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_MscMpanlIsdnDataSigChan_Type.__name__ = "Integer32"
_MscMpanlIsdnDataSigChan_Object = MibTableColumn
mscMpanlIsdnDataSigChan = _MscMpanlIsdnDataSigChan_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 22, 12, 1, 1),
    _MscMpanlIsdnDataSigChan_Type()
)
mscMpanlIsdnDataSigChan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlIsdnDataSigChan.setStatus("mandatory")


class _MscMpanlIsdnBChannelState_Type(Integer32):
    """Custom type mscMpanlIsdnBChannelState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("busy", 1),
          ("disabled", 2),
          ("idle", 0))
    )


_MscMpanlIsdnBChannelState_Type.__name__ = "Integer32"
_MscMpanlIsdnBChannelState_Object = MibTableColumn
mscMpanlIsdnBChannelState = _MscMpanlIsdnBChannelState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 22, 12, 1, 2),
    _MscMpanlIsdnBChannelState_Type()
)
mscMpanlIsdnBChannelState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlIsdnBChannelState.setStatus("mandatory")


class _MscMpanlIsdnLastUsedCgpn_Type(DigitString):
    """Custom type mscMpanlIsdnLastUsedCgpn based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_MscMpanlIsdnLastUsedCgpn_Type.__name__ = "DigitString"
_MscMpanlIsdnLastUsedCgpn_Object = MibTableColumn
mscMpanlIsdnLastUsedCgpn = _MscMpanlIsdnLastUsedCgpn_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 22, 12, 1, 3),
    _MscMpanlIsdnLastUsedCgpn_Type()
)
mscMpanlIsdnLastUsedCgpn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlIsdnLastUsedCgpn.setStatus("mandatory")


class _MscMpanlIsdnBChanIntState_Type(Integer32):
    """Custom type mscMpanlIsdnBChanIntState based on Integer32"""
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
        *(("down", 7),
          ("enabling", 4),
          ("isdnInit", 0),
          ("releasing", 8),
          ("up", 6),
          ("waitAccEnable", 1),
          ("waitAccRegAck", 5),
          ("waitFramerData", 3),
          ("waitLnsResponse", 2))
    )


_MscMpanlIsdnBChanIntState_Type.__name__ = "Integer32"
_MscMpanlIsdnBChanIntState_Object = MibTableColumn
mscMpanlIsdnBChanIntState = _MscMpanlIsdnBChanIntState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 22, 12, 1, 4),
    _MscMpanlIsdnBChanIntState_Type()
)
mscMpanlIsdnBChanIntState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlIsdnBChanIntState.setStatus("mandatory")
_MscMpanlIsdnActiveVirtualCircuitsCount_Type = Counter32
_MscMpanlIsdnActiveVirtualCircuitsCount_Object = MibTableColumn
mscMpanlIsdnActiveVirtualCircuitsCount = _MscMpanlIsdnActiveVirtualCircuitsCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 22, 12, 1, 5),
    _MscMpanlIsdnActiveVirtualCircuitsCount_Type()
)
mscMpanlIsdnActiveVirtualCircuitsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlIsdnActiveVirtualCircuitsCount.setStatus("mandatory")
_MscMpanlIfEntryTable_Object = MibTable
mscMpanlIfEntryTable = _MscMpanlIfEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 23)
)
if mibBuilder.loadTexts:
    mscMpanlIfEntryTable.setStatus("mandatory")
_MscMpanlIfEntryEntry_Object = MibTableRow
mscMpanlIfEntryEntry = _MscMpanlIfEntryEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 23, 1)
)
mscMpanlIfEntryEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-MpaNetworkLinkMIB", "mscMpanlIndex"),
)
if mibBuilder.loadTexts:
    mscMpanlIfEntryEntry.setStatus("mandatory")


class _MscMpanlIfAdminStatus_Type(Integer32):
    """Custom type mscMpanlIfAdminStatus based on Integer32"""
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


_MscMpanlIfAdminStatus_Type.__name__ = "Integer32"
_MscMpanlIfAdminStatus_Object = MibTableColumn
mscMpanlIfAdminStatus = _MscMpanlIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 23, 1, 1),
    _MscMpanlIfAdminStatus_Type()
)
mscMpanlIfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscMpanlIfAdminStatus.setStatus("mandatory")


class _MscMpanlIfIndex_Type(InterfaceIndex):
    """Custom type mscMpanlIfIndex based on InterfaceIndex"""
    subtypeSpec = InterfaceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MscMpanlIfIndex_Type.__name__ = "InterfaceIndex"
_MscMpanlIfIndex_Object = MibTableColumn
mscMpanlIfIndex = _MscMpanlIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 23, 1, 2),
    _MscMpanlIfIndex_Type()
)
mscMpanlIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlIfIndex.setStatus("mandatory")
_MscMpanlOperStatusTable_Object = MibTable
mscMpanlOperStatusTable = _MscMpanlOperStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 24)
)
if mibBuilder.loadTexts:
    mscMpanlOperStatusTable.setStatus("mandatory")
_MscMpanlOperStatusEntry_Object = MibTableRow
mscMpanlOperStatusEntry = _MscMpanlOperStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 24, 1)
)
mscMpanlOperStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-MpaNetworkLinkMIB", "mscMpanlIndex"),
)
if mibBuilder.loadTexts:
    mscMpanlOperStatusEntry.setStatus("mandatory")


class _MscMpanlSnmpOperStatus_Type(Integer32):
    """Custom type mscMpanlSnmpOperStatus based on Integer32"""
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


_MscMpanlSnmpOperStatus_Type.__name__ = "Integer32"
_MscMpanlSnmpOperStatus_Object = MibTableColumn
mscMpanlSnmpOperStatus = _MscMpanlSnmpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 24, 1, 1),
    _MscMpanlSnmpOperStatus_Type()
)
mscMpanlSnmpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlSnmpOperStatus.setStatus("mandatory")
_MscMpanlOperTable_Object = MibTable
mscMpanlOperTable = _MscMpanlOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 25)
)
if mibBuilder.loadTexts:
    mscMpanlOperTable.setStatus("mandatory")
_MscMpanlOperEntry_Object = MibTableRow
mscMpanlOperEntry = _MscMpanlOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 25, 1)
)
mscMpanlOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-MpaNetworkLinkMIB", "mscMpanlIndex"),
)
if mibBuilder.loadTexts:
    mscMpanlOperEntry.setStatus("mandatory")


class _MscMpanlRoundTripDelay_Type(Unsigned32):
    """Custom type mscMpanlRoundTripDelay based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_MscMpanlRoundTripDelay_Type.__name__ = "Unsigned32"
_MscMpanlRoundTripDelay_Object = MibTableColumn
mscMpanlRoundTripDelay = _MscMpanlRoundTripDelay_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 25, 1, 1),
    _MscMpanlRoundTripDelay_Type()
)
mscMpanlRoundTripDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlRoundTripDelay.setStatus("mandatory")
_MscMpanlFrmToIfByQueueTable_Object = MibTable
mscMpanlFrmToIfByQueueTable = _MscMpanlFrmToIfByQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 350)
)
if mibBuilder.loadTexts:
    mscMpanlFrmToIfByQueueTable.setStatus("mandatory")
_MscMpanlFrmToIfByQueueEntry_Object = MibTableRow
mscMpanlFrmToIfByQueueEntry = _MscMpanlFrmToIfByQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 350, 1)
)
mscMpanlFrmToIfByQueueEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-MpaNetworkLinkMIB", "mscMpanlIndex"),
    (0, "Nortel-MsCarrier-MscPassport-MpaNetworkLinkMIB", "mscMpanlFrmToIfByQueueIndex"),
)
if mibBuilder.loadTexts:
    mscMpanlFrmToIfByQueueEntry.setStatus("mandatory")


class _MscMpanlFrmToIfByQueueIndex_Type(Integer32):
    """Custom type mscMpanlFrmToIfByQueueIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_MscMpanlFrmToIfByQueueIndex_Type.__name__ = "Integer32"
_MscMpanlFrmToIfByQueueIndex_Object = MibTableColumn
mscMpanlFrmToIfByQueueIndex = _MscMpanlFrmToIfByQueueIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 350, 1, 1),
    _MscMpanlFrmToIfByQueueIndex_Type()
)
mscMpanlFrmToIfByQueueIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscMpanlFrmToIfByQueueIndex.setStatus("mandatory")


class _MscMpanlFrmToIfByQueueValue_Type(Unsigned32):
    """Custom type mscMpanlFrmToIfByQueueValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscMpanlFrmToIfByQueueValue_Type.__name__ = "Unsigned32"
_MscMpanlFrmToIfByQueueValue_Object = MibTableColumn
mscMpanlFrmToIfByQueueValue = _MscMpanlFrmToIfByQueueValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 350, 1, 2),
    _MscMpanlFrmToIfByQueueValue_Type()
)
mscMpanlFrmToIfByQueueValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlFrmToIfByQueueValue.setStatus("mandatory")
_MscMpanlOctetToIfByQueueTable_Object = MibTable
mscMpanlOctetToIfByQueueTable = _MscMpanlOctetToIfByQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 351)
)
if mibBuilder.loadTexts:
    mscMpanlOctetToIfByQueueTable.setStatus("mandatory")
_MscMpanlOctetToIfByQueueEntry_Object = MibTableRow
mscMpanlOctetToIfByQueueEntry = _MscMpanlOctetToIfByQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 351, 1)
)
mscMpanlOctetToIfByQueueEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-MpaNetworkLinkMIB", "mscMpanlIndex"),
    (0, "Nortel-MsCarrier-MscPassport-MpaNetworkLinkMIB", "mscMpanlOctetToIfByQueueIndex"),
)
if mibBuilder.loadTexts:
    mscMpanlOctetToIfByQueueEntry.setStatus("mandatory")


class _MscMpanlOctetToIfByQueueIndex_Type(Integer32):
    """Custom type mscMpanlOctetToIfByQueueIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_MscMpanlOctetToIfByQueueIndex_Type.__name__ = "Integer32"
_MscMpanlOctetToIfByQueueIndex_Object = MibTableColumn
mscMpanlOctetToIfByQueueIndex = _MscMpanlOctetToIfByQueueIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 351, 1, 1),
    _MscMpanlOctetToIfByQueueIndex_Type()
)
mscMpanlOctetToIfByQueueIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscMpanlOctetToIfByQueueIndex.setStatus("mandatory")


class _MscMpanlOctetToIfByQueueValue_Type(Unsigned32):
    """Custom type mscMpanlOctetToIfByQueueValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscMpanlOctetToIfByQueueValue_Type.__name__ = "Unsigned32"
_MscMpanlOctetToIfByQueueValue_Object = MibTableColumn
mscMpanlOctetToIfByQueueValue = _MscMpanlOctetToIfByQueueValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 123, 351, 1, 2),
    _MscMpanlOctetToIfByQueueValue_Type()
)
mscMpanlOctetToIfByQueueValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMpanlOctetToIfByQueueValue.setStatus("mandatory")
_MpaNetworkLinkMIB_ObjectIdentity = ObjectIdentity
mpaNetworkLinkMIB = _MpaNetworkLinkMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 119)
)
_MpaNetworkLinkGroup_ObjectIdentity = ObjectIdentity
mpaNetworkLinkGroup = _MpaNetworkLinkGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 119, 1)
)
_MpaNetworkLinkGroupCA_ObjectIdentity = ObjectIdentity
mpaNetworkLinkGroupCA = _MpaNetworkLinkGroupCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 119, 1, 1)
)
_MpaNetworkLinkGroupCA02_ObjectIdentity = ObjectIdentity
mpaNetworkLinkGroupCA02 = _MpaNetworkLinkGroupCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 119, 1, 1, 3)
)
_MpaNetworkLinkGroupCA02A_ObjectIdentity = ObjectIdentity
mpaNetworkLinkGroupCA02A = _MpaNetworkLinkGroupCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 119, 1, 1, 3, 2)
)
_MpaNetworkLinkCapabilities_ObjectIdentity = ObjectIdentity
mpaNetworkLinkCapabilities = _MpaNetworkLinkCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 119, 3)
)
_MpaNetworkLinkCapabilitiesCA_ObjectIdentity = ObjectIdentity
mpaNetworkLinkCapabilitiesCA = _MpaNetworkLinkCapabilitiesCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 119, 3, 1)
)
_MpaNetworkLinkCapabilitiesCA02_ObjectIdentity = ObjectIdentity
mpaNetworkLinkCapabilitiesCA02 = _MpaNetworkLinkCapabilitiesCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 119, 3, 1, 3)
)
_MpaNetworkLinkCapabilitiesCA02A_ObjectIdentity = ObjectIdentity
mpaNetworkLinkCapabilitiesCA02A = _MpaNetworkLinkCapabilitiesCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 119, 3, 1, 3, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-MsCarrier-MscPassport-MpaNetworkLinkMIB",
    **{"mscMpanl": mscMpanl,
       "mscMpanlRowStatusTable": mscMpanlRowStatusTable,
       "mscMpanlRowStatusEntry": mscMpanlRowStatusEntry,
       "mscMpanlRowStatus": mscMpanlRowStatus,
       "mscMpanlComponentName": mscMpanlComponentName,
       "mscMpanlStorageType": mscMpanlStorageType,
       "mscMpanlIndex": mscMpanlIndex,
       "mscMpanlDna": mscMpanlDna,
       "mscMpanlDnaRowStatusTable": mscMpanlDnaRowStatusTable,
       "mscMpanlDnaRowStatusEntry": mscMpanlDnaRowStatusEntry,
       "mscMpanlDnaRowStatus": mscMpanlDnaRowStatus,
       "mscMpanlDnaComponentName": mscMpanlDnaComponentName,
       "mscMpanlDnaStorageType": mscMpanlDnaStorageType,
       "mscMpanlDnaIndex": mscMpanlDnaIndex,
       "mscMpanlDnaOutgoingOptionsTable": mscMpanlDnaOutgoingOptionsTable,
       "mscMpanlDnaOutgoingOptionsEntry": mscMpanlDnaOutgoingOptionsEntry,
       "mscMpanlDnaDefaultTransferPriority": mscMpanlDnaDefaultTransferPriority,
       "mscMpanlDnaCallOptionsTable": mscMpanlDnaCallOptionsTable,
       "mscMpanlDnaCallOptionsEntry": mscMpanlDnaCallOptionsEntry,
       "mscMpanlDnaAccountClass": mscMpanlDnaAccountClass,
       "mscMpanlDnaAccountCollection": mscMpanlDnaAccountCollection,
       "mscMpanlDnaServiceExchange": mscMpanlDnaServiceExchange,
       "mscMpanlDnaEgressAccounting": mscMpanlDnaEgressAccounting,
       "mscMpanlFramer": mscMpanlFramer,
       "mscMpanlFramerRowStatusTable": mscMpanlFramerRowStatusTable,
       "mscMpanlFramerRowStatusEntry": mscMpanlFramerRowStatusEntry,
       "mscMpanlFramerRowStatus": mscMpanlFramerRowStatus,
       "mscMpanlFramerComponentName": mscMpanlFramerComponentName,
       "mscMpanlFramerStorageType": mscMpanlFramerStorageType,
       "mscMpanlFramerIndex": mscMpanlFramerIndex,
       "mscMpanlFramerProvTable": mscMpanlFramerProvTable,
       "mscMpanlFramerProvEntry": mscMpanlFramerProvEntry,
       "mscMpanlFramerInterfaceName": mscMpanlFramerInterfaceName,
       "mscMpanlFramerLinkTable": mscMpanlFramerLinkTable,
       "mscMpanlFramerLinkEntry": mscMpanlFramerLinkEntry,
       "mscMpanlFramerDataInversion": mscMpanlFramerDataInversion,
       "mscMpanlFramerFrameCrcType": mscMpanlFramerFrameCrcType,
       "mscMpanlFramerFlagsBetweenFrames": mscMpanlFramerFlagsBetweenFrames,
       "mscMpanlFramerStateTable": mscMpanlFramerStateTable,
       "mscMpanlFramerStateEntry": mscMpanlFramerStateEntry,
       "mscMpanlFramerAdminState": mscMpanlFramerAdminState,
       "mscMpanlFramerOperationalState": mscMpanlFramerOperationalState,
       "mscMpanlFramerUsageState": mscMpanlFramerUsageState,
       "mscMpanlFramerStatsTable": mscMpanlFramerStatsTable,
       "mscMpanlFramerStatsEntry": mscMpanlFramerStatsEntry,
       "mscMpanlFramerFrmToIf": mscMpanlFramerFrmToIf,
       "mscMpanlFramerFrmFromIf": mscMpanlFramerFrmFromIf,
       "mscMpanlFramerOctetFromIf": mscMpanlFramerOctetFromIf,
       "mscMpanlFramerAborts": mscMpanlFramerAborts,
       "mscMpanlFramerCrcErrors": mscMpanlFramerCrcErrors,
       "mscMpanlFramerLrcErrors": mscMpanlFramerLrcErrors,
       "mscMpanlFramerNonOctetErrors": mscMpanlFramerNonOctetErrors,
       "mscMpanlFramerOverruns": mscMpanlFramerOverruns,
       "mscMpanlFramerUnderruns": mscMpanlFramerUnderruns,
       "mscMpanlFramerLargeFrmErrors": mscMpanlFramerLargeFrmErrors,
       "mscMpanlFramerFrmModeErrors": mscMpanlFramerFrmModeErrors,
       "mscMpanlFramerFrmToIf64": mscMpanlFramerFrmToIf64,
       "mscMpanlFramerFrmFromIf64": mscMpanlFramerFrmFromIf64,
       "mscMpanlFramerOctetFromIf64": mscMpanlFramerOctetFromIf64,
       "mscMpanlFramerUtilTable": mscMpanlFramerUtilTable,
       "mscMpanlFramerUtilEntry": mscMpanlFramerUtilEntry,
       "mscMpanlFramerNormPrioLinkUtilToIf": mscMpanlFramerNormPrioLinkUtilToIf,
       "mscMpanlFramerNormPrioLinkUtilFromIf": mscMpanlFramerNormPrioLinkUtilFromIf,
       "mscMpanlPrefixDna": mscMpanlPrefixDna,
       "mscMpanlPrefixDnaRowStatusTable": mscMpanlPrefixDnaRowStatusTable,
       "mscMpanlPrefixDnaRowStatusEntry": mscMpanlPrefixDnaRowStatusEntry,
       "mscMpanlPrefixDnaRowStatus": mscMpanlPrefixDnaRowStatus,
       "mscMpanlPrefixDnaComponentName": mscMpanlPrefixDnaComponentName,
       "mscMpanlPrefixDnaStorageType": mscMpanlPrefixDnaStorageType,
       "mscMpanlPrefixDnaNumberingPlanIndicatorIndex": mscMpanlPrefixDnaNumberingPlanIndicatorIndex,
       "mscMpanlPrefixDnaDataNetworkAddressIndex": mscMpanlPrefixDnaDataNetworkAddressIndex,
       "mscMpanlDlci": mscMpanlDlci,
       "mscMpanlDlciRowStatusTable": mscMpanlDlciRowStatusTable,
       "mscMpanlDlciRowStatusEntry": mscMpanlDlciRowStatusEntry,
       "mscMpanlDlciRowStatus": mscMpanlDlciRowStatus,
       "mscMpanlDlciComponentName": mscMpanlDlciComponentName,
       "mscMpanlDlciStorageType": mscMpanlDlciStorageType,
       "mscMpanlDlciIndex": mscMpanlDlciIndex,
       "mscMpanlDlciLb": mscMpanlDlciLb,
       "mscMpanlDlciLbRowStatusTable": mscMpanlDlciLbRowStatusTable,
       "mscMpanlDlciLbRowStatusEntry": mscMpanlDlciLbRowStatusEntry,
       "mscMpanlDlciLbRowStatus": mscMpanlDlciLbRowStatus,
       "mscMpanlDlciLbComponentName": mscMpanlDlciLbComponentName,
       "mscMpanlDlciLbStorageType": mscMpanlDlciLbStorageType,
       "mscMpanlDlciLbIndex": mscMpanlDlciLbIndex,
       "mscMpanlDlciLbStatsTable": mscMpanlDlciLbStatsTable,
       "mscMpanlDlciLbStatsEntry": mscMpanlDlciLbStatsEntry,
       "mscMpanlDlciLbLocalTotalFrm": mscMpanlDlciLbLocalTotalFrm,
       "mscMpanlDlciLbLocalTotalBytes": mscMpanlDlciLbLocalTotalBytes,
       "mscMpanlDlciLbLocalFecnFrm": mscMpanlDlciLbLocalFecnFrm,
       "mscMpanlDlciLbLocalBecnFrm": mscMpanlDlciLbLocalBecnFrm,
       "mscMpanlDlciLbLocalDeFrm": mscMpanlDlciLbLocalDeFrm,
       "mscMpanlDlciLbLocalDeBytes": mscMpanlDlciLbLocalDeBytes,
       "mscMpanlDlciLbRemoteTotalFrm": mscMpanlDlciLbRemoteTotalFrm,
       "mscMpanlDlciLbRemoteTotalBytes": mscMpanlDlciLbRemoteTotalBytes,
       "mscMpanlDlciLbRemoteFecnFrm": mscMpanlDlciLbRemoteFecnFrm,
       "mscMpanlDlciLbRemoteBecnFrm": mscMpanlDlciLbRemoteBecnFrm,
       "mscMpanlDlciLbRemoteDeFrm": mscMpanlDlciLbRemoteDeFrm,
       "mscMpanlDlciLbRemoteDeBytes": mscMpanlDlciLbRemoteDeBytes,
       "mscMpanlDlciVc": mscMpanlDlciVc,
       "mscMpanlDlciVcRowStatusTable": mscMpanlDlciVcRowStatusTable,
       "mscMpanlDlciVcRowStatusEntry": mscMpanlDlciVcRowStatusEntry,
       "mscMpanlDlciVcRowStatus": mscMpanlDlciVcRowStatus,
       "mscMpanlDlciVcComponentName": mscMpanlDlciVcComponentName,
       "mscMpanlDlciVcStorageType": mscMpanlDlciVcStorageType,
       "mscMpanlDlciVcIndex": mscMpanlDlciVcIndex,
       "mscMpanlDlciVcCadTable": mscMpanlDlciVcCadTable,
       "mscMpanlDlciVcCadEntry": mscMpanlDlciVcCadEntry,
       "mscMpanlDlciVcType": mscMpanlDlciVcType,
       "mscMpanlDlciVcState": mscMpanlDlciVcState,
       "mscMpanlDlciVcPreviousState": mscMpanlDlciVcPreviousState,
       "mscMpanlDlciVcDiagnosticCode": mscMpanlDlciVcDiagnosticCode,
       "mscMpanlDlciVcPreviousDiagnosticCode": mscMpanlDlciVcPreviousDiagnosticCode,
       "mscMpanlDlciVcCalledNpi": mscMpanlDlciVcCalledNpi,
       "mscMpanlDlciVcCalledDna": mscMpanlDlciVcCalledDna,
       "mscMpanlDlciVcCalledLcn": mscMpanlDlciVcCalledLcn,
       "mscMpanlDlciVcCallingNpi": mscMpanlDlciVcCallingNpi,
       "mscMpanlDlciVcCallingDna": mscMpanlDlciVcCallingDna,
       "mscMpanlDlciVcCallingLcn": mscMpanlDlciVcCallingLcn,
       "mscMpanlDlciVcAccountingEnabled": mscMpanlDlciVcAccountingEnabled,
       "mscMpanlDlciVcFastSelectCall": mscMpanlDlciVcFastSelectCall,
       "mscMpanlDlciVcPathReliability": mscMpanlDlciVcPathReliability,
       "mscMpanlDlciVcAccountingEnd": mscMpanlDlciVcAccountingEnd,
       "mscMpanlDlciVcPriority": mscMpanlDlciVcPriority,
       "mscMpanlDlciVcSegmentSize": mscMpanlDlciVcSegmentSize,
       "mscMpanlDlciVcMaxSubnetPktSize": mscMpanlDlciVcMaxSubnetPktSize,
       "mscMpanlDlciVcRcosToNetwork": mscMpanlDlciVcRcosToNetwork,
       "mscMpanlDlciVcRcosFromNetwork": mscMpanlDlciVcRcosFromNetwork,
       "mscMpanlDlciVcEmissionPriorityToNetwork": mscMpanlDlciVcEmissionPriorityToNetwork,
       "mscMpanlDlciVcEmissionPriorityFromNetwork": mscMpanlDlciVcEmissionPriorityFromNetwork,
       "mscMpanlDlciVcDataPath": mscMpanlDlciVcDataPath,
       "mscMpanlDlciVcIntdTable": mscMpanlDlciVcIntdTable,
       "mscMpanlDlciVcIntdEntry": mscMpanlDlciVcIntdEntry,
       "mscMpanlDlciVcCallReferenceNumber": mscMpanlDlciVcCallReferenceNumber,
       "mscMpanlDlciVcElapsedTimeTillNow": mscMpanlDlciVcElapsedTimeTillNow,
       "mscMpanlDlciVcSegmentsRx": mscMpanlDlciVcSegmentsRx,
       "mscMpanlDlciVcSegmentsSent": mscMpanlDlciVcSegmentsSent,
       "mscMpanlDlciVcStartTime": mscMpanlDlciVcStartTime,
       "mscMpanlDlciVcCallReferenceNumberDecimal": mscMpanlDlciVcCallReferenceNumberDecimal,
       "mscMpanlDlciVcFrdTable": mscMpanlDlciVcFrdTable,
       "mscMpanlDlciVcFrdEntry": mscMpanlDlciVcFrdEntry,
       "mscMpanlDlciVcFrmCongestedToSubnet": mscMpanlDlciVcFrmCongestedToSubnet,
       "mscMpanlDlciVcCannotForwardToSubnet": mscMpanlDlciVcCannotForwardToSubnet,
       "mscMpanlDlciVcNotDataXferToSubnet": mscMpanlDlciVcNotDataXferToSubnet,
       "mscMpanlDlciVcOutOfRangeFrmFromSubnet": mscMpanlDlciVcOutOfRangeFrmFromSubnet,
       "mscMpanlDlciVcCombErrorsFromSubnet": mscMpanlDlciVcCombErrorsFromSubnet,
       "mscMpanlDlciVcDuplicatesFromSubnet": mscMpanlDlciVcDuplicatesFromSubnet,
       "mscMpanlDlciVcNotDataXferFromSubnet": mscMpanlDlciVcNotDataXferFromSubnet,
       "mscMpanlDlciVcFrmLossTimeouts": mscMpanlDlciVcFrmLossTimeouts,
       "mscMpanlDlciVcOoSeqByteCntExceeded": mscMpanlDlciVcOoSeqByteCntExceeded,
       "mscMpanlDlciVcPeakOoSeqPktCount": mscMpanlDlciVcPeakOoSeqPktCount,
       "mscMpanlDlciVcPeakOoSeqFrmForwarded": mscMpanlDlciVcPeakOoSeqFrmForwarded,
       "mscMpanlDlciVcSendSequenceNumber": mscMpanlDlciVcSendSequenceNumber,
       "mscMpanlDlciVcPktRetryTimeouts": mscMpanlDlciVcPktRetryTimeouts,
       "mscMpanlDlciVcPeakRetryQueueSize": mscMpanlDlciVcPeakRetryQueueSize,
       "mscMpanlDlciVcSubnetRecoveries": mscMpanlDlciVcSubnetRecoveries,
       "mscMpanlDlciVcOoSeqPktCntExceeded": mscMpanlDlciVcOoSeqPktCntExceeded,
       "mscMpanlDlciVcPeakOoSeqByteCount": mscMpanlDlciVcPeakOoSeqByteCount,
       "mscMpanlDlciVcDmepTable": mscMpanlDlciVcDmepTable,
       "mscMpanlDlciVcDmepEntry": mscMpanlDlciVcDmepEntry,
       "mscMpanlDlciVcDmepValue": mscMpanlDlciVcDmepValue,
       "mscMpanlDlciLCo": mscMpanlDlciLCo,
       "mscMpanlDlciLCoRowStatusTable": mscMpanlDlciLCoRowStatusTable,
       "mscMpanlDlciLCoRowStatusEntry": mscMpanlDlciLCoRowStatusEntry,
       "mscMpanlDlciLCoRowStatus": mscMpanlDlciLCoRowStatus,
       "mscMpanlDlciLCoComponentName": mscMpanlDlciLCoComponentName,
       "mscMpanlDlciLCoStorageType": mscMpanlDlciLCoStorageType,
       "mscMpanlDlciLCoIndex": mscMpanlDlciLCoIndex,
       "mscMpanlDlciLCoPathDataTable": mscMpanlDlciLCoPathDataTable,
       "mscMpanlDlciLCoPathDataEntry": mscMpanlDlciLCoPathDataEntry,
       "mscMpanlDlciLCoState": mscMpanlDlciLCoState,
       "mscMpanlDlciLCoEnd": mscMpanlDlciLCoEnd,
       "mscMpanlDlciLCoCostMetric": mscMpanlDlciLCoCostMetric,
       "mscMpanlDlciLCoDelayMetric": mscMpanlDlciLCoDelayMetric,
       "mscMpanlDlciLCoRoundTripDelay": mscMpanlDlciLCoRoundTripDelay,
       "mscMpanlDlciLCoSetupPriority": mscMpanlDlciLCoSetupPriority,
       "mscMpanlDlciLCoHoldingPriority": mscMpanlDlciLCoHoldingPriority,
       "mscMpanlDlciLCoRequiredTxBandwidth": mscMpanlDlciLCoRequiredTxBandwidth,
       "mscMpanlDlciLCoRequiredRxBandwidth": mscMpanlDlciLCoRequiredRxBandwidth,
       "mscMpanlDlciLCoRequiredTrafficType": mscMpanlDlciLCoRequiredTrafficType,
       "mscMpanlDlciLCoPermittedTrunkTypes": mscMpanlDlciLCoPermittedTrunkTypes,
       "mscMpanlDlciLCoRequiredSecurity": mscMpanlDlciLCoRequiredSecurity,
       "mscMpanlDlciLCoRequiredCustomerParameter": mscMpanlDlciLCoRequiredCustomerParameter,
       "mscMpanlDlciLCoEmissionPriority": mscMpanlDlciLCoEmissionPriority,
       "mscMpanlDlciLCoDiscardPriority": mscMpanlDlciLCoDiscardPriority,
       "mscMpanlDlciLCoRetryCount": mscMpanlDlciLCoRetryCount,
       "mscMpanlDlciLCoPathFailureCount": mscMpanlDlciLCoPathFailureCount,
       "mscMpanlDlciLCoReasonForNoRoute": mscMpanlDlciLCoReasonForNoRoute,
       "mscMpanlDlciLCoLastTearDownReason": mscMpanlDlciLCoLastTearDownReason,
       "mscMpanlDlciLCoPathFailureAction": mscMpanlDlciLCoPathFailureAction,
       "mscMpanlDlciLCoBumpPreference": mscMpanlDlciLCoBumpPreference,
       "mscMpanlDlciLCoOptimization": mscMpanlDlciLCoOptimization,
       "mscMpanlDlciLCoPathUpDateTime": mscMpanlDlciLCoPathUpDateTime,
       "mscMpanlDlciLCoStatsTable": mscMpanlDlciLCoStatsTable,
       "mscMpanlDlciLCoStatsEntry": mscMpanlDlciLCoStatsEntry,
       "mscMpanlDlciLCoPktsToNetwork": mscMpanlDlciLCoPktsToNetwork,
       "mscMpanlDlciLCoBytesToNetwork": mscMpanlDlciLCoBytesToNetwork,
       "mscMpanlDlciLCoPktsFromNetwork": mscMpanlDlciLCoPktsFromNetwork,
       "mscMpanlDlciLCoBytesFromNetwork": mscMpanlDlciLCoBytesFromNetwork,
       "mscMpanlDlciLCoCallDataTable": mscMpanlDlciLCoCallDataTable,
       "mscMpanlDlciLCoCallDataEntry": mscMpanlDlciLCoCallDataEntry,
       "mscMpanlDlciLCoCallingNpi": mscMpanlDlciLCoCallingNpi,
       "mscMpanlDlciLCoCallingDna": mscMpanlDlciLCoCallingDna,
       "mscMpanlDlciLCoElapsedTimeTillNow": mscMpanlDlciLCoElapsedTimeTillNow,
       "mscMpanlDlciLCoCallReferenceNumber": mscMpanlDlciLCoCallReferenceNumber,
       "mscMpanlDlciLCoCalledNpi": mscMpanlDlciLCoCalledNpi,
       "mscMpanlDlciLCoCalledDna": mscMpanlDlciLCoCalledDna,
       "mscMpanlDlciLCoPathTable": mscMpanlDlciLCoPathTable,
       "mscMpanlDlciLCoPathEntry": mscMpanlDlciLCoPathEntry,
       "mscMpanlDlciLCoPathValue": mscMpanlDlciLCoPathValue,
       "mscMpanlDlciJvc": mscMpanlDlciJvc,
       "mscMpanlDlciJvcRowStatusTable": mscMpanlDlciJvcRowStatusTable,
       "mscMpanlDlciJvcRowStatusEntry": mscMpanlDlciJvcRowStatusEntry,
       "mscMpanlDlciJvcRowStatus": mscMpanlDlciJvcRowStatus,
       "mscMpanlDlciJvcComponentName": mscMpanlDlciJvcComponentName,
       "mscMpanlDlciJvcStorageType": mscMpanlDlciJvcStorageType,
       "mscMpanlDlciJvcIndex": mscMpanlDlciJvcIndex,
       "mscMpanlDlciJvcOperTable": mscMpanlDlciJvcOperTable,
       "mscMpanlDlciJvcOperEntry": mscMpanlDlciJvcOperEntry,
       "mscMpanlDlciJvcCurrentState": mscMpanlDlciJvcCurrentState,
       "mscMpanlDlciJvcPreviousState": mscMpanlDlciJvcPreviousState,
       "mscMpanlDlciJvcCallingNpi": mscMpanlDlciJvcCallingNpi,
       "mscMpanlDlciJvcCallingAddress": mscMpanlDlciJvcCallingAddress,
       "mscMpanlDlciJvcCallingLcn": mscMpanlDlciJvcCallingLcn,
       "mscMpanlDlciJvcCalledNpi": mscMpanlDlciJvcCalledNpi,
       "mscMpanlDlciJvcCalledAddress": mscMpanlDlciJvcCalledAddress,
       "mscMpanlDlciJvcCalledLcn": mscMpanlDlciJvcCalledLcn,
       "mscMpanlDlciJvcStatTable": mscMpanlDlciJvcStatTable,
       "mscMpanlDlciJvcStatEntry": mscMpanlDlciJvcStatEntry,
       "mscMpanlDlciJvcPacketsFromSubnet": mscMpanlDlciJvcPacketsFromSubnet,
       "mscMpanlDlciJvcPacketsToSubnet": mscMpanlDlciJvcPacketsToSubnet,
       "mscMpanlDlciJvcPacketsDiscarded": mscMpanlDlciJvcPacketsDiscarded,
       "mscMpanlDlciJvcProtocolErrors": mscMpanlDlciJvcProtocolErrors,
       "mscMpanlDlciStateTable": mscMpanlDlciStateTable,
       "mscMpanlDlciStateEntry": mscMpanlDlciStateEntry,
       "mscMpanlDlciAdminState": mscMpanlDlciAdminState,
       "mscMpanlDlciOperationalState": mscMpanlDlciOperationalState,
       "mscMpanlDlciUsageState": mscMpanlDlciUsageState,
       "mscMpanlDlciAvailabilityStatus": mscMpanlDlciAvailabilityStatus,
       "mscMpanlDlciProceduralStatus": mscMpanlDlciProceduralStatus,
       "mscMpanlDlciControlStatus": mscMpanlDlciControlStatus,
       "mscMpanlDlciAlarmStatus": mscMpanlDlciAlarmStatus,
       "mscMpanlDlciStandbyStatus": mscMpanlDlciStandbyStatus,
       "mscMpanlDlciUnknownStatus": mscMpanlDlciUnknownStatus,
       "mscMpanlDlciCalldTable": mscMpanlDlciCalldTable,
       "mscMpanlDlciCalldEntry": mscMpanlDlciCalldEntry,
       "mscMpanlDlciQ933CallState": mscMpanlDlciQ933CallState,
       "mscMpanlDlciQ933CallReference": mscMpanlDlciQ933CallReference,
       "mscMpanlDlciSpOpTable": mscMpanlDlciSpOpTable,
       "mscMpanlDlciSpOpEntry": mscMpanlDlciSpOpEntry,
       "mscMpanlDlciMaximumFrameSize": mscMpanlDlciMaximumFrameSize,
       "mscMpanlDlciCommittedBurstSize": mscMpanlDlciCommittedBurstSize,
       "mscMpanlDlciExcessBurstSize": mscMpanlDlciExcessBurstSize,
       "mscMpanlDlciAccounting": mscMpanlDlciAccounting,
       "mscMpanlDlciEmissionPriorityToIf": mscMpanlDlciEmissionPriorityToIf,
       "mscMpanlDlciTransferPriToNwk": mscMpanlDlciTransferPriToNwk,
       "mscMpanlDlciTransferPriFromNwk": mscMpanlDlciTransferPriFromNwk,
       "mscMpanlDlciStatsTable": mscMpanlDlciStatsTable,
       "mscMpanlDlciStatsEntry": mscMpanlDlciStatsEntry,
       "mscMpanlDlciFrmToIf": mscMpanlDlciFrmToIf,
       "mscMpanlDlciFecnFrmToIf": mscMpanlDlciFecnFrmToIf,
       "mscMpanlDlciBecnFrmToIf": mscMpanlDlciBecnFrmToIf,
       "mscMpanlDlciBciToSubnet": mscMpanlDlciBciToSubnet,
       "mscMpanlDlciDeFrmToIf": mscMpanlDlciDeFrmToIf,
       "mscMpanlDlciDiscCongestedToIf": mscMpanlDlciDiscCongestedToIf,
       "mscMpanlDlciDiscDeCongestedToIf": mscMpanlDlciDiscDeCongestedToIf,
       "mscMpanlDlciFrmFromIf": mscMpanlDlciFrmFromIf,
       "mscMpanlDlciFecnFrmFromIf": mscMpanlDlciFecnFrmFromIf,
       "mscMpanlDlciBecnFrmFromIf": mscMpanlDlciBecnFrmFromIf,
       "mscMpanlDlciFciFromSubnet": mscMpanlDlciFciFromSubnet,
       "mscMpanlDlciBciFromSubnet": mscMpanlDlciBciFromSubnet,
       "mscMpanlDlciDeFrmFromIf": mscMpanlDlciDeFrmFromIf,
       "mscMpanlDlciExcessFrmFromIf": mscMpanlDlciExcessFrmFromIf,
       "mscMpanlDlciDiscExcessFromIf": mscMpanlDlciDiscExcessFromIf,
       "mscMpanlDlciDiscFrameAbit": mscMpanlDlciDiscFrameAbit,
       "mscMpanlDlciDiscCongestedFromIf": mscMpanlDlciDiscCongestedFromIf,
       "mscMpanlDlciDiscDeCongestedFromIf": mscMpanlDlciDiscDeCongestedFromIf,
       "mscMpanlDlciErrorShortFrmFromIf": mscMpanlDlciErrorShortFrmFromIf,
       "mscMpanlDlciErrorLongFrmFromIf": mscMpanlDlciErrorLongFrmFromIf,
       "mscMpanlDlciBecnFrmSetByService": mscMpanlDlciBecnFrmSetByService,
       "mscMpanlDlciBytesToIf": mscMpanlDlciBytesToIf,
       "mscMpanlDlciDeBytesToIf": mscMpanlDlciDeBytesToIf,
       "mscMpanlDlciDiscCongestedToIfBytes": mscMpanlDlciDiscCongestedToIfBytes,
       "mscMpanlDlciDiscDeCongestedToIfBytes": mscMpanlDlciDiscDeCongestedToIfBytes,
       "mscMpanlDlciBytesFromIf": mscMpanlDlciBytesFromIf,
       "mscMpanlDlciDeBytesFromIf": mscMpanlDlciDeBytesFromIf,
       "mscMpanlDlciExcessBytesFromIf": mscMpanlDlciExcessBytesFromIf,
       "mscMpanlDlciDiscExcessFromIfBytes": mscMpanlDlciDiscExcessFromIfBytes,
       "mscMpanlDlciDiscByteAbit": mscMpanlDlciDiscByteAbit,
       "mscMpanlDlciDiscCongestedFromIfBytes": mscMpanlDlciDiscCongestedFromIfBytes,
       "mscMpanlDlciDiscDeCongestedFromIfBytes": mscMpanlDlciDiscDeCongestedFromIfBytes,
       "mscMpanlDlciErrorLongBytesFromIf": mscMpanlDlciErrorLongBytesFromIf,
       "mscMpanlDlciTransferPriorityToNetwork": mscMpanlDlciTransferPriorityToNetwork,
       "mscMpanlDlciTransferPriorityFromNetwork": mscMpanlDlciTransferPriorityFromNetwork,
       "mscMpanlDlciIntTable": mscMpanlDlciIntTable,
       "mscMpanlDlciIntEntry": mscMpanlDlciIntEntry,
       "mscMpanlDlciStartTime": mscMpanlDlciStartTime,
       "mscMpanlDlciTotalIngressBytes": mscMpanlDlciTotalIngressBytes,
       "mscMpanlDlciTotalEgressBytes": mscMpanlDlciTotalEgressBytes,
       "mscMpanlDlciEirIngressBytes": mscMpanlDlciEirIngressBytes,
       "mscMpanlDlciEirEgressBytes": mscMpanlDlciEirEgressBytes,
       "mscMpanlDlciDiscardedBytes": mscMpanlDlciDiscardedBytes,
       "mscMpanlDlciTotalIngressSegFrm": mscMpanlDlciTotalIngressSegFrm,
       "mscMpanlDlciTotalEgressSegFrm": mscMpanlDlciTotalEgressSegFrm,
       "mscMpanlDlciEirIngressSegFrm": mscMpanlDlciEirIngressSegFrm,
       "mscMpanlDlciEirEgressSegFrm": mscMpanlDlciEirEgressSegFrm,
       "mscMpanlDlciDiscardedSegFrm": mscMpanlDlciDiscardedSegFrm,
       "mscMpanlDlciCallReferenceNumber": mscMpanlDlciCallReferenceNumber,
       "mscMpanlDlciElapsedDifference": mscMpanlDlciElapsedDifference,
       "mscMpanlDlciAbitTable": mscMpanlDlciAbitTable,
       "mscMpanlDlciAbitEntry": mscMpanlDlciAbitEntry,
       "mscMpanlDlciABitStatusToIf": mscMpanlDlciABitStatusToIf,
       "mscMpanlDlciABitReasonToIf": mscMpanlDlciABitReasonToIf,
       "mscMpanlDlciABitStatusFromIf": mscMpanlDlciABitStatusFromIf,
       "mscMpanlDlciABitReasonFromIf": mscMpanlDlciABitReasonFromIf,
       "mscMpanlDlciLoopbackState": mscMpanlDlciLoopbackState,
       "mscMpanlSig": mscMpanlSig,
       "mscMpanlSigRowStatusTable": mscMpanlSigRowStatusTable,
       "mscMpanlSigRowStatusEntry": mscMpanlSigRowStatusEntry,
       "mscMpanlSigRowStatus": mscMpanlSigRowStatus,
       "mscMpanlSigComponentName": mscMpanlSigComponentName,
       "mscMpanlSigStorageType": mscMpanlSigStorageType,
       "mscMpanlSigIndex": mscMpanlSigIndex,
       "mscMpanlSigSysParmsTable": mscMpanlSigSysParmsTable,
       "mscMpanlSigSysParmsEntry": mscMpanlSigSysParmsEntry,
       "mscMpanlSigCallSetupTimer": mscMpanlSigCallSetupTimer,
       "mscMpanlSigDisconnectTimer": mscMpanlSigDisconnectTimer,
       "mscMpanlSigReleaseTimer": mscMpanlSigReleaseTimer,
       "mscMpanlSigCallProceedingTimer": mscMpanlSigCallProceedingTimer,
       "mscMpanlSigNetworkType": mscMpanlSigNetworkType,
       "mscMpanlSigLapfSysTable": mscMpanlSigLapfSysTable,
       "mscMpanlSigLapfSysEntry": mscMpanlSigLapfSysEntry,
       "mscMpanlSigWindowSize": mscMpanlSigWindowSize,
       "mscMpanlSigRetransmitLimit": mscMpanlSigRetransmitLimit,
       "mscMpanlSigAckTimer": mscMpanlSigAckTimer,
       "mscMpanlSigAckDelayTimer": mscMpanlSigAckDelayTimer,
       "mscMpanlSigIdleProbeTimer": mscMpanlSigIdleProbeTimer,
       "mscMpanlSigSvcaccTable": mscMpanlSigSvcaccTable,
       "mscMpanlSigSvcaccEntry": mscMpanlSigSvcaccEntry,
       "mscMpanlSigDefaultAccounting": mscMpanlSigDefaultAccounting,
       "mscMpanlSigStateTable": mscMpanlSigStateTable,
       "mscMpanlSigStateEntry": mscMpanlSigStateEntry,
       "mscMpanlSigAdminState": mscMpanlSigAdminState,
       "mscMpanlSigOperationalState": mscMpanlSigOperationalState,
       "mscMpanlSigUsageState": mscMpanlSigUsageState,
       "mscMpanlSigStatsTable": mscMpanlSigStatsTable,
       "mscMpanlSigStatsEntry": mscMpanlSigStatsEntry,
       "mscMpanlSigCurrentNumberOfSvcCalls": mscMpanlSigCurrentNumberOfSvcCalls,
       "mscMpanlSigInCalls": mscMpanlSigInCalls,
       "mscMpanlSigInCallsRefused": mscMpanlSigInCallsRefused,
       "mscMpanlSigOutCalls": mscMpanlSigOutCalls,
       "mscMpanlSigOutCallsFailed": mscMpanlSigOutCallsFailed,
       "mscMpanlSigProtocolErrors": mscMpanlSigProtocolErrors,
       "mscMpanlSigQualityOfServiceNotAvailable": mscMpanlSigQualityOfServiceNotAvailable,
       "mscMpanlSigSetupTimeout": mscMpanlSigSetupTimeout,
       "mscMpanlSigLastCauseInStatusMsgReceived": mscMpanlSigLastCauseInStatusMsgReceived,
       "mscMpanlSigLastStateInStatusMsgReceived": mscMpanlSigLastStateInStatusMsgReceived,
       "mscMpanlSigLastDlciReceivedStatus": mscMpanlSigLastDlciReceivedStatus,
       "mscMpanlSigLastQ933StateReceivedStatus": mscMpanlSigLastQ933StateReceivedStatus,
       "mscMpanlSigLastTimeMsgBlockCongested": mscMpanlSigLastTimeMsgBlockCongested,
       "mscMpanlSigLastDlciWithMsgBlockCongestion": mscMpanlSigLastDlciWithMsgBlockCongestion,
       "mscMpanlSigLapfStatusTable": mscMpanlSigLapfStatusTable,
       "mscMpanlSigLapfStatusEntry": mscMpanlSigLapfStatusEntry,
       "mscMpanlSigCurrentState": mscMpanlSigCurrentState,
       "mscMpanlSigLastStateChangeReason": mscMpanlSigLastStateChangeReason,
       "mscMpanlSigFrmrReceive": mscMpanlSigFrmrReceive,
       "mscMpanlSigCurrentQueueSize": mscMpanlSigCurrentQueueSize,
       "mscMpanlSigLapfStatsTable": mscMpanlSigLapfStatsTable,
       "mscMpanlSigLapfStatsEntry": mscMpanlSigLapfStatsEntry,
       "mscMpanlSigStateChange": mscMpanlSigStateChange,
       "mscMpanlSigRemoteBusy": mscMpanlSigRemoteBusy,
       "mscMpanlSigReceiveRejectFrame": mscMpanlSigReceiveRejectFrame,
       "mscMpanlSigAckTimeout": mscMpanlSigAckTimeout,
       "mscMpanlSigIFramesTransmitted": mscMpanlSigIFramesTransmitted,
       "mscMpanlSigIFramesTxDiscarded": mscMpanlSigIFramesTxDiscarded,
       "mscMpanlSigIFramesReceived": mscMpanlSigIFramesReceived,
       "mscMpanlSigIFramesRcvdDiscarded": mscMpanlSigIFramesRcvdDiscarded,
       "mscMpanlSigMpanl": mscMpanlSigMpanl,
       "mscMpanlSigMpanlRowStatusTable": mscMpanlSigMpanlRowStatusTable,
       "mscMpanlSigMpanlRowStatusEntry": mscMpanlSigMpanlRowStatusEntry,
       "mscMpanlSigMpanlRowStatus": mscMpanlSigMpanlRowStatus,
       "mscMpanlSigMpanlComponentName": mscMpanlSigMpanlComponentName,
       "mscMpanlSigMpanlStorageType": mscMpanlSigMpanlStorageType,
       "mscMpanlSigMpanlIndex": mscMpanlSigMpanlIndex,
       "mscMpanlSigMpanlStateTable": mscMpanlSigMpanlStateTable,
       "mscMpanlSigMpanlStateEntry": mscMpanlSigMpanlStateEntry,
       "mscMpanlSigMpanlAdminState": mscMpanlSigMpanlAdminState,
       "mscMpanlSigMpanlOperationalState": mscMpanlSigMpanlOperationalState,
       "mscMpanlSigMpanlUsageState": mscMpanlSigMpanlUsageState,
       "mscMpanlSigMpanlProfileTable": mscMpanlSigMpanlProfileTable,
       "mscMpanlSigMpanlProfileEntry": mscMpanlSigMpanlProfileEntry,
       "mscMpanlSigMpanlDteCustomerId": mscMpanlSigMpanlDteCustomerId,
       "mscMpanlSigMpanlDteNodeId": mscMpanlSigMpanlDteNodeId,
       "mscMpanlSigMpanlDteComponentName": mscMpanlSigMpanlDteComponentName,
       "mscMpanlSigMpanlHighestDlci": mscMpanlSigMpanlHighestDlci,
       "mscMpanlSigMpanlStatsTable": mscMpanlSigMpanlStatsTable,
       "mscMpanlSigMpanlStatsEntry": mscMpanlSigMpanlStatsEntry,
       "mscMpanlSigMpanlProtocolErrors": mscMpanlSigMpanlProtocolErrors,
       "mscMpanlSigMpanlSap0CommandsRx": mscMpanlSigMpanlSap0CommandsRx,
       "mscMpanlSigMpanlSap0CommandsTx": mscMpanlSigMpanlSap0CommandsTx,
       "mscMpanlSigMpanlSapXCommandsRx": mscMpanlSigMpanlSapXCommandsRx,
       "mscMpanlSigMpanlSapXCommandsTx": mscMpanlSigMpanlSapXCommandsTx,
       "mscMpanlSigMpanlLapfStatusTable": mscMpanlSigMpanlLapfStatusTable,
       "mscMpanlSigMpanlLapfStatusEntry": mscMpanlSigMpanlLapfStatusEntry,
       "mscMpanlSigMpanlCurrentState": mscMpanlSigMpanlCurrentState,
       "mscMpanlSigMpanlLastStateChangeReason": mscMpanlSigMpanlLastStateChangeReason,
       "mscMpanlSigMpanlFrmrReceive": mscMpanlSigMpanlFrmrReceive,
       "mscMpanlSigMpanlCurrentQueueSize": mscMpanlSigMpanlCurrentQueueSize,
       "mscMpanlSigMpanlLapfStatsTable": mscMpanlSigMpanlLapfStatsTable,
       "mscMpanlSigMpanlLapfStatsEntry": mscMpanlSigMpanlLapfStatsEntry,
       "mscMpanlSigMpanlStateChange": mscMpanlSigMpanlStateChange,
       "mscMpanlSigMpanlRemoteBusy": mscMpanlSigMpanlRemoteBusy,
       "mscMpanlSigMpanlReceiveRejectFrame": mscMpanlSigMpanlReceiveRejectFrame,
       "mscMpanlSigMpanlAckTimeout": mscMpanlSigMpanlAckTimeout,
       "mscMpanlSigMpanlIFramesTransmitted": mscMpanlSigMpanlIFramesTransmitted,
       "mscMpanlSigMpanlIFramesTxDiscarded": mscMpanlSigMpanlIFramesTxDiscarded,
       "mscMpanlSigMpanlIFramesReceived": mscMpanlSigMpanlIFramesReceived,
       "mscMpanlSigMpanlIFramesRcvdDiscarded": mscMpanlSigMpanlIFramesRcvdDiscarded,
       "mscMpanlLmi": mscMpanlLmi,
       "mscMpanlLmiRowStatusTable": mscMpanlLmiRowStatusTable,
       "mscMpanlLmiRowStatusEntry": mscMpanlLmiRowStatusEntry,
       "mscMpanlLmiRowStatus": mscMpanlLmiRowStatus,
       "mscMpanlLmiComponentName": mscMpanlLmiComponentName,
       "mscMpanlLmiStorageType": mscMpanlLmiStorageType,
       "mscMpanlLmiIndex": mscMpanlLmiIndex,
       "mscMpanlLmiParmsTable": mscMpanlLmiParmsTable,
       "mscMpanlLmiParmsEntry": mscMpanlLmiParmsEntry,
       "mscMpanlLmiProcedures": mscMpanlLmiProcedures,
       "mscMpanlLmiStateTable": mscMpanlLmiStateTable,
       "mscMpanlLmiStateEntry": mscMpanlLmiStateEntry,
       "mscMpanlLmiAdminState": mscMpanlLmiAdminState,
       "mscMpanlLmiOperationalState": mscMpanlLmiOperationalState,
       "mscMpanlLmiUsageState": mscMpanlLmiUsageState,
       "mscMpanlCidDataTable": mscMpanlCidDataTable,
       "mscMpanlCidDataEntry": mscMpanlCidDataEntry,
       "mscMpanlCustomerIdentifier": mscMpanlCustomerIdentifier,
       "mscMpanlProvTable": mscMpanlProvTable,
       "mscMpanlProvEntry": mscMpanlProvEntry,
       "mscMpanlCommentText": mscMpanlCommentText,
       "mscMpanlEmissionPriorityQsTable": mscMpanlEmissionPriorityQsTable,
       "mscMpanlEmissionPriorityQsEntry": mscMpanlEmissionPriorityQsEntry,
       "mscMpanlNumberOfEmissionQs": mscMpanlNumberOfEmissionQs,
       "mscMpanlStateTable": mscMpanlStateTable,
       "mscMpanlStateEntry": mscMpanlStateEntry,
       "mscMpanlAdminState": mscMpanlAdminState,
       "mscMpanlOperationalState": mscMpanlOperationalState,
       "mscMpanlUsageState": mscMpanlUsageState,
       "mscMpanlAvailabilityStatus": mscMpanlAvailabilityStatus,
       "mscMpanlProceduralStatus": mscMpanlProceduralStatus,
       "mscMpanlControlStatus": mscMpanlControlStatus,
       "mscMpanlAlarmStatus": mscMpanlAlarmStatus,
       "mscMpanlStandbyStatus": mscMpanlStandbyStatus,
       "mscMpanlUnknownStatus": mscMpanlUnknownStatus,
       "mscMpanlStatsTable": mscMpanlStatsTable,
       "mscMpanlStatsEntry": mscMpanlStatsEntry,
       "mscMpanlLastUnknownDlci": mscMpanlLastUnknownDlci,
       "mscMpanlUnknownDlciFramesFromIf": mscMpanlUnknownDlciFramesFromIf,
       "mscMpanlInvalidHeaderFramesFromIf": mscMpanlInvalidHeaderFramesFromIf,
       "mscMpanlTrafficStatsTable": mscMpanlTrafficStatsTable,
       "mscMpanlTrafficStatsEntry": mscMpanlTrafficStatsEntry,
       "mscMpanlFrmToIf": mscMpanlFrmToIf,
       "mscMpanlOctetToIf": mscMpanlOctetToIf,
       "mscMpanlFrmFromIf": mscMpanlFrmFromIf,
       "mscMpanlOctetFromIf": mscMpanlOctetFromIf,
       "mscMpanlVoFr": mscMpanlVoFr,
       "mscMpanlVoFrRowStatusTable": mscMpanlVoFrRowStatusTable,
       "mscMpanlVoFrRowStatusEntry": mscMpanlVoFrRowStatusEntry,
       "mscMpanlVoFrRowStatus": mscMpanlVoFrRowStatus,
       "mscMpanlVoFrComponentName": mscMpanlVoFrComponentName,
       "mscMpanlVoFrStorageType": mscMpanlVoFrStorageType,
       "mscMpanlVoFrIndex": mscMpanlVoFrIndex,
       "mscMpanlVoFrOperTable": mscMpanlVoFrOperTable,
       "mscMpanlVoFrOperEntry": mscMpanlVoFrOperEntry,
       "mscMpanlVoFrMaximumFrameSize": mscMpanlVoFrMaximumFrameSize,
       "mscMpanlVoFrTransmitInformationRate": mscMpanlVoFrTransmitInformationRate,
       "mscMpanlVoFrStatsTable": mscMpanlVoFrStatsTable,
       "mscMpanlVoFrStatsEntry": mscMpanlVoFrStatsEntry,
       "mscMpanlVoFrFragmentedHighestPriorityFrames": mscMpanlVoFrFragmentedHighestPriorityFrames,
       "mscMpanlVoFrLostFragmentsFromIf": mscMpanlVoFrLostFragmentsFromIf,
       "mscMpanlVoFrProtocolViolationsFromIf": mscMpanlVoFrProtocolViolationsFromIf,
       "mscMpanlFrMuxSetup": mscMpanlFrMuxSetup,
       "mscMpanlFrMuxSetupRowStatusTable": mscMpanlFrMuxSetupRowStatusTable,
       "mscMpanlFrMuxSetupRowStatusEntry": mscMpanlFrMuxSetupRowStatusEntry,
       "mscMpanlFrMuxSetupRowStatus": mscMpanlFrMuxSetupRowStatus,
       "mscMpanlFrMuxSetupComponentName": mscMpanlFrMuxSetupComponentName,
       "mscMpanlFrMuxSetupStorageType": mscMpanlFrMuxSetupStorageType,
       "mscMpanlFrMuxSetupIndex": mscMpanlFrMuxSetupIndex,
       "mscMpanlFrMuxSetupPvcSetup": mscMpanlFrMuxSetupPvcSetup,
       "mscMpanlFrMuxSetupPvcSetupRowStatusTable": mscMpanlFrMuxSetupPvcSetupRowStatusTable,
       "mscMpanlFrMuxSetupPvcSetupRowStatusEntry": mscMpanlFrMuxSetupPvcSetupRowStatusEntry,
       "mscMpanlFrMuxSetupPvcSetupRowStatus": mscMpanlFrMuxSetupPvcSetupRowStatus,
       "mscMpanlFrMuxSetupPvcSetupComponentName": mscMpanlFrMuxSetupPvcSetupComponentName,
       "mscMpanlFrMuxSetupPvcSetupStorageType": mscMpanlFrMuxSetupPvcSetupStorageType,
       "mscMpanlFrMuxSetupPvcSetupIndex": mscMpanlFrMuxSetupPvcSetupIndex,
       "mscMpanlFrMuxSetupPvcSetupProvTable": mscMpanlFrMuxSetupPvcSetupProvTable,
       "mscMpanlFrMuxSetupPvcSetupProvEntry": mscMpanlFrMuxSetupPvcSetupProvEntry,
       "mscMpanlFrMuxSetupPvcSetupDlciName": mscMpanlFrMuxSetupPvcSetupDlciName,
       "mscMpanlFrMuxSetupOpTable": mscMpanlFrMuxSetupOpTable,
       "mscMpanlFrMuxSetupOpEntry": mscMpanlFrMuxSetupOpEntry,
       "mscMpanlFrMuxSetupCommittedInformationRate": mscMpanlFrMuxSetupCommittedInformationRate,
       "mscMpanlFrMuxSetupDlciCompName": mscMpanlFrMuxSetupDlciCompName,
       "mscMpanlIsdn": mscMpanlIsdn,
       "mscMpanlIsdnRowStatusTable": mscMpanlIsdnRowStatusTable,
       "mscMpanlIsdnRowStatusEntry": mscMpanlIsdnRowStatusEntry,
       "mscMpanlIsdnRowStatus": mscMpanlIsdnRowStatus,
       "mscMpanlIsdnComponentName": mscMpanlIsdnComponentName,
       "mscMpanlIsdnStorageType": mscMpanlIsdnStorageType,
       "mscMpanlIsdnIndex": mscMpanlIsdnIndex,
       "mscMpanlIsdnProvTable": mscMpanlIsdnProvTable,
       "mscMpanlIsdnProvEntry": mscMpanlIsdnProvEntry,
       "mscMpanlIsdnT320": mscMpanlIsdnT320,
       "mscMpanlIsdnAddressSignalling": mscMpanlIsdnAddressSignalling,
       "mscMpanlIsdnOperTable": mscMpanlIsdnOperTable,
       "mscMpanlIsdnOperEntry": mscMpanlIsdnOperEntry,
       "mscMpanlIsdnDataSigChan": mscMpanlIsdnDataSigChan,
       "mscMpanlIsdnBChannelState": mscMpanlIsdnBChannelState,
       "mscMpanlIsdnLastUsedCgpn": mscMpanlIsdnLastUsedCgpn,
       "mscMpanlIsdnBChanIntState": mscMpanlIsdnBChanIntState,
       "mscMpanlIsdnActiveVirtualCircuitsCount": mscMpanlIsdnActiveVirtualCircuitsCount,
       "mscMpanlIfEntryTable": mscMpanlIfEntryTable,
       "mscMpanlIfEntryEntry": mscMpanlIfEntryEntry,
       "mscMpanlIfAdminStatus": mscMpanlIfAdminStatus,
       "mscMpanlIfIndex": mscMpanlIfIndex,
       "mscMpanlOperStatusTable": mscMpanlOperStatusTable,
       "mscMpanlOperStatusEntry": mscMpanlOperStatusEntry,
       "mscMpanlSnmpOperStatus": mscMpanlSnmpOperStatus,
       "mscMpanlOperTable": mscMpanlOperTable,
       "mscMpanlOperEntry": mscMpanlOperEntry,
       "mscMpanlRoundTripDelay": mscMpanlRoundTripDelay,
       "mscMpanlFrmToIfByQueueTable": mscMpanlFrmToIfByQueueTable,
       "mscMpanlFrmToIfByQueueEntry": mscMpanlFrmToIfByQueueEntry,
       "mscMpanlFrmToIfByQueueIndex": mscMpanlFrmToIfByQueueIndex,
       "mscMpanlFrmToIfByQueueValue": mscMpanlFrmToIfByQueueValue,
       "mscMpanlOctetToIfByQueueTable": mscMpanlOctetToIfByQueueTable,
       "mscMpanlOctetToIfByQueueEntry": mscMpanlOctetToIfByQueueEntry,
       "mscMpanlOctetToIfByQueueIndex": mscMpanlOctetToIfByQueueIndex,
       "mscMpanlOctetToIfByQueueValue": mscMpanlOctetToIfByQueueValue,
       "mpaNetworkLinkMIB": mpaNetworkLinkMIB,
       "mpaNetworkLinkGroup": mpaNetworkLinkGroup,
       "mpaNetworkLinkGroupCA": mpaNetworkLinkGroupCA,
       "mpaNetworkLinkGroupCA02": mpaNetworkLinkGroupCA02,
       "mpaNetworkLinkGroupCA02A": mpaNetworkLinkGroupCA02A,
       "mpaNetworkLinkCapabilities": mpaNetworkLinkCapabilities,
       "mpaNetworkLinkCapabilitiesCA": mpaNetworkLinkCapabilitiesCA,
       "mpaNetworkLinkCapabilitiesCA02": mpaNetworkLinkCapabilitiesCA02,
       "mpaNetworkLinkCapabilitiesCA02A": mpaNetworkLinkCapabilitiesCA02A}
)
