# SNMP MIB module (Nortel-Magellan-Passport-MpaNetworkLinkMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-Magellan-Passport-MpaNetworkLinkMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:31:12 2024
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
 PassportCounter64,
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
    "PassportCounter64",
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
 Unsigned64) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-TextualConventionsMIB",
    "AsciiString",
    "DigitString",
    "EnterpriseDateAndTime",
    "Hex",
    "HexString",
    "Link",
    "NonReplicated",
    "Unsigned64")

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

_Mpanl_ObjectIdentity = ObjectIdentity
mpanl = _Mpanl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123)
)
_MpanlRowStatusTable_Object = MibTable
mpanlRowStatusTable = _MpanlRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 1)
)
if mibBuilder.loadTexts:
    mpanlRowStatusTable.setStatus("mandatory")
_MpanlRowStatusEntry_Object = MibTableRow
mpanlRowStatusEntry = _MpanlRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 1, 1)
)
mpanlRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-MpaNetworkLinkMIB", "mpanlIndex"),
)
if mibBuilder.loadTexts:
    mpanlRowStatusEntry.setStatus("mandatory")
_MpanlRowStatus_Type = RowStatus
_MpanlRowStatus_Object = MibTableColumn
mpanlRowStatus = _MpanlRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 1, 1, 1),
    _MpanlRowStatus_Type()
)
mpanlRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpanlRowStatus.setStatus("mandatory")
_MpanlComponentName_Type = DisplayString
_MpanlComponentName_Object = MibTableColumn
mpanlComponentName = _MpanlComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 1, 1, 2),
    _MpanlComponentName_Type()
)
mpanlComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlComponentName.setStatus("mandatory")
_MpanlStorageType_Type = StorageType
_MpanlStorageType_Object = MibTableColumn
mpanlStorageType = _MpanlStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 1, 1, 4),
    _MpanlStorageType_Type()
)
mpanlStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlStorageType.setStatus("mandatory")


class _MpanlIndex_Type(Integer32):
    """Custom type mpanlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MpanlIndex_Type.__name__ = "Integer32"
_MpanlIndex_Object = MibTableColumn
mpanlIndex = _MpanlIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 1, 1, 10),
    _MpanlIndex_Type()
)
mpanlIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mpanlIndex.setStatus("mandatory")
_MpanlDna_ObjectIdentity = ObjectIdentity
mpanlDna = _MpanlDna_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 2)
)
_MpanlDnaRowStatusTable_Object = MibTable
mpanlDnaRowStatusTable = _MpanlDnaRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 2, 1)
)
if mibBuilder.loadTexts:
    mpanlDnaRowStatusTable.setStatus("mandatory")
_MpanlDnaRowStatusEntry_Object = MibTableRow
mpanlDnaRowStatusEntry = _MpanlDnaRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 2, 1, 1)
)
mpanlDnaRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-MpaNetworkLinkMIB", "mpanlIndex"),
    (0, "Nortel-Magellan-Passport-MpaNetworkLinkMIB", "mpanlDnaIndex"),
)
if mibBuilder.loadTexts:
    mpanlDnaRowStatusEntry.setStatus("mandatory")
_MpanlDnaRowStatus_Type = RowStatus
_MpanlDnaRowStatus_Object = MibTableColumn
mpanlDnaRowStatus = _MpanlDnaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 2, 1, 1, 1),
    _MpanlDnaRowStatus_Type()
)
mpanlDnaRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDnaRowStatus.setStatus("mandatory")
_MpanlDnaComponentName_Type = DisplayString
_MpanlDnaComponentName_Object = MibTableColumn
mpanlDnaComponentName = _MpanlDnaComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 2, 1, 1, 2),
    _MpanlDnaComponentName_Type()
)
mpanlDnaComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDnaComponentName.setStatus("mandatory")
_MpanlDnaStorageType_Type = StorageType
_MpanlDnaStorageType_Object = MibTableColumn
mpanlDnaStorageType = _MpanlDnaStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 2, 1, 1, 4),
    _MpanlDnaStorageType_Type()
)
mpanlDnaStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDnaStorageType.setStatus("mandatory")
_MpanlDnaIndex_Type = NonReplicated
_MpanlDnaIndex_Object = MibTableColumn
mpanlDnaIndex = _MpanlDnaIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 2, 1, 1, 10),
    _MpanlDnaIndex_Type()
)
mpanlDnaIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mpanlDnaIndex.setStatus("mandatory")
_MpanlDnaOutgoingOptionsTable_Object = MibTable
mpanlDnaOutgoingOptionsTable = _MpanlDnaOutgoingOptionsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 2, 11)
)
if mibBuilder.loadTexts:
    mpanlDnaOutgoingOptionsTable.setStatus("mandatory")
_MpanlDnaOutgoingOptionsEntry_Object = MibTableRow
mpanlDnaOutgoingOptionsEntry = _MpanlDnaOutgoingOptionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 2, 11, 1)
)
mpanlDnaOutgoingOptionsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-MpaNetworkLinkMIB", "mpanlIndex"),
    (0, "Nortel-Magellan-Passport-MpaNetworkLinkMIB", "mpanlDnaIndex"),
)
if mibBuilder.loadTexts:
    mpanlDnaOutgoingOptionsEntry.setStatus("mandatory")


class _MpanlDnaDefaultTransferPriority_Type(Integer32):
    """Custom type mpanlDnaDefaultTransferPriority based on Integer32"""
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


_MpanlDnaDefaultTransferPriority_Type.__name__ = "Integer32"
_MpanlDnaDefaultTransferPriority_Object = MibTableColumn
mpanlDnaDefaultTransferPriority = _MpanlDnaDefaultTransferPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 2, 11, 1, 18),
    _MpanlDnaDefaultTransferPriority_Type()
)
mpanlDnaDefaultTransferPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpanlDnaDefaultTransferPriority.setStatus("mandatory")
_MpanlDnaCallOptionsTable_Object = MibTable
mpanlDnaCallOptionsTable = _MpanlDnaCallOptionsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 2, 13)
)
if mibBuilder.loadTexts:
    mpanlDnaCallOptionsTable.setStatus("mandatory")
_MpanlDnaCallOptionsEntry_Object = MibTableRow
mpanlDnaCallOptionsEntry = _MpanlDnaCallOptionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 2, 13, 1)
)
mpanlDnaCallOptionsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-MpaNetworkLinkMIB", "mpanlIndex"),
    (0, "Nortel-Magellan-Passport-MpaNetworkLinkMIB", "mpanlDnaIndex"),
)
if mibBuilder.loadTexts:
    mpanlDnaCallOptionsEntry.setStatus("mandatory")


class _MpanlDnaAccountClass_Type(Unsigned32):
    """Custom type mpanlDnaAccountClass based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MpanlDnaAccountClass_Type.__name__ = "Unsigned32"
_MpanlDnaAccountClass_Object = MibTableColumn
mpanlDnaAccountClass = _MpanlDnaAccountClass_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 2, 13, 1, 10),
    _MpanlDnaAccountClass_Type()
)
mpanlDnaAccountClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpanlDnaAccountClass.setStatus("mandatory")


class _MpanlDnaAccountCollection_Type(OctetString):
    """Custom type mpanlDnaAccountCollection based on OctetString"""
    defaultHexValue = "80"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MpanlDnaAccountCollection_Type.__name__ = "OctetString"
_MpanlDnaAccountCollection_Object = MibTableColumn
mpanlDnaAccountCollection = _MpanlDnaAccountCollection_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 2, 13, 1, 11),
    _MpanlDnaAccountCollection_Type()
)
mpanlDnaAccountCollection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpanlDnaAccountCollection.setStatus("mandatory")


class _MpanlDnaServiceExchange_Type(Unsigned32):
    """Custom type mpanlDnaServiceExchange based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MpanlDnaServiceExchange_Type.__name__ = "Unsigned32"
_MpanlDnaServiceExchange_Object = MibTableColumn
mpanlDnaServiceExchange = _MpanlDnaServiceExchange_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 2, 13, 1, 12),
    _MpanlDnaServiceExchange_Type()
)
mpanlDnaServiceExchange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpanlDnaServiceExchange.setStatus("mandatory")


class _MpanlDnaEgressAccounting_Type(Integer32):
    """Custom type mpanlDnaEgressAccounting based on Integer32"""
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


_MpanlDnaEgressAccounting_Type.__name__ = "Integer32"
_MpanlDnaEgressAccounting_Object = MibTableColumn
mpanlDnaEgressAccounting = _MpanlDnaEgressAccounting_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 2, 13, 1, 13),
    _MpanlDnaEgressAccounting_Type()
)
mpanlDnaEgressAccounting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpanlDnaEgressAccounting.setStatus("mandatory")
_MpanlFramer_ObjectIdentity = ObjectIdentity
mpanlFramer = _MpanlFramer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 3)
)
_MpanlFramerRowStatusTable_Object = MibTable
mpanlFramerRowStatusTable = _MpanlFramerRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 3, 1)
)
if mibBuilder.loadTexts:
    mpanlFramerRowStatusTable.setStatus("mandatory")
_MpanlFramerRowStatusEntry_Object = MibTableRow
mpanlFramerRowStatusEntry = _MpanlFramerRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 3, 1, 1)
)
mpanlFramerRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-MpaNetworkLinkMIB", "mpanlIndex"),
    (0, "Nortel-Magellan-Passport-MpaNetworkLinkMIB", "mpanlFramerIndex"),
)
if mibBuilder.loadTexts:
    mpanlFramerRowStatusEntry.setStatus("mandatory")
_MpanlFramerRowStatus_Type = RowStatus
_MpanlFramerRowStatus_Object = MibTableColumn
mpanlFramerRowStatus = _MpanlFramerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 3, 1, 1, 1),
    _MpanlFramerRowStatus_Type()
)
mpanlFramerRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpanlFramerRowStatus.setStatus("mandatory")
_MpanlFramerComponentName_Type = DisplayString
_MpanlFramerComponentName_Object = MibTableColumn
mpanlFramerComponentName = _MpanlFramerComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 3, 1, 1, 2),
    _MpanlFramerComponentName_Type()
)
mpanlFramerComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlFramerComponentName.setStatus("mandatory")
_MpanlFramerStorageType_Type = StorageType
_MpanlFramerStorageType_Object = MibTableColumn
mpanlFramerStorageType = _MpanlFramerStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 3, 1, 1, 4),
    _MpanlFramerStorageType_Type()
)
mpanlFramerStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlFramerStorageType.setStatus("mandatory")
_MpanlFramerIndex_Type = NonReplicated
_MpanlFramerIndex_Object = MibTableColumn
mpanlFramerIndex = _MpanlFramerIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 3, 1, 1, 10),
    _MpanlFramerIndex_Type()
)
mpanlFramerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mpanlFramerIndex.setStatus("mandatory")
_MpanlFramerProvTable_Object = MibTable
mpanlFramerProvTable = _MpanlFramerProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 3, 10)
)
if mibBuilder.loadTexts:
    mpanlFramerProvTable.setStatus("mandatory")
_MpanlFramerProvEntry_Object = MibTableRow
mpanlFramerProvEntry = _MpanlFramerProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 3, 10, 1)
)
mpanlFramerProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-MpaNetworkLinkMIB", "mpanlIndex"),
    (0, "Nortel-Magellan-Passport-MpaNetworkLinkMIB", "mpanlFramerIndex"),
)
if mibBuilder.loadTexts:
    mpanlFramerProvEntry.setStatus("mandatory")
_MpanlFramerInterfaceName_Type = Link
_MpanlFramerInterfaceName_Object = MibTableColumn
mpanlFramerInterfaceName = _MpanlFramerInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 3, 10, 1, 1),
    _MpanlFramerInterfaceName_Type()
)
mpanlFramerInterfaceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpanlFramerInterfaceName.setStatus("mandatory")
_MpanlFramerLinkTable_Object = MibTable
mpanlFramerLinkTable = _MpanlFramerLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 3, 11)
)
if mibBuilder.loadTexts:
    mpanlFramerLinkTable.setStatus("mandatory")
_MpanlFramerLinkEntry_Object = MibTableRow
mpanlFramerLinkEntry = _MpanlFramerLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 3, 11, 1)
)
mpanlFramerLinkEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-MpaNetworkLinkMIB", "mpanlIndex"),
    (0, "Nortel-Magellan-Passport-MpaNetworkLinkMIB", "mpanlFramerIndex"),
)
if mibBuilder.loadTexts:
    mpanlFramerLinkEntry.setStatus("mandatory")


class _MpanlFramerFlagsBetweenFrames_Type(Unsigned32):
    """Custom type mpanlFramerFlagsBetweenFrames based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_MpanlFramerFlagsBetweenFrames_Type.__name__ = "Unsigned32"
_MpanlFramerFlagsBetweenFrames_Object = MibTableColumn
mpanlFramerFlagsBetweenFrames = _MpanlFramerFlagsBetweenFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 3, 11, 1, 4),
    _MpanlFramerFlagsBetweenFrames_Type()
)
mpanlFramerFlagsBetweenFrames.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpanlFramerFlagsBetweenFrames.setStatus("mandatory")
_MpanlFramerStateTable_Object = MibTable
mpanlFramerStateTable = _MpanlFramerStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 3, 12)
)
if mibBuilder.loadTexts:
    mpanlFramerStateTable.setStatus("mandatory")
_MpanlFramerStateEntry_Object = MibTableRow
mpanlFramerStateEntry = _MpanlFramerStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 3, 12, 1)
)
mpanlFramerStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-MpaNetworkLinkMIB", "mpanlIndex"),
    (0, "Nortel-Magellan-Passport-MpaNetworkLinkMIB", "mpanlFramerIndex"),
)
if mibBuilder.loadTexts:
    mpanlFramerStateEntry.setStatus("mandatory")


class _MpanlFramerAdminState_Type(Integer32):
    """Custom type mpanlFramerAdminState based on Integer32"""
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


_MpanlFramerAdminState_Type.__name__ = "Integer32"
_MpanlFramerAdminState_Object = MibTableColumn
mpanlFramerAdminState = _MpanlFramerAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 3, 12, 1, 1),
    _MpanlFramerAdminState_Type()
)
mpanlFramerAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlFramerAdminState.setStatus("mandatory")


class _MpanlFramerOperationalState_Type(Integer32):
    """Custom type mpanlFramerOperationalState based on Integer32"""
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


_MpanlFramerOperationalState_Type.__name__ = "Integer32"
_MpanlFramerOperationalState_Object = MibTableColumn
mpanlFramerOperationalState = _MpanlFramerOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 3, 12, 1, 2),
    _MpanlFramerOperationalState_Type()
)
mpanlFramerOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlFramerOperationalState.setStatus("mandatory")


class _MpanlFramerUsageState_Type(Integer32):
    """Custom type mpanlFramerUsageState based on Integer32"""
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


_MpanlFramerUsageState_Type.__name__ = "Integer32"
_MpanlFramerUsageState_Object = MibTableColumn
mpanlFramerUsageState = _MpanlFramerUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 3, 12, 1, 3),
    _MpanlFramerUsageState_Type()
)
mpanlFramerUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlFramerUsageState.setStatus("mandatory")
_MpanlFramerStatsTable_Object = MibTable
mpanlFramerStatsTable = _MpanlFramerStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 3, 13)
)
if mibBuilder.loadTexts:
    mpanlFramerStatsTable.setStatus("mandatory")
_MpanlFramerStatsEntry_Object = MibTableRow
mpanlFramerStatsEntry = _MpanlFramerStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 3, 13, 1)
)
mpanlFramerStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-MpaNetworkLinkMIB", "mpanlIndex"),
    (0, "Nortel-Magellan-Passport-MpaNetworkLinkMIB", "mpanlFramerIndex"),
)
if mibBuilder.loadTexts:
    mpanlFramerStatsEntry.setStatus("mandatory")
_MpanlFramerFrmToIf_Type = Counter32
_MpanlFramerFrmToIf_Object = MibTableColumn
mpanlFramerFrmToIf = _MpanlFramerFrmToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 3, 13, 1, 1),
    _MpanlFramerFrmToIf_Type()
)
mpanlFramerFrmToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlFramerFrmToIf.setStatus("mandatory")
_MpanlFramerFrmFromIf_Type = Counter32
_MpanlFramerFrmFromIf_Object = MibTableColumn
mpanlFramerFrmFromIf = _MpanlFramerFrmFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 3, 13, 1, 2),
    _MpanlFramerFrmFromIf_Type()
)
mpanlFramerFrmFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlFramerFrmFromIf.setStatus("mandatory")
_MpanlFramerOctetFromIf_Type = Counter32
_MpanlFramerOctetFromIf_Object = MibTableColumn
mpanlFramerOctetFromIf = _MpanlFramerOctetFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 3, 13, 1, 3),
    _MpanlFramerOctetFromIf_Type()
)
mpanlFramerOctetFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlFramerOctetFromIf.setStatus("mandatory")
_MpanlFramerAborts_Type = Counter32
_MpanlFramerAborts_Object = MibTableColumn
mpanlFramerAborts = _MpanlFramerAborts_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 3, 13, 1, 4),
    _MpanlFramerAborts_Type()
)
mpanlFramerAborts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlFramerAborts.setStatus("mandatory")
_MpanlFramerCrcErrors_Type = Counter32
_MpanlFramerCrcErrors_Object = MibTableColumn
mpanlFramerCrcErrors = _MpanlFramerCrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 3, 13, 1, 5),
    _MpanlFramerCrcErrors_Type()
)
mpanlFramerCrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlFramerCrcErrors.setStatus("mandatory")
_MpanlFramerLrcErrors_Type = Counter32
_MpanlFramerLrcErrors_Object = MibTableColumn
mpanlFramerLrcErrors = _MpanlFramerLrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 3, 13, 1, 6),
    _MpanlFramerLrcErrors_Type()
)
mpanlFramerLrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlFramerLrcErrors.setStatus("mandatory")
_MpanlFramerNonOctetErrors_Type = Counter32
_MpanlFramerNonOctetErrors_Object = MibTableColumn
mpanlFramerNonOctetErrors = _MpanlFramerNonOctetErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 3, 13, 1, 7),
    _MpanlFramerNonOctetErrors_Type()
)
mpanlFramerNonOctetErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlFramerNonOctetErrors.setStatus("mandatory")
_MpanlFramerOverruns_Type = Counter32
_MpanlFramerOverruns_Object = MibTableColumn
mpanlFramerOverruns = _MpanlFramerOverruns_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 3, 13, 1, 8),
    _MpanlFramerOverruns_Type()
)
mpanlFramerOverruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlFramerOverruns.setStatus("mandatory")
_MpanlFramerUnderruns_Type = Counter32
_MpanlFramerUnderruns_Object = MibTableColumn
mpanlFramerUnderruns = _MpanlFramerUnderruns_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 3, 13, 1, 9),
    _MpanlFramerUnderruns_Type()
)
mpanlFramerUnderruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlFramerUnderruns.setStatus("mandatory")
_MpanlFramerLargeFrmErrors_Type = Counter32
_MpanlFramerLargeFrmErrors_Object = MibTableColumn
mpanlFramerLargeFrmErrors = _MpanlFramerLargeFrmErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 3, 13, 1, 10),
    _MpanlFramerLargeFrmErrors_Type()
)
mpanlFramerLargeFrmErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlFramerLargeFrmErrors.setStatus("mandatory")
_MpanlFramerFrmModeErrors_Type = Counter32
_MpanlFramerFrmModeErrors_Object = MibTableColumn
mpanlFramerFrmModeErrors = _MpanlFramerFrmModeErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 3, 13, 1, 11),
    _MpanlFramerFrmModeErrors_Type()
)
mpanlFramerFrmModeErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlFramerFrmModeErrors.setStatus("mandatory")
_MpanlFramerUtilTable_Object = MibTable
mpanlFramerUtilTable = _MpanlFramerUtilTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 3, 14)
)
if mibBuilder.loadTexts:
    mpanlFramerUtilTable.setStatus("mandatory")
_MpanlFramerUtilEntry_Object = MibTableRow
mpanlFramerUtilEntry = _MpanlFramerUtilEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 3, 14, 1)
)
mpanlFramerUtilEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-MpaNetworkLinkMIB", "mpanlIndex"),
    (0, "Nortel-Magellan-Passport-MpaNetworkLinkMIB", "mpanlFramerIndex"),
)
if mibBuilder.loadTexts:
    mpanlFramerUtilEntry.setStatus("mandatory")


class _MpanlFramerNormPrioLinkUtilToIf_Type(Gauge32):
    """Custom type mpanlFramerNormPrioLinkUtilToIf based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_MpanlFramerNormPrioLinkUtilToIf_Type.__name__ = "Gauge32"
_MpanlFramerNormPrioLinkUtilToIf_Object = MibTableColumn
mpanlFramerNormPrioLinkUtilToIf = _MpanlFramerNormPrioLinkUtilToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 3, 14, 1, 1),
    _MpanlFramerNormPrioLinkUtilToIf_Type()
)
mpanlFramerNormPrioLinkUtilToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlFramerNormPrioLinkUtilToIf.setStatus("mandatory")


class _MpanlFramerNormPrioLinkUtilFromIf_Type(Gauge32):
    """Custom type mpanlFramerNormPrioLinkUtilFromIf based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_MpanlFramerNormPrioLinkUtilFromIf_Type.__name__ = "Gauge32"
_MpanlFramerNormPrioLinkUtilFromIf_Object = MibTableColumn
mpanlFramerNormPrioLinkUtilFromIf = _MpanlFramerNormPrioLinkUtilFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 3, 14, 1, 3),
    _MpanlFramerNormPrioLinkUtilFromIf_Type()
)
mpanlFramerNormPrioLinkUtilFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlFramerNormPrioLinkUtilFromIf.setStatus("mandatory")
_MpanlPrefixDna_ObjectIdentity = ObjectIdentity
mpanlPrefixDna = _MpanlPrefixDna_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 4)
)
_MpanlPrefixDnaRowStatusTable_Object = MibTable
mpanlPrefixDnaRowStatusTable = _MpanlPrefixDnaRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 4, 1)
)
if mibBuilder.loadTexts:
    mpanlPrefixDnaRowStatusTable.setStatus("mandatory")
_MpanlPrefixDnaRowStatusEntry_Object = MibTableRow
mpanlPrefixDnaRowStatusEntry = _MpanlPrefixDnaRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 4, 1, 1)
)
mpanlPrefixDnaRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-MpaNetworkLinkMIB", "mpanlIndex"),
    (0, "Nortel-Magellan-Passport-MpaNetworkLinkMIB", "mpanlPrefixDnaNumberingPlanIndicatorIndex"),
    (0, "Nortel-Magellan-Passport-MpaNetworkLinkMIB", "mpanlPrefixDnaDataNetworkAddressIndex"),
)
if mibBuilder.loadTexts:
    mpanlPrefixDnaRowStatusEntry.setStatus("mandatory")
_MpanlPrefixDnaRowStatus_Type = RowStatus
_MpanlPrefixDnaRowStatus_Object = MibTableColumn
mpanlPrefixDnaRowStatus = _MpanlPrefixDnaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 4, 1, 1, 1),
    _MpanlPrefixDnaRowStatus_Type()
)
mpanlPrefixDnaRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlPrefixDnaRowStatus.setStatus("mandatory")
_MpanlPrefixDnaComponentName_Type = DisplayString
_MpanlPrefixDnaComponentName_Object = MibTableColumn
mpanlPrefixDnaComponentName = _MpanlPrefixDnaComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 4, 1, 1, 2),
    _MpanlPrefixDnaComponentName_Type()
)
mpanlPrefixDnaComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlPrefixDnaComponentName.setStatus("mandatory")
_MpanlPrefixDnaStorageType_Type = StorageType
_MpanlPrefixDnaStorageType_Object = MibTableColumn
mpanlPrefixDnaStorageType = _MpanlPrefixDnaStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 4, 1, 1, 4),
    _MpanlPrefixDnaStorageType_Type()
)
mpanlPrefixDnaStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlPrefixDnaStorageType.setStatus("mandatory")


class _MpanlPrefixDnaNumberingPlanIndicatorIndex_Type(Integer32):
    """Custom type mpanlPrefixDnaNumberingPlanIndicatorIndex based on Integer32"""
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


_MpanlPrefixDnaNumberingPlanIndicatorIndex_Type.__name__ = "Integer32"
_MpanlPrefixDnaNumberingPlanIndicatorIndex_Object = MibTableColumn
mpanlPrefixDnaNumberingPlanIndicatorIndex = _MpanlPrefixDnaNumberingPlanIndicatorIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 4, 1, 1, 10),
    _MpanlPrefixDnaNumberingPlanIndicatorIndex_Type()
)
mpanlPrefixDnaNumberingPlanIndicatorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mpanlPrefixDnaNumberingPlanIndicatorIndex.setStatus("mandatory")


class _MpanlPrefixDnaDataNetworkAddressIndex_Type(DigitString):
    """Custom type mpanlPrefixDnaDataNetworkAddressIndex based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_MpanlPrefixDnaDataNetworkAddressIndex_Type.__name__ = "DigitString"
_MpanlPrefixDnaDataNetworkAddressIndex_Object = MibTableColumn
mpanlPrefixDnaDataNetworkAddressIndex = _MpanlPrefixDnaDataNetworkAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 4, 1, 1, 11),
    _MpanlPrefixDnaDataNetworkAddressIndex_Type()
)
mpanlPrefixDnaDataNetworkAddressIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mpanlPrefixDnaDataNetworkAddressIndex.setStatus("mandatory")
_MpanlDlci_ObjectIdentity = ObjectIdentity
mpanlDlci = _MpanlDlci_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5)
)
_MpanlDlciRowStatusTable_Object = MibTable
mpanlDlciRowStatusTable = _MpanlDlciRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 1)
)
if mibBuilder.loadTexts:
    mpanlDlciRowStatusTable.setStatus("mandatory")
_MpanlDlciRowStatusEntry_Object = MibTableRow
mpanlDlciRowStatusEntry = _MpanlDlciRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 1, 1)
)
mpanlDlciRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-MpaNetworkLinkMIB", "mpanlIndex"),
    (0, "Nortel-Magellan-Passport-MpaNetworkLinkMIB", "mpanlDlciIndex"),
)
if mibBuilder.loadTexts:
    mpanlDlciRowStatusEntry.setStatus("mandatory")
_MpanlDlciRowStatus_Type = RowStatus
_MpanlDlciRowStatus_Object = MibTableColumn
mpanlDlciRowStatus = _MpanlDlciRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 1, 1, 1),
    _MpanlDlciRowStatus_Type()
)
mpanlDlciRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciRowStatus.setStatus("mandatory")
_MpanlDlciComponentName_Type = DisplayString
_MpanlDlciComponentName_Object = MibTableColumn
mpanlDlciComponentName = _MpanlDlciComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 1, 1, 2),
    _MpanlDlciComponentName_Type()
)
mpanlDlciComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciComponentName.setStatus("mandatory")
_MpanlDlciStorageType_Type = StorageType
_MpanlDlciStorageType_Object = MibTableColumn
mpanlDlciStorageType = _MpanlDlciStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 1, 1, 4),
    _MpanlDlciStorageType_Type()
)
mpanlDlciStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciStorageType.setStatus("mandatory")


class _MpanlDlciIndex_Type(Integer32):
    """Custom type mpanlDlciIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(17, 1007),
    )


_MpanlDlciIndex_Type.__name__ = "Integer32"
_MpanlDlciIndex_Object = MibTableColumn
mpanlDlciIndex = _MpanlDlciIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 1, 1, 10),
    _MpanlDlciIndex_Type()
)
mpanlDlciIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mpanlDlciIndex.setStatus("mandatory")
_MpanlDlciLb_ObjectIdentity = ObjectIdentity
mpanlDlciLb = _MpanlDlciLb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 2)
)
_MpanlDlciLbRowStatusTable_Object = MibTable
mpanlDlciLbRowStatusTable = _MpanlDlciLbRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 2, 1)
)
if mibBuilder.loadTexts:
    mpanlDlciLbRowStatusTable.setStatus("mandatory")
_MpanlDlciLbRowStatusEntry_Object = MibTableRow
mpanlDlciLbRowStatusEntry = _MpanlDlciLbRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 2, 1, 1)
)
mpanlDlciLbRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-MpaNetworkLinkMIB", "mpanlIndex"),
    (0, "Nortel-Magellan-Passport-MpaNetworkLinkMIB", "mpanlDlciIndex"),
    (0, "Nortel-Magellan-Passport-MpaNetworkLinkMIB", "mpanlDlciLbIndex"),
)
if mibBuilder.loadTexts:
    mpanlDlciLbRowStatusEntry.setStatus("mandatory")
_MpanlDlciLbRowStatus_Type = RowStatus
_MpanlDlciLbRowStatus_Object = MibTableColumn
mpanlDlciLbRowStatus = _MpanlDlciLbRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 2, 1, 1, 1),
    _MpanlDlciLbRowStatus_Type()
)
mpanlDlciLbRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciLbRowStatus.setStatus("mandatory")
_MpanlDlciLbComponentName_Type = DisplayString
_MpanlDlciLbComponentName_Object = MibTableColumn
mpanlDlciLbComponentName = _MpanlDlciLbComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 2, 1, 1, 2),
    _MpanlDlciLbComponentName_Type()
)
mpanlDlciLbComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciLbComponentName.setStatus("mandatory")
_MpanlDlciLbStorageType_Type = StorageType
_MpanlDlciLbStorageType_Object = MibTableColumn
mpanlDlciLbStorageType = _MpanlDlciLbStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 2, 1, 1, 4),
    _MpanlDlciLbStorageType_Type()
)
mpanlDlciLbStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciLbStorageType.setStatus("mandatory")
_MpanlDlciLbIndex_Type = NonReplicated
_MpanlDlciLbIndex_Object = MibTableColumn
mpanlDlciLbIndex = _MpanlDlciLbIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 2, 1, 1, 10),
    _MpanlDlciLbIndex_Type()
)
mpanlDlciLbIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mpanlDlciLbIndex.setStatus("mandatory")
_MpanlDlciLbStatsTable_Object = MibTable
mpanlDlciLbStatsTable = _MpanlDlciLbStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 2, 10)
)
if mibBuilder.loadTexts:
    mpanlDlciLbStatsTable.setStatus("mandatory")
_MpanlDlciLbStatsEntry_Object = MibTableRow
mpanlDlciLbStatsEntry = _MpanlDlciLbStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 2, 10, 1)
)
mpanlDlciLbStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-MpaNetworkLinkMIB", "mpanlIndex"),
    (0, "Nortel-Magellan-Passport-MpaNetworkLinkMIB", "mpanlDlciIndex"),
    (0, "Nortel-Magellan-Passport-MpaNetworkLinkMIB", "mpanlDlciLbIndex"),
)
if mibBuilder.loadTexts:
    mpanlDlciLbStatsEntry.setStatus("mandatory")


class _MpanlDlciLbLocalTotalFrm_Type(Unsigned32):
    """Custom type mpanlDlciLbLocalTotalFrm based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MpanlDlciLbLocalTotalFrm_Type.__name__ = "Unsigned32"
_MpanlDlciLbLocalTotalFrm_Object = MibTableColumn
mpanlDlciLbLocalTotalFrm = _MpanlDlciLbLocalTotalFrm_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 2, 10, 1, 1),
    _MpanlDlciLbLocalTotalFrm_Type()
)
mpanlDlciLbLocalTotalFrm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciLbLocalTotalFrm.setStatus("mandatory")


class _MpanlDlciLbLocalTotalBytes_Type(Unsigned32):
    """Custom type mpanlDlciLbLocalTotalBytes based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MpanlDlciLbLocalTotalBytes_Type.__name__ = "Unsigned32"
_MpanlDlciLbLocalTotalBytes_Object = MibTableColumn
mpanlDlciLbLocalTotalBytes = _MpanlDlciLbLocalTotalBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 2, 10, 1, 2),
    _MpanlDlciLbLocalTotalBytes_Type()
)
mpanlDlciLbLocalTotalBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciLbLocalTotalBytes.setStatus("mandatory")


class _MpanlDlciLbLocalFecnFrm_Type(Unsigned32):
    """Custom type mpanlDlciLbLocalFecnFrm based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MpanlDlciLbLocalFecnFrm_Type.__name__ = "Unsigned32"
_MpanlDlciLbLocalFecnFrm_Object = MibTableColumn
mpanlDlciLbLocalFecnFrm = _MpanlDlciLbLocalFecnFrm_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 2, 10, 1, 3),
    _MpanlDlciLbLocalFecnFrm_Type()
)
mpanlDlciLbLocalFecnFrm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciLbLocalFecnFrm.setStatus("mandatory")


class _MpanlDlciLbLocalBecnFrm_Type(Unsigned32):
    """Custom type mpanlDlciLbLocalBecnFrm based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MpanlDlciLbLocalBecnFrm_Type.__name__ = "Unsigned32"
_MpanlDlciLbLocalBecnFrm_Object = MibTableColumn
mpanlDlciLbLocalBecnFrm = _MpanlDlciLbLocalBecnFrm_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 2, 10, 1, 4),
    _MpanlDlciLbLocalBecnFrm_Type()
)
mpanlDlciLbLocalBecnFrm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciLbLocalBecnFrm.setStatus("mandatory")


class _MpanlDlciLbLocalDeFrm_Type(Unsigned32):
    """Custom type mpanlDlciLbLocalDeFrm based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MpanlDlciLbLocalDeFrm_Type.__name__ = "Unsigned32"
_MpanlDlciLbLocalDeFrm_Object = MibTableColumn
mpanlDlciLbLocalDeFrm = _MpanlDlciLbLocalDeFrm_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 2, 10, 1, 5),
    _MpanlDlciLbLocalDeFrm_Type()
)
mpanlDlciLbLocalDeFrm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciLbLocalDeFrm.setStatus("mandatory")


class _MpanlDlciLbLocalDeBytes_Type(Unsigned32):
    """Custom type mpanlDlciLbLocalDeBytes based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MpanlDlciLbLocalDeBytes_Type.__name__ = "Unsigned32"
_MpanlDlciLbLocalDeBytes_Object = MibTableColumn
mpanlDlciLbLocalDeBytes = _MpanlDlciLbLocalDeBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 2, 10, 1, 6),
    _MpanlDlciLbLocalDeBytes_Type()
)
mpanlDlciLbLocalDeBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciLbLocalDeBytes.setStatus("mandatory")


class _MpanlDlciLbRemoteTotalFrm_Type(Unsigned32):
    """Custom type mpanlDlciLbRemoteTotalFrm based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MpanlDlciLbRemoteTotalFrm_Type.__name__ = "Unsigned32"
_MpanlDlciLbRemoteTotalFrm_Object = MibTableColumn
mpanlDlciLbRemoteTotalFrm = _MpanlDlciLbRemoteTotalFrm_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 2, 10, 1, 7),
    _MpanlDlciLbRemoteTotalFrm_Type()
)
mpanlDlciLbRemoteTotalFrm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciLbRemoteTotalFrm.setStatus("mandatory")


class _MpanlDlciLbRemoteTotalBytes_Type(Unsigned32):
    """Custom type mpanlDlciLbRemoteTotalBytes based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MpanlDlciLbRemoteTotalBytes_Type.__name__ = "Unsigned32"
_MpanlDlciLbRemoteTotalBytes_Object = MibTableColumn
mpanlDlciLbRemoteTotalBytes = _MpanlDlciLbRemoteTotalBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 2, 10, 1, 8),
    _MpanlDlciLbRemoteTotalBytes_Type()
)
mpanlDlciLbRemoteTotalBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciLbRemoteTotalBytes.setStatus("mandatory")


class _MpanlDlciLbRemoteFecnFrm_Type(Unsigned32):
    """Custom type mpanlDlciLbRemoteFecnFrm based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MpanlDlciLbRemoteFecnFrm_Type.__name__ = "Unsigned32"
_MpanlDlciLbRemoteFecnFrm_Object = MibTableColumn
mpanlDlciLbRemoteFecnFrm = _MpanlDlciLbRemoteFecnFrm_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 2, 10, 1, 9),
    _MpanlDlciLbRemoteFecnFrm_Type()
)
mpanlDlciLbRemoteFecnFrm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciLbRemoteFecnFrm.setStatus("mandatory")


class _MpanlDlciLbRemoteBecnFrm_Type(Unsigned32):
    """Custom type mpanlDlciLbRemoteBecnFrm based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MpanlDlciLbRemoteBecnFrm_Type.__name__ = "Unsigned32"
_MpanlDlciLbRemoteBecnFrm_Object = MibTableColumn
mpanlDlciLbRemoteBecnFrm = _MpanlDlciLbRemoteBecnFrm_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 2, 10, 1, 10),
    _MpanlDlciLbRemoteBecnFrm_Type()
)
mpanlDlciLbRemoteBecnFrm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciLbRemoteBecnFrm.setStatus("mandatory")


class _MpanlDlciLbRemoteDeFrm_Type(Unsigned32):
    """Custom type mpanlDlciLbRemoteDeFrm based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MpanlDlciLbRemoteDeFrm_Type.__name__ = "Unsigned32"
_MpanlDlciLbRemoteDeFrm_Object = MibTableColumn
mpanlDlciLbRemoteDeFrm = _MpanlDlciLbRemoteDeFrm_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 2, 10, 1, 13),
    _MpanlDlciLbRemoteDeFrm_Type()
)
mpanlDlciLbRemoteDeFrm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciLbRemoteDeFrm.setStatus("mandatory")


class _MpanlDlciLbRemoteDeBytes_Type(Unsigned32):
    """Custom type mpanlDlciLbRemoteDeBytes based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MpanlDlciLbRemoteDeBytes_Type.__name__ = "Unsigned32"
_MpanlDlciLbRemoteDeBytes_Object = MibTableColumn
mpanlDlciLbRemoteDeBytes = _MpanlDlciLbRemoteDeBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 2, 10, 1, 14),
    _MpanlDlciLbRemoteDeBytes_Type()
)
mpanlDlciLbRemoteDeBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciLbRemoteDeBytes.setStatus("mandatory")
_MpanlDlciVc_ObjectIdentity = ObjectIdentity
mpanlDlciVc = _MpanlDlciVc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 3)
)
_MpanlDlciVcRowStatusTable_Object = MibTable
mpanlDlciVcRowStatusTable = _MpanlDlciVcRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 3, 1)
)
if mibBuilder.loadTexts:
    mpanlDlciVcRowStatusTable.setStatus("mandatory")
_MpanlDlciVcRowStatusEntry_Object = MibTableRow
mpanlDlciVcRowStatusEntry = _MpanlDlciVcRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 3, 1, 1)
)
mpanlDlciVcRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-MpaNetworkLinkMIB", "mpanlIndex"),
    (0, "Nortel-Magellan-Passport-MpaNetworkLinkMIB", "mpanlDlciIndex"),
    (0, "Nortel-Magellan-Passport-MpaNetworkLinkMIB", "mpanlDlciVcIndex"),
)
if mibBuilder.loadTexts:
    mpanlDlciVcRowStatusEntry.setStatus("mandatory")
_MpanlDlciVcRowStatus_Type = RowStatus
_MpanlDlciVcRowStatus_Object = MibTableColumn
mpanlDlciVcRowStatus = _MpanlDlciVcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 3, 1, 1, 1),
    _MpanlDlciVcRowStatus_Type()
)
mpanlDlciVcRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciVcRowStatus.setStatus("mandatory")
_MpanlDlciVcComponentName_Type = DisplayString
_MpanlDlciVcComponentName_Object = MibTableColumn
mpanlDlciVcComponentName = _MpanlDlciVcComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 3, 1, 1, 2),
    _MpanlDlciVcComponentName_Type()
)
mpanlDlciVcComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciVcComponentName.setStatus("mandatory")
_MpanlDlciVcStorageType_Type = StorageType
_MpanlDlciVcStorageType_Object = MibTableColumn
mpanlDlciVcStorageType = _MpanlDlciVcStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 3, 1, 1, 4),
    _MpanlDlciVcStorageType_Type()
)
mpanlDlciVcStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciVcStorageType.setStatus("mandatory")
_MpanlDlciVcIndex_Type = NonReplicated
_MpanlDlciVcIndex_Object = MibTableColumn
mpanlDlciVcIndex = _MpanlDlciVcIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 3, 1, 1, 10),
    _MpanlDlciVcIndex_Type()
)
mpanlDlciVcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mpanlDlciVcIndex.setStatus("mandatory")
_MpanlDlciVcCadTable_Object = MibTable
mpanlDlciVcCadTable = _MpanlDlciVcCadTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 3, 10)
)
if mibBuilder.loadTexts:
    mpanlDlciVcCadTable.setStatus("mandatory")
_MpanlDlciVcCadEntry_Object = MibTableRow
mpanlDlciVcCadEntry = _MpanlDlciVcCadEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 3, 10, 1)
)
mpanlDlciVcCadEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-MpaNetworkLinkMIB", "mpanlIndex"),
    (0, "Nortel-Magellan-Passport-MpaNetworkLinkMIB", "mpanlDlciIndex"),
    (0, "Nortel-Magellan-Passport-MpaNetworkLinkMIB", "mpanlDlciVcIndex"),
)
if mibBuilder.loadTexts:
    mpanlDlciVcCadEntry.setStatus("mandatory")


class _MpanlDlciVcType_Type(Integer32):
    """Custom type mpanlDlciVcType based on Integer32"""
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


_MpanlDlciVcType_Type.__name__ = "Integer32"
_MpanlDlciVcType_Object = MibTableColumn
mpanlDlciVcType = _MpanlDlciVcType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 3, 10, 1, 1),
    _MpanlDlciVcType_Type()
)
mpanlDlciVcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciVcType.setStatus("mandatory")


class _MpanlDlciVcState_Type(Integer32):
    """Custom type mpanlDlciVcState based on Integer32"""
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


_MpanlDlciVcState_Type.__name__ = "Integer32"
_MpanlDlciVcState_Object = MibTableColumn
mpanlDlciVcState = _MpanlDlciVcState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 3, 10, 1, 2),
    _MpanlDlciVcState_Type()
)
mpanlDlciVcState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciVcState.setStatus("mandatory")


class _MpanlDlciVcPreviousState_Type(Integer32):
    """Custom type mpanlDlciVcPreviousState based on Integer32"""
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


_MpanlDlciVcPreviousState_Type.__name__ = "Integer32"
_MpanlDlciVcPreviousState_Object = MibTableColumn
mpanlDlciVcPreviousState = _MpanlDlciVcPreviousState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 3, 10, 1, 3),
    _MpanlDlciVcPreviousState_Type()
)
mpanlDlciVcPreviousState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciVcPreviousState.setStatus("mandatory")


class _MpanlDlciVcDiagnosticCode_Type(Unsigned32):
    """Custom type mpanlDlciVcDiagnosticCode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MpanlDlciVcDiagnosticCode_Type.__name__ = "Unsigned32"
_MpanlDlciVcDiagnosticCode_Object = MibTableColumn
mpanlDlciVcDiagnosticCode = _MpanlDlciVcDiagnosticCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 3, 10, 1, 4),
    _MpanlDlciVcDiagnosticCode_Type()
)
mpanlDlciVcDiagnosticCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciVcDiagnosticCode.setStatus("mandatory")


class _MpanlDlciVcPreviousDiagnosticCode_Type(Unsigned32):
    """Custom type mpanlDlciVcPreviousDiagnosticCode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MpanlDlciVcPreviousDiagnosticCode_Type.__name__ = "Unsigned32"
_MpanlDlciVcPreviousDiagnosticCode_Object = MibTableColumn
mpanlDlciVcPreviousDiagnosticCode = _MpanlDlciVcPreviousDiagnosticCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 3, 10, 1, 5),
    _MpanlDlciVcPreviousDiagnosticCode_Type()
)
mpanlDlciVcPreviousDiagnosticCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciVcPreviousDiagnosticCode.setStatus("mandatory")


class _MpanlDlciVcCalledNpi_Type(Integer32):
    """Custom type mpanlDlciVcCalledNpi based on Integer32"""
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


_MpanlDlciVcCalledNpi_Type.__name__ = "Integer32"
_MpanlDlciVcCalledNpi_Object = MibTableColumn
mpanlDlciVcCalledNpi = _MpanlDlciVcCalledNpi_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 3, 10, 1, 6),
    _MpanlDlciVcCalledNpi_Type()
)
mpanlDlciVcCalledNpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciVcCalledNpi.setStatus("mandatory")


class _MpanlDlciVcCalledDna_Type(DigitString):
    """Custom type mpanlDlciVcCalledDna based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_MpanlDlciVcCalledDna_Type.__name__ = "DigitString"
_MpanlDlciVcCalledDna_Object = MibTableColumn
mpanlDlciVcCalledDna = _MpanlDlciVcCalledDna_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 3, 10, 1, 7),
    _MpanlDlciVcCalledDna_Type()
)
mpanlDlciVcCalledDna.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciVcCalledDna.setStatus("mandatory")


class _MpanlDlciVcCalledLcn_Type(Unsigned32):
    """Custom type mpanlDlciVcCalledLcn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MpanlDlciVcCalledLcn_Type.__name__ = "Unsigned32"
_MpanlDlciVcCalledLcn_Object = MibTableColumn
mpanlDlciVcCalledLcn = _MpanlDlciVcCalledLcn_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 3, 10, 1, 8),
    _MpanlDlciVcCalledLcn_Type()
)
mpanlDlciVcCalledLcn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciVcCalledLcn.setStatus("mandatory")


class _MpanlDlciVcCallingNpi_Type(Integer32):
    """Custom type mpanlDlciVcCallingNpi based on Integer32"""
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


_MpanlDlciVcCallingNpi_Type.__name__ = "Integer32"
_MpanlDlciVcCallingNpi_Object = MibTableColumn
mpanlDlciVcCallingNpi = _MpanlDlciVcCallingNpi_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 3, 10, 1, 9),
    _MpanlDlciVcCallingNpi_Type()
)
mpanlDlciVcCallingNpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciVcCallingNpi.setStatus("mandatory")


class _MpanlDlciVcCallingDna_Type(DigitString):
    """Custom type mpanlDlciVcCallingDna based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_MpanlDlciVcCallingDna_Type.__name__ = "DigitString"
_MpanlDlciVcCallingDna_Object = MibTableColumn
mpanlDlciVcCallingDna = _MpanlDlciVcCallingDna_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 3, 10, 1, 10),
    _MpanlDlciVcCallingDna_Type()
)
mpanlDlciVcCallingDna.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciVcCallingDna.setStatus("mandatory")


class _MpanlDlciVcCallingLcn_Type(Unsigned32):
    """Custom type mpanlDlciVcCallingLcn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MpanlDlciVcCallingLcn_Type.__name__ = "Unsigned32"
_MpanlDlciVcCallingLcn_Object = MibTableColumn
mpanlDlciVcCallingLcn = _MpanlDlciVcCallingLcn_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 3, 10, 1, 11),
    _MpanlDlciVcCallingLcn_Type()
)
mpanlDlciVcCallingLcn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciVcCallingLcn.setStatus("mandatory")


class _MpanlDlciVcAccountingEnabled_Type(Integer32):
    """Custom type mpanlDlciVcAccountingEnabled based on Integer32"""
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


_MpanlDlciVcAccountingEnabled_Type.__name__ = "Integer32"
_MpanlDlciVcAccountingEnabled_Object = MibTableColumn
mpanlDlciVcAccountingEnabled = _MpanlDlciVcAccountingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 3, 10, 1, 12),
    _MpanlDlciVcAccountingEnabled_Type()
)
mpanlDlciVcAccountingEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciVcAccountingEnabled.setStatus("mandatory")


class _MpanlDlciVcFastSelectCall_Type(Integer32):
    """Custom type mpanlDlciVcFastSelectCall based on Integer32"""
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


_MpanlDlciVcFastSelectCall_Type.__name__ = "Integer32"
_MpanlDlciVcFastSelectCall_Object = MibTableColumn
mpanlDlciVcFastSelectCall = _MpanlDlciVcFastSelectCall_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 3, 10, 1, 13),
    _MpanlDlciVcFastSelectCall_Type()
)
mpanlDlciVcFastSelectCall.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciVcFastSelectCall.setStatus("mandatory")


class _MpanlDlciVcPathReliability_Type(Integer32):
    """Custom type mpanlDlciVcPathReliability based on Integer32"""
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


_MpanlDlciVcPathReliability_Type.__name__ = "Integer32"
_MpanlDlciVcPathReliability_Object = MibTableColumn
mpanlDlciVcPathReliability = _MpanlDlciVcPathReliability_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 3, 10, 1, 19),
    _MpanlDlciVcPathReliability_Type()
)
mpanlDlciVcPathReliability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciVcPathReliability.setStatus("mandatory")


class _MpanlDlciVcAccountingEnd_Type(Integer32):
    """Custom type mpanlDlciVcAccountingEnd based on Integer32"""
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


_MpanlDlciVcAccountingEnd_Type.__name__ = "Integer32"
_MpanlDlciVcAccountingEnd_Object = MibTableColumn
mpanlDlciVcAccountingEnd = _MpanlDlciVcAccountingEnd_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 3, 10, 1, 20),
    _MpanlDlciVcAccountingEnd_Type()
)
mpanlDlciVcAccountingEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciVcAccountingEnd.setStatus("mandatory")


class _MpanlDlciVcPriority_Type(Integer32):
    """Custom type mpanlDlciVcPriority based on Integer32"""
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


_MpanlDlciVcPriority_Type.__name__ = "Integer32"
_MpanlDlciVcPriority_Object = MibTableColumn
mpanlDlciVcPriority = _MpanlDlciVcPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 3, 10, 1, 21),
    _MpanlDlciVcPriority_Type()
)
mpanlDlciVcPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciVcPriority.setStatus("mandatory")


class _MpanlDlciVcSegmentSize_Type(Unsigned32):
    """Custom type mpanlDlciVcSegmentSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_MpanlDlciVcSegmentSize_Type.__name__ = "Unsigned32"
_MpanlDlciVcSegmentSize_Object = MibTableColumn
mpanlDlciVcSegmentSize = _MpanlDlciVcSegmentSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 3, 10, 1, 22),
    _MpanlDlciVcSegmentSize_Type()
)
mpanlDlciVcSegmentSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciVcSegmentSize.setStatus("mandatory")


class _MpanlDlciVcMaxSubnetPktSize_Type(Unsigned32):
    """Custom type mpanlDlciVcMaxSubnetPktSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_MpanlDlciVcMaxSubnetPktSize_Type.__name__ = "Unsigned32"
_MpanlDlciVcMaxSubnetPktSize_Object = MibTableColumn
mpanlDlciVcMaxSubnetPktSize = _MpanlDlciVcMaxSubnetPktSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 3, 10, 1, 27),
    _MpanlDlciVcMaxSubnetPktSize_Type()
)
mpanlDlciVcMaxSubnetPktSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciVcMaxSubnetPktSize.setStatus("mandatory")


class _MpanlDlciVcRcosToNetwork_Type(Integer32):
    """Custom type mpanlDlciVcRcosToNetwork based on Integer32"""
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


_MpanlDlciVcRcosToNetwork_Type.__name__ = "Integer32"
_MpanlDlciVcRcosToNetwork_Object = MibTableColumn
mpanlDlciVcRcosToNetwork = _MpanlDlciVcRcosToNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 3, 10, 1, 28),
    _MpanlDlciVcRcosToNetwork_Type()
)
mpanlDlciVcRcosToNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciVcRcosToNetwork.setStatus("mandatory")


class _MpanlDlciVcRcosFromNetwork_Type(Integer32):
    """Custom type mpanlDlciVcRcosFromNetwork based on Integer32"""
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


_MpanlDlciVcRcosFromNetwork_Type.__name__ = "Integer32"
_MpanlDlciVcRcosFromNetwork_Object = MibTableColumn
mpanlDlciVcRcosFromNetwork = _MpanlDlciVcRcosFromNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 3, 10, 1, 29),
    _MpanlDlciVcRcosFromNetwork_Type()
)
mpanlDlciVcRcosFromNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciVcRcosFromNetwork.setStatus("mandatory")


class _MpanlDlciVcEmissionPriorityToNetwork_Type(Integer32):
    """Custom type mpanlDlciVcEmissionPriorityToNetwork based on Integer32"""
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


_MpanlDlciVcEmissionPriorityToNetwork_Type.__name__ = "Integer32"
_MpanlDlciVcEmissionPriorityToNetwork_Object = MibTableColumn
mpanlDlciVcEmissionPriorityToNetwork = _MpanlDlciVcEmissionPriorityToNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 3, 10, 1, 30),
    _MpanlDlciVcEmissionPriorityToNetwork_Type()
)
mpanlDlciVcEmissionPriorityToNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciVcEmissionPriorityToNetwork.setStatus("mandatory")


class _MpanlDlciVcEmissionPriorityFromNetwork_Type(Integer32):
    """Custom type mpanlDlciVcEmissionPriorityFromNetwork based on Integer32"""
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


_MpanlDlciVcEmissionPriorityFromNetwork_Type.__name__ = "Integer32"
_MpanlDlciVcEmissionPriorityFromNetwork_Object = MibTableColumn
mpanlDlciVcEmissionPriorityFromNetwork = _MpanlDlciVcEmissionPriorityFromNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 3, 10, 1, 31),
    _MpanlDlciVcEmissionPriorityFromNetwork_Type()
)
mpanlDlciVcEmissionPriorityFromNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciVcEmissionPriorityFromNetwork.setStatus("mandatory")


class _MpanlDlciVcDataPath_Type(AsciiString):
    """Custom type mpanlDlciVcDataPath based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MpanlDlciVcDataPath_Type.__name__ = "AsciiString"
_MpanlDlciVcDataPath_Object = MibTableColumn
mpanlDlciVcDataPath = _MpanlDlciVcDataPath_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 3, 10, 1, 32),
    _MpanlDlciVcDataPath_Type()
)
mpanlDlciVcDataPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciVcDataPath.setStatus("mandatory")
_MpanlDlciVcIntdTable_Object = MibTable
mpanlDlciVcIntdTable = _MpanlDlciVcIntdTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 3, 11)
)
if mibBuilder.loadTexts:
    mpanlDlciVcIntdTable.setStatus("mandatory")
_MpanlDlciVcIntdEntry_Object = MibTableRow
mpanlDlciVcIntdEntry = _MpanlDlciVcIntdEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 3, 11, 1)
)
mpanlDlciVcIntdEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-MpaNetworkLinkMIB", "mpanlIndex"),
    (0, "Nortel-Magellan-Passport-MpaNetworkLinkMIB", "mpanlDlciIndex"),
    (0, "Nortel-Magellan-Passport-MpaNetworkLinkMIB", "mpanlDlciVcIndex"),
)
if mibBuilder.loadTexts:
    mpanlDlciVcIntdEntry.setStatus("mandatory")


class _MpanlDlciVcCallReferenceNumber_Type(Hex):
    """Custom type mpanlDlciVcCallReferenceNumber based on Hex"""
    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_MpanlDlciVcCallReferenceNumber_Type.__name__ = "Hex"
_MpanlDlciVcCallReferenceNumber_Object = MibTableColumn
mpanlDlciVcCallReferenceNumber = _MpanlDlciVcCallReferenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 3, 11, 1, 1),
    _MpanlDlciVcCallReferenceNumber_Type()
)
mpanlDlciVcCallReferenceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciVcCallReferenceNumber.setStatus("mandatory")


class _MpanlDlciVcElapsedTimeTillNow_Type(Unsigned32):
    """Custom type mpanlDlciVcElapsedTimeTillNow based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_MpanlDlciVcElapsedTimeTillNow_Type.__name__ = "Unsigned32"
_MpanlDlciVcElapsedTimeTillNow_Object = MibTableColumn
mpanlDlciVcElapsedTimeTillNow = _MpanlDlciVcElapsedTimeTillNow_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 3, 11, 1, 2),
    _MpanlDlciVcElapsedTimeTillNow_Type()
)
mpanlDlciVcElapsedTimeTillNow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciVcElapsedTimeTillNow.setStatus("mandatory")


class _MpanlDlciVcSegmentsRx_Type(Unsigned32):
    """Custom type mpanlDlciVcSegmentsRx based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_MpanlDlciVcSegmentsRx_Type.__name__ = "Unsigned32"
_MpanlDlciVcSegmentsRx_Object = MibTableColumn
mpanlDlciVcSegmentsRx = _MpanlDlciVcSegmentsRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 3, 11, 1, 3),
    _MpanlDlciVcSegmentsRx_Type()
)
mpanlDlciVcSegmentsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciVcSegmentsRx.setStatus("mandatory")


class _MpanlDlciVcSegmentsSent_Type(Unsigned32):
    """Custom type mpanlDlciVcSegmentsSent based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_MpanlDlciVcSegmentsSent_Type.__name__ = "Unsigned32"
_MpanlDlciVcSegmentsSent_Object = MibTableColumn
mpanlDlciVcSegmentsSent = _MpanlDlciVcSegmentsSent_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 3, 11, 1, 4),
    _MpanlDlciVcSegmentsSent_Type()
)
mpanlDlciVcSegmentsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciVcSegmentsSent.setStatus("mandatory")


class _MpanlDlciVcStartTime_Type(EnterpriseDateAndTime):
    """Custom type mpanlDlciVcStartTime based on EnterpriseDateAndTime"""
    subtypeSpec = EnterpriseDateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(19, 19),
    )


_MpanlDlciVcStartTime_Type.__name__ = "EnterpriseDateAndTime"
_MpanlDlciVcStartTime_Object = MibTableColumn
mpanlDlciVcStartTime = _MpanlDlciVcStartTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 3, 11, 1, 5),
    _MpanlDlciVcStartTime_Type()
)
mpanlDlciVcStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciVcStartTime.setStatus("mandatory")
_MpanlDlciVcFrdTable_Object = MibTable
mpanlDlciVcFrdTable = _MpanlDlciVcFrdTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 3, 12)
)
if mibBuilder.loadTexts:
    mpanlDlciVcFrdTable.setStatus("mandatory")
_MpanlDlciVcFrdEntry_Object = MibTableRow
mpanlDlciVcFrdEntry = _MpanlDlciVcFrdEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 3, 12, 1)
)
mpanlDlciVcFrdEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-MpaNetworkLinkMIB", "mpanlIndex"),
    (0, "Nortel-Magellan-Passport-MpaNetworkLinkMIB", "mpanlDlciIndex"),
    (0, "Nortel-Magellan-Passport-MpaNetworkLinkMIB", "mpanlDlciVcIndex"),
)
if mibBuilder.loadTexts:
    mpanlDlciVcFrdEntry.setStatus("mandatory")


class _MpanlDlciVcFrmCongestedToSubnet_Type(Unsigned32):
    """Custom type mpanlDlciVcFrmCongestedToSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MpanlDlciVcFrmCongestedToSubnet_Type.__name__ = "Unsigned32"
_MpanlDlciVcFrmCongestedToSubnet_Object = MibTableColumn
mpanlDlciVcFrmCongestedToSubnet = _MpanlDlciVcFrmCongestedToSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 3, 12, 1, 2),
    _MpanlDlciVcFrmCongestedToSubnet_Type()
)
mpanlDlciVcFrmCongestedToSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciVcFrmCongestedToSubnet.setStatus("mandatory")


class _MpanlDlciVcCannotForwardToSubnet_Type(Unsigned32):
    """Custom type mpanlDlciVcCannotForwardToSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MpanlDlciVcCannotForwardToSubnet_Type.__name__ = "Unsigned32"
_MpanlDlciVcCannotForwardToSubnet_Object = MibTableColumn
mpanlDlciVcCannotForwardToSubnet = _MpanlDlciVcCannotForwardToSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 3, 12, 1, 3),
    _MpanlDlciVcCannotForwardToSubnet_Type()
)
mpanlDlciVcCannotForwardToSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciVcCannotForwardToSubnet.setStatus("mandatory")


class _MpanlDlciVcNotDataXferToSubnet_Type(Unsigned32):
    """Custom type mpanlDlciVcNotDataXferToSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MpanlDlciVcNotDataXferToSubnet_Type.__name__ = "Unsigned32"
_MpanlDlciVcNotDataXferToSubnet_Object = MibTableColumn
mpanlDlciVcNotDataXferToSubnet = _MpanlDlciVcNotDataXferToSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 3, 12, 1, 4),
    _MpanlDlciVcNotDataXferToSubnet_Type()
)
mpanlDlciVcNotDataXferToSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciVcNotDataXferToSubnet.setStatus("mandatory")


class _MpanlDlciVcOutOfRangeFrmFromSubnet_Type(Unsigned32):
    """Custom type mpanlDlciVcOutOfRangeFrmFromSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MpanlDlciVcOutOfRangeFrmFromSubnet_Type.__name__ = "Unsigned32"
_MpanlDlciVcOutOfRangeFrmFromSubnet_Object = MibTableColumn
mpanlDlciVcOutOfRangeFrmFromSubnet = _MpanlDlciVcOutOfRangeFrmFromSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 3, 12, 1, 5),
    _MpanlDlciVcOutOfRangeFrmFromSubnet_Type()
)
mpanlDlciVcOutOfRangeFrmFromSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciVcOutOfRangeFrmFromSubnet.setStatus("mandatory")


class _MpanlDlciVcCombErrorsFromSubnet_Type(Unsigned32):
    """Custom type mpanlDlciVcCombErrorsFromSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MpanlDlciVcCombErrorsFromSubnet_Type.__name__ = "Unsigned32"
_MpanlDlciVcCombErrorsFromSubnet_Object = MibTableColumn
mpanlDlciVcCombErrorsFromSubnet = _MpanlDlciVcCombErrorsFromSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 3, 12, 1, 6),
    _MpanlDlciVcCombErrorsFromSubnet_Type()
)
mpanlDlciVcCombErrorsFromSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciVcCombErrorsFromSubnet.setStatus("mandatory")


class _MpanlDlciVcDuplicatesFromSubnet_Type(Unsigned32):
    """Custom type mpanlDlciVcDuplicatesFromSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MpanlDlciVcDuplicatesFromSubnet_Type.__name__ = "Unsigned32"
_MpanlDlciVcDuplicatesFromSubnet_Object = MibTableColumn
mpanlDlciVcDuplicatesFromSubnet = _MpanlDlciVcDuplicatesFromSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 3, 12, 1, 7),
    _MpanlDlciVcDuplicatesFromSubnet_Type()
)
mpanlDlciVcDuplicatesFromSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciVcDuplicatesFromSubnet.setStatus("mandatory")


class _MpanlDlciVcNotDataXferFromSubnet_Type(Unsigned32):
    """Custom type mpanlDlciVcNotDataXferFromSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MpanlDlciVcNotDataXferFromSubnet_Type.__name__ = "Unsigned32"
_MpanlDlciVcNotDataXferFromSubnet_Object = MibTableColumn
mpanlDlciVcNotDataXferFromSubnet = _MpanlDlciVcNotDataXferFromSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 3, 12, 1, 8),
    _MpanlDlciVcNotDataXferFromSubnet_Type()
)
mpanlDlciVcNotDataXferFromSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciVcNotDataXferFromSubnet.setStatus("mandatory")


class _MpanlDlciVcFrmLossTimeouts_Type(Unsigned32):
    """Custom type mpanlDlciVcFrmLossTimeouts based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MpanlDlciVcFrmLossTimeouts_Type.__name__ = "Unsigned32"
_MpanlDlciVcFrmLossTimeouts_Object = MibTableColumn
mpanlDlciVcFrmLossTimeouts = _MpanlDlciVcFrmLossTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 3, 12, 1, 9),
    _MpanlDlciVcFrmLossTimeouts_Type()
)
mpanlDlciVcFrmLossTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciVcFrmLossTimeouts.setStatus("mandatory")


class _MpanlDlciVcOoSeqByteCntExceeded_Type(Unsigned32):
    """Custom type mpanlDlciVcOoSeqByteCntExceeded based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MpanlDlciVcOoSeqByteCntExceeded_Type.__name__ = "Unsigned32"
_MpanlDlciVcOoSeqByteCntExceeded_Object = MibTableColumn
mpanlDlciVcOoSeqByteCntExceeded = _MpanlDlciVcOoSeqByteCntExceeded_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 3, 12, 1, 10),
    _MpanlDlciVcOoSeqByteCntExceeded_Type()
)
mpanlDlciVcOoSeqByteCntExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciVcOoSeqByteCntExceeded.setStatus("mandatory")


class _MpanlDlciVcPeakOoSeqPktCount_Type(Unsigned32):
    """Custom type mpanlDlciVcPeakOoSeqPktCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MpanlDlciVcPeakOoSeqPktCount_Type.__name__ = "Unsigned32"
_MpanlDlciVcPeakOoSeqPktCount_Object = MibTableColumn
mpanlDlciVcPeakOoSeqPktCount = _MpanlDlciVcPeakOoSeqPktCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 3, 12, 1, 11),
    _MpanlDlciVcPeakOoSeqPktCount_Type()
)
mpanlDlciVcPeakOoSeqPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciVcPeakOoSeqPktCount.setStatus("mandatory")


class _MpanlDlciVcPeakOoSeqFrmForwarded_Type(Unsigned32):
    """Custom type mpanlDlciVcPeakOoSeqFrmForwarded based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MpanlDlciVcPeakOoSeqFrmForwarded_Type.__name__ = "Unsigned32"
_MpanlDlciVcPeakOoSeqFrmForwarded_Object = MibTableColumn
mpanlDlciVcPeakOoSeqFrmForwarded = _MpanlDlciVcPeakOoSeqFrmForwarded_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 3, 12, 1, 12),
    _MpanlDlciVcPeakOoSeqFrmForwarded_Type()
)
mpanlDlciVcPeakOoSeqFrmForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciVcPeakOoSeqFrmForwarded.setStatus("mandatory")


class _MpanlDlciVcSendSequenceNumber_Type(Unsigned32):
    """Custom type mpanlDlciVcSendSequenceNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MpanlDlciVcSendSequenceNumber_Type.__name__ = "Unsigned32"
_MpanlDlciVcSendSequenceNumber_Object = MibTableColumn
mpanlDlciVcSendSequenceNumber = _MpanlDlciVcSendSequenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 3, 12, 1, 13),
    _MpanlDlciVcSendSequenceNumber_Type()
)
mpanlDlciVcSendSequenceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciVcSendSequenceNumber.setStatus("mandatory")


class _MpanlDlciVcPktRetryTimeouts_Type(Unsigned32):
    """Custom type mpanlDlciVcPktRetryTimeouts based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MpanlDlciVcPktRetryTimeouts_Type.__name__ = "Unsigned32"
_MpanlDlciVcPktRetryTimeouts_Object = MibTableColumn
mpanlDlciVcPktRetryTimeouts = _MpanlDlciVcPktRetryTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 3, 12, 1, 15),
    _MpanlDlciVcPktRetryTimeouts_Type()
)
mpanlDlciVcPktRetryTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciVcPktRetryTimeouts.setStatus("mandatory")


class _MpanlDlciVcPeakRetryQueueSize_Type(Unsigned32):
    """Custom type mpanlDlciVcPeakRetryQueueSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MpanlDlciVcPeakRetryQueueSize_Type.__name__ = "Unsigned32"
_MpanlDlciVcPeakRetryQueueSize_Object = MibTableColumn
mpanlDlciVcPeakRetryQueueSize = _MpanlDlciVcPeakRetryQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 3, 12, 1, 16),
    _MpanlDlciVcPeakRetryQueueSize_Type()
)
mpanlDlciVcPeakRetryQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciVcPeakRetryQueueSize.setStatus("mandatory")


class _MpanlDlciVcSubnetRecoveries_Type(Unsigned32):
    """Custom type mpanlDlciVcSubnetRecoveries based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MpanlDlciVcSubnetRecoveries_Type.__name__ = "Unsigned32"
_MpanlDlciVcSubnetRecoveries_Object = MibTableColumn
mpanlDlciVcSubnetRecoveries = _MpanlDlciVcSubnetRecoveries_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 3, 12, 1, 17),
    _MpanlDlciVcSubnetRecoveries_Type()
)
mpanlDlciVcSubnetRecoveries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciVcSubnetRecoveries.setStatus("mandatory")


class _MpanlDlciVcOoSeqPktCntExceeded_Type(Unsigned32):
    """Custom type mpanlDlciVcOoSeqPktCntExceeded based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MpanlDlciVcOoSeqPktCntExceeded_Type.__name__ = "Unsigned32"
_MpanlDlciVcOoSeqPktCntExceeded_Object = MibTableColumn
mpanlDlciVcOoSeqPktCntExceeded = _MpanlDlciVcOoSeqPktCntExceeded_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 3, 12, 1, 19),
    _MpanlDlciVcOoSeqPktCntExceeded_Type()
)
mpanlDlciVcOoSeqPktCntExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciVcOoSeqPktCntExceeded.setStatus("mandatory")


class _MpanlDlciVcPeakOoSeqByteCount_Type(Unsigned32):
    """Custom type mpanlDlciVcPeakOoSeqByteCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50000),
    )


_MpanlDlciVcPeakOoSeqByteCount_Type.__name__ = "Unsigned32"
_MpanlDlciVcPeakOoSeqByteCount_Object = MibTableColumn
mpanlDlciVcPeakOoSeqByteCount = _MpanlDlciVcPeakOoSeqByteCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 3, 12, 1, 20),
    _MpanlDlciVcPeakOoSeqByteCount_Type()
)
mpanlDlciVcPeakOoSeqByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciVcPeakOoSeqByteCount.setStatus("mandatory")
_MpanlDlciVcDmepTable_Object = MibTable
mpanlDlciVcDmepTable = _MpanlDlciVcDmepTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 3, 417)
)
if mibBuilder.loadTexts:
    mpanlDlciVcDmepTable.setStatus("mandatory")
_MpanlDlciVcDmepEntry_Object = MibTableRow
mpanlDlciVcDmepEntry = _MpanlDlciVcDmepEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 3, 417, 1)
)
mpanlDlciVcDmepEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-MpaNetworkLinkMIB", "mpanlIndex"),
    (0, "Nortel-Magellan-Passport-MpaNetworkLinkMIB", "mpanlDlciIndex"),
    (0, "Nortel-Magellan-Passport-MpaNetworkLinkMIB", "mpanlDlciVcIndex"),
    (0, "Nortel-Magellan-Passport-MpaNetworkLinkMIB", "mpanlDlciVcDmepValue"),
)
if mibBuilder.loadTexts:
    mpanlDlciVcDmepEntry.setStatus("mandatory")
_MpanlDlciVcDmepValue_Type = RowPointer
_MpanlDlciVcDmepValue_Object = MibTableColumn
mpanlDlciVcDmepValue = _MpanlDlciVcDmepValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 3, 417, 1, 1),
    _MpanlDlciVcDmepValue_Type()
)
mpanlDlciVcDmepValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciVcDmepValue.setStatus("mandatory")
_MpanlDlciLCo_ObjectIdentity = ObjectIdentity
mpanlDlciLCo = _MpanlDlciLCo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 4)
)
_MpanlDlciLCoRowStatusTable_Object = MibTable
mpanlDlciLCoRowStatusTable = _MpanlDlciLCoRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 4, 1)
)
if mibBuilder.loadTexts:
    mpanlDlciLCoRowStatusTable.setStatus("mandatory")
_MpanlDlciLCoRowStatusEntry_Object = MibTableRow
mpanlDlciLCoRowStatusEntry = _MpanlDlciLCoRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 4, 1, 1)
)
mpanlDlciLCoRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-MpaNetworkLinkMIB", "mpanlIndex"),
    (0, "Nortel-Magellan-Passport-MpaNetworkLinkMIB", "mpanlDlciIndex"),
    (0, "Nortel-Magellan-Passport-MpaNetworkLinkMIB", "mpanlDlciLCoIndex"),
)
if mibBuilder.loadTexts:
    mpanlDlciLCoRowStatusEntry.setStatus("mandatory")
_MpanlDlciLCoRowStatus_Type = RowStatus
_MpanlDlciLCoRowStatus_Object = MibTableColumn
mpanlDlciLCoRowStatus = _MpanlDlciLCoRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 4, 1, 1, 1),
    _MpanlDlciLCoRowStatus_Type()
)
mpanlDlciLCoRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciLCoRowStatus.setStatus("mandatory")
_MpanlDlciLCoComponentName_Type = DisplayString
_MpanlDlciLCoComponentName_Object = MibTableColumn
mpanlDlciLCoComponentName = _MpanlDlciLCoComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 4, 1, 1, 2),
    _MpanlDlciLCoComponentName_Type()
)
mpanlDlciLCoComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciLCoComponentName.setStatus("mandatory")
_MpanlDlciLCoStorageType_Type = StorageType
_MpanlDlciLCoStorageType_Object = MibTableColumn
mpanlDlciLCoStorageType = _MpanlDlciLCoStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 4, 1, 1, 4),
    _MpanlDlciLCoStorageType_Type()
)
mpanlDlciLCoStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciLCoStorageType.setStatus("mandatory")
_MpanlDlciLCoIndex_Type = NonReplicated
_MpanlDlciLCoIndex_Object = MibTableColumn
mpanlDlciLCoIndex = _MpanlDlciLCoIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 4, 1, 1, 10),
    _MpanlDlciLCoIndex_Type()
)
mpanlDlciLCoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mpanlDlciLCoIndex.setStatus("mandatory")
_MpanlDlciLCoPathDataTable_Object = MibTable
mpanlDlciLCoPathDataTable = _MpanlDlciLCoPathDataTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 4, 10)
)
if mibBuilder.loadTexts:
    mpanlDlciLCoPathDataTable.setStatus("mandatory")
_MpanlDlciLCoPathDataEntry_Object = MibTableRow
mpanlDlciLCoPathDataEntry = _MpanlDlciLCoPathDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 4, 10, 1)
)
mpanlDlciLCoPathDataEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-MpaNetworkLinkMIB", "mpanlIndex"),
    (0, "Nortel-Magellan-Passport-MpaNetworkLinkMIB", "mpanlDlciIndex"),
    (0, "Nortel-Magellan-Passport-MpaNetworkLinkMIB", "mpanlDlciLCoIndex"),
)
if mibBuilder.loadTexts:
    mpanlDlciLCoPathDataEntry.setStatus("mandatory")


class _MpanlDlciLCoState_Type(Integer32):
    """Custom type mpanlDlciLCoState based on Integer32"""
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


_MpanlDlciLCoState_Type.__name__ = "Integer32"
_MpanlDlciLCoState_Object = MibTableColumn
mpanlDlciLCoState = _MpanlDlciLCoState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 4, 10, 1, 1),
    _MpanlDlciLCoState_Type()
)
mpanlDlciLCoState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciLCoState.setStatus("mandatory")


class _MpanlDlciLCoEnd_Type(Integer32):
    """Custom type mpanlDlciLCoEnd based on Integer32"""
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


_MpanlDlciLCoEnd_Type.__name__ = "Integer32"
_MpanlDlciLCoEnd_Object = MibTableColumn
mpanlDlciLCoEnd = _MpanlDlciLCoEnd_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 4, 10, 1, 3),
    _MpanlDlciLCoEnd_Type()
)
mpanlDlciLCoEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciLCoEnd.setStatus("mandatory")


class _MpanlDlciLCoCostMetric_Type(Unsigned32):
    """Custom type mpanlDlciLCoCostMetric based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MpanlDlciLCoCostMetric_Type.__name__ = "Unsigned32"
_MpanlDlciLCoCostMetric_Object = MibTableColumn
mpanlDlciLCoCostMetric = _MpanlDlciLCoCostMetric_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 4, 10, 1, 4),
    _MpanlDlciLCoCostMetric_Type()
)
mpanlDlciLCoCostMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciLCoCostMetric.setStatus("mandatory")


class _MpanlDlciLCoDelayMetric_Type(Unsigned32):
    """Custom type mpanlDlciLCoDelayMetric based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_MpanlDlciLCoDelayMetric_Type.__name__ = "Unsigned32"
_MpanlDlciLCoDelayMetric_Object = MibTableColumn
mpanlDlciLCoDelayMetric = _MpanlDlciLCoDelayMetric_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 4, 10, 1, 5),
    _MpanlDlciLCoDelayMetric_Type()
)
mpanlDlciLCoDelayMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciLCoDelayMetric.setStatus("mandatory")


class _MpanlDlciLCoRoundTripDelay_Type(Unsigned32):
    """Custom type mpanlDlciLCoRoundTripDelay based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000),
    )


_MpanlDlciLCoRoundTripDelay_Type.__name__ = "Unsigned32"
_MpanlDlciLCoRoundTripDelay_Object = MibTableColumn
mpanlDlciLCoRoundTripDelay = _MpanlDlciLCoRoundTripDelay_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 4, 10, 1, 6),
    _MpanlDlciLCoRoundTripDelay_Type()
)
mpanlDlciLCoRoundTripDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciLCoRoundTripDelay.setStatus("mandatory")


class _MpanlDlciLCoSetupPriority_Type(Unsigned32):
    """Custom type mpanlDlciLCoSetupPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_MpanlDlciLCoSetupPriority_Type.__name__ = "Unsigned32"
_MpanlDlciLCoSetupPriority_Object = MibTableColumn
mpanlDlciLCoSetupPriority = _MpanlDlciLCoSetupPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 4, 10, 1, 7),
    _MpanlDlciLCoSetupPriority_Type()
)
mpanlDlciLCoSetupPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciLCoSetupPriority.setStatus("mandatory")


class _MpanlDlciLCoHoldingPriority_Type(Unsigned32):
    """Custom type mpanlDlciLCoHoldingPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_MpanlDlciLCoHoldingPriority_Type.__name__ = "Unsigned32"
_MpanlDlciLCoHoldingPriority_Object = MibTableColumn
mpanlDlciLCoHoldingPriority = _MpanlDlciLCoHoldingPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 4, 10, 1, 8),
    _MpanlDlciLCoHoldingPriority_Type()
)
mpanlDlciLCoHoldingPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciLCoHoldingPriority.setStatus("mandatory")


class _MpanlDlciLCoRequiredTxBandwidth_Type(Gauge32):
    """Custom type mpanlDlciLCoRequiredTxBandwidth based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2048000),
    )


_MpanlDlciLCoRequiredTxBandwidth_Type.__name__ = "Gauge32"
_MpanlDlciLCoRequiredTxBandwidth_Object = MibTableColumn
mpanlDlciLCoRequiredTxBandwidth = _MpanlDlciLCoRequiredTxBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 4, 10, 1, 9),
    _MpanlDlciLCoRequiredTxBandwidth_Type()
)
mpanlDlciLCoRequiredTxBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciLCoRequiredTxBandwidth.setStatus("mandatory")


class _MpanlDlciLCoRequiredRxBandwidth_Type(Gauge32):
    """Custom type mpanlDlciLCoRequiredRxBandwidth based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2048000),
    )


_MpanlDlciLCoRequiredRxBandwidth_Type.__name__ = "Gauge32"
_MpanlDlciLCoRequiredRxBandwidth_Object = MibTableColumn
mpanlDlciLCoRequiredRxBandwidth = _MpanlDlciLCoRequiredRxBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 4, 10, 1, 10),
    _MpanlDlciLCoRequiredRxBandwidth_Type()
)
mpanlDlciLCoRequiredRxBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciLCoRequiredRxBandwidth.setStatus("mandatory")


class _MpanlDlciLCoRequiredTrafficType_Type(Integer32):
    """Custom type mpanlDlciLCoRequiredTrafficType based on Integer32"""
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


_MpanlDlciLCoRequiredTrafficType_Type.__name__ = "Integer32"
_MpanlDlciLCoRequiredTrafficType_Object = MibTableColumn
mpanlDlciLCoRequiredTrafficType = _MpanlDlciLCoRequiredTrafficType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 4, 10, 1, 11),
    _MpanlDlciLCoRequiredTrafficType_Type()
)
mpanlDlciLCoRequiredTrafficType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciLCoRequiredTrafficType.setStatus("mandatory")


class _MpanlDlciLCoPermittedTrunkTypes_Type(OctetString):
    """Custom type mpanlDlciLCoPermittedTrunkTypes based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MpanlDlciLCoPermittedTrunkTypes_Type.__name__ = "OctetString"
_MpanlDlciLCoPermittedTrunkTypes_Object = MibTableColumn
mpanlDlciLCoPermittedTrunkTypes = _MpanlDlciLCoPermittedTrunkTypes_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 4, 10, 1, 12),
    _MpanlDlciLCoPermittedTrunkTypes_Type()
)
mpanlDlciLCoPermittedTrunkTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciLCoPermittedTrunkTypes.setStatus("mandatory")


class _MpanlDlciLCoRequiredSecurity_Type(Unsigned32):
    """Custom type mpanlDlciLCoRequiredSecurity based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_MpanlDlciLCoRequiredSecurity_Type.__name__ = "Unsigned32"
_MpanlDlciLCoRequiredSecurity_Object = MibTableColumn
mpanlDlciLCoRequiredSecurity = _MpanlDlciLCoRequiredSecurity_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 4, 10, 1, 13),
    _MpanlDlciLCoRequiredSecurity_Type()
)
mpanlDlciLCoRequiredSecurity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciLCoRequiredSecurity.setStatus("mandatory")


class _MpanlDlciLCoRequiredCustomerParameter_Type(Unsigned32):
    """Custom type mpanlDlciLCoRequiredCustomerParameter based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_MpanlDlciLCoRequiredCustomerParameter_Type.__name__ = "Unsigned32"
_MpanlDlciLCoRequiredCustomerParameter_Object = MibTableColumn
mpanlDlciLCoRequiredCustomerParameter = _MpanlDlciLCoRequiredCustomerParameter_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 4, 10, 1, 14),
    _MpanlDlciLCoRequiredCustomerParameter_Type()
)
mpanlDlciLCoRequiredCustomerParameter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciLCoRequiredCustomerParameter.setStatus("mandatory")


class _MpanlDlciLCoEmissionPriority_Type(Unsigned32):
    """Custom type mpanlDlciLCoEmissionPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_MpanlDlciLCoEmissionPriority_Type.__name__ = "Unsigned32"
_MpanlDlciLCoEmissionPriority_Object = MibTableColumn
mpanlDlciLCoEmissionPriority = _MpanlDlciLCoEmissionPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 4, 10, 1, 15),
    _MpanlDlciLCoEmissionPriority_Type()
)
mpanlDlciLCoEmissionPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciLCoEmissionPriority.setStatus("mandatory")


class _MpanlDlciLCoDiscardPriority_Type(Unsigned32):
    """Custom type mpanlDlciLCoDiscardPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_MpanlDlciLCoDiscardPriority_Type.__name__ = "Unsigned32"
_MpanlDlciLCoDiscardPriority_Object = MibTableColumn
mpanlDlciLCoDiscardPriority = _MpanlDlciLCoDiscardPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 4, 10, 1, 16),
    _MpanlDlciLCoDiscardPriority_Type()
)
mpanlDlciLCoDiscardPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciLCoDiscardPriority.setStatus("mandatory")


class _MpanlDlciLCoRetryCount_Type(Unsigned32):
    """Custom type mpanlDlciLCoRetryCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MpanlDlciLCoRetryCount_Type.__name__ = "Unsigned32"
_MpanlDlciLCoRetryCount_Object = MibTableColumn
mpanlDlciLCoRetryCount = _MpanlDlciLCoRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 4, 10, 1, 18),
    _MpanlDlciLCoRetryCount_Type()
)
mpanlDlciLCoRetryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciLCoRetryCount.setStatus("mandatory")


class _MpanlDlciLCoPathFailureCount_Type(Unsigned32):
    """Custom type mpanlDlciLCoPathFailureCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MpanlDlciLCoPathFailureCount_Type.__name__ = "Unsigned32"
_MpanlDlciLCoPathFailureCount_Object = MibTableColumn
mpanlDlciLCoPathFailureCount = _MpanlDlciLCoPathFailureCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 4, 10, 1, 19),
    _MpanlDlciLCoPathFailureCount_Type()
)
mpanlDlciLCoPathFailureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciLCoPathFailureCount.setStatus("mandatory")


class _MpanlDlciLCoReasonForNoRoute_Type(Integer32):
    """Custom type mpanlDlciLCoReasonForNoRoute based on Integer32"""
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


_MpanlDlciLCoReasonForNoRoute_Type.__name__ = "Integer32"
_MpanlDlciLCoReasonForNoRoute_Object = MibTableColumn
mpanlDlciLCoReasonForNoRoute = _MpanlDlciLCoReasonForNoRoute_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 4, 10, 1, 20),
    _MpanlDlciLCoReasonForNoRoute_Type()
)
mpanlDlciLCoReasonForNoRoute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciLCoReasonForNoRoute.setStatus("mandatory")


class _MpanlDlciLCoLastTearDownReason_Type(Integer32):
    """Custom type mpanlDlciLCoLastTearDownReason based on Integer32"""
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


_MpanlDlciLCoLastTearDownReason_Type.__name__ = "Integer32"
_MpanlDlciLCoLastTearDownReason_Object = MibTableColumn
mpanlDlciLCoLastTearDownReason = _MpanlDlciLCoLastTearDownReason_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 4, 10, 1, 21),
    _MpanlDlciLCoLastTearDownReason_Type()
)
mpanlDlciLCoLastTearDownReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciLCoLastTearDownReason.setStatus("mandatory")


class _MpanlDlciLCoPathFailureAction_Type(Integer32):
    """Custom type mpanlDlciLCoPathFailureAction based on Integer32"""
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


_MpanlDlciLCoPathFailureAction_Type.__name__ = "Integer32"
_MpanlDlciLCoPathFailureAction_Object = MibTableColumn
mpanlDlciLCoPathFailureAction = _MpanlDlciLCoPathFailureAction_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 4, 10, 1, 22),
    _MpanlDlciLCoPathFailureAction_Type()
)
mpanlDlciLCoPathFailureAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciLCoPathFailureAction.setStatus("mandatory")


class _MpanlDlciLCoBumpPreference_Type(Integer32):
    """Custom type mpanlDlciLCoBumpPreference based on Integer32"""
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


_MpanlDlciLCoBumpPreference_Type.__name__ = "Integer32"
_MpanlDlciLCoBumpPreference_Object = MibTableColumn
mpanlDlciLCoBumpPreference = _MpanlDlciLCoBumpPreference_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 4, 10, 1, 23),
    _MpanlDlciLCoBumpPreference_Type()
)
mpanlDlciLCoBumpPreference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciLCoBumpPreference.setStatus("mandatory")


class _MpanlDlciLCoOptimization_Type(Integer32):
    """Custom type mpanlDlciLCoOptimization based on Integer32"""
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


_MpanlDlciLCoOptimization_Type.__name__ = "Integer32"
_MpanlDlciLCoOptimization_Object = MibTableColumn
mpanlDlciLCoOptimization = _MpanlDlciLCoOptimization_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 4, 10, 1, 24),
    _MpanlDlciLCoOptimization_Type()
)
mpanlDlciLCoOptimization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciLCoOptimization.setStatus("mandatory")


class _MpanlDlciLCoPathUpDateTime_Type(EnterpriseDateAndTime):
    """Custom type mpanlDlciLCoPathUpDateTime based on EnterpriseDateAndTime"""
    subtypeSpec = EnterpriseDateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(19, 19),
    )


_MpanlDlciLCoPathUpDateTime_Type.__name__ = "EnterpriseDateAndTime"
_MpanlDlciLCoPathUpDateTime_Object = MibTableColumn
mpanlDlciLCoPathUpDateTime = _MpanlDlciLCoPathUpDateTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 4, 10, 1, 25),
    _MpanlDlciLCoPathUpDateTime_Type()
)
mpanlDlciLCoPathUpDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciLCoPathUpDateTime.setStatus("mandatory")
_MpanlDlciLCoStatsTable_Object = MibTable
mpanlDlciLCoStatsTable = _MpanlDlciLCoStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 4, 11)
)
if mibBuilder.loadTexts:
    mpanlDlciLCoStatsTable.setStatus("mandatory")
_MpanlDlciLCoStatsEntry_Object = MibTableRow
mpanlDlciLCoStatsEntry = _MpanlDlciLCoStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 4, 11, 1)
)
mpanlDlciLCoStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-MpaNetworkLinkMIB", "mpanlIndex"),
    (0, "Nortel-Magellan-Passport-MpaNetworkLinkMIB", "mpanlDlciIndex"),
    (0, "Nortel-Magellan-Passport-MpaNetworkLinkMIB", "mpanlDlciLCoIndex"),
)
if mibBuilder.loadTexts:
    mpanlDlciLCoStatsEntry.setStatus("mandatory")
_MpanlDlciLCoPktsToNetwork_Type = PassportCounter64
_MpanlDlciLCoPktsToNetwork_Object = MibTableColumn
mpanlDlciLCoPktsToNetwork = _MpanlDlciLCoPktsToNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 4, 11, 1, 1),
    _MpanlDlciLCoPktsToNetwork_Type()
)
mpanlDlciLCoPktsToNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciLCoPktsToNetwork.setStatus("mandatory")
_MpanlDlciLCoBytesToNetwork_Type = PassportCounter64
_MpanlDlciLCoBytesToNetwork_Object = MibTableColumn
mpanlDlciLCoBytesToNetwork = _MpanlDlciLCoBytesToNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 4, 11, 1, 2),
    _MpanlDlciLCoBytesToNetwork_Type()
)
mpanlDlciLCoBytesToNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciLCoBytesToNetwork.setStatus("mandatory")
_MpanlDlciLCoPktsFromNetwork_Type = PassportCounter64
_MpanlDlciLCoPktsFromNetwork_Object = MibTableColumn
mpanlDlciLCoPktsFromNetwork = _MpanlDlciLCoPktsFromNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 4, 11, 1, 3),
    _MpanlDlciLCoPktsFromNetwork_Type()
)
mpanlDlciLCoPktsFromNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciLCoPktsFromNetwork.setStatus("mandatory")
_MpanlDlciLCoBytesFromNetwork_Type = PassportCounter64
_MpanlDlciLCoBytesFromNetwork_Object = MibTableColumn
mpanlDlciLCoBytesFromNetwork = _MpanlDlciLCoBytesFromNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 4, 11, 1, 4),
    _MpanlDlciLCoBytesFromNetwork_Type()
)
mpanlDlciLCoBytesFromNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciLCoBytesFromNetwork.setStatus("mandatory")
_MpanlDlciLCoCallDataTable_Object = MibTable
mpanlDlciLCoCallDataTable = _MpanlDlciLCoCallDataTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 4, 12)
)
if mibBuilder.loadTexts:
    mpanlDlciLCoCallDataTable.setStatus("mandatory")
_MpanlDlciLCoCallDataEntry_Object = MibTableRow
mpanlDlciLCoCallDataEntry = _MpanlDlciLCoCallDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 4, 12, 1)
)
mpanlDlciLCoCallDataEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-MpaNetworkLinkMIB", "mpanlIndex"),
    (0, "Nortel-Magellan-Passport-MpaNetworkLinkMIB", "mpanlDlciIndex"),
    (0, "Nortel-Magellan-Passport-MpaNetworkLinkMIB", "mpanlDlciLCoIndex"),
)
if mibBuilder.loadTexts:
    mpanlDlciLCoCallDataEntry.setStatus("mandatory")


class _MpanlDlciLCoCallingNpi_Type(Integer32):
    """Custom type mpanlDlciLCoCallingNpi based on Integer32"""
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


_MpanlDlciLCoCallingNpi_Type.__name__ = "Integer32"
_MpanlDlciLCoCallingNpi_Object = MibTableColumn
mpanlDlciLCoCallingNpi = _MpanlDlciLCoCallingNpi_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 4, 12, 1, 27),
    _MpanlDlciLCoCallingNpi_Type()
)
mpanlDlciLCoCallingNpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciLCoCallingNpi.setStatus("mandatory")


class _MpanlDlciLCoCallingDna_Type(DigitString):
    """Custom type mpanlDlciLCoCallingDna based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_MpanlDlciLCoCallingDna_Type.__name__ = "DigitString"
_MpanlDlciLCoCallingDna_Object = MibTableColumn
mpanlDlciLCoCallingDna = _MpanlDlciLCoCallingDna_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 4, 12, 1, 28),
    _MpanlDlciLCoCallingDna_Type()
)
mpanlDlciLCoCallingDna.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciLCoCallingDna.setStatus("mandatory")


class _MpanlDlciLCoElapsedTimeTillNow_Type(Unsigned32):
    """Custom type mpanlDlciLCoElapsedTimeTillNow based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_MpanlDlciLCoElapsedTimeTillNow_Type.__name__ = "Unsigned32"
_MpanlDlciLCoElapsedTimeTillNow_Object = MibTableColumn
mpanlDlciLCoElapsedTimeTillNow = _MpanlDlciLCoElapsedTimeTillNow_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 4, 12, 1, 30),
    _MpanlDlciLCoElapsedTimeTillNow_Type()
)
mpanlDlciLCoElapsedTimeTillNow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciLCoElapsedTimeTillNow.setStatus("mandatory")


class _MpanlDlciLCoCallReferenceNumber_Type(Hex):
    """Custom type mpanlDlciLCoCallReferenceNumber based on Hex"""
    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_MpanlDlciLCoCallReferenceNumber_Type.__name__ = "Hex"
_MpanlDlciLCoCallReferenceNumber_Object = MibTableColumn
mpanlDlciLCoCallReferenceNumber = _MpanlDlciLCoCallReferenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 4, 12, 1, 31),
    _MpanlDlciLCoCallReferenceNumber_Type()
)
mpanlDlciLCoCallReferenceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciLCoCallReferenceNumber.setStatus("mandatory")


class _MpanlDlciLCoCalledNpi_Type(Integer32):
    """Custom type mpanlDlciLCoCalledNpi based on Integer32"""
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


_MpanlDlciLCoCalledNpi_Type.__name__ = "Integer32"
_MpanlDlciLCoCalledNpi_Object = MibTableColumn
mpanlDlciLCoCalledNpi = _MpanlDlciLCoCalledNpi_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 4, 12, 1, 33),
    _MpanlDlciLCoCalledNpi_Type()
)
mpanlDlciLCoCalledNpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciLCoCalledNpi.setStatus("mandatory")


class _MpanlDlciLCoCalledDna_Type(DigitString):
    """Custom type mpanlDlciLCoCalledDna based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_MpanlDlciLCoCalledDna_Type.__name__ = "DigitString"
_MpanlDlciLCoCalledDna_Object = MibTableColumn
mpanlDlciLCoCalledDna = _MpanlDlciLCoCalledDna_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 4, 12, 1, 34),
    _MpanlDlciLCoCalledDna_Type()
)
mpanlDlciLCoCalledDna.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciLCoCalledDna.setStatus("mandatory")
_MpanlDlciLCoPathTable_Object = MibTable
mpanlDlciLCoPathTable = _MpanlDlciLCoPathTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 4, 401)
)
if mibBuilder.loadTexts:
    mpanlDlciLCoPathTable.setStatus("mandatory")
_MpanlDlciLCoPathEntry_Object = MibTableRow
mpanlDlciLCoPathEntry = _MpanlDlciLCoPathEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 4, 401, 1)
)
mpanlDlciLCoPathEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-MpaNetworkLinkMIB", "mpanlIndex"),
    (0, "Nortel-Magellan-Passport-MpaNetworkLinkMIB", "mpanlDlciIndex"),
    (0, "Nortel-Magellan-Passport-MpaNetworkLinkMIB", "mpanlDlciLCoIndex"),
    (0, "Nortel-Magellan-Passport-MpaNetworkLinkMIB", "mpanlDlciLCoPathValue"),
)
if mibBuilder.loadTexts:
    mpanlDlciLCoPathEntry.setStatus("mandatory")


class _MpanlDlciLCoPathValue_Type(AsciiString):
    """Custom type mpanlDlciLCoPathValue based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_MpanlDlciLCoPathValue_Type.__name__ = "AsciiString"
_MpanlDlciLCoPathValue_Object = MibTableColumn
mpanlDlciLCoPathValue = _MpanlDlciLCoPathValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 4, 401, 1, 1),
    _MpanlDlciLCoPathValue_Type()
)
mpanlDlciLCoPathValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciLCoPathValue.setStatus("mandatory")
_MpanlDlciJvc_ObjectIdentity = ObjectIdentity
mpanlDlciJvc = _MpanlDlciJvc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 5)
)
_MpanlDlciJvcRowStatusTable_Object = MibTable
mpanlDlciJvcRowStatusTable = _MpanlDlciJvcRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 5, 1)
)
if mibBuilder.loadTexts:
    mpanlDlciJvcRowStatusTable.setStatus("mandatory")
_MpanlDlciJvcRowStatusEntry_Object = MibTableRow
mpanlDlciJvcRowStatusEntry = _MpanlDlciJvcRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 5, 1, 1)
)
mpanlDlciJvcRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-MpaNetworkLinkMIB", "mpanlIndex"),
    (0, "Nortel-Magellan-Passport-MpaNetworkLinkMIB", "mpanlDlciIndex"),
    (0, "Nortel-Magellan-Passport-MpaNetworkLinkMIB", "mpanlDlciJvcIndex"),
)
if mibBuilder.loadTexts:
    mpanlDlciJvcRowStatusEntry.setStatus("mandatory")
_MpanlDlciJvcRowStatus_Type = RowStatus
_MpanlDlciJvcRowStatus_Object = MibTableColumn
mpanlDlciJvcRowStatus = _MpanlDlciJvcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 5, 1, 1, 1),
    _MpanlDlciJvcRowStatus_Type()
)
mpanlDlciJvcRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciJvcRowStatus.setStatus("mandatory")
_MpanlDlciJvcComponentName_Type = DisplayString
_MpanlDlciJvcComponentName_Object = MibTableColumn
mpanlDlciJvcComponentName = _MpanlDlciJvcComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 5, 1, 1, 2),
    _MpanlDlciJvcComponentName_Type()
)
mpanlDlciJvcComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciJvcComponentName.setStatus("mandatory")
_MpanlDlciJvcStorageType_Type = StorageType
_MpanlDlciJvcStorageType_Object = MibTableColumn
mpanlDlciJvcStorageType = _MpanlDlciJvcStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 5, 1, 1, 4),
    _MpanlDlciJvcStorageType_Type()
)
mpanlDlciJvcStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciJvcStorageType.setStatus("mandatory")
_MpanlDlciJvcIndex_Type = NonReplicated
_MpanlDlciJvcIndex_Object = MibTableColumn
mpanlDlciJvcIndex = _MpanlDlciJvcIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 5, 1, 1, 10),
    _MpanlDlciJvcIndex_Type()
)
mpanlDlciJvcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mpanlDlciJvcIndex.setStatus("mandatory")
_MpanlDlciJvcOperTable_Object = MibTable
mpanlDlciJvcOperTable = _MpanlDlciJvcOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 5, 10)
)
if mibBuilder.loadTexts:
    mpanlDlciJvcOperTable.setStatus("mandatory")
_MpanlDlciJvcOperEntry_Object = MibTableRow
mpanlDlciJvcOperEntry = _MpanlDlciJvcOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 5, 10, 1)
)
mpanlDlciJvcOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-MpaNetworkLinkMIB", "mpanlIndex"),
    (0, "Nortel-Magellan-Passport-MpaNetworkLinkMIB", "mpanlDlciIndex"),
    (0, "Nortel-Magellan-Passport-MpaNetworkLinkMIB", "mpanlDlciJvcIndex"),
)
if mibBuilder.loadTexts:
    mpanlDlciJvcOperEntry.setStatus("mandatory")


class _MpanlDlciJvcCurrentState_Type(Integer32):
    """Custom type mpanlDlciJvcCurrentState based on Integer32"""
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


_MpanlDlciJvcCurrentState_Type.__name__ = "Integer32"
_MpanlDlciJvcCurrentState_Object = MibTableColumn
mpanlDlciJvcCurrentState = _MpanlDlciJvcCurrentState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 5, 10, 1, 1),
    _MpanlDlciJvcCurrentState_Type()
)
mpanlDlciJvcCurrentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciJvcCurrentState.setStatus("mandatory")


class _MpanlDlciJvcPreviousState_Type(Integer32):
    """Custom type mpanlDlciJvcPreviousState based on Integer32"""
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


_MpanlDlciJvcPreviousState_Type.__name__ = "Integer32"
_MpanlDlciJvcPreviousState_Object = MibTableColumn
mpanlDlciJvcPreviousState = _MpanlDlciJvcPreviousState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 5, 10, 1, 2),
    _MpanlDlciJvcPreviousState_Type()
)
mpanlDlciJvcPreviousState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciJvcPreviousState.setStatus("mandatory")


class _MpanlDlciJvcCallingNpi_Type(Integer32):
    """Custom type mpanlDlciJvcCallingNpi based on Integer32"""
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


_MpanlDlciJvcCallingNpi_Type.__name__ = "Integer32"
_MpanlDlciJvcCallingNpi_Object = MibTableColumn
mpanlDlciJvcCallingNpi = _MpanlDlciJvcCallingNpi_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 5, 10, 1, 6),
    _MpanlDlciJvcCallingNpi_Type()
)
mpanlDlciJvcCallingNpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciJvcCallingNpi.setStatus("mandatory")


class _MpanlDlciJvcCallingAddress_Type(DigitString):
    """Custom type mpanlDlciJvcCallingAddress based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_MpanlDlciJvcCallingAddress_Type.__name__ = "DigitString"
_MpanlDlciJvcCallingAddress_Object = MibTableColumn
mpanlDlciJvcCallingAddress = _MpanlDlciJvcCallingAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 5, 10, 1, 7),
    _MpanlDlciJvcCallingAddress_Type()
)
mpanlDlciJvcCallingAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciJvcCallingAddress.setStatus("mandatory")


class _MpanlDlciJvcCallingLcn_Type(Unsigned32):
    """Custom type mpanlDlciJvcCallingLcn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_MpanlDlciJvcCallingLcn_Type.__name__ = "Unsigned32"
_MpanlDlciJvcCallingLcn_Object = MibTableColumn
mpanlDlciJvcCallingLcn = _MpanlDlciJvcCallingLcn_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 5, 10, 1, 8),
    _MpanlDlciJvcCallingLcn_Type()
)
mpanlDlciJvcCallingLcn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciJvcCallingLcn.setStatus("mandatory")


class _MpanlDlciJvcCalledNpi_Type(Integer32):
    """Custom type mpanlDlciJvcCalledNpi based on Integer32"""
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


_MpanlDlciJvcCalledNpi_Type.__name__ = "Integer32"
_MpanlDlciJvcCalledNpi_Object = MibTableColumn
mpanlDlciJvcCalledNpi = _MpanlDlciJvcCalledNpi_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 5, 10, 1, 9),
    _MpanlDlciJvcCalledNpi_Type()
)
mpanlDlciJvcCalledNpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciJvcCalledNpi.setStatus("mandatory")


class _MpanlDlciJvcCalledAddress_Type(DigitString):
    """Custom type mpanlDlciJvcCalledAddress based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_MpanlDlciJvcCalledAddress_Type.__name__ = "DigitString"
_MpanlDlciJvcCalledAddress_Object = MibTableColumn
mpanlDlciJvcCalledAddress = _MpanlDlciJvcCalledAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 5, 10, 1, 10),
    _MpanlDlciJvcCalledAddress_Type()
)
mpanlDlciJvcCalledAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciJvcCalledAddress.setStatus("mandatory")


class _MpanlDlciJvcCalledLcn_Type(Unsigned32):
    """Custom type mpanlDlciJvcCalledLcn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_MpanlDlciJvcCalledLcn_Type.__name__ = "Unsigned32"
_MpanlDlciJvcCalledLcn_Object = MibTableColumn
mpanlDlciJvcCalledLcn = _MpanlDlciJvcCalledLcn_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 5, 10, 1, 11),
    _MpanlDlciJvcCalledLcn_Type()
)
mpanlDlciJvcCalledLcn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciJvcCalledLcn.setStatus("mandatory")
_MpanlDlciJvcStatTable_Object = MibTable
mpanlDlciJvcStatTable = _MpanlDlciJvcStatTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 5, 11)
)
if mibBuilder.loadTexts:
    mpanlDlciJvcStatTable.setStatus("mandatory")
_MpanlDlciJvcStatEntry_Object = MibTableRow
mpanlDlciJvcStatEntry = _MpanlDlciJvcStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 5, 11, 1)
)
mpanlDlciJvcStatEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-MpaNetworkLinkMIB", "mpanlIndex"),
    (0, "Nortel-Magellan-Passport-MpaNetworkLinkMIB", "mpanlDlciIndex"),
    (0, "Nortel-Magellan-Passport-MpaNetworkLinkMIB", "mpanlDlciJvcIndex"),
)
if mibBuilder.loadTexts:
    mpanlDlciJvcStatEntry.setStatus("mandatory")


class _MpanlDlciJvcPacketsFromSubnet_Type(Unsigned32):
    """Custom type mpanlDlciJvcPacketsFromSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MpanlDlciJvcPacketsFromSubnet_Type.__name__ = "Unsigned32"
_MpanlDlciJvcPacketsFromSubnet_Object = MibTableColumn
mpanlDlciJvcPacketsFromSubnet = _MpanlDlciJvcPacketsFromSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 5, 11, 1, 1),
    _MpanlDlciJvcPacketsFromSubnet_Type()
)
mpanlDlciJvcPacketsFromSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciJvcPacketsFromSubnet.setStatus("mandatory")


class _MpanlDlciJvcPacketsToSubnet_Type(Unsigned32):
    """Custom type mpanlDlciJvcPacketsToSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MpanlDlciJvcPacketsToSubnet_Type.__name__ = "Unsigned32"
_MpanlDlciJvcPacketsToSubnet_Object = MibTableColumn
mpanlDlciJvcPacketsToSubnet = _MpanlDlciJvcPacketsToSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 5, 11, 1, 2),
    _MpanlDlciJvcPacketsToSubnet_Type()
)
mpanlDlciJvcPacketsToSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciJvcPacketsToSubnet.setStatus("mandatory")


class _MpanlDlciJvcPacketsDiscarded_Type(Unsigned32):
    """Custom type mpanlDlciJvcPacketsDiscarded based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MpanlDlciJvcPacketsDiscarded_Type.__name__ = "Unsigned32"
_MpanlDlciJvcPacketsDiscarded_Object = MibTableColumn
mpanlDlciJvcPacketsDiscarded = _MpanlDlciJvcPacketsDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 5, 11, 1, 3),
    _MpanlDlciJvcPacketsDiscarded_Type()
)
mpanlDlciJvcPacketsDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciJvcPacketsDiscarded.setStatus("mandatory")


class _MpanlDlciJvcProtocolErrors_Type(Unsigned32):
    """Custom type mpanlDlciJvcProtocolErrors based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MpanlDlciJvcProtocolErrors_Type.__name__ = "Unsigned32"
_MpanlDlciJvcProtocolErrors_Object = MibTableColumn
mpanlDlciJvcProtocolErrors = _MpanlDlciJvcProtocolErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 5, 11, 1, 4),
    _MpanlDlciJvcProtocolErrors_Type()
)
mpanlDlciJvcProtocolErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciJvcProtocolErrors.setStatus("mandatory")
_MpanlDlciStateTable_Object = MibTable
mpanlDlciStateTable = _MpanlDlciStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 10)
)
if mibBuilder.loadTexts:
    mpanlDlciStateTable.setStatus("mandatory")
_MpanlDlciStateEntry_Object = MibTableRow
mpanlDlciStateEntry = _MpanlDlciStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 10, 1)
)
mpanlDlciStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-MpaNetworkLinkMIB", "mpanlIndex"),
    (0, "Nortel-Magellan-Passport-MpaNetworkLinkMIB", "mpanlDlciIndex"),
)
if mibBuilder.loadTexts:
    mpanlDlciStateEntry.setStatus("mandatory")


class _MpanlDlciAdminState_Type(Integer32):
    """Custom type mpanlDlciAdminState based on Integer32"""
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


_MpanlDlciAdminState_Type.__name__ = "Integer32"
_MpanlDlciAdminState_Object = MibTableColumn
mpanlDlciAdminState = _MpanlDlciAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 10, 1, 1),
    _MpanlDlciAdminState_Type()
)
mpanlDlciAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciAdminState.setStatus("mandatory")


class _MpanlDlciOperationalState_Type(Integer32):
    """Custom type mpanlDlciOperationalState based on Integer32"""
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


_MpanlDlciOperationalState_Type.__name__ = "Integer32"
_MpanlDlciOperationalState_Object = MibTableColumn
mpanlDlciOperationalState = _MpanlDlciOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 10, 1, 2),
    _MpanlDlciOperationalState_Type()
)
mpanlDlciOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciOperationalState.setStatus("mandatory")


class _MpanlDlciUsageState_Type(Integer32):
    """Custom type mpanlDlciUsageState based on Integer32"""
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


_MpanlDlciUsageState_Type.__name__ = "Integer32"
_MpanlDlciUsageState_Object = MibTableColumn
mpanlDlciUsageState = _MpanlDlciUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 10, 1, 3),
    _MpanlDlciUsageState_Type()
)
mpanlDlciUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciUsageState.setStatus("mandatory")


class _MpanlDlciAvailabilityStatus_Type(OctetString):
    """Custom type mpanlDlciAvailabilityStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_MpanlDlciAvailabilityStatus_Type.__name__ = "OctetString"
_MpanlDlciAvailabilityStatus_Object = MibTableColumn
mpanlDlciAvailabilityStatus = _MpanlDlciAvailabilityStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 10, 1, 4),
    _MpanlDlciAvailabilityStatus_Type()
)
mpanlDlciAvailabilityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciAvailabilityStatus.setStatus("mandatory")


class _MpanlDlciProceduralStatus_Type(OctetString):
    """Custom type mpanlDlciProceduralStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MpanlDlciProceduralStatus_Type.__name__ = "OctetString"
_MpanlDlciProceduralStatus_Object = MibTableColumn
mpanlDlciProceduralStatus = _MpanlDlciProceduralStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 10, 1, 5),
    _MpanlDlciProceduralStatus_Type()
)
mpanlDlciProceduralStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciProceduralStatus.setStatus("mandatory")


class _MpanlDlciControlStatus_Type(OctetString):
    """Custom type mpanlDlciControlStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MpanlDlciControlStatus_Type.__name__ = "OctetString"
_MpanlDlciControlStatus_Object = MibTableColumn
mpanlDlciControlStatus = _MpanlDlciControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 10, 1, 6),
    _MpanlDlciControlStatus_Type()
)
mpanlDlciControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciControlStatus.setStatus("mandatory")


class _MpanlDlciAlarmStatus_Type(OctetString):
    """Custom type mpanlDlciAlarmStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MpanlDlciAlarmStatus_Type.__name__ = "OctetString"
_MpanlDlciAlarmStatus_Object = MibTableColumn
mpanlDlciAlarmStatus = _MpanlDlciAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 10, 1, 7),
    _MpanlDlciAlarmStatus_Type()
)
mpanlDlciAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciAlarmStatus.setStatus("mandatory")


class _MpanlDlciStandbyStatus_Type(Integer32):
    """Custom type mpanlDlciStandbyStatus based on Integer32"""
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


_MpanlDlciStandbyStatus_Type.__name__ = "Integer32"
_MpanlDlciStandbyStatus_Object = MibTableColumn
mpanlDlciStandbyStatus = _MpanlDlciStandbyStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 10, 1, 8),
    _MpanlDlciStandbyStatus_Type()
)
mpanlDlciStandbyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciStandbyStatus.setStatus("mandatory")


class _MpanlDlciUnknownStatus_Type(Integer32):
    """Custom type mpanlDlciUnknownStatus based on Integer32"""
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


_MpanlDlciUnknownStatus_Type.__name__ = "Integer32"
_MpanlDlciUnknownStatus_Object = MibTableColumn
mpanlDlciUnknownStatus = _MpanlDlciUnknownStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 10, 1, 9),
    _MpanlDlciUnknownStatus_Type()
)
mpanlDlciUnknownStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciUnknownStatus.setStatus("mandatory")
_MpanlDlciCalldTable_Object = MibTable
mpanlDlciCalldTable = _MpanlDlciCalldTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 11)
)
if mibBuilder.loadTexts:
    mpanlDlciCalldTable.setStatus("mandatory")
_MpanlDlciCalldEntry_Object = MibTableRow
mpanlDlciCalldEntry = _MpanlDlciCalldEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 11, 1)
)
mpanlDlciCalldEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-MpaNetworkLinkMIB", "mpanlIndex"),
    (0, "Nortel-Magellan-Passport-MpaNetworkLinkMIB", "mpanlDlciIndex"),
)
if mibBuilder.loadTexts:
    mpanlDlciCalldEntry.setStatus("mandatory")


class _MpanlDlciQ933CallState_Type(Integer32):
    """Custom type mpanlDlciQ933CallState based on Integer32"""
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


_MpanlDlciQ933CallState_Type.__name__ = "Integer32"
_MpanlDlciQ933CallState_Object = MibTableColumn
mpanlDlciQ933CallState = _MpanlDlciQ933CallState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 11, 1, 2),
    _MpanlDlciQ933CallState_Type()
)
mpanlDlciQ933CallState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciQ933CallState.setStatus("mandatory")


class _MpanlDlciQ933CallReference_Type(Unsigned32):
    """Custom type mpanlDlciQ933CallReference based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_MpanlDlciQ933CallReference_Type.__name__ = "Unsigned32"
_MpanlDlciQ933CallReference_Object = MibTableColumn
mpanlDlciQ933CallReference = _MpanlDlciQ933CallReference_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 11, 1, 3),
    _MpanlDlciQ933CallReference_Type()
)
mpanlDlciQ933CallReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciQ933CallReference.setStatus("mandatory")
_MpanlDlciSpOpTable_Object = MibTable
mpanlDlciSpOpTable = _MpanlDlciSpOpTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 12)
)
if mibBuilder.loadTexts:
    mpanlDlciSpOpTable.setStatus("mandatory")
_MpanlDlciSpOpEntry_Object = MibTableRow
mpanlDlciSpOpEntry = _MpanlDlciSpOpEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 12, 1)
)
mpanlDlciSpOpEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-MpaNetworkLinkMIB", "mpanlIndex"),
    (0, "Nortel-Magellan-Passport-MpaNetworkLinkMIB", "mpanlDlciIndex"),
)
if mibBuilder.loadTexts:
    mpanlDlciSpOpEntry.setStatus("mandatory")


class _MpanlDlciMaximumFrameSize_Type(Unsigned32):
    """Custom type mpanlDlciMaximumFrameSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_MpanlDlciMaximumFrameSize_Type.__name__ = "Unsigned32"
_MpanlDlciMaximumFrameSize_Object = MibTableColumn
mpanlDlciMaximumFrameSize = _MpanlDlciMaximumFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 12, 1, 1),
    _MpanlDlciMaximumFrameSize_Type()
)
mpanlDlciMaximumFrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciMaximumFrameSize.setStatus("mandatory")


class _MpanlDlciCommittedBurstSize_Type(Unsigned32):
    """Custom type mpanlDlciCommittedBurstSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50000000),
    )


_MpanlDlciCommittedBurstSize_Type.__name__ = "Unsigned32"
_MpanlDlciCommittedBurstSize_Object = MibTableColumn
mpanlDlciCommittedBurstSize = _MpanlDlciCommittedBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 12, 1, 4),
    _MpanlDlciCommittedBurstSize_Type()
)
mpanlDlciCommittedBurstSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciCommittedBurstSize.setStatus("mandatory")


class _MpanlDlciExcessBurstSize_Type(Unsigned32):
    """Custom type mpanlDlciExcessBurstSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50000000),
    )


_MpanlDlciExcessBurstSize_Type.__name__ = "Unsigned32"
_MpanlDlciExcessBurstSize_Object = MibTableColumn
mpanlDlciExcessBurstSize = _MpanlDlciExcessBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 12, 1, 5),
    _MpanlDlciExcessBurstSize_Type()
)
mpanlDlciExcessBurstSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciExcessBurstSize.setStatus("mandatory")


class _MpanlDlciAccounting_Type(Integer32):
    """Custom type mpanlDlciAccounting based on Integer32"""
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


_MpanlDlciAccounting_Type.__name__ = "Integer32"
_MpanlDlciAccounting_Object = MibTableColumn
mpanlDlciAccounting = _MpanlDlciAccounting_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 12, 1, 8),
    _MpanlDlciAccounting_Type()
)
mpanlDlciAccounting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciAccounting.setStatus("mandatory")


class _MpanlDlciEmissionPriorityToIf_Type(Integer32):
    """Custom type mpanlDlciEmissionPriorityToIf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
        ValueRangeConstraint(3, 3),
    )


_MpanlDlciEmissionPriorityToIf_Type.__name__ = "Integer32"
_MpanlDlciEmissionPriorityToIf_Object = MibTableColumn
mpanlDlciEmissionPriorityToIf = _MpanlDlciEmissionPriorityToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 12, 1, 9),
    _MpanlDlciEmissionPriorityToIf_Type()
)
mpanlDlciEmissionPriorityToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciEmissionPriorityToIf.setStatus("mandatory")


class _MpanlDlciTransferPriToNwk_Type(Unsigned32):
    """Custom type mpanlDlciTransferPriToNwk based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_MpanlDlciTransferPriToNwk_Type.__name__ = "Unsigned32"
_MpanlDlciTransferPriToNwk_Object = MibTableColumn
mpanlDlciTransferPriToNwk = _MpanlDlciTransferPriToNwk_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 12, 1, 10),
    _MpanlDlciTransferPriToNwk_Type()
)
mpanlDlciTransferPriToNwk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciTransferPriToNwk.setStatus("mandatory")


class _MpanlDlciTransferPriFromNwk_Type(Unsigned32):
    """Custom type mpanlDlciTransferPriFromNwk based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_MpanlDlciTransferPriFromNwk_Type.__name__ = "Unsigned32"
_MpanlDlciTransferPriFromNwk_Object = MibTableColumn
mpanlDlciTransferPriFromNwk = _MpanlDlciTransferPriFromNwk_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 12, 1, 11),
    _MpanlDlciTransferPriFromNwk_Type()
)
mpanlDlciTransferPriFromNwk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciTransferPriFromNwk.setStatus("mandatory")
_MpanlDlciStatsTable_Object = MibTable
mpanlDlciStatsTable = _MpanlDlciStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 13)
)
if mibBuilder.loadTexts:
    mpanlDlciStatsTable.setStatus("mandatory")
_MpanlDlciStatsEntry_Object = MibTableRow
mpanlDlciStatsEntry = _MpanlDlciStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 13, 1)
)
mpanlDlciStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-MpaNetworkLinkMIB", "mpanlIndex"),
    (0, "Nortel-Magellan-Passport-MpaNetworkLinkMIB", "mpanlDlciIndex"),
)
if mibBuilder.loadTexts:
    mpanlDlciStatsEntry.setStatus("mandatory")


class _MpanlDlciFrmToIf_Type(Unsigned32):
    """Custom type mpanlDlciFrmToIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MpanlDlciFrmToIf_Type.__name__ = "Unsigned32"
_MpanlDlciFrmToIf_Object = MibTableColumn
mpanlDlciFrmToIf = _MpanlDlciFrmToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 13, 1, 1),
    _MpanlDlciFrmToIf_Type()
)
mpanlDlciFrmToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciFrmToIf.setStatus("mandatory")


class _MpanlDlciFecnFrmToIf_Type(Unsigned32):
    """Custom type mpanlDlciFecnFrmToIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MpanlDlciFecnFrmToIf_Type.__name__ = "Unsigned32"
_MpanlDlciFecnFrmToIf_Object = MibTableColumn
mpanlDlciFecnFrmToIf = _MpanlDlciFecnFrmToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 13, 1, 2),
    _MpanlDlciFecnFrmToIf_Type()
)
mpanlDlciFecnFrmToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciFecnFrmToIf.setStatus("mandatory")


class _MpanlDlciBecnFrmToIf_Type(Unsigned32):
    """Custom type mpanlDlciBecnFrmToIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MpanlDlciBecnFrmToIf_Type.__name__ = "Unsigned32"
_MpanlDlciBecnFrmToIf_Object = MibTableColumn
mpanlDlciBecnFrmToIf = _MpanlDlciBecnFrmToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 13, 1, 3),
    _MpanlDlciBecnFrmToIf_Type()
)
mpanlDlciBecnFrmToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciBecnFrmToIf.setStatus("mandatory")


class _MpanlDlciBciToSubnet_Type(Unsigned32):
    """Custom type mpanlDlciBciToSubnet based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MpanlDlciBciToSubnet_Type.__name__ = "Unsigned32"
_MpanlDlciBciToSubnet_Object = MibTableColumn
mpanlDlciBciToSubnet = _MpanlDlciBciToSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 13, 1, 4),
    _MpanlDlciBciToSubnet_Type()
)
mpanlDlciBciToSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciBciToSubnet.setStatus("mandatory")


class _MpanlDlciDeFrmToIf_Type(Unsigned32):
    """Custom type mpanlDlciDeFrmToIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MpanlDlciDeFrmToIf_Type.__name__ = "Unsigned32"
_MpanlDlciDeFrmToIf_Object = MibTableColumn
mpanlDlciDeFrmToIf = _MpanlDlciDeFrmToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 13, 1, 5),
    _MpanlDlciDeFrmToIf_Type()
)
mpanlDlciDeFrmToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciDeFrmToIf.setStatus("mandatory")


class _MpanlDlciDiscCongestedToIf_Type(Unsigned32):
    """Custom type mpanlDlciDiscCongestedToIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MpanlDlciDiscCongestedToIf_Type.__name__ = "Unsigned32"
_MpanlDlciDiscCongestedToIf_Object = MibTableColumn
mpanlDlciDiscCongestedToIf = _MpanlDlciDiscCongestedToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 13, 1, 6),
    _MpanlDlciDiscCongestedToIf_Type()
)
mpanlDlciDiscCongestedToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciDiscCongestedToIf.setStatus("mandatory")


class _MpanlDlciDiscDeCongestedToIf_Type(Unsigned32):
    """Custom type mpanlDlciDiscDeCongestedToIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MpanlDlciDiscDeCongestedToIf_Type.__name__ = "Unsigned32"
_MpanlDlciDiscDeCongestedToIf_Object = MibTableColumn
mpanlDlciDiscDeCongestedToIf = _MpanlDlciDiscDeCongestedToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 13, 1, 7),
    _MpanlDlciDiscDeCongestedToIf_Type()
)
mpanlDlciDiscDeCongestedToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciDiscDeCongestedToIf.setStatus("mandatory")


class _MpanlDlciFrmFromIf_Type(Unsigned32):
    """Custom type mpanlDlciFrmFromIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MpanlDlciFrmFromIf_Type.__name__ = "Unsigned32"
_MpanlDlciFrmFromIf_Object = MibTableColumn
mpanlDlciFrmFromIf = _MpanlDlciFrmFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 13, 1, 8),
    _MpanlDlciFrmFromIf_Type()
)
mpanlDlciFrmFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciFrmFromIf.setStatus("mandatory")


class _MpanlDlciFecnFrmFromIf_Type(Unsigned32):
    """Custom type mpanlDlciFecnFrmFromIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MpanlDlciFecnFrmFromIf_Type.__name__ = "Unsigned32"
_MpanlDlciFecnFrmFromIf_Object = MibTableColumn
mpanlDlciFecnFrmFromIf = _MpanlDlciFecnFrmFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 13, 1, 9),
    _MpanlDlciFecnFrmFromIf_Type()
)
mpanlDlciFecnFrmFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciFecnFrmFromIf.setStatus("mandatory")


class _MpanlDlciBecnFrmFromIf_Type(Unsigned32):
    """Custom type mpanlDlciBecnFrmFromIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MpanlDlciBecnFrmFromIf_Type.__name__ = "Unsigned32"
_MpanlDlciBecnFrmFromIf_Object = MibTableColumn
mpanlDlciBecnFrmFromIf = _MpanlDlciBecnFrmFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 13, 1, 10),
    _MpanlDlciBecnFrmFromIf_Type()
)
mpanlDlciBecnFrmFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciBecnFrmFromIf.setStatus("mandatory")


class _MpanlDlciFciFromSubnet_Type(Unsigned32):
    """Custom type mpanlDlciFciFromSubnet based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MpanlDlciFciFromSubnet_Type.__name__ = "Unsigned32"
_MpanlDlciFciFromSubnet_Object = MibTableColumn
mpanlDlciFciFromSubnet = _MpanlDlciFciFromSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 13, 1, 11),
    _MpanlDlciFciFromSubnet_Type()
)
mpanlDlciFciFromSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciFciFromSubnet.setStatus("mandatory")


class _MpanlDlciBciFromSubnet_Type(Unsigned32):
    """Custom type mpanlDlciBciFromSubnet based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MpanlDlciBciFromSubnet_Type.__name__ = "Unsigned32"
_MpanlDlciBciFromSubnet_Object = MibTableColumn
mpanlDlciBciFromSubnet = _MpanlDlciBciFromSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 13, 1, 12),
    _MpanlDlciBciFromSubnet_Type()
)
mpanlDlciBciFromSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciBciFromSubnet.setStatus("mandatory")


class _MpanlDlciDeFrmFromIf_Type(Unsigned32):
    """Custom type mpanlDlciDeFrmFromIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MpanlDlciDeFrmFromIf_Type.__name__ = "Unsigned32"
_MpanlDlciDeFrmFromIf_Object = MibTableColumn
mpanlDlciDeFrmFromIf = _MpanlDlciDeFrmFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 13, 1, 13),
    _MpanlDlciDeFrmFromIf_Type()
)
mpanlDlciDeFrmFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciDeFrmFromIf.setStatus("mandatory")


class _MpanlDlciExcessFrmFromIf_Type(Unsigned32):
    """Custom type mpanlDlciExcessFrmFromIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MpanlDlciExcessFrmFromIf_Type.__name__ = "Unsigned32"
_MpanlDlciExcessFrmFromIf_Object = MibTableColumn
mpanlDlciExcessFrmFromIf = _MpanlDlciExcessFrmFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 13, 1, 14),
    _MpanlDlciExcessFrmFromIf_Type()
)
mpanlDlciExcessFrmFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciExcessFrmFromIf.setStatus("mandatory")


class _MpanlDlciDiscExcessFromIf_Type(Unsigned32):
    """Custom type mpanlDlciDiscExcessFromIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MpanlDlciDiscExcessFromIf_Type.__name__ = "Unsigned32"
_MpanlDlciDiscExcessFromIf_Object = MibTableColumn
mpanlDlciDiscExcessFromIf = _MpanlDlciDiscExcessFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 13, 1, 15),
    _MpanlDlciDiscExcessFromIf_Type()
)
mpanlDlciDiscExcessFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciDiscExcessFromIf.setStatus("mandatory")


class _MpanlDlciDiscFrameAbit_Type(Unsigned32):
    """Custom type mpanlDlciDiscFrameAbit based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MpanlDlciDiscFrameAbit_Type.__name__ = "Unsigned32"
_MpanlDlciDiscFrameAbit_Object = MibTableColumn
mpanlDlciDiscFrameAbit = _MpanlDlciDiscFrameAbit_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 13, 1, 16),
    _MpanlDlciDiscFrameAbit_Type()
)
mpanlDlciDiscFrameAbit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciDiscFrameAbit.setStatus("mandatory")


class _MpanlDlciDiscCongestedFromIf_Type(Unsigned32):
    """Custom type mpanlDlciDiscCongestedFromIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MpanlDlciDiscCongestedFromIf_Type.__name__ = "Unsigned32"
_MpanlDlciDiscCongestedFromIf_Object = MibTableColumn
mpanlDlciDiscCongestedFromIf = _MpanlDlciDiscCongestedFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 13, 1, 17),
    _MpanlDlciDiscCongestedFromIf_Type()
)
mpanlDlciDiscCongestedFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciDiscCongestedFromIf.setStatus("mandatory")


class _MpanlDlciDiscDeCongestedFromIf_Type(Unsigned32):
    """Custom type mpanlDlciDiscDeCongestedFromIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MpanlDlciDiscDeCongestedFromIf_Type.__name__ = "Unsigned32"
_MpanlDlciDiscDeCongestedFromIf_Object = MibTableColumn
mpanlDlciDiscDeCongestedFromIf = _MpanlDlciDiscDeCongestedFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 13, 1, 18),
    _MpanlDlciDiscDeCongestedFromIf_Type()
)
mpanlDlciDiscDeCongestedFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciDiscDeCongestedFromIf.setStatus("mandatory")


class _MpanlDlciErrorShortFrmFromIf_Type(Unsigned32):
    """Custom type mpanlDlciErrorShortFrmFromIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MpanlDlciErrorShortFrmFromIf_Type.__name__ = "Unsigned32"
_MpanlDlciErrorShortFrmFromIf_Object = MibTableColumn
mpanlDlciErrorShortFrmFromIf = _MpanlDlciErrorShortFrmFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 13, 1, 19),
    _MpanlDlciErrorShortFrmFromIf_Type()
)
mpanlDlciErrorShortFrmFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciErrorShortFrmFromIf.setStatus("mandatory")


class _MpanlDlciErrorLongFrmFromIf_Type(Unsigned32):
    """Custom type mpanlDlciErrorLongFrmFromIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MpanlDlciErrorLongFrmFromIf_Type.__name__ = "Unsigned32"
_MpanlDlciErrorLongFrmFromIf_Object = MibTableColumn
mpanlDlciErrorLongFrmFromIf = _MpanlDlciErrorLongFrmFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 13, 1, 20),
    _MpanlDlciErrorLongFrmFromIf_Type()
)
mpanlDlciErrorLongFrmFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciErrorLongFrmFromIf.setStatus("mandatory")


class _MpanlDlciBecnFrmSetByService_Type(Unsigned32):
    """Custom type mpanlDlciBecnFrmSetByService based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MpanlDlciBecnFrmSetByService_Type.__name__ = "Unsigned32"
_MpanlDlciBecnFrmSetByService_Object = MibTableColumn
mpanlDlciBecnFrmSetByService = _MpanlDlciBecnFrmSetByService_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 13, 1, 21),
    _MpanlDlciBecnFrmSetByService_Type()
)
mpanlDlciBecnFrmSetByService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciBecnFrmSetByService.setStatus("mandatory")


class _MpanlDlciBytesToIf_Type(Unsigned32):
    """Custom type mpanlDlciBytesToIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MpanlDlciBytesToIf_Type.__name__ = "Unsigned32"
_MpanlDlciBytesToIf_Object = MibTableColumn
mpanlDlciBytesToIf = _MpanlDlciBytesToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 13, 1, 22),
    _MpanlDlciBytesToIf_Type()
)
mpanlDlciBytesToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciBytesToIf.setStatus("mandatory")


class _MpanlDlciDeBytesToIf_Type(Unsigned32):
    """Custom type mpanlDlciDeBytesToIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MpanlDlciDeBytesToIf_Type.__name__ = "Unsigned32"
_MpanlDlciDeBytesToIf_Object = MibTableColumn
mpanlDlciDeBytesToIf = _MpanlDlciDeBytesToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 13, 1, 23),
    _MpanlDlciDeBytesToIf_Type()
)
mpanlDlciDeBytesToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciDeBytesToIf.setStatus("mandatory")


class _MpanlDlciDiscCongestedToIfBytes_Type(Unsigned32):
    """Custom type mpanlDlciDiscCongestedToIfBytes based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MpanlDlciDiscCongestedToIfBytes_Type.__name__ = "Unsigned32"
_MpanlDlciDiscCongestedToIfBytes_Object = MibTableColumn
mpanlDlciDiscCongestedToIfBytes = _MpanlDlciDiscCongestedToIfBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 13, 1, 24),
    _MpanlDlciDiscCongestedToIfBytes_Type()
)
mpanlDlciDiscCongestedToIfBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciDiscCongestedToIfBytes.setStatus("mandatory")


class _MpanlDlciDiscDeCongestedToIfBytes_Type(Unsigned32):
    """Custom type mpanlDlciDiscDeCongestedToIfBytes based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MpanlDlciDiscDeCongestedToIfBytes_Type.__name__ = "Unsigned32"
_MpanlDlciDiscDeCongestedToIfBytes_Object = MibTableColumn
mpanlDlciDiscDeCongestedToIfBytes = _MpanlDlciDiscDeCongestedToIfBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 13, 1, 25),
    _MpanlDlciDiscDeCongestedToIfBytes_Type()
)
mpanlDlciDiscDeCongestedToIfBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciDiscDeCongestedToIfBytes.setStatus("mandatory")


class _MpanlDlciBytesFromIf_Type(Unsigned32):
    """Custom type mpanlDlciBytesFromIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MpanlDlciBytesFromIf_Type.__name__ = "Unsigned32"
_MpanlDlciBytesFromIf_Object = MibTableColumn
mpanlDlciBytesFromIf = _MpanlDlciBytesFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 13, 1, 26),
    _MpanlDlciBytesFromIf_Type()
)
mpanlDlciBytesFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciBytesFromIf.setStatus("mandatory")


class _MpanlDlciDeBytesFromIf_Type(Unsigned32):
    """Custom type mpanlDlciDeBytesFromIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MpanlDlciDeBytesFromIf_Type.__name__ = "Unsigned32"
_MpanlDlciDeBytesFromIf_Object = MibTableColumn
mpanlDlciDeBytesFromIf = _MpanlDlciDeBytesFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 13, 1, 27),
    _MpanlDlciDeBytesFromIf_Type()
)
mpanlDlciDeBytesFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciDeBytesFromIf.setStatus("mandatory")


class _MpanlDlciExcessBytesFromIf_Type(Unsigned32):
    """Custom type mpanlDlciExcessBytesFromIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MpanlDlciExcessBytesFromIf_Type.__name__ = "Unsigned32"
_MpanlDlciExcessBytesFromIf_Object = MibTableColumn
mpanlDlciExcessBytesFromIf = _MpanlDlciExcessBytesFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 13, 1, 28),
    _MpanlDlciExcessBytesFromIf_Type()
)
mpanlDlciExcessBytesFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciExcessBytesFromIf.setStatus("mandatory")


class _MpanlDlciDiscExcessFromIfBytes_Type(Unsigned32):
    """Custom type mpanlDlciDiscExcessFromIfBytes based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MpanlDlciDiscExcessFromIfBytes_Type.__name__ = "Unsigned32"
_MpanlDlciDiscExcessFromIfBytes_Object = MibTableColumn
mpanlDlciDiscExcessFromIfBytes = _MpanlDlciDiscExcessFromIfBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 13, 1, 29),
    _MpanlDlciDiscExcessFromIfBytes_Type()
)
mpanlDlciDiscExcessFromIfBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciDiscExcessFromIfBytes.setStatus("mandatory")


class _MpanlDlciDiscByteAbit_Type(Unsigned32):
    """Custom type mpanlDlciDiscByteAbit based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MpanlDlciDiscByteAbit_Type.__name__ = "Unsigned32"
_MpanlDlciDiscByteAbit_Object = MibTableColumn
mpanlDlciDiscByteAbit = _MpanlDlciDiscByteAbit_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 13, 1, 30),
    _MpanlDlciDiscByteAbit_Type()
)
mpanlDlciDiscByteAbit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciDiscByteAbit.setStatus("mandatory")


class _MpanlDlciDiscCongestedFromIfBytes_Type(Unsigned32):
    """Custom type mpanlDlciDiscCongestedFromIfBytes based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MpanlDlciDiscCongestedFromIfBytes_Type.__name__ = "Unsigned32"
_MpanlDlciDiscCongestedFromIfBytes_Object = MibTableColumn
mpanlDlciDiscCongestedFromIfBytes = _MpanlDlciDiscCongestedFromIfBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 13, 1, 31),
    _MpanlDlciDiscCongestedFromIfBytes_Type()
)
mpanlDlciDiscCongestedFromIfBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciDiscCongestedFromIfBytes.setStatus("mandatory")


class _MpanlDlciDiscDeCongestedFromIfBytes_Type(Unsigned32):
    """Custom type mpanlDlciDiscDeCongestedFromIfBytes based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MpanlDlciDiscDeCongestedFromIfBytes_Type.__name__ = "Unsigned32"
_MpanlDlciDiscDeCongestedFromIfBytes_Object = MibTableColumn
mpanlDlciDiscDeCongestedFromIfBytes = _MpanlDlciDiscDeCongestedFromIfBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 13, 1, 32),
    _MpanlDlciDiscDeCongestedFromIfBytes_Type()
)
mpanlDlciDiscDeCongestedFromIfBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciDiscDeCongestedFromIfBytes.setStatus("mandatory")


class _MpanlDlciErrorLongBytesFromIf_Type(Unsigned32):
    """Custom type mpanlDlciErrorLongBytesFromIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MpanlDlciErrorLongBytesFromIf_Type.__name__ = "Unsigned32"
_MpanlDlciErrorLongBytesFromIf_Object = MibTableColumn
mpanlDlciErrorLongBytesFromIf = _MpanlDlciErrorLongBytesFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 13, 1, 34),
    _MpanlDlciErrorLongBytesFromIf_Type()
)
mpanlDlciErrorLongBytesFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciErrorLongBytesFromIf.setStatus("mandatory")


class _MpanlDlciTransferPriorityToNetwork_Type(Integer32):
    """Custom type mpanlDlciTransferPriorityToNetwork based on Integer32"""
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


_MpanlDlciTransferPriorityToNetwork_Type.__name__ = "Integer32"
_MpanlDlciTransferPriorityToNetwork_Object = MibTableColumn
mpanlDlciTransferPriorityToNetwork = _MpanlDlciTransferPriorityToNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 13, 1, 37),
    _MpanlDlciTransferPriorityToNetwork_Type()
)
mpanlDlciTransferPriorityToNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciTransferPriorityToNetwork.setStatus("obsolete")


class _MpanlDlciTransferPriorityFromNetwork_Type(Integer32):
    """Custom type mpanlDlciTransferPriorityFromNetwork based on Integer32"""
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


_MpanlDlciTransferPriorityFromNetwork_Type.__name__ = "Integer32"
_MpanlDlciTransferPriorityFromNetwork_Object = MibTableColumn
mpanlDlciTransferPriorityFromNetwork = _MpanlDlciTransferPriorityFromNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 13, 1, 38),
    _MpanlDlciTransferPriorityFromNetwork_Type()
)
mpanlDlciTransferPriorityFromNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciTransferPriorityFromNetwork.setStatus("obsolete")
_MpanlDlciIntTable_Object = MibTable
mpanlDlciIntTable = _MpanlDlciIntTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 14)
)
if mibBuilder.loadTexts:
    mpanlDlciIntTable.setStatus("mandatory")
_MpanlDlciIntEntry_Object = MibTableRow
mpanlDlciIntEntry = _MpanlDlciIntEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 14, 1)
)
mpanlDlciIntEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-MpaNetworkLinkMIB", "mpanlIndex"),
    (0, "Nortel-Magellan-Passport-MpaNetworkLinkMIB", "mpanlDlciIndex"),
)
if mibBuilder.loadTexts:
    mpanlDlciIntEntry.setStatus("mandatory")


class _MpanlDlciStartTime_Type(EnterpriseDateAndTime):
    """Custom type mpanlDlciStartTime based on EnterpriseDateAndTime"""
    subtypeSpec = EnterpriseDateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(19, 19),
    )


_MpanlDlciStartTime_Type.__name__ = "EnterpriseDateAndTime"
_MpanlDlciStartTime_Object = MibTableColumn
mpanlDlciStartTime = _MpanlDlciStartTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 14, 1, 1),
    _MpanlDlciStartTime_Type()
)
mpanlDlciStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciStartTime.setStatus("mandatory")


class _MpanlDlciTotalIngressBytes_Type(Unsigned64):
    """Custom type mpanlDlciTotalIngressBytes based on Unsigned64"""
    subtypeSpec = Unsigned64.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_MpanlDlciTotalIngressBytes_Type.__name__ = "Unsigned64"
_MpanlDlciTotalIngressBytes_Object = MibTableColumn
mpanlDlciTotalIngressBytes = _MpanlDlciTotalIngressBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 14, 1, 2),
    _MpanlDlciTotalIngressBytes_Type()
)
mpanlDlciTotalIngressBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciTotalIngressBytes.setStatus("mandatory")


class _MpanlDlciTotalEgressBytes_Type(Unsigned64):
    """Custom type mpanlDlciTotalEgressBytes based on Unsigned64"""
    subtypeSpec = Unsigned64.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_MpanlDlciTotalEgressBytes_Type.__name__ = "Unsigned64"
_MpanlDlciTotalEgressBytes_Object = MibTableColumn
mpanlDlciTotalEgressBytes = _MpanlDlciTotalEgressBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 14, 1, 3),
    _MpanlDlciTotalEgressBytes_Type()
)
mpanlDlciTotalEgressBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciTotalEgressBytes.setStatus("mandatory")


class _MpanlDlciEirIngressBytes_Type(Unsigned64):
    """Custom type mpanlDlciEirIngressBytes based on Unsigned64"""
    subtypeSpec = Unsigned64.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_MpanlDlciEirIngressBytes_Type.__name__ = "Unsigned64"
_MpanlDlciEirIngressBytes_Object = MibTableColumn
mpanlDlciEirIngressBytes = _MpanlDlciEirIngressBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 14, 1, 4),
    _MpanlDlciEirIngressBytes_Type()
)
mpanlDlciEirIngressBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciEirIngressBytes.setStatus("mandatory")


class _MpanlDlciEirEgressBytes_Type(Unsigned64):
    """Custom type mpanlDlciEirEgressBytes based on Unsigned64"""
    subtypeSpec = Unsigned64.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_MpanlDlciEirEgressBytes_Type.__name__ = "Unsigned64"
_MpanlDlciEirEgressBytes_Object = MibTableColumn
mpanlDlciEirEgressBytes = _MpanlDlciEirEgressBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 14, 1, 5),
    _MpanlDlciEirEgressBytes_Type()
)
mpanlDlciEirEgressBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciEirEgressBytes.setStatus("mandatory")


class _MpanlDlciDiscardedBytes_Type(Unsigned64):
    """Custom type mpanlDlciDiscardedBytes based on Unsigned64"""
    subtypeSpec = Unsigned64.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_MpanlDlciDiscardedBytes_Type.__name__ = "Unsigned64"
_MpanlDlciDiscardedBytes_Object = MibTableColumn
mpanlDlciDiscardedBytes = _MpanlDlciDiscardedBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 14, 1, 6),
    _MpanlDlciDiscardedBytes_Type()
)
mpanlDlciDiscardedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciDiscardedBytes.setStatus("mandatory")


class _MpanlDlciTotalIngressSegFrm_Type(Unsigned32):
    """Custom type mpanlDlciTotalIngressSegFrm based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MpanlDlciTotalIngressSegFrm_Type.__name__ = "Unsigned32"
_MpanlDlciTotalIngressSegFrm_Object = MibTableColumn
mpanlDlciTotalIngressSegFrm = _MpanlDlciTotalIngressSegFrm_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 14, 1, 7),
    _MpanlDlciTotalIngressSegFrm_Type()
)
mpanlDlciTotalIngressSegFrm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciTotalIngressSegFrm.setStatus("mandatory")


class _MpanlDlciTotalEgressSegFrm_Type(Unsigned32):
    """Custom type mpanlDlciTotalEgressSegFrm based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MpanlDlciTotalEgressSegFrm_Type.__name__ = "Unsigned32"
_MpanlDlciTotalEgressSegFrm_Object = MibTableColumn
mpanlDlciTotalEgressSegFrm = _MpanlDlciTotalEgressSegFrm_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 14, 1, 8),
    _MpanlDlciTotalEgressSegFrm_Type()
)
mpanlDlciTotalEgressSegFrm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciTotalEgressSegFrm.setStatus("mandatory")


class _MpanlDlciEirIngressSegFrm_Type(Unsigned32):
    """Custom type mpanlDlciEirIngressSegFrm based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MpanlDlciEirIngressSegFrm_Type.__name__ = "Unsigned32"
_MpanlDlciEirIngressSegFrm_Object = MibTableColumn
mpanlDlciEirIngressSegFrm = _MpanlDlciEirIngressSegFrm_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 14, 1, 9),
    _MpanlDlciEirIngressSegFrm_Type()
)
mpanlDlciEirIngressSegFrm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciEirIngressSegFrm.setStatus("mandatory")


class _MpanlDlciEirEgressSegFrm_Type(Unsigned32):
    """Custom type mpanlDlciEirEgressSegFrm based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MpanlDlciEirEgressSegFrm_Type.__name__ = "Unsigned32"
_MpanlDlciEirEgressSegFrm_Object = MibTableColumn
mpanlDlciEirEgressSegFrm = _MpanlDlciEirEgressSegFrm_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 14, 1, 10),
    _MpanlDlciEirEgressSegFrm_Type()
)
mpanlDlciEirEgressSegFrm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciEirEgressSegFrm.setStatus("mandatory")


class _MpanlDlciDiscardedSegFrm_Type(Unsigned32):
    """Custom type mpanlDlciDiscardedSegFrm based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MpanlDlciDiscardedSegFrm_Type.__name__ = "Unsigned32"
_MpanlDlciDiscardedSegFrm_Object = MibTableColumn
mpanlDlciDiscardedSegFrm = _MpanlDlciDiscardedSegFrm_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 14, 1, 11),
    _MpanlDlciDiscardedSegFrm_Type()
)
mpanlDlciDiscardedSegFrm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciDiscardedSegFrm.setStatus("mandatory")


class _MpanlDlciCallReferenceNumber_Type(Unsigned32):
    """Custom type mpanlDlciCallReferenceNumber based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MpanlDlciCallReferenceNumber_Type.__name__ = "Unsigned32"
_MpanlDlciCallReferenceNumber_Object = MibTableColumn
mpanlDlciCallReferenceNumber = _MpanlDlciCallReferenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 14, 1, 17),
    _MpanlDlciCallReferenceNumber_Type()
)
mpanlDlciCallReferenceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciCallReferenceNumber.setStatus("mandatory")


class _MpanlDlciElapsedDifference_Type(Unsigned32):
    """Custom type mpanlDlciElapsedDifference based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MpanlDlciElapsedDifference_Type.__name__ = "Unsigned32"
_MpanlDlciElapsedDifference_Object = MibTableColumn
mpanlDlciElapsedDifference = _MpanlDlciElapsedDifference_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 14, 1, 18),
    _MpanlDlciElapsedDifference_Type()
)
mpanlDlciElapsedDifference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciElapsedDifference.setStatus("mandatory")
_MpanlDlciAbitTable_Object = MibTable
mpanlDlciAbitTable = _MpanlDlciAbitTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 15)
)
if mibBuilder.loadTexts:
    mpanlDlciAbitTable.setStatus("mandatory")
_MpanlDlciAbitEntry_Object = MibTableRow
mpanlDlciAbitEntry = _MpanlDlciAbitEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 15, 1)
)
mpanlDlciAbitEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-MpaNetworkLinkMIB", "mpanlIndex"),
    (0, "Nortel-Magellan-Passport-MpaNetworkLinkMIB", "mpanlDlciIndex"),
)
if mibBuilder.loadTexts:
    mpanlDlciAbitEntry.setStatus("mandatory")


class _MpanlDlciABitStatusToIf_Type(Integer32):
    """Custom type mpanlDlciABitStatusToIf based on Integer32"""
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


_MpanlDlciABitStatusToIf_Type.__name__ = "Integer32"
_MpanlDlciABitStatusToIf_Object = MibTableColumn
mpanlDlciABitStatusToIf = _MpanlDlciABitStatusToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 15, 1, 1),
    _MpanlDlciABitStatusToIf_Type()
)
mpanlDlciABitStatusToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciABitStatusToIf.setStatus("mandatory")


class _MpanlDlciABitReasonToIf_Type(Integer32):
    """Custom type mpanlDlciABitReasonToIf based on Integer32"""
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


_MpanlDlciABitReasonToIf_Type.__name__ = "Integer32"
_MpanlDlciABitReasonToIf_Object = MibTableColumn
mpanlDlciABitReasonToIf = _MpanlDlciABitReasonToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 15, 1, 2),
    _MpanlDlciABitReasonToIf_Type()
)
mpanlDlciABitReasonToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciABitReasonToIf.setStatus("mandatory")


class _MpanlDlciABitStatusFromIf_Type(Integer32):
    """Custom type mpanlDlciABitStatusFromIf based on Integer32"""
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


_MpanlDlciABitStatusFromIf_Type.__name__ = "Integer32"
_MpanlDlciABitStatusFromIf_Object = MibTableColumn
mpanlDlciABitStatusFromIf = _MpanlDlciABitStatusFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 15, 1, 3),
    _MpanlDlciABitStatusFromIf_Type()
)
mpanlDlciABitStatusFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciABitStatusFromIf.setStatus("mandatory")


class _MpanlDlciABitReasonFromIf_Type(Integer32):
    """Custom type mpanlDlciABitReasonFromIf based on Integer32"""
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


_MpanlDlciABitReasonFromIf_Type.__name__ = "Integer32"
_MpanlDlciABitReasonFromIf_Object = MibTableColumn
mpanlDlciABitReasonFromIf = _MpanlDlciABitReasonFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 15, 1, 4),
    _MpanlDlciABitReasonFromIf_Type()
)
mpanlDlciABitReasonFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciABitReasonFromIf.setStatus("mandatory")


class _MpanlDlciLoopbackState_Type(Integer32):
    """Custom type mpanlDlciLoopbackState based on Integer32"""
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


_MpanlDlciLoopbackState_Type.__name__ = "Integer32"
_MpanlDlciLoopbackState_Object = MibTableColumn
mpanlDlciLoopbackState = _MpanlDlciLoopbackState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 5, 15, 1, 5),
    _MpanlDlciLoopbackState_Type()
)
mpanlDlciLoopbackState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlDlciLoopbackState.setStatus("mandatory")
_MpanlSig_ObjectIdentity = ObjectIdentity
mpanlSig = _MpanlSig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 6)
)
_MpanlSigRowStatusTable_Object = MibTable
mpanlSigRowStatusTable = _MpanlSigRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 6, 1)
)
if mibBuilder.loadTexts:
    mpanlSigRowStatusTable.setStatus("mandatory")
_MpanlSigRowStatusEntry_Object = MibTableRow
mpanlSigRowStatusEntry = _MpanlSigRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 6, 1, 1)
)
mpanlSigRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-MpaNetworkLinkMIB", "mpanlIndex"),
    (0, "Nortel-Magellan-Passport-MpaNetworkLinkMIB", "mpanlSigIndex"),
)
if mibBuilder.loadTexts:
    mpanlSigRowStatusEntry.setStatus("mandatory")
_MpanlSigRowStatus_Type = RowStatus
_MpanlSigRowStatus_Object = MibTableColumn
mpanlSigRowStatus = _MpanlSigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 6, 1, 1, 1),
    _MpanlSigRowStatus_Type()
)
mpanlSigRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlSigRowStatus.setStatus("mandatory")
_MpanlSigComponentName_Type = DisplayString
_MpanlSigComponentName_Object = MibTableColumn
mpanlSigComponentName = _MpanlSigComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 6, 1, 1, 2),
    _MpanlSigComponentName_Type()
)
mpanlSigComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlSigComponentName.setStatus("mandatory")
_MpanlSigStorageType_Type = StorageType
_MpanlSigStorageType_Object = MibTableColumn
mpanlSigStorageType = _MpanlSigStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 6, 1, 1, 4),
    _MpanlSigStorageType_Type()
)
mpanlSigStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlSigStorageType.setStatus("mandatory")
_MpanlSigIndex_Type = NonReplicated
_MpanlSigIndex_Object = MibTableColumn
mpanlSigIndex = _MpanlSigIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 6, 1, 1, 10),
    _MpanlSigIndex_Type()
)
mpanlSigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mpanlSigIndex.setStatus("mandatory")
_MpanlSigSysParmsTable_Object = MibTable
mpanlSigSysParmsTable = _MpanlSigSysParmsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 6, 13)
)
if mibBuilder.loadTexts:
    mpanlSigSysParmsTable.setStatus("mandatory")
_MpanlSigSysParmsEntry_Object = MibTableRow
mpanlSigSysParmsEntry = _MpanlSigSysParmsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 6, 13, 1)
)
mpanlSigSysParmsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-MpaNetworkLinkMIB", "mpanlIndex"),
    (0, "Nortel-Magellan-Passport-MpaNetworkLinkMIB", "mpanlSigIndex"),
)
if mibBuilder.loadTexts:
    mpanlSigSysParmsEntry.setStatus("mandatory")


class _MpanlSigCallSetupTimer_Type(Unsigned32):
    """Custom type mpanlSigCallSetupTimer based on Unsigned32"""
    defaultValue = 4

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_MpanlSigCallSetupTimer_Type.__name__ = "Unsigned32"
_MpanlSigCallSetupTimer_Object = MibTableColumn
mpanlSigCallSetupTimer = _MpanlSigCallSetupTimer_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 6, 13, 1, 1),
    _MpanlSigCallSetupTimer_Type()
)
mpanlSigCallSetupTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpanlSigCallSetupTimer.setStatus("mandatory")


class _MpanlSigDisconnectTimer_Type(Unsigned32):
    """Custom type mpanlSigDisconnectTimer based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_MpanlSigDisconnectTimer_Type.__name__ = "Unsigned32"
_MpanlSigDisconnectTimer_Object = MibTableColumn
mpanlSigDisconnectTimer = _MpanlSigDisconnectTimer_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 6, 13, 1, 2),
    _MpanlSigDisconnectTimer_Type()
)
mpanlSigDisconnectTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpanlSigDisconnectTimer.setStatus("mandatory")


class _MpanlSigReleaseTimer_Type(Unsigned32):
    """Custom type mpanlSigReleaseTimer based on Unsigned32"""
    defaultValue = 4

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_MpanlSigReleaseTimer_Type.__name__ = "Unsigned32"
_MpanlSigReleaseTimer_Object = MibTableColumn
mpanlSigReleaseTimer = _MpanlSigReleaseTimer_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 6, 13, 1, 3),
    _MpanlSigReleaseTimer_Type()
)
mpanlSigReleaseTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpanlSigReleaseTimer.setStatus("mandatory")


class _MpanlSigCallProceedingTimer_Type(Unsigned32):
    """Custom type mpanlSigCallProceedingTimer based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_MpanlSigCallProceedingTimer_Type.__name__ = "Unsigned32"
_MpanlSigCallProceedingTimer_Object = MibTableColumn
mpanlSigCallProceedingTimer = _MpanlSigCallProceedingTimer_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 6, 13, 1, 4),
    _MpanlSigCallProceedingTimer_Type()
)
mpanlSigCallProceedingTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpanlSigCallProceedingTimer.setStatus("mandatory")


class _MpanlSigNetworkType_Type(Integer32):
    """Custom type mpanlSigNetworkType based on Integer32"""
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


_MpanlSigNetworkType_Type.__name__ = "Integer32"
_MpanlSigNetworkType_Object = MibTableColumn
mpanlSigNetworkType = _MpanlSigNetworkType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 6, 13, 1, 5),
    _MpanlSigNetworkType_Type()
)
mpanlSigNetworkType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpanlSigNetworkType.setStatus("mandatory")
_MpanlSigLapfSysTable_Object = MibTable
mpanlSigLapfSysTable = _MpanlSigLapfSysTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 6, 14)
)
if mibBuilder.loadTexts:
    mpanlSigLapfSysTable.setStatus("mandatory")
_MpanlSigLapfSysEntry_Object = MibTableRow
mpanlSigLapfSysEntry = _MpanlSigLapfSysEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 6, 14, 1)
)
mpanlSigLapfSysEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-MpaNetworkLinkMIB", "mpanlIndex"),
    (0, "Nortel-Magellan-Passport-MpaNetworkLinkMIB", "mpanlSigIndex"),
)
if mibBuilder.loadTexts:
    mpanlSigLapfSysEntry.setStatus("mandatory")


class _MpanlSigWindowSize_Type(Unsigned32):
    """Custom type mpanlSigWindowSize based on Unsigned32"""
    defaultValue = 7

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_MpanlSigWindowSize_Type.__name__ = "Unsigned32"
_MpanlSigWindowSize_Object = MibTableColumn
mpanlSigWindowSize = _MpanlSigWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 6, 14, 1, 2),
    _MpanlSigWindowSize_Type()
)
mpanlSigWindowSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpanlSigWindowSize.setStatus("mandatory")


class _MpanlSigRetransmitLimit_Type(Unsigned32):
    """Custom type mpanlSigRetransmitLimit based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_MpanlSigRetransmitLimit_Type.__name__ = "Unsigned32"
_MpanlSigRetransmitLimit_Object = MibTableColumn
mpanlSigRetransmitLimit = _MpanlSigRetransmitLimit_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 6, 14, 1, 3),
    _MpanlSigRetransmitLimit_Type()
)
mpanlSigRetransmitLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpanlSigRetransmitLimit.setStatus("mandatory")


class _MpanlSigAckTimer_Type(Unsigned32):
    """Custom type mpanlSigAckTimer based on Unsigned32"""
    defaultValue = 1500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 10000),
    )


_MpanlSigAckTimer_Type.__name__ = "Unsigned32"
_MpanlSigAckTimer_Object = MibTableColumn
mpanlSigAckTimer = _MpanlSigAckTimer_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 6, 14, 1, 4),
    _MpanlSigAckTimer_Type()
)
mpanlSigAckTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpanlSigAckTimer.setStatus("mandatory")


class _MpanlSigAckDelayTimer_Type(Unsigned32):
    """Custom type mpanlSigAckDelayTimer based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_MpanlSigAckDelayTimer_Type.__name__ = "Unsigned32"
_MpanlSigAckDelayTimer_Object = MibTableColumn
mpanlSigAckDelayTimer = _MpanlSigAckDelayTimer_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 6, 14, 1, 5),
    _MpanlSigAckDelayTimer_Type()
)
mpanlSigAckDelayTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpanlSigAckDelayTimer.setStatus("mandatory")


class _MpanlSigIdleProbeTimer_Type(Unsigned32):
    """Custom type mpanlSigIdleProbeTimer based on Unsigned32"""
    defaultValue = 30000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 65535000),
    )


_MpanlSigIdleProbeTimer_Type.__name__ = "Unsigned32"
_MpanlSigIdleProbeTimer_Object = MibTableColumn
mpanlSigIdleProbeTimer = _MpanlSigIdleProbeTimer_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 6, 14, 1, 6),
    _MpanlSigIdleProbeTimer_Type()
)
mpanlSigIdleProbeTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpanlSigIdleProbeTimer.setStatus("mandatory")
_MpanlSigSvcaccTable_Object = MibTable
mpanlSigSvcaccTable = _MpanlSigSvcaccTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 6, 15)
)
if mibBuilder.loadTexts:
    mpanlSigSvcaccTable.setStatus("mandatory")
_MpanlSigSvcaccEntry_Object = MibTableRow
mpanlSigSvcaccEntry = _MpanlSigSvcaccEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 6, 15, 1)
)
mpanlSigSvcaccEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-MpaNetworkLinkMIB", "mpanlIndex"),
    (0, "Nortel-Magellan-Passport-MpaNetworkLinkMIB", "mpanlSigIndex"),
)
if mibBuilder.loadTexts:
    mpanlSigSvcaccEntry.setStatus("mandatory")


class _MpanlSigDefaultAccounting_Type(Integer32):
    """Custom type mpanlSigDefaultAccounting based on Integer32"""
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


_MpanlSigDefaultAccounting_Type.__name__ = "Integer32"
_MpanlSigDefaultAccounting_Object = MibTableColumn
mpanlSigDefaultAccounting = _MpanlSigDefaultAccounting_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 6, 15, 1, 1),
    _MpanlSigDefaultAccounting_Type()
)
mpanlSigDefaultAccounting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpanlSigDefaultAccounting.setStatus("mandatory")
_MpanlSigStateTable_Object = MibTable
mpanlSigStateTable = _MpanlSigStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 6, 16)
)
if mibBuilder.loadTexts:
    mpanlSigStateTable.setStatus("mandatory")
_MpanlSigStateEntry_Object = MibTableRow
mpanlSigStateEntry = _MpanlSigStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 6, 16, 1)
)
mpanlSigStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-MpaNetworkLinkMIB", "mpanlIndex"),
    (0, "Nortel-Magellan-Passport-MpaNetworkLinkMIB", "mpanlSigIndex"),
)
if mibBuilder.loadTexts:
    mpanlSigStateEntry.setStatus("mandatory")


class _MpanlSigAdminState_Type(Integer32):
    """Custom type mpanlSigAdminState based on Integer32"""
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


_MpanlSigAdminState_Type.__name__ = "Integer32"
_MpanlSigAdminState_Object = MibTableColumn
mpanlSigAdminState = _MpanlSigAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 6, 16, 1, 1),
    _MpanlSigAdminState_Type()
)
mpanlSigAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlSigAdminState.setStatus("mandatory")


class _MpanlSigOperationalState_Type(Integer32):
    """Custom type mpanlSigOperationalState based on Integer32"""
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


_MpanlSigOperationalState_Type.__name__ = "Integer32"
_MpanlSigOperationalState_Object = MibTableColumn
mpanlSigOperationalState = _MpanlSigOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 6, 16, 1, 2),
    _MpanlSigOperationalState_Type()
)
mpanlSigOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlSigOperationalState.setStatus("mandatory")


class _MpanlSigUsageState_Type(Integer32):
    """Custom type mpanlSigUsageState based on Integer32"""
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


_MpanlSigUsageState_Type.__name__ = "Integer32"
_MpanlSigUsageState_Object = MibTableColumn
mpanlSigUsageState = _MpanlSigUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 6, 16, 1, 3),
    _MpanlSigUsageState_Type()
)
mpanlSigUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlSigUsageState.setStatus("mandatory")
_MpanlSigStatsTable_Object = MibTable
mpanlSigStatsTable = _MpanlSigStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 6, 17)
)
if mibBuilder.loadTexts:
    mpanlSigStatsTable.setStatus("mandatory")
_MpanlSigStatsEntry_Object = MibTableRow
mpanlSigStatsEntry = _MpanlSigStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 6, 17, 1)
)
mpanlSigStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-MpaNetworkLinkMIB", "mpanlIndex"),
    (0, "Nortel-Magellan-Passport-MpaNetworkLinkMIB", "mpanlSigIndex"),
)
if mibBuilder.loadTexts:
    mpanlSigStatsEntry.setStatus("mandatory")


class _MpanlSigCurrentNumberOfSvcCalls_Type(Unsigned32):
    """Custom type mpanlSigCurrentNumberOfSvcCalls based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 991),
    )


_MpanlSigCurrentNumberOfSvcCalls_Type.__name__ = "Unsigned32"
_MpanlSigCurrentNumberOfSvcCalls_Object = MibTableColumn
mpanlSigCurrentNumberOfSvcCalls = _MpanlSigCurrentNumberOfSvcCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 6, 17, 1, 1),
    _MpanlSigCurrentNumberOfSvcCalls_Type()
)
mpanlSigCurrentNumberOfSvcCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlSigCurrentNumberOfSvcCalls.setStatus("mandatory")
_MpanlSigInCalls_Type = Counter32
_MpanlSigInCalls_Object = MibTableColumn
mpanlSigInCalls = _MpanlSigInCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 6, 17, 1, 4),
    _MpanlSigInCalls_Type()
)
mpanlSigInCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlSigInCalls.setStatus("mandatory")
_MpanlSigInCallsRefused_Type = Counter32
_MpanlSigInCallsRefused_Object = MibTableColumn
mpanlSigInCallsRefused = _MpanlSigInCallsRefused_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 6, 17, 1, 5),
    _MpanlSigInCallsRefused_Type()
)
mpanlSigInCallsRefused.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlSigInCallsRefused.setStatus("mandatory")
_MpanlSigOutCalls_Type = Counter32
_MpanlSigOutCalls_Object = MibTableColumn
mpanlSigOutCalls = _MpanlSigOutCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 6, 17, 1, 6),
    _MpanlSigOutCalls_Type()
)
mpanlSigOutCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlSigOutCalls.setStatus("mandatory")
_MpanlSigOutCallsFailed_Type = Counter32
_MpanlSigOutCallsFailed_Object = MibTableColumn
mpanlSigOutCallsFailed = _MpanlSigOutCallsFailed_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 6, 17, 1, 7),
    _MpanlSigOutCallsFailed_Type()
)
mpanlSigOutCallsFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlSigOutCallsFailed.setStatus("mandatory")
_MpanlSigProtocolErrors_Type = Counter32
_MpanlSigProtocolErrors_Object = MibTableColumn
mpanlSigProtocolErrors = _MpanlSigProtocolErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 6, 17, 1, 8),
    _MpanlSigProtocolErrors_Type()
)
mpanlSigProtocolErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlSigProtocolErrors.setStatus("mandatory")
_MpanlSigQualityOfServiceNotAvailable_Type = Counter32
_MpanlSigQualityOfServiceNotAvailable_Object = MibTableColumn
mpanlSigQualityOfServiceNotAvailable = _MpanlSigQualityOfServiceNotAvailable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 6, 17, 1, 9),
    _MpanlSigQualityOfServiceNotAvailable_Type()
)
mpanlSigQualityOfServiceNotAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlSigQualityOfServiceNotAvailable.setStatus("mandatory")
_MpanlSigSetupTimeout_Type = Counter32
_MpanlSigSetupTimeout_Object = MibTableColumn
mpanlSigSetupTimeout = _MpanlSigSetupTimeout_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 6, 17, 1, 10),
    _MpanlSigSetupTimeout_Type()
)
mpanlSigSetupTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlSigSetupTimeout.setStatus("mandatory")


class _MpanlSigLastCauseInStatusMsgReceived_Type(Unsigned32):
    """Custom type mpanlSigLastCauseInStatusMsgReceived based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MpanlSigLastCauseInStatusMsgReceived_Type.__name__ = "Unsigned32"
_MpanlSigLastCauseInStatusMsgReceived_Object = MibTableColumn
mpanlSigLastCauseInStatusMsgReceived = _MpanlSigLastCauseInStatusMsgReceived_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 6, 17, 1, 11),
    _MpanlSigLastCauseInStatusMsgReceived_Type()
)
mpanlSigLastCauseInStatusMsgReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlSigLastCauseInStatusMsgReceived.setStatus("mandatory")


class _MpanlSigLastStateInStatusMsgReceived_Type(Integer32):
    """Custom type mpanlSigLastStateInStatusMsgReceived based on Integer32"""
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


_MpanlSigLastStateInStatusMsgReceived_Type.__name__ = "Integer32"
_MpanlSigLastStateInStatusMsgReceived_Object = MibTableColumn
mpanlSigLastStateInStatusMsgReceived = _MpanlSigLastStateInStatusMsgReceived_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 6, 17, 1, 12),
    _MpanlSigLastStateInStatusMsgReceived_Type()
)
mpanlSigLastStateInStatusMsgReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlSigLastStateInStatusMsgReceived.setStatus("mandatory")


class _MpanlSigLastDlciReceivedStatus_Type(Unsigned32):
    """Custom type mpanlSigLastDlciReceivedStatus based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(17, 1007),
    )


_MpanlSigLastDlciReceivedStatus_Type.__name__ = "Unsigned32"
_MpanlSigLastDlciReceivedStatus_Object = MibTableColumn
mpanlSigLastDlciReceivedStatus = _MpanlSigLastDlciReceivedStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 6, 17, 1, 13),
    _MpanlSigLastDlciReceivedStatus_Type()
)
mpanlSigLastDlciReceivedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlSigLastDlciReceivedStatus.setStatus("mandatory")


class _MpanlSigLastQ933StateReceivedStatus_Type(Integer32):
    """Custom type mpanlSigLastQ933StateReceivedStatus based on Integer32"""
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


_MpanlSigLastQ933StateReceivedStatus_Type.__name__ = "Integer32"
_MpanlSigLastQ933StateReceivedStatus_Object = MibTableColumn
mpanlSigLastQ933StateReceivedStatus = _MpanlSigLastQ933StateReceivedStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 6, 17, 1, 14),
    _MpanlSigLastQ933StateReceivedStatus_Type()
)
mpanlSigLastQ933StateReceivedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlSigLastQ933StateReceivedStatus.setStatus("mandatory")


class _MpanlSigLastTimeMsgBlockCongested_Type(EnterpriseDateAndTime):
    """Custom type mpanlSigLastTimeMsgBlockCongested based on EnterpriseDateAndTime"""
    subtypeSpec = EnterpriseDateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(16, 16),
    )


_MpanlSigLastTimeMsgBlockCongested_Type.__name__ = "EnterpriseDateAndTime"
_MpanlSigLastTimeMsgBlockCongested_Object = MibTableColumn
mpanlSigLastTimeMsgBlockCongested = _MpanlSigLastTimeMsgBlockCongested_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 6, 17, 1, 15),
    _MpanlSigLastTimeMsgBlockCongested_Type()
)
mpanlSigLastTimeMsgBlockCongested.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlSigLastTimeMsgBlockCongested.setStatus("mandatory")


class _MpanlSigLastDlciWithMsgBlockCongestion_Type(Unsigned32):
    """Custom type mpanlSigLastDlciWithMsgBlockCongestion based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(16, 1007),
    )


_MpanlSigLastDlciWithMsgBlockCongestion_Type.__name__ = "Unsigned32"
_MpanlSigLastDlciWithMsgBlockCongestion_Object = MibTableColumn
mpanlSigLastDlciWithMsgBlockCongestion = _MpanlSigLastDlciWithMsgBlockCongestion_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 6, 17, 1, 16),
    _MpanlSigLastDlciWithMsgBlockCongestion_Type()
)
mpanlSigLastDlciWithMsgBlockCongestion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlSigLastDlciWithMsgBlockCongestion.setStatus("mandatory")
_MpanlSigLapfStatusTable_Object = MibTable
mpanlSigLapfStatusTable = _MpanlSigLapfStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 6, 18)
)
if mibBuilder.loadTexts:
    mpanlSigLapfStatusTable.setStatus("mandatory")
_MpanlSigLapfStatusEntry_Object = MibTableRow
mpanlSigLapfStatusEntry = _MpanlSigLapfStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 6, 18, 1)
)
mpanlSigLapfStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-MpaNetworkLinkMIB", "mpanlIndex"),
    (0, "Nortel-Magellan-Passport-MpaNetworkLinkMIB", "mpanlSigIndex"),
)
if mibBuilder.loadTexts:
    mpanlSigLapfStatusEntry.setStatus("mandatory")


class _MpanlSigCurrentState_Type(Integer32):
    """Custom type mpanlSigCurrentState based on Integer32"""
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


_MpanlSigCurrentState_Type.__name__ = "Integer32"
_MpanlSigCurrentState_Object = MibTableColumn
mpanlSigCurrentState = _MpanlSigCurrentState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 6, 18, 1, 1),
    _MpanlSigCurrentState_Type()
)
mpanlSigCurrentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlSigCurrentState.setStatus("mandatory")


class _MpanlSigLastStateChangeReason_Type(Integer32):
    """Custom type mpanlSigLastStateChangeReason based on Integer32"""
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


_MpanlSigLastStateChangeReason_Type.__name__ = "Integer32"
_MpanlSigLastStateChangeReason_Object = MibTableColumn
mpanlSigLastStateChangeReason = _MpanlSigLastStateChangeReason_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 6, 18, 1, 2),
    _MpanlSigLastStateChangeReason_Type()
)
mpanlSigLastStateChangeReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlSigLastStateChangeReason.setStatus("mandatory")


class _MpanlSigFrmrReceive_Type(HexString):
    """Custom type mpanlSigFrmrReceive based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_MpanlSigFrmrReceive_Type.__name__ = "HexString"
_MpanlSigFrmrReceive_Object = MibTableColumn
mpanlSigFrmrReceive = _MpanlSigFrmrReceive_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 6, 18, 1, 3),
    _MpanlSigFrmrReceive_Type()
)
mpanlSigFrmrReceive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlSigFrmrReceive.setStatus("mandatory")
_MpanlSigCurrentQueueSize_Type = Counter32
_MpanlSigCurrentQueueSize_Object = MibTableColumn
mpanlSigCurrentQueueSize = _MpanlSigCurrentQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 6, 18, 1, 4),
    _MpanlSigCurrentQueueSize_Type()
)
mpanlSigCurrentQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlSigCurrentQueueSize.setStatus("mandatory")
_MpanlSigLapfStatsTable_Object = MibTable
mpanlSigLapfStatsTable = _MpanlSigLapfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 6, 19)
)
if mibBuilder.loadTexts:
    mpanlSigLapfStatsTable.setStatus("mandatory")
_MpanlSigLapfStatsEntry_Object = MibTableRow
mpanlSigLapfStatsEntry = _MpanlSigLapfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 6, 19, 1)
)
mpanlSigLapfStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-MpaNetworkLinkMIB", "mpanlIndex"),
    (0, "Nortel-Magellan-Passport-MpaNetworkLinkMIB", "mpanlSigIndex"),
)
if mibBuilder.loadTexts:
    mpanlSigLapfStatsEntry.setStatus("mandatory")
_MpanlSigStateChange_Type = Counter32
_MpanlSigStateChange_Object = MibTableColumn
mpanlSigStateChange = _MpanlSigStateChange_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 6, 19, 1, 1),
    _MpanlSigStateChange_Type()
)
mpanlSigStateChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlSigStateChange.setStatus("mandatory")
_MpanlSigRemoteBusy_Type = Counter32
_MpanlSigRemoteBusy_Object = MibTableColumn
mpanlSigRemoteBusy = _MpanlSigRemoteBusy_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 6, 19, 1, 2),
    _MpanlSigRemoteBusy_Type()
)
mpanlSigRemoteBusy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlSigRemoteBusy.setStatus("mandatory")
_MpanlSigReceiveRejectFrame_Type = Counter32
_MpanlSigReceiveRejectFrame_Object = MibTableColumn
mpanlSigReceiveRejectFrame = _MpanlSigReceiveRejectFrame_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 6, 19, 1, 3),
    _MpanlSigReceiveRejectFrame_Type()
)
mpanlSigReceiveRejectFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlSigReceiveRejectFrame.setStatus("mandatory")
_MpanlSigAckTimeout_Type = Counter32
_MpanlSigAckTimeout_Object = MibTableColumn
mpanlSigAckTimeout = _MpanlSigAckTimeout_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 6, 19, 1, 4),
    _MpanlSigAckTimeout_Type()
)
mpanlSigAckTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlSigAckTimeout.setStatus("mandatory")
_MpanlSigIFramesTransmitted_Type = Counter32
_MpanlSigIFramesTransmitted_Object = MibTableColumn
mpanlSigIFramesTransmitted = _MpanlSigIFramesTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 6, 19, 1, 5),
    _MpanlSigIFramesTransmitted_Type()
)
mpanlSigIFramesTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlSigIFramesTransmitted.setStatus("mandatory")
_MpanlSigIFramesTxDiscarded_Type = Counter32
_MpanlSigIFramesTxDiscarded_Object = MibTableColumn
mpanlSigIFramesTxDiscarded = _MpanlSigIFramesTxDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 6, 19, 1, 6),
    _MpanlSigIFramesTxDiscarded_Type()
)
mpanlSigIFramesTxDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlSigIFramesTxDiscarded.setStatus("mandatory")
_MpanlSigIFramesReceived_Type = Counter32
_MpanlSigIFramesReceived_Object = MibTableColumn
mpanlSigIFramesReceived = _MpanlSigIFramesReceived_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 6, 19, 1, 7),
    _MpanlSigIFramesReceived_Type()
)
mpanlSigIFramesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlSigIFramesReceived.setStatus("mandatory")
_MpanlSigIFramesRcvdDiscarded_Type = Counter32
_MpanlSigIFramesRcvdDiscarded_Object = MibTableColumn
mpanlSigIFramesRcvdDiscarded = _MpanlSigIFramesRcvdDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 6, 19, 1, 8),
    _MpanlSigIFramesRcvdDiscarded_Type()
)
mpanlSigIFramesRcvdDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlSigIFramesRcvdDiscarded.setStatus("mandatory")
_MpanlSigMpanl_ObjectIdentity = ObjectIdentity
mpanlSigMpanl = _MpanlSigMpanl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 7)
)
_MpanlSigMpanlRowStatusTable_Object = MibTable
mpanlSigMpanlRowStatusTable = _MpanlSigMpanlRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 7, 1)
)
if mibBuilder.loadTexts:
    mpanlSigMpanlRowStatusTable.setStatus("mandatory")
_MpanlSigMpanlRowStatusEntry_Object = MibTableRow
mpanlSigMpanlRowStatusEntry = _MpanlSigMpanlRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 7, 1, 1)
)
mpanlSigMpanlRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-MpaNetworkLinkMIB", "mpanlIndex"),
    (0, "Nortel-Magellan-Passport-MpaNetworkLinkMIB", "mpanlSigMpanlIndex"),
)
if mibBuilder.loadTexts:
    mpanlSigMpanlRowStatusEntry.setStatus("mandatory")
_MpanlSigMpanlRowStatus_Type = RowStatus
_MpanlSigMpanlRowStatus_Object = MibTableColumn
mpanlSigMpanlRowStatus = _MpanlSigMpanlRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 7, 1, 1, 1),
    _MpanlSigMpanlRowStatus_Type()
)
mpanlSigMpanlRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlSigMpanlRowStatus.setStatus("mandatory")
_MpanlSigMpanlComponentName_Type = DisplayString
_MpanlSigMpanlComponentName_Object = MibTableColumn
mpanlSigMpanlComponentName = _MpanlSigMpanlComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 7, 1, 1, 2),
    _MpanlSigMpanlComponentName_Type()
)
mpanlSigMpanlComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlSigMpanlComponentName.setStatus("mandatory")
_MpanlSigMpanlStorageType_Type = StorageType
_MpanlSigMpanlStorageType_Object = MibTableColumn
mpanlSigMpanlStorageType = _MpanlSigMpanlStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 7, 1, 1, 4),
    _MpanlSigMpanlStorageType_Type()
)
mpanlSigMpanlStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlSigMpanlStorageType.setStatus("mandatory")
_MpanlSigMpanlIndex_Type = NonReplicated
_MpanlSigMpanlIndex_Object = MibTableColumn
mpanlSigMpanlIndex = _MpanlSigMpanlIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 7, 1, 1, 10),
    _MpanlSigMpanlIndex_Type()
)
mpanlSigMpanlIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mpanlSigMpanlIndex.setStatus("mandatory")
_MpanlSigMpanlStateTable_Object = MibTable
mpanlSigMpanlStateTable = _MpanlSigMpanlStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 7, 10)
)
if mibBuilder.loadTexts:
    mpanlSigMpanlStateTable.setStatus("mandatory")
_MpanlSigMpanlStateEntry_Object = MibTableRow
mpanlSigMpanlStateEntry = _MpanlSigMpanlStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 7, 10, 1)
)
mpanlSigMpanlStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-MpaNetworkLinkMIB", "mpanlIndex"),
    (0, "Nortel-Magellan-Passport-MpaNetworkLinkMIB", "mpanlSigMpanlIndex"),
)
if mibBuilder.loadTexts:
    mpanlSigMpanlStateEntry.setStatus("mandatory")


class _MpanlSigMpanlAdminState_Type(Integer32):
    """Custom type mpanlSigMpanlAdminState based on Integer32"""
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


_MpanlSigMpanlAdminState_Type.__name__ = "Integer32"
_MpanlSigMpanlAdminState_Object = MibTableColumn
mpanlSigMpanlAdminState = _MpanlSigMpanlAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 7, 10, 1, 1),
    _MpanlSigMpanlAdminState_Type()
)
mpanlSigMpanlAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlSigMpanlAdminState.setStatus("mandatory")


class _MpanlSigMpanlOperationalState_Type(Integer32):
    """Custom type mpanlSigMpanlOperationalState based on Integer32"""
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


_MpanlSigMpanlOperationalState_Type.__name__ = "Integer32"
_MpanlSigMpanlOperationalState_Object = MibTableColumn
mpanlSigMpanlOperationalState = _MpanlSigMpanlOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 7, 10, 1, 2),
    _MpanlSigMpanlOperationalState_Type()
)
mpanlSigMpanlOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlSigMpanlOperationalState.setStatus("mandatory")


class _MpanlSigMpanlUsageState_Type(Integer32):
    """Custom type mpanlSigMpanlUsageState based on Integer32"""
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


_MpanlSigMpanlUsageState_Type.__name__ = "Integer32"
_MpanlSigMpanlUsageState_Object = MibTableColumn
mpanlSigMpanlUsageState = _MpanlSigMpanlUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 7, 10, 1, 3),
    _MpanlSigMpanlUsageState_Type()
)
mpanlSigMpanlUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlSigMpanlUsageState.setStatus("mandatory")
_MpanlSigMpanlProfileTable_Object = MibTable
mpanlSigMpanlProfileTable = _MpanlSigMpanlProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 7, 11)
)
if mibBuilder.loadTexts:
    mpanlSigMpanlProfileTable.setStatus("mandatory")
_MpanlSigMpanlProfileEntry_Object = MibTableRow
mpanlSigMpanlProfileEntry = _MpanlSigMpanlProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 7, 11, 1)
)
mpanlSigMpanlProfileEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-MpaNetworkLinkMIB", "mpanlIndex"),
    (0, "Nortel-Magellan-Passport-MpaNetworkLinkMIB", "mpanlSigMpanlIndex"),
)
if mibBuilder.loadTexts:
    mpanlSigMpanlProfileEntry.setStatus("mandatory")


class _MpanlSigMpanlDteCustomerId_Type(Unsigned32):
    """Custom type mpanlSigMpanlDteCustomerId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 8191),
    )


_MpanlSigMpanlDteCustomerId_Type.__name__ = "Unsigned32"
_MpanlSigMpanlDteCustomerId_Object = MibTableColumn
mpanlSigMpanlDteCustomerId = _MpanlSigMpanlDteCustomerId_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 7, 11, 1, 1),
    _MpanlSigMpanlDteCustomerId_Type()
)
mpanlSigMpanlDteCustomerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlSigMpanlDteCustomerId.setStatus("mandatory")


class _MpanlSigMpanlDteNodeId_Type(Unsigned32):
    """Custom type mpanlSigMpanlDteNodeId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_MpanlSigMpanlDteNodeId_Type.__name__ = "Unsigned32"
_MpanlSigMpanlDteNodeId_Object = MibTableColumn
mpanlSigMpanlDteNodeId = _MpanlSigMpanlDteNodeId_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 7, 11, 1, 2),
    _MpanlSigMpanlDteNodeId_Type()
)
mpanlSigMpanlDteNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlSigMpanlDteNodeId.setStatus("mandatory")


class _MpanlSigMpanlDteComponentName_Type(AsciiString):
    """Custom type mpanlSigMpanlDteComponentName based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_MpanlSigMpanlDteComponentName_Type.__name__ = "AsciiString"
_MpanlSigMpanlDteComponentName_Object = MibTableColumn
mpanlSigMpanlDteComponentName = _MpanlSigMpanlDteComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 7, 11, 1, 3),
    _MpanlSigMpanlDteComponentName_Type()
)
mpanlSigMpanlDteComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlSigMpanlDteComponentName.setStatus("mandatory")


class _MpanlSigMpanlHighestDlci_Type(Unsigned32):
    """Custom type mpanlSigMpanlHighestDlci based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(17, 1007),
    )


_MpanlSigMpanlHighestDlci_Type.__name__ = "Unsigned32"
_MpanlSigMpanlHighestDlci_Object = MibTableColumn
mpanlSigMpanlHighestDlci = _MpanlSigMpanlHighestDlci_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 7, 11, 1, 4),
    _MpanlSigMpanlHighestDlci_Type()
)
mpanlSigMpanlHighestDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlSigMpanlHighestDlci.setStatus("mandatory")
_MpanlSigMpanlStatsTable_Object = MibTable
mpanlSigMpanlStatsTable = _MpanlSigMpanlStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 7, 12)
)
if mibBuilder.loadTexts:
    mpanlSigMpanlStatsTable.setStatus("mandatory")
_MpanlSigMpanlStatsEntry_Object = MibTableRow
mpanlSigMpanlStatsEntry = _MpanlSigMpanlStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 7, 12, 1)
)
mpanlSigMpanlStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-MpaNetworkLinkMIB", "mpanlIndex"),
    (0, "Nortel-Magellan-Passport-MpaNetworkLinkMIB", "mpanlSigMpanlIndex"),
)
if mibBuilder.loadTexts:
    mpanlSigMpanlStatsEntry.setStatus("mandatory")
_MpanlSigMpanlProtocolErrors_Type = Counter32
_MpanlSigMpanlProtocolErrors_Object = MibTableColumn
mpanlSigMpanlProtocolErrors = _MpanlSigMpanlProtocolErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 7, 12, 1, 1),
    _MpanlSigMpanlProtocolErrors_Type()
)
mpanlSigMpanlProtocolErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlSigMpanlProtocolErrors.setStatus("mandatory")
_MpanlSigMpanlSap0CommandsRx_Type = Counter32
_MpanlSigMpanlSap0CommandsRx_Object = MibTableColumn
mpanlSigMpanlSap0CommandsRx = _MpanlSigMpanlSap0CommandsRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 7, 12, 1, 2),
    _MpanlSigMpanlSap0CommandsRx_Type()
)
mpanlSigMpanlSap0CommandsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlSigMpanlSap0CommandsRx.setStatus("mandatory")
_MpanlSigMpanlSap0CommandsTx_Type = Counter32
_MpanlSigMpanlSap0CommandsTx_Object = MibTableColumn
mpanlSigMpanlSap0CommandsTx = _MpanlSigMpanlSap0CommandsTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 7, 12, 1, 3),
    _MpanlSigMpanlSap0CommandsTx_Type()
)
mpanlSigMpanlSap0CommandsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlSigMpanlSap0CommandsTx.setStatus("mandatory")
_MpanlSigMpanlSapXCommandsRx_Type = Counter32
_MpanlSigMpanlSapXCommandsRx_Object = MibTableColumn
mpanlSigMpanlSapXCommandsRx = _MpanlSigMpanlSapXCommandsRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 7, 12, 1, 4),
    _MpanlSigMpanlSapXCommandsRx_Type()
)
mpanlSigMpanlSapXCommandsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlSigMpanlSapXCommandsRx.setStatus("mandatory")
_MpanlSigMpanlSapXCommandsTx_Type = Counter32
_MpanlSigMpanlSapXCommandsTx_Object = MibTableColumn
mpanlSigMpanlSapXCommandsTx = _MpanlSigMpanlSapXCommandsTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 7, 12, 1, 5),
    _MpanlSigMpanlSapXCommandsTx_Type()
)
mpanlSigMpanlSapXCommandsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlSigMpanlSapXCommandsTx.setStatus("mandatory")
_MpanlSigMpanlLapfStatusTable_Object = MibTable
mpanlSigMpanlLapfStatusTable = _MpanlSigMpanlLapfStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 7, 13)
)
if mibBuilder.loadTexts:
    mpanlSigMpanlLapfStatusTable.setStatus("mandatory")
_MpanlSigMpanlLapfStatusEntry_Object = MibTableRow
mpanlSigMpanlLapfStatusEntry = _MpanlSigMpanlLapfStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 7, 13, 1)
)
mpanlSigMpanlLapfStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-MpaNetworkLinkMIB", "mpanlIndex"),
    (0, "Nortel-Magellan-Passport-MpaNetworkLinkMIB", "mpanlSigMpanlIndex"),
)
if mibBuilder.loadTexts:
    mpanlSigMpanlLapfStatusEntry.setStatus("mandatory")


class _MpanlSigMpanlCurrentState_Type(Integer32):
    """Custom type mpanlSigMpanlCurrentState based on Integer32"""
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


_MpanlSigMpanlCurrentState_Type.__name__ = "Integer32"
_MpanlSigMpanlCurrentState_Object = MibTableColumn
mpanlSigMpanlCurrentState = _MpanlSigMpanlCurrentState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 7, 13, 1, 1),
    _MpanlSigMpanlCurrentState_Type()
)
mpanlSigMpanlCurrentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlSigMpanlCurrentState.setStatus("mandatory")


class _MpanlSigMpanlLastStateChangeReason_Type(Integer32):
    """Custom type mpanlSigMpanlLastStateChangeReason based on Integer32"""
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


_MpanlSigMpanlLastStateChangeReason_Type.__name__ = "Integer32"
_MpanlSigMpanlLastStateChangeReason_Object = MibTableColumn
mpanlSigMpanlLastStateChangeReason = _MpanlSigMpanlLastStateChangeReason_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 7, 13, 1, 2),
    _MpanlSigMpanlLastStateChangeReason_Type()
)
mpanlSigMpanlLastStateChangeReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlSigMpanlLastStateChangeReason.setStatus("mandatory")


class _MpanlSigMpanlFrmrReceive_Type(HexString):
    """Custom type mpanlSigMpanlFrmrReceive based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_MpanlSigMpanlFrmrReceive_Type.__name__ = "HexString"
_MpanlSigMpanlFrmrReceive_Object = MibTableColumn
mpanlSigMpanlFrmrReceive = _MpanlSigMpanlFrmrReceive_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 7, 13, 1, 3),
    _MpanlSigMpanlFrmrReceive_Type()
)
mpanlSigMpanlFrmrReceive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlSigMpanlFrmrReceive.setStatus("mandatory")
_MpanlSigMpanlCurrentQueueSize_Type = Counter32
_MpanlSigMpanlCurrentQueueSize_Object = MibTableColumn
mpanlSigMpanlCurrentQueueSize = _MpanlSigMpanlCurrentQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 7, 13, 1, 4),
    _MpanlSigMpanlCurrentQueueSize_Type()
)
mpanlSigMpanlCurrentQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlSigMpanlCurrentQueueSize.setStatus("mandatory")
_MpanlSigMpanlLapfStatsTable_Object = MibTable
mpanlSigMpanlLapfStatsTable = _MpanlSigMpanlLapfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 7, 14)
)
if mibBuilder.loadTexts:
    mpanlSigMpanlLapfStatsTable.setStatus("mandatory")
_MpanlSigMpanlLapfStatsEntry_Object = MibTableRow
mpanlSigMpanlLapfStatsEntry = _MpanlSigMpanlLapfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 7, 14, 1)
)
mpanlSigMpanlLapfStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-MpaNetworkLinkMIB", "mpanlIndex"),
    (0, "Nortel-Magellan-Passport-MpaNetworkLinkMIB", "mpanlSigMpanlIndex"),
)
if mibBuilder.loadTexts:
    mpanlSigMpanlLapfStatsEntry.setStatus("mandatory")
_MpanlSigMpanlStateChange_Type = Counter32
_MpanlSigMpanlStateChange_Object = MibTableColumn
mpanlSigMpanlStateChange = _MpanlSigMpanlStateChange_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 7, 14, 1, 1),
    _MpanlSigMpanlStateChange_Type()
)
mpanlSigMpanlStateChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlSigMpanlStateChange.setStatus("mandatory")
_MpanlSigMpanlRemoteBusy_Type = Counter32
_MpanlSigMpanlRemoteBusy_Object = MibTableColumn
mpanlSigMpanlRemoteBusy = _MpanlSigMpanlRemoteBusy_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 7, 14, 1, 2),
    _MpanlSigMpanlRemoteBusy_Type()
)
mpanlSigMpanlRemoteBusy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlSigMpanlRemoteBusy.setStatus("mandatory")
_MpanlSigMpanlReceiveRejectFrame_Type = Counter32
_MpanlSigMpanlReceiveRejectFrame_Object = MibTableColumn
mpanlSigMpanlReceiveRejectFrame = _MpanlSigMpanlReceiveRejectFrame_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 7, 14, 1, 3),
    _MpanlSigMpanlReceiveRejectFrame_Type()
)
mpanlSigMpanlReceiveRejectFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlSigMpanlReceiveRejectFrame.setStatus("mandatory")
_MpanlSigMpanlAckTimeout_Type = Counter32
_MpanlSigMpanlAckTimeout_Object = MibTableColumn
mpanlSigMpanlAckTimeout = _MpanlSigMpanlAckTimeout_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 7, 14, 1, 4),
    _MpanlSigMpanlAckTimeout_Type()
)
mpanlSigMpanlAckTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlSigMpanlAckTimeout.setStatus("mandatory")
_MpanlSigMpanlIFramesTransmitted_Type = Counter32
_MpanlSigMpanlIFramesTransmitted_Object = MibTableColumn
mpanlSigMpanlIFramesTransmitted = _MpanlSigMpanlIFramesTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 7, 14, 1, 5),
    _MpanlSigMpanlIFramesTransmitted_Type()
)
mpanlSigMpanlIFramesTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlSigMpanlIFramesTransmitted.setStatus("mandatory")
_MpanlSigMpanlIFramesTxDiscarded_Type = Counter32
_MpanlSigMpanlIFramesTxDiscarded_Object = MibTableColumn
mpanlSigMpanlIFramesTxDiscarded = _MpanlSigMpanlIFramesTxDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 7, 14, 1, 6),
    _MpanlSigMpanlIFramesTxDiscarded_Type()
)
mpanlSigMpanlIFramesTxDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlSigMpanlIFramesTxDiscarded.setStatus("mandatory")
_MpanlSigMpanlIFramesReceived_Type = Counter32
_MpanlSigMpanlIFramesReceived_Object = MibTableColumn
mpanlSigMpanlIFramesReceived = _MpanlSigMpanlIFramesReceived_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 7, 14, 1, 7),
    _MpanlSigMpanlIFramesReceived_Type()
)
mpanlSigMpanlIFramesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlSigMpanlIFramesReceived.setStatus("mandatory")
_MpanlSigMpanlIFramesRcvdDiscarded_Type = Counter32
_MpanlSigMpanlIFramesRcvdDiscarded_Object = MibTableColumn
mpanlSigMpanlIFramesRcvdDiscarded = _MpanlSigMpanlIFramesRcvdDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 7, 14, 1, 8),
    _MpanlSigMpanlIFramesRcvdDiscarded_Type()
)
mpanlSigMpanlIFramesRcvdDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlSigMpanlIFramesRcvdDiscarded.setStatus("mandatory")
_MpanlLmi_ObjectIdentity = ObjectIdentity
mpanlLmi = _MpanlLmi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 8)
)
_MpanlLmiRowStatusTable_Object = MibTable
mpanlLmiRowStatusTable = _MpanlLmiRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 8, 1)
)
if mibBuilder.loadTexts:
    mpanlLmiRowStatusTable.setStatus("mandatory")
_MpanlLmiRowStatusEntry_Object = MibTableRow
mpanlLmiRowStatusEntry = _MpanlLmiRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 8, 1, 1)
)
mpanlLmiRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-MpaNetworkLinkMIB", "mpanlIndex"),
    (0, "Nortel-Magellan-Passport-MpaNetworkLinkMIB", "mpanlLmiIndex"),
)
if mibBuilder.loadTexts:
    mpanlLmiRowStatusEntry.setStatus("mandatory")
_MpanlLmiRowStatus_Type = RowStatus
_MpanlLmiRowStatus_Object = MibTableColumn
mpanlLmiRowStatus = _MpanlLmiRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 8, 1, 1, 1),
    _MpanlLmiRowStatus_Type()
)
mpanlLmiRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlLmiRowStatus.setStatus("mandatory")
_MpanlLmiComponentName_Type = DisplayString
_MpanlLmiComponentName_Object = MibTableColumn
mpanlLmiComponentName = _MpanlLmiComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 8, 1, 1, 2),
    _MpanlLmiComponentName_Type()
)
mpanlLmiComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlLmiComponentName.setStatus("mandatory")
_MpanlLmiStorageType_Type = StorageType
_MpanlLmiStorageType_Object = MibTableColumn
mpanlLmiStorageType = _MpanlLmiStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 8, 1, 1, 4),
    _MpanlLmiStorageType_Type()
)
mpanlLmiStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlLmiStorageType.setStatus("mandatory")
_MpanlLmiIndex_Type = NonReplicated
_MpanlLmiIndex_Object = MibTableColumn
mpanlLmiIndex = _MpanlLmiIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 8, 1, 1, 10),
    _MpanlLmiIndex_Type()
)
mpanlLmiIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mpanlLmiIndex.setStatus("mandatory")
_MpanlLmiParmsTable_Object = MibTable
mpanlLmiParmsTable = _MpanlLmiParmsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 8, 10)
)
if mibBuilder.loadTexts:
    mpanlLmiParmsTable.setStatus("mandatory")
_MpanlLmiParmsEntry_Object = MibTableRow
mpanlLmiParmsEntry = _MpanlLmiParmsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 8, 10, 1)
)
mpanlLmiParmsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-MpaNetworkLinkMIB", "mpanlIndex"),
    (0, "Nortel-Magellan-Passport-MpaNetworkLinkMIB", "mpanlLmiIndex"),
)
if mibBuilder.loadTexts:
    mpanlLmiParmsEntry.setStatus("mandatory")


class _MpanlLmiProcedures_Type(Integer32):
    """Custom type mpanlLmiProcedures based on Integer32"""
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


_MpanlLmiProcedures_Type.__name__ = "Integer32"
_MpanlLmiProcedures_Object = MibTableColumn
mpanlLmiProcedures = _MpanlLmiProcedures_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 8, 10, 1, 1),
    _MpanlLmiProcedures_Type()
)
mpanlLmiProcedures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlLmiProcedures.setStatus("mandatory")
_MpanlLmiStateTable_Object = MibTable
mpanlLmiStateTable = _MpanlLmiStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 8, 12)
)
if mibBuilder.loadTexts:
    mpanlLmiStateTable.setStatus("mandatory")
_MpanlLmiStateEntry_Object = MibTableRow
mpanlLmiStateEntry = _MpanlLmiStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 8, 12, 1)
)
mpanlLmiStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-MpaNetworkLinkMIB", "mpanlIndex"),
    (0, "Nortel-Magellan-Passport-MpaNetworkLinkMIB", "mpanlLmiIndex"),
)
if mibBuilder.loadTexts:
    mpanlLmiStateEntry.setStatus("mandatory")


class _MpanlLmiAdminState_Type(Integer32):
    """Custom type mpanlLmiAdminState based on Integer32"""
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


_MpanlLmiAdminState_Type.__name__ = "Integer32"
_MpanlLmiAdminState_Object = MibTableColumn
mpanlLmiAdminState = _MpanlLmiAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 8, 12, 1, 1),
    _MpanlLmiAdminState_Type()
)
mpanlLmiAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlLmiAdminState.setStatus("mandatory")


class _MpanlLmiOperationalState_Type(Integer32):
    """Custom type mpanlLmiOperationalState based on Integer32"""
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


_MpanlLmiOperationalState_Type.__name__ = "Integer32"
_MpanlLmiOperationalState_Object = MibTableColumn
mpanlLmiOperationalState = _MpanlLmiOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 8, 12, 1, 2),
    _MpanlLmiOperationalState_Type()
)
mpanlLmiOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlLmiOperationalState.setStatus("mandatory")


class _MpanlLmiUsageState_Type(Integer32):
    """Custom type mpanlLmiUsageState based on Integer32"""
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


_MpanlLmiUsageState_Type.__name__ = "Integer32"
_MpanlLmiUsageState_Object = MibTableColumn
mpanlLmiUsageState = _MpanlLmiUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 8, 12, 1, 3),
    _MpanlLmiUsageState_Type()
)
mpanlLmiUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlLmiUsageState.setStatus("mandatory")
_MpanlCidDataTable_Object = MibTable
mpanlCidDataTable = _MpanlCidDataTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 10)
)
if mibBuilder.loadTexts:
    mpanlCidDataTable.setStatus("mandatory")
_MpanlCidDataEntry_Object = MibTableRow
mpanlCidDataEntry = _MpanlCidDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 10, 1)
)
mpanlCidDataEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-MpaNetworkLinkMIB", "mpanlIndex"),
)
if mibBuilder.loadTexts:
    mpanlCidDataEntry.setStatus("mandatory")


class _MpanlCustomerIdentifier_Type(Unsigned32):
    """Custom type mpanlCustomerIdentifier based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 8191),
    )


_MpanlCustomerIdentifier_Type.__name__ = "Unsigned32"
_MpanlCustomerIdentifier_Object = MibTableColumn
mpanlCustomerIdentifier = _MpanlCustomerIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 10, 1, 1),
    _MpanlCustomerIdentifier_Type()
)
mpanlCustomerIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlCustomerIdentifier.setStatus("mandatory")
_MpanlProvTable_Object = MibTable
mpanlProvTable = _MpanlProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 12)
)
if mibBuilder.loadTexts:
    mpanlProvTable.setStatus("mandatory")
_MpanlProvEntry_Object = MibTableRow
mpanlProvEntry = _MpanlProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 12, 1)
)
mpanlProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-MpaNetworkLinkMIB", "mpanlIndex"),
)
if mibBuilder.loadTexts:
    mpanlProvEntry.setStatus("mandatory")


class _MpanlCommentText_Type(AsciiString):
    """Custom type mpanlCommentText based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_MpanlCommentText_Type.__name__ = "AsciiString"
_MpanlCommentText_Object = MibTableColumn
mpanlCommentText = _MpanlCommentText_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 12, 1, 1),
    _MpanlCommentText_Type()
)
mpanlCommentText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpanlCommentText.setStatus("mandatory")
_MpanlEmissionPriorityQsTable_Object = MibTable
mpanlEmissionPriorityQsTable = _MpanlEmissionPriorityQsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 13)
)
if mibBuilder.loadTexts:
    mpanlEmissionPriorityQsTable.setStatus("mandatory")
_MpanlEmissionPriorityQsEntry_Object = MibTableRow
mpanlEmissionPriorityQsEntry = _MpanlEmissionPriorityQsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 13, 1)
)
mpanlEmissionPriorityQsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-MpaNetworkLinkMIB", "mpanlIndex"),
)
if mibBuilder.loadTexts:
    mpanlEmissionPriorityQsEntry.setStatus("mandatory")


class _MpanlNumberOfEmissionQs_Type(Unsigned32):
    """Custom type mpanlNumberOfEmissionQs based on Unsigned32"""
    defaultValue = 4

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 2),
        ValueRangeConstraint(4, 4),
    )


_MpanlNumberOfEmissionQs_Type.__name__ = "Unsigned32"
_MpanlNumberOfEmissionQs_Object = MibTableColumn
mpanlNumberOfEmissionQs = _MpanlNumberOfEmissionQs_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 13, 1, 1),
    _MpanlNumberOfEmissionQs_Type()
)
mpanlNumberOfEmissionQs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlNumberOfEmissionQs.setStatus("mandatory")
_MpanlStateTable_Object = MibTable
mpanlStateTable = _MpanlStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 14)
)
if mibBuilder.loadTexts:
    mpanlStateTable.setStatus("mandatory")
_MpanlStateEntry_Object = MibTableRow
mpanlStateEntry = _MpanlStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 14, 1)
)
mpanlStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-MpaNetworkLinkMIB", "mpanlIndex"),
)
if mibBuilder.loadTexts:
    mpanlStateEntry.setStatus("mandatory")


class _MpanlAdminState_Type(Integer32):
    """Custom type mpanlAdminState based on Integer32"""
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


_MpanlAdminState_Type.__name__ = "Integer32"
_MpanlAdminState_Object = MibTableColumn
mpanlAdminState = _MpanlAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 14, 1, 1),
    _MpanlAdminState_Type()
)
mpanlAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlAdminState.setStatus("mandatory")


class _MpanlOperationalState_Type(Integer32):
    """Custom type mpanlOperationalState based on Integer32"""
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


_MpanlOperationalState_Type.__name__ = "Integer32"
_MpanlOperationalState_Object = MibTableColumn
mpanlOperationalState = _MpanlOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 14, 1, 2),
    _MpanlOperationalState_Type()
)
mpanlOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlOperationalState.setStatus("mandatory")


class _MpanlUsageState_Type(Integer32):
    """Custom type mpanlUsageState based on Integer32"""
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


_MpanlUsageState_Type.__name__ = "Integer32"
_MpanlUsageState_Object = MibTableColumn
mpanlUsageState = _MpanlUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 14, 1, 3),
    _MpanlUsageState_Type()
)
mpanlUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlUsageState.setStatus("mandatory")


class _MpanlAvailabilityStatus_Type(OctetString):
    """Custom type mpanlAvailabilityStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_MpanlAvailabilityStatus_Type.__name__ = "OctetString"
_MpanlAvailabilityStatus_Object = MibTableColumn
mpanlAvailabilityStatus = _MpanlAvailabilityStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 14, 1, 4),
    _MpanlAvailabilityStatus_Type()
)
mpanlAvailabilityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlAvailabilityStatus.setStatus("mandatory")


class _MpanlProceduralStatus_Type(OctetString):
    """Custom type mpanlProceduralStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MpanlProceduralStatus_Type.__name__ = "OctetString"
_MpanlProceduralStatus_Object = MibTableColumn
mpanlProceduralStatus = _MpanlProceduralStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 14, 1, 5),
    _MpanlProceduralStatus_Type()
)
mpanlProceduralStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlProceduralStatus.setStatus("mandatory")


class _MpanlControlStatus_Type(OctetString):
    """Custom type mpanlControlStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MpanlControlStatus_Type.__name__ = "OctetString"
_MpanlControlStatus_Object = MibTableColumn
mpanlControlStatus = _MpanlControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 14, 1, 6),
    _MpanlControlStatus_Type()
)
mpanlControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlControlStatus.setStatus("mandatory")


class _MpanlAlarmStatus_Type(OctetString):
    """Custom type mpanlAlarmStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MpanlAlarmStatus_Type.__name__ = "OctetString"
_MpanlAlarmStatus_Object = MibTableColumn
mpanlAlarmStatus = _MpanlAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 14, 1, 7),
    _MpanlAlarmStatus_Type()
)
mpanlAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlAlarmStatus.setStatus("mandatory")


class _MpanlStandbyStatus_Type(Integer32):
    """Custom type mpanlStandbyStatus based on Integer32"""
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


_MpanlStandbyStatus_Type.__name__ = "Integer32"
_MpanlStandbyStatus_Object = MibTableColumn
mpanlStandbyStatus = _MpanlStandbyStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 14, 1, 8),
    _MpanlStandbyStatus_Type()
)
mpanlStandbyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlStandbyStatus.setStatus("mandatory")


class _MpanlUnknownStatus_Type(Integer32):
    """Custom type mpanlUnknownStatus based on Integer32"""
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


_MpanlUnknownStatus_Type.__name__ = "Integer32"
_MpanlUnknownStatus_Object = MibTableColumn
mpanlUnknownStatus = _MpanlUnknownStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 14, 1, 9),
    _MpanlUnknownStatus_Type()
)
mpanlUnknownStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlUnknownStatus.setStatus("mandatory")
_MpanlStatsTable_Object = MibTable
mpanlStatsTable = _MpanlStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 16)
)
if mibBuilder.loadTexts:
    mpanlStatsTable.setStatus("mandatory")
_MpanlStatsEntry_Object = MibTableRow
mpanlStatsEntry = _MpanlStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 16, 1)
)
mpanlStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-MpaNetworkLinkMIB", "mpanlIndex"),
)
if mibBuilder.loadTexts:
    mpanlStatsEntry.setStatus("mandatory")


class _MpanlLastUnknownDlci_Type(Unsigned32):
    """Custom type mpanlLastUnknownDlci based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_MpanlLastUnknownDlci_Type.__name__ = "Unsigned32"
_MpanlLastUnknownDlci_Object = MibTableColumn
mpanlLastUnknownDlci = _MpanlLastUnknownDlci_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 16, 1, 1),
    _MpanlLastUnknownDlci_Type()
)
mpanlLastUnknownDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlLastUnknownDlci.setStatus("mandatory")
_MpanlUnknownDlciFramesFromIf_Type = Counter32
_MpanlUnknownDlciFramesFromIf_Object = MibTableColumn
mpanlUnknownDlciFramesFromIf = _MpanlUnknownDlciFramesFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 16, 1, 2),
    _MpanlUnknownDlciFramesFromIf_Type()
)
mpanlUnknownDlciFramesFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlUnknownDlciFramesFromIf.setStatus("mandatory")
_MpanlInvalidHeaderFramesFromIf_Type = Counter32
_MpanlInvalidHeaderFramesFromIf_Object = MibTableColumn
mpanlInvalidHeaderFramesFromIf = _MpanlInvalidHeaderFramesFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 16, 1, 3),
    _MpanlInvalidHeaderFramesFromIf_Type()
)
mpanlInvalidHeaderFramesFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlInvalidHeaderFramesFromIf.setStatus("mandatory")
_MpanlTrafficStatsTable_Object = MibTable
mpanlTrafficStatsTable = _MpanlTrafficStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 17)
)
if mibBuilder.loadTexts:
    mpanlTrafficStatsTable.setStatus("mandatory")
_MpanlTrafficStatsEntry_Object = MibTableRow
mpanlTrafficStatsEntry = _MpanlTrafficStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 17, 1)
)
mpanlTrafficStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-MpaNetworkLinkMIB", "mpanlIndex"),
)
if mibBuilder.loadTexts:
    mpanlTrafficStatsEntry.setStatus("mandatory")


class _MpanlFrmToIf_Type(Unsigned32):
    """Custom type mpanlFrmToIf based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MpanlFrmToIf_Type.__name__ = "Unsigned32"
_MpanlFrmToIf_Object = MibTableColumn
mpanlFrmToIf = _MpanlFrmToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 17, 1, 1),
    _MpanlFrmToIf_Type()
)
mpanlFrmToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlFrmToIf.setStatus("mandatory")


class _MpanlOctetToIf_Type(Unsigned32):
    """Custom type mpanlOctetToIf based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MpanlOctetToIf_Type.__name__ = "Unsigned32"
_MpanlOctetToIf_Object = MibTableColumn
mpanlOctetToIf = _MpanlOctetToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 17, 1, 2),
    _MpanlOctetToIf_Type()
)
mpanlOctetToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlOctetToIf.setStatus("mandatory")


class _MpanlFrmFromIf_Type(Unsigned32):
    """Custom type mpanlFrmFromIf based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MpanlFrmFromIf_Type.__name__ = "Unsigned32"
_MpanlFrmFromIf_Object = MibTableColumn
mpanlFrmFromIf = _MpanlFrmFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 17, 1, 3),
    _MpanlFrmFromIf_Type()
)
mpanlFrmFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlFrmFromIf.setStatus("mandatory")


class _MpanlOctetFromIf_Type(Unsigned32):
    """Custom type mpanlOctetFromIf based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MpanlOctetFromIf_Type.__name__ = "Unsigned32"
_MpanlOctetFromIf_Object = MibTableColumn
mpanlOctetFromIf = _MpanlOctetFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 17, 1, 4),
    _MpanlOctetFromIf_Type()
)
mpanlOctetFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlOctetFromIf.setStatus("mandatory")
_MpanlVoFr_ObjectIdentity = ObjectIdentity
mpanlVoFr = _MpanlVoFr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 18)
)
_MpanlVoFrRowStatusTable_Object = MibTable
mpanlVoFrRowStatusTable = _MpanlVoFrRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 18, 1)
)
if mibBuilder.loadTexts:
    mpanlVoFrRowStatusTable.setStatus("mandatory")
_MpanlVoFrRowStatusEntry_Object = MibTableRow
mpanlVoFrRowStatusEntry = _MpanlVoFrRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 18, 1, 1)
)
mpanlVoFrRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-MpaNetworkLinkMIB", "mpanlIndex"),
    (0, "Nortel-Magellan-Passport-MpaNetworkLinkMIB", "mpanlVoFrIndex"),
)
if mibBuilder.loadTexts:
    mpanlVoFrRowStatusEntry.setStatus("mandatory")
_MpanlVoFrRowStatus_Type = RowStatus
_MpanlVoFrRowStatus_Object = MibTableColumn
mpanlVoFrRowStatus = _MpanlVoFrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 18, 1, 1, 1),
    _MpanlVoFrRowStatus_Type()
)
mpanlVoFrRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlVoFrRowStatus.setStatus("mandatory")
_MpanlVoFrComponentName_Type = DisplayString
_MpanlVoFrComponentName_Object = MibTableColumn
mpanlVoFrComponentName = _MpanlVoFrComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 18, 1, 1, 2),
    _MpanlVoFrComponentName_Type()
)
mpanlVoFrComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlVoFrComponentName.setStatus("mandatory")
_MpanlVoFrStorageType_Type = StorageType
_MpanlVoFrStorageType_Object = MibTableColumn
mpanlVoFrStorageType = _MpanlVoFrStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 18, 1, 1, 4),
    _MpanlVoFrStorageType_Type()
)
mpanlVoFrStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlVoFrStorageType.setStatus("mandatory")
_MpanlVoFrIndex_Type = NonReplicated
_MpanlVoFrIndex_Object = MibTableColumn
mpanlVoFrIndex = _MpanlVoFrIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 18, 1, 1, 10),
    _MpanlVoFrIndex_Type()
)
mpanlVoFrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mpanlVoFrIndex.setStatus("mandatory")
_MpanlVoFrOperTable_Object = MibTable
mpanlVoFrOperTable = _MpanlVoFrOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 18, 10)
)
if mibBuilder.loadTexts:
    mpanlVoFrOperTable.setStatus("mandatory")
_MpanlVoFrOperEntry_Object = MibTableRow
mpanlVoFrOperEntry = _MpanlVoFrOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 18, 10, 1)
)
mpanlVoFrOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-MpaNetworkLinkMIB", "mpanlIndex"),
    (0, "Nortel-Magellan-Passport-MpaNetworkLinkMIB", "mpanlVoFrIndex"),
)
if mibBuilder.loadTexts:
    mpanlVoFrOperEntry.setStatus("mandatory")
_MpanlVoFrMaximumFrameSize_Type = Counter32
_MpanlVoFrMaximumFrameSize_Object = MibTableColumn
mpanlVoFrMaximumFrameSize = _MpanlVoFrMaximumFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 18, 10, 1, 1),
    _MpanlVoFrMaximumFrameSize_Type()
)
mpanlVoFrMaximumFrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlVoFrMaximumFrameSize.setStatus("mandatory")
_MpanlVoFrTransmitInformationRate_Type = Counter32
_MpanlVoFrTransmitInformationRate_Object = MibTableColumn
mpanlVoFrTransmitInformationRate = _MpanlVoFrTransmitInformationRate_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 18, 10, 1, 2),
    _MpanlVoFrTransmitInformationRate_Type()
)
mpanlVoFrTransmitInformationRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlVoFrTransmitInformationRate.setStatus("mandatory")
_MpanlVoFrStatsTable_Object = MibTable
mpanlVoFrStatsTable = _MpanlVoFrStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 18, 11)
)
if mibBuilder.loadTexts:
    mpanlVoFrStatsTable.setStatus("mandatory")
_MpanlVoFrStatsEntry_Object = MibTableRow
mpanlVoFrStatsEntry = _MpanlVoFrStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 18, 11, 1)
)
mpanlVoFrStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-MpaNetworkLinkMIB", "mpanlIndex"),
    (0, "Nortel-Magellan-Passport-MpaNetworkLinkMIB", "mpanlVoFrIndex"),
)
if mibBuilder.loadTexts:
    mpanlVoFrStatsEntry.setStatus("mandatory")
_MpanlVoFrFragmentedHighestPriorityFrames_Type = Counter32
_MpanlVoFrFragmentedHighestPriorityFrames_Object = MibTableColumn
mpanlVoFrFragmentedHighestPriorityFrames = _MpanlVoFrFragmentedHighestPriorityFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 18, 11, 1, 1),
    _MpanlVoFrFragmentedHighestPriorityFrames_Type()
)
mpanlVoFrFragmentedHighestPriorityFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlVoFrFragmentedHighestPriorityFrames.setStatus("mandatory")
_MpanlVoFrLostFragmentsFromIf_Type = Counter32
_MpanlVoFrLostFragmentsFromIf_Object = MibTableColumn
mpanlVoFrLostFragmentsFromIf = _MpanlVoFrLostFragmentsFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 18, 11, 1, 5),
    _MpanlVoFrLostFragmentsFromIf_Type()
)
mpanlVoFrLostFragmentsFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlVoFrLostFragmentsFromIf.setStatus("mandatory")
_MpanlVoFrProtocolViolationsFromIf_Type = Counter32
_MpanlVoFrProtocolViolationsFromIf_Object = MibTableColumn
mpanlVoFrProtocolViolationsFromIf = _MpanlVoFrProtocolViolationsFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 18, 11, 1, 6),
    _MpanlVoFrProtocolViolationsFromIf_Type()
)
mpanlVoFrProtocolViolationsFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlVoFrProtocolViolationsFromIf.setStatus("mandatory")
_MpanlFrMuxSetup_ObjectIdentity = ObjectIdentity
mpanlFrMuxSetup = _MpanlFrMuxSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 19)
)
_MpanlFrMuxSetupRowStatusTable_Object = MibTable
mpanlFrMuxSetupRowStatusTable = _MpanlFrMuxSetupRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 19, 1)
)
if mibBuilder.loadTexts:
    mpanlFrMuxSetupRowStatusTable.setStatus("mandatory")
_MpanlFrMuxSetupRowStatusEntry_Object = MibTableRow
mpanlFrMuxSetupRowStatusEntry = _MpanlFrMuxSetupRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 19, 1, 1)
)
mpanlFrMuxSetupRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-MpaNetworkLinkMIB", "mpanlIndex"),
    (0, "Nortel-Magellan-Passport-MpaNetworkLinkMIB", "mpanlFrMuxSetupIndex"),
)
if mibBuilder.loadTexts:
    mpanlFrMuxSetupRowStatusEntry.setStatus("mandatory")
_MpanlFrMuxSetupRowStatus_Type = RowStatus
_MpanlFrMuxSetupRowStatus_Object = MibTableColumn
mpanlFrMuxSetupRowStatus = _MpanlFrMuxSetupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 19, 1, 1, 1),
    _MpanlFrMuxSetupRowStatus_Type()
)
mpanlFrMuxSetupRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpanlFrMuxSetupRowStatus.setStatus("mandatory")
_MpanlFrMuxSetupComponentName_Type = DisplayString
_MpanlFrMuxSetupComponentName_Object = MibTableColumn
mpanlFrMuxSetupComponentName = _MpanlFrMuxSetupComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 19, 1, 1, 2),
    _MpanlFrMuxSetupComponentName_Type()
)
mpanlFrMuxSetupComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlFrMuxSetupComponentName.setStatus("mandatory")
_MpanlFrMuxSetupStorageType_Type = StorageType
_MpanlFrMuxSetupStorageType_Object = MibTableColumn
mpanlFrMuxSetupStorageType = _MpanlFrMuxSetupStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 19, 1, 1, 4),
    _MpanlFrMuxSetupStorageType_Type()
)
mpanlFrMuxSetupStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlFrMuxSetupStorageType.setStatus("mandatory")
_MpanlFrMuxSetupIndex_Type = NonReplicated
_MpanlFrMuxSetupIndex_Object = MibTableColumn
mpanlFrMuxSetupIndex = _MpanlFrMuxSetupIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 19, 1, 1, 10),
    _MpanlFrMuxSetupIndex_Type()
)
mpanlFrMuxSetupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mpanlFrMuxSetupIndex.setStatus("mandatory")
_MpanlFrMuxSetupPvcSetup_ObjectIdentity = ObjectIdentity
mpanlFrMuxSetupPvcSetup = _MpanlFrMuxSetupPvcSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 19, 2)
)
_MpanlFrMuxSetupPvcSetupRowStatusTable_Object = MibTable
mpanlFrMuxSetupPvcSetupRowStatusTable = _MpanlFrMuxSetupPvcSetupRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 19, 2, 1)
)
if mibBuilder.loadTexts:
    mpanlFrMuxSetupPvcSetupRowStatusTable.setStatus("mandatory")
_MpanlFrMuxSetupPvcSetupRowStatusEntry_Object = MibTableRow
mpanlFrMuxSetupPvcSetupRowStatusEntry = _MpanlFrMuxSetupPvcSetupRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 19, 2, 1, 1)
)
mpanlFrMuxSetupPvcSetupRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-MpaNetworkLinkMIB", "mpanlIndex"),
    (0, "Nortel-Magellan-Passport-MpaNetworkLinkMIB", "mpanlFrMuxSetupIndex"),
    (0, "Nortel-Magellan-Passport-MpaNetworkLinkMIB", "mpanlFrMuxSetupPvcSetupIndex"),
)
if mibBuilder.loadTexts:
    mpanlFrMuxSetupPvcSetupRowStatusEntry.setStatus("mandatory")
_MpanlFrMuxSetupPvcSetupRowStatus_Type = RowStatus
_MpanlFrMuxSetupPvcSetupRowStatus_Object = MibTableColumn
mpanlFrMuxSetupPvcSetupRowStatus = _MpanlFrMuxSetupPvcSetupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 19, 2, 1, 1, 1),
    _MpanlFrMuxSetupPvcSetupRowStatus_Type()
)
mpanlFrMuxSetupPvcSetupRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlFrMuxSetupPvcSetupRowStatus.setStatus("mandatory")
_MpanlFrMuxSetupPvcSetupComponentName_Type = DisplayString
_MpanlFrMuxSetupPvcSetupComponentName_Object = MibTableColumn
mpanlFrMuxSetupPvcSetupComponentName = _MpanlFrMuxSetupPvcSetupComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 19, 2, 1, 1, 2),
    _MpanlFrMuxSetupPvcSetupComponentName_Type()
)
mpanlFrMuxSetupPvcSetupComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlFrMuxSetupPvcSetupComponentName.setStatus("mandatory")
_MpanlFrMuxSetupPvcSetupStorageType_Type = StorageType
_MpanlFrMuxSetupPvcSetupStorageType_Object = MibTableColumn
mpanlFrMuxSetupPvcSetupStorageType = _MpanlFrMuxSetupPvcSetupStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 19, 2, 1, 1, 4),
    _MpanlFrMuxSetupPvcSetupStorageType_Type()
)
mpanlFrMuxSetupPvcSetupStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlFrMuxSetupPvcSetupStorageType.setStatus("mandatory")
_MpanlFrMuxSetupPvcSetupIndex_Type = NonReplicated
_MpanlFrMuxSetupPvcSetupIndex_Object = MibTableColumn
mpanlFrMuxSetupPvcSetupIndex = _MpanlFrMuxSetupPvcSetupIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 19, 2, 1, 1, 10),
    _MpanlFrMuxSetupPvcSetupIndex_Type()
)
mpanlFrMuxSetupPvcSetupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mpanlFrMuxSetupPvcSetupIndex.setStatus("mandatory")
_MpanlFrMuxSetupPvcSetupProvTable_Object = MibTable
mpanlFrMuxSetupPvcSetupProvTable = _MpanlFrMuxSetupPvcSetupProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 19, 2, 10)
)
if mibBuilder.loadTexts:
    mpanlFrMuxSetupPvcSetupProvTable.setStatus("mandatory")
_MpanlFrMuxSetupPvcSetupProvEntry_Object = MibTableRow
mpanlFrMuxSetupPvcSetupProvEntry = _MpanlFrMuxSetupPvcSetupProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 19, 2, 10, 1)
)
mpanlFrMuxSetupPvcSetupProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-MpaNetworkLinkMIB", "mpanlIndex"),
    (0, "Nortel-Magellan-Passport-MpaNetworkLinkMIB", "mpanlFrMuxSetupIndex"),
    (0, "Nortel-Magellan-Passport-MpaNetworkLinkMIB", "mpanlFrMuxSetupPvcSetupIndex"),
)
if mibBuilder.loadTexts:
    mpanlFrMuxSetupPvcSetupProvEntry.setStatus("mandatory")
_MpanlFrMuxSetupPvcSetupDlciName_Type = Link
_MpanlFrMuxSetupPvcSetupDlciName_Object = MibTableColumn
mpanlFrMuxSetupPvcSetupDlciName = _MpanlFrMuxSetupPvcSetupDlciName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 19, 2, 10, 1, 1),
    _MpanlFrMuxSetupPvcSetupDlciName_Type()
)
mpanlFrMuxSetupPvcSetupDlciName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpanlFrMuxSetupPvcSetupDlciName.setStatus("mandatory")
_MpanlFrMuxSetupOpTable_Object = MibTable
mpanlFrMuxSetupOpTable = _MpanlFrMuxSetupOpTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 19, 11)
)
if mibBuilder.loadTexts:
    mpanlFrMuxSetupOpTable.setStatus("mandatory")
_MpanlFrMuxSetupOpEntry_Object = MibTableRow
mpanlFrMuxSetupOpEntry = _MpanlFrMuxSetupOpEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 19, 11, 1)
)
mpanlFrMuxSetupOpEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-MpaNetworkLinkMIB", "mpanlIndex"),
    (0, "Nortel-Magellan-Passport-MpaNetworkLinkMIB", "mpanlFrMuxSetupIndex"),
)
if mibBuilder.loadTexts:
    mpanlFrMuxSetupOpEntry.setStatus("mandatory")


class _MpanlFrMuxSetupCommittedInformationRate_Type(Unsigned32):
    """Custom type mpanlFrMuxSetupCommittedInformationRate based on Unsigned32"""
    defaultValue = 16000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16000, 4294967295),
    )


_MpanlFrMuxSetupCommittedInformationRate_Type.__name__ = "Unsigned32"
_MpanlFrMuxSetupCommittedInformationRate_Object = MibTableColumn
mpanlFrMuxSetupCommittedInformationRate = _MpanlFrMuxSetupCommittedInformationRate_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 19, 11, 1, 1),
    _MpanlFrMuxSetupCommittedInformationRate_Type()
)
mpanlFrMuxSetupCommittedInformationRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlFrMuxSetupCommittedInformationRate.setStatus("mandatory")
_MpanlFrMuxSetupDlciCompName_Type = RowPointer
_MpanlFrMuxSetupDlciCompName_Object = MibTableColumn
mpanlFrMuxSetupDlciCompName = _MpanlFrMuxSetupDlciCompName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 19, 11, 1, 2),
    _MpanlFrMuxSetupDlciCompName_Type()
)
mpanlFrMuxSetupDlciCompName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlFrMuxSetupDlciCompName.setStatus("mandatory")
_MpanlIsdn_ObjectIdentity = ObjectIdentity
mpanlIsdn = _MpanlIsdn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 22)
)
_MpanlIsdnRowStatusTable_Object = MibTable
mpanlIsdnRowStatusTable = _MpanlIsdnRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 22, 1)
)
if mibBuilder.loadTexts:
    mpanlIsdnRowStatusTable.setStatus("mandatory")
_MpanlIsdnRowStatusEntry_Object = MibTableRow
mpanlIsdnRowStatusEntry = _MpanlIsdnRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 22, 1, 1)
)
mpanlIsdnRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-MpaNetworkLinkMIB", "mpanlIndex"),
    (0, "Nortel-Magellan-Passport-MpaNetworkLinkMIB", "mpanlIsdnIndex"),
)
if mibBuilder.loadTexts:
    mpanlIsdnRowStatusEntry.setStatus("mandatory")
_MpanlIsdnRowStatus_Type = RowStatus
_MpanlIsdnRowStatus_Object = MibTableColumn
mpanlIsdnRowStatus = _MpanlIsdnRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 22, 1, 1, 1),
    _MpanlIsdnRowStatus_Type()
)
mpanlIsdnRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpanlIsdnRowStatus.setStatus("mandatory")
_MpanlIsdnComponentName_Type = DisplayString
_MpanlIsdnComponentName_Object = MibTableColumn
mpanlIsdnComponentName = _MpanlIsdnComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 22, 1, 1, 2),
    _MpanlIsdnComponentName_Type()
)
mpanlIsdnComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlIsdnComponentName.setStatus("mandatory")
_MpanlIsdnStorageType_Type = StorageType
_MpanlIsdnStorageType_Object = MibTableColumn
mpanlIsdnStorageType = _MpanlIsdnStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 22, 1, 1, 4),
    _MpanlIsdnStorageType_Type()
)
mpanlIsdnStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlIsdnStorageType.setStatus("mandatory")
_MpanlIsdnIndex_Type = NonReplicated
_MpanlIsdnIndex_Object = MibTableColumn
mpanlIsdnIndex = _MpanlIsdnIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 22, 1, 1, 10),
    _MpanlIsdnIndex_Type()
)
mpanlIsdnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mpanlIsdnIndex.setStatus("mandatory")
_MpanlIsdnProvTable_Object = MibTable
mpanlIsdnProvTable = _MpanlIsdnProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 22, 11)
)
if mibBuilder.loadTexts:
    mpanlIsdnProvTable.setStatus("mandatory")
_MpanlIsdnProvEntry_Object = MibTableRow
mpanlIsdnProvEntry = _MpanlIsdnProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 22, 11, 1)
)
mpanlIsdnProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-MpaNetworkLinkMIB", "mpanlIndex"),
    (0, "Nortel-Magellan-Passport-MpaNetworkLinkMIB", "mpanlIsdnIndex"),
)
if mibBuilder.loadTexts:
    mpanlIsdnProvEntry.setStatus("mandatory")


class _MpanlIsdnT320_Type(Unsigned32):
    """Custom type mpanlIsdnT320 based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MpanlIsdnT320_Type.__name__ = "Unsigned32"
_MpanlIsdnT320_Object = MibTableColumn
mpanlIsdnT320 = _MpanlIsdnT320_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 22, 11, 1, 1),
    _MpanlIsdnT320_Type()
)
mpanlIsdnT320.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpanlIsdnT320.setStatus("mandatory")


class _MpanlIsdnAddressSignalling_Type(Integer32):
    """Custom type mpanlIsdnAddressSignalling based on Integer32"""
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


_MpanlIsdnAddressSignalling_Type.__name__ = "Integer32"
_MpanlIsdnAddressSignalling_Object = MibTableColumn
mpanlIsdnAddressSignalling = _MpanlIsdnAddressSignalling_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 22, 11, 1, 2),
    _MpanlIsdnAddressSignalling_Type()
)
mpanlIsdnAddressSignalling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpanlIsdnAddressSignalling.setStatus("mandatory")
_MpanlIsdnOperTable_Object = MibTable
mpanlIsdnOperTable = _MpanlIsdnOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 22, 12)
)
if mibBuilder.loadTexts:
    mpanlIsdnOperTable.setStatus("mandatory")
_MpanlIsdnOperEntry_Object = MibTableRow
mpanlIsdnOperEntry = _MpanlIsdnOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 22, 12, 1)
)
mpanlIsdnOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-MpaNetworkLinkMIB", "mpanlIndex"),
    (0, "Nortel-Magellan-Passport-MpaNetworkLinkMIB", "mpanlIsdnIndex"),
)
if mibBuilder.loadTexts:
    mpanlIsdnOperEntry.setStatus("mandatory")


class _MpanlIsdnDataSigChan_Type(Integer32):
    """Custom type mpanlIsdnDataSigChan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_MpanlIsdnDataSigChan_Type.__name__ = "Integer32"
_MpanlIsdnDataSigChan_Object = MibTableColumn
mpanlIsdnDataSigChan = _MpanlIsdnDataSigChan_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 22, 12, 1, 1),
    _MpanlIsdnDataSigChan_Type()
)
mpanlIsdnDataSigChan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlIsdnDataSigChan.setStatus("mandatory")


class _MpanlIsdnBChannelState_Type(Integer32):
    """Custom type mpanlIsdnBChannelState based on Integer32"""
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


_MpanlIsdnBChannelState_Type.__name__ = "Integer32"
_MpanlIsdnBChannelState_Object = MibTableColumn
mpanlIsdnBChannelState = _MpanlIsdnBChannelState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 22, 12, 1, 2),
    _MpanlIsdnBChannelState_Type()
)
mpanlIsdnBChannelState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlIsdnBChannelState.setStatus("mandatory")


class _MpanlIsdnLastUsedCgpn_Type(DigitString):
    """Custom type mpanlIsdnLastUsedCgpn based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_MpanlIsdnLastUsedCgpn_Type.__name__ = "DigitString"
_MpanlIsdnLastUsedCgpn_Object = MibTableColumn
mpanlIsdnLastUsedCgpn = _MpanlIsdnLastUsedCgpn_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 22, 12, 1, 3),
    _MpanlIsdnLastUsedCgpn_Type()
)
mpanlIsdnLastUsedCgpn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlIsdnLastUsedCgpn.setStatus("mandatory")


class _MpanlIsdnBChanIntState_Type(Integer32):
    """Custom type mpanlIsdnBChanIntState based on Integer32"""
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


_MpanlIsdnBChanIntState_Type.__name__ = "Integer32"
_MpanlIsdnBChanIntState_Object = MibTableColumn
mpanlIsdnBChanIntState = _MpanlIsdnBChanIntState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 22, 12, 1, 4),
    _MpanlIsdnBChanIntState_Type()
)
mpanlIsdnBChanIntState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlIsdnBChanIntState.setStatus("mandatory")
_MpanlIsdnActiveVirtualCircuitsCount_Type = Counter32
_MpanlIsdnActiveVirtualCircuitsCount_Object = MibTableColumn
mpanlIsdnActiveVirtualCircuitsCount = _MpanlIsdnActiveVirtualCircuitsCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 22, 12, 1, 5),
    _MpanlIsdnActiveVirtualCircuitsCount_Type()
)
mpanlIsdnActiveVirtualCircuitsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlIsdnActiveVirtualCircuitsCount.setStatus("mandatory")
_MpanlIfEntryTable_Object = MibTable
mpanlIfEntryTable = _MpanlIfEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 23)
)
if mibBuilder.loadTexts:
    mpanlIfEntryTable.setStatus("mandatory")
_MpanlIfEntryEntry_Object = MibTableRow
mpanlIfEntryEntry = _MpanlIfEntryEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 23, 1)
)
mpanlIfEntryEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-MpaNetworkLinkMIB", "mpanlIndex"),
)
if mibBuilder.loadTexts:
    mpanlIfEntryEntry.setStatus("mandatory")


class _MpanlIfAdminStatus_Type(Integer32):
    """Custom type mpanlIfAdminStatus based on Integer32"""
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


_MpanlIfAdminStatus_Type.__name__ = "Integer32"
_MpanlIfAdminStatus_Object = MibTableColumn
mpanlIfAdminStatus = _MpanlIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 23, 1, 1),
    _MpanlIfAdminStatus_Type()
)
mpanlIfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpanlIfAdminStatus.setStatus("mandatory")


class _MpanlIfIndex_Type(InterfaceIndex):
    """Custom type mpanlIfIndex based on InterfaceIndex"""
    subtypeSpec = InterfaceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MpanlIfIndex_Type.__name__ = "InterfaceIndex"
_MpanlIfIndex_Object = MibTableColumn
mpanlIfIndex = _MpanlIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 23, 1, 2),
    _MpanlIfIndex_Type()
)
mpanlIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlIfIndex.setStatus("mandatory")
_MpanlOperStatusTable_Object = MibTable
mpanlOperStatusTable = _MpanlOperStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 24)
)
if mibBuilder.loadTexts:
    mpanlOperStatusTable.setStatus("mandatory")
_MpanlOperStatusEntry_Object = MibTableRow
mpanlOperStatusEntry = _MpanlOperStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 24, 1)
)
mpanlOperStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-MpaNetworkLinkMIB", "mpanlIndex"),
)
if mibBuilder.loadTexts:
    mpanlOperStatusEntry.setStatus("mandatory")


class _MpanlSnmpOperStatus_Type(Integer32):
    """Custom type mpanlSnmpOperStatus based on Integer32"""
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


_MpanlSnmpOperStatus_Type.__name__ = "Integer32"
_MpanlSnmpOperStatus_Object = MibTableColumn
mpanlSnmpOperStatus = _MpanlSnmpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 24, 1, 1),
    _MpanlSnmpOperStatus_Type()
)
mpanlSnmpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlSnmpOperStatus.setStatus("mandatory")
_MpanlOperTable_Object = MibTable
mpanlOperTable = _MpanlOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 25)
)
if mibBuilder.loadTexts:
    mpanlOperTable.setStatus("mandatory")
_MpanlOperEntry_Object = MibTableRow
mpanlOperEntry = _MpanlOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 25, 1)
)
mpanlOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-MpaNetworkLinkMIB", "mpanlIndex"),
)
if mibBuilder.loadTexts:
    mpanlOperEntry.setStatus("mandatory")


class _MpanlRoundTripDelay_Type(Unsigned32):
    """Custom type mpanlRoundTripDelay based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_MpanlRoundTripDelay_Type.__name__ = "Unsigned32"
_MpanlRoundTripDelay_Object = MibTableColumn
mpanlRoundTripDelay = _MpanlRoundTripDelay_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 25, 1, 1),
    _MpanlRoundTripDelay_Type()
)
mpanlRoundTripDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlRoundTripDelay.setStatus("mandatory")
_MpanlFrmToIfByQueueTable_Object = MibTable
mpanlFrmToIfByQueueTable = _MpanlFrmToIfByQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 350)
)
if mibBuilder.loadTexts:
    mpanlFrmToIfByQueueTable.setStatus("mandatory")
_MpanlFrmToIfByQueueEntry_Object = MibTableRow
mpanlFrmToIfByQueueEntry = _MpanlFrmToIfByQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 350, 1)
)
mpanlFrmToIfByQueueEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-MpaNetworkLinkMIB", "mpanlIndex"),
    (0, "Nortel-Magellan-Passport-MpaNetworkLinkMIB", "mpanlFrmToIfByQueueIndex"),
)
if mibBuilder.loadTexts:
    mpanlFrmToIfByQueueEntry.setStatus("mandatory")


class _MpanlFrmToIfByQueueIndex_Type(Integer32):
    """Custom type mpanlFrmToIfByQueueIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_MpanlFrmToIfByQueueIndex_Type.__name__ = "Integer32"
_MpanlFrmToIfByQueueIndex_Object = MibTableColumn
mpanlFrmToIfByQueueIndex = _MpanlFrmToIfByQueueIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 350, 1, 1),
    _MpanlFrmToIfByQueueIndex_Type()
)
mpanlFrmToIfByQueueIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mpanlFrmToIfByQueueIndex.setStatus("mandatory")


class _MpanlFrmToIfByQueueValue_Type(Unsigned32):
    """Custom type mpanlFrmToIfByQueueValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MpanlFrmToIfByQueueValue_Type.__name__ = "Unsigned32"
_MpanlFrmToIfByQueueValue_Object = MibTableColumn
mpanlFrmToIfByQueueValue = _MpanlFrmToIfByQueueValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 350, 1, 2),
    _MpanlFrmToIfByQueueValue_Type()
)
mpanlFrmToIfByQueueValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlFrmToIfByQueueValue.setStatus("mandatory")
_MpanlOctetToIfByQueueTable_Object = MibTable
mpanlOctetToIfByQueueTable = _MpanlOctetToIfByQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 351)
)
if mibBuilder.loadTexts:
    mpanlOctetToIfByQueueTable.setStatus("mandatory")
_MpanlOctetToIfByQueueEntry_Object = MibTableRow
mpanlOctetToIfByQueueEntry = _MpanlOctetToIfByQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 351, 1)
)
mpanlOctetToIfByQueueEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-MpaNetworkLinkMIB", "mpanlIndex"),
    (0, "Nortel-Magellan-Passport-MpaNetworkLinkMIB", "mpanlOctetToIfByQueueIndex"),
)
if mibBuilder.loadTexts:
    mpanlOctetToIfByQueueEntry.setStatus("mandatory")


class _MpanlOctetToIfByQueueIndex_Type(Integer32):
    """Custom type mpanlOctetToIfByQueueIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_MpanlOctetToIfByQueueIndex_Type.__name__ = "Integer32"
_MpanlOctetToIfByQueueIndex_Object = MibTableColumn
mpanlOctetToIfByQueueIndex = _MpanlOctetToIfByQueueIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 351, 1, 1),
    _MpanlOctetToIfByQueueIndex_Type()
)
mpanlOctetToIfByQueueIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mpanlOctetToIfByQueueIndex.setStatus("mandatory")


class _MpanlOctetToIfByQueueValue_Type(Unsigned32):
    """Custom type mpanlOctetToIfByQueueValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MpanlOctetToIfByQueueValue_Type.__name__ = "Unsigned32"
_MpanlOctetToIfByQueueValue_Object = MibTableColumn
mpanlOctetToIfByQueueValue = _MpanlOctetToIfByQueueValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 123, 351, 1, 2),
    _MpanlOctetToIfByQueueValue_Type()
)
mpanlOctetToIfByQueueValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpanlOctetToIfByQueueValue.setStatus("mandatory")
_MpaNetworkLinkMIB_ObjectIdentity = ObjectIdentity
mpaNetworkLinkMIB = _MpaNetworkLinkMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 119)
)
_MpaNetworkLinkGroup_ObjectIdentity = ObjectIdentity
mpaNetworkLinkGroup = _MpaNetworkLinkGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 119, 1)
)
_MpaNetworkLinkGroupBE_ObjectIdentity = ObjectIdentity
mpaNetworkLinkGroupBE = _MpaNetworkLinkGroupBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 119, 1, 5)
)
_MpaNetworkLinkGroupBE01_ObjectIdentity = ObjectIdentity
mpaNetworkLinkGroupBE01 = _MpaNetworkLinkGroupBE01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 119, 1, 5, 2)
)
_MpaNetworkLinkGroupBE01A_ObjectIdentity = ObjectIdentity
mpaNetworkLinkGroupBE01A = _MpaNetworkLinkGroupBE01A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 119, 1, 5, 2, 2)
)
_MpaNetworkLinkCapabilities_ObjectIdentity = ObjectIdentity
mpaNetworkLinkCapabilities = _MpaNetworkLinkCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 119, 3)
)
_MpaNetworkLinkCapabilitiesBE_ObjectIdentity = ObjectIdentity
mpaNetworkLinkCapabilitiesBE = _MpaNetworkLinkCapabilitiesBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 119, 3, 5)
)
_MpaNetworkLinkCapabilitiesBE01_ObjectIdentity = ObjectIdentity
mpaNetworkLinkCapabilitiesBE01 = _MpaNetworkLinkCapabilitiesBE01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 119, 3, 5, 2)
)
_MpaNetworkLinkCapabilitiesBE01A_ObjectIdentity = ObjectIdentity
mpaNetworkLinkCapabilitiesBE01A = _MpaNetworkLinkCapabilitiesBE01A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 119, 3, 5, 2, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-Magellan-Passport-MpaNetworkLinkMIB",
    **{"mpanl": mpanl,
       "mpanlRowStatusTable": mpanlRowStatusTable,
       "mpanlRowStatusEntry": mpanlRowStatusEntry,
       "mpanlRowStatus": mpanlRowStatus,
       "mpanlComponentName": mpanlComponentName,
       "mpanlStorageType": mpanlStorageType,
       "mpanlIndex": mpanlIndex,
       "mpanlDna": mpanlDna,
       "mpanlDnaRowStatusTable": mpanlDnaRowStatusTable,
       "mpanlDnaRowStatusEntry": mpanlDnaRowStatusEntry,
       "mpanlDnaRowStatus": mpanlDnaRowStatus,
       "mpanlDnaComponentName": mpanlDnaComponentName,
       "mpanlDnaStorageType": mpanlDnaStorageType,
       "mpanlDnaIndex": mpanlDnaIndex,
       "mpanlDnaOutgoingOptionsTable": mpanlDnaOutgoingOptionsTable,
       "mpanlDnaOutgoingOptionsEntry": mpanlDnaOutgoingOptionsEntry,
       "mpanlDnaDefaultTransferPriority": mpanlDnaDefaultTransferPriority,
       "mpanlDnaCallOptionsTable": mpanlDnaCallOptionsTable,
       "mpanlDnaCallOptionsEntry": mpanlDnaCallOptionsEntry,
       "mpanlDnaAccountClass": mpanlDnaAccountClass,
       "mpanlDnaAccountCollection": mpanlDnaAccountCollection,
       "mpanlDnaServiceExchange": mpanlDnaServiceExchange,
       "mpanlDnaEgressAccounting": mpanlDnaEgressAccounting,
       "mpanlFramer": mpanlFramer,
       "mpanlFramerRowStatusTable": mpanlFramerRowStatusTable,
       "mpanlFramerRowStatusEntry": mpanlFramerRowStatusEntry,
       "mpanlFramerRowStatus": mpanlFramerRowStatus,
       "mpanlFramerComponentName": mpanlFramerComponentName,
       "mpanlFramerStorageType": mpanlFramerStorageType,
       "mpanlFramerIndex": mpanlFramerIndex,
       "mpanlFramerProvTable": mpanlFramerProvTable,
       "mpanlFramerProvEntry": mpanlFramerProvEntry,
       "mpanlFramerInterfaceName": mpanlFramerInterfaceName,
       "mpanlFramerLinkTable": mpanlFramerLinkTable,
       "mpanlFramerLinkEntry": mpanlFramerLinkEntry,
       "mpanlFramerFlagsBetweenFrames": mpanlFramerFlagsBetweenFrames,
       "mpanlFramerStateTable": mpanlFramerStateTable,
       "mpanlFramerStateEntry": mpanlFramerStateEntry,
       "mpanlFramerAdminState": mpanlFramerAdminState,
       "mpanlFramerOperationalState": mpanlFramerOperationalState,
       "mpanlFramerUsageState": mpanlFramerUsageState,
       "mpanlFramerStatsTable": mpanlFramerStatsTable,
       "mpanlFramerStatsEntry": mpanlFramerStatsEntry,
       "mpanlFramerFrmToIf": mpanlFramerFrmToIf,
       "mpanlFramerFrmFromIf": mpanlFramerFrmFromIf,
       "mpanlFramerOctetFromIf": mpanlFramerOctetFromIf,
       "mpanlFramerAborts": mpanlFramerAborts,
       "mpanlFramerCrcErrors": mpanlFramerCrcErrors,
       "mpanlFramerLrcErrors": mpanlFramerLrcErrors,
       "mpanlFramerNonOctetErrors": mpanlFramerNonOctetErrors,
       "mpanlFramerOverruns": mpanlFramerOverruns,
       "mpanlFramerUnderruns": mpanlFramerUnderruns,
       "mpanlFramerLargeFrmErrors": mpanlFramerLargeFrmErrors,
       "mpanlFramerFrmModeErrors": mpanlFramerFrmModeErrors,
       "mpanlFramerUtilTable": mpanlFramerUtilTable,
       "mpanlFramerUtilEntry": mpanlFramerUtilEntry,
       "mpanlFramerNormPrioLinkUtilToIf": mpanlFramerNormPrioLinkUtilToIf,
       "mpanlFramerNormPrioLinkUtilFromIf": mpanlFramerNormPrioLinkUtilFromIf,
       "mpanlPrefixDna": mpanlPrefixDna,
       "mpanlPrefixDnaRowStatusTable": mpanlPrefixDnaRowStatusTable,
       "mpanlPrefixDnaRowStatusEntry": mpanlPrefixDnaRowStatusEntry,
       "mpanlPrefixDnaRowStatus": mpanlPrefixDnaRowStatus,
       "mpanlPrefixDnaComponentName": mpanlPrefixDnaComponentName,
       "mpanlPrefixDnaStorageType": mpanlPrefixDnaStorageType,
       "mpanlPrefixDnaNumberingPlanIndicatorIndex": mpanlPrefixDnaNumberingPlanIndicatorIndex,
       "mpanlPrefixDnaDataNetworkAddressIndex": mpanlPrefixDnaDataNetworkAddressIndex,
       "mpanlDlci": mpanlDlci,
       "mpanlDlciRowStatusTable": mpanlDlciRowStatusTable,
       "mpanlDlciRowStatusEntry": mpanlDlciRowStatusEntry,
       "mpanlDlciRowStatus": mpanlDlciRowStatus,
       "mpanlDlciComponentName": mpanlDlciComponentName,
       "mpanlDlciStorageType": mpanlDlciStorageType,
       "mpanlDlciIndex": mpanlDlciIndex,
       "mpanlDlciLb": mpanlDlciLb,
       "mpanlDlciLbRowStatusTable": mpanlDlciLbRowStatusTable,
       "mpanlDlciLbRowStatusEntry": mpanlDlciLbRowStatusEntry,
       "mpanlDlciLbRowStatus": mpanlDlciLbRowStatus,
       "mpanlDlciLbComponentName": mpanlDlciLbComponentName,
       "mpanlDlciLbStorageType": mpanlDlciLbStorageType,
       "mpanlDlciLbIndex": mpanlDlciLbIndex,
       "mpanlDlciLbStatsTable": mpanlDlciLbStatsTable,
       "mpanlDlciLbStatsEntry": mpanlDlciLbStatsEntry,
       "mpanlDlciLbLocalTotalFrm": mpanlDlciLbLocalTotalFrm,
       "mpanlDlciLbLocalTotalBytes": mpanlDlciLbLocalTotalBytes,
       "mpanlDlciLbLocalFecnFrm": mpanlDlciLbLocalFecnFrm,
       "mpanlDlciLbLocalBecnFrm": mpanlDlciLbLocalBecnFrm,
       "mpanlDlciLbLocalDeFrm": mpanlDlciLbLocalDeFrm,
       "mpanlDlciLbLocalDeBytes": mpanlDlciLbLocalDeBytes,
       "mpanlDlciLbRemoteTotalFrm": mpanlDlciLbRemoteTotalFrm,
       "mpanlDlciLbRemoteTotalBytes": mpanlDlciLbRemoteTotalBytes,
       "mpanlDlciLbRemoteFecnFrm": mpanlDlciLbRemoteFecnFrm,
       "mpanlDlciLbRemoteBecnFrm": mpanlDlciLbRemoteBecnFrm,
       "mpanlDlciLbRemoteDeFrm": mpanlDlciLbRemoteDeFrm,
       "mpanlDlciLbRemoteDeBytes": mpanlDlciLbRemoteDeBytes,
       "mpanlDlciVc": mpanlDlciVc,
       "mpanlDlciVcRowStatusTable": mpanlDlciVcRowStatusTable,
       "mpanlDlciVcRowStatusEntry": mpanlDlciVcRowStatusEntry,
       "mpanlDlciVcRowStatus": mpanlDlciVcRowStatus,
       "mpanlDlciVcComponentName": mpanlDlciVcComponentName,
       "mpanlDlciVcStorageType": mpanlDlciVcStorageType,
       "mpanlDlciVcIndex": mpanlDlciVcIndex,
       "mpanlDlciVcCadTable": mpanlDlciVcCadTable,
       "mpanlDlciVcCadEntry": mpanlDlciVcCadEntry,
       "mpanlDlciVcType": mpanlDlciVcType,
       "mpanlDlciVcState": mpanlDlciVcState,
       "mpanlDlciVcPreviousState": mpanlDlciVcPreviousState,
       "mpanlDlciVcDiagnosticCode": mpanlDlciVcDiagnosticCode,
       "mpanlDlciVcPreviousDiagnosticCode": mpanlDlciVcPreviousDiagnosticCode,
       "mpanlDlciVcCalledNpi": mpanlDlciVcCalledNpi,
       "mpanlDlciVcCalledDna": mpanlDlciVcCalledDna,
       "mpanlDlciVcCalledLcn": mpanlDlciVcCalledLcn,
       "mpanlDlciVcCallingNpi": mpanlDlciVcCallingNpi,
       "mpanlDlciVcCallingDna": mpanlDlciVcCallingDna,
       "mpanlDlciVcCallingLcn": mpanlDlciVcCallingLcn,
       "mpanlDlciVcAccountingEnabled": mpanlDlciVcAccountingEnabled,
       "mpanlDlciVcFastSelectCall": mpanlDlciVcFastSelectCall,
       "mpanlDlciVcPathReliability": mpanlDlciVcPathReliability,
       "mpanlDlciVcAccountingEnd": mpanlDlciVcAccountingEnd,
       "mpanlDlciVcPriority": mpanlDlciVcPriority,
       "mpanlDlciVcSegmentSize": mpanlDlciVcSegmentSize,
       "mpanlDlciVcMaxSubnetPktSize": mpanlDlciVcMaxSubnetPktSize,
       "mpanlDlciVcRcosToNetwork": mpanlDlciVcRcosToNetwork,
       "mpanlDlciVcRcosFromNetwork": mpanlDlciVcRcosFromNetwork,
       "mpanlDlciVcEmissionPriorityToNetwork": mpanlDlciVcEmissionPriorityToNetwork,
       "mpanlDlciVcEmissionPriorityFromNetwork": mpanlDlciVcEmissionPriorityFromNetwork,
       "mpanlDlciVcDataPath": mpanlDlciVcDataPath,
       "mpanlDlciVcIntdTable": mpanlDlciVcIntdTable,
       "mpanlDlciVcIntdEntry": mpanlDlciVcIntdEntry,
       "mpanlDlciVcCallReferenceNumber": mpanlDlciVcCallReferenceNumber,
       "mpanlDlciVcElapsedTimeTillNow": mpanlDlciVcElapsedTimeTillNow,
       "mpanlDlciVcSegmentsRx": mpanlDlciVcSegmentsRx,
       "mpanlDlciVcSegmentsSent": mpanlDlciVcSegmentsSent,
       "mpanlDlciVcStartTime": mpanlDlciVcStartTime,
       "mpanlDlciVcFrdTable": mpanlDlciVcFrdTable,
       "mpanlDlciVcFrdEntry": mpanlDlciVcFrdEntry,
       "mpanlDlciVcFrmCongestedToSubnet": mpanlDlciVcFrmCongestedToSubnet,
       "mpanlDlciVcCannotForwardToSubnet": mpanlDlciVcCannotForwardToSubnet,
       "mpanlDlciVcNotDataXferToSubnet": mpanlDlciVcNotDataXferToSubnet,
       "mpanlDlciVcOutOfRangeFrmFromSubnet": mpanlDlciVcOutOfRangeFrmFromSubnet,
       "mpanlDlciVcCombErrorsFromSubnet": mpanlDlciVcCombErrorsFromSubnet,
       "mpanlDlciVcDuplicatesFromSubnet": mpanlDlciVcDuplicatesFromSubnet,
       "mpanlDlciVcNotDataXferFromSubnet": mpanlDlciVcNotDataXferFromSubnet,
       "mpanlDlciVcFrmLossTimeouts": mpanlDlciVcFrmLossTimeouts,
       "mpanlDlciVcOoSeqByteCntExceeded": mpanlDlciVcOoSeqByteCntExceeded,
       "mpanlDlciVcPeakOoSeqPktCount": mpanlDlciVcPeakOoSeqPktCount,
       "mpanlDlciVcPeakOoSeqFrmForwarded": mpanlDlciVcPeakOoSeqFrmForwarded,
       "mpanlDlciVcSendSequenceNumber": mpanlDlciVcSendSequenceNumber,
       "mpanlDlciVcPktRetryTimeouts": mpanlDlciVcPktRetryTimeouts,
       "mpanlDlciVcPeakRetryQueueSize": mpanlDlciVcPeakRetryQueueSize,
       "mpanlDlciVcSubnetRecoveries": mpanlDlciVcSubnetRecoveries,
       "mpanlDlciVcOoSeqPktCntExceeded": mpanlDlciVcOoSeqPktCntExceeded,
       "mpanlDlciVcPeakOoSeqByteCount": mpanlDlciVcPeakOoSeqByteCount,
       "mpanlDlciVcDmepTable": mpanlDlciVcDmepTable,
       "mpanlDlciVcDmepEntry": mpanlDlciVcDmepEntry,
       "mpanlDlciVcDmepValue": mpanlDlciVcDmepValue,
       "mpanlDlciLCo": mpanlDlciLCo,
       "mpanlDlciLCoRowStatusTable": mpanlDlciLCoRowStatusTable,
       "mpanlDlciLCoRowStatusEntry": mpanlDlciLCoRowStatusEntry,
       "mpanlDlciLCoRowStatus": mpanlDlciLCoRowStatus,
       "mpanlDlciLCoComponentName": mpanlDlciLCoComponentName,
       "mpanlDlciLCoStorageType": mpanlDlciLCoStorageType,
       "mpanlDlciLCoIndex": mpanlDlciLCoIndex,
       "mpanlDlciLCoPathDataTable": mpanlDlciLCoPathDataTable,
       "mpanlDlciLCoPathDataEntry": mpanlDlciLCoPathDataEntry,
       "mpanlDlciLCoState": mpanlDlciLCoState,
       "mpanlDlciLCoEnd": mpanlDlciLCoEnd,
       "mpanlDlciLCoCostMetric": mpanlDlciLCoCostMetric,
       "mpanlDlciLCoDelayMetric": mpanlDlciLCoDelayMetric,
       "mpanlDlciLCoRoundTripDelay": mpanlDlciLCoRoundTripDelay,
       "mpanlDlciLCoSetupPriority": mpanlDlciLCoSetupPriority,
       "mpanlDlciLCoHoldingPriority": mpanlDlciLCoHoldingPriority,
       "mpanlDlciLCoRequiredTxBandwidth": mpanlDlciLCoRequiredTxBandwidth,
       "mpanlDlciLCoRequiredRxBandwidth": mpanlDlciLCoRequiredRxBandwidth,
       "mpanlDlciLCoRequiredTrafficType": mpanlDlciLCoRequiredTrafficType,
       "mpanlDlciLCoPermittedTrunkTypes": mpanlDlciLCoPermittedTrunkTypes,
       "mpanlDlciLCoRequiredSecurity": mpanlDlciLCoRequiredSecurity,
       "mpanlDlciLCoRequiredCustomerParameter": mpanlDlciLCoRequiredCustomerParameter,
       "mpanlDlciLCoEmissionPriority": mpanlDlciLCoEmissionPriority,
       "mpanlDlciLCoDiscardPriority": mpanlDlciLCoDiscardPriority,
       "mpanlDlciLCoRetryCount": mpanlDlciLCoRetryCount,
       "mpanlDlciLCoPathFailureCount": mpanlDlciLCoPathFailureCount,
       "mpanlDlciLCoReasonForNoRoute": mpanlDlciLCoReasonForNoRoute,
       "mpanlDlciLCoLastTearDownReason": mpanlDlciLCoLastTearDownReason,
       "mpanlDlciLCoPathFailureAction": mpanlDlciLCoPathFailureAction,
       "mpanlDlciLCoBumpPreference": mpanlDlciLCoBumpPreference,
       "mpanlDlciLCoOptimization": mpanlDlciLCoOptimization,
       "mpanlDlciLCoPathUpDateTime": mpanlDlciLCoPathUpDateTime,
       "mpanlDlciLCoStatsTable": mpanlDlciLCoStatsTable,
       "mpanlDlciLCoStatsEntry": mpanlDlciLCoStatsEntry,
       "mpanlDlciLCoPktsToNetwork": mpanlDlciLCoPktsToNetwork,
       "mpanlDlciLCoBytesToNetwork": mpanlDlciLCoBytesToNetwork,
       "mpanlDlciLCoPktsFromNetwork": mpanlDlciLCoPktsFromNetwork,
       "mpanlDlciLCoBytesFromNetwork": mpanlDlciLCoBytesFromNetwork,
       "mpanlDlciLCoCallDataTable": mpanlDlciLCoCallDataTable,
       "mpanlDlciLCoCallDataEntry": mpanlDlciLCoCallDataEntry,
       "mpanlDlciLCoCallingNpi": mpanlDlciLCoCallingNpi,
       "mpanlDlciLCoCallingDna": mpanlDlciLCoCallingDna,
       "mpanlDlciLCoElapsedTimeTillNow": mpanlDlciLCoElapsedTimeTillNow,
       "mpanlDlciLCoCallReferenceNumber": mpanlDlciLCoCallReferenceNumber,
       "mpanlDlciLCoCalledNpi": mpanlDlciLCoCalledNpi,
       "mpanlDlciLCoCalledDna": mpanlDlciLCoCalledDna,
       "mpanlDlciLCoPathTable": mpanlDlciLCoPathTable,
       "mpanlDlciLCoPathEntry": mpanlDlciLCoPathEntry,
       "mpanlDlciLCoPathValue": mpanlDlciLCoPathValue,
       "mpanlDlciJvc": mpanlDlciJvc,
       "mpanlDlciJvcRowStatusTable": mpanlDlciJvcRowStatusTable,
       "mpanlDlciJvcRowStatusEntry": mpanlDlciJvcRowStatusEntry,
       "mpanlDlciJvcRowStatus": mpanlDlciJvcRowStatus,
       "mpanlDlciJvcComponentName": mpanlDlciJvcComponentName,
       "mpanlDlciJvcStorageType": mpanlDlciJvcStorageType,
       "mpanlDlciJvcIndex": mpanlDlciJvcIndex,
       "mpanlDlciJvcOperTable": mpanlDlciJvcOperTable,
       "mpanlDlciJvcOperEntry": mpanlDlciJvcOperEntry,
       "mpanlDlciJvcCurrentState": mpanlDlciJvcCurrentState,
       "mpanlDlciJvcPreviousState": mpanlDlciJvcPreviousState,
       "mpanlDlciJvcCallingNpi": mpanlDlciJvcCallingNpi,
       "mpanlDlciJvcCallingAddress": mpanlDlciJvcCallingAddress,
       "mpanlDlciJvcCallingLcn": mpanlDlciJvcCallingLcn,
       "mpanlDlciJvcCalledNpi": mpanlDlciJvcCalledNpi,
       "mpanlDlciJvcCalledAddress": mpanlDlciJvcCalledAddress,
       "mpanlDlciJvcCalledLcn": mpanlDlciJvcCalledLcn,
       "mpanlDlciJvcStatTable": mpanlDlciJvcStatTable,
       "mpanlDlciJvcStatEntry": mpanlDlciJvcStatEntry,
       "mpanlDlciJvcPacketsFromSubnet": mpanlDlciJvcPacketsFromSubnet,
       "mpanlDlciJvcPacketsToSubnet": mpanlDlciJvcPacketsToSubnet,
       "mpanlDlciJvcPacketsDiscarded": mpanlDlciJvcPacketsDiscarded,
       "mpanlDlciJvcProtocolErrors": mpanlDlciJvcProtocolErrors,
       "mpanlDlciStateTable": mpanlDlciStateTable,
       "mpanlDlciStateEntry": mpanlDlciStateEntry,
       "mpanlDlciAdminState": mpanlDlciAdminState,
       "mpanlDlciOperationalState": mpanlDlciOperationalState,
       "mpanlDlciUsageState": mpanlDlciUsageState,
       "mpanlDlciAvailabilityStatus": mpanlDlciAvailabilityStatus,
       "mpanlDlciProceduralStatus": mpanlDlciProceduralStatus,
       "mpanlDlciControlStatus": mpanlDlciControlStatus,
       "mpanlDlciAlarmStatus": mpanlDlciAlarmStatus,
       "mpanlDlciStandbyStatus": mpanlDlciStandbyStatus,
       "mpanlDlciUnknownStatus": mpanlDlciUnknownStatus,
       "mpanlDlciCalldTable": mpanlDlciCalldTable,
       "mpanlDlciCalldEntry": mpanlDlciCalldEntry,
       "mpanlDlciQ933CallState": mpanlDlciQ933CallState,
       "mpanlDlciQ933CallReference": mpanlDlciQ933CallReference,
       "mpanlDlciSpOpTable": mpanlDlciSpOpTable,
       "mpanlDlciSpOpEntry": mpanlDlciSpOpEntry,
       "mpanlDlciMaximumFrameSize": mpanlDlciMaximumFrameSize,
       "mpanlDlciCommittedBurstSize": mpanlDlciCommittedBurstSize,
       "mpanlDlciExcessBurstSize": mpanlDlciExcessBurstSize,
       "mpanlDlciAccounting": mpanlDlciAccounting,
       "mpanlDlciEmissionPriorityToIf": mpanlDlciEmissionPriorityToIf,
       "mpanlDlciTransferPriToNwk": mpanlDlciTransferPriToNwk,
       "mpanlDlciTransferPriFromNwk": mpanlDlciTransferPriFromNwk,
       "mpanlDlciStatsTable": mpanlDlciStatsTable,
       "mpanlDlciStatsEntry": mpanlDlciStatsEntry,
       "mpanlDlciFrmToIf": mpanlDlciFrmToIf,
       "mpanlDlciFecnFrmToIf": mpanlDlciFecnFrmToIf,
       "mpanlDlciBecnFrmToIf": mpanlDlciBecnFrmToIf,
       "mpanlDlciBciToSubnet": mpanlDlciBciToSubnet,
       "mpanlDlciDeFrmToIf": mpanlDlciDeFrmToIf,
       "mpanlDlciDiscCongestedToIf": mpanlDlciDiscCongestedToIf,
       "mpanlDlciDiscDeCongestedToIf": mpanlDlciDiscDeCongestedToIf,
       "mpanlDlciFrmFromIf": mpanlDlciFrmFromIf,
       "mpanlDlciFecnFrmFromIf": mpanlDlciFecnFrmFromIf,
       "mpanlDlciBecnFrmFromIf": mpanlDlciBecnFrmFromIf,
       "mpanlDlciFciFromSubnet": mpanlDlciFciFromSubnet,
       "mpanlDlciBciFromSubnet": mpanlDlciBciFromSubnet,
       "mpanlDlciDeFrmFromIf": mpanlDlciDeFrmFromIf,
       "mpanlDlciExcessFrmFromIf": mpanlDlciExcessFrmFromIf,
       "mpanlDlciDiscExcessFromIf": mpanlDlciDiscExcessFromIf,
       "mpanlDlciDiscFrameAbit": mpanlDlciDiscFrameAbit,
       "mpanlDlciDiscCongestedFromIf": mpanlDlciDiscCongestedFromIf,
       "mpanlDlciDiscDeCongestedFromIf": mpanlDlciDiscDeCongestedFromIf,
       "mpanlDlciErrorShortFrmFromIf": mpanlDlciErrorShortFrmFromIf,
       "mpanlDlciErrorLongFrmFromIf": mpanlDlciErrorLongFrmFromIf,
       "mpanlDlciBecnFrmSetByService": mpanlDlciBecnFrmSetByService,
       "mpanlDlciBytesToIf": mpanlDlciBytesToIf,
       "mpanlDlciDeBytesToIf": mpanlDlciDeBytesToIf,
       "mpanlDlciDiscCongestedToIfBytes": mpanlDlciDiscCongestedToIfBytes,
       "mpanlDlciDiscDeCongestedToIfBytes": mpanlDlciDiscDeCongestedToIfBytes,
       "mpanlDlciBytesFromIf": mpanlDlciBytesFromIf,
       "mpanlDlciDeBytesFromIf": mpanlDlciDeBytesFromIf,
       "mpanlDlciExcessBytesFromIf": mpanlDlciExcessBytesFromIf,
       "mpanlDlciDiscExcessFromIfBytes": mpanlDlciDiscExcessFromIfBytes,
       "mpanlDlciDiscByteAbit": mpanlDlciDiscByteAbit,
       "mpanlDlciDiscCongestedFromIfBytes": mpanlDlciDiscCongestedFromIfBytes,
       "mpanlDlciDiscDeCongestedFromIfBytes": mpanlDlciDiscDeCongestedFromIfBytes,
       "mpanlDlciErrorLongBytesFromIf": mpanlDlciErrorLongBytesFromIf,
       "mpanlDlciTransferPriorityToNetwork": mpanlDlciTransferPriorityToNetwork,
       "mpanlDlciTransferPriorityFromNetwork": mpanlDlciTransferPriorityFromNetwork,
       "mpanlDlciIntTable": mpanlDlciIntTable,
       "mpanlDlciIntEntry": mpanlDlciIntEntry,
       "mpanlDlciStartTime": mpanlDlciStartTime,
       "mpanlDlciTotalIngressBytes": mpanlDlciTotalIngressBytes,
       "mpanlDlciTotalEgressBytes": mpanlDlciTotalEgressBytes,
       "mpanlDlciEirIngressBytes": mpanlDlciEirIngressBytes,
       "mpanlDlciEirEgressBytes": mpanlDlciEirEgressBytes,
       "mpanlDlciDiscardedBytes": mpanlDlciDiscardedBytes,
       "mpanlDlciTotalIngressSegFrm": mpanlDlciTotalIngressSegFrm,
       "mpanlDlciTotalEgressSegFrm": mpanlDlciTotalEgressSegFrm,
       "mpanlDlciEirIngressSegFrm": mpanlDlciEirIngressSegFrm,
       "mpanlDlciEirEgressSegFrm": mpanlDlciEirEgressSegFrm,
       "mpanlDlciDiscardedSegFrm": mpanlDlciDiscardedSegFrm,
       "mpanlDlciCallReferenceNumber": mpanlDlciCallReferenceNumber,
       "mpanlDlciElapsedDifference": mpanlDlciElapsedDifference,
       "mpanlDlciAbitTable": mpanlDlciAbitTable,
       "mpanlDlciAbitEntry": mpanlDlciAbitEntry,
       "mpanlDlciABitStatusToIf": mpanlDlciABitStatusToIf,
       "mpanlDlciABitReasonToIf": mpanlDlciABitReasonToIf,
       "mpanlDlciABitStatusFromIf": mpanlDlciABitStatusFromIf,
       "mpanlDlciABitReasonFromIf": mpanlDlciABitReasonFromIf,
       "mpanlDlciLoopbackState": mpanlDlciLoopbackState,
       "mpanlSig": mpanlSig,
       "mpanlSigRowStatusTable": mpanlSigRowStatusTable,
       "mpanlSigRowStatusEntry": mpanlSigRowStatusEntry,
       "mpanlSigRowStatus": mpanlSigRowStatus,
       "mpanlSigComponentName": mpanlSigComponentName,
       "mpanlSigStorageType": mpanlSigStorageType,
       "mpanlSigIndex": mpanlSigIndex,
       "mpanlSigSysParmsTable": mpanlSigSysParmsTable,
       "mpanlSigSysParmsEntry": mpanlSigSysParmsEntry,
       "mpanlSigCallSetupTimer": mpanlSigCallSetupTimer,
       "mpanlSigDisconnectTimer": mpanlSigDisconnectTimer,
       "mpanlSigReleaseTimer": mpanlSigReleaseTimer,
       "mpanlSigCallProceedingTimer": mpanlSigCallProceedingTimer,
       "mpanlSigNetworkType": mpanlSigNetworkType,
       "mpanlSigLapfSysTable": mpanlSigLapfSysTable,
       "mpanlSigLapfSysEntry": mpanlSigLapfSysEntry,
       "mpanlSigWindowSize": mpanlSigWindowSize,
       "mpanlSigRetransmitLimit": mpanlSigRetransmitLimit,
       "mpanlSigAckTimer": mpanlSigAckTimer,
       "mpanlSigAckDelayTimer": mpanlSigAckDelayTimer,
       "mpanlSigIdleProbeTimer": mpanlSigIdleProbeTimer,
       "mpanlSigSvcaccTable": mpanlSigSvcaccTable,
       "mpanlSigSvcaccEntry": mpanlSigSvcaccEntry,
       "mpanlSigDefaultAccounting": mpanlSigDefaultAccounting,
       "mpanlSigStateTable": mpanlSigStateTable,
       "mpanlSigStateEntry": mpanlSigStateEntry,
       "mpanlSigAdminState": mpanlSigAdminState,
       "mpanlSigOperationalState": mpanlSigOperationalState,
       "mpanlSigUsageState": mpanlSigUsageState,
       "mpanlSigStatsTable": mpanlSigStatsTable,
       "mpanlSigStatsEntry": mpanlSigStatsEntry,
       "mpanlSigCurrentNumberOfSvcCalls": mpanlSigCurrentNumberOfSvcCalls,
       "mpanlSigInCalls": mpanlSigInCalls,
       "mpanlSigInCallsRefused": mpanlSigInCallsRefused,
       "mpanlSigOutCalls": mpanlSigOutCalls,
       "mpanlSigOutCallsFailed": mpanlSigOutCallsFailed,
       "mpanlSigProtocolErrors": mpanlSigProtocolErrors,
       "mpanlSigQualityOfServiceNotAvailable": mpanlSigQualityOfServiceNotAvailable,
       "mpanlSigSetupTimeout": mpanlSigSetupTimeout,
       "mpanlSigLastCauseInStatusMsgReceived": mpanlSigLastCauseInStatusMsgReceived,
       "mpanlSigLastStateInStatusMsgReceived": mpanlSigLastStateInStatusMsgReceived,
       "mpanlSigLastDlciReceivedStatus": mpanlSigLastDlciReceivedStatus,
       "mpanlSigLastQ933StateReceivedStatus": mpanlSigLastQ933StateReceivedStatus,
       "mpanlSigLastTimeMsgBlockCongested": mpanlSigLastTimeMsgBlockCongested,
       "mpanlSigLastDlciWithMsgBlockCongestion": mpanlSigLastDlciWithMsgBlockCongestion,
       "mpanlSigLapfStatusTable": mpanlSigLapfStatusTable,
       "mpanlSigLapfStatusEntry": mpanlSigLapfStatusEntry,
       "mpanlSigCurrentState": mpanlSigCurrentState,
       "mpanlSigLastStateChangeReason": mpanlSigLastStateChangeReason,
       "mpanlSigFrmrReceive": mpanlSigFrmrReceive,
       "mpanlSigCurrentQueueSize": mpanlSigCurrentQueueSize,
       "mpanlSigLapfStatsTable": mpanlSigLapfStatsTable,
       "mpanlSigLapfStatsEntry": mpanlSigLapfStatsEntry,
       "mpanlSigStateChange": mpanlSigStateChange,
       "mpanlSigRemoteBusy": mpanlSigRemoteBusy,
       "mpanlSigReceiveRejectFrame": mpanlSigReceiveRejectFrame,
       "mpanlSigAckTimeout": mpanlSigAckTimeout,
       "mpanlSigIFramesTransmitted": mpanlSigIFramesTransmitted,
       "mpanlSigIFramesTxDiscarded": mpanlSigIFramesTxDiscarded,
       "mpanlSigIFramesReceived": mpanlSigIFramesReceived,
       "mpanlSigIFramesRcvdDiscarded": mpanlSigIFramesRcvdDiscarded,
       "mpanlSigMpanl": mpanlSigMpanl,
       "mpanlSigMpanlRowStatusTable": mpanlSigMpanlRowStatusTable,
       "mpanlSigMpanlRowStatusEntry": mpanlSigMpanlRowStatusEntry,
       "mpanlSigMpanlRowStatus": mpanlSigMpanlRowStatus,
       "mpanlSigMpanlComponentName": mpanlSigMpanlComponentName,
       "mpanlSigMpanlStorageType": mpanlSigMpanlStorageType,
       "mpanlSigMpanlIndex": mpanlSigMpanlIndex,
       "mpanlSigMpanlStateTable": mpanlSigMpanlStateTable,
       "mpanlSigMpanlStateEntry": mpanlSigMpanlStateEntry,
       "mpanlSigMpanlAdminState": mpanlSigMpanlAdminState,
       "mpanlSigMpanlOperationalState": mpanlSigMpanlOperationalState,
       "mpanlSigMpanlUsageState": mpanlSigMpanlUsageState,
       "mpanlSigMpanlProfileTable": mpanlSigMpanlProfileTable,
       "mpanlSigMpanlProfileEntry": mpanlSigMpanlProfileEntry,
       "mpanlSigMpanlDteCustomerId": mpanlSigMpanlDteCustomerId,
       "mpanlSigMpanlDteNodeId": mpanlSigMpanlDteNodeId,
       "mpanlSigMpanlDteComponentName": mpanlSigMpanlDteComponentName,
       "mpanlSigMpanlHighestDlci": mpanlSigMpanlHighestDlci,
       "mpanlSigMpanlStatsTable": mpanlSigMpanlStatsTable,
       "mpanlSigMpanlStatsEntry": mpanlSigMpanlStatsEntry,
       "mpanlSigMpanlProtocolErrors": mpanlSigMpanlProtocolErrors,
       "mpanlSigMpanlSap0CommandsRx": mpanlSigMpanlSap0CommandsRx,
       "mpanlSigMpanlSap0CommandsTx": mpanlSigMpanlSap0CommandsTx,
       "mpanlSigMpanlSapXCommandsRx": mpanlSigMpanlSapXCommandsRx,
       "mpanlSigMpanlSapXCommandsTx": mpanlSigMpanlSapXCommandsTx,
       "mpanlSigMpanlLapfStatusTable": mpanlSigMpanlLapfStatusTable,
       "mpanlSigMpanlLapfStatusEntry": mpanlSigMpanlLapfStatusEntry,
       "mpanlSigMpanlCurrentState": mpanlSigMpanlCurrentState,
       "mpanlSigMpanlLastStateChangeReason": mpanlSigMpanlLastStateChangeReason,
       "mpanlSigMpanlFrmrReceive": mpanlSigMpanlFrmrReceive,
       "mpanlSigMpanlCurrentQueueSize": mpanlSigMpanlCurrentQueueSize,
       "mpanlSigMpanlLapfStatsTable": mpanlSigMpanlLapfStatsTable,
       "mpanlSigMpanlLapfStatsEntry": mpanlSigMpanlLapfStatsEntry,
       "mpanlSigMpanlStateChange": mpanlSigMpanlStateChange,
       "mpanlSigMpanlRemoteBusy": mpanlSigMpanlRemoteBusy,
       "mpanlSigMpanlReceiveRejectFrame": mpanlSigMpanlReceiveRejectFrame,
       "mpanlSigMpanlAckTimeout": mpanlSigMpanlAckTimeout,
       "mpanlSigMpanlIFramesTransmitted": mpanlSigMpanlIFramesTransmitted,
       "mpanlSigMpanlIFramesTxDiscarded": mpanlSigMpanlIFramesTxDiscarded,
       "mpanlSigMpanlIFramesReceived": mpanlSigMpanlIFramesReceived,
       "mpanlSigMpanlIFramesRcvdDiscarded": mpanlSigMpanlIFramesRcvdDiscarded,
       "mpanlLmi": mpanlLmi,
       "mpanlLmiRowStatusTable": mpanlLmiRowStatusTable,
       "mpanlLmiRowStatusEntry": mpanlLmiRowStatusEntry,
       "mpanlLmiRowStatus": mpanlLmiRowStatus,
       "mpanlLmiComponentName": mpanlLmiComponentName,
       "mpanlLmiStorageType": mpanlLmiStorageType,
       "mpanlLmiIndex": mpanlLmiIndex,
       "mpanlLmiParmsTable": mpanlLmiParmsTable,
       "mpanlLmiParmsEntry": mpanlLmiParmsEntry,
       "mpanlLmiProcedures": mpanlLmiProcedures,
       "mpanlLmiStateTable": mpanlLmiStateTable,
       "mpanlLmiStateEntry": mpanlLmiStateEntry,
       "mpanlLmiAdminState": mpanlLmiAdminState,
       "mpanlLmiOperationalState": mpanlLmiOperationalState,
       "mpanlLmiUsageState": mpanlLmiUsageState,
       "mpanlCidDataTable": mpanlCidDataTable,
       "mpanlCidDataEntry": mpanlCidDataEntry,
       "mpanlCustomerIdentifier": mpanlCustomerIdentifier,
       "mpanlProvTable": mpanlProvTable,
       "mpanlProvEntry": mpanlProvEntry,
       "mpanlCommentText": mpanlCommentText,
       "mpanlEmissionPriorityQsTable": mpanlEmissionPriorityQsTable,
       "mpanlEmissionPriorityQsEntry": mpanlEmissionPriorityQsEntry,
       "mpanlNumberOfEmissionQs": mpanlNumberOfEmissionQs,
       "mpanlStateTable": mpanlStateTable,
       "mpanlStateEntry": mpanlStateEntry,
       "mpanlAdminState": mpanlAdminState,
       "mpanlOperationalState": mpanlOperationalState,
       "mpanlUsageState": mpanlUsageState,
       "mpanlAvailabilityStatus": mpanlAvailabilityStatus,
       "mpanlProceduralStatus": mpanlProceduralStatus,
       "mpanlControlStatus": mpanlControlStatus,
       "mpanlAlarmStatus": mpanlAlarmStatus,
       "mpanlStandbyStatus": mpanlStandbyStatus,
       "mpanlUnknownStatus": mpanlUnknownStatus,
       "mpanlStatsTable": mpanlStatsTable,
       "mpanlStatsEntry": mpanlStatsEntry,
       "mpanlLastUnknownDlci": mpanlLastUnknownDlci,
       "mpanlUnknownDlciFramesFromIf": mpanlUnknownDlciFramesFromIf,
       "mpanlInvalidHeaderFramesFromIf": mpanlInvalidHeaderFramesFromIf,
       "mpanlTrafficStatsTable": mpanlTrafficStatsTable,
       "mpanlTrafficStatsEntry": mpanlTrafficStatsEntry,
       "mpanlFrmToIf": mpanlFrmToIf,
       "mpanlOctetToIf": mpanlOctetToIf,
       "mpanlFrmFromIf": mpanlFrmFromIf,
       "mpanlOctetFromIf": mpanlOctetFromIf,
       "mpanlVoFr": mpanlVoFr,
       "mpanlVoFrRowStatusTable": mpanlVoFrRowStatusTable,
       "mpanlVoFrRowStatusEntry": mpanlVoFrRowStatusEntry,
       "mpanlVoFrRowStatus": mpanlVoFrRowStatus,
       "mpanlVoFrComponentName": mpanlVoFrComponentName,
       "mpanlVoFrStorageType": mpanlVoFrStorageType,
       "mpanlVoFrIndex": mpanlVoFrIndex,
       "mpanlVoFrOperTable": mpanlVoFrOperTable,
       "mpanlVoFrOperEntry": mpanlVoFrOperEntry,
       "mpanlVoFrMaximumFrameSize": mpanlVoFrMaximumFrameSize,
       "mpanlVoFrTransmitInformationRate": mpanlVoFrTransmitInformationRate,
       "mpanlVoFrStatsTable": mpanlVoFrStatsTable,
       "mpanlVoFrStatsEntry": mpanlVoFrStatsEntry,
       "mpanlVoFrFragmentedHighestPriorityFrames": mpanlVoFrFragmentedHighestPriorityFrames,
       "mpanlVoFrLostFragmentsFromIf": mpanlVoFrLostFragmentsFromIf,
       "mpanlVoFrProtocolViolationsFromIf": mpanlVoFrProtocolViolationsFromIf,
       "mpanlFrMuxSetup": mpanlFrMuxSetup,
       "mpanlFrMuxSetupRowStatusTable": mpanlFrMuxSetupRowStatusTable,
       "mpanlFrMuxSetupRowStatusEntry": mpanlFrMuxSetupRowStatusEntry,
       "mpanlFrMuxSetupRowStatus": mpanlFrMuxSetupRowStatus,
       "mpanlFrMuxSetupComponentName": mpanlFrMuxSetupComponentName,
       "mpanlFrMuxSetupStorageType": mpanlFrMuxSetupStorageType,
       "mpanlFrMuxSetupIndex": mpanlFrMuxSetupIndex,
       "mpanlFrMuxSetupPvcSetup": mpanlFrMuxSetupPvcSetup,
       "mpanlFrMuxSetupPvcSetupRowStatusTable": mpanlFrMuxSetupPvcSetupRowStatusTable,
       "mpanlFrMuxSetupPvcSetupRowStatusEntry": mpanlFrMuxSetupPvcSetupRowStatusEntry,
       "mpanlFrMuxSetupPvcSetupRowStatus": mpanlFrMuxSetupPvcSetupRowStatus,
       "mpanlFrMuxSetupPvcSetupComponentName": mpanlFrMuxSetupPvcSetupComponentName,
       "mpanlFrMuxSetupPvcSetupStorageType": mpanlFrMuxSetupPvcSetupStorageType,
       "mpanlFrMuxSetupPvcSetupIndex": mpanlFrMuxSetupPvcSetupIndex,
       "mpanlFrMuxSetupPvcSetupProvTable": mpanlFrMuxSetupPvcSetupProvTable,
       "mpanlFrMuxSetupPvcSetupProvEntry": mpanlFrMuxSetupPvcSetupProvEntry,
       "mpanlFrMuxSetupPvcSetupDlciName": mpanlFrMuxSetupPvcSetupDlciName,
       "mpanlFrMuxSetupOpTable": mpanlFrMuxSetupOpTable,
       "mpanlFrMuxSetupOpEntry": mpanlFrMuxSetupOpEntry,
       "mpanlFrMuxSetupCommittedInformationRate": mpanlFrMuxSetupCommittedInformationRate,
       "mpanlFrMuxSetupDlciCompName": mpanlFrMuxSetupDlciCompName,
       "mpanlIsdn": mpanlIsdn,
       "mpanlIsdnRowStatusTable": mpanlIsdnRowStatusTable,
       "mpanlIsdnRowStatusEntry": mpanlIsdnRowStatusEntry,
       "mpanlIsdnRowStatus": mpanlIsdnRowStatus,
       "mpanlIsdnComponentName": mpanlIsdnComponentName,
       "mpanlIsdnStorageType": mpanlIsdnStorageType,
       "mpanlIsdnIndex": mpanlIsdnIndex,
       "mpanlIsdnProvTable": mpanlIsdnProvTable,
       "mpanlIsdnProvEntry": mpanlIsdnProvEntry,
       "mpanlIsdnT320": mpanlIsdnT320,
       "mpanlIsdnAddressSignalling": mpanlIsdnAddressSignalling,
       "mpanlIsdnOperTable": mpanlIsdnOperTable,
       "mpanlIsdnOperEntry": mpanlIsdnOperEntry,
       "mpanlIsdnDataSigChan": mpanlIsdnDataSigChan,
       "mpanlIsdnBChannelState": mpanlIsdnBChannelState,
       "mpanlIsdnLastUsedCgpn": mpanlIsdnLastUsedCgpn,
       "mpanlIsdnBChanIntState": mpanlIsdnBChanIntState,
       "mpanlIsdnActiveVirtualCircuitsCount": mpanlIsdnActiveVirtualCircuitsCount,
       "mpanlIfEntryTable": mpanlIfEntryTable,
       "mpanlIfEntryEntry": mpanlIfEntryEntry,
       "mpanlIfAdminStatus": mpanlIfAdminStatus,
       "mpanlIfIndex": mpanlIfIndex,
       "mpanlOperStatusTable": mpanlOperStatusTable,
       "mpanlOperStatusEntry": mpanlOperStatusEntry,
       "mpanlSnmpOperStatus": mpanlSnmpOperStatus,
       "mpanlOperTable": mpanlOperTable,
       "mpanlOperEntry": mpanlOperEntry,
       "mpanlRoundTripDelay": mpanlRoundTripDelay,
       "mpanlFrmToIfByQueueTable": mpanlFrmToIfByQueueTable,
       "mpanlFrmToIfByQueueEntry": mpanlFrmToIfByQueueEntry,
       "mpanlFrmToIfByQueueIndex": mpanlFrmToIfByQueueIndex,
       "mpanlFrmToIfByQueueValue": mpanlFrmToIfByQueueValue,
       "mpanlOctetToIfByQueueTable": mpanlOctetToIfByQueueTable,
       "mpanlOctetToIfByQueueEntry": mpanlOctetToIfByQueueEntry,
       "mpanlOctetToIfByQueueIndex": mpanlOctetToIfByQueueIndex,
       "mpanlOctetToIfByQueueValue": mpanlOctetToIfByQueueValue,
       "mpaNetworkLinkMIB": mpaNetworkLinkMIB,
       "mpaNetworkLinkGroup": mpaNetworkLinkGroup,
       "mpaNetworkLinkGroupBE": mpaNetworkLinkGroupBE,
       "mpaNetworkLinkGroupBE01": mpaNetworkLinkGroupBE01,
       "mpaNetworkLinkGroupBE01A": mpaNetworkLinkGroupBE01A,
       "mpaNetworkLinkCapabilities": mpaNetworkLinkCapabilities,
       "mpaNetworkLinkCapabilitiesBE": mpaNetworkLinkCapabilitiesBE,
       "mpaNetworkLinkCapabilitiesBE01": mpaNetworkLinkCapabilitiesBE01,
       "mpaNetworkLinkCapabilitiesBE01A": mpaNetworkLinkCapabilitiesBE01A}
)
