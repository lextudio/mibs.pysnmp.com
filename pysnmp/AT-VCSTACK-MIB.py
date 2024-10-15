# SNMP MIB module (AT-VCSTACK-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/AT-VCSTACK-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:43:37 2024
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

(sysinfo,) = mibBuilder.importSymbols(
    "AT-SMI-MIB",
    "sysinfo")

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
 MacAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

vcstack = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13)
)
vcstack.setRevisions(
        ("2011-11-03 00:00",
         "2010-09-07 00:00",
         "2010-09-03 00:00",
         "2010-06-15 00:15",
         "2010-05-24 01:19",
         "2010-01-15 00:39",
         "2009-11-05 00:00",
         "2009-06-08 00:00",
         "2009-01-20 00:00",
         "2008-03-19 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_VcstackNotifications_ObjectIdentity = ObjectIdentity
vcstackNotifications = _VcstackNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 0)
)


class _VcstackNbrMemberIdNotify_Type(Unsigned32):
    """Custom type vcstackNbrMemberIdNotify based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_VcstackNbrMemberIdNotify_Type.__name__ = "Unsigned32"
_VcstackNbrMemberIdNotify_Object = MibScalar
vcstackNbrMemberIdNotify = _VcstackNbrMemberIdNotify_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 0, 8),
    _VcstackNbrMemberIdNotify_Type()
)
vcstackNbrMemberIdNotify.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vcstackNbrMemberIdNotify.setStatus("current")
_VcstackStkPortNameNotify_Type = DisplayString
_VcstackStkPortNameNotify_Object = MibScalar
vcstackStkPortNameNotify = _VcstackStkPortNameNotify_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 0, 9),
    _VcstackStkPortNameNotify_Type()
)
vcstackStkPortNameNotify.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vcstackStkPortNameNotify.setStatus("current")


class _VcstackStatus_Type(Integer32):
    """Custom type vcstackStatus based on Integer32"""
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
        *(("normalOperation", 1),
          ("operatingInFailoverState", 2),
          ("ringTopologyBroken", 4),
          ("standaloneUnit", 3))
    )


_VcstackStatus_Type.__name__ = "Integer32"
_VcstackStatus_Object = MibScalar
vcstackStatus = _VcstackStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 1),
    _VcstackStatus_Type()
)
vcstackStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcstackStatus.setStatus("current")


class _VcstackOperationalStatus_Type(Integer32):
    """Custom type vcstackOperationalStatus based on Integer32"""
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


_VcstackOperationalStatus_Type.__name__ = "Integer32"
_VcstackOperationalStatus_Object = MibScalar
vcstackOperationalStatus = _VcstackOperationalStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 2),
    _VcstackOperationalStatus_Type()
)
vcstackOperationalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcstackOperationalStatus.setStatus("current")
_VcstackMgmtVlanId_Type = Integer32
_VcstackMgmtVlanId_Object = MibScalar
vcstackMgmtVlanId = _VcstackMgmtVlanId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 3),
    _VcstackMgmtVlanId_Type()
)
vcstackMgmtVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcstackMgmtVlanId.setStatus("current")
_VcstackMgmtVlanSubnetAddr_Type = IpAddress
_VcstackMgmtVlanSubnetAddr_Object = MibScalar
vcstackMgmtVlanSubnetAddr = _VcstackMgmtVlanSubnetAddr_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 4),
    _VcstackMgmtVlanSubnetAddr_Type()
)
vcstackMgmtVlanSubnetAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcstackMgmtVlanSubnetAddr.setStatus("current")
_VcstackTable_Object = MibTable
vcstackTable = _VcstackTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 5)
)
if mibBuilder.loadTexts:
    vcstackTable.setStatus("current")
_VcstackEntry_Object = MibTableRow
vcstackEntry = _VcstackEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 5, 1)
)
vcstackEntry.setIndexNames(
    (0, "AT-VCSTACK-MIB", "vcstackId"),
)
if mibBuilder.loadTexts:
    vcstackEntry.setStatus("current")


class _VcstackId_Type(Unsigned32):
    """Custom type vcstackId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_VcstackId_Type.__name__ = "Unsigned32"
_VcstackId_Object = MibTableColumn
vcstackId = _VcstackId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 5, 1, 1),
    _VcstackId_Type()
)
vcstackId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcstackId.setStatus("current")


class _VcstackPendingId_Type(Unsigned32):
    """Custom type vcstackPendingId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_VcstackPendingId_Type.__name__ = "Unsigned32"
_VcstackPendingId_Object = MibTableColumn
vcstackPendingId = _VcstackPendingId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 5, 1, 2),
    _VcstackPendingId_Type()
)
vcstackPendingId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcstackPendingId.setStatus("current")
_VcstackMacAddr_Type = MacAddress
_VcstackMacAddr_Object = MibTableColumn
vcstackMacAddr = _VcstackMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 5, 1, 3),
    _VcstackMacAddr_Type()
)
vcstackMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcstackMacAddr.setStatus("current")


class _VcstackPriority_Type(Unsigned32):
    """Custom type vcstackPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VcstackPriority_Type.__name__ = "Unsigned32"
_VcstackPriority_Object = MibTableColumn
vcstackPriority = _VcstackPriority_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 5, 1, 4),
    _VcstackPriority_Type()
)
vcstackPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcstackPriority.setStatus("current")


class _VcstackRole_Type(Integer32):
    """Custom type vcstackRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("activeMaster", 8),
          ("backupMember", 4),
          ("disabledMaster", 6),
          ("discovering", 2),
          ("fallbackMaster", 7),
          ("leaving", 1),
          ("pendingMaster", 5),
          ("synchronizing", 3))
    )


_VcstackRole_Type.__name__ = "Integer32"
_VcstackRole_Object = MibTableColumn
vcstackRole = _VcstackRole_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 5, 1, 5),
    _VcstackRole_Type()
)
vcstackRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcstackRole.setStatus("current")
_VcstackLastRoleChange_Type = DisplayString
_VcstackLastRoleChange_Object = MibTableColumn
vcstackLastRoleChange = _VcstackLastRoleChange_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 5, 1, 6),
    _VcstackLastRoleChange_Type()
)
vcstackLastRoleChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcstackLastRoleChange.setStatus("current")
_VcstackHostname_Type = DisplayString
_VcstackHostname_Object = MibTableColumn
vcstackHostname = _VcstackHostname_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 5, 1, 7),
    _VcstackHostname_Type()
)
vcstackHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcstackHostname.setStatus("current")
_VcstackProductType_Type = DisplayString
_VcstackProductType_Object = MibTableColumn
vcstackProductType = _VcstackProductType_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 5, 1, 8),
    _VcstackProductType_Type()
)
vcstackProductType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcstackProductType.setStatus("current")
_VcstackSWVersionAutoSync_Type = TruthValue
_VcstackSWVersionAutoSync_Object = MibTableColumn
vcstackSWVersionAutoSync = _VcstackSWVersionAutoSync_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 5, 1, 9),
    _VcstackSWVersionAutoSync_Type()
)
vcstackSWVersionAutoSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcstackSWVersionAutoSync.setStatus("current")


class _VcstackFallbackConfigStatus_Type(Integer32):
    """Custom type vcstackFallbackConfigStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fileExists", 1),
          ("fileNotFound", 2),
          ("notConfigured", 3))
    )


_VcstackFallbackConfigStatus_Type.__name__ = "Integer32"
_VcstackFallbackConfigStatus_Object = MibTableColumn
vcstackFallbackConfigStatus = _VcstackFallbackConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 5, 1, 10),
    _VcstackFallbackConfigStatus_Type()
)
vcstackFallbackConfigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcstackFallbackConfigStatus.setStatus("obsolete")
_VcstackFallbackConfigFilename_Type = DisplayString
_VcstackFallbackConfigFilename_Object = MibTableColumn
vcstackFallbackConfigFilename = _VcstackFallbackConfigFilename_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 5, 1, 11),
    _VcstackFallbackConfigFilename_Type()
)
vcstackFallbackConfigFilename.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcstackFallbackConfigFilename.setStatus("obsolete")


class _VcstackResiliencyLinkStatus_Type(Integer32):
    """Custom type vcstackResiliencyLinkStatus based on Integer32"""
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
        *(("configured", 1),
          ("failed", 3),
          ("notConfigured", 4),
          ("stopped", 5),
          ("successful", 2))
    )


_VcstackResiliencyLinkStatus_Type.__name__ = "Integer32"
_VcstackResiliencyLinkStatus_Object = MibTableColumn
vcstackResiliencyLinkStatus = _VcstackResiliencyLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 5, 1, 12),
    _VcstackResiliencyLinkStatus_Type()
)
vcstackResiliencyLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcstackResiliencyLinkStatus.setStatus("current")
_VcstackResiliencyLinkInterfaceName_Type = DisplayString
_VcstackResiliencyLinkInterfaceName_Object = MibTableColumn
vcstackResiliencyLinkInterfaceName = _VcstackResiliencyLinkInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 5, 1, 13),
    _VcstackResiliencyLinkInterfaceName_Type()
)
vcstackResiliencyLinkInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcstackResiliencyLinkInterfaceName.setStatus("current")


class _VcstackActiveStkHardware_Type(Integer32):
    """Custom type vcstackActiveStkHardware based on Integer32"""
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
        *(("builtinStackingPorts", 2),
          ("none", 3),
          ("stackXG", 4),
          ("x6EMXS2", 5),
          ("xemStk", 1))
    )


_VcstackActiveStkHardware_Type.__name__ = "Integer32"
_VcstackActiveStkHardware_Object = MibTableColumn
vcstackActiveStkHardware = _VcstackActiveStkHardware_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 5, 1, 14),
    _VcstackActiveStkHardware_Type()
)
vcstackActiveStkHardware.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcstackActiveStkHardware.setStatus("current")


class _VcstackStkPort1Status_Type(Integer32):
    """Custom type vcstackStkPort1Status based on Integer32"""
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
        *(("discoveringNeighbour", 3),
          ("down", 1),
          ("learntNeighbour", 4),
          ("neighbourIncompatible", 2))
    )


_VcstackStkPort1Status_Type.__name__ = "Integer32"
_VcstackStkPort1Status_Object = MibTableColumn
vcstackStkPort1Status = _VcstackStkPort1Status_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 5, 1, 15),
    _VcstackStkPort1Status_Type()
)
vcstackStkPort1Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcstackStkPort1Status.setStatus("current")


class _VcstackStkPort1NeighbourId_Type(Unsigned32):
    """Custom type vcstackStkPort1NeighbourId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_VcstackStkPort1NeighbourId_Type.__name__ = "Unsigned32"
_VcstackStkPort1NeighbourId_Object = MibTableColumn
vcstackStkPort1NeighbourId = _VcstackStkPort1NeighbourId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 5, 1, 16),
    _VcstackStkPort1NeighbourId_Type()
)
vcstackStkPort1NeighbourId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcstackStkPort1NeighbourId.setStatus("current")


class _VcstackStkPort2Status_Type(Integer32):
    """Custom type vcstackStkPort2Status based on Integer32"""
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
        *(("discoveringNeighbour", 3),
          ("down", 1),
          ("learntNeighbour", 4),
          ("neighbourIncompatible", 2))
    )


_VcstackStkPort2Status_Type.__name__ = "Integer32"
_VcstackStkPort2Status_Object = MibTableColumn
vcstackStkPort2Status = _VcstackStkPort2Status_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 5, 1, 17),
    _VcstackStkPort2Status_Type()
)
vcstackStkPort2Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcstackStkPort2Status.setStatus("current")


class _VcstackStkPort2NeighbourId_Type(Unsigned32):
    """Custom type vcstackStkPort2NeighbourId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_VcstackStkPort2NeighbourId_Type.__name__ = "Unsigned32"
_VcstackStkPort2NeighbourId_Object = MibTableColumn
vcstackStkPort2NeighbourId = _VcstackStkPort2NeighbourId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 5, 1, 18),
    _VcstackStkPort2NeighbourId_Type()
)
vcstackStkPort2NeighbourId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcstackStkPort2NeighbourId.setStatus("current")
_VcstackNumMembersJoined_Type = Counter32
_VcstackNumMembersJoined_Object = MibTableColumn
vcstackNumMembersJoined = _VcstackNumMembersJoined_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 5, 1, 19),
    _VcstackNumMembersJoined_Type()
)
vcstackNumMembersJoined.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcstackNumMembersJoined.setStatus("current")
_VcstackNumMembersLeft_Type = Counter32
_VcstackNumMembersLeft_Object = MibTableColumn
vcstackNumMembersLeft = _VcstackNumMembersLeft_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 5, 1, 20),
    _VcstackNumMembersLeft_Type()
)
vcstackNumMembersLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcstackNumMembersLeft.setStatus("current")
_VcstackNumIdConflict_Type = Counter32
_VcstackNumIdConflict_Object = MibTableColumn
vcstackNumIdConflict = _VcstackNumIdConflict_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 5, 1, 21),
    _VcstackNumIdConflict_Type()
)
vcstackNumIdConflict.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcstackNumIdConflict.setStatus("current")
_VcstackNumMasterConflict_Type = Counter32
_VcstackNumMasterConflict_Object = MibTableColumn
vcstackNumMasterConflict = _VcstackNumMasterConflict_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 5, 1, 22),
    _VcstackNumMasterConflict_Type()
)
vcstackNumMasterConflict.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcstackNumMasterConflict.setStatus("current")
_VcstackNumMasterFailover_Type = Counter32
_VcstackNumMasterFailover_Object = MibTableColumn
vcstackNumMasterFailover = _VcstackNumMasterFailover_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 5, 1, 23),
    _VcstackNumMasterFailover_Type()
)
vcstackNumMasterFailover.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcstackNumMasterFailover.setStatus("current")
_VcstackNumStkPort1NbrIncompatible_Type = Counter32
_VcstackNumStkPort1NbrIncompatible_Object = MibTableColumn
vcstackNumStkPort1NbrIncompatible = _VcstackNumStkPort1NbrIncompatible_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 5, 1, 24),
    _VcstackNumStkPort1NbrIncompatible_Type()
)
vcstackNumStkPort1NbrIncompatible.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcstackNumStkPort1NbrIncompatible.setStatus("current")
_VcstackNumStkPort2NbrIncompatible_Type = Counter32
_VcstackNumStkPort2NbrIncompatible_Object = MibTableColumn
vcstackNumStkPort2NbrIncompatible = _VcstackNumStkPort2NbrIncompatible_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 5, 1, 25),
    _VcstackNumStkPort2NbrIncompatible_Type()
)
vcstackNumStkPort2NbrIncompatible.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcstackNumStkPort2NbrIncompatible.setStatus("current")


class _VcstackReadinessStatus_Type(Integer32):
    """Custom type vcstackReadinessStatus based on Integer32"""
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
        *(("init", 1),
          ("ready", 3),
          ("syncError", 4),
          ("syncing", 2))
    )


_VcstackReadinessStatus_Type.__name__ = "Integer32"
_VcstackReadinessStatus_Object = MibTableColumn
vcstackReadinessStatus = _VcstackReadinessStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 5, 1, 26),
    _VcstackReadinessStatus_Type()
)
vcstackReadinessStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcstackReadinessStatus.setStatus("current")
_VcstackTraps_ObjectIdentity = ObjectIdentity
vcstackTraps = _VcstackTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 6)
)


class _VcstackNbrMemberId_Type(Unsigned32):
    """Custom type vcstackNbrMemberId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_VcstackNbrMemberId_Type.__name__ = "Unsigned32"
_VcstackNbrMemberId_Object = MibScalar
vcstackNbrMemberId = _VcstackNbrMemberId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 6, 8),
    _VcstackNbrMemberId_Type()
)
vcstackNbrMemberId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vcstackNbrMemberId.setStatus("deprecated")
_VcstackStkPortName_Type = DisplayString
_VcstackStkPortName_Object = MibScalar
vcstackStkPortName = _VcstackStkPortName_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 6, 9),
    _VcstackStkPortName_Type()
)
vcstackStkPortName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vcstackStkPortName.setStatus("deprecated")


class _VcstackVirtualMacAddressStatus_Type(Integer32):
    """Custom type vcstackVirtualMacAddressStatus based on Integer32"""
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


_VcstackVirtualMacAddressStatus_Type.__name__ = "Integer32"
_VcstackVirtualMacAddressStatus_Object = MibScalar
vcstackVirtualMacAddressStatus = _VcstackVirtualMacAddressStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 7),
    _VcstackVirtualMacAddressStatus_Type()
)
vcstackVirtualMacAddressStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcstackVirtualMacAddressStatus.setStatus("current")
_VcstackVirtualChassisId_Type = Integer32
_VcstackVirtualChassisId_Object = MibScalar
vcstackVirtualChassisId = _VcstackVirtualChassisId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 8),
    _VcstackVirtualChassisId_Type()
)
vcstackVirtualChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcstackVirtualChassisId.setStatus("current")
_VcstackVirtualMacAddr_Type = MacAddress
_VcstackVirtualMacAddr_Object = MibScalar
vcstackVirtualMacAddr = _VcstackVirtualMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 9),
    _VcstackVirtualMacAddr_Type()
)
vcstackVirtualMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcstackVirtualMacAddr.setStatus("current")


class _VcstackMasterId_Type(Unsigned32):
    """Custom type vcstackMasterId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_VcstackMasterId_Type.__name__ = "Unsigned32"
_VcstackMasterId_Object = MibScalar
vcstackMasterId = _VcstackMasterId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 10),
    _VcstackMasterId_Type()
)
vcstackMasterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcstackMasterId.setStatus("current")


class _VcstackDisabledMasterMonitoringStatus_Type(Integer32):
    """Custom type vcstackDisabledMasterMonitoringStatus based on Integer32"""
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
          ("enabled", 1),
          ("inactive", 3))
    )


_VcstackDisabledMasterMonitoringStatus_Type.__name__ = "Integer32"
_VcstackDisabledMasterMonitoringStatus_Object = MibScalar
vcstackDisabledMasterMonitoringStatus = _VcstackDisabledMasterMonitoringStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 11),
    _VcstackDisabledMasterMonitoringStatus_Type()
)
vcstackDisabledMasterMonitoringStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcstackDisabledMasterMonitoringStatus.setStatus("current")

# Managed Objects groups


# Notification objects

vcstackRoleChangeNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 0, 1)
)
vcstackRoleChangeNotify.setObjects(
      *(("AT-VCSTACK-MIB", "vcstackId"),
        ("AT-VCSTACK-MIB", "vcstackRole"))
)
if mibBuilder.loadTexts:
    vcstackRoleChangeNotify.setStatus(
        "current"
    )

vcstackMemberJoinNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 0, 2)
)
vcstackMemberJoinNotify.setObjects(
      *(("AT-VCSTACK-MIB", "vcstackId"),
        ("AT-VCSTACK-MIB", "vcstackNbrMemberIdNotify"))
)
if mibBuilder.loadTexts:
    vcstackMemberJoinNotify.setStatus(
        "current"
    )

vcstackMemberLeaveNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 0, 3)
)
vcstackMemberLeaveNotify.setObjects(
      *(("AT-VCSTACK-MIB", "vcstackId"),
        ("AT-VCSTACK-MIB", "vcstackNbrMemberIdNotify"))
)
if mibBuilder.loadTexts:
    vcstackMemberLeaveNotify.setStatus(
        "current"
    )

vcstackResiliencyLinkHealthCheckReceivingNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 0, 4)
)
vcstackResiliencyLinkHealthCheckReceivingNotify.setObjects(
      *(("AT-VCSTACK-MIB", "vcstackId"),
        ("AT-VCSTACK-MIB", "vcstackResiliencyLinkInterfaceName"))
)
if mibBuilder.loadTexts:
    vcstackResiliencyLinkHealthCheckReceivingNotify.setStatus(
        "current"
    )

vcstackResiliencyLinkHealthCheckTimeOutNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 0, 5)
)
vcstackResiliencyLinkHealthCheckTimeOutNotify.setObjects(
      *(("AT-VCSTACK-MIB", "vcstackId"),
        ("AT-VCSTACK-MIB", "vcstackResiliencyLinkInterfaceName"))
)
if mibBuilder.loadTexts:
    vcstackResiliencyLinkHealthCheckTimeOutNotify.setStatus(
        "current"
    )

vcstackStkPortLinkUpNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 0, 6)
)
vcstackStkPortLinkUpNotify.setObjects(
      *(("AT-VCSTACK-MIB", "vcstackId"),
        ("AT-VCSTACK-MIB", "vcstackStkPortNameNotify"))
)
if mibBuilder.loadTexts:
    vcstackStkPortLinkUpNotify.setStatus(
        "current"
    )

vcstackStkPortLinkDownNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 0, 7)
)
vcstackStkPortLinkDownNotify.setObjects(
      *(("AT-VCSTACK-MIB", "vcstackId"),
        ("AT-VCSTACK-MIB", "vcstackStkPortNameNotify"))
)
if mibBuilder.loadTexts:
    vcstackStkPortLinkDownNotify.setStatus(
        "current"
    )

vcstackRoleChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 6, 1)
)
vcstackRoleChange.setObjects(
      *(("AT-VCSTACK-MIB", "vcstackId"),
        ("AT-VCSTACK-MIB", "vcstackRole"))
)
if mibBuilder.loadTexts:
    vcstackRoleChange.setStatus(
        "deprecated"
    )

vcstackMemberJoin = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 6, 2)
)
vcstackMemberJoin.setObjects(
      *(("AT-VCSTACK-MIB", "vcstackId"),
        ("AT-VCSTACK-MIB", "vcstackNbrMemberId"))
)
if mibBuilder.loadTexts:
    vcstackMemberJoin.setStatus(
        "deprecated"
    )

vcstackMemberLeave = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 6, 3)
)
vcstackMemberLeave.setObjects(
      *(("AT-VCSTACK-MIB", "vcstackId"),
        ("AT-VCSTACK-MIB", "vcstackNbrMemberId"))
)
if mibBuilder.loadTexts:
    vcstackMemberLeave.setStatus(
        "deprecated"
    )

vcstackResiliencyLinkHealthCheckReceiving = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 6, 4)
)
vcstackResiliencyLinkHealthCheckReceiving.setObjects(
      *(("AT-VCSTACK-MIB", "vcstackId"),
        ("AT-VCSTACK-MIB", "vcstackResiliencyLinkInterfaceName"))
)
if mibBuilder.loadTexts:
    vcstackResiliencyLinkHealthCheckReceiving.setStatus(
        "deprecated"
    )

vcstackResiliencyLinkHealthCheckTimeOut = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 6, 5)
)
vcstackResiliencyLinkHealthCheckTimeOut.setObjects(
      *(("AT-VCSTACK-MIB", "vcstackId"),
        ("AT-VCSTACK-MIB", "vcstackResiliencyLinkInterfaceName"))
)
if mibBuilder.loadTexts:
    vcstackResiliencyLinkHealthCheckTimeOut.setStatus(
        "deprecated"
    )

vcstackStkPortLinkUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 6, 6)
)
vcstackStkPortLinkUp.setObjects(
      *(("AT-VCSTACK-MIB", "vcstackId"),
        ("AT-VCSTACK-MIB", "vcstackStkPortName"))
)
if mibBuilder.loadTexts:
    vcstackStkPortLinkUp.setStatus(
        "deprecated"
    )

vcstackStkPortLinkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 6, 7)
)
vcstackStkPortLinkDown.setObjects(
      *(("AT-VCSTACK-MIB", "vcstackId"),
        ("AT-VCSTACK-MIB", "vcstackStkPortName"))
)
if mibBuilder.loadTexts:
    vcstackStkPortLinkDown.setStatus(
        "deprecated"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AT-VCSTACK-MIB",
    **{"vcstack": vcstack,
       "vcstackNotifications": vcstackNotifications,
       "vcstackRoleChangeNotify": vcstackRoleChangeNotify,
       "vcstackMemberJoinNotify": vcstackMemberJoinNotify,
       "vcstackMemberLeaveNotify": vcstackMemberLeaveNotify,
       "vcstackResiliencyLinkHealthCheckReceivingNotify": vcstackResiliencyLinkHealthCheckReceivingNotify,
       "vcstackResiliencyLinkHealthCheckTimeOutNotify": vcstackResiliencyLinkHealthCheckTimeOutNotify,
       "vcstackStkPortLinkUpNotify": vcstackStkPortLinkUpNotify,
       "vcstackStkPortLinkDownNotify": vcstackStkPortLinkDownNotify,
       "vcstackNbrMemberIdNotify": vcstackNbrMemberIdNotify,
       "vcstackStkPortNameNotify": vcstackStkPortNameNotify,
       "vcstackStatus": vcstackStatus,
       "vcstackOperationalStatus": vcstackOperationalStatus,
       "vcstackMgmtVlanId": vcstackMgmtVlanId,
       "vcstackMgmtVlanSubnetAddr": vcstackMgmtVlanSubnetAddr,
       "vcstackTable": vcstackTable,
       "vcstackEntry": vcstackEntry,
       "vcstackId": vcstackId,
       "vcstackPendingId": vcstackPendingId,
       "vcstackMacAddr": vcstackMacAddr,
       "vcstackPriority": vcstackPriority,
       "vcstackRole": vcstackRole,
       "vcstackLastRoleChange": vcstackLastRoleChange,
       "vcstackHostname": vcstackHostname,
       "vcstackProductType": vcstackProductType,
       "vcstackSWVersionAutoSync": vcstackSWVersionAutoSync,
       "vcstackFallbackConfigStatus": vcstackFallbackConfigStatus,
       "vcstackFallbackConfigFilename": vcstackFallbackConfigFilename,
       "vcstackResiliencyLinkStatus": vcstackResiliencyLinkStatus,
       "vcstackResiliencyLinkInterfaceName": vcstackResiliencyLinkInterfaceName,
       "vcstackActiveStkHardware": vcstackActiveStkHardware,
       "vcstackStkPort1Status": vcstackStkPort1Status,
       "vcstackStkPort1NeighbourId": vcstackStkPort1NeighbourId,
       "vcstackStkPort2Status": vcstackStkPort2Status,
       "vcstackStkPort2NeighbourId": vcstackStkPort2NeighbourId,
       "vcstackNumMembersJoined": vcstackNumMembersJoined,
       "vcstackNumMembersLeft": vcstackNumMembersLeft,
       "vcstackNumIdConflict": vcstackNumIdConflict,
       "vcstackNumMasterConflict": vcstackNumMasterConflict,
       "vcstackNumMasterFailover": vcstackNumMasterFailover,
       "vcstackNumStkPort1NbrIncompatible": vcstackNumStkPort1NbrIncompatible,
       "vcstackNumStkPort2NbrIncompatible": vcstackNumStkPort2NbrIncompatible,
       "vcstackReadinessStatus": vcstackReadinessStatus,
       "vcstackTraps": vcstackTraps,
       "vcstackRoleChange": vcstackRoleChange,
       "vcstackMemberJoin": vcstackMemberJoin,
       "vcstackMemberLeave": vcstackMemberLeave,
       "vcstackResiliencyLinkHealthCheckReceiving": vcstackResiliencyLinkHealthCheckReceiving,
       "vcstackResiliencyLinkHealthCheckTimeOut": vcstackResiliencyLinkHealthCheckTimeOut,
       "vcstackStkPortLinkUp": vcstackStkPortLinkUp,
       "vcstackStkPortLinkDown": vcstackStkPortLinkDown,
       "vcstackNbrMemberId": vcstackNbrMemberId,
       "vcstackStkPortName": vcstackStkPortName,
       "vcstackVirtualMacAddressStatus": vcstackVirtualMacAddressStatus,
       "vcstackVirtualChassisId": vcstackVirtualChassisId,
       "vcstackVirtualMacAddr": vcstackVirtualMacAddr,
       "vcstackMasterId": vcstackMasterId,
       "vcstackDisabledMasterMonitoringStatus": vcstackDisabledMasterMonitoringStatus}
)
