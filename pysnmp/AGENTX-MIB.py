# SNMP MIB module (AGENTX-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/AGENTX-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:34:55 2024
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
 TDomain,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TDomain",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

agentxMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 74)
)
agentxMIB.setRevisions(
        ("2000-01-10 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class AgentxTAddress(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



# MIB Managed Objects in the order of their OIDs

_AgentxObjects_ObjectIdentity = ObjectIdentity
agentxObjects = _AgentxObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 74, 1)
)
_AgentxGeneral_ObjectIdentity = ObjectIdentity
agentxGeneral = _AgentxGeneral_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 74, 1, 1)
)


class _AgentxDefaultTimeout_Type(Integer32):
    """Custom type agentxDefaultTimeout based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AgentxDefaultTimeout_Type.__name__ = "Integer32"
_AgentxDefaultTimeout_Object = MibScalar
agentxDefaultTimeout = _AgentxDefaultTimeout_Object(
    (1, 3, 6, 1, 2, 1, 74, 1, 1, 1),
    _AgentxDefaultTimeout_Type()
)
agentxDefaultTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentxDefaultTimeout.setStatus("current")
if mibBuilder.loadTexts:
    agentxDefaultTimeout.setUnits("seconds")


class _AgentxMasterAgentXVer_Type(Integer32):
    """Custom type agentxMasterAgentXVer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AgentxMasterAgentXVer_Type.__name__ = "Integer32"
_AgentxMasterAgentXVer_Object = MibScalar
agentxMasterAgentXVer = _AgentxMasterAgentXVer_Object(
    (1, 3, 6, 1, 2, 1, 74, 1, 1, 2),
    _AgentxMasterAgentXVer_Type()
)
agentxMasterAgentXVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentxMasterAgentXVer.setStatus("current")
_AgentxConnection_ObjectIdentity = ObjectIdentity
agentxConnection = _AgentxConnection_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 74, 1, 2)
)
_AgentxConnTableLastChange_Type = TimeStamp
_AgentxConnTableLastChange_Object = MibScalar
agentxConnTableLastChange = _AgentxConnTableLastChange_Object(
    (1, 3, 6, 1, 2, 1, 74, 1, 2, 1),
    _AgentxConnTableLastChange_Type()
)
agentxConnTableLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentxConnTableLastChange.setStatus("current")
_AgentxConnectionTable_Object = MibTable
agentxConnectionTable = _AgentxConnectionTable_Object(
    (1, 3, 6, 1, 2, 1, 74, 1, 2, 2)
)
if mibBuilder.loadTexts:
    agentxConnectionTable.setStatus("current")
_AgentxConnectionEntry_Object = MibTableRow
agentxConnectionEntry = _AgentxConnectionEntry_Object(
    (1, 3, 6, 1, 2, 1, 74, 1, 2, 2, 1)
)
agentxConnectionEntry.setIndexNames(
    (0, "AGENTX-MIB", "agentxConnIndex"),
)
if mibBuilder.loadTexts:
    agentxConnectionEntry.setStatus("current")


class _AgentxConnIndex_Type(Unsigned32):
    """Custom type agentxConnIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_AgentxConnIndex_Type.__name__ = "Unsigned32"
_AgentxConnIndex_Object = MibTableColumn
agentxConnIndex = _AgentxConnIndex_Object(
    (1, 3, 6, 1, 2, 1, 74, 1, 2, 2, 1, 1),
    _AgentxConnIndex_Type()
)
agentxConnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentxConnIndex.setStatus("current")
_AgentxConnOpenTime_Type = TimeStamp
_AgentxConnOpenTime_Object = MibTableColumn
agentxConnOpenTime = _AgentxConnOpenTime_Object(
    (1, 3, 6, 1, 2, 1, 74, 1, 2, 2, 1, 2),
    _AgentxConnOpenTime_Type()
)
agentxConnOpenTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentxConnOpenTime.setStatus("current")
_AgentxConnTransportDomain_Type = TDomain
_AgentxConnTransportDomain_Object = MibTableColumn
agentxConnTransportDomain = _AgentxConnTransportDomain_Object(
    (1, 3, 6, 1, 2, 1, 74, 1, 2, 2, 1, 3),
    _AgentxConnTransportDomain_Type()
)
agentxConnTransportDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentxConnTransportDomain.setStatus("current")
_AgentxConnTransportAddress_Type = AgentxTAddress
_AgentxConnTransportAddress_Object = MibTableColumn
agentxConnTransportAddress = _AgentxConnTransportAddress_Object(
    (1, 3, 6, 1, 2, 1, 74, 1, 2, 2, 1, 4),
    _AgentxConnTransportAddress_Type()
)
agentxConnTransportAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentxConnTransportAddress.setStatus("current")
_AgentxSession_ObjectIdentity = ObjectIdentity
agentxSession = _AgentxSession_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 74, 1, 3)
)
_AgentxSessionTableLastChange_Type = TimeStamp
_AgentxSessionTableLastChange_Object = MibScalar
agentxSessionTableLastChange = _AgentxSessionTableLastChange_Object(
    (1, 3, 6, 1, 2, 1, 74, 1, 3, 1),
    _AgentxSessionTableLastChange_Type()
)
agentxSessionTableLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentxSessionTableLastChange.setStatus("current")
_AgentxSessionTable_Object = MibTable
agentxSessionTable = _AgentxSessionTable_Object(
    (1, 3, 6, 1, 2, 1, 74, 1, 3, 2)
)
if mibBuilder.loadTexts:
    agentxSessionTable.setStatus("current")
_AgentxSessionEntry_Object = MibTableRow
agentxSessionEntry = _AgentxSessionEntry_Object(
    (1, 3, 6, 1, 2, 1, 74, 1, 3, 2, 1)
)
agentxSessionEntry.setIndexNames(
    (0, "AGENTX-MIB", "agentxConnIndex"),
    (0, "AGENTX-MIB", "agentxSessionIndex"),
)
if mibBuilder.loadTexts:
    agentxSessionEntry.setStatus("current")


class _AgentxSessionIndex_Type(Unsigned32):
    """Custom type agentxSessionIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AgentxSessionIndex_Type.__name__ = "Unsigned32"
_AgentxSessionIndex_Object = MibTableColumn
agentxSessionIndex = _AgentxSessionIndex_Object(
    (1, 3, 6, 1, 2, 1, 74, 1, 3, 2, 1, 1),
    _AgentxSessionIndex_Type()
)
agentxSessionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentxSessionIndex.setStatus("current")
_AgentxSessionObjectID_Type = ObjectIdentifier
_AgentxSessionObjectID_Object = MibTableColumn
agentxSessionObjectID = _AgentxSessionObjectID_Object(
    (1, 3, 6, 1, 2, 1, 74, 1, 3, 2, 1, 2),
    _AgentxSessionObjectID_Type()
)
agentxSessionObjectID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentxSessionObjectID.setStatus("current")
_AgentxSessionDescr_Type = SnmpAdminString
_AgentxSessionDescr_Object = MibTableColumn
agentxSessionDescr = _AgentxSessionDescr_Object(
    (1, 3, 6, 1, 2, 1, 74, 1, 3, 2, 1, 3),
    _AgentxSessionDescr_Type()
)
agentxSessionDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentxSessionDescr.setStatus("current")


class _AgentxSessionAdminStatus_Type(Integer32):
    """Custom type agentxSessionAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_AgentxSessionAdminStatus_Type.__name__ = "Integer32"
_AgentxSessionAdminStatus_Object = MibTableColumn
agentxSessionAdminStatus = _AgentxSessionAdminStatus_Object(
    (1, 3, 6, 1, 2, 1, 74, 1, 3, 2, 1, 4),
    _AgentxSessionAdminStatus_Type()
)
agentxSessionAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentxSessionAdminStatus.setStatus("current")
_AgentxSessionOpenTime_Type = TimeStamp
_AgentxSessionOpenTime_Object = MibTableColumn
agentxSessionOpenTime = _AgentxSessionOpenTime_Object(
    (1, 3, 6, 1, 2, 1, 74, 1, 3, 2, 1, 5),
    _AgentxSessionOpenTime_Type()
)
agentxSessionOpenTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentxSessionOpenTime.setStatus("current")


class _AgentxSessionAgentXVer_Type(Integer32):
    """Custom type agentxSessionAgentXVer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AgentxSessionAgentXVer_Type.__name__ = "Integer32"
_AgentxSessionAgentXVer_Object = MibTableColumn
agentxSessionAgentXVer = _AgentxSessionAgentXVer_Object(
    (1, 3, 6, 1, 2, 1, 74, 1, 3, 2, 1, 6),
    _AgentxSessionAgentXVer_Type()
)
agentxSessionAgentXVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentxSessionAgentXVer.setStatus("current")


class _AgentxSessionTimeout_Type(Integer32):
    """Custom type agentxSessionTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AgentxSessionTimeout_Type.__name__ = "Integer32"
_AgentxSessionTimeout_Object = MibTableColumn
agentxSessionTimeout = _AgentxSessionTimeout_Object(
    (1, 3, 6, 1, 2, 1, 74, 1, 3, 2, 1, 7),
    _AgentxSessionTimeout_Type()
)
agentxSessionTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentxSessionTimeout.setStatus("current")
if mibBuilder.loadTexts:
    agentxSessionTimeout.setUnits("seconds")
_AgentxRegistration_ObjectIdentity = ObjectIdentity
agentxRegistration = _AgentxRegistration_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 74, 1, 4)
)
_AgentxRegistrationTableLastChange_Type = TimeStamp
_AgentxRegistrationTableLastChange_Object = MibScalar
agentxRegistrationTableLastChange = _AgentxRegistrationTableLastChange_Object(
    (1, 3, 6, 1, 2, 1, 74, 1, 4, 1),
    _AgentxRegistrationTableLastChange_Type()
)
agentxRegistrationTableLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentxRegistrationTableLastChange.setStatus("current")
_AgentxRegistrationTable_Object = MibTable
agentxRegistrationTable = _AgentxRegistrationTable_Object(
    (1, 3, 6, 1, 2, 1, 74, 1, 4, 2)
)
if mibBuilder.loadTexts:
    agentxRegistrationTable.setStatus("current")
_AgentxRegistrationEntry_Object = MibTableRow
agentxRegistrationEntry = _AgentxRegistrationEntry_Object(
    (1, 3, 6, 1, 2, 1, 74, 1, 4, 2, 1)
)
agentxRegistrationEntry.setIndexNames(
    (0, "AGENTX-MIB", "agentxConnIndex"),
    (0, "AGENTX-MIB", "agentxSessionIndex"),
    (0, "AGENTX-MIB", "agentxRegIndex"),
)
if mibBuilder.loadTexts:
    agentxRegistrationEntry.setStatus("current")


class _AgentxRegIndex_Type(Unsigned32):
    """Custom type agentxRegIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_AgentxRegIndex_Type.__name__ = "Unsigned32"
_AgentxRegIndex_Object = MibTableColumn
agentxRegIndex = _AgentxRegIndex_Object(
    (1, 3, 6, 1, 2, 1, 74, 1, 4, 2, 1, 1),
    _AgentxRegIndex_Type()
)
agentxRegIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentxRegIndex.setStatus("current")
_AgentxRegContext_Type = OctetString
_AgentxRegContext_Object = MibTableColumn
agentxRegContext = _AgentxRegContext_Object(
    (1, 3, 6, 1, 2, 1, 74, 1, 4, 2, 1, 2),
    _AgentxRegContext_Type()
)
agentxRegContext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentxRegContext.setStatus("current")
_AgentxRegStart_Type = ObjectIdentifier
_AgentxRegStart_Object = MibTableColumn
agentxRegStart = _AgentxRegStart_Object(
    (1, 3, 6, 1, 2, 1, 74, 1, 4, 2, 1, 3),
    _AgentxRegStart_Type()
)
agentxRegStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentxRegStart.setStatus("current")
_AgentxRegRangeSubId_Type = Unsigned32
_AgentxRegRangeSubId_Object = MibTableColumn
agentxRegRangeSubId = _AgentxRegRangeSubId_Object(
    (1, 3, 6, 1, 2, 1, 74, 1, 4, 2, 1, 4),
    _AgentxRegRangeSubId_Type()
)
agentxRegRangeSubId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentxRegRangeSubId.setStatus("current")
_AgentxRegUpperBound_Type = Unsigned32
_AgentxRegUpperBound_Object = MibTableColumn
agentxRegUpperBound = _AgentxRegUpperBound_Object(
    (1, 3, 6, 1, 2, 1, 74, 1, 4, 2, 1, 5),
    _AgentxRegUpperBound_Type()
)
agentxRegUpperBound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentxRegUpperBound.setStatus("current")
_AgentxRegPriority_Type = Unsigned32
_AgentxRegPriority_Object = MibTableColumn
agentxRegPriority = _AgentxRegPriority_Object(
    (1, 3, 6, 1, 2, 1, 74, 1, 4, 2, 1, 6),
    _AgentxRegPriority_Type()
)
agentxRegPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentxRegPriority.setStatus("current")


class _AgentxRegTimeout_Type(Integer32):
    """Custom type agentxRegTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AgentxRegTimeout_Type.__name__ = "Integer32"
_AgentxRegTimeout_Object = MibTableColumn
agentxRegTimeout = _AgentxRegTimeout_Object(
    (1, 3, 6, 1, 2, 1, 74, 1, 4, 2, 1, 7),
    _AgentxRegTimeout_Type()
)
agentxRegTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentxRegTimeout.setStatus("current")
if mibBuilder.loadTexts:
    agentxRegTimeout.setUnits("seconds")
_AgentxRegInstance_Type = TruthValue
_AgentxRegInstance_Object = MibTableColumn
agentxRegInstance = _AgentxRegInstance_Object(
    (1, 3, 6, 1, 2, 1, 74, 1, 4, 2, 1, 8),
    _AgentxRegInstance_Type()
)
agentxRegInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentxRegInstance.setStatus("current")
_AgentxConformance_ObjectIdentity = ObjectIdentity
agentxConformance = _AgentxConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 74, 2)
)
_AgentxMIBGroups_ObjectIdentity = ObjectIdentity
agentxMIBGroups = _AgentxMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 74, 2, 1)
)
_AgentxMIBCompliances_ObjectIdentity = ObjectIdentity
agentxMIBCompliances = _AgentxMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 74, 2, 2)
)

# Managed Objects groups

agentxMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 74, 2, 1, 1)
)
agentxMIBGroup.setObjects(
      *(("AGENTX-MIB", "agentxDefaultTimeout"),
        ("AGENTX-MIB", "agentxMasterAgentXVer"),
        ("AGENTX-MIB", "agentxConnTableLastChange"),
        ("AGENTX-MIB", "agentxConnOpenTime"),
        ("AGENTX-MIB", "agentxConnTransportDomain"),
        ("AGENTX-MIB", "agentxConnTransportAddress"),
        ("AGENTX-MIB", "agentxSessionTableLastChange"),
        ("AGENTX-MIB", "agentxSessionTimeout"),
        ("AGENTX-MIB", "agentxSessionObjectID"),
        ("AGENTX-MIB", "agentxSessionDescr"),
        ("AGENTX-MIB", "agentxSessionAdminStatus"),
        ("AGENTX-MIB", "agentxSessionOpenTime"),
        ("AGENTX-MIB", "agentxSessionAgentXVer"),
        ("AGENTX-MIB", "agentxRegistrationTableLastChange"),
        ("AGENTX-MIB", "agentxRegContext"),
        ("AGENTX-MIB", "agentxRegStart"),
        ("AGENTX-MIB", "agentxRegRangeSubId"),
        ("AGENTX-MIB", "agentxRegUpperBound"),
        ("AGENTX-MIB", "agentxRegPriority"),
        ("AGENTX-MIB", "agentxRegTimeout"),
        ("AGENTX-MIB", "agentxRegInstance"))
)
if mibBuilder.loadTexts:
    agentxMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

agentxMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 74, 2, 2, 1)
)
if mibBuilder.loadTexts:
    agentxMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AGENTX-MIB",
    **{"AgentxTAddress": AgentxTAddress,
       "agentxMIB": agentxMIB,
       "agentxObjects": agentxObjects,
       "agentxGeneral": agentxGeneral,
       "agentxDefaultTimeout": agentxDefaultTimeout,
       "agentxMasterAgentXVer": agentxMasterAgentXVer,
       "agentxConnection": agentxConnection,
       "agentxConnTableLastChange": agentxConnTableLastChange,
       "agentxConnectionTable": agentxConnectionTable,
       "agentxConnectionEntry": agentxConnectionEntry,
       "agentxConnIndex": agentxConnIndex,
       "agentxConnOpenTime": agentxConnOpenTime,
       "agentxConnTransportDomain": agentxConnTransportDomain,
       "agentxConnTransportAddress": agentxConnTransportAddress,
       "agentxSession": agentxSession,
       "agentxSessionTableLastChange": agentxSessionTableLastChange,
       "agentxSessionTable": agentxSessionTable,
       "agentxSessionEntry": agentxSessionEntry,
       "agentxSessionIndex": agentxSessionIndex,
       "agentxSessionObjectID": agentxSessionObjectID,
       "agentxSessionDescr": agentxSessionDescr,
       "agentxSessionAdminStatus": agentxSessionAdminStatus,
       "agentxSessionOpenTime": agentxSessionOpenTime,
       "agentxSessionAgentXVer": agentxSessionAgentXVer,
       "agentxSessionTimeout": agentxSessionTimeout,
       "agentxRegistration": agentxRegistration,
       "agentxRegistrationTableLastChange": agentxRegistrationTableLastChange,
       "agentxRegistrationTable": agentxRegistrationTable,
       "agentxRegistrationEntry": agentxRegistrationEntry,
       "agentxRegIndex": agentxRegIndex,
       "agentxRegContext": agentxRegContext,
       "agentxRegStart": agentxRegStart,
       "agentxRegRangeSubId": agentxRegRangeSubId,
       "agentxRegUpperBound": agentxRegUpperBound,
       "agentxRegPriority": agentxRegPriority,
       "agentxRegTimeout": agentxRegTimeout,
       "agentxRegInstance": agentxRegInstance,
       "agentxConformance": agentxConformance,
       "agentxMIBGroups": agentxMIBGroups,
       "agentxMIBGroup": agentxMIBGroup,
       "agentxMIBCompliances": agentxMIBCompliances,
       "agentxMIBCompliance": agentxMIBCompliance}
)
