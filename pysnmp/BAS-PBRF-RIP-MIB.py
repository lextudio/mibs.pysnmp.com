# SNMP MIB module (BAS-PBRF-RIP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BAS-PBRF-RIP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:45:30 2024
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

(BasChassisId,
 BasInterfaceId,
 BasLogicalPortId,
 BasSlotId,
 basPbrfRIP) = mibBuilder.importSymbols(
    "BAS-MIB",
    "BasChassisId",
    "BasInterfaceId",
    "BasLogicalPortId",
    "BasSlotId",
    "basPbrfRIP")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

basPbrfRIPMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BasPbrfRIPImport_ObjectIdentity = ObjectIdentity
basPbrfRIPImport = _BasPbrfRIPImport_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 1)
)
_BasPbrfRIPImportTable_Object = MibTable
basPbrfRIPImportTable = _BasPbrfRIPImportTable_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    basPbrfRIPImportTable.setStatus("current")
_BasPbrfRIPImportEntry_Object = MibTableRow
basPbrfRIPImportEntry = _BasPbrfRIPImportEntry_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 1, 1, 1)
)
basPbrfRIPImportEntry.setIndexNames(
    (0, "BAS-PBRF-RIP-MIB", "basPbrfRIPImportChassis"),
    (0, "BAS-PBRF-RIP-MIB", "basPbrfRIPImportSlot"),
    (0, "BAS-PBRF-RIP-MIB", "basPbrfRIPImportIf"),
    (0, "BAS-PBRF-RIP-MIB", "basPbrfRIPImportLPort"),
    (0, "BAS-PBRF-RIP-MIB", "basPbrfRIPImportIndex"),
)
if mibBuilder.loadTexts:
    basPbrfRIPImportEntry.setStatus("current")
_BasPbrfRIPImportChassis_Type = BasChassisId
_BasPbrfRIPImportChassis_Object = MibTableColumn
basPbrfRIPImportChassis = _BasPbrfRIPImportChassis_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 1, 1, 1, 1),
    _BasPbrfRIPImportChassis_Type()
)
basPbrfRIPImportChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basPbrfRIPImportChassis.setStatus("current")
_BasPbrfRIPImportSlot_Type = BasSlotId
_BasPbrfRIPImportSlot_Object = MibTableColumn
basPbrfRIPImportSlot = _BasPbrfRIPImportSlot_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 1, 1, 1, 2),
    _BasPbrfRIPImportSlot_Type()
)
basPbrfRIPImportSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basPbrfRIPImportSlot.setStatus("current")
_BasPbrfRIPImportIf_Type = BasInterfaceId
_BasPbrfRIPImportIf_Object = MibTableColumn
basPbrfRIPImportIf = _BasPbrfRIPImportIf_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 1, 1, 1, 3),
    _BasPbrfRIPImportIf_Type()
)
basPbrfRIPImportIf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basPbrfRIPImportIf.setStatus("current")
_BasPbrfRIPImportLPort_Type = BasLogicalPortId
_BasPbrfRIPImportLPort_Object = MibTableColumn
basPbrfRIPImportLPort = _BasPbrfRIPImportLPort_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 1, 1, 1, 4),
    _BasPbrfRIPImportLPort_Type()
)
basPbrfRIPImportLPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basPbrfRIPImportLPort.setStatus("current")
_BasPbrfRIPImportIndex_Type = Integer32
_BasPbrfRIPImportIndex_Object = MibTableColumn
basPbrfRIPImportIndex = _BasPbrfRIPImportIndex_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 1, 1, 1, 5),
    _BasPbrfRIPImportIndex_Type()
)
basPbrfRIPImportIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basPbrfRIPImportIndex.setStatus("current")
_BasPbrfRIPImportTemplateCount_Type = Integer32
_BasPbrfRIPImportTemplateCount_Object = MibTableColumn
basPbrfRIPImportTemplateCount = _BasPbrfRIPImportTemplateCount_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 1, 1, 1, 7),
    _BasPbrfRIPImportTemplateCount_Type()
)
basPbrfRIPImportTemplateCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basPbrfRIPImportTemplateCount.setStatus("current")
_BasPbrfRIPImportRowStatus_Type = RowStatus
_BasPbrfRIPImportRowStatus_Object = MibTableColumn
basPbrfRIPImportRowStatus = _BasPbrfRIPImportRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 1, 1, 1, 8),
    _BasPbrfRIPImportRowStatus_Type()
)
basPbrfRIPImportRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basPbrfRIPImportRowStatus.setStatus("current")


class _BasPbrfRIPImportDescr_Type(OctetString):
    """Custom type basPbrfRIPImportDescr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_BasPbrfRIPImportDescr_Type.__name__ = "OctetString"
_BasPbrfRIPImportDescr_Object = MibTableColumn
basPbrfRIPImportDescr = _BasPbrfRIPImportDescr_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 1, 1, 1, 9),
    _BasPbrfRIPImportDescr_Type()
)
basPbrfRIPImportDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basPbrfRIPImportDescr.setStatus("current")
_BasPbrfRIPImportFilterTempTable_Object = MibTable
basPbrfRIPImportFilterTempTable = _BasPbrfRIPImportFilterTempTable_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    basPbrfRIPImportFilterTempTable.setStatus("current")
_BasPbrfRIPImportFilterTempEntry_Object = MibTableRow
basPbrfRIPImportFilterTempEntry = _BasPbrfRIPImportFilterTempEntry_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 1, 2, 1)
)
basPbrfRIPImportFilterTempEntry.setIndexNames(
    (0, "BAS-PBRF-RIP-MIB", "basPbrfRIPImportFilterTempChassis"),
    (0, "BAS-PBRF-RIP-MIB", "basPbrfRIPImportFilterTempSlot"),
    (0, "BAS-PBRF-RIP-MIB", "basPbrfRIPImportFilterTempIf"),
    (0, "BAS-PBRF-RIP-MIB", "basPbrfRIPImportFilterTempLPort"),
    (0, "BAS-PBRF-RIP-MIB", "basPbrfRIPImportFilterTempIndex"),
    (0, "BAS-PBRF-RIP-MIB", "basPbrfRIPImportFilterTempTemplate"),
)
if mibBuilder.loadTexts:
    basPbrfRIPImportFilterTempEntry.setStatus("current")
_BasPbrfRIPImportFilterTempChassis_Type = BasChassisId
_BasPbrfRIPImportFilterTempChassis_Object = MibTableColumn
basPbrfRIPImportFilterTempChassis = _BasPbrfRIPImportFilterTempChassis_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 1, 2, 1, 1),
    _BasPbrfRIPImportFilterTempChassis_Type()
)
basPbrfRIPImportFilterTempChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basPbrfRIPImportFilterTempChassis.setStatus("current")
_BasPbrfRIPImportFilterTempSlot_Type = BasSlotId
_BasPbrfRIPImportFilterTempSlot_Object = MibTableColumn
basPbrfRIPImportFilterTempSlot = _BasPbrfRIPImportFilterTempSlot_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 1, 2, 1, 2),
    _BasPbrfRIPImportFilterTempSlot_Type()
)
basPbrfRIPImportFilterTempSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basPbrfRIPImportFilterTempSlot.setStatus("current")
_BasPbrfRIPImportFilterTempIf_Type = BasInterfaceId
_BasPbrfRIPImportFilterTempIf_Object = MibTableColumn
basPbrfRIPImportFilterTempIf = _BasPbrfRIPImportFilterTempIf_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 1, 2, 1, 3),
    _BasPbrfRIPImportFilterTempIf_Type()
)
basPbrfRIPImportFilterTempIf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basPbrfRIPImportFilterTempIf.setStatus("current")
_BasPbrfRIPImportFilterTempLPort_Type = BasLogicalPortId
_BasPbrfRIPImportFilterTempLPort_Object = MibTableColumn
basPbrfRIPImportFilterTempLPort = _BasPbrfRIPImportFilterTempLPort_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 1, 2, 1, 4),
    _BasPbrfRIPImportFilterTempLPort_Type()
)
basPbrfRIPImportFilterTempLPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basPbrfRIPImportFilterTempLPort.setStatus("current")
_BasPbrfRIPImportFilterTempIndex_Type = Integer32
_BasPbrfRIPImportFilterTempIndex_Object = MibTableColumn
basPbrfRIPImportFilterTempIndex = _BasPbrfRIPImportFilterTempIndex_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 1, 2, 1, 5),
    _BasPbrfRIPImportFilterTempIndex_Type()
)
basPbrfRIPImportFilterTempIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basPbrfRIPImportFilterTempIndex.setStatus("current")
_BasPbrfRIPImportFilterTempTemplate_Type = Integer32
_BasPbrfRIPImportFilterTempTemplate_Object = MibTableColumn
basPbrfRIPImportFilterTempTemplate = _BasPbrfRIPImportFilterTempTemplate_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 1, 2, 1, 6),
    _BasPbrfRIPImportFilterTempTemplate_Type()
)
basPbrfRIPImportFilterTempTemplate.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basPbrfRIPImportFilterTempTemplate.setStatus("current")
_BasPbrfRIPImportFilterTempOrder_Type = Integer32
_BasPbrfRIPImportFilterTempOrder_Object = MibTableColumn
basPbrfRIPImportFilterTempOrder = _BasPbrfRIPImportFilterTempOrder_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 1, 2, 1, 7),
    _BasPbrfRIPImportFilterTempOrder_Type()
)
basPbrfRIPImportFilterTempOrder.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basPbrfRIPImportFilterTempOrder.setStatus("current")
_BasPbrfRIPImportFilterTempRowStatus_Type = RowStatus
_BasPbrfRIPImportFilterTempRowStatus_Object = MibTableColumn
basPbrfRIPImportFilterTempRowStatus = _BasPbrfRIPImportFilterTempRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 1, 2, 1, 8),
    _BasPbrfRIPImportFilterTempRowStatus_Type()
)
basPbrfRIPImportFilterTempRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basPbrfRIPImportFilterTempRowStatus.setStatus("current")
_BasPbrfRIPImportTemplateTable_Object = MibTable
basPbrfRIPImportTemplateTable = _BasPbrfRIPImportTemplateTable_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 1, 3)
)
if mibBuilder.loadTexts:
    basPbrfRIPImportTemplateTable.setStatus("current")
_BasPbrfRIPImportTemplateEntry_Object = MibTableRow
basPbrfRIPImportTemplateEntry = _BasPbrfRIPImportTemplateEntry_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 1, 3, 1)
)
basPbrfRIPImportTemplateEntry.setIndexNames(
    (0, "BAS-PBRF-RIP-MIB", "basPbrfRIPImportTemplateChassis"),
    (0, "BAS-PBRF-RIP-MIB", "basPbrfRIPImportTemplateSlot"),
    (0, "BAS-PBRF-RIP-MIB", "basPbrfRIPImportTemplateIf"),
    (0, "BAS-PBRF-RIP-MIB", "basPbrfRIPImportTemplateLPort"),
    (0, "BAS-PBRF-RIP-MIB", "basPbrfRIPImportTemplateIndex"),
)
if mibBuilder.loadTexts:
    basPbrfRIPImportTemplateEntry.setStatus("current")
_BasPbrfRIPImportTemplateChassis_Type = BasChassisId
_BasPbrfRIPImportTemplateChassis_Object = MibTableColumn
basPbrfRIPImportTemplateChassis = _BasPbrfRIPImportTemplateChassis_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 1, 3, 1, 1),
    _BasPbrfRIPImportTemplateChassis_Type()
)
basPbrfRIPImportTemplateChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basPbrfRIPImportTemplateChassis.setStatus("current")
_BasPbrfRIPImportTemplateSlot_Type = BasSlotId
_BasPbrfRIPImportTemplateSlot_Object = MibTableColumn
basPbrfRIPImportTemplateSlot = _BasPbrfRIPImportTemplateSlot_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 1, 3, 1, 2),
    _BasPbrfRIPImportTemplateSlot_Type()
)
basPbrfRIPImportTemplateSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basPbrfRIPImportTemplateSlot.setStatus("current")
_BasPbrfRIPImportTemplateIf_Type = BasInterfaceId
_BasPbrfRIPImportTemplateIf_Object = MibTableColumn
basPbrfRIPImportTemplateIf = _BasPbrfRIPImportTemplateIf_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 1, 3, 1, 3),
    _BasPbrfRIPImportTemplateIf_Type()
)
basPbrfRIPImportTemplateIf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basPbrfRIPImportTemplateIf.setStatus("current")
_BasPbrfRIPImportTemplateLPort_Type = BasLogicalPortId
_BasPbrfRIPImportTemplateLPort_Object = MibTableColumn
basPbrfRIPImportTemplateLPort = _BasPbrfRIPImportTemplateLPort_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 1, 3, 1, 4),
    _BasPbrfRIPImportTemplateLPort_Type()
)
basPbrfRIPImportTemplateLPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basPbrfRIPImportTemplateLPort.setStatus("current")
_BasPbrfRIPImportTemplateIndex_Type = Integer32
_BasPbrfRIPImportTemplateIndex_Object = MibTableColumn
basPbrfRIPImportTemplateIndex = _BasPbrfRIPImportTemplateIndex_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 1, 3, 1, 5),
    _BasPbrfRIPImportTemplateIndex_Type()
)
basPbrfRIPImportTemplateIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basPbrfRIPImportTemplateIndex.setStatus("current")
_BasPbrfRIPImportTemplateRouteAddr_Type = IpAddress
_BasPbrfRIPImportTemplateRouteAddr_Object = MibTableColumn
basPbrfRIPImportTemplateRouteAddr = _BasPbrfRIPImportTemplateRouteAddr_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 1, 3, 1, 6),
    _BasPbrfRIPImportTemplateRouteAddr_Type()
)
basPbrfRIPImportTemplateRouteAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basPbrfRIPImportTemplateRouteAddr.setStatus("current")
_BasPbrfRIPImportTemplateRouteMask_Type = IpAddress
_BasPbrfRIPImportTemplateRouteMask_Object = MibTableColumn
basPbrfRIPImportTemplateRouteMask = _BasPbrfRIPImportTemplateRouteMask_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 1, 3, 1, 7),
    _BasPbrfRIPImportTemplateRouteMask_Type()
)
basPbrfRIPImportTemplateRouteMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basPbrfRIPImportTemplateRouteMask.setStatus("current")
_BasPbrfRIPImportTemplatePeerAddr_Type = IpAddress
_BasPbrfRIPImportTemplatePeerAddr_Object = MibTableColumn
basPbrfRIPImportTemplatePeerAddr = _BasPbrfRIPImportTemplatePeerAddr_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 1, 3, 1, 8),
    _BasPbrfRIPImportTemplatePeerAddr_Type()
)
basPbrfRIPImportTemplatePeerAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basPbrfRIPImportTemplatePeerAddr.setStatus("current")
_BasPbrfRIPImportTemplatePeerMask_Type = IpAddress
_BasPbrfRIPImportTemplatePeerMask_Object = MibTableColumn
basPbrfRIPImportTemplatePeerMask = _BasPbrfRIPImportTemplatePeerMask_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 1, 3, 1, 9),
    _BasPbrfRIPImportTemplatePeerMask_Type()
)
basPbrfRIPImportTemplatePeerMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basPbrfRIPImportTemplatePeerMask.setStatus("current")
_BasPbrfRIPImportTemplateTag_Type = Integer32
_BasPbrfRIPImportTemplateTag_Object = MibTableColumn
basPbrfRIPImportTemplateTag = _BasPbrfRIPImportTemplateTag_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 1, 3, 1, 10),
    _BasPbrfRIPImportTemplateTag_Type()
)
basPbrfRIPImportTemplateTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basPbrfRIPImportTemplateTag.setStatus("current")
_BasPbrfRIPImportTemplateKeyBits_Type = Integer32
_BasPbrfRIPImportTemplateKeyBits_Object = MibTableColumn
basPbrfRIPImportTemplateKeyBits = _BasPbrfRIPImportTemplateKeyBits_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 1, 3, 1, 11),
    _BasPbrfRIPImportTemplateKeyBits_Type()
)
basPbrfRIPImportTemplateKeyBits.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basPbrfRIPImportTemplateKeyBits.setStatus("current")
_BasPbrfRIPImportTemplatePref_Type = Integer32
_BasPbrfRIPImportTemplatePref_Object = MibTableColumn
basPbrfRIPImportTemplatePref = _BasPbrfRIPImportTemplatePref_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 1, 3, 1, 12),
    _BasPbrfRIPImportTemplatePref_Type()
)
basPbrfRIPImportTemplatePref.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basPbrfRIPImportTemplatePref.setStatus("current")
_BasPbrfRIPImportTemplateMetric_Type = Integer32
_BasPbrfRIPImportTemplateMetric_Object = MibTableColumn
basPbrfRIPImportTemplateMetric = _BasPbrfRIPImportTemplateMetric_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 1, 3, 1, 13),
    _BasPbrfRIPImportTemplateMetric_Type()
)
basPbrfRIPImportTemplateMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basPbrfRIPImportTemplateMetric.setStatus("current")
_BasPbrfRIPImportTemplateFlags_Type = Integer32
_BasPbrfRIPImportTemplateFlags_Object = MibTableColumn
basPbrfRIPImportTemplateFlags = _BasPbrfRIPImportTemplateFlags_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 1, 3, 1, 14),
    _BasPbrfRIPImportTemplateFlags_Type()
)
basPbrfRIPImportTemplateFlags.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basPbrfRIPImportTemplateFlags.setStatus("current")
_BasPbrfRIPImportTemplateActionTag_Type = Integer32
_BasPbrfRIPImportTemplateActionTag_Object = MibTableColumn
basPbrfRIPImportTemplateActionTag = _BasPbrfRIPImportTemplateActionTag_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 1, 3, 1, 15),
    _BasPbrfRIPImportTemplateActionTag_Type()
)
basPbrfRIPImportTemplateActionTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basPbrfRIPImportTemplateActionTag.setStatus("current")
_BasPbrfRIPImportTemplateRowStatus_Type = RowStatus
_BasPbrfRIPImportTemplateRowStatus_Object = MibTableColumn
basPbrfRIPImportTemplateRowStatus = _BasPbrfRIPImportTemplateRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 1, 3, 1, 16),
    _BasPbrfRIPImportTemplateRowStatus_Type()
)
basPbrfRIPImportTemplateRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basPbrfRIPImportTemplateRowStatus.setStatus("current")


class _BasPbrfRIPImportTemplateDescr_Type(OctetString):
    """Custom type basPbrfRIPImportTemplateDescr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_BasPbrfRIPImportTemplateDescr_Type.__name__ = "OctetString"
_BasPbrfRIPImportTemplateDescr_Object = MibTableColumn
basPbrfRIPImportTemplateDescr = _BasPbrfRIPImportTemplateDescr_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 1, 3, 1, 17),
    _BasPbrfRIPImportTemplateDescr_Type()
)
basPbrfRIPImportTemplateDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basPbrfRIPImportTemplateDescr.setStatus("current")
_BasPbrfRIPExport_ObjectIdentity = ObjectIdentity
basPbrfRIPExport = _BasPbrfRIPExport_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 2)
)
_BasPbrfRIPExportTable_Object = MibTable
basPbrfRIPExportTable = _BasPbrfRIPExportTable_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    basPbrfRIPExportTable.setStatus("current")
_BasPbrfRIPExportEntry_Object = MibTableRow
basPbrfRIPExportEntry = _BasPbrfRIPExportEntry_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 2, 1, 1)
)
basPbrfRIPExportEntry.setIndexNames(
    (0, "BAS-PBRF-RIP-MIB", "basPbrfRIPExportChassis"),
    (0, "BAS-PBRF-RIP-MIB", "basPbrfRIPExportSlot"),
    (0, "BAS-PBRF-RIP-MIB", "basPbrfRIPExportIf"),
    (0, "BAS-PBRF-RIP-MIB", "basPbrfRIPExportLPort"),
    (0, "BAS-PBRF-RIP-MIB", "basPbrfRIPExportIndex"),
)
if mibBuilder.loadTexts:
    basPbrfRIPExportEntry.setStatus("current")
_BasPbrfRIPExportChassis_Type = BasChassisId
_BasPbrfRIPExportChassis_Object = MibTableColumn
basPbrfRIPExportChassis = _BasPbrfRIPExportChassis_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 2, 1, 1, 1),
    _BasPbrfRIPExportChassis_Type()
)
basPbrfRIPExportChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basPbrfRIPExportChassis.setStatus("current")
_BasPbrfRIPExportSlot_Type = BasSlotId
_BasPbrfRIPExportSlot_Object = MibTableColumn
basPbrfRIPExportSlot = _BasPbrfRIPExportSlot_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 2, 1, 1, 2),
    _BasPbrfRIPExportSlot_Type()
)
basPbrfRIPExportSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basPbrfRIPExportSlot.setStatus("current")
_BasPbrfRIPExportIf_Type = BasInterfaceId
_BasPbrfRIPExportIf_Object = MibTableColumn
basPbrfRIPExportIf = _BasPbrfRIPExportIf_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 2, 1, 1, 3),
    _BasPbrfRIPExportIf_Type()
)
basPbrfRIPExportIf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basPbrfRIPExportIf.setStatus("current")
_BasPbrfRIPExportLPort_Type = BasLogicalPortId
_BasPbrfRIPExportLPort_Object = MibTableColumn
basPbrfRIPExportLPort = _BasPbrfRIPExportLPort_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 2, 1, 1, 4),
    _BasPbrfRIPExportLPort_Type()
)
basPbrfRIPExportLPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basPbrfRIPExportLPort.setStatus("current")
_BasPbrfRIPExportIndex_Type = Integer32
_BasPbrfRIPExportIndex_Object = MibTableColumn
basPbrfRIPExportIndex = _BasPbrfRIPExportIndex_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 2, 1, 1, 5),
    _BasPbrfRIPExportIndex_Type()
)
basPbrfRIPExportIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basPbrfRIPExportIndex.setStatus("current")
_BasPbrfRIPExportTemplateCount_Type = Integer32
_BasPbrfRIPExportTemplateCount_Object = MibTableColumn
basPbrfRIPExportTemplateCount = _BasPbrfRIPExportTemplateCount_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 2, 1, 1, 7),
    _BasPbrfRIPExportTemplateCount_Type()
)
basPbrfRIPExportTemplateCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basPbrfRIPExportTemplateCount.setStatus("current")
_BasPbrfRIPExportRowStatus_Type = RowStatus
_BasPbrfRIPExportRowStatus_Object = MibTableColumn
basPbrfRIPExportRowStatus = _BasPbrfRIPExportRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 2, 1, 1, 8),
    _BasPbrfRIPExportRowStatus_Type()
)
basPbrfRIPExportRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basPbrfRIPExportRowStatus.setStatus("current")


class _BasPbrfRIPExportDescr_Type(OctetString):
    """Custom type basPbrfRIPExportDescr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_BasPbrfRIPExportDescr_Type.__name__ = "OctetString"
_BasPbrfRIPExportDescr_Object = MibTableColumn
basPbrfRIPExportDescr = _BasPbrfRIPExportDescr_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 2, 1, 1, 9),
    _BasPbrfRIPExportDescr_Type()
)
basPbrfRIPExportDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basPbrfRIPExportDescr.setStatus("current")
_BasPbrfRIPExportFilterTempTable_Object = MibTable
basPbrfRIPExportFilterTempTable = _BasPbrfRIPExportFilterTempTable_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    basPbrfRIPExportFilterTempTable.setStatus("current")
_BasPbrfRIPExportFilterTempEntry_Object = MibTableRow
basPbrfRIPExportFilterTempEntry = _BasPbrfRIPExportFilterTempEntry_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 2, 2, 1)
)
basPbrfRIPExportFilterTempEntry.setIndexNames(
    (0, "BAS-PBRF-RIP-MIB", "basPbrfRIPExportFilterTempChassis"),
    (0, "BAS-PBRF-RIP-MIB", "basPbrfRIPExportFilterTempSlot"),
    (0, "BAS-PBRF-RIP-MIB", "basPbrfRIPExportFilterTempIf"),
    (0, "BAS-PBRF-RIP-MIB", "basPbrfRIPExportFilterTempLPort"),
    (0, "BAS-PBRF-RIP-MIB", "basPbrfRIPExportFilterTempIndex"),
    (0, "BAS-PBRF-RIP-MIB", "basPbrfRIPExportFilterTempTemplate"),
)
if mibBuilder.loadTexts:
    basPbrfRIPExportFilterTempEntry.setStatus("current")
_BasPbrfRIPExportFilterTempChassis_Type = BasChassisId
_BasPbrfRIPExportFilterTempChassis_Object = MibTableColumn
basPbrfRIPExportFilterTempChassis = _BasPbrfRIPExportFilterTempChassis_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 2, 2, 1, 1),
    _BasPbrfRIPExportFilterTempChassis_Type()
)
basPbrfRIPExportFilterTempChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basPbrfRIPExportFilterTempChassis.setStatus("current")
_BasPbrfRIPExportFilterTempSlot_Type = BasSlotId
_BasPbrfRIPExportFilterTempSlot_Object = MibTableColumn
basPbrfRIPExportFilterTempSlot = _BasPbrfRIPExportFilterTempSlot_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 2, 2, 1, 2),
    _BasPbrfRIPExportFilterTempSlot_Type()
)
basPbrfRIPExportFilterTempSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basPbrfRIPExportFilterTempSlot.setStatus("current")
_BasPbrfRIPExportFilterTempIf_Type = BasInterfaceId
_BasPbrfRIPExportFilterTempIf_Object = MibTableColumn
basPbrfRIPExportFilterTempIf = _BasPbrfRIPExportFilterTempIf_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 2, 2, 1, 3),
    _BasPbrfRIPExportFilterTempIf_Type()
)
basPbrfRIPExportFilterTempIf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basPbrfRIPExportFilterTempIf.setStatus("current")
_BasPbrfRIPExportFilterTempLPort_Type = BasLogicalPortId
_BasPbrfRIPExportFilterTempLPort_Object = MibTableColumn
basPbrfRIPExportFilterTempLPort = _BasPbrfRIPExportFilterTempLPort_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 2, 2, 1, 4),
    _BasPbrfRIPExportFilterTempLPort_Type()
)
basPbrfRIPExportFilterTempLPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basPbrfRIPExportFilterTempLPort.setStatus("current")
_BasPbrfRIPExportFilterTempIndex_Type = Integer32
_BasPbrfRIPExportFilterTempIndex_Object = MibTableColumn
basPbrfRIPExportFilterTempIndex = _BasPbrfRIPExportFilterTempIndex_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 2, 2, 1, 5),
    _BasPbrfRIPExportFilterTempIndex_Type()
)
basPbrfRIPExportFilterTempIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basPbrfRIPExportFilterTempIndex.setStatus("current")
_BasPbrfRIPExportFilterTempTemplate_Type = Integer32
_BasPbrfRIPExportFilterTempTemplate_Object = MibTableColumn
basPbrfRIPExportFilterTempTemplate = _BasPbrfRIPExportFilterTempTemplate_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 2, 2, 1, 6),
    _BasPbrfRIPExportFilterTempTemplate_Type()
)
basPbrfRIPExportFilterTempTemplate.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basPbrfRIPExportFilterTempTemplate.setStatus("current")
_BasPbrfRIPExportFilterTempOrder_Type = Integer32
_BasPbrfRIPExportFilterTempOrder_Object = MibTableColumn
basPbrfRIPExportFilterTempOrder = _BasPbrfRIPExportFilterTempOrder_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 2, 2, 1, 7),
    _BasPbrfRIPExportFilterTempOrder_Type()
)
basPbrfRIPExportFilterTempOrder.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basPbrfRIPExportFilterTempOrder.setStatus("current")
_BasPbrfRIPExportFilterTempRowStatus_Type = RowStatus
_BasPbrfRIPExportFilterTempRowStatus_Object = MibTableColumn
basPbrfRIPExportFilterTempRowStatus = _BasPbrfRIPExportFilterTempRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 2, 2, 1, 8),
    _BasPbrfRIPExportFilterTempRowStatus_Type()
)
basPbrfRIPExportFilterTempRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basPbrfRIPExportFilterTempRowStatus.setStatus("current")
_BasPbrfRIPExportTemplateTable_Object = MibTable
basPbrfRIPExportTemplateTable = _BasPbrfRIPExportTemplateTable_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 2, 3)
)
if mibBuilder.loadTexts:
    basPbrfRIPExportTemplateTable.setStatus("current")
_BasPbrfRIPExportTemplateEntry_Object = MibTableRow
basPbrfRIPExportTemplateEntry = _BasPbrfRIPExportTemplateEntry_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 2, 3, 1)
)
basPbrfRIPExportTemplateEntry.setIndexNames(
    (0, "BAS-PBRF-RIP-MIB", "basPbrfRIPExportTemplateChassis"),
    (0, "BAS-PBRF-RIP-MIB", "basPbrfRIPExportTemplateSlot"),
    (0, "BAS-PBRF-RIP-MIB", "basPbrfRIPExportTemplateIf"),
    (0, "BAS-PBRF-RIP-MIB", "basPbrfRIPExportTemplateLPort"),
    (0, "BAS-PBRF-RIP-MIB", "basPbrfRIPExportTemplateIndex"),
)
if mibBuilder.loadTexts:
    basPbrfRIPExportTemplateEntry.setStatus("current")
_BasPbrfRIPExportTemplateChassis_Type = BasChassisId
_BasPbrfRIPExportTemplateChassis_Object = MibTableColumn
basPbrfRIPExportTemplateChassis = _BasPbrfRIPExportTemplateChassis_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 2, 3, 1, 1),
    _BasPbrfRIPExportTemplateChassis_Type()
)
basPbrfRIPExportTemplateChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basPbrfRIPExportTemplateChassis.setStatus("current")
_BasPbrfRIPExportTemplateSlot_Type = BasSlotId
_BasPbrfRIPExportTemplateSlot_Object = MibTableColumn
basPbrfRIPExportTemplateSlot = _BasPbrfRIPExportTemplateSlot_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 2, 3, 1, 2),
    _BasPbrfRIPExportTemplateSlot_Type()
)
basPbrfRIPExportTemplateSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basPbrfRIPExportTemplateSlot.setStatus("current")
_BasPbrfRIPExportTemplateIf_Type = BasInterfaceId
_BasPbrfRIPExportTemplateIf_Object = MibTableColumn
basPbrfRIPExportTemplateIf = _BasPbrfRIPExportTemplateIf_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 2, 3, 1, 3),
    _BasPbrfRIPExportTemplateIf_Type()
)
basPbrfRIPExportTemplateIf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basPbrfRIPExportTemplateIf.setStatus("current")
_BasPbrfRIPExportTemplateLPort_Type = BasLogicalPortId
_BasPbrfRIPExportTemplateLPort_Object = MibTableColumn
basPbrfRIPExportTemplateLPort = _BasPbrfRIPExportTemplateLPort_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 2, 3, 1, 4),
    _BasPbrfRIPExportTemplateLPort_Type()
)
basPbrfRIPExportTemplateLPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basPbrfRIPExportTemplateLPort.setStatus("current")
_BasPbrfRIPExportTemplateIndex_Type = Integer32
_BasPbrfRIPExportTemplateIndex_Object = MibTableColumn
basPbrfRIPExportTemplateIndex = _BasPbrfRIPExportTemplateIndex_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 2, 3, 1, 5),
    _BasPbrfRIPExportTemplateIndex_Type()
)
basPbrfRIPExportTemplateIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basPbrfRIPExportTemplateIndex.setStatus("current")
_BasPbrfRIPExportTemplateRouteAddr_Type = IpAddress
_BasPbrfRIPExportTemplateRouteAddr_Object = MibTableColumn
basPbrfRIPExportTemplateRouteAddr = _BasPbrfRIPExportTemplateRouteAddr_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 2, 3, 1, 6),
    _BasPbrfRIPExportTemplateRouteAddr_Type()
)
basPbrfRIPExportTemplateRouteAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basPbrfRIPExportTemplateRouteAddr.setStatus("current")
_BasPbrfRIPExportTemplateRouteMask_Type = IpAddress
_BasPbrfRIPExportTemplateRouteMask_Object = MibTableColumn
basPbrfRIPExportTemplateRouteMask = _BasPbrfRIPExportTemplateRouteMask_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 2, 3, 1, 7),
    _BasPbrfRIPExportTemplateRouteMask_Type()
)
basPbrfRIPExportTemplateRouteMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basPbrfRIPExportTemplateRouteMask.setStatus("current")
_BasPbrfRIPExportTemplateIntfAddr_Type = IpAddress
_BasPbrfRIPExportTemplateIntfAddr_Object = MibTableColumn
basPbrfRIPExportTemplateIntfAddr = _BasPbrfRIPExportTemplateIntfAddr_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 2, 3, 1, 8),
    _BasPbrfRIPExportTemplateIntfAddr_Type()
)
basPbrfRIPExportTemplateIntfAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basPbrfRIPExportTemplateIntfAddr.setStatus("current")
_BasPbrfRIPExportTemplateProtocol_Type = Integer32
_BasPbrfRIPExportTemplateProtocol_Object = MibTableColumn
basPbrfRIPExportTemplateProtocol = _BasPbrfRIPExportTemplateProtocol_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 2, 3, 1, 9),
    _BasPbrfRIPExportTemplateProtocol_Type()
)
basPbrfRIPExportTemplateProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basPbrfRIPExportTemplateProtocol.setStatus("current")
_BasPbrfRIPExportTemplateSpecific_Type = IpAddress
_BasPbrfRIPExportTemplateSpecific_Object = MibTableColumn
basPbrfRIPExportTemplateSpecific = _BasPbrfRIPExportTemplateSpecific_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 2, 3, 1, 10),
    _BasPbrfRIPExportTemplateSpecific_Type()
)
basPbrfRIPExportTemplateSpecific.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basPbrfRIPExportTemplateSpecific.setStatus("current")
_BasPbrfRIPExportTemplatePeerMask_Type = IpAddress
_BasPbrfRIPExportTemplatePeerMask_Object = MibTableColumn
basPbrfRIPExportTemplatePeerMask = _BasPbrfRIPExportTemplatePeerMask_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 2, 3, 1, 11),
    _BasPbrfRIPExportTemplatePeerMask_Type()
)
basPbrfRIPExportTemplatePeerMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basPbrfRIPExportTemplatePeerMask.setStatus("current")
_BasPbrfRIPExportTemplateTag_Type = Integer32
_BasPbrfRIPExportTemplateTag_Object = MibTableColumn
basPbrfRIPExportTemplateTag = _BasPbrfRIPExportTemplateTag_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 2, 3, 1, 12),
    _BasPbrfRIPExportTemplateTag_Type()
)
basPbrfRIPExportTemplateTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basPbrfRIPExportTemplateTag.setStatus("current")
_BasPbrfRIPExportTemplateKeyBits_Type = Integer32
_BasPbrfRIPExportTemplateKeyBits_Object = MibTableColumn
basPbrfRIPExportTemplateKeyBits = _BasPbrfRIPExportTemplateKeyBits_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 2, 3, 1, 13),
    _BasPbrfRIPExportTemplateKeyBits_Type()
)
basPbrfRIPExportTemplateKeyBits.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basPbrfRIPExportTemplateKeyBits.setStatus("current")
_BasPbrfRIPExportTemplateMetric_Type = Integer32
_BasPbrfRIPExportTemplateMetric_Object = MibTableColumn
basPbrfRIPExportTemplateMetric = _BasPbrfRIPExportTemplateMetric_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 2, 3, 1, 14),
    _BasPbrfRIPExportTemplateMetric_Type()
)
basPbrfRIPExportTemplateMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basPbrfRIPExportTemplateMetric.setStatus("current")
_BasPbrfRIPExportTemplateFlags_Type = Integer32
_BasPbrfRIPExportTemplateFlags_Object = MibTableColumn
basPbrfRIPExportTemplateFlags = _BasPbrfRIPExportTemplateFlags_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 2, 3, 1, 15),
    _BasPbrfRIPExportTemplateFlags_Type()
)
basPbrfRIPExportTemplateFlags.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basPbrfRIPExportTemplateFlags.setStatus("current")
_BasPbrfRIPExportTemplateActionTag_Type = Integer32
_BasPbrfRIPExportTemplateActionTag_Object = MibTableColumn
basPbrfRIPExportTemplateActionTag = _BasPbrfRIPExportTemplateActionTag_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 2, 3, 1, 16),
    _BasPbrfRIPExportTemplateActionTag_Type()
)
basPbrfRIPExportTemplateActionTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basPbrfRIPExportTemplateActionTag.setStatus("current")
_BasPbrfRIPExportTemplateRowStatus_Type = RowStatus
_BasPbrfRIPExportTemplateRowStatus_Object = MibTableColumn
basPbrfRIPExportTemplateRowStatus = _BasPbrfRIPExportTemplateRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 2, 3, 1, 17),
    _BasPbrfRIPExportTemplateRowStatus_Type()
)
basPbrfRIPExportTemplateRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basPbrfRIPExportTemplateRowStatus.setStatus("current")


class _BasPbrfRIPExportTemplateDescr_Type(OctetString):
    """Custom type basPbrfRIPExportTemplateDescr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_BasPbrfRIPExportTemplateDescr_Type.__name__ = "OctetString"
_BasPbrfRIPExportTemplateDescr_Object = MibTableColumn
basPbrfRIPExportTemplateDescr = _BasPbrfRIPExportTemplateDescr_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 1, 1, 2, 3, 1, 18),
    _BasPbrfRIPExportTemplateDescr_Type()
)
basPbrfRIPExportTemplateDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basPbrfRIPExportTemplateDescr.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BAS-PBRF-RIP-MIB",
    **{"basPbrfRIPMIB": basPbrfRIPMIB,
       "basPbrfRIPImport": basPbrfRIPImport,
       "basPbrfRIPImportTable": basPbrfRIPImportTable,
       "basPbrfRIPImportEntry": basPbrfRIPImportEntry,
       "basPbrfRIPImportChassis": basPbrfRIPImportChassis,
       "basPbrfRIPImportSlot": basPbrfRIPImportSlot,
       "basPbrfRIPImportIf": basPbrfRIPImportIf,
       "basPbrfRIPImportLPort": basPbrfRIPImportLPort,
       "basPbrfRIPImportIndex": basPbrfRIPImportIndex,
       "basPbrfRIPImportTemplateCount": basPbrfRIPImportTemplateCount,
       "basPbrfRIPImportRowStatus": basPbrfRIPImportRowStatus,
       "basPbrfRIPImportDescr": basPbrfRIPImportDescr,
       "basPbrfRIPImportFilterTempTable": basPbrfRIPImportFilterTempTable,
       "basPbrfRIPImportFilterTempEntry": basPbrfRIPImportFilterTempEntry,
       "basPbrfRIPImportFilterTempChassis": basPbrfRIPImportFilterTempChassis,
       "basPbrfRIPImportFilterTempSlot": basPbrfRIPImportFilterTempSlot,
       "basPbrfRIPImportFilterTempIf": basPbrfRIPImportFilterTempIf,
       "basPbrfRIPImportFilterTempLPort": basPbrfRIPImportFilterTempLPort,
       "basPbrfRIPImportFilterTempIndex": basPbrfRIPImportFilterTempIndex,
       "basPbrfRIPImportFilterTempTemplate": basPbrfRIPImportFilterTempTemplate,
       "basPbrfRIPImportFilterTempOrder": basPbrfRIPImportFilterTempOrder,
       "basPbrfRIPImportFilterTempRowStatus": basPbrfRIPImportFilterTempRowStatus,
       "basPbrfRIPImportTemplateTable": basPbrfRIPImportTemplateTable,
       "basPbrfRIPImportTemplateEntry": basPbrfRIPImportTemplateEntry,
       "basPbrfRIPImportTemplateChassis": basPbrfRIPImportTemplateChassis,
       "basPbrfRIPImportTemplateSlot": basPbrfRIPImportTemplateSlot,
       "basPbrfRIPImportTemplateIf": basPbrfRIPImportTemplateIf,
       "basPbrfRIPImportTemplateLPort": basPbrfRIPImportTemplateLPort,
       "basPbrfRIPImportTemplateIndex": basPbrfRIPImportTemplateIndex,
       "basPbrfRIPImportTemplateRouteAddr": basPbrfRIPImportTemplateRouteAddr,
       "basPbrfRIPImportTemplateRouteMask": basPbrfRIPImportTemplateRouteMask,
       "basPbrfRIPImportTemplatePeerAddr": basPbrfRIPImportTemplatePeerAddr,
       "basPbrfRIPImportTemplatePeerMask": basPbrfRIPImportTemplatePeerMask,
       "basPbrfRIPImportTemplateTag": basPbrfRIPImportTemplateTag,
       "basPbrfRIPImportTemplateKeyBits": basPbrfRIPImportTemplateKeyBits,
       "basPbrfRIPImportTemplatePref": basPbrfRIPImportTemplatePref,
       "basPbrfRIPImportTemplateMetric": basPbrfRIPImportTemplateMetric,
       "basPbrfRIPImportTemplateFlags": basPbrfRIPImportTemplateFlags,
       "basPbrfRIPImportTemplateActionTag": basPbrfRIPImportTemplateActionTag,
       "basPbrfRIPImportTemplateRowStatus": basPbrfRIPImportTemplateRowStatus,
       "basPbrfRIPImportTemplateDescr": basPbrfRIPImportTemplateDescr,
       "basPbrfRIPExport": basPbrfRIPExport,
       "basPbrfRIPExportTable": basPbrfRIPExportTable,
       "basPbrfRIPExportEntry": basPbrfRIPExportEntry,
       "basPbrfRIPExportChassis": basPbrfRIPExportChassis,
       "basPbrfRIPExportSlot": basPbrfRIPExportSlot,
       "basPbrfRIPExportIf": basPbrfRIPExportIf,
       "basPbrfRIPExportLPort": basPbrfRIPExportLPort,
       "basPbrfRIPExportIndex": basPbrfRIPExportIndex,
       "basPbrfRIPExportTemplateCount": basPbrfRIPExportTemplateCount,
       "basPbrfRIPExportRowStatus": basPbrfRIPExportRowStatus,
       "basPbrfRIPExportDescr": basPbrfRIPExportDescr,
       "basPbrfRIPExportFilterTempTable": basPbrfRIPExportFilterTempTable,
       "basPbrfRIPExportFilterTempEntry": basPbrfRIPExportFilterTempEntry,
       "basPbrfRIPExportFilterTempChassis": basPbrfRIPExportFilterTempChassis,
       "basPbrfRIPExportFilterTempSlot": basPbrfRIPExportFilterTempSlot,
       "basPbrfRIPExportFilterTempIf": basPbrfRIPExportFilterTempIf,
       "basPbrfRIPExportFilterTempLPort": basPbrfRIPExportFilterTempLPort,
       "basPbrfRIPExportFilterTempIndex": basPbrfRIPExportFilterTempIndex,
       "basPbrfRIPExportFilterTempTemplate": basPbrfRIPExportFilterTempTemplate,
       "basPbrfRIPExportFilterTempOrder": basPbrfRIPExportFilterTempOrder,
       "basPbrfRIPExportFilterTempRowStatus": basPbrfRIPExportFilterTempRowStatus,
       "basPbrfRIPExportTemplateTable": basPbrfRIPExportTemplateTable,
       "basPbrfRIPExportTemplateEntry": basPbrfRIPExportTemplateEntry,
       "basPbrfRIPExportTemplateChassis": basPbrfRIPExportTemplateChassis,
       "basPbrfRIPExportTemplateSlot": basPbrfRIPExportTemplateSlot,
       "basPbrfRIPExportTemplateIf": basPbrfRIPExportTemplateIf,
       "basPbrfRIPExportTemplateLPort": basPbrfRIPExportTemplateLPort,
       "basPbrfRIPExportTemplateIndex": basPbrfRIPExportTemplateIndex,
       "basPbrfRIPExportTemplateRouteAddr": basPbrfRIPExportTemplateRouteAddr,
       "basPbrfRIPExportTemplateRouteMask": basPbrfRIPExportTemplateRouteMask,
       "basPbrfRIPExportTemplateIntfAddr": basPbrfRIPExportTemplateIntfAddr,
       "basPbrfRIPExportTemplateProtocol": basPbrfRIPExportTemplateProtocol,
       "basPbrfRIPExportTemplateSpecific": basPbrfRIPExportTemplateSpecific,
       "basPbrfRIPExportTemplatePeerMask": basPbrfRIPExportTemplatePeerMask,
       "basPbrfRIPExportTemplateTag": basPbrfRIPExportTemplateTag,
       "basPbrfRIPExportTemplateKeyBits": basPbrfRIPExportTemplateKeyBits,
       "basPbrfRIPExportTemplateMetric": basPbrfRIPExportTemplateMetric,
       "basPbrfRIPExportTemplateFlags": basPbrfRIPExportTemplateFlags,
       "basPbrfRIPExportTemplateActionTag": basPbrfRIPExportTemplateActionTag,
       "basPbrfRIPExportTemplateRowStatus": basPbrfRIPExportTemplateRowStatus,
       "basPbrfRIPExportTemplateDescr": basPbrfRIPExportTemplateDescr}
)
