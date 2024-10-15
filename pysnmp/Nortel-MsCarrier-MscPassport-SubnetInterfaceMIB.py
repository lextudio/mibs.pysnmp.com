# SNMP MIB module (Nortel-MsCarrier-MscPassport-SubnetInterfaceMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-MsCarrier-MscPassport-SubnetInterfaceMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:33:06 2024
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

(mscMod,
 mscModIndex) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-BaseShelfMIB",
    "mscMod",
    "mscModIndex")

(DisplayString,
 Integer32,
 RowStatus,
 StorageType,
 Unsigned32) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-StandardTextualConventionsMIB",
    "DisplayString",
    "Integer32",
    "RowStatus",
    "StorageType",
    "Unsigned32")

(DigitString,
 NonReplicated) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-TextualConventionsMIB",
    "DigitString",
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

_MscModVcs_ObjectIdentity = ObjectIdentity
mscModVcs = _MscModVcs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 2)
)
_MscModVcsRowStatusTable_Object = MibTable
mscModVcsRowStatusTable = _MscModVcsRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 2, 1)
)
if mibBuilder.loadTexts:
    mscModVcsRowStatusTable.setStatus("mandatory")
_MscModVcsRowStatusEntry_Object = MibTableRow
mscModVcsRowStatusEntry = _MscModVcsRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 2, 1, 1)
)
mscModVcsRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscModIndex"),
    (0, "Nortel-MsCarrier-MscPassport-SubnetInterfaceMIB", "mscModVcsIndex"),
)
if mibBuilder.loadTexts:
    mscModVcsRowStatusEntry.setStatus("mandatory")
_MscModVcsRowStatus_Type = RowStatus
_MscModVcsRowStatus_Object = MibTableColumn
mscModVcsRowStatus = _MscModVcsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 2, 1, 1, 1),
    _MscModVcsRowStatus_Type()
)
mscModVcsRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscModVcsRowStatus.setStatus("mandatory")
_MscModVcsComponentName_Type = DisplayString
_MscModVcsComponentName_Object = MibTableColumn
mscModVcsComponentName = _MscModVcsComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 2, 1, 1, 2),
    _MscModVcsComponentName_Type()
)
mscModVcsComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscModVcsComponentName.setStatus("mandatory")
_MscModVcsStorageType_Type = StorageType
_MscModVcsStorageType_Object = MibTableColumn
mscModVcsStorageType = _MscModVcsStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 2, 1, 1, 4),
    _MscModVcsStorageType_Type()
)
mscModVcsStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscModVcsStorageType.setStatus("mandatory")
_MscModVcsIndex_Type = NonReplicated
_MscModVcsIndex_Object = MibTableColumn
mscModVcsIndex = _MscModVcsIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 2, 1, 1, 10),
    _MscModVcsIndex_Type()
)
mscModVcsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscModVcsIndex.setStatus("mandatory")
_MscModVcsAccOptTable_Object = MibTable
mscModVcsAccOptTable = _MscModVcsAccOptTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 2, 10)
)
if mibBuilder.loadTexts:
    mscModVcsAccOptTable.setStatus("mandatory")
_MscModVcsAccOptEntry_Object = MibTableRow
mscModVcsAccOptEntry = _MscModVcsAccOptEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 2, 10, 1)
)
mscModVcsAccOptEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscModIndex"),
    (0, "Nortel-MsCarrier-MscPassport-SubnetInterfaceMIB", "mscModVcsIndex"),
)
if mibBuilder.loadTexts:
    mscModVcsAccOptEntry.setStatus("mandatory")


class _MscModVcsSegmentSize_Type(Integer32):
    """Custom type mscModVcsSegmentSize based on Integer32"""
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


_MscModVcsSegmentSize_Type.__name__ = "Integer32"
_MscModVcsSegmentSize_Object = MibTableColumn
mscModVcsSegmentSize = _MscModVcsSegmentSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 2, 10, 1, 1),
    _MscModVcsSegmentSize_Type()
)
mscModVcsSegmentSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscModVcsSegmentSize.setStatus("mandatory")


class _MscModVcsUnitsCounted_Type(Integer32):
    """Custom type mscModVcsUnitsCounted based on Integer32"""
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


_MscModVcsUnitsCounted_Type.__name__ = "Integer32"
_MscModVcsUnitsCounted_Object = MibTableColumn
mscModVcsUnitsCounted = _MscModVcsUnitsCounted_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 2, 10, 1, 2),
    _MscModVcsUnitsCounted_Type()
)
mscModVcsUnitsCounted.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscModVcsUnitsCounted.setStatus("mandatory")


class _MscModVcsAccountingFax_Type(OctetString):
    """Custom type mscModVcsAccountingFax based on OctetString"""
    defaultHexValue = "20"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscModVcsAccountingFax_Type.__name__ = "OctetString"
_MscModVcsAccountingFax_Object = MibTableColumn
mscModVcsAccountingFax = _MscModVcsAccountingFax_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 2, 10, 1, 3),
    _MscModVcsAccountingFax_Type()
)
mscModVcsAccountingFax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscModVcsAccountingFax.setStatus("mandatory")


class _MscModVcsGenerationMode_Type(Integer32):
    """Custom type mscModVcsGenerationMode based on Integer32"""
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


_MscModVcsGenerationMode_Type.__name__ = "Integer32"
_MscModVcsGenerationMode_Object = MibTableColumn
mscModVcsGenerationMode = _MscModVcsGenerationMode_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 2, 10, 1, 4),
    _MscModVcsGenerationMode_Type()
)
mscModVcsGenerationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscModVcsGenerationMode.setStatus("mandatory")
_MscModVcsAddOptTable_Object = MibTable
mscModVcsAddOptTable = _MscModVcsAddOptTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 2, 12)
)
if mibBuilder.loadTexts:
    mscModVcsAddOptTable.setStatus("mandatory")
_MscModVcsAddOptEntry_Object = MibTableRow
mscModVcsAddOptEntry = _MscModVcsAddOptEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 2, 12, 1)
)
mscModVcsAddOptEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscModIndex"),
    (0, "Nortel-MsCarrier-MscPassport-SubnetInterfaceMIB", "mscModVcsIndex"),
)
if mibBuilder.loadTexts:
    mscModVcsAddOptEntry.setStatus("mandatory")


class _MscModVcsDefaultNumberingPlan_Type(Integer32):
    """Custom type mscModVcsDefaultNumberingPlan based on Integer32"""
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


_MscModVcsDefaultNumberingPlan_Type.__name__ = "Integer32"
_MscModVcsDefaultNumberingPlan_Object = MibTableColumn
mscModVcsDefaultNumberingPlan = _MscModVcsDefaultNumberingPlan_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 2, 12, 1, 3),
    _MscModVcsDefaultNumberingPlan_Type()
)
mscModVcsDefaultNumberingPlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscModVcsDefaultNumberingPlan.setStatus("mandatory")


class _MscModVcsNetworkIdType_Type(Integer32):
    """Custom type mscModVcsNetworkIdType based on Integer32"""
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


_MscModVcsNetworkIdType_Type.__name__ = "Integer32"
_MscModVcsNetworkIdType_Object = MibTableColumn
mscModVcsNetworkIdType = _MscModVcsNetworkIdType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 2, 12, 1, 4),
    _MscModVcsNetworkIdType_Type()
)
mscModVcsNetworkIdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscModVcsNetworkIdType.setStatus("mandatory")


class _MscModVcsX121Type_Type(Integer32):
    """Custom type mscModVcsX121Type based on Integer32"""
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


_MscModVcsX121Type_Type.__name__ = "Integer32"
_MscModVcsX121Type_Object = MibTableColumn
mscModVcsX121Type = _MscModVcsX121Type_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 2, 12, 1, 5),
    _MscModVcsX121Type_Type()
)
mscModVcsX121Type.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscModVcsX121Type.setStatus("mandatory")


class _MscModVcsNetworkIdCode_Type(DigitString):
    """Custom type mscModVcsNetworkIdCode based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 4),
    )


_MscModVcsNetworkIdCode_Type.__name__ = "DigitString"
_MscModVcsNetworkIdCode_Object = MibTableColumn
mscModVcsNetworkIdCode = _MscModVcsNetworkIdCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 2, 12, 1, 6),
    _MscModVcsNetworkIdCode_Type()
)
mscModVcsNetworkIdCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscModVcsNetworkIdCode.setStatus("mandatory")


class _MscModVcsX121IntlAddresses_Type(Integer32):
    """Custom type mscModVcsX121IntlAddresses based on Integer32"""
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


_MscModVcsX121IntlAddresses_Type.__name__ = "Integer32"
_MscModVcsX121IntlAddresses_Object = MibTableColumn
mscModVcsX121IntlAddresses = _MscModVcsX121IntlAddresses_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 2, 12, 1, 7),
    _MscModVcsX121IntlAddresses_Type()
)
mscModVcsX121IntlAddresses.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscModVcsX121IntlAddresses.setStatus("mandatory")


class _MscModVcsX121IntllPrefixDigit_Type(Unsigned32):
    """Custom type mscModVcsX121IntllPrefixDigit based on Unsigned32"""
    defaultValue = 9

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_MscModVcsX121IntllPrefixDigit_Type.__name__ = "Unsigned32"
_MscModVcsX121IntllPrefixDigit_Object = MibTableColumn
mscModVcsX121IntllPrefixDigit = _MscModVcsX121IntllPrefixDigit_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 2, 12, 1, 8),
    _MscModVcsX121IntllPrefixDigit_Type()
)
mscModVcsX121IntllPrefixDigit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscModVcsX121IntllPrefixDigit.setStatus("mandatory")


class _MscModVcsX121MinAddressLength_Type(Unsigned32):
    """Custom type mscModVcsX121MinAddressLength based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_MscModVcsX121MinAddressLength_Type.__name__ = "Unsigned32"
_MscModVcsX121MinAddressLength_Object = MibTableColumn
mscModVcsX121MinAddressLength = _MscModVcsX121MinAddressLength_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 2, 12, 1, 11),
    _MscModVcsX121MinAddressLength_Type()
)
mscModVcsX121MinAddressLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscModVcsX121MinAddressLength.setStatus("mandatory")


class _MscModVcsX121MaxAddressLength_Type(Unsigned32):
    """Custom type mscModVcsX121MaxAddressLength based on Unsigned32"""
    defaultValue = 15

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_MscModVcsX121MaxAddressLength_Type.__name__ = "Unsigned32"
_MscModVcsX121MaxAddressLength_Object = MibTableColumn
mscModVcsX121MaxAddressLength = _MscModVcsX121MaxAddressLength_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 2, 12, 1, 12),
    _MscModVcsX121MaxAddressLength_Type()
)
mscModVcsX121MaxAddressLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscModVcsX121MaxAddressLength.setStatus("mandatory")


class _MscModVcsX121ToE164EscapeSignificance_Type(Integer32):
    """Custom type mscModVcsX121ToE164EscapeSignificance based on Integer32"""
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


_MscModVcsX121ToE164EscapeSignificance_Type.__name__ = "Integer32"
_MscModVcsX121ToE164EscapeSignificance_Object = MibTableColumn
mscModVcsX121ToE164EscapeSignificance = _MscModVcsX121ToE164EscapeSignificance_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 2, 12, 1, 13),
    _MscModVcsX121ToE164EscapeSignificance_Type()
)
mscModVcsX121ToE164EscapeSignificance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscModVcsX121ToE164EscapeSignificance.setStatus("mandatory")


class _MscModVcsE164IntlFormatAllowed_Type(Integer32):
    """Custom type mscModVcsE164IntlFormatAllowed based on Integer32"""
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


_MscModVcsE164IntlFormatAllowed_Type.__name__ = "Integer32"
_MscModVcsE164IntlFormatAllowed_Object = MibTableColumn
mscModVcsE164IntlFormatAllowed = _MscModVcsE164IntlFormatAllowed_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 2, 12, 1, 14),
    _MscModVcsE164IntlFormatAllowed_Type()
)
mscModVcsE164IntlFormatAllowed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscModVcsE164IntlFormatAllowed.setStatus("mandatory")


class _MscModVcsE164IntlPrefixDigits_Type(DigitString):
    """Custom type mscModVcsE164IntlPrefixDigits based on DigitString"""
    defaultHexValue = "30"

    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )


_MscModVcsE164IntlPrefixDigits_Type.__name__ = "DigitString"
_MscModVcsE164IntlPrefixDigits_Object = MibTableColumn
mscModVcsE164IntlPrefixDigits = _MscModVcsE164IntlPrefixDigits_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 2, 12, 1, 15),
    _MscModVcsE164IntlPrefixDigits_Type()
)
mscModVcsE164IntlPrefixDigits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscModVcsE164IntlPrefixDigits.setStatus("mandatory")


class _MscModVcsE164NatlPrefixDigit_Type(Unsigned32):
    """Custom type mscModVcsE164NatlPrefixDigit based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_MscModVcsE164NatlPrefixDigit_Type.__name__ = "Unsigned32"
_MscModVcsE164NatlPrefixDigit_Object = MibTableColumn
mscModVcsE164NatlPrefixDigit = _MscModVcsE164NatlPrefixDigit_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 2, 12, 1, 16),
    _MscModVcsE164NatlPrefixDigit_Type()
)
mscModVcsE164NatlPrefixDigit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscModVcsE164NatlPrefixDigit.setStatus("mandatory")


class _MscModVcsE164LocalAddressLength_Type(Unsigned32):
    """Custom type mscModVcsE164LocalAddressLength based on Unsigned32"""
    defaultValue = 7

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 15),
    )


_MscModVcsE164LocalAddressLength_Type.__name__ = "Unsigned32"
_MscModVcsE164LocalAddressLength_Object = MibTableColumn
mscModVcsE164LocalAddressLength = _MscModVcsE164LocalAddressLength_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 2, 12, 1, 17),
    _MscModVcsE164LocalAddressLength_Type()
)
mscModVcsE164LocalAddressLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscModVcsE164LocalAddressLength.setStatus("mandatory")


class _MscModVcsE164TeleCountryCode_Type(DigitString):
    """Custom type mscModVcsE164TeleCountryCode based on DigitString"""
    defaultHexValue = "31"

    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4),
    )


_MscModVcsE164TeleCountryCode_Type.__name__ = "DigitString"
_MscModVcsE164TeleCountryCode_Object = MibTableColumn
mscModVcsE164TeleCountryCode = _MscModVcsE164TeleCountryCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 2, 12, 1, 18),
    _MscModVcsE164TeleCountryCode_Type()
)
mscModVcsE164TeleCountryCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscModVcsE164TeleCountryCode.setStatus("mandatory")


class _MscModVcsE164NatlMinAddressLength_Type(Unsigned32):
    """Custom type mscModVcsE164NatlMinAddressLength based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_MscModVcsE164NatlMinAddressLength_Type.__name__ = "Unsigned32"
_MscModVcsE164NatlMinAddressLength_Object = MibTableColumn
mscModVcsE164NatlMinAddressLength = _MscModVcsE164NatlMinAddressLength_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 2, 12, 1, 20),
    _MscModVcsE164NatlMinAddressLength_Type()
)
mscModVcsE164NatlMinAddressLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscModVcsE164NatlMinAddressLength.setStatus("mandatory")


class _MscModVcsE164NatlMaxAddressLength_Type(Unsigned32):
    """Custom type mscModVcsE164NatlMaxAddressLength based on Unsigned32"""
    defaultValue = 15

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_MscModVcsE164NatlMaxAddressLength_Type.__name__ = "Unsigned32"
_MscModVcsE164NatlMaxAddressLength_Object = MibTableColumn
mscModVcsE164NatlMaxAddressLength = _MscModVcsE164NatlMaxAddressLength_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 2, 12, 1, 21),
    _MscModVcsE164NatlMaxAddressLength_Type()
)
mscModVcsE164NatlMaxAddressLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscModVcsE164NatlMaxAddressLength.setStatus("mandatory")


class _MscModVcsE164IntlMinAddressLength_Type(Unsigned32):
    """Custom type mscModVcsE164IntlMinAddressLength based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_MscModVcsE164IntlMinAddressLength_Type.__name__ = "Unsigned32"
_MscModVcsE164IntlMinAddressLength_Object = MibTableColumn
mscModVcsE164IntlMinAddressLength = _MscModVcsE164IntlMinAddressLength_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 2, 12, 1, 22),
    _MscModVcsE164IntlMinAddressLength_Type()
)
mscModVcsE164IntlMinAddressLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscModVcsE164IntlMinAddressLength.setStatus("mandatory")


class _MscModVcsE164IntlMaxAddressLength_Type(Unsigned32):
    """Custom type mscModVcsE164IntlMaxAddressLength based on Unsigned32"""
    defaultValue = 15

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_MscModVcsE164IntlMaxAddressLength_Type.__name__ = "Unsigned32"
_MscModVcsE164IntlMaxAddressLength_Object = MibTableColumn
mscModVcsE164IntlMaxAddressLength = _MscModVcsE164IntlMaxAddressLength_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 2, 12, 1, 23),
    _MscModVcsE164IntlMaxAddressLength_Type()
)
mscModVcsE164IntlMaxAddressLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscModVcsE164IntlMaxAddressLength.setStatus("mandatory")


class _MscModVcsE164LocalMinAddressLength_Type(Unsigned32):
    """Custom type mscModVcsE164LocalMinAddressLength based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_MscModVcsE164LocalMinAddressLength_Type.__name__ = "Unsigned32"
_MscModVcsE164LocalMinAddressLength_Object = MibTableColumn
mscModVcsE164LocalMinAddressLength = _MscModVcsE164LocalMinAddressLength_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 2, 12, 1, 24),
    _MscModVcsE164LocalMinAddressLength_Type()
)
mscModVcsE164LocalMinAddressLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscModVcsE164LocalMinAddressLength.setStatus("mandatory")


class _MscModVcsE164LocalMaxAddressLength_Type(Unsigned32):
    """Custom type mscModVcsE164LocalMaxAddressLength based on Unsigned32"""
    defaultValue = 15

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_MscModVcsE164LocalMaxAddressLength_Type.__name__ = "Unsigned32"
_MscModVcsE164LocalMaxAddressLength_Object = MibTableColumn
mscModVcsE164LocalMaxAddressLength = _MscModVcsE164LocalMaxAddressLength_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 2, 12, 1, 25),
    _MscModVcsE164LocalMaxAddressLength_Type()
)
mscModVcsE164LocalMaxAddressLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscModVcsE164LocalMaxAddressLength.setStatus("mandatory")
_MscModVcsIntOptTable_Object = MibTable
mscModVcsIntOptTable = _MscModVcsIntOptTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 2, 13)
)
if mibBuilder.loadTexts:
    mscModVcsIntOptTable.setStatus("mandatory")
_MscModVcsIntOptEntry_Object = MibTableRow
mscModVcsIntOptEntry = _MscModVcsIntOptEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 2, 13, 1)
)
mscModVcsIntOptEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscModIndex"),
    (0, "Nortel-MsCarrier-MscPassport-SubnetInterfaceMIB", "mscModVcsIndex"),
)
if mibBuilder.loadTexts:
    mscModVcsIntOptEntry.setStatus("mandatory")


class _MscModVcsHighPriorityPacketSizes_Type(OctetString):
    """Custom type mscModVcsHighPriorityPacketSizes based on OctetString"""
    defaultHexValue = "ff80"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_MscModVcsHighPriorityPacketSizes_Type.__name__ = "OctetString"
_MscModVcsHighPriorityPacketSizes_Object = MibTableColumn
mscModVcsHighPriorityPacketSizes = _MscModVcsHighPriorityPacketSizes_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 2, 13, 1, 1),
    _MscModVcsHighPriorityPacketSizes_Type()
)
mscModVcsHighPriorityPacketSizes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscModVcsHighPriorityPacketSizes.setStatus("mandatory")


class _MscModVcsMaxSubnetPacketSize_Type(Integer32):
    """Custom type mscModVcsMaxSubnetPacketSize based on Integer32"""
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


_MscModVcsMaxSubnetPacketSize_Type.__name__ = "Integer32"
_MscModVcsMaxSubnetPacketSize_Object = MibTableColumn
mscModVcsMaxSubnetPacketSize = _MscModVcsMaxSubnetPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 2, 13, 1, 2),
    _MscModVcsMaxSubnetPacketSize_Type()
)
mscModVcsMaxSubnetPacketSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscModVcsMaxSubnetPacketSize.setStatus("mandatory")


class _MscModVcsCallSetupTimer_Type(Unsigned32):
    """Custom type mscModVcsCallSetupTimer based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 100),
    )


_MscModVcsCallSetupTimer_Type.__name__ = "Unsigned32"
_MscModVcsCallSetupTimer_Object = MibTableColumn
mscModVcsCallSetupTimer = _MscModVcsCallSetupTimer_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 2, 13, 1, 3),
    _MscModVcsCallSetupTimer_Type()
)
mscModVcsCallSetupTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscModVcsCallSetupTimer.setStatus("mandatory")


class _MscModVcsCallRetryTimer_Type(Unsigned32):
    """Custom type mscModVcsCallRetryTimer based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 300),
    )


_MscModVcsCallRetryTimer_Type.__name__ = "Unsigned32"
_MscModVcsCallRetryTimer_Object = MibTableColumn
mscModVcsCallRetryTimer = _MscModVcsCallRetryTimer_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 2, 13, 1, 4),
    _MscModVcsCallRetryTimer_Type()
)
mscModVcsCallRetryTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscModVcsCallRetryTimer.setStatus("mandatory")


class _MscModVcsDelaySubnetAcks_Type(Integer32):
    """Custom type mscModVcsDelaySubnetAcks based on Integer32"""
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


_MscModVcsDelaySubnetAcks_Type.__name__ = "Integer32"
_MscModVcsDelaySubnetAcks_Object = MibTableColumn
mscModVcsDelaySubnetAcks = _MscModVcsDelaySubnetAcks_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 2, 13, 1, 5),
    _MscModVcsDelaySubnetAcks_Type()
)
mscModVcsDelaySubnetAcks.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscModVcsDelaySubnetAcks.setStatus("mandatory")
_MscModVcsWinsTable_Object = MibTable
mscModVcsWinsTable = _MscModVcsWinsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 2, 213)
)
if mibBuilder.loadTexts:
    mscModVcsWinsTable.setStatus("mandatory")
_MscModVcsWinsEntry_Object = MibTableRow
mscModVcsWinsEntry = _MscModVcsWinsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 2, 213, 1)
)
mscModVcsWinsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscModIndex"),
    (0, "Nortel-MsCarrier-MscPassport-SubnetInterfaceMIB", "mscModVcsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-SubnetInterfaceMIB", "mscModVcsWinsPktIndex"),
    (0, "Nortel-MsCarrier-MscPassport-SubnetInterfaceMIB", "mscModVcsWinsTptIndex"),
)
if mibBuilder.loadTexts:
    mscModVcsWinsEntry.setStatus("mandatory")


class _MscModVcsWinsPktIndex_Type(Integer32):
    """Custom type mscModVcsWinsPktIndex based on Integer32"""
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


_MscModVcsWinsPktIndex_Type.__name__ = "Integer32"
_MscModVcsWinsPktIndex_Object = MibTableColumn
mscModVcsWinsPktIndex = _MscModVcsWinsPktIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 2, 213, 1, 1),
    _MscModVcsWinsPktIndex_Type()
)
mscModVcsWinsPktIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscModVcsWinsPktIndex.setStatus("mandatory")


class _MscModVcsWinsTptIndex_Type(Integer32):
    """Custom type mscModVcsWinsTptIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_MscModVcsWinsTptIndex_Type.__name__ = "Integer32"
_MscModVcsWinsTptIndex_Object = MibTableColumn
mscModVcsWinsTptIndex = _MscModVcsWinsTptIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 2, 213, 1, 2),
    _MscModVcsWinsTptIndex_Type()
)
mscModVcsWinsTptIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscModVcsWinsTptIndex.setStatus("mandatory")


class _MscModVcsWinsValue_Type(Unsigned32):
    """Custom type mscModVcsWinsValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 63),
    )


_MscModVcsWinsValue_Type.__name__ = "Unsigned32"
_MscModVcsWinsValue_Object = MibTableColumn
mscModVcsWinsValue = _MscModVcsWinsValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 2, 213, 1, 3),
    _MscModVcsWinsValue_Type()
)
mscModVcsWinsValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscModVcsWinsValue.setStatus("mandatory")
_SubnetInterfaceMIB_ObjectIdentity = ObjectIdentity
subnetInterfaceMIB = _SubnetInterfaceMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 45)
)
_SubnetInterfaceGroup_ObjectIdentity = ObjectIdentity
subnetInterfaceGroup = _SubnetInterfaceGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 45, 1)
)
_SubnetInterfaceGroupCA_ObjectIdentity = ObjectIdentity
subnetInterfaceGroupCA = _SubnetInterfaceGroupCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 45, 1, 1)
)
_SubnetInterfaceGroupCA02_ObjectIdentity = ObjectIdentity
subnetInterfaceGroupCA02 = _SubnetInterfaceGroupCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 45, 1, 1, 3)
)
_SubnetInterfaceGroupCA02A_ObjectIdentity = ObjectIdentity
subnetInterfaceGroupCA02A = _SubnetInterfaceGroupCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 45, 1, 1, 3, 2)
)
_SubnetInterfaceCapabilities_ObjectIdentity = ObjectIdentity
subnetInterfaceCapabilities = _SubnetInterfaceCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 45, 3)
)
_SubnetInterfaceCapabilitiesCA_ObjectIdentity = ObjectIdentity
subnetInterfaceCapabilitiesCA = _SubnetInterfaceCapabilitiesCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 45, 3, 1)
)
_SubnetInterfaceCapabilitiesCA02_ObjectIdentity = ObjectIdentity
subnetInterfaceCapabilitiesCA02 = _SubnetInterfaceCapabilitiesCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 45, 3, 1, 3)
)
_SubnetInterfaceCapabilitiesCA02A_ObjectIdentity = ObjectIdentity
subnetInterfaceCapabilitiesCA02A = _SubnetInterfaceCapabilitiesCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 45, 3, 1, 3, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-MsCarrier-MscPassport-SubnetInterfaceMIB",
    **{"mscModVcs": mscModVcs,
       "mscModVcsRowStatusTable": mscModVcsRowStatusTable,
       "mscModVcsRowStatusEntry": mscModVcsRowStatusEntry,
       "mscModVcsRowStatus": mscModVcsRowStatus,
       "mscModVcsComponentName": mscModVcsComponentName,
       "mscModVcsStorageType": mscModVcsStorageType,
       "mscModVcsIndex": mscModVcsIndex,
       "mscModVcsAccOptTable": mscModVcsAccOptTable,
       "mscModVcsAccOptEntry": mscModVcsAccOptEntry,
       "mscModVcsSegmentSize": mscModVcsSegmentSize,
       "mscModVcsUnitsCounted": mscModVcsUnitsCounted,
       "mscModVcsAccountingFax": mscModVcsAccountingFax,
       "mscModVcsGenerationMode": mscModVcsGenerationMode,
       "mscModVcsAddOptTable": mscModVcsAddOptTable,
       "mscModVcsAddOptEntry": mscModVcsAddOptEntry,
       "mscModVcsDefaultNumberingPlan": mscModVcsDefaultNumberingPlan,
       "mscModVcsNetworkIdType": mscModVcsNetworkIdType,
       "mscModVcsX121Type": mscModVcsX121Type,
       "mscModVcsNetworkIdCode": mscModVcsNetworkIdCode,
       "mscModVcsX121IntlAddresses": mscModVcsX121IntlAddresses,
       "mscModVcsX121IntllPrefixDigit": mscModVcsX121IntllPrefixDigit,
       "mscModVcsX121MinAddressLength": mscModVcsX121MinAddressLength,
       "mscModVcsX121MaxAddressLength": mscModVcsX121MaxAddressLength,
       "mscModVcsX121ToE164EscapeSignificance": mscModVcsX121ToE164EscapeSignificance,
       "mscModVcsE164IntlFormatAllowed": mscModVcsE164IntlFormatAllowed,
       "mscModVcsE164IntlPrefixDigits": mscModVcsE164IntlPrefixDigits,
       "mscModVcsE164NatlPrefixDigit": mscModVcsE164NatlPrefixDigit,
       "mscModVcsE164LocalAddressLength": mscModVcsE164LocalAddressLength,
       "mscModVcsE164TeleCountryCode": mscModVcsE164TeleCountryCode,
       "mscModVcsE164NatlMinAddressLength": mscModVcsE164NatlMinAddressLength,
       "mscModVcsE164NatlMaxAddressLength": mscModVcsE164NatlMaxAddressLength,
       "mscModVcsE164IntlMinAddressLength": mscModVcsE164IntlMinAddressLength,
       "mscModVcsE164IntlMaxAddressLength": mscModVcsE164IntlMaxAddressLength,
       "mscModVcsE164LocalMinAddressLength": mscModVcsE164LocalMinAddressLength,
       "mscModVcsE164LocalMaxAddressLength": mscModVcsE164LocalMaxAddressLength,
       "mscModVcsIntOptTable": mscModVcsIntOptTable,
       "mscModVcsIntOptEntry": mscModVcsIntOptEntry,
       "mscModVcsHighPriorityPacketSizes": mscModVcsHighPriorityPacketSizes,
       "mscModVcsMaxSubnetPacketSize": mscModVcsMaxSubnetPacketSize,
       "mscModVcsCallSetupTimer": mscModVcsCallSetupTimer,
       "mscModVcsCallRetryTimer": mscModVcsCallRetryTimer,
       "mscModVcsDelaySubnetAcks": mscModVcsDelaySubnetAcks,
       "mscModVcsWinsTable": mscModVcsWinsTable,
       "mscModVcsWinsEntry": mscModVcsWinsEntry,
       "mscModVcsWinsPktIndex": mscModVcsWinsPktIndex,
       "mscModVcsWinsTptIndex": mscModVcsWinsTptIndex,
       "mscModVcsWinsValue": mscModVcsWinsValue,
       "subnetInterfaceMIB": subnetInterfaceMIB,
       "subnetInterfaceGroup": subnetInterfaceGroup,
       "subnetInterfaceGroupCA": subnetInterfaceGroupCA,
       "subnetInterfaceGroupCA02": subnetInterfaceGroupCA02,
       "subnetInterfaceGroupCA02A": subnetInterfaceGroupCA02A,
       "subnetInterfaceCapabilities": subnetInterfaceCapabilities,
       "subnetInterfaceCapabilitiesCA": subnetInterfaceCapabilitiesCA,
       "subnetInterfaceCapabilitiesCA02": subnetInterfaceCapabilitiesCA02,
       "subnetInterfaceCapabilitiesCA02A": subnetInterfaceCapabilitiesCA02A}
)
