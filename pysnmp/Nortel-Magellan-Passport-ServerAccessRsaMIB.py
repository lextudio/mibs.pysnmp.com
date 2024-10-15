# SNMP MIB module (Nortel-Magellan-Passport-ServerAccessRsaMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-Magellan-Passport-ServerAccessRsaMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:31:19 2024
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
 Integer32,
 RowPointer,
 RowStatus,
 StorageType,
 Unsigned32) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-StandardTextualConventionsMIB",
    "Counter32",
    "DisplayString",
    "Integer32",
    "RowPointer",
    "RowStatus",
    "StorageType",
    "Unsigned32")

(AsciiString,
 AsciiStringIndex,
 DigitString,
 EnterpriseDateAndTime,
 Hex,
 Link,
 NonReplicated) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-TextualConventionsMIB",
    "AsciiString",
    "AsciiStringIndex",
    "DigitString",
    "EnterpriseDateAndTime",
    "Hex",
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

_Rsa_ObjectIdentity = ObjectIdentity
rsa = _Rsa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108)
)
_RsaRowStatusTable_Object = MibTable
rsaRowStatusTable = _RsaRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 1)
)
if mibBuilder.loadTexts:
    rsaRowStatusTable.setStatus("mandatory")
_RsaRowStatusEntry_Object = MibTableRow
rsaRowStatusEntry = _RsaRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 1, 1)
)
rsaRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-ServerAccessRsaMIB", "rsaIndex"),
)
if mibBuilder.loadTexts:
    rsaRowStatusEntry.setStatus("mandatory")
_RsaRowStatus_Type = RowStatus
_RsaRowStatus_Object = MibTableColumn
rsaRowStatus = _RsaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 1, 1, 1),
    _RsaRowStatus_Type()
)
rsaRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsaRowStatus.setStatus("mandatory")
_RsaComponentName_Type = DisplayString
_RsaComponentName_Object = MibTableColumn
rsaComponentName = _RsaComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 1, 1, 2),
    _RsaComponentName_Type()
)
rsaComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsaComponentName.setStatus("mandatory")
_RsaStorageType_Type = StorageType
_RsaStorageType_Object = MibTableColumn
rsaStorageType = _RsaStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 1, 1, 4),
    _RsaStorageType_Type()
)
rsaStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsaStorageType.setStatus("mandatory")


class _RsaIndex_Type(AsciiStringIndex):
    """Custom type rsaIndex based on AsciiStringIndex"""
    subtypeSpec = AsciiStringIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_RsaIndex_Type.__name__ = "AsciiStringIndex"
_RsaIndex_Object = MibTableColumn
rsaIndex = _RsaIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 1, 1, 10),
    _RsaIndex_Type()
)
rsaIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rsaIndex.setStatus("mandatory")
_RsaDna_ObjectIdentity = ObjectIdentity
rsaDna = _RsaDna_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 2)
)
_RsaDnaRowStatusTable_Object = MibTable
rsaDnaRowStatusTable = _RsaDnaRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 2, 1)
)
if mibBuilder.loadTexts:
    rsaDnaRowStatusTable.setStatus("mandatory")
_RsaDnaRowStatusEntry_Object = MibTableRow
rsaDnaRowStatusEntry = _RsaDnaRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 2, 1, 1)
)
rsaDnaRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-ServerAccessRsaMIB", "rsaIndex"),
    (0, "Nortel-Magellan-Passport-ServerAccessRsaMIB", "rsaDnaIndex"),
)
if mibBuilder.loadTexts:
    rsaDnaRowStatusEntry.setStatus("mandatory")
_RsaDnaRowStatus_Type = RowStatus
_RsaDnaRowStatus_Object = MibTableColumn
rsaDnaRowStatus = _RsaDnaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 2, 1, 1, 1),
    _RsaDnaRowStatus_Type()
)
rsaDnaRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsaDnaRowStatus.setStatus("mandatory")
_RsaDnaComponentName_Type = DisplayString
_RsaDnaComponentName_Object = MibTableColumn
rsaDnaComponentName = _RsaDnaComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 2, 1, 1, 2),
    _RsaDnaComponentName_Type()
)
rsaDnaComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsaDnaComponentName.setStatus("mandatory")
_RsaDnaStorageType_Type = StorageType
_RsaDnaStorageType_Object = MibTableColumn
rsaDnaStorageType = _RsaDnaStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 2, 1, 1, 4),
    _RsaDnaStorageType_Type()
)
rsaDnaStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsaDnaStorageType.setStatus("mandatory")
_RsaDnaIndex_Type = NonReplicated
_RsaDnaIndex_Object = MibTableColumn
rsaDnaIndex = _RsaDnaIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 2, 1, 1, 10),
    _RsaDnaIndex_Type()
)
rsaDnaIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rsaDnaIndex.setStatus("mandatory")
_RsaDnaCug_ObjectIdentity = ObjectIdentity
rsaDnaCug = _RsaDnaCug_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 2, 2)
)
_RsaDnaCugRowStatusTable_Object = MibTable
rsaDnaCugRowStatusTable = _RsaDnaCugRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 2, 2, 1)
)
if mibBuilder.loadTexts:
    rsaDnaCugRowStatusTable.setStatus("mandatory")
_RsaDnaCugRowStatusEntry_Object = MibTableRow
rsaDnaCugRowStatusEntry = _RsaDnaCugRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 2, 2, 1, 1)
)
rsaDnaCugRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-ServerAccessRsaMIB", "rsaIndex"),
    (0, "Nortel-Magellan-Passport-ServerAccessRsaMIB", "rsaDnaIndex"),
    (0, "Nortel-Magellan-Passport-ServerAccessRsaMIB", "rsaDnaCugIndex"),
)
if mibBuilder.loadTexts:
    rsaDnaCugRowStatusEntry.setStatus("mandatory")
_RsaDnaCugRowStatus_Type = RowStatus
_RsaDnaCugRowStatus_Object = MibTableColumn
rsaDnaCugRowStatus = _RsaDnaCugRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 2, 2, 1, 1, 1),
    _RsaDnaCugRowStatus_Type()
)
rsaDnaCugRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsaDnaCugRowStatus.setStatus("mandatory")
_RsaDnaCugComponentName_Type = DisplayString
_RsaDnaCugComponentName_Object = MibTableColumn
rsaDnaCugComponentName = _RsaDnaCugComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 2, 2, 1, 1, 2),
    _RsaDnaCugComponentName_Type()
)
rsaDnaCugComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsaDnaCugComponentName.setStatus("mandatory")
_RsaDnaCugStorageType_Type = StorageType
_RsaDnaCugStorageType_Object = MibTableColumn
rsaDnaCugStorageType = _RsaDnaCugStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 2, 2, 1, 1, 4),
    _RsaDnaCugStorageType_Type()
)
rsaDnaCugStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsaDnaCugStorageType.setStatus("mandatory")


class _RsaDnaCugIndex_Type(Integer32):
    """Custom type rsaDnaCugIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RsaDnaCugIndex_Type.__name__ = "Integer32"
_RsaDnaCugIndex_Object = MibTableColumn
rsaDnaCugIndex = _RsaDnaCugIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 2, 2, 1, 1, 10),
    _RsaDnaCugIndex_Type()
)
rsaDnaCugIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rsaDnaCugIndex.setStatus("mandatory")
_RsaDnaCugCugOptionsTable_Object = MibTable
rsaDnaCugCugOptionsTable = _RsaDnaCugCugOptionsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 2, 2, 10)
)
if mibBuilder.loadTexts:
    rsaDnaCugCugOptionsTable.setStatus("mandatory")
_RsaDnaCugCugOptionsEntry_Object = MibTableRow
rsaDnaCugCugOptionsEntry = _RsaDnaCugCugOptionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 2, 2, 10, 1)
)
rsaDnaCugCugOptionsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-ServerAccessRsaMIB", "rsaIndex"),
    (0, "Nortel-Magellan-Passport-ServerAccessRsaMIB", "rsaDnaIndex"),
    (0, "Nortel-Magellan-Passport-ServerAccessRsaMIB", "rsaDnaCugIndex"),
)
if mibBuilder.loadTexts:
    rsaDnaCugCugOptionsEntry.setStatus("mandatory")


class _RsaDnaCugType_Type(Integer32):
    """Custom type rsaDnaCugType based on Integer32"""
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


_RsaDnaCugType_Type.__name__ = "Integer32"
_RsaDnaCugType_Object = MibTableColumn
rsaDnaCugType = _RsaDnaCugType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 2, 2, 10, 1, 1),
    _RsaDnaCugType_Type()
)
rsaDnaCugType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsaDnaCugType.setStatus("mandatory")


class _RsaDnaCugDnic_Type(DigitString):
    """Custom type rsaDnaCugDnic based on DigitString"""
    defaultHexValue = "30303030"

    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_RsaDnaCugDnic_Type.__name__ = "DigitString"
_RsaDnaCugDnic_Object = MibTableColumn
rsaDnaCugDnic = _RsaDnaCugDnic_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 2, 2, 10, 1, 2),
    _RsaDnaCugDnic_Type()
)
rsaDnaCugDnic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsaDnaCugDnic.setStatus("mandatory")


class _RsaDnaCugInterlockCode_Type(Unsigned32):
    """Custom type rsaDnaCugInterlockCode based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RsaDnaCugInterlockCode_Type.__name__ = "Unsigned32"
_RsaDnaCugInterlockCode_Object = MibTableColumn
rsaDnaCugInterlockCode = _RsaDnaCugInterlockCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 2, 2, 10, 1, 3),
    _RsaDnaCugInterlockCode_Type()
)
rsaDnaCugInterlockCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsaDnaCugInterlockCode.setStatus("mandatory")


class _RsaDnaCugPreferential_Type(Integer32):
    """Custom type rsaDnaCugPreferential based on Integer32"""
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


_RsaDnaCugPreferential_Type.__name__ = "Integer32"
_RsaDnaCugPreferential_Object = MibTableColumn
rsaDnaCugPreferential = _RsaDnaCugPreferential_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 2, 2, 10, 1, 4),
    _RsaDnaCugPreferential_Type()
)
rsaDnaCugPreferential.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsaDnaCugPreferential.setStatus("mandatory")


class _RsaDnaCugOutCalls_Type(Integer32):
    """Custom type rsaDnaCugOutCalls based on Integer32"""
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


_RsaDnaCugOutCalls_Type.__name__ = "Integer32"
_RsaDnaCugOutCalls_Object = MibTableColumn
rsaDnaCugOutCalls = _RsaDnaCugOutCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 2, 2, 10, 1, 5),
    _RsaDnaCugOutCalls_Type()
)
rsaDnaCugOutCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsaDnaCugOutCalls.setStatus("mandatory")


class _RsaDnaCugIncCalls_Type(Integer32):
    """Custom type rsaDnaCugIncCalls based on Integer32"""
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


_RsaDnaCugIncCalls_Type.__name__ = "Integer32"
_RsaDnaCugIncCalls_Object = MibTableColumn
rsaDnaCugIncCalls = _RsaDnaCugIncCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 2, 2, 10, 1, 6),
    _RsaDnaCugIncCalls_Type()
)
rsaDnaCugIncCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsaDnaCugIncCalls.setStatus("mandatory")


class _RsaDnaCugPrivileged_Type(Integer32):
    """Custom type rsaDnaCugPrivileged based on Integer32"""
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


_RsaDnaCugPrivileged_Type.__name__ = "Integer32"
_RsaDnaCugPrivileged_Object = MibTableColumn
rsaDnaCugPrivileged = _RsaDnaCugPrivileged_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 2, 2, 10, 1, 7),
    _RsaDnaCugPrivileged_Type()
)
rsaDnaCugPrivileged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsaDnaCugPrivileged.setStatus("mandatory")
_RsaDnaAddressTable_Object = MibTable
rsaDnaAddressTable = _RsaDnaAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 2, 10)
)
if mibBuilder.loadTexts:
    rsaDnaAddressTable.setStatus("mandatory")
_RsaDnaAddressEntry_Object = MibTableRow
rsaDnaAddressEntry = _RsaDnaAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 2, 10, 1)
)
rsaDnaAddressEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-ServerAccessRsaMIB", "rsaIndex"),
    (0, "Nortel-Magellan-Passport-ServerAccessRsaMIB", "rsaDnaIndex"),
)
if mibBuilder.loadTexts:
    rsaDnaAddressEntry.setStatus("mandatory")


class _RsaDnaNumberingPlanIndicator_Type(Integer32):
    """Custom type rsaDnaNumberingPlanIndicator based on Integer32"""
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


_RsaDnaNumberingPlanIndicator_Type.__name__ = "Integer32"
_RsaDnaNumberingPlanIndicator_Object = MibTableColumn
rsaDnaNumberingPlanIndicator = _RsaDnaNumberingPlanIndicator_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 2, 10, 1, 1),
    _RsaDnaNumberingPlanIndicator_Type()
)
rsaDnaNumberingPlanIndicator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsaDnaNumberingPlanIndicator.setStatus("mandatory")


class _RsaDnaDataNetworkAddress_Type(DigitString):
    """Custom type rsaDnaDataNetworkAddress based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_RsaDnaDataNetworkAddress_Type.__name__ = "DigitString"
_RsaDnaDataNetworkAddress_Object = MibTableColumn
rsaDnaDataNetworkAddress = _RsaDnaDataNetworkAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 2, 10, 1, 2),
    _RsaDnaDataNetworkAddress_Type()
)
rsaDnaDataNetworkAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsaDnaDataNetworkAddress.setStatus("mandatory")
_RsaDnaOutgoingOptionsTable_Object = MibTable
rsaDnaOutgoingOptionsTable = _RsaDnaOutgoingOptionsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 2, 11)
)
if mibBuilder.loadTexts:
    rsaDnaOutgoingOptionsTable.setStatus("mandatory")
_RsaDnaOutgoingOptionsEntry_Object = MibTableRow
rsaDnaOutgoingOptionsEntry = _RsaDnaOutgoingOptionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 2, 11, 1)
)
rsaDnaOutgoingOptionsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-ServerAccessRsaMIB", "rsaIndex"),
    (0, "Nortel-Magellan-Passport-ServerAccessRsaMIB", "rsaDnaIndex"),
)
if mibBuilder.loadTexts:
    rsaDnaOutgoingOptionsEntry.setStatus("mandatory")


class _RsaDnaOutCalls_Type(Integer32):
    """Custom type rsaDnaOutCalls based on Integer32"""
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


_RsaDnaOutCalls_Type.__name__ = "Integer32"
_RsaDnaOutCalls_Object = MibTableColumn
rsaDnaOutCalls = _RsaDnaOutCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 2, 11, 1, 1),
    _RsaDnaOutCalls_Type()
)
rsaDnaOutCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsaDnaOutCalls.setStatus("mandatory")
_RsaDnaIncomingOptionsTable_Object = MibTable
rsaDnaIncomingOptionsTable = _RsaDnaIncomingOptionsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 2, 12)
)
if mibBuilder.loadTexts:
    rsaDnaIncomingOptionsTable.setStatus("mandatory")
_RsaDnaIncomingOptionsEntry_Object = MibTableRow
rsaDnaIncomingOptionsEntry = _RsaDnaIncomingOptionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 2, 12, 1)
)
rsaDnaIncomingOptionsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-ServerAccessRsaMIB", "rsaIndex"),
    (0, "Nortel-Magellan-Passport-ServerAccessRsaMIB", "rsaDnaIndex"),
)
if mibBuilder.loadTexts:
    rsaDnaIncomingOptionsEntry.setStatus("mandatory")


class _RsaDnaIncCalls_Type(Integer32):
    """Custom type rsaDnaIncCalls based on Integer32"""
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


_RsaDnaIncCalls_Type.__name__ = "Integer32"
_RsaDnaIncCalls_Object = MibTableColumn
rsaDnaIncCalls = _RsaDnaIncCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 2, 12, 1, 1),
    _RsaDnaIncCalls_Type()
)
rsaDnaIncCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsaDnaIncCalls.setStatus("mandatory")


class _RsaDnaIncAccess_Type(Integer32):
    """Custom type rsaDnaIncAccess based on Integer32"""
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


_RsaDnaIncAccess_Type.__name__ = "Integer32"
_RsaDnaIncAccess_Object = MibTableColumn
rsaDnaIncAccess = _RsaDnaIncAccess_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 2, 12, 1, 9),
    _RsaDnaIncAccess_Type()
)
rsaDnaIncAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsaDnaIncAccess.setStatus("mandatory")
_RsaVncsAccess_ObjectIdentity = ObjectIdentity
rsaVncsAccess = _RsaVncsAccess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 3)
)
_RsaVncsAccessRowStatusTable_Object = MibTable
rsaVncsAccessRowStatusTable = _RsaVncsAccessRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 3, 1)
)
if mibBuilder.loadTexts:
    rsaVncsAccessRowStatusTable.setStatus("mandatory")
_RsaVncsAccessRowStatusEntry_Object = MibTableRow
rsaVncsAccessRowStatusEntry = _RsaVncsAccessRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 3, 1, 1)
)
rsaVncsAccessRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-ServerAccessRsaMIB", "rsaIndex"),
    (0, "Nortel-Magellan-Passport-ServerAccessRsaMIB", "rsaVncsAccessIndex"),
)
if mibBuilder.loadTexts:
    rsaVncsAccessRowStatusEntry.setStatus("mandatory")
_RsaVncsAccessRowStatus_Type = RowStatus
_RsaVncsAccessRowStatus_Object = MibTableColumn
rsaVncsAccessRowStatus = _RsaVncsAccessRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 3, 1, 1, 1),
    _RsaVncsAccessRowStatus_Type()
)
rsaVncsAccessRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsaVncsAccessRowStatus.setStatus("mandatory")
_RsaVncsAccessComponentName_Type = DisplayString
_RsaVncsAccessComponentName_Object = MibTableColumn
rsaVncsAccessComponentName = _RsaVncsAccessComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 3, 1, 1, 2),
    _RsaVncsAccessComponentName_Type()
)
rsaVncsAccessComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsaVncsAccessComponentName.setStatus("mandatory")
_RsaVncsAccessStorageType_Type = StorageType
_RsaVncsAccessStorageType_Object = MibTableColumn
rsaVncsAccessStorageType = _RsaVncsAccessStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 3, 1, 1, 4),
    _RsaVncsAccessStorageType_Type()
)
rsaVncsAccessStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsaVncsAccessStorageType.setStatus("mandatory")
_RsaVncsAccessIndex_Type = NonReplicated
_RsaVncsAccessIndex_Object = MibTableColumn
rsaVncsAccessIndex = _RsaVncsAccessIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 3, 1, 1, 10),
    _RsaVncsAccessIndex_Type()
)
rsaVncsAccessIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rsaVncsAccessIndex.setStatus("mandatory")
_RsaVncsAccessProvisionedTable_Object = MibTable
rsaVncsAccessProvisionedTable = _RsaVncsAccessProvisionedTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 3, 10)
)
if mibBuilder.loadTexts:
    rsaVncsAccessProvisionedTable.setStatus("mandatory")
_RsaVncsAccessProvisionedEntry_Object = MibTableRow
rsaVncsAccessProvisionedEntry = _RsaVncsAccessProvisionedEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 3, 10, 1)
)
rsaVncsAccessProvisionedEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-ServerAccessRsaMIB", "rsaIndex"),
    (0, "Nortel-Magellan-Passport-ServerAccessRsaMIB", "rsaVncsAccessIndex"),
)
if mibBuilder.loadTexts:
    rsaVncsAccessProvisionedEntry.setStatus("mandatory")


class _RsaVncsAccessTimeToLive_Type(Integer32):
    """Custom type rsaVncsAccessTimeToLive based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_RsaVncsAccessTimeToLive_Type.__name__ = "Integer32"
_RsaVncsAccessTimeToLive_Object = MibTableColumn
rsaVncsAccessTimeToLive = _RsaVncsAccessTimeToLive_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 3, 10, 1, 1),
    _RsaVncsAccessTimeToLive_Type()
)
rsaVncsAccessTimeToLive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsaVncsAccessTimeToLive.setStatus("mandatory")
_RsaVncsAccessStateTable_Object = MibTable
rsaVncsAccessStateTable = _RsaVncsAccessStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 3, 11)
)
if mibBuilder.loadTexts:
    rsaVncsAccessStateTable.setStatus("mandatory")
_RsaVncsAccessStateEntry_Object = MibTableRow
rsaVncsAccessStateEntry = _RsaVncsAccessStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 3, 11, 1)
)
rsaVncsAccessStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-ServerAccessRsaMIB", "rsaIndex"),
    (0, "Nortel-Magellan-Passport-ServerAccessRsaMIB", "rsaVncsAccessIndex"),
)
if mibBuilder.loadTexts:
    rsaVncsAccessStateEntry.setStatus("mandatory")


class _RsaVncsAccessAdminState_Type(Integer32):
    """Custom type rsaVncsAccessAdminState based on Integer32"""
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


_RsaVncsAccessAdminState_Type.__name__ = "Integer32"
_RsaVncsAccessAdminState_Object = MibTableColumn
rsaVncsAccessAdminState = _RsaVncsAccessAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 3, 11, 1, 1),
    _RsaVncsAccessAdminState_Type()
)
rsaVncsAccessAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsaVncsAccessAdminState.setStatus("mandatory")


class _RsaVncsAccessOperationalState_Type(Integer32):
    """Custom type rsaVncsAccessOperationalState based on Integer32"""
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


_RsaVncsAccessOperationalState_Type.__name__ = "Integer32"
_RsaVncsAccessOperationalState_Object = MibTableColumn
rsaVncsAccessOperationalState = _RsaVncsAccessOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 3, 11, 1, 2),
    _RsaVncsAccessOperationalState_Type()
)
rsaVncsAccessOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsaVncsAccessOperationalState.setStatus("mandatory")


class _RsaVncsAccessUsageState_Type(Integer32):
    """Custom type rsaVncsAccessUsageState based on Integer32"""
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


_RsaVncsAccessUsageState_Type.__name__ = "Integer32"
_RsaVncsAccessUsageState_Object = MibTableColumn
rsaVncsAccessUsageState = _RsaVncsAccessUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 3, 11, 1, 3),
    _RsaVncsAccessUsageState_Type()
)
rsaVncsAccessUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsaVncsAccessUsageState.setStatus("mandatory")
_RsaVncsAccessOperationalTable_Object = MibTable
rsaVncsAccessOperationalTable = _RsaVncsAccessOperationalTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 3, 12)
)
if mibBuilder.loadTexts:
    rsaVncsAccessOperationalTable.setStatus("mandatory")
_RsaVncsAccessOperationalEntry_Object = MibTableRow
rsaVncsAccessOperationalEntry = _RsaVncsAccessOperationalEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 3, 12, 1)
)
rsaVncsAccessOperationalEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-ServerAccessRsaMIB", "rsaIndex"),
    (0, "Nortel-Magellan-Passport-ServerAccessRsaMIB", "rsaVncsAccessIndex"),
)
if mibBuilder.loadTexts:
    rsaVncsAccessOperationalEntry.setStatus("mandatory")
_RsaVncsAccessRequestsSent_Type = Counter32
_RsaVncsAccessRequestsSent_Object = MibTableColumn
rsaVncsAccessRequestsSent = _RsaVncsAccessRequestsSent_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 3, 12, 1, 1),
    _RsaVncsAccessRequestsSent_Type()
)
rsaVncsAccessRequestsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsaVncsAccessRequestsSent.setStatus("mandatory")
_RsaVncsAccessRepliesReceived_Type = Counter32
_RsaVncsAccessRepliesReceived_Object = MibTableColumn
rsaVncsAccessRepliesReceived = _RsaVncsAccessRepliesReceived_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 3, 12, 1, 2),
    _RsaVncsAccessRepliesReceived_Type()
)
rsaVncsAccessRepliesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsaVncsAccessRepliesReceived.setStatus("mandatory")


class _RsaVncsAccessRequestsQueued_Type(Integer32):
    """Custom type rsaVncsAccessRequestsQueued based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RsaVncsAccessRequestsQueued_Type.__name__ = "Integer32"
_RsaVncsAccessRequestsQueued_Object = MibTableColumn
rsaVncsAccessRequestsQueued = _RsaVncsAccessRequestsQueued_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 3, 12, 1, 3),
    _RsaVncsAccessRequestsQueued_Type()
)
rsaVncsAccessRequestsQueued.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsaVncsAccessRequestsQueued.setStatus("mandatory")
_RsaVncsAccessRequestsDiscarded_Type = Counter32
_RsaVncsAccessRequestsDiscarded_Object = MibTableColumn
rsaVncsAccessRequestsDiscarded = _RsaVncsAccessRequestsDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 3, 12, 1, 4),
    _RsaVncsAccessRequestsDiscarded_Type()
)
rsaVncsAccessRequestsDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsaVncsAccessRequestsDiscarded.setStatus("mandatory")
_RsaConnection_ObjectIdentity = ObjectIdentity
rsaConnection = _RsaConnection_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 4)
)
_RsaConnectionRowStatusTable_Object = MibTable
rsaConnectionRowStatusTable = _RsaConnectionRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 4, 1)
)
if mibBuilder.loadTexts:
    rsaConnectionRowStatusTable.setStatus("mandatory")
_RsaConnectionRowStatusEntry_Object = MibTableRow
rsaConnectionRowStatusEntry = _RsaConnectionRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 4, 1, 1)
)
rsaConnectionRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-ServerAccessRsaMIB", "rsaIndex"),
    (0, "Nortel-Magellan-Passport-ServerAccessRsaMIB", "rsaConnectionIndex"),
)
if mibBuilder.loadTexts:
    rsaConnectionRowStatusEntry.setStatus("mandatory")
_RsaConnectionRowStatus_Type = RowStatus
_RsaConnectionRowStatus_Object = MibTableColumn
rsaConnectionRowStatus = _RsaConnectionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 4, 1, 1, 1),
    _RsaConnectionRowStatus_Type()
)
rsaConnectionRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsaConnectionRowStatus.setStatus("mandatory")
_RsaConnectionComponentName_Type = DisplayString
_RsaConnectionComponentName_Object = MibTableColumn
rsaConnectionComponentName = _RsaConnectionComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 4, 1, 1, 2),
    _RsaConnectionComponentName_Type()
)
rsaConnectionComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsaConnectionComponentName.setStatus("mandatory")
_RsaConnectionStorageType_Type = StorageType
_RsaConnectionStorageType_Object = MibTableColumn
rsaConnectionStorageType = _RsaConnectionStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 4, 1, 1, 4),
    _RsaConnectionStorageType_Type()
)
rsaConnectionStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsaConnectionStorageType.setStatus("mandatory")


class _RsaConnectionIndex_Type(Integer32):
    """Custom type rsaConnectionIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_RsaConnectionIndex_Type.__name__ = "Integer32"
_RsaConnectionIndex_Object = MibTableColumn
rsaConnectionIndex = _RsaConnectionIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 4, 1, 1, 10),
    _RsaConnectionIndex_Type()
)
rsaConnectionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rsaConnectionIndex.setStatus("mandatory")
_RsaConnectionVc_ObjectIdentity = ObjectIdentity
rsaConnectionVc = _RsaConnectionVc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 4, 2)
)
_RsaConnectionVcRowStatusTable_Object = MibTable
rsaConnectionVcRowStatusTable = _RsaConnectionVcRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 4, 2, 1)
)
if mibBuilder.loadTexts:
    rsaConnectionVcRowStatusTable.setStatus("mandatory")
_RsaConnectionVcRowStatusEntry_Object = MibTableRow
rsaConnectionVcRowStatusEntry = _RsaConnectionVcRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 4, 2, 1, 1)
)
rsaConnectionVcRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-ServerAccessRsaMIB", "rsaIndex"),
    (0, "Nortel-Magellan-Passport-ServerAccessRsaMIB", "rsaConnectionIndex"),
    (0, "Nortel-Magellan-Passport-ServerAccessRsaMIB", "rsaConnectionVcIndex"),
)
if mibBuilder.loadTexts:
    rsaConnectionVcRowStatusEntry.setStatus("mandatory")
_RsaConnectionVcRowStatus_Type = RowStatus
_RsaConnectionVcRowStatus_Object = MibTableColumn
rsaConnectionVcRowStatus = _RsaConnectionVcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 4, 2, 1, 1, 1),
    _RsaConnectionVcRowStatus_Type()
)
rsaConnectionVcRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsaConnectionVcRowStatus.setStatus("mandatory")
_RsaConnectionVcComponentName_Type = DisplayString
_RsaConnectionVcComponentName_Object = MibTableColumn
rsaConnectionVcComponentName = _RsaConnectionVcComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 4, 2, 1, 1, 2),
    _RsaConnectionVcComponentName_Type()
)
rsaConnectionVcComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsaConnectionVcComponentName.setStatus("mandatory")
_RsaConnectionVcStorageType_Type = StorageType
_RsaConnectionVcStorageType_Object = MibTableColumn
rsaConnectionVcStorageType = _RsaConnectionVcStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 4, 2, 1, 1, 4),
    _RsaConnectionVcStorageType_Type()
)
rsaConnectionVcStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsaConnectionVcStorageType.setStatus("mandatory")
_RsaConnectionVcIndex_Type = NonReplicated
_RsaConnectionVcIndex_Object = MibTableColumn
rsaConnectionVcIndex = _RsaConnectionVcIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 4, 2, 1, 1, 10),
    _RsaConnectionVcIndex_Type()
)
rsaConnectionVcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rsaConnectionVcIndex.setStatus("mandatory")
_RsaConnectionVcCadTable_Object = MibTable
rsaConnectionVcCadTable = _RsaConnectionVcCadTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 4, 2, 10)
)
if mibBuilder.loadTexts:
    rsaConnectionVcCadTable.setStatus("mandatory")
_RsaConnectionVcCadEntry_Object = MibTableRow
rsaConnectionVcCadEntry = _RsaConnectionVcCadEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 4, 2, 10, 1)
)
rsaConnectionVcCadEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-ServerAccessRsaMIB", "rsaIndex"),
    (0, "Nortel-Magellan-Passport-ServerAccessRsaMIB", "rsaConnectionIndex"),
    (0, "Nortel-Magellan-Passport-ServerAccessRsaMIB", "rsaConnectionVcIndex"),
)
if mibBuilder.loadTexts:
    rsaConnectionVcCadEntry.setStatus("mandatory")


class _RsaConnectionVcType_Type(Integer32):
    """Custom type rsaConnectionVcType based on Integer32"""
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


_RsaConnectionVcType_Type.__name__ = "Integer32"
_RsaConnectionVcType_Object = MibTableColumn
rsaConnectionVcType = _RsaConnectionVcType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 4, 2, 10, 1, 1),
    _RsaConnectionVcType_Type()
)
rsaConnectionVcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsaConnectionVcType.setStatus("mandatory")


class _RsaConnectionVcState_Type(Integer32):
    """Custom type rsaConnectionVcState based on Integer32"""
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


_RsaConnectionVcState_Type.__name__ = "Integer32"
_RsaConnectionVcState_Object = MibTableColumn
rsaConnectionVcState = _RsaConnectionVcState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 4, 2, 10, 1, 2),
    _RsaConnectionVcState_Type()
)
rsaConnectionVcState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsaConnectionVcState.setStatus("mandatory")


class _RsaConnectionVcPreviousState_Type(Integer32):
    """Custom type rsaConnectionVcPreviousState based on Integer32"""
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


_RsaConnectionVcPreviousState_Type.__name__ = "Integer32"
_RsaConnectionVcPreviousState_Object = MibTableColumn
rsaConnectionVcPreviousState = _RsaConnectionVcPreviousState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 4, 2, 10, 1, 3),
    _RsaConnectionVcPreviousState_Type()
)
rsaConnectionVcPreviousState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsaConnectionVcPreviousState.setStatus("mandatory")


class _RsaConnectionVcDiagnosticCode_Type(Unsigned32):
    """Custom type rsaConnectionVcDiagnosticCode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RsaConnectionVcDiagnosticCode_Type.__name__ = "Unsigned32"
_RsaConnectionVcDiagnosticCode_Object = MibTableColumn
rsaConnectionVcDiagnosticCode = _RsaConnectionVcDiagnosticCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 4, 2, 10, 1, 4),
    _RsaConnectionVcDiagnosticCode_Type()
)
rsaConnectionVcDiagnosticCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsaConnectionVcDiagnosticCode.setStatus("mandatory")


class _RsaConnectionVcPreviousDiagnosticCode_Type(Unsigned32):
    """Custom type rsaConnectionVcPreviousDiagnosticCode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RsaConnectionVcPreviousDiagnosticCode_Type.__name__ = "Unsigned32"
_RsaConnectionVcPreviousDiagnosticCode_Object = MibTableColumn
rsaConnectionVcPreviousDiagnosticCode = _RsaConnectionVcPreviousDiagnosticCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 4, 2, 10, 1, 5),
    _RsaConnectionVcPreviousDiagnosticCode_Type()
)
rsaConnectionVcPreviousDiagnosticCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsaConnectionVcPreviousDiagnosticCode.setStatus("mandatory")


class _RsaConnectionVcCalledNpi_Type(Integer32):
    """Custom type rsaConnectionVcCalledNpi based on Integer32"""
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


_RsaConnectionVcCalledNpi_Type.__name__ = "Integer32"
_RsaConnectionVcCalledNpi_Object = MibTableColumn
rsaConnectionVcCalledNpi = _RsaConnectionVcCalledNpi_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 4, 2, 10, 1, 6),
    _RsaConnectionVcCalledNpi_Type()
)
rsaConnectionVcCalledNpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsaConnectionVcCalledNpi.setStatus("mandatory")


class _RsaConnectionVcCalledDna_Type(DigitString):
    """Custom type rsaConnectionVcCalledDna based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_RsaConnectionVcCalledDna_Type.__name__ = "DigitString"
_RsaConnectionVcCalledDna_Object = MibTableColumn
rsaConnectionVcCalledDna = _RsaConnectionVcCalledDna_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 4, 2, 10, 1, 7),
    _RsaConnectionVcCalledDna_Type()
)
rsaConnectionVcCalledDna.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsaConnectionVcCalledDna.setStatus("mandatory")


class _RsaConnectionVcCalledLcn_Type(Unsigned32):
    """Custom type rsaConnectionVcCalledLcn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RsaConnectionVcCalledLcn_Type.__name__ = "Unsigned32"
_RsaConnectionVcCalledLcn_Object = MibTableColumn
rsaConnectionVcCalledLcn = _RsaConnectionVcCalledLcn_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 4, 2, 10, 1, 8),
    _RsaConnectionVcCalledLcn_Type()
)
rsaConnectionVcCalledLcn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsaConnectionVcCalledLcn.setStatus("mandatory")


class _RsaConnectionVcCallingNpi_Type(Integer32):
    """Custom type rsaConnectionVcCallingNpi based on Integer32"""
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


_RsaConnectionVcCallingNpi_Type.__name__ = "Integer32"
_RsaConnectionVcCallingNpi_Object = MibTableColumn
rsaConnectionVcCallingNpi = _RsaConnectionVcCallingNpi_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 4, 2, 10, 1, 9),
    _RsaConnectionVcCallingNpi_Type()
)
rsaConnectionVcCallingNpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsaConnectionVcCallingNpi.setStatus("mandatory")


class _RsaConnectionVcCallingDna_Type(DigitString):
    """Custom type rsaConnectionVcCallingDna based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_RsaConnectionVcCallingDna_Type.__name__ = "DigitString"
_RsaConnectionVcCallingDna_Object = MibTableColumn
rsaConnectionVcCallingDna = _RsaConnectionVcCallingDna_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 4, 2, 10, 1, 10),
    _RsaConnectionVcCallingDna_Type()
)
rsaConnectionVcCallingDna.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsaConnectionVcCallingDna.setStatus("mandatory")


class _RsaConnectionVcCallingLcn_Type(Unsigned32):
    """Custom type rsaConnectionVcCallingLcn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RsaConnectionVcCallingLcn_Type.__name__ = "Unsigned32"
_RsaConnectionVcCallingLcn_Object = MibTableColumn
rsaConnectionVcCallingLcn = _RsaConnectionVcCallingLcn_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 4, 2, 10, 1, 11),
    _RsaConnectionVcCallingLcn_Type()
)
rsaConnectionVcCallingLcn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsaConnectionVcCallingLcn.setStatus("mandatory")


class _RsaConnectionVcAccountingEnabled_Type(Integer32):
    """Custom type rsaConnectionVcAccountingEnabled based on Integer32"""
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


_RsaConnectionVcAccountingEnabled_Type.__name__ = "Integer32"
_RsaConnectionVcAccountingEnabled_Object = MibTableColumn
rsaConnectionVcAccountingEnabled = _RsaConnectionVcAccountingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 4, 2, 10, 1, 12),
    _RsaConnectionVcAccountingEnabled_Type()
)
rsaConnectionVcAccountingEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsaConnectionVcAccountingEnabled.setStatus("mandatory")


class _RsaConnectionVcFastSelectCall_Type(Integer32):
    """Custom type rsaConnectionVcFastSelectCall based on Integer32"""
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


_RsaConnectionVcFastSelectCall_Type.__name__ = "Integer32"
_RsaConnectionVcFastSelectCall_Object = MibTableColumn
rsaConnectionVcFastSelectCall = _RsaConnectionVcFastSelectCall_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 4, 2, 10, 1, 13),
    _RsaConnectionVcFastSelectCall_Type()
)
rsaConnectionVcFastSelectCall.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsaConnectionVcFastSelectCall.setStatus("mandatory")


class _RsaConnectionVcPathReliability_Type(Integer32):
    """Custom type rsaConnectionVcPathReliability based on Integer32"""
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


_RsaConnectionVcPathReliability_Type.__name__ = "Integer32"
_RsaConnectionVcPathReliability_Object = MibTableColumn
rsaConnectionVcPathReliability = _RsaConnectionVcPathReliability_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 4, 2, 10, 1, 19),
    _RsaConnectionVcPathReliability_Type()
)
rsaConnectionVcPathReliability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsaConnectionVcPathReliability.setStatus("mandatory")


class _RsaConnectionVcAccountingEnd_Type(Integer32):
    """Custom type rsaConnectionVcAccountingEnd based on Integer32"""
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


_RsaConnectionVcAccountingEnd_Type.__name__ = "Integer32"
_RsaConnectionVcAccountingEnd_Object = MibTableColumn
rsaConnectionVcAccountingEnd = _RsaConnectionVcAccountingEnd_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 4, 2, 10, 1, 20),
    _RsaConnectionVcAccountingEnd_Type()
)
rsaConnectionVcAccountingEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsaConnectionVcAccountingEnd.setStatus("mandatory")


class _RsaConnectionVcPriority_Type(Integer32):
    """Custom type rsaConnectionVcPriority based on Integer32"""
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


_RsaConnectionVcPriority_Type.__name__ = "Integer32"
_RsaConnectionVcPriority_Object = MibTableColumn
rsaConnectionVcPriority = _RsaConnectionVcPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 4, 2, 10, 1, 21),
    _RsaConnectionVcPriority_Type()
)
rsaConnectionVcPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsaConnectionVcPriority.setStatus("mandatory")


class _RsaConnectionVcSegmentSize_Type(Unsigned32):
    """Custom type rsaConnectionVcSegmentSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_RsaConnectionVcSegmentSize_Type.__name__ = "Unsigned32"
_RsaConnectionVcSegmentSize_Object = MibTableColumn
rsaConnectionVcSegmentSize = _RsaConnectionVcSegmentSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 4, 2, 10, 1, 22),
    _RsaConnectionVcSegmentSize_Type()
)
rsaConnectionVcSegmentSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsaConnectionVcSegmentSize.setStatus("mandatory")


class _RsaConnectionVcMaxSubnetPktSize_Type(Unsigned32):
    """Custom type rsaConnectionVcMaxSubnetPktSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_RsaConnectionVcMaxSubnetPktSize_Type.__name__ = "Unsigned32"
_RsaConnectionVcMaxSubnetPktSize_Object = MibTableColumn
rsaConnectionVcMaxSubnetPktSize = _RsaConnectionVcMaxSubnetPktSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 4, 2, 10, 1, 27),
    _RsaConnectionVcMaxSubnetPktSize_Type()
)
rsaConnectionVcMaxSubnetPktSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsaConnectionVcMaxSubnetPktSize.setStatus("mandatory")


class _RsaConnectionVcRcosToNetwork_Type(Integer32):
    """Custom type rsaConnectionVcRcosToNetwork based on Integer32"""
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


_RsaConnectionVcRcosToNetwork_Type.__name__ = "Integer32"
_RsaConnectionVcRcosToNetwork_Object = MibTableColumn
rsaConnectionVcRcosToNetwork = _RsaConnectionVcRcosToNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 4, 2, 10, 1, 28),
    _RsaConnectionVcRcosToNetwork_Type()
)
rsaConnectionVcRcosToNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsaConnectionVcRcosToNetwork.setStatus("mandatory")


class _RsaConnectionVcRcosFromNetwork_Type(Integer32):
    """Custom type rsaConnectionVcRcosFromNetwork based on Integer32"""
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


_RsaConnectionVcRcosFromNetwork_Type.__name__ = "Integer32"
_RsaConnectionVcRcosFromNetwork_Object = MibTableColumn
rsaConnectionVcRcosFromNetwork = _RsaConnectionVcRcosFromNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 4, 2, 10, 1, 29),
    _RsaConnectionVcRcosFromNetwork_Type()
)
rsaConnectionVcRcosFromNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsaConnectionVcRcosFromNetwork.setStatus("mandatory")


class _RsaConnectionVcEmissionPriorityToNetwork_Type(Integer32):
    """Custom type rsaConnectionVcEmissionPriorityToNetwork based on Integer32"""
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


_RsaConnectionVcEmissionPriorityToNetwork_Type.__name__ = "Integer32"
_RsaConnectionVcEmissionPriorityToNetwork_Object = MibTableColumn
rsaConnectionVcEmissionPriorityToNetwork = _RsaConnectionVcEmissionPriorityToNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 4, 2, 10, 1, 30),
    _RsaConnectionVcEmissionPriorityToNetwork_Type()
)
rsaConnectionVcEmissionPriorityToNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsaConnectionVcEmissionPriorityToNetwork.setStatus("mandatory")


class _RsaConnectionVcEmissionPriorityFromNetwork_Type(Integer32):
    """Custom type rsaConnectionVcEmissionPriorityFromNetwork based on Integer32"""
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


_RsaConnectionVcEmissionPriorityFromNetwork_Type.__name__ = "Integer32"
_RsaConnectionVcEmissionPriorityFromNetwork_Object = MibTableColumn
rsaConnectionVcEmissionPriorityFromNetwork = _RsaConnectionVcEmissionPriorityFromNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 4, 2, 10, 1, 31),
    _RsaConnectionVcEmissionPriorityFromNetwork_Type()
)
rsaConnectionVcEmissionPriorityFromNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsaConnectionVcEmissionPriorityFromNetwork.setStatus("mandatory")


class _RsaConnectionVcDataPath_Type(AsciiString):
    """Custom type rsaConnectionVcDataPath based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RsaConnectionVcDataPath_Type.__name__ = "AsciiString"
_RsaConnectionVcDataPath_Object = MibTableColumn
rsaConnectionVcDataPath = _RsaConnectionVcDataPath_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 4, 2, 10, 1, 32),
    _RsaConnectionVcDataPath_Type()
)
rsaConnectionVcDataPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsaConnectionVcDataPath.setStatus("mandatory")
_RsaConnectionVcIntdTable_Object = MibTable
rsaConnectionVcIntdTable = _RsaConnectionVcIntdTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 4, 2, 11)
)
if mibBuilder.loadTexts:
    rsaConnectionVcIntdTable.setStatus("mandatory")
_RsaConnectionVcIntdEntry_Object = MibTableRow
rsaConnectionVcIntdEntry = _RsaConnectionVcIntdEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 4, 2, 11, 1)
)
rsaConnectionVcIntdEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-ServerAccessRsaMIB", "rsaIndex"),
    (0, "Nortel-Magellan-Passport-ServerAccessRsaMIB", "rsaConnectionIndex"),
    (0, "Nortel-Magellan-Passport-ServerAccessRsaMIB", "rsaConnectionVcIndex"),
)
if mibBuilder.loadTexts:
    rsaConnectionVcIntdEntry.setStatus("mandatory")


class _RsaConnectionVcCallReferenceNumber_Type(Hex):
    """Custom type rsaConnectionVcCallReferenceNumber based on Hex"""
    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_RsaConnectionVcCallReferenceNumber_Type.__name__ = "Hex"
_RsaConnectionVcCallReferenceNumber_Object = MibTableColumn
rsaConnectionVcCallReferenceNumber = _RsaConnectionVcCallReferenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 4, 2, 11, 1, 1),
    _RsaConnectionVcCallReferenceNumber_Type()
)
rsaConnectionVcCallReferenceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsaConnectionVcCallReferenceNumber.setStatus("mandatory")


class _RsaConnectionVcElapsedTimeTillNow_Type(Unsigned32):
    """Custom type rsaConnectionVcElapsedTimeTillNow based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_RsaConnectionVcElapsedTimeTillNow_Type.__name__ = "Unsigned32"
_RsaConnectionVcElapsedTimeTillNow_Object = MibTableColumn
rsaConnectionVcElapsedTimeTillNow = _RsaConnectionVcElapsedTimeTillNow_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 4, 2, 11, 1, 2),
    _RsaConnectionVcElapsedTimeTillNow_Type()
)
rsaConnectionVcElapsedTimeTillNow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsaConnectionVcElapsedTimeTillNow.setStatus("mandatory")


class _RsaConnectionVcSegmentsRx_Type(Unsigned32):
    """Custom type rsaConnectionVcSegmentsRx based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_RsaConnectionVcSegmentsRx_Type.__name__ = "Unsigned32"
_RsaConnectionVcSegmentsRx_Object = MibTableColumn
rsaConnectionVcSegmentsRx = _RsaConnectionVcSegmentsRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 4, 2, 11, 1, 3),
    _RsaConnectionVcSegmentsRx_Type()
)
rsaConnectionVcSegmentsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsaConnectionVcSegmentsRx.setStatus("mandatory")


class _RsaConnectionVcSegmentsSent_Type(Unsigned32):
    """Custom type rsaConnectionVcSegmentsSent based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_RsaConnectionVcSegmentsSent_Type.__name__ = "Unsigned32"
_RsaConnectionVcSegmentsSent_Object = MibTableColumn
rsaConnectionVcSegmentsSent = _RsaConnectionVcSegmentsSent_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 4, 2, 11, 1, 4),
    _RsaConnectionVcSegmentsSent_Type()
)
rsaConnectionVcSegmentsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsaConnectionVcSegmentsSent.setStatus("mandatory")


class _RsaConnectionVcStartTime_Type(EnterpriseDateAndTime):
    """Custom type rsaConnectionVcStartTime based on EnterpriseDateAndTime"""
    subtypeSpec = EnterpriseDateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(19, 19),
    )


_RsaConnectionVcStartTime_Type.__name__ = "EnterpriseDateAndTime"
_RsaConnectionVcStartTime_Object = MibTableColumn
rsaConnectionVcStartTime = _RsaConnectionVcStartTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 4, 2, 11, 1, 5),
    _RsaConnectionVcStartTime_Type()
)
rsaConnectionVcStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsaConnectionVcStartTime.setStatus("mandatory")
_RsaConnectionVcFrdTable_Object = MibTable
rsaConnectionVcFrdTable = _RsaConnectionVcFrdTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 4, 2, 12)
)
if mibBuilder.loadTexts:
    rsaConnectionVcFrdTable.setStatus("mandatory")
_RsaConnectionVcFrdEntry_Object = MibTableRow
rsaConnectionVcFrdEntry = _RsaConnectionVcFrdEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 4, 2, 12, 1)
)
rsaConnectionVcFrdEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-ServerAccessRsaMIB", "rsaIndex"),
    (0, "Nortel-Magellan-Passport-ServerAccessRsaMIB", "rsaConnectionIndex"),
    (0, "Nortel-Magellan-Passport-ServerAccessRsaMIB", "rsaConnectionVcIndex"),
)
if mibBuilder.loadTexts:
    rsaConnectionVcFrdEntry.setStatus("mandatory")


class _RsaConnectionVcFrmCongestedToSubnet_Type(Unsigned32):
    """Custom type rsaConnectionVcFrmCongestedToSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_RsaConnectionVcFrmCongestedToSubnet_Type.__name__ = "Unsigned32"
_RsaConnectionVcFrmCongestedToSubnet_Object = MibTableColumn
rsaConnectionVcFrmCongestedToSubnet = _RsaConnectionVcFrmCongestedToSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 4, 2, 12, 1, 2),
    _RsaConnectionVcFrmCongestedToSubnet_Type()
)
rsaConnectionVcFrmCongestedToSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsaConnectionVcFrmCongestedToSubnet.setStatus("mandatory")


class _RsaConnectionVcCannotForwardToSubnet_Type(Unsigned32):
    """Custom type rsaConnectionVcCannotForwardToSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_RsaConnectionVcCannotForwardToSubnet_Type.__name__ = "Unsigned32"
_RsaConnectionVcCannotForwardToSubnet_Object = MibTableColumn
rsaConnectionVcCannotForwardToSubnet = _RsaConnectionVcCannotForwardToSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 4, 2, 12, 1, 3),
    _RsaConnectionVcCannotForwardToSubnet_Type()
)
rsaConnectionVcCannotForwardToSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsaConnectionVcCannotForwardToSubnet.setStatus("mandatory")


class _RsaConnectionVcNotDataXferToSubnet_Type(Unsigned32):
    """Custom type rsaConnectionVcNotDataXferToSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_RsaConnectionVcNotDataXferToSubnet_Type.__name__ = "Unsigned32"
_RsaConnectionVcNotDataXferToSubnet_Object = MibTableColumn
rsaConnectionVcNotDataXferToSubnet = _RsaConnectionVcNotDataXferToSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 4, 2, 12, 1, 4),
    _RsaConnectionVcNotDataXferToSubnet_Type()
)
rsaConnectionVcNotDataXferToSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsaConnectionVcNotDataXferToSubnet.setStatus("mandatory")


class _RsaConnectionVcOutOfRangeFrmFromSubnet_Type(Unsigned32):
    """Custom type rsaConnectionVcOutOfRangeFrmFromSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_RsaConnectionVcOutOfRangeFrmFromSubnet_Type.__name__ = "Unsigned32"
_RsaConnectionVcOutOfRangeFrmFromSubnet_Object = MibTableColumn
rsaConnectionVcOutOfRangeFrmFromSubnet = _RsaConnectionVcOutOfRangeFrmFromSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 4, 2, 12, 1, 5),
    _RsaConnectionVcOutOfRangeFrmFromSubnet_Type()
)
rsaConnectionVcOutOfRangeFrmFromSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsaConnectionVcOutOfRangeFrmFromSubnet.setStatus("mandatory")


class _RsaConnectionVcCombErrorsFromSubnet_Type(Unsigned32):
    """Custom type rsaConnectionVcCombErrorsFromSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_RsaConnectionVcCombErrorsFromSubnet_Type.__name__ = "Unsigned32"
_RsaConnectionVcCombErrorsFromSubnet_Object = MibTableColumn
rsaConnectionVcCombErrorsFromSubnet = _RsaConnectionVcCombErrorsFromSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 4, 2, 12, 1, 6),
    _RsaConnectionVcCombErrorsFromSubnet_Type()
)
rsaConnectionVcCombErrorsFromSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsaConnectionVcCombErrorsFromSubnet.setStatus("mandatory")


class _RsaConnectionVcDuplicatesFromSubnet_Type(Unsigned32):
    """Custom type rsaConnectionVcDuplicatesFromSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_RsaConnectionVcDuplicatesFromSubnet_Type.__name__ = "Unsigned32"
_RsaConnectionVcDuplicatesFromSubnet_Object = MibTableColumn
rsaConnectionVcDuplicatesFromSubnet = _RsaConnectionVcDuplicatesFromSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 4, 2, 12, 1, 7),
    _RsaConnectionVcDuplicatesFromSubnet_Type()
)
rsaConnectionVcDuplicatesFromSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsaConnectionVcDuplicatesFromSubnet.setStatus("mandatory")


class _RsaConnectionVcNotDataXferFromSubnet_Type(Unsigned32):
    """Custom type rsaConnectionVcNotDataXferFromSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_RsaConnectionVcNotDataXferFromSubnet_Type.__name__ = "Unsigned32"
_RsaConnectionVcNotDataXferFromSubnet_Object = MibTableColumn
rsaConnectionVcNotDataXferFromSubnet = _RsaConnectionVcNotDataXferFromSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 4, 2, 12, 1, 8),
    _RsaConnectionVcNotDataXferFromSubnet_Type()
)
rsaConnectionVcNotDataXferFromSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsaConnectionVcNotDataXferFromSubnet.setStatus("mandatory")


class _RsaConnectionVcFrmLossTimeouts_Type(Unsigned32):
    """Custom type rsaConnectionVcFrmLossTimeouts based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_RsaConnectionVcFrmLossTimeouts_Type.__name__ = "Unsigned32"
_RsaConnectionVcFrmLossTimeouts_Object = MibTableColumn
rsaConnectionVcFrmLossTimeouts = _RsaConnectionVcFrmLossTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 4, 2, 12, 1, 9),
    _RsaConnectionVcFrmLossTimeouts_Type()
)
rsaConnectionVcFrmLossTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsaConnectionVcFrmLossTimeouts.setStatus("mandatory")


class _RsaConnectionVcOoSeqByteCntExceeded_Type(Unsigned32):
    """Custom type rsaConnectionVcOoSeqByteCntExceeded based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_RsaConnectionVcOoSeqByteCntExceeded_Type.__name__ = "Unsigned32"
_RsaConnectionVcOoSeqByteCntExceeded_Object = MibTableColumn
rsaConnectionVcOoSeqByteCntExceeded = _RsaConnectionVcOoSeqByteCntExceeded_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 4, 2, 12, 1, 10),
    _RsaConnectionVcOoSeqByteCntExceeded_Type()
)
rsaConnectionVcOoSeqByteCntExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsaConnectionVcOoSeqByteCntExceeded.setStatus("mandatory")


class _RsaConnectionVcPeakOoSeqPktCount_Type(Unsigned32):
    """Custom type rsaConnectionVcPeakOoSeqPktCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_RsaConnectionVcPeakOoSeqPktCount_Type.__name__ = "Unsigned32"
_RsaConnectionVcPeakOoSeqPktCount_Object = MibTableColumn
rsaConnectionVcPeakOoSeqPktCount = _RsaConnectionVcPeakOoSeqPktCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 4, 2, 12, 1, 11),
    _RsaConnectionVcPeakOoSeqPktCount_Type()
)
rsaConnectionVcPeakOoSeqPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsaConnectionVcPeakOoSeqPktCount.setStatus("mandatory")


class _RsaConnectionVcPeakOoSeqFrmForwarded_Type(Unsigned32):
    """Custom type rsaConnectionVcPeakOoSeqFrmForwarded based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_RsaConnectionVcPeakOoSeqFrmForwarded_Type.__name__ = "Unsigned32"
_RsaConnectionVcPeakOoSeqFrmForwarded_Object = MibTableColumn
rsaConnectionVcPeakOoSeqFrmForwarded = _RsaConnectionVcPeakOoSeqFrmForwarded_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 4, 2, 12, 1, 12),
    _RsaConnectionVcPeakOoSeqFrmForwarded_Type()
)
rsaConnectionVcPeakOoSeqFrmForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsaConnectionVcPeakOoSeqFrmForwarded.setStatus("mandatory")


class _RsaConnectionVcSendSequenceNumber_Type(Unsigned32):
    """Custom type rsaConnectionVcSendSequenceNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_RsaConnectionVcSendSequenceNumber_Type.__name__ = "Unsigned32"
_RsaConnectionVcSendSequenceNumber_Object = MibTableColumn
rsaConnectionVcSendSequenceNumber = _RsaConnectionVcSendSequenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 4, 2, 12, 1, 13),
    _RsaConnectionVcSendSequenceNumber_Type()
)
rsaConnectionVcSendSequenceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsaConnectionVcSendSequenceNumber.setStatus("mandatory")


class _RsaConnectionVcPktRetryTimeouts_Type(Unsigned32):
    """Custom type rsaConnectionVcPktRetryTimeouts based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_RsaConnectionVcPktRetryTimeouts_Type.__name__ = "Unsigned32"
_RsaConnectionVcPktRetryTimeouts_Object = MibTableColumn
rsaConnectionVcPktRetryTimeouts = _RsaConnectionVcPktRetryTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 4, 2, 12, 1, 15),
    _RsaConnectionVcPktRetryTimeouts_Type()
)
rsaConnectionVcPktRetryTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsaConnectionVcPktRetryTimeouts.setStatus("mandatory")


class _RsaConnectionVcPeakRetryQueueSize_Type(Unsigned32):
    """Custom type rsaConnectionVcPeakRetryQueueSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_RsaConnectionVcPeakRetryQueueSize_Type.__name__ = "Unsigned32"
_RsaConnectionVcPeakRetryQueueSize_Object = MibTableColumn
rsaConnectionVcPeakRetryQueueSize = _RsaConnectionVcPeakRetryQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 4, 2, 12, 1, 16),
    _RsaConnectionVcPeakRetryQueueSize_Type()
)
rsaConnectionVcPeakRetryQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsaConnectionVcPeakRetryQueueSize.setStatus("mandatory")


class _RsaConnectionVcSubnetRecoveries_Type(Unsigned32):
    """Custom type rsaConnectionVcSubnetRecoveries based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_RsaConnectionVcSubnetRecoveries_Type.__name__ = "Unsigned32"
_RsaConnectionVcSubnetRecoveries_Object = MibTableColumn
rsaConnectionVcSubnetRecoveries = _RsaConnectionVcSubnetRecoveries_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 4, 2, 12, 1, 17),
    _RsaConnectionVcSubnetRecoveries_Type()
)
rsaConnectionVcSubnetRecoveries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsaConnectionVcSubnetRecoveries.setStatus("mandatory")


class _RsaConnectionVcOoSeqPktCntExceeded_Type(Unsigned32):
    """Custom type rsaConnectionVcOoSeqPktCntExceeded based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RsaConnectionVcOoSeqPktCntExceeded_Type.__name__ = "Unsigned32"
_RsaConnectionVcOoSeqPktCntExceeded_Object = MibTableColumn
rsaConnectionVcOoSeqPktCntExceeded = _RsaConnectionVcOoSeqPktCntExceeded_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 4, 2, 12, 1, 19),
    _RsaConnectionVcOoSeqPktCntExceeded_Type()
)
rsaConnectionVcOoSeqPktCntExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsaConnectionVcOoSeqPktCntExceeded.setStatus("mandatory")


class _RsaConnectionVcPeakOoSeqByteCount_Type(Unsigned32):
    """Custom type rsaConnectionVcPeakOoSeqByteCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50000),
    )


_RsaConnectionVcPeakOoSeqByteCount_Type.__name__ = "Unsigned32"
_RsaConnectionVcPeakOoSeqByteCount_Object = MibTableColumn
rsaConnectionVcPeakOoSeqByteCount = _RsaConnectionVcPeakOoSeqByteCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 4, 2, 12, 1, 20),
    _RsaConnectionVcPeakOoSeqByteCount_Type()
)
rsaConnectionVcPeakOoSeqByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsaConnectionVcPeakOoSeqByteCount.setStatus("mandatory")
_RsaConnectionVcDmepTable_Object = MibTable
rsaConnectionVcDmepTable = _RsaConnectionVcDmepTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 4, 2, 417)
)
if mibBuilder.loadTexts:
    rsaConnectionVcDmepTable.setStatus("mandatory")
_RsaConnectionVcDmepEntry_Object = MibTableRow
rsaConnectionVcDmepEntry = _RsaConnectionVcDmepEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 4, 2, 417, 1)
)
rsaConnectionVcDmepEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-ServerAccessRsaMIB", "rsaIndex"),
    (0, "Nortel-Magellan-Passport-ServerAccessRsaMIB", "rsaConnectionIndex"),
    (0, "Nortel-Magellan-Passport-ServerAccessRsaMIB", "rsaConnectionVcIndex"),
    (0, "Nortel-Magellan-Passport-ServerAccessRsaMIB", "rsaConnectionVcDmepValue"),
)
if mibBuilder.loadTexts:
    rsaConnectionVcDmepEntry.setStatus("mandatory")
_RsaConnectionVcDmepValue_Type = RowPointer
_RsaConnectionVcDmepValue_Object = MibTableColumn
rsaConnectionVcDmepValue = _RsaConnectionVcDmepValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 4, 2, 417, 1, 1),
    _RsaConnectionVcDmepValue_Type()
)
rsaConnectionVcDmepValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsaConnectionVcDmepValue.setStatus("mandatory")
_RsaConnectionOperationalTable_Object = MibTable
rsaConnectionOperationalTable = _RsaConnectionOperationalTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 4, 10)
)
if mibBuilder.loadTexts:
    rsaConnectionOperationalTable.setStatus("mandatory")
_RsaConnectionOperationalEntry_Object = MibTableRow
rsaConnectionOperationalEntry = _RsaConnectionOperationalEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 4, 10, 1)
)
rsaConnectionOperationalEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-ServerAccessRsaMIB", "rsaIndex"),
    (0, "Nortel-Magellan-Passport-ServerAccessRsaMIB", "rsaConnectionIndex"),
)
if mibBuilder.loadTexts:
    rsaConnectionOperationalEntry.setStatus("mandatory")


class _RsaConnectionRemoteName_Type(AsciiString):
    """Custom type rsaConnectionRemoteName based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RsaConnectionRemoteName_Type.__name__ = "AsciiString"
_RsaConnectionRemoteName_Object = MibTableColumn
rsaConnectionRemoteName = _RsaConnectionRemoteName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 4, 10, 1, 1),
    _RsaConnectionRemoteName_Type()
)
rsaConnectionRemoteName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsaConnectionRemoteName.setStatus("mandatory")


class _RsaConnectionCallState_Type(Integer32):
    """Custom type rsaConnectionCallState based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("acceptingCall", 3),
          ("calling", 2),
          ("clearingCall", 7),
          ("creatingVc", 1),
          ("dataTransfer", 6),
          ("establishingLapf", 5),
          ("initializing", 0),
          ("registeringFmo", 4),
          ("terminated", 10),
          ("terminating", 8),
          ("terminatingVc", 9))
    )


_RsaConnectionCallState_Type.__name__ = "Integer32"
_RsaConnectionCallState_Object = MibTableColumn
rsaConnectionCallState = _RsaConnectionCallState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 4, 10, 1, 2),
    _RsaConnectionCallState_Type()
)
rsaConnectionCallState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsaConnectionCallState.setStatus("mandatory")
_RsaConnectionServerStatsTable_Object = MibTable
rsaConnectionServerStatsTable = _RsaConnectionServerStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 4, 11)
)
if mibBuilder.loadTexts:
    rsaConnectionServerStatsTable.setStatus("mandatory")
_RsaConnectionServerStatsEntry_Object = MibTableRow
rsaConnectionServerStatsEntry = _RsaConnectionServerStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 4, 11, 1)
)
rsaConnectionServerStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-ServerAccessRsaMIB", "rsaIndex"),
    (0, "Nortel-Magellan-Passport-ServerAccessRsaMIB", "rsaConnectionIndex"),
)
if mibBuilder.loadTexts:
    rsaConnectionServerStatsEntry.setStatus("mandatory")
_RsaConnectionVncsRequests_Type = Counter32
_RsaConnectionVncsRequests_Object = MibTableColumn
rsaConnectionVncsRequests = _RsaConnectionVncsRequests_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 4, 11, 1, 1),
    _RsaConnectionVncsRequests_Type()
)
rsaConnectionVncsRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsaConnectionVncsRequests.setStatus("mandatory")
_RsaConnectionVncsReplies_Type = Counter32
_RsaConnectionVncsReplies_Object = MibTableColumn
rsaConnectionVncsReplies = _RsaConnectionVncsReplies_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 4, 11, 1, 2),
    _RsaConnectionVncsReplies_Type()
)
rsaConnectionVncsReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsaConnectionVncsReplies.setStatus("mandatory")
_RsaConnectionLapfStatusTable_Object = MibTable
rsaConnectionLapfStatusTable = _RsaConnectionLapfStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 4, 12)
)
if mibBuilder.loadTexts:
    rsaConnectionLapfStatusTable.setStatus("mandatory")
_RsaConnectionLapfStatusEntry_Object = MibTableRow
rsaConnectionLapfStatusEntry = _RsaConnectionLapfStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 4, 12, 1)
)
rsaConnectionLapfStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-ServerAccessRsaMIB", "rsaIndex"),
    (0, "Nortel-Magellan-Passport-ServerAccessRsaMIB", "rsaConnectionIndex"),
)
if mibBuilder.loadTexts:
    rsaConnectionLapfStatusEntry.setStatus("mandatory")


class _RsaConnectionLapfState_Type(Integer32):
    """Custom type rsaConnectionLapfState based on Integer32"""
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


_RsaConnectionLapfState_Type.__name__ = "Integer32"
_RsaConnectionLapfState_Object = MibTableColumn
rsaConnectionLapfState = _RsaConnectionLapfState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 4, 12, 1, 1),
    _RsaConnectionLapfState_Type()
)
rsaConnectionLapfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsaConnectionLapfState.setStatus("mandatory")
_RsaConnectionLapfQueueSize_Type = Counter32
_RsaConnectionLapfQueueSize_Object = MibTableColumn
rsaConnectionLapfQueueSize = _RsaConnectionLapfQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 4, 12, 1, 4),
    _RsaConnectionLapfQueueSize_Type()
)
rsaConnectionLapfQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsaConnectionLapfQueueSize.setStatus("mandatory")
_RsaConnectionLapfStatsTable_Object = MibTable
rsaConnectionLapfStatsTable = _RsaConnectionLapfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 4, 13)
)
if mibBuilder.loadTexts:
    rsaConnectionLapfStatsTable.setStatus("mandatory")
_RsaConnectionLapfStatsEntry_Object = MibTableRow
rsaConnectionLapfStatsEntry = _RsaConnectionLapfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 4, 13, 1)
)
rsaConnectionLapfStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-ServerAccessRsaMIB", "rsaIndex"),
    (0, "Nortel-Magellan-Passport-ServerAccessRsaMIB", "rsaConnectionIndex"),
)
if mibBuilder.loadTexts:
    rsaConnectionLapfStatsEntry.setStatus("mandatory")
_RsaConnectionLapfStateChanges_Type = Counter32
_RsaConnectionLapfStateChanges_Object = MibTableColumn
rsaConnectionLapfStateChanges = _RsaConnectionLapfStateChanges_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 4, 13, 1, 1),
    _RsaConnectionLapfStateChanges_Type()
)
rsaConnectionLapfStateChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsaConnectionLapfStateChanges.setStatus("mandatory")
_RsaConnectionLapfRemoteBusy_Type = Counter32
_RsaConnectionLapfRemoteBusy_Object = MibTableColumn
rsaConnectionLapfRemoteBusy = _RsaConnectionLapfRemoteBusy_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 4, 13, 1, 2),
    _RsaConnectionLapfRemoteBusy_Type()
)
rsaConnectionLapfRemoteBusy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsaConnectionLapfRemoteBusy.setStatus("mandatory")
_RsaConnectionLapfAckTimeouts_Type = Counter32
_RsaConnectionLapfAckTimeouts_Object = MibTableColumn
rsaConnectionLapfAckTimeouts = _RsaConnectionLapfAckTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 4, 13, 1, 3),
    _RsaConnectionLapfAckTimeouts_Type()
)
rsaConnectionLapfAckTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsaConnectionLapfAckTimeouts.setStatus("mandatory")
_RsaConnectionLapfRejectFramesRx_Type = Counter32
_RsaConnectionLapfRejectFramesRx_Object = MibTableColumn
rsaConnectionLapfRejectFramesRx = _RsaConnectionLapfRejectFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 4, 13, 1, 4),
    _RsaConnectionLapfRejectFramesRx_Type()
)
rsaConnectionLapfRejectFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsaConnectionLapfRejectFramesRx.setStatus("mandatory")
_RsaConnectionLapfIFramesTx_Type = Counter32
_RsaConnectionLapfIFramesTx_Object = MibTableColumn
rsaConnectionLapfIFramesTx = _RsaConnectionLapfIFramesTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 4, 13, 1, 5),
    _RsaConnectionLapfIFramesTx_Type()
)
rsaConnectionLapfIFramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsaConnectionLapfIFramesTx.setStatus("mandatory")
_RsaConnectionLapfIFramesTxDiscarded_Type = Counter32
_RsaConnectionLapfIFramesTxDiscarded_Object = MibTableColumn
rsaConnectionLapfIFramesTxDiscarded = _RsaConnectionLapfIFramesTxDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 4, 13, 1, 6),
    _RsaConnectionLapfIFramesTxDiscarded_Type()
)
rsaConnectionLapfIFramesTxDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsaConnectionLapfIFramesTxDiscarded.setStatus("mandatory")
_RsaConnectionLapfIFramesRx_Type = Counter32
_RsaConnectionLapfIFramesRx_Object = MibTableColumn
rsaConnectionLapfIFramesRx = _RsaConnectionLapfIFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 4, 13, 1, 7),
    _RsaConnectionLapfIFramesRx_Type()
)
rsaConnectionLapfIFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsaConnectionLapfIFramesRx.setStatus("mandatory")
_RsaConnectionLapfIFramesRxDiscarded_Type = Counter32
_RsaConnectionLapfIFramesRxDiscarded_Object = MibTableColumn
rsaConnectionLapfIFramesRxDiscarded = _RsaConnectionLapfIFramesRxDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 4, 13, 1, 8),
    _RsaConnectionLapfIFramesRxDiscarded_Type()
)
rsaConnectionLapfIFramesRxDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsaConnectionLapfIFramesRxDiscarded.setStatus("mandatory")
_RsaOptionsTable_Object = MibTable
rsaOptionsTable = _RsaOptionsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 10)
)
if mibBuilder.loadTexts:
    rsaOptionsTable.setStatus("mandatory")
_RsaOptionsEntry_Object = MibTableRow
rsaOptionsEntry = _RsaOptionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 10, 1)
)
rsaOptionsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-ServerAccessRsaMIB", "rsaIndex"),
)
if mibBuilder.loadTexts:
    rsaOptionsEntry.setStatus("mandatory")
_RsaLogicalProcessor_Type = Link
_RsaLogicalProcessor_Object = MibTableColumn
rsaLogicalProcessor = _RsaLogicalProcessor_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 10, 1, 2),
    _RsaLogicalProcessor_Type()
)
rsaLogicalProcessor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsaLogicalProcessor.setStatus("mandatory")
_RsaStateTable_Object = MibTable
rsaStateTable = _RsaStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 11)
)
if mibBuilder.loadTexts:
    rsaStateTable.setStatus("mandatory")
_RsaStateEntry_Object = MibTableRow
rsaStateEntry = _RsaStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 11, 1)
)
rsaStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-ServerAccessRsaMIB", "rsaIndex"),
)
if mibBuilder.loadTexts:
    rsaStateEntry.setStatus("mandatory")


class _RsaAdminState_Type(Integer32):
    """Custom type rsaAdminState based on Integer32"""
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


_RsaAdminState_Type.__name__ = "Integer32"
_RsaAdminState_Object = MibTableColumn
rsaAdminState = _RsaAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 11, 1, 1),
    _RsaAdminState_Type()
)
rsaAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsaAdminState.setStatus("mandatory")


class _RsaOperationalState_Type(Integer32):
    """Custom type rsaOperationalState based on Integer32"""
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


_RsaOperationalState_Type.__name__ = "Integer32"
_RsaOperationalState_Object = MibTableColumn
rsaOperationalState = _RsaOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 11, 1, 2),
    _RsaOperationalState_Type()
)
rsaOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsaOperationalState.setStatus("mandatory")


class _RsaUsageState_Type(Integer32):
    """Custom type rsaUsageState based on Integer32"""
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


_RsaUsageState_Type.__name__ = "Integer32"
_RsaUsageState_Object = MibTableColumn
rsaUsageState = _RsaUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 11, 1, 3),
    _RsaUsageState_Type()
)
rsaUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsaUsageState.setStatus("mandatory")
_RsaOperationalTable_Object = MibTable
rsaOperationalTable = _RsaOperationalTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 12)
)
if mibBuilder.loadTexts:
    rsaOperationalTable.setStatus("mandatory")
_RsaOperationalEntry_Object = MibTableRow
rsaOperationalEntry = _RsaOperationalEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 12, 1)
)
rsaOperationalEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-ServerAccessRsaMIB", "rsaIndex"),
)
if mibBuilder.loadTexts:
    rsaOperationalEntry.setStatus("mandatory")


class _RsaMaxRsiConnections_Type(Integer32):
    """Custom type rsaMaxRsiConnections based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 1000),
    )


_RsaMaxRsiConnections_Type.__name__ = "Integer32"
_RsaMaxRsiConnections_Object = MibTableColumn
rsaMaxRsiConnections = _RsaMaxRsiConnections_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 12, 1, 2),
    _RsaMaxRsiConnections_Type()
)
rsaMaxRsiConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsaMaxRsiConnections.setStatus("mandatory")


class _RsaRsiConnections_Type(Integer32):
    """Custom type rsaRsiConnections based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_RsaRsiConnections_Type.__name__ = "Integer32"
_RsaRsiConnections_Object = MibTableColumn
rsaRsiConnections = _RsaRsiConnections_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 108, 12, 1, 3),
    _RsaRsiConnections_Type()
)
rsaRsiConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsaRsiConnections.setStatus("mandatory")
_ServerAccessRsaMIB_ObjectIdentity = ObjectIdentity
serverAccessRsaMIB = _ServerAccessRsaMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 116)
)
_ServerAccessRsaGroup_ObjectIdentity = ObjectIdentity
serverAccessRsaGroup = _ServerAccessRsaGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 116, 1)
)
_ServerAccessRsaGroupBE_ObjectIdentity = ObjectIdentity
serverAccessRsaGroupBE = _ServerAccessRsaGroupBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 116, 1, 5)
)
_ServerAccessRsaGroupBE01_ObjectIdentity = ObjectIdentity
serverAccessRsaGroupBE01 = _ServerAccessRsaGroupBE01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 116, 1, 5, 2)
)
_ServerAccessRsaGroupBE01A_ObjectIdentity = ObjectIdentity
serverAccessRsaGroupBE01A = _ServerAccessRsaGroupBE01A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 116, 1, 5, 2, 2)
)
_ServerAccessRsaCapabilities_ObjectIdentity = ObjectIdentity
serverAccessRsaCapabilities = _ServerAccessRsaCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 116, 3)
)
_ServerAccessRsaCapabilitiesBE_ObjectIdentity = ObjectIdentity
serverAccessRsaCapabilitiesBE = _ServerAccessRsaCapabilitiesBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 116, 3, 5)
)
_ServerAccessRsaCapabilitiesBE01_ObjectIdentity = ObjectIdentity
serverAccessRsaCapabilitiesBE01 = _ServerAccessRsaCapabilitiesBE01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 116, 3, 5, 2)
)
_ServerAccessRsaCapabilitiesBE01A_ObjectIdentity = ObjectIdentity
serverAccessRsaCapabilitiesBE01A = _ServerAccessRsaCapabilitiesBE01A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 116, 3, 5, 2, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-Magellan-Passport-ServerAccessRsaMIB",
    **{"rsa": rsa,
       "rsaRowStatusTable": rsaRowStatusTable,
       "rsaRowStatusEntry": rsaRowStatusEntry,
       "rsaRowStatus": rsaRowStatus,
       "rsaComponentName": rsaComponentName,
       "rsaStorageType": rsaStorageType,
       "rsaIndex": rsaIndex,
       "rsaDna": rsaDna,
       "rsaDnaRowStatusTable": rsaDnaRowStatusTable,
       "rsaDnaRowStatusEntry": rsaDnaRowStatusEntry,
       "rsaDnaRowStatus": rsaDnaRowStatus,
       "rsaDnaComponentName": rsaDnaComponentName,
       "rsaDnaStorageType": rsaDnaStorageType,
       "rsaDnaIndex": rsaDnaIndex,
       "rsaDnaCug": rsaDnaCug,
       "rsaDnaCugRowStatusTable": rsaDnaCugRowStatusTable,
       "rsaDnaCugRowStatusEntry": rsaDnaCugRowStatusEntry,
       "rsaDnaCugRowStatus": rsaDnaCugRowStatus,
       "rsaDnaCugComponentName": rsaDnaCugComponentName,
       "rsaDnaCugStorageType": rsaDnaCugStorageType,
       "rsaDnaCugIndex": rsaDnaCugIndex,
       "rsaDnaCugCugOptionsTable": rsaDnaCugCugOptionsTable,
       "rsaDnaCugCugOptionsEntry": rsaDnaCugCugOptionsEntry,
       "rsaDnaCugType": rsaDnaCugType,
       "rsaDnaCugDnic": rsaDnaCugDnic,
       "rsaDnaCugInterlockCode": rsaDnaCugInterlockCode,
       "rsaDnaCugPreferential": rsaDnaCugPreferential,
       "rsaDnaCugOutCalls": rsaDnaCugOutCalls,
       "rsaDnaCugIncCalls": rsaDnaCugIncCalls,
       "rsaDnaCugPrivileged": rsaDnaCugPrivileged,
       "rsaDnaAddressTable": rsaDnaAddressTable,
       "rsaDnaAddressEntry": rsaDnaAddressEntry,
       "rsaDnaNumberingPlanIndicator": rsaDnaNumberingPlanIndicator,
       "rsaDnaDataNetworkAddress": rsaDnaDataNetworkAddress,
       "rsaDnaOutgoingOptionsTable": rsaDnaOutgoingOptionsTable,
       "rsaDnaOutgoingOptionsEntry": rsaDnaOutgoingOptionsEntry,
       "rsaDnaOutCalls": rsaDnaOutCalls,
       "rsaDnaIncomingOptionsTable": rsaDnaIncomingOptionsTable,
       "rsaDnaIncomingOptionsEntry": rsaDnaIncomingOptionsEntry,
       "rsaDnaIncCalls": rsaDnaIncCalls,
       "rsaDnaIncAccess": rsaDnaIncAccess,
       "rsaVncsAccess": rsaVncsAccess,
       "rsaVncsAccessRowStatusTable": rsaVncsAccessRowStatusTable,
       "rsaVncsAccessRowStatusEntry": rsaVncsAccessRowStatusEntry,
       "rsaVncsAccessRowStatus": rsaVncsAccessRowStatus,
       "rsaVncsAccessComponentName": rsaVncsAccessComponentName,
       "rsaVncsAccessStorageType": rsaVncsAccessStorageType,
       "rsaVncsAccessIndex": rsaVncsAccessIndex,
       "rsaVncsAccessProvisionedTable": rsaVncsAccessProvisionedTable,
       "rsaVncsAccessProvisionedEntry": rsaVncsAccessProvisionedEntry,
       "rsaVncsAccessTimeToLive": rsaVncsAccessTimeToLive,
       "rsaVncsAccessStateTable": rsaVncsAccessStateTable,
       "rsaVncsAccessStateEntry": rsaVncsAccessStateEntry,
       "rsaVncsAccessAdminState": rsaVncsAccessAdminState,
       "rsaVncsAccessOperationalState": rsaVncsAccessOperationalState,
       "rsaVncsAccessUsageState": rsaVncsAccessUsageState,
       "rsaVncsAccessOperationalTable": rsaVncsAccessOperationalTable,
       "rsaVncsAccessOperationalEntry": rsaVncsAccessOperationalEntry,
       "rsaVncsAccessRequestsSent": rsaVncsAccessRequestsSent,
       "rsaVncsAccessRepliesReceived": rsaVncsAccessRepliesReceived,
       "rsaVncsAccessRequestsQueued": rsaVncsAccessRequestsQueued,
       "rsaVncsAccessRequestsDiscarded": rsaVncsAccessRequestsDiscarded,
       "rsaConnection": rsaConnection,
       "rsaConnectionRowStatusTable": rsaConnectionRowStatusTable,
       "rsaConnectionRowStatusEntry": rsaConnectionRowStatusEntry,
       "rsaConnectionRowStatus": rsaConnectionRowStatus,
       "rsaConnectionComponentName": rsaConnectionComponentName,
       "rsaConnectionStorageType": rsaConnectionStorageType,
       "rsaConnectionIndex": rsaConnectionIndex,
       "rsaConnectionVc": rsaConnectionVc,
       "rsaConnectionVcRowStatusTable": rsaConnectionVcRowStatusTable,
       "rsaConnectionVcRowStatusEntry": rsaConnectionVcRowStatusEntry,
       "rsaConnectionVcRowStatus": rsaConnectionVcRowStatus,
       "rsaConnectionVcComponentName": rsaConnectionVcComponentName,
       "rsaConnectionVcStorageType": rsaConnectionVcStorageType,
       "rsaConnectionVcIndex": rsaConnectionVcIndex,
       "rsaConnectionVcCadTable": rsaConnectionVcCadTable,
       "rsaConnectionVcCadEntry": rsaConnectionVcCadEntry,
       "rsaConnectionVcType": rsaConnectionVcType,
       "rsaConnectionVcState": rsaConnectionVcState,
       "rsaConnectionVcPreviousState": rsaConnectionVcPreviousState,
       "rsaConnectionVcDiagnosticCode": rsaConnectionVcDiagnosticCode,
       "rsaConnectionVcPreviousDiagnosticCode": rsaConnectionVcPreviousDiagnosticCode,
       "rsaConnectionVcCalledNpi": rsaConnectionVcCalledNpi,
       "rsaConnectionVcCalledDna": rsaConnectionVcCalledDna,
       "rsaConnectionVcCalledLcn": rsaConnectionVcCalledLcn,
       "rsaConnectionVcCallingNpi": rsaConnectionVcCallingNpi,
       "rsaConnectionVcCallingDna": rsaConnectionVcCallingDna,
       "rsaConnectionVcCallingLcn": rsaConnectionVcCallingLcn,
       "rsaConnectionVcAccountingEnabled": rsaConnectionVcAccountingEnabled,
       "rsaConnectionVcFastSelectCall": rsaConnectionVcFastSelectCall,
       "rsaConnectionVcPathReliability": rsaConnectionVcPathReliability,
       "rsaConnectionVcAccountingEnd": rsaConnectionVcAccountingEnd,
       "rsaConnectionVcPriority": rsaConnectionVcPriority,
       "rsaConnectionVcSegmentSize": rsaConnectionVcSegmentSize,
       "rsaConnectionVcMaxSubnetPktSize": rsaConnectionVcMaxSubnetPktSize,
       "rsaConnectionVcRcosToNetwork": rsaConnectionVcRcosToNetwork,
       "rsaConnectionVcRcosFromNetwork": rsaConnectionVcRcosFromNetwork,
       "rsaConnectionVcEmissionPriorityToNetwork": rsaConnectionVcEmissionPriorityToNetwork,
       "rsaConnectionVcEmissionPriorityFromNetwork": rsaConnectionVcEmissionPriorityFromNetwork,
       "rsaConnectionVcDataPath": rsaConnectionVcDataPath,
       "rsaConnectionVcIntdTable": rsaConnectionVcIntdTable,
       "rsaConnectionVcIntdEntry": rsaConnectionVcIntdEntry,
       "rsaConnectionVcCallReferenceNumber": rsaConnectionVcCallReferenceNumber,
       "rsaConnectionVcElapsedTimeTillNow": rsaConnectionVcElapsedTimeTillNow,
       "rsaConnectionVcSegmentsRx": rsaConnectionVcSegmentsRx,
       "rsaConnectionVcSegmentsSent": rsaConnectionVcSegmentsSent,
       "rsaConnectionVcStartTime": rsaConnectionVcStartTime,
       "rsaConnectionVcFrdTable": rsaConnectionVcFrdTable,
       "rsaConnectionVcFrdEntry": rsaConnectionVcFrdEntry,
       "rsaConnectionVcFrmCongestedToSubnet": rsaConnectionVcFrmCongestedToSubnet,
       "rsaConnectionVcCannotForwardToSubnet": rsaConnectionVcCannotForwardToSubnet,
       "rsaConnectionVcNotDataXferToSubnet": rsaConnectionVcNotDataXferToSubnet,
       "rsaConnectionVcOutOfRangeFrmFromSubnet": rsaConnectionVcOutOfRangeFrmFromSubnet,
       "rsaConnectionVcCombErrorsFromSubnet": rsaConnectionVcCombErrorsFromSubnet,
       "rsaConnectionVcDuplicatesFromSubnet": rsaConnectionVcDuplicatesFromSubnet,
       "rsaConnectionVcNotDataXferFromSubnet": rsaConnectionVcNotDataXferFromSubnet,
       "rsaConnectionVcFrmLossTimeouts": rsaConnectionVcFrmLossTimeouts,
       "rsaConnectionVcOoSeqByteCntExceeded": rsaConnectionVcOoSeqByteCntExceeded,
       "rsaConnectionVcPeakOoSeqPktCount": rsaConnectionVcPeakOoSeqPktCount,
       "rsaConnectionVcPeakOoSeqFrmForwarded": rsaConnectionVcPeakOoSeqFrmForwarded,
       "rsaConnectionVcSendSequenceNumber": rsaConnectionVcSendSequenceNumber,
       "rsaConnectionVcPktRetryTimeouts": rsaConnectionVcPktRetryTimeouts,
       "rsaConnectionVcPeakRetryQueueSize": rsaConnectionVcPeakRetryQueueSize,
       "rsaConnectionVcSubnetRecoveries": rsaConnectionVcSubnetRecoveries,
       "rsaConnectionVcOoSeqPktCntExceeded": rsaConnectionVcOoSeqPktCntExceeded,
       "rsaConnectionVcPeakOoSeqByteCount": rsaConnectionVcPeakOoSeqByteCount,
       "rsaConnectionVcDmepTable": rsaConnectionVcDmepTable,
       "rsaConnectionVcDmepEntry": rsaConnectionVcDmepEntry,
       "rsaConnectionVcDmepValue": rsaConnectionVcDmepValue,
       "rsaConnectionOperationalTable": rsaConnectionOperationalTable,
       "rsaConnectionOperationalEntry": rsaConnectionOperationalEntry,
       "rsaConnectionRemoteName": rsaConnectionRemoteName,
       "rsaConnectionCallState": rsaConnectionCallState,
       "rsaConnectionServerStatsTable": rsaConnectionServerStatsTable,
       "rsaConnectionServerStatsEntry": rsaConnectionServerStatsEntry,
       "rsaConnectionVncsRequests": rsaConnectionVncsRequests,
       "rsaConnectionVncsReplies": rsaConnectionVncsReplies,
       "rsaConnectionLapfStatusTable": rsaConnectionLapfStatusTable,
       "rsaConnectionLapfStatusEntry": rsaConnectionLapfStatusEntry,
       "rsaConnectionLapfState": rsaConnectionLapfState,
       "rsaConnectionLapfQueueSize": rsaConnectionLapfQueueSize,
       "rsaConnectionLapfStatsTable": rsaConnectionLapfStatsTable,
       "rsaConnectionLapfStatsEntry": rsaConnectionLapfStatsEntry,
       "rsaConnectionLapfStateChanges": rsaConnectionLapfStateChanges,
       "rsaConnectionLapfRemoteBusy": rsaConnectionLapfRemoteBusy,
       "rsaConnectionLapfAckTimeouts": rsaConnectionLapfAckTimeouts,
       "rsaConnectionLapfRejectFramesRx": rsaConnectionLapfRejectFramesRx,
       "rsaConnectionLapfIFramesTx": rsaConnectionLapfIFramesTx,
       "rsaConnectionLapfIFramesTxDiscarded": rsaConnectionLapfIFramesTxDiscarded,
       "rsaConnectionLapfIFramesRx": rsaConnectionLapfIFramesRx,
       "rsaConnectionLapfIFramesRxDiscarded": rsaConnectionLapfIFramesRxDiscarded,
       "rsaOptionsTable": rsaOptionsTable,
       "rsaOptionsEntry": rsaOptionsEntry,
       "rsaLogicalProcessor": rsaLogicalProcessor,
       "rsaStateTable": rsaStateTable,
       "rsaStateEntry": rsaStateEntry,
       "rsaAdminState": rsaAdminState,
       "rsaOperationalState": rsaOperationalState,
       "rsaUsageState": rsaUsageState,
       "rsaOperationalTable": rsaOperationalTable,
       "rsaOperationalEntry": rsaOperationalEntry,
       "rsaMaxRsiConnections": rsaMaxRsiConnections,
       "rsaRsiConnections": rsaRsiConnections,
       "serverAccessRsaMIB": serverAccessRsaMIB,
       "serverAccessRsaGroup": serverAccessRsaGroup,
       "serverAccessRsaGroupBE": serverAccessRsaGroupBE,
       "serverAccessRsaGroupBE01": serverAccessRsaGroupBE01,
       "serverAccessRsaGroupBE01A": serverAccessRsaGroupBE01A,
       "serverAccessRsaCapabilities": serverAccessRsaCapabilities,
       "serverAccessRsaCapabilitiesBE": serverAccessRsaCapabilitiesBE,
       "serverAccessRsaCapabilitiesBE01": serverAccessRsaCapabilitiesBE01,
       "serverAccessRsaCapabilitiesBE01A": serverAccessRsaCapabilitiesBE01A}
)
