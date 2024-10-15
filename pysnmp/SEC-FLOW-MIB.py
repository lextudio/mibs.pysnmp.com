# SNMP MIB module (SEC-FLOW-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SEC-FLOW-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:50:13 2024
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

(nbSwitchG1,) = mibBuilder.importSymbols(
    "NBASE-G1-MIB",
    "nbSwitchG1")

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



class MacAddress(OctetString):
    """Custom type MacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NbSwitchG1Il_ObjectIdentity = ObjectIdentity
nbSwitchG1Il = _NbSwitchG1Il_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50)
)
_NbsAccelerouter_ObjectIdentity = ObjectIdentity
nbsAccelerouter = _NbsAccelerouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 10)
)
_NbsArSecFlow_ObjectIdentity = ObjectIdentity
nbsArSecFlow = _NbsArSecFlow_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 10, 8)
)
_NbsArSecFlowTable_Object = MibTable
nbsArSecFlowTable = _NbsArSecFlowTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 10, 8, 1)
)
if mibBuilder.loadTexts:
    nbsArSecFlowTable.setStatus("mandatory")
_NbsArSecFlowEntry_Object = MibTableRow
nbsArSecFlowEntry = _NbsArSecFlowEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 10, 8, 1, 1)
)
nbsArSecFlowEntry.setIndexNames(
    (0, "SEC-FLOW-MIB", "nbsArSecFlowIndex"),
)
if mibBuilder.loadTexts:
    nbsArSecFlowEntry.setStatus("mandatory")


class _NbsArSecFlowIndex_Type(Integer32):
    """Custom type nbsArSecFlowIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_NbsArSecFlowIndex_Type.__name__ = "Integer32"
_NbsArSecFlowIndex_Object = MibTableColumn
nbsArSecFlowIndex = _NbsArSecFlowIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 10, 8, 1, 1, 1),
    _NbsArSecFlowIndex_Type()
)
nbsArSecFlowIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsArSecFlowIndex.setStatus("mandatory")
_NbsArSecFlowValid_Type = Integer32
_NbsArSecFlowValid_Object = MibTableColumn
nbsArSecFlowValid = _NbsArSecFlowValid_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 10, 8, 1, 1, 2),
    _NbsArSecFlowValid_Type()
)
nbsArSecFlowValid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsArSecFlowValid.setStatus("mandatory")
_NbsArSecFlowState_Type = Integer32
_NbsArSecFlowState_Object = MibTableColumn
nbsArSecFlowState = _NbsArSecFlowState_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 10, 8, 1, 1, 3),
    _NbsArSecFlowState_Type()
)
nbsArSecFlowState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsArSecFlowState.setStatus("mandatory")


class _NbsArSecFlowLastUsedTimestamp_Type(Integer32):
    """Custom type nbsArSecFlowLastUsedTimestamp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_NbsArSecFlowLastUsedTimestamp_Type.__name__ = "Integer32"
_NbsArSecFlowLastUsedTimestamp_Object = MibTableColumn
nbsArSecFlowLastUsedTimestamp = _NbsArSecFlowLastUsedTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 10, 8, 1, 1, 4),
    _NbsArSecFlowLastUsedTimestamp_Type()
)
nbsArSecFlowLastUsedTimestamp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsArSecFlowLastUsedTimestamp.setStatus("mandatory")
_NbsArSecFlowServTypes_Type = Integer32
_NbsArSecFlowServTypes_Object = MibTableColumn
nbsArSecFlowServTypes = _NbsArSecFlowServTypes_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 10, 8, 1, 1, 5),
    _NbsArSecFlowServTypes_Type()
)
nbsArSecFlowServTypes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsArSecFlowServTypes.setStatus("mandatory")
_NbsArSecFlowServId_Type = Integer32
_NbsArSecFlowServId_Object = MibTableColumn
nbsArSecFlowServId = _NbsArSecFlowServId_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 10, 8, 1, 1, 6),
    _NbsArSecFlowServId_Type()
)
nbsArSecFlowServId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsArSecFlowServId.setStatus("mandatory")
_NbsArFlowID_Type = OctetString
_NbsArFlowID_Object = MibTableColumn
nbsArFlowID = _NbsArFlowID_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 10, 8, 1, 1, 7),
    _NbsArFlowID_Type()
)
nbsArFlowID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsArFlowID.setStatus("mandatory")
_NbsArFlowQoSSpec_Type = OctetString
_NbsArFlowQoSSpec_Object = MibTableColumn
nbsArFlowQoSSpec = _NbsArFlowQoSSpec_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 10, 8, 1, 1, 8),
    _NbsArFlowQoSSpec_Type()
)
nbsArFlowQoSSpec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsArFlowQoSSpec.setStatus("mandatory")


class _NbsArSecFlowNumOfServices_Type(Integer32):
    """Custom type nbsArSecFlowNumOfServices based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_NbsArSecFlowNumOfServices_Type.__name__ = "Integer32"
_NbsArSecFlowNumOfServices_Object = MibTableColumn
nbsArSecFlowNumOfServices = _NbsArSecFlowNumOfServices_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 10, 8, 1, 1, 9),
    _NbsArSecFlowNumOfServices_Type()
)
nbsArSecFlowNumOfServices.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsArSecFlowNumOfServices.setStatus("mandatory")
_NbsArSecFlowDriverData_Type = OctetString
_NbsArSecFlowDriverData_Object = MibTableColumn
nbsArSecFlowDriverData = _NbsArSecFlowDriverData_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 10, 8, 1, 1, 10),
    _NbsArSecFlowDriverData_Type()
)
nbsArSecFlowDriverData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsArSecFlowDriverData.setStatus("mandatory")
_NbsArSecFlowActions_Type = OctetString
_NbsArSecFlowActions_Object = MibTableColumn
nbsArSecFlowActions = _NbsArSecFlowActions_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 10, 8, 1, 1, 11),
    _NbsArSecFlowActions_Type()
)
nbsArSecFlowActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsArSecFlowActions.setStatus("mandatory")
_NbsArSecFlowCounters_Type = OctetString
_NbsArSecFlowCounters_Object = MibTableColumn
nbsArSecFlowCounters = _NbsArSecFlowCounters_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 10, 8, 1, 1, 12),
    _NbsArSecFlowCounters_Type()
)
nbsArSecFlowCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsArSecFlowCounters.setStatus("mandatory")


class _NbsArSecFlowAdminStatus_Type(Integer32):
    """Custom type nbsArSecFlowAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("activate", 5),
          ("add", 2),
          ("deactivate", 6),
          ("delete", 3),
          ("modify", 4),
          ("none", 1))
    )


_NbsArSecFlowAdminStatus_Type.__name__ = "Integer32"
_NbsArSecFlowAdminStatus_Object = MibTableColumn
nbsArSecFlowAdminStatus = _NbsArSecFlowAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 10, 8, 1, 1, 13),
    _NbsArSecFlowAdminStatus_Type()
)
nbsArSecFlowAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsArSecFlowAdminStatus.setStatus("mandatory")
_NbsArFlowServiceSpecTable_Object = MibTable
nbsArFlowServiceSpecTable = _NbsArFlowServiceSpecTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 10, 8, 2)
)
if mibBuilder.loadTexts:
    nbsArFlowServiceSpecTable.setStatus("mandatory")
_NbsArFlowServiceSpecEntry_Object = MibTableRow
nbsArFlowServiceSpecEntry = _NbsArFlowServiceSpecEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 10, 8, 2, 1)
)
nbsArFlowServiceSpecEntry.setIndexNames(
    (0, "SEC-FLOW-MIB", "nbsArFlowServiceFlowIndex"),
    (0, "SEC-FLOW-MIB", "nbsArFlowServiceSpecsServiceId"),
)
if mibBuilder.loadTexts:
    nbsArFlowServiceSpecEntry.setStatus("mandatory")
_NbsArFlowServiceFlowIndex_Type = Integer32
_NbsArFlowServiceFlowIndex_Object = MibTableColumn
nbsArFlowServiceFlowIndex = _NbsArFlowServiceFlowIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 10, 8, 2, 1, 1),
    _NbsArFlowServiceFlowIndex_Type()
)
nbsArFlowServiceFlowIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsArFlowServiceFlowIndex.setStatus("mandatory")
_NbsArFlowServiceSpecsServiceId_Type = Integer32
_NbsArFlowServiceSpecsServiceId_Object = MibTableColumn
nbsArFlowServiceSpecsServiceId = _NbsArFlowServiceSpecsServiceId_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 10, 8, 2, 1, 2),
    _NbsArFlowServiceSpecsServiceId_Type()
)
nbsArFlowServiceSpecsServiceId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsArFlowServiceSpecsServiceId.setStatus("mandatory")
_NbsArFlowServiceSpecsServiceType_Type = Integer32
_NbsArFlowServiceSpecsServiceType_Object = MibTableColumn
nbsArFlowServiceSpecsServiceType = _NbsArFlowServiceSpecsServiceType_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 10, 8, 2, 1, 3),
    _NbsArFlowServiceSpecsServiceType_Type()
)
nbsArFlowServiceSpecsServiceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsArFlowServiceSpecsServiceType.setStatus("mandatory")
_NbsArFlowServiceSpecsServiceFlowIndex_Type = Integer32
_NbsArFlowServiceSpecsServiceFlowIndex_Object = MibTableColumn
nbsArFlowServiceSpecsServiceFlowIndex = _NbsArFlowServiceSpecsServiceFlowIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 10, 8, 2, 1, 4),
    _NbsArFlowServiceSpecsServiceFlowIndex_Type()
)
nbsArFlowServiceSpecsServiceFlowIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsArFlowServiceSpecsServiceFlowIndex.setStatus("mandatory")
_NbsArFlowServiceSpecsFlowIDExtension_Type = OctetString
_NbsArFlowServiceSpecsFlowIDExtension_Object = MibTableColumn
nbsArFlowServiceSpecsFlowIDExtension = _NbsArFlowServiceSpecsFlowIDExtension_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 10, 8, 2, 1, 5),
    _NbsArFlowServiceSpecsFlowIDExtension_Type()
)
nbsArFlowServiceSpecsFlowIDExtension.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsArFlowServiceSpecsFlowIDExtension.setStatus("mandatory")
_NbsArFlowServiceSpecsFlowModifier_Type = OctetString
_NbsArFlowServiceSpecsFlowModifier_Object = MibTableColumn
nbsArFlowServiceSpecsFlowModifier = _NbsArFlowServiceSpecsFlowModifier_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 10, 8, 2, 1, 6),
    _NbsArFlowServiceSpecsFlowModifier_Type()
)
nbsArFlowServiceSpecsFlowModifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsArFlowServiceSpecsFlowModifier.setStatus("mandatory")
_NbsArFlowServiceSpecsFlowSpec_Type = OctetString
_NbsArFlowServiceSpecsFlowSpec_Object = MibTableColumn
nbsArFlowServiceSpecsFlowSpec = _NbsArFlowServiceSpecsFlowSpec_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 10, 8, 2, 1, 7),
    _NbsArFlowServiceSpecsFlowSpec_Type()
)
nbsArFlowServiceSpecsFlowSpec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsArFlowServiceSpecsFlowSpec.setStatus("mandatory")


class _NbsArFlowServiceSpecsAdminStatus_Type(Integer32):
    """Custom type nbsArFlowServiceSpecsAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("add", 2),
          ("delete", 3),
          ("modify", 4),
          ("none", 1))
    )


_NbsArFlowServiceSpecsAdminStatus_Type.__name__ = "Integer32"
_NbsArFlowServiceSpecsAdminStatus_Object = MibTableColumn
nbsArFlowServiceSpecsAdminStatus = _NbsArFlowServiceSpecsAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 10, 8, 2, 1, 8),
    _NbsArFlowServiceSpecsAdminStatus_Type()
)
nbsArFlowServiceSpecsAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsArFlowServiceSpecsAdminStatus.setStatus("mandatory")
_NbsArFlowServicePortTable_Object = MibTable
nbsArFlowServicePortTable = _NbsArFlowServicePortTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 10, 8, 3)
)
if mibBuilder.loadTexts:
    nbsArFlowServicePortTable.setStatus("mandatory")
_NbsArFlowServicePortEntry_Object = MibTableRow
nbsArFlowServicePortEntry = _NbsArFlowServicePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 10, 8, 3, 1)
)
nbsArFlowServicePortEntry.setIndexNames(
    (0, "SEC-FLOW-MIB", "nbsArFlowServicePortNumber"),
)
if mibBuilder.loadTexts:
    nbsArFlowServicePortEntry.setStatus("mandatory")
_NbsArFlowServicePortNumber_Type = Integer32
_NbsArFlowServicePortNumber_Object = MibTableColumn
nbsArFlowServicePortNumber = _NbsArFlowServicePortNumber_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 10, 8, 3, 1, 1),
    _NbsArFlowServicePortNumber_Type()
)
nbsArFlowServicePortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsArFlowServicePortNumber.setStatus("mandatory")
_NbsArFlowServicePortData_Type = OctetString
_NbsArFlowServicePortData_Object = MibTableColumn
nbsArFlowServicePortData = _NbsArFlowServicePortData_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 10, 8, 3, 1, 2),
    _NbsArFlowServicePortData_Type()
)
nbsArFlowServicePortData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsArFlowServicePortData.setStatus("mandatory")


class _NbsArFlowServicePortAdminStatus_Type(Integer32):
    """Custom type nbsArFlowServicePortAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("add", 2),
          ("delete", 3),
          ("modify", 4),
          ("none", 1))
    )


_NbsArFlowServicePortAdminStatus_Type.__name__ = "Integer32"
_NbsArFlowServicePortAdminStatus_Object = MibTableColumn
nbsArFlowServicePortAdminStatus = _NbsArFlowServicePortAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 10, 8, 3, 1, 3),
    _NbsArFlowServicePortAdminStatus_Type()
)
nbsArFlowServicePortAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsArFlowServicePortAdminStatus.setStatus("mandatory")
_NbsArSecFlowFwdStatus_Type = OctetString
_NbsArSecFlowFwdStatus_Object = MibScalar
nbsArSecFlowFwdStatus = _NbsArSecFlowFwdStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 10, 8, 4),
    _NbsArSecFlowFwdStatus_Type()
)
nbsArSecFlowFwdStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsArSecFlowFwdStatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SEC-FLOW-MIB",
    **{"MacAddress": MacAddress,
       "nbSwitchG1Il": nbSwitchG1Il,
       "nbsAccelerouter": nbsAccelerouter,
       "nbsArSecFlow": nbsArSecFlow,
       "nbsArSecFlowTable": nbsArSecFlowTable,
       "nbsArSecFlowEntry": nbsArSecFlowEntry,
       "nbsArSecFlowIndex": nbsArSecFlowIndex,
       "nbsArSecFlowValid": nbsArSecFlowValid,
       "nbsArSecFlowState": nbsArSecFlowState,
       "nbsArSecFlowLastUsedTimestamp": nbsArSecFlowLastUsedTimestamp,
       "nbsArSecFlowServTypes": nbsArSecFlowServTypes,
       "nbsArSecFlowServId": nbsArSecFlowServId,
       "nbsArFlowID": nbsArFlowID,
       "nbsArFlowQoSSpec": nbsArFlowQoSSpec,
       "nbsArSecFlowNumOfServices": nbsArSecFlowNumOfServices,
       "nbsArSecFlowDriverData": nbsArSecFlowDriverData,
       "nbsArSecFlowActions": nbsArSecFlowActions,
       "nbsArSecFlowCounters": nbsArSecFlowCounters,
       "nbsArSecFlowAdminStatus": nbsArSecFlowAdminStatus,
       "nbsArFlowServiceSpecTable": nbsArFlowServiceSpecTable,
       "nbsArFlowServiceSpecEntry": nbsArFlowServiceSpecEntry,
       "nbsArFlowServiceFlowIndex": nbsArFlowServiceFlowIndex,
       "nbsArFlowServiceSpecsServiceId": nbsArFlowServiceSpecsServiceId,
       "nbsArFlowServiceSpecsServiceType": nbsArFlowServiceSpecsServiceType,
       "nbsArFlowServiceSpecsServiceFlowIndex": nbsArFlowServiceSpecsServiceFlowIndex,
       "nbsArFlowServiceSpecsFlowIDExtension": nbsArFlowServiceSpecsFlowIDExtension,
       "nbsArFlowServiceSpecsFlowModifier": nbsArFlowServiceSpecsFlowModifier,
       "nbsArFlowServiceSpecsFlowSpec": nbsArFlowServiceSpecsFlowSpec,
       "nbsArFlowServiceSpecsAdminStatus": nbsArFlowServiceSpecsAdminStatus,
       "nbsArFlowServicePortTable": nbsArFlowServicePortTable,
       "nbsArFlowServicePortEntry": nbsArFlowServicePortEntry,
       "nbsArFlowServicePortNumber": nbsArFlowServicePortNumber,
       "nbsArFlowServicePortData": nbsArFlowServicePortData,
       "nbsArFlowServicePortAdminStatus": nbsArFlowServicePortAdminStatus,
       "nbsArSecFlowFwdStatus": nbsArSecFlowFwdStatus}
)
