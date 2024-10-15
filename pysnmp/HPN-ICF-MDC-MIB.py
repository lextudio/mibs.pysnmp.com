# SNMP MIB module (HPN-ICF-MDC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-MDC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:01:05 2024
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

(entPhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalIndex")

(hpnicfCommon,) = mibBuilder.importSymbols(
    "HPN-ICF-OID-MIB",
    "hpnicfCommon")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hpnicfMDC = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 136)
)
hpnicfMDC.setRevisions(
        ("2013-03-05 14:48",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class HpnicfMdcActionValue(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("start", 1),
          ("stop", 2))
    )



class HpnicfMdcRunStatus(Integer32, TextualConvention):
    status = "current"
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
        *(("active", 3),
          ("inactive", 1),
          ("starting", 2),
          ("stopping", 4),
          ("updating", 5))
    )



# MIB Managed Objects in the order of their OIDs

_HpnicfMDCScalarObjects_ObjectIdentity = ObjectIdentity
hpnicfMDCScalarObjects = _HpnicfMDCScalarObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 136, 1)
)
_HpnicfMDCMaxMDCNum_Type = Integer32
_HpnicfMDCMaxMDCNum_Object = MibScalar
hpnicfMDCMaxMDCNum = _HpnicfMDCMaxMDCNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 136, 1, 1),
    _HpnicfMDCMaxMDCNum_Type()
)
hpnicfMDCMaxMDCNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfMDCMaxMDCNum.setStatus("current")
_HpnicfMDCCurrentMDCNum_Type = Integer32
_HpnicfMDCCurrentMDCNum_Object = MibScalar
hpnicfMDCCurrentMDCNum = _HpnicfMDCCurrentMDCNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 136, 1, 2),
    _HpnicfMDCCurrentMDCNum_Type()
)
hpnicfMDCCurrentMDCNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfMDCCurrentMDCNum.setStatus("current")
_HpnicfMDCTables_ObjectIdentity = ObjectIdentity
hpnicfMDCTables = _HpnicfMDCTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 136, 2)
)
_HpnicfMDCControl_ObjectIdentity = ObjectIdentity
hpnicfMDCControl = _HpnicfMDCControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 136, 2, 1)
)
_HpnicfMDCControlTable_Object = MibTable
hpnicfMDCControlTable = _HpnicfMDCControlTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 136, 2, 1, 1)
)
if mibBuilder.loadTexts:
    hpnicfMDCControlTable.setStatus("current")
_HpnicfMDCControlEntry_Object = MibTableRow
hpnicfMDCControlEntry = _HpnicfMDCControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 136, 2, 1, 1, 1)
)
hpnicfMDCControlEntry.setIndexNames(
    (0, "HPN-ICF-MDC-MIB", "hpnicfMDCIndex"),
)
if mibBuilder.loadTexts:
    hpnicfMDCControlEntry.setStatus("current")


class _HpnicfMDCIndex_Type(Integer32):
    """Custom type hpnicfMDCIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HpnicfMDCIndex_Type.__name__ = "Integer32"
_HpnicfMDCIndex_Object = MibTableColumn
hpnicfMDCIndex = _HpnicfMDCIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 136, 2, 1, 1, 1, 1),
    _HpnicfMDCIndex_Type()
)
hpnicfMDCIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfMDCIndex.setStatus("current")


class _HpnicfMDCName_Type(DisplayString):
    """Custom type hpnicfMDCName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_HpnicfMDCName_Type.__name__ = "DisplayString"
_HpnicfMDCName_Object = MibTableColumn
hpnicfMDCName = _HpnicfMDCName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 136, 2, 1, 1, 1, 2),
    _HpnicfMDCName_Type()
)
hpnicfMDCName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMDCName.setStatus("current")


class _HpnicfMDCAction_Type(HpnicfMdcActionValue):
    """Custom type hpnicfMDCAction based on HpnicfMdcActionValue"""


_HpnicfMDCAction_Object = MibTableColumn
hpnicfMDCAction = _HpnicfMDCAction_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 136, 2, 1, 1, 1, 3),
    _HpnicfMDCAction_Type()
)
hpnicfMDCAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfMDCAction.setStatus("current")
_HpnicfMDCStatus_Type = HpnicfMdcRunStatus
_HpnicfMDCStatus_Object = MibTableColumn
hpnicfMDCStatus = _HpnicfMDCStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 136, 2, 1, 1, 1, 4),
    _HpnicfMDCStatus_Type()
)
hpnicfMDCStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfMDCStatus.setStatus("current")
_HpnicfMDCRowStatus_Type = RowStatus
_HpnicfMDCRowStatus_Object = MibTableColumn
hpnicfMDCRowStatus = _HpnicfMDCRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 136, 2, 1, 1, 1, 5),
    _HpnicfMDCRowStatus_Type()
)
hpnicfMDCRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMDCRowStatus.setStatus("current")
_HpnicfMDCResource_ObjectIdentity = ObjectIdentity
hpnicfMDCResource = _HpnicfMDCResource_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 136, 2, 2)
)
_HpnicfMDCDISKResourceTable_Object = MibTable
hpnicfMDCDISKResourceTable = _HpnicfMDCDISKResourceTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 136, 2, 2, 1)
)
if mibBuilder.loadTexts:
    hpnicfMDCDISKResourceTable.setStatus("current")
_HpnicfMDCDISKResourceEntry_Object = MibTableRow
hpnicfMDCDISKResourceEntry = _HpnicfMDCDISKResourceEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 136, 2, 2, 1, 1)
)
hpnicfMDCDISKResourceEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "HPN-ICF-MDC-MIB", "hpnicfMDCIndex"),
    (0, "HPN-ICF-MDC-MIB", "hpnicfMDCDISKResourceInstance"),
)
if mibBuilder.loadTexts:
    hpnicfMDCDISKResourceEntry.setStatus("current")


class _HpnicfMDCDISKResourceInstance_Type(Integer32):
    """Custom type hpnicfMDCDISKResourceInstance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HpnicfMDCDISKResourceInstance_Type.__name__ = "Integer32"
_HpnicfMDCDISKResourceInstance_Object = MibTableColumn
hpnicfMDCDISKResourceInstance = _HpnicfMDCDISKResourceInstance_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 136, 2, 2, 1, 1, 1),
    _HpnicfMDCDISKResourceInstance_Type()
)
hpnicfMDCDISKResourceInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfMDCDISKResourceInstance.setStatus("current")


class _HpnicfMDCDISKResourceInstanceName_Type(DisplayString):
    """Custom type hpnicfMDCDISKResourceInstanceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HpnicfMDCDISKResourceInstanceName_Type.__name__ = "DisplayString"
_HpnicfMDCDISKResourceInstanceName_Object = MibTableColumn
hpnicfMDCDISKResourceInstanceName = _HpnicfMDCDISKResourceInstanceName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 136, 2, 2, 1, 1, 2),
    _HpnicfMDCDISKResourceInstanceName_Type()
)
hpnicfMDCDISKResourceInstanceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfMDCDISKResourceInstanceName.setStatus("current")


class _HpnicfMDCDISKResourceMinLimit_Type(Integer32):
    """Custom type hpnicfMDCDISKResourceMinLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HpnicfMDCDISKResourceMinLimit_Type.__name__ = "Integer32"
_HpnicfMDCDISKResourceMinLimit_Object = MibTableColumn
hpnicfMDCDISKResourceMinLimit = _HpnicfMDCDISKResourceMinLimit_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 136, 2, 2, 1, 1, 3),
    _HpnicfMDCDISKResourceMinLimit_Type()
)
hpnicfMDCDISKResourceMinLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfMDCDISKResourceMinLimit.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfMDCDISKResourceMinLimit.setUnits("percent")


class _HpnicfMDCDISKResourceMaxLimit_Type(Integer32):
    """Custom type hpnicfMDCDISKResourceMaxLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_HpnicfMDCDISKResourceMaxLimit_Type.__name__ = "Integer32"
_HpnicfMDCDISKResourceMaxLimit_Object = MibTableColumn
hpnicfMDCDISKResourceMaxLimit = _HpnicfMDCDISKResourceMaxLimit_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 136, 2, 2, 1, 1, 4),
    _HpnicfMDCDISKResourceMaxLimit_Type()
)
hpnicfMDCDISKResourceMaxLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfMDCDISKResourceMaxLimit.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfMDCDISKResourceMaxLimit.setUnits("percent")
_HpnicfMDCDISKResourceReserve_Type = Unsigned32
_HpnicfMDCDISKResourceReserve_Object = MibTableColumn
hpnicfMDCDISKResourceReserve = _HpnicfMDCDISKResourceReserve_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 136, 2, 2, 1, 1, 5),
    _HpnicfMDCDISKResourceReserve_Type()
)
hpnicfMDCDISKResourceReserve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfMDCDISKResourceReserve.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfMDCDISKResourceReserve.setUnits("KB")
_HpnicfMDCDISKResourceQuota_Type = Unsigned32
_HpnicfMDCDISKResourceQuota_Object = MibTableColumn
hpnicfMDCDISKResourceQuota = _HpnicfMDCDISKResourceQuota_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 136, 2, 2, 1, 1, 6),
    _HpnicfMDCDISKResourceQuota_Type()
)
hpnicfMDCDISKResourceQuota.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfMDCDISKResourceQuota.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfMDCDISKResourceQuota.setUnits("KB")
_HpnicfMDCDISKResourceUsage_Type = Unsigned32
_HpnicfMDCDISKResourceUsage_Object = MibTableColumn
hpnicfMDCDISKResourceUsage = _HpnicfMDCDISKResourceUsage_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 136, 2, 2, 1, 1, 7),
    _HpnicfMDCDISKResourceUsage_Type()
)
hpnicfMDCDISKResourceUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfMDCDISKResourceUsage.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfMDCDISKResourceUsage.setUnits("KB")
_HpnicfMDCDISKResourceAvailable_Type = Unsigned32
_HpnicfMDCDISKResourceAvailable_Object = MibTableColumn
hpnicfMDCDISKResourceAvailable = _HpnicfMDCDISKResourceAvailable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 136, 2, 2, 1, 1, 8),
    _HpnicfMDCDISKResourceAvailable_Type()
)
hpnicfMDCDISKResourceAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfMDCDISKResourceAvailable.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfMDCDISKResourceAvailable.setUnits("KB")
_HpnicfMDCMemoryResourceTable_Object = MibTable
hpnicfMDCMemoryResourceTable = _HpnicfMDCMemoryResourceTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 136, 2, 2, 2)
)
if mibBuilder.loadTexts:
    hpnicfMDCMemoryResourceTable.setStatus("current")
_HpnicfMDCMemoryResourceEntry_Object = MibTableRow
hpnicfMDCMemoryResourceEntry = _HpnicfMDCMemoryResourceEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 136, 2, 2, 2, 1)
)
hpnicfMDCMemoryResourceEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "HPN-ICF-MDC-MIB", "hpnicfMDCIndex"),
)
if mibBuilder.loadTexts:
    hpnicfMDCMemoryResourceEntry.setStatus("current")


class _HpnicfMDCMemoryResourceMinLimit_Type(Integer32):
    """Custom type hpnicfMDCMemoryResourceMinLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HpnicfMDCMemoryResourceMinLimit_Type.__name__ = "Integer32"
_HpnicfMDCMemoryResourceMinLimit_Object = MibTableColumn
hpnicfMDCMemoryResourceMinLimit = _HpnicfMDCMemoryResourceMinLimit_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 136, 2, 2, 2, 1, 1),
    _HpnicfMDCMemoryResourceMinLimit_Type()
)
hpnicfMDCMemoryResourceMinLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfMDCMemoryResourceMinLimit.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfMDCMemoryResourceMinLimit.setUnits("percent")


class _HpnicfMDCMemoryResourceMaxLimit_Type(Integer32):
    """Custom type hpnicfMDCMemoryResourceMaxLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_HpnicfMDCMemoryResourceMaxLimit_Type.__name__ = "Integer32"
_HpnicfMDCMemoryResourceMaxLimit_Object = MibTableColumn
hpnicfMDCMemoryResourceMaxLimit = _HpnicfMDCMemoryResourceMaxLimit_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 136, 2, 2, 2, 1, 2),
    _HpnicfMDCMemoryResourceMaxLimit_Type()
)
hpnicfMDCMemoryResourceMaxLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfMDCMemoryResourceMaxLimit.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfMDCMemoryResourceMaxLimit.setUnits("percent")
_HpnicfMDCMemoryResourceReserve_Type = Unsigned32
_HpnicfMDCMemoryResourceReserve_Object = MibTableColumn
hpnicfMDCMemoryResourceReserve = _HpnicfMDCMemoryResourceReserve_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 136, 2, 2, 2, 1, 3),
    _HpnicfMDCMemoryResourceReserve_Type()
)
hpnicfMDCMemoryResourceReserve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfMDCMemoryResourceReserve.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfMDCMemoryResourceReserve.setUnits("KB")
_HpnicfMDCMemoryResourceQuota_Type = Unsigned32
_HpnicfMDCMemoryResourceQuota_Object = MibTableColumn
hpnicfMDCMemoryResourceQuota = _HpnicfMDCMemoryResourceQuota_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 136, 2, 2, 2, 1, 4),
    _HpnicfMDCMemoryResourceQuota_Type()
)
hpnicfMDCMemoryResourceQuota.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfMDCMemoryResourceQuota.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfMDCMemoryResourceQuota.setUnits("KB")
_HpnicfMDCMemoryResourceUsage_Type = Unsigned32
_HpnicfMDCMemoryResourceUsage_Object = MibTableColumn
hpnicfMDCMemoryResourceUsage = _HpnicfMDCMemoryResourceUsage_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 136, 2, 2, 2, 1, 5),
    _HpnicfMDCMemoryResourceUsage_Type()
)
hpnicfMDCMemoryResourceUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfMDCMemoryResourceUsage.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfMDCMemoryResourceUsage.setUnits("KB")
_HpnicfMDCMemoryResourceAvailable_Type = Unsigned32
_HpnicfMDCMemoryResourceAvailable_Object = MibTableColumn
hpnicfMDCMemoryResourceAvailable = _HpnicfMDCMemoryResourceAvailable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 136, 2, 2, 2, 1, 6),
    _HpnicfMDCMemoryResourceAvailable_Type()
)
hpnicfMDCMemoryResourceAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfMDCMemoryResourceAvailable.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfMDCMemoryResourceAvailable.setUnits("KB")
_HpnicfMDCCPUResourceTable_Object = MibTable
hpnicfMDCCPUResourceTable = _HpnicfMDCCPUResourceTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 136, 2, 2, 3)
)
if mibBuilder.loadTexts:
    hpnicfMDCCPUResourceTable.setStatus("current")
_HpnicfMDCCPUResourceEntry_Object = MibTableRow
hpnicfMDCCPUResourceEntry = _HpnicfMDCCPUResourceEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 136, 2, 2, 3, 1)
)
hpnicfMDCCPUResourceEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "HPN-ICF-MDC-MIB", "hpnicfMDCIndex"),
)
if mibBuilder.loadTexts:
    hpnicfMDCCPUResourceEntry.setStatus("current")


class _HpnicfMDCCPUResourceLimit_Type(Integer32):
    """Custom type hpnicfMDCCPUResourceLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_HpnicfMDCCPUResourceLimit_Type.__name__ = "Integer32"
_HpnicfMDCCPUResourceLimit_Object = MibTableColumn
hpnicfMDCCPUResourceLimit = _HpnicfMDCCPUResourceLimit_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 136, 2, 2, 3, 1, 1),
    _HpnicfMDCCPUResourceLimit_Type()
)
hpnicfMDCCPUResourceLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfMDCCPUResourceLimit.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfMDCCPUResourceLimit.setUnits("weight")


class _HpnicfMDCCPUResourceUsage_Type(Integer32):
    """Custom type hpnicfMDCCPUResourceUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HpnicfMDCCPUResourceUsage_Type.__name__ = "Integer32"
_HpnicfMDCCPUResourceUsage_Object = MibTableColumn
hpnicfMDCCPUResourceUsage = _HpnicfMDCCPUResourceUsage_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 136, 2, 2, 3, 1, 2),
    _HpnicfMDCCPUResourceUsage_Type()
)
hpnicfMDCCPUResourceUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfMDCCPUResourceUsage.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfMDCCPUResourceUsage.setUnits("percent")
_HpnicfMDCLocation_ObjectIdentity = ObjectIdentity
hpnicfMDCLocation = _HpnicfMDCLocation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 136, 2, 3)
)
_HpnicfMDCLocationTable_Object = MibTable
hpnicfMDCLocationTable = _HpnicfMDCLocationTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 136, 2, 3, 1)
)
if mibBuilder.loadTexts:
    hpnicfMDCLocationTable.setStatus("current")
_HpnicfMDCLocationEntry_Object = MibTableRow
hpnicfMDCLocationEntry = _HpnicfMDCLocationEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 136, 2, 3, 1, 1)
)
hpnicfMDCLocationEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "HPN-ICF-MDC-MIB", "hpnicfMDCIndex"),
)
if mibBuilder.loadTexts:
    hpnicfMDCLocationEntry.setStatus("current")
_HpnicfMDCLocationStatus_Type = TruthValue
_HpnicfMDCLocationStatus_Object = MibTableColumn
hpnicfMDCLocationStatus = _HpnicfMDCLocationStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 136, 2, 3, 1, 1, 1),
    _HpnicfMDCLocationStatus_Type()
)
hpnicfMDCLocationStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfMDCLocationStatus.setStatus("current")
_HpnicfMDCAllocate_ObjectIdentity = ObjectIdentity
hpnicfMDCAllocate = _HpnicfMDCAllocate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 136, 2, 4)
)
_HpnicfMDCGroupIfTable_Object = MibTable
hpnicfMDCGroupIfTable = _HpnicfMDCGroupIfTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 136, 2, 4, 1)
)
if mibBuilder.loadTexts:
    hpnicfMDCGroupIfTable.setStatus("current")
_HpnicfMDCGroupIfEntry_Object = MibTableRow
hpnicfMDCGroupIfEntry = _HpnicfMDCGroupIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 136, 2, 4, 1, 1)
)
hpnicfMDCGroupIfEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    hpnicfMDCGroupIfEntry.setStatus("current")
_HpnicfMDCGroupIdentity_Type = Integer32
_HpnicfMDCGroupIdentity_Object = MibTableColumn
hpnicfMDCGroupIdentity = _HpnicfMDCGroupIdentity_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 136, 2, 4, 1, 1, 2),
    _HpnicfMDCGroupIdentity_Type()
)
hpnicfMDCGroupIdentity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfMDCGroupIdentity.setStatus("current")
_HpnicfMDCAllocateTable_Object = MibTable
hpnicfMDCAllocateTable = _HpnicfMDCAllocateTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 136, 2, 4, 2)
)
if mibBuilder.loadTexts:
    hpnicfMDCAllocateTable.setStatus("current")
_HpnicfMDCAllocateEntry_Object = MibTableRow
hpnicfMDCAllocateEntry = _HpnicfMDCAllocateEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 136, 2, 4, 2, 1)
)
hpnicfMDCAllocateEntry.setIndexNames(
    (0, "HPN-ICF-MDC-MIB", "hpnicfMDCAllocateGroupIndex"),
)
if mibBuilder.loadTexts:
    hpnicfMDCAllocateEntry.setStatus("current")


class _HpnicfMDCAllocateGroupIndex_Type(Integer32):
    """Custom type hpnicfMDCAllocateGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HpnicfMDCAllocateGroupIndex_Type.__name__ = "Integer32"
_HpnicfMDCAllocateGroupIndex_Object = MibTableColumn
hpnicfMDCAllocateGroupIndex = _HpnicfMDCAllocateGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 136, 2, 4, 2, 1, 1),
    _HpnicfMDCAllocateGroupIndex_Type()
)
hpnicfMDCAllocateGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfMDCAllocateGroupIndex.setStatus("current")


class _HpnicfMDCAllocateGroupDescription_Type(DisplayString):
    """Custom type hpnicfMDCAllocateGroupDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_HpnicfMDCAllocateGroupDescription_Type.__name__ = "DisplayString"
_HpnicfMDCAllocateGroupDescription_Object = MibTableColumn
hpnicfMDCAllocateGroupDescription = _HpnicfMDCAllocateGroupDescription_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 136, 2, 4, 2, 1, 2),
    _HpnicfMDCAllocateGroupDescription_Type()
)
hpnicfMDCAllocateGroupDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfMDCAllocateGroupDescription.setStatus("current")


class _HpnicfMDCAllocateMDCId_Type(Integer32):
    """Custom type hpnicfMDCAllocateMDCId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HpnicfMDCAllocateMDCId_Type.__name__ = "Integer32"
_HpnicfMDCAllocateMDCId_Object = MibTableColumn
hpnicfMDCAllocateMDCId = _HpnicfMDCAllocateMDCId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 136, 2, 4, 2, 1, 3),
    _HpnicfMDCAllocateMDCId_Type()
)
hpnicfMDCAllocateMDCId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfMDCAllocateMDCId.setStatus("current")
_HpnicfMDCNotification_ObjectIdentity = ObjectIdentity
hpnicfMDCNotification = _HpnicfMDCNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 136, 3)
)
_HpnicfMDCNotificationObjects_ObjectIdentity = ObjectIdentity
hpnicfMDCNotificationObjects = _HpnicfMDCNotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 136, 3, 0)
)

# Managed Objects groups


# Notification objects

hpnicfMDCStateChangeToActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 136, 3, 0, 1)
)
hpnicfMDCStateChangeToActive.setObjects(
      *(("HPN-ICF-MDC-MIB", "hpnicfMDCIndex"),
        ("HPN-ICF-MDC-MIB", "hpnicfMDCName"))
)
if mibBuilder.loadTexts:
    hpnicfMDCStateChangeToActive.setStatus(
        "current"
    )

hpnicfMDCStateChangeToInactive = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 136, 3, 0, 2)
)
hpnicfMDCStateChangeToInactive.setObjects(
      *(("HPN-ICF-MDC-MIB", "hpnicfMDCIndex"),
        ("HPN-ICF-MDC-MIB", "hpnicfMDCName"))
)
if mibBuilder.loadTexts:
    hpnicfMDCStateChangeToInactive.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-MDC-MIB",
    **{"HpnicfMdcActionValue": HpnicfMdcActionValue,
       "HpnicfMdcRunStatus": HpnicfMdcRunStatus,
       "hpnicfMDC": hpnicfMDC,
       "hpnicfMDCScalarObjects": hpnicfMDCScalarObjects,
       "hpnicfMDCMaxMDCNum": hpnicfMDCMaxMDCNum,
       "hpnicfMDCCurrentMDCNum": hpnicfMDCCurrentMDCNum,
       "hpnicfMDCTables": hpnicfMDCTables,
       "hpnicfMDCControl": hpnicfMDCControl,
       "hpnicfMDCControlTable": hpnicfMDCControlTable,
       "hpnicfMDCControlEntry": hpnicfMDCControlEntry,
       "hpnicfMDCIndex": hpnicfMDCIndex,
       "hpnicfMDCName": hpnicfMDCName,
       "hpnicfMDCAction": hpnicfMDCAction,
       "hpnicfMDCStatus": hpnicfMDCStatus,
       "hpnicfMDCRowStatus": hpnicfMDCRowStatus,
       "hpnicfMDCResource": hpnicfMDCResource,
       "hpnicfMDCDISKResourceTable": hpnicfMDCDISKResourceTable,
       "hpnicfMDCDISKResourceEntry": hpnicfMDCDISKResourceEntry,
       "hpnicfMDCDISKResourceInstance": hpnicfMDCDISKResourceInstance,
       "hpnicfMDCDISKResourceInstanceName": hpnicfMDCDISKResourceInstanceName,
       "hpnicfMDCDISKResourceMinLimit": hpnicfMDCDISKResourceMinLimit,
       "hpnicfMDCDISKResourceMaxLimit": hpnicfMDCDISKResourceMaxLimit,
       "hpnicfMDCDISKResourceReserve": hpnicfMDCDISKResourceReserve,
       "hpnicfMDCDISKResourceQuota": hpnicfMDCDISKResourceQuota,
       "hpnicfMDCDISKResourceUsage": hpnicfMDCDISKResourceUsage,
       "hpnicfMDCDISKResourceAvailable": hpnicfMDCDISKResourceAvailable,
       "hpnicfMDCMemoryResourceTable": hpnicfMDCMemoryResourceTable,
       "hpnicfMDCMemoryResourceEntry": hpnicfMDCMemoryResourceEntry,
       "hpnicfMDCMemoryResourceMinLimit": hpnicfMDCMemoryResourceMinLimit,
       "hpnicfMDCMemoryResourceMaxLimit": hpnicfMDCMemoryResourceMaxLimit,
       "hpnicfMDCMemoryResourceReserve": hpnicfMDCMemoryResourceReserve,
       "hpnicfMDCMemoryResourceQuota": hpnicfMDCMemoryResourceQuota,
       "hpnicfMDCMemoryResourceUsage": hpnicfMDCMemoryResourceUsage,
       "hpnicfMDCMemoryResourceAvailable": hpnicfMDCMemoryResourceAvailable,
       "hpnicfMDCCPUResourceTable": hpnicfMDCCPUResourceTable,
       "hpnicfMDCCPUResourceEntry": hpnicfMDCCPUResourceEntry,
       "hpnicfMDCCPUResourceLimit": hpnicfMDCCPUResourceLimit,
       "hpnicfMDCCPUResourceUsage": hpnicfMDCCPUResourceUsage,
       "hpnicfMDCLocation": hpnicfMDCLocation,
       "hpnicfMDCLocationTable": hpnicfMDCLocationTable,
       "hpnicfMDCLocationEntry": hpnicfMDCLocationEntry,
       "hpnicfMDCLocationStatus": hpnicfMDCLocationStatus,
       "hpnicfMDCAllocate": hpnicfMDCAllocate,
       "hpnicfMDCGroupIfTable": hpnicfMDCGroupIfTable,
       "hpnicfMDCGroupIfEntry": hpnicfMDCGroupIfEntry,
       "hpnicfMDCGroupIdentity": hpnicfMDCGroupIdentity,
       "hpnicfMDCAllocateTable": hpnicfMDCAllocateTable,
       "hpnicfMDCAllocateEntry": hpnicfMDCAllocateEntry,
       "hpnicfMDCAllocateGroupIndex": hpnicfMDCAllocateGroupIndex,
       "hpnicfMDCAllocateGroupDescription": hpnicfMDCAllocateGroupDescription,
       "hpnicfMDCAllocateMDCId": hpnicfMDCAllocateMDCId,
       "hpnicfMDCNotification": hpnicfMDCNotification,
       "hpnicfMDCNotificationObjects": hpnicfMDCNotificationObjects,
       "hpnicfMDCStateChangeToActive": hpnicfMDCStateChangeToActive,
       "hpnicfMDCStateChangeToInactive": hpnicfMDCStateChangeToInactive}
)
