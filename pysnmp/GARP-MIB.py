# SNMP MIB module (GARP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/GARP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:47:41 2024
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
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Cabletron_ObjectIdentity = ObjectIdentity
cabletron = _Cabletron_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52)
)
_Mibs_ObjectIdentity = ObjectIdentity
mibs = _Mibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4)
)
_CtronExp_ObjectIdentity = ObjectIdentity
ctronExp = _CtronExp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2)
)
_CtVLANMib_ObjectIdentity = ObjectIdentity
ctVLANMib = _CtVLANMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12)
)
_CtVLANMgr_ObjectIdentity = ObjectIdentity
ctVLANMgr = _CtVLANMgr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1)
)
_CtGarp_ObjectIdentity = ObjectIdentity
ctGarp = _CtGarp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 3)
)
_CtGarpTables_ObjectIdentity = ObjectIdentity
ctGarpTables = _CtGarpTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 3, 2)
)
_GarpApplicationTable_Object = MibTable
garpApplicationTable = _GarpApplicationTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 3, 2, 1)
)
if mibBuilder.loadTexts:
    garpApplicationTable.setStatus("mandatory")
_GarpApplicationEntry_Object = MibTableRow
garpApplicationEntry = _GarpApplicationEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 3, 2, 1, 1)
)
garpApplicationEntry.setIndexNames(
    (0, "GARP-MIB", "garpApplicationAppType"),
)
if mibBuilder.loadTexts:
    garpApplicationEntry.setStatus("mandatory")
_GarpApplicationAppType_Type = Integer32
_GarpApplicationAppType_Object = MibTableColumn
garpApplicationAppType = _GarpApplicationAppType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 3, 2, 1, 1, 1),
    _GarpApplicationAppType_Type()
)
garpApplicationAppType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    garpApplicationAppType.setStatus("mandatory")
_GarpApplicationName_Type = PhysAddress
_GarpApplicationName_Object = MibTableColumn
garpApplicationName = _GarpApplicationName_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 3, 2, 1, 1, 2),
    _GarpApplicationName_Type()
)
garpApplicationName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    garpApplicationName.setStatus("mandatory")
_GarpApplicationFailedRegistrations_Type = Integer32
_GarpApplicationFailedRegistrations_Object = MibTableColumn
garpApplicationFailedRegistrations = _GarpApplicationFailedRegistrations_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 3, 2, 1, 1, 3),
    _GarpApplicationFailedRegistrations_Type()
)
garpApplicationFailedRegistrations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    garpApplicationFailedRegistrations.setStatus("mandatory")
_GarpApplicationOperationStatus_Type = Integer32
_GarpApplicationOperationStatus_Object = MibTableColumn
garpApplicationOperationStatus = _GarpApplicationOperationStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 3, 2, 1, 1, 4),
    _GarpApplicationOperationStatus_Type()
)
garpApplicationOperationStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    garpApplicationOperationStatus.setStatus("mandatory")
_GarpPortOperationTable_Object = MibTable
garpPortOperationTable = _GarpPortOperationTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 3, 2, 2)
)
if mibBuilder.loadTexts:
    garpPortOperationTable.setStatus("mandatory")
_GarpPortOperationEntry_Object = MibTableRow
garpPortOperationEntry = _GarpPortOperationEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 3, 2, 2, 1)
)
garpPortOperationEntry.setIndexNames(
    (0, "GARP-MIB", "garpPortOperationAppType"),
    (0, "GARP-MIB", "garpPortOperationPort"),
)
if mibBuilder.loadTexts:
    garpPortOperationEntry.setStatus("mandatory")
_GarpPortOperationAppType_Type = Integer32
_GarpPortOperationAppType_Object = MibTableColumn
garpPortOperationAppType = _GarpPortOperationAppType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 3, 2, 2, 1, 1),
    _GarpPortOperationAppType_Type()
)
garpPortOperationAppType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    garpPortOperationAppType.setStatus("mandatory")
_GarpPortOperationPort_Type = DisplayString
_GarpPortOperationPort_Object = MibTableColumn
garpPortOperationPort = _GarpPortOperationPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 3, 2, 2, 1, 2),
    _GarpPortOperationPort_Type()
)
garpPortOperationPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    garpPortOperationPort.setStatus("mandatory")
_GarpPortOperationStatus_Type = Integer32
_GarpPortOperationStatus_Object = MibTableColumn
garpPortOperationStatus = _GarpPortOperationStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 3, 2, 2, 1, 3),
    _GarpPortOperationStatus_Type()
)
garpPortOperationStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    garpPortOperationStatus.setStatus("mandatory")
_GarpTimerTable_Object = MibTable
garpTimerTable = _GarpTimerTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 3, 2, 3)
)
if mibBuilder.loadTexts:
    garpTimerTable.setStatus("mandatory")
_GarpTimerEntry_Object = MibTableRow
garpTimerEntry = _GarpTimerEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 3, 2, 3, 1)
)
garpTimerEntry.setIndexNames(
    (0, "GARP-MIB", "garpTimerAttributeAppType"),
    (0, "GARP-MIB", "garpTimerAttributePort"),
)
if mibBuilder.loadTexts:
    garpTimerEntry.setStatus("mandatory")
_GarpTimerAttributeAppType_Type = Integer32
_GarpTimerAttributeAppType_Object = MibTableColumn
garpTimerAttributeAppType = _GarpTimerAttributeAppType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 3, 2, 3, 1, 1),
    _GarpTimerAttributeAppType_Type()
)
garpTimerAttributeAppType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    garpTimerAttributeAppType.setStatus("mandatory")
_GarpTimerAttributePort_Type = Integer32
_GarpTimerAttributePort_Object = MibTableColumn
garpTimerAttributePort = _GarpTimerAttributePort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 3, 2, 3, 1, 2),
    _GarpTimerAttributePort_Type()
)
garpTimerAttributePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    garpTimerAttributePort.setStatus("mandatory")
_GarpTimerAttributeJoin_Type = Integer32
_GarpTimerAttributeJoin_Object = MibTableColumn
garpTimerAttributeJoin = _GarpTimerAttributeJoin_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 3, 2, 3, 1, 3),
    _GarpTimerAttributeJoin_Type()
)
garpTimerAttributeJoin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    garpTimerAttributeJoin.setStatus("mandatory")
_GarpTimerAttributeLeave_Type = Integer32
_GarpTimerAttributeLeave_Object = MibTableColumn
garpTimerAttributeLeave = _GarpTimerAttributeLeave_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 3, 2, 3, 1, 4),
    _GarpTimerAttributeLeave_Type()
)
garpTimerAttributeLeave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    garpTimerAttributeLeave.setStatus("mandatory")
_GarpTimerAttributeLeaveAll_Type = Integer32
_GarpTimerAttributeLeaveAll_Object = MibTableColumn
garpTimerAttributeLeaveAll = _GarpTimerAttributeLeaveAll_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 3, 2, 3, 1, 5),
    _GarpTimerAttributeLeaveAll_Type()
)
garpTimerAttributeLeaveAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    garpTimerAttributeLeaveAll.setStatus("mandatory")
_GarpAttributeTable_Object = MibTable
garpAttributeTable = _GarpAttributeTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 3, 2, 4)
)
if mibBuilder.loadTexts:
    garpAttributeTable.setStatus("mandatory")
_GarpAttributeEntry_Object = MibTableRow
garpAttributeEntry = _GarpAttributeEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 3, 2, 4, 1)
)
garpAttributeEntry.setIndexNames(
    (0, "GARP-MIB", "garpAttributeAppType"),
    (0, "GARP-MIB", "garpAttributePort"),
    (0, "GARP-MIB", "garpAttributeValue"),
    (0, "GARP-MIB", "garpAttributeGIPContextID"),
)
if mibBuilder.loadTexts:
    garpAttributeEntry.setStatus("mandatory")
_GarpAttributeAppType_Type = Integer32
_GarpAttributeAppType_Object = MibTableColumn
garpAttributeAppType = _GarpAttributeAppType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 3, 2, 4, 1, 1),
    _GarpAttributeAppType_Type()
)
garpAttributeAppType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    garpAttributeAppType.setStatus("mandatory")
_GarpAttributePort_Type = Integer32
_GarpAttributePort_Object = MibTableColumn
garpAttributePort = _GarpAttributePort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 3, 2, 4, 1, 2),
    _GarpAttributePort_Type()
)
garpAttributePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    garpAttributePort.setStatus("mandatory")
_GarpAttributeValue_Type = OctetString
_GarpAttributeValue_Object = MibTableColumn
garpAttributeValue = _GarpAttributeValue_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 3, 2, 4, 1, 3),
    _GarpAttributeValue_Type()
)
garpAttributeValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    garpAttributeValue.setStatus("mandatory")
_GarpAttributeGIPContextID_Type = Integer32
_GarpAttributeGIPContextID_Object = MibTableColumn
garpAttributeGIPContextID = _GarpAttributeGIPContextID_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 3, 2, 4, 1, 4),
    _GarpAttributeGIPContextID_Type()
)
garpAttributeGIPContextID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    garpAttributeGIPContextID.setStatus("mandatory")
_GarpAttributeType_Type = Integer32
_GarpAttributeType_Object = MibTableColumn
garpAttributeType = _GarpAttributeType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 3, 2, 4, 1, 5),
    _GarpAttributeType_Type()
)
garpAttributeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    garpAttributeType.setStatus("mandatory")


class _GarpAttributeProtoAdminCtrl_Type(Integer32):
    """Custom type garpAttributeProtoAdminCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("non-Participan", 1),
          ("normal-Participan", 0))
    )


_GarpAttributeProtoAdminCtrl_Type.__name__ = "Integer32"
_GarpAttributeProtoAdminCtrl_Object = MibTableColumn
garpAttributeProtoAdminCtrl = _GarpAttributeProtoAdminCtrl_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 3, 2, 4, 1, 6),
    _GarpAttributeProtoAdminCtrl_Type()
)
garpAttributeProtoAdminCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    garpAttributeProtoAdminCtrl.setStatus("mandatory")


class _GarpAttributeRegisControl_Type(Integer32):
    """Custom type garpAttributeRegisControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("garpRegistrarFixed", 1),
          ("garpRegistrarForbidden", 2),
          ("garpRegistrarNormal", 0))
    )


_GarpAttributeRegisControl_Type.__name__ = "Integer32"
_GarpAttributeRegisControl_Object = MibTableColumn
garpAttributeRegisControl = _GarpAttributeRegisControl_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 3, 2, 4, 1, 7),
    _GarpAttributeRegisControl_Type()
)
garpAttributeRegisControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    garpAttributeRegisControl.setStatus("mandatory")


class _GarpAttributeStateValue_Type(Integer32):
    """Custom type garpAttributeStateValue based on Integer32"""
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
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23)
        )
    )
    namedValues = NamedValues(
        *(("aa-in", 11),
          ("aa-lv", 10),
          ("aa-mt", 9),
          ("ao-in", 13),
          ("ap-in", 12),
          ("la-in", 23),
          ("la-lv", 20),
          ("la-mt", 19),
          ("lo-lv", 22),
          ("lo-mt", 21),
          ("qa-in", 16),
          ("qa-lv", 15),
          ("qa-mt", 14),
          ("qo-in", 18),
          ("qp-in", 17),
          ("va-in", 6),
          ("va-lv", 1),
          ("va-mt", 0),
          ("vo-in", 8),
          ("vo-lv", 5),
          ("vo-mt", 4),
          ("vp-in", 7),
          ("vp-lv", 3),
          ("vp-mt", 2))
    )


_GarpAttributeStateValue_Type.__name__ = "Integer32"
_GarpAttributeStateValue_Object = MibTableColumn
garpAttributeStateValue = _GarpAttributeStateValue_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 3, 2, 4, 1, 8),
    _GarpAttributeStateValue_Type()
)
garpAttributeStateValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    garpAttributeStateValue.setStatus("mandatory")
_GarpAttributeOrigOfLastPDU_Type = PhysAddress
_GarpAttributeOrigOfLastPDU_Object = MibTableColumn
garpAttributeOrigOfLastPDU = _GarpAttributeOrigOfLastPDU_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 3, 2, 4, 1, 9),
    _GarpAttributeOrigOfLastPDU_Type()
)
garpAttributeOrigOfLastPDU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    garpAttributeOrigOfLastPDU.setStatus("optional")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "GARP-MIB",
    **{"cabletron": cabletron,
       "mibs": mibs,
       "ctronExp": ctronExp,
       "ctVLANMib": ctVLANMib,
       "ctVLANMgr": ctVLANMgr,
       "ctGarp": ctGarp,
       "ctGarpTables": ctGarpTables,
       "garpApplicationTable": garpApplicationTable,
       "garpApplicationEntry": garpApplicationEntry,
       "garpApplicationAppType": garpApplicationAppType,
       "garpApplicationName": garpApplicationName,
       "garpApplicationFailedRegistrations": garpApplicationFailedRegistrations,
       "garpApplicationOperationStatus": garpApplicationOperationStatus,
       "garpPortOperationTable": garpPortOperationTable,
       "garpPortOperationEntry": garpPortOperationEntry,
       "garpPortOperationAppType": garpPortOperationAppType,
       "garpPortOperationPort": garpPortOperationPort,
       "garpPortOperationStatus": garpPortOperationStatus,
       "garpTimerTable": garpTimerTable,
       "garpTimerEntry": garpTimerEntry,
       "garpTimerAttributeAppType": garpTimerAttributeAppType,
       "garpTimerAttributePort": garpTimerAttributePort,
       "garpTimerAttributeJoin": garpTimerAttributeJoin,
       "garpTimerAttributeLeave": garpTimerAttributeLeave,
       "garpTimerAttributeLeaveAll": garpTimerAttributeLeaveAll,
       "garpAttributeTable": garpAttributeTable,
       "garpAttributeEntry": garpAttributeEntry,
       "garpAttributeAppType": garpAttributeAppType,
       "garpAttributePort": garpAttributePort,
       "garpAttributeValue": garpAttributeValue,
       "garpAttributeGIPContextID": garpAttributeGIPContextID,
       "garpAttributeType": garpAttributeType,
       "garpAttributeProtoAdminCtrl": garpAttributeProtoAdminCtrl,
       "garpAttributeRegisControl": garpAttributeRegisControl,
       "garpAttributeStateValue": garpAttributeStateValue,
       "garpAttributeOrigOfLastPDU": garpAttributeOrigOfLastPDU}
)
