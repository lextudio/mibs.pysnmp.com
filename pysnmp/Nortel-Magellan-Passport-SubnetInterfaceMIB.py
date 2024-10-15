# SNMP MIB module (Nortel-Magellan-Passport-SubnetInterfaceMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-Magellan-Passport-SubnetInterfaceMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:31:25 2024
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

(mod,
 modIndex) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-ShelfMIB",
    "mod",
    "modIndex")

(DisplayString,
 Integer32,
 RowStatus,
 StorageType,
 Unsigned32) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-StandardTextualConventionsMIB",
    "DisplayString",
    "Integer32",
    "RowStatus",
    "StorageType",
    "Unsigned32")

(DigitString,
 NonReplicated) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-TextualConventionsMIB",
    "DigitString",
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

_ModVcs_ObjectIdentity = ObjectIdentity
modVcs = _ModVcs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 16, 2)
)
_ModVcsRowStatusTable_Object = MibTable
modVcsRowStatusTable = _ModVcsRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 16, 2, 1)
)
if mibBuilder.loadTexts:
    modVcsRowStatusTable.setStatus("mandatory")
_ModVcsRowStatusEntry_Object = MibTableRow
modVcsRowStatusEntry = _ModVcsRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 16, 2, 1, 1)
)
modVcsRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-ShelfMIB", "modIndex"),
    (0, "Nortel-Magellan-Passport-SubnetInterfaceMIB", "modVcsIndex"),
)
if mibBuilder.loadTexts:
    modVcsRowStatusEntry.setStatus("mandatory")
_ModVcsRowStatus_Type = RowStatus
_ModVcsRowStatus_Object = MibTableColumn
modVcsRowStatus = _ModVcsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 16, 2, 1, 1, 1),
    _ModVcsRowStatus_Type()
)
modVcsRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modVcsRowStatus.setStatus("mandatory")
_ModVcsComponentName_Type = DisplayString
_ModVcsComponentName_Object = MibTableColumn
modVcsComponentName = _ModVcsComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 16, 2, 1, 1, 2),
    _ModVcsComponentName_Type()
)
modVcsComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modVcsComponentName.setStatus("mandatory")
_ModVcsStorageType_Type = StorageType
_ModVcsStorageType_Object = MibTableColumn
modVcsStorageType = _ModVcsStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 16, 2, 1, 1, 4),
    _ModVcsStorageType_Type()
)
modVcsStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modVcsStorageType.setStatus("mandatory")
_ModVcsIndex_Type = NonReplicated
_ModVcsIndex_Object = MibTableColumn
modVcsIndex = _ModVcsIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 16, 2, 1, 1, 10),
    _ModVcsIndex_Type()
)
modVcsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    modVcsIndex.setStatus("mandatory")
_ModVcsAccOptTable_Object = MibTable
modVcsAccOptTable = _ModVcsAccOptTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 16, 2, 10)
)
if mibBuilder.loadTexts:
    modVcsAccOptTable.setStatus("mandatory")
_ModVcsAccOptEntry_Object = MibTableRow
modVcsAccOptEntry = _ModVcsAccOptEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 16, 2, 10, 1)
)
modVcsAccOptEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-ShelfMIB", "modIndex"),
    (0, "Nortel-Magellan-Passport-SubnetInterfaceMIB", "modVcsIndex"),
)
if mibBuilder.loadTexts:
    modVcsAccOptEntry.setStatus("mandatory")


class _ModVcsSegmentSize_Type(Integer32):
    """Custom type modVcsSegmentSize based on Integer32"""
    defaultValue = 7

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
              12)
        )
    )
    namedValues = NamedValues(
        *(("n1", 0),
          ("n1024", 10),
          ("n128", 7),
          ("n16", 4),
          ("n2", 1),
          ("n2048", 11),
          ("n256", 8),
          ("n32", 5),
          ("n4", 2),
          ("n4096", 12),
          ("n512", 9),
          ("n64", 6),
          ("n8", 3))
    )


_ModVcsSegmentSize_Type.__name__ = "Integer32"
_ModVcsSegmentSize_Object = MibTableColumn
modVcsSegmentSize = _ModVcsSegmentSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 16, 2, 10, 1, 1),
    _ModVcsSegmentSize_Type()
)
modVcsSegmentSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modVcsSegmentSize.setStatus("mandatory")


class _ModVcsUnitsCounted_Type(Integer32):
    """Custom type modVcsUnitsCounted based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("frames", 1),
          ("segments", 0))
    )


_ModVcsUnitsCounted_Type.__name__ = "Integer32"
_ModVcsUnitsCounted_Object = MibTableColumn
modVcsUnitsCounted = _ModVcsUnitsCounted_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 16, 2, 10, 1, 2),
    _ModVcsUnitsCounted_Type()
)
modVcsUnitsCounted.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modVcsUnitsCounted.setStatus("mandatory")


class _ModVcsAccountingFax_Type(OctetString):
    """Custom type modVcsAccountingFax based on OctetString"""
    defaultHexValue = "20"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_ModVcsAccountingFax_Type.__name__ = "OctetString"
_ModVcsAccountingFax_Object = MibTableColumn
modVcsAccountingFax = _ModVcsAccountingFax_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 16, 2, 10, 1, 3),
    _ModVcsAccountingFax_Type()
)
modVcsAccountingFax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modVcsAccountingFax.setStatus("mandatory")


class _ModVcsGenerationMode_Type(Integer32):
    """Custom type modVcsGenerationMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("bothEnds", 0),
          ("singleEnd", 1))
    )


_ModVcsGenerationMode_Type.__name__ = "Integer32"
_ModVcsGenerationMode_Object = MibTableColumn
modVcsGenerationMode = _ModVcsGenerationMode_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 16, 2, 10, 1, 4),
    _ModVcsGenerationMode_Type()
)
modVcsGenerationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modVcsGenerationMode.setStatus("mandatory")
_ModVcsAddOptTable_Object = MibTable
modVcsAddOptTable = _ModVcsAddOptTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 16, 2, 12)
)
if mibBuilder.loadTexts:
    modVcsAddOptTable.setStatus("mandatory")
_ModVcsAddOptEntry_Object = MibTableRow
modVcsAddOptEntry = _ModVcsAddOptEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 16, 2, 12, 1)
)
modVcsAddOptEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-ShelfMIB", "modIndex"),
    (0, "Nortel-Magellan-Passport-SubnetInterfaceMIB", "modVcsIndex"),
)
if mibBuilder.loadTexts:
    modVcsAddOptEntry.setStatus("mandatory")


class _ModVcsDefaultNumberingPlan_Type(Integer32):
    """Custom type modVcsDefaultNumberingPlan based on Integer32"""
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


_ModVcsDefaultNumberingPlan_Type.__name__ = "Integer32"
_ModVcsDefaultNumberingPlan_Object = MibTableColumn
modVcsDefaultNumberingPlan = _ModVcsDefaultNumberingPlan_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 16, 2, 12, 1, 3),
    _ModVcsDefaultNumberingPlan_Type()
)
modVcsDefaultNumberingPlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modVcsDefaultNumberingPlan.setStatus("mandatory")


class _ModVcsNetworkIdType_Type(Integer32):
    """Custom type modVcsNetworkIdType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("dnic", 0),
          ("inic", 1))
    )


_ModVcsNetworkIdType_Type.__name__ = "Integer32"
_ModVcsNetworkIdType_Object = MibTableColumn
modVcsNetworkIdType = _ModVcsNetworkIdType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 16, 2, 12, 1, 4),
    _ModVcsNetworkIdType_Type()
)
modVcsNetworkIdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modVcsNetworkIdType.setStatus("mandatory")


class _ModVcsX121Type_Type(Integer32):
    """Custom type modVcsX121Type based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("dcc", 1),
          ("dnic", 0))
    )


_ModVcsX121Type_Type.__name__ = "Integer32"
_ModVcsX121Type_Object = MibTableColumn
modVcsX121Type = _ModVcsX121Type_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 16, 2, 12, 1, 5),
    _ModVcsX121Type_Type()
)
modVcsX121Type.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modVcsX121Type.setStatus("mandatory")


class _ModVcsNetworkIdCode_Type(DigitString):
    """Custom type modVcsNetworkIdCode based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 4),
    )


_ModVcsNetworkIdCode_Type.__name__ = "DigitString"
_ModVcsNetworkIdCode_Object = MibTableColumn
modVcsNetworkIdCode = _ModVcsNetworkIdCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 16, 2, 12, 1, 6),
    _ModVcsNetworkIdCode_Type()
)
modVcsNetworkIdCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modVcsNetworkIdCode.setStatus("mandatory")


class _ModVcsX121IntlAddresses_Type(Integer32):
    """Custom type modVcsX121IntlAddresses based on Integer32"""
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


_ModVcsX121IntlAddresses_Type.__name__ = "Integer32"
_ModVcsX121IntlAddresses_Object = MibTableColumn
modVcsX121IntlAddresses = _ModVcsX121IntlAddresses_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 16, 2, 12, 1, 7),
    _ModVcsX121IntlAddresses_Type()
)
modVcsX121IntlAddresses.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modVcsX121IntlAddresses.setStatus("mandatory")


class _ModVcsX121IntllPrefixDigit_Type(Unsigned32):
    """Custom type modVcsX121IntllPrefixDigit based on Unsigned32"""
    defaultValue = 9

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_ModVcsX121IntllPrefixDigit_Type.__name__ = "Unsigned32"
_ModVcsX121IntllPrefixDigit_Object = MibTableColumn
modVcsX121IntllPrefixDigit = _ModVcsX121IntllPrefixDigit_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 16, 2, 12, 1, 8),
    _ModVcsX121IntllPrefixDigit_Type()
)
modVcsX121IntllPrefixDigit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modVcsX121IntllPrefixDigit.setStatus("mandatory")


class _ModVcsX121MinAddressLength_Type(Unsigned32):
    """Custom type modVcsX121MinAddressLength based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_ModVcsX121MinAddressLength_Type.__name__ = "Unsigned32"
_ModVcsX121MinAddressLength_Object = MibTableColumn
modVcsX121MinAddressLength = _ModVcsX121MinAddressLength_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 16, 2, 12, 1, 11),
    _ModVcsX121MinAddressLength_Type()
)
modVcsX121MinAddressLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modVcsX121MinAddressLength.setStatus("mandatory")


class _ModVcsX121MaxAddressLength_Type(Unsigned32):
    """Custom type modVcsX121MaxAddressLength based on Unsigned32"""
    defaultValue = 15

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_ModVcsX121MaxAddressLength_Type.__name__ = "Unsigned32"
_ModVcsX121MaxAddressLength_Object = MibTableColumn
modVcsX121MaxAddressLength = _ModVcsX121MaxAddressLength_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 16, 2, 12, 1, 12),
    _ModVcsX121MaxAddressLength_Type()
)
modVcsX121MaxAddressLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modVcsX121MaxAddressLength.setStatus("mandatory")


class _ModVcsX121ToE164EscapeSignificance_Type(Integer32):
    """Custom type modVcsX121ToE164EscapeSignificance based on Integer32"""
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


_ModVcsX121ToE164EscapeSignificance_Type.__name__ = "Integer32"
_ModVcsX121ToE164EscapeSignificance_Object = MibTableColumn
modVcsX121ToE164EscapeSignificance = _ModVcsX121ToE164EscapeSignificance_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 16, 2, 12, 1, 13),
    _ModVcsX121ToE164EscapeSignificance_Type()
)
modVcsX121ToE164EscapeSignificance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modVcsX121ToE164EscapeSignificance.setStatus("mandatory")


class _ModVcsE164IntlFormatAllowed_Type(Integer32):
    """Custom type modVcsE164IntlFormatAllowed based on Integer32"""
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


_ModVcsE164IntlFormatAllowed_Type.__name__ = "Integer32"
_ModVcsE164IntlFormatAllowed_Object = MibTableColumn
modVcsE164IntlFormatAllowed = _ModVcsE164IntlFormatAllowed_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 16, 2, 12, 1, 14),
    _ModVcsE164IntlFormatAllowed_Type()
)
modVcsE164IntlFormatAllowed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modVcsE164IntlFormatAllowed.setStatus("mandatory")


class _ModVcsE164IntlPrefixDigits_Type(DigitString):
    """Custom type modVcsE164IntlPrefixDigits based on DigitString"""
    defaultHexValue = "30"

    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )


_ModVcsE164IntlPrefixDigits_Type.__name__ = "DigitString"
_ModVcsE164IntlPrefixDigits_Object = MibTableColumn
modVcsE164IntlPrefixDigits = _ModVcsE164IntlPrefixDigits_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 16, 2, 12, 1, 15),
    _ModVcsE164IntlPrefixDigits_Type()
)
modVcsE164IntlPrefixDigits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modVcsE164IntlPrefixDigits.setStatus("mandatory")


class _ModVcsE164NatlPrefixDigit_Type(Unsigned32):
    """Custom type modVcsE164NatlPrefixDigit based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_ModVcsE164NatlPrefixDigit_Type.__name__ = "Unsigned32"
_ModVcsE164NatlPrefixDigit_Object = MibTableColumn
modVcsE164NatlPrefixDigit = _ModVcsE164NatlPrefixDigit_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 16, 2, 12, 1, 16),
    _ModVcsE164NatlPrefixDigit_Type()
)
modVcsE164NatlPrefixDigit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modVcsE164NatlPrefixDigit.setStatus("mandatory")


class _ModVcsE164LocalAddressLength_Type(Unsigned32):
    """Custom type modVcsE164LocalAddressLength based on Unsigned32"""
    defaultValue = 7

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 15),
    )


_ModVcsE164LocalAddressLength_Type.__name__ = "Unsigned32"
_ModVcsE164LocalAddressLength_Object = MibTableColumn
modVcsE164LocalAddressLength = _ModVcsE164LocalAddressLength_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 16, 2, 12, 1, 17),
    _ModVcsE164LocalAddressLength_Type()
)
modVcsE164LocalAddressLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modVcsE164LocalAddressLength.setStatus("mandatory")


class _ModVcsE164TeleCountryCode_Type(DigitString):
    """Custom type modVcsE164TeleCountryCode based on DigitString"""
    defaultHexValue = "31"

    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4),
    )


_ModVcsE164TeleCountryCode_Type.__name__ = "DigitString"
_ModVcsE164TeleCountryCode_Object = MibTableColumn
modVcsE164TeleCountryCode = _ModVcsE164TeleCountryCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 16, 2, 12, 1, 18),
    _ModVcsE164TeleCountryCode_Type()
)
modVcsE164TeleCountryCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modVcsE164TeleCountryCode.setStatus("mandatory")


class _ModVcsE164NatlMinAddressLength_Type(Unsigned32):
    """Custom type modVcsE164NatlMinAddressLength based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_ModVcsE164NatlMinAddressLength_Type.__name__ = "Unsigned32"
_ModVcsE164NatlMinAddressLength_Object = MibTableColumn
modVcsE164NatlMinAddressLength = _ModVcsE164NatlMinAddressLength_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 16, 2, 12, 1, 20),
    _ModVcsE164NatlMinAddressLength_Type()
)
modVcsE164NatlMinAddressLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modVcsE164NatlMinAddressLength.setStatus("mandatory")


class _ModVcsE164NatlMaxAddressLength_Type(Unsigned32):
    """Custom type modVcsE164NatlMaxAddressLength based on Unsigned32"""
    defaultValue = 15

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_ModVcsE164NatlMaxAddressLength_Type.__name__ = "Unsigned32"
_ModVcsE164NatlMaxAddressLength_Object = MibTableColumn
modVcsE164NatlMaxAddressLength = _ModVcsE164NatlMaxAddressLength_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 16, 2, 12, 1, 21),
    _ModVcsE164NatlMaxAddressLength_Type()
)
modVcsE164NatlMaxAddressLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modVcsE164NatlMaxAddressLength.setStatus("mandatory")


class _ModVcsE164IntlMinAddressLength_Type(Unsigned32):
    """Custom type modVcsE164IntlMinAddressLength based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_ModVcsE164IntlMinAddressLength_Type.__name__ = "Unsigned32"
_ModVcsE164IntlMinAddressLength_Object = MibTableColumn
modVcsE164IntlMinAddressLength = _ModVcsE164IntlMinAddressLength_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 16, 2, 12, 1, 22),
    _ModVcsE164IntlMinAddressLength_Type()
)
modVcsE164IntlMinAddressLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modVcsE164IntlMinAddressLength.setStatus("mandatory")


class _ModVcsE164IntlMaxAddressLength_Type(Unsigned32):
    """Custom type modVcsE164IntlMaxAddressLength based on Unsigned32"""
    defaultValue = 15

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_ModVcsE164IntlMaxAddressLength_Type.__name__ = "Unsigned32"
_ModVcsE164IntlMaxAddressLength_Object = MibTableColumn
modVcsE164IntlMaxAddressLength = _ModVcsE164IntlMaxAddressLength_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 16, 2, 12, 1, 23),
    _ModVcsE164IntlMaxAddressLength_Type()
)
modVcsE164IntlMaxAddressLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modVcsE164IntlMaxAddressLength.setStatus("mandatory")


class _ModVcsE164LocalMinAddressLength_Type(Unsigned32):
    """Custom type modVcsE164LocalMinAddressLength based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_ModVcsE164LocalMinAddressLength_Type.__name__ = "Unsigned32"
_ModVcsE164LocalMinAddressLength_Object = MibTableColumn
modVcsE164LocalMinAddressLength = _ModVcsE164LocalMinAddressLength_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 16, 2, 12, 1, 24),
    _ModVcsE164LocalMinAddressLength_Type()
)
modVcsE164LocalMinAddressLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modVcsE164LocalMinAddressLength.setStatus("mandatory")


class _ModVcsE164LocalMaxAddressLength_Type(Unsigned32):
    """Custom type modVcsE164LocalMaxAddressLength based on Unsigned32"""
    defaultValue = 15

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_ModVcsE164LocalMaxAddressLength_Type.__name__ = "Unsigned32"
_ModVcsE164LocalMaxAddressLength_Object = MibTableColumn
modVcsE164LocalMaxAddressLength = _ModVcsE164LocalMaxAddressLength_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 16, 2, 12, 1, 25),
    _ModVcsE164LocalMaxAddressLength_Type()
)
modVcsE164LocalMaxAddressLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modVcsE164LocalMaxAddressLength.setStatus("mandatory")
_ModVcsIntOptTable_Object = MibTable
modVcsIntOptTable = _ModVcsIntOptTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 16, 2, 13)
)
if mibBuilder.loadTexts:
    modVcsIntOptTable.setStatus("mandatory")
_ModVcsIntOptEntry_Object = MibTableRow
modVcsIntOptEntry = _ModVcsIntOptEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 16, 2, 13, 1)
)
modVcsIntOptEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-ShelfMIB", "modIndex"),
    (0, "Nortel-Magellan-Passport-SubnetInterfaceMIB", "modVcsIndex"),
)
if mibBuilder.loadTexts:
    modVcsIntOptEntry.setStatus("mandatory")


class _ModVcsHighPriorityPacketSizes_Type(OctetString):
    """Custom type modVcsHighPriorityPacketSizes based on OctetString"""
    defaultHexValue = "ff80"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_ModVcsHighPriorityPacketSizes_Type.__name__ = "OctetString"
_ModVcsHighPriorityPacketSizes_Object = MibTableColumn
modVcsHighPriorityPacketSizes = _ModVcsHighPriorityPacketSizes_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 16, 2, 13, 1, 1),
    _ModVcsHighPriorityPacketSizes_Type()
)
modVcsHighPriorityPacketSizes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modVcsHighPriorityPacketSizes.setStatus("mandatory")


class _ModVcsMaxSubnetPacketSize_Type(Integer32):
    """Custom type modVcsMaxSubnetPacketSize based on Integer32"""
    defaultValue = 9

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


_ModVcsMaxSubnetPacketSize_Type.__name__ = "Integer32"
_ModVcsMaxSubnetPacketSize_Object = MibTableColumn
modVcsMaxSubnetPacketSize = _ModVcsMaxSubnetPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 16, 2, 13, 1, 2),
    _ModVcsMaxSubnetPacketSize_Type()
)
modVcsMaxSubnetPacketSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modVcsMaxSubnetPacketSize.setStatus("mandatory")


class _ModVcsCallSetupTimer_Type(Unsigned32):
    """Custom type modVcsCallSetupTimer based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 100),
    )


_ModVcsCallSetupTimer_Type.__name__ = "Unsigned32"
_ModVcsCallSetupTimer_Object = MibTableColumn
modVcsCallSetupTimer = _ModVcsCallSetupTimer_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 16, 2, 13, 1, 3),
    _ModVcsCallSetupTimer_Type()
)
modVcsCallSetupTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modVcsCallSetupTimer.setStatus("mandatory")


class _ModVcsCallRetryTimer_Type(Unsigned32):
    """Custom type modVcsCallRetryTimer based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 300),
    )


_ModVcsCallRetryTimer_Type.__name__ = "Unsigned32"
_ModVcsCallRetryTimer_Object = MibTableColumn
modVcsCallRetryTimer = _ModVcsCallRetryTimer_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 16, 2, 13, 1, 4),
    _ModVcsCallRetryTimer_Type()
)
modVcsCallRetryTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modVcsCallRetryTimer.setStatus("mandatory")


class _ModVcsDelaySubnetAcks_Type(Integer32):
    """Custom type modVcsDelaySubnetAcks based on Integer32"""
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


_ModVcsDelaySubnetAcks_Type.__name__ = "Integer32"
_ModVcsDelaySubnetAcks_Object = MibTableColumn
modVcsDelaySubnetAcks = _ModVcsDelaySubnetAcks_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 16, 2, 13, 1, 5),
    _ModVcsDelaySubnetAcks_Type()
)
modVcsDelaySubnetAcks.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modVcsDelaySubnetAcks.setStatus("mandatory")
_ModVcsWinsTable_Object = MibTable
modVcsWinsTable = _ModVcsWinsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 16, 2, 213)
)
if mibBuilder.loadTexts:
    modVcsWinsTable.setStatus("mandatory")
_ModVcsWinsEntry_Object = MibTableRow
modVcsWinsEntry = _ModVcsWinsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 16, 2, 213, 1)
)
modVcsWinsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-ShelfMIB", "modIndex"),
    (0, "Nortel-Magellan-Passport-SubnetInterfaceMIB", "modVcsIndex"),
    (0, "Nortel-Magellan-Passport-SubnetInterfaceMIB", "modVcsWinsPktIndex"),
    (0, "Nortel-Magellan-Passport-SubnetInterfaceMIB", "modVcsWinsTptIndex"),
)
if mibBuilder.loadTexts:
    modVcsWinsEntry.setStatus("mandatory")


class _ModVcsWinsPktIndex_Type(Integer32):
    """Custom type modVcsWinsPktIndex based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("n1024", 6),
          ("n128", 3),
          ("n16", 0),
          ("n2048", 7),
          ("n256", 4),
          ("n32", 1),
          ("n32768", 10),
          ("n4096", 8),
          ("n512", 5),
          ("n64", 2),
          ("n65535", 11),
          ("n8192", 9))
    )


_ModVcsWinsPktIndex_Type.__name__ = "Integer32"
_ModVcsWinsPktIndex_Object = MibTableColumn
modVcsWinsPktIndex = _ModVcsWinsPktIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 16, 2, 213, 1, 1),
    _ModVcsWinsPktIndex_Type()
)
modVcsWinsPktIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    modVcsWinsPktIndex.setStatus("mandatory")


class _ModVcsWinsTptIndex_Type(Integer32):
    """Custom type modVcsWinsTptIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_ModVcsWinsTptIndex_Type.__name__ = "Integer32"
_ModVcsWinsTptIndex_Object = MibTableColumn
modVcsWinsTptIndex = _ModVcsWinsTptIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 16, 2, 213, 1, 2),
    _ModVcsWinsTptIndex_Type()
)
modVcsWinsTptIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    modVcsWinsTptIndex.setStatus("mandatory")


class _ModVcsWinsValue_Type(Unsigned32):
    """Custom type modVcsWinsValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 63),
    )


_ModVcsWinsValue_Type.__name__ = "Unsigned32"
_ModVcsWinsValue_Object = MibTableColumn
modVcsWinsValue = _ModVcsWinsValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 16, 2, 213, 1, 3),
    _ModVcsWinsValue_Type()
)
modVcsWinsValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modVcsWinsValue.setStatus("mandatory")
_SubnetInterfaceMIB_ObjectIdentity = ObjectIdentity
subnetInterfaceMIB = _SubnetInterfaceMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 45)
)
_SubnetInterfaceGroup_ObjectIdentity = ObjectIdentity
subnetInterfaceGroup = _SubnetInterfaceGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 45, 1)
)
_SubnetInterfaceGroupBE_ObjectIdentity = ObjectIdentity
subnetInterfaceGroupBE = _SubnetInterfaceGroupBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 45, 1, 5)
)
_SubnetInterfaceGroupBE00_ObjectIdentity = ObjectIdentity
subnetInterfaceGroupBE00 = _SubnetInterfaceGroupBE00_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 45, 1, 5, 1)
)
_SubnetInterfaceGroupBE00A_ObjectIdentity = ObjectIdentity
subnetInterfaceGroupBE00A = _SubnetInterfaceGroupBE00A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 45, 1, 5, 1, 2)
)
_SubnetInterfaceCapabilities_ObjectIdentity = ObjectIdentity
subnetInterfaceCapabilities = _SubnetInterfaceCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 45, 3)
)
_SubnetInterfaceCapabilitiesBE_ObjectIdentity = ObjectIdentity
subnetInterfaceCapabilitiesBE = _SubnetInterfaceCapabilitiesBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 45, 3, 5)
)
_SubnetInterfaceCapabilitiesBE00_ObjectIdentity = ObjectIdentity
subnetInterfaceCapabilitiesBE00 = _SubnetInterfaceCapabilitiesBE00_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 45, 3, 5, 1)
)
_SubnetInterfaceCapabilitiesBE00A_ObjectIdentity = ObjectIdentity
subnetInterfaceCapabilitiesBE00A = _SubnetInterfaceCapabilitiesBE00A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 45, 3, 5, 1, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-Magellan-Passport-SubnetInterfaceMIB",
    **{"modVcs": modVcs,
       "modVcsRowStatusTable": modVcsRowStatusTable,
       "modVcsRowStatusEntry": modVcsRowStatusEntry,
       "modVcsRowStatus": modVcsRowStatus,
       "modVcsComponentName": modVcsComponentName,
       "modVcsStorageType": modVcsStorageType,
       "modVcsIndex": modVcsIndex,
       "modVcsAccOptTable": modVcsAccOptTable,
       "modVcsAccOptEntry": modVcsAccOptEntry,
       "modVcsSegmentSize": modVcsSegmentSize,
       "modVcsUnitsCounted": modVcsUnitsCounted,
       "modVcsAccountingFax": modVcsAccountingFax,
       "modVcsGenerationMode": modVcsGenerationMode,
       "modVcsAddOptTable": modVcsAddOptTable,
       "modVcsAddOptEntry": modVcsAddOptEntry,
       "modVcsDefaultNumberingPlan": modVcsDefaultNumberingPlan,
       "modVcsNetworkIdType": modVcsNetworkIdType,
       "modVcsX121Type": modVcsX121Type,
       "modVcsNetworkIdCode": modVcsNetworkIdCode,
       "modVcsX121IntlAddresses": modVcsX121IntlAddresses,
       "modVcsX121IntllPrefixDigit": modVcsX121IntllPrefixDigit,
       "modVcsX121MinAddressLength": modVcsX121MinAddressLength,
       "modVcsX121MaxAddressLength": modVcsX121MaxAddressLength,
       "modVcsX121ToE164EscapeSignificance": modVcsX121ToE164EscapeSignificance,
       "modVcsE164IntlFormatAllowed": modVcsE164IntlFormatAllowed,
       "modVcsE164IntlPrefixDigits": modVcsE164IntlPrefixDigits,
       "modVcsE164NatlPrefixDigit": modVcsE164NatlPrefixDigit,
       "modVcsE164LocalAddressLength": modVcsE164LocalAddressLength,
       "modVcsE164TeleCountryCode": modVcsE164TeleCountryCode,
       "modVcsE164NatlMinAddressLength": modVcsE164NatlMinAddressLength,
       "modVcsE164NatlMaxAddressLength": modVcsE164NatlMaxAddressLength,
       "modVcsE164IntlMinAddressLength": modVcsE164IntlMinAddressLength,
       "modVcsE164IntlMaxAddressLength": modVcsE164IntlMaxAddressLength,
       "modVcsE164LocalMinAddressLength": modVcsE164LocalMinAddressLength,
       "modVcsE164LocalMaxAddressLength": modVcsE164LocalMaxAddressLength,
       "modVcsIntOptTable": modVcsIntOptTable,
       "modVcsIntOptEntry": modVcsIntOptEntry,
       "modVcsHighPriorityPacketSizes": modVcsHighPriorityPacketSizes,
       "modVcsMaxSubnetPacketSize": modVcsMaxSubnetPacketSize,
       "modVcsCallSetupTimer": modVcsCallSetupTimer,
       "modVcsCallRetryTimer": modVcsCallRetryTimer,
       "modVcsDelaySubnetAcks": modVcsDelaySubnetAcks,
       "modVcsWinsTable": modVcsWinsTable,
       "modVcsWinsEntry": modVcsWinsEntry,
       "modVcsWinsPktIndex": modVcsWinsPktIndex,
       "modVcsWinsTptIndex": modVcsWinsTptIndex,
       "modVcsWinsValue": modVcsWinsValue,
       "subnetInterfaceMIB": subnetInterfaceMIB,
       "subnetInterfaceGroup": subnetInterfaceGroup,
       "subnetInterfaceGroupBE": subnetInterfaceGroupBE,
       "subnetInterfaceGroupBE00": subnetInterfaceGroupBE00,
       "subnetInterfaceGroupBE00A": subnetInterfaceGroupBE00A,
       "subnetInterfaceCapabilities": subnetInterfaceCapabilities,
       "subnetInterfaceCapabilitiesBE": subnetInterfaceCapabilitiesBE,
       "subnetInterfaceCapabilitiesBE00": subnetInterfaceCapabilitiesBE00,
       "subnetInterfaceCapabilitiesBE00A": subnetInterfaceCapabilitiesBE00A}
)
