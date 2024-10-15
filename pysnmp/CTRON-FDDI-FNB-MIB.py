# SNMP MIB module (CTRON-FDDI-FNB-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CTRON-FDDI-FNB-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:18:51 2024
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

(ctFDDIFnb,) = mibBuilder.importSymbols(
    "CTRON-MIB-NAMES",
    "ctFDDIFnb")

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

_CtFDDIResource_ObjectIdentity = ObjectIdentity
ctFDDIResource = _CtFDDIResource_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 1)
)
_CtFDDIResourceTable_Object = MibTable
ctFDDIResourceTable = _CtFDDIResourceTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ctFDDIResourceTable.setStatus("mandatory")
_CtFDDIResourceEntry_Object = MibTableRow
ctFDDIResourceEntry = _CtFDDIResourceEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 1, 1, 1)
)
ctFDDIResourceEntry.setIndexNames(
    (0, "CTRON-FDDI-FNB-MIB", "ctFDDIResourceSlotID"),
    (0, "CTRON-FDDI-FNB-MIB", "ctFDDIResourceID"),
)
if mibBuilder.loadTexts:
    ctFDDIResourceEntry.setStatus("mandatory")


class _CtFDDIResourceSlotID_Type(Integer32):
    """Custom type ctFDDIResourceSlotID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_CtFDDIResourceSlotID_Type.__name__ = "Integer32"
_CtFDDIResourceSlotID_Object = MibTableColumn
ctFDDIResourceSlotID = _CtFDDIResourceSlotID_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 1, 1, 1, 1),
    _CtFDDIResourceSlotID_Type()
)
ctFDDIResourceSlotID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctFDDIResourceSlotID.setStatus("mandatory")
_CtFDDIResourceID_Type = Integer32
_CtFDDIResourceID_Object = MibTableColumn
ctFDDIResourceID = _CtFDDIResourceID_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 1, 1, 1, 2),
    _CtFDDIResourceID_Type()
)
ctFDDIResourceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctFDDIResourceID.setStatus("mandatory")
_CtFDDIResourceType_Type = ObjectIdentifier
_CtFDDIResourceType_Object = MibTableColumn
ctFDDIResourceType = _CtFDDIResourceType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 1, 1, 1, 3),
    _CtFDDIResourceType_Type()
)
ctFDDIResourceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctFDDIResourceType.setStatus("mandatory")
_CtFDDIResourceNumbInstance_Type = Integer32
_CtFDDIResourceNumbInstance_Object = MibTableColumn
ctFDDIResourceNumbInstance = _CtFDDIResourceNumbInstance_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 1, 1, 1, 4),
    _CtFDDIResourceNumbInstance_Type()
)
ctFDDIResourceNumbInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctFDDIResourceNumbInstance.setStatus("mandatory")
_CtFDDINonMux_ObjectIdentity = ObjectIdentity
ctFDDINonMux = _CtFDDINonMux_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 2)
)
_CtFDDINonMuxCapTable_Object = MibTable
ctFDDINonMuxCapTable = _CtFDDINonMuxCapTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 2, 1)
)
if mibBuilder.loadTexts:
    ctFDDINonMuxCapTable.setStatus("mandatory")
_CtFDDINonMuxCapEntry_Object = MibTableRow
ctFDDINonMuxCapEntry = _CtFDDINonMuxCapEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 2, 1, 1)
)
ctFDDINonMuxCapEntry.setIndexNames(
    (0, "CTRON-FDDI-FNB-MIB", "ctFDDINMSlot"),
    (0, "CTRON-FDDI-FNB-MIB", "ctFDDINMConfigID"),
)
if mibBuilder.loadTexts:
    ctFDDINonMuxCapEntry.setStatus("mandatory")


class _CtFDDINMSlot_Type(Integer32):
    """Custom type ctFDDINMSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_CtFDDINMSlot_Type.__name__ = "Integer32"
_CtFDDINMSlot_Object = MibTableColumn
ctFDDINMSlot = _CtFDDINMSlot_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 2, 1, 1, 1),
    _CtFDDINMSlot_Type()
)
ctFDDINMSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctFDDINMSlot.setStatus("mandatory")
_CtFDDINMConfigID_Type = Integer32
_CtFDDINMConfigID_Object = MibTableColumn
ctFDDINMConfigID = _CtFDDINMConfigID_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 2, 1, 1, 2),
    _CtFDDINMConfigID_Type()
)
ctFDDINMConfigID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctFDDINMConfigID.setStatus("mandatory")
_CtFDDINMConfig_Type = DisplayString
_CtFDDINMConfig_Object = MibTableColumn
ctFDDINMConfig = _CtFDDINMConfig_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 2, 1, 1, 3),
    _CtFDDINMConfig_Type()
)
ctFDDINMConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctFDDINMConfig.setStatus("mandatory")
_CtFDDINMConfigDesc_Type = DisplayString
_CtFDDINMConfigDesc_Object = MibTableColumn
ctFDDINMConfigDesc = _CtFDDINMConfigDesc_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 2, 1, 1, 4),
    _CtFDDINMConfigDesc_Type()
)
ctFDDINMConfigDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctFDDINMConfigDesc.setStatus("mandatory")
_CtFDDINonMuxCapEnableTable_Object = MibTable
ctFDDINonMuxCapEnableTable = _CtFDDINonMuxCapEnableTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 2, 2)
)
if mibBuilder.loadTexts:
    ctFDDINonMuxCapEnableTable.setStatus("mandatory")
_CtFDDINonMuxCapEnableEntry_Object = MibTableRow
ctFDDINonMuxCapEnableEntry = _CtFDDINonMuxCapEnableEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 2, 2, 1)
)
ctFDDINonMuxCapEnableEntry.setIndexNames(
    (0, "CTRON-FDDI-FNB-MIB", "ctFDDINMEnableSlot"),
)
if mibBuilder.loadTexts:
    ctFDDINonMuxCapEnableEntry.setStatus("mandatory")
_CtFDDINMEnableSlot_Type = Integer32
_CtFDDINMEnableSlot_Object = MibTableColumn
ctFDDINMEnableSlot = _CtFDDINMEnableSlot_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 2, 2, 1, 1),
    _CtFDDINMEnableSlot_Type()
)
ctFDDINMEnableSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctFDDINMEnableSlot.setStatus("mandatory")
_CtFDDINMCapEnable_Type = Integer32
_CtFDDINMCapEnable_Object = MibTableColumn
ctFDDINMCapEnable = _CtFDDINMCapEnable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 2, 2, 1, 2),
    _CtFDDINMCapEnable_Type()
)
ctFDDINMCapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctFDDINMCapEnable.setStatus("mandatory")
_CtFDDINonMuxConnectionTable_Object = MibTable
ctFDDINonMuxConnectionTable = _CtFDDINonMuxConnectionTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 2, 3)
)
if mibBuilder.loadTexts:
    ctFDDINonMuxConnectionTable.setStatus("mandatory")
_CtFDDINonMuxConnectionEntry_Object = MibTableRow
ctFDDINonMuxConnectionEntry = _CtFDDINonMuxConnectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 2, 3, 1)
)
ctFDDINonMuxConnectionEntry.setIndexNames(
    (0, "CTRON-FDDI-FNB-MIB", "ctFDDINMConnectionSlot"),
    (0, "CTRON-FDDI-FNB-MIB", "ctFDDINMConnectionID"),
)
if mibBuilder.loadTexts:
    ctFDDINonMuxConnectionEntry.setStatus("mandatory")
_CtFDDINMConnectionSlot_Type = Integer32
_CtFDDINMConnectionSlot_Object = MibTableColumn
ctFDDINMConnectionSlot = _CtFDDINMConnectionSlot_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 2, 3, 1, 1),
    _CtFDDINMConnectionSlot_Type()
)
ctFDDINMConnectionSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctFDDINMConnectionSlot.setStatus("mandatory")
_CtFDDINMConnectionID_Type = Integer32
_CtFDDINMConnectionID_Object = MibTableColumn
ctFDDINMConnectionID = _CtFDDINMConnectionID_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 2, 3, 1, 2),
    _CtFDDINMConnectionID_Type()
)
ctFDDINMConnectionID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctFDDINMConnectionID.setStatus("mandatory")
_CtFDDINMSMT_Type = Integer32
_CtFDDINMSMT_Object = MibTableColumn
ctFDDINMSMT = _CtFDDINMSMT_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 2, 3, 1, 3),
    _CtFDDINMSMT_Type()
)
ctFDDINMSMT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctFDDINMSMT.setStatus("mandatory")
_CtFDDINMMAC_Type = Integer32
_CtFDDINMMAC_Object = MibTableColumn
ctFDDINMMAC = _CtFDDINMMAC_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 2, 3, 1, 4),
    _CtFDDINMMAC_Type()
)
ctFDDINMMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctFDDINMMAC.setStatus("mandatory")
_CtFDDINMBytes_Type = Integer32
_CtFDDINMBytes_Object = MibTableColumn
ctFDDINMBytes = _CtFDDINMBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 2, 3, 1, 5),
    _CtFDDINMBytes_Type()
)
ctFDDINMBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctFDDINMBytes.setStatus("mandatory")
_CtFDDINMFrames_Type = Integer32
_CtFDDINMFrames_Object = MibTableColumn
ctFDDINMFrames = _CtFDDINMFrames_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 2, 3, 1, 6),
    _CtFDDINMFrames_Type()
)
ctFDDINMFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctFDDINMFrames.setStatus("mandatory")
_CtFDDINonMuxInterfaceTable_Object = MibTable
ctFDDINonMuxInterfaceTable = _CtFDDINonMuxInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 2, 4)
)
if mibBuilder.loadTexts:
    ctFDDINonMuxInterfaceTable.setStatus("mandatory")
_CtFDDINonMuxInterfaceEntry_Object = MibTableRow
ctFDDINonMuxInterfaceEntry = _CtFDDINonMuxInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 2, 4, 1)
)
ctFDDINonMuxInterfaceEntry.setIndexNames(
    (0, "CTRON-FDDI-FNB-MIB", "ctFDDINMInterSlot"),
)
if mibBuilder.loadTexts:
    ctFDDINonMuxInterfaceEntry.setStatus("mandatory")
_CtFDDINMInterSlot_Type = Integer32
_CtFDDINMInterSlot_Object = MibTableColumn
ctFDDINMInterSlot = _CtFDDINMInterSlot_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 2, 4, 1, 1),
    _CtFDDINMInterSlot_Type()
)
ctFDDINMInterSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctFDDINMInterSlot.setStatus("mandatory")
_CtFDDINMNumbInterfaces_Type = Integer32
_CtFDDINMNumbInterfaces_Object = MibTableColumn
ctFDDINMNumbInterfaces = _CtFDDINMNumbInterfaces_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 2, 4, 1, 2),
    _CtFDDINMNumbInterfaces_Type()
)
ctFDDINMNumbInterfaces.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctFDDINMNumbInterfaces.setStatus("mandatory")
_CtFDDIMux_ObjectIdentity = ObjectIdentity
ctFDDIMux = _CtFDDIMux_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 3)
)
_CtFDDIMuxCapTable_Object = MibTable
ctFDDIMuxCapTable = _CtFDDIMuxCapTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 3, 1)
)
if mibBuilder.loadTexts:
    ctFDDIMuxCapTable.setStatus("mandatory")
_CtFDDIMuxCapEntry_Object = MibTableRow
ctFDDIMuxCapEntry = _CtFDDIMuxCapEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 3, 1, 1)
)
ctFDDIMuxCapEntry.setIndexNames(
    (0, "CTRON-FDDI-FNB-MIB", "ctFDDIMuxSlot"),
    (0, "CTRON-FDDI-FNB-MIB", "ctFDDIMuxConfig"),
)
if mibBuilder.loadTexts:
    ctFDDIMuxCapEntry.setStatus("mandatory")


class _CtFDDIMuxSlot_Type(Integer32):
    """Custom type ctFDDIMuxSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_CtFDDIMuxSlot_Type.__name__ = "Integer32"
_CtFDDIMuxSlot_Object = MibTableColumn
ctFDDIMuxSlot = _CtFDDIMuxSlot_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 3, 1, 1, 1),
    _CtFDDIMuxSlot_Type()
)
ctFDDIMuxSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctFDDIMuxSlot.setStatus("mandatory")
_CtFDDIMuxConfigID_Type = Integer32
_CtFDDIMuxConfigID_Object = MibTableColumn
ctFDDIMuxConfigID = _CtFDDIMuxConfigID_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 3, 1, 1, 2),
    _CtFDDIMuxConfigID_Type()
)
ctFDDIMuxConfigID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctFDDIMuxConfigID.setStatus("mandatory")
_CtFDDIMuxConfig_Type = DisplayString
_CtFDDIMuxConfig_Object = MibTableColumn
ctFDDIMuxConfig = _CtFDDIMuxConfig_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 3, 1, 1, 3),
    _CtFDDIMuxConfig_Type()
)
ctFDDIMuxConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctFDDIMuxConfig.setStatus("mandatory")
_CtFDDIMuxConfigDesc_Type = DisplayString
_CtFDDIMuxConfigDesc_Object = MibTableColumn
ctFDDIMuxConfigDesc = _CtFDDIMuxConfigDesc_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 3, 1, 1, 4),
    _CtFDDIMuxConfigDesc_Type()
)
ctFDDIMuxConfigDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctFDDIMuxConfigDesc.setStatus("mandatory")
_CtFDDIMuxCapEnableTable_Object = MibTable
ctFDDIMuxCapEnableTable = _CtFDDIMuxCapEnableTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 3, 2)
)
if mibBuilder.loadTexts:
    ctFDDIMuxCapEnableTable.setStatus("mandatory")
_CtFDDIMuxCapEnableEntry_Object = MibTableRow
ctFDDIMuxCapEnableEntry = _CtFDDIMuxCapEnableEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 3, 2, 1)
)
ctFDDIMuxCapEnableEntry.setIndexNames(
    (0, "CTRON-FDDI-FNB-MIB", "ctFDDIMuxEnableSlot"),
)
if mibBuilder.loadTexts:
    ctFDDIMuxCapEnableEntry.setStatus("mandatory")


class _CtFDDIMuxEnableSlot_Type(Integer32):
    """Custom type ctFDDIMuxEnableSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_CtFDDIMuxEnableSlot_Type.__name__ = "Integer32"
_CtFDDIMuxEnableSlot_Object = MibTableColumn
ctFDDIMuxEnableSlot = _CtFDDIMuxEnableSlot_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 3, 2, 1, 1),
    _CtFDDIMuxEnableSlot_Type()
)
ctFDDIMuxEnableSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctFDDIMuxEnableSlot.setStatus("mandatory")
_CtFDDIMuxCapEnable_Type = Integer32
_CtFDDIMuxCapEnable_Object = MibTableColumn
ctFDDIMuxCapEnable = _CtFDDIMuxCapEnable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 3, 2, 1, 2),
    _CtFDDIMuxCapEnable_Type()
)
ctFDDIMuxCapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctFDDIMuxCapEnable.setStatus("mandatory")
_CtFDDIMuxMasterPortAssignmentChange_Type = Counter32
_CtFDDIMuxMasterPortAssignmentChange_Object = MibTableColumn
ctFDDIMuxMasterPortAssignmentChange = _CtFDDIMuxMasterPortAssignmentChange_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 3, 2, 1, 3),
    _CtFDDIMuxMasterPortAssignmentChange_Type()
)
ctFDDIMuxMasterPortAssignmentChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctFDDIMuxMasterPortAssignmentChange.setStatus("mandatory")
_CtFDDIMuxOutTable_Object = MibTable
ctFDDIMuxOutTable = _CtFDDIMuxOutTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 3, 3)
)
if mibBuilder.loadTexts:
    ctFDDIMuxOutTable.setStatus("mandatory")
_CtFDDIMuxOutEntry_Object = MibTableRow
ctFDDIMuxOutEntry = _CtFDDIMuxOutEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 3, 3, 1)
)
ctFDDIMuxOutEntry.setIndexNames(
    (0, "CTRON-FDDI-FNB-MIB", "ctFDDIMuxOutSlot"),
    (0, "CTRON-FDDI-FNB-MIB", "ctFDDIMuxOutID"),
)
if mibBuilder.loadTexts:
    ctFDDIMuxOutEntry.setStatus("mandatory")


class _CtFDDIMuxOutSlot_Type(Integer32):
    """Custom type ctFDDIMuxOutSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_CtFDDIMuxOutSlot_Type.__name__ = "Integer32"
_CtFDDIMuxOutSlot_Object = MibTableColumn
ctFDDIMuxOutSlot = _CtFDDIMuxOutSlot_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 3, 3, 1, 1),
    _CtFDDIMuxOutSlot_Type()
)
ctFDDIMuxOutSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctFDDIMuxOutSlot.setStatus("mandatory")
_CtFDDIMuxOutID_Type = Integer32
_CtFDDIMuxOutID_Object = MibTableColumn
ctFDDIMuxOutID = _CtFDDIMuxOutID_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 3, 3, 1, 2),
    _CtFDDIMuxOutID_Type()
)
ctFDDIMuxOutID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctFDDIMuxOutID.setStatus("mandatory")


class _CtFDDIMuxOutMACIndex_Type(Integer32):
    """Custom type ctFDDIMuxOutMACIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CtFDDIMuxOutMACIndex_Type.__name__ = "Integer32"
_CtFDDIMuxOutMACIndex_Object = MibTableColumn
ctFDDIMuxOutMACIndex = _CtFDDIMuxOutMACIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 3, 3, 1, 3),
    _CtFDDIMuxOutMACIndex_Type()
)
ctFDDIMuxOutMACIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctFDDIMuxOutMACIndex.setStatus("mandatory")


class _CtFDDIMuxOutSMTIndex_Type(Integer32):
    """Custom type ctFDDIMuxOutSMTIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CtFDDIMuxOutSMTIndex_Type.__name__ = "Integer32"
_CtFDDIMuxOutSMTIndex_Object = MibTableColumn
ctFDDIMuxOutSMTIndex = _CtFDDIMuxOutSMTIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 3, 3, 1, 4),
    _CtFDDIMuxOutSMTIndex_Type()
)
ctFDDIMuxOutSMTIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctFDDIMuxOutSMTIndex.setStatus("mandatory")
_CtFDDIMuxBytes_Type = Integer32
_CtFDDIMuxBytes_Object = MibTableColumn
ctFDDIMuxBytes = _CtFDDIMuxBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 3, 3, 1, 5),
    _CtFDDIMuxBytes_Type()
)
ctFDDIMuxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctFDDIMuxBytes.setStatus("mandatory")
_CtFDDIMuxFrames_Type = Integer32
_CtFDDIMuxFrames_Object = MibTableColumn
ctFDDIMuxFrames = _CtFDDIMuxFrames_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 3, 3, 1, 6),
    _CtFDDIMuxFrames_Type()
)
ctFDDIMuxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctFDDIMuxFrames.setStatus("mandatory")
_CtFDDIMuxMasterPortTable_Object = MibTable
ctFDDIMuxMasterPortTable = _CtFDDIMuxMasterPortTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 3, 4)
)
if mibBuilder.loadTexts:
    ctFDDIMuxMasterPortTable.setStatus("mandatory")
_CtFDDIMuxMasterPortEntry_Object = MibTableRow
ctFDDIMuxMasterPortEntry = _CtFDDIMuxMasterPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 3, 4, 1)
)
ctFDDIMuxMasterPortEntry.setIndexNames(
    (0, "CTRON-FDDI-FNB-MIB", "ctFDDIMuxMasterPortSlotID"),
    (0, "CTRON-FDDI-FNB-MIB", "ctFDDIMuxMasterPortID"),
)
if mibBuilder.loadTexts:
    ctFDDIMuxMasterPortEntry.setStatus("mandatory")


class _CtFDDIMuxMasterPortSlotID_Type(Integer32):
    """Custom type ctFDDIMuxMasterPortSlotID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_CtFDDIMuxMasterPortSlotID_Type.__name__ = "Integer32"
_CtFDDIMuxMasterPortSlotID_Object = MibTableColumn
ctFDDIMuxMasterPortSlotID = _CtFDDIMuxMasterPortSlotID_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 3, 4, 1, 1),
    _CtFDDIMuxMasterPortSlotID_Type()
)
ctFDDIMuxMasterPortSlotID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctFDDIMuxMasterPortSlotID.setStatus("mandatory")


class _CtFDDIMuxMasterPortID_Type(Integer32):
    """Custom type ctFDDIMuxMasterPortID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CtFDDIMuxMasterPortID_Type.__name__ = "Integer32"
_CtFDDIMuxMasterPortID_Object = MibTableColumn
ctFDDIMuxMasterPortID = _CtFDDIMuxMasterPortID_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 3, 4, 1, 2),
    _CtFDDIMuxMasterPortID_Type()
)
ctFDDIMuxMasterPortID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctFDDIMuxMasterPortID.setStatus("mandatory")
_CtFDDIMuxMasterPortAssignment_Type = Integer32
_CtFDDIMuxMasterPortAssignment_Object = MibTableColumn
ctFDDIMuxMasterPortAssignment = _CtFDDIMuxMasterPortAssignment_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 3, 4, 1, 3),
    _CtFDDIMuxMasterPortAssignment_Type()
)
ctFDDIMuxMasterPortAssignment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctFDDIMuxMasterPortAssignment.setStatus("mandatory")


class _CtFDDIMuxMasterPortIndex_Type(Integer32):
    """Custom type ctFDDIMuxMasterPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CtFDDIMuxMasterPortIndex_Type.__name__ = "Integer32"
_CtFDDIMuxMasterPortIndex_Object = MibTableColumn
ctFDDIMuxMasterPortIndex = _CtFDDIMuxMasterPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 3, 4, 1, 4),
    _CtFDDIMuxMasterPortIndex_Type()
)
ctFDDIMuxMasterPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctFDDIMuxMasterPortIndex.setStatus("mandatory")
_CtFDDISerialConfig_ObjectIdentity = ObjectIdentity
ctFDDISerialConfig = _CtFDDISerialConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 4)
)


class _CtFDDINumbModules_Type(Integer32):
    """Custom type ctFDDINumbModules based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 14),
    )


_CtFDDINumbModules_Type.__name__ = "Integer32"
_CtFDDINumbModules_Object = MibScalar
ctFDDINumbModules = _CtFDDINumbModules_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 4, 1),
    _CtFDDINumbModules_Type()
)
ctFDDINumbModules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctFDDINumbModules.setStatus("mandatory")
_CtFDDISerialConfigTable_Object = MibTable
ctFDDISerialConfigTable = _CtFDDISerialConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 4, 2)
)
if mibBuilder.loadTexts:
    ctFDDISerialConfigTable.setStatus("mandatory")
_CtFDDISerialConfigEntry_Object = MibTableRow
ctFDDISerialConfigEntry = _CtFDDISerialConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 4, 2, 1)
)
ctFDDISerialConfigEntry.setIndexNames(
    (0, "CTRON-FDDI-FNB-MIB", "ctFDDISerialSlotID"),
)
if mibBuilder.loadTexts:
    ctFDDISerialConfigEntry.setStatus("mandatory")
_CtFDDISerialSlotID_Type = Integer32
_CtFDDISerialSlotID_Object = MibTableColumn
ctFDDISerialSlotID = _CtFDDISerialSlotID_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 4, 2, 1, 1),
    _CtFDDISerialSlotID_Type()
)
ctFDDISerialSlotID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctFDDISerialSlotID.setStatus("mandatory")


class _CtFDDISerialAdminStatus_Type(Integer32):
    """Custom type ctFDDISerialAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("bypass", 4),
          ("hwControl", 7),
          ("hwControlFNB1", 5),
          ("hwControlFNB2", 6),
          ("insertFNB1", 1),
          ("insertFNB1FNB2", 3),
          ("insertFNB2", 2))
    )


_CtFDDISerialAdminStatus_Type.__name__ = "Integer32"
_CtFDDISerialAdminStatus_Object = MibTableColumn
ctFDDISerialAdminStatus = _CtFDDISerialAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 4, 2, 1, 2),
    _CtFDDISerialAdminStatus_Type()
)
ctFDDISerialAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctFDDISerialAdminStatus.setStatus("mandatory")


class _CtFDDISerialOperStatus_Type(Integer32):
    """Custom type ctFDDISerialOperStatus based on Integer32"""
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
        *(("bypass", 4),
          ("insertFNB1", 1),
          ("insertFNB1FNB2", 3),
          ("insertFNB2", 2))
    )


_CtFDDISerialOperStatus_Type.__name__ = "Integer32"
_CtFDDISerialOperStatus_Object = MibTableColumn
ctFDDISerialOperStatus = _CtFDDISerialOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 4, 2, 1, 3),
    _CtFDDISerialOperStatus_Type()
)
ctFDDISerialOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctFDDISerialOperStatus.setStatus("mandatory")
_CtFDDIModuleFPIMTable_Object = MibTable
ctFDDIModuleFPIMTable = _CtFDDIModuleFPIMTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 4, 3)
)
if mibBuilder.loadTexts:
    ctFDDIModuleFPIMTable.setStatus("mandatory")
_CtFDDIModuleFPIMEntry_Object = MibTableRow
ctFDDIModuleFPIMEntry = _CtFDDIModuleFPIMEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 4, 3, 1)
)
ctFDDIModuleFPIMEntry.setIndexNames(
    (0, "CTRON-FDDI-FNB-MIB", "ctFddiFPIMSlotID"),
    (0, "CTRON-FDDI-FNB-MIB", "ctFddiFPIM"),
)
if mibBuilder.loadTexts:
    ctFDDIModuleFPIMEntry.setStatus("mandatory")
_CtFddiFPIMSlotID_Type = Integer32
_CtFddiFPIMSlotID_Object = MibTableColumn
ctFddiFPIMSlotID = _CtFddiFPIMSlotID_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 4, 3, 1, 1),
    _CtFddiFPIMSlotID_Type()
)
ctFddiFPIMSlotID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctFddiFPIMSlotID.setStatus("mandatory")
_CtFddiFPIM_Type = Integer32
_CtFddiFPIM_Object = MibTableColumn
ctFddiFPIM = _CtFddiFPIM_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 4, 3, 1, 2),
    _CtFddiFPIM_Type()
)
ctFddiFPIM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctFddiFPIM.setStatus("mandatory")


class _CtFddiFPIMStatus_Type(Integer32):
    """Custom type ctFddiFPIMStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("link", 1),
          ("noLink", 2),
          ("notSupported", 3))
    )


_CtFddiFPIMStatus_Type.__name__ = "Integer32"
_CtFddiFPIMStatus_Object = MibTableColumn
ctFddiFPIMStatus = _CtFddiFPIMStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 4, 3, 1, 4),
    _CtFddiFPIMStatus_Type()
)
ctFddiFPIMStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctFddiFPIMStatus.setStatus("mandatory")
_CtFddiFPIMType_Type = ObjectIdentifier
_CtFddiFPIMType_Object = MibTableColumn
ctFddiFPIMType = _CtFddiFPIMType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 4, 3, 1, 5),
    _CtFddiFPIMType_Type()
)
ctFddiFPIMType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctFddiFPIMType.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CTRON-FDDI-FNB-MIB",
    **{"ctFDDIResource": ctFDDIResource,
       "ctFDDIResourceTable": ctFDDIResourceTable,
       "ctFDDIResourceEntry": ctFDDIResourceEntry,
       "ctFDDIResourceSlotID": ctFDDIResourceSlotID,
       "ctFDDIResourceID": ctFDDIResourceID,
       "ctFDDIResourceType": ctFDDIResourceType,
       "ctFDDIResourceNumbInstance": ctFDDIResourceNumbInstance,
       "ctFDDINonMux": ctFDDINonMux,
       "ctFDDINonMuxCapTable": ctFDDINonMuxCapTable,
       "ctFDDINonMuxCapEntry": ctFDDINonMuxCapEntry,
       "ctFDDINMSlot": ctFDDINMSlot,
       "ctFDDINMConfigID": ctFDDINMConfigID,
       "ctFDDINMConfig": ctFDDINMConfig,
       "ctFDDINMConfigDesc": ctFDDINMConfigDesc,
       "ctFDDINonMuxCapEnableTable": ctFDDINonMuxCapEnableTable,
       "ctFDDINonMuxCapEnableEntry": ctFDDINonMuxCapEnableEntry,
       "ctFDDINMEnableSlot": ctFDDINMEnableSlot,
       "ctFDDINMCapEnable": ctFDDINMCapEnable,
       "ctFDDINonMuxConnectionTable": ctFDDINonMuxConnectionTable,
       "ctFDDINonMuxConnectionEntry": ctFDDINonMuxConnectionEntry,
       "ctFDDINMConnectionSlot": ctFDDINMConnectionSlot,
       "ctFDDINMConnectionID": ctFDDINMConnectionID,
       "ctFDDINMSMT": ctFDDINMSMT,
       "ctFDDINMMAC": ctFDDINMMAC,
       "ctFDDINMBytes": ctFDDINMBytes,
       "ctFDDINMFrames": ctFDDINMFrames,
       "ctFDDINonMuxInterfaceTable": ctFDDINonMuxInterfaceTable,
       "ctFDDINonMuxInterfaceEntry": ctFDDINonMuxInterfaceEntry,
       "ctFDDINMInterSlot": ctFDDINMInterSlot,
       "ctFDDINMNumbInterfaces": ctFDDINMNumbInterfaces,
       "ctFDDIMux": ctFDDIMux,
       "ctFDDIMuxCapTable": ctFDDIMuxCapTable,
       "ctFDDIMuxCapEntry": ctFDDIMuxCapEntry,
       "ctFDDIMuxSlot": ctFDDIMuxSlot,
       "ctFDDIMuxConfigID": ctFDDIMuxConfigID,
       "ctFDDIMuxConfig": ctFDDIMuxConfig,
       "ctFDDIMuxConfigDesc": ctFDDIMuxConfigDesc,
       "ctFDDIMuxCapEnableTable": ctFDDIMuxCapEnableTable,
       "ctFDDIMuxCapEnableEntry": ctFDDIMuxCapEnableEntry,
       "ctFDDIMuxEnableSlot": ctFDDIMuxEnableSlot,
       "ctFDDIMuxCapEnable": ctFDDIMuxCapEnable,
       "ctFDDIMuxMasterPortAssignmentChange": ctFDDIMuxMasterPortAssignmentChange,
       "ctFDDIMuxOutTable": ctFDDIMuxOutTable,
       "ctFDDIMuxOutEntry": ctFDDIMuxOutEntry,
       "ctFDDIMuxOutSlot": ctFDDIMuxOutSlot,
       "ctFDDIMuxOutID": ctFDDIMuxOutID,
       "ctFDDIMuxOutMACIndex": ctFDDIMuxOutMACIndex,
       "ctFDDIMuxOutSMTIndex": ctFDDIMuxOutSMTIndex,
       "ctFDDIMuxBytes": ctFDDIMuxBytes,
       "ctFDDIMuxFrames": ctFDDIMuxFrames,
       "ctFDDIMuxMasterPortTable": ctFDDIMuxMasterPortTable,
       "ctFDDIMuxMasterPortEntry": ctFDDIMuxMasterPortEntry,
       "ctFDDIMuxMasterPortSlotID": ctFDDIMuxMasterPortSlotID,
       "ctFDDIMuxMasterPortID": ctFDDIMuxMasterPortID,
       "ctFDDIMuxMasterPortAssignment": ctFDDIMuxMasterPortAssignment,
       "ctFDDIMuxMasterPortIndex": ctFDDIMuxMasterPortIndex,
       "ctFDDISerialConfig": ctFDDISerialConfig,
       "ctFDDINumbModules": ctFDDINumbModules,
       "ctFDDISerialConfigTable": ctFDDISerialConfigTable,
       "ctFDDISerialConfigEntry": ctFDDISerialConfigEntry,
       "ctFDDISerialSlotID": ctFDDISerialSlotID,
       "ctFDDISerialAdminStatus": ctFDDISerialAdminStatus,
       "ctFDDISerialOperStatus": ctFDDISerialOperStatus,
       "ctFDDIModuleFPIMTable": ctFDDIModuleFPIMTable,
       "ctFDDIModuleFPIMEntry": ctFDDIModuleFPIMEntry,
       "ctFddiFPIMSlotID": ctFddiFPIMSlotID,
       "ctFddiFPIM": ctFddiFPIM,
       "ctFddiFPIMStatus": ctFddiFPIMStatus,
       "ctFddiFPIMType": ctFddiFPIMType}
)
