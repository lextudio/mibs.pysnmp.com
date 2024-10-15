# SNMP MIB module (RADLAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RADLAN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:36:57 2024
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

(BridgeId,
 MacAddress,
 Timeout,
 dot1dBasePort,
 dot1dBasePortEntry) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "BridgeId",
    "MacAddress",
    "Timeout",
    "dot1dBasePort",
    "dot1dBasePortEntry")

(PaeControlledPortStatus,
 dot1xAuthSessionStatsEntry,
 dot1xPaePortNumber) = mibBuilder.importSymbols(
    "IEEE8021-PAE-MIB",
    "PaeControlledPortStatus",
    "dot1xAuthSessionStatsEntry",
    "dot1xPaePortNumber")

(InterfaceIndex,
 InterfaceIndexOrZero,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero",
    "ifIndex")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

(PortList,
 VlanIndex,
 dot1qFdbId) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList",
    "VlanIndex",
    "dot1qFdbId")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 enterprises,
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
    "enterprises",
    "iso")

(Counter_32,
 Integer_32,
 Unsigned_32) = mibBuilder.importSymbols(
    "SNMPv2-SMI-v1",
    "Counter-32",
    "Integer-32",
    "Unsigned-32")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(DateAndTime,
 DisplayString,
 PhysAddress,
 RowPointer,
 RowStatus,
 TimeInterval,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC-v1",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowPointer",
    "RowStatus",
    "TimeInterval",
    "TruthValue")


# MODULE-IDENTITY


# Types definitions



class Percents(Integer32):
    """Custom type Percents based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )





class NetNumber(OctetString):
    """Custom type NetNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )





class VlanPriority(Integer32):
    """Custom type VlanPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )





class RlStormCtrlRateUnit(Integer32):
    """Custom type RlStormCtrlRateUnit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("bytesPerSecond", 2),
          ("framesPerBuffer", 3),
          ("kiloBitsPerSecond", 6),
          ("kiloBytesPerSecond", 5),
          ("packetsPerSecond", 1),
          ("precentages", 4))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Rnd_ObjectIdentity = ObjectIdentity
rnd = _Rnd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89)
)
_RndNotifications_ObjectIdentity = ObjectIdentity
rndNotifications = _RndNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 0)
)
if mibBuilder.loadTexts:
    rndNotifications.setStatus("current")
_RndMng_ObjectIdentity = ObjectIdentity
rndMng = _RndMng_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 1)
)
_RndDeviceParams_ObjectIdentity = ObjectIdentity
rndDeviceParams = _RndDeviceParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 2)
)


class _RndBridgeType_Type(Integer32):
    """Custom type rndBridgeType based on Integer32"""
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
              8,
              9,
              10,
              11,
              12,
              13,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48)
        )
    )
    namedValues = NamedValues(
        *(("ceb", 2),
          ("ceblb", 3),
          ("ete", 12),
          ("gatelinx", 36),
          ("ielb", 30),
          ("itlb", 35),
          ("leb", 31),
          ("lre", 46),
          ("ltb", 8),
          ("mrt", 47),
          ("ogRanTR", 38),
          ("ogRubE", 42),
          ("ogRubT", 43),
          ("ogVan", 40),
          ("openGate12", 32),
          ("openGate2", 37),
          ("openGate4", 33),
          ("ran", 34),
          ("rdapter", 39),
          ("reb", 1),
          ("rebsx", 6),
          ("rete", 13),
          ("rtb", 7),
          ("rtre", 10),
          ("tre", 9),
          ("vGate2", 48),
          ("vGate4", 45),
          ("wanGate", 41),
          ("wanGateI", 44),
          ("xeb", 4),
          ("xeb1", 5),
          ("xtb", 11))
    )


_RndBridgeType_Type.__name__ = "Integer32"
_RndBridgeType_Object = MibScalar
rndBridgeType = _RndBridgeType_Object(
    (1, 3, 6, 1, 4, 1, 89, 2, 1),
    _RndBridgeType_Type()
)
rndBridgeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rndBridgeType.setStatus("mandatory")
_RndInactiveArpTimeOut_Type = Integer32
_RndInactiveArpTimeOut_Object = MibScalar
rndInactiveArpTimeOut = _RndInactiveArpTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 89, 2, 2),
    _RndInactiveArpTimeOut_Type()
)
rndInactiveArpTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndInactiveArpTimeOut.setStatus("mandatory")
_RndBridgeAlarm_ObjectIdentity = ObjectIdentity
rndBridgeAlarm = _RndBridgeAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 2, 3)
)
_RndErrorDesc_Type = DisplayString
_RndErrorDesc_Object = MibScalar
rndErrorDesc = _RndErrorDesc_Object(
    (1, 3, 6, 1, 4, 1, 89, 2, 3, 1),
    _RndErrorDesc_Type()
)
rndErrorDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rndErrorDesc.setStatus("mandatory")


class _RndErrorSeverity_Type(Integer32):
    """Custom type rndErrorSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("error", 2),
          ("fatal-error", 3),
          ("info", 0),
          ("warning", 1))
    )


_RndErrorSeverity_Type.__name__ = "Integer32"
_RndErrorSeverity_Object = MibScalar
rndErrorSeverity = _RndErrorSeverity_Object(
    (1, 3, 6, 1, 4, 1, 89, 2, 3, 2),
    _RndErrorSeverity_Type()
)
rndErrorSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rndErrorSeverity.setStatus("mandatory")
_RndBrgVersion_Type = DisplayString
_RndBrgVersion_Object = MibScalar
rndBrgVersion = _RndBrgVersion_Object(
    (1, 3, 6, 1, 4, 1, 89, 2, 4),
    _RndBrgVersion_Type()
)
rndBrgVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rndBrgVersion.setStatus("mandatory")
_RndBrgFeatures_Type = OctetString
_RndBrgFeatures_Object = MibScalar
rndBrgFeatures = _RndBrgFeatures_Object(
    (1, 3, 6, 1, 4, 1, 89, 2, 5),
    _RndBrgFeatures_Type()
)
rndBrgFeatures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rndBrgFeatures.setStatus("mandatory")
_RndBrgLicense_Type = OctetString
_RndBrgLicense_Object = MibScalar
rndBrgLicense = _RndBrgLicense_Object(
    (1, 3, 6, 1, 4, 1, 89, 2, 6),
    _RndBrgLicense_Type()
)
rndBrgLicense.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndBrgLicense.setStatus("mandatory")
_RndIpHost_ObjectIdentity = ObjectIdentity
rndIpHost = _RndIpHost_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 2, 7)
)
_RndCommunityTable_Object = MibTable
rndCommunityTable = _RndCommunityTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 2, 7, 2)
)
if mibBuilder.loadTexts:
    rndCommunityTable.setStatus("mandatory")
_RndCommunityEntry_Object = MibTableRow
rndCommunityEntry = _RndCommunityEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 2, 7, 2, 1)
)
rndCommunityEntry.setIndexNames(
    (0, "RADLAN-MIB", "rndCommunityMngStationAddr"),
    (1, "RADLAN-MIB", "rndCommunityString"),
)
if mibBuilder.loadTexts:
    rndCommunityEntry.setStatus("mandatory")
_RndCommunityMngStationAddr_Type = IpAddress
_RndCommunityMngStationAddr_Object = MibTableColumn
rndCommunityMngStationAddr = _RndCommunityMngStationAddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 2, 7, 2, 1, 1),
    _RndCommunityMngStationAddr_Type()
)
rndCommunityMngStationAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndCommunityMngStationAddr.setStatus("mandatory")


class _RndCommunityString_Type(DisplayString):
    """Custom type rndCommunityString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_RndCommunityString_Type.__name__ = "DisplayString"
_RndCommunityString_Object = MibTableColumn
rndCommunityString = _RndCommunityString_Object(
    (1, 3, 6, 1, 4, 1, 89, 2, 7, 2, 1, 2),
    _RndCommunityString_Type()
)
rndCommunityString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndCommunityString.setStatus("mandatory")


class _RndCommunityAccess_Type(Integer32):
    """Custom type rndCommunityAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("readOnly", 1),
          ("readWrite", 2),
          ("super", 3))
    )


_RndCommunityAccess_Type.__name__ = "Integer32"
_RndCommunityAccess_Object = MibTableColumn
rndCommunityAccess = _RndCommunityAccess_Object(
    (1, 3, 6, 1, 4, 1, 89, 2, 7, 2, 1, 3),
    _RndCommunityAccess_Type()
)
rndCommunityAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndCommunityAccess.setStatus("mandatory")


class _RndCommunityTrapsEnable_Type(Integer32):
    """Custom type rndCommunityTrapsEnable based on Integer32"""
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
        *(("snmpV1", 1),
          ("snmpV2", 2),
          ("snmpV3", 3),
          ("trapsDisable", 4))
    )


_RndCommunityTrapsEnable_Type.__name__ = "Integer32"
_RndCommunityTrapsEnable_Object = MibTableColumn
rndCommunityTrapsEnable = _RndCommunityTrapsEnable_Object(
    (1, 3, 6, 1, 4, 1, 89, 2, 7, 2, 1, 4),
    _RndCommunityTrapsEnable_Type()
)
rndCommunityTrapsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndCommunityTrapsEnable.setStatus("mandatory")


class _RndCommunityStatus_Type(Integer32):
    """Custom type rndCommunityStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("invalid", 2))
    )


_RndCommunityStatus_Type.__name__ = "Integer32"
_RndCommunityStatus_Object = MibTableColumn
rndCommunityStatus = _RndCommunityStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 2, 7, 2, 1, 5),
    _RndCommunityStatus_Type()
)
rndCommunityStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndCommunityStatus.setStatus("mandatory")


class _RndCommunityPortSecurity_Type(Integer32):
    """Custom type rndCommunityPortSecurity based on Integer32"""
    defaultValue = 2

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


_RndCommunityPortSecurity_Type.__name__ = "Integer32"
_RndCommunityPortSecurity_Object = MibTableColumn
rndCommunityPortSecurity = _RndCommunityPortSecurity_Object(
    (1, 3, 6, 1, 4, 1, 89, 2, 7, 2, 1, 6),
    _RndCommunityPortSecurity_Type()
)
rndCommunityPortSecurity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndCommunityPortSecurity.setStatus("mandatory")


class _RndCommunityOwner_Type(DisplayString):
    """Custom type rndCommunityOwner based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RndCommunityOwner_Type.__name__ = "DisplayString"
_RndCommunityOwner_Object = MibTableColumn
rndCommunityOwner = _RndCommunityOwner_Object(
    (1, 3, 6, 1, 4, 1, 89, 2, 7, 2, 1, 7),
    _RndCommunityOwner_Type()
)
rndCommunityOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndCommunityOwner.setStatus("mandatory")


class _RndCommunityTrapDestPort_Type(Integer32):
    """Custom type rndCommunityTrapDestPort based on Integer32"""
    defaultValue = 162

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RndCommunityTrapDestPort_Type.__name__ = "Integer32"
_RndCommunityTrapDestPort_Object = MibTableColumn
rndCommunityTrapDestPort = _RndCommunityTrapDestPort_Object(
    (1, 3, 6, 1, 4, 1, 89, 2, 7, 2, 1, 8),
    _RndCommunityTrapDestPort_Type()
)
rndCommunityTrapDestPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndCommunityTrapDestPort.setStatus("mandatory")
_RlMridTable_Object = MibTable
rlMridTable = _RlMridTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 2, 7, 3)
)
if mibBuilder.loadTexts:
    rlMridTable.setStatus("mandatory")
_RlMridEntry_Object = MibTableRow
rlMridEntry = _RlMridEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 2, 7, 3, 1)
)
rlMridEntry.setIndexNames(
    (0, "RADLAN-MIB", "rndCommunityMngStationAddr"),
    (1, "RADLAN-MIB", "rndCommunityString"),
)
if mibBuilder.loadTexts:
    rlMridEntry.setStatus("mandatory")
_RlMridConnection_Type = Integer32
_RlMridConnection_Object = MibTableColumn
rlMridConnection = _RlMridConnection_Object(
    (1, 3, 6, 1, 4, 1, 89, 2, 7, 3, 1, 1),
    _RlMridConnection_Type()
)
rlMridConnection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlMridConnection.setStatus("mandatory")
_RlManagedMrid_Type = Integer32
_RlManagedMrid_Object = MibTableColumn
rlManagedMrid = _RlManagedMrid_Object(
    (1, 3, 6, 1, 4, 1, 89, 2, 7, 3, 1, 2),
    _RlManagedMrid_Type()
)
rlManagedMrid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlManagedMrid.setStatus("mandatory")
_RndIpHostManagement_ObjectIdentity = ObjectIdentity
rndIpHostManagement = _RndIpHostManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 2, 7, 4)
)
_RndIpHostManagementSupported_Type = TruthValue
_RndIpHostManagementSupported_Object = MibScalar
rndIpHostManagementSupported = _RndIpHostManagementSupported_Object(
    (1, 3, 6, 1, 4, 1, 89, 2, 7, 4, 1),
    _RndIpHostManagementSupported_Type()
)
rndIpHostManagementSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rndIpHostManagementSupported.setStatus("mandatory")
_RndIpHostManagementIfIndex_Type = Integer32
_RndIpHostManagementIfIndex_Object = MibScalar
rndIpHostManagementIfIndex = _RndIpHostManagementIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 2, 7, 4, 2),
    _RndIpHostManagementIfIndex_Type()
)
rndIpHostManagementIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndIpHostManagementIfIndex.setStatus("mandatory")


class _RndManagedTime_Type(DisplayString):
    """Custom type rndManagedTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_RndManagedTime_Type.__name__ = "DisplayString"
_RndManagedTime_Object = MibScalar
rndManagedTime = _RndManagedTime_Object(
    (1, 3, 6, 1, 4, 1, 89, 2, 8),
    _RndManagedTime_Type()
)
rndManagedTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndManagedTime.setStatus("mandatory")


class _RndManagedDate_Type(DisplayString):
    """Custom type rndManagedDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_RndManagedDate_Type.__name__ = "DisplayString"
_RndManagedDate_Object = MibScalar
rndManagedDate = _RndManagedDate_Object(
    (1, 3, 6, 1, 4, 1, 89, 2, 9),
    _RndManagedDate_Type()
)
rndManagedDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndManagedDate.setStatus("mandatory")
_RndBaseBootVersion_Type = DisplayString
_RndBaseBootVersion_Object = MibScalar
rndBaseBootVersion = _RndBaseBootVersion_Object(
    (1, 3, 6, 1, 4, 1, 89, 2, 10),
    _RndBaseBootVersion_Type()
)
rndBaseBootVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rndBaseBootVersion.setStatus("mandatory")
_GenGroup_ObjectIdentity = ObjectIdentity
genGroup = _GenGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 2, 11)
)
_GenGroupHWVersion_Type = DisplayString
_GenGroupHWVersion_Object = MibScalar
genGroupHWVersion = _GenGroupHWVersion_Object(
    (1, 3, 6, 1, 4, 1, 89, 2, 11, 1),
    _GenGroupHWVersion_Type()
)
genGroupHWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genGroupHWVersion.setStatus("mandatory")


class _GenGroupConfigurationSymbol_Type(DisplayString):
    """Custom type genGroupConfigurationSymbol based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_GenGroupConfigurationSymbol_Type.__name__ = "DisplayString"
_GenGroupConfigurationSymbol_Object = MibScalar
genGroupConfigurationSymbol = _GenGroupConfigurationSymbol_Object(
    (1, 3, 6, 1, 4, 1, 89, 2, 11, 2),
    _GenGroupConfigurationSymbol_Type()
)
genGroupConfigurationSymbol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genGroupConfigurationSymbol.setStatus("mandatory")


class _GenGroupHWStatus_Type(Integer32):
    """Custom type genGroupHWStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("hardwareProblems", 2),
          ("notSupported", 255),
          ("ok", 1))
    )


_GenGroupHWStatus_Type.__name__ = "Integer32"
_GenGroupHWStatus_Object = MibScalar
genGroupHWStatus = _GenGroupHWStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 2, 11, 3),
    _GenGroupHWStatus_Type()
)
genGroupHWStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genGroupHWStatus.setStatus("mandatory")
_RndBasePhysicalAddress_Type = PhysAddress
_RndBasePhysicalAddress_Object = MibScalar
rndBasePhysicalAddress = _RndBasePhysicalAddress_Object(
    (1, 3, 6, 1, 4, 1, 89, 2, 12),
    _RndBasePhysicalAddress_Type()
)
rndBasePhysicalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rndBasePhysicalAddress.setStatus("mandatory")
_RndSoftwareFile_ObjectIdentity = ObjectIdentity
rndSoftwareFile = _RndSoftwareFile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 2, 13)
)
_RndActiveSoftwareFileTable_Object = MibTable
rndActiveSoftwareFileTable = _RndActiveSoftwareFileTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 2, 13, 1)
)
if mibBuilder.loadTexts:
    rndActiveSoftwareFileTable.setStatus("mandatory")
_RndActiveSoftwareFileEntry_Object = MibTableRow
rndActiveSoftwareFileEntry = _RndActiveSoftwareFileEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 2, 13, 1, 1)
)
rndActiveSoftwareFileEntry.setIndexNames(
    (0, "RADLAN-MIB", "rndUnitNumber"),
)
if mibBuilder.loadTexts:
    rndActiveSoftwareFileEntry.setStatus("mandatory")
_RndUnitNumber_Type = Integer32
_RndUnitNumber_Object = MibTableColumn
rndUnitNumber = _RndUnitNumber_Object(
    (1, 3, 6, 1, 4, 1, 89, 2, 13, 1, 1, 1),
    _RndUnitNumber_Type()
)
rndUnitNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndUnitNumber.setStatus("mandatory")


class _RndActiveSoftwareFile_Type(Integer32):
    """Custom type rndActiveSoftwareFile based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("image1", 1),
          ("image2", 2))
    )


_RndActiveSoftwareFile_Type.__name__ = "Integer32"
_RndActiveSoftwareFile_Object = MibTableColumn
rndActiveSoftwareFile = _RndActiveSoftwareFile_Object(
    (1, 3, 6, 1, 4, 1, 89, 2, 13, 1, 1, 2),
    _RndActiveSoftwareFile_Type()
)
rndActiveSoftwareFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rndActiveSoftwareFile.setStatus("mandatory")


class _RndActiveSoftwareFileAfterReset_Type(Integer32):
    """Custom type rndActiveSoftwareFileAfterReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("image1", 1),
          ("image2", 2),
          ("invalidImage", 3))
    )


_RndActiveSoftwareFileAfterReset_Type.__name__ = "Integer32"
_RndActiveSoftwareFileAfterReset_Object = MibTableColumn
rndActiveSoftwareFileAfterReset = _RndActiveSoftwareFileAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 2, 13, 1, 1, 3),
    _RndActiveSoftwareFileAfterReset_Type()
)
rndActiveSoftwareFileAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndActiveSoftwareFileAfterReset.setStatus("mandatory")
_RndImageSize_Type = Integer32
_RndImageSize_Object = MibScalar
rndImageSize = _RndImageSize_Object(
    (1, 3, 6, 1, 4, 1, 89, 2, 14),
    _RndImageSize_Type()
)
rndImageSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rndImageSize.setStatus("mandatory")
_RndBackupConfigurationEnabled_Type = TruthValue
_RndBackupConfigurationEnabled_Object = MibScalar
rndBackupConfigurationEnabled = _RndBackupConfigurationEnabled_Object(
    (1, 3, 6, 1, 4, 1, 89, 2, 15),
    _RndBackupConfigurationEnabled_Type()
)
rndBackupConfigurationEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rndBackupConfigurationEnabled.setStatus("mandatory")
_RndImageInfo_ObjectIdentity = ObjectIdentity
rndImageInfo = _RndImageInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 2, 16)
)
_RndImageInfoTable_Object = MibTable
rndImageInfoTable = _RndImageInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 2, 16, 1)
)
if mibBuilder.loadTexts:
    rndImageInfoTable.setStatus("mandatory")
_RndImageInfoEntry_Object = MibTableRow
rndImageInfoEntry = _RndImageInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 2, 16, 1, 1)
)
rndImageInfoEntry.setIndexNames(
    (0, "RADLAN-MIB", "rndStackUnitNumber"),
)
if mibBuilder.loadTexts:
    rndImageInfoEntry.setStatus("mandatory")
_RndStackUnitNumber_Type = Integer32
_RndStackUnitNumber_Object = MibTableColumn
rndStackUnitNumber = _RndStackUnitNumber_Object(
    (1, 3, 6, 1, 4, 1, 89, 2, 16, 1, 1, 1),
    _RndStackUnitNumber_Type()
)
rndStackUnitNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndStackUnitNumber.setStatus("mandatory")
_RndImage1Name_Type = DisplayString
_RndImage1Name_Object = MibTableColumn
rndImage1Name = _RndImage1Name_Object(
    (1, 3, 6, 1, 4, 1, 89, 2, 16, 1, 1, 2),
    _RndImage1Name_Type()
)
rndImage1Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rndImage1Name.setStatus("mandatory")
_RndImage2Name_Type = DisplayString
_RndImage2Name_Object = MibTableColumn
rndImage2Name = _RndImage2Name_Object(
    (1, 3, 6, 1, 4, 1, 89, 2, 16, 1, 1, 3),
    _RndImage2Name_Type()
)
rndImage2Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rndImage2Name.setStatus("mandatory")
_RndImage1Version_Type = DisplayString
_RndImage1Version_Object = MibTableColumn
rndImage1Version = _RndImage1Version_Object(
    (1, 3, 6, 1, 4, 1, 89, 2, 16, 1, 1, 4),
    _RndImage1Version_Type()
)
rndImage1Version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rndImage1Version.setStatus("mandatory")
_RndImage2Version_Type = DisplayString
_RndImage2Version_Object = MibTableColumn
rndImage2Version = _RndImage2Version_Object(
    (1, 3, 6, 1, 4, 1, 89, 2, 16, 1, 1, 5),
    _RndImage2Version_Type()
)
rndImage2Version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rndImage2Version.setStatus("mandatory")
_RndImage1Date_Type = DisplayString
_RndImage1Date_Object = MibTableColumn
rndImage1Date = _RndImage1Date_Object(
    (1, 3, 6, 1, 4, 1, 89, 2, 16, 1, 1, 6),
    _RndImage1Date_Type()
)
rndImage1Date.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rndImage1Date.setStatus("mandatory")
_RndImage2Date_Type = DisplayString
_RndImage2Date_Object = MibTableColumn
rndImage2Date = _RndImage2Date_Object(
    (1, 3, 6, 1, 4, 1, 89, 2, 16, 1, 1, 7),
    _RndImage2Date_Type()
)
rndImage2Date.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rndImage2Date.setStatus("mandatory")
_RndImage1Time_Type = DisplayString
_RndImage1Time_Object = MibTableColumn
rndImage1Time = _RndImage1Time_Object(
    (1, 3, 6, 1, 4, 1, 89, 2, 16, 1, 1, 8),
    _RndImage1Time_Type()
)
rndImage1Time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rndImage1Time.setStatus("mandatory")
_RndImage2Time_Type = DisplayString
_RndImage2Time_Object = MibTableColumn
rndImage2Time = _RndImage2Time_Object(
    (1, 3, 6, 1, 4, 1, 89, 2, 16, 1, 1, 9),
    _RndImage2Time_Type()
)
rndImage2Time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rndImage2Time.setStatus("mandatory")
_RndBootP_ObjectIdentity = ObjectIdentity
rndBootP = _RndBootP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 24)
)


class _RndBootPServerAddress_Type(IpAddress):
    """Custom type rndBootPServerAddress based on IpAddress"""
    defaultHexValue = "00000000"


_RndBootPServerAddress_Object = MibScalar
rndBootPServerAddress = _RndBootPServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 89, 24, 1),
    _RndBootPServerAddress_Type()
)
rndBootPServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndBootPServerAddress.setStatus("mandatory")
_RndBootPRelaySecThreshold_Type = Integer32
_RndBootPRelaySecThreshold_Object = MibScalar
rndBootPRelaySecThreshold = _RndBootPRelaySecThreshold_Object(
    (1, 3, 6, 1, 4, 1, 89, 24, 2),
    _RndBootPRelaySecThreshold_Type()
)
rndBootPRelaySecThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndBootPRelaySecThreshold.setStatus("mandatory")
_IpSpec_ObjectIdentity = ObjectIdentity
ipSpec = _IpSpec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 26)
)
_RsTunning_ObjectIdentity = ObjectIdentity
rsTunning = _RsTunning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 29)
)
_RndApplications_ObjectIdentity = ObjectIdentity
rndApplications = _RndApplications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35)
)
_RsUDP_ObjectIdentity = ObjectIdentity
rsUDP = _RsUDP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 42)
)
_SwInterfaces_ObjectIdentity = ObjectIdentity
swInterfaces = _SwInterfaces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 43)
)
_RlIPmulticast_ObjectIdentity = ObjectIdentity
rlIPmulticast = _RlIPmulticast_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 46)
)
_RlFFT_ObjectIdentity = ObjectIdentity
rlFFT = _RlFFT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 47)
)
_Vlan_ObjectIdentity = ObjectIdentity
vlan = _Vlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 48)
)
_RlRmonControl_ObjectIdentity = ObjectIdentity
rlRmonControl = _RlRmonControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 49)
)
_RlBrgMacSwitch_ObjectIdentity = ObjectIdentity
rlBrgMacSwitch = _RlBrgMacSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 50)
)
_RlBrgMacSwVersion_Type = Integer32
_RlBrgMacSwVersion_Object = MibScalar
rlBrgMacSwVersion = _RlBrgMacSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 89, 50, 1),
    _RlBrgMacSwVersion_Type()
)
rlBrgMacSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlBrgMacSwVersion.setStatus("mandatory")
_RlBrgMacSwMaxTableNumber_Type = Integer32
_RlBrgMacSwMaxTableNumber_Object = MibScalar
rlBrgMacSwMaxTableNumber = _RlBrgMacSwMaxTableNumber_Object(
    (1, 3, 6, 1, 4, 1, 89, 50, 2),
    _RlBrgMacSwMaxTableNumber_Type()
)
rlBrgMacSwMaxTableNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlBrgMacSwMaxTableNumber.setStatus("mandatory")


class _RlBrgMacSwDynamicTables_Type(Integer32):
    """Custom type rlBrgMacSwDynamicTables based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("supported", 1),
          ("unsupported", 2))
    )


_RlBrgMacSwDynamicTables_Type.__name__ = "Integer32"
_RlBrgMacSwDynamicTables_Object = MibScalar
rlBrgMacSwDynamicTables = _RlBrgMacSwDynamicTables_Object(
    (1, 3, 6, 1, 4, 1, 89, 50, 3),
    _RlBrgMacSwDynamicTables_Type()
)
rlBrgMacSwDynamicTables.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlBrgMacSwDynamicTables.setStatus("mandatory")


class _RlBrgMacSwOldEntryDeleteMode_Type(Integer32):
    """Custom type rlBrgMacSwOldEntryDeleteMode based on Integer32"""
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
        *(("agingFlag", 2),
          ("agingTime", 3),
          ("boundaries", 4),
          ("refreshFlag", 1))
    )


_RlBrgMacSwOldEntryDeleteMode_Type.__name__ = "Integer32"
_RlBrgMacSwOldEntryDeleteMode_Object = MibScalar
rlBrgMacSwOldEntryDeleteMode = _RlBrgMacSwOldEntryDeleteMode_Object(
    (1, 3, 6, 1, 4, 1, 89, 50, 5),
    _RlBrgMacSwOldEntryDeleteMode_Type()
)
rlBrgMacSwOldEntryDeleteMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlBrgMacSwOldEntryDeleteMode.setStatus("mandatory")


class _RlBrgMacSwSpanningTree_Type(Integer32):
    """Custom type rlBrgMacSwSpanningTree based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("supported", 1),
          ("unsupported", 2))
    )


_RlBrgMacSwSpanningTree_Type.__name__ = "Integer32"
_RlBrgMacSwSpanningTree_Object = MibScalar
rlBrgMacSwSpanningTree = _RlBrgMacSwSpanningTree_Object(
    (1, 3, 6, 1, 4, 1, 89, 50, 6),
    _RlBrgMacSwSpanningTree_Type()
)
rlBrgMacSwSpanningTree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlBrgMacSwSpanningTree.setStatus("mandatory")


class _RlBrgMacSwKeyType_Type(Integer32):
    """Custom type rlBrgMacSwKeyType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("macOnly", 1),
          ("tagAndMac", 2))
    )


_RlBrgMacSwKeyType_Type.__name__ = "Integer32"
_RlBrgMacSwKeyType_Object = MibScalar
rlBrgMacSwKeyType = _RlBrgMacSwKeyType_Object(
    (1, 3, 6, 1, 4, 1, 89, 50, 7),
    _RlBrgMacSwKeyType_Type()
)
rlBrgMacSwKeyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlBrgMacSwKeyType.setStatus("mandatory")
_RlBrgMacSwYellowBoundary_Type = Integer32
_RlBrgMacSwYellowBoundary_Object = MibScalar
rlBrgMacSwYellowBoundary = _RlBrgMacSwYellowBoundary_Object(
    (1, 3, 6, 1, 4, 1, 89, 50, 8),
    _RlBrgMacSwYellowBoundary_Type()
)
rlBrgMacSwYellowBoundary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlBrgMacSwYellowBoundary.setStatus("mandatory")
_RlBrgMacSwRedBoundary_Type = Integer32
_RlBrgMacSwRedBoundary_Object = MibScalar
rlBrgMacSwRedBoundary = _RlBrgMacSwRedBoundary_Object(
    (1, 3, 6, 1, 4, 1, 89, 50, 9),
    _RlBrgMacSwRedBoundary_Type()
)
rlBrgMacSwRedBoundary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlBrgMacSwRedBoundary.setStatus("mandatory")


class _RlBrgMacSwTrapEnable_Type(TruthValue):
    """Custom type rlBrgMacSwTrapEnable based on TruthValue"""


_RlBrgMacSwTrapEnable_Object = MibScalar
rlBrgMacSwTrapEnable = _RlBrgMacSwTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 89, 50, 10),
    _RlBrgMacSwTrapEnable_Type()
)
rlBrgMacSwTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlBrgMacSwTrapEnable.setStatus("mandatory")
_RlBrgMacSwOperTrapCount_Type = Integer32
_RlBrgMacSwOperTrapCount_Object = MibScalar
rlBrgMacSwOperTrapCount = _RlBrgMacSwOperTrapCount_Object(
    (1, 3, 6, 1, 4, 1, 89, 50, 11),
    _RlBrgMacSwOperTrapCount_Type()
)
rlBrgMacSwOperTrapCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlBrgMacSwOperTrapCount.setStatus("mandatory")


class _RlBrgMacSwAdminTrapFrequency_Type(Integer32):
    """Custom type rlBrgMacSwAdminTrapFrequency based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 86400),
    )


_RlBrgMacSwAdminTrapFrequency_Type.__name__ = "Integer32"
_RlBrgMacSwAdminTrapFrequency_Object = MibScalar
rlBrgMacSwAdminTrapFrequency = _RlBrgMacSwAdminTrapFrequency_Object(
    (1, 3, 6, 1, 4, 1, 89, 50, 12),
    _RlBrgMacSwAdminTrapFrequency_Type()
)
rlBrgMacSwAdminTrapFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlBrgMacSwAdminTrapFrequency.setStatus("mandatory")
_RlExperience_ObjectIdentity = ObjectIdentity
rlExperience = _RlExperience_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 51)
)
_RlCli_ObjectIdentity = ObjectIdentity
rlCli = _RlCli_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 52)
)
_RlCliMibVersion_Type = Integer32
_RlCliMibVersion_Object = MibScalar
rlCliMibVersion = _RlCliMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 89, 52, 1),
    _RlCliMibVersion_Type()
)
rlCliMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlCliMibVersion.setStatus("mandatory")


class _RlCliPassword_Type(DisplayString):
    """Custom type rlCliPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RlCliPassword_Type.__name__ = "DisplayString"
_RlCliPassword_Object = MibScalar
rlCliPassword = _RlCliPassword_Object(
    (1, 3, 6, 1, 4, 1, 89, 52, 2),
    _RlCliPassword_Type()
)
rlCliPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlCliPassword.setStatus("mandatory")


class _RlCliTimer_Type(Integer32):
    """Custom type rlCliTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 3600),
    )


_RlCliTimer_Type.__name__ = "Integer32"
_RlCliTimer_Object = MibScalar
rlCliTimer = _RlCliTimer_Object(
    (1, 3, 6, 1, 4, 1, 89, 52, 3),
    _RlCliTimer_Type()
)
rlCliTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlCliTimer.setStatus("mandatory")
_RlCliFileEnable_Type = TruthValue
_RlCliFileEnable_Object = MibScalar
rlCliFileEnable = _RlCliFileEnable_Object(
    (1, 3, 6, 1, 4, 1, 89, 52, 4),
    _RlCliFileEnable_Type()
)
rlCliFileEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlCliFileEnable.setStatus("mandatory")
_RlCliFileEnableAfterReset_Type = TruthValue
_RlCliFileEnableAfterReset_Object = MibScalar
rlCliFileEnableAfterReset = _RlCliFileEnableAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 52, 5),
    _RlCliFileEnableAfterReset_Type()
)
rlCliFileEnableAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlCliFileEnableAfterReset.setStatus("mandatory")
_RlPhysicalDescription_ObjectIdentity = ObjectIdentity
rlPhysicalDescription = _RlPhysicalDescription_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 53)
)
_RlIfInterfaces_ObjectIdentity = ObjectIdentity
rlIfInterfaces = _RlIfInterfaces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 54)
)
_RlMacMulticast_ObjectIdentity = ObjectIdentity
rlMacMulticast = _RlMacMulticast_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 55)
)
_RlGalileo_ObjectIdentity = ObjectIdentity
rlGalileo = _RlGalileo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 56)
)
_RlpBridgeMIBObjects_ObjectIdentity = ObjectIdentity
rlpBridgeMIBObjects = _RlpBridgeMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 57)
)
_Rldot1dPriority_ObjectIdentity = ObjectIdentity
rldot1dPriority = _Rldot1dPriority_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 57, 1)
)
_Rldot1dPriorityMibVersion_Type = Integer32
_Rldot1dPriorityMibVersion_Object = MibScalar
rldot1dPriorityMibVersion = _Rldot1dPriorityMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 89, 57, 1, 1),
    _Rldot1dPriorityMibVersion_Type()
)
rldot1dPriorityMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1dPriorityMibVersion.setStatus("mandatory")
_Rldot1dPriorityPortGroupTable_Object = MibTable
rldot1dPriorityPortGroupTable = _Rldot1dPriorityPortGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 57, 1, 2)
)
if mibBuilder.loadTexts:
    rldot1dPriorityPortGroupTable.setStatus("mandatory")
_Rldot1dPriorityPortGroupEntry_Object = MibTableRow
rldot1dPriorityPortGroupEntry = _Rldot1dPriorityPortGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 57, 1, 2, 1)
)
rldot1dPriorityPortGroupEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    rldot1dPriorityPortGroupEntry.setStatus("mandatory")
_Rldot1dPriorityPortGroupNumber_Type = Integer32
_Rldot1dPriorityPortGroupNumber_Object = MibTableColumn
rldot1dPriorityPortGroupNumber = _Rldot1dPriorityPortGroupNumber_Object(
    (1, 3, 6, 1, 4, 1, 89, 57, 1, 2, 1, 1),
    _Rldot1dPriorityPortGroupNumber_Type()
)
rldot1dPriorityPortGroupNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1dPriorityPortGroupNumber.setStatus("mandatory")
_Rldot1dStp_ObjectIdentity = ObjectIdentity
rldot1dStp = _Rldot1dStp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 57, 2)
)
_Rldot1dStpMibVersion_Type = Integer32
_Rldot1dStpMibVersion_Object = MibScalar
rldot1dStpMibVersion = _Rldot1dStpMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 89, 57, 2, 1),
    _Rldot1dStpMibVersion_Type()
)
rldot1dStpMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1dStpMibVersion.setStatus("mandatory")


class _Rldot1dStpType_Type(Integer32):
    """Custom type rldot1dStpType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4)
        )
    )
    namedValues = NamedValues(
        *(("mstp", 4),
          ("perDevice", 1))
    )


_Rldot1dStpType_Type.__name__ = "Integer32"
_Rldot1dStpType_Object = MibScalar
rldot1dStpType = _Rldot1dStpType_Object(
    (1, 3, 6, 1, 4, 1, 89, 57, 2, 2),
    _Rldot1dStpType_Type()
)
rldot1dStpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1dStpType.setStatus("mandatory")


class _Rldot1dStpEnable_Type(TruthValue):
    """Custom type rldot1dStpEnable based on TruthValue"""


_Rldot1dStpEnable_Object = MibScalar
rldot1dStpEnable = _Rldot1dStpEnable_Object(
    (1, 3, 6, 1, 4, 1, 89, 57, 2, 3),
    _Rldot1dStpEnable_Type()
)
rldot1dStpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rldot1dStpEnable.setStatus("mandatory")


class _Rldot1dStpPortMustBelongToVlan_Type(TruthValue):
    """Custom type rldot1dStpPortMustBelongToVlan based on TruthValue"""


_Rldot1dStpPortMustBelongToVlan_Object = MibScalar
rldot1dStpPortMustBelongToVlan = _Rldot1dStpPortMustBelongToVlan_Object(
    (1, 3, 6, 1, 4, 1, 89, 57, 2, 4),
    _Rldot1dStpPortMustBelongToVlan_Type()
)
rldot1dStpPortMustBelongToVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rldot1dStpPortMustBelongToVlan.setStatus("mandatory")


class _Rldot1dStpExtendedPortNumberFormat_Type(TruthValue):
    """Custom type rldot1dStpExtendedPortNumberFormat based on TruthValue"""


_Rldot1dStpExtendedPortNumberFormat_Object = MibScalar
rldot1dStpExtendedPortNumberFormat = _Rldot1dStpExtendedPortNumberFormat_Object(
    (1, 3, 6, 1, 4, 1, 89, 57, 2, 5),
    _Rldot1dStpExtendedPortNumberFormat_Type()
)
rldot1dStpExtendedPortNumberFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rldot1dStpExtendedPortNumberFormat.setStatus("mandatory")
_Rldot1dStpVlanTable_Object = MibTable
rldot1dStpVlanTable = _Rldot1dStpVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 57, 2, 6)
)
if mibBuilder.loadTexts:
    rldot1dStpVlanTable.setStatus("mandatory")
_Rldot1dStpVlanEntry_Object = MibTableRow
rldot1dStpVlanEntry = _Rldot1dStpVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 57, 2, 6, 1)
)
rldot1dStpVlanEntry.setIndexNames(
    (0, "RADLAN-MIB", "rldot1dStpVlan"),
)
if mibBuilder.loadTexts:
    rldot1dStpVlanEntry.setStatus("mandatory")
_Rldot1dStpVlan_Type = Integer32
_Rldot1dStpVlan_Object = MibTableColumn
rldot1dStpVlan = _Rldot1dStpVlan_Object(
    (1, 3, 6, 1, 4, 1, 89, 57, 2, 6, 1, 1),
    _Rldot1dStpVlan_Type()
)
rldot1dStpVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1dStpVlan.setStatus("mandatory")


class _Rldot1dStpVlanEnable_Type(TruthValue):
    """Custom type rldot1dStpVlanEnable based on TruthValue"""


_Rldot1dStpVlanEnable_Object = MibTableColumn
rldot1dStpVlanEnable = _Rldot1dStpVlanEnable_Object(
    (1, 3, 6, 1, 4, 1, 89, 57, 2, 6, 1, 2),
    _Rldot1dStpVlanEnable_Type()
)
rldot1dStpVlanEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rldot1dStpVlanEnable.setStatus("mandatory")
_Rldot1dStpTimeSinceTopologyChange_Type = TimeTicks
_Rldot1dStpTimeSinceTopologyChange_Object = MibTableColumn
rldot1dStpTimeSinceTopologyChange = _Rldot1dStpTimeSinceTopologyChange_Object(
    (1, 3, 6, 1, 4, 1, 89, 57, 2, 6, 1, 3),
    _Rldot1dStpTimeSinceTopologyChange_Type()
)
rldot1dStpTimeSinceTopologyChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1dStpTimeSinceTopologyChange.setStatus("mandatory")
_Rldot1dStpTopChanges_Type = Counter32
_Rldot1dStpTopChanges_Object = MibTableColumn
rldot1dStpTopChanges = _Rldot1dStpTopChanges_Object(
    (1, 3, 6, 1, 4, 1, 89, 57, 2, 6, 1, 4),
    _Rldot1dStpTopChanges_Type()
)
rldot1dStpTopChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1dStpTopChanges.setStatus("mandatory")
_Rldot1dStpDesignatedRoot_Type = BridgeId
_Rldot1dStpDesignatedRoot_Object = MibTableColumn
rldot1dStpDesignatedRoot = _Rldot1dStpDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 89, 57, 2, 6, 1, 5),
    _Rldot1dStpDesignatedRoot_Type()
)
rldot1dStpDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1dStpDesignatedRoot.setStatus("mandatory")
_Rldot1dStpRootCost_Type = Integer32
_Rldot1dStpRootCost_Object = MibTableColumn
rldot1dStpRootCost = _Rldot1dStpRootCost_Object(
    (1, 3, 6, 1, 4, 1, 89, 57, 2, 6, 1, 6),
    _Rldot1dStpRootCost_Type()
)
rldot1dStpRootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1dStpRootCost.setStatus("mandatory")
_Rldot1dStpRootPort_Type = Integer32
_Rldot1dStpRootPort_Object = MibTableColumn
rldot1dStpRootPort = _Rldot1dStpRootPort_Object(
    (1, 3, 6, 1, 4, 1, 89, 57, 2, 6, 1, 7),
    _Rldot1dStpRootPort_Type()
)
rldot1dStpRootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1dStpRootPort.setStatus("mandatory")
_Rldot1dStpMaxAge_Type = Timeout
_Rldot1dStpMaxAge_Object = MibTableColumn
rldot1dStpMaxAge = _Rldot1dStpMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 89, 57, 2, 6, 1, 8),
    _Rldot1dStpMaxAge_Type()
)
rldot1dStpMaxAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1dStpMaxAge.setStatus("mandatory")
_Rldot1dStpHelloTime_Type = Timeout
_Rldot1dStpHelloTime_Object = MibTableColumn
rldot1dStpHelloTime = _Rldot1dStpHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 89, 57, 2, 6, 1, 9),
    _Rldot1dStpHelloTime_Type()
)
rldot1dStpHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1dStpHelloTime.setStatus("mandatory")
_Rldot1dStpHoldTime_Type = Integer32
_Rldot1dStpHoldTime_Object = MibTableColumn
rldot1dStpHoldTime = _Rldot1dStpHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 89, 57, 2, 6, 1, 10),
    _Rldot1dStpHoldTime_Type()
)
rldot1dStpHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1dStpHoldTime.setStatus("mandatory")
_Rldot1dStpForwardDelay_Type = Timeout
_Rldot1dStpForwardDelay_Object = MibTableColumn
rldot1dStpForwardDelay = _Rldot1dStpForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 89, 57, 2, 6, 1, 11),
    _Rldot1dStpForwardDelay_Type()
)
rldot1dStpForwardDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1dStpForwardDelay.setStatus("mandatory")
_Rldot1dStpVlanPortTable_Object = MibTable
rldot1dStpVlanPortTable = _Rldot1dStpVlanPortTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 57, 2, 7)
)
if mibBuilder.loadTexts:
    rldot1dStpVlanPortTable.setStatus("mandatory")
_Rldot1dStpVlanPortEntry_Object = MibTableRow
rldot1dStpVlanPortEntry = _Rldot1dStpVlanPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 57, 2, 7, 1)
)
rldot1dStpVlanPortEntry.setIndexNames(
    (0, "RADLAN-MIB", "rldot1dStpVlanPortVlan"),
    (0, "RADLAN-MIB", "rldot1dStpVlanPortPort"),
)
if mibBuilder.loadTexts:
    rldot1dStpVlanPortEntry.setStatus("mandatory")


class _Rldot1dStpVlanPortVlan_Type(Integer32):
    """Custom type rldot1dStpVlanPortVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Rldot1dStpVlanPortVlan_Type.__name__ = "Integer32"
_Rldot1dStpVlanPortVlan_Object = MibTableColumn
rldot1dStpVlanPortVlan = _Rldot1dStpVlanPortVlan_Object(
    (1, 3, 6, 1, 4, 1, 89, 57, 2, 7, 1, 1),
    _Rldot1dStpVlanPortVlan_Type()
)
rldot1dStpVlanPortVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1dStpVlanPortVlan.setStatus("mandatory")


class _Rldot1dStpVlanPortPort_Type(Integer32):
    """Custom type rldot1dStpVlanPortPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_Rldot1dStpVlanPortPort_Type.__name__ = "Integer32"
_Rldot1dStpVlanPortPort_Object = MibTableColumn
rldot1dStpVlanPortPort = _Rldot1dStpVlanPortPort_Object(
    (1, 3, 6, 1, 4, 1, 89, 57, 2, 7, 1, 2),
    _Rldot1dStpVlanPortPort_Type()
)
rldot1dStpVlanPortPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1dStpVlanPortPort.setStatus("mandatory")


class _Rldot1dStpVlanPortPriority_Type(Integer32):
    """Custom type rldot1dStpVlanPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Rldot1dStpVlanPortPriority_Type.__name__ = "Integer32"
_Rldot1dStpVlanPortPriority_Object = MibTableColumn
rldot1dStpVlanPortPriority = _Rldot1dStpVlanPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 89, 57, 2, 7, 1, 3),
    _Rldot1dStpVlanPortPriority_Type()
)
rldot1dStpVlanPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rldot1dStpVlanPortPriority.setStatus("mandatory")


class _Rldot1dStpVlanPortState_Type(Integer32):
    """Custom type rldot1dStpVlanPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("blocking", 2),
          ("broken", 6),
          ("disabled", 1),
          ("forwarding", 5),
          ("learning", 4),
          ("listening", 3))
    )


_Rldot1dStpVlanPortState_Type.__name__ = "Integer32"
_Rldot1dStpVlanPortState_Object = MibTableColumn
rldot1dStpVlanPortState = _Rldot1dStpVlanPortState_Object(
    (1, 3, 6, 1, 4, 1, 89, 57, 2, 7, 1, 4),
    _Rldot1dStpVlanPortState_Type()
)
rldot1dStpVlanPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1dStpVlanPortState.setStatus("mandatory")


class _Rldot1dStpVlanPortEnable_Type(Integer32):
    """Custom type rldot1dStpVlanPortEnable based on Integer32"""
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


_Rldot1dStpVlanPortEnable_Type.__name__ = "Integer32"
_Rldot1dStpVlanPortEnable_Object = MibTableColumn
rldot1dStpVlanPortEnable = _Rldot1dStpVlanPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 89, 57, 2, 7, 1, 5),
    _Rldot1dStpVlanPortEnable_Type()
)
rldot1dStpVlanPortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rldot1dStpVlanPortEnable.setStatus("mandatory")


class _Rldot1dStpVlanPortPathCost_Type(Integer32):
    """Custom type rldot1dStpVlanPortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Rldot1dStpVlanPortPathCost_Type.__name__ = "Integer32"
_Rldot1dStpVlanPortPathCost_Object = MibTableColumn
rldot1dStpVlanPortPathCost = _Rldot1dStpVlanPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 89, 57, 2, 7, 1, 6),
    _Rldot1dStpVlanPortPathCost_Type()
)
rldot1dStpVlanPortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rldot1dStpVlanPortPathCost.setStatus("mandatory")
_Rldot1dStpVlanPortDesignatedRoot_Type = BridgeId
_Rldot1dStpVlanPortDesignatedRoot_Object = MibTableColumn
rldot1dStpVlanPortDesignatedRoot = _Rldot1dStpVlanPortDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 89, 57, 2, 7, 1, 7),
    _Rldot1dStpVlanPortDesignatedRoot_Type()
)
rldot1dStpVlanPortDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1dStpVlanPortDesignatedRoot.setStatus("mandatory")
_Rldot1dStpVlanPortDesignatedCost_Type = Integer32
_Rldot1dStpVlanPortDesignatedCost_Object = MibTableColumn
rldot1dStpVlanPortDesignatedCost = _Rldot1dStpVlanPortDesignatedCost_Object(
    (1, 3, 6, 1, 4, 1, 89, 57, 2, 7, 1, 8),
    _Rldot1dStpVlanPortDesignatedCost_Type()
)
rldot1dStpVlanPortDesignatedCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1dStpVlanPortDesignatedCost.setStatus("mandatory")
_Rldot1dStpVlanPortDesignatedBridge_Type = BridgeId
_Rldot1dStpVlanPortDesignatedBridge_Object = MibTableColumn
rldot1dStpVlanPortDesignatedBridge = _Rldot1dStpVlanPortDesignatedBridge_Object(
    (1, 3, 6, 1, 4, 1, 89, 57, 2, 7, 1, 9),
    _Rldot1dStpVlanPortDesignatedBridge_Type()
)
rldot1dStpVlanPortDesignatedBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1dStpVlanPortDesignatedBridge.setStatus("mandatory")


class _Rldot1dStpVlanPortDesignatedPort_Type(OctetString):
    """Custom type rldot1dStpVlanPortDesignatedPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_Rldot1dStpVlanPortDesignatedPort_Type.__name__ = "OctetString"
_Rldot1dStpVlanPortDesignatedPort_Object = MibTableColumn
rldot1dStpVlanPortDesignatedPort = _Rldot1dStpVlanPortDesignatedPort_Object(
    (1, 3, 6, 1, 4, 1, 89, 57, 2, 7, 1, 10),
    _Rldot1dStpVlanPortDesignatedPort_Type()
)
rldot1dStpVlanPortDesignatedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1dStpVlanPortDesignatedPort.setStatus("mandatory")
_Rldot1dStpVlanPortForwardTransitions_Type = Counter32
_Rldot1dStpVlanPortForwardTransitions_Object = MibTableColumn
rldot1dStpVlanPortForwardTransitions = _Rldot1dStpVlanPortForwardTransitions_Object(
    (1, 3, 6, 1, 4, 1, 89, 57, 2, 7, 1, 11),
    _Rldot1dStpVlanPortForwardTransitions_Type()
)
rldot1dStpVlanPortForwardTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1dStpVlanPortForwardTransitions.setStatus("mandatory")
_Rldot1dStpTrapVariable_ObjectIdentity = ObjectIdentity
rldot1dStpTrapVariable = _Rldot1dStpTrapVariable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 57, 2, 8)
)
_Rldot1dStpTrapVrblifIndex_Type = InterfaceIndex
_Rldot1dStpTrapVrblifIndex_Object = MibScalar
rldot1dStpTrapVrblifIndex = _Rldot1dStpTrapVrblifIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 57, 2, 8, 1),
    _Rldot1dStpTrapVrblifIndex_Type()
)
rldot1dStpTrapVrblifIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1dStpTrapVrblifIndex.setStatus("mandatory")
_Rldot1dStpTrapVrblVID_Type = Integer32
_Rldot1dStpTrapVrblVID_Object = MibScalar
rldot1dStpTrapVrblVID = _Rldot1dStpTrapVrblVID_Object(
    (1, 3, 6, 1, 4, 1, 89, 57, 2, 8, 2),
    _Rldot1dStpTrapVrblVID_Type()
)
rldot1dStpTrapVrblVID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1dStpTrapVrblVID.setStatus("mandatory")


class _Rldot1dStpTypeAfterReset_Type(Integer32):
    """Custom type rldot1dStpTypeAfterReset based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4)
        )
    )
    namedValues = NamedValues(
        *(("mstp", 4),
          ("perDevice", 1))
    )


_Rldot1dStpTypeAfterReset_Type.__name__ = "Integer32"
_Rldot1dStpTypeAfterReset_Object = MibScalar
rldot1dStpTypeAfterReset = _Rldot1dStpTypeAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 57, 2, 9),
    _Rldot1dStpTypeAfterReset_Type()
)
rldot1dStpTypeAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rldot1dStpTypeAfterReset.setStatus("mandatory")


class _Rldot1dStpMonitorTime_Type(Integer32):
    """Custom type rldot1dStpMonitorTime based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_Rldot1dStpMonitorTime_Type.__name__ = "Integer32"
_Rldot1dStpMonitorTime_Object = MibScalar
rldot1dStpMonitorTime = _Rldot1dStpMonitorTime_Object(
    (1, 3, 6, 1, 4, 1, 89, 57, 2, 10),
    _Rldot1dStpMonitorTime_Type()
)
rldot1dStpMonitorTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rldot1dStpMonitorTime.setStatus("mandatory")


class _Rldot1dStpBpduCount_Type(Integer32):
    """Custom type rldot1dStpBpduCount based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_Rldot1dStpBpduCount_Type.__name__ = "Integer32"
_Rldot1dStpBpduCount_Object = MibScalar
rldot1dStpBpduCount = _Rldot1dStpBpduCount_Object(
    (1, 3, 6, 1, 4, 1, 89, 57, 2, 11),
    _Rldot1dStpBpduCount_Type()
)
rldot1dStpBpduCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rldot1dStpBpduCount.setStatus("mandatory")
_Rldot1dStpLastChanged_Type = TimeTicks
_Rldot1dStpLastChanged_Object = MibScalar
rldot1dStpLastChanged = _Rldot1dStpLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 89, 57, 2, 12),
    _Rldot1dStpLastChanged_Type()
)
rldot1dStpLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1dStpLastChanged.setStatus("mandatory")
_Rldot1dStpPortTable_Object = MibTable
rldot1dStpPortTable = _Rldot1dStpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 57, 2, 13)
)
if mibBuilder.loadTexts:
    rldot1dStpPortTable.setStatus("mandatory")
_Rldot1dStpPortEntry_Object = MibTableRow
rldot1dStpPortEntry = _Rldot1dStpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 57, 2, 13, 1)
)
rldot1dStpPortEntry.setIndexNames(
    (0, "RADLAN-MIB", "rldot1dStpPortPort"),
)
if mibBuilder.loadTexts:
    rldot1dStpPortEntry.setStatus("mandatory")


class _Rldot1dStpPortPort_Type(Integer32):
    """Custom type rldot1dStpPortPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_Rldot1dStpPortPort_Type.__name__ = "Integer32"
_Rldot1dStpPortPort_Object = MibTableColumn
rldot1dStpPortPort = _Rldot1dStpPortPort_Object(
    (1, 3, 6, 1, 4, 1, 89, 57, 2, 13, 1, 1),
    _Rldot1dStpPortPort_Type()
)
rldot1dStpPortPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1dStpPortPort.setStatus("mandatory")


class _Rldot1dStpPortDampEnable_Type(TruthValue):
    """Custom type rldot1dStpPortDampEnable based on TruthValue"""


_Rldot1dStpPortDampEnable_Object = MibTableColumn
rldot1dStpPortDampEnable = _Rldot1dStpPortDampEnable_Object(
    (1, 3, 6, 1, 4, 1, 89, 57, 2, 13, 1, 2),
    _Rldot1dStpPortDampEnable_Type()
)
rldot1dStpPortDampEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rldot1dStpPortDampEnable.setStatus("mandatory")


class _Rldot1dStpPortDampStable_Type(TruthValue):
    """Custom type rldot1dStpPortDampStable based on TruthValue"""


_Rldot1dStpPortDampStable_Object = MibTableColumn
rldot1dStpPortDampStable = _Rldot1dStpPortDampStable_Object(
    (1, 3, 6, 1, 4, 1, 89, 57, 2, 13, 1, 3),
    _Rldot1dStpPortDampStable_Type()
)
rldot1dStpPortDampStable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1dStpPortDampStable.setStatus("mandatory")


class _Rldot1dStpPortFilterBpdu_Type(TruthValue):
    """Custom type rldot1dStpPortFilterBpdu based on TruthValue"""


_Rldot1dStpPortFilterBpdu_Object = MibTableColumn
rldot1dStpPortFilterBpdu = _Rldot1dStpPortFilterBpdu_Object(
    (1, 3, 6, 1, 4, 1, 89, 57, 2, 13, 1, 4),
    _Rldot1dStpPortFilterBpdu_Type()
)
rldot1dStpPortFilterBpdu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rldot1dStpPortFilterBpdu.setStatus("mandatory")
_Rldot1dStpPortBpduSent_Type = Counter_32
_Rldot1dStpPortBpduSent_Object = MibTableColumn
rldot1dStpPortBpduSent = _Rldot1dStpPortBpduSent_Object(
    (1, 3, 6, 1, 4, 1, 89, 57, 2, 13, 1, 5),
    _Rldot1dStpPortBpduSent_Type()
)
rldot1dStpPortBpduSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1dStpPortBpduSent.setStatus("mandatory")
_Rldot1dStpPortBpduReceived_Type = Counter_32
_Rldot1dStpPortBpduReceived_Object = MibTableColumn
rldot1dStpPortBpduReceived = _Rldot1dStpPortBpduReceived_Object(
    (1, 3, 6, 1, 4, 1, 89, 57, 2, 13, 1, 6),
    _Rldot1dStpPortBpduReceived_Type()
)
rldot1dStpPortBpduReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1dStpPortBpduReceived.setStatus("mandatory")


class _Rldot1dStpPortRole_Type(Integer32):
    """Custom type rldot1dStpPortRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("alternate", 2),
          ("backup", 3),
          ("designated", 5),
          ("disabled", 1),
          ("root", 4),
          ("unknown", 0))
    )


_Rldot1dStpPortRole_Type.__name__ = "Integer32"
_Rldot1dStpPortRole_Object = MibTableColumn
rldot1dStpPortRole = _Rldot1dStpPortRole_Object(
    (1, 3, 6, 1, 4, 1, 89, 57, 2, 13, 1, 7),
    _Rldot1dStpPortRole_Type()
)
rldot1dStpPortRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1dStpPortRole.setStatus("mandatory")


class _Rldot1dStpBpduType_Type(Integer32):
    """Custom type rldot1dStpBpduType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("rstp", 1),
          ("stp", 0))
    )


_Rldot1dStpBpduType_Type.__name__ = "Integer32"
_Rldot1dStpBpduType_Object = MibTableColumn
rldot1dStpBpduType = _Rldot1dStpBpduType_Object(
    (1, 3, 6, 1, 4, 1, 89, 57, 2, 13, 1, 8),
    _Rldot1dStpBpduType_Type()
)
rldot1dStpBpduType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1dStpBpduType.setStatus("mandatory")


class _Rldot1dStpPortRestrictedRole_Type(TruthValue):
    """Custom type rldot1dStpPortRestrictedRole based on TruthValue"""


_Rldot1dStpPortRestrictedRole_Object = MibTableColumn
rldot1dStpPortRestrictedRole = _Rldot1dStpPortRestrictedRole_Object(
    (1, 3, 6, 1, 4, 1, 89, 57, 2, 13, 1, 9),
    _Rldot1dStpPortRestrictedRole_Type()
)
rldot1dStpPortRestrictedRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rldot1dStpPortRestrictedRole.setStatus("mandatory")


class _Rldot1dStpPortAutoEdgePort_Type(TruthValue):
    """Custom type rldot1dStpPortAutoEdgePort based on TruthValue"""


_Rldot1dStpPortAutoEdgePort_Object = MibTableColumn
rldot1dStpPortAutoEdgePort = _Rldot1dStpPortAutoEdgePort_Object(
    (1, 3, 6, 1, 4, 1, 89, 57, 2, 13, 1, 10),
    _Rldot1dStpPortAutoEdgePort_Type()
)
rldot1dStpPortAutoEdgePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rldot1dStpPortAutoEdgePort.setStatus("mandatory")
_Rldot1dStpPortLoopback_Type = TruthValue
_Rldot1dStpPortLoopback_Object = MibTableColumn
rldot1dStpPortLoopback = _Rldot1dStpPortLoopback_Object(
    (1, 3, 6, 1, 4, 1, 89, 57, 2, 13, 1, 11),
    _Rldot1dStpPortLoopback_Type()
)
rldot1dStpPortLoopback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1dStpPortLoopback.setStatus("mandatory")


class _Rldot1dStpPortsEnable_Type(TruthValue):
    """Custom type rldot1dStpPortsEnable based on TruthValue"""


_Rldot1dStpPortsEnable_Object = MibScalar
rldot1dStpPortsEnable = _Rldot1dStpPortsEnable_Object(
    (1, 3, 6, 1, 4, 1, 89, 57, 2, 14),
    _Rldot1dStpPortsEnable_Type()
)
rldot1dStpPortsEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1dStpPortsEnable.setStatus("mandatory")
_Rldot1dStpTaggedFlooding_Type = TruthValue
_Rldot1dStpTaggedFlooding_Object = MibScalar
rldot1dStpTaggedFlooding = _Rldot1dStpTaggedFlooding_Object(
    (1, 3, 6, 1, 4, 1, 89, 57, 2, 15),
    _Rldot1dStpTaggedFlooding_Type()
)
rldot1dStpTaggedFlooding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1dStpTaggedFlooding.setStatus("mandatory")
_Rldot1dStpPortBelongToVlanDefault_Type = TruthValue
_Rldot1dStpPortBelongToVlanDefault_Object = MibScalar
rldot1dStpPortBelongToVlanDefault = _Rldot1dStpPortBelongToVlanDefault_Object(
    (1, 3, 6, 1, 4, 1, 89, 57, 2, 16),
    _Rldot1dStpPortBelongToVlanDefault_Type()
)
rldot1dStpPortBelongToVlanDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1dStpPortBelongToVlanDefault.setStatus("mandatory")
_Rldot1dStpEnableByDefault_Type = TruthValue
_Rldot1dStpEnableByDefault_Object = MibScalar
rldot1dStpEnableByDefault = _Rldot1dStpEnableByDefault_Object(
    (1, 3, 6, 1, 4, 1, 89, 57, 2, 17),
    _Rldot1dStpEnableByDefault_Type()
)
rldot1dStpEnableByDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1dStpEnableByDefault.setStatus("mandatory")
_Rldot1dStpPortToDefault_Type = Integer32
_Rldot1dStpPortToDefault_Object = MibScalar
rldot1dStpPortToDefault = _Rldot1dStpPortToDefault_Object(
    (1, 3, 6, 1, 4, 1, 89, 57, 2, 18),
    _Rldot1dStpPortToDefault_Type()
)
rldot1dStpPortToDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rldot1dStpPortToDefault.setStatus("mandatory")


class _Rldot1dStpSupportedType_Type(Integer32):
    """Custom type rldot1dStpSupportedType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mstp", 3),
          ("perDevice", 1),
          ("perVlan", 2))
    )


_Rldot1dStpSupportedType_Type.__name__ = "Integer32"
_Rldot1dStpSupportedType_Object = MibScalar
rldot1dStpSupportedType = _Rldot1dStpSupportedType_Object(
    (1, 3, 6, 1, 4, 1, 89, 57, 2, 19),
    _Rldot1dStpSupportedType_Type()
)
rldot1dStpSupportedType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1dStpSupportedType.setStatus("mandatory")
_Rldot1dStpEdgeportSupportInStp_Type = TruthValue
_Rldot1dStpEdgeportSupportInStp_Object = MibScalar
rldot1dStpEdgeportSupportInStp = _Rldot1dStpEdgeportSupportInStp_Object(
    (1, 3, 6, 1, 4, 1, 89, 57, 2, 20),
    _Rldot1dStpEdgeportSupportInStp_Type()
)
rldot1dStpEdgeportSupportInStp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1dStpEdgeportSupportInStp.setStatus("mandatory")
_Rldot1dStpFilterBpdu_Type = TruthValue
_Rldot1dStpFilterBpdu_Object = MibScalar
rldot1dStpFilterBpdu = _Rldot1dStpFilterBpdu_Object(
    (1, 3, 6, 1, 4, 1, 89, 57, 2, 21),
    _Rldot1dStpFilterBpdu_Type()
)
rldot1dStpFilterBpdu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rldot1dStpFilterBpdu.setStatus("mandatory")


class _Rldot1dStpFloodBpduMethod_Type(Integer32):
    """Custom type rldot1dStpFloodBpduMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("bridging", 1),
          ("classic", 0))
    )


_Rldot1dStpFloodBpduMethod_Type.__name__ = "Integer32"
_Rldot1dStpFloodBpduMethod_Object = MibScalar
rldot1dStpFloodBpduMethod = _Rldot1dStpFloodBpduMethod_Object(
    (1, 3, 6, 1, 4, 1, 89, 57, 2, 22),
    _Rldot1dStpFloodBpduMethod_Type()
)
rldot1dStpFloodBpduMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rldot1dStpFloodBpduMethod.setStatus("mandatory")
_Rldot1dStpSeparatedBridges_ObjectIdentity = ObjectIdentity
rldot1dStpSeparatedBridges = _Rldot1dStpSeparatedBridges_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 57, 2, 23)
)
_Rldot1dStpSeparatedBridgesTable_Object = MibTable
rldot1dStpSeparatedBridgesTable = _Rldot1dStpSeparatedBridgesTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 57, 2, 23, 1)
)
if mibBuilder.loadTexts:
    rldot1dStpSeparatedBridgesTable.setStatus("mandatory")
_Rldot1dStpSeparatedBridgesEntry_Object = MibTableRow
rldot1dStpSeparatedBridgesEntry = _Rldot1dStpSeparatedBridgesEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 57, 2, 23, 1, 1)
)
rldot1dStpSeparatedBridgesEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    rldot1dStpSeparatedBridgesEntry.setStatus("mandatory")


class _Rldot1dStpSeparatedBridgesPortEnable_Type(TruthValue):
    """Custom type rldot1dStpSeparatedBridgesPortEnable based on TruthValue"""


_Rldot1dStpSeparatedBridgesPortEnable_Object = MibTableColumn
rldot1dStpSeparatedBridgesPortEnable = _Rldot1dStpSeparatedBridgesPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 89, 57, 2, 23, 1, 1, 1),
    _Rldot1dStpSeparatedBridgesPortEnable_Type()
)
rldot1dStpSeparatedBridgesPortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rldot1dStpSeparatedBridgesPortEnable.setStatus("mandatory")


class _Rldot1dStpSeparatedBridgesEnable_Type(TruthValue):
    """Custom type rldot1dStpSeparatedBridgesEnable based on TruthValue"""


_Rldot1dStpSeparatedBridgesEnable_Object = MibScalar
rldot1dStpSeparatedBridgesEnable = _Rldot1dStpSeparatedBridgesEnable_Object(
    (1, 3, 6, 1, 4, 1, 89, 57, 2, 23, 2),
    _Rldot1dStpSeparatedBridgesEnable_Type()
)
rldot1dStpSeparatedBridgesEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rldot1dStpSeparatedBridgesEnable.setStatus("mandatory")


class _Rldot1dStpSeparatedBridgesAutoConfig_Type(TruthValue):
    """Custom type rldot1dStpSeparatedBridgesAutoConfig based on TruthValue"""


_Rldot1dStpSeparatedBridgesAutoConfig_Object = MibScalar
rldot1dStpSeparatedBridgesAutoConfig = _Rldot1dStpSeparatedBridgesAutoConfig_Object(
    (1, 3, 6, 1, 4, 1, 89, 57, 2, 23, 3),
    _Rldot1dStpSeparatedBridgesAutoConfig_Type()
)
rldot1dStpSeparatedBridgesAutoConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rldot1dStpSeparatedBridgesAutoConfig.setStatus("mandatory")
_Rldot1dStpPortBpduGuardTable_Object = MibTable
rldot1dStpPortBpduGuardTable = _Rldot1dStpPortBpduGuardTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 57, 2, 24)
)
if mibBuilder.loadTexts:
    rldot1dStpPortBpduGuardTable.setStatus("mandatory")
_Rldot1dStpPortBpduGuardEntry_Object = MibTableRow
rldot1dStpPortBpduGuardEntry = _Rldot1dStpPortBpduGuardEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 57, 2, 24, 1)
)
rldot1dStpPortBpduGuardEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    rldot1dStpPortBpduGuardEntry.setStatus("mandatory")


class _Rldot1dStpPortBpduGuardEnable_Type(TruthValue):
    """Custom type rldot1dStpPortBpduGuardEnable based on TruthValue"""


_Rldot1dStpPortBpduGuardEnable_Object = MibTableColumn
rldot1dStpPortBpduGuardEnable = _Rldot1dStpPortBpduGuardEnable_Object(
    (1, 3, 6, 1, 4, 1, 89, 57, 2, 24, 1, 1),
    _Rldot1dStpPortBpduGuardEnable_Type()
)
rldot1dStpPortBpduGuardEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rldot1dStpPortBpduGuardEnable.setStatus("mandatory")
_Rldot1dExtBase_ObjectIdentity = ObjectIdentity
rldot1dExtBase = _Rldot1dExtBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 57, 3)
)
_Rldot1dExtBaseMibVersion_Type = Integer32
_Rldot1dExtBaseMibVersion_Object = MibScalar
rldot1dExtBaseMibVersion = _Rldot1dExtBaseMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 89, 57, 3, 1),
    _Rldot1dExtBaseMibVersion_Type()
)
rldot1dExtBaseMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1dExtBaseMibVersion.setStatus("mandatory")


class _Rldot1dDeviceCapabilities_Type(OctetString):
    """Custom type rldot1dDeviceCapabilities based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_Rldot1dDeviceCapabilities_Type.__name__ = "OctetString"
_Rldot1dDeviceCapabilities_Object = MibScalar
rldot1dDeviceCapabilities = _Rldot1dDeviceCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 89, 57, 3, 2),
    _Rldot1dDeviceCapabilities_Type()
)
rldot1dDeviceCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1dDeviceCapabilities.setStatus("mandatory")
_Rldot1wRStp_ObjectIdentity = ObjectIdentity
rldot1wRStp = _Rldot1wRStp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 57, 4)
)
_Rldot1wRStpVlanEdgePortTable_Object = MibTable
rldot1wRStpVlanEdgePortTable = _Rldot1wRStpVlanEdgePortTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 57, 4, 1)
)
if mibBuilder.loadTexts:
    rldot1wRStpVlanEdgePortTable.setStatus("mandatory")
_Rldot1wRStpVlanEdgePortEntry_Object = MibTableRow
rldot1wRStpVlanEdgePortEntry = _Rldot1wRStpVlanEdgePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 57, 4, 1, 1)
)
rldot1wRStpVlanEdgePortEntry.setIndexNames(
    (0, "RADLAN-MIB", "rldot1wRStpVlanEdgePortVlan"),
    (0, "RADLAN-MIB", "rldot1wRStpVlanEdgePortPort"),
)
if mibBuilder.loadTexts:
    rldot1wRStpVlanEdgePortEntry.setStatus("mandatory")


class _Rldot1wRStpVlanEdgePortVlan_Type(Integer32):
    """Custom type rldot1wRStpVlanEdgePortVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Rldot1wRStpVlanEdgePortVlan_Type.__name__ = "Integer32"
_Rldot1wRStpVlanEdgePortVlan_Object = MibTableColumn
rldot1wRStpVlanEdgePortVlan = _Rldot1wRStpVlanEdgePortVlan_Object(
    (1, 3, 6, 1, 4, 1, 89, 57, 4, 1, 1, 1),
    _Rldot1wRStpVlanEdgePortVlan_Type()
)
rldot1wRStpVlanEdgePortVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1wRStpVlanEdgePortVlan.setStatus("mandatory")
_Rldot1wRStpVlanEdgePortPort_Type = Integer32
_Rldot1wRStpVlanEdgePortPort_Object = MibTableColumn
rldot1wRStpVlanEdgePortPort = _Rldot1wRStpVlanEdgePortPort_Object(
    (1, 3, 6, 1, 4, 1, 89, 57, 4, 1, 1, 2),
    _Rldot1wRStpVlanEdgePortPort_Type()
)
rldot1wRStpVlanEdgePortPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1wRStpVlanEdgePortPort.setStatus("mandatory")


class _Rldot1wRStpEdgePortStatus_Type(TruthValue):
    """Custom type rldot1wRStpEdgePortStatus based on TruthValue"""


_Rldot1wRStpEdgePortStatus_Object = MibTableColumn
rldot1wRStpEdgePortStatus = _Rldot1wRStpEdgePortStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 57, 4, 1, 1, 3),
    _Rldot1wRStpEdgePortStatus_Type()
)
rldot1wRStpEdgePortStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rldot1wRStpEdgePortStatus.setStatus("mandatory")
_Rldot1wRStpForceVersionTable_Object = MibTable
rldot1wRStpForceVersionTable = _Rldot1wRStpForceVersionTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 57, 4, 2)
)
if mibBuilder.loadTexts:
    rldot1wRStpForceVersionTable.setStatus("mandatory")
_Rldot1wRStpForceVersionEntry_Object = MibTableRow
rldot1wRStpForceVersionEntry = _Rldot1wRStpForceVersionEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 57, 4, 2, 1)
)
rldot1wRStpForceVersionEntry.setIndexNames(
    (0, "RADLAN-MIB", "rldot1wRStpForceVersionVlan"),
)
if mibBuilder.loadTexts:
    rldot1wRStpForceVersionEntry.setStatus("mandatory")


class _Rldot1wRStpForceVersionVlan_Type(Integer32):
    """Custom type rldot1wRStpForceVersionVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Rldot1wRStpForceVersionVlan_Type.__name__ = "Integer32"
_Rldot1wRStpForceVersionVlan_Object = MibTableColumn
rldot1wRStpForceVersionVlan = _Rldot1wRStpForceVersionVlan_Object(
    (1, 3, 6, 1, 4, 1, 89, 57, 4, 2, 1, 1),
    _Rldot1wRStpForceVersionVlan_Type()
)
rldot1wRStpForceVersionVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1wRStpForceVersionVlan.setStatus("mandatory")


class _Rldot1wRStpForceVersionState_Type(Integer32):
    """Custom type rldot1wRStpForceVersionState based on Integer32"""
    defaultValue = 2


_Rldot1wRStpForceVersionState_Object = MibTableColumn
rldot1wRStpForceVersionState = _Rldot1wRStpForceVersionState_Object(
    (1, 3, 6, 1, 4, 1, 89, 57, 4, 2, 1, 2),
    _Rldot1wRStpForceVersionState_Type()
)
rldot1wRStpForceVersionState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rldot1wRStpForceVersionState.setStatus("mandatory")
_Rldot1pPriorityMap_ObjectIdentity = ObjectIdentity
rldot1pPriorityMap = _Rldot1pPriorityMap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 57, 5)
)


class _Rldot1pPriorityMapState_Type(Integer32):
    """Custom type rldot1pPriorityMapState based on Integer32"""
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


_Rldot1pPriorityMapState_Type.__name__ = "Integer32"
_Rldot1pPriorityMapState_Object = MibScalar
rldot1pPriorityMapState = _Rldot1pPriorityMapState_Object(
    (1, 3, 6, 1, 4, 1, 89, 57, 5, 1),
    _Rldot1pPriorityMapState_Type()
)
rldot1pPriorityMapState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rldot1pPriorityMapState.setStatus("mandatory")
_Rldot1pPriorityMapTable_Object = MibTable
rldot1pPriorityMapTable = _Rldot1pPriorityMapTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 57, 5, 2)
)
if mibBuilder.loadTexts:
    rldot1pPriorityMapTable.setStatus("mandatory")
_Rldot1pPriorityMapEntry_Object = MibTableRow
rldot1pPriorityMapEntry = _Rldot1pPriorityMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 57, 5, 2, 1)
)
rldot1pPriorityMapEntry.setIndexNames(
    (0, "RADLAN-MIB", "rldot1pPriorityMapName"),
)
if mibBuilder.loadTexts:
    rldot1pPriorityMapEntry.setStatus("mandatory")


class _Rldot1pPriorityMapName_Type(DisplayString):
    """Custom type rldot1pPriorityMapName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 25),
    )


_Rldot1pPriorityMapName_Type.__name__ = "DisplayString"
_Rldot1pPriorityMapName_Object = MibTableColumn
rldot1pPriorityMapName = _Rldot1pPriorityMapName_Object(
    (1, 3, 6, 1, 4, 1, 89, 57, 5, 2, 1, 1),
    _Rldot1pPriorityMapName_Type()
)
rldot1pPriorityMapName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1pPriorityMapName.setStatus("mandatory")


class _Rldot1pPriorityMapPriority_Type(OctetString):
    """Custom type rldot1pPriorityMapPriority based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_Rldot1pPriorityMapPriority_Type.__name__ = "OctetString"
_Rldot1pPriorityMapPriority_Object = MibTableColumn
rldot1pPriorityMapPriority = _Rldot1pPriorityMapPriority_Object(
    (1, 3, 6, 1, 4, 1, 89, 57, 5, 2, 1, 2),
    _Rldot1pPriorityMapPriority_Type()
)
rldot1pPriorityMapPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rldot1pPriorityMapPriority.setStatus("mandatory")
_Rldot1pPriorityMapPort_Type = PortList
_Rldot1pPriorityMapPort_Object = MibTableColumn
rldot1pPriorityMapPort = _Rldot1pPriorityMapPort_Object(
    (1, 3, 6, 1, 4, 1, 89, 57, 5, 2, 1, 3),
    _Rldot1pPriorityMapPort_Type()
)
rldot1pPriorityMapPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rldot1pPriorityMapPort.setStatus("mandatory")
_Rldot1pPriorityMapPortList_Type = PortList
_Rldot1pPriorityMapPortList_Object = MibTableColumn
rldot1pPriorityMapPortList = _Rldot1pPriorityMapPortList_Object(
    (1, 3, 6, 1, 4, 1, 89, 57, 5, 2, 1, 4),
    _Rldot1pPriorityMapPortList_Type()
)
rldot1pPriorityMapPortList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1pPriorityMapPortList.setStatus("mandatory")
_Rldot1pPriorityMapStatus_Type = RowStatus
_Rldot1pPriorityMapStatus_Object = MibTableColumn
rldot1pPriorityMapStatus = _Rldot1pPriorityMapStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 57, 5, 2, 1, 5),
    _Rldot1pPriorityMapStatus_Type()
)
rldot1pPriorityMapStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rldot1pPriorityMapStatus.setStatus("mandatory")
_Rldot1sMstp_ObjectIdentity = ObjectIdentity
rldot1sMstp = _Rldot1sMstp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 57, 6)
)
_Rldot1sMstpInstanceTable_Object = MibTable
rldot1sMstpInstanceTable = _Rldot1sMstpInstanceTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 57, 6, 1)
)
if mibBuilder.loadTexts:
    rldot1sMstpInstanceTable.setStatus("mandatory")
_Rldot1sMstpInstanceEntry_Object = MibTableRow
rldot1sMstpInstanceEntry = _Rldot1sMstpInstanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 57, 6, 1, 1)
)
rldot1sMstpInstanceEntry.setIndexNames(
    (0, "RADLAN-MIB", "rldot1sMstpInstanceId"),
)
if mibBuilder.loadTexts:
    rldot1sMstpInstanceEntry.setStatus("mandatory")


class _Rldot1sMstpInstanceId_Type(Integer32):
    """Custom type rldot1sMstpInstanceId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Rldot1sMstpInstanceId_Type.__name__ = "Integer32"
_Rldot1sMstpInstanceId_Object = MibTableColumn
rldot1sMstpInstanceId = _Rldot1sMstpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 89, 57, 6, 1, 1, 1),
    _Rldot1sMstpInstanceId_Type()
)
rldot1sMstpInstanceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1sMstpInstanceId.setStatus("mandatory")
_Rldot1sMstpInstanceEnable_Type = TruthValue
_Rldot1sMstpInstanceEnable_Object = MibTableColumn
rldot1sMstpInstanceEnable = _Rldot1sMstpInstanceEnable_Object(
    (1, 3, 6, 1, 4, 1, 89, 57, 6, 1, 1, 2),
    _Rldot1sMstpInstanceEnable_Type()
)
rldot1sMstpInstanceEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1sMstpInstanceEnable.setStatus("mandatory")
_Rldot1sMstpInstanceTimeSinceTopologyChange_Type = TimeTicks
_Rldot1sMstpInstanceTimeSinceTopologyChange_Object = MibTableColumn
rldot1sMstpInstanceTimeSinceTopologyChange = _Rldot1sMstpInstanceTimeSinceTopologyChange_Object(
    (1, 3, 6, 1, 4, 1, 89, 57, 6, 1, 1, 3),
    _Rldot1sMstpInstanceTimeSinceTopologyChange_Type()
)
rldot1sMstpInstanceTimeSinceTopologyChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1sMstpInstanceTimeSinceTopologyChange.setStatus("mandatory")
_Rldot1sMstpInstanceTopChanges_Type = Counter32
_Rldot1sMstpInstanceTopChanges_Object = MibTableColumn
rldot1sMstpInstanceTopChanges = _Rldot1sMstpInstanceTopChanges_Object(
    (1, 3, 6, 1, 4, 1, 89, 57, 6, 1, 1, 4),
    _Rldot1sMstpInstanceTopChanges_Type()
)
rldot1sMstpInstanceTopChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1sMstpInstanceTopChanges.setStatus("mandatory")
_Rldot1sMstpInstanceDesignatedRoot_Type = BridgeId
_Rldot1sMstpInstanceDesignatedRoot_Object = MibTableColumn
rldot1sMstpInstanceDesignatedRoot = _Rldot1sMstpInstanceDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 89, 57, 6, 1, 1, 5),
    _Rldot1sMstpInstanceDesignatedRoot_Type()
)
rldot1sMstpInstanceDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1sMstpInstanceDesignatedRoot.setStatus("mandatory")
_Rldot1sMstpInstanceRootCost_Type = Integer32
_Rldot1sMstpInstanceRootCost_Object = MibTableColumn
rldot1sMstpInstanceRootCost = _Rldot1sMstpInstanceRootCost_Object(
    (1, 3, 6, 1, 4, 1, 89, 57, 6, 1, 1, 6),
    _Rldot1sMstpInstanceRootCost_Type()
)
rldot1sMstpInstanceRootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1sMstpInstanceRootCost.setStatus("mandatory")
_Rldot1sMstpInstanceRootPort_Type = Integer32
_Rldot1sMstpInstanceRootPort_Object = MibTableColumn
rldot1sMstpInstanceRootPort = _Rldot1sMstpInstanceRootPort_Object(
    (1, 3, 6, 1, 4, 1, 89, 57, 6, 1, 1, 7),
    _Rldot1sMstpInstanceRootPort_Type()
)
rldot1sMstpInstanceRootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1sMstpInstanceRootPort.setStatus("mandatory")
_Rldot1sMstpInstanceMaxAge_Type = Timeout
_Rldot1sMstpInstanceMaxAge_Object = MibTableColumn
rldot1sMstpInstanceMaxAge = _Rldot1sMstpInstanceMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 89, 57, 6, 1, 1, 8),
    _Rldot1sMstpInstanceMaxAge_Type()
)
rldot1sMstpInstanceMaxAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1sMstpInstanceMaxAge.setStatus("mandatory")
_Rldot1sMstpInstanceHelloTime_Type = Timeout
_Rldot1sMstpInstanceHelloTime_Object = MibTableColumn
rldot1sMstpInstanceHelloTime = _Rldot1sMstpInstanceHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 89, 57, 6, 1, 1, 9),
    _Rldot1sMstpInstanceHelloTime_Type()
)
rldot1sMstpInstanceHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1sMstpInstanceHelloTime.setStatus("mandatory")
_Rldot1sMstpInstanceHoldTime_Type = Integer32
_Rldot1sMstpInstanceHoldTime_Object = MibTableColumn
rldot1sMstpInstanceHoldTime = _Rldot1sMstpInstanceHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 89, 57, 6, 1, 1, 10),
    _Rldot1sMstpInstanceHoldTime_Type()
)
rldot1sMstpInstanceHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1sMstpInstanceHoldTime.setStatus("mandatory")
_Rldot1sMstpInstanceForwardDelay_Type = Timeout
_Rldot1sMstpInstanceForwardDelay_Object = MibTableColumn
rldot1sMstpInstanceForwardDelay = _Rldot1sMstpInstanceForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 89, 57, 6, 1, 1, 11),
    _Rldot1sMstpInstanceForwardDelay_Type()
)
rldot1sMstpInstanceForwardDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1sMstpInstanceForwardDelay.setStatus("mandatory")


class _Rldot1sMstpInstancePriority_Type(Integer32):
    """Custom type rldot1sMstpInstancePriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 61440),
    )


_Rldot1sMstpInstancePriority_Type.__name__ = "Integer32"
_Rldot1sMstpInstancePriority_Object = MibTableColumn
rldot1sMstpInstancePriority = _Rldot1sMstpInstancePriority_Object(
    (1, 3, 6, 1, 4, 1, 89, 57, 6, 1, 1, 12),
    _Rldot1sMstpInstancePriority_Type()
)
rldot1sMstpInstancePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rldot1sMstpInstancePriority.setStatus("mandatory")
_Rldot1sMstpInstanceRemainingHopes_Type = Integer32
_Rldot1sMstpInstanceRemainingHopes_Object = MibTableColumn
rldot1sMstpInstanceRemainingHopes = _Rldot1sMstpInstanceRemainingHopes_Object(
    (1, 3, 6, 1, 4, 1, 89, 57, 6, 1, 1, 13),
    _Rldot1sMstpInstanceRemainingHopes_Type()
)
rldot1sMstpInstanceRemainingHopes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1sMstpInstanceRemainingHopes.setStatus("mandatory")
_Rldot1sMstpInstancePortTable_Object = MibTable
rldot1sMstpInstancePortTable = _Rldot1sMstpInstancePortTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 57, 6, 2)
)
if mibBuilder.loadTexts:
    rldot1sMstpInstancePortTable.setStatus("mandatory")
_Rldot1sMstpInstancePortEntry_Object = MibTableRow
rldot1sMstpInstancePortEntry = _Rldot1sMstpInstancePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 57, 6, 2, 1)
)
rldot1sMstpInstancePortEntry.setIndexNames(
    (0, "RADLAN-MIB", "rldot1sMstpInstancePortMstiId"),
    (0, "RADLAN-MIB", "rldot1sMstpInstancePortPort"),
)
if mibBuilder.loadTexts:
    rldot1sMstpInstancePortEntry.setStatus("mandatory")


class _Rldot1sMstpInstancePortMstiId_Type(Integer32):
    """Custom type rldot1sMstpInstancePortMstiId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Rldot1sMstpInstancePortMstiId_Type.__name__ = "Integer32"
_Rldot1sMstpInstancePortMstiId_Object = MibTableColumn
rldot1sMstpInstancePortMstiId = _Rldot1sMstpInstancePortMstiId_Object(
    (1, 3, 6, 1, 4, 1, 89, 57, 6, 2, 1, 1),
    _Rldot1sMstpInstancePortMstiId_Type()
)
rldot1sMstpInstancePortMstiId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1sMstpInstancePortMstiId.setStatus("mandatory")


class _Rldot1sMstpInstancePortPort_Type(Integer32):
    """Custom type rldot1sMstpInstancePortPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_Rldot1sMstpInstancePortPort_Type.__name__ = "Integer32"
_Rldot1sMstpInstancePortPort_Object = MibTableColumn
rldot1sMstpInstancePortPort = _Rldot1sMstpInstancePortPort_Object(
    (1, 3, 6, 1, 4, 1, 89, 57, 6, 2, 1, 2),
    _Rldot1sMstpInstancePortPort_Type()
)
rldot1sMstpInstancePortPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1sMstpInstancePortPort.setStatus("mandatory")


class _Rldot1sMstpInstancePortPriority_Type(Integer32):
    """Custom type rldot1sMstpInstancePortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_Rldot1sMstpInstancePortPriority_Type.__name__ = "Integer32"
_Rldot1sMstpInstancePortPriority_Object = MibTableColumn
rldot1sMstpInstancePortPriority = _Rldot1sMstpInstancePortPriority_Object(
    (1, 3, 6, 1, 4, 1, 89, 57, 6, 2, 1, 3),
    _Rldot1sMstpInstancePortPriority_Type()
)
rldot1sMstpInstancePortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rldot1sMstpInstancePortPriority.setStatus("mandatory")


class _Rldot1sMstpInstancePortState_Type(Integer32):
    """Custom type rldot1sMstpInstancePortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("blocking", 2),
          ("broken", 6),
          ("disabled", 1),
          ("forwarding", 5),
          ("learning", 4),
          ("listening", 3))
    )


_Rldot1sMstpInstancePortState_Type.__name__ = "Integer32"
_Rldot1sMstpInstancePortState_Object = MibTableColumn
rldot1sMstpInstancePortState = _Rldot1sMstpInstancePortState_Object(
    (1, 3, 6, 1, 4, 1, 89, 57, 6, 2, 1, 4),
    _Rldot1sMstpInstancePortState_Type()
)
rldot1sMstpInstancePortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1sMstpInstancePortState.setStatus("mandatory")


class _Rldot1sMstpInstancePortEnable_Type(Integer32):
    """Custom type rldot1sMstpInstancePortEnable based on Integer32"""
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


_Rldot1sMstpInstancePortEnable_Type.__name__ = "Integer32"
_Rldot1sMstpInstancePortEnable_Object = MibTableColumn
rldot1sMstpInstancePortEnable = _Rldot1sMstpInstancePortEnable_Object(
    (1, 3, 6, 1, 4, 1, 89, 57, 6, 2, 1, 5),
    _Rldot1sMstpInstancePortEnable_Type()
)
rldot1sMstpInstancePortEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1sMstpInstancePortEnable.setStatus("mandatory")


class _Rldot1sMstpInstancePortPathCost_Type(Integer32):
    """Custom type rldot1sMstpInstancePortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200000000),
    )


_Rldot1sMstpInstancePortPathCost_Type.__name__ = "Integer32"
_Rldot1sMstpInstancePortPathCost_Object = MibTableColumn
rldot1sMstpInstancePortPathCost = _Rldot1sMstpInstancePortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 89, 57, 6, 2, 1, 6),
    _Rldot1sMstpInstancePortPathCost_Type()
)
rldot1sMstpInstancePortPathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1sMstpInstancePortPathCost.setStatus("mandatory")
_Rldot1sMstpInstancePortDesignatedRoot_Type = BridgeId
_Rldot1sMstpInstancePortDesignatedRoot_Object = MibTableColumn
rldot1sMstpInstancePortDesignatedRoot = _Rldot1sMstpInstancePortDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 89, 57, 6, 2, 1, 7),
    _Rldot1sMstpInstancePortDesignatedRoot_Type()
)
rldot1sMstpInstancePortDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1sMstpInstancePortDesignatedRoot.setStatus("mandatory")
_Rldot1sMstpInstancePortDesignatedCost_Type = Integer32
_Rldot1sMstpInstancePortDesignatedCost_Object = MibTableColumn
rldot1sMstpInstancePortDesignatedCost = _Rldot1sMstpInstancePortDesignatedCost_Object(
    (1, 3, 6, 1, 4, 1, 89, 57, 6, 2, 1, 8),
    _Rldot1sMstpInstancePortDesignatedCost_Type()
)
rldot1sMstpInstancePortDesignatedCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1sMstpInstancePortDesignatedCost.setStatus("mandatory")
_Rldot1sMstpInstancePortDesignatedBridge_Type = BridgeId
_Rldot1sMstpInstancePortDesignatedBridge_Object = MibTableColumn
rldot1sMstpInstancePortDesignatedBridge = _Rldot1sMstpInstancePortDesignatedBridge_Object(
    (1, 3, 6, 1, 4, 1, 89, 57, 6, 2, 1, 9),
    _Rldot1sMstpInstancePortDesignatedBridge_Type()
)
rldot1sMstpInstancePortDesignatedBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1sMstpInstancePortDesignatedBridge.setStatus("mandatory")


class _Rldot1sMstpInstancePortDesignatedPort_Type(OctetString):
    """Custom type rldot1sMstpInstancePortDesignatedPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_Rldot1sMstpInstancePortDesignatedPort_Type.__name__ = "OctetString"
_Rldot1sMstpInstancePortDesignatedPort_Object = MibTableColumn
rldot1sMstpInstancePortDesignatedPort = _Rldot1sMstpInstancePortDesignatedPort_Object(
    (1, 3, 6, 1, 4, 1, 89, 57, 6, 2, 1, 10),
    _Rldot1sMstpInstancePortDesignatedPort_Type()
)
rldot1sMstpInstancePortDesignatedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1sMstpInstancePortDesignatedPort.setStatus("mandatory")
_Rldot1sMstpInstancePortForwardTransitions_Type = Counter32
_Rldot1sMstpInstancePortForwardTransitions_Object = MibTableColumn
rldot1sMstpInstancePortForwardTransitions = _Rldot1sMstpInstancePortForwardTransitions_Object(
    (1, 3, 6, 1, 4, 1, 89, 57, 6, 2, 1, 11),
    _Rldot1sMstpInstancePortForwardTransitions_Type()
)
rldot1sMstpInstancePortForwardTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1sMstpInstancePortForwardTransitions.setStatus("mandatory")


class _Rldot1sMStpInstancePortAdminPathCost_Type(Integer32):
    """Custom type rldot1sMStpInstancePortAdminPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Rldot1sMStpInstancePortAdminPathCost_Type.__name__ = "Integer32"
_Rldot1sMStpInstancePortAdminPathCost_Object = MibTableColumn
rldot1sMStpInstancePortAdminPathCost = _Rldot1sMStpInstancePortAdminPathCost_Object(
    (1, 3, 6, 1, 4, 1, 89, 57, 6, 2, 1, 12),
    _Rldot1sMStpInstancePortAdminPathCost_Type()
)
rldot1sMStpInstancePortAdminPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rldot1sMStpInstancePortAdminPathCost.setStatus("mandatory")


class _Rldot1sMStpInstancePortRole_Type(Integer32):
    """Custom type rldot1sMStpInstancePortRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("alternate", 2),
          ("backup", 3),
          ("designated", 5),
          ("disabled", 1),
          ("master", 6),
          ("root", 4),
          ("unknown", 0))
    )


_Rldot1sMStpInstancePortRole_Type.__name__ = "Integer32"
_Rldot1sMStpInstancePortRole_Object = MibTableColumn
rldot1sMStpInstancePortRole = _Rldot1sMStpInstancePortRole_Object(
    (1, 3, 6, 1, 4, 1, 89, 57, 6, 2, 1, 13),
    _Rldot1sMStpInstancePortRole_Type()
)
rldot1sMStpInstancePortRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1sMStpInstancePortRole.setStatus("mandatory")


class _Rldot1sMstpMaxHopes_Type(Integer32):
    """Custom type rldot1sMstpMaxHopes based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 40),
    )


_Rldot1sMstpMaxHopes_Type.__name__ = "Integer32"
_Rldot1sMstpMaxHopes_Object = MibScalar
rldot1sMstpMaxHopes = _Rldot1sMstpMaxHopes_Object(
    (1, 3, 6, 1, 4, 1, 89, 57, 6, 3),
    _Rldot1sMstpMaxHopes_Type()
)
rldot1sMstpMaxHopes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rldot1sMstpMaxHopes.setStatus("mandatory")
_Rldot1sMstpConfigurationName_Type = SnmpAdminString
_Rldot1sMstpConfigurationName_Object = MibScalar
rldot1sMstpConfigurationName = _Rldot1sMstpConfigurationName_Object(
    (1, 3, 6, 1, 4, 1, 89, 57, 6, 4),
    _Rldot1sMstpConfigurationName_Type()
)
rldot1sMstpConfigurationName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1sMstpConfigurationName.setStatus("mandatory")


class _Rldot1sMstpRevisionLevel_Type(Integer32):
    """Custom type rldot1sMstpRevisionLevel based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rldot1sMstpRevisionLevel_Type.__name__ = "Integer32"
_Rldot1sMstpRevisionLevel_Object = MibScalar
rldot1sMstpRevisionLevel = _Rldot1sMstpRevisionLevel_Object(
    (1, 3, 6, 1, 4, 1, 89, 57, 6, 5),
    _Rldot1sMstpRevisionLevel_Type()
)
rldot1sMstpRevisionLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1sMstpRevisionLevel.setStatus("mandatory")
_Rldot1sMstpVlanTable_Object = MibTable
rldot1sMstpVlanTable = _Rldot1sMstpVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 57, 6, 6)
)
if mibBuilder.loadTexts:
    rldot1sMstpVlanTable.setStatus("mandatory")
_Rldot1sMstpVlanEntry_Object = MibTableRow
rldot1sMstpVlanEntry = _Rldot1sMstpVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 57, 6, 6, 1)
)
rldot1sMstpVlanEntry.setIndexNames(
    (0, "RADLAN-MIB", "rldot1sMstpVlan"),
)
if mibBuilder.loadTexts:
    rldot1sMstpVlanEntry.setStatus("mandatory")


class _Rldot1sMstpVlan_Type(Integer32):
    """Custom type rldot1sMstpVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Rldot1sMstpVlan_Type.__name__ = "Integer32"
_Rldot1sMstpVlan_Object = MibTableColumn
rldot1sMstpVlan = _Rldot1sMstpVlan_Object(
    (1, 3, 6, 1, 4, 1, 89, 57, 6, 6, 1, 1),
    _Rldot1sMstpVlan_Type()
)
rldot1sMstpVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1sMstpVlan.setStatus("mandatory")


class _Rldot1sMstpGroup_Type(Integer32):
    """Custom type rldot1sMstpGroup based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_Rldot1sMstpGroup_Type.__name__ = "Integer32"
_Rldot1sMstpGroup_Object = MibTableColumn
rldot1sMstpGroup = _Rldot1sMstpGroup_Object(
    (1, 3, 6, 1, 4, 1, 89, 57, 6, 6, 1, 2),
    _Rldot1sMstpGroup_Type()
)
rldot1sMstpGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1sMstpGroup.setStatus("mandatory")


class _Rldot1sMstpPendingGroup_Type(Integer32):
    """Custom type rldot1sMstpPendingGroup based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_Rldot1sMstpPendingGroup_Type.__name__ = "Integer32"
_Rldot1sMstpPendingGroup_Object = MibTableColumn
rldot1sMstpPendingGroup = _Rldot1sMstpPendingGroup_Object(
    (1, 3, 6, 1, 4, 1, 89, 57, 6, 6, 1, 3),
    _Rldot1sMstpPendingGroup_Type()
)
rldot1sMstpPendingGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rldot1sMstpPendingGroup.setStatus("mandatory")
_Rldot1sMstpExtPortTable_Object = MibTable
rldot1sMstpExtPortTable = _Rldot1sMstpExtPortTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 57, 6, 7)
)
if mibBuilder.loadTexts:
    rldot1sMstpExtPortTable.setStatus("mandatory")
_Rldot1sMstpExtPortEntry_Object = MibTableRow
rldot1sMstpExtPortEntry = _Rldot1sMstpExtPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 57, 6, 7, 1)
)
rldot1sMstpExtPortEntry.setIndexNames(
    (0, "RADLAN-MIB", "rldot1sMstpExtPortPort"),
)
if mibBuilder.loadTexts:
    rldot1sMstpExtPortEntry.setStatus("mandatory")


class _Rldot1sMstpExtPortPort_Type(Integer32):
    """Custom type rldot1sMstpExtPortPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_Rldot1sMstpExtPortPort_Type.__name__ = "Integer32"
_Rldot1sMstpExtPortPort_Object = MibTableColumn
rldot1sMstpExtPortPort = _Rldot1sMstpExtPortPort_Object(
    (1, 3, 6, 1, 4, 1, 89, 57, 6, 7, 1, 1),
    _Rldot1sMstpExtPortPort_Type()
)
rldot1sMstpExtPortPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1sMstpExtPortPort.setStatus("mandatory")


class _Rldot1sMstpExtPortInternalOperPathCost_Type(Integer32):
    """Custom type rldot1sMstpExtPortInternalOperPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200000000),
    )


_Rldot1sMstpExtPortInternalOperPathCost_Type.__name__ = "Integer32"
_Rldot1sMstpExtPortInternalOperPathCost_Object = MibTableColumn
rldot1sMstpExtPortInternalOperPathCost = _Rldot1sMstpExtPortInternalOperPathCost_Object(
    (1, 3, 6, 1, 4, 1, 89, 57, 6, 7, 1, 2),
    _Rldot1sMstpExtPortInternalOperPathCost_Type()
)
rldot1sMstpExtPortInternalOperPathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1sMstpExtPortInternalOperPathCost.setStatus("mandatory")
_Rldot1sMstpExtPortDesignatedRegionalRoot_Type = BridgeId
_Rldot1sMstpExtPortDesignatedRegionalRoot_Object = MibTableColumn
rldot1sMstpExtPortDesignatedRegionalRoot = _Rldot1sMstpExtPortDesignatedRegionalRoot_Object(
    (1, 3, 6, 1, 4, 1, 89, 57, 6, 7, 1, 3),
    _Rldot1sMstpExtPortDesignatedRegionalRoot_Type()
)
rldot1sMstpExtPortDesignatedRegionalRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1sMstpExtPortDesignatedRegionalRoot.setStatus("mandatory")
_Rldot1sMstpExtPortDesignatedRegionalCost_Type = Integer32
_Rldot1sMstpExtPortDesignatedRegionalCost_Object = MibTableColumn
rldot1sMstpExtPortDesignatedRegionalCost = _Rldot1sMstpExtPortDesignatedRegionalCost_Object(
    (1, 3, 6, 1, 4, 1, 89, 57, 6, 7, 1, 4),
    _Rldot1sMstpExtPortDesignatedRegionalCost_Type()
)
rldot1sMstpExtPortDesignatedRegionalCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1sMstpExtPortDesignatedRegionalCost.setStatus("mandatory")
_Rldot1sMstpExtPortBoundary_Type = TruthValue
_Rldot1sMstpExtPortBoundary_Object = MibTableColumn
rldot1sMstpExtPortBoundary = _Rldot1sMstpExtPortBoundary_Object(
    (1, 3, 6, 1, 4, 1, 89, 57, 6, 7, 1, 5),
    _Rldot1sMstpExtPortBoundary_Type()
)
rldot1sMstpExtPortBoundary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1sMstpExtPortBoundary.setStatus("mandatory")


class _Rldot1sMstpExtPortInternalAdminPathCost_Type(Integer32):
    """Custom type rldot1sMstpExtPortInternalAdminPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Rldot1sMstpExtPortInternalAdminPathCost_Type.__name__ = "Integer32"
_Rldot1sMstpExtPortInternalAdminPathCost_Object = MibTableColumn
rldot1sMstpExtPortInternalAdminPathCost = _Rldot1sMstpExtPortInternalAdminPathCost_Object(
    (1, 3, 6, 1, 4, 1, 89, 57, 6, 7, 1, 6),
    _Rldot1sMstpExtPortInternalAdminPathCost_Type()
)
rldot1sMstpExtPortInternalAdminPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rldot1sMstpExtPortInternalAdminPathCost.setStatus("mandatory")


class _Rldot1sMstpDesignatedMaxHopes_Type(Integer32):
    """Custom type rldot1sMstpDesignatedMaxHopes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 40),
    )


_Rldot1sMstpDesignatedMaxHopes_Type.__name__ = "Integer32"
_Rldot1sMstpDesignatedMaxHopes_Object = MibScalar
rldot1sMstpDesignatedMaxHopes = _Rldot1sMstpDesignatedMaxHopes_Object(
    (1, 3, 6, 1, 4, 1, 89, 57, 6, 8),
    _Rldot1sMstpDesignatedMaxHopes_Type()
)
rldot1sMstpDesignatedMaxHopes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1sMstpDesignatedMaxHopes.setStatus("mandatory")
_Rldot1sMstpRegionalRoot_Type = BridgeId
_Rldot1sMstpRegionalRoot_Object = MibScalar
rldot1sMstpRegionalRoot = _Rldot1sMstpRegionalRoot_Object(
    (1, 3, 6, 1, 4, 1, 89, 57, 6, 9),
    _Rldot1sMstpRegionalRoot_Type()
)
rldot1sMstpRegionalRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1sMstpRegionalRoot.setStatus("mandatory")
_Rldot1sMstpRegionalRootCost_Type = Integer32
_Rldot1sMstpRegionalRootCost_Object = MibScalar
rldot1sMstpRegionalRootCost = _Rldot1sMstpRegionalRootCost_Object(
    (1, 3, 6, 1, 4, 1, 89, 57, 6, 10),
    _Rldot1sMstpRegionalRootCost_Type()
)
rldot1sMstpRegionalRootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1sMstpRegionalRootCost.setStatus("mandatory")


class _Rldot1sMstpPendingConfigurationName_Type(SnmpAdminString):
    """Custom type rldot1sMstpPendingConfigurationName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Rldot1sMstpPendingConfigurationName_Type.__name__ = "SnmpAdminString"
_Rldot1sMstpPendingConfigurationName_Object = MibScalar
rldot1sMstpPendingConfigurationName = _Rldot1sMstpPendingConfigurationName_Object(
    (1, 3, 6, 1, 4, 1, 89, 57, 6, 11),
    _Rldot1sMstpPendingConfigurationName_Type()
)
rldot1sMstpPendingConfigurationName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rldot1sMstpPendingConfigurationName.setStatus("mandatory")


class _Rldot1sMstpPendingRevisionLevel_Type(Integer32):
    """Custom type rldot1sMstpPendingRevisionLevel based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rldot1sMstpPendingRevisionLevel_Type.__name__ = "Integer32"
_Rldot1sMstpPendingRevisionLevel_Object = MibScalar
rldot1sMstpPendingRevisionLevel = _Rldot1sMstpPendingRevisionLevel_Object(
    (1, 3, 6, 1, 4, 1, 89, 57, 6, 12),
    _Rldot1sMstpPendingRevisionLevel_Type()
)
rldot1sMstpPendingRevisionLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rldot1sMstpPendingRevisionLevel.setStatus("mandatory")


class _Rldot1sMstpPendingAction_Type(Integer32):
    """Custom type rldot1sMstpPendingAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("copyActivePending", 2),
          ("copyPendingActive", 1))
    )


_Rldot1sMstpPendingAction_Type.__name__ = "Integer32"
_Rldot1sMstpPendingAction_Object = MibScalar
rldot1sMstpPendingAction = _Rldot1sMstpPendingAction_Object(
    (1, 3, 6, 1, 4, 1, 89, 57, 6, 13),
    _Rldot1sMstpPendingAction_Type()
)
rldot1sMstpPendingAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rldot1sMstpPendingAction.setStatus("mandatory")
_Rldot1sMstpRemainingHops_Type = Integer32
_Rldot1sMstpRemainingHops_Object = MibScalar
rldot1sMstpRemainingHops = _Rldot1sMstpRemainingHops_Object(
    (1, 3, 6, 1, 4, 1, 89, 57, 6, 14),
    _Rldot1sMstpRemainingHops_Type()
)
rldot1sMstpRemainingHops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1sMstpRemainingHops.setStatus("mandatory")
_Rldot1dTpAgingTime_ObjectIdentity = ObjectIdentity
rldot1dTpAgingTime = _Rldot1dTpAgingTime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 57, 7)
)
_Rldot1dTpAgingTimeMin_Type = Integer32
_Rldot1dTpAgingTimeMin_Object = MibScalar
rldot1dTpAgingTimeMin = _Rldot1dTpAgingTimeMin_Object(
    (1, 3, 6, 1, 4, 1, 89, 57, 7, 1),
    _Rldot1dTpAgingTimeMin_Type()
)
rldot1dTpAgingTimeMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1dTpAgingTimeMin.setStatus("mandatory")
_Rldot1dTpAgingTimeMax_Type = Integer32
_Rldot1dTpAgingTimeMax_Object = MibScalar
rldot1dTpAgingTimeMax = _Rldot1dTpAgingTimeMax_Object(
    (1, 3, 6, 1, 4, 1, 89, 57, 7, 2),
    _Rldot1dTpAgingTimeMax_Type()
)
rldot1dTpAgingTimeMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1dTpAgingTimeMax.setStatus("mandatory")
_RlTelnet_ObjectIdentity = ObjectIdentity
rlTelnet = _RlTelnet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 58)
)
_RlTelnetMibVersion_Type = Integer32
_RlTelnetMibVersion_Object = MibScalar
rlTelnetMibVersion = _RlTelnetMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 89, 58, 1),
    _RlTelnetMibVersion_Type()
)
rlTelnetMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlTelnetMibVersion.setStatus("mandatory")


class _RlTelnetPassword_Type(DisplayString):
    """Custom type rlTelnetPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RlTelnetPassword_Type.__name__ = "DisplayString"
_RlTelnetPassword_Object = MibScalar
rlTelnetPassword = _RlTelnetPassword_Object(
    (1, 3, 6, 1, 4, 1, 89, 58, 2),
    _RlTelnetPassword_Type()
)
rlTelnetPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlTelnetPassword.setStatus("mandatory")


class _RlTelnetTimeout_Type(Integer32):
    """Custom type rlTelnetTimeout based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RlTelnetTimeout_Type.__name__ = "Integer32"
_RlTelnetTimeout_Object = MibScalar
rlTelnetTimeout = _RlTelnetTimeout_Object(
    (1, 3, 6, 1, 4, 1, 89, 58, 3),
    _RlTelnetTimeout_Type()
)
rlTelnetTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlTelnetTimeout.setStatus("mandatory")
_RlTelnetUsersTable_Object = MibTable
rlTelnetUsersTable = _RlTelnetUsersTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 58, 4)
)
if mibBuilder.loadTexts:
    rlTelnetUsersTable.setStatus("mandatory")
_RlTelnetUsersEntry_Object = MibTableRow
rlTelnetUsersEntry = _RlTelnetUsersEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 58, 4, 1)
)
rlTelnetUsersEntry.setIndexNames(
    (0, "RADLAN-MIB", "rlTelnetSessionId"),
)
if mibBuilder.loadTexts:
    rlTelnetUsersEntry.setStatus("mandatory")
_RlTelnetSessionId_Type = Integer32
_RlTelnetSessionId_Object = MibTableColumn
rlTelnetSessionId = _RlTelnetSessionId_Object(
    (1, 3, 6, 1, 4, 1, 89, 58, 4, 1, 1),
    _RlTelnetSessionId_Type()
)
rlTelnetSessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlTelnetSessionId.setStatus("mandatory")
_RlTelnetSessionClientAddress_Type = IpAddress
_RlTelnetSessionClientAddress_Object = MibTableColumn
rlTelnetSessionClientAddress = _RlTelnetSessionClientAddress_Object(
    (1, 3, 6, 1, 4, 1, 89, 58, 4, 1, 2),
    _RlTelnetSessionClientAddress_Type()
)
rlTelnetSessionClientAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlTelnetSessionClientAddress.setStatus("mandatory")
_RlTelnetSessionLoginTime_Type = DisplayString
_RlTelnetSessionLoginTime_Object = MibTableColumn
rlTelnetSessionLoginTime = _RlTelnetSessionLoginTime_Object(
    (1, 3, 6, 1, 4, 1, 89, 58, 4, 1, 3),
    _RlTelnetSessionLoginTime_Type()
)
rlTelnetSessionLoginTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlTelnetSessionLoginTime.setStatus("mandatory")


class _RlTelnetSessionStatus_Type(Integer32):
    """Custom type rlTelnetSessionStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("connected", 1),
          ("disconnect", 2))
    )


_RlTelnetSessionStatus_Type.__name__ = "Integer32"
_RlTelnetSessionStatus_Object = MibTableColumn
rlTelnetSessionStatus = _RlTelnetSessionStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 58, 4, 1, 4),
    _RlTelnetSessionStatus_Type()
)
rlTelnetSessionStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlTelnetSessionStatus.setStatus("mandatory")
_RlTelnetLoginBanner_Type = DisplayString
_RlTelnetLoginBanner_Object = MibScalar
rlTelnetLoginBanner = _RlTelnetLoginBanner_Object(
    (1, 3, 6, 1, 4, 1, 89, 58, 5),
    _RlTelnetLoginBanner_Type()
)
rlTelnetLoginBanner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlTelnetLoginBanner.setStatus("mandatory")
_RlTelnetSecondLoginBanner_Type = DisplayString
_RlTelnetSecondLoginBanner_Object = MibScalar
rlTelnetSecondLoginBanner = _RlTelnetSecondLoginBanner_Object(
    (1, 3, 6, 1, 4, 1, 89, 58, 6),
    _RlTelnetSecondLoginBanner_Type()
)
rlTelnetSecondLoginBanner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlTelnetSecondLoginBanner.setStatus("mandatory")
_RlPolicy_ObjectIdentity = ObjectIdentity
rlPolicy = _RlPolicy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 59)
)
_RlArpSpoofing_ObjectIdentity = ObjectIdentity
rlArpSpoofing = _RlArpSpoofing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 60)
)
_RlArpSpoofingMibVersion_Type = Integer32
_RlArpSpoofingMibVersion_Object = MibScalar
rlArpSpoofingMibVersion = _RlArpSpoofingMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 89, 60, 1),
    _RlArpSpoofingMibVersion_Type()
)
rlArpSpoofingMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlArpSpoofingMibVersion.setStatus("mandatory")
_RlArpSpoofingTable_Object = MibTable
rlArpSpoofingTable = _RlArpSpoofingTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 60, 2)
)
if mibBuilder.loadTexts:
    rlArpSpoofingTable.setStatus("mandatory")
_RlArpSpoofingEntry_Object = MibTableRow
rlArpSpoofingEntry = _RlArpSpoofingEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 60, 2, 1)
)
rlArpSpoofingEntry.setIndexNames(
    (0, "RADLAN-MIB", "rlArpSpoofingIfIndex"),
    (0, "RADLAN-MIB", "rlArpSpoofingLocalIpAddr"),
)
if mibBuilder.loadTexts:
    rlArpSpoofingEntry.setStatus("mandatory")
_RlArpSpoofingIfIndex_Type = InterfaceIndex
_RlArpSpoofingIfIndex_Object = MibTableColumn
rlArpSpoofingIfIndex = _RlArpSpoofingIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 60, 2, 1, 1),
    _RlArpSpoofingIfIndex_Type()
)
rlArpSpoofingIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlArpSpoofingIfIndex.setStatus("mandatory")
_RlArpSpoofingLocalIpAddr_Type = IpAddress
_RlArpSpoofingLocalIpAddr_Object = MibTableColumn
rlArpSpoofingLocalIpAddr = _RlArpSpoofingLocalIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 60, 2, 1, 2),
    _RlArpSpoofingLocalIpAddr_Type()
)
rlArpSpoofingLocalIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlArpSpoofingLocalIpAddr.setStatus("mandatory")
_RlArpSpoofingMacAddr_Type = PhysAddress
_RlArpSpoofingMacAddr_Object = MibTableColumn
rlArpSpoofingMacAddr = _RlArpSpoofingMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 60, 2, 1, 3),
    _RlArpSpoofingMacAddr_Type()
)
rlArpSpoofingMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlArpSpoofingMacAddr.setStatus("mandatory")
_RlArpSpoofingRemoteIpAddr_Type = IpAddress
_RlArpSpoofingRemoteIpAddr_Object = MibTableColumn
rlArpSpoofingRemoteIpAddr = _RlArpSpoofingRemoteIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 60, 2, 1, 4),
    _RlArpSpoofingRemoteIpAddr_Type()
)
rlArpSpoofingRemoteIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlArpSpoofingRemoteIpAddr.setStatus("mandatory")


class _RlArpSpoofingOutPhysIfIndex_Type(InterfaceIndexOrZero):
    """Custom type rlArpSpoofingOutPhysIfIndex based on InterfaceIndexOrZero"""
    defaultValue = 0


_RlArpSpoofingOutPhysIfIndex_Object = MibTableColumn
rlArpSpoofingOutPhysIfIndex = _RlArpSpoofingOutPhysIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 60, 2, 1, 5),
    _RlArpSpoofingOutPhysIfIndex_Type()
)
rlArpSpoofingOutPhysIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlArpSpoofingOutPhysIfIndex.setStatus("mandatory")
_RlArpSpoofingStatus_Type = RowStatus
_RlArpSpoofingStatus_Object = MibTableColumn
rlArpSpoofingStatus = _RlArpSpoofingStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 60, 2, 1, 6),
    _RlArpSpoofingStatus_Type()
)
rlArpSpoofingStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlArpSpoofingStatus.setStatus("mandatory")
_RlMir_ObjectIdentity = ObjectIdentity
rlMir = _RlMir_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 61)
)
_RlMirMibVersion_Type = Integer32
_RlMirMibVersion_Object = MibScalar
rlMirMibVersion = _RlMirMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 89, 61, 1),
    _RlMirMibVersion_Type()
)
rlMirMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlMirMibVersion.setStatus("mandatory")


class _RlMirMaxNumOfMRIsAfterReset_Type(Integer32):
    """Custom type rlMirMaxNumOfMRIsAfterReset based on Integer32"""
    defaultValue = 1


_RlMirMaxNumOfMRIsAfterReset_Object = MibScalar
rlMirMaxNumOfMRIsAfterReset = _RlMirMaxNumOfMRIsAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 61, 2),
    _RlMirMaxNumOfMRIsAfterReset_Type()
)
rlMirMaxNumOfMRIsAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlMirMaxNumOfMRIsAfterReset.setStatus("mandatory")
_RlMirMaxNumOfMRIs_Type = Integer32
_RlMirMaxNumOfMRIs_Object = MibScalar
rlMirMaxNumOfMRIs = _RlMirMaxNumOfMRIs_Object(
    (1, 3, 6, 1, 4, 1, 89, 61, 3),
    _RlMirMaxNumOfMRIs_Type()
)
rlMirMaxNumOfMRIs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlMirMaxNumOfMRIs.setStatus("mandatory")
_RlMirCurMriNum_Type = Integer32
_RlMirCurMriNum_Object = MibScalar
rlMirCurMriNum = _RlMirCurMriNum_Object(
    (1, 3, 6, 1, 4, 1, 89, 61, 4),
    _RlMirCurMriNum_Type()
)
rlMirCurMriNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlMirCurMriNum.setStatus("mandatory")
_RlMirInterfaceTable_Object = MibTable
rlMirInterfaceTable = _RlMirInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 61, 5)
)
if mibBuilder.loadTexts:
    rlMirInterfaceTable.setStatus("mandatory")
_RlMirInterfaceEntry_Object = MibTableRow
rlMirInterfaceEntry = _RlMirInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 61, 5, 1)
)
rlMirInterfaceEntry.setIndexNames(
    (0, "RADLAN-MIB", "rlMirInterfaceIfIndex"),
)
if mibBuilder.loadTexts:
    rlMirInterfaceEntry.setStatus("mandatory")
_RlMirInterfaceIfIndex_Type = InterfaceIndex
_RlMirInterfaceIfIndex_Object = MibTableColumn
rlMirInterfaceIfIndex = _RlMirInterfaceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 61, 5, 1, 1),
    _RlMirInterfaceIfIndex_Type()
)
rlMirInterfaceIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlMirInterfaceIfIndex.setStatus("mandatory")


class _RlMirInterfaceMrid_Type(Integer32):
    """Custom type rlMirInterfaceMrid based on Integer32"""
    defaultValue = 0


_RlMirInterfaceMrid_Object = MibTableColumn
rlMirInterfaceMrid = _RlMirInterfaceMrid_Object(
    (1, 3, 6, 1, 4, 1, 89, 61, 5, 1, 2),
    _RlMirInterfaceMrid_Type()
)
rlMirInterfaceMrid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlMirInterfaceMrid.setStatus("mandatory")
_RlMirVlanBaseReservedPortsTable_Object = MibTable
rlMirVlanBaseReservedPortsTable = _RlMirVlanBaseReservedPortsTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 61, 6)
)
if mibBuilder.loadTexts:
    rlMirVlanBaseReservedPortsTable.setStatus("mandatory")
_RlMirVlanBaseReservedPortsEntry_Object = MibTableRow
rlMirVlanBaseReservedPortsEntry = _RlMirVlanBaseReservedPortsEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 61, 6, 1)
)
rlMirVlanBaseReservedPortsEntry.setIndexNames(
    (0, "RADLAN-MIB", "rlMirVlanBaseReservedPortsIfIndex"),
)
if mibBuilder.loadTexts:
    rlMirVlanBaseReservedPortsEntry.setStatus("mandatory")
_RlMirVlanBaseReservedPortsIfIndex_Type = InterfaceIndex
_RlMirVlanBaseReservedPortsIfIndex_Object = MibTableColumn
rlMirVlanBaseReservedPortsIfIndex = _RlMirVlanBaseReservedPortsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 61, 6, 1, 1),
    _RlMirVlanBaseReservedPortsIfIndex_Type()
)
rlMirVlanBaseReservedPortsIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlMirVlanBaseReservedPortsIfIndex.setStatus("mandatory")
_RlMirVlanBaseReservedPortsStatus_Type = RowStatus
_RlMirVlanBaseReservedPortsStatus_Object = MibTableColumn
rlMirVlanBaseReservedPortsStatus = _RlMirVlanBaseReservedPortsStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 61, 6, 1, 2),
    _RlMirVlanBaseReservedPortsStatus_Type()
)
rlMirVlanBaseReservedPortsStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlMirVlanBaseReservedPortsStatus.setStatus("mandatory")
_RlMirVlanBaseLogicalPortsTable_Object = MibTable
rlMirVlanBaseLogicalPortsTable = _RlMirVlanBaseLogicalPortsTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 61, 7)
)
if mibBuilder.loadTexts:
    rlMirVlanBaseLogicalPortsTable.setStatus("mandatory")
_RlMirVlanBaseLogicalPortsEntry_Object = MibTableRow
rlMirVlanBaseLogicalPortsEntry = _RlMirVlanBaseLogicalPortsEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 61, 7, 1)
)
rlMirVlanBaseLogicalPortsEntry.setIndexNames(
    (0, "RADLAN-MIB", "rlMirVlanBaseLogicalPortsIfIndex"),
)
if mibBuilder.loadTexts:
    rlMirVlanBaseLogicalPortsEntry.setStatus("mandatory")
_RlMirVlanBaseLogicalPortsIfIndex_Type = InterfaceIndex
_RlMirVlanBaseLogicalPortsIfIndex_Object = MibTableColumn
rlMirVlanBaseLogicalPortsIfIndex = _RlMirVlanBaseLogicalPortsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 61, 7, 1, 1),
    _RlMirVlanBaseLogicalPortsIfIndex_Type()
)
rlMirVlanBaseLogicalPortsIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlMirVlanBaseLogicalPortsIfIndex.setStatus("mandatory")
_RlMirVlanBaseLogicalPortsReservedIfIndex_Type = InterfaceIndex
_RlMirVlanBaseLogicalPortsReservedIfIndex_Object = MibTableColumn
rlMirVlanBaseLogicalPortsReservedIfIndex = _RlMirVlanBaseLogicalPortsReservedIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 61, 7, 1, 2),
    _RlMirVlanBaseLogicalPortsReservedIfIndex_Type()
)
rlMirVlanBaseLogicalPortsReservedIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlMirVlanBaseLogicalPortsReservedIfIndex.setStatus("mandatory")


class _RlMirVlanBaseLogicalPortsVlanTag_Type(Integer32):
    """Custom type rlMirVlanBaseLogicalPortsVlanTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_RlMirVlanBaseLogicalPortsVlanTag_Type.__name__ = "Integer32"
_RlMirVlanBaseLogicalPortsVlanTag_Object = MibTableColumn
rlMirVlanBaseLogicalPortsVlanTag = _RlMirVlanBaseLogicalPortsVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 89, 61, 7, 1, 3),
    _RlMirVlanBaseLogicalPortsVlanTag_Type()
)
rlMirVlanBaseLogicalPortsVlanTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlMirVlanBaseLogicalPortsVlanTag.setStatus("mandatory")
_RlMirVlanBaseLogicalPortsStatus_Type = RowStatus
_RlMirVlanBaseLogicalPortsStatus_Object = MibTableColumn
rlMirVlanBaseLogicalPortsStatus = _RlMirVlanBaseLogicalPortsStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 61, 7, 1, 4),
    _RlMirVlanBaseLogicalPortsStatus_Type()
)
rlMirVlanBaseLogicalPortsStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlMirVlanBaseLogicalPortsStatus.setStatus("mandatory")
_RlIpMRouteStdMIB_ObjectIdentity = ObjectIdentity
rlIpMRouteStdMIB = _RlIpMRouteStdMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 62)
)
_Rl3sw2swTables_ObjectIdentity = ObjectIdentity
rl3sw2swTables = _Rl3sw2swTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 63)
)


class _Rl3sw2swTablesPollingInterval_Type(Integer32):
    """Custom type rl3sw2swTablesPollingInterval based on Integer32"""
    defaultValue = 3


_Rl3sw2swTablesPollingInterval_Object = MibScalar
rl3sw2swTablesPollingInterval = _Rl3sw2swTablesPollingInterval_Object(
    (1, 3, 6, 1, 4, 1, 89, 63, 1),
    _Rl3sw2swTablesPollingInterval_Type()
)
rl3sw2swTablesPollingInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rl3sw2swTablesPollingInterval.setStatus("mandatory")
_RlGvrp_ObjectIdentity = ObjectIdentity
rlGvrp = _RlGvrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 64)
)
_RlPortGvrpTimersTable_Object = MibTable
rlPortGvrpTimersTable = _RlPortGvrpTimersTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 64, 1)
)
if mibBuilder.loadTexts:
    rlPortGvrpTimersTable.setStatus("mandatory")
_RlPortGvrpTimersEntry_Object = MibTableRow
rlPortGvrpTimersEntry = _RlPortGvrpTimersEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 64, 1, 1)
)
rlPortGvrpTimersEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    rlPortGvrpTimersEntry.setStatus("mandatory")


class _RlPortGvrpJoinTime_Type(TimeInterval):
    """Custom type rlPortGvrpJoinTime based on TimeInterval"""
    defaultValue = 20


_RlPortGvrpJoinTime_Object = MibTableColumn
rlPortGvrpJoinTime = _RlPortGvrpJoinTime_Object(
    (1, 3, 6, 1, 4, 1, 89, 64, 1, 1, 1),
    _RlPortGvrpJoinTime_Type()
)
rlPortGvrpJoinTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPortGvrpJoinTime.setStatus("mandatory")


class _RlPortGvrpLeaveTime_Type(TimeInterval):
    """Custom type rlPortGvrpLeaveTime based on TimeInterval"""
    defaultValue = 60


_RlPortGvrpLeaveTime_Object = MibTableColumn
rlPortGvrpLeaveTime = _RlPortGvrpLeaveTime_Object(
    (1, 3, 6, 1, 4, 1, 89, 64, 1, 1, 2),
    _RlPortGvrpLeaveTime_Type()
)
rlPortGvrpLeaveTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPortGvrpLeaveTime.setStatus("mandatory")


class _RlPortGvrpLeaveAllTime_Type(TimeInterval):
    """Custom type rlPortGvrpLeaveAllTime based on TimeInterval"""
    defaultValue = 1000


_RlPortGvrpLeaveAllTime_Object = MibTableColumn
rlPortGvrpLeaveAllTime = _RlPortGvrpLeaveAllTime_Object(
    (1, 3, 6, 1, 4, 1, 89, 64, 1, 1, 3),
    _RlPortGvrpLeaveAllTime_Type()
)
rlPortGvrpLeaveAllTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPortGvrpLeaveAllTime.setStatus("mandatory")


class _RlPortGvrpOverrideGarp_Type(EnabledStatus):
    """Custom type rlPortGvrpOverrideGarp based on EnabledStatus"""


_RlPortGvrpOverrideGarp_Object = MibTableColumn
rlPortGvrpOverrideGarp = _RlPortGvrpOverrideGarp_Object(
    (1, 3, 6, 1, 4, 1, 89, 64, 1, 1, 4),
    _RlPortGvrpOverrideGarp_Type()
)
rlPortGvrpOverrideGarp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPortGvrpOverrideGarp.setStatus("mandatory")
_RlGvrpSupported_Type = TruthValue
_RlGvrpSupported_Object = MibScalar
rlGvrpSupported = _RlGvrpSupported_Object(
    (1, 3, 6, 1, 4, 1, 89, 64, 2),
    _RlGvrpSupported_Type()
)
rlGvrpSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlGvrpSupported.setStatus("mandatory")
_RlGvrpMibVersion_Type = Integer32
_RlGvrpMibVersion_Object = MibScalar
rlGvrpMibVersion = _RlGvrpMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 89, 64, 3),
    _RlGvrpMibVersion_Type()
)
rlGvrpMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlGvrpMibVersion.setStatus("mandatory")
_RlPortGvrpStatisticsTable_Object = MibTable
rlPortGvrpStatisticsTable = _RlPortGvrpStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 64, 4)
)
if mibBuilder.loadTexts:
    rlPortGvrpStatisticsTable.setStatus("mandatory")
_RlPortGvrpStatisticsEntry_Object = MibTableRow
rlPortGvrpStatisticsEntry = _RlPortGvrpStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 64, 4, 1)
)
rlPortGvrpStatisticsEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    rlPortGvrpStatisticsEntry.setStatus("mandatory")
_RlPortGvrpStatisticsRJE_Type = Counter32
_RlPortGvrpStatisticsRJE_Object = MibTableColumn
rlPortGvrpStatisticsRJE = _RlPortGvrpStatisticsRJE_Object(
    (1, 3, 6, 1, 4, 1, 89, 64, 4, 1, 1),
    _RlPortGvrpStatisticsRJE_Type()
)
rlPortGvrpStatisticsRJE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPortGvrpStatisticsRJE.setStatus("mandatory")
_RlPortGvrpStatisticsRJIn_Type = Counter32
_RlPortGvrpStatisticsRJIn_Object = MibTableColumn
rlPortGvrpStatisticsRJIn = _RlPortGvrpStatisticsRJIn_Object(
    (1, 3, 6, 1, 4, 1, 89, 64, 4, 1, 2),
    _RlPortGvrpStatisticsRJIn_Type()
)
rlPortGvrpStatisticsRJIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPortGvrpStatisticsRJIn.setStatus("mandatory")
_RlPortGvrpStatisticsREmp_Type = Counter32
_RlPortGvrpStatisticsREmp_Object = MibTableColumn
rlPortGvrpStatisticsREmp = _RlPortGvrpStatisticsREmp_Object(
    (1, 3, 6, 1, 4, 1, 89, 64, 4, 1, 3),
    _RlPortGvrpStatisticsREmp_Type()
)
rlPortGvrpStatisticsREmp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPortGvrpStatisticsREmp.setStatus("mandatory")
_RlPortGvrpStatisticsRLIn_Type = Counter32
_RlPortGvrpStatisticsRLIn_Object = MibTableColumn
rlPortGvrpStatisticsRLIn = _RlPortGvrpStatisticsRLIn_Object(
    (1, 3, 6, 1, 4, 1, 89, 64, 4, 1, 4),
    _RlPortGvrpStatisticsRLIn_Type()
)
rlPortGvrpStatisticsRLIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPortGvrpStatisticsRLIn.setStatus("mandatory")
_RlPortGvrpStatisticsRLE_Type = Counter32
_RlPortGvrpStatisticsRLE_Object = MibTableColumn
rlPortGvrpStatisticsRLE = _RlPortGvrpStatisticsRLE_Object(
    (1, 3, 6, 1, 4, 1, 89, 64, 4, 1, 5),
    _RlPortGvrpStatisticsRLE_Type()
)
rlPortGvrpStatisticsRLE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPortGvrpStatisticsRLE.setStatus("mandatory")
_RlPortGvrpStatisticsRLA_Type = Counter32
_RlPortGvrpStatisticsRLA_Object = MibTableColumn
rlPortGvrpStatisticsRLA = _RlPortGvrpStatisticsRLA_Object(
    (1, 3, 6, 1, 4, 1, 89, 64, 4, 1, 6),
    _RlPortGvrpStatisticsRLA_Type()
)
rlPortGvrpStatisticsRLA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPortGvrpStatisticsRLA.setStatus("mandatory")
_RlPortGvrpStatisticsSJE_Type = Counter32
_RlPortGvrpStatisticsSJE_Object = MibTableColumn
rlPortGvrpStatisticsSJE = _RlPortGvrpStatisticsSJE_Object(
    (1, 3, 6, 1, 4, 1, 89, 64, 4, 1, 7),
    _RlPortGvrpStatisticsSJE_Type()
)
rlPortGvrpStatisticsSJE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPortGvrpStatisticsSJE.setStatus("mandatory")
_RlPortGvrpStatisticsSJIn_Type = Counter32
_RlPortGvrpStatisticsSJIn_Object = MibTableColumn
rlPortGvrpStatisticsSJIn = _RlPortGvrpStatisticsSJIn_Object(
    (1, 3, 6, 1, 4, 1, 89, 64, 4, 1, 8),
    _RlPortGvrpStatisticsSJIn_Type()
)
rlPortGvrpStatisticsSJIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPortGvrpStatisticsSJIn.setStatus("mandatory")
_RlPortGvrpStatisticsSEmp_Type = Counter32
_RlPortGvrpStatisticsSEmp_Object = MibTableColumn
rlPortGvrpStatisticsSEmp = _RlPortGvrpStatisticsSEmp_Object(
    (1, 3, 6, 1, 4, 1, 89, 64, 4, 1, 9),
    _RlPortGvrpStatisticsSEmp_Type()
)
rlPortGvrpStatisticsSEmp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPortGvrpStatisticsSEmp.setStatus("mandatory")
_RlPortGvrpStatisticsSLIn_Type = Counter32
_RlPortGvrpStatisticsSLIn_Object = MibTableColumn
rlPortGvrpStatisticsSLIn = _RlPortGvrpStatisticsSLIn_Object(
    (1, 3, 6, 1, 4, 1, 89, 64, 4, 1, 10),
    _RlPortGvrpStatisticsSLIn_Type()
)
rlPortGvrpStatisticsSLIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPortGvrpStatisticsSLIn.setStatus("mandatory")
_RlPortGvrpStatisticsSLE_Type = Counter32
_RlPortGvrpStatisticsSLE_Object = MibTableColumn
rlPortGvrpStatisticsSLE = _RlPortGvrpStatisticsSLE_Object(
    (1, 3, 6, 1, 4, 1, 89, 64, 4, 1, 11),
    _RlPortGvrpStatisticsSLE_Type()
)
rlPortGvrpStatisticsSLE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPortGvrpStatisticsSLE.setStatus("mandatory")
_RlPortGvrpStatisticsSLA_Type = Counter32
_RlPortGvrpStatisticsSLA_Object = MibTableColumn
rlPortGvrpStatisticsSLA = _RlPortGvrpStatisticsSLA_Object(
    (1, 3, 6, 1, 4, 1, 89, 64, 4, 1, 12),
    _RlPortGvrpStatisticsSLA_Type()
)
rlPortGvrpStatisticsSLA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPortGvrpStatisticsSLA.setStatus("mandatory")


class _RlPortGvrpStatisticsClear_Type(Integer32):
    """Custom type rlPortGvrpStatisticsClear based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("activate", 1),
          ("passive", 2))
    )


_RlPortGvrpStatisticsClear_Type.__name__ = "Integer32"
_RlPortGvrpStatisticsClear_Object = MibTableColumn
rlPortGvrpStatisticsClear = _RlPortGvrpStatisticsClear_Object(
    (1, 3, 6, 1, 4, 1, 89, 64, 4, 1, 13),
    _RlPortGvrpStatisticsClear_Type()
)
rlPortGvrpStatisticsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPortGvrpStatisticsClear.setStatus("mandatory")
_RlPortGvrpErrorStatisticsTable_Object = MibTable
rlPortGvrpErrorStatisticsTable = _RlPortGvrpErrorStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 64, 5)
)
if mibBuilder.loadTexts:
    rlPortGvrpErrorStatisticsTable.setStatus("mandatory")
_RlPortGvrpErrorStatisticsEntry_Object = MibTableRow
rlPortGvrpErrorStatisticsEntry = _RlPortGvrpErrorStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 64, 5, 1)
)
rlPortGvrpErrorStatisticsEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    rlPortGvrpErrorStatisticsEntry.setStatus("mandatory")
_RlPortGvrpErrorStatisticsInvProt_Type = Counter32
_RlPortGvrpErrorStatisticsInvProt_Object = MibTableColumn
rlPortGvrpErrorStatisticsInvProt = _RlPortGvrpErrorStatisticsInvProt_Object(
    (1, 3, 6, 1, 4, 1, 89, 64, 5, 1, 1),
    _RlPortGvrpErrorStatisticsInvProt_Type()
)
rlPortGvrpErrorStatisticsInvProt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPortGvrpErrorStatisticsInvProt.setStatus("mandatory")
_RlPortGvrpErrorStatisticsInvAtyp_Type = Counter32
_RlPortGvrpErrorStatisticsInvAtyp_Object = MibTableColumn
rlPortGvrpErrorStatisticsInvAtyp = _RlPortGvrpErrorStatisticsInvAtyp_Object(
    (1, 3, 6, 1, 4, 1, 89, 64, 5, 1, 2),
    _RlPortGvrpErrorStatisticsInvAtyp_Type()
)
rlPortGvrpErrorStatisticsInvAtyp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPortGvrpErrorStatisticsInvAtyp.setStatus("mandatory")
_RlPortGvrpErrorStatisticsInvAval_Type = Counter32
_RlPortGvrpErrorStatisticsInvAval_Object = MibTableColumn
rlPortGvrpErrorStatisticsInvAval = _RlPortGvrpErrorStatisticsInvAval_Object(
    (1, 3, 6, 1, 4, 1, 89, 64, 5, 1, 3),
    _RlPortGvrpErrorStatisticsInvAval_Type()
)
rlPortGvrpErrorStatisticsInvAval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPortGvrpErrorStatisticsInvAval.setStatus("mandatory")
_RlPortGvrpErrorStatisticsInvPlen_Type = Counter32
_RlPortGvrpErrorStatisticsInvPlen_Object = MibTableColumn
rlPortGvrpErrorStatisticsInvPlen = _RlPortGvrpErrorStatisticsInvPlen_Object(
    (1, 3, 6, 1, 4, 1, 89, 64, 5, 1, 4),
    _RlPortGvrpErrorStatisticsInvPlen_Type()
)
rlPortGvrpErrorStatisticsInvPlen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPortGvrpErrorStatisticsInvPlen.setStatus("mandatory")
_RlPortGvrpErrorStatisticsInvAlen_Type = Counter32
_RlPortGvrpErrorStatisticsInvAlen_Object = MibTableColumn
rlPortGvrpErrorStatisticsInvAlen = _RlPortGvrpErrorStatisticsInvAlen_Object(
    (1, 3, 6, 1, 4, 1, 89, 64, 5, 1, 5),
    _RlPortGvrpErrorStatisticsInvAlen_Type()
)
rlPortGvrpErrorStatisticsInvAlen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPortGvrpErrorStatisticsInvAlen.setStatus("mandatory")
_RlPortGvrpErrorStatisticsInvEvent_Type = Counter32
_RlPortGvrpErrorStatisticsInvEvent_Object = MibTableColumn
rlPortGvrpErrorStatisticsInvEvent = _RlPortGvrpErrorStatisticsInvEvent_Object(
    (1, 3, 6, 1, 4, 1, 89, 64, 5, 1, 6),
    _RlPortGvrpErrorStatisticsInvEvent_Type()
)
rlPortGvrpErrorStatisticsInvEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPortGvrpErrorStatisticsInvEvent.setStatus("mandatory")


class _RlPortGvrpErrorStatisticsClear_Type(Integer32):
    """Custom type rlPortGvrpErrorStatisticsClear based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("activate", 1),
          ("passive", 2))
    )


_RlPortGvrpErrorStatisticsClear_Type.__name__ = "Integer32"
_RlPortGvrpErrorStatisticsClear_Object = MibTableColumn
rlPortGvrpErrorStatisticsClear = _RlPortGvrpErrorStatisticsClear_Object(
    (1, 3, 6, 1, 4, 1, 89, 64, 5, 1, 7),
    _RlPortGvrpErrorStatisticsClear_Type()
)
rlPortGvrpErrorStatisticsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPortGvrpErrorStatisticsClear.setStatus("mandatory")
_RlPortGvrpApplicantStatusTable_Object = MibTable
rlPortGvrpApplicantStatusTable = _RlPortGvrpApplicantStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 64, 6)
)
if mibBuilder.loadTexts:
    rlPortGvrpApplicantStatusTable.setStatus("mandatory")
_RlPortGvrpApplicantStatusEntry_Object = MibTableRow
rlPortGvrpApplicantStatusEntry = _RlPortGvrpApplicantStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 64, 6, 1)
)
rlPortGvrpApplicantStatusEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    rlPortGvrpApplicantStatusEntry.setStatus("mandatory")


class _RlPortGvrpApplicantStatusValue_Type(Integer32):
    """Custom type rlPortGvrpApplicantStatusValue based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nonParticipant", 2),
          ("participant", 1))
    )


_RlPortGvrpApplicantStatusValue_Type.__name__ = "Integer32"
_RlPortGvrpApplicantStatusValue_Object = MibTableColumn
rlPortGvrpApplicantStatusValue = _RlPortGvrpApplicantStatusValue_Object(
    (1, 3, 6, 1, 4, 1, 89, 64, 6, 1, 1),
    _RlPortGvrpApplicantStatusValue_Type()
)
rlPortGvrpApplicantStatusValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPortGvrpApplicantStatusValue.setStatus("mandatory")
_RlPortGvrpRegistrationModeTable_Object = MibTable
rlPortGvrpRegistrationModeTable = _RlPortGvrpRegistrationModeTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 64, 8)
)
if mibBuilder.loadTexts:
    rlPortGvrpRegistrationModeTable.setStatus("mandatory")
_RlPortGvrpRegistrationModeEntry_Object = MibTableRow
rlPortGvrpRegistrationModeEntry = _RlPortGvrpRegistrationModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 64, 8, 1)
)
rlPortGvrpRegistrationModeEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    rlPortGvrpRegistrationModeEntry.setStatus("mandatory")


class _RlPortGvrpRegistrationModeForbidden_Type(TruthValue):
    """Custom type rlPortGvrpRegistrationModeForbidden based on TruthValue"""


_RlPortGvrpRegistrationModeForbidden_Object = MibTableColumn
rlPortGvrpRegistrationModeForbidden = _RlPortGvrpRegistrationModeForbidden_Object(
    (1, 3, 6, 1, 4, 1, 89, 64, 8, 1, 1),
    _RlPortGvrpRegistrationModeForbidden_Type()
)
rlPortGvrpRegistrationModeForbidden.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPortGvrpRegistrationModeForbidden.setStatus("mandatory")
_RlDot3adAgg_ObjectIdentity = ObjectIdentity
rlDot3adAgg = _RlDot3adAgg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 65)
)
_RlEmbWeb_ObjectIdentity = ObjectIdentity
rlEmbWeb = _RlEmbWeb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 66)
)
_RlSwPackageVersion_ObjectIdentity = ObjectIdentity
rlSwPackageVersion = _RlSwPackageVersion_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 67)
)
_RlSwPackageVersionTable_Object = MibTable
rlSwPackageVersionTable = _RlSwPackageVersionTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 67, 1)
)
if mibBuilder.loadTexts:
    rlSwPackageVersionTable.setStatus("mandatory")
_RlSwPackageVersionEntry_Object = MibTableRow
rlSwPackageVersionEntry = _RlSwPackageVersionEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 67, 1, 1)
)
rlSwPackageVersionEntry.setIndexNames(
    (1, "RADLAN-MIB", "rlSwPackageVersionName"),
)
if mibBuilder.loadTexts:
    rlSwPackageVersionEntry.setStatus("mandatory")


class _RlSwPackageVersionName_Type(DisplayString):
    """Custom type rlSwPackageVersionName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_RlSwPackageVersionName_Type.__name__ = "DisplayString"
_RlSwPackageVersionName_Object = MibTableColumn
rlSwPackageVersionName = _RlSwPackageVersionName_Object(
    (1, 3, 6, 1, 4, 1, 89, 67, 1, 1, 1),
    _RlSwPackageVersionName_Type()
)
rlSwPackageVersionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSwPackageVersionName.setStatus("mandatory")


class _RlSwPackageVersionVesrion_Type(DisplayString):
    """Custom type rlSwPackageVersionVesrion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_RlSwPackageVersionVesrion_Type.__name__ = "DisplayString"
_RlSwPackageVersionVesrion_Object = MibTableColumn
rlSwPackageVersionVesrion = _RlSwPackageVersionVesrion_Object(
    (1, 3, 6, 1, 4, 1, 89, 67, 1, 1, 2),
    _RlSwPackageVersionVesrion_Type()
)
rlSwPackageVersionVesrion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSwPackageVersionVesrion.setStatus("mandatory")
_RlBroadcom_ObjectIdentity = ObjectIdentity
rlBroadcom = _RlBroadcom_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 68)
)
_RlMultiSessionTerminal_ObjectIdentity = ObjectIdentity
rlMultiSessionTerminal = _RlMultiSessionTerminal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 69)
)


class _RlTerminalDebugModePassword_Type(DisplayString):
    """Custom type rlTerminalDebugModePassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RlTerminalDebugModePassword_Type.__name__ = "DisplayString"
_RlTerminalDebugModePassword_Object = MibScalar
rlTerminalDebugModePassword = _RlTerminalDebugModePassword_Object(
    (1, 3, 6, 1, 4, 1, 89, 69, 1),
    _RlTerminalDebugModePassword_Type()
)
rlTerminalDebugModePassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlTerminalDebugModePassword.setStatus("mandatory")
_RlRCli_ObjectIdentity = ObjectIdentity
rlRCli = _RlRCli_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 70)
)
_RlRCliMibVersion_Type = Integer32
_RlRCliMibVersion_Object = MibScalar
rlRCliMibVersion = _RlRCliMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 89, 70, 1),
    _RlRCliMibVersion_Type()
)
rlRCliMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlRCliMibVersion.setStatus("mandatory")


class _RlRCliUserPassword_Type(OctetString):
    """Custom type rlRCliUserPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RlRCliUserPassword_Type.__name__ = "OctetString"
_RlRCliUserPassword_Object = MibScalar
rlRCliUserPassword = _RlRCliUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 89, 70, 2),
    _RlRCliUserPassword_Type()
)
rlRCliUserPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlRCliUserPassword.setStatus("mandatory")


class _RlRCliEnablePassword_Type(OctetString):
    """Custom type rlRCliEnablePassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RlRCliEnablePassword_Type.__name__ = "OctetString"
_RlRCliEnablePassword_Object = MibScalar
rlRCliEnablePassword = _RlRCliEnablePassword_Object(
    (1, 3, 6, 1, 4, 1, 89, 70, 3),
    _RlRCliEnablePassword_Type()
)
rlRCliEnablePassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlRCliEnablePassword.setStatus("mandatory")


class _RlRCliConfigPassword_Type(OctetString):
    """Custom type rlRCliConfigPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RlRCliConfigPassword_Type.__name__ = "OctetString"
_RlRCliConfigPassword_Object = MibScalar
rlRCliConfigPassword = _RlRCliConfigPassword_Object(
    (1, 3, 6, 1, 4, 1, 89, 70, 4),
    _RlRCliConfigPassword_Type()
)
rlRCliConfigPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlRCliConfigPassword.setStatus("mandatory")


class _RlRCliTimer_Type(Integer32):
    """Custom type rlRCliTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 3600),
    )


_RlRCliTimer_Type.__name__ = "Integer32"
_RlRCliTimer_Object = MibScalar
rlRCliTimer = _RlRCliTimer_Object(
    (1, 3, 6, 1, 4, 1, 89, 70, 5),
    _RlRCliTimer_Type()
)
rlRCliTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlRCliTimer.setStatus("mandatory")


class _RlRcliFileAction_Type(Integer32):
    """Custom type rlRcliFileAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notUsedAfterReset", 1),
          ("usedAfterReset", 2))
    )


_RlRcliFileAction_Type.__name__ = "Integer32"
_RlRcliFileAction_Object = MibScalar
rlRcliFileAction = _RlRcliFileAction_Object(
    (1, 3, 6, 1, 4, 1, 89, 70, 6),
    _RlRcliFileAction_Type()
)
rlRcliFileAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlRcliFileAction.setStatus("mandatory")
_RlBgp_ObjectIdentity = ObjectIdentity
rlBgp = _RlBgp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 71)
)
_RlAgentsCapabilitiesGroups_ObjectIdentity = ObjectIdentity
rlAgentsCapabilitiesGroups = _RlAgentsCapabilitiesGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 72)
)
_RlAggregateVlan_ObjectIdentity = ObjectIdentity
rlAggregateVlan = _RlAggregateVlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 73)
)
_RlAggregateVlanMibVersion_Type = Integer32
_RlAggregateVlanMibVersion_Object = MibScalar
rlAggregateVlanMibVersion = _RlAggregateVlanMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 89, 73, 1),
    _RlAggregateVlanMibVersion_Type()
)
rlAggregateVlanMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlAggregateVlanMibVersion.setStatus("mandatory")
_RlAggregateVlanTable_Object = MibTable
rlAggregateVlanTable = _RlAggregateVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 73, 2)
)
if mibBuilder.loadTexts:
    rlAggregateVlanTable.setStatus("mandatory")
_RlAggregateVlanEntry_Object = MibTableRow
rlAggregateVlanEntry = _RlAggregateVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 73, 2, 1)
)
rlAggregateVlanEntry.setIndexNames(
    (0, "RADLAN-MIB", "rlAggregateVlanIndex"),
)
if mibBuilder.loadTexts:
    rlAggregateVlanEntry.setStatus("mandatory")
_RlAggregateVlanIndex_Type = InterfaceIndex
_RlAggregateVlanIndex_Object = MibTableColumn
rlAggregateVlanIndex = _RlAggregateVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 73, 2, 1, 1),
    _RlAggregateVlanIndex_Type()
)
rlAggregateVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlAggregateVlanIndex.setStatus("mandatory")


class _RlAggregateVlanName_Type(DisplayString):
    """Custom type rlAggregateVlanName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RlAggregateVlanName_Type.__name__ = "DisplayString"
_RlAggregateVlanName_Object = MibTableColumn
rlAggregateVlanName = _RlAggregateVlanName_Object(
    (1, 3, 6, 1, 4, 1, 89, 73, 2, 1, 2),
    _RlAggregateVlanName_Type()
)
rlAggregateVlanName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlAggregateVlanName.setStatus("mandatory")


class _RlAggregateVlanPhysAddressType_Type(Integer32):
    """Custom type rlAggregateVlanPhysAddressType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("reserve", 2))
    )


_RlAggregateVlanPhysAddressType_Type.__name__ = "Integer32"
_RlAggregateVlanPhysAddressType_Object = MibTableColumn
rlAggregateVlanPhysAddressType = _RlAggregateVlanPhysAddressType_Object(
    (1, 3, 6, 1, 4, 1, 89, 73, 2, 1, 3),
    _RlAggregateVlanPhysAddressType_Type()
)
rlAggregateVlanPhysAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlAggregateVlanPhysAddressType.setStatus("mandatory")
_RlAggregateVlanStatus_Type = RowStatus
_RlAggregateVlanStatus_Object = MibTableColumn
rlAggregateVlanStatus = _RlAggregateVlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 73, 2, 1, 4),
    _RlAggregateVlanStatus_Type()
)
rlAggregateVlanStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlAggregateVlanStatus.setStatus("mandatory")
_RlAggregateSubVlanTable_Object = MibTable
rlAggregateSubVlanTable = _RlAggregateSubVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 73, 3)
)
if mibBuilder.loadTexts:
    rlAggregateSubVlanTable.setStatus("mandatory")
_RlAggregateSubVlanEntry_Object = MibTableRow
rlAggregateSubVlanEntry = _RlAggregateSubVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 73, 3, 1)
)
rlAggregateSubVlanEntry.setIndexNames(
    (0, "RADLAN-MIB", "rlAggregateVlanIndex"),
    (0, "RADLAN-MIB", "rlAggregateSubVlanIfIndex"),
)
if mibBuilder.loadTexts:
    rlAggregateSubVlanEntry.setStatus("mandatory")
_RlAggregateSubVlanIfIndex_Type = InterfaceIndex
_RlAggregateSubVlanIfIndex_Object = MibTableColumn
rlAggregateSubVlanIfIndex = _RlAggregateSubVlanIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 73, 3, 1, 1),
    _RlAggregateSubVlanIfIndex_Type()
)
rlAggregateSubVlanIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlAggregateSubVlanIfIndex.setStatus("mandatory")
_RlAggregateSubVlanStatus_Type = RowStatus
_RlAggregateSubVlanStatus_Object = MibTableColumn
rlAggregateSubVlanStatus = _RlAggregateSubVlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 73, 3, 1, 2),
    _RlAggregateSubVlanStatus_Type()
)
rlAggregateSubVlanStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlAggregateSubVlanStatus.setStatus("mandatory")


class _RlAggregateVlanArpProxy_Type(Integer32):
    """Custom type rlAggregateVlanArpProxy based on Integer32"""
    defaultValue = 2

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


_RlAggregateVlanArpProxy_Type.__name__ = "Integer32"
_RlAggregateVlanArpProxy_Object = MibScalar
rlAggregateVlanArpProxy = _RlAggregateVlanArpProxy_Object(
    (1, 3, 6, 1, 4, 1, 89, 73, 4),
    _RlAggregateVlanArpProxy_Type()
)
rlAggregateVlanArpProxy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlAggregateVlanArpProxy.setStatus("mandatory")
_RlGmrp_ObjectIdentity = ObjectIdentity
rlGmrp = _RlGmrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 75)
)
_RlGmrpSupported_Type = TruthValue
_RlGmrpSupported_Object = MibScalar
rlGmrpSupported = _RlGmrpSupported_Object(
    (1, 3, 6, 1, 4, 1, 89, 75, 1),
    _RlGmrpSupported_Type()
)
rlGmrpSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlGmrpSupported.setStatus("mandatory")
_RlGmrpMibVersion_Type = Integer32
_RlGmrpMibVersion_Object = MibScalar
rlGmrpMibVersion = _RlGmrpMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 89, 75, 2),
    _RlGmrpMibVersion_Type()
)
rlGmrpMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlGmrpMibVersion.setStatus("mandatory")
_RlPortGmrpTimersTable_Object = MibTable
rlPortGmrpTimersTable = _RlPortGmrpTimersTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 75, 3)
)
if mibBuilder.loadTexts:
    rlPortGmrpTimersTable.setStatus("mandatory")
_RlPortGmrpTimersEntry_Object = MibTableRow
rlPortGmrpTimersEntry = _RlPortGmrpTimersEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 75, 3, 1)
)
rlPortGmrpTimersEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    rlPortGmrpTimersEntry.setStatus("mandatory")


class _RlPortGmrpJoinTime_Type(TimeInterval):
    """Custom type rlPortGmrpJoinTime based on TimeInterval"""
    defaultValue = 20


_RlPortGmrpJoinTime_Object = MibTableColumn
rlPortGmrpJoinTime = _RlPortGmrpJoinTime_Object(
    (1, 3, 6, 1, 4, 1, 89, 75, 3, 1, 1),
    _RlPortGmrpJoinTime_Type()
)
rlPortGmrpJoinTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPortGmrpJoinTime.setStatus("mandatory")


class _RlPortGmrpLeaveTime_Type(TimeInterval):
    """Custom type rlPortGmrpLeaveTime based on TimeInterval"""
    defaultValue = 60


_RlPortGmrpLeaveTime_Object = MibTableColumn
rlPortGmrpLeaveTime = _RlPortGmrpLeaveTime_Object(
    (1, 3, 6, 1, 4, 1, 89, 75, 3, 1, 2),
    _RlPortGmrpLeaveTime_Type()
)
rlPortGmrpLeaveTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPortGmrpLeaveTime.setStatus("mandatory")


class _RlPortGmrpLeaveAllTime_Type(TimeInterval):
    """Custom type rlPortGmrpLeaveAllTime based on TimeInterval"""
    defaultValue = 1000


_RlPortGmrpLeaveAllTime_Object = MibTableColumn
rlPortGmrpLeaveAllTime = _RlPortGmrpLeaveAllTime_Object(
    (1, 3, 6, 1, 4, 1, 89, 75, 3, 1, 3),
    _RlPortGmrpLeaveAllTime_Type()
)
rlPortGmrpLeaveAllTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPortGmrpLeaveAllTime.setStatus("mandatory")


class _RlPortGmrpOverrideGarp_Type(EnabledStatus):
    """Custom type rlPortGmrpOverrideGarp based on EnabledStatus"""


_RlPortGmrpOverrideGarp_Object = MibTableColumn
rlPortGmrpOverrideGarp = _RlPortGmrpOverrideGarp_Object(
    (1, 3, 6, 1, 4, 1, 89, 75, 3, 1, 4),
    _RlPortGmrpOverrideGarp_Type()
)
rlPortGmrpOverrideGarp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPortGmrpOverrideGarp.setStatus("mandatory")
_RlGmrpVlanTable_Object = MibTable
rlGmrpVlanTable = _RlGmrpVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 75, 4)
)
if mibBuilder.loadTexts:
    rlGmrpVlanTable.setStatus("mandatory")
_RlGmrpVlanEntry_Object = MibTableRow
rlGmrpVlanEntry = _RlGmrpVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 75, 4, 1)
)
rlGmrpVlanEntry.setIndexNames(
    (0, "RADLAN-MIB", "rlGmrpVlanTag"),
)
if mibBuilder.loadTexts:
    rlGmrpVlanEntry.setStatus("mandatory")
_RlGmrpVlanTag_Type = Integer32
_RlGmrpVlanTag_Object = MibTableColumn
rlGmrpVlanTag = _RlGmrpVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 89, 75, 4, 1, 1),
    _RlGmrpVlanTag_Type()
)
rlGmrpVlanTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlGmrpVlanTag.setStatus("mandatory")


class _RlGmrpVlanEnable_Type(TruthValue):
    """Custom type rlGmrpVlanEnable based on TruthValue"""


_RlGmrpVlanEnable_Object = MibTableColumn
rlGmrpVlanEnable = _RlGmrpVlanEnable_Object(
    (1, 3, 6, 1, 4, 1, 89, 75, 4, 1, 2),
    _RlGmrpVlanEnable_Type()
)
rlGmrpVlanEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlGmrpVlanEnable.setStatus("mandatory")
_RlDhcpCl_ObjectIdentity = ObjectIdentity
rlDhcpCl = _RlDhcpCl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 76)
)
_RlDhcpClActionTable_Object = MibTable
rlDhcpClActionTable = _RlDhcpClActionTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 76, 3)
)
if mibBuilder.loadTexts:
    rlDhcpClActionTable.setStatus("mandatory")
_RlDhcpClActionEntry_Object = MibTableRow
rlDhcpClActionEntry = _RlDhcpClActionEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 76, 3, 1)
)
rlDhcpClActionEntry.setIndexNames(
    (0, "RADLAN-MIB", "rlDhcpClActionIfIndex"),
)
if mibBuilder.loadTexts:
    rlDhcpClActionEntry.setStatus("mandatory")
_RlDhcpClActionIfIndex_Type = InterfaceIndex
_RlDhcpClActionIfIndex_Object = MibTableColumn
rlDhcpClActionIfIndex = _RlDhcpClActionIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 76, 3, 1, 1),
    _RlDhcpClActionIfIndex_Type()
)
rlDhcpClActionIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDhcpClActionIfIndex.setStatus("mandatory")
_RlDhcpClActionStatus_Type = RowStatus
_RlDhcpClActionStatus_Object = MibTableColumn
rlDhcpClActionStatus = _RlDhcpClActionStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 76, 3, 1, 2),
    _RlDhcpClActionStatus_Type()
)
rlDhcpClActionStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpClActionStatus.setStatus("mandatory")


class _RlDhcpClActionHostName_Type(SnmpAdminString):
    """Custom type rlDhcpClActionHostName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RlDhcpClActionHostName_Type.__name__ = "SnmpAdminString"
_RlDhcpClActionHostName_Object = MibTableColumn
rlDhcpClActionHostName = _RlDhcpClActionHostName_Object(
    (1, 3, 6, 1, 4, 1, 89, 76, 3, 1, 3),
    _RlDhcpClActionHostName_Type()
)
rlDhcpClActionHostName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpClActionHostName.setStatus("mandatory")
_RlDhcpApprovalEnabled_Type = TruthValue
_RlDhcpApprovalEnabled_Object = MibScalar
rlDhcpApprovalEnabled = _RlDhcpApprovalEnabled_Object(
    (1, 3, 6, 1, 4, 1, 89, 76, 4),
    _RlDhcpApprovalEnabled_Type()
)
rlDhcpApprovalEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDhcpApprovalEnabled.setStatus("mandatory")
_RlDhcpApprovalWaitingTable_Object = MibTable
rlDhcpApprovalWaitingTable = _RlDhcpApprovalWaitingTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 76, 5)
)
if mibBuilder.loadTexts:
    rlDhcpApprovalWaitingTable.setStatus("mandatory")
_RlDhcpApprovalWaitingEntry_Object = MibTableRow
rlDhcpApprovalWaitingEntry = _RlDhcpApprovalWaitingEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 76, 5, 1)
)
rlDhcpApprovalWaitingEntry.setIndexNames(
    (0, "RADLAN-MIB", "rlDhcpApprovalWaitingIfIndex"),
)
if mibBuilder.loadTexts:
    rlDhcpApprovalWaitingEntry.setStatus("mandatory")
_RlDhcpApprovalWaitingIfIndex_Type = InterfaceIndex
_RlDhcpApprovalWaitingIfIndex_Object = MibTableColumn
rlDhcpApprovalWaitingIfIndex = _RlDhcpApprovalWaitingIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 76, 5, 1, 1),
    _RlDhcpApprovalWaitingIfIndex_Type()
)
rlDhcpApprovalWaitingIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDhcpApprovalWaitingIfIndex.setStatus("mandatory")
_RlDhcpApprovalWaitingAddress_Type = IpAddress
_RlDhcpApprovalWaitingAddress_Object = MibTableColumn
rlDhcpApprovalWaitingAddress = _RlDhcpApprovalWaitingAddress_Object(
    (1, 3, 6, 1, 4, 1, 89, 76, 5, 1, 2),
    _RlDhcpApprovalWaitingAddress_Type()
)
rlDhcpApprovalWaitingAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDhcpApprovalWaitingAddress.setStatus("mandatory")
_RlDhcpApprovalWaitingMask_Type = IpAddress
_RlDhcpApprovalWaitingMask_Object = MibTableColumn
rlDhcpApprovalWaitingMask = _RlDhcpApprovalWaitingMask_Object(
    (1, 3, 6, 1, 4, 1, 89, 76, 5, 1, 3),
    _RlDhcpApprovalWaitingMask_Type()
)
rlDhcpApprovalWaitingMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDhcpApprovalWaitingMask.setStatus("mandatory")
_RlDhcpApprovalWaitingGateway_Type = IpAddress
_RlDhcpApprovalWaitingGateway_Object = MibTableColumn
rlDhcpApprovalWaitingGateway = _RlDhcpApprovalWaitingGateway_Object(
    (1, 3, 6, 1, 4, 1, 89, 76, 5, 1, 4),
    _RlDhcpApprovalWaitingGateway_Type()
)
rlDhcpApprovalWaitingGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDhcpApprovalWaitingGateway.setStatus("mandatory")
_RlDhcpApprovalActionTable_Object = MibTable
rlDhcpApprovalActionTable = _RlDhcpApprovalActionTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 76, 6)
)
if mibBuilder.loadTexts:
    rlDhcpApprovalActionTable.setStatus("mandatory")
_RlDhcpApprovalActionEntry_Object = MibTableRow
rlDhcpApprovalActionEntry = _RlDhcpApprovalActionEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 76, 6, 1)
)
rlDhcpApprovalActionEntry.setIndexNames(
    (0, "RADLAN-MIB", "rlDhcpApprovalActionIfIndex"),
    (0, "RADLAN-MIB", "rlDhcpApprovalActionAddress"),
    (0, "RADLAN-MIB", "rlDhcpApprovalActionMask"),
)
if mibBuilder.loadTexts:
    rlDhcpApprovalActionEntry.setStatus("mandatory")
_RlDhcpApprovalActionIfIndex_Type = InterfaceIndex
_RlDhcpApprovalActionIfIndex_Object = MibTableColumn
rlDhcpApprovalActionIfIndex = _RlDhcpApprovalActionIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 76, 6, 1, 1),
    _RlDhcpApprovalActionIfIndex_Type()
)
rlDhcpApprovalActionIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDhcpApprovalActionIfIndex.setStatus("mandatory")
_RlDhcpApprovalActionAddress_Type = IpAddress
_RlDhcpApprovalActionAddress_Object = MibTableColumn
rlDhcpApprovalActionAddress = _RlDhcpApprovalActionAddress_Object(
    (1, 3, 6, 1, 4, 1, 89, 76, 6, 1, 2),
    _RlDhcpApprovalActionAddress_Type()
)
rlDhcpApprovalActionAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDhcpApprovalActionAddress.setStatus("mandatory")
_RlDhcpApprovalActionMask_Type = IpAddress
_RlDhcpApprovalActionMask_Object = MibTableColumn
rlDhcpApprovalActionMask = _RlDhcpApprovalActionMask_Object(
    (1, 3, 6, 1, 4, 1, 89, 76, 6, 1, 3),
    _RlDhcpApprovalActionMask_Type()
)
rlDhcpApprovalActionMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDhcpApprovalActionMask.setStatus("mandatory")
_RlDhcpApprovalActionApprove_Type = TruthValue
_RlDhcpApprovalActionApprove_Object = MibTableColumn
rlDhcpApprovalActionApprove = _RlDhcpApprovalActionApprove_Object(
    (1, 3, 6, 1, 4, 1, 89, 76, 6, 1, 4),
    _RlDhcpApprovalActionApprove_Type()
)
rlDhcpApprovalActionApprove.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpApprovalActionApprove.setStatus("mandatory")
_RlDhcpClCommandTable_Object = MibTable
rlDhcpClCommandTable = _RlDhcpClCommandTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 76, 7)
)
if mibBuilder.loadTexts:
    rlDhcpClCommandTable.setStatus("mandatory")
_RlDhcpClCommandEntry_Object = MibTableRow
rlDhcpClCommandEntry = _RlDhcpClCommandEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 76, 7, 1)
)
rlDhcpClCommandEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    rlDhcpClCommandEntry.setStatus("mandatory")


class _RlDhcpClCommandAction_Type(Integer32):
    """Custom type rlDhcpClCommandAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("renew", 1))
    )


_RlDhcpClCommandAction_Type.__name__ = "Integer32"
_RlDhcpClCommandAction_Object = MibTableColumn
rlDhcpClCommandAction = _RlDhcpClCommandAction_Object(
    (1, 3, 6, 1, 4, 1, 89, 76, 7, 1, 2),
    _RlDhcpClCommandAction_Type()
)
rlDhcpClCommandAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpClCommandAction.setStatus("mandatory")
_RlStormCtrl_ObjectIdentity = ObjectIdentity
rlStormCtrl = _RlStormCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 77)
)
_RlStormCtrlSupport_Type = TruthValue
_RlStormCtrlSupport_Object = MibScalar
rlStormCtrlSupport = _RlStormCtrlSupport_Object(
    (1, 3, 6, 1, 4, 1, 89, 77, 1),
    _RlStormCtrlSupport_Type()
)
rlStormCtrlSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlStormCtrlSupport.setStatus("mandatory")
_RlStormCtrlMibVersion_Type = Integer32
_RlStormCtrlMibVersion_Object = MibScalar
rlStormCtrlMibVersion = _RlStormCtrlMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 89, 77, 2),
    _RlStormCtrlMibVersion_Type()
)
rlStormCtrlMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlStormCtrlMibVersion.setStatus("mandatory")


class _RlStormCtrlRateUnitTypeSupport_Type(OctetString):
    """Custom type rlStormCtrlRateUnitTypeSupport based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_RlStormCtrlRateUnitTypeSupport_Type.__name__ = "OctetString"
_RlStormCtrlRateUnitTypeSupport_Object = MibScalar
rlStormCtrlRateUnitTypeSupport = _RlStormCtrlRateUnitTypeSupport_Object(
    (1, 3, 6, 1, 4, 1, 89, 77, 3),
    _RlStormCtrlRateUnitTypeSupport_Type()
)
rlStormCtrlRateUnitTypeSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlStormCtrlRateUnitTypeSupport.setStatus("mandatory")


class _RlStormCtrlTypeSupport_Type(OctetString):
    """Custom type rlStormCtrlTypeSupport based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_RlStormCtrlTypeSupport_Type.__name__ = "OctetString"
_RlStormCtrlTypeSupport_Object = MibScalar
rlStormCtrlTypeSupport = _RlStormCtrlTypeSupport_Object(
    (1, 3, 6, 1, 4, 1, 89, 77, 4),
    _RlStormCtrlTypeSupport_Type()
)
rlStormCtrlTypeSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlStormCtrlTypeSupport.setStatus("mandatory")


class _RlStormCtrlRateSupportPerType_Type(OctetString):
    """Custom type rlStormCtrlRateSupportPerType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_RlStormCtrlRateSupportPerType_Type.__name__ = "OctetString"
_RlStormCtrlRateSupportPerType_Object = MibScalar
rlStormCtrlRateSupportPerType = _RlStormCtrlRateSupportPerType_Object(
    (1, 3, 6, 1, 4, 1, 89, 77, 5),
    _RlStormCtrlRateSupportPerType_Type()
)
rlStormCtrlRateSupportPerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlStormCtrlRateSupportPerType.setStatus("mandatory")


class _RlStormCtrlEnbaleDependencyBetweenTypes_Type(OctetString):
    """Custom type rlStormCtrlEnbaleDependencyBetweenTypes based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_RlStormCtrlEnbaleDependencyBetweenTypes_Type.__name__ = "OctetString"
_RlStormCtrlEnbaleDependencyBetweenTypes_Object = MibScalar
rlStormCtrlEnbaleDependencyBetweenTypes = _RlStormCtrlEnbaleDependencyBetweenTypes_Object(
    (1, 3, 6, 1, 4, 1, 89, 77, 6),
    _RlStormCtrlEnbaleDependencyBetweenTypes_Type()
)
rlStormCtrlEnbaleDependencyBetweenTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlStormCtrlEnbaleDependencyBetweenTypes.setStatus("mandatory")


class _RlStormCtrlRateDependencyBetweenTypes_Type(OctetString):
    """Custom type rlStormCtrlRateDependencyBetweenTypes based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_RlStormCtrlRateDependencyBetweenTypes_Type.__name__ = "OctetString"
_RlStormCtrlRateDependencyBetweenTypes_Object = MibScalar
rlStormCtrlRateDependencyBetweenTypes = _RlStormCtrlRateDependencyBetweenTypes_Object(
    (1, 3, 6, 1, 4, 1, 89, 77, 7),
    _RlStormCtrlRateDependencyBetweenTypes_Type()
)
rlStormCtrlRateDependencyBetweenTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlStormCtrlRateDependencyBetweenTypes.setStatus("mandatory")
_RlStormCtrlTable_Object = MibTable
rlStormCtrlTable = _RlStormCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 77, 8)
)
if mibBuilder.loadTexts:
    rlStormCtrlTable.setStatus("mandatory")
_RlStormCtrlEntry_Object = MibTableRow
rlStormCtrlEntry = _RlStormCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 77, 8, 1)
)
rlStormCtrlEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    rlStormCtrlEntry.setStatus("mandatory")
_RlStormCtrlRateType_Type = RlStormCtrlRateUnit
_RlStormCtrlRateType_Object = MibTableColumn
rlStormCtrlRateType = _RlStormCtrlRateType_Object(
    (1, 3, 6, 1, 4, 1, 89, 77, 8, 1, 1),
    _RlStormCtrlRateType_Type()
)
rlStormCtrlRateType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlStormCtrlRateType.setStatus("mandatory")


class _RlStormCtrlUnknownUnicastEnable_Type(TruthValue):
    """Custom type rlStormCtrlUnknownUnicastEnable based on TruthValue"""


_RlStormCtrlUnknownUnicastEnable_Object = MibTableColumn
rlStormCtrlUnknownUnicastEnable = _RlStormCtrlUnknownUnicastEnable_Object(
    (1, 3, 6, 1, 4, 1, 89, 77, 8, 1, 2),
    _RlStormCtrlUnknownUnicastEnable_Type()
)
rlStormCtrlUnknownUnicastEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlStormCtrlUnknownUnicastEnable.setStatus("mandatory")


class _RlStormCtrlUnknownUnicastRate_Type(Unsigned_32):
    """Custom type rlStormCtrlUnknownUnicastRate based on Unsigned_32"""
    defaultValue = 0


_RlStormCtrlUnknownUnicastRate_Object = MibTableColumn
rlStormCtrlUnknownUnicastRate = _RlStormCtrlUnknownUnicastRate_Object(
    (1, 3, 6, 1, 4, 1, 89, 77, 8, 1, 3),
    _RlStormCtrlUnknownUnicastRate_Type()
)
rlStormCtrlUnknownUnicastRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlStormCtrlUnknownUnicastRate.setStatus("mandatory")


class _RlStormCtrlUnknownMulticastEnable_Type(TruthValue):
    """Custom type rlStormCtrlUnknownMulticastEnable based on TruthValue"""


_RlStormCtrlUnknownMulticastEnable_Object = MibTableColumn
rlStormCtrlUnknownMulticastEnable = _RlStormCtrlUnknownMulticastEnable_Object(
    (1, 3, 6, 1, 4, 1, 89, 77, 8, 1, 4),
    _RlStormCtrlUnknownMulticastEnable_Type()
)
rlStormCtrlUnknownMulticastEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlStormCtrlUnknownMulticastEnable.setStatus("mandatory")


class _RlStormCtrlUnknownMulticastRate_Type(Unsigned_32):
    """Custom type rlStormCtrlUnknownMulticastRate based on Unsigned_32"""
    defaultValue = 0


_RlStormCtrlUnknownMulticastRate_Object = MibTableColumn
rlStormCtrlUnknownMulticastRate = _RlStormCtrlUnknownMulticastRate_Object(
    (1, 3, 6, 1, 4, 1, 89, 77, 8, 1, 5),
    _RlStormCtrlUnknownMulticastRate_Type()
)
rlStormCtrlUnknownMulticastRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlStormCtrlUnknownMulticastRate.setStatus("mandatory")


class _RlStormCtrlBroadcastEnable_Type(TruthValue):
    """Custom type rlStormCtrlBroadcastEnable based on TruthValue"""


_RlStormCtrlBroadcastEnable_Object = MibTableColumn
rlStormCtrlBroadcastEnable = _RlStormCtrlBroadcastEnable_Object(
    (1, 3, 6, 1, 4, 1, 89, 77, 8, 1, 6),
    _RlStormCtrlBroadcastEnable_Type()
)
rlStormCtrlBroadcastEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlStormCtrlBroadcastEnable.setStatus("mandatory")


class _RlStormCtrlBroadcastRate_Type(Unsigned_32):
    """Custom type rlStormCtrlBroadcastRate based on Unsigned_32"""
    defaultValue = 0


_RlStormCtrlBroadcastRate_Object = MibTableColumn
rlStormCtrlBroadcastRate = _RlStormCtrlBroadcastRate_Object(
    (1, 3, 6, 1, 4, 1, 89, 77, 8, 1, 7),
    _RlStormCtrlBroadcastRate_Type()
)
rlStormCtrlBroadcastRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlStormCtrlBroadcastRate.setStatus("mandatory")


class _RlStormCtrlMulticastEnable_Type(TruthValue):
    """Custom type rlStormCtrlMulticastEnable based on TruthValue"""


_RlStormCtrlMulticastEnable_Object = MibTableColumn
rlStormCtrlMulticastEnable = _RlStormCtrlMulticastEnable_Object(
    (1, 3, 6, 1, 4, 1, 89, 77, 8, 1, 8),
    _RlStormCtrlMulticastEnable_Type()
)
rlStormCtrlMulticastEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlStormCtrlMulticastEnable.setStatus("mandatory")


class _RlStormCtrlMulticastRate_Type(Unsigned_32):
    """Custom type rlStormCtrlMulticastRate based on Unsigned_32"""
    defaultValue = 0


_RlStormCtrlMulticastRate_Object = MibTableColumn
rlStormCtrlMulticastRate = _RlStormCtrlMulticastRate_Object(
    (1, 3, 6, 1, 4, 1, 89, 77, 8, 1, 9),
    _RlStormCtrlMulticastRate_Type()
)
rlStormCtrlMulticastRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlStormCtrlMulticastRate.setStatus("mandatory")


class _RlStormCtrlSetDefaultRateType_Type(TruthValue):
    """Custom type rlStormCtrlSetDefaultRateType based on TruthValue"""


_RlStormCtrlSetDefaultRateType_Object = MibTableColumn
rlStormCtrlSetDefaultRateType = _RlStormCtrlSetDefaultRateType_Object(
    (1, 3, 6, 1, 4, 1, 89, 77, 8, 1, 10),
    _RlStormCtrlSetDefaultRateType_Type()
)
rlStormCtrlSetDefaultRateType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlStormCtrlSetDefaultRateType.setStatus("mandatory")


class _RlStormCtrlSetDefaultUnknownUnicastEnable_Type(TruthValue):
    """Custom type rlStormCtrlSetDefaultUnknownUnicastEnable based on TruthValue"""


_RlStormCtrlSetDefaultUnknownUnicastEnable_Object = MibTableColumn
rlStormCtrlSetDefaultUnknownUnicastEnable = _RlStormCtrlSetDefaultUnknownUnicastEnable_Object(
    (1, 3, 6, 1, 4, 1, 89, 77, 8, 1, 11),
    _RlStormCtrlSetDefaultUnknownUnicastEnable_Type()
)
rlStormCtrlSetDefaultUnknownUnicastEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlStormCtrlSetDefaultUnknownUnicastEnable.setStatus("mandatory")


class _RlStormCtrlSetDefaultUnknownUnicastRate_Type(TruthValue):
    """Custom type rlStormCtrlSetDefaultUnknownUnicastRate based on TruthValue"""


_RlStormCtrlSetDefaultUnknownUnicastRate_Object = MibTableColumn
rlStormCtrlSetDefaultUnknownUnicastRate = _RlStormCtrlSetDefaultUnknownUnicastRate_Object(
    (1, 3, 6, 1, 4, 1, 89, 77, 8, 1, 12),
    _RlStormCtrlSetDefaultUnknownUnicastRate_Type()
)
rlStormCtrlSetDefaultUnknownUnicastRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlStormCtrlSetDefaultUnknownUnicastRate.setStatus("mandatory")


class _RlStormCtrlSetDefaultUnknownMulticastEnable_Type(TruthValue):
    """Custom type rlStormCtrlSetDefaultUnknownMulticastEnable based on TruthValue"""


_RlStormCtrlSetDefaultUnknownMulticastEnable_Object = MibTableColumn
rlStormCtrlSetDefaultUnknownMulticastEnable = _RlStormCtrlSetDefaultUnknownMulticastEnable_Object(
    (1, 3, 6, 1, 4, 1, 89, 77, 8, 1, 13),
    _RlStormCtrlSetDefaultUnknownMulticastEnable_Type()
)
rlStormCtrlSetDefaultUnknownMulticastEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlStormCtrlSetDefaultUnknownMulticastEnable.setStatus("mandatory")


class _RlStormCtrlSetDefaultUnknownMulticastRate_Type(TruthValue):
    """Custom type rlStormCtrlSetDefaultUnknownMulticastRate based on TruthValue"""


_RlStormCtrlSetDefaultUnknownMulticastRate_Object = MibTableColumn
rlStormCtrlSetDefaultUnknownMulticastRate = _RlStormCtrlSetDefaultUnknownMulticastRate_Object(
    (1, 3, 6, 1, 4, 1, 89, 77, 8, 1, 14),
    _RlStormCtrlSetDefaultUnknownMulticastRate_Type()
)
rlStormCtrlSetDefaultUnknownMulticastRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlStormCtrlSetDefaultUnknownMulticastRate.setStatus("mandatory")


class _RlStormCtrlSetDefaultBroadcastEnable_Type(TruthValue):
    """Custom type rlStormCtrlSetDefaultBroadcastEnable based on TruthValue"""


_RlStormCtrlSetDefaultBroadcastEnable_Object = MibTableColumn
rlStormCtrlSetDefaultBroadcastEnable = _RlStormCtrlSetDefaultBroadcastEnable_Object(
    (1, 3, 6, 1, 4, 1, 89, 77, 8, 1, 15),
    _RlStormCtrlSetDefaultBroadcastEnable_Type()
)
rlStormCtrlSetDefaultBroadcastEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlStormCtrlSetDefaultBroadcastEnable.setStatus("mandatory")


class _RlStormCtrlSetDefaultBroadcastRate_Type(TruthValue):
    """Custom type rlStormCtrlSetDefaultBroadcastRate based on TruthValue"""


_RlStormCtrlSetDefaultBroadcastRate_Object = MibTableColumn
rlStormCtrlSetDefaultBroadcastRate = _RlStormCtrlSetDefaultBroadcastRate_Object(
    (1, 3, 6, 1, 4, 1, 89, 77, 8, 1, 16),
    _RlStormCtrlSetDefaultBroadcastRate_Type()
)
rlStormCtrlSetDefaultBroadcastRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlStormCtrlSetDefaultBroadcastRate.setStatus("mandatory")


class _RlStormCtrlSetDefaultMulticastEnable_Type(TruthValue):
    """Custom type rlStormCtrlSetDefaultMulticastEnable based on TruthValue"""


_RlStormCtrlSetDefaultMulticastEnable_Object = MibTableColumn
rlStormCtrlSetDefaultMulticastEnable = _RlStormCtrlSetDefaultMulticastEnable_Object(
    (1, 3, 6, 1, 4, 1, 89, 77, 8, 1, 17),
    _RlStormCtrlSetDefaultMulticastEnable_Type()
)
rlStormCtrlSetDefaultMulticastEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlStormCtrlSetDefaultMulticastEnable.setStatus("mandatory")


class _RlStormCtrlSetDefaultMulticastRate_Type(TruthValue):
    """Custom type rlStormCtrlSetDefaultMulticastRate based on TruthValue"""


_RlStormCtrlSetDefaultMulticastRate_Object = MibTableColumn
rlStormCtrlSetDefaultMulticastRate = _RlStormCtrlSetDefaultMulticastRate_Object(
    (1, 3, 6, 1, 4, 1, 89, 77, 8, 1, 18),
    _RlStormCtrlSetDefaultMulticastRate_Type()
)
rlStormCtrlSetDefaultMulticastRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlStormCtrlSetDefaultMulticastRate.setStatus("mandatory")
_RlStormCtrlGroupTable_Object = MibTable
rlStormCtrlGroupTable = _RlStormCtrlGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 77, 9)
)
if mibBuilder.loadTexts:
    rlStormCtrlGroupTable.setStatus("mandatory")
_RlStormCtrlGroupEntry_Object = MibTableRow
rlStormCtrlGroupEntry = _RlStormCtrlGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 77, 9, 1)
)
rlStormCtrlGroupEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    rlStormCtrlGroupEntry.setStatus("mandatory")
_RlStormCtrlGroupUnknownUnicastId_Type = Integer32
_RlStormCtrlGroupUnknownUnicastId_Object = MibTableColumn
rlStormCtrlGroupUnknownUnicastId = _RlStormCtrlGroupUnknownUnicastId_Object(
    (1, 3, 6, 1, 4, 1, 89, 77, 9, 1, 1),
    _RlStormCtrlGroupUnknownUnicastId_Type()
)
rlStormCtrlGroupUnknownUnicastId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlStormCtrlGroupUnknownUnicastId.setStatus("mandatory")
_RlStormCtrlGroupUnknownMulticastId_Type = Integer32
_RlStormCtrlGroupUnknownMulticastId_Object = MibTableColumn
rlStormCtrlGroupUnknownMulticastId = _RlStormCtrlGroupUnknownMulticastId_Object(
    (1, 3, 6, 1, 4, 1, 89, 77, 9, 1, 2),
    _RlStormCtrlGroupUnknownMulticastId_Type()
)
rlStormCtrlGroupUnknownMulticastId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlStormCtrlGroupUnknownMulticastId.setStatus("mandatory")
_RlStormCtrlGroupBroadcastId_Type = Integer32
_RlStormCtrlGroupBroadcastId_Object = MibTableColumn
rlStormCtrlGroupBroadcastId = _RlStormCtrlGroupBroadcastId_Object(
    (1, 3, 6, 1, 4, 1, 89, 77, 9, 1, 3),
    _RlStormCtrlGroupBroadcastId_Type()
)
rlStormCtrlGroupBroadcastId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlStormCtrlGroupBroadcastId.setStatus("mandatory")
_RlStormCtrlGroupMulticastId_Type = Integer32
_RlStormCtrlGroupMulticastId_Object = MibTableColumn
rlStormCtrlGroupMulticastId = _RlStormCtrlGroupMulticastId_Object(
    (1, 3, 6, 1, 4, 1, 89, 77, 9, 1, 4),
    _RlStormCtrlGroupMulticastId_Type()
)
rlStormCtrlGroupMulticastId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlStormCtrlGroupMulticastId.setStatus("mandatory")
_RlSsh_ObjectIdentity = ObjectIdentity
rlSsh = _RlSsh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 78)
)
_RlAAA_ObjectIdentity = ObjectIdentity
rlAAA = _RlAAA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 79)
)
_RlRadius_ObjectIdentity = ObjectIdentity
rlRadius = _RlRadius_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 80)
)
_RlTraceRoute_ObjectIdentity = ObjectIdentity
rlTraceRoute = _RlTraceRoute_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 81)
)
_RlTraceRouteMibVersion_Type = Integer32
_RlTraceRouteMibVersion_Object = MibScalar
rlTraceRouteMibVersion = _RlTraceRouteMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 89, 81, 1),
    _RlTraceRouteMibVersion_Type()
)
rlTraceRouteMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlTraceRouteMibVersion.setStatus("mandatory")
_RlSyslog_ObjectIdentity = ObjectIdentity
rlSyslog = _RlSyslog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 82)
)
_RlEnv_ObjectIdentity = ObjectIdentity
rlEnv = _RlEnv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 83)
)
_RlSmon_ObjectIdentity = ObjectIdentity
rlSmon = _RlSmon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 84)
)
_RlPortCopyMibVersion_Type = Integer32
_RlPortCopyMibVersion_Object = MibScalar
rlPortCopyMibVersion = _RlPortCopyMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 89, 84, 1),
    _RlPortCopyMibVersion_Type()
)
rlPortCopyMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPortCopyMibVersion.setStatus("mandatory")


class _RlPortCopySupport_Type(Integer32):
    """Custom type rlPortCopySupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 2),
          ("supported", 1))
    )


_RlPortCopySupport_Type.__name__ = "Integer32"
_RlPortCopySupport_Object = MibScalar
rlPortCopySupport = _RlPortCopySupport_Object(
    (1, 3, 6, 1, 4, 1, 89, 84, 2),
    _RlPortCopySupport_Type()
)
rlPortCopySupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPortCopySupport.setStatus("mandatory")
_RlPortCopyVlanTaggingTable_Object = MibTable
rlPortCopyVlanTaggingTable = _RlPortCopyVlanTaggingTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 84, 3)
)
if mibBuilder.loadTexts:
    rlPortCopyVlanTaggingTable.setStatus("mandatory")
_RlPortCopyVlanTaggingEntry_Object = MibTableRow
rlPortCopyVlanTaggingEntry = _RlPortCopyVlanTaggingEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 84, 3, 1)
)
rlPortCopyVlanTaggingEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    rlPortCopyVlanTaggingEntry.setStatus("mandatory")


class _RlPortCopyVlanTagging_Type(TruthValue):
    """Custom type rlPortCopyVlanTagging based on TruthValue"""


_RlPortCopyVlanTagging_Object = MibTableColumn
rlPortCopyVlanTagging = _RlPortCopyVlanTagging_Object(
    (1, 3, 6, 1, 4, 1, 89, 84, 3, 1, 1),
    _RlPortCopyVlanTagging_Type()
)
rlPortCopyVlanTagging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPortCopyVlanTagging.setStatus("mandatory")
_RlSocket_ObjectIdentity = ObjectIdentity
rlSocket = _RlSocket_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 85)
)
_RlSocketMibVersion_Type = Integer32
_RlSocketMibVersion_Object = MibScalar
rlSocketMibVersion = _RlSocketMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 89, 85, 1),
    _RlSocketMibVersion_Type()
)
rlSocketMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSocketMibVersion.setStatus("mandatory")
_RlSocketTable_Object = MibTable
rlSocketTable = _RlSocketTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 85, 2)
)
if mibBuilder.loadTexts:
    rlSocketTable.setStatus("mandatory")
_RlSocketEntry_Object = MibTableRow
rlSocketEntry = _RlSocketEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 85, 2, 1)
)
rlSocketEntry.setIndexNames(
    (0, "RADLAN-MIB", "rlSocketId"),
)
if mibBuilder.loadTexts:
    rlSocketEntry.setStatus("mandatory")
_RlSocketId_Type = Integer32
_RlSocketId_Object = MibTableColumn
rlSocketId = _RlSocketId_Object(
    (1, 3, 6, 1, 4, 1, 89, 85, 2, 1, 1),
    _RlSocketId_Type()
)
rlSocketId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSocketId.setStatus("mandatory")


class _RlSocketType_Type(Integer32):
    """Custom type rlSocketType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dgram", 2),
          ("raw", 3),
          ("stream", 1))
    )


_RlSocketType_Type.__name__ = "Integer32"
_RlSocketType_Object = MibTableColumn
rlSocketType = _RlSocketType_Object(
    (1, 3, 6, 1, 4, 1, 89, 85, 2, 1, 2),
    _RlSocketType_Type()
)
rlSocketType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSocketType.setStatus("mandatory")


class _RlSocketState_Type(Integer32):
    """Custom type rlSocketState based on Integer32"""
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
        *(("closed", 5),
          ("connected", 1),
          ("notConnected", 2),
          ("recvClosed", 3),
          ("sendClosed", 4))
    )


_RlSocketState_Type.__name__ = "Integer32"
_RlSocketState_Object = MibTableColumn
rlSocketState = _RlSocketState_Object(
    (1, 3, 6, 1, 4, 1, 89, 85, 2, 1, 3),
    _RlSocketState_Type()
)
rlSocketState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSocketState.setStatus("mandatory")


class _RlSocketBlockMode_Type(Integer32):
    """Custom type rlSocketBlockMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("blocking", 1),
          ("nonBlocking", 2))
    )


_RlSocketBlockMode_Type.__name__ = "Integer32"
_RlSocketBlockMode_Object = MibTableColumn
rlSocketBlockMode = _RlSocketBlockMode_Object(
    (1, 3, 6, 1, 4, 1, 89, 85, 2, 1, 4),
    _RlSocketBlockMode_Type()
)
rlSocketBlockMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSocketBlockMode.setStatus("mandatory")
_RlSocketUpTime_Type = TimeTicks
_RlSocketUpTime_Object = MibTableColumn
rlSocketUpTime = _RlSocketUpTime_Object(
    (1, 3, 6, 1, 4, 1, 89, 85, 2, 1, 5),
    _RlSocketUpTime_Type()
)
rlSocketUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSocketUpTime.setStatus("mandatory")
_RlDigitalKeyManage_ObjectIdentity = ObjectIdentity
rlDigitalKeyManage = _RlDigitalKeyManage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 86)
)
_RlMD5KeyChainTable_Object = MibTable
rlMD5KeyChainTable = _RlMD5KeyChainTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 86, 1)
)
if mibBuilder.loadTexts:
    rlMD5KeyChainTable.setStatus("mandatory")
_RlMD5KeyChainEntry_Object = MibTableRow
rlMD5KeyChainEntry = _RlMD5KeyChainEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 86, 1, 1)
)
rlMD5KeyChainEntry.setIndexNames(
    (0, "RADLAN-MIB", "rlMD5KeyChainName"),
    (0, "RADLAN-MIB", "rlMD5KeyChainKeyId"),
)
if mibBuilder.loadTexts:
    rlMD5KeyChainEntry.setStatus("mandatory")
_RlMD5KeyChainName_Type = DisplayString
_RlMD5KeyChainName_Object = MibTableColumn
rlMD5KeyChainName = _RlMD5KeyChainName_Object(
    (1, 3, 6, 1, 4, 1, 89, 86, 1, 1, 1),
    _RlMD5KeyChainName_Type()
)
rlMD5KeyChainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlMD5KeyChainName.setStatus("mandatory")


class _RlMD5KeyChainKeyId_Type(Integer32):
    """Custom type rlMD5KeyChainKeyId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_RlMD5KeyChainKeyId_Type.__name__ = "Integer32"
_RlMD5KeyChainKeyId_Object = MibTableColumn
rlMD5KeyChainKeyId = _RlMD5KeyChainKeyId_Object(
    (1, 3, 6, 1, 4, 1, 89, 86, 1, 1, 2),
    _RlMD5KeyChainKeyId_Type()
)
rlMD5KeyChainKeyId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlMD5KeyChainKeyId.setStatus("mandatory")
_RlMD5KeyChainKeyRowStatus_Type = RowStatus
_RlMD5KeyChainKeyRowStatus_Object = MibTableColumn
rlMD5KeyChainKeyRowStatus = _RlMD5KeyChainKeyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 86, 1, 1, 3),
    _RlMD5KeyChainKeyRowStatus_Type()
)
rlMD5KeyChainKeyRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlMD5KeyChainKeyRowStatus.setStatus("mandatory")
_RlMD5KeyTable_Object = MibTable
rlMD5KeyTable = _RlMD5KeyTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 86, 2)
)
if mibBuilder.loadTexts:
    rlMD5KeyTable.setStatus("mandatory")
_RlMD5KeyEntry_Object = MibTableRow
rlMD5KeyEntry = _RlMD5KeyEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 86, 2, 1)
)
rlMD5KeyEntry.setIndexNames(
    (0, "RADLAN-MIB", "rlMD5KeyId"),
)
if mibBuilder.loadTexts:
    rlMD5KeyEntry.setStatus("mandatory")


class _RlMD5KeyId_Type(Integer32):
    """Custom type rlMD5KeyId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_RlMD5KeyId_Type.__name__ = "Integer32"
_RlMD5KeyId_Object = MibTableColumn
rlMD5KeyId = _RlMD5KeyId_Object(
    (1, 3, 6, 1, 4, 1, 89, 86, 2, 1, 1),
    _RlMD5KeyId_Type()
)
rlMD5KeyId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlMD5KeyId.setStatus("mandatory")


class _RlMD5Key_Type(DisplayString):
    """Custom type rlMD5Key based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_RlMD5Key_Type.__name__ = "DisplayString"
_RlMD5Key_Object = MibTableColumn
rlMD5Key = _RlMD5Key_Object(
    (1, 3, 6, 1, 4, 1, 89, 86, 2, 1, 2),
    _RlMD5Key_Type()
)
rlMD5Key.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlMD5Key.setStatus("mandatory")


class _RlMD5KeyStartAccept_Type(DateAndTime):
    """Custom type rlMD5KeyStartAccept based on DateAndTime"""
    defaultHexValue = "00000000"


_RlMD5KeyStartAccept_Object = MibTableColumn
rlMD5KeyStartAccept = _RlMD5KeyStartAccept_Object(
    (1, 3, 6, 1, 4, 1, 89, 86, 2, 1, 3),
    _RlMD5KeyStartAccept_Type()
)
rlMD5KeyStartAccept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlMD5KeyStartAccept.setStatus("mandatory")


class _RlMD5KeyStartGenerate_Type(DateAndTime):
    """Custom type rlMD5KeyStartGenerate based on DateAndTime"""
    defaultHexValue = "00000000"


_RlMD5KeyStartGenerate_Object = MibTableColumn
rlMD5KeyStartGenerate = _RlMD5KeyStartGenerate_Object(
    (1, 3, 6, 1, 4, 1, 89, 86, 2, 1, 4),
    _RlMD5KeyStartGenerate_Type()
)
rlMD5KeyStartGenerate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlMD5KeyStartGenerate.setStatus("mandatory")


class _RlMD5KeyStopGenerate_Type(DateAndTime):
    """Custom type rlMD5KeyStopGenerate based on DateAndTime"""
    defaultHexValue = "FFFFFFFF"


_RlMD5KeyStopGenerate_Object = MibTableColumn
rlMD5KeyStopGenerate = _RlMD5KeyStopGenerate_Object(
    (1, 3, 6, 1, 4, 1, 89, 86, 2, 1, 5),
    _RlMD5KeyStopGenerate_Type()
)
rlMD5KeyStopGenerate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlMD5KeyStopGenerate.setStatus("mandatory")


class _RlMD5KeyStopAccept_Type(DateAndTime):
    """Custom type rlMD5KeyStopAccept based on DateAndTime"""
    defaultHexValue = "FFFFFFFF"


_RlMD5KeyStopAccept_Object = MibTableColumn
rlMD5KeyStopAccept = _RlMD5KeyStopAccept_Object(
    (1, 3, 6, 1, 4, 1, 89, 86, 2, 1, 6),
    _RlMD5KeyStopAccept_Type()
)
rlMD5KeyStopAccept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlMD5KeyStopAccept.setStatus("mandatory")
_RlMD5KeyRowStatus_Type = RowStatus
_RlMD5KeyRowStatus_Object = MibTableColumn
rlMD5KeyRowStatus = _RlMD5KeyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 86, 2, 1, 7),
    _RlMD5KeyRowStatus_Type()
)
rlMD5KeyRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlMD5KeyRowStatus.setStatus("mandatory")
_RlCopy_ObjectIdentity = ObjectIdentity
rlCopy = _RlCopy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 87)
)
_RlQosCliMib_ObjectIdentity = ObjectIdentity
rlQosCliMib = _RlQosCliMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 88)
)
_RlMngInf_ObjectIdentity = ObjectIdentity
rlMngInf = _RlMngInf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 89)
)
_RlPhy_ObjectIdentity = ObjectIdentity
rlPhy = _RlPhy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 90)
)
_RlJumboFrames_ObjectIdentity = ObjectIdentity
rlJumboFrames = _RlJumboFrames_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 91)
)


class _RlJumboFramesCurrentStatus_Type(Integer32):
    """Custom type rlJumboFramesCurrentStatus based on Integer32"""
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


_RlJumboFramesCurrentStatus_Type.__name__ = "Integer32"
_RlJumboFramesCurrentStatus_Object = MibScalar
rlJumboFramesCurrentStatus = _RlJumboFramesCurrentStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 91, 1),
    _RlJumboFramesCurrentStatus_Type()
)
rlJumboFramesCurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlJumboFramesCurrentStatus.setStatus("mandatory")


class _RlJumboFramesStatusAfterReset_Type(Integer32):
    """Custom type rlJumboFramesStatusAfterReset based on Integer32"""
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


_RlJumboFramesStatusAfterReset_Type.__name__ = "Integer32"
_RlJumboFramesStatusAfterReset_Object = MibScalar
rlJumboFramesStatusAfterReset = _RlJumboFramesStatusAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 91, 2),
    _RlJumboFramesStatusAfterReset_Type()
)
rlJumboFramesStatusAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlJumboFramesStatusAfterReset.setStatus("mandatory")
_RlTimeSynchronization_ObjectIdentity = ObjectIdentity
rlTimeSynchronization = _RlTimeSynchronization_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 92)
)
_RlDnsCl_ObjectIdentity = ObjectIdentity
rlDnsCl = _RlDnsCl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 93)
)
_RlCDB_ObjectIdentity = ObjectIdentity
rlCDB = _RlCDB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 94)
)
_RlStartupCDBChanged_Type = TruthValue
_RlStartupCDBChanged_Object = MibScalar
rlStartupCDBChanged = _RlStartupCDBChanged_Object(
    (1, 3, 6, 1, 4, 1, 89, 94, 1),
    _RlStartupCDBChanged_Type()
)
rlStartupCDBChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlStartupCDBChanged.setStatus("mandatory")
_RlManualReboot_Type = TruthValue
_RlManualReboot_Object = MibScalar
rlManualReboot = _RlManualReboot_Object(
    (1, 3, 6, 1, 4, 1, 89, 94, 2),
    _RlManualReboot_Type()
)
rlManualReboot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlManualReboot.setStatus("mandatory")
_Rldot1x_ObjectIdentity = ObjectIdentity
rldot1x = _Rldot1x_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 95)
)
_Rldot1xMibVersion_Type = Integer32
_Rldot1xMibVersion_Object = MibScalar
rldot1xMibVersion = _Rldot1xMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 89, 95, 1),
    _Rldot1xMibVersion_Type()
)
rldot1xMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1xMibVersion.setStatus("mandatory")
_Rldot1xExtAuthSessionStatsTable_Object = MibTable
rldot1xExtAuthSessionStatsTable = _Rldot1xExtAuthSessionStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 95, 2)
)
if mibBuilder.loadTexts:
    rldot1xExtAuthSessionStatsTable.setStatus("mandatory")
_Rldot1xExtAuthSessionStatsEntry_Object = MibTableRow
rldot1xExtAuthSessionStatsEntry = _Rldot1xExtAuthSessionStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 95, 2, 1)
)
if mibBuilder.loadTexts:
    rldot1xExtAuthSessionStatsEntry.setStatus("mandatory")


class _RlDot1xAuthSessionAuthenticMethod_Type(Integer32):
    """Custom type rlDot1xAuthSessionAuthenticMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("localAuthServer", 2),
          ("none", 3),
          ("remoteAuthServer", 1))
    )


_RlDot1xAuthSessionAuthenticMethod_Type.__name__ = "Integer32"
_RlDot1xAuthSessionAuthenticMethod_Object = MibTableColumn
rlDot1xAuthSessionAuthenticMethod = _RlDot1xAuthSessionAuthenticMethod_Object(
    (1, 3, 6, 1, 4, 1, 89, 95, 2, 1, 1),
    _RlDot1xAuthSessionAuthenticMethod_Type()
)
rlDot1xAuthSessionAuthenticMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDot1xAuthSessionAuthenticMethod.setStatus("mandatory")
_Rldot1xGuestVlanSupported_Type = TruthValue
_Rldot1xGuestVlanSupported_Object = MibScalar
rldot1xGuestVlanSupported = _Rldot1xGuestVlanSupported_Object(
    (1, 3, 6, 1, 4, 1, 89, 95, 3),
    _Rldot1xGuestVlanSupported_Type()
)
rldot1xGuestVlanSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1xGuestVlanSupported.setStatus("mandatory")
_Rldot1xGuestVlanVID_Type = VlanIndex
_Rldot1xGuestVlanVID_Object = MibScalar
rldot1xGuestVlanVID = _Rldot1xGuestVlanVID_Object(
    (1, 3, 6, 1, 4, 1, 89, 95, 4),
    _Rldot1xGuestVlanVID_Type()
)
rldot1xGuestVlanVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rldot1xGuestVlanVID.setStatus("mandatory")
_Rldot1xGuestVlanPorts_Type = PortList
_Rldot1xGuestVlanPorts_Object = MibScalar
rldot1xGuestVlanPorts = _Rldot1xGuestVlanPorts_Object(
    (1, 3, 6, 1, 4, 1, 89, 95, 5),
    _Rldot1xGuestVlanPorts_Type()
)
rldot1xGuestVlanPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rldot1xGuestVlanPorts.setStatus("mandatory")
_Rldot1xUnAuthenticatedVlanSupported_Type = TruthValue
_Rldot1xUnAuthenticatedVlanSupported_Object = MibScalar
rldot1xUnAuthenticatedVlanSupported = _Rldot1xUnAuthenticatedVlanSupported_Object(
    (1, 3, 6, 1, 4, 1, 89, 95, 6),
    _Rldot1xUnAuthenticatedVlanSupported_Type()
)
rldot1xUnAuthenticatedVlanSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1xUnAuthenticatedVlanSupported.setStatus("mandatory")
_Rldot1xUnAuthenticatedVlanTable_Object = MibTable
rldot1xUnAuthenticatedVlanTable = _Rldot1xUnAuthenticatedVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 95, 7)
)
if mibBuilder.loadTexts:
    rldot1xUnAuthenticatedVlanTable.setStatus("mandatory")
_Rldot1xUnAuthenticatedVlanEntry_Object = MibTableRow
rldot1xUnAuthenticatedVlanEntry = _Rldot1xUnAuthenticatedVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 95, 7, 1)
)
rldot1xUnAuthenticatedVlanEntry.setIndexNames(
    (0, "Q-BRIDGE-MIB", "dot1qFdbId"),
)
if mibBuilder.loadTexts:
    rldot1xUnAuthenticatedVlanEntry.setStatus("mandatory")
_Rldot1xUnAuthenticatedVlanStatus_Type = RowStatus
_Rldot1xUnAuthenticatedVlanStatus_Object = MibTableColumn
rldot1xUnAuthenticatedVlanStatus = _Rldot1xUnAuthenticatedVlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 95, 7, 1, 1),
    _Rldot1xUnAuthenticatedVlanStatus_Type()
)
rldot1xUnAuthenticatedVlanStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rldot1xUnAuthenticatedVlanStatus.setStatus("mandatory")
_Rldot1xUserBasedVlanSupported_Type = TruthValue
_Rldot1xUserBasedVlanSupported_Object = MibScalar
rldot1xUserBasedVlanSupported = _Rldot1xUserBasedVlanSupported_Object(
    (1, 3, 6, 1, 4, 1, 89, 95, 8),
    _Rldot1xUserBasedVlanSupported_Type()
)
rldot1xUserBasedVlanSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1xUserBasedVlanSupported.setStatus("mandatory")
_Rldot1xUserBasedVlanPorts_Type = PortList
_Rldot1xUserBasedVlanPorts_Object = MibScalar
rldot1xUserBasedVlanPorts = _Rldot1xUserBasedVlanPorts_Object(
    (1, 3, 6, 1, 4, 1, 89, 95, 9),
    _Rldot1xUserBasedVlanPorts_Type()
)
rldot1xUserBasedVlanPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rldot1xUserBasedVlanPorts.setStatus("mandatory")
_Rldot1xAuthenticationPortTable_Object = MibTable
rldot1xAuthenticationPortTable = _Rldot1xAuthenticationPortTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 95, 10)
)
if mibBuilder.loadTexts:
    rldot1xAuthenticationPortTable.setStatus("mandatory")
_Rldot1xAuthenticationPortEntry_Object = MibTableRow
rldot1xAuthenticationPortEntry = _Rldot1xAuthenticationPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 95, 10, 1)
)
rldot1xAuthenticationPortEntry.setIndexNames(
    (0, "IEEE8021-PAE-MIB", "dot1xPaePortNumber"),
)
if mibBuilder.loadTexts:
    rldot1xAuthenticationPortEntry.setStatus("mandatory")


class _Rldot1xAuthenticationPortMethod_Type(Integer32):
    """Custom type rldot1xAuthenticationPortMethod based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("eapolOnly", 1),
          ("macAndEapol", 2),
          ("macOnly", 3))
    )


_Rldot1xAuthenticationPortMethod_Type.__name__ = "Integer32"
_Rldot1xAuthenticationPortMethod_Object = MibTableColumn
rldot1xAuthenticationPortMethod = _Rldot1xAuthenticationPortMethod_Object(
    (1, 3, 6, 1, 4, 1, 89, 95, 10, 1, 1),
    _Rldot1xAuthenticationPortMethod_Type()
)
rldot1xAuthenticationPortMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rldot1xAuthenticationPortMethod.setStatus("mandatory")
_Rldot1xAuthMultiStatsTable_Object = MibTable
rldot1xAuthMultiStatsTable = _Rldot1xAuthMultiStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 95, 11)
)
if mibBuilder.loadTexts:
    rldot1xAuthMultiStatsTable.setStatus("mandatory")
_Rldot1xAuthMultiStatsEntry_Object = MibTableRow
rldot1xAuthMultiStatsEntry = _Rldot1xAuthMultiStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 95, 11, 1)
)
rldot1xAuthMultiStatsEntry.setIndexNames(
    (0, "RADLAN-MIB", "rldot1xAuthMultiStatsPortNumber"),
    (0, "RADLAN-MIB", "rldot1xAuthMultiStatsSourceMac"),
)
if mibBuilder.loadTexts:
    rldot1xAuthMultiStatsEntry.setStatus("mandatory")
_Rldot1xAuthMultiStatsPortNumber_Type = Integer32
_Rldot1xAuthMultiStatsPortNumber_Object = MibTableColumn
rldot1xAuthMultiStatsPortNumber = _Rldot1xAuthMultiStatsPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 89, 95, 11, 1, 1),
    _Rldot1xAuthMultiStatsPortNumber_Type()
)
rldot1xAuthMultiStatsPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1xAuthMultiStatsPortNumber.setStatus("mandatory")
_Rldot1xAuthMultiStatsSourceMac_Type = MacAddress
_Rldot1xAuthMultiStatsSourceMac_Object = MibTableColumn
rldot1xAuthMultiStatsSourceMac = _Rldot1xAuthMultiStatsSourceMac_Object(
    (1, 3, 6, 1, 4, 1, 89, 95, 11, 1, 2),
    _Rldot1xAuthMultiStatsSourceMac_Type()
)
rldot1xAuthMultiStatsSourceMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1xAuthMultiStatsSourceMac.setStatus("mandatory")
_Rldot1xAuthMultiEapolFramesRx_Type = Counter32
_Rldot1xAuthMultiEapolFramesRx_Object = MibTableColumn
rldot1xAuthMultiEapolFramesRx = _Rldot1xAuthMultiEapolFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 89, 95, 11, 1, 3),
    _Rldot1xAuthMultiEapolFramesRx_Type()
)
rldot1xAuthMultiEapolFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1xAuthMultiEapolFramesRx.setStatus("mandatory")
_Rldot1xAuthMultiEapolFramesTx_Type = Counter32
_Rldot1xAuthMultiEapolFramesTx_Object = MibTableColumn
rldot1xAuthMultiEapolFramesTx = _Rldot1xAuthMultiEapolFramesTx_Object(
    (1, 3, 6, 1, 4, 1, 89, 95, 11, 1, 4),
    _Rldot1xAuthMultiEapolFramesTx_Type()
)
rldot1xAuthMultiEapolFramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1xAuthMultiEapolFramesTx.setStatus("mandatory")
_Rldot1xAuthMultiEapolStartFramesRx_Type = Counter32
_Rldot1xAuthMultiEapolStartFramesRx_Object = MibTableColumn
rldot1xAuthMultiEapolStartFramesRx = _Rldot1xAuthMultiEapolStartFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 89, 95, 11, 1, 5),
    _Rldot1xAuthMultiEapolStartFramesRx_Type()
)
rldot1xAuthMultiEapolStartFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1xAuthMultiEapolStartFramesRx.setStatus("mandatory")
_Rldot1xAuthMultiEapolLogoffFramesRx_Type = Counter32
_Rldot1xAuthMultiEapolLogoffFramesRx_Object = MibTableColumn
rldot1xAuthMultiEapolLogoffFramesRx = _Rldot1xAuthMultiEapolLogoffFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 89, 95, 11, 1, 6),
    _Rldot1xAuthMultiEapolLogoffFramesRx_Type()
)
rldot1xAuthMultiEapolLogoffFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1xAuthMultiEapolLogoffFramesRx.setStatus("mandatory")
_Rldot1xAuthMultiEapolRespIdFramesRx_Type = Counter32
_Rldot1xAuthMultiEapolRespIdFramesRx_Object = MibTableColumn
rldot1xAuthMultiEapolRespIdFramesRx = _Rldot1xAuthMultiEapolRespIdFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 89, 95, 11, 1, 7),
    _Rldot1xAuthMultiEapolRespIdFramesRx_Type()
)
rldot1xAuthMultiEapolRespIdFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1xAuthMultiEapolRespIdFramesRx.setStatus("mandatory")
_Rldot1xAuthMultiEapolRespFramesRx_Type = Counter32
_Rldot1xAuthMultiEapolRespFramesRx_Object = MibTableColumn
rldot1xAuthMultiEapolRespFramesRx = _Rldot1xAuthMultiEapolRespFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 89, 95, 11, 1, 8),
    _Rldot1xAuthMultiEapolRespFramesRx_Type()
)
rldot1xAuthMultiEapolRespFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1xAuthMultiEapolRespFramesRx.setStatus("mandatory")
_Rldot1xAuthMultiEapolReqIdFramesTx_Type = Counter32
_Rldot1xAuthMultiEapolReqIdFramesTx_Object = MibTableColumn
rldot1xAuthMultiEapolReqIdFramesTx = _Rldot1xAuthMultiEapolReqIdFramesTx_Object(
    (1, 3, 6, 1, 4, 1, 89, 95, 11, 1, 9),
    _Rldot1xAuthMultiEapolReqIdFramesTx_Type()
)
rldot1xAuthMultiEapolReqIdFramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1xAuthMultiEapolReqIdFramesTx.setStatus("mandatory")
_Rldot1xAuthMultiEapolReqFramesTx_Type = Counter32
_Rldot1xAuthMultiEapolReqFramesTx_Object = MibTableColumn
rldot1xAuthMultiEapolReqFramesTx = _Rldot1xAuthMultiEapolReqFramesTx_Object(
    (1, 3, 6, 1, 4, 1, 89, 95, 11, 1, 10),
    _Rldot1xAuthMultiEapolReqFramesTx_Type()
)
rldot1xAuthMultiEapolReqFramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1xAuthMultiEapolReqFramesTx.setStatus("mandatory")
_Rldot1xAuthMultiInvalidEapolFramesRx_Type = Counter32
_Rldot1xAuthMultiInvalidEapolFramesRx_Object = MibTableColumn
rldot1xAuthMultiInvalidEapolFramesRx = _Rldot1xAuthMultiInvalidEapolFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 89, 95, 11, 1, 11),
    _Rldot1xAuthMultiInvalidEapolFramesRx_Type()
)
rldot1xAuthMultiInvalidEapolFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1xAuthMultiInvalidEapolFramesRx.setStatus("mandatory")
_Rldot1xAuthMultiEapLengthErrorFramesRx_Type = Counter32
_Rldot1xAuthMultiEapLengthErrorFramesRx_Object = MibTableColumn
rldot1xAuthMultiEapLengthErrorFramesRx = _Rldot1xAuthMultiEapLengthErrorFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 89, 95, 11, 1, 12),
    _Rldot1xAuthMultiEapLengthErrorFramesRx_Type()
)
rldot1xAuthMultiEapLengthErrorFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1xAuthMultiEapLengthErrorFramesRx.setStatus("mandatory")
_Rldot1xAuthMultiDiagTable_Object = MibTable
rldot1xAuthMultiDiagTable = _Rldot1xAuthMultiDiagTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 95, 12)
)
if mibBuilder.loadTexts:
    rldot1xAuthMultiDiagTable.setStatus("mandatory")
_Rldot1xAuthMultiDiagEntry_Object = MibTableRow
rldot1xAuthMultiDiagEntry = _Rldot1xAuthMultiDiagEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 95, 12, 1)
)
rldot1xAuthMultiDiagEntry.setIndexNames(
    (0, "RADLAN-MIB", "rldot1xAuthMultiDiagPortNumber"),
    (0, "RADLAN-MIB", "rldot1xAuthMultiDiagSourceMac"),
)
if mibBuilder.loadTexts:
    rldot1xAuthMultiDiagEntry.setStatus("mandatory")
_Rldot1xAuthMultiDiagPortNumber_Type = Integer32
_Rldot1xAuthMultiDiagPortNumber_Object = MibTableColumn
rldot1xAuthMultiDiagPortNumber = _Rldot1xAuthMultiDiagPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 89, 95, 12, 1, 1),
    _Rldot1xAuthMultiDiagPortNumber_Type()
)
rldot1xAuthMultiDiagPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1xAuthMultiDiagPortNumber.setStatus("mandatory")
_Rldot1xAuthMultiDiagSourceMac_Type = MacAddress
_Rldot1xAuthMultiDiagSourceMac_Object = MibTableColumn
rldot1xAuthMultiDiagSourceMac = _Rldot1xAuthMultiDiagSourceMac_Object(
    (1, 3, 6, 1, 4, 1, 89, 95, 12, 1, 2),
    _Rldot1xAuthMultiDiagSourceMac_Type()
)
rldot1xAuthMultiDiagSourceMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1xAuthMultiDiagSourceMac.setStatus("mandatory")
_Rldot1xAuthMultiEntersConnecting_Type = Counter32
_Rldot1xAuthMultiEntersConnecting_Object = MibTableColumn
rldot1xAuthMultiEntersConnecting = _Rldot1xAuthMultiEntersConnecting_Object(
    (1, 3, 6, 1, 4, 1, 89, 95, 12, 1, 3),
    _Rldot1xAuthMultiEntersConnecting_Type()
)
rldot1xAuthMultiEntersConnecting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1xAuthMultiEntersConnecting.setStatus("mandatory")
_Rldot1xAuthMultiEntersAuthenticating_Type = Counter32
_Rldot1xAuthMultiEntersAuthenticating_Object = MibTableColumn
rldot1xAuthMultiEntersAuthenticating = _Rldot1xAuthMultiEntersAuthenticating_Object(
    (1, 3, 6, 1, 4, 1, 89, 95, 12, 1, 4),
    _Rldot1xAuthMultiEntersAuthenticating_Type()
)
rldot1xAuthMultiEntersAuthenticating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1xAuthMultiEntersAuthenticating.setStatus("mandatory")
_Rldot1xAuthMultiAuthSuccessWhileAuthenticating_Type = Counter32
_Rldot1xAuthMultiAuthSuccessWhileAuthenticating_Object = MibTableColumn
rldot1xAuthMultiAuthSuccessWhileAuthenticating = _Rldot1xAuthMultiAuthSuccessWhileAuthenticating_Object(
    (1, 3, 6, 1, 4, 1, 89, 95, 12, 1, 5),
    _Rldot1xAuthMultiAuthSuccessWhileAuthenticating_Type()
)
rldot1xAuthMultiAuthSuccessWhileAuthenticating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1xAuthMultiAuthSuccessWhileAuthenticating.setStatus("mandatory")
_Rldot1xAuthMultiAuthFailWhileAuthenticating_Type = Counter32
_Rldot1xAuthMultiAuthFailWhileAuthenticating_Object = MibTableColumn
rldot1xAuthMultiAuthFailWhileAuthenticating = _Rldot1xAuthMultiAuthFailWhileAuthenticating_Object(
    (1, 3, 6, 1, 4, 1, 89, 95, 12, 1, 6),
    _Rldot1xAuthMultiAuthFailWhileAuthenticating_Type()
)
rldot1xAuthMultiAuthFailWhileAuthenticating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1xAuthMultiAuthFailWhileAuthenticating.setStatus("mandatory")
_Rldot1xAuthMultiAuthReauthsWhileAuthenticating_Type = Counter32
_Rldot1xAuthMultiAuthReauthsWhileAuthenticating_Object = MibTableColumn
rldot1xAuthMultiAuthReauthsWhileAuthenticating = _Rldot1xAuthMultiAuthReauthsWhileAuthenticating_Object(
    (1, 3, 6, 1, 4, 1, 89, 95, 12, 1, 7),
    _Rldot1xAuthMultiAuthReauthsWhileAuthenticating_Type()
)
rldot1xAuthMultiAuthReauthsWhileAuthenticating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1xAuthMultiAuthReauthsWhileAuthenticating.setStatus("mandatory")
_Rldot1xAuthMultiAuthEapStartsWhileAuthenticating_Type = Counter32
_Rldot1xAuthMultiAuthEapStartsWhileAuthenticating_Object = MibTableColumn
rldot1xAuthMultiAuthEapStartsWhileAuthenticating = _Rldot1xAuthMultiAuthEapStartsWhileAuthenticating_Object(
    (1, 3, 6, 1, 4, 1, 89, 95, 12, 1, 8),
    _Rldot1xAuthMultiAuthEapStartsWhileAuthenticating_Type()
)
rldot1xAuthMultiAuthEapStartsWhileAuthenticating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1xAuthMultiAuthEapStartsWhileAuthenticating.setStatus("mandatory")
_Rldot1xAuthMultiAuthReauthsWhileAuthenticated_Type = Counter32
_Rldot1xAuthMultiAuthReauthsWhileAuthenticated_Object = MibTableColumn
rldot1xAuthMultiAuthReauthsWhileAuthenticated = _Rldot1xAuthMultiAuthReauthsWhileAuthenticated_Object(
    (1, 3, 6, 1, 4, 1, 89, 95, 12, 1, 9),
    _Rldot1xAuthMultiAuthReauthsWhileAuthenticated_Type()
)
rldot1xAuthMultiAuthReauthsWhileAuthenticated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1xAuthMultiAuthReauthsWhileAuthenticated.setStatus("mandatory")
_Rldot1xAuthMultiAuthEapStartsWhileAuthenticated_Type = Counter32
_Rldot1xAuthMultiAuthEapStartsWhileAuthenticated_Object = MibTableColumn
rldot1xAuthMultiAuthEapStartsWhileAuthenticated = _Rldot1xAuthMultiAuthEapStartsWhileAuthenticated_Object(
    (1, 3, 6, 1, 4, 1, 89, 95, 12, 1, 10),
    _Rldot1xAuthMultiAuthEapStartsWhileAuthenticated_Type()
)
rldot1xAuthMultiAuthEapStartsWhileAuthenticated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1xAuthMultiAuthEapStartsWhileAuthenticated.setStatus("mandatory")
_Rldot1xAuthMultiBackendResponses_Type = Counter32
_Rldot1xAuthMultiBackendResponses_Object = MibTableColumn
rldot1xAuthMultiBackendResponses = _Rldot1xAuthMultiBackendResponses_Object(
    (1, 3, 6, 1, 4, 1, 89, 95, 12, 1, 11),
    _Rldot1xAuthMultiBackendResponses_Type()
)
rldot1xAuthMultiBackendResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1xAuthMultiBackendResponses.setStatus("mandatory")
_Rldot1xAuthMultiBackendAccessChallenges_Type = Counter32
_Rldot1xAuthMultiBackendAccessChallenges_Object = MibTableColumn
rldot1xAuthMultiBackendAccessChallenges = _Rldot1xAuthMultiBackendAccessChallenges_Object(
    (1, 3, 6, 1, 4, 1, 89, 95, 12, 1, 12),
    _Rldot1xAuthMultiBackendAccessChallenges_Type()
)
rldot1xAuthMultiBackendAccessChallenges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1xAuthMultiBackendAccessChallenges.setStatus("mandatory")
_Rldot1xAuthMultiBackendOtherRequestsToSupplicant_Type = Counter32
_Rldot1xAuthMultiBackendOtherRequestsToSupplicant_Object = MibTableColumn
rldot1xAuthMultiBackendOtherRequestsToSupplicant = _Rldot1xAuthMultiBackendOtherRequestsToSupplicant_Object(
    (1, 3, 6, 1, 4, 1, 89, 95, 12, 1, 13),
    _Rldot1xAuthMultiBackendOtherRequestsToSupplicant_Type()
)
rldot1xAuthMultiBackendOtherRequestsToSupplicant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1xAuthMultiBackendOtherRequestsToSupplicant.setStatus("mandatory")
_Rldot1xAuthMultiBackendNonNakResponsesFromSupplicant_Type = Counter32
_Rldot1xAuthMultiBackendNonNakResponsesFromSupplicant_Object = MibTableColumn
rldot1xAuthMultiBackendNonNakResponsesFromSupplicant = _Rldot1xAuthMultiBackendNonNakResponsesFromSupplicant_Object(
    (1, 3, 6, 1, 4, 1, 89, 95, 12, 1, 14),
    _Rldot1xAuthMultiBackendNonNakResponsesFromSupplicant_Type()
)
rldot1xAuthMultiBackendNonNakResponsesFromSupplicant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1xAuthMultiBackendNonNakResponsesFromSupplicant.setStatus("mandatory")
_Rldot1xAuthMultiBackendAuthSuccesses_Type = Counter32
_Rldot1xAuthMultiBackendAuthSuccesses_Object = MibTableColumn
rldot1xAuthMultiBackendAuthSuccesses = _Rldot1xAuthMultiBackendAuthSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 89, 95, 12, 1, 15),
    _Rldot1xAuthMultiBackendAuthSuccesses_Type()
)
rldot1xAuthMultiBackendAuthSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1xAuthMultiBackendAuthSuccesses.setStatus("mandatory")
_Rldot1xAuthMultiSessionStatsTable_Object = MibTable
rldot1xAuthMultiSessionStatsTable = _Rldot1xAuthMultiSessionStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 95, 13)
)
if mibBuilder.loadTexts:
    rldot1xAuthMultiSessionStatsTable.setStatus("mandatory")
_Rldot1xAuthMultiSessionStatsEntry_Object = MibTableRow
rldot1xAuthMultiSessionStatsEntry = _Rldot1xAuthMultiSessionStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 95, 13, 1)
)
rldot1xAuthMultiSessionStatsEntry.setIndexNames(
    (0, "RADLAN-MIB", "rldot1xAuthMultiSessionStatsPortNumber"),
    (0, "RADLAN-MIB", "rldot1xAuthMultiSessionStatsSourceMac"),
)
if mibBuilder.loadTexts:
    rldot1xAuthMultiSessionStatsEntry.setStatus("mandatory")
_Rldot1xAuthMultiSessionStatsPortNumber_Type = Integer32
_Rldot1xAuthMultiSessionStatsPortNumber_Object = MibTableColumn
rldot1xAuthMultiSessionStatsPortNumber = _Rldot1xAuthMultiSessionStatsPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 89, 95, 13, 1, 1),
    _Rldot1xAuthMultiSessionStatsPortNumber_Type()
)
rldot1xAuthMultiSessionStatsPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1xAuthMultiSessionStatsPortNumber.setStatus("mandatory")
_Rldot1xAuthMultiSessionStatsSourceMac_Type = MacAddress
_Rldot1xAuthMultiSessionStatsSourceMac_Object = MibTableColumn
rldot1xAuthMultiSessionStatsSourceMac = _Rldot1xAuthMultiSessionStatsSourceMac_Object(
    (1, 3, 6, 1, 4, 1, 89, 95, 13, 1, 2),
    _Rldot1xAuthMultiSessionStatsSourceMac_Type()
)
rldot1xAuthMultiSessionStatsSourceMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1xAuthMultiSessionStatsSourceMac.setStatus("mandatory")
_Rldot1xAuthMultiSessionOctetsRx_Type = Counter64
_Rldot1xAuthMultiSessionOctetsRx_Object = MibTableColumn
rldot1xAuthMultiSessionOctetsRx = _Rldot1xAuthMultiSessionOctetsRx_Object(
    (1, 3, 6, 1, 4, 1, 89, 95, 13, 1, 3),
    _Rldot1xAuthMultiSessionOctetsRx_Type()
)
rldot1xAuthMultiSessionOctetsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1xAuthMultiSessionOctetsRx.setStatus("mandatory")
_Rldot1xAuthMultiSessionOctetsTx_Type = Counter64
_Rldot1xAuthMultiSessionOctetsTx_Object = MibTableColumn
rldot1xAuthMultiSessionOctetsTx = _Rldot1xAuthMultiSessionOctetsTx_Object(
    (1, 3, 6, 1, 4, 1, 89, 95, 13, 1, 4),
    _Rldot1xAuthMultiSessionOctetsTx_Type()
)
rldot1xAuthMultiSessionOctetsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1xAuthMultiSessionOctetsTx.setStatus("mandatory")
_Rldot1xAuthMultiSessionFramesRx_Type = Counter32
_Rldot1xAuthMultiSessionFramesRx_Object = MibTableColumn
rldot1xAuthMultiSessionFramesRx = _Rldot1xAuthMultiSessionFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 89, 95, 13, 1, 5),
    _Rldot1xAuthMultiSessionFramesRx_Type()
)
rldot1xAuthMultiSessionFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1xAuthMultiSessionFramesRx.setStatus("mandatory")
_Rldot1xAuthMultiSessionFramesTx_Type = Counter32
_Rldot1xAuthMultiSessionFramesTx_Object = MibTableColumn
rldot1xAuthMultiSessionFramesTx = _Rldot1xAuthMultiSessionFramesTx_Object(
    (1, 3, 6, 1, 4, 1, 89, 95, 13, 1, 6),
    _Rldot1xAuthMultiSessionFramesTx_Type()
)
rldot1xAuthMultiSessionFramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1xAuthMultiSessionFramesTx.setStatus("mandatory")
_Rldot1xAuthMultiSessionId_Type = SnmpAdminString
_Rldot1xAuthMultiSessionId_Object = MibTableColumn
rldot1xAuthMultiSessionId = _Rldot1xAuthMultiSessionId_Object(
    (1, 3, 6, 1, 4, 1, 89, 95, 13, 1, 7),
    _Rldot1xAuthMultiSessionId_Type()
)
rldot1xAuthMultiSessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1xAuthMultiSessionId.setStatus("mandatory")
_Rldot1xAuthMultiSessionTime_Type = TimeTicks
_Rldot1xAuthMultiSessionTime_Object = MibTableColumn
rldot1xAuthMultiSessionTime = _Rldot1xAuthMultiSessionTime_Object(
    (1, 3, 6, 1, 4, 1, 89, 95, 13, 1, 8),
    _Rldot1xAuthMultiSessionTime_Type()
)
rldot1xAuthMultiSessionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1xAuthMultiSessionTime.setStatus("mandatory")
_Rldot1xAuthMultiSessionUserName_Type = SnmpAdminString
_Rldot1xAuthMultiSessionUserName_Object = MibTableColumn
rldot1xAuthMultiSessionUserName = _Rldot1xAuthMultiSessionUserName_Object(
    (1, 3, 6, 1, 4, 1, 89, 95, 13, 1, 9),
    _Rldot1xAuthMultiSessionUserName_Type()
)
rldot1xAuthMultiSessionUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1xAuthMultiSessionUserName.setStatus("mandatory")
_Rldot1xAuthMultiConfigTable_Object = MibTable
rldot1xAuthMultiConfigTable = _Rldot1xAuthMultiConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 95, 14)
)
if mibBuilder.loadTexts:
    rldot1xAuthMultiConfigTable.setStatus("mandatory")
_Rldot1xAuthMultiConfigEntry_Object = MibTableRow
rldot1xAuthMultiConfigEntry = _Rldot1xAuthMultiConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 95, 14, 1)
)
rldot1xAuthMultiConfigEntry.setIndexNames(
    (0, "RADLAN-MIB", "rldot1xAuthMultiPortNumber"),
    (0, "RADLAN-MIB", "rldot1xAuthMultiSourceMac"),
)
if mibBuilder.loadTexts:
    rldot1xAuthMultiConfigEntry.setStatus("mandatory")
_Rldot1xAuthMultiPortNumber_Type = Integer32
_Rldot1xAuthMultiPortNumber_Object = MibTableColumn
rldot1xAuthMultiPortNumber = _Rldot1xAuthMultiPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 89, 95, 14, 1, 1),
    _Rldot1xAuthMultiPortNumber_Type()
)
rldot1xAuthMultiPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1xAuthMultiPortNumber.setStatus("mandatory")
_Rldot1xAuthMultiSourceMac_Type = MacAddress
_Rldot1xAuthMultiSourceMac_Object = MibTableColumn
rldot1xAuthMultiSourceMac = _Rldot1xAuthMultiSourceMac_Object(
    (1, 3, 6, 1, 4, 1, 89, 95, 14, 1, 2),
    _Rldot1xAuthMultiSourceMac_Type()
)
rldot1xAuthMultiSourceMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1xAuthMultiSourceMac.setStatus("mandatory")


class _Rldot1xAuthMultiPaeState_Type(Integer32):
    """Custom type rldot1xAuthMultiPaeState based on Integer32"""
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
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("aborting", 6),
          ("authenticated", 5),
          ("authenticating", 4),
          ("connecting", 3),
          ("disconnected", 2),
          ("forceAuth", 8),
          ("forceUnauth", 9),
          ("held", 7),
          ("initialize", 1))
    )


_Rldot1xAuthMultiPaeState_Type.__name__ = "Integer32"
_Rldot1xAuthMultiPaeState_Object = MibTableColumn
rldot1xAuthMultiPaeState = _Rldot1xAuthMultiPaeState_Object(
    (1, 3, 6, 1, 4, 1, 89, 95, 14, 1, 3),
    _Rldot1xAuthMultiPaeState_Type()
)
rldot1xAuthMultiPaeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1xAuthMultiPaeState.setStatus("mandatory")


class _Rldot1xAuthMultiBackendAuthState_Type(Integer32):
    """Custom type rldot1xAuthMultiBackendAuthState based on Integer32"""
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
        *(("fail", 4),
          ("idle", 6),
          ("initialize", 7),
          ("request", 1),
          ("response", 2),
          ("success", 3),
          ("timeout", 5))
    )


_Rldot1xAuthMultiBackendAuthState_Type.__name__ = "Integer32"
_Rldot1xAuthMultiBackendAuthState_Object = MibTableColumn
rldot1xAuthMultiBackendAuthState = _Rldot1xAuthMultiBackendAuthState_Object(
    (1, 3, 6, 1, 4, 1, 89, 95, 14, 1, 4),
    _Rldot1xAuthMultiBackendAuthState_Type()
)
rldot1xAuthMultiBackendAuthState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1xAuthMultiBackendAuthState.setStatus("mandatory")
_Rldot1xAuthMultiControlledPortStatus_Type = PaeControlledPortStatus
_Rldot1xAuthMultiControlledPortStatus_Object = MibTableColumn
rldot1xAuthMultiControlledPortStatus = _Rldot1xAuthMultiControlledPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 95, 14, 1, 5),
    _Rldot1xAuthMultiControlledPortStatus_Type()
)
rldot1xAuthMultiControlledPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1xAuthMultiControlledPortStatus.setStatus("mandatory")
_Rldot1xBpduFilteringEnabled_Type = TruthValue
_Rldot1xBpduFilteringEnabled_Object = MibScalar
rldot1xBpduFilteringEnabled = _Rldot1xBpduFilteringEnabled_Object(
    (1, 3, 6, 1, 4, 1, 89, 95, 15),
    _Rldot1xBpduFilteringEnabled_Type()
)
rldot1xBpduFilteringEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rldot1xBpduFilteringEnabled.setStatus("mandatory")
_RlFile_ObjectIdentity = ObjectIdentity
rlFile = _RlFile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 96)
)
_RlAAAEap_ObjectIdentity = ObjectIdentity
rlAAAEap = _RlAAAEap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 97)
)
_RlSNMP_ObjectIdentity = ObjectIdentity
rlSNMP = _RlSNMP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 98)
)
_RlSsl_ObjectIdentity = ObjectIdentity
rlSsl = _RlSsl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 100)
)
_RlMacBasePrio_ObjectIdentity = ObjectIdentity
rlMacBasePrio = _RlMacBasePrio_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 101)
)
_RlWlanAccessPoint_ObjectIdentity = ObjectIdentity
rlWlanAccessPoint = _RlWlanAccessPoint_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 102)
)
_RlLocalization_ObjectIdentity = ObjectIdentity
rlLocalization = _RlLocalization_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 103)
)
_RlRs232_ObjectIdentity = ObjectIdentity
rlRs232 = _RlRs232_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 104)
)
_RlNicRedundancy_ObjectIdentity = ObjectIdentity
rlNicRedundancy = _RlNicRedundancy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 105)
)
_RlAmap_ObjectIdentity = ObjectIdentity
rlAmap = _RlAmap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 106)
)
_RlStack_ObjectIdentity = ObjectIdentity
rlStack = _RlStack_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 107)
)
_RlPoe_ObjectIdentity = ObjectIdentity
rlPoe = _RlPoe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 108)
)
_RlUPnP_ObjectIdentity = ObjectIdentity
rlUPnP = _RlUPnP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 109)
)
_RlLldp_ObjectIdentity = ObjectIdentity
rlLldp = _RlLldp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 110)
)
_RlOib_ObjectIdentity = ObjectIdentity
rlOib = _RlOib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 111)
)
_RlBridgeSecurity_ObjectIdentity = ObjectIdentity
rlBridgeSecurity = _RlBridgeSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 112)
)
_RlDhcpSpoofing_ObjectIdentity = ObjectIdentity
rlDhcpSpoofing = _RlDhcpSpoofing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 113)
)
_RlBonjour_ObjectIdentity = ObjectIdentity
rlBonjour = _RlBonjour_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 114)
)
_RlLinksysSmartMIB_ObjectIdentity = ObjectIdentity
rlLinksysSmartMIB = _RlLinksysSmartMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 115)
)
_RlBrgMulticast_ObjectIdentity = ObjectIdentity
rlBrgMulticast = _RlBrgMulticast_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 116)
)
_RlBrgMcMngr_ObjectIdentity = ObjectIdentity
rlBrgMcMngr = _RlBrgMcMngr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 117)
)
_RlGlobalIpAddrTable_ObjectIdentity = ObjectIdentity
rlGlobalIpAddrTable = _RlGlobalIpAddrTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 118)
)
_DlPrivate_ObjectIdentity = ObjectIdentity
dlPrivate = _DlPrivate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 119)
)
_RlSecuritySuiteMib_ObjectIdentity = ObjectIdentity
rlSecuritySuiteMib = _RlSecuritySuiteMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 120)
)
_RlIntel_ObjectIdentity = ObjectIdentity
rlIntel = _RlIntel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 121)
)
_RlAutoUpdate_ObjectIdentity = ObjectIdentity
rlAutoUpdate = _RlAutoUpdate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 123)
)
_RlCpuCounters_ObjectIdentity = ObjectIdentity
rlCpuCounters = _RlCpuCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 124)
)
_RlWlanMIB_ObjectIdentity = ObjectIdentity
rlWlanMIB = _RlWlanMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 200)
)
_RndEndOfMibGroup_ObjectIdentity = ObjectIdentity
rndEndOfMibGroup = _RndEndOfMibGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 1000)
)
_RndEndOfMib_Type = Integer32
_RndEndOfMib_Object = MibScalar
rndEndOfMib = _RndEndOfMib_Object(
    (1, 3, 6, 1, 4, 1, 89, 1000, 1),
    _RndEndOfMib_Type()
)
rndEndOfMib.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rndEndOfMib.setStatus("mandatory")
dot1xAuthSessionStatsEntry.registerAugmentions(
    ("RADLAN-MIB",
     "rldot1xExtAuthSessionStatsEntry")
)
rldot1xExtAuthSessionStatsEntry.setIndexNames(*dot1xAuthSessionStatsEntry.getIndexNames())

# Managed Objects groups


# Notification objects

rxOverflowHWFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 3)
)
rxOverflowHWFault.setObjects(
      *(("RADLAN-MIB", "rndErrorDesc"),
        ("RADLAN-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rxOverflowHWFault.setStatus(
        ""
    )

txOverflowHWFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 4)
)
txOverflowHWFault.setObjects(
      *(("RADLAN-MIB", "rndErrorDesc"),
        ("RADLAN-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    txOverflowHWFault.setStatus(
        ""
    )

routeTableOverflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 5)
)
routeTableOverflow.setObjects(
      *(("RADLAN-MIB", "rndErrorDesc"),
        ("RADLAN-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    routeTableOverflow.setStatus(
        ""
    )

resetRequired = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 10)
)
resetRequired.setObjects(
      *(("RADLAN-MIB", "rndErrorDesc"),
        ("RADLAN-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    resetRequired.setStatus(
        ""
    )

endTftp = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 12)
)
endTftp.setObjects(
      *(("RADLAN-MIB", "rndErrorDesc"),
        ("RADLAN-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    endTftp.setStatus(
        ""
    )

abortTftp = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 13)
)
abortTftp.setObjects(
      *(("RADLAN-MIB", "rndErrorDesc"),
        ("RADLAN-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    abortTftp.setStatus(
        ""
    )

startTftp = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 14)
)
startTftp.setObjects(
      *(("RADLAN-MIB", "rndErrorDesc"),
        ("RADLAN-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    startTftp.setStatus(
        ""
    )

faultBackUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 23)
)
faultBackUp.setObjects(
      *(("RADLAN-MIB", "rndErrorDesc"),
        ("RADLAN-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    faultBackUp.setStatus(
        ""
    )

mainLinkUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 24)
)
mainLinkUp.setObjects(
      *(("RADLAN-MIB", "rndErrorDesc"),
        ("RADLAN-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    mainLinkUp.setStatus(
        ""
    )

ipxRipTblOverflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 36)
)
ipxRipTblOverflow.setObjects(
      *(("RADLAN-MIB", "rndErrorDesc"),
        ("RADLAN-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    ipxRipTblOverflow.setStatus(
        ""
    )

ipxSapTblOverflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 37)
)
ipxSapTblOverflow.setObjects(
      *(("RADLAN-MIB", "rndErrorDesc"),
        ("RADLAN-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    ipxSapTblOverflow.setStatus(
        ""
    )

facsAccessVoilation = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 49)
)
facsAccessVoilation.setObjects(
      *(("RADLAN-MIB", "rndErrorDesc"),
        ("RADLAN-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    facsAccessVoilation.setStatus(
        ""
    )

autoConfigurationCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 50)
)
autoConfigurationCompleted.setObjects(
      *(("RADLAN-MIB", "rndErrorDesc"),
        ("RADLAN-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    autoConfigurationCompleted.setStatus(
        ""
    )

forwardingTabOverflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 51)
)
forwardingTabOverflow.setObjects(
      *(("RADLAN-MIB", "rndErrorDesc"),
        ("RADLAN-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    forwardingTabOverflow.setStatus(
        ""
    )

framRelaySwitchConnectionUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 53)
)
framRelaySwitchConnectionUp.setObjects(
      *(("RADLAN-MIB", "rndErrorDesc"),
        ("RADLAN-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    framRelaySwitchConnectionUp.setStatus(
        ""
    )

framRelaySwitchConnectionDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 54)
)
framRelaySwitchConnectionDown.setObjects(
      *(("RADLAN-MIB", "rndErrorDesc"),
        ("RADLAN-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    framRelaySwitchConnectionDown.setStatus(
        ""
    )

errorsDuringInit = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 61)
)
errorsDuringInit.setObjects(
      *(("RADLAN-MIB", "rndErrorDesc"),
        ("RADLAN-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    errorsDuringInit.setStatus(
        ""
    )

vlanDynPortAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 66)
)
vlanDynPortAdded.setObjects(
      *(("RADLAN-MIB", "rndErrorDesc"),
        ("RADLAN-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    vlanDynPortAdded.setStatus(
        ""
    )

vlanDynPortRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 67)
)
vlanDynPortRemoved.setObjects(
      *(("RADLAN-MIB", "rndErrorDesc"),
        ("RADLAN-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    vlanDynPortRemoved.setStatus(
        ""
    )

rsSDclientsTableOverflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 68)
)
rsSDclientsTableOverflow.setObjects(
      *(("RADLAN-MIB", "rndErrorDesc"),
        ("RADLAN-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rsSDclientsTableOverflow.setStatus(
        ""
    )

rsSDinactiveServer = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 69)
)
rsSDinactiveServer.setObjects(
      *(("RADLAN-MIB", "rndErrorDesc"),
        ("RADLAN-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rsSDinactiveServer.setStatus(
        ""
    )

rsIpZhrConnectionsTableOverflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 70)
)
rsIpZhrConnectionsTableOverflow.setObjects(
      *(("RADLAN-MIB", "rndErrorDesc"),
        ("RADLAN-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rsIpZhrConnectionsTableOverflow.setStatus(
        ""
    )

rsIpZhrReqStaticConnNotAccepted = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 71)
)
rsIpZhrReqStaticConnNotAccepted.setObjects(
      *(("RADLAN-MIB", "rndErrorDesc"),
        ("RADLAN-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rsIpZhrReqStaticConnNotAccepted.setStatus(
        ""
    )

rsIpZhrVirtualIpAsSource = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 72)
)
rsIpZhrVirtualIpAsSource.setObjects(
      *(("RADLAN-MIB", "rndErrorDesc"),
        ("RADLAN-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rsIpZhrVirtualIpAsSource.setStatus(
        ""
    )

rsIpZhrNotAllocVirtualIp = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 73)
)
rsIpZhrNotAllocVirtualIp.setObjects(
      *(("RADLAN-MIB", "rndErrorDesc"),
        ("RADLAN-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rsIpZhrNotAllocVirtualIp.setStatus(
        ""
    )

rsSnmpSetRequestInSpecialCfgState = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 74)
)
rsSnmpSetRequestInSpecialCfgState.setObjects(
      *(("RADLAN-MIB", "rndErrorDesc"),
        ("RADLAN-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rsSnmpSetRequestInSpecialCfgState.setStatus(
        ""
    )

rsPingCompletion = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 136)
)
rsPingCompletion.setObjects(
      *(("RADLAN-MIB", "rndErrorDesc"),
        ("RADLAN-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rsPingCompletion.setStatus(
        ""
    )

pppSecurityViolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 137)
)
pppSecurityViolation.setObjects(
      *(("RADLAN-MIB", "rndErrorDesc"),
        ("RADLAN-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    pppSecurityViolation.setStatus(
        ""
    )

frDLCIStatudChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 138)
)
frDLCIStatudChange.setObjects(
      *(("RADLAN-MIB", "rndErrorDesc"),
        ("RADLAN-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    frDLCIStatudChange.setStatus(
        ""
    )

papFailedCommunication = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 139)
)
papFailedCommunication.setObjects(
      *(("RADLAN-MIB", "rndErrorDesc"),
        ("RADLAN-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    papFailedCommunication.setStatus(
        ""
    )

chapFailedCommunication = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 140)
)
chapFailedCommunication.setObjects(
      *(("RADLAN-MIB", "rndErrorDesc"),
        ("RADLAN-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    chapFailedCommunication.setStatus(
        ""
    )

rsWSDRedundancySwitch = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 141)
)
rsWSDRedundancySwitch.setObjects(
      *(("RADLAN-MIB", "rndErrorDesc"),
        ("RADLAN-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rsWSDRedundancySwitch.setStatus(
        ""
    )

rsDhcpAllocationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 142)
)
rsDhcpAllocationFailure.setObjects(
      *(("RADLAN-MIB", "rndErrorDesc"),
        ("RADLAN-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rsDhcpAllocationFailure.setStatus(
        ""
    )

rlIpFftStnOverflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 145)
)
rlIpFftStnOverflow.setObjects(
      *(("RADLAN-MIB", "rndErrorDesc"),
        ("RADLAN-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rlIpFftStnOverflow.setStatus(
        ""
    )

rlIpFftSubOverflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 146)
)
rlIpFftSubOverflow.setObjects(
      *(("RADLAN-MIB", "rndErrorDesc"),
        ("RADLAN-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rlIpFftSubOverflow.setStatus(
        ""
    )

rlIpxFftStnOverflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 147)
)
rlIpxFftStnOverflow.setObjects(
      *(("RADLAN-MIB", "rndErrorDesc"),
        ("RADLAN-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rlIpxFftStnOverflow.setStatus(
        ""
    )

rlIpxFftSubOverflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 148)
)
rlIpxFftSubOverflow.setObjects(
      *(("RADLAN-MIB", "rndErrorDesc"),
        ("RADLAN-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rlIpxFftSubOverflow.setStatus(
        ""
    )

rlIpmFftOverflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 149)
)
rlIpmFftOverflow.setObjects(
      *(("RADLAN-MIB", "rndErrorDesc"),
        ("RADLAN-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rlIpmFftOverflow.setStatus(
        ""
    )

rlPhysicalDescriptionChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 150)
)
rlPhysicalDescriptionChanged.setObjects(
      *(("RADLAN-MIB", "rndErrorDesc"),
        ("RADLAN-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rlPhysicalDescriptionChanged.setStatus(
        ""
    )

rldot1dStpPortStateForwarding = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 151)
)
rldot1dStpPortStateForwarding.setObjects(
      *(("RADLAN-MIB", "rndErrorDesc"),
        ("RADLAN-MIB", "rndErrorSeverity"),
        ("RADLAN-MIB", "rldot1dStpTrapVrblifIndex"),
        ("RADLAN-MIB", "rldot1dStpTrapVrblVID"))
)
if mibBuilder.loadTexts:
    rldot1dStpPortStateForwarding.setStatus(
        ""
    )

rldot1dStpPortStateNotForwarding = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 152)
)
rldot1dStpPortStateNotForwarding.setObjects(
      *(("RADLAN-MIB", "rndErrorDesc"),
        ("RADLAN-MIB", "rndErrorSeverity"),
        ("RADLAN-MIB", "rldot1dStpTrapVrblifIndex"),
        ("RADLAN-MIB", "rldot1dStpTrapVrblVID"))
)
if mibBuilder.loadTexts:
    rldot1dStpPortStateNotForwarding.setStatus(
        ""
    )

rlPolicyDropPacketTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 153)
)
rlPolicyDropPacketTrap.setObjects(
      *(("RADLAN-MIB", "rndErrorDesc"),
        ("RADLAN-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rlPolicyDropPacketTrap.setStatus(
        ""
    )

rlPolicyForwardPacketTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 154)
)
rlPolicyForwardPacketTrap.setObjects(
      *(("RADLAN-MIB", "rndErrorDesc"),
        ("RADLAN-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rlPolicyForwardPacketTrap.setStatus(
        ""
    )

rlIgmpProxyTableOverflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 156)
)
rlIgmpProxyTableOverflow.setObjects(
      *(("RADLAN-MIB", "rndErrorDesc"),
        ("RADLAN-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rlIgmpProxyTableOverflow.setStatus(
        ""
    )

rlIgmpV1MsgReceived = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 157)
)
rlIgmpV1MsgReceived.setObjects(
      *(("RADLAN-MIB", "rndErrorDesc"),
        ("RADLAN-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rlIgmpV1MsgReceived.setStatus(
        ""
    )

rlVrrpEntriesDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 158)
)
rlVrrpEntriesDeleted.setObjects(
      *(("RADLAN-MIB", "rndErrorDesc"),
        ("RADLAN-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rlVrrpEntriesDeleted.setStatus(
        ""
    )

rlHotSwapTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 159)
)
rlHotSwapTrap.setObjects(
      *(("RADLAN-MIB", "rndErrorDesc"),
        ("RADLAN-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rlHotSwapTrap.setStatus(
        ""
    )

rlTrunkPortAddedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 160)
)
rlTrunkPortAddedTrap.setObjects(
      *(("RADLAN-MIB", "rndErrorDesc"),
        ("RADLAN-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rlTrunkPortAddedTrap.setStatus(
        ""
    )

rlTrunkPortRemovedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 161)
)
rlTrunkPortRemovedTrap.setObjects(
      *(("RADLAN-MIB", "rndErrorDesc"),
        ("RADLAN-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rlTrunkPortRemovedTrap.setStatus(
        ""
    )

rlTrunkPortNotCapableTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 162)
)
rlTrunkPortNotCapableTrap.setObjects(
      *(("RADLAN-MIB", "rndErrorDesc"),
        ("RADLAN-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rlTrunkPortNotCapableTrap.setStatus(
        ""
    )

rlLockPortTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 170)
)
rlLockPortTrap.setObjects(
      *(("RADLAN-MIB", "rndErrorDesc"),
        ("RADLAN-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rlLockPortTrap.setStatus(
        ""
    )

vlanDynVlanAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 171)
)
vlanDynVlanAdded.setObjects(
      *(("RADLAN-MIB", "rndErrorDesc"),
        ("RADLAN-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    vlanDynVlanAdded.setStatus(
        ""
    )

vlanDynVlanRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 172)
)
vlanDynVlanRemoved.setObjects(
      *(("RADLAN-MIB", "rndErrorDesc"),
        ("RADLAN-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    vlanDynVlanRemoved.setStatus(
        ""
    )

vlanDynamicToStatic = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 173)
)
vlanDynamicToStatic.setObjects(
      *(("RADLAN-MIB", "rndErrorDesc"),
        ("RADLAN-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    vlanDynamicToStatic.setStatus(
        ""
    )

vlanStaticToDynamic = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 174)
)
vlanStaticToDynamic.setObjects(
      *(("RADLAN-MIB", "rndErrorDesc"),
        ("RADLAN-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    vlanStaticToDynamic.setStatus(
        ""
    )

dstrSysLog = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 175)
)
dstrSysLog.setObjects(
      *(("RADLAN-MIB", "rndErrorDesc"),
        ("RADLAN-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    dstrSysLog.setStatus(
        ""
    )

rlEnvMonFanStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 176)
)
rlEnvMonFanStateChange.setObjects(
      *(("RADLAN-MIB", "rndErrorDesc"),
        ("RADLAN-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rlEnvMonFanStateChange.setStatus(
        ""
    )

rlEnvMonPowerSupplyStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 177)
)
rlEnvMonPowerSupplyStateChange.setObjects(
      *(("RADLAN-MIB", "rndErrorDesc"),
        ("RADLAN-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rlEnvMonPowerSupplyStateChange.setStatus(
        ""
    )

rlStackStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 178)
)
rlStackStateChange.setObjects(
      *(("RADLAN-MIB", "rndErrorDesc"),
        ("RADLAN-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rlStackStateChange.setStatus(
        ""
    )

rlEnvMonTemperatureRisingAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 179)
)
rlEnvMonTemperatureRisingAlarm.setObjects(
      *(("RADLAN-MIB", "rndErrorDesc"),
        ("RADLAN-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rlEnvMonTemperatureRisingAlarm.setStatus(
        ""
    )

rlBrgMacAddFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 183)
)
rlBrgMacAddFailedTrap.setObjects(
      *(("RADLAN-MIB", "rndErrorDesc"),
        ("RADLAN-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rlBrgMacAddFailedTrap.setStatus(
        ""
    )

rldot1xPortStatusAuthorizedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 184)
)
rldot1xPortStatusAuthorizedTrap.setObjects(
      *(("RADLAN-MIB", "rndErrorDesc"),
        ("RADLAN-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rldot1xPortStatusAuthorizedTrap.setStatus(
        ""
    )

rldot1xPortStatusUnauthorizedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 185)
)
rldot1xPortStatusUnauthorizedTrap.setObjects(
      *(("RADLAN-MIB", "rndErrorDesc"),
        ("RADLAN-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rldot1xPortStatusUnauthorizedTrap.setStatus(
        ""
    )

swIfTablePortLock = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 192)
)
swIfTablePortLock.setObjects(
      *(("RADLAN-MIB", "rndErrorDesc"),
        ("RADLAN-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    swIfTablePortLock.setStatus(
        ""
    )

swIfTablePortUnLock = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 193)
)
swIfTablePortUnLock.setObjects(
      *(("RADLAN-MIB", "rndErrorDesc"),
        ("RADLAN-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    swIfTablePortUnLock.setStatus(
        ""
    )

rlAAAUserLocked = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 194)
)
rlAAAUserLocked.setObjects(
      *(("RADLAN-MIB", "rndErrorDesc"),
        ("RADLAN-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rlAAAUserLocked.setStatus(
        ""
    )

bpduGuardPortSuspended = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 202)
)
bpduGuardPortSuspended.setObjects(
      *(("RADLAN-MIB", "rndErrorDesc"),
        ("RADLAN-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    bpduGuardPortSuspended.setStatus(
        ""
    )

rldot1xSupplicantMacAuthorizedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 203)
)
rldot1xSupplicantMacAuthorizedTrap.setObjects(
      *(("RADLAN-MIB", "rndErrorDesc"),
        ("RADLAN-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rldot1xSupplicantMacAuthorizedTrap.setStatus(
        ""
    )

rldot1xSupplicantMacUnauthorizedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 204)
)
rldot1xSupplicantMacUnauthorizedTrap.setObjects(
      *(("RADLAN-MIB", "rndErrorDesc"),
        ("RADLAN-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rldot1xSupplicantMacUnauthorizedTrap.setStatus(
        ""
    )

stpLoopbackDetection = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 205)
)
stpLoopbackDetection.setObjects(
      *(("RADLAN-MIB", "rndErrorDesc"),
        ("RADLAN-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    stpLoopbackDetection.setStatus(
        ""
    )

stpLoopbackDetectionResolved = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 206)
)
stpLoopbackDetectionResolved.setObjects(
      *(("RADLAN-MIB", "rndErrorDesc"),
        ("RADLAN-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    stpLoopbackDetectionResolved.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RADLAN-MIB",
    **{"Percents": Percents,
       "NetNumber": NetNumber,
       "VlanPriority": VlanPriority,
       "RlStormCtrlRateUnit": RlStormCtrlRateUnit,
       "rnd": rnd,
       "rndNotifications": rndNotifications,
       "rxOverflowHWFault": rxOverflowHWFault,
       "txOverflowHWFault": txOverflowHWFault,
       "routeTableOverflow": routeTableOverflow,
       "resetRequired": resetRequired,
       "endTftp": endTftp,
       "abortTftp": abortTftp,
       "startTftp": startTftp,
       "faultBackUp": faultBackUp,
       "mainLinkUp": mainLinkUp,
       "ipxRipTblOverflow": ipxRipTblOverflow,
       "ipxSapTblOverflow": ipxSapTblOverflow,
       "facsAccessVoilation": facsAccessVoilation,
       "autoConfigurationCompleted": autoConfigurationCompleted,
       "forwardingTabOverflow": forwardingTabOverflow,
       "framRelaySwitchConnectionUp": framRelaySwitchConnectionUp,
       "framRelaySwitchConnectionDown": framRelaySwitchConnectionDown,
       "errorsDuringInit": errorsDuringInit,
       "vlanDynPortAdded": vlanDynPortAdded,
       "vlanDynPortRemoved": vlanDynPortRemoved,
       "rsSDclientsTableOverflow": rsSDclientsTableOverflow,
       "rsSDinactiveServer": rsSDinactiveServer,
       "rsIpZhrConnectionsTableOverflow": rsIpZhrConnectionsTableOverflow,
       "rsIpZhrReqStaticConnNotAccepted": rsIpZhrReqStaticConnNotAccepted,
       "rsIpZhrVirtualIpAsSource": rsIpZhrVirtualIpAsSource,
       "rsIpZhrNotAllocVirtualIp": rsIpZhrNotAllocVirtualIp,
       "rsSnmpSetRequestInSpecialCfgState": rsSnmpSetRequestInSpecialCfgState,
       "rsPingCompletion": rsPingCompletion,
       "pppSecurityViolation": pppSecurityViolation,
       "frDLCIStatudChange": frDLCIStatudChange,
       "papFailedCommunication": papFailedCommunication,
       "chapFailedCommunication": chapFailedCommunication,
       "rsWSDRedundancySwitch": rsWSDRedundancySwitch,
       "rsDhcpAllocationFailure": rsDhcpAllocationFailure,
       "rlIpFftStnOverflow": rlIpFftStnOverflow,
       "rlIpFftSubOverflow": rlIpFftSubOverflow,
       "rlIpxFftStnOverflow": rlIpxFftStnOverflow,
       "rlIpxFftSubOverflow": rlIpxFftSubOverflow,
       "rlIpmFftOverflow": rlIpmFftOverflow,
       "rlPhysicalDescriptionChanged": rlPhysicalDescriptionChanged,
       "rldot1dStpPortStateForwarding": rldot1dStpPortStateForwarding,
       "rldot1dStpPortStateNotForwarding": rldot1dStpPortStateNotForwarding,
       "rlPolicyDropPacketTrap": rlPolicyDropPacketTrap,
       "rlPolicyForwardPacketTrap": rlPolicyForwardPacketTrap,
       "rlIgmpProxyTableOverflow": rlIgmpProxyTableOverflow,
       "rlIgmpV1MsgReceived": rlIgmpV1MsgReceived,
       "rlVrrpEntriesDeleted": rlVrrpEntriesDeleted,
       "rlHotSwapTrap": rlHotSwapTrap,
       "rlTrunkPortAddedTrap": rlTrunkPortAddedTrap,
       "rlTrunkPortRemovedTrap": rlTrunkPortRemovedTrap,
       "rlTrunkPortNotCapableTrap": rlTrunkPortNotCapableTrap,
       "rlLockPortTrap": rlLockPortTrap,
       "vlanDynVlanAdded": vlanDynVlanAdded,
       "vlanDynVlanRemoved": vlanDynVlanRemoved,
       "vlanDynamicToStatic": vlanDynamicToStatic,
       "vlanStaticToDynamic": vlanStaticToDynamic,
       "dstrSysLog": dstrSysLog,
       "rlEnvMonFanStateChange": rlEnvMonFanStateChange,
       "rlEnvMonPowerSupplyStateChange": rlEnvMonPowerSupplyStateChange,
       "rlStackStateChange": rlStackStateChange,
       "rlEnvMonTemperatureRisingAlarm": rlEnvMonTemperatureRisingAlarm,
       "rlBrgMacAddFailedTrap": rlBrgMacAddFailedTrap,
       "rldot1xPortStatusAuthorizedTrap": rldot1xPortStatusAuthorizedTrap,
       "rldot1xPortStatusUnauthorizedTrap": rldot1xPortStatusUnauthorizedTrap,
       "swIfTablePortLock": swIfTablePortLock,
       "swIfTablePortUnLock": swIfTablePortUnLock,
       "rlAAAUserLocked": rlAAAUserLocked,
       "bpduGuardPortSuspended": bpduGuardPortSuspended,
       "rldot1xSupplicantMacAuthorizedTrap": rldot1xSupplicantMacAuthorizedTrap,
       "rldot1xSupplicantMacUnauthorizedTrap": rldot1xSupplicantMacUnauthorizedTrap,
       "stpLoopbackDetection": stpLoopbackDetection,
       "stpLoopbackDetectionResolved": stpLoopbackDetectionResolved,
       "rndMng": rndMng,
       "rndDeviceParams": rndDeviceParams,
       "rndBridgeType": rndBridgeType,
       "rndInactiveArpTimeOut": rndInactiveArpTimeOut,
       "rndBridgeAlarm": rndBridgeAlarm,
       "rndErrorDesc": rndErrorDesc,
       "rndErrorSeverity": rndErrorSeverity,
       "rndBrgVersion": rndBrgVersion,
       "rndBrgFeatures": rndBrgFeatures,
       "rndBrgLicense": rndBrgLicense,
       "rndIpHost": rndIpHost,
       "rndCommunityTable": rndCommunityTable,
       "rndCommunityEntry": rndCommunityEntry,
       "rndCommunityMngStationAddr": rndCommunityMngStationAddr,
       "rndCommunityString": rndCommunityString,
       "rndCommunityAccess": rndCommunityAccess,
       "rndCommunityTrapsEnable": rndCommunityTrapsEnable,
       "rndCommunityStatus": rndCommunityStatus,
       "rndCommunityPortSecurity": rndCommunityPortSecurity,
       "rndCommunityOwner": rndCommunityOwner,
       "rndCommunityTrapDestPort": rndCommunityTrapDestPort,
       "rlMridTable": rlMridTable,
       "rlMridEntry": rlMridEntry,
       "rlMridConnection": rlMridConnection,
       "rlManagedMrid": rlManagedMrid,
       "rndIpHostManagement": rndIpHostManagement,
       "rndIpHostManagementSupported": rndIpHostManagementSupported,
       "rndIpHostManagementIfIndex": rndIpHostManagementIfIndex,
       "rndManagedTime": rndManagedTime,
       "rndManagedDate": rndManagedDate,
       "rndBaseBootVersion": rndBaseBootVersion,
       "genGroup": genGroup,
       "genGroupHWVersion": genGroupHWVersion,
       "genGroupConfigurationSymbol": genGroupConfigurationSymbol,
       "genGroupHWStatus": genGroupHWStatus,
       "rndBasePhysicalAddress": rndBasePhysicalAddress,
       "rndSoftwareFile": rndSoftwareFile,
       "rndActiveSoftwareFileTable": rndActiveSoftwareFileTable,
       "rndActiveSoftwareFileEntry": rndActiveSoftwareFileEntry,
       "rndUnitNumber": rndUnitNumber,
       "rndActiveSoftwareFile": rndActiveSoftwareFile,
       "rndActiveSoftwareFileAfterReset": rndActiveSoftwareFileAfterReset,
       "rndImageSize": rndImageSize,
       "rndBackupConfigurationEnabled": rndBackupConfigurationEnabled,
       "rndImageInfo": rndImageInfo,
       "rndImageInfoTable": rndImageInfoTable,
       "rndImageInfoEntry": rndImageInfoEntry,
       "rndStackUnitNumber": rndStackUnitNumber,
       "rndImage1Name": rndImage1Name,
       "rndImage2Name": rndImage2Name,
       "rndImage1Version": rndImage1Version,
       "rndImage2Version": rndImage2Version,
       "rndImage1Date": rndImage1Date,
       "rndImage2Date": rndImage2Date,
       "rndImage1Time": rndImage1Time,
       "rndImage2Time": rndImage2Time,
       "rndBootP": rndBootP,
       "rndBootPServerAddress": rndBootPServerAddress,
       "rndBootPRelaySecThreshold": rndBootPRelaySecThreshold,
       "ipSpec": ipSpec,
       "rsTunning": rsTunning,
       "rndApplications": rndApplications,
       "rsUDP": rsUDP,
       "swInterfaces": swInterfaces,
       "rlIPmulticast": rlIPmulticast,
       "rlFFT": rlFFT,
       "vlan": vlan,
       "rlRmonControl": rlRmonControl,
       "rlBrgMacSwitch": rlBrgMacSwitch,
       "rlBrgMacSwVersion": rlBrgMacSwVersion,
       "rlBrgMacSwMaxTableNumber": rlBrgMacSwMaxTableNumber,
       "rlBrgMacSwDynamicTables": rlBrgMacSwDynamicTables,
       "rlBrgMacSwOldEntryDeleteMode": rlBrgMacSwOldEntryDeleteMode,
       "rlBrgMacSwSpanningTree": rlBrgMacSwSpanningTree,
       "rlBrgMacSwKeyType": rlBrgMacSwKeyType,
       "rlBrgMacSwYellowBoundary": rlBrgMacSwYellowBoundary,
       "rlBrgMacSwRedBoundary": rlBrgMacSwRedBoundary,
       "rlBrgMacSwTrapEnable": rlBrgMacSwTrapEnable,
       "rlBrgMacSwOperTrapCount": rlBrgMacSwOperTrapCount,
       "rlBrgMacSwAdminTrapFrequency": rlBrgMacSwAdminTrapFrequency,
       "rlExperience": rlExperience,
       "rlCli": rlCli,
       "rlCliMibVersion": rlCliMibVersion,
       "rlCliPassword": rlCliPassword,
       "rlCliTimer": rlCliTimer,
       "rlCliFileEnable": rlCliFileEnable,
       "rlCliFileEnableAfterReset": rlCliFileEnableAfterReset,
       "rlPhysicalDescription": rlPhysicalDescription,
       "rlIfInterfaces": rlIfInterfaces,
       "rlMacMulticast": rlMacMulticast,
       "rlGalileo": rlGalileo,
       "rlpBridgeMIBObjects": rlpBridgeMIBObjects,
       "rldot1dPriority": rldot1dPriority,
       "rldot1dPriorityMibVersion": rldot1dPriorityMibVersion,
       "rldot1dPriorityPortGroupTable": rldot1dPriorityPortGroupTable,
       "rldot1dPriorityPortGroupEntry": rldot1dPriorityPortGroupEntry,
       "rldot1dPriorityPortGroupNumber": rldot1dPriorityPortGroupNumber,
       "rldot1dStp": rldot1dStp,
       "rldot1dStpMibVersion": rldot1dStpMibVersion,
       "rldot1dStpType": rldot1dStpType,
       "rldot1dStpEnable": rldot1dStpEnable,
       "rldot1dStpPortMustBelongToVlan": rldot1dStpPortMustBelongToVlan,
       "rldot1dStpExtendedPortNumberFormat": rldot1dStpExtendedPortNumberFormat,
       "rldot1dStpVlanTable": rldot1dStpVlanTable,
       "rldot1dStpVlanEntry": rldot1dStpVlanEntry,
       "rldot1dStpVlan": rldot1dStpVlan,
       "rldot1dStpVlanEnable": rldot1dStpVlanEnable,
       "rldot1dStpTimeSinceTopologyChange": rldot1dStpTimeSinceTopologyChange,
       "rldot1dStpTopChanges": rldot1dStpTopChanges,
       "rldot1dStpDesignatedRoot": rldot1dStpDesignatedRoot,
       "rldot1dStpRootCost": rldot1dStpRootCost,
       "rldot1dStpRootPort": rldot1dStpRootPort,
       "rldot1dStpMaxAge": rldot1dStpMaxAge,
       "rldot1dStpHelloTime": rldot1dStpHelloTime,
       "rldot1dStpHoldTime": rldot1dStpHoldTime,
       "rldot1dStpForwardDelay": rldot1dStpForwardDelay,
       "rldot1dStpVlanPortTable": rldot1dStpVlanPortTable,
       "rldot1dStpVlanPortEntry": rldot1dStpVlanPortEntry,
       "rldot1dStpVlanPortVlan": rldot1dStpVlanPortVlan,
       "rldot1dStpVlanPortPort": rldot1dStpVlanPortPort,
       "rldot1dStpVlanPortPriority": rldot1dStpVlanPortPriority,
       "rldot1dStpVlanPortState": rldot1dStpVlanPortState,
       "rldot1dStpVlanPortEnable": rldot1dStpVlanPortEnable,
       "rldot1dStpVlanPortPathCost": rldot1dStpVlanPortPathCost,
       "rldot1dStpVlanPortDesignatedRoot": rldot1dStpVlanPortDesignatedRoot,
       "rldot1dStpVlanPortDesignatedCost": rldot1dStpVlanPortDesignatedCost,
       "rldot1dStpVlanPortDesignatedBridge": rldot1dStpVlanPortDesignatedBridge,
       "rldot1dStpVlanPortDesignatedPort": rldot1dStpVlanPortDesignatedPort,
       "rldot1dStpVlanPortForwardTransitions": rldot1dStpVlanPortForwardTransitions,
       "rldot1dStpTrapVariable": rldot1dStpTrapVariable,
       "rldot1dStpTrapVrblifIndex": rldot1dStpTrapVrblifIndex,
       "rldot1dStpTrapVrblVID": rldot1dStpTrapVrblVID,
       "rldot1dStpTypeAfterReset": rldot1dStpTypeAfterReset,
       "rldot1dStpMonitorTime": rldot1dStpMonitorTime,
       "rldot1dStpBpduCount": rldot1dStpBpduCount,
       "rldot1dStpLastChanged": rldot1dStpLastChanged,
       "rldot1dStpPortTable": rldot1dStpPortTable,
       "rldot1dStpPortEntry": rldot1dStpPortEntry,
       "rldot1dStpPortPort": rldot1dStpPortPort,
       "rldot1dStpPortDampEnable": rldot1dStpPortDampEnable,
       "rldot1dStpPortDampStable": rldot1dStpPortDampStable,
       "rldot1dStpPortFilterBpdu": rldot1dStpPortFilterBpdu,
       "rldot1dStpPortBpduSent": rldot1dStpPortBpduSent,
       "rldot1dStpPortBpduReceived": rldot1dStpPortBpduReceived,
       "rldot1dStpPortRole": rldot1dStpPortRole,
       "rldot1dStpBpduType": rldot1dStpBpduType,
       "rldot1dStpPortRestrictedRole": rldot1dStpPortRestrictedRole,
       "rldot1dStpPortAutoEdgePort": rldot1dStpPortAutoEdgePort,
       "rldot1dStpPortLoopback": rldot1dStpPortLoopback,
       "rldot1dStpPortsEnable": rldot1dStpPortsEnable,
       "rldot1dStpTaggedFlooding": rldot1dStpTaggedFlooding,
       "rldot1dStpPortBelongToVlanDefault": rldot1dStpPortBelongToVlanDefault,
       "rldot1dStpEnableByDefault": rldot1dStpEnableByDefault,
       "rldot1dStpPortToDefault": rldot1dStpPortToDefault,
       "rldot1dStpSupportedType": rldot1dStpSupportedType,
       "rldot1dStpEdgeportSupportInStp": rldot1dStpEdgeportSupportInStp,
       "rldot1dStpFilterBpdu": rldot1dStpFilterBpdu,
       "rldot1dStpFloodBpduMethod": rldot1dStpFloodBpduMethod,
       "rldot1dStpSeparatedBridges": rldot1dStpSeparatedBridges,
       "rldot1dStpSeparatedBridgesTable": rldot1dStpSeparatedBridgesTable,
       "rldot1dStpSeparatedBridgesEntry": rldot1dStpSeparatedBridgesEntry,
       "rldot1dStpSeparatedBridgesPortEnable": rldot1dStpSeparatedBridgesPortEnable,
       "rldot1dStpSeparatedBridgesEnable": rldot1dStpSeparatedBridgesEnable,
       "rldot1dStpSeparatedBridgesAutoConfig": rldot1dStpSeparatedBridgesAutoConfig,
       "rldot1dStpPortBpduGuardTable": rldot1dStpPortBpduGuardTable,
       "rldot1dStpPortBpduGuardEntry": rldot1dStpPortBpduGuardEntry,
       "rldot1dStpPortBpduGuardEnable": rldot1dStpPortBpduGuardEnable,
       "rldot1dExtBase": rldot1dExtBase,
       "rldot1dExtBaseMibVersion": rldot1dExtBaseMibVersion,
       "rldot1dDeviceCapabilities": rldot1dDeviceCapabilities,
       "rldot1wRStp": rldot1wRStp,
       "rldot1wRStpVlanEdgePortTable": rldot1wRStpVlanEdgePortTable,
       "rldot1wRStpVlanEdgePortEntry": rldot1wRStpVlanEdgePortEntry,
       "rldot1wRStpVlanEdgePortVlan": rldot1wRStpVlanEdgePortVlan,
       "rldot1wRStpVlanEdgePortPort": rldot1wRStpVlanEdgePortPort,
       "rldot1wRStpEdgePortStatus": rldot1wRStpEdgePortStatus,
       "rldot1wRStpForceVersionTable": rldot1wRStpForceVersionTable,
       "rldot1wRStpForceVersionEntry": rldot1wRStpForceVersionEntry,
       "rldot1wRStpForceVersionVlan": rldot1wRStpForceVersionVlan,
       "rldot1wRStpForceVersionState": rldot1wRStpForceVersionState,
       "rldot1pPriorityMap": rldot1pPriorityMap,
       "rldot1pPriorityMapState": rldot1pPriorityMapState,
       "rldot1pPriorityMapTable": rldot1pPriorityMapTable,
       "rldot1pPriorityMapEntry": rldot1pPriorityMapEntry,
       "rldot1pPriorityMapName": rldot1pPriorityMapName,
       "rldot1pPriorityMapPriority": rldot1pPriorityMapPriority,
       "rldot1pPriorityMapPort": rldot1pPriorityMapPort,
       "rldot1pPriorityMapPortList": rldot1pPriorityMapPortList,
       "rldot1pPriorityMapStatus": rldot1pPriorityMapStatus,
       "rldot1sMstp": rldot1sMstp,
       "rldot1sMstpInstanceTable": rldot1sMstpInstanceTable,
       "rldot1sMstpInstanceEntry": rldot1sMstpInstanceEntry,
       "rldot1sMstpInstanceId": rldot1sMstpInstanceId,
       "rldot1sMstpInstanceEnable": rldot1sMstpInstanceEnable,
       "rldot1sMstpInstanceTimeSinceTopologyChange": rldot1sMstpInstanceTimeSinceTopologyChange,
       "rldot1sMstpInstanceTopChanges": rldot1sMstpInstanceTopChanges,
       "rldot1sMstpInstanceDesignatedRoot": rldot1sMstpInstanceDesignatedRoot,
       "rldot1sMstpInstanceRootCost": rldot1sMstpInstanceRootCost,
       "rldot1sMstpInstanceRootPort": rldot1sMstpInstanceRootPort,
       "rldot1sMstpInstanceMaxAge": rldot1sMstpInstanceMaxAge,
       "rldot1sMstpInstanceHelloTime": rldot1sMstpInstanceHelloTime,
       "rldot1sMstpInstanceHoldTime": rldot1sMstpInstanceHoldTime,
       "rldot1sMstpInstanceForwardDelay": rldot1sMstpInstanceForwardDelay,
       "rldot1sMstpInstancePriority": rldot1sMstpInstancePriority,
       "rldot1sMstpInstanceRemainingHopes": rldot1sMstpInstanceRemainingHopes,
       "rldot1sMstpInstancePortTable": rldot1sMstpInstancePortTable,
       "rldot1sMstpInstancePortEntry": rldot1sMstpInstancePortEntry,
       "rldot1sMstpInstancePortMstiId": rldot1sMstpInstancePortMstiId,
       "rldot1sMstpInstancePortPort": rldot1sMstpInstancePortPort,
       "rldot1sMstpInstancePortPriority": rldot1sMstpInstancePortPriority,
       "rldot1sMstpInstancePortState": rldot1sMstpInstancePortState,
       "rldot1sMstpInstancePortEnable": rldot1sMstpInstancePortEnable,
       "rldot1sMstpInstancePortPathCost": rldot1sMstpInstancePortPathCost,
       "rldot1sMstpInstancePortDesignatedRoot": rldot1sMstpInstancePortDesignatedRoot,
       "rldot1sMstpInstancePortDesignatedCost": rldot1sMstpInstancePortDesignatedCost,
       "rldot1sMstpInstancePortDesignatedBridge": rldot1sMstpInstancePortDesignatedBridge,
       "rldot1sMstpInstancePortDesignatedPort": rldot1sMstpInstancePortDesignatedPort,
       "rldot1sMstpInstancePortForwardTransitions": rldot1sMstpInstancePortForwardTransitions,
       "rldot1sMStpInstancePortAdminPathCost": rldot1sMStpInstancePortAdminPathCost,
       "rldot1sMStpInstancePortRole": rldot1sMStpInstancePortRole,
       "rldot1sMstpMaxHopes": rldot1sMstpMaxHopes,
       "rldot1sMstpConfigurationName": rldot1sMstpConfigurationName,
       "rldot1sMstpRevisionLevel": rldot1sMstpRevisionLevel,
       "rldot1sMstpVlanTable": rldot1sMstpVlanTable,
       "rldot1sMstpVlanEntry": rldot1sMstpVlanEntry,
       "rldot1sMstpVlan": rldot1sMstpVlan,
       "rldot1sMstpGroup": rldot1sMstpGroup,
       "rldot1sMstpPendingGroup": rldot1sMstpPendingGroup,
       "rldot1sMstpExtPortTable": rldot1sMstpExtPortTable,
       "rldot1sMstpExtPortEntry": rldot1sMstpExtPortEntry,
       "rldot1sMstpExtPortPort": rldot1sMstpExtPortPort,
       "rldot1sMstpExtPortInternalOperPathCost": rldot1sMstpExtPortInternalOperPathCost,
       "rldot1sMstpExtPortDesignatedRegionalRoot": rldot1sMstpExtPortDesignatedRegionalRoot,
       "rldot1sMstpExtPortDesignatedRegionalCost": rldot1sMstpExtPortDesignatedRegionalCost,
       "rldot1sMstpExtPortBoundary": rldot1sMstpExtPortBoundary,
       "rldot1sMstpExtPortInternalAdminPathCost": rldot1sMstpExtPortInternalAdminPathCost,
       "rldot1sMstpDesignatedMaxHopes": rldot1sMstpDesignatedMaxHopes,
       "rldot1sMstpRegionalRoot": rldot1sMstpRegionalRoot,
       "rldot1sMstpRegionalRootCost": rldot1sMstpRegionalRootCost,
       "rldot1sMstpPendingConfigurationName": rldot1sMstpPendingConfigurationName,
       "rldot1sMstpPendingRevisionLevel": rldot1sMstpPendingRevisionLevel,
       "rldot1sMstpPendingAction": rldot1sMstpPendingAction,
       "rldot1sMstpRemainingHops": rldot1sMstpRemainingHops,
       "rldot1dTpAgingTime": rldot1dTpAgingTime,
       "rldot1dTpAgingTimeMin": rldot1dTpAgingTimeMin,
       "rldot1dTpAgingTimeMax": rldot1dTpAgingTimeMax,
       "rlTelnet": rlTelnet,
       "rlTelnetMibVersion": rlTelnetMibVersion,
       "rlTelnetPassword": rlTelnetPassword,
       "rlTelnetTimeout": rlTelnetTimeout,
       "rlTelnetUsersTable": rlTelnetUsersTable,
       "rlTelnetUsersEntry": rlTelnetUsersEntry,
       "rlTelnetSessionId": rlTelnetSessionId,
       "rlTelnetSessionClientAddress": rlTelnetSessionClientAddress,
       "rlTelnetSessionLoginTime": rlTelnetSessionLoginTime,
       "rlTelnetSessionStatus": rlTelnetSessionStatus,
       "rlTelnetLoginBanner": rlTelnetLoginBanner,
       "rlTelnetSecondLoginBanner": rlTelnetSecondLoginBanner,
       "rlPolicy": rlPolicy,
       "rlArpSpoofing": rlArpSpoofing,
       "rlArpSpoofingMibVersion": rlArpSpoofingMibVersion,
       "rlArpSpoofingTable": rlArpSpoofingTable,
       "rlArpSpoofingEntry": rlArpSpoofingEntry,
       "rlArpSpoofingIfIndex": rlArpSpoofingIfIndex,
       "rlArpSpoofingLocalIpAddr": rlArpSpoofingLocalIpAddr,
       "rlArpSpoofingMacAddr": rlArpSpoofingMacAddr,
       "rlArpSpoofingRemoteIpAddr": rlArpSpoofingRemoteIpAddr,
       "rlArpSpoofingOutPhysIfIndex": rlArpSpoofingOutPhysIfIndex,
       "rlArpSpoofingStatus": rlArpSpoofingStatus,
       "rlMir": rlMir,
       "rlMirMibVersion": rlMirMibVersion,
       "rlMirMaxNumOfMRIsAfterReset": rlMirMaxNumOfMRIsAfterReset,
       "rlMirMaxNumOfMRIs": rlMirMaxNumOfMRIs,
       "rlMirCurMriNum": rlMirCurMriNum,
       "rlMirInterfaceTable": rlMirInterfaceTable,
       "rlMirInterfaceEntry": rlMirInterfaceEntry,
       "rlMirInterfaceIfIndex": rlMirInterfaceIfIndex,
       "rlMirInterfaceMrid": rlMirInterfaceMrid,
       "rlMirVlanBaseReservedPortsTable": rlMirVlanBaseReservedPortsTable,
       "rlMirVlanBaseReservedPortsEntry": rlMirVlanBaseReservedPortsEntry,
       "rlMirVlanBaseReservedPortsIfIndex": rlMirVlanBaseReservedPortsIfIndex,
       "rlMirVlanBaseReservedPortsStatus": rlMirVlanBaseReservedPortsStatus,
       "rlMirVlanBaseLogicalPortsTable": rlMirVlanBaseLogicalPortsTable,
       "rlMirVlanBaseLogicalPortsEntry": rlMirVlanBaseLogicalPortsEntry,
       "rlMirVlanBaseLogicalPortsIfIndex": rlMirVlanBaseLogicalPortsIfIndex,
       "rlMirVlanBaseLogicalPortsReservedIfIndex": rlMirVlanBaseLogicalPortsReservedIfIndex,
       "rlMirVlanBaseLogicalPortsVlanTag": rlMirVlanBaseLogicalPortsVlanTag,
       "rlMirVlanBaseLogicalPortsStatus": rlMirVlanBaseLogicalPortsStatus,
       "rlIpMRouteStdMIB": rlIpMRouteStdMIB,
       "rl3sw2swTables": rl3sw2swTables,
       "rl3sw2swTablesPollingInterval": rl3sw2swTablesPollingInterval,
       "rlGvrp": rlGvrp,
       "rlPortGvrpTimersTable": rlPortGvrpTimersTable,
       "rlPortGvrpTimersEntry": rlPortGvrpTimersEntry,
       "rlPortGvrpJoinTime": rlPortGvrpJoinTime,
       "rlPortGvrpLeaveTime": rlPortGvrpLeaveTime,
       "rlPortGvrpLeaveAllTime": rlPortGvrpLeaveAllTime,
       "rlPortGvrpOverrideGarp": rlPortGvrpOverrideGarp,
       "rlGvrpSupported": rlGvrpSupported,
       "rlGvrpMibVersion": rlGvrpMibVersion,
       "rlPortGvrpStatisticsTable": rlPortGvrpStatisticsTable,
       "rlPortGvrpStatisticsEntry": rlPortGvrpStatisticsEntry,
       "rlPortGvrpStatisticsRJE": rlPortGvrpStatisticsRJE,
       "rlPortGvrpStatisticsRJIn": rlPortGvrpStatisticsRJIn,
       "rlPortGvrpStatisticsREmp": rlPortGvrpStatisticsREmp,
       "rlPortGvrpStatisticsRLIn": rlPortGvrpStatisticsRLIn,
       "rlPortGvrpStatisticsRLE": rlPortGvrpStatisticsRLE,
       "rlPortGvrpStatisticsRLA": rlPortGvrpStatisticsRLA,
       "rlPortGvrpStatisticsSJE": rlPortGvrpStatisticsSJE,
       "rlPortGvrpStatisticsSJIn": rlPortGvrpStatisticsSJIn,
       "rlPortGvrpStatisticsSEmp": rlPortGvrpStatisticsSEmp,
       "rlPortGvrpStatisticsSLIn": rlPortGvrpStatisticsSLIn,
       "rlPortGvrpStatisticsSLE": rlPortGvrpStatisticsSLE,
       "rlPortGvrpStatisticsSLA": rlPortGvrpStatisticsSLA,
       "rlPortGvrpStatisticsClear": rlPortGvrpStatisticsClear,
       "rlPortGvrpErrorStatisticsTable": rlPortGvrpErrorStatisticsTable,
       "rlPortGvrpErrorStatisticsEntry": rlPortGvrpErrorStatisticsEntry,
       "rlPortGvrpErrorStatisticsInvProt": rlPortGvrpErrorStatisticsInvProt,
       "rlPortGvrpErrorStatisticsInvAtyp": rlPortGvrpErrorStatisticsInvAtyp,
       "rlPortGvrpErrorStatisticsInvAval": rlPortGvrpErrorStatisticsInvAval,
       "rlPortGvrpErrorStatisticsInvPlen": rlPortGvrpErrorStatisticsInvPlen,
       "rlPortGvrpErrorStatisticsInvAlen": rlPortGvrpErrorStatisticsInvAlen,
       "rlPortGvrpErrorStatisticsInvEvent": rlPortGvrpErrorStatisticsInvEvent,
       "rlPortGvrpErrorStatisticsClear": rlPortGvrpErrorStatisticsClear,
       "rlPortGvrpApplicantStatusTable": rlPortGvrpApplicantStatusTable,
       "rlPortGvrpApplicantStatusEntry": rlPortGvrpApplicantStatusEntry,
       "rlPortGvrpApplicantStatusValue": rlPortGvrpApplicantStatusValue,
       "rlPortGvrpRegistrationModeTable": rlPortGvrpRegistrationModeTable,
       "rlPortGvrpRegistrationModeEntry": rlPortGvrpRegistrationModeEntry,
       "rlPortGvrpRegistrationModeForbidden": rlPortGvrpRegistrationModeForbidden,
       "rlDot3adAgg": rlDot3adAgg,
       "rlEmbWeb": rlEmbWeb,
       "rlSwPackageVersion": rlSwPackageVersion,
       "rlSwPackageVersionTable": rlSwPackageVersionTable,
       "rlSwPackageVersionEntry": rlSwPackageVersionEntry,
       "rlSwPackageVersionName": rlSwPackageVersionName,
       "rlSwPackageVersionVesrion": rlSwPackageVersionVesrion,
       "rlBroadcom": rlBroadcom,
       "rlMultiSessionTerminal": rlMultiSessionTerminal,
       "rlTerminalDebugModePassword": rlTerminalDebugModePassword,
       "rlRCli": rlRCli,
       "rlRCliMibVersion": rlRCliMibVersion,
       "rlRCliUserPassword": rlRCliUserPassword,
       "rlRCliEnablePassword": rlRCliEnablePassword,
       "rlRCliConfigPassword": rlRCliConfigPassword,
       "rlRCliTimer": rlRCliTimer,
       "rlRcliFileAction": rlRcliFileAction,
       "rlBgp": rlBgp,
       "rlAgentsCapabilitiesGroups": rlAgentsCapabilitiesGroups,
       "rlAggregateVlan": rlAggregateVlan,
       "rlAggregateVlanMibVersion": rlAggregateVlanMibVersion,
       "rlAggregateVlanTable": rlAggregateVlanTable,
       "rlAggregateVlanEntry": rlAggregateVlanEntry,
       "rlAggregateVlanIndex": rlAggregateVlanIndex,
       "rlAggregateVlanName": rlAggregateVlanName,
       "rlAggregateVlanPhysAddressType": rlAggregateVlanPhysAddressType,
       "rlAggregateVlanStatus": rlAggregateVlanStatus,
       "rlAggregateSubVlanTable": rlAggregateSubVlanTable,
       "rlAggregateSubVlanEntry": rlAggregateSubVlanEntry,
       "rlAggregateSubVlanIfIndex": rlAggregateSubVlanIfIndex,
       "rlAggregateSubVlanStatus": rlAggregateSubVlanStatus,
       "rlAggregateVlanArpProxy": rlAggregateVlanArpProxy,
       "rlGmrp": rlGmrp,
       "rlGmrpSupported": rlGmrpSupported,
       "rlGmrpMibVersion": rlGmrpMibVersion,
       "rlPortGmrpTimersTable": rlPortGmrpTimersTable,
       "rlPortGmrpTimersEntry": rlPortGmrpTimersEntry,
       "rlPortGmrpJoinTime": rlPortGmrpJoinTime,
       "rlPortGmrpLeaveTime": rlPortGmrpLeaveTime,
       "rlPortGmrpLeaveAllTime": rlPortGmrpLeaveAllTime,
       "rlPortGmrpOverrideGarp": rlPortGmrpOverrideGarp,
       "rlGmrpVlanTable": rlGmrpVlanTable,
       "rlGmrpVlanEntry": rlGmrpVlanEntry,
       "rlGmrpVlanTag": rlGmrpVlanTag,
       "rlGmrpVlanEnable": rlGmrpVlanEnable,
       "rlDhcpCl": rlDhcpCl,
       "rlDhcpClActionTable": rlDhcpClActionTable,
       "rlDhcpClActionEntry": rlDhcpClActionEntry,
       "rlDhcpClActionIfIndex": rlDhcpClActionIfIndex,
       "rlDhcpClActionStatus": rlDhcpClActionStatus,
       "rlDhcpClActionHostName": rlDhcpClActionHostName,
       "rlDhcpApprovalEnabled": rlDhcpApprovalEnabled,
       "rlDhcpApprovalWaitingTable": rlDhcpApprovalWaitingTable,
       "rlDhcpApprovalWaitingEntry": rlDhcpApprovalWaitingEntry,
       "rlDhcpApprovalWaitingIfIndex": rlDhcpApprovalWaitingIfIndex,
       "rlDhcpApprovalWaitingAddress": rlDhcpApprovalWaitingAddress,
       "rlDhcpApprovalWaitingMask": rlDhcpApprovalWaitingMask,
       "rlDhcpApprovalWaitingGateway": rlDhcpApprovalWaitingGateway,
       "rlDhcpApprovalActionTable": rlDhcpApprovalActionTable,
       "rlDhcpApprovalActionEntry": rlDhcpApprovalActionEntry,
       "rlDhcpApprovalActionIfIndex": rlDhcpApprovalActionIfIndex,
       "rlDhcpApprovalActionAddress": rlDhcpApprovalActionAddress,
       "rlDhcpApprovalActionMask": rlDhcpApprovalActionMask,
       "rlDhcpApprovalActionApprove": rlDhcpApprovalActionApprove,
       "rlDhcpClCommandTable": rlDhcpClCommandTable,
       "rlDhcpClCommandEntry": rlDhcpClCommandEntry,
       "rlDhcpClCommandAction": rlDhcpClCommandAction,
       "rlStormCtrl": rlStormCtrl,
       "rlStormCtrlSupport": rlStormCtrlSupport,
       "rlStormCtrlMibVersion": rlStormCtrlMibVersion,
       "rlStormCtrlRateUnitTypeSupport": rlStormCtrlRateUnitTypeSupport,
       "rlStormCtrlTypeSupport": rlStormCtrlTypeSupport,
       "rlStormCtrlRateSupportPerType": rlStormCtrlRateSupportPerType,
       "rlStormCtrlEnbaleDependencyBetweenTypes": rlStormCtrlEnbaleDependencyBetweenTypes,
       "rlStormCtrlRateDependencyBetweenTypes": rlStormCtrlRateDependencyBetweenTypes,
       "rlStormCtrlTable": rlStormCtrlTable,
       "rlStormCtrlEntry": rlStormCtrlEntry,
       "rlStormCtrlRateType": rlStormCtrlRateType,
       "rlStormCtrlUnknownUnicastEnable": rlStormCtrlUnknownUnicastEnable,
       "rlStormCtrlUnknownUnicastRate": rlStormCtrlUnknownUnicastRate,
       "rlStormCtrlUnknownMulticastEnable": rlStormCtrlUnknownMulticastEnable,
       "rlStormCtrlUnknownMulticastRate": rlStormCtrlUnknownMulticastRate,
       "rlStormCtrlBroadcastEnable": rlStormCtrlBroadcastEnable,
       "rlStormCtrlBroadcastRate": rlStormCtrlBroadcastRate,
       "rlStormCtrlMulticastEnable": rlStormCtrlMulticastEnable,
       "rlStormCtrlMulticastRate": rlStormCtrlMulticastRate,
       "rlStormCtrlSetDefaultRateType": rlStormCtrlSetDefaultRateType,
       "rlStormCtrlSetDefaultUnknownUnicastEnable": rlStormCtrlSetDefaultUnknownUnicastEnable,
       "rlStormCtrlSetDefaultUnknownUnicastRate": rlStormCtrlSetDefaultUnknownUnicastRate,
       "rlStormCtrlSetDefaultUnknownMulticastEnable": rlStormCtrlSetDefaultUnknownMulticastEnable,
       "rlStormCtrlSetDefaultUnknownMulticastRate": rlStormCtrlSetDefaultUnknownMulticastRate,
       "rlStormCtrlSetDefaultBroadcastEnable": rlStormCtrlSetDefaultBroadcastEnable,
       "rlStormCtrlSetDefaultBroadcastRate": rlStormCtrlSetDefaultBroadcastRate,
       "rlStormCtrlSetDefaultMulticastEnable": rlStormCtrlSetDefaultMulticastEnable,
       "rlStormCtrlSetDefaultMulticastRate": rlStormCtrlSetDefaultMulticastRate,
       "rlStormCtrlGroupTable": rlStormCtrlGroupTable,
       "rlStormCtrlGroupEntry": rlStormCtrlGroupEntry,
       "rlStormCtrlGroupUnknownUnicastId": rlStormCtrlGroupUnknownUnicastId,
       "rlStormCtrlGroupUnknownMulticastId": rlStormCtrlGroupUnknownMulticastId,
       "rlStormCtrlGroupBroadcastId": rlStormCtrlGroupBroadcastId,
       "rlStormCtrlGroupMulticastId": rlStormCtrlGroupMulticastId,
       "rlSsh": rlSsh,
       "rlAAA": rlAAA,
       "rlRadius": rlRadius,
       "rlTraceRoute": rlTraceRoute,
       "rlTraceRouteMibVersion": rlTraceRouteMibVersion,
       "rlSyslog": rlSyslog,
       "rlEnv": rlEnv,
       "rlSmon": rlSmon,
       "rlPortCopyMibVersion": rlPortCopyMibVersion,
       "rlPortCopySupport": rlPortCopySupport,
       "rlPortCopyVlanTaggingTable": rlPortCopyVlanTaggingTable,
       "rlPortCopyVlanTaggingEntry": rlPortCopyVlanTaggingEntry,
       "rlPortCopyVlanTagging": rlPortCopyVlanTagging,
       "rlSocket": rlSocket,
       "rlSocketMibVersion": rlSocketMibVersion,
       "rlSocketTable": rlSocketTable,
       "rlSocketEntry": rlSocketEntry,
       "rlSocketId": rlSocketId,
       "rlSocketType": rlSocketType,
       "rlSocketState": rlSocketState,
       "rlSocketBlockMode": rlSocketBlockMode,
       "rlSocketUpTime": rlSocketUpTime,
       "rlDigitalKeyManage": rlDigitalKeyManage,
       "rlMD5KeyChainTable": rlMD5KeyChainTable,
       "rlMD5KeyChainEntry": rlMD5KeyChainEntry,
       "rlMD5KeyChainName": rlMD5KeyChainName,
       "rlMD5KeyChainKeyId": rlMD5KeyChainKeyId,
       "rlMD5KeyChainKeyRowStatus": rlMD5KeyChainKeyRowStatus,
       "rlMD5KeyTable": rlMD5KeyTable,
       "rlMD5KeyEntry": rlMD5KeyEntry,
       "rlMD5KeyId": rlMD5KeyId,
       "rlMD5Key": rlMD5Key,
       "rlMD5KeyStartAccept": rlMD5KeyStartAccept,
       "rlMD5KeyStartGenerate": rlMD5KeyStartGenerate,
       "rlMD5KeyStopGenerate": rlMD5KeyStopGenerate,
       "rlMD5KeyStopAccept": rlMD5KeyStopAccept,
       "rlMD5KeyRowStatus": rlMD5KeyRowStatus,
       "rlCopy": rlCopy,
       "rlQosCliMib": rlQosCliMib,
       "rlMngInf": rlMngInf,
       "rlPhy": rlPhy,
       "rlJumboFrames": rlJumboFrames,
       "rlJumboFramesCurrentStatus": rlJumboFramesCurrentStatus,
       "rlJumboFramesStatusAfterReset": rlJumboFramesStatusAfterReset,
       "rlTimeSynchronization": rlTimeSynchronization,
       "rlDnsCl": rlDnsCl,
       "rlCDB": rlCDB,
       "rlStartupCDBChanged": rlStartupCDBChanged,
       "rlManualReboot": rlManualReboot,
       "rldot1x": rldot1x,
       "rldot1xMibVersion": rldot1xMibVersion,
       "rldot1xExtAuthSessionStatsTable": rldot1xExtAuthSessionStatsTable,
       "rldot1xExtAuthSessionStatsEntry": rldot1xExtAuthSessionStatsEntry,
       "rlDot1xAuthSessionAuthenticMethod": rlDot1xAuthSessionAuthenticMethod,
       "rldot1xGuestVlanSupported": rldot1xGuestVlanSupported,
       "rldot1xGuestVlanVID": rldot1xGuestVlanVID,
       "rldot1xGuestVlanPorts": rldot1xGuestVlanPorts,
       "rldot1xUnAuthenticatedVlanSupported": rldot1xUnAuthenticatedVlanSupported,
       "rldot1xUnAuthenticatedVlanTable": rldot1xUnAuthenticatedVlanTable,
       "rldot1xUnAuthenticatedVlanEntry": rldot1xUnAuthenticatedVlanEntry,
       "rldot1xUnAuthenticatedVlanStatus": rldot1xUnAuthenticatedVlanStatus,
       "rldot1xUserBasedVlanSupported": rldot1xUserBasedVlanSupported,
       "rldot1xUserBasedVlanPorts": rldot1xUserBasedVlanPorts,
       "rldot1xAuthenticationPortTable": rldot1xAuthenticationPortTable,
       "rldot1xAuthenticationPortEntry": rldot1xAuthenticationPortEntry,
       "rldot1xAuthenticationPortMethod": rldot1xAuthenticationPortMethod,
       "rldot1xAuthMultiStatsTable": rldot1xAuthMultiStatsTable,
       "rldot1xAuthMultiStatsEntry": rldot1xAuthMultiStatsEntry,
       "rldot1xAuthMultiStatsPortNumber": rldot1xAuthMultiStatsPortNumber,
       "rldot1xAuthMultiStatsSourceMac": rldot1xAuthMultiStatsSourceMac,
       "rldot1xAuthMultiEapolFramesRx": rldot1xAuthMultiEapolFramesRx,
       "rldot1xAuthMultiEapolFramesTx": rldot1xAuthMultiEapolFramesTx,
       "rldot1xAuthMultiEapolStartFramesRx": rldot1xAuthMultiEapolStartFramesRx,
       "rldot1xAuthMultiEapolLogoffFramesRx": rldot1xAuthMultiEapolLogoffFramesRx,
       "rldot1xAuthMultiEapolRespIdFramesRx": rldot1xAuthMultiEapolRespIdFramesRx,
       "rldot1xAuthMultiEapolRespFramesRx": rldot1xAuthMultiEapolRespFramesRx,
       "rldot1xAuthMultiEapolReqIdFramesTx": rldot1xAuthMultiEapolReqIdFramesTx,
       "rldot1xAuthMultiEapolReqFramesTx": rldot1xAuthMultiEapolReqFramesTx,
       "rldot1xAuthMultiInvalidEapolFramesRx": rldot1xAuthMultiInvalidEapolFramesRx,
       "rldot1xAuthMultiEapLengthErrorFramesRx": rldot1xAuthMultiEapLengthErrorFramesRx,
       "rldot1xAuthMultiDiagTable": rldot1xAuthMultiDiagTable,
       "rldot1xAuthMultiDiagEntry": rldot1xAuthMultiDiagEntry,
       "rldot1xAuthMultiDiagPortNumber": rldot1xAuthMultiDiagPortNumber,
       "rldot1xAuthMultiDiagSourceMac": rldot1xAuthMultiDiagSourceMac,
       "rldot1xAuthMultiEntersConnecting": rldot1xAuthMultiEntersConnecting,
       "rldot1xAuthMultiEntersAuthenticating": rldot1xAuthMultiEntersAuthenticating,
       "rldot1xAuthMultiAuthSuccessWhileAuthenticating": rldot1xAuthMultiAuthSuccessWhileAuthenticating,
       "rldot1xAuthMultiAuthFailWhileAuthenticating": rldot1xAuthMultiAuthFailWhileAuthenticating,
       "rldot1xAuthMultiAuthReauthsWhileAuthenticating": rldot1xAuthMultiAuthReauthsWhileAuthenticating,
       "rldot1xAuthMultiAuthEapStartsWhileAuthenticating": rldot1xAuthMultiAuthEapStartsWhileAuthenticating,
       "rldot1xAuthMultiAuthReauthsWhileAuthenticated": rldot1xAuthMultiAuthReauthsWhileAuthenticated,
       "rldot1xAuthMultiAuthEapStartsWhileAuthenticated": rldot1xAuthMultiAuthEapStartsWhileAuthenticated,
       "rldot1xAuthMultiBackendResponses": rldot1xAuthMultiBackendResponses,
       "rldot1xAuthMultiBackendAccessChallenges": rldot1xAuthMultiBackendAccessChallenges,
       "rldot1xAuthMultiBackendOtherRequestsToSupplicant": rldot1xAuthMultiBackendOtherRequestsToSupplicant,
       "rldot1xAuthMultiBackendNonNakResponsesFromSupplicant": rldot1xAuthMultiBackendNonNakResponsesFromSupplicant,
       "rldot1xAuthMultiBackendAuthSuccesses": rldot1xAuthMultiBackendAuthSuccesses,
       "rldot1xAuthMultiSessionStatsTable": rldot1xAuthMultiSessionStatsTable,
       "rldot1xAuthMultiSessionStatsEntry": rldot1xAuthMultiSessionStatsEntry,
       "rldot1xAuthMultiSessionStatsPortNumber": rldot1xAuthMultiSessionStatsPortNumber,
       "rldot1xAuthMultiSessionStatsSourceMac": rldot1xAuthMultiSessionStatsSourceMac,
       "rldot1xAuthMultiSessionOctetsRx": rldot1xAuthMultiSessionOctetsRx,
       "rldot1xAuthMultiSessionOctetsTx": rldot1xAuthMultiSessionOctetsTx,
       "rldot1xAuthMultiSessionFramesRx": rldot1xAuthMultiSessionFramesRx,
       "rldot1xAuthMultiSessionFramesTx": rldot1xAuthMultiSessionFramesTx,
       "rldot1xAuthMultiSessionId": rldot1xAuthMultiSessionId,
       "rldot1xAuthMultiSessionTime": rldot1xAuthMultiSessionTime,
       "rldot1xAuthMultiSessionUserName": rldot1xAuthMultiSessionUserName,
       "rldot1xAuthMultiConfigTable": rldot1xAuthMultiConfigTable,
       "rldot1xAuthMultiConfigEntry": rldot1xAuthMultiConfigEntry,
       "rldot1xAuthMultiPortNumber": rldot1xAuthMultiPortNumber,
       "rldot1xAuthMultiSourceMac": rldot1xAuthMultiSourceMac,
       "rldot1xAuthMultiPaeState": rldot1xAuthMultiPaeState,
       "rldot1xAuthMultiBackendAuthState": rldot1xAuthMultiBackendAuthState,
       "rldot1xAuthMultiControlledPortStatus": rldot1xAuthMultiControlledPortStatus,
       "rldot1xBpduFilteringEnabled": rldot1xBpduFilteringEnabled,
       "rlFile": rlFile,
       "rlAAAEap": rlAAAEap,
       "rlSNMP": rlSNMP,
       "rlSsl": rlSsl,
       "rlMacBasePrio": rlMacBasePrio,
       "rlWlanAccessPoint": rlWlanAccessPoint,
       "rlLocalization": rlLocalization,
       "rlRs232": rlRs232,
       "rlNicRedundancy": rlNicRedundancy,
       "rlAmap": rlAmap,
       "rlStack": rlStack,
       "rlPoe": rlPoe,
       "rlUPnP": rlUPnP,
       "rlLldp": rlLldp,
       "rlOib": rlOib,
       "rlBridgeSecurity": rlBridgeSecurity,
       "rlDhcpSpoofing": rlDhcpSpoofing,
       "rlBonjour": rlBonjour,
       "rlLinksysSmartMIB": rlLinksysSmartMIB,
       "rlBrgMulticast": rlBrgMulticast,
       "rlBrgMcMngr": rlBrgMcMngr,
       "rlGlobalIpAddrTable": rlGlobalIpAddrTable,
       "dlPrivate": dlPrivate,
       "rlSecuritySuiteMib": rlSecuritySuiteMib,
       "rlIntel": rlIntel,
       "rlAutoUpdate": rlAutoUpdate,
       "rlCpuCounters": rlCpuCounters,
       "rlWlanMIB": rlWlanMIB,
       "rndEndOfMibGroup": rndEndOfMibGroup,
       "rndEndOfMib": rndEndOfMib}
)
