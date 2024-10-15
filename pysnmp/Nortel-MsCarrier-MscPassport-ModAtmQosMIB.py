# SNMP MIB module (Nortel-MsCarrier-MscPassport-ModAtmQosMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-MsCarrier-MscPassport-ModAtmQosMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:32:49 2024
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

(mscModIndex,) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-BaseShelfMIB",
    "mscModIndex")

(mscModFrs,
 mscModFrsIndex) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-ModCommonMIB",
    "mscModFrs",
    "mscModFrsIndex")

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

(NonReplicated,) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-TextualConventionsMIB",
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

_MscModFrsAtmNet_ObjectIdentity = ObjectIdentity
mscModFrsAtmNet = _MscModFrsAtmNet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 3, 2)
)
_MscModFrsAtmNetRowStatusTable_Object = MibTable
mscModFrsAtmNetRowStatusTable = _MscModFrsAtmNetRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 3, 2, 1)
)
if mibBuilder.loadTexts:
    mscModFrsAtmNetRowStatusTable.setStatus("mandatory")
_MscModFrsAtmNetRowStatusEntry_Object = MibTableRow
mscModFrsAtmNetRowStatusEntry = _MscModFrsAtmNetRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 3, 2, 1, 1)
)
mscModFrsAtmNetRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscModIndex"),
    (0, "Nortel-MsCarrier-MscPassport-ModCommonMIB", "mscModFrsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-ModAtmQosMIB", "mscModFrsAtmNetIndex"),
)
if mibBuilder.loadTexts:
    mscModFrsAtmNetRowStatusEntry.setStatus("mandatory")
_MscModFrsAtmNetRowStatus_Type = RowStatus
_MscModFrsAtmNetRowStatus_Object = MibTableColumn
mscModFrsAtmNetRowStatus = _MscModFrsAtmNetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 3, 2, 1, 1, 1),
    _MscModFrsAtmNetRowStatus_Type()
)
mscModFrsAtmNetRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscModFrsAtmNetRowStatus.setStatus("mandatory")
_MscModFrsAtmNetComponentName_Type = DisplayString
_MscModFrsAtmNetComponentName_Object = MibTableColumn
mscModFrsAtmNetComponentName = _MscModFrsAtmNetComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 3, 2, 1, 1, 2),
    _MscModFrsAtmNetComponentName_Type()
)
mscModFrsAtmNetComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscModFrsAtmNetComponentName.setStatus("mandatory")
_MscModFrsAtmNetStorageType_Type = StorageType
_MscModFrsAtmNetStorageType_Object = MibTableColumn
mscModFrsAtmNetStorageType = _MscModFrsAtmNetStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 3, 2, 1, 1, 4),
    _MscModFrsAtmNetStorageType_Type()
)
mscModFrsAtmNetStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscModFrsAtmNetStorageType.setStatus("mandatory")
_MscModFrsAtmNetIndex_Type = NonReplicated
_MscModFrsAtmNetIndex_Object = MibTableColumn
mscModFrsAtmNetIndex = _MscModFrsAtmNetIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 3, 2, 1, 1, 10),
    _MscModFrsAtmNetIndex_Type()
)
mscModFrsAtmNetIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscModFrsAtmNetIndex.setStatus("mandatory")
_MscModFrsAtmNetTpm_ObjectIdentity = ObjectIdentity
mscModFrsAtmNetTpm = _MscModFrsAtmNetTpm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 3, 2, 2)
)
_MscModFrsAtmNetTpmRowStatusTable_Object = MibTable
mscModFrsAtmNetTpmRowStatusTable = _MscModFrsAtmNetTpmRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 3, 2, 2, 1)
)
if mibBuilder.loadTexts:
    mscModFrsAtmNetTpmRowStatusTable.setStatus("mandatory")
_MscModFrsAtmNetTpmRowStatusEntry_Object = MibTableRow
mscModFrsAtmNetTpmRowStatusEntry = _MscModFrsAtmNetTpmRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 3, 2, 2, 1, 1)
)
mscModFrsAtmNetTpmRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscModIndex"),
    (0, "Nortel-MsCarrier-MscPassport-ModCommonMIB", "mscModFrsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-ModAtmQosMIB", "mscModFrsAtmNetIndex"),
    (0, "Nortel-MsCarrier-MscPassport-ModAtmQosMIB", "mscModFrsAtmNetTpmIndex"),
)
if mibBuilder.loadTexts:
    mscModFrsAtmNetTpmRowStatusEntry.setStatus("mandatory")
_MscModFrsAtmNetTpmRowStatus_Type = RowStatus
_MscModFrsAtmNetTpmRowStatus_Object = MibTableColumn
mscModFrsAtmNetTpmRowStatus = _MscModFrsAtmNetTpmRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 3, 2, 2, 1, 1, 1),
    _MscModFrsAtmNetTpmRowStatus_Type()
)
mscModFrsAtmNetTpmRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscModFrsAtmNetTpmRowStatus.setStatus("mandatory")
_MscModFrsAtmNetTpmComponentName_Type = DisplayString
_MscModFrsAtmNetTpmComponentName_Object = MibTableColumn
mscModFrsAtmNetTpmComponentName = _MscModFrsAtmNetTpmComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 3, 2, 2, 1, 1, 2),
    _MscModFrsAtmNetTpmComponentName_Type()
)
mscModFrsAtmNetTpmComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscModFrsAtmNetTpmComponentName.setStatus("mandatory")
_MscModFrsAtmNetTpmStorageType_Type = StorageType
_MscModFrsAtmNetTpmStorageType_Object = MibTableColumn
mscModFrsAtmNetTpmStorageType = _MscModFrsAtmNetTpmStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 3, 2, 2, 1, 1, 4),
    _MscModFrsAtmNetTpmStorageType_Type()
)
mscModFrsAtmNetTpmStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscModFrsAtmNetTpmStorageType.setStatus("mandatory")


class _MscModFrsAtmNetTpmIndex_Type(Integer32):
    """Custom type mscModFrsAtmNetTpmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_MscModFrsAtmNetTpmIndex_Type.__name__ = "Integer32"
_MscModFrsAtmNetTpmIndex_Object = MibTableColumn
mscModFrsAtmNetTpmIndex = _MscModFrsAtmNetTpmIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 3, 2, 2, 1, 1, 10),
    _MscModFrsAtmNetTpmIndex_Type()
)
mscModFrsAtmNetTpmIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscModFrsAtmNetTpmIndex.setStatus("mandatory")
_MscModFrsAtmNetTpmProvTable_Object = MibTable
mscModFrsAtmNetTpmProvTable = _MscModFrsAtmNetTpmProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 3, 2, 2, 2)
)
if mibBuilder.loadTexts:
    mscModFrsAtmNetTpmProvTable.setStatus("mandatory")
_MscModFrsAtmNetTpmProvEntry_Object = MibTableRow
mscModFrsAtmNetTpmProvEntry = _MscModFrsAtmNetTpmProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 3, 2, 2, 2, 1)
)
mscModFrsAtmNetTpmProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscModIndex"),
    (0, "Nortel-MsCarrier-MscPassport-ModCommonMIB", "mscModFrsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-ModAtmQosMIB", "mscModFrsAtmNetIndex"),
    (0, "Nortel-MsCarrier-MscPassport-ModAtmQosMIB", "mscModFrsAtmNetTpmIndex"),
)
if mibBuilder.loadTexts:
    mscModFrsAtmNetTpmProvEntry.setStatus("mandatory")


class _MscModFrsAtmNetTpmEmissionPriority_Type(Unsigned32):
    """Custom type mscModFrsAtmNetTpmEmissionPriority based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_MscModFrsAtmNetTpmEmissionPriority_Type.__name__ = "Unsigned32"
_MscModFrsAtmNetTpmEmissionPriority_Object = MibTableColumn
mscModFrsAtmNetTpmEmissionPriority = _MscModFrsAtmNetTpmEmissionPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 3, 2, 2, 2, 1, 1),
    _MscModFrsAtmNetTpmEmissionPriority_Type()
)
mscModFrsAtmNetTpmEmissionPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscModFrsAtmNetTpmEmissionPriority.setStatus("mandatory")


class _MscModFrsAtmNetTpmAtmServiceCategory_Type(Integer32):
    """Custom type mscModFrsAtmNetTpmAtmServiceCategory based on Integer32"""
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


_MscModFrsAtmNetTpmAtmServiceCategory_Type.__name__ = "Integer32"
_MscModFrsAtmNetTpmAtmServiceCategory_Object = MibTableColumn
mscModFrsAtmNetTpmAtmServiceCategory = _MscModFrsAtmNetTpmAtmServiceCategory_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 3, 2, 2, 2, 1, 2),
    _MscModFrsAtmNetTpmAtmServiceCategory_Type()
)
mscModFrsAtmNetTpmAtmServiceCategory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscModFrsAtmNetTpmAtmServiceCategory.setStatus("mandatory")


class _MscModFrsAtmNetTpmAvgFrameSize_Type(Unsigned32):
    """Custom type mscModFrsAtmNetTpmAvgFrameSize based on Unsigned32"""
    defaultValue = 128

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8187),
    )


_MscModFrsAtmNetTpmAvgFrameSize_Type.__name__ = "Unsigned32"
_MscModFrsAtmNetTpmAvgFrameSize_Object = MibTableColumn
mscModFrsAtmNetTpmAvgFrameSize = _MscModFrsAtmNetTpmAvgFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 3, 2, 2, 2, 1, 3),
    _MscModFrsAtmNetTpmAvgFrameSize_Type()
)
mscModFrsAtmNetTpmAvgFrameSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscModFrsAtmNetTpmAvgFrameSize.setStatus("mandatory")


class _MscModFrsAtmNetTpmTrafficParmConversionPolicy_Type(Integer32):
    """Custom type mscModFrsAtmNetTpmTrafficParmConversionPolicy based on Integer32"""
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


_MscModFrsAtmNetTpmTrafficParmConversionPolicy_Type.__name__ = "Integer32"
_MscModFrsAtmNetTpmTrafficParmConversionPolicy_Object = MibTableColumn
mscModFrsAtmNetTpmTrafficParmConversionPolicy = _MscModFrsAtmNetTpmTrafficParmConversionPolicy_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 3, 2, 2, 2, 1, 4),
    _MscModFrsAtmNetTpmTrafficParmConversionPolicy_Type()
)
mscModFrsAtmNetTpmTrafficParmConversionPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscModFrsAtmNetTpmTrafficParmConversionPolicy.setStatus("mandatory")


class _MscModFrsAtmNetTpmAssignedBandwidthPool_Type(Integer32):
    """Custom type mscModFrsAtmNetTpmAssignedBandwidthPool based on Integer32"""
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


_MscModFrsAtmNetTpmAssignedBandwidthPool_Type.__name__ = "Integer32"
_MscModFrsAtmNetTpmAssignedBandwidthPool_Object = MibTableColumn
mscModFrsAtmNetTpmAssignedBandwidthPool = _MscModFrsAtmNetTpmAssignedBandwidthPool_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 3, 2, 2, 2, 1, 5),
    _MscModFrsAtmNetTpmAssignedBandwidthPool_Type()
)
mscModFrsAtmNetTpmAssignedBandwidthPool.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscModFrsAtmNetTpmAssignedBandwidthPool.setStatus("mandatory")
_MscModFrsAtmNetProvTable_Object = MibTable
mscModFrsAtmNetProvTable = _MscModFrsAtmNetProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 3, 2, 10)
)
if mibBuilder.loadTexts:
    mscModFrsAtmNetProvTable.setStatus("mandatory")
_MscModFrsAtmNetProvEntry_Object = MibTableRow
mscModFrsAtmNetProvEntry = _MscModFrsAtmNetProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 3, 2, 10, 1)
)
mscModFrsAtmNetProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscModIndex"),
    (0, "Nortel-MsCarrier-MscPassport-ModCommonMIB", "mscModFrsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-ModAtmQosMIB", "mscModFrsAtmNetIndex"),
)
if mibBuilder.loadTexts:
    mscModFrsAtmNetProvEntry.setStatus("mandatory")


class _MscModFrsAtmNetRetryTimerPeriod_Type(Unsigned32):
    """Custom type mscModFrsAtmNetRetryTimerPeriod based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 300),
    )


_MscModFrsAtmNetRetryTimerPeriod_Type.__name__ = "Unsigned32"
_MscModFrsAtmNetRetryTimerPeriod_Object = MibTableColumn
mscModFrsAtmNetRetryTimerPeriod = _MscModFrsAtmNetRetryTimerPeriod_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 3, 2, 10, 1, 1),
    _MscModFrsAtmNetRetryTimerPeriod_Type()
)
mscModFrsAtmNetRetryTimerPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscModFrsAtmNetRetryTimerPeriod.setStatus("mandatory")
_ModAtmQosMIB_ObjectIdentity = ObjectIdentity
modAtmQosMIB = _ModAtmQosMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 75)
)
_ModAtmQosGroup_ObjectIdentity = ObjectIdentity
modAtmQosGroup = _ModAtmQosGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 75, 1)
)
_ModAtmQosGroupCA_ObjectIdentity = ObjectIdentity
modAtmQosGroupCA = _ModAtmQosGroupCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 75, 1, 1)
)
_ModAtmQosGroupCA02_ObjectIdentity = ObjectIdentity
modAtmQosGroupCA02 = _ModAtmQosGroupCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 75, 1, 1, 3)
)
_ModAtmQosGroupCA02A_ObjectIdentity = ObjectIdentity
modAtmQosGroupCA02A = _ModAtmQosGroupCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 75, 1, 1, 3, 2)
)
_ModAtmQosCapabilities_ObjectIdentity = ObjectIdentity
modAtmQosCapabilities = _ModAtmQosCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 75, 3)
)
_ModAtmQosCapabilitiesCA_ObjectIdentity = ObjectIdentity
modAtmQosCapabilitiesCA = _ModAtmQosCapabilitiesCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 75, 3, 1)
)
_ModAtmQosCapabilitiesCA02_ObjectIdentity = ObjectIdentity
modAtmQosCapabilitiesCA02 = _ModAtmQosCapabilitiesCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 75, 3, 1, 3)
)
_ModAtmQosCapabilitiesCA02A_ObjectIdentity = ObjectIdentity
modAtmQosCapabilitiesCA02A = _ModAtmQosCapabilitiesCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 75, 3, 1, 3, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-MsCarrier-MscPassport-ModAtmQosMIB",
    **{"mscModFrsAtmNet": mscModFrsAtmNet,
       "mscModFrsAtmNetRowStatusTable": mscModFrsAtmNetRowStatusTable,
       "mscModFrsAtmNetRowStatusEntry": mscModFrsAtmNetRowStatusEntry,
       "mscModFrsAtmNetRowStatus": mscModFrsAtmNetRowStatus,
       "mscModFrsAtmNetComponentName": mscModFrsAtmNetComponentName,
       "mscModFrsAtmNetStorageType": mscModFrsAtmNetStorageType,
       "mscModFrsAtmNetIndex": mscModFrsAtmNetIndex,
       "mscModFrsAtmNetTpm": mscModFrsAtmNetTpm,
       "mscModFrsAtmNetTpmRowStatusTable": mscModFrsAtmNetTpmRowStatusTable,
       "mscModFrsAtmNetTpmRowStatusEntry": mscModFrsAtmNetTpmRowStatusEntry,
       "mscModFrsAtmNetTpmRowStatus": mscModFrsAtmNetTpmRowStatus,
       "mscModFrsAtmNetTpmComponentName": mscModFrsAtmNetTpmComponentName,
       "mscModFrsAtmNetTpmStorageType": mscModFrsAtmNetTpmStorageType,
       "mscModFrsAtmNetTpmIndex": mscModFrsAtmNetTpmIndex,
       "mscModFrsAtmNetTpmProvTable": mscModFrsAtmNetTpmProvTable,
       "mscModFrsAtmNetTpmProvEntry": mscModFrsAtmNetTpmProvEntry,
       "mscModFrsAtmNetTpmEmissionPriority": mscModFrsAtmNetTpmEmissionPriority,
       "mscModFrsAtmNetTpmAtmServiceCategory": mscModFrsAtmNetTpmAtmServiceCategory,
       "mscModFrsAtmNetTpmAvgFrameSize": mscModFrsAtmNetTpmAvgFrameSize,
       "mscModFrsAtmNetTpmTrafficParmConversionPolicy": mscModFrsAtmNetTpmTrafficParmConversionPolicy,
       "mscModFrsAtmNetTpmAssignedBandwidthPool": mscModFrsAtmNetTpmAssignedBandwidthPool,
       "mscModFrsAtmNetProvTable": mscModFrsAtmNetProvTable,
       "mscModFrsAtmNetProvEntry": mscModFrsAtmNetProvEntry,
       "mscModFrsAtmNetRetryTimerPeriod": mscModFrsAtmNetRetryTimerPeriod,
       "modAtmQosMIB": modAtmQosMIB,
       "modAtmQosGroup": modAtmQosGroup,
       "modAtmQosGroupCA": modAtmQosGroupCA,
       "modAtmQosGroupCA02": modAtmQosGroupCA02,
       "modAtmQosGroupCA02A": modAtmQosGroupCA02A,
       "modAtmQosCapabilities": modAtmQosCapabilities,
       "modAtmQosCapabilitiesCA": modAtmQosCapabilitiesCA,
       "modAtmQosCapabilitiesCA02": modAtmQosCapabilitiesCA02,
       "modAtmQosCapabilitiesCA02A": modAtmQosCapabilitiesCA02A}
)
