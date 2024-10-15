# SNMP MIB module (HH3C-MPM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-MPM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:54:15 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(DisplayString,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

hh3cMpm = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 51)
)
hh3cMpm.setRevisions(
        ("2005-03-22 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class EnabledStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )



# MIB Managed Objects in the order of their OIDs

_Hh3cMPMObject_ObjectIdentity = ObjectIdentity
hh3cMPMObject = _Hh3cMPMObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 51, 1)
)
_Hh3cMPortGroupLimitMinNumber_Type = Unsigned32
_Hh3cMPortGroupLimitMinNumber_Object = MibScalar
hh3cMPortGroupLimitMinNumber = _Hh3cMPortGroupLimitMinNumber_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 51, 1, 1),
    _Hh3cMPortGroupLimitMinNumber_Type()
)
hh3cMPortGroupLimitMinNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMPortGroupLimitMinNumber.setStatus("current")
_Hh3cMPortGroupLimitMaxNumber_Type = Unsigned32
_Hh3cMPortGroupLimitMaxNumber_Object = MibScalar
hh3cMPortGroupLimitMaxNumber = _Hh3cMPortGroupLimitMaxNumber_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 51, 1, 2),
    _Hh3cMPortGroupLimitMaxNumber_Type()
)
hh3cMPortGroupLimitMaxNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMPortGroupLimitMaxNumber.setStatus("current")
_Hh3cMPMTable_ObjectIdentity = ObjectIdentity
hh3cMPMTable = _Hh3cMPMTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 51, 2)
)
_Hh3cMPortGroupJoinTable_Object = MibTable
hh3cMPortGroupJoinTable = _Hh3cMPortGroupJoinTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 51, 2, 1)
)
if mibBuilder.loadTexts:
    hh3cMPortGroupJoinTable.setStatus("current")
_Hh3cMPortGroupJoinEntry_Object = MibTableRow
hh3cMPortGroupJoinEntry = _Hh3cMPortGroupJoinEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 51, 2, 1, 1)
)
hh3cMPortGroupJoinEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HH3C-MPM-MIB", "hh3cMPortGroupJoinVlanID"),
    (0, "HH3C-MPM-MIB", "hh3cMPortGroupJoinAddressType"),
    (0, "HH3C-MPM-MIB", "hh3cMPortGroupJoinAddress"),
)
if mibBuilder.loadTexts:
    hh3cMPortGroupJoinEntry.setStatus("current")
_Hh3cMPortGroupJoinVlanID_Type = Integer32
_Hh3cMPortGroupJoinVlanID_Object = MibTableColumn
hh3cMPortGroupJoinVlanID = _Hh3cMPortGroupJoinVlanID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 51, 2, 1, 1, 1),
    _Hh3cMPortGroupJoinVlanID_Type()
)
hh3cMPortGroupJoinVlanID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cMPortGroupJoinVlanID.setStatus("current")
_Hh3cMPortGroupJoinAddressType_Type = InetAddressType
_Hh3cMPortGroupJoinAddressType_Object = MibTableColumn
hh3cMPortGroupJoinAddressType = _Hh3cMPortGroupJoinAddressType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 51, 2, 1, 1, 2),
    _Hh3cMPortGroupJoinAddressType_Type()
)
hh3cMPortGroupJoinAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cMPortGroupJoinAddressType.setStatus("current")
_Hh3cMPortGroupJoinAddress_Type = InetAddress
_Hh3cMPortGroupJoinAddress_Object = MibTableColumn
hh3cMPortGroupJoinAddress = _Hh3cMPortGroupJoinAddress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 51, 2, 1, 1, 3),
    _Hh3cMPortGroupJoinAddress_Type()
)
hh3cMPortGroupJoinAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cMPortGroupJoinAddress.setStatus("current")
_Hh3cMPortGroupJoinStatus_Type = RowStatus
_Hh3cMPortGroupJoinStatus_Object = MibTableColumn
hh3cMPortGroupJoinStatus = _Hh3cMPortGroupJoinStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 51, 2, 1, 1, 4),
    _Hh3cMPortGroupJoinStatus_Type()
)
hh3cMPortGroupJoinStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMPortGroupJoinStatus.setStatus("current")
_Hh3cMPortGroupTable_Object = MibTable
hh3cMPortGroupTable = _Hh3cMPortGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 51, 2, 2)
)
if mibBuilder.loadTexts:
    hh3cMPortGroupTable.setStatus("current")
_Hh3cMPortGroupEntry_Object = MibTableRow
hh3cMPortGroupEntry = _Hh3cMPortGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 51, 2, 2, 1)
)
hh3cMPortGroupEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HH3C-MPM-MIB", "hh3cMPortGroupVlanID"),
    (0, "HH3C-MPM-MIB", "hh3cMPortGroupAddressType"),
    (0, "HH3C-MPM-MIB", "hh3cMPortGroupAddress"),
)
if mibBuilder.loadTexts:
    hh3cMPortGroupEntry.setStatus("current")
_Hh3cMPortGroupVlanID_Type = Integer32
_Hh3cMPortGroupVlanID_Object = MibTableColumn
hh3cMPortGroupVlanID = _Hh3cMPortGroupVlanID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 51, 2, 2, 1, 1),
    _Hh3cMPortGroupVlanID_Type()
)
hh3cMPortGroupVlanID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cMPortGroupVlanID.setStatus("current")
_Hh3cMPortGroupAddressType_Type = InetAddressType
_Hh3cMPortGroupAddressType_Object = MibTableColumn
hh3cMPortGroupAddressType = _Hh3cMPortGroupAddressType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 51, 2, 2, 1, 2),
    _Hh3cMPortGroupAddressType_Type()
)
hh3cMPortGroupAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMPortGroupAddressType.setStatus("current")
_Hh3cMPortGroupAddress_Type = InetAddress
_Hh3cMPortGroupAddress_Object = MibTableColumn
hh3cMPortGroupAddress = _Hh3cMPortGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 51, 2, 2, 1, 3),
    _Hh3cMPortGroupAddress_Type()
)
hh3cMPortGroupAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMPortGroupAddress.setStatus("current")
_Hh3cMPortConfigTable_Object = MibTable
hh3cMPortConfigTable = _Hh3cMPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 51, 2, 3)
)
if mibBuilder.loadTexts:
    hh3cMPortConfigTable.setStatus("current")
_Hh3cMPortConfigEntry_Object = MibTableRow
hh3cMPortConfigEntry = _Hh3cMPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 51, 2, 3, 1)
)
hh3cMPortConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HH3C-MPM-MIB", "hh3cMPortConfigVlanID"),
)
if mibBuilder.loadTexts:
    hh3cMPortConfigEntry.setStatus("current")
_Hh3cMPortConfigVlanID_Type = Integer32
_Hh3cMPortConfigVlanID_Object = MibTableColumn
hh3cMPortConfigVlanID = _Hh3cMPortConfigVlanID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 51, 2, 3, 1, 1),
    _Hh3cMPortConfigVlanID_Type()
)
hh3cMPortConfigVlanID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cMPortConfigVlanID.setStatus("current")
_Hh3cMPortGroupLimitNumber_Type = Unsigned32
_Hh3cMPortGroupLimitNumber_Object = MibTableColumn
hh3cMPortGroupLimitNumber = _Hh3cMPortGroupLimitNumber_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 51, 2, 3, 1, 2),
    _Hh3cMPortGroupLimitNumber_Type()
)
hh3cMPortGroupLimitNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMPortGroupLimitNumber.setStatus("current")


class _Hh3cMPortFastLeaveStatus_Type(EnabledStatus):
    """Custom type hh3cMPortFastLeaveStatus based on EnabledStatus"""
    defaultValue = 2


_Hh3cMPortFastLeaveStatus_Object = MibTableColumn
hh3cMPortFastLeaveStatus = _Hh3cMPortFastLeaveStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 51, 2, 3, 1, 3),
    _Hh3cMPortFastLeaveStatus_Type()
)
hh3cMPortFastLeaveStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMPortFastLeaveStatus.setStatus("current")


class _Hh3cMPortGroupPolicyParameter_Type(Integer32):
    """Custom type hh3cMPortGroupPolicyParameter based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2000, 2999),
    )


_Hh3cMPortGroupPolicyParameter_Type.__name__ = "Integer32"
_Hh3cMPortGroupPolicyParameter_Object = MibTableColumn
hh3cMPortGroupPolicyParameter = _Hh3cMPortGroupPolicyParameter_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 51, 2, 3, 1, 4),
    _Hh3cMPortGroupPolicyParameter_Type()
)
hh3cMPortGroupPolicyParameter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMPortGroupPolicyParameter.setStatus("current")
_Hh3cMPortConfigRowStatus_Type = RowStatus
_Hh3cMPortConfigRowStatus_Object = MibTableColumn
hh3cMPortConfigRowStatus = _Hh3cMPortConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 51, 2, 3, 1, 5),
    _Hh3cMPortConfigRowStatus_Type()
)
hh3cMPortConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMPortConfigRowStatus.setStatus("current")


class _Hh3cMPortGroupLimitReplace_Type(EnabledStatus):
    """Custom type hh3cMPortGroupLimitReplace based on EnabledStatus"""


_Hh3cMPortGroupLimitReplace_Object = MibTableColumn
hh3cMPortGroupLimitReplace = _Hh3cMPortGroupLimitReplace_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 51, 2, 3, 1, 6),
    _Hh3cMPortGroupLimitReplace_Type()
)
hh3cMPortGroupLimitReplace.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMPortGroupLimitReplace.setStatus("current")
_Hh3cHostStaticJoinTable_Object = MibTable
hh3cHostStaticJoinTable = _Hh3cHostStaticJoinTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 51, 2, 4)
)
if mibBuilder.loadTexts:
    hh3cHostStaticJoinTable.setStatus("current")
_Hh3cHostStaticJoinEntry_Object = MibTableRow
hh3cHostStaticJoinEntry = _Hh3cHostStaticJoinEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 51, 2, 4, 1)
)
hh3cHostStaticJoinEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HH3C-MPM-MIB", "hh3cHostStaticJoinVlanID"),
    (0, "HH3C-MPM-MIB", "hh3cHostStaticJoinAddressType"),
    (0, "HH3C-MPM-MIB", "hh3cHostStaticJoinAddress"),
)
if mibBuilder.loadTexts:
    hh3cHostStaticJoinEntry.setStatus("current")
_Hh3cHostStaticJoinVlanID_Type = Integer32
_Hh3cHostStaticJoinVlanID_Object = MibTableColumn
hh3cHostStaticJoinVlanID = _Hh3cHostStaticJoinVlanID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 51, 2, 4, 1, 1),
    _Hh3cHostStaticJoinVlanID_Type()
)
hh3cHostStaticJoinVlanID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cHostStaticJoinVlanID.setStatus("current")
_Hh3cHostStaticJoinAddressType_Type = InetAddressType
_Hh3cHostStaticJoinAddressType_Object = MibTableColumn
hh3cHostStaticJoinAddressType = _Hh3cHostStaticJoinAddressType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 51, 2, 4, 1, 2),
    _Hh3cHostStaticJoinAddressType_Type()
)
hh3cHostStaticJoinAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cHostStaticJoinAddressType.setStatus("current")
_Hh3cHostStaticJoinAddress_Type = InetAddress
_Hh3cHostStaticJoinAddress_Object = MibTableColumn
hh3cHostStaticJoinAddress = _Hh3cHostStaticJoinAddress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 51, 2, 4, 1, 3),
    _Hh3cHostStaticJoinAddress_Type()
)
hh3cHostStaticJoinAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cHostStaticJoinAddress.setStatus("current")
_Hh3cHostStaticJoinStatus_Type = RowStatus
_Hh3cHostStaticJoinStatus_Object = MibTableColumn
hh3cHostStaticJoinStatus = _Hh3cHostStaticJoinStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 51, 2, 4, 1, 4),
    _Hh3cHostStaticJoinStatus_Type()
)
hh3cHostStaticJoinStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cHostStaticJoinStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-MPM-MIB",
    **{"EnabledStatus": EnabledStatus,
       "hh3cMpm": hh3cMpm,
       "hh3cMPMObject": hh3cMPMObject,
       "hh3cMPortGroupLimitMinNumber": hh3cMPortGroupLimitMinNumber,
       "hh3cMPortGroupLimitMaxNumber": hh3cMPortGroupLimitMaxNumber,
       "hh3cMPMTable": hh3cMPMTable,
       "hh3cMPortGroupJoinTable": hh3cMPortGroupJoinTable,
       "hh3cMPortGroupJoinEntry": hh3cMPortGroupJoinEntry,
       "hh3cMPortGroupJoinVlanID": hh3cMPortGroupJoinVlanID,
       "hh3cMPortGroupJoinAddressType": hh3cMPortGroupJoinAddressType,
       "hh3cMPortGroupJoinAddress": hh3cMPortGroupJoinAddress,
       "hh3cMPortGroupJoinStatus": hh3cMPortGroupJoinStatus,
       "hh3cMPortGroupTable": hh3cMPortGroupTable,
       "hh3cMPortGroupEntry": hh3cMPortGroupEntry,
       "hh3cMPortGroupVlanID": hh3cMPortGroupVlanID,
       "hh3cMPortGroupAddressType": hh3cMPortGroupAddressType,
       "hh3cMPortGroupAddress": hh3cMPortGroupAddress,
       "hh3cMPortConfigTable": hh3cMPortConfigTable,
       "hh3cMPortConfigEntry": hh3cMPortConfigEntry,
       "hh3cMPortConfigVlanID": hh3cMPortConfigVlanID,
       "hh3cMPortGroupLimitNumber": hh3cMPortGroupLimitNumber,
       "hh3cMPortFastLeaveStatus": hh3cMPortFastLeaveStatus,
       "hh3cMPortGroupPolicyParameter": hh3cMPortGroupPolicyParameter,
       "hh3cMPortConfigRowStatus": hh3cMPortConfigRowStatus,
       "hh3cMPortGroupLimitReplace": hh3cMPortGroupLimitReplace,
       "hh3cHostStaticJoinTable": hh3cHostStaticJoinTable,
       "hh3cHostStaticJoinEntry": hh3cHostStaticJoinEntry,
       "hh3cHostStaticJoinVlanID": hh3cHostStaticJoinVlanID,
       "hh3cHostStaticJoinAddressType": hh3cHostStaticJoinAddressType,
       "hh3cHostStaticJoinAddress": hh3cHostStaticJoinAddress,
       "hh3cHostStaticJoinStatus": hh3cHostStaticJoinStatus}
)
