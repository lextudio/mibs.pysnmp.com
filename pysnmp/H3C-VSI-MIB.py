# SNMP MIB module (H3C-VSI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/H3C-VSI-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:50:56 2024
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

(h3cCommon,) = mibBuilder.importSymbols(
    "HUAWEI-3COM-OID-MIB",
    "h3cCommon")

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

h3cVsi = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 105)
)
h3cVsi.setRevisions(
        ("2009-08-08 10:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_H3cVsiObjects_ObjectIdentity = ObjectIdentity
h3cVsiObjects = _H3cVsiObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 105, 1)
)
_H3cVsiScalarGroup_ObjectIdentity = ObjectIdentity
h3cVsiScalarGroup = _H3cVsiScalarGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 105, 1, 1)
)
_H3cVsiNextAvailableVsiIndex_Type = Unsigned32
_H3cVsiNextAvailableVsiIndex_Object = MibScalar
h3cVsiNextAvailableVsiIndex = _H3cVsiNextAvailableVsiIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 105, 1, 1, 1),
    _H3cVsiNextAvailableVsiIndex_Type()
)
h3cVsiNextAvailableVsiIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVsiNextAvailableVsiIndex.setStatus("current")
_H3cVsiTable_Object = MibTable
h3cVsiTable = _H3cVsiTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 105, 1, 2)
)
if mibBuilder.loadTexts:
    h3cVsiTable.setStatus("current")
_H3cVsiEntry_Object = MibTableRow
h3cVsiEntry = _H3cVsiEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 105, 1, 2, 1)
)
h3cVsiEntry.setIndexNames(
    (0, "H3C-VSI-MIB", "h3cVsiIndex"),
)
if mibBuilder.loadTexts:
    h3cVsiEntry.setStatus("current")
_H3cVsiIndex_Type = Unsigned32
_H3cVsiIndex_Object = MibTableColumn
h3cVsiIndex = _H3cVsiIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 105, 1, 2, 1, 1),
    _H3cVsiIndex_Type()
)
h3cVsiIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cVsiIndex.setStatus("current")


class _H3cVsiName_Type(OctetString):
    """Custom type h3cVsiName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_H3cVsiName_Type.__name__ = "OctetString"
_H3cVsiName_Object = MibTableColumn
h3cVsiName = _H3cVsiName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 105, 1, 2, 1, 2),
    _H3cVsiName_Type()
)
h3cVsiName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cVsiName.setStatus("current")


class _H3cVsiMode_Type(Integer32):
    """Custom type h3cVsiMode based on Integer32"""
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
        *(("kompella", 4),
          ("kompellaAndMinm", 5),
          ("martini", 1),
          ("martiniAndMinm", 3),
          ("minm", 2))
    )


_H3cVsiMode_Type.__name__ = "Integer32"
_H3cVsiMode_Object = MibTableColumn
h3cVsiMode = _H3cVsiMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 105, 1, 2, 1, 3),
    _H3cVsiMode_Type()
)
h3cVsiMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cVsiMode.setStatus("current")
_H3cMinmIsid_Type = Integer32
_H3cMinmIsid_Object = MibTableColumn
h3cMinmIsid = _H3cMinmIsid_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 105, 1, 2, 1, 4),
    _H3cMinmIsid_Type()
)
h3cMinmIsid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cMinmIsid.setStatus("current")
_H3cVsiId_Type = Unsigned32
_H3cVsiId_Object = MibTableColumn
h3cVsiId = _H3cVsiId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 105, 1, 2, 1, 5),
    _H3cVsiId_Type()
)
h3cVsiId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cVsiId.setStatus("current")


class _H3cVsiTransMode_Type(Integer32):
    """Custom type h3cVsiTransMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ethernet", 2),
          ("vlan", 1))
    )


_H3cVsiTransMode_Type.__name__ = "Integer32"
_H3cVsiTransMode_Object = MibTableColumn
h3cVsiTransMode = _H3cVsiTransMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 105, 1, 2, 1, 6),
    _H3cVsiTransMode_Type()
)
h3cVsiTransMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cVsiTransMode.setStatus("current")


class _H3cVsiEnableHubSpoke_Type(Integer32):
    """Custom type h3cVsiEnableHubSpoke based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_H3cVsiEnableHubSpoke_Type.__name__ = "Integer32"
_H3cVsiEnableHubSpoke_Object = MibTableColumn
h3cVsiEnableHubSpoke = _H3cVsiEnableHubSpoke_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 105, 1, 2, 1, 7),
    _H3cVsiEnableHubSpoke_Type()
)
h3cVsiEnableHubSpoke.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cVsiEnableHubSpoke.setStatus("current")


class _H3cVsiAdminState_Type(Integer32):
    """Custom type h3cVsiAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("adminDown", 2),
          ("adminUp", 1))
    )


_H3cVsiAdminState_Type.__name__ = "Integer32"
_H3cVsiAdminState_Object = MibTableColumn
h3cVsiAdminState = _H3cVsiAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 105, 1, 2, 1, 8),
    _H3cVsiAdminState_Type()
)
h3cVsiAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cVsiAdminState.setStatus("current")
_H3cVsiRowStatus_Type = RowStatus
_H3cVsiRowStatus_Object = MibTableColumn
h3cVsiRowStatus = _H3cVsiRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 105, 1, 2, 1, 9),
    _H3cVsiRowStatus_Type()
)
h3cVsiRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cVsiRowStatus.setStatus("current")
_H3cVsiXconnectTable_Object = MibTable
h3cVsiXconnectTable = _H3cVsiXconnectTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 105, 1, 3)
)
if mibBuilder.loadTexts:
    h3cVsiXconnectTable.setStatus("current")
_H3cVsiXconnectEntry_Object = MibTableRow
h3cVsiXconnectEntry = _H3cVsiXconnectEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 105, 1, 3, 1)
)
h3cVsiXconnectEntry.setIndexNames(
    (0, "H3C-VSI-MIB", "h3cVsiXconnectIfIndex"),
    (0, "H3C-VSI-MIB", "h3cVsiXconnectEvcSrvInstId"),
)
if mibBuilder.loadTexts:
    h3cVsiXconnectEntry.setStatus("current")
_H3cVsiXconnectIfIndex_Type = Unsigned32
_H3cVsiXconnectIfIndex_Object = MibTableColumn
h3cVsiXconnectIfIndex = _H3cVsiXconnectIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 105, 1, 3, 1, 1),
    _H3cVsiXconnectIfIndex_Type()
)
h3cVsiXconnectIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cVsiXconnectIfIndex.setStatus("current")
_H3cVsiXconnectEvcSrvInstId_Type = Unsigned32
_H3cVsiXconnectEvcSrvInstId_Object = MibTableColumn
h3cVsiXconnectEvcSrvInstId = _H3cVsiXconnectEvcSrvInstId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 105, 1, 3, 1, 2),
    _H3cVsiXconnectEvcSrvInstId_Type()
)
h3cVsiXconnectEvcSrvInstId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cVsiXconnectEvcSrvInstId.setStatus("current")


class _H3cVsiXconnectVsiName_Type(OctetString):
    """Custom type h3cVsiXconnectVsiName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_H3cVsiXconnectVsiName_Type.__name__ = "OctetString"
_H3cVsiXconnectVsiName_Object = MibTableColumn
h3cVsiXconnectVsiName = _H3cVsiXconnectVsiName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 105, 1, 3, 1, 3),
    _H3cVsiXconnectVsiName_Type()
)
h3cVsiXconnectVsiName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cVsiXconnectVsiName.setStatus("current")


class _H3cVsiXconnectAccessMode_Type(Integer32):
    """Custom type h3cVsiXconnectAccessMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ethernet", 2),
          ("vlan", 1))
    )


_H3cVsiXconnectAccessMode_Type.__name__ = "Integer32"
_H3cVsiXconnectAccessMode_Object = MibTableColumn
h3cVsiXconnectAccessMode = _H3cVsiXconnectAccessMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 105, 1, 3, 1, 4),
    _H3cVsiXconnectAccessMode_Type()
)
h3cVsiXconnectAccessMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cVsiXconnectAccessMode.setStatus("current")


class _H3cVsiXconnectHubSpoke_Type(Integer32):
    """Custom type h3cVsiXconnectHubSpoke based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hub", 2),
          ("none", 1),
          ("spoke", 3))
    )


_H3cVsiXconnectHubSpoke_Type.__name__ = "Integer32"
_H3cVsiXconnectHubSpoke_Object = MibTableColumn
h3cVsiXconnectHubSpoke = _H3cVsiXconnectHubSpoke_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 105, 1, 3, 1, 5),
    _H3cVsiXconnectHubSpoke_Type()
)
h3cVsiXconnectHubSpoke.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cVsiXconnectHubSpoke.setStatus("current")
_H3cVsiXconnectRowStatus_Type = RowStatus
_H3cVsiXconnectRowStatus_Object = MibTableColumn
h3cVsiXconnectRowStatus = _H3cVsiXconnectRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 105, 1, 3, 1, 6),
    _H3cVsiXconnectRowStatus_Type()
)
h3cVsiXconnectRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cVsiXconnectRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "H3C-VSI-MIB",
    **{"h3cVsi": h3cVsi,
       "h3cVsiObjects": h3cVsiObjects,
       "h3cVsiScalarGroup": h3cVsiScalarGroup,
       "h3cVsiNextAvailableVsiIndex": h3cVsiNextAvailableVsiIndex,
       "h3cVsiTable": h3cVsiTable,
       "h3cVsiEntry": h3cVsiEntry,
       "h3cVsiIndex": h3cVsiIndex,
       "h3cVsiName": h3cVsiName,
       "h3cVsiMode": h3cVsiMode,
       "h3cMinmIsid": h3cMinmIsid,
       "h3cVsiId": h3cVsiId,
       "h3cVsiTransMode": h3cVsiTransMode,
       "h3cVsiEnableHubSpoke": h3cVsiEnableHubSpoke,
       "h3cVsiAdminState": h3cVsiAdminState,
       "h3cVsiRowStatus": h3cVsiRowStatus,
       "h3cVsiXconnectTable": h3cVsiXconnectTable,
       "h3cVsiXconnectEntry": h3cVsiXconnectEntry,
       "h3cVsiXconnectIfIndex": h3cVsiXconnectIfIndex,
       "h3cVsiXconnectEvcSrvInstId": h3cVsiXconnectEvcSrvInstId,
       "h3cVsiXconnectVsiName": h3cVsiXconnectVsiName,
       "h3cVsiXconnectAccessMode": h3cVsiXconnectAccessMode,
       "h3cVsiXconnectHubSpoke": h3cVsiXconnectHubSpoke,
       "h3cVsiXconnectRowStatus": h3cVsiXconnectRowStatus}
)
