# SNMP MIB module (XYLAN-SOFT-PVC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/XYLAN-SOFT-PVC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:19:13 2024
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
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(xylanCsmArch,) = mibBuilder.importSymbols(
    "XYLAN-BASE-MIB",
    "xylanCsmArch")

(AtmxTrafficDescrParamIndex,) = mibBuilder.importSymbols(
    "XYLAN-CSM-MIB",
    "AtmxTrafficDescrParamIndex")


# MODULE-IDENTITY


# Types definitions



class TruthValue(Integer32):
    """Custom type TruthValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )





class AtmxSoftPvcBbcIndex(Integer32):
    """Custom type AtmxSoftPvcBbcIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2048),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AtmxSoftPvcMIB_ObjectIdentity = ObjectIdentity
atmxSoftPvcMIB = _AtmxSoftPvcMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 2)
)
_AtmxSoftPvcMIBObjects_ObjectIdentity = ObjectIdentity
atmxSoftPvcMIBObjects = _AtmxSoftPvcMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 2, 1)
)
_AtmxSoftPvcBaseGroup_ObjectIdentity = ObjectIdentity
atmxSoftPvcBaseGroup = _AtmxSoftPvcBaseGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 2, 1, 1)
)
_AtmxSoftPvcCallFailuresTrapEnable_Type = TruthValue
_AtmxSoftPvcCallFailuresTrapEnable_Object = MibScalar
atmxSoftPvcCallFailuresTrapEnable = _AtmxSoftPvcCallFailuresTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 2, 1, 1, 1),
    _AtmxSoftPvcCallFailuresTrapEnable_Type()
)
atmxSoftPvcCallFailuresTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxSoftPvcCallFailuresTrapEnable.setStatus("mandatory")
_AtmxSoftPvcCallFailures_Type = Counter32
_AtmxSoftPvcCallFailures_Object = MibScalar
atmxSoftPvcCallFailures = _AtmxSoftPvcCallFailures_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 2, 1, 1, 2),
    _AtmxSoftPvcCallFailures_Type()
)
atmxSoftPvcCallFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxSoftPvcCallFailures.setStatus("mandatory")
_AtmxSoftPvcCurrentlyFailingSoftPVccs_Type = Gauge32
_AtmxSoftPvcCurrentlyFailingSoftPVccs_Object = MibScalar
atmxSoftPvcCurrentlyFailingSoftPVccs = _AtmxSoftPvcCurrentlyFailingSoftPVccs_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 2, 1, 1, 3),
    _AtmxSoftPvcCurrentlyFailingSoftPVccs_Type()
)
atmxSoftPvcCurrentlyFailingSoftPVccs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxSoftPvcCurrentlyFailingSoftPVccs.setStatus("mandatory")
_AtmxSoftPvcCurrentlyFailingSoftPVpcs_Type = Gauge32
_AtmxSoftPvcCurrentlyFailingSoftPVpcs_Object = MibScalar
atmxSoftPvcCurrentlyFailingSoftPVpcs = _AtmxSoftPvcCurrentlyFailingSoftPVpcs_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 2, 1, 1, 4),
    _AtmxSoftPvcCurrentlyFailingSoftPVpcs_Type()
)
atmxSoftPvcCurrentlyFailingSoftPVpcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxSoftPvcCurrentlyFailingSoftPVpcs.setStatus("mandatory")


class _AtmxSoftPvcNotificationInterval_Type(Integer32):
    """Custom type atmxSoftPvcNotificationInterval based on Integer32"""
    defaultValue = 30


_AtmxSoftPvcNotificationInterval_Object = MibScalar
atmxSoftPvcNotificationInterval = _AtmxSoftPvcNotificationInterval_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 2, 1, 1, 5),
    _AtmxSoftPvcNotificationInterval_Type()
)
atmxSoftPvcNotificationInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxSoftPvcNotificationInterval.setStatus("mandatory")
_AtmxCurrentlyFailingSoftPVccTable_Object = MibTable
atmxCurrentlyFailingSoftPVccTable = _AtmxCurrentlyFailingSoftPVccTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 2, 1, 2)
)
if mibBuilder.loadTexts:
    atmxCurrentlyFailingSoftPVccTable.setStatus("mandatory")
_AtmxCurrentlyFailingSoftPVccEntry_Object = MibTableRow
atmxCurrentlyFailingSoftPVccEntry = _AtmxCurrentlyFailingSoftPVccEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 2, 1, 2, 1)
)
atmxCurrentlyFailingSoftPVccEntry.setIndexNames(
    (0, "XYLAN-SOFT-PVC-MIB", "atmxCurrentlyFailingSoftPVccSlotIndex"),
    (0, "XYLAN-SOFT-PVC-MIB", "atmxCurrentlyFailingSoftPVccPortIndex"),
    (0, "XYLAN-SOFT-PVC-MIB", "atmxCurrentlyFailingSoftPVccVpi"),
    (0, "XYLAN-SOFT-PVC-MIB", "atmxCurrentlyFailingSoftPVccVci"),
    (0, "XYLAN-SOFT-PVC-MIB", "atmxCurrentlyFailingSoftPVccLeafReference"),
)
if mibBuilder.loadTexts:
    atmxCurrentlyFailingSoftPVccEntry.setStatus("mandatory")
_AtmxCurrentlyFailingSoftPVccSlotIndex_Type = Integer32
_AtmxCurrentlyFailingSoftPVccSlotIndex_Object = MibTableColumn
atmxCurrentlyFailingSoftPVccSlotIndex = _AtmxCurrentlyFailingSoftPVccSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 2, 1, 2, 1, 1),
    _AtmxCurrentlyFailingSoftPVccSlotIndex_Type()
)
atmxCurrentlyFailingSoftPVccSlotIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmxCurrentlyFailingSoftPVccSlotIndex.setStatus("mandatory")
_AtmxCurrentlyFailingSoftPVccPortIndex_Type = Integer32
_AtmxCurrentlyFailingSoftPVccPortIndex_Object = MibTableColumn
atmxCurrentlyFailingSoftPVccPortIndex = _AtmxCurrentlyFailingSoftPVccPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 2, 1, 2, 1, 2),
    _AtmxCurrentlyFailingSoftPVccPortIndex_Type()
)
atmxCurrentlyFailingSoftPVccPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmxCurrentlyFailingSoftPVccPortIndex.setStatus("mandatory")
_AtmxCurrentlyFailingSoftPVccVpi_Type = Integer32
_AtmxCurrentlyFailingSoftPVccVpi_Object = MibTableColumn
atmxCurrentlyFailingSoftPVccVpi = _AtmxCurrentlyFailingSoftPVccVpi_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 2, 1, 2, 1, 3),
    _AtmxCurrentlyFailingSoftPVccVpi_Type()
)
atmxCurrentlyFailingSoftPVccVpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmxCurrentlyFailingSoftPVccVpi.setStatus("mandatory")
_AtmxCurrentlyFailingSoftPVccVci_Type = Integer32
_AtmxCurrentlyFailingSoftPVccVci_Object = MibTableColumn
atmxCurrentlyFailingSoftPVccVci = _AtmxCurrentlyFailingSoftPVccVci_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 2, 1, 2, 1, 4),
    _AtmxCurrentlyFailingSoftPVccVci_Type()
)
atmxCurrentlyFailingSoftPVccVci.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmxCurrentlyFailingSoftPVccVci.setStatus("mandatory")
_AtmxCurrentlyFailingSoftPVccLeafReference_Type = Integer32
_AtmxCurrentlyFailingSoftPVccLeafReference_Object = MibTableColumn
atmxCurrentlyFailingSoftPVccLeafReference = _AtmxCurrentlyFailingSoftPVccLeafReference_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 2, 1, 2, 1, 5),
    _AtmxCurrentlyFailingSoftPVccLeafReference_Type()
)
atmxCurrentlyFailingSoftPVccLeafReference.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmxCurrentlyFailingSoftPVccLeafReference.setStatus("mandatory")
_AtmxCurrentlyFailingSoftPVccTimeStamp_Type = DisplayString
_AtmxCurrentlyFailingSoftPVccTimeStamp_Object = MibTableColumn
atmxCurrentlyFailingSoftPVccTimeStamp = _AtmxCurrentlyFailingSoftPVccTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 2, 1, 2, 1, 6),
    _AtmxCurrentlyFailingSoftPVccTimeStamp_Type()
)
atmxCurrentlyFailingSoftPVccTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxCurrentlyFailingSoftPVccTimeStamp.setStatus("mandatory")
_AtmxCurrentlyFailingSoftPVpcTable_Object = MibTable
atmxCurrentlyFailingSoftPVpcTable = _AtmxCurrentlyFailingSoftPVpcTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 2, 1, 3)
)
if mibBuilder.loadTexts:
    atmxCurrentlyFailingSoftPVpcTable.setStatus("mandatory")
_AtmxCurrentlyFailingSoftPVpcEntry_Object = MibTableRow
atmxCurrentlyFailingSoftPVpcEntry = _AtmxCurrentlyFailingSoftPVpcEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 2, 1, 3, 1)
)
atmxCurrentlyFailingSoftPVpcEntry.setIndexNames(
    (0, "XYLAN-SOFT-PVC-MIB", "atmxCurrentlyFailingSoftPVpcSlotIndex"),
    (0, "XYLAN-SOFT-PVC-MIB", "atmxCurrentlyFailingSoftPVpcPortIndex"),
    (0, "XYLAN-SOFT-PVC-MIB", "atmxCurrentlyFailingSoftPVpcVpi"),
    (0, "XYLAN-SOFT-PVC-MIB", "atmxCurrentlyFailingSoftPVpcLeafReference"),
)
if mibBuilder.loadTexts:
    atmxCurrentlyFailingSoftPVpcEntry.setStatus("mandatory")
_AtmxCurrentlyFailingSoftPVpcSlotIndex_Type = Integer32
_AtmxCurrentlyFailingSoftPVpcSlotIndex_Object = MibTableColumn
atmxCurrentlyFailingSoftPVpcSlotIndex = _AtmxCurrentlyFailingSoftPVpcSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 2, 1, 3, 1, 1),
    _AtmxCurrentlyFailingSoftPVpcSlotIndex_Type()
)
atmxCurrentlyFailingSoftPVpcSlotIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmxCurrentlyFailingSoftPVpcSlotIndex.setStatus("mandatory")
_AtmxCurrentlyFailingSoftPVpcPortIndex_Type = Integer32
_AtmxCurrentlyFailingSoftPVpcPortIndex_Object = MibTableColumn
atmxCurrentlyFailingSoftPVpcPortIndex = _AtmxCurrentlyFailingSoftPVpcPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 2, 1, 3, 1, 2),
    _AtmxCurrentlyFailingSoftPVpcPortIndex_Type()
)
atmxCurrentlyFailingSoftPVpcPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmxCurrentlyFailingSoftPVpcPortIndex.setStatus("mandatory")
_AtmxCurrentlyFailingSoftPVpcVpi_Type = Integer32
_AtmxCurrentlyFailingSoftPVpcVpi_Object = MibTableColumn
atmxCurrentlyFailingSoftPVpcVpi = _AtmxCurrentlyFailingSoftPVpcVpi_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 2, 1, 3, 1, 3),
    _AtmxCurrentlyFailingSoftPVpcVpi_Type()
)
atmxCurrentlyFailingSoftPVpcVpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmxCurrentlyFailingSoftPVpcVpi.setStatus("mandatory")
_AtmxCurrentlyFailingSoftPVpcLeafReference_Type = Integer32
_AtmxCurrentlyFailingSoftPVpcLeafReference_Object = MibTableColumn
atmxCurrentlyFailingSoftPVpcLeafReference = _AtmxCurrentlyFailingSoftPVpcLeafReference_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 2, 1, 3, 1, 4),
    _AtmxCurrentlyFailingSoftPVpcLeafReference_Type()
)
atmxCurrentlyFailingSoftPVpcLeafReference.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmxCurrentlyFailingSoftPVpcLeafReference.setStatus("mandatory")
_AtmxCurrentlyFailingSoftPVpcTimeStamp_Type = DisplayString
_AtmxCurrentlyFailingSoftPVpcTimeStamp_Object = MibTableColumn
atmxCurrentlyFailingSoftPVpcTimeStamp = _AtmxCurrentlyFailingSoftPVpcTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 2, 1, 3, 1, 5),
    _AtmxCurrentlyFailingSoftPVpcTimeStamp_Type()
)
atmxCurrentlyFailingSoftPVpcTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxCurrentlyFailingSoftPVpcTimeStamp.setStatus("mandatory")
_XylnatmSoftPVpcTable_Object = MibTable
xylnatmSoftPVpcTable = _XylnatmSoftPVpcTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 2, 1, 4)
)
if mibBuilder.loadTexts:
    xylnatmSoftPVpcTable.setStatus("mandatory")
_XylnatmSoftPVpcEntry_Object = MibTableRow
xylnatmSoftPVpcEntry = _XylnatmSoftPVpcEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 2, 1, 4, 1)
)
xylnatmSoftPVpcEntry.setIndexNames(
    (0, "XYLAN-SOFT-PVC-MIB", "xylnatmSoftPVpcSlotIndex"),
    (0, "XYLAN-SOFT-PVC-MIB", "xylnatmSoftPVpcPortIndex"),
    (0, "XYLAN-SOFT-PVC-MIB", "xylnatmSoftPVpcVpi"),
    (0, "XYLAN-SOFT-PVC-MIB", "xylnatmSoftPVpcLeafReference"),
)
if mibBuilder.loadTexts:
    xylnatmSoftPVpcEntry.setStatus("mandatory")


class _XylnatmSoftPVpcSlotIndex_Type(Integer32):
    """Custom type xylnatmSoftPVpcSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_XylnatmSoftPVpcSlotIndex_Type.__name__ = "Integer32"
_XylnatmSoftPVpcSlotIndex_Object = MibTableColumn
xylnatmSoftPVpcSlotIndex = _XylnatmSoftPVpcSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 2, 1, 4, 1, 1),
    _XylnatmSoftPVpcSlotIndex_Type()
)
xylnatmSoftPVpcSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmSoftPVpcSlotIndex.setStatus("mandatory")
_XylnatmSoftPVpcPortIndex_Type = Integer32
_XylnatmSoftPVpcPortIndex_Object = MibTableColumn
xylnatmSoftPVpcPortIndex = _XylnatmSoftPVpcPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 2, 1, 4, 1, 2),
    _XylnatmSoftPVpcPortIndex_Type()
)
xylnatmSoftPVpcPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmSoftPVpcPortIndex.setStatus("mandatory")


class _XylnatmSoftPVpcVpi_Type(Integer32):
    """Custom type xylnatmSoftPVpcVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_XylnatmSoftPVpcVpi_Type.__name__ = "Integer32"
_XylnatmSoftPVpcVpi_Object = MibTableColumn
xylnatmSoftPVpcVpi = _XylnatmSoftPVpcVpi_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 2, 1, 4, 1, 3),
    _XylnatmSoftPVpcVpi_Type()
)
xylnatmSoftPVpcVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmSoftPVpcVpi.setStatus("mandatory")


class _XylnatmSoftPVpcLeafReference_Type(Integer32):
    """Custom type xylnatmSoftPVpcLeafReference based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_XylnatmSoftPVpcLeafReference_Type.__name__ = "Integer32"
_XylnatmSoftPVpcLeafReference_Object = MibTableColumn
xylnatmSoftPVpcLeafReference = _XylnatmSoftPVpcLeafReference_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 2, 1, 4, 1, 4),
    _XylnatmSoftPVpcLeafReference_Type()
)
xylnatmSoftPVpcLeafReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmSoftPVpcLeafReference.setStatus("mandatory")
_XylnatmSoftPVpcTargetAddress_Type = DisplayString
_XylnatmSoftPVpcTargetAddress_Object = MibTableColumn
xylnatmSoftPVpcTargetAddress = _XylnatmSoftPVpcTargetAddress_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 2, 1, 4, 1, 5),
    _XylnatmSoftPVpcTargetAddress_Type()
)
xylnatmSoftPVpcTargetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylnatmSoftPVpcTargetAddress.setStatus("mandatory")


class _XylnatmSoftPVpcTargetSelectType_Type(Integer32):
    """Custom type xylnatmSoftPVpcTargetSelectType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("any", 2),
          ("required", 1))
    )


_XylnatmSoftPVpcTargetSelectType_Type.__name__ = "Integer32"
_XylnatmSoftPVpcTargetSelectType_Object = MibTableColumn
xylnatmSoftPVpcTargetSelectType = _XylnatmSoftPVpcTargetSelectType_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 2, 1, 4, 1, 6),
    _XylnatmSoftPVpcTargetSelectType_Type()
)
xylnatmSoftPVpcTargetSelectType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylnatmSoftPVpcTargetSelectType.setStatus("mandatory")


class _XylnatmSoftPVpcTargetVpi_Type(Integer32):
    """Custom type xylnatmSoftPVpcTargetVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_XylnatmSoftPVpcTargetVpi_Type.__name__ = "Integer32"
_XylnatmSoftPVpcTargetVpi_Object = MibTableColumn
xylnatmSoftPVpcTargetVpi = _XylnatmSoftPVpcTargetVpi_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 2, 1, 4, 1, 7),
    _XylnatmSoftPVpcTargetVpi_Type()
)
xylnatmSoftPVpcTargetVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylnatmSoftPVpcTargetVpi.setStatus("mandatory")


class _XylnatmSoftPVpcLastReleaseCause_Type(Integer32):
    """Custom type xylnatmSoftPVpcLastReleaseCause based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_XylnatmSoftPVpcLastReleaseCause_Type.__name__ = "Integer32"
_XylnatmSoftPVpcLastReleaseCause_Object = MibTableColumn
xylnatmSoftPVpcLastReleaseCause = _XylnatmSoftPVpcLastReleaseCause_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 2, 1, 4, 1, 8),
    _XylnatmSoftPVpcLastReleaseCause_Type()
)
xylnatmSoftPVpcLastReleaseCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmSoftPVpcLastReleaseCause.setStatus("mandatory")


class _XylnatmSoftPVpcLastReleaseDiagnostic_Type(OctetString):
    """Custom type xylnatmSoftPVpcLastReleaseDiagnostic based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_XylnatmSoftPVpcLastReleaseDiagnostic_Type.__name__ = "OctetString"
_XylnatmSoftPVpcLastReleaseDiagnostic_Object = MibTableColumn
xylnatmSoftPVpcLastReleaseDiagnostic = _XylnatmSoftPVpcLastReleaseDiagnostic_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 2, 1, 4, 1, 9),
    _XylnatmSoftPVpcLastReleaseDiagnostic_Type()
)
xylnatmSoftPVpcLastReleaseDiagnostic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmSoftPVpcLastReleaseDiagnostic.setStatus("mandatory")


class _XylnatmSoftPVpcOperStatus_Type(Integer32):
    """Custom type xylnatmSoftPVpcOperStatus based on Integer32"""
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
        *(("connected", 3),
          ("establishmentInProgress", 2),
          ("other", 1),
          ("retriesExhausted", 4))
    )


_XylnatmSoftPVpcOperStatus_Type.__name__ = "Integer32"
_XylnatmSoftPVpcOperStatus_Object = MibTableColumn
xylnatmSoftPVpcOperStatus = _XylnatmSoftPVpcOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 2, 1, 4, 1, 10),
    _XylnatmSoftPVpcOperStatus_Type()
)
xylnatmSoftPVpcOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmSoftPVpcOperStatus.setStatus("mandatory")


class _XylnatmSoftPVpcRestart_Type(Integer32):
    """Custom type xylnatmSoftPVpcRestart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noop", 2),
          ("restart", 1))
    )


_XylnatmSoftPVpcRestart_Type.__name__ = "Integer32"
_XylnatmSoftPVpcRestart_Object = MibTableColumn
xylnatmSoftPVpcRestart = _XylnatmSoftPVpcRestart_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 2, 1, 4, 1, 11),
    _XylnatmSoftPVpcRestart_Type()
)
xylnatmSoftPVpcRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylnatmSoftPVpcRestart.setStatus("mandatory")


class _XylnatmSoftPVpcRetryInterval_Type(Integer32):
    """Custom type xylnatmSoftPVpcRetryInterval based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_XylnatmSoftPVpcRetryInterval_Type.__name__ = "Integer32"
_XylnatmSoftPVpcRetryInterval_Object = MibTableColumn
xylnatmSoftPVpcRetryInterval = _XylnatmSoftPVpcRetryInterval_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 2, 1, 4, 1, 12),
    _XylnatmSoftPVpcRetryInterval_Type()
)
xylnatmSoftPVpcRetryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylnatmSoftPVpcRetryInterval.setStatus("mandatory")


class _XylnatmSoftPVpcRetryTimer_Type(Integer32):
    """Custom type xylnatmSoftPVpcRetryTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_XylnatmSoftPVpcRetryTimer_Type.__name__ = "Integer32"
_XylnatmSoftPVpcRetryTimer_Object = MibTableColumn
xylnatmSoftPVpcRetryTimer = _XylnatmSoftPVpcRetryTimer_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 2, 1, 4, 1, 13),
    _XylnatmSoftPVpcRetryTimer_Type()
)
xylnatmSoftPVpcRetryTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmSoftPVpcRetryTimer.setStatus("mandatory")


class _XylnatmSoftPVpcRetryThreshold_Type(Integer32):
    """Custom type xylnatmSoftPVpcRetryThreshold based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_XylnatmSoftPVpcRetryThreshold_Type.__name__ = "Integer32"
_XylnatmSoftPVpcRetryThreshold_Object = MibTableColumn
xylnatmSoftPVpcRetryThreshold = _XylnatmSoftPVpcRetryThreshold_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 2, 1, 4, 1, 14),
    _XylnatmSoftPVpcRetryThreshold_Type()
)
xylnatmSoftPVpcRetryThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylnatmSoftPVpcRetryThreshold.setStatus("mandatory")
_XylnatmSoftPVpcRetryFailures_Type = Gauge32
_XylnatmSoftPVpcRetryFailures_Object = MibTableColumn
xylnatmSoftPVpcRetryFailures = _XylnatmSoftPVpcRetryFailures_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 2, 1, 4, 1, 15),
    _XylnatmSoftPVpcRetryFailures_Type()
)
xylnatmSoftPVpcRetryFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmSoftPVpcRetryFailures.setStatus("mandatory")


class _XylnatmSoftPVpcRetryLimit_Type(Integer32):
    """Custom type xylnatmSoftPVpcRetryLimit based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_XylnatmSoftPVpcRetryLimit_Type.__name__ = "Integer32"
_XylnatmSoftPVpcRetryLimit_Object = MibTableColumn
xylnatmSoftPVpcRetryLimit = _XylnatmSoftPVpcRetryLimit_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 2, 1, 4, 1, 16),
    _XylnatmSoftPVpcRetryLimit_Type()
)
xylnatmSoftPVpcRetryLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylnatmSoftPVpcRetryLimit.setStatus("mandatory")
_XylnatmSoftPVpcLowTDIndex_Type = AtmxTrafficDescrParamIndex
_XylnatmSoftPVpcLowTDIndex_Object = MibTableColumn
xylnatmSoftPVpcLowTDIndex = _XylnatmSoftPVpcLowTDIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 2, 1, 4, 1, 17),
    _XylnatmSoftPVpcLowTDIndex_Type()
)
xylnatmSoftPVpcLowTDIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylnatmSoftPVpcLowTDIndex.setStatus("mandatory")
_XylnatmSoftPVpcHighTDIndex_Type = AtmxTrafficDescrParamIndex
_XylnatmSoftPVpcHighTDIndex_Object = MibTableColumn
xylnatmSoftPVpcHighTDIndex = _XylnatmSoftPVpcHighTDIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 2, 1, 4, 1, 18),
    _XylnatmSoftPVpcHighTDIndex_Type()
)
xylnatmSoftPVpcHighTDIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylnatmSoftPVpcHighTDIndex.setStatus("mandatory")
_XylnatmSoftPVpcLastChange_Type = DisplayString
_XylnatmSoftPVpcLastChange_Object = MibTableColumn
xylnatmSoftPVpcLastChange = _XylnatmSoftPVpcLastChange_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 2, 1, 4, 1, 19),
    _XylnatmSoftPVpcLastChange_Type()
)
xylnatmSoftPVpcLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmSoftPVpcLastChange.setStatus("mandatory")
_XylnatmSoftPVpcOutSlot_Type = Integer32
_XylnatmSoftPVpcOutSlot_Object = MibTableColumn
xylnatmSoftPVpcOutSlot = _XylnatmSoftPVpcOutSlot_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 2, 1, 4, 1, 20),
    _XylnatmSoftPVpcOutSlot_Type()
)
xylnatmSoftPVpcOutSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmSoftPVpcOutSlot.setStatus("mandatory")
_XylnatmSoftPVpcOutPort_Type = Integer32
_XylnatmSoftPVpcOutPort_Object = MibTableColumn
xylnatmSoftPVpcOutPort = _XylnatmSoftPVpcOutPort_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 2, 1, 4, 1, 21),
    _XylnatmSoftPVpcOutPort_Type()
)
xylnatmSoftPVpcOutPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmSoftPVpcOutPort.setStatus("mandatory")
_XylnatmSoftPVpcOutVpi_Type = Integer32
_XylnatmSoftPVpcOutVpi_Object = MibTableColumn
xylnatmSoftPVpcOutVpi = _XylnatmSoftPVpcOutVpi_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 2, 1, 4, 1, 22),
    _XylnatmSoftPVpcOutVpi_Type()
)
xylnatmSoftPVpcOutVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmSoftPVpcOutVpi.setStatus("mandatory")
_XylnatmSoftPVpcAdminStatus_Type = Integer32
_XylnatmSoftPVpcAdminStatus_Object = MibTableColumn
xylnatmSoftPVpcAdminStatus = _XylnatmSoftPVpcAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 2, 1, 4, 1, 23),
    _XylnatmSoftPVpcAdminStatus_Type()
)
xylnatmSoftPVpcAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylnatmSoftPVpcAdminStatus.setStatus("mandatory")
_XylnatmSoftPVpcCrossConnectIdentifier_Type = Integer32
_XylnatmSoftPVpcCrossConnectIdentifier_Object = MibTableColumn
xylnatmSoftPVpcCrossConnectIdentifier = _XylnatmSoftPVpcCrossConnectIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 2, 1, 4, 1, 24),
    _XylnatmSoftPVpcCrossConnectIdentifier_Type()
)
xylnatmSoftPVpcCrossConnectIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmSoftPVpcCrossConnectIdentifier.setStatus("mandatory")
_XylnatmSoftPVpcBbcIndex_Type = Integer32
_XylnatmSoftPVpcBbcIndex_Object = MibTableColumn
xylnatmSoftPVpcBbcIndex = _XylnatmSoftPVpcBbcIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 2, 1, 4, 1, 25),
    _XylnatmSoftPVpcBbcIndex_Type()
)
xylnatmSoftPVpcBbcIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylnatmSoftPVpcBbcIndex.setStatus("mandatory")


class _XylnatmSoftPVpcRowStatus_Type(Integer32):
    """Custom type xylnatmSoftPVpcRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("active", 4),
          ("create", 1),
          ("delete", 3),
          ("modify", 2),
          ("unknown", 5))
    )


_XylnatmSoftPVpcRowStatus_Type.__name__ = "Integer32"
_XylnatmSoftPVpcRowStatus_Object = MibTableColumn
xylnatmSoftPVpcRowStatus = _XylnatmSoftPVpcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 2, 1, 4, 1, 26),
    _XylnatmSoftPVpcRowStatus_Type()
)
xylnatmSoftPVpcRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylnatmSoftPVpcRowStatus.setStatus("mandatory")
_XylnatmSoftPVccTable_Object = MibTable
xylnatmSoftPVccTable = _XylnatmSoftPVccTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 2, 1, 5)
)
if mibBuilder.loadTexts:
    xylnatmSoftPVccTable.setStatus("mandatory")
_XylnatmSoftPVccEntry_Object = MibTableRow
xylnatmSoftPVccEntry = _XylnatmSoftPVccEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 2, 1, 5, 1)
)
xylnatmSoftPVccEntry.setIndexNames(
    (0, "XYLAN-SOFT-PVC-MIB", "xylnatmSoftPVccSlotIndex"),
    (0, "XYLAN-SOFT-PVC-MIB", "xylnatmSoftPVccPortIndex"),
    (0, "XYLAN-SOFT-PVC-MIB", "xylnatmSoftPVccVpi"),
    (0, "XYLAN-SOFT-PVC-MIB", "xylnatmSoftPVccVci"),
    (0, "XYLAN-SOFT-PVC-MIB", "xylnatmSoftPVccLeafReference"),
)
if mibBuilder.loadTexts:
    xylnatmSoftPVccEntry.setStatus("mandatory")
_XylnatmSoftPVccSlotIndex_Type = Integer32
_XylnatmSoftPVccSlotIndex_Object = MibTableColumn
xylnatmSoftPVccSlotIndex = _XylnatmSoftPVccSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 2, 1, 5, 1, 1),
    _XylnatmSoftPVccSlotIndex_Type()
)
xylnatmSoftPVccSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmSoftPVccSlotIndex.setStatus("mandatory")
_XylnatmSoftPVccPortIndex_Type = Integer32
_XylnatmSoftPVccPortIndex_Object = MibTableColumn
xylnatmSoftPVccPortIndex = _XylnatmSoftPVccPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 2, 1, 5, 1, 2),
    _XylnatmSoftPVccPortIndex_Type()
)
xylnatmSoftPVccPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmSoftPVccPortIndex.setStatus("mandatory")
_XylnatmSoftPVccVpi_Type = Integer32
_XylnatmSoftPVccVpi_Object = MibTableColumn
xylnatmSoftPVccVpi = _XylnatmSoftPVccVpi_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 2, 1, 5, 1, 3),
    _XylnatmSoftPVccVpi_Type()
)
xylnatmSoftPVccVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmSoftPVccVpi.setStatus("mandatory")
_XylnatmSoftPVccVci_Type = Integer32
_XylnatmSoftPVccVci_Object = MibTableColumn
xylnatmSoftPVccVci = _XylnatmSoftPVccVci_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 2, 1, 5, 1, 4),
    _XylnatmSoftPVccVci_Type()
)
xylnatmSoftPVccVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmSoftPVccVci.setStatus("mandatory")
_XylnatmSoftPVccLeafReference_Type = Integer32
_XylnatmSoftPVccLeafReference_Object = MibTableColumn
xylnatmSoftPVccLeafReference = _XylnatmSoftPVccLeafReference_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 2, 1, 5, 1, 5),
    _XylnatmSoftPVccLeafReference_Type()
)
xylnatmSoftPVccLeafReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmSoftPVccLeafReference.setStatus("mandatory")
_XylnatmSoftPVccTargetAddress_Type = DisplayString
_XylnatmSoftPVccTargetAddress_Object = MibTableColumn
xylnatmSoftPVccTargetAddress = _XylnatmSoftPVccTargetAddress_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 2, 1, 5, 1, 6),
    _XylnatmSoftPVccTargetAddress_Type()
)
xylnatmSoftPVccTargetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylnatmSoftPVccTargetAddress.setStatus("mandatory")


class _XylnatmSoftPVccTargetSelectType_Type(Integer32):
    """Custom type xylnatmSoftPVccTargetSelectType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("any", 2),
          ("required", 1))
    )


_XylnatmSoftPVccTargetSelectType_Type.__name__ = "Integer32"
_XylnatmSoftPVccTargetSelectType_Object = MibTableColumn
xylnatmSoftPVccTargetSelectType = _XylnatmSoftPVccTargetSelectType_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 2, 1, 5, 1, 7),
    _XylnatmSoftPVccTargetSelectType_Type()
)
xylnatmSoftPVccTargetSelectType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylnatmSoftPVccTargetSelectType.setStatus("mandatory")


class _XylnatmSoftPVccTargetVpi_Type(Integer32):
    """Custom type xylnatmSoftPVccTargetVpi based on Integer32"""
    defaultValue = 0


_XylnatmSoftPVccTargetVpi_Object = MibTableColumn
xylnatmSoftPVccTargetVpi = _XylnatmSoftPVccTargetVpi_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 2, 1, 5, 1, 8),
    _XylnatmSoftPVccTargetVpi_Type()
)
xylnatmSoftPVccTargetVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylnatmSoftPVccTargetVpi.setStatus("mandatory")
_XylnatmSoftPVccTargetVci_Type = Integer32
_XylnatmSoftPVccTargetVci_Object = MibTableColumn
xylnatmSoftPVccTargetVci = _XylnatmSoftPVccTargetVci_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 2, 1, 5, 1, 9),
    _XylnatmSoftPVccTargetVci_Type()
)
xylnatmSoftPVccTargetVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylnatmSoftPVccTargetVci.setStatus("mandatory")
_XylnatmSoftPVccLastReleaseCause_Type = Integer32
_XylnatmSoftPVccLastReleaseCause_Object = MibTableColumn
xylnatmSoftPVccLastReleaseCause = _XylnatmSoftPVccLastReleaseCause_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 2, 1, 5, 1, 10),
    _XylnatmSoftPVccLastReleaseCause_Type()
)
xylnatmSoftPVccLastReleaseCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmSoftPVccLastReleaseCause.setStatus("mandatory")
_XylnatmSoftPVccLastReleaseDiagnostic_Type = OctetString
_XylnatmSoftPVccLastReleaseDiagnostic_Object = MibTableColumn
xylnatmSoftPVccLastReleaseDiagnostic = _XylnatmSoftPVccLastReleaseDiagnostic_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 2, 1, 5, 1, 11),
    _XylnatmSoftPVccLastReleaseDiagnostic_Type()
)
xylnatmSoftPVccLastReleaseDiagnostic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmSoftPVccLastReleaseDiagnostic.setStatus("mandatory")


class _XylnatmSoftPVccOperStatus_Type(Integer32):
    """Custom type xylnatmSoftPVccOperStatus based on Integer32"""
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
        *(("connected", 3),
          ("establishmentInProgress", 2),
          ("other", 1),
          ("retriesExhausted", 4))
    )


_XylnatmSoftPVccOperStatus_Type.__name__ = "Integer32"
_XylnatmSoftPVccOperStatus_Object = MibTableColumn
xylnatmSoftPVccOperStatus = _XylnatmSoftPVccOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 2, 1, 5, 1, 12),
    _XylnatmSoftPVccOperStatus_Type()
)
xylnatmSoftPVccOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmSoftPVccOperStatus.setStatus("mandatory")


class _XylnatmSoftPVccRestart_Type(Integer32):
    """Custom type xylnatmSoftPVccRestart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noop", 2),
          ("restart", 1))
    )


_XylnatmSoftPVccRestart_Type.__name__ = "Integer32"
_XylnatmSoftPVccRestart_Object = MibTableColumn
xylnatmSoftPVccRestart = _XylnatmSoftPVccRestart_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 2, 1, 5, 1, 13),
    _XylnatmSoftPVccRestart_Type()
)
xylnatmSoftPVccRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylnatmSoftPVccRestart.setStatus("mandatory")


class _XylnatmSoftPVccRetryInterval_Type(Integer32):
    """Custom type xylnatmSoftPVccRetryInterval based on Integer32"""
    defaultValue = 10


_XylnatmSoftPVccRetryInterval_Object = MibTableColumn
xylnatmSoftPVccRetryInterval = _XylnatmSoftPVccRetryInterval_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 2, 1, 5, 1, 14),
    _XylnatmSoftPVccRetryInterval_Type()
)
xylnatmSoftPVccRetryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylnatmSoftPVccRetryInterval.setStatus("mandatory")
_XylnatmSoftPVccRetryTimer_Type = Integer32
_XylnatmSoftPVccRetryTimer_Object = MibTableColumn
xylnatmSoftPVccRetryTimer = _XylnatmSoftPVccRetryTimer_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 2, 1, 5, 1, 15),
    _XylnatmSoftPVccRetryTimer_Type()
)
xylnatmSoftPVccRetryTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmSoftPVccRetryTimer.setStatus("mandatory")


class _XylnatmSoftPVccRetryThreshold_Type(Integer32):
    """Custom type xylnatmSoftPVccRetryThreshold based on Integer32"""
    defaultValue = 1


_XylnatmSoftPVccRetryThreshold_Object = MibTableColumn
xylnatmSoftPVccRetryThreshold = _XylnatmSoftPVccRetryThreshold_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 2, 1, 5, 1, 16),
    _XylnatmSoftPVccRetryThreshold_Type()
)
xylnatmSoftPVccRetryThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylnatmSoftPVccRetryThreshold.setStatus("mandatory")
_XylnatmSoftPVccRetryFailures_Type = Gauge32
_XylnatmSoftPVccRetryFailures_Object = MibTableColumn
xylnatmSoftPVccRetryFailures = _XylnatmSoftPVccRetryFailures_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 2, 1, 5, 1, 17),
    _XylnatmSoftPVccRetryFailures_Type()
)
xylnatmSoftPVccRetryFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmSoftPVccRetryFailures.setStatus("mandatory")


class _XylnatmSoftPVccRetryLimit_Type(Integer32):
    """Custom type xylnatmSoftPVccRetryLimit based on Integer32"""
    defaultValue = 0


_XylnatmSoftPVccRetryLimit_Object = MibTableColumn
xylnatmSoftPVccRetryLimit = _XylnatmSoftPVccRetryLimit_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 2, 1, 5, 1, 18),
    _XylnatmSoftPVccRetryLimit_Type()
)
xylnatmSoftPVccRetryLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylnatmSoftPVccRetryLimit.setStatus("mandatory")
_XylnatmSoftPVccLowTDIndex_Type = AtmxTrafficDescrParamIndex
_XylnatmSoftPVccLowTDIndex_Object = MibTableColumn
xylnatmSoftPVccLowTDIndex = _XylnatmSoftPVccLowTDIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 2, 1, 5, 1, 19),
    _XylnatmSoftPVccLowTDIndex_Type()
)
xylnatmSoftPVccLowTDIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylnatmSoftPVccLowTDIndex.setStatus("mandatory")
_XylnatmSoftPVccHighTDIndex_Type = AtmxTrafficDescrParamIndex
_XylnatmSoftPVccHighTDIndex_Object = MibTableColumn
xylnatmSoftPVccHighTDIndex = _XylnatmSoftPVccHighTDIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 2, 1, 5, 1, 20),
    _XylnatmSoftPVccHighTDIndex_Type()
)
xylnatmSoftPVccHighTDIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylnatmSoftPVccHighTDIndex.setStatus("mandatory")
_XylnatmSoftPVccLastChange_Type = DisplayString
_XylnatmSoftPVccLastChange_Object = MibTableColumn
xylnatmSoftPVccLastChange = _XylnatmSoftPVccLastChange_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 2, 1, 5, 1, 21),
    _XylnatmSoftPVccLastChange_Type()
)
xylnatmSoftPVccLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmSoftPVccLastChange.setStatus("mandatory")
_XylnatmSoftPVccOutSlot_Type = Integer32
_XylnatmSoftPVccOutSlot_Object = MibTableColumn
xylnatmSoftPVccOutSlot = _XylnatmSoftPVccOutSlot_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 2, 1, 5, 1, 22),
    _XylnatmSoftPVccOutSlot_Type()
)
xylnatmSoftPVccOutSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmSoftPVccOutSlot.setStatus("mandatory")
_XylnatmSoftPVccOutPort_Type = Integer32
_XylnatmSoftPVccOutPort_Object = MibTableColumn
xylnatmSoftPVccOutPort = _XylnatmSoftPVccOutPort_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 2, 1, 5, 1, 23),
    _XylnatmSoftPVccOutPort_Type()
)
xylnatmSoftPVccOutPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmSoftPVccOutPort.setStatus("mandatory")
_XylnatmSoftPVccOutVpi_Type = Integer32
_XylnatmSoftPVccOutVpi_Object = MibTableColumn
xylnatmSoftPVccOutVpi = _XylnatmSoftPVccOutVpi_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 2, 1, 5, 1, 24),
    _XylnatmSoftPVccOutVpi_Type()
)
xylnatmSoftPVccOutVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmSoftPVccOutVpi.setStatus("mandatory")
_XylnatmSoftPVccOutVci_Type = Integer32
_XylnatmSoftPVccOutVci_Object = MibTableColumn
xylnatmSoftPVccOutVci = _XylnatmSoftPVccOutVci_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 2, 1, 5, 1, 25),
    _XylnatmSoftPVccOutVci_Type()
)
xylnatmSoftPVccOutVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmSoftPVccOutVci.setStatus("mandatory")
_XylnatmSoftPVccAdminStatus_Type = Integer32
_XylnatmSoftPVccAdminStatus_Object = MibTableColumn
xylnatmSoftPVccAdminStatus = _XylnatmSoftPVccAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 2, 1, 5, 1, 26),
    _XylnatmSoftPVccAdminStatus_Type()
)
xylnatmSoftPVccAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylnatmSoftPVccAdminStatus.setStatus("mandatory")
_XylnatmSoftPVccCrossConnectIdentifier_Type = Integer32
_XylnatmSoftPVccCrossConnectIdentifier_Object = MibTableColumn
xylnatmSoftPVccCrossConnectIdentifier = _XylnatmSoftPVccCrossConnectIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 2, 1, 5, 1, 27),
    _XylnatmSoftPVccCrossConnectIdentifier_Type()
)
xylnatmSoftPVccCrossConnectIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmSoftPVccCrossConnectIdentifier.setStatus("mandatory")
_XylnatmSoftPVccBbcIndex_Type = Integer32
_XylnatmSoftPVccBbcIndex_Object = MibTableColumn
xylnatmSoftPVccBbcIndex = _XylnatmSoftPVccBbcIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 2, 1, 5, 1, 28),
    _XylnatmSoftPVccBbcIndex_Type()
)
xylnatmSoftPVccBbcIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylnatmSoftPVccBbcIndex.setStatus("mandatory")


class _XylnatmSoftPVccRowStatus_Type(Integer32):
    """Custom type xylnatmSoftPVccRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("active", 4),
          ("create", 1),
          ("delete", 3),
          ("modify", 2),
          ("unknown", 5))
    )


_XylnatmSoftPVccRowStatus_Type.__name__ = "Integer32"
_XylnatmSoftPVccRowStatus_Object = MibTableColumn
xylnatmSoftPVccRowStatus = _XylnatmSoftPVccRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 2, 1, 5, 1, 29),
    _XylnatmSoftPVccRowStatus_Type()
)
xylnatmSoftPVccRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylnatmSoftPVccRowStatus.setStatus("mandatory")
_AtmxSoftPvcBbcTable_Object = MibTable
atmxSoftPvcBbcTable = _AtmxSoftPvcBbcTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 2, 1, 6)
)
if mibBuilder.loadTexts:
    atmxSoftPvcBbcTable.setStatus("mandatory")
_AtmxSoftPvcBbcEntry_Object = MibTableRow
atmxSoftPvcBbcEntry = _AtmxSoftPvcBbcEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 2, 1, 6, 1)
)
atmxSoftPvcBbcEntry.setIndexNames(
    (0, "XYLAN-SOFT-PVC-MIB", "atmxSoftPvcBbcIndex"),
)
if mibBuilder.loadTexts:
    atmxSoftPvcBbcEntry.setStatus("mandatory")


class _AtmxSoftPvcBbcIndex_Type(AtmxSoftPvcBbcIndex):
    """Custom type atmxSoftPvcBbcIndex based on AtmxSoftPvcBbcIndex"""
    defaultValue = 0


_AtmxSoftPvcBbcIndex_Object = MibTableColumn
atmxSoftPvcBbcIndex = _AtmxSoftPvcBbcIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 2, 1, 6, 1, 1),
    _AtmxSoftPvcBbcIndex_Type()
)
atmxSoftPvcBbcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmxSoftPvcBbcIndex.setStatus("mandatory")


class _AtmxSoftPvcBbcClass_Type(Integer32):
    """Custom type atmxSoftPvcBbcClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bcobA", 1),
          ("bcobC", 2),
          ("bcobX", 3))
    )


_AtmxSoftPvcBbcClass_Type.__name__ = "Integer32"
_AtmxSoftPvcBbcClass_Object = MibTableColumn
atmxSoftPvcBbcClass = _AtmxSoftPvcBbcClass_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 2, 1, 6, 1, 2),
    _AtmxSoftPvcBbcClass_Type()
)
atmxSoftPvcBbcClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxSoftPvcBbcClass.setStatus("mandatory")


class _AtmxSoftPvcBbcTrafficType_Type(Integer32):
    """Custom type atmxSoftPvcBbcTrafficType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("constantBitRate", 2),
          ("noIndication", 1),
          ("variableBitRate", 3))
    )


_AtmxSoftPvcBbcTrafficType_Type.__name__ = "Integer32"
_AtmxSoftPvcBbcTrafficType_Object = MibTableColumn
atmxSoftPvcBbcTrafficType = _AtmxSoftPvcBbcTrafficType_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 2, 1, 6, 1, 3),
    _AtmxSoftPvcBbcTrafficType_Type()
)
atmxSoftPvcBbcTrafficType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxSoftPvcBbcTrafficType.setStatus("mandatory")


class _AtmxSoftPvcBbcTimingRequirements_Type(Integer32):
    """Custom type atmxSoftPvcBbcTimingRequirements based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("endToEndTimingNotRequired", 3),
          ("endToEndTimingRequired", 2),
          ("noIndication", 1))
    )


_AtmxSoftPvcBbcTimingRequirements_Type.__name__ = "Integer32"
_AtmxSoftPvcBbcTimingRequirements_Object = MibTableColumn
atmxSoftPvcBbcTimingRequirements = _AtmxSoftPvcBbcTimingRequirements_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 2, 1, 6, 1, 4),
    _AtmxSoftPvcBbcTimingRequirements_Type()
)
atmxSoftPvcBbcTimingRequirements.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxSoftPvcBbcTimingRequirements.setStatus("mandatory")


class _AtmxSoftPvcBbcSusceptibilityToClipping_Type(Integer32):
    """Custom type atmxSoftPvcBbcSusceptibilityToClipping based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notSusceptibleToClipping", 2),
          ("susceptibleToClipping", 1))
    )


_AtmxSoftPvcBbcSusceptibilityToClipping_Type.__name__ = "Integer32"
_AtmxSoftPvcBbcSusceptibilityToClipping_Object = MibTableColumn
atmxSoftPvcBbcSusceptibilityToClipping = _AtmxSoftPvcBbcSusceptibilityToClipping_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 2, 1, 6, 1, 5),
    _AtmxSoftPvcBbcSusceptibilityToClipping_Type()
)
atmxSoftPvcBbcSusceptibilityToClipping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxSoftPvcBbcSusceptibilityToClipping.setStatus("mandatory")


class _AtmxSoftPvcBbcUserPlaneConnectionConfig_Type(Integer32):
    """Custom type atmxSoftPvcBbcUserPlaneConnectionConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("point-to-multipoint", 2),
          ("point-to-point", 1))
    )


_AtmxSoftPvcBbcUserPlaneConnectionConfig_Type.__name__ = "Integer32"
_AtmxSoftPvcBbcUserPlaneConnectionConfig_Object = MibTableColumn
atmxSoftPvcBbcUserPlaneConnectionConfig = _AtmxSoftPvcBbcUserPlaneConnectionConfig_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 2, 1, 6, 1, 6),
    _AtmxSoftPvcBbcUserPlaneConnectionConfig_Type()
)
atmxSoftPvcBbcUserPlaneConnectionConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxSoftPvcBbcUserPlaneConnectionConfig.setStatus("mandatory")


class _AtmxSoftPvcBbcRowStatus_Type(Integer32):
    """Custom type atmxSoftPvcBbcRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("active", 4),
          ("create", 1),
          ("delete", 3),
          ("modify", 2),
          ("unknown", 5))
    )


_AtmxSoftPvcBbcRowStatus_Type.__name__ = "Integer32"
_AtmxSoftPvcBbcRowStatus_Object = MibTableColumn
atmxSoftPvcBbcRowStatus = _AtmxSoftPvcBbcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 2, 1, 6, 1, 7),
    _AtmxSoftPvcBbcRowStatus_Type()
)
atmxSoftPvcBbcRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxSoftPvcBbcRowStatus.setStatus("mandatory")
_AtmxSoftPvcMIBTraps_ObjectIdentity = ObjectIdentity
atmxSoftPvcMIBTraps = _AtmxSoftPvcMIBTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 2, 2)
)
_AtmxSoftPvcTraps_ObjectIdentity = ObjectIdentity
atmxSoftPvcTraps = _AtmxSoftPvcTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 2, 2, 1)
)
_AtmxSoftPvcTrapsPrefix_ObjectIdentity = ObjectIdentity
atmxSoftPvcTrapsPrefix = _AtmxSoftPvcTrapsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 2, 2, 1, 1)
)
_AtmxSoftPvcMIBConformance_ObjectIdentity = ObjectIdentity
atmxSoftPvcMIBConformance = _AtmxSoftPvcMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 2, 3)
)
_AtmxSoftPvcMIBCompliances_ObjectIdentity = ObjectIdentity
atmxSoftPvcMIBCompliances = _AtmxSoftPvcMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 2, 3, 1)
)
_AtmxSoftPvcMIBCompliance_ObjectIdentity = ObjectIdentity
atmxSoftPvcMIBCompliance = _AtmxSoftPvcMIBCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 2, 3, 1, 1)
)
_AtmxSoftPvcMIBGroups_ObjectIdentity = ObjectIdentity
atmxSoftPvcMIBGroups = _AtmxSoftPvcMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 2, 3, 2)
)
_AtmxSoftPvcBaseMIBGroup_ObjectIdentity = ObjectIdentity
atmxSoftPvcBaseMIBGroup = _AtmxSoftPvcBaseMIBGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 2, 3, 2, 1)
)
_AtmxSoftPvcVccMIBGroup_ObjectIdentity = ObjectIdentity
atmxSoftPvcVccMIBGroup = _AtmxSoftPvcVccMIBGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 2, 3, 2, 2)
)
_AtmxSoftPvcVpcMIBGroup_ObjectIdentity = ObjectIdentity
atmxSoftPvcVpcMIBGroup = _AtmxSoftPvcVpcMIBGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 2, 3, 2, 3)
)
_AtmxSoftPvcAddressMIBGroup_ObjectIdentity = ObjectIdentity
atmxSoftPvcAddressMIBGroup = _AtmxSoftPvcAddressMIBGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 2, 3, 2, 4)
)
_AtmxCurrentlyFailingSoftPVccMIBGroup_ObjectIdentity = ObjectIdentity
atmxCurrentlyFailingSoftPVccMIBGroup = _AtmxCurrentlyFailingSoftPVccMIBGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 2, 3, 2, 5)
)
_AtmxCurrentlyFailingSoftPVpcMIBGroup_ObjectIdentity = ObjectIdentity
atmxCurrentlyFailingSoftPVpcMIBGroup = _AtmxCurrentlyFailingSoftPVpcMIBGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 2, 3, 2, 6)
)

# Managed Objects groups


# Notification objects

atmxSoftPvcCallFailuresTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 2, 2, 1, 1, 0, 1)
)
atmxSoftPvcCallFailuresTrap.setObjects(
      *(("XYLAN-SOFT-PVC-MIB", "atmxSoftPvcCallFailures"),
        ("XYLAN-SOFT-PVC-MIB", "atmxSoftPvcCurrentlyFailingSoftPVccs"),
        ("XYLAN-SOFT-PVC-MIB", "atmxSoftPvcCurrentlyFailingSoftPVpcs"))
)
if mibBuilder.loadTexts:
    atmxSoftPvcCallFailuresTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "XYLAN-SOFT-PVC-MIB",
    **{"TruthValue": TruthValue,
       "AtmxSoftPvcBbcIndex": AtmxSoftPvcBbcIndex,
       "atmxSoftPvcMIB": atmxSoftPvcMIB,
       "atmxSoftPvcMIBObjects": atmxSoftPvcMIBObjects,
       "atmxSoftPvcBaseGroup": atmxSoftPvcBaseGroup,
       "atmxSoftPvcCallFailuresTrapEnable": atmxSoftPvcCallFailuresTrapEnable,
       "atmxSoftPvcCallFailures": atmxSoftPvcCallFailures,
       "atmxSoftPvcCurrentlyFailingSoftPVccs": atmxSoftPvcCurrentlyFailingSoftPVccs,
       "atmxSoftPvcCurrentlyFailingSoftPVpcs": atmxSoftPvcCurrentlyFailingSoftPVpcs,
       "atmxSoftPvcNotificationInterval": atmxSoftPvcNotificationInterval,
       "atmxCurrentlyFailingSoftPVccTable": atmxCurrentlyFailingSoftPVccTable,
       "atmxCurrentlyFailingSoftPVccEntry": atmxCurrentlyFailingSoftPVccEntry,
       "atmxCurrentlyFailingSoftPVccSlotIndex": atmxCurrentlyFailingSoftPVccSlotIndex,
       "atmxCurrentlyFailingSoftPVccPortIndex": atmxCurrentlyFailingSoftPVccPortIndex,
       "atmxCurrentlyFailingSoftPVccVpi": atmxCurrentlyFailingSoftPVccVpi,
       "atmxCurrentlyFailingSoftPVccVci": atmxCurrentlyFailingSoftPVccVci,
       "atmxCurrentlyFailingSoftPVccLeafReference": atmxCurrentlyFailingSoftPVccLeafReference,
       "atmxCurrentlyFailingSoftPVccTimeStamp": atmxCurrentlyFailingSoftPVccTimeStamp,
       "atmxCurrentlyFailingSoftPVpcTable": atmxCurrentlyFailingSoftPVpcTable,
       "atmxCurrentlyFailingSoftPVpcEntry": atmxCurrentlyFailingSoftPVpcEntry,
       "atmxCurrentlyFailingSoftPVpcSlotIndex": atmxCurrentlyFailingSoftPVpcSlotIndex,
       "atmxCurrentlyFailingSoftPVpcPortIndex": atmxCurrentlyFailingSoftPVpcPortIndex,
       "atmxCurrentlyFailingSoftPVpcVpi": atmxCurrentlyFailingSoftPVpcVpi,
       "atmxCurrentlyFailingSoftPVpcLeafReference": atmxCurrentlyFailingSoftPVpcLeafReference,
       "atmxCurrentlyFailingSoftPVpcTimeStamp": atmxCurrentlyFailingSoftPVpcTimeStamp,
       "xylnatmSoftPVpcTable": xylnatmSoftPVpcTable,
       "xylnatmSoftPVpcEntry": xylnatmSoftPVpcEntry,
       "xylnatmSoftPVpcSlotIndex": xylnatmSoftPVpcSlotIndex,
       "xylnatmSoftPVpcPortIndex": xylnatmSoftPVpcPortIndex,
       "xylnatmSoftPVpcVpi": xylnatmSoftPVpcVpi,
       "xylnatmSoftPVpcLeafReference": xylnatmSoftPVpcLeafReference,
       "xylnatmSoftPVpcTargetAddress": xylnatmSoftPVpcTargetAddress,
       "xylnatmSoftPVpcTargetSelectType": xylnatmSoftPVpcTargetSelectType,
       "xylnatmSoftPVpcTargetVpi": xylnatmSoftPVpcTargetVpi,
       "xylnatmSoftPVpcLastReleaseCause": xylnatmSoftPVpcLastReleaseCause,
       "xylnatmSoftPVpcLastReleaseDiagnostic": xylnatmSoftPVpcLastReleaseDiagnostic,
       "xylnatmSoftPVpcOperStatus": xylnatmSoftPVpcOperStatus,
       "xylnatmSoftPVpcRestart": xylnatmSoftPVpcRestart,
       "xylnatmSoftPVpcRetryInterval": xylnatmSoftPVpcRetryInterval,
       "xylnatmSoftPVpcRetryTimer": xylnatmSoftPVpcRetryTimer,
       "xylnatmSoftPVpcRetryThreshold": xylnatmSoftPVpcRetryThreshold,
       "xylnatmSoftPVpcRetryFailures": xylnatmSoftPVpcRetryFailures,
       "xylnatmSoftPVpcRetryLimit": xylnatmSoftPVpcRetryLimit,
       "xylnatmSoftPVpcLowTDIndex": xylnatmSoftPVpcLowTDIndex,
       "xylnatmSoftPVpcHighTDIndex": xylnatmSoftPVpcHighTDIndex,
       "xylnatmSoftPVpcLastChange": xylnatmSoftPVpcLastChange,
       "xylnatmSoftPVpcOutSlot": xylnatmSoftPVpcOutSlot,
       "xylnatmSoftPVpcOutPort": xylnatmSoftPVpcOutPort,
       "xylnatmSoftPVpcOutVpi": xylnatmSoftPVpcOutVpi,
       "xylnatmSoftPVpcAdminStatus": xylnatmSoftPVpcAdminStatus,
       "xylnatmSoftPVpcCrossConnectIdentifier": xylnatmSoftPVpcCrossConnectIdentifier,
       "xylnatmSoftPVpcBbcIndex": xylnatmSoftPVpcBbcIndex,
       "xylnatmSoftPVpcRowStatus": xylnatmSoftPVpcRowStatus,
       "xylnatmSoftPVccTable": xylnatmSoftPVccTable,
       "xylnatmSoftPVccEntry": xylnatmSoftPVccEntry,
       "xylnatmSoftPVccSlotIndex": xylnatmSoftPVccSlotIndex,
       "xylnatmSoftPVccPortIndex": xylnatmSoftPVccPortIndex,
       "xylnatmSoftPVccVpi": xylnatmSoftPVccVpi,
       "xylnatmSoftPVccVci": xylnatmSoftPVccVci,
       "xylnatmSoftPVccLeafReference": xylnatmSoftPVccLeafReference,
       "xylnatmSoftPVccTargetAddress": xylnatmSoftPVccTargetAddress,
       "xylnatmSoftPVccTargetSelectType": xylnatmSoftPVccTargetSelectType,
       "xylnatmSoftPVccTargetVpi": xylnatmSoftPVccTargetVpi,
       "xylnatmSoftPVccTargetVci": xylnatmSoftPVccTargetVci,
       "xylnatmSoftPVccLastReleaseCause": xylnatmSoftPVccLastReleaseCause,
       "xylnatmSoftPVccLastReleaseDiagnostic": xylnatmSoftPVccLastReleaseDiagnostic,
       "xylnatmSoftPVccOperStatus": xylnatmSoftPVccOperStatus,
       "xylnatmSoftPVccRestart": xylnatmSoftPVccRestart,
       "xylnatmSoftPVccRetryInterval": xylnatmSoftPVccRetryInterval,
       "xylnatmSoftPVccRetryTimer": xylnatmSoftPVccRetryTimer,
       "xylnatmSoftPVccRetryThreshold": xylnatmSoftPVccRetryThreshold,
       "xylnatmSoftPVccRetryFailures": xylnatmSoftPVccRetryFailures,
       "xylnatmSoftPVccRetryLimit": xylnatmSoftPVccRetryLimit,
       "xylnatmSoftPVccLowTDIndex": xylnatmSoftPVccLowTDIndex,
       "xylnatmSoftPVccHighTDIndex": xylnatmSoftPVccHighTDIndex,
       "xylnatmSoftPVccLastChange": xylnatmSoftPVccLastChange,
       "xylnatmSoftPVccOutSlot": xylnatmSoftPVccOutSlot,
       "xylnatmSoftPVccOutPort": xylnatmSoftPVccOutPort,
       "xylnatmSoftPVccOutVpi": xylnatmSoftPVccOutVpi,
       "xylnatmSoftPVccOutVci": xylnatmSoftPVccOutVci,
       "xylnatmSoftPVccAdminStatus": xylnatmSoftPVccAdminStatus,
       "xylnatmSoftPVccCrossConnectIdentifier": xylnatmSoftPVccCrossConnectIdentifier,
       "xylnatmSoftPVccBbcIndex": xylnatmSoftPVccBbcIndex,
       "xylnatmSoftPVccRowStatus": xylnatmSoftPVccRowStatus,
       "atmxSoftPvcBbcTable": atmxSoftPvcBbcTable,
       "atmxSoftPvcBbcEntry": atmxSoftPvcBbcEntry,
       "atmxSoftPvcBbcIndex": atmxSoftPvcBbcIndex,
       "atmxSoftPvcBbcClass": atmxSoftPvcBbcClass,
       "atmxSoftPvcBbcTrafficType": atmxSoftPvcBbcTrafficType,
       "atmxSoftPvcBbcTimingRequirements": atmxSoftPvcBbcTimingRequirements,
       "atmxSoftPvcBbcSusceptibilityToClipping": atmxSoftPvcBbcSusceptibilityToClipping,
       "atmxSoftPvcBbcUserPlaneConnectionConfig": atmxSoftPvcBbcUserPlaneConnectionConfig,
       "atmxSoftPvcBbcRowStatus": atmxSoftPvcBbcRowStatus,
       "atmxSoftPvcMIBTraps": atmxSoftPvcMIBTraps,
       "atmxSoftPvcTraps": atmxSoftPvcTraps,
       "atmxSoftPvcTrapsPrefix": atmxSoftPvcTrapsPrefix,
       "atmxSoftPvcCallFailuresTrap": atmxSoftPvcCallFailuresTrap,
       "atmxSoftPvcMIBConformance": atmxSoftPvcMIBConformance,
       "atmxSoftPvcMIBCompliances": atmxSoftPvcMIBCompliances,
       "atmxSoftPvcMIBCompliance": atmxSoftPvcMIBCompliance,
       "atmxSoftPvcMIBGroups": atmxSoftPvcMIBGroups,
       "atmxSoftPvcBaseMIBGroup": atmxSoftPvcBaseMIBGroup,
       "atmxSoftPvcVccMIBGroup": atmxSoftPvcVccMIBGroup,
       "atmxSoftPvcVpcMIBGroup": atmxSoftPvcVpcMIBGroup,
       "atmxSoftPvcAddressMIBGroup": atmxSoftPvcAddressMIBGroup,
       "atmxCurrentlyFailingSoftPVccMIBGroup": atmxCurrentlyFailingSoftPVccMIBGroup,
       "atmxCurrentlyFailingSoftPVpcMIBGroup": atmxCurrentlyFailingSoftPVpcMIBGroup}
)
