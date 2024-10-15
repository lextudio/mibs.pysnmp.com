# SNMP MIB module (EVENT-ACTIONS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/EVENT-ACTIONS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:40:59 2024
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

(ctActions,) = mibBuilder.importSymbols(
    "CTRON-MIB-NAMES",
    "ctActions")

(eventIndex,) = mibBuilder.importSymbols(
    "RMON-MIB",
    "eventIndex")

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

_CtActionDefn_ObjectIdentity = ObjectIdentity
ctActionDefn = _CtActionDefn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 4, 1)
)
_CtEventActionTable_Object = MibTable
ctEventActionTable = _CtEventActionTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 4, 1, 1)
)
if mibBuilder.loadTexts:
    ctEventActionTable.setStatus("mandatory")
_CtEventActionEntry_Object = MibTableRow
ctEventActionEntry = _CtEventActionEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 4, 1, 1, 1)
)
ctEventActionEntry.setIndexNames(
    (0, "RMON-MIB", "eventIndex"),
    (0, "EVENT-ACTIONS-MIB", "ctActionObjectBase"),
)
if mibBuilder.loadTexts:
    ctEventActionEntry.setStatus("mandatory")
_CtActionObjectBase_Type = ObjectIdentifier
_CtActionObjectBase_Object = MibTableColumn
ctActionObjectBase = _CtActionObjectBase_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 4, 1, 1, 1, 1),
    _CtActionObjectBase_Type()
)
ctActionObjectBase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctActionObjectBase.setStatus("mandatory")
_CtActionValue_Type = Integer32
_CtActionValue_Object = MibTableColumn
ctActionValue = _CtActionValue_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 4, 1, 1, 1, 2),
    _CtActionValue_Type()
)
ctActionValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctActionValue.setStatus("mandatory")


class _CtActionOperStatus_Type(Integer32):
    """Custom type ctActionOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1),
          ("error", 5),
          ("invalidExtension", 6),
          ("normal", 4))
    )


_CtActionOperStatus_Type.__name__ = "Integer32"
_CtActionOperStatus_Object = MibTableColumn
ctActionOperStatus = _CtActionOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 4, 1, 1, 1, 3),
    _CtActionOperStatus_Type()
)
ctActionOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctActionOperStatus.setStatus("mandatory")


class _CtActionAdminStatus_Type(Integer32):
    """Custom type ctActionAdminStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("delete", 3),
          ("disable", 2),
          ("enable", 1))
    )


_CtActionAdminStatus_Type.__name__ = "Integer32"
_CtActionAdminStatus_Object = MibTableColumn
ctActionAdminStatus = _CtActionAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 4, 1, 1, 1, 4),
    _CtActionAdminStatus_Type()
)
ctActionAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctActionAdminStatus.setStatus("mandatory")


class _CtActionDescription_Type(DisplayString):
    """Custom type ctActionDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_CtActionDescription_Type.__name__ = "DisplayString"
_CtActionDescription_Object = MibTableColumn
ctActionDescription = _CtActionDescription_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 4, 1, 1, 1, 5),
    _CtActionDescription_Type()
)
ctActionDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctActionDescription.setStatus("mandatory")


class _CtActionOrder_Type(Integer32):
    """Custom type ctActionOrder based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CtActionOrder_Type.__name__ = "Integer32"
_CtActionOrder_Object = MibTableColumn
ctActionOrder = _CtActionOrder_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 4, 1, 1, 1, 6),
    _CtActionOrder_Type()
)
ctActionOrder.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctActionOrder.setStatus("mandatory")
_CtActionExtensionTable_Object = MibTable
ctActionExtensionTable = _CtActionExtensionTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 4, 1, 2)
)
if mibBuilder.loadTexts:
    ctActionExtensionTable.setStatus("deprecated")
_CtActionExtensionEntry_Object = MibTableRow
ctActionExtensionEntry = _CtActionExtensionEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 4, 1, 2, 1)
)
ctActionExtensionEntry.setIndexNames(
    (0, "EVENT-ACTIONS-MIB", "ctActionObjectBase"),
    (0, "EVENT-ACTIONS-MIB", "ctActionExtensionID"),
)
if mibBuilder.loadTexts:
    ctActionExtensionEntry.setStatus("deprecated")
_CtActionExtensionID_Type = Integer32
_CtActionExtensionID_Object = MibTableColumn
ctActionExtensionID = _CtActionExtensionID_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 4, 1, 2, 1, 1),
    _CtActionExtensionID_Type()
)
ctActionExtensionID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctActionExtensionID.setStatus("deprecated")
_CtActionExtensionOID_Type = ObjectIdentifier
_CtActionExtensionOID_Object = MibTableColumn
ctActionExtensionOID = _CtActionExtensionOID_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 4, 1, 2, 1, 2),
    _CtActionExtensionOID_Type()
)
ctActionExtensionOID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctActionExtensionOID.setStatus("deprecated")
_CtActionExtensionValue_Type = Integer32
_CtActionExtensionValue_Object = MibTableColumn
ctActionExtensionValue = _CtActionExtensionValue_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 4, 1, 2, 1, 3),
    _CtActionExtensionValue_Type()
)
ctActionExtensionValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctActionExtensionValue.setStatus("deprecated")


class _CtActionExtensionOperStatus_Type(Integer32):
    """Custom type ctActionExtensionOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1),
          ("error", 5),
          ("normal", 4))
    )


_CtActionExtensionOperStatus_Type.__name__ = "Integer32"
_CtActionExtensionOperStatus_Object = MibTableColumn
ctActionExtensionOperStatus = _CtActionExtensionOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 4, 1, 2, 1, 4),
    _CtActionExtensionOperStatus_Type()
)
ctActionExtensionOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctActionExtensionOperStatus.setStatus("deprecated")


class _CtActionExtensionAdminStatus_Type(Integer32):
    """Custom type ctActionExtensionAdminStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("delete", 3),
          ("disable", 2),
          ("enable", 1))
    )


_CtActionExtensionAdminStatus_Type.__name__ = "Integer32"
_CtActionExtensionAdminStatus_Object = MibTableColumn
ctActionExtensionAdminStatus = _CtActionExtensionAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 4, 1, 2, 1, 5),
    _CtActionExtensionAdminStatus_Type()
)
ctActionExtensionAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctActionExtensionAdminStatus.setStatus("deprecated")
_CtEventActionTableEntries_Type = Integer32
_CtEventActionTableEntries_Object = MibScalar
ctEventActionTableEntries = _CtEventActionTableEntries_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 4, 1, 3),
    _CtEventActionTableEntries_Type()
)
ctEventActionTableEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctEventActionTableEntries.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EVENT-ACTIONS-MIB",
    **{"ctActionDefn": ctActionDefn,
       "ctEventActionTable": ctEventActionTable,
       "ctEventActionEntry": ctEventActionEntry,
       "ctActionObjectBase": ctActionObjectBase,
       "ctActionValue": ctActionValue,
       "ctActionOperStatus": ctActionOperStatus,
       "ctActionAdminStatus": ctActionAdminStatus,
       "ctActionDescription": ctActionDescription,
       "ctActionOrder": ctActionOrder,
       "ctActionExtensionTable": ctActionExtensionTable,
       "ctActionExtensionEntry": ctActionExtensionEntry,
       "ctActionExtensionID": ctActionExtensionID,
       "ctActionExtensionOID": ctActionExtensionOID,
       "ctActionExtensionValue": ctActionExtensionValue,
       "ctActionExtensionOperStatus": ctActionExtensionOperStatus,
       "ctActionExtensionAdminStatus": ctActionExtensionAdminStatus,
       "ctEventActionTableEntries": ctEventActionTableEntries}
)
