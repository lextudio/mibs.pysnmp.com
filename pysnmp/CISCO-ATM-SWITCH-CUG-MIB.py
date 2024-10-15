# SNMP MIB module (CISCO-ATM-SWITCH-CUG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-ATM-SWITCH-CUG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:56:01 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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

csCugMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 89)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CsCugInterlockCode(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(24, 24),
    )



class Unsigned32(Gauge32, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_CsCugMIBObjects_ObjectIdentity = ObjectIdentity
csCugMIBObjects = _CsCugMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 89, 1)
)
_CsCugInterlockCodeTable_Object = MibTable
csCugInterlockCodeTable = _CsCugInterlockCodeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 89, 1, 1)
)
if mibBuilder.loadTexts:
    csCugInterlockCodeTable.setStatus("current")
_CsCugInterlockCodeEntry_Object = MibTableRow
csCugInterlockCodeEntry = _CsCugInterlockCodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 89, 1, 1, 1)
)
csCugInterlockCodeEntry.setIndexNames(
    (0, "CISCO-ATM-SWITCH-CUG-MIB", "csCugInterlockCode"),
)
if mibBuilder.loadTexts:
    csCugInterlockCodeEntry.setStatus("current")
_CsCugInterlockCode_Type = CsCugInterlockCode
_CsCugInterlockCode_Object = MibTableColumn
csCugInterlockCode = _CsCugInterlockCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 89, 1, 1, 1, 1),
    _CsCugInterlockCode_Type()
)
csCugInterlockCode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    csCugInterlockCode.setStatus("current")


class _CsCugInterlockCodeAliasName_Type(DisplayString):
    """Custom type csCugInterlockCodeAliasName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 30),
    )


_CsCugInterlockCodeAliasName_Type.__name__ = "DisplayString"
_CsCugInterlockCodeAliasName_Object = MibTableColumn
csCugInterlockCodeAliasName = _CsCugInterlockCodeAliasName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 89, 1, 1, 1, 2),
    _CsCugInterlockCodeAliasName_Type()
)
csCugInterlockCodeAliasName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    csCugInterlockCodeAliasName.setStatus("current")
_CsCugInterlockCodeRowStatus_Type = RowStatus
_CsCugInterlockCodeRowStatus_Object = MibTableColumn
csCugInterlockCodeRowStatus = _CsCugInterlockCodeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 89, 1, 1, 1, 3),
    _CsCugInterlockCodeRowStatus_Type()
)
csCugInterlockCodeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    csCugInterlockCodeRowStatus.setStatus("current")
_CsCugIfTable_Object = MibTable
csCugIfTable = _CsCugIfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 89, 1, 2)
)
if mibBuilder.loadTexts:
    csCugIfTable.setStatus("current")
_CsCugIfEntry_Object = MibTableRow
csCugIfEntry = _CsCugIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 89, 1, 2, 1)
)
csCugIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    csCugIfEntry.setStatus("current")


class _CsCugIfAccessEnable_Type(TruthValue):
    """Custom type csCugIfAccessEnable based on TruthValue"""


_CsCugIfAccessEnable_Object = MibTableColumn
csCugIfAccessEnable = _CsCugIfAccessEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 89, 1, 2, 1, 1),
    _CsCugIfAccessEnable_Type()
)
csCugIfAccessEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    csCugIfAccessEnable.setStatus("current")


class _CsCugIfPermitUnknownCugsToUser_Type(TruthValue):
    """Custom type csCugIfPermitUnknownCugsToUser based on TruthValue"""


_CsCugIfPermitUnknownCugsToUser_Object = MibTableColumn
csCugIfPermitUnknownCugsToUser = _CsCugIfPermitUnknownCugsToUser_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 89, 1, 2, 1, 2),
    _CsCugIfPermitUnknownCugsToUser_Type()
)
csCugIfPermitUnknownCugsToUser.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    csCugIfPermitUnknownCugsToUser.setStatus("current")


class _CsCugIfPermitUnknownCugsFromUser_Type(Integer32):
    """Custom type csCugIfPermitUnknownCugsFromUser based on Integer32"""
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
        *(("deny", 1),
          ("permitPerCall", 2),
          ("permitPermanently", 3))
    )


_CsCugIfPermitUnknownCugsFromUser_Type.__name__ = "Integer32"
_CsCugIfPermitUnknownCugsFromUser_Object = MibTableColumn
csCugIfPermitUnknownCugsFromUser = _CsCugIfPermitUnknownCugsFromUser_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 89, 1, 2, 1, 3),
    _CsCugIfPermitUnknownCugsFromUser_Type()
)
csCugIfPermitUnknownCugsFromUser.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    csCugIfPermitUnknownCugsFromUser.setStatus("current")
_CsCugIfRowStatus_Type = RowStatus
_CsCugIfRowStatus_Object = MibTableColumn
csCugIfRowStatus = _CsCugIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 89, 1, 2, 1, 4),
    _CsCugIfRowStatus_Type()
)
csCugIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    csCugIfRowStatus.setStatus("current")
_CsCugTable_Object = MibTable
csCugTable = _CsCugTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 89, 1, 3)
)
if mibBuilder.loadTexts:
    csCugTable.setStatus("current")
_CsCugEntry_Object = MibTableRow
csCugEntry = _CsCugEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 89, 1, 3, 1)
)
csCugEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-ATM-SWITCH-CUG-MIB", "csCugInterlockCode"),
)
if mibBuilder.loadTexts:
    csCugEntry.setStatus("current")


class _CsCugIndex_Type(Unsigned32):
    """Custom type csCugIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CsCugIndex_Type.__name__ = "Unsigned32"
_CsCugIndex_Object = MibTableColumn
csCugIndex = _CsCugIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 89, 1, 3, 1, 1),
    _CsCugIndex_Type()
)
csCugIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    csCugIndex.setStatus("current")


class _CsCugPreferential_Type(TruthValue):
    """Custom type csCugPreferential based on TruthValue"""


_CsCugPreferential_Object = MibTableColumn
csCugPreferential = _CsCugPreferential_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 89, 1, 3, 1, 2),
    _CsCugPreferential_Type()
)
csCugPreferential.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    csCugPreferential.setStatus("current")


class _CsCugDenySameGroupToUser_Type(TruthValue):
    """Custom type csCugDenySameGroupToUser based on TruthValue"""


_CsCugDenySameGroupToUser_Object = MibTableColumn
csCugDenySameGroupToUser = _CsCugDenySameGroupToUser_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 89, 1, 3, 1, 3),
    _CsCugDenySameGroupToUser_Type()
)
csCugDenySameGroupToUser.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    csCugDenySameGroupToUser.setStatus("current")


class _CsCugDenySameGroupFromUser_Type(TruthValue):
    """Custom type csCugDenySameGroupFromUser based on TruthValue"""


_CsCugDenySameGroupFromUser_Object = MibTableColumn
csCugDenySameGroupFromUser = _CsCugDenySameGroupFromUser_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 89, 1, 3, 1, 4),
    _CsCugDenySameGroupFromUser_Type()
)
csCugDenySameGroupFromUser.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    csCugDenySameGroupFromUser.setStatus("current")
_CsCugRowStatus_Type = RowStatus
_CsCugRowStatus_Object = MibTableColumn
csCugRowStatus = _CsCugRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 89, 1, 3, 1, 5),
    _CsCugRowStatus_Type()
)
csCugRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    csCugRowStatus.setStatus("current")
_CsCugMIBConformance_ObjectIdentity = ObjectIdentity
csCugMIBConformance = _CsCugMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 89, 3)
)
_CsCugMIBCompliances_ObjectIdentity = ObjectIdentity
csCugMIBCompliances = _CsCugMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 89, 3, 1)
)
_CsCugMIBGroups_ObjectIdentity = ObjectIdentity
csCugMIBGroups = _CsCugMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 89, 3, 2)
)

# Managed Objects groups

csCugMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 89, 3, 2, 1)
)
csCugMIBGroup.setObjects(
      *(("CISCO-ATM-SWITCH-CUG-MIB", "csCugInterlockCodeAliasName"),
        ("CISCO-ATM-SWITCH-CUG-MIB", "csCugInterlockCodeRowStatus"),
        ("CISCO-ATM-SWITCH-CUG-MIB", "csCugIfAccessEnable"),
        ("CISCO-ATM-SWITCH-CUG-MIB", "csCugIfPermitUnknownCugsToUser"),
        ("CISCO-ATM-SWITCH-CUG-MIB", "csCugIfPermitUnknownCugsFromUser"),
        ("CISCO-ATM-SWITCH-CUG-MIB", "csCugIfRowStatus"),
        ("CISCO-ATM-SWITCH-CUG-MIB", "csCugIndex"),
        ("CISCO-ATM-SWITCH-CUG-MIB", "csCugPreferential"),
        ("CISCO-ATM-SWITCH-CUG-MIB", "csCugDenySameGroupToUser"),
        ("CISCO-ATM-SWITCH-CUG-MIB", "csCugDenySameGroupFromUser"),
        ("CISCO-ATM-SWITCH-CUG-MIB", "csCugRowStatus"))
)
if mibBuilder.loadTexts:
    csCugMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

csCugMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 89, 3, 1, 1)
)
if mibBuilder.loadTexts:
    csCugMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-ATM-SWITCH-CUG-MIB",
    **{"CsCugInterlockCode": CsCugInterlockCode,
       "Unsigned32": Unsigned32,
       "csCugMIB": csCugMIB,
       "csCugMIBObjects": csCugMIBObjects,
       "csCugInterlockCodeTable": csCugInterlockCodeTable,
       "csCugInterlockCodeEntry": csCugInterlockCodeEntry,
       "csCugInterlockCode": csCugInterlockCode,
       "csCugInterlockCodeAliasName": csCugInterlockCodeAliasName,
       "csCugInterlockCodeRowStatus": csCugInterlockCodeRowStatus,
       "csCugIfTable": csCugIfTable,
       "csCugIfEntry": csCugIfEntry,
       "csCugIfAccessEnable": csCugIfAccessEnable,
       "csCugIfPermitUnknownCugsToUser": csCugIfPermitUnknownCugsToUser,
       "csCugIfPermitUnknownCugsFromUser": csCugIfPermitUnknownCugsFromUser,
       "csCugIfRowStatus": csCugIfRowStatus,
       "csCugTable": csCugTable,
       "csCugEntry": csCugEntry,
       "csCugIndex": csCugIndex,
       "csCugPreferential": csCugPreferential,
       "csCugDenySameGroupToUser": csCugDenySameGroupToUser,
       "csCugDenySameGroupFromUser": csCugDenySameGroupFromUser,
       "csCugRowStatus": csCugRowStatus,
       "csCugMIBConformance": csCugMIBConformance,
       "csCugMIBCompliances": csCugMIBCompliances,
       "csCugMIBCompliance": csCugMIBCompliance,
       "csCugMIBGroups": csCugMIBGroups,
       "csCugMIBGroup": csCugMIBGroup}
)
