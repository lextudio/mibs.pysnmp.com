# SNMP MIB module (Nortel-Magellan-Passport-ModAtmQosMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-Magellan-Passport-ModAtmQosMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:31:10 2024
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

(modFrs,
 modFrsIndex) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-ModCommonMIB",
    "modFrs",
    "modFrsIndex")

(modIndex,) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-ShelfMIB",
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

(NonReplicated,) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-TextualConventionsMIB",
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

_ModFrsAtmNet_ObjectIdentity = ObjectIdentity
modFrsAtmNet = _ModFrsAtmNet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 16, 3, 2)
)
_ModFrsAtmNetRowStatusTable_Object = MibTable
modFrsAtmNetRowStatusTable = _ModFrsAtmNetRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 16, 3, 2, 1)
)
if mibBuilder.loadTexts:
    modFrsAtmNetRowStatusTable.setStatus("mandatory")
_ModFrsAtmNetRowStatusEntry_Object = MibTableRow
modFrsAtmNetRowStatusEntry = _ModFrsAtmNetRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 16, 3, 2, 1, 1)
)
modFrsAtmNetRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-ShelfMIB", "modIndex"),
    (0, "Nortel-Magellan-Passport-ModCommonMIB", "modFrsIndex"),
    (0, "Nortel-Magellan-Passport-ModAtmQosMIB", "modFrsAtmNetIndex"),
)
if mibBuilder.loadTexts:
    modFrsAtmNetRowStatusEntry.setStatus("mandatory")
_ModFrsAtmNetRowStatus_Type = RowStatus
_ModFrsAtmNetRowStatus_Object = MibTableColumn
modFrsAtmNetRowStatus = _ModFrsAtmNetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 16, 3, 2, 1, 1, 1),
    _ModFrsAtmNetRowStatus_Type()
)
modFrsAtmNetRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modFrsAtmNetRowStatus.setStatus("mandatory")
_ModFrsAtmNetComponentName_Type = DisplayString
_ModFrsAtmNetComponentName_Object = MibTableColumn
modFrsAtmNetComponentName = _ModFrsAtmNetComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 16, 3, 2, 1, 1, 2),
    _ModFrsAtmNetComponentName_Type()
)
modFrsAtmNetComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modFrsAtmNetComponentName.setStatus("mandatory")
_ModFrsAtmNetStorageType_Type = StorageType
_ModFrsAtmNetStorageType_Object = MibTableColumn
modFrsAtmNetStorageType = _ModFrsAtmNetStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 16, 3, 2, 1, 1, 4),
    _ModFrsAtmNetStorageType_Type()
)
modFrsAtmNetStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modFrsAtmNetStorageType.setStatus("mandatory")
_ModFrsAtmNetIndex_Type = NonReplicated
_ModFrsAtmNetIndex_Object = MibTableColumn
modFrsAtmNetIndex = _ModFrsAtmNetIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 16, 3, 2, 1, 1, 10),
    _ModFrsAtmNetIndex_Type()
)
modFrsAtmNetIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    modFrsAtmNetIndex.setStatus("mandatory")
_ModFrsAtmNetTpm_ObjectIdentity = ObjectIdentity
modFrsAtmNetTpm = _ModFrsAtmNetTpm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 16, 3, 2, 2)
)
_ModFrsAtmNetTpmRowStatusTable_Object = MibTable
modFrsAtmNetTpmRowStatusTable = _ModFrsAtmNetTpmRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 16, 3, 2, 2, 1)
)
if mibBuilder.loadTexts:
    modFrsAtmNetTpmRowStatusTable.setStatus("mandatory")
_ModFrsAtmNetTpmRowStatusEntry_Object = MibTableRow
modFrsAtmNetTpmRowStatusEntry = _ModFrsAtmNetTpmRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 16, 3, 2, 2, 1, 1)
)
modFrsAtmNetTpmRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-ShelfMIB", "modIndex"),
    (0, "Nortel-Magellan-Passport-ModCommonMIB", "modFrsIndex"),
    (0, "Nortel-Magellan-Passport-ModAtmQosMIB", "modFrsAtmNetIndex"),
    (0, "Nortel-Magellan-Passport-ModAtmQosMIB", "modFrsAtmNetTpmIndex"),
)
if mibBuilder.loadTexts:
    modFrsAtmNetTpmRowStatusEntry.setStatus("mandatory")
_ModFrsAtmNetTpmRowStatus_Type = RowStatus
_ModFrsAtmNetTpmRowStatus_Object = MibTableColumn
modFrsAtmNetTpmRowStatus = _ModFrsAtmNetTpmRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 16, 3, 2, 2, 1, 1, 1),
    _ModFrsAtmNetTpmRowStatus_Type()
)
modFrsAtmNetTpmRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modFrsAtmNetTpmRowStatus.setStatus("mandatory")
_ModFrsAtmNetTpmComponentName_Type = DisplayString
_ModFrsAtmNetTpmComponentName_Object = MibTableColumn
modFrsAtmNetTpmComponentName = _ModFrsAtmNetTpmComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 16, 3, 2, 2, 1, 1, 2),
    _ModFrsAtmNetTpmComponentName_Type()
)
modFrsAtmNetTpmComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modFrsAtmNetTpmComponentName.setStatus("mandatory")
_ModFrsAtmNetTpmStorageType_Type = StorageType
_ModFrsAtmNetTpmStorageType_Object = MibTableColumn
modFrsAtmNetTpmStorageType = _ModFrsAtmNetTpmStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 16, 3, 2, 2, 1, 1, 4),
    _ModFrsAtmNetTpmStorageType_Type()
)
modFrsAtmNetTpmStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modFrsAtmNetTpmStorageType.setStatus("mandatory")


class _ModFrsAtmNetTpmIndex_Type(Integer32):
    """Custom type modFrsAtmNetTpmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_ModFrsAtmNetTpmIndex_Type.__name__ = "Integer32"
_ModFrsAtmNetTpmIndex_Object = MibTableColumn
modFrsAtmNetTpmIndex = _ModFrsAtmNetTpmIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 16, 3, 2, 2, 1, 1, 10),
    _ModFrsAtmNetTpmIndex_Type()
)
modFrsAtmNetTpmIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    modFrsAtmNetTpmIndex.setStatus("mandatory")
_ModFrsAtmNetTpmProvTable_Object = MibTable
modFrsAtmNetTpmProvTable = _ModFrsAtmNetTpmProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 16, 3, 2, 2, 2)
)
if mibBuilder.loadTexts:
    modFrsAtmNetTpmProvTable.setStatus("mandatory")
_ModFrsAtmNetTpmProvEntry_Object = MibTableRow
modFrsAtmNetTpmProvEntry = _ModFrsAtmNetTpmProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 16, 3, 2, 2, 2, 1)
)
modFrsAtmNetTpmProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-ShelfMIB", "modIndex"),
    (0, "Nortel-Magellan-Passport-ModCommonMIB", "modFrsIndex"),
    (0, "Nortel-Magellan-Passport-ModAtmQosMIB", "modFrsAtmNetIndex"),
    (0, "Nortel-Magellan-Passport-ModAtmQosMIB", "modFrsAtmNetTpmIndex"),
)
if mibBuilder.loadTexts:
    modFrsAtmNetTpmProvEntry.setStatus("mandatory")


class _ModFrsAtmNetTpmEmissionPriority_Type(Unsigned32):
    """Custom type modFrsAtmNetTpmEmissionPriority based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_ModFrsAtmNetTpmEmissionPriority_Type.__name__ = "Unsigned32"
_ModFrsAtmNetTpmEmissionPriority_Object = MibTableColumn
modFrsAtmNetTpmEmissionPriority = _ModFrsAtmNetTpmEmissionPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 16, 3, 2, 2, 2, 1, 1),
    _ModFrsAtmNetTpmEmissionPriority_Type()
)
modFrsAtmNetTpmEmissionPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modFrsAtmNetTpmEmissionPriority.setStatus("mandatory")


class _ModFrsAtmNetTpmAtmServiceCategory_Type(Integer32):
    """Custom type modFrsAtmNetTpmAtmServiceCategory based on Integer32"""
    defaultValue = 3

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
        *(("cbr", 1),
          ("nrtVbr", 3),
          ("rtVbr", 2),
          ("ubr", 0))
    )


_ModFrsAtmNetTpmAtmServiceCategory_Type.__name__ = "Integer32"
_ModFrsAtmNetTpmAtmServiceCategory_Object = MibTableColumn
modFrsAtmNetTpmAtmServiceCategory = _ModFrsAtmNetTpmAtmServiceCategory_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 16, 3, 2, 2, 2, 1, 2),
    _ModFrsAtmNetTpmAtmServiceCategory_Type()
)
modFrsAtmNetTpmAtmServiceCategory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modFrsAtmNetTpmAtmServiceCategory.setStatus("mandatory")


class _ModFrsAtmNetTpmAvgFrameSize_Type(Unsigned32):
    """Custom type modFrsAtmNetTpmAvgFrameSize based on Unsigned32"""
    defaultValue = 128

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8187),
    )


_ModFrsAtmNetTpmAvgFrameSize_Type.__name__ = "Unsigned32"
_ModFrsAtmNetTpmAvgFrameSize_Object = MibTableColumn
modFrsAtmNetTpmAvgFrameSize = _ModFrsAtmNetTpmAvgFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 16, 3, 2, 2, 2, 1, 3),
    _ModFrsAtmNetTpmAvgFrameSize_Type()
)
modFrsAtmNetTpmAvgFrameSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modFrsAtmNetTpmAvgFrameSize.setStatus("mandatory")


class _ModFrsAtmNetTpmTrafficParmConversionPolicy_Type(Integer32):
    """Custom type modFrsAtmNetTpmTrafficParmConversionPolicy based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("n3", 3),
          ("n4", 4),
          ("n5", 5),
          ("n6", 6))
    )


_ModFrsAtmNetTpmTrafficParmConversionPolicy_Type.__name__ = "Integer32"
_ModFrsAtmNetTpmTrafficParmConversionPolicy_Object = MibTableColumn
modFrsAtmNetTpmTrafficParmConversionPolicy = _ModFrsAtmNetTpmTrafficParmConversionPolicy_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 16, 3, 2, 2, 2, 1, 4),
    _ModFrsAtmNetTpmTrafficParmConversionPolicy_Type()
)
modFrsAtmNetTpmTrafficParmConversionPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modFrsAtmNetTpmTrafficParmConversionPolicy.setStatus("mandatory")


class _ModFrsAtmNetTpmAssignedBandwidthPool_Type(Integer32):
    """Custom type modFrsAtmNetTpmAssignedBandwidthPool based on Integer32"""
    defaultValue = 0

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
              12,
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("n0", 0),
          ("n1", 1),
          ("n10", 10),
          ("n11", 11),
          ("n12", 12),
          ("n13", 13),
          ("n14", 14),
          ("n15", 15),
          ("n2", 2),
          ("n3", 3),
          ("n4", 4),
          ("n5", 5),
          ("n6", 6),
          ("n7", 7),
          ("n8", 8),
          ("n9", 9))
    )


_ModFrsAtmNetTpmAssignedBandwidthPool_Type.__name__ = "Integer32"
_ModFrsAtmNetTpmAssignedBandwidthPool_Object = MibTableColumn
modFrsAtmNetTpmAssignedBandwidthPool = _ModFrsAtmNetTpmAssignedBandwidthPool_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 16, 3, 2, 2, 2, 1, 5),
    _ModFrsAtmNetTpmAssignedBandwidthPool_Type()
)
modFrsAtmNetTpmAssignedBandwidthPool.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modFrsAtmNetTpmAssignedBandwidthPool.setStatus("mandatory")
_ModFrsAtmNetProvTable_Object = MibTable
modFrsAtmNetProvTable = _ModFrsAtmNetProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 16, 3, 2, 10)
)
if mibBuilder.loadTexts:
    modFrsAtmNetProvTable.setStatus("mandatory")
_ModFrsAtmNetProvEntry_Object = MibTableRow
modFrsAtmNetProvEntry = _ModFrsAtmNetProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 16, 3, 2, 10, 1)
)
modFrsAtmNetProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-ShelfMIB", "modIndex"),
    (0, "Nortel-Magellan-Passport-ModCommonMIB", "modFrsIndex"),
    (0, "Nortel-Magellan-Passport-ModAtmQosMIB", "modFrsAtmNetIndex"),
)
if mibBuilder.loadTexts:
    modFrsAtmNetProvEntry.setStatus("mandatory")


class _ModFrsAtmNetRetryTimerPeriod_Type(Unsigned32):
    """Custom type modFrsAtmNetRetryTimerPeriod based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 300),
    )


_ModFrsAtmNetRetryTimerPeriod_Type.__name__ = "Unsigned32"
_ModFrsAtmNetRetryTimerPeriod_Object = MibTableColumn
modFrsAtmNetRetryTimerPeriod = _ModFrsAtmNetRetryTimerPeriod_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 16, 3, 2, 10, 1, 1),
    _ModFrsAtmNetRetryTimerPeriod_Type()
)
modFrsAtmNetRetryTimerPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modFrsAtmNetRetryTimerPeriod.setStatus("mandatory")
_ModAtmQosMIB_ObjectIdentity = ObjectIdentity
modAtmQosMIB = _ModAtmQosMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 75)
)
_ModAtmQosGroup_ObjectIdentity = ObjectIdentity
modAtmQosGroup = _ModAtmQosGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 75, 1)
)
_ModAtmQosGroupBE_ObjectIdentity = ObjectIdentity
modAtmQosGroupBE = _ModAtmQosGroupBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 75, 1, 5)
)
_ModAtmQosGroupBE01_ObjectIdentity = ObjectIdentity
modAtmQosGroupBE01 = _ModAtmQosGroupBE01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 75, 1, 5, 2)
)
_ModAtmQosGroupBE01A_ObjectIdentity = ObjectIdentity
modAtmQosGroupBE01A = _ModAtmQosGroupBE01A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 75, 1, 5, 2, 2)
)
_ModAtmQosCapabilities_ObjectIdentity = ObjectIdentity
modAtmQosCapabilities = _ModAtmQosCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 75, 3)
)
_ModAtmQosCapabilitiesBE_ObjectIdentity = ObjectIdentity
modAtmQosCapabilitiesBE = _ModAtmQosCapabilitiesBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 75, 3, 5)
)
_ModAtmQosCapabilitiesBE01_ObjectIdentity = ObjectIdentity
modAtmQosCapabilitiesBE01 = _ModAtmQosCapabilitiesBE01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 75, 3, 5, 2)
)
_ModAtmQosCapabilitiesBE01A_ObjectIdentity = ObjectIdentity
modAtmQosCapabilitiesBE01A = _ModAtmQosCapabilitiesBE01A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 75, 3, 5, 2, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-Magellan-Passport-ModAtmQosMIB",
    **{"modFrsAtmNet": modFrsAtmNet,
       "modFrsAtmNetRowStatusTable": modFrsAtmNetRowStatusTable,
       "modFrsAtmNetRowStatusEntry": modFrsAtmNetRowStatusEntry,
       "modFrsAtmNetRowStatus": modFrsAtmNetRowStatus,
       "modFrsAtmNetComponentName": modFrsAtmNetComponentName,
       "modFrsAtmNetStorageType": modFrsAtmNetStorageType,
       "modFrsAtmNetIndex": modFrsAtmNetIndex,
       "modFrsAtmNetTpm": modFrsAtmNetTpm,
       "modFrsAtmNetTpmRowStatusTable": modFrsAtmNetTpmRowStatusTable,
       "modFrsAtmNetTpmRowStatusEntry": modFrsAtmNetTpmRowStatusEntry,
       "modFrsAtmNetTpmRowStatus": modFrsAtmNetTpmRowStatus,
       "modFrsAtmNetTpmComponentName": modFrsAtmNetTpmComponentName,
       "modFrsAtmNetTpmStorageType": modFrsAtmNetTpmStorageType,
       "modFrsAtmNetTpmIndex": modFrsAtmNetTpmIndex,
       "modFrsAtmNetTpmProvTable": modFrsAtmNetTpmProvTable,
       "modFrsAtmNetTpmProvEntry": modFrsAtmNetTpmProvEntry,
       "modFrsAtmNetTpmEmissionPriority": modFrsAtmNetTpmEmissionPriority,
       "modFrsAtmNetTpmAtmServiceCategory": modFrsAtmNetTpmAtmServiceCategory,
       "modFrsAtmNetTpmAvgFrameSize": modFrsAtmNetTpmAvgFrameSize,
       "modFrsAtmNetTpmTrafficParmConversionPolicy": modFrsAtmNetTpmTrafficParmConversionPolicy,
       "modFrsAtmNetTpmAssignedBandwidthPool": modFrsAtmNetTpmAssignedBandwidthPool,
       "modFrsAtmNetProvTable": modFrsAtmNetProvTable,
       "modFrsAtmNetProvEntry": modFrsAtmNetProvEntry,
       "modFrsAtmNetRetryTimerPeriod": modFrsAtmNetRetryTimerPeriod,
       "modAtmQosMIB": modAtmQosMIB,
       "modAtmQosGroup": modAtmQosGroup,
       "modAtmQosGroupBE": modAtmQosGroupBE,
       "modAtmQosGroupBE01": modAtmQosGroupBE01,
       "modAtmQosGroupBE01A": modAtmQosGroupBE01A,
       "modAtmQosCapabilities": modAtmQosCapabilities,
       "modAtmQosCapabilitiesBE": modAtmQosCapabilitiesBE,
       "modAtmQosCapabilitiesBE01": modAtmQosCapabilitiesBE01,
       "modAtmQosCapabilitiesBE01A": modAtmQosCapabilitiesBE01A}
)
