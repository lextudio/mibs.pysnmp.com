# SNMP MIB module (CISCO-MEDIATRACE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-MEDIATRACE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:05:23 2024
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

(FlowMetricValue,) = mibBuilder.importSymbols(
    "CISCO-FLOW-MONITOR-TC-MIB",
    "FlowMetricValue")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

(InetAddress,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType",
    "InetPortNumber")

(VlanId,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanId")

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
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ciscoMediatraceMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 800)
)
ciscoMediatraceMIB.setRevisions(
        ("2012-08-23 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CiscoNTPTimeStamp(OctetString, TextualConvention):
    status = "current"
    displayHint = "4d.4d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )



class CiscoMediatraceSupportProtocol(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(6,
              17)
        )
    )
    namedValues = NamedValues(
        *(("tcp", 6),
          ("udp", 17))
    )



class CiscoMediatraceDiscoveryProtocol(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            46
        )
    )
    namedValues = NamedValues(
        ("rsvp", 46)
    )



# MIB Managed Objects in the order of their OIDs

_CiscoMediatraceMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoMediatraceMIBNotifs = _CiscoMediatraceMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 0)
)
_CiscoMediatraceMIBObjects_ObjectIdentity = ObjectIdentity
ciscoMediatraceMIBObjects = _CiscoMediatraceMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1)
)
_CMTCtrl_ObjectIdentity = ObjectIdentity
cMTCtrl = _CMTCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 1)
)
_CMTInitiatorEnable_Type = TruthValue
_CMTInitiatorEnable_Object = MibScalar
cMTInitiatorEnable = _CMTInitiatorEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 1, 2),
    _CMTInitiatorEnable_Type()
)
cMTInitiatorEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cMTInitiatorEnable.setStatus("current")
_CMTInitiatorSourceInterface_Type = InterfaceIndexOrZero
_CMTInitiatorSourceInterface_Object = MibScalar
cMTInitiatorSourceInterface = _CMTInitiatorSourceInterface_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 1, 3),
    _CMTInitiatorSourceInterface_Type()
)
cMTInitiatorSourceInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cMTInitiatorSourceInterface.setStatus("current")
_CMTInitiatorSourceAddressType_Type = InetAddressType
_CMTInitiatorSourceAddressType_Object = MibScalar
cMTInitiatorSourceAddressType = _CMTInitiatorSourceAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 1, 4),
    _CMTInitiatorSourceAddressType_Type()
)
cMTInitiatorSourceAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cMTInitiatorSourceAddressType.setStatus("current")
_CMTInitiatorSourceAddress_Type = InetAddress
_CMTInitiatorSourceAddress_Object = MibScalar
cMTInitiatorSourceAddress = _CMTInitiatorSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 1, 5),
    _CMTInitiatorSourceAddress_Type()
)
cMTInitiatorSourceAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cMTInitiatorSourceAddress.setStatus("current")
_CMTInitiatorMaxSessions_Type = Unsigned32
_CMTInitiatorMaxSessions_Object = MibScalar
cMTInitiatorMaxSessions = _CMTInitiatorMaxSessions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 1, 6),
    _CMTInitiatorMaxSessions_Type()
)
cMTInitiatorMaxSessions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cMTInitiatorMaxSessions.setStatus("current")
_CMTInitiatorSoftwareVersionMajor_Type = Unsigned32
_CMTInitiatorSoftwareVersionMajor_Object = MibScalar
cMTInitiatorSoftwareVersionMajor = _CMTInitiatorSoftwareVersionMajor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 1, 7),
    _CMTInitiatorSoftwareVersionMajor_Type()
)
cMTInitiatorSoftwareVersionMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMTInitiatorSoftwareVersionMajor.setStatus("current")
_CMTInitiatorSoftwareVersionMinor_Type = Unsigned32
_CMTInitiatorSoftwareVersionMinor_Object = MibScalar
cMTInitiatorSoftwareVersionMinor = _CMTInitiatorSoftwareVersionMinor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 1, 8),
    _CMTInitiatorSoftwareVersionMinor_Type()
)
cMTInitiatorSoftwareVersionMinor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMTInitiatorSoftwareVersionMinor.setStatus("current")
_CMTInitiatorProtocolVersionMajor_Type = Unsigned32
_CMTInitiatorProtocolVersionMajor_Object = MibScalar
cMTInitiatorProtocolVersionMajor = _CMTInitiatorProtocolVersionMajor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 1, 9),
    _CMTInitiatorProtocolVersionMajor_Type()
)
cMTInitiatorProtocolVersionMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMTInitiatorProtocolVersionMajor.setStatus("current")
_CMTInitiatorProtocolVersionMinor_Type = Unsigned32
_CMTInitiatorProtocolVersionMinor_Object = MibScalar
cMTInitiatorProtocolVersionMinor = _CMTInitiatorProtocolVersionMinor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 1, 10),
    _CMTInitiatorProtocolVersionMinor_Type()
)
cMTInitiatorProtocolVersionMinor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMTInitiatorProtocolVersionMinor.setStatus("current")
_CMTInitiatorConfiguredSessions_Type = Gauge32
_CMTInitiatorConfiguredSessions_Object = MibScalar
cMTInitiatorConfiguredSessions = _CMTInitiatorConfiguredSessions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 1, 11),
    _CMTInitiatorConfiguredSessions_Type()
)
cMTInitiatorConfiguredSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMTInitiatorConfiguredSessions.setStatus("current")
_CMTInitiatorPendingSessions_Type = Gauge32
_CMTInitiatorPendingSessions_Object = MibScalar
cMTInitiatorPendingSessions = _CMTInitiatorPendingSessions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 1, 12),
    _CMTInitiatorPendingSessions_Type()
)
cMTInitiatorPendingSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMTInitiatorPendingSessions.setStatus("current")
_CMTInitiatorInactiveSessions_Type = Gauge32
_CMTInitiatorInactiveSessions_Object = MibScalar
cMTInitiatorInactiveSessions = _CMTInitiatorInactiveSessions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 1, 13),
    _CMTInitiatorInactiveSessions_Type()
)
cMTInitiatorInactiveSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMTInitiatorInactiveSessions.setStatus("current")
_CMTInitiatorActiveSessions_Type = Gauge32
_CMTInitiatorActiveSessions_Object = MibScalar
cMTInitiatorActiveSessions = _CMTInitiatorActiveSessions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 1, 14),
    _CMTInitiatorActiveSessions_Type()
)
cMTInitiatorActiveSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMTInitiatorActiveSessions.setStatus("current")
_CMTResponderEnable_Type = TruthValue
_CMTResponderEnable_Object = MibScalar
cMTResponderEnable = _CMTResponderEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 1, 15),
    _CMTResponderEnable_Type()
)
cMTResponderEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cMTResponderEnable.setStatus("current")
_CMTResponderMaxSessions_Type = Unsigned32
_CMTResponderMaxSessions_Object = MibScalar
cMTResponderMaxSessions = _CMTResponderMaxSessions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 1, 16),
    _CMTResponderMaxSessions_Type()
)
cMTResponderMaxSessions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cMTResponderMaxSessions.setStatus("current")
_CMTResponderActiveSessions_Type = Gauge32
_CMTResponderActiveSessions_Object = MibScalar
cMTResponderActiveSessions = _CMTResponderActiveSessions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 1, 17),
    _CMTResponderActiveSessions_Type()
)
cMTResponderActiveSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMTResponderActiveSessions.setStatus("current")
if mibBuilder.loadTexts:
    cMTResponderActiveSessions.setUnits("sessions")
_CMTFlowSpecifierTable_Object = MibTable
cMTFlowSpecifierTable = _CMTFlowSpecifierTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 1, 18)
)
if mibBuilder.loadTexts:
    cMTFlowSpecifierTable.setStatus("current")
_CMTFlowSpecifierEntry_Object = MibTableRow
cMTFlowSpecifierEntry = _CMTFlowSpecifierEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 1, 18, 1)
)
cMTFlowSpecifierEntry.setIndexNames(
    (0, "CISCO-MEDIATRACE-MIB", "cMTFlowSpecifierName"),
)
if mibBuilder.loadTexts:
    cMTFlowSpecifierEntry.setStatus("current")
_CMTFlowSpecifierName_Type = SnmpAdminString
_CMTFlowSpecifierName_Object = MibTableColumn
cMTFlowSpecifierName = _CMTFlowSpecifierName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 1, 18, 1, 1),
    _CMTFlowSpecifierName_Type()
)
cMTFlowSpecifierName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cMTFlowSpecifierName.setStatus("current")
_CMTFlowSpecifierRowStatus_Type = RowStatus
_CMTFlowSpecifierRowStatus_Object = MibTableColumn
cMTFlowSpecifierRowStatus = _CMTFlowSpecifierRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 1, 18, 1, 2),
    _CMTFlowSpecifierRowStatus_Type()
)
cMTFlowSpecifierRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cMTFlowSpecifierRowStatus.setStatus("current")
_CMTFlowSpecifierMetadataGlobalId_Type = SnmpAdminString
_CMTFlowSpecifierMetadataGlobalId_Object = MibTableColumn
cMTFlowSpecifierMetadataGlobalId = _CMTFlowSpecifierMetadataGlobalId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 1, 18, 1, 3),
    _CMTFlowSpecifierMetadataGlobalId_Type()
)
cMTFlowSpecifierMetadataGlobalId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cMTFlowSpecifierMetadataGlobalId.setStatus("current")
_CMTFlowSpecifierDestAddrType_Type = InetAddressType
_CMTFlowSpecifierDestAddrType_Object = MibTableColumn
cMTFlowSpecifierDestAddrType = _CMTFlowSpecifierDestAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 1, 18, 1, 4),
    _CMTFlowSpecifierDestAddrType_Type()
)
cMTFlowSpecifierDestAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cMTFlowSpecifierDestAddrType.setStatus("current")
_CMTFlowSpecifierDestAddr_Type = InetAddress
_CMTFlowSpecifierDestAddr_Object = MibTableColumn
cMTFlowSpecifierDestAddr = _CMTFlowSpecifierDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 1, 18, 1, 5),
    _CMTFlowSpecifierDestAddr_Type()
)
cMTFlowSpecifierDestAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cMTFlowSpecifierDestAddr.setStatus("current")
_CMTFlowSpecifierDestPort_Type = InetPortNumber
_CMTFlowSpecifierDestPort_Object = MibTableColumn
cMTFlowSpecifierDestPort = _CMTFlowSpecifierDestPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 1, 18, 1, 6),
    _CMTFlowSpecifierDestPort_Type()
)
cMTFlowSpecifierDestPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cMTFlowSpecifierDestPort.setStatus("current")
_CMTFlowSpecifierSourceAddrType_Type = InetAddressType
_CMTFlowSpecifierSourceAddrType_Object = MibTableColumn
cMTFlowSpecifierSourceAddrType = _CMTFlowSpecifierSourceAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 1, 18, 1, 7),
    _CMTFlowSpecifierSourceAddrType_Type()
)
cMTFlowSpecifierSourceAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cMTFlowSpecifierSourceAddrType.setStatus("current")
_CMTFlowSpecifierSourceAddr_Type = InetAddress
_CMTFlowSpecifierSourceAddr_Object = MibTableColumn
cMTFlowSpecifierSourceAddr = _CMTFlowSpecifierSourceAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 1, 18, 1, 8),
    _CMTFlowSpecifierSourceAddr_Type()
)
cMTFlowSpecifierSourceAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cMTFlowSpecifierSourceAddr.setStatus("current")
_CMTFlowSpecifierSourcePort_Type = InetPortNumber
_CMTFlowSpecifierSourcePort_Object = MibTableColumn
cMTFlowSpecifierSourcePort = _CMTFlowSpecifierSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 1, 18, 1, 9),
    _CMTFlowSpecifierSourcePort_Type()
)
cMTFlowSpecifierSourcePort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cMTFlowSpecifierSourcePort.setStatus("current")


class _CMTFlowSpecifierIpProtocol_Type(CiscoMediatraceSupportProtocol):
    """Custom type cMTFlowSpecifierIpProtocol based on CiscoMediatraceSupportProtocol"""


_CMTFlowSpecifierIpProtocol_Object = MibTableColumn
cMTFlowSpecifierIpProtocol = _CMTFlowSpecifierIpProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 1, 18, 1, 10),
    _CMTFlowSpecifierIpProtocol_Type()
)
cMTFlowSpecifierIpProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cMTFlowSpecifierIpProtocol.setStatus("current")
_CMTPathSpecifierTable_Object = MibTable
cMTPathSpecifierTable = _CMTPathSpecifierTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 1, 19)
)
if mibBuilder.loadTexts:
    cMTPathSpecifierTable.setStatus("current")
_CMTPathSpecifierEntry_Object = MibTableRow
cMTPathSpecifierEntry = _CMTPathSpecifierEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 1, 19, 1)
)
cMTPathSpecifierEntry.setIndexNames(
    (0, "CISCO-MEDIATRACE-MIB", "cMTPathSpecifierName"),
)
if mibBuilder.loadTexts:
    cMTPathSpecifierEntry.setStatus("current")
_CMTPathSpecifierName_Type = SnmpAdminString
_CMTPathSpecifierName_Object = MibTableColumn
cMTPathSpecifierName = _CMTPathSpecifierName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 1, 19, 1, 1),
    _CMTPathSpecifierName_Type()
)
cMTPathSpecifierName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cMTPathSpecifierName.setStatus("current")
_CMTPathSpecifierRowStatus_Type = RowStatus
_CMTPathSpecifierRowStatus_Object = MibTableColumn
cMTPathSpecifierRowStatus = _CMTPathSpecifierRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 1, 19, 1, 2),
    _CMTPathSpecifierRowStatus_Type()
)
cMTPathSpecifierRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cMTPathSpecifierRowStatus.setStatus("current")
_CMTPathSpecifierMetadataGlobalId_Type = SnmpAdminString
_CMTPathSpecifierMetadataGlobalId_Object = MibTableColumn
cMTPathSpecifierMetadataGlobalId = _CMTPathSpecifierMetadataGlobalId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 1, 19, 1, 3),
    _CMTPathSpecifierMetadataGlobalId_Type()
)
cMTPathSpecifierMetadataGlobalId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cMTPathSpecifierMetadataGlobalId.setStatus("current")
_CMTPathSpecifierDestAddrType_Type = InetAddressType
_CMTPathSpecifierDestAddrType_Object = MibTableColumn
cMTPathSpecifierDestAddrType = _CMTPathSpecifierDestAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 1, 19, 1, 4),
    _CMTPathSpecifierDestAddrType_Type()
)
cMTPathSpecifierDestAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cMTPathSpecifierDestAddrType.setStatus("current")
_CMTPathSpecifierDestAddr_Type = InetAddress
_CMTPathSpecifierDestAddr_Object = MibTableColumn
cMTPathSpecifierDestAddr = _CMTPathSpecifierDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 1, 19, 1, 5),
    _CMTPathSpecifierDestAddr_Type()
)
cMTPathSpecifierDestAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cMTPathSpecifierDestAddr.setStatus("current")
_CMTPathSpecifierDestPort_Type = InetPortNumber
_CMTPathSpecifierDestPort_Object = MibTableColumn
cMTPathSpecifierDestPort = _CMTPathSpecifierDestPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 1, 19, 1, 6),
    _CMTPathSpecifierDestPort_Type()
)
cMTPathSpecifierDestPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cMTPathSpecifierDestPort.setStatus("current")
_CMTPathSpecifierSourceAddrType_Type = InetAddressType
_CMTPathSpecifierSourceAddrType_Object = MibTableColumn
cMTPathSpecifierSourceAddrType = _CMTPathSpecifierSourceAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 1, 19, 1, 7),
    _CMTPathSpecifierSourceAddrType_Type()
)
cMTPathSpecifierSourceAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cMTPathSpecifierSourceAddrType.setStatus("current")
_CMTPathSpecifierSourceAddr_Type = InetAddress
_CMTPathSpecifierSourceAddr_Object = MibTableColumn
cMTPathSpecifierSourceAddr = _CMTPathSpecifierSourceAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 1, 19, 1, 8),
    _CMTPathSpecifierSourceAddr_Type()
)
cMTPathSpecifierSourceAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cMTPathSpecifierSourceAddr.setStatus("current")
_CMTPathSpecifierSourcePort_Type = InetPortNumber
_CMTPathSpecifierSourcePort_Object = MibTableColumn
cMTPathSpecifierSourcePort = _CMTPathSpecifierSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 1, 19, 1, 9),
    _CMTPathSpecifierSourcePort_Type()
)
cMTPathSpecifierSourcePort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cMTPathSpecifierSourcePort.setStatus("current")


class _CMTPathSpecifierProtocolForDiscovery_Type(CiscoMediatraceDiscoveryProtocol):
    """Custom type cMTPathSpecifierProtocolForDiscovery based on CiscoMediatraceDiscoveryProtocol"""


_CMTPathSpecifierProtocolForDiscovery_Object = MibTableColumn
cMTPathSpecifierProtocolForDiscovery = _CMTPathSpecifierProtocolForDiscovery_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 1, 19, 1, 10),
    _CMTPathSpecifierProtocolForDiscovery_Type()
)
cMTPathSpecifierProtocolForDiscovery.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cMTPathSpecifierProtocolForDiscovery.setStatus("current")
_CMTPathSpecifierGatewayAddrType_Type = InetAddressType
_CMTPathSpecifierGatewayAddrType_Object = MibTableColumn
cMTPathSpecifierGatewayAddrType = _CMTPathSpecifierGatewayAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 1, 19, 1, 11),
    _CMTPathSpecifierGatewayAddrType_Type()
)
cMTPathSpecifierGatewayAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cMTPathSpecifierGatewayAddrType.setStatus("current")
_CMTPathSpecifierGatewayAddr_Type = InetAddress
_CMTPathSpecifierGatewayAddr_Object = MibTableColumn
cMTPathSpecifierGatewayAddr = _CMTPathSpecifierGatewayAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 1, 19, 1, 12),
    _CMTPathSpecifierGatewayAddr_Type()
)
cMTPathSpecifierGatewayAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cMTPathSpecifierGatewayAddr.setStatus("current")


class _CMTPathSpecifierGatewayVlanId_Type(VlanId):
    """Custom type cMTPathSpecifierGatewayVlanId based on VlanId"""
    subtypeSpec = VlanId.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_CMTPathSpecifierGatewayVlanId_Type.__name__ = "VlanId"
_CMTPathSpecifierGatewayVlanId_Object = MibTableColumn
cMTPathSpecifierGatewayVlanId = _CMTPathSpecifierGatewayVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 1, 19, 1, 13),
    _CMTPathSpecifierGatewayVlanId_Type()
)
cMTPathSpecifierGatewayVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cMTPathSpecifierGatewayVlanId.setStatus("current")


class _CMTPathSpecifierIpProtocol_Type(CiscoMediatraceSupportProtocol):
    """Custom type cMTPathSpecifierIpProtocol based on CiscoMediatraceSupportProtocol"""


_CMTPathSpecifierIpProtocol_Object = MibTableColumn
cMTPathSpecifierIpProtocol = _CMTPathSpecifierIpProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 1, 19, 1, 14),
    _CMTPathSpecifierIpProtocol_Type()
)
cMTPathSpecifierIpProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cMTPathSpecifierIpProtocol.setStatus("current")
_CMTSessionParamsTable_Object = MibTable
cMTSessionParamsTable = _CMTSessionParamsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 1, 20)
)
if mibBuilder.loadTexts:
    cMTSessionParamsTable.setStatus("current")
_CMTSessionParamsEntry_Object = MibTableRow
cMTSessionParamsEntry = _CMTSessionParamsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 1, 20, 1)
)
cMTSessionParamsEntry.setIndexNames(
    (0, "CISCO-MEDIATRACE-MIB", "cMTSessionParamsName"),
)
if mibBuilder.loadTexts:
    cMTSessionParamsEntry.setStatus("current")
_CMTSessionParamsName_Type = SnmpAdminString
_CMTSessionParamsName_Object = MibTableColumn
cMTSessionParamsName = _CMTSessionParamsName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 1, 20, 1, 1),
    _CMTSessionParamsName_Type()
)
cMTSessionParamsName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cMTSessionParamsName.setStatus("current")
_CMTSessionParamsRowStatus_Type = RowStatus
_CMTSessionParamsRowStatus_Object = MibTableColumn
cMTSessionParamsRowStatus = _CMTSessionParamsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 1, 20, 1, 2),
    _CMTSessionParamsRowStatus_Type()
)
cMTSessionParamsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cMTSessionParamsRowStatus.setStatus("current")


class _CMTSessionParamsResponseTimeout_Type(Unsigned32):
    """Custom type cMTSessionParamsResponseTimeout based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CMTSessionParamsResponseTimeout_Type.__name__ = "Unsigned32"
_CMTSessionParamsResponseTimeout_Object = MibTableColumn
cMTSessionParamsResponseTimeout = _CMTSessionParamsResponseTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 1, 20, 1, 3),
    _CMTSessionParamsResponseTimeout_Type()
)
cMTSessionParamsResponseTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cMTSessionParamsResponseTimeout.setStatus("current")
if mibBuilder.loadTexts:
    cMTSessionParamsResponseTimeout.setUnits("seconds")


class _CMTSessionParamsFrequency_Type(Unsigned32):
    """Custom type cMTSessionParamsFrequency based on Unsigned32"""
    defaultValue = 120

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 3600),
    )


_CMTSessionParamsFrequency_Type.__name__ = "Unsigned32"
_CMTSessionParamsFrequency_Object = MibTableColumn
cMTSessionParamsFrequency = _CMTSessionParamsFrequency_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 1, 20, 1, 4),
    _CMTSessionParamsFrequency_Type()
)
cMTSessionParamsFrequency.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cMTSessionParamsFrequency.setStatus("current")
if mibBuilder.loadTexts:
    cMTSessionParamsFrequency.setUnits("seconds")


class _CMTSessionParamsInactivityTimeout_Type(Unsigned32):
    """Custom type cMTSessionParamsInactivityTimeout based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10800),
    )


_CMTSessionParamsInactivityTimeout_Type.__name__ = "Unsigned32"
_CMTSessionParamsInactivityTimeout_Object = MibTableColumn
cMTSessionParamsInactivityTimeout = _CMTSessionParamsInactivityTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 1, 20, 1, 5),
    _CMTSessionParamsInactivityTimeout_Type()
)
cMTSessionParamsInactivityTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cMTSessionParamsInactivityTimeout.setStatus("current")
if mibBuilder.loadTexts:
    cMTSessionParamsInactivityTimeout.setUnits("sconds")


class _CMTSessionParamsHistoryBuckets_Type(Unsigned32):
    """Custom type cMTSessionParamsHistoryBuckets based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_CMTSessionParamsHistoryBuckets_Type.__name__ = "Unsigned32"
_CMTSessionParamsHistoryBuckets_Object = MibTableColumn
cMTSessionParamsHistoryBuckets = _CMTSessionParamsHistoryBuckets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 1, 20, 1, 6),
    _CMTSessionParamsHistoryBuckets_Type()
)
cMTSessionParamsHistoryBuckets.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cMTSessionParamsHistoryBuckets.setStatus("current")
if mibBuilder.loadTexts:
    cMTSessionParamsHistoryBuckets.setUnits("buckets")


class _CMTSessionParamsRouteChangeReactiontime_Type(Unsigned32):
    """Custom type cMTSessionParamsRouteChangeReactiontime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_CMTSessionParamsRouteChangeReactiontime_Type.__name__ = "Unsigned32"
_CMTSessionParamsRouteChangeReactiontime_Object = MibTableColumn
cMTSessionParamsRouteChangeReactiontime = _CMTSessionParamsRouteChangeReactiontime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 1, 20, 1, 7),
    _CMTSessionParamsRouteChangeReactiontime_Type()
)
cMTSessionParamsRouteChangeReactiontime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cMTSessionParamsRouteChangeReactiontime.setStatus("current")
if mibBuilder.loadTexts:
    cMTSessionParamsRouteChangeReactiontime.setUnits("seconds")
_CMTMediaMonitorProfileTable_Object = MibTable
cMTMediaMonitorProfileTable = _CMTMediaMonitorProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 1, 21)
)
if mibBuilder.loadTexts:
    cMTMediaMonitorProfileTable.setStatus("current")
_CMTMediaMonitorProfileEntry_Object = MibTableRow
cMTMediaMonitorProfileEntry = _CMTMediaMonitorProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 1, 21, 1)
)
cMTMediaMonitorProfileEntry.setIndexNames(
    (0, "CISCO-MEDIATRACE-MIB", "cMTMediaMonitorProfileName"),
)
if mibBuilder.loadTexts:
    cMTMediaMonitorProfileEntry.setStatus("current")
_CMTMediaMonitorProfileName_Type = SnmpAdminString
_CMTMediaMonitorProfileName_Object = MibTableColumn
cMTMediaMonitorProfileName = _CMTMediaMonitorProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 1, 21, 1, 1),
    _CMTMediaMonitorProfileName_Type()
)
cMTMediaMonitorProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cMTMediaMonitorProfileName.setStatus("current")
_CMTMediaMonitorProfileRowStatus_Type = RowStatus
_CMTMediaMonitorProfileRowStatus_Object = MibTableColumn
cMTMediaMonitorProfileRowStatus = _CMTMediaMonitorProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 1, 21, 1, 2),
    _CMTMediaMonitorProfileRowStatus_Type()
)
cMTMediaMonitorProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cMTMediaMonitorProfileRowStatus.setStatus("current")


class _CMTMediaMonitorProfileMetric_Type(Integer32):
    """Custom type cMTMediaMonitorProfileMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rtp", 1),
          ("tcp", 2))
    )


_CMTMediaMonitorProfileMetric_Type.__name__ = "Integer32"
_CMTMediaMonitorProfileMetric_Object = MibTableColumn
cMTMediaMonitorProfileMetric = _CMTMediaMonitorProfileMetric_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 1, 21, 1, 3),
    _CMTMediaMonitorProfileMetric_Type()
)
cMTMediaMonitorProfileMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cMTMediaMonitorProfileMetric.setStatus("current")


class _CMTMediaMonitorProfileInterval_Type(Unsigned32):
    """Custom type cMTMediaMonitorProfileInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 120),
    )


_CMTMediaMonitorProfileInterval_Type.__name__ = "Unsigned32"
_CMTMediaMonitorProfileInterval_Object = MibTableColumn
cMTMediaMonitorProfileInterval = _CMTMediaMonitorProfileInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 1, 21, 1, 4),
    _CMTMediaMonitorProfileInterval_Type()
)
cMTMediaMonitorProfileInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cMTMediaMonitorProfileInterval.setStatus("current")
if mibBuilder.loadTexts:
    cMTMediaMonitorProfileInterval.setUnits("seconds")


class _CMTMediaMonitorProfileRtpMaxDropout_Type(Unsigned32):
    """Custom type cMTMediaMonitorProfileRtpMaxDropout based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_CMTMediaMonitorProfileRtpMaxDropout_Type.__name__ = "Unsigned32"
_CMTMediaMonitorProfileRtpMaxDropout_Object = MibTableColumn
cMTMediaMonitorProfileRtpMaxDropout = _CMTMediaMonitorProfileRtpMaxDropout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 1, 21, 1, 5),
    _CMTMediaMonitorProfileRtpMaxDropout_Type()
)
cMTMediaMonitorProfileRtpMaxDropout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cMTMediaMonitorProfileRtpMaxDropout.setStatus("current")
if mibBuilder.loadTexts:
    cMTMediaMonitorProfileRtpMaxDropout.setUnits("packets")


class _CMTMediaMonitorProfileRtpMaxReorder_Type(Unsigned32):
    """Custom type cMTMediaMonitorProfileRtpMaxReorder based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_CMTMediaMonitorProfileRtpMaxReorder_Type.__name__ = "Unsigned32"
_CMTMediaMonitorProfileRtpMaxReorder_Object = MibTableColumn
cMTMediaMonitorProfileRtpMaxReorder = _CMTMediaMonitorProfileRtpMaxReorder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 1, 21, 1, 6),
    _CMTMediaMonitorProfileRtpMaxReorder_Type()
)
cMTMediaMonitorProfileRtpMaxReorder.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cMTMediaMonitorProfileRtpMaxReorder.setStatus("current")
if mibBuilder.loadTexts:
    cMTMediaMonitorProfileRtpMaxReorder.setUnits("packets")


class _CMTMediaMonitorProfileRtpMinimalSequential_Type(Unsigned32):
    """Custom type cMTMediaMonitorProfileRtpMinimalSequential based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 10),
    )


_CMTMediaMonitorProfileRtpMinimalSequential_Type.__name__ = "Unsigned32"
_CMTMediaMonitorProfileRtpMinimalSequential_Object = MibTableColumn
cMTMediaMonitorProfileRtpMinimalSequential = _CMTMediaMonitorProfileRtpMinimalSequential_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 1, 21, 1, 7),
    _CMTMediaMonitorProfileRtpMinimalSequential_Type()
)
cMTMediaMonitorProfileRtpMinimalSequential.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cMTMediaMonitorProfileRtpMinimalSequential.setStatus("current")
if mibBuilder.loadTexts:
    cMTMediaMonitorProfileRtpMinimalSequential.setUnits("packets")
_CMTSystemProfileTable_Object = MibTable
cMTSystemProfileTable = _CMTSystemProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 1, 22)
)
if mibBuilder.loadTexts:
    cMTSystemProfileTable.setStatus("current")
_CMTSystemProfileEntry_Object = MibTableRow
cMTSystemProfileEntry = _CMTSystemProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 1, 22, 1)
)
cMTSystemProfileEntry.setIndexNames(
    (0, "CISCO-MEDIATRACE-MIB", "cMTSystemProfileName"),
)
if mibBuilder.loadTexts:
    cMTSystemProfileEntry.setStatus("current")
_CMTSystemProfileName_Type = SnmpAdminString
_CMTSystemProfileName_Object = MibTableColumn
cMTSystemProfileName = _CMTSystemProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 1, 22, 1, 1),
    _CMTSystemProfileName_Type()
)
cMTSystemProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cMTSystemProfileName.setStatus("current")
_CMTSystemProfileRowStatus_Type = RowStatus
_CMTSystemProfileRowStatus_Object = MibTableColumn
cMTSystemProfileRowStatus = _CMTSystemProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 1, 22, 1, 2),
    _CMTSystemProfileRowStatus_Type()
)
cMTSystemProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cMTSystemProfileRowStatus.setStatus("current")


class _CMTSystemProfileMetric_Type(Integer32):
    """Custom type cMTSystemProfileMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cpu", 2),
          ("interface", 1),
          ("memory", 3))
    )


_CMTSystemProfileMetric_Type.__name__ = "Integer32"
_CMTSystemProfileMetric_Object = MibTableColumn
cMTSystemProfileMetric = _CMTSystemProfileMetric_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 1, 22, 1, 3),
    _CMTSystemProfileMetric_Type()
)
cMTSystemProfileMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cMTSystemProfileMetric.setStatus("current")
_CMTSessionTable_Object = MibTable
cMTSessionTable = _CMTSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 1, 23)
)
if mibBuilder.loadTexts:
    cMTSessionTable.setStatus("current")
_CMTSessionEntry_Object = MibTableRow
cMTSessionEntry = _CMTSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 1, 23, 1)
)
cMTSessionEntry.setIndexNames(
    (0, "CISCO-MEDIATRACE-MIB", "cMTSessionNumber"),
)
if mibBuilder.loadTexts:
    cMTSessionEntry.setStatus("current")


class _CMTSessionNumber_Type(Unsigned32):
    """Custom type cMTSessionNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CMTSessionNumber_Type.__name__ = "Unsigned32"
_CMTSessionNumber_Object = MibTableColumn
cMTSessionNumber = _CMTSessionNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 1, 23, 1, 2),
    _CMTSessionNumber_Type()
)
cMTSessionNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cMTSessionNumber.setStatus("current")
_CMTSessionRowStatus_Type = RowStatus
_CMTSessionRowStatus_Object = MibTableColumn
cMTSessionRowStatus = _CMTSessionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 1, 23, 1, 3),
    _CMTSessionRowStatus_Type()
)
cMTSessionRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cMTSessionRowStatus.setStatus("current")
_CMTSessionPathSpecifierName_Type = SnmpAdminString
_CMTSessionPathSpecifierName_Object = MibTableColumn
cMTSessionPathSpecifierName = _CMTSessionPathSpecifierName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 1, 23, 1, 4),
    _CMTSessionPathSpecifierName_Type()
)
cMTSessionPathSpecifierName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cMTSessionPathSpecifierName.setStatus("current")
_CMTSessionParamName_Type = SnmpAdminString
_CMTSessionParamName_Object = MibTableColumn
cMTSessionParamName = _CMTSessionParamName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 1, 23, 1, 5),
    _CMTSessionParamName_Type()
)
cMTSessionParamName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cMTSessionParamName.setStatus("current")
_CMTSessionProfileName_Type = SnmpAdminString
_CMTSessionProfileName_Object = MibTableColumn
cMTSessionProfileName = _CMTSessionProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 1, 23, 1, 6),
    _CMTSessionProfileName_Type()
)
cMTSessionProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cMTSessionProfileName.setStatus("current")
_CMTSessionFlowSpecifierName_Type = SnmpAdminString
_CMTSessionFlowSpecifierName_Object = MibTableColumn
cMTSessionFlowSpecifierName = _CMTSessionFlowSpecifierName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 1, 23, 1, 7),
    _CMTSessionFlowSpecifierName_Type()
)
cMTSessionFlowSpecifierName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cMTSessionFlowSpecifierName.setStatus("current")
_CMTSessionTraceRouteEnabled_Type = TruthValue
_CMTSessionTraceRouteEnabled_Object = MibTableColumn
cMTSessionTraceRouteEnabled = _CMTSessionTraceRouteEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 1, 23, 1, 8),
    _CMTSessionTraceRouteEnabled_Type()
)
cMTSessionTraceRouteEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cMTSessionTraceRouteEnabled.setStatus("current")
_CMTScheduleTable_Object = MibTable
cMTScheduleTable = _CMTScheduleTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 1, 24)
)
if mibBuilder.loadTexts:
    cMTScheduleTable.setStatus("current")
_CMTScheduleEntry_Object = MibTableRow
cMTScheduleEntry = _CMTScheduleEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 1, 24, 1)
)
cMTScheduleEntry.setIndexNames(
    (0, "CISCO-MEDIATRACE-MIB", "cMTSessionNumber"),
)
if mibBuilder.loadTexts:
    cMTScheduleEntry.setStatus("current")
_CMTScheduleRowStatus_Type = RowStatus
_CMTScheduleRowStatus_Object = MibTableColumn
cMTScheduleRowStatus = _CMTScheduleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 1, 24, 1, 1),
    _CMTScheduleRowStatus_Type()
)
cMTScheduleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cMTScheduleRowStatus.setStatus("current")
_CMTScheduleStartTime_Type = TimeStamp
_CMTScheduleStartTime_Object = MibTableColumn
cMTScheduleStartTime = _CMTScheduleStartTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 1, 24, 1, 2),
    _CMTScheduleStartTime_Type()
)
cMTScheduleStartTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cMTScheduleStartTime.setStatus("current")


class _CMTScheduleLife_Type(Unsigned32):
    """Custom type cMTScheduleLife based on Unsigned32"""
    defaultValue = 3600

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CMTScheduleLife_Type.__name__ = "Unsigned32"
_CMTScheduleLife_Object = MibTableColumn
cMTScheduleLife = _CMTScheduleLife_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 1, 24, 1, 3),
    _CMTScheduleLife_Type()
)
cMTScheduleLife.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cMTScheduleLife.setStatus("current")
if mibBuilder.loadTexts:
    cMTScheduleLife.setUnits("seconds")


class _CMTScheduleEntryAgeout_Type(Unsigned32):
    """Custom type cMTScheduleEntryAgeout based on Unsigned32"""
    defaultValue = 3600

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2073600),
    )


_CMTScheduleEntryAgeout_Type.__name__ = "Unsigned32"
_CMTScheduleEntryAgeout_Object = MibTableColumn
cMTScheduleEntryAgeout = _CMTScheduleEntryAgeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 1, 24, 1, 4),
    _CMTScheduleEntryAgeout_Type()
)
cMTScheduleEntryAgeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cMTScheduleEntryAgeout.setStatus("current")
if mibBuilder.loadTexts:
    cMTScheduleEntryAgeout.setUnits("seconds")
_CMTScheduleRecurring_Type = TruthValue
_CMTScheduleRecurring_Object = MibTableColumn
cMTScheduleRecurring = _CMTScheduleRecurring_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 1, 24, 1, 5),
    _CMTScheduleRecurring_Type()
)
cMTScheduleRecurring.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cMTScheduleRecurring.setStatus("current")
_CMTStats_ObjectIdentity = ObjectIdentity
cMTStats = _CMTStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 2)
)
_CMTPathTable_Object = MibTable
cMTPathTable = _CMTPathTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cMTPathTable.setStatus("current")
_CMTPathEntry_Object = MibTableRow
cMTPathEntry = _CMTPathEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 2, 1, 1)
)
cMTPathEntry.setIndexNames(
    (0, "CISCO-MEDIATRACE-MIB", "cMTSessionNumber"),
    (0, "CISCO-MEDIATRACE-MIB", "cMTSessionLifeNumber"),
    (0, "CISCO-MEDIATRACE-MIB", "cMTBucketNumber"),
    (0, "CISCO-MEDIATRACE-MIB", "cMTPathHopNumber"),
)
if mibBuilder.loadTexts:
    cMTPathEntry.setStatus("current")


class _CMTSessionLifeNumber_Type(Unsigned32):
    """Custom type cMTSessionLifeNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_CMTSessionLifeNumber_Type.__name__ = "Unsigned32"
_CMTSessionLifeNumber_Object = MibTableColumn
cMTSessionLifeNumber = _CMTSessionLifeNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 2, 1, 1, 1),
    _CMTSessionLifeNumber_Type()
)
cMTSessionLifeNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cMTSessionLifeNumber.setStatus("current")


class _CMTBucketNumber_Type(Unsigned32):
    """Custom type cMTBucketNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_CMTBucketNumber_Type.__name__ = "Unsigned32"
_CMTBucketNumber_Object = MibTableColumn
cMTBucketNumber = _CMTBucketNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 2, 1, 1, 2),
    _CMTBucketNumber_Type()
)
cMTBucketNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cMTBucketNumber.setStatus("current")


class _CMTPathHopNumber_Type(Unsigned32):
    """Custom type cMTPathHopNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CMTPathHopNumber_Type.__name__ = "Unsigned32"
_CMTPathHopNumber_Object = MibTableColumn
cMTPathHopNumber = _CMTPathHopNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 2, 1, 1, 3),
    _CMTPathHopNumber_Type()
)
cMTPathHopNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cMTPathHopNumber.setStatus("current")
_CMTPathHopAddrType_Type = InetAddressType
_CMTPathHopAddrType_Object = MibTableColumn
cMTPathHopAddrType = _CMTPathHopAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 2, 1, 1, 4),
    _CMTPathHopAddrType_Type()
)
cMTPathHopAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMTPathHopAddrType.setStatus("current")
_CMTPathHopAddr_Type = InetAddress
_CMTPathHopAddr_Object = MibTableColumn
cMTPathHopAddr = _CMTPathHopAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 2, 1, 1, 5),
    _CMTPathHopAddr_Type()
)
cMTPathHopAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMTPathHopAddr.setStatus("current")


class _CMTPathHopType_Type(Integer32):
    """Custom type cMTPathHopType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mediatrace", 1),
          ("traceroute", 2))
    )


_CMTPathHopType_Type.__name__ = "Integer32"
_CMTPathHopType_Object = MibTableColumn
cMTPathHopType = _CMTPathHopType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 2, 1, 1, 6),
    _CMTPathHopType_Type()
)
cMTPathHopType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMTPathHopType.setStatus("current")
_CMTPathHopAlternate1AddrType_Type = InetAddressType
_CMTPathHopAlternate1AddrType_Object = MibTableColumn
cMTPathHopAlternate1AddrType = _CMTPathHopAlternate1AddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 2, 1, 1, 7),
    _CMTPathHopAlternate1AddrType_Type()
)
cMTPathHopAlternate1AddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMTPathHopAlternate1AddrType.setStatus("current")
_CMTPathHopAlternate1Addr_Type = InetAddress
_CMTPathHopAlternate1Addr_Object = MibTableColumn
cMTPathHopAlternate1Addr = _CMTPathHopAlternate1Addr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 2, 1, 1, 8),
    _CMTPathHopAlternate1Addr_Type()
)
cMTPathHopAlternate1Addr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMTPathHopAlternate1Addr.setStatus("current")
_CMTPathHopAlternate2AddrType_Type = InetAddressType
_CMTPathHopAlternate2AddrType_Object = MibTableColumn
cMTPathHopAlternate2AddrType = _CMTPathHopAlternate2AddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 2, 1, 1, 9),
    _CMTPathHopAlternate2AddrType_Type()
)
cMTPathHopAlternate2AddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMTPathHopAlternate2AddrType.setStatus("current")
_CMTPathHopAlternate2Addr_Type = InetAddress
_CMTPathHopAlternate2Addr_Object = MibTableColumn
cMTPathHopAlternate2Addr = _CMTPathHopAlternate2Addr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 2, 1, 1, 10),
    _CMTPathHopAlternate2Addr_Type()
)
cMTPathHopAlternate2Addr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMTPathHopAlternate2Addr.setStatus("current")
_CMTPathHopAlternate3AddrType_Type = InetAddressType
_CMTPathHopAlternate3AddrType_Object = MibTableColumn
cMTPathHopAlternate3AddrType = _CMTPathHopAlternate3AddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 2, 1, 1, 11),
    _CMTPathHopAlternate3AddrType_Type()
)
cMTPathHopAlternate3AddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMTPathHopAlternate3AddrType.setStatus("current")
_CMTPathHopAlternate3Addr_Type = InetAddress
_CMTPathHopAlternate3Addr_Object = MibTableColumn
cMTPathHopAlternate3Addr = _CMTPathHopAlternate3Addr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 2, 1, 1, 12),
    _CMTPathHopAlternate3Addr_Type()
)
cMTPathHopAlternate3Addr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMTPathHopAlternate3Addr.setStatus("current")
_CMTHopStatsTable_Object = MibTable
cMTHopStatsTable = _CMTHopStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 2, 2)
)
if mibBuilder.loadTexts:
    cMTHopStatsTable.setStatus("current")
_CMTHopStatsEntry_Object = MibTableRow
cMTHopStatsEntry = _CMTHopStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 2, 2, 1)
)
cMTHopStatsEntry.setIndexNames(
    (0, "CISCO-MEDIATRACE-MIB", "cMTSessionNumber"),
    (0, "CISCO-MEDIATRACE-MIB", "cMTSessionLifeNumber"),
    (0, "CISCO-MEDIATRACE-MIB", "cMTBucketNumber"),
    (0, "CISCO-MEDIATRACE-MIB", "cMTHopStatsAddrType"),
    (0, "CISCO-MEDIATRACE-MIB", "cMTHopStatsAddr"),
)
if mibBuilder.loadTexts:
    cMTHopStatsEntry.setStatus("current")


class _CMTHopStatsMaskBitmaps_Type(Bits):
    """Custom type cMTHopStatsMaskBitmaps based on Bits"""
    namedValues = NamedValues(
        *(("collectionStatsUncollected", 3),
          ("collectionStatsUnsupported", 2),
          ("egressInterfaceUncollected", 7),
          ("egressInterfaceUnsupported", 6),
          ("ingressInterfaceUncollected", 5),
          ("ingressInterfaceUnsupported", 4),
          ("mediatraceTtlUncollected", 1),
          ("mediatraceTtlUnsupported", 0))
    )

_CMTHopStatsMaskBitmaps_Type.__name__ = "Bits"
_CMTHopStatsMaskBitmaps_Object = MibTableColumn
cMTHopStatsMaskBitmaps = _CMTHopStatsMaskBitmaps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 2, 2, 1, 1),
    _CMTHopStatsMaskBitmaps_Type()
)
cMTHopStatsMaskBitmaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMTHopStatsMaskBitmaps.setStatus("current")
_CMTHopStatsAddrType_Type = InetAddressType
_CMTHopStatsAddrType_Object = MibTableColumn
cMTHopStatsAddrType = _CMTHopStatsAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 2, 2, 1, 2),
    _CMTHopStatsAddrType_Type()
)
cMTHopStatsAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cMTHopStatsAddrType.setStatus("current")
_CMTHopStatsAddr_Type = InetAddress
_CMTHopStatsAddr_Object = MibTableColumn
cMTHopStatsAddr = _CMTHopStatsAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 2, 2, 1, 3),
    _CMTHopStatsAddr_Type()
)
cMTHopStatsAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cMTHopStatsAddr.setStatus("current")
_CMTHopStatsName_Type = SnmpAdminString
_CMTHopStatsName_Object = MibTableColumn
cMTHopStatsName = _CMTHopStatsName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 2, 2, 1, 4),
    _CMTHopStatsName_Type()
)
cMTHopStatsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMTHopStatsName.setStatus("current")


class _CMTHopStatsMediatraceTtl_Type(Unsigned32):
    """Custom type cMTHopStatsMediatraceTtl based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CMTHopStatsMediatraceTtl_Type.__name__ = "Unsigned32"
_CMTHopStatsMediatraceTtl_Object = MibTableColumn
cMTHopStatsMediatraceTtl = _CMTHopStatsMediatraceTtl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 2, 2, 1, 5),
    _CMTHopStatsMediatraceTtl_Type()
)
cMTHopStatsMediatraceTtl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMTHopStatsMediatraceTtl.setStatus("current")


class _CMTHopStatsCollectionStatus_Type(Integer32):
    """Custom type cMTHopStatsCollectionStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notSuccess", 2),
          ("success", 1))
    )


_CMTHopStatsCollectionStatus_Type.__name__ = "Integer32"
_CMTHopStatsCollectionStatus_Object = MibTableColumn
cMTHopStatsCollectionStatus = _CMTHopStatsCollectionStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 2, 2, 1, 6),
    _CMTHopStatsCollectionStatus_Type()
)
cMTHopStatsCollectionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMTHopStatsCollectionStatus.setStatus("current")
_CMTHopStatsIngressInterface_Type = SnmpAdminString
_CMTHopStatsIngressInterface_Object = MibTableColumn
cMTHopStatsIngressInterface = _CMTHopStatsIngressInterface_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 2, 2, 1, 7),
    _CMTHopStatsIngressInterface_Type()
)
cMTHopStatsIngressInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMTHopStatsIngressInterface.setStatus("current")
_CMTHopStatsEgressInterface_Type = SnmpAdminString
_CMTHopStatsEgressInterface_Object = MibTableColumn
cMTHopStatsEgressInterface = _CMTHopStatsEgressInterface_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 2, 2, 1, 8),
    _CMTHopStatsEgressInterface_Type()
)
cMTHopStatsEgressInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMTHopStatsEgressInterface.setStatus("current")
_CMTTraceRouteTable_Object = MibTable
cMTTraceRouteTable = _CMTTraceRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 2, 3)
)
if mibBuilder.loadTexts:
    cMTTraceRouteTable.setStatus("current")
_CMTTraceRouteEntry_Object = MibTableRow
cMTTraceRouteEntry = _CMTTraceRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 2, 3, 1)
)
cMTTraceRouteEntry.setIndexNames(
    (0, "CISCO-MEDIATRACE-MIB", "cMTSessionNumber"),
    (0, "CISCO-MEDIATRACE-MIB", "cMTSessionLifeNumber"),
    (0, "CISCO-MEDIATRACE-MIB", "cMTBucketNumber"),
    (0, "CISCO-MEDIATRACE-MIB", "cMTHopStatsAddrType"),
    (0, "CISCO-MEDIATRACE-MIB", "cMTHopStatsAddr"),
)
if mibBuilder.loadTexts:
    cMTTraceRouteEntry.setStatus("current")
_CMTTraceRouteHopNumber_Type = Gauge32
_CMTTraceRouteHopNumber_Object = MibTableColumn
cMTTraceRouteHopNumber = _CMTTraceRouteHopNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 2, 3, 1, 1),
    _CMTTraceRouteHopNumber_Type()
)
cMTTraceRouteHopNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMTTraceRouteHopNumber.setStatus("current")
_CMTTraceRouteHopRtt_Type = Counter64
_CMTTraceRouteHopRtt_Object = MibTableColumn
cMTTraceRouteHopRtt = _CMTTraceRouteHopRtt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 2, 3, 1, 2),
    _CMTTraceRouteHopRtt_Type()
)
cMTTraceRouteHopRtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMTTraceRouteHopRtt.setStatus("current")
_CMTSessionStatusTable_Object = MibTable
cMTSessionStatusTable = _CMTSessionStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 2, 4)
)
if mibBuilder.loadTexts:
    cMTSessionStatusTable.setStatus("current")
_CMTSessionStatusEntry_Object = MibTableRow
cMTSessionStatusEntry = _CMTSessionStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 2, 4, 1)
)
cMTSessionStatusEntry.setIndexNames(
    (0, "CISCO-MEDIATRACE-MIB", "cMTSessionNumber"),
)
if mibBuilder.loadTexts:
    cMTSessionStatusEntry.setStatus("current")


class _CMTSessionStatusBitmaps_Type(Bits):
    """Custom type cMTSessionStatusBitmaps based on Bits"""
    namedValues = NamedValues(
        *(("globalSessionIdUncollected", 1),
          ("globalSessionIdUusupport", 0),
          ("operationStateUncollected", 3),
          ("operationStateUusupport", 2),
          ("operationTimeToLiveUncollected", 5),
          ("operationTimeToLiveUusupport", 4))
    )

_CMTSessionStatusBitmaps_Type.__name__ = "Bits"
_CMTSessionStatusBitmaps_Object = MibTableColumn
cMTSessionStatusBitmaps = _CMTSessionStatusBitmaps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 2, 4, 1, 1),
    _CMTSessionStatusBitmaps_Type()
)
cMTSessionStatusBitmaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMTSessionStatusBitmaps.setStatus("current")
_CMTSessionStatusGlobalSessionId_Type = Unsigned32
_CMTSessionStatusGlobalSessionId_Object = MibTableColumn
cMTSessionStatusGlobalSessionId = _CMTSessionStatusGlobalSessionId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 2, 4, 1, 2),
    _CMTSessionStatusGlobalSessionId_Type()
)
cMTSessionStatusGlobalSessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMTSessionStatusGlobalSessionId.setStatus("current")


class _CMTSessionStatusOperationState_Type(Integer32):
    """Custom type cMTSessionStatusOperationState based on Integer32"""
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
        *(("active", 2),
          ("inactive", 3),
          ("pending", 1),
          ("sleep", 4))
    )


_CMTSessionStatusOperationState_Type.__name__ = "Integer32"
_CMTSessionStatusOperationState_Object = MibTableColumn
cMTSessionStatusOperationState = _CMTSessionStatusOperationState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 2, 4, 1, 3),
    _CMTSessionStatusOperationState_Type()
)
cMTSessionStatusOperationState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMTSessionStatusOperationState.setStatus("current")
_CMTSessionStatusOperationTimeToLive_Type = Counter64
_CMTSessionStatusOperationTimeToLive_Object = MibTableColumn
cMTSessionStatusOperationTimeToLive = _CMTSessionStatusOperationTimeToLive_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 2, 4, 1, 4),
    _CMTSessionStatusOperationTimeToLive_Type()
)
cMTSessionStatusOperationTimeToLive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMTSessionStatusOperationTimeToLive.setStatus("current")
_CMTSessionRequestStatsTable_Object = MibTable
cMTSessionRequestStatsTable = _CMTSessionRequestStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 2, 5)
)
if mibBuilder.loadTexts:
    cMTSessionRequestStatsTable.setStatus("current")
_CMTSessionRequestStatsEntry_Object = MibTableRow
cMTSessionRequestStatsEntry = _CMTSessionRequestStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 2, 5, 1)
)
cMTSessionRequestStatsEntry.setIndexNames(
    (0, "CISCO-MEDIATRACE-MIB", "cMTSessionNumber"),
    (0, "CISCO-MEDIATRACE-MIB", "cMTSessionLifeNumber"),
    (0, "CISCO-MEDIATRACE-MIB", "cMTBucketNumber"),
)
if mibBuilder.loadTexts:
    cMTSessionRequestStatsEntry.setStatus("current")


class _CMTSessionRequestStatsBitmaps_Type(Bits):
    """Custom type cMTSessionRequestStatsBitmaps based on Bits"""
    namedValues = NamedValues(
        *(("metaAppNameUncollected", 23),
          ("metaAppNameUnsupport", 22),
          ("metaGlobalIdUncollected", 19),
          ("metaGlobalIdUnsupport", 18),
          ("metaMultiPartySessionIdUncollected", 21),
          ("metaMultiPartySessionIdUnsupport", 20),
          ("numberOfErrorHopsUncollected", 15),
          ("numberOfErrorHopsUnsupport", 14),
          ("numberOfMediatraceHopsUncollected", 9),
          ("numberOfMediatraceHopsUnsupport", 8),
          ("numberOfNoDataRecordHopsUncollected", 17),
          ("numberOfNoDataRecordHopsUnsupport", 16),
          ("numberOfNonMediatraceHopsUncollected", 11),
          ("numberOfNonMediatraceHopsUnsupport", 10),
          ("numberOfValidHopsUncollected", 13),
          ("numberOfValidHopsUnsupport", 12),
          ("requestStatusUncollected", 3),
          ("requestStatusUnsupport", 2),
          ("requestTimestampUncollected", 1),
          ("requestTimestampUnsupport", 0),
          ("routeIndexUncollected", 7),
          ("routeIndexUnsupport", 6),
          ("tracerouteStatusUncollected", 5),
          ("tracerouteStatusUnsupport", 4))
    )

_CMTSessionRequestStatsBitmaps_Type.__name__ = "Bits"
_CMTSessionRequestStatsBitmaps_Object = MibTableColumn
cMTSessionRequestStatsBitmaps = _CMTSessionRequestStatsBitmaps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 2, 5, 1, 1),
    _CMTSessionRequestStatsBitmaps_Type()
)
cMTSessionRequestStatsBitmaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMTSessionRequestStatsBitmaps.setStatus("current")
_CMTSessionRequestStatsRequestTimestamp_Type = TimeStamp
_CMTSessionRequestStatsRequestTimestamp_Object = MibTableColumn
cMTSessionRequestStatsRequestTimestamp = _CMTSessionRequestStatsRequestTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 2, 5, 1, 2),
    _CMTSessionRequestStatsRequestTimestamp_Type()
)
cMTSessionRequestStatsRequestTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMTSessionRequestStatsRequestTimestamp.setStatus("current")


class _CMTSessionRequestStatsRequestStatus_Type(Integer32):
    """Custom type cMTSessionRequestStatsRequestStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("completed", 1),
          ("notCompleted", 2))
    )


_CMTSessionRequestStatsRequestStatus_Type.__name__ = "Integer32"
_CMTSessionRequestStatsRequestStatus_Object = MibTableColumn
cMTSessionRequestStatsRequestStatus = _CMTSessionRequestStatsRequestStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 2, 5, 1, 3),
    _CMTSessionRequestStatsRequestStatus_Type()
)
cMTSessionRequestStatsRequestStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMTSessionRequestStatsRequestStatus.setStatus("current")


class _CMTSessionRequestStatsTracerouteStatus_Type(Integer32):
    """Custom type cMTSessionRequestStatsTracerouteStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("completed", 1),
          ("notCompleted", 2))
    )


_CMTSessionRequestStatsTracerouteStatus_Type.__name__ = "Integer32"
_CMTSessionRequestStatsTracerouteStatus_Object = MibTableColumn
cMTSessionRequestStatsTracerouteStatus = _CMTSessionRequestStatsTracerouteStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 2, 5, 1, 4),
    _CMTSessionRequestStatsTracerouteStatus_Type()
)
cMTSessionRequestStatsTracerouteStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMTSessionRequestStatsTracerouteStatus.setStatus("current")
_CMTSessionRequestStatsRouteIndex_Type = Gauge32
_CMTSessionRequestStatsRouteIndex_Object = MibTableColumn
cMTSessionRequestStatsRouteIndex = _CMTSessionRequestStatsRouteIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 2, 5, 1, 5),
    _CMTSessionRequestStatsRouteIndex_Type()
)
cMTSessionRequestStatsRouteIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMTSessionRequestStatsRouteIndex.setStatus("current")
_CMTSessionRequestStatsNumberOfMediatraceHops_Type = Counter32
_CMTSessionRequestStatsNumberOfMediatraceHops_Object = MibTableColumn
cMTSessionRequestStatsNumberOfMediatraceHops = _CMTSessionRequestStatsNumberOfMediatraceHops_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 2, 5, 1, 6),
    _CMTSessionRequestStatsNumberOfMediatraceHops_Type()
)
cMTSessionRequestStatsNumberOfMediatraceHops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMTSessionRequestStatsNumberOfMediatraceHops.setStatus("current")
_CMTSessionRequestStatsNumberOfNonMediatraceHops_Type = Counter32
_CMTSessionRequestStatsNumberOfNonMediatraceHops_Object = MibTableColumn
cMTSessionRequestStatsNumberOfNonMediatraceHops = _CMTSessionRequestStatsNumberOfNonMediatraceHops_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 2, 5, 1, 7),
    _CMTSessionRequestStatsNumberOfNonMediatraceHops_Type()
)
cMTSessionRequestStatsNumberOfNonMediatraceHops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMTSessionRequestStatsNumberOfNonMediatraceHops.setStatus("current")
_CMTSessionRequestStatsNumberOfValidHops_Type = Counter32
_CMTSessionRequestStatsNumberOfValidHops_Object = MibTableColumn
cMTSessionRequestStatsNumberOfValidHops = _CMTSessionRequestStatsNumberOfValidHops_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 2, 5, 1, 8),
    _CMTSessionRequestStatsNumberOfValidHops_Type()
)
cMTSessionRequestStatsNumberOfValidHops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMTSessionRequestStatsNumberOfValidHops.setStatus("current")
_CMTSessionRequestStatsNumberOfErrorHops_Type = Counter32
_CMTSessionRequestStatsNumberOfErrorHops_Object = MibTableColumn
cMTSessionRequestStatsNumberOfErrorHops = _CMTSessionRequestStatsNumberOfErrorHops_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 2, 5, 1, 9),
    _CMTSessionRequestStatsNumberOfErrorHops_Type()
)
cMTSessionRequestStatsNumberOfErrorHops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMTSessionRequestStatsNumberOfErrorHops.setStatus("current")
_CMTSessionRequestStatsNumberOfNoDataRecordHops_Type = Counter32
_CMTSessionRequestStatsNumberOfNoDataRecordHops_Object = MibTableColumn
cMTSessionRequestStatsNumberOfNoDataRecordHops = _CMTSessionRequestStatsNumberOfNoDataRecordHops_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 2, 5, 1, 10),
    _CMTSessionRequestStatsNumberOfNoDataRecordHops_Type()
)
cMTSessionRequestStatsNumberOfNoDataRecordHops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMTSessionRequestStatsNumberOfNoDataRecordHops.setStatus("current")
_CMTSessionRequestStatsMDGlobalId_Type = OctetString
_CMTSessionRequestStatsMDGlobalId_Object = MibTableColumn
cMTSessionRequestStatsMDGlobalId = _CMTSessionRequestStatsMDGlobalId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 2, 5, 1, 11),
    _CMTSessionRequestStatsMDGlobalId_Type()
)
cMTSessionRequestStatsMDGlobalId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMTSessionRequestStatsMDGlobalId.setStatus("current")
_CMTSessionRequestStatsMDMultiPartySessionId_Type = OctetString
_CMTSessionRequestStatsMDMultiPartySessionId_Object = MibTableColumn
cMTSessionRequestStatsMDMultiPartySessionId = _CMTSessionRequestStatsMDMultiPartySessionId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 2, 5, 1, 12),
    _CMTSessionRequestStatsMDMultiPartySessionId_Type()
)
cMTSessionRequestStatsMDMultiPartySessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMTSessionRequestStatsMDMultiPartySessionId.setStatus("current")
_CMTSessionRequestStatsMDAppName_Type = OctetString
_CMTSessionRequestStatsMDAppName_Object = MibTableColumn
cMTSessionRequestStatsMDAppName = _CMTSessionRequestStatsMDAppName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 2, 5, 1, 13),
    _CMTSessionRequestStatsMDAppName_Type()
)
cMTSessionRequestStatsMDAppName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMTSessionRequestStatsMDAppName.setStatus("current")
_CMTCommonMetricStatsTable_Object = MibTable
cMTCommonMetricStatsTable = _CMTCommonMetricStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 2, 6)
)
if mibBuilder.loadTexts:
    cMTCommonMetricStatsTable.setStatus("current")
_CMTCommonMetricStatsEntry_Object = MibTableRow
cMTCommonMetricStatsEntry = _CMTCommonMetricStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 2, 6, 1)
)
cMTCommonMetricStatsEntry.setIndexNames(
    (0, "CISCO-MEDIATRACE-MIB", "cMTSessionNumber"),
    (0, "CISCO-MEDIATRACE-MIB", "cMTSessionLifeNumber"),
    (0, "CISCO-MEDIATRACE-MIB", "cMTBucketNumber"),
    (0, "CISCO-MEDIATRACE-MIB", "cMTHopStatsAddrType"),
    (0, "CISCO-MEDIATRACE-MIB", "cMTHopStatsAddr"),
)
if mibBuilder.loadTexts:
    cMTCommonMetricStatsEntry.setStatus("current")


class _CMTCommonMetricsBitmaps_Type(Bits):
    """Custom type cMTCommonMetricsBitmaps based on Bits"""
    namedValues = NamedValues(
        *(("flowCounterUncollected", 15),
          ("flowCounterUnsupported", 14),
          ("flowDirectionUncollected", 17),
          ("flowDirectionUnsupported", 16),
          ("flowSamplingStartTimeUncollected", 1),
          ("flowSamplingStartTimeUnsupported", 0),
          ("ipByteRateUncollected", 9),
          ("ipByteRateUnsupported", 8),
          ("ipDscpUncollected", 11),
          ("ipDscpUnsupported", 10),
          ("ipOctetsUncollected", 7),
          ("ipOctetsUnsupported", 6),
          ("ipPktCountUncollected", 5),
          ("ipPktCountUnsupported", 4),
          ("ipPktDroppedUncollected", 3),
          ("ipPktDroppedUnsupported", 2),
          ("ipProtocolUncollected", 25),
          ("ipProtocolUnsupported", 24),
          ("ipTtlUncollected", 13),
          ("ipTtlUnsupported", 12),
          ("lossMeasurementUncollected", 19),
          ("lossMeasurementUnsupported", 18),
          ("mediaStopOccurredUncollected", 21),
          ("mediaStopOccurredUnsupported", 20),
          ("routeForwardUncollected", 23),
          ("routeForwardUnsupported", 22))
    )

_CMTCommonMetricsBitmaps_Type.__name__ = "Bits"
_CMTCommonMetricsBitmaps_Object = MibTableColumn
cMTCommonMetricsBitmaps = _CMTCommonMetricsBitmaps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 2, 6, 1, 2),
    _CMTCommonMetricsBitmaps_Type()
)
cMTCommonMetricsBitmaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMTCommonMetricsBitmaps.setStatus("current")
_CMTCommonMetricsFlowSamplingStartTime_Type = CiscoNTPTimeStamp
_CMTCommonMetricsFlowSamplingStartTime_Object = MibTableColumn
cMTCommonMetricsFlowSamplingStartTime = _CMTCommonMetricsFlowSamplingStartTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 2, 6, 1, 3),
    _CMTCommonMetricsFlowSamplingStartTime_Type()
)
cMTCommonMetricsFlowSamplingStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMTCommonMetricsFlowSamplingStartTime.setStatus("current")
_CMTCommonMetricsIpPktDropped_Type = Counter64
_CMTCommonMetricsIpPktDropped_Object = MibTableColumn
cMTCommonMetricsIpPktDropped = _CMTCommonMetricsIpPktDropped_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 2, 6, 1, 4),
    _CMTCommonMetricsIpPktDropped_Type()
)
cMTCommonMetricsIpPktDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMTCommonMetricsIpPktDropped.setStatus("current")
if mibBuilder.loadTexts:
    cMTCommonMetricsIpPktDropped.setUnits("packets")
_CMTCommonMetricsIpOctets_Type = Counter64
_CMTCommonMetricsIpOctets_Object = MibTableColumn
cMTCommonMetricsIpOctets = _CMTCommonMetricsIpOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 2, 6, 1, 5),
    _CMTCommonMetricsIpOctets_Type()
)
cMTCommonMetricsIpOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMTCommonMetricsIpOctets.setStatus("current")
if mibBuilder.loadTexts:
    cMTCommonMetricsIpOctets.setUnits("octets")
_CMTCommonMetricsIpPktCount_Type = Counter64
_CMTCommonMetricsIpPktCount_Object = MibTableColumn
cMTCommonMetricsIpPktCount = _CMTCommonMetricsIpPktCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 2, 6, 1, 6),
    _CMTCommonMetricsIpPktCount_Type()
)
cMTCommonMetricsIpPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMTCommonMetricsIpPktCount.setStatus("current")
if mibBuilder.loadTexts:
    cMTCommonMetricsIpPktCount.setUnits("packets")
_CMTCommonMetricsIpByteRate_Type = Gauge32
_CMTCommonMetricsIpByteRate_Object = MibTableColumn
cMTCommonMetricsIpByteRate = _CMTCommonMetricsIpByteRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 2, 6, 1, 7),
    _CMTCommonMetricsIpByteRate_Type()
)
cMTCommonMetricsIpByteRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMTCommonMetricsIpByteRate.setStatus("current")
if mibBuilder.loadTexts:
    cMTCommonMetricsIpByteRate.setUnits("packets per second")


class _CMTCommonMetricsIpDscp_Type(Unsigned32):
    """Custom type cMTCommonMetricsIpDscp based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_CMTCommonMetricsIpDscp_Type.__name__ = "Unsigned32"
_CMTCommonMetricsIpDscp_Object = MibTableColumn
cMTCommonMetricsIpDscp = _CMTCommonMetricsIpDscp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 2, 6, 1, 8),
    _CMTCommonMetricsIpDscp_Type()
)
cMTCommonMetricsIpDscp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMTCommonMetricsIpDscp.setStatus("current")


class _CMTCommonMetricsIpTtl_Type(Unsigned32):
    """Custom type cMTCommonMetricsIpTtl based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CMTCommonMetricsIpTtl_Type.__name__ = "Unsigned32"
_CMTCommonMetricsIpTtl_Object = MibTableColumn
cMTCommonMetricsIpTtl = _CMTCommonMetricsIpTtl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 2, 6, 1, 9),
    _CMTCommonMetricsIpTtl_Type()
)
cMTCommonMetricsIpTtl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMTCommonMetricsIpTtl.setStatus("current")
_CMTCommonMetricsFlowCounter_Type = Gauge32
_CMTCommonMetricsFlowCounter_Object = MibTableColumn
cMTCommonMetricsFlowCounter = _CMTCommonMetricsFlowCounter_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 2, 6, 1, 10),
    _CMTCommonMetricsFlowCounter_Type()
)
cMTCommonMetricsFlowCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMTCommonMetricsFlowCounter.setStatus("current")


class _CMTCommonMetricsFlowDirection_Type(Integer32):
    """Custom type cMTCommonMetricsFlowDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("egress", 3),
          ("ingress", 2),
          ("unknown", 1))
    )


_CMTCommonMetricsFlowDirection_Type.__name__ = "Integer32"
_CMTCommonMetricsFlowDirection_Object = MibTableColumn
cMTCommonMetricsFlowDirection = _CMTCommonMetricsFlowDirection_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 2, 6, 1, 11),
    _CMTCommonMetricsFlowDirection_Type()
)
cMTCommonMetricsFlowDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMTCommonMetricsFlowDirection.setStatus("current")


class _CMTCommonMetricsLossMeasurement_Type(Integer32):
    """Custom type cMTCommonMetricsLossMeasurement based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_CMTCommonMetricsLossMeasurement_Type.__name__ = "Integer32"
_CMTCommonMetricsLossMeasurement_Object = MibTableColumn
cMTCommonMetricsLossMeasurement = _CMTCommonMetricsLossMeasurement_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 2, 6, 1, 12),
    _CMTCommonMetricsLossMeasurement_Type()
)
cMTCommonMetricsLossMeasurement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMTCommonMetricsLossMeasurement.setStatus("current")


class _CMTCommonMetricsMediaStopOccurred_Type(Integer32):
    """Custom type cMTCommonMetricsMediaStopOccurred based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_CMTCommonMetricsMediaStopOccurred_Type.__name__ = "Integer32"
_CMTCommonMetricsMediaStopOccurred_Object = MibTableColumn
cMTCommonMetricsMediaStopOccurred = _CMTCommonMetricsMediaStopOccurred_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 2, 6, 1, 13),
    _CMTCommonMetricsMediaStopOccurred_Type()
)
cMTCommonMetricsMediaStopOccurred.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMTCommonMetricsMediaStopOccurred.setStatus("current")
_CMTCommonMetricsRouteForward_Type = SnmpAdminString
_CMTCommonMetricsRouteForward_Object = MibTableColumn
cMTCommonMetricsRouteForward = _CMTCommonMetricsRouteForward_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 2, 6, 1, 14),
    _CMTCommonMetricsRouteForward_Type()
)
cMTCommonMetricsRouteForward.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMTCommonMetricsRouteForward.setStatus("current")
_CMTCommonMetricsIpProtocol_Type = CiscoMediatraceSupportProtocol
_CMTCommonMetricsIpProtocol_Object = MibTableColumn
cMTCommonMetricsIpProtocol = _CMTCommonMetricsIpProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 2, 6, 1, 15),
    _CMTCommonMetricsIpProtocol_Type()
)
cMTCommonMetricsIpProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMTCommonMetricsIpProtocol.setStatus("current")
_CMTRtpMetricStatsTable_Object = MibTable
cMTRtpMetricStatsTable = _CMTRtpMetricStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 2, 7)
)
if mibBuilder.loadTexts:
    cMTRtpMetricStatsTable.setStatus("current")
_CMTRtpMetricStatsEntry_Object = MibTableRow
cMTRtpMetricStatsEntry = _CMTRtpMetricStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 2, 7, 1)
)
if mibBuilder.loadTexts:
    cMTRtpMetricStatsEntry.setStatus("current")


class _CMTRtpMetricsBitmaps_Type(Bits):
    """Custom type cMTRtpMetricsBitmaps based on Bits"""
    namedValues = NamedValues(
        *(("bitRateunCollected", 1),
          ("bitRateunSupport", 0),
          ("expectedPktsunCollected", 11),
          ("expectedPktsunSupport", 10),
          ("jitterunCollected", 7),
          ("jitterunSupport", 6),
          ("losspercentUncollected", 15),
          ("losspercentUnsupport", 14),
          ("lostPktEventsunCollected", 13),
          ("lostPktEventsunSupport", 12),
          ("lostPktsunCollected", 9),
          ("lostPktsunSupport", 8),
          ("octetsunCollected", 3),
          ("octetsunSupport", 2),
          ("pktsunCollected", 5),
          ("pktsunSupport", 4))
    )

_CMTRtpMetricsBitmaps_Type.__name__ = "Bits"
_CMTRtpMetricsBitmaps_Object = MibTableColumn
cMTRtpMetricsBitmaps = _CMTRtpMetricsBitmaps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 2, 7, 1, 2),
    _CMTRtpMetricsBitmaps_Type()
)
cMTRtpMetricsBitmaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMTRtpMetricsBitmaps.setStatus("current")
_CMTRtpMetricsBitRate_Type = Gauge32
_CMTRtpMetricsBitRate_Object = MibTableColumn
cMTRtpMetricsBitRate = _CMTRtpMetricsBitRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 2, 7, 1, 3),
    _CMTRtpMetricsBitRate_Type()
)
cMTRtpMetricsBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMTRtpMetricsBitRate.setStatus("current")
_CMTRtpMetricsOctets_Type = Counter64
_CMTRtpMetricsOctets_Object = MibTableColumn
cMTRtpMetricsOctets = _CMTRtpMetricsOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 2, 7, 1, 4),
    _CMTRtpMetricsOctets_Type()
)
cMTRtpMetricsOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMTRtpMetricsOctets.setStatus("current")
_CMTRtpMetricsPkts_Type = Counter64
_CMTRtpMetricsPkts_Object = MibTableColumn
cMTRtpMetricsPkts = _CMTRtpMetricsPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 2, 7, 1, 5),
    _CMTRtpMetricsPkts_Type()
)
cMTRtpMetricsPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMTRtpMetricsPkts.setStatus("current")
if mibBuilder.loadTexts:
    cMTRtpMetricsPkts.setUnits("packets")
_CMTRtpMetricsJitter_Type = FlowMetricValue
_CMTRtpMetricsJitter_Object = MibTableColumn
cMTRtpMetricsJitter = _CMTRtpMetricsJitter_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 2, 7, 1, 6),
    _CMTRtpMetricsJitter_Type()
)
cMTRtpMetricsJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMTRtpMetricsJitter.setStatus("current")
if mibBuilder.loadTexts:
    cMTRtpMetricsJitter.setUnits("seconds")
_CMTRtpMetricsLostPkts_Type = Counter64
_CMTRtpMetricsLostPkts_Object = MibTableColumn
cMTRtpMetricsLostPkts = _CMTRtpMetricsLostPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 2, 7, 1, 7),
    _CMTRtpMetricsLostPkts_Type()
)
cMTRtpMetricsLostPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMTRtpMetricsLostPkts.setStatus("current")
if mibBuilder.loadTexts:
    cMTRtpMetricsLostPkts.setUnits("packets")
_CMTRtpMetricsExpectedPkts_Type = Counter64
_CMTRtpMetricsExpectedPkts_Object = MibTableColumn
cMTRtpMetricsExpectedPkts = _CMTRtpMetricsExpectedPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 2, 7, 1, 8),
    _CMTRtpMetricsExpectedPkts_Type()
)
cMTRtpMetricsExpectedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMTRtpMetricsExpectedPkts.setStatus("current")
if mibBuilder.loadTexts:
    cMTRtpMetricsExpectedPkts.setUnits("packets")
_CMTRtpMetricsLostPktEvents_Type = Counter64
_CMTRtpMetricsLostPktEvents_Object = MibTableColumn
cMTRtpMetricsLostPktEvents = _CMTRtpMetricsLostPktEvents_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 2, 7, 1, 9),
    _CMTRtpMetricsLostPktEvents_Type()
)
cMTRtpMetricsLostPktEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMTRtpMetricsLostPktEvents.setStatus("current")
if mibBuilder.loadTexts:
    cMTRtpMetricsLostPktEvents.setUnits("packets")


class _CMTRtpMetricsLossPercent_Type(Gauge32):
    """Custom type cMTRtpMetricsLossPercent based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CMTRtpMetricsLossPercent_Type.__name__ = "Gauge32"
_CMTRtpMetricsLossPercent_Object = MibTableColumn
cMTRtpMetricsLossPercent = _CMTRtpMetricsLossPercent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 2, 7, 1, 10),
    _CMTRtpMetricsLossPercent_Type()
)
cMTRtpMetricsLossPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMTRtpMetricsLossPercent.setStatus("current")
_CMTTcpMetricStatsTable_Object = MibTable
cMTTcpMetricStatsTable = _CMTTcpMetricStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 2, 8)
)
if mibBuilder.loadTexts:
    cMTTcpMetricStatsTable.setStatus("current")
_CMTTcpMetricStatsEntry_Object = MibTableRow
cMTTcpMetricStatsEntry = _CMTTcpMetricStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 2, 8, 1)
)
if mibBuilder.loadTexts:
    cMTTcpMetricStatsEntry.setStatus("current")


class _CMTTcpMetricBitmaps_Type(Bits):
    """Custom type cMTTcpMetricBitmaps based on Bits"""
    namedValues = NamedValues(
        *(("connectRoundTripDelayUncollected", 3),
          ("connectRoundTripDelayUnsupport", 2),
          ("lostEventCountUncollected", 5),
          ("lostEventCountUnsupport", 4),
          ("mediaByteCountUncollected", 1),
          ("mediaByteCountUnsupport", 0))
    )

_CMTTcpMetricBitmaps_Type.__name__ = "Bits"
_CMTTcpMetricBitmaps_Object = MibTableColumn
cMTTcpMetricBitmaps = _CMTTcpMetricBitmaps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 2, 8, 1, 2),
    _CMTTcpMetricBitmaps_Type()
)
cMTTcpMetricBitmaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMTTcpMetricBitmaps.setStatus("current")
_CMTTcpMetricMediaByteCount_Type = FlowMetricValue
_CMTTcpMetricMediaByteCount_Object = MibTableColumn
cMTTcpMetricMediaByteCount = _CMTTcpMetricMediaByteCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 2, 8, 1, 3),
    _CMTTcpMetricMediaByteCount_Type()
)
cMTTcpMetricMediaByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMTTcpMetricMediaByteCount.setStatus("current")
_CMTTcpMetricConnectRoundTripDelay_Type = Counter64
_CMTTcpMetricConnectRoundTripDelay_Object = MibTableColumn
cMTTcpMetricConnectRoundTripDelay = _CMTTcpMetricConnectRoundTripDelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 2, 8, 1, 4),
    _CMTTcpMetricConnectRoundTripDelay_Type()
)
cMTTcpMetricConnectRoundTripDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMTTcpMetricConnectRoundTripDelay.setStatus("current")
_CMTTcpMetricLostEventCount_Type = Counter64
_CMTTcpMetricLostEventCount_Object = MibTableColumn
cMTTcpMetricLostEventCount = _CMTTcpMetricLostEventCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 2, 8, 1, 5),
    _CMTTcpMetricLostEventCount_Type()
)
cMTTcpMetricLostEventCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMTTcpMetricLostEventCount.setStatus("current")
_CMTSystemMetricStatsTable_Object = MibTable
cMTSystemMetricStatsTable = _CMTSystemMetricStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 2, 9)
)
if mibBuilder.loadTexts:
    cMTSystemMetricStatsTable.setStatus("current")
_CMTSystemMetricStatsEntry_Object = MibTableRow
cMTSystemMetricStatsEntry = _CMTSystemMetricStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 2, 9, 1)
)
cMTSystemMetricStatsEntry.setIndexNames(
    (0, "CISCO-MEDIATRACE-MIB", "cMTSessionNumber"),
    (0, "CISCO-MEDIATRACE-MIB", "cMTSessionLifeNumber"),
    (0, "CISCO-MEDIATRACE-MIB", "cMTBucketNumber"),
    (0, "CISCO-MEDIATRACE-MIB", "cMTHopStatsAddrType"),
    (0, "CISCO-MEDIATRACE-MIB", "cMTHopStatsAddr"),
)
if mibBuilder.loadTexts:
    cMTSystemMetricStatsEntry.setStatus("current")


class _CMTSystemMetricBitmaps_Type(Bits):
    """Custom type cMTSystemMetricBitmaps based on Bits"""
    namedValues = NamedValues(
        *(("cpuFiveMinutesUtilizationUncollected", 3),
          ("cpuFiveMinutesUtilizationUnsupport", 2),
          ("cpuOneMinuteUtilizationUncollected", 1),
          ("cpuOneMinuteUtilizationUnsupport", 0),
          ("memoryMetricsUncollected", 5),
          ("memoryMetricsUnsupport", 4))
    )

_CMTSystemMetricBitmaps_Type.__name__ = "Bits"
_CMTSystemMetricBitmaps_Object = MibTableColumn
cMTSystemMetricBitmaps = _CMTSystemMetricBitmaps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 2, 9, 1, 1),
    _CMTSystemMetricBitmaps_Type()
)
cMTSystemMetricBitmaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMTSystemMetricBitmaps.setStatus("current")


class _CMTSystemMetricCpuOneMinuteUtilization_Type(Gauge32):
    """Custom type cMTSystemMetricCpuOneMinuteUtilization based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CMTSystemMetricCpuOneMinuteUtilization_Type.__name__ = "Gauge32"
_CMTSystemMetricCpuOneMinuteUtilization_Object = MibTableColumn
cMTSystemMetricCpuOneMinuteUtilization = _CMTSystemMetricCpuOneMinuteUtilization_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 2, 9, 1, 2),
    _CMTSystemMetricCpuOneMinuteUtilization_Type()
)
cMTSystemMetricCpuOneMinuteUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMTSystemMetricCpuOneMinuteUtilization.setStatus("current")


class _CMTSystemMetricCpuFiveMinutesUtilization_Type(Gauge32):
    """Custom type cMTSystemMetricCpuFiveMinutesUtilization based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CMTSystemMetricCpuFiveMinutesUtilization_Type.__name__ = "Gauge32"
_CMTSystemMetricCpuFiveMinutesUtilization_Object = MibTableColumn
cMTSystemMetricCpuFiveMinutesUtilization = _CMTSystemMetricCpuFiveMinutesUtilization_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 2, 9, 1, 3),
    _CMTSystemMetricCpuFiveMinutesUtilization_Type()
)
cMTSystemMetricCpuFiveMinutesUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMTSystemMetricCpuFiveMinutesUtilization.setStatus("current")


class _CMTSystemMetricMemoryUtilization_Type(Gauge32):
    """Custom type cMTSystemMetricMemoryUtilization based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CMTSystemMetricMemoryUtilization_Type.__name__ = "Gauge32"
_CMTSystemMetricMemoryUtilization_Object = MibTableColumn
cMTSystemMetricMemoryUtilization = _CMTSystemMetricMemoryUtilization_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 2, 9, 1, 4),
    _CMTSystemMetricMemoryUtilization_Type()
)
cMTSystemMetricMemoryUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMTSystemMetricMemoryUtilization.setStatus("current")
_CMTInterfaceMetricStatsTable_Object = MibTable
cMTInterfaceMetricStatsTable = _CMTInterfaceMetricStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 2, 10)
)
if mibBuilder.loadTexts:
    cMTInterfaceMetricStatsTable.setStatus("current")
_CMTInterfaceMetricStatsEntry_Object = MibTableRow
cMTInterfaceMetricStatsEntry = _CMTInterfaceMetricStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 2, 10, 1)
)
cMTInterfaceMetricStatsEntry.setIndexNames(
    (0, "CISCO-MEDIATRACE-MIB", "cMTSessionNumber"),
    (0, "CISCO-MEDIATRACE-MIB", "cMTSessionLifeNumber"),
    (0, "CISCO-MEDIATRACE-MIB", "cMTBucketNumber"),
    (0, "CISCO-MEDIATRACE-MIB", "cMTHopStatsAddrType"),
    (0, "CISCO-MEDIATRACE-MIB", "cMTHopStatsAddr"),
)
if mibBuilder.loadTexts:
    cMTInterfaceMetricStatsEntry.setStatus("current")


class _CMTInterfaceBitmaps_Type(Bits):
    """Custom type cMTInterfaceBitmaps based on Bits"""
    namedValues = NamedValues(
        *(("inDiscardsUncollected", 7),
          ("inDiscardsUnsupport", 6),
          ("inErrorsUncollected", 11),
          ("inErrorsUnsupport", 10),
          ("inOctetsUncollected", 15),
          ("inOctetsUnsupport", 14),
          ("inSpeedUncollected", 1),
          ("inSpeedUnsupport", 0),
          ("outDiscardsUncollected", 5),
          ("outDiscardsUnsupport", 4),
          ("outErrorsUncollected", 9),
          ("outErrorsUnsupport", 8),
          ("outOctetsUncollected", 13),
          ("outOctetsUnsupport", 12),
          ("outSpeedUncollected", 3),
          ("outSpeedUnsupport", 2))
    )

_CMTInterfaceBitmaps_Type.__name__ = "Bits"
_CMTInterfaceBitmaps_Object = MibTableColumn
cMTInterfaceBitmaps = _CMTInterfaceBitmaps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 2, 10, 1, 2),
    _CMTInterfaceBitmaps_Type()
)
cMTInterfaceBitmaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMTInterfaceBitmaps.setStatus("current")
_CMTInterfaceOutSpeed_Type = Gauge32
_CMTInterfaceOutSpeed_Object = MibTableColumn
cMTInterfaceOutSpeed = _CMTInterfaceOutSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 2, 10, 1, 3),
    _CMTInterfaceOutSpeed_Type()
)
cMTInterfaceOutSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMTInterfaceOutSpeed.setStatus("current")
_CMTInterfaceInSpeed_Type = Gauge32
_CMTInterfaceInSpeed_Object = MibTableColumn
cMTInterfaceInSpeed = _CMTInterfaceInSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 2, 10, 1, 4),
    _CMTInterfaceInSpeed_Type()
)
cMTInterfaceInSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMTInterfaceInSpeed.setStatus("current")
_CMTInterfaceOutDiscards_Type = Counter32
_CMTInterfaceOutDiscards_Object = MibTableColumn
cMTInterfaceOutDiscards = _CMTInterfaceOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 2, 10, 1, 5),
    _CMTInterfaceOutDiscards_Type()
)
cMTInterfaceOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMTInterfaceOutDiscards.setStatus("current")
_CMTInterfaceInDiscards_Type = Counter32
_CMTInterfaceInDiscards_Object = MibTableColumn
cMTInterfaceInDiscards = _CMTInterfaceInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 2, 10, 1, 6),
    _CMTInterfaceInDiscards_Type()
)
cMTInterfaceInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMTInterfaceInDiscards.setStatus("current")
_CMTInterfaceOutErrors_Type = Counter32
_CMTInterfaceOutErrors_Object = MibTableColumn
cMTInterfaceOutErrors = _CMTInterfaceOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 2, 10, 1, 7),
    _CMTInterfaceOutErrors_Type()
)
cMTInterfaceOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMTInterfaceOutErrors.setStatus("current")
_CMTInterfaceInErrors_Type = Counter32
_CMTInterfaceInErrors_Object = MibTableColumn
cMTInterfaceInErrors = _CMTInterfaceInErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 2, 10, 1, 8),
    _CMTInterfaceInErrors_Type()
)
cMTInterfaceInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMTInterfaceInErrors.setStatus("current")
_CMTInterfaceOutOctets_Type = Counter32
_CMTInterfaceOutOctets_Object = MibTableColumn
cMTInterfaceOutOctets = _CMTInterfaceOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 2, 10, 1, 9),
    _CMTInterfaceOutOctets_Type()
)
cMTInterfaceOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMTInterfaceOutOctets.setStatus("current")
_CMTInterfaceInOctets_Type = Counter32
_CMTInterfaceInOctets_Object = MibTableColumn
cMTInterfaceInOctets = _CMTInterfaceInOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 1, 2, 10, 1, 10),
    _CMTInterfaceInOctets_Type()
)
cMTInterfaceInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMTInterfaceInOctets.setStatus("current")
_CiscoMediatraceMIBConform_ObjectIdentity = ObjectIdentity
ciscoMediatraceMIBConform = _CiscoMediatraceMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 2)
)
_CiscoMediatraceMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoMediatraceMIBCompliances = _CiscoMediatraceMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 2, 1)
)
_CiscoMediatraceMIBGroups_ObjectIdentity = ObjectIdentity
ciscoMediatraceMIBGroups = _CiscoMediatraceMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 2, 2)
)
cMTCommonMetricStatsEntry.registerAugmentions(
    ("CISCO-MEDIATRACE-MIB",
     "cMTRtpMetricStatsEntry")
)
cMTRtpMetricStatsEntry.setIndexNames(*cMTCommonMetricStatsEntry.getIndexNames())
cMTCommonMetricStatsEntry.registerAugmentions(
    ("CISCO-MEDIATRACE-MIB",
     "cMTTcpMetricStatsEntry")
)
cMTTcpMetricStatsEntry.setIndexNames(*cMTCommonMetricStatsEntry.getIndexNames())

# Managed Objects groups

ciscoMediatraceMIBMainObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 2, 2, 1)
)
ciscoMediatraceMIBMainObjectGroup.setObjects(
      *(("CISCO-MEDIATRACE-MIB", "cMTFlowSpecifierRowStatus"),
        ("CISCO-MEDIATRACE-MIB", "cMTFlowSpecifierDestAddrType"),
        ("CISCO-MEDIATRACE-MIB", "cMTFlowSpecifierDestAddr"),
        ("CISCO-MEDIATRACE-MIB", "cMTFlowSpecifierDestPort"),
        ("CISCO-MEDIATRACE-MIB", "cMTFlowSpecifierSourceAddrType"),
        ("CISCO-MEDIATRACE-MIB", "cMTFlowSpecifierSourceAddr"),
        ("CISCO-MEDIATRACE-MIB", "cMTFlowSpecifierSourcePort"),
        ("CISCO-MEDIATRACE-MIB", "cMTFlowSpecifierIpProtocol"),
        ("CISCO-MEDIATRACE-MIB", "cMTPathSpecifierRowStatus"),
        ("CISCO-MEDIATRACE-MIB", "cMTPathSpecifierDestAddrType"),
        ("CISCO-MEDIATRACE-MIB", "cMTPathSpecifierDestAddr"),
        ("CISCO-MEDIATRACE-MIB", "cMTPathSpecifierDestPort"),
        ("CISCO-MEDIATRACE-MIB", "cMTPathSpecifierSourceAddrType"),
        ("CISCO-MEDIATRACE-MIB", "cMTPathSpecifierSourceAddr"),
        ("CISCO-MEDIATRACE-MIB", "cMTPathSpecifierSourcePort"),
        ("CISCO-MEDIATRACE-MIB", "cMTPathSpecifierProtocolForDiscovery"),
        ("CISCO-MEDIATRACE-MIB", "cMTPathSpecifierGatewayAddrType"),
        ("CISCO-MEDIATRACE-MIB", "cMTPathSpecifierGatewayAddr"),
        ("CISCO-MEDIATRACE-MIB", "cMTPathSpecifierGatewayVlanId"),
        ("CISCO-MEDIATRACE-MIB", "cMTPathSpecifierIpProtocol"),
        ("CISCO-MEDIATRACE-MIB", "cMTSessionParamsResponseTimeout"),
        ("CISCO-MEDIATRACE-MIB", "cMTSessionParamsFrequency"),
        ("CISCO-MEDIATRACE-MIB", "cMTSessionParamsHistoryBuckets"),
        ("CISCO-MEDIATRACE-MIB", "cMTSessionParamsInactivityTimeout"),
        ("CISCO-MEDIATRACE-MIB", "cMTSessionParamsRouteChangeReactiontime"),
        ("CISCO-MEDIATRACE-MIB", "cMTSessionParamsRowStatus"),
        ("CISCO-MEDIATRACE-MIB", "cMTSessionPathSpecifierName"),
        ("CISCO-MEDIATRACE-MIB", "cMTMediaMonitorProfileRtpMaxDropout"),
        ("CISCO-MEDIATRACE-MIB", "cMTMediaMonitorProfileRtpMaxReorder"),
        ("CISCO-MEDIATRACE-MIB", "cMTMediaMonitorProfileRtpMinimalSequential"),
        ("CISCO-MEDIATRACE-MIB", "cMTMediaMonitorProfileInterval"),
        ("CISCO-MEDIATRACE-MIB", "cMTMediaMonitorProfileRowStatus"),
        ("CISCO-MEDIATRACE-MIB", "cMTSessionFlowSpecifierName"),
        ("CISCO-MEDIATRACE-MIB", "cMTSessionParamName"),
        ("CISCO-MEDIATRACE-MIB", "cMTSessionProfileName"),
        ("CISCO-MEDIATRACE-MIB", "cMTSessionRequestStatsRouteIndex"),
        ("CISCO-MEDIATRACE-MIB", "cMTSessionRequestStatsTracerouteStatus"),
        ("CISCO-MEDIATRACE-MIB", "cMTSessionRowStatus"),
        ("CISCO-MEDIATRACE-MIB", "cMTScheduleLife"),
        ("CISCO-MEDIATRACE-MIB", "cMTScheduleStartTime"),
        ("CISCO-MEDIATRACE-MIB", "cMTScheduleEntryAgeout"),
        ("CISCO-MEDIATRACE-MIB", "cMTScheduleRowStatus"),
        ("CISCO-MEDIATRACE-MIB", "cMTSystemProfileMetric"),
        ("CISCO-MEDIATRACE-MIB", "cMTSystemProfileRowStatus"),
        ("CISCO-MEDIATRACE-MIB", "cMTHopStatsMediatraceTtl"),
        ("CISCO-MEDIATRACE-MIB", "cMTHopStatsName"),
        ("CISCO-MEDIATRACE-MIB", "cMTHopStatsCollectionStatus"),
        ("CISCO-MEDIATRACE-MIB", "cMTHopStatsIngressInterface"),
        ("CISCO-MEDIATRACE-MIB", "cMTHopStatsEgressInterface"),
        ("CISCO-MEDIATRACE-MIB", "cMTPathHopType"),
        ("CISCO-MEDIATRACE-MIB", "cMTPathHopAddrType"),
        ("CISCO-MEDIATRACE-MIB", "cMTPathHopAddr"),
        ("CISCO-MEDIATRACE-MIB", "cMTPathHopAlternate1AddrType"),
        ("CISCO-MEDIATRACE-MIB", "cMTPathHopAlternate1Addr"),
        ("CISCO-MEDIATRACE-MIB", "cMTPathHopAlternate2AddrType"),
        ("CISCO-MEDIATRACE-MIB", "cMTPathHopAlternate2Addr"),
        ("CISCO-MEDIATRACE-MIB", "cMTPathHopAlternate3AddrType"),
        ("CISCO-MEDIATRACE-MIB", "cMTPathHopAlternate3Addr"),
        ("CISCO-MEDIATRACE-MIB", "cMTTraceRouteHopNumber"),
        ("CISCO-MEDIATRACE-MIB", "cMTTraceRouteHopRtt"),
        ("CISCO-MEDIATRACE-MIB", "cMTSessionRequestStatsRequestTimestamp"),
        ("CISCO-MEDIATRACE-MIB", "cMTSessionRequestStatsRequestStatus"),
        ("CISCO-MEDIATRACE-MIB", "cMTSessionRequestStatsNumberOfMediatraceHops"),
        ("CISCO-MEDIATRACE-MIB", "cMTSessionRequestStatsNumberOfValidHops"),
        ("CISCO-MEDIATRACE-MIB", "cMTSessionRequestStatsNumberOfErrorHops"),
        ("CISCO-MEDIATRACE-MIB", "cMTSessionRequestStatsNumberOfNoDataRecordHops"),
        ("CISCO-MEDIATRACE-MIB", "cMTSessionRequestStatsNumberOfNonMediatraceHops"),
        ("CISCO-MEDIATRACE-MIB", "cMTCommonMetricsIpPktDropped"),
        ("CISCO-MEDIATRACE-MIB", "cMTCommonMetricsIpOctets"),
        ("CISCO-MEDIATRACE-MIB", "cMTCommonMetricsIpPktCount"),
        ("CISCO-MEDIATRACE-MIB", "cMTCommonMetricsIpByteRate"),
        ("CISCO-MEDIATRACE-MIB", "cMTCommonMetricsIpDscp"),
        ("CISCO-MEDIATRACE-MIB", "cMTCommonMetricsIpTtl"),
        ("CISCO-MEDIATRACE-MIB", "cMTCommonMetricsFlowCounter"),
        ("CISCO-MEDIATRACE-MIB", "cMTCommonMetricsFlowDirection"),
        ("CISCO-MEDIATRACE-MIB", "cMTCommonMetricsLossMeasurement"),
        ("CISCO-MEDIATRACE-MIB", "cMTCommonMetricsMediaStopOccurred"),
        ("CISCO-MEDIATRACE-MIB", "cMTCommonMetricsRouteForward"),
        ("CISCO-MEDIATRACE-MIB", "cMTCommonMetricsIpProtocol"),
        ("CISCO-MEDIATRACE-MIB", "cMTRtpMetricsBitRate"),
        ("CISCO-MEDIATRACE-MIB", "cMTRtpMetricsOctets"),
        ("CISCO-MEDIATRACE-MIB", "cMTRtpMetricsPkts"),
        ("CISCO-MEDIATRACE-MIB", "cMTRtpMetricsJitter"),
        ("CISCO-MEDIATRACE-MIB", "cMTRtpMetricsLostPkts"),
        ("CISCO-MEDIATRACE-MIB", "cMTRtpMetricsExpectedPkts"),
        ("CISCO-MEDIATRACE-MIB", "cMTRtpMetricsLostPktEvents"),
        ("CISCO-MEDIATRACE-MIB", "cMTRtpMetricsLossPercent"),
        ("CISCO-MEDIATRACE-MIB", "cMTTcpMetricMediaByteCount"),
        ("CISCO-MEDIATRACE-MIB", "cMTTcpMetricConnectRoundTripDelay"),
        ("CISCO-MEDIATRACE-MIB", "cMTTcpMetricLostEventCount"),
        ("CISCO-MEDIATRACE-MIB", "cMTSystemMetricCpuOneMinuteUtilization"),
        ("CISCO-MEDIATRACE-MIB", "cMTSystemMetricCpuFiveMinutesUtilization"),
        ("CISCO-MEDIATRACE-MIB", "cMTSystemMetricMemoryUtilization"),
        ("CISCO-MEDIATRACE-MIB", "cMTInterfaceOutSpeed"),
        ("CISCO-MEDIATRACE-MIB", "cMTInterfaceInSpeed"),
        ("CISCO-MEDIATRACE-MIB", "cMTInterfaceOutDiscards"),
        ("CISCO-MEDIATRACE-MIB", "cMTInterfaceInDiscards"),
        ("CISCO-MEDIATRACE-MIB", "cMTInterfaceOutErrors"),
        ("CISCO-MEDIATRACE-MIB", "cMTInterfaceInErrors"),
        ("CISCO-MEDIATRACE-MIB", "cMTInterfaceOutOctets"),
        ("CISCO-MEDIATRACE-MIB", "cMTInterfaceInOctets"),
        ("CISCO-MEDIATRACE-MIB", "cMTMediaMonitorProfileMetric"),
        ("CISCO-MEDIATRACE-MIB", "cMTSessionTraceRouteEnabled"),
        ("CISCO-MEDIATRACE-MIB", "cMTScheduleRecurring"),
        ("CISCO-MEDIATRACE-MIB", "cMTFlowSpecifierMetadataGlobalId"),
        ("CISCO-MEDIATRACE-MIB", "cMTPathSpecifierMetadataGlobalId"),
        ("CISCO-MEDIATRACE-MIB", "cMTHopStatsMaskBitmaps"),
        ("CISCO-MEDIATRACE-MIB", "cMTSessionStatusBitmaps"),
        ("CISCO-MEDIATRACE-MIB", "cMTCommonMetricsBitmaps"),
        ("CISCO-MEDIATRACE-MIB", "cMTRtpMetricsBitmaps"),
        ("CISCO-MEDIATRACE-MIB", "cMTTcpMetricBitmaps"),
        ("CISCO-MEDIATRACE-MIB", "cMTSystemMetricBitmaps"),
        ("CISCO-MEDIATRACE-MIB", "cMTInterfaceBitmaps"),
        ("CISCO-MEDIATRACE-MIB", "cMTSessionStatusOperationState"),
        ("CISCO-MEDIATRACE-MIB", "cMTSessionStatusOperationTimeToLive"),
        ("CISCO-MEDIATRACE-MIB", "cMTSessionStatusGlobalSessionId"),
        ("CISCO-MEDIATRACE-MIB", "cMTSessionRequestStatsBitmaps"),
        ("CISCO-MEDIATRACE-MIB", "cMTSessionRequestStatsMDGlobalId"),
        ("CISCO-MEDIATRACE-MIB", "cMTSessionRequestStatsMDMultiPartySessionId"),
        ("CISCO-MEDIATRACE-MIB", "cMTSessionRequestStatsMDAppName"),
        ("CISCO-MEDIATRACE-MIB", "cMTInitiatorEnable"),
        ("CISCO-MEDIATRACE-MIB", "cMTInitiatorSourceInterface"),
        ("CISCO-MEDIATRACE-MIB", "cMTInitiatorSourceAddressType"),
        ("CISCO-MEDIATRACE-MIB", "cMTInitiatorSourceAddress"),
        ("CISCO-MEDIATRACE-MIB", "cMTInitiatorMaxSessions"),
        ("CISCO-MEDIATRACE-MIB", "cMTInitiatorSoftwareVersionMajor"),
        ("CISCO-MEDIATRACE-MIB", "cMTInitiatorProtocolVersionMajor"),
        ("CISCO-MEDIATRACE-MIB", "cMTInitiatorConfiguredSessions"),
        ("CISCO-MEDIATRACE-MIB", "cMTInitiatorPendingSessions"),
        ("CISCO-MEDIATRACE-MIB", "cMTInitiatorInactiveSessions"),
        ("CISCO-MEDIATRACE-MIB", "cMTInitiatorActiveSessions"),
        ("CISCO-MEDIATRACE-MIB", "cMTResponderEnable"),
        ("CISCO-MEDIATRACE-MIB", "cMTResponderMaxSessions"),
        ("CISCO-MEDIATRACE-MIB", "cMTResponderActiveSessions"),
        ("CISCO-MEDIATRACE-MIB", "cMTInitiatorSoftwareVersionMinor"),
        ("CISCO-MEDIATRACE-MIB", "cMTInitiatorProtocolVersionMinor"),
        ("CISCO-MEDIATRACE-MIB", "cMTCommonMetricsFlowSamplingStartTime"))
)
if mibBuilder.loadTexts:
    ciscoMediatraceMIBMainObjectGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoMediatraceMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 800, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoMediatraceMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-MEDIATRACE-MIB",
    **{"CiscoNTPTimeStamp": CiscoNTPTimeStamp,
       "CiscoMediatraceSupportProtocol": CiscoMediatraceSupportProtocol,
       "CiscoMediatraceDiscoveryProtocol": CiscoMediatraceDiscoveryProtocol,
       "ciscoMediatraceMIB": ciscoMediatraceMIB,
       "ciscoMediatraceMIBNotifs": ciscoMediatraceMIBNotifs,
       "ciscoMediatraceMIBObjects": ciscoMediatraceMIBObjects,
       "cMTCtrl": cMTCtrl,
       "cMTInitiatorEnable": cMTInitiatorEnable,
       "cMTInitiatorSourceInterface": cMTInitiatorSourceInterface,
       "cMTInitiatorSourceAddressType": cMTInitiatorSourceAddressType,
       "cMTInitiatorSourceAddress": cMTInitiatorSourceAddress,
       "cMTInitiatorMaxSessions": cMTInitiatorMaxSessions,
       "cMTInitiatorSoftwareVersionMajor": cMTInitiatorSoftwareVersionMajor,
       "cMTInitiatorSoftwareVersionMinor": cMTInitiatorSoftwareVersionMinor,
       "cMTInitiatorProtocolVersionMajor": cMTInitiatorProtocolVersionMajor,
       "cMTInitiatorProtocolVersionMinor": cMTInitiatorProtocolVersionMinor,
       "cMTInitiatorConfiguredSessions": cMTInitiatorConfiguredSessions,
       "cMTInitiatorPendingSessions": cMTInitiatorPendingSessions,
       "cMTInitiatorInactiveSessions": cMTInitiatorInactiveSessions,
       "cMTInitiatorActiveSessions": cMTInitiatorActiveSessions,
       "cMTResponderEnable": cMTResponderEnable,
       "cMTResponderMaxSessions": cMTResponderMaxSessions,
       "cMTResponderActiveSessions": cMTResponderActiveSessions,
       "cMTFlowSpecifierTable": cMTFlowSpecifierTable,
       "cMTFlowSpecifierEntry": cMTFlowSpecifierEntry,
       "cMTFlowSpecifierName": cMTFlowSpecifierName,
       "cMTFlowSpecifierRowStatus": cMTFlowSpecifierRowStatus,
       "cMTFlowSpecifierMetadataGlobalId": cMTFlowSpecifierMetadataGlobalId,
       "cMTFlowSpecifierDestAddrType": cMTFlowSpecifierDestAddrType,
       "cMTFlowSpecifierDestAddr": cMTFlowSpecifierDestAddr,
       "cMTFlowSpecifierDestPort": cMTFlowSpecifierDestPort,
       "cMTFlowSpecifierSourceAddrType": cMTFlowSpecifierSourceAddrType,
       "cMTFlowSpecifierSourceAddr": cMTFlowSpecifierSourceAddr,
       "cMTFlowSpecifierSourcePort": cMTFlowSpecifierSourcePort,
       "cMTFlowSpecifierIpProtocol": cMTFlowSpecifierIpProtocol,
       "cMTPathSpecifierTable": cMTPathSpecifierTable,
       "cMTPathSpecifierEntry": cMTPathSpecifierEntry,
       "cMTPathSpecifierName": cMTPathSpecifierName,
       "cMTPathSpecifierRowStatus": cMTPathSpecifierRowStatus,
       "cMTPathSpecifierMetadataGlobalId": cMTPathSpecifierMetadataGlobalId,
       "cMTPathSpecifierDestAddrType": cMTPathSpecifierDestAddrType,
       "cMTPathSpecifierDestAddr": cMTPathSpecifierDestAddr,
       "cMTPathSpecifierDestPort": cMTPathSpecifierDestPort,
       "cMTPathSpecifierSourceAddrType": cMTPathSpecifierSourceAddrType,
       "cMTPathSpecifierSourceAddr": cMTPathSpecifierSourceAddr,
       "cMTPathSpecifierSourcePort": cMTPathSpecifierSourcePort,
       "cMTPathSpecifierProtocolForDiscovery": cMTPathSpecifierProtocolForDiscovery,
       "cMTPathSpecifierGatewayAddrType": cMTPathSpecifierGatewayAddrType,
       "cMTPathSpecifierGatewayAddr": cMTPathSpecifierGatewayAddr,
       "cMTPathSpecifierGatewayVlanId": cMTPathSpecifierGatewayVlanId,
       "cMTPathSpecifierIpProtocol": cMTPathSpecifierIpProtocol,
       "cMTSessionParamsTable": cMTSessionParamsTable,
       "cMTSessionParamsEntry": cMTSessionParamsEntry,
       "cMTSessionParamsName": cMTSessionParamsName,
       "cMTSessionParamsRowStatus": cMTSessionParamsRowStatus,
       "cMTSessionParamsResponseTimeout": cMTSessionParamsResponseTimeout,
       "cMTSessionParamsFrequency": cMTSessionParamsFrequency,
       "cMTSessionParamsInactivityTimeout": cMTSessionParamsInactivityTimeout,
       "cMTSessionParamsHistoryBuckets": cMTSessionParamsHistoryBuckets,
       "cMTSessionParamsRouteChangeReactiontime": cMTSessionParamsRouteChangeReactiontime,
       "cMTMediaMonitorProfileTable": cMTMediaMonitorProfileTable,
       "cMTMediaMonitorProfileEntry": cMTMediaMonitorProfileEntry,
       "cMTMediaMonitorProfileName": cMTMediaMonitorProfileName,
       "cMTMediaMonitorProfileRowStatus": cMTMediaMonitorProfileRowStatus,
       "cMTMediaMonitorProfileMetric": cMTMediaMonitorProfileMetric,
       "cMTMediaMonitorProfileInterval": cMTMediaMonitorProfileInterval,
       "cMTMediaMonitorProfileRtpMaxDropout": cMTMediaMonitorProfileRtpMaxDropout,
       "cMTMediaMonitorProfileRtpMaxReorder": cMTMediaMonitorProfileRtpMaxReorder,
       "cMTMediaMonitorProfileRtpMinimalSequential": cMTMediaMonitorProfileRtpMinimalSequential,
       "cMTSystemProfileTable": cMTSystemProfileTable,
       "cMTSystemProfileEntry": cMTSystemProfileEntry,
       "cMTSystemProfileName": cMTSystemProfileName,
       "cMTSystemProfileRowStatus": cMTSystemProfileRowStatus,
       "cMTSystemProfileMetric": cMTSystemProfileMetric,
       "cMTSessionTable": cMTSessionTable,
       "cMTSessionEntry": cMTSessionEntry,
       "cMTSessionNumber": cMTSessionNumber,
       "cMTSessionRowStatus": cMTSessionRowStatus,
       "cMTSessionPathSpecifierName": cMTSessionPathSpecifierName,
       "cMTSessionParamName": cMTSessionParamName,
       "cMTSessionProfileName": cMTSessionProfileName,
       "cMTSessionFlowSpecifierName": cMTSessionFlowSpecifierName,
       "cMTSessionTraceRouteEnabled": cMTSessionTraceRouteEnabled,
       "cMTScheduleTable": cMTScheduleTable,
       "cMTScheduleEntry": cMTScheduleEntry,
       "cMTScheduleRowStatus": cMTScheduleRowStatus,
       "cMTScheduleStartTime": cMTScheduleStartTime,
       "cMTScheduleLife": cMTScheduleLife,
       "cMTScheduleEntryAgeout": cMTScheduleEntryAgeout,
       "cMTScheduleRecurring": cMTScheduleRecurring,
       "cMTStats": cMTStats,
       "cMTPathTable": cMTPathTable,
       "cMTPathEntry": cMTPathEntry,
       "cMTSessionLifeNumber": cMTSessionLifeNumber,
       "cMTBucketNumber": cMTBucketNumber,
       "cMTPathHopNumber": cMTPathHopNumber,
       "cMTPathHopAddrType": cMTPathHopAddrType,
       "cMTPathHopAddr": cMTPathHopAddr,
       "cMTPathHopType": cMTPathHopType,
       "cMTPathHopAlternate1AddrType": cMTPathHopAlternate1AddrType,
       "cMTPathHopAlternate1Addr": cMTPathHopAlternate1Addr,
       "cMTPathHopAlternate2AddrType": cMTPathHopAlternate2AddrType,
       "cMTPathHopAlternate2Addr": cMTPathHopAlternate2Addr,
       "cMTPathHopAlternate3AddrType": cMTPathHopAlternate3AddrType,
       "cMTPathHopAlternate3Addr": cMTPathHopAlternate3Addr,
       "cMTHopStatsTable": cMTHopStatsTable,
       "cMTHopStatsEntry": cMTHopStatsEntry,
       "cMTHopStatsMaskBitmaps": cMTHopStatsMaskBitmaps,
       "cMTHopStatsAddrType": cMTHopStatsAddrType,
       "cMTHopStatsAddr": cMTHopStatsAddr,
       "cMTHopStatsName": cMTHopStatsName,
       "cMTHopStatsMediatraceTtl": cMTHopStatsMediatraceTtl,
       "cMTHopStatsCollectionStatus": cMTHopStatsCollectionStatus,
       "cMTHopStatsIngressInterface": cMTHopStatsIngressInterface,
       "cMTHopStatsEgressInterface": cMTHopStatsEgressInterface,
       "cMTTraceRouteTable": cMTTraceRouteTable,
       "cMTTraceRouteEntry": cMTTraceRouteEntry,
       "cMTTraceRouteHopNumber": cMTTraceRouteHopNumber,
       "cMTTraceRouteHopRtt": cMTTraceRouteHopRtt,
       "cMTSessionStatusTable": cMTSessionStatusTable,
       "cMTSessionStatusEntry": cMTSessionStatusEntry,
       "cMTSessionStatusBitmaps": cMTSessionStatusBitmaps,
       "cMTSessionStatusGlobalSessionId": cMTSessionStatusGlobalSessionId,
       "cMTSessionStatusOperationState": cMTSessionStatusOperationState,
       "cMTSessionStatusOperationTimeToLive": cMTSessionStatusOperationTimeToLive,
       "cMTSessionRequestStatsTable": cMTSessionRequestStatsTable,
       "cMTSessionRequestStatsEntry": cMTSessionRequestStatsEntry,
       "cMTSessionRequestStatsBitmaps": cMTSessionRequestStatsBitmaps,
       "cMTSessionRequestStatsRequestTimestamp": cMTSessionRequestStatsRequestTimestamp,
       "cMTSessionRequestStatsRequestStatus": cMTSessionRequestStatsRequestStatus,
       "cMTSessionRequestStatsTracerouteStatus": cMTSessionRequestStatsTracerouteStatus,
       "cMTSessionRequestStatsRouteIndex": cMTSessionRequestStatsRouteIndex,
       "cMTSessionRequestStatsNumberOfMediatraceHops": cMTSessionRequestStatsNumberOfMediatraceHops,
       "cMTSessionRequestStatsNumberOfNonMediatraceHops": cMTSessionRequestStatsNumberOfNonMediatraceHops,
       "cMTSessionRequestStatsNumberOfValidHops": cMTSessionRequestStatsNumberOfValidHops,
       "cMTSessionRequestStatsNumberOfErrorHops": cMTSessionRequestStatsNumberOfErrorHops,
       "cMTSessionRequestStatsNumberOfNoDataRecordHops": cMTSessionRequestStatsNumberOfNoDataRecordHops,
       "cMTSessionRequestStatsMDGlobalId": cMTSessionRequestStatsMDGlobalId,
       "cMTSessionRequestStatsMDMultiPartySessionId": cMTSessionRequestStatsMDMultiPartySessionId,
       "cMTSessionRequestStatsMDAppName": cMTSessionRequestStatsMDAppName,
       "cMTCommonMetricStatsTable": cMTCommonMetricStatsTable,
       "cMTCommonMetricStatsEntry": cMTCommonMetricStatsEntry,
       "cMTCommonMetricsBitmaps": cMTCommonMetricsBitmaps,
       "cMTCommonMetricsFlowSamplingStartTime": cMTCommonMetricsFlowSamplingStartTime,
       "cMTCommonMetricsIpPktDropped": cMTCommonMetricsIpPktDropped,
       "cMTCommonMetricsIpOctets": cMTCommonMetricsIpOctets,
       "cMTCommonMetricsIpPktCount": cMTCommonMetricsIpPktCount,
       "cMTCommonMetricsIpByteRate": cMTCommonMetricsIpByteRate,
       "cMTCommonMetricsIpDscp": cMTCommonMetricsIpDscp,
       "cMTCommonMetricsIpTtl": cMTCommonMetricsIpTtl,
       "cMTCommonMetricsFlowCounter": cMTCommonMetricsFlowCounter,
       "cMTCommonMetricsFlowDirection": cMTCommonMetricsFlowDirection,
       "cMTCommonMetricsLossMeasurement": cMTCommonMetricsLossMeasurement,
       "cMTCommonMetricsMediaStopOccurred": cMTCommonMetricsMediaStopOccurred,
       "cMTCommonMetricsRouteForward": cMTCommonMetricsRouteForward,
       "cMTCommonMetricsIpProtocol": cMTCommonMetricsIpProtocol,
       "cMTRtpMetricStatsTable": cMTRtpMetricStatsTable,
       "cMTRtpMetricStatsEntry": cMTRtpMetricStatsEntry,
       "cMTRtpMetricsBitmaps": cMTRtpMetricsBitmaps,
       "cMTRtpMetricsBitRate": cMTRtpMetricsBitRate,
       "cMTRtpMetricsOctets": cMTRtpMetricsOctets,
       "cMTRtpMetricsPkts": cMTRtpMetricsPkts,
       "cMTRtpMetricsJitter": cMTRtpMetricsJitter,
       "cMTRtpMetricsLostPkts": cMTRtpMetricsLostPkts,
       "cMTRtpMetricsExpectedPkts": cMTRtpMetricsExpectedPkts,
       "cMTRtpMetricsLostPktEvents": cMTRtpMetricsLostPktEvents,
       "cMTRtpMetricsLossPercent": cMTRtpMetricsLossPercent,
       "cMTTcpMetricStatsTable": cMTTcpMetricStatsTable,
       "cMTTcpMetricStatsEntry": cMTTcpMetricStatsEntry,
       "cMTTcpMetricBitmaps": cMTTcpMetricBitmaps,
       "cMTTcpMetricMediaByteCount": cMTTcpMetricMediaByteCount,
       "cMTTcpMetricConnectRoundTripDelay": cMTTcpMetricConnectRoundTripDelay,
       "cMTTcpMetricLostEventCount": cMTTcpMetricLostEventCount,
       "cMTSystemMetricStatsTable": cMTSystemMetricStatsTable,
       "cMTSystemMetricStatsEntry": cMTSystemMetricStatsEntry,
       "cMTSystemMetricBitmaps": cMTSystemMetricBitmaps,
       "cMTSystemMetricCpuOneMinuteUtilization": cMTSystemMetricCpuOneMinuteUtilization,
       "cMTSystemMetricCpuFiveMinutesUtilization": cMTSystemMetricCpuFiveMinutesUtilization,
       "cMTSystemMetricMemoryUtilization": cMTSystemMetricMemoryUtilization,
       "cMTInterfaceMetricStatsTable": cMTInterfaceMetricStatsTable,
       "cMTInterfaceMetricStatsEntry": cMTInterfaceMetricStatsEntry,
       "cMTInterfaceBitmaps": cMTInterfaceBitmaps,
       "cMTInterfaceOutSpeed": cMTInterfaceOutSpeed,
       "cMTInterfaceInSpeed": cMTInterfaceInSpeed,
       "cMTInterfaceOutDiscards": cMTInterfaceOutDiscards,
       "cMTInterfaceInDiscards": cMTInterfaceInDiscards,
       "cMTInterfaceOutErrors": cMTInterfaceOutErrors,
       "cMTInterfaceInErrors": cMTInterfaceInErrors,
       "cMTInterfaceOutOctets": cMTInterfaceOutOctets,
       "cMTInterfaceInOctets": cMTInterfaceInOctets,
       "ciscoMediatraceMIBConform": ciscoMediatraceMIBConform,
       "ciscoMediatraceMIBCompliances": ciscoMediatraceMIBCompliances,
       "ciscoMediatraceMIBCompliance": ciscoMediatraceMIBCompliance,
       "ciscoMediatraceMIBGroups": ciscoMediatraceMIBGroups,
       "ciscoMediatraceMIBMainObjectGroup": ciscoMediatraceMIBMainObjectGroup}
)
