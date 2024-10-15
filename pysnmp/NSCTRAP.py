# SNMP MIB module (NSCTRAP) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NSCTRAP
# Produced by pysmi-1.5.4 at Mon Oct 14 22:29:33 2024
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

(ifDescr,
 ifIndex,
 ifType) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifDescr",
    "ifIndex",
    "ifType")

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
 NotificationType,
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
    "NotificationType",
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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Nsc_ObjectIdentity = ObjectIdentity
nsc = _Nsc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10)
)
_NscMib_ObjectIdentity = ObjectIdentity
nscMib = _NscMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10, 2)
)
_NscManagement_ObjectIdentity = ObjectIdentity
nscManagement = _NscManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10, 2, 2)
)
_NscTraps_ObjectIdentity = ObjectIdentity
nscTraps = _NscTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10, 2, 2, 4)
)


class _NscTrapsProtBindIndex_Type(Integer32):
    """Custom type nscTrapsProtBindIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("appleTalk", 3),
          ("bridging", 9),
          ("bridgingEc", 10),
          ("decnet", 2),
          ("ip", 1),
          ("ipx", 4),
          ("xns", 5))
    )


_NscTrapsProtBindIndex_Type.__name__ = "Integer32"
_NscTrapsProtBindIndex_Object = MibScalar
nscTrapsProtBindIndex = _NscTrapsProtBindIndex_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 2, 4, 1),
    _NscTrapsProtBindIndex_Type()
)
nscTrapsProtBindIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nscTrapsProtBindIndex.setStatus("mandatory")


class _NscTrapsFddiSMTCFState_Type(Integer32):
    """Custom type nscTrapsFddiSMTCFState based on Integer32"""
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
        *(("cf0", 1),
          ("cf1", 2),
          ("cf2", 3),
          ("cf3", 4),
          ("cf4", 5),
          ("cf5", 6))
    )


_NscTrapsFddiSMTCFState_Type.__name__ = "Integer32"
_NscTrapsFddiSMTCFState_Object = MibScalar
nscTrapsFddiSMTCFState = _NscTrapsFddiSMTCFState_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 2, 4, 2),
    _NscTrapsFddiSMTCFState_Type()
)
nscTrapsFddiSMTCFState.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nscTrapsFddiSMTCFState.setStatus("mandatory")


class _NscTrapsDecNetAreaNbr_Type(OctetString):
    """Custom type nscTrapsDecNetAreaNbr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_NscTrapsDecNetAreaNbr_Type.__name__ = "OctetString"
_NscTrapsDecNetAreaNbr_Object = MibScalar
nscTrapsDecNetAreaNbr = _NscTrapsDecNetAreaNbr_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 2, 4, 3),
    _NscTrapsDecNetAreaNbr_Type()
)
nscTrapsDecNetAreaNbr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nscTrapsDecNetAreaNbr.setStatus("mandatory")


class _NscTrapsDecNetNodeNbr_Type(OctetString):
    """Custom type nscTrapsDecNetNodeNbr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_NscTrapsDecNetNodeNbr_Type.__name__ = "OctetString"
_NscTrapsDecNetNodeNbr_Object = MibScalar
nscTrapsDecNetNodeNbr = _NscTrapsDecNetNodeNbr_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 2, 4, 4),
    _NscTrapsDecNetNodeNbr_Type()
)
nscTrapsDecNetNodeNbr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nscTrapsDecNetNodeNbr.setStatus("mandatory")


class _NscTrapsDecNetCircuitName_Type(DisplayString):
    """Custom type nscTrapsDecNetCircuitName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_NscTrapsDecNetCircuitName_Type.__name__ = "DisplayString"
_NscTrapsDecNetCircuitName_Object = MibScalar
nscTrapsDecNetCircuitName = _NscTrapsDecNetCircuitName_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 2, 4, 5),
    _NscTrapsDecNetCircuitName_Type()
)
nscTrapsDecNetCircuitName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nscTrapsDecNetCircuitName.setStatus("mandatory")


class _NscTrapsDecNetEventReason_Type(DisplayString):
    """Custom type nscTrapsDecNetEventReason based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )


_NscTrapsDecNetEventReason_Type.__name__ = "DisplayString"
_NscTrapsDecNetEventReason_Object = MibScalar
nscTrapsDecNetEventReason = _NscTrapsDecNetEventReason_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 2, 4, 6),
    _NscTrapsDecNetEventReason_Type()
)
nscTrapsDecNetEventReason.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nscTrapsDecNetEventReason.setStatus("mandatory")


class _NscTrapsDecNetReachStatus_Type(Integer32):
    """Custom type nscTrapsDecNetReachStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("reachable", 1),
          ("unreachable", 2))
    )


_NscTrapsDecNetReachStatus_Type.__name__ = "Integer32"
_NscTrapsDecNetReachStatus_Object = MibScalar
nscTrapsDecNetReachStatus = _NscTrapsDecNetReachStatus_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 2, 4, 7),
    _NscTrapsDecNetReachStatus_Type()
)
nscTrapsDecNetReachStatus.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nscTrapsDecNetReachStatus.setStatus("mandatory")


class _NscTrapsVcpPortName_Type(DisplayString):
    """Custom type nscTrapsVcpPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_NscTrapsVcpPortName_Type.__name__ = "DisplayString"
_NscTrapsVcpPortName_Object = MibScalar
nscTrapsVcpPortName = _NscTrapsVcpPortName_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 2, 4, 8),
    _NscTrapsVcpPortName_Type()
)
nscTrapsVcpPortName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nscTrapsVcpPortName.setStatus("mandatory")


class _NscTrapsVcpLogicalState_Type(DisplayString):
    """Custom type nscTrapsVcpLogicalState based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_NscTrapsVcpLogicalState_Type.__name__ = "DisplayString"
_NscTrapsVcpLogicalState_Object = MibScalar
nscTrapsVcpLogicalState = _NscTrapsVcpLogicalState_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 2, 4, 9),
    _NscTrapsVcpLogicalState_Type()
)
nscTrapsVcpLogicalState.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nscTrapsVcpLogicalState.setStatus("mandatory")


class _NscTrapsVcpPhysicalState_Type(DisplayString):
    """Custom type nscTrapsVcpPhysicalState based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_NscTrapsVcpPhysicalState_Type.__name__ = "DisplayString"
_NscTrapsVcpPhysicalState_Object = MibScalar
nscTrapsVcpPhysicalState = _NscTrapsVcpPhysicalState_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 2, 4, 10),
    _NscTrapsVcpPhysicalState_Type()
)
nscTrapsVcpPhysicalState.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nscTrapsVcpPhysicalState.setStatus("mandatory")

# Managed Objects groups


# Notification objects

protocolBound = NotificationType(
    (1, 3, 6, 1, 4, 1, 10, 2, 2, 4, 0, 1)
)
protocolBound.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifType"),
        ("NSCTRAP", "nscTrapsProtBindIndex"))
)
if mibBuilder.loadTexts:
    protocolBound.setStatus(
        ""
    )

protocolUnbound = NotificationType(
    (1, 3, 6, 1, 4, 1, 10, 2, 2, 4, 0, 2)
)
protocolUnbound.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifType"),
        ("NSCTRAP", "nscTrapsProtBindIndex"))
)
if mibBuilder.loadTexts:
    protocolUnbound.setStatus(
        ""
    )

physicalLinkUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 10, 2, 2, 4, 0, 3)
)
physicalLinkUp.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifType"))
)
if mibBuilder.loadTexts:
    physicalLinkUp.setStatus(
        ""
    )

physicalLinkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 10, 2, 2, 4, 0, 4)
)
physicalLinkDown.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifType"))
)
if mibBuilder.loadTexts:
    physicalLinkDown.setStatus(
        ""
    )

fddiWrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 10, 2, 2, 4, 0, 5)
)
fddiWrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("NSCTRAP", "nscTrapsFddiSMTCFState"))
)
if mibBuilder.loadTexts:
    fddiWrap.setStatus(
        ""
    )

vcpActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 10, 2, 2, 4, 0, 6)
)
vcpActive.setObjects(
      *(("NSCTRAP", "nscTrapsVcpPortName"),
        ("NSCTRAP", "nscTrapsVcpLogicalState"),
        ("NSCTRAP", "nscTrapsVcpPhysicalState"))
)
if mibBuilder.loadTexts:
    vcpActive.setStatus(
        ""
    )

vcpInactive = NotificationType(
    (1, 3, 6, 1, 4, 1, 10, 2, 2, 4, 0, 7)
)
vcpInactive.setObjects(
      *(("NSCTRAP", "nscTrapsVcpPortName"),
        ("NSCTRAP", "nscTrapsVcpLogicalState"),
        ("NSCTRAP", "nscTrapsVcpPhysicalState"))
)
if mibBuilder.loadTexts:
    vcpInactive.setStatus(
        ""
    )

vcpReconfig = NotificationType(
    (1, 3, 6, 1, 4, 1, 10, 2, 2, 4, 0, 8)
)
vcpReconfig.setObjects(
      *(("NSCTRAP", "nscTrapsVcpPortName"),
        ("NSCTRAP", "nscTrapsVcpLogicalState"),
        ("NSCTRAP", "nscTrapsVcpPhysicalState"))
)
if mibBuilder.loadTexts:
    vcpReconfig.setStatus(
        ""
    )

vcpBroken = NotificationType(
    (1, 3, 6, 1, 4, 1, 10, 2, 2, 4, 0, 9)
)
vcpBroken.setObjects(
      *(("NSCTRAP", "nscTrapsVcpPortName"),
        ("NSCTRAP", "nscTrapsVcpLogicalState"),
        ("NSCTRAP", "nscTrapsVcpPhysicalState"))
)
if mibBuilder.loadTexts:
    vcpBroken.setStatus(
        ""
    )

vcpMisconfigured = NotificationType(
    (1, 3, 6, 1, 4, 1, 10, 2, 2, 4, 0, 10)
)
vcpMisconfigured.setObjects(
    ("NSCTRAP", "nscTrapsVcpPortName")
)
if mibBuilder.loadTexts:
    vcpMisconfigured.setStatus(
        ""
    )

decNetCircDownFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 10, 2, 2, 4, 0, 407)
)
decNetCircDownFault.setObjects(
      *(("NSCTRAP", "nscTrapsDecNetAreaNbr"),
        ("NSCTRAP", "nscTrapsDecNetNodeNbr"),
        ("NSCTRAP", "nscTrapsDecNetCircuitName"),
        ("NSCTRAP", "nscTrapsDecNetEventReason"))
)
if mibBuilder.loadTexts:
    decNetCircDownFault.setStatus(
        ""
    )

decNetCircDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 10, 2, 2, 4, 0, 408)
)
decNetCircDown.setObjects(
      *(("NSCTRAP", "nscTrapsDecNetAreaNbr"),
        ("NSCTRAP", "nscTrapsDecNetNodeNbr"),
        ("NSCTRAP", "nscTrapsDecNetCircuitName"),
        ("NSCTRAP", "nscTrapsDecNetEventReason"))
)
if mibBuilder.loadTexts:
    decNetCircDown.setStatus(
        ""
    )

decNetCircUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 10, 2, 2, 4, 0, 410)
)
decNetCircUp.setObjects(
      *(("NSCTRAP", "nscTrapsDecNetAreaNbr"),
        ("NSCTRAP", "nscTrapsDecNetNodeNbr"),
        ("NSCTRAP", "nscTrapsDecNetCircuitName"))
)
if mibBuilder.loadTexts:
    decNetCircUp.setStatus(
        ""
    )

decNetNodeReachChg = NotificationType(
    (1, 3, 6, 1, 4, 1, 10, 2, 2, 4, 0, 414)
)
decNetNodeReachChg.setObjects(
      *(("NSCTRAP", "nscTrapsDecNetNodeNbr"),
        ("NSCTRAP", "nscTrapsDecNetReachStatus"))
)
if mibBuilder.loadTexts:
    decNetNodeReachChg.setStatus(
        ""
    )

decNetAdjUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 10, 2, 2, 4, 0, 415)
)
decNetAdjUp.setObjects(
      *(("NSCTRAP", "nscTrapsDecNetAreaNbr"),
        ("NSCTRAP", "nscTrapsDecNetNodeNbr"),
        ("NSCTRAP", "nscTrapsDecNetCircuitName"))
)
if mibBuilder.loadTexts:
    decNetAdjUp.setStatus(
        ""
    )

decNetAdjRejected = NotificationType(
    (1, 3, 6, 1, 4, 1, 10, 2, 2, 4, 0, 416)
)
decNetAdjRejected.setObjects(
      *(("NSCTRAP", "nscTrapsDecNetAreaNbr"),
        ("NSCTRAP", "nscTrapsDecNetNodeNbr"),
        ("NSCTRAP", "nscTrapsDecNetCircuitName"),
        ("NSCTRAP", "nscTrapsDecNetEventReason"))
)
if mibBuilder.loadTexts:
    decNetAdjRejected.setStatus(
        ""
    )

decNetAreaReachChg = NotificationType(
    (1, 3, 6, 1, 4, 1, 10, 2, 2, 4, 0, 417)
)
decNetAreaReachChg.setObjects(
      *(("NSCTRAP", "nscTrapsDecNetAreaNbr"),
        ("NSCTRAP", "nscTrapsDecNetReachStatus"))
)
if mibBuilder.loadTexts:
    decNetAreaReachChg.setStatus(
        ""
    )

decNetAdjDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 10, 2, 2, 4, 0, 418)
)
decNetAdjDown.setObjects(
      *(("NSCTRAP", "nscTrapsDecNetAreaNbr"),
        ("NSCTRAP", "nscTrapsDecNetNodeNbr"),
        ("NSCTRAP", "nscTrapsDecNetCircuitName"),
        ("NSCTRAP", "nscTrapsDecNetEventReason"))
)
if mibBuilder.loadTexts:
    decNetAdjDown.setStatus(
        ""
    )

decNetDesignatedRouter = NotificationType(
    (1, 3, 6, 1, 4, 1, 10, 2, 2, 4, 0, 422)
)
decNetDesignatedRouter.setObjects(
      *(("NSCTRAP", "nscTrapsDecNetAreaNbr"),
        ("NSCTRAP", "nscTrapsDecNetNodeNbr"),
        ("NSCTRAP", "nscTrapsDecNetCircuitName"))
)
if mibBuilder.loadTexts:
    decNetDesignatedRouter.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NSCTRAP",
    **{"nsc": nsc,
       "nscMib": nscMib,
       "nscManagement": nscManagement,
       "nscTraps": nscTraps,
       "protocolBound": protocolBound,
       "protocolUnbound": protocolUnbound,
       "physicalLinkUp": physicalLinkUp,
       "physicalLinkDown": physicalLinkDown,
       "fddiWrap": fddiWrap,
       "vcpActive": vcpActive,
       "vcpInactive": vcpInactive,
       "vcpReconfig": vcpReconfig,
       "vcpBroken": vcpBroken,
       "vcpMisconfigured": vcpMisconfigured,
       "decNetCircDownFault": decNetCircDownFault,
       "decNetCircDown": decNetCircDown,
       "decNetCircUp": decNetCircUp,
       "decNetNodeReachChg": decNetNodeReachChg,
       "decNetAdjUp": decNetAdjUp,
       "decNetAdjRejected": decNetAdjRejected,
       "decNetAreaReachChg": decNetAreaReachChg,
       "decNetAdjDown": decNetAdjDown,
       "decNetDesignatedRouter": decNetDesignatedRouter,
       "nscTrapsProtBindIndex": nscTrapsProtBindIndex,
       "nscTrapsFddiSMTCFState": nscTrapsFddiSMTCFState,
       "nscTrapsDecNetAreaNbr": nscTrapsDecNetAreaNbr,
       "nscTrapsDecNetNodeNbr": nscTrapsDecNetNodeNbr,
       "nscTrapsDecNetCircuitName": nscTrapsDecNetCircuitName,
       "nscTrapsDecNetEventReason": nscTrapsDecNetEventReason,
       "nscTrapsDecNetReachStatus": nscTrapsDecNetReachStatus,
       "nscTrapsVcpPortName": nscTrapsVcpPortName,
       "nscTrapsVcpLogicalState": nscTrapsVcpLogicalState,
       "nscTrapsVcpPhysicalState": nscTrapsVcpPhysicalState}
)
