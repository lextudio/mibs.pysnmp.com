# SNMP MIB module (HPN-ICF-MPM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-MPM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:01:15 2024
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

(hpnicfCommon,) = mibBuilder.importSymbols(
    "HPN-ICF-OID-MIB",
    "hpnicfCommon")

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

hpnicfMpm = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 51)
)
hpnicfMpm.setRevisions(
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

_HpnicfMPMObject_ObjectIdentity = ObjectIdentity
hpnicfMPMObject = _HpnicfMPMObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 51, 1)
)
_HpnicfMPortGroupLimitMinNumber_Type = Unsigned32
_HpnicfMPortGroupLimitMinNumber_Object = MibScalar
hpnicfMPortGroupLimitMinNumber = _HpnicfMPortGroupLimitMinNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 51, 1, 1),
    _HpnicfMPortGroupLimitMinNumber_Type()
)
hpnicfMPortGroupLimitMinNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfMPortGroupLimitMinNumber.setStatus("current")
_HpnicfMPortGroupLimitMaxNumber_Type = Unsigned32
_HpnicfMPortGroupLimitMaxNumber_Object = MibScalar
hpnicfMPortGroupLimitMaxNumber = _HpnicfMPortGroupLimitMaxNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 51, 1, 2),
    _HpnicfMPortGroupLimitMaxNumber_Type()
)
hpnicfMPortGroupLimitMaxNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfMPortGroupLimitMaxNumber.setStatus("current")
_HpnicfMPMTable_ObjectIdentity = ObjectIdentity
hpnicfMPMTable = _HpnicfMPMTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 51, 2)
)
_HpnicfMPortGroupJoinTable_Object = MibTable
hpnicfMPortGroupJoinTable = _HpnicfMPortGroupJoinTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 51, 2, 1)
)
if mibBuilder.loadTexts:
    hpnicfMPortGroupJoinTable.setStatus("current")
_HpnicfMPortGroupJoinEntry_Object = MibTableRow
hpnicfMPortGroupJoinEntry = _HpnicfMPortGroupJoinEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 51, 2, 1, 1)
)
hpnicfMPortGroupJoinEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HPN-ICF-MPM-MIB", "hpnicfMPortGroupJoinVlanID"),
    (0, "HPN-ICF-MPM-MIB", "hpnicfMPortGroupJoinAddressType"),
    (0, "HPN-ICF-MPM-MIB", "hpnicfMPortGroupJoinAddress"),
)
if mibBuilder.loadTexts:
    hpnicfMPortGroupJoinEntry.setStatus("current")
_HpnicfMPortGroupJoinVlanID_Type = Integer32
_HpnicfMPortGroupJoinVlanID_Object = MibTableColumn
hpnicfMPortGroupJoinVlanID = _HpnicfMPortGroupJoinVlanID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 51, 2, 1, 1, 1),
    _HpnicfMPortGroupJoinVlanID_Type()
)
hpnicfMPortGroupJoinVlanID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfMPortGroupJoinVlanID.setStatus("current")
_HpnicfMPortGroupJoinAddressType_Type = InetAddressType
_HpnicfMPortGroupJoinAddressType_Object = MibTableColumn
hpnicfMPortGroupJoinAddressType = _HpnicfMPortGroupJoinAddressType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 51, 2, 1, 1, 2),
    _HpnicfMPortGroupJoinAddressType_Type()
)
hpnicfMPortGroupJoinAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfMPortGroupJoinAddressType.setStatus("current")
_HpnicfMPortGroupJoinAddress_Type = InetAddress
_HpnicfMPortGroupJoinAddress_Object = MibTableColumn
hpnicfMPortGroupJoinAddress = _HpnicfMPortGroupJoinAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 51, 2, 1, 1, 3),
    _HpnicfMPortGroupJoinAddress_Type()
)
hpnicfMPortGroupJoinAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfMPortGroupJoinAddress.setStatus("current")
_HpnicfMPortGroupJoinStatus_Type = RowStatus
_HpnicfMPortGroupJoinStatus_Object = MibTableColumn
hpnicfMPortGroupJoinStatus = _HpnicfMPortGroupJoinStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 51, 2, 1, 1, 4),
    _HpnicfMPortGroupJoinStatus_Type()
)
hpnicfMPortGroupJoinStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMPortGroupJoinStatus.setStatus("current")
_HpnicfMPortGroupTable_Object = MibTable
hpnicfMPortGroupTable = _HpnicfMPortGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 51, 2, 2)
)
if mibBuilder.loadTexts:
    hpnicfMPortGroupTable.setStatus("current")
_HpnicfMPortGroupEntry_Object = MibTableRow
hpnicfMPortGroupEntry = _HpnicfMPortGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 51, 2, 2, 1)
)
hpnicfMPortGroupEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HPN-ICF-MPM-MIB", "hpnicfMPortGroupVlanID"),
    (0, "HPN-ICF-MPM-MIB", "hpnicfMPortGroupAddressType"),
    (0, "HPN-ICF-MPM-MIB", "hpnicfMPortGroupAddress"),
)
if mibBuilder.loadTexts:
    hpnicfMPortGroupEntry.setStatus("current")
_HpnicfMPortGroupVlanID_Type = Integer32
_HpnicfMPortGroupVlanID_Object = MibTableColumn
hpnicfMPortGroupVlanID = _HpnicfMPortGroupVlanID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 51, 2, 2, 1, 1),
    _HpnicfMPortGroupVlanID_Type()
)
hpnicfMPortGroupVlanID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfMPortGroupVlanID.setStatus("current")
_HpnicfMPortGroupAddressType_Type = InetAddressType
_HpnicfMPortGroupAddressType_Object = MibTableColumn
hpnicfMPortGroupAddressType = _HpnicfMPortGroupAddressType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 51, 2, 2, 1, 2),
    _HpnicfMPortGroupAddressType_Type()
)
hpnicfMPortGroupAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfMPortGroupAddressType.setStatus("current")
_HpnicfMPortGroupAddress_Type = InetAddress
_HpnicfMPortGroupAddress_Object = MibTableColumn
hpnicfMPortGroupAddress = _HpnicfMPortGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 51, 2, 2, 1, 3),
    _HpnicfMPortGroupAddress_Type()
)
hpnicfMPortGroupAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfMPortGroupAddress.setStatus("current")
_HpnicfMPortConfigTable_Object = MibTable
hpnicfMPortConfigTable = _HpnicfMPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 51, 2, 3)
)
if mibBuilder.loadTexts:
    hpnicfMPortConfigTable.setStatus("current")
_HpnicfMPortConfigEntry_Object = MibTableRow
hpnicfMPortConfigEntry = _HpnicfMPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 51, 2, 3, 1)
)
hpnicfMPortConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HPN-ICF-MPM-MIB", "hpnicfMPortConfigVlanID"),
)
if mibBuilder.loadTexts:
    hpnicfMPortConfigEntry.setStatus("current")
_HpnicfMPortConfigVlanID_Type = Integer32
_HpnicfMPortConfigVlanID_Object = MibTableColumn
hpnicfMPortConfigVlanID = _HpnicfMPortConfigVlanID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 51, 2, 3, 1, 1),
    _HpnicfMPortConfigVlanID_Type()
)
hpnicfMPortConfigVlanID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfMPortConfigVlanID.setStatus("current")
_HpnicfMPortGroupLimitNumber_Type = Unsigned32
_HpnicfMPortGroupLimitNumber_Object = MibTableColumn
hpnicfMPortGroupLimitNumber = _HpnicfMPortGroupLimitNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 51, 2, 3, 1, 2),
    _HpnicfMPortGroupLimitNumber_Type()
)
hpnicfMPortGroupLimitNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMPortGroupLimitNumber.setStatus("current")


class _HpnicfMPortFastLeaveStatus_Type(EnabledStatus):
    """Custom type hpnicfMPortFastLeaveStatus based on EnabledStatus"""
    defaultValue = 2


_HpnicfMPortFastLeaveStatus_Object = MibTableColumn
hpnicfMPortFastLeaveStatus = _HpnicfMPortFastLeaveStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 51, 2, 3, 1, 3),
    _HpnicfMPortFastLeaveStatus_Type()
)
hpnicfMPortFastLeaveStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMPortFastLeaveStatus.setStatus("current")


class _HpnicfMPortGroupPolicyParameter_Type(Integer32):
    """Custom type hpnicfMPortGroupPolicyParameter based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2000, 2999),
    )


_HpnicfMPortGroupPolicyParameter_Type.__name__ = "Integer32"
_HpnicfMPortGroupPolicyParameter_Object = MibTableColumn
hpnicfMPortGroupPolicyParameter = _HpnicfMPortGroupPolicyParameter_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 51, 2, 3, 1, 4),
    _HpnicfMPortGroupPolicyParameter_Type()
)
hpnicfMPortGroupPolicyParameter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMPortGroupPolicyParameter.setStatus("current")
_HpnicfMPortConfigRowStatus_Type = RowStatus
_HpnicfMPortConfigRowStatus_Object = MibTableColumn
hpnicfMPortConfigRowStatus = _HpnicfMPortConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 51, 2, 3, 1, 5),
    _HpnicfMPortConfigRowStatus_Type()
)
hpnicfMPortConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMPortConfigRowStatus.setStatus("current")


class _HpnicfMPortGroupLimitReplace_Type(EnabledStatus):
    """Custom type hpnicfMPortGroupLimitReplace based on EnabledStatus"""


_HpnicfMPortGroupLimitReplace_Object = MibTableColumn
hpnicfMPortGroupLimitReplace = _HpnicfMPortGroupLimitReplace_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 51, 2, 3, 1, 6),
    _HpnicfMPortGroupLimitReplace_Type()
)
hpnicfMPortGroupLimitReplace.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMPortGroupLimitReplace.setStatus("current")
_HpnicfHostStaticJoinTable_Object = MibTable
hpnicfHostStaticJoinTable = _HpnicfHostStaticJoinTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 51, 2, 4)
)
if mibBuilder.loadTexts:
    hpnicfHostStaticJoinTable.setStatus("current")
_HpnicfHostStaticJoinEntry_Object = MibTableRow
hpnicfHostStaticJoinEntry = _HpnicfHostStaticJoinEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 51, 2, 4, 1)
)
hpnicfHostStaticJoinEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HPN-ICF-MPM-MIB", "hpnicfHostStaticJoinVlanID"),
    (0, "HPN-ICF-MPM-MIB", "hpnicfHostStaticJoinAddressType"),
    (0, "HPN-ICF-MPM-MIB", "hpnicfHostStaticJoinAddress"),
)
if mibBuilder.loadTexts:
    hpnicfHostStaticJoinEntry.setStatus("current")
_HpnicfHostStaticJoinVlanID_Type = Integer32
_HpnicfHostStaticJoinVlanID_Object = MibTableColumn
hpnicfHostStaticJoinVlanID = _HpnicfHostStaticJoinVlanID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 51, 2, 4, 1, 1),
    _HpnicfHostStaticJoinVlanID_Type()
)
hpnicfHostStaticJoinVlanID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfHostStaticJoinVlanID.setStatus("current")
_HpnicfHostStaticJoinAddressType_Type = InetAddressType
_HpnicfHostStaticJoinAddressType_Object = MibTableColumn
hpnicfHostStaticJoinAddressType = _HpnicfHostStaticJoinAddressType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 51, 2, 4, 1, 2),
    _HpnicfHostStaticJoinAddressType_Type()
)
hpnicfHostStaticJoinAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfHostStaticJoinAddressType.setStatus("current")
_HpnicfHostStaticJoinAddress_Type = InetAddress
_HpnicfHostStaticJoinAddress_Object = MibTableColumn
hpnicfHostStaticJoinAddress = _HpnicfHostStaticJoinAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 51, 2, 4, 1, 3),
    _HpnicfHostStaticJoinAddress_Type()
)
hpnicfHostStaticJoinAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfHostStaticJoinAddress.setStatus("current")
_HpnicfHostStaticJoinStatus_Type = RowStatus
_HpnicfHostStaticJoinStatus_Object = MibTableColumn
hpnicfHostStaticJoinStatus = _HpnicfHostStaticJoinStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 51, 2, 4, 1, 4),
    _HpnicfHostStaticJoinStatus_Type()
)
hpnicfHostStaticJoinStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfHostStaticJoinStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-MPM-MIB",
    **{"EnabledStatus": EnabledStatus,
       "hpnicfMpm": hpnicfMpm,
       "hpnicfMPMObject": hpnicfMPMObject,
       "hpnicfMPortGroupLimitMinNumber": hpnicfMPortGroupLimitMinNumber,
       "hpnicfMPortGroupLimitMaxNumber": hpnicfMPortGroupLimitMaxNumber,
       "hpnicfMPMTable": hpnicfMPMTable,
       "hpnicfMPortGroupJoinTable": hpnicfMPortGroupJoinTable,
       "hpnicfMPortGroupJoinEntry": hpnicfMPortGroupJoinEntry,
       "hpnicfMPortGroupJoinVlanID": hpnicfMPortGroupJoinVlanID,
       "hpnicfMPortGroupJoinAddressType": hpnicfMPortGroupJoinAddressType,
       "hpnicfMPortGroupJoinAddress": hpnicfMPortGroupJoinAddress,
       "hpnicfMPortGroupJoinStatus": hpnicfMPortGroupJoinStatus,
       "hpnicfMPortGroupTable": hpnicfMPortGroupTable,
       "hpnicfMPortGroupEntry": hpnicfMPortGroupEntry,
       "hpnicfMPortGroupVlanID": hpnicfMPortGroupVlanID,
       "hpnicfMPortGroupAddressType": hpnicfMPortGroupAddressType,
       "hpnicfMPortGroupAddress": hpnicfMPortGroupAddress,
       "hpnicfMPortConfigTable": hpnicfMPortConfigTable,
       "hpnicfMPortConfigEntry": hpnicfMPortConfigEntry,
       "hpnicfMPortConfigVlanID": hpnicfMPortConfigVlanID,
       "hpnicfMPortGroupLimitNumber": hpnicfMPortGroupLimitNumber,
       "hpnicfMPortFastLeaveStatus": hpnicfMPortFastLeaveStatus,
       "hpnicfMPortGroupPolicyParameter": hpnicfMPortGroupPolicyParameter,
       "hpnicfMPortConfigRowStatus": hpnicfMPortConfigRowStatus,
       "hpnicfMPortGroupLimitReplace": hpnicfMPortGroupLimitReplace,
       "hpnicfHostStaticJoinTable": hpnicfHostStaticJoinTable,
       "hpnicfHostStaticJoinEntry": hpnicfHostStaticJoinEntry,
       "hpnicfHostStaticJoinVlanID": hpnicfHostStaticJoinVlanID,
       "hpnicfHostStaticJoinAddressType": hpnicfHostStaticJoinAddressType,
       "hpnicfHostStaticJoinAddress": hpnicfHostStaticJoinAddress,
       "hpnicfHostStaticJoinStatus": hpnicfHostStaticJoinStatus}
)
