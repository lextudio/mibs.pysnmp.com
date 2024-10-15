# SNMP MIB module (ATM-SOFT-PVC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ATM-SOFT-PVC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:44:01 2024
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

(atmVclVci,
 atmVclVpi,
 atmVplVpi) = mibBuilder.importSymbols(
    "ATM-MIB",
    "atmVclVci",
    "atmVclVpi",
    "atmVplVpi")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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

(RowStatus,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC-v1",
    "RowStatus",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY


# Types definitions



class AtmAddr(OctetString):
    """Custom type AtmAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(20, 20),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AtmForum_ObjectIdentity = ObjectIdentity
atmForum = _AtmForum_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353)
)
_AtmForumNetworkManagement_ObjectIdentity = ObjectIdentity
atmForumNetworkManagement = _AtmForumNetworkManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5)
)
_AtmfSoftPvc_ObjectIdentity = ObjectIdentity
atmfSoftPvc = _AtmfSoftPvc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 5)
)
_AtmSoftPvcMIB_ObjectIdentity = ObjectIdentity
atmSoftPvcMIB = _AtmSoftPvcMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 5, 1)
)
_AtmSoftPvcMIBObjects_ObjectIdentity = ObjectIdentity
atmSoftPvcMIBObjects = _AtmSoftPvcMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1)
)
_AtmSoftPvcBaseGroup_ObjectIdentity = ObjectIdentity
atmSoftPvcBaseGroup = _AtmSoftPvcBaseGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 1)
)
_AtmSoftPvcCallFailuresTrapEnable_Type = TruthValue
_AtmSoftPvcCallFailuresTrapEnable_Object = MibScalar
atmSoftPvcCallFailuresTrapEnable = _AtmSoftPvcCallFailuresTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 1, 1),
    _AtmSoftPvcCallFailuresTrapEnable_Type()
)
atmSoftPvcCallFailuresTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmSoftPvcCallFailuresTrapEnable.setStatus("mandatory")
_AtmSoftPvcCallFailures_Type = Counter32
_AtmSoftPvcCallFailures_Object = MibScalar
atmSoftPvcCallFailures = _AtmSoftPvcCallFailures_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 1, 2),
    _AtmSoftPvcCallFailures_Type()
)
atmSoftPvcCallFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSoftPvcCallFailures.setStatus("mandatory")
_AtmSoftPvcCurrentlyFailingSoftPVccs_Type = Gauge32
_AtmSoftPvcCurrentlyFailingSoftPVccs_Object = MibScalar
atmSoftPvcCurrentlyFailingSoftPVccs = _AtmSoftPvcCurrentlyFailingSoftPVccs_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 1, 3),
    _AtmSoftPvcCurrentlyFailingSoftPVccs_Type()
)
atmSoftPvcCurrentlyFailingSoftPVccs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSoftPvcCurrentlyFailingSoftPVccs.setStatus("mandatory")
_AtmSoftPvcCurrentlyFailingSoftPVpcs_Type = Gauge32
_AtmSoftPvcCurrentlyFailingSoftPVpcs_Object = MibScalar
atmSoftPvcCurrentlyFailingSoftPVpcs = _AtmSoftPvcCurrentlyFailingSoftPVpcs_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 1, 4),
    _AtmSoftPvcCurrentlyFailingSoftPVpcs_Type()
)
atmSoftPvcCurrentlyFailingSoftPVpcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSoftPvcCurrentlyFailingSoftPVpcs.setStatus("mandatory")


class _AtmSoftPvcNotificationInterval_Type(Integer32):
    """Custom type atmSoftPvcNotificationInterval based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_AtmSoftPvcNotificationInterval_Type.__name__ = "Integer32"
_AtmSoftPvcNotificationInterval_Object = MibScalar
atmSoftPvcNotificationInterval = _AtmSoftPvcNotificationInterval_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 1, 5),
    _AtmSoftPvcNotificationInterval_Type()
)
atmSoftPvcNotificationInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmSoftPvcNotificationInterval.setStatus("mandatory")
_AtmSoftPVccTable_Object = MibTable
atmSoftPVccTable = _AtmSoftPVccTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 2)
)
if mibBuilder.loadTexts:
    atmSoftPVccTable.setStatus("mandatory")
_AtmSoftPVccEntry_Object = MibTableRow
atmSoftPVccEntry = _AtmSoftPVccEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 2, 1)
)
atmSoftPVccEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ATM-MIB", "atmVclVpi"),
    (0, "ATM-MIB", "atmVclVci"),
    (0, "ATM-SOFT-PVC-MIB", "atmSoftPVccLeafReference"),
)
if mibBuilder.loadTexts:
    atmSoftPVccEntry.setStatus("mandatory")


class _AtmSoftPVccLeafReference_Type(Integer32):
    """Custom type atmSoftPVccLeafReference based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AtmSoftPVccLeafReference_Type.__name__ = "Integer32"
_AtmSoftPVccLeafReference_Object = MibTableColumn
atmSoftPVccLeafReference = _AtmSoftPVccLeafReference_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 2, 1, 1),
    _AtmSoftPVccLeafReference_Type()
)
atmSoftPVccLeafReference.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmSoftPVccLeafReference.setStatus("mandatory")
_AtmSoftPVccTargetAddress_Type = AtmAddr
_AtmSoftPVccTargetAddress_Object = MibTableColumn
atmSoftPVccTargetAddress = _AtmSoftPVccTargetAddress_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 2, 1, 2),
    _AtmSoftPVccTargetAddress_Type()
)
atmSoftPVccTargetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmSoftPVccTargetAddress.setStatus("mandatory")


class _AtmSoftPVccTargetSelectType_Type(Integer32):
    """Custom type atmSoftPVccTargetSelectType based on Integer32"""
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


_AtmSoftPVccTargetSelectType_Type.__name__ = "Integer32"
_AtmSoftPVccTargetSelectType_Object = MibTableColumn
atmSoftPVccTargetSelectType = _AtmSoftPVccTargetSelectType_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 2, 1, 3),
    _AtmSoftPVccTargetSelectType_Type()
)
atmSoftPVccTargetSelectType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmSoftPVccTargetSelectType.setStatus("mandatory")


class _AtmSoftPVccTargetVpi_Type(Integer32):
    """Custom type atmSoftPVccTargetVpi based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_AtmSoftPVccTargetVpi_Type.__name__ = "Integer32"
_AtmSoftPVccTargetVpi_Object = MibTableColumn
atmSoftPVccTargetVpi = _AtmSoftPVccTargetVpi_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 2, 1, 4),
    _AtmSoftPVccTargetVpi_Type()
)
atmSoftPVccTargetVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmSoftPVccTargetVpi.setStatus("mandatory")


class _AtmSoftPVccTargetVci_Type(Integer32):
    """Custom type atmSoftPVccTargetVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AtmSoftPVccTargetVci_Type.__name__ = "Integer32"
_AtmSoftPVccTargetVci_Object = MibTableColumn
atmSoftPVccTargetVci = _AtmSoftPVccTargetVci_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 2, 1, 5),
    _AtmSoftPVccTargetVci_Type()
)
atmSoftPVccTargetVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmSoftPVccTargetVci.setStatus("mandatory")


class _AtmSoftPVccLastReleaseCause_Type(Integer32):
    """Custom type atmSoftPVccLastReleaseCause based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_AtmSoftPVccLastReleaseCause_Type.__name__ = "Integer32"
_AtmSoftPVccLastReleaseCause_Object = MibTableColumn
atmSoftPVccLastReleaseCause = _AtmSoftPVccLastReleaseCause_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 2, 1, 6),
    _AtmSoftPVccLastReleaseCause_Type()
)
atmSoftPVccLastReleaseCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSoftPVccLastReleaseCause.setStatus("mandatory")


class _AtmSoftPVccLastReleaseDiagnostic_Type(OctetString):
    """Custom type atmSoftPVccLastReleaseDiagnostic based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_AtmSoftPVccLastReleaseDiagnostic_Type.__name__ = "OctetString"
_AtmSoftPVccLastReleaseDiagnostic_Object = MibTableColumn
atmSoftPVccLastReleaseDiagnostic = _AtmSoftPVccLastReleaseDiagnostic_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 2, 1, 7),
    _AtmSoftPVccLastReleaseDiagnostic_Type()
)
atmSoftPVccLastReleaseDiagnostic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSoftPVccLastReleaseDiagnostic.setStatus("mandatory")


class _AtmSoftPVccOperStatus_Type(Integer32):
    """Custom type atmSoftPVccOperStatus based on Integer32"""
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
        *(("connected", 3),
          ("establishmentInProgress", 2),
          ("lowerLayerDown", 6),
          ("noAddressSupplied", 5),
          ("other", 1),
          ("retriesExhausted", 4))
    )


_AtmSoftPVccOperStatus_Type.__name__ = "Integer32"
_AtmSoftPVccOperStatus_Object = MibTableColumn
atmSoftPVccOperStatus = _AtmSoftPVccOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 2, 1, 8),
    _AtmSoftPVccOperStatus_Type()
)
atmSoftPVccOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSoftPVccOperStatus.setStatus("mandatory")


class _AtmSoftPVccRestart_Type(Integer32):
    """Custom type atmSoftPVccRestart based on Integer32"""
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


_AtmSoftPVccRestart_Type.__name__ = "Integer32"
_AtmSoftPVccRestart_Object = MibTableColumn
atmSoftPVccRestart = _AtmSoftPVccRestart_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 2, 1, 9),
    _AtmSoftPVccRestart_Type()
)
atmSoftPVccRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmSoftPVccRestart.setStatus("mandatory")


class _AtmSoftPVccRetryInterval_Type(Integer32):
    """Custom type atmSoftPVccRetryInterval based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_AtmSoftPVccRetryInterval_Type.__name__ = "Integer32"
_AtmSoftPVccRetryInterval_Object = MibTableColumn
atmSoftPVccRetryInterval = _AtmSoftPVccRetryInterval_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 2, 1, 10),
    _AtmSoftPVccRetryInterval_Type()
)
atmSoftPVccRetryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmSoftPVccRetryInterval.setStatus("mandatory")


class _AtmSoftPVccRetryTimer_Type(Integer32):
    """Custom type atmSoftPVccRetryTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_AtmSoftPVccRetryTimer_Type.__name__ = "Integer32"
_AtmSoftPVccRetryTimer_Object = MibTableColumn
atmSoftPVccRetryTimer = _AtmSoftPVccRetryTimer_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 2, 1, 11),
    _AtmSoftPVccRetryTimer_Type()
)
atmSoftPVccRetryTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSoftPVccRetryTimer.setStatus("mandatory")


class _AtmSoftPVccRetryThreshold_Type(Integer32):
    """Custom type atmSoftPVccRetryThreshold based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AtmSoftPVccRetryThreshold_Type.__name__ = "Integer32"
_AtmSoftPVccRetryThreshold_Object = MibTableColumn
atmSoftPVccRetryThreshold = _AtmSoftPVccRetryThreshold_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 2, 1, 12),
    _AtmSoftPVccRetryThreshold_Type()
)
atmSoftPVccRetryThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmSoftPVccRetryThreshold.setStatus("mandatory")
_AtmSoftPVccRetryFailures_Type = Gauge32
_AtmSoftPVccRetryFailures_Object = MibTableColumn
atmSoftPVccRetryFailures = _AtmSoftPVccRetryFailures_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 2, 1, 13),
    _AtmSoftPVccRetryFailures_Type()
)
atmSoftPVccRetryFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSoftPVccRetryFailures.setStatus("mandatory")


class _AtmSoftPVccRetryLimit_Type(Integer32):
    """Custom type atmSoftPVccRetryLimit based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AtmSoftPVccRetryLimit_Type.__name__ = "Integer32"
_AtmSoftPVccRetryLimit_Object = MibTableColumn
atmSoftPVccRetryLimit = _AtmSoftPVccRetryLimit_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 2, 1, 14),
    _AtmSoftPVccRetryLimit_Type()
)
atmSoftPVccRetryLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmSoftPVccRetryLimit.setStatus("mandatory")
_AtmSoftPVccRowStatus_Type = RowStatus
_AtmSoftPVccRowStatus_Object = MibTableColumn
atmSoftPVccRowStatus = _AtmSoftPVccRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 2, 1, 15),
    _AtmSoftPVccRowStatus_Type()
)
atmSoftPVccRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmSoftPVccRowStatus.setStatus("mandatory")
_AtmSoftPVpcTable_Object = MibTable
atmSoftPVpcTable = _AtmSoftPVpcTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 3)
)
if mibBuilder.loadTexts:
    atmSoftPVpcTable.setStatus("mandatory")
_AtmSoftPVpcEntry_Object = MibTableRow
atmSoftPVpcEntry = _AtmSoftPVpcEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 3, 1)
)
atmSoftPVpcEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ATM-MIB", "atmVplVpi"),
    (0, "ATM-SOFT-PVC-MIB", "atmSoftPVpcLeafReference"),
)
if mibBuilder.loadTexts:
    atmSoftPVpcEntry.setStatus("mandatory")


class _AtmSoftPVpcLeafReference_Type(Integer32):
    """Custom type atmSoftPVpcLeafReference based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 63535),
    )


_AtmSoftPVpcLeafReference_Type.__name__ = "Integer32"
_AtmSoftPVpcLeafReference_Object = MibTableColumn
atmSoftPVpcLeafReference = _AtmSoftPVpcLeafReference_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 3, 1, 1),
    _AtmSoftPVpcLeafReference_Type()
)
atmSoftPVpcLeafReference.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmSoftPVpcLeafReference.setStatus("mandatory")
_AtmSoftPVpcTargetAddress_Type = AtmAddr
_AtmSoftPVpcTargetAddress_Object = MibTableColumn
atmSoftPVpcTargetAddress = _AtmSoftPVpcTargetAddress_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 3, 1, 2),
    _AtmSoftPVpcTargetAddress_Type()
)
atmSoftPVpcTargetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmSoftPVpcTargetAddress.setStatus("mandatory")


class _AtmSoftPVpcTargetSelectType_Type(Integer32):
    """Custom type atmSoftPVpcTargetSelectType based on Integer32"""
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


_AtmSoftPVpcTargetSelectType_Type.__name__ = "Integer32"
_AtmSoftPVpcTargetSelectType_Object = MibTableColumn
atmSoftPVpcTargetSelectType = _AtmSoftPVpcTargetSelectType_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 3, 1, 3),
    _AtmSoftPVpcTargetSelectType_Type()
)
atmSoftPVpcTargetSelectType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmSoftPVpcTargetSelectType.setStatus("mandatory")


class _AtmSoftPVpcTargetVpi_Type(Integer32):
    """Custom type atmSoftPVpcTargetVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_AtmSoftPVpcTargetVpi_Type.__name__ = "Integer32"
_AtmSoftPVpcTargetVpi_Object = MibTableColumn
atmSoftPVpcTargetVpi = _AtmSoftPVpcTargetVpi_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 3, 1, 4),
    _AtmSoftPVpcTargetVpi_Type()
)
atmSoftPVpcTargetVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmSoftPVpcTargetVpi.setStatus("mandatory")


class _AtmSoftPVpcLastReleaseCause_Type(Integer32):
    """Custom type atmSoftPVpcLastReleaseCause based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_AtmSoftPVpcLastReleaseCause_Type.__name__ = "Integer32"
_AtmSoftPVpcLastReleaseCause_Object = MibTableColumn
atmSoftPVpcLastReleaseCause = _AtmSoftPVpcLastReleaseCause_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 3, 1, 5),
    _AtmSoftPVpcLastReleaseCause_Type()
)
atmSoftPVpcLastReleaseCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSoftPVpcLastReleaseCause.setStatus("mandatory")


class _AtmSoftPVpcLastReleaseDiagnostic_Type(OctetString):
    """Custom type atmSoftPVpcLastReleaseDiagnostic based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_AtmSoftPVpcLastReleaseDiagnostic_Type.__name__ = "OctetString"
_AtmSoftPVpcLastReleaseDiagnostic_Object = MibTableColumn
atmSoftPVpcLastReleaseDiagnostic = _AtmSoftPVpcLastReleaseDiagnostic_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 3, 1, 6),
    _AtmSoftPVpcLastReleaseDiagnostic_Type()
)
atmSoftPVpcLastReleaseDiagnostic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSoftPVpcLastReleaseDiagnostic.setStatus("mandatory")


class _AtmSoftPVpcOperStatus_Type(Integer32):
    """Custom type atmSoftPVpcOperStatus based on Integer32"""
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
        *(("connected", 3),
          ("establishmentInProgress", 2),
          ("lowerLayerDown", 6),
          ("noAddressSupplied", 5),
          ("other", 1),
          ("retriesExhausted", 4))
    )


_AtmSoftPVpcOperStatus_Type.__name__ = "Integer32"
_AtmSoftPVpcOperStatus_Object = MibTableColumn
atmSoftPVpcOperStatus = _AtmSoftPVpcOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 3, 1, 7),
    _AtmSoftPVpcOperStatus_Type()
)
atmSoftPVpcOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSoftPVpcOperStatus.setStatus("mandatory")


class _AtmSoftPVpcRestart_Type(Integer32):
    """Custom type atmSoftPVpcRestart based on Integer32"""
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


_AtmSoftPVpcRestart_Type.__name__ = "Integer32"
_AtmSoftPVpcRestart_Object = MibTableColumn
atmSoftPVpcRestart = _AtmSoftPVpcRestart_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 3, 1, 8),
    _AtmSoftPVpcRestart_Type()
)
atmSoftPVpcRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmSoftPVpcRestart.setStatus("mandatory")


class _AtmSoftPVpcRetryInterval_Type(Integer32):
    """Custom type atmSoftPVpcRetryInterval based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_AtmSoftPVpcRetryInterval_Type.__name__ = "Integer32"
_AtmSoftPVpcRetryInterval_Object = MibTableColumn
atmSoftPVpcRetryInterval = _AtmSoftPVpcRetryInterval_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 3, 1, 9),
    _AtmSoftPVpcRetryInterval_Type()
)
atmSoftPVpcRetryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmSoftPVpcRetryInterval.setStatus("mandatory")


class _AtmSoftPVpcRetryTimer_Type(Integer32):
    """Custom type atmSoftPVpcRetryTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_AtmSoftPVpcRetryTimer_Type.__name__ = "Integer32"
_AtmSoftPVpcRetryTimer_Object = MibTableColumn
atmSoftPVpcRetryTimer = _AtmSoftPVpcRetryTimer_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 3, 1, 10),
    _AtmSoftPVpcRetryTimer_Type()
)
atmSoftPVpcRetryTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSoftPVpcRetryTimer.setStatus("mandatory")


class _AtmSoftPVpcRetryThreshold_Type(Integer32):
    """Custom type atmSoftPVpcRetryThreshold based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AtmSoftPVpcRetryThreshold_Type.__name__ = "Integer32"
_AtmSoftPVpcRetryThreshold_Object = MibTableColumn
atmSoftPVpcRetryThreshold = _AtmSoftPVpcRetryThreshold_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 3, 1, 11),
    _AtmSoftPVpcRetryThreshold_Type()
)
atmSoftPVpcRetryThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmSoftPVpcRetryThreshold.setStatus("mandatory")
_AtmSoftPVpcRetryFailures_Type = Gauge32
_AtmSoftPVpcRetryFailures_Object = MibTableColumn
atmSoftPVpcRetryFailures = _AtmSoftPVpcRetryFailures_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 3, 1, 12),
    _AtmSoftPVpcRetryFailures_Type()
)
atmSoftPVpcRetryFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSoftPVpcRetryFailures.setStatus("mandatory")


class _AtmSoftPVpcRetryLimit_Type(Integer32):
    """Custom type atmSoftPVpcRetryLimit based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AtmSoftPVpcRetryLimit_Type.__name__ = "Integer32"
_AtmSoftPVpcRetryLimit_Object = MibTableColumn
atmSoftPVpcRetryLimit = _AtmSoftPVpcRetryLimit_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 3, 1, 13),
    _AtmSoftPVpcRetryLimit_Type()
)
atmSoftPVpcRetryLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmSoftPVpcRetryLimit.setStatus("mandatory")
_AtmSoftPVpcRowStatus_Type = RowStatus
_AtmSoftPVpcRowStatus_Object = MibTableColumn
atmSoftPVpcRowStatus = _AtmSoftPVpcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 3, 1, 14),
    _AtmSoftPVpcRowStatus_Type()
)
atmSoftPVpcRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmSoftPVpcRowStatus.setStatus("mandatory")
_AtmInterfaceSoftPvcAddressTable_Object = MibTable
atmInterfaceSoftPvcAddressTable = _AtmInterfaceSoftPvcAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 4)
)
if mibBuilder.loadTexts:
    atmInterfaceSoftPvcAddressTable.setStatus("mandatory")
_AtmInterfaceSoftPvcAddressEntry_Object = MibTableRow
atmInterfaceSoftPvcAddressEntry = _AtmInterfaceSoftPvcAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 4, 1)
)
atmInterfaceSoftPvcAddressEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ATM-SOFT-PVC-MIB", "atmInterfaceSoftPvcAddress"),
)
if mibBuilder.loadTexts:
    atmInterfaceSoftPvcAddressEntry.setStatus("mandatory")
_AtmInterfaceSoftPvcAddress_Type = AtmAddr
_AtmInterfaceSoftPvcAddress_Object = MibTableColumn
atmInterfaceSoftPvcAddress = _AtmInterfaceSoftPvcAddress_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 4, 1, 1),
    _AtmInterfaceSoftPvcAddress_Type()
)
atmInterfaceSoftPvcAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmInterfaceSoftPvcAddress.setStatus("mandatory")
_AtmInterfaceSoftPvcAddressRowStatus_Type = RowStatus
_AtmInterfaceSoftPvcAddressRowStatus_Object = MibTableColumn
atmInterfaceSoftPvcAddressRowStatus = _AtmInterfaceSoftPvcAddressRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 4, 1, 2),
    _AtmInterfaceSoftPvcAddressRowStatus_Type()
)
atmInterfaceSoftPvcAddressRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmInterfaceSoftPvcAddressRowStatus.setStatus("mandatory")
_AtmCurrentlyFailingSoftPVccTable_Object = MibTable
atmCurrentlyFailingSoftPVccTable = _AtmCurrentlyFailingSoftPVccTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 5)
)
if mibBuilder.loadTexts:
    atmCurrentlyFailingSoftPVccTable.setStatus("mandatory")
_AtmCurrentlyFailingSoftPVccEntry_Object = MibTableRow
atmCurrentlyFailingSoftPVccEntry = _AtmCurrentlyFailingSoftPVccEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 5, 1)
)
atmCurrentlyFailingSoftPVccEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ATM-MIB", "atmVclVpi"),
    (0, "ATM-MIB", "atmVclVci"),
    (0, "ATM-SOFT-PVC-MIB", "atmSoftPVccLeafReference"),
)
if mibBuilder.loadTexts:
    atmCurrentlyFailingSoftPVccEntry.setStatus("mandatory")
_AtmCurrentlyFailingSoftPVccTimeStamp_Type = TimeStamp
_AtmCurrentlyFailingSoftPVccTimeStamp_Object = MibTableColumn
atmCurrentlyFailingSoftPVccTimeStamp = _AtmCurrentlyFailingSoftPVccTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 5, 1, 1),
    _AtmCurrentlyFailingSoftPVccTimeStamp_Type()
)
atmCurrentlyFailingSoftPVccTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmCurrentlyFailingSoftPVccTimeStamp.setStatus("mandatory")
_AtmCurrentlyFailingSoftPVpcTable_Object = MibTable
atmCurrentlyFailingSoftPVpcTable = _AtmCurrentlyFailingSoftPVpcTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 6)
)
if mibBuilder.loadTexts:
    atmCurrentlyFailingSoftPVpcTable.setStatus("mandatory")
_AtmCurrentlyFailingSoftPVpcEntry_Object = MibTableRow
atmCurrentlyFailingSoftPVpcEntry = _AtmCurrentlyFailingSoftPVpcEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 6, 1)
)
atmCurrentlyFailingSoftPVpcEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ATM-MIB", "atmVclVpi"),
    (0, "ATM-SOFT-PVC-MIB", "atmSoftPVpcLeafReference"),
)
if mibBuilder.loadTexts:
    atmCurrentlyFailingSoftPVpcEntry.setStatus("mandatory")
_AtmCurrentlyFailingSoftPVpcTimeStamp_Type = TimeStamp
_AtmCurrentlyFailingSoftPVpcTimeStamp_Object = MibTableColumn
atmCurrentlyFailingSoftPVpcTimeStamp = _AtmCurrentlyFailingSoftPVpcTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 6, 1, 1),
    _AtmCurrentlyFailingSoftPVpcTimeStamp_Type()
)
atmCurrentlyFailingSoftPVpcTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmCurrentlyFailingSoftPVpcTimeStamp.setStatus("mandatory")
_AtmSoftPvcMIBTraps_ObjectIdentity = ObjectIdentity
atmSoftPvcMIBTraps = _AtmSoftPvcMIBTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 2)
)
_AtmSoftPvcTraps_ObjectIdentity = ObjectIdentity
atmSoftPvcTraps = _AtmSoftPvcTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 2, 1)
)
_AtmSoftPvcTrapsPrefix_ObjectIdentity = ObjectIdentity
atmSoftPvcTrapsPrefix = _AtmSoftPvcTrapsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 2, 1, 0)
)
_AtmSoftPvcMIBConformance_ObjectIdentity = ObjectIdentity
atmSoftPvcMIBConformance = _AtmSoftPvcMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 3)
)
_AtmSoftPvcMIBCompliances_ObjectIdentity = ObjectIdentity
atmSoftPvcMIBCompliances = _AtmSoftPvcMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 3, 1)
)
_AtmSoftPvcMIBCompliance_ObjectIdentity = ObjectIdentity
atmSoftPvcMIBCompliance = _AtmSoftPvcMIBCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 3, 1, 1)
)
_AtmSoftPvcMIBGroups_ObjectIdentity = ObjectIdentity
atmSoftPvcMIBGroups = _AtmSoftPvcMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 3, 2)
)
_AtmSoftPvcBaseMIBGroup_ObjectIdentity = ObjectIdentity
atmSoftPvcBaseMIBGroup = _AtmSoftPvcBaseMIBGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 3, 2, 1)
)
_AtmSoftPvcVccMIBGroup_ObjectIdentity = ObjectIdentity
atmSoftPvcVccMIBGroup = _AtmSoftPvcVccMIBGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 3, 2, 2)
)
_AtmSoftPvcVpcMIBGroup_ObjectIdentity = ObjectIdentity
atmSoftPvcVpcMIBGroup = _AtmSoftPvcVpcMIBGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 3, 2, 3)
)
_AtmSoftPvcAddressMIBGroup_ObjectIdentity = ObjectIdentity
atmSoftPvcAddressMIBGroup = _AtmSoftPvcAddressMIBGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 3, 2, 4)
)
_AtmCurrentlyFailingSoftPVccMIBGroup_ObjectIdentity = ObjectIdentity
atmCurrentlyFailingSoftPVccMIBGroup = _AtmCurrentlyFailingSoftPVccMIBGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 3, 2, 5)
)
_AtmCurrentlyFailingSoftPVpcMIBGroup_ObjectIdentity = ObjectIdentity
atmCurrentlyFailingSoftPVpcMIBGroup = _AtmCurrentlyFailingSoftPVpcMIBGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 3, 2, 6)
)

# Managed Objects groups


# Notification objects

atmSoftPvcCallFailuresTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 2, 1, 0, 1)
)
atmSoftPvcCallFailuresTrap.setObjects(
      *(("ATM-SOFT-PVC-MIB", "atmSoftPvcCallFailures"),
        ("ATM-SOFT-PVC-MIB", "atmSoftPvcCurrentlyFailingSoftPVccs"),
        ("ATM-SOFT-PVC-MIB", "atmSoftPvcCurrentlyFailingSoftPVpcs"))
)
if mibBuilder.loadTexts:
    atmSoftPvcCallFailuresTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ATM-SOFT-PVC-MIB",
    **{"AtmAddr": AtmAddr,
       "atmForum": atmForum,
       "atmForumNetworkManagement": atmForumNetworkManagement,
       "atmfSoftPvc": atmfSoftPvc,
       "atmSoftPvcMIB": atmSoftPvcMIB,
       "atmSoftPvcMIBObjects": atmSoftPvcMIBObjects,
       "atmSoftPvcBaseGroup": atmSoftPvcBaseGroup,
       "atmSoftPvcCallFailuresTrapEnable": atmSoftPvcCallFailuresTrapEnable,
       "atmSoftPvcCallFailures": atmSoftPvcCallFailures,
       "atmSoftPvcCurrentlyFailingSoftPVccs": atmSoftPvcCurrentlyFailingSoftPVccs,
       "atmSoftPvcCurrentlyFailingSoftPVpcs": atmSoftPvcCurrentlyFailingSoftPVpcs,
       "atmSoftPvcNotificationInterval": atmSoftPvcNotificationInterval,
       "atmSoftPVccTable": atmSoftPVccTable,
       "atmSoftPVccEntry": atmSoftPVccEntry,
       "atmSoftPVccLeafReference": atmSoftPVccLeafReference,
       "atmSoftPVccTargetAddress": atmSoftPVccTargetAddress,
       "atmSoftPVccTargetSelectType": atmSoftPVccTargetSelectType,
       "atmSoftPVccTargetVpi": atmSoftPVccTargetVpi,
       "atmSoftPVccTargetVci": atmSoftPVccTargetVci,
       "atmSoftPVccLastReleaseCause": atmSoftPVccLastReleaseCause,
       "atmSoftPVccLastReleaseDiagnostic": atmSoftPVccLastReleaseDiagnostic,
       "atmSoftPVccOperStatus": atmSoftPVccOperStatus,
       "atmSoftPVccRestart": atmSoftPVccRestart,
       "atmSoftPVccRetryInterval": atmSoftPVccRetryInterval,
       "atmSoftPVccRetryTimer": atmSoftPVccRetryTimer,
       "atmSoftPVccRetryThreshold": atmSoftPVccRetryThreshold,
       "atmSoftPVccRetryFailures": atmSoftPVccRetryFailures,
       "atmSoftPVccRetryLimit": atmSoftPVccRetryLimit,
       "atmSoftPVccRowStatus": atmSoftPVccRowStatus,
       "atmSoftPVpcTable": atmSoftPVpcTable,
       "atmSoftPVpcEntry": atmSoftPVpcEntry,
       "atmSoftPVpcLeafReference": atmSoftPVpcLeafReference,
       "atmSoftPVpcTargetAddress": atmSoftPVpcTargetAddress,
       "atmSoftPVpcTargetSelectType": atmSoftPVpcTargetSelectType,
       "atmSoftPVpcTargetVpi": atmSoftPVpcTargetVpi,
       "atmSoftPVpcLastReleaseCause": atmSoftPVpcLastReleaseCause,
       "atmSoftPVpcLastReleaseDiagnostic": atmSoftPVpcLastReleaseDiagnostic,
       "atmSoftPVpcOperStatus": atmSoftPVpcOperStatus,
       "atmSoftPVpcRestart": atmSoftPVpcRestart,
       "atmSoftPVpcRetryInterval": atmSoftPVpcRetryInterval,
       "atmSoftPVpcRetryTimer": atmSoftPVpcRetryTimer,
       "atmSoftPVpcRetryThreshold": atmSoftPVpcRetryThreshold,
       "atmSoftPVpcRetryFailures": atmSoftPVpcRetryFailures,
       "atmSoftPVpcRetryLimit": atmSoftPVpcRetryLimit,
       "atmSoftPVpcRowStatus": atmSoftPVpcRowStatus,
       "atmInterfaceSoftPvcAddressTable": atmInterfaceSoftPvcAddressTable,
       "atmInterfaceSoftPvcAddressEntry": atmInterfaceSoftPvcAddressEntry,
       "atmInterfaceSoftPvcAddress": atmInterfaceSoftPvcAddress,
       "atmInterfaceSoftPvcAddressRowStatus": atmInterfaceSoftPvcAddressRowStatus,
       "atmCurrentlyFailingSoftPVccTable": atmCurrentlyFailingSoftPVccTable,
       "atmCurrentlyFailingSoftPVccEntry": atmCurrentlyFailingSoftPVccEntry,
       "atmCurrentlyFailingSoftPVccTimeStamp": atmCurrentlyFailingSoftPVccTimeStamp,
       "atmCurrentlyFailingSoftPVpcTable": atmCurrentlyFailingSoftPVpcTable,
       "atmCurrentlyFailingSoftPVpcEntry": atmCurrentlyFailingSoftPVpcEntry,
       "atmCurrentlyFailingSoftPVpcTimeStamp": atmCurrentlyFailingSoftPVpcTimeStamp,
       "atmSoftPvcMIBTraps": atmSoftPvcMIBTraps,
       "atmSoftPvcTraps": atmSoftPvcTraps,
       "atmSoftPvcTrapsPrefix": atmSoftPvcTrapsPrefix,
       "atmSoftPvcCallFailuresTrap": atmSoftPvcCallFailuresTrap,
       "atmSoftPvcMIBConformance": atmSoftPvcMIBConformance,
       "atmSoftPvcMIBCompliances": atmSoftPvcMIBCompliances,
       "atmSoftPvcMIBCompliance": atmSoftPvcMIBCompliance,
       "atmSoftPvcMIBGroups": atmSoftPvcMIBGroups,
       "atmSoftPvcBaseMIBGroup": atmSoftPvcBaseMIBGroup,
       "atmSoftPvcVccMIBGroup": atmSoftPvcVccMIBGroup,
       "atmSoftPvcVpcMIBGroup": atmSoftPvcVpcMIBGroup,
       "atmSoftPvcAddressMIBGroup": atmSoftPvcAddressMIBGroup,
       "atmCurrentlyFailingSoftPVccMIBGroup": atmCurrentlyFailingSoftPVccMIBGroup,
       "atmCurrentlyFailingSoftPVpcMIBGroup": atmCurrentlyFailingSoftPVpcMIBGroup}
)
