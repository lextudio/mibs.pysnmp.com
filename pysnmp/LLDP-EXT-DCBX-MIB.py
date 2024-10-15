# SNMP MIB module (LLDP-EXT-DCBX-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/LLDP-EXT-DCBX-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:18:59 2024
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

(LldpPortNumber,
 lldpExtensions) = mibBuilder.importSymbols(
    "LLDP-MIB",
    "LldpPortNumber",
    "lldpExtensions")

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

lldpXdcbxMIB = ModuleIdentity(
    (1, 0, 8802, 1, 1, 2, 1, 5, 6945)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class LldpXdcbxPriority(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )



class LldpXdcbxPriorityGroup(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("noBandwidthLimit", 15),
          ("priorityGroupId0", 0),
          ("priorityGroupId1", 1),
          ("priorityGroupId2", 2),
          ("priorityGroupId3", 3),
          ("priorityGroupId4", 4),
          ("priorityGroupId5", 5),
          ("priorityGroupId6", 6),
          ("priorityGroupId7", 7),
          ("reserved10", 10),
          ("reserved11", 11),
          ("reserved12", 12),
          ("reserved13", 13),
          ("reserved14", 14),
          ("reserved8", 8),
          ("reserved9", 9))
    )



class LldpXdcbxFeatureType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("applicationProtocol", 4),
          ("priorityFlowControl", 3),
          ("priorityGroup", 2))
    )



class LldpXdcbxFeatureSubType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class LldpXdcbxVersion(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class LldpXdcbxTC(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )



class LldpXdcbxPgBw(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )



class LldpXdcbxTCPFC(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )



class LldpXdcbxTCPeer(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )



class LldpXdcbxAppProtos(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )



class LldpXdcbxSF(Integer32, TextualConvention):
    status = "current"
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
        *(("l2EtherType", 0),
          ("reserved2", 2),
          ("reserved3", 3),
          ("socketNumber", 1))
    )



# MIB Managed Objects in the order of their OIDs

_LldpXdcbxNotifications_ObjectIdentity = ObjectIdentity
lldpXdcbxNotifications = _LldpXdcbxNotifications_ObjectIdentity(
    (1, 0, 8802, 1, 1, 2, 1, 5, 6945, 0)
)
_LldpXdcbxObjects_ObjectIdentity = ObjectIdentity
lldpXdcbxObjects = _LldpXdcbxObjects_ObjectIdentity(
    (1, 0, 8802, 1, 1, 2, 1, 5, 6945, 1)
)
_LldpXdcbxPortTable_Object = MibTable
lldpXdcbxPortTable = _LldpXdcbxPortTable_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 6945, 1, 1)
)
if mibBuilder.loadTexts:
    lldpXdcbxPortTable.setStatus("current")
_LldpXdcbxPortEntry_Object = MibTableRow
lldpXdcbxPortEntry = _LldpXdcbxPortEntry_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 6945, 1, 1, 1)
)
lldpXdcbxPortEntry.setIndexNames(
    (0, "LLDP-EXT-DCBX-MIB", "lldpXdcbxPortNumber"),
)
if mibBuilder.loadTexts:
    lldpXdcbxPortEntry.setStatus("current")
_LldpXdcbxPortNumber_Type = LldpPortNumber
_LldpXdcbxPortNumber_Object = MibTableColumn
lldpXdcbxPortNumber = _LldpXdcbxPortNumber_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 6945, 1, 1, 1, 1),
    _LldpXdcbxPortNumber_Type()
)
lldpXdcbxPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdcbxPortNumber.setStatus("current")


class _LldpXdcbxPortEnable_Type(TruthValue):
    """Custom type lldpXdcbxPortEnable based on TruthValue"""


_LldpXdcbxPortEnable_Object = MibTableColumn
lldpXdcbxPortEnable = _LldpXdcbxPortEnable_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 6945, 1, 1, 1, 2),
    _LldpXdcbxPortEnable_Type()
)
lldpXdcbxPortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpXdcbxPortEnable.setStatus("current")
_LldpXdcbxPortVersionOper_Type = LldpXdcbxVersion
_LldpXdcbxPortVersionOper_Object = MibTableColumn
lldpXdcbxPortVersionOper = _LldpXdcbxPortVersionOper_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 6945, 1, 1, 1, 3),
    _LldpXdcbxPortVersionOper_Type()
)
lldpXdcbxPortVersionOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdcbxPortVersionOper.setStatus("current")
_LldpXdcbxPortVersionMax_Type = LldpXdcbxVersion
_LldpXdcbxPortVersionMax_Object = MibTableColumn
lldpXdcbxPortVersionMax = _LldpXdcbxPortVersionMax_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 6945, 1, 1, 1, 4),
    _LldpXdcbxPortVersionMax_Type()
)
lldpXdcbxPortVersionMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdcbxPortVersionMax.setStatus("current")
_LldpXdcbxPortSeqNo_Type = Integer32
_LldpXdcbxPortSeqNo_Object = MibTableColumn
lldpXdcbxPortSeqNo = _LldpXdcbxPortSeqNo_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 6945, 1, 1, 1, 5),
    _LldpXdcbxPortSeqNo_Type()
)
lldpXdcbxPortSeqNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdcbxPortSeqNo.setStatus("current")
_LldpXdcbxPortAckNo_Type = Integer32
_LldpXdcbxPortAckNo_Object = MibTableColumn
lldpXdcbxPortAckNo = _LldpXdcbxPortAckNo_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 6945, 1, 1, 1, 6),
    _LldpXdcbxPortAckNo_Type()
)
lldpXdcbxPortAckNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdcbxPortAckNo.setStatus("current")
_LldpXdcbxFeatures_ObjectIdentity = ObjectIdentity
lldpXdcbxFeatures = _LldpXdcbxFeatures_ObjectIdentity(
    (1, 0, 8802, 1, 1, 2, 1, 5, 6945, 2)
)
_LldpXdcbxFeatTable_Object = MibTable
lldpXdcbxFeatTable = _LldpXdcbxFeatTable_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 6945, 2, 1)
)
if mibBuilder.loadTexts:
    lldpXdcbxFeatTable.setStatus("current")
_LldpXdcbxFeatEntry_Object = MibTableRow
lldpXdcbxFeatEntry = _LldpXdcbxFeatEntry_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 6945, 2, 1, 1)
)
lldpXdcbxFeatEntry.setIndexNames(
    (0, "LLDP-EXT-DCBX-MIB", "lldpXdcbxPortNumber"),
    (0, "LLDP-EXT-DCBX-MIB", "lldpXdcbxFeatType"),
    (0, "LLDP-EXT-DCBX-MIB", "lldpXdcbxFeatSubType"),
)
if mibBuilder.loadTexts:
    lldpXdcbxFeatEntry.setStatus("current")
_LldpXdcbxFeatType_Type = LldpXdcbxFeatureType
_LldpXdcbxFeatType_Object = MibTableColumn
lldpXdcbxFeatType = _LldpXdcbxFeatType_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 6945, 2, 1, 1, 1),
    _LldpXdcbxFeatType_Type()
)
lldpXdcbxFeatType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpXdcbxFeatType.setStatus("current")


class _LldpXdcbxFeatSubType_Type(LldpXdcbxFeatureSubType):
    """Custom type lldpXdcbxFeatSubType based on LldpXdcbxFeatureSubType"""
    defaultValue = 0


_LldpXdcbxFeatSubType_Object = MibTableColumn
lldpXdcbxFeatSubType = _LldpXdcbxFeatSubType_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 6945, 2, 1, 1, 2),
    _LldpXdcbxFeatSubType_Type()
)
lldpXdcbxFeatSubType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpXdcbxFeatSubType.setStatus("current")
_LldpXdcbxFeatVersionOper_Type = LldpXdcbxVersion
_LldpXdcbxFeatVersionOper_Object = MibTableColumn
lldpXdcbxFeatVersionOper = _LldpXdcbxFeatVersionOper_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 6945, 2, 1, 1, 3),
    _LldpXdcbxFeatVersionOper_Type()
)
lldpXdcbxFeatVersionOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdcbxFeatVersionOper.setStatus("current")
_LldpXdcbxFeatVersionMax_Type = LldpXdcbxVersion
_LldpXdcbxFeatVersionMax_Object = MibTableColumn
lldpXdcbxFeatVersionMax = _LldpXdcbxFeatVersionMax_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 6945, 2, 1, 1, 4),
    _LldpXdcbxFeatVersionMax_Type()
)
lldpXdcbxFeatVersionMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdcbxFeatVersionMax.setStatus("current")


class _LldpXdcbxFeatEnable_Type(TruthValue):
    """Custom type lldpXdcbxFeatEnable based on TruthValue"""


_LldpXdcbxFeatEnable_Object = MibTableColumn
lldpXdcbxFeatEnable = _LldpXdcbxFeatEnable_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 6945, 2, 1, 1, 5),
    _LldpXdcbxFeatEnable_Type()
)
lldpXdcbxFeatEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpXdcbxFeatEnable.setStatus("current")


class _LldpXdcbxFeatWilling_Type(TruthValue):
    """Custom type lldpXdcbxFeatWilling based on TruthValue"""


_LldpXdcbxFeatWilling_Object = MibTableColumn
lldpXdcbxFeatWilling = _LldpXdcbxFeatWilling_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 6945, 2, 1, 1, 6),
    _LldpXdcbxFeatWilling_Type()
)
lldpXdcbxFeatWilling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpXdcbxFeatWilling.setStatus("current")


class _LldpXdcbxFeatError_Type(TruthValue):
    """Custom type lldpXdcbxFeatError based on TruthValue"""


_LldpXdcbxFeatError_Object = MibTableColumn
lldpXdcbxFeatError = _LldpXdcbxFeatError_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 6945, 2, 1, 1, 7),
    _LldpXdcbxFeatError_Type()
)
lldpXdcbxFeatError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdcbxFeatError.setStatus("current")
_LldpXdcbxFeatAdvertise_Type = TruthValue
_LldpXdcbxFeatAdvertise_Object = MibTableColumn
lldpXdcbxFeatAdvertise = _LldpXdcbxFeatAdvertise_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 6945, 2, 1, 1, 8),
    _LldpXdcbxFeatAdvertise_Type()
)
lldpXdcbxFeatAdvertise.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpXdcbxFeatAdvertise.setStatus("current")
_LldpXdcbxFeatOperMode_Type = TruthValue
_LldpXdcbxFeatOperMode_Object = MibTableColumn
lldpXdcbxFeatOperMode = _LldpXdcbxFeatOperMode_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 6945, 2, 1, 1, 9),
    _LldpXdcbxFeatOperMode_Type()
)
lldpXdcbxFeatOperMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdcbxFeatOperMode.setStatus("current")
_LldpXdcbxFeatSyncd_Type = TruthValue
_LldpXdcbxFeatSyncd_Object = MibTableColumn
lldpXdcbxFeatSyncd = _LldpXdcbxFeatSyncd_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 6945, 2, 1, 1, 10),
    _LldpXdcbxFeatSyncd_Type()
)
lldpXdcbxFeatSyncd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdcbxFeatSyncd.setStatus("current")
_LldpXdcbxFeatSeqNo_Type = Integer32
_LldpXdcbxFeatSeqNo_Object = MibTableColumn
lldpXdcbxFeatSeqNo = _LldpXdcbxFeatSeqNo_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 6945, 2, 1, 1, 11),
    _LldpXdcbxFeatSeqNo_Type()
)
lldpXdcbxFeatSeqNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdcbxFeatSeqNo.setStatus("current")
_LldpXdcbxFeatPeerWilling_Type = TruthValue
_LldpXdcbxFeatPeerWilling_Object = MibTableColumn
lldpXdcbxFeatPeerWilling = _LldpXdcbxFeatPeerWilling_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 6945, 2, 1, 1, 12),
    _LldpXdcbxFeatPeerWilling_Type()
)
lldpXdcbxFeatPeerWilling.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdcbxFeatPeerWilling.setStatus("current")
_LldpXdcbxFeatLocalParameterChange_Type = TruthValue
_LldpXdcbxFeatLocalParameterChange_Object = MibTableColumn
lldpXdcbxFeatLocalParameterChange = _LldpXdcbxFeatLocalParameterChange_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 6945, 2, 1, 1, 13),
    _LldpXdcbxFeatLocalParameterChange_Type()
)
lldpXdcbxFeatLocalParameterChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdcbxFeatLocalParameterChange.setStatus("current")
_LldpXdcbxFeatPeerEnable_Type = TruthValue
_LldpXdcbxFeatPeerEnable_Object = MibTableColumn
lldpXdcbxFeatPeerEnable = _LldpXdcbxFeatPeerEnable_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 6945, 2, 1, 1, 14),
    _LldpXdcbxFeatPeerEnable_Type()
)
lldpXdcbxFeatPeerEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdcbxFeatPeerEnable.setStatus("current")
_LldpXdcbxFeatPeerError_Type = TruthValue
_LldpXdcbxFeatPeerError_Object = MibTableColumn
lldpXdcbxFeatPeerError = _LldpXdcbxFeatPeerError_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 6945, 2, 1, 1, 15),
    _LldpXdcbxFeatPeerError_Type()
)
lldpXdcbxFeatPeerError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdcbxFeatPeerError.setStatus("current")
_LldpXdcbxFeatPeerAdvertise_Type = TruthValue
_LldpXdcbxFeatPeerAdvertise_Object = MibTableColumn
lldpXdcbxFeatPeerAdvertise = _LldpXdcbxFeatPeerAdvertise_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 6945, 2, 1, 1, 16),
    _LldpXdcbxFeatPeerAdvertise_Type()
)
lldpXdcbxFeatPeerAdvertise.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpXdcbxFeatPeerAdvertise.setStatus("current")
_LldpXdcbxFeatPeerTC_Type = LldpXdcbxTCPeer
_LldpXdcbxFeatPeerTC_Object = MibTableColumn
lldpXdcbxFeatPeerTC = _LldpXdcbxFeatPeerTC_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 6945, 2, 1, 1, 17),
    _LldpXdcbxFeatPeerTC_Type()
)
lldpXdcbxFeatPeerTC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdcbxFeatPeerTC.setStatus("current")
_LldpXdcbxFeatPg_ObjectIdentity = ObjectIdentity
lldpXdcbxFeatPg = _LldpXdcbxFeatPg_ObjectIdentity(
    (1, 0, 8802, 1, 1, 2, 1, 5, 6945, 2, 2)
)
_LldpXdcbxFeatPgNumTCsSupported_Type = LldpXdcbxTC
_LldpXdcbxFeatPgNumTCsSupported_Object = MibScalar
lldpXdcbxFeatPgNumTCsSupported = _LldpXdcbxFeatPgNumTCsSupported_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 6945, 2, 2, 1),
    _LldpXdcbxFeatPgNumTCsSupported_Type()
)
lldpXdcbxFeatPgNumTCsSupported.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpXdcbxFeatPgNumTCsSupported.setStatus("current")
_LldpXdcbxFeatPgPrioAllocTable_Object = MibTable
lldpXdcbxFeatPgPrioAllocTable = _LldpXdcbxFeatPgPrioAllocTable_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 6945, 2, 2, 2)
)
if mibBuilder.loadTexts:
    lldpXdcbxFeatPgPrioAllocTable.setStatus("current")
_LldpXdcbxFeatPgPrioAllocEntry_Object = MibTableRow
lldpXdcbxFeatPgPrioAllocEntry = _LldpXdcbxFeatPgPrioAllocEntry_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 6945, 2, 2, 2, 1)
)
lldpXdcbxFeatPgPrioAllocEntry.setIndexNames(
    (0, "LLDP-EXT-DCBX-MIB", "lldpXdcbxPortNumber"),
    (0, "LLDP-EXT-DCBX-MIB", "lldpXdcbxFeatPgPrioAllocPrioId"),
)
if mibBuilder.loadTexts:
    lldpXdcbxFeatPgPrioAllocEntry.setStatus("current")
_LldpXdcbxFeatPgPrioAllocPrioId_Type = LldpXdcbxPriority
_LldpXdcbxFeatPgPrioAllocPrioId_Object = MibTableColumn
lldpXdcbxFeatPgPrioAllocPrioId = _LldpXdcbxFeatPgPrioAllocPrioId_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 6945, 2, 2, 2, 1, 1),
    _LldpXdcbxFeatPgPrioAllocPrioId_Type()
)
lldpXdcbxFeatPgPrioAllocPrioId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpXdcbxFeatPgPrioAllocPrioId.setStatus("current")
_LldpXdcbxFeatPgPrioAllocPgIdDesired_Type = LldpXdcbxPriorityGroup
_LldpXdcbxFeatPgPrioAllocPgIdDesired_Object = MibTableColumn
lldpXdcbxFeatPgPrioAllocPgIdDesired = _LldpXdcbxFeatPgPrioAllocPgIdDesired_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 6945, 2, 2, 2, 1, 2),
    _LldpXdcbxFeatPgPrioAllocPgIdDesired_Type()
)
lldpXdcbxFeatPgPrioAllocPgIdDesired.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpXdcbxFeatPgPrioAllocPgIdDesired.setStatus("current")
_LldpXdcbxFeatPgPrioAllocPgIdOper_Type = LldpXdcbxPriorityGroup
_LldpXdcbxFeatPgPrioAllocPgIdOper_Object = MibTableColumn
lldpXdcbxFeatPgPrioAllocPgIdOper = _LldpXdcbxFeatPgPrioAllocPgIdOper_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 6945, 2, 2, 2, 1, 3),
    _LldpXdcbxFeatPgPrioAllocPgIdOper_Type()
)
lldpXdcbxFeatPgPrioAllocPgIdOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdcbxFeatPgPrioAllocPgIdOper.setStatus("current")
_LldpXdcbxFeatPgPrioAllocPgIdPeer_Type = LldpXdcbxPriorityGroup
_LldpXdcbxFeatPgPrioAllocPgIdPeer_Object = MibTableColumn
lldpXdcbxFeatPgPrioAllocPgIdPeer = _LldpXdcbxFeatPgPrioAllocPgIdPeer_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 6945, 2, 2, 2, 1, 4),
    _LldpXdcbxFeatPgPrioAllocPgIdPeer_Type()
)
lldpXdcbxFeatPgPrioAllocPgIdPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdcbxFeatPgPrioAllocPgIdPeer.setStatus("current")
_LldpXdcbxFeatPgBwAllocTable_Object = MibTable
lldpXdcbxFeatPgBwAllocTable = _LldpXdcbxFeatPgBwAllocTable_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 6945, 2, 2, 3)
)
if mibBuilder.loadTexts:
    lldpXdcbxFeatPgBwAllocTable.setStatus("current")
_LldpXdcbxFeatPgBwAllocEntry_Object = MibTableRow
lldpXdcbxFeatPgBwAllocEntry = _LldpXdcbxFeatPgBwAllocEntry_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 6945, 2, 2, 3, 1)
)
lldpXdcbxFeatPgBwAllocEntry.setIndexNames(
    (0, "LLDP-EXT-DCBX-MIB", "lldpXdcbxPortNumber"),
    (0, "LLDP-EXT-DCBX-MIB", "lldpXdcbxFeatPgBwAllocPgId"),
)
if mibBuilder.loadTexts:
    lldpXdcbxFeatPgBwAllocEntry.setStatus("current")
_LldpXdcbxFeatPgBwAllocPgId_Type = LldpXdcbxPriorityGroup
_LldpXdcbxFeatPgBwAllocPgId_Object = MibTableColumn
lldpXdcbxFeatPgBwAllocPgId = _LldpXdcbxFeatPgBwAllocPgId_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 6945, 2, 2, 3, 1, 1),
    _LldpXdcbxFeatPgBwAllocPgId_Type()
)
lldpXdcbxFeatPgBwAllocPgId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpXdcbxFeatPgBwAllocPgId.setStatus("current")
_LldpXdcbxFeatPgBwAllocBwDesired_Type = LldpXdcbxPgBw
_LldpXdcbxFeatPgBwAllocBwDesired_Object = MibTableColumn
lldpXdcbxFeatPgBwAllocBwDesired = _LldpXdcbxFeatPgBwAllocBwDesired_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 6945, 2, 2, 3, 1, 2),
    _LldpXdcbxFeatPgBwAllocBwDesired_Type()
)
lldpXdcbxFeatPgBwAllocBwDesired.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpXdcbxFeatPgBwAllocBwDesired.setStatus("current")
if mibBuilder.loadTexts:
    lldpXdcbxFeatPgBwAllocBwDesired.setUnits("percent")
_LldpXdcbxFeatPgBwAllocBwOper_Type = LldpXdcbxPgBw
_LldpXdcbxFeatPgBwAllocBwOper_Object = MibTableColumn
lldpXdcbxFeatPgBwAllocBwOper = _LldpXdcbxFeatPgBwAllocBwOper_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 6945, 2, 2, 3, 1, 3),
    _LldpXdcbxFeatPgBwAllocBwOper_Type()
)
lldpXdcbxFeatPgBwAllocBwOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdcbxFeatPgBwAllocBwOper.setStatus("current")
if mibBuilder.loadTexts:
    lldpXdcbxFeatPgBwAllocBwOper.setUnits("percent")
_LldpXdcbxFeatPgBwAllocBwPeer_Type = LldpXdcbxPgBw
_LldpXdcbxFeatPgBwAllocBwPeer_Object = MibTableColumn
lldpXdcbxFeatPgBwAllocBwPeer = _LldpXdcbxFeatPgBwAllocBwPeer_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 6945, 2, 2, 3, 1, 4),
    _LldpXdcbxFeatPgBwAllocBwPeer_Type()
)
lldpXdcbxFeatPgBwAllocBwPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdcbxFeatPgBwAllocBwPeer.setStatus("current")
if mibBuilder.loadTexts:
    lldpXdcbxFeatPgBwAllocBwPeer.setUnits("percent")
_LldpXdcbxFeatPfc_ObjectIdentity = ObjectIdentity
lldpXdcbxFeatPfc = _LldpXdcbxFeatPfc_ObjectIdentity(
    (1, 0, 8802, 1, 1, 2, 1, 5, 6945, 2, 3)
)
_LldpXdcbxFeatPfcNumTCPFCSupported_Type = LldpXdcbxTCPFC
_LldpXdcbxFeatPfcNumTCPFCSupported_Object = MibScalar
lldpXdcbxFeatPfcNumTCPFCSupported = _LldpXdcbxFeatPfcNumTCPFCSupported_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 6945, 2, 3, 1),
    _LldpXdcbxFeatPfcNumTCPFCSupported_Type()
)
lldpXdcbxFeatPfcNumTCPFCSupported.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpXdcbxFeatPfcNumTCPFCSupported.setStatus("current")
_LldpXdcbxFeatPfcTable_Object = MibTable
lldpXdcbxFeatPfcTable = _LldpXdcbxFeatPfcTable_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 6945, 2, 3, 2)
)
if mibBuilder.loadTexts:
    lldpXdcbxFeatPfcTable.setStatus("current")
_LldpXdcbxFeatPfcEntry_Object = MibTableRow
lldpXdcbxFeatPfcEntry = _LldpXdcbxFeatPfcEntry_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 6945, 2, 3, 2, 1)
)
lldpXdcbxFeatPfcEntry.setIndexNames(
    (0, "LLDP-EXT-DCBX-MIB", "lldpXdcbxPortNumber"),
    (0, "LLDP-EXT-DCBX-MIB", "lldpXdcbxFeatPfcPriority"),
)
if mibBuilder.loadTexts:
    lldpXdcbxFeatPfcEntry.setStatus("current")
_LldpXdcbxFeatPfcPriority_Type = LldpXdcbxPriority
_LldpXdcbxFeatPfcPriority_Object = MibTableColumn
lldpXdcbxFeatPfcPriority = _LldpXdcbxFeatPfcPriority_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 6945, 2, 3, 2, 1, 1),
    _LldpXdcbxFeatPfcPriority_Type()
)
lldpXdcbxFeatPfcPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpXdcbxFeatPfcPriority.setStatus("current")
_LldpXdcbxFeatPfcEnableDesired_Type = TruthValue
_LldpXdcbxFeatPfcEnableDesired_Object = MibTableColumn
lldpXdcbxFeatPfcEnableDesired = _LldpXdcbxFeatPfcEnableDesired_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 6945, 2, 3, 2, 1, 2),
    _LldpXdcbxFeatPfcEnableDesired_Type()
)
lldpXdcbxFeatPfcEnableDesired.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpXdcbxFeatPfcEnableDesired.setStatus("current")
_LldpXdcbxFeatPfcEnableOper_Type = TruthValue
_LldpXdcbxFeatPfcEnableOper_Object = MibTableColumn
lldpXdcbxFeatPfcEnableOper = _LldpXdcbxFeatPfcEnableOper_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 6945, 2, 3, 2, 1, 3),
    _LldpXdcbxFeatPfcEnableOper_Type()
)
lldpXdcbxFeatPfcEnableOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdcbxFeatPfcEnableOper.setStatus("current")
_LldpXdcbxFeatPfcEnablePeer_Type = TruthValue
_LldpXdcbxFeatPfcEnablePeer_Object = MibTableColumn
lldpXdcbxFeatPfcEnablePeer = _LldpXdcbxFeatPfcEnablePeer_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 6945, 2, 3, 2, 1, 4),
    _LldpXdcbxFeatPfcEnablePeer_Type()
)
lldpXdcbxFeatPfcEnablePeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdcbxFeatPfcEnablePeer.setStatus("current")
_LldpXdcbxFeatAppProto_ObjectIdentity = ObjectIdentity
lldpXdcbxFeatAppProto = _LldpXdcbxFeatAppProto_ObjectIdentity(
    (1, 0, 8802, 1, 1, 2, 1, 5, 6945, 2, 4)
)
_LldpXdcbxFeatAppProtoTable_Object = MibTable
lldpXdcbxFeatAppProtoTable = _LldpXdcbxFeatAppProtoTable_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 6945, 2, 4, 1)
)
if mibBuilder.loadTexts:
    lldpXdcbxFeatAppProtoTable.setStatus("current")
_LldpXdcbxFeatAppProtoEntry_Object = MibTableRow
lldpXdcbxFeatAppProtoEntry = _LldpXdcbxFeatAppProtoEntry_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 6945, 2, 4, 1, 1)
)
lldpXdcbxFeatAppProtoEntry.setIndexNames(
    (0, "LLDP-EXT-DCBX-MIB", "lldpXdcbxPortNumber"),
    (0, "LLDP-EXT-DCBX-MIB", "lldpXdcbxFeatAppProtoIndex"),
)
if mibBuilder.loadTexts:
    lldpXdcbxFeatAppProtoEntry.setStatus("current")
_LldpXdcbxFeatAppProtoIndex_Type = LldpXdcbxAppProtos
_LldpXdcbxFeatAppProtoIndex_Object = MibTableColumn
lldpXdcbxFeatAppProtoIndex = _LldpXdcbxFeatAppProtoIndex_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 6945, 2, 4, 1, 1, 1),
    _LldpXdcbxFeatAppProtoIndex_Type()
)
lldpXdcbxFeatAppProtoIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpXdcbxFeatAppProtoIndex.setStatus("current")
_LldpXdcbxFeatAppProtoSF_Type = LldpXdcbxSF
_LldpXdcbxFeatAppProtoSF_Object = MibTableColumn
lldpXdcbxFeatAppProtoSF = _LldpXdcbxFeatAppProtoSF_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 6945, 2, 4, 1, 1, 2),
    _LldpXdcbxFeatAppProtoSF_Type()
)
lldpXdcbxFeatAppProtoSF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpXdcbxFeatAppProtoSF.setStatus("current")
_LldpXdcbxFeatAppProtoOUI_Type = Integer32
_LldpXdcbxFeatAppProtoOUI_Object = MibTableColumn
lldpXdcbxFeatAppProtoOUI = _LldpXdcbxFeatAppProtoOUI_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 6945, 2, 4, 1, 1, 3),
    _LldpXdcbxFeatAppProtoOUI_Type()
)
lldpXdcbxFeatAppProtoOUI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpXdcbxFeatAppProtoOUI.setStatus("current")
_LldpXdcbxFeatAppProtoId_Type = Integer32
_LldpXdcbxFeatAppProtoId_Object = MibTableColumn
lldpXdcbxFeatAppProtoId = _LldpXdcbxFeatAppProtoId_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 6945, 2, 4, 1, 1, 4),
    _LldpXdcbxFeatAppProtoId_Type()
)
lldpXdcbxFeatAppProtoId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpXdcbxFeatAppProtoId.setStatus("current")
_LldpXdcbxFeatAppProtoPrioTable_Object = MibTable
lldpXdcbxFeatAppProtoPrioTable = _LldpXdcbxFeatAppProtoPrioTable_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 6945, 2, 4, 2)
)
if mibBuilder.loadTexts:
    lldpXdcbxFeatAppProtoPrioTable.setStatus("current")
_LldpXdcbxFeatAppProtoPrioEntry_Object = MibTableRow
lldpXdcbxFeatAppProtoPrioEntry = _LldpXdcbxFeatAppProtoPrioEntry_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 6945, 2, 4, 2, 1)
)
lldpXdcbxFeatAppProtoPrioEntry.setIndexNames(
    (0, "LLDP-EXT-DCBX-MIB", "lldpXdcbxPortNumber"),
    (0, "LLDP-EXT-DCBX-MIB", "lldpXdcbxFeatAppProtoIndex"),
    (0, "LLDP-EXT-DCBX-MIB", "lldpXdcbxFeatAppProtoPriority"),
)
if mibBuilder.loadTexts:
    lldpXdcbxFeatAppProtoPrioEntry.setStatus("current")
_LldpXdcbxFeatAppProtoPriority_Type = LldpXdcbxPriority
_LldpXdcbxFeatAppProtoPriority_Object = MibTableColumn
lldpXdcbxFeatAppProtoPriority = _LldpXdcbxFeatAppProtoPriority_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 6945, 2, 4, 2, 1, 1),
    _LldpXdcbxFeatAppProtoPriority_Type()
)
lldpXdcbxFeatAppProtoPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpXdcbxFeatAppProtoPriority.setStatus("current")
_LldpXdcbxFeatAppProtoEnableDesired_Type = TruthValue
_LldpXdcbxFeatAppProtoEnableDesired_Object = MibTableColumn
lldpXdcbxFeatAppProtoEnableDesired = _LldpXdcbxFeatAppProtoEnableDesired_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 6945, 2, 4, 2, 1, 2),
    _LldpXdcbxFeatAppProtoEnableDesired_Type()
)
lldpXdcbxFeatAppProtoEnableDesired.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpXdcbxFeatAppProtoEnableDesired.setStatus("current")
_LldpXdcbxFeatAppProtoEnableOper_Type = TruthValue
_LldpXdcbxFeatAppProtoEnableOper_Object = MibTableColumn
lldpXdcbxFeatAppProtoEnableOper = _LldpXdcbxFeatAppProtoEnableOper_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 6945, 2, 4, 2, 1, 3),
    _LldpXdcbxFeatAppProtoEnableOper_Type()
)
lldpXdcbxFeatAppProtoEnableOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdcbxFeatAppProtoEnableOper.setStatus("current")
_LldpXdcbxFeatAppProtoEnablePeer_Type = TruthValue
_LldpXdcbxFeatAppProtoEnablePeer_Object = MibTableColumn
lldpXdcbxFeatAppProtoEnablePeer = _LldpXdcbxFeatAppProtoEnablePeer_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 6945, 2, 4, 2, 1, 4),
    _LldpXdcbxFeatAppProtoEnablePeer_Type()
)
lldpXdcbxFeatAppProtoEnablePeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdcbxFeatAppProtoEnablePeer.setStatus("current")

# Managed Objects groups


# Notification objects

lldpXdcbxMiscControlError = NotificationType(
    (1, 0, 8802, 1, 1, 2, 1, 5, 6945, 0, 1)
)
lldpXdcbxMiscControlError.setObjects(
    ("LLDP-EXT-DCBX-MIB", "lldpXdcbxPortNumber")
)
if mibBuilder.loadTexts:
    lldpXdcbxMiscControlError.setStatus(
        "current"
    )

lldpXdcbxMiscFeatureError = NotificationType(
    (1, 0, 8802, 1, 1, 2, 1, 5, 6945, 0, 2)
)
lldpXdcbxMiscFeatureError.setObjects(
    ("LLDP-EXT-DCBX-MIB", "lldpXdcbxFeatError")
)
if mibBuilder.loadTexts:
    lldpXdcbxMiscFeatureError.setStatus(
        "current"
    )

lldpXdcbxMultiplePeers = NotificationType(
    (1, 0, 8802, 1, 1, 2, 1, 5, 6945, 0, 3)
)
lldpXdcbxMultiplePeers.setObjects(
    ("LLDP-EXT-DCBX-MIB", "lldpXdcbxPortNumber")
)
if mibBuilder.loadTexts:
    lldpXdcbxMultiplePeers.setStatus(
        "current"
    )

lldpXdcbxLldpTxDisabled = NotificationType(
    (1, 0, 8802, 1, 1, 2, 1, 5, 6945, 0, 4)
)
lldpXdcbxLldpTxDisabled.setObjects(
    ("LLDP-EXT-DCBX-MIB", "lldpXdcbxPortNumber")
)
if mibBuilder.loadTexts:
    lldpXdcbxLldpTxDisabled.setStatus(
        "current"
    )

lldpXdcbxLldpRxDisabled = NotificationType(
    (1, 0, 8802, 1, 1, 2, 1, 5, 6945, 0, 5)
)
lldpXdcbxLldpRxDisabled.setObjects(
    ("LLDP-EXT-DCBX-MIB", "lldpXdcbxPortNumber")
)
if mibBuilder.loadTexts:
    lldpXdcbxLldpRxDisabled.setStatus(
        "current"
    )

lldpXdcbxDupControlTlv = NotificationType(
    (1, 0, 8802, 1, 1, 2, 1, 5, 6945, 0, 6)
)
lldpXdcbxDupControlTlv.setObjects(
    ("LLDP-EXT-DCBX-MIB", "lldpXdcbxPortNumber")
)
if mibBuilder.loadTexts:
    lldpXdcbxDupControlTlv.setStatus(
        "current"
    )

lldpXdcbxDupFeatureTlv = NotificationType(
    (1, 0, 8802, 1, 1, 2, 1, 5, 6945, 0, 7)
)
lldpXdcbxDupFeatureTlv.setObjects(
    ("LLDP-EXT-DCBX-MIB", "lldpXdcbxFeatType")
)
if mibBuilder.loadTexts:
    lldpXdcbxDupFeatureTlv.setStatus(
        "current"
    )

lldpXdcbxPeerNoFeat = NotificationType(
    (1, 0, 8802, 1, 1, 2, 1, 5, 6945, 0, 8)
)
lldpXdcbxPeerNoFeat.setObjects(
    ("LLDP-EXT-DCBX-MIB", "lldpXdcbxFeatType")
)
if mibBuilder.loadTexts:
    lldpXdcbxPeerNoFeat.setStatus(
        "current"
    )

lldpXdcbxPeerNoResp = NotificationType(
    (1, 0, 8802, 1, 1, 2, 1, 5, 6945, 0, 9)
)
lldpXdcbxPeerNoResp.setObjects(
    ("LLDP-EXT-DCBX-MIB", "lldpXdcbxPortNumber")
)
if mibBuilder.loadTexts:
    lldpXdcbxPeerNoResp.setStatus(
        "current"
    )

lldpXdcbxPeerConfigMismatch = NotificationType(
    (1, 0, 8802, 1, 1, 2, 1, 5, 6945, 0, 10)
)
lldpXdcbxPeerConfigMismatch.setObjects(
    ("LLDP-EXT-DCBX-MIB", "lldpXdcbxPortNumber")
)
if mibBuilder.loadTexts:
    lldpXdcbxPeerConfigMismatch.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LLDP-EXT-DCBX-MIB",
    **{"LldpXdcbxPriority": LldpXdcbxPriority,
       "LldpXdcbxPriorityGroup": LldpXdcbxPriorityGroup,
       "LldpXdcbxFeatureType": LldpXdcbxFeatureType,
       "LldpXdcbxFeatureSubType": LldpXdcbxFeatureSubType,
       "LldpXdcbxVersion": LldpXdcbxVersion,
       "LldpXdcbxTC": LldpXdcbxTC,
       "LldpXdcbxPgBw": LldpXdcbxPgBw,
       "LldpXdcbxTCPFC": LldpXdcbxTCPFC,
       "LldpXdcbxTCPeer": LldpXdcbxTCPeer,
       "LldpXdcbxAppProtos": LldpXdcbxAppProtos,
       "LldpXdcbxSF": LldpXdcbxSF,
       "lldpXdcbxMIB": lldpXdcbxMIB,
       "lldpXdcbxNotifications": lldpXdcbxNotifications,
       "lldpXdcbxMiscControlError": lldpXdcbxMiscControlError,
       "lldpXdcbxMiscFeatureError": lldpXdcbxMiscFeatureError,
       "lldpXdcbxMultiplePeers": lldpXdcbxMultiplePeers,
       "lldpXdcbxLldpTxDisabled": lldpXdcbxLldpTxDisabled,
       "lldpXdcbxLldpRxDisabled": lldpXdcbxLldpRxDisabled,
       "lldpXdcbxDupControlTlv": lldpXdcbxDupControlTlv,
       "lldpXdcbxDupFeatureTlv": lldpXdcbxDupFeatureTlv,
       "lldpXdcbxPeerNoFeat": lldpXdcbxPeerNoFeat,
       "lldpXdcbxPeerNoResp": lldpXdcbxPeerNoResp,
       "lldpXdcbxPeerConfigMismatch": lldpXdcbxPeerConfigMismatch,
       "lldpXdcbxObjects": lldpXdcbxObjects,
       "lldpXdcbxPortTable": lldpXdcbxPortTable,
       "lldpXdcbxPortEntry": lldpXdcbxPortEntry,
       "lldpXdcbxPortNumber": lldpXdcbxPortNumber,
       "lldpXdcbxPortEnable": lldpXdcbxPortEnable,
       "lldpXdcbxPortVersionOper": lldpXdcbxPortVersionOper,
       "lldpXdcbxPortVersionMax": lldpXdcbxPortVersionMax,
       "lldpXdcbxPortSeqNo": lldpXdcbxPortSeqNo,
       "lldpXdcbxPortAckNo": lldpXdcbxPortAckNo,
       "lldpXdcbxFeatures": lldpXdcbxFeatures,
       "lldpXdcbxFeatTable": lldpXdcbxFeatTable,
       "lldpXdcbxFeatEntry": lldpXdcbxFeatEntry,
       "lldpXdcbxFeatType": lldpXdcbxFeatType,
       "lldpXdcbxFeatSubType": lldpXdcbxFeatSubType,
       "lldpXdcbxFeatVersionOper": lldpXdcbxFeatVersionOper,
       "lldpXdcbxFeatVersionMax": lldpXdcbxFeatVersionMax,
       "lldpXdcbxFeatEnable": lldpXdcbxFeatEnable,
       "lldpXdcbxFeatWilling": lldpXdcbxFeatWilling,
       "lldpXdcbxFeatError": lldpXdcbxFeatError,
       "lldpXdcbxFeatAdvertise": lldpXdcbxFeatAdvertise,
       "lldpXdcbxFeatOperMode": lldpXdcbxFeatOperMode,
       "lldpXdcbxFeatSyncd": lldpXdcbxFeatSyncd,
       "lldpXdcbxFeatSeqNo": lldpXdcbxFeatSeqNo,
       "lldpXdcbxFeatPeerWilling": lldpXdcbxFeatPeerWilling,
       "lldpXdcbxFeatLocalParameterChange": lldpXdcbxFeatLocalParameterChange,
       "lldpXdcbxFeatPeerEnable": lldpXdcbxFeatPeerEnable,
       "lldpXdcbxFeatPeerError": lldpXdcbxFeatPeerError,
       "lldpXdcbxFeatPeerAdvertise": lldpXdcbxFeatPeerAdvertise,
       "lldpXdcbxFeatPeerTC": lldpXdcbxFeatPeerTC,
       "lldpXdcbxFeatPg": lldpXdcbxFeatPg,
       "lldpXdcbxFeatPgNumTCsSupported": lldpXdcbxFeatPgNumTCsSupported,
       "lldpXdcbxFeatPgPrioAllocTable": lldpXdcbxFeatPgPrioAllocTable,
       "lldpXdcbxFeatPgPrioAllocEntry": lldpXdcbxFeatPgPrioAllocEntry,
       "lldpXdcbxFeatPgPrioAllocPrioId": lldpXdcbxFeatPgPrioAllocPrioId,
       "lldpXdcbxFeatPgPrioAllocPgIdDesired": lldpXdcbxFeatPgPrioAllocPgIdDesired,
       "lldpXdcbxFeatPgPrioAllocPgIdOper": lldpXdcbxFeatPgPrioAllocPgIdOper,
       "lldpXdcbxFeatPgPrioAllocPgIdPeer": lldpXdcbxFeatPgPrioAllocPgIdPeer,
       "lldpXdcbxFeatPgBwAllocTable": lldpXdcbxFeatPgBwAllocTable,
       "lldpXdcbxFeatPgBwAllocEntry": lldpXdcbxFeatPgBwAllocEntry,
       "lldpXdcbxFeatPgBwAllocPgId": lldpXdcbxFeatPgBwAllocPgId,
       "lldpXdcbxFeatPgBwAllocBwDesired": lldpXdcbxFeatPgBwAllocBwDesired,
       "lldpXdcbxFeatPgBwAllocBwOper": lldpXdcbxFeatPgBwAllocBwOper,
       "lldpXdcbxFeatPgBwAllocBwPeer": lldpXdcbxFeatPgBwAllocBwPeer,
       "lldpXdcbxFeatPfc": lldpXdcbxFeatPfc,
       "lldpXdcbxFeatPfcNumTCPFCSupported": lldpXdcbxFeatPfcNumTCPFCSupported,
       "lldpXdcbxFeatPfcTable": lldpXdcbxFeatPfcTable,
       "lldpXdcbxFeatPfcEntry": lldpXdcbxFeatPfcEntry,
       "lldpXdcbxFeatPfcPriority": lldpXdcbxFeatPfcPriority,
       "lldpXdcbxFeatPfcEnableDesired": lldpXdcbxFeatPfcEnableDesired,
       "lldpXdcbxFeatPfcEnableOper": lldpXdcbxFeatPfcEnableOper,
       "lldpXdcbxFeatPfcEnablePeer": lldpXdcbxFeatPfcEnablePeer,
       "lldpXdcbxFeatAppProto": lldpXdcbxFeatAppProto,
       "lldpXdcbxFeatAppProtoTable": lldpXdcbxFeatAppProtoTable,
       "lldpXdcbxFeatAppProtoEntry": lldpXdcbxFeatAppProtoEntry,
       "lldpXdcbxFeatAppProtoIndex": lldpXdcbxFeatAppProtoIndex,
       "lldpXdcbxFeatAppProtoSF": lldpXdcbxFeatAppProtoSF,
       "lldpXdcbxFeatAppProtoOUI": lldpXdcbxFeatAppProtoOUI,
       "lldpXdcbxFeatAppProtoId": lldpXdcbxFeatAppProtoId,
       "lldpXdcbxFeatAppProtoPrioTable": lldpXdcbxFeatAppProtoPrioTable,
       "lldpXdcbxFeatAppProtoPrioEntry": lldpXdcbxFeatAppProtoPrioEntry,
       "lldpXdcbxFeatAppProtoPriority": lldpXdcbxFeatAppProtoPriority,
       "lldpXdcbxFeatAppProtoEnableDesired": lldpXdcbxFeatAppProtoEnableDesired,
       "lldpXdcbxFeatAppProtoEnableOper": lldpXdcbxFeatAppProtoEnableOper,
       "lldpXdcbxFeatAppProtoEnablePeer": lldpXdcbxFeatAppProtoEnablePeer}
)
