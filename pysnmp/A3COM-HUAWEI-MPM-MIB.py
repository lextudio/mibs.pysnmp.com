# SNMP MIB module (A3COM-HUAWEI-MPM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/A3COM-HUAWEI-MPM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:28:39 2024
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
    "A3COM-HUAWEI-OID-MIB",
    "h3cCommon")

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

h3cMpm = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 51)
)
h3cMpm.setRevisions(
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

_H3cMPMObject_ObjectIdentity = ObjectIdentity
h3cMPMObject = _H3cMPMObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 51, 1)
)
_H3cMPortGroupLimitMinNumber_Type = Unsigned32
_H3cMPortGroupLimitMinNumber_Object = MibScalar
h3cMPortGroupLimitMinNumber = _H3cMPortGroupLimitMinNumber_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 51, 1, 1),
    _H3cMPortGroupLimitMinNumber_Type()
)
h3cMPortGroupLimitMinNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cMPortGroupLimitMinNumber.setStatus("current")
_H3cMPortGroupLimitMaxNumber_Type = Unsigned32
_H3cMPortGroupLimitMaxNumber_Object = MibScalar
h3cMPortGroupLimitMaxNumber = _H3cMPortGroupLimitMaxNumber_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 51, 1, 2),
    _H3cMPortGroupLimitMaxNumber_Type()
)
h3cMPortGroupLimitMaxNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cMPortGroupLimitMaxNumber.setStatus("current")
_H3cMPMTable_ObjectIdentity = ObjectIdentity
h3cMPMTable = _H3cMPMTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 51, 2)
)
_H3cMPortGroupJoinTable_Object = MibTable
h3cMPortGroupJoinTable = _H3cMPortGroupJoinTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 51, 2, 1)
)
if mibBuilder.loadTexts:
    h3cMPortGroupJoinTable.setStatus("current")
_H3cMPortGroupJoinEntry_Object = MibTableRow
h3cMPortGroupJoinEntry = _H3cMPortGroupJoinEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 51, 2, 1, 1)
)
h3cMPortGroupJoinEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "A3COM-HUAWEI-MPM-MIB", "h3cMPortGroupJoinVlanID"),
    (0, "A3COM-HUAWEI-MPM-MIB", "h3cMPortGroupJoinAddressType"),
    (0, "A3COM-HUAWEI-MPM-MIB", "h3cMPortGroupJoinAddress"),
)
if mibBuilder.loadTexts:
    h3cMPortGroupJoinEntry.setStatus("current")
_H3cMPortGroupJoinVlanID_Type = Integer32
_H3cMPortGroupJoinVlanID_Object = MibTableColumn
h3cMPortGroupJoinVlanID = _H3cMPortGroupJoinVlanID_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 51, 2, 1, 1, 1),
    _H3cMPortGroupJoinVlanID_Type()
)
h3cMPortGroupJoinVlanID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cMPortGroupJoinVlanID.setStatus("current")
_H3cMPortGroupJoinAddressType_Type = InetAddressType
_H3cMPortGroupJoinAddressType_Object = MibTableColumn
h3cMPortGroupJoinAddressType = _H3cMPortGroupJoinAddressType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 51, 2, 1, 1, 2),
    _H3cMPortGroupJoinAddressType_Type()
)
h3cMPortGroupJoinAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cMPortGroupJoinAddressType.setStatus("current")
_H3cMPortGroupJoinAddress_Type = InetAddress
_H3cMPortGroupJoinAddress_Object = MibTableColumn
h3cMPortGroupJoinAddress = _H3cMPortGroupJoinAddress_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 51, 2, 1, 1, 3),
    _H3cMPortGroupJoinAddress_Type()
)
h3cMPortGroupJoinAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cMPortGroupJoinAddress.setStatus("current")
_H3cMPortGroupJoinStatus_Type = RowStatus
_H3cMPortGroupJoinStatus_Object = MibTableColumn
h3cMPortGroupJoinStatus = _H3cMPortGroupJoinStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 51, 2, 1, 1, 4),
    _H3cMPortGroupJoinStatus_Type()
)
h3cMPortGroupJoinStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cMPortGroupJoinStatus.setStatus("current")
_H3cMPortGroupTable_Object = MibTable
h3cMPortGroupTable = _H3cMPortGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 51, 2, 2)
)
if mibBuilder.loadTexts:
    h3cMPortGroupTable.setStatus("current")
_H3cMPortGroupEntry_Object = MibTableRow
h3cMPortGroupEntry = _H3cMPortGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 51, 2, 2, 1)
)
h3cMPortGroupEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "A3COM-HUAWEI-MPM-MIB", "h3cMPortGroupVlanID"),
    (0, "A3COM-HUAWEI-MPM-MIB", "h3cMPortGroupAddressType"),
    (0, "A3COM-HUAWEI-MPM-MIB", "h3cMPortGroupAddress"),
)
if mibBuilder.loadTexts:
    h3cMPortGroupEntry.setStatus("current")
_H3cMPortGroupVlanID_Type = Integer32
_H3cMPortGroupVlanID_Object = MibTableColumn
h3cMPortGroupVlanID = _H3cMPortGroupVlanID_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 51, 2, 2, 1, 1),
    _H3cMPortGroupVlanID_Type()
)
h3cMPortGroupVlanID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cMPortGroupVlanID.setStatus("current")
_H3cMPortGroupAddressType_Type = InetAddressType
_H3cMPortGroupAddressType_Object = MibTableColumn
h3cMPortGroupAddressType = _H3cMPortGroupAddressType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 51, 2, 2, 1, 2),
    _H3cMPortGroupAddressType_Type()
)
h3cMPortGroupAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cMPortGroupAddressType.setStatus("current")
_H3cMPortGroupAddress_Type = InetAddress
_H3cMPortGroupAddress_Object = MibTableColumn
h3cMPortGroupAddress = _H3cMPortGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 51, 2, 2, 1, 3),
    _H3cMPortGroupAddress_Type()
)
h3cMPortGroupAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cMPortGroupAddress.setStatus("current")
_H3cMPortConfigTable_Object = MibTable
h3cMPortConfigTable = _H3cMPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 51, 2, 3)
)
if mibBuilder.loadTexts:
    h3cMPortConfigTable.setStatus("current")
_H3cMPortConfigEntry_Object = MibTableRow
h3cMPortConfigEntry = _H3cMPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 51, 2, 3, 1)
)
h3cMPortConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "A3COM-HUAWEI-MPM-MIB", "h3cMPortConfigVlanID"),
)
if mibBuilder.loadTexts:
    h3cMPortConfigEntry.setStatus("current")
_H3cMPortConfigVlanID_Type = Integer32
_H3cMPortConfigVlanID_Object = MibTableColumn
h3cMPortConfigVlanID = _H3cMPortConfigVlanID_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 51, 2, 3, 1, 1),
    _H3cMPortConfigVlanID_Type()
)
h3cMPortConfigVlanID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cMPortConfigVlanID.setStatus("current")
_H3cMPortGroupLimitNumber_Type = Unsigned32
_H3cMPortGroupLimitNumber_Object = MibTableColumn
h3cMPortGroupLimitNumber = _H3cMPortGroupLimitNumber_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 51, 2, 3, 1, 2),
    _H3cMPortGroupLimitNumber_Type()
)
h3cMPortGroupLimitNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cMPortGroupLimitNumber.setStatus("current")


class _H3cMPortFastLeaveStatus_Type(EnabledStatus):
    """Custom type h3cMPortFastLeaveStatus based on EnabledStatus"""
    defaultValue = 2


_H3cMPortFastLeaveStatus_Object = MibTableColumn
h3cMPortFastLeaveStatus = _H3cMPortFastLeaveStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 51, 2, 3, 1, 3),
    _H3cMPortFastLeaveStatus_Type()
)
h3cMPortFastLeaveStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cMPortFastLeaveStatus.setStatus("current")


class _H3cMPortGroupPolicyParameter_Type(Integer32):
    """Custom type h3cMPortGroupPolicyParameter based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2000, 2999),
    )


_H3cMPortGroupPolicyParameter_Type.__name__ = "Integer32"
_H3cMPortGroupPolicyParameter_Object = MibTableColumn
h3cMPortGroupPolicyParameter = _H3cMPortGroupPolicyParameter_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 51, 2, 3, 1, 4),
    _H3cMPortGroupPolicyParameter_Type()
)
h3cMPortGroupPolicyParameter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cMPortGroupPolicyParameter.setStatus("current")
_H3cMPortConfigRowStatus_Type = RowStatus
_H3cMPortConfigRowStatus_Object = MibTableColumn
h3cMPortConfigRowStatus = _H3cMPortConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 51, 2, 3, 1, 5),
    _H3cMPortConfigRowStatus_Type()
)
h3cMPortConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cMPortConfigRowStatus.setStatus("current")


class _H3cMPortGroupLimitReplace_Type(EnabledStatus):
    """Custom type h3cMPortGroupLimitReplace based on EnabledStatus"""


_H3cMPortGroupLimitReplace_Object = MibTableColumn
h3cMPortGroupLimitReplace = _H3cMPortGroupLimitReplace_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 51, 2, 3, 1, 6),
    _H3cMPortGroupLimitReplace_Type()
)
h3cMPortGroupLimitReplace.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cMPortGroupLimitReplace.setStatus("current")
_H3cHostStaticJoinTable_Object = MibTable
h3cHostStaticJoinTable = _H3cHostStaticJoinTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 51, 2, 4)
)
if mibBuilder.loadTexts:
    h3cHostStaticJoinTable.setStatus("current")
_H3cHostStaticJoinEntry_Object = MibTableRow
h3cHostStaticJoinEntry = _H3cHostStaticJoinEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 51, 2, 4, 1)
)
h3cHostStaticJoinEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "A3COM-HUAWEI-MPM-MIB", "h3cHostStaticJoinVlanID"),
    (0, "A3COM-HUAWEI-MPM-MIB", "h3cHostStaticJoinAddressType"),
    (0, "A3COM-HUAWEI-MPM-MIB", "h3cHostStaticJoinAddress"),
)
if mibBuilder.loadTexts:
    h3cHostStaticJoinEntry.setStatus("current")
_H3cHostStaticJoinVlanID_Type = Integer32
_H3cHostStaticJoinVlanID_Object = MibTableColumn
h3cHostStaticJoinVlanID = _H3cHostStaticJoinVlanID_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 51, 2, 4, 1, 1),
    _H3cHostStaticJoinVlanID_Type()
)
h3cHostStaticJoinVlanID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cHostStaticJoinVlanID.setStatus("current")
_H3cHostStaticJoinAddressType_Type = InetAddressType
_H3cHostStaticJoinAddressType_Object = MibTableColumn
h3cHostStaticJoinAddressType = _H3cHostStaticJoinAddressType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 51, 2, 4, 1, 2),
    _H3cHostStaticJoinAddressType_Type()
)
h3cHostStaticJoinAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cHostStaticJoinAddressType.setStatus("current")
_H3cHostStaticJoinAddress_Type = InetAddress
_H3cHostStaticJoinAddress_Object = MibTableColumn
h3cHostStaticJoinAddress = _H3cHostStaticJoinAddress_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 51, 2, 4, 1, 3),
    _H3cHostStaticJoinAddress_Type()
)
h3cHostStaticJoinAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cHostStaticJoinAddress.setStatus("current")
_H3cHostStaticJoinStatus_Type = RowStatus
_H3cHostStaticJoinStatus_Object = MibTableColumn
h3cHostStaticJoinStatus = _H3cHostStaticJoinStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 51, 2, 4, 1, 4),
    _H3cHostStaticJoinStatus_Type()
)
h3cHostStaticJoinStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cHostStaticJoinStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "A3COM-HUAWEI-MPM-MIB",
    **{"EnabledStatus": EnabledStatus,
       "h3cMpm": h3cMpm,
       "h3cMPMObject": h3cMPMObject,
       "h3cMPortGroupLimitMinNumber": h3cMPortGroupLimitMinNumber,
       "h3cMPortGroupLimitMaxNumber": h3cMPortGroupLimitMaxNumber,
       "h3cMPMTable": h3cMPMTable,
       "h3cMPortGroupJoinTable": h3cMPortGroupJoinTable,
       "h3cMPortGroupJoinEntry": h3cMPortGroupJoinEntry,
       "h3cMPortGroupJoinVlanID": h3cMPortGroupJoinVlanID,
       "h3cMPortGroupJoinAddressType": h3cMPortGroupJoinAddressType,
       "h3cMPortGroupJoinAddress": h3cMPortGroupJoinAddress,
       "h3cMPortGroupJoinStatus": h3cMPortGroupJoinStatus,
       "h3cMPortGroupTable": h3cMPortGroupTable,
       "h3cMPortGroupEntry": h3cMPortGroupEntry,
       "h3cMPortGroupVlanID": h3cMPortGroupVlanID,
       "h3cMPortGroupAddressType": h3cMPortGroupAddressType,
       "h3cMPortGroupAddress": h3cMPortGroupAddress,
       "h3cMPortConfigTable": h3cMPortConfigTable,
       "h3cMPortConfigEntry": h3cMPortConfigEntry,
       "h3cMPortConfigVlanID": h3cMPortConfigVlanID,
       "h3cMPortGroupLimitNumber": h3cMPortGroupLimitNumber,
       "h3cMPortFastLeaveStatus": h3cMPortFastLeaveStatus,
       "h3cMPortGroupPolicyParameter": h3cMPortGroupPolicyParameter,
       "h3cMPortConfigRowStatus": h3cMPortConfigRowStatus,
       "h3cMPortGroupLimitReplace": h3cMPortGroupLimitReplace,
       "h3cHostStaticJoinTable": h3cHostStaticJoinTable,
       "h3cHostStaticJoinEntry": h3cHostStaticJoinEntry,
       "h3cHostStaticJoinVlanID": h3cHostStaticJoinVlanID,
       "h3cHostStaticJoinAddressType": h3cHostStaticJoinAddressType,
       "h3cHostStaticJoinAddress": h3cHostStaticJoinAddress,
       "h3cHostStaticJoinStatus": h3cHostStaticJoinStatus}
)
