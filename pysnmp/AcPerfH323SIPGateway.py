# SNMP MIB module (AcPerfH323SIPGateway) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/AcPerfH323SIPGateway
# Produced by pysmi-1.5.4 at Mon Oct 14 20:45:02 2024
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

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

acPerfH323SIPGateway = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 10, 3)
)
acPerfH323SIPGateway.setRevisions(
        ("2003-11-20 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AudioCodes_ObjectIdentity = ObjectIdentity
audioCodes = _AudioCodes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003)
)
_AcRegistrations_ObjectIdentity = ObjectIdentity
acRegistrations = _AcRegistrations_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 7)
)
_AcGeneric_ObjectIdentity = ObjectIdentity
acGeneric = _AcGeneric_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8)
)
_AcProducts_ObjectIdentity = ObjectIdentity
acProducts = _AcProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9)
)
_AcPerformance_ObjectIdentity = ObjectIdentity
acPerformance = _AcPerformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 10)
)
_AcPerfH323SIPGWCommon_ObjectIdentity = ObjectIdentity
acPerfH323SIPGWCommon = _AcPerfH323SIPGWCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 10, 3, 1)
)
_AcPerfH323SIPGWCalls_ObjectIdentity = ObjectIdentity
acPerfH323SIPGWCalls = _AcPerfH323SIPGWCalls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 10, 3, 1, 1)
)
_AcPerfTel2IP_ObjectIdentity = ObjectIdentity
acPerfTel2IP = _AcPerfTel2IP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 10, 3, 1, 1, 1)
)
_AcPerfTel2IPAttemptedCalls_Type = Counter32
_AcPerfTel2IPAttemptedCalls_Object = MibScalar
acPerfTel2IPAttemptedCalls = _AcPerfTel2IPAttemptedCalls_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 3, 1, 1, 1, 1),
    _AcPerfTel2IPAttemptedCalls_Type()
)
acPerfTel2IPAttemptedCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPerfTel2IPAttemptedCalls.setStatus("current")
_AcPerfTel2IPEstablishedCalls_Type = Counter32
_AcPerfTel2IPEstablishedCalls_Object = MibScalar
acPerfTel2IPEstablishedCalls = _AcPerfTel2IPEstablishedCalls_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 3, 1, 1, 1, 2),
    _AcPerfTel2IPEstablishedCalls_Type()
)
acPerfTel2IPEstablishedCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPerfTel2IPEstablishedCalls.setStatus("current")
_AcPerfTel2IPBusyCalls_Type = Counter32
_AcPerfTel2IPBusyCalls_Object = MibScalar
acPerfTel2IPBusyCalls = _AcPerfTel2IPBusyCalls_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 3, 1, 1, 1, 3),
    _AcPerfTel2IPBusyCalls_Type()
)
acPerfTel2IPBusyCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPerfTel2IPBusyCalls.setStatus("current")
_AcPerfTel2IPNoAnswerCalls_Type = Counter32
_AcPerfTel2IPNoAnswerCalls_Object = MibScalar
acPerfTel2IPNoAnswerCalls = _AcPerfTel2IPNoAnswerCalls_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 3, 1, 1, 1, 4),
    _AcPerfTel2IPNoAnswerCalls_Type()
)
acPerfTel2IPNoAnswerCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPerfTel2IPNoAnswerCalls.setStatus("current")
_AcPerfTel2IPNoRouteCalls_Type = Counter32
_AcPerfTel2IPNoRouteCalls_Object = MibScalar
acPerfTel2IPNoRouteCalls = _AcPerfTel2IPNoRouteCalls_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 3, 1, 1, 1, 5),
    _AcPerfTel2IPNoRouteCalls_Type()
)
acPerfTel2IPNoRouteCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPerfTel2IPNoRouteCalls.setStatus("current")
_AcPerfTel2IPNoMatchCalls_Type = Counter32
_AcPerfTel2IPNoMatchCalls_Object = MibScalar
acPerfTel2IPNoMatchCalls = _AcPerfTel2IPNoMatchCalls_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 3, 1, 1, 1, 6),
    _AcPerfTel2IPNoMatchCalls_Type()
)
acPerfTel2IPNoMatchCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPerfTel2IPNoMatchCalls.setStatus("current")
_AcPerfTel2IPFailCalls_Type = Counter32
_AcPerfTel2IPFailCalls_Object = MibScalar
acPerfTel2IPFailCalls = _AcPerfTel2IPFailCalls_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 3, 1, 1, 1, 7),
    _AcPerfTel2IPFailCalls_Type()
)
acPerfTel2IPFailCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPerfTel2IPFailCalls.setStatus("current")
_AcPerfTel2IPFaxAttemptedCalls_Type = Counter32
_AcPerfTel2IPFaxAttemptedCalls_Object = MibScalar
acPerfTel2IPFaxAttemptedCalls = _AcPerfTel2IPFaxAttemptedCalls_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 3, 1, 1, 1, 8),
    _AcPerfTel2IPFaxAttemptedCalls_Type()
)
acPerfTel2IPFaxAttemptedCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPerfTel2IPFaxAttemptedCalls.setStatus("current")
_AcPerfTel2IPFaxSuccessCalls_Type = Counter32
_AcPerfTel2IPFaxSuccessCalls_Object = MibScalar
acPerfTel2IPFaxSuccessCalls = _AcPerfTel2IPFaxSuccessCalls_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 3, 1, 1, 1, 9),
    _AcPerfTel2IPFaxSuccessCalls_Type()
)
acPerfTel2IPFaxSuccessCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPerfTel2IPFaxSuccessCalls.setStatus("current")
_AcPerfTel2IPTotalDuration_Type = Counter32
_AcPerfTel2IPTotalDuration_Object = MibScalar
acPerfTel2IPTotalDuration = _AcPerfTel2IPTotalDuration_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 3, 1, 1, 1, 10),
    _AcPerfTel2IPTotalDuration_Type()
)
acPerfTel2IPTotalDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPerfTel2IPTotalDuration.setStatus("current")
_AcPerfIP2Tel_ObjectIdentity = ObjectIdentity
acPerfIP2Tel = _AcPerfIP2Tel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 10, 3, 1, 1, 2)
)
_AcPerfIP2TelAttemptedCalls_Type = Counter32
_AcPerfIP2TelAttemptedCalls_Object = MibScalar
acPerfIP2TelAttemptedCalls = _AcPerfIP2TelAttemptedCalls_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 3, 1, 1, 2, 1),
    _AcPerfIP2TelAttemptedCalls_Type()
)
acPerfIP2TelAttemptedCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPerfIP2TelAttemptedCalls.setStatus("current")
_AcPerfIP2TelEstablishedCalls_Type = Counter32
_AcPerfIP2TelEstablishedCalls_Object = MibScalar
acPerfIP2TelEstablishedCalls = _AcPerfIP2TelEstablishedCalls_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 3, 1, 1, 2, 2),
    _AcPerfIP2TelEstablishedCalls_Type()
)
acPerfIP2TelEstablishedCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPerfIP2TelEstablishedCalls.setStatus("current")
_AcPerfIP2TelBusyCalls_Type = Counter32
_AcPerfIP2TelBusyCalls_Object = MibScalar
acPerfIP2TelBusyCalls = _AcPerfIP2TelBusyCalls_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 3, 1, 1, 2, 3),
    _AcPerfIP2TelBusyCalls_Type()
)
acPerfIP2TelBusyCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPerfIP2TelBusyCalls.setStatus("current")
_AcPerfIP2TelNoAnswerCalls_Type = Counter32
_AcPerfIP2TelNoAnswerCalls_Object = MibScalar
acPerfIP2TelNoAnswerCalls = _AcPerfIP2TelNoAnswerCalls_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 3, 1, 1, 2, 4),
    _AcPerfIP2TelNoAnswerCalls_Type()
)
acPerfIP2TelNoAnswerCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPerfIP2TelNoAnswerCalls.setStatus("current")
_AcPerfIP2TelNoRouteCalls_Type = Counter32
_AcPerfIP2TelNoRouteCalls_Object = MibScalar
acPerfIP2TelNoRouteCalls = _AcPerfIP2TelNoRouteCalls_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 3, 1, 1, 2, 5),
    _AcPerfIP2TelNoRouteCalls_Type()
)
acPerfIP2TelNoRouteCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPerfIP2TelNoRouteCalls.setStatus("current")
_AcPerfIP2TelNoMatchCalls_Type = Counter32
_AcPerfIP2TelNoMatchCalls_Object = MibScalar
acPerfIP2TelNoMatchCalls = _AcPerfIP2TelNoMatchCalls_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 3, 1, 1, 2, 6),
    _AcPerfIP2TelNoMatchCalls_Type()
)
acPerfIP2TelNoMatchCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPerfIP2TelNoMatchCalls.setStatus("current")
_AcPerfIP2TelFailCalls_Type = Counter32
_AcPerfIP2TelFailCalls_Object = MibScalar
acPerfIP2TelFailCalls = _AcPerfIP2TelFailCalls_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 3, 1, 1, 2, 7),
    _AcPerfIP2TelFailCalls_Type()
)
acPerfIP2TelFailCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPerfIP2TelFailCalls.setStatus("current")
_AcPerfIP2TelFaxAttemptedCalls_Type = Counter32
_AcPerfIP2TelFaxAttemptedCalls_Object = MibScalar
acPerfIP2TelFaxAttemptedCalls = _AcPerfIP2TelFaxAttemptedCalls_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 3, 1, 1, 2, 8),
    _AcPerfIP2TelFaxAttemptedCalls_Type()
)
acPerfIP2TelFaxAttemptedCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPerfIP2TelFaxAttemptedCalls.setStatus("current")
_AcPerfIP2TelFaxSuccessCalls_Type = Counter32
_AcPerfIP2TelFaxSuccessCalls_Object = MibScalar
acPerfIP2TelFaxSuccessCalls = _AcPerfIP2TelFaxSuccessCalls_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 3, 1, 1, 2, 9),
    _AcPerfIP2TelFaxSuccessCalls_Type()
)
acPerfIP2TelFaxSuccessCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPerfIP2TelFaxSuccessCalls.setStatus("current")
_AcPerfIP2TelTotalDuration_Type = Counter32
_AcPerfIP2TelTotalDuration_Object = MibScalar
acPerfIP2TelTotalDuration = _AcPerfIP2TelTotalDuration_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 3, 1, 1, 2, 10),
    _AcPerfIP2TelTotalDuration_Type()
)
acPerfIP2TelTotalDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPerfIP2TelTotalDuration.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AcPerfH323SIPGateway",
    **{"audioCodes": audioCodes,
       "acRegistrations": acRegistrations,
       "acGeneric": acGeneric,
       "acProducts": acProducts,
       "acPerformance": acPerformance,
       "acPerfH323SIPGateway": acPerfH323SIPGateway,
       "acPerfH323SIPGWCommon": acPerfH323SIPGWCommon,
       "acPerfH323SIPGWCalls": acPerfH323SIPGWCalls,
       "acPerfTel2IP": acPerfTel2IP,
       "acPerfTel2IPAttemptedCalls": acPerfTel2IPAttemptedCalls,
       "acPerfTel2IPEstablishedCalls": acPerfTel2IPEstablishedCalls,
       "acPerfTel2IPBusyCalls": acPerfTel2IPBusyCalls,
       "acPerfTel2IPNoAnswerCalls": acPerfTel2IPNoAnswerCalls,
       "acPerfTel2IPNoRouteCalls": acPerfTel2IPNoRouteCalls,
       "acPerfTel2IPNoMatchCalls": acPerfTel2IPNoMatchCalls,
       "acPerfTel2IPFailCalls": acPerfTel2IPFailCalls,
       "acPerfTel2IPFaxAttemptedCalls": acPerfTel2IPFaxAttemptedCalls,
       "acPerfTel2IPFaxSuccessCalls": acPerfTel2IPFaxSuccessCalls,
       "acPerfTel2IPTotalDuration": acPerfTel2IPTotalDuration,
       "acPerfIP2Tel": acPerfIP2Tel,
       "acPerfIP2TelAttemptedCalls": acPerfIP2TelAttemptedCalls,
       "acPerfIP2TelEstablishedCalls": acPerfIP2TelEstablishedCalls,
       "acPerfIP2TelBusyCalls": acPerfIP2TelBusyCalls,
       "acPerfIP2TelNoAnswerCalls": acPerfIP2TelNoAnswerCalls,
       "acPerfIP2TelNoRouteCalls": acPerfIP2TelNoRouteCalls,
       "acPerfIP2TelNoMatchCalls": acPerfIP2TelNoMatchCalls,
       "acPerfIP2TelFailCalls": acPerfIP2TelFailCalls,
       "acPerfIP2TelFaxAttemptedCalls": acPerfIP2TelFaxAttemptedCalls,
       "acPerfIP2TelFaxSuccessCalls": acPerfIP2TelFaxSuccessCalls,
       "acPerfIP2TelTotalDuration": acPerfIP2TelTotalDuration}
)
