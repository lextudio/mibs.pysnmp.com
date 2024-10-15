# SNMP MIB module (CISCO-GGSN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-GGSN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:00:50 2024
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

(cGtpPathAddress,
 cGtpPathAddressType,
 cGtpPathPort) = mibBuilder.importSymbols(
    "CISCO-GTP-MIB",
    "cGtpPathAddress",
    "cGtpPathAddressType",
    "cGtpPathPort")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(CiscoAlarmSeverity,
 CiscoInetAddressMask) = mibBuilder.importSymbols(
    "CISCO-TC",
    "CiscoAlarmSeverity",
    "CiscoInetAddressMask")

(InterfaceIndexOrZero,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero",
    "ifIndex")

(InetAddress,
 InetAddressDNS,
 InetAddressPrefixLength,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressDNS",
    "InetAddressPrefixLength",
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

cGgsnMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 240)
)
cGgsnMIB.setRevisions(
        ("2012-05-04 00:00",
         "2012-01-11 00:00",
         "2011-03-21 00:00",
         "2011-03-01 00:00",
         "2010-03-23 00:00",
         "2010-02-19 00:00",
         "2008-11-03 00:00",
         "2008-02-04 00:00",
         "2006-10-05 00:00",
         "2006-03-30 09:00",
         "2005-08-24 18:00",
         "2005-01-04 18:00",
         "2004-11-23 01:00",
         "2004-02-23 01:00",
         "2003-12-31 01:00",
         "2001-12-08 15:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CGgsnMIBObjects_ObjectIdentity = ObjectIdentity
cGgsnMIBObjects = _CGgsnMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1)
)
_CGgsnStatistics_ObjectIdentity = ObjectIdentity
cGgsnStatistics = _CGgsnStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 1)
)
_CGgsnSentSigMessages_Type = Counter32
_CGgsnSentSigMessages_Object = MibScalar
cGgsnSentSigMessages = _CGgsnSentSigMessages_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 1, 1),
    _CGgsnSentSigMessages_Type()
)
cGgsnSentSigMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnSentSigMessages.setStatus("current")
if mibBuilder.loadTexts:
    cGgsnSentSigMessages.setUnits("packets")
_CGgsnReceivedSigMessages_Type = Counter32
_CGgsnReceivedSigMessages_Object = MibScalar
cGgsnReceivedSigMessages = _CGgsnReceivedSigMessages_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 1, 2),
    _CGgsnReceivedSigMessages_Type()
)
cGgsnReceivedSigMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnReceivedSigMessages.setStatus("current")
if mibBuilder.loadTexts:
    cGgsnReceivedSigMessages.setUnits("packets")
_CGgsnUnexpectedSigMessages_Type = Counter32
_CGgsnUnexpectedSigMessages_Object = MibScalar
cGgsnUnexpectedSigMessages = _CGgsnUnexpectedSigMessages_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 1, 3),
    _CGgsnUnexpectedSigMessages_Type()
)
cGgsnUnexpectedSigMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnUnexpectedSigMessages.setStatus("current")
if mibBuilder.loadTexts:
    cGgsnUnexpectedSigMessages.setUnits("packets")
_CGgsnSentGPDUs_Type = Counter32
_CGgsnSentGPDUs_Object = MibScalar
cGgsnSentGPDUs = _CGgsnSentGPDUs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 1, 4),
    _CGgsnSentGPDUs_Type()
)
cGgsnSentGPDUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnSentGPDUs.setStatus("current")
if mibBuilder.loadTexts:
    cGgsnSentGPDUs.setUnits("packets")
_CGgsnReceivedGPDUs_Type = Counter32
_CGgsnReceivedGPDUs_Object = MibScalar
cGgsnReceivedGPDUs = _CGgsnReceivedGPDUs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 1, 5),
    _CGgsnReceivedGPDUs_Type()
)
cGgsnReceivedGPDUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnReceivedGPDUs.setStatus("current")
if mibBuilder.loadTexts:
    cGgsnReceivedGPDUs.setUnits("packets")
_CGgsnSentGPDUOctets_Type = Counter32
_CGgsnSentGPDUOctets_Object = MibScalar
cGgsnSentGPDUOctets = _CGgsnSentGPDUOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 1, 6),
    _CGgsnSentGPDUOctets_Type()
)
cGgsnSentGPDUOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnSentGPDUOctets.setStatus("deprecated")
if mibBuilder.loadTexts:
    cGgsnSentGPDUOctets.setUnits("bytes")
_CGgsnReceivedGPDUOctets_Type = Counter32
_CGgsnReceivedGPDUOctets_Object = MibScalar
cGgsnReceivedGPDUOctets = _CGgsnReceivedGPDUOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 1, 7),
    _CGgsnReceivedGPDUOctets_Type()
)
cGgsnReceivedGPDUOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnReceivedGPDUOctets.setStatus("deprecated")
if mibBuilder.loadTexts:
    cGgsnReceivedGPDUOctets.setUnits("bytes")
_CGgsnUnexpectedGPDUs_Type = Counter32
_CGgsnUnexpectedGPDUs_Object = MibScalar
cGgsnUnexpectedGPDUs = _CGgsnUnexpectedGPDUs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 1, 8),
    _CGgsnUnexpectedGPDUs_Type()
)
cGgsnUnexpectedGPDUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnUnexpectedGPDUs.setStatus("current")
if mibBuilder.loadTexts:
    cGgsnUnexpectedGPDUs.setUnits("packets")
_CGgsnActivationRejectedPdps_Type = Counter32
_CGgsnActivationRejectedPdps_Object = MibScalar
cGgsnActivationRejectedPdps = _CGgsnActivationRejectedPdps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 1, 9),
    _CGgsnActivationRejectedPdps_Type()
)
cGgsnActivationRejectedPdps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnActivationRejectedPdps.setStatus("current")
if mibBuilder.loadTexts:
    cGgsnActivationRejectedPdps.setUnits("packets")
_CGgsnOutOfResourcePdps_Type = Counter32
_CGgsnOutOfResourcePdps_Object = MibScalar
cGgsnOutOfResourcePdps = _CGgsnOutOfResourcePdps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 1, 10),
    _CGgsnOutOfResourcePdps_Type()
)
cGgsnOutOfResourcePdps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnOutOfResourcePdps.setStatus("current")
if mibBuilder.loadTexts:
    cGgsnOutOfResourcePdps.setUnits("packets")
_CGgsnParserErrorMessages_Type = Counter32
_CGgsnParserErrorMessages_Object = MibScalar
cGgsnParserErrorMessages = _CGgsnParserErrorMessages_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 1, 11),
    _CGgsnParserErrorMessages_Type()
)
cGgsnParserErrorMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnParserErrorMessages.setStatus("current")
if mibBuilder.loadTexts:
    cGgsnParserErrorMessages.setUnits("packets")
_CGgsnTotalCreatedPdps_Type = Counter32
_CGgsnTotalCreatedPdps_Object = MibScalar
cGgsnTotalCreatedPdps = _CGgsnTotalCreatedPdps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 1, 12),
    _CGgsnTotalCreatedPdps_Type()
)
cGgsnTotalCreatedPdps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnTotalCreatedPdps.setStatus("current")
if mibBuilder.loadTexts:
    cGgsnTotalCreatedPdps.setUnits("packets")
_CGgsnTotalDeletedPdps_Type = Counter32
_CGgsnTotalDeletedPdps_Object = MibScalar
cGgsnTotalDeletedPdps = _CGgsnTotalDeletedPdps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 1, 13),
    _CGgsnTotalDeletedPdps_Type()
)
cGgsnTotalDeletedPdps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnTotalDeletedPdps.setStatus("current")
if mibBuilder.loadTexts:
    cGgsnTotalDeletedPdps.setUnits("packets")
_CGgsnTotalNetworkInitPdps_Type = Counter32
_CGgsnTotalNetworkInitPdps_Object = MibScalar
cGgsnTotalNetworkInitPdps = _CGgsnTotalNetworkInitPdps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 1, 14),
    _CGgsnTotalNetworkInitPdps_Type()
)
cGgsnTotalNetworkInitPdps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnTotalNetworkInitPdps.setStatus("current")
if mibBuilder.loadTexts:
    cGgsnTotalNetworkInitPdps.setUnits("packets")
_CGgsnTotalPppPdpsCreated_Type = Counter32
_CGgsnTotalPppPdpsCreated_Object = MibScalar
cGgsnTotalPppPdpsCreated = _CGgsnTotalPppPdpsCreated_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 1, 15),
    _CGgsnTotalPppPdpsCreated_Type()
)
cGgsnTotalPppPdpsCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnTotalPppPdpsCreated.setStatus("current")
if mibBuilder.loadTexts:
    cGgsnTotalPppPdpsCreated.setUnits("packets")
_CGgsnTotalPppPdpsDeleted_Type = Counter32
_CGgsnTotalPppPdpsDeleted_Object = MibScalar
cGgsnTotalPppPdpsDeleted = _CGgsnTotalPppPdpsDeleted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 1, 16),
    _CGgsnTotalPppPdpsDeleted_Type()
)
cGgsnTotalPppPdpsDeleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnTotalPppPdpsDeleted.setStatus("current")
if mibBuilder.loadTexts:
    cGgsnTotalPppPdpsDeleted.setUnits("packets")
_CGgsnOutOfResourcePppRegenPdps_Type = Counter32
_CGgsnOutOfResourcePppRegenPdps_Object = MibScalar
cGgsnOutOfResourcePppRegenPdps = _CGgsnOutOfResourcePppRegenPdps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 1, 17),
    _CGgsnOutOfResourcePppRegenPdps_Type()
)
cGgsnOutOfResourcePppRegenPdps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnOutOfResourcePppRegenPdps.setStatus("current")
if mibBuilder.loadTexts:
    cGgsnOutOfResourcePppRegenPdps.setUnits("packets")
_CGgsnDroppedPppRegenPdps_Type = Counter32
_CGgsnDroppedPppRegenPdps_Object = MibScalar
cGgsnDroppedPppRegenPdps = _CGgsnDroppedPppRegenPdps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 1, 18),
    _CGgsnDroppedPppRegenPdps_Type()
)
cGgsnDroppedPppRegenPdps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnDroppedPppRegenPdps.setStatus("current")
if mibBuilder.loadTexts:
    cGgsnDroppedPppRegenPdps.setUnits("packets")
_CGgsnTftSemanticErrorPdps_Type = Counter32
_CGgsnTftSemanticErrorPdps_Object = MibScalar
cGgsnTftSemanticErrorPdps = _CGgsnTftSemanticErrorPdps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 1, 19),
    _CGgsnTftSemanticErrorPdps_Type()
)
cGgsnTftSemanticErrorPdps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnTftSemanticErrorPdps.setStatus("current")
_CGgsnTftSyntacticErrorPdps_Type = Counter32
_CGgsnTftSyntacticErrorPdps_Object = MibScalar
cGgsnTftSyntacticErrorPdps = _CGgsnTftSyntacticErrorPdps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 1, 20),
    _CGgsnTftSyntacticErrorPdps_Type()
)
cGgsnTftSyntacticErrorPdps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnTftSyntacticErrorPdps.setStatus("current")
_CGgsnPktFilterSemanticErrorPdps_Type = Counter32
_CGgsnPktFilterSemanticErrorPdps_Object = MibScalar
cGgsnPktFilterSemanticErrorPdps = _CGgsnPktFilterSemanticErrorPdps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 1, 21),
    _CGgsnPktFilterSemanticErrorPdps_Type()
)
cGgsnPktFilterSemanticErrorPdps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnPktFilterSemanticErrorPdps.setStatus("current")
_CGgsnPktFilterSyntacticErrorPdps_Type = Counter32
_CGgsnPktFilterSyntacticErrorPdps_Object = MibScalar
cGgsnPktFilterSyntacticErrorPdps = _CGgsnPktFilterSyntacticErrorPdps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 1, 22),
    _CGgsnPktFilterSyntacticErrorPdps_Type()
)
cGgsnPktFilterSyntacticErrorPdps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnPktFilterSyntacticErrorPdps.setStatus("current")
_CGgsnHCSentGPDUOctets_Type = Counter64
_CGgsnHCSentGPDUOctets_Object = MibScalar
cGgsnHCSentGPDUOctets = _CGgsnHCSentGPDUOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 1, 23),
    _CGgsnHCSentGPDUOctets_Type()
)
cGgsnHCSentGPDUOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnHCSentGPDUOctets.setStatus("current")
if mibBuilder.loadTexts:
    cGgsnHCSentGPDUOctets.setUnits("bytes")
_CGgsnHCReceivedGPDUOctets_Type = Counter64
_CGgsnHCReceivedGPDUOctets_Object = MibScalar
cGgsnHCReceivedGPDUOctets = _CGgsnHCReceivedGPDUOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 1, 24),
    _CGgsnHCReceivedGPDUOctets_Type()
)
cGgsnHCReceivedGPDUOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnHCReceivedGPDUOctets.setStatus("current")
if mibBuilder.loadTexts:
    cGgsnHCReceivedGPDUOctets.setUnits("bytes")
_CGgsnPdpsRejStatistics_ObjectIdentity = ObjectIdentity
cGgsnPdpsRejStatistics = _CGgsnPdpsRejStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 1, 25)
)
_CGgsnVersionNotSupportedRejPdps_Type = Counter32
_CGgsnVersionNotSupportedRejPdps_Object = MibScalar
cGgsnVersionNotSupportedRejPdps = _CGgsnVersionNotSupportedRejPdps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 1, 25, 1),
    _CGgsnVersionNotSupportedRejPdps_Type()
)
cGgsnVersionNotSupportedRejPdps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnVersionNotSupportedRejPdps.setStatus("deprecated")
if mibBuilder.loadTexts:
    cGgsnVersionNotSupportedRejPdps.setUnits("packets")
_CGgsnUnkownMessageRejPdps_Type = Counter32
_CGgsnUnkownMessageRejPdps_Object = MibScalar
cGgsnUnkownMessageRejPdps = _CGgsnUnkownMessageRejPdps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 1, 25, 2),
    _CGgsnUnkownMessageRejPdps_Type()
)
cGgsnUnkownMessageRejPdps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnUnkownMessageRejPdps.setStatus("deprecated")
if mibBuilder.loadTexts:
    cGgsnUnkownMessageRejPdps.setUnits("packets")
_CGgsnMsgTooShortRejPdps_Type = Counter32
_CGgsnMsgTooShortRejPdps_Object = MibScalar
cGgsnMsgTooShortRejPdps = _CGgsnMsgTooShortRejPdps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 1, 25, 3),
    _CGgsnMsgTooShortRejPdps_Type()
)
cGgsnMsgTooShortRejPdps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnMsgTooShortRejPdps.setStatus("deprecated")
if mibBuilder.loadTexts:
    cGgsnMsgTooShortRejPdps.setUnits("packets")
_CGgsnMandIeMissingRejPdps_Type = Counter32
_CGgsnMandIeMissingRejPdps_Object = MibScalar
cGgsnMandIeMissingRejPdps = _CGgsnMandIeMissingRejPdps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 1, 25, 4),
    _CGgsnMandIeMissingRejPdps_Type()
)
cGgsnMandIeMissingRejPdps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnMandIeMissingRejPdps.setStatus("deprecated")
if mibBuilder.loadTexts:
    cGgsnMandIeMissingRejPdps.setUnits("packets")
_CGgsnMandIeIncorrectRejPdps_Type = Counter32
_CGgsnMandIeIncorrectRejPdps_Object = MibScalar
cGgsnMandIeIncorrectRejPdps = _CGgsnMandIeIncorrectRejPdps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 1, 25, 5),
    _CGgsnMandIeIncorrectRejPdps_Type()
)
cGgsnMandIeIncorrectRejPdps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnMandIeIncorrectRejPdps.setStatus("deprecated")
if mibBuilder.loadTexts:
    cGgsnMandIeIncorrectRejPdps.setUnits("packets")
_CGgsnOptIeInvalidRejPdps_Type = Counter32
_CGgsnOptIeInvalidRejPdps_Object = MibScalar
cGgsnOptIeInvalidRejPdps = _CGgsnOptIeInvalidRejPdps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 1, 25, 6),
    _CGgsnOptIeInvalidRejPdps_Type()
)
cGgsnOptIeInvalidRejPdps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnOptIeInvalidRejPdps.setStatus("deprecated")
if mibBuilder.loadTexts:
    cGgsnOptIeInvalidRejPdps.setUnits("packets")
_CGgsnIeUnknownRejPdps_Type = Counter32
_CGgsnIeUnknownRejPdps_Object = MibScalar
cGgsnIeUnknownRejPdps = _CGgsnIeUnknownRejPdps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 1, 25, 7),
    _CGgsnIeUnknownRejPdps_Type()
)
cGgsnIeUnknownRejPdps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnIeUnknownRejPdps.setStatus("deprecated")
if mibBuilder.loadTexts:
    cGgsnIeUnknownRejPdps.setUnits("packets")
_CGgsnIeOutOfOrderRejPdps_Type = Counter32
_CGgsnIeOutOfOrderRejPdps_Object = MibScalar
cGgsnIeOutOfOrderRejPdps = _CGgsnIeOutOfOrderRejPdps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 1, 25, 8),
    _CGgsnIeOutOfOrderRejPdps_Type()
)
cGgsnIeOutOfOrderRejPdps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnIeOutOfOrderRejPdps.setStatus("deprecated")
if mibBuilder.loadTexts:
    cGgsnIeOutOfOrderRejPdps.setUnits("packets")
_CGgsnIeUnexpectedRejPdps_Type = Counter32
_CGgsnIeUnexpectedRejPdps_Object = MibScalar
cGgsnIeUnexpectedRejPdps = _CGgsnIeUnexpectedRejPdps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 1, 25, 9),
    _CGgsnIeUnexpectedRejPdps_Type()
)
cGgsnIeUnexpectedRejPdps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnIeUnexpectedRejPdps.setStatus("deprecated")
if mibBuilder.loadTexts:
    cGgsnIeUnexpectedRejPdps.setUnits("packets")
_CGgsnIeDuplicatedRejPdps_Type = Counter32
_CGgsnIeDuplicatedRejPdps_Object = MibScalar
cGgsnIeDuplicatedRejPdps = _CGgsnIeDuplicatedRejPdps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 1, 25, 10),
    _CGgsnIeDuplicatedRejPdps_Type()
)
cGgsnIeDuplicatedRejPdps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnIeDuplicatedRejPdps.setStatus("deprecated")
if mibBuilder.loadTexts:
    cGgsnIeDuplicatedRejPdps.setUnits("packets")
_CGgsnOptIeIncorrectRejPdps_Type = Counter32
_CGgsnOptIeIncorrectRejPdps_Object = MibScalar
cGgsnOptIeIncorrectRejPdps = _CGgsnOptIeIncorrectRejPdps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 1, 25, 11),
    _CGgsnOptIeIncorrectRejPdps_Type()
)
cGgsnOptIeIncorrectRejPdps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnOptIeIncorrectRejPdps.setStatus("deprecated")
if mibBuilder.loadTexts:
    cGgsnOptIeIncorrectRejPdps.setUnits("packets")
_CGgsnPdpWithoutTftExistsRejPdps_Type = Counter32
_CGgsnPdpWithoutTftExistsRejPdps_Object = MibScalar
cGgsnPdpWithoutTftExistsRejPdps = _CGgsnPdpWithoutTftExistsRejPdps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 1, 25, 12),
    _CGgsnPdpWithoutTftExistsRejPdps_Type()
)
cGgsnPdpWithoutTftExistsRejPdps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnPdpWithoutTftExistsRejPdps.setStatus("deprecated")
if mibBuilder.loadTexts:
    cGgsnPdpWithoutTftExistsRejPdps.setUnits("packets")
_CGgsnSgsnStatTable_Object = MibTable
cGgsnSgsnStatTable = _CGgsnSgsnStatTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 1, 26)
)
if mibBuilder.loadTexts:
    cGgsnSgsnStatTable.setStatus("current")
_CGgsnSgsnStatEntry_Object = MibTableRow
cGgsnSgsnStatEntry = _CGgsnSgsnStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 1, 26, 1)
)
cGgsnSgsnStatEntry.setIndexNames(
    (0, "CISCO-GTP-MIB", "cGtpPathAddressType"),
    (0, "CISCO-GTP-MIB", "cGtpPathAddress"),
    (0, "CISCO-GTP-MIB", "cGtpPathPort"),
    (0, "CISCO-GGSN-MIB", "cGgsnSgsnThruPutInterval"),
)
if mibBuilder.loadTexts:
    cGgsnSgsnStatEntry.setStatus("current")


class _CGgsnSgsnThruPutInterval_Type(Integer32):
    """Custom type cGgsnSgsnThruPutInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CGgsnSgsnThruPutInterval_Type.__name__ = "Integer32"
_CGgsnSgsnThruPutInterval_Object = MibTableColumn
cGgsnSgsnThruPutInterval = _CGgsnSgsnThruPutInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 1, 26, 1, 1),
    _CGgsnSgsnThruPutInterval_Type()
)
cGgsnSgsnThruPutInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cGgsnSgsnThruPutInterval.setStatus("current")
if mibBuilder.loadTexts:
    cGgsnSgsnThruPutInterval.setUnits("minutes")


class _CGgsnSgsnThruPutLastCollected_Type(Integer32):
    """Custom type cGgsnSgsnThruPutLastCollected based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CGgsnSgsnThruPutLastCollected_Type.__name__ = "Integer32"
_CGgsnSgsnThruPutLastCollected_Object = MibTableColumn
cGgsnSgsnThruPutLastCollected = _CGgsnSgsnThruPutLastCollected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 1, 26, 1, 2),
    _CGgsnSgsnThruPutLastCollected_Type()
)
cGgsnSgsnThruPutLastCollected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnSgsnThruPutLastCollected.setStatus("current")
if mibBuilder.loadTexts:
    cGgsnSgsnThruPutLastCollected.setUnits("minutes")
_CGgsnSgsnUpStreamPktCnt_Type = Gauge32
_CGgsnSgsnUpStreamPktCnt_Object = MibTableColumn
cGgsnSgsnUpStreamPktCnt = _CGgsnSgsnUpStreamPktCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 1, 26, 1, 3),
    _CGgsnSgsnUpStreamPktCnt_Type()
)
cGgsnSgsnUpStreamPktCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnSgsnUpStreamPktCnt.setStatus("current")
if mibBuilder.loadTexts:
    cGgsnSgsnUpStreamPktCnt.setUnits("packets")
_CGgsnSgsnUpStreamByteCnt_Type = Gauge32
_CGgsnSgsnUpStreamByteCnt_Object = MibTableColumn
cGgsnSgsnUpStreamByteCnt = _CGgsnSgsnUpStreamByteCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 1, 26, 1, 4),
    _CGgsnSgsnUpStreamByteCnt_Type()
)
cGgsnSgsnUpStreamByteCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnSgsnUpStreamByteCnt.setStatus("current")
if mibBuilder.loadTexts:
    cGgsnSgsnUpStreamByteCnt.setUnits("bytes")
_CGgsnSgsnDownStreamPktCnt_Type = Gauge32
_CGgsnSgsnDownStreamPktCnt_Object = MibTableColumn
cGgsnSgsnDownStreamPktCnt = _CGgsnSgsnDownStreamPktCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 1, 26, 1, 5),
    _CGgsnSgsnDownStreamPktCnt_Type()
)
cGgsnSgsnDownStreamPktCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnSgsnDownStreamPktCnt.setStatus("current")
if mibBuilder.loadTexts:
    cGgsnSgsnDownStreamPktCnt.setUnits("packets")
_CGgsnSgsnDownStreamByteCnt_Type = Gauge32
_CGgsnSgsnDownStreamByteCnt_Object = MibTableColumn
cGgsnSgsnDownStreamByteCnt = _CGgsnSgsnDownStreamByteCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 1, 26, 1, 6),
    _CGgsnSgsnDownStreamByteCnt_Type()
)
cGgsnSgsnDownStreamByteCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnSgsnDownStreamByteCnt.setStatus("current")
if mibBuilder.loadTexts:
    cGgsnSgsnDownStreamByteCnt.setUnits("bytes")
_CGgsnRedundancyStatistics_ObjectIdentity = ObjectIdentity
cGgsnRedundancyStatistics = _CGgsnRedundancyStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 1, 27)
)
_CGgsnTotalMessages_Type = Counter32
_CGgsnTotalMessages_Object = MibScalar
cGgsnTotalMessages = _CGgsnTotalMessages_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 1, 27, 1),
    _CGgsnTotalMessages_Type()
)
cGgsnTotalMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnTotalMessages.setStatus("current")
_CGgsnContextSetupMessages_Type = Counter32
_CGgsnContextSetupMessages_Object = MibScalar
cGgsnContextSetupMessages = _CGgsnContextSetupMessages_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 1, 27, 2),
    _CGgsnContextSetupMessages_Type()
)
cGgsnContextSetupMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnContextSetupMessages.setStatus("current")
_CGgsnContextModifyMessages_Type = Counter32
_CGgsnContextModifyMessages_Object = MibScalar
cGgsnContextModifyMessages = _CGgsnContextModifyMessages_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 1, 27, 3),
    _CGgsnContextModifyMessages_Type()
)
cGgsnContextModifyMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnContextModifyMessages.setStatus("current")
_CGgsnContextRemoveMessages_Type = Counter32
_CGgsnContextRemoveMessages_Object = MibScalar
cGgsnContextRemoveMessages = _CGgsnContextRemoveMessages_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 1, 27, 4),
    _CGgsnContextRemoveMessages_Type()
)
cGgsnContextRemoveMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnContextRemoveMessages.setStatus("current")
_CGgsnPathSetupMessages_Type = Counter32
_CGgsnPathSetupMessages_Object = MibScalar
cGgsnPathSetupMessages = _CGgsnPathSetupMessages_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 1, 27, 5),
    _CGgsnPathSetupMessages_Type()
)
cGgsnPathSetupMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnPathSetupMessages.setStatus("current")
_CGgsnPathModifyMessages_Type = Counter32
_CGgsnPathModifyMessages_Object = MibScalar
cGgsnPathModifyMessages = _CGgsnPathModifyMessages_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 1, 27, 6),
    _CGgsnPathModifyMessages_Type()
)
cGgsnPathModifyMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnPathModifyMessages.setStatus("current")
_CGgsnPathRemoveMessages_Type = Counter32
_CGgsnPathRemoveMessages_Object = MibScalar
cGgsnPathRemoveMessages = _CGgsnPathRemoveMessages_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 1, 27, 7),
    _CGgsnPathRemoveMessages_Type()
)
cGgsnPathRemoveMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnPathRemoveMessages.setStatus("current")
_CGgsnCGFReadyMessages_Type = Counter32
_CGgsnCGFReadyMessages_Object = MibScalar
cGgsnCGFReadyMessages = _CGgsnCGFReadyMessages_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 1, 27, 8),
    _CGgsnCGFReadyMessages_Type()
)
cGgsnCGFReadyMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnCGFReadyMessages.setStatus("current")
_CGgsnCGFModifyMessages_Type = Counter32
_CGgsnCGFModifyMessages_Object = MibScalar
cGgsnCGFModifyMessages = _CGgsnCGFModifyMessages_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 1, 27, 9),
    _CGgsnCGFModifyMessages_Type()
)
cGgsnCGFModifyMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnCGFModifyMessages.setStatus("current")
_CGgsnCGFRemoveMessages_Type = Counter32
_CGgsnCGFRemoveMessages_Object = MibScalar
cGgsnCGFRemoveMessages = _CGgsnCGFRemoveMessages_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 1, 27, 10),
    _CGgsnCGFRemoveMessages_Type()
)
cGgsnCGFRemoveMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnCGFRemoveMessages.setStatus("current")
_CGgsnInternalStateMsgs_Type = Counter32
_CGgsnInternalStateMsgs_Object = MibScalar
cGgsnInternalStateMsgs = _CGgsnInternalStateMsgs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 1, 27, 11),
    _CGgsnInternalStateMsgs_Type()
)
cGgsnInternalStateMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnInternalStateMsgs.setStatus("current")
_CGgsnSlbCacFailures_Type = Counter32
_CGgsnSlbCacFailures_Object = MibScalar
cGgsnSlbCacFailures = _CGgsnSlbCacFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 1, 28),
    _CGgsnSlbCacFailures_Type()
)
cGgsnSlbCacFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnSlbCacFailures.setStatus("current")
_CGgsnSlbSessionFailures_Type = Counter32
_CGgsnSlbSessionFailures_Object = MibScalar
cGgsnSlbSessionFailures = _CGgsnSlbSessionFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 1, 29),
    _CGgsnSlbSessionFailures_Type()
)
cGgsnSlbSessionFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnSlbSessionFailures.setStatus("current")
_CGgsnTotalCreatedIpv6Pdps_Type = Counter32
_CGgsnTotalCreatedIpv6Pdps_Object = MibScalar
cGgsnTotalCreatedIpv6Pdps = _CGgsnTotalCreatedIpv6Pdps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 1, 30),
    _CGgsnTotalCreatedIpv6Pdps_Type()
)
cGgsnTotalCreatedIpv6Pdps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnTotalCreatedIpv6Pdps.setStatus("current")
if mibBuilder.loadTexts:
    cGgsnTotalCreatedIpv6Pdps.setUnits("PDPs")
_CGgsnTotalDeletedIpv6Pdps_Type = Counter32
_CGgsnTotalDeletedIpv6Pdps_Object = MibScalar
cGgsnTotalDeletedIpv6Pdps = _CGgsnTotalDeletedIpv6Pdps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 1, 31),
    _CGgsnTotalDeletedIpv6Pdps_Type()
)
cGgsnTotalDeletedIpv6Pdps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnTotalDeletedIpv6Pdps.setStatus("current")
if mibBuilder.loadTexts:
    cGgsnTotalDeletedIpv6Pdps.setUnits("PDPs")
_CGgsnTotalRejectedIpv6Pdps_Type = Counter32
_CGgsnTotalRejectedIpv6Pdps_Object = MibScalar
cGgsnTotalRejectedIpv6Pdps = _CGgsnTotalRejectedIpv6Pdps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 1, 32),
    _CGgsnTotalRejectedIpv6Pdps_Type()
)
cGgsnTotalRejectedIpv6Pdps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnTotalRejectedIpv6Pdps.setStatus("current")
if mibBuilder.loadTexts:
    cGgsnTotalRejectedIpv6Pdps.setUnits("PDPs")
_CGgsnSentIpv6SigMessages_Type = Counter32
_CGgsnSentIpv6SigMessages_Object = MibScalar
cGgsnSentIpv6SigMessages = _CGgsnSentIpv6SigMessages_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 1, 33),
    _CGgsnSentIpv6SigMessages_Type()
)
cGgsnSentIpv6SigMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnSentIpv6SigMessages.setStatus("current")
if mibBuilder.loadTexts:
    cGgsnSentIpv6SigMessages.setUnits("messages")
_CGgsnReceivedIpv6SigMessages_Type = Counter32
_CGgsnReceivedIpv6SigMessages_Object = MibScalar
cGgsnReceivedIpv6SigMessages = _CGgsnReceivedIpv6SigMessages_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 1, 34),
    _CGgsnReceivedIpv6SigMessages_Type()
)
cGgsnReceivedIpv6SigMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnReceivedIpv6SigMessages.setStatus("current")
if mibBuilder.loadTexts:
    cGgsnReceivedIpv6SigMessages.setUnits("messages")
_CGgsnSentIpv6PDUs_Type = Counter32
_CGgsnSentIpv6PDUs_Object = MibScalar
cGgsnSentIpv6PDUs = _CGgsnSentIpv6PDUs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 1, 35),
    _CGgsnSentIpv6PDUs_Type()
)
cGgsnSentIpv6PDUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnSentIpv6PDUs.setStatus("current")
if mibBuilder.loadTexts:
    cGgsnSentIpv6PDUs.setUnits("packets")
_CGgsnReceivedIpv6PDUs_Type = Counter32
_CGgsnReceivedIpv6PDUs_Object = MibScalar
cGgsnReceivedIpv6PDUs = _CGgsnReceivedIpv6PDUs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 1, 36),
    _CGgsnReceivedIpv6PDUs_Type()
)
cGgsnReceivedIpv6PDUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnReceivedIpv6PDUs.setStatus("current")
if mibBuilder.loadTexts:
    cGgsnReceivedIpv6PDUs.setUnits("packets")
_CGgsnSentIpv6PDUOctets_Type = Counter64
_CGgsnSentIpv6PDUOctets_Object = MibScalar
cGgsnSentIpv6PDUOctets = _CGgsnSentIpv6PDUOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 1, 37),
    _CGgsnSentIpv6PDUOctets_Type()
)
cGgsnSentIpv6PDUOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnSentIpv6PDUOctets.setStatus("current")
if mibBuilder.loadTexts:
    cGgsnSentIpv6PDUOctets.setUnits("bytes")
_CGgsnReceivedIpv6PDUOctets_Type = Counter64
_CGgsnReceivedIpv6PDUOctets_Object = MibScalar
cGgsnReceivedIpv6PDUOctets = _CGgsnReceivedIpv6PDUOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 1, 38),
    _CGgsnReceivedIpv6PDUOctets_Type()
)
cGgsnReceivedIpv6PDUOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnReceivedIpv6PDUOctets.setStatus("current")
if mibBuilder.loadTexts:
    cGgsnReceivedIpv6PDUOctets.setUnits("bytes")
_CGgsnVersionNotSupportedMsgs_Type = Counter32
_CGgsnVersionNotSupportedMsgs_Object = MibScalar
cGgsnVersionNotSupportedMsgs = _CGgsnVersionNotSupportedMsgs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 1, 39),
    _CGgsnVersionNotSupportedMsgs_Type()
)
cGgsnVersionNotSupportedMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnVersionNotSupportedMsgs.setStatus("current")
if mibBuilder.loadTexts:
    cGgsnVersionNotSupportedMsgs.setUnits("messages")
_CGgsnUnkownGtpMsgs_Type = Counter32
_CGgsnUnkownGtpMsgs_Object = MibScalar
cGgsnUnkownGtpMsgs = _CGgsnUnkownGtpMsgs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 1, 40),
    _CGgsnUnkownGtpMsgs_Type()
)
cGgsnUnkownGtpMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnUnkownGtpMsgs.setStatus("current")
if mibBuilder.loadTexts:
    cGgsnUnkownGtpMsgs.setUnits("messages")
_CGgsnTooShortMsgs_Type = Counter32
_CGgsnTooShortMsgs_Object = MibScalar
cGgsnTooShortMsgs = _CGgsnTooShortMsgs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 1, 41),
    _CGgsnTooShortMsgs_Type()
)
cGgsnTooShortMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnTooShortMsgs.setStatus("current")
if mibBuilder.loadTexts:
    cGgsnTooShortMsgs.setUnits("messages")
_CGgsnMandIeMissingMsgs_Type = Counter32
_CGgsnMandIeMissingMsgs_Object = MibScalar
cGgsnMandIeMissingMsgs = _CGgsnMandIeMissingMsgs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 1, 42),
    _CGgsnMandIeMissingMsgs_Type()
)
cGgsnMandIeMissingMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnMandIeMissingMsgs.setStatus("current")
if mibBuilder.loadTexts:
    cGgsnMandIeMissingMsgs.setUnits("messages")
_CGgsnMandIeIncorrectMsgs_Type = Counter32
_CGgsnMandIeIncorrectMsgs_Object = MibScalar
cGgsnMandIeIncorrectMsgs = _CGgsnMandIeIncorrectMsgs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 1, 43),
    _CGgsnMandIeIncorrectMsgs_Type()
)
cGgsnMandIeIncorrectMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnMandIeIncorrectMsgs.setStatus("current")
if mibBuilder.loadTexts:
    cGgsnMandIeIncorrectMsgs.setUnits("messages")
_CGgsnOptIeInvalidMsgs_Type = Counter32
_CGgsnOptIeInvalidMsgs_Object = MibScalar
cGgsnOptIeInvalidMsgs = _CGgsnOptIeInvalidMsgs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 1, 44),
    _CGgsnOptIeInvalidMsgs_Type()
)
cGgsnOptIeInvalidMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnOptIeInvalidMsgs.setStatus("current")
if mibBuilder.loadTexts:
    cGgsnOptIeInvalidMsgs.setUnits("messages")
_CGgsnIeUnknownMsgs_Type = Counter32
_CGgsnIeUnknownMsgs_Object = MibScalar
cGgsnIeUnknownMsgs = _CGgsnIeUnknownMsgs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 1, 45),
    _CGgsnIeUnknownMsgs_Type()
)
cGgsnIeUnknownMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnIeUnknownMsgs.setStatus("current")
if mibBuilder.loadTexts:
    cGgsnIeUnknownMsgs.setUnits("messages")
_CGgsnIeOutOfOrderMsgs_Type = Counter32
_CGgsnIeOutOfOrderMsgs_Object = MibScalar
cGgsnIeOutOfOrderMsgs = _CGgsnIeOutOfOrderMsgs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 1, 46),
    _CGgsnIeOutOfOrderMsgs_Type()
)
cGgsnIeOutOfOrderMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnIeOutOfOrderMsgs.setStatus("current")
if mibBuilder.loadTexts:
    cGgsnIeOutOfOrderMsgs.setUnits("messages")
_CGgsnIeUnexpectedMsgs_Type = Counter32
_CGgsnIeUnexpectedMsgs_Object = MibScalar
cGgsnIeUnexpectedMsgs = _CGgsnIeUnexpectedMsgs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 1, 47),
    _CGgsnIeUnexpectedMsgs_Type()
)
cGgsnIeUnexpectedMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnIeUnexpectedMsgs.setStatus("current")
if mibBuilder.loadTexts:
    cGgsnIeUnexpectedMsgs.setUnits("messages")
_CGgsnIeDuplicatedMsgs_Type = Counter32
_CGgsnIeDuplicatedMsgs_Object = MibScalar
cGgsnIeDuplicatedMsgs = _CGgsnIeDuplicatedMsgs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 1, 48),
    _CGgsnIeDuplicatedMsgs_Type()
)
cGgsnIeDuplicatedMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnIeDuplicatedMsgs.setStatus("current")
if mibBuilder.loadTexts:
    cGgsnIeDuplicatedMsgs.setUnits("messages")
_CGgsnOptIeIncorrectMsgs_Type = Counter32
_CGgsnOptIeIncorrectMsgs_Object = MibScalar
cGgsnOptIeIncorrectMsgs = _CGgsnOptIeIncorrectMsgs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 1, 49),
    _CGgsnOptIeIncorrectMsgs_Type()
)
cGgsnOptIeIncorrectMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnOptIeIncorrectMsgs.setStatus("current")
if mibBuilder.loadTexts:
    cGgsnOptIeIncorrectMsgs.setUnits("messages")
_CGgsnPdpWithoutTftExistsPdps_Type = Counter32
_CGgsnPdpWithoutTftExistsPdps_Object = MibScalar
cGgsnPdpWithoutTftExistsPdps = _CGgsnPdpWithoutTftExistsPdps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 1, 50),
    _CGgsnPdpWithoutTftExistsPdps_Type()
)
cGgsnPdpWithoutTftExistsPdps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnPdpWithoutTftExistsPdps.setStatus("current")
if mibBuilder.loadTexts:
    cGgsnPdpWithoutTftExistsPdps.setUnits("packets")
_CGgsnNotifMgmt_ObjectIdentity = ObjectIdentity
cGgsnNotifMgmt = _CGgsnNotifMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 2)
)


class _CGgsnNotifEnabled_Type(TruthValue):
    """Custom type cGgsnNotifEnabled based on TruthValue"""


_CGgsnNotifEnabled_Object = MibScalar
cGgsnNotifEnabled = _CGgsnNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 2, 1),
    _CGgsnNotifEnabled_Type()
)
cGgsnNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cGgsnNotifEnabled.setStatus("deprecated")


class _CGgsnNotifLeastSeverLevel_Type(CiscoAlarmSeverity):
    """Custom type cGgsnNotifLeastSeverLevel based on CiscoAlarmSeverity"""


_CGgsnNotifLeastSeverLevel_Object = MibScalar
cGgsnNotifLeastSeverLevel = _CGgsnNotifLeastSeverLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 2, 2),
    _CGgsnNotifLeastSeverLevel_Type()
)
cGgsnNotifLeastSeverLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cGgsnNotifLeastSeverLevel.setStatus("current")
_CGgsnGeneratedNotifs_Type = Counter32
_CGgsnGeneratedNotifs_Object = MibScalar
cGgsnGeneratedNotifs = _CGgsnGeneratedNotifs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 2, 3),
    _CGgsnGeneratedNotifs_Type()
)
cGgsnGeneratedNotifs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnGeneratedNotifs.setStatus("current")
if mibBuilder.loadTexts:
    cGgsnGeneratedNotifs.setUnits("notifications")
_CGgsnIgnoredAlarms_Type = Counter32
_CGgsnIgnoredAlarms_Object = MibScalar
cGgsnIgnoredAlarms = _CGgsnIgnoredAlarms_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 2, 4),
    _CGgsnIgnoredAlarms_Type()
)
cGgsnIgnoredAlarms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnIgnoredAlarms.setStatus("current")
if mibBuilder.loadTexts:
    cGgsnIgnoredAlarms.setUnits("notifications")


class _CGgsnHistNotifMaxLength_Type(Integer32):
    """Custom type cGgsnHistNotifMaxLength based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CGgsnHistNotifMaxLength_Type.__name__ = "Integer32"
_CGgsnHistNotifMaxLength_Object = MibScalar
cGgsnHistNotifMaxLength = _CGgsnHistNotifMaxLength_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 2, 5),
    _CGgsnHistNotifMaxLength_Type()
)
cGgsnHistNotifMaxLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cGgsnHistNotifMaxLength.setStatus("current")
if mibBuilder.loadTexts:
    cGgsnHistNotifMaxLength.setUnits("entries")


class _CGgsnHistNotifLatestIndex_Type(Unsigned32):
    """Custom type cGgsnHistNotifLatestIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CGgsnHistNotifLatestIndex_Type.__name__ = "Unsigned32"
_CGgsnHistNotifLatestIndex_Object = MibScalar
cGgsnHistNotifLatestIndex = _CGgsnHistNotifLatestIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 2, 6),
    _CGgsnHistNotifLatestIndex_Type()
)
cGgsnHistNotifLatestIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnHistNotifLatestIndex.setStatus("current")
_CGgsnHistNotifTable_Object = MibTable
cGgsnHistNotifTable = _CGgsnHistNotifTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 2, 7)
)
if mibBuilder.loadTexts:
    cGgsnHistNotifTable.setStatus("current")
_CGgsnHistNotifEntry_Object = MibTableRow
cGgsnHistNotifEntry = _CGgsnHistNotifEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 2, 7, 1)
)
cGgsnHistNotifEntry.setIndexNames(
    (0, "CISCO-GGSN-MIB", "cGgsnHistNotifIndex"),
)
if mibBuilder.loadTexts:
    cGgsnHistNotifEntry.setStatus("current")


class _CGgsnHistNotifIndex_Type(Unsigned32):
    """Custom type cGgsnHistNotifIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CGgsnHistNotifIndex_Type.__name__ = "Unsigned32"
_CGgsnHistNotifIndex_Object = MibTableColumn
cGgsnHistNotifIndex = _CGgsnHistNotifIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 2, 7, 1, 1),
    _CGgsnHistNotifIndex_Type()
)
cGgsnHistNotifIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cGgsnHistNotifIndex.setStatus("current")


class _CGgsnHistNotifType_Type(Integer32):
    """Custom type cGgsnHistNotifType based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("apnUnreachable", 10),
          ("authenticationFail", 9),
          ("ggsnServiceDown", 2),
          ("ggsnServiceUp", 1),
          ("ipAllocationFail", 8),
          ("mapSgsnDown", 4),
          ("mapSgsnUp", 3),
          ("noDHCPServer", 7),
          ("noRADIUS", 6),
          ("noResource", 5))
    )


_CGgsnHistNotifType_Type.__name__ = "Integer32"
_CGgsnHistNotifType_Object = MibTableColumn
cGgsnHistNotifType = _CGgsnHistNotifType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 2, 7, 1, 2),
    _CGgsnHistNotifType_Type()
)
cGgsnHistNotifType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnHistNotifType.setStatus("current")
_CGgsnHistNotifSeverity_Type = CiscoAlarmSeverity
_CGgsnHistNotifSeverity_Object = MibTableColumn
cGgsnHistNotifSeverity = _CGgsnHistNotifSeverity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 2, 7, 1, 3),
    _CGgsnHistNotifSeverity_Type()
)
cGgsnHistNotifSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnHistNotifSeverity.setStatus("current")
_CGgsnHistNotifTimestamp_Type = TimeStamp
_CGgsnHistNotifTimestamp_Object = MibTableColumn
cGgsnHistNotifTimestamp = _CGgsnHistNotifTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 2, 7, 1, 4),
    _CGgsnHistNotifTimestamp_Type()
)
cGgsnHistNotifTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnHistNotifTimestamp.setStatus("current")
_CGgsnHistNotifGgsnIpAddrType_Type = InetAddressType
_CGgsnHistNotifGgsnIpAddrType_Object = MibTableColumn
cGgsnHistNotifGgsnIpAddrType = _CGgsnHistNotifGgsnIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 2, 7, 1, 5),
    _CGgsnHistNotifGgsnIpAddrType_Type()
)
cGgsnHistNotifGgsnIpAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnHistNotifGgsnIpAddrType.setStatus("current")
_CGgsnHistNotifGgsnIpAddr_Type = InetAddress
_CGgsnHistNotifGgsnIpAddr_Object = MibTableColumn
cGgsnHistNotifGgsnIpAddr = _CGgsnHistNotifGgsnIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 2, 7, 1, 6),
    _CGgsnHistNotifGgsnIpAddr_Type()
)
cGgsnHistNotifGgsnIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnHistNotifGgsnIpAddr.setStatus("current")


class _CGgsnHistNotifInfo_Type(DisplayString):
    """Custom type cGgsnHistNotifInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CGgsnHistNotifInfo_Type.__name__ = "DisplayString"
_CGgsnHistNotifInfo_Object = MibTableColumn
cGgsnHistNotifInfo = _CGgsnHistNotifInfo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 2, 7, 1, 7),
    _CGgsnHistNotifInfo_Type()
)
cGgsnHistNotifInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnHistNotifInfo.setStatus("current")


class _CGgsnServiceNotifEnabled_Type(TruthValue):
    """Custom type cGgsnServiceNotifEnabled based on TruthValue"""


_CGgsnServiceNotifEnabled_Object = MibScalar
cGgsnServiceNotifEnabled = _CGgsnServiceNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 2, 8),
    _CGgsnServiceNotifEnabled_Type()
)
cGgsnServiceNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cGgsnServiceNotifEnabled.setStatus("current")


class _CGgsnMemoryNotifEnabled_Type(TruthValue):
    """Custom type cGgsnMemoryNotifEnabled based on TruthValue"""


_CGgsnMemoryNotifEnabled_Object = MibScalar
cGgsnMemoryNotifEnabled = _CGgsnMemoryNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 2, 9),
    _CGgsnMemoryNotifEnabled_Type()
)
cGgsnMemoryNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cGgsnMemoryNotifEnabled.setStatus("current")


class _CGgsnPdfNotifEnabled_Type(TruthValue):
    """Custom type cGgsnPdfNotifEnabled based on TruthValue"""


_CGgsnPdfNotifEnabled_Object = MibScalar
cGgsnPdfNotifEnabled = _CGgsnPdfNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 2, 10),
    _CGgsnPdfNotifEnabled_Type()
)
cGgsnPdfNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cGgsnPdfNotifEnabled.setStatus("deprecated")


class _CGgsnGlobalErrorNotifEnabled_Type(TruthValue):
    """Custom type cGgsnGlobalErrorNotifEnabled based on TruthValue"""


_CGgsnGlobalErrorNotifEnabled_Object = MibScalar
cGgsnGlobalErrorNotifEnabled = _CGgsnGlobalErrorNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 2, 11),
    _CGgsnGlobalErrorNotifEnabled_Type()
)
cGgsnGlobalErrorNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cGgsnGlobalErrorNotifEnabled.setStatus("current")


class _CGgsnAccessPointNotifEnabled_Type(TruthValue):
    """Custom type cGgsnAccessPointNotifEnabled based on TruthValue"""


_CGgsnAccessPointNotifEnabled_Object = MibScalar
cGgsnAccessPointNotifEnabled = _CGgsnAccessPointNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 2, 12),
    _CGgsnAccessPointNotifEnabled_Type()
)
cGgsnAccessPointNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cGgsnAccessPointNotifEnabled.setStatus("current")


class _CGgsnPdpNotifEnabled_Type(TruthValue):
    """Custom type cGgsnPdpNotifEnabled based on TruthValue"""


_CGgsnPdpNotifEnabled_Object = MibScalar
cGgsnPdpNotifEnabled = _CGgsnPdpNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 2, 13),
    _CGgsnPdpNotifEnabled_Type()
)
cGgsnPdpNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cGgsnPdpNotifEnabled.setStatus("current")
_CGgsnConfigurations_ObjectIdentity = ObjectIdentity
cGgsnConfigurations = _CGgsnConfigurations_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 3)
)


class _CGgsnDefaultIpAllocationMethod_Type(Integer32):
    """Custom type cGgsnDefaultIpAllocationMethod based on Integer32"""
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
        *(("dhcp", 2),
          ("disable", 1),
          ("radius", 3))
    )


_CGgsnDefaultIpAllocationMethod_Type.__name__ = "Integer32"
_CGgsnDefaultIpAllocationMethod_Object = MibScalar
cGgsnDefaultIpAllocationMethod = _CGgsnDefaultIpAllocationMethod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 3, 1),
    _CGgsnDefaultIpAllocationMethod_Type()
)
cGgsnDefaultIpAllocationMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cGgsnDefaultIpAllocationMethod.setStatus("current")


class _CGgsnIdlePdpPurgeTimer_Type(Unsigned32):
    """Custom type cGgsnIdlePdpPurgeTimer based on Unsigned32"""
    defaultValue = 72

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CGgsnIdlePdpPurgeTimer_Type.__name__ = "Unsigned32"
_CGgsnIdlePdpPurgeTimer_Object = MibScalar
cGgsnIdlePdpPurgeTimer = _CGgsnIdlePdpPurgeTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 3, 2),
    _CGgsnIdlePdpPurgeTimer_Type()
)
cGgsnIdlePdpPurgeTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cGgsnIdlePdpPurgeTimer.setStatus("current")
if mibBuilder.loadTexts:
    cGgsnIdlePdpPurgeTimer.setUnits("hours")
_CGgsnIpDupProtectTable_Object = MibTable
cGgsnIpDupProtectTable = _CGgsnIpDupProtectTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 3, 3)
)
if mibBuilder.loadTexts:
    cGgsnIpDupProtectTable.setStatus("current")
_CGgsnIpDupProtectEntry_Object = MibTableRow
cGgsnIpDupProtectEntry = _CGgsnIpDupProtectEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 3, 3, 1)
)
cGgsnIpDupProtectEntry.setIndexNames(
    (0, "CISCO-GGSN-MIB", "cGgsnMsExcludeRangeStartIpType"),
    (0, "CISCO-GGSN-MIB", "cGgsnMsExcludeRangeStartIp"),
    (0, "CISCO-GGSN-MIB", "cGgsnMsExcludeRangeEndIpType"),
    (0, "CISCO-GGSN-MIB", "cGgsnMsExcludeRangeEndIp"),
)
if mibBuilder.loadTexts:
    cGgsnIpDupProtectEntry.setStatus("current")
_CGgsnMsExcludeRangeStartIpType_Type = InetAddressType
_CGgsnMsExcludeRangeStartIpType_Object = MibTableColumn
cGgsnMsExcludeRangeStartIpType = _CGgsnMsExcludeRangeStartIpType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 3, 3, 1, 1),
    _CGgsnMsExcludeRangeStartIpType_Type()
)
cGgsnMsExcludeRangeStartIpType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cGgsnMsExcludeRangeStartIpType.setStatus("current")


class _CGgsnMsExcludeRangeStartIp_Type(InetAddress):
    """Custom type cGgsnMsExcludeRangeStartIp based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 20),
    )


_CGgsnMsExcludeRangeStartIp_Type.__name__ = "InetAddress"
_CGgsnMsExcludeRangeStartIp_Object = MibTableColumn
cGgsnMsExcludeRangeStartIp = _CGgsnMsExcludeRangeStartIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 3, 3, 1, 2),
    _CGgsnMsExcludeRangeStartIp_Type()
)
cGgsnMsExcludeRangeStartIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cGgsnMsExcludeRangeStartIp.setStatus("current")
_CGgsnMsExcludeRangeEndIpType_Type = InetAddressType
_CGgsnMsExcludeRangeEndIpType_Object = MibTableColumn
cGgsnMsExcludeRangeEndIpType = _CGgsnMsExcludeRangeEndIpType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 3, 3, 1, 3),
    _CGgsnMsExcludeRangeEndIpType_Type()
)
cGgsnMsExcludeRangeEndIpType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cGgsnMsExcludeRangeEndIpType.setStatus("current")


class _CGgsnMsExcludeRangeEndIp_Type(InetAddress):
    """Custom type cGgsnMsExcludeRangeEndIp based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 20),
    )


_CGgsnMsExcludeRangeEndIp_Type.__name__ = "InetAddress"
_CGgsnMsExcludeRangeEndIp_Object = MibTableColumn
cGgsnMsExcludeRangeEndIp = _CGgsnMsExcludeRangeEndIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 3, 3, 1, 4),
    _CGgsnMsExcludeRangeEndIp_Type()
)
cGgsnMsExcludeRangeEndIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cGgsnMsExcludeRangeEndIp.setStatus("current")
_CGgsnIpDupProtectRowStatus_Type = RowStatus
_CGgsnIpDupProtectRowStatus_Object = MibTableColumn
cGgsnIpDupProtectRowStatus = _CGgsnIpDupProtectRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 3, 3, 1, 5),
    _CGgsnIpDupProtectRowStatus_Type()
)
cGgsnIpDupProtectRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cGgsnIpDupProtectRowStatus.setStatus("current")
_CGgsnMsExcludeRangeStartIpv6Prefixlen_Type = InetAddressPrefixLength
_CGgsnMsExcludeRangeStartIpv6Prefixlen_Object = MibTableColumn
cGgsnMsExcludeRangeStartIpv6Prefixlen = _CGgsnMsExcludeRangeStartIpv6Prefixlen_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 3, 3, 1, 6),
    _CGgsnMsExcludeRangeStartIpv6Prefixlen_Type()
)
cGgsnMsExcludeRangeStartIpv6Prefixlen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cGgsnMsExcludeRangeStartIpv6Prefixlen.setStatus("current")
_CGgsnMsExcludeRangeEndIpv6Prefixlen_Type = InetAddressPrefixLength
_CGgsnMsExcludeRangeEndIpv6Prefixlen_Object = MibTableColumn
cGgsnMsExcludeRangeEndIpv6Prefixlen = _CGgsnMsExcludeRangeEndIpv6Prefixlen_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 3, 3, 1, 7),
    _CGgsnMsExcludeRangeEndIpv6Prefixlen_Type()
)
cGgsnMsExcludeRangeEndIpv6Prefixlen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cGgsnMsExcludeRangeEndIpv6Prefixlen.setStatus("current")
_CGgsnDefaultAggregTable_Object = MibTable
cGgsnDefaultAggregTable = _CGgsnDefaultAggregTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 3, 4)
)
if mibBuilder.loadTexts:
    cGgsnDefaultAggregTable.setStatus("current")
_CGgsnDefaultAggregEntry_Object = MibTableRow
cGgsnDefaultAggregEntry = _CGgsnDefaultAggregEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 3, 4, 1)
)
cGgsnDefaultAggregEntry.setIndexNames(
    (0, "CISCO-GGSN-MIB", "cGgsnDefaultAggregIpAddrType"),
    (0, "CISCO-GGSN-MIB", "cGgsnDefaultAggregIpAddr"),
    (0, "CISCO-GGSN-MIB", "cGgsnDefaultAggregIpMask"),
)
if mibBuilder.loadTexts:
    cGgsnDefaultAggregEntry.setStatus("current")
_CGgsnDefaultAggregIpAddrType_Type = InetAddressType
_CGgsnDefaultAggregIpAddrType_Object = MibTableColumn
cGgsnDefaultAggregIpAddrType = _CGgsnDefaultAggregIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 3, 4, 1, 1),
    _CGgsnDefaultAggregIpAddrType_Type()
)
cGgsnDefaultAggregIpAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cGgsnDefaultAggregIpAddrType.setStatus("current")


class _CGgsnDefaultAggregIpAddr_Type(InetAddress):
    """Custom type cGgsnDefaultAggregIpAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 20),
    )


_CGgsnDefaultAggregIpAddr_Type.__name__ = "InetAddress"
_CGgsnDefaultAggregIpAddr_Object = MibTableColumn
cGgsnDefaultAggregIpAddr = _CGgsnDefaultAggregIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 3, 4, 1, 2),
    _CGgsnDefaultAggregIpAddr_Type()
)
cGgsnDefaultAggregIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cGgsnDefaultAggregIpAddr.setStatus("current")
_CGgsnDefaultAggregIpMask_Type = CiscoInetAddressMask
_CGgsnDefaultAggregIpMask_Object = MibTableColumn
cGgsnDefaultAggregIpMask = _CGgsnDefaultAggregIpMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 3, 4, 1, 3),
    _CGgsnDefaultAggregIpMask_Type()
)
cGgsnDefaultAggregIpMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cGgsnDefaultAggregIpMask.setStatus("current")
_CGgsnDefaultAggregRowStatus_Type = RowStatus
_CGgsnDefaultAggregRowStatus_Object = MibTableColumn
cGgsnDefaultAggregRowStatus = _CGgsnDefaultAggregRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 3, 4, 1, 4),
    _CGgsnDefaultAggregRowStatus_Type()
)
cGgsnDefaultAggregRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cGgsnDefaultAggregRowStatus.setStatus("current")
_CGgsnDefaultAaaAuthServerGroup_Type = DisplayString
_CGgsnDefaultAaaAuthServerGroup_Object = MibScalar
cGgsnDefaultAaaAuthServerGroup = _CGgsnDefaultAaaAuthServerGroup_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 3, 5),
    _CGgsnDefaultAaaAuthServerGroup_Type()
)
cGgsnDefaultAaaAuthServerGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cGgsnDefaultAaaAuthServerGroup.setStatus("current")
_CGgsnDefaultAaaAccServerGroup_Type = DisplayString
_CGgsnDefaultAaaAccServerGroup_Object = MibScalar
cGgsnDefaultAaaAccServerGroup = _CGgsnDefaultAaaAccServerGroup_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 3, 6),
    _CGgsnDefaultAaaAccServerGroup_Type()
)
cGgsnDefaultAaaAccServerGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cGgsnDefaultAaaAccServerGroup.setStatus("current")
_CGgsnPppVirtualTemplate_Type = InterfaceIndexOrZero
_CGgsnPppVirtualTemplate_Object = MibScalar
cGgsnPppVirtualTemplate = _CGgsnPppVirtualTemplate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 3, 7),
    _CGgsnPppVirtualTemplate_Type()
)
cGgsnPppVirtualTemplate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cGgsnPppVirtualTemplate.setStatus("current")


class _CGgsnPppRegenVirtualTemplate_Type(InterfaceIndexOrZero):
    """Custom type cGgsnPppRegenVirtualTemplate based on InterfaceIndexOrZero"""
    defaultValue = 0


_CGgsnPppRegenVirtualTemplate_Object = MibScalar
cGgsnPppRegenVirtualTemplate = _CGgsnPppRegenVirtualTemplate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 3, 8),
    _CGgsnPppRegenVirtualTemplate_Type()
)
cGgsnPppRegenVirtualTemplate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cGgsnPppRegenVirtualTemplate.setStatus("current")
_CGgsnPlmnIpAddrRangeTable_Object = MibTable
cGgsnPlmnIpAddrRangeTable = _CGgsnPlmnIpAddrRangeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 3, 9)
)
if mibBuilder.loadTexts:
    cGgsnPlmnIpAddrRangeTable.setStatus("current")
_CGgsnPlmnIpAddrRangeEntry_Object = MibTableRow
cGgsnPlmnIpAddrRangeEntry = _CGgsnPlmnIpAddrRangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 3, 9, 1)
)
cGgsnPlmnIpAddrRangeEntry.setIndexNames(
    (0, "CISCO-GGSN-MIB", "cGgsnPlmnAddrRangeIpAddrType"),
    (0, "CISCO-GGSN-MIB", "cGgsnPlmnAddrRangeFirstIp"),
    (0, "CISCO-GGSN-MIB", "cGgsnPlmnAddrRangeLastIp"),
)
if mibBuilder.loadTexts:
    cGgsnPlmnIpAddrRangeEntry.setStatus("current")
_CGgsnPlmnAddrRangeIpAddrType_Type = InetAddressType
_CGgsnPlmnAddrRangeIpAddrType_Object = MibTableColumn
cGgsnPlmnAddrRangeIpAddrType = _CGgsnPlmnAddrRangeIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 3, 9, 1, 1),
    _CGgsnPlmnAddrRangeIpAddrType_Type()
)
cGgsnPlmnAddrRangeIpAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cGgsnPlmnAddrRangeIpAddrType.setStatus("current")


class _CGgsnPlmnAddrRangeFirstIp_Type(InetAddress):
    """Custom type cGgsnPlmnAddrRangeFirstIp based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 20),
    )


_CGgsnPlmnAddrRangeFirstIp_Type.__name__ = "InetAddress"
_CGgsnPlmnAddrRangeFirstIp_Object = MibTableColumn
cGgsnPlmnAddrRangeFirstIp = _CGgsnPlmnAddrRangeFirstIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 3, 9, 1, 2),
    _CGgsnPlmnAddrRangeFirstIp_Type()
)
cGgsnPlmnAddrRangeFirstIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cGgsnPlmnAddrRangeFirstIp.setStatus("current")


class _CGgsnPlmnAddrRangeLastIp_Type(InetAddress):
    """Custom type cGgsnPlmnAddrRangeLastIp based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 20),
    )


_CGgsnPlmnAddrRangeLastIp_Type.__name__ = "InetAddress"
_CGgsnPlmnAddrRangeLastIp_Object = MibTableColumn
cGgsnPlmnAddrRangeLastIp = _CGgsnPlmnAddrRangeLastIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 3, 9, 1, 3),
    _CGgsnPlmnAddrRangeLastIp_Type()
)
cGgsnPlmnAddrRangeLastIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cGgsnPlmnAddrRangeLastIp.setStatus("current")
_CGgsnPlmnAddrRangeRowStatus_Type = RowStatus
_CGgsnPlmnAddrRangeRowStatus_Object = MibTableColumn
cGgsnPlmnAddrRangeRowStatus = _CGgsnPlmnAddrRangeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 3, 9, 1, 4),
    _CGgsnPlmnAddrRangeRowStatus_Type()
)
cGgsnPlmnAddrRangeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cGgsnPlmnAddrRangeRowStatus.setStatus("current")


class _CGgsnPlmnAddrRangeUsage_Type(Integer32):
    """Custom type cGgsnPlmnAddrRangeUsage based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("security", 1),
          ("sgsn", 2))
    )


_CGgsnPlmnAddrRangeUsage_Type.__name__ = "Integer32"
_CGgsnPlmnAddrRangeUsage_Object = MibTableColumn
cGgsnPlmnAddrRangeUsage = _CGgsnPlmnAddrRangeUsage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 3, 9, 1, 5),
    _CGgsnPlmnAddrRangeUsage_Type()
)
cGgsnPlmnAddrRangeUsage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cGgsnPlmnAddrRangeUsage.setStatus("current")
_CGgsnPlmnAddrRangeFirstIpv6Prefixlen_Type = InetAddressPrefixLength
_CGgsnPlmnAddrRangeFirstIpv6Prefixlen_Object = MibTableColumn
cGgsnPlmnAddrRangeFirstIpv6Prefixlen = _CGgsnPlmnAddrRangeFirstIpv6Prefixlen_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 3, 9, 1, 6),
    _CGgsnPlmnAddrRangeFirstIpv6Prefixlen_Type()
)
cGgsnPlmnAddrRangeFirstIpv6Prefixlen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cGgsnPlmnAddrRangeFirstIpv6Prefixlen.setStatus("current")
_CGgsnPlmnAddrRangeLastIpv6Prefixlen_Type = InetAddressPrefixLength
_CGgsnPlmnAddrRangeLastIpv6Prefixlen_Object = MibTableColumn
cGgsnPlmnAddrRangeLastIpv6Prefixlen = _CGgsnPlmnAddrRangeLastIpv6Prefixlen_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 3, 9, 1, 7),
    _CGgsnPlmnAddrRangeLastIpv6Prefixlen_Type()
)
cGgsnPlmnAddrRangeLastIpv6Prefixlen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cGgsnPlmnAddrRangeLastIpv6Prefixlen.setStatus("current")
_CGgsnImsConfigurations_ObjectIdentity = ObjectIdentity
cGgsnImsConfigurations = _CGgsnImsConfigurations_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 3, 10)
)
_CGgsnPdfTable_Object = MibTable
cGgsnPdfTable = _CGgsnPdfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 3, 10, 1)
)
if mibBuilder.loadTexts:
    cGgsnPdfTable.setStatus("deprecated")
_CGgsnPdfEntry_Object = MibTableRow
cGgsnPdfEntry = _CGgsnPdfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 3, 10, 1, 1)
)
cGgsnPdfEntry.setIndexNames(
    (0, "CISCO-GGSN-MIB", "cGgsnPdfGroupName"),
    (0, "CISCO-GGSN-MIB", "cGgsnPdfDomainName"),
    (0, "CISCO-GGSN-MIB", "cGgsnPdfIpAddressType"),
    (0, "CISCO-GGSN-MIB", "cGgsnPdfIpAddress"),
)
if mibBuilder.loadTexts:
    cGgsnPdfEntry.setStatus("deprecated")


class _CGgsnPdfGroupName_Type(SnmpAdminString):
    """Custom type cGgsnPdfGroupName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 100),
    )


_CGgsnPdfGroupName_Type.__name__ = "SnmpAdminString"
_CGgsnPdfGroupName_Object = MibTableColumn
cGgsnPdfGroupName = _CGgsnPdfGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 3, 10, 1, 1, 1),
    _CGgsnPdfGroupName_Type()
)
cGgsnPdfGroupName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cGgsnPdfGroupName.setStatus("deprecated")


class _CGgsnPdfDomainName_Type(InetAddressDNS):
    """Custom type cGgsnPdfDomainName based on InetAddressDNS"""
    subtypeSpec = InetAddressDNS.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 100),
    )


_CGgsnPdfDomainName_Type.__name__ = "InetAddressDNS"
_CGgsnPdfDomainName_Object = MibTableColumn
cGgsnPdfDomainName = _CGgsnPdfDomainName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 3, 10, 1, 1, 2),
    _CGgsnPdfDomainName_Type()
)
cGgsnPdfDomainName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cGgsnPdfDomainName.setStatus("deprecated")
_CGgsnPdfIpAddressType_Type = InetAddressType
_CGgsnPdfIpAddressType_Object = MibTableColumn
cGgsnPdfIpAddressType = _CGgsnPdfIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 3, 10, 1, 1, 3),
    _CGgsnPdfIpAddressType_Type()
)
cGgsnPdfIpAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cGgsnPdfIpAddressType.setStatus("deprecated")
_CGgsnPdfIpAddress_Type = InetAddress
_CGgsnPdfIpAddress_Object = MibTableColumn
cGgsnPdfIpAddress = _CGgsnPdfIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 3, 10, 1, 1, 4),
    _CGgsnPdfIpAddress_Type()
)
cGgsnPdfIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cGgsnPdfIpAddress.setStatus("deprecated")
_CGgsnPdfRowStatus_Type = RowStatus
_CGgsnPdfRowStatus_Object = MibTableColumn
cGgsnPdfRowStatus = _CGgsnPdfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 3, 10, 1, 1, 5),
    _CGgsnPdfRowStatus_Type()
)
cGgsnPdfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cGgsnPdfRowStatus.setStatus("deprecated")


class _CGgsnPdfReconnectTimeOut_Type(Unsigned32):
    """Custom type cGgsnPdfReconnectTimeOut based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_CGgsnPdfReconnectTimeOut_Type.__name__ = "Unsigned32"
_CGgsnPdfReconnectTimeOut_Object = MibTableColumn
cGgsnPdfReconnectTimeOut = _CGgsnPdfReconnectTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 3, 10, 1, 1, 6),
    _CGgsnPdfReconnectTimeOut_Type()
)
cGgsnPdfReconnectTimeOut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cGgsnPdfReconnectTimeOut.setStatus("deprecated")
if mibBuilder.loadTexts:
    cGgsnPdfReconnectTimeOut.setUnits("minutes")


class _CGgsnPdfReconnectRetries_Type(Unsigned32):
    """Custom type cGgsnPdfReconnectRetries based on Unsigned32"""
    defaultValue = 65535

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
        ValueRangeConstraint(65535, 65535),
    )


_CGgsnPdfReconnectRetries_Type.__name__ = "Unsigned32"
_CGgsnPdfReconnectRetries_Object = MibTableColumn
cGgsnPdfReconnectRetries = _CGgsnPdfReconnectRetries_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 3, 10, 1, 1, 7),
    _CGgsnPdfReconnectRetries_Type()
)
cGgsnPdfReconnectRetries.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cGgsnPdfReconnectRetries.setStatus("deprecated")


class _CGgsnPdfReconExpPdpDelete_Type(TruthValue):
    """Custom type cGgsnPdfReconExpPdpDelete based on TruthValue"""


_CGgsnPdfReconExpPdpDelete_Object = MibTableColumn
cGgsnPdfReconExpPdpDelete = _CGgsnPdfReconExpPdpDelete_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 3, 10, 1, 1, 8),
    _CGgsnPdfReconExpPdpDelete_Type()
)
cGgsnPdfReconExpPdpDelete.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cGgsnPdfReconExpPdpDelete.setStatus("deprecated")


class _CGgsnPdfReqRetryTimeOut_Type(Unsigned32):
    """Custom type cGgsnPdfReqRetryTimeOut based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_CGgsnPdfReqRetryTimeOut_Type.__name__ = "Unsigned32"
_CGgsnPdfReqRetryTimeOut_Object = MibTableColumn
cGgsnPdfReqRetryTimeOut = _CGgsnPdfReqRetryTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 3, 10, 1, 1, 9),
    _CGgsnPdfReqRetryTimeOut_Type()
)
cGgsnPdfReqRetryTimeOut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cGgsnPdfReqRetryTimeOut.setStatus("deprecated")
if mibBuilder.loadTexts:
    cGgsnPdfReqRetryTimeOut.setUnits("seconds")


class _CGgsnPdfReqRetries_Type(Unsigned32):
    """Custom type cGgsnPdfReqRetries based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_CGgsnPdfReqRetries_Type.__name__ = "Unsigned32"
_CGgsnPdfReqRetries_Object = MibTableColumn
cGgsnPdfReqRetries = _CGgsnPdfReqRetries_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 3, 10, 1, 1, 10),
    _CGgsnPdfReqRetries_Type()
)
cGgsnPdfReqRetries.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cGgsnPdfReqRetries.setStatus("deprecated")
_CGgsnPcscfTable_Object = MibTable
cGgsnPcscfTable = _CGgsnPcscfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 3, 10, 2)
)
if mibBuilder.loadTexts:
    cGgsnPcscfTable.setStatus("current")
_CGgsnPcscfEntry_Object = MibTableRow
cGgsnPcscfEntry = _CGgsnPcscfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 3, 10, 2, 1)
)
cGgsnPcscfEntry.setIndexNames(
    (0, "CISCO-GGSN-MIB", "cGgsnPcscfGroupName"),
    (0, "CISCO-GGSN-MIB", "cGgsnPcscfIpAddressType"),
    (0, "CISCO-GGSN-MIB", "cGgsnPcscfIpAddress"),
)
if mibBuilder.loadTexts:
    cGgsnPcscfEntry.setStatus("current")


class _CGgsnPcscfGroupName_Type(SnmpAdminString):
    """Custom type cGgsnPcscfGroupName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 100),
    )


_CGgsnPcscfGroupName_Type.__name__ = "SnmpAdminString"
_CGgsnPcscfGroupName_Object = MibTableColumn
cGgsnPcscfGroupName = _CGgsnPcscfGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 3, 10, 2, 1, 1),
    _CGgsnPcscfGroupName_Type()
)
cGgsnPcscfGroupName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cGgsnPcscfGroupName.setStatus("current")
_CGgsnPcscfIpAddressType_Type = InetAddressType
_CGgsnPcscfIpAddressType_Object = MibTableColumn
cGgsnPcscfIpAddressType = _CGgsnPcscfIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 3, 10, 2, 1, 2),
    _CGgsnPcscfIpAddressType_Type()
)
cGgsnPcscfIpAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cGgsnPcscfIpAddressType.setStatus("current")
_CGgsnPcscfIpAddress_Type = InetAddress
_CGgsnPcscfIpAddress_Object = MibTableColumn
cGgsnPcscfIpAddress = _CGgsnPcscfIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 3, 10, 2, 1, 3),
    _CGgsnPcscfIpAddress_Type()
)
cGgsnPcscfIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cGgsnPcscfIpAddress.setStatus("current")
_CGgsnPcscfRowStatus_Type = RowStatus
_CGgsnPcscfRowStatus_Object = MibTableColumn
cGgsnPcscfRowStatus = _CGgsnPcscfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 3, 10, 2, 1, 4),
    _CGgsnPcscfRowStatus_Type()
)
cGgsnPcscfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cGgsnPcscfRowStatus.setStatus("current")


class _CGgsnMemoryThreshold_Type(Unsigned32):
    """Custom type cGgsnMemoryThreshold based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_CGgsnMemoryThreshold_Type.__name__ = "Unsigned32"
_CGgsnMemoryThreshold_Object = MibScalar
cGgsnMemoryThreshold = _CGgsnMemoryThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 3, 11),
    _CGgsnMemoryThreshold_Type()
)
cGgsnMemoryThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cGgsnMemoryThreshold.setStatus("current")
if mibBuilder.loadTexts:
    cGgsnMemoryThreshold.setUnits("98304Bytes")


class _CGgsnServiceMode_Type(Integer32):
    """Custom type cGgsnServiceMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inService", 1),
          ("maintenance", 2))
    )


_CGgsnServiceMode_Type.__name__ = "Integer32"
_CGgsnServiceMode_Object = MibScalar
cGgsnServiceMode = _CGgsnServiceMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 3, 12),
    _CGgsnServiceMode_Type()
)
cGgsnServiceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cGgsnServiceMode.setStatus("current")
_CGgsnPlmnTable_Object = MibTable
cGgsnPlmnTable = _CGgsnPlmnTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 3, 13)
)
if mibBuilder.loadTexts:
    cGgsnPlmnTable.setStatus("current")
_CGgsnPlmnEntry_Object = MibTableRow
cGgsnPlmnEntry = _CGgsnPlmnEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 3, 13, 1)
)
cGgsnPlmnEntry.setIndexNames(
    (0, "CISCO-GGSN-MIB", "cGgsnPlmnMcc"),
    (0, "CISCO-GGSN-MIB", "cGgsnPlmnMnc"),
)
if mibBuilder.loadTexts:
    cGgsnPlmnEntry.setStatus("current")


class _CGgsnPlmnMcc_Type(SnmpAdminString):
    """Custom type cGgsnPlmnMcc based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_CGgsnPlmnMcc_Type.__name__ = "SnmpAdminString"
_CGgsnPlmnMcc_Object = MibTableColumn
cGgsnPlmnMcc = _CGgsnPlmnMcc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 3, 13, 1, 1),
    _CGgsnPlmnMcc_Type()
)
cGgsnPlmnMcc.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cGgsnPlmnMcc.setStatus("current")


class _CGgsnPlmnMnc_Type(SnmpAdminString):
    """Custom type cGgsnPlmnMnc based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 3),
    )


_CGgsnPlmnMnc_Type.__name__ = "SnmpAdminString"
_CGgsnPlmnMnc_Object = MibTableColumn
cGgsnPlmnMnc = _CGgsnPlmnMnc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 3, 13, 1, 2),
    _CGgsnPlmnMnc_Type()
)
cGgsnPlmnMnc.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cGgsnPlmnMnc.setStatus("current")
_CGgsnPlmnRowStatus_Type = RowStatus
_CGgsnPlmnRowStatus_Object = MibTableColumn
cGgsnPlmnRowStatus = _CGgsnPlmnRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 3, 13, 1, 3),
    _CGgsnPlmnRowStatus_Type()
)
cGgsnPlmnRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cGgsnPlmnRowStatus.setStatus("current")


class _CGgsnPlmnScope_Type(Integer32):
    """Custom type cGgsnPlmnScope based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("home", 1),
          ("trusted", 2))
    )


_CGgsnPlmnScope_Type.__name__ = "Integer32"
_CGgsnPlmnScope_Object = MibTableColumn
cGgsnPlmnScope = _CGgsnPlmnScope_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 3, 13, 1, 4),
    _CGgsnPlmnScope_Type()
)
cGgsnPlmnScope.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cGgsnPlmnScope.setStatus("current")


class _CGgsnSessionTimeout_Type(Unsigned32):
    """Custom type cGgsnSessionTimeout based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(30, 4294967),
    )


_CGgsnSessionTimeout_Type.__name__ = "Unsigned32"
_CGgsnSessionTimeout_Object = MibScalar
cGgsnSessionTimeout = _CGgsnSessionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 3, 14),
    _CGgsnSessionTimeout_Type()
)
cGgsnSessionTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cGgsnSessionTimeout.setStatus("current")
if mibBuilder.loadTexts:
    cGgsnSessionTimeout.setUnits("seconds")


class _CGgsnThruputIntervalOne_Type(Unsigned32):
    """Custom type cGgsnThruputIntervalOne based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CGgsnThruputIntervalOne_Type.__name__ = "Unsigned32"
_CGgsnThruputIntervalOne_Object = MibScalar
cGgsnThruputIntervalOne = _CGgsnThruputIntervalOne_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 3, 15),
    _CGgsnThruputIntervalOne_Type()
)
cGgsnThruputIntervalOne.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cGgsnThruputIntervalOne.setStatus("current")
if mibBuilder.loadTexts:
    cGgsnThruputIntervalOne.setUnits("minutes")


class _CGgsnThruputIntervalTwo_Type(Unsigned32):
    """Custom type cGgsnThruputIntervalTwo based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CGgsnThruputIntervalTwo_Type.__name__ = "Unsigned32"
_CGgsnThruputIntervalTwo_Object = MibScalar
cGgsnThruputIntervalTwo = _CGgsnThruputIntervalTwo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 3, 16),
    _CGgsnThruputIntervalTwo_Type()
)
cGgsnThruputIntervalTwo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cGgsnThruputIntervalTwo.setStatus("current")
if mibBuilder.loadTexts:
    cGgsnThruputIntervalTwo.setUnits("minutes")


class _CGgsnCompliance3GppGgsn_Type(Integer32):
    """Custom type cGgsnCompliance3GppGgsn based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("release40", 1))
    )


_CGgsnCompliance3GppGgsn_Type.__name__ = "Integer32"
_CGgsnCompliance3GppGgsn_Object = MibScalar
cGgsnCompliance3GppGgsn = _CGgsnCompliance3GppGgsn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 3, 17),
    _CGgsnCompliance3GppGgsn_Type()
)
cGgsnCompliance3GppGgsn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cGgsnCompliance3GppGgsn.setStatus("deprecated")


class _CGgsnCreateReqV1UpdExistPdp_Type(TruthValue):
    """Custom type cGgsnCreateReqV1UpdExistPdp based on TruthValue"""


_CGgsnCreateReqV1UpdExistPdp_Object = MibScalar
cGgsnCreateReqV1UpdExistPdp = _CGgsnCreateReqV1UpdExistPdp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 3, 18),
    _CGgsnCreateReqV1UpdExistPdp_Type()
)
cGgsnCreateReqV1UpdExistPdp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cGgsnCreateReqV1UpdExistPdp.setStatus("deprecated")


class _CGgsnRadAttrSessTimeout_Type(TruthValue):
    """Custom type cGgsnRadAttrSessTimeout based on TruthValue"""


_CGgsnRadAttrSessTimeout_Object = MibScalar
cGgsnRadAttrSessTimeout = _CGgsnRadAttrSessTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 3, 19),
    _CGgsnRadAttrSessTimeout_Type()
)
cGgsnRadAttrSessTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cGgsnRadAttrSessTimeout.setStatus("current")


class _CGgsnDownlinkVerifyMsDisable_Type(TruthValue):
    """Custom type cGgsnDownlinkVerifyMsDisable based on TruthValue"""


_CGgsnDownlinkVerifyMsDisable_Object = MibScalar
cGgsnDownlinkVerifyMsDisable = _CGgsnDownlinkVerifyMsDisable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 3, 20),
    _CGgsnDownlinkVerifyMsDisable_Type()
)
cGgsnDownlinkVerifyMsDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cGgsnDownlinkVerifyMsDisable.setStatus("current")


class _CGgsnSlbMode_Type(Integer32):
    """Custom type cGgsnSlbMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("directed", 1),
          ("dispatched", 2))
    )


_CGgsnSlbMode_Type.__name__ = "Integer32"
_CGgsnSlbMode_Object = MibScalar
cGgsnSlbMode = _CGgsnSlbMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 3, 21),
    _CGgsnSlbMode_Type()
)
cGgsnSlbMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cGgsnSlbMode.setStatus("current")


class _CGgsnSlbNotif_Type(Integer32):
    """Custom type cGgsnSlbNotif based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cacFailure", 1),
          ("sessionDeletion", 2))
    )


_CGgsnSlbNotif_Type.__name__ = "Integer32"
_CGgsnSlbNotif_Object = MibScalar
cGgsnSlbNotif = _CGgsnSlbNotif_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 3, 22),
    _CGgsnSlbNotif_Type()
)
cGgsnSlbNotif.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cGgsnSlbNotif.setStatus("deprecated")
_CGgsnSlbVserverTable_Object = MibTable
cGgsnSlbVserverTable = _CGgsnSlbVserverTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 3, 23)
)
if mibBuilder.loadTexts:
    cGgsnSlbVserverTable.setStatus("current")
_CGgsnSlbVserverEntry_Object = MibTableRow
cGgsnSlbVserverEntry = _CGgsnSlbVserverEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 3, 23, 1)
)
cGgsnSlbVserverEntry.setIndexNames(
    (0, "CISCO-GGSN-MIB", "cGgsnSlbVserAddrType"),
    (0, "CISCO-GGSN-MIB", "cGgsnSlbVserAddress"),
)
if mibBuilder.loadTexts:
    cGgsnSlbVserverEntry.setStatus("current")
_CGgsnSlbVserAddrType_Type = InetAddressType
_CGgsnSlbVserAddrType_Object = MibTableColumn
cGgsnSlbVserAddrType = _CGgsnSlbVserAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 3, 23, 1, 1),
    _CGgsnSlbVserAddrType_Type()
)
cGgsnSlbVserAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cGgsnSlbVserAddrType.setStatus("current")


class _CGgsnSlbVserAddress_Type(InetAddress):
    """Custom type cGgsnSlbVserAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 20),
    )


_CGgsnSlbVserAddress_Type.__name__ = "InetAddress"
_CGgsnSlbVserAddress_Object = MibTableColumn
cGgsnSlbVserAddress = _CGgsnSlbVserAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 3, 23, 1, 2),
    _CGgsnSlbVserAddress_Type()
)
cGgsnSlbVserAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cGgsnSlbVserAddress.setStatus("current")


class _CGgsnSlbVserNextHopAddrType_Type(InetAddressType):
    """Custom type cGgsnSlbVserNextHopAddrType based on InetAddressType"""


_CGgsnSlbVserNextHopAddrType_Object = MibTableColumn
cGgsnSlbVserNextHopAddrType = _CGgsnSlbVserNextHopAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 3, 23, 1, 3),
    _CGgsnSlbVserNextHopAddrType_Type()
)
cGgsnSlbVserNextHopAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cGgsnSlbVserNextHopAddrType.setStatus("current")


class _CGgsnSlbVserNextHopAddress_Type(InetAddress):
    """Custom type cGgsnSlbVserNextHopAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 20),
    )


_CGgsnSlbVserNextHopAddress_Type.__name__ = "InetAddress"
_CGgsnSlbVserNextHopAddress_Object = MibTableColumn
cGgsnSlbVserNextHopAddress = _CGgsnSlbVserNextHopAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 3, 23, 1, 4),
    _CGgsnSlbVserNextHopAddress_Type()
)
cGgsnSlbVserNextHopAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cGgsnSlbVserNextHopAddress.setStatus("current")
_CGgsnSlbVserVrfName_Type = SnmpAdminString
_CGgsnSlbVserVrfName_Object = MibTableColumn
cGgsnSlbVserVrfName = _CGgsnSlbVserVrfName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 3, 23, 1, 5),
    _CGgsnSlbVserVrfName_Type()
)
cGgsnSlbVserVrfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cGgsnSlbVserVrfName.setStatus("current")
_CGgsnSlbVserRowStatus_Type = RowStatus
_CGgsnSlbVserRowStatus_Object = MibTableColumn
cGgsnSlbVserRowStatus = _CGgsnSlbVserRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 3, 23, 1, 6),
    _CGgsnSlbVserRowStatus_Type()
)
cGgsnSlbVserRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cGgsnSlbVserRowStatus.setStatus("current")


class _CGgsnSlbNotifyCacFailure_Type(TruthValue):
    """Custom type cGgsnSlbNotifyCacFailure based on TruthValue"""


_CGgsnSlbNotifyCacFailure_Object = MibScalar
cGgsnSlbNotifyCacFailure = _CGgsnSlbNotifyCacFailure_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 3, 24),
    _CGgsnSlbNotifyCacFailure_Type()
)
cGgsnSlbNotifyCacFailure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cGgsnSlbNotifyCacFailure.setStatus("current")


class _CGgsnSlbNotifySessionDeletion_Type(TruthValue):
    """Custom type cGgsnSlbNotifySessionDeletion based on TruthValue"""


_CGgsnSlbNotifySessionDeletion_Object = MibScalar
cGgsnSlbNotifySessionDeletion = _CGgsnSlbNotifySessionDeletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 3, 25),
    _CGgsnSlbNotifySessionDeletion_Type()
)
cGgsnSlbNotifySessionDeletion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cGgsnSlbNotifySessionDeletion.setStatus("current")
_CGgsnStatus_ObjectIdentity = ObjectIdentity
cGgsnStatus = _CGgsnStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 4)
)


class _CGgsnVersion_Type(Integer32):
    """Custom type cGgsnVersion based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("release100", 10),
          ("release14", 1),
          ("release30", 2),
          ("release31", 4),
          ("release40", 3),
          ("release50", 5),
          ("release60", 6),
          ("release70", 7),
          ("release80", 8),
          ("release90", 9))
    )


_CGgsnVersion_Type.__name__ = "Integer32"
_CGgsnVersion_Object = MibScalar
cGgsnVersion = _CGgsnVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 4, 1),
    _CGgsnVersion_Type()
)
cGgsnVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnVersion.setStatus("current")
_CGgsnActiveNetworkInitPdps_Type = Gauge32
_CGgsnActiveNetworkInitPdps_Object = MibScalar
cGgsnActiveNetworkInitPdps = _CGgsnActiveNetworkInitPdps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 4, 2),
    _CGgsnActiveNetworkInitPdps_Type()
)
cGgsnActiveNetworkInitPdps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnActiveNetworkInitPdps.setStatus("current")
if mibBuilder.loadTexts:
    cGgsnActiveNetworkInitPdps.setUnits("packets")
_CGgsnActivePppPdps_Type = Gauge32
_CGgsnActivePppPdps_Object = MibScalar
cGgsnActivePppPdps = _CGgsnActivePppPdps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 4, 3),
    _CGgsnActivePppPdps_Type()
)
cGgsnActivePppPdps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnActivePppPdps.setStatus("current")
if mibBuilder.loadTexts:
    cGgsnActivePppPdps.setUnits("packets")
_CGgsnActivePppRegenPdps_Type = Gauge32
_CGgsnActivePppRegenPdps_Object = MibScalar
cGgsnActivePppRegenPdps = _CGgsnActivePppRegenPdps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 4, 4),
    _CGgsnActivePppRegenPdps_Type()
)
cGgsnActivePppRegenPdps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnActivePppRegenPdps.setStatus("current")
if mibBuilder.loadTexts:
    cGgsnActivePppRegenPdps.setUnits("packets")
_CGgsnPendingPppRegenPdps_Type = Gauge32
_CGgsnPendingPppRegenPdps_Object = MibScalar
cGgsnPendingPppRegenPdps = _CGgsnPendingPppRegenPdps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 4, 5),
    _CGgsnPendingPppRegenPdps_Type()
)
cGgsnPendingPppRegenPdps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnPendingPppRegenPdps.setStatus("current")
if mibBuilder.loadTexts:
    cGgsnPendingPppRegenPdps.setUnits("packets")
_CGgsnActiveGtpVersion0Pdps_Type = Gauge32
_CGgsnActiveGtpVersion0Pdps_Object = MibScalar
cGgsnActiveGtpVersion0Pdps = _CGgsnActiveGtpVersion0Pdps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 4, 6),
    _CGgsnActiveGtpVersion0Pdps_Type()
)
cGgsnActiveGtpVersion0Pdps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnActiveGtpVersion0Pdps.setStatus("current")
_CGgsnActiveGtpVersion1Pdps_Type = Gauge32
_CGgsnActiveGtpVersion1Pdps_Object = MibScalar
cGgsnActiveGtpVersion1Pdps = _CGgsnActiveGtpVersion1Pdps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 4, 7),
    _CGgsnActiveGtpVersion1Pdps_Type()
)
cGgsnActiveGtpVersion1Pdps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnActiveGtpVersion1Pdps.setStatus("current")
_CGgsnGtpEncapInterface_Type = InterfaceIndexOrZero
_CGgsnGtpEncapInterface_Object = MibScalar
cGgsnGtpEncapInterface = _CGgsnGtpEncapInterface_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 4, 8),
    _CGgsnGtpEncapInterface_Type()
)
cGgsnGtpEncapInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnGtpEncapInterface.setStatus("current")


class _CGgsnServiceModeStatus_Type(Integer32):
    """Custom type cGgsnServiceModeStatus based on Integer32"""
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
        *(("inService", 1),
          ("maintenance", 2),
          ("outOfService", 4),
          ("outOfServiceInProgress", 3))
    )


_CGgsnServiceModeStatus_Type.__name__ = "Integer32"
_CGgsnServiceModeStatus_Object = MibScalar
cGgsnServiceModeStatus = _CGgsnServiceModeStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 4, 9),
    _CGgsnServiceModeStatus_Type()
)
cGgsnServiceModeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnServiceModeStatus.setStatus("current")
_CGgsnConfigVersion_Type = SnmpAdminString
_CGgsnConfigVersion_Object = MibScalar
cGgsnConfigVersion = _CGgsnConfigVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 4, 10),
    _CGgsnConfigVersion_Type()
)
cGgsnConfigVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnConfigVersion.setStatus("current")
_CGgsnPrepaidPDPs_Type = Gauge32
_CGgsnPrepaidPDPs_Object = MibScalar
cGgsnPrepaidPDPs = _CGgsnPrepaidPDPs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 4, 11),
    _CGgsnPrepaidPDPs_Type()
)
cGgsnPrepaidPDPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnPrepaidPDPs.setStatus("current")
_CGgsnPostpaidPDPs_Type = Gauge32
_CGgsnPostpaidPDPs_Object = MibScalar
cGgsnPostpaidPDPs = _CGgsnPostpaidPDPs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 4, 12),
    _CGgsnPostpaidPDPs_Type()
)
cGgsnPostpaidPDPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnPostpaidPDPs.setStatus("current")
_CGgsnActivatedIpv6Gtpv0Pdp_Type = Gauge32
_CGgsnActivatedIpv6Gtpv0Pdp_Object = MibScalar
cGgsnActivatedIpv6Gtpv0Pdp = _CGgsnActivatedIpv6Gtpv0Pdp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 4, 13),
    _CGgsnActivatedIpv6Gtpv0Pdp_Type()
)
cGgsnActivatedIpv6Gtpv0Pdp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnActivatedIpv6Gtpv0Pdp.setStatus("current")
if mibBuilder.loadTexts:
    cGgsnActivatedIpv6Gtpv0Pdp.setUnits("PDPs")
_CGgsnActivatedIpv6Gtpv1Pdp_Type = Gauge32
_CGgsnActivatedIpv6Gtpv1Pdp_Object = MibScalar
cGgsnActivatedIpv6Gtpv1Pdp = _CGgsnActivatedIpv6Gtpv1Pdp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 4, 14),
    _CGgsnActivatedIpv6Gtpv1Pdp_Type()
)
cGgsnActivatedIpv6Gtpv1Pdp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnActivatedIpv6Gtpv1Pdp.setStatus("current")
if mibBuilder.loadTexts:
    cGgsnActivatedIpv6Gtpv1Pdp.setUnits("PDPs")
_CGgsnActivatedIpv6Ms_Type = Gauge32
_CGgsnActivatedIpv6Ms_Object = MibScalar
cGgsnActivatedIpv6Ms = _CGgsnActivatedIpv6Ms_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 4, 15),
    _CGgsnActivatedIpv6Ms_Type()
)
cGgsnActivatedIpv6Ms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnActivatedIpv6Ms.setStatus("current")
if mibBuilder.loadTexts:
    cGgsnActivatedIpv6Ms.setUnits("PDPs")
_CGgsnGtpEncapsuTable_Object = MibTable
cGgsnGtpEncapsuTable = _CGgsnGtpEncapsuTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 4, 16)
)
if mibBuilder.loadTexts:
    cGgsnGtpEncapsuTable.setStatus("current")
_CGgsnGtpEncapsuEntry_Object = MibTableRow
cGgsnGtpEncapsuEntry = _CGgsnGtpEncapsuEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 4, 16, 1)
)
cGgsnGtpEncapsuEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cGgsnGtpEncapsuEntry.setStatus("current")
_CGgsnGtpEncapsuInterface_Type = InterfaceIndexOrZero
_CGgsnGtpEncapsuInterface_Object = MibTableColumn
cGgsnGtpEncapsuInterface = _CGgsnGtpEncapsuInterface_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 4, 16, 1, 1),
    _CGgsnGtpEncapsuInterface_Type()
)
cGgsnGtpEncapsuInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnGtpEncapsuInterface.setStatus("current")
_CGgsnNotifInfo_ObjectIdentity = ObjectIdentity
cGgsnNotifInfo = _CGgsnNotifInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 5)
)
_CGgsnPdfServerAddrType_Type = InetAddressType
_CGgsnPdfServerAddrType_Object = MibScalar
cGgsnPdfServerAddrType = _CGgsnPdfServerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 5, 1),
    _CGgsnPdfServerAddrType_Type()
)
cGgsnPdfServerAddrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cGgsnPdfServerAddrType.setStatus("deprecated")
_CGgsnPdfServerAddr_Type = InetAddress
_CGgsnPdfServerAddr_Object = MibScalar
cGgsnPdfServerAddr = _CGgsnPdfServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 5, 2),
    _CGgsnPdfServerAddr_Type()
)
cGgsnPdfServerAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cGgsnPdfServerAddr.setStatus("deprecated")


class _CGgsnNotifAccessPointName_Type(SnmpAdminString):
    """Custom type cGgsnNotifAccessPointName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 100),
    )


_CGgsnNotifAccessPointName_Type.__name__ = "SnmpAdminString"
_CGgsnNotifAccessPointName_Object = MibScalar
cGgsnNotifAccessPointName = _CGgsnNotifAccessPointName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 5, 3),
    _CGgsnNotifAccessPointName_Type()
)
cGgsnNotifAccessPointName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cGgsnNotifAccessPointName.setStatus("current")


class _CGgsnNotifPdpImsi_Type(SnmpAdminString):
    """Custom type cGgsnNotifPdpImsi based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_CGgsnNotifPdpImsi_Type.__name__ = "SnmpAdminString"
_CGgsnNotifPdpImsi_Object = MibScalar
cGgsnNotifPdpImsi = _CGgsnNotifPdpImsi_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 5, 4),
    _CGgsnNotifPdpImsi_Type()
)
cGgsnNotifPdpImsi.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cGgsnNotifPdpImsi.setStatus("current")


class _CGgsnGlobalErrorTypes_Type(Integer32):
    """Custom type cGgsnGlobalErrorTypes based on Integer32"""
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
        *(("ggsnServiceDown", 2),
          ("ggsnServiceUp", 1),
          ("mapSgsnDown", 4),
          ("mapSgsnUp", 3),
          ("noDHCPServer", 5))
    )


_CGgsnGlobalErrorTypes_Type.__name__ = "Integer32"
_CGgsnGlobalErrorTypes_Object = MibScalar
cGgsnGlobalErrorTypes = _CGgsnGlobalErrorTypes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 5, 5),
    _CGgsnGlobalErrorTypes_Type()
)
cGgsnGlobalErrorTypes.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cGgsnGlobalErrorTypes.setStatus("current")


class _CGgsnAccessPointErrorTypes_Type(Integer32):
    """Custom type cGgsnAccessPointErrorTypes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("apnUnreachable", 3),
          ("ipAllocationFail", 2),
          ("noRadius", 1))
    )


_CGgsnAccessPointErrorTypes_Type.__name__ = "Integer32"
_CGgsnAccessPointErrorTypes_Object = MibScalar
cGgsnAccessPointErrorTypes = _CGgsnAccessPointErrorTypes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 5, 6),
    _CGgsnAccessPointErrorTypes_Type()
)
cGgsnAccessPointErrorTypes.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cGgsnAccessPointErrorTypes.setStatus("current")


class _CGgsnPacketDataProtoErrorTypes_Type(Integer32):
    """Custom type cGgsnPacketDataProtoErrorTypes based on Integer32"""
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
        *(("authenticationFail", 2),
          ("ccrInitFail", 3),
          ("noResource", 1),
          ("quotaPushFail", 4))
    )


_CGgsnPacketDataProtoErrorTypes_Type.__name__ = "Integer32"
_CGgsnPacketDataProtoErrorTypes_Object = MibScalar
cGgsnPacketDataProtoErrorTypes = _CGgsnPacketDataProtoErrorTypes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 5, 7),
    _CGgsnPacketDataProtoErrorTypes_Type()
)
cGgsnPacketDataProtoErrorTypes.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cGgsnPacketDataProtoErrorTypes.setStatus("current")
_CGgsnNotifPdpMsisdn_Type = SnmpAdminString
_CGgsnNotifPdpMsisdn_Object = MibScalar
cGgsnNotifPdpMsisdn = _CGgsnNotifPdpMsisdn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 1, 5, 8),
    _CGgsnNotifPdpMsisdn_Type()
)
cGgsnNotifPdpMsisdn.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cGgsnNotifPdpMsisdn.setStatus("current")
_CGgsnNotifPrefix_ObjectIdentity = ObjectIdentity
cGgsnNotifPrefix = _CGgsnNotifPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 2)
)
_CGgsnNotifications_ObjectIdentity = ObjectIdentity
cGgsnNotifications = _CGgsnNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 2, 0)
)
_CGgsnMIBConformances_ObjectIdentity = ObjectIdentity
cGgsnMIBConformances = _CGgsnMIBConformances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 3)
)
_CGgsnMIBCompliances_ObjectIdentity = ObjectIdentity
cGgsnMIBCompliances = _CGgsnMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 3, 1)
)
_CGgsnMIBGroups_ObjectIdentity = ObjectIdentity
cGgsnMIBGroups = _CGgsnMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 3, 2)
)

# Managed Objects groups

cGgsnStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 3, 2, 1)
)
cGgsnStatisticsGroup.setObjects(
      *(("CISCO-GGSN-MIB", "cGgsnSentSigMessages"),
        ("CISCO-GGSN-MIB", "cGgsnReceivedSigMessages"),
        ("CISCO-GGSN-MIB", "cGgsnUnexpectedSigMessages"),
        ("CISCO-GGSN-MIB", "cGgsnSentGPDUs"),
        ("CISCO-GGSN-MIB", "cGgsnReceivedGPDUs"),
        ("CISCO-GGSN-MIB", "cGgsnSentGPDUOctets"),
        ("CISCO-GGSN-MIB", "cGgsnReceivedGPDUOctets"),
        ("CISCO-GGSN-MIB", "cGgsnUnexpectedGPDUs"),
        ("CISCO-GGSN-MIB", "cGgsnActivationRejectedPdps"),
        ("CISCO-GGSN-MIB", "cGgsnOutOfResourcePdps"),
        ("CISCO-GGSN-MIB", "cGgsnParserErrorMessages"),
        ("CISCO-GGSN-MIB", "cGgsnTotalCreatedPdps"),
        ("CISCO-GGSN-MIB", "cGgsnTotalDeletedPdps"),
        ("CISCO-GGSN-MIB", "cGgsnTotalNetworkInitPdps"),
        ("CISCO-GGSN-MIB", "cGgsnTotalPppPdpsCreated"),
        ("CISCO-GGSN-MIB", "cGgsnTotalPppPdpsDeleted"),
        ("CISCO-GGSN-MIB", "cGgsnOutOfResourcePppRegenPdps"),
        ("CISCO-GGSN-MIB", "cGgsnDroppedPppRegenPdps"))
)
if mibBuilder.loadTexts:
    cGgsnStatisticsGroup.setStatus("deprecated")

cGgsnNotifMgmtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 3, 2, 2)
)
cGgsnNotifMgmtGroup.setObjects(
      *(("CISCO-GGSN-MIB", "cGgsnNotifEnabled"),
        ("CISCO-GGSN-MIB", "cGgsnNotifLeastSeverLevel"),
        ("CISCO-GGSN-MIB", "cGgsnGeneratedNotifs"),
        ("CISCO-GGSN-MIB", "cGgsnIgnoredAlarms"),
        ("CISCO-GGSN-MIB", "cGgsnHistNotifMaxLength"),
        ("CISCO-GGSN-MIB", "cGgsnHistNotifLatestIndex"),
        ("CISCO-GGSN-MIB", "cGgsnHistNotifType"),
        ("CISCO-GGSN-MIB", "cGgsnHistNotifSeverity"),
        ("CISCO-GGSN-MIB", "cGgsnHistNotifTimestamp"),
        ("CISCO-GGSN-MIB", "cGgsnHistNotifGgsnIpAddrType"),
        ("CISCO-GGSN-MIB", "cGgsnHistNotifGgsnIpAddr"),
        ("CISCO-GGSN-MIB", "cGgsnHistNotifInfo"))
)
if mibBuilder.loadTexts:
    cGgsnNotifMgmtGroup.setStatus("deprecated")

cGgsnConfigurationsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 3, 2, 3)
)
cGgsnConfigurationsGroup.setObjects(
      *(("CISCO-GGSN-MIB", "cGgsnDefaultIpAllocationMethod"),
        ("CISCO-GGSN-MIB", "cGgsnIdlePdpPurgeTimer"),
        ("CISCO-GGSN-MIB", "cGgsnIpDupProtectRowStatus"),
        ("CISCO-GGSN-MIB", "cGgsnDefaultAggregRowStatus"),
        ("CISCO-GGSN-MIB", "cGgsnDefaultAaaAuthServerGroup"),
        ("CISCO-GGSN-MIB", "cGgsnDefaultAaaAccServerGroup"),
        ("CISCO-GGSN-MIB", "cGgsnPppVirtualTemplate"),
        ("CISCO-GGSN-MIB", "cGgsnPppRegenVirtualTemplate"))
)
if mibBuilder.loadTexts:
    cGgsnConfigurationsGroup.setStatus("deprecated")

cGgsnStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 3, 2, 5)
)
cGgsnStatusGroup.setObjects(
      *(("CISCO-GGSN-MIB", "cGgsnVersion"),
        ("CISCO-GGSN-MIB", "cGgsnActiveNetworkInitPdps"),
        ("CISCO-GGSN-MIB", "cGgsnActivePppPdps"),
        ("CISCO-GGSN-MIB", "cGgsnActivePppRegenPdps"),
        ("CISCO-GGSN-MIB", "cGgsnPendingPppRegenPdps"))
)
if mibBuilder.loadTexts:
    cGgsnStatusGroup.setStatus("deprecated")

cGgsnConfigurationsGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 3, 2, 6)
)
cGgsnConfigurationsGroupRev1.setObjects(
      *(("CISCO-GGSN-MIB", "cGgsnDefaultIpAllocationMethod"),
        ("CISCO-GGSN-MIB", "cGgsnIdlePdpPurgeTimer"),
        ("CISCO-GGSN-MIB", "cGgsnIpDupProtectRowStatus"),
        ("CISCO-GGSN-MIB", "cGgsnDefaultAggregRowStatus"),
        ("CISCO-GGSN-MIB", "cGgsnDefaultAaaAuthServerGroup"),
        ("CISCO-GGSN-MIB", "cGgsnDefaultAaaAccServerGroup"),
        ("CISCO-GGSN-MIB", "cGgsnPppVirtualTemplate"),
        ("CISCO-GGSN-MIB", "cGgsnPppRegenVirtualTemplate"),
        ("CISCO-GGSN-MIB", "cGgsnPlmnAddrRangeRowStatus"))
)
if mibBuilder.loadTexts:
    cGgsnConfigurationsGroupRev1.setStatus("deprecated")

cGgsnUmtsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 3, 2, 7)
)
cGgsnUmtsGroup.setObjects(
      *(("CISCO-GGSN-MIB", "cGgsnTftSemanticErrorPdps"),
        ("CISCO-GGSN-MIB", "cGgsnTftSyntacticErrorPdps"),
        ("CISCO-GGSN-MIB", "cGgsnPktFilterSemanticErrorPdps"),
        ("CISCO-GGSN-MIB", "cGgsnPktFilterSyntacticErrorPdps"),
        ("CISCO-GGSN-MIB", "cGgsnPlmnAddrRangeUsage"),
        ("CISCO-GGSN-MIB", "cGgsnActiveGtpVersion0Pdps"),
        ("CISCO-GGSN-MIB", "cGgsnActiveGtpVersion1Pdps"),
        ("CISCO-GGSN-MIB", "cGgsnGtpEncapInterface"))
)
if mibBuilder.loadTexts:
    cGgsnUmtsGroup.setStatus("current")

cGgsnStatisticsGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 3, 2, 8)
)
cGgsnStatisticsGroupRev1.setObjects(
      *(("CISCO-GGSN-MIB", "cGgsnSentSigMessages"),
        ("CISCO-GGSN-MIB", "cGgsnReceivedSigMessages"),
        ("CISCO-GGSN-MIB", "cGgsnUnexpectedSigMessages"),
        ("CISCO-GGSN-MIB", "cGgsnSentGPDUs"),
        ("CISCO-GGSN-MIB", "cGgsnReceivedGPDUs"),
        ("CISCO-GGSN-MIB", "cGgsnUnexpectedGPDUs"),
        ("CISCO-GGSN-MIB", "cGgsnActivationRejectedPdps"),
        ("CISCO-GGSN-MIB", "cGgsnOutOfResourcePdps"),
        ("CISCO-GGSN-MIB", "cGgsnParserErrorMessages"),
        ("CISCO-GGSN-MIB", "cGgsnTotalCreatedPdps"),
        ("CISCO-GGSN-MIB", "cGgsnTotalDeletedPdps"),
        ("CISCO-GGSN-MIB", "cGgsnTotalNetworkInitPdps"),
        ("CISCO-GGSN-MIB", "cGgsnTotalPppPdpsCreated"),
        ("CISCO-GGSN-MIB", "cGgsnTotalPppPdpsDeleted"),
        ("CISCO-GGSN-MIB", "cGgsnOutOfResourcePppRegenPdps"),
        ("CISCO-GGSN-MIB", "cGgsnDroppedPppRegenPdps"),
        ("CISCO-GGSN-MIB", "cGgsnHCSentGPDUOctets"),
        ("CISCO-GGSN-MIB", "cGgsnHCReceivedGPDUOctets"),
        ("CISCO-GGSN-MIB", "cGgsnVersionNotSupportedRejPdps"),
        ("CISCO-GGSN-MIB", "cGgsnUnkownMessageRejPdps"),
        ("CISCO-GGSN-MIB", "cGgsnMsgTooShortRejPdps"),
        ("CISCO-GGSN-MIB", "cGgsnMandIeMissingRejPdps"),
        ("CISCO-GGSN-MIB", "cGgsnMandIeIncorrectRejPdps"),
        ("CISCO-GGSN-MIB", "cGgsnOptIeInvalidRejPdps"),
        ("CISCO-GGSN-MIB", "cGgsnIeUnknownRejPdps"),
        ("CISCO-GGSN-MIB", "cGgsnIeOutOfOrderRejPdps"),
        ("CISCO-GGSN-MIB", "cGgsnIeUnexpectedRejPdps"),
        ("CISCO-GGSN-MIB", "cGgsnIeDuplicatedRejPdps"),
        ("CISCO-GGSN-MIB", "cGgsnOptIeIncorrectRejPdps"),
        ("CISCO-GGSN-MIB", "cGgsnPdpWithoutTftExistsRejPdps"),
        ("CISCO-GGSN-MIB", "cGgsnSgsnThruPutLastCollected"),
        ("CISCO-GGSN-MIB", "cGgsnSgsnUpStreamPktCnt"),
        ("CISCO-GGSN-MIB", "cGgsnSgsnUpStreamByteCnt"),
        ("CISCO-GGSN-MIB", "cGgsnSgsnDownStreamPktCnt"),
        ("CISCO-GGSN-MIB", "cGgsnSgsnDownStreamByteCnt"))
)
if mibBuilder.loadTexts:
    cGgsnStatisticsGroupRev1.setStatus("deprecated")

cGgsnConfigurationsGroupRev2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 3, 2, 10)
)
cGgsnConfigurationsGroupRev2.setObjects(
      *(("CISCO-GGSN-MIB", "cGgsnDefaultIpAllocationMethod"),
        ("CISCO-GGSN-MIB", "cGgsnIdlePdpPurgeTimer"),
        ("CISCO-GGSN-MIB", "cGgsnIpDupProtectRowStatus"),
        ("CISCO-GGSN-MIB", "cGgsnDefaultAggregRowStatus"),
        ("CISCO-GGSN-MIB", "cGgsnDefaultAaaAuthServerGroup"),
        ("CISCO-GGSN-MIB", "cGgsnDefaultAaaAccServerGroup"),
        ("CISCO-GGSN-MIB", "cGgsnPppVirtualTemplate"),
        ("CISCO-GGSN-MIB", "cGgsnPppRegenVirtualTemplate"),
        ("CISCO-GGSN-MIB", "cGgsnPlmnAddrRangeRowStatus"),
        ("CISCO-GGSN-MIB", "cGgsnPdfRowStatus"),
        ("CISCO-GGSN-MIB", "cGgsnPdfReconnectTimeOut"),
        ("CISCO-GGSN-MIB", "cGgsnPdfReconnectRetries"),
        ("CISCO-GGSN-MIB", "cGgsnPdfReconExpPdpDelete"),
        ("CISCO-GGSN-MIB", "cGgsnPdfReqRetryTimeOut"),
        ("CISCO-GGSN-MIB", "cGgsnPdfReqRetries"),
        ("CISCO-GGSN-MIB", "cGgsnPcscfRowStatus"),
        ("CISCO-GGSN-MIB", "cGgsnMemoryThreshold"),
        ("CISCO-GGSN-MIB", "cGgsnServiceMode"),
        ("CISCO-GGSN-MIB", "cGgsnPlmnRowStatus"),
        ("CISCO-GGSN-MIB", "cGgsnPlmnScope"),
        ("CISCO-GGSN-MIB", "cGgsnSessionTimeout"),
        ("CISCO-GGSN-MIB", "cGgsnThruputIntervalOne"),
        ("CISCO-GGSN-MIB", "cGgsnThruputIntervalTwo"),
        ("CISCO-GGSN-MIB", "cGgsnCompliance3GppGgsn"),
        ("CISCO-GGSN-MIB", "cGgsnCreateReqV1UpdExistPdp"),
        ("CISCO-GGSN-MIB", "cGgsnRadAttrSessTimeout"),
        ("CISCO-GGSN-MIB", "cGgsnDownlinkVerifyMsDisable"))
)
if mibBuilder.loadTexts:
    cGgsnConfigurationsGroupRev2.setStatus("deprecated")

cGgsnStatusGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 3, 2, 11)
)
cGgsnStatusGroupRev1.setObjects(
      *(("CISCO-GGSN-MIB", "cGgsnVersion"),
        ("CISCO-GGSN-MIB", "cGgsnActiveNetworkInitPdps"),
        ("CISCO-GGSN-MIB", "cGgsnActivePppPdps"),
        ("CISCO-GGSN-MIB", "cGgsnActivePppRegenPdps"),
        ("CISCO-GGSN-MIB", "cGgsnPendingPppRegenPdps"),
        ("CISCO-GGSN-MIB", "cGgsnServiceModeStatus"))
)
if mibBuilder.loadTexts:
    cGgsnStatusGroupRev1.setStatus("current")

cGgsnNotifInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 3, 2, 12)
)
cGgsnNotifInfoGroup.setObjects(
      *(("CISCO-GGSN-MIB", "cGgsnPdfServerAddrType"),
        ("CISCO-GGSN-MIB", "cGgsnPdfServerAddr"))
)
if mibBuilder.loadTexts:
    cGgsnNotifInfoGroup.setStatus("deprecated")

cGgsnNotifInfoGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 3, 2, 14)
)
cGgsnNotifInfoGroupRev1.setObjects(
      *(("CISCO-GGSN-MIB", "cGgsnPdfServerAddrType"),
        ("CISCO-GGSN-MIB", "cGgsnPdfServerAddr"),
        ("CISCO-GGSN-MIB", "cGgsnNotifAccessPointName"),
        ("CISCO-GGSN-MIB", "cGgsnNotifPdpImsi"),
        ("CISCO-GGSN-MIB", "cGgsnGlobalErrorTypes"),
        ("CISCO-GGSN-MIB", "cGgsnAccessPointErrorTypes"),
        ("CISCO-GGSN-MIB", "cGgsnPacketDataProtoErrorTypes"))
)
if mibBuilder.loadTexts:
    cGgsnNotifInfoGroupRev1.setStatus("deprecated")

cGgsnNotifMgmtGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 3, 2, 15)
)
cGgsnNotifMgmtGroupRev1.setObjects(
      *(("CISCO-GGSN-MIB", "cGgsnNotifLeastSeverLevel"),
        ("CISCO-GGSN-MIB", "cGgsnGeneratedNotifs"),
        ("CISCO-GGSN-MIB", "cGgsnIgnoredAlarms"),
        ("CISCO-GGSN-MIB", "cGgsnHistNotifMaxLength"),
        ("CISCO-GGSN-MIB", "cGgsnHistNotifLatestIndex"),
        ("CISCO-GGSN-MIB", "cGgsnHistNotifType"),
        ("CISCO-GGSN-MIB", "cGgsnHistNotifSeverity"),
        ("CISCO-GGSN-MIB", "cGgsnHistNotifTimestamp"),
        ("CISCO-GGSN-MIB", "cGgsnHistNotifGgsnIpAddrType"),
        ("CISCO-GGSN-MIB", "cGgsnHistNotifGgsnIpAddr"),
        ("CISCO-GGSN-MIB", "cGgsnHistNotifInfo"),
        ("CISCO-GGSN-MIB", "cGgsnServiceNotifEnabled"),
        ("CISCO-GGSN-MIB", "cGgsnMemoryNotifEnabled"),
        ("CISCO-GGSN-MIB", "cGgsnPdfNotifEnabled"),
        ("CISCO-GGSN-MIB", "cGgsnGlobalErrorNotifEnabled"),
        ("CISCO-GGSN-MIB", "cGgsnAccessPointNotifEnabled"),
        ("CISCO-GGSN-MIB", "cGgsnPdpNotifEnabled"))
)
if mibBuilder.loadTexts:
    cGgsnNotifMgmtGroupRev1.setStatus("deprecated")

cGgsnStatusGroupConfigVer = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 3, 2, 16)
)
cGgsnStatusGroupConfigVer.setObjects(
    ("CISCO-GGSN-MIB", "cGgsnConfigVersion")
)
if mibBuilder.loadTexts:
    cGgsnStatusGroupConfigVer.setStatus("current")

cGgsnConfigurationsGroupR60 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 3, 2, 17)
)
cGgsnConfigurationsGroupR60.setObjects(
      *(("CISCO-GGSN-MIB", "cGgsnSlbMode"),
        ("CISCO-GGSN-MIB", "cGgsnSlbNotif"),
        ("CISCO-GGSN-MIB", "cGgsnSlbVserRowStatus"),
        ("CISCO-GGSN-MIB", "cGgsnSlbVserNextHopAddrType"),
        ("CISCO-GGSN-MIB", "cGgsnSlbVserNextHopAddress"),
        ("CISCO-GGSN-MIB", "cGgsnSlbVserVrfName"))
)
if mibBuilder.loadTexts:
    cGgsnConfigurationsGroupR60.setStatus("deprecated")

cGgsnStatisticsGroupR60 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 3, 2, 18)
)
cGgsnStatisticsGroupR60.setObjects(
      *(("CISCO-GGSN-MIB", "cGgsnTotalMessages"),
        ("CISCO-GGSN-MIB", "cGgsnContextSetupMessages"),
        ("CISCO-GGSN-MIB", "cGgsnContextModifyMessages"),
        ("CISCO-GGSN-MIB", "cGgsnContextRemoveMessages"),
        ("CISCO-GGSN-MIB", "cGgsnPathSetupMessages"),
        ("CISCO-GGSN-MIB", "cGgsnPathModifyMessages"),
        ("CISCO-GGSN-MIB", "cGgsnPathRemoveMessages"),
        ("CISCO-GGSN-MIB", "cGgsnCGFReadyMessages"),
        ("CISCO-GGSN-MIB", "cGgsnCGFModifyMessages"),
        ("CISCO-GGSN-MIB", "cGgsnCGFRemoveMessages"),
        ("CISCO-GGSN-MIB", "cGgsnInternalStateMsgs"),
        ("CISCO-GGSN-MIB", "cGgsnSlbCacFailures"),
        ("CISCO-GGSN-MIB", "cGgsnSlbSessionFailures"))
)
if mibBuilder.loadTexts:
    cGgsnStatisticsGroupR60.setStatus("current")

cGgsnStatusGroupR60 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 3, 2, 19)
)
cGgsnStatusGroupR60.setObjects(
      *(("CISCO-GGSN-MIB", "cGgsnPrepaidPDPs"),
        ("CISCO-GGSN-MIB", "cGgsnPostpaidPDPs"))
)
if mibBuilder.loadTexts:
    cGgsnStatusGroupR60.setStatus("current")

cGgsnNotifInfoGroupR60 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 3, 2, 20)
)
cGgsnNotifInfoGroupR60.setObjects(
    ("CISCO-GGSN-MIB", "cGgsnNotifPdpMsisdn")
)
if mibBuilder.loadTexts:
    cGgsnNotifInfoGroupR60.setStatus("current")

cGgsnConfigurationsGroupR60Rev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 3, 2, 21)
)
cGgsnConfigurationsGroupR60Rev1.setObjects(
      *(("CISCO-GGSN-MIB", "cGgsnSlbMode"),
        ("CISCO-GGSN-MIB", "cGgsnSlbVserRowStatus"),
        ("CISCO-GGSN-MIB", "cGgsnSlbVserNextHopAddrType"),
        ("CISCO-GGSN-MIB", "cGgsnSlbVserNextHopAddress"),
        ("CISCO-GGSN-MIB", "cGgsnSlbVserVrfName"),
        ("CISCO-GGSN-MIB", "cGgsnSlbNotifyCacFailure"),
        ("CISCO-GGSN-MIB", "cGgsnSlbNotifySessionDeletion"))
)
if mibBuilder.loadTexts:
    cGgsnConfigurationsGroupR60Rev1.setStatus("current")

cGgsnStatisticsGroupRev2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 3, 2, 22)
)
cGgsnStatisticsGroupRev2.setObjects(
      *(("CISCO-GGSN-MIB", "cGgsnSentSigMessages"),
        ("CISCO-GGSN-MIB", "cGgsnReceivedSigMessages"),
        ("CISCO-GGSN-MIB", "cGgsnUnexpectedSigMessages"),
        ("CISCO-GGSN-MIB", "cGgsnSentGPDUs"),
        ("CISCO-GGSN-MIB", "cGgsnReceivedGPDUs"),
        ("CISCO-GGSN-MIB", "cGgsnUnexpectedGPDUs"),
        ("CISCO-GGSN-MIB", "cGgsnActivationRejectedPdps"),
        ("CISCO-GGSN-MIB", "cGgsnOutOfResourcePdps"),
        ("CISCO-GGSN-MIB", "cGgsnParserErrorMessages"),
        ("CISCO-GGSN-MIB", "cGgsnTotalCreatedPdps"),
        ("CISCO-GGSN-MIB", "cGgsnTotalDeletedPdps"),
        ("CISCO-GGSN-MIB", "cGgsnTotalNetworkInitPdps"),
        ("CISCO-GGSN-MIB", "cGgsnTotalPppPdpsCreated"),
        ("CISCO-GGSN-MIB", "cGgsnTotalPppPdpsDeleted"),
        ("CISCO-GGSN-MIB", "cGgsnOutOfResourcePppRegenPdps"),
        ("CISCO-GGSN-MIB", "cGgsnDroppedPppRegenPdps"),
        ("CISCO-GGSN-MIB", "cGgsnHCSentGPDUOctets"),
        ("CISCO-GGSN-MIB", "cGgsnHCReceivedGPDUOctets"),
        ("CISCO-GGSN-MIB", "cGgsnSgsnThruPutLastCollected"),
        ("CISCO-GGSN-MIB", "cGgsnSgsnUpStreamPktCnt"),
        ("CISCO-GGSN-MIB", "cGgsnSgsnUpStreamByteCnt"),
        ("CISCO-GGSN-MIB", "cGgsnSgsnDownStreamPktCnt"),
        ("CISCO-GGSN-MIB", "cGgsnSgsnDownStreamByteCnt"),
        ("CISCO-GGSN-MIB", "cGgsnTotalCreatedIpv6Pdps"),
        ("CISCO-GGSN-MIB", "cGgsnTotalDeletedIpv6Pdps"),
        ("CISCO-GGSN-MIB", "cGgsnTotalRejectedIpv6Pdps"),
        ("CISCO-GGSN-MIB", "cGgsnSentIpv6SigMessages"),
        ("CISCO-GGSN-MIB", "cGgsnReceivedIpv6SigMessages"),
        ("CISCO-GGSN-MIB", "cGgsnSentIpv6PDUs"),
        ("CISCO-GGSN-MIB", "cGgsnReceivedIpv6PDUs"),
        ("CISCO-GGSN-MIB", "cGgsnSentIpv6PDUOctets"),
        ("CISCO-GGSN-MIB", "cGgsnReceivedIpv6PDUOctets"),
        ("CISCO-GGSN-MIB", "cGgsnVersionNotSupportedMsgs"),
        ("CISCO-GGSN-MIB", "cGgsnUnkownGtpMsgs"),
        ("CISCO-GGSN-MIB", "cGgsnTooShortMsgs"),
        ("CISCO-GGSN-MIB", "cGgsnMandIeMissingMsgs"),
        ("CISCO-GGSN-MIB", "cGgsnMandIeIncorrectMsgs"),
        ("CISCO-GGSN-MIB", "cGgsnOptIeInvalidMsgs"),
        ("CISCO-GGSN-MIB", "cGgsnIeUnknownMsgs"),
        ("CISCO-GGSN-MIB", "cGgsnIeOutOfOrderMsgs"),
        ("CISCO-GGSN-MIB", "cGgsnIeUnexpectedMsgs"),
        ("CISCO-GGSN-MIB", "cGgsnIeDuplicatedMsgs"),
        ("CISCO-GGSN-MIB", "cGgsnOptIeIncorrectMsgs"),
        ("CISCO-GGSN-MIB", "cGgsnPdpWithoutTftExistsPdps"))
)
if mibBuilder.loadTexts:
    cGgsnStatisticsGroupRev2.setStatus("current")

cGgsnStatusGroupR70 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 3, 2, 23)
)
cGgsnStatusGroupR70.setObjects(
      *(("CISCO-GGSN-MIB", "cGgsnActivatedIpv6Gtpv0Pdp"),
        ("CISCO-GGSN-MIB", "cGgsnActivatedIpv6Gtpv1Pdp"),
        ("CISCO-GGSN-MIB", "cGgsnActivatedIpv6Ms"))
)
if mibBuilder.loadTexts:
    cGgsnStatusGroupR70.setStatus("current")

cGgsnConfigurationsGroupRev3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 3, 2, 24)
)
cGgsnConfigurationsGroupRev3.setObjects(
      *(("CISCO-GGSN-MIB", "cGgsnDefaultIpAllocationMethod"),
        ("CISCO-GGSN-MIB", "cGgsnIdlePdpPurgeTimer"),
        ("CISCO-GGSN-MIB", "cGgsnIpDupProtectRowStatus"),
        ("CISCO-GGSN-MIB", "cGgsnDefaultAggregRowStatus"),
        ("CISCO-GGSN-MIB", "cGgsnDefaultAaaAuthServerGroup"),
        ("CISCO-GGSN-MIB", "cGgsnDefaultAaaAccServerGroup"),
        ("CISCO-GGSN-MIB", "cGgsnPppVirtualTemplate"),
        ("CISCO-GGSN-MIB", "cGgsnPppRegenVirtualTemplate"),
        ("CISCO-GGSN-MIB", "cGgsnPlmnAddrRangeRowStatus"),
        ("CISCO-GGSN-MIB", "cGgsnPcscfRowStatus"),
        ("CISCO-GGSN-MIB", "cGgsnMemoryThreshold"),
        ("CISCO-GGSN-MIB", "cGgsnServiceMode"),
        ("CISCO-GGSN-MIB", "cGgsnPlmnRowStatus"),
        ("CISCO-GGSN-MIB", "cGgsnPlmnScope"),
        ("CISCO-GGSN-MIB", "cGgsnSessionTimeout"),
        ("CISCO-GGSN-MIB", "cGgsnThruputIntervalOne"),
        ("CISCO-GGSN-MIB", "cGgsnThruputIntervalTwo"),
        ("CISCO-GGSN-MIB", "cGgsnCompliance3GppGgsn"),
        ("CISCO-GGSN-MIB", "cGgsnRadAttrSessTimeout"),
        ("CISCO-GGSN-MIB", "cGgsnDownlinkVerifyMsDisable"))
)
if mibBuilder.loadTexts:
    cGgsnConfigurationsGroupRev3.setStatus("deprecated")

cGgsnNotifMgmtGroupRev2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 3, 2, 25)
)
cGgsnNotifMgmtGroupRev2.setObjects(
      *(("CISCO-GGSN-MIB", "cGgsnNotifLeastSeverLevel"),
        ("CISCO-GGSN-MIB", "cGgsnGeneratedNotifs"),
        ("CISCO-GGSN-MIB", "cGgsnIgnoredAlarms"),
        ("CISCO-GGSN-MIB", "cGgsnHistNotifMaxLength"),
        ("CISCO-GGSN-MIB", "cGgsnHistNotifLatestIndex"),
        ("CISCO-GGSN-MIB", "cGgsnHistNotifType"),
        ("CISCO-GGSN-MIB", "cGgsnHistNotifSeverity"),
        ("CISCO-GGSN-MIB", "cGgsnHistNotifTimestamp"),
        ("CISCO-GGSN-MIB", "cGgsnHistNotifGgsnIpAddrType"),
        ("CISCO-GGSN-MIB", "cGgsnHistNotifGgsnIpAddr"),
        ("CISCO-GGSN-MIB", "cGgsnHistNotifInfo"),
        ("CISCO-GGSN-MIB", "cGgsnServiceNotifEnabled"),
        ("CISCO-GGSN-MIB", "cGgsnMemoryNotifEnabled"),
        ("CISCO-GGSN-MIB", "cGgsnGlobalErrorNotifEnabled"),
        ("CISCO-GGSN-MIB", "cGgsnAccessPointNotifEnabled"),
        ("CISCO-GGSN-MIB", "cGgsnPdpNotifEnabled"))
)
if mibBuilder.loadTexts:
    cGgsnNotifMgmtGroupRev2.setStatus("current")

cGgsnNotifInfoGroupRev2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 3, 2, 27)
)
cGgsnNotifInfoGroupRev2.setObjects(
      *(("CISCO-GGSN-MIB", "cGgsnNotifAccessPointName"),
        ("CISCO-GGSN-MIB", "cGgsnNotifPdpImsi"),
        ("CISCO-GGSN-MIB", "cGgsnGlobalErrorTypes"),
        ("CISCO-GGSN-MIB", "cGgsnAccessPointErrorTypes"),
        ("CISCO-GGSN-MIB", "cGgsnPacketDataProtoErrorTypes"))
)
if mibBuilder.loadTexts:
    cGgsnNotifInfoGroupRev2.setStatus("current")

cGgsnConfigurationsGroupRev4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 3, 2, 28)
)
cGgsnConfigurationsGroupRev4.setObjects(
      *(("CISCO-GGSN-MIB", "cGgsnDefaultIpAllocationMethod"),
        ("CISCO-GGSN-MIB", "cGgsnIdlePdpPurgeTimer"),
        ("CISCO-GGSN-MIB", "cGgsnIpDupProtectRowStatus"),
        ("CISCO-GGSN-MIB", "cGgsnDefaultAggregRowStatus"),
        ("CISCO-GGSN-MIB", "cGgsnDefaultAaaAuthServerGroup"),
        ("CISCO-GGSN-MIB", "cGgsnDefaultAaaAccServerGroup"),
        ("CISCO-GGSN-MIB", "cGgsnPppVirtualTemplate"),
        ("CISCO-GGSN-MIB", "cGgsnPppRegenVirtualTemplate"),
        ("CISCO-GGSN-MIB", "cGgsnPlmnAddrRangeRowStatus"),
        ("CISCO-GGSN-MIB", "cGgsnPcscfRowStatus"),
        ("CISCO-GGSN-MIB", "cGgsnMemoryThreshold"),
        ("CISCO-GGSN-MIB", "cGgsnServiceMode"),
        ("CISCO-GGSN-MIB", "cGgsnPlmnRowStatus"),
        ("CISCO-GGSN-MIB", "cGgsnPlmnScope"),
        ("CISCO-GGSN-MIB", "cGgsnSessionTimeout"),
        ("CISCO-GGSN-MIB", "cGgsnThruputIntervalOne"),
        ("CISCO-GGSN-MIB", "cGgsnThruputIntervalTwo"),
        ("CISCO-GGSN-MIB", "cGgsnRadAttrSessTimeout"),
        ("CISCO-GGSN-MIB", "cGgsnDownlinkVerifyMsDisable"))
)
if mibBuilder.loadTexts:
    cGgsnConfigurationsGroupRev4.setStatus("current")

cGgsnStatusGroupR90 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 3, 2, 29)
)
cGgsnStatusGroupR90.setObjects(
    ("CISCO-GGSN-MIB", "cGgsnGtpEncapsuInterface")
)
if mibBuilder.loadTexts:
    cGgsnStatusGroupR90.setStatus("current")

cGgsnConfigurationsGroupSup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 3, 2, 30)
)
cGgsnConfigurationsGroupSup1.setObjects(
      *(("CISCO-GGSN-MIB", "cGgsnMsExcludeRangeStartIpv6Prefixlen"),
        ("CISCO-GGSN-MIB", "cGgsnMsExcludeRangeEndIpv6Prefixlen"),
        ("CISCO-GGSN-MIB", "cGgsnPlmnAddrRangeFirstIpv6Prefixlen"),
        ("CISCO-GGSN-MIB", "cGgsnPlmnAddrRangeLastIpv6Prefixlen"))
)
if mibBuilder.loadTexts:
    cGgsnConfigurationsGroupSup1.setStatus("current")


# Notification objects

cGgsnNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 2, 0, 1)
)
cGgsnNotification.setObjects(
      *(("CISCO-GGSN-MIB", "cGgsnHistNotifType"),
        ("CISCO-GGSN-MIB", "cGgsnHistNotifSeverity"),
        ("CISCO-GGSN-MIB", "cGgsnHistNotifTimestamp"),
        ("CISCO-GGSN-MIB", "cGgsnHistNotifGgsnIpAddrType"),
        ("CISCO-GGSN-MIB", "cGgsnHistNotifGgsnIpAddr"),
        ("CISCO-GGSN-MIB", "cGgsnHistNotifInfo"))
)
if mibBuilder.loadTexts:
    cGgsnNotification.setStatus(
        "deprecated"
    )

cGgsnInServiceNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 2, 0, 2)
)
if mibBuilder.loadTexts:
    cGgsnInServiceNotif.setStatus(
        "current"
    )

cGgsnMaintenanceNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 2, 0, 3)
)
if mibBuilder.loadTexts:
    cGgsnMaintenanceNotif.setStatus(
        "current"
    )

cGgsnMemThresholdReachedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 2, 0, 4)
)
if mibBuilder.loadTexts:
    cGgsnMemThresholdReachedNotif.setStatus(
        "current"
    )

cGgsnMemThresholdClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 2, 0, 5)
)
if mibBuilder.loadTexts:
    cGgsnMemThresholdClearedNotif.setStatus(
        "current"
    )

cGgsnPdfStateUpNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 2, 0, 6)
)
cGgsnPdfStateUpNotif.setObjects(
      *(("CISCO-GGSN-MIB", "cGgsnPdfServerAddrType"),
        ("CISCO-GGSN-MIB", "cGgsnPdfServerAddr"))
)
if mibBuilder.loadTexts:
    cGgsnPdfStateUpNotif.setStatus(
        "deprecated"
    )

cGgsnPdfStateDownNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 2, 0, 7)
)
cGgsnPdfStateDownNotif.setObjects(
      *(("CISCO-GGSN-MIB", "cGgsnPdfServerAddrType"),
        ("CISCO-GGSN-MIB", "cGgsnPdfServerAddr"))
)
if mibBuilder.loadTexts:
    cGgsnPdfStateDownNotif.setStatus(
        "deprecated"
    )

cGgsnGlobalErrorNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 2, 0, 8)
)
cGgsnGlobalErrorNotif.setObjects(
      *(("CISCO-GGSN-MIB", "cGgsnGlobalErrorTypes"),
        ("CISCO-GGSN-MIB", "cGgsnHistNotifSeverity"),
        ("CISCO-GGSN-MIB", "cGgsnHistNotifTimestamp"),
        ("CISCO-GGSN-MIB", "cGgsnHistNotifGgsnIpAddrType"),
        ("CISCO-GGSN-MIB", "cGgsnHistNotifGgsnIpAddr"),
        ("CISCO-GGSN-MIB", "cGgsnHistNotifInfo"))
)
if mibBuilder.loadTexts:
    cGgsnGlobalErrorNotif.setStatus(
        "current"
    )

cGgsnAccessPointNameNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 2, 0, 9)
)
cGgsnAccessPointNameNotif.setObjects(
      *(("CISCO-GGSN-MIB", "cGgsnAccessPointErrorTypes"),
        ("CISCO-GGSN-MIB", "cGgsnHistNotifSeverity"),
        ("CISCO-GGSN-MIB", "cGgsnHistNotifTimestamp"),
        ("CISCO-GGSN-MIB", "cGgsnHistNotifGgsnIpAddrType"),
        ("CISCO-GGSN-MIB", "cGgsnHistNotifGgsnIpAddr"),
        ("CISCO-GGSN-MIB", "cGgsnHistNotifInfo"),
        ("CISCO-GGSN-MIB", "cGgsnNotifAccessPointName"))
)
if mibBuilder.loadTexts:
    cGgsnAccessPointNameNotif.setStatus(
        "current"
    )

cGgsnPacketDataProtocolNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 2, 0, 10)
)
cGgsnPacketDataProtocolNotif.setObjects(
      *(("CISCO-GGSN-MIB", "cGgsnPacketDataProtoErrorTypes"),
        ("CISCO-GGSN-MIB", "cGgsnHistNotifSeverity"),
        ("CISCO-GGSN-MIB", "cGgsnHistNotifTimestamp"),
        ("CISCO-GGSN-MIB", "cGgsnHistNotifGgsnIpAddrType"),
        ("CISCO-GGSN-MIB", "cGgsnHistNotifGgsnIpAddr"),
        ("CISCO-GGSN-MIB", "cGgsnHistNotifInfo"),
        ("CISCO-GGSN-MIB", "cGgsnNotifPdpImsi"),
        ("CISCO-GGSN-MIB", "cGgsnNotifPdpMsisdn"),
        ("CISCO-GGSN-MIB", "cGgsnNotifAccessPointName"))
)
if mibBuilder.loadTexts:
    cGgsnPacketDataProtocolNotif.setStatus(
        "current"
    )


# Notifications groups

cGgsnNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 3, 2, 4)
)
cGgsnNotifGroup.setObjects(
    ("CISCO-GGSN-MIB", "cGgsnNotification")
)
if mibBuilder.loadTexts:
    cGgsnNotifGroup.setStatus(
        "deprecated"
    )

cGgsnNotifGroupRev1 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 3, 2, 9)
)
cGgsnNotifGroupRev1.setObjects(
      *(("CISCO-GGSN-MIB", "cGgsnNotification"),
        ("CISCO-GGSN-MIB", "cGgsnInServiceNotif"),
        ("CISCO-GGSN-MIB", "cGgsnMaintenanceNotif"),
        ("CISCO-GGSN-MIB", "cGgsnMemThresholdReachedNotif"),
        ("CISCO-GGSN-MIB", "cGgsnMemThresholdClearedNotif"),
        ("CISCO-GGSN-MIB", "cGgsnPdfStateUpNotif"),
        ("CISCO-GGSN-MIB", "cGgsnPdfStateDownNotif"))
)
if mibBuilder.loadTexts:
    cGgsnNotifGroupRev1.setStatus(
        "deprecated"
    )

cGgsnNotifGroupRev2 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 3, 2, 13)
)
cGgsnNotifGroupRev2.setObjects(
      *(("CISCO-GGSN-MIB", "cGgsnInServiceNotif"),
        ("CISCO-GGSN-MIB", "cGgsnMaintenanceNotif"),
        ("CISCO-GGSN-MIB", "cGgsnMemThresholdReachedNotif"),
        ("CISCO-GGSN-MIB", "cGgsnMemThresholdClearedNotif"),
        ("CISCO-GGSN-MIB", "cGgsnPdfStateUpNotif"),
        ("CISCO-GGSN-MIB", "cGgsnPdfStateDownNotif"),
        ("CISCO-GGSN-MIB", "cGgsnGlobalErrorNotif"),
        ("CISCO-GGSN-MIB", "cGgsnAccessPointNameNotif"),
        ("CISCO-GGSN-MIB", "cGgsnPacketDataProtocolNotif"))
)
if mibBuilder.loadTexts:
    cGgsnNotifGroupRev2.setStatus(
        "deprecated"
    )

cGgsnNotifGroupRev3 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 3, 2, 26)
)
cGgsnNotifGroupRev3.setObjects(
      *(("CISCO-GGSN-MIB", "cGgsnInServiceNotif"),
        ("CISCO-GGSN-MIB", "cGgsnMaintenanceNotif"),
        ("CISCO-GGSN-MIB", "cGgsnMemThresholdReachedNotif"),
        ("CISCO-GGSN-MIB", "cGgsnMemThresholdClearedNotif"),
        ("CISCO-GGSN-MIB", "cGgsnGlobalErrorNotif"),
        ("CISCO-GGSN-MIB", "cGgsnAccessPointNameNotif"),
        ("CISCO-GGSN-MIB", "cGgsnPacketDataProtocolNotif"))
)
if mibBuilder.loadTexts:
    cGgsnNotifGroupRev3.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

cGgsnMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 3, 1, 1)
)
if mibBuilder.loadTexts:
    cGgsnMIBCompliance.setStatus(
        "obsolete"
    )

cGgsnMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 3, 1, 2)
)
if mibBuilder.loadTexts:
    cGgsnMIBComplianceRev1.setStatus(
        "deprecated"
    )

cGgsnMIBComplianceRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 3, 1, 3)
)
if mibBuilder.loadTexts:
    cGgsnMIBComplianceRev2.setStatus(
        "deprecated"
    )

cGgsnMIBComplianceRev3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 3, 1, 4)
)
if mibBuilder.loadTexts:
    cGgsnMIBComplianceRev3.setStatus(
        "deprecated"
    )

cGgsnMIBComplianceRev4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 3, 1, 5)
)
if mibBuilder.loadTexts:
    cGgsnMIBComplianceRev4.setStatus(
        "deprecated"
    )

cGgsnMIBComplianceRev5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 3, 1, 6)
)
if mibBuilder.loadTexts:
    cGgsnMIBComplianceRev5.setStatus(
        "deprecated"
    )

cGgsnMIBComplianceRev6 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 3, 1, 7)
)
if mibBuilder.loadTexts:
    cGgsnMIBComplianceRev6.setStatus(
        "deprecated"
    )

cGgsnMIBComplianceRev7 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 3, 1, 8)
)
if mibBuilder.loadTexts:
    cGgsnMIBComplianceRev7.setStatus(
        "deprecated"
    )

cGgsnMIBComplianceRev8 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 3, 1, 9)
)
if mibBuilder.loadTexts:
    cGgsnMIBComplianceRev8.setStatus(
        "deprecated"
    )

cGgsnMIBComplianceRev9 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 3, 1, 10)
)
if mibBuilder.loadTexts:
    cGgsnMIBComplianceRev9.setStatus(
        "deprecated"
    )

cGgsnMIBComplianceRev10 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 240, 3, 1, 11)
)
if mibBuilder.loadTexts:
    cGgsnMIBComplianceRev10.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-GGSN-MIB",
    **{"cGgsnMIB": cGgsnMIB,
       "cGgsnMIBObjects": cGgsnMIBObjects,
       "cGgsnStatistics": cGgsnStatistics,
       "cGgsnSentSigMessages": cGgsnSentSigMessages,
       "cGgsnReceivedSigMessages": cGgsnReceivedSigMessages,
       "cGgsnUnexpectedSigMessages": cGgsnUnexpectedSigMessages,
       "cGgsnSentGPDUs": cGgsnSentGPDUs,
       "cGgsnReceivedGPDUs": cGgsnReceivedGPDUs,
       "cGgsnSentGPDUOctets": cGgsnSentGPDUOctets,
       "cGgsnReceivedGPDUOctets": cGgsnReceivedGPDUOctets,
       "cGgsnUnexpectedGPDUs": cGgsnUnexpectedGPDUs,
       "cGgsnActivationRejectedPdps": cGgsnActivationRejectedPdps,
       "cGgsnOutOfResourcePdps": cGgsnOutOfResourcePdps,
       "cGgsnParserErrorMessages": cGgsnParserErrorMessages,
       "cGgsnTotalCreatedPdps": cGgsnTotalCreatedPdps,
       "cGgsnTotalDeletedPdps": cGgsnTotalDeletedPdps,
       "cGgsnTotalNetworkInitPdps": cGgsnTotalNetworkInitPdps,
       "cGgsnTotalPppPdpsCreated": cGgsnTotalPppPdpsCreated,
       "cGgsnTotalPppPdpsDeleted": cGgsnTotalPppPdpsDeleted,
       "cGgsnOutOfResourcePppRegenPdps": cGgsnOutOfResourcePppRegenPdps,
       "cGgsnDroppedPppRegenPdps": cGgsnDroppedPppRegenPdps,
       "cGgsnTftSemanticErrorPdps": cGgsnTftSemanticErrorPdps,
       "cGgsnTftSyntacticErrorPdps": cGgsnTftSyntacticErrorPdps,
       "cGgsnPktFilterSemanticErrorPdps": cGgsnPktFilterSemanticErrorPdps,
       "cGgsnPktFilterSyntacticErrorPdps": cGgsnPktFilterSyntacticErrorPdps,
       "cGgsnHCSentGPDUOctets": cGgsnHCSentGPDUOctets,
       "cGgsnHCReceivedGPDUOctets": cGgsnHCReceivedGPDUOctets,
       "cGgsnPdpsRejStatistics": cGgsnPdpsRejStatistics,
       "cGgsnVersionNotSupportedRejPdps": cGgsnVersionNotSupportedRejPdps,
       "cGgsnUnkownMessageRejPdps": cGgsnUnkownMessageRejPdps,
       "cGgsnMsgTooShortRejPdps": cGgsnMsgTooShortRejPdps,
       "cGgsnMandIeMissingRejPdps": cGgsnMandIeMissingRejPdps,
       "cGgsnMandIeIncorrectRejPdps": cGgsnMandIeIncorrectRejPdps,
       "cGgsnOptIeInvalidRejPdps": cGgsnOptIeInvalidRejPdps,
       "cGgsnIeUnknownRejPdps": cGgsnIeUnknownRejPdps,
       "cGgsnIeOutOfOrderRejPdps": cGgsnIeOutOfOrderRejPdps,
       "cGgsnIeUnexpectedRejPdps": cGgsnIeUnexpectedRejPdps,
       "cGgsnIeDuplicatedRejPdps": cGgsnIeDuplicatedRejPdps,
       "cGgsnOptIeIncorrectRejPdps": cGgsnOptIeIncorrectRejPdps,
       "cGgsnPdpWithoutTftExistsRejPdps": cGgsnPdpWithoutTftExistsRejPdps,
       "cGgsnSgsnStatTable": cGgsnSgsnStatTable,
       "cGgsnSgsnStatEntry": cGgsnSgsnStatEntry,
       "cGgsnSgsnThruPutInterval": cGgsnSgsnThruPutInterval,
       "cGgsnSgsnThruPutLastCollected": cGgsnSgsnThruPutLastCollected,
       "cGgsnSgsnUpStreamPktCnt": cGgsnSgsnUpStreamPktCnt,
       "cGgsnSgsnUpStreamByteCnt": cGgsnSgsnUpStreamByteCnt,
       "cGgsnSgsnDownStreamPktCnt": cGgsnSgsnDownStreamPktCnt,
       "cGgsnSgsnDownStreamByteCnt": cGgsnSgsnDownStreamByteCnt,
       "cGgsnRedundancyStatistics": cGgsnRedundancyStatistics,
       "cGgsnTotalMessages": cGgsnTotalMessages,
       "cGgsnContextSetupMessages": cGgsnContextSetupMessages,
       "cGgsnContextModifyMessages": cGgsnContextModifyMessages,
       "cGgsnContextRemoveMessages": cGgsnContextRemoveMessages,
       "cGgsnPathSetupMessages": cGgsnPathSetupMessages,
       "cGgsnPathModifyMessages": cGgsnPathModifyMessages,
       "cGgsnPathRemoveMessages": cGgsnPathRemoveMessages,
       "cGgsnCGFReadyMessages": cGgsnCGFReadyMessages,
       "cGgsnCGFModifyMessages": cGgsnCGFModifyMessages,
       "cGgsnCGFRemoveMessages": cGgsnCGFRemoveMessages,
       "cGgsnInternalStateMsgs": cGgsnInternalStateMsgs,
       "cGgsnSlbCacFailures": cGgsnSlbCacFailures,
       "cGgsnSlbSessionFailures": cGgsnSlbSessionFailures,
       "cGgsnTotalCreatedIpv6Pdps": cGgsnTotalCreatedIpv6Pdps,
       "cGgsnTotalDeletedIpv6Pdps": cGgsnTotalDeletedIpv6Pdps,
       "cGgsnTotalRejectedIpv6Pdps": cGgsnTotalRejectedIpv6Pdps,
       "cGgsnSentIpv6SigMessages": cGgsnSentIpv6SigMessages,
       "cGgsnReceivedIpv6SigMessages": cGgsnReceivedIpv6SigMessages,
       "cGgsnSentIpv6PDUs": cGgsnSentIpv6PDUs,
       "cGgsnReceivedIpv6PDUs": cGgsnReceivedIpv6PDUs,
       "cGgsnSentIpv6PDUOctets": cGgsnSentIpv6PDUOctets,
       "cGgsnReceivedIpv6PDUOctets": cGgsnReceivedIpv6PDUOctets,
       "cGgsnVersionNotSupportedMsgs": cGgsnVersionNotSupportedMsgs,
       "cGgsnUnkownGtpMsgs": cGgsnUnkownGtpMsgs,
       "cGgsnTooShortMsgs": cGgsnTooShortMsgs,
       "cGgsnMandIeMissingMsgs": cGgsnMandIeMissingMsgs,
       "cGgsnMandIeIncorrectMsgs": cGgsnMandIeIncorrectMsgs,
       "cGgsnOptIeInvalidMsgs": cGgsnOptIeInvalidMsgs,
       "cGgsnIeUnknownMsgs": cGgsnIeUnknownMsgs,
       "cGgsnIeOutOfOrderMsgs": cGgsnIeOutOfOrderMsgs,
       "cGgsnIeUnexpectedMsgs": cGgsnIeUnexpectedMsgs,
       "cGgsnIeDuplicatedMsgs": cGgsnIeDuplicatedMsgs,
       "cGgsnOptIeIncorrectMsgs": cGgsnOptIeIncorrectMsgs,
       "cGgsnPdpWithoutTftExistsPdps": cGgsnPdpWithoutTftExistsPdps,
       "cGgsnNotifMgmt": cGgsnNotifMgmt,
       "cGgsnNotifEnabled": cGgsnNotifEnabled,
       "cGgsnNotifLeastSeverLevel": cGgsnNotifLeastSeverLevel,
       "cGgsnGeneratedNotifs": cGgsnGeneratedNotifs,
       "cGgsnIgnoredAlarms": cGgsnIgnoredAlarms,
       "cGgsnHistNotifMaxLength": cGgsnHistNotifMaxLength,
       "cGgsnHistNotifLatestIndex": cGgsnHistNotifLatestIndex,
       "cGgsnHistNotifTable": cGgsnHistNotifTable,
       "cGgsnHistNotifEntry": cGgsnHistNotifEntry,
       "cGgsnHistNotifIndex": cGgsnHistNotifIndex,
       "cGgsnHistNotifType": cGgsnHistNotifType,
       "cGgsnHistNotifSeverity": cGgsnHistNotifSeverity,
       "cGgsnHistNotifTimestamp": cGgsnHistNotifTimestamp,
       "cGgsnHistNotifGgsnIpAddrType": cGgsnHistNotifGgsnIpAddrType,
       "cGgsnHistNotifGgsnIpAddr": cGgsnHistNotifGgsnIpAddr,
       "cGgsnHistNotifInfo": cGgsnHistNotifInfo,
       "cGgsnServiceNotifEnabled": cGgsnServiceNotifEnabled,
       "cGgsnMemoryNotifEnabled": cGgsnMemoryNotifEnabled,
       "cGgsnPdfNotifEnabled": cGgsnPdfNotifEnabled,
       "cGgsnGlobalErrorNotifEnabled": cGgsnGlobalErrorNotifEnabled,
       "cGgsnAccessPointNotifEnabled": cGgsnAccessPointNotifEnabled,
       "cGgsnPdpNotifEnabled": cGgsnPdpNotifEnabled,
       "cGgsnConfigurations": cGgsnConfigurations,
       "cGgsnDefaultIpAllocationMethod": cGgsnDefaultIpAllocationMethod,
       "cGgsnIdlePdpPurgeTimer": cGgsnIdlePdpPurgeTimer,
       "cGgsnIpDupProtectTable": cGgsnIpDupProtectTable,
       "cGgsnIpDupProtectEntry": cGgsnIpDupProtectEntry,
       "cGgsnMsExcludeRangeStartIpType": cGgsnMsExcludeRangeStartIpType,
       "cGgsnMsExcludeRangeStartIp": cGgsnMsExcludeRangeStartIp,
       "cGgsnMsExcludeRangeEndIpType": cGgsnMsExcludeRangeEndIpType,
       "cGgsnMsExcludeRangeEndIp": cGgsnMsExcludeRangeEndIp,
       "cGgsnIpDupProtectRowStatus": cGgsnIpDupProtectRowStatus,
       "cGgsnMsExcludeRangeStartIpv6Prefixlen": cGgsnMsExcludeRangeStartIpv6Prefixlen,
       "cGgsnMsExcludeRangeEndIpv6Prefixlen": cGgsnMsExcludeRangeEndIpv6Prefixlen,
       "cGgsnDefaultAggregTable": cGgsnDefaultAggregTable,
       "cGgsnDefaultAggregEntry": cGgsnDefaultAggregEntry,
       "cGgsnDefaultAggregIpAddrType": cGgsnDefaultAggregIpAddrType,
       "cGgsnDefaultAggregIpAddr": cGgsnDefaultAggregIpAddr,
       "cGgsnDefaultAggregIpMask": cGgsnDefaultAggregIpMask,
       "cGgsnDefaultAggregRowStatus": cGgsnDefaultAggregRowStatus,
       "cGgsnDefaultAaaAuthServerGroup": cGgsnDefaultAaaAuthServerGroup,
       "cGgsnDefaultAaaAccServerGroup": cGgsnDefaultAaaAccServerGroup,
       "cGgsnPppVirtualTemplate": cGgsnPppVirtualTemplate,
       "cGgsnPppRegenVirtualTemplate": cGgsnPppRegenVirtualTemplate,
       "cGgsnPlmnIpAddrRangeTable": cGgsnPlmnIpAddrRangeTable,
       "cGgsnPlmnIpAddrRangeEntry": cGgsnPlmnIpAddrRangeEntry,
       "cGgsnPlmnAddrRangeIpAddrType": cGgsnPlmnAddrRangeIpAddrType,
       "cGgsnPlmnAddrRangeFirstIp": cGgsnPlmnAddrRangeFirstIp,
       "cGgsnPlmnAddrRangeLastIp": cGgsnPlmnAddrRangeLastIp,
       "cGgsnPlmnAddrRangeRowStatus": cGgsnPlmnAddrRangeRowStatus,
       "cGgsnPlmnAddrRangeUsage": cGgsnPlmnAddrRangeUsage,
       "cGgsnPlmnAddrRangeFirstIpv6Prefixlen": cGgsnPlmnAddrRangeFirstIpv6Prefixlen,
       "cGgsnPlmnAddrRangeLastIpv6Prefixlen": cGgsnPlmnAddrRangeLastIpv6Prefixlen,
       "cGgsnImsConfigurations": cGgsnImsConfigurations,
       "cGgsnPdfTable": cGgsnPdfTable,
       "cGgsnPdfEntry": cGgsnPdfEntry,
       "cGgsnPdfGroupName": cGgsnPdfGroupName,
       "cGgsnPdfDomainName": cGgsnPdfDomainName,
       "cGgsnPdfIpAddressType": cGgsnPdfIpAddressType,
       "cGgsnPdfIpAddress": cGgsnPdfIpAddress,
       "cGgsnPdfRowStatus": cGgsnPdfRowStatus,
       "cGgsnPdfReconnectTimeOut": cGgsnPdfReconnectTimeOut,
       "cGgsnPdfReconnectRetries": cGgsnPdfReconnectRetries,
       "cGgsnPdfReconExpPdpDelete": cGgsnPdfReconExpPdpDelete,
       "cGgsnPdfReqRetryTimeOut": cGgsnPdfReqRetryTimeOut,
       "cGgsnPdfReqRetries": cGgsnPdfReqRetries,
       "cGgsnPcscfTable": cGgsnPcscfTable,
       "cGgsnPcscfEntry": cGgsnPcscfEntry,
       "cGgsnPcscfGroupName": cGgsnPcscfGroupName,
       "cGgsnPcscfIpAddressType": cGgsnPcscfIpAddressType,
       "cGgsnPcscfIpAddress": cGgsnPcscfIpAddress,
       "cGgsnPcscfRowStatus": cGgsnPcscfRowStatus,
       "cGgsnMemoryThreshold": cGgsnMemoryThreshold,
       "cGgsnServiceMode": cGgsnServiceMode,
       "cGgsnPlmnTable": cGgsnPlmnTable,
       "cGgsnPlmnEntry": cGgsnPlmnEntry,
       "cGgsnPlmnMcc": cGgsnPlmnMcc,
       "cGgsnPlmnMnc": cGgsnPlmnMnc,
       "cGgsnPlmnRowStatus": cGgsnPlmnRowStatus,
       "cGgsnPlmnScope": cGgsnPlmnScope,
       "cGgsnSessionTimeout": cGgsnSessionTimeout,
       "cGgsnThruputIntervalOne": cGgsnThruputIntervalOne,
       "cGgsnThruputIntervalTwo": cGgsnThruputIntervalTwo,
       "cGgsnCompliance3GppGgsn": cGgsnCompliance3GppGgsn,
       "cGgsnCreateReqV1UpdExistPdp": cGgsnCreateReqV1UpdExistPdp,
       "cGgsnRadAttrSessTimeout": cGgsnRadAttrSessTimeout,
       "cGgsnDownlinkVerifyMsDisable": cGgsnDownlinkVerifyMsDisable,
       "cGgsnSlbMode": cGgsnSlbMode,
       "cGgsnSlbNotif": cGgsnSlbNotif,
       "cGgsnSlbVserverTable": cGgsnSlbVserverTable,
       "cGgsnSlbVserverEntry": cGgsnSlbVserverEntry,
       "cGgsnSlbVserAddrType": cGgsnSlbVserAddrType,
       "cGgsnSlbVserAddress": cGgsnSlbVserAddress,
       "cGgsnSlbVserNextHopAddrType": cGgsnSlbVserNextHopAddrType,
       "cGgsnSlbVserNextHopAddress": cGgsnSlbVserNextHopAddress,
       "cGgsnSlbVserVrfName": cGgsnSlbVserVrfName,
       "cGgsnSlbVserRowStatus": cGgsnSlbVserRowStatus,
       "cGgsnSlbNotifyCacFailure": cGgsnSlbNotifyCacFailure,
       "cGgsnSlbNotifySessionDeletion": cGgsnSlbNotifySessionDeletion,
       "cGgsnStatus": cGgsnStatus,
       "cGgsnVersion": cGgsnVersion,
       "cGgsnActiveNetworkInitPdps": cGgsnActiveNetworkInitPdps,
       "cGgsnActivePppPdps": cGgsnActivePppPdps,
       "cGgsnActivePppRegenPdps": cGgsnActivePppRegenPdps,
       "cGgsnPendingPppRegenPdps": cGgsnPendingPppRegenPdps,
       "cGgsnActiveGtpVersion0Pdps": cGgsnActiveGtpVersion0Pdps,
       "cGgsnActiveGtpVersion1Pdps": cGgsnActiveGtpVersion1Pdps,
       "cGgsnGtpEncapInterface": cGgsnGtpEncapInterface,
       "cGgsnServiceModeStatus": cGgsnServiceModeStatus,
       "cGgsnConfigVersion": cGgsnConfigVersion,
       "cGgsnPrepaidPDPs": cGgsnPrepaidPDPs,
       "cGgsnPostpaidPDPs": cGgsnPostpaidPDPs,
       "cGgsnActivatedIpv6Gtpv0Pdp": cGgsnActivatedIpv6Gtpv0Pdp,
       "cGgsnActivatedIpv6Gtpv1Pdp": cGgsnActivatedIpv6Gtpv1Pdp,
       "cGgsnActivatedIpv6Ms": cGgsnActivatedIpv6Ms,
       "cGgsnGtpEncapsuTable": cGgsnGtpEncapsuTable,
       "cGgsnGtpEncapsuEntry": cGgsnGtpEncapsuEntry,
       "cGgsnGtpEncapsuInterface": cGgsnGtpEncapsuInterface,
       "cGgsnNotifInfo": cGgsnNotifInfo,
       "cGgsnPdfServerAddrType": cGgsnPdfServerAddrType,
       "cGgsnPdfServerAddr": cGgsnPdfServerAddr,
       "cGgsnNotifAccessPointName": cGgsnNotifAccessPointName,
       "cGgsnNotifPdpImsi": cGgsnNotifPdpImsi,
       "cGgsnGlobalErrorTypes": cGgsnGlobalErrorTypes,
       "cGgsnAccessPointErrorTypes": cGgsnAccessPointErrorTypes,
       "cGgsnPacketDataProtoErrorTypes": cGgsnPacketDataProtoErrorTypes,
       "cGgsnNotifPdpMsisdn": cGgsnNotifPdpMsisdn,
       "cGgsnNotifPrefix": cGgsnNotifPrefix,
       "cGgsnNotifications": cGgsnNotifications,
       "cGgsnNotification": cGgsnNotification,
       "cGgsnInServiceNotif": cGgsnInServiceNotif,
       "cGgsnMaintenanceNotif": cGgsnMaintenanceNotif,
       "cGgsnMemThresholdReachedNotif": cGgsnMemThresholdReachedNotif,
       "cGgsnMemThresholdClearedNotif": cGgsnMemThresholdClearedNotif,
       "cGgsnPdfStateUpNotif": cGgsnPdfStateUpNotif,
       "cGgsnPdfStateDownNotif": cGgsnPdfStateDownNotif,
       "cGgsnGlobalErrorNotif": cGgsnGlobalErrorNotif,
       "cGgsnAccessPointNameNotif": cGgsnAccessPointNameNotif,
       "cGgsnPacketDataProtocolNotif": cGgsnPacketDataProtocolNotif,
       "cGgsnMIBConformances": cGgsnMIBConformances,
       "cGgsnMIBCompliances": cGgsnMIBCompliances,
       "cGgsnMIBCompliance": cGgsnMIBCompliance,
       "cGgsnMIBComplianceRev1": cGgsnMIBComplianceRev1,
       "cGgsnMIBComplianceRev2": cGgsnMIBComplianceRev2,
       "cGgsnMIBComplianceRev3": cGgsnMIBComplianceRev3,
       "cGgsnMIBComplianceRev4": cGgsnMIBComplianceRev4,
       "cGgsnMIBComplianceRev5": cGgsnMIBComplianceRev5,
       "cGgsnMIBComplianceRev6": cGgsnMIBComplianceRev6,
       "cGgsnMIBComplianceRev7": cGgsnMIBComplianceRev7,
       "cGgsnMIBComplianceRev8": cGgsnMIBComplianceRev8,
       "cGgsnMIBComplianceRev9": cGgsnMIBComplianceRev9,
       "cGgsnMIBComplianceRev10": cGgsnMIBComplianceRev10,
       "cGgsnMIBGroups": cGgsnMIBGroups,
       "cGgsnStatisticsGroup": cGgsnStatisticsGroup,
       "cGgsnNotifMgmtGroup": cGgsnNotifMgmtGroup,
       "cGgsnConfigurationsGroup": cGgsnConfigurationsGroup,
       "cGgsnNotifGroup": cGgsnNotifGroup,
       "cGgsnStatusGroup": cGgsnStatusGroup,
       "cGgsnConfigurationsGroupRev1": cGgsnConfigurationsGroupRev1,
       "cGgsnUmtsGroup": cGgsnUmtsGroup,
       "cGgsnStatisticsGroupRev1": cGgsnStatisticsGroupRev1,
       "cGgsnNotifGroupRev1": cGgsnNotifGroupRev1,
       "cGgsnConfigurationsGroupRev2": cGgsnConfigurationsGroupRev2,
       "cGgsnStatusGroupRev1": cGgsnStatusGroupRev1,
       "cGgsnNotifInfoGroup": cGgsnNotifInfoGroup,
       "cGgsnNotifGroupRev2": cGgsnNotifGroupRev2,
       "cGgsnNotifInfoGroupRev1": cGgsnNotifInfoGroupRev1,
       "cGgsnNotifMgmtGroupRev1": cGgsnNotifMgmtGroupRev1,
       "cGgsnStatusGroupConfigVer": cGgsnStatusGroupConfigVer,
       "cGgsnConfigurationsGroupR60": cGgsnConfigurationsGroupR60,
       "cGgsnStatisticsGroupR60": cGgsnStatisticsGroupR60,
       "cGgsnStatusGroupR60": cGgsnStatusGroupR60,
       "cGgsnNotifInfoGroupR60": cGgsnNotifInfoGroupR60,
       "cGgsnConfigurationsGroupR60Rev1": cGgsnConfigurationsGroupR60Rev1,
       "cGgsnStatisticsGroupRev2": cGgsnStatisticsGroupRev2,
       "cGgsnStatusGroupR70": cGgsnStatusGroupR70,
       "cGgsnConfigurationsGroupRev3": cGgsnConfigurationsGroupRev3,
       "cGgsnNotifMgmtGroupRev2": cGgsnNotifMgmtGroupRev2,
       "cGgsnNotifGroupRev3": cGgsnNotifGroupRev3,
       "cGgsnNotifInfoGroupRev2": cGgsnNotifInfoGroupRev2,
       "cGgsnConfigurationsGroupRev4": cGgsnConfigurationsGroupRev4,
       "cGgsnStatusGroupR90": cGgsnStatusGroupR90,
       "cGgsnConfigurationsGroupSup1": cGgsnConfigurationsGroupSup1}
)
