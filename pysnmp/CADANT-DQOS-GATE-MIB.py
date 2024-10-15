# SNMP MIB module (CADANT-DQOS-GATE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CADANT-DQOS-GATE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:52:56 2024
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

(cadPCMibObjects,) = mibBuilder.importSymbols(
    "CADANT-CMTS-PACKETCABLE-MIB",
    "cadPCMibObjects")

(InetAddressIPv4or6,) = mibBuilder.importSymbols(
    "CADANT-TC",
    "InetAddressIPv4or6")

(docsQosIfDirection,) = mibBuilder.importSymbols(
    "DOCS-QOS3-MIB",
    "docsQosIfDirection")

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

cadDQoSMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 2)
)
cadDQoSMib.setRevisions(
        ("2001-08-09 00:00",
         "2003-01-07 00:00",
         "2003-03-21 00:00",
         "2003-05-23 00:00",
         "2004-01-19 00:00",
         "2004-02-11 00:00",
         "2005-09-30 00:00",
         "2007-10-24 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CadDQoSSource(Integer32, TextualConvention):
    status = "current"
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
        *(("compiledIntoCode", 6),
          ("configurationFile", 2),
          ("externalDatabase", 3),
          ("other", 4),
          ("policyServer", 5),
          ("snmp", 1))
    )



class PCReasonCode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              127)
        )
    )
    namedValues = NamedValues(
        *(("deregistration", 3),
          ("newGateForFlows", 8),
          ("noReason", -1),
          ("normal", 0),
          ("reservationMaintFail", 2),
          ("resourceReassignment", 1),
          ("timerT0Expiry", 4),
          ("timerT1Expiry", 5),
          ("timerT7Expiry", 6),
          ("timerT8Expiry", 7),
          ("unspecified", 127))
    )



class SDPString(OctetString, TextualConvention):
    status = "current"
    displayHint = "1024a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )



# MIB Managed Objects in the order of their OIDs

_CadDQoSMibObjects_ObjectIdentity = ObjectIdentity
cadDQoSMibObjects = _CadDQoSMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 2, 1)
)
_CadDQoSConfigBase_ObjectIdentity = ObjectIdentity
cadDQoSConfigBase = _CadDQoSConfigBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 2, 1, 1)
)
_CadDQoSGateTable_Object = MibTable
cadDQoSGateTable = _CadDQoSGateTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cadDQoSGateTable.setStatus("current")
_CadDQoSGateEntry_Object = MibTableRow
cadDQoSGateEntry = _CadDQoSGateEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 2, 1, 1, 1, 1)
)
cadDQoSGateEntry.setIndexNames(
    (0, "DOCS-QOS3-MIB", "docsQosIfDirection"),
    (0, "CADANT-DQOS-GATE-MIB", "cadDQoSGateId"),
)
if mibBuilder.loadTexts:
    cadDQoSGateEntry.setStatus("current")
_CadDQoSGateId_Type = Unsigned32
_CadDQoSGateId_Object = MibTableColumn
cadDQoSGateId = _CadDQoSGateId_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 2, 1, 1, 1, 1, 1),
    _CadDQoSGateId_Type()
)
cadDQoSGateId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadDQoSGateId.setStatus("current")
_CadDQoSGateSubscriberID_Type = InetAddressIPv4or6
_CadDQoSGateSubscriberID_Object = MibTableColumn
cadDQoSGateSubscriberID = _CadDQoSGateSubscriberID_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 2, 1, 1, 1, 1, 2),
    _CadDQoSGateSubscriberID_Type()
)
cadDQoSGateSubscriberID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadDQoSGateSubscriberID.setStatus("current")
_CadDQoSGateClassifierProtoID_Type = Unsigned32
_CadDQoSGateClassifierProtoID_Object = MibTableColumn
cadDQoSGateClassifierProtoID = _CadDQoSGateClassifierProtoID_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 2, 1, 1, 1, 1, 3),
    _CadDQoSGateClassifierProtoID_Type()
)
cadDQoSGateClassifierProtoID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadDQoSGateClassifierProtoID.setStatus("current")
_CadDQoSGateClassifierSrcIP_Type = InetAddressIPv4or6
_CadDQoSGateClassifierSrcIP_Object = MibTableColumn
cadDQoSGateClassifierSrcIP = _CadDQoSGateClassifierSrcIP_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 2, 1, 1, 1, 1, 4),
    _CadDQoSGateClassifierSrcIP_Type()
)
cadDQoSGateClassifierSrcIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadDQoSGateClassifierSrcIP.setStatus("current")
_CadDQoSGateClassifierDestIP_Type = InetAddressIPv4or6
_CadDQoSGateClassifierDestIP_Object = MibTableColumn
cadDQoSGateClassifierDestIP = _CadDQoSGateClassifierDestIP_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 2, 1, 1, 1, 1, 5),
    _CadDQoSGateClassifierDestIP_Type()
)
cadDQoSGateClassifierDestIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadDQoSGateClassifierDestIP.setStatus("current")
_CadDQoSGateClassifierSrcPort_Type = Unsigned32
_CadDQoSGateClassifierSrcPort_Object = MibTableColumn
cadDQoSGateClassifierSrcPort = _CadDQoSGateClassifierSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 2, 1, 1, 1, 1, 6),
    _CadDQoSGateClassifierSrcPort_Type()
)
cadDQoSGateClassifierSrcPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadDQoSGateClassifierSrcPort.setStatus("current")
_CadDQoSGateClassifierDestPort_Type = Unsigned32
_CadDQoSGateClassifierDestPort_Object = MibTableColumn
cadDQoSGateClassifierDestPort = _CadDQoSGateClassifierDestPort_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 2, 1, 1, 1, 1, 7),
    _CadDQoSGateClassifierDestPort_Type()
)
cadDQoSGateClassifierDestPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadDQoSGateClassifierDestPort.setStatus("current")


class _CadDQoSMgmtGateCommitNotAllowed_Type(TruthValue):
    """Custom type cadDQoSMgmtGateCommitNotAllowed based on TruthValue"""


_CadDQoSMgmtGateCommitNotAllowed_Object = MibTableColumn
cadDQoSMgmtGateCommitNotAllowed = _CadDQoSMgmtGateCommitNotAllowed_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 2, 1, 1, 1, 1, 8),
    _CadDQoSMgmtGateCommitNotAllowed_Type()
)
cadDQoSMgmtGateCommitNotAllowed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadDQoSMgmtGateCommitNotAllowed.setStatus("current")


class _CadDQoSGateAutoCommit_Type(TruthValue):
    """Custom type cadDQoSGateAutoCommit based on TruthValue"""


_CadDQoSGateAutoCommit_Object = MibTableColumn
cadDQoSGateAutoCommit = _CadDQoSGateAutoCommit_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 2, 1, 1, 1, 1, 9),
    _CadDQoSGateAutoCommit_Type()
)
cadDQoSGateAutoCommit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadDQoSGateAutoCommit.setStatus("current")
_CadDQoSGateResourceID_Type = Unsigned32
_CadDQoSGateResourceID_Object = MibTableColumn
cadDQoSGateResourceID = _CadDQoSGateResourceID_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 2, 1, 1, 1, 1, 17),
    _CadDQoSGateResourceID_Type()
)
cadDQoSGateResourceID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadDQoSGateResourceID.setStatus("current")


class _CadDQoSGateSessionClass_Type(Integer32):
    """Custom type cadDQoSGateSessionClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("emergency", 2),
          ("normalVoIP", 1),
          ("unspecified", 0))
    )


_CadDQoSGateSessionClass_Type.__name__ = "Integer32"
_CadDQoSGateSessionClass_Object = MibTableColumn
cadDQoSGateSessionClass = _CadDQoSGateSessionClass_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 2, 1, 1, 1, 1, 18),
    _CadDQoSGateSessionClass_Type()
)
cadDQoSGateSessionClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadDQoSGateSessionClass.setStatus("current")


class _CadDQoSGateDSField_Type(Unsigned32):
    """Custom type cadDQoSGateDSField based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CadDQoSGateDSField_Type.__name__ = "Unsigned32"
_CadDQoSGateDSField_Object = MibTableColumn
cadDQoSGateDSField = _CadDQoSGateDSField_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 2, 1, 1, 1, 1, 19),
    _CadDQoSGateDSField_Type()
)
cadDQoSGateDSField.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadDQoSGateDSField.setStatus("current")


class _CadDQoSGateTimerT7_Type(Unsigned32):
    """Custom type cadDQoSGateTimerT7 based on Unsigned32"""
    defaultValue = 200

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_CadDQoSGateTimerT7_Type.__name__ = "Unsigned32"
_CadDQoSGateTimerT7_Object = MibTableColumn
cadDQoSGateTimerT7 = _CadDQoSGateTimerT7_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 2, 1, 1, 1, 1, 20),
    _CadDQoSGateTimerT7_Type()
)
cadDQoSGateTimerT7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadDQoSGateTimerT7.setStatus("current")
if mibBuilder.loadTexts:
    cadDQoSGateTimerT7.setUnits("seconds")


class _CadDQoSGateTimerT8_Type(Unsigned32):
    """Custom type cadDQoSGateTimerT8 based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_CadDQoSGateTimerT8_Type.__name__ = "Unsigned32"
_CadDQoSGateTimerT8_Object = MibTableColumn
cadDQoSGateTimerT8 = _CadDQoSGateTimerT8_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 2, 1, 1, 1, 1, 21),
    _CadDQoSGateTimerT8_Type()
)
cadDQoSGateTimerT8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadDQoSGateTimerT8.setStatus("current")
if mibBuilder.loadTexts:
    cadDQoSGateTimerT8.setUnits("seconds")


class _CadDQoSGateReserveRequest_Type(TruthValue):
    """Custom type cadDQoSGateReserveRequest based on TruthValue"""


_CadDQoSGateReserveRequest_Object = MibTableColumn
cadDQoSGateReserveRequest = _CadDQoSGateReserveRequest_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 2, 1, 1, 1, 1, 22),
    _CadDQoSGateReserveRequest_Type()
)
cadDQoSGateReserveRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadDQoSGateReserveRequest.setStatus("current")


class _CadDQoSGateCommited_Type(TruthValue):
    """Custom type cadDQoSGateCommited based on TruthValue"""


_CadDQoSGateCommited_Object = MibTableColumn
cadDQoSGateCommited = _CadDQoSGateCommited_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 2, 1, 1, 1, 1, 23),
    _CadDQoSGateCommited_Type()
)
cadDQoSGateCommited.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadDQoSGateCommited.setStatus("current")


class _CadDQoSTearFlows_Type(PCReasonCode):
    """Custom type cadDQoSTearFlows based on PCReasonCode"""


_CadDQoSTearFlows_Object = MibTableColumn
cadDQoSTearFlows = _CadDQoSTearFlows_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 2, 1, 1, 1, 1, 24),
    _CadDQoSTearFlows_Type()
)
cadDQoSTearFlows.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadDQoSTearFlows.setStatus("current")
_CadDQoSGateESPDupContent_Type = TruthValue
_CadDQoSGateESPDupContent_Object = MibTableColumn
cadDQoSGateESPDupContent = _CadDQoSGateESPDupContent_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 2, 1, 1, 1, 1, 25),
    _CadDQoSGateESPDupContent_Type()
)
cadDQoSGateESPDupContent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadDQoSGateESPDupContent.setStatus("current")
_CadDQoSGateESPDfCCCIp_Type = InetAddressIPv4or6
_CadDQoSGateESPDfCCCIp_Object = MibTableColumn
cadDQoSGateESPDfCCCIp = _CadDQoSGateESPDfCCCIp_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 2, 1, 1, 1, 1, 26),
    _CadDQoSGateESPDfCCCIp_Type()
)
cadDQoSGateESPDfCCCIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadDQoSGateESPDfCCCIp.setStatus("current")
_CadDQoSGateESPDfCCCPort_Type = Unsigned32
_CadDQoSGateESPDfCCCPort_Object = MibTableColumn
cadDQoSGateESPDfCCCPort = _CadDQoSGateESPDfCCCPort_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 2, 1, 1, 1, 1, 27),
    _CadDQoSGateESPDfCCCPort_Type()
)
cadDQoSGateESPDfCCCPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadDQoSGateESPDfCCCPort.setStatus("current")


class _CadDQoSSFID_Type(Unsigned32):
    """Custom type cadDQoSSFID based on Unsigned32"""
    defaultValue = 0


_CadDQoSSFID_Object = MibTableColumn
cadDQoSSFID = _CadDQoSSFID_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 2, 1, 1, 1, 1, 28),
    _CadDQoSSFID_Type()
)
cadDQoSSFID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadDQoSSFID.setStatus("current")
_CadDQoSGateESPCCCId_Type = Unsigned32
_CadDQoSGateESPCCCId_Object = MibTableColumn
cadDQoSGateESPCCCId = _CadDQoSGateESPCCCId_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 2, 1, 1, 1, 1, 29),
    _CadDQoSGateESPCCCId_Type()
)
cadDQoSGateESPCCCId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadDQoSGateESPCCCId.setStatus("current")
_CadDQoSGateESPSrcCCCIp_Type = InetAddressIPv4or6
_CadDQoSGateESPSrcCCCIp_Object = MibTableColumn
cadDQoSGateESPSrcCCCIp = _CadDQoSGateESPSrcCCCIp_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 2, 1, 1, 1, 1, 30),
    _CadDQoSGateESPSrcCCCIp_Type()
)
cadDQoSGateESPSrcCCCIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadDQoSGateESPSrcCCCIp.setStatus("current")


class _CadDQoSGateServiceClassName_Type(DisplayString):
    """Custom type cadDQoSGateServiceClassName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_CadDQoSGateServiceClassName_Type.__name__ = "DisplayString"
_CadDQoSGateServiceClassName_Object = MibTableColumn
cadDQoSGateServiceClassName = _CadDQoSGateServiceClassName_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 2, 1, 1, 1, 1, 31),
    _CadDQoSGateServiceClassName_Type()
)
cadDQoSGateServiceClassName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadDQoSGateServiceClassName.setStatus("current")


class _CadDQoSGateUsSFSchedType_Type(Unsigned32):
    """Custom type cadDQoSGateUsSFSchedType based on Unsigned32"""
    defaultValue = 0


_CadDQoSGateUsSFSchedType_Object = MibTableColumn
cadDQoSGateUsSFSchedType = _CadDQoSGateUsSFSchedType_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 2, 1, 1, 1, 1, 32),
    _CadDQoSGateUsSFSchedType_Type()
)
cadDQoSGateUsSFSchedType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadDQoSGateUsSFSchedType.setStatus("current")


class _CadDQoSGateUsNomGrantInterval_Type(Unsigned32):
    """Custom type cadDQoSGateUsNomGrantInterval based on Unsigned32"""
    defaultValue = 0


_CadDQoSGateUsNomGrantInterval_Object = MibTableColumn
cadDQoSGateUsNomGrantInterval = _CadDQoSGateUsNomGrantInterval_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 2, 1, 1, 1, 1, 33),
    _CadDQoSGateUsNomGrantInterval_Type()
)
cadDQoSGateUsNomGrantInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadDQoSGateUsNomGrantInterval.setStatus("current")


class _CadDQoSGateUsTolGrantJitter_Type(Unsigned32):
    """Custom type cadDQoSGateUsTolGrantJitter based on Unsigned32"""
    defaultValue = 0


_CadDQoSGateUsTolGrantJitter_Object = MibTableColumn
cadDQoSGateUsTolGrantJitter = _CadDQoSGateUsTolGrantJitter_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 2, 1, 1, 1, 1, 34),
    _CadDQoSGateUsTolGrantJitter_Type()
)
cadDQoSGateUsTolGrantJitter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadDQoSGateUsTolGrantJitter.setStatus("current")


class _CadDQoSGateUsGrantsPerInterval_Type(Unsigned32):
    """Custom type cadDQoSGateUsGrantsPerInterval based on Unsigned32"""
    defaultValue = 0


_CadDQoSGateUsGrantsPerInterval_Object = MibTableColumn
cadDQoSGateUsGrantsPerInterval = _CadDQoSGateUsGrantsPerInterval_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 2, 1, 1, 1, 1, 35),
    _CadDQoSGateUsGrantsPerInterval_Type()
)
cadDQoSGateUsGrantsPerInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadDQoSGateUsGrantsPerInterval.setStatus("current")


class _CadDQoSGateUsUnsolitedGrantSize_Type(Unsigned32):
    """Custom type cadDQoSGateUsUnsolitedGrantSize based on Unsigned32"""
    defaultValue = 0


_CadDQoSGateUsUnsolitedGrantSize_Object = MibTableColumn
cadDQoSGateUsUnsolitedGrantSize = _CadDQoSGateUsUnsolitedGrantSize_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 2, 1, 1, 1, 1, 36),
    _CadDQoSGateUsUnsolitedGrantSize_Type()
)
cadDQoSGateUsUnsolitedGrantSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadDQoSGateUsUnsolitedGrantSize.setStatus("current")


class _CadDQoSGateUsReqTransPolicy_Type(Unsigned32):
    """Custom type cadDQoSGateUsReqTransPolicy based on Unsigned32"""
    defaultValue = 0


_CadDQoSGateUsReqTransPolicy_Object = MibTableColumn
cadDQoSGateUsReqTransPolicy = _CadDQoSGateUsReqTransPolicy_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 2, 1, 1, 1, 1, 37),
    _CadDQoSGateUsReqTransPolicy_Type()
)
cadDQoSGateUsReqTransPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadDQoSGateUsReqTransPolicy.setStatus("current")


class _CadDQoSGateUsNomPollingInterval_Type(Unsigned32):
    """Custom type cadDQoSGateUsNomPollingInterval based on Unsigned32"""
    defaultValue = 0


_CadDQoSGateUsNomPollingInterval_Object = MibTableColumn
cadDQoSGateUsNomPollingInterval = _CadDQoSGateUsNomPollingInterval_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 2, 1, 1, 1, 1, 38),
    _CadDQoSGateUsNomPollingInterval_Type()
)
cadDQoSGateUsNomPollingInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadDQoSGateUsNomPollingInterval.setStatus("current")


class _CadDQoSGateUsTolPollJitter_Type(Unsigned32):
    """Custom type cadDQoSGateUsTolPollJitter based on Unsigned32"""
    defaultValue = 0


_CadDQoSGateUsTolPollJitter_Object = MibTableColumn
cadDQoSGateUsTolPollJitter = _CadDQoSGateUsTolPollJitter_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 2, 1, 1, 1, 1, 39),
    _CadDQoSGateUsTolPollJitter_Type()
)
cadDQoSGateUsTolPollJitter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadDQoSGateUsTolPollJitter.setStatus("current")


class _CadDQoSGateUsIpToSOverride_Type(Unsigned32):
    """Custom type cadDQoSGateUsIpToSOverride based on Unsigned32"""
    defaultValue = 0


_CadDQoSGateUsIpToSOverride_Object = MibTableColumn
cadDQoSGateUsIpToSOverride = _CadDQoSGateUsIpToSOverride_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 2, 1, 1, 1, 1, 40),
    _CadDQoSGateUsIpToSOverride_Type()
)
cadDQoSGateUsIpToSOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadDQoSGateUsIpToSOverride.setStatus("current")


class _CadDQoSGateUsMaxConcatBurst_Type(Unsigned32):
    """Custom type cadDQoSGateUsMaxConcatBurst based on Unsigned32"""
    defaultValue = 0


_CadDQoSGateUsMaxConcatBurst_Object = MibTableColumn
cadDQoSGateUsMaxConcatBurst = _CadDQoSGateUsMaxConcatBurst_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 2, 1, 1, 1, 1, 41),
    _CadDQoSGateUsMaxConcatBurst_Type()
)
cadDQoSGateUsMaxConcatBurst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadDQoSGateUsMaxConcatBurst.setStatus("current")


class _CadDQoSGateDsTrafficPriority_Type(Unsigned32):
    """Custom type cadDQoSGateDsTrafficPriority based on Unsigned32"""
    defaultValue = 0


_CadDQoSGateDsTrafficPriority_Object = MibTableColumn
cadDQoSGateDsTrafficPriority = _CadDQoSGateDsTrafficPriority_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 2, 1, 1, 1, 1, 42),
    _CadDQoSGateDsTrafficPriority_Type()
)
cadDQoSGateDsTrafficPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadDQoSGateDsTrafficPriority.setStatus("current")


class _CadDQoSGateDsMaxSustainedRate_Type(Unsigned32):
    """Custom type cadDQoSGateDsMaxSustainedRate based on Unsigned32"""
    defaultValue = 0


_CadDQoSGateDsMaxSustainedRate_Object = MibTableColumn
cadDQoSGateDsMaxSustainedRate = _CadDQoSGateDsMaxSustainedRate_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 2, 1, 1, 1, 1, 43),
    _CadDQoSGateDsMaxSustainedRate_Type()
)
cadDQoSGateDsMaxSustainedRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadDQoSGateDsMaxSustainedRate.setStatus("current")


class _CadDQoSGateDsMaxTrafBurst_Type(Unsigned32):
    """Custom type cadDQoSGateDsMaxTrafBurst based on Unsigned32"""
    defaultValue = 0


_CadDQoSGateDsMaxTrafBurst_Object = MibTableColumn
cadDQoSGateDsMaxTrafBurst = _CadDQoSGateDsMaxTrafBurst_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 2, 1, 1, 1, 1, 44),
    _CadDQoSGateDsMaxTrafBurst_Type()
)
cadDQoSGateDsMaxTrafBurst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadDQoSGateDsMaxTrafBurst.setStatus("current")


class _CadDQoSGateDsMinReservedTrafRate_Type(Unsigned32):
    """Custom type cadDQoSGateDsMinReservedTrafRate based on Unsigned32"""
    defaultValue = 0


_CadDQoSGateDsMinReservedTrafRate_Object = MibTableColumn
cadDQoSGateDsMinReservedTrafRate = _CadDQoSGateDsMinReservedTrafRate_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 2, 1, 1, 1, 1, 45),
    _CadDQoSGateDsMinReservedTrafRate_Type()
)
cadDQoSGateDsMinReservedTrafRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadDQoSGateDsMinReservedTrafRate.setStatus("current")


class _CadDQoSGateDsMinPacketSize_Type(Unsigned32):
    """Custom type cadDQoSGateDsMinPacketSize based on Unsigned32"""
    defaultValue = 0


_CadDQoSGateDsMinPacketSize_Object = MibTableColumn
cadDQoSGateDsMinPacketSize = _CadDQoSGateDsMinPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 2, 1, 1, 1, 1, 46),
    _CadDQoSGateDsMinPacketSize_Type()
)
cadDQoSGateDsMinPacketSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadDQoSGateDsMinPacketSize.setStatus("current")


class _CadDQoSGateDsMaxLatency_Type(Unsigned32):
    """Custom type cadDQoSGateDsMaxLatency based on Unsigned32"""
    defaultValue = 0


_CadDQoSGateDsMaxLatency_Object = MibTableColumn
cadDQoSGateDsMaxLatency = _CadDQoSGateDsMaxLatency_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 2, 1, 1, 1, 1, 47),
    _CadDQoSGateDsMaxLatency_Type()
)
cadDQoSGateDsMaxLatency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadDQoSGateDsMaxLatency.setStatus("current")
_CadDQoSMgmtGateTable_Object = MibTable
cadDQoSMgmtGateTable = _CadDQoSMgmtGateTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 2, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cadDQoSMgmtGateTable.setStatus("current")
_CadDQoSMgmtGateEntry_Object = MibTableRow
cadDQoSMgmtGateEntry = _CadDQoSMgmtGateEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 2, 1, 1, 2, 1)
)
cadDQoSMgmtGateEntry.setIndexNames(
    (0, "DOCS-QOS3-MIB", "docsQosIfDirection"),
    (0, "CADANT-DQOS-GATE-MIB", "cadDQoSGateId"),
)
if mibBuilder.loadTexts:
    cadDQoSMgmtGateEntry.setStatus("current")
_CadDQoSMgmtGateControllerIP_Type = InetAddressIPv4or6
_CadDQoSMgmtGateControllerIP_Object = MibTableColumn
cadDQoSMgmtGateControllerIP = _CadDQoSMgmtGateControllerIP_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 2, 1, 1, 2, 1, 1),
    _CadDQoSMgmtGateControllerIP_Type()
)
cadDQoSMgmtGateControllerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadDQoSMgmtGateControllerIP.setStatus("current")
_CadDQoSMgmtGateRemoteGateIP_Type = InetAddressIPv4or6
_CadDQoSMgmtGateRemoteGateIP_Object = MibTableColumn
cadDQoSMgmtGateRemoteGateIP = _CadDQoSMgmtGateRemoteGateIP_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 2, 1, 1, 2, 1, 2),
    _CadDQoSMgmtGateRemoteGateIP_Type()
)
cadDQoSMgmtGateRemoteGateIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadDQoSMgmtGateRemoteGateIP.setStatus("current")
_CadDQoSMgmtGateRemoteGatePort_Type = Unsigned32
_CadDQoSMgmtGateRemoteGatePort_Object = MibTableColumn
cadDQoSMgmtGateRemoteGatePort = _CadDQoSMgmtGateRemoteGatePort_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 2, 1, 1, 2, 1, 3),
    _CadDQoSMgmtGateRemoteGatePort_Type()
)
cadDQoSMgmtGateRemoteGatePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadDQoSMgmtGateRemoteGatePort.setStatus("current")
_CadDQoSMgmtGateRemoteGateNoRequireGateOpen_Type = TruthValue
_CadDQoSMgmtGateRemoteGateNoRequireGateOpen_Object = MibTableColumn
cadDQoSMgmtGateRemoteGateNoRequireGateOpen = _CadDQoSMgmtGateRemoteGateNoRequireGateOpen_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 2, 1, 1, 2, 1, 4),
    _CadDQoSMgmtGateRemoteGateNoRequireGateOpen_Type()
)
cadDQoSMgmtGateRemoteGateNoRequireGateOpen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadDQoSMgmtGateRemoteGateNoRequireGateOpen.setStatus("current")
_CadDQoSMgmtGateRemoteGateNoSendGateOpen_Type = TruthValue
_CadDQoSMgmtGateRemoteGateNoSendGateOpen_Object = MibTableColumn
cadDQoSMgmtGateRemoteGateNoSendGateOpen = _CadDQoSMgmtGateRemoteGateNoSendGateOpen_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 2, 1, 1, 2, 1, 5),
    _CadDQoSMgmtGateRemoteGateNoSendGateOpen_Type()
)
cadDQoSMgmtGateRemoteGateNoSendGateOpen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadDQoSMgmtGateRemoteGateNoSendGateOpen.setStatus("current")
_CadDQoSMgmtGateRemoteGateID_Type = Unsigned32
_CadDQoSMgmtGateRemoteGateID_Object = MibTableColumn
cadDQoSMgmtGateRemoteGateID = _CadDQoSMgmtGateRemoteGateID_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 2, 1, 1, 2, 1, 6),
    _CadDQoSMgmtGateRemoteGateID_Type()
)
cadDQoSMgmtGateRemoteGateID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadDQoSMgmtGateRemoteGateID.setStatus("current")


class _CadDQoSMgmtGateRemoteGateAlgorithm_Type(Integer32):
    """Custom type cadDQoSMgmtGateRemoteGateAlgorithm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            100
        )
    )
    namedValues = NamedValues(
        ("md5BasedMac", 100)
    )


_CadDQoSMgmtGateRemoteGateAlgorithm_Type.__name__ = "Integer32"
_CadDQoSMgmtGateRemoteGateAlgorithm_Object = MibTableColumn
cadDQoSMgmtGateRemoteGateAlgorithm = _CadDQoSMgmtGateRemoteGateAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 2, 1, 1, 2, 1, 7),
    _CadDQoSMgmtGateRemoteGateAlgorithm_Type()
)
cadDQoSMgmtGateRemoteGateAlgorithm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadDQoSMgmtGateRemoteGateAlgorithm.setStatus("current")


class _CadDQoSMgmtGateRemoteGateSecurityKey_Type(OctetString):
    """Custom type cadDQoSMgmtGateRemoteGateSecurityKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CadDQoSMgmtGateRemoteGateSecurityKey_Type.__name__ = "OctetString"
_CadDQoSMgmtGateRemoteGateSecurityKey_Object = MibTableColumn
cadDQoSMgmtGateRemoteGateSecurityKey = _CadDQoSMgmtGateRemoteGateSecurityKey_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 2, 1, 1, 2, 1, 8),
    _CadDQoSMgmtGateRemoteGateSecurityKey_Type()
)
cadDQoSMgmtGateRemoteGateSecurityKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadDQoSMgmtGateRemoteGateSecurityKey.setStatus("current")
_CadDQoSMgmtGateEventGenPriRKSIP_Type = InetAddressIPv4or6
_CadDQoSMgmtGateEventGenPriRKSIP_Object = MibTableColumn
cadDQoSMgmtGateEventGenPriRKSIP = _CadDQoSMgmtGateEventGenPriRKSIP_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 2, 1, 1, 2, 1, 9),
    _CadDQoSMgmtGateEventGenPriRKSIP_Type()
)
cadDQoSMgmtGateEventGenPriRKSIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadDQoSMgmtGateEventGenPriRKSIP.setStatus("current")
_CadDQoSMgmtGateEventGenPriRKSPort_Type = Unsigned32
_CadDQoSMgmtGateEventGenPriRKSPort_Object = MibTableColumn
cadDQoSMgmtGateEventGenPriRKSPort = _CadDQoSMgmtGateEventGenPriRKSPort_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 2, 1, 1, 2, 1, 10),
    _CadDQoSMgmtGateEventGenPriRKSPort_Type()
)
cadDQoSMgmtGateEventGenPriRKSPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadDQoSMgmtGateEventGenPriRKSPort.setStatus("current")
_CadDQoSMgmtGateEventGenBatchIndicator_Type = TruthValue
_CadDQoSMgmtGateEventGenBatchIndicator_Object = MibTableColumn
cadDQoSMgmtGateEventGenBatchIndicator = _CadDQoSMgmtGateEventGenBatchIndicator_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 2, 1, 1, 2, 1, 11),
    _CadDQoSMgmtGateEventGenBatchIndicator_Type()
)
cadDQoSMgmtGateEventGenBatchIndicator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadDQoSMgmtGateEventGenBatchIndicator.setStatus("current")
_CadDQoSMgmtGateEventGenSecRKSIP_Type = InetAddressIPv4or6
_CadDQoSMgmtGateEventGenSecRKSIP_Object = MibTableColumn
cadDQoSMgmtGateEventGenSecRKSIP = _CadDQoSMgmtGateEventGenSecRKSIP_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 2, 1, 1, 2, 1, 12),
    _CadDQoSMgmtGateEventGenSecRKSIP_Type()
)
cadDQoSMgmtGateEventGenSecRKSIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadDQoSMgmtGateEventGenSecRKSIP.setStatus("current")
_CadDQoSMgmtGateEventGenSecRKSPort_Type = Unsigned32
_CadDQoSMgmtGateEventGenSecRKSPort_Object = MibTableColumn
cadDQoSMgmtGateEventGenSecRKSPort = _CadDQoSMgmtGateEventGenSecRKSPort_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 2, 1, 1, 2, 1, 13),
    _CadDQoSMgmtGateEventGenSecRKSPort_Type()
)
cadDQoSMgmtGateEventGenSecRKSPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadDQoSMgmtGateEventGenSecRKSPort.setStatus("current")
_CadDQoSMgmtGateEventGenBillCorrID_Type = Unsigned32
_CadDQoSMgmtGateEventGenBillCorrID_Object = MibTableColumn
cadDQoSMgmtGateEventGenBillCorrID = _CadDQoSMgmtGateEventGenBillCorrID_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 2, 1, 1, 2, 1, 14),
    _CadDQoSMgmtGateEventGenBillCorrID_Type()
)
cadDQoSMgmtGateEventGenBillCorrID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadDQoSMgmtGateEventGenBillCorrID.setStatus("current")


class _CadDQoSMgmtGateMediaConnCalledParty_Type(DisplayString):
    """Custom type cadDQoSMgmtGateMediaConnCalledParty based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CadDQoSMgmtGateMediaConnCalledParty_Type.__name__ = "DisplayString"
_CadDQoSMgmtGateMediaConnCalledParty_Object = MibTableColumn
cadDQoSMgmtGateMediaConnCalledParty = _CadDQoSMgmtGateMediaConnCalledParty_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 2, 1, 1, 2, 1, 15),
    _CadDQoSMgmtGateMediaConnCalledParty_Type()
)
cadDQoSMgmtGateMediaConnCalledParty.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadDQoSMgmtGateMediaConnCalledParty.setStatus("current")


class _CadDQoSMgmtGateMediaConnRoutingNum_Type(DisplayString):
    """Custom type cadDQoSMgmtGateMediaConnRoutingNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CadDQoSMgmtGateMediaConnRoutingNum_Type.__name__ = "DisplayString"
_CadDQoSMgmtGateMediaConnRoutingNum_Object = MibTableColumn
cadDQoSMgmtGateMediaConnRoutingNum = _CadDQoSMgmtGateMediaConnRoutingNum_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 2, 1, 1, 2, 1, 16),
    _CadDQoSMgmtGateMediaConnRoutingNum_Type()
)
cadDQoSMgmtGateMediaConnRoutingNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadDQoSMgmtGateMediaConnRoutingNum.setStatus("current")


class _CadDQoSMgmtGateMediaConnChargeNum_Type(DisplayString):
    """Custom type cadDQoSMgmtGateMediaConnChargeNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CadDQoSMgmtGateMediaConnChargeNum_Type.__name__ = "DisplayString"
_CadDQoSMgmtGateMediaConnChargeNum_Object = MibTableColumn
cadDQoSMgmtGateMediaConnChargeNum = _CadDQoSMgmtGateMediaConnChargeNum_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 2, 1, 1, 2, 1, 17),
    _CadDQoSMgmtGateMediaConnChargeNum_Type()
)
cadDQoSMgmtGateMediaConnChargeNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadDQoSMgmtGateMediaConnChargeNum.setStatus("current")


class _CadDQoSMgmtGateMediaConnLocRouteNum_Type(DisplayString):
    """Custom type cadDQoSMgmtGateMediaConnLocRouteNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CadDQoSMgmtGateMediaConnLocRouteNum_Type.__name__ = "DisplayString"
_CadDQoSMgmtGateMediaConnLocRouteNum_Object = MibTableColumn
cadDQoSMgmtGateMediaConnLocRouteNum = _CadDQoSMgmtGateMediaConnLocRouteNum_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 2, 1, 1, 2, 1, 18),
    _CadDQoSMgmtGateMediaConnLocRouteNum_Type()
)
cadDQoSMgmtGateMediaConnLocRouteNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadDQoSMgmtGateMediaConnLocRouteNum.setStatus("current")
_CadDQoSMgmtGateESPDfCDCIP_Type = InetAddressIPv4or6
_CadDQoSMgmtGateESPDfCDCIP_Object = MibTableColumn
cadDQoSMgmtGateESPDfCDCIP = _CadDQoSMgmtGateESPDfCDCIP_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 2, 1, 1, 2, 1, 19),
    _CadDQoSMgmtGateESPDfCDCIP_Type()
)
cadDQoSMgmtGateESPDfCDCIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadDQoSMgmtGateESPDfCDCIP.setStatus("current")
_CadDQoSMgmtGateESPDfCDCPort_Type = Unsigned32
_CadDQoSMgmtGateESPDfCDCPort_Object = MibTableColumn
cadDQoSMgmtGateESPDfCDCPort = _CadDQoSMgmtGateESPDfCDCPort_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 2, 1, 1, 2, 1, 20),
    _CadDQoSMgmtGateESPDfCDCPort_Type()
)
cadDQoSMgmtGateESPDfCDCPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadDQoSMgmtGateESPDfCDCPort.setStatus("current")
_CadDQoSMgmtGateESPDupEvent_Type = TruthValue
_CadDQoSMgmtGateESPDupEvent_Object = MibTableColumn
cadDQoSMgmtGateESPDupEvent = _CadDQoSMgmtGateESPDupEvent_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 2, 1, 1, 2, 1, 21),
    _CadDQoSMgmtGateESPDupEvent_Type()
)
cadDQoSMgmtGateESPDupEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadDQoSMgmtGateESPDupEvent.setStatus("current")
_CadDQoSMgmtGateSDPStrings_Type = SDPString
_CadDQoSMgmtGateSDPStrings_Object = MibTableColumn
cadDQoSMgmtGateSDPStrings = _CadDQoSMgmtGateSDPStrings_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 2, 1, 1, 2, 1, 25),
    _CadDQoSMgmtGateSDPStrings_Type()
)
cadDQoSMgmtGateSDPStrings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadDQoSMgmtGateSDPStrings.setStatus("current")


class _CadDQoSMgmtGateState_Type(Integer32):
    """Custom type cadDQoSMgmtGateState based on Integer32"""
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
        *(("allocated", 1),
          ("authorized", 2),
          ("committed", 6),
          ("localCommitted", 5),
          ("remoteCommitted", 4),
          ("reserved", 3))
    )


_CadDQoSMgmtGateState_Type.__name__ = "Integer32"
_CadDQoSMgmtGateState_Object = MibTableColumn
cadDQoSMgmtGateState = _CadDQoSMgmtGateState_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 2, 1, 1, 2, 1, 26),
    _CadDQoSMgmtGateState_Type()
)
cadDQoSMgmtGateState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadDQoSMgmtGateState.setStatus("current")
_CadDQoSMgmtGateSource_Type = CadDQoSSource
_CadDQoSMgmtGateSource_Object = MibTableColumn
cadDQoSMgmtGateSource = _CadDQoSMgmtGateSource_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 2, 1, 1, 2, 1, 27),
    _CadDQoSMgmtGateSource_Type()
)
cadDQoSMgmtGateSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadDQoSMgmtGateSource.setStatus("current")
_CadDQoSAuthFlowSpecTable_Object = MibTable
cadDQoSAuthFlowSpecTable = _CadDQoSAuthFlowSpecTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 2, 1, 1, 3)
)
if mibBuilder.loadTexts:
    cadDQoSAuthFlowSpecTable.setStatus("current")
_CadDQoSAuthFlowSpecEntry_Object = MibTableRow
cadDQoSAuthFlowSpecEntry = _CadDQoSAuthFlowSpecEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 2, 1, 1, 3, 1)
)
cadDQoSAuthFlowSpecEntry.setIndexNames(
    (0, "DOCS-QOS3-MIB", "docsQosIfDirection"),
    (0, "CADANT-DQOS-GATE-MIB", "cadDQoSGateId"),
    (0, "CADANT-DQOS-GATE-MIB", "cadDQoSAuthFlowSpecIdx"),
)
if mibBuilder.loadTexts:
    cadDQoSAuthFlowSpecEntry.setStatus("current")
_CadDQoSAuthFlowSpecIdx_Type = Unsigned32
_CadDQoSAuthFlowSpecIdx_Object = MibTableColumn
cadDQoSAuthFlowSpecIdx = _CadDQoSAuthFlowSpecIdx_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 2, 1, 1, 3, 1, 1),
    _CadDQoSAuthFlowSpecIdx_Type()
)
cadDQoSAuthFlowSpecIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadDQoSAuthFlowSpecIdx.setStatus("current")
_CadDQoSAuthFlowSpecBucketDepthb_Type = Unsigned32
_CadDQoSAuthFlowSpecBucketDepthb_Object = MibTableColumn
cadDQoSAuthFlowSpecBucketDepthb = _CadDQoSAuthFlowSpecBucketDepthb_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 2, 1, 1, 3, 1, 2),
    _CadDQoSAuthFlowSpecBucketDepthb_Type()
)
cadDQoSAuthFlowSpecBucketDepthb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadDQoSAuthFlowSpecBucketDepthb.setStatus("current")
if mibBuilder.loadTexts:
    cadDQoSAuthFlowSpecBucketDepthb.setUnits("octets")
_CadDQoSAuthFlowSpecBucketRater_Type = Unsigned32
_CadDQoSAuthFlowSpecBucketRater_Object = MibTableColumn
cadDQoSAuthFlowSpecBucketRater = _CadDQoSAuthFlowSpecBucketRater_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 2, 1, 1, 3, 1, 3),
    _CadDQoSAuthFlowSpecBucketRater_Type()
)
cadDQoSAuthFlowSpecBucketRater.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadDQoSAuthFlowSpecBucketRater.setStatus("current")
if mibBuilder.loadTexts:
    cadDQoSAuthFlowSpecBucketRater.setUnits("bits per second")
_CadDQoSAuthFlowSpecPeakRatep_Type = Unsigned32
_CadDQoSAuthFlowSpecPeakRatep_Object = MibTableColumn
cadDQoSAuthFlowSpecPeakRatep = _CadDQoSAuthFlowSpecPeakRatep_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 2, 1, 1, 3, 1, 4),
    _CadDQoSAuthFlowSpecPeakRatep_Type()
)
cadDQoSAuthFlowSpecPeakRatep.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadDQoSAuthFlowSpecPeakRatep.setStatus("current")
if mibBuilder.loadTexts:
    cadDQoSAuthFlowSpecPeakRatep.setUnits("bits per second")
_CadDQoSAuthFlowSpecMinPolicedUnitm_Type = Unsigned32
_CadDQoSAuthFlowSpecMinPolicedUnitm_Object = MibTableColumn
cadDQoSAuthFlowSpecMinPolicedUnitm = _CadDQoSAuthFlowSpecMinPolicedUnitm_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 2, 1, 1, 3, 1, 5),
    _CadDQoSAuthFlowSpecMinPolicedUnitm_Type()
)
cadDQoSAuthFlowSpecMinPolicedUnitm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadDQoSAuthFlowSpecMinPolicedUnitm.setStatus("current")
if mibBuilder.loadTexts:
    cadDQoSAuthFlowSpecMinPolicedUnitm.setUnits("octets")
_CadDQoSAuthFlowSpecMaxPktSizeM_Type = Unsigned32
_CadDQoSAuthFlowSpecMaxPktSizeM_Object = MibTableColumn
cadDQoSAuthFlowSpecMaxPktSizeM = _CadDQoSAuthFlowSpecMaxPktSizeM_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 2, 1, 1, 3, 1, 6),
    _CadDQoSAuthFlowSpecMaxPktSizeM_Type()
)
cadDQoSAuthFlowSpecMaxPktSizeM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadDQoSAuthFlowSpecMaxPktSizeM.setStatus("current")
if mibBuilder.loadTexts:
    cadDQoSAuthFlowSpecMaxPktSizeM.setUnits("octets")
_CadDQoSAuthFlowSpecReservedRateR_Type = Unsigned32
_CadDQoSAuthFlowSpecReservedRateR_Object = MibTableColumn
cadDQoSAuthFlowSpecReservedRateR = _CadDQoSAuthFlowSpecReservedRateR_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 2, 1, 1, 3, 1, 7),
    _CadDQoSAuthFlowSpecReservedRateR_Type()
)
cadDQoSAuthFlowSpecReservedRateR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadDQoSAuthFlowSpecReservedRateR.setStatus("current")
if mibBuilder.loadTexts:
    cadDQoSAuthFlowSpecReservedRateR.setUnits("bits per second")
_CadDQoSAuthFlowSpecSlackTermS_Type = Unsigned32
_CadDQoSAuthFlowSpecSlackTermS_Object = MibTableColumn
cadDQoSAuthFlowSpecSlackTermS = _CadDQoSAuthFlowSpecSlackTermS_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 2, 1, 1, 3, 1, 8),
    _CadDQoSAuthFlowSpecSlackTermS_Type()
)
cadDQoSAuthFlowSpecSlackTermS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadDQoSAuthFlowSpecSlackTermS.setStatus("current")
if mibBuilder.loadTexts:
    cadDQoSAuthFlowSpecSlackTermS.setUnits("microseconds")
_CadDQoSAuthFlowSpecSubscriberID_Type = InetAddressIPv4or6
_CadDQoSAuthFlowSpecSubscriberID_Object = MibTableColumn
cadDQoSAuthFlowSpecSubscriberID = _CadDQoSAuthFlowSpecSubscriberID_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 2, 1, 1, 3, 1, 9),
    _CadDQoSAuthFlowSpecSubscriberID_Type()
)
cadDQoSAuthFlowSpecSubscriberID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadDQoSAuthFlowSpecSubscriberID.setStatus("current")


class _CadDQoSTimerT0_Type(Unsigned32):
    """Custom type cadDQoSTimerT0 based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_CadDQoSTimerT0_Type.__name__ = "Unsigned32"
_CadDQoSTimerT0_Object = MibScalar
cadDQoSTimerT0 = _CadDQoSTimerT0_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 2, 1, 1, 4),
    _CadDQoSTimerT0_Type()
)
cadDQoSTimerT0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadDQoSTimerT0.setStatus("current")
if mibBuilder.loadTexts:
    cadDQoSTimerT0.setUnits("seconds")


class _CadDQoSTimerT1_Type(Unsigned32):
    """Custom type cadDQoSTimerT1 based on Unsigned32"""
    defaultValue = 250

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_CadDQoSTimerT1_Type.__name__ = "Unsigned32"
_CadDQoSTimerT1_Object = MibScalar
cadDQoSTimerT1 = _CadDQoSTimerT1_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 2, 1, 1, 5),
    _CadDQoSTimerT1_Type()
)
cadDQoSTimerT1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadDQoSTimerT1.setStatus("current")
if mibBuilder.loadTexts:
    cadDQoSTimerT1.setUnits("seconds")


class _CadDQoSTimerT2_Type(Unsigned32):
    """Custom type cadDQoSTimerT2 based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_CadDQoSTimerT2_Type.__name__ = "Unsigned32"
_CadDQoSTimerT2_Object = MibScalar
cadDQoSTimerT2 = _CadDQoSTimerT2_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 2, 1, 1, 6),
    _CadDQoSTimerT2_Type()
)
cadDQoSTimerT2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadDQoSTimerT2.setStatus("current")
if mibBuilder.loadTexts:
    cadDQoSTimerT2.setUnits("seconds")


class _CadDQoSTimerT3_Type(Unsigned32):
    """Custom type cadDQoSTimerT3 based on Unsigned32"""
    defaultValue = 40

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 50),
    )


_CadDQoSTimerT3_Type.__name__ = "Unsigned32"
_CadDQoSTimerT3_Object = MibScalar
cadDQoSTimerT3 = _CadDQoSTimerT3_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 2, 1, 1, 7),
    _CadDQoSTimerT3_Type()
)
cadDQoSTimerT3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadDQoSTimerT3.setStatus("current")
if mibBuilder.loadTexts:
    cadDQoSTimerT3.setUnits("tenths of a second")


class _CadDQoSTimerT4_Type(Unsigned32):
    """Custom type cadDQoSTimerT4 based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_CadDQoSTimerT4_Type.__name__ = "Unsigned32"
_CadDQoSTimerT4_Object = MibScalar
cadDQoSTimerT4 = _CadDQoSTimerT4_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 2, 1, 1, 8),
    _CadDQoSTimerT4_Type()
)
cadDQoSTimerT4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadDQoSTimerT4.setStatus("current")
if mibBuilder.loadTexts:
    cadDQoSTimerT4.setUnits("tenths of a second")


class _CadDQoSTimerT5_Type(Unsigned32):
    """Custom type cadDQoSTimerT5 based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_CadDQoSTimerT5_Type.__name__ = "Unsigned32"
_CadDQoSTimerT5_Object = MibScalar
cadDQoSTimerT5 = _CadDQoSTimerT5_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 2, 1, 1, 9),
    _CadDQoSTimerT5_Type()
)
cadDQoSTimerT5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadDQoSTimerT5.setStatus("current")
if mibBuilder.loadTexts:
    cadDQoSTimerT5.setUnits("tenths of a second")


class _CadDQoSTimerT6_Type(Unsigned32):
    """Custom type cadDQoSTimerT6 based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_CadDQoSTimerT6_Type.__name__ = "Unsigned32"
_CadDQoSTimerT6_Object = MibScalar
cadDQoSTimerT6 = _CadDQoSTimerT6_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 2, 1, 1, 10),
    _CadDQoSTimerT6_Type()
)
cadDQoSTimerT6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadDQoSTimerT6.setStatus("current")
if mibBuilder.loadTexts:
    cadDQoSTimerT6.setUnits("tenths of a second")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CADANT-DQOS-GATE-MIB",
    **{"CadDQoSSource": CadDQoSSource,
       "PCReasonCode": PCReasonCode,
       "SDPString": SDPString,
       "cadDQoSMib": cadDQoSMib,
       "cadDQoSMibObjects": cadDQoSMibObjects,
       "cadDQoSConfigBase": cadDQoSConfigBase,
       "cadDQoSGateTable": cadDQoSGateTable,
       "cadDQoSGateEntry": cadDQoSGateEntry,
       "cadDQoSGateId": cadDQoSGateId,
       "cadDQoSGateSubscriberID": cadDQoSGateSubscriberID,
       "cadDQoSGateClassifierProtoID": cadDQoSGateClassifierProtoID,
       "cadDQoSGateClassifierSrcIP": cadDQoSGateClassifierSrcIP,
       "cadDQoSGateClassifierDestIP": cadDQoSGateClassifierDestIP,
       "cadDQoSGateClassifierSrcPort": cadDQoSGateClassifierSrcPort,
       "cadDQoSGateClassifierDestPort": cadDQoSGateClassifierDestPort,
       "cadDQoSMgmtGateCommitNotAllowed": cadDQoSMgmtGateCommitNotAllowed,
       "cadDQoSGateAutoCommit": cadDQoSGateAutoCommit,
       "cadDQoSGateResourceID": cadDQoSGateResourceID,
       "cadDQoSGateSessionClass": cadDQoSGateSessionClass,
       "cadDQoSGateDSField": cadDQoSGateDSField,
       "cadDQoSGateTimerT7": cadDQoSGateTimerT7,
       "cadDQoSGateTimerT8": cadDQoSGateTimerT8,
       "cadDQoSGateReserveRequest": cadDQoSGateReserveRequest,
       "cadDQoSGateCommited": cadDQoSGateCommited,
       "cadDQoSTearFlows": cadDQoSTearFlows,
       "cadDQoSGateESPDupContent": cadDQoSGateESPDupContent,
       "cadDQoSGateESPDfCCCIp": cadDQoSGateESPDfCCCIp,
       "cadDQoSGateESPDfCCCPort": cadDQoSGateESPDfCCCPort,
       "cadDQoSSFID": cadDQoSSFID,
       "cadDQoSGateESPCCCId": cadDQoSGateESPCCCId,
       "cadDQoSGateESPSrcCCCIp": cadDQoSGateESPSrcCCCIp,
       "cadDQoSGateServiceClassName": cadDQoSGateServiceClassName,
       "cadDQoSGateUsSFSchedType": cadDQoSGateUsSFSchedType,
       "cadDQoSGateUsNomGrantInterval": cadDQoSGateUsNomGrantInterval,
       "cadDQoSGateUsTolGrantJitter": cadDQoSGateUsTolGrantJitter,
       "cadDQoSGateUsGrantsPerInterval": cadDQoSGateUsGrantsPerInterval,
       "cadDQoSGateUsUnsolitedGrantSize": cadDQoSGateUsUnsolitedGrantSize,
       "cadDQoSGateUsReqTransPolicy": cadDQoSGateUsReqTransPolicy,
       "cadDQoSGateUsNomPollingInterval": cadDQoSGateUsNomPollingInterval,
       "cadDQoSGateUsTolPollJitter": cadDQoSGateUsTolPollJitter,
       "cadDQoSGateUsIpToSOverride": cadDQoSGateUsIpToSOverride,
       "cadDQoSGateUsMaxConcatBurst": cadDQoSGateUsMaxConcatBurst,
       "cadDQoSGateDsTrafficPriority": cadDQoSGateDsTrafficPriority,
       "cadDQoSGateDsMaxSustainedRate": cadDQoSGateDsMaxSustainedRate,
       "cadDQoSGateDsMaxTrafBurst": cadDQoSGateDsMaxTrafBurst,
       "cadDQoSGateDsMinReservedTrafRate": cadDQoSGateDsMinReservedTrafRate,
       "cadDQoSGateDsMinPacketSize": cadDQoSGateDsMinPacketSize,
       "cadDQoSGateDsMaxLatency": cadDQoSGateDsMaxLatency,
       "cadDQoSMgmtGateTable": cadDQoSMgmtGateTable,
       "cadDQoSMgmtGateEntry": cadDQoSMgmtGateEntry,
       "cadDQoSMgmtGateControllerIP": cadDQoSMgmtGateControllerIP,
       "cadDQoSMgmtGateRemoteGateIP": cadDQoSMgmtGateRemoteGateIP,
       "cadDQoSMgmtGateRemoteGatePort": cadDQoSMgmtGateRemoteGatePort,
       "cadDQoSMgmtGateRemoteGateNoRequireGateOpen": cadDQoSMgmtGateRemoteGateNoRequireGateOpen,
       "cadDQoSMgmtGateRemoteGateNoSendGateOpen": cadDQoSMgmtGateRemoteGateNoSendGateOpen,
       "cadDQoSMgmtGateRemoteGateID": cadDQoSMgmtGateRemoteGateID,
       "cadDQoSMgmtGateRemoteGateAlgorithm": cadDQoSMgmtGateRemoteGateAlgorithm,
       "cadDQoSMgmtGateRemoteGateSecurityKey": cadDQoSMgmtGateRemoteGateSecurityKey,
       "cadDQoSMgmtGateEventGenPriRKSIP": cadDQoSMgmtGateEventGenPriRKSIP,
       "cadDQoSMgmtGateEventGenPriRKSPort": cadDQoSMgmtGateEventGenPriRKSPort,
       "cadDQoSMgmtGateEventGenBatchIndicator": cadDQoSMgmtGateEventGenBatchIndicator,
       "cadDQoSMgmtGateEventGenSecRKSIP": cadDQoSMgmtGateEventGenSecRKSIP,
       "cadDQoSMgmtGateEventGenSecRKSPort": cadDQoSMgmtGateEventGenSecRKSPort,
       "cadDQoSMgmtGateEventGenBillCorrID": cadDQoSMgmtGateEventGenBillCorrID,
       "cadDQoSMgmtGateMediaConnCalledParty": cadDQoSMgmtGateMediaConnCalledParty,
       "cadDQoSMgmtGateMediaConnRoutingNum": cadDQoSMgmtGateMediaConnRoutingNum,
       "cadDQoSMgmtGateMediaConnChargeNum": cadDQoSMgmtGateMediaConnChargeNum,
       "cadDQoSMgmtGateMediaConnLocRouteNum": cadDQoSMgmtGateMediaConnLocRouteNum,
       "cadDQoSMgmtGateESPDfCDCIP": cadDQoSMgmtGateESPDfCDCIP,
       "cadDQoSMgmtGateESPDfCDCPort": cadDQoSMgmtGateESPDfCDCPort,
       "cadDQoSMgmtGateESPDupEvent": cadDQoSMgmtGateESPDupEvent,
       "cadDQoSMgmtGateSDPStrings": cadDQoSMgmtGateSDPStrings,
       "cadDQoSMgmtGateState": cadDQoSMgmtGateState,
       "cadDQoSMgmtGateSource": cadDQoSMgmtGateSource,
       "cadDQoSAuthFlowSpecTable": cadDQoSAuthFlowSpecTable,
       "cadDQoSAuthFlowSpecEntry": cadDQoSAuthFlowSpecEntry,
       "cadDQoSAuthFlowSpecIdx": cadDQoSAuthFlowSpecIdx,
       "cadDQoSAuthFlowSpecBucketDepthb": cadDQoSAuthFlowSpecBucketDepthb,
       "cadDQoSAuthFlowSpecBucketRater": cadDQoSAuthFlowSpecBucketRater,
       "cadDQoSAuthFlowSpecPeakRatep": cadDQoSAuthFlowSpecPeakRatep,
       "cadDQoSAuthFlowSpecMinPolicedUnitm": cadDQoSAuthFlowSpecMinPolicedUnitm,
       "cadDQoSAuthFlowSpecMaxPktSizeM": cadDQoSAuthFlowSpecMaxPktSizeM,
       "cadDQoSAuthFlowSpecReservedRateR": cadDQoSAuthFlowSpecReservedRateR,
       "cadDQoSAuthFlowSpecSlackTermS": cadDQoSAuthFlowSpecSlackTermS,
       "cadDQoSAuthFlowSpecSubscriberID": cadDQoSAuthFlowSpecSubscriberID,
       "cadDQoSTimerT0": cadDQoSTimerT0,
       "cadDQoSTimerT1": cadDQoSTimerT1,
       "cadDQoSTimerT2": cadDQoSTimerT2,
       "cadDQoSTimerT3": cadDQoSTimerT3,
       "cadDQoSTimerT4": cadDQoSTimerT4,
       "cadDQoSTimerT5": cadDQoSTimerT5,
       "cadDQoSTimerT6": cadDQoSTimerT6}
)
