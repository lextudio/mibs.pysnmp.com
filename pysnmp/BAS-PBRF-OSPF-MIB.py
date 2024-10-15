# SNMP MIB module (BAS-PBRF-OSPF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BAS-PBRF-OSPF-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:45:29 2024
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
 basPbrfOSPF) = mibBuilder.importSymbols(
    "BAS-MIB",
    "BasChassisId",
    "BasInterfaceId",
    "BasLogicalPortId",
    "BasSlotId",
    "basPbrfOSPF")

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

basPbrfOSPFMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 2, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BasPbrfOSPFImport_ObjectIdentity = ObjectIdentity
basPbrfOSPFImport = _BasPbrfOSPFImport_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 2, 1, 1)
)
_BasPbrfOSPFImportTable_Object = MibTable
basPbrfOSPFImportTable = _BasPbrfOSPFImportTable_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    basPbrfOSPFImportTable.setStatus("current")
_BasPbrfOSPFImportEntry_Object = MibTableRow
basPbrfOSPFImportEntry = _BasPbrfOSPFImportEntry_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 2, 1, 1, 1, 1)
)
basPbrfOSPFImportEntry.setIndexNames(
    (0, "BAS-PBRF-OSPF-MIB", "basPbrfOSPFImportChassis"),
    (0, "BAS-PBRF-OSPF-MIB", "basPbrfOSPFImportSlot"),
    (0, "BAS-PBRF-OSPF-MIB", "basPbrfOSPFImportIf"),
    (0, "BAS-PBRF-OSPF-MIB", "basPbrfOSPFImportLPort"),
    (0, "BAS-PBRF-OSPF-MIB", "basPbrfOSPFImportIndex"),
)
if mibBuilder.loadTexts:
    basPbrfOSPFImportEntry.setStatus("current")
_BasPbrfOSPFImportChassis_Type = BasChassisId
_BasPbrfOSPFImportChassis_Object = MibTableColumn
basPbrfOSPFImportChassis = _BasPbrfOSPFImportChassis_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 2, 1, 1, 1, 1, 1),
    _BasPbrfOSPFImportChassis_Type()
)
basPbrfOSPFImportChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basPbrfOSPFImportChassis.setStatus("current")
_BasPbrfOSPFImportSlot_Type = BasSlotId
_BasPbrfOSPFImportSlot_Object = MibTableColumn
basPbrfOSPFImportSlot = _BasPbrfOSPFImportSlot_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 2, 1, 1, 1, 1, 2),
    _BasPbrfOSPFImportSlot_Type()
)
basPbrfOSPFImportSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basPbrfOSPFImportSlot.setStatus("current")
_BasPbrfOSPFImportIf_Type = BasInterfaceId
_BasPbrfOSPFImportIf_Object = MibTableColumn
basPbrfOSPFImportIf = _BasPbrfOSPFImportIf_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 2, 1, 1, 1, 1, 3),
    _BasPbrfOSPFImportIf_Type()
)
basPbrfOSPFImportIf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basPbrfOSPFImportIf.setStatus("current")
_BasPbrfOSPFImportLPort_Type = BasLogicalPortId
_BasPbrfOSPFImportLPort_Object = MibTableColumn
basPbrfOSPFImportLPort = _BasPbrfOSPFImportLPort_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 2, 1, 1, 1, 1, 4),
    _BasPbrfOSPFImportLPort_Type()
)
basPbrfOSPFImportLPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basPbrfOSPFImportLPort.setStatus("current")
_BasPbrfOSPFImportIndex_Type = Integer32
_BasPbrfOSPFImportIndex_Object = MibTableColumn
basPbrfOSPFImportIndex = _BasPbrfOSPFImportIndex_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 2, 1, 1, 1, 1, 5),
    _BasPbrfOSPFImportIndex_Type()
)
basPbrfOSPFImportIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basPbrfOSPFImportIndex.setStatus("current")
_BasPbrfOSPFImportTemplateCount_Type = Integer32
_BasPbrfOSPFImportTemplateCount_Object = MibTableColumn
basPbrfOSPFImportTemplateCount = _BasPbrfOSPFImportTemplateCount_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 2, 1, 1, 1, 1, 7),
    _BasPbrfOSPFImportTemplateCount_Type()
)
basPbrfOSPFImportTemplateCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basPbrfOSPFImportTemplateCount.setStatus("current")
_BasPbrfOSPFImportRowStatus_Type = RowStatus
_BasPbrfOSPFImportRowStatus_Object = MibTableColumn
basPbrfOSPFImportRowStatus = _BasPbrfOSPFImportRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 2, 1, 1, 1, 1, 8),
    _BasPbrfOSPFImportRowStatus_Type()
)
basPbrfOSPFImportRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basPbrfOSPFImportRowStatus.setStatus("current")


class _BasPbrfOSPFImportDescr_Type(OctetString):
    """Custom type basPbrfOSPFImportDescr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_BasPbrfOSPFImportDescr_Type.__name__ = "OctetString"
_BasPbrfOSPFImportDescr_Object = MibTableColumn
basPbrfOSPFImportDescr = _BasPbrfOSPFImportDescr_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 2, 1, 1, 1, 1, 9),
    _BasPbrfOSPFImportDescr_Type()
)
basPbrfOSPFImportDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basPbrfOSPFImportDescr.setStatus("current")
_BasPbrfOSPFImportFilterTempTable_Object = MibTable
basPbrfOSPFImportFilterTempTable = _BasPbrfOSPFImportFilterTempTable_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 2, 1, 1, 2)
)
if mibBuilder.loadTexts:
    basPbrfOSPFImportFilterTempTable.setStatus("current")
_BasPbrfOSPFImportFilterTempEntry_Object = MibTableRow
basPbrfOSPFImportFilterTempEntry = _BasPbrfOSPFImportFilterTempEntry_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 2, 1, 1, 2, 1)
)
basPbrfOSPFImportFilterTempEntry.setIndexNames(
    (0, "BAS-PBRF-OSPF-MIB", "basPbrfOSPFImportFilterTempChassis"),
    (0, "BAS-PBRF-OSPF-MIB", "basPbrfOSPFImportFilterTempSlot"),
    (0, "BAS-PBRF-OSPF-MIB", "basPbrfOSPFImportFilterTempIf"),
    (0, "BAS-PBRF-OSPF-MIB", "basPbrfOSPFImportFilterTempLPort"),
    (0, "BAS-PBRF-OSPF-MIB", "basPbrfOSPFImportFilterTempIndex"),
    (0, "BAS-PBRF-OSPF-MIB", "basPbrfOSPFImportFilterTempTemplate"),
)
if mibBuilder.loadTexts:
    basPbrfOSPFImportFilterTempEntry.setStatus("current")
_BasPbrfOSPFImportFilterTempChassis_Type = BasChassisId
_BasPbrfOSPFImportFilterTempChassis_Object = MibTableColumn
basPbrfOSPFImportFilterTempChassis = _BasPbrfOSPFImportFilterTempChassis_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 2, 1, 1, 2, 1, 1),
    _BasPbrfOSPFImportFilterTempChassis_Type()
)
basPbrfOSPFImportFilterTempChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basPbrfOSPFImportFilterTempChassis.setStatus("current")
_BasPbrfOSPFImportFilterTempSlot_Type = BasSlotId
_BasPbrfOSPFImportFilterTempSlot_Object = MibTableColumn
basPbrfOSPFImportFilterTempSlot = _BasPbrfOSPFImportFilterTempSlot_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 2, 1, 1, 2, 1, 2),
    _BasPbrfOSPFImportFilterTempSlot_Type()
)
basPbrfOSPFImportFilterTempSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basPbrfOSPFImportFilterTempSlot.setStatus("current")
_BasPbrfOSPFImportFilterTempIf_Type = BasInterfaceId
_BasPbrfOSPFImportFilterTempIf_Object = MibTableColumn
basPbrfOSPFImportFilterTempIf = _BasPbrfOSPFImportFilterTempIf_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 2, 1, 1, 2, 1, 3),
    _BasPbrfOSPFImportFilterTempIf_Type()
)
basPbrfOSPFImportFilterTempIf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basPbrfOSPFImportFilterTempIf.setStatus("current")
_BasPbrfOSPFImportFilterTempLPort_Type = BasLogicalPortId
_BasPbrfOSPFImportFilterTempLPort_Object = MibTableColumn
basPbrfOSPFImportFilterTempLPort = _BasPbrfOSPFImportFilterTempLPort_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 2, 1, 1, 2, 1, 4),
    _BasPbrfOSPFImportFilterTempLPort_Type()
)
basPbrfOSPFImportFilterTempLPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basPbrfOSPFImportFilterTempLPort.setStatus("current")
_BasPbrfOSPFImportFilterTempIndex_Type = Integer32
_BasPbrfOSPFImportFilterTempIndex_Object = MibTableColumn
basPbrfOSPFImportFilterTempIndex = _BasPbrfOSPFImportFilterTempIndex_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 2, 1, 1, 2, 1, 5),
    _BasPbrfOSPFImportFilterTempIndex_Type()
)
basPbrfOSPFImportFilterTempIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basPbrfOSPFImportFilterTempIndex.setStatus("current")
_BasPbrfOSPFImportFilterTempTemplate_Type = Integer32
_BasPbrfOSPFImportFilterTempTemplate_Object = MibTableColumn
basPbrfOSPFImportFilterTempTemplate = _BasPbrfOSPFImportFilterTempTemplate_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 2, 1, 1, 2, 1, 6),
    _BasPbrfOSPFImportFilterTempTemplate_Type()
)
basPbrfOSPFImportFilterTempTemplate.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basPbrfOSPFImportFilterTempTemplate.setStatus("current")
_BasPbrfOSPFImportFilterTempOrder_Type = Integer32
_BasPbrfOSPFImportFilterTempOrder_Object = MibTableColumn
basPbrfOSPFImportFilterTempOrder = _BasPbrfOSPFImportFilterTempOrder_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 2, 1, 1, 2, 1, 7),
    _BasPbrfOSPFImportFilterTempOrder_Type()
)
basPbrfOSPFImportFilterTempOrder.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basPbrfOSPFImportFilterTempOrder.setStatus("current")
_BasPbrfOSPFImportFilterTempRowStatus_Type = RowStatus
_BasPbrfOSPFImportFilterTempRowStatus_Object = MibTableColumn
basPbrfOSPFImportFilterTempRowStatus = _BasPbrfOSPFImportFilterTempRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 2, 1, 1, 2, 1, 8),
    _BasPbrfOSPFImportFilterTempRowStatus_Type()
)
basPbrfOSPFImportFilterTempRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basPbrfOSPFImportFilterTempRowStatus.setStatus("current")
_BasPbrfOSPFImportTemplateTable_Object = MibTable
basPbrfOSPFImportTemplateTable = _BasPbrfOSPFImportTemplateTable_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 2, 1, 1, 3)
)
if mibBuilder.loadTexts:
    basPbrfOSPFImportTemplateTable.setStatus("current")
_BasPbrfOSPFImportTemplateEntry_Object = MibTableRow
basPbrfOSPFImportTemplateEntry = _BasPbrfOSPFImportTemplateEntry_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 2, 1, 1, 3, 1)
)
basPbrfOSPFImportTemplateEntry.setIndexNames(
    (0, "BAS-PBRF-OSPF-MIB", "basPbrfOSPFImportTemplateChassis"),
    (0, "BAS-PBRF-OSPF-MIB", "basPbrfOSPFImportTemplateSlot"),
    (0, "BAS-PBRF-OSPF-MIB", "basPbrfOSPFImportTemplateIf"),
    (0, "BAS-PBRF-OSPF-MIB", "basPbrfOSPFImportTemplateLPort"),
    (0, "BAS-PBRF-OSPF-MIB", "basPbrfOSPFImportTemplateIndex"),
)
if mibBuilder.loadTexts:
    basPbrfOSPFImportTemplateEntry.setStatus("current")
_BasPbrfOSPFImportTemplateChassis_Type = BasChassisId
_BasPbrfOSPFImportTemplateChassis_Object = MibTableColumn
basPbrfOSPFImportTemplateChassis = _BasPbrfOSPFImportTemplateChassis_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 2, 1, 1, 3, 1, 1),
    _BasPbrfOSPFImportTemplateChassis_Type()
)
basPbrfOSPFImportTemplateChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basPbrfOSPFImportTemplateChassis.setStatus("current")
_BasPbrfOSPFImportTemplateSlot_Type = BasSlotId
_BasPbrfOSPFImportTemplateSlot_Object = MibTableColumn
basPbrfOSPFImportTemplateSlot = _BasPbrfOSPFImportTemplateSlot_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 2, 1, 1, 3, 1, 2),
    _BasPbrfOSPFImportTemplateSlot_Type()
)
basPbrfOSPFImportTemplateSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basPbrfOSPFImportTemplateSlot.setStatus("current")
_BasPbrfOSPFImportTemplateIf_Type = BasInterfaceId
_BasPbrfOSPFImportTemplateIf_Object = MibTableColumn
basPbrfOSPFImportTemplateIf = _BasPbrfOSPFImportTemplateIf_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 2, 1, 1, 3, 1, 3),
    _BasPbrfOSPFImportTemplateIf_Type()
)
basPbrfOSPFImportTemplateIf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basPbrfOSPFImportTemplateIf.setStatus("current")
_BasPbrfOSPFImportTemplateLPort_Type = BasLogicalPortId
_BasPbrfOSPFImportTemplateLPort_Object = MibTableColumn
basPbrfOSPFImportTemplateLPort = _BasPbrfOSPFImportTemplateLPort_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 2, 1, 1, 3, 1, 4),
    _BasPbrfOSPFImportTemplateLPort_Type()
)
basPbrfOSPFImportTemplateLPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basPbrfOSPFImportTemplateLPort.setStatus("current")
_BasPbrfOSPFImportTemplateIndex_Type = Integer32
_BasPbrfOSPFImportTemplateIndex_Object = MibTableColumn
basPbrfOSPFImportTemplateIndex = _BasPbrfOSPFImportTemplateIndex_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 2, 1, 1, 3, 1, 5),
    _BasPbrfOSPFImportTemplateIndex_Type()
)
basPbrfOSPFImportTemplateIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basPbrfOSPFImportTemplateIndex.setStatus("current")
_BasPbrfOSPFImportTemplateRouteAddr_Type = IpAddress
_BasPbrfOSPFImportTemplateRouteAddr_Object = MibTableColumn
basPbrfOSPFImportTemplateRouteAddr = _BasPbrfOSPFImportTemplateRouteAddr_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 2, 1, 1, 3, 1, 6),
    _BasPbrfOSPFImportTemplateRouteAddr_Type()
)
basPbrfOSPFImportTemplateRouteAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basPbrfOSPFImportTemplateRouteAddr.setStatus("current")
_BasPbrfOSPFImportTemplateRouteMask_Type = IpAddress
_BasPbrfOSPFImportTemplateRouteMask_Object = MibTableColumn
basPbrfOSPFImportTemplateRouteMask = _BasPbrfOSPFImportTemplateRouteMask_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 2, 1, 1, 3, 1, 7),
    _BasPbrfOSPFImportTemplateRouteMask_Type()
)
basPbrfOSPFImportTemplateRouteMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basPbrfOSPFImportTemplateRouteMask.setStatus("current")
_BasPbrfOSPFImportTemplatePeerAddr_Type = IpAddress
_BasPbrfOSPFImportTemplatePeerAddr_Object = MibTableColumn
basPbrfOSPFImportTemplatePeerAddr = _BasPbrfOSPFImportTemplatePeerAddr_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 2, 1, 1, 3, 1, 8),
    _BasPbrfOSPFImportTemplatePeerAddr_Type()
)
basPbrfOSPFImportTemplatePeerAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basPbrfOSPFImportTemplatePeerAddr.setStatus("current")
_BasPbrfOSPFImportTemplatePeerMask_Type = IpAddress
_BasPbrfOSPFImportTemplatePeerMask_Object = MibTableColumn
basPbrfOSPFImportTemplatePeerMask = _BasPbrfOSPFImportTemplatePeerMask_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 2, 1, 1, 3, 1, 9),
    _BasPbrfOSPFImportTemplatePeerMask_Type()
)
basPbrfOSPFImportTemplatePeerMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basPbrfOSPFImportTemplatePeerMask.setStatus("current")
_BasPbrfOSPFImportTemplateTag_Type = Integer32
_BasPbrfOSPFImportTemplateTag_Object = MibTableColumn
basPbrfOSPFImportTemplateTag = _BasPbrfOSPFImportTemplateTag_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 2, 1, 1, 3, 1, 10),
    _BasPbrfOSPFImportTemplateTag_Type()
)
basPbrfOSPFImportTemplateTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basPbrfOSPFImportTemplateTag.setStatus("current")
_BasPbrfOSPFImportTemplateKeyBits_Type = Integer32
_BasPbrfOSPFImportTemplateKeyBits_Object = MibTableColumn
basPbrfOSPFImportTemplateKeyBits = _BasPbrfOSPFImportTemplateKeyBits_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 2, 1, 1, 3, 1, 11),
    _BasPbrfOSPFImportTemplateKeyBits_Type()
)
basPbrfOSPFImportTemplateKeyBits.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basPbrfOSPFImportTemplateKeyBits.setStatus("current")
_BasPbrfOSPFImportTemplatePref_Type = Integer32
_BasPbrfOSPFImportTemplatePref_Object = MibTableColumn
basPbrfOSPFImportTemplatePref = _BasPbrfOSPFImportTemplatePref_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 2, 1, 1, 3, 1, 12),
    _BasPbrfOSPFImportTemplatePref_Type()
)
basPbrfOSPFImportTemplatePref.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basPbrfOSPFImportTemplatePref.setStatus("current")
_BasPbrfOSPFImportTemplateFlags_Type = Integer32
_BasPbrfOSPFImportTemplateFlags_Object = MibTableColumn
basPbrfOSPFImportTemplateFlags = _BasPbrfOSPFImportTemplateFlags_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 2, 1, 1, 3, 1, 13),
    _BasPbrfOSPFImportTemplateFlags_Type()
)
basPbrfOSPFImportTemplateFlags.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basPbrfOSPFImportTemplateFlags.setStatus("current")
_BasPbrfOSPFImportTemplateRowStatus_Type = RowStatus
_BasPbrfOSPFImportTemplateRowStatus_Object = MibTableColumn
basPbrfOSPFImportTemplateRowStatus = _BasPbrfOSPFImportTemplateRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 2, 1, 1, 3, 1, 14),
    _BasPbrfOSPFImportTemplateRowStatus_Type()
)
basPbrfOSPFImportTemplateRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basPbrfOSPFImportTemplateRowStatus.setStatus("current")


class _BasPbrfOSPFImportTemplateDescr_Type(OctetString):
    """Custom type basPbrfOSPFImportTemplateDescr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_BasPbrfOSPFImportTemplateDescr_Type.__name__ = "OctetString"
_BasPbrfOSPFImportTemplateDescr_Object = MibTableColumn
basPbrfOSPFImportTemplateDescr = _BasPbrfOSPFImportTemplateDescr_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 2, 1, 1, 3, 1, 15),
    _BasPbrfOSPFImportTemplateDescr_Type()
)
basPbrfOSPFImportTemplateDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basPbrfOSPFImportTemplateDescr.setStatus("current")
_BasPbrfOSPFExport_ObjectIdentity = ObjectIdentity
basPbrfOSPFExport = _BasPbrfOSPFExport_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 2, 1, 2)
)
_BasPbrfOSPFExportTable_Object = MibTable
basPbrfOSPFExportTable = _BasPbrfOSPFExportTable_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 2, 1, 2, 1)
)
if mibBuilder.loadTexts:
    basPbrfOSPFExportTable.setStatus("current")
_BasPbrfOSPFExportEntry_Object = MibTableRow
basPbrfOSPFExportEntry = _BasPbrfOSPFExportEntry_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 2, 1, 2, 1, 1)
)
basPbrfOSPFExportEntry.setIndexNames(
    (0, "BAS-PBRF-OSPF-MIB", "basPbrfOSPFExportChassis"),
    (0, "BAS-PBRF-OSPF-MIB", "basPbrfOSPFExportSlot"),
    (0, "BAS-PBRF-OSPF-MIB", "basPbrfOSPFExportIf"),
    (0, "BAS-PBRF-OSPF-MIB", "basPbrfOSPFExportLPort"),
    (0, "BAS-PBRF-OSPF-MIB", "basPbrfOSPFExportIndex"),
)
if mibBuilder.loadTexts:
    basPbrfOSPFExportEntry.setStatus("current")
_BasPbrfOSPFExportChassis_Type = BasChassisId
_BasPbrfOSPFExportChassis_Object = MibTableColumn
basPbrfOSPFExportChassis = _BasPbrfOSPFExportChassis_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 2, 1, 2, 1, 1, 1),
    _BasPbrfOSPFExportChassis_Type()
)
basPbrfOSPFExportChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basPbrfOSPFExportChassis.setStatus("current")
_BasPbrfOSPFExportSlot_Type = BasSlotId
_BasPbrfOSPFExportSlot_Object = MibTableColumn
basPbrfOSPFExportSlot = _BasPbrfOSPFExportSlot_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 2, 1, 2, 1, 1, 2),
    _BasPbrfOSPFExportSlot_Type()
)
basPbrfOSPFExportSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basPbrfOSPFExportSlot.setStatus("current")
_BasPbrfOSPFExportIf_Type = BasInterfaceId
_BasPbrfOSPFExportIf_Object = MibTableColumn
basPbrfOSPFExportIf = _BasPbrfOSPFExportIf_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 2, 1, 2, 1, 1, 3),
    _BasPbrfOSPFExportIf_Type()
)
basPbrfOSPFExportIf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basPbrfOSPFExportIf.setStatus("current")
_BasPbrfOSPFExportLPort_Type = BasLogicalPortId
_BasPbrfOSPFExportLPort_Object = MibTableColumn
basPbrfOSPFExportLPort = _BasPbrfOSPFExportLPort_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 2, 1, 2, 1, 1, 4),
    _BasPbrfOSPFExportLPort_Type()
)
basPbrfOSPFExportLPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basPbrfOSPFExportLPort.setStatus("current")
_BasPbrfOSPFExportIndex_Type = Integer32
_BasPbrfOSPFExportIndex_Object = MibTableColumn
basPbrfOSPFExportIndex = _BasPbrfOSPFExportIndex_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 2, 1, 2, 1, 1, 5),
    _BasPbrfOSPFExportIndex_Type()
)
basPbrfOSPFExportIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basPbrfOSPFExportIndex.setStatus("current")
_BasPbrfOSPFExportTemplateCount_Type = Integer32
_BasPbrfOSPFExportTemplateCount_Object = MibTableColumn
basPbrfOSPFExportTemplateCount = _BasPbrfOSPFExportTemplateCount_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 2, 1, 2, 1, 1, 7),
    _BasPbrfOSPFExportTemplateCount_Type()
)
basPbrfOSPFExportTemplateCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basPbrfOSPFExportTemplateCount.setStatus("current")
_BasPbrfOSPFExportRowStatus_Type = RowStatus
_BasPbrfOSPFExportRowStatus_Object = MibTableColumn
basPbrfOSPFExportRowStatus = _BasPbrfOSPFExportRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 2, 1, 2, 1, 1, 8),
    _BasPbrfOSPFExportRowStatus_Type()
)
basPbrfOSPFExportRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basPbrfOSPFExportRowStatus.setStatus("current")


class _BasPbrfOSPFExportDescr_Type(OctetString):
    """Custom type basPbrfOSPFExportDescr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_BasPbrfOSPFExportDescr_Type.__name__ = "OctetString"
_BasPbrfOSPFExportDescr_Object = MibTableColumn
basPbrfOSPFExportDescr = _BasPbrfOSPFExportDescr_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 2, 1, 2, 1, 1, 9),
    _BasPbrfOSPFExportDescr_Type()
)
basPbrfOSPFExportDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basPbrfOSPFExportDescr.setStatus("current")
_BasPbrfOSPFExportFilterTempTable_Object = MibTable
basPbrfOSPFExportFilterTempTable = _BasPbrfOSPFExportFilterTempTable_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 2, 1, 2, 2)
)
if mibBuilder.loadTexts:
    basPbrfOSPFExportFilterTempTable.setStatus("current")
_BasPbrfOSPFExportFilterTempEntry_Object = MibTableRow
basPbrfOSPFExportFilterTempEntry = _BasPbrfOSPFExportFilterTempEntry_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 2, 1, 2, 2, 1)
)
basPbrfOSPFExportFilterTempEntry.setIndexNames(
    (0, "BAS-PBRF-OSPF-MIB", "basPbrfOSPFExportFilterTempChassis"),
    (0, "BAS-PBRF-OSPF-MIB", "basPbrfOSPFExportFilterTempSlot"),
    (0, "BAS-PBRF-OSPF-MIB", "basPbrfOSPFExportFilterTempIf"),
    (0, "BAS-PBRF-OSPF-MIB", "basPbrfOSPFExportFilterTempLPort"),
    (0, "BAS-PBRF-OSPF-MIB", "basPbrfOSPFExportFilterTempIndex"),
    (0, "BAS-PBRF-OSPF-MIB", "basPbrfOSPFExportFilterTempTemplate"),
)
if mibBuilder.loadTexts:
    basPbrfOSPFExportFilterTempEntry.setStatus("current")
_BasPbrfOSPFExportFilterTempChassis_Type = BasChassisId
_BasPbrfOSPFExportFilterTempChassis_Object = MibTableColumn
basPbrfOSPFExportFilterTempChassis = _BasPbrfOSPFExportFilterTempChassis_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 2, 1, 2, 2, 1, 1),
    _BasPbrfOSPFExportFilterTempChassis_Type()
)
basPbrfOSPFExportFilterTempChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basPbrfOSPFExportFilterTempChassis.setStatus("current")
_BasPbrfOSPFExportFilterTempSlot_Type = BasSlotId
_BasPbrfOSPFExportFilterTempSlot_Object = MibTableColumn
basPbrfOSPFExportFilterTempSlot = _BasPbrfOSPFExportFilterTempSlot_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 2, 1, 2, 2, 1, 2),
    _BasPbrfOSPFExportFilterTempSlot_Type()
)
basPbrfOSPFExportFilterTempSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basPbrfOSPFExportFilterTempSlot.setStatus("current")
_BasPbrfOSPFExportFilterTempIf_Type = BasInterfaceId
_BasPbrfOSPFExportFilterTempIf_Object = MibTableColumn
basPbrfOSPFExportFilterTempIf = _BasPbrfOSPFExportFilterTempIf_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 2, 1, 2, 2, 1, 3),
    _BasPbrfOSPFExportFilterTempIf_Type()
)
basPbrfOSPFExportFilterTempIf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basPbrfOSPFExportFilterTempIf.setStatus("current")
_BasPbrfOSPFExportFilterTempLPort_Type = BasLogicalPortId
_BasPbrfOSPFExportFilterTempLPort_Object = MibTableColumn
basPbrfOSPFExportFilterTempLPort = _BasPbrfOSPFExportFilterTempLPort_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 2, 1, 2, 2, 1, 4),
    _BasPbrfOSPFExportFilterTempLPort_Type()
)
basPbrfOSPFExportFilterTempLPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basPbrfOSPFExportFilterTempLPort.setStatus("current")
_BasPbrfOSPFExportFilterTempIndex_Type = Integer32
_BasPbrfOSPFExportFilterTempIndex_Object = MibTableColumn
basPbrfOSPFExportFilterTempIndex = _BasPbrfOSPFExportFilterTempIndex_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 2, 1, 2, 2, 1, 5),
    _BasPbrfOSPFExportFilterTempIndex_Type()
)
basPbrfOSPFExportFilterTempIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basPbrfOSPFExportFilterTempIndex.setStatus("current")
_BasPbrfOSPFExportFilterTempTemplate_Type = Integer32
_BasPbrfOSPFExportFilterTempTemplate_Object = MibTableColumn
basPbrfOSPFExportFilterTempTemplate = _BasPbrfOSPFExportFilterTempTemplate_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 2, 1, 2, 2, 1, 6),
    _BasPbrfOSPFExportFilterTempTemplate_Type()
)
basPbrfOSPFExportFilterTempTemplate.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basPbrfOSPFExportFilterTempTemplate.setStatus("current")
_BasPbrfOSPFExportFilterTempOrder_Type = Integer32
_BasPbrfOSPFExportFilterTempOrder_Object = MibTableColumn
basPbrfOSPFExportFilterTempOrder = _BasPbrfOSPFExportFilterTempOrder_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 2, 1, 2, 2, 1, 7),
    _BasPbrfOSPFExportFilterTempOrder_Type()
)
basPbrfOSPFExportFilterTempOrder.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basPbrfOSPFExportFilterTempOrder.setStatus("current")
_BasPbrfOSPFExportFilterTempRowStatus_Type = RowStatus
_BasPbrfOSPFExportFilterTempRowStatus_Object = MibTableColumn
basPbrfOSPFExportFilterTempRowStatus = _BasPbrfOSPFExportFilterTempRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 2, 1, 2, 2, 1, 8),
    _BasPbrfOSPFExportFilterTempRowStatus_Type()
)
basPbrfOSPFExportFilterTempRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basPbrfOSPFExportFilterTempRowStatus.setStatus("current")
_BasPbrfOSPFExportTemplateTable_Object = MibTable
basPbrfOSPFExportTemplateTable = _BasPbrfOSPFExportTemplateTable_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 2, 1, 2, 3)
)
if mibBuilder.loadTexts:
    basPbrfOSPFExportTemplateTable.setStatus("current")
_BasPbrfOSPFExportTemplateEntry_Object = MibTableRow
basPbrfOSPFExportTemplateEntry = _BasPbrfOSPFExportTemplateEntry_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 2, 1, 2, 3, 1)
)
basPbrfOSPFExportTemplateEntry.setIndexNames(
    (0, "BAS-PBRF-OSPF-MIB", "basPbrfOSPFExportTemplateChassis"),
    (0, "BAS-PBRF-OSPF-MIB", "basPbrfOSPFExportTemplateSlot"),
    (0, "BAS-PBRF-OSPF-MIB", "basPbrfOSPFExportTemplateIf"),
    (0, "BAS-PBRF-OSPF-MIB", "basPbrfOSPFExportTemplateLPort"),
    (0, "BAS-PBRF-OSPF-MIB", "basPbrfOSPFExportTemplateIndex"),
)
if mibBuilder.loadTexts:
    basPbrfOSPFExportTemplateEntry.setStatus("current")
_BasPbrfOSPFExportTemplateChassis_Type = BasChassisId
_BasPbrfOSPFExportTemplateChassis_Object = MibTableColumn
basPbrfOSPFExportTemplateChassis = _BasPbrfOSPFExportTemplateChassis_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 2, 1, 2, 3, 1, 1),
    _BasPbrfOSPFExportTemplateChassis_Type()
)
basPbrfOSPFExportTemplateChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basPbrfOSPFExportTemplateChassis.setStatus("current")
_BasPbrfOSPFExportTemplateSlot_Type = BasSlotId
_BasPbrfOSPFExportTemplateSlot_Object = MibTableColumn
basPbrfOSPFExportTemplateSlot = _BasPbrfOSPFExportTemplateSlot_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 2, 1, 2, 3, 1, 2),
    _BasPbrfOSPFExportTemplateSlot_Type()
)
basPbrfOSPFExportTemplateSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basPbrfOSPFExportTemplateSlot.setStatus("current")
_BasPbrfOSPFExportTemplateIf_Type = BasInterfaceId
_BasPbrfOSPFExportTemplateIf_Object = MibTableColumn
basPbrfOSPFExportTemplateIf = _BasPbrfOSPFExportTemplateIf_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 2, 1, 2, 3, 1, 3),
    _BasPbrfOSPFExportTemplateIf_Type()
)
basPbrfOSPFExportTemplateIf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basPbrfOSPFExportTemplateIf.setStatus("current")
_BasPbrfOSPFExportTemplateLPort_Type = BasLogicalPortId
_BasPbrfOSPFExportTemplateLPort_Object = MibTableColumn
basPbrfOSPFExportTemplateLPort = _BasPbrfOSPFExportTemplateLPort_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 2, 1, 2, 3, 1, 4),
    _BasPbrfOSPFExportTemplateLPort_Type()
)
basPbrfOSPFExportTemplateLPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basPbrfOSPFExportTemplateLPort.setStatus("current")
_BasPbrfOSPFExportTemplateIndex_Type = Integer32
_BasPbrfOSPFExportTemplateIndex_Object = MibTableColumn
basPbrfOSPFExportTemplateIndex = _BasPbrfOSPFExportTemplateIndex_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 2, 1, 2, 3, 1, 5),
    _BasPbrfOSPFExportTemplateIndex_Type()
)
basPbrfOSPFExportTemplateIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basPbrfOSPFExportTemplateIndex.setStatus("current")
_BasPbrfOSPFExportTemplateRouteAddr_Type = IpAddress
_BasPbrfOSPFExportTemplateRouteAddr_Object = MibTableColumn
basPbrfOSPFExportTemplateRouteAddr = _BasPbrfOSPFExportTemplateRouteAddr_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 2, 1, 2, 3, 1, 6),
    _BasPbrfOSPFExportTemplateRouteAddr_Type()
)
basPbrfOSPFExportTemplateRouteAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basPbrfOSPFExportTemplateRouteAddr.setStatus("current")
_BasPbrfOSPFExportTemplateRouteMask_Type = IpAddress
_BasPbrfOSPFExportTemplateRouteMask_Object = MibTableColumn
basPbrfOSPFExportTemplateRouteMask = _BasPbrfOSPFExportTemplateRouteMask_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 2, 1, 2, 3, 1, 7),
    _BasPbrfOSPFExportTemplateRouteMask_Type()
)
basPbrfOSPFExportTemplateRouteMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basPbrfOSPFExportTemplateRouteMask.setStatus("current")
_BasPbrfOSPFExportTemplateProtocol_Type = Integer32
_BasPbrfOSPFExportTemplateProtocol_Object = MibTableColumn
basPbrfOSPFExportTemplateProtocol = _BasPbrfOSPFExportTemplateProtocol_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 2, 1, 2, 3, 1, 8),
    _BasPbrfOSPFExportTemplateProtocol_Type()
)
basPbrfOSPFExportTemplateProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basPbrfOSPFExportTemplateProtocol.setStatus("current")
_BasPbrfOSPFExportTemplateSpecific1_Type = IpAddress
_BasPbrfOSPFExportTemplateSpecific1_Object = MibTableColumn
basPbrfOSPFExportTemplateSpecific1 = _BasPbrfOSPFExportTemplateSpecific1_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 2, 1, 2, 3, 1, 9),
    _BasPbrfOSPFExportTemplateSpecific1_Type()
)
basPbrfOSPFExportTemplateSpecific1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basPbrfOSPFExportTemplateSpecific1.setStatus("current")
_BasPbrfOSPFExportTemplateSpecific2_Type = IpAddress
_BasPbrfOSPFExportTemplateSpecific2_Object = MibTableColumn
basPbrfOSPFExportTemplateSpecific2 = _BasPbrfOSPFExportTemplateSpecific2_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 2, 1, 2, 3, 1, 10),
    _BasPbrfOSPFExportTemplateSpecific2_Type()
)
basPbrfOSPFExportTemplateSpecific2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basPbrfOSPFExportTemplateSpecific2.setStatus("current")
_BasPbrfOSPFExportTemplateTag_Type = Integer32
_BasPbrfOSPFExportTemplateTag_Object = MibTableColumn
basPbrfOSPFExportTemplateTag = _BasPbrfOSPFExportTemplateTag_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 2, 1, 2, 3, 1, 11),
    _BasPbrfOSPFExportTemplateTag_Type()
)
basPbrfOSPFExportTemplateTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basPbrfOSPFExportTemplateTag.setStatus("current")
_BasPbrfOSPFExportTemplateKeyBits_Type = Integer32
_BasPbrfOSPFExportTemplateKeyBits_Object = MibTableColumn
basPbrfOSPFExportTemplateKeyBits = _BasPbrfOSPFExportTemplateKeyBits_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 2, 1, 2, 3, 1, 12),
    _BasPbrfOSPFExportTemplateKeyBits_Type()
)
basPbrfOSPFExportTemplateKeyBits.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basPbrfOSPFExportTemplateKeyBits.setStatus("current")
_BasPbrfOSPFExportTemplateMetric_Type = Integer32
_BasPbrfOSPFExportTemplateMetric_Object = MibTableColumn
basPbrfOSPFExportTemplateMetric = _BasPbrfOSPFExportTemplateMetric_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 2, 1, 2, 3, 1, 13),
    _BasPbrfOSPFExportTemplateMetric_Type()
)
basPbrfOSPFExportTemplateMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basPbrfOSPFExportTemplateMetric.setStatus("current")
_BasPbrfOSPFExportTemplateFlags_Type = Integer32
_BasPbrfOSPFExportTemplateFlags_Object = MibTableColumn
basPbrfOSPFExportTemplateFlags = _BasPbrfOSPFExportTemplateFlags_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 2, 1, 2, 3, 1, 14),
    _BasPbrfOSPFExportTemplateFlags_Type()
)
basPbrfOSPFExportTemplateFlags.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basPbrfOSPFExportTemplateFlags.setStatus("current")
_BasPbrfOSPFExportTemplateActionTag_Type = Integer32
_BasPbrfOSPFExportTemplateActionTag_Object = MibTableColumn
basPbrfOSPFExportTemplateActionTag = _BasPbrfOSPFExportTemplateActionTag_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 2, 1, 2, 3, 1, 15),
    _BasPbrfOSPFExportTemplateActionTag_Type()
)
basPbrfOSPFExportTemplateActionTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basPbrfOSPFExportTemplateActionTag.setStatus("current")
_BasPbrfOSPFExportTemplateRowStatus_Type = RowStatus
_BasPbrfOSPFExportTemplateRowStatus_Object = MibTableColumn
basPbrfOSPFExportTemplateRowStatus = _BasPbrfOSPFExportTemplateRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 2, 1, 2, 3, 1, 16),
    _BasPbrfOSPFExportTemplateRowStatus_Type()
)
basPbrfOSPFExportTemplateRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basPbrfOSPFExportTemplateRowStatus.setStatus("current")


class _BasPbrfOSPFExportTemplateDescr_Type(OctetString):
    """Custom type basPbrfOSPFExportTemplateDescr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_BasPbrfOSPFExportTemplateDescr_Type.__name__ = "OctetString"
_BasPbrfOSPFExportTemplateDescr_Object = MibTableColumn
basPbrfOSPFExportTemplateDescr = _BasPbrfOSPFExportTemplateDescr_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 2, 1, 2, 3, 1, 17),
    _BasPbrfOSPFExportTemplateDescr_Type()
)
basPbrfOSPFExportTemplateDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basPbrfOSPFExportTemplateDescr.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BAS-PBRF-OSPF-MIB",
    **{"basPbrfOSPFMIB": basPbrfOSPFMIB,
       "basPbrfOSPFImport": basPbrfOSPFImport,
       "basPbrfOSPFImportTable": basPbrfOSPFImportTable,
       "basPbrfOSPFImportEntry": basPbrfOSPFImportEntry,
       "basPbrfOSPFImportChassis": basPbrfOSPFImportChassis,
       "basPbrfOSPFImportSlot": basPbrfOSPFImportSlot,
       "basPbrfOSPFImportIf": basPbrfOSPFImportIf,
       "basPbrfOSPFImportLPort": basPbrfOSPFImportLPort,
       "basPbrfOSPFImportIndex": basPbrfOSPFImportIndex,
       "basPbrfOSPFImportTemplateCount": basPbrfOSPFImportTemplateCount,
       "basPbrfOSPFImportRowStatus": basPbrfOSPFImportRowStatus,
       "basPbrfOSPFImportDescr": basPbrfOSPFImportDescr,
       "basPbrfOSPFImportFilterTempTable": basPbrfOSPFImportFilterTempTable,
       "basPbrfOSPFImportFilterTempEntry": basPbrfOSPFImportFilterTempEntry,
       "basPbrfOSPFImportFilterTempChassis": basPbrfOSPFImportFilterTempChassis,
       "basPbrfOSPFImportFilterTempSlot": basPbrfOSPFImportFilterTempSlot,
       "basPbrfOSPFImportFilterTempIf": basPbrfOSPFImportFilterTempIf,
       "basPbrfOSPFImportFilterTempLPort": basPbrfOSPFImportFilterTempLPort,
       "basPbrfOSPFImportFilterTempIndex": basPbrfOSPFImportFilterTempIndex,
       "basPbrfOSPFImportFilterTempTemplate": basPbrfOSPFImportFilterTempTemplate,
       "basPbrfOSPFImportFilterTempOrder": basPbrfOSPFImportFilterTempOrder,
       "basPbrfOSPFImportFilterTempRowStatus": basPbrfOSPFImportFilterTempRowStatus,
       "basPbrfOSPFImportTemplateTable": basPbrfOSPFImportTemplateTable,
       "basPbrfOSPFImportTemplateEntry": basPbrfOSPFImportTemplateEntry,
       "basPbrfOSPFImportTemplateChassis": basPbrfOSPFImportTemplateChassis,
       "basPbrfOSPFImportTemplateSlot": basPbrfOSPFImportTemplateSlot,
       "basPbrfOSPFImportTemplateIf": basPbrfOSPFImportTemplateIf,
       "basPbrfOSPFImportTemplateLPort": basPbrfOSPFImportTemplateLPort,
       "basPbrfOSPFImportTemplateIndex": basPbrfOSPFImportTemplateIndex,
       "basPbrfOSPFImportTemplateRouteAddr": basPbrfOSPFImportTemplateRouteAddr,
       "basPbrfOSPFImportTemplateRouteMask": basPbrfOSPFImportTemplateRouteMask,
       "basPbrfOSPFImportTemplatePeerAddr": basPbrfOSPFImportTemplatePeerAddr,
       "basPbrfOSPFImportTemplatePeerMask": basPbrfOSPFImportTemplatePeerMask,
       "basPbrfOSPFImportTemplateTag": basPbrfOSPFImportTemplateTag,
       "basPbrfOSPFImportTemplateKeyBits": basPbrfOSPFImportTemplateKeyBits,
       "basPbrfOSPFImportTemplatePref": basPbrfOSPFImportTemplatePref,
       "basPbrfOSPFImportTemplateFlags": basPbrfOSPFImportTemplateFlags,
       "basPbrfOSPFImportTemplateRowStatus": basPbrfOSPFImportTemplateRowStatus,
       "basPbrfOSPFImportTemplateDescr": basPbrfOSPFImportTemplateDescr,
       "basPbrfOSPFExport": basPbrfOSPFExport,
       "basPbrfOSPFExportTable": basPbrfOSPFExportTable,
       "basPbrfOSPFExportEntry": basPbrfOSPFExportEntry,
       "basPbrfOSPFExportChassis": basPbrfOSPFExportChassis,
       "basPbrfOSPFExportSlot": basPbrfOSPFExportSlot,
       "basPbrfOSPFExportIf": basPbrfOSPFExportIf,
       "basPbrfOSPFExportLPort": basPbrfOSPFExportLPort,
       "basPbrfOSPFExportIndex": basPbrfOSPFExportIndex,
       "basPbrfOSPFExportTemplateCount": basPbrfOSPFExportTemplateCount,
       "basPbrfOSPFExportRowStatus": basPbrfOSPFExportRowStatus,
       "basPbrfOSPFExportDescr": basPbrfOSPFExportDescr,
       "basPbrfOSPFExportFilterTempTable": basPbrfOSPFExportFilterTempTable,
       "basPbrfOSPFExportFilterTempEntry": basPbrfOSPFExportFilterTempEntry,
       "basPbrfOSPFExportFilterTempChassis": basPbrfOSPFExportFilterTempChassis,
       "basPbrfOSPFExportFilterTempSlot": basPbrfOSPFExportFilterTempSlot,
       "basPbrfOSPFExportFilterTempIf": basPbrfOSPFExportFilterTempIf,
       "basPbrfOSPFExportFilterTempLPort": basPbrfOSPFExportFilterTempLPort,
       "basPbrfOSPFExportFilterTempIndex": basPbrfOSPFExportFilterTempIndex,
       "basPbrfOSPFExportFilterTempTemplate": basPbrfOSPFExportFilterTempTemplate,
       "basPbrfOSPFExportFilterTempOrder": basPbrfOSPFExportFilterTempOrder,
       "basPbrfOSPFExportFilterTempRowStatus": basPbrfOSPFExportFilterTempRowStatus,
       "basPbrfOSPFExportTemplateTable": basPbrfOSPFExportTemplateTable,
       "basPbrfOSPFExportTemplateEntry": basPbrfOSPFExportTemplateEntry,
       "basPbrfOSPFExportTemplateChassis": basPbrfOSPFExportTemplateChassis,
       "basPbrfOSPFExportTemplateSlot": basPbrfOSPFExportTemplateSlot,
       "basPbrfOSPFExportTemplateIf": basPbrfOSPFExportTemplateIf,
       "basPbrfOSPFExportTemplateLPort": basPbrfOSPFExportTemplateLPort,
       "basPbrfOSPFExportTemplateIndex": basPbrfOSPFExportTemplateIndex,
       "basPbrfOSPFExportTemplateRouteAddr": basPbrfOSPFExportTemplateRouteAddr,
       "basPbrfOSPFExportTemplateRouteMask": basPbrfOSPFExportTemplateRouteMask,
       "basPbrfOSPFExportTemplateProtocol": basPbrfOSPFExportTemplateProtocol,
       "basPbrfOSPFExportTemplateSpecific1": basPbrfOSPFExportTemplateSpecific1,
       "basPbrfOSPFExportTemplateSpecific2": basPbrfOSPFExportTemplateSpecific2,
       "basPbrfOSPFExportTemplateTag": basPbrfOSPFExportTemplateTag,
       "basPbrfOSPFExportTemplateKeyBits": basPbrfOSPFExportTemplateKeyBits,
       "basPbrfOSPFExportTemplateMetric": basPbrfOSPFExportTemplateMetric,
       "basPbrfOSPFExportTemplateFlags": basPbrfOSPFExportTemplateFlags,
       "basPbrfOSPFExportTemplateActionTag": basPbrfOSPFExportTemplateActionTag,
       "basPbrfOSPFExportTemplateRowStatus": basPbrfOSPFExportTemplateRowStatus,
       "basPbrfOSPFExportTemplateDescr": basPbrfOSPFExportTemplateDescr}
)
