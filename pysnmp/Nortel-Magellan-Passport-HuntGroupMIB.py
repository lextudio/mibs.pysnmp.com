# SNMP MIB module (Nortel-Magellan-Passport-HuntGroupMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-Magellan-Passport-HuntGroupMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:30:55 2024
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
 RowStatus,
 StorageType,
 Unsigned32) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-StandardTextualConventionsMIB",
    "Counter32",
    "DisplayString",
    "Integer32",
    "RowStatus",
    "StorageType",
    "Unsigned32")

(AsciiString,
 Link) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-TextualConventionsMIB",
    "AsciiString",
    "Link")

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

_Hg_ObjectIdentity = ObjectIdentity
hg = _Hg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 131)
)
_HgRowStatusTable_Object = MibTable
hgRowStatusTable = _HgRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 131, 1)
)
if mibBuilder.loadTexts:
    hgRowStatusTable.setStatus("mandatory")
_HgRowStatusEntry_Object = MibTableRow
hgRowStatusEntry = _HgRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 131, 1, 1)
)
hgRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-HuntGroupMIB", "hgIndex"),
)
if mibBuilder.loadTexts:
    hgRowStatusEntry.setStatus("mandatory")
_HgRowStatus_Type = RowStatus
_HgRowStatus_Object = MibTableColumn
hgRowStatus = _HgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 131, 1, 1, 1),
    _HgRowStatus_Type()
)
hgRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hgRowStatus.setStatus("mandatory")
_HgComponentName_Type = DisplayString
_HgComponentName_Object = MibTableColumn
hgComponentName = _HgComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 131, 1, 1, 2),
    _HgComponentName_Type()
)
hgComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hgComponentName.setStatus("mandatory")
_HgStorageType_Type = StorageType
_HgStorageType_Object = MibTableColumn
hgStorageType = _HgStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 131, 1, 1, 4),
    _HgStorageType_Type()
)
hgStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hgStorageType.setStatus("mandatory")


class _HgIndex_Type(Integer32):
    """Custom type hgIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HgIndex_Type.__name__ = "Integer32"
_HgIndex_Object = MibTableColumn
hgIndex = _HgIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 131, 1, 1, 10),
    _HgIndex_Type()
)
hgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hgIndex.setStatus("mandatory")
_HgHgM_ObjectIdentity = ObjectIdentity
hgHgM = _HgHgM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 131, 2)
)
_HgHgMRowStatusTable_Object = MibTable
hgHgMRowStatusTable = _HgHgMRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 131, 2, 1)
)
if mibBuilder.loadTexts:
    hgHgMRowStatusTable.setStatus("mandatory")
_HgHgMRowStatusEntry_Object = MibTableRow
hgHgMRowStatusEntry = _HgHgMRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 131, 2, 1, 1)
)
hgHgMRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-HuntGroupMIB", "hgIndex"),
    (0, "Nortel-Magellan-Passport-HuntGroupMIB", "hgHgMIndex"),
)
if mibBuilder.loadTexts:
    hgHgMRowStatusEntry.setStatus("mandatory")
_HgHgMRowStatus_Type = RowStatus
_HgHgMRowStatus_Object = MibTableColumn
hgHgMRowStatus = _HgHgMRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 131, 2, 1, 1, 1),
    _HgHgMRowStatus_Type()
)
hgHgMRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hgHgMRowStatus.setStatus("mandatory")
_HgHgMComponentName_Type = DisplayString
_HgHgMComponentName_Object = MibTableColumn
hgHgMComponentName = _HgHgMComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 131, 2, 1, 1, 2),
    _HgHgMComponentName_Type()
)
hgHgMComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hgHgMComponentName.setStatus("mandatory")
_HgHgMStorageType_Type = StorageType
_HgHgMStorageType_Object = MibTableColumn
hgHgMStorageType = _HgHgMStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 131, 2, 1, 1, 4),
    _HgHgMStorageType_Type()
)
hgHgMStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hgHgMStorageType.setStatus("mandatory")


class _HgHgMIndex_Type(Integer32):
    """Custom type hgHgMIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 63),
    )


_HgHgMIndex_Type.__name__ = "Integer32"
_HgHgMIndex_Object = MibTableColumn
hgHgMIndex = _HgHgMIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 131, 2, 1, 1, 10),
    _HgHgMIndex_Type()
)
hgHgMIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hgHgMIndex.setStatus("mandatory")
_HgHgMProvTable_Object = MibTable
hgHgMProvTable = _HgHgMProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 131, 2, 10)
)
if mibBuilder.loadTexts:
    hgHgMProvTable.setStatus("mandatory")
_HgHgMProvEntry_Object = MibTableRow
hgHgMProvEntry = _HgHgMProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 131, 2, 10, 1)
)
hgHgMProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-HuntGroupMIB", "hgIndex"),
    (0, "Nortel-Magellan-Passport-HuntGroupMIB", "hgHgMIndex"),
)
if mibBuilder.loadTexts:
    hgHgMProvEntry.setStatus("mandatory")


class _HgHgMAddress_Type(AsciiString):
    """Custom type hgHgMAddress based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 17),
    )


_HgHgMAddress_Type.__name__ = "AsciiString"
_HgHgMAddress_Object = MibTableColumn
hgHgMAddress = _HgHgMAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 131, 2, 10, 1, 1),
    _HgHgMAddress_Type()
)
hgHgMAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hgHgMAddress.setStatus("mandatory")
_HgHgMStateTable_Object = MibTable
hgHgMStateTable = _HgHgMStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 131, 2, 11)
)
if mibBuilder.loadTexts:
    hgHgMStateTable.setStatus("mandatory")
_HgHgMStateEntry_Object = MibTableRow
hgHgMStateEntry = _HgHgMStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 131, 2, 11, 1)
)
hgHgMStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-HuntGroupMIB", "hgIndex"),
    (0, "Nortel-Magellan-Passport-HuntGroupMIB", "hgHgMIndex"),
)
if mibBuilder.loadTexts:
    hgHgMStateEntry.setStatus("mandatory")


class _HgHgMAdminState_Type(Integer32):
    """Custom type hgHgMAdminState based on Integer32"""
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


_HgHgMAdminState_Type.__name__ = "Integer32"
_HgHgMAdminState_Object = MibTableColumn
hgHgMAdminState = _HgHgMAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 131, 2, 11, 1, 1),
    _HgHgMAdminState_Type()
)
hgHgMAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hgHgMAdminState.setStatus("mandatory")


class _HgHgMOperationalState_Type(Integer32):
    """Custom type hgHgMOperationalState based on Integer32"""
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


_HgHgMOperationalState_Type.__name__ = "Integer32"
_HgHgMOperationalState_Object = MibTableColumn
hgHgMOperationalState = _HgHgMOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 131, 2, 11, 1, 2),
    _HgHgMOperationalState_Type()
)
hgHgMOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hgHgMOperationalState.setStatus("mandatory")


class _HgHgMUsageState_Type(Integer32):
    """Custom type hgHgMUsageState based on Integer32"""
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


_HgHgMUsageState_Type.__name__ = "Integer32"
_HgHgMUsageState_Object = MibTableColumn
hgHgMUsageState = _HgHgMUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 131, 2, 11, 1, 3),
    _HgHgMUsageState_Type()
)
hgHgMUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hgHgMUsageState.setStatus("mandatory")
_HgHgMOperationalTable_Object = MibTable
hgHgMOperationalTable = _HgHgMOperationalTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 131, 2, 12)
)
if mibBuilder.loadTexts:
    hgHgMOperationalTable.setStatus("mandatory")
_HgHgMOperationalEntry_Object = MibTableRow
hgHgMOperationalEntry = _HgHgMOperationalEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 131, 2, 12, 1)
)
hgHgMOperationalEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-HuntGroupMIB", "hgIndex"),
    (0, "Nortel-Magellan-Passport-HuntGroupMIB", "hgHgMIndex"),
)
if mibBuilder.loadTexts:
    hgHgMOperationalEntry.setStatus("mandatory")


class _HgHgMAvailability_Type(Unsigned32):
    """Custom type hgHgMAvailability based on Unsigned32"""
    defaultValue = 4095

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_HgHgMAvailability_Type.__name__ = "Unsigned32"
_HgHgMAvailability_Object = MibTableColumn
hgHgMAvailability = _HgHgMAvailability_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 131, 2, 12, 1, 1),
    _HgHgMAvailability_Type()
)
hgHgMAvailability.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hgHgMAvailability.setStatus("mandatory")
_HgHgMAvailabilityUpdates_Type = Counter32
_HgHgMAvailabilityUpdates_Object = MibTableColumn
hgHgMAvailabilityUpdates = _HgHgMAvailabilityUpdates_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 131, 2, 12, 1, 2),
    _HgHgMAvailabilityUpdates_Type()
)
hgHgMAvailabilityUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hgHgMAvailabilityUpdates.setStatus("mandatory")
_HgHgMCallsRefused_Type = Counter32
_HgHgMCallsRefused_Object = MibTableColumn
hgHgMCallsRefused = _HgHgMCallsRefused_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 131, 2, 12, 1, 3),
    _HgHgMCallsRefused_Type()
)
hgHgMCallsRefused.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hgHgMCallsRefused.setStatus("mandatory")
_HgCidDataTable_Object = MibTable
hgCidDataTable = _HgCidDataTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 131, 10)
)
if mibBuilder.loadTexts:
    hgCidDataTable.setStatus("mandatory")
_HgCidDataEntry_Object = MibTableRow
hgCidDataEntry = _HgCidDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 131, 10, 1)
)
hgCidDataEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-HuntGroupMIB", "hgIndex"),
)
if mibBuilder.loadTexts:
    hgCidDataEntry.setStatus("mandatory")


class _HgCustomerIdentifier_Type(Unsigned32):
    """Custom type hgCustomerIdentifier based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 8191),
    )


_HgCustomerIdentifier_Type.__name__ = "Unsigned32"
_HgCustomerIdentifier_Object = MibTableColumn
hgCustomerIdentifier = _HgCustomerIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 131, 10, 1, 1),
    _HgCustomerIdentifier_Type()
)
hgCustomerIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hgCustomerIdentifier.setStatus("mandatory")
_HgNsapAddressTable_Object = MibTable
hgNsapAddressTable = _HgNsapAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 131, 11)
)
if mibBuilder.loadTexts:
    hgNsapAddressTable.setStatus("mandatory")
_HgNsapAddressEntry_Object = MibTableRow
hgNsapAddressEntry = _HgNsapAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 131, 11, 1)
)
hgNsapAddressEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-HuntGroupMIB", "hgIndex"),
)
if mibBuilder.loadTexts:
    hgNsapAddressEntry.setStatus("mandatory")


class _HgAddress_Type(AsciiString):
    """Custom type hgAddress based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 17),
    )


_HgAddress_Type.__name__ = "AsciiString"
_HgAddress_Object = MibTableColumn
hgAddress = _HgAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 131, 11, 1, 1),
    _HgAddress_Type()
)
hgAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hgAddress.setStatus("mandatory")
_HgProvTable_Object = MibTable
hgProvTable = _HgProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 131, 12)
)
if mibBuilder.loadTexts:
    hgProvTable.setStatus("mandatory")
_HgProvEntry_Object = MibTableRow
hgProvEntry = _HgProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 131, 12, 1)
)
hgProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-HuntGroupMIB", "hgIndex"),
)
if mibBuilder.loadTexts:
    hgProvEntry.setStatus("mandatory")
_HgLogicalProcessor_Type = Link
_HgLogicalProcessor_Object = MibTableColumn
hgLogicalProcessor = _HgLogicalProcessor_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 131, 12, 1, 1),
    _HgLogicalProcessor_Type()
)
hgLogicalProcessor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hgLogicalProcessor.setStatus("mandatory")


class _HgSelectionPolicy_Type(Integer32):
    """Custom type hgSelectionPolicy based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mostAvailable", 2),
          ("rotary", 1),
          ("startFromZero", 0))
    )


_HgSelectionPolicy_Type.__name__ = "Integer32"
_HgSelectionPolicy_Object = MibTableColumn
hgSelectionPolicy = _HgSelectionPolicy_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 131, 12, 1, 2),
    _HgSelectionPolicy_Type()
)
hgSelectionPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hgSelectionPolicy.setStatus("mandatory")


class _HgMaxHuntAttempts_Type(Unsigned32):
    """Custom type hgMaxHuntAttempts based on Unsigned32"""
    defaultValue = 63

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 63),
    )


_HgMaxHuntAttempts_Type.__name__ = "Unsigned32"
_HgMaxHuntAttempts_Object = MibTableColumn
hgMaxHuntAttempts = _HgMaxHuntAttempts_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 131, 12, 1, 3),
    _HgMaxHuntAttempts_Type()
)
hgMaxHuntAttempts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hgMaxHuntAttempts.setStatus("mandatory")


class _HgAppendSuffixDigits_Type(Integer32):
    """Custom type hgAppendSuffixDigits based on Integer32"""
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


_HgAppendSuffixDigits_Type.__name__ = "Integer32"
_HgAppendSuffixDigits_Object = MibTableColumn
hgAppendSuffixDigits = _HgAppendSuffixDigits_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 131, 12, 1, 4),
    _HgAppendSuffixDigits_Type()
)
hgAppendSuffixDigits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hgAppendSuffixDigits.setStatus("mandatory")
_HgStateTable_Object = MibTable
hgStateTable = _HgStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 131, 20)
)
if mibBuilder.loadTexts:
    hgStateTable.setStatus("mandatory")
_HgStateEntry_Object = MibTableRow
hgStateEntry = _HgStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 131, 20, 1)
)
hgStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-HuntGroupMIB", "hgIndex"),
)
if mibBuilder.loadTexts:
    hgStateEntry.setStatus("mandatory")


class _HgAdminState_Type(Integer32):
    """Custom type hgAdminState based on Integer32"""
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


_HgAdminState_Type.__name__ = "Integer32"
_HgAdminState_Object = MibTableColumn
hgAdminState = _HgAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 131, 20, 1, 1),
    _HgAdminState_Type()
)
hgAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hgAdminState.setStatus("mandatory")


class _HgOperationalState_Type(Integer32):
    """Custom type hgOperationalState based on Integer32"""
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


_HgOperationalState_Type.__name__ = "Integer32"
_HgOperationalState_Object = MibTableColumn
hgOperationalState = _HgOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 131, 20, 1, 2),
    _HgOperationalState_Type()
)
hgOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hgOperationalState.setStatus("mandatory")


class _HgUsageState_Type(Integer32):
    """Custom type hgUsageState based on Integer32"""
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


_HgUsageState_Type.__name__ = "Integer32"
_HgUsageState_Object = MibTableColumn
hgUsageState = _HgUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 131, 20, 1, 3),
    _HgUsageState_Type()
)
hgUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hgUsageState.setStatus("mandatory")
_HgOperationalTable_Object = MibTable
hgOperationalTable = _HgOperationalTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 131, 21)
)
if mibBuilder.loadTexts:
    hgOperationalTable.setStatus("mandatory")
_HgOperationalEntry_Object = MibTableRow
hgOperationalEntry = _HgOperationalEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 131, 21, 1)
)
hgOperationalEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-HuntGroupMIB", "hgIndex"),
)
if mibBuilder.loadTexts:
    hgOperationalEntry.setStatus("mandatory")
_HgHuntAttempts_Type = Counter32
_HgHuntAttempts_Object = MibTableColumn
hgHuntAttempts = _HgHuntAttempts_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 131, 21, 1, 2),
    _HgHuntAttempts_Type()
)
hgHuntAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hgHuntAttempts.setStatus("mandatory")
_HgFailedCalls_Type = Counter32
_HgFailedCalls_Object = MibTableColumn
hgFailedCalls = _HgFailedCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 131, 21, 1, 3),
    _HgFailedCalls_Type()
)
hgFailedCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hgFailedCalls.setStatus("mandatory")
_HgInitialHuntAttempts_Type = Counter32
_HgInitialHuntAttempts_Object = MibTableColumn
hgInitialHuntAttempts = _HgInitialHuntAttempts_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 131, 21, 1, 4),
    _HgInitialHuntAttempts_Type()
)
hgInitialHuntAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hgInitialHuntAttempts.setStatus("mandatory")
_HgAvailabilityUpdates_Type = Counter32
_HgAvailabilityUpdates_Object = MibTableColumn
hgAvailabilityUpdates = _HgAvailabilityUpdates_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 131, 21, 1, 5),
    _HgAvailabilityUpdates_Type()
)
hgAvailabilityUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hgAvailabilityUpdates.setStatus("mandatory")
_HgMaxAddrLenExceeded_Type = Counter32
_HgMaxAddrLenExceeded_Object = MibTableColumn
hgMaxAddrLenExceeded = _HgMaxAddrLenExceeded_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 131, 21, 1, 6),
    _HgMaxAddrLenExceeded_Type()
)
hgMaxAddrLenExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hgMaxAddrLenExceeded.setStatus("mandatory")
_HgBadPackets_Type = Counter32
_HgBadPackets_Object = MibTableColumn
hgBadPackets = _HgBadPackets_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 131, 21, 1, 7),
    _HgBadPackets_Type()
)
hgBadPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hgBadPackets.setStatus("mandatory")
_HuntGroupMIB_ObjectIdentity = ObjectIdentity
huntGroupMIB = _HuntGroupMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 130)
)
_HuntGroupGroup_ObjectIdentity = ObjectIdentity
huntGroupGroup = _HuntGroupGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 130, 1)
)
_HuntGroupGroupBE_ObjectIdentity = ObjectIdentity
huntGroupGroupBE = _HuntGroupGroupBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 130, 1, 5)
)
_HuntGroupGroupBE01_ObjectIdentity = ObjectIdentity
huntGroupGroupBE01 = _HuntGroupGroupBE01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 130, 1, 5, 2)
)
_HuntGroupGroupBE01A_ObjectIdentity = ObjectIdentity
huntGroupGroupBE01A = _HuntGroupGroupBE01A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 130, 1, 5, 2, 2)
)
_HuntGroupCapabilities_ObjectIdentity = ObjectIdentity
huntGroupCapabilities = _HuntGroupCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 130, 3)
)
_HuntGroupCapabilitiesBE_ObjectIdentity = ObjectIdentity
huntGroupCapabilitiesBE = _HuntGroupCapabilitiesBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 130, 3, 5)
)
_HuntGroupCapabilitiesBE01_ObjectIdentity = ObjectIdentity
huntGroupCapabilitiesBE01 = _HuntGroupCapabilitiesBE01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 130, 3, 5, 2)
)
_HuntGroupCapabilitiesBE01A_ObjectIdentity = ObjectIdentity
huntGroupCapabilitiesBE01A = _HuntGroupCapabilitiesBE01A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 130, 3, 5, 2, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-Magellan-Passport-HuntGroupMIB",
    **{"hg": hg,
       "hgRowStatusTable": hgRowStatusTable,
       "hgRowStatusEntry": hgRowStatusEntry,
       "hgRowStatus": hgRowStatus,
       "hgComponentName": hgComponentName,
       "hgStorageType": hgStorageType,
       "hgIndex": hgIndex,
       "hgHgM": hgHgM,
       "hgHgMRowStatusTable": hgHgMRowStatusTable,
       "hgHgMRowStatusEntry": hgHgMRowStatusEntry,
       "hgHgMRowStatus": hgHgMRowStatus,
       "hgHgMComponentName": hgHgMComponentName,
       "hgHgMStorageType": hgHgMStorageType,
       "hgHgMIndex": hgHgMIndex,
       "hgHgMProvTable": hgHgMProvTable,
       "hgHgMProvEntry": hgHgMProvEntry,
       "hgHgMAddress": hgHgMAddress,
       "hgHgMStateTable": hgHgMStateTable,
       "hgHgMStateEntry": hgHgMStateEntry,
       "hgHgMAdminState": hgHgMAdminState,
       "hgHgMOperationalState": hgHgMOperationalState,
       "hgHgMUsageState": hgHgMUsageState,
       "hgHgMOperationalTable": hgHgMOperationalTable,
       "hgHgMOperationalEntry": hgHgMOperationalEntry,
       "hgHgMAvailability": hgHgMAvailability,
       "hgHgMAvailabilityUpdates": hgHgMAvailabilityUpdates,
       "hgHgMCallsRefused": hgHgMCallsRefused,
       "hgCidDataTable": hgCidDataTable,
       "hgCidDataEntry": hgCidDataEntry,
       "hgCustomerIdentifier": hgCustomerIdentifier,
       "hgNsapAddressTable": hgNsapAddressTable,
       "hgNsapAddressEntry": hgNsapAddressEntry,
       "hgAddress": hgAddress,
       "hgProvTable": hgProvTable,
       "hgProvEntry": hgProvEntry,
       "hgLogicalProcessor": hgLogicalProcessor,
       "hgSelectionPolicy": hgSelectionPolicy,
       "hgMaxHuntAttempts": hgMaxHuntAttempts,
       "hgAppendSuffixDigits": hgAppendSuffixDigits,
       "hgStateTable": hgStateTable,
       "hgStateEntry": hgStateEntry,
       "hgAdminState": hgAdminState,
       "hgOperationalState": hgOperationalState,
       "hgUsageState": hgUsageState,
       "hgOperationalTable": hgOperationalTable,
       "hgOperationalEntry": hgOperationalEntry,
       "hgHuntAttempts": hgHuntAttempts,
       "hgFailedCalls": hgFailedCalls,
       "hgInitialHuntAttempts": hgInitialHuntAttempts,
       "hgAvailabilityUpdates": hgAvailabilityUpdates,
       "hgMaxAddrLenExceeded": hgMaxAddrLenExceeded,
       "hgBadPackets": hgBadPackets,
       "huntGroupMIB": huntGroupMIB,
       "huntGroupGroup": huntGroupGroup,
       "huntGroupGroupBE": huntGroupGroupBE,
       "huntGroupGroupBE01": huntGroupGroupBE01,
       "huntGroupGroupBE01A": huntGroupGroupBE01A,
       "huntGroupCapabilities": huntGroupCapabilities,
       "huntGroupCapabilitiesBE": huntGroupCapabilitiesBE,
       "huntGroupCapabilitiesBE01": huntGroupCapabilitiesBE01,
       "huntGroupCapabilitiesBE01A": huntGroupCapabilitiesBE01A}
)
