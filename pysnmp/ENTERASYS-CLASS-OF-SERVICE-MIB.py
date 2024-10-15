# SNMP MIB module (ENTERASYS-CLASS-OF-SERVICE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ENTERASYS-CLASS-OF-SERVICE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:38:43 2024
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

(dot1dBasePort,) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "dot1dBasePort")

(etsysModules,) = mibBuilder.importSymbols(
    "ENTERASYS-MIB-NAMES",
    "etsysModules")

(ifName,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifName")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

(PortList,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList")

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

etsysCosMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55)
)
etsysCosMIB.setRevisions(
        ("2008-02-13 15:03",
         "2007-05-24 02:29",
         "2005-04-13 21:22",
         "2004-11-22 16:28",
         "2004-11-09 15:52")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class TxqArbiterModes(Bits, TextualConvention):
    status = "current"


class TxqAlgorithms(Bits, TextualConvention):
    status = "current"


class TxQueueList(OctetString, TextualConvention):
    status = "current"


class EtsysCosRateTypes(Bits, TextualConvention):
    status = "current"


class EtsysCosRlCapabilities(Bits, TextualConvention):
    status = "current"


class EtsysViolationAction(Bits, TextualConvention):
    status = "current"


class EtsysRateLimitingType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("count", 4),
          ("drop", 0),
          ("dropOR", 1),
          ("rePrioritize", 2),
          ("rePrioritizeOR", 3))
    )



class EtsysRateLimitResetBits(Bits, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_EtsysCosObjects_ObjectIdentity = ObjectIdentity
etsysCosObjects = _EtsysCosObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1)
)
_EtsysCosNotifications_ObjectIdentity = ObjectIdentity
etsysCosNotifications = _EtsysCosNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 0)
)
_EtsysCosMasterReset_ObjectIdentity = ObjectIdentity
etsysCosMasterReset = _EtsysCosMasterReset_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 1)
)


class _EtsysCosMibObjectAnullingBehavior_Type(TruthValue):
    """Custom type etsysCosMibObjectAnullingBehavior based on TruthValue"""


_EtsysCosMibObjectAnullingBehavior_Object = MibScalar
etsysCosMibObjectAnullingBehavior = _EtsysCosMibObjectAnullingBehavior_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 1, 1),
    _EtsysCosMibObjectAnullingBehavior_Type()
)
etsysCosMibObjectAnullingBehavior.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysCosMibObjectAnullingBehavior.setStatus("current")
_EtsysCosCapabilities_ObjectIdentity = ObjectIdentity
etsysCosCapabilities = _EtsysCosCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 2)
)


class _EtsysCosCapability_Type(Bits):
    """Custom type etsysCosCapability based on Bits"""
    namedValues = NamedValues(
        *(("supports8021Dpriority", 0),
          ("supportsBroadcastRateLimiting", 9),
          ("supportsDropPrecedence", 6),
          ("supportsInboundRateLimiting", 4),
          ("supportsMulticastRateLimiting", 8),
          ("supportsOutBoundRateLimiting", 5),
          ("supportsTosMasking", 2),
          ("supportsTosOverwrite", 1),
          ("supportsTransmitQueue", 3),
          ("supportsTransmitQueuePortShaping", 10),
          ("supportsUnknownUnicastRateLimiting", 7))
    )

_EtsysCosCapability_Type.__name__ = "Bits"
_EtsysCosCapability_Object = MibScalar
etsysCosCapability = _EtsysCosCapability_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 2, 1),
    _EtsysCosCapability_Type()
)
etsysCosCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysCosCapability.setStatus("current")
_EtsysCos_ObjectIdentity = ObjectIdentity
etsysCos = _EtsysCos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 3)
)
_EtsysCosMaxEntries_Type = Unsigned32
_EtsysCosMaxEntries_Object = MibScalar
etsysCosMaxEntries = _EtsysCosMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 3, 1),
    _EtsysCosMaxEntries_Type()
)
etsysCosMaxEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysCosMaxEntries.setStatus("current")
_EtsysCosNumEntries_Type = Gauge32
_EtsysCosNumEntries_Object = MibScalar
etsysCosNumEntries = _EtsysCosNumEntries_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 3, 2),
    _EtsysCosNumEntries_Type()
)
etsysCosNumEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysCosNumEntries.setStatus("current")
_EtsysCosLastChange_Type = TimeStamp
_EtsysCosLastChange_Object = MibScalar
etsysCosLastChange = _EtsysCosLastChange_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 3, 3),
    _EtsysCosLastChange_Type()
)
etsysCosLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysCosLastChange.setStatus("current")


class _EtsysCosEnableState_Type(EnabledStatus):
    """Custom type etsysCosEnableState based on EnabledStatus"""


_EtsysCosEnableState_Object = MibScalar
etsysCosEnableState = _EtsysCosEnableState_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 3, 4),
    _EtsysCosEnableState_Type()
)
etsysCosEnableState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysCosEnableState.setStatus("current")
_EtsysCosTable_Object = MibTable
etsysCosTable = _EtsysCosTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 3, 5)
)
if mibBuilder.loadTexts:
    etsysCosTable.setStatus("current")
_EtsysCosEntry_Object = MibTableRow
etsysCosEntry = _EtsysCosEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 3, 5, 1)
)
etsysCosEntry.setIndexNames(
    (0, "ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosIndex"),
)
if mibBuilder.loadTexts:
    etsysCosEntry.setStatus("current")


class _EtsysCosIndex_Type(Unsigned32):
    """Custom type etsysCosIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_EtsysCosIndex_Type.__name__ = "Unsigned32"
_EtsysCosIndex_Object = MibTableColumn
etsysCosIndex = _EtsysCosIndex_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 3, 5, 1, 1),
    _EtsysCosIndex_Type()
)
etsysCosIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysCosIndex.setStatus("current")
_EtsysCosRowStatus_Type = RowStatus
_EtsysCosRowStatus_Object = MibTableColumn
etsysCosRowStatus = _EtsysCosRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 3, 5, 1, 2),
    _EtsysCosRowStatus_Type()
)
etsysCosRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysCosRowStatus.setStatus("current")


class _EtsysCos8021dPriority_Type(Integer32):
    """Custom type etsysCos8021dPriority based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 7),
    )


_EtsysCos8021dPriority_Type.__name__ = "Integer32"
_EtsysCos8021dPriority_Object = MibTableColumn
etsysCos8021dPriority = _EtsysCos8021dPriority_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 3, 5, 1, 3),
    _EtsysCos8021dPriority_Type()
)
etsysCos8021dPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysCos8021dPriority.setStatus("current")


class _EtsysCosTosValue_Type(OctetString):
    """Custom type etsysCosTosValue based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2),
    )


_EtsysCosTosValue_Type.__name__ = "OctetString"
_EtsysCosTosValue_Object = MibTableColumn
etsysCosTosValue = _EtsysCosTosValue_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 3, 5, 1, 4),
    _EtsysCosTosValue_Type()
)
etsysCosTosValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysCosTosValue.setStatus("current")


class _EtsysCosTxqReference_Type(Integer32):
    """Custom type etsysCosTxqReference based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_EtsysCosTxqReference_Type.__name__ = "Integer32"
_EtsysCosTxqReference_Object = MibTableColumn
etsysCosTxqReference = _EtsysCosTxqReference_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 3, 5, 1, 5),
    _EtsysCosTxqReference_Type()
)
etsysCosTxqReference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysCosTxqReference.setStatus("current")


class _EtsysCosIrlReference_Type(Integer32):
    """Custom type etsysCosIrlReference based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 32767),
    )


_EtsysCosIrlReference_Type.__name__ = "Integer32"
_EtsysCosIrlReference_Object = MibTableColumn
etsysCosIrlReference = _EtsysCosIrlReference_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 3, 5, 1, 6),
    _EtsysCosIrlReference_Type()
)
etsysCosIrlReference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysCosIrlReference.setStatus("current")


class _EtsysCosOrlReference_Type(Integer32):
    """Custom type etsysCosOrlReference based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 32767),
    )


_EtsysCosOrlReference_Type.__name__ = "Integer32"
_EtsysCosOrlReference_Object = MibTableColumn
etsysCosOrlReference = _EtsysCosOrlReference_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 3, 5, 1, 7),
    _EtsysCosOrlReference_Type()
)
etsysCosOrlReference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysCosOrlReference.setStatus("current")


class _EtsysCosDropPrecedence_Type(Integer32):
    """Custom type etsysCosDropPrecedence based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 255),
    )


_EtsysCosDropPrecedence_Type.__name__ = "Integer32"
_EtsysCosDropPrecedence_Object = MibTableColumn
etsysCosDropPrecedence = _EtsysCosDropPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 3, 5, 1, 8),
    _EtsysCosDropPrecedence_Type()
)
etsysCosDropPrecedence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysCosDropPrecedence.setStatus("current")


class _EtsysCosFloodControlStatus_Type(EnabledStatus):
    """Custom type etsysCosFloodControlStatus based on EnabledStatus"""


_EtsysCosFloodControlStatus_Object = MibTableColumn
etsysCosFloodControlStatus = _EtsysCosFloodControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 3, 5, 1, 9),
    _EtsysCosFloodControlStatus_Type()
)
etsysCosFloodControlStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysCosFloodControlStatus.setStatus("current")
_EtsysCosTxq_ObjectIdentity = ObjectIdentity
etsysCosTxq = _EtsysCosTxq_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 4)
)


class _EtsysCosTxqNumPortTypes_Type(Integer32):
    """Custom type etsysCosTxqNumPortTypes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2048),
    )


_EtsysCosTxqNumPortTypes_Type.__name__ = "Integer32"
_EtsysCosTxqNumPortTypes_Object = MibScalar
etsysCosTxqNumPortTypes = _EtsysCosTxqNumPortTypes_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 4, 1),
    _EtsysCosTxqNumPortTypes_Type()
)
etsysCosTxqNumPortTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysCosTxqNumPortTypes.setStatus("current")
_EtsysCosTxqPortTypeTable_Object = MibTable
etsysCosTxqPortTypeTable = _EtsysCosTxqPortTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 4, 2)
)
if mibBuilder.loadTexts:
    etsysCosTxqPortTypeTable.setStatus("current")
_EtsysCosTxqPortTypeEntry_Object = MibTableRow
etsysCosTxqPortTypeEntry = _EtsysCosTxqPortTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 4, 2, 1)
)
etsysCosTxqPortTypeEntry.setIndexNames(
    (0, "ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosTxqPortTypeIndex"),
)
if mibBuilder.loadTexts:
    etsysCosTxqPortTypeEntry.setStatus("current")


class _EtsysCosTxqPortTypeIndex_Type(Integer32):
    """Custom type etsysCosTxqPortTypeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_EtsysCosTxqPortTypeIndex_Type.__name__ = "Integer32"
_EtsysCosTxqPortTypeIndex_Object = MibTableColumn
etsysCosTxqPortTypeIndex = _EtsysCosTxqPortTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 4, 2, 1, 1),
    _EtsysCosTxqPortTypeIndex_Type()
)
etsysCosTxqPortTypeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysCosTxqPortTypeIndex.setStatus("current")
_EtsysCosTxqPortTypeDescr_Type = SnmpAdminString
_EtsysCosTxqPortTypeDescr_Object = MibTableColumn
etsysCosTxqPortTypeDescr = _EtsysCosTxqPortTypeDescr_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 4, 2, 1, 2),
    _EtsysCosTxqPortTypeDescr_Type()
)
etsysCosTxqPortTypeDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysCosTxqPortTypeDescr.setStatus("current")
_EtsysCosTxqPortTypeEligiblePorts_Type = PortList
_EtsysCosTxqPortTypeEligiblePorts_Object = MibTableColumn
etsysCosTxqPortTypeEligiblePorts = _EtsysCosTxqPortTypeEligiblePorts_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 4, 2, 1, 3),
    _EtsysCosTxqPortTypeEligiblePorts_Type()
)
etsysCosTxqPortTypeEligiblePorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysCosTxqPortTypeEligiblePorts.setStatus("current")
_EtsysCosTxqPortTypeUnselectedPorts_Type = PortList
_EtsysCosTxqPortTypeUnselectedPorts_Object = MibTableColumn
etsysCosTxqPortTypeUnselectedPorts = _EtsysCosTxqPortTypeUnselectedPorts_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 4, 2, 1, 4),
    _EtsysCosTxqPortTypeUnselectedPorts_Type()
)
etsysCosTxqPortTypeUnselectedPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysCosTxqPortTypeUnselectedPorts.setStatus("current")
_EtsysCosTxqPortTypeNumberOfQueues_Type = Integer32
_EtsysCosTxqPortTypeNumberOfQueues_Object = MibTableColumn
etsysCosTxqPortTypeNumberOfQueues = _EtsysCosTxqPortTypeNumberOfQueues_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 4, 2, 1, 5),
    _EtsysCosTxqPortTypeNumberOfQueues_Type()
)
etsysCosTxqPortTypeNumberOfQueues.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysCosTxqPortTypeNumberOfQueues.setStatus("current")
_EtsysCosTxqPortTypeSupportedRateTypes_Type = EtsysCosRateTypes
_EtsysCosTxqPortTypeSupportedRateTypes_Object = MibTableColumn
etsysCosTxqPortTypeSupportedRateTypes = _EtsysCosTxqPortTypeSupportedRateTypes_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 4, 2, 1, 6),
    _EtsysCosTxqPortTypeSupportedRateTypes_Type()
)
etsysCosTxqPortTypeSupportedRateTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysCosTxqPortTypeSupportedRateTypes.setStatus("current")
_EtsysCosTxqPortTypeNumberOfSlices_Type = Integer32
_EtsysCosTxqPortTypeNumberOfSlices_Object = MibTableColumn
etsysCosTxqPortTypeNumberOfSlices = _EtsysCosTxqPortTypeNumberOfSlices_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 4, 2, 1, 7),
    _EtsysCosTxqPortTypeNumberOfSlices_Type()
)
etsysCosTxqPortTypeNumberOfSlices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysCosTxqPortTypeNumberOfSlices.setStatus("current")
_EtsysCosTxqPortTypeQueueAlgorithms_Type = TxqAlgorithms
_EtsysCosTxqPortTypeQueueAlgorithms_Object = MibTableColumn
etsysCosTxqPortTypeQueueAlgorithms = _EtsysCosTxqPortTypeQueueAlgorithms_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 4, 2, 1, 8),
    _EtsysCosTxqPortTypeQueueAlgorithms_Type()
)
etsysCosTxqPortTypeQueueAlgorithms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysCosTxqPortTypeQueueAlgorithms.setStatus("current")
_EtsysCosTxqPortTypeQueueArbiterModes_Type = TxqArbiterModes
_EtsysCosTxqPortTypeQueueArbiterModes_Object = MibTableColumn
etsysCosTxqPortTypeQueueArbiterModes = _EtsysCosTxqPortTypeQueueArbiterModes_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 4, 2, 1, 9),
    _EtsysCosTxqPortTypeQueueArbiterModes_Type()
)
etsysCosTxqPortTypeQueueArbiterModes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysCosTxqPortTypeQueueArbiterModes.setStatus("current")


class _EtsysCosTxqPortTypeMaxDropPrecedence_Type(Unsigned32):
    """Custom type etsysCosTxqPortTypeMaxDropPrecedence based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_EtsysCosTxqPortTypeMaxDropPrecedence_Type.__name__ = "Unsigned32"
_EtsysCosTxqPortTypeMaxDropPrecedence_Object = MibTableColumn
etsysCosTxqPortTypeMaxDropPrecedence = _EtsysCosTxqPortTypeMaxDropPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 4, 2, 1, 10),
    _EtsysCosTxqPortTypeMaxDropPrecedence_Type()
)
etsysCosTxqPortTypeMaxDropPrecedence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysCosTxqPortTypeMaxDropPrecedence.setStatus("current")
_EtsysCosTxqPortTypeLLQEligibleQueues_Type = TxQueueList
_EtsysCosTxqPortTypeLLQEligibleQueues_Object = MibTableColumn
etsysCosTxqPortTypeLLQEligibleQueues = _EtsysCosTxqPortTypeLLQEligibleQueues_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 4, 2, 1, 11),
    _EtsysCosTxqPortTypeLLQEligibleQueues_Type()
)
etsysCosTxqPortTypeLLQEligibleQueues.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysCosTxqPortTypeLLQEligibleQueues.setStatus("current")
_EtsysCosTxqUnitTable_Object = MibTable
etsysCosTxqUnitTable = _EtsysCosTxqUnitTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 4, 3)
)
if mibBuilder.loadTexts:
    etsysCosTxqUnitTable.setStatus("current")
_EtsysCosTxqUnitEntry_Object = MibTableRow
etsysCosTxqUnitEntry = _EtsysCosTxqUnitEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 4, 3, 1)
)
etsysCosTxqUnitEntry.setIndexNames(
    (0, "ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosTxqPortTypeIndex"),
    (0, "ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosTxqUnitTypeIndex"),
)
if mibBuilder.loadTexts:
    etsysCosTxqUnitEntry.setStatus("current")
_EtsysCosTxqUnitTypeIndex_Type = EtsysCosRateTypes
_EtsysCosTxqUnitTypeIndex_Object = MibTableColumn
etsysCosTxqUnitTypeIndex = _EtsysCosTxqUnitTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 4, 3, 1, 1),
    _EtsysCosTxqUnitTypeIndex_Type()
)
etsysCosTxqUnitTypeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysCosTxqUnitTypeIndex.setStatus("current")
_EtsysCosTxqUnitMaxRate_Type = Unsigned32
_EtsysCosTxqUnitMaxRate_Object = MibTableColumn
etsysCosTxqUnitMaxRate = _EtsysCosTxqUnitMaxRate_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 4, 3, 1, 2),
    _EtsysCosTxqUnitMaxRate_Type()
)
etsysCosTxqUnitMaxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysCosTxqUnitMaxRate.setStatus("current")
_EtsysCosTxqUnitMinRate_Type = Unsigned32
_EtsysCosTxqUnitMinRate_Object = MibTableColumn
etsysCosTxqUnitMinRate = _EtsysCosTxqUnitMinRate_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 4, 3, 1, 3),
    _EtsysCosTxqUnitMinRate_Type()
)
etsysCosTxqUnitMinRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysCosTxqUnitMinRate.setStatus("current")
_EtsysCosTxqUnitGranularity_Type = Unsigned32
_EtsysCosTxqUnitGranularity_Object = MibTableColumn
etsysCosTxqUnitGranularity = _EtsysCosTxqUnitGranularity_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 4, 3, 1, 4),
    _EtsysCosTxqUnitGranularity_Type()
)
etsysCosTxqUnitGranularity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysCosTxqUnitGranularity.setStatus("current")
_EtsysCosTxqMaxPortGroups_Type = Unsigned32
_EtsysCosTxqMaxPortGroups_Object = MibScalar
etsysCosTxqMaxPortGroups = _EtsysCosTxqMaxPortGroups_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 4, 4),
    _EtsysCosTxqMaxPortGroups_Type()
)
etsysCosTxqMaxPortGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysCosTxqMaxPortGroups.setStatus("current")
_EtsysCosTxqNumPortGroups_Type = Gauge32
_EtsysCosTxqNumPortGroups_Object = MibScalar
etsysCosTxqNumPortGroups = _EtsysCosTxqNumPortGroups_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 4, 5),
    _EtsysCosTxqNumPortGroups_Type()
)
etsysCosTxqNumPortGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysCosTxqNumPortGroups.setStatus("current")
_EtsysCosTxqPortGroupLastChange_Type = TimeStamp
_EtsysCosTxqPortGroupLastChange_Object = MibScalar
etsysCosTxqPortGroupLastChange = _EtsysCosTxqPortGroupLastChange_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 4, 6),
    _EtsysCosTxqPortGroupLastChange_Type()
)
etsysCosTxqPortGroupLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysCosTxqPortGroupLastChange.setStatus("current")
_EtsysCosTxqPortGroupTable_Object = MibTable
etsysCosTxqPortGroupTable = _EtsysCosTxqPortGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 4, 7)
)
if mibBuilder.loadTexts:
    etsysCosTxqPortGroupTable.setStatus("current")
_EtsysCosTxqPortGroupEntry_Object = MibTableRow
etsysCosTxqPortGroupEntry = _EtsysCosTxqPortGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 4, 7, 1)
)
etsysCosTxqPortGroupEntry.setIndexNames(
    (0, "ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosTxqPortGroupIndex"),
    (0, "ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosTxqPortTypeIndex"),
)
if mibBuilder.loadTexts:
    etsysCosTxqPortGroupEntry.setStatus("current")


class _EtsysCosTxqPortGroupIndex_Type(Integer32):
    """Custom type etsysCosTxqPortGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 32767),
    )


_EtsysCosTxqPortGroupIndex_Type.__name__ = "Integer32"
_EtsysCosTxqPortGroupIndex_Object = MibTableColumn
etsysCosTxqPortGroupIndex = _EtsysCosTxqPortGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 4, 7, 1, 1),
    _EtsysCosTxqPortGroupIndex_Type()
)
etsysCosTxqPortGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysCosTxqPortGroupIndex.setStatus("current")
_EtsysCosTxqPortGroupRowStatus_Type = RowStatus
_EtsysCosTxqPortGroupRowStatus_Object = MibTableColumn
etsysCosTxqPortGroupRowStatus = _EtsysCosTxqPortGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 4, 7, 1, 2),
    _EtsysCosTxqPortGroupRowStatus_Type()
)
etsysCosTxqPortGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysCosTxqPortGroupRowStatus.setStatus("current")


class _EtsysCosTxqPortGroupList_Type(PortList):
    """Custom type etsysCosTxqPortGroupList based on PortList"""
    defaultHexValue = ""


_EtsysCosTxqPortGroupList_Object = MibTableColumn
etsysCosTxqPortGroupList = _EtsysCosTxqPortGroupList_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 4, 7, 1, 3),
    _EtsysCosTxqPortGroupList_Type()
)
etsysCosTxqPortGroupList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysCosTxqPortGroupList.setStatus("current")


class _EtsysCosTxqPortGroupName_Type(SnmpAdminString):
    """Custom type etsysCosTxqPortGroupName based on SnmpAdminString"""
    defaultHexValue = ""


_EtsysCosTxqPortGroupName_Object = MibTableColumn
etsysCosTxqPortGroupName = _EtsysCosTxqPortGroupName_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 4, 7, 1, 4),
    _EtsysCosTxqPortGroupName_Type()
)
etsysCosTxqPortGroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysCosTxqPortGroupName.setStatus("current")
_EtsysCosTxqPortCfgTable_Object = MibTable
etsysCosTxqPortCfgTable = _EtsysCosTxqPortCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 4, 8)
)
if mibBuilder.loadTexts:
    etsysCosTxqPortCfgTable.setStatus("current")
_EtsysCosTxqPortCfgEntry_Object = MibTableRow
etsysCosTxqPortCfgEntry = _EtsysCosTxqPortCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 4, 8, 1)
)
etsysCosTxqPortCfgEntry.setIndexNames(
    (0, "ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosTxqPortGroupIndex"),
    (0, "ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosTxqPortTypeIndex"),
)
if mibBuilder.loadTexts:
    etsysCosTxqPortCfgEntry.setStatus("current")
_EtsysCosTxqPortArbMode_Type = TxqArbiterModes
_EtsysCosTxqPortArbMode_Object = MibTableColumn
etsysCosTxqPortArbMode = _EtsysCosTxqPortArbMode_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 4, 8, 1, 1),
    _EtsysCosTxqPortArbMode_Type()
)
etsysCosTxqPortArbMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysCosTxqPortArbMode.setStatus("current")


class _EtsysCosTxqPortSliceSetting_Type(OctetString):
    """Custom type etsysCosTxqPortSliceSetting based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )


_EtsysCosTxqPortSliceSetting_Type.__name__ = "OctetString"
_EtsysCosTxqPortSliceSetting_Object = MibTableColumn
etsysCosTxqPortSliceSetting = _EtsysCosTxqPortSliceSetting_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 4, 8, 1, 2),
    _EtsysCosTxqPortSliceSetting_Type()
)
etsysCosTxqPortSliceSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysCosTxqPortSliceSetting.setStatus("current")
_EtsysCosTxqResourceTable_Object = MibTable
etsysCosTxqResourceTable = _EtsysCosTxqResourceTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 4, 9)
)
if mibBuilder.loadTexts:
    etsysCosTxqResourceTable.setStatus("current")
_EtsysCosTxqResourceEntry_Object = MibTableRow
etsysCosTxqResourceEntry = _EtsysCosTxqResourceEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 4, 9, 1)
)
etsysCosTxqResourceEntry.setIndexNames(
    (0, "ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosTxqPortGroupIndex"),
    (0, "ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosTxqPortTypeIndex"),
    (0, "ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosTxqResourceQueueNum"),
)
if mibBuilder.loadTexts:
    etsysCosTxqResourceEntry.setStatus("current")


class _EtsysCosTxqResourceQueueNum_Type(Integer32):
    """Custom type etsysCosTxqResourceQueueNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_EtsysCosTxqResourceQueueNum_Type.__name__ = "Integer32"
_EtsysCosTxqResourceQueueNum_Object = MibTableColumn
etsysCosTxqResourceQueueNum = _EtsysCosTxqResourceQueueNum_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 4, 9, 1, 1),
    _EtsysCosTxqResourceQueueNum_Type()
)
etsysCosTxqResourceQueueNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysCosTxqResourceQueueNum.setStatus("current")
_EtsysCosTxqPortQUnit_Type = EtsysCosRateTypes
_EtsysCosTxqPortQUnit_Object = MibTableColumn
etsysCosTxqPortQUnit = _EtsysCosTxqPortQUnit_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 4, 9, 1, 2),
    _EtsysCosTxqPortQUnit_Type()
)
etsysCosTxqPortQUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysCosTxqPortQUnit.setStatus("current")


class _EtsysCosTxqPortQRate_Type(Integer32):
    """Custom type etsysCosTxqPortQRate based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 2147483647),
    )


_EtsysCosTxqPortQRate_Type.__name__ = "Integer32"
_EtsysCosTxqPortQRate_Object = MibTableColumn
etsysCosTxqPortQRate = _EtsysCosTxqPortQRate_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 4, 9, 1, 3),
    _EtsysCosTxqPortQRate_Type()
)
etsysCosTxqPortQRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysCosTxqPortQRate.setStatus("current")
_EtsysCosTxqPortQAlgorithm_Type = TxqAlgorithms
_EtsysCosTxqPortQAlgorithm_Object = MibTableColumn
etsysCosTxqPortQAlgorithm = _EtsysCosTxqPortQAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 4, 9, 1, 4),
    _EtsysCosTxqPortQAlgorithm_Type()
)
etsysCosTxqPortQAlgorithm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysCosTxqPortQAlgorithm.setStatus("current")
_EtsysCosTxqPortQLLQenable_Type = EnabledStatus
_EtsysCosTxqPortQLLQenable_Object = MibTableColumn
etsysCosTxqPortQLLQenable = _EtsysCosTxqPortQLLQenable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 4, 9, 1, 5),
    _EtsysCosTxqPortQLLQenable_Type()
)
etsysCosTxqPortQLLQenable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysCosTxqPortQLLQenable.setStatus("current")
_EtsysCosTxqReferenceMappingMaxReference_Type = Unsigned32
_EtsysCosTxqReferenceMappingMaxReference_Object = MibScalar
etsysCosTxqReferenceMappingMaxReference = _EtsysCosTxqReferenceMappingMaxReference_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 4, 10),
    _EtsysCosTxqReferenceMappingMaxReference_Type()
)
etsysCosTxqReferenceMappingMaxReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysCosTxqReferenceMappingMaxReference.setStatus("current")
_EtsysCosTxqReferenceMappingTable_Object = MibTable
etsysCosTxqReferenceMappingTable = _EtsysCosTxqReferenceMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 4, 11)
)
if mibBuilder.loadTexts:
    etsysCosTxqReferenceMappingTable.setStatus("current")
_EtsysCosTxqReferenceMappingEntry_Object = MibTableRow
etsysCosTxqReferenceMappingEntry = _EtsysCosTxqReferenceMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 4, 11, 1)
)
etsysCosTxqReferenceMappingEntry.setIndexNames(
    (0, "ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosTxqPortGroupIndex"),
    (0, "ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosTxqPortTypeIndex"),
    (0, "ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosTxqReference"),
)
if mibBuilder.loadTexts:
    etsysCosTxqReferenceMappingEntry.setStatus("current")


class _EtsysCosTxqResourceQueueNumber_Type(Integer32):
    """Custom type etsysCosTxqResourceQueueNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_EtsysCosTxqResourceQueueNumber_Type.__name__ = "Integer32"
_EtsysCosTxqResourceQueueNumber_Object = MibTableColumn
etsysCosTxqResourceQueueNumber = _EtsysCosTxqResourceQueueNumber_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 4, 11, 1, 1),
    _EtsysCosTxqResourceQueueNumber_Type()
)
etsysCosTxqResourceQueueNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysCosTxqResourceQueueNumber.setStatus("current")
_EtsysCosTxqDropProfilesMaxEntries_Type = Unsigned32
_EtsysCosTxqDropProfilesMaxEntries_Object = MibScalar
etsysCosTxqDropProfilesMaxEntries = _EtsysCosTxqDropProfilesMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 4, 12),
    _EtsysCosTxqDropProfilesMaxEntries_Type()
)
etsysCosTxqDropProfilesMaxEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysCosTxqDropProfilesMaxEntries.setStatus("current")
_EtsysCosTxqDropProfilesNumEntries_Type = Gauge32
_EtsysCosTxqDropProfilesNumEntries_Object = MibScalar
etsysCosTxqDropProfilesNumEntries = _EtsysCosTxqDropProfilesNumEntries_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 4, 13),
    _EtsysCosTxqDropProfilesNumEntries_Type()
)
etsysCosTxqDropProfilesNumEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysCosTxqDropProfilesNumEntries.setStatus("current")
_EtsysCosTxqDropProfilesLastChange_Type = TimeStamp
_EtsysCosTxqDropProfilesLastChange_Object = MibScalar
etsysCosTxqDropProfilesLastChange = _EtsysCosTxqDropProfilesLastChange_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 4, 14),
    _EtsysCosTxqDropProfilesLastChange_Type()
)
etsysCosTxqDropProfilesLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysCosTxqDropProfilesLastChange.setStatus("current")
_EtsysCosTxqDropProfilesTable_Object = MibTable
etsysCosTxqDropProfilesTable = _EtsysCosTxqDropProfilesTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 4, 15)
)
if mibBuilder.loadTexts:
    etsysCosTxqDropProfilesTable.setStatus("current")
_EtsysCosTxqDropProfilesEntry_Object = MibTableRow
etsysCosTxqDropProfilesEntry = _EtsysCosTxqDropProfilesEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 4, 15, 1)
)
etsysCosTxqDropProfilesEntry.setIndexNames(
    (0, "ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosTxqDropSettingIndex"),
)
if mibBuilder.loadTexts:
    etsysCosTxqDropProfilesEntry.setStatus("current")
_EtsysCosTxqDropSettingIndex_Type = Unsigned32
_EtsysCosTxqDropSettingIndex_Object = MibTableColumn
etsysCosTxqDropSettingIndex = _EtsysCosTxqDropSettingIndex_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 4, 15, 1, 1),
    _EtsysCosTxqDropSettingIndex_Type()
)
etsysCosTxqDropSettingIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysCosTxqDropSettingIndex.setStatus("current")
_EtsysCosTxqDropProfilesRowStatus_Type = RowStatus
_EtsysCosTxqDropProfilesRowStatus_Object = MibTableColumn
etsysCosTxqDropProfilesRowStatus = _EtsysCosTxqDropProfilesRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 4, 15, 1, 2),
    _EtsysCosTxqDropProfilesRowStatus_Type()
)
etsysCosTxqDropProfilesRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysCosTxqDropProfilesRowStatus.setStatus("current")


class _EtsysCosTxqDropProfilesMin_Type(Integer32):
    """Custom type etsysCosTxqDropProfilesMin based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_EtsysCosTxqDropProfilesMin_Type.__name__ = "Integer32"
_EtsysCosTxqDropProfilesMin_Object = MibTableColumn
etsysCosTxqDropProfilesMin = _EtsysCosTxqDropProfilesMin_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 4, 15, 1, 3),
    _EtsysCosTxqDropProfilesMin_Type()
)
etsysCosTxqDropProfilesMin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysCosTxqDropProfilesMin.setStatus("current")


class _EtsysCosTxqDropProfilesMax_Type(Integer32):
    """Custom type etsysCosTxqDropProfilesMax based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_EtsysCosTxqDropProfilesMax_Type.__name__ = "Integer32"
_EtsysCosTxqDropProfilesMax_Object = MibTableColumn
etsysCosTxqDropProfilesMax = _EtsysCosTxqDropProfilesMax_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 4, 15, 1, 4),
    _EtsysCosTxqDropProfilesMax_Type()
)
etsysCosTxqDropProfilesMax.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysCosTxqDropProfilesMax.setStatus("current")


class _EtsysCosTxqDropProfilesMaxDropProb_Type(Integer32):
    """Custom type etsysCosTxqDropProfilesMaxDropProb based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_EtsysCosTxqDropProfilesMaxDropProb_Type.__name__ = "Integer32"
_EtsysCosTxqDropProfilesMaxDropProb_Object = MibTableColumn
etsysCosTxqDropProfilesMaxDropProb = _EtsysCosTxqDropProfilesMaxDropProb_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 4, 15, 1, 5),
    _EtsysCosTxqDropProfilesMaxDropProb_Type()
)
etsysCosTxqDropProfilesMaxDropProb.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysCosTxqDropProfilesMaxDropProb.setStatus("current")


class _EtsysCosTxqDropProfilesQueueDepthAtMaxProb_Type(Integer32):
    """Custom type etsysCosTxqDropProfilesQueueDepthAtMaxProb based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_EtsysCosTxqDropProfilesQueueDepthAtMaxProb_Type.__name__ = "Integer32"
_EtsysCosTxqDropProfilesQueueDepthAtMaxProb_Object = MibTableColumn
etsysCosTxqDropProfilesQueueDepthAtMaxProb = _EtsysCosTxqDropProfilesQueueDepthAtMaxProb_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 4, 15, 1, 6),
    _EtsysCosTxqDropProfilesQueueDepthAtMaxProb_Type()
)
etsysCosTxqDropProfilesQueueDepthAtMaxProb.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysCosTxqDropProfilesQueueDepthAtMaxProb.setStatus("current")
_EtsysCosTxqDropPrecedenceTable_Object = MibTable
etsysCosTxqDropPrecedenceTable = _EtsysCosTxqDropPrecedenceTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 4, 16)
)
if mibBuilder.loadTexts:
    etsysCosTxqDropPrecedenceTable.setStatus("current")
_EtsysCosTxqDropPrecedenceEntry_Object = MibTableRow
etsysCosTxqDropPrecedenceEntry = _EtsysCosTxqDropPrecedenceEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 4, 16, 1)
)
etsysCosTxqDropPrecedenceEntry.setIndexNames(
    (0, "ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosTxqPortGroupIndex"),
    (0, "ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosTxqPortTypeIndex"),
    (0, "ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosTxqResourceQueueNum"),
    (0, "ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosTableDropPrecedence"),
)
if mibBuilder.loadTexts:
    etsysCosTxqDropPrecedenceEntry.setStatus("current")
_EtsysCosTableDropPrecedence_Type = Unsigned32
_EtsysCosTableDropPrecedence_Object = MibTableColumn
etsysCosTableDropPrecedence = _EtsysCosTableDropPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 4, 16, 1, 1),
    _EtsysCosTableDropPrecedence_Type()
)
etsysCosTableDropPrecedence.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysCosTableDropPrecedence.setStatus("current")
_EtsysCosTxqDropProfileQueueCfgID_Type = Integer32
_EtsysCosTxqDropProfileQueueCfgID_Object = MibTableColumn
etsysCosTxqDropProfileQueueCfgID = _EtsysCosTxqDropProfileQueueCfgID_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 4, 16, 1, 2),
    _EtsysCosTxqDropProfileQueueCfgID_Type()
)
etsysCosTxqDropProfileQueueCfgID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysCosTxqDropProfileQueueCfgID.setStatus("current")
_EtsysCosIrl_ObjectIdentity = ObjectIdentity
etsysCosIrl = _EtsysCosIrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 5)
)
_EtsysCosIrlPortTypeMaxEntries_Type = Unsigned32
_EtsysCosIrlPortTypeMaxEntries_Object = MibScalar
etsysCosIrlPortTypeMaxEntries = _EtsysCosIrlPortTypeMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 5, 1),
    _EtsysCosIrlPortTypeMaxEntries_Type()
)
etsysCosIrlPortTypeMaxEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysCosIrlPortTypeMaxEntries.setStatus("current")
_EtsysCosIrlPortTypeTable_Object = MibTable
etsysCosIrlPortTypeTable = _EtsysCosIrlPortTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 5, 2)
)
if mibBuilder.loadTexts:
    etsysCosIrlPortTypeTable.setStatus("current")
_EtsysCosIrlPortTypeEntry_Object = MibTableRow
etsysCosIrlPortTypeEntry = _EtsysCosIrlPortTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 5, 2, 1)
)
etsysCosIrlPortTypeEntry.setIndexNames(
    (0, "ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosIrlPortTypeIndex"),
)
if mibBuilder.loadTexts:
    etsysCosIrlPortTypeEntry.setStatus("current")


class _EtsysCosIrlPortTypeIndex_Type(Integer32):
    """Custom type etsysCosIrlPortTypeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_EtsysCosIrlPortTypeIndex_Type.__name__ = "Integer32"
_EtsysCosIrlPortTypeIndex_Object = MibTableColumn
etsysCosIrlPortTypeIndex = _EtsysCosIrlPortTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 5, 2, 1, 1),
    _EtsysCosIrlPortTypeIndex_Type()
)
etsysCosIrlPortTypeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysCosIrlPortTypeIndex.setStatus("current")
_EtsysCosIrlPortTypeDescr_Type = SnmpAdminString
_EtsysCosIrlPortTypeDescr_Object = MibTableColumn
etsysCosIrlPortTypeDescr = _EtsysCosIrlPortTypeDescr_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 5, 2, 1, 2),
    _EtsysCosIrlPortTypeDescr_Type()
)
etsysCosIrlPortTypeDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysCosIrlPortTypeDescr.setStatus("current")
_EtsysCosIrlPortTypeEligiblePorts_Type = PortList
_EtsysCosIrlPortTypeEligiblePorts_Object = MibTableColumn
etsysCosIrlPortTypeEligiblePorts = _EtsysCosIrlPortTypeEligiblePorts_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 5, 2, 1, 3),
    _EtsysCosIrlPortTypeEligiblePorts_Type()
)
etsysCosIrlPortTypeEligiblePorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysCosIrlPortTypeEligiblePorts.setStatus("current")
_EtsysCosIrlPortTypeUnselectedPorts_Type = PortList
_EtsysCosIrlPortTypeUnselectedPorts_Object = MibTableColumn
etsysCosIrlPortTypeUnselectedPorts = _EtsysCosIrlPortTypeUnselectedPorts_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 5, 2, 1, 4),
    _EtsysCosIrlPortTypeUnselectedPorts_Type()
)
etsysCosIrlPortTypeUnselectedPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysCosIrlPortTypeUnselectedPorts.setStatus("current")


class _EtsysCosIrlPortTypeNumberOfIRLs_Type(Integer32):
    """Custom type etsysCosIrlPortTypeNumberOfIRLs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_EtsysCosIrlPortTypeNumberOfIRLs_Type.__name__ = "Integer32"
_EtsysCosIrlPortTypeNumberOfIRLs_Object = MibTableColumn
etsysCosIrlPortTypeNumberOfIRLs = _EtsysCosIrlPortTypeNumberOfIRLs_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 5, 2, 1, 5),
    _EtsysCosIrlPortTypeNumberOfIRLs_Type()
)
etsysCosIrlPortTypeNumberOfIRLs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysCosIrlPortTypeNumberOfIRLs.setStatus("current")
_EtsysCosIrlPortTypeSupportedRateTypes_Type = EtsysCosRateTypes
_EtsysCosIrlPortTypeSupportedRateTypes_Object = MibTableColumn
etsysCosIrlPortTypeSupportedRateTypes = _EtsysCosIrlPortTypeSupportedRateTypes_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 5, 2, 1, 6),
    _EtsysCosIrlPortTypeSupportedRateTypes_Type()
)
etsysCosIrlPortTypeSupportedRateTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysCosIrlPortTypeSupportedRateTypes.setStatus("current")
_EtsysCosIrlPortTypeCapabilities_Type = EtsysCosRlCapabilities
_EtsysCosIrlPortTypeCapabilities_Object = MibTableColumn
etsysCosIrlPortTypeCapabilities = _EtsysCosIrlPortTypeCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 5, 2, 1, 7),
    _EtsysCosIrlPortTypeCapabilities_Type()
)
etsysCosIrlPortTypeCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysCosIrlPortTypeCapabilities.setStatus("current")
_EtsysCosIrlUnitTable_Object = MibTable
etsysCosIrlUnitTable = _EtsysCosIrlUnitTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 5, 3)
)
if mibBuilder.loadTexts:
    etsysCosIrlUnitTable.setStatus("current")
_EtsysCosIrlUnitEntry_Object = MibTableRow
etsysCosIrlUnitEntry = _EtsysCosIrlUnitEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 5, 3, 1)
)
etsysCosIrlUnitEntry.setIndexNames(
    (0, "ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosIrlPortTypeIndex"),
    (0, "ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosIrlUnitTypeIndex"),
)
if mibBuilder.loadTexts:
    etsysCosIrlUnitEntry.setStatus("current")
_EtsysCosIrlUnitTypeIndex_Type = EtsysCosRateTypes
_EtsysCosIrlUnitTypeIndex_Object = MibTableColumn
etsysCosIrlUnitTypeIndex = _EtsysCosIrlUnitTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 5, 3, 1, 1),
    _EtsysCosIrlUnitTypeIndex_Type()
)
etsysCosIrlUnitTypeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysCosIrlUnitTypeIndex.setStatus("current")
_EtsysCosIrlUnitMaxRate_Type = Unsigned32
_EtsysCosIrlUnitMaxRate_Object = MibTableColumn
etsysCosIrlUnitMaxRate = _EtsysCosIrlUnitMaxRate_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 5, 3, 1, 2),
    _EtsysCosIrlUnitMaxRate_Type()
)
etsysCosIrlUnitMaxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysCosIrlUnitMaxRate.setStatus("current")
_EtsysCosIrlUnitMinRate_Type = Unsigned32
_EtsysCosIrlUnitMinRate_Object = MibTableColumn
etsysCosIrlUnitMinRate = _EtsysCosIrlUnitMinRate_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 5, 3, 1, 3),
    _EtsysCosIrlUnitMinRate_Type()
)
etsysCosIrlUnitMinRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysCosIrlUnitMinRate.setStatus("current")
_EtsysCosIrlUnitGranularity_Type = Unsigned32
_EtsysCosIrlUnitGranularity_Object = MibTableColumn
etsysCosIrlUnitGranularity = _EtsysCosIrlUnitGranularity_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 5, 3, 1, 4),
    _EtsysCosIrlUnitGranularity_Type()
)
etsysCosIrlUnitGranularity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysCosIrlUnitGranularity.setStatus("current")
_EtsysCosIrlPortGroupMaxEntries_Type = Unsigned32
_EtsysCosIrlPortGroupMaxEntries_Object = MibScalar
etsysCosIrlPortGroupMaxEntries = _EtsysCosIrlPortGroupMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 5, 4),
    _EtsysCosIrlPortGroupMaxEntries_Type()
)
etsysCosIrlPortGroupMaxEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysCosIrlPortGroupMaxEntries.setStatus("current")
_EtsysCosIrlPortGroupNumEntries_Type = Gauge32
_EtsysCosIrlPortGroupNumEntries_Object = MibScalar
etsysCosIrlPortGroupNumEntries = _EtsysCosIrlPortGroupNumEntries_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 5, 5),
    _EtsysCosIrlPortGroupNumEntries_Type()
)
etsysCosIrlPortGroupNumEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysCosIrlPortGroupNumEntries.setStatus("current")
_EtsysCosIrlPortGroupLastChange_Type = TimeStamp
_EtsysCosIrlPortGroupLastChange_Object = MibScalar
etsysCosIrlPortGroupLastChange = _EtsysCosIrlPortGroupLastChange_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 5, 6),
    _EtsysCosIrlPortGroupLastChange_Type()
)
etsysCosIrlPortGroupLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysCosIrlPortGroupLastChange.setStatus("current")
_EtsysCosIrlPortGroupTable_Object = MibTable
etsysCosIrlPortGroupTable = _EtsysCosIrlPortGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 5, 7)
)
if mibBuilder.loadTexts:
    etsysCosIrlPortGroupTable.setStatus("current")
_EtsysCosIrlPortGroupEntry_Object = MibTableRow
etsysCosIrlPortGroupEntry = _EtsysCosIrlPortGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 5, 7, 1)
)
etsysCosIrlPortGroupEntry.setIndexNames(
    (0, "ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosIrlPortGroupIndex"),
    (0, "ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosIrlPortTypeIndex"),
)
if mibBuilder.loadTexts:
    etsysCosIrlPortGroupEntry.setStatus("current")


class _EtsysCosIrlPortGroupIndex_Type(Integer32):
    """Custom type etsysCosIrlPortGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 32767),
    )


_EtsysCosIrlPortGroupIndex_Type.__name__ = "Integer32"
_EtsysCosIrlPortGroupIndex_Object = MibTableColumn
etsysCosIrlPortGroupIndex = _EtsysCosIrlPortGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 5, 7, 1, 1),
    _EtsysCosIrlPortGroupIndex_Type()
)
etsysCosIrlPortGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysCosIrlPortGroupIndex.setStatus("current")
_EtsysCosIrlPortGroupRowStatus_Type = RowStatus
_EtsysCosIrlPortGroupRowStatus_Object = MibTableColumn
etsysCosIrlPortGroupRowStatus = _EtsysCosIrlPortGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 5, 7, 1, 2),
    _EtsysCosIrlPortGroupRowStatus_Type()
)
etsysCosIrlPortGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysCosIrlPortGroupRowStatus.setStatus("current")


class _EtsysCosIrlPortGroupList_Type(PortList):
    """Custom type etsysCosIrlPortGroupList based on PortList"""
    defaultHexValue = ""


_EtsysCosIrlPortGroupList_Object = MibTableColumn
etsysCosIrlPortGroupList = _EtsysCosIrlPortGroupList_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 5, 7, 1, 3),
    _EtsysCosIrlPortGroupList_Type()
)
etsysCosIrlPortGroupList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysCosIrlPortGroupList.setStatus("current")


class _EtsysCosIrlPortGroupName_Type(SnmpAdminString):
    """Custom type etsysCosIrlPortGroupName based on SnmpAdminString"""
    defaultHexValue = ""


_EtsysCosIrlPortGroupName_Object = MibTableColumn
etsysCosIrlPortGroupName = _EtsysCosIrlPortGroupName_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 5, 7, 1, 4),
    _EtsysCosIrlPortGroupName_Type()
)
etsysCosIrlPortGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysCosIrlPortGroupName.setStatus("current")
_EtsysCosIrlPortCfgTable_Object = MibTable
etsysCosIrlPortCfgTable = _EtsysCosIrlPortCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 5, 8)
)
if mibBuilder.loadTexts:
    etsysCosIrlPortCfgTable.setStatus("current")
_EtsysCosIrlPortCfgEntry_Object = MibTableRow
etsysCosIrlPortCfgEntry = _EtsysCosIrlPortCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 5, 8, 1)
)
etsysCosIrlPortCfgEntry.setIndexNames(
    (0, "ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosIrlPortGroupIndex"),
    (0, "ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosIrlPortTypeIndex"),
)
if mibBuilder.loadTexts:
    etsysCosIrlPortCfgEntry.setStatus("current")


class _EtsysCosIrlPortCfgFloodLimiter_Type(Integer32):
    """Custom type etsysCosIrlPortCfgFloodLimiter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 65535),
    )


_EtsysCosIrlPortCfgFloodLimiter_Type.__name__ = "Integer32"
_EtsysCosIrlPortCfgFloodLimiter_Object = MibTableColumn
etsysCosIrlPortCfgFloodLimiter = _EtsysCosIrlPortCfgFloodLimiter_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 5, 8, 1, 2),
    _EtsysCosIrlPortCfgFloodLimiter_Type()
)
etsysCosIrlPortCfgFloodLimiter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysCosIrlPortCfgFloodLimiter.setStatus("deprecated")
_EtsysCosIrlResourceTable_Object = MibTable
etsysCosIrlResourceTable = _EtsysCosIrlResourceTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 5, 9)
)
if mibBuilder.loadTexts:
    etsysCosIrlResourceTable.setStatus("current")
_EtsysCosIrlResourceEntry_Object = MibTableRow
etsysCosIrlResourceEntry = _EtsysCosIrlResourceEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 5, 9, 1)
)
etsysCosIrlResourceEntry.setIndexNames(
    (0, "ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosIrlPortGroupIndex"),
    (0, "ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosIrlPortTypeIndex"),
    (0, "ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosIrlResourceIrlNum"),
)
if mibBuilder.loadTexts:
    etsysCosIrlResourceEntry.setStatus("current")
_EtsysCosIrlResourceIrlNum_Type = Unsigned32
_EtsysCosIrlResourceIrlNum_Object = MibTableColumn
etsysCosIrlResourceIrlNum = _EtsysCosIrlResourceIrlNum_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 5, 9, 1, 1),
    _EtsysCosIrlResourceIrlNum_Type()
)
etsysCosIrlResourceIrlNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysCosIrlResourceIrlNum.setStatus("current")


class _EtsysCosIrlResourceUnits_Type(EtsysCosRateTypes):
    """Custom type etsysCosIrlResourceUnits based on EtsysCosRateTypes"""
    defaultBinValue = "01"


_EtsysCosIrlResourceUnits_Object = MibTableColumn
etsysCosIrlResourceUnits = _EtsysCosIrlResourceUnits_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 5, 9, 1, 2),
    _EtsysCosIrlResourceUnits_Type()
)
etsysCosIrlResourceUnits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysCosIrlResourceUnits.setStatus("current")


class _EtsysCosIrlResourceRate_Type(Integer32):
    """Custom type etsysCosIrlResourceRate based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 2147483647),
    )


_EtsysCosIrlResourceRate_Type.__name__ = "Integer32"
_EtsysCosIrlResourceRate_Object = MibTableColumn
etsysCosIrlResourceRate = _EtsysCosIrlResourceRate_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 5, 9, 1, 3),
    _EtsysCosIrlResourceRate_Type()
)
etsysCosIrlResourceRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysCosIrlResourceRate.setStatus("current")


class _EtsysCosIrlResourceParentIrl_Type(Integer32):
    """Custom type etsysCosIrlResourceParentIrl based on Integer32"""
    defaultValue = -1


_EtsysCosIrlResourceParentIrl_Object = MibTableColumn
etsysCosIrlResourceParentIrl = _EtsysCosIrlResourceParentIrl_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 5, 9, 1, 4),
    _EtsysCosIrlResourceParentIrl_Type()
)
etsysCosIrlResourceParentIrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysCosIrlResourceParentIrl.setStatus("current")
_EtsysCosIrlResourceType_Type = EtsysRateLimitingType
_EtsysCosIrlResourceType_Object = MibTableColumn
etsysCosIrlResourceType = _EtsysCosIrlResourceType_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 5, 9, 1, 5),
    _EtsysCosIrlResourceType_Type()
)
etsysCosIrlResourceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysCosIrlResourceType.setStatus("current")


class _EtsysCosIrlResourceActionCosIndex_Type(Integer32):
    """Custom type etsysCosIrlResourceActionCosIndex based on Integer32"""
    defaultValue = -1


_EtsysCosIrlResourceActionCosIndex_Object = MibTableColumn
etsysCosIrlResourceActionCosIndex = _EtsysCosIrlResourceActionCosIndex_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 5, 9, 1, 6),
    _EtsysCosIrlResourceActionCosIndex_Type()
)
etsysCosIrlResourceActionCosIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysCosIrlResourceActionCosIndex.setStatus("current")
_EtsysCosIrlResourceAction_Type = EtsysViolationAction
_EtsysCosIrlResourceAction_Object = MibTableColumn
etsysCosIrlResourceAction = _EtsysCosIrlResourceAction_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 5, 9, 1, 7),
    _EtsysCosIrlResourceAction_Type()
)
etsysCosIrlResourceAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysCosIrlResourceAction.setStatus("current")
_EtsysCosIrlResourceViolationPortList_Type = PortList
_EtsysCosIrlResourceViolationPortList_Object = MibTableColumn
etsysCosIrlResourceViolationPortList = _EtsysCosIrlResourceViolationPortList_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 5, 9, 1, 8),
    _EtsysCosIrlResourceViolationPortList_Type()
)
etsysCosIrlResourceViolationPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysCosIrlResourceViolationPortList.setStatus("current")
_EtsysCosIrlResourceClearCounters_Type = TruthValue
_EtsysCosIrlResourceClearCounters_Object = MibTableColumn
etsysCosIrlResourceClearCounters = _EtsysCosIrlResourceClearCounters_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 5, 9, 1, 9),
    _EtsysCosIrlResourceClearCounters_Type()
)
etsysCosIrlResourceClearCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysCosIrlResourceClearCounters.setStatus("current")
_EtsysCosIrlReferenceMappingMaxReference_Type = Unsigned32
_EtsysCosIrlReferenceMappingMaxReference_Object = MibScalar
etsysCosIrlReferenceMappingMaxReference = _EtsysCosIrlReferenceMappingMaxReference_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 5, 10),
    _EtsysCosIrlReferenceMappingMaxReference_Type()
)
etsysCosIrlReferenceMappingMaxReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysCosIrlReferenceMappingMaxReference.setStatus("current")
_EtsysCosIrlReferenceMappingLastChange_Type = TimeStamp
_EtsysCosIrlReferenceMappingLastChange_Object = MibScalar
etsysCosIrlReferenceMappingLastChange = _EtsysCosIrlReferenceMappingLastChange_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 5, 11),
    _EtsysCosIrlReferenceMappingLastChange_Type()
)
etsysCosIrlReferenceMappingLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysCosIrlReferenceMappingLastChange.setStatus("current")
_EtsysCosIrlReferenceMappingTable_Object = MibTable
etsysCosIrlReferenceMappingTable = _EtsysCosIrlReferenceMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 5, 12)
)
if mibBuilder.loadTexts:
    etsysCosIrlReferenceMappingTable.setStatus("current")
_EtsysCosIrlReferenceMappingEntry_Object = MibTableRow
etsysCosIrlReferenceMappingEntry = _EtsysCosIrlReferenceMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 5, 12, 1)
)
etsysCosIrlReferenceMappingEntry.setIndexNames(
    (0, "ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosIrlPortGroupIndex"),
    (0, "ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosIrlPortTypeIndex"),
    (0, "ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosIrlReference"),
)
if mibBuilder.loadTexts:
    etsysCosIrlReferenceMappingEntry.setStatus("current")


class _EtsysCosIrlResourceIrlNumber_Type(Integer32):
    """Custom type etsysCosIrlResourceIrlNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 32767),
    )


_EtsysCosIrlResourceIrlNumber_Type.__name__ = "Integer32"
_EtsysCosIrlResourceIrlNumber_Object = MibTableColumn
etsysCosIrlResourceIrlNumber = _EtsysCosIrlResourceIrlNumber_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 5, 12, 1, 1),
    _EtsysCosIrlResourceIrlNumber_Type()
)
etsysCosIrlResourceIrlNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysCosIrlResourceIrlNumber.setStatus("current")
_EtsysCosIrlViolationClearTable_Type = TruthValue
_EtsysCosIrlViolationClearTable_Object = MibScalar
etsysCosIrlViolationClearTable = _EtsysCosIrlViolationClearTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 5, 13),
    _EtsysCosIrlViolationClearTable_Type()
)
etsysCosIrlViolationClearTable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysCosIrlViolationClearTable.setStatus("current")
_EtsysCosIrlViolationLastChange_Type = TimeStamp
_EtsysCosIrlViolationLastChange_Object = MibScalar
etsysCosIrlViolationLastChange = _EtsysCosIrlViolationLastChange_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 5, 14),
    _EtsysCosIrlViolationLastChange_Type()
)
etsysCosIrlViolationLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysCosIrlViolationLastChange.setStatus("current")
_EtsysCosIrlDisabledPortsList_Type = PortList
_EtsysCosIrlDisabledPortsList_Object = MibScalar
etsysCosIrlDisabledPortsList = _EtsysCosIrlDisabledPortsList_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 5, 15),
    _EtsysCosIrlDisabledPortsList_Type()
)
etsysCosIrlDisabledPortsList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysCosIrlDisabledPortsList.setStatus("current")
_EtsysCosIrlViolationTable_Object = MibTable
etsysCosIrlViolationTable = _EtsysCosIrlViolationTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 5, 16)
)
if mibBuilder.loadTexts:
    etsysCosIrlViolationTable.setStatus("current")
_EtsysCosIrlViolationEntry_Object = MibTableRow
etsysCosIrlViolationEntry = _EtsysCosIrlViolationEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 5, 16, 1)
)
etsysCosIrlViolationEntry.setIndexNames(
    (0, "ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosIrlPortIndex"),
    (0, "ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosIrlResourceIrlNumber"),
)
if mibBuilder.loadTexts:
    etsysCosIrlViolationEntry.setStatus("current")


class _EtsysCosIrlPortIndex_Type(Integer32):
    """Custom type etsysCosIrlPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_EtsysCosIrlPortIndex_Type.__name__ = "Integer32"
_EtsysCosIrlPortIndex_Object = MibTableColumn
etsysCosIrlPortIndex = _EtsysCosIrlPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 5, 16, 1, 1),
    _EtsysCosIrlPortIndex_Type()
)
etsysCosIrlPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysCosIrlPortIndex.setStatus("current")
_EtsysCosIrlViolation_Type = TruthValue
_EtsysCosIrlViolation_Object = MibTableColumn
etsysCosIrlViolation = _EtsysCosIrlViolation_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 5, 16, 1, 2),
    _EtsysCosIrlViolation_Type()
)
etsysCosIrlViolation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysCosIrlViolation.setStatus("current")
_EtsysCosIrlCounter_Type = Counter64
_EtsysCosIrlCounter_Object = MibTableColumn
etsysCosIrlCounter = _EtsysCosIrlCounter_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 5, 16, 1, 3),
    _EtsysCosIrlCounter_Type()
)
etsysCosIrlCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysCosIrlCounter.setStatus("current")
_EtsysCosIrlResetFlags_Type = EtsysRateLimitResetBits
_EtsysCosIrlResetFlags_Object = MibTableColumn
etsysCosIrlResetFlags = _EtsysCosIrlResetFlags_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 5, 16, 1, 4),
    _EtsysCosIrlResetFlags_Type()
)
etsysCosIrlResetFlags.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysCosIrlResetFlags.setStatus("current")
_EtsysCosOrl_ObjectIdentity = ObjectIdentity
etsysCosOrl = _EtsysCosOrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 6)
)
_EtsysCosOrlPortTypeMaxEntries_Type = Unsigned32
_EtsysCosOrlPortTypeMaxEntries_Object = MibScalar
etsysCosOrlPortTypeMaxEntries = _EtsysCosOrlPortTypeMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 6, 1),
    _EtsysCosOrlPortTypeMaxEntries_Type()
)
etsysCosOrlPortTypeMaxEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysCosOrlPortTypeMaxEntries.setStatus("current")
_EtsysCosOrlPortTypeTable_Object = MibTable
etsysCosOrlPortTypeTable = _EtsysCosOrlPortTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 6, 2)
)
if mibBuilder.loadTexts:
    etsysCosOrlPortTypeTable.setStatus("current")
_EtsysCosOrlPortTypeEntry_Object = MibTableRow
etsysCosOrlPortTypeEntry = _EtsysCosOrlPortTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 6, 2, 1)
)
etsysCosOrlPortTypeEntry.setIndexNames(
    (0, "ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosOrlPortTypeIndex"),
)
if mibBuilder.loadTexts:
    etsysCosOrlPortTypeEntry.setStatus("current")


class _EtsysCosOrlPortTypeIndex_Type(Integer32):
    """Custom type etsysCosOrlPortTypeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_EtsysCosOrlPortTypeIndex_Type.__name__ = "Integer32"
_EtsysCosOrlPortTypeIndex_Object = MibTableColumn
etsysCosOrlPortTypeIndex = _EtsysCosOrlPortTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 6, 2, 1, 1),
    _EtsysCosOrlPortTypeIndex_Type()
)
etsysCosOrlPortTypeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysCosOrlPortTypeIndex.setStatus("current")
_EtsysCosOrlPortTypeDescr_Type = SnmpAdminString
_EtsysCosOrlPortTypeDescr_Object = MibTableColumn
etsysCosOrlPortTypeDescr = _EtsysCosOrlPortTypeDescr_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 6, 2, 1, 2),
    _EtsysCosOrlPortTypeDescr_Type()
)
etsysCosOrlPortTypeDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysCosOrlPortTypeDescr.setStatus("current")
_EtsysCosOrlPortTypeEligiblePorts_Type = PortList
_EtsysCosOrlPortTypeEligiblePorts_Object = MibTableColumn
etsysCosOrlPortTypeEligiblePorts = _EtsysCosOrlPortTypeEligiblePorts_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 6, 2, 1, 3),
    _EtsysCosOrlPortTypeEligiblePorts_Type()
)
etsysCosOrlPortTypeEligiblePorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysCosOrlPortTypeEligiblePorts.setStatus("current")
_EtsysCosOrlPortTypeUnselectedPorts_Type = PortList
_EtsysCosOrlPortTypeUnselectedPorts_Object = MibTableColumn
etsysCosOrlPortTypeUnselectedPorts = _EtsysCosOrlPortTypeUnselectedPorts_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 6, 2, 1, 4),
    _EtsysCosOrlPortTypeUnselectedPorts_Type()
)
etsysCosOrlPortTypeUnselectedPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysCosOrlPortTypeUnselectedPorts.setStatus("current")


class _EtsysCosOrlPortTypeNumberOfORLs_Type(Integer32):
    """Custom type etsysCosOrlPortTypeNumberOfORLs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_EtsysCosOrlPortTypeNumberOfORLs_Type.__name__ = "Integer32"
_EtsysCosOrlPortTypeNumberOfORLs_Object = MibTableColumn
etsysCosOrlPortTypeNumberOfORLs = _EtsysCosOrlPortTypeNumberOfORLs_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 6, 2, 1, 5),
    _EtsysCosOrlPortTypeNumberOfORLs_Type()
)
etsysCosOrlPortTypeNumberOfORLs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysCosOrlPortTypeNumberOfORLs.setStatus("current")
_EtsysCosOrlPortTypeSupportedRateTypes_Type = EtsysCosRateTypes
_EtsysCosOrlPortTypeSupportedRateTypes_Object = MibTableColumn
etsysCosOrlPortTypeSupportedRateTypes = _EtsysCosOrlPortTypeSupportedRateTypes_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 6, 2, 1, 6),
    _EtsysCosOrlPortTypeSupportedRateTypes_Type()
)
etsysCosOrlPortTypeSupportedRateTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysCosOrlPortTypeSupportedRateTypes.setStatus("current")
_EtsysCosOrlPortTypeCapabilities_Type = EtsysCosRlCapabilities
_EtsysCosOrlPortTypeCapabilities_Object = MibTableColumn
etsysCosOrlPortTypeCapabilities = _EtsysCosOrlPortTypeCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 6, 2, 1, 7),
    _EtsysCosOrlPortTypeCapabilities_Type()
)
etsysCosOrlPortTypeCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysCosOrlPortTypeCapabilities.setStatus("current")
_EtsysCosOrlUnitTable_Object = MibTable
etsysCosOrlUnitTable = _EtsysCosOrlUnitTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 6, 3)
)
if mibBuilder.loadTexts:
    etsysCosOrlUnitTable.setStatus("current")
_EtsysCosOrlUnitEntry_Object = MibTableRow
etsysCosOrlUnitEntry = _EtsysCosOrlUnitEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 6, 3, 1)
)
etsysCosOrlUnitEntry.setIndexNames(
    (0, "ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosOrlPortTypeIndex"),
    (0, "ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosOrlUnitTypeIndex"),
)
if mibBuilder.loadTexts:
    etsysCosOrlUnitEntry.setStatus("current")
_EtsysCosOrlUnitTypeIndex_Type = EtsysCosRateTypes
_EtsysCosOrlUnitTypeIndex_Object = MibTableColumn
etsysCosOrlUnitTypeIndex = _EtsysCosOrlUnitTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 6, 3, 1, 1),
    _EtsysCosOrlUnitTypeIndex_Type()
)
etsysCosOrlUnitTypeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysCosOrlUnitTypeIndex.setStatus("current")
_EtsysCosOrlUnitMaxRate_Type = Unsigned32
_EtsysCosOrlUnitMaxRate_Object = MibTableColumn
etsysCosOrlUnitMaxRate = _EtsysCosOrlUnitMaxRate_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 6, 3, 1, 2),
    _EtsysCosOrlUnitMaxRate_Type()
)
etsysCosOrlUnitMaxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysCosOrlUnitMaxRate.setStatus("current")
_EtsysCosOrlUnitMinRate_Type = Unsigned32
_EtsysCosOrlUnitMinRate_Object = MibTableColumn
etsysCosOrlUnitMinRate = _EtsysCosOrlUnitMinRate_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 6, 3, 1, 3),
    _EtsysCosOrlUnitMinRate_Type()
)
etsysCosOrlUnitMinRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysCosOrlUnitMinRate.setStatus("current")
_EtsysCosOrlUnitGranularity_Type = Unsigned32
_EtsysCosOrlUnitGranularity_Object = MibTableColumn
etsysCosOrlUnitGranularity = _EtsysCosOrlUnitGranularity_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 6, 3, 1, 4),
    _EtsysCosOrlUnitGranularity_Type()
)
etsysCosOrlUnitGranularity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysCosOrlUnitGranularity.setStatus("current")
_EtsysCosOrlPortGroupMaxEntries_Type = Unsigned32
_EtsysCosOrlPortGroupMaxEntries_Object = MibScalar
etsysCosOrlPortGroupMaxEntries = _EtsysCosOrlPortGroupMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 6, 4),
    _EtsysCosOrlPortGroupMaxEntries_Type()
)
etsysCosOrlPortGroupMaxEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysCosOrlPortGroupMaxEntries.setStatus("current")
_EtsysCosOrlPortGroupNumEntries_Type = Gauge32
_EtsysCosOrlPortGroupNumEntries_Object = MibScalar
etsysCosOrlPortGroupNumEntries = _EtsysCosOrlPortGroupNumEntries_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 6, 5),
    _EtsysCosOrlPortGroupNumEntries_Type()
)
etsysCosOrlPortGroupNumEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysCosOrlPortGroupNumEntries.setStatus("current")
_EtsysCosOrlPortGroupLastChange_Type = TimeStamp
_EtsysCosOrlPortGroupLastChange_Object = MibScalar
etsysCosOrlPortGroupLastChange = _EtsysCosOrlPortGroupLastChange_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 6, 6),
    _EtsysCosOrlPortGroupLastChange_Type()
)
etsysCosOrlPortGroupLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysCosOrlPortGroupLastChange.setStatus("current")
_EtsysCosOrlPortGroupTable_Object = MibTable
etsysCosOrlPortGroupTable = _EtsysCosOrlPortGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 6, 7)
)
if mibBuilder.loadTexts:
    etsysCosOrlPortGroupTable.setStatus("current")
_EtsysCosOrlPortGroupEntry_Object = MibTableRow
etsysCosOrlPortGroupEntry = _EtsysCosOrlPortGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 6, 7, 1)
)
etsysCosOrlPortGroupEntry.setIndexNames(
    (0, "ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosOrlPortGroupIndex"),
    (0, "ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosOrlPortTypeIndex"),
)
if mibBuilder.loadTexts:
    etsysCosOrlPortGroupEntry.setStatus("current")


class _EtsysCosOrlPortGroupIndex_Type(Integer32):
    """Custom type etsysCosOrlPortGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 32767),
    )


_EtsysCosOrlPortGroupIndex_Type.__name__ = "Integer32"
_EtsysCosOrlPortGroupIndex_Object = MibTableColumn
etsysCosOrlPortGroupIndex = _EtsysCosOrlPortGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 6, 7, 1, 1),
    _EtsysCosOrlPortGroupIndex_Type()
)
etsysCosOrlPortGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysCosOrlPortGroupIndex.setStatus("current")
_EtsysCosOrlPortGroupRowStatus_Type = RowStatus
_EtsysCosOrlPortGroupRowStatus_Object = MibTableColumn
etsysCosOrlPortGroupRowStatus = _EtsysCosOrlPortGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 6, 7, 1, 2),
    _EtsysCosOrlPortGroupRowStatus_Type()
)
etsysCosOrlPortGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysCosOrlPortGroupRowStatus.setStatus("current")


class _EtsysCosOrlPortGroupList_Type(PortList):
    """Custom type etsysCosOrlPortGroupList based on PortList"""
    defaultHexValue = ""


_EtsysCosOrlPortGroupList_Object = MibTableColumn
etsysCosOrlPortGroupList = _EtsysCosOrlPortGroupList_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 6, 7, 1, 3),
    _EtsysCosOrlPortGroupList_Type()
)
etsysCosOrlPortGroupList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysCosOrlPortGroupList.setStatus("current")


class _EtsysCosOrlPortGroupName_Type(SnmpAdminString):
    """Custom type etsysCosOrlPortGroupName based on SnmpAdminString"""
    defaultHexValue = ""


_EtsysCosOrlPortGroupName_Object = MibTableColumn
etsysCosOrlPortGroupName = _EtsysCosOrlPortGroupName_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 6, 7, 1, 4),
    _EtsysCosOrlPortGroupName_Type()
)
etsysCosOrlPortGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysCosOrlPortGroupName.setStatus("current")
_EtsysCosOrlPortCfgTable_Object = MibTable
etsysCosOrlPortCfgTable = _EtsysCosOrlPortCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 6, 8)
)
if mibBuilder.loadTexts:
    etsysCosOrlPortCfgTable.setStatus("current")
_EtsysCosOrlPortCfgEntry_Object = MibTableRow
etsysCosOrlPortCfgEntry = _EtsysCosOrlPortCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 6, 8, 1)
)
etsysCosOrlPortCfgEntry.setIndexNames(
    (0, "ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosOrlPortGroupIndex"),
    (0, "ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosOrlPortTypeIndex"),
)
if mibBuilder.loadTexts:
    etsysCosOrlPortCfgEntry.setStatus("current")


class _EtsysCosOrlPortCfgFloodLimiter_Type(Integer32):
    """Custom type etsysCosOrlPortCfgFloodLimiter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 65535),
    )


_EtsysCosOrlPortCfgFloodLimiter_Type.__name__ = "Integer32"
_EtsysCosOrlPortCfgFloodLimiter_Object = MibTableColumn
etsysCosOrlPortCfgFloodLimiter = _EtsysCosOrlPortCfgFloodLimiter_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 6, 8, 1, 2),
    _EtsysCosOrlPortCfgFloodLimiter_Type()
)
etsysCosOrlPortCfgFloodLimiter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysCosOrlPortCfgFloodLimiter.setStatus("current")
_EtsysCosOrlResourceTable_Object = MibTable
etsysCosOrlResourceTable = _EtsysCosOrlResourceTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 6, 9)
)
if mibBuilder.loadTexts:
    etsysCosOrlResourceTable.setStatus("current")
_EtsysCosOrlResourceEntry_Object = MibTableRow
etsysCosOrlResourceEntry = _EtsysCosOrlResourceEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 6, 9, 1)
)
etsysCosOrlResourceEntry.setIndexNames(
    (0, "ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosOrlPortGroupIndex"),
    (0, "ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosOrlPortTypeIndex"),
    (0, "ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosOrlResourceOrlNum"),
)
if mibBuilder.loadTexts:
    etsysCosOrlResourceEntry.setStatus("current")
_EtsysCosOrlResourceOrlNum_Type = Unsigned32
_EtsysCosOrlResourceOrlNum_Object = MibTableColumn
etsysCosOrlResourceOrlNum = _EtsysCosOrlResourceOrlNum_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 6, 9, 1, 1),
    _EtsysCosOrlResourceOrlNum_Type()
)
etsysCosOrlResourceOrlNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysCosOrlResourceOrlNum.setStatus("current")


class _EtsysCosOrlResourceUnits_Type(EtsysCosRateTypes):
    """Custom type etsysCosOrlResourceUnits based on EtsysCosRateTypes"""
    defaultBinValue = "01"


_EtsysCosOrlResourceUnits_Object = MibTableColumn
etsysCosOrlResourceUnits = _EtsysCosOrlResourceUnits_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 6, 9, 1, 2),
    _EtsysCosOrlResourceUnits_Type()
)
etsysCosOrlResourceUnits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysCosOrlResourceUnits.setStatus("current")


class _EtsysCosOrlResourceRate_Type(Integer32):
    """Custom type etsysCosOrlResourceRate based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 2147483647),
    )


_EtsysCosOrlResourceRate_Type.__name__ = "Integer32"
_EtsysCosOrlResourceRate_Object = MibTableColumn
etsysCosOrlResourceRate = _EtsysCosOrlResourceRate_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 6, 9, 1, 3),
    _EtsysCosOrlResourceRate_Type()
)
etsysCosOrlResourceRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysCosOrlResourceRate.setStatus("current")


class _EtsysCosOrlResourceParentOrl_Type(Integer32):
    """Custom type etsysCosOrlResourceParentOrl based on Integer32"""
    defaultValue = -1


_EtsysCosOrlResourceParentOrl_Object = MibTableColumn
etsysCosOrlResourceParentOrl = _EtsysCosOrlResourceParentOrl_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 6, 9, 1, 4),
    _EtsysCosOrlResourceParentOrl_Type()
)
etsysCosOrlResourceParentOrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysCosOrlResourceParentOrl.setStatus("current")
_EtsysCosOrlResourceType_Type = EtsysRateLimitingType
_EtsysCosOrlResourceType_Object = MibTableColumn
etsysCosOrlResourceType = _EtsysCosOrlResourceType_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 6, 9, 1, 5),
    _EtsysCosOrlResourceType_Type()
)
etsysCosOrlResourceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysCosOrlResourceType.setStatus("current")


class _EtsysCosOrlResourceActionCosIndex_Type(Integer32):
    """Custom type etsysCosOrlResourceActionCosIndex based on Integer32"""
    defaultValue = -1


_EtsysCosOrlResourceActionCosIndex_Object = MibTableColumn
etsysCosOrlResourceActionCosIndex = _EtsysCosOrlResourceActionCosIndex_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 6, 9, 1, 6),
    _EtsysCosOrlResourceActionCosIndex_Type()
)
etsysCosOrlResourceActionCosIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysCosOrlResourceActionCosIndex.setStatus("current")
_EtsysCosOrlResourceAction_Type = EtsysViolationAction
_EtsysCosOrlResourceAction_Object = MibTableColumn
etsysCosOrlResourceAction = _EtsysCosOrlResourceAction_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 6, 9, 1, 7),
    _EtsysCosOrlResourceAction_Type()
)
etsysCosOrlResourceAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysCosOrlResourceAction.setStatus("current")
_EtsysCosOrlResourceViolationPortList_Type = PortList
_EtsysCosOrlResourceViolationPortList_Object = MibTableColumn
etsysCosOrlResourceViolationPortList = _EtsysCosOrlResourceViolationPortList_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 6, 9, 1, 8),
    _EtsysCosOrlResourceViolationPortList_Type()
)
etsysCosOrlResourceViolationPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysCosOrlResourceViolationPortList.setStatus("current")
_EtsysCosOrlResourceClearCounters_Type = TruthValue
_EtsysCosOrlResourceClearCounters_Object = MibTableColumn
etsysCosOrlResourceClearCounters = _EtsysCosOrlResourceClearCounters_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 6, 9, 1, 9),
    _EtsysCosOrlResourceClearCounters_Type()
)
etsysCosOrlResourceClearCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysCosOrlResourceClearCounters.setStatus("current")
_EtsysCosOrlReferenceMappingMaxReference_Type = Unsigned32
_EtsysCosOrlReferenceMappingMaxReference_Object = MibScalar
etsysCosOrlReferenceMappingMaxReference = _EtsysCosOrlReferenceMappingMaxReference_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 6, 10),
    _EtsysCosOrlReferenceMappingMaxReference_Type()
)
etsysCosOrlReferenceMappingMaxReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysCosOrlReferenceMappingMaxReference.setStatus("current")
_EtsysCosOrlReferenceMappingLastChange_Type = TimeStamp
_EtsysCosOrlReferenceMappingLastChange_Object = MibScalar
etsysCosOrlReferenceMappingLastChange = _EtsysCosOrlReferenceMappingLastChange_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 6, 11),
    _EtsysCosOrlReferenceMappingLastChange_Type()
)
etsysCosOrlReferenceMappingLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysCosOrlReferenceMappingLastChange.setStatus("current")
_EtsysCosOrlReferenceMappingTable_Object = MibTable
etsysCosOrlReferenceMappingTable = _EtsysCosOrlReferenceMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 6, 12)
)
if mibBuilder.loadTexts:
    etsysCosOrlReferenceMappingTable.setStatus("current")
_EtsysCosOrlReferenceMappingEntry_Object = MibTableRow
etsysCosOrlReferenceMappingEntry = _EtsysCosOrlReferenceMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 6, 12, 1)
)
etsysCosOrlReferenceMappingEntry.setIndexNames(
    (0, "ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosOrlPortGroupIndex"),
    (0, "ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosOrlPortTypeIndex"),
    (0, "ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosOrlReference"),
)
if mibBuilder.loadTexts:
    etsysCosOrlReferenceMappingEntry.setStatus("current")


class _EtsysCosOrlResourceOrlNumber_Type(Integer32):
    """Custom type etsysCosOrlResourceOrlNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 32767),
    )


_EtsysCosOrlResourceOrlNumber_Type.__name__ = "Integer32"
_EtsysCosOrlResourceOrlNumber_Object = MibTableColumn
etsysCosOrlResourceOrlNumber = _EtsysCosOrlResourceOrlNumber_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 6, 12, 1, 1),
    _EtsysCosOrlResourceOrlNumber_Type()
)
etsysCosOrlResourceOrlNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysCosOrlResourceOrlNumber.setStatus("current")
_EtsysCosOrlViolationClearTable_Type = TruthValue
_EtsysCosOrlViolationClearTable_Object = MibScalar
etsysCosOrlViolationClearTable = _EtsysCosOrlViolationClearTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 6, 13),
    _EtsysCosOrlViolationClearTable_Type()
)
etsysCosOrlViolationClearTable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysCosOrlViolationClearTable.setStatus("current")
_EtsysCosOrlViolationLastChange_Type = TimeStamp
_EtsysCosOrlViolationLastChange_Object = MibScalar
etsysCosOrlViolationLastChange = _EtsysCosOrlViolationLastChange_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 6, 14),
    _EtsysCosOrlViolationLastChange_Type()
)
etsysCosOrlViolationLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysCosOrlViolationLastChange.setStatus("current")
_EtsysCosOrlDisabledPortsList_Type = PortList
_EtsysCosOrlDisabledPortsList_Object = MibScalar
etsysCosOrlDisabledPortsList = _EtsysCosOrlDisabledPortsList_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 6, 15),
    _EtsysCosOrlDisabledPortsList_Type()
)
etsysCosOrlDisabledPortsList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysCosOrlDisabledPortsList.setStatus("current")
_EtsysCosOrlViolationTable_Object = MibTable
etsysCosOrlViolationTable = _EtsysCosOrlViolationTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 6, 16)
)
if mibBuilder.loadTexts:
    etsysCosOrlViolationTable.setStatus("current")
_EtsysCosOrlViolationEntry_Object = MibTableRow
etsysCosOrlViolationEntry = _EtsysCosOrlViolationEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 6, 16, 1)
)
etsysCosOrlViolationEntry.setIndexNames(
    (0, "ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosOrlPortIndex"),
    (0, "ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosOrlResourceOrlNumber"),
)
if mibBuilder.loadTexts:
    etsysCosOrlViolationEntry.setStatus("current")


class _EtsysCosOrlPortIndex_Type(Integer32):
    """Custom type etsysCosOrlPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_EtsysCosOrlPortIndex_Type.__name__ = "Integer32"
_EtsysCosOrlPortIndex_Object = MibTableColumn
etsysCosOrlPortIndex = _EtsysCosOrlPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 6, 16, 1, 1),
    _EtsysCosOrlPortIndex_Type()
)
etsysCosOrlPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysCosOrlPortIndex.setStatus("current")
_EtsysCosOrlViolation_Type = TruthValue
_EtsysCosOrlViolation_Object = MibTableColumn
etsysCosOrlViolation = _EtsysCosOrlViolation_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 6, 16, 1, 2),
    _EtsysCosOrlViolation_Type()
)
etsysCosOrlViolation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysCosOrlViolation.setStatus("current")
_EtsysCosOrlCounter_Type = Counter64
_EtsysCosOrlCounter_Object = MibTableColumn
etsysCosOrlCounter = _EtsysCosOrlCounter_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 6, 16, 1, 3),
    _EtsysCosOrlCounter_Type()
)
etsysCosOrlCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysCosOrlCounter.setStatus("current")
_EtsysCosOrlResetFlags_Type = EtsysRateLimitResetBits
_EtsysCosOrlResetFlags_Object = MibTableColumn
etsysCosOrlResetFlags = _EtsysCosOrlResetFlags_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 6, 16, 1, 4),
    _EtsysCosOrlResetFlags_Type()
)
etsysCosOrlResetFlags.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysCosOrlResetFlags.setStatus("current")
_EtsysCosFloodControl_ObjectIdentity = ObjectIdentity
etsysCosFloodControl = _EtsysCosFloodControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 7)
)
_EtsysCosFloodCtrlPortTypeMaxEntries_Type = Unsigned32
_EtsysCosFloodCtrlPortTypeMaxEntries_Object = MibScalar
etsysCosFloodCtrlPortTypeMaxEntries = _EtsysCosFloodCtrlPortTypeMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 7, 1),
    _EtsysCosFloodCtrlPortTypeMaxEntries_Type()
)
etsysCosFloodCtrlPortTypeMaxEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysCosFloodCtrlPortTypeMaxEntries.setStatus("current")
_EtsysCosFloodCtrlPortTypeTable_Object = MibTable
etsysCosFloodCtrlPortTypeTable = _EtsysCosFloodCtrlPortTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 7, 2)
)
if mibBuilder.loadTexts:
    etsysCosFloodCtrlPortTypeTable.setStatus("current")
_EtsysCosFloodCtrlPortTypeEntry_Object = MibTableRow
etsysCosFloodCtrlPortTypeEntry = _EtsysCosFloodCtrlPortTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 7, 2, 1)
)
etsysCosFloodCtrlPortTypeEntry.setIndexNames(
    (0, "ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosFloodCtrlPortTypeIndex"),
)
if mibBuilder.loadTexts:
    etsysCosFloodCtrlPortTypeEntry.setStatus("current")


class _EtsysCosFloodCtrlPortTypeIndex_Type(Integer32):
    """Custom type etsysCosFloodCtrlPortTypeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_EtsysCosFloodCtrlPortTypeIndex_Type.__name__ = "Integer32"
_EtsysCosFloodCtrlPortTypeIndex_Object = MibTableColumn
etsysCosFloodCtrlPortTypeIndex = _EtsysCosFloodCtrlPortTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 7, 2, 1, 1),
    _EtsysCosFloodCtrlPortTypeIndex_Type()
)
etsysCosFloodCtrlPortTypeIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    etsysCosFloodCtrlPortTypeIndex.setStatus("current")
_EtsysCosFloodCtrlPortTypeDescr_Type = SnmpAdminString
_EtsysCosFloodCtrlPortTypeDescr_Object = MibTableColumn
etsysCosFloodCtrlPortTypeDescr = _EtsysCosFloodCtrlPortTypeDescr_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 7, 2, 1, 2),
    _EtsysCosFloodCtrlPortTypeDescr_Type()
)
etsysCosFloodCtrlPortTypeDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysCosFloodCtrlPortTypeDescr.setStatus("current")
_EtsysCosFloodCtrlPortTypeEligiblePorts_Type = PortList
_EtsysCosFloodCtrlPortTypeEligiblePorts_Object = MibTableColumn
etsysCosFloodCtrlPortTypeEligiblePorts = _EtsysCosFloodCtrlPortTypeEligiblePorts_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 7, 2, 1, 3),
    _EtsysCosFloodCtrlPortTypeEligiblePorts_Type()
)
etsysCosFloodCtrlPortTypeEligiblePorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysCosFloodCtrlPortTypeEligiblePorts.setStatus("current")
_EtsysCosFloodCtrlPortTypeUnselectedPorts_Type = PortList
_EtsysCosFloodCtrlPortTypeUnselectedPorts_Object = MibTableColumn
etsysCosFloodCtrlPortTypeUnselectedPorts = _EtsysCosFloodCtrlPortTypeUnselectedPorts_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 7, 2, 1, 4),
    _EtsysCosFloodCtrlPortTypeUnselectedPorts_Type()
)
etsysCosFloodCtrlPortTypeUnselectedPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysCosFloodCtrlPortTypeUnselectedPorts.setStatus("current")
_EtsysCosFloodCtrlPortTypeSupportedRateTypes_Type = EtsysCosRateTypes
_EtsysCosFloodCtrlPortTypeSupportedRateTypes_Object = MibTableColumn
etsysCosFloodCtrlPortTypeSupportedRateTypes = _EtsysCosFloodCtrlPortTypeSupportedRateTypes_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 7, 2, 1, 5),
    _EtsysCosFloodCtrlPortTypeSupportedRateTypes_Type()
)
etsysCosFloodCtrlPortTypeSupportedRateTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysCosFloodCtrlPortTypeSupportedRateTypes.setStatus("current")
_EtsysCosFloodCtrlPortTypeCapabilities_Type = EtsysCosRlCapabilities
_EtsysCosFloodCtrlPortTypeCapabilities_Object = MibTableColumn
etsysCosFloodCtrlPortTypeCapabilities = _EtsysCosFloodCtrlPortTypeCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 7, 2, 1, 7),
    _EtsysCosFloodCtrlPortTypeCapabilities_Type()
)
etsysCosFloodCtrlPortTypeCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysCosFloodCtrlPortTypeCapabilities.setStatus("current")
_EtsysCosFloodCtrlUnitTable_Object = MibTable
etsysCosFloodCtrlUnitTable = _EtsysCosFloodCtrlUnitTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 7, 3)
)
if mibBuilder.loadTexts:
    etsysCosFloodCtrlUnitTable.setStatus("current")
_EtsysCosFloodCtrlUnitEntry_Object = MibTableRow
etsysCosFloodCtrlUnitEntry = _EtsysCosFloodCtrlUnitEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 7, 3, 1)
)
etsysCosFloodCtrlUnitEntry.setIndexNames(
    (0, "ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosFloodCtrlPortTypeIndex"),
    (0, "ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosFloodCtrlUnitTypeIndex"),
)
if mibBuilder.loadTexts:
    etsysCosFloodCtrlUnitEntry.setStatus("current")
_EtsysCosFloodCtrlUnitTypeIndex_Type = EtsysCosRateTypes
_EtsysCosFloodCtrlUnitTypeIndex_Object = MibTableColumn
etsysCosFloodCtrlUnitTypeIndex = _EtsysCosFloodCtrlUnitTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 7, 3, 1, 1),
    _EtsysCosFloodCtrlUnitTypeIndex_Type()
)
etsysCosFloodCtrlUnitTypeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysCosFloodCtrlUnitTypeIndex.setStatus("current")
_EtsysCosFloodCtrlUnitMaxRate_Type = Unsigned32
_EtsysCosFloodCtrlUnitMaxRate_Object = MibTableColumn
etsysCosFloodCtrlUnitMaxRate = _EtsysCosFloodCtrlUnitMaxRate_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 7, 3, 1, 2),
    _EtsysCosFloodCtrlUnitMaxRate_Type()
)
etsysCosFloodCtrlUnitMaxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysCosFloodCtrlUnitMaxRate.setStatus("current")
_EtsysCosFloodCtrlUnitMinRate_Type = Unsigned32
_EtsysCosFloodCtrlUnitMinRate_Object = MibTableColumn
etsysCosFloodCtrlUnitMinRate = _EtsysCosFloodCtrlUnitMinRate_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 7, 3, 1, 3),
    _EtsysCosFloodCtrlUnitMinRate_Type()
)
etsysCosFloodCtrlUnitMinRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysCosFloodCtrlUnitMinRate.setStatus("current")
_EtsysCosFloodCtrlUnitGranularity_Type = Unsigned32
_EtsysCosFloodCtrlUnitGranularity_Object = MibTableColumn
etsysCosFloodCtrlUnitGranularity = _EtsysCosFloodCtrlUnitGranularity_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 7, 3, 1, 4),
    _EtsysCosFloodCtrlUnitGranularity_Type()
)
etsysCosFloodCtrlUnitGranularity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysCosFloodCtrlUnitGranularity.setStatus("current")
_EtsysCosFloodCtrlPortGroupMaxEntries_Type = Unsigned32
_EtsysCosFloodCtrlPortGroupMaxEntries_Object = MibScalar
etsysCosFloodCtrlPortGroupMaxEntries = _EtsysCosFloodCtrlPortGroupMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 7, 4),
    _EtsysCosFloodCtrlPortGroupMaxEntries_Type()
)
etsysCosFloodCtrlPortGroupMaxEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysCosFloodCtrlPortGroupMaxEntries.setStatus("current")
_EtsysCosFloodCtrlPortGroupNumEntries_Type = Gauge32
_EtsysCosFloodCtrlPortGroupNumEntries_Object = MibScalar
etsysCosFloodCtrlPortGroupNumEntries = _EtsysCosFloodCtrlPortGroupNumEntries_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 7, 5),
    _EtsysCosFloodCtrlPortGroupNumEntries_Type()
)
etsysCosFloodCtrlPortGroupNumEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysCosFloodCtrlPortGroupNumEntries.setStatus("current")
_EtsysCosFloodCtrlPortGroupLastChange_Type = TimeStamp
_EtsysCosFloodCtrlPortGroupLastChange_Object = MibScalar
etsysCosFloodCtrlPortGroupLastChange = _EtsysCosFloodCtrlPortGroupLastChange_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 7, 6),
    _EtsysCosFloodCtrlPortGroupLastChange_Type()
)
etsysCosFloodCtrlPortGroupLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysCosFloodCtrlPortGroupLastChange.setStatus("current")
_EtsysCosFloodCtrlPortGroupTable_Object = MibTable
etsysCosFloodCtrlPortGroupTable = _EtsysCosFloodCtrlPortGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 7, 7)
)
if mibBuilder.loadTexts:
    etsysCosFloodCtrlPortGroupTable.setStatus("current")
_EtsysCosFloodCtrlPortGroupEntry_Object = MibTableRow
etsysCosFloodCtrlPortGroupEntry = _EtsysCosFloodCtrlPortGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 7, 7, 1)
)
etsysCosFloodCtrlPortGroupEntry.setIndexNames(
    (0, "ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosFloodCtrlPortGroupIndex"),
    (0, "ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosFloodCtrlPortTypeIndex"),
)
if mibBuilder.loadTexts:
    etsysCosFloodCtrlPortGroupEntry.setStatus("current")


class _EtsysCosFloodCtrlPortGroupIndex_Type(Integer32):
    """Custom type etsysCosFloodCtrlPortGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 32767),
    )


_EtsysCosFloodCtrlPortGroupIndex_Type.__name__ = "Integer32"
_EtsysCosFloodCtrlPortGroupIndex_Object = MibTableColumn
etsysCosFloodCtrlPortGroupIndex = _EtsysCosFloodCtrlPortGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 7, 7, 1, 1),
    _EtsysCosFloodCtrlPortGroupIndex_Type()
)
etsysCosFloodCtrlPortGroupIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    etsysCosFloodCtrlPortGroupIndex.setStatus("current")
_EtsysCosFloodCtrlPortGroupRowStatus_Type = RowStatus
_EtsysCosFloodCtrlPortGroupRowStatus_Object = MibTableColumn
etsysCosFloodCtrlPortGroupRowStatus = _EtsysCosFloodCtrlPortGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 7, 7, 1, 2),
    _EtsysCosFloodCtrlPortGroupRowStatus_Type()
)
etsysCosFloodCtrlPortGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysCosFloodCtrlPortGroupRowStatus.setStatus("current")


class _EtsysCosFloodCtrlPortGroupList_Type(PortList):
    """Custom type etsysCosFloodCtrlPortGroupList based on PortList"""
    defaultHexValue = ""


_EtsysCosFloodCtrlPortGroupList_Object = MibTableColumn
etsysCosFloodCtrlPortGroupList = _EtsysCosFloodCtrlPortGroupList_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 7, 7, 1, 3),
    _EtsysCosFloodCtrlPortGroupList_Type()
)
etsysCosFloodCtrlPortGroupList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysCosFloodCtrlPortGroupList.setStatus("current")


class _EtsysCosFloodCtrlPortGroupName_Type(SnmpAdminString):
    """Custom type etsysCosFloodCtrlPortGroupName based on SnmpAdminString"""
    defaultHexValue = ""


_EtsysCosFloodCtrlPortGroupName_Object = MibTableColumn
etsysCosFloodCtrlPortGroupName = _EtsysCosFloodCtrlPortGroupName_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 7, 7, 1, 4),
    _EtsysCosFloodCtrlPortGroupName_Type()
)
etsysCosFloodCtrlPortGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysCosFloodCtrlPortGroupName.setStatus("current")


class _EtsysCosFloodCtrlSyslogActionMsgFormat_Type(Integer32):
    """Custom type etsysCosFloodCtrlSyslogActionMsgFormat based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notification", 1),
          ("notificationWithPktHdr", 2))
    )


_EtsysCosFloodCtrlSyslogActionMsgFormat_Type.__name__ = "Integer32"
_EtsysCosFloodCtrlSyslogActionMsgFormat_Object = MibScalar
etsysCosFloodCtrlSyslogActionMsgFormat = _EtsysCosFloodCtrlSyslogActionMsgFormat_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 7, 8),
    _EtsysCosFloodCtrlSyslogActionMsgFormat_Type()
)
etsysCosFloodCtrlSyslogActionMsgFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysCosFloodCtrlSyslogActionMsgFormat.setStatus("current")
_EtsysCosFloodCtrlResourceTable_Object = MibTable
etsysCosFloodCtrlResourceTable = _EtsysCosFloodCtrlResourceTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 7, 9)
)
if mibBuilder.loadTexts:
    etsysCosFloodCtrlResourceTable.setStatus("current")
_EtsysCosFloodCtrlResourceEntry_Object = MibTableRow
etsysCosFloodCtrlResourceEntry = _EtsysCosFloodCtrlResourceEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 7, 9, 1)
)
etsysCosFloodCtrlResourceEntry.setIndexNames(
    (0, "ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosFloodCtrlPortGroupIndex"),
    (0, "ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosFloodCtrlPortTypeIndex"),
    (0, "ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosFloodCtrlFloodType"),
)
if mibBuilder.loadTexts:
    etsysCosFloodCtrlResourceEntry.setStatus("current")


class _EtsysCosFloodCtrlFloodType_Type(Integer32):
    """Custom type etsysCosFloodCtrlFloodType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("broadcast", 3),
          ("multicast", 2),
          ("unicastUnknown", 1))
    )


_EtsysCosFloodCtrlFloodType_Type.__name__ = "Integer32"
_EtsysCosFloodCtrlFloodType_Object = MibTableColumn
etsysCosFloodCtrlFloodType = _EtsysCosFloodCtrlFloodType_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 7, 9, 1, 1),
    _EtsysCosFloodCtrlFloodType_Type()
)
etsysCosFloodCtrlFloodType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    etsysCosFloodCtrlFloodType.setStatus("current")


class _EtsysCosFloodCtrlResourceUnits_Type(EtsysCosRateTypes):
    """Custom type etsysCosFloodCtrlResourceUnits based on EtsysCosRateTypes"""
    defaultBinValue = "01"


_EtsysCosFloodCtrlResourceUnits_Object = MibTableColumn
etsysCosFloodCtrlResourceUnits = _EtsysCosFloodCtrlResourceUnits_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 7, 9, 1, 2),
    _EtsysCosFloodCtrlResourceUnits_Type()
)
etsysCosFloodCtrlResourceUnits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysCosFloodCtrlResourceUnits.setStatus("current")


class _EtsysCosFloodCtrlResourceRate_Type(Integer32):
    """Custom type etsysCosFloodCtrlResourceRate based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 2147483647),
    )


_EtsysCosFloodCtrlResourceRate_Type.__name__ = "Integer32"
_EtsysCosFloodCtrlResourceRate_Object = MibTableColumn
etsysCosFloodCtrlResourceRate = _EtsysCosFloodCtrlResourceRate_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 7, 9, 1, 3),
    _EtsysCosFloodCtrlResourceRate_Type()
)
etsysCosFloodCtrlResourceRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysCosFloodCtrlResourceRate.setStatus("current")


class _EtsysCosFloodCtrlResourceAction_Type(Bits):
    """Custom type etsysCosFloodCtrlResourceAction based on Bits"""
    defaultBinValue = "1"

    namedValues = NamedValues(
        *(("disable", 3),
          ("drop", 0),
          ("syslog", 1),
          ("trap", 2))
    )

_EtsysCosFloodCtrlResourceAction_Type.__name__ = "Bits"
_EtsysCosFloodCtrlResourceAction_Object = MibTableColumn
etsysCosFloodCtrlResourceAction = _EtsysCosFloodCtrlResourceAction_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 7, 9, 1, 4),
    _EtsysCosFloodCtrlResourceAction_Type()
)
etsysCosFloodCtrlResourceAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysCosFloodCtrlResourceAction.setStatus("current")
_EtsysCosFloodCtrlResourceViolationPortList_Type = PortList
_EtsysCosFloodCtrlResourceViolationPortList_Object = MibTableColumn
etsysCosFloodCtrlResourceViolationPortList = _EtsysCosFloodCtrlResourceViolationPortList_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 7, 9, 1, 5),
    _EtsysCosFloodCtrlResourceViolationPortList_Type()
)
etsysCosFloodCtrlResourceViolationPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysCosFloodCtrlResourceViolationPortList.setStatus("current")
_EtsysCosFloodCtrlResourceClearCounters_Type = TruthValue
_EtsysCosFloodCtrlResourceClearCounters_Object = MibTableColumn
etsysCosFloodCtrlResourceClearCounters = _EtsysCosFloodCtrlResourceClearCounters_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 7, 9, 1, 6),
    _EtsysCosFloodCtrlResourceClearCounters_Type()
)
etsysCosFloodCtrlResourceClearCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysCosFloodCtrlResourceClearCounters.setStatus("current")
_EtsysCosFloodCtrlViolationClearTable_Type = TruthValue
_EtsysCosFloodCtrlViolationClearTable_Object = MibScalar
etsysCosFloodCtrlViolationClearTable = _EtsysCosFloodCtrlViolationClearTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 7, 10),
    _EtsysCosFloodCtrlViolationClearTable_Type()
)
etsysCosFloodCtrlViolationClearTable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysCosFloodCtrlViolationClearTable.setStatus("current")
_EtsysCosFloodCtrlViolationLastChange_Type = TimeStamp
_EtsysCosFloodCtrlViolationLastChange_Object = MibScalar
etsysCosFloodCtrlViolationLastChange = _EtsysCosFloodCtrlViolationLastChange_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 7, 11),
    _EtsysCosFloodCtrlViolationLastChange_Type()
)
etsysCosFloodCtrlViolationLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysCosFloodCtrlViolationLastChange.setStatus("current")
_EtsysCosFloodCtrlDisabledPortsList_Type = PortList
_EtsysCosFloodCtrlDisabledPortsList_Object = MibScalar
etsysCosFloodCtrlDisabledPortsList = _EtsysCosFloodCtrlDisabledPortsList_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 7, 12),
    _EtsysCosFloodCtrlDisabledPortsList_Type()
)
etsysCosFloodCtrlDisabledPortsList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysCosFloodCtrlDisabledPortsList.setStatus("current")
_EtsysCosFloodCtrlViolationTable_Object = MibTable
etsysCosFloodCtrlViolationTable = _EtsysCosFloodCtrlViolationTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 7, 13)
)
if mibBuilder.loadTexts:
    etsysCosFloodCtrlViolationTable.setStatus("current")
_EtsysCosFloodCtrlViolationEntry_Object = MibTableRow
etsysCosFloodCtrlViolationEntry = _EtsysCosFloodCtrlViolationEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 7, 13, 1)
)
etsysCosFloodCtrlViolationEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
    (0, "ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosFloodCtrlFloodType"),
)
if mibBuilder.loadTexts:
    etsysCosFloodCtrlViolationEntry.setStatus("current")
_EtsysCosFloodCtrlViolation_Type = TruthValue
_EtsysCosFloodCtrlViolation_Object = MibTableColumn
etsysCosFloodCtrlViolation = _EtsysCosFloodCtrlViolation_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 7, 13, 1, 1),
    _EtsysCosFloodCtrlViolation_Type()
)
etsysCosFloodCtrlViolation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysCosFloodCtrlViolation.setStatus("current")
_EtsysCosFloodCtrlCounter_Type = Counter64
_EtsysCosFloodCtrlCounter_Object = MibTableColumn
etsysCosFloodCtrlCounter = _EtsysCosFloodCtrlCounter_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 7, 13, 1, 2),
    _EtsysCosFloodCtrlCounter_Type()
)
etsysCosFloodCtrlCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysCosFloodCtrlCounter.setStatus("current")
_EtsysCosFloodCtrlResetFlags_Type = EtsysRateLimitResetBits
_EtsysCosFloodCtrlResetFlags_Object = MibTableColumn
etsysCosFloodCtrlResetFlags = _EtsysCosFloodCtrlResetFlags_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 7, 13, 1, 3),
    _EtsysCosFloodCtrlResetFlags_Type()
)
etsysCosFloodCtrlResetFlags.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysCosFloodCtrlResetFlags.setStatus("current")
_EtsysCosConformance_ObjectIdentity = ObjectIdentity
etsysCosConformance = _EtsysCosConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 2)
)
_EtsysCosGroups_ObjectIdentity = ObjectIdentity
etsysCosGroups = _EtsysCosGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 2, 1)
)
_EtsysCosCompliances_ObjectIdentity = ObjectIdentity
etsysCosCompliances = _EtsysCosCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 2, 2)
)

# Managed Objects groups

etsysCosMasterResetGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 2, 1, 1)
)
etsysCosMasterResetGroup.setObjects(
    ("ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosMibObjectAnullingBehavior")
)
if mibBuilder.loadTexts:
    etsysCosMasterResetGroup.setStatus("current")

etsysCosCapabilitiesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 2, 1, 2)
)
etsysCosCapabilitiesGroup.setObjects(
    ("ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosCapability")
)
if mibBuilder.loadTexts:
    etsysCosCapabilitiesGroup.setStatus("current")

etsysCosGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 2, 1, 3)
)
etsysCosGroup.setObjects(
      *(("ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosMaxEntries"),
        ("ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosNumEntries"),
        ("ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosLastChange"),
        ("ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosEnableState"),
        ("ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosRowStatus"),
        ("ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCos8021dPriority"),
        ("ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosTosValue"),
        ("ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosTxqReference"),
        ("ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosIrlReference"),
        ("ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosOrlReference"),
        ("ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosDropPrecedence"))
)
if mibBuilder.loadTexts:
    etsysCosGroup.setStatus("current")

etsysCosTxqGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 2, 1, 4)
)
etsysCosTxqGroup.setObjects(
      *(("ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosTxqReference"),
        ("ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosTxqNumPortTypes"),
        ("ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosTxqPortTypeDescr"),
        ("ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosTxqPortTypeEligiblePorts"),
        ("ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosTxqPortTypeUnselectedPorts"),
        ("ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosTxqPortTypeNumberOfQueues"),
        ("ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosTxqPortTypeSupportedRateTypes"),
        ("ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosTxqPortTypeNumberOfSlices"),
        ("ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosTxqPortTypeQueueAlgorithms"),
        ("ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosTxqPortTypeQueueArbiterModes"),
        ("ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosTxqPortTypeMaxDropPrecedence"),
        ("ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosTxqPortTypeLLQEligibleQueues"),
        ("ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosTxqUnitMaxRate"),
        ("ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosTxqUnitMinRate"),
        ("ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosTxqUnitGranularity"),
        ("ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosTxqMaxPortGroups"),
        ("ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosTxqNumPortGroups"),
        ("ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosTxqPortGroupLastChange"),
        ("ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosTxqPortGroupRowStatus"),
        ("ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosTxqPortGroupList"),
        ("ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosTxqPortGroupName"),
        ("ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosTxqPortArbMode"),
        ("ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosTxqPortSliceSetting"),
        ("ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosTxqPortQUnit"),
        ("ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosTxqPortQRate"),
        ("ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosTxqPortQAlgorithm"),
        ("ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosTxqPortQLLQenable"),
        ("ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosTxqReferenceMappingMaxReference"),
        ("ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosTxqResourceQueueNumber"),
        ("ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosTxqDropProfilesMaxEntries"),
        ("ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosTxqDropProfilesNumEntries"),
        ("ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosTxqDropProfilesLastChange"),
        ("ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosTxqDropProfilesRowStatus"),
        ("ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosTxqDropProfilesMin"),
        ("ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosTxqDropProfilesMax"),
        ("ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosTxqDropProfilesMaxDropProb"),
        ("ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosTxqDropProfilesQueueDepthAtMaxProb"),
        ("ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosTxqDropProfileQueueCfgID"))
)
if mibBuilder.loadTexts:
    etsysCosTxqGroup.setStatus("current")

etsysCosIrlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 2, 1, 5)
)
etsysCosIrlGroup.setObjects(
      *(("ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosIrlReference"),
        ("ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosIrlPortTypeMaxEntries"),
        ("ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosIrlPortTypeDescr"),
        ("ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosIrlPortTypeEligiblePorts"),
        ("ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosIrlPortTypeUnselectedPorts"),
        ("ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosIrlPortTypeNumberOfIRLs"),
        ("ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosIrlPortTypeCapabilities"),
        ("ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosIrlPortTypeSupportedRateTypes"),
        ("ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosIrlUnitMaxRate"),
        ("ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosIrlUnitMinRate"),
        ("ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosIrlUnitGranularity"),
        ("ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosIrlPortGroupMaxEntries"),
        ("ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosIrlPortGroupNumEntries"),
        ("ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosIrlPortGroupLastChange"),
        ("ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosIrlPortGroupRowStatus"),
        ("ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosIrlPortGroupList"),
        ("ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosIrlPortGroupName"),
        ("ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosIrlPortCfgFloodLimiter"),
        ("ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosIrlResourceIrlNumber"),
        ("ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosIrlResourceUnits"),
        ("ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosIrlResourceRate"),
        ("ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosIrlResourceParentIrl"),
        ("ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosIrlResourceActionCosIndex"),
        ("ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosIrlResourceType"),
        ("ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosIrlResourceAction"),
        ("ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosIrlResourceViolationPortList"),
        ("ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosIrlResourceClearCounters"),
        ("ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosIrlReferenceMappingMaxReference"),
        ("ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosIrlReferenceMappingLastChange"),
        ("ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosIrlViolationLastChange"),
        ("ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosIrlDisabledPortsList"),
        ("ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosIrlViolation"),
        ("ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosIrlViolationClearTable"),
        ("ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosIrlCounter"),
        ("ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosIrlResetFlags"))
)
if mibBuilder.loadTexts:
    etsysCosIrlGroup.setStatus("current")

etsysCosOrlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 2, 1, 6)
)
etsysCosOrlGroup.setObjects(
      *(("ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosOrlReference"),
        ("ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosOrlPortTypeMaxEntries"),
        ("ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosOrlPortTypeDescr"),
        ("ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosOrlPortTypeEligiblePorts"),
        ("ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosOrlPortTypeUnselectedPorts"),
        ("ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosOrlPortTypeNumberOfORLs"),
        ("ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosOrlPortTypeCapabilities"),
        ("ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosOrlPortTypeSupportedRateTypes"),
        ("ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosOrlUnitMaxRate"),
        ("ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosOrlUnitMinRate"),
        ("ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosOrlUnitGranularity"),
        ("ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosOrlPortGroupMaxEntries"),
        ("ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosOrlPortGroupNumEntries"),
        ("ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosOrlPortGroupLastChange"),
        ("ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosOrlPortGroupRowStatus"),
        ("ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosOrlPortGroupList"),
        ("ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosOrlPortGroupName"),
        ("ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosOrlPortCfgFloodLimiter"),
        ("ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosOrlResourceOrlNumber"),
        ("ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosOrlResourceUnits"),
        ("ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosOrlResourceRate"),
        ("ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosOrlResourceParentOrl"),
        ("ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosOrlResourceActionCosIndex"),
        ("ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosOrlResourceType"),
        ("ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosOrlResourceAction"),
        ("ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosOrlResourceViolationPortList"),
        ("ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosOrlResourceClearCounters"),
        ("ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosOrlReferenceMappingMaxReference"),
        ("ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosOrlReferenceMappingLastChange"),
        ("ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosOrlViolationLastChange"),
        ("ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosOrlDisabledPortsList"),
        ("ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosOrlViolation"),
        ("ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosOrlViolationClearTable"),
        ("ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosOrlCounter"),
        ("ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosOrlResetFlags"))
)
if mibBuilder.loadTexts:
    etsysCosOrlGroup.setStatus("current")


# Notification objects

etsysCosIrlExceededNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 0, 1)
)
etsysCosIrlExceededNotification.setObjects(
      *(("IF-MIB", "ifName"),
        ("ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosIrlViolation"))
)
if mibBuilder.loadTexts:
    etsysCosIrlExceededNotification.setStatus(
        "current"
    )

etsysCosOrlExceededNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 0, 2)
)
etsysCosOrlExceededNotification.setObjects(
      *(("IF-MIB", "ifName"),
        ("ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosOrlViolation"))
)
if mibBuilder.loadTexts:
    etsysCosOrlExceededNotification.setStatus(
        "current"
    )

etsysCosFloodLimitExceededNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 1, 0, 3)
)
etsysCosFloodLimitExceededNotification.setObjects(
      *(("IF-MIB", "ifName"),
        ("ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosFloodCtrlViolation"))
)
if mibBuilder.loadTexts:
    etsysCosFloodLimitExceededNotification.setStatus(
        "current"
    )


# Notifications groups

etsysCosNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 2, 1, 7)
)
etsysCosNotificationGroup.setObjects(
      *(("ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosIrlExceededNotification"),
        ("ENTERASYS-CLASS-OF-SERVICE-MIB", "etsysCosOrlExceededNotification"))
)
if mibBuilder.loadTexts:
    etsysCosNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

etsysCosCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 55, 2, 2, 1)
)
if mibBuilder.loadTexts:
    etsysCosCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ENTERASYS-CLASS-OF-SERVICE-MIB",
    **{"TxqArbiterModes": TxqArbiterModes,
       "TxqAlgorithms": TxqAlgorithms,
       "TxQueueList": TxQueueList,
       "EtsysCosRateTypes": EtsysCosRateTypes,
       "EtsysCosRlCapabilities": EtsysCosRlCapabilities,
       "EtsysViolationAction": EtsysViolationAction,
       "EtsysRateLimitingType": EtsysRateLimitingType,
       "EtsysRateLimitResetBits": EtsysRateLimitResetBits,
       "etsysCosMIB": etsysCosMIB,
       "etsysCosObjects": etsysCosObjects,
       "etsysCosNotifications": etsysCosNotifications,
       "etsysCosIrlExceededNotification": etsysCosIrlExceededNotification,
       "etsysCosOrlExceededNotification": etsysCosOrlExceededNotification,
       "etsysCosFloodLimitExceededNotification": etsysCosFloodLimitExceededNotification,
       "etsysCosMasterReset": etsysCosMasterReset,
       "etsysCosMibObjectAnullingBehavior": etsysCosMibObjectAnullingBehavior,
       "etsysCosCapabilities": etsysCosCapabilities,
       "etsysCosCapability": etsysCosCapability,
       "etsysCos": etsysCos,
       "etsysCosMaxEntries": etsysCosMaxEntries,
       "etsysCosNumEntries": etsysCosNumEntries,
       "etsysCosLastChange": etsysCosLastChange,
       "etsysCosEnableState": etsysCosEnableState,
       "etsysCosTable": etsysCosTable,
       "etsysCosEntry": etsysCosEntry,
       "etsysCosIndex": etsysCosIndex,
       "etsysCosRowStatus": etsysCosRowStatus,
       "etsysCos8021dPriority": etsysCos8021dPriority,
       "etsysCosTosValue": etsysCosTosValue,
       "etsysCosTxqReference": etsysCosTxqReference,
       "etsysCosIrlReference": etsysCosIrlReference,
       "etsysCosOrlReference": etsysCosOrlReference,
       "etsysCosDropPrecedence": etsysCosDropPrecedence,
       "etsysCosFloodControlStatus": etsysCosFloodControlStatus,
       "etsysCosTxq": etsysCosTxq,
       "etsysCosTxqNumPortTypes": etsysCosTxqNumPortTypes,
       "etsysCosTxqPortTypeTable": etsysCosTxqPortTypeTable,
       "etsysCosTxqPortTypeEntry": etsysCosTxqPortTypeEntry,
       "etsysCosTxqPortTypeIndex": etsysCosTxqPortTypeIndex,
       "etsysCosTxqPortTypeDescr": etsysCosTxqPortTypeDescr,
       "etsysCosTxqPortTypeEligiblePorts": etsysCosTxqPortTypeEligiblePorts,
       "etsysCosTxqPortTypeUnselectedPorts": etsysCosTxqPortTypeUnselectedPorts,
       "etsysCosTxqPortTypeNumberOfQueues": etsysCosTxqPortTypeNumberOfQueues,
       "etsysCosTxqPortTypeSupportedRateTypes": etsysCosTxqPortTypeSupportedRateTypes,
       "etsysCosTxqPortTypeNumberOfSlices": etsysCosTxqPortTypeNumberOfSlices,
       "etsysCosTxqPortTypeQueueAlgorithms": etsysCosTxqPortTypeQueueAlgorithms,
       "etsysCosTxqPortTypeQueueArbiterModes": etsysCosTxqPortTypeQueueArbiterModes,
       "etsysCosTxqPortTypeMaxDropPrecedence": etsysCosTxqPortTypeMaxDropPrecedence,
       "etsysCosTxqPortTypeLLQEligibleQueues": etsysCosTxqPortTypeLLQEligibleQueues,
       "etsysCosTxqUnitTable": etsysCosTxqUnitTable,
       "etsysCosTxqUnitEntry": etsysCosTxqUnitEntry,
       "etsysCosTxqUnitTypeIndex": etsysCosTxqUnitTypeIndex,
       "etsysCosTxqUnitMaxRate": etsysCosTxqUnitMaxRate,
       "etsysCosTxqUnitMinRate": etsysCosTxqUnitMinRate,
       "etsysCosTxqUnitGranularity": etsysCosTxqUnitGranularity,
       "etsysCosTxqMaxPortGroups": etsysCosTxqMaxPortGroups,
       "etsysCosTxqNumPortGroups": etsysCosTxqNumPortGroups,
       "etsysCosTxqPortGroupLastChange": etsysCosTxqPortGroupLastChange,
       "etsysCosTxqPortGroupTable": etsysCosTxqPortGroupTable,
       "etsysCosTxqPortGroupEntry": etsysCosTxqPortGroupEntry,
       "etsysCosTxqPortGroupIndex": etsysCosTxqPortGroupIndex,
       "etsysCosTxqPortGroupRowStatus": etsysCosTxqPortGroupRowStatus,
       "etsysCosTxqPortGroupList": etsysCosTxqPortGroupList,
       "etsysCosTxqPortGroupName": etsysCosTxqPortGroupName,
       "etsysCosTxqPortCfgTable": etsysCosTxqPortCfgTable,
       "etsysCosTxqPortCfgEntry": etsysCosTxqPortCfgEntry,
       "etsysCosTxqPortArbMode": etsysCosTxqPortArbMode,
       "etsysCosTxqPortSliceSetting": etsysCosTxqPortSliceSetting,
       "etsysCosTxqResourceTable": etsysCosTxqResourceTable,
       "etsysCosTxqResourceEntry": etsysCosTxqResourceEntry,
       "etsysCosTxqResourceQueueNum": etsysCosTxqResourceQueueNum,
       "etsysCosTxqPortQUnit": etsysCosTxqPortQUnit,
       "etsysCosTxqPortQRate": etsysCosTxqPortQRate,
       "etsysCosTxqPortQAlgorithm": etsysCosTxqPortQAlgorithm,
       "etsysCosTxqPortQLLQenable": etsysCosTxqPortQLLQenable,
       "etsysCosTxqReferenceMappingMaxReference": etsysCosTxqReferenceMappingMaxReference,
       "etsysCosTxqReferenceMappingTable": etsysCosTxqReferenceMappingTable,
       "etsysCosTxqReferenceMappingEntry": etsysCosTxqReferenceMappingEntry,
       "etsysCosTxqResourceQueueNumber": etsysCosTxqResourceQueueNumber,
       "etsysCosTxqDropProfilesMaxEntries": etsysCosTxqDropProfilesMaxEntries,
       "etsysCosTxqDropProfilesNumEntries": etsysCosTxqDropProfilesNumEntries,
       "etsysCosTxqDropProfilesLastChange": etsysCosTxqDropProfilesLastChange,
       "etsysCosTxqDropProfilesTable": etsysCosTxqDropProfilesTable,
       "etsysCosTxqDropProfilesEntry": etsysCosTxqDropProfilesEntry,
       "etsysCosTxqDropSettingIndex": etsysCosTxqDropSettingIndex,
       "etsysCosTxqDropProfilesRowStatus": etsysCosTxqDropProfilesRowStatus,
       "etsysCosTxqDropProfilesMin": etsysCosTxqDropProfilesMin,
       "etsysCosTxqDropProfilesMax": etsysCosTxqDropProfilesMax,
       "etsysCosTxqDropProfilesMaxDropProb": etsysCosTxqDropProfilesMaxDropProb,
       "etsysCosTxqDropProfilesQueueDepthAtMaxProb": etsysCosTxqDropProfilesQueueDepthAtMaxProb,
       "etsysCosTxqDropPrecedenceTable": etsysCosTxqDropPrecedenceTable,
       "etsysCosTxqDropPrecedenceEntry": etsysCosTxqDropPrecedenceEntry,
       "etsysCosTableDropPrecedence": etsysCosTableDropPrecedence,
       "etsysCosTxqDropProfileQueueCfgID": etsysCosTxqDropProfileQueueCfgID,
       "etsysCosIrl": etsysCosIrl,
       "etsysCosIrlPortTypeMaxEntries": etsysCosIrlPortTypeMaxEntries,
       "etsysCosIrlPortTypeTable": etsysCosIrlPortTypeTable,
       "etsysCosIrlPortTypeEntry": etsysCosIrlPortTypeEntry,
       "etsysCosIrlPortTypeIndex": etsysCosIrlPortTypeIndex,
       "etsysCosIrlPortTypeDescr": etsysCosIrlPortTypeDescr,
       "etsysCosIrlPortTypeEligiblePorts": etsysCosIrlPortTypeEligiblePorts,
       "etsysCosIrlPortTypeUnselectedPorts": etsysCosIrlPortTypeUnselectedPorts,
       "etsysCosIrlPortTypeNumberOfIRLs": etsysCosIrlPortTypeNumberOfIRLs,
       "etsysCosIrlPortTypeSupportedRateTypes": etsysCosIrlPortTypeSupportedRateTypes,
       "etsysCosIrlPortTypeCapabilities": etsysCosIrlPortTypeCapabilities,
       "etsysCosIrlUnitTable": etsysCosIrlUnitTable,
       "etsysCosIrlUnitEntry": etsysCosIrlUnitEntry,
       "etsysCosIrlUnitTypeIndex": etsysCosIrlUnitTypeIndex,
       "etsysCosIrlUnitMaxRate": etsysCosIrlUnitMaxRate,
       "etsysCosIrlUnitMinRate": etsysCosIrlUnitMinRate,
       "etsysCosIrlUnitGranularity": etsysCosIrlUnitGranularity,
       "etsysCosIrlPortGroupMaxEntries": etsysCosIrlPortGroupMaxEntries,
       "etsysCosIrlPortGroupNumEntries": etsysCosIrlPortGroupNumEntries,
       "etsysCosIrlPortGroupLastChange": etsysCosIrlPortGroupLastChange,
       "etsysCosIrlPortGroupTable": etsysCosIrlPortGroupTable,
       "etsysCosIrlPortGroupEntry": etsysCosIrlPortGroupEntry,
       "etsysCosIrlPortGroupIndex": etsysCosIrlPortGroupIndex,
       "etsysCosIrlPortGroupRowStatus": etsysCosIrlPortGroupRowStatus,
       "etsysCosIrlPortGroupList": etsysCosIrlPortGroupList,
       "etsysCosIrlPortGroupName": etsysCosIrlPortGroupName,
       "etsysCosIrlPortCfgTable": etsysCosIrlPortCfgTable,
       "etsysCosIrlPortCfgEntry": etsysCosIrlPortCfgEntry,
       "etsysCosIrlPortCfgFloodLimiter": etsysCosIrlPortCfgFloodLimiter,
       "etsysCosIrlResourceTable": etsysCosIrlResourceTable,
       "etsysCosIrlResourceEntry": etsysCosIrlResourceEntry,
       "etsysCosIrlResourceIrlNum": etsysCosIrlResourceIrlNum,
       "etsysCosIrlResourceUnits": etsysCosIrlResourceUnits,
       "etsysCosIrlResourceRate": etsysCosIrlResourceRate,
       "etsysCosIrlResourceParentIrl": etsysCosIrlResourceParentIrl,
       "etsysCosIrlResourceType": etsysCosIrlResourceType,
       "etsysCosIrlResourceActionCosIndex": etsysCosIrlResourceActionCosIndex,
       "etsysCosIrlResourceAction": etsysCosIrlResourceAction,
       "etsysCosIrlResourceViolationPortList": etsysCosIrlResourceViolationPortList,
       "etsysCosIrlResourceClearCounters": etsysCosIrlResourceClearCounters,
       "etsysCosIrlReferenceMappingMaxReference": etsysCosIrlReferenceMappingMaxReference,
       "etsysCosIrlReferenceMappingLastChange": etsysCosIrlReferenceMappingLastChange,
       "etsysCosIrlReferenceMappingTable": etsysCosIrlReferenceMappingTable,
       "etsysCosIrlReferenceMappingEntry": etsysCosIrlReferenceMappingEntry,
       "etsysCosIrlResourceIrlNumber": etsysCosIrlResourceIrlNumber,
       "etsysCosIrlViolationClearTable": etsysCosIrlViolationClearTable,
       "etsysCosIrlViolationLastChange": etsysCosIrlViolationLastChange,
       "etsysCosIrlDisabledPortsList": etsysCosIrlDisabledPortsList,
       "etsysCosIrlViolationTable": etsysCosIrlViolationTable,
       "etsysCosIrlViolationEntry": etsysCosIrlViolationEntry,
       "etsysCosIrlPortIndex": etsysCosIrlPortIndex,
       "etsysCosIrlViolation": etsysCosIrlViolation,
       "etsysCosIrlCounter": etsysCosIrlCounter,
       "etsysCosIrlResetFlags": etsysCosIrlResetFlags,
       "etsysCosOrl": etsysCosOrl,
       "etsysCosOrlPortTypeMaxEntries": etsysCosOrlPortTypeMaxEntries,
       "etsysCosOrlPortTypeTable": etsysCosOrlPortTypeTable,
       "etsysCosOrlPortTypeEntry": etsysCosOrlPortTypeEntry,
       "etsysCosOrlPortTypeIndex": etsysCosOrlPortTypeIndex,
       "etsysCosOrlPortTypeDescr": etsysCosOrlPortTypeDescr,
       "etsysCosOrlPortTypeEligiblePorts": etsysCosOrlPortTypeEligiblePorts,
       "etsysCosOrlPortTypeUnselectedPorts": etsysCosOrlPortTypeUnselectedPorts,
       "etsysCosOrlPortTypeNumberOfORLs": etsysCosOrlPortTypeNumberOfORLs,
       "etsysCosOrlPortTypeSupportedRateTypes": etsysCosOrlPortTypeSupportedRateTypes,
       "etsysCosOrlPortTypeCapabilities": etsysCosOrlPortTypeCapabilities,
       "etsysCosOrlUnitTable": etsysCosOrlUnitTable,
       "etsysCosOrlUnitEntry": etsysCosOrlUnitEntry,
       "etsysCosOrlUnitTypeIndex": etsysCosOrlUnitTypeIndex,
       "etsysCosOrlUnitMaxRate": etsysCosOrlUnitMaxRate,
       "etsysCosOrlUnitMinRate": etsysCosOrlUnitMinRate,
       "etsysCosOrlUnitGranularity": etsysCosOrlUnitGranularity,
       "etsysCosOrlPortGroupMaxEntries": etsysCosOrlPortGroupMaxEntries,
       "etsysCosOrlPortGroupNumEntries": etsysCosOrlPortGroupNumEntries,
       "etsysCosOrlPortGroupLastChange": etsysCosOrlPortGroupLastChange,
       "etsysCosOrlPortGroupTable": etsysCosOrlPortGroupTable,
       "etsysCosOrlPortGroupEntry": etsysCosOrlPortGroupEntry,
       "etsysCosOrlPortGroupIndex": etsysCosOrlPortGroupIndex,
       "etsysCosOrlPortGroupRowStatus": etsysCosOrlPortGroupRowStatus,
       "etsysCosOrlPortGroupList": etsysCosOrlPortGroupList,
       "etsysCosOrlPortGroupName": etsysCosOrlPortGroupName,
       "etsysCosOrlPortCfgTable": etsysCosOrlPortCfgTable,
       "etsysCosOrlPortCfgEntry": etsysCosOrlPortCfgEntry,
       "etsysCosOrlPortCfgFloodLimiter": etsysCosOrlPortCfgFloodLimiter,
       "etsysCosOrlResourceTable": etsysCosOrlResourceTable,
       "etsysCosOrlResourceEntry": etsysCosOrlResourceEntry,
       "etsysCosOrlResourceOrlNum": etsysCosOrlResourceOrlNum,
       "etsysCosOrlResourceUnits": etsysCosOrlResourceUnits,
       "etsysCosOrlResourceRate": etsysCosOrlResourceRate,
       "etsysCosOrlResourceParentOrl": etsysCosOrlResourceParentOrl,
       "etsysCosOrlResourceType": etsysCosOrlResourceType,
       "etsysCosOrlResourceActionCosIndex": etsysCosOrlResourceActionCosIndex,
       "etsysCosOrlResourceAction": etsysCosOrlResourceAction,
       "etsysCosOrlResourceViolationPortList": etsysCosOrlResourceViolationPortList,
       "etsysCosOrlResourceClearCounters": etsysCosOrlResourceClearCounters,
       "etsysCosOrlReferenceMappingMaxReference": etsysCosOrlReferenceMappingMaxReference,
       "etsysCosOrlReferenceMappingLastChange": etsysCosOrlReferenceMappingLastChange,
       "etsysCosOrlReferenceMappingTable": etsysCosOrlReferenceMappingTable,
       "etsysCosOrlReferenceMappingEntry": etsysCosOrlReferenceMappingEntry,
       "etsysCosOrlResourceOrlNumber": etsysCosOrlResourceOrlNumber,
       "etsysCosOrlViolationClearTable": etsysCosOrlViolationClearTable,
       "etsysCosOrlViolationLastChange": etsysCosOrlViolationLastChange,
       "etsysCosOrlDisabledPortsList": etsysCosOrlDisabledPortsList,
       "etsysCosOrlViolationTable": etsysCosOrlViolationTable,
       "etsysCosOrlViolationEntry": etsysCosOrlViolationEntry,
       "etsysCosOrlPortIndex": etsysCosOrlPortIndex,
       "etsysCosOrlViolation": etsysCosOrlViolation,
       "etsysCosOrlCounter": etsysCosOrlCounter,
       "etsysCosOrlResetFlags": etsysCosOrlResetFlags,
       "etsysCosFloodControl": etsysCosFloodControl,
       "etsysCosFloodCtrlPortTypeMaxEntries": etsysCosFloodCtrlPortTypeMaxEntries,
       "etsysCosFloodCtrlPortTypeTable": etsysCosFloodCtrlPortTypeTable,
       "etsysCosFloodCtrlPortTypeEntry": etsysCosFloodCtrlPortTypeEntry,
       "etsysCosFloodCtrlPortTypeIndex": etsysCosFloodCtrlPortTypeIndex,
       "etsysCosFloodCtrlPortTypeDescr": etsysCosFloodCtrlPortTypeDescr,
       "etsysCosFloodCtrlPortTypeEligiblePorts": etsysCosFloodCtrlPortTypeEligiblePorts,
       "etsysCosFloodCtrlPortTypeUnselectedPorts": etsysCosFloodCtrlPortTypeUnselectedPorts,
       "etsysCosFloodCtrlPortTypeSupportedRateTypes": etsysCosFloodCtrlPortTypeSupportedRateTypes,
       "etsysCosFloodCtrlPortTypeCapabilities": etsysCosFloodCtrlPortTypeCapabilities,
       "etsysCosFloodCtrlUnitTable": etsysCosFloodCtrlUnitTable,
       "etsysCosFloodCtrlUnitEntry": etsysCosFloodCtrlUnitEntry,
       "etsysCosFloodCtrlUnitTypeIndex": etsysCosFloodCtrlUnitTypeIndex,
       "etsysCosFloodCtrlUnitMaxRate": etsysCosFloodCtrlUnitMaxRate,
       "etsysCosFloodCtrlUnitMinRate": etsysCosFloodCtrlUnitMinRate,
       "etsysCosFloodCtrlUnitGranularity": etsysCosFloodCtrlUnitGranularity,
       "etsysCosFloodCtrlPortGroupMaxEntries": etsysCosFloodCtrlPortGroupMaxEntries,
       "etsysCosFloodCtrlPortGroupNumEntries": etsysCosFloodCtrlPortGroupNumEntries,
       "etsysCosFloodCtrlPortGroupLastChange": etsysCosFloodCtrlPortGroupLastChange,
       "etsysCosFloodCtrlPortGroupTable": etsysCosFloodCtrlPortGroupTable,
       "etsysCosFloodCtrlPortGroupEntry": etsysCosFloodCtrlPortGroupEntry,
       "etsysCosFloodCtrlPortGroupIndex": etsysCosFloodCtrlPortGroupIndex,
       "etsysCosFloodCtrlPortGroupRowStatus": etsysCosFloodCtrlPortGroupRowStatus,
       "etsysCosFloodCtrlPortGroupList": etsysCosFloodCtrlPortGroupList,
       "etsysCosFloodCtrlPortGroupName": etsysCosFloodCtrlPortGroupName,
       "etsysCosFloodCtrlSyslogActionMsgFormat": etsysCosFloodCtrlSyslogActionMsgFormat,
       "etsysCosFloodCtrlResourceTable": etsysCosFloodCtrlResourceTable,
       "etsysCosFloodCtrlResourceEntry": etsysCosFloodCtrlResourceEntry,
       "etsysCosFloodCtrlFloodType": etsysCosFloodCtrlFloodType,
       "etsysCosFloodCtrlResourceUnits": etsysCosFloodCtrlResourceUnits,
       "etsysCosFloodCtrlResourceRate": etsysCosFloodCtrlResourceRate,
       "etsysCosFloodCtrlResourceAction": etsysCosFloodCtrlResourceAction,
       "etsysCosFloodCtrlResourceViolationPortList": etsysCosFloodCtrlResourceViolationPortList,
       "etsysCosFloodCtrlResourceClearCounters": etsysCosFloodCtrlResourceClearCounters,
       "etsysCosFloodCtrlViolationClearTable": etsysCosFloodCtrlViolationClearTable,
       "etsysCosFloodCtrlViolationLastChange": etsysCosFloodCtrlViolationLastChange,
       "etsysCosFloodCtrlDisabledPortsList": etsysCosFloodCtrlDisabledPortsList,
       "etsysCosFloodCtrlViolationTable": etsysCosFloodCtrlViolationTable,
       "etsysCosFloodCtrlViolationEntry": etsysCosFloodCtrlViolationEntry,
       "etsysCosFloodCtrlViolation": etsysCosFloodCtrlViolation,
       "etsysCosFloodCtrlCounter": etsysCosFloodCtrlCounter,
       "etsysCosFloodCtrlResetFlags": etsysCosFloodCtrlResetFlags,
       "etsysCosConformance": etsysCosConformance,
       "etsysCosGroups": etsysCosGroups,
       "etsysCosMasterResetGroup": etsysCosMasterResetGroup,
       "etsysCosCapabilitiesGroup": etsysCosCapabilitiesGroup,
       "etsysCosGroup": etsysCosGroup,
       "etsysCosTxqGroup": etsysCosTxqGroup,
       "etsysCosIrlGroup": etsysCosIrlGroup,
       "etsysCosOrlGroup": etsysCosOrlGroup,
       "etsysCosNotificationGroup": etsysCosNotificationGroup,
       "etsysCosCompliances": etsysCosCompliances,
       "etsysCosCompliance": etsysCosCompliance}
)
