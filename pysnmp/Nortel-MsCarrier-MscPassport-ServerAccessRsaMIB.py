# SNMP MIB module (Nortel-MsCarrier-MscPassport-ServerAccessRsaMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-MsCarrier-MscPassport-ServerAccessRsaMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:33:00 2024
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
    "Nortel-MsCarrier-MscPassport-StandardTextualConventionsMIB",
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
    "Nortel-MsCarrier-MscPassport-TextualConventionsMIB",
    "AsciiString",
    "AsciiStringIndex",
    "DigitString",
    "EnterpriseDateAndTime",
    "Hex",
    "Link",
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

_MscRsa_ObjectIdentity = ObjectIdentity
mscRsa = _MscRsa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108)
)
_MscRsaRowStatusTable_Object = MibTable
mscRsaRowStatusTable = _MscRsaRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 1)
)
if mibBuilder.loadTexts:
    mscRsaRowStatusTable.setStatus("mandatory")
_MscRsaRowStatusEntry_Object = MibTableRow
mscRsaRowStatusEntry = _MscRsaRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 1, 1)
)
mscRsaRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-ServerAccessRsaMIB", "mscRsaIndex"),
)
if mibBuilder.loadTexts:
    mscRsaRowStatusEntry.setStatus("mandatory")
_MscRsaRowStatus_Type = RowStatus
_MscRsaRowStatus_Object = MibTableColumn
mscRsaRowStatus = _MscRsaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 1, 1, 1),
    _MscRsaRowStatus_Type()
)
mscRsaRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscRsaRowStatus.setStatus("mandatory")
_MscRsaComponentName_Type = DisplayString
_MscRsaComponentName_Object = MibTableColumn
mscRsaComponentName = _MscRsaComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 1, 1, 2),
    _MscRsaComponentName_Type()
)
mscRsaComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRsaComponentName.setStatus("mandatory")
_MscRsaStorageType_Type = StorageType
_MscRsaStorageType_Object = MibTableColumn
mscRsaStorageType = _MscRsaStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 1, 1, 4),
    _MscRsaStorageType_Type()
)
mscRsaStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRsaStorageType.setStatus("mandatory")


class _MscRsaIndex_Type(AsciiStringIndex):
    """Custom type mscRsaIndex based on AsciiStringIndex"""
    subtypeSpec = AsciiStringIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_MscRsaIndex_Type.__name__ = "AsciiStringIndex"
_MscRsaIndex_Object = MibTableColumn
mscRsaIndex = _MscRsaIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 1, 1, 10),
    _MscRsaIndex_Type()
)
mscRsaIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscRsaIndex.setStatus("mandatory")
_MscRsaDna_ObjectIdentity = ObjectIdentity
mscRsaDna = _MscRsaDna_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 2)
)
_MscRsaDnaRowStatusTable_Object = MibTable
mscRsaDnaRowStatusTable = _MscRsaDnaRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 2, 1)
)
if mibBuilder.loadTexts:
    mscRsaDnaRowStatusTable.setStatus("mandatory")
_MscRsaDnaRowStatusEntry_Object = MibTableRow
mscRsaDnaRowStatusEntry = _MscRsaDnaRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 2, 1, 1)
)
mscRsaDnaRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-ServerAccessRsaMIB", "mscRsaIndex"),
    (0, "Nortel-MsCarrier-MscPassport-ServerAccessRsaMIB", "mscRsaDnaIndex"),
)
if mibBuilder.loadTexts:
    mscRsaDnaRowStatusEntry.setStatus("mandatory")
_MscRsaDnaRowStatus_Type = RowStatus
_MscRsaDnaRowStatus_Object = MibTableColumn
mscRsaDnaRowStatus = _MscRsaDnaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 2, 1, 1, 1),
    _MscRsaDnaRowStatus_Type()
)
mscRsaDnaRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRsaDnaRowStatus.setStatus("mandatory")
_MscRsaDnaComponentName_Type = DisplayString
_MscRsaDnaComponentName_Object = MibTableColumn
mscRsaDnaComponentName = _MscRsaDnaComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 2, 1, 1, 2),
    _MscRsaDnaComponentName_Type()
)
mscRsaDnaComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRsaDnaComponentName.setStatus("mandatory")
_MscRsaDnaStorageType_Type = StorageType
_MscRsaDnaStorageType_Object = MibTableColumn
mscRsaDnaStorageType = _MscRsaDnaStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 2, 1, 1, 4),
    _MscRsaDnaStorageType_Type()
)
mscRsaDnaStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRsaDnaStorageType.setStatus("mandatory")
_MscRsaDnaIndex_Type = NonReplicated
_MscRsaDnaIndex_Object = MibTableColumn
mscRsaDnaIndex = _MscRsaDnaIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 2, 1, 1, 10),
    _MscRsaDnaIndex_Type()
)
mscRsaDnaIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscRsaDnaIndex.setStatus("mandatory")
_MscRsaDnaCug_ObjectIdentity = ObjectIdentity
mscRsaDnaCug = _MscRsaDnaCug_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 2, 2)
)
_MscRsaDnaCugRowStatusTable_Object = MibTable
mscRsaDnaCugRowStatusTable = _MscRsaDnaCugRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 2, 2, 1)
)
if mibBuilder.loadTexts:
    mscRsaDnaCugRowStatusTable.setStatus("mandatory")
_MscRsaDnaCugRowStatusEntry_Object = MibTableRow
mscRsaDnaCugRowStatusEntry = _MscRsaDnaCugRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 2, 2, 1, 1)
)
mscRsaDnaCugRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-ServerAccessRsaMIB", "mscRsaIndex"),
    (0, "Nortel-MsCarrier-MscPassport-ServerAccessRsaMIB", "mscRsaDnaIndex"),
    (0, "Nortel-MsCarrier-MscPassport-ServerAccessRsaMIB", "mscRsaDnaCugIndex"),
)
if mibBuilder.loadTexts:
    mscRsaDnaCugRowStatusEntry.setStatus("mandatory")
_MscRsaDnaCugRowStatus_Type = RowStatus
_MscRsaDnaCugRowStatus_Object = MibTableColumn
mscRsaDnaCugRowStatus = _MscRsaDnaCugRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 2, 2, 1, 1, 1),
    _MscRsaDnaCugRowStatus_Type()
)
mscRsaDnaCugRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscRsaDnaCugRowStatus.setStatus("mandatory")
_MscRsaDnaCugComponentName_Type = DisplayString
_MscRsaDnaCugComponentName_Object = MibTableColumn
mscRsaDnaCugComponentName = _MscRsaDnaCugComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 2, 2, 1, 1, 2),
    _MscRsaDnaCugComponentName_Type()
)
mscRsaDnaCugComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRsaDnaCugComponentName.setStatus("mandatory")
_MscRsaDnaCugStorageType_Type = StorageType
_MscRsaDnaCugStorageType_Object = MibTableColumn
mscRsaDnaCugStorageType = _MscRsaDnaCugStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 2, 2, 1, 1, 4),
    _MscRsaDnaCugStorageType_Type()
)
mscRsaDnaCugStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRsaDnaCugStorageType.setStatus("mandatory")


class _MscRsaDnaCugIndex_Type(Integer32):
    """Custom type mscRsaDnaCugIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscRsaDnaCugIndex_Type.__name__ = "Integer32"
_MscRsaDnaCugIndex_Object = MibTableColumn
mscRsaDnaCugIndex = _MscRsaDnaCugIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 2, 2, 1, 1, 10),
    _MscRsaDnaCugIndex_Type()
)
mscRsaDnaCugIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscRsaDnaCugIndex.setStatus("mandatory")
_MscRsaDnaCugCugOptionsTable_Object = MibTable
mscRsaDnaCugCugOptionsTable = _MscRsaDnaCugCugOptionsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 2, 2, 10)
)
if mibBuilder.loadTexts:
    mscRsaDnaCugCugOptionsTable.setStatus("mandatory")
_MscRsaDnaCugCugOptionsEntry_Object = MibTableRow
mscRsaDnaCugCugOptionsEntry = _MscRsaDnaCugCugOptionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 2, 2, 10, 1)
)
mscRsaDnaCugCugOptionsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-ServerAccessRsaMIB", "mscRsaIndex"),
    (0, "Nortel-MsCarrier-MscPassport-ServerAccessRsaMIB", "mscRsaDnaIndex"),
    (0, "Nortel-MsCarrier-MscPassport-ServerAccessRsaMIB", "mscRsaDnaCugIndex"),
)
if mibBuilder.loadTexts:
    mscRsaDnaCugCugOptionsEntry.setStatus("mandatory")


class _MscRsaDnaCugType_Type(Integer32):
    """Custom type mscRsaDnaCugType based on Integer32"""
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


_MscRsaDnaCugType_Type.__name__ = "Integer32"
_MscRsaDnaCugType_Object = MibTableColumn
mscRsaDnaCugType = _MscRsaDnaCugType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 2, 2, 10, 1, 1),
    _MscRsaDnaCugType_Type()
)
mscRsaDnaCugType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscRsaDnaCugType.setStatus("mandatory")


class _MscRsaDnaCugDnic_Type(DigitString):
    """Custom type mscRsaDnaCugDnic based on DigitString"""
    defaultHexValue = "30303030"

    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_MscRsaDnaCugDnic_Type.__name__ = "DigitString"
_MscRsaDnaCugDnic_Object = MibTableColumn
mscRsaDnaCugDnic = _MscRsaDnaCugDnic_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 2, 2, 10, 1, 2),
    _MscRsaDnaCugDnic_Type()
)
mscRsaDnaCugDnic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscRsaDnaCugDnic.setStatus("mandatory")


class _MscRsaDnaCugInterlockCode_Type(Unsigned32):
    """Custom type mscRsaDnaCugInterlockCode based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscRsaDnaCugInterlockCode_Type.__name__ = "Unsigned32"
_MscRsaDnaCugInterlockCode_Object = MibTableColumn
mscRsaDnaCugInterlockCode = _MscRsaDnaCugInterlockCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 2, 2, 10, 1, 3),
    _MscRsaDnaCugInterlockCode_Type()
)
mscRsaDnaCugInterlockCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscRsaDnaCugInterlockCode.setStatus("mandatory")


class _MscRsaDnaCugPreferential_Type(Integer32):
    """Custom type mscRsaDnaCugPreferential based on Integer32"""
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


_MscRsaDnaCugPreferential_Type.__name__ = "Integer32"
_MscRsaDnaCugPreferential_Object = MibTableColumn
mscRsaDnaCugPreferential = _MscRsaDnaCugPreferential_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 2, 2, 10, 1, 4),
    _MscRsaDnaCugPreferential_Type()
)
mscRsaDnaCugPreferential.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRsaDnaCugPreferential.setStatus("mandatory")


class _MscRsaDnaCugOutCalls_Type(Integer32):
    """Custom type mscRsaDnaCugOutCalls based on Integer32"""
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


_MscRsaDnaCugOutCalls_Type.__name__ = "Integer32"
_MscRsaDnaCugOutCalls_Object = MibTableColumn
mscRsaDnaCugOutCalls = _MscRsaDnaCugOutCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 2, 2, 10, 1, 5),
    _MscRsaDnaCugOutCalls_Type()
)
mscRsaDnaCugOutCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRsaDnaCugOutCalls.setStatus("mandatory")


class _MscRsaDnaCugIncCalls_Type(Integer32):
    """Custom type mscRsaDnaCugIncCalls based on Integer32"""
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


_MscRsaDnaCugIncCalls_Type.__name__ = "Integer32"
_MscRsaDnaCugIncCalls_Object = MibTableColumn
mscRsaDnaCugIncCalls = _MscRsaDnaCugIncCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 2, 2, 10, 1, 6),
    _MscRsaDnaCugIncCalls_Type()
)
mscRsaDnaCugIncCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRsaDnaCugIncCalls.setStatus("mandatory")


class _MscRsaDnaCugPrivileged_Type(Integer32):
    """Custom type mscRsaDnaCugPrivileged based on Integer32"""
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


_MscRsaDnaCugPrivileged_Type.__name__ = "Integer32"
_MscRsaDnaCugPrivileged_Object = MibTableColumn
mscRsaDnaCugPrivileged = _MscRsaDnaCugPrivileged_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 2, 2, 10, 1, 7),
    _MscRsaDnaCugPrivileged_Type()
)
mscRsaDnaCugPrivileged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRsaDnaCugPrivileged.setStatus("mandatory")
_MscRsaDnaAddressTable_Object = MibTable
mscRsaDnaAddressTable = _MscRsaDnaAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 2, 10)
)
if mibBuilder.loadTexts:
    mscRsaDnaAddressTable.setStatus("mandatory")
_MscRsaDnaAddressEntry_Object = MibTableRow
mscRsaDnaAddressEntry = _MscRsaDnaAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 2, 10, 1)
)
mscRsaDnaAddressEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-ServerAccessRsaMIB", "mscRsaIndex"),
    (0, "Nortel-MsCarrier-MscPassport-ServerAccessRsaMIB", "mscRsaDnaIndex"),
)
if mibBuilder.loadTexts:
    mscRsaDnaAddressEntry.setStatus("mandatory")


class _MscRsaDnaNumberingPlanIndicator_Type(Integer32):
    """Custom type mscRsaDnaNumberingPlanIndicator based on Integer32"""
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


_MscRsaDnaNumberingPlanIndicator_Type.__name__ = "Integer32"
_MscRsaDnaNumberingPlanIndicator_Object = MibTableColumn
mscRsaDnaNumberingPlanIndicator = _MscRsaDnaNumberingPlanIndicator_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 2, 10, 1, 1),
    _MscRsaDnaNumberingPlanIndicator_Type()
)
mscRsaDnaNumberingPlanIndicator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscRsaDnaNumberingPlanIndicator.setStatus("mandatory")


class _MscRsaDnaDataNetworkAddress_Type(DigitString):
    """Custom type mscRsaDnaDataNetworkAddress based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_MscRsaDnaDataNetworkAddress_Type.__name__ = "DigitString"
_MscRsaDnaDataNetworkAddress_Object = MibTableColumn
mscRsaDnaDataNetworkAddress = _MscRsaDnaDataNetworkAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 2, 10, 1, 2),
    _MscRsaDnaDataNetworkAddress_Type()
)
mscRsaDnaDataNetworkAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscRsaDnaDataNetworkAddress.setStatus("mandatory")
_MscRsaDnaOutgoingOptionsTable_Object = MibTable
mscRsaDnaOutgoingOptionsTable = _MscRsaDnaOutgoingOptionsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 2, 11)
)
if mibBuilder.loadTexts:
    mscRsaDnaOutgoingOptionsTable.setStatus("mandatory")
_MscRsaDnaOutgoingOptionsEntry_Object = MibTableRow
mscRsaDnaOutgoingOptionsEntry = _MscRsaDnaOutgoingOptionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 2, 11, 1)
)
mscRsaDnaOutgoingOptionsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-ServerAccessRsaMIB", "mscRsaIndex"),
    (0, "Nortel-MsCarrier-MscPassport-ServerAccessRsaMIB", "mscRsaDnaIndex"),
)
if mibBuilder.loadTexts:
    mscRsaDnaOutgoingOptionsEntry.setStatus("mandatory")


class _MscRsaDnaOutCalls_Type(Integer32):
    """Custom type mscRsaDnaOutCalls based on Integer32"""
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


_MscRsaDnaOutCalls_Type.__name__ = "Integer32"
_MscRsaDnaOutCalls_Object = MibTableColumn
mscRsaDnaOutCalls = _MscRsaDnaOutCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 2, 11, 1, 1),
    _MscRsaDnaOutCalls_Type()
)
mscRsaDnaOutCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRsaDnaOutCalls.setStatus("mandatory")
_MscRsaDnaIncomingOptionsTable_Object = MibTable
mscRsaDnaIncomingOptionsTable = _MscRsaDnaIncomingOptionsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 2, 12)
)
if mibBuilder.loadTexts:
    mscRsaDnaIncomingOptionsTable.setStatus("mandatory")
_MscRsaDnaIncomingOptionsEntry_Object = MibTableRow
mscRsaDnaIncomingOptionsEntry = _MscRsaDnaIncomingOptionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 2, 12, 1)
)
mscRsaDnaIncomingOptionsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-ServerAccessRsaMIB", "mscRsaIndex"),
    (0, "Nortel-MsCarrier-MscPassport-ServerAccessRsaMIB", "mscRsaDnaIndex"),
)
if mibBuilder.loadTexts:
    mscRsaDnaIncomingOptionsEntry.setStatus("mandatory")


class _MscRsaDnaIncCalls_Type(Integer32):
    """Custom type mscRsaDnaIncCalls based on Integer32"""
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


_MscRsaDnaIncCalls_Type.__name__ = "Integer32"
_MscRsaDnaIncCalls_Object = MibTableColumn
mscRsaDnaIncCalls = _MscRsaDnaIncCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 2, 12, 1, 1),
    _MscRsaDnaIncCalls_Type()
)
mscRsaDnaIncCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRsaDnaIncCalls.setStatus("mandatory")


class _MscRsaDnaIncAccess_Type(Integer32):
    """Custom type mscRsaDnaIncAccess based on Integer32"""
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


_MscRsaDnaIncAccess_Type.__name__ = "Integer32"
_MscRsaDnaIncAccess_Object = MibTableColumn
mscRsaDnaIncAccess = _MscRsaDnaIncAccess_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 2, 12, 1, 9),
    _MscRsaDnaIncAccess_Type()
)
mscRsaDnaIncAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscRsaDnaIncAccess.setStatus("mandatory")
_MscRsaVncsAccess_ObjectIdentity = ObjectIdentity
mscRsaVncsAccess = _MscRsaVncsAccess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 3)
)
_MscRsaVncsAccessRowStatusTable_Object = MibTable
mscRsaVncsAccessRowStatusTable = _MscRsaVncsAccessRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 3, 1)
)
if mibBuilder.loadTexts:
    mscRsaVncsAccessRowStatusTable.setStatus("mandatory")
_MscRsaVncsAccessRowStatusEntry_Object = MibTableRow
mscRsaVncsAccessRowStatusEntry = _MscRsaVncsAccessRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 3, 1, 1)
)
mscRsaVncsAccessRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-ServerAccessRsaMIB", "mscRsaIndex"),
    (0, "Nortel-MsCarrier-MscPassport-ServerAccessRsaMIB", "mscRsaVncsAccessIndex"),
)
if mibBuilder.loadTexts:
    mscRsaVncsAccessRowStatusEntry.setStatus("mandatory")
_MscRsaVncsAccessRowStatus_Type = RowStatus
_MscRsaVncsAccessRowStatus_Object = MibTableColumn
mscRsaVncsAccessRowStatus = _MscRsaVncsAccessRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 3, 1, 1, 1),
    _MscRsaVncsAccessRowStatus_Type()
)
mscRsaVncsAccessRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscRsaVncsAccessRowStatus.setStatus("mandatory")
_MscRsaVncsAccessComponentName_Type = DisplayString
_MscRsaVncsAccessComponentName_Object = MibTableColumn
mscRsaVncsAccessComponentName = _MscRsaVncsAccessComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 3, 1, 1, 2),
    _MscRsaVncsAccessComponentName_Type()
)
mscRsaVncsAccessComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRsaVncsAccessComponentName.setStatus("mandatory")
_MscRsaVncsAccessStorageType_Type = StorageType
_MscRsaVncsAccessStorageType_Object = MibTableColumn
mscRsaVncsAccessStorageType = _MscRsaVncsAccessStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 3, 1, 1, 4),
    _MscRsaVncsAccessStorageType_Type()
)
mscRsaVncsAccessStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRsaVncsAccessStorageType.setStatus("mandatory")
_MscRsaVncsAccessIndex_Type = NonReplicated
_MscRsaVncsAccessIndex_Object = MibTableColumn
mscRsaVncsAccessIndex = _MscRsaVncsAccessIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 3, 1, 1, 10),
    _MscRsaVncsAccessIndex_Type()
)
mscRsaVncsAccessIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscRsaVncsAccessIndex.setStatus("mandatory")
_MscRsaVncsAccessProvisionedTable_Object = MibTable
mscRsaVncsAccessProvisionedTable = _MscRsaVncsAccessProvisionedTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 3, 10)
)
if mibBuilder.loadTexts:
    mscRsaVncsAccessProvisionedTable.setStatus("mandatory")
_MscRsaVncsAccessProvisionedEntry_Object = MibTableRow
mscRsaVncsAccessProvisionedEntry = _MscRsaVncsAccessProvisionedEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 3, 10, 1)
)
mscRsaVncsAccessProvisionedEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-ServerAccessRsaMIB", "mscRsaIndex"),
    (0, "Nortel-MsCarrier-MscPassport-ServerAccessRsaMIB", "mscRsaVncsAccessIndex"),
)
if mibBuilder.loadTexts:
    mscRsaVncsAccessProvisionedEntry.setStatus("mandatory")


class _MscRsaVncsAccessTimeToLive_Type(Integer32):
    """Custom type mscRsaVncsAccessTimeToLive based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_MscRsaVncsAccessTimeToLive_Type.__name__ = "Integer32"
_MscRsaVncsAccessTimeToLive_Object = MibTableColumn
mscRsaVncsAccessTimeToLive = _MscRsaVncsAccessTimeToLive_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 3, 10, 1, 1),
    _MscRsaVncsAccessTimeToLive_Type()
)
mscRsaVncsAccessTimeToLive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscRsaVncsAccessTimeToLive.setStatus("mandatory")
_MscRsaVncsAccessStateTable_Object = MibTable
mscRsaVncsAccessStateTable = _MscRsaVncsAccessStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 3, 11)
)
if mibBuilder.loadTexts:
    mscRsaVncsAccessStateTable.setStatus("mandatory")
_MscRsaVncsAccessStateEntry_Object = MibTableRow
mscRsaVncsAccessStateEntry = _MscRsaVncsAccessStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 3, 11, 1)
)
mscRsaVncsAccessStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-ServerAccessRsaMIB", "mscRsaIndex"),
    (0, "Nortel-MsCarrier-MscPassport-ServerAccessRsaMIB", "mscRsaVncsAccessIndex"),
)
if mibBuilder.loadTexts:
    mscRsaVncsAccessStateEntry.setStatus("mandatory")


class _MscRsaVncsAccessAdminState_Type(Integer32):
    """Custom type mscRsaVncsAccessAdminState based on Integer32"""
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


_MscRsaVncsAccessAdminState_Type.__name__ = "Integer32"
_MscRsaVncsAccessAdminState_Object = MibTableColumn
mscRsaVncsAccessAdminState = _MscRsaVncsAccessAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 3, 11, 1, 1),
    _MscRsaVncsAccessAdminState_Type()
)
mscRsaVncsAccessAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRsaVncsAccessAdminState.setStatus("mandatory")


class _MscRsaVncsAccessOperationalState_Type(Integer32):
    """Custom type mscRsaVncsAccessOperationalState based on Integer32"""
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


_MscRsaVncsAccessOperationalState_Type.__name__ = "Integer32"
_MscRsaVncsAccessOperationalState_Object = MibTableColumn
mscRsaVncsAccessOperationalState = _MscRsaVncsAccessOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 3, 11, 1, 2),
    _MscRsaVncsAccessOperationalState_Type()
)
mscRsaVncsAccessOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRsaVncsAccessOperationalState.setStatus("mandatory")


class _MscRsaVncsAccessUsageState_Type(Integer32):
    """Custom type mscRsaVncsAccessUsageState based on Integer32"""
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


_MscRsaVncsAccessUsageState_Type.__name__ = "Integer32"
_MscRsaVncsAccessUsageState_Object = MibTableColumn
mscRsaVncsAccessUsageState = _MscRsaVncsAccessUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 3, 11, 1, 3),
    _MscRsaVncsAccessUsageState_Type()
)
mscRsaVncsAccessUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRsaVncsAccessUsageState.setStatus("mandatory")
_MscRsaVncsAccessOperationalTable_Object = MibTable
mscRsaVncsAccessOperationalTable = _MscRsaVncsAccessOperationalTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 3, 12)
)
if mibBuilder.loadTexts:
    mscRsaVncsAccessOperationalTable.setStatus("mandatory")
_MscRsaVncsAccessOperationalEntry_Object = MibTableRow
mscRsaVncsAccessOperationalEntry = _MscRsaVncsAccessOperationalEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 3, 12, 1)
)
mscRsaVncsAccessOperationalEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-ServerAccessRsaMIB", "mscRsaIndex"),
    (0, "Nortel-MsCarrier-MscPassport-ServerAccessRsaMIB", "mscRsaVncsAccessIndex"),
)
if mibBuilder.loadTexts:
    mscRsaVncsAccessOperationalEntry.setStatus("mandatory")
_MscRsaVncsAccessRequestsSent_Type = Counter32
_MscRsaVncsAccessRequestsSent_Object = MibTableColumn
mscRsaVncsAccessRequestsSent = _MscRsaVncsAccessRequestsSent_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 3, 12, 1, 1),
    _MscRsaVncsAccessRequestsSent_Type()
)
mscRsaVncsAccessRequestsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRsaVncsAccessRequestsSent.setStatus("mandatory")
_MscRsaVncsAccessRepliesReceived_Type = Counter32
_MscRsaVncsAccessRepliesReceived_Object = MibTableColumn
mscRsaVncsAccessRepliesReceived = _MscRsaVncsAccessRepliesReceived_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 3, 12, 1, 2),
    _MscRsaVncsAccessRepliesReceived_Type()
)
mscRsaVncsAccessRepliesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRsaVncsAccessRepliesReceived.setStatus("mandatory")


class _MscRsaVncsAccessRequestsQueued_Type(Integer32):
    """Custom type mscRsaVncsAccessRequestsQueued based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscRsaVncsAccessRequestsQueued_Type.__name__ = "Integer32"
_MscRsaVncsAccessRequestsQueued_Object = MibTableColumn
mscRsaVncsAccessRequestsQueued = _MscRsaVncsAccessRequestsQueued_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 3, 12, 1, 3),
    _MscRsaVncsAccessRequestsQueued_Type()
)
mscRsaVncsAccessRequestsQueued.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRsaVncsAccessRequestsQueued.setStatus("mandatory")
_MscRsaVncsAccessRequestsDiscarded_Type = Counter32
_MscRsaVncsAccessRequestsDiscarded_Object = MibTableColumn
mscRsaVncsAccessRequestsDiscarded = _MscRsaVncsAccessRequestsDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 3, 12, 1, 4),
    _MscRsaVncsAccessRequestsDiscarded_Type()
)
mscRsaVncsAccessRequestsDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRsaVncsAccessRequestsDiscarded.setStatus("mandatory")
_MscRsaConnection_ObjectIdentity = ObjectIdentity
mscRsaConnection = _MscRsaConnection_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 4)
)
_MscRsaConnectionRowStatusTable_Object = MibTable
mscRsaConnectionRowStatusTable = _MscRsaConnectionRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 4, 1)
)
if mibBuilder.loadTexts:
    mscRsaConnectionRowStatusTable.setStatus("mandatory")
_MscRsaConnectionRowStatusEntry_Object = MibTableRow
mscRsaConnectionRowStatusEntry = _MscRsaConnectionRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 4, 1, 1)
)
mscRsaConnectionRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-ServerAccessRsaMIB", "mscRsaIndex"),
    (0, "Nortel-MsCarrier-MscPassport-ServerAccessRsaMIB", "mscRsaConnectionIndex"),
)
if mibBuilder.loadTexts:
    mscRsaConnectionRowStatusEntry.setStatus("mandatory")
_MscRsaConnectionRowStatus_Type = RowStatus
_MscRsaConnectionRowStatus_Object = MibTableColumn
mscRsaConnectionRowStatus = _MscRsaConnectionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 4, 1, 1, 1),
    _MscRsaConnectionRowStatus_Type()
)
mscRsaConnectionRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRsaConnectionRowStatus.setStatus("mandatory")
_MscRsaConnectionComponentName_Type = DisplayString
_MscRsaConnectionComponentName_Object = MibTableColumn
mscRsaConnectionComponentName = _MscRsaConnectionComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 4, 1, 1, 2),
    _MscRsaConnectionComponentName_Type()
)
mscRsaConnectionComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRsaConnectionComponentName.setStatus("mandatory")
_MscRsaConnectionStorageType_Type = StorageType
_MscRsaConnectionStorageType_Object = MibTableColumn
mscRsaConnectionStorageType = _MscRsaConnectionStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 4, 1, 1, 4),
    _MscRsaConnectionStorageType_Type()
)
mscRsaConnectionStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRsaConnectionStorageType.setStatus("mandatory")


class _MscRsaConnectionIndex_Type(Integer32):
    """Custom type mscRsaConnectionIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_MscRsaConnectionIndex_Type.__name__ = "Integer32"
_MscRsaConnectionIndex_Object = MibTableColumn
mscRsaConnectionIndex = _MscRsaConnectionIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 4, 1, 1, 10),
    _MscRsaConnectionIndex_Type()
)
mscRsaConnectionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscRsaConnectionIndex.setStatus("mandatory")
_MscRsaConnectionVc_ObjectIdentity = ObjectIdentity
mscRsaConnectionVc = _MscRsaConnectionVc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 4, 2)
)
_MscRsaConnectionVcRowStatusTable_Object = MibTable
mscRsaConnectionVcRowStatusTable = _MscRsaConnectionVcRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 4, 2, 1)
)
if mibBuilder.loadTexts:
    mscRsaConnectionVcRowStatusTable.setStatus("mandatory")
_MscRsaConnectionVcRowStatusEntry_Object = MibTableRow
mscRsaConnectionVcRowStatusEntry = _MscRsaConnectionVcRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 4, 2, 1, 1)
)
mscRsaConnectionVcRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-ServerAccessRsaMIB", "mscRsaIndex"),
    (0, "Nortel-MsCarrier-MscPassport-ServerAccessRsaMIB", "mscRsaConnectionIndex"),
    (0, "Nortel-MsCarrier-MscPassport-ServerAccessRsaMIB", "mscRsaConnectionVcIndex"),
)
if mibBuilder.loadTexts:
    mscRsaConnectionVcRowStatusEntry.setStatus("mandatory")
_MscRsaConnectionVcRowStatus_Type = RowStatus
_MscRsaConnectionVcRowStatus_Object = MibTableColumn
mscRsaConnectionVcRowStatus = _MscRsaConnectionVcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 4, 2, 1, 1, 1),
    _MscRsaConnectionVcRowStatus_Type()
)
mscRsaConnectionVcRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRsaConnectionVcRowStatus.setStatus("mandatory")
_MscRsaConnectionVcComponentName_Type = DisplayString
_MscRsaConnectionVcComponentName_Object = MibTableColumn
mscRsaConnectionVcComponentName = _MscRsaConnectionVcComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 4, 2, 1, 1, 2),
    _MscRsaConnectionVcComponentName_Type()
)
mscRsaConnectionVcComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRsaConnectionVcComponentName.setStatus("mandatory")
_MscRsaConnectionVcStorageType_Type = StorageType
_MscRsaConnectionVcStorageType_Object = MibTableColumn
mscRsaConnectionVcStorageType = _MscRsaConnectionVcStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 4, 2, 1, 1, 4),
    _MscRsaConnectionVcStorageType_Type()
)
mscRsaConnectionVcStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRsaConnectionVcStorageType.setStatus("mandatory")
_MscRsaConnectionVcIndex_Type = NonReplicated
_MscRsaConnectionVcIndex_Object = MibTableColumn
mscRsaConnectionVcIndex = _MscRsaConnectionVcIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 4, 2, 1, 1, 10),
    _MscRsaConnectionVcIndex_Type()
)
mscRsaConnectionVcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscRsaConnectionVcIndex.setStatus("mandatory")
_MscRsaConnectionVcCadTable_Object = MibTable
mscRsaConnectionVcCadTable = _MscRsaConnectionVcCadTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 4, 2, 10)
)
if mibBuilder.loadTexts:
    mscRsaConnectionVcCadTable.setStatus("mandatory")
_MscRsaConnectionVcCadEntry_Object = MibTableRow
mscRsaConnectionVcCadEntry = _MscRsaConnectionVcCadEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 4, 2, 10, 1)
)
mscRsaConnectionVcCadEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-ServerAccessRsaMIB", "mscRsaIndex"),
    (0, "Nortel-MsCarrier-MscPassport-ServerAccessRsaMIB", "mscRsaConnectionIndex"),
    (0, "Nortel-MsCarrier-MscPassport-ServerAccessRsaMIB", "mscRsaConnectionVcIndex"),
)
if mibBuilder.loadTexts:
    mscRsaConnectionVcCadEntry.setStatus("mandatory")


class _MscRsaConnectionVcType_Type(Integer32):
    """Custom type mscRsaConnectionVcType based on Integer32"""
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


_MscRsaConnectionVcType_Type.__name__ = "Integer32"
_MscRsaConnectionVcType_Object = MibTableColumn
mscRsaConnectionVcType = _MscRsaConnectionVcType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 4, 2, 10, 1, 1),
    _MscRsaConnectionVcType_Type()
)
mscRsaConnectionVcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRsaConnectionVcType.setStatus("mandatory")


class _MscRsaConnectionVcState_Type(Integer32):
    """Custom type mscRsaConnectionVcState based on Integer32"""
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


_MscRsaConnectionVcState_Type.__name__ = "Integer32"
_MscRsaConnectionVcState_Object = MibTableColumn
mscRsaConnectionVcState = _MscRsaConnectionVcState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 4, 2, 10, 1, 2),
    _MscRsaConnectionVcState_Type()
)
mscRsaConnectionVcState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRsaConnectionVcState.setStatus("mandatory")


class _MscRsaConnectionVcPreviousState_Type(Integer32):
    """Custom type mscRsaConnectionVcPreviousState based on Integer32"""
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


_MscRsaConnectionVcPreviousState_Type.__name__ = "Integer32"
_MscRsaConnectionVcPreviousState_Object = MibTableColumn
mscRsaConnectionVcPreviousState = _MscRsaConnectionVcPreviousState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 4, 2, 10, 1, 3),
    _MscRsaConnectionVcPreviousState_Type()
)
mscRsaConnectionVcPreviousState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRsaConnectionVcPreviousState.setStatus("mandatory")


class _MscRsaConnectionVcDiagnosticCode_Type(Unsigned32):
    """Custom type mscRsaConnectionVcDiagnosticCode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscRsaConnectionVcDiagnosticCode_Type.__name__ = "Unsigned32"
_MscRsaConnectionVcDiagnosticCode_Object = MibTableColumn
mscRsaConnectionVcDiagnosticCode = _MscRsaConnectionVcDiagnosticCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 4, 2, 10, 1, 4),
    _MscRsaConnectionVcDiagnosticCode_Type()
)
mscRsaConnectionVcDiagnosticCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRsaConnectionVcDiagnosticCode.setStatus("mandatory")


class _MscRsaConnectionVcPreviousDiagnosticCode_Type(Unsigned32):
    """Custom type mscRsaConnectionVcPreviousDiagnosticCode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscRsaConnectionVcPreviousDiagnosticCode_Type.__name__ = "Unsigned32"
_MscRsaConnectionVcPreviousDiagnosticCode_Object = MibTableColumn
mscRsaConnectionVcPreviousDiagnosticCode = _MscRsaConnectionVcPreviousDiagnosticCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 4, 2, 10, 1, 5),
    _MscRsaConnectionVcPreviousDiagnosticCode_Type()
)
mscRsaConnectionVcPreviousDiagnosticCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRsaConnectionVcPreviousDiagnosticCode.setStatus("mandatory")


class _MscRsaConnectionVcCalledNpi_Type(Integer32):
    """Custom type mscRsaConnectionVcCalledNpi based on Integer32"""
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


_MscRsaConnectionVcCalledNpi_Type.__name__ = "Integer32"
_MscRsaConnectionVcCalledNpi_Object = MibTableColumn
mscRsaConnectionVcCalledNpi = _MscRsaConnectionVcCalledNpi_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 4, 2, 10, 1, 6),
    _MscRsaConnectionVcCalledNpi_Type()
)
mscRsaConnectionVcCalledNpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRsaConnectionVcCalledNpi.setStatus("mandatory")


class _MscRsaConnectionVcCalledDna_Type(DigitString):
    """Custom type mscRsaConnectionVcCalledDna based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_MscRsaConnectionVcCalledDna_Type.__name__ = "DigitString"
_MscRsaConnectionVcCalledDna_Object = MibTableColumn
mscRsaConnectionVcCalledDna = _MscRsaConnectionVcCalledDna_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 4, 2, 10, 1, 7),
    _MscRsaConnectionVcCalledDna_Type()
)
mscRsaConnectionVcCalledDna.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRsaConnectionVcCalledDna.setStatus("mandatory")


class _MscRsaConnectionVcCalledLcn_Type(Unsigned32):
    """Custom type mscRsaConnectionVcCalledLcn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MscRsaConnectionVcCalledLcn_Type.__name__ = "Unsigned32"
_MscRsaConnectionVcCalledLcn_Object = MibTableColumn
mscRsaConnectionVcCalledLcn = _MscRsaConnectionVcCalledLcn_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 4, 2, 10, 1, 8),
    _MscRsaConnectionVcCalledLcn_Type()
)
mscRsaConnectionVcCalledLcn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRsaConnectionVcCalledLcn.setStatus("mandatory")


class _MscRsaConnectionVcCallingNpi_Type(Integer32):
    """Custom type mscRsaConnectionVcCallingNpi based on Integer32"""
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


_MscRsaConnectionVcCallingNpi_Type.__name__ = "Integer32"
_MscRsaConnectionVcCallingNpi_Object = MibTableColumn
mscRsaConnectionVcCallingNpi = _MscRsaConnectionVcCallingNpi_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 4, 2, 10, 1, 9),
    _MscRsaConnectionVcCallingNpi_Type()
)
mscRsaConnectionVcCallingNpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRsaConnectionVcCallingNpi.setStatus("mandatory")


class _MscRsaConnectionVcCallingDna_Type(DigitString):
    """Custom type mscRsaConnectionVcCallingDna based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_MscRsaConnectionVcCallingDna_Type.__name__ = "DigitString"
_MscRsaConnectionVcCallingDna_Object = MibTableColumn
mscRsaConnectionVcCallingDna = _MscRsaConnectionVcCallingDna_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 4, 2, 10, 1, 10),
    _MscRsaConnectionVcCallingDna_Type()
)
mscRsaConnectionVcCallingDna.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRsaConnectionVcCallingDna.setStatus("mandatory")


class _MscRsaConnectionVcCallingLcn_Type(Unsigned32):
    """Custom type mscRsaConnectionVcCallingLcn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MscRsaConnectionVcCallingLcn_Type.__name__ = "Unsigned32"
_MscRsaConnectionVcCallingLcn_Object = MibTableColumn
mscRsaConnectionVcCallingLcn = _MscRsaConnectionVcCallingLcn_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 4, 2, 10, 1, 11),
    _MscRsaConnectionVcCallingLcn_Type()
)
mscRsaConnectionVcCallingLcn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRsaConnectionVcCallingLcn.setStatus("mandatory")


class _MscRsaConnectionVcAccountingEnabled_Type(Integer32):
    """Custom type mscRsaConnectionVcAccountingEnabled based on Integer32"""
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


_MscRsaConnectionVcAccountingEnabled_Type.__name__ = "Integer32"
_MscRsaConnectionVcAccountingEnabled_Object = MibTableColumn
mscRsaConnectionVcAccountingEnabled = _MscRsaConnectionVcAccountingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 4, 2, 10, 1, 12),
    _MscRsaConnectionVcAccountingEnabled_Type()
)
mscRsaConnectionVcAccountingEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRsaConnectionVcAccountingEnabled.setStatus("mandatory")


class _MscRsaConnectionVcFastSelectCall_Type(Integer32):
    """Custom type mscRsaConnectionVcFastSelectCall based on Integer32"""
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


_MscRsaConnectionVcFastSelectCall_Type.__name__ = "Integer32"
_MscRsaConnectionVcFastSelectCall_Object = MibTableColumn
mscRsaConnectionVcFastSelectCall = _MscRsaConnectionVcFastSelectCall_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 4, 2, 10, 1, 13),
    _MscRsaConnectionVcFastSelectCall_Type()
)
mscRsaConnectionVcFastSelectCall.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRsaConnectionVcFastSelectCall.setStatus("mandatory")


class _MscRsaConnectionVcPathReliability_Type(Integer32):
    """Custom type mscRsaConnectionVcPathReliability based on Integer32"""
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


_MscRsaConnectionVcPathReliability_Type.__name__ = "Integer32"
_MscRsaConnectionVcPathReliability_Object = MibTableColumn
mscRsaConnectionVcPathReliability = _MscRsaConnectionVcPathReliability_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 4, 2, 10, 1, 19),
    _MscRsaConnectionVcPathReliability_Type()
)
mscRsaConnectionVcPathReliability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRsaConnectionVcPathReliability.setStatus("mandatory")


class _MscRsaConnectionVcAccountingEnd_Type(Integer32):
    """Custom type mscRsaConnectionVcAccountingEnd based on Integer32"""
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


_MscRsaConnectionVcAccountingEnd_Type.__name__ = "Integer32"
_MscRsaConnectionVcAccountingEnd_Object = MibTableColumn
mscRsaConnectionVcAccountingEnd = _MscRsaConnectionVcAccountingEnd_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 4, 2, 10, 1, 20),
    _MscRsaConnectionVcAccountingEnd_Type()
)
mscRsaConnectionVcAccountingEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRsaConnectionVcAccountingEnd.setStatus("mandatory")


class _MscRsaConnectionVcPriority_Type(Integer32):
    """Custom type mscRsaConnectionVcPriority based on Integer32"""
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


_MscRsaConnectionVcPriority_Type.__name__ = "Integer32"
_MscRsaConnectionVcPriority_Object = MibTableColumn
mscRsaConnectionVcPriority = _MscRsaConnectionVcPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 4, 2, 10, 1, 21),
    _MscRsaConnectionVcPriority_Type()
)
mscRsaConnectionVcPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRsaConnectionVcPriority.setStatus("mandatory")


class _MscRsaConnectionVcSegmentSize_Type(Unsigned32):
    """Custom type mscRsaConnectionVcSegmentSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_MscRsaConnectionVcSegmentSize_Type.__name__ = "Unsigned32"
_MscRsaConnectionVcSegmentSize_Object = MibTableColumn
mscRsaConnectionVcSegmentSize = _MscRsaConnectionVcSegmentSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 4, 2, 10, 1, 22),
    _MscRsaConnectionVcSegmentSize_Type()
)
mscRsaConnectionVcSegmentSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRsaConnectionVcSegmentSize.setStatus("mandatory")


class _MscRsaConnectionVcMaxSubnetPktSize_Type(Unsigned32):
    """Custom type mscRsaConnectionVcMaxSubnetPktSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_MscRsaConnectionVcMaxSubnetPktSize_Type.__name__ = "Unsigned32"
_MscRsaConnectionVcMaxSubnetPktSize_Object = MibTableColumn
mscRsaConnectionVcMaxSubnetPktSize = _MscRsaConnectionVcMaxSubnetPktSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 4, 2, 10, 1, 27),
    _MscRsaConnectionVcMaxSubnetPktSize_Type()
)
mscRsaConnectionVcMaxSubnetPktSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRsaConnectionVcMaxSubnetPktSize.setStatus("mandatory")


class _MscRsaConnectionVcRcosToNetwork_Type(Integer32):
    """Custom type mscRsaConnectionVcRcosToNetwork based on Integer32"""
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


_MscRsaConnectionVcRcosToNetwork_Type.__name__ = "Integer32"
_MscRsaConnectionVcRcosToNetwork_Object = MibTableColumn
mscRsaConnectionVcRcosToNetwork = _MscRsaConnectionVcRcosToNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 4, 2, 10, 1, 28),
    _MscRsaConnectionVcRcosToNetwork_Type()
)
mscRsaConnectionVcRcosToNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRsaConnectionVcRcosToNetwork.setStatus("mandatory")


class _MscRsaConnectionVcRcosFromNetwork_Type(Integer32):
    """Custom type mscRsaConnectionVcRcosFromNetwork based on Integer32"""
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


_MscRsaConnectionVcRcosFromNetwork_Type.__name__ = "Integer32"
_MscRsaConnectionVcRcosFromNetwork_Object = MibTableColumn
mscRsaConnectionVcRcosFromNetwork = _MscRsaConnectionVcRcosFromNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 4, 2, 10, 1, 29),
    _MscRsaConnectionVcRcosFromNetwork_Type()
)
mscRsaConnectionVcRcosFromNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRsaConnectionVcRcosFromNetwork.setStatus("mandatory")


class _MscRsaConnectionVcEmissionPriorityToNetwork_Type(Integer32):
    """Custom type mscRsaConnectionVcEmissionPriorityToNetwork based on Integer32"""
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


_MscRsaConnectionVcEmissionPriorityToNetwork_Type.__name__ = "Integer32"
_MscRsaConnectionVcEmissionPriorityToNetwork_Object = MibTableColumn
mscRsaConnectionVcEmissionPriorityToNetwork = _MscRsaConnectionVcEmissionPriorityToNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 4, 2, 10, 1, 30),
    _MscRsaConnectionVcEmissionPriorityToNetwork_Type()
)
mscRsaConnectionVcEmissionPriorityToNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRsaConnectionVcEmissionPriorityToNetwork.setStatus("mandatory")


class _MscRsaConnectionVcEmissionPriorityFromNetwork_Type(Integer32):
    """Custom type mscRsaConnectionVcEmissionPriorityFromNetwork based on Integer32"""
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


_MscRsaConnectionVcEmissionPriorityFromNetwork_Type.__name__ = "Integer32"
_MscRsaConnectionVcEmissionPriorityFromNetwork_Object = MibTableColumn
mscRsaConnectionVcEmissionPriorityFromNetwork = _MscRsaConnectionVcEmissionPriorityFromNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 4, 2, 10, 1, 31),
    _MscRsaConnectionVcEmissionPriorityFromNetwork_Type()
)
mscRsaConnectionVcEmissionPriorityFromNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRsaConnectionVcEmissionPriorityFromNetwork.setStatus("mandatory")


class _MscRsaConnectionVcDataPath_Type(AsciiString):
    """Custom type mscRsaConnectionVcDataPath based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MscRsaConnectionVcDataPath_Type.__name__ = "AsciiString"
_MscRsaConnectionVcDataPath_Object = MibTableColumn
mscRsaConnectionVcDataPath = _MscRsaConnectionVcDataPath_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 4, 2, 10, 1, 32),
    _MscRsaConnectionVcDataPath_Type()
)
mscRsaConnectionVcDataPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRsaConnectionVcDataPath.setStatus("mandatory")
_MscRsaConnectionVcIntdTable_Object = MibTable
mscRsaConnectionVcIntdTable = _MscRsaConnectionVcIntdTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 4, 2, 11)
)
if mibBuilder.loadTexts:
    mscRsaConnectionVcIntdTable.setStatus("mandatory")
_MscRsaConnectionVcIntdEntry_Object = MibTableRow
mscRsaConnectionVcIntdEntry = _MscRsaConnectionVcIntdEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 4, 2, 11, 1)
)
mscRsaConnectionVcIntdEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-ServerAccessRsaMIB", "mscRsaIndex"),
    (0, "Nortel-MsCarrier-MscPassport-ServerAccessRsaMIB", "mscRsaConnectionIndex"),
    (0, "Nortel-MsCarrier-MscPassport-ServerAccessRsaMIB", "mscRsaConnectionVcIndex"),
)
if mibBuilder.loadTexts:
    mscRsaConnectionVcIntdEntry.setStatus("mandatory")


class _MscRsaConnectionVcCallReferenceNumber_Type(Hex):
    """Custom type mscRsaConnectionVcCallReferenceNumber based on Hex"""
    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_MscRsaConnectionVcCallReferenceNumber_Type.__name__ = "Hex"
_MscRsaConnectionVcCallReferenceNumber_Object = MibTableColumn
mscRsaConnectionVcCallReferenceNumber = _MscRsaConnectionVcCallReferenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 4, 2, 11, 1, 1),
    _MscRsaConnectionVcCallReferenceNumber_Type()
)
mscRsaConnectionVcCallReferenceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRsaConnectionVcCallReferenceNumber.setStatus("obsolete")


class _MscRsaConnectionVcElapsedTimeTillNow_Type(Unsigned32):
    """Custom type mscRsaConnectionVcElapsedTimeTillNow based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_MscRsaConnectionVcElapsedTimeTillNow_Type.__name__ = "Unsigned32"
_MscRsaConnectionVcElapsedTimeTillNow_Object = MibTableColumn
mscRsaConnectionVcElapsedTimeTillNow = _MscRsaConnectionVcElapsedTimeTillNow_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 4, 2, 11, 1, 2),
    _MscRsaConnectionVcElapsedTimeTillNow_Type()
)
mscRsaConnectionVcElapsedTimeTillNow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRsaConnectionVcElapsedTimeTillNow.setStatus("mandatory")


class _MscRsaConnectionVcSegmentsRx_Type(Unsigned32):
    """Custom type mscRsaConnectionVcSegmentsRx based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_MscRsaConnectionVcSegmentsRx_Type.__name__ = "Unsigned32"
_MscRsaConnectionVcSegmentsRx_Object = MibTableColumn
mscRsaConnectionVcSegmentsRx = _MscRsaConnectionVcSegmentsRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 4, 2, 11, 1, 3),
    _MscRsaConnectionVcSegmentsRx_Type()
)
mscRsaConnectionVcSegmentsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRsaConnectionVcSegmentsRx.setStatus("mandatory")


class _MscRsaConnectionVcSegmentsSent_Type(Unsigned32):
    """Custom type mscRsaConnectionVcSegmentsSent based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_MscRsaConnectionVcSegmentsSent_Type.__name__ = "Unsigned32"
_MscRsaConnectionVcSegmentsSent_Object = MibTableColumn
mscRsaConnectionVcSegmentsSent = _MscRsaConnectionVcSegmentsSent_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 4, 2, 11, 1, 4),
    _MscRsaConnectionVcSegmentsSent_Type()
)
mscRsaConnectionVcSegmentsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRsaConnectionVcSegmentsSent.setStatus("mandatory")


class _MscRsaConnectionVcStartTime_Type(EnterpriseDateAndTime):
    """Custom type mscRsaConnectionVcStartTime based on EnterpriseDateAndTime"""
    subtypeSpec = EnterpriseDateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(19, 19),
    )


_MscRsaConnectionVcStartTime_Type.__name__ = "EnterpriseDateAndTime"
_MscRsaConnectionVcStartTime_Object = MibTableColumn
mscRsaConnectionVcStartTime = _MscRsaConnectionVcStartTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 4, 2, 11, 1, 5),
    _MscRsaConnectionVcStartTime_Type()
)
mscRsaConnectionVcStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRsaConnectionVcStartTime.setStatus("mandatory")


class _MscRsaConnectionVcCallReferenceNumberDecimal_Type(Unsigned32):
    """Custom type mscRsaConnectionVcCallReferenceNumberDecimal based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscRsaConnectionVcCallReferenceNumberDecimal_Type.__name__ = "Unsigned32"
_MscRsaConnectionVcCallReferenceNumberDecimal_Object = MibTableColumn
mscRsaConnectionVcCallReferenceNumberDecimal = _MscRsaConnectionVcCallReferenceNumberDecimal_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 4, 2, 11, 1, 7),
    _MscRsaConnectionVcCallReferenceNumberDecimal_Type()
)
mscRsaConnectionVcCallReferenceNumberDecimal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRsaConnectionVcCallReferenceNumberDecimal.setStatus("mandatory")
_MscRsaConnectionVcFrdTable_Object = MibTable
mscRsaConnectionVcFrdTable = _MscRsaConnectionVcFrdTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 4, 2, 12)
)
if mibBuilder.loadTexts:
    mscRsaConnectionVcFrdTable.setStatus("mandatory")
_MscRsaConnectionVcFrdEntry_Object = MibTableRow
mscRsaConnectionVcFrdEntry = _MscRsaConnectionVcFrdEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 4, 2, 12, 1)
)
mscRsaConnectionVcFrdEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-ServerAccessRsaMIB", "mscRsaIndex"),
    (0, "Nortel-MsCarrier-MscPassport-ServerAccessRsaMIB", "mscRsaConnectionIndex"),
    (0, "Nortel-MsCarrier-MscPassport-ServerAccessRsaMIB", "mscRsaConnectionVcIndex"),
)
if mibBuilder.loadTexts:
    mscRsaConnectionVcFrdEntry.setStatus("mandatory")


class _MscRsaConnectionVcFrmCongestedToSubnet_Type(Unsigned32):
    """Custom type mscRsaConnectionVcFrmCongestedToSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscRsaConnectionVcFrmCongestedToSubnet_Type.__name__ = "Unsigned32"
_MscRsaConnectionVcFrmCongestedToSubnet_Object = MibTableColumn
mscRsaConnectionVcFrmCongestedToSubnet = _MscRsaConnectionVcFrmCongestedToSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 4, 2, 12, 1, 2),
    _MscRsaConnectionVcFrmCongestedToSubnet_Type()
)
mscRsaConnectionVcFrmCongestedToSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRsaConnectionVcFrmCongestedToSubnet.setStatus("mandatory")


class _MscRsaConnectionVcCannotForwardToSubnet_Type(Unsigned32):
    """Custom type mscRsaConnectionVcCannotForwardToSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscRsaConnectionVcCannotForwardToSubnet_Type.__name__ = "Unsigned32"
_MscRsaConnectionVcCannotForwardToSubnet_Object = MibTableColumn
mscRsaConnectionVcCannotForwardToSubnet = _MscRsaConnectionVcCannotForwardToSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 4, 2, 12, 1, 3),
    _MscRsaConnectionVcCannotForwardToSubnet_Type()
)
mscRsaConnectionVcCannotForwardToSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRsaConnectionVcCannotForwardToSubnet.setStatus("mandatory")


class _MscRsaConnectionVcNotDataXferToSubnet_Type(Unsigned32):
    """Custom type mscRsaConnectionVcNotDataXferToSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscRsaConnectionVcNotDataXferToSubnet_Type.__name__ = "Unsigned32"
_MscRsaConnectionVcNotDataXferToSubnet_Object = MibTableColumn
mscRsaConnectionVcNotDataXferToSubnet = _MscRsaConnectionVcNotDataXferToSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 4, 2, 12, 1, 4),
    _MscRsaConnectionVcNotDataXferToSubnet_Type()
)
mscRsaConnectionVcNotDataXferToSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRsaConnectionVcNotDataXferToSubnet.setStatus("mandatory")


class _MscRsaConnectionVcOutOfRangeFrmFromSubnet_Type(Unsigned32):
    """Custom type mscRsaConnectionVcOutOfRangeFrmFromSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscRsaConnectionVcOutOfRangeFrmFromSubnet_Type.__name__ = "Unsigned32"
_MscRsaConnectionVcOutOfRangeFrmFromSubnet_Object = MibTableColumn
mscRsaConnectionVcOutOfRangeFrmFromSubnet = _MscRsaConnectionVcOutOfRangeFrmFromSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 4, 2, 12, 1, 5),
    _MscRsaConnectionVcOutOfRangeFrmFromSubnet_Type()
)
mscRsaConnectionVcOutOfRangeFrmFromSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRsaConnectionVcOutOfRangeFrmFromSubnet.setStatus("mandatory")


class _MscRsaConnectionVcCombErrorsFromSubnet_Type(Unsigned32):
    """Custom type mscRsaConnectionVcCombErrorsFromSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscRsaConnectionVcCombErrorsFromSubnet_Type.__name__ = "Unsigned32"
_MscRsaConnectionVcCombErrorsFromSubnet_Object = MibTableColumn
mscRsaConnectionVcCombErrorsFromSubnet = _MscRsaConnectionVcCombErrorsFromSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 4, 2, 12, 1, 6),
    _MscRsaConnectionVcCombErrorsFromSubnet_Type()
)
mscRsaConnectionVcCombErrorsFromSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRsaConnectionVcCombErrorsFromSubnet.setStatus("mandatory")


class _MscRsaConnectionVcDuplicatesFromSubnet_Type(Unsigned32):
    """Custom type mscRsaConnectionVcDuplicatesFromSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscRsaConnectionVcDuplicatesFromSubnet_Type.__name__ = "Unsigned32"
_MscRsaConnectionVcDuplicatesFromSubnet_Object = MibTableColumn
mscRsaConnectionVcDuplicatesFromSubnet = _MscRsaConnectionVcDuplicatesFromSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 4, 2, 12, 1, 7),
    _MscRsaConnectionVcDuplicatesFromSubnet_Type()
)
mscRsaConnectionVcDuplicatesFromSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRsaConnectionVcDuplicatesFromSubnet.setStatus("mandatory")


class _MscRsaConnectionVcNotDataXferFromSubnet_Type(Unsigned32):
    """Custom type mscRsaConnectionVcNotDataXferFromSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscRsaConnectionVcNotDataXferFromSubnet_Type.__name__ = "Unsigned32"
_MscRsaConnectionVcNotDataXferFromSubnet_Object = MibTableColumn
mscRsaConnectionVcNotDataXferFromSubnet = _MscRsaConnectionVcNotDataXferFromSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 4, 2, 12, 1, 8),
    _MscRsaConnectionVcNotDataXferFromSubnet_Type()
)
mscRsaConnectionVcNotDataXferFromSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRsaConnectionVcNotDataXferFromSubnet.setStatus("mandatory")


class _MscRsaConnectionVcFrmLossTimeouts_Type(Unsigned32):
    """Custom type mscRsaConnectionVcFrmLossTimeouts based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscRsaConnectionVcFrmLossTimeouts_Type.__name__ = "Unsigned32"
_MscRsaConnectionVcFrmLossTimeouts_Object = MibTableColumn
mscRsaConnectionVcFrmLossTimeouts = _MscRsaConnectionVcFrmLossTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 4, 2, 12, 1, 9),
    _MscRsaConnectionVcFrmLossTimeouts_Type()
)
mscRsaConnectionVcFrmLossTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRsaConnectionVcFrmLossTimeouts.setStatus("mandatory")


class _MscRsaConnectionVcOoSeqByteCntExceeded_Type(Unsigned32):
    """Custom type mscRsaConnectionVcOoSeqByteCntExceeded based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscRsaConnectionVcOoSeqByteCntExceeded_Type.__name__ = "Unsigned32"
_MscRsaConnectionVcOoSeqByteCntExceeded_Object = MibTableColumn
mscRsaConnectionVcOoSeqByteCntExceeded = _MscRsaConnectionVcOoSeqByteCntExceeded_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 4, 2, 12, 1, 10),
    _MscRsaConnectionVcOoSeqByteCntExceeded_Type()
)
mscRsaConnectionVcOoSeqByteCntExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRsaConnectionVcOoSeqByteCntExceeded.setStatus("mandatory")


class _MscRsaConnectionVcPeakOoSeqPktCount_Type(Unsigned32):
    """Custom type mscRsaConnectionVcPeakOoSeqPktCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscRsaConnectionVcPeakOoSeqPktCount_Type.__name__ = "Unsigned32"
_MscRsaConnectionVcPeakOoSeqPktCount_Object = MibTableColumn
mscRsaConnectionVcPeakOoSeqPktCount = _MscRsaConnectionVcPeakOoSeqPktCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 4, 2, 12, 1, 11),
    _MscRsaConnectionVcPeakOoSeqPktCount_Type()
)
mscRsaConnectionVcPeakOoSeqPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRsaConnectionVcPeakOoSeqPktCount.setStatus("mandatory")


class _MscRsaConnectionVcPeakOoSeqFrmForwarded_Type(Unsigned32):
    """Custom type mscRsaConnectionVcPeakOoSeqFrmForwarded based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscRsaConnectionVcPeakOoSeqFrmForwarded_Type.__name__ = "Unsigned32"
_MscRsaConnectionVcPeakOoSeqFrmForwarded_Object = MibTableColumn
mscRsaConnectionVcPeakOoSeqFrmForwarded = _MscRsaConnectionVcPeakOoSeqFrmForwarded_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 4, 2, 12, 1, 12),
    _MscRsaConnectionVcPeakOoSeqFrmForwarded_Type()
)
mscRsaConnectionVcPeakOoSeqFrmForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRsaConnectionVcPeakOoSeqFrmForwarded.setStatus("mandatory")


class _MscRsaConnectionVcSendSequenceNumber_Type(Unsigned32):
    """Custom type mscRsaConnectionVcSendSequenceNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscRsaConnectionVcSendSequenceNumber_Type.__name__ = "Unsigned32"
_MscRsaConnectionVcSendSequenceNumber_Object = MibTableColumn
mscRsaConnectionVcSendSequenceNumber = _MscRsaConnectionVcSendSequenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 4, 2, 12, 1, 13),
    _MscRsaConnectionVcSendSequenceNumber_Type()
)
mscRsaConnectionVcSendSequenceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRsaConnectionVcSendSequenceNumber.setStatus("mandatory")


class _MscRsaConnectionVcPktRetryTimeouts_Type(Unsigned32):
    """Custom type mscRsaConnectionVcPktRetryTimeouts based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscRsaConnectionVcPktRetryTimeouts_Type.__name__ = "Unsigned32"
_MscRsaConnectionVcPktRetryTimeouts_Object = MibTableColumn
mscRsaConnectionVcPktRetryTimeouts = _MscRsaConnectionVcPktRetryTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 4, 2, 12, 1, 15),
    _MscRsaConnectionVcPktRetryTimeouts_Type()
)
mscRsaConnectionVcPktRetryTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRsaConnectionVcPktRetryTimeouts.setStatus("mandatory")


class _MscRsaConnectionVcPeakRetryQueueSize_Type(Unsigned32):
    """Custom type mscRsaConnectionVcPeakRetryQueueSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscRsaConnectionVcPeakRetryQueueSize_Type.__name__ = "Unsigned32"
_MscRsaConnectionVcPeakRetryQueueSize_Object = MibTableColumn
mscRsaConnectionVcPeakRetryQueueSize = _MscRsaConnectionVcPeakRetryQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 4, 2, 12, 1, 16),
    _MscRsaConnectionVcPeakRetryQueueSize_Type()
)
mscRsaConnectionVcPeakRetryQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRsaConnectionVcPeakRetryQueueSize.setStatus("mandatory")


class _MscRsaConnectionVcSubnetRecoveries_Type(Unsigned32):
    """Custom type mscRsaConnectionVcSubnetRecoveries based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscRsaConnectionVcSubnetRecoveries_Type.__name__ = "Unsigned32"
_MscRsaConnectionVcSubnetRecoveries_Object = MibTableColumn
mscRsaConnectionVcSubnetRecoveries = _MscRsaConnectionVcSubnetRecoveries_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 4, 2, 12, 1, 17),
    _MscRsaConnectionVcSubnetRecoveries_Type()
)
mscRsaConnectionVcSubnetRecoveries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRsaConnectionVcSubnetRecoveries.setStatus("mandatory")


class _MscRsaConnectionVcOoSeqPktCntExceeded_Type(Unsigned32):
    """Custom type mscRsaConnectionVcOoSeqPktCntExceeded based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscRsaConnectionVcOoSeqPktCntExceeded_Type.__name__ = "Unsigned32"
_MscRsaConnectionVcOoSeqPktCntExceeded_Object = MibTableColumn
mscRsaConnectionVcOoSeqPktCntExceeded = _MscRsaConnectionVcOoSeqPktCntExceeded_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 4, 2, 12, 1, 19),
    _MscRsaConnectionVcOoSeqPktCntExceeded_Type()
)
mscRsaConnectionVcOoSeqPktCntExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRsaConnectionVcOoSeqPktCntExceeded.setStatus("mandatory")


class _MscRsaConnectionVcPeakOoSeqByteCount_Type(Unsigned32):
    """Custom type mscRsaConnectionVcPeakOoSeqByteCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50000),
    )


_MscRsaConnectionVcPeakOoSeqByteCount_Type.__name__ = "Unsigned32"
_MscRsaConnectionVcPeakOoSeqByteCount_Object = MibTableColumn
mscRsaConnectionVcPeakOoSeqByteCount = _MscRsaConnectionVcPeakOoSeqByteCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 4, 2, 12, 1, 20),
    _MscRsaConnectionVcPeakOoSeqByteCount_Type()
)
mscRsaConnectionVcPeakOoSeqByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRsaConnectionVcPeakOoSeqByteCount.setStatus("mandatory")
_MscRsaConnectionVcDmepTable_Object = MibTable
mscRsaConnectionVcDmepTable = _MscRsaConnectionVcDmepTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 4, 2, 417)
)
if mibBuilder.loadTexts:
    mscRsaConnectionVcDmepTable.setStatus("mandatory")
_MscRsaConnectionVcDmepEntry_Object = MibTableRow
mscRsaConnectionVcDmepEntry = _MscRsaConnectionVcDmepEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 4, 2, 417, 1)
)
mscRsaConnectionVcDmepEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-ServerAccessRsaMIB", "mscRsaIndex"),
    (0, "Nortel-MsCarrier-MscPassport-ServerAccessRsaMIB", "mscRsaConnectionIndex"),
    (0, "Nortel-MsCarrier-MscPassport-ServerAccessRsaMIB", "mscRsaConnectionVcIndex"),
    (0, "Nortel-MsCarrier-MscPassport-ServerAccessRsaMIB", "mscRsaConnectionVcDmepValue"),
)
if mibBuilder.loadTexts:
    mscRsaConnectionVcDmepEntry.setStatus("mandatory")
_MscRsaConnectionVcDmepValue_Type = RowPointer
_MscRsaConnectionVcDmepValue_Object = MibTableColumn
mscRsaConnectionVcDmepValue = _MscRsaConnectionVcDmepValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 4, 2, 417, 1, 1),
    _MscRsaConnectionVcDmepValue_Type()
)
mscRsaConnectionVcDmepValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRsaConnectionVcDmepValue.setStatus("mandatory")
_MscRsaConnectionOperationalTable_Object = MibTable
mscRsaConnectionOperationalTable = _MscRsaConnectionOperationalTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 4, 10)
)
if mibBuilder.loadTexts:
    mscRsaConnectionOperationalTable.setStatus("mandatory")
_MscRsaConnectionOperationalEntry_Object = MibTableRow
mscRsaConnectionOperationalEntry = _MscRsaConnectionOperationalEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 4, 10, 1)
)
mscRsaConnectionOperationalEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-ServerAccessRsaMIB", "mscRsaIndex"),
    (0, "Nortel-MsCarrier-MscPassport-ServerAccessRsaMIB", "mscRsaConnectionIndex"),
)
if mibBuilder.loadTexts:
    mscRsaConnectionOperationalEntry.setStatus("mandatory")


class _MscRsaConnectionRemoteName_Type(AsciiString):
    """Custom type mscRsaConnectionRemoteName based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MscRsaConnectionRemoteName_Type.__name__ = "AsciiString"
_MscRsaConnectionRemoteName_Object = MibTableColumn
mscRsaConnectionRemoteName = _MscRsaConnectionRemoteName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 4, 10, 1, 1),
    _MscRsaConnectionRemoteName_Type()
)
mscRsaConnectionRemoteName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRsaConnectionRemoteName.setStatus("mandatory")


class _MscRsaConnectionCallState_Type(Integer32):
    """Custom type mscRsaConnectionCallState based on Integer32"""
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


_MscRsaConnectionCallState_Type.__name__ = "Integer32"
_MscRsaConnectionCallState_Object = MibTableColumn
mscRsaConnectionCallState = _MscRsaConnectionCallState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 4, 10, 1, 2),
    _MscRsaConnectionCallState_Type()
)
mscRsaConnectionCallState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRsaConnectionCallState.setStatus("mandatory")
_MscRsaConnectionServerStatsTable_Object = MibTable
mscRsaConnectionServerStatsTable = _MscRsaConnectionServerStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 4, 11)
)
if mibBuilder.loadTexts:
    mscRsaConnectionServerStatsTable.setStatus("mandatory")
_MscRsaConnectionServerStatsEntry_Object = MibTableRow
mscRsaConnectionServerStatsEntry = _MscRsaConnectionServerStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 4, 11, 1)
)
mscRsaConnectionServerStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-ServerAccessRsaMIB", "mscRsaIndex"),
    (0, "Nortel-MsCarrier-MscPassport-ServerAccessRsaMIB", "mscRsaConnectionIndex"),
)
if mibBuilder.loadTexts:
    mscRsaConnectionServerStatsEntry.setStatus("mandatory")
_MscRsaConnectionVncsRequests_Type = Counter32
_MscRsaConnectionVncsRequests_Object = MibTableColumn
mscRsaConnectionVncsRequests = _MscRsaConnectionVncsRequests_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 4, 11, 1, 1),
    _MscRsaConnectionVncsRequests_Type()
)
mscRsaConnectionVncsRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRsaConnectionVncsRequests.setStatus("mandatory")
_MscRsaConnectionVncsReplies_Type = Counter32
_MscRsaConnectionVncsReplies_Object = MibTableColumn
mscRsaConnectionVncsReplies = _MscRsaConnectionVncsReplies_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 4, 11, 1, 2),
    _MscRsaConnectionVncsReplies_Type()
)
mscRsaConnectionVncsReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRsaConnectionVncsReplies.setStatus("mandatory")
_MscRsaConnectionLapfStatusTable_Object = MibTable
mscRsaConnectionLapfStatusTable = _MscRsaConnectionLapfStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 4, 12)
)
if mibBuilder.loadTexts:
    mscRsaConnectionLapfStatusTable.setStatus("mandatory")
_MscRsaConnectionLapfStatusEntry_Object = MibTableRow
mscRsaConnectionLapfStatusEntry = _MscRsaConnectionLapfStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 4, 12, 1)
)
mscRsaConnectionLapfStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-ServerAccessRsaMIB", "mscRsaIndex"),
    (0, "Nortel-MsCarrier-MscPassport-ServerAccessRsaMIB", "mscRsaConnectionIndex"),
)
if mibBuilder.loadTexts:
    mscRsaConnectionLapfStatusEntry.setStatus("mandatory")


class _MscRsaConnectionLapfState_Type(Integer32):
    """Custom type mscRsaConnectionLapfState based on Integer32"""
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


_MscRsaConnectionLapfState_Type.__name__ = "Integer32"
_MscRsaConnectionLapfState_Object = MibTableColumn
mscRsaConnectionLapfState = _MscRsaConnectionLapfState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 4, 12, 1, 1),
    _MscRsaConnectionLapfState_Type()
)
mscRsaConnectionLapfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRsaConnectionLapfState.setStatus("mandatory")
_MscRsaConnectionLapfQueueSize_Type = Counter32
_MscRsaConnectionLapfQueueSize_Object = MibTableColumn
mscRsaConnectionLapfQueueSize = _MscRsaConnectionLapfQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 4, 12, 1, 4),
    _MscRsaConnectionLapfQueueSize_Type()
)
mscRsaConnectionLapfQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRsaConnectionLapfQueueSize.setStatus("mandatory")
_MscRsaConnectionLapfStatsTable_Object = MibTable
mscRsaConnectionLapfStatsTable = _MscRsaConnectionLapfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 4, 13)
)
if mibBuilder.loadTexts:
    mscRsaConnectionLapfStatsTable.setStatus("mandatory")
_MscRsaConnectionLapfStatsEntry_Object = MibTableRow
mscRsaConnectionLapfStatsEntry = _MscRsaConnectionLapfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 4, 13, 1)
)
mscRsaConnectionLapfStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-ServerAccessRsaMIB", "mscRsaIndex"),
    (0, "Nortel-MsCarrier-MscPassport-ServerAccessRsaMIB", "mscRsaConnectionIndex"),
)
if mibBuilder.loadTexts:
    mscRsaConnectionLapfStatsEntry.setStatus("mandatory")
_MscRsaConnectionLapfStateChanges_Type = Counter32
_MscRsaConnectionLapfStateChanges_Object = MibTableColumn
mscRsaConnectionLapfStateChanges = _MscRsaConnectionLapfStateChanges_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 4, 13, 1, 1),
    _MscRsaConnectionLapfStateChanges_Type()
)
mscRsaConnectionLapfStateChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRsaConnectionLapfStateChanges.setStatus("mandatory")
_MscRsaConnectionLapfRemoteBusy_Type = Counter32
_MscRsaConnectionLapfRemoteBusy_Object = MibTableColumn
mscRsaConnectionLapfRemoteBusy = _MscRsaConnectionLapfRemoteBusy_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 4, 13, 1, 2),
    _MscRsaConnectionLapfRemoteBusy_Type()
)
mscRsaConnectionLapfRemoteBusy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRsaConnectionLapfRemoteBusy.setStatus("mandatory")
_MscRsaConnectionLapfAckTimeouts_Type = Counter32
_MscRsaConnectionLapfAckTimeouts_Object = MibTableColumn
mscRsaConnectionLapfAckTimeouts = _MscRsaConnectionLapfAckTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 4, 13, 1, 3),
    _MscRsaConnectionLapfAckTimeouts_Type()
)
mscRsaConnectionLapfAckTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRsaConnectionLapfAckTimeouts.setStatus("mandatory")
_MscRsaConnectionLapfRejectFramesRx_Type = Counter32
_MscRsaConnectionLapfRejectFramesRx_Object = MibTableColumn
mscRsaConnectionLapfRejectFramesRx = _MscRsaConnectionLapfRejectFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 4, 13, 1, 4),
    _MscRsaConnectionLapfRejectFramesRx_Type()
)
mscRsaConnectionLapfRejectFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRsaConnectionLapfRejectFramesRx.setStatus("mandatory")
_MscRsaConnectionLapfIFramesTx_Type = Counter32
_MscRsaConnectionLapfIFramesTx_Object = MibTableColumn
mscRsaConnectionLapfIFramesTx = _MscRsaConnectionLapfIFramesTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 4, 13, 1, 5),
    _MscRsaConnectionLapfIFramesTx_Type()
)
mscRsaConnectionLapfIFramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRsaConnectionLapfIFramesTx.setStatus("mandatory")
_MscRsaConnectionLapfIFramesTxDiscarded_Type = Counter32
_MscRsaConnectionLapfIFramesTxDiscarded_Object = MibTableColumn
mscRsaConnectionLapfIFramesTxDiscarded = _MscRsaConnectionLapfIFramesTxDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 4, 13, 1, 6),
    _MscRsaConnectionLapfIFramesTxDiscarded_Type()
)
mscRsaConnectionLapfIFramesTxDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRsaConnectionLapfIFramesTxDiscarded.setStatus("mandatory")
_MscRsaConnectionLapfIFramesRx_Type = Counter32
_MscRsaConnectionLapfIFramesRx_Object = MibTableColumn
mscRsaConnectionLapfIFramesRx = _MscRsaConnectionLapfIFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 4, 13, 1, 7),
    _MscRsaConnectionLapfIFramesRx_Type()
)
mscRsaConnectionLapfIFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRsaConnectionLapfIFramesRx.setStatus("mandatory")
_MscRsaConnectionLapfIFramesRxDiscarded_Type = Counter32
_MscRsaConnectionLapfIFramesRxDiscarded_Object = MibTableColumn
mscRsaConnectionLapfIFramesRxDiscarded = _MscRsaConnectionLapfIFramesRxDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 4, 13, 1, 8),
    _MscRsaConnectionLapfIFramesRxDiscarded_Type()
)
mscRsaConnectionLapfIFramesRxDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRsaConnectionLapfIFramesRxDiscarded.setStatus("mandatory")
_MscRsaOptionsTable_Object = MibTable
mscRsaOptionsTable = _MscRsaOptionsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 10)
)
if mibBuilder.loadTexts:
    mscRsaOptionsTable.setStatus("mandatory")
_MscRsaOptionsEntry_Object = MibTableRow
mscRsaOptionsEntry = _MscRsaOptionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 10, 1)
)
mscRsaOptionsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-ServerAccessRsaMIB", "mscRsaIndex"),
)
if mibBuilder.loadTexts:
    mscRsaOptionsEntry.setStatus("mandatory")
_MscRsaLogicalProcessor_Type = Link
_MscRsaLogicalProcessor_Object = MibTableColumn
mscRsaLogicalProcessor = _MscRsaLogicalProcessor_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 10, 1, 2),
    _MscRsaLogicalProcessor_Type()
)
mscRsaLogicalProcessor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscRsaLogicalProcessor.setStatus("mandatory")
_MscRsaStateTable_Object = MibTable
mscRsaStateTable = _MscRsaStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 11)
)
if mibBuilder.loadTexts:
    mscRsaStateTable.setStatus("mandatory")
_MscRsaStateEntry_Object = MibTableRow
mscRsaStateEntry = _MscRsaStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 11, 1)
)
mscRsaStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-ServerAccessRsaMIB", "mscRsaIndex"),
)
if mibBuilder.loadTexts:
    mscRsaStateEntry.setStatus("mandatory")


class _MscRsaAdminState_Type(Integer32):
    """Custom type mscRsaAdminState based on Integer32"""
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


_MscRsaAdminState_Type.__name__ = "Integer32"
_MscRsaAdminState_Object = MibTableColumn
mscRsaAdminState = _MscRsaAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 11, 1, 1),
    _MscRsaAdminState_Type()
)
mscRsaAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRsaAdminState.setStatus("mandatory")


class _MscRsaOperationalState_Type(Integer32):
    """Custom type mscRsaOperationalState based on Integer32"""
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


_MscRsaOperationalState_Type.__name__ = "Integer32"
_MscRsaOperationalState_Object = MibTableColumn
mscRsaOperationalState = _MscRsaOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 11, 1, 2),
    _MscRsaOperationalState_Type()
)
mscRsaOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRsaOperationalState.setStatus("mandatory")


class _MscRsaUsageState_Type(Integer32):
    """Custom type mscRsaUsageState based on Integer32"""
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


_MscRsaUsageState_Type.__name__ = "Integer32"
_MscRsaUsageState_Object = MibTableColumn
mscRsaUsageState = _MscRsaUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 11, 1, 3),
    _MscRsaUsageState_Type()
)
mscRsaUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRsaUsageState.setStatus("mandatory")
_MscRsaOperationalTable_Object = MibTable
mscRsaOperationalTable = _MscRsaOperationalTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 12)
)
if mibBuilder.loadTexts:
    mscRsaOperationalTable.setStatus("mandatory")
_MscRsaOperationalEntry_Object = MibTableRow
mscRsaOperationalEntry = _MscRsaOperationalEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 12, 1)
)
mscRsaOperationalEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-ServerAccessRsaMIB", "mscRsaIndex"),
)
if mibBuilder.loadTexts:
    mscRsaOperationalEntry.setStatus("mandatory")


class _MscRsaMaxRsiConnections_Type(Integer32):
    """Custom type mscRsaMaxRsiConnections based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 1000),
    )


_MscRsaMaxRsiConnections_Type.__name__ = "Integer32"
_MscRsaMaxRsiConnections_Object = MibTableColumn
mscRsaMaxRsiConnections = _MscRsaMaxRsiConnections_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 12, 1, 2),
    _MscRsaMaxRsiConnections_Type()
)
mscRsaMaxRsiConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRsaMaxRsiConnections.setStatus("mandatory")


class _MscRsaRsiConnections_Type(Integer32):
    """Custom type mscRsaRsiConnections based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_MscRsaRsiConnections_Type.__name__ = "Integer32"
_MscRsaRsiConnections_Object = MibTableColumn
mscRsaRsiConnections = _MscRsaRsiConnections_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 108, 12, 1, 3),
    _MscRsaRsiConnections_Type()
)
mscRsaRsiConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRsaRsiConnections.setStatus("mandatory")
_ServerAccessRsaMIB_ObjectIdentity = ObjectIdentity
serverAccessRsaMIB = _ServerAccessRsaMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 116)
)
_ServerAccessRsaGroup_ObjectIdentity = ObjectIdentity
serverAccessRsaGroup = _ServerAccessRsaGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 116, 1)
)
_ServerAccessRsaGroupCA_ObjectIdentity = ObjectIdentity
serverAccessRsaGroupCA = _ServerAccessRsaGroupCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 116, 1, 1)
)
_ServerAccessRsaGroupCA02_ObjectIdentity = ObjectIdentity
serverAccessRsaGroupCA02 = _ServerAccessRsaGroupCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 116, 1, 1, 3)
)
_ServerAccessRsaGroupCA02A_ObjectIdentity = ObjectIdentity
serverAccessRsaGroupCA02A = _ServerAccessRsaGroupCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 116, 1, 1, 3, 2)
)
_ServerAccessRsaCapabilities_ObjectIdentity = ObjectIdentity
serverAccessRsaCapabilities = _ServerAccessRsaCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 116, 3)
)
_ServerAccessRsaCapabilitiesCA_ObjectIdentity = ObjectIdentity
serverAccessRsaCapabilitiesCA = _ServerAccessRsaCapabilitiesCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 116, 3, 1)
)
_ServerAccessRsaCapabilitiesCA02_ObjectIdentity = ObjectIdentity
serverAccessRsaCapabilitiesCA02 = _ServerAccessRsaCapabilitiesCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 116, 3, 1, 3)
)
_ServerAccessRsaCapabilitiesCA02A_ObjectIdentity = ObjectIdentity
serverAccessRsaCapabilitiesCA02A = _ServerAccessRsaCapabilitiesCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 116, 3, 1, 3, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-MsCarrier-MscPassport-ServerAccessRsaMIB",
    **{"mscRsa": mscRsa,
       "mscRsaRowStatusTable": mscRsaRowStatusTable,
       "mscRsaRowStatusEntry": mscRsaRowStatusEntry,
       "mscRsaRowStatus": mscRsaRowStatus,
       "mscRsaComponentName": mscRsaComponentName,
       "mscRsaStorageType": mscRsaStorageType,
       "mscRsaIndex": mscRsaIndex,
       "mscRsaDna": mscRsaDna,
       "mscRsaDnaRowStatusTable": mscRsaDnaRowStatusTable,
       "mscRsaDnaRowStatusEntry": mscRsaDnaRowStatusEntry,
       "mscRsaDnaRowStatus": mscRsaDnaRowStatus,
       "mscRsaDnaComponentName": mscRsaDnaComponentName,
       "mscRsaDnaStorageType": mscRsaDnaStorageType,
       "mscRsaDnaIndex": mscRsaDnaIndex,
       "mscRsaDnaCug": mscRsaDnaCug,
       "mscRsaDnaCugRowStatusTable": mscRsaDnaCugRowStatusTable,
       "mscRsaDnaCugRowStatusEntry": mscRsaDnaCugRowStatusEntry,
       "mscRsaDnaCugRowStatus": mscRsaDnaCugRowStatus,
       "mscRsaDnaCugComponentName": mscRsaDnaCugComponentName,
       "mscRsaDnaCugStorageType": mscRsaDnaCugStorageType,
       "mscRsaDnaCugIndex": mscRsaDnaCugIndex,
       "mscRsaDnaCugCugOptionsTable": mscRsaDnaCugCugOptionsTable,
       "mscRsaDnaCugCugOptionsEntry": mscRsaDnaCugCugOptionsEntry,
       "mscRsaDnaCugType": mscRsaDnaCugType,
       "mscRsaDnaCugDnic": mscRsaDnaCugDnic,
       "mscRsaDnaCugInterlockCode": mscRsaDnaCugInterlockCode,
       "mscRsaDnaCugPreferential": mscRsaDnaCugPreferential,
       "mscRsaDnaCugOutCalls": mscRsaDnaCugOutCalls,
       "mscRsaDnaCugIncCalls": mscRsaDnaCugIncCalls,
       "mscRsaDnaCugPrivileged": mscRsaDnaCugPrivileged,
       "mscRsaDnaAddressTable": mscRsaDnaAddressTable,
       "mscRsaDnaAddressEntry": mscRsaDnaAddressEntry,
       "mscRsaDnaNumberingPlanIndicator": mscRsaDnaNumberingPlanIndicator,
       "mscRsaDnaDataNetworkAddress": mscRsaDnaDataNetworkAddress,
       "mscRsaDnaOutgoingOptionsTable": mscRsaDnaOutgoingOptionsTable,
       "mscRsaDnaOutgoingOptionsEntry": mscRsaDnaOutgoingOptionsEntry,
       "mscRsaDnaOutCalls": mscRsaDnaOutCalls,
       "mscRsaDnaIncomingOptionsTable": mscRsaDnaIncomingOptionsTable,
       "mscRsaDnaIncomingOptionsEntry": mscRsaDnaIncomingOptionsEntry,
       "mscRsaDnaIncCalls": mscRsaDnaIncCalls,
       "mscRsaDnaIncAccess": mscRsaDnaIncAccess,
       "mscRsaVncsAccess": mscRsaVncsAccess,
       "mscRsaVncsAccessRowStatusTable": mscRsaVncsAccessRowStatusTable,
       "mscRsaVncsAccessRowStatusEntry": mscRsaVncsAccessRowStatusEntry,
       "mscRsaVncsAccessRowStatus": mscRsaVncsAccessRowStatus,
       "mscRsaVncsAccessComponentName": mscRsaVncsAccessComponentName,
       "mscRsaVncsAccessStorageType": mscRsaVncsAccessStorageType,
       "mscRsaVncsAccessIndex": mscRsaVncsAccessIndex,
       "mscRsaVncsAccessProvisionedTable": mscRsaVncsAccessProvisionedTable,
       "mscRsaVncsAccessProvisionedEntry": mscRsaVncsAccessProvisionedEntry,
       "mscRsaVncsAccessTimeToLive": mscRsaVncsAccessTimeToLive,
       "mscRsaVncsAccessStateTable": mscRsaVncsAccessStateTable,
       "mscRsaVncsAccessStateEntry": mscRsaVncsAccessStateEntry,
       "mscRsaVncsAccessAdminState": mscRsaVncsAccessAdminState,
       "mscRsaVncsAccessOperationalState": mscRsaVncsAccessOperationalState,
       "mscRsaVncsAccessUsageState": mscRsaVncsAccessUsageState,
       "mscRsaVncsAccessOperationalTable": mscRsaVncsAccessOperationalTable,
       "mscRsaVncsAccessOperationalEntry": mscRsaVncsAccessOperationalEntry,
       "mscRsaVncsAccessRequestsSent": mscRsaVncsAccessRequestsSent,
       "mscRsaVncsAccessRepliesReceived": mscRsaVncsAccessRepliesReceived,
       "mscRsaVncsAccessRequestsQueued": mscRsaVncsAccessRequestsQueued,
       "mscRsaVncsAccessRequestsDiscarded": mscRsaVncsAccessRequestsDiscarded,
       "mscRsaConnection": mscRsaConnection,
       "mscRsaConnectionRowStatusTable": mscRsaConnectionRowStatusTable,
       "mscRsaConnectionRowStatusEntry": mscRsaConnectionRowStatusEntry,
       "mscRsaConnectionRowStatus": mscRsaConnectionRowStatus,
       "mscRsaConnectionComponentName": mscRsaConnectionComponentName,
       "mscRsaConnectionStorageType": mscRsaConnectionStorageType,
       "mscRsaConnectionIndex": mscRsaConnectionIndex,
       "mscRsaConnectionVc": mscRsaConnectionVc,
       "mscRsaConnectionVcRowStatusTable": mscRsaConnectionVcRowStatusTable,
       "mscRsaConnectionVcRowStatusEntry": mscRsaConnectionVcRowStatusEntry,
       "mscRsaConnectionVcRowStatus": mscRsaConnectionVcRowStatus,
       "mscRsaConnectionVcComponentName": mscRsaConnectionVcComponentName,
       "mscRsaConnectionVcStorageType": mscRsaConnectionVcStorageType,
       "mscRsaConnectionVcIndex": mscRsaConnectionVcIndex,
       "mscRsaConnectionVcCadTable": mscRsaConnectionVcCadTable,
       "mscRsaConnectionVcCadEntry": mscRsaConnectionVcCadEntry,
       "mscRsaConnectionVcType": mscRsaConnectionVcType,
       "mscRsaConnectionVcState": mscRsaConnectionVcState,
       "mscRsaConnectionVcPreviousState": mscRsaConnectionVcPreviousState,
       "mscRsaConnectionVcDiagnosticCode": mscRsaConnectionVcDiagnosticCode,
       "mscRsaConnectionVcPreviousDiagnosticCode": mscRsaConnectionVcPreviousDiagnosticCode,
       "mscRsaConnectionVcCalledNpi": mscRsaConnectionVcCalledNpi,
       "mscRsaConnectionVcCalledDna": mscRsaConnectionVcCalledDna,
       "mscRsaConnectionVcCalledLcn": mscRsaConnectionVcCalledLcn,
       "mscRsaConnectionVcCallingNpi": mscRsaConnectionVcCallingNpi,
       "mscRsaConnectionVcCallingDna": mscRsaConnectionVcCallingDna,
       "mscRsaConnectionVcCallingLcn": mscRsaConnectionVcCallingLcn,
       "mscRsaConnectionVcAccountingEnabled": mscRsaConnectionVcAccountingEnabled,
       "mscRsaConnectionVcFastSelectCall": mscRsaConnectionVcFastSelectCall,
       "mscRsaConnectionVcPathReliability": mscRsaConnectionVcPathReliability,
       "mscRsaConnectionVcAccountingEnd": mscRsaConnectionVcAccountingEnd,
       "mscRsaConnectionVcPriority": mscRsaConnectionVcPriority,
       "mscRsaConnectionVcSegmentSize": mscRsaConnectionVcSegmentSize,
       "mscRsaConnectionVcMaxSubnetPktSize": mscRsaConnectionVcMaxSubnetPktSize,
       "mscRsaConnectionVcRcosToNetwork": mscRsaConnectionVcRcosToNetwork,
       "mscRsaConnectionVcRcosFromNetwork": mscRsaConnectionVcRcosFromNetwork,
       "mscRsaConnectionVcEmissionPriorityToNetwork": mscRsaConnectionVcEmissionPriorityToNetwork,
       "mscRsaConnectionVcEmissionPriorityFromNetwork": mscRsaConnectionVcEmissionPriorityFromNetwork,
       "mscRsaConnectionVcDataPath": mscRsaConnectionVcDataPath,
       "mscRsaConnectionVcIntdTable": mscRsaConnectionVcIntdTable,
       "mscRsaConnectionVcIntdEntry": mscRsaConnectionVcIntdEntry,
       "mscRsaConnectionVcCallReferenceNumber": mscRsaConnectionVcCallReferenceNumber,
       "mscRsaConnectionVcElapsedTimeTillNow": mscRsaConnectionVcElapsedTimeTillNow,
       "mscRsaConnectionVcSegmentsRx": mscRsaConnectionVcSegmentsRx,
       "mscRsaConnectionVcSegmentsSent": mscRsaConnectionVcSegmentsSent,
       "mscRsaConnectionVcStartTime": mscRsaConnectionVcStartTime,
       "mscRsaConnectionVcCallReferenceNumberDecimal": mscRsaConnectionVcCallReferenceNumberDecimal,
       "mscRsaConnectionVcFrdTable": mscRsaConnectionVcFrdTable,
       "mscRsaConnectionVcFrdEntry": mscRsaConnectionVcFrdEntry,
       "mscRsaConnectionVcFrmCongestedToSubnet": mscRsaConnectionVcFrmCongestedToSubnet,
       "mscRsaConnectionVcCannotForwardToSubnet": mscRsaConnectionVcCannotForwardToSubnet,
       "mscRsaConnectionVcNotDataXferToSubnet": mscRsaConnectionVcNotDataXferToSubnet,
       "mscRsaConnectionVcOutOfRangeFrmFromSubnet": mscRsaConnectionVcOutOfRangeFrmFromSubnet,
       "mscRsaConnectionVcCombErrorsFromSubnet": mscRsaConnectionVcCombErrorsFromSubnet,
       "mscRsaConnectionVcDuplicatesFromSubnet": mscRsaConnectionVcDuplicatesFromSubnet,
       "mscRsaConnectionVcNotDataXferFromSubnet": mscRsaConnectionVcNotDataXferFromSubnet,
       "mscRsaConnectionVcFrmLossTimeouts": mscRsaConnectionVcFrmLossTimeouts,
       "mscRsaConnectionVcOoSeqByteCntExceeded": mscRsaConnectionVcOoSeqByteCntExceeded,
       "mscRsaConnectionVcPeakOoSeqPktCount": mscRsaConnectionVcPeakOoSeqPktCount,
       "mscRsaConnectionVcPeakOoSeqFrmForwarded": mscRsaConnectionVcPeakOoSeqFrmForwarded,
       "mscRsaConnectionVcSendSequenceNumber": mscRsaConnectionVcSendSequenceNumber,
       "mscRsaConnectionVcPktRetryTimeouts": mscRsaConnectionVcPktRetryTimeouts,
       "mscRsaConnectionVcPeakRetryQueueSize": mscRsaConnectionVcPeakRetryQueueSize,
       "mscRsaConnectionVcSubnetRecoveries": mscRsaConnectionVcSubnetRecoveries,
       "mscRsaConnectionVcOoSeqPktCntExceeded": mscRsaConnectionVcOoSeqPktCntExceeded,
       "mscRsaConnectionVcPeakOoSeqByteCount": mscRsaConnectionVcPeakOoSeqByteCount,
       "mscRsaConnectionVcDmepTable": mscRsaConnectionVcDmepTable,
       "mscRsaConnectionVcDmepEntry": mscRsaConnectionVcDmepEntry,
       "mscRsaConnectionVcDmepValue": mscRsaConnectionVcDmepValue,
       "mscRsaConnectionOperationalTable": mscRsaConnectionOperationalTable,
       "mscRsaConnectionOperationalEntry": mscRsaConnectionOperationalEntry,
       "mscRsaConnectionRemoteName": mscRsaConnectionRemoteName,
       "mscRsaConnectionCallState": mscRsaConnectionCallState,
       "mscRsaConnectionServerStatsTable": mscRsaConnectionServerStatsTable,
       "mscRsaConnectionServerStatsEntry": mscRsaConnectionServerStatsEntry,
       "mscRsaConnectionVncsRequests": mscRsaConnectionVncsRequests,
       "mscRsaConnectionVncsReplies": mscRsaConnectionVncsReplies,
       "mscRsaConnectionLapfStatusTable": mscRsaConnectionLapfStatusTable,
       "mscRsaConnectionLapfStatusEntry": mscRsaConnectionLapfStatusEntry,
       "mscRsaConnectionLapfState": mscRsaConnectionLapfState,
       "mscRsaConnectionLapfQueueSize": mscRsaConnectionLapfQueueSize,
       "mscRsaConnectionLapfStatsTable": mscRsaConnectionLapfStatsTable,
       "mscRsaConnectionLapfStatsEntry": mscRsaConnectionLapfStatsEntry,
       "mscRsaConnectionLapfStateChanges": mscRsaConnectionLapfStateChanges,
       "mscRsaConnectionLapfRemoteBusy": mscRsaConnectionLapfRemoteBusy,
       "mscRsaConnectionLapfAckTimeouts": mscRsaConnectionLapfAckTimeouts,
       "mscRsaConnectionLapfRejectFramesRx": mscRsaConnectionLapfRejectFramesRx,
       "mscRsaConnectionLapfIFramesTx": mscRsaConnectionLapfIFramesTx,
       "mscRsaConnectionLapfIFramesTxDiscarded": mscRsaConnectionLapfIFramesTxDiscarded,
       "mscRsaConnectionLapfIFramesRx": mscRsaConnectionLapfIFramesRx,
       "mscRsaConnectionLapfIFramesRxDiscarded": mscRsaConnectionLapfIFramesRxDiscarded,
       "mscRsaOptionsTable": mscRsaOptionsTable,
       "mscRsaOptionsEntry": mscRsaOptionsEntry,
       "mscRsaLogicalProcessor": mscRsaLogicalProcessor,
       "mscRsaStateTable": mscRsaStateTable,
       "mscRsaStateEntry": mscRsaStateEntry,
       "mscRsaAdminState": mscRsaAdminState,
       "mscRsaOperationalState": mscRsaOperationalState,
       "mscRsaUsageState": mscRsaUsageState,
       "mscRsaOperationalTable": mscRsaOperationalTable,
       "mscRsaOperationalEntry": mscRsaOperationalEntry,
       "mscRsaMaxRsiConnections": mscRsaMaxRsiConnections,
       "mscRsaRsiConnections": mscRsaRsiConnections,
       "serverAccessRsaMIB": serverAccessRsaMIB,
       "serverAccessRsaGroup": serverAccessRsaGroup,
       "serverAccessRsaGroupCA": serverAccessRsaGroupCA,
       "serverAccessRsaGroupCA02": serverAccessRsaGroupCA02,
       "serverAccessRsaGroupCA02A": serverAccessRsaGroupCA02A,
       "serverAccessRsaCapabilities": serverAccessRsaCapabilities,
       "serverAccessRsaCapabilitiesCA": serverAccessRsaCapabilitiesCA,
       "serverAccessRsaCapabilitiesCA02": serverAccessRsaCapabilitiesCA02,
       "serverAccessRsaCapabilitiesCA02A": serverAccessRsaCapabilitiesCA02A}
)
