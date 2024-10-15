# SNMP MIB module (INTELCORPORATIONSERVERHEALTH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/INTELCORPORATIONSERVERHEALTH-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:10:18 2024
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
 NotificationType,
 TimeTicks,
 Unsigned32,
 enterprises,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class DmiInteger(Integer32):
    """Custom type DmiInteger based on Integer32"""




class DmiDisplaystring(DisplayString):
    """Custom type DmiDisplaystring based on DisplayString"""




class DmiDateX(OctetString):
    """Custom type DmiDateX based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(28, 28),
    )





class DmiComponentIndex(Integer32):
    """Custom type DmiComponentIndex based on Integer32"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Intel_ObjectIdentity = ObjectIdentity
intel = _Intel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 2)
)
_Server_management_ObjectIdentity = ObjectIdentity
server_management = _Server_management_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 2, 10)
)
_Software_ObjectIdentity = ObjectIdentity
software = _Software_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 2, 10, 3)
)
_Sha_ObjectIdentity = ObjectIdentity
sha = _Sha_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 2)
)
_DmtfGroups_ObjectIdentity = ObjectIdentity
dmtfGroups = _DmtfGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 2, 1)
)
_TComponentid_Object = MibTable
tComponentid = _TComponentid_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 2, 1, 1)
)
if mibBuilder.loadTexts:
    tComponentid.setStatus("mandatory")
_EComponentid_Object = MibTableRow
eComponentid = _EComponentid_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 2, 1, 1, 1)
)
eComponentid.setIndexNames(
    (0, "INTELCORPORATIONSERVERHEALTH-MIB", "DmiComponentIndex"),
)
if mibBuilder.loadTexts:
    eComponentid.setStatus("mandatory")
_A1Manufacturer_Type = DmiDisplaystring
_A1Manufacturer_Object = MibTableColumn
a1Manufacturer = _A1Manufacturer_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 2, 1, 1, 1, 1),
    _A1Manufacturer_Type()
)
a1Manufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1Manufacturer.setStatus("mandatory")
_A1Product_Type = DmiDisplaystring
_A1Product_Object = MibTableColumn
a1Product = _A1Product_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 2, 1, 1, 1, 2),
    _A1Product_Type()
)
a1Product.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1Product.setStatus("mandatory")
_A1Version_Type = DmiDisplaystring
_A1Version_Object = MibTableColumn
a1Version = _A1Version_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 2, 1, 1, 1, 3),
    _A1Version_Type()
)
a1Version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1Version.setStatus("mandatory")
_A1SerialNumber_Type = DmiDisplaystring
_A1SerialNumber_Object = MibTableColumn
a1SerialNumber = _A1SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 2, 1, 1, 1, 4),
    _A1SerialNumber_Type()
)
a1SerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1SerialNumber.setStatus("mandatory")
_A1Installation_Type = DmiDateX
_A1Installation_Object = MibTableColumn
a1Installation = _A1Installation_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 2, 1, 1, 1, 5),
    _A1Installation_Type()
)
a1Installation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1Installation.setStatus("mandatory")


class _A1Verify_Type(Integer32):
    """Custom type a1Verify based on Integer32"""
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
        *(("vAnErrorOccurredCheckStatusCode", 0),
          ("vReserved", 3),
          ("vThisComponentDoesNotExist", 1),
          ("vThisComponentExistsAndIsFunctioningCorr", 7),
          ("vThisComponentExistsAndIsNotFunctioningC", 6),
          ("vThisComponentExistsButTheFunctionality1", 5),
          ("vThisComponentExistsButTheFunctionalityI", 4),
          ("vVerificationIsNotSupported", 2))
    )


_A1Verify_Type.__name__ = "Integer32"
_A1Verify_Object = MibTableColumn
a1Verify = _A1Verify_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 2, 1, 1, 1, 6),
    _A1Verify_Type()
)
a1Verify.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1Verify.setStatus("mandatory")
_TServerHealthContributionTable_Object = MibTable
tServerHealthContributionTable = _TServerHealthContributionTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 2, 1, 2)
)
if mibBuilder.loadTexts:
    tServerHealthContributionTable.setStatus("mandatory")
_EServerHealthContributionTable_Object = MibTableRow
eServerHealthContributionTable = _EServerHealthContributionTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 2, 1, 2, 1)
)
eServerHealthContributionTable.setIndexNames(
    (0, "INTELCORPORATIONSERVERHEALTH-MIB", "DmiComponentIndex"),
    (0, "INTELCORPORATIONSERVERHEALTH-MIB", "a2ContributionTableIndex"),
)
if mibBuilder.loadTexts:
    eServerHealthContributionTable.setStatus("mandatory")
_A2ContributionTableIndex_Type = DmiInteger
_A2ContributionTableIndex_Object = MibTableColumn
a2ContributionTableIndex = _A2ContributionTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 2, 1, 2, 1, 1),
    _A2ContributionTableIndex_Type()
)
a2ContributionTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2ContributionTableIndex.setStatus("mandatory")
_A2Component_Type = DmiDisplaystring
_A2Component_Object = MibTableColumn
a2Component = _A2Component_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 2, 1, 2, 1, 2),
    _A2Component_Type()
)
a2Component.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2Component.setStatus("mandatory")
_A2Group_Type = DmiDisplaystring
_A2Group_Object = MibTableColumn
a2Group = _A2Group_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 2, 1, 2, 1, 3),
    _A2Group_Type()
)
a2Group.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2Group.setStatus("mandatory")


class _A2StatusStore_Type(Integer32):
    """Custom type a2StatusStore based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("vErrorControl", 2),
          ("vLocal", 0),
          ("vOperationalState", 1))
    )


_A2StatusStore_Type.__name__ = "Integer32"
_A2StatusStore_Object = MibTableColumn
a2StatusStore = _A2StatusStore_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 2, 1, 2, 1, 4),
    _A2StatusStore_Type()
)
a2StatusStore.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2StatusStore.setStatus("mandatory")
_A2LocalIndexAttributeIdToStoreGroup_Type = DmiInteger
_A2LocalIndexAttributeIdToStoreGroup_Object = MibTableColumn
a2LocalIndexAttributeIdToStoreGroup = _A2LocalIndexAttributeIdToStoreGroup_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 2, 1, 2, 1, 5),
    _A2LocalIndexAttributeIdToStoreGroup_Type()
)
a2LocalIndexAttributeIdToStoreGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2LocalIndexAttributeIdToStoreGroup.setStatus("mandatory")
_A2HealthAttributeId_Type = DmiInteger
_A2HealthAttributeId_Object = MibTableColumn
a2HealthAttributeId = _A2HealthAttributeId_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 2, 1, 2, 1, 6),
    _A2HealthAttributeId_Type()
)
a2HealthAttributeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2HealthAttributeId.setStatus("mandatory")


class _A2Contribution_Type(Integer32):
    """Custom type a2Contribution based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("vFalse", 0),
          ("vTrue", 1))
    )


_A2Contribution_Type.__name__ = "Integer32"
_A2Contribution_Object = MibTableColumn
a2Contribution = _A2Contribution_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 2, 1, 2, 1, 7),
    _A2Contribution_Type()
)
a2Contribution.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a2Contribution.setStatus("mandatory")


class _A2UpdateThroughPolling_Type(Integer32):
    """Custom type a2UpdateThroughPolling based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("vFalse", 0),
          ("vTrue", 1))
    )


_A2UpdateThroughPolling_Type.__name__ = "Integer32"
_A2UpdateThroughPolling_Object = MibTableColumn
a2UpdateThroughPolling = _A2UpdateThroughPolling_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 2, 1, 2, 1, 8),
    _A2UpdateThroughPolling_Type()
)
a2UpdateThroughPolling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a2UpdateThroughPolling.setStatus("mandatory")
_TServerHealthFilterTable_Object = MibTable
tServerHealthFilterTable = _TServerHealthFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 2, 1, 3)
)
if mibBuilder.loadTexts:
    tServerHealthFilterTable.setStatus("mandatory")
_EServerHealthFilterTable_Object = MibTableRow
eServerHealthFilterTable = _EServerHealthFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 2, 1, 3, 1)
)
eServerHealthFilterTable.setIndexNames(
    (0, "INTELCORPORATIONSERVERHEALTH-MIB", "DmiComponentIndex"),
    (0, "INTELCORPORATIONSERVERHEALTH-MIB", "a3FilterTableIndex"),
)
if mibBuilder.loadTexts:
    eServerHealthFilterTable.setStatus("mandatory")
_A3FilterTableIndex_Type = DmiInteger
_A3FilterTableIndex_Object = MibTableColumn
a3FilterTableIndex = _A3FilterTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 2, 1, 3, 1, 1),
    _A3FilterTableIndex_Type()
)
a3FilterTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3FilterTableIndex.setStatus("mandatory")
_A3Component_Type = DmiDisplaystring
_A3Component_Object = MibTableColumn
a3Component = _A3Component_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 2, 1, 3, 1, 2),
    _A3Component_Type()
)
a3Component.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3Component.setStatus("mandatory")
_A3Group_Type = DmiDisplaystring
_A3Group_Object = MibTableColumn
a3Group = _A3Group_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 2, 1, 3, 1, 3),
    _A3Group_Type()
)
a3Group.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3Group.setStatus("mandatory")
_TServerHealthStatus_Object = MibTable
tServerHealthStatus = _TServerHealthStatus_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 2, 1, 4)
)
if mibBuilder.loadTexts:
    tServerHealthStatus.setStatus("mandatory")
_EServerHealthStatus_Object = MibTableRow
eServerHealthStatus = _EServerHealthStatus_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 2, 1, 4, 1)
)
eServerHealthStatus.setIndexNames(
    (0, "INTELCORPORATIONSERVERHEALTH-MIB", "DmiComponentIndex"),
)
if mibBuilder.loadTexts:
    eServerHealthStatus.setStatus("mandatory")


class _A4Status_Type(Integer32):
    """Custom type a4Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16,
              32)
        )
    )
    namedValues = NamedValues(
        *(("vCritical", 16),
          ("vNon-critical", 8),
          ("vNon-recoverable", 32),
          ("vOk", 4),
          ("vOther", 1),
          ("vUnknown", 2))
    )


_A4Status_Type.__name__ = "Integer32"
_A4Status_Object = MibTableColumn
a4Status = _A4Status_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 2, 1, 4, 1, 1),
    _A4Status_Type()
)
a4Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a4Status.setStatus("mandatory")
_A4StatusInInteger_Type = DmiInteger
_A4StatusInInteger_Object = MibTableColumn
a4StatusInInteger = _A4StatusInInteger_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 2, 1, 4, 1, 2),
    _A4StatusInInteger_Type()
)
a4StatusInInteger.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a4StatusInInteger.setStatus("mandatory")
_A4PollInterval_Type = DmiInteger
_A4PollInterval_Object = MibTableColumn
a4PollInterval = _A4PollInterval_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 2, 1, 4, 1, 3),
    _A4PollInterval_Type()
)
a4PollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a4PollInterval.setStatus("mandatory")
_TEventGenerationForServerHealthStatus_Object = MibTable
tEventGenerationForServerHealthStatus = _TEventGenerationForServerHealthStatus_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 2, 1, 5)
)
if mibBuilder.loadTexts:
    tEventGenerationForServerHealthStatus.setStatus("mandatory")
_EEventGenerationForServerHealthStatus_Object = MibTableRow
eEventGenerationForServerHealthStatus = _EEventGenerationForServerHealthStatus_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 2, 1, 5, 1)
)
eEventGenerationForServerHealthStatus.setIndexNames(
    (0, "INTELCORPORATIONSERVERHEALTH-MIB", "DmiComponentIndex"),
    (0, "INTELCORPORATIONSERVERHEALTH-MIB", "a5AssociatedGroup"),
)
if mibBuilder.loadTexts:
    eEventGenerationForServerHealthStatus.setStatus("mandatory")


class _A5EventType_Type(Integer32):
    """Custom type a5EventType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(4,
              8,
              16,
              32,
              48,
              64)
        )
    )
    namedValues = NamedValues(
        *(("vServerCritical", 16),
          ("vServerHealthDetailChanged", 48),
          ("vServerHealthDetailRefresh", 64),
          ("vServerNon-critical", 8),
          ("vServerNon-recoverable", 32),
          ("vServerOk", 4))
    )


_A5EventType_Type.__name__ = "Integer32"
_A5EventType_Object = MibTableColumn
a5EventType = _A5EventType_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 2, 1, 5, 1, 1),
    _A5EventType_Type()
)
a5EventType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a5EventType.setStatus("mandatory")


class _A5EventSeverity_Type(Integer32):
    """Custom type a5EventSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16,
              32)
        )
    )
    namedValues = NamedValues(
        *(("vCritical", 16),
          ("vInformation", 2),
          ("vMonitor", 1),
          ("vNon-critical", 8),
          ("vNon-recoverable", 32),
          ("vOk", 4))
    )


_A5EventSeverity_Type.__name__ = "Integer32"
_A5EventSeverity_Object = MibTableColumn
a5EventSeverity = _A5EventSeverity_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 2, 1, 5, 1, 2),
    _A5EventSeverity_Type()
)
a5EventSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a5EventSeverity.setStatus("mandatory")


class _A5IsEventState_based_Type(Integer32):
    """Custom type a5IsEventState_based based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("vFalse", 0),
          ("vTrue", 1))
    )


_A5IsEventState_based_Type.__name__ = "Integer32"
_A5IsEventState_based_Object = MibScalar
a5IsEventState_based = _A5IsEventState_based_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 2, 1, 5, 1, 3),
    _A5IsEventState_based_Type()
)
a5IsEventState_based.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a5IsEventState_based.setStatus("mandatory")
_A5EventStateKey_Type = DmiInteger
_A5EventStateKey_Object = MibTableColumn
a5EventStateKey = _A5EventStateKey_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 2, 1, 5, 1, 4),
    _A5EventStateKey_Type()
)
a5EventStateKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a5EventStateKey.setStatus("mandatory")
_A5AssociatedGroup_Type = DmiDisplaystring
_A5AssociatedGroup_Object = MibTableColumn
a5AssociatedGroup = _A5AssociatedGroup_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 2, 1, 5, 1, 5),
    _A5AssociatedGroup_Type()
)
a5AssociatedGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a5AssociatedGroup.setStatus("mandatory")


class _A5EventSystem_Type(Integer32):
    """Custom type a5EventSystem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("vOther", 0),
          ("vUnknown", 1))
    )


_A5EventSystem_Type.__name__ = "Integer32"
_A5EventSystem_Object = MibTableColumn
a5EventSystem = _A5EventSystem_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 2, 1, 5, 1, 6),
    _A5EventSystem_Type()
)
a5EventSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a5EventSystem.setStatus("mandatory")


class _A5EventSubsystem_Type(Integer32):
    """Custom type a5EventSubsystem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("vOther", 0),
          ("vUnknown", 1))
    )


_A5EventSubsystem_Type.__name__ = "Integer32"
_A5EventSubsystem_Object = MibTableColumn
a5EventSubsystem = _A5EventSubsystem_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 2, 1, 5, 1, 7),
    _A5EventSubsystem_Type()
)
a5EventSubsystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a5EventSubsystem.setStatus("mandatory")


class _A5IsInstanceDataPresent_Type(Integer32):
    """Custom type a5IsInstanceDataPresent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("vFalse", 0),
          ("vTrue", 1))
    )


_A5IsInstanceDataPresent_Type.__name__ = "Integer32"
_A5IsInstanceDataPresent_Object = MibTableColumn
a5IsInstanceDataPresent = _A5IsInstanceDataPresent_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 2, 1, 5, 1, 9),
    _A5IsInstanceDataPresent_Type()
)
a5IsInstanceDataPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a5IsInstanceDataPresent.setStatus("mandatory")
_A5EventMessage_Type = DmiDisplaystring
_A5EventMessage_Object = MibTableColumn
a5EventMessage = _A5EventMessage_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 2, 1, 5, 1, 10),
    _A5EventMessage_Type()
)
a5EventMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a5EventMessage.setStatus("mandatory")
_TServerHealthDetail_Object = MibTable
tServerHealthDetail = _TServerHealthDetail_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 2, 1, 6)
)
if mibBuilder.loadTexts:
    tServerHealthDetail.setStatus("mandatory")
_EServerHealthDetail_Object = MibTableRow
eServerHealthDetail = _EServerHealthDetail_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 2, 1, 6, 1)
)
eServerHealthDetail.setIndexNames(
    (0, "INTELCORPORATIONSERVERHEALTH-MIB", "DmiComponentIndex"),
    (0, "INTELCORPORATIONSERVERHEALTH-MIB", "a6HealthInstanceIndex"),
)
if mibBuilder.loadTexts:
    eServerHealthDetail.setStatus("mandatory")
_A6HealthInstanceIndex_Type = DmiInteger
_A6HealthInstanceIndex_Object = MibTableColumn
a6HealthInstanceIndex = _A6HealthInstanceIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 2, 1, 6, 1, 1),
    _A6HealthInstanceIndex_Type()
)
a6HealthInstanceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a6HealthInstanceIndex.setStatus("mandatory")
_A6Component_Type = DmiDisplaystring
_A6Component_Object = MibTableColumn
a6Component = _A6Component_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 2, 1, 6, 1, 2),
    _A6Component_Type()
)
a6Component.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a6Component.setStatus("mandatory")
_A6Group_Type = DmiDisplaystring
_A6Group_Object = MibTableColumn
a6Group = _A6Group_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 2, 1, 6, 1, 3),
    _A6Group_Type()
)
a6Group.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a6Group.setStatus("mandatory")
_A6InstancePath_Type = DmiDisplaystring
_A6InstancePath_Object = MibTableColumn
a6InstancePath = _A6InstancePath_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 2, 1, 6, 1, 4),
    _A6InstancePath_Type()
)
a6InstancePath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a6InstancePath.setStatus("mandatory")
_A6LastEventType_Type = DmiInteger
_A6LastEventType_Object = MibTableColumn
a6LastEventType = _A6LastEventType_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 2, 1, 6, 1, 5),
    _A6LastEventType_Type()
)
a6LastEventType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a6LastEventType.setStatus("mandatory")


class _A6Status_Type(Integer32):
    """Custom type a6Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16,
              32)
        )
    )
    namedValues = NamedValues(
        *(("vCritical", 16),
          ("vNon-critical", 8),
          ("vNon-recoverable", 32),
          ("vOk", 4),
          ("vOther", 1),
          ("vUnknown", 2))
    )


_A6Status_Type.__name__ = "Integer32"
_A6Status_Object = MibTableColumn
a6Status = _A6Status_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 2, 1, 6, 1, 6),
    _A6Status_Type()
)
a6Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a6Status.setStatus("mandatory")
_TMiftomib_Object = MibTable
tMiftomib = _TMiftomib_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 2, 1, 99)
)
if mibBuilder.loadTexts:
    tMiftomib.setStatus("mandatory")
_EMiftomib_Object = MibTableRow
eMiftomib = _EMiftomib_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 2, 1, 99, 1)
)
eMiftomib.setIndexNames(
    (0, "INTELCORPORATIONSERVERHEALTH-MIB", "DmiComponentIndex"),
)
if mibBuilder.loadTexts:
    eMiftomib.setStatus("mandatory")
_A99MibName_Type = DmiDisplaystring
_A99MibName_Object = MibTableColumn
a99MibName = _A99MibName_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 2, 1, 99, 1, 1),
    _A99MibName_Type()
)
a99MibName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a99MibName.setStatus("mandatory")
_A99MibOid_Type = DmiDisplaystring
_A99MibOid_Object = MibTableColumn
a99MibOid = _A99MibOid_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 2, 1, 99, 1, 2),
    _A99MibOid_Type()
)
a99MibOid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a99MibOid.setStatus("mandatory")
_A99DisableTrap_Type = DmiInteger
_A99DisableTrap_Object = MibTableColumn
a99DisableTrap = _A99DisableTrap_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 2, 1, 99, 1, 3),
    _A99DisableTrap_Type()
)
a99DisableTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a99DisableTrap.setStatus("mandatory")

# Managed Objects groups


# Notification objects

trap1ForServerHealthStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 2, 1, 5, 1, 0, 4)
)
trap1ForServerHealthStatus.setObjects(
      *(("INTELCORPORATIONSERVERHEALTH-MIB", "a5EventType"),
        ("INTELCORPORATIONSERVERHEALTH-MIB", "a5EventSeverity"),
        ("INTELCORPORATIONSERVERHEALTH-MIB", "a5IsEventState_based"),
        ("INTELCORPORATIONSERVERHEALTH-MIB", "a5EventStateKey"),
        ("INTELCORPORATIONSERVERHEALTH-MIB", "a5AssociatedGroup"),
        ("INTELCORPORATIONSERVERHEALTH-MIB", "a5EventSystem"),
        ("INTELCORPORATIONSERVERHEALTH-MIB", "a5EventSubsystem"),
        ("INTELCORPORATIONSERVERHEALTH-MIB", "a5IsInstanceDataPresent"),
        ("INTELCORPORATIONSERVERHEALTH-MIB", "a5EventMessage"))
)
if mibBuilder.loadTexts:
    trap1ForServerHealthStatus.setStatus(
        ""
    )

trap2ForServerHealthStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 2, 1, 5, 1, 0, 8)
)
trap2ForServerHealthStatus.setObjects(
      *(("INTELCORPORATIONSERVERHEALTH-MIB", "a5EventType"),
        ("INTELCORPORATIONSERVERHEALTH-MIB", "a5EventSeverity"),
        ("INTELCORPORATIONSERVERHEALTH-MIB", "a5IsEventState_based"),
        ("INTELCORPORATIONSERVERHEALTH-MIB", "a5EventStateKey"),
        ("INTELCORPORATIONSERVERHEALTH-MIB", "a5AssociatedGroup"),
        ("INTELCORPORATIONSERVERHEALTH-MIB", "a5EventSystem"),
        ("INTELCORPORATIONSERVERHEALTH-MIB", "a5EventSubsystem"),
        ("INTELCORPORATIONSERVERHEALTH-MIB", "a5IsInstanceDataPresent"),
        ("INTELCORPORATIONSERVERHEALTH-MIB", "a5EventMessage"))
)
if mibBuilder.loadTexts:
    trap2ForServerHealthStatus.setStatus(
        ""
    )

trap3ForServerHealthStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 2, 1, 5, 1, 0, 16)
)
trap3ForServerHealthStatus.setObjects(
      *(("INTELCORPORATIONSERVERHEALTH-MIB", "a5EventType"),
        ("INTELCORPORATIONSERVERHEALTH-MIB", "a5EventSeverity"),
        ("INTELCORPORATIONSERVERHEALTH-MIB", "a5IsEventState_based"),
        ("INTELCORPORATIONSERVERHEALTH-MIB", "a5EventStateKey"),
        ("INTELCORPORATIONSERVERHEALTH-MIB", "a5AssociatedGroup"),
        ("INTELCORPORATIONSERVERHEALTH-MIB", "a5EventSystem"),
        ("INTELCORPORATIONSERVERHEALTH-MIB", "a5EventSubsystem"),
        ("INTELCORPORATIONSERVERHEALTH-MIB", "a5IsInstanceDataPresent"),
        ("INTELCORPORATIONSERVERHEALTH-MIB", "a5EventMessage"))
)
if mibBuilder.loadTexts:
    trap3ForServerHealthStatus.setStatus(
        ""
    )

trap4ForServerHealthStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 2, 1, 5, 1, 0, 32)
)
trap4ForServerHealthStatus.setObjects(
      *(("INTELCORPORATIONSERVERHEALTH-MIB", "a5EventType"),
        ("INTELCORPORATIONSERVERHEALTH-MIB", "a5EventSeverity"),
        ("INTELCORPORATIONSERVERHEALTH-MIB", "a5IsEventState_based"),
        ("INTELCORPORATIONSERVERHEALTH-MIB", "a5EventStateKey"),
        ("INTELCORPORATIONSERVERHEALTH-MIB", "a5AssociatedGroup"),
        ("INTELCORPORATIONSERVERHEALTH-MIB", "a5EventSystem"),
        ("INTELCORPORATIONSERVERHEALTH-MIB", "a5EventSubsystem"),
        ("INTELCORPORATIONSERVERHEALTH-MIB", "a5IsInstanceDataPresent"),
        ("INTELCORPORATIONSERVERHEALTH-MIB", "a5EventMessage"))
)
if mibBuilder.loadTexts:
    trap4ForServerHealthStatus.setStatus(
        ""
    )

trap5ForServerHealthStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 2, 1, 5, 1, 0, 48)
)
trap5ForServerHealthStatus.setObjects(
      *(("INTELCORPORATIONSERVERHEALTH-MIB", "a5EventType"),
        ("INTELCORPORATIONSERVERHEALTH-MIB", "a5EventSeverity"),
        ("INTELCORPORATIONSERVERHEALTH-MIB", "a5IsEventState_based"),
        ("INTELCORPORATIONSERVERHEALTH-MIB", "a5EventStateKey"),
        ("INTELCORPORATIONSERVERHEALTH-MIB", "a5AssociatedGroup"),
        ("INTELCORPORATIONSERVERHEALTH-MIB", "a5EventSystem"),
        ("INTELCORPORATIONSERVERHEALTH-MIB", "a5EventSubsystem"),
        ("INTELCORPORATIONSERVERHEALTH-MIB", "a5IsInstanceDataPresent"),
        ("INTELCORPORATIONSERVERHEALTH-MIB", "a5EventMessage"))
)
if mibBuilder.loadTexts:
    trap5ForServerHealthStatus.setStatus(
        ""
    )

trap6ForServerHealthStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 2, 1, 5, 1, 0, 64)
)
trap6ForServerHealthStatus.setObjects(
      *(("INTELCORPORATIONSERVERHEALTH-MIB", "a5EventType"),
        ("INTELCORPORATIONSERVERHEALTH-MIB", "a5EventSeverity"),
        ("INTELCORPORATIONSERVERHEALTH-MIB", "a5IsEventState_based"),
        ("INTELCORPORATIONSERVERHEALTH-MIB", "a5EventStateKey"),
        ("INTELCORPORATIONSERVERHEALTH-MIB", "a5AssociatedGroup"),
        ("INTELCORPORATIONSERVERHEALTH-MIB", "a5EventSystem"),
        ("INTELCORPORATIONSERVERHEALTH-MIB", "a5EventSubsystem"),
        ("INTELCORPORATIONSERVERHEALTH-MIB", "a5IsInstanceDataPresent"),
        ("INTELCORPORATIONSERVERHEALTH-MIB", "a5EventMessage"))
)
if mibBuilder.loadTexts:
    trap6ForServerHealthStatus.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INTELCORPORATIONSERVERHEALTH-MIB",
    **{"DmiInteger": DmiInteger,
       "DmiDisplaystring": DmiDisplaystring,
       "DmiDateX": DmiDateX,
       "DmiComponentIndex": DmiComponentIndex,
       "intel": intel,
       "products": products,
       "server-management": server_management,
       "software": software,
       "sha": sha,
       "dmtfGroups": dmtfGroups,
       "tComponentid": tComponentid,
       "eComponentid": eComponentid,
       "a1Manufacturer": a1Manufacturer,
       "a1Product": a1Product,
       "a1Version": a1Version,
       "a1SerialNumber": a1SerialNumber,
       "a1Installation": a1Installation,
       "a1Verify": a1Verify,
       "tServerHealthContributionTable": tServerHealthContributionTable,
       "eServerHealthContributionTable": eServerHealthContributionTable,
       "a2ContributionTableIndex": a2ContributionTableIndex,
       "a2Component": a2Component,
       "a2Group": a2Group,
       "a2StatusStore": a2StatusStore,
       "a2LocalIndexAttributeIdToStoreGroup": a2LocalIndexAttributeIdToStoreGroup,
       "a2HealthAttributeId": a2HealthAttributeId,
       "a2Contribution": a2Contribution,
       "a2UpdateThroughPolling": a2UpdateThroughPolling,
       "tServerHealthFilterTable": tServerHealthFilterTable,
       "eServerHealthFilterTable": eServerHealthFilterTable,
       "a3FilterTableIndex": a3FilterTableIndex,
       "a3Component": a3Component,
       "a3Group": a3Group,
       "tServerHealthStatus": tServerHealthStatus,
       "eServerHealthStatus": eServerHealthStatus,
       "a4Status": a4Status,
       "a4StatusInInteger": a4StatusInInteger,
       "a4PollInterval": a4PollInterval,
       "tEventGenerationForServerHealthStatus": tEventGenerationForServerHealthStatus,
       "eEventGenerationForServerHealthStatus": eEventGenerationForServerHealthStatus,
       "trap1ForServerHealthStatus": trap1ForServerHealthStatus,
       "trap2ForServerHealthStatus": trap2ForServerHealthStatus,
       "trap3ForServerHealthStatus": trap3ForServerHealthStatus,
       "trap4ForServerHealthStatus": trap4ForServerHealthStatus,
       "trap5ForServerHealthStatus": trap5ForServerHealthStatus,
       "trap6ForServerHealthStatus": trap6ForServerHealthStatus,
       "a5EventType": a5EventType,
       "a5EventSeverity": a5EventSeverity,
       "a5IsEventState-based": a5IsEventState_based,
       "a5EventStateKey": a5EventStateKey,
       "a5AssociatedGroup": a5AssociatedGroup,
       "a5EventSystem": a5EventSystem,
       "a5EventSubsystem": a5EventSubsystem,
       "a5IsInstanceDataPresent": a5IsInstanceDataPresent,
       "a5EventMessage": a5EventMessage,
       "tServerHealthDetail": tServerHealthDetail,
       "eServerHealthDetail": eServerHealthDetail,
       "a6HealthInstanceIndex": a6HealthInstanceIndex,
       "a6Component": a6Component,
       "a6Group": a6Group,
       "a6InstancePath": a6InstancePath,
       "a6LastEventType": a6LastEventType,
       "a6Status": a6Status,
       "tMiftomib": tMiftomib,
       "eMiftomib": eMiftomib,
       "a99MibName": a99MibName,
       "a99MibOid": a99MibOid,
       "a99DisableTrap": a99DisableTrap}
)
