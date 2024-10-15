# SNMP MIB module (PTOPO-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PTOPO-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:07:16 2024
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

(PhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "PhysicalIndex")

(AddressFamilyNumbers,) = mibBuilder.importSymbols(
    "IANA-ADDRESS-FAMILY-NUMBERS-MIB",
    "AddressFamilyNumbers")

(TimeFilter,) = mibBuilder.importSymbols(
    "RMON2-MIB",
    "TimeFilter")

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

(AutonomousType,
 DisplayString,
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "AutonomousType",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ptopoMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 79)
)
ptopoMIB.setRevisions(
        ("2000-09-21 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class PtopoGenAddr(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )



class PtopoChassisIdType(Integer32, TextualConvention):
    status = "current"
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
        *(("chasIdEntPhysicalAlias", 1),
          ("chasIdIfAlias", 2),
          ("chasIdMacAddress", 4),
          ("chasIdPortEntPhysicalAlias", 3),
          ("chasIdPtopoGenAddr", 5))
    )



class PtopoChassisId(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )



class PtopoPortIdType(Integer32, TextualConvention):
    status = "current"
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
        *(("portIdEntPhysicalAlias", 2),
          ("portIdIfAlias", 1),
          ("portIdMacAddr", 3),
          ("portIdPtopoGenAddr", 4))
    )



class PtopoPortId(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )



class PtopoAddrSeenState(Integer32, TextualConvention):
    status = "current"
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
        *(("multiAddr", 4),
          ("notUsed", 1),
          ("oneAddr", 3),
          ("unknown", 2))
    )



# MIB Managed Objects in the order of their OIDs

_PtopoMIBObjects_ObjectIdentity = ObjectIdentity
ptopoMIBObjects = _PtopoMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 79, 1)
)
_PtopoData_ObjectIdentity = ObjectIdentity
ptopoData = _PtopoData_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 79, 1, 1)
)
_PtopoConnTable_Object = MibTable
ptopoConnTable = _PtopoConnTable_Object(
    (1, 3, 6, 1, 2, 1, 79, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ptopoConnTable.setStatus("current")
_PtopoConnEntry_Object = MibTableRow
ptopoConnEntry = _PtopoConnEntry_Object(
    (1, 3, 6, 1, 2, 1, 79, 1, 1, 1, 1)
)
ptopoConnEntry.setIndexNames(
    (0, "PTOPO-MIB", "ptopoConnTimeMark"),
    (0, "PTOPO-MIB", "ptopoConnLocalChassis"),
    (0, "PTOPO-MIB", "ptopoConnLocalPort"),
    (0, "PTOPO-MIB", "ptopoConnIndex"),
)
if mibBuilder.loadTexts:
    ptopoConnEntry.setStatus("current")
_PtopoConnTimeMark_Type = TimeFilter
_PtopoConnTimeMark_Object = MibTableColumn
ptopoConnTimeMark = _PtopoConnTimeMark_Object(
    (1, 3, 6, 1, 2, 1, 79, 1, 1, 1, 1, 1),
    _PtopoConnTimeMark_Type()
)
ptopoConnTimeMark.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ptopoConnTimeMark.setStatus("current")
_PtopoConnLocalChassis_Type = PhysicalIndex
_PtopoConnLocalChassis_Object = MibTableColumn
ptopoConnLocalChassis = _PtopoConnLocalChassis_Object(
    (1, 3, 6, 1, 2, 1, 79, 1, 1, 1, 1, 2),
    _PtopoConnLocalChassis_Type()
)
ptopoConnLocalChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ptopoConnLocalChassis.setStatus("current")
_PtopoConnLocalPort_Type = PhysicalIndex
_PtopoConnLocalPort_Object = MibTableColumn
ptopoConnLocalPort = _PtopoConnLocalPort_Object(
    (1, 3, 6, 1, 2, 1, 79, 1, 1, 1, 1, 3),
    _PtopoConnLocalPort_Type()
)
ptopoConnLocalPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ptopoConnLocalPort.setStatus("current")


class _PtopoConnIndex_Type(Integer32):
    """Custom type ptopoConnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PtopoConnIndex_Type.__name__ = "Integer32"
_PtopoConnIndex_Object = MibTableColumn
ptopoConnIndex = _PtopoConnIndex_Object(
    (1, 3, 6, 1, 2, 1, 79, 1, 1, 1, 1, 4),
    _PtopoConnIndex_Type()
)
ptopoConnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ptopoConnIndex.setStatus("current")
_PtopoConnRemoteChassisType_Type = PtopoChassisIdType
_PtopoConnRemoteChassisType_Object = MibTableColumn
ptopoConnRemoteChassisType = _PtopoConnRemoteChassisType_Object(
    (1, 3, 6, 1, 2, 1, 79, 1, 1, 1, 1, 5),
    _PtopoConnRemoteChassisType_Type()
)
ptopoConnRemoteChassisType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ptopoConnRemoteChassisType.setStatus("current")
_PtopoConnRemoteChassis_Type = PtopoChassisId
_PtopoConnRemoteChassis_Object = MibTableColumn
ptopoConnRemoteChassis = _PtopoConnRemoteChassis_Object(
    (1, 3, 6, 1, 2, 1, 79, 1, 1, 1, 1, 6),
    _PtopoConnRemoteChassis_Type()
)
ptopoConnRemoteChassis.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ptopoConnRemoteChassis.setStatus("current")
_PtopoConnRemotePortType_Type = PtopoPortIdType
_PtopoConnRemotePortType_Object = MibTableColumn
ptopoConnRemotePortType = _PtopoConnRemotePortType_Object(
    (1, 3, 6, 1, 2, 1, 79, 1, 1, 1, 1, 7),
    _PtopoConnRemotePortType_Type()
)
ptopoConnRemotePortType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ptopoConnRemotePortType.setStatus("current")
_PtopoConnRemotePort_Type = PtopoPortId
_PtopoConnRemotePort_Object = MibTableColumn
ptopoConnRemotePort = _PtopoConnRemotePort_Object(
    (1, 3, 6, 1, 2, 1, 79, 1, 1, 1, 1, 8),
    _PtopoConnRemotePort_Type()
)
ptopoConnRemotePort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ptopoConnRemotePort.setStatus("current")
_PtopoConnDiscAlgorithm_Type = AutonomousType
_PtopoConnDiscAlgorithm_Object = MibTableColumn
ptopoConnDiscAlgorithm = _PtopoConnDiscAlgorithm_Object(
    (1, 3, 6, 1, 2, 1, 79, 1, 1, 1, 1, 9),
    _PtopoConnDiscAlgorithm_Type()
)
ptopoConnDiscAlgorithm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptopoConnDiscAlgorithm.setStatus("current")
_PtopoConnAgentNetAddrType_Type = AddressFamilyNumbers
_PtopoConnAgentNetAddrType_Object = MibTableColumn
ptopoConnAgentNetAddrType = _PtopoConnAgentNetAddrType_Object(
    (1, 3, 6, 1, 2, 1, 79, 1, 1, 1, 1, 10),
    _PtopoConnAgentNetAddrType_Type()
)
ptopoConnAgentNetAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ptopoConnAgentNetAddrType.setStatus("current")
_PtopoConnAgentNetAddr_Type = PtopoGenAddr
_PtopoConnAgentNetAddr_Object = MibTableColumn
ptopoConnAgentNetAddr = _PtopoConnAgentNetAddr_Object(
    (1, 3, 6, 1, 2, 1, 79, 1, 1, 1, 1, 11),
    _PtopoConnAgentNetAddr_Type()
)
ptopoConnAgentNetAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ptopoConnAgentNetAddr.setStatus("current")
_PtopoConnMultiMacSASeen_Type = PtopoAddrSeenState
_PtopoConnMultiMacSASeen_Object = MibTableColumn
ptopoConnMultiMacSASeen = _PtopoConnMultiMacSASeen_Object(
    (1, 3, 6, 1, 2, 1, 79, 1, 1, 1, 1, 12),
    _PtopoConnMultiMacSASeen_Type()
)
ptopoConnMultiMacSASeen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptopoConnMultiMacSASeen.setStatus("current")
_PtopoConnMultiNetSASeen_Type = PtopoAddrSeenState
_PtopoConnMultiNetSASeen_Object = MibTableColumn
ptopoConnMultiNetSASeen = _PtopoConnMultiNetSASeen_Object(
    (1, 3, 6, 1, 2, 1, 79, 1, 1, 1, 1, 13),
    _PtopoConnMultiNetSASeen_Type()
)
ptopoConnMultiNetSASeen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptopoConnMultiNetSASeen.setStatus("current")


class _PtopoConnIsStatic_Type(TruthValue):
    """Custom type ptopoConnIsStatic based on TruthValue"""


_PtopoConnIsStatic_Object = MibTableColumn
ptopoConnIsStatic = _PtopoConnIsStatic_Object(
    (1, 3, 6, 1, 2, 1, 79, 1, 1, 1, 1, 14),
    _PtopoConnIsStatic_Type()
)
ptopoConnIsStatic.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ptopoConnIsStatic.setStatus("current")
_PtopoConnLastVerifyTime_Type = TimeStamp
_PtopoConnLastVerifyTime_Object = MibTableColumn
ptopoConnLastVerifyTime = _PtopoConnLastVerifyTime_Object(
    (1, 3, 6, 1, 2, 1, 79, 1, 1, 1, 1, 15),
    _PtopoConnLastVerifyTime_Type()
)
ptopoConnLastVerifyTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptopoConnLastVerifyTime.setStatus("current")
_PtopoConnRowStatus_Type = RowStatus
_PtopoConnRowStatus_Object = MibTableColumn
ptopoConnRowStatus = _PtopoConnRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 79, 1, 1, 1, 1, 16),
    _PtopoConnRowStatus_Type()
)
ptopoConnRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ptopoConnRowStatus.setStatus("current")
_PtopoGeneral_ObjectIdentity = ObjectIdentity
ptopoGeneral = _PtopoGeneral_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 79, 1, 2)
)
_PtopoLastChangeTime_Type = TimeStamp
_PtopoLastChangeTime_Object = MibScalar
ptopoLastChangeTime = _PtopoLastChangeTime_Object(
    (1, 3, 6, 1, 2, 1, 79, 1, 2, 1),
    _PtopoLastChangeTime_Type()
)
ptopoLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptopoLastChangeTime.setStatus("current")
_PtopoConnTabInserts_Type = Counter32
_PtopoConnTabInserts_Object = MibScalar
ptopoConnTabInserts = _PtopoConnTabInserts_Object(
    (1, 3, 6, 1, 2, 1, 79, 1, 2, 2),
    _PtopoConnTabInserts_Type()
)
ptopoConnTabInserts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptopoConnTabInserts.setStatus("current")
if mibBuilder.loadTexts:
    ptopoConnTabInserts.setUnits("table entries")
_PtopoConnTabDeletes_Type = Counter32
_PtopoConnTabDeletes_Object = MibScalar
ptopoConnTabDeletes = _PtopoConnTabDeletes_Object(
    (1, 3, 6, 1, 2, 1, 79, 1, 2, 3),
    _PtopoConnTabDeletes_Type()
)
ptopoConnTabDeletes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptopoConnTabDeletes.setStatus("current")
if mibBuilder.loadTexts:
    ptopoConnTabDeletes.setUnits("table entries")
_PtopoConnTabDrops_Type = Counter32
_PtopoConnTabDrops_Object = MibScalar
ptopoConnTabDrops = _PtopoConnTabDrops_Object(
    (1, 3, 6, 1, 2, 1, 79, 1, 2, 4),
    _PtopoConnTabDrops_Type()
)
ptopoConnTabDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptopoConnTabDrops.setStatus("current")
if mibBuilder.loadTexts:
    ptopoConnTabDrops.setUnits("table entries")
_PtopoConnTabAgeouts_Type = Counter32
_PtopoConnTabAgeouts_Object = MibScalar
ptopoConnTabAgeouts = _PtopoConnTabAgeouts_Object(
    (1, 3, 6, 1, 2, 1, 79, 1, 2, 5),
    _PtopoConnTabAgeouts_Type()
)
ptopoConnTabAgeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptopoConnTabAgeouts.setStatus("current")
_PtopoConfig_ObjectIdentity = ObjectIdentity
ptopoConfig = _PtopoConfig_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 79, 1, 3)
)


class _PtopoConfigTrapInterval_Type(Integer32):
    """Custom type ptopoConfigTrapInterval based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(5, 3600),
    )


_PtopoConfigTrapInterval_Type.__name__ = "Integer32"
_PtopoConfigTrapInterval_Object = MibScalar
ptopoConfigTrapInterval = _PtopoConfigTrapInterval_Object(
    (1, 3, 6, 1, 2, 1, 79, 1, 3, 1),
    _PtopoConfigTrapInterval_Type()
)
ptopoConfigTrapInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ptopoConfigTrapInterval.setStatus("current")
if mibBuilder.loadTexts:
    ptopoConfigTrapInterval.setUnits("seconds")


class _PtopoConfigMaxHoldTime_Type(Integer32):
    """Custom type ptopoConfigMaxHoldTime based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PtopoConfigMaxHoldTime_Type.__name__ = "Integer32"
_PtopoConfigMaxHoldTime_Object = MibScalar
ptopoConfigMaxHoldTime = _PtopoConfigMaxHoldTime_Object(
    (1, 3, 6, 1, 2, 1, 79, 1, 3, 2),
    _PtopoConfigMaxHoldTime_Type()
)
ptopoConfigMaxHoldTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ptopoConfigMaxHoldTime.setStatus("current")
if mibBuilder.loadTexts:
    ptopoConfigMaxHoldTime.setUnits("seconds")
_PtopoMIBNotifications_ObjectIdentity = ObjectIdentity
ptopoMIBNotifications = _PtopoMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 79, 2)
)
_PtopoMIBTrapPrefix_ObjectIdentity = ObjectIdentity
ptopoMIBTrapPrefix = _PtopoMIBTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 79, 2, 0)
)
_PtopoRegistrationPoints_ObjectIdentity = ObjectIdentity
ptopoRegistrationPoints = _PtopoRegistrationPoints_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 79, 3)
)
_PtopoDiscoveryMechanisms_ObjectIdentity = ObjectIdentity
ptopoDiscoveryMechanisms = _PtopoDiscoveryMechanisms_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 79, 3, 1)
)
_PtopoDiscoveryLocal_ObjectIdentity = ObjectIdentity
ptopoDiscoveryLocal = _PtopoDiscoveryLocal_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 79, 3, 1, 1)
)
_PtopoConformance_ObjectIdentity = ObjectIdentity
ptopoConformance = _PtopoConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 79, 4)
)
_PtopoCompliances_ObjectIdentity = ObjectIdentity
ptopoCompliances = _PtopoCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 79, 4, 1)
)
_PtopoGroups_ObjectIdentity = ObjectIdentity
ptopoGroups = _PtopoGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 79, 4, 2)
)

# Managed Objects groups

ptopoDataGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 79, 4, 2, 1)
)
ptopoDataGroup.setObjects(
      *(("PTOPO-MIB", "ptopoConnRemoteChassisType"),
        ("PTOPO-MIB", "ptopoConnRemoteChassis"),
        ("PTOPO-MIB", "ptopoConnRemotePortType"),
        ("PTOPO-MIB", "ptopoConnRemotePort"),
        ("PTOPO-MIB", "ptopoConnDiscAlgorithm"),
        ("PTOPO-MIB", "ptopoConnAgentNetAddrType"),
        ("PTOPO-MIB", "ptopoConnAgentNetAddr"),
        ("PTOPO-MIB", "ptopoConnMultiMacSASeen"),
        ("PTOPO-MIB", "ptopoConnMultiNetSASeen"),
        ("PTOPO-MIB", "ptopoConnIsStatic"),
        ("PTOPO-MIB", "ptopoConnLastVerifyTime"),
        ("PTOPO-MIB", "ptopoConnRowStatus"))
)
if mibBuilder.loadTexts:
    ptopoDataGroup.setStatus("current")

ptopoGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 79, 4, 2, 2)
)
ptopoGeneralGroup.setObjects(
      *(("PTOPO-MIB", "ptopoLastChangeTime"),
        ("PTOPO-MIB", "ptopoConnTabInserts"),
        ("PTOPO-MIB", "ptopoConnTabDeletes"),
        ("PTOPO-MIB", "ptopoConnTabDrops"),
        ("PTOPO-MIB", "ptopoConnTabAgeouts"))
)
if mibBuilder.loadTexts:
    ptopoGeneralGroup.setStatus("current")

ptopoConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 79, 4, 2, 3)
)
ptopoConfigGroup.setObjects(
      *(("PTOPO-MIB", "ptopoConfigTrapInterval"),
        ("PTOPO-MIB", "ptopoConfigMaxHoldTime"))
)
if mibBuilder.loadTexts:
    ptopoConfigGroup.setStatus("current")


# Notification objects

ptopoConfigChange = NotificationType(
    (1, 3, 6, 1, 2, 1, 79, 2, 0, 1)
)
ptopoConfigChange.setObjects(
      *(("PTOPO-MIB", "ptopoConnTabInserts"),
        ("PTOPO-MIB", "ptopoConnTabDeletes"),
        ("PTOPO-MIB", "ptopoConnTabDrops"),
        ("PTOPO-MIB", "ptopoConnTabAgeouts"))
)
if mibBuilder.loadTexts:
    ptopoConfigChange.setStatus(
        "current"
    )


# Notifications groups

ptopoNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 2, 1, 79, 4, 2, 4)
)
ptopoNotificationsGroup.setObjects(
    ("PTOPO-MIB", "ptopoConfigChange")
)
if mibBuilder.loadTexts:
    ptopoNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ptopoCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 79, 4, 1, 1)
)
if mibBuilder.loadTexts:
    ptopoCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PTOPO-MIB",
    **{"PtopoGenAddr": PtopoGenAddr,
       "PtopoChassisIdType": PtopoChassisIdType,
       "PtopoChassisId": PtopoChassisId,
       "PtopoPortIdType": PtopoPortIdType,
       "PtopoPortId": PtopoPortId,
       "PtopoAddrSeenState": PtopoAddrSeenState,
       "ptopoMIB": ptopoMIB,
       "ptopoMIBObjects": ptopoMIBObjects,
       "ptopoData": ptopoData,
       "ptopoConnTable": ptopoConnTable,
       "ptopoConnEntry": ptopoConnEntry,
       "ptopoConnTimeMark": ptopoConnTimeMark,
       "ptopoConnLocalChassis": ptopoConnLocalChassis,
       "ptopoConnLocalPort": ptopoConnLocalPort,
       "ptopoConnIndex": ptopoConnIndex,
       "ptopoConnRemoteChassisType": ptopoConnRemoteChassisType,
       "ptopoConnRemoteChassis": ptopoConnRemoteChassis,
       "ptopoConnRemotePortType": ptopoConnRemotePortType,
       "ptopoConnRemotePort": ptopoConnRemotePort,
       "ptopoConnDiscAlgorithm": ptopoConnDiscAlgorithm,
       "ptopoConnAgentNetAddrType": ptopoConnAgentNetAddrType,
       "ptopoConnAgentNetAddr": ptopoConnAgentNetAddr,
       "ptopoConnMultiMacSASeen": ptopoConnMultiMacSASeen,
       "ptopoConnMultiNetSASeen": ptopoConnMultiNetSASeen,
       "ptopoConnIsStatic": ptopoConnIsStatic,
       "ptopoConnLastVerifyTime": ptopoConnLastVerifyTime,
       "ptopoConnRowStatus": ptopoConnRowStatus,
       "ptopoGeneral": ptopoGeneral,
       "ptopoLastChangeTime": ptopoLastChangeTime,
       "ptopoConnTabInserts": ptopoConnTabInserts,
       "ptopoConnTabDeletes": ptopoConnTabDeletes,
       "ptopoConnTabDrops": ptopoConnTabDrops,
       "ptopoConnTabAgeouts": ptopoConnTabAgeouts,
       "ptopoConfig": ptopoConfig,
       "ptopoConfigTrapInterval": ptopoConfigTrapInterval,
       "ptopoConfigMaxHoldTime": ptopoConfigMaxHoldTime,
       "ptopoMIBNotifications": ptopoMIBNotifications,
       "ptopoMIBTrapPrefix": ptopoMIBTrapPrefix,
       "ptopoConfigChange": ptopoConfigChange,
       "ptopoRegistrationPoints": ptopoRegistrationPoints,
       "ptopoDiscoveryMechanisms": ptopoDiscoveryMechanisms,
       "ptopoDiscoveryLocal": ptopoDiscoveryLocal,
       "ptopoConformance": ptopoConformance,
       "ptopoCompliances": ptopoCompliances,
       "ptopoCompliance": ptopoCompliance,
       "ptopoGroups": ptopoGroups,
       "ptopoDataGroup": ptopoDataGroup,
       "ptopoGeneralGroup": ptopoGeneralGroup,
       "ptopoConfigGroup": ptopoConfigGroup,
       "ptopoNotificationsGroup": ptopoNotificationsGroup}
)
