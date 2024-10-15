# SNMP MIB module (SW-FDB-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SW-FDB-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:58:51 2024
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class MacAddress(OctetString):
    """Custom type MacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )





class PortList(OctetString):
    """Custom type PortList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Marconi_ObjectIdentity = ObjectIdentity
marconi = _Marconi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326)
)
_Systems_ObjectIdentity = ObjectIdentity
systems = _Systems_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2)
)
_External_ObjectIdentity = ObjectIdentity
external = _External_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20)
)
_Dlink_ObjectIdentity = ObjectIdentity
dlink = _Dlink_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1)
)
_Dlinkcommon_ObjectIdentity = ObjectIdentity
dlinkcommon = _Dlinkcommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 1)
)
_Golf_ObjectIdentity = ObjectIdentity
golf = _Golf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2)
)
_Golfproducts_ObjectIdentity = ObjectIdentity
golfproducts = _Golfproducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 1)
)
_Es2000_ObjectIdentity = ObjectIdentity
es2000 = _Es2000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 1, 3)
)
_Golfcommon_ObjectIdentity = ObjectIdentity
golfcommon = _Golfcommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2)
)
_Marconi_mgmt_ObjectIdentity = ObjectIdentity
marconi_mgmt = _Marconi_mgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2)
)
_Es2000Mgmt_ObjectIdentity = ObjectIdentity
es2000Mgmt = _Es2000Mgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28)
)
_SwL2Mgmt_ObjectIdentity = ObjectIdentity
swL2Mgmt = _SwL2Mgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2)
)
_SwFDB_ObjectIdentity = ObjectIdentity
swFDB = _SwFDB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 9)
)
_SwFdbStaticTable_Object = MibTable
swFdbStaticTable = _SwFdbStaticTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 9, 1)
)
if mibBuilder.loadTexts:
    swFdbStaticTable.setStatus("mandatory")
_SwFdbStaticEntry_Object = MibTableRow
swFdbStaticEntry = _SwFdbStaticEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 9, 1, 1)
)
swFdbStaticEntry.setIndexNames(
    (0, "SW-FDB-MIB", "swFdbStaticVid"),
    (0, "SW-FDB-MIB", "swFdbStaticAddress"),
)
if mibBuilder.loadTexts:
    swFdbStaticEntry.setStatus("mandatory")
_SwFdbStaticVid_Type = Integer32
_SwFdbStaticVid_Object = MibTableColumn
swFdbStaticVid = _SwFdbStaticVid_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 9, 1, 1, 1),
    _SwFdbStaticVid_Type()
)
swFdbStaticVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFdbStaticVid.setStatus("mandatory")
_SwFdbStaticAddress_Type = MacAddress
_SwFdbStaticAddress_Object = MibTableColumn
swFdbStaticAddress = _SwFdbStaticAddress_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 9, 1, 1, 2),
    _SwFdbStaticAddress_Type()
)
swFdbStaticAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFdbStaticAddress.setStatus("mandatory")
_SwFdbStaticPortMap_Type = PortList
_SwFdbStaticPortMap_Object = MibTableColumn
swFdbStaticPortMap = _SwFdbStaticPortMap_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 9, 1, 1, 3),
    _SwFdbStaticPortMap_Type()
)
swFdbStaticPortMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swFdbStaticPortMap.setStatus("mandatory")


class _SwFdbStaticState_Type(Integer32):
    """Custom type swFdbStaticState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("other", 1),
          ("valid", 3))
    )


_SwFdbStaticState_Type.__name__ = "Integer32"
_SwFdbStaticState_Object = MibTableColumn
swFdbStaticState = _SwFdbStaticState_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 9, 1, 1, 4),
    _SwFdbStaticState_Type()
)
swFdbStaticState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swFdbStaticState.setStatus("mandatory")


class _SwFdbStaticStatus_Type(Integer32):
    """Custom type swFdbStaticStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("apply", 2),
          ("not-apply", 3),
          ("other", 1))
    )


_SwFdbStaticStatus_Type.__name__ = "Integer32"
_SwFdbStaticStatus_Object = MibTableColumn
swFdbStaticStatus = _SwFdbStaticStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 9, 1, 1, 5),
    _SwFdbStaticStatus_Type()
)
swFdbStaticStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFdbStaticStatus.setStatus("mandatory")
_SwFdbStaticMemberTable_Object = MibTable
swFdbStaticMemberTable = _SwFdbStaticMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 9, 2)
)
if mibBuilder.loadTexts:
    swFdbStaticMemberTable.setStatus("mandatory")
_SwFdbStaticMemberEntry_Object = MibTableRow
swFdbStaticMemberEntry = _SwFdbStaticMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 9, 2, 1)
)
swFdbStaticMemberEntry.setIndexNames(
    (0, "SW-FDB-MIB", "swFdbStaticMemberVid"),
    (0, "SW-FDB-MIB", "swFdbStaticMemberAddress"),
    (0, "SW-FDB-MIB", "swFdbStaticMemberUnitIndex"),
    (0, "SW-FDB-MIB", "swFdbStaticMemberModuleIndex"),
    (0, "SW-FDB-MIB", "swFdbStaticMemberPortIndex"),
)
if mibBuilder.loadTexts:
    swFdbStaticMemberEntry.setStatus("mandatory")
_SwFdbStaticMemberVid_Type = Integer32
_SwFdbStaticMemberVid_Object = MibTableColumn
swFdbStaticMemberVid = _SwFdbStaticMemberVid_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 9, 2, 1, 1),
    _SwFdbStaticMemberVid_Type()
)
swFdbStaticMemberVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFdbStaticMemberVid.setStatus("mandatory")
_SwFdbStaticMemberAddress_Type = MacAddress
_SwFdbStaticMemberAddress_Object = MibTableColumn
swFdbStaticMemberAddress = _SwFdbStaticMemberAddress_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 9, 2, 1, 2),
    _SwFdbStaticMemberAddress_Type()
)
swFdbStaticMemberAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFdbStaticMemberAddress.setStatus("mandatory")
_SwFdbStaticMemberUnitIndex_Type = Integer32
_SwFdbStaticMemberUnitIndex_Object = MibTableColumn
swFdbStaticMemberUnitIndex = _SwFdbStaticMemberUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 9, 2, 1, 3),
    _SwFdbStaticMemberUnitIndex_Type()
)
swFdbStaticMemberUnitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFdbStaticMemberUnitIndex.setStatus("mandatory")
_SwFdbStaticMemberModuleIndex_Type = Integer32
_SwFdbStaticMemberModuleIndex_Object = MibTableColumn
swFdbStaticMemberModuleIndex = _SwFdbStaticMemberModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 9, 2, 1, 4),
    _SwFdbStaticMemberModuleIndex_Type()
)
swFdbStaticMemberModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFdbStaticMemberModuleIndex.setStatus("mandatory")
_SwFdbStaticMemberPortIndex_Type = Integer32
_SwFdbStaticMemberPortIndex_Object = MibTableColumn
swFdbStaticMemberPortIndex = _SwFdbStaticMemberPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 9, 2, 1, 5),
    _SwFdbStaticMemberPortIndex_Type()
)
swFdbStaticMemberPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFdbStaticMemberPortIndex.setStatus("mandatory")
_SwFdbFilterTable_Object = MibTable
swFdbFilterTable = _SwFdbFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 9, 3)
)
if mibBuilder.loadTexts:
    swFdbFilterTable.setStatus("mandatory")
_SwFdbFilterEntry_Object = MibTableRow
swFdbFilterEntry = _SwFdbFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 9, 3, 1)
)
swFdbFilterEntry.setIndexNames(
    (0, "SW-FDB-MIB", "swFdbFilterVid"),
    (0, "SW-FDB-MIB", "swFdbFilterAddress"),
)
if mibBuilder.loadTexts:
    swFdbFilterEntry.setStatus("mandatory")
_SwFdbFilterVid_Type = Integer32
_SwFdbFilterVid_Object = MibTableColumn
swFdbFilterVid = _SwFdbFilterVid_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 9, 3, 1, 1),
    _SwFdbFilterVid_Type()
)
swFdbFilterVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFdbFilterVid.setStatus("mandatory")
_SwFdbFilterAddress_Type = MacAddress
_SwFdbFilterAddress_Object = MibTableColumn
swFdbFilterAddress = _SwFdbFilterAddress_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 9, 3, 1, 2),
    _SwFdbFilterAddress_Type()
)
swFdbFilterAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFdbFilterAddress.setStatus("mandatory")


class _SwFdbFilterState_Type(Integer32):
    """Custom type swFdbFilterState based on Integer32"""
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
        *(("dst-src-addr", 4),
          ("invalid", 2),
          ("other", 1),
          ("valid", 3))
    )


_SwFdbFilterState_Type.__name__ = "Integer32"
_SwFdbFilterState_Object = MibTableColumn
swFdbFilterState = _SwFdbFilterState_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 9, 3, 1, 3),
    _SwFdbFilterState_Type()
)
swFdbFilterState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swFdbFilterState.setStatus("mandatory")
_EndOfMIB_Type = Integer32
_EndOfMIB_Object = MibScalar
endOfMIB = _EndOfMIB_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 9999),
    _EndOfMIB_Type()
)
endOfMIB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endOfMIB.setStatus("optional")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SW-FDB-MIB",
    **{"MacAddress": MacAddress,
       "PortList": PortList,
       "marconi": marconi,
       "systems": systems,
       "external": external,
       "dlink": dlink,
       "dlinkcommon": dlinkcommon,
       "golf": golf,
       "golfproducts": golfproducts,
       "es2000": es2000,
       "golfcommon": golfcommon,
       "marconi-mgmt": marconi_mgmt,
       "es2000Mgmt": es2000Mgmt,
       "swL2Mgmt": swL2Mgmt,
       "swFDB": swFDB,
       "swFdbStaticTable": swFdbStaticTable,
       "swFdbStaticEntry": swFdbStaticEntry,
       "swFdbStaticVid": swFdbStaticVid,
       "swFdbStaticAddress": swFdbStaticAddress,
       "swFdbStaticPortMap": swFdbStaticPortMap,
       "swFdbStaticState": swFdbStaticState,
       "swFdbStaticStatus": swFdbStaticStatus,
       "swFdbStaticMemberTable": swFdbStaticMemberTable,
       "swFdbStaticMemberEntry": swFdbStaticMemberEntry,
       "swFdbStaticMemberVid": swFdbStaticMemberVid,
       "swFdbStaticMemberAddress": swFdbStaticMemberAddress,
       "swFdbStaticMemberUnitIndex": swFdbStaticMemberUnitIndex,
       "swFdbStaticMemberModuleIndex": swFdbStaticMemberModuleIndex,
       "swFdbStaticMemberPortIndex": swFdbStaticMemberPortIndex,
       "swFdbFilterTable": swFdbFilterTable,
       "swFdbFilterEntry": swFdbFilterEntry,
       "swFdbFilterVid": swFdbFilterVid,
       "swFdbFilterAddress": swFdbFilterAddress,
       "swFdbFilterState": swFdbFilterState,
       "endOfMIB": endOfMIB}
)
