# SNMP MIB module (Nortel-MsCarrier-MscPassport-ProvisioningMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-MsCarrier-MscPassport-ProvisioningMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:32:59 2024
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
    "Nortel-MsCarrier-MscPassport-StandardTextualConventionsMIB",
    "DisplayString",
    "RowPointer",
    "RowStatus",
    "StorageType",
    "Unsigned32")

(AsciiString,
 AsciiStringIndex,
 EnterpriseDateAndTime,
 NonReplicated) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-TextualConventionsMIB",
    "AsciiString",
    "AsciiStringIndex",
    "EnterpriseDateAndTime",
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

_MscProv_ObjectIdentity = ObjectIdentity
mscProv = _MscProv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 11)
)
_MscProvRowStatusTable_Object = MibTable
mscProvRowStatusTable = _MscProvRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 11, 1)
)
if mibBuilder.loadTexts:
    mscProvRowStatusTable.setStatus("mandatory")
_MscProvRowStatusEntry_Object = MibTableRow
mscProvRowStatusEntry = _MscProvRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 11, 1, 1)
)
mscProvRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-ProvisioningMIB", "mscProvIndex"),
)
if mibBuilder.loadTexts:
    mscProvRowStatusEntry.setStatus("mandatory")
_MscProvRowStatus_Type = RowStatus
_MscProvRowStatus_Object = MibTableColumn
mscProvRowStatus = _MscProvRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 11, 1, 1, 1),
    _MscProvRowStatus_Type()
)
mscProvRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscProvRowStatus.setStatus("mandatory")
_MscProvComponentName_Type = DisplayString
_MscProvComponentName_Object = MibTableColumn
mscProvComponentName = _MscProvComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 11, 1, 1, 2),
    _MscProvComponentName_Type()
)
mscProvComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscProvComponentName.setStatus("mandatory")
_MscProvStorageType_Type = StorageType
_MscProvStorageType_Object = MibTableColumn
mscProvStorageType = _MscProvStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 11, 1, 1, 4),
    _MscProvStorageType_Type()
)
mscProvStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscProvStorageType.setStatus("mandatory")
_MscProvIndex_Type = NonReplicated
_MscProvIndex_Object = MibTableColumn
mscProvIndex = _MscProvIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 11, 1, 1, 10),
    _MscProvIndex_Type()
)
mscProvIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscProvIndex.setStatus("mandatory")
_MscProvView_ObjectIdentity = ObjectIdentity
mscProvView = _MscProvView_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 11, 2)
)
_MscProvViewRowStatusTable_Object = MibTable
mscProvViewRowStatusTable = _MscProvViewRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 11, 2, 1)
)
if mibBuilder.loadTexts:
    mscProvViewRowStatusTable.setStatus("mandatory")
_MscProvViewRowStatusEntry_Object = MibTableRow
mscProvViewRowStatusEntry = _MscProvViewRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 11, 2, 1, 1)
)
mscProvViewRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-ProvisioningMIB", "mscProvIndex"),
    (0, "Nortel-MsCarrier-MscPassport-ProvisioningMIB", "mscProvViewIndex"),
)
if mibBuilder.loadTexts:
    mscProvViewRowStatusEntry.setStatus("mandatory")
_MscProvViewRowStatus_Type = RowStatus
_MscProvViewRowStatus_Object = MibTableColumn
mscProvViewRowStatus = _MscProvViewRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 11, 2, 1, 1, 1),
    _MscProvViewRowStatus_Type()
)
mscProvViewRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscProvViewRowStatus.setStatus("mandatory")
_MscProvViewComponentName_Type = DisplayString
_MscProvViewComponentName_Object = MibTableColumn
mscProvViewComponentName = _MscProvViewComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 11, 2, 1, 1, 2),
    _MscProvViewComponentName_Type()
)
mscProvViewComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscProvViewComponentName.setStatus("mandatory")
_MscProvViewStorageType_Type = StorageType
_MscProvViewStorageType_Object = MibTableColumn
mscProvViewStorageType = _MscProvViewStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 11, 2, 1, 1, 4),
    _MscProvViewStorageType_Type()
)
mscProvViewStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscProvViewStorageType.setStatus("mandatory")


class _MscProvViewIndex_Type(AsciiStringIndex):
    """Custom type mscProvViewIndex based on AsciiStringIndex"""
    subtypeSpec = AsciiStringIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_MscProvViewIndex_Type.__name__ = "AsciiStringIndex"
_MscProvViewIndex_Object = MibTableColumn
mscProvViewIndex = _MscProvViewIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 11, 2, 1, 1, 10),
    _MscProvViewIndex_Type()
)
mscProvViewIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscProvViewIndex.setStatus("mandatory")
_MscProvViewOperTable_Object = MibTable
mscProvViewOperTable = _MscProvViewOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 11, 2, 100)
)
if mibBuilder.loadTexts:
    mscProvViewOperTable.setStatus("mandatory")
_MscProvViewOperEntry_Object = MibTableRow
mscProvViewOperEntry = _MscProvViewOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 11, 2, 100, 1)
)
mscProvViewOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-ProvisioningMIB", "mscProvIndex"),
    (0, "Nortel-MsCarrier-MscPassport-ProvisioningMIB", "mscProvViewIndex"),
)
if mibBuilder.loadTexts:
    mscProvViewOperEntry.setStatus("mandatory")


class _MscProvViewUser_Type(AsciiString):
    """Custom type mscProvViewUser based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_MscProvViewUser_Type.__name__ = "AsciiString"
_MscProvViewUser_Object = MibTableColumn
mscProvViewUser = _MscProvViewUser_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 11, 2, 100, 1, 1),
    _MscProvViewUser_Type()
)
mscProvViewUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscProvViewUser.setStatus("mandatory")


class _MscProvViewCheckState_Type(Integer32):
    """Custom type mscProvViewCheckState based on Integer32"""
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


_MscProvViewCheckState_Type.__name__ = "Integer32"
_MscProvViewCheckState_Object = MibTableColumn
mscProvViewCheckState = _MscProvViewCheckState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 11, 2, 100, 1, 2),
    _MscProvViewCheckState_Type()
)
mscProvViewCheckState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscProvViewCheckState.setStatus("mandatory")


class _MscProvViewComponents_Type(Unsigned32):
    """Custom type mscProvViewComponents based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999999),
    )


_MscProvViewComponents_Type.__name__ = "Unsigned32"
_MscProvViewComponents_Object = MibTableColumn
mscProvViewComponents = _MscProvViewComponents_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 11, 2, 100, 1, 3),
    _MscProvViewComponents_Type()
)
mscProvViewComponents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscProvViewComponents.setStatus("mandatory")


class _MscProvViewFormats_Type(OctetString):
    """Custom type mscProvViewFormats based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscProvViewFormats_Type.__name__ = "OctetString"
_MscProvViewFormats_Object = MibTableColumn
mscProvViewFormats = _MscProvViewFormats_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 11, 2, 100, 1, 4),
    _MscProvViewFormats_Type()
)
mscProvViewFormats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscProvViewFormats.setStatus("mandatory")


class _MscProvViewBaseView_Type(AsciiString):
    """Custom type mscProvViewBaseView based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_MscProvViewBaseView_Type.__name__ = "AsciiString"
_MscProvViewBaseView_Object = MibTableColumn
mscProvViewBaseView = _MscProvViewBaseView_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 11, 2, 100, 1, 5),
    _MscProvViewBaseView_Type()
)
mscProvViewBaseView.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscProvViewBaseView.setStatus("mandatory")


class _MscProvViewVersion_Type(AsciiString):
    """Custom type mscProvViewVersion based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_MscProvViewVersion_Type.__name__ = "AsciiString"
_MscProvViewVersion_Object = MibTableColumn
mscProvViewVersion = _MscProvViewVersion_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 11, 2, 100, 1, 6),
    _MscProvViewVersion_Type()
)
mscProvViewVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscProvViewVersion.setStatus("mandatory")


class _MscProvViewCreationDate_Type(EnterpriseDateAndTime):
    """Custom type mscProvViewCreationDate based on EnterpriseDateAndTime"""
    subtypeSpec = EnterpriseDateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(19, 19),
    )


_MscProvViewCreationDate_Type.__name__ = "EnterpriseDateAndTime"
_MscProvViewCreationDate_Object = MibTableColumn
mscProvViewCreationDate = _MscProvViewCreationDate_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 11, 2, 100, 1, 7),
    _MscProvViewCreationDate_Type()
)
mscProvViewCreationDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscProvViewCreationDate.setStatus("mandatory")
_MscProvStateTable_Object = MibTable
mscProvStateTable = _MscProvStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 11, 10)
)
if mibBuilder.loadTexts:
    mscProvStateTable.setStatus("mandatory")
_MscProvStateEntry_Object = MibTableRow
mscProvStateEntry = _MscProvStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 11, 10, 1)
)
mscProvStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-ProvisioningMIB", "mscProvIndex"),
)
if mibBuilder.loadTexts:
    mscProvStateEntry.setStatus("mandatory")


class _MscProvAdminState_Type(Integer32):
    """Custom type mscProvAdminState based on Integer32"""
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


_MscProvAdminState_Type.__name__ = "Integer32"
_MscProvAdminState_Object = MibTableColumn
mscProvAdminState = _MscProvAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 11, 10, 1, 1),
    _MscProvAdminState_Type()
)
mscProvAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscProvAdminState.setStatus("mandatory")


class _MscProvOperationalState_Type(Integer32):
    """Custom type mscProvOperationalState based on Integer32"""
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


_MscProvOperationalState_Type.__name__ = "Integer32"
_MscProvOperationalState_Object = MibTableColumn
mscProvOperationalState = _MscProvOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 11, 10, 1, 2),
    _MscProvOperationalState_Type()
)
mscProvOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscProvOperationalState.setStatus("mandatory")


class _MscProvUsageState_Type(Integer32):
    """Custom type mscProvUsageState based on Integer32"""
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


_MscProvUsageState_Type.__name__ = "Integer32"
_MscProvUsageState_Object = MibTableColumn
mscProvUsageState = _MscProvUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 11, 10, 1, 3),
    _MscProvUsageState_Type()
)
mscProvUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscProvUsageState.setStatus("mandatory")
_MscProvOperTable_Object = MibTable
mscProvOperTable = _MscProvOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 11, 11)
)
if mibBuilder.loadTexts:
    mscProvOperTable.setStatus("mandatory")
_MscProvOperEntry_Object = MibTableRow
mscProvOperEntry = _MscProvOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 11, 11, 1)
)
mscProvOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-ProvisioningMIB", "mscProvIndex"),
)
if mibBuilder.loadTexts:
    mscProvOperEntry.setStatus("mandatory")


class _MscProvProvisioningActivity_Type(Integer32):
    """Custom type mscProvProvisioningActivity based on Integer32"""
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


_MscProvProvisioningActivity_Type.__name__ = "Integer32"
_MscProvProvisioningActivity_Object = MibTableColumn
mscProvProvisioningActivity = _MscProvProvisioningActivity_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 11, 11, 1, 1),
    _MscProvProvisioningActivity_Type()
)
mscProvProvisioningActivity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscProvProvisioningActivity.setStatus("mandatory")


class _MscProvActivityProgress_Type(AsciiString):
    """Custom type mscProvActivityProgress based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_MscProvActivityProgress_Type.__name__ = "AsciiString"
_MscProvActivityProgress_Object = MibTableColumn
mscProvActivityProgress = _MscProvActivityProgress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 11, 11, 1, 2),
    _MscProvActivityProgress_Type()
)
mscProvActivityProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscProvActivityProgress.setStatus("mandatory")


class _MscProvCommittedFileName_Type(AsciiString):
    """Custom type mscProvCommittedFileName based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_MscProvCommittedFileName_Type.__name__ = "AsciiString"
_MscProvCommittedFileName_Object = MibTableColumn
mscProvCommittedFileName = _MscProvCommittedFileName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 11, 11, 1, 3),
    _MscProvCommittedFileName_Type()
)
mscProvCommittedFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscProvCommittedFileName.setStatus("mandatory")


class _MscProvCurrentViewFileName_Type(AsciiString):
    """Custom type mscProvCurrentViewFileName based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_MscProvCurrentViewFileName_Type.__name__ = "AsciiString"
_MscProvCurrentViewFileName_Object = MibTableColumn
mscProvCurrentViewFileName = _MscProvCurrentViewFileName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 11, 11, 1, 4),
    _MscProvCurrentViewFileName_Type()
)
mscProvCurrentViewFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscProvCurrentViewFileName.setStatus("mandatory")


class _MscProvLastUsedFileName_Type(AsciiString):
    """Custom type mscProvLastUsedFileName based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_MscProvLastUsedFileName_Type.__name__ = "AsciiString"
_MscProvLastUsedFileName_Object = MibTableColumn
mscProvLastUsedFileName = _MscProvLastUsedFileName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 11, 11, 1, 5),
    _MscProvLastUsedFileName_Type()
)
mscProvLastUsedFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscProvLastUsedFileName.setStatus("mandatory")
_MscProvProvisioningSession_Type = RowPointer
_MscProvProvisioningSession_Object = MibTableColumn
mscProvProvisioningSession = _MscProvProvisioningSession_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 11, 11, 1, 6),
    _MscProvProvisioningSession_Type()
)
mscProvProvisioningSession.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscProvProvisioningSession.setStatus("mandatory")


class _MscProvProvisioningUser_Type(AsciiString):
    """Custom type mscProvProvisioningUser based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_MscProvProvisioningUser_Type.__name__ = "AsciiString"
_MscProvProvisioningUser_Object = MibTableColumn
mscProvProvisioningUser = _MscProvProvisioningUser_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 11, 11, 1, 7),
    _MscProvProvisioningUser_Type()
)
mscProvProvisioningUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscProvProvisioningUser.setStatus("mandatory")


class _MscProvCheckRequired_Type(Integer32):
    """Custom type mscProvCheckRequired based on Integer32"""
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


_MscProvCheckRequired_Type.__name__ = "Integer32"
_MscProvCheckRequired_Object = MibTableColumn
mscProvCheckRequired = _MscProvCheckRequired_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 11, 11, 1, 8),
    _MscProvCheckRequired_Type()
)
mscProvCheckRequired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscProvCheckRequired.setStatus("mandatory")


class _MscProvNextFileSequenceNumber_Type(Unsigned32):
    """Custom type mscProvNextFileSequenceNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 999),
    )


_MscProvNextFileSequenceNumber_Type.__name__ = "Unsigned32"
_MscProvNextFileSequenceNumber_Object = MibTableColumn
mscProvNextFileSequenceNumber = _MscProvNextFileSequenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 11, 11, 1, 9),
    _MscProvNextFileSequenceNumber_Type()
)
mscProvNextFileSequenceNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscProvNextFileSequenceNumber.setStatus("obsolete")


class _MscProvConfirmRequired_Type(Integer32):
    """Custom type mscProvConfirmRequired based on Integer32"""
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


_MscProvConfirmRequired_Type.__name__ = "Integer32"
_MscProvConfirmRequired_Object = MibTableColumn
mscProvConfirmRequired = _MscProvConfirmRequired_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 11, 11, 1, 10),
    _MscProvConfirmRequired_Type()
)
mscProvConfirmRequired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscProvConfirmRequired.setStatus("mandatory")


class _MscProvProvisioningDirectory_Type(AsciiString):
    """Custom type mscProvProvisioningDirectory based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_MscProvProvisioningDirectory_Type.__name__ = "AsciiString"
_MscProvProvisioningDirectory_Object = MibTableColumn
mscProvProvisioningDirectory = _MscProvProvisioningDirectory_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 11, 11, 1, 11),
    _MscProvProvisioningDirectory_Type()
)
mscProvProvisioningDirectory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscProvProvisioningDirectory.setStatus("obsolete")


class _MscProvEditViewName_Type(AsciiString):
    """Custom type mscProvEditViewName based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_MscProvEditViewName_Type.__name__ = "AsciiString"
_MscProvEditViewName_Object = MibTableColumn
mscProvEditViewName = _MscProvEditViewName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 11, 11, 1, 12),
    _MscProvEditViewName_Type()
)
mscProvEditViewName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscProvEditViewName.setStatus("mandatory")


class _MscProvEditViewAddedComponents_Type(Unsigned32):
    """Custom type mscProvEditViewAddedComponents based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscProvEditViewAddedComponents_Type.__name__ = "Unsigned32"
_MscProvEditViewAddedComponents_Object = MibTableColumn
mscProvEditViewAddedComponents = _MscProvEditViewAddedComponents_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 11, 11, 1, 13),
    _MscProvEditViewAddedComponents_Type()
)
mscProvEditViewAddedComponents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscProvEditViewAddedComponents.setStatus("mandatory")


class _MscProvEditViewDeletedComponents_Type(Unsigned32):
    """Custom type mscProvEditViewDeletedComponents based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscProvEditViewDeletedComponents_Type.__name__ = "Unsigned32"
_MscProvEditViewDeletedComponents_Object = MibTableColumn
mscProvEditViewDeletedComponents = _MscProvEditViewDeletedComponents_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 11, 11, 1, 14),
    _MscProvEditViewDeletedComponents_Type()
)
mscProvEditViewDeletedComponents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscProvEditViewDeletedComponents.setStatus("mandatory")


class _MscProvEditViewChangedComponents_Type(Unsigned32):
    """Custom type mscProvEditViewChangedComponents based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscProvEditViewChangedComponents_Type.__name__ = "Unsigned32"
_MscProvEditViewChangedComponents_Object = MibTableColumn
mscProvEditViewChangedComponents = _MscProvEditViewChangedComponents_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 11, 11, 1, 15),
    _MscProvEditViewChangedComponents_Type()
)
mscProvEditViewChangedComponents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscProvEditViewChangedComponents.setStatus("mandatory")


class _MscProvStandbyCpActivity_Type(Integer32):
    """Custom type mscProvStandbyCpActivity based on Integer32"""
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


_MscProvStandbyCpActivity_Type.__name__ = "Integer32"
_MscProvStandbyCpActivity_Object = MibTableColumn
mscProvStandbyCpActivity = _MscProvStandbyCpActivity_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 11, 11, 1, 16),
    _MscProvStandbyCpActivity_Type()
)
mscProvStandbyCpActivity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscProvStandbyCpActivity.setStatus("mandatory")


class _MscProvStandbyCpActivityProgress_Type(AsciiString):
    """Custom type mscProvStandbyCpActivityProgress based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_MscProvStandbyCpActivityProgress_Type.__name__ = "AsciiString"
_MscProvStandbyCpActivityProgress_Object = MibTableColumn
mscProvStandbyCpActivityProgress = _MscProvStandbyCpActivityProgress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 11, 11, 1, 17),
    _MscProvStandbyCpActivityProgress_Type()
)
mscProvStandbyCpActivityProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscProvStandbyCpActivityProgress.setStatus("mandatory")
_ProvisioningMIB_ObjectIdentity = ObjectIdentity
provisioningMIB = _ProvisioningMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 19)
)
_ProvisioningGroup_ObjectIdentity = ObjectIdentity
provisioningGroup = _ProvisioningGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 19, 1)
)
_ProvisioningGroupCA_ObjectIdentity = ObjectIdentity
provisioningGroupCA = _ProvisioningGroupCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 19, 1, 1)
)
_ProvisioningGroupCA02_ObjectIdentity = ObjectIdentity
provisioningGroupCA02 = _ProvisioningGroupCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 19, 1, 1, 3)
)
_ProvisioningGroupCA02A_ObjectIdentity = ObjectIdentity
provisioningGroupCA02A = _ProvisioningGroupCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 19, 1, 1, 3, 2)
)
_ProvisioningCapabilities_ObjectIdentity = ObjectIdentity
provisioningCapabilities = _ProvisioningCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 19, 3)
)
_ProvisioningCapabilitiesCA_ObjectIdentity = ObjectIdentity
provisioningCapabilitiesCA = _ProvisioningCapabilitiesCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 19, 3, 1)
)
_ProvisioningCapabilitiesCA02_ObjectIdentity = ObjectIdentity
provisioningCapabilitiesCA02 = _ProvisioningCapabilitiesCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 19, 3, 1, 3)
)
_ProvisioningCapabilitiesCA02A_ObjectIdentity = ObjectIdentity
provisioningCapabilitiesCA02A = _ProvisioningCapabilitiesCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 19, 3, 1, 3, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-MsCarrier-MscPassport-ProvisioningMIB",
    **{"mscProv": mscProv,
       "mscProvRowStatusTable": mscProvRowStatusTable,
       "mscProvRowStatusEntry": mscProvRowStatusEntry,
       "mscProvRowStatus": mscProvRowStatus,
       "mscProvComponentName": mscProvComponentName,
       "mscProvStorageType": mscProvStorageType,
       "mscProvIndex": mscProvIndex,
       "mscProvView": mscProvView,
       "mscProvViewRowStatusTable": mscProvViewRowStatusTable,
       "mscProvViewRowStatusEntry": mscProvViewRowStatusEntry,
       "mscProvViewRowStatus": mscProvViewRowStatus,
       "mscProvViewComponentName": mscProvViewComponentName,
       "mscProvViewStorageType": mscProvViewStorageType,
       "mscProvViewIndex": mscProvViewIndex,
       "mscProvViewOperTable": mscProvViewOperTable,
       "mscProvViewOperEntry": mscProvViewOperEntry,
       "mscProvViewUser": mscProvViewUser,
       "mscProvViewCheckState": mscProvViewCheckState,
       "mscProvViewComponents": mscProvViewComponents,
       "mscProvViewFormats": mscProvViewFormats,
       "mscProvViewBaseView": mscProvViewBaseView,
       "mscProvViewVersion": mscProvViewVersion,
       "mscProvViewCreationDate": mscProvViewCreationDate,
       "mscProvStateTable": mscProvStateTable,
       "mscProvStateEntry": mscProvStateEntry,
       "mscProvAdminState": mscProvAdminState,
       "mscProvOperationalState": mscProvOperationalState,
       "mscProvUsageState": mscProvUsageState,
       "mscProvOperTable": mscProvOperTable,
       "mscProvOperEntry": mscProvOperEntry,
       "mscProvProvisioningActivity": mscProvProvisioningActivity,
       "mscProvActivityProgress": mscProvActivityProgress,
       "mscProvCommittedFileName": mscProvCommittedFileName,
       "mscProvCurrentViewFileName": mscProvCurrentViewFileName,
       "mscProvLastUsedFileName": mscProvLastUsedFileName,
       "mscProvProvisioningSession": mscProvProvisioningSession,
       "mscProvProvisioningUser": mscProvProvisioningUser,
       "mscProvCheckRequired": mscProvCheckRequired,
       "mscProvNextFileSequenceNumber": mscProvNextFileSequenceNumber,
       "mscProvConfirmRequired": mscProvConfirmRequired,
       "mscProvProvisioningDirectory": mscProvProvisioningDirectory,
       "mscProvEditViewName": mscProvEditViewName,
       "mscProvEditViewAddedComponents": mscProvEditViewAddedComponents,
       "mscProvEditViewDeletedComponents": mscProvEditViewDeletedComponents,
       "mscProvEditViewChangedComponents": mscProvEditViewChangedComponents,
       "mscProvStandbyCpActivity": mscProvStandbyCpActivity,
       "mscProvStandbyCpActivityProgress": mscProvStandbyCpActivityProgress,
       "provisioningMIB": provisioningMIB,
       "provisioningGroup": provisioningGroup,
       "provisioningGroupCA": provisioningGroupCA,
       "provisioningGroupCA02": provisioningGroupCA02,
       "provisioningGroupCA02A": provisioningGroupCA02A,
       "provisioningCapabilities": provisioningCapabilities,
       "provisioningCapabilitiesCA": provisioningCapabilitiesCA,
       "provisioningCapabilitiesCA02": provisioningCapabilitiesCA02,
       "provisioningCapabilitiesCA02A": provisioningCapabilitiesCA02A}
)
