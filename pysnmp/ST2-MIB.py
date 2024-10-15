# SNMP MIB module (ST2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ST2-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:57:50 2024
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(wfSt2Group,) = mibBuilder.importSymbols(
    "Wellfleet-ST2-MIB",
    "wfSt2Group")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Stii_ObjectIdentity = ObjectIdentity
stii = _Stii_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5)
)
_St2AgentCopyright_Type = DisplayString
_St2AgentCopyright_Object = MibScalar
st2AgentCopyright = _St2AgentCopyright_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 1),
    _St2AgentCopyright_Type()
)
st2AgentCopyright.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2AgentCopyright.setStatus("mandatory")
_St2ProtoVersion_Type = DisplayString
_St2ProtoVersion_Object = MibScalar
st2ProtoVersion = _St2ProtoVersion_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 2),
    _St2ProtoVersion_Type()
)
st2ProtoVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2ProtoVersion.setStatus("mandatory")
_St2FlowSpecVersion_Type = Integer32
_St2FlowSpecVersion_Object = MibScalar
st2FlowSpecVersion = _St2FlowSpecVersion_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 3),
    _St2FlowSpecVersion_Type()
)
st2FlowSpecVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2FlowSpecVersion.setStatus("mandatory")


class _St2AgentType_Type(Integer32):
    """Custom type st2AgentType based on Integer32"""
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
        *(("endSystem", 3),
          ("intermediateAndEndSystem", 4),
          ("intermediateSystem", 2),
          ("other", 1))
    )


_St2AgentType_Type.__name__ = "Integer32"
_St2AgentType_Object = MibScalar
st2AgentType = _St2AgentType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 4),
    _St2AgentType_Type()
)
st2AgentType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2AgentType.setStatus("mandatory")


class _St2RoutingDerived_Type(Integer32):
    """Custom type st2RoutingDerived based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fixed", 2),
          ("other", 1),
          ("regularIP", 3))
    )


_St2RoutingDerived_Type.__name__ = "Integer32"
_St2RoutingDerived_Object = MibScalar
st2RoutingDerived = _St2RoutingDerived_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 5),
    _St2RoutingDerived_Type()
)
st2RoutingDerived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2RoutingDerived.setStatus("mandatory")
_St2ToAccept_Type = TimeTicks
_St2ToAccept_Object = MibScalar
st2ToAccept = _St2ToAccept_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 6),
    _St2ToAccept_Type()
)
st2ToAccept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    st2ToAccept.setStatus("mandatory")
_St2NAccept_Type = Integer32
_St2NAccept_Object = MibScalar
st2NAccept = _St2NAccept_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 7),
    _St2NAccept_Type()
)
st2NAccept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    st2NAccept.setStatus("mandatory")
_St2ToConnect_Type = TimeTicks
_St2ToConnect_Object = MibScalar
st2ToConnect = _St2ToConnect_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 8),
    _St2ToConnect_Type()
)
st2ToConnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    st2ToConnect.setStatus("mandatory")
_St2NConnect_Type = Integer32
_St2NConnect_Object = MibScalar
st2NConnect = _St2NConnect_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 9),
    _St2NConnect_Type()
)
st2NConnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    st2NConnect.setStatus("mandatory")
_St2ToDisconnect_Type = TimeTicks
_St2ToDisconnect_Object = MibScalar
st2ToDisconnect = _St2ToDisconnect_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 10),
    _St2ToDisconnect_Type()
)
st2ToDisconnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    st2ToDisconnect.setStatus("mandatory")
_St2NDisconnect_Type = Integer32
_St2NDisconnect_Object = MibScalar
st2NDisconnect = _St2NDisconnect_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 11),
    _St2NDisconnect_Type()
)
st2NDisconnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    st2NDisconnect.setStatus("mandatory")
_St2ToHidAck_Type = TimeTicks
_St2ToHidAck_Object = MibScalar
st2ToHidAck = _St2ToHidAck_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 12),
    _St2ToHidAck_Type()
)
st2ToHidAck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    st2ToHidAck.setStatus("mandatory")
_St2NHidAck_Type = Integer32
_St2NHidAck_Object = MibScalar
st2NHidAck = _St2NHidAck_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 13),
    _St2NHidAck_Type()
)
st2NHidAck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    st2NHidAck.setStatus("mandatory")
_St2ToHidChange_Type = TimeTicks
_St2ToHidChange_Object = MibScalar
st2ToHidChange = _St2ToHidChange_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 14),
    _St2ToHidChange_Type()
)
st2ToHidChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    st2ToHidChange.setStatus("mandatory")
_St2NHidChange_Type = Integer32
_St2NHidChange_Object = MibScalar
st2NHidChange = _St2NHidChange_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 15),
    _St2NHidChange_Type()
)
st2NHidChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    st2NHidChange.setStatus("mandatory")
_St2ToNotify_Type = TimeTicks
_St2ToNotify_Object = MibScalar
st2ToNotify = _St2ToNotify_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 16),
    _St2ToNotify_Type()
)
st2ToNotify.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    st2ToNotify.setStatus("mandatory")
_St2NNotify_Type = Integer32
_St2NNotify_Object = MibScalar
st2NNotify = _St2NNotify_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 17),
    _St2NNotify_Type()
)
st2NNotify.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    st2NNotify.setStatus("mandatory")
_St2ToRefuse_Type = TimeTicks
_St2ToRefuse_Object = MibScalar
st2ToRefuse = _St2ToRefuse_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 18),
    _St2ToRefuse_Type()
)
st2ToRefuse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    st2ToRefuse.setStatus("mandatory")
_St2NRefuse_Type = Integer32
_St2NRefuse_Object = MibScalar
st2NRefuse = _St2NRefuse_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 19),
    _St2NRefuse_Type()
)
st2NRefuse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    st2NRefuse.setStatus("mandatory")
_St2ToReroute_Type = TimeTicks
_St2ToReroute_Object = MibScalar
st2ToReroute = _St2ToReroute_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 20),
    _St2ToReroute_Type()
)
st2ToReroute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    st2ToReroute.setStatus("mandatory")
_St2NReroute_Type = Integer32
_St2NReroute_Object = MibScalar
st2NReroute = _St2NReroute_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 21),
    _St2NReroute_Type()
)
st2NReroute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    st2NReroute.setStatus("mandatory")
_St2ToEnd2End_Type = TimeTicks
_St2ToEnd2End_Object = MibScalar
st2ToEnd2End = _St2ToEnd2End_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 22),
    _St2ToEnd2End_Type()
)
st2ToEnd2End.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    st2ToEnd2End.setStatus("mandatory")
_St2NEnd2End_Type = Integer32
_St2NEnd2End_Object = MibScalar
st2NEnd2End = _St2NEnd2End_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 23),
    _St2NEnd2End_Type()
)
st2NEnd2End.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    st2NEnd2End.setStatus("mandatory")
_St2NHidAbort_Type = Integer32
_St2NHidAbort_Object = MibScalar
st2NHidAbort = _St2NHidAbort_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 24),
    _St2NHidAbort_Type()
)
st2NHidAbort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    st2NHidAbort.setStatus("mandatory")
_St2HelloTimerHoldDown_Type = TimeTicks
_St2HelloTimerHoldDown_Object = MibScalar
st2HelloTimerHoldDown = _St2HelloTimerHoldDown_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 25),
    _St2HelloTimerHoldDown_Type()
)
st2HelloTimerHoldDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    st2HelloTimerHoldDown.setStatus("mandatory")
_St2HelloLossFactor_Type = Integer32
_St2HelloLossFactor_Object = MibScalar
st2HelloLossFactor = _St2HelloLossFactor_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 26),
    _St2HelloLossFactor_Type()
)
st2HelloLossFactor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    st2HelloLossFactor.setStatus("mandatory")
_St2DefaultRecoveryTimeout_Type = TimeTicks
_St2DefaultRecoveryTimeout_Object = MibScalar
st2DefaultRecoveryTimeout = _St2DefaultRecoveryTimeout_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 27),
    _St2DefaultRecoveryTimeout_Type()
)
st2DefaultRecoveryTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    st2DefaultRecoveryTimeout.setStatus("mandatory")
_St2DefaultHelloFactor_Type = Integer32
_St2DefaultHelloFactor_Object = MibScalar
st2DefaultHelloFactor = _St2DefaultHelloFactor_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 28),
    _St2DefaultHelloFactor_Type()
)
st2DefaultHelloFactor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    st2DefaultHelloFactor.setStatus("mandatory")
_St2ScmpRcvdOctets_Type = Counter32
_St2ScmpRcvdOctets_Object = MibScalar
st2ScmpRcvdOctets = _St2ScmpRcvdOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 29),
    _St2ScmpRcvdOctets_Type()
)
st2ScmpRcvdOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2ScmpRcvdOctets.setStatus("mandatory")
_St2ScmpSentOctets_Type = Counter32
_St2ScmpSentOctets_Object = MibScalar
st2ScmpSentOctets = _St2ScmpSentOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 30),
    _St2ScmpSentOctets_Type()
)
st2ScmpSentOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2ScmpSentOctets.setStatus("mandatory")
_St2ScmpRcvdBadTypes_Type = Counter32
_St2ScmpRcvdBadTypes_Object = MibScalar
st2ScmpRcvdBadTypes = _St2ScmpRcvdBadTypes_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 31),
    _St2ScmpRcvdBadTypes_Type()
)
st2ScmpRcvdBadTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2ScmpRcvdBadTypes.setStatus("mandatory")
_St2ScmpRcvdBadCks_Type = Counter32
_St2ScmpRcvdBadCks_Object = MibScalar
st2ScmpRcvdBadCks = _St2ScmpRcvdBadCks_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 32),
    _St2ScmpRcvdBadCks_Type()
)
st2ScmpRcvdBadCks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2ScmpRcvdBadCks.setStatus("mandatory")
_St2ScmpSentAccepts_Type = Counter32
_St2ScmpSentAccepts_Object = MibScalar
st2ScmpSentAccepts = _St2ScmpSentAccepts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 33),
    _St2ScmpSentAccepts_Type()
)
st2ScmpSentAccepts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2ScmpSentAccepts.setStatus("mandatory")
_St2ScmpSentAcks_Type = Counter32
_St2ScmpSentAcks_Object = MibScalar
st2ScmpSentAcks = _St2ScmpSentAcks_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 34),
    _St2ScmpSentAcks_Type()
)
st2ScmpSentAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2ScmpSentAcks.setStatus("mandatory")
_St2ScmpSentChanges_Type = Counter32
_St2ScmpSentChanges_Object = MibScalar
st2ScmpSentChanges = _St2ScmpSentChanges_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 35),
    _St2ScmpSentChanges_Type()
)
st2ScmpSentChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2ScmpSentChanges.setStatus("mandatory")
_St2ScmpSentChangeReqs_Type = Counter32
_St2ScmpSentChangeReqs_Object = MibScalar
st2ScmpSentChangeReqs = _St2ScmpSentChangeReqs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 36),
    _St2ScmpSentChangeReqs_Type()
)
st2ScmpSentChangeReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2ScmpSentChangeReqs.setStatus("mandatory")
_St2ScmpSentConnects_Type = Counter32
_St2ScmpSentConnects_Object = MibScalar
st2ScmpSentConnects = _St2ScmpSentConnects_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 37),
    _St2ScmpSentConnects_Type()
)
st2ScmpSentConnects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2ScmpSentConnects.setStatus("mandatory")
_St2ScmpSentDisconnects_Type = Counter32
_St2ScmpSentDisconnects_Object = MibScalar
st2ScmpSentDisconnects = _St2ScmpSentDisconnects_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 38),
    _St2ScmpSentDisconnects_Type()
)
st2ScmpSentDisconnects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2ScmpSentDisconnects.setStatus("mandatory")
_St2ScmpSentErrorInReqs_Type = Counter32
_St2ScmpSentErrorInReqs_Object = MibScalar
st2ScmpSentErrorInReqs = _St2ScmpSentErrorInReqs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 39),
    _St2ScmpSentErrorInReqs_Type()
)
st2ScmpSentErrorInReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2ScmpSentErrorInReqs.setStatus("mandatory")
_St2ScmpSentErrorInResps_Type = Counter32
_St2ScmpSentErrorInResps_Object = MibScalar
st2ScmpSentErrorInResps = _St2ScmpSentErrorInResps_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 40),
    _St2ScmpSentErrorInResps_Type()
)
st2ScmpSentErrorInResps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2ScmpSentErrorInResps.setStatus("mandatory")
_St2ScmpSentHellos_Type = Counter32
_St2ScmpSentHellos_Object = MibScalar
st2ScmpSentHellos = _St2ScmpSentHellos_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 41),
    _St2ScmpSentHellos_Type()
)
st2ScmpSentHellos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2ScmpSentHellos.setStatus("mandatory")
_St2ScmpSentHidApproves_Type = Counter32
_St2ScmpSentHidApproves_Object = MibScalar
st2ScmpSentHidApproves = _St2ScmpSentHidApproves_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 42),
    _St2ScmpSentHidApproves_Type()
)
st2ScmpSentHidApproves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2ScmpSentHidApproves.setStatus("mandatory")
_St2ScmpSentHidChanges_Type = Counter32
_St2ScmpSentHidChanges_Object = MibScalar
st2ScmpSentHidChanges = _St2ScmpSentHidChanges_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 43),
    _St2ScmpSentHidChanges_Type()
)
st2ScmpSentHidChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2ScmpSentHidChanges.setStatus("mandatory")
_St2ScmpSentHidChangeReqs_Type = Counter32
_St2ScmpSentHidChangeReqs_Object = MibScalar
st2ScmpSentHidChangeReqs = _St2ScmpSentHidChangeReqs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 44),
    _St2ScmpSentHidChangeReqs_Type()
)
st2ScmpSentHidChangeReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2ScmpSentHidChangeReqs.setStatus("mandatory")
_St2ScmpSentHidRejects_Type = Counter32
_St2ScmpSentHidRejects_Object = MibScalar
st2ScmpSentHidRejects = _St2ScmpSentHidRejects_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 45),
    _St2ScmpSentHidRejects_Type()
)
st2ScmpSentHidRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2ScmpSentHidRejects.setStatus("mandatory")
_St2ScmpSentNotifys_Type = Counter32
_St2ScmpSentNotifys_Object = MibScalar
st2ScmpSentNotifys = _St2ScmpSentNotifys_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 46),
    _St2ScmpSentNotifys_Type()
)
st2ScmpSentNotifys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2ScmpSentNotifys.setStatus("mandatory")
_St2ScmpSentRefuses_Type = Counter32
_St2ScmpSentRefuses_Object = MibScalar
st2ScmpSentRefuses = _St2ScmpSentRefuses_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 47),
    _St2ScmpSentRefuses_Type()
)
st2ScmpSentRefuses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2ScmpSentRefuses.setStatus("mandatory")
_St2ScmpSentStatus_Type = Counter32
_St2ScmpSentStatus_Object = MibScalar
st2ScmpSentStatus = _St2ScmpSentStatus_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 48),
    _St2ScmpSentStatus_Type()
)
st2ScmpSentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2ScmpSentStatus.setStatus("mandatory")
_St2ScmpSentStatusResps_Type = Counter32
_St2ScmpSentStatusResps_Object = MibScalar
st2ScmpSentStatusResps = _St2ScmpSentStatusResps_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 49),
    _St2ScmpSentStatusResps_Type()
)
st2ScmpSentStatusResps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2ScmpSentStatusResps.setStatus("mandatory")
_St2ScmpRcvdAccepts_Type = Counter32
_St2ScmpRcvdAccepts_Object = MibScalar
st2ScmpRcvdAccepts = _St2ScmpRcvdAccepts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 50),
    _St2ScmpRcvdAccepts_Type()
)
st2ScmpRcvdAccepts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2ScmpRcvdAccepts.setStatus("mandatory")
_St2ScmpRcvdAcks_Type = Counter32
_St2ScmpRcvdAcks_Object = MibScalar
st2ScmpRcvdAcks = _St2ScmpRcvdAcks_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 51),
    _St2ScmpRcvdAcks_Type()
)
st2ScmpRcvdAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2ScmpRcvdAcks.setStatus("mandatory")
_St2ScmpRcvdChanges_Type = Counter32
_St2ScmpRcvdChanges_Object = MibScalar
st2ScmpRcvdChanges = _St2ScmpRcvdChanges_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 52),
    _St2ScmpRcvdChanges_Type()
)
st2ScmpRcvdChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2ScmpRcvdChanges.setStatus("mandatory")
_St2ScmpRcvdChangeReqs_Type = Counter32
_St2ScmpRcvdChangeReqs_Object = MibScalar
st2ScmpRcvdChangeReqs = _St2ScmpRcvdChangeReqs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 53),
    _St2ScmpRcvdChangeReqs_Type()
)
st2ScmpRcvdChangeReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2ScmpRcvdChangeReqs.setStatus("mandatory")
_St2ScmpRcvdConnects_Type = Counter32
_St2ScmpRcvdConnects_Object = MibScalar
st2ScmpRcvdConnects = _St2ScmpRcvdConnects_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 54),
    _St2ScmpRcvdConnects_Type()
)
st2ScmpRcvdConnects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2ScmpRcvdConnects.setStatus("mandatory")
_St2ScmpRcvdDisconnects_Type = Counter32
_St2ScmpRcvdDisconnects_Object = MibScalar
st2ScmpRcvdDisconnects = _St2ScmpRcvdDisconnects_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 55),
    _St2ScmpRcvdDisconnects_Type()
)
st2ScmpRcvdDisconnects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2ScmpRcvdDisconnects.setStatus("mandatory")
_St2ScmpRcvdErrorInReqs_Type = Counter32
_St2ScmpRcvdErrorInReqs_Object = MibScalar
st2ScmpRcvdErrorInReqs = _St2ScmpRcvdErrorInReqs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 56),
    _St2ScmpRcvdErrorInReqs_Type()
)
st2ScmpRcvdErrorInReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2ScmpRcvdErrorInReqs.setStatus("mandatory")
_St2ScmpRcvdErrorInResps_Type = Counter32
_St2ScmpRcvdErrorInResps_Object = MibScalar
st2ScmpRcvdErrorInResps = _St2ScmpRcvdErrorInResps_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 57),
    _St2ScmpRcvdErrorInResps_Type()
)
st2ScmpRcvdErrorInResps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2ScmpRcvdErrorInResps.setStatus("mandatory")
_St2ScmpRcvdHellos_Type = Counter32
_St2ScmpRcvdHellos_Object = MibScalar
st2ScmpRcvdHellos = _St2ScmpRcvdHellos_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 58),
    _St2ScmpRcvdHellos_Type()
)
st2ScmpRcvdHellos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2ScmpRcvdHellos.setStatus("mandatory")
_St2ScmpRcvdHidApproves_Type = Counter32
_St2ScmpRcvdHidApproves_Object = MibScalar
st2ScmpRcvdHidApproves = _St2ScmpRcvdHidApproves_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 59),
    _St2ScmpRcvdHidApproves_Type()
)
st2ScmpRcvdHidApproves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2ScmpRcvdHidApproves.setStatus("mandatory")
_St2ScmpRcvdHidChanges_Type = Counter32
_St2ScmpRcvdHidChanges_Object = MibScalar
st2ScmpRcvdHidChanges = _St2ScmpRcvdHidChanges_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 60),
    _St2ScmpRcvdHidChanges_Type()
)
st2ScmpRcvdHidChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2ScmpRcvdHidChanges.setStatus("mandatory")
_St2ScmpRcvdHidChangeReqs_Type = Counter32
_St2ScmpRcvdHidChangeReqs_Object = MibScalar
st2ScmpRcvdHidChangeReqs = _St2ScmpRcvdHidChangeReqs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 61),
    _St2ScmpRcvdHidChangeReqs_Type()
)
st2ScmpRcvdHidChangeReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2ScmpRcvdHidChangeReqs.setStatus("mandatory")
_St2ScmpRcvdHidRejects_Type = Counter32
_St2ScmpRcvdHidRejects_Object = MibScalar
st2ScmpRcvdHidRejects = _St2ScmpRcvdHidRejects_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 62),
    _St2ScmpRcvdHidRejects_Type()
)
st2ScmpRcvdHidRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2ScmpRcvdHidRejects.setStatus("mandatory")
_St2ScmpRcvdNotifys_Type = Counter32
_St2ScmpRcvdNotifys_Object = MibScalar
st2ScmpRcvdNotifys = _St2ScmpRcvdNotifys_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 63),
    _St2ScmpRcvdNotifys_Type()
)
st2ScmpRcvdNotifys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2ScmpRcvdNotifys.setStatus("mandatory")
_St2ScmpRcvdRefuses_Type = Counter32
_St2ScmpRcvdRefuses_Object = MibScalar
st2ScmpRcvdRefuses = _St2ScmpRcvdRefuses_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 64),
    _St2ScmpRcvdRefuses_Type()
)
st2ScmpRcvdRefuses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2ScmpRcvdRefuses.setStatus("mandatory")
_St2ScmpRcvdStatus_Type = Counter32
_St2ScmpRcvdStatus_Object = MibScalar
st2ScmpRcvdStatus = _St2ScmpRcvdStatus_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 65),
    _St2ScmpRcvdStatus_Type()
)
st2ScmpRcvdStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2ScmpRcvdStatus.setStatus("mandatory")
_St2ScmpRcvdStatusResps_Type = Counter32
_St2ScmpRcvdStatusResps_Object = MibScalar
st2ScmpRcvdStatusResps = _St2ScmpRcvdStatusResps_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 66),
    _St2ScmpRcvdStatusResps_Type()
)
st2ScmpRcvdStatusResps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2ScmpRcvdStatusResps.setStatus("mandatory")


class _St2ScmpRcvdErrorSnap_Type(OctetString):
    """Custom type st2ScmpRcvdErrorSnap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_St2ScmpRcvdErrorSnap_Type.__name__ = "OctetString"
_St2ScmpRcvdErrorSnap_Object = MibScalar
st2ScmpRcvdErrorSnap = _St2ScmpRcvdErrorSnap_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 67),
    _St2ScmpRcvdErrorSnap_Type()
)
st2ScmpRcvdErrorSnap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2ScmpRcvdErrorSnap.setStatus("mandatory")
_St2ScmpRcvdBadTypeTime_Type = TimeTicks
_St2ScmpRcvdBadTypeTime_Object = MibScalar
st2ScmpRcvdBadTypeTime = _St2ScmpRcvdBadTypeTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 68),
    _St2ScmpRcvdBadTypeTime_Type()
)
st2ScmpRcvdBadTypeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2ScmpRcvdBadTypeTime.setStatus("mandatory")
_St2ScmpRcvdBadCksTime_Type = TimeTicks
_St2ScmpRcvdBadCksTime_Object = MibScalar
st2ScmpRcvdBadCksTime = _St2ScmpRcvdBadCksTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 69),
    _St2ScmpRcvdBadCksTime_Type()
)
st2ScmpRcvdBadCksTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2ScmpRcvdBadCksTime.setStatus("mandatory")
_St2OriginOpens_Type = Counter32
_St2OriginOpens_Object = MibScalar
st2OriginOpens = _St2OriginOpens_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 70),
    _St2OriginOpens_Type()
)
st2OriginOpens.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2OriginOpens.setStatus("mandatory")
_St2IntermedOpens_Type = Counter32
_St2IntermedOpens_Object = MibScalar
st2IntermedOpens = _St2IntermedOpens_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 71),
    _St2IntermedOpens_Type()
)
st2IntermedOpens.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2IntermedOpens.setStatus("mandatory")
_St2TargetOpens_Type = Counter32
_St2TargetOpens_Object = MibScalar
st2TargetOpens = _St2TargetOpens_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 72),
    _St2TargetOpens_Type()
)
st2TargetOpens.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2TargetOpens.setStatus("mandatory")
_St2FailOpens_Type = Counter32
_St2FailOpens_Object = MibScalar
st2FailOpens = _St2FailOpens_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 73),
    _St2FailOpens_Type()
)
st2FailOpens.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2FailOpens.setStatus("mandatory")
_St2AcceptTimeouts_Type = Counter32
_St2AcceptTimeouts_Object = MibScalar
st2AcceptTimeouts = _St2AcceptTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 74),
    _St2AcceptTimeouts_Type()
)
st2AcceptTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2AcceptTimeouts.setStatus("mandatory")
_St2ParamChangeFails_Type = Counter32
_St2ParamChangeFails_Object = MibScalar
st2ParamChangeFails = _St2ParamChangeFails_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 75),
    _St2ParamChangeFails_Type()
)
st2ParamChangeFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2ParamChangeFails.setStatus("mandatory")
_St2NumStreamEntries_Type = Gauge32
_St2NumStreamEntries_Object = MibScalar
st2NumStreamEntries = _St2NumStreamEntries_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 76),
    _St2NumStreamEntries_Type()
)
st2NumStreamEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2NumStreamEntries.setStatus("mandatory")
_St2NumOpenStreams_Type = Gauge32
_St2NumOpenStreams_Object = MibScalar
st2NumOpenStreams = _St2NumOpenStreams_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 77),
    _St2NumOpenStreams_Type()
)
st2NumOpenStreams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2NumOpenStreams.setStatus("mandatory")
_St2NumOpenOriginStreams_Type = Gauge32
_St2NumOpenOriginStreams_Object = MibScalar
st2NumOpenOriginStreams = _St2NumOpenOriginStreams_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 78),
    _St2NumOpenOriginStreams_Type()
)
st2NumOpenOriginStreams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2NumOpenOriginStreams.setStatus("mandatory")
_St2NumHops_Type = Gauge32
_St2NumHops_Object = MibScalar
st2NumHops = _St2NumHops_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 79),
    _St2NumHops_Type()
)
st2NumHops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2NumHops.setStatus("mandatory")
_St2NumNeighbors_Type = Gauge32
_St2NumNeighbors_Object = MibScalar
st2NumNeighbors = _St2NumNeighbors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 80),
    _St2NumNeighbors_Type()
)
st2NumNeighbors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2NumNeighbors.setStatus("mandatory")
_St2NumTargets_Type = Gauge32
_St2NumTargets_Object = MibScalar
st2NumTargets = _St2NumTargets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 81),
    _St2NumTargets_Type()
)
st2NumTargets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2NumTargets.setStatus("mandatory")
_St2NumGroups_Type = Gauge32
_St2NumGroups_Object = MibScalar
st2NumGroups = _St2NumGroups_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 82),
    _St2NumGroups_Type()
)
st2NumGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2NumGroups.setStatus("mandatory")
_St2NumSubgroups_Type = Gauge32
_St2NumSubgroups_Object = MibScalar
st2NumSubgroups = _St2NumSubgroups_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 83),
    _St2NumSubgroups_Type()
)
st2NumSubgroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2NumSubgroups.setStatus("mandatory")
_St2RouteFailures_Type = Counter32
_St2RouteFailures_Object = MibScalar
st2RouteFailures = _St2RouteFailures_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 84),
    _St2RouteFailures_Type()
)
st2RouteFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2RouteFailures.setStatus("mandatory")
_St2RouteLoops_Type = Counter32
_St2RouteLoops_Object = MibScalar
st2RouteLoops = _St2RouteLoops_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 85),
    _St2RouteLoops_Type()
)
st2RouteLoops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2RouteLoops.setStatus("mandatory")
_St2ScmpRetrans_Type = Counter32
_St2ScmpRetrans_Object = MibScalar
st2ScmpRetrans = _St2ScmpRetrans_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 86),
    _St2ScmpRetrans_Type()
)
st2ScmpRetrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2ScmpRetrans.setStatus("mandatory")
_St2StreamTable_Object = MibTable
st2StreamTable = _St2StreamTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 87)
)
if mibBuilder.loadTexts:
    st2StreamTable.setStatus("mandatory")
_St2StreamEntry_Object = MibTableRow
st2StreamEntry = _St2StreamEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 87, 1)
)
st2StreamEntry.setIndexNames(
    (0, "ST2-MIB", "st2StreamName"),
    (0, "ST2-MIB", "st2StreamPrevHopAddr"),
    (0, "ST2-MIB", "st2StreamPrevHopVlid"),
)
if mibBuilder.loadTexts:
    st2StreamEntry.setStatus("mandatory")


class _St2StreamName_Type(OctetString):
    """Custom type st2StreamName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )


_St2StreamName_Type.__name__ = "OctetString"
_St2StreamName_Object = MibTableColumn
st2StreamName = _St2StreamName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 87, 1, 1),
    _St2StreamName_Type()
)
st2StreamName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2StreamName.setStatus("mandatory")
_St2StreamPrevHopAddr_Type = IpAddress
_St2StreamPrevHopAddr_Object = MibTableColumn
st2StreamPrevHopAddr = _St2StreamPrevHopAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 87, 1, 2),
    _St2StreamPrevHopAddr_Type()
)
st2StreamPrevHopAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2StreamPrevHopAddr.setStatus("mandatory")


class _St2StreamPrevHopVlid_Type(Integer32):
    """Custom type st2StreamPrevHopVlid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_St2StreamPrevHopVlid_Type.__name__ = "Integer32"
_St2StreamPrevHopVlid_Object = MibTableColumn
st2StreamPrevHopVlid = _St2StreamPrevHopVlid_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 87, 1, 3),
    _St2StreamPrevHopVlid_Type()
)
st2StreamPrevHopVlid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2StreamPrevHopVlid.setStatus("mandatory")
_St2StreamStartTime_Type = TimeTicks
_St2StreamStartTime_Object = MibTableColumn
st2StreamStartTime = _St2StreamStartTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 87, 1, 4),
    _St2StreamStartTime_Type()
)
st2StreamStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2StreamStartTime.setStatus("mandatory")


class _St2StreamState_Type(Integer32):
    """Custom type st2StreamState based on Integer32"""
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
        *(("acceptable", 4),
          ("active", 5),
          ("activeReduced", 6),
          ("hidNotOk", 3),
          ("idle", 2),
          ("other", 1),
          ("passive", 7))
    )


_St2StreamState_Type.__name__ = "Integer32"
_St2StreamState_Object = MibTableColumn
st2StreamState = _St2StreamState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 87, 1, 5),
    _St2StreamState_Type()
)
st2StreamState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2StreamState.setStatus("mandatory")
_St2StreamStateTime_Type = TimeTicks
_St2StreamStateTime_Object = MibTableColumn
st2StreamStateTime = _St2StreamStateTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 87, 1, 6),
    _St2StreamStateTime_Type()
)
st2StreamStateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2StreamStateTime.setStatus("mandatory")


class _St2StreamRole_Type(Integer32):
    """Custom type st2StreamRole based on Integer32"""
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
        *(("intermediate", 4),
          ("intermediateAndTarget", 5),
          ("origin", 2),
          ("other", 1),
          ("target", 3))
    )


_St2StreamRole_Type.__name__ = "Integer32"
_St2StreamRole_Object = MibTableColumn
st2StreamRole = _St2StreamRole_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 87, 1, 7),
    _St2StreamRole_Type()
)
st2StreamRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2StreamRole.setStatus("mandatory")


class _St2StreamGroup_Type(OctetString):
    """Custom type st2StreamGroup based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )


_St2StreamGroup_Type.__name__ = "OctetString"
_St2StreamGroup_Object = MibTableColumn
st2StreamGroup = _St2StreamGroup_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 87, 1, 8),
    _St2StreamGroup_Type()
)
st2StreamGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2StreamGroup.setStatus("mandatory")
_St2StreamNumSubgroups_Type = Gauge32
_St2StreamNumSubgroups_Object = MibTableColumn
st2StreamNumSubgroups = _St2StreamNumSubgroups_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 87, 1, 9),
    _St2StreamNumSubgroups_Type()
)
st2StreamNumSubgroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2StreamNumSubgroups.setStatus("mandatory")
_St2StreamNumNextHops_Type = Gauge32
_St2StreamNumNextHops_Object = MibTableColumn
st2StreamNumNextHops = _St2StreamNumNextHops_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 87, 1, 10),
    _St2StreamNumNextHops_Type()
)
st2StreamNumNextHops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2StreamNumNextHops.setStatus("mandatory")
_St2StreamNumTargets_Type = Gauge32
_St2StreamNumTargets_Object = MibTableColumn
st2StreamNumTargets = _St2StreamNumTargets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 87, 1, 11),
    _St2StreamNumTargets_Type()
)
st2StreamNumTargets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2StreamNumTargets.setStatus("mandatory")
_St2StreamRefuses_Type = Counter32
_St2StreamRefuses_Object = MibTableColumn
st2StreamRefuses = _St2StreamRefuses_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 87, 1, 12),
    _St2StreamRefuses_Type()
)
st2StreamRefuses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2StreamRefuses.setStatus("mandatory")
_St2StreamFlowspecChanges_Type = Counter32
_St2StreamFlowspecChanges_Object = MibTableColumn
st2StreamFlowspecChanges = _St2StreamFlowspecChanges_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 87, 1, 13),
    _St2StreamFlowspecChanges_Type()
)
st2StreamFlowspecChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2StreamFlowspecChanges.setStatus("mandatory")


class _St2StreamFlowPrecedence_Type(Integer32):
    """Custom type st2StreamFlowPrecedence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_St2StreamFlowPrecedence_Type.__name__ = "Integer32"
_St2StreamFlowPrecedence_Object = MibTableColumn
st2StreamFlowPrecedence = _St2StreamFlowPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 87, 1, 14),
    _St2StreamFlowPrecedence_Type()
)
st2StreamFlowPrecedence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2StreamFlowPrecedence.setStatus("mandatory")


class _St2StreamFlowDutyFactor_Type(Integer32):
    """Custom type st2StreamFlowDutyFactor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_St2StreamFlowDutyFactor_Type.__name__ = "Integer32"
_St2StreamFlowDutyFactor_Object = MibTableColumn
st2StreamFlowDutyFactor = _St2StreamFlowDutyFactor_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 87, 1, 15),
    _St2StreamFlowDutyFactor_Type()
)
st2StreamFlowDutyFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2StreamFlowDutyFactor.setStatus("mandatory")


class _St2StreamFlowErrorRate_Type(Integer32):
    """Custom type st2StreamFlowErrorRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_St2StreamFlowErrorRate_Type.__name__ = "Integer32"
_St2StreamFlowErrorRate_Object = MibTableColumn
st2StreamFlowErrorRate = _St2StreamFlowErrorRate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 87, 1, 16),
    _St2StreamFlowErrorRate_Type()
)
st2StreamFlowErrorRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2StreamFlowErrorRate.setStatus("mandatory")


class _St2StreamFlowReliability_Type(Integer32):
    """Custom type st2StreamFlowReliability based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_St2StreamFlowReliability_Type.__name__ = "Integer32"
_St2StreamFlowReliability_Object = MibTableColumn
st2StreamFlowReliability = _St2StreamFlowReliability_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 87, 1, 17),
    _St2StreamFlowReliability_Type()
)
st2StreamFlowReliability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2StreamFlowReliability.setStatus("mandatory")


class _St2StreamFlowTradeoffs_Type(Integer32):
    """Custom type st2StreamFlowTradeoffs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_St2StreamFlowTradeoffs_Type.__name__ = "Integer32"
_St2StreamFlowTradeoffs_Object = MibTableColumn
st2StreamFlowTradeoffs = _St2StreamFlowTradeoffs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 87, 1, 18),
    _St2StreamFlowTradeoffs_Type()
)
st2StreamFlowTradeoffs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2StreamFlowTradeoffs.setStatus("mandatory")


class _St2StreamFlowRecoveryTimeout_Type(Integer32):
    """Custom type st2StreamFlowRecoveryTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_St2StreamFlowRecoveryTimeout_Type.__name__ = "Integer32"
_St2StreamFlowRecoveryTimeout_Object = MibTableColumn
st2StreamFlowRecoveryTimeout = _St2StreamFlowRecoveryTimeout_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 87, 1, 19),
    _St2StreamFlowRecoveryTimeout_Type()
)
st2StreamFlowRecoveryTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2StreamFlowRecoveryTimeout.setStatus("mandatory")


class _St2StreamFlowLimitOnCost_Type(Integer32):
    """Custom type st2StreamFlowLimitOnCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_St2StreamFlowLimitOnCost_Type.__name__ = "Integer32"
_St2StreamFlowLimitOnCost_Object = MibTableColumn
st2StreamFlowLimitOnCost = _St2StreamFlowLimitOnCost_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 87, 1, 20),
    _St2StreamFlowLimitOnCost_Type()
)
st2StreamFlowLimitOnCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2StreamFlowLimitOnCost.setStatus("mandatory")


class _St2StreamFlowLimitOnDelay_Type(Integer32):
    """Custom type st2StreamFlowLimitOnDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_St2StreamFlowLimitOnDelay_Type.__name__ = "Integer32"
_St2StreamFlowLimitOnDelay_Object = MibTableColumn
st2StreamFlowLimitOnDelay = _St2StreamFlowLimitOnDelay_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 87, 1, 21),
    _St2StreamFlowLimitOnDelay_Type()
)
st2StreamFlowLimitOnDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2StreamFlowLimitOnDelay.setStatus("mandatory")


class _St2StreamFlowLimitOnPduBytes_Type(Integer32):
    """Custom type st2StreamFlowLimitOnPduBytes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_St2StreamFlowLimitOnPduBytes_Type.__name__ = "Integer32"
_St2StreamFlowLimitOnPduBytes_Object = MibTableColumn
st2StreamFlowLimitOnPduBytes = _St2StreamFlowLimitOnPduBytes_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 87, 1, 22),
    _St2StreamFlowLimitOnPduBytes_Type()
)
st2StreamFlowLimitOnPduBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2StreamFlowLimitOnPduBytes.setStatus("mandatory")


class _St2StreamFlowLimitOnPduRate_Type(Integer32):
    """Custom type st2StreamFlowLimitOnPduRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_St2StreamFlowLimitOnPduRate_Type.__name__ = "Integer32"
_St2StreamFlowLimitOnPduRate_Object = MibTableColumn
st2StreamFlowLimitOnPduRate = _St2StreamFlowLimitOnPduRate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 87, 1, 23),
    _St2StreamFlowLimitOnPduRate_Type()
)
st2StreamFlowLimitOnPduRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2StreamFlowLimitOnPduRate.setStatus("mandatory")


class _St2StreamFlowMinBytesXRate_Type(Integer32):
    """Custom type st2StreamFlowMinBytesXRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_St2StreamFlowMinBytesXRate_Type.__name__ = "Integer32"
_St2StreamFlowMinBytesXRate_Object = MibTableColumn
st2StreamFlowMinBytesXRate = _St2StreamFlowMinBytesXRate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 87, 1, 24),
    _St2StreamFlowMinBytesXRate_Type()
)
st2StreamFlowMinBytesXRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2StreamFlowMinBytesXRate.setStatus("mandatory")


class _St2StreamFlowMeanDelay_Type(Integer32):
    """Custom type st2StreamFlowMeanDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_St2StreamFlowMeanDelay_Type.__name__ = "Integer32"
_St2StreamFlowMeanDelay_Object = MibTableColumn
st2StreamFlowMeanDelay = _St2StreamFlowMeanDelay_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 87, 1, 25),
    _St2StreamFlowMeanDelay_Type()
)
st2StreamFlowMeanDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2StreamFlowMeanDelay.setStatus("mandatory")


class _St2StreamFlowDelayVariance_Type(Integer32):
    """Custom type st2StreamFlowDelayVariance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_St2StreamFlowDelayVariance_Type.__name__ = "Integer32"
_St2StreamFlowDelayVariance_Object = MibTableColumn
st2StreamFlowDelayVariance = _St2StreamFlowDelayVariance_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 87, 1, 26),
    _St2StreamFlowDelayVariance_Type()
)
st2StreamFlowDelayVariance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2StreamFlowDelayVariance.setStatus("mandatory")


class _St2StreamFlowDesPduBytes_Type(Integer32):
    """Custom type st2StreamFlowDesPduBytes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_St2StreamFlowDesPduBytes_Type.__name__ = "Integer32"
_St2StreamFlowDesPduBytes_Object = MibTableColumn
st2StreamFlowDesPduBytes = _St2StreamFlowDesPduBytes_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 87, 1, 27),
    _St2StreamFlowDesPduBytes_Type()
)
st2StreamFlowDesPduBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2StreamFlowDesPduBytes.setStatus("mandatory")


class _St2StreamFlowDesPduRate_Type(Integer32):
    """Custom type st2StreamFlowDesPduRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_St2StreamFlowDesPduRate_Type.__name__ = "Integer32"
_St2StreamFlowDesPduRate_Object = MibTableColumn
st2StreamFlowDesPduRate = _St2StreamFlowDesPduRate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 87, 1, 28),
    _St2StreamFlowDesPduRate_Type()
)
st2StreamFlowDesPduRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2StreamFlowDesPduRate.setStatus("mandatory")


class _St2StreamOptionPtp_Type(Integer32):
    """Custom type st2StreamOptionPtp based on Integer32"""
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


_St2StreamOptionPtp_Type.__name__ = "Integer32"
_St2StreamOptionPtp_Object = MibTableColumn
st2StreamOptionPtp = _St2StreamOptionPtp_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 87, 1, 29),
    _St2StreamOptionPtp_Type()
)
st2StreamOptionPtp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2StreamOptionPtp.setStatus("mandatory")


class _St2StreamOptionFdx_Type(Integer32):
    """Custom type st2StreamOptionFdx based on Integer32"""
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


_St2StreamOptionFdx_Type.__name__ = "Integer32"
_St2StreamOptionFdx_Object = MibTableColumn
st2StreamOptionFdx = _St2StreamOptionFdx_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 87, 1, 30),
    _St2StreamOptionFdx_Type()
)
st2StreamOptionFdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2StreamOptionFdx.setStatus("mandatory")


class _St2StreamOptionRecover_Type(Integer32):
    """Custom type st2StreamOptionRecover based on Integer32"""
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


_St2StreamOptionRecover_Type.__name__ = "Integer32"
_St2StreamOptionRecover_Object = MibTableColumn
st2StreamOptionRecover = _St2StreamOptionRecover_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 87, 1, 31),
    _St2StreamOptionRecover_Type()
)
st2StreamOptionRecover.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2StreamOptionRecover.setStatus("mandatory")


class _St2StreamOptionReverseCharge_Type(Integer32):
    """Custom type st2StreamOptionReverseCharge based on Integer32"""
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


_St2StreamOptionReverseCharge_Type.__name__ = "Integer32"
_St2StreamOptionReverseCharge_Object = MibTableColumn
st2StreamOptionReverseCharge = _St2StreamOptionReverseCharge_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 87, 1, 32),
    _St2StreamOptionReverseCharge_Type()
)
st2StreamOptionReverseCharge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2StreamOptionReverseCharge.setStatus("mandatory")


class _St2StreamOptionTimestamp_Type(Integer32):
    """Custom type st2StreamOptionTimestamp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_St2StreamOptionTimestamp_Type.__name__ = "Integer32"
_St2StreamOptionTimestamp_Object = MibTableColumn
st2StreamOptionTimestamp = _St2StreamOptionTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 87, 1, 33),
    _St2StreamOptionTimestamp_Type()
)
st2StreamOptionTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2StreamOptionTimestamp.setStatus("mandatory")
_St2HopTable_Object = MibTable
st2HopTable = _St2HopTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 88)
)
if mibBuilder.loadTexts:
    st2HopTable.setStatus("mandatory")
_St2HopEntry_Object = MibTableRow
st2HopEntry = _St2HopEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 88, 1)
)
st2HopEntry.setIndexNames(
    (0, "ST2-MIB", "st2StreamName"),
    (0, "ST2-MIB", "st2StreamPrevHopAddr"),
    (0, "ST2-MIB", "st2StreamPrevHopVlid"),
    (0, "ST2-MIB", "st2HopNeighborAddr"),
)
if mibBuilder.loadTexts:
    st2HopEntry.setStatus("mandatory")


class _St2HopHid_Type(Integer32):
    """Custom type st2HopHid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_St2HopHid_Type.__name__ = "Integer32"
_St2HopHid_Object = MibTableColumn
st2HopHid = _St2HopHid_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 88, 1, 1),
    _St2HopHid_Type()
)
st2HopHid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2HopHid.setStatus("mandatory")


class _St2HopMyVlid_Type(Integer32):
    """Custom type st2HopMyVlid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_St2HopMyVlid_Type.__name__ = "Integer32"
_St2HopMyVlid_Object = MibTableColumn
st2HopMyVlid = _St2HopMyVlid_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 88, 1, 2),
    _St2HopMyVlid_Type()
)
st2HopMyVlid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2HopMyVlid.setStatus("mandatory")


class _St2HopYourVlid_Type(Integer32):
    """Custom type st2HopYourVlid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_St2HopYourVlid_Type.__name__ = "Integer32"
_St2HopYourVlid_Object = MibTableColumn
st2HopYourVlid = _St2HopYourVlid_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 88, 1, 3),
    _St2HopYourVlid_Type()
)
st2HopYourVlid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2HopYourVlid.setStatus("mandatory")


class _St2HopState_Type(Integer32):
    """Custom type st2HopState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("negotiating", 3),
          ("ok", 1),
          ("open", 2))
    )


_St2HopState_Type.__name__ = "Integer32"
_St2HopState_Object = MibTableColumn
st2HopState = _St2HopState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 88, 1, 4),
    _St2HopState_Type()
)
st2HopState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2HopState.setStatus("mandatory")
_St2HopStateTime_Type = TimeTicks
_St2HopStateTime_Object = MibTableColumn
st2HopStateTime = _St2HopStateTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 88, 1, 5),
    _St2HopStateTime_Type()
)
st2HopStateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2HopStateTime.setStatus("mandatory")
_St2HopNumTargets_Type = Gauge32
_St2HopNumTargets_Object = MibTableColumn
st2HopNumTargets = _St2HopNumTargets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 88, 1, 6),
    _St2HopNumTargets_Type()
)
st2HopNumTargets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2HopNumTargets.setStatus("mandatory")
_St2HopMcastAddr_Type = IpAddress
_St2HopMcastAddr_Object = MibTableColumn
st2HopMcastAddr = _St2HopMcastAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 88, 1, 7),
    _St2HopMcastAddr_Type()
)
st2HopMcastAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2HopMcastAddr.setStatus("mandatory")
_St2HopErrorCode_Type = Integer32
_St2HopErrorCode_Object = MibTableColumn
st2HopErrorCode = _St2HopErrorCode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 88, 1, 8),
    _St2HopErrorCode_Type()
)
st2HopErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2HopErrorCode.setStatus("mandatory")
_St2HopDetectorAddr_Type = IpAddress
_St2HopDetectorAddr_Object = MibTableColumn
st2HopDetectorAddr = _St2HopDetectorAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 88, 1, 9),
    _St2HopDetectorAddr_Type()
)
st2HopDetectorAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2HopDetectorAddr.setStatus("mandatory")
_St2HopNeighborAddr_Type = IpAddress
_St2HopNeighborAddr_Object = MibTableColumn
st2HopNeighborAddr = _St2HopNeighborAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 88, 1, 10),
    _St2HopNeighborAddr_Type()
)
st2HopNeighborAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2HopNeighborAddr.setStatus("mandatory")


class _St2HopStreamName_Type(OctetString):
    """Custom type st2HopStreamName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )


_St2HopStreamName_Type.__name__ = "OctetString"
_St2HopStreamName_Object = MibTableColumn
st2HopStreamName = _St2HopStreamName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 88, 1, 11),
    _St2HopStreamName_Type()
)
st2HopStreamName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2HopStreamName.setStatus("mandatory")
_St2HopPkts_Type = Counter32
_St2HopPkts_Object = MibTableColumn
st2HopPkts = _St2HopPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 88, 1, 12),
    _St2HopPkts_Type()
)
st2HopPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2HopPkts.setStatus("mandatory")
_St2HopOctets_Type = Counter32
_St2HopOctets_Object = MibTableColumn
st2HopOctets = _St2HopOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 88, 1, 13),
    _St2HopOctets_Type()
)
st2HopOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2HopOctets.setStatus("mandatory")
_St2HopDiscards_Type = Counter32
_St2HopDiscards_Object = MibTableColumn
st2HopDiscards = _St2HopDiscards_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 88, 1, 14),
    _St2HopDiscards_Type()
)
st2HopDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2HopDiscards.setStatus("mandatory")


class _St2HopIpEncap_Type(Integer32):
    """Custom type st2HopIpEncap based on Integer32"""
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


_St2HopIpEncap_Type.__name__ = "Integer32"
_St2HopIpEncap_Object = MibTableColumn
st2HopIpEncap = _St2HopIpEncap_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 88, 1, 15),
    _St2HopIpEncap_Type()
)
st2HopIpEncap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2HopIpEncap.setStatus("mandatory")
_St2HopIpAddr_Type = IpAddress
_St2HopIpAddr_Object = MibTableColumn
st2HopIpAddr = _St2HopIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 88, 1, 16),
    _St2HopIpAddr_Type()
)
st2HopIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2HopIpAddr.setStatus("mandatory")


class _St2HopRole_Type(Integer32):
    """Custom type st2HopRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nexthop", 1),
          ("prevhop", 2))
    )


_St2HopRole_Type.__name__ = "Integer32"
_St2HopRole_Object = MibTableColumn
st2HopRole = _St2HopRole_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 88, 1, 17),
    _St2HopRole_Type()
)
st2HopRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2HopRole.setStatus("mandatory")
_St2HopInterfaceIndex_Type = Integer32
_St2HopInterfaceIndex_Object = MibTableColumn
st2HopInterfaceIndex = _St2HopInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 88, 1, 18),
    _St2HopInterfaceIndex_Type()
)
st2HopInterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2HopInterfaceIndex.setStatus("mandatory")
_St2HopErrorTime_Type = TimeTicks
_St2HopErrorTime_Object = MibTableColumn
st2HopErrorTime = _St2HopErrorTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 88, 1, 19),
    _St2HopErrorTime_Type()
)
st2HopErrorTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2HopErrorTime.setStatus("mandatory")
_St2NeighborTable_Object = MibTable
st2NeighborTable = _St2NeighborTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 89)
)
if mibBuilder.loadTexts:
    st2NeighborTable.setStatus("mandatory")
_St2NeighborEntry_Object = MibTableRow
st2NeighborEntry = _St2NeighborEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 89, 1)
)
st2NeighborEntry.setIndexNames(
    (0, "ST2-MIB", "st2NeighborAddr"),
)
if mibBuilder.loadTexts:
    st2NeighborEntry.setStatus("mandatory")
_St2NeighborAddr_Type = IpAddress
_St2NeighborAddr_Object = MibTableColumn
st2NeighborAddr = _St2NeighborAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 89, 1, 1),
    _St2NeighborAddr_Type()
)
st2NeighborAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2NeighborAddr.setStatus("mandatory")


class _St2NeighborState_Type(Integer32):
    """Custom type st2NeighborState based on Integer32"""
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


_St2NeighborState_Type.__name__ = "Integer32"
_St2NeighborState_Object = MibTableColumn
st2NeighborState = _St2NeighborState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 89, 1, 2),
    _St2NeighborState_Type()
)
st2NeighborState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2NeighborState.setStatus("mandatory")
_St2NeighborStateTime_Type = TimeTicks
_St2NeighborStateTime_Object = MibTableColumn
st2NeighborStateTime = _St2NeighborStateTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 89, 1, 3),
    _St2NeighborStateTime_Type()
)
st2NeighborStateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2NeighborStateTime.setStatus("mandatory")
_St2NeighborNumHops_Type = Gauge32
_St2NeighborNumHops_Object = MibTableColumn
st2NeighborNumHops = _St2NeighborNumHops_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 89, 1, 4),
    _St2NeighborNumHops_Type()
)
st2NeighborNumHops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2NeighborNumHops.setStatus("mandatory")
_St2NeighborHelloTimer_Type = TimeTicks
_St2NeighborHelloTimer_Object = MibTableColumn
st2NeighborHelloTimer = _St2NeighborHelloTimer_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 89, 1, 5),
    _St2NeighborHelloTimer_Type()
)
st2NeighborHelloTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2NeighborHelloTimer.setStatus("mandatory")
_St2NeighborHelloRcvdTime_Type = TimeTicks
_St2NeighborHelloRcvdTime_Object = MibTableColumn
st2NeighborHelloRcvdTime = _St2NeighborHelloRcvdTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 89, 1, 6),
    _St2NeighborHelloRcvdTime_Type()
)
st2NeighborHelloRcvdTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2NeighborHelloRcvdTime.setStatus("mandatory")
_St2NeighborDataRcvdTime_Type = TimeTicks
_St2NeighborDataRcvdTime_Object = MibTableColumn
st2NeighborDataRcvdTime = _St2NeighborDataRcvdTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 89, 1, 7),
    _St2NeighborDataRcvdTime_Type()
)
st2NeighborDataRcvdTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2NeighborDataRcvdTime.setStatus("mandatory")


class _St2NeighborAckRequested_Type(Integer32):
    """Custom type st2NeighborAckRequested based on Integer32"""
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


_St2NeighborAckRequested_Type.__name__ = "Integer32"
_St2NeighborAckRequested_Object = MibTableColumn
st2NeighborAckRequested = _St2NeighborAckRequested_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 89, 1, 8),
    _St2NeighborAckRequested_Type()
)
st2NeighborAckRequested.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2NeighborAckRequested.setStatus("mandatory")


class _St2NeighborRestarted_Type(Integer32):
    """Custom type st2NeighborRestarted based on Integer32"""
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


_St2NeighborRestarted_Type.__name__ = "Integer32"
_St2NeighborRestarted_Object = MibTableColumn
st2NeighborRestarted = _St2NeighborRestarted_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 89, 1, 9),
    _St2NeighborRestarted_Type()
)
st2NeighborRestarted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2NeighborRestarted.setStatus("mandatory")
_St2NeighborSentHellos_Type = Counter32
_St2NeighborSentHellos_Object = MibTableColumn
st2NeighborSentHellos = _St2NeighborSentHellos_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 89, 1, 10),
    _St2NeighborSentHellos_Type()
)
st2NeighborSentHellos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2NeighborSentHellos.setStatus("mandatory")
_St2NeighborRcvdHellos_Type = Counter32
_St2NeighborRcvdHellos_Object = MibTableColumn
st2NeighborRcvdHellos = _St2NeighborRcvdHellos_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 89, 1, 11),
    _St2NeighborRcvdHellos_Type()
)
st2NeighborRcvdHellos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2NeighborRcvdHellos.setStatus("mandatory")
_St2NeighborMissedHellos_Type = Counter32
_St2NeighborMissedHellos_Object = MibTableColumn
st2NeighborMissedHellos = _St2NeighborMissedHellos_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 89, 1, 12),
    _St2NeighborMissedHellos_Type()
)
st2NeighborMissedHellos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2NeighborMissedHellos.setStatus("mandatory")
_St2NeighborRoundTripTime_Type = TimeTicks
_St2NeighborRoundTripTime_Object = MibTableColumn
st2NeighborRoundTripTime = _St2NeighborRoundTripTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 89, 1, 13),
    _St2NeighborRoundTripTime_Type()
)
st2NeighborRoundTripTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2NeighborRoundTripTime.setStatus("mandatory")
_St2NeighborInterfaceIdx_Type = Integer32
_St2NeighborInterfaceIdx_Object = MibTableColumn
st2NeighborInterfaceIdx = _St2NeighborInterfaceIdx_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 89, 1, 14),
    _St2NeighborInterfaceIdx_Type()
)
st2NeighborInterfaceIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2NeighborInterfaceIdx.setStatus("mandatory")
_St2NeighborStBadMsgs_Type = Counter32
_St2NeighborStBadMsgs_Object = MibTableColumn
st2NeighborStBadMsgs = _St2NeighborStBadMsgs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 89, 1, 15),
    _St2NeighborStBadMsgs_Type()
)
st2NeighborStBadMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2NeighborStBadMsgs.setStatus("mandatory")
_St2NeighborScmpBadMsgs_Type = Counter32
_St2NeighborScmpBadMsgs_Object = MibTableColumn
st2NeighborScmpBadMsgs = _St2NeighborScmpBadMsgs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 89, 1, 16),
    _St2NeighborScmpBadMsgs_Type()
)
st2NeighborScmpBadMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2NeighborScmpBadMsgs.setStatus("mandatory")
_St2TargetTable_Object = MibTable
st2TargetTable = _St2TargetTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 90)
)
if mibBuilder.loadTexts:
    st2TargetTable.setStatus("mandatory")
_St2TargetEntry_Object = MibTableRow
st2TargetEntry = _St2TargetEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 90, 1)
)
st2TargetEntry.setIndexNames(
    (0, "ST2-MIB", "st2StreamName"),
    (0, "ST2-MIB", "st2TargetAddr"),
)
if mibBuilder.loadTexts:
    st2TargetEntry.setStatus("mandatory")
_St2TargetAddr_Type = IpAddress
_St2TargetAddr_Object = MibTableColumn
st2TargetAddr = _St2TargetAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 90, 1, 1),
    _St2TargetAddr_Type()
)
st2TargetAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2TargetAddr.setStatus("mandatory")
_St2TargetHop_Type = IpAddress
_St2TargetHop_Object = MibTableColumn
st2TargetHop = _St2TargetHop_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 90, 1, 2),
    _St2TargetHop_Type()
)
st2TargetHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2TargetHop.setStatus("mandatory")


class _St2TargetStreamName_Type(OctetString):
    """Custom type st2TargetStreamName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )


_St2TargetStreamName_Type.__name__ = "OctetString"
_St2TargetStreamName_Object = MibTableColumn
st2TargetStreamName = _St2TargetStreamName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 90, 1, 3),
    _St2TargetStreamName_Type()
)
st2TargetStreamName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2TargetStreamName.setStatus("mandatory")
_St2GroupTable_Object = MibTable
st2GroupTable = _St2GroupTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 91)
)
if mibBuilder.loadTexts:
    st2GroupTable.setStatus("mandatory")
_St2GroupEntry_Object = MibTableRow
st2GroupEntry = _St2GroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 91, 1)
)
st2GroupEntry.setIndexNames(
    (0, "ST2-MIB", "st2GroupName"),
)
if mibBuilder.loadTexts:
    st2GroupEntry.setStatus("mandatory")


class _St2GroupName_Type(OctetString):
    """Custom type st2GroupName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )


_St2GroupName_Type.__name__ = "OctetString"
_St2GroupName_Object = MibTableColumn
st2GroupName = _St2GroupName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 91, 1, 1),
    _St2GroupName_Type()
)
st2GroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2GroupName.setStatus("mandatory")


class _St2GroupId_Type(Integer32):
    """Custom type st2GroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_St2GroupId_Type.__name__ = "Integer32"
_St2GroupId_Object = MibTableColumn
st2GroupId = _St2GroupId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 91, 1, 2),
    _St2GroupId_Type()
)
st2GroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2GroupId.setStatus("mandatory")
_St2GroupNumStreams_Type = Gauge32
_St2GroupNumStreams_Object = MibTableColumn
st2GroupNumStreams = _St2GroupNumStreams_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 91, 1, 3),
    _St2GroupNumStreams_Type()
)
st2GroupNumStreams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2GroupNumStreams.setStatus("mandatory")
_St2GroupNumSubgroups_Type = Gauge32
_St2GroupNumSubgroups_Object = MibTableColumn
st2GroupNumSubgroups = _St2GroupNumSubgroups_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 91, 1, 4),
    _St2GroupNumSubgroups_Type()
)
st2GroupNumSubgroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2GroupNumSubgroups.setStatus("mandatory")
_St2SubgroupTable_Object = MibTable
st2SubgroupTable = _St2SubgroupTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 92)
)
if mibBuilder.loadTexts:
    st2SubgroupTable.setStatus("mandatory")
_St2SubgroupEntry_Object = MibTableRow
st2SubgroupEntry = _St2SubgroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 92, 1)
)
st2SubgroupEntry.setIndexNames(
    (0, "ST2-MIB", "st2SubgroupIndex"),
)
if mibBuilder.loadTexts:
    st2SubgroupEntry.setStatus("mandatory")


class _St2SubgroupGroup_Type(OctetString):
    """Custom type st2SubgroupGroup based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )


_St2SubgroupGroup_Type.__name__ = "OctetString"
_St2SubgroupGroup_Object = MibTableColumn
st2SubgroupGroup = _St2SubgroupGroup_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 92, 1, 1),
    _St2SubgroupGroup_Type()
)
st2SubgroupGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2SubgroupGroup.setStatus("mandatory")
_St2SubgroupNumStreams_Type = Gauge32
_St2SubgroupNumStreams_Object = MibTableColumn
st2SubgroupNumStreams = _St2SubgroupNumStreams_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 92, 1, 2),
    _St2SubgroupNumStreams_Type()
)
st2SubgroupNumStreams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2SubgroupNumStreams.setStatus("mandatory")


class _St2SubgroupIndex_Type(Integer32):
    """Custom type st2SubgroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_St2SubgroupIndex_Type.__name__ = "Integer32"
_St2SubgroupIndex_Object = MibTableColumn
st2SubgroupIndex = _St2SubgroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 92, 1, 3),
    _St2SubgroupIndex_Type()
)
st2SubgroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2SubgroupIndex.setStatus("mandatory")
_St2InterfaceTable_Object = MibTable
st2InterfaceTable = _St2InterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 93)
)
if mibBuilder.loadTexts:
    st2InterfaceTable.setStatus("mandatory")
_St2InterfaceEntry_Object = MibTableRow
st2InterfaceEntry = _St2InterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 93, 1)
)
st2InterfaceEntry.setIndexNames(
    (0, "ST2-MIB", "st2InterfaceIndex"),
)
if mibBuilder.loadTexts:
    st2InterfaceEntry.setStatus("mandatory")
_St2InterfaceIndex_Type = Integer32
_St2InterfaceIndex_Object = MibTableColumn
st2InterfaceIndex = _St2InterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 93, 1, 1),
    _St2InterfaceIndex_Type()
)
st2InterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2InterfaceIndex.setStatus("mandatory")
_St2InterfaceNumInStreams_Type = Gauge32
_St2InterfaceNumInStreams_Object = MibTableColumn
st2InterfaceNumInStreams = _St2InterfaceNumInStreams_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 93, 1, 2),
    _St2InterfaceNumInStreams_Type()
)
st2InterfaceNumInStreams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2InterfaceNumInStreams.setStatus("mandatory")
_St2InterfaceNumOutStreams_Type = Gauge32
_St2InterfaceNumOutStreams_Object = MibTableColumn
st2InterfaceNumOutStreams = _St2InterfaceNumOutStreams_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 93, 1, 3),
    _St2InterfaceNumOutStreams_Type()
)
st2InterfaceNumOutStreams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2InterfaceNumOutStreams.setStatus("mandatory")
_St2InterfaceNumNeighbors_Type = Gauge32
_St2InterfaceNumNeighbors_Object = MibTableColumn
st2InterfaceNumNeighbors = _St2InterfaceNumNeighbors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 93, 1, 4),
    _St2InterfaceNumNeighbors_Type()
)
st2InterfaceNumNeighbors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2InterfaceNumNeighbors.setStatus("mandatory")
_St2InterfaceInBwReserved_Type = Gauge32
_St2InterfaceInBwReserved_Object = MibTableColumn
st2InterfaceInBwReserved = _St2InterfaceInBwReserved_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 93, 1, 5),
    _St2InterfaceInBwReserved_Type()
)
st2InterfaceInBwReserved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2InterfaceInBwReserved.setStatus("mandatory")
_St2InterfaceInBwReservable_Type = Gauge32
_St2InterfaceInBwReservable_Object = MibTableColumn
st2InterfaceInBwReservable = _St2InterfaceInBwReservable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 93, 1, 6),
    _St2InterfaceInBwReservable_Type()
)
st2InterfaceInBwReservable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    st2InterfaceInBwReservable.setStatus("mandatory")
_St2InterfaceOutBwReserved_Type = Gauge32
_St2InterfaceOutBwReserved_Object = MibTableColumn
st2InterfaceOutBwReserved = _St2InterfaceOutBwReserved_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 93, 1, 7),
    _St2InterfaceOutBwReserved_Type()
)
st2InterfaceOutBwReserved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2InterfaceOutBwReserved.setStatus("mandatory")
_St2InterfaceOutBwReservable_Type = Gauge32
_St2InterfaceOutBwReservable_Object = MibTableColumn
st2InterfaceOutBwReservable = _St2InterfaceOutBwReservable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 93, 1, 8),
    _St2InterfaceOutBwReservable_Type()
)
st2InterfaceOutBwReservable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    st2InterfaceOutBwReservable.setStatus("mandatory")
_St2InterfaceTotRcvdPkts_Type = Counter32
_St2InterfaceTotRcvdPkts_Object = MibTableColumn
st2InterfaceTotRcvdPkts = _St2InterfaceTotRcvdPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 93, 1, 9),
    _St2InterfaceTotRcvdPkts_Type()
)
st2InterfaceTotRcvdPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2InterfaceTotRcvdPkts.setStatus("mandatory")
_St2InterfaceTotSentPkts_Type = Counter32
_St2InterfaceTotSentPkts_Object = MibTableColumn
st2InterfaceTotSentPkts = _St2InterfaceTotSentPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 93, 1, 10),
    _St2InterfaceTotSentPkts_Type()
)
st2InterfaceTotSentPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2InterfaceTotSentPkts.setStatus("mandatory")
_St2InterfaceTotRcvdOctets_Type = Counter32
_St2InterfaceTotRcvdOctets_Object = MibTableColumn
st2InterfaceTotRcvdOctets = _St2InterfaceTotRcvdOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 93, 1, 11),
    _St2InterfaceTotRcvdOctets_Type()
)
st2InterfaceTotRcvdOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2InterfaceTotRcvdOctets.setStatus("mandatory")
_St2InterfaceTotSentOctets_Type = Counter32
_St2InterfaceTotSentOctets_Object = MibTableColumn
st2InterfaceTotSentOctets = _St2InterfaceTotSentOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 93, 1, 12),
    _St2InterfaceTotSentOctets_Type()
)
st2InterfaceTotSentOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2InterfaceTotSentOctets.setStatus("mandatory")
_St2InterfaceRcvdHdrErrors_Type = Counter32
_St2InterfaceRcvdHdrErrors_Object = MibTableColumn
st2InterfaceRcvdHdrErrors = _St2InterfaceRcvdHdrErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 93, 1, 13),
    _St2InterfaceRcvdHdrErrors_Type()
)
st2InterfaceRcvdHdrErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2InterfaceRcvdHdrErrors.setStatus("mandatory")
_St2InterfaceRcvdHidErrors_Type = Counter32
_St2InterfaceRcvdHidErrors_Object = MibTableColumn
st2InterfaceRcvdHidErrors = _St2InterfaceRcvdHidErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 93, 1, 14),
    _St2InterfaceRcvdHidErrors_Type()
)
st2InterfaceRcvdHidErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2InterfaceRcvdHidErrors.setStatus("mandatory")
_St2InterfaceRcvdLenErrors_Type = Counter32
_St2InterfaceRcvdLenErrors_Object = MibTableColumn
st2InterfaceRcvdLenErrors = _St2InterfaceRcvdLenErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 93, 1, 15),
    _St2InterfaceRcvdLenErrors_Type()
)
st2InterfaceRcvdLenErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2InterfaceRcvdLenErrors.setStatus("mandatory")
_St2InterfaceRcvdHdrErrorTime_Type = TimeTicks
_St2InterfaceRcvdHdrErrorTime_Object = MibTableColumn
st2InterfaceRcvdHdrErrorTime = _St2InterfaceRcvdHdrErrorTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 93, 1, 16),
    _St2InterfaceRcvdHdrErrorTime_Type()
)
st2InterfaceRcvdHdrErrorTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2InterfaceRcvdHdrErrorTime.setStatus("mandatory")
_St2InterfaceRcvdHidErrorTime_Type = TimeTicks
_St2InterfaceRcvdHidErrorTime_Object = MibTableColumn
st2InterfaceRcvdHidErrorTime = _St2InterfaceRcvdHidErrorTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 93, 1, 17),
    _St2InterfaceRcvdHidErrorTime_Type()
)
st2InterfaceRcvdHidErrorTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2InterfaceRcvdHidErrorTime.setStatus("mandatory")
_St2InterfaceRcvdLenErrorTime_Type = TimeTicks
_St2InterfaceRcvdLenErrorTime_Object = MibTableColumn
st2InterfaceRcvdLenErrorTime = _St2InterfaceRcvdLenErrorTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 93, 1, 18),
    _St2InterfaceRcvdLenErrorTime_Type()
)
st2InterfaceRcvdLenErrorTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2InterfaceRcvdLenErrorTime.setStatus("mandatory")
_St2InterfaceRcvdErrorSnap_Type = DisplayString
_St2InterfaceRcvdErrorSnap_Object = MibTableColumn
st2InterfaceRcvdErrorSnap = _St2InterfaceRcvdErrorSnap_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 93, 1, 19),
    _St2InterfaceRcvdErrorSnap_Type()
)
st2InterfaceRcvdErrorSnap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2InterfaceRcvdErrorSnap.setStatus("mandatory")
_St2InterfaceRcvdPktDrops_Type = Counter32
_St2InterfaceRcvdPktDrops_Object = MibTableColumn
st2InterfaceRcvdPktDrops = _St2InterfaceRcvdPktDrops_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 93, 1, 20),
    _St2InterfaceRcvdPktDrops_Type()
)
st2InterfaceRcvdPktDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2InterfaceRcvdPktDrops.setStatus("mandatory")
_St2InterfaceSentPktDrops_Type = Counter32
_St2InterfaceSentPktDrops_Object = MibTableColumn
st2InterfaceSentPktDrops = _St2InterfaceSentPktDrops_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 93, 1, 21),
    _St2InterfaceSentPktDrops_Type()
)
st2InterfaceSentPktDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2InterfaceSentPktDrops.setStatus("mandatory")
_St2InterfaceIpAddr_Type = IpAddress
_St2InterfaceIpAddr_Object = MibTableColumn
st2InterfaceIpAddr = _St2InterfaceIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 93, 1, 22),
    _St2InterfaceIpAddr_Type()
)
st2InterfaceIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2InterfaceIpAddr.setStatus("mandatory")


class _St2LastCloseStreamName_Type(OctetString):
    """Custom type st2LastCloseStreamName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )


_St2LastCloseStreamName_Type.__name__ = "OctetString"
_St2LastCloseStreamName_Object = MibScalar
st2LastCloseStreamName = _St2LastCloseStreamName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 94),
    _St2LastCloseStreamName_Type()
)
st2LastCloseStreamName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2LastCloseStreamName.setStatus("mandatory")
_St2LastClosePrevHopIpAddr_Type = IpAddress
_St2LastClosePrevHopIpAddr_Object = MibScalar
st2LastClosePrevHopIpAddr = _St2LastClosePrevHopIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 95),
    _St2LastClosePrevHopIpAddr_Type()
)
st2LastClosePrevHopIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2LastClosePrevHopIpAddr.setStatus("mandatory")
_St2LastCloseReasonCode_Type = Integer32
_St2LastCloseReasonCode_Object = MibScalar
st2LastCloseReasonCode = _St2LastCloseReasonCode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 96),
    _St2LastCloseReasonCode_Type()
)
st2LastCloseReasonCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2LastCloseReasonCode.setStatus("mandatory")
_St2LastCloseDetectorIpAddress_Type = IpAddress
_St2LastCloseDetectorIpAddress_Object = MibScalar
st2LastCloseDetectorIpAddress = _St2LastCloseDetectorIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 97),
    _St2LastCloseDetectorIpAddress_Type()
)
st2LastCloseDetectorIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2LastCloseDetectorIpAddress.setStatus("mandatory")
_St2LastCloseTime_Type = TimeTicks
_St2LastCloseTime_Object = MibScalar
st2LastCloseTime = _St2LastCloseTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 5, 98),
    _St2LastCloseTime_Type()
)
st2LastCloseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st2LastCloseTime.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ST2-MIB",
    **{"stii": stii,
       "st2AgentCopyright": st2AgentCopyright,
       "st2ProtoVersion": st2ProtoVersion,
       "st2FlowSpecVersion": st2FlowSpecVersion,
       "st2AgentType": st2AgentType,
       "st2RoutingDerived": st2RoutingDerived,
       "st2ToAccept": st2ToAccept,
       "st2NAccept": st2NAccept,
       "st2ToConnect": st2ToConnect,
       "st2NConnect": st2NConnect,
       "st2ToDisconnect": st2ToDisconnect,
       "st2NDisconnect": st2NDisconnect,
       "st2ToHidAck": st2ToHidAck,
       "st2NHidAck": st2NHidAck,
       "st2ToHidChange": st2ToHidChange,
       "st2NHidChange": st2NHidChange,
       "st2ToNotify": st2ToNotify,
       "st2NNotify": st2NNotify,
       "st2ToRefuse": st2ToRefuse,
       "st2NRefuse": st2NRefuse,
       "st2ToReroute": st2ToReroute,
       "st2NReroute": st2NReroute,
       "st2ToEnd2End": st2ToEnd2End,
       "st2NEnd2End": st2NEnd2End,
       "st2NHidAbort": st2NHidAbort,
       "st2HelloTimerHoldDown": st2HelloTimerHoldDown,
       "st2HelloLossFactor": st2HelloLossFactor,
       "st2DefaultRecoveryTimeout": st2DefaultRecoveryTimeout,
       "st2DefaultHelloFactor": st2DefaultHelloFactor,
       "st2ScmpRcvdOctets": st2ScmpRcvdOctets,
       "st2ScmpSentOctets": st2ScmpSentOctets,
       "st2ScmpRcvdBadTypes": st2ScmpRcvdBadTypes,
       "st2ScmpRcvdBadCks": st2ScmpRcvdBadCks,
       "st2ScmpSentAccepts": st2ScmpSentAccepts,
       "st2ScmpSentAcks": st2ScmpSentAcks,
       "st2ScmpSentChanges": st2ScmpSentChanges,
       "st2ScmpSentChangeReqs": st2ScmpSentChangeReqs,
       "st2ScmpSentConnects": st2ScmpSentConnects,
       "st2ScmpSentDisconnects": st2ScmpSentDisconnects,
       "st2ScmpSentErrorInReqs": st2ScmpSentErrorInReqs,
       "st2ScmpSentErrorInResps": st2ScmpSentErrorInResps,
       "st2ScmpSentHellos": st2ScmpSentHellos,
       "st2ScmpSentHidApproves": st2ScmpSentHidApproves,
       "st2ScmpSentHidChanges": st2ScmpSentHidChanges,
       "st2ScmpSentHidChangeReqs": st2ScmpSentHidChangeReqs,
       "st2ScmpSentHidRejects": st2ScmpSentHidRejects,
       "st2ScmpSentNotifys": st2ScmpSentNotifys,
       "st2ScmpSentRefuses": st2ScmpSentRefuses,
       "st2ScmpSentStatus": st2ScmpSentStatus,
       "st2ScmpSentStatusResps": st2ScmpSentStatusResps,
       "st2ScmpRcvdAccepts": st2ScmpRcvdAccepts,
       "st2ScmpRcvdAcks": st2ScmpRcvdAcks,
       "st2ScmpRcvdChanges": st2ScmpRcvdChanges,
       "st2ScmpRcvdChangeReqs": st2ScmpRcvdChangeReqs,
       "st2ScmpRcvdConnects": st2ScmpRcvdConnects,
       "st2ScmpRcvdDisconnects": st2ScmpRcvdDisconnects,
       "st2ScmpRcvdErrorInReqs": st2ScmpRcvdErrorInReqs,
       "st2ScmpRcvdErrorInResps": st2ScmpRcvdErrorInResps,
       "st2ScmpRcvdHellos": st2ScmpRcvdHellos,
       "st2ScmpRcvdHidApproves": st2ScmpRcvdHidApproves,
       "st2ScmpRcvdHidChanges": st2ScmpRcvdHidChanges,
       "st2ScmpRcvdHidChangeReqs": st2ScmpRcvdHidChangeReqs,
       "st2ScmpRcvdHidRejects": st2ScmpRcvdHidRejects,
       "st2ScmpRcvdNotifys": st2ScmpRcvdNotifys,
       "st2ScmpRcvdRefuses": st2ScmpRcvdRefuses,
       "st2ScmpRcvdStatus": st2ScmpRcvdStatus,
       "st2ScmpRcvdStatusResps": st2ScmpRcvdStatusResps,
       "st2ScmpRcvdErrorSnap": st2ScmpRcvdErrorSnap,
       "st2ScmpRcvdBadTypeTime": st2ScmpRcvdBadTypeTime,
       "st2ScmpRcvdBadCksTime": st2ScmpRcvdBadCksTime,
       "st2OriginOpens": st2OriginOpens,
       "st2IntermedOpens": st2IntermedOpens,
       "st2TargetOpens": st2TargetOpens,
       "st2FailOpens": st2FailOpens,
       "st2AcceptTimeouts": st2AcceptTimeouts,
       "st2ParamChangeFails": st2ParamChangeFails,
       "st2NumStreamEntries": st2NumStreamEntries,
       "st2NumOpenStreams": st2NumOpenStreams,
       "st2NumOpenOriginStreams": st2NumOpenOriginStreams,
       "st2NumHops": st2NumHops,
       "st2NumNeighbors": st2NumNeighbors,
       "st2NumTargets": st2NumTargets,
       "st2NumGroups": st2NumGroups,
       "st2NumSubgroups": st2NumSubgroups,
       "st2RouteFailures": st2RouteFailures,
       "st2RouteLoops": st2RouteLoops,
       "st2ScmpRetrans": st2ScmpRetrans,
       "st2StreamTable": st2StreamTable,
       "st2StreamEntry": st2StreamEntry,
       "st2StreamName": st2StreamName,
       "st2StreamPrevHopAddr": st2StreamPrevHopAddr,
       "st2StreamPrevHopVlid": st2StreamPrevHopVlid,
       "st2StreamStartTime": st2StreamStartTime,
       "st2StreamState": st2StreamState,
       "st2StreamStateTime": st2StreamStateTime,
       "st2StreamRole": st2StreamRole,
       "st2StreamGroup": st2StreamGroup,
       "st2StreamNumSubgroups": st2StreamNumSubgroups,
       "st2StreamNumNextHops": st2StreamNumNextHops,
       "st2StreamNumTargets": st2StreamNumTargets,
       "st2StreamRefuses": st2StreamRefuses,
       "st2StreamFlowspecChanges": st2StreamFlowspecChanges,
       "st2StreamFlowPrecedence": st2StreamFlowPrecedence,
       "st2StreamFlowDutyFactor": st2StreamFlowDutyFactor,
       "st2StreamFlowErrorRate": st2StreamFlowErrorRate,
       "st2StreamFlowReliability": st2StreamFlowReliability,
       "st2StreamFlowTradeoffs": st2StreamFlowTradeoffs,
       "st2StreamFlowRecoveryTimeout": st2StreamFlowRecoveryTimeout,
       "st2StreamFlowLimitOnCost": st2StreamFlowLimitOnCost,
       "st2StreamFlowLimitOnDelay": st2StreamFlowLimitOnDelay,
       "st2StreamFlowLimitOnPduBytes": st2StreamFlowLimitOnPduBytes,
       "st2StreamFlowLimitOnPduRate": st2StreamFlowLimitOnPduRate,
       "st2StreamFlowMinBytesXRate": st2StreamFlowMinBytesXRate,
       "st2StreamFlowMeanDelay": st2StreamFlowMeanDelay,
       "st2StreamFlowDelayVariance": st2StreamFlowDelayVariance,
       "st2StreamFlowDesPduBytes": st2StreamFlowDesPduBytes,
       "st2StreamFlowDesPduRate": st2StreamFlowDesPduRate,
       "st2StreamOptionPtp": st2StreamOptionPtp,
       "st2StreamOptionFdx": st2StreamOptionFdx,
       "st2StreamOptionRecover": st2StreamOptionRecover,
       "st2StreamOptionReverseCharge": st2StreamOptionReverseCharge,
       "st2StreamOptionTimestamp": st2StreamOptionTimestamp,
       "st2HopTable": st2HopTable,
       "st2HopEntry": st2HopEntry,
       "st2HopHid": st2HopHid,
       "st2HopMyVlid": st2HopMyVlid,
       "st2HopYourVlid": st2HopYourVlid,
       "st2HopState": st2HopState,
       "st2HopStateTime": st2HopStateTime,
       "st2HopNumTargets": st2HopNumTargets,
       "st2HopMcastAddr": st2HopMcastAddr,
       "st2HopErrorCode": st2HopErrorCode,
       "st2HopDetectorAddr": st2HopDetectorAddr,
       "st2HopNeighborAddr": st2HopNeighborAddr,
       "st2HopStreamName": st2HopStreamName,
       "st2HopPkts": st2HopPkts,
       "st2HopOctets": st2HopOctets,
       "st2HopDiscards": st2HopDiscards,
       "st2HopIpEncap": st2HopIpEncap,
       "st2HopIpAddr": st2HopIpAddr,
       "st2HopRole": st2HopRole,
       "st2HopInterfaceIndex": st2HopInterfaceIndex,
       "st2HopErrorTime": st2HopErrorTime,
       "st2NeighborTable": st2NeighborTable,
       "st2NeighborEntry": st2NeighborEntry,
       "st2NeighborAddr": st2NeighborAddr,
       "st2NeighborState": st2NeighborState,
       "st2NeighborStateTime": st2NeighborStateTime,
       "st2NeighborNumHops": st2NeighborNumHops,
       "st2NeighborHelloTimer": st2NeighborHelloTimer,
       "st2NeighborHelloRcvdTime": st2NeighborHelloRcvdTime,
       "st2NeighborDataRcvdTime": st2NeighborDataRcvdTime,
       "st2NeighborAckRequested": st2NeighborAckRequested,
       "st2NeighborRestarted": st2NeighborRestarted,
       "st2NeighborSentHellos": st2NeighborSentHellos,
       "st2NeighborRcvdHellos": st2NeighborRcvdHellos,
       "st2NeighborMissedHellos": st2NeighborMissedHellos,
       "st2NeighborRoundTripTime": st2NeighborRoundTripTime,
       "st2NeighborInterfaceIdx": st2NeighborInterfaceIdx,
       "st2NeighborStBadMsgs": st2NeighborStBadMsgs,
       "st2NeighborScmpBadMsgs": st2NeighborScmpBadMsgs,
       "st2TargetTable": st2TargetTable,
       "st2TargetEntry": st2TargetEntry,
       "st2TargetAddr": st2TargetAddr,
       "st2TargetHop": st2TargetHop,
       "st2TargetStreamName": st2TargetStreamName,
       "st2GroupTable": st2GroupTable,
       "st2GroupEntry": st2GroupEntry,
       "st2GroupName": st2GroupName,
       "st2GroupId": st2GroupId,
       "st2GroupNumStreams": st2GroupNumStreams,
       "st2GroupNumSubgroups": st2GroupNumSubgroups,
       "st2SubgroupTable": st2SubgroupTable,
       "st2SubgroupEntry": st2SubgroupEntry,
       "st2SubgroupGroup": st2SubgroupGroup,
       "st2SubgroupNumStreams": st2SubgroupNumStreams,
       "st2SubgroupIndex": st2SubgroupIndex,
       "st2InterfaceTable": st2InterfaceTable,
       "st2InterfaceEntry": st2InterfaceEntry,
       "st2InterfaceIndex": st2InterfaceIndex,
       "st2InterfaceNumInStreams": st2InterfaceNumInStreams,
       "st2InterfaceNumOutStreams": st2InterfaceNumOutStreams,
       "st2InterfaceNumNeighbors": st2InterfaceNumNeighbors,
       "st2InterfaceInBwReserved": st2InterfaceInBwReserved,
       "st2InterfaceInBwReservable": st2InterfaceInBwReservable,
       "st2InterfaceOutBwReserved": st2InterfaceOutBwReserved,
       "st2InterfaceOutBwReservable": st2InterfaceOutBwReservable,
       "st2InterfaceTotRcvdPkts": st2InterfaceTotRcvdPkts,
       "st2InterfaceTotSentPkts": st2InterfaceTotSentPkts,
       "st2InterfaceTotRcvdOctets": st2InterfaceTotRcvdOctets,
       "st2InterfaceTotSentOctets": st2InterfaceTotSentOctets,
       "st2InterfaceRcvdHdrErrors": st2InterfaceRcvdHdrErrors,
       "st2InterfaceRcvdHidErrors": st2InterfaceRcvdHidErrors,
       "st2InterfaceRcvdLenErrors": st2InterfaceRcvdLenErrors,
       "st2InterfaceRcvdHdrErrorTime": st2InterfaceRcvdHdrErrorTime,
       "st2InterfaceRcvdHidErrorTime": st2InterfaceRcvdHidErrorTime,
       "st2InterfaceRcvdLenErrorTime": st2InterfaceRcvdLenErrorTime,
       "st2InterfaceRcvdErrorSnap": st2InterfaceRcvdErrorSnap,
       "st2InterfaceRcvdPktDrops": st2InterfaceRcvdPktDrops,
       "st2InterfaceSentPktDrops": st2InterfaceSentPktDrops,
       "st2InterfaceIpAddr": st2InterfaceIpAddr,
       "st2LastCloseStreamName": st2LastCloseStreamName,
       "st2LastClosePrevHopIpAddr": st2LastClosePrevHopIpAddr,
       "st2LastCloseReasonCode": st2LastCloseReasonCode,
       "st2LastCloseDetectorIpAddress": st2LastCloseDetectorIpAddress,
       "st2LastCloseTime": st2LastCloseTime}
)
