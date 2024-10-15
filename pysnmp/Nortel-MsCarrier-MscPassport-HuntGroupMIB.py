# SNMP MIB module (Nortel-MsCarrier-MscPassport-HuntGroupMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-MsCarrier-MscPassport-HuntGroupMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:32:36 2024
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
    "Nortel-MsCarrier-MscPassport-StandardTextualConventionsMIB",
    "Counter32",
    "DisplayString",
    "Integer32",
    "RowStatus",
    "StorageType",
    "Unsigned32")

(AsciiString,
 Link) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-TextualConventionsMIB",
    "AsciiString",
    "Link")

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

_MscHg_ObjectIdentity = ObjectIdentity
mscHg = _MscHg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 131)
)
_MscHgRowStatusTable_Object = MibTable
mscHgRowStatusTable = _MscHgRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 131, 1)
)
if mibBuilder.loadTexts:
    mscHgRowStatusTable.setStatus("mandatory")
_MscHgRowStatusEntry_Object = MibTableRow
mscHgRowStatusEntry = _MscHgRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 131, 1, 1)
)
mscHgRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-HuntGroupMIB", "mscHgIndex"),
)
if mibBuilder.loadTexts:
    mscHgRowStatusEntry.setStatus("mandatory")
_MscHgRowStatus_Type = RowStatus
_MscHgRowStatus_Object = MibTableColumn
mscHgRowStatus = _MscHgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 131, 1, 1, 1),
    _MscHgRowStatus_Type()
)
mscHgRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscHgRowStatus.setStatus("mandatory")
_MscHgComponentName_Type = DisplayString
_MscHgComponentName_Object = MibTableColumn
mscHgComponentName = _MscHgComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 131, 1, 1, 2),
    _MscHgComponentName_Type()
)
mscHgComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscHgComponentName.setStatus("mandatory")
_MscHgStorageType_Type = StorageType
_MscHgStorageType_Object = MibTableColumn
mscHgStorageType = _MscHgStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 131, 1, 1, 4),
    _MscHgStorageType_Type()
)
mscHgStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscHgStorageType.setStatus("mandatory")


class _MscHgIndex_Type(Integer32):
    """Custom type mscHgIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MscHgIndex_Type.__name__ = "Integer32"
_MscHgIndex_Object = MibTableColumn
mscHgIndex = _MscHgIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 131, 1, 1, 10),
    _MscHgIndex_Type()
)
mscHgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscHgIndex.setStatus("mandatory")
_MscHgHgM_ObjectIdentity = ObjectIdentity
mscHgHgM = _MscHgHgM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 131, 2)
)
_MscHgHgMRowStatusTable_Object = MibTable
mscHgHgMRowStatusTable = _MscHgHgMRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 131, 2, 1)
)
if mibBuilder.loadTexts:
    mscHgHgMRowStatusTable.setStatus("mandatory")
_MscHgHgMRowStatusEntry_Object = MibTableRow
mscHgHgMRowStatusEntry = _MscHgHgMRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 131, 2, 1, 1)
)
mscHgHgMRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-HuntGroupMIB", "mscHgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-HuntGroupMIB", "mscHgHgMIndex"),
)
if mibBuilder.loadTexts:
    mscHgHgMRowStatusEntry.setStatus("mandatory")
_MscHgHgMRowStatus_Type = RowStatus
_MscHgHgMRowStatus_Object = MibTableColumn
mscHgHgMRowStatus = _MscHgHgMRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 131, 2, 1, 1, 1),
    _MscHgHgMRowStatus_Type()
)
mscHgHgMRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscHgHgMRowStatus.setStatus("mandatory")
_MscHgHgMComponentName_Type = DisplayString
_MscHgHgMComponentName_Object = MibTableColumn
mscHgHgMComponentName = _MscHgHgMComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 131, 2, 1, 1, 2),
    _MscHgHgMComponentName_Type()
)
mscHgHgMComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscHgHgMComponentName.setStatus("mandatory")
_MscHgHgMStorageType_Type = StorageType
_MscHgHgMStorageType_Object = MibTableColumn
mscHgHgMStorageType = _MscHgHgMStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 131, 2, 1, 1, 4),
    _MscHgHgMStorageType_Type()
)
mscHgHgMStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscHgHgMStorageType.setStatus("mandatory")


class _MscHgHgMIndex_Type(Integer32):
    """Custom type mscHgHgMIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 63),
    )


_MscHgHgMIndex_Type.__name__ = "Integer32"
_MscHgHgMIndex_Object = MibTableColumn
mscHgHgMIndex = _MscHgHgMIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 131, 2, 1, 1, 10),
    _MscHgHgMIndex_Type()
)
mscHgHgMIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscHgHgMIndex.setStatus("mandatory")
_MscHgHgMProvTable_Object = MibTable
mscHgHgMProvTable = _MscHgHgMProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 131, 2, 10)
)
if mibBuilder.loadTexts:
    mscHgHgMProvTable.setStatus("mandatory")
_MscHgHgMProvEntry_Object = MibTableRow
mscHgHgMProvEntry = _MscHgHgMProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 131, 2, 10, 1)
)
mscHgHgMProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-HuntGroupMIB", "mscHgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-HuntGroupMIB", "mscHgHgMIndex"),
)
if mibBuilder.loadTexts:
    mscHgHgMProvEntry.setStatus("mandatory")


class _MscHgHgMAddress_Type(AsciiString):
    """Custom type mscHgHgMAddress based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 17),
    )


_MscHgHgMAddress_Type.__name__ = "AsciiString"
_MscHgHgMAddress_Object = MibTableColumn
mscHgHgMAddress = _MscHgHgMAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 131, 2, 10, 1, 1),
    _MscHgHgMAddress_Type()
)
mscHgHgMAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscHgHgMAddress.setStatus("mandatory")
_MscHgHgMStateTable_Object = MibTable
mscHgHgMStateTable = _MscHgHgMStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 131, 2, 11)
)
if mibBuilder.loadTexts:
    mscHgHgMStateTable.setStatus("mandatory")
_MscHgHgMStateEntry_Object = MibTableRow
mscHgHgMStateEntry = _MscHgHgMStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 131, 2, 11, 1)
)
mscHgHgMStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-HuntGroupMIB", "mscHgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-HuntGroupMIB", "mscHgHgMIndex"),
)
if mibBuilder.loadTexts:
    mscHgHgMStateEntry.setStatus("mandatory")


class _MscHgHgMAdminState_Type(Integer32):
    """Custom type mscHgHgMAdminState based on Integer32"""
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


_MscHgHgMAdminState_Type.__name__ = "Integer32"
_MscHgHgMAdminState_Object = MibTableColumn
mscHgHgMAdminState = _MscHgHgMAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 131, 2, 11, 1, 1),
    _MscHgHgMAdminState_Type()
)
mscHgHgMAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscHgHgMAdminState.setStatus("mandatory")


class _MscHgHgMOperationalState_Type(Integer32):
    """Custom type mscHgHgMOperationalState based on Integer32"""
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


_MscHgHgMOperationalState_Type.__name__ = "Integer32"
_MscHgHgMOperationalState_Object = MibTableColumn
mscHgHgMOperationalState = _MscHgHgMOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 131, 2, 11, 1, 2),
    _MscHgHgMOperationalState_Type()
)
mscHgHgMOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscHgHgMOperationalState.setStatus("mandatory")


class _MscHgHgMUsageState_Type(Integer32):
    """Custom type mscHgHgMUsageState based on Integer32"""
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


_MscHgHgMUsageState_Type.__name__ = "Integer32"
_MscHgHgMUsageState_Object = MibTableColumn
mscHgHgMUsageState = _MscHgHgMUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 131, 2, 11, 1, 3),
    _MscHgHgMUsageState_Type()
)
mscHgHgMUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscHgHgMUsageState.setStatus("mandatory")
_MscHgHgMOperationalTable_Object = MibTable
mscHgHgMOperationalTable = _MscHgHgMOperationalTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 131, 2, 12)
)
if mibBuilder.loadTexts:
    mscHgHgMOperationalTable.setStatus("mandatory")
_MscHgHgMOperationalEntry_Object = MibTableRow
mscHgHgMOperationalEntry = _MscHgHgMOperationalEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 131, 2, 12, 1)
)
mscHgHgMOperationalEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-HuntGroupMIB", "mscHgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-HuntGroupMIB", "mscHgHgMIndex"),
)
if mibBuilder.loadTexts:
    mscHgHgMOperationalEntry.setStatus("mandatory")


class _MscHgHgMAvailability_Type(Unsigned32):
    """Custom type mscHgHgMAvailability based on Unsigned32"""
    defaultValue = 4095

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_MscHgHgMAvailability_Type.__name__ = "Unsigned32"
_MscHgHgMAvailability_Object = MibTableColumn
mscHgHgMAvailability = _MscHgHgMAvailability_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 131, 2, 12, 1, 1),
    _MscHgHgMAvailability_Type()
)
mscHgHgMAvailability.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscHgHgMAvailability.setStatus("mandatory")
_MscHgHgMAvailabilityUpdates_Type = Counter32
_MscHgHgMAvailabilityUpdates_Object = MibTableColumn
mscHgHgMAvailabilityUpdates = _MscHgHgMAvailabilityUpdates_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 131, 2, 12, 1, 2),
    _MscHgHgMAvailabilityUpdates_Type()
)
mscHgHgMAvailabilityUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscHgHgMAvailabilityUpdates.setStatus("mandatory")
_MscHgHgMCallsRefused_Type = Counter32
_MscHgHgMCallsRefused_Object = MibTableColumn
mscHgHgMCallsRefused = _MscHgHgMCallsRefused_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 131, 2, 12, 1, 3),
    _MscHgHgMCallsRefused_Type()
)
mscHgHgMCallsRefused.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscHgHgMCallsRefused.setStatus("mandatory")
_MscHgCidDataTable_Object = MibTable
mscHgCidDataTable = _MscHgCidDataTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 131, 10)
)
if mibBuilder.loadTexts:
    mscHgCidDataTable.setStatus("mandatory")
_MscHgCidDataEntry_Object = MibTableRow
mscHgCidDataEntry = _MscHgCidDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 131, 10, 1)
)
mscHgCidDataEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-HuntGroupMIB", "mscHgIndex"),
)
if mibBuilder.loadTexts:
    mscHgCidDataEntry.setStatus("mandatory")


class _MscHgCustomerIdentifier_Type(Unsigned32):
    """Custom type mscHgCustomerIdentifier based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 8191),
    )


_MscHgCustomerIdentifier_Type.__name__ = "Unsigned32"
_MscHgCustomerIdentifier_Object = MibTableColumn
mscHgCustomerIdentifier = _MscHgCustomerIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 131, 10, 1, 1),
    _MscHgCustomerIdentifier_Type()
)
mscHgCustomerIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscHgCustomerIdentifier.setStatus("mandatory")
_MscHgNsapAddressTable_Object = MibTable
mscHgNsapAddressTable = _MscHgNsapAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 131, 11)
)
if mibBuilder.loadTexts:
    mscHgNsapAddressTable.setStatus("mandatory")
_MscHgNsapAddressEntry_Object = MibTableRow
mscHgNsapAddressEntry = _MscHgNsapAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 131, 11, 1)
)
mscHgNsapAddressEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-HuntGroupMIB", "mscHgIndex"),
)
if mibBuilder.loadTexts:
    mscHgNsapAddressEntry.setStatus("mandatory")


class _MscHgAddress_Type(AsciiString):
    """Custom type mscHgAddress based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 17),
    )


_MscHgAddress_Type.__name__ = "AsciiString"
_MscHgAddress_Object = MibTableColumn
mscHgAddress = _MscHgAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 131, 11, 1, 1),
    _MscHgAddress_Type()
)
mscHgAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscHgAddress.setStatus("mandatory")
_MscHgProvTable_Object = MibTable
mscHgProvTable = _MscHgProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 131, 12)
)
if mibBuilder.loadTexts:
    mscHgProvTable.setStatus("mandatory")
_MscHgProvEntry_Object = MibTableRow
mscHgProvEntry = _MscHgProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 131, 12, 1)
)
mscHgProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-HuntGroupMIB", "mscHgIndex"),
)
if mibBuilder.loadTexts:
    mscHgProvEntry.setStatus("mandatory")
_MscHgLogicalProcessor_Type = Link
_MscHgLogicalProcessor_Object = MibTableColumn
mscHgLogicalProcessor = _MscHgLogicalProcessor_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 131, 12, 1, 1),
    _MscHgLogicalProcessor_Type()
)
mscHgLogicalProcessor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscHgLogicalProcessor.setStatus("mandatory")


class _MscHgSelectionPolicy_Type(Integer32):
    """Custom type mscHgSelectionPolicy based on Integer32"""
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


_MscHgSelectionPolicy_Type.__name__ = "Integer32"
_MscHgSelectionPolicy_Object = MibTableColumn
mscHgSelectionPolicy = _MscHgSelectionPolicy_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 131, 12, 1, 2),
    _MscHgSelectionPolicy_Type()
)
mscHgSelectionPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscHgSelectionPolicy.setStatus("mandatory")


class _MscHgMaxHuntAttempts_Type(Unsigned32):
    """Custom type mscHgMaxHuntAttempts based on Unsigned32"""
    defaultValue = 63

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 63),
    )


_MscHgMaxHuntAttempts_Type.__name__ = "Unsigned32"
_MscHgMaxHuntAttempts_Object = MibTableColumn
mscHgMaxHuntAttempts = _MscHgMaxHuntAttempts_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 131, 12, 1, 3),
    _MscHgMaxHuntAttempts_Type()
)
mscHgMaxHuntAttempts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscHgMaxHuntAttempts.setStatus("mandatory")


class _MscHgAppendSuffixDigits_Type(Integer32):
    """Custom type mscHgAppendSuffixDigits based on Integer32"""
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


_MscHgAppendSuffixDigits_Type.__name__ = "Integer32"
_MscHgAppendSuffixDigits_Object = MibTableColumn
mscHgAppendSuffixDigits = _MscHgAppendSuffixDigits_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 131, 12, 1, 4),
    _MscHgAppendSuffixDigits_Type()
)
mscHgAppendSuffixDigits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscHgAppendSuffixDigits.setStatus("mandatory")
_MscHgStateTable_Object = MibTable
mscHgStateTable = _MscHgStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 131, 20)
)
if mibBuilder.loadTexts:
    mscHgStateTable.setStatus("mandatory")
_MscHgStateEntry_Object = MibTableRow
mscHgStateEntry = _MscHgStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 131, 20, 1)
)
mscHgStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-HuntGroupMIB", "mscHgIndex"),
)
if mibBuilder.loadTexts:
    mscHgStateEntry.setStatus("mandatory")


class _MscHgAdminState_Type(Integer32):
    """Custom type mscHgAdminState based on Integer32"""
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


_MscHgAdminState_Type.__name__ = "Integer32"
_MscHgAdminState_Object = MibTableColumn
mscHgAdminState = _MscHgAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 131, 20, 1, 1),
    _MscHgAdminState_Type()
)
mscHgAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscHgAdminState.setStatus("mandatory")


class _MscHgOperationalState_Type(Integer32):
    """Custom type mscHgOperationalState based on Integer32"""
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


_MscHgOperationalState_Type.__name__ = "Integer32"
_MscHgOperationalState_Object = MibTableColumn
mscHgOperationalState = _MscHgOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 131, 20, 1, 2),
    _MscHgOperationalState_Type()
)
mscHgOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscHgOperationalState.setStatus("mandatory")


class _MscHgUsageState_Type(Integer32):
    """Custom type mscHgUsageState based on Integer32"""
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


_MscHgUsageState_Type.__name__ = "Integer32"
_MscHgUsageState_Object = MibTableColumn
mscHgUsageState = _MscHgUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 131, 20, 1, 3),
    _MscHgUsageState_Type()
)
mscHgUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscHgUsageState.setStatus("mandatory")
_MscHgOperationalTable_Object = MibTable
mscHgOperationalTable = _MscHgOperationalTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 131, 21)
)
if mibBuilder.loadTexts:
    mscHgOperationalTable.setStatus("mandatory")
_MscHgOperationalEntry_Object = MibTableRow
mscHgOperationalEntry = _MscHgOperationalEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 131, 21, 1)
)
mscHgOperationalEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-HuntGroupMIB", "mscHgIndex"),
)
if mibBuilder.loadTexts:
    mscHgOperationalEntry.setStatus("mandatory")
_MscHgHuntAttempts_Type = Counter32
_MscHgHuntAttempts_Object = MibTableColumn
mscHgHuntAttempts = _MscHgHuntAttempts_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 131, 21, 1, 2),
    _MscHgHuntAttempts_Type()
)
mscHgHuntAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscHgHuntAttempts.setStatus("mandatory")
_MscHgFailedCalls_Type = Counter32
_MscHgFailedCalls_Object = MibTableColumn
mscHgFailedCalls = _MscHgFailedCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 131, 21, 1, 3),
    _MscHgFailedCalls_Type()
)
mscHgFailedCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscHgFailedCalls.setStatus("mandatory")
_MscHgInitialHuntAttempts_Type = Counter32
_MscHgInitialHuntAttempts_Object = MibTableColumn
mscHgInitialHuntAttempts = _MscHgInitialHuntAttempts_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 131, 21, 1, 4),
    _MscHgInitialHuntAttempts_Type()
)
mscHgInitialHuntAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscHgInitialHuntAttempts.setStatus("mandatory")
_MscHgAvailabilityUpdates_Type = Counter32
_MscHgAvailabilityUpdates_Object = MibTableColumn
mscHgAvailabilityUpdates = _MscHgAvailabilityUpdates_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 131, 21, 1, 5),
    _MscHgAvailabilityUpdates_Type()
)
mscHgAvailabilityUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscHgAvailabilityUpdates.setStatus("mandatory")
_MscHgMaxAddrLenExceeded_Type = Counter32
_MscHgMaxAddrLenExceeded_Object = MibTableColumn
mscHgMaxAddrLenExceeded = _MscHgMaxAddrLenExceeded_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 131, 21, 1, 6),
    _MscHgMaxAddrLenExceeded_Type()
)
mscHgMaxAddrLenExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscHgMaxAddrLenExceeded.setStatus("mandatory")
_MscHgBadPackets_Type = Counter32
_MscHgBadPackets_Object = MibTableColumn
mscHgBadPackets = _MscHgBadPackets_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 131, 21, 1, 7),
    _MscHgBadPackets_Type()
)
mscHgBadPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscHgBadPackets.setStatus("mandatory")
_HuntGroupMIB_ObjectIdentity = ObjectIdentity
huntGroupMIB = _HuntGroupMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 130)
)
_HuntGroupGroup_ObjectIdentity = ObjectIdentity
huntGroupGroup = _HuntGroupGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 130, 1)
)
_HuntGroupGroupCA_ObjectIdentity = ObjectIdentity
huntGroupGroupCA = _HuntGroupGroupCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 130, 1, 1)
)
_HuntGroupGroupCA02_ObjectIdentity = ObjectIdentity
huntGroupGroupCA02 = _HuntGroupGroupCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 130, 1, 1, 3)
)
_HuntGroupGroupCA02A_ObjectIdentity = ObjectIdentity
huntGroupGroupCA02A = _HuntGroupGroupCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 130, 1, 1, 3, 2)
)
_HuntGroupCapabilities_ObjectIdentity = ObjectIdentity
huntGroupCapabilities = _HuntGroupCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 130, 3)
)
_HuntGroupCapabilitiesCA_ObjectIdentity = ObjectIdentity
huntGroupCapabilitiesCA = _HuntGroupCapabilitiesCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 130, 3, 1)
)
_HuntGroupCapabilitiesCA02_ObjectIdentity = ObjectIdentity
huntGroupCapabilitiesCA02 = _HuntGroupCapabilitiesCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 130, 3, 1, 3)
)
_HuntGroupCapabilitiesCA02A_ObjectIdentity = ObjectIdentity
huntGroupCapabilitiesCA02A = _HuntGroupCapabilitiesCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 130, 3, 1, 3, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-MsCarrier-MscPassport-HuntGroupMIB",
    **{"mscHg": mscHg,
       "mscHgRowStatusTable": mscHgRowStatusTable,
       "mscHgRowStatusEntry": mscHgRowStatusEntry,
       "mscHgRowStatus": mscHgRowStatus,
       "mscHgComponentName": mscHgComponentName,
       "mscHgStorageType": mscHgStorageType,
       "mscHgIndex": mscHgIndex,
       "mscHgHgM": mscHgHgM,
       "mscHgHgMRowStatusTable": mscHgHgMRowStatusTable,
       "mscHgHgMRowStatusEntry": mscHgHgMRowStatusEntry,
       "mscHgHgMRowStatus": mscHgHgMRowStatus,
       "mscHgHgMComponentName": mscHgHgMComponentName,
       "mscHgHgMStorageType": mscHgHgMStorageType,
       "mscHgHgMIndex": mscHgHgMIndex,
       "mscHgHgMProvTable": mscHgHgMProvTable,
       "mscHgHgMProvEntry": mscHgHgMProvEntry,
       "mscHgHgMAddress": mscHgHgMAddress,
       "mscHgHgMStateTable": mscHgHgMStateTable,
       "mscHgHgMStateEntry": mscHgHgMStateEntry,
       "mscHgHgMAdminState": mscHgHgMAdminState,
       "mscHgHgMOperationalState": mscHgHgMOperationalState,
       "mscHgHgMUsageState": mscHgHgMUsageState,
       "mscHgHgMOperationalTable": mscHgHgMOperationalTable,
       "mscHgHgMOperationalEntry": mscHgHgMOperationalEntry,
       "mscHgHgMAvailability": mscHgHgMAvailability,
       "mscHgHgMAvailabilityUpdates": mscHgHgMAvailabilityUpdates,
       "mscHgHgMCallsRefused": mscHgHgMCallsRefused,
       "mscHgCidDataTable": mscHgCidDataTable,
       "mscHgCidDataEntry": mscHgCidDataEntry,
       "mscHgCustomerIdentifier": mscHgCustomerIdentifier,
       "mscHgNsapAddressTable": mscHgNsapAddressTable,
       "mscHgNsapAddressEntry": mscHgNsapAddressEntry,
       "mscHgAddress": mscHgAddress,
       "mscHgProvTable": mscHgProvTable,
       "mscHgProvEntry": mscHgProvEntry,
       "mscHgLogicalProcessor": mscHgLogicalProcessor,
       "mscHgSelectionPolicy": mscHgSelectionPolicy,
       "mscHgMaxHuntAttempts": mscHgMaxHuntAttempts,
       "mscHgAppendSuffixDigits": mscHgAppendSuffixDigits,
       "mscHgStateTable": mscHgStateTable,
       "mscHgStateEntry": mscHgStateEntry,
       "mscHgAdminState": mscHgAdminState,
       "mscHgOperationalState": mscHgOperationalState,
       "mscHgUsageState": mscHgUsageState,
       "mscHgOperationalTable": mscHgOperationalTable,
       "mscHgOperationalEntry": mscHgOperationalEntry,
       "mscHgHuntAttempts": mscHgHuntAttempts,
       "mscHgFailedCalls": mscHgFailedCalls,
       "mscHgInitialHuntAttempts": mscHgInitialHuntAttempts,
       "mscHgAvailabilityUpdates": mscHgAvailabilityUpdates,
       "mscHgMaxAddrLenExceeded": mscHgMaxAddrLenExceeded,
       "mscHgBadPackets": mscHgBadPackets,
       "huntGroupMIB": huntGroupMIB,
       "huntGroupGroup": huntGroupGroup,
       "huntGroupGroupCA": huntGroupGroupCA,
       "huntGroupGroupCA02": huntGroupGroupCA02,
       "huntGroupGroupCA02A": huntGroupGroupCA02A,
       "huntGroupCapabilities": huntGroupCapabilities,
       "huntGroupCapabilitiesCA": huntGroupCapabilitiesCA,
       "huntGroupCapabilitiesCA02": huntGroupCapabilitiesCA02,
       "huntGroupCapabilitiesCA02A": huntGroupCapabilitiesCA02A}
)
