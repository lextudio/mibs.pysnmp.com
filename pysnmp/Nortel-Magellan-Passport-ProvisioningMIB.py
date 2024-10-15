# SNMP MIB module (Nortel-Magellan-Passport-ProvisioningMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-Magellan-Passport-ProvisioningMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:31:18 2024
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

(DisplayString,
 RowPointer,
 RowStatus,
 StorageType,
 Unsigned32) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-StandardTextualConventionsMIB",
    "DisplayString",
    "RowPointer",
    "RowStatus",
    "StorageType",
    "Unsigned32")

(AsciiString,
 AsciiStringIndex,
 EnterpriseDateAndTime,
 NonReplicated) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-TextualConventionsMIB",
    "AsciiString",
    "AsciiStringIndex",
    "EnterpriseDateAndTime",
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

_Prov_ObjectIdentity = ObjectIdentity
prov = _Prov_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 11)
)
_ProvRowStatusTable_Object = MibTable
provRowStatusTable = _ProvRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 11, 1)
)
if mibBuilder.loadTexts:
    provRowStatusTable.setStatus("mandatory")
_ProvRowStatusEntry_Object = MibTableRow
provRowStatusEntry = _ProvRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 11, 1, 1)
)
provRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-ProvisioningMIB", "provIndex"),
)
if mibBuilder.loadTexts:
    provRowStatusEntry.setStatus("mandatory")
_ProvRowStatus_Type = RowStatus
_ProvRowStatus_Object = MibTableColumn
provRowStatus = _ProvRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 11, 1, 1, 1),
    _ProvRowStatus_Type()
)
provRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    provRowStatus.setStatus("mandatory")
_ProvComponentName_Type = DisplayString
_ProvComponentName_Object = MibTableColumn
provComponentName = _ProvComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 11, 1, 1, 2),
    _ProvComponentName_Type()
)
provComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    provComponentName.setStatus("mandatory")
_ProvStorageType_Type = StorageType
_ProvStorageType_Object = MibTableColumn
provStorageType = _ProvStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 11, 1, 1, 4),
    _ProvStorageType_Type()
)
provStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    provStorageType.setStatus("mandatory")
_ProvIndex_Type = NonReplicated
_ProvIndex_Object = MibTableColumn
provIndex = _ProvIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 11, 1, 1, 10),
    _ProvIndex_Type()
)
provIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    provIndex.setStatus("mandatory")
_ProvView_ObjectIdentity = ObjectIdentity
provView = _ProvView_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 11, 2)
)
_ProvViewRowStatusTable_Object = MibTable
provViewRowStatusTable = _ProvViewRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 11, 2, 1)
)
if mibBuilder.loadTexts:
    provViewRowStatusTable.setStatus("mandatory")
_ProvViewRowStatusEntry_Object = MibTableRow
provViewRowStatusEntry = _ProvViewRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 11, 2, 1, 1)
)
provViewRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-ProvisioningMIB", "provIndex"),
    (0, "Nortel-Magellan-Passport-ProvisioningMIB", "provViewIndex"),
)
if mibBuilder.loadTexts:
    provViewRowStatusEntry.setStatus("mandatory")
_ProvViewRowStatus_Type = RowStatus
_ProvViewRowStatus_Object = MibTableColumn
provViewRowStatus = _ProvViewRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 11, 2, 1, 1, 1),
    _ProvViewRowStatus_Type()
)
provViewRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    provViewRowStatus.setStatus("mandatory")
_ProvViewComponentName_Type = DisplayString
_ProvViewComponentName_Object = MibTableColumn
provViewComponentName = _ProvViewComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 11, 2, 1, 1, 2),
    _ProvViewComponentName_Type()
)
provViewComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    provViewComponentName.setStatus("mandatory")
_ProvViewStorageType_Type = StorageType
_ProvViewStorageType_Object = MibTableColumn
provViewStorageType = _ProvViewStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 11, 2, 1, 1, 4),
    _ProvViewStorageType_Type()
)
provViewStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    provViewStorageType.setStatus("mandatory")


class _ProvViewIndex_Type(AsciiStringIndex):
    """Custom type provViewIndex based on AsciiStringIndex"""
    subtypeSpec = AsciiStringIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_ProvViewIndex_Type.__name__ = "AsciiStringIndex"
_ProvViewIndex_Object = MibTableColumn
provViewIndex = _ProvViewIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 11, 2, 1, 1, 10),
    _ProvViewIndex_Type()
)
provViewIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    provViewIndex.setStatus("mandatory")
_ProvViewOperTable_Object = MibTable
provViewOperTable = _ProvViewOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 11, 2, 100)
)
if mibBuilder.loadTexts:
    provViewOperTable.setStatus("mandatory")
_ProvViewOperEntry_Object = MibTableRow
provViewOperEntry = _ProvViewOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 11, 2, 100, 1)
)
provViewOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-ProvisioningMIB", "provIndex"),
    (0, "Nortel-Magellan-Passport-ProvisioningMIB", "provViewIndex"),
)
if mibBuilder.loadTexts:
    provViewOperEntry.setStatus("mandatory")


class _ProvViewUser_Type(AsciiString):
    """Custom type provViewUser based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_ProvViewUser_Type.__name__ = "AsciiString"
_ProvViewUser_Object = MibTableColumn
provViewUser = _ProvViewUser_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 11, 2, 100, 1, 1),
    _ProvViewUser_Type()
)
provViewUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    provViewUser.setStatus("mandatory")


class _ProvViewCheckState_Type(Integer32):
    """Custom type provViewCheckState based on Integer32"""
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
        *(("failed", 0),
          ("full", 4),
          ("partial", 2),
          ("softwareChanged", 3),
          ("unknown", 1))
    )


_ProvViewCheckState_Type.__name__ = "Integer32"
_ProvViewCheckState_Object = MibTableColumn
provViewCheckState = _ProvViewCheckState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 11, 2, 100, 1, 2),
    _ProvViewCheckState_Type()
)
provViewCheckState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    provViewCheckState.setStatus("mandatory")


class _ProvViewComponents_Type(Unsigned32):
    """Custom type provViewComponents based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999999),
    )


_ProvViewComponents_Type.__name__ = "Unsigned32"
_ProvViewComponents_Object = MibTableColumn
provViewComponents = _ProvViewComponents_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 11, 2, 100, 1, 3),
    _ProvViewComponents_Type()
)
provViewComponents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    provViewComponents.setStatus("mandatory")


class _ProvViewFormats_Type(OctetString):
    """Custom type provViewFormats based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_ProvViewFormats_Type.__name__ = "OctetString"
_ProvViewFormats_Object = MibTableColumn
provViewFormats = _ProvViewFormats_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 11, 2, 100, 1, 4),
    _ProvViewFormats_Type()
)
provViewFormats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    provViewFormats.setStatus("mandatory")


class _ProvViewBaseView_Type(AsciiString):
    """Custom type provViewBaseView based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_ProvViewBaseView_Type.__name__ = "AsciiString"
_ProvViewBaseView_Object = MibTableColumn
provViewBaseView = _ProvViewBaseView_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 11, 2, 100, 1, 5),
    _ProvViewBaseView_Type()
)
provViewBaseView.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    provViewBaseView.setStatus("mandatory")


class _ProvViewVersion_Type(AsciiString):
    """Custom type provViewVersion based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_ProvViewVersion_Type.__name__ = "AsciiString"
_ProvViewVersion_Object = MibTableColumn
provViewVersion = _ProvViewVersion_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 11, 2, 100, 1, 6),
    _ProvViewVersion_Type()
)
provViewVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    provViewVersion.setStatus("mandatory")


class _ProvViewCreationDate_Type(EnterpriseDateAndTime):
    """Custom type provViewCreationDate based on EnterpriseDateAndTime"""
    subtypeSpec = EnterpriseDateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(19, 19),
    )


_ProvViewCreationDate_Type.__name__ = "EnterpriseDateAndTime"
_ProvViewCreationDate_Object = MibTableColumn
provViewCreationDate = _ProvViewCreationDate_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 11, 2, 100, 1, 7),
    _ProvViewCreationDate_Type()
)
provViewCreationDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    provViewCreationDate.setStatus("mandatory")
_ProvStateTable_Object = MibTable
provStateTable = _ProvStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 11, 10)
)
if mibBuilder.loadTexts:
    provStateTable.setStatus("mandatory")
_ProvStateEntry_Object = MibTableRow
provStateEntry = _ProvStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 11, 10, 1)
)
provStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-ProvisioningMIB", "provIndex"),
)
if mibBuilder.loadTexts:
    provStateEntry.setStatus("mandatory")


class _ProvAdminState_Type(Integer32):
    """Custom type provAdminState based on Integer32"""
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


_ProvAdminState_Type.__name__ = "Integer32"
_ProvAdminState_Object = MibTableColumn
provAdminState = _ProvAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 11, 10, 1, 1),
    _ProvAdminState_Type()
)
provAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    provAdminState.setStatus("mandatory")


class _ProvOperationalState_Type(Integer32):
    """Custom type provOperationalState based on Integer32"""
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


_ProvOperationalState_Type.__name__ = "Integer32"
_ProvOperationalState_Object = MibTableColumn
provOperationalState = _ProvOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 11, 10, 1, 2),
    _ProvOperationalState_Type()
)
provOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    provOperationalState.setStatus("mandatory")


class _ProvUsageState_Type(Integer32):
    """Custom type provUsageState based on Integer32"""
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


_ProvUsageState_Type.__name__ = "Integer32"
_ProvUsageState_Object = MibTableColumn
provUsageState = _ProvUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 11, 10, 1, 3),
    _ProvUsageState_Type()
)
provUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    provUsageState.setStatus("mandatory")
_ProvOperTable_Object = MibTable
provOperTable = _ProvOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 11, 11)
)
if mibBuilder.loadTexts:
    provOperTable.setStatus("mandatory")
_ProvOperEntry_Object = MibTableRow
provOperEntry = _ProvOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 11, 11, 1)
)
provOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-ProvisioningMIB", "provIndex"),
)
if mibBuilder.loadTexts:
    provOperEntry.setStatus("mandatory")


class _ProvProvisioningActivity_Type(Integer32):
    """Custom type provProvisioningActivity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              11,
              12,
              13,
              14,
              15,
              21)
        )
    )
    namedValues = NamedValues(
        *(("activation", 3),
          ("adding", 21),
          ("clearing", 11),
          ("committing", 13),
          ("confirming", 15),
          ("copying", 12),
          ("deleting", 14),
          ("initialActivation", 4),
          ("initialLoading", 0),
          ("loadingOrApplying", 7),
          ("none", 2),
          ("rollingBack", 5),
          ("saving", 6),
          ("semanticChecking", 8),
          ("waitingForConfirm", 9))
    )


_ProvProvisioningActivity_Type.__name__ = "Integer32"
_ProvProvisioningActivity_Object = MibTableColumn
provProvisioningActivity = _ProvProvisioningActivity_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 11, 11, 1, 1),
    _ProvProvisioningActivity_Type()
)
provProvisioningActivity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    provProvisioningActivity.setStatus("mandatory")


class _ProvActivityProgress_Type(AsciiString):
    """Custom type provActivityProgress based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_ProvActivityProgress_Type.__name__ = "AsciiString"
_ProvActivityProgress_Object = MibTableColumn
provActivityProgress = _ProvActivityProgress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 11, 11, 1, 2),
    _ProvActivityProgress_Type()
)
provActivityProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    provActivityProgress.setStatus("mandatory")


class _ProvCommittedFileName_Type(AsciiString):
    """Custom type provCommittedFileName based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_ProvCommittedFileName_Type.__name__ = "AsciiString"
_ProvCommittedFileName_Object = MibTableColumn
provCommittedFileName = _ProvCommittedFileName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 11, 11, 1, 3),
    _ProvCommittedFileName_Type()
)
provCommittedFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    provCommittedFileName.setStatus("mandatory")


class _ProvCurrentViewFileName_Type(AsciiString):
    """Custom type provCurrentViewFileName based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_ProvCurrentViewFileName_Type.__name__ = "AsciiString"
_ProvCurrentViewFileName_Object = MibTableColumn
provCurrentViewFileName = _ProvCurrentViewFileName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 11, 11, 1, 4),
    _ProvCurrentViewFileName_Type()
)
provCurrentViewFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    provCurrentViewFileName.setStatus("mandatory")


class _ProvLastUsedFileName_Type(AsciiString):
    """Custom type provLastUsedFileName based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_ProvLastUsedFileName_Type.__name__ = "AsciiString"
_ProvLastUsedFileName_Object = MibTableColumn
provLastUsedFileName = _ProvLastUsedFileName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 11, 11, 1, 5),
    _ProvLastUsedFileName_Type()
)
provLastUsedFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    provLastUsedFileName.setStatus("mandatory")
_ProvProvisioningSession_Type = RowPointer
_ProvProvisioningSession_Object = MibTableColumn
provProvisioningSession = _ProvProvisioningSession_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 11, 11, 1, 6),
    _ProvProvisioningSession_Type()
)
provProvisioningSession.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    provProvisioningSession.setStatus("mandatory")


class _ProvProvisioningUser_Type(AsciiString):
    """Custom type provProvisioningUser based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_ProvProvisioningUser_Type.__name__ = "AsciiString"
_ProvProvisioningUser_Object = MibTableColumn
provProvisioningUser = _ProvProvisioningUser_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 11, 11, 1, 7),
    _ProvProvisioningUser_Type()
)
provProvisioningUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    provProvisioningUser.setStatus("mandatory")


class _ProvCheckRequired_Type(Integer32):
    """Custom type provCheckRequired based on Integer32"""
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


_ProvCheckRequired_Type.__name__ = "Integer32"
_ProvCheckRequired_Object = MibTableColumn
provCheckRequired = _ProvCheckRequired_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 11, 11, 1, 8),
    _ProvCheckRequired_Type()
)
provCheckRequired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    provCheckRequired.setStatus("mandatory")


class _ProvNextFileSequenceNumber_Type(Unsigned32):
    """Custom type provNextFileSequenceNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 999),
    )


_ProvNextFileSequenceNumber_Type.__name__ = "Unsigned32"
_ProvNextFileSequenceNumber_Object = MibTableColumn
provNextFileSequenceNumber = _ProvNextFileSequenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 11, 11, 1, 9),
    _ProvNextFileSequenceNumber_Type()
)
provNextFileSequenceNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    provNextFileSequenceNumber.setStatus("obsolete")


class _ProvConfirmRequired_Type(Integer32):
    """Custom type provConfirmRequired based on Integer32"""
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


_ProvConfirmRequired_Type.__name__ = "Integer32"
_ProvConfirmRequired_Object = MibTableColumn
provConfirmRequired = _ProvConfirmRequired_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 11, 11, 1, 10),
    _ProvConfirmRequired_Type()
)
provConfirmRequired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    provConfirmRequired.setStatus("mandatory")


class _ProvProvisioningDirectory_Type(AsciiString):
    """Custom type provProvisioningDirectory based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_ProvProvisioningDirectory_Type.__name__ = "AsciiString"
_ProvProvisioningDirectory_Object = MibTableColumn
provProvisioningDirectory = _ProvProvisioningDirectory_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 11, 11, 1, 11),
    _ProvProvisioningDirectory_Type()
)
provProvisioningDirectory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    provProvisioningDirectory.setStatus("obsolete")


class _ProvEditViewName_Type(AsciiString):
    """Custom type provEditViewName based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_ProvEditViewName_Type.__name__ = "AsciiString"
_ProvEditViewName_Object = MibTableColumn
provEditViewName = _ProvEditViewName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 11, 11, 1, 12),
    _ProvEditViewName_Type()
)
provEditViewName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    provEditViewName.setStatus("mandatory")


class _ProvEditViewAddedComponents_Type(Unsigned32):
    """Custom type provEditViewAddedComponents based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_ProvEditViewAddedComponents_Type.__name__ = "Unsigned32"
_ProvEditViewAddedComponents_Object = MibTableColumn
provEditViewAddedComponents = _ProvEditViewAddedComponents_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 11, 11, 1, 13),
    _ProvEditViewAddedComponents_Type()
)
provEditViewAddedComponents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    provEditViewAddedComponents.setStatus("mandatory")


class _ProvEditViewDeletedComponents_Type(Unsigned32):
    """Custom type provEditViewDeletedComponents based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_ProvEditViewDeletedComponents_Type.__name__ = "Unsigned32"
_ProvEditViewDeletedComponents_Object = MibTableColumn
provEditViewDeletedComponents = _ProvEditViewDeletedComponents_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 11, 11, 1, 14),
    _ProvEditViewDeletedComponents_Type()
)
provEditViewDeletedComponents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    provEditViewDeletedComponents.setStatus("mandatory")


class _ProvEditViewChangedComponents_Type(Unsigned32):
    """Custom type provEditViewChangedComponents based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_ProvEditViewChangedComponents_Type.__name__ = "Unsigned32"
_ProvEditViewChangedComponents_Object = MibTableColumn
provEditViewChangedComponents = _ProvEditViewChangedComponents_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 11, 11, 1, 15),
    _ProvEditViewChangedComponents_Type()
)
provEditViewChangedComponents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    provEditViewChangedComponents.setStatus("mandatory")


class _ProvStandbyCpActivity_Type(Integer32):
    """Custom type provStandbyCpActivity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              6)
        )
    )
    namedValues = NamedValues(
        *(("loadingProvisioningData", 1),
          ("none", 0),
          ("savingCommitFormatProvisioningData", 6))
    )


_ProvStandbyCpActivity_Type.__name__ = "Integer32"
_ProvStandbyCpActivity_Object = MibTableColumn
provStandbyCpActivity = _ProvStandbyCpActivity_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 11, 11, 1, 16),
    _ProvStandbyCpActivity_Type()
)
provStandbyCpActivity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    provStandbyCpActivity.setStatus("mandatory")


class _ProvStandbyCpActivityProgress_Type(AsciiString):
    """Custom type provStandbyCpActivityProgress based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_ProvStandbyCpActivityProgress_Type.__name__ = "AsciiString"
_ProvStandbyCpActivityProgress_Object = MibTableColumn
provStandbyCpActivityProgress = _ProvStandbyCpActivityProgress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 11, 11, 1, 17),
    _ProvStandbyCpActivityProgress_Type()
)
provStandbyCpActivityProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    provStandbyCpActivityProgress.setStatus("mandatory")
_ProvisioningMIB_ObjectIdentity = ObjectIdentity
provisioningMIB = _ProvisioningMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 19)
)
_ProvisioningGroup_ObjectIdentity = ObjectIdentity
provisioningGroup = _ProvisioningGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 19, 1)
)
_ProvisioningGroupBE_ObjectIdentity = ObjectIdentity
provisioningGroupBE = _ProvisioningGroupBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 19, 1, 5)
)
_ProvisioningGroupBE00_ObjectIdentity = ObjectIdentity
provisioningGroupBE00 = _ProvisioningGroupBE00_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 19, 1, 5, 1)
)
_ProvisioningGroupBE00A_ObjectIdentity = ObjectIdentity
provisioningGroupBE00A = _ProvisioningGroupBE00A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 19, 1, 5, 1, 2)
)
_ProvisioningCapabilities_ObjectIdentity = ObjectIdentity
provisioningCapabilities = _ProvisioningCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 19, 3)
)
_ProvisioningCapabilitiesBE_ObjectIdentity = ObjectIdentity
provisioningCapabilitiesBE = _ProvisioningCapabilitiesBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 19, 3, 5)
)
_ProvisioningCapabilitiesBE00_ObjectIdentity = ObjectIdentity
provisioningCapabilitiesBE00 = _ProvisioningCapabilitiesBE00_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 19, 3, 5, 1)
)
_ProvisioningCapabilitiesBE00A_ObjectIdentity = ObjectIdentity
provisioningCapabilitiesBE00A = _ProvisioningCapabilitiesBE00A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 19, 3, 5, 1, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-Magellan-Passport-ProvisioningMIB",
    **{"prov": prov,
       "provRowStatusTable": provRowStatusTable,
       "provRowStatusEntry": provRowStatusEntry,
       "provRowStatus": provRowStatus,
       "provComponentName": provComponentName,
       "provStorageType": provStorageType,
       "provIndex": provIndex,
       "provView": provView,
       "provViewRowStatusTable": provViewRowStatusTable,
       "provViewRowStatusEntry": provViewRowStatusEntry,
       "provViewRowStatus": provViewRowStatus,
       "provViewComponentName": provViewComponentName,
       "provViewStorageType": provViewStorageType,
       "provViewIndex": provViewIndex,
       "provViewOperTable": provViewOperTable,
       "provViewOperEntry": provViewOperEntry,
       "provViewUser": provViewUser,
       "provViewCheckState": provViewCheckState,
       "provViewComponents": provViewComponents,
       "provViewFormats": provViewFormats,
       "provViewBaseView": provViewBaseView,
       "provViewVersion": provViewVersion,
       "provViewCreationDate": provViewCreationDate,
       "provStateTable": provStateTable,
       "provStateEntry": provStateEntry,
       "provAdminState": provAdminState,
       "provOperationalState": provOperationalState,
       "provUsageState": provUsageState,
       "provOperTable": provOperTable,
       "provOperEntry": provOperEntry,
       "provProvisioningActivity": provProvisioningActivity,
       "provActivityProgress": provActivityProgress,
       "provCommittedFileName": provCommittedFileName,
       "provCurrentViewFileName": provCurrentViewFileName,
       "provLastUsedFileName": provLastUsedFileName,
       "provProvisioningSession": provProvisioningSession,
       "provProvisioningUser": provProvisioningUser,
       "provCheckRequired": provCheckRequired,
       "provNextFileSequenceNumber": provNextFileSequenceNumber,
       "provConfirmRequired": provConfirmRequired,
       "provProvisioningDirectory": provProvisioningDirectory,
       "provEditViewName": provEditViewName,
       "provEditViewAddedComponents": provEditViewAddedComponents,
       "provEditViewDeletedComponents": provEditViewDeletedComponents,
       "provEditViewChangedComponents": provEditViewChangedComponents,
       "provStandbyCpActivity": provStandbyCpActivity,
       "provStandbyCpActivityProgress": provStandbyCpActivityProgress,
       "provisioningMIB": provisioningMIB,
       "provisioningGroup": provisioningGroup,
       "provisioningGroupBE": provisioningGroupBE,
       "provisioningGroupBE00": provisioningGroupBE00,
       "provisioningGroupBE00A": provisioningGroupBE00A,
       "provisioningCapabilities": provisioningCapabilities,
       "provisioningCapabilitiesBE": provisioningCapabilitiesBE,
       "provisioningCapabilitiesBE00": provisioningCapabilitiesBE00,
       "provisioningCapabilitiesBE00A": provisioningCapabilitiesBE00A}
)
