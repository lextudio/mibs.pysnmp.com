# SNMP MIB module (PCE-PCEP-DRAFT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PCE-PCEP-DRAFT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:37:07 2024
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

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType",
    "InetPortNumber")

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
 experimental,
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
    "experimental",
    "iso")

(DisplayString,
 RowStatus,
 StorageType,
 TextualConvention,
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

pcePcepDraftMIB = ModuleIdentity(
    (1, 3, 6, 1, 3, 9999)
)
pcePcepDraftMIB.setRevisions(
        ("2007-07-08 12:00",
         "2007-02-20 12:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class PcePcepIdentifier(OctetString, TextualConvention):
    status = "current"
    displayHint = "1d.1d.1d.1d:1d:1d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )



# MIB Managed Objects in the order of their OIDs

_PcePcepNotifications_ObjectIdentity = ObjectIdentity
pcePcepNotifications = _PcePcepNotifications_ObjectIdentity(
    (1, 3, 6, 1, 3, 9999, 0)
)
_PcePcepMIBObjects_ObjectIdentity = ObjectIdentity
pcePcepMIBObjects = _PcePcepMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 3, 9999, 1)
)
_PcePcepClientObjects_ObjectIdentity = ObjectIdentity
pcePcepClientObjects = _PcePcepClientObjects_ObjectIdentity(
    (1, 3, 6, 1, 3, 9999, 1, 1)
)
_PcePcepClientLastChange_Type = TimeStamp
_PcePcepClientLastChange_Object = MibScalar
pcePcepClientLastChange = _PcePcepClientLastChange_Object(
    (1, 3, 6, 1, 3, 9999, 1, 1, 1),
    _PcePcepClientLastChange_Type()
)
pcePcepClientLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcePcepClientLastChange.setStatus("current")
_PcePcepClientIndexNext_Type = Unsigned32
_PcePcepClientIndexNext_Object = MibScalar
pcePcepClientIndexNext = _PcePcepClientIndexNext_Object(
    (1, 3, 6, 1, 3, 9999, 1, 1, 2),
    _PcePcepClientIndexNext_Type()
)
pcePcepClientIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcePcepClientIndexNext.setStatus("current")
_PcePcepClientTable_Object = MibTable
pcePcepClientTable = _PcePcepClientTable_Object(
    (1, 3, 6, 1, 3, 9999, 1, 1, 3)
)
if mibBuilder.loadTexts:
    pcePcepClientTable.setStatus("current")
_PcePcepClientEntry_Object = MibTableRow
pcePcepClientEntry = _PcePcepClientEntry_Object(
    (1, 3, 6, 1, 3, 9999, 1, 1, 3, 1)
)
pcePcepClientEntry.setIndexNames(
    (0, "PCE-PCEP-DRAFT-MIB", "pcePcepClientPcepId"),
    (0, "PCE-PCEP-DRAFT-MIB", "pcePcepClientIndex"),
)
if mibBuilder.loadTexts:
    pcePcepClientEntry.setStatus("current")
_PcePcepClientPcepId_Type = PcePcepIdentifier
_PcePcepClientPcepId_Object = MibTableColumn
pcePcepClientPcepId = _PcePcepClientPcepId_Object(
    (1, 3, 6, 1, 3, 9999, 1, 1, 3, 1, 1),
    _PcePcepClientPcepId_Type()
)
pcePcepClientPcepId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pcePcepClientPcepId.setStatus("current")
_PcePcepClientIndex_Type = Unsigned32
_PcePcepClientIndex_Object = MibTableColumn
pcePcepClientIndex = _PcePcepClientIndex_Object(
    (1, 3, 6, 1, 3, 9999, 1, 1, 3, 1, 2),
    _PcePcepClientIndex_Type()
)
pcePcepClientIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pcePcepClientIndex.setStatus("current")


class _PcePcepClientAdminStatus_Type(Integer32):
    """Custom type pcePcepClientAdminStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_PcePcepClientAdminStatus_Type.__name__ = "Integer32"
_PcePcepClientAdminStatus_Object = MibTableColumn
pcePcepClientAdminStatus = _PcePcepClientAdminStatus_Object(
    (1, 3, 6, 1, 3, 9999, 1, 1, 3, 1, 4),
    _PcePcepClientAdminStatus_Type()
)
pcePcepClientAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pcePcepClientAdminStatus.setStatus("current")


class _PcePcepClientOperStatus_Type(Integer32):
    """Custom type pcePcepClientOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enabled", 2),
          ("unknown", 1))
    )


_PcePcepClientOperStatus_Type.__name__ = "Integer32"
_PcePcepClientOperStatus_Object = MibTableColumn
pcePcepClientOperStatus = _PcePcepClientOperStatus_Object(
    (1, 3, 6, 1, 3, 9999, 1, 1, 3, 1, 5),
    _PcePcepClientOperStatus_Type()
)
pcePcepClientOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcePcepClientOperStatus.setStatus("current")
_PcePcepClientTcpPort_Type = InetPortNumber
_PcePcepClientTcpPort_Object = MibTableColumn
pcePcepClientTcpPort = _PcePcepClientTcpPort_Object(
    (1, 3, 6, 1, 3, 9999, 1, 1, 3, 1, 6),
    _PcePcepClientTcpPort_Type()
)
pcePcepClientTcpPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pcePcepClientTcpPort.setStatus("current")


class _PcePcepClientKeepAliveTimer_Type(Unsigned32):
    """Custom type pcePcepClientKeepAliveTimer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PcePcepClientKeepAliveTimer_Type.__name__ = "Unsigned32"
_PcePcepClientKeepAliveTimer_Object = MibTableColumn
pcePcepClientKeepAliveTimer = _PcePcepClientKeepAliveTimer_Object(
    (1, 3, 6, 1, 3, 9999, 1, 1, 3, 1, 7),
    _PcePcepClientKeepAliveTimer_Type()
)
pcePcepClientKeepAliveTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pcePcepClientKeepAliveTimer.setStatus("current")
if mibBuilder.loadTexts:
    pcePcepClientKeepAliveTimer.setUnits("seconds")


class _PcePcepClientStorageType_Type(StorageType):
    """Custom type pcePcepClientStorageType based on StorageType"""


_PcePcepClientStorageType_Object = MibTableColumn
pcePcepClientStorageType = _PcePcepClientStorageType_Object(
    (1, 3, 6, 1, 3, 9999, 1, 1, 3, 1, 8),
    _PcePcepClientStorageType_Type()
)
pcePcepClientStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pcePcepClientStorageType.setStatus("current")
_PcePcepClientRowStatus_Type = RowStatus
_PcePcepClientRowStatus_Object = MibTableColumn
pcePcepClientRowStatus = _PcePcepClientRowStatus_Object(
    (1, 3, 6, 1, 3, 9999, 1, 1, 3, 1, 9),
    _PcePcepClientRowStatus_Type()
)
pcePcepClientRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pcePcepClientRowStatus.setStatus("current")


class _PcePcepClientDeadTimer_Type(Unsigned32):
    """Custom type pcePcepClientDeadTimer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 262140),
    )


_PcePcepClientDeadTimer_Type.__name__ = "Unsigned32"
_PcePcepClientDeadTimer_Object = MibTableColumn
pcePcepClientDeadTimer = _PcePcepClientDeadTimer_Object(
    (1, 3, 6, 1, 3, 9999, 1, 1, 3, 1, 10),
    _PcePcepClientDeadTimer_Type()
)
pcePcepClientDeadTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pcePcepClientDeadTimer.setStatus("current")
if mibBuilder.loadTexts:
    pcePcepClientDeadTimer.setUnits("seconds")
_PcePcepSessionObjects_ObjectIdentity = ObjectIdentity
pcePcepSessionObjects = _PcePcepSessionObjects_ObjectIdentity(
    (1, 3, 6, 1, 3, 9999, 1, 3)
)
_PcePcepPeerLastChange_Type = TimeStamp
_PcePcepPeerLastChange_Object = MibScalar
pcePcepPeerLastChange = _PcePcepPeerLastChange_Object(
    (1, 3, 6, 1, 3, 9999, 1, 3, 1),
    _PcePcepPeerLastChange_Type()
)
pcePcepPeerLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcePcepPeerLastChange.setStatus("current")
_PcePcepPeerTable_Object = MibTable
pcePcepPeerTable = _PcePcepPeerTable_Object(
    (1, 3, 6, 1, 3, 9999, 1, 3, 2)
)
if mibBuilder.loadTexts:
    pcePcepPeerTable.setStatus("current")
_PcePcepPeerEntry_Object = MibTableRow
pcePcepPeerEntry = _PcePcepPeerEntry_Object(
    (1, 3, 6, 1, 3, 9999, 1, 3, 2, 1)
)
pcePcepPeerEntry.setIndexNames(
    (0, "PCE-PCEP-DRAFT-MIB", "pcePcepClientPcepId"),
    (0, "PCE-PCEP-DRAFT-MIB", "pcePcepClientIndex"),
    (0, "PCE-PCEP-DRAFT-MIB", "pcePcepPeerPcepId"),
)
if mibBuilder.loadTexts:
    pcePcepPeerEntry.setStatus("current")
_PcePcepPeerPcepId_Type = PcePcepIdentifier
_PcePcepPeerPcepId_Object = MibTableColumn
pcePcepPeerPcepId = _PcePcepPeerPcepId_Object(
    (1, 3, 6, 1, 3, 9999, 1, 3, 2, 1, 1),
    _PcePcepPeerPcepId_Type()
)
pcePcepPeerPcepId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pcePcepPeerPcepId.setStatus("current")
_PcePcepPeerTransportAddrType_Type = InetAddressType
_PcePcepPeerTransportAddrType_Object = MibTableColumn
pcePcepPeerTransportAddrType = _PcePcepPeerTransportAddrType_Object(
    (1, 3, 6, 1, 3, 9999, 1, 3, 2, 1, 2),
    _PcePcepPeerTransportAddrType_Type()
)
pcePcepPeerTransportAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcePcepPeerTransportAddrType.setStatus("current")
_PcePcepPeerTransportAddr_Type = InetAddress
_PcePcepPeerTransportAddr_Object = MibTableColumn
pcePcepPeerTransportAddr = _PcePcepPeerTransportAddr_Object(
    (1, 3, 6, 1, 3, 9999, 1, 3, 2, 1, 3),
    _PcePcepPeerTransportAddr_Type()
)
pcePcepPeerTransportAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcePcepPeerTransportAddr.setStatus("current")
_PcePcepSessionTable_Object = MibTable
pcePcepSessionTable = _PcePcepSessionTable_Object(
    (1, 3, 6, 1, 3, 9999, 1, 3, 3)
)
if mibBuilder.loadTexts:
    pcePcepSessionTable.setStatus("current")
_PcePcepSessionEntry_Object = MibTableRow
pcePcepSessionEntry = _PcePcepSessionEntry_Object(
    (1, 3, 6, 1, 3, 9999, 1, 3, 3, 1)
)
if mibBuilder.loadTexts:
    pcePcepSessionEntry.setStatus("current")
_PcePcepSessionStateLastChange_Type = TimeStamp
_PcePcepSessionStateLastChange_Object = MibTableColumn
pcePcepSessionStateLastChange = _PcePcepSessionStateLastChange_Object(
    (1, 3, 6, 1, 3, 9999, 1, 3, 3, 1, 1),
    _PcePcepSessionStateLastChange_Type()
)
pcePcepSessionStateLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcePcepSessionStateLastChange.setStatus("current")


class _PcePcepSessionState_Type(Integer32):
    """Custom type pcePcepSessionState based on Integer32"""
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
        *(("idle", 5),
          ("keepWait", 2),
          ("openWait", 3),
          ("sessionUp", 1),
          ("tcpPending", 4))
    )


_PcePcepSessionState_Type.__name__ = "Integer32"
_PcePcepSessionState_Object = MibTableColumn
pcePcepSessionState = _PcePcepSessionState_Object(
    (1, 3, 6, 1, 3, 9999, 1, 3, 3, 1, 2),
    _PcePcepSessionState_Type()
)
pcePcepSessionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcePcepSessionState.setStatus("current")
_PcePcepSessionKeepAliveHoldTimeRem_Type = TimeInterval
_PcePcepSessionKeepAliveHoldTimeRem_Object = MibTableColumn
pcePcepSessionKeepAliveHoldTimeRem = _PcePcepSessionKeepAliveHoldTimeRem_Object(
    (1, 3, 6, 1, 3, 9999, 1, 3, 3, 1, 3),
    _PcePcepSessionKeepAliveHoldTimeRem_Type()
)
pcePcepSessionKeepAliveHoldTimeRem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcePcepSessionKeepAliveHoldTimeRem.setStatus("current")


class _PcePcepSessionKeepAliveTime_Type(Unsigned32):
    """Custom type pcePcepSessionKeepAliveTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PcePcepSessionKeepAliveTime_Type.__name__ = "Unsigned32"
_PcePcepSessionKeepAliveTime_Object = MibTableColumn
pcePcepSessionKeepAliveTime = _PcePcepSessionKeepAliveTime_Object(
    (1, 3, 6, 1, 3, 9999, 1, 3, 3, 1, 4),
    _PcePcepSessionKeepAliveTime_Type()
)
pcePcepSessionKeepAliveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcePcepSessionKeepAliveTime.setStatus("current")
if mibBuilder.loadTexts:
    pcePcepSessionKeepAliveTime.setUnits("seconds")
_PcePcepSessionDiscontinuityTime_Type = TimeStamp
_PcePcepSessionDiscontinuityTime_Object = MibTableColumn
pcePcepSessionDiscontinuityTime = _PcePcepSessionDiscontinuityTime_Object(
    (1, 3, 6, 1, 3, 9999, 1, 3, 3, 1, 5),
    _PcePcepSessionDiscontinuityTime_Type()
)
pcePcepSessionDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcePcepSessionDiscontinuityTime.setStatus("current")


class _PcePcepSessionSpeakerRole_Type(Integer32):
    """Custom type pcePcepSessionSpeakerRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("pcc", 1),
          ("pccandpce", 3),
          ("pce", 2))
    )


_PcePcepSessionSpeakerRole_Type.__name__ = "Integer32"
_PcePcepSessionSpeakerRole_Object = MibTableColumn
pcePcepSessionSpeakerRole = _PcePcepSessionSpeakerRole_Object(
    (1, 3, 6, 1, 3, 9999, 1, 3, 3, 1, 6),
    _PcePcepSessionSpeakerRole_Type()
)
pcePcepSessionSpeakerRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcePcepSessionSpeakerRole.setStatus("current")
_PcePcepSessionMax_Type = Unsigned32
_PcePcepSessionMax_Object = MibScalar
pcePcepSessionMax = _PcePcepSessionMax_Object(
    (1, 3, 6, 1, 3, 9999, 1, 3, 4),
    _PcePcepSessionMax_Type()
)
pcePcepSessionMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcePcepSessionMax.setStatus("current")
_PcePcepConformance_ObjectIdentity = ObjectIdentity
pcePcepConformance = _PcePcepConformance_ObjectIdentity(
    (1, 3, 6, 1, 3, 9999, 2)
)
_PcePcepGroups_ObjectIdentity = ObjectIdentity
pcePcepGroups = _PcePcepGroups_ObjectIdentity(
    (1, 3, 6, 1, 3, 9999, 2, 1)
)
_PcePcepCompliances_ObjectIdentity = ObjectIdentity
pcePcepCompliances = _PcePcepCompliances_ObjectIdentity(
    (1, 3, 6, 1, 3, 9999, 2, 2)
)
pcePcepPeerEntry.registerAugmentions(
    ("PCE-PCEP-DRAFT-MIB",
     "pcePcepSessionEntry")
)
pcePcepSessionEntry.setIndexNames(*pcePcepPeerEntry.getIndexNames())

# Managed Objects groups

pcePcepGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 9999, 2, 1, 1)
)
pcePcepGeneralGroup.setObjects(
      *(("PCE-PCEP-DRAFT-MIB", "pcePcepClientLastChange"),
        ("PCE-PCEP-DRAFT-MIB", "pcePcepClientIndexNext"),
        ("PCE-PCEP-DRAFT-MIB", "pcePcepClientAdminStatus"),
        ("PCE-PCEP-DRAFT-MIB", "pcePcepClientOperStatus"),
        ("PCE-PCEP-DRAFT-MIB", "pcePcepClientTcpPort"),
        ("PCE-PCEP-DRAFT-MIB", "pcePcepClientKeepAliveTimer"),
        ("PCE-PCEP-DRAFT-MIB", "pcePcepClientStorageType"),
        ("PCE-PCEP-DRAFT-MIB", "pcePcepClientRowStatus"),
        ("PCE-PCEP-DRAFT-MIB", "pcePcepPeerLastChange"),
        ("PCE-PCEP-DRAFT-MIB", "pcePcepPeerTransportAddrType"),
        ("PCE-PCEP-DRAFT-MIB", "pcePcepPeerTransportAddr"),
        ("PCE-PCEP-DRAFT-MIB", "pcePcepSessionStateLastChange"),
        ("PCE-PCEP-DRAFT-MIB", "pcePcepSessionState"),
        ("PCE-PCEP-DRAFT-MIB", "pcePcepSessionKeepAliveHoldTimeRem"),
        ("PCE-PCEP-DRAFT-MIB", "pcePcepSessionKeepAliveTime"),
        ("PCE-PCEP-DRAFT-MIB", "pcePcepSessionDiscontinuityTime"),
        ("PCE-PCEP-DRAFT-MIB", "pcePcepClientDeadTimer"),
        ("PCE-PCEP-DRAFT-MIB", "pcePcepSessionMax"),
        ("PCE-PCEP-DRAFT-MIB", "pcePcepSessionSpeakerRole"))
)
if mibBuilder.loadTexts:
    pcePcepGeneralGroup.setStatus("current")


# Notification objects

pcePcepSessionUp = NotificationType(
    (1, 3, 6, 1, 3, 9999, 0, 1)
)
pcePcepSessionUp.setObjects(
      *(("PCE-PCEP-DRAFT-MIB", "pcePcepSessionState"),
        ("PCE-PCEP-DRAFT-MIB", "pcePcepSessionDiscontinuityTime"))
)
if mibBuilder.loadTexts:
    pcePcepSessionUp.setStatus(
        "current"
    )

pcePcepSessionDown = NotificationType(
    (1, 3, 6, 1, 3, 9999, 0, 2)
)
pcePcepSessionDown.setObjects(
      *(("PCE-PCEP-DRAFT-MIB", "pcePcepSessionState"),
        ("PCE-PCEP-DRAFT-MIB", "pcePcepSessionDiscontinuityTime"))
)
if mibBuilder.loadTexts:
    pcePcepSessionDown.setStatus(
        "current"
    )


# Notifications groups

pcePcepNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 3, 9999, 2, 1, 2)
)
pcePcepNotificationsGroup.setObjects(
      *(("PCE-PCEP-DRAFT-MIB", "pcePcepSessionUp"),
        ("PCE-PCEP-DRAFT-MIB", "pcePcepSessionDown"))
)
if mibBuilder.loadTexts:
    pcePcepNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

pcePcepModuleFullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 3, 9999, 2, 2, 1)
)
if mibBuilder.loadTexts:
    pcePcepModuleFullCompliance.setStatus(
        "current"
    )

pcePcepModuleReadOnlyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 3, 9999, 2, 2, 2)
)
if mibBuilder.loadTexts:
    pcePcepModuleReadOnlyCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PCE-PCEP-DRAFT-MIB",
    **{"PcePcepIdentifier": PcePcepIdentifier,
       "pcePcepDraftMIB": pcePcepDraftMIB,
       "pcePcepNotifications": pcePcepNotifications,
       "pcePcepSessionUp": pcePcepSessionUp,
       "pcePcepSessionDown": pcePcepSessionDown,
       "pcePcepMIBObjects": pcePcepMIBObjects,
       "pcePcepClientObjects": pcePcepClientObjects,
       "pcePcepClientLastChange": pcePcepClientLastChange,
       "pcePcepClientIndexNext": pcePcepClientIndexNext,
       "pcePcepClientTable": pcePcepClientTable,
       "pcePcepClientEntry": pcePcepClientEntry,
       "pcePcepClientPcepId": pcePcepClientPcepId,
       "pcePcepClientIndex": pcePcepClientIndex,
       "pcePcepClientAdminStatus": pcePcepClientAdminStatus,
       "pcePcepClientOperStatus": pcePcepClientOperStatus,
       "pcePcepClientTcpPort": pcePcepClientTcpPort,
       "pcePcepClientKeepAliveTimer": pcePcepClientKeepAliveTimer,
       "pcePcepClientStorageType": pcePcepClientStorageType,
       "pcePcepClientRowStatus": pcePcepClientRowStatus,
       "pcePcepClientDeadTimer": pcePcepClientDeadTimer,
       "pcePcepSessionObjects": pcePcepSessionObjects,
       "pcePcepPeerLastChange": pcePcepPeerLastChange,
       "pcePcepPeerTable": pcePcepPeerTable,
       "pcePcepPeerEntry": pcePcepPeerEntry,
       "pcePcepPeerPcepId": pcePcepPeerPcepId,
       "pcePcepPeerTransportAddrType": pcePcepPeerTransportAddrType,
       "pcePcepPeerTransportAddr": pcePcepPeerTransportAddr,
       "pcePcepSessionTable": pcePcepSessionTable,
       "pcePcepSessionEntry": pcePcepSessionEntry,
       "pcePcepSessionStateLastChange": pcePcepSessionStateLastChange,
       "pcePcepSessionState": pcePcepSessionState,
       "pcePcepSessionKeepAliveHoldTimeRem": pcePcepSessionKeepAliveHoldTimeRem,
       "pcePcepSessionKeepAliveTime": pcePcepSessionKeepAliveTime,
       "pcePcepSessionDiscontinuityTime": pcePcepSessionDiscontinuityTime,
       "pcePcepSessionSpeakerRole": pcePcepSessionSpeakerRole,
       "pcePcepSessionMax": pcePcepSessionMax,
       "pcePcepConformance": pcePcepConformance,
       "pcePcepGroups": pcePcepGroups,
       "pcePcepGeneralGroup": pcePcepGeneralGroup,
       "pcePcepNotificationsGroup": pcePcepNotificationsGroup,
       "pcePcepCompliances": pcePcepCompliances,
       "pcePcepModuleFullCompliance": pcePcepModuleFullCompliance,
       "pcePcepModuleReadOnlyCompliance": pcePcepModuleReadOnlyCompliance}
)
