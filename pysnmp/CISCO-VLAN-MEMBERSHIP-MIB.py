# SNMP MIB module (CISCO-VLAN-MEMBERSHIP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-VLAN-MEMBERSHIP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:12:07 2024
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

(CiscoPortList,
 CiscoPortListRange) = mibBuilder.importSymbols(
    "CISCO-TC",
    "CiscoPortList",
    "CiscoPortListRange")

(VlanIndex,) = mibBuilder.importSymbols(
    "CISCO-VTP-MIB",
    "VlanIndex")

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

ciscoVlanMembershipMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 68)
)
ciscoVlanMembershipMIB.setRevisions(
        ("2007-12-14 00:00",
         "2004-07-16 00:00",
         "2004-04-07 00:00",
         "2003-10-10 00:00",
         "2003-06-05 00:00",
         "2002-03-28 00:00",
         "2001-05-01 00:00",
         "2001-01-30 00:00",
         "2000-01-06 00:00",
         "1999-01-18 00:00",
         "1996-12-06 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoVlanMembershipMIBObjects_ObjectIdentity = ObjectIdentity
ciscoVlanMembershipMIBObjects = _CiscoVlanMembershipMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 68, 1)
)
_VmVmps_ObjectIdentity = ObjectIdentity
vmVmps = _VmVmps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 68, 1, 1)
)
_VmVmpsVQPVersion_Type = Integer32
_VmVmpsVQPVersion_Object = MibScalar
vmVmpsVQPVersion = _VmVmpsVQPVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 68, 1, 1, 1),
    _VmVmpsVQPVersion_Type()
)
vmVmpsVQPVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmVmpsVQPVersion.setStatus("current")


class _VmVmpsRetries_Type(Integer32):
    """Custom type vmVmpsRetries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_VmVmpsRetries_Type.__name__ = "Integer32"
_VmVmpsRetries_Object = MibScalar
vmVmpsRetries = _VmVmpsRetries_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 68, 1, 1, 2),
    _VmVmpsRetries_Type()
)
vmVmpsRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vmVmpsRetries.setStatus("current")


class _VmVmpsReconfirmInterval_Type(Integer32):
    """Custom type vmVmpsReconfirmInterval based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 120),
    )


_VmVmpsReconfirmInterval_Type.__name__ = "Integer32"
_VmVmpsReconfirmInterval_Object = MibScalar
vmVmpsReconfirmInterval = _VmVmpsReconfirmInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 68, 1, 1, 3),
    _VmVmpsReconfirmInterval_Type()
)
vmVmpsReconfirmInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vmVmpsReconfirmInterval.setStatus("current")
if mibBuilder.loadTexts:
    vmVmpsReconfirmInterval.setUnits("Minutes")


class _VmVmpsReconfirm_Type(Integer32):
    """Custom type vmVmpsReconfirm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("execute", 2),
          ("ready", 1))
    )


_VmVmpsReconfirm_Type.__name__ = "Integer32"
_VmVmpsReconfirm_Object = MibScalar
vmVmpsReconfirm = _VmVmpsReconfirm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 68, 1, 1, 4),
    _VmVmpsReconfirm_Type()
)
vmVmpsReconfirm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vmVmpsReconfirm.setStatus("current")


class _VmVmpsReconfirmResult_Type(Integer32):
    """Custom type vmVmpsReconfirmResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("inProgress", 2),
          ("noDynamicPort", 6),
          ("noHostConnected", 7),
          ("noResponse", 4),
          ("noVmps", 5),
          ("other", 1),
          ("success", 3))
    )


_VmVmpsReconfirmResult_Type.__name__ = "Integer32"
_VmVmpsReconfirmResult_Object = MibScalar
vmVmpsReconfirmResult = _VmVmpsReconfirmResult_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 68, 1, 1, 5),
    _VmVmpsReconfirmResult_Type()
)
vmVmpsReconfirmResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmVmpsReconfirmResult.setStatus("current")
_VmVmpsCurrent_Type = IpAddress
_VmVmpsCurrent_Object = MibScalar
vmVmpsCurrent = _VmVmpsCurrent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 68, 1, 1, 6),
    _VmVmpsCurrent_Type()
)
vmVmpsCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmVmpsCurrent.setStatus("current")
_VmVmpsTable_Object = MibTable
vmVmpsTable = _VmVmpsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 68, 1, 1, 7)
)
if mibBuilder.loadTexts:
    vmVmpsTable.setStatus("current")
_VmVmpsEntry_Object = MibTableRow
vmVmpsEntry = _VmVmpsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 68, 1, 1, 7, 1)
)
vmVmpsEntry.setIndexNames(
    (0, "CISCO-VLAN-MEMBERSHIP-MIB", "vmVmpsIpAddress"),
)
if mibBuilder.loadTexts:
    vmVmpsEntry.setStatus("current")
_VmVmpsIpAddress_Type = IpAddress
_VmVmpsIpAddress_Object = MibTableColumn
vmVmpsIpAddress = _VmVmpsIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 68, 1, 1, 7, 1, 1),
    _VmVmpsIpAddress_Type()
)
vmVmpsIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmVmpsIpAddress.setStatus("current")
_VmVmpsPrimary_Type = TruthValue
_VmVmpsPrimary_Object = MibTableColumn
vmVmpsPrimary = _VmVmpsPrimary_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 68, 1, 1, 7, 1, 2),
    _VmVmpsPrimary_Type()
)
vmVmpsPrimary.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vmVmpsPrimary.setStatus("current")
_VmVmpsRowStatus_Type = RowStatus
_VmVmpsRowStatus_Object = MibTableColumn
vmVmpsRowStatus = _VmVmpsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 68, 1, 1, 7, 1, 3),
    _VmVmpsRowStatus_Type()
)
vmVmpsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vmVmpsRowStatus.setStatus("current")
_VmMembership_ObjectIdentity = ObjectIdentity
vmMembership = _VmMembership_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 68, 1, 2)
)
_VmMembershipSummaryTable_Object = MibTable
vmMembershipSummaryTable = _VmMembershipSummaryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 68, 1, 2, 1)
)
if mibBuilder.loadTexts:
    vmMembershipSummaryTable.setStatus("current")
_VmMembershipSummaryEntry_Object = MibTableRow
vmMembershipSummaryEntry = _VmMembershipSummaryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 68, 1, 2, 1, 1)
)
vmMembershipSummaryEntry.setIndexNames(
    (0, "CISCO-VLAN-MEMBERSHIP-MIB", "vmMembershipSummaryVlanIndex"),
)
if mibBuilder.loadTexts:
    vmMembershipSummaryEntry.setStatus("current")
_VmMembershipSummaryVlanIndex_Type = VlanIndex
_VmMembershipSummaryVlanIndex_Object = MibTableColumn
vmMembershipSummaryVlanIndex = _VmMembershipSummaryVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 68, 1, 2, 1, 1, 1),
    _VmMembershipSummaryVlanIndex_Type()
)
vmMembershipSummaryVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vmMembershipSummaryVlanIndex.setStatus("current")


class _VmMembershipSummaryMemberPorts_Type(OctetString):
    """Custom type vmMembershipSummaryMemberPorts based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_VmMembershipSummaryMemberPorts_Type.__name__ = "OctetString"
_VmMembershipSummaryMemberPorts_Object = MibTableColumn
vmMembershipSummaryMemberPorts = _VmMembershipSummaryMemberPorts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 68, 1, 2, 1, 1, 2),
    _VmMembershipSummaryMemberPorts_Type()
)
vmMembershipSummaryMemberPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmMembershipSummaryMemberPorts.setStatus("deprecated")
_VmMembershipSummaryMember2kPorts_Type = CiscoPortList
_VmMembershipSummaryMember2kPorts_Object = MibTableColumn
vmMembershipSummaryMember2kPorts = _VmMembershipSummaryMember2kPorts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 68, 1, 2, 1, 1, 3),
    _VmMembershipSummaryMember2kPorts_Type()
)
vmMembershipSummaryMember2kPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmMembershipSummaryMember2kPorts.setStatus("current")
_VmMembershipTable_Object = MibTable
vmMembershipTable = _VmMembershipTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 68, 1, 2, 2)
)
if mibBuilder.loadTexts:
    vmMembershipTable.setStatus("current")
_VmMembershipEntry_Object = MibTableRow
vmMembershipEntry = _VmMembershipEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 68, 1, 2, 2, 1)
)
vmMembershipEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    vmMembershipEntry.setStatus("current")


class _VmVlanType_Type(Integer32):
    """Custom type vmVlanType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("multiVlan", 3),
          ("static", 1))
    )


_VmVlanType_Type.__name__ = "Integer32"
_VmVlanType_Object = MibTableColumn
vmVlanType = _VmVlanType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 68, 1, 2, 2, 1, 1),
    _VmVlanType_Type()
)
vmVlanType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vmVlanType.setStatus("current")


class _VmVlan_Type(Integer32):
    """Custom type vmVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_VmVlan_Type.__name__ = "Integer32"
_VmVlan_Object = MibTableColumn
vmVlan = _VmVlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 68, 1, 2, 2, 1, 2),
    _VmVlan_Type()
)
vmVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vmVlan.setStatus("current")


class _VmPortStatus_Type(Integer32):
    """Custom type vmPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("inactive", 1),
          ("shutdown", 3))
    )


_VmPortStatus_Type.__name__ = "Integer32"
_VmPortStatus_Object = MibTableColumn
vmPortStatus = _VmPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 68, 1, 2, 2, 1, 3),
    _VmPortStatus_Type()
)
vmPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmPortStatus.setStatus("current")


class _VmVlans_Type(OctetString):
    """Custom type vmVlans based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_VmVlans_Type.__name__ = "OctetString"
_VmVlans_Object = MibTableColumn
vmVlans = _VmVlans_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 68, 1, 2, 2, 1, 4),
    _VmVlans_Type()
)
vmVlans.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vmVlans.setStatus("current")


class _VmVlans2k_Type(OctetString):
    """Custom type vmVlans2k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_VmVlans2k_Type.__name__ = "OctetString"
_VmVlans2k_Object = MibTableColumn
vmVlans2k = _VmVlans2k_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 68, 1, 2, 2, 1, 5),
    _VmVlans2k_Type()
)
vmVlans2k.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vmVlans2k.setStatus("current")


class _VmVlans3k_Type(OctetString):
    """Custom type vmVlans3k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_VmVlans3k_Type.__name__ = "OctetString"
_VmVlans3k_Object = MibTableColumn
vmVlans3k = _VmVlans3k_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 68, 1, 2, 2, 1, 6),
    _VmVlans3k_Type()
)
vmVlans3k.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vmVlans3k.setStatus("current")


class _VmVlans4k_Type(OctetString):
    """Custom type vmVlans4k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_VmVlans4k_Type.__name__ = "OctetString"
_VmVlans4k_Object = MibTableColumn
vmVlans4k = _VmVlans4k_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 68, 1, 2, 2, 1, 7),
    _VmVlans4k_Type()
)
vmVlans4k.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vmVlans4k.setStatus("current")
_VmMembershipSummaryExtTable_Object = MibTable
vmMembershipSummaryExtTable = _VmMembershipSummaryExtTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 68, 1, 2, 3)
)
if mibBuilder.loadTexts:
    vmMembershipSummaryExtTable.setStatus("current")
_VmMembershipSummaryExtEntry_Object = MibTableRow
vmMembershipSummaryExtEntry = _VmMembershipSummaryExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 68, 1, 2, 3, 1)
)
vmMembershipSummaryExtEntry.setIndexNames(
    (0, "CISCO-VLAN-MEMBERSHIP-MIB", "vmMembershipSummaryVlanIndex"),
    (0, "CISCO-VLAN-MEMBERSHIP-MIB", "vmMembershipPortRangeIndex"),
)
if mibBuilder.loadTexts:
    vmMembershipSummaryExtEntry.setStatus("current")
_VmMembershipPortRangeIndex_Type = CiscoPortListRange
_VmMembershipPortRangeIndex_Object = MibTableColumn
vmMembershipPortRangeIndex = _VmMembershipPortRangeIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 68, 1, 2, 3, 1, 1),
    _VmMembershipPortRangeIndex_Type()
)
vmMembershipPortRangeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vmMembershipPortRangeIndex.setStatus("current")
_VmMembershipSummaryExtPorts_Type = CiscoPortList
_VmMembershipSummaryExtPorts_Object = MibTableColumn
vmMembershipSummaryExtPorts = _VmMembershipSummaryExtPorts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 68, 1, 2, 3, 1, 2),
    _VmMembershipSummaryExtPorts_Type()
)
vmMembershipSummaryExtPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmMembershipSummaryExtPorts.setStatus("current")


class _VmVlanCreationMode_Type(Integer32):
    """Custom type vmVlanCreationMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("automatic", 1),
          ("manual", 2))
    )


_VmVlanCreationMode_Type.__name__ = "Integer32"
_VmVlanCreationMode_Object = MibScalar
vmVlanCreationMode = _VmVlanCreationMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 68, 1, 2, 4),
    _VmVlanCreationMode_Type()
)
vmVlanCreationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vmVlanCreationMode.setStatus("current")
_VmStatistics_ObjectIdentity = ObjectIdentity
vmStatistics = _VmStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 68, 1, 3)
)
_VmVQPQueries_Type = Counter32
_VmVQPQueries_Object = MibScalar
vmVQPQueries = _VmVQPQueries_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 68, 1, 3, 1),
    _VmVQPQueries_Type()
)
vmVQPQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmVQPQueries.setStatus("current")
_VmVQPResponses_Type = Counter32
_VmVQPResponses_Object = MibScalar
vmVQPResponses = _VmVQPResponses_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 68, 1, 3, 2),
    _VmVQPResponses_Type()
)
vmVQPResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmVQPResponses.setStatus("current")
_VmVmpsChanges_Type = Counter32
_VmVmpsChanges_Object = MibScalar
vmVmpsChanges = _VmVmpsChanges_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 68, 1, 3, 3),
    _VmVmpsChanges_Type()
)
vmVmpsChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmVmpsChanges.setStatus("current")
_VmVQPShutdown_Type = Counter32
_VmVQPShutdown_Object = MibScalar
vmVQPShutdown = _VmVQPShutdown_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 68, 1, 3, 4),
    _VmVQPShutdown_Type()
)
vmVQPShutdown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmVQPShutdown.setStatus("current")
_VmVQPDenied_Type = Counter32
_VmVQPDenied_Object = MibScalar
vmVQPDenied = _VmVQPDenied_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 68, 1, 3, 5),
    _VmVQPDenied_Type()
)
vmVQPDenied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmVQPDenied.setStatus("current")
_VmVQPWrongDomain_Type = Counter32
_VmVQPWrongDomain_Object = MibScalar
vmVQPWrongDomain = _VmVQPWrongDomain_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 68, 1, 3, 6),
    _VmVQPWrongDomain_Type()
)
vmVQPWrongDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmVQPWrongDomain.setStatus("current")
_VmVQPWrongVersion_Type = Counter32
_VmVQPWrongVersion_Object = MibScalar
vmVQPWrongVersion = _VmVQPWrongVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 68, 1, 3, 7),
    _VmVQPWrongVersion_Type()
)
vmVQPWrongVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmVQPWrongVersion.setStatus("current")
_VmInsufficientResources_Type = Counter32
_VmInsufficientResources_Object = MibScalar
vmInsufficientResources = _VmInsufficientResources_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 68, 1, 3, 8),
    _VmInsufficientResources_Type()
)
vmInsufficientResources.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmInsufficientResources.setStatus("current")
_VmStatus_ObjectIdentity = ObjectIdentity
vmStatus = _VmStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 68, 1, 4)
)
_VmNotificationsEnabled_Type = TruthValue
_VmNotificationsEnabled_Object = MibScalar
vmNotificationsEnabled = _VmNotificationsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 68, 1, 4, 1),
    _VmNotificationsEnabled_Type()
)
vmNotificationsEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vmNotificationsEnabled.setStatus("current")
_VmVoiceVlan_ObjectIdentity = ObjectIdentity
vmVoiceVlan = _VmVoiceVlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 68, 1, 5)
)
_VmVoiceVlanTable_Object = MibTable
vmVoiceVlanTable = _VmVoiceVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 68, 1, 5, 1)
)
if mibBuilder.loadTexts:
    vmVoiceVlanTable.setStatus("current")
_VmVoiceVlanEntry_Object = MibTableRow
vmVoiceVlanEntry = _VmVoiceVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 68, 1, 5, 1, 1)
)
vmVoiceVlanEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    vmVoiceVlanEntry.setStatus("current")


class _VmVoiceVlanId_Type(Integer32):
    """Custom type vmVoiceVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_VmVoiceVlanId_Type.__name__ = "Integer32"
_VmVoiceVlanId_Object = MibTableColumn
vmVoiceVlanId = _VmVoiceVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 68, 1, 5, 1, 1, 1),
    _VmVoiceVlanId_Type()
)
vmVoiceVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vmVoiceVlanId.setStatus("current")
_VmVoiceVlanCdpVerifyEnable_Type = TruthValue
_VmVoiceVlanCdpVerifyEnable_Object = MibTableColumn
vmVoiceVlanCdpVerifyEnable = _VmVoiceVlanCdpVerifyEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 68, 1, 5, 1, 1, 2),
    _VmVoiceVlanCdpVerifyEnable_Type()
)
vmVoiceVlanCdpVerifyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vmVoiceVlanCdpVerifyEnable.setStatus("current")
_VmNotifications_ObjectIdentity = ObjectIdentity
vmNotifications = _VmNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 68, 2)
)
_VmNotificationsPrefix_ObjectIdentity = ObjectIdentity
vmNotificationsPrefix = _VmNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 68, 2, 0)
)
_VmMIBConformance_ObjectIdentity = ObjectIdentity
vmMIBConformance = _VmMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 68, 3)
)
_VmMIBCompliances_ObjectIdentity = ObjectIdentity
vmMIBCompliances = _VmMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 68, 3, 1)
)
_VmMIBGroups_ObjectIdentity = ObjectIdentity
vmMIBGroups = _VmMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 68, 3, 2)
)

# Managed Objects groups

vmMembershipGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 68, 3, 2, 1)
)
vmMembershipGroup.setObjects(
      *(("CISCO-VLAN-MEMBERSHIP-MIB", "vmMembershipSummaryMemberPorts"),
        ("CISCO-VLAN-MEMBERSHIP-MIB", "vmVlan"),
        ("CISCO-VLAN-MEMBERSHIP-MIB", "vmVlanType"),
        ("CISCO-VLAN-MEMBERSHIP-MIB", "vmPortStatus"))
)
if mibBuilder.loadTexts:
    vmMembershipGroup.setStatus("deprecated")

vmVQPClientGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 68, 3, 2, 2)
)
vmVQPClientGroup.setObjects(
      *(("CISCO-VLAN-MEMBERSHIP-MIB", "vmVmpsVQPVersion"),
        ("CISCO-VLAN-MEMBERSHIP-MIB", "vmVmpsRetries"),
        ("CISCO-VLAN-MEMBERSHIP-MIB", "vmVmpsReconfirm"),
        ("CISCO-VLAN-MEMBERSHIP-MIB", "vmVmpsReconfirmInterval"),
        ("CISCO-VLAN-MEMBERSHIP-MIB", "vmVmpsReconfirmResult"),
        ("CISCO-VLAN-MEMBERSHIP-MIB", "vmVmpsCurrent"),
        ("CISCO-VLAN-MEMBERSHIP-MIB", "vmVmpsIpAddress"),
        ("CISCO-VLAN-MEMBERSHIP-MIB", "vmVmpsPrimary"),
        ("CISCO-VLAN-MEMBERSHIP-MIB", "vmVmpsRowStatus"),
        ("CISCO-VLAN-MEMBERSHIP-MIB", "vmVQPQueries"),
        ("CISCO-VLAN-MEMBERSHIP-MIB", "vmVQPResponses"),
        ("CISCO-VLAN-MEMBERSHIP-MIB", "vmVmpsChanges"),
        ("CISCO-VLAN-MEMBERSHIP-MIB", "vmVQPShutdown"),
        ("CISCO-VLAN-MEMBERSHIP-MIB", "vmVQPDenied"),
        ("CISCO-VLAN-MEMBERSHIP-MIB", "vmVQPWrongDomain"),
        ("CISCO-VLAN-MEMBERSHIP-MIB", "vmVQPWrongVersion"),
        ("CISCO-VLAN-MEMBERSHIP-MIB", "vmInsufficientResources"))
)
if mibBuilder.loadTexts:
    vmVQPClientGroup.setStatus("current")

vmStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 68, 3, 2, 4)
)
vmStatusGroup.setObjects(
    ("CISCO-VLAN-MEMBERSHIP-MIB", "vmNotificationsEnabled")
)
if mibBuilder.loadTexts:
    vmStatusGroup.setStatus("current")

vmMembershipGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 68, 3, 2, 5)
)
vmMembershipGroup2.setObjects(
      *(("CISCO-VLAN-MEMBERSHIP-MIB", "vmMembershipSummaryMemberPorts"),
        ("CISCO-VLAN-MEMBERSHIP-MIB", "vmVlan"),
        ("CISCO-VLAN-MEMBERSHIP-MIB", "vmVlans"),
        ("CISCO-VLAN-MEMBERSHIP-MIB", "vmVlanType"),
        ("CISCO-VLAN-MEMBERSHIP-MIB", "vmPortStatus"))
)
if mibBuilder.loadTexts:
    vmMembershipGroup2.setStatus("deprecated")

vm4kVlanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 68, 3, 2, 6)
)
vm4kVlanGroup.setObjects(
      *(("CISCO-VLAN-MEMBERSHIP-MIB", "vmVlans2k"),
        ("CISCO-VLAN-MEMBERSHIP-MIB", "vmVlans3k"),
        ("CISCO-VLAN-MEMBERSHIP-MIB", "vmVlans4k"))
)
if mibBuilder.loadTexts:
    vm4kVlanGroup.setStatus("current")

vmVoiceVlanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 68, 3, 2, 7)
)
vmVoiceVlanGroup.setObjects(
    ("CISCO-VLAN-MEMBERSHIP-MIB", "vmVoiceVlanId")
)
if mibBuilder.loadTexts:
    vmVoiceVlanGroup.setStatus("current")

vm1kVlanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 68, 3, 2, 8)
)
vm1kVlanGroup.setObjects(
    ("CISCO-VLAN-MEMBERSHIP-MIB", "vmVlans")
)
if mibBuilder.loadTexts:
    vm1kVlanGroup.setStatus("current")

vmMembershipGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 68, 3, 2, 9)
)
vmMembershipGroup3.setObjects(
      *(("CISCO-VLAN-MEMBERSHIP-MIB", "vmMembershipSummaryMember2kPorts"),
        ("CISCO-VLAN-MEMBERSHIP-MIB", "vmVlan"),
        ("CISCO-VLAN-MEMBERSHIP-MIB", "vmVlanType"),
        ("CISCO-VLAN-MEMBERSHIP-MIB", "vmPortStatus"))
)
if mibBuilder.loadTexts:
    vmMembershipGroup3.setStatus("current")

vmVoiceVlanExtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 68, 3, 2, 10)
)
vmVoiceVlanExtGroup.setObjects(
    ("CISCO-VLAN-MEMBERSHIP-MIB", "vmVoiceVlanCdpVerifyEnable")
)
if mibBuilder.loadTexts:
    vmVoiceVlanExtGroup.setStatus("current")

vmMembershipExtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 68, 3, 2, 11)
)
vmMembershipExtGroup.setObjects(
    ("CISCO-VLAN-MEMBERSHIP-MIB", "vmMembershipSummaryExtPorts")
)
if mibBuilder.loadTexts:
    vmMembershipExtGroup.setStatus("current")

vmVlanCreationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 68, 3, 2, 12)
)
vmVlanCreationGroup.setObjects(
    ("CISCO-VLAN-MEMBERSHIP-MIB", "vmVlanCreationMode")
)
if mibBuilder.loadTexts:
    vmVlanCreationGroup.setStatus("current")


# Notification objects

vmVmpsChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 68, 2, 0, 1)
)
vmVmpsChange.setObjects(
    ("CISCO-VLAN-MEMBERSHIP-MIB", "vmVmpsIpAddress")
)
if mibBuilder.loadTexts:
    vmVmpsChange.setStatus(
        "current"
    )


# Notifications groups

vmVQPNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 68, 3, 2, 3)
)
vmVQPNotificationsGroup.setObjects(
    ("CISCO-VLAN-MEMBERSHIP-MIB", "vmVmpsChange")
)
if mibBuilder.loadTexts:
    vmVQPNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

vmMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 68, 3, 1, 1)
)
if mibBuilder.loadTexts:
    vmMIBCompliance.setStatus(
        "obsolete"
    )

vmMIBCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 68, 3, 1, 2)
)
if mibBuilder.loadTexts:
    vmMIBCompliance2.setStatus(
        "deprecated"
    )

vmMIBCompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 68, 3, 1, 3)
)
if mibBuilder.loadTexts:
    vmMIBCompliance3.setStatus(
        "deprecated"
    )

vmMIBCompliance4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 68, 3, 1, 4)
)
if mibBuilder.loadTexts:
    vmMIBCompliance4.setStatus(
        "deprecated"
    )

vmMIBCompliance5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 68, 3, 1, 5)
)
if mibBuilder.loadTexts:
    vmMIBCompliance5.setStatus(
        "deprecated"
    )

vmMIBCompliance6 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 68, 3, 1, 6)
)
if mibBuilder.loadTexts:
    vmMIBCompliance6.setStatus(
        "deprecated"
    )

vmMIBCompliance7 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 68, 3, 1, 7)
)
if mibBuilder.loadTexts:
    vmMIBCompliance7.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-VLAN-MEMBERSHIP-MIB",
    **{"ciscoVlanMembershipMIB": ciscoVlanMembershipMIB,
       "ciscoVlanMembershipMIBObjects": ciscoVlanMembershipMIBObjects,
       "vmVmps": vmVmps,
       "vmVmpsVQPVersion": vmVmpsVQPVersion,
       "vmVmpsRetries": vmVmpsRetries,
       "vmVmpsReconfirmInterval": vmVmpsReconfirmInterval,
       "vmVmpsReconfirm": vmVmpsReconfirm,
       "vmVmpsReconfirmResult": vmVmpsReconfirmResult,
       "vmVmpsCurrent": vmVmpsCurrent,
       "vmVmpsTable": vmVmpsTable,
       "vmVmpsEntry": vmVmpsEntry,
       "vmVmpsIpAddress": vmVmpsIpAddress,
       "vmVmpsPrimary": vmVmpsPrimary,
       "vmVmpsRowStatus": vmVmpsRowStatus,
       "vmMembership": vmMembership,
       "vmMembershipSummaryTable": vmMembershipSummaryTable,
       "vmMembershipSummaryEntry": vmMembershipSummaryEntry,
       "vmMembershipSummaryVlanIndex": vmMembershipSummaryVlanIndex,
       "vmMembershipSummaryMemberPorts": vmMembershipSummaryMemberPorts,
       "vmMembershipSummaryMember2kPorts": vmMembershipSummaryMember2kPorts,
       "vmMembershipTable": vmMembershipTable,
       "vmMembershipEntry": vmMembershipEntry,
       "vmVlanType": vmVlanType,
       "vmVlan": vmVlan,
       "vmPortStatus": vmPortStatus,
       "vmVlans": vmVlans,
       "vmVlans2k": vmVlans2k,
       "vmVlans3k": vmVlans3k,
       "vmVlans4k": vmVlans4k,
       "vmMembershipSummaryExtTable": vmMembershipSummaryExtTable,
       "vmMembershipSummaryExtEntry": vmMembershipSummaryExtEntry,
       "vmMembershipPortRangeIndex": vmMembershipPortRangeIndex,
       "vmMembershipSummaryExtPorts": vmMembershipSummaryExtPorts,
       "vmVlanCreationMode": vmVlanCreationMode,
       "vmStatistics": vmStatistics,
       "vmVQPQueries": vmVQPQueries,
       "vmVQPResponses": vmVQPResponses,
       "vmVmpsChanges": vmVmpsChanges,
       "vmVQPShutdown": vmVQPShutdown,
       "vmVQPDenied": vmVQPDenied,
       "vmVQPWrongDomain": vmVQPWrongDomain,
       "vmVQPWrongVersion": vmVQPWrongVersion,
       "vmInsufficientResources": vmInsufficientResources,
       "vmStatus": vmStatus,
       "vmNotificationsEnabled": vmNotificationsEnabled,
       "vmVoiceVlan": vmVoiceVlan,
       "vmVoiceVlanTable": vmVoiceVlanTable,
       "vmVoiceVlanEntry": vmVoiceVlanEntry,
       "vmVoiceVlanId": vmVoiceVlanId,
       "vmVoiceVlanCdpVerifyEnable": vmVoiceVlanCdpVerifyEnable,
       "vmNotifications": vmNotifications,
       "vmNotificationsPrefix": vmNotificationsPrefix,
       "vmVmpsChange": vmVmpsChange,
       "vmMIBConformance": vmMIBConformance,
       "vmMIBCompliances": vmMIBCompliances,
       "vmMIBCompliance": vmMIBCompliance,
       "vmMIBCompliance2": vmMIBCompliance2,
       "vmMIBCompliance3": vmMIBCompliance3,
       "vmMIBCompliance4": vmMIBCompliance4,
       "vmMIBCompliance5": vmMIBCompliance5,
       "vmMIBCompliance6": vmMIBCompliance6,
       "vmMIBCompliance7": vmMIBCompliance7,
       "vmMIBGroups": vmMIBGroups,
       "vmMembershipGroup": vmMembershipGroup,
       "vmVQPClientGroup": vmVQPClientGroup,
       "vmVQPNotificationsGroup": vmVQPNotificationsGroup,
       "vmStatusGroup": vmStatusGroup,
       "vmMembershipGroup2": vmMembershipGroup2,
       "vm4kVlanGroup": vm4kVlanGroup,
       "vmVoiceVlanGroup": vmVoiceVlanGroup,
       "vm1kVlanGroup": vm1kVlanGroup,
       "vmMembershipGroup3": vmMembershipGroup3,
       "vmVoiceVlanExtGroup": vmVoiceVlanExtGroup,
       "vmMembershipExtGroup": vmMembershipExtGroup,
       "vmVlanCreationGroup": vmVlanCreationGroup}
)
