# SNMP MIB module (Nortel-MsCarrier-MscPassport-ModDprsQosMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-MsCarrier-MscPassport-ModDprsQosMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:32:50 2024
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

_MscModFrsDprsNet_ObjectIdentity = ObjectIdentity
mscModFrsDprsNet = _MscModFrsDprsNet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 3, 3)
)
_MscModFrsDprsNetRowStatusTable_Object = MibTable
mscModFrsDprsNetRowStatusTable = _MscModFrsDprsNetRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 3, 3, 1)
)
if mibBuilder.loadTexts:
    mscModFrsDprsNetRowStatusTable.setStatus("mandatory")
_MscModFrsDprsNetRowStatusEntry_Object = MibTableRow
mscModFrsDprsNetRowStatusEntry = _MscModFrsDprsNetRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 3, 3, 1, 1)
)
mscModFrsDprsNetRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscModIndex"),
    (0, "Nortel-MsCarrier-MscPassport-ModCommonMIB", "mscModFrsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-ModDprsQosMIB", "mscModFrsDprsNetIndex"),
)
if mibBuilder.loadTexts:
    mscModFrsDprsNetRowStatusEntry.setStatus("mandatory")
_MscModFrsDprsNetRowStatus_Type = RowStatus
_MscModFrsDprsNetRowStatus_Object = MibTableColumn
mscModFrsDprsNetRowStatus = _MscModFrsDprsNetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 3, 3, 1, 1, 1),
    _MscModFrsDprsNetRowStatus_Type()
)
mscModFrsDprsNetRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscModFrsDprsNetRowStatus.setStatus("mandatory")
_MscModFrsDprsNetComponentName_Type = DisplayString
_MscModFrsDprsNetComponentName_Object = MibTableColumn
mscModFrsDprsNetComponentName = _MscModFrsDprsNetComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 3, 3, 1, 1, 2),
    _MscModFrsDprsNetComponentName_Type()
)
mscModFrsDprsNetComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscModFrsDprsNetComponentName.setStatus("mandatory")
_MscModFrsDprsNetStorageType_Type = StorageType
_MscModFrsDprsNetStorageType_Object = MibTableColumn
mscModFrsDprsNetStorageType = _MscModFrsDprsNetStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 3, 3, 1, 1, 4),
    _MscModFrsDprsNetStorageType_Type()
)
mscModFrsDprsNetStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscModFrsDprsNetStorageType.setStatus("mandatory")
_MscModFrsDprsNetIndex_Type = NonReplicated
_MscModFrsDprsNetIndex_Object = MibTableColumn
mscModFrsDprsNetIndex = _MscModFrsDprsNetIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 3, 3, 1, 1, 10),
    _MscModFrsDprsNetIndex_Type()
)
mscModFrsDprsNetIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscModFrsDprsNetIndex.setStatus("mandatory")
_MscModFrsDprsNetTpm_ObjectIdentity = ObjectIdentity
mscModFrsDprsNetTpm = _MscModFrsDprsNetTpm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 3, 3, 2)
)
_MscModFrsDprsNetTpmRowStatusTable_Object = MibTable
mscModFrsDprsNetTpmRowStatusTable = _MscModFrsDprsNetTpmRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 3, 3, 2, 1)
)
if mibBuilder.loadTexts:
    mscModFrsDprsNetTpmRowStatusTable.setStatus("mandatory")
_MscModFrsDprsNetTpmRowStatusEntry_Object = MibTableRow
mscModFrsDprsNetTpmRowStatusEntry = _MscModFrsDprsNetTpmRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 3, 3, 2, 1, 1)
)
mscModFrsDprsNetTpmRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscModIndex"),
    (0, "Nortel-MsCarrier-MscPassport-ModCommonMIB", "mscModFrsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-ModDprsQosMIB", "mscModFrsDprsNetIndex"),
    (0, "Nortel-MsCarrier-MscPassport-ModDprsQosMIB", "mscModFrsDprsNetTpmIndex"),
)
if mibBuilder.loadTexts:
    mscModFrsDprsNetTpmRowStatusEntry.setStatus("mandatory")
_MscModFrsDprsNetTpmRowStatus_Type = RowStatus
_MscModFrsDprsNetTpmRowStatus_Object = MibTableColumn
mscModFrsDprsNetTpmRowStatus = _MscModFrsDprsNetTpmRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 3, 3, 2, 1, 1, 1),
    _MscModFrsDprsNetTpmRowStatus_Type()
)
mscModFrsDprsNetTpmRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscModFrsDprsNetTpmRowStatus.setStatus("mandatory")
_MscModFrsDprsNetTpmComponentName_Type = DisplayString
_MscModFrsDprsNetTpmComponentName_Object = MibTableColumn
mscModFrsDprsNetTpmComponentName = _MscModFrsDprsNetTpmComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 3, 3, 2, 1, 1, 2),
    _MscModFrsDprsNetTpmComponentName_Type()
)
mscModFrsDprsNetTpmComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscModFrsDprsNetTpmComponentName.setStatus("mandatory")
_MscModFrsDprsNetTpmStorageType_Type = StorageType
_MscModFrsDprsNetTpmStorageType_Object = MibTableColumn
mscModFrsDprsNetTpmStorageType = _MscModFrsDprsNetTpmStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 3, 3, 2, 1, 1, 4),
    _MscModFrsDprsNetTpmStorageType_Type()
)
mscModFrsDprsNetTpmStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscModFrsDprsNetTpmStorageType.setStatus("mandatory")


class _MscModFrsDprsNetTpmIndex_Type(Integer32):
    """Custom type mscModFrsDprsNetTpmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_MscModFrsDprsNetTpmIndex_Type.__name__ = "Integer32"
_MscModFrsDprsNetTpmIndex_Object = MibTableColumn
mscModFrsDprsNetTpmIndex = _MscModFrsDprsNetTpmIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 3, 3, 2, 1, 1, 10),
    _MscModFrsDprsNetTpmIndex_Type()
)
mscModFrsDprsNetTpmIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscModFrsDprsNetTpmIndex.setStatus("mandatory")
_MscModFrsDprsNetTpmProvTable_Object = MibTable
mscModFrsDprsNetTpmProvTable = _MscModFrsDprsNetTpmProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 3, 3, 2, 10)
)
if mibBuilder.loadTexts:
    mscModFrsDprsNetTpmProvTable.setStatus("mandatory")
_MscModFrsDprsNetTpmProvEntry_Object = MibTableRow
mscModFrsDprsNetTpmProvEntry = _MscModFrsDprsNetTpmProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 3, 3, 2, 10, 1)
)
mscModFrsDprsNetTpmProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscModIndex"),
    (0, "Nortel-MsCarrier-MscPassport-ModCommonMIB", "mscModFrsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-ModDprsQosMIB", "mscModFrsDprsNetIndex"),
    (0, "Nortel-MsCarrier-MscPassport-ModDprsQosMIB", "mscModFrsDprsNetTpmIndex"),
)
if mibBuilder.loadTexts:
    mscModFrsDprsNetTpmProvEntry.setStatus("mandatory")


class _MscModFrsDprsNetTpmEmissionPriority_Type(Unsigned32):
    """Custom type mscModFrsDprsNetTpmEmissionPriority based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_MscModFrsDprsNetTpmEmissionPriority_Type.__name__ = "Unsigned32"
_MscModFrsDprsNetTpmEmissionPriority_Object = MibTableColumn
mscModFrsDprsNetTpmEmissionPriority = _MscModFrsDprsNetTpmEmissionPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 3, 3, 2, 10, 1, 1),
    _MscModFrsDprsNetTpmEmissionPriority_Type()
)
mscModFrsDprsNetTpmEmissionPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscModFrsDprsNetTpmEmissionPriority.setStatus("mandatory")


class _MscModFrsDprsNetTpmRoutingClassOfService_Type(Integer32):
    """Custom type mscModFrsDprsNetTpmRoutingClassOfService based on Integer32"""
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
        *(("delay", 1),
          ("multimedia", 2),
          ("throughput", 0))
    )


_MscModFrsDprsNetTpmRoutingClassOfService_Type.__name__ = "Integer32"
_MscModFrsDprsNetTpmRoutingClassOfService_Object = MibTableColumn
mscModFrsDprsNetTpmRoutingClassOfService = _MscModFrsDprsNetTpmRoutingClassOfService_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 3, 3, 2, 10, 1, 2),
    _MscModFrsDprsNetTpmRoutingClassOfService_Type()
)
mscModFrsDprsNetTpmRoutingClassOfService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscModFrsDprsNetTpmRoutingClassOfService.setStatus("mandatory")


class _MscModFrsDprsNetTpmAssignedIngressBandwidthPool_Type(Unsigned32):
    """Custom type mscModFrsDprsNetTpmAssignedIngressBandwidthPool based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_MscModFrsDprsNetTpmAssignedIngressBandwidthPool_Type.__name__ = "Unsigned32"
_MscModFrsDprsNetTpmAssignedIngressBandwidthPool_Object = MibTableColumn
mscModFrsDprsNetTpmAssignedIngressBandwidthPool = _MscModFrsDprsNetTpmAssignedIngressBandwidthPool_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 3, 3, 2, 10, 1, 3),
    _MscModFrsDprsNetTpmAssignedIngressBandwidthPool_Type()
)
mscModFrsDprsNetTpmAssignedIngressBandwidthPool.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscModFrsDprsNetTpmAssignedIngressBandwidthPool.setStatus("mandatory")


class _MscModFrsDprsNetTpmAssignedEgressBandwidthPool_Type(Unsigned32):
    """Custom type mscModFrsDprsNetTpmAssignedEgressBandwidthPool based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_MscModFrsDprsNetTpmAssignedEgressBandwidthPool_Type.__name__ = "Unsigned32"
_MscModFrsDprsNetTpmAssignedEgressBandwidthPool_Object = MibTableColumn
mscModFrsDprsNetTpmAssignedEgressBandwidthPool = _MscModFrsDprsNetTpmAssignedEgressBandwidthPool_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 3, 3, 2, 10, 1, 4),
    _MscModFrsDprsNetTpmAssignedEgressBandwidthPool_Type()
)
mscModFrsDprsNetTpmAssignedEgressBandwidthPool.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscModFrsDprsNetTpmAssignedEgressBandwidthPool.setStatus("mandatory")
_ModDprsQosMIB_ObjectIdentity = ObjectIdentity
modDprsQosMIB = _ModDprsQosMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 76)
)
_ModDprsQosGroup_ObjectIdentity = ObjectIdentity
modDprsQosGroup = _ModDprsQosGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 76, 1)
)
_ModDprsQosGroupCA_ObjectIdentity = ObjectIdentity
modDprsQosGroupCA = _ModDprsQosGroupCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 76, 1, 1)
)
_ModDprsQosGroupCA02_ObjectIdentity = ObjectIdentity
modDprsQosGroupCA02 = _ModDprsQosGroupCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 76, 1, 1, 3)
)
_ModDprsQosGroupCA02A_ObjectIdentity = ObjectIdentity
modDprsQosGroupCA02A = _ModDprsQosGroupCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 76, 1, 1, 3, 2)
)
_ModDprsQosCapabilities_ObjectIdentity = ObjectIdentity
modDprsQosCapabilities = _ModDprsQosCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 76, 3)
)
_ModDprsQosCapabilitiesCA_ObjectIdentity = ObjectIdentity
modDprsQosCapabilitiesCA = _ModDprsQosCapabilitiesCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 76, 3, 1)
)
_ModDprsQosCapabilitiesCA02_ObjectIdentity = ObjectIdentity
modDprsQosCapabilitiesCA02 = _ModDprsQosCapabilitiesCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 76, 3, 1, 3)
)
_ModDprsQosCapabilitiesCA02A_ObjectIdentity = ObjectIdentity
modDprsQosCapabilitiesCA02A = _ModDprsQosCapabilitiesCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 76, 3, 1, 3, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-MsCarrier-MscPassport-ModDprsQosMIB",
    **{"mscModFrsDprsNet": mscModFrsDprsNet,
       "mscModFrsDprsNetRowStatusTable": mscModFrsDprsNetRowStatusTable,
       "mscModFrsDprsNetRowStatusEntry": mscModFrsDprsNetRowStatusEntry,
       "mscModFrsDprsNetRowStatus": mscModFrsDprsNetRowStatus,
       "mscModFrsDprsNetComponentName": mscModFrsDprsNetComponentName,
       "mscModFrsDprsNetStorageType": mscModFrsDprsNetStorageType,
       "mscModFrsDprsNetIndex": mscModFrsDprsNetIndex,
       "mscModFrsDprsNetTpm": mscModFrsDprsNetTpm,
       "mscModFrsDprsNetTpmRowStatusTable": mscModFrsDprsNetTpmRowStatusTable,
       "mscModFrsDprsNetTpmRowStatusEntry": mscModFrsDprsNetTpmRowStatusEntry,
       "mscModFrsDprsNetTpmRowStatus": mscModFrsDprsNetTpmRowStatus,
       "mscModFrsDprsNetTpmComponentName": mscModFrsDprsNetTpmComponentName,
       "mscModFrsDprsNetTpmStorageType": mscModFrsDprsNetTpmStorageType,
       "mscModFrsDprsNetTpmIndex": mscModFrsDprsNetTpmIndex,
       "mscModFrsDprsNetTpmProvTable": mscModFrsDprsNetTpmProvTable,
       "mscModFrsDprsNetTpmProvEntry": mscModFrsDprsNetTpmProvEntry,
       "mscModFrsDprsNetTpmEmissionPriority": mscModFrsDprsNetTpmEmissionPriority,
       "mscModFrsDprsNetTpmRoutingClassOfService": mscModFrsDprsNetTpmRoutingClassOfService,
       "mscModFrsDprsNetTpmAssignedIngressBandwidthPool": mscModFrsDprsNetTpmAssignedIngressBandwidthPool,
       "mscModFrsDprsNetTpmAssignedEgressBandwidthPool": mscModFrsDprsNetTpmAssignedEgressBandwidthPool,
       "modDprsQosMIB": modDprsQosMIB,
       "modDprsQosGroup": modDprsQosGroup,
       "modDprsQosGroupCA": modDprsQosGroupCA,
       "modDprsQosGroupCA02": modDprsQosGroupCA02,
       "modDprsQosGroupCA02A": modDprsQosGroupCA02A,
       "modDprsQosCapabilities": modDprsQosCapabilities,
       "modDprsQosCapabilitiesCA": modDprsQosCapabilitiesCA,
       "modDprsQosCapabilitiesCA02": modDprsQosCapabilitiesCA02,
       "modDprsQosCapabilitiesCA02A": modDprsQosCapabilitiesCA02A}
)
