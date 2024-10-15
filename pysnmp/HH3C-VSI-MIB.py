# SNMP MIB module (HH3C-VSI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-VSI-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:54:07 2024
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

(hh3cCommon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cCommon")

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

hh3cVsi = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 105)
)
hh3cVsi.setRevisions(
        ("2009-08-08 10:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cVsiObjects_ObjectIdentity = ObjectIdentity
hh3cVsiObjects = _Hh3cVsiObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 105, 1)
)
_Hh3cVsiScalarGroup_ObjectIdentity = ObjectIdentity
hh3cVsiScalarGroup = _Hh3cVsiScalarGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 105, 1, 1)
)
_Hh3cVsiNextAvailableVsiIndex_Type = Unsigned32
_Hh3cVsiNextAvailableVsiIndex_Object = MibScalar
hh3cVsiNextAvailableVsiIndex = _Hh3cVsiNextAvailableVsiIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 105, 1, 1, 1),
    _Hh3cVsiNextAvailableVsiIndex_Type()
)
hh3cVsiNextAvailableVsiIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cVsiNextAvailableVsiIndex.setStatus("current")
_Hh3cVsiTable_Object = MibTable
hh3cVsiTable = _Hh3cVsiTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 105, 1, 2)
)
if mibBuilder.loadTexts:
    hh3cVsiTable.setStatus("current")
_Hh3cVsiEntry_Object = MibTableRow
hh3cVsiEntry = _Hh3cVsiEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 105, 1, 2, 1)
)
hh3cVsiEntry.setIndexNames(
    (0, "HH3C-VSI-MIB", "hh3cVsiIndex"),
)
if mibBuilder.loadTexts:
    hh3cVsiEntry.setStatus("current")
_Hh3cVsiIndex_Type = Unsigned32
_Hh3cVsiIndex_Object = MibTableColumn
hh3cVsiIndex = _Hh3cVsiIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 105, 1, 2, 1, 1),
    _Hh3cVsiIndex_Type()
)
hh3cVsiIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cVsiIndex.setStatus("current")


class _Hh3cVsiName_Type(OctetString):
    """Custom type hh3cVsiName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_Hh3cVsiName_Type.__name__ = "OctetString"
_Hh3cVsiName_Object = MibTableColumn
hh3cVsiName = _Hh3cVsiName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 105, 1, 2, 1, 2),
    _Hh3cVsiName_Type()
)
hh3cVsiName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cVsiName.setStatus("current")


class _Hh3cVsiMode_Type(Integer32):
    """Custom type hh3cVsiMode based on Integer32"""
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


_Hh3cVsiMode_Type.__name__ = "Integer32"
_Hh3cVsiMode_Object = MibTableColumn
hh3cVsiMode = _Hh3cVsiMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 105, 1, 2, 1, 3),
    _Hh3cVsiMode_Type()
)
hh3cVsiMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cVsiMode.setStatus("current")
_Hh3cMinmIsid_Type = Integer32
_Hh3cMinmIsid_Object = MibTableColumn
hh3cMinmIsid = _Hh3cMinmIsid_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 105, 1, 2, 1, 4),
    _Hh3cMinmIsid_Type()
)
hh3cMinmIsid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMinmIsid.setStatus("current")
_Hh3cVsiId_Type = Unsigned32
_Hh3cVsiId_Object = MibTableColumn
hh3cVsiId = _Hh3cVsiId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 105, 1, 2, 1, 5),
    _Hh3cVsiId_Type()
)
hh3cVsiId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cVsiId.setStatus("current")


class _Hh3cVsiTransMode_Type(Integer32):
    """Custom type hh3cVsiTransMode based on Integer32"""
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


_Hh3cVsiTransMode_Type.__name__ = "Integer32"
_Hh3cVsiTransMode_Object = MibTableColumn
hh3cVsiTransMode = _Hh3cVsiTransMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 105, 1, 2, 1, 6),
    _Hh3cVsiTransMode_Type()
)
hh3cVsiTransMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cVsiTransMode.setStatus("current")


class _Hh3cVsiEnableHubSpoke_Type(Integer32):
    """Custom type hh3cVsiEnableHubSpoke based on Integer32"""
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


_Hh3cVsiEnableHubSpoke_Type.__name__ = "Integer32"
_Hh3cVsiEnableHubSpoke_Object = MibTableColumn
hh3cVsiEnableHubSpoke = _Hh3cVsiEnableHubSpoke_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 105, 1, 2, 1, 7),
    _Hh3cVsiEnableHubSpoke_Type()
)
hh3cVsiEnableHubSpoke.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cVsiEnableHubSpoke.setStatus("current")


class _Hh3cVsiAdminState_Type(Integer32):
    """Custom type hh3cVsiAdminState based on Integer32"""
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


_Hh3cVsiAdminState_Type.__name__ = "Integer32"
_Hh3cVsiAdminState_Object = MibTableColumn
hh3cVsiAdminState = _Hh3cVsiAdminState_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 105, 1, 2, 1, 8),
    _Hh3cVsiAdminState_Type()
)
hh3cVsiAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cVsiAdminState.setStatus("current")
_Hh3cVsiRowStatus_Type = RowStatus
_Hh3cVsiRowStatus_Object = MibTableColumn
hh3cVsiRowStatus = _Hh3cVsiRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 105, 1, 2, 1, 9),
    _Hh3cVsiRowStatus_Type()
)
hh3cVsiRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cVsiRowStatus.setStatus("current")
_Hh3cVsiXconnectTable_Object = MibTable
hh3cVsiXconnectTable = _Hh3cVsiXconnectTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 105, 1, 3)
)
if mibBuilder.loadTexts:
    hh3cVsiXconnectTable.setStatus("current")
_Hh3cVsiXconnectEntry_Object = MibTableRow
hh3cVsiXconnectEntry = _Hh3cVsiXconnectEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 105, 1, 3, 1)
)
hh3cVsiXconnectEntry.setIndexNames(
    (0, "HH3C-VSI-MIB", "hh3cVsiXconnectIfIndex"),
    (0, "HH3C-VSI-MIB", "hh3cVsiXconnectEvcSrvInstId"),
)
if mibBuilder.loadTexts:
    hh3cVsiXconnectEntry.setStatus("current")
_Hh3cVsiXconnectIfIndex_Type = Unsigned32
_Hh3cVsiXconnectIfIndex_Object = MibTableColumn
hh3cVsiXconnectIfIndex = _Hh3cVsiXconnectIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 105, 1, 3, 1, 1),
    _Hh3cVsiXconnectIfIndex_Type()
)
hh3cVsiXconnectIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cVsiXconnectIfIndex.setStatus("current")
_Hh3cVsiXconnectEvcSrvInstId_Type = Unsigned32
_Hh3cVsiXconnectEvcSrvInstId_Object = MibTableColumn
hh3cVsiXconnectEvcSrvInstId = _Hh3cVsiXconnectEvcSrvInstId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 105, 1, 3, 1, 2),
    _Hh3cVsiXconnectEvcSrvInstId_Type()
)
hh3cVsiXconnectEvcSrvInstId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cVsiXconnectEvcSrvInstId.setStatus("current")


class _Hh3cVsiXconnectVsiName_Type(OctetString):
    """Custom type hh3cVsiXconnectVsiName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_Hh3cVsiXconnectVsiName_Type.__name__ = "OctetString"
_Hh3cVsiXconnectVsiName_Object = MibTableColumn
hh3cVsiXconnectVsiName = _Hh3cVsiXconnectVsiName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 105, 1, 3, 1, 3),
    _Hh3cVsiXconnectVsiName_Type()
)
hh3cVsiXconnectVsiName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cVsiXconnectVsiName.setStatus("current")


class _Hh3cVsiXconnectAccessMode_Type(Integer32):
    """Custom type hh3cVsiXconnectAccessMode based on Integer32"""
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


_Hh3cVsiXconnectAccessMode_Type.__name__ = "Integer32"
_Hh3cVsiXconnectAccessMode_Object = MibTableColumn
hh3cVsiXconnectAccessMode = _Hh3cVsiXconnectAccessMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 105, 1, 3, 1, 4),
    _Hh3cVsiXconnectAccessMode_Type()
)
hh3cVsiXconnectAccessMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cVsiXconnectAccessMode.setStatus("current")


class _Hh3cVsiXconnectHubSpoke_Type(Integer32):
    """Custom type hh3cVsiXconnectHubSpoke based on Integer32"""
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


_Hh3cVsiXconnectHubSpoke_Type.__name__ = "Integer32"
_Hh3cVsiXconnectHubSpoke_Object = MibTableColumn
hh3cVsiXconnectHubSpoke = _Hh3cVsiXconnectHubSpoke_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 105, 1, 3, 1, 5),
    _Hh3cVsiXconnectHubSpoke_Type()
)
hh3cVsiXconnectHubSpoke.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cVsiXconnectHubSpoke.setStatus("current")
_Hh3cVsiXconnectRowStatus_Type = RowStatus
_Hh3cVsiXconnectRowStatus_Object = MibTableColumn
hh3cVsiXconnectRowStatus = _Hh3cVsiXconnectRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 105, 1, 3, 1, 6),
    _Hh3cVsiXconnectRowStatus_Type()
)
hh3cVsiXconnectRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cVsiXconnectRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-VSI-MIB",
    **{"hh3cVsi": hh3cVsi,
       "hh3cVsiObjects": hh3cVsiObjects,
       "hh3cVsiScalarGroup": hh3cVsiScalarGroup,
       "hh3cVsiNextAvailableVsiIndex": hh3cVsiNextAvailableVsiIndex,
       "hh3cVsiTable": hh3cVsiTable,
       "hh3cVsiEntry": hh3cVsiEntry,
       "hh3cVsiIndex": hh3cVsiIndex,
       "hh3cVsiName": hh3cVsiName,
       "hh3cVsiMode": hh3cVsiMode,
       "hh3cMinmIsid": hh3cMinmIsid,
       "hh3cVsiId": hh3cVsiId,
       "hh3cVsiTransMode": hh3cVsiTransMode,
       "hh3cVsiEnableHubSpoke": hh3cVsiEnableHubSpoke,
       "hh3cVsiAdminState": hh3cVsiAdminState,
       "hh3cVsiRowStatus": hh3cVsiRowStatus,
       "hh3cVsiXconnectTable": hh3cVsiXconnectTable,
       "hh3cVsiXconnectEntry": hh3cVsiXconnectEntry,
       "hh3cVsiXconnectIfIndex": hh3cVsiXconnectIfIndex,
       "hh3cVsiXconnectEvcSrvInstId": hh3cVsiXconnectEvcSrvInstId,
       "hh3cVsiXconnectVsiName": hh3cVsiXconnectVsiName,
       "hh3cVsiXconnectAccessMode": hh3cVsiXconnectAccessMode,
       "hh3cVsiXconnectHubSpoke": hh3cVsiXconnectHubSpoke,
       "hh3cVsiXconnectRowStatus": hh3cVsiXconnectRowStatus}
)
