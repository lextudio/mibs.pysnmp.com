# SNMP MIB module (CISCO-CABLE-AVAILABILITY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-CABLE-AVAILABILITY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:56:32 2024
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

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoCableAvailabilityMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 242)
)
ciscoCableAvailabilityMIB.setRevisions(
        ("2003-02-20 00:00",
         "2001-11-25 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoCableAvailabilityMIBObjects_ObjectIdentity = ObjectIdentity
ciscoCableAvailabilityMIBObjects = _CiscoCableAvailabilityMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 242, 1)
)
_CcaHCCPObjects_ObjectIdentity = ObjectIdentity
ccaHCCPObjects = _CcaHCCPObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 242, 1, 1)
)


class _CcaHCCPVersion_Type(Integer32):
    """Custom type ccaHCCPVersion based on Integer32"""
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
        *(("others", 1),
          ("version1", 2),
          ("version2", 3),
          ("version3", 4))
    )


_CcaHCCPVersion_Type.__name__ = "Integer32"
_CcaHCCPVersion_Object = MibScalar
ccaHCCPVersion = _CcaHCCPVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 242, 1, 1, 1),
    _CcaHCCPVersion_Type()
)
ccaHCCPVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccaHCCPVersion.setStatus("current")
_CcaHCCPGroupTable_Object = MibTable
ccaHCCPGroupTable = _CcaHCCPGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 242, 1, 1, 2)
)
if mibBuilder.loadTexts:
    ccaHCCPGroupTable.setStatus("current")
_CcaHCCPGroupEntry_Object = MibTableRow
ccaHCCPGroupEntry = _CcaHCCPGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 242, 1, 1, 2, 1)
)
ccaHCCPGroupEntry.setIndexNames(
    (0, "CISCO-CABLE-AVAILABILITY-MIB", "ccaHCCPGroupID"),
)
if mibBuilder.loadTexts:
    ccaHCCPGroupEntry.setStatus("current")


class _CcaHCCPGroupID_Type(Integer32):
    """Custom type ccaHCCPGroupID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_CcaHCCPGroupID_Type.__name__ = "Integer32"
_CcaHCCPGroupID_Object = MibTableColumn
ccaHCCPGroupID = _CcaHCCPGroupID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 242, 1, 1, 2, 1, 1),
    _CcaHCCPGroupID_Type()
)
ccaHCCPGroupID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccaHCCPGroupID.setStatus("current")


class _CcaHCCPGroupAuthentication_Type(Integer32):
    """Custom type ccaHCCPGroupAuthentication based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("md5", 2),
          ("none", 1),
          ("text", 3))
    )


_CcaHCCPGroupAuthentication_Type.__name__ = "Integer32"
_CcaHCCPGroupAuthentication_Object = MibTableColumn
ccaHCCPGroupAuthentication = _CcaHCCPGroupAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 242, 1, 1, 2, 1, 2),
    _CcaHCCPGroupAuthentication_Type()
)
ccaHCCPGroupAuthentication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccaHCCPGroupAuthentication.setStatus("current")
_CcaHCCPGroupAuthKeyChain_Type = SnmpAdminString
_CcaHCCPGroupAuthKeyChain_Object = MibTableColumn
ccaHCCPGroupAuthKeyChain = _CcaHCCPGroupAuthKeyChain_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 242, 1, 1, 2, 1, 3),
    _CcaHCCPGroupAuthKeyChain_Type()
)
ccaHCCPGroupAuthKeyChain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccaHCCPGroupAuthKeyChain.setStatus("current")


class _CcaHCCPGroupHelloTime_Type(Integer32):
    """Custom type ccaHCCPGroupHelloTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(333, 5000),
    )


_CcaHCCPGroupHelloTime_Type.__name__ = "Integer32"
_CcaHCCPGroupHelloTime_Object = MibTableColumn
ccaHCCPGroupHelloTime = _CcaHCCPGroupHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 242, 1, 1, 2, 1, 4),
    _CcaHCCPGroupHelloTime_Type()
)
ccaHCCPGroupHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccaHCCPGroupHelloTime.setStatus("current")
if mibBuilder.loadTexts:
    ccaHCCPGroupHelloTime.setUnits("milliseconds")


class _CcaHCCPGroupHoldTime_Type(Integer32):
    """Custom type ccaHCCPGroupHoldTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 25000),
    )


_CcaHCCPGroupHoldTime_Type.__name__ = "Integer32"
_CcaHCCPGroupHoldTime_Object = MibTableColumn
ccaHCCPGroupHoldTime = _CcaHCCPGroupHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 242, 1, 1, 2, 1, 5),
    _CcaHCCPGroupHoldTime_Type()
)
ccaHCCPGroupHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccaHCCPGroupHoldTime.setStatus("current")
if mibBuilder.loadTexts:
    ccaHCCPGroupHoldTime.setUnits("milliseconds")
_CcaHCCPGroupRevertEnable_Type = TruthValue
_CcaHCCPGroupRevertEnable_Object = MibTableColumn
ccaHCCPGroupRevertEnable = _CcaHCCPGroupRevertEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 242, 1, 1, 2, 1, 6),
    _CcaHCCPGroupRevertEnable_Type()
)
ccaHCCPGroupRevertEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccaHCCPGroupRevertEnable.setStatus("current")
_CcaHCCPGroupProtectIpAddrType_Type = InetAddressType
_CcaHCCPGroupProtectIpAddrType_Object = MibTableColumn
ccaHCCPGroupProtectIpAddrType = _CcaHCCPGroupProtectIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 242, 1, 1, 2, 1, 7),
    _CcaHCCPGroupProtectIpAddrType_Type()
)
ccaHCCPGroupProtectIpAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccaHCCPGroupProtectIpAddrType.setStatus("current")
_CcaHCCPGroupProtectIpAddress_Type = InetAddress
_CcaHCCPGroupProtectIpAddress_Object = MibTableColumn
ccaHCCPGroupProtectIpAddress = _CcaHCCPGroupProtectIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 242, 1, 1, 2, 1, 8),
    _CcaHCCPGroupProtectIpAddress_Type()
)
ccaHCCPGroupProtectIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccaHCCPGroupProtectIpAddress.setStatus("current")
_CcaHCCPGroupIfTable_Object = MibTable
ccaHCCPGroupIfTable = _CcaHCCPGroupIfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 242, 1, 1, 3)
)
if mibBuilder.loadTexts:
    ccaHCCPGroupIfTable.setStatus("current")
_CcaHCCPGroupIfEntry_Object = MibTableRow
ccaHCCPGroupIfEntry = _CcaHCCPGroupIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 242, 1, 1, 3, 1)
)
ccaHCCPGroupIfEntry.setIndexNames(
    (0, "CISCO-CABLE-AVAILABILITY-MIB", "ccaHCCPGroupID"),
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ccaHCCPGroupIfEntry.setStatus("current")


class _CcaHCCPGroupIfStatus_Type(Integer32):
    """Custom type ccaHCCPGroupIfStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("protect", 2),
          ("unknown", 1),
          ("working", 3))
    )


_CcaHCCPGroupIfStatus_Type.__name__ = "Integer32"
_CcaHCCPGroupIfStatus_Object = MibTableColumn
ccaHCCPGroupIfStatus = _CcaHCCPGroupIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 242, 1, 1, 3, 1, 1),
    _CcaHCCPGroupIfStatus_Type()
)
ccaHCCPGroupIfStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccaHCCPGroupIfStatus.setStatus("current")


class _CcaHCCPGroupIfRevertTime_Type(Integer32):
    """Custom type ccaHCCPGroupIfRevertTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CcaHCCPGroupIfRevertTime_Type.__name__ = "Integer32"
_CcaHCCPGroupIfRevertTime_Object = MibTableColumn
ccaHCCPGroupIfRevertTime = _CcaHCCPGroupIfRevertTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 242, 1, 1, 3, 1, 2),
    _CcaHCCPGroupIfRevertTime_Type()
)
ccaHCCPGroupIfRevertTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccaHCCPGroupIfRevertTime.setStatus("current")
_CcaHCCPGroupIfTrackEnable_Type = TruthValue
_CcaHCCPGroupIfTrackEnable_Object = MibTableColumn
ccaHCCPGroupIfTrackEnable = _CcaHCCPGroupIfTrackEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 242, 1, 1, 3, 1, 3),
    _CcaHCCPGroupIfTrackEnable_Type()
)
ccaHCCPGroupIfTrackEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccaHCCPGroupIfTrackEnable.setStatus("current")


class _CcaHCCPGroupIfState_Type(Integer32):
    """Custom type ccaHCCPGroupIfState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("blocking", 2),
          ("forwarding", 1))
    )


_CcaHCCPGroupIfState_Type.__name__ = "Integer32"
_CcaHCCPGroupIfState_Object = MibTableColumn
ccaHCCPGroupIfState = _CcaHCCPGroupIfState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 242, 1, 1, 3, 1, 4),
    _CcaHCCPGroupIfState_Type()
)
ccaHCCPGroupIfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccaHCCPGroupIfState.setStatus("current")


class _CcaHCCPGroupIfLastSwitchReason_Type(Integer32):
    """Custom type ccaHCCPGroupIfLastSwitchReason based on Integer32"""
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
        *(("failBundleDown", 6),
          ("failLinkDown", 5),
          ("failTest", 4),
          ("holdTimeExpire", 2),
          ("hwIfDown", 3),
          ("internal", 7),
          ("none", 1))
    )


_CcaHCCPGroupIfLastSwitchReason_Type.__name__ = "Integer32"
_CcaHCCPGroupIfLastSwitchReason_Object = MibTableColumn
ccaHCCPGroupIfLastSwitchReason = _CcaHCCPGroupIfLastSwitchReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 242, 1, 1, 3, 1, 5),
    _CcaHCCPGroupIfLastSwitchReason_Type()
)
ccaHCCPGroupIfLastSwitchReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccaHCCPGroupIfLastSwitchReason.setStatus("current")
_CcaHCCPGroupIfOnTransitions_Type = Counter32
_CcaHCCPGroupIfOnTransitions_Object = MibTableColumn
ccaHCCPGroupIfOnTransitions = _CcaHCCPGroupIfOnTransitions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 242, 1, 1, 3, 1, 6),
    _CcaHCCPGroupIfOnTransitions_Type()
)
ccaHCCPGroupIfOnTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccaHCCPGroupIfOnTransitions.setStatus("current")
_CcaHCCPGroupIfOffTransitions_Type = Counter32
_CcaHCCPGroupIfOffTransitions_Object = MibTableColumn
ccaHCCPGroupIfOffTransitions = _CcaHCCPGroupIfOffTransitions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 242, 1, 1, 3, 1, 7),
    _CcaHCCPGroupIfOffTransitions_Type()
)
ccaHCCPGroupIfOffTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccaHCCPGroupIfOffTransitions.setStatus("current")
_CcaHCCPGroupTrackInterfaceTable_Object = MibTable
ccaHCCPGroupTrackInterfaceTable = _CcaHCCPGroupTrackInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 242, 1, 1, 4)
)
if mibBuilder.loadTexts:
    ccaHCCPGroupTrackInterfaceTable.setStatus("current")
_CcaHCCPGroupTrackInterfaceEntry_Object = MibTableRow
ccaHCCPGroupTrackInterfaceEntry = _CcaHCCPGroupTrackInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 242, 1, 1, 4, 1)
)
ccaHCCPGroupTrackInterfaceEntry.setIndexNames(
    (0, "CISCO-CABLE-AVAILABILITY-MIB", "ccaHCCPGroupID"),
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-CABLE-AVAILABILITY-MIB", "ccaHCCPGroupTrackIfID"),
)
if mibBuilder.loadTexts:
    ccaHCCPGroupTrackInterfaceEntry.setStatus("current")


class _CcaHCCPGroupTrackIfID_Type(Integer32):
    """Custom type ccaHCCPGroupTrackIfID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CcaHCCPGroupTrackIfID_Type.__name__ = "Integer32"
_CcaHCCPGroupTrackIfID_Object = MibTableColumn
ccaHCCPGroupTrackIfID = _CcaHCCPGroupTrackIfID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 242, 1, 1, 4, 1, 1),
    _CcaHCCPGroupTrackIfID_Type()
)
ccaHCCPGroupTrackIfID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccaHCCPGroupTrackIfID.setStatus("current")


class _CcaHCCPGroupTrackIfDescr_Type(DisplayString):
    """Custom type ccaHCCPGroupTrackIfDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CcaHCCPGroupTrackIfDescr_Type.__name__ = "DisplayString"
_CcaHCCPGroupTrackIfDescr_Object = MibTableColumn
ccaHCCPGroupTrackIfDescr = _CcaHCCPGroupTrackIfDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 242, 1, 1, 4, 1, 2),
    _CcaHCCPGroupTrackIfDescr_Type()
)
ccaHCCPGroupTrackIfDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccaHCCPGroupTrackIfDescr.setStatus("current")
_CcaHCCPMemberTable_Object = MibTable
ccaHCCPMemberTable = _CcaHCCPMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 242, 1, 1, 5)
)
if mibBuilder.loadTexts:
    ccaHCCPMemberTable.setStatus("current")
_CcaHCCPMemberEntry_Object = MibTableRow
ccaHCCPMemberEntry = _CcaHCCPMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 242, 1, 1, 5, 1)
)
ccaHCCPMemberEntry.setIndexNames(
    (0, "CISCO-CABLE-AVAILABILITY-MIB", "ccaHCCPGroupID"),
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-CABLE-AVAILABILITY-MIB", "ccaHCCPMemberID"),
)
if mibBuilder.loadTexts:
    ccaHCCPMemberEntry.setStatus("current")


class _CcaHCCPMemberID_Type(Integer32):
    """Custom type ccaHCCPMemberID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_CcaHCCPMemberID_Type.__name__ = "Integer32"
_CcaHCCPMemberID_Object = MibTableColumn
ccaHCCPMemberID = _CcaHCCPMemberID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 242, 1, 1, 5, 1, 1),
    _CcaHCCPMemberID_Type()
)
ccaHCCPMemberID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccaHCCPMemberID.setStatus("current")
_CcaHCCPMemberIpAddrType_Type = InetAddressType
_CcaHCCPMemberIpAddrType_Object = MibTableColumn
ccaHCCPMemberIpAddrType = _CcaHCCPMemberIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 242, 1, 1, 5, 1, 2),
    _CcaHCCPMemberIpAddrType_Type()
)
ccaHCCPMemberIpAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccaHCCPMemberIpAddrType.setStatus("current")
_CcaHCCPMemberIpAddress_Type = InetAddress
_CcaHCCPMemberIpAddress_Object = MibTableColumn
ccaHCCPMemberIpAddress = _CcaHCCPMemberIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 242, 1, 1, 5, 1, 3),
    _CcaHCCPMemberIpAddress_Type()
)
ccaHCCPMemberIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccaHCCPMemberIpAddress.setStatus("current")


class _CcaHCCPMemberState_Type(Integer32):
    """Custom type ccaHCCPMemberState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("nonFunctional", 3),
          ("standby", 2))
    )


_CcaHCCPMemberState_Type.__name__ = "Integer32"
_CcaHCCPMemberState_Object = MibTableColumn
ccaHCCPMemberState = _CcaHCCPMemberState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 242, 1, 1, 5, 1, 4),
    _CcaHCCPMemberState_Type()
)
ccaHCCPMemberState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccaHCCPMemberState.setStatus("current")
_CcaHCCPMemberSwitchNow_Type = TruthValue
_CcaHCCPMemberSwitchNow_Object = MibTableColumn
ccaHCCPMemberSwitchNow = _CcaHCCPMemberSwitchNow_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 242, 1, 1, 5, 1, 5),
    _CcaHCCPMemberSwitchNow_Type()
)
ccaHCCPMemberSwitchNow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccaHCCPMemberSwitchNow.setStatus("current")
_CcaHCCPMemChanSwitchTable_Object = MibTable
ccaHCCPMemChanSwitchTable = _CcaHCCPMemChanSwitchTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 242, 1, 1, 6)
)
if mibBuilder.loadTexts:
    ccaHCCPMemChanSwitchTable.setStatus("current")
_CcaHCCPMemChanSwitchEntry_Object = MibTableRow
ccaHCCPMemChanSwitchEntry = _CcaHCCPMemChanSwitchEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 242, 1, 1, 6, 1)
)
ccaHCCPMemChanSwitchEntry.setIndexNames(
    (0, "CISCO-CABLE-AVAILABILITY-MIB", "ccaHCCPGroupID"),
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-CABLE-AVAILABILITY-MIB", "ccaHCCPMemberID"),
    (0, "CISCO-CABLE-AVAILABILITY-MIB", "ccaHCCPMemChanSwitchID"),
)
if mibBuilder.loadTexts:
    ccaHCCPMemChanSwitchEntry.setStatus("current")


class _CcaHCCPMemChanSwitchID_Type(Integer32):
    """Custom type ccaHCCPMemChanSwitchID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CcaHCCPMemChanSwitchID_Type.__name__ = "Integer32"
_CcaHCCPMemChanSwitchID_Object = MibTableColumn
ccaHCCPMemChanSwitchID = _CcaHCCPMemChanSwitchID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 242, 1, 1, 6, 1, 1),
    _CcaHCCPMemChanSwitchID_Type()
)
ccaHCCPMemChanSwitchID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccaHCCPMemChanSwitchID.setStatus("current")


class _CcaHCCPMemChanSwitchType_Type(Integer32):
    """Custom type ccaHCCPMemChanSwitchType based on Integer32"""
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
        *(("others", 1),
          ("rfSwitchGrp", 3),
          ("rfSwitchModule", 4),
          ("ucWavecom", 2))
    )


_CcaHCCPMemChanSwitchType_Type.__name__ = "Integer32"
_CcaHCCPMemChanSwitchType_Object = MibTableColumn
ccaHCCPMemChanSwitchType = _CcaHCCPMemChanSwitchType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 242, 1, 1, 6, 1, 2),
    _CcaHCCPMemChanSwitchType_Type()
)
ccaHCCPMemChanSwitchType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccaHCCPMemChanSwitchType.setStatus("current")
_CcaHCCPMemChanSwitchIpAddrType_Type = InetAddressType
_CcaHCCPMemChanSwitchIpAddrType_Object = MibTableColumn
ccaHCCPMemChanSwitchIpAddrType = _CcaHCCPMemChanSwitchIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 242, 1, 1, 6, 1, 3),
    _CcaHCCPMemChanSwitchIpAddrType_Type()
)
ccaHCCPMemChanSwitchIpAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccaHCCPMemChanSwitchIpAddrType.setStatus("current")
_CcaHCCPMemChanSwitchIpAddress_Type = InetAddress
_CcaHCCPMemChanSwitchIpAddress_Object = MibTableColumn
ccaHCCPMemChanSwitchIpAddress = _CcaHCCPMemChanSwitchIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 242, 1, 1, 6, 1, 4),
    _CcaHCCPMemChanSwitchIpAddress_Type()
)
ccaHCCPMemChanSwitchIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccaHCCPMemChanSwitchIpAddress.setStatus("current")


class _CcaHCCPMemChanSwitchModule_Type(Integer32):
    """Custom type ccaHCCPMemChanSwitchModule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_CcaHCCPMemChanSwitchModule_Type.__name__ = "Integer32"
_CcaHCCPMemChanSwitchModule_Object = MibTableColumn
ccaHCCPMemChanSwitchModule = _CcaHCCPMemChanSwitchModule_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 242, 1, 1, 6, 1, 5),
    _CcaHCCPMemChanSwitchModule_Type()
)
ccaHCCPMemChanSwitchModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccaHCCPMemChanSwitchModule.setStatus("current")
_CcaHCCPMemChanSwitchProtIpAddrType_Type = InetAddressType
_CcaHCCPMemChanSwitchProtIpAddrType_Object = MibTableColumn
ccaHCCPMemChanSwitchProtIpAddrType = _CcaHCCPMemChanSwitchProtIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 242, 1, 1, 6, 1, 6),
    _CcaHCCPMemChanSwitchProtIpAddrType_Type()
)
ccaHCCPMemChanSwitchProtIpAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccaHCCPMemChanSwitchProtIpAddrType.setStatus("current")
_CcaHCCPMemChanSwitchProtIpAddr_Type = InetAddress
_CcaHCCPMemChanSwitchProtIpAddr_Object = MibTableColumn
ccaHCCPMemChanSwitchProtIpAddr = _CcaHCCPMemChanSwitchProtIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 242, 1, 1, 6, 1, 7),
    _CcaHCCPMemChanSwitchProtIpAddr_Type()
)
ccaHCCPMemChanSwitchProtIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccaHCCPMemChanSwitchProtIpAddr.setStatus("current")


class _CcaHCCPMemChanSwitchProtModule_Type(Integer32):
    """Custom type ccaHCCPMemChanSwitchProtModule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_CcaHCCPMemChanSwitchProtModule_Type.__name__ = "Integer32"
_CcaHCCPMemChanSwitchProtModule_Object = MibTableColumn
ccaHCCPMemChanSwitchProtModule = _CcaHCCPMemChanSwitchProtModule_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 242, 1, 1, 6, 1, 8),
    _CcaHCCPMemChanSwitchProtModule_Type()
)
ccaHCCPMemChanSwitchProtModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccaHCCPMemChanSwitchProtModule.setStatus("current")


class _CcaHCCPMemChanSwitchPosition_Type(Integer32):
    """Custom type ccaHCCPMemChanSwitchPosition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_CcaHCCPMemChanSwitchPosition_Type.__name__ = "Integer32"
_CcaHCCPMemChanSwitchPosition_Object = MibTableColumn
ccaHCCPMemChanSwitchPosition = _CcaHCCPMemChanSwitchPosition_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 242, 1, 1, 6, 1, 9),
    _CcaHCCPMemChanSwitchPosition_Type()
)
ccaHCCPMemChanSwitchPosition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccaHCCPMemChanSwitchPosition.setStatus("current")
_CcaHCCPMemChanSwitchSnmpEnable_Type = TruthValue
_CcaHCCPMemChanSwitchSnmpEnable_Object = MibTableColumn
ccaHCCPMemChanSwitchSnmpEnable = _CcaHCCPMemChanSwitchSnmpEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 242, 1, 1, 6, 1, 10),
    _CcaHCCPMemChanSwitchSnmpEnable_Type()
)
ccaHCCPMemChanSwitchSnmpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccaHCCPMemChanSwitchSnmpEnable.setStatus("current")


class _CcaHCCPOnOffNotificationEnable_Type(TruthValue):
    """Custom type ccaHCCPOnOffNotificationEnable based on TruthValue"""


_CcaHCCPOnOffNotificationEnable_Object = MibScalar
ccaHCCPOnOffNotificationEnable = _CcaHCCPOnOffNotificationEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 242, 1, 1, 7),
    _CcaHCCPOnOffNotificationEnable_Type()
)
ccaHCCPOnOffNotificationEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccaHCCPOnOffNotificationEnable.setStatus("current")
_CiscoCableAvailabilityMIBNotificationsPrefix_ObjectIdentity = ObjectIdentity
ciscoCableAvailabilityMIBNotificationsPrefix = _CiscoCableAvailabilityMIBNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 242, 2)
)
_CiscoCableAvailabilityMIBNotifications_ObjectIdentity = ObjectIdentity
ciscoCableAvailabilityMIBNotifications = _CiscoCableAvailabilityMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 242, 2, 0)
)
_CiscoCableAvailabilityMIBConformance_ObjectIdentity = ObjectIdentity
ciscoCableAvailabilityMIBConformance = _CiscoCableAvailabilityMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 242, 3)
)
_CiscoCableAvailabilityMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoCableAvailabilityMIBCompliances = _CiscoCableAvailabilityMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 242, 3, 1)
)
_CiscoCableAvailabilityMIBGroups_ObjectIdentity = ObjectIdentity
ciscoCableAvailabilityMIBGroups = _CiscoCableAvailabilityMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 242, 3, 2)
)

# Managed Objects groups

ccaHCCPGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 242, 3, 2, 1)
)
ccaHCCPGroup.setObjects(
      *(("CISCO-CABLE-AVAILABILITY-MIB", "ccaHCCPVersion"),
        ("CISCO-CABLE-AVAILABILITY-MIB", "ccaHCCPOnOffNotificationEnable"),
        ("CISCO-CABLE-AVAILABILITY-MIB", "ccaHCCPGroupAuthentication"),
        ("CISCO-CABLE-AVAILABILITY-MIB", "ccaHCCPGroupAuthKeyChain"),
        ("CISCO-CABLE-AVAILABILITY-MIB", "ccaHCCPGroupHelloTime"),
        ("CISCO-CABLE-AVAILABILITY-MIB", "ccaHCCPGroupHoldTime"),
        ("CISCO-CABLE-AVAILABILITY-MIB", "ccaHCCPGroupRevertEnable"),
        ("CISCO-CABLE-AVAILABILITY-MIB", "ccaHCCPGroupProtectIpAddrType"),
        ("CISCO-CABLE-AVAILABILITY-MIB", "ccaHCCPGroupProtectIpAddress"),
        ("CISCO-CABLE-AVAILABILITY-MIB", "ccaHCCPGroupIfRevertTime"),
        ("CISCO-CABLE-AVAILABILITY-MIB", "ccaHCCPGroupIfTrackEnable"),
        ("CISCO-CABLE-AVAILABILITY-MIB", "ccaHCCPGroupIfStatus"),
        ("CISCO-CABLE-AVAILABILITY-MIB", "ccaHCCPGroupIfLastSwitchReason"),
        ("CISCO-CABLE-AVAILABILITY-MIB", "ccaHCCPGroupIfOnTransitions"),
        ("CISCO-CABLE-AVAILABILITY-MIB", "ccaHCCPGroupIfOffTransitions"),
        ("CISCO-CABLE-AVAILABILITY-MIB", "ccaHCCPGroupTrackIfDescr"),
        ("CISCO-CABLE-AVAILABILITY-MIB", "ccaHCCPGroupIfState"))
)
if mibBuilder.loadTexts:
    ccaHCCPGroup.setStatus("current")

ccaHCCPMemberGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 242, 3, 2, 2)
)
ccaHCCPMemberGroup.setObjects(
      *(("CISCO-CABLE-AVAILABILITY-MIB", "ccaHCCPMemberIpAddrType"),
        ("CISCO-CABLE-AVAILABILITY-MIB", "ccaHCCPMemberIpAddress"),
        ("CISCO-CABLE-AVAILABILITY-MIB", "ccaHCCPMemberState"),
        ("CISCO-CABLE-AVAILABILITY-MIB", "ccaHCCPMemberSwitchNow"),
        ("CISCO-CABLE-AVAILABILITY-MIB", "ccaHCCPMemChanSwitchType"),
        ("CISCO-CABLE-AVAILABILITY-MIB", "ccaHCCPMemChanSwitchIpAddrType"),
        ("CISCO-CABLE-AVAILABILITY-MIB", "ccaHCCPMemChanSwitchIpAddress"),
        ("CISCO-CABLE-AVAILABILITY-MIB", "ccaHCCPMemChanSwitchModule"),
        ("CISCO-CABLE-AVAILABILITY-MIB", "ccaHCCPMemChanSwitchProtIpAddrType"),
        ("CISCO-CABLE-AVAILABILITY-MIB", "ccaHCCPMemChanSwitchProtIpAddr"),
        ("CISCO-CABLE-AVAILABILITY-MIB", "ccaHCCPMemChanSwitchProtModule"),
        ("CISCO-CABLE-AVAILABILITY-MIB", "ccaHCCPMemChanSwitchPosition"),
        ("CISCO-CABLE-AVAILABILITY-MIB", "ccaHCCPMemChanSwitchSnmpEnable"))
)
if mibBuilder.loadTexts:
    ccaHCCPMemberGroup.setStatus("current")


# Notification objects

ccaHCCPOnNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 242, 2, 0, 1)
)
ccaHCCPOnNotification.setObjects(
      *(("CISCO-CABLE-AVAILABILITY-MIB", "ccaHCCPGroupIfStatus"),
        ("CISCO-CABLE-AVAILABILITY-MIB", "ccaHCCPGroupIfLastSwitchReason"),
        ("CISCO-CABLE-AVAILABILITY-MIB", "ccaHCCPMemberState"))
)
if mibBuilder.loadTexts:
    ccaHCCPOnNotification.setStatus(
        "current"
    )

ccaHCCPOffNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 242, 2, 0, 2)
)
ccaHCCPOffNotification.setObjects(
      *(("CISCO-CABLE-AVAILABILITY-MIB", "ccaHCCPGroupIfStatus"),
        ("CISCO-CABLE-AVAILABILITY-MIB", "ccaHCCPGroupIfLastSwitchReason"),
        ("CISCO-CABLE-AVAILABILITY-MIB", "ccaHCCPMemberState"))
)
if mibBuilder.loadTexts:
    ccaHCCPOffNotification.setStatus(
        "current"
    )


# Notifications groups

ccaHCCPNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 242, 3, 2, 3)
)
ccaHCCPNotificationGroup.setObjects(
      *(("CISCO-CABLE-AVAILABILITY-MIB", "ccaHCCPOnNotification"),
        ("CISCO-CABLE-AVAILABILITY-MIB", "ccaHCCPOffNotification"))
)
if mibBuilder.loadTexts:
    ccaHCCPNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoCableAvailabilityCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 242, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoCableAvailabilityCompliance.setStatus(
        "deprecated"
    )

ciscoCableAvailabilityComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 242, 3, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoCableAvailabilityComplianceRev1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-CABLE-AVAILABILITY-MIB",
    **{"ciscoCableAvailabilityMIB": ciscoCableAvailabilityMIB,
       "ciscoCableAvailabilityMIBObjects": ciscoCableAvailabilityMIBObjects,
       "ccaHCCPObjects": ccaHCCPObjects,
       "ccaHCCPVersion": ccaHCCPVersion,
       "ccaHCCPGroupTable": ccaHCCPGroupTable,
       "ccaHCCPGroupEntry": ccaHCCPGroupEntry,
       "ccaHCCPGroupID": ccaHCCPGroupID,
       "ccaHCCPGroupAuthentication": ccaHCCPGroupAuthentication,
       "ccaHCCPGroupAuthKeyChain": ccaHCCPGroupAuthKeyChain,
       "ccaHCCPGroupHelloTime": ccaHCCPGroupHelloTime,
       "ccaHCCPGroupHoldTime": ccaHCCPGroupHoldTime,
       "ccaHCCPGroupRevertEnable": ccaHCCPGroupRevertEnable,
       "ccaHCCPGroupProtectIpAddrType": ccaHCCPGroupProtectIpAddrType,
       "ccaHCCPGroupProtectIpAddress": ccaHCCPGroupProtectIpAddress,
       "ccaHCCPGroupIfTable": ccaHCCPGroupIfTable,
       "ccaHCCPGroupIfEntry": ccaHCCPGroupIfEntry,
       "ccaHCCPGroupIfStatus": ccaHCCPGroupIfStatus,
       "ccaHCCPGroupIfRevertTime": ccaHCCPGroupIfRevertTime,
       "ccaHCCPGroupIfTrackEnable": ccaHCCPGroupIfTrackEnable,
       "ccaHCCPGroupIfState": ccaHCCPGroupIfState,
       "ccaHCCPGroupIfLastSwitchReason": ccaHCCPGroupIfLastSwitchReason,
       "ccaHCCPGroupIfOnTransitions": ccaHCCPGroupIfOnTransitions,
       "ccaHCCPGroupIfOffTransitions": ccaHCCPGroupIfOffTransitions,
       "ccaHCCPGroupTrackInterfaceTable": ccaHCCPGroupTrackInterfaceTable,
       "ccaHCCPGroupTrackInterfaceEntry": ccaHCCPGroupTrackInterfaceEntry,
       "ccaHCCPGroupTrackIfID": ccaHCCPGroupTrackIfID,
       "ccaHCCPGroupTrackIfDescr": ccaHCCPGroupTrackIfDescr,
       "ccaHCCPMemberTable": ccaHCCPMemberTable,
       "ccaHCCPMemberEntry": ccaHCCPMemberEntry,
       "ccaHCCPMemberID": ccaHCCPMemberID,
       "ccaHCCPMemberIpAddrType": ccaHCCPMemberIpAddrType,
       "ccaHCCPMemberIpAddress": ccaHCCPMemberIpAddress,
       "ccaHCCPMemberState": ccaHCCPMemberState,
       "ccaHCCPMemberSwitchNow": ccaHCCPMemberSwitchNow,
       "ccaHCCPMemChanSwitchTable": ccaHCCPMemChanSwitchTable,
       "ccaHCCPMemChanSwitchEntry": ccaHCCPMemChanSwitchEntry,
       "ccaHCCPMemChanSwitchID": ccaHCCPMemChanSwitchID,
       "ccaHCCPMemChanSwitchType": ccaHCCPMemChanSwitchType,
       "ccaHCCPMemChanSwitchIpAddrType": ccaHCCPMemChanSwitchIpAddrType,
       "ccaHCCPMemChanSwitchIpAddress": ccaHCCPMemChanSwitchIpAddress,
       "ccaHCCPMemChanSwitchModule": ccaHCCPMemChanSwitchModule,
       "ccaHCCPMemChanSwitchProtIpAddrType": ccaHCCPMemChanSwitchProtIpAddrType,
       "ccaHCCPMemChanSwitchProtIpAddr": ccaHCCPMemChanSwitchProtIpAddr,
       "ccaHCCPMemChanSwitchProtModule": ccaHCCPMemChanSwitchProtModule,
       "ccaHCCPMemChanSwitchPosition": ccaHCCPMemChanSwitchPosition,
       "ccaHCCPMemChanSwitchSnmpEnable": ccaHCCPMemChanSwitchSnmpEnable,
       "ccaHCCPOnOffNotificationEnable": ccaHCCPOnOffNotificationEnable,
       "ciscoCableAvailabilityMIBNotificationsPrefix": ciscoCableAvailabilityMIBNotificationsPrefix,
       "ciscoCableAvailabilityMIBNotifications": ciscoCableAvailabilityMIBNotifications,
       "ccaHCCPOnNotification": ccaHCCPOnNotification,
       "ccaHCCPOffNotification": ccaHCCPOffNotification,
       "ciscoCableAvailabilityMIBConformance": ciscoCableAvailabilityMIBConformance,
       "ciscoCableAvailabilityMIBCompliances": ciscoCableAvailabilityMIBCompliances,
       "ciscoCableAvailabilityCompliance": ciscoCableAvailabilityCompliance,
       "ciscoCableAvailabilityComplianceRev1": ciscoCableAvailabilityComplianceRev1,
       "ciscoCableAvailabilityMIBGroups": ciscoCableAvailabilityMIBGroups,
       "ccaHCCPGroup": ccaHCCPGroup,
       "ccaHCCPMemberGroup": ccaHCCPMemberGroup,
       "ccaHCCPNotificationGroup": ccaHCCPNotificationGroup}
)
