# SNMP MIB module (SW-TRUNK-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SW-TRUNK-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:58:58 2024
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



class TrunkSetList(OctetString):
    """Custom type TrunkSetList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
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
_SwPortTrunk_ObjectIdentity = ObjectIdentity
swPortTrunk = _SwPortTrunk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 6)
)
_SwPortTrunkCtrlTable_Object = MibTable
swPortTrunkCtrlTable = _SwPortTrunkCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 6, 1)
)
if mibBuilder.loadTexts:
    swPortTrunkCtrlTable.setStatus("mandatory")
_SwPortTrunkCtrlEntry_Object = MibTableRow
swPortTrunkCtrlEntry = _SwPortTrunkCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 6, 1, 1)
)
swPortTrunkCtrlEntry.setIndexNames(
    (0, "SW-TRUNK-MIB", "swPortTrunkCtrlIndex"),
)
if mibBuilder.loadTexts:
    swPortTrunkCtrlEntry.setStatus("mandatory")
_SwPortTrunkCtrlIndex_Type = Integer32
_SwPortTrunkCtrlIndex_Object = MibTableColumn
swPortTrunkCtrlIndex = _SwPortTrunkCtrlIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 6, 1, 1, 1),
    _SwPortTrunkCtrlIndex_Type()
)
swPortTrunkCtrlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortTrunkCtrlIndex.setStatus("mandatory")
_SwPortTrunkCtrlAnchorPort_Type = Integer32
_SwPortTrunkCtrlAnchorPort_Object = MibTableColumn
swPortTrunkCtrlAnchorPort = _SwPortTrunkCtrlAnchorPort_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 6, 1, 1, 2),
    _SwPortTrunkCtrlAnchorPort_Type()
)
swPortTrunkCtrlAnchorPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPortTrunkCtrlAnchorPort.setStatus("mandatory")
_SwPortTrunkCtrlMasterPort_Type = Integer32
_SwPortTrunkCtrlMasterPort_Object = MibTableColumn
swPortTrunkCtrlMasterPort = _SwPortTrunkCtrlMasterPort_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 6, 1, 1, 3),
    _SwPortTrunkCtrlMasterPort_Type()
)
swPortTrunkCtrlMasterPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortTrunkCtrlMasterPort.setStatus("mandatory")


class _SwPortTrunkCtrlName_Type(DisplayString):
    """Custom type swPortTrunkCtrlName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SwPortTrunkCtrlName_Type.__name__ = "DisplayString"
_SwPortTrunkCtrlName_Object = MibTableColumn
swPortTrunkCtrlName = _SwPortTrunkCtrlName_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 6, 1, 1, 4),
    _SwPortTrunkCtrlName_Type()
)
swPortTrunkCtrlName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPortTrunkCtrlName.setStatus("mandatory")
_SwPortTrunkCtrlMember_Type = TrunkSetList
_SwPortTrunkCtrlMember_Object = MibTableColumn
swPortTrunkCtrlMember = _SwPortTrunkCtrlMember_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 6, 1, 1, 5),
    _SwPortTrunkCtrlMember_Type()
)
swPortTrunkCtrlMember.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPortTrunkCtrlMember.setStatus("mandatory")


class _SwPortTrunkCtrlState_Type(Integer32):
    """Custom type swPortTrunkCtrlState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_SwPortTrunkCtrlState_Type.__name__ = "Integer32"
_SwPortTrunkCtrlState_Object = MibTableColumn
swPortTrunkCtrlState = _SwPortTrunkCtrlState_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 6, 1, 1, 6),
    _SwPortTrunkCtrlState_Type()
)
swPortTrunkCtrlState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPortTrunkCtrlState.setStatus("mandatory")
_SwPortTrunkMemberTable_Object = MibTable
swPortTrunkMemberTable = _SwPortTrunkMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 6, 2)
)
if mibBuilder.loadTexts:
    swPortTrunkMemberTable.setStatus("mandatory")
_SwPortTrunkMemberEntry_Object = MibTableRow
swPortTrunkMemberEntry = _SwPortTrunkMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 6, 2, 1)
)
swPortTrunkMemberEntry.setIndexNames(
    (0, "SW-TRUNK-MIB", "swPortTrunkMemberIndex"),
    (0, "SW-TRUNK-MIB", "swPortTrunkMemberUnitIndex"),
    (0, "SW-TRUNK-MIB", "swPortTrunkMemberModuleIndex"),
    (0, "SW-TRUNK-MIB", "swPortTrunkMemberPortIndex"),
)
if mibBuilder.loadTexts:
    swPortTrunkMemberEntry.setStatus("mandatory")
_SwPortTrunkMemberIndex_Type = Integer32
_SwPortTrunkMemberIndex_Object = MibTableColumn
swPortTrunkMemberIndex = _SwPortTrunkMemberIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 6, 2, 1, 1),
    _SwPortTrunkMemberIndex_Type()
)
swPortTrunkMemberIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortTrunkMemberIndex.setStatus("mandatory")
_SwPortTrunkMemberUnitIndex_Type = Integer32
_SwPortTrunkMemberUnitIndex_Object = MibTableColumn
swPortTrunkMemberUnitIndex = _SwPortTrunkMemberUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 6, 2, 1, 2),
    _SwPortTrunkMemberUnitIndex_Type()
)
swPortTrunkMemberUnitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortTrunkMemberUnitIndex.setStatus("mandatory")
_SwPortTrunkMemberModuleIndex_Type = Integer32
_SwPortTrunkMemberModuleIndex_Object = MibTableColumn
swPortTrunkMemberModuleIndex = _SwPortTrunkMemberModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 6, 2, 1, 3),
    _SwPortTrunkMemberModuleIndex_Type()
)
swPortTrunkMemberModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortTrunkMemberModuleIndex.setStatus("mandatory")
_SwPortTrunkMemberPortIndex_Type = Integer32
_SwPortTrunkMemberPortIndex_Object = MibTableColumn
swPortTrunkMemberPortIndex = _SwPortTrunkMemberPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 6, 2, 1, 4),
    _SwPortTrunkMemberPortIndex_Type()
)
swPortTrunkMemberPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortTrunkMemberPortIndex.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SW-TRUNK-MIB",
    **{"TrunkSetList": TrunkSetList,
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
       "swPortTrunk": swPortTrunk,
       "swPortTrunkCtrlTable": swPortTrunkCtrlTable,
       "swPortTrunkCtrlEntry": swPortTrunkCtrlEntry,
       "swPortTrunkCtrlIndex": swPortTrunkCtrlIndex,
       "swPortTrunkCtrlAnchorPort": swPortTrunkCtrlAnchorPort,
       "swPortTrunkCtrlMasterPort": swPortTrunkCtrlMasterPort,
       "swPortTrunkCtrlName": swPortTrunkCtrlName,
       "swPortTrunkCtrlMember": swPortTrunkCtrlMember,
       "swPortTrunkCtrlState": swPortTrunkCtrlState,
       "swPortTrunkMemberTable": swPortTrunkMemberTable,
       "swPortTrunkMemberEntry": swPortTrunkMemberEntry,
       "swPortTrunkMemberIndex": swPortTrunkMemberIndex,
       "swPortTrunkMemberUnitIndex": swPortTrunkMemberUnitIndex,
       "swPortTrunkMemberModuleIndex": swPortTrunkMemberModuleIndex,
       "swPortTrunkMemberPortIndex": swPortTrunkMemberPortIndex}
)
